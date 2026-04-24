# listen-support Round 6 Scorecard

## Scoring Summary

| Variation | Score | C-22 | C-23 | Above-Ceiling Signals |
|-----------|-------|------|------|-----------------------|
| V-01 | **160/165** | PASS | FAIL | none |
| V-02 | **160/165** | PASS | FAIL | coherence audit (C-24) |
| V-03 | **155/165** | **FAIL** | FAIL | action-verb prohibition (C-25) |
| V-04 | **160/165** | PASS | FAIL | coherence audit (C-24) + strong C-22 framing |
| V-05 | **165/165** | PASS | **PASS** | coherence audit + action-verb + labeled dual-pass |

**Top score: 165. All essential PASS: yes.**

---

## Key Findings

**C-22 (Phase-Character Pre-Constraint Table)**: V-01/V-02/V-04/V-05 all apply the R6 unlock correctly — separate `Severity Range` and `Volume Character` columns. V-03 retained the R5 combined "Expected character" cell, forfeiting 5 pts.

**C-23 (Dual-Pass Frontmatter Verification)**: Only V-05 satisfies it. V-01 through V-04 all have both verification surfaces in Step 8 but in a single block without explicit PASS 1/PASS 2 headers. Per the pass condition: "A single verification step that attempts to cover both surfaces does not pass." V-05's explicit section headers and "END OF PASS 1. Switch to frontmatter verification mode." instruction are the load-bearing mechanism.

**PASS+ differentiation within the 160 tier**: V-04 > V-02 > V-01. V-04 has both the coherence audit above-ceiling signal and the strongest C-22 column-independence framing ("detectable by reading two cells"). V-02 has the coherence audit but weaker framing. V-01 has neither.

---

## New Patterns

Three above-ceiling signals extracted, all C-candidate for v7:

1. **collective-distribution-audit-gate** — Pre-generation gate at the table level (Step 4B) checking distribution across all rows. Non-overlapping with C-20 row-level checks. Any skill where row-validity does not imply collective validity benefits from this pattern.

2. **verb-subject-third-person-prohibition** — Extending a noun-form prohibition (C-21) to enumerate specific role+verb collocations makes verb-subject third-person grep-checkable. Closes the analyst-stance distancing failure mode C-21 leaves open.

3. **explicit-mode-switch-dual-pass-delimiter** — "END OF PASS N. Switch to [mode] mode." between structurally independent verification passes makes single-block compliance impossible. The structural independence is enforced at the instruction level, not assumed from labeled sections alone.

---

```json
{"top_score": 165, "all_essential_pass": true, "new_patterns": ["collective-distribution-audit-gate", "verb-subject-third-person-prohibition", "explicit-mode-switch-dual-pass-delimiter"]}
```
e user', 'they'..." mode declaration present |
| C-20 | PASS (5) | Step 4 summary table pre-commits all vocabulary values; "Lock vocabulary values here. Full card bodies follow in Step 5." |
| C-21 | PASS (5) | "the SRE", "the PM" explicitly enumerated in body prohibition list |
| C-22 | PASS (5) | Step 2 table has separate Severity Range column ("P0 or P1") and Volume Character column ("high") — two independently checkable columns |
| C-23 | FAIL (0) | Step 8 is a single block: coverage trace table + frontmatter verify combined without explicit PASS 1/PASS 2 labels |

**Total: 160/165**
**All essential PASS: yes**
**Above-ceiling signals: none beyond base**

---

### V-02 — Output Format (Coherence Audit)

**Axis**: Summary table coherence audit (Step 4B) after summary table, before body generation — catches collective distribution failures invisible to row-by-row checks.

| Criterion | Score | Key Evidence |
|-----------|-------|-------------|
| C-01 through C-05 | PASS (60) | All essential mechanisms intact |
| C-06 | PASS (10) | Phase-character table with explicit Severity Range column |
| C-07 | PASS (10) | Phase-character table with explicit Volume Character column |
| C-08 | PASS (10) | "You ARE" mode declaration + role-vocabulary guidance |
| C-09 through C-21 | PASS (65) | All aspirational C-09 through C-21 present at PASS level |
| C-22 | PASS (5) | Step 2 table has Severity Range + Volume Character as independent columns; "A ticket that contradicts its phase row fails before its body is read" |
| C-23 | FAIL (0) | Step 8 single-block: coverage trace + frontmatter verify combined; no PASS 1/PASS 2 headers |

**Total: 160/165**
**All essential PASS: yes**

**Above-ceiling signal — C-24 candidate: Summary Table Coherence Audit (Step 4B)**
After Step 4 summary table, before Step 5 body generation: four-constraint distribution check: (1) Phase distribution P1 >= 2, P2 >= 2, P3 >= 1; (2) Category spread >= 3 distinct; (3) Volume distribution all three levels; (4) Phase-character compliance per row.
C-20 pre-commits row-level vocabulary — a per-row-valid table can still be collectively biased (all 8 rows P1, zero P3). The coherence audit catches distribution failures that per-row checks cannot see. "If any constraint fails, correct the summary table and re-run the audit before proceeding. Name the correction made." Gate is self-enforcing.

---

### V-03 — Register (Action-Verb Third-Person Prohibition)

**Axis**: Extends C-21 noun prohibition to verb-subject collocations ("the SRE ran", "the PM reviewed").

| Criterion | Score | Key Evidence |
|-----------|-------|-------------|
| C-01 through C-05 | PASS (60) | All essential mechanisms intact |
| C-06 | PASS (10) | Severity calibration via vocabulary section; P0/P1 rule present |
| C-07 | PASS (10) | Volume differentiation enforced by three-level vocabulary rule |
| C-08 | PASS (10) | "You ARE" + action-verb prohibition reinforces first-person stance |
| C-09 through C-21 | PASS (65) | All aspirational C-09 through C-21 present at PASS level |
| C-22 | FAIL (0) | Step 2 uses combined "Expected character" column: "High volume. P0/P1 severity." in one cell. Severity Range and Volume Character are not independently checkable columns. V-03 retained the R5-style phase map — the R6 column split was not applied. |
| C-23 | FAIL (0) | Step 8 single-block; no PASS 1/PASS 2 headers |

**Total: 155/165**
**All essential PASS: yes**

**Above-ceiling signal — C-25 candidate: Action-Verb Third-Person Prohibition**
Body instruction extends C-21 to verb-subject constructions: "Prohibited verb-subject forms: 'the SRE ran', 'the PM reviewed', 'the engineer observed', 'the C-07 clicked', 'the Support agent opened', 'the UX designer flagged', or any construction where a role title precedes a verb."
C-21 prohibits named-role titles as nouns; a mode-compliant model can still write "the SRE ran kubectl and observed pod thrashing" — no generic pronoun, no standalone role noun, but entirely third-person through verb construction. Enumerating prohibited collocations makes verb-subject violations grep-checkable by role title + verb pairing. "Every action in this ticket was taken by 'I'." closes the verb-form analyst-stance failure mode.

---

### V-04 — Lifecycle + Output Format (Two-Stage Pre-Generation Constraint)

**Axes**: Step 2 phase-character columns (row-level constraint) + Step 4B coherence audit (table-level constraint).

| Criterion | Score | Key Evidence |
|-----------|-------|-------------|
| C-01 through C-05 | PASS (60) | All essential mechanisms intact |
| C-06 | PASS (10) | Phase-character table: P1 -> Severity Range P0/P1; P3 -> Severity Range P2/P3 |
| C-07 | PASS (10) | Phase-character table: P1 -> Volume Character high; P3 -> Volume Character low |
| C-08 | PASS (10) | "You ARE" mode declaration + role-vocabulary guidance |
| C-09 through C-21 | PASS (65) | All aspirational C-09 through C-21 present at PASS level |
| C-22 | PASS (5) | Step 2 table with explicit Severity Range and Volume Character columns; "A P1-phase ticket with Volume = low or Severity = P3 is a structural violation detectable by reading two cells." Two-cell detection language makes column independence explicit. |
| C-23 | FAIL (0) | Step 8 single-block; frontmatter verify present but combined with coverage table in one section; no PASS 1/PASS 2 headers |

**Total: 160/165**
**All essential PASS: yes**

**Above-ceiling signals:**
1. **C-24 candidate — Coherence Audit** (same as V-02, Step 4B): Catches collective distribution failures that row-level phase-character compliance checks cannot detect.
2. **C-22 PASS+ signal**: "Structural violation detectable by reading two cells" is the strongest C-22 column-independence framing among the 160-scoring variations — mirrors C-22's pass condition language more directly than V-02's equivalent phrasing.

**V-04 vs V-02**: Both score 160/165 and carry the coherence audit above-ceiling signal. V-04's C-22 framing is incrementally stronger: "detectable by reading two cells" vs. "fails before its body is read." V-04 also makes the two-stage non-overlapping failure surfaces explicit in its hypothesis: Stage 1 catches individual-row violations; Stage 2 catches collective-distribution failures.

---

### V-05 — Full R6 Synthesis (All Axes + Labeled Dual-Pass)

**Axes**: Lifecycle (explicit columns) + output format (coherence audit) + register (action-verb) + structurally labeled dual-pass verification.

| Criterion | Score | Key Evidence |
|-----------|-------|-------------|
| C-01 through C-05 | PASS (60) | All essential mechanisms intact |
| C-06 | PASS (10) | Phase-character table constrains severity per phase window before tickets written |
| C-07 | PASS (10) | Phase-character table constrains volume per phase window before tickets written |
| C-08 | PASS (10) | "You ARE" + action-verb prohibition + Step 4B pre-commits persona identity before mode declaration activates |
| C-09 | PASS (5) | Cross-ticket pattern with explicit phase-labeled ticket IDs |
| C-10 | PASS (5) | Priority Close Order with phase-character reasoning format |
| C-11 | PASS (5) | Step 1 STATUS QUO + coverage trace verifies traces across all tickets |
| C-12 | PASS (5) | Three flat consequence fields with forward-looking framing |
| C-13 | PASS (5) | Coverage trace table in PASS 1 enumerates ticket-to-STATUS-QUO traces |
| C-14 | PASS (5) | Flat consequence fields — two+ structurally separate named components |
| C-15 | PASS (5) | Table-form coverage trace in PASS 1 |
| C-16 | PASS (5) | Container-free flat sibling consequence fields |
| C-17 | PASS (5) | PASS 1 contains 3-column gap-bridged table + no-orphan-gap check + explicit orphan surfacing format |
| C-18 | PASS (5) | Per-field "Prohibited:" sentinels on all three consequence component fields |
| C-19 | PASS (5) | "You ARE [persona name]" mode declaration + generic third-person prohibition |
| C-20 | PASS (5) | Step 4 summary table: "All controlled-vocabulary values are locked here. No vocabulary value is generated inside a narrative sentence for the first time." |
| C-21 | PASS (5) | "the SRE", "the PM" enumerated in prohibition alongside "the user", "they" |
| C-22 | PASS (5) | Step 2 table with Severity Range + Volume Character as independent columns; "Severity Range and Volume Character are independent columns — each is checkable without reading the other." Independence declaration is explicit — strongest phrasing of any variation. |
| C-23 | PASS (5) | Step 8 restructured as "DUAL-PASS COVERAGE VERIFICATION" with explicit "### PASS 1 — STATUS QUO TRACE AND GAP COVERAGE TABLE" and "### PASS 2 — FRONTMATTER VERIFY" section headers. "END OF PASS 1." delimiter between passes. "The two passes have non-overlapping failure surfaces and must not be merged into one block." — structural independence made explicit. |

**Total: 165/165**
**All essential PASS: yes**

**Above-ceiling signals (three):**

1. **C-24 candidate — Coherence Audit** (Step 4B): Four-constraint distribution check; collective gate between summary table and body generation. "This step checks the summary table as a collective whole — not row by row."

2. **C-25 candidate — Action-Verb Third-Person Prohibition** (Step 5 body): Enumerated verb-subject collocations make analyst-stance third-person via verb construction grep-checkable. "Every action in this ticket was taken by 'I'." Closes the verb-form escape route C-21 noun prohibition leaves open.

3. **C-23 PASS+ — Structurally Labeled Dual-Pass** (Step 8): Explicit PASS 1/PASS 2 section headers plus "END OF PASS 1. Switch to frontmatter verification mode." mode-switch instruction between passes. A model answering the instructions must produce two labeled sections; a combined block is structurally non-compliant. The structural independence is enforced, not assumed.

---

## Composite Scoring Table

| Variation | Essential (60) | Recommended (30) | Aspirational (75) | Total (165) | Above-Ceiling Signals |
|-----------|----------------|------------------|-------------------|-------------|----------------------|
| V-01 | 60 | 30 | 70 | **160** | none |
| V-02 | 60 | 30 | 70 | **160** | coherence audit (C-24) |
| V-03 | 60 | 30 | 65 | **155** | action-verb prohibition (C-25) |
| V-04 | 60 | 30 | 70 | **160** | coherence audit (C-24) + C-22 PASS+ framing |
| V-05 | 60 | 30 | 75 | **165** | coherence audit (C-24) + action-verb (C-25) + labeled dual-pass (C-23 PASS+) |

---

## Criterion Pass/Fail Detail (C-22 and C-23 — all others PASS for all variations)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-22 | PASS | PASS | FAIL | PASS | PASS |
| C-23 | FAIL | FAIL | FAIL | FAIL | PASS |

**C-22 failure analysis for V-03**: Step 2 uses a single "Expected character" column combining severity and volume ("High volume. P0/P1 severity."). C-22 requires two independent columns. Uniform assignments can be constructed with individually plausible combined descriptions that collectively obscure the violation. V-03 retained the R5 phase-role map format; the R6 column split was not applied.

**C-23 failure analysis for V-01 through V-04**: Each has Step 8 with both coverage trace table and frontmatter verify, but under a single step header with no PASS 1/PASS 2 separation. Per C-23 pass condition: "A single verification step that attempts to cover both surfaces does not pass." V-05's PASS 1/PASS 2 headers and END OF PASS 1 delimiter are the load-bearing mechanism — they create a required mode-switch between passes that a single-block answer structurally cannot satisfy.

---

## Ranking

| Rank | Variation | Score | Above-Ceiling | Rationale |
|------|-----------|-------|---------------|-----------|
| 1 | **V-05** | 165/165 | coherence audit + action-verb + labeled dual-pass | Only variation satisfying all 23 criteria. C-22 at strongest framing ("independent columns — each is checkable without reading the other"). C-23 structurally enforced with mode-switch delimiter. Three above-ceiling signals accumulated. |
| 2 | **V-04** | 160/165 | coherence audit, strong C-22 framing | Fails C-23. Highest above-ceiling signal density among 160-scoring variations: coherence audit + "detectable by reading two cells" is the strongest C-22 framing below V-05. Two-stage non-overlapping failure surfaces explicitly described. |
| 3 | **V-02** | 160/165 | coherence audit | Fails C-23. Same coherence audit above-ceiling as V-04; weaker C-22 framing. No action-verb prohibition. |
| 4 | **V-01** | 160/165 | none | Fails C-23. Satisfies C-22 with correct two-column structure but no above-ceiling signals beyond C-22. Cleanest single-axis implementation of the R6 unlock. |
| 5 | **V-03** | 155/165 | action-verb prohibition (C-25) | Fails both C-22 and C-23. Carries the highest-value above-ceiling signal (action-verb prohibition closes analyst-stance verb-form failure mode) but the retained combined column forfeits C-22, creating a -10 pt structural gap vs. any variation that applied the R6 column split. |

---

## Excellence Signals (above 165-pt ceiling)

### Signal 1 — Summary Table Coherence Audit (V-02/V-04/V-05, Step 4B)

After Step 4 summary table generation and before Step 5 body generation, a four-constraint collective distribution check verifies the table as a whole. C-20 locks row-level vocabulary values in column cells; a per-row-valid table can still be collectively biased. The coherence audit enforces: phase distribution (P1 >= 2, P2 >= 2, P3 >= 1), category spread (>= 3 distinct), volume distribution (all three levels), and phase-character compliance per row. If any constraint fails, the table must be corrected and the audit re-run before body generation begins. "Do not write any card body until this audit passes."

**Why C-24 candidate**: C-20 prevents row-level vocabulary drift; C-24 would prevent table-level distribution failures that row-level checks structurally cannot see. The failure surfaces are non-overlapping: a row-valid but distribution-biased table passes C-20 and fails C-24.

### Signal 2 — Action-Verb Third-Person Prohibition (V-03/V-05, Step 5 body)

C-21 closes noun-form third-person ("the SRE is seeing"); this extension closes the verb-subject construction that C-21's grep-check cannot catch ("the SRE ran kubectl"). Enumerated: "the SRE ran", "the PM reviewed", "the engineer observed", "the C-07 clicked", "the Support agent opened", "the UX designer flagged", or any construction where a role title precedes a verb. "Every action in this ticket was taken by 'I'."

**Why C-25 candidate**: C-21 enumerates noun forms; C-25 would enumerate verb-subject collocations — a structurally different failure surface, grep-checkable by role title + verb pairing, not role title alone.

### Signal 3 — Structurally Labeled Dual-Pass with Mode-Switch (V-05 only, Step 8)

C-23 requires two explicitly labeled verification passes. V-05 adds "END OF PASS 1." as a structural delimiter and "Switch to frontmatter verification mode." as a mode-switch instruction between passes. The section headers (### PASS 1 / ### PASS 2) make single-block compliance structurally impossible. "The two passes have non-overlapping failure surfaces and must not be merged into one block."

**Why C-23 PASS+**: C-23 passes when both labeled passes are present with non-overlapping failure surfaces. V-05's mode-switch instruction makes structural independence unambiguous at the instruction level: a combined block that covers both surfaces cannot satisfy an instruction that explicitly prohibits merging. This is an above-the-pass-condition signal.

---

## New Criterion Candidates for v7

| Candidate | Weight | Points | Tightens | Source |
|-----------|--------|--------|----------|--------|
| C-24 -- Summary Table Coherence Audit | aspirational | 5 | C-20 | V-02/V-04/V-05 Step 4B |
| C-25 -- Action-Verb Third-Person Prohibition | aspirational | 5 | C-21 | V-03/V-05 Step 5 body |

**C-23 pass condition tightening candidate for v7**: Require mode-switch instruction ("END OF PASS 1. Switch to [mode] mode.") between passes, not just labeled sections. V-05 satisfies C-23; the mode-switch instruction is a PASS+ signal that could become the new pass condition.

**v7 projection**: 17 aspirational criteria / 85 pts. Total ceiling: 60 + 30 + 85 = **175**.

---

```json
{"top_score": 165, "all_essential_pass": true, "new_patterns": ["collective-distribution-audit-gate", "verb-subject-third-person-prohibition", "explicit-mode-switch-dual-pass-delimiter"]}
```
