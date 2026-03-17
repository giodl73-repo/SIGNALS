## corps-pr R19 Scorecard

### Evaluation Method

Audit each variation against v17 rubric criteria. All structure read from file; four R19 patterns (C-51--C-54) spot-checked per variation by direct evidence location.

---

### Criterion Audit

#### Essential (C-01--C-05, 12.0 pts each)

| Criterion | Evidence (all 5 variations) | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|----------------------------|------|------|------|------|------|
| C-01: Phase A routing table, every file has a row, scope patterns cited | All have `## Phase A: Routing` table template | PASS | PASS | PASS | PASS | PASS |
| C-02: Phase C minimum 2 findings per role | All have `F-01` + `F-02 [minimum 2]` | PASS | PASS | PASS | PASS | PASS |
| C-03: Phase D consensus with agreement/divergence/critical/ban-to-fix | All have `Agreement:`, `Divergence:`, `Critical:`, ban-to-fix table | PASS | PASS | PASS | PASS | PASS |
| C-04: Phase E exactly one GO/NO-GO/GO WITH CONDITIONS | All have `One decision. Values: GO, NO-GO, GO WITH CONDITIONS only.` | PASS | PASS | PASS | PASS | PASS |
| C-05: Phase C domain-lens gate applied to findings | All have `Apply domain-lens gate per finding: Step A ... Step B` | PASS | PASS | PASS | PASS | PASS |

**Essential: 5/5 all variations — 60.0 pts**

---

#### Recommended (C-06--C-08, 10.0 pts each)

| Criterion | Evidence | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|---------|------|------|------|------|------|
| C-06: Coverage gap declaration in Phase A | All have `COVERAGE GAP: [file] -- no org.yaml scope pattern covers this path.` | PASS | PASS | PASS | PASS | PASS |
| C-07: Phase C minimum findings satisfy domain-lens gate | All have `Step A ... Step B` filter with "Still NO -> drop" | PASS | PASS | PASS | PASS | PASS |
| C-08: Post-commitment delta block in findings | All have `Post-commitment delta: Pre-committed: ... After findings: [HELD / CHANGED]` | PASS | PASS | PASS | PASS | PASS |

**Recommended: 3/3 all variations — 30.0 pts**

---

#### Aspirational (C-09--C-54, ~0.217 pts each, 46 total)

**C-51 (IA adversarial designation label in section header):**

| Variation | Evidence | Result |
|-----------|---------|--------|
| V-01 | Line 216: `Status-quo champion [C-11]: First reviewer in the pipeline.` | PASS |
| V-02 | Lines 624--625: `Status-quo champion [C-11]: Null Hypothesis Defender. Sequenced first.` | PASS |
| V-03 | Line 1006: `Status-quo champion [C-11]: First reviewer in the pipeline.` | PASS |
| V-04 | Lines 1397--1398: `Status-quo champion [C-11]: Null Hypothesis Defender. Sequenced first.` | PASS |
| V-05 | Line 1783: `Status-quo champion [C-11]: Null Hypothesis Defender. Sequenced first [C-11].` | PASS |

**C-52 (sub-condition headers carry inline criterion annotations):**

| Variation | Evidence | Result |
|-----------|---------|--------|
| V-01 | Lines 107/111: `C1 ... [C-26]:` and `C2 ... [C-26/C-33]:` | PASS |
| V-02 | Lines 519/523: same pattern | PASS |
| V-03 | Lines 899/903: same pattern | PASS |
| V-04 | Lines 1291/1295: same pattern | PASS |
| V-05 | Lines 1674/1678: same pattern | PASS |

**C-53 (Budget verdict clause lines carry `[C-25]` end-of-line annotations):**

| Variation | Evidence | Result |
|-----------|---------|--------|
| V-01 | Lines 231--233: `<- B3 line 1 [C-25]`, `<- B3 line 2 [C-25]`, `<- B3 line 3 [C-25]` | PASS |
| V-02 | Lines 640--642: same pattern; B3 line 3 uses null-hypothesis language | PASS |
| V-03 | Lines 1021--1023: same pattern | PASS |
| V-04 | Lines 1413--1415: same pattern | PASS |
| V-05 | Lines 1799--1801: same pattern | PASS |

**C-54 (C2 RESULT field (e) names both evidence forms as explicit disjuncts):**

| Variation | Evidence | Result |
|-----------|---------|--------|
| V-01 | Line 309: `[valid: inline value OR cross-reference "see PRE-COMMITMENT block: [row]"]` | PASS |
| V-02 | Line 709: same | PASS |
| V-03 | Line 1089: same | PASS |
| V-04 | Lines 1485--1486: same | PASS |
| V-05 | Line 1875: same | PASS |

**Remaining aspirational criteria (C-09--C-50), all carried from R18 invariant core:**

All five variations carry the complete invariant structure. Spot-checked key indicators:

| Criterion cluster | Evidence anchor | All 5 |
|-------------------|----------------|-------|
| C-11: IA sequenced first, structured as reference object | `Status-quo champion [C-11]:` label present and sequenced before all role reviews | PASS |
| C-17/C-19/C-21: IA findings ≥2, cost ledger 4×2, B5 verdict in cost terms | `F-01`/`F-02` in Phase B; 4-row cost ledger; `IA verdict: BLOCK / CONDITION / PASS` | PASS |
| C-25: Budget verdict string-matchable three-clause formula | `WORSE rows:` / `BETTER rows:` / `Conclusion:` on own lines | PASS |
| C-26: Named result tokens for C1/C2 | `C1 RESULT: ALL CLEAR` / `C2 RESULT: SATISFIED` / `C2 RESULT: UNSATISFIED` | PASS |
| C-27: PRE-COMMITMENT before findings | `STEP 3 -- PRE-COMMITMENT [C-27, before reading diff]` declared before `STEP 4 -- FINDINGS` | PASS |
| C-33/C-35/C-36: READ RECEIPT completeness, ordering, gate failure | (a)-(e) fields; STEP 1 before STEP 2; ordering violation = Phase D blocked | PASS |
| C-34/C-38/C-40: F-01 column-header schema | `[IA-VERDICT]` and `[ROLE-MECHANISM]` as column headers in findings table | PASS |
| C-37/C-39: C2 RESULT self-contained block | (a)-(e) PRESENT/ABSENT; terminal verdict in same block | PASS |
| C-41/C-46: Three-level enforcement partition + named path-negation | `Structural enforcement levels [C-41]:` with `Eliminated [C-46]:` sub-entry | PASS |
| C-43/C-45: CLOSED PATHS enumeration + format-rules restatement | `Closed paths [C-43]:` block in all pipeline declarations | PASS |
| C-49/C-50: Reverse cross-reference + bidirectional symmetry | `Declaration: see "Closed paths [C-43]:"` in `Eliminated [C-46]:` + `Audit loop closed [C-50]:` | PASS |

**Aspirational: 46/46 all variations — 10.0 pts**

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational | Composite |
|-----------|-----------|-------------|--------------|-----------|
| V-01 (Lifecycle Emphasis) | 60.0 | 30.0 | 10.0 | **100** |
| V-02 (Inertia Framing) | 60.0 | 30.0 | 10.0 | **100** |
| V-03 (Output Format / Risk Register) | 60.0 | 30.0 | 10.0 | **100** |
| V-04 (Lifecycle + Inertia) | 60.0 | 30.0 | 10.0 | **100** |
| V-05 (Full Combination) | 60.0 | 30.0 | 10.0 | **100** |

**All five variations: 46/46 aspirational, composite 100 against v17 rubric.**
R19 prediction confirmed.

---

### Excellence Signals

All five variations score 100. No single top-scoring variation. R19 is a propagation verification round -- the four patterns introduced in v17 (C-51--C-54) cleanly integrate across all variation axes without structural degradation. Observations:

**Patterns present in R19 that extend beyond C-51--C-54:**

1. **C2 sub-condition per-requirement criterion annotations** -- V-01 and V-05 (and by inspection all variations) carry per-bullet criterion annotations within the C2 sub-condition description: `[C-37]`, `[C-39]`, `[C-54]`, `[C-35]` on each compliance requirement line inside C2. C-52 requires the header-level annotation; these per-bullet annotations make each C2 sub-requirement individually traceable without reading the rubric. This goes beyond what C-52 requires.

2. **Imperative-register annotation directives** (V-05 pattern) -- Phase B template carries the annotation requirement as an output directive: _"Start each line with its clause label and end it with its governing criterion annotation."_ C-53 declares the annotation must be present; V-05 encodes compliance as a procedural instruction. The annotation requirement is now both structurally declared and operationally directed.

Neither pattern closes a gap large enough to warrant a new criterion -- the C2 per-bullet annotation is an extension of C-52 scope rather than a separate auditable dimension, and the imperative register encoding is stylistic. **No new criteria are extracted from R19.** The round confirms that the R18 excellence signal layer (C-51--C-54) is fully compatible with all five variation axes.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": []}
```
