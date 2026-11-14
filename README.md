# maturity-model-template

Executable scaffold for a conformant **maturity-model repository** in the [Assessment-Models](https://github.com/Assessment-Models) organization.

> **Implementation, not authority.** The normative source of truth is [maturity-model-standard](https://github.com/Assessment-Models/maturity-model-standard) (AM-MODEL-REPOSITORY-STANDARD v1.0.1, established by CR-AM-ORG-RES-000). If this template ever disagrees with the standard, the standard wins and a template issue is filed.

## Status

`0.1.0` · template

> Keep this line in sync with `VERSION`, `model.yaml` and `standard.yaml` — the repository-standard conformance workflow enforces it.

## Using this template

1. Create your repository from this template and rename it `maturity-model-{domain}`.
2. Work through the checklist below, replacing every `TODO` and every placeholder between `{}` braces.
3. Keep `model.yaml` as the authoritative identity manifest (CR-AM-11 §15 contract handshake) — `standard.yaml` cross-references it, it never replaces it.
4. Never mint a competing maturity scale: bind the canonical scale from [`technehub-labs/dea-metamodel`](https://github.com/technehub-labs/dea-metamodel) in `maturity/scale.yaml`.
5. Raise your `standard.yaml` conformance level deliberately (`registered` → `structural` → `full`) as structure and validation are completed, and record adoption in the [portfolio conformance registry](https://github.com/Assessment-Models/maturity-model-standard/blob/main/registry/conformance.yaml).

## Checklist for a new model repository

- [ ] Rename the repository to `maturity-model-{domain}`.
- [ ] `model.yaml` — real identity, description, version, contract handshake, dependencies, compatibility.
- [ ] `standard.yaml` — real model id/name/version matching `model.yaml` and `VERSION`.
- [ ] `VERSION`, `README.md` status line and `model.yaml` version all agree (CI enforces this).
- [ ] `maturity/scale.yaml` — bind the canonical scale id/version; do not mint a new one.
- [ ] `maturity/model/{domain}.yaml` — authoritative model definition: dimensions, criteria, levels, scoring rules.
- [ ] `examples/` — at least one reproducible example consistent with the model definition.
- [ ] `docs/` — fill the required documents; wire `docs/diagrams/` (DGM-01..04 required at `full`).
- [ ] `mappings/framework-mappings.yaml` — provenance and external-framework mappings.
- [ ] `.github/workflows/contract-conformance.yml` — re-pin `dea-metamodel-ref` to the current immutable reference at creation time.
- [ ] Registry record in [`assessment-registry`](https://github.com/Assessment-Models/assessment-registry) (Level 3 ecosystem validation).
- [ ] Adoption entry in the [portfolio conformance registry](https://github.com/Assessment-Models/maturity-model-standard/blob/main/registry/conformance.yaml).

## CI levels (all additive; none replaces another)

| Level | Workflow | Validates |
|---|---|---|
| 1 — Repository | `.github/workflows/local-model-ci.yml` | Structure, YAML syntax, manifest, declaration coherence (via `scripts/local_validate.py`) |
| 2 — Contract | `.github/workflows/contract-conformance.yml` | Canonical metamodel and contract conformance (reusable workflow from [`assessment-ci`](https://github.com/Assessment-Models/assessment-ci)) |
| Ecosystem standard | `.github/workflows/repository-standard.yml` | AM-MODEL-REPOSITORY-STANDARD declaration and structure (reusable workflow from [`maturity-model-standard`](https://github.com/Assessment-Models/maturity-model-standard)) |
| 3 — Ecosystem | `assessment-registry` | Registration, immutable refs, release resolution (add a record there; do not re-implement) |

## Standardize the architecture, never the model's content

Your model keeps its own dimensions, criteria, scale, scoring and evidence semantics (AP-01). A Technology model must not inherit Autonomous Operations dimensions merely because both use this scaffold. Canonical semantics live in [`technehub-labs/dea-metamodel`](https://github.com/technehub-labs/dea-metamodel); this template governs repository shape only.

## Licence

MIT — see [LICENSE](LICENSE).
