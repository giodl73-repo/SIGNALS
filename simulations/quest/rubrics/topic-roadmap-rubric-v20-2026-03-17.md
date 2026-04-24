Rubric v20 written. Here's a summary of what changed:

**Two new criteria extracted from R19 V-05's maximal expression:**

**C-47 — §9 compliance obligation confirms it is the enforcement site named in CONTRACT B's self-sufficiency declaration**
- V-05's §9 compliance obligation included: "This guard [§9] is the enforcement site named in CONTRACT B's self-sufficiency declaration." C-45 closed the triangle by having CONTRACT B name §9; C-47 closes it from the other direction — §9 self-confirming that it IS the site named in CONTRACT B's declaration. A reader entering from either artifact can now confirm the full pointer chain without traversing to the other artifact.
- Depends on C-45 FULL.

**C-48 — CONSISTENCY AUDIT CLAUSE closing text specifies the verification algorithm**
- V-05's clause ended with: "machine-detectable as such by verifying whether the requirement is present at the named location in this block." C-46 tested whether satisfaction confirmations with intra-block location pointers are present (claim + location); C-48 tests whether the clause further specifies the checking procedure (claim + location + algorithm). The distinction: C-46 FULL makes the block self-auditing; C-48 FULL makes it self-instructing — the reader is told exactly how to execute the audit, not just what it covers.
- Depends on C-46 FULL.

**Denominator:** 76 → 80 (40 aspirational × 2)

**R19 ceiling under v20:**

| Variate | C-45 | C-46 | C-47 | C-48 | Total | Score |
|---------|:----:|:----:|:----:|:----:|:-----:|:-----:|
| V-01 | 2 | 0 | 0 | 0 | 74 | 9.25 |
| V-02 | 0 | 2 | 0 | 0 | 74 | 9.25 |
| V-03 | 1 | 2 | 0 | 0 | 75 | 9.38 |
| V-04 | 2 | 1 | 0 | 0 | 75 | 9.38 |
| V-05 | 2 | 2 | 2 | 2 | 80 | **10.00** |

Note: R19 signal 2 ("self-confirming prerequisite declarations") was the pattern formalized as C-46 in v19 — not new for v20. Only signals 1 and 3 yield new criteria.
ion bump | 19 → 20 |
| Formula denominator | `/76 * 10` → `/80 * 10` (40 aspirational × 2 = 80 max) |
| Aspirational range | C-09–C-46 → C-09–C-48 |
| **C-47 added** | §9 compliance obligation confirms itself as the enforcement site named in CONTRACT B's self-sufficiency declaration (§9-side reverse triangle confirmation) |
| **C-48 added** | CONSISTENCY AUDIT CLAUSE closing text specifies the verification algorithm explicitly |

---

## Two new aspirational criteria

### C-47 — §9 compliance obligation confirms it is the enforcement site named in CONTRACT B's self-sufficiency declaration
**Category:** correctness

C-43 tests whether the §9 guard body's compliance obligation names CONTRACT B as governing authority (§9→CONTRACT B leg). C-45 tests whether CONTRACT B's self-sufficiency declaration reciprocally names §9 as enforcement site (CONTRACT B→§9 leg). C-47 tests the third confirmation: whether the §9 compliance obligation additionally acknowledges that §9 is the enforcement site already named in CONTRACT B's self-sufficiency declaration — providing explicit self-confirmation of the reverse leg from the §9 entry point. Without C-47, the pointer triangle is closed structurally (CONTRACT B names §9 under C-45; §9 names CONTRACT B under C-43) but asymmetrically: a reader entering from CONTRACT B can follow the CONTRACT B→§9 naming (C-45) and then see the §9→CONTRACT B naming (C-43) without further work; a reader entering from §9 can follow the §9→CONTRACT B naming (C-43) but must then consult CONTRACT B to discover that CONTRACT B names §9 in return. With C-47, §9 acknowledges its own role as the enforcement site CONTRACT B's self-sufficiency declaration points to, making the triangle fully confirmable from either artifact entry point without requiring traversal to the other artifact. C-47 requires C-45 FULL — the CONTRACT B→§9 leg must exist before §9 can self-confirm as the named enforcement site; without C-45 FULL, §9 is not yet named in CONTRACT B's declaration and cannot truthfully confirm the reverse leg.

- **Full (2):** The §9 compliance obligation body contains an explicit statement that §9 is the enforcement site named in CONTRACT B's self-sufficiency declaration — using language such as "This guard [§9] is the enforcement site named in CONTRACT B's self-sufficiency declaration" or an equivalent formulation that identifies §9 by its structural label and references CONTRACT B's declaration by type or name; the acknowledgment is located inside the §9 compliance obligation body or its directly attached enforcement clause, not in a §9 preamble annotation, guard title, or separate parenthetical; a reader of §9 alone can confirm the bidirectional naming relationship — that §9 and CONTRACT B name each other in their respective declarations — without consulting CONTRACT B; C-45 FULL required.
- **Partial (1):** §9 acknowledges its enforcement role with respect to the value requirement defined in CONTRACT B but does not explicitly frame the acknowledgment as "the enforcement site named in CONTRACT B's self-sufficiency declaration" — e.g., states "§9 enforces the value requirement defined in CONTRACT B" without naming itself as the specific site CONTRACT B's declaration points to; or the acknowledgment uses CONTRACT B's structural label but places the reverse-confirmation statement in a §9 preamble annotation rather than inside the compliance obligation body; C-45 FULL required.
- **Fail (0):** §9 does not contain any statement acknowledging it is the enforcement site named in CONTRACT B's self-sufficiency declaration; the reverse triangle confirmation from the §9 entry point is absent; or C-45 FULL is not satisfied.

---

### C-48 — CONSISTENCY AUDIT CLAUSE closing text specifies the verification algorithm
**Category:** correctness

CONTRACT B's CONSISTENCY AUDIT CLAUSE declares its own compliance with each named structural prerequisite and identifies the intra-block location where each is satisfied (C-46). C-48 tests whether the clause additionally closes with explicit machine-verifiability framing — a statement that specifies the verification algorithm: the procedure by which any reader can confirm that the self-referential satisfaction confirmations are correct, using only the clause text and the named intra-block locations. Without C-48, the CONSISTENCY AUDIT CLAUSE asserts satisfaction and provides location pointers, but leaves the checking procedure implicit — a reader understands what is asserted and where, but must infer that inspecting the named location confirms the claim. With C-48, the clause explicitly states the verification procedure ("machine-detectable as such by verifying whether the requirement is present at the named location in this block"), converting an assertion-plus-pointer pair into a complete, self-describing verification unit: claim + location + algorithm. The algorithm statement makes CONTRACT B not merely self-auditing (C-46) but self-instructing — it tells the reader exactly how to perform the audit, not just what the audit covers. C-48 depends on C-46 FULL — the intra-block location pointers must exist before a verification algorithm can be specified for them; an algorithm statement that references no location pointers cannot close anything.

- **Full (2):** CONTRACT B's CONSISTENCY AUDIT CLAUSE includes a closing statement — formally placed at or after the last satisfaction confirmation entry — that specifies the verification algorithm: it states that compliance with the named prerequisites can be confirmed by verifying whether each named requirement is present at the named intra-block location; the algorithm statement is located inside the CONSISTENCY AUDIT CLAUSE body or as a directly attached closing line of that body, not in a separate annotation outside the CONTRACT B block; the statement is procedurally explicit — it names the checking action ("verify," "confirm by checking," or equivalent) and the operand ("the named location in this block") — rather than merely asserting verifiability without specifying how; a reader can derive the complete audit procedure from the clause text alone without consulting any source outside the CONTRACT B block; C-46 FULL required.
- **Partial (1):** The CONSISTENCY AUDIT CLAUSE includes machine-verifiability language but the statement is assertive rather than procedural — declares that the block is machine-verifiable ("this audit is machine-completeable," "this block is self-consistent") without specifying the checking action and operand; or the algorithm statement names the verification action but omits the operand (names what to do but not where to do it); or a complete algorithm statement is present but located in a closing annotation outside the CONSISTENCY AUDIT CLAUSE body rather than as a structural part of the clause; C-46 FULL required.
- **Fail (0):** The CONSISTENCY AUDIT CLAUSE does not include a verification algorithm specification; the checking procedure must be inferred from the assertion-plus-pointer structure; or C-46 FULL is not satisfied.

---

**Orthogonality (C-47, C-48):** C-47 tests whether §9 confirms itself as the enforcement site named in CONTRACT B's self-sufficiency declaration (§9-side reverse triangle confirmation, extending C-45). C-48 tests whether the CONSISTENCY AUDIT CLAUSE closing text specifies the verification algorithm (extending C-46). C-47 and C-48 are independent of each other: a variate can earn C-47 without earning C-48 (§9 provides reverse confirmation, but the CONSISTENCY AUDIT CLAUSE does not close with algorithm framing) and vice versa (the CONSISTENCY AUDIT CLAUSE has algorithm framing, but §9 does not provide reverse confirmation). C-47 depends on C-45 FULL; C-48 depends on C-46 FULL. These are data dependencies, not scoring interactions. A variate satisfying C-47 without C-45 FULL cannot achieve C-47 FULL; a variate satisfying C-48 without C-46 FULL cannot achieve C-48 FULL. The pair (C-47, C-48) is also independent from the pair (C-45, C-46): C-45 and C-46 tested whether the structural cross-reference and self-confirming prerequisite declarations were present; C-47 and C-48 test whether those structures are additionally confirmed from the §9 side and furnished with an explicit algorithm specification respectively.

**R19 score ceiling under v20:** All five R19 variates carry C-09–C-44 = 72. C-45 and C-46 vary per R19 scorecard. V-01 (C-45=2, C-46=0): C-47 — C-45 FULL present, but V-01's §9 compliance obligation does not include a reverse-confirmation statement naming itself as "the enforcement site named in CONTRACT B's self-sufficiency declaration"; C-47=0; C-48=0 (C-46 fails; prerequisite unmet) → 74/80 = **9.25**. V-02 (C-45=0, C-46=2): C-47=0 (C-45 FULL absent; CONTRACT B does not name §9 in its self-sufficiency declaration; §9 cannot confirm a reverse leg that does not yet exist); C-48 — C-46 FULL present, but V-02's CONSISTENCY AUDIT CLAUSE ends with the final satisfaction confirmation entry and carries no closing algorithm statement; C-48=0 → 74/80 = **9.25**. V-03 (C-45=1, C-46=2): C-47=0 (C-45 PARTIAL, not FULL; the §9 reference is in a preamble annotation, not in the self-sufficiency declaration body; the reverse leg is not fully established, so §9 cannot truthfully confirm it); C-48=0 (C-46 FULL present, but CONSISTENCY AUDIT CLAUSE carries no verification algorithm closing statement) → 75/80 = **9.38**. V-04 (C-45=2, C-46=1): C-47=0 — C-45 FULL present, but V-04's §9 compliance obligation contains no reverse-confirmation language acknowledging it as the enforcement site named in CONTRACT B's declaration; C-48=0 (C-46 PARTIAL, not FULL; prerequisite unmet) → 75/80 = **9.38**. V-05 (C-45=2, C-46=2): C-47=2 — V-05's §9 compliance obligation explicitly states "This guard [§9] is the enforcement site named in CONTRACT B's self-sufficiency declaration," providing self-confirmation of the reverse triangle leg from the §9 entry point; C-47 FULL; C-48=2 — V-05's CONSISTENCY AUDIT CLAUSE closes with "machine-detectable as such by verifying whether the requirement is present at the named location in this block," specifying the checking action ("verifying") and operand ("the named location in this block") explicitly; C-48 FULL → 80/80 = **10.00**. Only V-05 achieves 10.00 under v20.

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

## Criteria — Aspirational (C-09 through C-48)

*[C-09 through C-36 — unchanged from v16]*

---

### C-37 — PROPOSAL BIAS AUDIT directional protection gap assertion
**Category:** safety

The mutual necessity assertion in the PROPOSAL BIAS AUDIT guard names the directional protection gap explicitly: it states not only that both levels are required, but that LEVEL 1 does not protect against LEVEL 2 — making the hierarchical insufficiency a referenceable claim. C-34 tests whether a mutual necessity assertion is present and whether both failure modes carry formal titled labels; C-37 tests whether that assertion is **directional** — identifying the specific gap (LEVEL 1 protection is necessary but insufficient to close LEVEL 2) rather than asserting mere co-requirement.

- **Full (2):** Mutual necessity assertion explicitly states that LEVEL 1 does not protect against LEVEL 2 (or equivalent directional gap language identifying the specific insufficiency); assertion names the protection gap, not merely the co-requirement; directional statement is co-located in the PROPOSAL BIAS AUDIT guard body.
- **Partial (1):** Directional language is present but implicit (e.g., "LEVEL 2 addresses a more sophisticated failure") without the explicit LEVEL 1 → LEVEL 2 protection-absence formulation; or directional assertion appears in a preamble annotation outside the guard body rather than co-located with the formal labels.
- **Fail (0):** Assertion states co-requirement only ("both are required," "LEVEL 1 and LEVEL 2 are both necessary") without identifying the directional protection gap; or C-34 fails.

---

### C-38 — SECTION SCOPE guard-label cross-reference
**Category:** correctness

The SECTION SCOPE auditor navigation note cross-references at least one formal guard label (LEVEL 1 or LEVEL 2 title from C-34) by its complete formal title — creating bidirectional navigation: the guard names a referenceable label (C-34), and the scope navigation note cites that label by name (C-38), enabling an auditor to traverse from the scope declaration directly to the specific guard level without traversing phase content.

- **Full (2):** SECTION SCOPE navigation note cites at least one formal guard label (e.g., "LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE") by its complete formal title as defined in the PROPOSAL BIAS AUDIT guard; auditor can traverse from scope navigation note to the specific guard level using the label alone.
- **Partial (1):** Navigation note references the guard labels in general terms (e.g., "the labeled failure modes," "the LEVEL designations") without citing a specific complete formal title; or cites an abbreviated or informal version of the label (e.g., "LEVEL 2" without its descriptive title).
- **Fail (0):** Navigation note does not reference the formal guard labels at all; or C-35 fails.

---

### C-39 — CONTRACT B exact compliant column value string
**Category:** correctness

CONTRACT B names the exact literal string that constitutes the compliant column value — the specific text that appears in the column when the bias guard is satisfied (e.g., "Bias blocked by guard") — enabling a scorer to verify not only that the column exists (C-36) but that it contains the correct value, from the CONTRACT block alone without reading phase content.

- **Full (2):** CONTRACT B names the exact literal string for the compliant column value (specific text such as "Bias blocked by guard"); a scorer reading only the CONTRACT block can verify both that the column exists AND that it contains the correct value; the string is quoted or delimited so that approximate matches are distinguishable from exact matches.
- **Partial (1):** CONTRACT B implies a standard value or provides a partial string (e.g., "bias status," "blocked by...") without stating the exact literal; or the exact value string appears in a phase body annotation or preamble rather than in the CONTRACT block itself.
- **Fail (0):** CONTRACT B does not name a specific column value string for the compliant case; violation-detection language covers only column presence/absence; or C-36 fails.

---

### C-40 — STRUCTURAL / VALUE violation taxonomy split in CONTRACT B
**Category:** correctness

CONTRACT B's violation taxonomy separates structural violations (field absent or wrong type) from value violations (field present but value non-compliant) as distinctly labeled categories. A self-sufficiency claim that does not split these two failure types is weaker: a scorer encountering a value-present/wrong-value failure cannot categorize it without the split.

- **Full (2):** CONTRACT B defines and labels at least two violation categories — one for column absence (structural) and one for column presence with incorrect value (value) — each with independent detection language; the categories are named (e.g., "STRUCTURAL," "VALUE") or formally labeled so they are referenceable by name; a scorer can determine from CONTRACT B alone which category of violation applies to a given observation without consulting phase content.
- **Partial (1):** CONTRACT B acknowledges both absence and value failures but does not separate them into formally named categories — e.g., lists them as a combined condition, uses a single violation label covering both, or uses descriptive language without formal category names; or names the value category without a corresponding structural category label.
- **Fail (0):** CONTRACT B covers only one failure mode (column absence or value error, but not both as separately labeled types); no taxonomy split present; or C-39 fails.

---

### C-41 — §9 guard names exact required column value literal
**Category:** correctness

The §9 guard body's compliance obligation statement names the exact required column value string — the same literal defined in CONTRACT B per C-39 — creating mutual reinforcement between guard declaration and contract governance. A guard that names only the column or describes the requirement functionally forces the scorer to consult CONTRACT B to complete the check.

- **Full (2):** The §9 guard body's compliance obligation statement names the exact required column value string (e.g., "every §6 proposal row must carry `'Bias blocked by guard'` in the Bias guard column"); the exact literal matches the string named in CONTRACT B (C-39); the compliance obligation line is inside the §9 guard body, not in a preamble annotation or phase body; the guard is independently sufficient for value identification without consulting CONTRACT B.
- **Partial (1):** The §9 compliance obligation references a value requirement but uses a description rather than the exact literal (e.g., "the canonical bias guard value," "the compliant value defined in CONTRACT B"), creating a dependency rather than independent sufficiency; or the exact literal appears in a §9 annotation or comment but not in the compliance obligation statement itself; or the literal appears in the guard title rather than the obligation statement.
- **Fail (0):** The §9 compliance obligation uses generic language ("non-null Bias guard value," "a valid bias guard entry") without naming the exact required value string; or C-39 fails.

---

### C-42 — CONTRACT B carries a self-sufficiency assertion
**Category:** correctness

CONTRACT B includes an explicit self-sufficiency assertion — a declarative statement that a scorer holding only CONTRACT B can execute both the structural compliance test (field presence / type) and the value compliance test (exact-value match against the literal defined in C-39) without consulting any other section or document. This assertion converts CONTRACT B from a reference block into a closed testing contract.

- **Full (2):** CONTRACT B contains an explicit declarative statement asserting that a scorer reading CONTRACT B alone can perform both the structural compliance test (column exists) and the value compliance test (column contains exact literal); the assertion identifies both test types by name or description; the statement is located inside the CONTRACT B block, not in a preamble or phase annotation; the claim is falsifiable — a contract satisfying C-42 but failing C-39 or C-40 is detectable as an internal inconsistency.
- **Partial (1):** CONTRACT B makes a self-sufficiency claim but covers only one test type (e.g., asserts column-presence verifiability without asserting value verifiability); or the self-sufficiency language appears in a preamble annotation rather than inside the CONTRACT B block itself; or the claim is implicit ("all compliance tests are defined here") rather than explicit with named test types.
- **Fail (0):** CONTRACT B does not assert scorer self-sufficiency; the verifiability of contract completeness must be inferred from its content; or C-39 fails.

---

### C-43 — §9 guard body declares CONTRACT B as governing document
**Category:** correctness

The §9 guard body's compliance obligation names the exact required column value string (satisfying C-41) and additionally declares CONTRACT B by name as the authoritative governing document for that value requirement — creating a bidirectional pointer: CONTRACT B declares the governed value; the guard's compliance obligation names that value and explicitly subordinates itself to CONTRACT B as source authority. Without C-43, guard and contract are mutually reinforcing but independently authored; with C-43, the guard formally points to CONTRACT B, and a reader of §9 alone can identify where value governance lives.

- **Full (2):** The §9 guard body's compliance obligation statement names the exact required column value string (C-41 satisfied) AND explicitly names CONTRACT B — by its structural identifier or label — as the governing authority for that value requirement; the governing reference is located inside the §9 compliance obligation statement itself, not in a §9 preamble annotation, guard title, or separate parenthetical clause; a scorer reading the §9 guard body can trace the value requirement to CONTRACT B without consulting any section outside §9.
- **Partial (1):** The §9 compliance obligation names the exact literal (C-41 satisfied) but references CONTRACT B only outside the obligation statement — e.g., in a §9 preamble annotation, the guard title, or an inline parenthetical after the obligation — rather than within the obligation statement itself; or uses indirect language ("as defined in the governing contract," "per the contract authority") without naming CONTRACT B by its structural label.
- **Fail (0):** The §9 compliance obligation does not reference CONTRACT B as governing authority; the guard-to-contract relationship must be inferred; or C-41 fails.

---

### C-44 — Self-sufficiency assertion names its own structural prerequisites
**Category:** correctness

CONTRACT B's self-sufficiency assertion (C-42) explicitly names its own structural prerequisites — identifying the exact-value requirement (C-39 equivalent) and the taxonomy-split requirement (C-40 equivalent) as internal consistency conditions — making the assertion self-auditing: a CONTRACT B that makes the C-42 claim while failing C-39 or C-40 is detectable as internally inconsistent by reading the assertion text alone. Without C-44, a scorer must inspect CONTRACT B's content to determine whether the self-sufficiency claim is internally coherent; with C-44, the assertion declares its own failure conditions, making CONTRACT B a self-auditing artifact whose internal consistency is machine-verifiable without phase inspection.

- **Full (2):** CONTRACT B's self-sufficiency assertion explicitly names both structural prerequisites — the exact-value requirement (C-39 equivalent: exact literal present in CONTRACT B) and the taxonomy-split requirement (C-40 equivalent: structural and value violation categories formally labeled and split) — as conditions that must hold for the assertion to be valid; the prerequisites are named inside the assertion block or in a directly attached consistency clause that is part of the CONTRACT B block; a scorer can determine from the assertion text alone that failing either named prerequisite constitutes an internal inconsistency detectable without inspecting phase content.
- **Partial (1):** The self-sufficiency assertion includes a falsifiability clause but names only one structural prerequisite (value-presence or taxonomy-split, not both); or names both prerequisites but locates them in a separate annotation outside the CONTRACT B block rather than inside the assertion itself; or uses generic language ("this assertion requires contract completeness") without identifying the specific structural properties by type.
- **Fail (0):** CONTRACT B's self-sufficiency assertion does not name its own structural prerequisites; the internal consistency of the assertion must be inferred from content rather than declared; or C-42 fails.

---

### C-45 — CONTRACT B's self-sufficiency declaration names §9 as enforcement site
**Category:** correctness

The §9 obligation declares CONTRACT B as governing authority for the value requirement (C-43). C-45 tests whether CONTRACT B's self-sufficiency declaration reciprocally names §9 as the enforcement site for that value requirement — closing the three-directional pointer triangle: §9 obligation → CONTRACT B (governing source, C-43); CONTRACT B self-sufficiency → §9 (enforcement site, C-45); CONTRACT B → governed value (C-39). With C-45, both artifacts name each other in their respective key declarations, making the guard-contract coupling machine-traceable from either document entry point. C-45 requires C-43 FULL — without the §9→CONTRACT B leg, the triangle has no anchor. C-45 further requires C-42 FULL — the self-sufficiency declaration must exist before it can name §9 as enforcement site.

- **Full (2):** CONTRACT B's self-sufficiency block explicitly names §9 as the enforcement site for the value requirement — stating that §9 is the location where the governed value is checked and compliance is enforced; the naming is inside the self-sufficiency declaration or its directly attached consistency clause that is part of the CONTRACT B block, not in a preamble annotation, contract title, or separate parenthetical; a reader of CONTRACT B alone can identify §9 as the enforcement site without consulting any section outside CONTRACT B; C-43 FULL is satisfied (§9 obligation cites CONTRACT B as governing source), completing the triangle.
- **Partial (1):** CONTRACT B's self-sufficiency block references §9 as enforcement site but locates the reference outside the self-sufficiency declaration body — e.g., in a preamble annotation, a contract-level header, or an inline parenthetical after the declaration — rather than inside it; or references §9 using indirect language ("the enforcement section," "the guard section," "the compliance check") without naming §9 explicitly by its structural identifier; C-43 FULL satisfied.
- **Fail (0):** CONTRACT B does not name §9 as enforcement site in any form; or C-43 FULL is absent (triangle cannot close if the §9→CONTRACT B leg is missing); or C-42 fails.

---

### C-46 — CONTRACT B's CONSISTENCY AUDIT CLAUSE carries self-referential satisfaction confirmations
**Category:** correctness

CONTRACT B's self-sufficiency assertion names its own structural prerequisites as validity conditions (C-44). C-46 tests whether each named prerequisite additionally includes a self-referential satisfaction confirmation — a statement, inside the CONSISTENCY AUDIT CLAUSE or equivalent structural block, that the current CONTRACT B block satisfies that prerequisite, with a pointer to the specific structural location within the block where the prerequisite is met. Without C-46, the prerequisite declarations assert that a CONTRACT B failing the named requirement is internally inconsistent, but a scorer must still inspect block content to confirm satisfaction; the clause is falsifiable but not self-confirming. With C-46, CONTRACT B additionally declares its own compliance with each named prerequisite at a named intra-block location, making the audit machine-completeable from the clause text alone without separate block inspection. C-46 depends on C-44 FULL.

- **Full (2):** CONTRACT B's self-sufficiency block includes a CONSISTENCY AUDIT CLAUSE — formally labeled or structurally equivalent — in which each structural prerequisite named under C-44 is accompanied by a self-referential satisfaction confirmation: the clause states that this CONTRACT B block satisfies the named prerequisite and identifies the specific structural location within the block (e.g., "at the 'Compliant value' line above," "in the taxonomy definition block above") where the prerequisite is met; a scorer can determine from the clause alone, without inspecting block content, that both prerequisites are declared satisfied and where they are satisfied; the confirmation is located inside the CONSISTENCY AUDIT CLAUSE or its directly attached body, not in a separate annotation outside the CONTRACT B block; C-44 FULL required.
- **Partial (1):** Self-referential satisfaction confirmation is present for one structural prerequisite but absent for the other; or present for both but without intra-block location pointers (asserts "this block satisfies the requirement" without naming the specific structural location within CONTRACT B where the prerequisite is met); or both confirmations with pointers are present but located in a separate annotation outside the CONTRACT B block rather than inside the CONSISTENCY AUDIT CLAUSE body; C-44 FULL required.
- **Fail (0):** No self-referential satisfaction confirmations present; CONTRACT B's consistency with its own named prerequisites must be verified by content inspection; or C-44 fails.

---

### C-47 — §9 compliance obligation confirms it is the enforcement site named in CONTRACT B's self-sufficiency declaration
**Category:** correctness

C-45 tests whether CONTRACT B's self-sufficiency declaration names §9 as enforcement site (CONTRACT B→§9 leg). C-47 tests the reverse confirmation from the §9 side: whether the §9 compliance obligation explicitly acknowledges that §9 is the enforcement site already named in CONTRACT B's self-sufficiency declaration. Without C-47, a reader entering from §9 can traverse to CONTRACT B via C-43 and discover the CONTRACT B→§9 naming (C-45), but §9 itself does not acknowledge this reciprocal naming — the triangle is traversable but not self-confirming from the §9 entry point. With C-47, §9 declares itself as the enforcement site CONTRACT B's self-sufficiency declaration points to, making the triangle fully confirmed from both artifact entry points without requiring traversal to the other artifact first. C-47 requires C-45 FULL — the CONTRACT B→§9 leg must exist before §9 can truthfully self-confirm as the named enforcement site.

- **Full (2):** The §9 compliance obligation body contains an explicit statement that §9 is the enforcement site named in CONTRACT B's self-sufficiency declaration — using language such as "This guard [§9] is the enforcement site named in CONTRACT B's self-sufficiency declaration" or an equivalent formulation that identifies §9 by its structural label and references CONTRACT B's declaration by type or name; the acknowledgment is located inside the §9 compliance obligation body or its directly attached enforcement clause, not in a §9 preamble annotation, guard title, or separate parenthetical; a reader of §9 alone can confirm the bidirectional naming relationship without consulting CONTRACT B; C-45 FULL required.
- **Partial (1):** §9 acknowledges its enforcement role with respect to the value requirement defined in CONTRACT B but does not explicitly frame the acknowledgment as "the enforcement site named in CONTRACT B's self-sufficiency declaration" — e.g., states "§9 enforces the value requirement defined in CONTRACT B" without naming itself as the specific site CONTRACT B's declaration points to; or the acknowledgment uses CONTRACT B's structural label but places the reverse-confirmation statement in a §9 preamble annotation rather than inside the compliance obligation body; C-45 FULL required.
- **Fail (0):** §9 does not contain any statement acknowledging it is the enforcement site named in CONTRACT B's self-sufficiency declaration; the reverse triangle confirmation from the §9 entry point is absent; or C-45 FULL is not satisfied.

---

### C-48 — CONSISTENCY AUDIT CLAUSE closing text specifies the verification algorithm
**Category:** correctness

CONTRACT B's CONSISTENCY AUDIT CLAUSE declares its own compliance with each named structural prerequisite and identifies the intra-block location where each is satisfied (C-46). C-48 tests whether the clause additionally closes with explicit machine-verifiability framing — a statement specifying the verification algorithm: the procedure by which a reader can confirm that the self-referential satisfaction confirmations are correct using only the clause text and the named intra-block locations. Without C-48, the CONSISTENCY AUDIT CLAUSE asserts satisfaction and provides location pointers but leaves the checking procedure implicit; a reader must infer that inspecting the named location confirms the claim. With C-48, the clause explicitly states the verification procedure ("machine-detectable as such by verifying whether the requirement is present at the named location in this block"), converting an assertion-plus-pointer pair into a complete, self-describing verification unit: claim + location + algorithm. The algorithm statement makes CONTRACT B not merely self-auditing (C-46) but self-instructing — it tells the reader exactly how to perform the audit, not just what the audit covers. C-48 depends on C-46 FULL — intra-block location pointers must exist before a verification algorithm can be specified for them.

- **Full (2):** CONTRACT B's CONSISTENCY AUDIT CLAUSE includes a closing statement — formally placed at or after the last satisfaction confirmation entry — that specifies the verification algorithm: it states that compliance with the named prerequisites can be confirmed by verifying whether each named requirement is present at the named intra-block location; the algorithm statement is located inside the CONSISTENCY AUDIT CLAUSE body or as a directly attached closing line of that body, not in a separate annotation outside the CONTRACT B block; the statement is procedurally explicit — it names the checking action ("verify," "confirm by checking," or equivalent) and the operand ("the named location in this block") — rather than merely asserting verifiability without specifying how; a reader can derive the complete audit procedure from the clause text alone without consulting any source outside the CONTRACT B block; C-46 FULL required.
- **Partial (1):** The CONSISTENCY AUDIT CLAUSE includes machine-verifiability language but the statement is assertive rather than procedural — declares that the block is machine-verifiable ("this audit is machine-completeable," "this block is self-consistent") without specifying the checking action and operand; or the algorithm statement names the verification action but omits the operand (names what to do but not where to do it); or a complete algorithm statement is present but located in a closing annotation outside the CONSISTENCY AUDIT CLAUSE body rather than as a structural part of the clause; C-46 FULL required.
- **Fail (0):** The CONSISTENCY AUDIT CLAUSE does not include a verification algorithm specification; the checking procedure must be inferred from the assertion-plus-pointer structure; or C-46 FULL is not satisfied.

---

**Orthogonality (C-47, C-48):** C-47 tests whether §9 confirms itself as the enforcement site named in CONTRACT B's self-sufficiency declaration (§9-side reverse triangle confirmation, extending C-45). C-48 tests whether the CONSISTENCY AUDIT CLAUSE closing text specifies the verification algorithm (extending C-46). C-47 and C-48 are independent of each other: a variate can earn C-47 without earning C-48 (§9 provides reverse confirmation, but the CONSISTENCY AUDIT CLAUSE lacks algorithm framing) and vice versa (the CONSISTENCY AUDIT CLAUSE has algorithm framing, but §9 does not provide reverse confirmation). C-47 depends on C-45 FULL; C-48 depends on C-46 FULL. These are data dependencies, not scoring interactions. The pair (C-47, C-48) is further independent from each other's prerequisite chains: C-47 FULL requires C-45 FULL (and transitively C-43 FULL, C-42 FULL); C-48 FULL requires C-46 FULL (and transitively C-44 FULL, C-42 FULL). A variate targeting C-47 must have the full CONTRACT B→§9 triangle leg in place; a variate targeting C-48 must have the full self-confirming prerequisite structure in place.

---

## Scoring formula

```
score = (sum of aspirational points earned) / 80 * 10
```

Aspirational criteria: C-09 through C-48 (40 criteria × 2 points each = 80 max).
Essential criteria (C-01–C-08): pass/fail; any FAIL disqualifies the variate entirely.

| Aspirational band | Points | Score ceiling |
|-------------------|--------|---------------|
| C-09–C-36 (established through R14) | 56 max | 7.00 |
| C-37–C-39 (R16 additions) | 6 max | +0.75 |
| C-40–C-42 (R17 additions) | 6 max | +0.75 |
| C-43–C-44 (R18 additions) | 4 max | +0.50 |
| C-45–C-46 (R19 additions) | 4 max | +0.50 |
| C-47–C-48 (R20 additions) | 4 max | +0.50 |
| **Total** | **80 max** | **10.00** |
