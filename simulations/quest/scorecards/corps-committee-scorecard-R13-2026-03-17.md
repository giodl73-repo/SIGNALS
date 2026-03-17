## corps-committee — Quest Score R13

### Rubric version: v13 | Variations: V-01 through V-05

---

### Scoring Methodology

**Composite formula:** 60% Essential (C-01–C-05) + 30% Recommended (C-06–C-08) + 10% Aspirational (31-criterion denominator)

**Aspirational weight per criterion:** 10 ÷ 31 ≈ 0.323 pts each

**Baseline assumption:** R12 V-05 baseline criteria (C-16–C-33, 18 criteria) inherited as PASS for all variations.

---

### Per-Criterion Scores

#### Essential (C-01–C-05) — Same across all variations

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|-----------|------|------|------|------|------|-------|
| C-01 | Committee type correctly instantiated | PASS | PASS | PASS | PASS | PASS | BEFORE YOU START block enforces ROB/shiproom/arch-board imperatives with natural-language fail conditions in all five variations |
| C-02 | Each participant speaks from role | PASS | PASS | PASS | PASS | PASS | Sequential tier gate present in all; ROLE VOICE GUARD adds Mech 2 in V-01/V-04/V-05 — but single-mechanism still passes the essential bar |
| C-03 | Decisions explicitly recorded | PASS | PASS | PASS | PASS | PASS | DECISIONS table in Phase 5 with Verdict field and labeled outcome in all variations |
| C-04 | Action items captured with owners | PASS | PASS | PASS | PASS | PASS | ACTION ITEMS table with Owner Role column and FAILS enforcement in all; OWNERSHIP TALLY adds count verification in V-01/V-04/V-05 |
| C-05 | Dissenting opinion represented | PASS | PASS | PASS | PASS | PASS | DISSENTING OPINIONS table with FAILS for missing dissent rows in all variations |

**Essential score: 5/5 = 60.0 pts for all variations**

---

#### Recommended (C-06–C-08) — Same across all variations

| ID | Criterion | All | Notes |
|----|-----------|-----|-------|
| C-06 | Formal meeting structure | PASS | Phase 5 produces DECISIONS + ACTION ITEMS + DISSENTING OPINIONS in all |
| C-07 | Discussion depth reflects committee type | PASS | Tier structure enforces role-specific challenge depth; BEFORE YOU START anchors type-specific evidence requirements |
| C-08 | AMEND capability honored | PASS | AMEND ROUTING TABLE + RECOMMIT MANIFEST with delta tracking present in all five; V-01/V-05 include AMEND-AFFECTED SITES enumeration |

**Recommended score: 3/3 = 30.0 pts for all variations**

---

#### Aspirational (C-09–C-15, C-34–C-39) — Differentiated

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|-----------|------|------|------|------|------|-------|
| C-09 | Pre-mortem risk | PASS | PASS | PASS | PASS | PASS | GATE-1 requires INERTIA-FINDING-D to surface non-obvious cost; loop until YES |
| C-10 | Charter fidelity traceable | PASS | PASS | PASS | PASS | PASS | Charter Source field, quorum in Phase 0, SORT-CHECK for scope |
| C-11 | Injection treated as default | PASS | PASS | PASS | PASS | PASS | INERTIA CONTINUITY BRIDGE with injection enforcement and FAILS (C-49) for incorrect YES |
| C-12 | Provisional annotation in Phase 0 | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL | Injection decided post-Phase 2 (not pending at Phase 0); no forward-reference annotation in participant table — criterion is neither vacuously satisfied nor fully met |
| C-13 | Pre-skeleton imperative block | PASS | PASS | PASS | PASS | PASS | BEFORE YOU START present in all before skeleton; per-type imperatives + natural-language fail conditions |
| C-14 | FAILS entries annotated with criterion ID | PASS | PASS | PASS | PASS | PASS | V-01/V-03 reference C-NN at end of entry (sufficient for C-14); V-02/V-04/V-05 use canonical positional form |
| C-15 | Phase-gate with charter constraints as entry conditions | PASS | PASS | PASS | PASS | PASS | PHASE-N-ENTER preconditions in all; committee type/quorum committed in Phase 0 before simulation |
| C-34 | Re-COMMIT cycle after AMEND | PASS | PASS | PASS | PASS | PASS | RECOMMIT MANIFEST with version increment, delta list, and downstream gate requirement in all |
| C-35 | COMMIT seal token manifest | PASS | PASS | PASS | PASS | PASS | PHASE-0-COMMIT and PHASE-1-COMMIT enumerate explicit closed sets with named tokens and N= count |
| C-36 | Three-way CONFIRMATION status | PASS | PASS | PASS | PASS | PASS | TOKEN TRACE CONFIRMATION table with CONSUMED/NOT-APPLICABLE/DROPPED vocabulary and CONFIRMATION INVARIANT row count check |
| **C-37** | **Dual-enforcement for C-02 and C-04** | **PASS** | **FAIL** | **FAIL** | **PASS** | **PASS** | V-01/V-04/V-05: ROLE VOICE GUARD (domain-scope Mech 2) + tier gate (ordering Mech 1) for C-02; OWNERSHIP TALLY (count Mech 2) + Owner column (cell Mech 1) for C-04. V-02/V-03: only single mechanism for each |
| **C-38** | **FAILS syntax template enforces `[C-NN]`** | **FAIL** | **PASS** | **FAIL** | **PASS** | **PASS** | V-02/V-04/V-05: canonical template block declared before fill rules; states missing [C-NN] is "syntactically malformed"; shows correct vs MALFORMED examples; all fill-rule FAILS use positional form. V-01/V-03: use "FAILS: [desc] -- C-NN" (C-NN at end, not positional; no template declared) |
| **C-39** | **Co-dependent criteria with `REQUIRES:` annotations** | **FAIL** | **FAIL** | **PASS** | **FAIL** | **PASS** | V-03: CO-DEPENDENCY PREAMBLE table + `REQUIRES: C-35` in skeleton at PHASE-2-ENTER and before TOKEN TRACE fill rules + `REQUIRES: [TIER SORT complete]` before bridge fill rule. V-05: same plus PHASE-1-COMMIT inline note + halt condition at PHASE-2-ENTER + `FAILS [C-39]:` self-referential entry. V-01/V-02/V-04: no REQUIRES: annotations |
| Baseline C-16–C-33 | (18 criteria, all inherited) | PASS×18 | PASS×18 | PASS×18 | PASS×18 | PASS×18 | |

---

### Composite Score Computation

**Aspirational denominator: 31**

| Variation | Aspirational pts (×0.323 each) | Aspirational score /10 | Composite |
|-----------|-------------------------------|------------------------|-----------|
| V-01 | C-37✓ C-38✗ C-39✗ + 9 PASS + 0.5 + 18 baseline = 28.5/31 | 9.19 | **99.2** |
| V-02 | C-37✗ C-38✓ C-39✗ + 9 PASS + 0.5 + 18 baseline = 28.5/31 | 9.19 | **99.2** |
| V-03 | C-37✗ C-38✗ C-39✓ + 9 PASS + 0.5 + 18 baseline = 28.5/31 | 9.19 | **99.2** |
| V-04 | C-37✓ C-38✓ C-39✗ + 9 PASS + 0.5 + 18 baseline = 29.5/31 | 9.52 | **99.5** |
| V-05 | C-37✓ C-38✓ C-39✓ + 9 PASS + 0.5 + 18 baseline = 30.5/31 | 9.84 | **99.8** |

---

### Rankings

| Rank | Variation | Score | New criteria | Gap vs next |
|------|-----------|-------|-------------|-------------|
| 1 | **V-05** | 99.8 | C-37 + C-38 + C-39 | +0.3 |
| 2 | **V-04** | 99.5 | C-37 + C-38 | +0.3 |
| 3 (tie) | **V-01** | 99.2 | C-37 only | — |
| 3 (tie) | **V-02** | 99.2 | C-38 only | — |
| 3 (tie) | **V-03** | 99.2 | C-39 only | — |

The three-way tie at 99.2 is structurally correct: each single-axis variation adds exactly one of three equally-weighted aspirational criteria.

---

### Excellence Signals from V-05

**E-01: Self-referential FAILS entries in the FAILS template block**
V-05's FAILS SYNTAX TEMPLATE includes `CORRECT: FAILS [C-38]: FAILS entry missing [C-NN]` and `CORRECT: FAILS [C-39]: REQUIRES: C-35 absent`. The template teaches itself: a reviewer learning the form also learns exactly what to cite if it's violated. This makes the template self-documenting in a way V-02 and V-04 don't achieve.

**E-02: Dependency declared at the source, not only at the consumption site**
V-05's PHASE-1-COMMIT includes an inline note: `[This explicit closed set is the prerequisite for C-36 TOKEN TRACE CONFIRMATION row count = 4]`. V-03 and V-05 both declare REQUIRES: at the consumption site (TOKEN TRACE CONFIRMATION); only V-05 also annotates the source (PHASE-1-COMMIT) as the prerequisite. This closes the gap where a reviewer might pass C-35 at the source without realizing the dependency flows downstream.

**E-03: BEFORE YOU START escalates C-37 to orientation-level guidance**
V-05 adds `TWO-MECHANISM CHECK: role voice violations are caught by ROLE VOICE GUARD (domain mismatch) AND by TIER-N-SEQUENCE-COMMIT (ordering enforcement). Both must be satisfied.` in the BEFORE YOU START block. This converts C-37's structural requirement from an aspirational audit item into a simulation orientation constraint — the reviewer is primed to check both mechanisms before the simulation begins, not only during fill-rule review.

**E-04: Phase entry halt conditions for each new mechanism**
V-05's PHASE-2-ENTER includes an explicit halt condition: `C-35 pre-check: PHASE-1-COMMIT Sealed tokens enumerated as explicit closed set? [YES / NO] / If NO: halt`. V-03 has the REQUIRES: annotation but no halt gating. V-05 converts the dependency declaration into a blocking gate — unenforceability produces a halt, not just a reviewer flag.

---

### C-12 Gap (uniform across all)

All variations remain PARTIAL on C-12 (provisional participant annotation in Phase 0 when injection is pending). The INERTIA CONTINUITY BRIDGE pattern determines injection post-Phase 2 based on TIER SORT results — this means at Phase 0 there is no "pending injection" to annotate. Either the criterion is vacuously satisfied by this design, or the skill needs a Phase 0 forward-reference mechanism for the Inertia-Advocate slot. This structural ambiguity is inherited from the baseline and not addressed by any R13 variation.

---

```json
{"top_score": 99, "all_essential_pass": true, "new_patterns": ["self-referential FAILS entries in syntax template make the canonical form teach itself — template includes examples that cite C-38 and C-39 for their own violations", "declare co-dependencies at both source and consumption sites — PHASE-1-COMMIT annotates it is the C-35 prerequisite; TOKEN TRACE CONFIRMATION declares REQUIRES: C-35; closure at both ends eliminates the unidirectional gap", "phase entry halt conditions convert REQUIRES: annotations from reviewer flags into structural blocking gates — unenforceability produces halt, not just advisory warning"]}
```
