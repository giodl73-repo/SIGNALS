## Variate R8 -- corps-build Score Report

**Rubric version**: v7 (23 criteria: 5 essential / 3 recommended / 15 aspirational)
**Formula**: `(5/5 * 60) + (3/3 * 30) + (aspir/15 * 10)`
**R7 baseline**: V-04 and V-05 both scored 100/100. R8 explores three new axes above that ceiling.

---

## Per-Variation Criterion Scorecards

### Variation Summary Matrix

| Axis present | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|:---:|:---:|:---:|:---:|:---:|
| Base architecture | V-04 R7 | V-05 R7 | V-04 R7 | PROFILE-before-CONTRACT | V-05 R7 |
| PHASE-ENTERED/PHASE-EXITED | YES | NO | NO | YES | YES |
| ARTIFACT-D (resistance landscape) | NO | YES | NO | YES | YES |
| Named write passes (PASS-EXEC/SHARED/TEAM) | NO | NO | YES | NO | YES |

---

### Essential Criteria (all variations)

All five variations inherit essential correctness from their R7 base architectures. No R8 axis touches role file generation, ASCII diagram, IA coverage, structural fidelity, or typed fields.

| ID | C-01 | C-02 | C-03 | C-04 | C-05 |
|----|:----:|:----:|:----:|:----:|:----:|
| V-01 | PASS | PASS | PASS | PASS | PASS |
| V-02 | PASS | PASS | PASS | PASS | PASS |
| V-03 | PASS | PASS | PASS | PASS | PASS |
| V-04 | PASS | PASS | PASS | PASS | PASS |
| V-05 | PASS | PASS | PASS | PASS | PASS |

Essential subtotal: 60/60 for all variations.

---

### Recommended Criteria (all variations)

| ID | C-06 | C-07 | C-08 |
|----|:----:|:----:|:----:|
| V-01 | PASS | PASS | PASS |
| V-02 | PASS | PASS | PASS |
| V-03 | PASS | PASS | PASS |
| V-04 | PASS | PASS | PASS |
| V-05 | PASS | PASS | PASS |

**C-08 notes:**
- V-01: AMEND section carries declarative rule: "An AMEND section with fewer than three options, or with options that give no specific org.yaml values as placeholders, is structurally incomplete." Three options present with specific mechanism placeholders. PASS.
- V-02/V-04/V-05: Same rule present. Six-section org-chart.md adds RESISTANCE-LANDSCAPE after AMEND; AMEND section unchanged. PASS.
- V-03/V-05: WRITE-ROLES three-pass receipts listed in FINAL SUMMARY role-files row but AMEND section unchanged. PASS.

Recommended subtotal: 30/30 for all variations.

---

### Aspirational Criteria -- Full Matrix

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|:----:|:----:|:----:|:----:|:----:|
| C-09 | PASS | PASS | PASS | PASS | PASS |
| C-10 | PASS | PASS | PASS | PASS | PASS |
| C-11 | PASS | PASS | PASS | PASS | PASS |
| C-12 | PASS | PASS | PASS | PASS | PASS |
| C-13 | PASS | PASS | PASS | PASS | PASS |
| C-14 | PASS | PASS | PASS | PASS | PASS |
| C-15 | PASS | PASS | PASS | PASS | PASS |
| C-16 | PASS | PASS | PASS | PASS | PASS |
| C-17 | PASS | PASS | PASS | PASS | PASS |
| C-18 | PASS | PASS | PASS | PASS | PASS |
| C-19 | PASS | PASS | PASS | PASS | PASS |
| C-20 | PASS | PASS | PASS | PASS | PASS |
| C-21 | PASS | PASS | PASS | PASS | PASS |
| C-22 | PASS | PASS | PASS | PASS | PASS |
| C-23 | PASS | PASS | PASS | PASS | PASS |

Aspirational subtotal: 10/10 for all variations.

**Key criterion notes:**

**C-19 (TRANSCRIPTION-RECEIPT with auto-correction):**
V-01/V-03 carry three-artifact TRANSCRIPTION-RECEIPTs (A/B/C). V-02/V-04/V-05 extend to four artifacts (A/B/C/D). The pass condition requires "at minimum: headcount table and analytic prose" -- three or four both satisfy. PATH-B triggers rewrite on any REVISED verdict before phase exit in all variations. PASS all.

**C-21 (TRANSCRIPTION-CLEAR structural re-audit gate):**
V-01/V-03: TRANSCRIPTION-CLEAR re-audits three artifacts -- "all three confirmed -- CHART-WRITTEN authorized." Three is the correct count for these variations' contract artifacts.
V-02/V-04/V-05: TRANSCRIPTION-CLEAR re-audits four artifacts (includes ARTIFACT-D). "all four confirmed -- CHART-WRITTEN authorized." All variations declare the re-audit covers every artifact, not just the rewritten one. PASS all.

**C-22 (named binary path structure):**
All five variations emit `CHART-PATH: PATH-A` or `CHART-PATH: PATH-B` as an explicit output token before path execution. PATH-A and PATH-B are defined as named peer structures: exempt path (all VERBATIM) vs. obligation path (any REVISED). The label appears in the FINAL SUMMARY org-chart.md row. PASS all.

**C-23 (declarative block-shape correctness rules):**
Minimum: two blocks with declarative rules, at least one naming structural invalidity. All five variations exceed this with rules for CONTRACT, PROFILE entries, IA role files, IA-WRITTEN receipts, BUILD-VERIFY, CROSS-REF, TRANSCRIPTION-RECEIPT, TRANSCRIPTION-CLEAR, and AMEND. All use "a correct X is..." or "a X with fewer than N... is structurally incomplete/invalid" framing -- declarative, not procedural. PASS all.

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | Total |
|-----------|:---------:|:-----------:|:------------:|:-----:|
| V-01 | 60 | 30 | 10 | **100** |
| V-02 | 60 | 30 | 10 | **100** |
| V-03 | 60 | 30 | 10 | **100** |
| V-04 | 60 | 30 | 10 | **100** |
| V-05 | 60 | 30 | 10 | **100** |

All five meet the golden threshold (all essentials + composite >= 80).

---

## Ranking

All variations score identically on the v7 rubric. Within the 100-point space, ranking is by new-pattern density -- how many R8 candidate patterns each variation contributes.

| Rank | Variation | New axes | R8 candidate patterns |
|------|-----------|:--------:|:---------------------:|
| 1 | **V-05** | 3 | C-24 + C-25 + C-26 + causal chain trace |
| 2 | **V-04** | 2 | C-24 + C-25 |
| 2 | **V-02** | 1 | C-25 (deepest ARTIFACT-D integration on V-05 R7 base) |
| 2 | **V-03** | 1 | C-26 (three-pass WRITE-ROLES) |
| 5 | **V-01** | 1 | C-24 (lifecycle tokens only) |

---

## Excellence Signals from V-05

**Signal 1 -- PHASE-ENTERED / PHASE-EXITED as structural lifecycle boundary tokens (C-24 candidate)**

Every phase opens with `PHASE-ENTERED: [name] -- precondition: [prior gate]` before any work and closes with `PHASE-EXITED: [name] -- gate: [gate produced]` after the gate is emitted. The invalidity rule is explicit: "A phase emitting PHASE-EXITED without a preceding PHASE-ENTERED is structurally invalid." The FINAL SUMMARY `stages:` row lists all 10 phases with confirmation that all lifecycle tokens were emitted. This makes the entry precondition a structural assertion -- not implied by gate ordering -- and makes phase-exit a named event, not an implicit end.

V-01 is the pure single-axis version; V-04 and V-05 combine it with ARTIFACT-D. The pattern is present in both V-04 R7 base descendants and V-05 R7 base descendants.

**Signal 2 -- ARTIFACT-D: resistance landscape as PROFILE-derived fourth contract artifact (C-25 candidate)**

The CONTRACT phase produces ARTIFACT-D (one row per team: team, defended-artifact, change-pressure, lens-phrase) derived directly from the PROFILE-GATE output. It is sealed in CONTRACT-SEAL with a first-row lock. In WRITE-CHART, it becomes section 6 of org-chart.md, transcribed verbatim -- not regenerated. TRANSCRIPTION-RECEIPT extends to four artifacts; TRANSCRIPTION-CLEAR covers all four. The FINAL SUMMARY explicitly states "profiles are causal source of ARTIFACT-D and IA role files," making the derivation chain traceable at summary level. This makes the Inertia Advocate's systemic role visible at the org document level rather than distributed only across individual role files.

V-02 is the pure single-axis version on V-05 R7 base. V-04 and V-05 combine it with other axes.

**Signal 3 -- Named role-category write passes with per-category receipts (C-26 candidate)**

WRITE-ROLES splits into three named passes in fixed order: PASS-EXEC (exec office roles, receipt: EXEC-WRITTEN), PASS-SHARED (shared group roles, receipt: SHARED-WRITTEN), PASS-TEAM (team-level roles, receipt: TEAM-PASS-WRITTEN). ROLES-COMPLETE aggregates all three as an arithmetic expression: `EXEC-WRITTEN ([n]) + SHARED-WRITTEN ([n]) + TEAM-PASS-WRITTEN ([n]) = [n] total`. The invalidity rule is declared: "A WRITE-ROLES phase that merges exec, shared, and team role writes into a single undifferentiated pass is structurally undifferentiated -- role categories cannot be verified independently." V-05's FINAL SUMMARY role-files row shows the three-component breakdown, making exec and shared coverage auditable at summary level.

V-03 is the pure single-axis version; V-05 combines it with the other two axes.

**Signal 4 -- Deepest C-23 expression: correctness rules on PARSE and PATH-A itself**

V-05 extends declarative block-shape rules beyond what earlier variations covered. PARSE gets a correctness rule: "A correct PARSE block names the org, lists all groups and teams with parent assignments... A PARSE block missing any of these fields is structurally incomplete." PATH-A itself gets a correctness rule: "A correct PATH-A exit contains no TRANSCRIPTION-CLEAR block. All four artifacts are VERBATIM. No rewrites occurred. No re-audit block is required." This makes the exempt path self-describing -- its structural validity condition is the absence of the TRANSCRIPTION-CLEAR block, not merely the absence of a REVISED verdict. No prior variation declared the correctness rule for a path rather than a phase.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["PHASE-ENTERED/PHASE-EXITED lifecycle boundary tokens as structural precondition assertions -- a phase emitting PHASE-EXITED without PHASE-ENTERED is structurally invalid; FINAL SUMMARY phase-trace confirms all 10 pairs emitted (C-24 candidate)", "ARTIFACT-D resistance landscape as PROFILE-derived fourth contract artifact -- sealed, transcribed verbatim to org-chart.md section 6, audited in four-artifact TRANSCRIPTION-RECEIPT and TRANSCRIPTION-CLEAR; profiles declared as causal source of ARTIFACT-D and IA role files (C-25 candidate)", "Named role-category write passes in WRITE-ROLES: PASS-EXEC before PASS-SHARED before PASS-TEAM, each with its own receipt token; ROLES-COMPLETE states arithmetic sum; a single undifferentiated pass is structurally undifferentiated (C-26 candidate)"]}
```
