# Gestionnaire de modèles neutre — CIVITAS Agent

> Complète [`01-architecture-cible-civitas-agent.md`](./01-architecture-cible-civitas-agent.md)
> §10 ("Interfaces (ports) pour rester remplaçable"), qui anticipait ce chantier sans encore le
> réaliser. Fait suite à une remarque explicite : **le modèle utilisé par CIVITAS ne sera pas
> toujours Gemini** — ce document décrit le gestionnaire de modèles neutre qui en découle,
> vivant entièrement dans `services/civitas-agent/app/models/`.

---

## 1. Pourquoi deux surfaces, pas une seule

Le CIVITAS Agent fait appel à un modèle IA à deux endroits **fonctionnellement différents**, qui
n'ont pas à partager le même fournisseur ni la même configuration :

| Surface | Rôle | Nœud/module concerné |
|---|---|---|
| **Moteur de parole** (`models.speech`) | Session temps réel bidirectionnelle : écoute l'audio des participants, comprend, décide de répondre et parle — fusion VAD+ASR+génération+TTS (doc 00 §4.1) | `app/speech/gemini_live.py`, `app/models/speech/openai_realtime.py`, pilotés par le nœud `act` (doc 01 §6) |
| **Modèle de raisonnement** (`models.reasoning`) | Décide, en texte, quels outils du catalogue (doc 02) appeler en complément de la réponse conversationnelle | nœud `reason` (`app/graph/nodes/reasoning.py`, doc 01 §6) |

Un déploiement peut par exemple garder Gemini Live pour la voix (latence minimale, fusion déjà
éprouvée) tout en confiant la sélection d'outils à un modèle différent — ou l'inverse. Les deux
sont **indépendamment configurables** et **indépendamment optionnels au sens fournisseur** :
seul le moteur de parole est obligatoire au fonctionnement de l'agent, le modèle de
raisonnement reste une amélioration facultative (repli sur l'heuristique historique si absent,
doc 00 §5.6).

---

## 2. Principe d'architecture — aucun SDK de fournisseur hors de `app/models/`

Règle stricte, vérifiable par une simple recherche dans le code : **aucun module en dehors de
`app/models/` n'importe `google.genai`, `openai` ou `anthropic`.** Tout accès passe par une
factory :

```
app/main.py
    │
    │ build_speech_engine(settings, ...)          — app/models/speech/factory.py
    │ build_reasoning_model(settings)              — app/models/reasoning/factory.py
    ▼
Settings.SPEECH_MODEL_PROVIDER / REASONING_MODEL_PROVIDER   (app/config.py)
    │
    ▼
implémentation concrète, instanciée à la demande, jamais importée avant d'être sélectionnée
```

C'est la même logique de "port" déjà utilisée pour `tools/registry.py` (doc 01 §9) : le reste
du CIVITAS Agent (graphe, outils, browser) ne connaît que les interfaces
(`app/speech/engine.py::SpeechEngine`, `app/models/reasoning/base.py::ReasoningModel`), jamais
une implémentation précise. Ajouter un quatrième fournisseur ne modifie donc **jamais**
`app/main.py` ni `app/graph/`.

---

## 3. Configuration — variables d'environnement (`app/config.py`)

```
# Moteur de parole (obligatoire)
SPEECH_MODEL_PROVIDER=gemini_live        # "gemini_live" | "openai_realtime"
SPEECH_MODEL_NAME=gemini-2.5-flash-native-audio-preview-12-2025
SPEECH_MODEL_API_KEY=
SPEECH_MODEL_VOICE=Aoede
SPEECH_MODEL_LANGUAGE=fr
SPEECH_MODEL_EXTRA={}                    # JSON libre, paramètres propres au fournisseur

# Modèle de raisonnement (optionnel — vide = heuristique historique conservée)
REASONING_MODEL_PROVIDER=                # "" | "gemini" | "openai" | "anthropic"
REASONING_MODEL_NAME=
REASONING_MODEL_API_KEY=
REASONING_MODEL_EXTRA={}
```

`SPEECH_MODEL_EXTRA`/`REASONING_MODEL_EXTRA` sont l'échappatoire volontaire pour tout paramètre
propre à un fournisseur qui ne mérite pas sa propre variable d'environnement dédiée (ex: un
réglage `turn_detection` spécifique à OpenAI Realtime, ou un `temperature` pour un fournisseur
de raisonnement) — parsé en JSON avec dégradation gracieuse sur valeur invalide
(`Settings.speech_model_extra()`/`reasoning_model_extra()`, jamais une exception qui
empêcherait le démarrage pour un paramètre secondaire mal formé).

**Compatibilité ascendante** : `GEMINI_API_KEY` (nom historique) est repris automatiquement en
repli si `SPEECH_MODEL_API_KEY` est vide, avec un avertissement loggé — cf. `app/config.py`,
`Settings._backward_compat_gemini_api_key`. Les déploiements existants continuent de fonctionner
sans modification immédiate de leur `.env`.

---

## 4. Moteur de parole — `app/models/speech/`

### 4.1 Fournisseurs disponibles aujourd'hui

| Provider | Implémentation | Statut |
|---|---|---|
| `gemini_live` (défaut) | `app/speech/gemini_live.py` (`GeminiSession`) | ✅ Complet, porté depuis `services/peer`, testé (cf. doc 04) |
| `openai_realtime` | `app/models/speech/openai_realtime.py` (`OpenAIRealtimeEngine`) | ✅ Implémenté et groundé contre la documentation officielle OpenAI (endpoint WebSocket, événements client/serveur GA) — **non testé en conditions réelles** (pas de clé API OpenAI ni de vrai Jitsi dans l'environnement où ce module a été écrit, cf. doc 04) ; `send_image` lève explicitement `NotImplementedError` (format non confirmé, jamais deviné) |

### 4.2 Débits d'échantillonnage — désormais paramétrés, jamais figés en dur

Différence concrète entre fournisseurs qui aurait pu casser silencieusement un changement de
provider : Gemini Live attend du PCM **16kHz** en entrée et produit du **24kHz** en sortie ;
l'API Realtime OpenAI (GA) attend et produit du PCM **24kHz** dans les deux sens. L'interface
`SpeechEngine` (`app/speech/engine.py`) déclare donc `input_sample_rate`/`output_sample_rate`
comme propriétés que chaque implémentation doit exposer, et :

- `app/browser/driver.py` (`AUDIO_BRIDGE_JS`) accepte désormais ces deux débits en paramètres
  d'injection au lieu de `16000`/`24000` codés en dur dans le script JS.
- `app/main.py` construit `CivitasBrowser` en lui passant
  `speech_engine.input_sample_rate`/`output_sample_rate`, lus dynamiquement sur l'instance
  réellement construite par la factory — jamais supposés.

C'est la condition nécessaire pour que "changer `SPEECH_MODEL_PROVIDER`" soit réellement une
bascule complète, pas seulement côté Python.

### 4.3 Ajouter un nouveau fournisseur de moteur de parole

1. Créer `app/models/speech/<fournisseur>.py`, implémentant le contrat `SpeechEngine`
   (`app/speech/engine.py`) : `start`, `stop`, `send_audio`, `send_text`, `send_image`,
   `input_sample_rate`, `output_sample_rate`.
2. Ajouter une branche dans `app/models/speech/factory.py::build_speech_engine`.
3. Documenter le débit d'échantillonnage réel du fournisseur — jamais supposer 16k/24k.
4. Si une capacité n'est pas supportée par ce fournisseur (ex: vision), lever
   `NotImplementedError` explicitement plutôt que de simuler un succès — même principe que les
   outils P1 du catalogue (doc 02 §11).

---

## 5. Modèle de raisonnement — `app/models/reasoning/`

### 5.1 Fournisseurs disponibles aujourd'hui

| Provider | Implémentation | API sous-jacente |
|---|---|---|
| `gemini` | `app/models/reasoning/gemini_text.py` | `google-genai`, `generate_content` (texte, PAS Gemini Live) |
| `openai` | `app/models/reasoning/openai_chat.py` | `openai`, Chat Completions avec `response_format={"type":"json_object"}` (JSON strict natif) |
| `anthropic` | `app/models/reasoning/anthropic_chat.py` | `anthropic`, Messages API |

### 5.2 Contrat commun — sortie JSON stricte, parsing défensif

Les 3 implémentations partagent `app/models/reasoning/base.py` :

- `build_prompt(system, context, available_tools, user_message)` — construit un prompt unique
  incluant uniquement les outils **réellement implémentés** du registre de CETTE room
  (`ToolRegistry.describe()`, doc 01 §9), avec une consigne de sortie JSON stricte
  (`{"say": ..., "tool_calls": [...]}`).
- `parse_completion(raw_text)` — **ne lève jamais d'exception**, quelle que soit la réponse du
  modèle (JSON invalide, texte parasite, bloc Markdown ` ```json ` ajouté malgré la consigne) :
  une réponse mal formée produit `{"say": None, "tool_calls": []}`, jamais un crash.

### 5.3 Aucune confiance implicite accordée au modèle de raisonnement

Point de sécurité central, à ne jamais retirer si ce module évolue : chaque `tool_call` proposé
par le modèle de raisonnement retraverse **intégralement** le gating de permissions du nœud
`act` (`app/graph/nodes/acting.py` → `ToolRegistry.invoke`, doc 01 §9) avant tout effet réel. Un
modèle de raisonnement mal configuré, qui hallucine un nom d'outil, ou qui propose un outil hors
`tools_allowed`, ne peut **jamais** provoquer une action non autorisée — au pire un refus
loggé, exactement comme pour l'heuristique historique.

### 5.4 Dégradation gracieuse — jamais bloquant

```
REASONING_MODEL_PROVIDER vide                → reason garde l'heuristique seule (doc 00 §5.6)
provider configuré, clé API absente          → averti, repli sur l'heuristique
provider configuré, SDK non installé         → averti, repli sur l'heuristique
provider configuré, appel réseau en échec    → capturé dans reason(), repli sur cette invocation
réponse du modèle mal formée                 → parse_completion() → tool_calls=[]
```

À chaque étage, le pire cas possible est "pas de raisonnement outillé supplémentaire pour ce
tour" — jamais un agent qui ne répond plus du tout, ni un graphe qui plante.

### 5.5 Ajouter un nouveau fournisseur de raisonnement

1. Créer `app/models/reasoning/<fournisseur>.py`, implémentant `ReasoningModel.decide(...)` via
   `build_prompt`/`parse_completion` partagés.
2. Ajouter une branche dans `app/models/reasoning/factory.py::build_reasoning_model`, à
   l'intérieur du `try/except ImportError` déjà en place (dégradation gracieuse automatique si
   le SDK manque).

---

## 6. Statut et tests

Testé dans cette session (cf. `services/civitas-agent/tests/`) :

- `test_models_reasoning_base.py` — construction de prompt, parsing défensif (y compris sur
  entrée délibérément invalide).
- `test_models_reasoning_factory.py` — sélection de fournisseur, repli sur `None` si
  fournisseur vide/inconnu/clé absente/**SDK réellement absent** (exécuté dans un environnement
  où aucun des 3 SDK n'est installé — ce test valide donc un vrai chemin de dégradation, pas
  une simulation).
- `test_models_speech_factory.py` — fournisseur inconnu (`ValueError`), SDK manquant pour
  `gemini_live` (`RuntimeError` explicite plutôt qu'un `ImportError` brut).

Non testé en conditions réelles (nécessite l'environnement de déploiement réel, cf. doc 04) :
une session `OpenAIRealtimeEngine` contre une vraie clé API OpenAI et un vrai flux audio Jitsi ;
un appel réel à `GeminiReasoningModel`/`OpenAIReasoningModel`/`AnthropicReasoningModel` contre
les API respectives. C'est, comme pour le reste de la Phase 1, le travail restant avant bascule
vers la Phase 2 du plan de migration (doc 04).
