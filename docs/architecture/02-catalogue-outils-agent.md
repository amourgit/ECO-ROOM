# Catalogue exhaustif des outils du CIVITAS Agent

> Objectif explicite de ce document : **tout ce qu'un participant humain peut faire dans
> l'interface Jitsi Meet doit avoir un outil CIVITAS Agent correspondant**, quand un équivalent
> a un sens pour un agent (certaines actions humaines — partage d'écran vidéo, flou d'arrière-plan
> — n'ont pas d'équivalent significatif pour un bot sans caméra ; elles sont listées et
> explicitement justifiées comme non applicables plutôt que silencieusement omises).
>
> **Méthode de vérification** : le `peer` actuel pilote Jitsi via
> `window.APP.conference._room`, c'est-à-dire l'instance `JitsiConference` de `lib-jitsi-meet`
> exposée par l'app React de Jitsi Meet (doc 00 §2.2). La liste des méthodes ci-dessous a été
> confrontée à l'interface **`IJitsiConference`** réellement déclarée dans le code source de
> `jitsi-meet` (`react/features/base/conference/reducer.ts`, version vendée récente), pas
> reconstituée de mémoire — chaque outil indique la méthode réelle utilisée. Quelques
> mécanismes (sondages, breakout rooms, partage de fichiers) exposent une méthode de lecture
> mais pas une méthode d'écriture unique documentée publiquement : ils sont marqués
> **"à valider contre la version déployée"** plutôt que présentés comme certains — pas de détail
> inventé.

---

## 0. Légende

| Statut | Signification |
|---|---|
| ✅ Existe déjà | Implémenté dans `services/peer/app/browser/browser.py`, à porter tel quel |
| 🆕 À implémenter (P0) | Nouveau, méthode `JitsiConference` confirmée, effort faible/moyen — cible du MVP |
| 🔧 À implémenter (P1) | Nouveau, mécanisme plus complexe (payload JSON à confirmer, UI additionnelle) — cible post-MVP |
| 📖 Lecture seule | Capacité d'observation utile au raisonnement, pas une "action" |
| 🚫 Non applicable | Pas d'équivalent significatif pour un agent sans caméra/écran à partager |

Chaque outil est nommé `module.fonction`, correspondant au fichier `app/tools/<module>.py` du
CIVITAS Agent (doc 01 §8).

---

## 1. `chat_tools` — communication écrite

| Action humaine | Outil CIVITAS Agent | Mécanisme réel | Statut | Notes |
|---|---|---|---|---|
| Écrire dans le chat de groupe | `chat_tools.send_chat(text)` | Aujourd'hui : `SEND_MESSAGE` Redux. Cible : `JitsiConference.sendTextMessage(text)` (méthode officielle équivalente, à privilégier pour rester sur l'API `lib-jitsi-meet` plutôt que sur un détail d'implémentation Redux) | ✅ Existe déjà | Conservé, migration douce vers `sendTextMessage` recommandée mais non bloquante |
| Écrire un message privé à un participant | `chat_tools.send_private_chat(participant_id, text)` | `JitsiConference.sendPrivateTextMessage(participant_id, text)` | 🆕 P0 | Utile pour une réponse ciblée sans polluer le chat de groupe |
| Envoyer une réaction (👍😂👏 etc.) | `chat_tools.send_reaction(emoji)` | `JitsiConference.sendReaction(reaction)` | 🆕 P0 | Permet à l'agent d'accuser réception sans interrompre à la voix |
| Envoyer des tonalités DTMF (pavé téléphonique) | `chat_tools.send_tones(tones)` | `JitsiConference.sendTones(tones, duration, pause)` | 🔧 P1 | Utile seulement si un pont téléphonique (dial-in) est utilisé |
| Envoyer un feedback de fin d'appel | `chat_tools.send_feedback(score, text)` | `JitsiConference.sendFeedback(overallFeedback, detailedFeedback)` | 🔧 P1 | Peu pertinent pour un agent qui ne "vit" pas la fin d'appel comme un humain — bas de la pile |

---

## 2. `presence_tools` — état de présence de l'agent lui-même

| Action humaine | Outil CIVITAS Agent | Mécanisme réel | Statut | Notes |
|---|---|---|---|---|
| Lever la main | `presence_tools.raise_hand()` | `JitsiConference.setLocalParticipantProperty('raisedHand', <timestamp>)` | 🆕 P0 | Convention de valeur (booléen vs timestamp) **à valider contre la version déployée** — le code actuel écoute déjà `PARTICIPANT_PROPERTY_CHANGED` sur `raisedHand` en lecture (doc 00 §5.5), il ne l'écrit jamais |
| Baisser la main | `presence_tools.lower_hand()` | `JitsiConference.setLocalParticipantProperty('raisedHand', false)` | 🆕 P0 | — |
| Changer son propre nom affiché | `presence_tools.set_display_name(name)` | `JitsiConference.setDisplayName(name)` | 🆕 P0 | Permet par ex. de refléter dynamiquement le mode (`CIVITAS 🔇 silencieux`) |
| Se rendre "silencieux" au sens protocole (bot/enregistreur) | `presence_tools.set_silent(bool)` | `JitsiConference.setIsSilent(bool)` | 🔧 P1 | Mécanisme normalement réservé aux bots système (ex: transcripteur) ; à évaluer si pertinent pour CIVITAS ou si `behavior_mode="silent"` (déjà existant, applicatif) suffit |
| Couper son propre micro | `presence_tools.mute_self_audio()` | **Pas un équivalent direct `track.mute()`** — cf. note ci-dessous | 🆕 P0 (comportement applicatif) | Voir §2.1 |
| Réactiver son propre micro | `presence_tools.unmute_self_audio()` | idem | 🆕 P0 | idem |
| Choisir la langue de transcription reçue | `presence_tools.set_transcription_language(lang)` | `JitsiConference.setTranscriptionLanguage(lang)` | 🔧 P1 | Utile en réunion multilingue |
| Choisir la langue de traduction reçue | `presence_tools.set_receiver_translation_language(lang)` | `JitsiConference.setReceiverTranslationLanguage(lang)` | 🔧 P1 | Dépend du composant de traduction audio (`audioTranslation`, vu dans `IConferenceMetadata`) — à confirmer déployé ou non |

### 2.1 Note importante — "couper le micro" de l'agent n'est pas symétrique à un humain

L'agent n'a pas de `JitsiLocalTrack` micro classique : sa voix sortante est un flux PCM de
synthèse (Gemini Live) injecté via `replaceTrack()` sur un track de substitution en
permanence présent (doc 00 §4.1). "Se couper le micro" pour CIVITAS ne peut donc pas être un
`track.mute()` au sens Jitsi (qui couperait un flux qui, techniquement, ne porte que du
silence tant que l'agent ne parle pas) — c'est un **comportement applicatif** : arrêter de
transmettre les buffers audio de Gemini vers `AudioPipe` (mécanisme déjà présent aujourd'hui,
`ResponseMode.TEXT` bloque déjà `_on_gemini_audio`, doc 00 §5.6). `mute_self_audio()` /
`unmute_self_audio()` sont donc des outils qui pilotent `response_mode` côté CIVITAS Agent, pas
un appel `JitsiConference`. Documenté explicitement ici pour éviter qu'une future
implémentation ne cherche, à tort, un `track.mute()` inexistant côté agent.

---

## 3. `moderation_tools` — actions sur les autres participants (requièrent `can_moderate`)

| Action humaine | Outil CIVITAS Agent | Mécanisme réel | Statut | Notes |
|---|---|---|---|---|
| Exclure un participant | `moderation_tools.kick_participant(id, reason)` | `JitsiConference.kickParticipant(id, reason)` | ✅ Existe déjà | Conservé tel quel, doc 00 §5.4 |
| Couper le micro d'un participant | `moderation_tools.mute_participant(id)` | `JitsiConference.muteParticipant(id, 'audio')` | ✅ Existe déjà | Ne peut jamais réactiver à sa place (restriction Jitsi standard, déjà documentée) |
| Accorder les droits de modérateur | `moderation_tools.grant_moderator(id)` | `JitsiConference.grantOwner(id)` | 🆕 P0 | Nécessite déjà que l'agent soit lui-même modérateur |
| Lire le statut modérateur de l'agent | `moderation_tools.get_moderator_status()` | `JitsiParticipant.getRole()` sur `myUserId()` | ✅ Existe déjà | Conservé tel quel |
| Vérifier le rôle réel du peer avant toute action | (interne au registre, doc 01 §9) | `getRole()` | ✅ Existe déjà | Pattern "vérifier avant d'agir" généralisé à tous les outils de modération |
| Activer la modération audio/vidéo (AV moderation) | `moderation_tools.enable_av_moderation(media_type)` | `JitsiConference.enableAVModeration(mediaType)` | 🆕 P0 | Force tous les participants (hors modérateurs) à demander l'autorisation avant d'activer micro/caméra |
| Désactiver la modération AV | `moderation_tools.disable_av_moderation(media_type)` | `JitsiConference.disableAVModeration(mediaType)` | 🆕 P0 | — |
| Vérifier si la modération AV est supportée | `moderation_tools.is_av_moderation_supported()` | `JitsiConference.isAVModerationSupported()` | 📖 Lecture seule | À consulter avant d'activer |
| Approuver une demande de prise de parole (AV moderation) | `moderation_tools.approve_unmute_request(participant_id, media_type)` | `JitsiConference.avModerationApprove(mediaType, participantId)` | 🆕 P0 | Équivalent du bouton "autoriser" côté UI Jitsi quand la modération AV est active |
| Refuser une demande de prise de parole | `moderation_tools.reject_unmute_request(participant_id, media_type)` | `JitsiConference.avModerationReject(mediaType, participantId)` | 🆕 P0 | — |
| Activer la salle d'attente (lobby) | `moderation_tools.enable_lobby()` | `JitsiConference.enableLobby()` | 🆕 P0 | — |
| Désactiver la salle d'attente | `moderation_tools.disable_lobby()` | `JitsiConference.disableLobby()` | 🆕 P0 | — |
| Admettre un participant en salle d'attente | `moderation_tools.lobby_approve_access(id)` | `JitsiConference.lobbyApproveAccess(id)` | 🆕 P0 | Permet à CIVITAS de jouer un rôle d'accueil automatisé |
| Refuser un participant en salle d'attente | `moderation_tools.lobby_deny_access(id)` | `JitsiConference.lobbyDenyAccess(id)` | 🆕 P0 | — |
| Envoyer un message à quelqu'un en salle d'attente | `moderation_tools.send_lobby_message(id, text)` | `JitsiConference.sendLobbyMessage(...)` | 🔧 P1 | — |
| Vérifier le support de la salle d'attente sur ce déploiement | `moderation_tools.is_lobby_supported()` | `JitsiConference.isLobbySupported()` | 📖 Lecture seule | — |
| Définir la politique de démarrage muet | `room_tools.set_start_muted_policy(audio, video)` | `JitsiConference.setStartMutedPolicy({audio, video})` | 🆕 P1 | Classé aussi bien modération que réglage de room — placé ici car c'est une action à droits de modérateur |

---

## 4. `room_tools` — réglages de la réunion (requièrent `can_moderate`, sauf mention contraire)

| Action humaine | Outil CIVITAS Agent | Mécanisme réel | Statut | Notes |
|---|---|---|---|---|
| Changer le sujet de la réunion | `room_tools.set_subject(text)` | `JitsiConference.setSubject(text)` | 🆕 P0 | Déjà **capté en lecture** (`SUBJECT_CHANGED`, doc 00 §5.5) ; il manquait l'écriture |
| Verrouiller la room (mot de passe) | `room_tools.lock_room(password)` | `JitsiConference.lock(password)` | 🆕 P0 | Déjà **capté en lecture** (`LOCK_STATE_CHANGED`) ; il manquait l'écriture |
| Déverrouiller la room | `room_tools.unlock_room()` | `JitsiConference.lock(null)` (ou méthode `unlock` équivalente selon version) | 🆕 P0 | À valider : certaines versions exposent `unlock()` séparément |
| Terminer la réunion pour tout le monde | `room_tools.end_meeting()` | `JitsiConference.end()` | 🆕 P0 | Vérifier au préalable `isEndConferenceSupported()` |
| Vérifier si "terminer pour tous" est supporté | `room_tools.is_end_conference_supported()` | `JitsiConference.isEndConferenceSupported()` | 📖 Lecture seule | — |
| Activer le chiffrement de bout en bout (E2EE) | `room_tools.toggle_e2ee(enabled)` | `JitsiConference.toggleE2EE(enabled)` | 🔧 P1 | Impact fort sur l'agent lui-même : si E2EE est actif, la clé doit être partagée (`setMediaEncryptionKey`) — sujet sensible, à traiter avec soin, pas un simple toggle isolé |
| Consulter si l'E2EE est actif/supporté | `room_tools.get_e2ee_status()` | `isE2EEEnabled()` / `isE2EESupported()` | 📖 Lecture seule | — |
| Composer un numéro / inviter par téléphone (dial-out) | `room_tools.dial(number)` | `JitsiConference.dial(number)` | 🔧 P1 | Nécessite une passerelle SIP configurée côté Jitsi — dépend du déploiement |
| Créer une session de passerelle SIP vidéo | `room_tools.create_sip_gateway_session(...)` | `JitsiConference.createVideoSIPGWSession(...)` | 🔧 P1 | Avancé, dépend de `jigasi`/infra SIP — non prioritaire |
| Vérifier si les appels SIP sont supportés | `room_tools.is_sip_calling_supported()` | `JitsiConference.isSIPCallingSupported()` | 📖 Lecture seule | — |
| Lister/consulter les breakout rooms | `room_tools.get_breakout_rooms()` | `JitsiConference.getBreakoutRooms()` | 📖 Lecture seule | Confirmé pris en charge côté infra (`mod_muc_breakout_rooms.lua` présent dans le vendoring Jitsi) |
| Créer / assigner / fermer des breakout rooms | `room_tools.manage_breakout_rooms(...)` | mécanisme XMPP dédié (composant breakout rooms), pas une méthode unique de `IJitsiConference` | 🔧 P1 — **à valider contre la version déployée** | Fonctionnalité réelle et supportée par l'infra vendée, mais le câblage exact (messages XMPP/JSON) doit être vérifié dans le bundle JS déployé avant implémentation — ne pas deviner le format |

---

## 5. `media_tools` — enregistrement, transcription, bande passante

| Action humaine | Outil CIVITAS Agent | Mécanisme réel | Statut | Notes |
|---|---|---|---|---|
| Démarrer l'enregistrement (fichier) | `media_tools.start_recording(mode="file")` | `JitsiConference.startRecording({mode: 'file', ...})` | 🆕 P0 | Nécessite Jibri configuré côté infra Jitsi — dépend du déploiement, pas de CIVITAS |
| Démarrer le streaming live (YouTube etc.) | `media_tools.start_recording(mode="stream", stream_key=...)` | `JitsiConference.startRecording({mode: 'stream', ...})` | 🔧 P1 | Idem, dépend de Jibri + clé de stream fournie par l'appelant |
| Arrêter l'enregistrement/streaming | `media_tools.stop_recording(mode)` | `JitsiConference.stopRecording(mode)` | 🆕 P0 | — |
| Consulter le statut de transcription | `media_tools.get_transcription_status()` | `JitsiConference.getTranscriptionStatus()` | 📖 Lecture seule | Transcription native Jitsi (Jigasi), distincte de la transcription Gemini Live interne à CIVITAS |
| Ajuster la bande passante estimée | `media_tools.set_assumed_bandwidth(bps)` | `JitsiConference.setAssumedBandwidthBps(bps)` | 🚫 Non applicable | Réglage réseau bas niveau, sans rapport avec un comportement "métier" de l'agent |
| Ajuster la fréquence d'images du partage d'écran | `media_tools.set_desktop_sharing_frame_rate(fps)` | `JitsiConference.setDesktopSharingFrameRate(fps)` | 🚫 Non applicable | L'agent ne partage jamais son écran (§6) |
| Contraintes de réception vidéo | — | `setReceiverConstraints` | 🚫 Non applicable | L'agent ne rend jamais de vidéo (headless, pas d'affichage) |
| Contraintes d'émission vidéo | — | `setSenderVideoConstraint` | 🚫 Non applicable | L'agent n'émet jamais de vidéo |

---

## 6. Actions vidéo / affichage — non applicables, avec justification explicite

Ces actions existent bien pour un participant humain mais **n'ont pas d'équivalent significatif**
pour un agent headless sans caméra ni rendu d'écran — elles sont listées pour être exhaustif,
pas omises silencieusement :

| Action humaine | Pourquoi non applicable à CIVITAS v1 |
|---|---|
| Activer/couper sa caméra | L'agent ne possède aucune source vidéo (`config.startWithVideoMuted=true` en dur, doc 00 §4.2) |
| Flou d'arrière-plan / fond virtuel | Nécessite un flux caméra en entrée — inexistant |
| Partager son écran | Nécessite une source `desktop`/`screen` côté navigateur headless (Playwright peut théoriquement le faire via un flux synthétique canvas → `createLocalTracks({video: {mediaSource: 'desktop'}})`, mais c'est un chantier à part entière : générer un contenu visuel utile — ex: un tableau de bord, une diapositive récapitulative — puis l'encoder comme track vidéo). **Piste d'extension future documentée** (`media_tools.share_generated_visual`) mais **hors périmètre de cette phase** |
| Épingler un participant / vue mosaïque | Pur choix de rendu local de l'UI React, sans effet serveur — n'a aucun sens pour un process qui ne rend jamais d'interface |
| Vérification E2EE visuelle (comparaison de code de sécurité) | `startVerification()`/`markParticipantVerified()` existent dans l'API mais concernent une vérification humaine de bout en bout — pas d'équivalent utile pour un agent automatisé |

---

## 7. `vision_tools` — perception visuelle (hors `IJitsiConference`, propre à CIVITAS)

| Capacité | Outil CIVITAS Agent | Mécanisme | Statut | Notes |
|---|---|---|---|---|
| Capturer l'écran de la réunion (ce que "voit" l'agent) | `vision_tools.capture_frame()` | `page.screenshot()` (Playwright) | ✅ Existe déjà | Conservé tel quel (doc 00 §4.2) |
| Décrire ce qui est visible | `vision_tools.describe_screen(prompt)` | `capture_frame()` + `SpeechEngine.send_image()` (Gemini vision) | ✅ Existe déjà | Déclenché aujourd'hui uniquement par mot-clé ; devient un outil appelable directement par le nœud `reason` (doc 01 §4.3) |
| Lire un document partagé à l'écran (OCR/compréhension) | `vision_tools.read_shared_content(prompt)` | même mécanisme que `describe_screen`, prompt orienté extraction | 🆕 P1 | Cas d'usage : lire un tableau de chiffres partagé, en extraire une valeur |

---

## 8. `platform_tools` — domaine 4 (CIVITAS Platform), pas Jitsi

Ces outils n'ont pas d'équivalent "action humaine dans Jitsi" — ils correspondent au §11 de la
note d'architecture d'origine (l'agent peut appeler la plateforme CIVITAS elle-même) :

| Outil | Rôle |
|---|---|
| `platform_tools.get_user(user_id)` | Récupère le profil d'un utilisateur CIVITAS (au-delà du simple `display_name` Jitsi) |
| `platform_tools.get_meeting(meeting_id)` | Métadonnées métier d'une réunion (au-delà de `room_id`) |
| `platform_tools.get_document(document_id)` | Récupère un document métier (ex: ordre du jour) |
| `platform_tools.create_task(payload)` | Crée une tâche de suivi issue de la réunion |
| `platform_tools.create_minutes(payload)` | Génère/enregistre un compte-rendu structuré |
| `platform_tools.create_vote(payload)` | Initialise un vote métier (distinct des sondages Jitsi natifs, §9) |

Tous soumis à `permissions.can_use_tools` + `tools_allowed` (doc 01 §9). Implémentation en
`Phase 2+` du plan de migration (doc 04) — ce sont des APIs métier qui n'existent pas encore
dans le dépôt, contrairement aux outils Jitsi ci-dessus qui portent tous sur une capacité déjà
présente côté infrastructure.

---

## 9. `rag_tools` — base de connaissances (nouveau, Qdrant)

| Outil | Rôle |
|---|---|
| `rag_tools.query_knowledge_base(query, knowledge_base_id)` | Recherche sémantique dans les documents indexés (doc 01 §7) |

Soumis à `permissions.can_use_rag`. Nécessite le pipeline d'ingestion documentaire (MinIO →
extraction → embedding → Qdrant, doc 01 §7 / doc 04 Phase 3) — non existant aujourd'hui,
correctement isolé comme nouveauté plutôt que présenté comme un portage.

---

## 10. Capacités de lecture pure (📖) — alimentent `ingest_data_event`/`update_state`

Toutes déjà couvertes en pratique par `JITSI_EVENTS_JS` + `SpeakerTracker` (doc 00 §5.2, §5.5),
listées ici pour rattacher explicitement chaque capacité `IJitsiConference` correspondante :

`getParticipants` / `getParticipantById` / `getParticipantCount` → alimentent
`ConferenceAgentState.participants`. `getRole` → rôle courant. `getSpeakerStats` → statistiques
de prise de parole cumulées (angle mort actuel : `SpeakerTracker` ne garde que le locuteur
*courant*, pas de cumul historique par participant — piste d'amélioration `Phase 2`).
`getMeetingUniqueId` / `getName` → identité de la conférence. `myUserId` → identité de l'agent
lui-même (déjà utilisé, `_resolve_my_id`). `getLocalParticipantProperty` → lecture symétrique de
`setLocalParticipantProperty` (§2). `getBreakoutRooms` → cf. §4. `getPolls` → cf. §11.
`getTranscriptionStatus` → cf. §5. `getConnection` / `getShortTermCredentials` → bas niveau,
utile seulement pour du diagnostic avancé, pas pour le raisonnement métier.

---

## 11. Sondages — cas particulier documenté avec prudence

`getPolls` est confirmé dans `IJitsiConference` (lecture). La **création** et la **réponse** à
un sondage sont des fonctionnalités réelles et actives de Jitsi Meet (événements déjà captés en
lecture aujourd'hui : `POLL_RECEIVED`, `POLL_ANSWER_RECEIVED`, doc 00 §5.5), mais leur méthode
d'écriture exacte n'apparaît pas nommément dans l'extrait d'interface consulté (elle transite
vraisemblablement par `sendMessage`/`sendCommand` avec un payload JSON structuré propre à la
feature "polls" de `jitsi-meet`, comme c'est le cas pour plusieurs fonctionnalités récentes de
l'app React qui n'exposent pas toutes une méthode `JitsiConference` dédiée).

**Décision documentée plutôt qu'improvisée** : `chat_tools.create_poll(question, answers)` et
`chat_tools.answer_poll(poll_id, answers)` sont inscrits au catalogue comme 🔧 P1, avec comme
tâche d'implémentation explicite "inspecter le bundle JS déployé
(`nginx/jitsi-meet-host-backup/libs/app.bundle.min.js`, déjà présent dans le dépôt vendé) pour
extraire le payload exact `sendMessage`/`sendCommand` utilisé par le composant Polls avant
d'écrire le premier appel" — pas une supposition de format codée en dur sans vérification.

---

## 12. Synthèse chiffrée

| Catégorie | Aujourd'hui (`peer`) | Cible (CIVITAS Agent) |
|---|---|---|
| Actions d'écriture vers Jitsi | 3 (`send_chat`, `kick_participant`, `mute_participant`) | ~25 outils P0 (🆕/✅) + ~10 outils P1 (🔧) |
| Capacités de lecture exploitées | via événements bruts uniquement | idem + capacités `IJitsiConference` de lecture directe (§10) explicitement cataloguées |
| Perception visuelle | 1 (`capture_frame`, déclenché par mot-clé) | 3 outils, appelables par le raisonnement, pas seulement par mot-clé |
| Outils "plateforme" (hors Jitsi) | 0 | 6 (`platform_tools`) + 1 (`rag_tools`) — nouveauté assumée du domaine 4 |
| Actions gérées par permission (`room_configs.permissions`/`tools_allowed`) | 2 (`can_moderate` sur kick/mute uniquement) | toutes, via le registre (doc 01 §9) |

Ce document est la référence à cocher, outil par outil, pendant l'implémentation (doc 04) — rien
n'y est laissé "pour plus tard" sans être explicitement nommé et statué (P0/P1/non applicable).
