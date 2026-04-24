## Scorecard — `discover-competitors-alt` Round 15

**Rubric version:** v15 (34 aspirational criteria, C-09–C-42; weight 0.294 pts each)
**Scoring date:** 2026-03-18

---

### Criteria evaluation — discriminating range (C-35–C-42)

All criteria C-01–C-34 are **PASS** across all five variations. The five variations differ only in the C-35–C-42 range and one dependency cascade. The analysis below focuses on the differential criteria; a batch note covers C-01–C-34.

**C-01–C-34 (all variations):** PASS — Essential (C-01–C-05) all satisfied; Recommended (C-06–C-08) all satisfied; Aspirational chain C-09–C-34 all satisfied. No variation introduces a lower-chain failure.

---

#### V-01 — C-40 Failure: Compact Yes-Cell (C-36 FAIL Cascade)

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-35 | **PASS** | Manifest column header uses `[TOKEN] propagation` bracket-notation syntax — substitution lifecycle participation active |
| C-36 | **FAIL** | Compact Yes-cell embeds propagation declaration inside the TOKEN commitment row's Yes-cell and includes an explicit manifest cross-reference. The two structural layers are not independently self-contained — consulting only GATE-0's REQUIRED OUTPUTS table reveals a pointer to the manifest rather than a closed declaration. Dependency for C-40, C-38, C-41 from C-36 side. |
| C-37 | **PASS** | C-33 (rubric-vocabulary cells), C-34 (pre-manifest architecture block), and C-35 (bracket-notation column header) are all simultaneously active with no delegation between them — triple-mechanism stack complete |
| C-38 | **FAIL** | Dep chain: C-38 requires C-36; C-36 FAIL → C-38 scored 0. Architecture block names both artifacts and uses verbatim vocabulary, but the C-36 prerequisite is absent — the structural independence the architecture block is supposed to prime is not achieved |
| C-39 | **PASS** | Architecture block uses "Declaration site" and "Substitution/inheritance site" verbatim. C-39 deps are C-34 and C-33 — neither requires C-36. Both dep criteria PASS independently |
| C-40 | **FAIL** | Dep: C-36 FAIL → C-40 scored 0. No dedicated propagation row — propagation declaration shares the TOKEN commitment row via the compact Yes-cell, making the two concerns inseparable at the table-row level |
| C-41 | **FAIL** | C-41 requires C-36 AND C-37 simultaneously. C-37 PASS but C-36 FAIL → conjunction fails. Triple-mechanism manifest hardening is structurally present but the underlying dual-layer independence guarantee is absent |
| C-42 | **FAIL** | Dep: C-42 requires C-38; C-38 scored 0 → C-42 scored 0. Architecture block prose satisfies the vocabulary and dual-target conditions, but the C-38 prerequisite failure propagates |

**Aspirational failures:** C-36, C-38, C-40, C-41, C-42 — **5 criteria**
**Aspirational pass count:** 29/34
**Composite:** 60 + 30 + (29 × 0.294) = **98.526**

---

#### V-02 — C-41 Failure: C-35 Dropped, C-37 Fails, C-42 Survives

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-35 | **FAIL** | Manifest column header uses static label `TOKEN propagation` — no bracket-notation syntax. Substitution lifecycle participation absent |
| C-36 | **PASS** | Dedicated propagation row present in GATE-0 REQUIRED OUTPUTS table. Consulting only the GATE-0 table: full propagation contract is self-contained. Consulting only the manifest column: full propagation contract is also self-contained. Neither layer cross-references or delegates to the other — dual-layer independence achieved |
| C-37 | **FAIL** | Triple-mechanism stack requires C-33+C-34+C-35 simultaneously. C-35 FAIL → stack incomplete. C-33 and C-34 both active but insufficient without C-35 |
| C-38 | **PASS** | Architecture block explicitly names both artifacts — the manifest TOKEN-propagation column and GATE-0's REQUIRED OUTPUTS table — as propagation contract targets. Deps C-36 (PASS) and C-34 (PASS) both satisfied. C-35 not in C-38's dep chain |
| C-39 | **PASS** | Architecture block uses "Declaration site" and "Substitution/inheritance site" verbatim. Deps C-34 (PASS) and C-33 (PASS). Neither requires C-35 |
| C-40 | **PASS** | Dedicated propagation row present; C-36 PASS → C-40 dep satisfied. Propagation declaration occupies a structurally distinct row with its own row header, separable from the TOKEN commitment row by row selection alone |
| C-41 | **FAIL** | C-41 requires C-37 AND C-36 simultaneously. C-36 PASS but C-37 FAIL → conjunction fails. Dep gate: C-37 is C-41's stated prerequisite; C-37 fails |
| C-42 | **PASS** | C-42 requires C-38 AND C-39 simultaneously. Both PASS independently. C-38 and C-39 dep chains do not include C-35 or C-37 → C-42 survives the C-35 failure |

**Aspirational failures:** C-35, C-37, C-41 — **3 criteria**
**Aspirational pass count:** 31/34
**Composite:** 60 + 30 + (31 × 0.294) = **99.114**

---

#### V-03 — C-42 Failure: C-39 FAIL (Synonyms in Architecture Block)

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-35 | **PASS** | Manifest column header uses `[TOKEN] propagation` bracket-notation |
| C-36 | **PASS** | Dedicated propagation row; both layers independently self-contained |
| C-37 | **PASS** | C-33+C-34+C-35 all simultaneously active |
| C-38 | **PASS** | Architecture block explicitly names both artifacts as targets |
| C-39 | **FAIL** | Architecture block uses synonyms — "declaring gate" and "consuming gates" — instead of the verbatim rubric-vocabulary terms "Declaration site" and "Substitution/inheritance site." A reader cannot match block prose to manifest column cells without a translation step. C-39 operative test fails: the same vocabulary scan that confirms C-33 does NOT apply identically to the block |
| C-40 | **PASS** | Dedicated propagation row; C-36 PASS |
| C-41 | **PASS** | C-36 PASS and C-37 PASS simultaneously — full independence-and-hardening conjunction satisfied |
| C-42 | **FAIL** | C-42 requires C-38 AND C-39 simultaneously. C-38 PASS but C-39 FAIL → conjunction fails. Architecture block names both artifacts but uses synonym vocabulary — dual-target coverage without vocabulary co-registration |

**Aspirational failures:** C-39, C-42 — **2 criteria**
**Aspirational pass count:** 32/34
**Composite:** 60 + 30 + (32 × 0.294) = **99.408**

---

#### V-04 — Full 34/34: Prose Architecture Block

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-35 | **PASS** | Bracket-notation manifest column header |
| C-36 | **PASS** | Dedicated propagation row; dual-layer independence satisfied |
| C-37 | **PASS** | Triple-mechanism stack complete |
| C-38 | **PASS** | Architecture block prose explicitly names "the manifest TOKEN-propagation column" and "GATE-0's REQUIRED OUTPUTS table" as the two targets of the propagation contract |
| C-39 | **PASS** | Architecture block uses "Declaration site" and "Substitution/inheritance site" verbatim in the same prose describing those named targets — vocabulary co-registration with manifest column cells achieved |
| C-40 | **PASS** | Dedicated propagation row present; C-36 PASS |
| C-41 | **PASS** | C-36 PASS + C-37 PASS simultaneously |
| C-42 | **PASS** | C-38 PASS + C-39 PASS simultaneously. Single prose paragraph satisfies dual-target naming and verbatim vocabulary in one artifact — operative test: all four elements (two artifact names, two verbatim phrases) readable from the architecture block without consulting any other artifact |

**Aspirational failures:** none — **34/34**
**Composite:** 60 + 30 + (34 × 0.294) = **99.996 ≈ 100.000**

---

#### V-05 — Full 34/34: Structured 4-Element Checklist Architecture Block

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-35 | **PASS** | Bracket-notation manifest column header |
| C-36 | **PASS** | Dedicated propagation row; dual-layer independence satisfied |
| C-37 | **PASS** | Triple-mechanism stack complete |
| C-38 | **PASS** | Checklist enumerates both structural artifacts by name as explicit checklist items — "Named target 1: manifest TOKEN-propagation column" and "Named target 2: GATE-0 REQUIRED OUTPUTS table" make the dual-priming structurally explicit |
| C-39 | **PASS** | Checklist enumerates verbatim phrases as explicit labeled items — "Verbatim phrase 1: Declaration site" and "Verbatim phrase 2: Substitution/inheritance site" — co-registering with manifest column cells. C-39 operative test: the vocabulary scan finds the exact terms as explicit checklist labels, zero inference required |
| C-40 | **PASS** | Dedicated propagation row; C-36 PASS |
| C-41 | **PASS** | C-36 PASS + C-37 PASS simultaneously |
| C-42 | **PASS** | All four C-42 operative-test elements enumerated as explicit checklist items: two named artifact targets (C-38) + two verbatim phrases (C-39). Architecture block is self-auditing — a reader can verify C-42 compliance by running the operative test against the checklist labels directly |

**Aspirational failures:** none — **34/34**
**Composite:** 60 + 30 + (34 × 0.294) = **99.996 ≈ 100.000**

---

### Composite Score Summary

| Rank | Variation | Asp pass | Composite | Differentiator |
|------|-----------|----------|-----------|----------------|
| 1 (tie) | V-04 | 34/34 | **100.000** | Prose paragraph achieves C-42 — minimal viable dual-primer form |
| 1 (tie) | V-05 | 34/34 | **100.000** | 4-element checklist achieves C-42 — self-auditing architecture block |
| 3 | V-03 | 32/34 | **99.408** | C-39 fails (synonym vocabulary); C-42 collapses |
| 4 | V-02 | 31/34 | **99.114** | C-35 fails (static header); C-37 collapses; C-41 collapses; C-42 survives |
| 5 | V-01 | 29/34 | **98.526** | C-36 fails (compact Yes-cell); 5-criterion cascade (C-36, C-38, C-40, C-41, C-42) |

---

### Decisive Questions — Verdict

**Q1 — V-01 vs V-02 gap:** V-01 loses 5 aspirational criteria; V-02 loses 3. Gap = 2 × 0.294 = 0.588 pts. Composite gap: 99.114 − 98.526 = **0.588**. ✓ Confirmed — C-36's cascade (blocking C-38, C-40, C-41, C-42) is larger than C-35's cascade (blocking C-37, C-41 only). The compact Yes-cell is the structurally costlier failure.

**Q2 — V-02 vs V-03:** V-02 = 31/34 (C-35, C-37, C-41 fail; C-42 survives). V-03 = 32/34 (C-39, C-42 fail; C-41 survives). Gap = 1 × 0.294 = 0.294 pts. Composite: 99.408 − 99.114 = **0.294**. ✓ Confirmed — C-41 and C-42 are genuinely independent contributions: V-02 loses C-41 (not C-42); V-03 loses C-42 (not C-41). Clean 1-criterion separation validates the dep-graph claim.

**Q3 — V-04 vs V-05:** Equivalent at 34/34 and 100.000. No compliance advantage or regression from the explicit checklist form. Both forms achieve C-42 — prose paragraph via unified delivery; checklist via explicit operative-test enumeration. The checklist creates a structural self-audit property not measurable by this rubric but visible as a reliability signal for future rubric extension.

---

### Excellence Signals — V-04 and V-05

1. **Minimal dual-primer form (V-04):** A single prose paragraph that names both structural artifacts AND uses both verbatim phrases satisfies C-42 without requiring additional structure. The critical insight is that C-38 and C-39 are simultaneously closeable in one artifact — they require neither separate blocks nor separate sentences.

2. **Self-auditing architecture block (V-05):** Structuring the architecture block as a 4-element operative-test checklist (two named targets + two verbatim phrases) makes the block a pre-executed answer to the C-42 operative test. A scorer can verify compliance by running the test against checklist labels directly. This eliminates the translation step that fails C-39 in V-03 (synonyms force inference) and V-01 (C-36 failure means the architecture block's correct vocabulary is structurally stranded).

3. **Vocabulary co-registration as the decisive C-42 mechanism:** V-03 demonstrates that dual-target naming alone (C-38) is insufficient without verbatim vocabulary (C-39). The architecture block must close both loops — naming the artifacts AND using the exact terms — in a single artifact. V-03's synonym failure ("declaring gate"/"consuming gates") is unambiguously the single remaining gap once C-40 and C-41 are achieved.

4. **C-36 as the highest-leverage single failure:** V-01 demonstrates that one compact Yes-cell cascades to five criterion failures (C-36, C-38, C-40, C-41, C-42). C-36's independence test is the widest-consequence criterion in the rubric — its failure simultaneously blocks both the C-40 (structural mechanism) and C-41 (conjunction) axes, and collapses C-38 and C-42 via the architecture block chain.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Dual-target naming and verbatim vocabulary co-registration in a single architecture block prose paragraph satisfies C-42 as the minimal viable form — no additional structure required beyond one paragraph naming both artifacts with rubric-exact terms", "4-element operative-test checklist architecture block makes C-42 self-auditing: enumerating named-target-1, named-target-2, verbatim-phrase-1, verbatim-phrase-2 as explicit checklist labels turns the block into a pre-executed C-42 operative test answer", "C-36 compact Yes-cell failure cascades to 5 aspirational criteria simultaneously (C-36, C-38, C-40, C-41, C-42), making it the highest-leverage single structural failure in the rubric — the dedicated propagation row pattern is essential to prevent this cascade"]}
```
