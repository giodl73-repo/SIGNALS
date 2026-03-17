## Round 12 — trace-state Scoring (V-01 through V-05)

### Rubric v26 — Criteria Summary

**Essential (60 pts):** C-01 through C-05  
**Recommended (30 pts):** C-06, C-07, C-08  
**Aspirational (10 pts):** any 5 of 25 × 2 pts each

---

## V-01 — Role Sequence: Finance → Sales → CS

| ID | Result | Evidence |
|----|--------|----------|
| **C-01** | **PASS** | Columns `[C-01a]` `[C-01b]` `[C-01c]` `[C-01d]` in all three pass tables |
| **C-02** | **PASS** | `Preconditions [C-02a — write "none" if genuinely absent; never leave blank]` + `Postconditions [C-02b ...]` in every pass |
| **C-03** | **PASS** | `Invariants Checked [C-03: min 2 per pass — never skip]` column enforced across all passes |
| **C-04** | **PASS** | `[C-04a]` `[C-04b]` `[C-04c]` `[C-04d]` sub-element labels in every defect log |
| **C-05** | **PASS** | Finance / Sales / Customer Service explicitly named |
| **C-06** | **PASS** | Uniform table format throughout all three passes |
| **C-07** | **PASS** | Exclusion list + qualifying example in every invariant section |
| **C-08** | **PASS** | Ordering 1 + Ordering 2 sections with named conflict slot |
| C-09 | PASS | Negative path table `[C-09a–d]` + active verification statement |
| C-10 | FAIL | No reachability annotation section |
| C-11 | PASS | Criterion IDs embedded in all column headers |
| C-12 | PASS | Both orderings present with independent description instruction |
| C-13 | PASS | `Derived From [C-13]` column in every invariant table |
| C-14 | FAIL | No explicit "mechanically satisfies" design note — headers carry directives but unavoidability not declared |
| C-15 | PASS | Reference rows filled with sample data; invariant tables use `…` anchors |
| C-16 | PASS | HARD RULES section: "prose is not a valid format for trace data [C-16]" |
| C-17 | PASS | "minimum 5 rows [C-17: explicit row floor; qualitative 'be thorough' does not satisfy]" per pass |
| C-18 | PASS | Three named disqualifying patterns in exclusion list |
| C-19 | PASS | "HARD RULES — any violation invalidates the entire artifact [C-19]" |
| C-20 | PASS | `Valid qualifying example [C-20]: "Invoice total must remain positive…"` |
| C-21 | PASS | "Do not write 'same as above' or any cross-reference to Ordering 1 [C-21]" |
| C-22 | PASS | `write "none" if genuinely absent` in precondition/postcondition headers |
| C-23 | PASS | "Finance/Sales/CS Defect Log — silent omissions invalidate this section [C-23]" |
| C-24 | PASS | "Reference row — template anchor; do not include this row in output [C-24]" |
| C-25 | PASS | Cross-Domain Invariant Register section with explicit cross-pass derivation |
| C-26 | PASS | "Minimum 15 transition rows across all three passes combined [C-26]" |
| C-27 | PASS | Three named disqualifying patterns in list form |
| C-28 | PASS | "Name both concurrent operations explicitly — naming only the conflict outcome does not qualify [C-28]" |
| C-29 | PASS | "actively verify that [C-09c] is identical to [C-09a] — write an explicit verification statement [C-29]" |
| C-30 | PASS | `[C-02a — write "none" if genuinely absent; never leave blank]`; `[C-03: min 2 per pass — never skip]` |
| C-31 | PASS | C-01a/b/c/d, C-02a/b, C-04a/b/c/d, C-09a/b/c/d all individually labeled |
| C-32 | PASS | HARD RULE: "Blank cells are prohibited... blank is not a permitted entry [C-32]" + "never leave blank" in headers |
| C-33 | PASS | `[C-02a — write "none" if genuinely absent; never leave blank]` — nil-value instruction within sub-criterion annotation |

**Aspirationals passed:** 23 of 25 (C-10, C-14 fail) → capped at 5 → **10 pts**

**V-01 Score: 60 + 30 + 10 = 100**

---

## V-02 — Output Format: Numbered Step Blocks

| ID | Result | Evidence |
|----|--------|----------|
| **C-01** | **PASS** | `Starting State [C-01b]`, `Operation [C-01c]`, `Ending State [C-01d]`, `Step [C-01a]` in block template |
| **C-02** | **PASS** | `Preconditions [C-02a: ...; write "none" if genuinely absent; never leave blank]` + `Postconditions [C-02b ...]` |
| **C-03** | **PASS** | `Invariant-1 [C-03: first domain invariant...]` + `Invariant-2 [C-03: second domain invariant — required]` |
| **C-04** | **PASS** | Defect block: `[C-04a]` ID, `Type [C-04b]`, `Triggering Op [C-04c]`, `Reason [C-04d]` |
| **C-05** | **PASS** | Sales domain explicitly named |
| **C-06** | **PASS** | Step-block format consistently applied for main trace |
| **C-07** | **PASS** | Exclusion list + `[C-07: real Sales business rule]` annotation in invariant table |
| **C-08** | **PASS** | Ordering 1 + Ordering 2 block structure present |
| C-09 | PASS | `[C-09a]`–`[C-09d]` in negative-step block + mutation verification |
| C-10 | FAIL | No reachability annotation section |
| C-11 | PASS | Criterion IDs in every step-block field label |
| C-12 | PASS | Ordering 1 (A→B) and Ordering 2 (B→A) independently described |
| C-13 | PASS | `Appears In Step` column in invariant summary provides trace-row cross-reference |
| C-14 | PASS | "Output format: filling each field mechanically satisfies its embedded criterion" — explicit design note |
| C-15 | PASS | Invariant table template row `\| INV-01 \| … \| Step … \|` with `…` anchors |
| C-16 | PASS | HARD RULES: "Prose is not a valid output format for trace data — no prose substitutions [C-16]" |
| C-17 | PASS | "Minimum 5 operation step blocks [C-17]"; section label repeats "[C-17: if fewer than 5 blocks…]" |
| C-18 | PASS | Three named disqualifying patterns in exclusion list |
| C-19 | PASS | "HARD RULES — violation of any rule invalidates the artifact [C-19]" |
| C-20 | PASS | `Valid qualifying example [C-20]: "Opportunity amount must remain ≥ 0…"` |
| C-21 | PASS | "do not reference Ordering 1; do not write 'same as above' [C-21]" |
| C-22 | PASS | `write "none" if genuinely absent` in preconditions/postconditions fields |
| C-23 | FAIL | Defect log section says "at least one entry required" but no "silent omissions invalidate this section" clause |
| C-24 | PASS | "Reference block — template anchor; do not reproduce this block in output [C-24]" |
| C-25 | FAIL | Single domain — no cross-domain invariant register |
| C-26 | FAIL | Single domain — no cross-pass aggregate floor |
| C-27 | PASS | Three named disqualifying patterns in exclusion list |
| C-28 | PASS | "Name both concurrent operations explicitly [C-28]" |
| C-29 | PASS | "Mutation verification [C-29 — active verification required]" + sentence requirement |
| C-30 | PASS | `[C-02a: ...; write "none" if genuinely absent; never leave blank]`; `[C-03: first domain invariant — must encode real Sales rule]` |
| C-31 | PASS | C-01a/b/c/d, C-02a/b, C-04a/b/c/d, C-09a/b/c/d independently labeled |
| C-32 | PASS | "Blank fields are prohibited throughout... blank is never an acceptable entry for any field [C-32]" |
| C-33 | PASS | `Preconditions [C-02a: list every condition...; write "none" if genuinely absent; never leave blank]` — sub-criterion level |

**Aspirationals passed:** 21 of 25 (C-10, C-23, C-25, C-26 fail) → capped at 5 → **10 pts**

**V-02 Score: 60 + 30 + 10 = 100**

---

## V-03 — Lifecycle Emphasis: Four Explicit Sub-Steps Per Operation

| ID | Result | Evidence |
|----|--------|----------|
| **C-01** | **PASS** | `Starting State [C-01b]`, `Operation [C-01c]`, `Ending State [C-01d]` in every operation record header |
| **C-02** | **PASS** | Sub-step 1: `Preconditions [C-02a: list all; write "none" if genuinely absent; never leave blank]`; Sub-step 3: `Postconditions [C-02b ...]` |
| **C-03** | **PASS** | Sub-step 4: `[C-03: min 2 per record — never skip]` with INV examples |
| **C-04** | **PASS** | Defect log table: `[C-04a]`, `[C-04b]`, `[C-04c]`, `[C-04d]` |
| **C-05** | **PASS** | Customer Service domain explicitly named |
| **C-06** | **PASS** | Uniform four-sub-step operation record format throughout |
| **C-07** | **PASS** | Exclusion list + qualifying example in invariant register |
| **C-08** | **PASS** | Race section with both orderings using four-sub-step structure |
| C-09 | PASS | Negative Path Record with `[C-09a–d]` and Sub-step 4 mutation verification |
| C-10 | PASS | Explicit Reachability Annotation section: "every reachable but untested path must be explicitly named" |
| C-11 | PASS | Criterion IDs in all sub-step and section labels |
| C-12 | PASS | Ordering 1 and Ordering 2 both present |
| C-13 | PASS | Sub-step 4 reference: "Derived: INV-C-01 sourced from this record [C-13]"; `Derived From [C-13]` column in register |
| C-14 | FAIL | No explicit "mechanically satisfies" design note — sub-step directives are present but unavoidability not framed |
| C-15 | PASS | Reference record fully filled with sample data; invariant register uses `\| INV-C-01 \| … \| Record … \|` |
| C-16 | FAIL | No explicit no-prose-substitution rule in HARD RULES section |
| C-17 | PASS | "Minimum 5 complete operation records [C-17]" |
| C-18 | PASS | Three named disqualifying patterns in exclusion list |
| C-19 | PASS | "HARD RULES — any violation invalidates the entire artifact [C-19]" |
| C-20 | PASS | `Valid qualifying example [C-20]: "SLA clock must be running while ticket status is Open or Pending."` |
| C-21 | PASS | "Do not write 'same as above' or cross-reference Ordering 1 [C-21]" |
| C-22 | PASS | `write "none" if genuinely absent` in sub-step 1 and sub-step 3 |
| C-23 | PASS | "Defect Log [C-04] — silent omissions invalidate this section [C-23]" |
| C-24 | PASS | "Reference record — template anchor; do not reproduce this record in output [C-24]" |
| C-25 | PASS | Invariant Register `[C-25]` aggregates all sub-step 4 invariants with derivation links |
| C-26 | FAIL | Single domain — no cross-pass aggregate floor |
| C-27 | PASS | Three named disqualifying patterns in list |
| C-28 | PASS | "Name both concurrent operations explicitly [C-28]" |
| C-29 | PASS | Sub-step 4 mutation verification in negative path: "Explicitly confirm that no field was mutated. Declare that [C-09c] = [C-09a]..." |
| C-30 | PASS | `[C-02a: list all; write "none" if genuinely absent; never leave blank]`; `[C-03: min 2 per record — never skip]` |
| C-31 | PASS | C-01b/c/d, C-02a/b at sub-step level, C-04a/b/c/d, C-09a/b/c/d individually annotated |
| C-32 | PASS | HARD RULE: "Blank cells are prohibited throughout... blank is not a permitted response for any labeled field [C-32]" |
| C-33 | PASS | `Preconditions [C-02a: list all; write "none" if genuinely absent; never leave blank]` — sub-criterion annotation |

**Aspirationals passed:** 22 of 25 (C-14, C-16, C-26 fail) → capped at 5 → **10 pts**

**V-03 Score: 60 + 30 + 10 = 100**

---

## V-04 — Role Sequence + Format: CS → Finance → Sales with Schema-Level Write-Time Enforcement

| ID | Result | Evidence |
|----|--------|----------|
| **C-01** | **PASS** | `[C-01a: sequential 1..N]`, `[C-01b: lifecycle state name only]`, `[C-01c: imperative verb phrase]`, `[C-01d: lifecycle state name]` in all three pass tables |
| **C-02** | **PASS** | `Preconditions [C-02a — write "none" if genuinely absent; never leave blank]` + `Postconditions [C-02b ...]` throughout |
| **C-03** | **PASS** | Two invariant columns per row: `Invariant 1 [C-03: real CS/Finance/Sales business constraint]` + `Invariant 2 [C-03: second ... — required]` |
| **C-04** | **PASS** | `[C-04a]` ID, `Type [C-04b]`, `Triggering Operation [C-04c]`, `Reason [C-04d]` in every defect log |
| **C-05** | **PASS** | CS / Finance / Sales domains |
| **C-06** | **PASS** | Uniform table format across all three passes |
| **C-07** | **PASS** | Exclusion list + qualifying example in every invariant register; `[C-07]` annotation in description column |
| **C-08** | **PASS** | Race section with named Op A/Op B and both independent orderings |
| C-09 | PASS | Negative path table `[C-09a–d]` + explicit mutation verification |
| C-10 | FAIL | No reachability annotation section |
| C-11 | PASS | Criterion IDs embedded in all column headers |
| C-12 | PASS | "Both orderings must be independently described — asymmetric conflict outcomes require it" |
| C-13 | PASS | `Derived From (Pass + Row) [C-13]` column in all invariant registers |
| C-14 | **PASS** | Explicit schema design note: "Filling a cell mechanically satisfies the embedded criterion — you cannot fill the cell without complying" |
| C-15 | PASS | Reference rows fully filled; invariant tables use `\| INV-C-01 \| … \| Pass 1 Row … \|` |
| C-16 | PASS | HARD RULES: "Prose is not a valid format for trace data — no prose substitutions [C-16]" |
| C-17 | PASS | "minimum 5 rows [C-17: fewer than 5 rows fails C-17]" per pass |
| C-18 | PASS | Three named disqualifying patterns in exclusion list |
| C-19 | PASS | "HARD RULES — any violation invalidates the entire artifact [C-19]" |
| C-20 | PASS | `Valid qualifying example [C-20]: "SLA clock must be running throughout the Open and Pending states."` |
| C-21 | PASS | "Do not write 'same as above' or any cross-reference to Ordering 1 [C-21]" |
| C-22 | PASS | `write "none" if genuinely absent` in precondition/postcondition column headers |
| C-23 | PASS | "at least one entry required; silent omissions invalidate this section [C-23]" in all three defect logs |
| C-24 | PASS | "Reference row — template anchor; do not reproduce in output [C-24]" |
| C-25 | PASS | Cross-Domain Invariant Register with explicit cross-pass derivation linkage |
| C-26 | PASS | "Minimum 15 transition rows total across all three passes [C-26]" + verification prompt |
| C-27 | PASS | Three named disqualifying patterns in enumerated list |
| C-28 | PASS | "Name both concurrent operations explicitly [C-28]" |
| C-29 | PASS | "write an explicit confirmation statement: declare that the state in [C-09c] is identical to [C-09a] and that no field values were modified [C-29]" |
| C-30 | PASS | `[C-02a — write "none" if genuinely absent; never leave blank]`; `[C-03: real CS business-rule invariant — must encode a real domain constraint, not a structural fact]` |
| C-31 | PASS | C-01a/b/c/d, C-02a/b, C-03×2, C-04a/b/c/d, C-09a/b/c/d all independently labeled |
| C-32 | PASS | HARD RULE: "blank is never a permitted entry [C-32]" + "never leave blank" in column headers |
| C-33 | PASS | `[C-02a — write "none" if genuinely absent; never leave blank]` — nil-value instruction at sub-criterion granularity |

**Aspirationals passed:** 24 of 25 (only C-10 fails) → capped at 5 → **10 pts**

**V-04 Score: 60 + 30 + 10 = 100**

---

## V-05 — Phrasing Register + Inertia Framing

| ID | Result | Evidence |
|----|--------|----------|
| **C-01** | **PASS** | `[C-01a]` `[C-01b]` `[C-01c]` `[C-01d]` in trace table headers |
| **C-02** | **PASS** | `Preconditions [C-02a — write "none" if genuinely absent; never leave blank]` + `Postconditions [C-02b ...]` |
| **C-03** | **PASS** | Two invariant columns: `Invariant 1 [C-03: a real Finance business rule]` + `Invariant 2 [C-03: second real Finance business rule — required]` |
| **C-04** | **PASS** | `[C-04a]`, `Type [C-04b]`, `Triggering Operation [C-04c]`, `Reason [C-04d]` |
| **C-05** | **PASS** | Finance domain |
| **C-06** | **PASS** | Consistent table format throughout |
| **C-07** | **PASS** | Exclusion list + qualifying example framed as "what DOES qualify" |
| **C-08** | **PASS** | Both orderings with full independence requirement |
| C-09 | PASS | Negative path table `[C-09a–d]` + "Active mutation verification [C-29]" |
| C-10 | PASS | Reachability Annotation section: "The naive trace silently omits the paths it does not test. Here, explicitly name every state transition NOT included…" |
| C-11 | PASS | Criterion IDs in column headers and section labels |
| C-12 | PASS | Both orderings required; "If outcomes are genuinely identical, demonstrate it by producing identical text — do not assert it" |
| C-13 | PASS | `Source Step` column in invariant summary links each invariant to its trace row |
| C-14 | FAIL | No explicit "mechanically satisfies" design note |
| C-15 | PASS | Reference row with filled values; invariant table uses `\| INV-01 \| … \| Step … \|` |
| C-16 | PASS | "No prose — every operation gets its own row, not a paragraph. If you find yourself writing a sentence instead of filling a cell, stop and restructure." — named declaration |
| C-17 | PASS | "Minimum 5 rows [C-17]" |
| C-18 | PASS | Three explicitly named disqualifying patterns with failure-mode explanations |
| C-19 | PASS | "Violating this constraint invalidates the artifact [C-19]" |
| C-20 | PASS | `"Here is what DOES qualify [C-20]: 'Invoice total must remain positive after any line-item modification.'"` |
| C-21 | PASS | "Do not write 'same as above,' 'symmetric,' or any reference to Ordering 1 [C-21]. Write it out completely as if Ordering 1 did not exist." |
| C-22 | PASS | `write "none" if genuinely absent` in all precondition/postcondition and negative-path columns |
| C-23 | FAIL | No section-level invalidation clause — defect log lacks "silent omissions invalidate this section" |
| C-24 | PASS | "Reference row — template only; do not copy this row into your output [C-24]" |
| C-25 | FAIL | Single domain — no cross-domain register |
| C-26 | FAIL | Single domain — no cross-pass aggregate floor |
| C-27 | PASS | Three named patterns with explicit explanations ("structural, not a business rule"; "a database constraint"; "a schema constraint") |
| C-28 | PASS | "Name both concurrent operations explicitly — do not name only the conflict [C-28]" |
| C-29 | PASS | "Active mutation verification [C-29]: …write one sentence that explicitly confirms no state mutation occurred" |
| C-30 | PASS | `[C-02a — write "none" if genuinely absent; never leave blank]`; `[C-03: a real Finance business rule — see exclusion list]` |
| C-31 | PASS | C-01a/b/c/d, C-02a/b, C-04a/b/c/d, C-09a/b/c/d individually labeled |
| C-32 | PASS | "A blank cell and a missing value are indistinguishable to a reviewer, so blank is never acceptable [C-32]" — plus anti-blank framing unique to V-05 |
| C-33 | PASS | `[C-02a — write "none" if genuinely absent; never leave blank]` — sub-criterion annotation |

**Aspirationals passed:** 21 of 25 (C-14, C-23, C-25, C-26 fail) → capped at 5 → **10 pts**

**V-05 Score: 60 + 30 + 10 = 100**

---

## Composite Scores

| Variation | Essential | Recommended | Aspirationals (capped) | **Total** | Aspirational Breadth |
|-----------|-----------|-------------|------------------------|-----------|---------------------|
| V-04 | 60 | 30 | 10 | **100** | 24/25 ✦ |
| V-01 | 60 | 30 | 10 | **100** | 23/25 |
| V-03 | 60 | 30 | 10 | **100** | 22/25 |
| V-02 | 60 | 30 | 10 | **100** | 21/25 |
| V-05 | 60 | 30 | 10 | **100** | 21/25 |

All five variations exceed the golden threshold (≥80, all essential pass). V-04 leads by aspirational breadth — only C-10 (reachability annotation) absent.

---

## Excellence Signals — V-04

**1. Schema design note as C-14 activation layer**
The single sentence *"Filling a cell mechanically satisfies the embedded criterion — you cannot fill the cell without complying"* is placed as a meta-instruction before the tables. It requires no changes to column headers — it reframes the existing criterion-in-header structure from C-11 (IDs are present) to C-14 (compliance is structurally unavoidable). One sentence, additive, zero structural cost.

**2. C-32/C-33/C-22 triple co-location via compound annotation**
`[C-02a — write "none" if genuinely absent; never leave blank]` satisfies all three criteria in a single label: C-33 (nil-value at sub-criterion level), C-22 (nil-value token itself), and C-32 (anti-blank prohibition). The semicolon creates structural separation between the nil-value instruction and the anti-blank prohibition, making them independently auditable despite co-location.

**3. C-12 + C-21 binding pair with consequence framing**
"Both orderings must be independently described — asymmetric conflict outcomes require it" couples the *purpose* of symmetric interleaving (C-12) with the prohibition against lazy copy (C-21) in a single sentence. The consequence ("asymmetric outcomes require it") is what prevents rationalized non-compliance — writers understand *why* both orderings are required.

**4. Reversed domain order (CS→Finance→Sales) achieves natural cross-domain invariant inheritance**
V-01's Finance-first order anchors hard numeric invariants first. V-04's CS-first order surfaces user-facing defects before financial validation, creating a different dependency direction. Combined with the cross-domain register, this means Finance invariants can explicitly reference CS-discovered defects — richer C-13 and C-25 content.

**5. C-10 as the single structural gap in multi-pass format**
V-04 and V-01 both omit C-10 (reachability annotation). V-03 and V-05 include it. The pattern is clear: the reachability annotation is architecturally orthogonal to multi-pass table format — it needs its own explicit section slot and doesn't emerge from any existing section. This is the one criterion that requires an additive structural decision rather than a label upgrade.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Schema design note as C-14 activation layer: one additive sentence before tables ('filling a cell mechanically satisfies the embedded criterion') elevates existing criterion-in-header structure from C-11 to C-14 without modifying column headers", "C-22/C-33/C-32 triple co-location via compound sub-element annotation: '[C-02a — write none if genuinely absent; never leave blank]' satisfies all three nil-value/anti-blank criteria in a single label using semicolon-separated independent clauses", "C-10 is architecturally orthogonal to multi-pass table format and cannot be earned without an explicit reachability section slot — it is the one criterion that requires additive structure rather than a label upgrade"]}
```
