---

## flow-throttle Variate Round 11 — Scorecard

**Rubric:** v11 | **Max composite:** 210 | **Criteria:** C-01–C-32 (5E, 3R, 24A)

---

### Scoring Foundation

**Baseline carry from R10 V-05 (verified under v11):**
- C-01–C-28: all PASS
- C-32: PASS — labeled "Escape route for C-26" present in all variations; states the C-22-redundancy counter-argument and rebuts it
- Open: C-29, C-30, C-31 (3 × 5 = 15 pts gap → 195 baseline)

R11 criteria under evaluation — pass conditions:

| ID | Pass Condition Core |
|----|---------------------|
| C-29 | Named annotation within/after C-27 closure with labeled fields applying C-18/C-26 form: (a) names implicit-complement inference, (b) traces it to content-inspection problem, (c) states how closure forecloses it |
| C-30 | C-29 annotation names ≥1 specific unregistered element type with a statement of classification ambiguity it creates under an open register |
| C-31 | Each audit path (compliance + absence) names ≥2 observables by artifact identifier AND structural position — independently falsifiable without parsing surrounding context |
| C-32 | Named demolisher element in C-26 annotation states the C-22-redundancy counter-argument and explains why it fails |

---

### V-01 — Single Axis: C-29 FAIL Isolation (prose baseline)

**Section B annotation form:** Prose paragraph under "Inertia annotation for C-27 — why the register must be declared closed (C-27):" — all three content elements present (implicit-complement inference named, content-inspection problem traced, closure explained) but embedded in narrative requiring reading comprehension, not field-presence scan.

**TYPE SCAN GATE audit test:** General scan language: "Confirm the gate step appears between TABLE E and TABLE F," "Confirm three per-category Y/N verdicts are present," "TABLE F opens immediately after TABLE E with no intervening named gate step."

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-01 | PASS | Carries from R10 V-05 |
| C-02 | PASS | Carries |
| C-03 | PASS | Carries |
| C-04 | PASS | Carries |
| C-05 | PASS | Carries |
| C-06–C-08 | PASS | Carries |
| C-09–C-28 | PASS | All 20 aspirational criteria carry |
| **C-29** | **FAIL** | Annotation is prose paragraph; no labeled "Failure mode prevented" / "Gap above C-25" fields; C-18/C-26 inertia-framing form absent — content present but not independently scannable by field lookup |
| **C-30** | **FAIL** | Structural dependency on C-29 labeled form — concrete examples exist in prose ("compound gate variant, a load-shape verdict label") but cannot be anchored to a C-29-compliant annotation that does not exist |
| **C-31** | **FAIL** | "Confirm three per-category Y/N verdicts are present" is a scan instruction, not a named observable with artifact ID; "between TABLE E and TABLE F" is a region, not an artifact-anchored structural position (TABLE E's last R-NN row / TABLE F's MR-01) |
| **C-32** | **PASS** | "Escape route for C-26" labeled section present; names the C-22-redundancy argument; rebuts via construction-time vs. post-hoc detection distinction |

**Composite:** 60 + 30 + 100 + 0 + 0 + 0 + 5 = **195/210**

---

### V-02 — Single Axis: Inertia Framing (C-29 minimal — two-field labeled annotation)

**Section B annotation form:** Two labeled fields under "Inertia annotation for C-27 — why the register must be declared closed (C-29):":
- `Failure mode prevented:` — implicit-complement classification, traces to content-inspection problem
- `Gap above C-25:` — C-25 compliance does not require register closure; closure converts implicit-exempt to explicitly-unclassified

**TYPE SCAN GATE audit test:** General scan language carries from V-01.

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-01–C-05 | PASS | Carries |
| C-06–C-08 | PASS | Carries |
| C-09–C-28 | PASS | All 20 aspirational carry |
| **C-29** | **PASS** | Named annotation ("Inertia annotation for C-27") with C-18/C-26 labeled-field form: "Failure mode prevented" field names implicit-complement inference and traces to content-inspection problem; "Gap above C-25" field states how closure forecloses it. All three pass-condition content elements satisfied in independently-scannable labeled form |
| **C-30** | **FAIL** | No concrete unregistered-element example in the labeled annotation; both fields use abstract language ("any unlisted element type," no specific example named). C-29 annotation exists but C-30's third-field requirement is absent |
| **C-31** | **FAIL** | General scan language carries from V-01; "between TABLE E and TABLE F" is not artifact-anchored to R-NN / MR-01 |
| **C-32** | **PASS** | Escape-route demolisher carries |

**Composite:** 60 + 30 + 100 + 5 + 0 + 0 + 5 = **200/210**

**Q1 result:** Two-field labeled form (without concrete example) satisfies C-29 minimum pass — confirmed. The compliance gap was structural form, not content. Form change alone closes C-29 while leaving C-30 as the independent open gap.

---

### V-03 — Single Axis: Lifecycle Emphasis (C-31 named-observable audit paths)

**Section B annotation form:** Prose paragraph carries from V-01 unchanged — C-29/C-30 remain open.

**TYPE SCAN GATE audit test:** Restructured with artifact-identifier anchoring and five named observables:
- *Gate-present:* "Locate the section titled **TYPE SCAN GATE** — artifact identifier: the exact section header string. Structural position: between TABLE E's last row (highest-numbered R-NN in Risk-ID column) and the TABLE F section header." Five named observables: `Burst: [Y / N]` verdict line, `Cascade: [Y / N]` verdict line, `RetryAfter: [Y / N]` verdict line, `PROCEED` or `BLOCKED` gate decision line (after verdicts, before TABLE F header), TABLE F header + MR-01 after gate decision line.
- *Gate-absent:* Position between last R-NN and MR-01 contains no **TYPE SCAN GATE** section header; observable: no `[Category]: [Y / N]` lines in that gap.

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-01–C-05 | PASS | Carries |
| C-06–C-08 | PASS | Carries |
| C-09–C-28 | PASS | All 20 aspirational carry |
| **C-29** | **FAIL** | Prose annotation carries from V-01; labeled-field form absent |
| **C-30** | **FAIL** | No C-29 labeled annotation to anchor example |
| **C-31** | **PASS** | Compliance path: "TYPE SCAN GATE" names artifact by exact header string; structural position anchored to TABLE E's last R-NN row and TABLE F header — two artifact-ID + structural-position anchors. Five named observables each independently falsifiable: the three per-category `[Category]: [Y / N]` verdict lines (form-specified), the `PROCEED`/`BLOCKED` decision line (position: after verdicts, before TABLE F), the TABLE F + MR-01 position (not first after R-NN). Gate-absent path: structural gap between R-NN and MR-01 named; distinguishing observable (`[Category]: [Y / N]` lines absent) specified. Passes ≥2 observables by artifact ID + structural position on both paths |
| **C-32** | **PASS** | Escape-route demolisher carries |

**Composite:** 60 + 30 + 100 + 0 + 0 + 5 + 5 = **200/210**

**Q2 result:** Artifact-ID anchoring satisfies C-31 independently of inertia framing change — confirmed. C-29/C-30 and C-31 are orthogonal structural regions with no cross-dependency.

---

### V-04 — Combined: Three-Field Annotation + Named-Observable Audit Paths

**Section B annotation form:** Three labeled fields under "Inertia annotation for C-27 — why the register must be declared closed (C-29, C-30):":
- `Failure mode prevented:` — implicit-complement inference → content-inspection problem
- `Gap above C-25:` — C-25 compliance ≠ closure; closure converts implicit-exempt to explicitly-unclassified
- `Concrete example (C-30):` — load-shape verdict label ("FLAT-LOAD: within nominal band") — traces all four classification-attempt failures against registered forms (not gate decision, not cross-artifact header, not phase boundary prohibition, not per-criterion verdict); states open-register inference path ("implicit-complement inference available") and closed-register consequence ("inference foreclosed: element type is unregistered, its Prose? and C-23-tag status is explicitly unresolved")

**TYPE SCAN GATE audit test:** Same named-observable form as V-03.

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-01–C-05 | PASS | Carries |
| C-06–C-08 | PASS | Carries |
| C-09–C-28 | PASS | All 20 carry |
| **C-29** | **PASS** | Three-field labeled annotation; same C-18/C-26 form as V-02 plus third field. "Failure mode prevented" and "Gap above C-25" fields satisfy all three C-29 content requirements in labeled-field form |
| **C-30** | **PASS** | Third field "Concrete example (C-30)" names "load-shape verdict label" (FLAT-LOAD: within nominal band) as specific unregistered type; traces four-way classification failure against all registered canonical forms; states ambiguity under open register (implicit-complement available) vs. closed register (explicitly unresolved). Independently testable: a reader can check FLAT-LOAD against the register's four canonical forms themselves |
| **C-31** | **PASS** | Named-observable audit paths carry from V-03 |
| **C-32** | **PASS** | Escape-route demolisher carries |

**Composite:** 60 + 30 + 100 + 5 + 5 + 5 + 5 = **210/210**

**Q3 preview:** V-04 achieves 210/210 without role separation — the three criteria are orthogonal and satisfiable in a single-role prompt. V-05 tests whether role separation adds architectural enforcement above this score.

---

### V-05 — Combined: Role Sequence + Three-Field Annotation + Named-Observable Audit Paths

**Role 1 (Format Analyst):** Produces complete OUTPUT FORMAT CONTRACT — including Section B with three-field labeled inertia annotation — and exits with "FORMAT CONTRACT COMPLETE" as the structural precondition for Role 2 activation. The three-field annotation is a role deliverable, not an inline note.

**Role 2 (Domain Expert):** Activates only after FORMAT CONTRACT COMPLETE; produces evidence and claims through TABLE E. Encounters the closed register as a pre-established contract; cannot modify it.

**Role 3 (Consequence Analyst):** Activates only after TYPE SCAN GATE is cleared; produces TABLE F and global criterion-coverage step. Owns the TYPE SCAN GATE with named-observable audit paths.

**Section B annotation form:** Same three-field content as V-04, now produced as Format Analyst deliverable.

**TYPE SCAN GATE:** Same named-observable paths as V-03/V-04, now owned by Consequence Analyst role.

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-01–C-05 | PASS | Carries |
| C-06–C-08 | PASS | Carries |
| C-09–C-28 | PASS | All 20 carry |
| **C-29** | **PASS** | Three-field labeled annotation as Format Analyst role deliverable — presence verifiable against role output, not executor willingness. Same content as V-04 |
| **C-30** | **PASS** | Same FLAT-LOAD concrete example as V-04; same four-way classification trace and open/closed register ambiguity statement |
| **C-31** | **PASS** | Five named observables with artifact-ID + structural-position anchors; now owned by Consequence Analyst — independent verification at role boundary |
| **C-32** | **PASS** | Escape-route demolisher in Consequence Analyst output |

**Composite:** 60 + 30 + 100 + 5 + 5 + 5 + 5 = **210/210**

**Q3 result:** Three-role pipeline does produce structural enforcement V-04 cannot: Format Analyst's FORMAT CONTRACT COMPLETE exit condition closes the register before Domain Expert activation — enforcement is architectural (structural precondition) rather than instructional (executable may ignore). However, both V-04 and V-05 score 210/210 — the enforcement upgrade improves robustness without adding scoreable points at this rubric version.

---

### Variation Ranking

| Rank | Variation | Score | All Essential | Delta from prior |
|------|-----------|-------|---------------|-----------------|
| 1 | **V-05** | **210/210** | PASS | — (architectural enforcement over V-04) |
| 1 | **V-04** | **210/210** | PASS | First combined-axis 210 |
| 3 | **V-02** | **200/210** | PASS | +5 vs V-01 (C-29 via form change) |
| 3 | **V-03** | **200/210** | PASS | +5 vs V-01 (C-31 via artifact anchoring) |
| 5 | **V-01** | **195/210** | PASS | baseline |

V-04 and V-05 are co-ranked at 210/210. V-05 is architecturally stronger (role-deliverable annotation, structural register closure before Domain Expert activation) but produces no additional scoring delta at the current rubric ceiling.

---

### Excellence Signals from Top-Scoring Variations

**E-01 — Three-field annotation with independent-testability third field (V-04, V-05)**
The `Failure mode prevented / Gap above C-25 / Concrete example` structure assigns each annotation layer to a distinct rubric obligation. The third field's function is not decoration — it converts the content-inspection risk from an abstract claim into a testable assertion: a reader can check FLAT-LOAD against the four registered canonical forms themselves and confirm the four-way classification failure. The concrete example makes the inertia argument falsifiable by a reader who has never seen the rubric.

**E-02 — Four-way classification-failure trace for concrete example (V-04, V-05)**
V-04's FLAT-LOAD example doesn't merely state that classification is ambiguous — it walks through each registered canonical form (gate decision line, cross-artifact header, phase boundary prohibition, per-criterion verdict) and names the non-match explicitly. This forces the claim to stand on structural evidence rather than assertion: the four-way non-match is independently verifiable and cannot be dismissed by naming one of the four forms as a match.

**E-03 — Role-deliverable format contract via exit-condition sequencing (V-05)**
Producing the format contract as a named role's output (with a `FORMAT CONTRACT COMPLETE` exit condition) converts compliance verification from a content check to a structural check: the annotation's presence is verifiable against the Format Analyst's output, not against the executor's mid-prompt decisions. The exit condition also makes the register closure architectural — the Domain Expert is structurally precluded from encountering an unregistered type before the register is declared closed.

**E-04 — Structural-position anchoring to R-NN / MR-01 boundaries (V-03, V-04, V-05)**
Replacing "between TABLE E and TABLE F" with "between TABLE E's last row (highest-numbered R-NN) and TABLE F's first data row (MR-01)" gives each audit path an artifact-identifier anchor that is independently resolvable without reading the gate section itself. The R-NN / MR-01 boundary is the minimum verifiable structural position — an auditor scanning only the Risk-ID and MR-ID columns can locate the gate region without understanding the gate's content.

---

```json
{"top_score": 210, "all_essential_pass": true, "new_patterns": ["Three-field labeled inertia annotation with concrete-testability third field: 'Failure mode prevented / Gap above prior criterion / Concrete example' structure makes each annotation layer independently scannable and the content-inspection risk claim independently testable via four-way canonical-form non-match trace", "Role-deliverable format contract via FORMAT CONTRACT COMPLETE exit condition: producing format contract elements as a named role's output converts compliance verification from executor discretion to structural precondition, closing the register before Domain Expert activation"]}
```
