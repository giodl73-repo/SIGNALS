```markdown
# listen-support Quest Rubric — v12

## Version History

| Version | Change |
|---------|--------|
| v1 | Initial rubric — 8 essential/recommended criteria |
| v2 | Added C-11 (Phase as card field), C-12 (Fallback-grounded severity), C-13 (Mid-output verification block) from R1 excellence signals. Max: 115 pts |
| v3 | Added C-14 (Phase+Title coexistence), C-15 (Temporal adoption window severity), C-16 (Prior-tool coverage in verification) from R2 excellence signals. Max: 130 pts |
| v4 | Added C-17 (Phase-as-severity-key declaration), C-18 (Gate minimum correct at ≥7) from R3 excellence signals. Max: 140 pts |
| v5 | Added C-19 (TABLE CHECK halt instruction), C-20 (Gap analysis coverage verification block) from R4 excellence signals. Max: 150 pts |
| v6 | Added C-21 (Evidence-to-gap traceability with orphan-gap check), C-22 (Prohibited sentinel language on consequence fields) from R5 excellence signals. Max: 160 pts |
| v7 | Added C-23 (Belt-and-suspenders criterion satisfaction), C-24 (Materialized-view traceability instruction), C-25 (Criterion-ID-named final verification spine) from R6 excellence signals. Max: 175 pts |
| v8 | Added C-26 (Self-referential criterion enforcement), C-27 (Spine-as-sole-suspenders declaration) from R7 excellence signals. Max: 185 pts |
| v9 | Added C-28 (Compliance Contract spine-criterion anchoring), C-29 (Triple self-referential mechanism stack) from R8 excellence signals. Max: 195 pts |
| v10 | Added C-30 (Spine-row self-enforcement imperative), C-31 (Dual-load CONTRACT implementation), C-32 (Three-timing enforcement coverage) from R9 excellence signals. Max: 210 pts |
| v11 | Added C-33 (VM Row ID CF at constraint load), C-34 (VM Row ID CF in compliance contract), C-35 (VM Row ID CF in verification spine) from R10 excellence signals. Max: 225 pts |
| v12 | Added C-36 (Phase-indexed CF in CONSTRAINT MANIFEST), C-37 (VERIFICATION MANIFEST per-row CF column), C-38 (RESTATING POSITIONS names CONSTRAINT MANIFEST) from R11 excellence signals. Max: 240 pts |

---

## Scoring Scale

| Tier | Points | PARTIAL | FAIL |
|------|--------|---------|------|
| Essential (×5) | 12 | 6 | 0 |
| Recommended (×3) | 10 | 5 | 0 |
| Aspirational (×30) | 5 | 2 | 0 |

**Max composite:** 240 pts  
**Golden gate:** all_essential_pass = TRUE AND composite ≥ 80

PARTIAL on any Essential criterion = all_essential_pass FALSE (Golden blocked regardless of composite).

---

## Essential Criteria (12 pts each, max 60)

### C-01 — Title field on card
Each ticket card includes `Title: [descriptive subject line]` as a named field. A ticket ID (`Ticket T-NN`) does not satisfy this criterion — Title must be a human-readable subject line that summarizes the feedback. A heading of the form `## T-NN — {Title}` does not satisfy this criterion; the title must appear as a discrete named field in the card body.

**PASS:** Every card has a `Title:` field with a descriptive value.  
**PARTIAL:** Title absent on some cards, or ticket ID used in place of subject line, or title embedded in heading only.  
**FAIL:** No title field on any card.

---

### C-02 — Controlled vocabulary declared and enforced
Phase, Category, Volume, and Severity use controlled vocabularies declared in the planning table. The model enforces values — no free-form variants accepted in scored fields.

**PASS:** Vocabulary table present; all card values match declared options.  
**PARTIAL:** Vocabulary declared but not consistently enforced.  
**FAIL:** Free-form values used; no vocabulary declaration.

---

### C-03 — First-person voice throughout
All ticket bodies written in first person. No role titles in body text. The voice constraint is stated explicitly in the prompt (e.g., "Write as me — first person throughout. No role titles in body text.").

**PASS:** All bodies pass first-person check; constraint is stated in prompt.  
**PARTIAL:** Constraint stated but some bodies break first-person or include role titles.  
**FAIL:** Constraint absent or systematically violated.

---

### C-04 — Gap analysis with three named sections
A gap analysis step (distinct from ticket generation) produces three sections: Doc Gaps, Design Gaps, Operational Gaps. Each section must reference ≥1 named artifact.

**PASS:** All three sections present, each with ≥1 named artifact.  
**PARTIAL:** Sections present but one or more is empty or unnamed.  
**FAIL:** Gap analysis absent or fewer than three sections.

---

### C-05 — Metadata fields complete on card
Each ticket card includes Phase, Category, Severity, and Volume as discrete named fields. Values are drawn from the controlled vocabulary declared in C-02. No required metadata field may be absent or substituted with free-form text.

**PASS:** All four metadata fields present on every card with controlled-vocabulary values.  
**PARTIAL:** One or more fields missing on some cards, or values outside the declared controlled vocabulary on some cards.  
**FAIL:** Metadata fields systematically absent; no named Phase, Category, Severity, or Volume fields on cards.

---

## Recommended Criteria (10 pts each, max 30)

### C-06 — Ticket count 6–12
The output contains between 6 and 12 tickets. A CONSTRAINT MANIFEST or equivalent pre-generation block declares the count range. A VERIFICATION MANIFEST or equivalent post-generation check confirms actual count against the declared range.

**PASS:** Count in range; pre-generation declaration and post-generation verification both present.  
**PARTIAL:** Count in range but declaration or verification absent; or one of the two is present without the other.  
**FAIL:** Count outside 6–12 range.

---

### C-07 — Cross-persona coverage ≥ 3
At least three distinct named personas (roles or user types) appear across the ticket set. A planning step mandates cross-role and cross-phase matrix coverage. Coverage is verified post-generation.

**PASS:** ≥3 distinct named personas present; coverage mandate stated in planning step; verification confirms coverage.  
**PARTIAL:** ≥3 personas present but coverage mandate absent; or mandate present but fewer than 3 personas achieved.  
**FAIL:** Fewer than 3 distinct named personas in ticket set.

---

### C-08 — Gap actionability
Each entry in the gap analysis identifies a named artifact or process change as the required action. Gaps are not stated as abstract problems — each has a concrete next step tied to a specific deliverable or owner.

**PASS:** Every gap entry names a specific artifact or process change as the action.  
**PARTIAL:** Some gap entries are actionable with named artifacts; others remain abstract problems without a concrete next step.  
**FAIL:** Gap analysis present but no entries identify concrete artifacts or process changes.

---

## Aspirational Criteria (5 pts each, max 150)

### C-09 — Ticket clustering and themes
Tickets are grouped into named themes declared before generation. A theme declaration step precedes ticket generation. A cross-ticket patterns table appears in the output summarizing theme-level observations.

**PASS:** Named themes declared pre-generation; cross-ticket patterns table present with theme-level observations.  
**PARTIAL:** Themes implied or labeled post-hoc; or patterns table absent; or only one of the two elements present.  
**FAIL:** No clustering or theme structure; tickets listed without grouping.

---

### C-10 — Ticket lifecycle and resolution
A resolution paths table is present with at minimum triage owner, root cause, and resolution type for each ticket or theme cluster. The table is distinct from the ticket cards.

**PASS:** Resolution paths table present; triage owner, root cause, and resolution type columns populated for all tickets or clusters.  
**PARTIAL:** Table present but one or more required columns missing or sparsely populated.  
**FAIL:** No resolution paths table; lifecycle information absent from output.

---

### C-11 — Phase as card field
Phase appears as a discrete named field in the card body metadata (e.g., `Phase: Phase N (day X–Y)`). A Phase Map Table is present that maps phases to severity and volume norms. Phase in a heading only does not satisfy this criterion.

**PASS:** Phase field present in all card bodies; Phase Map Table present mapping phases to norms.  
**PARTIAL:** Phase field present in card bodies but Phase Map Table absent; or Phase present only in headings.  
**FAIL:** Phase absent from card body fields.

---

### C-12 — Role-phase compound coverage
Roles with ≥3 tickets are required to span ≥2 phases. This compound coverage constraint is stated explicitly in a planning step and confirmed post-generation.

**PASS:** Constraint stated in planning step; all roles with ≥3 tickets span ≥2 phases; post-generation confirmation present.  
**PARTIAL:** Constraint stated but one or more high-count roles fail to span ≥2 phases; or coverage achieved but constraint not stated.  
**FAIL:** Constraint absent and role-phase compound coverage not achieved.

---

### C-13 — Phase-calibrated severity
Severity norms vary by phase. A Phase Map Table or equivalent declares phase-specific severity expectations (e.g., Phase 1 maps to P2/P3; Phase 3 maps to P0/P1). Ticket severity values match their phase norms.

**PASS:** Phase Map Table with severity norms present; all ticket severity values match declared phase norms.  
**PARTIAL:** Phase severity norms declared but not consistently applied across tickets.  
**FAIL:** No phase-calibrated severity norms; severity assigned uniformly or arbitrarily across phases.

---

### C-14 — Phase-anchored body voice
Committed phrases from the vocabulary manifest are indexed by Phase. A planning step (e.g., STEP 3B) assigns per-ticket committed phrases drawn from phase-specific registers. VERIFICATION MANIFEST rows confirm phrase placement.

**PASS:** Per-ticket committed phrases indexed by phase in planning table; verification rows confirm placement.  
**PARTIAL:** Phrases indexed by phase but verification absent; or verification present but phase-indexing absent from planning.  
**FAIL:** No phase-anchored voice indexing; phrases assigned without phase register linkage.

---

### C-15 — Pre-generation constraint declaration
A CONSTRAINT MANIFEST (or equivalent named block) appears before ticket generation and declares all governing constraints explicitly. A VERIFICATION MANIFEST (or equivalent post-generation block) performs numeric checks against those constraints.

**PASS:** CONSTRAINT MANIFEST (pre-generation) and VERIFICATION MANIFEST (post-generation) both present as named, distinct blocks.  
**PARTIAL:** Constraints declared but not in a named pre-generation block; or post-generation verification absent.  
**FAIL:** No pre-generation constraint declaration; constraints absent or embedded only in generation steps.

---

### C-16 — Per-ticket vocabulary pre-commitment
A pre-generation planning table commits a VM Row ID, phase, and specific phrase for every ticket before generation. Each ticket body is written to match its pre-committed phrase. Post-generation verification confirms match.

**PASS:** Planning table with T-ID, VM Row ID, phase, and committed phrase for every ticket; ticket bodies match commitments; verification confirms.  
**PARTIAL:** Planning table present but incomplete (some tickets missing); or bodies do not consistently match committed phrases.  
**FAIL:** No per-ticket vocabulary pre-commitment table.

---

### C-17 — Role-phase vocabulary matrix
A VOCABULARY MANIFEST covers all role × phase cells with distinct register descriptions. Generic descriptions do not satisfy this criterion — each cell must carry a register characterization specific to that role-phase combination.

**PASS:** VOCABULARY MANIFEST present; all role × phase cells populated with distinct, non-generic register descriptions.  
**PARTIAL:** Matrix present but some cells empty, generic, or duplicated across roles or phases.  
**FAIL:** No vocabulary matrix covering role-phase combinations.

---

### C-18 — Vocabulary planning artifact linkage
A three-node traceability chain is present for every ticket: VM Row ID → planning table row → `##` headline annotation (e.g., `*(VM: VM-xxx-P#)*`). Each node references or implies the adjacent node.

**PASS:** Three-node chain traceable for every ticket; each node references the adjacent node.  
**PARTIAL:** Chain partially traceable; one or more nodes absent or unlinked for some tickets.  
**FAIL:** No multi-node vocabulary traceability chain; VM Row IDs not connected across planning and output.

---

### C-19 — Multi-criteria vocabulary pre-flight gate
A standalone VOCABULARY PRE-FLIGHT GATE block appears before ticket generation. It contains ≥5 labeled check items (a)–(e), each with an individual PASS/FAIL verdict. The gate is not embedded within a generation step.

**PASS:** Gate block present and standalone (pre-generation); ≥5 labeled items each with individual verdict.  
**PARTIAL:** Gate block present but embedded in a generation step; or fewer than 5 labeled items; or items lack individual verdicts.  
**FAIL:** No pre-flight gate block.

---

### C-20 — Headline-level vocabulary ID annotation
Every ticket `##` headline carries an inline VM Row ID annotation (e.g., `*(VM: VM-xxx-P#)*`) on the same `##` line. Placement on a subline (body text beneath the headline) fails this criterion regardless of other compliance.

**PASS:** All `##` headlines include inline VM Row ID annotation; no VM Row IDs appear on sublines.  
**PARTIAL:** Some headlines lack VM Row ID annotation; or some VM Row IDs appear on sublines.  
**FAIL:** VM Row IDs systematically absent from headlines; or systematic subline placement.

---

### C-21 — Complete five-item pre-flight coverage
The VOCABULARY PRE-FLIGHT GATE covers all five required check items: (a) vocabulary declaration, (b) VM Row ID assignment, (c) phase-calibrated values, (d) headline annotation format, and (e) inter-role register differentiation. All five must be labeled and individually verdicted.

**PASS:** All five items (a)–(e) present, each labeled, each with an individual verdict.  
**PARTIAL:** Four or fewer items present; or items present but unlabeled or without individual verdicts.  
**FAIL:** Gate absent or fewer than three of the five required items present.

---

### C-22 — Front-loaded compliance contract
A COMPLIANCE CONTRACT named block appears before all generation steps. It contains the C-20 headline placement clause, the C-21 five-item gate mandate, and both a compliant and a failing sample headline illustrating the distinction.

**PASS:** COMPLIANCE CONTRACT block present pre-steps; contains C-20 clause, C-21 mandate, and compliant/failing sample headlines.  
**PARTIAL:** Block present but missing one of the three required elements.  
**FAIL:** No front-loaded COMPLIANCE CONTRACT block; or block appears after generation steps.

---

### C-23 — Multi-site subline prohibition anchoring
The prohibition on subline VM Row ID placement is stated at ≥2 distinct sites in the prompt body (e.g., STEP 3B and STEP 4), in addition to the COMPLIANCE CONTRACT. A VERIFICATION MANIFEST row confirms `##` headline annotation count.

**PASS:** Prohibition stated as direct text at ≥2 body sites distinct from COMPLIANCE CONTRACT; VERIFICATION MANIFEST has a `## headlines with *(VM: …)*` count row.  
**PARTIAL:** Prohibition at only one body site beyond COMPLIANCE CONTRACT; or verification row absent.  
**FAIL:** Subline prohibition absent from prompt body sections; present only in COMPLIANCE CONTRACT or absent entirely.

---

### C-24 — Output-embedded compliance evidence
The VERIFICATION MANIFEST contains a C-20 count row (Required/Actual/Pass?) and five per-item C-21 rows (one per gate item a–e), each with Required, Actual, and Pass? columns.

**PASS:** C-20 count row and five C-21 item rows all present in VERIFICATION MANIFEST, each with Required/Actual/Pass? populated.  
**PARTIAL:** Some rows present; one or more missing; or rows present but lacking the three-column structure.  
**FAIL:** No compliance evidence rows in VERIFICATION MANIFEST.

---

### C-25 — Per-item C-21 gate evidence rows
The VERIFICATION MANIFEST carries five individual rows — one per gate item (a)–(e) — each labeled by item letter, each with Required, Actual, and Pass? columns. These rows are structurally distinct from the aggregate C-20 count row.

**PASS:** Five individual, labeled gate evidence rows present (a)–(e), each with three columns, distinct from the C-20 row.  
**PARTIAL:** Fewer than five rows; or rows present but not labeled by item letter; or not structurally distinct from C-20 row.  
**FAIL:** No per-item gate evidence rows in VERIFICATION MANIFEST.

---

### C-26 — Contract enforcement site registry
A RESTATING POSITIONS section lists ≥3 named enforcement sites with a precedence declaration. Each entry names the governed site and states the governing rule. The section is distinct from COMPLIANCE CONTRACT.

**PASS:** RESTATING POSITIONS section present; ≥3 named enforcement sites with precedence declaration; section is structurally distinct.  
**PARTIAL:** Section present but fewer than 3 named sites; or sites named but no precedence declaration.  
**FAIL:** No RESTATING POSITIONS section.

---

### C-27 — Consequence-form criterion-citing prohibition
The COMPLIANCE CONTRACT C-20 clause includes a deterministic consequence-form (CF) qualifier that names the criterion by ID: "fails C-20 regardless of other compliance." The qualifier must name C-20 and use deterministic language — hedged language ("may fail") does not satisfy this criterion.

**PASS:** CF qualifier present in C-20 clause; names C-20 by ID; uses "regardless of other compliance" or equivalent deterministic form.  
**PARTIAL:** CF qualifier present but does not name C-20 by ID; or uses hedged or conditional language.  
**FAIL:** No CF qualifier on C-20 clause; consequence of violation not stated in COMPLIANCE CONTRACT.

---

### C-28 — Registry-manifest structural coherence
The RESTATING POSITIONS entry for the VM references the five-row gate structure in the VERIFICATION MANIFEST. The description in RESTATING POSITIONS matches the actual structure present in the manifest.

**PASS:** RESTATING POSITIONS VM entry explicitly references the five individual rows for gate items (a)–(e); VERIFICATION MANIFEST contains a matching five-row structure.  
**PARTIAL:** RESTATING POSITIONS references the VM but description does not match the actual structure; or reference is present but structural detail absent.  
**FAIL:** No cross-reference between RESTATING POSITIONS and VERIFICATION MANIFEST structure.

---

### C-29 — Consequence-form enforcement-site propagation
The CF clause "fails C-20 regardless of other compliance" (or a structural equivalent) appears as direct literal text in ≥2 prompt body sections — not only in COMPLIANCE CONTRACT or RESTATING POSITIONS. Delegation by reference to another section does not satisfy this criterion.

**PASS:** CF clause as direct literal text in ≥2 body sections (e.g., STEP 3B and STEP 4) distinct from COMPLIANCE CONTRACT and RESTATING POSITIONS.  
**PARTIAL:** CF clause as direct text in only one body section; or present only via delegation/reference.  
**FAIL:** CF clause absent from prompt body sections; present only in COMPLIANCE CONTRACT or RESTATING POSITIONS.

---

### C-30 — Spine-row self-enforcement imperative
STEP 6 carries direct-text CF in both a governing preamble and within the body template instruction. Both layers state the consequence of subline placement as direct text citing C-20 with deterministic language — neither layer may delegate to another section.

**PASS:** STEP 6 contains CF in governing preamble and in body template instruction, each as direct text citing C-20 with "regardless of other compliance" or equivalent.  
**PARTIAL:** CF present in one layer only (preamble or body template, not both); or one layer delegates to another section rather than stating CF directly.  
**FAIL:** STEP 6 carries no direct-text CF; enforcement relies entirely on sections outside STEP 6.

---

### C-31 — Dual-load CONTRACT implementation
The COMPLIANCE CONTRACT is implemented at two load points: once as a front-loaded named block before all steps, and once re-invoked or directly cited within the spine step (STEP 6) at the point of generation. A single instance at one load point does not satisfy this criterion.

**PASS:** CONTRACT present as standalone pre-step block AND re-invoked or directly cited within STEP 6.  
**PARTIAL:** CONTRACT present as standalone block only; STEP 6 does not reference or re-invoke it; or STEP 6 references it but no standalone block precedes the steps.  
**FAIL:** CONTRACT not implemented at two distinct load points.

---

### C-32 — Three-timing enforcement coverage
CF clauses are present at all three enforcement timing points: (1) CONSTRAINT MANIFEST load (pre-generation), (2) COMPLIANCE CONTRACT (front-loaded governance), and (3) VERIFICATION MANIFEST (post-generation check). Each timing point carries at least one CF clause independently.

**PASS:** CF clause present and independently stated at all three timing points.  
**PARTIAL:** CF present at two of three timing points; one timing point absent or CF absent at that point.  
**FAIL:** CF present at one or zero timing points.

---

### C-33 — VM Row ID CF at constraint load
The CONSTRAINT MANIFEST load site carries a VM Row ID–specific CF clause binding VM Row ID count or placement to the headline constraint and stating the consequence of violation in deterministic form. Presence of a VM Row ID count row without a CF clause does not satisfy this criterion.

**PASS:** CONSTRAINT MANIFEST contains a VM Row ID CF clause with deterministic consequence language (e.g., "fails C-20 regardless of other compliance").  
**PARTIAL:** CONSTRAINT MANIFEST references VM Row IDs or includes a count row but the CF clause is absent or uses hedged language.  
**FAIL:** CONSTRAINT MANIFEST load site has no VM Row ID CF anchoring.

---

### C-34 — VM Row ID CF in compliance contract
The COMPLIANCE CONTRACT contains a VM Row ID–specific CF clause naming VM Row ID headline placement as a governed site and stating the consequence of violation in deterministic, criterion-citing form.

**PASS:** COMPLIANCE CONTRACT contains VM Row ID CF clause naming C-20 and using deterministic form (e.g., "fails C-20 regardless of other compliance").  
**PARTIAL:** COMPLIANCE CONTRACT references VM Row IDs but CF clause absent; or language is hedged or does not name C-20.  
**FAIL:** COMPLIANCE CONTRACT has no VM Row ID CF anchoring.

---

### C-35 — VM Row ID CF in verification spine
The VERIFICATION MANIFEST contains VM Row ID CF anchoring at row level — each VM Row ID verification row carries consequence language binding the check to headline placement. Header-level CF at the manifest preamble without per-row CF does not fully satisfy this criterion.

**PASS:** VERIFICATION MANIFEST contains VM Row ID CF at individual check row level; consequence language present per row, not only at manifest header.  
**PARTIAL:** CF present at manifest header level only; individual check rows lack their own consequence language.  
**FAIL:** VERIFICATION MANIFEST has no VM Row ID CF anchoring at any level.

---

### C-36 — Phase-indexed CF in CONSTRAINT MANIFEST
The CONSTRAINT MANIFEST contains phase-specific VM Row ID CF rows — one row per phase — each carrying an inline CF clause that binds the per-phase VM Row ID count to headline placement. A single aggregate count row (even with a CF clause) does not satisfy this criterion; per-phase rows are required because they expose distribution errors that an aggregate total masks.

**PASS:** CONSTRAINT MANIFEST contains ≥3 phase-specific VM Row ID rows (one per phase), each with an inline CF clause binding per-phase count to headline placement.  
**PARTIAL:** CONSTRAINT MANIFEST contains a VM Row ID CF clause but only at aggregate level (single row covering all phases); no per-phase breakdown present.  
**FAIL:** CONSTRAINT MANIFEST contains no phase-indexed VM Row ID CF rows; per-phase enforcement absent.

---

### C-37 — VERIFICATION MANIFEST per-row CF column
Each VM Row ID check row in the VERIFICATION MANIFEST carries a dedicated Consequence-if-FAIL column that is structurally distinct from any header-level CF. The column fires the consequence clause at each individual check operation rather than only at manifest entry. Presence of header-level CF without a per-row column does not satisfy this criterion.

**PASS:** Every VM Row ID check row has a dedicated Consequence-if-FAIL column with deterministic consequence language; column is distinct from manifest-level CF.  
**PARTIAL:** Consequence-if-FAIL column present on some check rows but not all; or CF present only at manifest header level with no per-row column.  
**FAIL:** No per-row Consequence-if-FAIL column in VERIFICATION MANIFEST; CF present only at manifest entry level or absent entirely.

---

### C-38 — RESTATING POSITIONS names CONSTRAINT MANIFEST
The RESTATING POSITIONS section names the CONSTRAINT MANIFEST as a CF enforcement site. This entry creates a bidirectional link between the CONSTRAINT MANIFEST CF preamble (or phase-indexed rows) and the COMPLIANCE CONTRACT enforcement registry, making all CF sites in the prompt discoverable via RESTATING POSITIONS without reading each section individually.

**PASS:** RESTATING POSITIONS contains an entry naming CONSTRAINT MANIFEST as a CF site; entry references the CF preamble or phase-indexed rows, establishing a bidirectional link.  
**PARTIAL:** RESTATING POSITIONS present but does not name CONSTRAINT MANIFEST as a CF site; or a reference is present but does not establish the bidirectional link (e.g., names the section without describing its CF role).  
**FAIL:** RESTATING POSITIONS does not reference CONSTRAINT MANIFEST; no bidirectional link between CONSTRAINT MANIFEST and the enforcement registry.
```
