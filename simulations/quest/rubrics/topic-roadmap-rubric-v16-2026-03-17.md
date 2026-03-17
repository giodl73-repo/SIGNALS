Reading the scorecard carefully, I identify three new excellence patterns from Round 15 — one per variate axis — that exceed what C-34/C-35/C-36 already test:

- **V-01** (C-34 axis): the mutual necessity assertion is **directional** — "LEVEL 1 does not protect against LEVEL 2" — naming the specific protection gap, not merely asserting co-requirement
- **V-02** (C-35 axis): the SECTION SCOPE navigation note **cross-references a formal guard label by its complete title**, creating bidirectional navigation: guard → scope (via enumeration) and scope → guard (via named label)
- **V-03** (C-36 axis): CONTRACT B **names the exact literal column value string** for the compliant state ("Bias blocked by guard"), enabling value verification — not just absence detection — from the CONTRACT block alone

These become C-37, C-38, C-39. Denominator expands from 56 to 62.

---

# Scoring Rubric — topic-roadmap (topic-plan) v16

## What changed

| Change | Detail |
|--------|--------|
| Version bump | 15 → 16 |
| Formula denominator | `/56 * 10` → `/62 * 10` (31 aspirational × 2 = 62 max) |
| Aspirational range | C-09–C-36 → C-09–C-39 |
| **C-37 added** | PROPOSAL BIAS AUDIT directional protection gap assertion |
| **C-38 added** | SECTION SCOPE guard-label cross-reference |
| **C-39 added** | CONTRACT B exact compliant column value string |

---

## Three new aspirational criteria

### C-37 — PROPOSAL BIAS AUDIT directional protection gap assertion
**Category:** safety

The mutual necessity assertion in the PROPOSAL BIAS AUDIT guard names the directional protection gap explicitly: it states not only that both levels are required, but that LEVEL 1 does not protect against LEVEL 2 — making the hierarchical insufficiency a referenceable claim. C-34 tests whether a mutual necessity assertion is present and whether both failure modes carry formal titled labels; C-37 tests whether that assertion is **directional** — identifying the specific gap (LEVEL 1 protection is necessary but insufficient to close LEVEL 2) rather than asserting mere co-requirement. A directional assertion enables a reader to understand WHY the hierarchy exists, not only THAT it exists, and allows CONTRACT or SECTION SCOPE to cite the gap by name.

- **Full (2):** Mutual necessity assertion explicitly states that LEVEL 1 does not protect against LEVEL 2 (or equivalent directional gap language identifying the specific insufficiency); assertion names the protection gap, not merely the co-requirement; directional statement is co-located in the PROPOSAL BIAS AUDIT guard body.
- **Partial (1):** Directional language is present but implicit (e.g., "LEVEL 2 addresses a more sophisticated failure") without the explicit LEVEL 1 → LEVEL 2 protection-absence formulation; or directional assertion appears in a preamble annotation outside the guard body rather than co-located with the formal labels.
- **Fail (0):** Assertion states co-requirement only ("both are required," "LEVEL 1 and LEVEL 2 are both necessary") without identifying the directional protection gap; or C-34 fails.

### C-38 — SECTION SCOPE guard-label cross-reference
**Category:** correctness

The SECTION SCOPE auditor navigation note cross-references at least one formal guard label (LEVEL 1 or LEVEL 2 title from C-34) by its complete formal title — creating bidirectional navigation: the guard names a referenceable label (C-34), and the scope navigation note cites that label by name (C-38), enabling an auditor to traverse from the scope declaration directly to the specific guard level without traversing phase content. C-35 tests whether the SECTION SCOPE includes a navigation note that identifies the enumeration item by number or label; C-38 tests whether that navigation note also names the formal guard label by its complete title from C-34, so that the scope-to-guard traversal path is anchored to a named artifact, not merely to an enumeration position.

- **Full (2):** SECTION SCOPE navigation note cites at least one formal guard label (e.g., "LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE") by its complete formal title as defined in the PROPOSAL BIAS AUDIT guard; auditor can traverse from scope navigation note to the specific guard level using the label alone.
- **Partial (1):** Navigation note references the guard labels in general terms (e.g., "the labeled failure modes," "the LEVEL designations") without citing a specific complete formal title; or cites an abbreviated or informal version of the label (e.g., "LEVEL 2" without its descriptive title).
- **Fail (0):** Navigation note does not reference the formal guard labels at all; or C-35 fails.

### C-39 — CONTRACT B exact compliant column value string
**Category:** correctness

CONTRACT B names the exact literal string that constitutes the compliant column value — the specific text that appears in the column when the bias guard is satisfied (e.g., "Bias blocked by guard") — enabling a scorer to verify not only that the column exists (C-36) but that it contains the correct value, from the CONTRACT block alone without reading phase content. C-36 tests whether CONTRACT B includes violation-detection language for column absence; C-39 tests whether CONTRACT B further specifies the exact compliant value string, making column-value verification possible from the CONTRACT block. This is distinct from absence detection: a column that exists but contains an incorrect value is a schema conformance failure; C-39 makes that failure detectable from the CONTRACT alone.

- **Full (2):** CONTRACT B names the exact literal string for the compliant column value (specific text such as "Bias blocked by guard"); a scorer reading only the CONTRACT block can verify both that the column exists AND that it contains the correct value; the string is quoted or delimited so that approximate matches are distinguishable from exact matches.
- **Partial (1):** CONTRACT B implies a standard value or provides a partial string (e.g., "bias status," "blocked by...") without stating the exact literal; or the exact value string appears in a phase body annotation or preamble rather than in the CONTRACT block itself.
- **Fail (0):** CONTRACT B does not name a specific column value string for the compliant case; violation-detection language covers only column presence/absence; or C-36 fails.

---

**Orthogonality:** C-37 tests directional precision of the mutual necessity assertion (extends C-34). C-38 tests bidirectional navigation by guard-label citation in the scope note (extends C-35). C-39 tests compliant value specification in CONTRACT B (extends C-36). All three are independent: C-37 FAIL / C-38 PASS / C-39 PASS is achievable (scope and contract done, guard assertion non-directional). C-38 depends on C-34 FULL being present (guard labels must exist to cite), so C-34 FAIL entails C-38 FAIL; this is a data dependency, not a scoring interaction — a single-axis variate targeting only C-38 without satisfying C-34 cannot achieve C-38 FULL.

**R15 score ceiling under v16:** V-01, V-02, and V-03 (each 48/56 = 8.57 under v15) score 50/62 = 8.06 under v16: V-01 picks up C-37=2 (directional assertion present: "LEVEL 1 does not protect against LEVEL 2") but C-38=0 (scope unchanged, no guard-label citation) and C-39=0 (CONTRACT B uses generic "schema contract violation" language, not the exact column value string). V-04 scores 54/62 = 8.71 (adding C-37=2, C-38=2 from its cross-citation, C-39=0). V-05 (56/56 = 10.00 under v15) scores 62/62 = 10.00 under v16: V-05's C-34 evidence supplies the directional assertion (C-37=2), V-05's C-35 cross-reference cites "LEVEL 2: MOTIVATED REASONING…" by full title (C-38=2), and V-05's C-36 CONTRACT B names "Bias blocked by guard" as the exact literal value (C-39=2). An R16 variate targeting all three simultaneously achieves 56 (C-09–C-36) + 6 (C-37–C-39) = 62/62 = 10.00.

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

*(C-03–C-08 inherited unchanged from v15)*

---

## Criteria — Aspirational (C-09–C-39)

*(C-09–C-30 inherited unchanged from v15)*

---

### C-31 — PROPOSAL BIAS AUDIT distinguishes two failure modes
**Category:** safety

*(Inherited unchanged from v15)*

---

### C-32 — SECTION SCOPE updated for row-level bias labeling
**Category:** correctness

*(Inherited unchanged from v15)*

---

### C-33 — OUTPUT SCHEMA CONTRACT standalone pre-Phase-1 position
**Category:** correctness

*(Inherited unchanged from v15)*

---

### C-34 — PROPOSAL BIAS AUDIT failure mode label precision
**Category:** safety

The PROPOSAL BIAS AUDIT guard names each of the two failure modes with a formal descriptive title (e.g., LEVEL 1: SYSTEMIC PHASE STRUCTURE BIAS, LEVEL 2: MOTIVATED REASONING AT THE INDIVIDUAL PROPOSAL DECISION SURFACE), making each failure mode referenceable by name from other document sections. C-31 tests whether the guard distinguishes and explains the two failure modes; C-34 tests whether each failure mode carries a formal title that enables cross-referencing — turning explanatory prose into a named reference artifact that the CONTRACT or SECTION SCOPE can cite by label.

- **Full (2):** Both failure modes carry formal descriptive titles co-located in the PROPOSAL BIAS AUDIT guard text; titles are specific enough to be cited from the CONTRACT or SECTION SCOPE by name alone.
- **Partial (1):** One failure mode named with a formal title; the other described without one; or formal titles present but located outside the guard body (e.g., in a preamble annotation only).
- **Fail (0):** Neither failure mode carries a formal named title; guard text describes but does not formally label the two failure modes.

---

### C-35 — SECTION SCOPE auditor navigation note
**Category:** correctness

The Phase 6 SECTION SCOPE declaration includes an explicit auditor navigation note: a sentence confirming that a C-24 auditor checking Phase 6's declared scope can locate the row-level bias labeling entry from the scope declaration without traversing phase content. C-32 tests whether the scope is updated to include row-level bias labeling; C-35 tests whether that update is designed to serve auditor navigation — i.e., whether the scope declaration itself tells the auditor where to look and what to look for, rather than merely asserting the labeling's presence.

- **Full (2):** SECTION SCOPE includes an explicit navigation note stating that a C-24 auditor verifying row-level bias labeling finds it enumerated in the scope declaration; note identifies the enumeration item by number or label.
- **Partial (1):** SECTION SCOPE references C-24 or auditor navigation in passing (e.g., a parenthetical remark) but does not provide a full navigation note; or the navigation note appears in a preamble outside the SECTION SCOPE declaration itself.
- **Fail (0):** No auditor navigation note in the SECTION SCOPE declaration; or SECTION SCOPE fails C-32.

---

### C-36 — CONTRACT at absolute document-first position
**Category:** correctness

The OUTPUT SCHEMA CONTRACT is the absolute first section of the document — positioned before the INERTIA COMPETITOR DECLARATION — and satisfies three additional requirements: (a) a self-referential confirmation statement (e.g., "No file read instruction appears before this CONTRACT"), (b) CONTRACT A names all four consequence field sites: Phase 5 table column, Phase 6a column, Phase 6b column, and Phase 5 exit criterion, and (c) CONTRACT B names "Bias blocked by guard" with violation-detection language enabling a scorer to detect column absence from the CONTRACT block alone, without reading any phase content. C-33 tests standalone pre-Phase-1 positioning; C-36 tests whether the CONTRACT is the absolute first reader-encountered content — before all guards including INERTIA COMPETITOR DECLARATION — and whether it is fully self-sufficient for violation detection.

- **Full (2):** CONTRACT is the first section in the document, preceding INERTIA COMPETITOR DECLARATION; self-referential confirmation statement present; CONTRACT A names all four consequence field sites; CONTRACT B includes violation-detection language.
- **Partial (1):** CONTRACT precedes INERTIA COMPETITOR DECLARATION but is missing exactly one of the three additional requirements (self-referential statement, four-site CONTRACT A, or violation-detection language in CONTRACT B).
- **Fail (0):** CONTRACT does not precede INERTIA COMPETITOR DECLARATION; or C-33 fails.

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

## Scoring formula

```
score = (points_earned / 62) * 10
```

- Essential criteria (C-01–C-08): each FAIL voids the rubric score (score = 0)
- Aspirational criteria (C-09–C-39): 31 criteria × 2 pts = 62 pts maximum
- Each aspirational criterion: Full = 2, Partial = 1, Fail = 0
