# Changelog — maturity-model-template

## 0.1.0 — 2026-11-14

Initial scaffold under CR-AM-ORG-RES-000, implementing AM-MODEL-REPOSITORY-STANDARD v1.0.0.

### Added

- Annotated `model.yaml` (CR-AM-11 §15 handshake), `standard.yaml` declaration (registered), `maturity/` scale-binding and model-definition skeletons.
- `docs/` skeleton (overview, architecture, assessment-methodology, maturity-levels, dimensions, evidence-framework, provenance, governance, use-cases) and diagram index (DGM-01..07).
- `examples/`, `mappings/`, `schemas/` (by-reference policy).
- Level 1 `local-model-ci.yml`, Level 2 `contract-conformance.yml` (reusable, from `assessment-ci`), ecosystem-standard `repository-standard.yml` (reusable, from `maturity-model-standard`).
- Mirrored `scripts/local_validate.py` declaration validator.
