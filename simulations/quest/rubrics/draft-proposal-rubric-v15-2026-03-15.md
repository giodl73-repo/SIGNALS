**What changed from v14:**

**One new aspirational criterion extracted from R14 excellence signals:**

| ID | Criterion | Source Axis | Independence from Parent |
|----|-----------|-------------|--------------------------|
| C-39 | **Amendment table T-37 trigger entry includes correct-format prescription alongside the inline failure exemplar** | V-02 R14 C-38 PASS note | C-38 requires the T-37 CONDITION field to carry an inline failure exemplar quoting the exact construct that fires T-37. C-39 requires T-37 CONDITION to additionally carry an explicit correct-format prescription — stating the replacement format that would satisfy C-37. A T-37 entry stating "row-level confirmation 'R-NN IDs applied to risk row' fires T-37" passes C-38 but fails C-39 (no correct format stated). V-02 R14 demonstrated the two-part target: "row-level confirmation 'R-NN IDs applied to risk row' fires T-37; per-column format required: [OPTION-A column: R-NN IDs] \| [OPTION-B: R-NN IDs]" — Part 1 quotes the failure construct (C-38), Part 2 prescribes the correct form (C-39). The full two-part entry makes T-37 self-documenting at both levels: a reviewer can determine what fires T-37 and what would satisfy C-37 without consulting the rubric or Phase 9b. |

**Denominator:** `/31` → `/32`. Each aspirational criterion = `10/32` = `0.3125` points.

**Score projections under v15 for R14 variations:**

| Variation | v14 fails | v15 cascade adds | Total fails | Composite |
|-----------|-----------|-----------------|-------------|-----------|
| V-02 R14 (C-37 FAIL; C-38 PASS, C-39 PASS) | C-37 | none | 1 | **99.69** |
| V-01 R14 (C-38 FAIL: abstract T-37; C-39 FAIL by cascade) | C-38 | C-39 (no correct format in abstract entry) | 2 | **99.38** |
| V-03 R14 (C-24 FAIL: 37 rows < 38; C-38 FAIL: abstract T-37; C-39 FAIL by cascade) | C-24, C-38 | C-39 (no correct format in abstract entry) | 3 | **99.06** |

**Cascade invariants:**

- **C-39 cascade from C-38**: A T-37 CONDITION that is abstract (fails C-38, no failure exemplar) also fails C-39 — an abstract single-sentence condition contains neither Part 1 nor Part 2 of the two-part structure. C-38 FAIL → C-39 FAIL is deterministic.
- **C-39 independent fail**: A T-37 CONDITION carrying the inline failure exemplar (C-38 PASS, Part 1 present) but stopping there — no correct-format prescription — fails C-39 while passing C-38. C-39 is independently testable: a reviewer reads the T-37 CONDITION cell for a stated replacement format beyond the failure quote.
- **C-24 version-bump cascade**: All R14 variations had 38-row amendment tables (or 37-row for V-03). Under v15, all R14 variations with 38-row tables fail C-24 (39 rows required). V-03's 37-row table fails C-24 under both v14 and v15.

**Key changes to existing criteria:**
- **C-24**: updated from "exactly 38 trigger rows" → "exactly 39 trigger rows (one per C-01..C-39)"
- **Scoring formula denominator**: `/31` → `/32`

---

## Structural Testability Notes

- **C-22** is structurally testable: a reviewer reads the coverage table header and confirms whether a CLOSED BY column is present. No row scan required.
- **C-23** is structurally testable: a reviewer reads any option RISK field in the final output and confirms whether it contains R-NN identifiers or inline P×I notation. A single RISK field with inline scoring fails C-23 regardless of other options.
- **C-24** is structurally testable at PRE-DOCUMENT: a reviewer counts the amendment table rows at initialization. For v15, expected count = 39 (one row per C-01..C-39). A count of 38 (v14 table carried forward without adding T-39) fires C-24 at PRE-DOCUMENT.
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

## Aspirational Criteria (10% of composite, denominator /32)

### C-01 through C-07 — Mandatory C-tier (not counted in /32 denominator)

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

### C-08 through C-39 — Aspirational Criteria (denominator /32)

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
| C-24 | **Amendment table row count matches v15 criterion count** | behavior | Amendment table contains exactly 39 trigger rows at initialization (one per C-01..C-39 criterion). A table built from v14's criterion list (38 rows) without adding T-39 fires C-24 at PRE-DOCUMENT. A table with any count other than 39 fails C-24. |
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
| C-37 | **Phase 9b Domain 2 per-option-column R-NN attribution** | behavior | The Domain 2 (comparison matrix risk column) enumeration in Phase 9b explicitly attributes specific R-NN IDs to each option's column in the risk row — not a domain-level confirmation that R-NN IDs appear somewhere in the row. Per-column attribution format: each option column is identified by label with its applicable R-NN IDs listed. A Domain 2 entry stating "Risk row: R-NN IDs cited" or "comparison matrix risk column updated" confirms domain presence (C-32 PASS) but provides no per-column traceability (C-37 FAIL). A Domain 2 entry with "Risk row: [OPTION-A column: R-03, R-07] [OPTION-B column: R-01] [do-nothing column: R-02]" passes C-37. Satisfying C-32 (domain named) and C-34 (domain carries index prefix) does not satisfy C-37 — per-column attribution is independently required. |
| C-38 | **Amendment table T-37 trigger entry includes inline failure-condition exemplar** | behavior | The T-37 row in the amendment table carries an inline exemplar note within the CONDITION field — a parenthetical or quoted construct showing the exact document language that fires T-37. The exemplar must quote or closely paraphrase what row-level Domain 2 confirmation looks like, e.g., "row-level confirmation 'R-NN IDs applied to risk row' fires T-37". A T-37 entry stating only "C-37: per-column attribution absent" without an inline exemplar quote fails C-38. Satisfying C-18 (trigger rules front-loaded) and C-29 (PHASE column populated) does not satisfy C-38 — the inline exemplar is independently required within the T-37 CONDITION field itself. The exemplar makes the trigger self-documenting: a reviewer assessing a Phase 9b Domain 2 entry can determine whether T-37 fires without consulting the rubric. |
| C-39 | **Amendment table T-37 trigger entry includes correct-format prescription alongside the inline failure exemplar** | behavior | The T-37 CONDITION field carries both the inline failure exemplar (Part 1, required by C-38) AND an explicit correct-format prescription (Part 2). Part 2 states the replacement format that would satisfy C-37 — naming the expected per-option-column attribution structure. The two-part structure makes the T-37 entry fully self-contained: a reviewer can determine both what fires T-37 and what would satisfy C-37 without consulting the rubric or Phase 9b. Target form: "row-level confirmation 'R-NN IDs applied to risk row' fires T-37; per-column format required: [OPTION-A column: R-NN IDs] \| [OPTION-B: R-NN IDs]". A T-37 CONDITION field carrying only Part 1 ("row-level confirmation 'R-NN IDs applied to risk row' fires T-37") without a correct-format prescription passes C-38 but fails C-39. Satisfying C-38 (failure exemplar present) does not satisfy C-39 — the correct-format prescription is independently required in the same CONDITION cell. |

---

## Scoring Formula

```
composite = (essential_pass / 4 × 60)
          + (required_pass / 3 × 30)
          + (aspirational_pass / 32 × 10)
```

When all essential and required criteria pass, the formula simplifies to:

```
composite = 90 + (aspirational_pass / 32 × 10)
```

**Golden threshold**: all 4 essential criteria pass AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Golden | all essential + >= 80 | Ready for use as a reference artifact |
| Passing | all essential + >= 60 | Usable with minor gaps |
| Failing | any essential fails | Output is not a valid proposal |

**Score reference under v15:**
| Aspirational passes | Composite |
|---------------------|-----------|
| 32/32 | 100.00 |
| 31/32 | 99.69 |
| 30/32 | 99.38 |
| 29/32 | 99.06 |
| 28/32 | 98.75 |
| 27/32 | 98.44 |
| 26/32 | 98.13 |
| 25/32 | 97.81 |
| 24/32 | 97.50 |
| 23/32 | 97.19 |
| 22/32 | 96.88 |
| 21/32 | 96.56 |
| 20/32 | 96.25 |

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
- Phase 9b Domain 1 shows per-site transition notation (C-35 PASS) but entries list only R-NN IDs without P×I scores: `[R-NN pending] → [R-03, R-07]` — fails C-36; satisfies C-35 (V-01 R13 failure mode; note "reference the register for compound scores" is authored clarification, not a rubric substitute)
- Phase 9b Domain 2 carries index prefix (C-34 PASS) and is named as structural domain (C-32 PASS) but confirms only row-level R-NN presence ("R-NN IDs cited in risk row") without per-option-column attribution — fails C-37 (V-02 R13 failure mode; "Risk row: R-NN IDs applied to risk row" is the exact firing condition for T-37)
- Amendment table built from v13 criterion list (37 rows) without adding T-38 — fires C-24 at PRE-DOCUMENT; also cascades to C-38 FAIL if T-37 entry lacks inline exemplar (stale table omits T-38 definition entirely, but T-37 entry may still pass C-38 if the exemplar note was present in the v13-era table)
- Amendment table built from v14 criterion list (38 rows) without adding T-39 — fires C-24 at PRE-DOCUMENT under v15; also cascades to C-39 FAIL (no T-39 entry to carry any correct-format prescription, and the existing T-38 entry does not substitute)
- Amendment table T-37 entry states trigger condition abstractly ("C-37: per-column attribution absent from Domain 2") without an inline exemplar quoting the failure construct — fails C-38 even when C-18 (front-loaded trigger rules) and C-29 (PHASE column) both pass; also fails C-39 by cascade (abstract entry contains neither Part 1 nor Part 2)
- Amendment table T-37 entry carries inline failure exemplar (C-38 PASS, Part 1 present) but stops there — no correct-format prescription stating what per-column attribution looks like — fails C-39; satisfies C-38 (V-01 R14 ceiling: T-37 abstract, both fail; the C-39-only-fail would arise in a variant that adds the failure exemplar without the replacement format)
- Finalization executed as prose narrative ("walk through the document for completeness") rather than numbered steps — fails C-25 regardless of content quality
- PM contribution absent from risk register; all R-NN entries authored by Architect — fails C-04
- Phase headers carry no `[GATE: X-NN]` citations; gate audit has nothing to verify — fails C-21

---

## Round 1–11 Discriminator Summary

For early-round discriminator notes (R1–R11), see the v12 rubric file. The v15 rubric inherits all prior discriminator observations unchanged.

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
- C-38 cascade from stale table: A table missing T-37 entirely (e.g., 37-row table omitting T-38 but having T-37) can still pass C-38 if T-37 carries the inline exemplar. A table missing T-37 (e.g., 35-row table stopping at T-35) fails C-38 by cascade — no T-37 entry exists to carry the exemplar. The cascade is: T-37 absent from amendment table → C-38 FAIL.
- C-38 independent fail: A 38-row table with T-37 present (C-24 PASS) but T-37 CONDITION entry carrying only an abstract condition statement (C-18 PASS, C-29 PASS) fails C-38. C-38 is independently testable: a reviewer reads the T-37 CONDITION cell specifically for an inline quoted exemplar, not just a condition category name.
- C-24 version-bump cascade: All R13 variations had 37-row amendment tables (or 35-row for V-03). Under v14, all R13 variations fail C-24 (38 rows required). This is the expected version-bump cascade — newly added criteria require T-38 in the amendment table.

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
- C-39 independent fail boundary: A T-37 CONDITION carrying only Part 1 ("row-level confirmation 'R-NN IDs applied to risk row' fires T-37") without Part 2 passes C-38 and fails C-39. No R14 variation hit this exact pattern; V-02 demonstrated the full two-part pass. The independent fail is structurally established by criterion definition and C-39's testability note.
- C-24 version-bump cascade: All R14 variations with 38-row tables fail C-24 under v15 (39 rows required). V-03's 37-row table fails C-24 under both v14 and v15.
