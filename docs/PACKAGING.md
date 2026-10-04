# Agent Package Release Process

Any change to project identity, bootstrap, safety/recovery, protocol, message/task/artifact schemas, role instructions, capability rules, or package dependencies triggers evaluation of all three core role packages.

Release set `0.1.0-alpha.2` contains synchronized Primary, Manager, and Research packages built from the same source revision and protocol version.

Required sequence:

1. Update source.
2. Run source tests.
3. Build all affected packages as one release set.
4. Validate archive contents and hashes.
5. Confirm no foreign project authority/state is present.
6. Smoke-test bootstrap metadata.
7. Publish packages and update `PACKAGE_REGISTRY.json` with hashes and source revision.

A successful ZIP creation is not sufficient; validation is mandatory.
