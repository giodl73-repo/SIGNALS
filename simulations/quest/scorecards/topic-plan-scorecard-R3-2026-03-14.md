Now I have all 5 variations. Scoring each against the 18 criteria.

---

# topic-plan — Round 3 Scorecard

**Rubric**: v3 (C-01–C-18, 140 pts total)
**Variations**: V-01 through V-05
**Date**: 2026-03-15

---

## Criterion-by-Criterion Evaluation

### Essential Criteria (12 pts each)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Reads strategy.md | PASS | PASS | PASS | PASS | PASS |
| C-02 | Reads signal artifacts | PASS | PASS | PASS | PASS | PASS |
| C-03 | Delta not inventory | PASS | PASS | PASS | PASS | PASS |
| C-04 | Typed change proposals | PASS | PASS | PASS | PASS | PASS |
| C-05 | Confirmation gate before write | PASS | PASS | PASS | PASS | PASS |

Evidence notes:
- **C-01**: All variations read `simulations/{topic}/strategy.md` and extract declared stage, namespaces, skills, rationale, gaps before any analysis.
- **C-02**: All glob `simulations/**/{topic}-*` and read every file found; all include a null-case stop condition.
- **C-03**: All explicitly name the anti-pattern. V-01/V-02: verbatim "A plain inventory of signal files is not the delta." V-03: "what does the strategy fail to account for?" V-04: "Not: what changed." V-05: "Not: what has changed since..."
- **C-04**: All use the ADD / REMOVE / REPRIORITIZE typed table format, including the stage-correction REPRIORITIZE row when drift is detected.
- **C-05**: All present proposals first, then gate on "Waiting." before any write to strategy.md.

**Essential subtotal**: 60/60 for all five variations.

---

### Recommended Criteria (10 pts each)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Signal evidence per change | PASS | PASS | PASS | PASS | PASS |
| C-07 | Before/after summary | PASS | PASS | PASS | PASS | PASS |
| C-08 | All three change types addressed | PASS | PASS | PASS | PASS | PASS |

Evidence notes:
- **C-06**: All variations include an Evidence column in the proposal table specifying "specific signal artifact filenames — not descriptions."
- **C-07**: All produce a before/after table (diff-style) at the confirmation gate. V-04/V-05 label it "post-apply view" which is equivalent. V-02/V-03 produce it as a dedicated step.
- **C-08**: All mandate "None proposed" rows for empty types, making the three-type check structurally enforced.

**Recommended subtotal**: 30/30 for all five variations.

---

### Aspirational Criteria (5 pts each; PARTIAL = 2.5 pts)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|-----------|------|------|------|------|------|-------|
| C-09 | Namespace gap detection (stage-relative) | PASS | PASS | PASS | PASS | PASS | All use a 9-row table evaluated against the governing baseline, not the raw declared stage. |
| C-10 | Conflicting signal detection | PASS | PASS | PASS | PASS | PASS | All surface conflicts with strategy implications. V-02/V-03/V-05 use a dedicated conflict table; V-01/V-04 use inline annotation below conflict rows. |
| C-11 | Typed confirmation verb | PASS | PASS | PASS | PASS | PASS | All name "YES" as the confirmation token. Not "apply" specifically, but a named verb is present; closes the rationalization path. |
| C-12 | Explicit no-change rows per type | PASS | PASS | PASS | PASS | PASS | All use "None proposed" + "A missing type row is an incomplete review." V-05: "leaving out a type means I didn't check it" — same enforcement, different register. |
| **C-13** | **Inline evidence brackets in before/after diff** | **FAIL** | **FAIL** | **FAIL** | **FAIL** | **FAIL** | **Universal gap.** All before/after tables use `\| Before \| After \| Confidence \|` with no `[+skill: evidence-file]` bracket inline. Evidence lives in the proposal table, not in the diff — requires cross-referencing. |
| C-14 | Anti-inventory warning at delta step | PASS | PASS | PARTIAL | PARTIAL | PARTIAL | V-01/V-02: verbatim "A plain inventory of signal files is not the delta." V-03/V-04/V-05: name the correct framing ("fail to account for") but don't name the anti-pattern explicitly. |
| C-15 | All 9 namespaces enumerated by name | PASS | PASS | PASS | PASS | PASS | All list scout, draft, review, flow, trace, prove, listen, program, topic explicitly in the coverage table instruction. |
| C-16 | Two-level traceability chain | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL | No variation adds a "Delta Row" column alongside "Evidence [file(s)]". Conflict coverage tables (V-02/V-03/V-05: conflict→row; V-04: implication→row) provide partial two-level tracing for conflict-driven proposals only. Non-conflict proposals remain single-hop. |
| C-17 | Explicit no-conflicts declaration | FAIL | PASS | PASS | FAIL | PASS | V-02: "If no conflicts found, write 'No conflicts detected.' Do not omit this section — an absent conflict table is indistinguishable from a skipped audit." V-03/V-05: equivalent instruction. V-01/V-04 use inline-annotation format only — no null-case instruction. |
| C-18 | Structured delta format per finding | PASS | PASS | PASS | PASS | PASS | All mandate "→ Strategy assumed [X] / Signal revealed [Y]" per bullet. All include the stop condition: "Signals confirmed — no gaps detected." |

---

### Aspirational Subtotals

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 | 5 | 5 | 5 | 5 | 5 |
| C-10 | 5 | 5 | 5 | 5 | 5 |
| C-11 | 5 | 5 | 5 | 5 | 5 |
| C-12 | 5 | 5 | 5 | 5 | 5 |
| C-13 | 0 | 0 | 0 | 0 | 0 |
| C-14 | 5 | 5 | 2.5 | 2.5 | 2.5 |
| C-15 | 5 | 5 | 5 | 5 | 5 |
| C-16 | 2.5 | 2.5 | 2.5 | 2.5 | 2.5 |
| C-17 | 0 | 5 | 5 | 0 | 5 |
| C-18 | 5 | 5 | 5 | 5 | 5 |
| **Subtotal** | **37.5** | **42.5** | **40** | **35** | **40** |

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | **Total** | All Essential Pass? | Golden? |
|-----------|-----------|-------------|--------------|-----------|---------------------|---------|
| V-01 | 60 | 30 | 37.5 | **127.5** | Yes | Yes |
| **V-02** | **60** | **30** | **42.5** | **132.5** | **Yes** | **Yes** |
| V-03 | 60 | 30 | 40 | **130** | Yes | Yes |
| V-04 | 60 | 30 | 35 | **125** | Yes | Yes |
| V-05 | 60 | 30 | 40 | **130** | Yes | Yes |

**Golden threshold**: all essential pass + composite >= 80. All five clear it. V-02 leads.

---

## Ranking

1. **V-02 — Rich Protocol** (132.5/140) — Explicit OPEN/CLOSED gate field + "Do not omit this section" null declaration for conflicts (C-17 PASS); verbatim anti-inventory warning at delta step (C-14 PASS); phase-entry prerequisites make every transition auditable.
2. **V-03 — Stage-First** (130/140) — C-17 PASS; stage inference as Phase A makes drift detection architecturally governing. Loses 2.5 pts on C-14 (anti-inventory framing present, warning not verbatim).
3. **V-05 — Conversational Register** (130/140) — C-17 PASS; criterion coverage matches V-03 exactly but in first-person register. Loses 2.5 pts on C-14 for the same reason as V-03.
4. **V-01 — Minimal Footprint** (127.5/140) — Strongest on footprint and C-14. Loses 5 pts on C-17 (no null-declaration instruction for the inline conflict format).
5. **V-04 — Inertia-Foregrounded** (125/140) — Loses pts on both C-14 (partial) and C-17 (fail). The vintage-cost axis adds real value but doesn't compensate for the two structural gaps.

---

## Excellence Signals

**From V-02 (top scorer):**

1. **OPEN/CLOSED gate with named state field** — V-02 Step 4 names a "Gate status: OPEN / CLOSED" field that must read CLOSED before the change table is available. This converts the conflict-resolution check from an instruction into a structural prerequisite. V-01/V-04 have the coverage check but no named gate state; the rationalization path (write the table anyway) remains open.

2. **"Do not omit this section" rationale attached to the null case** — V-02's C-17 instruction doesn't just say "write 'No conflicts detected'"; it explains *why*: "an absent conflict table is indistinguishable from a skipped audit." Embedding the rationale at the instruction point is what makes V-02's C-17 self-enforcing rather than merely instructed.

3. **Phase-entry declarations between steps** — "Phase entry for Step N: AVAILABLE only after..." turns each transition into an auditable checkpoint. No other variation structures the protocol this way. This pattern makes regression to a previous phase visible rather than implicit.

**Universal gap (shared across all 5 variations):**

- **C-13 inline evidence brackets** — All five variations fail this criterion. The before/after diff table in every variation uses `| Before | After | Confidence |` only. Evidence lives in the separate proposal table, requiring the user to cross-reference when confirming. The fix is structural: add `[file.md]` brackets inline in the After cell, e.g., `scout: add stakeholder risk skill [scout-stakeholders-2026-03-14.md]`. This is the aspirational criterion most likely to be targeted in Round 4 variations.

---

```json
{"top_score": 132.5, "all_essential_pass": true, "new_patterns": ["OPEN/CLOSED gate field with named state converts conflict-resolution check from instruction to structural prerequisite (V-02 Step 4 gate)", "Attaching the rationale to null-case declarations ('Do not omit — indistinguishable from skipped') makes them self-enforcing rather than merely instructed", "C-13 inline evidence brackets failed universally across all 5 variations — the shared aspirational gap for Round 4"]}
```
