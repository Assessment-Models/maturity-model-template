#!/usr/bin/env python3
"""Validate a repository's AM-MODEL-REPOSITORY-STANDARD declaration (standard.yaml).

Mirrored from Assessment-Models/maturity-model-standard@main
(validators/validate_standard_declaration.py, standard v1.0.0, CR-AM-ORG-RES-000).
Extend or replace it with the model's own Level 1 validator as the model grows;
the cross-repository checks below remain the baseline.
"""
import argparse
import os
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required: pip install pyyaml")

STANDARD_ID = "AM-MODEL-REPOSITORY-STANDARD"
SEMVER = r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?$"
CONFORMANCE_LEVELS = {"registered": 0, "structural": 1, "full": 2}

REQUIRED_PATHS_STRUCTURAL = [
    "README.md",
    "standard.yaml",
    "model.yaml",
    "VERSION",
    "CHANGELOG.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "maturity/scale.yaml",
    "maturity/model",
    "examples",
    "scripts",
    ".github/workflows/local-model-ci.yml",
    ".github/workflows/contract-conformance.yml",
]
REQUIRED_PATHS_FULL = [
    "docs",
    "docs/diagrams",
    "mappings",
    "docs/provenance.md",
    "docs/assessment-methodology.md",
]


def read_version_file(root):
    path = os.path.join(root, "VERSION")
    if not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8") as handle:
        return handle.read().strip()


def readme_status_version(root):
    path = os.path.join(root, "README.md")
    if not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    match = re.search(r"^##\s*Status\s*$\n(.*?)(?=^##\s|\Z)", text, re.S | re.M)
    if not match:
        return None
    version = re.search(r"`(\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?)`", match.group(1))
    return version.group(1) if version else None


def load_yaml(path, violations, label):
    try:
        with open(path, encoding="utf-8") as handle:
            return yaml.safe_load(handle) or {}
    except yaml.YAMLError as exc:
        violations.append("%s does not parse: %s" % (label, exc))
        return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    root = args.root
    violations = []

    declaration_path = os.path.join(root, "standard.yaml")
    if not os.path.isfile(declaration_path):
        print("FAIL: standard.yaml not found — the repository does not declare "
              "AM-MODEL-REPOSITORY-STANDARD adoption (CR-AM-ORG-RES-000).")
        return 1

    declaration = load_yaml(declaration_path, violations, "standard.yaml") or {}
    repository = declaration.get("repository") or {}
    standard = declaration.get("standard") or {}
    model = declaration.get("model") or {}

    if repository.get("type") != "maturity-model":
        violations.append(
            "standard.yaml repository.type must be 'maturity-model' (got %r). "
            "Repositories of other classes must not declare maturity-model conformance."
            % (repository.get("type"),))

    if standard.get("id") != STANDARD_ID:
        violations.append("standard.yaml standard.id must be %r (got %r)."
                          % (STANDARD_ID, standard.get("id")))

    declared_version = str(standard.get("version") or "")
    if not re.match(SEMVER, declared_version):
        violations.append("standard.yaml standard.version must be a SemVer string (got %r)."
                          % (standard.get("version"),))

    conformance = standard.get("conformance")
    if conformance not in CONFORMANCE_LEVELS:
        violations.append("standard.yaml standard.conformance must be one of %s (got %r)."
                          % (sorted(CONFORMANCE_LEVELS), conformance))
    level = CONFORMANCE_LEVELS.get(conformance, 0)

    # --- Identity coherence: standard.yaml vs model.yaml vs VERSION vs README ---
    manifest = None
    manifest_path = os.path.join(root, "model.yaml")
    if os.path.isfile(manifest_path):
        manifest = load_yaml(manifest_path, violations, "model.yaml")
    if manifest:
        if model.get("id") != manifest.get("id"):
            violations.append("standard.yaml model.id (%r) does not match model.yaml id (%r)."
                              % (model.get("id"), manifest.get("id")))
        if str(model.get("version")) != str(manifest.get("version")):
            violations.append("standard.yaml model.version (%r) does not match model.yaml version (%r)."
                              % (model.get("version"), manifest.get("version")))
        if repository.get("type") != manifest.get("type"):
            violations.append("standard.yaml repository.type (%r) does not match model.yaml type (%r)."
                              % (repository.get("type"), manifest.get("type")))

    version_file = read_version_file(root)
    if version_file is not None and str(model.get("version")) != version_file:
        violations.append("standard.yaml model.version (%r) does not match VERSION file (%r)."
                          % (model.get("version"), version_file))

    readme_version = readme_status_version(root)
    if readme_version is not None and str(model.get("version")) != readme_version:
        violations.append("README Status version (%r) does not match declared model.version (%r). "
                          "Documentation must not drift from the authoritative manifest."
                          % (readme_version, model.get("version")))

    # --- Structure checks by declared level ---
    required = list(REQUIRED_PATHS_STRUCTURAL) if level >= 1 else []
    if level >= 2:
        required += REQUIRED_PATHS_FULL
    for rel in required:
        if not os.path.exists(os.path.join(root, rel)):
            violations.append("%s conformance: required path missing: %s"
                              % (conformance, rel))

    if violations:
        for item in violations:
            print("FAIL: %s" % item)
        return 1

    print("OK: %s conforms to %s v%s at conformance level '%s'."
          % (root, STANDARD_ID, declared_version, conformance))
    return 0


if __name__ == "__main__":
    sys.exit(main())
