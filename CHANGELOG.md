# Changelog — maturity-model-template

## Unreleased

### Changed

- Pin reusable assessment-ci and maturity-model-standard workflows to immutable commit SHAs; explicitly pin the nested assessment-ci validator source in the Level 2 workflow.
- Clarify immutable workflow pinning as a repository-creation requirement.

### Changed

- Align scale guidance with CR-AM-ORG-RES-000 and AP-01: models may define and version their own maturity scale or explicitly bind a published canonical scale.
- Replace the mandatory canonical-scale placeholder with a model-owned scale declaration and an optional immutable canonical binding pattern.
- Clarify that the shared maturity-scale contract does not mandate adoption of one canonical maturity ladder.
- Remove the template's implicit direct dependency on the DEA maturity-bands-v2 scale.

## 0.1.0 — 2026-11-14

Initial scaffold under CR-AM-ORG-RES-000, implementing AM-MODEL-REPOSITORY-STANDARD v1.0.0.

### Added

- Annotated `model.yaml` (CR-AM-11 §15 handshake), `standard.yaml` declaration (registered), `maturity/` scale-binding and model-definition skeletons.
- `docs/` skeleton (overview, architecture, assessment-methodology, maturity-levels, dimensions, evidence-framework, provenance, governance, use-cases) and diagram index (DGM-01..07).
- `examples/`, `mappings/`, `schemas/` (by-reference policy).
- Level 1 `local-model-ci.yml`, Level 2 `contract-conformance.yml` (reusable, from `assessment-ci`), ecosystem-standard `repository-standard.yml` (reusable, from `maturity-model-standard`).
- Mirrored `scripts/local_validate.py` declaration validator.
