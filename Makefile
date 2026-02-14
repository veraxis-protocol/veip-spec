SHELL := /bin/bash

REQUIRED_FILES = \
  README.md LICENSE GOVERNANCE.md TRADEMARKS.md VERSIONING.md VIP_PROCESS.md RELEASE_NOTES.md ECOSYSTEM.md \
  docs/architecture.md docs/regulatory-positioning.md docs/multi-operator-registry-model.md docs/public-working-draft.md docs/roadmap-to-1.0.md docs/regulator-briefing-memo.md \
  spec/state-transition-model.md spec/supervisory-verification-interface.md spec/evidence-pack-schema.md spec/conformance-test-suite.md spec/formal-invariants.md \
  profiles/README.md \
  schemas/veip-evidence-pack.schema.json

.PHONY: check check-files check-links check-schema

check: check-files check-links check-schema

check-files:
	@set -e; \
	for f in $(REQUIRED_FILES); do \
	  if [[ ! -f $$f ]]; then \
	    echo "Missing required file: $$f"; exit 1; \
	  fi; \
	done; \
	echo "OK: required files present"

check-links:
	@set -e; \
	# Fail on common broken relative links: ](spec/...), ](docs/...) when used from subdirs.
	# This is a light heuristic. It catches the most common mistakes.
	# Rule: from docs/*.md you should use ../spec/ or ../schemas etc.
	bad=0; \
	while IFS= read -r file; do \
	  if [[ $$file == docs/* ]]; then \
	    if grep -nE '\]\((spec/|schemas/|profiles/|vip/)' "$$file" >/dev/null; then \
	      echo "Bad relative link in $$file: docs/* must use ../spec, ../schemas, etc."; \
	      grep -nE '\]\((spec/|schemas/|profiles/|vip/)' "$$file" || true; \
	      bad=1; \
	    fi; \
	  fi; \
	done < <(git ls-files '*.md'); \
	if [[ $$bad -ne 0 ]]; then exit 1; fi; \
	echo "OK: basic link heuristics passed"

check-schema:
	@set -e; \
	python3 - <<'PY' \
import json, sys, pathlib \
p = pathlib.Path("schemas/veip-evidence-pack.schema.json") \
try: \
    data = json.loads(p.read_text(encoding="utf-8")) \
except Exception as e: \
    print(f"Schema JSON invalid: {e}") \
    sys.exit(1) \
required = ["$schema", "title", "type"] \
missing = [k for k in required if k not in data] \
if missing: \
    print(f"Schema missing keys: {missing}") \
    sys.exit(1) \
if data.get("type") != "object": \
    print("Schema type must be 'object'") \
    sys.exit(1) \
print("OK: schema JSON parses and has basic structure") \
PY
