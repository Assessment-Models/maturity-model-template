# DGM-06 — Repository architecture (TEMPLATE, recommended)

Purpose: explains the repository's files, directories and their relationships.

```mermaid
flowchart TB
    R["README.md + standard.yaml"] --> M["model.yaml<br/>authoritative manifest"]
    M --> Y["maturity/<br/>scale + model definition"]
    Y --> X["examples/"]
    Y --> D["docs/ + diagrams"]
    Y --> P["mappings/"]
    CI[".github/workflows<br/>Levels 1, 2, standard"] --> M
```

TODO: adapt to the repository's real structure once established.
