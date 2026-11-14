# DGM-02 — Conceptual architecture (TEMPLATE)

Purpose: explains the major concepts and relationships constituting the model.

```mermaid
flowchart TB
    M["MaturityModel"] --> S["MaturityScale"]
    M --> D["AssessmentDimension"]
    D --> C["AssessmentCriterion"]
    C --> E["EvidenceRequirement"]
    C --> P["ScoringRule"]
    P --> L["MaturityLevel determination"]
```

TODO: replace with the model's real conceptual diagram, keeping canonical boundaries (MaturityModel vs AssessmentModel vs AssessmentExecution vs AssessmentResult) distinct.
