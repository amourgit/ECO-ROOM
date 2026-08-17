# ⚠️ DÉPRÉCIÉ — remplacé par `services/civitas-agent`

Ce service est **remplacé** par le **CIVITAS Agent Runtime** (LangGraph), isolé strictement
par room. Voir la documentation complète de la refonte :

- [`docs/architecture/README.md`](../../docs/architecture/README.md) — index de la nouvelle
  architecture
- [`docs/architecture/00-etat-des-lieux.md`](../../docs/architecture/00-etat-des-lieux.md) —
  analyse de CE service tel qu'il existe aujourd'hui, et de ses limites (notamment l'absence
  d'isolation par room, cf. §5.1)
- [`docs/architecture/04-plan-migration.md`](../../docs/architecture/04-plan-migration.md) —
  plan de bascule phasé

## Ce service reste actif jusqu'à la Phase 6 du plan de migration

Ce code **n'est pas supprimé immédiatement** : `services/civitas-agent` doit d'abord atteindre
la parité fonctionnelle et être validé en conditions réelles (Phase 1 du plan de migration)
avant toute bascule de production. Supprimer ce service sans remplacement testé serait
irresponsable pour un système en production — cf. la justification complète dans
[`docs/architecture/04-plan-migration.md`](../../docs/architecture/04-plan-migration.md#phase-6--bascule-finale-et-suppression-de-lancien-code).

**Ne pas ajouter de nouvelle fonctionnalité ici.** Toute nouvelle capacité (nouveaux outils,
nouveaux comportements) va exclusivement dans `services/civitas-agent`, suivant le catalogue
[`docs/architecture/02-catalogue-outils-agent.md`](../../docs/architecture/02-catalogue-outils-agent.md).
