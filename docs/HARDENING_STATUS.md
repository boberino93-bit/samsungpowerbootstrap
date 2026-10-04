# Hardening Status

## Current state

This project is transitioning from bootstrap-only scaffolding to deterministically enforced project identity and package synchronization.

### ENFORCED + TESTED (source-level)

- project identity lock values are explicit;
- cross-project writes default to deny;
- scope gate rejects ambiguous/foreign project writes;
- message validator rejects foreign destination identity, duplicates, and expired commands in bounded tests;
- recovery contract blocks risky persistent mutation while `UNVALIDATED`;
- project/manifest/version identity consistency is testable;
- package builder and validator are deterministic.

### ENFORCED

- role capability sets are least-privilege relative to Primary;
- package dependency map identifies shared and role-specific inputs;
- cross-project exchange is a distinct explicit contract;
- package bootstrap must validate scope, identity, and recovery gate before tasks become actionable.

### DOCUMENTED / NOT YET RUNTIME-ENFORCED

- atomic task leasing against a live shared backend;
- global agent registry and heartbeat service;
- dead-letter/quarantine persistence in the external coordination store;
- live concurrent multi-project scheduler behavior.

### Device recovery

The recovery architecture is P0 but remains `UNVALIDATED`. High-risk device mutation remains blocked until a physical recovery drill is completed.
