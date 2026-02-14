# VEIP Ecosystem Architecture

                    ┌──────────────────────────┐
                    │        veip-spec         │
                    │  Open Standard (CC-BY)   │
                    │  - State Model           │
                    │  - SVI                  │
                    │  - Evidence Schema      │
                    │  - CTS Definitions      │
                    └─────────────┬────────────┘
                                  │
                                  ▼
                    ┌──────────────────────────┐
                    │        veip-sdk          │
                    │   MIT Reference Runtime  │
                    │  - Authorization Gate    │
                    │  - Evidence Emitter      │
                    └─────────────┬────────────┘
                                  │
                                  ▼
                    ┌──────────────────────────┐
                    │   veip-verifier-core     │
                    │  Source-Available Engine │
                    │  - Deterministic Replay  │
                    │  - Transition Validation │
                    │  - Conformance Checks    │
                    └─────────────┬────────────┘
                                  │
                                  ▼
                    ┌──────────────────────────┐
                    │      veip-registry       │
                    │  Certification Authority │
                    │  - Conformance Issuance  │
                    │  - Attestation Records   │
                    │  - Certification Marks   │
                    └──────────────────────────┘
