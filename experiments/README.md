# Experiments

Every device-facing experiment must declare scope, reversibility, expected success signal, failure signal, abort criteria, required recovery tier, known-good rollback target, and post-test health checks.

If the required recovery tier is not validated, the experiment remains design-only.
