# VEIP Ecosystem Overview

The Veraxis Execution Integrity Protocol (VEIP) is structured as a layered ecosystem designed to balance openness, interoperability, and supervisory integrity.

The VEIP specification (veip-spec) defines the open, normative standard for deterministic state-transition control, execution-time authorization semantics, and structured Evidence Packs. It is licensed openly to enable unrestricted implementation and regulatory citation.

The VEIP SDK (veip-sdk) provides a permissive, MIT-licensed reference implementation demonstrating how the specification may be implemented in practice. It accelerates ecosystem adoption but does not confer certification status.

The VEIP Verifier Core (veip-verifier-core) implements deterministic replay validation, conformance checking, and integrity enforcement. It ensures that implementations do not merely resemble VEIP structurally but conform to its formal invariants.

The VEIP Registry (veip-registry) operates as the certification and attestation authority. It governs issuance of official conformance certificates and maintains supervisory validation records.

This layered structure separates standard definition from enforcement and certification authority. The specification remains open and neutral, while certification remains controlled and auditable.

Together, these components form a governance-grade execution control-plane for AI systems that reduces supervisory ambiguity without centralizing implementation control.
