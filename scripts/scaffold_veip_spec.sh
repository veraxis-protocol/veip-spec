#!/usr/bin/env bash
set -euo pipefail

# VEIP Spec scaffold: gold-standard structure
# Run from repository root.

mkdir -p docs spec schemas profiles vip scripts .github/workflows

# Top-level governance + release artifacts
touch \
  README.md \
  LICENSE \
  GOVERNANCE.md \
  TRADEMARKS.md \
  VERSIONING.md \
  VIP_PROCESS.md \
  RELEASE_NOTES.md \
  ECOSYSTEM.md

# Docs
touch \
  docs/architecture.md \
  docs/regulatory-positioning.md \
  docs/multi-operator-registry-model.md \
  docs/public-working-draft.md \
  docs/roadmap-to-1.0.md \
  docs/regulator-briefing-memo.md

# Spec (normative)
touch \
  spec/state-transition-model.md \
  spec/supervisory-verification-interface.md \
  spec/evidence-pack-schema.md \
  spec/conformance-test-suite.md \
  spec/formal-invariants.md

# Profiles
touch profiles/README.md

# Schema
touch schemas/veip-evidence-pack.schema.json

# VIP directory placeholder
touch vip/.gitkeep

# Makefile and CI workflow (added below)
touch Makefile
touch .github/workflows/ci.yml

echo "Scaffold created."
echo "Next:"
echo "  1) Populate LICENSE (CC BY 4.0 text)"
echo "  2) Populate README and spec/*.md docs"
echo "  3) Populate schemas/veip-evidence-pack.schema.json"
echo "  4) Add CI + Makefile checks"
