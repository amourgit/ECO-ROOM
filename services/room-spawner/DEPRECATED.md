# ⚠️ DÉPRÉCIÉ — remplacé par `services/civitas-orchestrator`

Ce service est **remplacé** par le **CIVITAS Agent Orchestrator**, qui spawn désormais un
container isolé par room au lieu d'appeler un service `peer` partagé. Voir :

- [`docs/architecture/03-isolation-et-orchestration.md`](../../docs/architecture/03-isolation-et-orchestration.md) —
  mécanique complète du nouvel orchestrateur
- [`docs/architecture/04-plan-migration.md`](../../docs/architecture/04-plan-migration.md) —
  bascule progressive (les deux orchestrateurs peuvent coexister room par room, cf. Phase 2)

Ce service reste actif jusqu'à la Phase 6 du plan de migration — mêmes raisons qu'indiquées
dans [`services/peer/DEPRECATED.md`](../peer/DEPRECATED.md).
