# VEIP-Core Formal Invariants

## 1. System Model

Let:

S = finite set of system states  
A = set of proposed actions  
D = {ALLOW, DENY, ESCALATE, SUPERVISORY}  
E = set of Evidence Packs  
Auth = Authority Envelope function  

Define:

δ : S × A → D  
τ : S × D → S  
ε : S × A × D → E  

Where:

δ = authorization classifier  
τ = state transition function  
ε = evidence emission function  

---

## 2. Invariant I — Authorization Precedes Execution

∀ s ∈ S, ∀ a ∈ A:

If τ(s, δ(s,a)) = EXECUTED  
Then δ(s,a) = ALLOW  

Formally:

τ(s, δ(s,a)) = EXECUTED ⇒ δ(s,a) = ALLOW  

Execution without ALLOW classification is prohibited.

---

## 3. Invariant II — Deterministic Classification

Given identical inputs:

If (s₁ = s₂) ∧ (a₁ = a₂) ∧ (Auth₁ = Auth₂)

Then:

δ(s₁, a₁) = δ(s₂, a₂)

Authorization MUST be deterministic.

---

## 4. Invariant III — Total Transition Definition

∀ s ∈ S, ∀ d ∈ D:

If δ(s,a) = d  
Then τ(s,d) is defined  

Undefined transitions are prohibited.

---

## 5. Invariant IV — Evidence Emission Completeness

∀ s ∈ S, ∀ a ∈ A:

∃ e ∈ E such that:

e = ε(s, a, δ(s,a))

Every decision MUST produce an Evidence Pack.

---

## 6. Invariant V — Replay Equivalence

Let ε(s,a,d) = e  

Given replay input identical to (s,a,Auth):

Recomputed decision d' must satisfy:

d' = d  

Replay classification equivalence is mandatory.

---

## 7. Invariant VI — No Hidden Execution Paths

∀ s ∈ S, ∀ a ∈ A:

If τ(s, d) = EXECUTED  
Then ∃ δ(s,a) evaluated  

Execution without explicit classification is prohibited.

---

## 8. Invariant VII — Supervisory Resolution Constraint

If δ(s,a) = SUPERVISORY

Then:

τ(s,SUPERVISORY) ≠ EXECUTED  
Until supervisory resolution occurs.

Supervisory resolution is required prior to execution.

---

These invariants define VEIP-Core conformance at a formal level.

Any implementation violating these invariants is non-conformant.
