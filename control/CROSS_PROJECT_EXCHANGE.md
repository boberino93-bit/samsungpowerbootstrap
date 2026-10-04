# Cross-Project Exchange Contract

Ordinary project channels may never be used for cross-project writes.

Allowed pattern:

1. Explicit export request naming source and destination projects.
2. Capability/policy check.
3. Sanitized copy-by-value snapshot.
4. Provenance record containing source project, source revision, exporter, timestamp, and reason.
5. Destination-side import validation.
6. Immutable audit record.

No credentials, mutable task state, locks, leases, accepted-state authority, or project-instance secrets may cross this boundary.

Default outcome is `DENY`.
