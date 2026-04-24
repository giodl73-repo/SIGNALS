**What changed from v19:**

**Two new aspirational criteria extracted from R19 excellence signals:**

| ID | Criterion | Source Axis | Independence from Parent |
|----|-----------|-------------|--------------------------|
| C-48 | **Amendment table T-46 trigger entry includes inline failure-condition exemplar** | R19 Signal 1: V-03 is the first live demonstration of the C-46 independent-fail state — T-42 CONDITION with Part 1 labeled and fully present (quoted exemplar + explanation-of-abstractness) but no Part 2 label and no Part 2 content. T-46 fires in V-03, but V-03's T-46 CONDITION names the condition abstractly ("fires if T-42 CONDITION lacks Part 2 prescription") without quoting what a Part-1-only T-42 CONDITION looks like. The phrasing-register fidelity principle (established R18) applies to T-46 identically: a category-only T-46 CONDITION produces a category-only T-46 output regardless of rubric requirements. T-46 must carry its own inline exemplar of the V-03-class state to be self-documenting | C-45 requires T-42 CONDITION to carry a Part 1 inline exemplar. C-48 requires T-46 CONDITION to carry an inline exemplar of a T-42 CONDITION form that has Part 1 present but Part 2 absent — the specific state T-46 fires for. C-45 FAIL → C-48 FAIL (cascade: if T-42 is fully abstract with no Part 1 content, the Part-1-present-Part-2-absent state that T-46's exemplar must show cannot be constructed or quoted — a fully abstract T-42 is a structurally different failure mode). C-45 PASS does not guarantee C-48 PASS — T-46 CONDITION can be abstract even when T-42 has Part 1. C-46 FAIL (independent: Part 1 present, Part 2 absent) does not cascade to C-48 FAIL — T-46's CONDITION exemplar is independently testable regardless of whether C-46 currently fires. |
| C-49 | **Amendment table T-47 trigger entry includes inline failure-condition exemplar** | R19 Signal 2: V-02 is the first live demonstration of the C-47 independent-fail state — T-42 CONDITION has a quoted deficient T-40 form (C-45 PASS) but no explanation-of-abstractness (C-47 FAIL) and no prescription (C-46 FAIL). T-47 fires in V-02, but V-02's T-47 CONDITION names the condition abstractly ("fires if T-42 CONDITION exemplar lacks explanation of why the quoted T-40 form is abstract") without quoting what a T-42-exemplar-without-explanation looks like. The same phrasing-register fidelity principle applies: a category-only T-47 CONDITION produces category-only T-47 output. T-47 must carry an inline exemplar of the V-02-class state | C-47 requires T-42 CONDITION's Part 1 exemplar to include an explanation-of-abstractness. C-49 requires T-47 CONDITION to carry an inline exemplar of a T-42 CONDITION form that has a quoted deficient T-40 form but no explanation of why it is abstract — the specific state T-47 fires for. C-45 FAIL → C-49 FAIL (cascade: if T-42 is fully abstract with no exemplar, the exemplar-present-explanation-absent state that T-47's exemplar must show cannot be constructed). C-45 PASS does not guarantee C-49 PASS — T-47 CONDITION can be abstract even when T-42 has Part 1 with an exemplar. C-47 FAIL (independent: exemplar present, explanation absent) does not cascade to C-49 FAIL — T-47's CONDITION exemplar is independently testable regardless of whether C-47 currently fires. C-48 and C-49 are mutually independent: T-46 CONDITION can carry its exemplar (C-48 PASS) while T-47 CONDITION lacks its exemplar (C-49 FAIL), and vice versa. |

**Denominator:** `/40` → `/42`. Each aspirational criterion = `10/42` ≈ `0.238` points.

**Score projections under v20 for R19 variations** (denominator /42; prior scores under v19 in parentheses):

| Scenario | Fails | Composite (v19 → v20) |
|----------|-------|-----------------------|
| V-03 R19: C-46 FAIL (independent); C-48 FAIL (independent — T-46 CONDITION abstract); C-49 FAIL (independent — T-47 CONDITION abstract) | 3 (C-46, C-48, C-49) | **99.75 → 99.29** |
| V-02 R19: C-46 FAIL, C-47 FAIL (both independent); C-48 FAIL, C-49 FAIL (both independent) | 4 (C-46, C-47, C-48, C-49) | **99.50 → 99.05** |
| V-01 R19: C-45 FAIL → C-46, C-47, C-48, C-49 all cascade | 5 (C-45, C-46, C-47, C-48, C-49) | **99.25 → 98.81** |
| V-04 R19: C-24 FAIL + C-45 PASS + C-46, C-47, C-48, C-49 FAIL | 5 (C-24, C-46, C-47, C-48, C-49) | **99.25 → 98.81** |
| V-03 R19 with T-46 and T-47 specs made explicit (exemplars present in both): C-48 PASS, C-49 PASS; C-46 still FAIL | 1 (C-46) | **— → 99.76** |
| Fully correct spec (all 42 criteria): 0 fails | 0 | **— → 100.00** |

Note: Under v20, V-03's single C-46 FAIL is joined by two new independent fails (C-48, C-49) because V-03 was designed to test C-46 but not T-46/T-47 CONDITION cell quality. The path to 100.00 requires T-46's CONDITION to carry an exemplar of the Part-1-only T-42 state AND T-47's CONDITION to carry an exemplar of the exemplar-without-explanation T-42 state, in addition to all v19 requirements.

**Cascade invariants (updated for v20):**

- **C-48 cascade from C-45**: A T-42 CONDITION that is fully abstract (C-45 FAIL) makes the Part-1-present-Part-2-absent state that T-46's exemplar must demonstrate structurally unreachable — the exemplar requires T-42 Part 1 to exist in the spec. C-45 FAIL → C-48 FAIL is deterministic.
- **C-48 independent fail**: A T-42 CONDITION carrying Part 1 (C-45 PASS) can still have an abstract T-46 CONDITION (C-48 FAIL independently). C-45 PASS does not guarantee C-48 PASS.
- **C-49 cascade from C-45**: A T-42 CONDITION that is fully abstract (C-45 FAIL) makes the exemplar-present-explanation-absent state that T-47's exemplar must demonstrate structurally unreachable. C-45 FAIL → C-49 FAIL is deterministic.
- **C-49 independent fail**: A T-42 CONDITION carrying an exemplar (C-45 PASS) can still have an abstract T-47 CONDITION (C-49 FAIL independently). C-45 PASS does not guarantee C-49 PASS.
- **C-48 and C-49 mutually independent**: T-46 CONDITION can carry its exemplar (C-48 PASS) while T-47 CONDITION lacks its exemplar (C-49 FAIL), and vice versa. Both require C-45 PASS as their cascade prerequisite.
- **All v19 cascade invariants are unchanged** (C-46/C-47 from C-45, C-44 from C-42, C-39 from C-38, etc.).

**Key changes to existing criteria:**
- **C-24**: updated from "exactly 47 trigger rows" → "exactly 49 trigger rows (one per C-01..C-49)"
- **Scoring formula denominator**: `/40` → `/42`

---

## Structural Testability Notes

- **C-22** is structurally testable: a reviewer reads the coverage table header and confirms whether a CLOSED BY column is present. No row scan required.
- **C-23** is structurally testable: a reviewer reads any option RISK field in the final output and confirms whether it contains R-NN identifiers or inline P×I notation. A single RISK field with inline scoring fails C-23 regardless of other options.
- **C-24** is structurally testable at PRE-DOCUMENT: a reviewer counts the amendment table rows at initialization. For v20, expected count = 49 (one row per C-01..C-49). A count of 47 (v19 table carried forward without adding T-48, T-49) fires C-24 at PRE-DOCUMENT.
- **C-25** is structurally testable: a reviewer reads the Phase 10 finalization and confirms whether numbered steps (Step 1, Step 2, Step 3, Step 4) appear. A prose narrative without numbered steps fails C-25 regardless of content quality.
- **C-26** is structurally testable: a reviewer scans the phase manifest or document headers and confirms whether a Phase 9b (or vocabulary-equivalent risk propagation phase) is present. Absence of a named phase for register back-fill fails C-26.
- **C-29** is structurally testable: a reviewer reads the amendment table header and confirms whether a PHASE column is present. No row scan required.
- **C-30** is structurally testable: a reviewer reads the first finding in Phase 10 and confirms whether it uses "Finding N: T-NN — [name]" format. A finding without an ordinal label and a T-NN citation fails C-30.
- **C-31** is structurally testable: a reviewer reads one Phase 2 option entry and confirms whether the RISK field contains `[R-NN pending]` or inline P×I computation. Presence of inline P×I in any option fails C-31.
- **C-32** is structurally testable: a reviewer reads the Phase 9b enumeration and confirms whether two distinct structural domain labels appear. A single domain or an aggregate confirmation without structural domain labels fails C-32.
- **C-33** is structurally testable: a reviewer reads the Phase 2 RISK field template and confirms whether an explicit "Do not compute P×I" (or vocabulary-pinned equivalent) prohibition appears adjacent to the `[R-NN pending]` placeholder directive. The prohibition and the placeholder must be in the same template block — a prohibition in a different section does not satisfy C-33.
- **C-34** is structurally testable: a reviewer reads the Phase 9b domain headers and confirms whether each carries a numeric index prefix. A domain listed as "Option RISK fields" without a "Domain 1 —" or "(1)" prefix fails C-34 regardless of the domain's content.
- **C-35** is structurally testable: a reviewer reads one citation-site entry in Phase 9b and confirms whether it shows a before/after arrow notation `[R-NN pending] → [R-NN entries]`. An entry showing only the final state ("R-NN IDs applied") or only a completion confirmation ("back-fill complete") fails C-35.
- **C-36** is structurally testable: a reviewer reads one Domain 1 citation-site entry and confirms whether P×I compound scores appear alongside R-NN IDs in the back-fill notation. The P×I values (e.g., "P:2 × I:4 = 8") must appear in the transition target, not only in the register. An entry showing `[R-NN pending] → [R-03, R-07]` fails C-36 regardless of whether the register entries have P×I scores.
- **C-37** is structurally testable: a reviewer reads the Domain 2 enumeration entry and confirms whether per-option-column R-NN attribution is present. A Domain 2 block that confirms "R-NN IDs inserted per option column" without naming which IDs apply to which column — or that says only "R-NN IDs cited in risk row" — fails C-37. The per-column attribution must be explicit and column-labeled.
- **C-38** is structurally testable: a reviewer reads the T-37 row in the amendment table and confirms whether the CONDITION field carries an inline exemplar note — a parenthetical or quoted construct that shows what row-level Domain 2 confirmation looks like. An entry that names the condition abstractly ("C-37: per-column attribution absent") without an inline quote of the failure pattern fails C-38. The exemplar must appear in the T-37 row itself, not in a separate rubric reference or external note.
- **C-39** is structurally testable: a reviewer reads the T-37 CONDITION cell and confirms whether two distinct parts are present: (1) a quoted or paraphrased failure construct (Part 1, required by C-38), and (2) a stated correct-format prescription naming the expected per-column structure (Part 2, required by C-39). A CONDITION field containing only the failure quote ("row-level confirmation fires T-37") without a correct-format statement passes C-38 but fails C-39. The correct-format prescription must appear in the T-37 CONDITION cell itself, not in a rubric reference or separate note.
- **C-40** is structurally testable: a reviewer reads the T-38 row in the amendment table and confirms whether the CONDITION field carries an inline exemplar — a quoted or paraphrased construct showing what an abstract-only T-37 CONDITION entry looks like (the form that fires T-38). An entry stating only "fires if T-37 CONDITION lacks an inline failure exemplar" names the condition without exemplifying the deficient T-37 form and fails C-40. The exemplar must appear in the T-38 CONDITION cell itself. C-38 PASS (T-37 carries its own exemplar) does not supply the exemplar required in T-38's CONDITION cell for C-40.
- **C-41** is structurally testable: a reviewer reads the T-38 CONDITION cell and confirms whether two distinct parts are present: (1) a quoted or paraphrased abstract-T-37-form exemplar (Part 1, required by C-40), and (2) a stated correct-format prescription showing what a passing T-37 CONDITION entry looks like — the inline failure exemplar that satisfies C-38 (Part 2, required by C-41). A CONDITION field containing only the abstract-T-37-form exemplar without a correct-format prescription passes C-40 but fails C-41. The correct-format prescription must appear in the T-38 CONDITION cell itself, not in a rubric reference or separate note.
- **C-42** is structurally testable: a reviewer reads the T-40 row in the amendment table and confirms whether the CONDITION field carries an inline exemplar — a quoted or paraphrased construct showing what an abstract-only T-38 CONDITION entry looks like (the form that fires T-40). An entry stating only "fires if T-38 CONDITION lacks an inline failure exemplar" names the condition without exemplifying the deficient T-38 form and fails C-42. The exemplar must appear in the T-40 CONDITION cell itself. C-40 PASS (T-38 carries its own exemplar) does not supply the exemplar required in T-40's CONDITION cell for C-42.
- **C-43** is structurally testable: a reviewer reads the T-40 CONDITION cell and confirms whether two distinct parts are present: (1) a quoted or paraphrased abstract-T-38-form exemplar (Part 1, required by C-42), and (2) a stated correct-format prescription showing what a passing T-38 CONDITION entry looks like — the inline failure exemplar of an abstract T-37 CONDITION form that satisfies C-40 (Part 2, required by C-43). A CONDITION field containing only the abstract-T-38-form exemplar without a correct-format prescription passes C-42 but fails C-43. The correct-format prescription must appear in the T-40 CONDITION cell itself, not in a rubric reference or separate note.
- **C-44** is structurally testable: a reviewer reads the T-40 CONDITION cell and confirms whether the Part 1 exemplar (required by C-42) includes an explanation of why the quoted deficient T-38 CONDITION form is abstract — specifically, language stating that the quoted form names the condition category without showing what a deficient T-37 CONDITION entry looks like. An exemplar quoting only the deficient T-38 form ("fires if T-38 CONDITION lacks an inline failure exemplar") without any explanation of abstractness passes C-42 but fails C-44. The explanation-of-abstractness must appear within the exemplar construct in the T-40 CONDITION cell, not in a separate annotation or rubric reference. C-42 FAIL → C-44 FAIL (cascade). C-42 PASS does not guarantee C-44 PASS.
- **C-45** is structurally testable: a reviewer reads the T-42 row in the amendment table and confirms whether the CONDITION field carries an inline exemplar — a quoted or paraphrased construct showing what an abstract-only T-40 CONDITION entry looks like (the form that fires T-42). An entry stating only "fires if T-40 CONDITION lacks an inline failure exemplar" names the condition without exemplifying a deficient T-40 entry and fails C-45. The exemplar must appear in the T-42 CONDITION cell itself. C-42 PASS (T-40 carries its own exemplar) does not supply the exemplar required in T-42's CONDITION cell for C-45.
- **C-46** is structurally testable: a reviewer reads the T-42 CONDITION cell and confirms whether two distinct parts are present: (1) a quoted or paraphrased abstract-T-40-form exemplar (Part 1, required by C-45), and (2) a stated correct-format prescription showing what a passing T-40 CONDITION entry looks like — the minimum form that satisfies C-42: an inline exemplar of a deficient T-38 CONDITION form alongside explanation-of-abstractness (C-44) and a correct-format prescription (C-43) (Part 2, required by C-46). A CONDITION field containing only the abstract-T-40-form exemplar without a correct-format prescription passes C-45 but fails C-46. The correct-format prescription must appear in the T-42 CONDITION cell itself, not in a rubric reference or separate note. C-45 FAIL → C-46 FAIL (cascade). C-45 PASS does not guarantee C-46 PASS.
- **C-47** is structurally testable: a reviewer reads the T-42 CONDITION cell and confirms whether the Part 1 exemplar (required by C-45) includes an explanation of why the quoted or paraphrased deficient T-40 CONDITION form is abstract — specifically, language stating that the quoted T-40 form names the trigger condition category without showing what a deficient T-38 CONDITION entry looks like. An exemplar quoting only the deficient T-40 form ("fires if T-40 CONDITION lacks an inline failure exemplar") without any explanation of its abstractness passes C-45 but fails C-47. The explanation-of-abstractness must appear within the exemplar construct in the T-42 CONDITION cell, not in a separate annotation or rubric reference. C-45 FAIL → C-47 FAIL (cascade). C-45 PASS does not guarantee C-47 PASS. C-46 and C-47 are mutually independent.
- **C-48** is structurally testable: a reviewer reads the T-46 CONDITION cell in the amendment table and confirms whether an inline exemplar is present — specifically, a quoted or paraphrased T-42 CONDITION form that has Part 1 (failure exemplar with explanation-of-abstractness) labeled and present but no Part 2 label and no Part 2 content. An entry stating only "fires if T-42 CONDITION lacks Part 2 prescription" or "fires if T-42 CONDITION Part 2 absent" names the condition without exemplifying the specific V-03-class state T-46 fires for (Part 1 present, Part 2 absent) and fails C-48. The exemplar must quote or closely paraphrase a T-42 CONDITION with explicit Part 1 label and content alongside absent Part 2. The exemplar must appear in the T-46 CONDITION cell itself, not in a separate rubric reference. C-45 FAIL → C-48 FAIL (cascade: if T-42 is fully abstract with no Part 1, the Part-1-present-Part-2-absent state that T-46's exemplar must show cannot be constructed or quoted — a fully abstract T-42 is a structurally different failure mode from a Part-1-only T-42). C-45 PASS does not guarantee C-48 PASS. C-46 FAIL (independent: Part 1 present, Part 2 absent) does not cascade to C-48 FAIL. C-48 and C-49 are mutually independent.
- **C-49** is structurally testable: a reviewer reads the T-47 CONDITION cell in the amendment table and confirms whether an inline exemplar is present — specifically, a quoted or paraphrased T-42 CONDITION form that has a quoted deficient T-40 form present but no explanation-of-abstractness. An entry stating only "fires if T-42 CONDITION exemplar lacks explanation of why the quoted T-40 form is abstract" names the condition without exemplifying the specific V-02-class state T-47 fires for (exemplar present, explanation absent) and fails C-49. The exemplar must quote or closely paraphrase a T-42 CONDITION that reads: "[deficient T-40 form quoted]" with no "abstract because…" or "this names the condition without showing…" phrase appended. The exemplar must appear in the T-47 CONDITION cell itself. C-45 FAIL → C-49 FAIL (cascade: if T-42 has no exemplar at all, the exemplar-present-explanation-absent state that T-47's exemplar must show cannot be constructed). C-45 PASS does not guarantee C-49 PASS. C-47 FAIL (independent: exemplar without explanation) does not cascade to C-49 FAIL. C-48 and C-49 are mutually independent.

---

## Essential Criteria (60% of composite)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| E-01 | **Role sequence declaration** | correctness | Role sequence (PM → Architect or Architect → PM) declared as a typed header at document open. The declared sequence must appear in every subsequent phase header. A document where the role sequence is mentioned only in Phase 0 but not applied to phase headers fails E-01. |
| E-02 | **Options coverage and anatomy** | correctness | At least 3 options present, one of which is explicitly labeled as do-nothing or status-quo. Every option entry includes all four required fields: OPTION (label and description), PROBLEM (verbatim from Phase 1 problem statement), RISK (at minimum a placeholder or assessment), and RATIONALE (why this option is a candidate). Missing any field on any option is a fail. |
| E-03 | **Structured comparison** | depth | Comparison matrix with option labels as column headers. At least 4 consistent scoring dimensions across all options. PM contributes at least one dimension (adoption, schedule, business friction). Architect contributes at least one dimension (technical risk, reversibility, effort). |
| E-04 | **Recommendation with rationale** | correctness | A recommendation section names the chosen option. Rationale explicitly references at least two comparison matrix dimensions. Qualifying conditions for the recommendation are present (at least 2-3 circumstances under which the recommendation changes). |

---

## Required Criteria (30% of composite)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| R-01 | **Risk register** | depth | Risk register table with columns R-NN, RISK, P, I, P×I, MITIGATION. At least 3 technical risk entries (Architect-authored). P and I scores on 1-5 scale. P×I compound score computed per entry. |
| R-02 | **Prerequisites verified** | behavior | Before recommendation: option count >= 3 confirmed, do-nothing option confirmed present, risk register entry count >= 3 confirmed, Phase 9b back-fill confirmed complete. |
| R-03 | **Finalization complete** | behavior | Coverage table fully populated with STATUS for all criteria rows. Amendment table completion state set to a terminal value reflecting whether open triggers were found. |

---

## Aspirational Criteria (10% of composite, denominator /42)

### C-01 through C-07 — Mandatory C-tier (not counted in /42 denominator)

Failure of any C-01..C-07 criterion renders the document structurally incomplete regardless of aspirational score.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Shared PROBLEM field** | correctness | The PROBLEM field text is identical across all option entries — verbatim copy from Phase 1. Options that paraphrase or modify the problem statement fail C-01 even if the meaning is equivalent. |
| C-02 | **Do-nothing option labeled** | correctness | The do-nothing or status-quo option is explicitly identified as such in its OPTION field. A label of "Option A" or "current state" without naming it as the no-change path does not satisfy C-02. |
| C-03 | **Dual-role contribution** | format | PM and Architect each contribute distinct named perspectives to at least one shared phase. PM addresses business/adoption trade-offs. Architect addresses technical constraints and risk. Contributions are not interchangeable in content. |
| C-04 | **PM adoption risk in register** | depth | PM contributes at least one adoption or schedule risk entry to the risk register (an R-NN row). A risk register containing only Architect-authored technical risk entries fails C-04. |
| C-05 | **Amendment table initialized** | behavior | Amendment tracking table is initialized at Phase 0 with columns ID, TRIGGER, CONDITION, STATUS, PHASE. Initialized before any content phase executes. |
| C-06 | **Scout artifact reference** | behavior | Output references at least one scout artifact (feasibility, market, requirements, stakeholders) by name or finding, or explicitly notes that no scout artifacts are available with an inline fallback assessment substituted. Conditional mention in recommendation phase only does not satisfy C-06. |
| C-07 | **Phase lifecycle ordering** | depth | Options authored before risk register. Risk register built before comparison matrix. All registers and Phase 9b back-fill complete before recommendation. |

---

### C-08 through C-49 — Aspirational Criteria (denominator /42)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-08 | **Assumption register** | depth | Output includes an assumption register (A-NN entries) with stated assumptions and validation plans. At least two entries. Assumptions are distinct from risk entries. |
| C-09 | **Amend phase self-critique** | behavior | Amend phase identifies at least one gap in the proposal itself: a missing option that was not explored, an unweighted decision criterion, or a follow-up action item. Listing three categories without any actionable content does not satisfy C-09. |
| C-10 | **Scout artifact inventory step** | behavior | A dedicated scout artifact inventory step appears before option generation, explicitly listing which artifacts were found (by name or finding) and which are absent. The inventory is a discrete step — a conditional mention of artifacts in the recommendation phase does not satisfy C-10. |
| C-11 | **Per-category amend taxonomy** | behavior | Amend phase covers all three categories: (1) at least one missing option not explored, (2) at least one unweighted or equally-weighted decision criterion flagged for recalibration, and (3) at least one follow-up action item with an owner named. OWNER field must appear as a typed slot in the follow-up format template. |
| C-12 | **Structural OWNER template enforcement** | behavior | OWNER appears as a typed format slot in every amend entry across all three categories (missing option, unweighted criterion, follow-up) — not only in the follow-up category and not merely as a prose instruction. Satisfying C-11 (three categories, named owner in follow-up) does not satisfy C-12. |
| C-13 | **Decision framing temporal split** | depth | Decision framing includes a typed TEMPORAL ANCHOR (specific named date, sprint, or event — vague language such as "soon" or "near-term" is prohibited) and a typed INACTION CONSEQUENCE (concrete named outcome of not deciding — teams blocked, capability lost, window closed). A single WHY NOW field satisfies E-02 framing but not C-13. |
| C-14 | **Amend entry deadline enforcement** | behavior | Every amend entry across all three categories carries both an OWNER typed slot and a DEADLINE typed slot with specific values (sprint name, date, milestone — "TBD" or blank does not satisfy). DEADLINE must appear in the format template for all three category types, not only follow-up. |
| C-15 | **Failure mode register with sign-off linkage** | depth | Failure mode register (F-NN entries) distinct from risk register. Each F-row names: (1) failure mode, (2) trigger condition, (3) mitigation/escalation. Recommendation sign-off conditions reference at least one F-row by ID. |
| C-16 | **Numeric P×I scoring with project-specific anchors** | depth | Risk register uses separate numeric P (1-5) and I (1-5) scores per entry with computed P×I. Project-specific scoring anchors defined before any option is scored — what P=3 and I=3 mean for this specific project context. Holistic L/M/H labels do not satisfy C-16 even if probability and impact are mentioned. |
| C-17 | **Registers-before-recommendation ordering** | depth | Both assumption register and risk register appear as completed phases before the recommendation phase in document sequence. Registers that follow the recommendation justify rather than inform the decision. |
| C-18 | **Front-loaded amendment table** | behavior | Amendment table initialized before option generation with trigger rules that name which criterion fires under which condition. At document completion, the table shows either populated rows (violations caught during writing) or an explicit empty-table completion declaration. A retrospective editorial sweep assembled after the document is complete fails C-18. |
| C-19 | **Canonical failure mode field labels** | depth | Failure mode register uses exact field labels FAILURE MODE, TRIGGER CONDITION, and MITIGATION as typed column headers. Synonym substitution (e.g., "Observable Event" for TRIGGER CONDITION) requires reviewer inference and does not satisfy C-19. |
| C-20 | **PREREQUISITE GATE block** | depth | A typed PREREQUISITE GATE checklist appears as a discrete named phase immediately before the recommendation phase, confirming: (1) assumption register complete with >= 2 A-NN entries, (2) risk register complete with >= 3 R-NN entries, (3) both registers precede this gate block in document sequence. Each item is a named binary (complete / not complete). |
| C-21 | **Gate citations in all phase headers** | behavior | Every phase header carries a `[GATE: X-NN]` citation referencing a real criterion ID. A gate audit phase verifies all citations and records missing ones in the amendment table with STATUS = OPEN for the corresponding T-NN. |
| C-22 | **CLOSED BY column in coverage table** | behavior | Coverage table includes a CLOSED BY column. Every row carries a value naming the phase or step that satisfied the criterion. A coverage table with CRITERION and STATUS columns only, omitting CLOSED BY, fails C-22. |
| C-23 | **R-NN linkage in final RISK fields** | behavior | All option RISK fields in the final output carry R-NN register linkage rather than inline P×I notation computed at option-authoring time. RISK fields must reference the register entries that govern them. A document where Phase 2 used inline "P:3 × I:4 = 12" notation in RISK fields and no Phase 9b back-fill replaced it fails C-23. |
| C-24 | **Amendment table row count matches v20 criterion count** | behavior | Amendment table contains exactly 49 trigger rows at initialization (one per C-01..C-49 criterion). A table built from v19's criterion list (47 rows) without adding T-48, T-49 fires C-24 at PRE-DOCUMENT. A table with any count other than 49 fails C-24. |
| C-25 | **Numbered four-step finalization** | behavior | Phase 10 finalization executed as an explicitly numbered 4-step list: Step 1 (open trigger review with per-trigger findings), Step 2 (E-tier verification), Step 3 (R-tier verification), Step 4 (coverage table finalization). A prose narrative covering the same content without numbered steps fails C-25. |
| C-26 | **Dedicated Phase 9b risk propagation** | behavior | A dedicated Phase 9b (or explicitly named risk propagation equivalent) appears in the document for back-filling R-NN IDs from the register into option RISK fields. An inline comment, a retroactive edit note, or a Phase 3 postscript does not satisfy C-26 — Phase 9b must be a named phase in the document sequence. |
| C-27 | **Coverage table fully populated** | behavior | Every criterion row in the coverage table carries a STATUS value of PASS or FAIL. No row is left blank or marked TBD. A coverage table that omits STATUS for any criterion fails C-27. |
| C-28 | **Qualifying conditions in recommendation** | behavior | Recommendation sign-off includes at least two specific qualifying conditions naming circumstances under which the recommended option would no longer be valid or another option would supersede it. Generic confidence levels without named conditions do not satisfy C-28. |
| C-29 | **PHASE column in amendment table** | behavior | Amendment table includes a PHASE column. Every trigger row carries a populated PHASE value naming the lifecycle gate at which that trigger fires (PRE-DOCUMENT, PRE-OPTION, FINALIZATION, or a named phase). A table with blank PHASE cells on any row fails C-29. |
| C-30 | **Finding ordinal labels in finalization** | behavior | Each finding in Phase 10 Step 1 uses the format "Finding N: T-NN — [criterion name]". The ordinal N increments sequentially (Finding 1, Finding 2, ...). Each open trigger produces exactly one separately labeled finding entry — bundling two triggers into one finding entry fails C-30. |
| C-31 | **[R-NN pending] forward-reference placeholder** | behavior | Phase 2 RISK fields use `[R-NN pending]` as a forward-reference placeholder, reserving the register-linkage slot for Phase 9b back-fill. Inline P×I computation at Phase 2 is absent. Absence of the placeholder (blank RISK, generic risk category only, or direct P×I scoring) fails C-31. |
| C-32 | **Phase 9b dual-domain citation-site enumeration** | behavior | Phase 9b citation-site enumeration explicitly names both structural domains: (1) option RISK fields enumerated by option label, and (2) comparison matrix risk column. A single-domain enumeration (option fields only), a per-option-label iteration without naming the comparison matrix domain, or an aggregate "back-fill complete" confirmation all fail C-32. Both domain names must be explicit. |
| C-33 | **Phase 2 RISK prohibition instruction** | behavior | Phase 2 RISK field template includes an explicit prohibition — "Do not compute P×I in Phase 2 RISK fields" (or vocabulary-pinned equivalent) — adjacent to the `[R-NN pending]` placeholder directive. The prohibition and the placeholder must appear in the same template block. A Phase 2 template that contains the placeholder but omits the prohibition, or places the prohibition in a separate section, fails C-33. |
| C-34 | **Phase 9b domain-indexed labels** | behavior | Each domain entry in Phase 9b carries a numeric index prefix on its header: "Domain 1 —", "Domain 2 —", or an ordinal-indexed equivalent such as "(1)", "(2)". Every enumerated domain requires a prefix. A domain header listed as "Option RISK fields" without a preceding numeric index fails C-34 regardless of the domain's content quality. |
| C-35 | **Phase 9b per-site back-fill transition notation** | behavior | Each citation site in Phase 9b shows a before/after state transition using arrow notation: `[R-NN pending] → [R-NN entries]`. Showing only the final state ("the R-NN IDs applied to its RISK field"), only a completion confirmation ("back-fill complete"), or a domain-level summary without per-site arrows fails C-35. The transition notation must appear at each individual citation site. |
| C-36 | **Phase 9b Domain 1 back-fill includes P×I compound scores** | behavior | At each Domain 1 (option RISK fields) citation site, the back-fill transition notation includes the P×I compound scores from the risk register alongside the R-NN identifiers. The P×I values must appear in the transition target — e.g., `[OPTION-A label] RISK field: [R-NN pending] → [R-03 (P:2 × I:4 = 8), R-07 (P:3 × I:3 = 9)]`. A back-fill showing `[R-NN pending] → [R-03, R-07]` passes C-35 (transition notation present) but fails C-36 (P×I compound scores absent). Each back-filled RISK field is self-contained when C-36 passes: a reviewer can assess the risk level at the option anatomy without consulting the register. |
| C-37 | **Phase 9b Domain 2 per-option-column R-NN attribution** | behavior | The Domain 2 (comparison matrix risk column) enumeration in Phase 9b explicitly attributes specific R-NN IDs to each option's column in the risk row — not a domain-level confirmation that R-NN IDs appear somewhere in the row. Per-column attribution format: each option column is identified by label with its applicable R-NN IDs listed. A Domain 2 entry stating "Risk row: R-NN IDs cited" or "comparison matrix risk column updated" confirms domain presence (C-32 PASS) but provides no per-column traceability (C-37 FAIL). A Domain 2 entry with "Risk row: [OPTION-A column: R-03, R-07] \| [OPTION-B column: R-01] \| [do-nothing column: R-02]" passes C-37. Satisfying C-32 (domain named) and C-34 (domain carries index prefix) does not satisfy C-37 — per-column attribution is independently required. |
| C-38 | **Amendment table T-37 trigger entry includes inline failure-condition exemplar** | behavior | The T-37 row in the amendment table carries an inline exemplar note within the CONDITION field — a parenthetical or quoted construct showing the exact document language that fires T-37. The exemplar must quote or closely paraphrase what row-level Domain 2 confirmation looks like, e.g., "row-level confirmation 'R-NN IDs applied to risk row' fires T-37". A T-37 entry stating only "C-37: per-column attribution absent" without an inline exemplar quote fails C-38. Satisfying C-18 (trigger rules front-loaded) and C-29 (PHASE column populated) does not satisfy C-38 — the inline exemplar is independently required within the T-37 CONDITION field itself. The exemplar makes the trigger self-documenting: a reviewer assessing a Phase 9b Domain 2 entry can determine whether T-37 fires without consulting the rubric. |
| C-39 | **Amendment table T-37 trigger entry includes correct-format prescription alongside the inline failure exemplar** | behavior | The T-37 CONDITION field carries both the inline failure exemplar (Part 1, required by C-38) AND an explicit correct-format prescription (Part 2). Part 2 states the replacement format that would satisfy C-37 — naming the expected per-option-column attribution structure. The two-part structure makes the T-37 entry fully self-contained: a reviewer can determine both what fires T-37 and what would satisfy C-37 without consulting the rubric or Phase 9b. Target form: "row-level confirmation 'R-NN IDs applied to risk row' fires T-37; per-column format required: [OPTION-A column: R-NN IDs] \| [OPTION-B: R-NN IDs]". A T-37 CONDITION field carrying only Part 1 without a correct-format prescription passes C-38 but fails C-39. Satisfying C-38 (failure exemplar present) does not satisfy C-39 — the correct-format prescription is independently required in the same CONDITION cell. |
| C-40 | **Amendment table T-38 trigger entry includes inline failure-condition exemplar** | behavior | The T-38 row in the amendment table carries an inline exemplar note within the CONDITION field — a quoted or paraphrased construct showing what an abstract-only T-37 CONDITION entry looks like (the exact form that fires T-38). An abstract-only T-37 CONDITION is one that names the condition category without quoting the failure construct, e.g., "fires if Phase 9b Domain 2 enumeration does not carry per-option-column R-NN attribution". A T-38 CONDITION entry stating only "fires if T-37 CONDITION lacks an inline failure exemplar" names the condition but does not exemplify a deficient T-37 entry and fails C-40. The inline exemplar in T-38's CONDITION cell makes T-38 self-documenting: a reviewer assessing a T-37 CONDITION entry can determine whether T-38 fires without consulting C-38 or the rubric. Satisfying C-38 (T-37 CONDITION carries its own failure exemplar) does not satisfy C-40 — the exemplar in T-38's CONDITION is independently required and concerns T-38's trigger condition, not T-37's. |
| C-41 | **Amendment table T-38 trigger entry includes correct-format prescription alongside the inline failure exemplar** | behavior | The T-38 CONDITION field carries both the inline failure exemplar (Part 1, required by C-40) AND an explicit correct-format prescription (Part 2). Part 2 states what a passing T-37 CONDITION entry looks like — the minimum form that satisfies C-38: an inline failure exemplar quoting the exact construct that fires T-37. The two-part T-38 CONDITION makes it fully self-contained: a reviewer can determine both what fires T-38 and what would satisfy C-38 without consulting the rubric or T-37's CONDITION cell. A T-38 CONDITION carrying only Part 1 without a correct-format prescription passes C-40 but fails C-41. Satisfying C-39 (T-37 CONDITION carries its own correct-format prescription) does not satisfy C-41 — the correct-format prescription in T-38's CONDITION is independently required and concerns what satisfies C-38, not what satisfies C-37. |
| C-42 | **Amendment table T-40 trigger entry includes inline failure-condition exemplar** | behavior | The T-40 row in the amendment table carries an inline exemplar note within the CONDITION field — a quoted or paraphrased construct showing what an abstract-only T-38 CONDITION entry looks like (the exact form that fires T-40). An abstract-only T-38 CONDITION is one that names the condition category without quoting or paraphrasing a deficient T-37 CONDITION form, e.g., "fires if T-38 CONDITION lacks an inline failure exemplar" names the condition but does not show what a deficient T-38 entry looks like. A T-40 CONDITION entry stating only "fires if T-38 CONDITION lacks a failure exemplar" without an inline exemplar of a deficient T-38 form fails C-42. The inline exemplar in T-40's CONDITION cell makes T-40 self-documenting: a reviewer assessing a T-38 CONDITION entry can determine whether T-40 fires without consulting C-40 or the rubric. Satisfying C-40 (T-38 CONDITION carries its own failure exemplar) does not satisfy C-42 — the exemplar in T-40's CONDITION is independently required and concerns T-40's trigger condition, not T-38's. |
| C-43 | **Amendment table T-40 trigger entry includes correct-format prescription alongside the inline failure exemplar** | behavior | The T-40 CONDITION field carries both the inline failure exemplar (Part 1, required by C-42) AND an explicit correct-format prescription (Part 2). Part 2 states what a passing T-38 CONDITION entry looks like — the minimum form that satisfies C-40: a quoted or paraphrased exemplar of an abstract-only T-37 CONDITION form. The two-part T-40 CONDITION makes it fully self-contained: a reviewer can determine both what fires T-40 and what would satisfy C-40 without consulting the rubric or T-38's CONDITION cell. A T-40 CONDITION carrying only Part 1 without a correct-format prescription passes C-42 but fails C-43. Satisfying C-41 (T-38 CONDITION carries its own correct-format prescription) does not satisfy C-43 — the correct-format prescription in T-40's CONDITION is independently required and concerns what satisfies C-40, not what satisfies C-38. |
| C-44 | **T-40 CONDITION exemplar includes explanation of why the quoted deficient T-38 form is abstract** | behavior | The T-40 CONDITION field's Part 1 exemplar (required by C-42) must additionally include an explicit explanation of why the quoted or paraphrased T-38 CONDITION form is abstract — stating that it names the trigger condition category without showing what a deficient T-37 CONDITION entry looks like. A T-40 CONDITION that quotes the deficient T-38 form ("fires if T-38 CONDITION lacks an inline failure exemplar — this names the condition without exemplifying what a deficient T-37 entry looks like") passes C-44. A T-40 CONDITION that quotes the deficient T-38 form without any such explanation passes C-42 but fails C-44 — the quoted form alone identifies the deficient instance without explaining the nature of its deficiency. The explanation-of-abstractness is required content, not optional annotation: it makes the T-40 CONDITION fully self-contained such that a reviewer can determine not only what form fires T-40 but why that form is insufficient. The explanation must appear within the T-40 CONDITION cell's exemplar construct, not in a separate annotation or rubric reference. C-42 FAIL → C-44 FAIL (cascade: an absent exemplar contains no explanation-of-abstractness). C-42 PASS does not guarantee C-44 PASS — the C-44-independent-fail state is: exemplar present but no explanation of why it is abstract. |
| C-45 | **Amendment table T-42 trigger entry includes inline failure-condition exemplar** | behavior | The T-42 row in the amendment table carries an inline exemplar note within the CONDITION field — a quoted or paraphrased construct showing what an abstract-only T-40 CONDITION entry looks like (the exact form that fires T-42). An abstract-only T-40 CONDITION is one that names the condition category without showing what a deficient T-38 CONDITION entry looks like. A T-42 CONDITION entry stating only "fires if T-40 CONDITION lacks an inline failure exemplar" names the condition without exemplifying a deficient T-40 entry and fails C-45. The inline exemplar in T-42's CONDITION cell makes T-42 self-documenting: a reviewer assessing a T-40 CONDITION entry can determine whether T-42 fires without consulting C-42 or the rubric. Satisfying C-42 (T-40 CONDITION carries its own failure exemplar) does not satisfy C-45 — the exemplar in T-42's CONDITION is independently required and concerns T-42's trigger condition, not T-40's. This follows the same structural derivation as C-40 (T-38 CONDITION exemplar) and C-42 (T-40 CONDITION exemplar): each chain-tier's trigger entry must be independently self-documenting at the tier above it. |
| C-46 | **Amendment table T-42 trigger entry includes correct-format prescription alongside the inline failure exemplar** | behavior | The T-42 CONDITION field carries both the inline failure exemplar (Part 1, required by C-45) AND an explicit correct-format prescription (Part 2). Part 2 states what a passing T-40 CONDITION entry looks like — the minimum form that satisfies C-42: a quoted or paraphrased exemplar of an abstract-only T-38 CONDITION form, accompanied by an explanation of its abstractness (C-44) and a correct-format prescription (C-43). The two-part T-42 CONDITION makes it fully self-contained: a reviewer can determine both what fires T-42 and what would satisfy C-42 without consulting the rubric or T-40's CONDITION cell. A T-42 CONDITION carrying only Part 1 without a correct-format prescription passes C-45 but fails C-46. Satisfying C-43 (T-40 CONDITION carries its own correct-format prescription) does not satisfy C-46 — the correct-format prescription in T-42's CONDITION is independently required and concerns what satisfies C-42, not what satisfies C-40. C-45 FAIL → C-46 FAIL (cascade: no exemplar means no correct-format prescription is possible in the same cell). C-45 PASS does not guarantee C-46 PASS — the C-46-independent-fail state is: exemplar present, prescription absent. **Live demonstration: V-03 R19.** |
| C-47 | **T-42 CONDITION exemplar includes explanation of why the quoted deficient T-40 form is abstract** | behavior | The T-42 CONDITION field's Part 1 exemplar (required by C-45) must additionally include an explicit explanation of why the quoted or paraphrased T-40 CONDITION form is abstract — stating that it names the trigger condition category without showing what a deficient T-38 CONDITION entry looks like. A T-42 CONDITION that quotes the deficient T-40 form with explanation ("fires if T-40 CONDITION lacks an inline failure exemplar — this names the condition without exemplifying what a deficient T-38 entry looks like") passes C-47. A T-42 CONDITION that quotes the deficient T-40 form without any such explanation passes C-45 but fails C-47. The explanation-of-abstractness must appear within the T-42 CONDITION cell's exemplar construct, not in a separate annotation or rubric reference. C-45 FAIL → C-47 FAIL (cascade). C-45 PASS does not guarantee C-47 PASS — the C-47-independent-fail state is: exemplar present but no explanation of why it is abstract. **Live demonstration: V-02 R19.** C-46 and C-47 are mutually independent. **Mutual independence confirmed live: V-02 R19 (C-47 FAIL, C-46 FAIL) vs. V-03 R19 (C-47 PASS, C-46 FAIL).** |
| C-48 | **Amendment table T-46 trigger entry includes inline failure-condition exemplar** | behavior | The T-46 row in the amendment table carries an inline exemplar note within the CONDITION field — a quoted or paraphrased construct showing what a Part-1-only T-42 CONDITION entry looks like (the exact form that fires T-46: T-42 CONDITION has Part 1 labeled and present but no Part 2 label and no Part 2 content). A T-46 CONDITION entry stating only "fires if T-42 CONDITION lacks Part 2 prescription" names the condition without exemplifying the specific V-03-class state T-46 fires for and fails C-48. The inline exemplar in T-46's CONDITION cell makes T-46 self-documenting: a reviewer assessing a T-42 CONDITION entry can determine whether T-46 fires without consulting C-46 or the rubric. Satisfying C-45 (T-42 CONDITION carries its own failure exemplar) does not satisfy C-48 — the exemplar in T-46's CONDITION is independently required and concerns T-46's trigger condition (the Part-1-present-Part-2-absent T-42 state), not T-42's baseline exemplar requirement. This follows the same structural derivation as C-40 through C-45: each tier-watching trigger must be independently self-documenting by exemplifying the specific deficient state it fires for. C-45 FAIL → C-48 FAIL (cascade: if T-42 is fully abstract with no Part 1, the Part-1-present-Part-2-absent state T-46's exemplar must show cannot be constructed or quoted). C-45 PASS does not guarantee C-48 PASS. C-46 FAIL (independent: Part 1 present, Part 2 absent) does not cascade to C-48 FAIL — T-46's CONDITION exemplar is independently testable. C-48 and C-49 are mutually independent. |
| C-49 | **Amendment table T-47 trigger entry includes inline failure-condition exemplar** | behavior | The T-47 row in the amendment table carries an inline exemplar note within the CONDITION field — a quoted or paraphrased construct showing what a T-42 CONDITION entry looks like when it has a quoted deficient T-40 form present but no explanation-of-abstractness (the exact form that fires T-47: T-42 CONDITION has an exemplar of a deficient T-40 form but no "abstract because…" or "this names the condition without showing…" phrase appended). A T-47 CONDITION entry stating only "fires if T-42 CONDITION exemplar lacks explanation of why the quoted T-40 form is abstract" names the condition without exemplifying the specific V-02-class state T-47 fires for and fails C-49. The inline exemplar in T-47's CONDITION cell makes T-47 self-documenting: a reviewer assessing a T-42 CONDITION entry can determine whether T-47 fires without consulting C-47 or the rubric. Satisfying C-45 (T-42 CONDITION carries its own failure exemplar) does not satisfy C-49 — the exemplar in T-47's CONDITION is independently required and concerns T-47's trigger condition (the exemplar-present-explanation-absent T-42 state), not T-42's baseline exemplar requirement. C-45 FAIL → C-49 FAIL (cascade: if T-42 is fully abstract with no exemplar, the exemplar-present-explanation-absent state T-47's exemplar must show cannot be constructed). C-45 PASS does not guarantee C-49 PASS. C-47 FAIL (independent: exemplar without explanation) does not cascade to C-49 FAIL — T-47's CONDITION exemplar is independently testable. C-48 and C-49 are mutually independent. |

---

## Scoring Formula

```
composite = (essential_pass / 4 × 60)
          + (required_pass / 3 × 30)
          + (aspirational_pass / 42 × 10)
```

When all essential and required criteria pass, the formula simplifies to:

```
composite = 90 + (aspirational_pass / 42 × 10)
```

**Golden threshold**: all 4 essential criteria pass AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Golden | all essential + >= 80 | Ready for use as a reference artifact |
| Passing | all essential + >= 60 | Usable with minor gaps |
| Failing | any essential fails | Output is not a valid proposal |

**Score reference under v20:**
| Aspirational passes | Composite |
|---------------------|-----------|
| 42/42 | 100.00 |
| 41/42 | 99.76 |
| 40/42 | 99.52 |
| 39/42 | 99.29 |
| 38/42 | 99.05 |
| 37/42 | 98.81 |
| 36/42 | 98.57 |
| 35/42 | 98.33 |
| 34/42 | 98.10 |
| 33/42 | 97.86 |
| 32/42 | 97.62 |
| 31/42 | 97.38 |
| 30/42 | 97.14 |
| 29/42 | 96.90 |
| 28/42 | 96.67 |
| 27/42 | 96.43 |
| 26/42 | 96.19 |
| 25/42 | 95.95 |
| 24/42 | 95.71 |
| 23/42 | 95.48 |
| 22/42 | 95.24 |
| 21/42 | 95.00 |

---

## Common Failure Modes

- Options presented as prose paragraphs without OPTION / PROBLEM / RISK / RATIONALE fields — fails E-02
- Do-nothing option present but labeled "Option A" or "current state" without explicit no-change designation — fails C-02
- Recommendation present but qualifying conditions generic ("if circumstances change") without naming the specific circumstances — fails C-28 and E-04
- PROBLEM field paraphrased rather than repeated verbatim across options — fails C-01
- Scout artifacts mentioned conditionally in recommendation ("if a feasibility report exists...") with no dedicated inventory step — fails C-06 and C-10
- Amend phase lists three category headers but FOLLOW-UP entries have no OWNER slot in the format template — C-09 satisfied, C-11 and C-12 fail
- Amendment table assembled retrospectively at document end without initialization at Phase 0 — fails C-18
- Assumption register present but appears after the recommendation — registers-before-recommendation ordering violated, fails C-17
- Coverage table built with CRITERION and STATUS columns only; CLOSED BY column absent — fails C-22
- Phase 2 RISK fields use inline P×I notation ("P:3 × I:4 = 12") rather than `[R-NN pending]` placeholder — fails C-31; also fails C-23 at finalization when back-fill never occurs
- Phase 2 RISK template contains `[R-NN pending]` placeholder but no "Do not compute P×I" prohibition adjacent to it — fails C-33; satisfies C-31 if placeholder is present
- Phase 9b present but enumerates only option RISK fields ("enumerate each citation site visited by option label") without naming the comparison matrix risk column as a second domain — fails C-32; satisfies C-26 if Phase 9b phase is present
- Phase 9b names both structural domains (C-32 PASS) but domain headers appear as "Option RISK fields" and "Comparison matrix risk column" without numeric index prefixes — fails C-34; C-32 passes
- Phase 9b domain-indexed (C-34 PASS, C-32 PASS) but per-site output states only the final state: "the R-NN IDs applied to its RISK field" — no `[R-NN pending] → [R-NN IDs]` transition arrow — fails C-35 (V-04 R12 failure mode)
- Phase 9b aggregate confirmation: "all [R-NN pending] placeholders resolved; back-fill complete" — no structural domains named, no domain-index prefixes, no per-site entries — fails C-32, C-34, C-35, C-36, C-37 simultaneously (V-05 R12 failure mode)
- Phase 9b Domain 1 shows per-site transition notation (C-35 PASS) but entries list only R-NN IDs without P×I scores: `[R-NN pending] → [R-03, R-07]` — fails C-36; satisfies C-35 (V-01 R13 failure mode)
- Phase 9b Domain 2 carries index prefix (C-34 PASS) and is named as structural domain (C-32 PASS) but confirms only row-level R-NN presence ("R-NN IDs cited in risk row") without per-option-column attribution — fails C-37 (V-02 R13 failure mode)
- Amendment table built from v13 criterion list (37 rows) without adding T-38 — fires C-24 at PRE-DOCUMENT; also cascades to C-38 FAIL if T-37 entry lacks inline exemplar
- Amendment table built from v14 criterion list (38 rows) without adding T-39 — fires C-24 at PRE-DOCUMENT under v15; also cascades to C-39 FAIL
- Amendment table built from v15 criterion list (39 rows) without adding T-40 and T-41 — fires C-24 at PRE-DOCUMENT under v16; also cascades to C-40 FAIL and C-41 FAIL by cascade
- Amendment table built from v16 criterion list (41 rows) without adding T-42 and T-43 — fires C-24 at PRE-DOCUMENT under v17; also cascades to C-42 FAIL and C-43 FAIL by cascade
- Amendment table built from v17 criterion list (43 rows) without adding T-44 and T-45 — fires C-24 at PRE-DOCUMENT under v18; also cascades to C-44 FAIL and C-45 FAIL
- Amendment table built from v18 criterion list (45 rows) without adding T-46 and T-47 — fires C-24 at PRE-DOCUMENT under v19; also cascades to C-46 FAIL and C-47 FAIL; T-44 and T-45 rows do not supply the required T-46 and T-47 content
- Amendment table built from v19 criterion list (47 rows) without adding T-48 and T-49 — fires C-24 at PRE-DOCUMENT under v20; also cascades to C-48 FAIL (no T-48 entry to carry exemplar of T-46's Part-1-only firing condition) and C-49 FAIL (no T-49 entry to carry exemplar of T-47's exemplar-without-explanation firing condition); T-46 and T-47 rows do not supply the required T-48 and T-49 content
- Amendment table T-37 entry states trigger condition abstractly ("C-37: per-column attribution absent from Domain 2") without an inline exemplar quoting the failure construct — fails C-38 even when C-18 and C-29 both pass; also fails C-39 by cascade
- Amendment table T-37 entry carries inline failure exemplar (C-38 PASS, Part 1 present) but stops there — no correct-format prescription stating what per-column attribution looks like — fails C-39; satisfies C-38 (V-01 R15 ceiling)
- Amendment table T-38 entry states trigger condition abstractly ("fires if T-37 CONDITION lacks an inline failure exemplar") without a quoted or paraphrased sample of what an abstract T-37 CONDITION looks like — fails C-40; also fails C-41 by cascade
- Amendment table T-38 entry carries an inline abstract-T-37-form exemplar (C-40 PASS, Part 1 present) but stops there — no correct-format prescription stating what a passing T-37 CONDITION entry looks like — fails C-41; satisfies C-40 (V-02 R16 ceiling)
- Amendment table T-40 entry states trigger condition abstractly ("fires if T-38 CONDITION lacks an inline failure exemplar") without a quoted or paraphrased sample of what an abstract T-38 CONDITION looks like — fails C-42; also fails C-43 by cascade
- Amendment table T-40 entry carries an inline abstract-T-38-form exemplar (C-42 PASS, Part 1 present) but stops there — no correct-format prescription stating what a passing T-38 CONDITION entry looks like — fails C-43; satisfies C-42
- Amendment table T-40 entry carries an inline abstract-T-38-form exemplar (C-42 PASS) with a correct-format prescription (C-43 PASS) but the exemplar does not include an explanation of why the quoted T-38 form is abstract — fails C-44 independently; C-42 PASS and C-43 PASS do not supply the explanation-of-abstractness required by C-44
- Amendment table T-42 entry states trigger condition abstractly ("fires if T-40 CONDITION lacks an inline failure exemplar") without a quoted or paraphrased sample of what an abstract T-40 CONDITION looks like — fails C-45; also fails C-46, C-47, C-48, C-49 by cascade (abstract T-42 CONDITION contains no content from which the C-46/C-47/C-48/C-49-required states can be derived)
- Amendment table T-42 entry carries an inline abstract-T-40-form exemplar (C-45 PASS, Part 1 present) but stops there — no correct-format prescription stating what a passing T-40 CONDITION entry looks like — fails C-46 independently; satisfies C-45 (V-03 R19 ceiling under v19)
- Amendment table T-42 entry carries an inline abstract-T-40-form exemplar (C-45 PASS) with a correct-format prescription (C-46 PASS) but the exemplar does not include an explanation of why the quoted T-40 form is abstract — fails C-47 independently; C-45 PASS and C-46 PASS do not supply the explanation-of-abstractness required by C-47
- Amendment table T-46 entry states trigger condition abstractly ("fires if T-42 CONDITION lacks Part 2 prescription") without a quoted or paraphrased sample of what a Part-1-only T-42 CONDITION looks like — fails C-48; satisfies C-45 (the T-42 baseline exemplar is independent)
- Amendment table T-47 entry states trigger condition abstractly ("fires if T-42 CONDITION exemplar lacks explanation of abstractness") without a quoted or paraphrased sample of what a T-42-exemplar-without-explanation looks like — fails C-49; satisfies C-45 (the T-42 baseline exemplar is independent)
- Finalization executed as prose narrative ("walk through the document for completeness") rather than numbered steps — fails C-25 regardless of content quality
- PM contribution absent from risk register; all R-NN entries authored by Architect — fails C-04
- Phase headers carry no `[GATE: X-NN]` citations; gate audit has nothing to verify — fails C-21

---

## Round 1–11 Discriminator Summary

For early-round discriminator notes (R1–R11), see the v12 rubric file. The v20 rubric inherits all prior discriminator observations unchanged.

---

## Round 12 Discriminator Notes

**R12 design**: Five variations, two new criteria (C-34, C-35 under v12). Single-axis variations V-01..V-03 isolate individual failure modes; V-04 and V-05 combine axes.

**Confirmed discriminators:**

**C-34 isolation by V-04**: The "(1)"/"(2)" ordinal form satisfies C-34's numeric-index-prefix requirement. V-04 demonstrates C-34 PASS with ordinal-indexed domain headers while failing C-35 (per-site outcome-only notation). C-34 is therefore satisfiable without "Domain N —" canonical form — ordinal equivalents qualify.

**C-35 isolation by V-04**: V-04 provides the cleanest C-35 isolation: C-31 PASS (placeholder at Phase 2), C-32 PASS (both domains named), C-34 PASS (ordinal prefixes), C-35 FAIL (outcome-only: "the R-NN IDs applied to its RISK field" without before/after transition). The discriminating property: C-35 requires the before-state (`[R-NN pending]`) and the after-state (R-NN IDs) to appear together in a single arrow notation at each site.

**C-32 + C-34 + C-35 cascade from aggregate Phase 9b (V-05)**: An aggregate confirmation form ("Citation-site enumeration: all [R-NN pending] placeholders resolved; back-fill complete") collapses C-32, C-34, and C-35 simultaneously. No structural domain names → C-32 FAIL. No domains to carry index prefixes → C-34 FAIL. No per-site entries → C-35 FAIL. The aggregate shortcut is a single authoring decision that fails three independent structural requirements. Under v13+, the same aggregate form also cascades to C-36 FAIL (no per-site entries to carry P×I) and C-37 FAIL (no Domain 2 enumeration to carry per-column attribution) — five simultaneous failures from one shortcut.

**V-02 R12 as C-34 + C-35 + C-36 + C-37 exemplar**: V-02 R12's Phase 9b demonstrates the ceiling behavior for all four register-linkage depth criteria simultaneously:
- C-34 PASS: "Domain 1 —" / "Domain 2 —" explicit numeric-index domain headers
- C-35 PASS: `[OPTION-A label] RISK field: [R-NN pending] → [applicable R-NN entries, P×I scores]` arrow notation per site
- C-36 PASS: P×I compound scores included in the transition target alongside R-NN IDs
- C-37 PASS: "Risk row: [R-NN IDs inserted per option column]" per-column attribution for Domain 2

**New cascade evidence for v13:**
- C-37 independent fail from V-04 R12: V-04 passes C-32 (Domain 2 named) and C-34 (index prefix) but fails C-37 (Domain 2 row-level only, no per-column attribution). This confirms C-37 is independently testable from C-32 and C-34.
- C-36 cascade invariant confirmed: C-35 FAIL → C-36 FAIL. No variation in R12 passed C-35 while failing C-36.

---

## Round 13 Discriminator Notes

**R13 design**: Three variations. V-01 isolates C-36 (Domain 1 P×I absent, Domain 2 excellent). V-02 isolates C-37 (Domain 1 P×I present, Domain 2 row-level only). V-03 combines C-24 stale table with C-36 and C-37 simultaneously.

**Confirmed discriminators:**

**C-36 isolation by V-01**: V-01 demonstrates the cleanest C-36 isolation: C-35 PASS (per-site arrow notation present), C-37 PASS (Domain 2 per-column attribution present), C-36 FAIL (Domain 1 transition targets list only R-NN IDs without P×I scores). The designed-omission note "reference the register for compound scores" in V-01's Phase 9b is an authored clarification, not a rubric substitute — its presence does not affect C-36 scoring. C-36 requires P×I values in the transition target itself.

**C-37 isolation by V-02**: V-02 demonstrates C-37 isolation with Domain 1 fully excellent: C-35 PASS, C-36 PASS (P×I compound scores embedded in Domain 1 transitions), C-37 FAIL ("Risk row: R-NN IDs applied to risk row" — row-level confirmation without per-column attribution). The T-37 exemplar note in V-02's amendment spec ("row-level confirmation 'R-NN IDs applied to risk row' fires T-37") demonstrates that the exact firing language can be embedded in the trigger entry itself — this is the source excellence signal for C-38.

**Compact format CLOSED BY preservation (V-02 R13)**: V-02 R13 demonstrates that CLOSED BY column is preserved in compact coverage table format ("even in compact form for traceability"). This confirms C-22 has no compact-format exception — the column is required regardless of format density.

**V-03 stale-table cascade behavior (R13)**: V-03's 35-row amendment table (C-01..C-35) fails C-24 at PRE-DOCUMENT (35 ≠ 37 required by v13). The stale table prevents T-36 and T-37 from existing as named triggers, which means: (1) C-36 and C-37 violations cannot produce named T-NN findings during finalization, and (2) the finalization produces only one ordinal finding (T-24) rather than three. The undercounted finding set is a cascade consequence of the stale table, not an independent C-30 failure — C-30 requires each open trigger to produce a separately labeled finding, but no T-36 or T-37 rows exist to generate such findings when the table is stale.

**New cascade evidence for v14:**
- C-38 cascade from stale table: A table missing T-37 entirely fails C-38 by cascade — no T-37 entry exists to carry the exemplar. The cascade is: T-37 absent from amendment table → C-38 FAIL.
- C-38 independent fail: A 38-row table with T-37 present (C-24 PASS) but T-37 CONDITION entry carrying only an abstract condition statement fails C-38. C-38 is independently testable: a reviewer reads the T-37 CONDITION cell specifically for an inline quoted exemplar, not just a condition category name.
- C-24 version-bump cascade: All R13 variations had 37-row amendment tables (or 35-row for V-03). Under v14, all R13 variations fail C-24 (38 rows required). This is the expected version-bump cascade.

---

## Round 14 Discriminator Notes

**R14 design**: Three variations. V-01 isolates C-38 (abstract T-37 CONDITION, no inline failure exemplar). V-02 demonstrates C-38 PASS and is the source excellence signal for C-39 (T-37 two-part CONDITION structure). V-03 combines C-24 stale table (37 rows) with C-38 independent fail (abstract T-37 CONDITION).

**Confirmed discriminators:**

**C-38 isolation by V-01**: V-01's T-37 CONDITION is abstract — "fires if Phase 9b Domain 2 enumeration does not carry per-option-column R-NN attribution" — naming the condition category without quoting the failure construct. This fails C-38 (no inline exemplar) and by cascade C-39 (no correct format present in an abstract entry). V-01 demonstrates the criterion boundary: condition category naming alone is the floor; the inline failure exemplar is the C-38 threshold.

**V-02 R14 as C-38 ceiling and C-39 source exemplar**: V-02 demonstrates the two-part T-37 CONDITION structure that passes both C-38 and C-39:
- Part 1 (C-38): "row-level confirmation 'R-NN IDs applied to risk row' fires T-37" — exact failure construct quoted
- Part 2 (C-39): "per-column format required: [OPTION-A column: R-NN IDs] \| [OPTION-B: R-NN IDs]" — correct replacement format prescribed

The two-part entry is self-documenting at both levels simultaneously: a reviewer can determine what fires T-37 (Part 1) and what satisfies C-37 (Part 2) without consulting the rubric or Phase 9b. This is the reference exemplar for both criteria.

**C-39 cascade from C-38 confirmed**: V-01's abstract T-37 CONDITION establishes the deterministic cascade: C-38 FAIL → C-39 FAIL. An abstract entry contains neither Part 1 nor Part 2. No variation in R14 passed C-38 while failing C-39, confirming the cascade direction is one-way — C-38 PASS does not guarantee C-39 PASS (the C-39-independent-fail requires a variation that adds Part 1 but omits Part 2).

**V-03 stale-table C-38 and C-39 behavior (R14)**: V-03's 37-row table fails C-24 (38 rows required by v14; 39 by v15). T-37 is present (T-01..T-37 range) but carries an abstract CONDITION text — C-38 FAIL (independent, not cascade from C-24), C-39 FAIL (cascade from C-38). Under v15, V-03 fails C-24, C-38, and C-39 for three fails and a composite of 99.06.

**New cascade evidence for v15:**
- C-39 cascade from C-38: Confirmed by V-01 and V-03. An abstract T-37 CONDITION fails both C-38 (no failure exemplar) and C-39 (no correct format). C-38 FAIL → C-39 FAIL is deterministic.
- C-39 independent fail boundary: A T-37 CONDITION carrying only Part 1 without Part 2 passes C-38 and fails C-39. No R14 variation hit this exact pattern; V-02 demonstrated the full two-part pass. The independent fail is structurally established by criterion definition and C-39's testability note.
- C-24 version-bump cascade: All R14 variations with 38-row tables fail C-24 under v15 (39 rows required). V-03's 37-row table fails C-24 under both v14 and v15.

---

## Round 15 Discriminator Notes

**R15 design**: Two variations shown. V-01 isolates C-39 (T-37 CONDITION has Part 1 only — failure exemplar present, correct-format prescription absent). V-02 is the excellence exemplar for C-38 + C-39 simultaneously, and is the source of the T-38/T-39 silent-trigger observation that yields C-40 and C-41.

**Confirmed discriminators:**

**C-39 independent fail confirmed by V-01**: V-01's T-37 CONDITION carries Part 1 (the inline failure exemplar: "row-level confirmation 'R-NN IDs applied to risk row' fires T-37") but omits Part 2 — no correct-format prescription. This is the first live demonstration of the C-39-independent-fail pattern (C-38 PASS, C-39 FAIL). T-39 fires; Finding 1: T-39. V-01 establishes the exact criterion boundary: the inline failure exemplar is necessary but not sufficient for C-39; a separate correct-format prescription is required in the same CONDITION cell.

**V-02 R15 as T-38/T-39 silent-trigger exemplar and C-40/C-41 source**: V-02's T-37 CONDITION carries the full two-part structure (C-38 PASS, C-39 PASS). The closing note — "T-38 and T-39 are silent (both parts present in CONDITION)" — is the R15 excellence signal. T-38 being silent confirms that T-38 is a named, operational trigger with a CONDITION field that evaluates whether T-37 CONDITION carries Part 1. T-39 being silent confirms the same for Part 2. Both triggers having evaluable CONDITION fields and silencing correctly when C-38 and C-39 pass establishes T-38 and T-39 as first-class amendment table entries. Their CONDITION field quality — whether each carries an inline exemplar and a correct-format prescription — is the source of C-40 and C-41.

**T-38 and T-39 operational trigger structure (R15)**:
- T-38 fires when C-38 fails — when the T-37 CONDITION field lacks Part 1 (no inline failure exemplar showing what row-level Domain 2 confirmation looks like)
- T-39 fires when C-39 fails — when the T-37 CONDITION field has Part 1 but lacks Part 2 (no correct-format prescription)
- In V-02 R15, C-38 and C-39 both pass → T-38 and T-39 are both silent; the single finding is T-37 (C-37 FAIL)
- In V-01 R15, C-38 passes and C-39 fails → T-38 is silent, T-39 fires; the single finding is T-39

This is structurally analogous to how T-37 fires when C-37 fails, with T-38/T-39 watching the quality of the T-37 CONDITION cell rather than watching the Phase 9b Domain 2 output.

**C-40 and C-41 as T-38 CONDITION quality criteria**: Following the same structural principle that yielded C-38 (T-37 CONDITION must carry a failure exemplar) and C-39 (T-37 CONDITION must also carry a correct-format prescription), C-40 and C-41 impose the same two-part self-documentation standard on T-38's own CONDITION field. The cascade invariant is identical in form: C-40 FAIL → C-41 FAIL (an abstract T-38 CONDITION contains neither part); C-40 PASS does not guarantee C-41 PASS (Part 1 present, Part 2 absent is a valid independent-fail state for C-41).

**New cascade evidence for v16:**
- C-41 cascade from C-40: An abstract T-38 CONDITION (category statement only, no exemplar of what an abstract T-37 CONDITION looks like) fails both C-40 and C-41. C-40 FAIL → C-41 FAIL is deterministic.
- C-41 independent fail boundary: A T-38 CONDITION carrying only Part 1 without a correct-format prescription passes C-40 and fails C-41. No R15 variation hit this exact pattern. The independent fail is structurally established by criterion definition and C-41's testability note.
- C-24 version-bump cascade: All R15 variations had 39-row amendment tables (one per C-01..C-39, correct under v15). Under v16, all R15 variations fail C-24 (41 rows required: T-40 and T-41 absent). This is the expected version-bump cascade.

---

## Round 16 Discriminator Notes

**R16 design**: Two variations. V-01 isolates C-39 (T-37 CONDITION has Part 1 only — inline failure exemplar present, correct-format prescription absent) while demonstrating C-40 + C-41 both pass. V-02 isolates C-40 with C-41 cascade (T-38 CONDITION is abstract-only — names condition category without exemplifying a deficient T-37 CONDITION form).

**Confirmed discriminators:**

**C-39 independent fail re-confirmed by V-01**: V-01 provides a second live demonstration of the C-39-independent-fail pattern: C-38 PASS (inline failure exemplar present in T-37 CONDITION), C-39 FAIL (correct-format prescription absent). T-39 fires; Finding 1: T-39.

**V-01 R16 as T-40/T-41 silent-trigger exemplar and C-42/C-43 source**: V-01 passes C-40 (T-38 CONDITION carries Part 1 — inline exemplar of an abstract T-37 CONDITION form) and C-41 (T-38 CONDITION carries Part 2 — correct-format prescription of a passing T-37 CONDITION). The closure behavior — T-40 and T-41 are silent — is the R16 excellence signal. T-40 being silent confirms that T-40 is a named, operational trigger with a CONDITION field that evaluates whether T-38 CONDITION carries Part 1 (satisfying C-40). T-41 being silent confirms the same for Part 2 (C-41). Both triggers having evaluable CONDITION fields and silencing correctly when C-40 and C-41 pass establishes T-40 and T-41 as first-class amendment table entries whose CONDITION field quality is now independently observable and checkable — the source of C-42 and C-43.

**T-40 and T-41 operational trigger structure (R16)**:
- T-40 fires when C-40 fails — when the T-38 CONDITION field lacks Part 1 (no inline exemplar showing what an abstract-only T-37 CONDITION looks like)
- T-41 fires when C-41 fails — when the T-38 CONDITION field has Part 1 but lacks Part 2 (no correct-format prescription)
- In V-01 R16, C-40 and C-41 both pass → T-40 and T-41 are both silent; findings: T-39 only (C-39 FAIL)
- In V-02 R16, C-40 fails and C-41 cascades → T-40 fires, T-41 fires; findings: T-40 (Finding 1), T-41 (Finding 2)

This is structurally analogous to how T-38/T-39 watch the quality of the T-37 CONDITION cell (R15 observation), with T-40/T-41 watching the quality of the T-38 CONDITION cell one level up.

**C-40 independent-fail boundary confirmed by V-02**: V-02's T-38 CONDITION is abstract — "fires if T-37 CONDITION lacks an inline failure exemplar" — naming the condition category without quoting or paraphrasing a deficient T-37 CONDITION form. This fails C-40 (no inline exemplar of an abstract T-37 form in the T-38 CONDITION cell) and cascades to C-41 FAIL (abstract entry contains neither Part 1 nor Part 2). V-02 confirms the deterministic cascade: C-40 FAIL → C-41 FAIL.

**C-41 independent-fail boundary (not yet demonstrated)**: A T-38 CONDITION carrying only Part 1 without a correct-format prescription would pass C-40 and fail C-41 independently. No R16 variation hit this exact pattern. The independent fail is structurally established by criterion definition and C-41's testability note.

**C-42 and C-43 as T-40 CONDITION quality criteria**: Following the same structural principle that yielded C-40/C-41 from R15's T-38/T-39 silence observation, C-42 and C-43 impose the same two-part self-documentation standard on T-40's own CONDITION field. The cascade invariant is identical in form: C-42 FAIL → C-43 FAIL (an abstract T-40 CONDITION contains neither part); C-42 PASS does not guarantee C-43 PASS (Part 1 present, Part 2 absent is a valid independent-fail state for C-43).

**New cascade evidence for v17:**
- C-43 cascade from C-42: An abstract T-40 CONDITION (category statement only, no exemplar of what an abstract T-38 CONDITION looks like) fails both C-42 and C-43. C-42 FAIL → C-43 FAIL is deterministic.
- C-43 independent fail boundary: A T-40 CONDITION carrying only Part 1 without a correct-format prescription shows what a passing T-38 CONDITION entry looks like passes C-42 and fails C-43. No R16 variation hit this exact pattern. The independent fail is structurally established by criterion definition and C-43's testability note.
- C-24 version-bump cascade: All R16 variations had 41-row amendment tables (one per C-01..C-41, correct under v16). Under v17, all R16 variations fail C-24 (43 rows required: T-42 and T-43 absent). This is the expected version-bump cascade.

---

## Round 17 Discriminator Notes

**R17 design**: Golden run (top_score 99.72 = 35/36 under v17). Two new excellence patterns identified from the golden artifact's amendment table structure.

**Confirmed discriminators:**

**Three-tier self-documentation chain confirmed at T-40 level**: The R17 golden artifact demonstrates that T-37/T-38/T-40 CONDITION fields each carry the same two-part self-documentation structure — Part 1 (failure exemplar) and Part 2 (correct-format prescription) — with the one-directional cascade invariant (Part-1-only PASS does not force Part-2 PASS) applying identically at all three tiers. This chain confirmation at the T-40 level establishes that T-42 and T-43 are operational triggers with evaluable CONDITION fields, following the same pattern as R15's T-38/T-39 silence confirmation and R16's T-40/T-41 silence confirmation. T-42's CONDITION field quality — whether it carries an inline exemplar of a deficient T-40 CONDITION form — is now independently observable and is the source of C-45.

**Meta-exemplar content requirement confirmed (C-44 source)**: The R17 golden artifact establishes that the T-40 CONDITION's Part 1 exemplar must include not only a quotation of the deficient T-38 CONDITION form but also an explanation of why that form is abstract — specifically, that it names the trigger condition category without showing what a deficient T-37 CONDITION entry looks like. This explanation-of-abstractness is required content within the exemplar construct itself. A T-40 CONDITION that quotes "fires if T-38 CONDITION lacks an inline failure exemplar" passes C-42 (exemplar present) but fails C-44 if it does not additionally explain the abstractness of that quoted form. The R17 top score of 99.72 (35/36 under v17) indicates one aspirational criterion fell short; under v18, C-44 and C-45 provide the criteria that capture this pattern.

**C-44 as a C-42 Part 1 content refinement**: C-44 is not a second Part (like C-43 is Part 2 to C-42's Part 1). C-44 is a content-specificity requirement on Part 1 itself — the exemplar must do two things: (1) quote the deficient T-38 CONDITION form, and (2) explain why that form is abstract. C-43 (Part 2: correct-format prescription) is independently required alongside C-44. The three requirements on T-40's CONDITION are therefore: C-42 (exemplar present), C-44 (exemplar includes explanation-of-abstractness), and C-43 (correct-format prescription present). C-42 FAIL → C-44 FAIL and C-42 FAIL → C-43 FAIL (both cascade). C-43 and C-44 fail modes are independent of each other.

**C-45 as chain-extension to T-42 tier**: C-45 follows the same derivation logic as C-40 (from R15: T-38 CONDITION must carry exemplar of deficient T-37 form) and C-42 (from R16: T-40 CONDITION must carry exemplar of deficient T-38 form). C-45 requires T-42's CONDITION to carry an inline exemplar of a deficient T-40 CONDITION form — the next step in the chain, confirmed viable by R17's three-tier chain observation.

**T-42 and T-43 operational trigger structure (R17)**:
- T-42 fires when C-42 fails — when the T-40 CONDITION field lacks Part 1 (no inline exemplar showing what an abstract-only T-38 CONDITION looks like)
- T-43 fires when C-43 fails — when the T-40 CONDITION field has Part 1 but lacks Part 2 (no correct-format prescription)
- T-44 fires when C-44 fails — when the T-40 CONDITION's exemplar lacks an explanation of why the quoted T-38 form is abstract
- T-45 fires when C-45 fails — when the T-42 CONDITION field lacks an inline exemplar of a deficient T-40 CONDITION form

**New cascade evidence for v18:**
- C-44 cascade from C-42: An absent exemplar in T-40's CONDITION (C-42 FAIL) also fails C-44 (no exemplar → no explanation-of-abstractness content). C-42 FAIL → C-44 FAIL is deterministic.
- C-44 independent fail boundary: A T-40 CONDITION carrying a quoted deficient T-38 form (C-42 PASS) but no explanation of why it is abstract passes C-42 and fails C-44. No pre-R17 variation demonstrated this exact pattern. The independent fail is structurally established by the meta-exemplar content requirement and C-44's testability note.
- C-45 is independently testable at the T-42 row: a reviewer reads T-42's CONDITION cell and confirms whether a quoted or paraphrased deficient T-40 CONDITION form is present.
- C-24 version-bump cascade: All R17 variations had 43-row amendment tables (one per C-01..C-43, correct under v17). Under v18, all R17 variations fail C-24 (45 rows required: T-44 and T-45 absent). This is the expected version-bump cascade.

---

## Round 18 Discriminator Notes

**R18 design**: Five variations, two new excellence patterns identified. V-03 (Phrasing Register) is the top performer and the source of both signals. V-01 and V-05 demonstrate cascade root failure modes. V-02 and V-04 demonstrate C-44 independent fail (exemplar present, explanation absent).

**Confirmed discriminators:**

**Specification phrasing register fidelity confirmed by V-03**: V-03 demonstrates that spec phrasing register is load-bearing: where the T-40 spec used explicit labeled structure ("Part 1: exemplar + explanation / Part 2: prescription"), the LLM output precisely mirrored that structure, producing C-42 PASS + C-44 PASS + C-43 PASS simultaneously. Where T-42's spec used category-only language, the LLM output mirrored the abstraction level — T-42 CONDITION abstract in output → C-45 FAIL. The model does not upgrade abstract specs: category-only language in the spec produces category-only output regardless of what the rubric requires. This is the R18 source signal for C-46 and C-47: T-42's CONDITION spec must be written with explicit Part 1/Part 2 labeled directives (and explanation-of-abstractness in Part 1) to produce an output that satisfies C-45, C-46, and C-47.

**Triple-layer T-40 cascade immunity confirmed by V-03**: V-03 is the first variation to demonstrate C-42 PASS + C-44 PASS + C-43 PASS simultaneously. V-02 and V-04 both demonstrated the partial-pass pattern: C-42 PASS (exemplar present), C-44 FAIL (explanation absent), C-43 FAIL (prescription absent). V-03's triple-layer pass confirms that all three directives in the spec together are sufficient — not just necessary — to produce cascade immunity across C-42/C-43/C-44. The triple-layer structure at T-40 is the minimum spec content for achieving 0 fails across the three criteria.

**C-44 independent fail confirmed by V-02 and V-04**: Both V-02 and V-04 demonstrate the C-44-independent-fail pattern: T-40 CONDITION carries a quoted deficient T-38 form (C-42 PASS) but no explanation of why that form is abstract (C-44 FAIL), and no correct-format prescription (C-43 FAIL). V-02's failure was from omitted explanation directive in the spec; V-04's failure was from the same omission pattern combined with a C-24 stale-table fail. Both confirm that C-42 PASS is not sufficient for C-44 PASS and is not sufficient for C-43 PASS — each requires an independently present directive in the T-40 CONDITION cell.

**V-03 single-point calibration proof**: V-03's design — one deliberately abstract T-42 spec, everything else explicit — confirms the rubric is correctly calibrated at the 37-criterion level: all 37 other criteria are genuinely satisfiable without interdependence, and C-45 is a clean single-point failure with no cascade surface into other non-T-42 criteria. Under v19, C-45 FAIL cascades to C-46 FAIL and C-47 FAIL; under v20, C-45 FAIL further cascades to C-48 FAIL and C-49 FAIL. All cascade terms from a single abstract T-42 spec confirm the chain structure is deterministic.

**V-05 cascade root behavior confirmed**: V-05's C-23 root fail (P×I computed inline in Phase 2 RISK rather than `[R-NN pending]`) cascades 14 criteria deep including C-42/C-44/C-45, all of which fail independently from the T-40/T-42 abstract specs. V-05 confirms the non-interaction between the register-linkage cascade chain and the amendment-table self-documentation chain: fixing C-23 would leave C-42/C-44/C-45 as independent residual fails.

**T-46 and T-47 operational trigger structure (R18)**:
- T-46 fires when C-46 fails — when the T-42 CONDITION field carries an exemplar (C-45 PASS) but lacks a correct-format prescription (Part 2 absent)
- T-47 fires when C-47 fails — when the T-42 CONDITION's exemplar lacks an explanation of why the quoted T-40 form is abstract

**C-46 as T-42 Part 2 criterion**: C-46 follows the same derivation as C-43 (T-40 Part 2) and C-41 (T-38 Part 2) and C-39 (T-37 Part 2). The correct-format prescription must state what a passing T-40 CONDITION entry looks like: the three-component form that satisfies C-42 + C-44 + C-43. C-46 is independently testable from C-45: exemplar present, prescription absent is the C-46-independent-fail state (not yet demonstrated live at time of R18; first live demonstration: V-03 R19).

**C-47 as T-42 explanation-of-abstractness criterion**: C-47 follows the same derivation as C-44 (T-40 explanation-of-abstractness). The explanation must state why the quoted T-40 CONDITION form is abstract — naming that it states only a condition category without showing what a deficient T-38 CONDITION entry looks like. C-47 is independently testable from C-45 and C-46: exemplar present, explanation absent is the C-47-independent-fail state (not yet demonstrated live at time of R18; first live demonstration: V-02 R19).

**New cascade evidence for v19:**
- C-46 cascade from C-45: A T-42 CONDITION carrying no inline exemplar (C-45 FAIL) also fails C-46 (no exemplar → no correct-format prescription content). C-45 FAIL → C-46 FAIL is deterministic.
- C-46 independent fail boundary: A T-42 CONDITION carrying a quoted deficient T-40 form (C-45 PASS) but no correct-format prescription passes C-45 and fails C-46. Not yet demonstrated live at time of R18.
- C-47 cascade from C-45: A T-42 CONDITION carrying no inline exemplar (C-45 FAIL) also fails C-47 (no exemplar → no explanation-of-abstractness). C-45 FAIL → C-47 FAIL is deterministic.
- C-47 independent fail boundary: A T-42 CONDITION carrying a quoted deficient T-40 form (C-45 PASS) but no explanation of why it is abstract passes C-45 and fails C-47. Not yet demonstrated live at time of R18.
- C-46 and C-47 mutual independence: Confirmed structurally — exemplar with explanation but no prescription (C-47 PASS, C-46 FAIL) and exemplar with prescription but no explanation (C-47 FAIL, C-46 PASS) are distinct states. No live demonstration yet at time of R18.
- C-24 version-bump cascade: All R18 variations had 45-row amendment tables (one per C-01..C-45, correct under v18). Under v19, all R18 variations fail C-24 (47 rows required: T-46 and T-47 absent). This is the expected version-bump cascade.

---

## Round 19 Discriminator Notes

**R19 design**: Five variations. V-03 (Part 1 Explicit+Labeled, Part 2 Absent) is the top performer under v19 (39/40 = 99.75) and the source of Signal 1. V-02 (Exemplar-Only) demonstrates C-46 FAIL + C-47 FAIL simultaneously and is the source of Signal 2. V-01 demonstrates C-45 cascade root. V-04 combines stale C-24 with the V-02 pattern. V-05 combines C-23 cascade root with T-42 and T-40 abstract specs.

**Confirmed discriminators:**

**C-46 independent fail confirmed live by V-03**: V-03's T-42 CONDITION carries an explicitly labeled "Part 1 — Failure exemplar with explanation" structure with full content (quoted deficient T-40 form + explanation of why it is abstract) but no "Part 2" label and no Part 2 content. C-45 PASS (exemplar present and unambiguous), C-47 PASS (explanation-of-abstractness present in Part 1), C-46 FAIL (Part 2 prescription absent). T-46 fires; T-47 is silent. This is the first live demonstration of the C-46-independent-fail state: C-45 PASS + C-47 PASS + C-46 FAIL simultaneously. The labeled Part 1 structure confirms the phrasing-register fidelity principle in both directions: explicit labeled content in Part 1 produces a correct Part 1 output (C-47 PASS); absent Part 2 label produces absent Part 2 output (C-46 FAIL). The model does not infer the existence of Part 2 from the presence of Part 1.

**C-47 independent fail confirmed live by V-02**: V-02's T-42 CONDITION carries a quoted deficient T-40 form verbatim (exemplar present — C-45 PASS) but no explanation-of-abstractness directive and no prescription directive. C-45 PASS, C-46 FAIL (independent — no prescription), C-47 FAIL (independent — no explanation). Both T-46 and T-47 fire. This is the first live demonstration of the C-47-independent-fail state (C-45 PASS + C-47 FAIL) and simultaneously confirms C-46 independent fail again (C-45 PASS + C-46 FAIL). V-02 also confirms that C-46 FAIL and C-47 FAIL can occur together independently — neither cascades from the other.

**C-46 and C-47 mutual independence confirmed live (V-02 vs. V-03 comparison)**:
- V-02: C-45 PASS, C-46 FAIL, C-47 FAIL — exemplar present, both explanation and prescription absent
- V-03: C-45 PASS, C-46 FAIL, C-47 PASS — exemplar + explanation present, prescription absent

V-03 demonstrates that C-47 can pass while C-46 fails (explanation present, prescription absent). V-02 demonstrates that both can fail simultaneously. No variation yet demonstrates C-46 PASS + C-47 FAIL (exemplar + prescription, no explanation) — this state is structurally established but not yet live-tested.

**V-03 labeled-Part-1 structure as phrasing-register anchor**: V-03 establishes a new dimension of the phrasing-register fidelity principle: an explicit "Part 1 — [content description]" label in the spec is sufficient to anchor a correct Part 1 output. The label serves as a structural anchor — the LLM mirrors the labeled structure faithfully, producing the labeled Part 1 content in full. The absence of a "Part 2" label in the spec produces the absence of Part 2 content in the output. This confirms that label presence (not just content presence) is a load-bearing spec element.

**C-46 + C-47 two-fail ceiling for V-02 class specs**: V-02 establishes that a T-42 CONDITION carrying only a verbatim exemplar (no explanation, no prescription) produces exactly two independent fails — C-46 and C-47 — with no further cascade beyond the C-45-derived chain. The two-fail ceiling is clean: fixing both the prescription and the explanation directives in the spec would yield C-46 PASS + C-47 PASS simultaneously.

**C-46 one-fail ceiling for V-03 class specs**: V-03 establishes that a T-42 CONDITION with explicit Part 1 (exemplar + labeled explanation) but no Part 2 produces exactly one fail at the C-45/C-46/C-47 cluster: C-46 FAIL only. The one-fail ceiling requires the addition of a "Part 2" label and prescription directive to reach 0 fails at this cluster.

**T-48 and T-49 operational trigger structure (R19)**:
- T-48 fires when C-48 fails — when the T-46 CONDITION field lacks an inline exemplar of the V-03-class state (T-42 CONDITION with Part 1 labeled and present but no Part 2 label and no Part 2 content)
- T-49 fires when C-49 fails — when the T-47 CONDITION field lacks an inline exemplar of the V-02-class state (T-42 CONDITION with quoted deficient T-40 form but no explanation-of-abstractness)
- T-48 is silent when C-48 passes — when T-46's CONDITION carries the Part-1-only exemplar; no finding generated for T-48
- T-49 is silent when C-49 passes — when T-47's CONDITION carries the exemplar-without-explanation exemplar; no finding generated for T-49

In V-03 R19, T-46 fires (C-46 FAIL) and T-47 is silent (C-47 PASS). T-48 also fires (C-48 FAIL) because T-46's CONDITION cell is abstract — it names the condition without carrying the V-03-class exemplar. T-49 fires (C-49 FAIL) because T-47's CONDITION cell is also abstract — it names the condition without carrying the V-02-class exemplar.

**C-48 and C-49 as T-46/T-47 CONDITION quality criteria**: Following the identical structural derivation as C-40 (T-38 CONDITION exemplar from R15 chain), C-42 (T-40 CONDITION exemplar from R16 chain), and C-45 (T-42 CONDITION exemplar from R17 chain), C-48 and C-49 impose the exemplar-presence requirement on T-46 and T-47 CONDITION cells respectively. The cascade invariants are identical in form: C-45 FAIL → C-48 FAIL and C-45 FAIL → C-49 FAIL (the exemplar states T-46 and T-47 must demonstrate require T-42 Part 1 to exist). C-45 PASS does not guarantee C-48 PASS or C-49 PASS — T-46 and T-47 CONDITION cells can be abstract even when T-42 has Part 1. C-48 and C-49 are mutually independent.

**New cascade evidence for v20:**
- C-48 cascade from C-45: A fully abstract T-42 CONDITION (C-45 FAIL) makes the Part-1-present-Part-2-absent state that T-46's C-48 exemplar must show structurally unreachable — the state requires T-42 Part 1 to exist. C-45 FAIL → C-48 FAIL is deterministic.
- C-48 independent fail (V-03 R19): T-46 CONDITION is abstract in V-03 despite C-45 PASS and C-46 FAIL. The Part-1-only T-42 state is live and observable, but T-46's CONDITION cell does not quote it. C-45 PASS does not guarantee C-48 PASS. C-46 FAIL does not cascade to C-48 FAIL.
- C-49 cascade from C-45: A fully abstract T-42 CONDITION (C-45 FAIL) makes the exemplar-present-explanation-absent state that T-47's C-49 exemplar must show structurally unreachable. C-45 FAIL → C-49 FAIL is deterministic.
- C-49 independent fail (V-02 R19): T-47 CONDITION is abstract in V-02 despite C-45 PASS and C-47 FAIL. The exemplar-without-explanation T-42 state is live and observable, but T-47's CONDITION cell does not quote it. C-45 PASS does not guarantee C-49 PASS. C-47 FAIL does not cascade to C-49 FAIL.
- C-48 and C-49 mutual independence: Both fail in V-02 R19 and in V-03 R19. Confirmed structurally — T-46 CONDITION can carry its exemplar (C-48 PASS) while T-47 CONDITION lacks its exemplar (C-49 FAIL) and vice versa. No live demonstration of the asymmetric case yet.
- C-24 version-bump cascade: All R19 variations had 47-row amendment tables (one per C-01..C-47, correct under v19). Under v20, all R19 variations fail C-24 (49 rows required: T-48 and T-49 absent). This is the expected version-bump cascade.
