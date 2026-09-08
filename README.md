> ⚠️ **VEIP 0.1.0 – Public Working Draft**
>
> This version of the Veraxis Execution Integrity Protocol (VEIP) is released as a Public Working Draft.
>
> The specification is stable in principle but may undergo structural clarification, terminology refinement, and formal consistency updates prior to a 1.0 release.
>
> Implementations built against this draft should explicitly declare conformance to “VEIP 0.1.0 (Public Working Draft)”.
>
> Breaking changes may occur before 1.0.

# Veraxis Execution Integrity Protocol (VEIP) Specification

## Role in Open Institutional Computation

**Category:** Open Institutional Computation  
**This component:** Normative execution-integrity protocol specification — the runtime boundary at which established machine-operational authority/control state is bound to an exact action and to verifiable evidence  
**Upstream:** Machine-operational authority or control state, already established through authorized institutional interpretation and admission (the Veraxis reference path for that upstream problem is [OIC — Open Institutional Compiler](https://github.com/veraxis-protocol/Institutional-Compiler))  
**Downstream:** Conformant implementations, supervisory verification, and Evidence Packs consumed by verifiers, registries, and enforcement runtimes  
**Canonical category thesis:** https://github.com/veraxis-protocol/institutional-continuity/blob/main/THESIS.md

Architectural role does not imply production readiness; see this repository's status, versioning, and conformance documentation for the exact demonstrated scope.

## Overview

The Veraxis Execution Integrity Protocol (VEIP) defines a deterministic execution-control standard for AI and automated systems.

VEIP formalizes:

- State-transition integrity
- Execution-time authorization semantics
- Supervisory verification interface (SVI)
- Deterministic evidence packaging
- Conformance validation requirements

VEIP is an open specification.

This repository contains the normative standard documents and JSON schemas that define VEIP behavior.

### VEIP's position in the architecture

VEIP is the execution-integrity protocol within Open Institutional Computation. It consumes machine-operational authority or control state established upstream and binds/preserves that state across the boundary to an exact proposed action, runtime classification, execution transition, and verifiable evidence.

VEIP does not determine the institutional meaning of governing documents, perform institutional admission, or originate institutional authority.

OIC provides the Veraxis reference path for the upstream institutional compilation problem.

An Evidence Pack / Authorization Evidence Pack is a downstream evidence artifact used by the architecture. It is not VEIP itself and does not create the authority it records.

## Foundational Invariants

1. Execution Authorization Precedes Action.
2. All State Transitions Must Be Verifiable.
3. Evidence Must Be Deterministic and Replayable.
4. Supervisory Oversight Must Be Explicit.
5. No Hidden Execution Paths.

These invariants define VEIP compliance.

## Scope

The VEIP specification governs:

- State-transition formalism
- Authority envelope semantics
- Evidence Pack structure
- Conformance Test Suite definitions
- Versioning discipline

The specification does not govern:

- Commercial implementations
- Registry operations
- Jurisdiction-specific regulatory mandates

## Licensing

The VEIP specification is licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).

This permits unrestricted implementation, adaptation, and commercialization of VEIP-compliant systems, provided attribution is maintained.

Official certification and use of VEIP certification marks are governed separately (see TRADEMARKS.md).

## Version

Current Specification Version: 0.1.0 (Draft)

## Specification Documents

- [State-Transition Model](spec/state-transition-model.md)
- [Supervisory Verification Interface](spec/supervisory-verification-interface.md)
- [Evidence Pack Schema](spec/evidence-pack-schema.md)
- [Formal Invariants](spec/formal-invariants.md)
- [Conformance Test Suite](spec/conformance-test-suite.md)

