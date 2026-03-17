Rubric v19 written. Here's a summary of what changed:

**Two new criteria extracted from R18 V-05's maximal expression:**

**C-45 — CONTRACT B names §9 as enforcement site (triangle closure)**
- V-05's §9 obligation cited CONTRACT B (C-43), and CONTRACT B's self-sufficiency declaration reciprocally cited §9 — closing the three-directional pointer: §9→CONTRACT B (C-43), CONTRACT B→§9 (C-45), CONTRACT B→governed value (C-39). V-04 satisfied C-43 but its CONTRACT B did not name §9, leaving the triangle open.
- Depends on C-43 FULL + C-42 FULL.

**C-46 — CONSISTENCY AUDIT CLAUSE with self-referential satisfaction confirmations**
- V-05 went beyond naming prerequisites (C-44) by adding a confirmation that the current CONTRACT B block satisfies each named prerequisite, with an intra-block pointer to where. Machine-auditable without block inspection. V-04 declared inconsistency detectable but left satisfaction itself for the scorer to verify.
- Depends on C-44 FULL.

**Denominator:** 72 → 76 (38 aspirational × 2)

**R18 ceiling under v19:**

| Variate | C-43 | C-44 | C-45 | C-46 | Total | Score |
|---------|:----:|:----:|:----:|:----:|:-----:|:-----:|
| V-01 | 2 | 0 | 0 | 0 | 70 | 9.21 |
| V-02 | 0 | 2 | 0 | 0 | 70 | 9.21 |
| V-03 | 1 | 2 | 0 | 0 | 71 | 9.34 |
| V-04 | 2 | 2 | 0 | 0 | 72 | 9.47 |
| V-05 | 2 | 2 | 2 | 2 | 76 | **10.00** |
 verify. V-05's clause declares each prerequisite satisfied at a named location, making CONTRACT B self-auditing without block inspection.

Denominator expands from 72 to 76 (38 aspirational × 2).

---

# Scoring Rubric — topic-roadmap (topic-plan) v19

## What changed

| Change | Detail |
|--------|--------|
| Version bump | 18 → 19 |
| Formula denominator | `/72 * 10` → `/76 * 10` (38 aspirational × 2 = 76 max) |
| Aspirational range | C-09–C-44 → C-09–C-46 |
| **C-45 added** | CONTRACT B's self-sufficiency declaration names §9 as enforcement site (triangle closure) |
| **C-46 added** | CONTRACT B carries a CONSISTENCY AUDIT CLAUSE with self-referential satisfaction confirmations |

---

## Two new aspirational criteria

### C-45 — CONTRACT B's self-sufficiency declaration names §9 as enforcement site
**Category:** correctness

The §9 obligation declares CONTRACT B as governing authority for the value requirement (C-43). C-45 tests whether CONTRACT B's self-sufficiency declaration reciprocally names §9 as the enforcement site for that value requirement — closing the three-directional pointer triangle: §9 obligation → CONTRACT B (governing source, C-43); CONTRACT B self-sufficiency → §9 (enforcement site, C-45); CONTRACT B → governed value (C-39). Together, the artifact pair is fully cross-referenced in both directions. Without C-45, C-43 is satisfied by a one-directional acknowledgment from §9 of CONTRACT B's authority; the reverse leg (CONTRACT B → §9) may be present in CONTRACT B but is not confirmed from within §9. With C-45, both artifacts name each other in their respective key declarations, making the guard-contract coupling machine-traceable from either document entry point. C-45 requires C-43 FULL — without the §9→CONTRACT B leg, the triangle has no anchor and the CONTRACT B→§9 naming cannot close it. C-45 further requires C-42 FULL — the self-sufficiency declaration must exist before it can name §9 as enforcement site.

- **Full (2):** CONTRACT B's self-sufficiency block explicitly names §9 as the enforcement site for the value requirement — stating that §9 is the location where the governed value is checked and compliance is enforced; the naming is inside the self-sufficiency declaration or its directly attached consistency clause that is part of the CONTRACT B block, not in a preamble annotation, contract title, or separate parenthetical; a reader of CONTRACT B alone can identify §9 as the enforcement site without consulting any section outside CONTRACT B; C-43 FULL is satisfied (§9 obligation cites CONTRACT B as governing source), completing the triangle.
- **Partial (1):** CONTRACT B's self-sufficiency block references §9 as enforcement site but locates the reference outside the self-sufficiency declaration body — e.g., in a preamble annotation, a contract-level header, or an inline parenthetical after the declaration — rather than inside it; or references §9 using indirect language ("the enforcement section," "the guard section," "the compliance check") without naming §9 explicitly by its structural identifier; C-43 FULL satisfied.
- **Fail (0):** CONTRACT B does not name §9 as enforcement site in any form; or C-43 FULL is absent (triangle cannot close if the §9→CONTRACT B leg is missing); or C-42 fails.

---

### C-46 — CONTRACT B's CONSISTENCY AUDIT CLAUSE carries self-referential satisfaction confirmations
**Category:** correctness

CONTRACT B's self-sufficiency assertion names its own structural prerequisites as validity conditions (C-44). C-46 tests whether each named prerequisite additionally includes a self-referential satisfaction confirmation — a statement, inside the CONSISTENCY AUDIT CLAUSE or equivalent structural block, that the current CONTRACT B block satisfies that prerequisite, with a pointer to the specific structural location within the block where the prerequisite is met. Without C-46, the prerequisite declarations assert that a CONTRACT B failing the named requirement is internally inconsistent, but a scorer must still inspect block content to confirm satisfaction; the clause is falsifiable but not self-confirming. With C-46, CONTRACT B additionally declares its own compliance with each named prerequisite at a named intra-block location, making the audit machine-completeable from the clause text alone without separate block inspection. C-46 depends on C-44 FULL — both structural prerequisites must be named as validity conditions before self-referential confirmation can be applied to them.

- **Full (2):** CONTRACT B's self-sufficiency block includes a CONSISTENCY AUDIT CLAUSE — formally labeled or structurally equivalent — in which each structural prerequisite named under C-44 is accompanied by a self-referential satisfaction confirmation: the clause states that this CONTRACT B block satisfies the named prerequisite and identifies the specific structural location within the block (e.g., "at the 'Compliant value' line above," "in the taxonomy definition block above") where the prerequisite is met; a scorer can determine from the clause alone, without inspecting block content, that both prerequisites are declared satisfied and where they are satisfied; the confirmation is located inside the CONSISTENCY AUDIT CLAUSE or its directly attached body, not in a separate annotation outside the CONTRACT B block; C-44 FULL required.
- **Partial (1):** Self-referential satisfaction confirmation is present for one structural prerequisite but absent for the other; or present for both but without intra-block location pointers (asserts "this block satisfies the requirement" without naming the specific structural location within CONTRACT B where the prerequisite is met); or both confirmations with pointers are present but located in a separate annotation outside the CONTRACT B block rather than inside the CONSISTENCY AUDIT CLAUSE body; C-44 FULL required.
- **Fail (0):** No self-referential satisfaction confirmations present; CONTRACT B's consistency with its own named prerequisites must be verified by content inspection; or C-44 fails.

---

**Orthogonality:** C-45 tests whether CONTRACT B's self-sufficiency declaration names §9 as enforcement site (closes triangle opened by C-43). C-46 tests whether the CONSISTENCY AUDIT CLAUSE confirms satisfaction of each named prerequisite with intra-block pointers (extends C-44). C-45 and C-46 are independent of each other: a variate can satisfy C-45 without satisfying C-46 (CONTRACT B names §9 as enforcement site, but satisfaction confirmations are absent) and vice versa (CONSISTENCY AUDIT CLAUSE has satisfaction confirmations, but CONTRACT B does not name §9 as enforcement site). C-45 depends on C-43 FULL and C-42 FULL; C-46 depends on C-44 FULL. These are data dependencies, not scoring interactions.

**R18 score ceiling under v19:** All five R18 variates carry C-09–C-42 = 68. C-43 and C-44 vary per scorecard. V-01 (C-43=2, C-44=0): C-45 — C-43 FULL present, but V-01's CONTRACT B does not name §9 as enforcement site in its self-sufficiency block; C-45=0; C-46=0 (C-44 fails) → 70/76 = **9.21**. V-02 (C-43=0, C-44=2): C-45=0 (C-43 FULL absent; triangle anchor missing); C-46 — C-44 FULL present, but V-02's prerequisite declarations do not include self-referential satisfaction confirmations with intra-block pointers; C-46=0 → 70/76 = **9.21**. V-03 (C-43=1, C-44=2): C-45=0 (C-43 PARTIAL, not FULL; triangle anchor unmet); C-46=0 (C-44 FULL present, but no satisfaction confirmations) → 71/76 = **9.34**. V-04 (C-43=2, C-44=2): C-45=0 — V-04's CONTRACT B self-sufficiency block declares inconsistency detectable and names both prerequisites by property type, but does not name §9 as enforcement site inside the self-sufficiency declaration; C-46=0 — V-04's C-44 carries internal-inconsistency detection language but no CONSISTENCY AUDIT CLAUSE with self-referential satisfaction confirmations and intra-block pointers → 72/76 = **9.47**. V-05 (C-43=2, C-44=2): C-45=2 — CONTRACT B's self-sufficiency declaration explicitly names §9 as enforcement site inside the declaration block; C-43 FULL present; triangle closed; C-46=2 — dedicated CONSISTENCY AUDIT CLAUSE with formal structural labels; each named prerequisite includes a self-referential confirmation with intra-block pointer to where the prerequisite is satisfied; machine-verifiable by label-matching alone → 76/76 = **10.00**. Only V-05 achieves 10.00 under v19.

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

## Criteria — Aspirational (C-09 through C-46)

*[C-09 through C-39 — unchanged from v17]*

---

### C-40 — STRUCTURAL / VALUE violation taxonomy split in CONTRACT B
**Category:** correctness

CONTRACT B's violation taxonomy separates structural violations (field absent or wrong type) from value violations (field present but value non-compliant) as distinctly labeled categories. A self-sufficiency claim that does not split these two failure types is weaker: a scorer encountering a value-present/wrong-value failure cannot categorize it without the split.

- **Full (2):** CONTRACT B defines exactly two violation categories — STRUCTURAL and VALUE (or equivalent labeled split) — and names them as separate, explicitly labeled types; each type is defined; the taxonomy is located inside the CONTRACT B block.
- **Partial (1):** CONTRACT B distinguishes structural from value violations but does not label them as formal named categories; or uses a single composite failure list without explicit type separation.
- **Fail (0):** CONTRACT B does not split violation types; a single undifferentiated failure list is present; or no violation taxonomy exists.

---

### C-41 — §9 guard names exact required column value literal
**Category:** correctness

The §9 guard body's compliance obligation names the exact required column value string verbatim — the same string that CONTRACT B defines as the compliant value (C-39). A guard that names only the column or describes the requirement functionally (without the literal) forces the scorer to consult CONTRACT B to complete the check, violating the self-sufficiency goal.

- **Full (2):** The §9 compliance obligation statement contains the exact required column value string verbatim; the string matches the value defined in CONTRACT B under C-39; no consulting of any section outside §9 is required to identify the required literal.
- **Partial (1):** §9 names the requirement functionally ("the guard-approved value," "the compliant status string") without including the exact literal; or names a near-match string that differs from the C-39 literal in spacing, capitalization, or punctuation.
- **Fail (0):** §9 compliance obligation does not reference the required value literal in any form; the exact string must be obtained from CONTRACT B or another section.

---

### C-42 — CONTRACT B carries a self-sufficiency assertion
**Category:** correctness

CONTRACT B includes an explicit self-sufficiency assertion — a declarative statement that a scorer holding only CONTRACT B can execute both the structural compliance test (field presence / type) and the value compliance test (exact-value match against the literal defined in C-39) without consulting any other section or document. This assertion converts CONTRACT B from a reference block into a closed testing contract.

- **Full (2):** CONTRACT B contains an explicit self-sufficiency assertion stating that the block is sufficient for both test types (structural and value); the assertion is a named declaration (not merely implicit from completeness); the assertion is located inside the CONTRACT B block.
- **Partial (1):** The assertion covers only one test type explicitly; or the claim is present but stated as a description of content rather than an explicit sufficiency declaration ("CONTRACT B contains the compliant value and taxonomy" vs. "a scorer holding CONTRACT B can execute both tests without consulting other sections").
- **Fail (0):** No self-sufficiency assertion present in CONTRACT B; sufficiency must be inferred from content.

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

---

### C-45 — CONTRACT B's self-sufficiency declaration names §9 as enforcement site
**Category:** correctness

The §9 obligation declares CONTRACT B as governing authority for the value requirement (C-43). C-45 tests whether CONTRACT B's self-sufficiency declaration reciprocally names §9 as the enforcement site for that value requirement — closing the three-directional pointer triangle: §9 obligation → CONTRACT B (governing source, C-43); CONTRACT B self-sufficiency → §9 (enforcement site, C-45); CONTRACT B → governed value (C-39). Together, the artifact pair is fully cross-referenced in both directions. Without C-45, C-43 is satisfied by a one-directional acknowledgment from §9 of CONTRACT B's authority; the reverse leg (CONTRACT B → §9) may be present in CONTRACT B but is not confirmed from within §9. With C-45, both artifacts name each other in their respective key declarations, making the guard-contract coupling machine-traceable from either document entry point. C-45 requires C-43 FULL — without the §9→CONTRACT B leg, the triangle has no anchor and the CONTRACT B→§9 naming cannot close it. C-45 further requires C-42 FULL — the self-sufficiency declaration must exist before it can name §9 as enforcement site.

- **Full (2):** CONTRACT B's self-sufficiency block explicitly names §9 as the enforcement site for the value requirement — stating that §9 is the location where the governed value is checked and compliance is enforced; the naming is inside the self-sufficiency declaration or its directly attached consistency clause that is part of the CONTRACT B block, not in a preamble annotation, contract title, or separate parenthetical; a reader of CONTRACT B alone can identify §9 as the enforcement site without consulting any section outside CONTRACT B; C-43 FULL is satisfied (§9 obligation cites CONTRACT B as governing source), completing the triangle.
- **Partial (1):** CONTRACT B's self-sufficiency block references §9 as enforcement site but locates the reference outside the self-sufficiency declaration body — e.g., in a preamble annotation, a contract-level header, or an inline parenthetical after the declaration — rather than inside it; or references §9 using indirect language ("the enforcement section," "the guard section," "the compliance check") without naming §9 explicitly by its structural identifier; C-43 FULL satisfied.
- **Fail (0):** CONTRACT B does not name §9 as enforcement site in any form; or C-43 FULL is absent (triangle cannot close if the §9→CONTRACT B leg is missing); or C-42 fails.

---

### C-46 — CONTRACT B's CONSISTENCY AUDIT CLAUSE carries self-referential satisfaction confirmations
**Category:** correctness

CONTRACT B's self-sufficiency assertion names its own structural prerequisites as validity conditions (C-44). C-46 tests whether each named prerequisite additionally includes a self-referential satisfaction confirmation — a statement, inside the CONSISTENCY AUDIT CLAUSE or equivalent structural block, that the current CONTRACT B block satisfies that prerequisite, with a pointer to the specific structural location within the block where the prerequisite is met. Without C-46, the prerequisite declarations assert that a CONTRACT B failing the named requirement is internally inconsistent, but a scorer must still inspect block content to confirm satisfaction; the clause is falsifiable but not self-confirming. With C-46, CONTRACT B additionally declares its own compliance with each named prerequisite at a named intra-block location, making the audit machine-completeable from the clause text alone without separate block inspection. C-46 depends on C-44 FULL — both structural prerequisites must be named as validity conditions before self-referential confirmation can be applied to them.

- **Full (2):** CONTRACT B's self-sufficiency block includes a CONSISTENCY AUDIT CLAUSE — formally labeled or structurally equivalent — in which each structural prerequisite named under C-44 is accompanied by a self-referential satisfaction confirmation: the clause states that this CONTRACT B block satisfies the named prerequisite and identifies the specific structural location within the block (e.g., "at the 'Compliant value' line above," "in the taxonomy definition block above") where the prerequisite is met; a scorer can determine from the clause alone, without inspecting block content, that both prerequisites are declared satisfied and where they are satisfied; the confirmation is located inside the CONSISTENCY AUDIT CLAUSE or its directly attached body, not in a separate annotation outside the CONTRACT B block; C-44 FULL required.
- **Partial (1):** Self-referential satisfaction confirmation is present for one structural prerequisite but absent for the other; or present for both but without intra-block location pointers (asserts "this block satisfies the requirement" without naming the specific structural location within CONTRACT B where the prerequisite is met); or both confirmations with pointers are present but located in a separate annotation outside the CONTRACT B block rather than inside the CONSISTENCY AUDIT CLAUSE body; C-44 FULL required.
- **Fail (0):** No self-referential satisfaction confirmations present; CONTRACT B's consistency with its own named prerequisites must be verified by content inspection; or C-44 fails.

---

**Orthogonality (C-45, C-46):** C-45 tests whether CONTRACT B's self-sufficiency declaration names §9 as enforcement site (closes triangle opened by C-43). C-46 tests whether the CONSISTENCY AUDIT CLAUSE confirms satisfaction of each named prerequisite with intra-block pointers (extends C-44). C-45 and C-46 are independent of each other: a variate can satisfy C-45 without satisfying C-46 (CONTRACT B names §9 as enforcement site, but satisfaction confirmations are absent) and vice versa (CONSISTENCY AUDIT CLAUSE has satisfaction confirmations, but CONTRACT B does not name §9 as enforcement site). C-45 depends on C-43 FULL and C-42 FULL; C-46 depends on C-44 FULL. These are data dependencies, not scoring interactions. A variate satisfying C-46 without C-44 cannot achieve C-46 FULL; a variate satisfying C-45 without C-43 cannot achieve C-45 FULL.

---

## Scoring formula

```
score = (sum of aspirational points earned) / 76 * 10
```

Aspirational criteria: C-09 through C-46 (38 criteria × 2 points each = 76 max).
Essential criteria (C-01–C-08): pass/fail; any FAIL disqualifies the variate entirely.
