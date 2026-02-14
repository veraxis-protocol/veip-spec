# Conformance Test Suite (CTS)

## 1. Purpose

The VEIP Conformance Test Suite (CTS) defines the behavioral criteria required for VEIP compliance.

Conformance is determined by execution behavior, not by artifact structure alone.

An implementation MUST satisfy all mandatory CTS scenarios to claim VEIP compliance.

## 2. Conformance Categories

CTS is divided into five categories:

### 2.1 Transition Integrity

The implementation MUST:

- Reject execution without prior authorization.
- Enforce valid state transitions.
- Prevent undefined transitions.

### 2.2 Authority Enforcement

The implementation MUST:

- Enforce authority validity windows.
- Reject actions outside permitted scope.
- Correctly classify DENY vs ESCALATE semantics.

### 2.3 Evidence Emission

The implementation MUST:

- Emit an Evidence Pack for every decision.
- Ensure required fields are present.
- Produce deterministic output for identical inputs.

### 2.4 Supervisory Semantics

The implementation MUST:

- Require supervisory resolution for SUPERVISORY classification.
- Record supervisory decision in Evidence Pack.
- Prevent execution prior to resolution.

### 2.5 Replay Validation

The implementation MUST:

- Support deterministic replay of transitions.
- Reproduce identical classification results for identical inputs.

## 3. Test Vector Structure

Each CTS scenario SHALL include:

- Authority Envelope definition
- Action proposal
- Expected decision classification
- Expected state transition
- Expected Evidence Pack output fields
- Replay validation result

## 4. Mandatory vs Optional Tests

Mandatory tests define minimum compliance.

Optional tests define extended profile capabilities.

Certification-level compliance may require extended test categories.

## 5. Version Binding

Each CTS release SHALL bind explicitly to:

- VEIP specification version
- Evidence Pack schema version

Implementations MUST declare CTS version used for validation.

## 6. Certification Distinction

Passing public CTS does not grant certification.

Official certification requires registry validation and attestation.
