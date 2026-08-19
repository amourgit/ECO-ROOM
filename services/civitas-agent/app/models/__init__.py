"""
Gestionnaire de modèles neutre du CIVITAS Agent — cf.
docs/architecture/05-gestionnaire-de-modeles.md.

Deux surfaces distinctes, chacune avec son propre registre de fournisseurs configurable par
variables d'environnement (app/config.py) :

  - `models.speech`    — moteur de parole temps réel (Data Plane, doc 00 §4.1). Fournisseurs :
                          "gemini_live" (défaut), "openai_realtime".
  - `models.reasoning` — modèle de raisonnement texte pour la sélection d'outils (doc 01 §6,
                          nœud `reason`). Fournisseurs : "gemini", "openai", "anthropic".
                          Optionnel — vide par défaut, le nœud `reason` garde alors son
                          heuristique historique (doc 00 §5.6).

Aucun code en dehors de ce package ne doit importer directement un SDK de fournisseur
(`google.genai`, `openai`, `anthropic`) — tout accès passe par les factories
(`models.speech.factory.build_speech_engine`, `models.reasoning.factory.build_reasoning_model`),
seul point de couplage entre la configuration (app/config.py) et l'implémentation choisie.
"""
