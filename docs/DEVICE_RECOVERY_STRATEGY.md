# Device Recovery Strategy

## Goal

Make it difficult for experimental Samsung/Fold7 power-bootstrap work to strand the device in an unusable state and make recovery deterministic if it does.

## Core rule

**No high-risk mutation without a validated independent escape path.**

A change is high risk when it can affect boot, SystemUI, launcher/home, keyguard, input, package manager state, display power, physical/logical display routing, persistent settings, overlays, privileged services, or anything required to see and control the phone.

## Recovery architecture

### A. Known-good baseline

Before each risky experiment, preserve outside the phone:

- the last known-good build/artifact;
- SHA-256 hashes;
- configuration/state needed to restore it;
- the source commit that produced it;
- the exact changed component(s).

### B. External rescue host

The recovery plan must work from a second device/computer when the Fold7 UI is unavailable. The project must not assume the phone can display prompts, launch Settings, open a terminal, or approve a new trust dialog after failure.

### C. Mutation-specific rollback

Do not use one generic recovery script for every class of failure. Each experiment must declare what it changes and how that exact change is undone. Rollback should be as narrow as the mutation.

### D. Staged deployment

Prefer this progression:

1. offline/source analysis;
2. observation-only instrumentation;
3. temporary/reversible user-space experiment;
4. bounded device mutation with watchdog/timeout where possible;
5. persistent mutation only after the recovery drill for that class has passed.

### E. Recovery tiers

**Tier 0 — app-local:** stop/revert the experimental process or package and restore the known-good artifact.

**Tier 1 — Android alive, host channel alive:** use the already-authorized external rescue channel to reverse the exact package/configuration/display-control change.

**Tier 2 — Android alive, UI unusable:** treat the host as the primary control surface; revert the changed component, then reboot and validate normal UI/input/display behavior.

**Tier 3 — normal Android boot unavailable:** use Samsung-supported Recovery/Download mechanisms only under a separately prepared restore procedure. Any experiment capable of reaching this tier is blocked until that procedure is independently verified and the data-loss implications are understood.

## Mandatory preflight for risky field tests

- Recovery contract for the exact mutation class is `VALIDATED`.
- External rescue host has the rollback package and instructions.
- Physical USB/data path has been checked.
- Known-good artifact hash matches.
- Current state snapshot has been captured.
- Abort threshold is written before the test begins.
- The test changes one bounded mechanism at a time where practical.

## Post-recovery health check

Recovery is not complete just because the phone boots. Verify at least: boot completion, lock/unlock, touch/input, cover display, inner display, fold/unfold topology, launcher/home, Settings access, network basics, and the absence of repeated crash/boot loops attributable to the experiment.

## P0 engineering objective

Build a repeatable **rescue kit** that can eventually be generated per experiment: manifest, known-good artifacts, hashes, mutation record, revert procedure, and health-check checklist. Keep that kit off-device as well as in version control where safe.
