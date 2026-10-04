# Agent Bootstrap Contract

Canonical project ID: `fold7-power-lab`  
Project name: `Galaxy Z Fold7 Power Lab`  
Authorized repository: `boberino93-bit/samsungpowerbootstrap`  
Stable GitHub repository ID: `1404088763`  
Authoritative forum: ChatGPT Library Artifactory `/Fold7-PowerLab-AgentBus/messages`  
Artifact root: `/Fold7-PowerLab-AgentBus/artifacts`  
Repository forum view: `NONE`

`PROJECT_IDENTITY_LOCK.json` is the highest local machine-readable identity authority. `AGENT_BOOTSTRAP.json` must agree with it. This Markdown explains the contract but does not override either machine-readable file. Do not invent `.interagent/messages` as a substitute for the artifactory forum; the repository currently exposes bootstrap/state/recovery infrastructure, not a registered live forum mirror.

Before any mutation, a new agent MUST:

1. Resolve current human intent to `fold7-power-lab`; ambiguous intent means write nowhere.
2. Read and validate `PROJECT_IDENTITY_LOCK.json`.
3. Read and validate `AGENT_BOOTSTRAP.json` against the identity lock and central routing registry.
4. Determine its assigned role (`primary`, `manager`, `research`, `recovery`, `qa`, or `build`).
5. Verify repository full name and stable GitHub repository ID where available.
6. Load the device recovery contract before any device-facing mutation.
7. Read the authoritative artifactory forum plus registered repository handoffs/state (`PROJECT_MANIFEST.json`, `START_HERE.md`, `.interagent/state`, `.interagent/bootstrap`) before task activation.
8. Bind mutation authority only to `boberino93-bit/samsungpowerbootstrap`.
9. Emit: `IDENTITY RESOLVED: project=fold7-power-lab; role=<role>; forum=/Fold7-PowerLab-AgentBus/messages; repositories=boberino93-bit/samsungpowerbootstrap; state=<handoff/state ref>`.
10. Only then begin role-specific work.

If bootstrap, repository metadata, the identity lock, central registry, or inherited context disagree: **STOP BEFORE MUTATION**. Recent context, a nearby repo, or a newer handoff never overrides project identity.
