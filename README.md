# maturity-model-template

Executable scaffold for a conformant **maturity-model repository** in the [Assessment-Models](https://github.com/Assessment-Models) organization.

> **Implementation, not authority.** The normative source of truth is [maturity-model-standard](https://github.com/Assessment-Models/maturity-model-standard) (AM-MODEL-REPOSITORY-STANDARD v1.0.1, established by CR-AM-ORG-RES-000). If this template ever disagrees with the standard, the standard wins and a template issue is filed.

## Status

`0.1.0` · template

> Keep this line in sync with `VERSION`, `model.yaml` and `standard.yaml` — the repository-standard conformance workflow enforces it.

## Using this template

1. Create your repository from this template and rename it `maturity-model-{domain}`.
2. Work through the checklist below, replacing every `TODO` and every placeholder between `{}` braces.
3. Keep `model.yaml` as the authoritative identity manifest (CR-AM-11 §15 contract handshake). `standard.yaml` declares repository-standard adoption; it does not replace the manifest.
4. Define the model's maturity scale in `maturity/scale.yaml`. You may either:
   - define and version a model-owned scale; or
   - explicitly bind a published canonical scale by identifier, version and immutable source reference.
   
   The organization standard requires explicit, governed scale semantics. It does **not** require every model to adopt the same scale.
5. Document the scale's level identifiers, ordering, meanings, progression rules and any non-maturity states. Keep scoring and aggregation rules explicit in the authoritative model definition.
6. Raise your `standard.yaml` conformance level deliberately (`registered` → `structural` → `full`) as structure and validation are completed, and record adoption in the [portfolio conformance registry](https://github.com/Assessment-Models/maturity-model-standard/blob/main/registry/conformance.yaml).

## Checklist for a new model repository

- [ ] Rename the repository to `maturity-model-{domain}`.
- [ ] `model.yaml` — real identity, description, version, contract handshake, actual dependencies and compatibility.
- [ ] `standard.yaml` — real model id/name/version matching `model.yaml` and `VERSION`.
- [ ] `VERSION`, `README.md` status line and `model.yaml` version all agree (CI enforces this).
- [ ] `maturity/scale.yaml` — declare whether the scale is model-owned or a canonical-scale binding; identify and version the scale and document its semantics.
- [ ] `maturity/model/{domain}.yaml` — authoritative model definition: dimensions, criteria, level application, scoring rules and aggregation.
- [ ] `docs/maturity-levels.md` — explain every level and any separate states; align with the declared scale.
- [ ] `examples/` — at least one reproducible example consistent with the model definition.
- [ ] `docs/` — fill the required documents; wire `docs/diagrams/` (DGM-01..04 required at `full`).
- [ ] `mappings/framework-mappings.yaml` — provenance and external-framework mappings.
- [ ] `.github/workflows/contract-conformance.yml` — pin the reusable `assessment-ci` workflow and its `assessment-ci-ref` to immutable commit SHAs; re-pin `dea-metamodel-ref` to the intended immutable contract-suite reference.
- [ ] Registry record in [`assessment-registry`](https://github.com/Assessment-Models/assessment-registry) (Level 3 ecosystem validation).
- [ ] Adoption entry in the [portfolio conformance registry](https://github.com/Assessment-Models/maturity-model-standard/blob/main/registry/conformance.yaml).

## CI levels (all additive; none replaces another)

Reusable workflows must be referenced by immutable commit SHA, not `main`, `master`, or a moving version tag. Keep the nested validator source (`assessment-ci-ref`) immutable as well. The pins in this template are known-good reference points at publication time; review and update them deliberately when creating a repository.

| Level | Workflow | Validates |
|---|---|---|
| 1 — Repository | `.github/workflows/local-model-ci.yml` | Structure, YAML syntax, manifest, declaration coherence (via `scripts/local_validate.py`) |
| 2 — Contract | `.github/workflows/contract-conformance.yml` | Canonical metamodel and contract conformance (reusable workflow from [`assessment-ci`](https://github.com/Assessment-Models/assessment-ci)) |
| Ecosystem standard | `.github/workflows/repository-standard.yml` | AM-MODEL-REPOSITORY-STANDARD declaration and structure (reusable workflow from [`maturity-model-standard`](https://github.com/Assessment-Models/maturity-model-standard)) |
| 3 — Ecosystem | `assessment-registry` | Registration, immutable refs, release resolution (add a record there; do not re-implement) |

## Standardize the architecture, never the model's content

The organization standard establishes **common structure with independent semantics** (AP-01). Each model owns its dimensions, criteria, maturity scale, scoring method, aggregation rules and evidence semantics.

A model may adopt a published canonical scale where that is appropriate. If it does, bind the exact scale identifier and version to an immutable source reference. A model may instead define its own scale; in that case, document its identifiers, ordering, level meanings, progression semantics and provenance in the model repository. Neither choice is a departure from the organization standard.

Do not conflate a shared scale contract or metamodel dependency with adoption of one particular maturity ladder. Shared contracts support consistent representation and validation; they do not make model-specific scales identical. A model-specific scoring measure or supplementary index is likewise owned by that model unless separately adopted through an organization-level decision.

## Licence

MIT — see [LICENSE](LICENSE).
