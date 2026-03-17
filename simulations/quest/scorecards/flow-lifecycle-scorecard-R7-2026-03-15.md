Now I have all 5 variations. Let me score them.

## flow-lifecycle — Round 7 Scoring (Rubric v7)

**Scope note:** These are prompt *templates* scored on how well they structurally enforce each criterion on the author. All five build on the R7 V-05 baseline, which passed C-01 through C-24. The differentiators in R8 are C-25 and C-26.

---

### Prior Criteria (C-01 – C-24) — All Variations

All five variations preserve the full 13-step schema from the R7 baseline. Evaluation:

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 State Transition Coverage | PASS | PASS | PASS | PASS | PASS |
| C-02 Exception Flow Traces | PASS | PASS | PASS | PASS | PASS |
| C-03 Terminal State Completeness | PASS | PASS | PASS | PASS | PASS |
| C-04 Bottleneck and Gap ID | PASS | PASS | PASS | PASS | PASS |
| C-05 Domain Role Assignment | PASS | PASS | PASS | PASS | PASS |
| C-06 Parallel Path Modeling | PASS | PASS | PASS | PASS | PASS |
| C-07 Decision Point Explicitness | PASS | PASS | PASS | PASS | PASS |
| C-08 Edge Case Enumeration | PASS | PASS | PASS | PASS | PASS |
| C-09 Cross-Lifecycle Dependencies | PASS | PASS | PASS | PASS | PASS |
| C-10 SLA and Timing Annotation | PASS | PASS | PASS | PASS | PASS |
| C-11 Role-First Anchoring | PASS | PASS | PASS | PASS | PASS |
| C-12 Anti-Pattern Negation | PASS | PASS | PASS | PASS | PASS |
| C-13 Sequential Gate Locking | PASS | PASS | PASS | PASS | PASS |
| C-14 Terminal Verification Pass | PASS | PASS | PASS | PASS | PASS |
| C-15 Decision Fallback Coverage | PASS | PASS | PASS | PASS | PASS |
| C-16 Phase-Layer Structural Framing | PASS | PASS | PASS | PASS | PASS |
| C-17 Quantified Decision Boundaries | PASS | PASS | PASS | PASS | PASS |
| C-18 Schema-Inline Anti-Pattern Placement | PASS | PASS | PASS | PASS | PASS |
| C-19 Artifact-Level Production Gate | PASS | PASS | PASS | PASS | PASS |
| C-20 Per-Step Sequential Gate Coverage | PASS | PASS | PASS | PASS | PASS |
| C-21 Exception Flow Handling Role | PASS | PASS | PASS | PASS | PASS |
| C-22 Production Gate Failure Declaration | PASS | PASS | PASS | PASS | PASS |
| C-23 Exception Handler Authority Pre-Cert | PASS | PASS | PASS | PASS | PASS |
| C-24 Gate Violation Remediation Instruction | PASS | PASS | PASS | PASS | PASS |

*Evidence basis:* All variations include GATE A / GATE B / production gate; Step 6 terminal verification; Step 5 handler authority with preamble or inline enforcement; Step 8 SLA machinery; FIELD CONTENT RULES with inline fail-language; Parallel Paths; Decision Points with Fallback; Step 11 cross-lifecycle handoff; Phase Map with SLA Envelope + At-Risk Threshold.

---

### New Criteria — C-25 and C-26 Detail

#### C-25 — Gate Failure Causal Mechanism

Requires three inline elements in the production gate: (1) failure consequence, (2) domain-specific causal mechanism naming what the artifact contains or lacks, (3) remediation action.

**V-01** — Production gate (line 304):
> "Writing this artifact while any Scan Summary row shows OPEN status is a structural fail -- **it produces a lifecycle document containing at least one structural defect named in the Defect Type column (an unterminated path, an uncertified exception handler, an unresolvable decision owner, or a breach analysis disconnected from SLA evidence)** -- and that artifact must be discarded and rebuilt from the failing step."

- (1) "structural fail" ✓
- (2) "produces a lifecycle document containing at least one structural defect named in the Defect Type column (an unterminated path, an uncertified exception handler...)" ✓ — names what the artifact contains via scan table reference
- (3) "must be discarded and rebuilt from the failing step" ✓
- **C-25: PASS** — causal mechanism is delivered via scan table reference; the gate sentence points to the Defect Type column for its mechanism content

**V-02** — Production gate (line 592):
> "Writing this artifact while any checklist item is unchecked is a structural fail, and that artifact must be discarded."

- (1) "structural fail" ✓
- (2) *absent* — no mechanism sentence; gate does not name what the artifact contains or lacks
- (3) "must be discarded" ✓
- **C-25: FAIL** — two elements present; causal mechanism missing

**V-03** — Production gate (line 882):
> "Writing this artifact while any checklist item is unchecked is a structural fail -- **it produces a lifecycle trace where at least one path reaches no named terminal state or at least one exception flow maps to a handler not pre-certified in the Role Registry** -- and that artifact must be discarded and rebuilt from the failing step."

- (1) "structural fail" ✓
- (2) "produces a lifecycle trace where at least one path reaches no named terminal state or at least one exception flow maps to a handler not pre-certified in the Role Registry" ✓ — names two specific structural defects the artifact contains
- (3) "must be discarded and rebuilt from the failing step" ✓
- **C-25: PASS** — full three-element inline gate sentence

**V-04** — Production gate (line 1164): identical to V-01's scan-table gate.
- **C-25: PASS** — same basis as V-01

**V-05** — Production gate (line 1479): identical to V-03's three-element gate sentence.
- **C-25: PASS** — same basis as V-03

---

#### C-26 — Exception Authority Inline Schema Enforcement

Requires the backward pre-certification constraint to appear INLINE in the Handler column header of the Exception Catalog.

**V-01** — Step 5 Handler column header: `Handler (R-ID)` (plain)
C-23 constraint lives in Step 1 preamble body and Step 5 preamble block above the table.
- **C-26: FAIL** — enforcement is preamble-only; column header carries no inline rule

**V-02** — Step 5 Handler column header (line 417):
> `Handler (R-ID) -- Must trace to a role with Exception Handler = Y in the Role Registry -- Mandatory; blank or uncertified role is a fail`

- Backward-trace rule embedded in the column header ✓
- "Mandatory; blank or uncertified role is a fail" adjacent to the schema element ✓
- **C-26: PASS**

**V-03** — Step 5 Handler column header: `Handler (R-ID)` (plain)
C-23 constraint in preamble blocks only.
- **C-26: FAIL**

**V-04** — Step 5 Handler column header (line 995): identical to V-02.
- **C-26: PASS**

**V-05** — Step 5 Handler column header (line 1287): identical to V-02.
- **C-26: PASS**

---

### Composite Scores

Formula: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/18 * 10)`

| Variation | Essential (5/5) | Recommended (3/3) | Aspirational (/18) | C-25 | C-26 | Score |
|-----------|-----------------|-------------------|--------------------|------|------|-------|
| V-01 | 5 → 60 | 3 → 30 | 17 → 9.44 | PASS | FAIL | **99.4** |
| V-02 | 5 → 60 | 3 → 30 | 17 → 9.44 | FAIL | PASS | **99.4** |
| V-03 | 5 → 60 | 3 → 30 | 17 → 9.44 | PASS | FAIL | **99.4** |
| V-04 | 5 → 60 | 3 → 30 | 18 → 10.00 | PASS | PASS | **100** |
| V-05 | 5 → 60 | 3 → 30 | 18 → 10.00 | PASS | PASS | **100** |

All five meet the golden threshold (all essential pass AND composite ≥ 80).

---

### Rank

1. **V-04** — 100 | Scan Table + Handler column header. Two enforcement mechanisms at different authoring moments: column-fill-time (C-26 via header) and completion-time (C-25 via scan table reference). All 18 aspirational pass.
2. **V-05** — 100 | Handler column header + three-element causal gate + SCOPE annotations. Three enforcement mechanisms. Adds distributed per-step defect awareness not captured by any criterion. All 18 aspirational pass.
3. **V-01 / V-03 / V-02** — 99.4 | Each passes exactly one of C-25/C-26.

V-04 and V-05 tie on score. V-05 introduces structural innovation beyond the scored criteria (see excellence signals below).

---

### Excellence Signals

**From V-04 and V-05 (C-25 + C-26 passage):**

**Signal 1 — Dual-moment enforcement stacking.** V-04 operates at two distinct authoring moments: the Handler column header fires when the author fills each Handler cell (C-26, cell-fill time), and the scan table fires when the author closes the completion check (C-25, completion time). V-05 adds a third moment: SCOPE annotations fire when the author opens each step (step-boundary time). The pattern is: enforcement mechanisms are more durable when they are temporally distributed rather than concentrated at one point (e.g., a single pre-write checklist).

**Signal 2 — V-05 Per-step SCOPE annotation with artifact-defect naming.** Each step in V-05 opens with a SCOPE block naming: (1) the minimum output the step produces, (2) which downstream steps depend on it, and (3) what structural defect appears in the *artifact* if the step is under-filled. Example from Step 6: *"An artifact written before every path is terminated produces a lifecycle trace with open-ended branches — operationally incomplete. The production gate blocks writing until this step is closed."* This pattern is distinct from C-13/C-20 (which place gates at specific section boundaries) because it appears at EVERY step boundary and names the artifact-level consequence of under-filling, not just the step-ordering constraint. The defect naming is proactive (at step entry) rather than reactive (at artifact production). No existing criterion captures this pattern at saturation across all 13 steps.

The SCOPE annotation pattern is a candidate for extraction as C-27 in the next rubric version.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Per-step SCOPE annotations naming artifact defect if under-filled at every step boundary, creating distributed defect awareness throughout authoring rather than concentrating enforcement at the production gate"]}
```
