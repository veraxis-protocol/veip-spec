SHELL := /bin/bash
.PHONY: help check schema ci

help:
	@echo "Targets:"
	@echo "  make check   - required files + basic structure checks"
	@echo "  make schema  - parse the canonical schema as JSON"
	@echo "  make ci      - check + schema"

check:
	@set -euo pipefail; \
	req=(README.md LICENSE LICENSE.md GOVERNANCE.md VERSIONING.md VIP_PROCESS.md schemas/veip-evidence-pack.schema.json); \
	for f in "$${req[@]}"; do \
	  if [[ ! -f "$$f" ]]; then echo "Missing required file: $$f"; exit 1; fi; \
	done; \
	echo "OK: required files present"

schema:
	@python -c "import json,pathlib,sys; p=pathlib.Path(\"schemas/veip-evidence-pack.schema.json\");\
	  (p.exists() or (print(\"ERROR: missing schemas/veip-evidence-pack.schema.json\"), sys.exit(1)));\
	  json.loads(p.read_text(encoding=\"utf-8\"));\
	  print(\"OK: schema JSON parses:\", p)"

ci: check schema
