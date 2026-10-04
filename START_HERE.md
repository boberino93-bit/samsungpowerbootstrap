# Galaxy Z Fold7 Power Lab — START HERE

Project ID: `fold7-power-lab`

This repository is the dedicated GitHub home for the Samsung Power Bootstrap / Galaxy Z Fold7 Power Lab project.

**Current status: REPOSITORY_BOUND / PRIMARY_BOOTSTRAP_ACTIVE / RESEARCH_AND_MANAGER_SWARM_NOT_YET_AUTHORIZED / RISKY_DEVICE_MUTATION_BLOCKED.**

Bootstrap order:

1. Read `PROJECT_IDENTITY_LOCK.json`.
2. Read `BOOTSTRAP_ORDER.json` and `PROJECT_MANIFEST.json`.
3. Read `.interagent/bootstrap/initialization.json`.
4. Read `.interagent/recovery/RECOVERY.md` and `.interagent/recovery/DEVICE_RECOVERY_CONTRACT.json`.
5. Validate that current human intent names this project and that the writable repository is exactly `boberino93-bit/samsungpowerbootstrap`.
6. Load project-local state only after identity validation.
7. Review `.interagent/swarm/initial-assessment.json` and `.interagent/swarm/proposed-allocation.json` before authorizing research work.

## Non-negotiable safety gate

A change capable of affecting boot, SystemUI, launcher availability, display power/topology, input, lockscreen/keyguard, package management, privileged services, or other device-critical paths **must not be field-deployed until an independent recovery path is documented and validated for the exact mutation class**.

Recovery must not depend only on the phone UI that the experiment can break. The project must maintain an external-host rescue path, a known-good rollback target, pre-change state capture, and explicit abort/revert criteria.

If recovery readiness is `BLOCKED` or `UNVALIDATED`, risky persistent device mutation is prohibited.

## Authority boundary

This project is isolated from `duo-open`, Warp Propulsion Lab, Benefits/BenefitFlow, and all other projects. Their material may be read as reference evidence when useful, but it grants zero write authority here and this project's work must not be written into their repositories.

Only the Primary may promote research into implementation. Manager and Research roles do not receive production-write authority by default.
