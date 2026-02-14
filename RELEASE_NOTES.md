# VEIP 0.1.0 – Public Working Draft Release Notes 

Release Date: 02/14/2026

Status: Public Working Draft

## Overview

VEIP 0.1.0 establishes the initial public specification for the Veraxis Execution Integrity Protocol.

This release defines the foundational execution-control semantics required to govern action-taking AI systems.

## Core Deliverables

VEIP 0.1.0 formally defines:

- Deterministic State-Transition Model
- Execution-Time Authorization Classification
- Authority Envelope Semantics
- Supervisory Verification Interface (SVI)
- Evidence Pack Schema (v0.1.0)
- Conformance Test Suite (CTS) Structure
- Versioning and Governance Framework
- VEIP Improvement Proposal (VIP) Process

## Foundational Invariants Introduced

1. Execution Authorization Precedes Action.
2. No Hidden Execution Paths.
3. Deterministic Replay Requirement.
4. Supervisory Classification Must Be Explicit.
5. Conformance Defined by Behavioral Semantics.

## Conformance Scope

VEIP 0.1.0 defines baseline conformance (VEIP-Core).

Extended profiles (e.g., AML, Agentic Systems) are defined separately.

## Known Limitations

- Cryptographic binding profiles are not yet finalized.
- Multi-registry federation model is defined conceptually but not operationalized.
- Evidence Pack schema may receive non-breaking clarifications prior to 1.0.

## Intended Audience

- Financial regulators
- AI system integrators
- Risk and compliance architects
- Standards bodies
- Academic researchers

## Upgrade Path to 1.0

The 1.0 release will:

- Finalize Evidence Pack structure.
- Lock transition invariants.
- Publish normative CTS vectors.
- Stabilize supervisory escalation semantics.
