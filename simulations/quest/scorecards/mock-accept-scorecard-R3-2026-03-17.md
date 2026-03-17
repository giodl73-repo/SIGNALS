# mock-accept Round 3 — Quest Score

## Scoring Method

- **Essential**: 12 pts each, max 60. One FAIL → cap 55. Two FAILs → cap 43.
- **Recommended**: 10 pts each, max 30. PARTIAL = 5.
- **Aspirational**: binary PASS per criterion, pool = (passes / 10) × 10.

---

## V-01 — Lifecycle Emphasis

### Essential (60/60)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Auto-flag rules | PASS | Rule A/B/C all use artifact-as-subject; standing rule prohibits "I found…" / "This namespace has…" |
| C-02 | Forbidden triad | PASS | All three labels present; "A two-of-three set does not satisfy this gate." ✓ |
| C-03 | Status writeback + Canary | PASS | "Use Edit tool for each namespace." CANARY ASSERTION + CANARY-FALSE-POSITIVE + CANARY SUPPRESSED all present |
| C-04 | Review artifact structure | PASS | "ONE Write call. No sections outside this Write block." All 4 sections; Coverage table 4-col; urgency labels |
| C-05 | MOCK-ACCEPTED positive argument | PASS | Slot 1 and Slot 2 separated by `---`; explicit Constraint + Revert-on-violation; "Paraphrase is a violation" |

### Recommended (30/30)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | Entity-naming in roles | PASS | "Required artifact citation: The mock artifact's [namespace] section [field: X, token: Y, slot: Z]" in both evaluation phases |
| C-07 | Step sequencing + guard | PASS | Arch-blocked / Strategy-blocked initialized; "Arch-blocked: [list] / none" explicit; partition N+M=total in every gate |
| C-08 | Eval-driven REAL-REQUIRED | PASS | 5-field template present: Trigger condition + SQ (artifact-as-subject) + Artifact state + Verdict + Required action; VERDICT-ECHO named |

### Aspirational (8/10 → 8 pts)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Artifact-as-subject grammar | PASS | Standing rule at top: "PASS: 'The mock artifact's…'" |
| C-10 | Tier sourcing | PASS | Phase 0: "Tier: [N] (source: TOPICS.md \| --tier \| default)" |
| C-11 | Inline completeness gate | PASS | GATE A: "[N present] + [M absent] = [total]. Expected: 9." GATE B: three-way count |
| C-12 | Reason-code at point of use | PASS | Phase 5 Slot 1: "Constraint: Write exactly…" immediately below Reason field; Phase 2/3 inline tokens |
| C-13 | Phase exit assertions | PASS | GATE A–F each include count + "Do not proceed to Phase N+1 until GATE [X] is written" |
| C-14 | Blank-line failure signal | **FAIL** | Uses bracket notation `[name]` / `[list]`, not `___` blank slots |
| C-15 | Forbidden-form enumeration | PASS | "FAIL: 'I found…' / 'This namespace has…' / 'There is no…'" explicitly enumerated in standing rule |
| C-16 | Written-gate blocking language | PASS | Every GATE: "Do not proceed to Phase N+1 until GATE [X] is written." |
| C-17 | Named gate registry | PASS | GATE A through GATE F — stable named registry across 6 phase transitions |
| C-18 | Constraint-field co-location | **FAIL** | Phase 5 slots have explicit Constraint: blocks; Phase 2/3 embed constraints inline in template notation (no separate framed CONSTRAINT block) |

**V-01 Composite: 60 + 30 + 8 = 98.0**

---

## V-02 — Phrasing Register

### Essential (60/60)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Rule A/B/C artifact-as-subject form ✓ |
| C-02 | PASS | Three labels + "two-of-three does not satisfy" ✓ |
| C-03 | PASS | Edit + CANARY ASSERTION + CANARY-FALSE-POSITIVE + CANARY SUPPRESSED ✓ |
| C-04 | PASS | ONE Write call, 4 sections, 4-col table, urgency labels ✓ |
| C-05 | PASS | Slot 1/2 separate, Constraint + Revert-on-violation, paraphrase named ✓ |

### Recommended (30/30)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | Required artifact citation in both evaluation phases ✓ |
| C-07 | PASS | Named accumulators, partition explicit, "none" declared ✓ |
| C-08 | PASS | 5-field template including SQ field present in Phases 2/3 ✓ |

### Aspirational (7/10 → 7 pts)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | Standing rule present with PASS form ✓ |
| C-10 | PASS | Phase 0: "Tier: [N] (source: TOPICS.md \| --tier \| default)" ✓ |
| C-11 | PASS | Phase 1 completeness count; Phase 2 partition count |
| C-12 | PASS | Phase 5 constraints at point of use; Phase 2/3 inline token constraints |
| C-13 | PASS | PHASE 1/2/3 EXIT ASSERTIONs with "Do not proceed to Phase N+1 until partition is written" |
| C-14 | **FAIL** | Bracket notation only; no `___` blank slots |
| C-15 | PASS | "FAIL forms: 'I found…' / 'This namespace has…' / 'There is no…' / 'Coverage shows…'" — 4 forbidden forms with halt instruction |
| C-16 | PASS | All EXIT ASSERTIONs include "Do not proceed to Phase N+1 until partition is written" |
| C-17 | **FAIL** | Uses "PHASE N EXIT ASSERTION" ordinal names — rubric requires GATE A/B/C style sequential IDs; ordinal-only does not satisfy |
| C-18 | **FAIL** | Phase 5 has adjacent Constraint blocks; Phase 2/3 use inline template notation without separate framed CONSTRAINT blocks |

**V-02 Composite: 60 + 30 + 7 = 97.0**

---

## V-03 — Output Format

### Essential (60/60)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Rule A/B/C artifact-as-subject with blank `___` targets ✓ |
| C-02 | PASS | Three labels + "Two-of-three does not satisfy this gate" via CONSTRAINT ✓ |
| C-03 | PASS | Edit + CANARY ASSERTION (blank slot + CONSTRAINT) + CANARY-FALSE-POSITIVE + CANARY SUPPRESSED ✓ |
| C-04 | PASS | ONE Write call, 4 sections with CONSTRAINT per section, 4-col table, urgency labels ✓ |
| C-05 | PASS | `--- Slot 1 ---` / `--- Slot 2 ---` separated; CONSTRAINT blocks + Revert-on-violation with paraphrase examples ✓ |

### Recommended (25/30)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | Required artifact citation: `___` with CONSTRAINT specifying verbatim template ✓ |
| C-07 | PASS | Arch-blocked/Strategy-blocked with CONSTRAINT for "none" case; partition counts ✓ |
| C-08 | **PARTIAL** | Template has Trigger condition, Artifact state, Verdict, Required action, VERDICT-ECHO — but **SQ field is absent**; 4 of 5 required fields present |

### Aspirational (9/10 → 9 pts)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | Standing rule: "PASS: …" / "FAIL: …" forms present ✓ |
| C-10 | PASS | "Tier: ___" with CONSTRAINT: "Write 'Tier: N (source: …)'" ✓ |
| C-11 | PASS | Rule counts `___/___/___` with CONSTRAINT + Phase EXIT ASSERTIONs with count notation |
| C-12 | PASS | Explicit CONSTRAINT: line immediately after every constrained field in Phases 2/3/4/5 |
| C-13 | PASS | PHASE 1/2/3 EXIT ASSERTIONs with "Do not proceed" language; CANARY CONSTRAINT in Phase 4 |
| C-14 | PASS | All fill-in targets use `___` notation throughout all phases ✓ |
| C-15 | PASS | Standing rule: "FAIL: 'I found…' / 'This namespace has…' / 'There is no…'" enumerated ✓ |
| C-16 | PASS | "Do not proceed to Phase N until exit assertion is written" across all 3 EXIT ASSERTIONs ✓ |
| C-17 | **FAIL** | PHASE N EXIT ASSERTION naming is ordinal — no GATE A/B/C stable sequential registry |
| C-18 | PASS | Every constrained field has CONSTRAINT: block immediately following with no intervening prose in Phases 0/2/3/4/5/6 |

**V-03 Composite: 60 + 25 + 9 = 94.0**

---

## V-04 — Combined Lifecycle + Phrasing Register

### Essential (60/60)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Rule A/B/C artifact-as-subject; standing rule active "throughout all phases" ✓ |
| C-02 | PASS | Three labels; "A two-of-three set does not satisfy this gate." ✓ |
| C-03 | PASS | Edit + CANARY ASSERTION + CANARY-FALSE-POSITIVE + CANARY SUPPRESSED ✓ |
| C-04 | PASS | ONE Write call; all 4 sections; 4-col table; urgency labels ✓ |
| C-05 | PASS | Slot 1/2 separated; Constraint + Revert-on-violation; paraphrase examples ✓ |

### Recommended (30/30)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | Required artifact citation template in both evaluation phases ✓ |
| C-07 | PASS | Named accumulators; partition explicit; "none" declared ✓ |
| C-08 | PASS | Full 5-field template including SQ in both Phase 2 and Phase 3 ✓ |

### Aspirational (8/10 → 8 pts)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | Standing rule at top with PASS form ✓ |
| C-10 | PASS | Phase 0: "Tier: [N] (source: TOPICS.md \| --tier \| default)" ✓ |
| C-11 | PASS | GATE A through GATE F with N+M=total count assertions |
| C-12 | PASS | Phase 5 Constraint blocks at point of use; Phase 2/3 inline token constraints |
| C-13 | PASS | GATE A–F with count + "Do not proceed to Phase N+1 until GATE [X] is written" |
| C-14 | **FAIL** | Bracket notation `[name]` / `[list]`; no `___` blank slots |
| C-15 | PASS | Standing rule: 4 FAIL forms ("I found…" / "This namespace has…" / "There is no…" / "Coverage shows…") — stronger than V-01's 3 |
| C-16 | PASS | All 6 GATEs include "Do not proceed to Phase N+1 until GATE [X] is written" ✓ |
| C-17 | PASS | GATE A through GATE F — stable named registry; IDs citable from other phases ✓ |
| C-18 | **FAIL** | Phase 5 slots have framed Constraint blocks; Phase 2/3 embed constraints inline (no separate CONSTRAINT: blocks adjacent to fields) |

**V-04 Composite: 60 + 30 + 8 = 98.0**

---

## V-05 — Full Integration

### Essential (60/60)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Rule A/B/C artifact-as-subject with `___` fill-in targets ✓ |
| C-02 | PASS | "CONSTRAINT: All three lines required. Two-of-three does not satisfy this gate." ✓ |
| C-03 | PASS | Edit + "CANARY ASSERTION: Status fields written: ___" with CONSTRAINT + CANARY-FALSE-POSITIVE + CANARY SUPPRESSED ✓ |
| C-04 | PASS | ONE Write call; all 4 sections with adjacent CONSTRAINTs; 4-col table; urgency labels; GATE F confirms ✓ |
| C-05 | PASS | `--- Slot 1 ---` / `--- Slot 2 ---` separated; CONSTRAINT immediately after each slot; revert-on-violation with paraphrase examples ✓ |

### Recommended (25/30)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | PASS | Required artifact citation: `___` with CONSTRAINT "Write '…[field: X, token: Y, slot: Z]' verbatim" ✓ |
| C-07 | PASS | Arch-blocked/Strategy-blocked with CONSTRAINT for "none"; GATE C closes Arch list; GATE D closes Strategy list ✓ |
| C-08 | **PARTIAL** | Template has Trigger condition, Artifact state (with CONSTRAINT), Verdict, Reason, Required action — **SQ field absent**; template collapsed from 5 to 4 fields when transitioning to constraint-per-field format |

### Aspirational (10/10 → 10 pts)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | PASS | Standing rule at top with PASS/FAIL forms ✓ |
| C-10 | PASS | "Tier: ___" with CONSTRAINT: "Write exactly 'Tier: N (source: TOPICS.md \| --tier \| default)'" ✓ |
| C-11 | PASS | GATE B: "Total flags: ___ + ___ + ___ = ___" + CONSTRAINT; GATE C/D counts with CONSTRAINT |
| C-12 | PASS | CONSTRAINT: line immediately after every constrained fill-in field throughout all 6 phases |
| C-13 | PASS | GATE A–F with count + "Do not proceed to Phase N+1 until GATE [X] is written" |
| C-14 | PASS | `___` blank slots on every fill-in target throughout all phases ✓ |
| C-15 | PASS | Standing rule: 4 FAIL forms enumerated with "These FAIL forms are forbidden. Halt and rewrite before advancing." ✓ |
| C-16 | PASS | All 6 GATEs include "Do not proceed to Phase N+1 until GATE [X] is written" ✓ |
| C-17 | PASS | GATE A–F registry; Phase 3 cites "see GATE C"; Phase 6 CONSTRAINT: "reference GATE C and GATE D lists where relevant" — reference loop closed ✓ |
| C-18 | PASS | Every constrained field has CONSTRAINT: block physically adjacent with no intervening prose in all phases; preamble contains only the standing rule (no constraints) ✓ |

**V-05 Composite: 60 + 25 + 10 = 95.0**

---

## Score Summary

| Variation | Essential | Recommended | Aspirational | Composite | Rank |
|-----------|-----------|-------------|--------------|-----------|------|
| V-04 | 60 | 30 | 8 (8/10) | **98.0** | 1 (tied) |
| V-01 | 60 | 30 | 8 (8/10) | **98.0** | 1 (tied) |
| V-02 | 60 | 30 | 7 (7/10) | **97.0** | 3 |
| V-05 | 60 | 25 | 10 (10/10) | **95.0** | 4 |
| V-03 | 60 | 25 | 9 (9/10) | **94.0** | 5 |

---

## Excellence Signals

**Top variations (V-01 / V-04 tied at 98.0):**

1. **GATE registry + blocking language synergy**: Naming gates GATE A through GATE F rather than "PHASE N EXIT ASSERTION" achieves C-16 *and* C-17 simultaneously — the "GATE [X]" ID in the blocking phrase ("Do not proceed to Phase N+1 until GATE [X] is written") is the same stable ID used in the registry. The blocking language creates the ID as a side effect.

2. **Forbidden-form enumeration extends standing rule scope**: V-04 lists 4 FAIL forms (including "Coverage shows…" absent from V-01) and adds "The rule is active throughout all phases" as a scope declaration. The standing rule becomes a two-level enforcement: a global scope claim + specific forbidden strings that require zero inference to identify.

3. **V-04's combined-axis non-interference confirmed**: Merging GATE A–F structure (V-01 axis) with forbidden-form enumeration (V-02 axis) produced zero mutual interference. The structural surfaces are orthogonal — GATE headers and standing rule phrasing do not compete for the same prompt surface.

**New pattern from V-05 (not in top scorer, but first emergence of C-17 reference loop):**

4. **Gate reference loop closes C-17 at execution level**: V-05's Phase 3 instruction "For each Architect-ACCEPTED namespace (see GATE C)" and Phase 6 CONSTRAINT "reference GATE C and GATE D lists where relevant" makes gate IDs referenceable from downstream phase *instructions*, not just the gate assertions themselves. This is a stronger implementation of C-17 than V-04's static registry — the IDs propagate into the output artifact.

**Critical finding — C-08 SQ collapse**:

V-03 and V-05 both dropped the SQ field when transitioning to constraint-per-field format. The blank-slot discipline (`___`) apparently exerts design pressure to collapse the 5-field template because adding a CONSTRAINT after every field makes SQ feel redundant alongside Artifact state. This is the primary reason V-05 (full aspirational) scores below V-01/V-04 (partial aspirational). If R4 targets 100, it must either restore SQ explicitly or demonstrate that CONSTRAINT-guarded Artifact state fully subsumes it.

---

```json
{"top_score": 98.0, "all_essential_pass": true, "new_patterns": ["Named gate IDs (GATE A-F) in blocking language ('Do not proceed until GATE X is written') achieve C-16 and C-17 simultaneously — the gate ID and the blocking phrase are the same token, making registry creation a side-effect of writing the block", "Constraint-per-field format creates design pressure to collapse the 5-field SQ template — blank-slot variations (V-03, V-05) dropped the SQ field and lost a Recommended criterion, a quality trade-off that prevents V-05 from reaching 100 despite 10/10 aspirationals", "Gate reference loop closes C-17 at execution level: citing 'see GATE C' in Phase 3 instructions and 'GATE C/D lists' in Phase 6 CONSTRAINT makes gate IDs referenceable from downstream phases, not just from the review artifact"]}
```
