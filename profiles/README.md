# VEIP Profiles

VEIP Profiles define domain-specific constraint layers built on top of VEIP-Core.

Profiles do not alter foundational invariants.  
They extend or specialize conformance criteria for specific regulatory or operational domains.

All profiles MUST remain compatible with VEIP-Core semantics.

---

## VEIP-Core

Baseline conformance level.

Requirements:

- Deterministic state-transition enforcement
- Authority envelope validation
- Evidence Pack emission
- Supervisory classification semantics
- Replay validation capability

VEIP-Core defines minimum compliance.

---

## VEIP-AML

Domain: Anti-Money Laundering / Financial Crime

Additional Requirements:

- Explicit escalation triggers for suspicious classification
- Immutable linkage between risk score context and Evidence Pack
- Mandatory supervisory resolution for threshold exceedance
- Enhanced provenance metadata (case ID, alert lineage)

VEIP-AML ensures that automated AML systems maintain audit-grade determinism.

---

## VEIP-Agentic

Domain: Autonomous / Agentic AI Systems

Additional Requirements:

- Multi-step transition chaining validation
- Nested authority envelope validation
- Explicit interruption semantics
- Prohibition of implicit recursive transitions
- Deterministic rollback support

VEIP-Agentic formalizes governance for autonomous agents capable of initiating multi-stage actions.

---

## Future Profiles (Illustrative)

- VEIP-Insurance
- VEIP-Critical Infrastructure
- VEIP-Public Sector

Profiles SHALL:

- Declare binding VEIP version.
- Define additional CTS vectors.
- Not weaken baseline invariants.
