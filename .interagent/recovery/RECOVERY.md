# Recovery and Primary-Takeover Contract

Recovery has two independent meanings in this project: **agent/project recovery** and **physical device recovery**. Both fail closed.

## 1. Agent/project recovery

A replacement Primary, Manager, or Research agent does not inherit writable scope from recent context. It must revalidate current human intent, `PROJECT_IDENTITY_LOCK.json`, the canonical repository, and the project-local coordination namespace before acting.

Foreign handoffs are reference-only until explicitly transferred by the human.

## 2. Physical device recovery

The phone is the experimental target and cannot be treated as the only rescue console. A broken SystemUI, launcher, display route, input path, privileged service, package state, or boot path can remove the interface needed to undo the change.

Therefore every risky field test must have an **independent host-side escape route** prepared before the mutation.

At minimum, record:

- exact pre-change commit/build/configuration;
- exact mutation being applied;
- known-good rollback artifact and SHA-256;
- host-side commands or restore procedure specific to that mutation;
- expected symptoms of failure;
- abort threshold;
- proof that the rescue connection works before the test;
- proof that rollback restores a usable phone afterward.

## 3. Recovery readiness gate

`DEVICE_RECOVERY_CONTRACT.json` starts at `UNVALIDATED`. While unvalidated, persistent or device-critical mutation is blocked.

Observation-only work, offline modeling, source analysis, reversible app-local experiments, and diagnostics that cannot immobilize the phone may proceed under normal Primary review.

## 4. Never rely on

- a recovery UI that the experiment itself can disable;
- a rollback file stored only on the phone;
- remembering commands from chat history;
- a logical display ID remaining stable across Samsung topology changes;
- factory reset as the planned first-line recovery mechanism.
