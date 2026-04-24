**What changed from v12:**

**Two new aspirational criteria extracted from R12 excellence signals:**

| ID | Criterion | Source Axis | Independence from Parent |
|----|-----------|-------------|--------------------------|
| C-36 | **Phase 9b Domain 1 back-fill includes P×I compound scores** | V-02 excellence signal 1 | C-35 requires `[R-NN pending] → [R-NN entries]` transition notation per citation site. C-36 requires the entries in the back-fill transition to carry the computed P×I compound scores from the register alongside the R-NN identifiers. Satisfying C-35 (transition notation present) does not satisfy C-36 — a back-fill showing `[R-NN pending] → [R-03, R-07]` passes C-35 (before/after notation present) but fails C-36 (no P×I scores). A back-fill showing `[R-NN pending] → [R-03 (P:2 × I:4 = 8), R-07 (P:3 × I:3 = 9)]` passes both. C-36 makes each back-filled RISK field self-contained: the option anatomy carries the full risk score without requiring a register lookup at review time. |
| C-37 | **Phase 9b Domain 2 per-option-column R-NN attribution** | V-02 excellence signal 2 | C-32 requires Domain 2 (comparison matrix risk column) to be named as a structural domain in Phase 9b enumeration. C-37 requires the Domain 2 enumeration to attribute specific R-NN IDs to each option's column in the comparison matrix risk row, not just confirm that R-NN IDs appear in the row globally. Satisfying C-32 (domain named) does not satisfy C-37 — a Domain 2 entry stating "comparison matrix risk row: R-NN IDs inserted" passes C-32 but fails C-37 (no per-column attribution). A Domain 2 entry with per-column attribution ("OPTION-A column: R-03, R-07 \| OPTION-B column: R-01 \| do-nothing column: R-02") passes both. C-37 extends register-to-document traceability from option anatomy (Domain 1) into individual comparison matrix cells (Domain 2). |

**Denominator:** `/28` → `/30`. Each aspirational criterion = `10/30` = `0.333` points.

**Score projections under v13:**
| Variation | v12 fails | v13 cascade adds | Total fails | Composite |
|-----------|-----------|-----------------|-------------|-----------|
| V-02 motivated (C-36, C-37 both pass) | C-22 | — | 1 | **99.67** |
| V-04 R12 (C-25, C-33, C-35) | 3 | C-36 cascade from C-35; C-37 fail (Domain 2 outcome-only) | 5 | **98.33** |
| V-05 R12 (C-32, C-34, C-35) | 3 | C-36 cascade from C-35; C-37 cascade from C-32 | 5 | **98.33** |
| V-03 R12 (C-24, C-32, C-33, C-34, C-35) | 5 | C-36 cascade from C-35; C-37 cascade from C-32 | 7 | **97.67** |
| V-01 R12 (C-23 cascade: seven fails) | 7 | C-36 cascade from C-35; C-37 cascade from C-32 | 9 | **97.00** |

**Cascade invariants:**
- **C-36 cascade**: Any variation failing C-35 (no per-site transition notation) also fails C-36 — P×I scores cannot appear inside a notation that was never authored.
- **C-37 cascade from C-32**: Any variation failing C-32 (no structural domain enumeration) also fails C-37 — no Domain 2 enumeration exists to carry per-column attribution.
- **C-37 independent fail**: A variation can pass C-32 (Domain 2 named) and C-34 (Domain 2 index prefix present) while still failing C-37 when Domain 2 confirms R-NN presence at the row level only, without per-column attribution. V-04 demonstrates this: "(2) Comparison matrix risk column — confirm R-NN IDs are present in the risk row" names the domain (C-32 PASS, C-34 PASS) but provides no per-column breakdown (C-37 FAIL).

**C-37 V-02 exemplar**: V-02 Phase 9b Domain 2: "Risk row: [R-NN IDs inserted per option column]" — per-column attribution confirmed. The exemplar language explicitly names the per-column granularity as the target structure.

---

## Structural Testability Notes

- **C-22** is structurally testable: a reviewer reads the coverage table header and confirms whether a CLOSED BY column is present. No row scan required.
- **C-23** is structurally testable: a reviewer reads any option RISK field in the final output and confirms whether it contains R-NN identifiers or inline P×I notation. A single RISK field with inline scoring fails C-23 regardless of other options.
- **C-24** is structurally testable at PRE-DOCUMENT: a reviewer counts the amendment table rows at initialization. For v13, expected count = 37 (one row per C-01..C-37). A count of 35 (v12 table carried forward without adding T-36 and T-37) fires C-24 at PRE-DOCUMENT.
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

The R12 discriminator pattern confirms C-36 and C-37 structural independence: V-02 provided P×I scores in Domain 1 transition entries (C-36 PASS) and per-column attribution in Domain 2 (C-37 PASS). V-04 provided domain-indexed Phase 9b (C-34 PASS, C-32 PASS) with only outcome notation at Domain 1 sites and only row-level confirmation at Domain 2 — C-36 FAIL (no P×I in V-04's notation), C-37 FAIL (no per-column attribution). V-05's aggregate Phase 9b failed C-32, C-34, C-35, C-36, C-37 simultaneously — the aggregate "back-fill complete" form collapses all five discrimination axes at once.

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

## Aspirational Criteria (10% of composite, denominator /30)

### C-01 through C-07 — Mandatory C-tier (not counted in /30 denominator)

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

### C-08 through C-37 — Aspirational Criteria (denominator /30)

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
| C-24 | **Amendment table row count matches v13 criterion count** | behavior | Amendment table contains exactly 37 trigger rows at initialization (one per C-01..C-37 criterion). A table built from v12's criterion list (35 rows) without adding T-36 and T-37 fires C-24 at PRE-DOCUMENT. A table with any count other than 37 fails C-24. |
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

---

## Scoring Formula

```
composite = (essential_pass / 4 × 60)
          + (required_pass / 3 × 30)
          + (aspirational_pass / 30 × 10)
```

When all essential and required criteria pass, the formula simplifies to:

```
composite = 90 + (aspirational_pass / 30 × 10)
```

**Golden threshold**: all 4 essential criteria pass AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Golden | all essential + >= 80 | Ready for use as a reference artifact |
| Passing | all essential + >= 60 | Usable with minor gaps |
| Failing | any essential fails | Output is not a valid proposal |

**Score reference under v13:**
| Aspirational passes | Composite |
|---------------------|-----------|
| 30/30 | 100.00 |
| 29/30 | 99.67 |
| 28/30 | 99.33 |
| 27/30 | 99.00 |
| 26/30 | 98.67 |
| 25/30 | 98.33 |
| 24/30 | 98.00 |
| 23/30 | 97.67 |
| 21/30 | 97.00 |
| 20/30 | 96.67 |

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
- Phase 9b domain-indexed (C-34 PASS, C-32 PASS) but per-site output states only the final state: "the R-NN IDs applied to its RISK field" — no `[R-NN pending] → [R-NN IDs]` transition arrow — fails C-35 (V-04 failure mode)
- Phase 9b aggregate confirmation: "all [R-NN pending] placeholders resolved; back-fill complete" — no structural domains named, no domain-index prefixes, no per-site entries — fails C-32, C-34, C-35, C-36, C-37 simultaneously (V-05 failure mode)
- Phase 9b Domain 1 shows per-site transition notation (C-35 PASS) but entries list only R-NN IDs without P×I scores: `[R-NN pending] → [R-03, R-07]` — fails C-36; satisfies C-35
- Phase 9b Domain 2 carries index prefix (C-34 PASS) and is named as structural domain (C-32 PASS) but confirms only row-level R-NN presence ("R-NN IDs cited in risk row") without per-option-column attribution — fails C-37 (V-04 Domain 2 failure mode)
- Amendment table built from v12 criterion list (35 rows) without adding T-36 and T-37 — fires C-24 at PRE-DOCUMENT; score ceiling capped at 29/30 if C-24 is the only fail, but the stale table will also miss T-36 and T-37 trigger definitions, preventing C-36 and C-37 from being enforced
- Finalization executed as prose narrative ("walk through the document for completeness") rather than numbered steps — fails C-25 regardless of content quality
- PM contribution absent from risk register; all R-NN entries authored by Architect — fails C-04
- Phase headers carry no `[GATE: X-NN]` citations; gate audit has nothing to verify — fails C-21

---

## Round 1–11 Discriminator Summary

For early-round discriminator notes (R1–R11), see the v12 rubric file. The v13 rubric inherits all prior discriminator observations unchanged.

---

## Round 12 Discriminator Notes

**R12 design**: Five variations, two new criteria (C-34, C-35 under v12). Single-axis variations V-01..V-03 isolate individual failure modes; V-04 and V-05 combine axes.

**Confirmed discriminators:**

**C-34 isolation by V-04**: The "(1)"/"(2)" ordinal form satisfies C-34's numeric-index-prefix requirement. V-04 demonstrates C-34 PASS with ordinal-indexed domain headers while failing C-35 (per-site outcome-only notation). C-34 is therefore satisfiable without "Domain N —" canonical form — ordinal equivalents qualify.

**C-35 isolation by V-04**: V-04 provides the cleanest C-35 isolation: C-31 PASS (placeholder at Phase 2), C-32 PASS (both domains named), C-34 PASS (ordinal prefixes), C-35 FAIL (outcome-only: "the R-NN IDs applied to its RISK field" without before/after transition). The discriminating property: C-35 requires the before-state (`[R-NN pending]`) and the after-state (R-NN IDs) to appear together in a single arrow notation at each site.

**C-32 + C-34 + C-35 cascade from aggregate Phase 9b (V-05)**: An aggregate confirmation form ("Citation-site enumeration: all [R-NN pending] placeholders resolved; back-fill complete") collapses C-32, C-34, and C-35 simultaneously. No structural domain names → C-32 FAIL. No domains to carry index prefixes → C-34 FAIL. No per-site entries → C-35 FAIL. The aggregate shortcut is a single authoring decision that fails three independent structural requirements. Under v13, the same aggregate form also cascades to C-36 FAIL (no per-site entries to carry P×I) and C-37 FAIL (no Domain 2 enumeration to carry per-column attribution) — five simultaneous failures from one shortcut.

**V-02 as C-34 + C-35 + C-36 + C-37 exemplar**: V-02's Phase 9b demonstrates the ceiling behavior for all four register-linkage depth criteria simultaneously:
- C-34 PASS: "Domain 1 —" / "Domain 2 —" explicit numeric-index domain headers
- C-35 PASS: `[OPTION-A label] RISK field: [R-NN pending] → [applicable R-NN entries, P×I scores]` arrow notation per site
- C-36 PASS: P×I compound scores included in the transition target alongside R-NN IDs
- C-37 PASS: "Risk row: [R-NN IDs inserted per option column]" per-column attribution for Domain 2

V-02's one failure (C-22: CLOSED BY column absent from compact-format coverage table) is orthogonal to the register-linkage axis. The score of 27/28 under v12 projects to 29/30 under v13.

**New cascade evidence for v13:**
- C-37 independent fail from V-04: V-04 passes C-32 (Domain 2 named) and C-34 (index prefix) but fails C-37 (Domain 2 row-level only, no per-column attribution). This confirms C-37 is independently testable from C-32 and C-34 — a variation can name the domain and prefix it correctly while still providing only aggregate Domain 2 confirmation.
- C-36 cascade invariant confirmed: C-36 requires P×I scores in the transition entries. Any variation failing C-35 (no transition notation) cannot provide P×I in notation that was never authored. The cascade is deterministic: C-35 FAIL → C-36 FAIL. No variation in R12 passed C-35 while failing C-36 (or vice versa in the cascade direction).

**No new criterion warranted** from the V-03 stale-table finding. The stale table (31 rows for v12 criteria) causes C-24 to fire at PRE-DOCUMENT and prevents T-32..T-35 triggers from firing as named triggers during finalization — but the behavioral failures (C-32, C-33, C-34, C-35) are independently assessable by the rubric regardless of whether the trigger table captures them. The stale-table failure mode is documented in Common Failure Modes.
