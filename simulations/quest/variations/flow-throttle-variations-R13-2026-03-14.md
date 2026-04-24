Here are the 5 complete variations for Round 13:

---

## R13 Variations — flow-throttle (v13 Rubric, 184-point max)

**What these variations test:** C-37 (labeled evaluator-role declaration in barrier) and C-38 (heading-role semantic root alignment).

| Variation | Axis | C-37 | C-38 | Predicted |
|-----------|------|------|------|-----------|
| **V-01** | Single: `"Evaluator:"` label keyword — tests C-37 label-keyword inertness | PASS | PASS | **184/184** |
| **V-02** | Single: `"Role: Capacity ceiling analyst."` — label present but no shared root with `"Entitlement Verification"` heading | PASS | FAIL | **181/184** |
| **V-03** | Single: Generic framing sentence, no explicit label keyword | FAIL | FAIL | **178/184** |
| **V-04** | Combination: `"Analyst:"` keyword + `"Documentation Accuracy Review"` / `"Documentation accuracy analyst"` semantic pair + conversational register | PASS | PASS | **184/184** |
| **V-05** | Combination: No role label (generic framing) + inertia framing as secondary axis (prominent Phase 0 with status-quo competitor) | FAIL | FAIL | **178/184** |

**Score spread: 184 / 181 / 178 / 184 / 178**

---

### What each variation proves if the hypothesis holds

**V-01** — `"Evaluator:"` satisfies C-37 as well as `"Role:"`. C-37 is label-keyword-inert (same semantic pair, different keyword).

**V-02** — C-38 requires the shared semantic root, not just C-37's presence. `"Capacity ceiling analyst"` + `"Entitlement Verification"` share no root → C-38 fails even though C-37 passes. This establishes the C-38 failure boundary at exactly −3 points.

**V-03** — Generic framing (`"This section applies documentation-standard verification..."`) fails C-37. The explicit label keyword is required — contextual orientation without it doesn't satisfy the criterion. C-37 failure boundary = −6 points total (C-37 + C-38 by dependency).

**V-04** — `"Analyst:"` as a third label keyword passes C-37. `"documentation accuracy"` as a third semantic pair passes C-38. Confirms both criteria are text-inert beyond the two confirmed examples from R12 V-04.

**V-05** — C-37/C-38 absence costs exactly 6 points regardless of surface-level variation. An expanded, inertia-prominent Phase 0 (status-quo competitor section, do-nothing comparison, more elaborate baseline framing) does not substitute for the labeled declaration at the barrier.

Output written to `simulations/quest/rubrics/flow-throttle-rubric-v13-variations-R13-2026-03-15.md`.
