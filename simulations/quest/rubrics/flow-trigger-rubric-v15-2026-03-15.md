**flow-trigger-rubric-v15** written to `simulations/quest/rubrics/flow-trigger-rubric-v15-2026-03-16.md`.

---

**Two new aspirational criteria (C-42, C-43), N_aspirational: 33 → 35, max (raw): 147.5 → 152.5:**

| ID | Source | What it captures | Extends |
|----|--------|-----------------|---------|
| C-42 | V-05 extended bracket form — `[must be VALUE — inline rationale clause]` — where the consequence clause is syntax-bound inside the bracket, not a separate assertion line or prose sentence | Consequence-embedded assertion brackets: rationale clause is part of the constraint annotation syntax itself, making rationale removal require editing the bracket value rather than deleting a separate element | C-41 (same register requirement — C-42 requires rationale inside the bracket, not just in the same register); mirrors C-40→C-41 logic applied one level deeper: C-40 = fence inseparability, C-41 = register co-domain, C-42 = syntactic co-location of constraint and justification |
| C-43 | V-05 `REMEDIATION SELF-SUFFICIENCY: maintained [must be maintained — ...]` assertion — subject is a derived guarantee of two elements in combination, not either element alone | Systemic-property assertions in embedded NOTE blocks: at least one assertion in the NOTE block asserts a higher-order property of the element combination, not just element presence — making the combined guarantee explicit, detectable, and independently falsifiable | C-41 (same register domain); C-35 (DERIVATION TEST analogue: just as the derivation test proves failure mode labels specify all mechanism requirements, a systemic-property assertion proves the element combination achieves the named functional guarantee) |

**Structural relationship:** C-41 requires assertion-register parity (same `PROPERTY: VALUE [must be VALUE]` form). C-42 requires that the rationale for each constraint be embedded inside the bracket (`[must be VALUE — reason]`) rather than expressed as a separate line — making the justification syntax-bound to the obligation. C-43 requires that at least one assertion in the NOTE block assert a combined-system property (self-sufficiency, accountability closure) rather than only element presence — ensuring the functional guarantee of the element combination is explicitly asserted, not merely inferable.

Together, C-42 and C-43 capture the two axes of V-05's NOTE block that go beyond C-41: the extended bracket form, and the systemic-property assertion that makes `REMEDIATION SELF-SUFFICIENCY` a first-class detection target rather than an implicit inference from element presence.
