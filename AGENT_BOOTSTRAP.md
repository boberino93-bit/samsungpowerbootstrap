# Agent Bootstrap Contract

Canonical project ID: `fold7-power-lab`  
Project name: `Galaxy Z Fold7 Power Lab`  
Authorized repository: `boberino93-bit/samsungpowerbootstrap`  
Stable GitHub repository ID: `1404088763`  
Internal forum namespace: `/Fold7-PowerLab-AgentBus/messages`  
Preferred repository mirror path: `.interagent/messages`

`PROJECT_IDENTITY_LOCK.json` is the highest local machine-readable identity authority. `AGENT_BOOTSTRAP.json` must agree with it. This Markdown explains the contract but does not override either machine-readable file.

Before any mutation, a new agent MUST:

1. Resolve current human intent to `fold7-power-lab`; ambiguous intent means write nowhere.
2. Read and validate `PROJECT_IDENTITY_LOCK.json`.
3. Read and validate `AGENT_BOOTSTRAP.json` against the identity lock.
4. Determine its assigned role (`primary`, `manager`, `research`, `recovery`, `qa`, or `build`).
5. Verify repository full name and stable GitHub repository ID where available.
6. Load the device recovery contract before any device-facing mutation.
7. Read project-local forum/handoff/state before task activation.
8. Bind mutation authority only to `boberino93-bit/samsungpowerbootstrap`.
9. Emit the identity acknowledgement only after all checks pass.
10. Only then begin role-specific work.

If bootstrap, repository metadata, the identity lock, central registry, or inherited context disagree: **STOP BEFORE MUTATION**. Recent context, a nearby repo, or a newer handoff never overrides project identity.
