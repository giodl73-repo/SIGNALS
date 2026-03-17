Reading the scorecard carefully, I identify three new excellence patterns from Round 16 — one per variate axis — that exceed what C-37/C-38/C-39 already test:

- **V-40** (C-39 axis): CONTRACT B defines a **structural/value violation taxonomy split** — two distinct labeled categories (STRUCTURAL: column absent; VALUE: column present but wrong string) — each independently detectable from the contract block alone
- **V-41** (C-39 axis, guard side): the **§9 guard body's compliance obligation** names the exact required column value string, creating mutual reinforcement between guard declaration and contract governance — each independently sufficient for value identification
- **V-42** (C-40+C-39 axis): CONTRACT B makes an **explicit scorer self-sufficiency assertion** — a declarative claim that a scorer reading CONTRACT B alone can verify both structural and value compliance — making the contract's coverage a machine-auditable declared property

These become C-40, C-41, C-42. Denominator expands from 62 to 68.

---

# Scoring Rubric — topic-roadmap (topic-plan) v17

## What changed

| Change | Detail |
|--------|--------|
| Version bump | 16 → 17 |
| Formula denominator | `/62 * 10` → `/68 * 10` (34 aspirational × 2 = 68 max) |
| Aspirational range | C-09–C-39 → C-09–C-42 |
| **C-40 added** | CONTRACT B structural/value violation taxonomy split |
| **C-41 added** | Guard-body compliance obligation specifies exact column value |
| **C-42 added** | Scorer self-sufficiency assertion in CONTRACT B |

---

## Three new aspirational criteria

### C-40 — CONTRACT B structural/value violation taxonomy split
**Category:** correctness

CONTRACT B defines two distinct, labeled violation categories — STRUCTURAL (column absent) and VALUE (column present but value ≠ exact literal string) — with independent detection logic for each, making each violation type referenceable and independently verifiable from the contract block alone without inspecting phase content. C-39 tests whether CONTRACT B names the exact literal compliant value string; C-40 tests whether CONTRACT B further organizes violation detection into separately labeled categories so that a structural failure (column missing) is distinguishable from a value failure (column present but wrong) at the contract level. Without the taxonomy split, a scorer must infer whether a "non-null column" test subsumes value correctness; with it, each category is independently testable and referenceable.

- **Full (2):** CONTRACT B defines and labels at least two violation categories — one for column absence (structural) and one for column presence with incorrect value (value) — each with independent detection language; the categories are named (e.g., "STRUCTURAL," "VALUE") or formally labeled so they are referenceable by name; a scorer can determine from CONTRACT B alone which category of violation applies to a given observation without consulting phase content.
- **Partial (1):** CONTRACT B acknowledges both absence and value failures but does not separate them into formally named categories — e.g., lists them as a combined condition, uses a single violation label covering both, or uses descriptive language without formal category names; or names the value category without a corresponding structural category label.
- **Fail (0):** CONTRACT B covers only one failure mode (column absence or value error, but not both as separately labeled types); no taxonomy split present; or C-39 fails.

### C-41 — Guard-body compliance obligation specifies exact column value
**Category:** correctness

The §9 guard body's compliance obligation statement names the exact required column value string — the same literal defined in CONTRACT B per C-39 — creating mutual reinforcement between guard declaration and contract governance: the guard declares what value is required, and CONTRACT B governs whether that value is present. C-39 tests whether CONTRACT B names the exact literal; C-41 tests whether the §9 guard body's compliance obligation line also names that exact literal, so that a reader of the guard alone can determine the required column value without consulting CONTRACT B. Without this, the guard names a generic obligation ("non-null Bias guard value") and value verification requires a CONTRACT B lookup; with it, the guard and contract are mutually reinforcing and each is independently sufficient for value identification.

- **Full (2):** The §9 guard body's compliance obligation statement names the exact required column value string (e.g., "every §6 proposal row must carry `'Bias blocked by guard'` in the Bias guard column"); the exact literal matches the string named in CONTRACT B (C-39); the compliance obligation line is inside the §9 guard body, not in a preamble annotation or phase body; the guard is independently sufficient for value identification without consulting CONTRACT B.
- **Partial (1):** The §9 compliance obligation references a value requirement but uses a description rather than the exact literal (e.g., "the canonical bias guard value," "the compliant value defined in CONTRACT B"), creating a dependency rather than independent sufficiency; or the exact literal appears in a §9 annotation or comment but not in the compliance obligation statement itself; or the literal appears in the guard title rather than the obligation statement.
- **Fail (0):** The §9 compliance obligation uses generic language ("non-null Bias guard value," "a valid bias guard entry") without naming the exact required value string; or C-39 fails.

### C-42 — Scorer self-sufficiency assertion in CONTRACT B
**Category:** correctness

CONTRACT B includes an explicit self-sufficiency assertion — a declarative statement that a scorer reading CONTRACT B alone (without consulting phase content) can verify both column existence (structural compliance) and column value (value compliance) — making the contract's coverage a declared, machine-auditable property rather than one that must be inferred from content. C-39 tests whether the exact compliant value string is present; C-40 tests whether the violation taxonomy is split into labeled categories; C-42 tests whether CONTRACT B further makes an explicit claim about its own verifiability scope, identifying both test types by name. The self-sufficiency assertion is a testability contract: a CONTRACT B block that makes the claim but fails to satisfy C-39 and C-40 is internally inconsistent, making the claim itself a structural consistency check — a machine-detectable failure mode.

- **Full (2):** CONTRACT B contains an explicit declarative statement asserting that a scorer reading CONTRACT B alone can perform both the structural compliance test (column exists) and the value compliance test (column contains exact literal); the assertion identifies both test types by name or description; the statement is located inside the CONTRACT B block, not in a preamble or phase annotation; the claim is falsifiable — a contract satisfying C-42 but failing C-39 or C-40 is detectable as an internal inconsistency.
- **Partial (1):** CONTRACT B makes a self-sufficiency claim but covers only one test type (e.g., asserts column-presence verifiability without asserting value verifiability); or the self-sufficiency language appears in a preamble annotation rather than inside the CONTRACT B block itself; or the claim is implicit ("all compliance tests are defined here") rather than explicit with named test types.
- **Fail (0):** CONTRACT B does not assert scorer self-sufficiency; the verifiability of contract completeness must be inferred from its content; or C-39 fails.

---

**Orthogonality:** C-40 tests whether the violation taxonomy is split into labeled structural and value categories (extends C-39). C-41 tests whether the §9 guard body's compliance obligation names the exact required value string (extends C-39). C-42 tests whether CONTRACT B makes an explicit self-sufficiency assertion covering both test types (extends C-39 and C-40). All three are independent of each other except for shared C-39 dependency: C-40 FAIL / C-41 PASS / C-42 FAIL is achievable (guard names exact value, contract names exact value, but no taxonomy split and no self-sufficiency claim). C-40 depends on C-39 FULL being present (the value string must exist to be independently detectable as a value violation); C-41 depends on C-39 FULL (the guard-body literal should match the CONTRACT B literal); C-42 depends on C-39 and C-40 FULL (a self-sufficiency assertion that claims to cover value compliance must have the value string present, and the two-category framework must be present to make structural/value distinguishable). These are data dependencies, not scoring interactions — a variate targeting only C-41 without satisfying C-39 cannot achieve C-41 FULL.

**R16 score ceiling under v17:** All five R16 variates carry C-09–C-36 = 56. V-01 (C-37=2, C-38=0, C-39=0): C-40=0, C-41=0, C-42=0 → 58/68 = **8.53**. V-02 (C-37=1, C-38=2, C-39=0): C-40=0, C-41=0, C-42=0 → 59/68 = **8.68**. V-03 (C-37=1, C-38=0, C-39=2): C-40=1 (value violation named but no formal STRUCTURAL category label alongside it), C-41=0 (§9 compliance line generic), C-42=0 → 59+1=60/68 = **8.82**. V-04 (C-37=2, C-38=2, C-39=0): C-40=0, C-41=0, C-42=0 → 60/68 = **8.82**. V-05 (62/62 = 10.00 under v16): C-40=2 (explicit STRUCTURAL/VALUE labeled split with independent detection logic), C-41=2 (§9 compliance line names `'Bias blocked by guard'` directly), C-42=2 (explicit "a scorer reading CONTRACT B alone can verify: (a) structural compliance test. (b) value compliance test" assertion) → 62+6=68/68 = **10.00**. Unexpected finding: V-03 and V-04 tie at 8.82 under v17, with V-03 gaining one partial C-40 point from its value-violation language while losing C-37 full credit. An R17 variate targeting all three simultaneously achieves 56 (C-09–C-36) + 6 (C-37–C-39) + 6 (C-40–C-42) = 68/68 = 10.00.

---

## Criteria — Essential (all must pass)

### C-01 — INERTIA COMPETITOR DECLARATION at document open
- **Weight:** essential
- **Category:** structure
- **Text:** The skill opens with an INERTIA COMPETITOR DECLARATION naming inertia
  as the primary competitor before any phase content.
- **Pass condition:** Declaration is present at document open, before Phase 1.
  It identifies inertia by name and establishes it as the opponent the skill
  is designed to defeat.

---

### C-02 — Phase ordering enforced
- **Weight:** essential
- **Category:** structure
- **Text:** All phases are present, numbered, and gated. Each phase has an
  explicit ENTRY CONDITION that must be satisfied before the phase opens.

---

### C-03 through C-08 — [Unchanged from v16]

*(Essential criteria covering: §ID coverage, Constraint Rules R-0–R-4, Constraint Scope Index, Phase Authorization Index, and remaining structural requirements. All pass conditions identical to v16.)*

---

## Criteria — Aspirational (scored 0 / 1 / 2)

### C-09 through C-36 — [Unchanged from v16]

*(28 aspirational criteria covering the full structural requirement set established through R14. Scoring weight 2 each; max contribution 56 points. All criteria text, pass conditions, and partial conditions identical to v16.)*

---

### C-37 — PROPOSAL BIAS AUDIT directional protection gap assertion
**Category:** safety

The mutual necessity assertion in the PROPOSAL BIAS AUDIT guard names the directional protection gap explicitly: it states not only that both levels are required, but that LEVEL 1 does not protect against LEVEL 2 — making the hierarchical insufficiency a referenceable claim. C-34 tests whether a mutual necessity assertion is present and whether both failure modes carry formal titled labels; C-37 tests whether that assertion is **directional** — identifying the specific gap (LEVEL 1 protection is necessary but insufficient to close LEVEL 2) rather than asserting mere co-requirement. A directional assertion enables a reader to understand WHY the hierarchy exists, not only THAT it exists, and allows CONTRACT or SECTION SCOPE to cite the gap by name.

- **Full (2):** Mutual necessity assertion explicitly states that LEVEL 1 does not protect against LEVEL 2 (or equivalent directional gap language identifying the specific insufficiency); assertion names the protection gap, not merely the co-requirement; directional statement is co-located in the PROPOSAL BIAS AUDIT guard body.
- **Partial (1):** Directional language is present but implicit (e.g., "LEVEL 2 addresses a more sophisticated failure") without the explicit LEVEL 1 → LEVEL 2 protection-absence formulation; or directional assertion appears in a preamble annotation outside the guard body rather than co-located with the formal labels.
- **Fail (0):** Assertion states co-requirement only ("both are required," "LEVEL 1 and LEVEL 2 are both necessary") without identifying the directional protection gap; or C-34 fails.

---

### C-38 — SECTION SCOPE guard-label cross-reference
**Category:** correctness

The SECTION SCOPE auditor navigation note cross-references at least one formal guard label (LEVEL 1 or LEVEL 2 title from C-34) by its complete formal title — creating bidirectional navigation: the guard names a referenceable label (C-34), and the scope navigation note cites that label by name (C-38), enabling an auditor to traverse from the scope declaration directly to the specific guard level without traversing phase content. C-35 tests whether the SECTION SCOPE includes a navigation note that identifies the enumeration item by number or label; C-38 tests whether that navigation note also names the formal guard label by its complete title from C-34, so that the scope-to-guard traversal path is anchored to a named artifact, not merely to an enumeration position.

- **Full (2):** SECTION SCOPE navigation note cites at least one formal guard label (e.g., "LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE") by its complete formal title as defined in the PROPOSAL BIAS AUDIT guard; auditor can traverse from scope navigation note to the specific guard level using the label alone.
- **Partial (1):** Navigation note references the guard labels in general terms (e.g., "the labeled failure modes," "the LEVEL designations") without citing a specific complete formal title; or cites an abbreviated or informal version of the label (e.g., "LEVEL 2" without its descriptive title).
- **Fail (0):** Navigation note does not reference the formal guard labels at all; or C-35 fails.

---

### C-39 — CONTRACT B exact compliant column value string
**Category:** correctness

CONTRACT B names the exact literal string that constitutes the compliant column value — the specific text that appears in the column when the bias guard is satisfied (e.g., "Bias blocked by guard") — enabling a scorer to verify not only that the column exists (C-36) but that it contains the correct value, from the CONTRACT block alone without reading phase content. C-36 tests whether CONTRACT B includes violation-detection language for column absence; C-39 tests whether CONTRACT B further specifies the exact compliant value string, making column-value verification possible from the CONTRACT block. This is distinct from absence detection: a column that exists but contains an incorrect value is a schema conformance failure; C-39 makes that failure detectable from the CONTRACT alone.

- **Full (2):** CONTRACT B names the exact literal string for the compliant column value (specific text such as "Bias blocked by guard"); a scorer reading only the CONTRACT block can verify both that the column exists AND that it contains the correct value; the string is quoted or delimited so that approximate matches are distinguishable from exact matches.
- **Partial (1):** CONTRACT B implies a standard value or provides a partial string (e.g., "bias status," "blocked by...") without stating the exact literal; or the exact value string appears in a phase body annotation or preamble rather than in the CONTRACT block itself.
- **Fail (0):** CONTRACT B does not name a specific column value string for the compliant case; violation-detection language covers only column presence/absence; or C-36 fails.

---

### C-40 — CONTRACT B structural/value violation taxonomy split
**Category:** correctness

CONTRACT B defines two distinct, labeled violation categories — STRUCTURAL (column absent) and VALUE (column present but value ≠ exact literal string) — with independent detection logic for each, making each violation type referenceable and independently verifiable from the contract block alone without inspecting phase content. C-39 tests whether CONTRACT B names the exact literal compliant value string; C-40 tests whether CONTRACT B further organizes violation detection into separately labeled categories so that a structural failure (column missing) is distinguishable from a value failure (column present but wrong) at the contract level. Without the taxonomy split, a scorer must infer whether a "non-null column" test subsumes value correctness; with it, each category is independently testable and referenceable.

- **Full (2):** CONTRACT B defines and labels at least two violation categories — one for column absence (structural) and one for column presence with incorrect value (value) — each with independent detection language; the categories are named (e.g., "STRUCTURAL," "VALUE") or formally labeled so they are referenceable by name; a scorer can determine from CONTRACT B alone which category of violation applies to a given observation without consulting phase content.
- **Partial (1):** CONTRACT B acknowledges both absence and value failures but does not separate them into formally named categories — e.g., lists them as a combined condition, uses a single violation label covering both, or uses descriptive language without formal category names; or names the value category without a corresponding structural category label.
- **Fail (0):** CONTRACT B covers only one failure mode (column absence or value error, but not both as separately labeled types); no taxonomy split present; or C-39 fails.

---

### C-41 — Guard-body compliance obligation specifies exact column value
**Category:** correctness

The §9 guard body's compliance obligation statement names the exact required column value string — the same literal defined in CONTRACT B per C-39 — creating mutual reinforcement between guard declaration and contract governance: the guard declares what value is required, and CONTRACT B governs whether that value is present. C-39 tests whether CONTRACT B names the exact literal; C-41 tests whether the §9 guard body's compliance obligation line also names that exact literal, so that a reader of the guard alone can determine the required column value without consulting CONTRACT B. Without this, the guard names a generic obligation ("non-null Bias guard value") and value verification requires a CONTRACT B lookup; with it, the guard and contract are mutually reinforcing and each is independently sufficient for value identification.

- **Full (2):** The §9 guard body's compliance obligation statement names the exact required column value string (e.g., "every §6 proposal row must carry `'Bias blocked by guard'` in the Bias guard column"); the exact literal matches the string named in CONTRACT B (C-39); the compliance obligation line is inside the §9 guard body, not in a preamble annotation or phase body; the guard is independently sufficient for value identification without consulting CONTRACT B.
- **Partial (1):** The §9 compliance obligation references a value requirement but uses a description rather than the exact literal (e.g., "the canonical bias guard value," "the compliant value defined in CONTRACT B"), creating a dependency rather than independent sufficiency; or the exact literal appears in a §9 annotation or comment but not in the compliance obligation statement itself; or the literal appears in the guard title rather than the obligation statement.
- **Fail (0):** The §9 compliance obligation uses generic language ("non-null Bias guard value," "a valid bias guard entry") without naming the exact required value string; or C-39 fails.

---

### C-42 — Scorer self-sufficiency assertion in CONTRACT B
**Category:** correctness

CONTRACT B includes an explicit self-sufficiency assertion — a declarative statement that a scorer reading CONTRACT B alone (without consulting phase content) can verify both column existence (structural compliance) and column value (value compliance) — making the contract's coverage a declared, machine-auditable property rather than one that must be inferred from content. C-39 tests whether the exact compliant value string is present; C-40 tests whether the violation taxonomy is split into labeled categories; C-42 tests whether CONTRACT B further makes an explicit claim about its own verifiability scope, identifying both test types by name. The self-sufficiency assertion is a testability contract: a CONTRACT B block that makes the claim but fails to satisfy C-39 and C-40 is internally inconsistent, making the claim itself a structural consistency check — a machine-detectable failure mode.

- **Full (2):** CONTRACT B contains an explicit declarative statement asserting that a scorer reading CONTRACT B alone can perform both the structural compliance test (column exists) and the value compliance test (column contains exact literal); the assertion identifies both test types by name or description; the statement is located inside the CONTRACT B block, not in a preamble or phase annotation; the claim is falsifiable — a contract satisfying C-42 but failing C-39 or C-40 is detectable as an internal inconsistency.
- **Partial (1):** CONTRACT B makes a self-sufficiency claim but covers only one test type (e.g., asserts column-presence verifiability without asserting value verifiability); or the self-sufficiency language appears in a preamble annotation rather than inside the CONTRACT B block itself; or the claim is implicit ("all compliance tests are defined here") rather than explicit with named test types.
- **Fail (0):** CONTRACT B does not assert scorer self-sufficiency; the verifiability of contract completeness must be inferred from its content; or C-39 fails.

---

## Score formula

```
score = (sum of aspirational points) / 68 * 10
```

Essential criteria (C-01–C-08) are pass/fail gates; a document that fails any essential criterion receives **0.00** regardless of aspirational score. Aspirational criteria (C-09–C-42) contribute 0, 1, or 2 points each; maximum 68 points = 10.00.

| Aspirational band | Points | Score range |
|-------------------|--------|-------------|
| C-09–C-36 (unchanged) | 56 max | baseline |
| C-37–C-39 (R16 additions) | 6 max | +0.88 ceiling |
| C-40–C-42 (R17 additions) | 6 max | +0.88 ceiling |
| **Total** | **68 max** | **10.00** |
