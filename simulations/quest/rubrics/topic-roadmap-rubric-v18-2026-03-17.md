Reading the scorecard, I identify two excellence patterns from Round 17 where V-05 distinguishably exceeds V-04 despite both scoring 10.00 under v17:

- **V-43** (C-41 axis): The §9 compliance obligation not only names the exact literal but **explicitly declares CONTRACT B as the governing authority** — creating a bidirectional guard→contract pointer (guard cites contract as source), as opposed to C-41's mutual-reinforcement test where the guard is merely independently sufficient.
- **V-44** (C-42 axis): The self-sufficiency assertion **names its own structural prerequisites** (C-39 and C-40 equivalents) as internal consistency conditions — converting the assertion from a coverage claim into a self-auditing consistency contract, where internal incoherence is machine-detectable from the assertion text alone.

Denominator expands from 68 to 72 (36 aspirational × 2).

---

# Scoring Rubric — topic-roadmap (topic-plan) v18

## What changed

| Change | Detail |
|--------|--------|
| Version bump | 17 → 18 |
| Formula denominator | `/68 * 10` → `/72 * 10` (36 aspirational × 2 = 72 max) |
| Aspirational range | C-09–C-42 → C-09–C-44 |
| **C-43 added** | §9 guard body declares CONTRACT B as governing document (bidirectional pointer) |
| **C-44 added** | Self-sufficiency assertion names its own structural prerequisites |

---

## Two new aspirational criteria

### C-43 — §9 guard body declares CONTRACT B as governing document
**Category:** correctness

The §9 guard body's compliance obligation names the exact required column value string (satisfying C-41) and additionally declares CONTRACT B by name as the authoritative governing document for that value requirement — creating a bidirectional pointer: CONTRACT B declares the governed value; the guard's compliance obligation names that value and explicitly subordinates itself to CONTRACT B as source authority. C-41 tests whether the guard independently names the exact literal; C-43 tests whether the guard additionally cross-references CONTRACT B as governing authority, making the guard-contract relationship explicit and machine-traceable in both directions. Without C-43, guard and contract are mutually reinforcing but independently authored — a scorer verifying the guard sees the value but cannot, from the guard alone, identify the authoritative source. With C-43, the guard formally points to CONTRACT B, and a reader of §9 alone can identify where value governance lives.

- **Full (2):** The §9 guard body's compliance obligation statement names the exact required column value string (C-41 satisfied) AND explicitly names CONTRACT B — by its structural identifier or label — as the governing authority for that value requirement; the governing reference is located inside the §9 compliance obligation statement itself, not in a §9 preamble annotation, guard title, or separate parenthetical clause; a scorer reading the §9 guard body can trace the value requirement to CONTRACT B without consulting any section outside §9.
- **Partial (1):** The §9 compliance obligation names the exact literal (C-41 satisfied) but references CONTRACT B only outside the obligation statement — e.g., in a §9 preamble annotation, the guard title, or an inline parenthetical after the obligation — rather than within the obligation statement itself; or uses indirect language ("as defined in the governing contract," "per the contract authority") without naming CONTRACT B by its structural label.
- **Fail (0):** The §9 compliance obligation does not reference CONTRACT B as governing authority; the guard-to-contract relationship must be inferred; or C-41 fails.

---

### C-44 — Self-sufficiency assertion names its own structural prerequisites
**Category:** correctness

CONTRACT B's self-sufficiency assertion (C-42) explicitly names its own structural prerequisites — identifying the exact-value requirement (C-39 equivalent) and the taxonomy-split requirement (C-40 equivalent) as internal consistency conditions — making the assertion self-auditing: a CONTRACT B that makes the C-42 claim while failing C-39 or C-40 is detectable as internally inconsistent by reading the assertion text alone. C-42 tests whether the self-sufficiency assertion covers both test types by name; C-44 tests whether the assertion further declares those test types as prerequisites for its own validity, converting the assertion from a coverage claim into a structural consistency contract. Without C-44, a scorer must inspect CONTRACT B's content to determine whether the self-sufficiency claim is internally coherent; with C-44, the assertion declares its own failure conditions, making CONTRACT B a self-auditing artifact whose internal consistency is machine-verifiable without phase inspection.

- **Full (2):** CONTRACT B's self-sufficiency assertion explicitly names both structural prerequisites — the exact-value requirement (C-39 equivalent: exact literal present in CONTRACT B) and the taxonomy-split requirement (C-40 equivalent: structural and value violation categories formally labeled and split) — as conditions that must hold for the assertion to be valid; the prerequisites are named inside the assertion block or in a directly attached consistency clause that is part of the CONTRACT B block; a scorer can determine from the assertion text alone that failing either named prerequisite constitutes an internal inconsistency detectable without inspecting phase content; the claim is therefore stronger than C-42 because its falsifiability conditions are declared, not merely inferable.
- **Partial (1):** The self-sufficiency assertion includes a falsifiability clause but names only one structural prerequisite (value-presence or taxonomy-split, not both); or names both prerequisites but locates them in a separate annotation outside the CONTRACT B block rather than inside the assertion itself; or uses generic language ("this assertion requires contract completeness") without identifying the specific structural properties by type.
- **Fail (0):** CONTRACT B's self-sufficiency assertion does not name its own structural prerequisites; the internal consistency of the assertion must be inferred from content rather than declared; or C-42 fails.

---

**Orthogonality:** C-43 tests whether the §9 guard body cross-references CONTRACT B as governing authority (extends C-41). C-44 tests whether CONTRACT B's self-sufficiency assertion names its own structural prerequisites (extends C-42). C-43 and C-44 are independent of each other: a variate can satisfy C-43 without satisfying C-44 (guard cites CONTRACT B as governing, but assertion does not name prerequisites) and vice versa (assertion names prerequisites, but guard obligation does not cross-reference CONTRACT B). C-43 depends on C-41 FULL — the exact literal must be present in the guard for a governing reference to be meaningful; C-44 depends on C-42 FULL — a self-sufficiency assertion must exist in CONTRACT B before it can name its own prerequisites. These are data dependencies, not scoring interactions. A variate satisfying C-44 without C-42 cannot achieve C-44 FULL; a variate satisfying C-43 without C-41 cannot achieve C-43 FULL.

**R17 score ceiling under v18:** All five R17 variates carry C-09–C-36 = 56. V-01 (C-37=2, C-38=2, C-39=2, C-40=2, C-41=0, C-42=0): C-43=0 (C-41 fails; prerequisite unmet), C-44=0 (C-42 fails; prerequisite unmet) → 64/72 = **8.89**. V-02 (C-37=2, C-38=2, C-39=2, C-40=1, C-41=2, C-42=0): C-43=0 — the §9 obligation's "independently sufficient without consulting CONTRACT B" language references CONTRACT B in the context of independence, not as governing authority; governing reference is absent — C-43 FAIL; C-44=0 (C-42 fails) → 65/72 = **9.03**. V-03 (C-37=2, C-38=2, C-39=2, C-40=2, C-41=0, C-42=2): C-43=0 (C-41 fails), C-44=1 — the C-42 assertion carries a falsifiability clause naming both test types but names prerequisites generically ("structural compliance test," "value compliance test") rather than by structural property label (exact-value requirement, taxonomy-split requirement); PARTIAL → 66+1=67/72 = **9.31**. V-04 (C-37=2, C-38=2, C-39=2, C-40=2, C-41=2, C-42=2): C-43=0 — scorecard records "criteria satisfied independently — no cross-reference language between guard and contract"; governing reference absent — C-43 FAIL; C-44=0 — C-42 assertion covers both test types with falsifiability clause but does not name structural prerequisites by property type → 68/72 = **9.44**. V-05 (C-37=2, C-38=2, C-39=2, C-40=2, C-41=2, C-42=2): C-43=2 — §9 obligation names exact literal and explicitly declares CONTRACT B as governing document; bidirectional pointer present; C-44=2 — C-42 assertion names C-39 and C-40 as structural consistency dependencies, making internal inconsistency machine-detectable → 72/72 = **10.00**. Only V-05 achieves 10.00 under v18. V-04 drops to 9.44 despite full C-37–C-42, because neither the bidirectional governing reference nor the prerequisite-naming structure is present.

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

*[C-03 through C-08 — unchanged from v17]*

---

## Criteria — Aspirational (C-09 through C-44)

*[C-09 through C-39 — unchanged from v17]*

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

### C-43 — §9 guard body declares CONTRACT B as governing document
**Category:** correctness

The §9 guard body's compliance obligation names the exact required column value string (satisfying C-41) and additionally declares CONTRACT B by name as the authoritative governing document for that value requirement — creating a bidirectional pointer: CONTRACT B declares the governed value; the guard's compliance obligation names that value and explicitly subordinates itself to CONTRACT B as source authority. C-41 tests whether the guard independently names the exact literal; C-43 tests whether the guard additionally cross-references CONTRACT B as governing authority, making the guard-contract relationship explicit and machine-traceable in both directions. Without C-43, guard and contract are mutually reinforcing but independently authored — a scorer verifying the guard sees the value but cannot, from the guard alone, identify the authoritative source. With C-43, the guard formally points to CONTRACT B, and a reader of §9 alone can identify where value governance lives.

- **Full (2):** The §9 guard body's compliance obligation statement names the exact required column value string (C-41 satisfied) AND explicitly names CONTRACT B — by its structural identifier or label — as the governing authority for that value requirement; the governing reference is located inside the §9 compliance obligation statement itself, not in a §9 preamble annotation, guard title, or separate parenthetical clause; a scorer reading the §9 guard body can trace the value requirement to CONTRACT B without consulting any section outside §9.
- **Partial (1):** The §9 compliance obligation names the exact literal (C-41 satisfied) but references CONTRACT B only outside the obligation statement — e.g., in a §9 preamble annotation, the guard title, or an inline parenthetical after the obligation — rather than within the obligation statement itself; or uses indirect language ("as defined in the governing contract," "per the contract authority") without naming CONTRACT B by its structural label.
- **Fail (0):** The §9 compliance obligation does not reference CONTRACT B as governing authority; the guard-to-contract relationship must be inferred; or C-41 fails.

---

### C-44 — Self-sufficiency assertion names its own structural prerequisites
**Category:** correctness

CONTRACT B's self-sufficiency assertion (C-42) explicitly names its own structural prerequisites — identifying the exact-value requirement (C-39 equivalent) and the taxonomy-split requirement (C-40 equivalent) as internal consistency conditions — making the assertion self-auditing: a CONTRACT B that makes the C-42 claim while failing C-39 or C-40 is detectable as internally inconsistent by reading the assertion text alone. C-42 tests whether the self-sufficiency assertion covers both test types by name; C-44 tests whether the assertion further declares those test types as prerequisites for its own validity, converting the assertion from a coverage claim into a structural consistency contract. Without C-44, a scorer must inspect CONTRACT B's content to determine whether the self-sufficiency claim is internally coherent; with C-44, the assertion declares its own failure conditions, making CONTRACT B a self-auditing artifact whose internal consistency is machine-verifiable without phase inspection.

- **Full (2):** CONTRACT B's self-sufficiency assertion explicitly names both structural prerequisites — the exact-value requirement (C-39 equivalent: exact literal present in CONTRACT B) and the taxonomy-split requirement (C-40 equivalent: structural and value violation categories formally labeled and split) — as conditions that must hold for the assertion to be valid; the prerequisites are named inside the assertion block or in a directly attached consistency clause that is part of the CONTRACT B block; a scorer can determine from the assertion text alone that failing either named prerequisite constitutes an internal inconsistency detectable without inspecting phase content; the claim is therefore stronger than C-42 because its falsifiability conditions are declared, not merely inferable.
- **Partial (1):** The self-sufficiency assertion includes a falsifiability clause but names only one structural prerequisite (value-presence or taxonomy-split, not both); or names both prerequisites but locates them in a separate annotation outside the CONTRACT B block rather than inside the assertion itself; or uses generic language ("this assertion requires contract completeness") without identifying the specific structural properties by type.
- **Fail (0):** CONTRACT B's self-sufficiency assertion does not name its own structural prerequisites; the internal consistency of the assertion must be inferred from content rather than declared; or C-42 fails.
