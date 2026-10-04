# Safety and Authority Model

## Project identity

Current human intent → project scope gate → identity lock → recovery gate → local project state → task execution.

Recent context is not authority.

## Cross-project isolation

Cross-project reads may be used as reference evidence where appropriate. Cross-project writes are denied by default. Do not import another project's accepted state, credentials, authority, task queue, or mutable coordination state.

## Evidence classes

Research outputs should label claims as one of:

- `VERIFIED_FACT`
- `SUPPORTED_CLAIM`
- `HYPOTHESIS`
- `UNKNOWN`
- `REJECTED_CLAIM`
- `IMPLEMENTATION_AUTHORITY`

Only the Primary can convert evidence into implementation authority.

## Device safety

A successful code build does not prove a safe device mutation. Device-critical work requires rollback design, bounded testing, field evidence, and post-recovery validation.

## Role separation

Research proposes and tests bounded ideas. Manager reviews, deduplicates, and challenges evidence. Primary owns repository integration, device-test authorization, promotion, rollback status, and release decisions.
