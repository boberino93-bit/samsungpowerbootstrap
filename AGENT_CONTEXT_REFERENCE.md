# Galaxy Z Fold7 Power Lab — Fresh Agent Context Reference

Version: 1.0.0
Status: ACTIVE ORIENTATION
Authority: ORIENTATION_ONLY
Project ID: `fold7-power-lab`
Repository: `boberino93-bit/samsungpowerbootstrap`
Canonical coordination namespace: `/Fold7-PowerLab-AgentBus/messages`

## What this project is

This is the Galaxy Z Fold7 Power Lab. A contextless agent should use `PROJECT_MANIFEST.json`, `START_HERE.md`, current master handoff, and accepted AgentBus state for the exact device/power engineering objective instead of inferring requirements from the repository name. Typical work may include device/power experiments, bootstrap/runtime engineering, measurement, testing, validation, and package/recovery work defined by those local records.

## Human operating expectation

Once a valid objective is given, continue safe in-scope work without repeated routine confirmation. Recover existing context from durable project state before asking the human to repeat it. Iterate through investigation, implementation, testing, repair, and validation when within authority.

Fail closed only on the affected unsafe mutation or branch when possible; preserve the blocker and continue unrelated safe work. Escalate only for non-delegable authority, irrecoverable data integrity, a security-boundary decision, or a required unavailable external capability.

## Likely shorthand

- `this project` means `fold7-power-lab` after exact binding.
- `continue` means recover the latest valid active task/handoff and proceed.
- `do that` / `execute that` means resolve the current-message referent first, then durable state.
- `run the swarm` means use this project's own accepted swarm/bootstrap contract.
- `update the packages` means synchronize affected PRIMARY/MANAGER/RESEARCH packages within authority.
- references to the Fold7 Power Lab or Samsung power bootstrap normally refer here when already bound.

## Startup

Verify exact project identity; load `AGENT_BOOTSTRAP.json`; read this reference as orientation only; load `PROJECT_MANIFEST.json`, MASTER_HANDOFF, and current AgentBus state; recover the active task; verify scope, versions, dependencies, collisions, leases, and approvals; then execute within authority.

Likely intent is never permission to cross project boundaries.
