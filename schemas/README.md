# Schemas — by reference, never by fork

This template intentionally contains **no schema copies**. Validated schemas live where they are governed:

| Schema or contract | Authority | Used by |
|---|---|---|
| Model manifest (CR-AM-11 §15 handshake) | [`assessment-ci`](https://github.com/Assessment-Models/assessment-ci) | Level 1/2 CI |
| Shared maturity-scale contract and canonical scale definitions | [`technehub-labs/dea-metamodel`](https://github.com/technehub-labs/dea-metamodel) | Level 2 contract validation; optional canonical-scale binding |
| Repository-standard declaration (`standard.yaml`) | [`maturity-model-standard/schemas/standard-declaration.schema.json`](https://github.com/Assessment-Models/maturity-model-standard/blob/main/schemas/standard-declaration.schema.json) | Repository-standard conformance workflow |

The shared maturity-scale contract governs representation and conformance. It does **not** require every model to adopt the same scale definition. A model may define and version its own scale, or bind a published canonical scale explicitly in `maturity/scale.yaml`.

If your model needs model-specific schemas, add them here **in addition to** (never instead of) the referenced shared contracts, and declare their ownership and compatibility in `model.yaml`.
