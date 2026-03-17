## Quest Score — campaign-evidence R11

**Rubric version**: v11 | **Criteria**: 4 essential, 3 recommended, 26 aspirational | **Denominator**: 26

---

### C-32 and C-33 Placement Across Variates

Before scoring, locating the two new criteria in each variate:

| Variate | C-32 placement | C-33 placement |
|---------|---------------|----------------|
| V-01 | Role Roster table in preamble + repeated as role header at each stage boundary; explicit "information boundary" framing | Coverage map + checksum expression: `20 = 12 + 8 = 4 × 5`; audit table pre-populated 20 rows |
| V-02 | Role Roster table in preamble (minimal; no per-stage inline repeat) | Coverage map with totals column + checksum cell; arithmetic verification section at output close |
| V-03 | P0-B in Phase 0 commitment ledger; scope declaration required before Phase 1 can open | P0-D; locked at Phase 0 close; verified in Phase 6 checksum table |
| V-04 | Role Roster + Artifact Signatures table; scopes enforced via artifact provenance (citation must come from authorized artifacts) | Coverage map + checksum expression; pre-populated 20-row audit table uses artifact names |
| V-05 | Article II; "SHALL NOT read information outside a role's declared access scope"; violation treated as gate failure | Article III (INVOCATION MATRIX CHECKSUM); hard constraint: brief SHALL NOT be delivered until count = 20 |

---

### Criterion-by-Criterion Evaluation

#### Essential (C-01 – C-04)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01: 5-stage campaign | PASS | PASS | PASS | PASS | PASS |
| C-02: Evidence before hypothesis | PASS | PASS | PASS | PASS | PASS |
| C-03: Falsification conditions | PASS | PASS | PASS | PASS | PASS |
| C-04: Self-contained output | PASS | PASS | PASS | PASS | PASS |

All five variates: **4/4 essential pass**.

---

#### Recommended (C-05 – C-07)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-05: Source attribution per claim | PASS | PASS | PASS | PASS | PASS |
| C-06: Synthesis separates consensus/conflict | PASS | PASS | PASS | PASS | PASS |
| C-07: Calibrated confidence (not uniform) | PASS | PASS | PASS | PASS | PASS |

All five variates: **3/3 recommended pass**.

---

#### Aspirational (C-08 – C-33)

Evaluated per criterion; only failures noted in detail.

**C-08** (gaps surfaced): All five have explicit "Gaps and Open Questions" section. PASS ×5.

**C-09** (decision readiness signal): All five require the "Decision Readiness" signal. PASS ×5.

**C-10** (hypotheses declared post-evidence): All five place hypothesis declaration at Stage 3, gated behind Stage 1+2 exit. PASS ×5.

**C-11** (calibration anti-pattern guard): All five include an explicit "if all ratings are uniform, recalibrate" instruction in the CALIBRATION RULE. PASS ×5.

**C-12** (decision readiness compressed to one sentence): All five specify "one sentence" for Decision Readiness. PASS ×5.

**C-13** (named rules declared at preamble + invoked at point of use): All five have Rule Registry with identifiers, invoked by name at every stage. PASS ×5.

**C-14** (hypothesis reordering rationale stated):
- V-01: "A hypothesis anchored before evidence gathering is a bias, not a hypothesis." PASS.
- V-02: "Rationale: pre-evidence hypotheses are anchors, not hypotheses." PASS.
- V-03: "Rationale: a hypothesis declared before evidence is a bias, not a hypothesis." PASS.
- V-04: SEQUENCING RULE states the artifact-provenance enforcement mechanism but does not include the "bias, not a hypothesis" rationale sentence. **FAIL**.
- V-05: "Rationale: a hypothesis anchored before evidence gathering is a bias, not a hypothesis." PASS.

**C-15** (sequencing formalized as named rule): SEQUENCING RULE is declared by name in all five. PASS ×5.

**C-16** (zero-gap invocation — no applicable stage left untagged): All five invoke all four rules at all five stages (positive or negative). Traced counts: 20 invocations per variate, matching the coverage map. PASS ×5.

**C-17** (coverage mapping declared prospectively): All five have a coverage map table in the preamble before Stage 1. PASS ×5.

**C-18** (all governance rules at peer tier): All five have peer-equality declarations. PASS ×5.

**C-19** (coverage map immutability explicitly declared): All five include "immutable / cannot be modified after any stage executes." PASS ×5.

**C-20** (rule scope embedded inline): All five embed `[scope: S1(+), S2(-), ...]` (or equivalent) directly in the rule declaration body. PASS ×5.

**C-21** (interrogative invocation at critical rules): All five use `At least two distinct confidence levels present? [ Yes / No ]` at CALIBRATION's positive stages. PASS ×5.

**C-22** (universal binary invocation format): All five apply `[ Yes / No ]` (or `[ No — inapplicable ]`) at every invocation point. PASS ×5.

**C-23** (stage-indexed invocation trail): All five use `[Stage N of 5]` suffix. PASS ×5.

**C-24** (per-stage entry and exit conditions): All five have explicit entry and exit gates at every stage. PASS ×5.

**C-25** (gate record as named output artifact): All five include the gate record in the final output (V-01/V-04: dedicated Gate Record section; V-02: pre-declared table in preamble carried through; V-03: Phase 0 P0-E included in Phase 6 governance record; V-05: Article IV gate table is part of the delivery document). PASS ×5.

**C-26** (consolidated invocation audit table in final output): All five have a 20-row consolidated audit table required in the final output. V-02's approach of inline append during execution produces the same artifact in the output. PASS ×5.

**C-27** (gate record pre-templated in preamble with blank cells): All five include a blank gate record template in the preamble before Stage 1. PASS ×5.

**C-28** (sequencing compliance as machine-verifiable column value):
- V-01: SEQUENCING is enforced via gate conditions and invocation tags; the hypothesis register has a "Grounding" column but the SEQUENCING RULE's primary enforcement mechanism is prose gates + binary tags, not a sortable column. **FAIL**.
- V-02: Same mechanism as V-01; enforcement is via invocation tags and stage ordering. **FAIL**.
- V-03: Per-stage rule invocation tables have rules as rows (not evidence items). No unified evidence/hypothesis table with sortable stage column. **FAIL**.
- V-04: SEQUENCING RULE explicitly states "An ARTIFACT-S3 entry citing sources outside ARTIFACT-S1 and ARTIFACT-S2 is a sequencing violation at the artifact-provenance level." The hypothesis register has a "Source Artifacts" column (ARTIFACT-S1, ARTIFACT-S2, etc.) per hypothesis row. This is the "grounded-in constraints (hypothesis rows may reference only S1/S2 stage rows)" mechanism described in C-28's pass condition. **PASS**.
- V-05: Same as V-01/V-02; SEQUENCING enforced via SHALL NOT gates and invocation tags, no sortable column. **FAIL**.

**C-29** (governance framework extensible without static updates):
- V-01: "This declaration updates automatically as rules are added; no rule has primary status." Explicit extensibility claim. PASS.
- V-02: "Newly added rules inherit peer status automatically." PASS.
- V-03: "This declaration is extensible: adding a rule does not require updating any static integer or priority ranking." Most explicit. PASS.
- V-04: Rule Registry header says "(all peers)" but contains no statement that adding a rule does not require static updates. No extensibility claim anywhere. **FAIL**.
- V-05: "Adding a rule SHALL NOT require updating any static integer elsewhere in this brief." PASS.

**C-30** (named role handoffs with explicit transfer declarations): All five use "> **Role passes to: Stage N — Role Name**" (or equivalent "Transfer to:" / "SHALL transfer control to:") at every stage boundary. PASS ×5.

**C-31** (negative invocations at non-applicable stages): All five include explicit negative invocations — e.g., "CALIBRATION RULE [Stage 1 of 5] — Applicable here? [ No — not yet applicable ]" — at every non-applicable cell. PASS ×5.

**C-32** (role access scope declared per stage): All five include a Role Roster table with access scope per role. Scopes specify which prior-stage outputs each role is authorized to read. PASS ×5.

**C-33** (invocation matrix total pre-declared as derivable checksum): All five pre-declare `20 invocation artifacts = 12 positive + 8 negative, derived from 4 rules × 5 stages` in the preamble before Stage 1. PASS ×5.

---

### Aspirational Failure Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-14 (sequencing rationale stated) | PASS | PASS | PASS | **FAIL** | PASS |
| C-28 (column-encoded stage index) | **FAIL** | **FAIL** | **FAIL** | PASS | **FAIL** |
| C-29 (extensible without static updates) | PASS | PASS | PASS | **FAIL** | PASS |
| All other aspirational | PASS | PASS | PASS | PASS | PASS |

---

### Composite Scores

Formula: `(essential_pass/4 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/26 * 10)`

| Variate | Essential | Recommended | Aspirational | Composite |
|---------|-----------|-------------|--------------|-----------|
| V-01 | 4/4 = 60 | 3/3 = 30 | 25/26 = 9.62 | **99.6** |
| V-02 | 4/4 = 60 | 3/3 = 30 | 25/26 = 9.62 | **99.6** |
| V-03 | 4/4 = 60 | 3/3 = 30 | 25/26 = 9.62 | **99.6** |
| V-04 | 4/4 = 60 | 3/3 = 30 | 24/26 = 9.23 | **99.2** |
| V-05 | 4/4 = 60 | 3/3 = 30 | 25/26 = 9.62 | **99.6** |

---

### Ranking

1. **V-01, V-02, V-03, V-05** — tied at **99.6** (each fails only C-28)
2. **V-04** — **99.2** (fails C-14 and C-29; uniquely passes C-28 via artifact provenance)

---

### Excellence Signals

**From the top-scoring variates (V-01, V-03, V-05 in particular):**

**Signal 1 — Access scope as information-boundary declaration (V-01, C-32):** When a role's access scope is an explicit authorized-artifact list rather than a structural convention, a hypothesis citing pre-Stage-1 information becomes a role-charter violation — visible at the provenance level regardless of whether stage ordering appears correct. V-01's Role Roster table makes this structurally legible: "Any hypothesis constructed using information that predates Stage 1 violates this role's access scope." Impersonation is detectable at the boundary, not only after parsing the full sequence.

**Signal 2 — Checksum as subtraction problem (V-02 and all variates via C-33):** Pre-declaring `20 = 12 + 8 = 4 × 5` before Stage 1 converts completeness from a scan into arithmetic. Any executor who skips a negative invocation produces a row count that mismatches the pre-declared value. V-02 makes this the primary structural anchor — the final "Arithmetic Verification" section has Expected/Actual/Match cells that make the check explicit without reading the stage narrative.

**Near-miss from V-04:** V-04's artifact-provenance approach (C-28 PASS via grounded-in constraints) is structurally interesting — it makes sequencing violations visible at the source-citation level in the hypothesis register. However, V-04 sacrifices C-14 (no rationale sentence for why evidence must precede hypothesis) and C-29 (no extensibility declaration for the rule registry), which cost it the tie with the top group. The C-28 mechanism V-04 demonstrates should be the next signal for R12.

---

```json
{"top_score": 99.6, "all_essential_pass": true, "new_patterns": ["access scope as information boundary: declaring each role's authorized-artifact list makes hypothesis pre-commitment visible as a role charter violation at the provenance level, not just a stage-ordering violation", "invocation matrix checksum pre-declared as derivable expression (rules x stages) before Stage 1 converts coverage completeness from a scan into arithmetic — a missing invocation produces a count mismatch detectable without reading stage content"]}
```
