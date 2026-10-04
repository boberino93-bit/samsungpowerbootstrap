# Samsung Power Bootstrap — Galaxy Z Fold7 Power Lab

Dedicated research and device-engineering repository for project `fold7-power-lab`.

## Mission

Understand and safely prototype the earliest reliable Samsung Galaxy Z Fold7 display-power/bootstrap path, especially the interval between physical opening evidence, panel power, Samsung topology publication, and usable presentation. The project may study privileged/user-space mechanisms, display topology, SurfaceFlinger/HWC-facing behavior, Samsung-specific state transitions, diagnostics, and rollback architecture.

This repository is intentionally separate from `duo-open`. Findings may inform other projects only through explicit human-authorized transfer; no foreign project has write authority here.

## Target

- Device: Samsung Galaxy Z Fold7
- Platform: Android 16 / current Samsung One UI
- Inner geometry: 1968×2184
- Cover geometry: 1080×2520

Logical Android display IDs are not durable physical-panel identity and must not be treated as such across topology transitions.

## Current safety state

`RISKY_DEVICE_MUTATION_BLOCKED`

Before any change that could immobilize the phone, break the UI, disrupt boot, disable input, corrupt display routing, or otherwise remove the ordinary recovery surface, the exact mutation class must have a tested independent rollback path. See `docs/DEVICE_RECOVERY_STRATEGY.md`.

## Start here

Read `START_HERE.md`, then follow `BOOTSTRAP_ORDER.json`.
