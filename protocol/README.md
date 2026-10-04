# Fold7 Power Lab Protocol

Protocol version: `1.0.0-alpha.1`.

Project identity is a security boundary. Every mutating operation and every internal message must carry explicit project identity and must validate that identity against the bound session/repository state before execution.

Ordinary project channels are project-local. Cross-project exchange is a separate, explicit, sanitized copy-by-value operation and is denied by default.
