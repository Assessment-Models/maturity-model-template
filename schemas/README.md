# Schemas — by reference, never by fork

This template intentionally contains **no schema copies**. Validated schemas live where they are governed:

| Schema | Authority | Used by |
|---|---|---|
| Model manifest (CR-AM-11 §15 handshake) | [`assessment-ci`](https://github.com/Assessment-Models/assessment-ci) | Level 1/2 CI |
| Maturity scale and canonical contracts | [`technehub-labs/dea-metamodel`](https://github.com/technehub-labs/dea-metamodel) | Level 2 CI, `maturity/scale.yaml` binding |
| Repository-standard declaration (`standard.yaml`) | [`maturity-model-standard/schemas/standard-declaration.schema.json`](https://github.com/Assessment-Models/maturity-model-standard/blob/main/schemas/standard-declaration.schema.json) | Repository-standard conformance workflow |

If your model needs model-specific schemas, add them here **in addition to** (never instead of) the referenced canonical ones, and declare their ownership and compatibility in `model.yaml`.
