# State-Transition Model

VEIP models system behavior as deterministic state transitions.

Each proposed action SHALL originate in the PROPOSED state.

Transitions MUST be classified as:

- ALLOW
- DENY
- ESCALATE
- SUPERVISORY

Unauthorized transitions SHALL NOT result in execution.

Every transition MUST produce a VEIP Evidence Pack.
