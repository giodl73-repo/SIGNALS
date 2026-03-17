# Quest Score — campaign-specify (Round 2)

**Rubric:** v2 (13 criteria: 5 essential / 3 recommended / 5 aspirational)
**Scoring formula:** `(essential/5 * 60) + (recommended/3 * 30) + (aspirational/5 * 10)`
**Golden threshold:** all 5 essential pass AND composite >= 80

---

## Criterion Evaluation

### Essential Criteria (60 pts)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Three artifacts produced | PASS | PASS | PASS | PASS | PASS |
| C-02 | Spec has all six required sections | PASS | PASS | PASS | PASS | PASS |
| C-03 | Proposal has 3+ options incl. do-nothing | PASS | PASS | PASS | PASS | PASS |
| C-04 | Pitch covers three audience versions | PASS | PASS | PASS | PASS | PASS |
| C-05 | Cross-artifact consistency | PASS | PASS | PASS | PASS | PASS |

**Evidence notes:**

- **C-01 across all**: Every variation includes an active Completion Gate that triggers re-write, not just a reminder. Phrasing ranges from "Do not end this skill with an empty row" (V-01/V-05) to "End only when all three are confirmed Y on disk" (V-02) to "Do not end until all three files are on disk" (V-03/V-04).
- **C-02**: V-01/V-05 use mark-as-done checklist tables; V-02/V-03/V-04 use explicit section enumerations with "no section may be omitted" or equivalent.
- **C-03**: All variations require "Option 1: Do Nothing" as a named required option. V-04/V-05 additionally require "full treatment" for Do Nothing (pros/cons/risk/effort listed).
- **C-05 V-02**: Handoff statements force inheritance confirmation: "Feature name and core behavior must match the handoff exactly." Strongest C-05 mechanism in the set. V-05 matches V-02's handoff confirmation plus adds Phase 0 anchoring.

---

### Recommended Criteria (30 pts)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Spec self-review flags gaps | PASS | PASS | PASS | PASS | PASS |
| C-07 | Pitch contains anti-positioning section | PASS | PASS | PASS | PASS | PASS |
| C-08 | Recommendation cites trade-off rationale | PASS | PASS | PASS | PASS | PASS |

**Evidence notes:**

- **C-06 across all**: Self-Review is a required section in all five. V-01/V-05 checklist row: `"No gaps" fails this row`. V-02: `"No issues found is not acceptable"`. V-03: `"If you wrote 'no gaps' — that is a gap"`. Identical enforcement across register styles.
- **C-07 across all**: Anti-Positioning present in all pitch sections. V-04/V-05 specify that the first statement must address the most common status quo workaround — stronger framing than the baseline.
- **C-08 V-01**: Trade-off sentence template included in Recommendation row. PASS.
- **C-08 V-02**: Explicit falsifiability test — `"Option 2 is best does not pass"`. Strongest C-08 constraint in the set. PASS.
- **C-08 V-04/V-05**: Recommendation must name Do Nothing specifically: `"We chose [X] over Do Nothing because [specific Option 1 cost], and over [Y] because [specific trade-off]."` Forces comparison against a named concrete baseline, not just abstract options. PASS — qualitatively strongest.
- **C-08 V-03**: `"We chose [option] over [option] because [specific constraint or risk from above], accepting [what we give up]."` Traceable to options. PASS.

---

### Aspirational Criteria (10 pts)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-09 | Scout signal pull-through | PASS | PASS | PASS | PASS | PASS |
| C-10 | Audience voice differentiation | PASS | PASS | PASS | PASS | PASS |
| C-11 | Completion Check fail-safe | PASS | PASS | PASS | PASS | PASS |
| C-12 | Phase 0 audience framing pre-write | PASS | **FAIL** | PASS | PASS | PASS |
| C-13 | Namespace-targeted per-phase scout pull | PASS | PASS | PASS | PASS | PASS |

**Evidence notes:**

- **C-09 across all**: All five phase their scout pulls. Phase 1 reads broadly from `simulations/scout/`, Phase 2 targets `scout/feasibility/`, Phase 3 targets `scout/positioning/`. Pull-through is instructed, not assumed.
- **C-10 V-01/V-03/V-04/V-05**: Phase 0 establishes audience contracts before Phase 1 writing begins. Phase 3 requires each version to open with a sentence traceable to its contract, and V-05 adds `"If two match: rewrite the later one before marking DONE"`. PASS.
- **C-10 V-02**: No Phase 0. Phase 3 specifies distinct lead patterns for each version (outcome-first / capability-first / "you can now...") but no pre-established contract. The structural instructions are sufficient to produce differentiated voices in a cooperative model, but the mechanism is weaker — no enforcement gate. PASS on structural read, but noted as the predicted C-10 risk.
- **C-11 across all**: All five include an active recovery gate, not a passive warning. This criterion is axis-independent — every variation picked it up.
- **C-12 V-02**: Deliberately absent to isolate C-12's effect on C-10. FAIL (as designed).
- **C-12 V-03**: `"Before writing anything: state the audience frame"` block precedes Phase 1. States feature sentence + one phrase per audience. Qualifies as a dedicated pre-write phase per rubric: voice contracts defined upfront, phase boundary is explicit. PASS — borderline, but the block is labeled, required, and precedes Phase 1 writing.
- **C-13 across all**: Phase 2 invariably uses `simulations/scout/feasibility/`; Phase 3 invariably uses `simulations/scout/positioning/`. The single-glob-at-start failure mode is absent in every variation.

---

## Score Summary

| ID | Axis | Essential | Rec | Asp | Composite | Golden? |
|----|------|-----------|-----|-----|-----------|---------|
| V-01 | Checklist-before-write | 5/5 | 3/3 | 5/5 | **100** | YES |
| V-02 | Explicit handoff protocol (no Phase 0) | 5/5 | 3/3 | 4/5 | **98** | YES |
| V-03 | Imperative runbook register | 5/5 | 3/3 | 5/5 | **100** | YES |
| V-04 | Inertia framing | 5/5 | 3/3 | 5/5 | **100** | YES |
| V-05 | Combination (checklist + handoff + inertia) | 5/5 | 3/3 | 5/5 | **100** | YES |

**V-02** is the sole differentiator: C-12 fails by design, confirming Phase 0 audience framing is the specific mechanism behind full aspirational coverage.

---

## Ranking

1. **V-01 / V-03 / V-04 / V-05** — 100/100 (tied)
2. **V-02** — 98/100 (C-12 deliberate fail)

---

## Excellence Signals from Round 2

### From V-04 (inertia framing — new axis)
**Pattern: Per-audience inertia cost in Phase 0**
Naming the specific cost of inaction for exec/developer/maker in Phase 0 produces more concrete trade-off rationale (C-08) and more distinctive pitch hooks (C-10) than voice register labels alone. The audience contract is anchored to something the audience *loses* without the feature, not just the register they speak in. This makes the pitch version differentiation substantive rather than stylistic.

**Pattern: Do Nothing as named falsifiable baseline**
V-04/V-05 require the Recommendation to defeat Do Nothing by name — `"We chose [X] over Do Nothing because [specific Option 1 cost]"`. This converts C-08 from format compliance to argumentative completeness. A recommendation that doesn't defeat the status quo explicitly is structurally incomplete.

### From V-02 (isolation finding)
**Confirmed: C-12 is not required for C-05 (consistency)**
Explicit handoff confirmation (Phase N+1 must restate Phase N values verbatim and confirm match before writing) achieves C-05 reliability without Phase 0 framing. The two mechanisms are independent. This opens a path for a leaner variation that trades Phase 0 for a handoff-only consistency model — with known C-10 risk if voice instructions are underspecified.

### From V-03 (register finding)
**Confirmed: Imperative register achieves identical structural coverage to persona register**
V-03's "do this / write this / check this" command style produces the same criterion pass rate as V-01's "Role: Architect" persona framing. No criterion degrades from removing the persona header. This suggests persona framing adds zero structural reliability — it is a register choice, not a mechanism.

---

## Predicted Differentiators — Outcome vs. Prediction

| Prediction | Outcome |
|-----------|---------|
| C-10 failure on V-02 (no Phase 0) | PASS — voice instructions sufficient at structural level. Risk remains for cooperative models only. |
| C-08 strength on V-04 | CONFIRMED — "defeat Do Nothing by name" is the strongest C-08 formulation in the set. |
| C-11 universal across all five | CONFIRMED — axis-independent, appears in every variation. |
| C-12 edge case on V-03 inline framing | Resolved PASS — labeled, required, precedes Phase 1. |

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["per-audience inertia cost in Phase 0 drives more concrete pitch differentiation than voice register labels alone", "do-nothing as named falsifiable baseline in recommendation forces argumentative completeness not just format compliance", "handoff confirmation protocol achieves cross-artifact consistency independent of Phase 0 framing", "imperative register achieves identical structural coverage to persona register with no criterion degradation"]}
```
