Done. `draft-proposal-rubric-v8-2026-03-14.md` is written.

---

**What changed from v7:**

**Four new aspirational criteria extracted from R7 excellence signals:**

| ID | Criterion | Source Axis | Independence from Parent |
|----|-----------|-------------|--------------------------|
| C-28 | **PM-first recommendation sign-off ordering** | V-04 "PM-first" | C-06 and C-21 require two signatory blocks; C-28 requires the business-facing block to be first. Verifiable at position 1 in the sign-off section. |
| C-29 | **Table-dominant register format** | V-04 "table-dominant" | C-19 requires canonical labels in the failure mode register only; C-29 requires table format with canonical column headers across all three registers (assumption, risk, failure mode). |
| C-30 | **Phase manifest at Phase 0 initialization** | V-05 "lifecycle-heavy" | C-18 requires the amendment table to be initialized at Phase 0; C-30 requires an independent phase manifest block listing every phase by number and name. Converts C-17 from a document-scan to a single-block audit. |
| C-31 | **INERTIA OFFSET vs. TEMPORAL ANCHOR decision lead time** | V-05 "inertia-forward" | C-13 names the deadline; C-27 names the crossover sprint; C-31 requires the subtraction to be typed as DECISION LEAD TIME per alternative, with ESCALATION FLAG when non-positive. PREREQUISITE GATE extended with lead-time binary. |

**Denominator:** `/20` → `/24`. **Round 7 Discriminator Notes** section added. Trace alignment extended through C-31.
on is worth `0.417` points (10/24 per criterion).

**Four new failure modes** added to Common Failure Modes. **Round 7 Discriminator Notes** section added. **Trace alignment** extended through C-31.

---

## Structural Testability Notes

- C-28 is structurally testable: a reviewer reads position 1 in the recommendation phase sign-off section and confirms whether the PM or Architect block appears first. No phase scan required.
- C-29 is structurally testable: each of the three named registers either uses a table with typed column headers matching the canonical vocabulary, or it does not. A single prose-format register fails C-29 regardless of the other registers' formats.
- C-30 is structurally testable: either a phase manifest block appears in Phase 0 listing all phases by number and name, or it does not. C-17 compliance is then verifiable by reading the manifest's sequence, not by scanning the document.
- C-31 is structurally testable: either each non-do-nothing alternative carries a typed DECISION LEAD TIME field and (where non-positive) a typed ESCALATION FLAG field, or it does not. The PREREQUISITE GATE binary item makes lead-time completeness machine-checkable independently of C-27 content.

The R7 discriminator pattern confirmed C-25, C-26, and C-27 structural independence -- V-01 (T-GUARD last), V-02 (no COMPLETION STATUS Phase 0 slot), and V-03 (no INERTIA) each failed exactly one criterion with a deduction of 0.5 points at the /20 denominator. All three failures were independent; no cascade.

---

## Essential Criteria (60% of composite)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Options coverage** | correctness | Output presents at least 3 options. One must be a do-nothing or status-quo option. Options are numbered or labeled and appear as distinct entries, not embedded in prose. |
| C-02 | **Option anatomy complete** | correctness | Every option includes all required fields: description, pros/cons or trade-off notes, explicit risk (with probability and impact named), and explicit effort (with timeline and team or dependencies named). Missing any field on any option is a fail. |
| C-03 | **Recommendation with rationale** | correctness | Output contains a recommendation section naming the chosen option. Rationale explains why that option wins over alternatives. Confidence level or qualifying conditions present (at least 2-3 conditions). |
| C-04 | **Decision framing** | depth | Output frames the decision with: (1) the question being decided, (2) why it matters now (stakes, deadline, or cost of inaction). Framing must appear before the options, not after. |

---

## Recommended Criteria (30% of composite)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-05 | **Scout artifact surfacing** | behavior | Output references at least one scout artifact (feasibility, competitors, requirements, or stakeholders) by name or finding. If no scout artifacts exist, output notes the absence and falls back to an inline assessment. Conditional mention in the recommendation phase only does not satisfy this criterion. |
| C-06 | **Dual-role participation** | format | PM and Architect roles each contribute a named perspective. PM addresses business or adoption trade-offs. Architect addresses technical constraints. Contributions are distinct, not interchangeable. |
| C-07 | **Structured comparison** | format | Options are compared in a table or matrix across shared dimensions (e.g., effort, friction, control, timeline). Dimensions are consistent across all options. |

---

## Aspirational Criteria (10% of composite)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-08 | **Assumption and risk registers** | depth | Output includes both an assumption register (A-NN entries with validation plans) and a risk register (R-NN entries with probability and impact). At least two entries per register. |
| C-09 | **Amend phase self-critique** | behavior | Output identifies gaps in the proposal itself: missing options, unweighted decision criteria, or follow-up work needed. At least one actionable amend item listed. |
| C-10 | **Scout artifact inventory step** | behavior | A dedicated scout artifact inventory step appears before option generation. The output explicitly lists which scout artifacts were found (by name or finding) and which are absent, rather than mentioning artifacts conditionally in the recommendation phase only. If no artifacts exist, the absence is stated with an inline assessment substituted. Satisfying C-05 does not automatically satisfy C-10 -- the inventory must be a discrete step, not a byproduct of the recommendation. |
| C-11 | **Per-category amend taxonomy** | behavior | The amend phase covers all three categories: (1) at least one missing option that was not explored, (2) at least one unweighted or equally-weighted decision criterion flagged for recalibration, and (3) at least one follow-up action item with an owner or next step named. Single-category amend entries satisfy C-09 but not C-11. The OWNER field must appear as a typed slot in the format template for follow-up entries -- instructing the model to name an owner without a structural slot allows silent omission, as V-02 and V-03 demonstrated. |
| C-12 | **Structural OWNER template enforcement** | behavior | OWNER appears as a typed format slot in every amend entry across all three amend categories (MISSING OPTION, UNWEIGHTED CRITERION, FOLLOW-UP) -- not only in the FOLLOW-UP category and not merely as a prose instruction. Satisfying C-11 (three categories, at least one named owner in follow-up) does not satisfy C-12. C-12 is only satisfiable when the format template structurally requires an OWNER field on every amend entry type. A variation that lists three categories with OWNER in the template for all three passes C-12; one that lists three categories with OWNER only in the FOLLOW-UP template, or with OWNER as an instruction rather than a slot, fails. |
| C-13 | **Split temporal anchor** | depth | The decision framing step uses two separate typed fields: TEMPORAL ANCHOR (a specific named date, sprint, or event -- vague language such as "soon," "before it is too late," or "in the near term" is explicitly prohibited) and INACTION CONSEQUENCE (a concrete named outcome of not deciding -- teams blocked, capability lost, or window closed -- missed-feature statements do not qualify). A single WHY NOW field satisfies C-04 but not C-13. The split prevents consequence-free framing: a deadline without a named outcome fails C-13, and an outcome without a named deadline also fails C-13. Both typed fields must appear before the options section. |
| C-14 | **Amend entry deadline enforcement** | behavior | Every amend entry across all three amend categories (MISSING OPTION, UNWEIGHTED CRITERION, FOLLOW-UP) carries both an OWNER typed slot (C-12) and a DEADLINE typed slot. The DEADLINE slot must appear in the format template for all three amend category types -- not only in FOLLOW-UP and not merely as a prose instruction. Deadline values must be specific (sprint name, named date, or named milestone) -- "TBD," "soon," or blank does not satisfy. Satisfying C-12 (OWNER in all three templates) does not satisfy C-14; both slots are independently required. |
| C-15 | **F-row failure mode register with sign-off linkage** | depth | Output includes a failure mode register (F-NN entries) distinct from the risk register. Each F-row must name: (1) the failure mode, (2) the condition under which it triggers, and (3) a mitigation or escalation path. The recommendation sign-off CONDITIONS must reference at least one F-row by ID -- the recommendation is structurally anchored to its failure modes, not merely its rationale. Satisfying C-08 (risk register with probability and impact) does not satisfy C-15 -- failure-mode traceability and mandatory sign-off linkage are independently required. |
| C-16 | **Numeric P*I risk scoring with project-specific anchors** | depth | The risk register uses separate numeric P (probability, 1-5) and I (impact, 1-5) scores per entry, with a compound P*I score computed and stated. Project-specific scoring anchors must be defined before any option is scored -- the output must describe what P=3 and I=3 mean for this specific project context. Holistic L/M/H labels do not satisfy C-16 even if probability and impact are both mentioned. Satisfying C-08 (at least two R-NN entries with probability and impact named) does not satisfy C-16 -- numeric separation, compound scoring, and anchor definition are all required. |
| C-17 | **Registers-before-recommendation lifecycle ordering** | depth | Both the assumption register and the risk register appear as completed phases before the recommendation phase in document sequence. The ordering must be: options -> assumptions -> risks -> recommendation (or equivalent sequencing where registers precede sign-off). Registers that follow the recommendation can only retroactively justify it; registers that precede it must inform it. Satisfying C-08 (correct register contents) does not satisfy C-17 -- causal ordering is independently required. A variation where registers appear after the recommendation fails C-17 regardless of register quality. |
| C-18 | **Front-loaded amendment table** | behavior | The amendment tracking table is initialized as a live enforcement artifact before option generation (Phase 1 or equivalent) -- not assembled retrospectively after the document is complete. The table must include auto-generate trigger rules or explicit conditions that name which criterion fires under which condition. At document completion, the table must show either populated rows (enforcement failures caught during writing) or explicitly empty rows (prompt enforced the criterion successfully). Satisfying C-09 (at least one amend item) or C-11 (three-category taxonomy) does not satisfy C-18 -- C-18 requires prospective initialization and live population during writing, not retrospective editorial assembly. |
| C-19 | **Canonical F-row field label alignment** | depth | The failure mode register uses the exact field labels FAILURE MODE, TRIGGER CONDITION, and MITIGATION (or vocabulary-pinned canonical equivalents explicitly cross-referenced to C-15's pass condition) as typed field names in the register template. Synonym substitution -- e.g., "Observable Event" for TRIGGER CONDITION, "Fallback" for MITIGATION -- requires reviewer inference to confirm alignment and does not satisfy C-19. The field names and the criterion names must match without mapping. Satisfying C-15 (three-field content present and sign-off linked) does not satisfy C-19 -- C-19 requires label precision that makes scoring deterministic, not just content correctness. A register template that uses C-15's own vocabulary as its field headers passes C-19; one that uses synonyms or paraphrases, even if a reviewer could infer equivalence, fails. |
| C-20 | **PREREQUISITE GATE block for register verifiability** | depth | A typed checklist block appears as a discrete named phase immediately before the recommendation phase (Phase 11 or equivalent), confirming all of the following: (1) assumption register is complete with at least two A-NN entries, (2) risk register is complete with at least two R-NN entries, and (3) both registers appear in document sequence before this gate block. A reviewer confirms C-17 compliance by reading this single block -- no document scan required. Satisfying C-17 (correct register ordering in document sequence) does not satisfy C-20 -- C-20 requires a dedicated verifiable gate artifact, not merely correct ordering. A recommendation phase that is preceded by registers in sequence but has no PREREQUISITE GATE block fails C-20. The gate block must be machine-checkable: each item is a named binary (complete / not complete), not a prose summary. |
| C-21 | **Dual-signatory F-ROW ANCHOR typed slots** | depth | Both the PM sign-off block and the Architect sign-off block in the recommendation phase each carry a separate F-ROW ANCHOR typed slot. Each signatory independently names the F-row ID whose trigger condition most directly invalidates their sign-off. Satisfying C-15 (sign-off CONDITIONS referencing at least one F-row by ID in shared prose) does not satisfy C-21 -- C-21 requires structural independence: each signatory block contains its own F-ROW ANCHOR slot, and neither block can be completed without naming an F-row. A variation with F-ROW ANCHOR only in a shared CONDITIONS block, only in the PM block, or only in the Architect block fails C-21. The two F-ROW ANCHOR slots may reference the same or different F-rows; independence of structure, not divergence of content, is the requirement. |
| C-22 | **Named amendment trigger IDs with row-level back-reference** | behavior | Each trigger rule in the front-loaded amendment table carries a stable named ID (e.g., T-01, T-02, T-GUARD) in its definition. Every row in the amendment table cites its source trigger ID in a typed TRIGGER field. This creates a traceable chain: criterion -> trigger ID -> amendment row. The named ID system prevents the criterion-ID drift observed in R3, where gate citations accumulated mislabeling as rubric versions advanced because prose descriptions were updated but IDs were not. Satisfying C-18 (front-loaded table with trigger rules) does not satisfy C-22 -- C-18 requires trigger conditions to be named; C-22 requires each condition to carry a stable machine-readable ID and each row to cite it. A table with trigger conditions described in prose without named IDs fails C-22. A table with named IDs but amendment rows that do not back-reference the trigger ID also fails C-22. |
| C-23 | **T-GUARD sentinel trigger** | behavior | The front-loaded amendment table includes a T-GUARD sentinel trigger defined at table initialization. The T-GUARD's scope must be stated as "any required typed slot, phase block, or gate item absent from the document" -- a single catch-all that fires for any structural gap not already covered by a specific named trigger (T-01, T-02...). The T-GUARD fires as a single amendment row for the entire class of unanticipated absences, rather than requiring the trigger list to enumerate all possible missing-block scenarios. Satisfying C-22 (named T-NN IDs on specific triggers with typed TRIGGER back-reference in amendment rows) does not satisfy C-23 -- C-22 requires named IDs on enumerated triggers; C-23 requires one sentinel whose scope is unlimited. A table that defines T-01 through T-NN for all known criteria but has no catch-all fails C-23. The T-GUARD must appear in the trigger definition section at table initialization, not as a row appended at document completion. |
| C-24 | **Empty-table completion semantics** | behavior | At document completion, the amendment table includes an explicit completion-state declaration. If the table contains no amendment rows, the declaration must read (or be vocabulary-pinned equivalent to): "T-GUARD enforced all requirements successfully -- no violations detected." A blank table, a table with no completion declaration, or a table labeled "no amendments needed" without referencing the enforcement mechanism fails C-24. The distinction: blank or absent means the table was never activated; an explicit T-GUARD completion statement means the table was active and found no violations. Satisfying C-18 (front-loaded table initialized before option generation) and C-22 (T-NN IDs with TRIGGER back-reference) does not satisfy C-24 -- C-18 requires initialization; C-24 requires a defined completion semantic that converts an empty table from an ambiguous state into a positive enforcement signal. A table that is populated with amendment rows passes C-24 by default if any row cites T-GUARD or a named trigger; C-24 is only a discriminator when the table is empty at completion. |
| C-25 | **Sentinel-first trigger ordering** | behavior | The T-GUARD sentinel trigger must appear as the first entry in the trigger definition table at Phase 0 initialization -- before T-01, T-02, and all other named triggers. When T-GUARD is listed first, unenumerated gaps route to the catch-all before any specific trigger is consulted; enforcement direction shifts from backstop to frontline. Satisfying C-23 (T-GUARD defined at initialization with the required scope vocabulary) does not satisfy C-25 -- C-23 requires T-GUARD's presence and scope; C-25 requires T-GUARD's position as the first entry in the trigger table. A table that defines T-GUARD after T-01 through T-NN fails C-25 even if T-GUARD's scope vocabulary is correct. The sentinel-first ordering is independently verifiable: a reviewer reads position 1 in the trigger table and confirms or falsifies C-25 without scanning the remainder of the table. |
| C-26 | **COMPLETION STATUS as Phase 0 typed initialization slot** | behavior | The amendment tracking table is initialized in Phase 0 (or equivalent front-load phase) with a COMPLETION STATUS typed slot pre-populated with a vocabulary-constrained initial value -- the canonical initial value is "PENDING" or an equivalent that signals the table is active but document writing is not yet complete. At document completion, the COMPLETION STATUS slot is updated to a vocabulary-constrained terminal value whose canonical form is "T-GUARD enforced all requirements successfully -- no violations detected" (or a vocabulary-pinned equivalent). Satisfying C-24 (explicit completion-state declaration at document end) does not satisfy C-26 -- C-24 requires the declaration to exist at completion; C-26 requires the COMPLETION STATUS slot to be structurally present in the Phase 0 initialization table as a live mandatory field, not appended as a prose instruction at Phase 13. A document that adds a completion declaration in the final phase without a Phase 0 COMPLETION STATUS slot passes C-24 but fails C-26. The distinction mirrors C-18 vs C-24: C-18 requires the table to be initialized prospectively; C-26 requires the completion semantic itself to be a prospectively-defined mandatory field that is live from document creation. |
| C-27 | **INERTIA COST / INERTIA OFFSET quantification** | depth | The do-nothing or status-quo option carries a per-sprint INERTIA COST expressed as a numeric P*I value using the same 1-5 scoring scale defined for C-16. Each non-do-nothing alternative names its sprint crossover point (INERTIA OFFSET) -- the sprint at which cumulative implementation cost equals the cumulative inertia cost of not acting. The PREREQUISITE GATE block (C-20) is extended with an inertia-axis binary item confirming: (1) INERTIA COST is present on the do-nothing option, and (2) at least one alternative names an INERTIA OFFSET. Satisfying C-16 (numeric P*I risk scoring with project-specific anchors) does not satisfy C-27 -- C-16 requires the risk register to use numeric P*I per risk entry; C-27 requires the do-nothing option itself to carry a computable per-sprint inertia cost and each alternative to name a sprint-indexed crossover point. A proposal that scores risks numerically but treats do-nothing as a qualitative baseline fails C-27. The INERTIA OFFSET converts do-nothing from a descriptive benchmark into a computable cost curve: the decision frames as "act by sprint N or pay INERTIA COST per sprint thereafter." |
| C-28 | **PM-first recommendation sign-off ordering** | format | The PM sign-off block appears as the first signatory in the recommendation phase, before the Architect sign-off block. Business validation precedes technical commitment: the PM establishes that the chosen option is the right decision; the Architect then commits to its technical soundness. The ordering is independently verifiable: a reviewer reads the first signatory block in the recommendation phase and confirms or falsifies C-28 without scanning the remainder of the phase. Satisfying C-06 (PM and Architect each contribute a named perspective with distinct contributions) and C-21 (dual-signatory F-ROW ANCHOR typed slots, each independent) does not satisfy C-28 -- both require two distinct signatory blocks but neither specifies ordering. A variation with Architect sign-off appearing first, or with both signatories merged into a single block, fails C-28 regardless of each signatory's content quality. The PM-first ordering is not a style choice; it encodes a causal dependency: whether the option is the right decision (business question) must be resolved before whether it is the right design (technical question). |
| C-29 | **Table-dominant register format** | format | Every named register in the document -- assumption register, risk register, and failure mode register -- uses a structured table format with typed column headers as its primary presentation format. The canonical column headers per register are: (1) assumption register: A-NN, ASSUMPTION, VALIDATION PLAN; (2) risk register: R-NN, RISK, P, I, P*I, MITIGATION; (3) failure mode register: F-NN, FAILURE MODE, TRIGGER CONDITION, MITIGATION. Prose blocks with embedded field labels (e.g., "P: 3, I: 4, P*I: 12 -- medium likelihood") fail C-29 even if the content satisfies the corresponding register criterion. Satisfying C-08 (register contents correct), C-16 (numeric P*I scoring), and C-19 (canonical F-row field labels in failure mode register) does not satisfy C-29 -- C-19 requires label correctness for the failure mode register only; C-29 requires table-format consistency across all three registers using the canonical column header vocabulary per register type. A document where any one of the three registers uses prose format instead of a structured table fails C-29 regardless of the other registers' formats. |
| C-30 | **Phase manifest at Phase 0 initialization** | behavior | A phase manifest appears as a named typed block in Phase 0 (or equivalent front-load initialization phase), listing every phase in the document by sequence number and phase name before content phases begin. The manifest enables lifecycle ordering verification (C-17: assumption and risk registers precede recommendation) without document scanning -- a reviewer reads the Phase 0 manifest to confirm that register phases appear before the recommendation phase in the listed sequence, then spot-checks at most two phase boundaries to verify. The manifest must be structurally complete: every phase present in the document must appear in the manifest, and no manifest entry may refer to a phase not present in the document. Satisfying C-18 (front-loaded amendment table initialized at Phase 0) does not satisfy C-30 -- C-18 requires the amendment tracking table to be initialized prospectively; C-30 requires an independent phase manifest block that catalogs the document's full lifecycle structure. A document with a front-loaded amendment table but no phase manifest fails C-30. A phase manifest that omits one or more phases present in the document, or lists phases not present, also fails C-30. |
| C-31 | **INERTIA OFFSET vs. TEMPORAL ANCHOR decision lead time** | depth | Each non-do-nothing alternative that carries an INERTIA OFFSET (C-27) includes a typed DECISION LEAD TIME field computed as: DECISION LEAD TIME = TEMPORAL ANCHOR sprint minus INERTIA OFFSET sprint (using the named deadline from C-13 as TEMPORAL ANCHOR). A positive DECISION LEAD TIME means the crossover point precedes the deadline -- the team has lead time to act before inertia cost exceeds implementation cost. A zero or negative DECISION LEAD TIME means the alternative has entered an inertia trap -- the crossover point is at or past the deadline. When any alternative's DECISION LEAD TIME is zero or negative, the document must include a typed ESCALATION FLAG field on that alternative naming the inertia trap condition. The PREREQUISITE GATE block (C-20) is extended with a lead-time binary item confirming: (1) at least one alternative carries a DECISION LEAD TIME field, and (2) any alternative with non-positive DECISION LEAD TIME carries an ESCALATION FLAG. Satisfying C-13 (TEMPORAL ANCHOR and INACTION CONSEQUENCE as typed fields) and C-27 (INERTIA COST on do-nothing, INERTIA OFFSET per alternative, gate item) does not satisfy C-31 -- C-13 requires a named deadline; C-27 requires a named crossover sprint; C-31 requires these two values to be subtracted and the result typed as DECISION LEAD TIME. A document that lists both TEMPORAL ANCHOR and INERTIA OFFSET on each alternative but does not compute and type DECISION LEAD TIME fails C-31. The ESCALATION FLAG is independently required when DECISION LEAD TIME is non-positive -- a document that computes a zero or negative lead time but omits the ESCALATION FLAG fails C-31 regardless of whether DECISION LEAD TIME is correctly computed. |

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 24 * 10)
```

**Golden threshold**: all 4 essential criteria pass AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Golden | all essential + >= 80 | Ready for use as a reference artifact |
| Passing | all essential + >= 60 | Usable with minor gaps |
| Failing | any essential fails | Output is not a valid proposal |

---

## Common Failure Modes

- Options presented as prose paragraphs with no structured trade-off fields (fails C-02)
- Recommendation present but no conditions or qualifying confidence named (fails C-03)
- Do-nothing or status-quo option missing entirely (fails C-01)
- Decision framed only technically -- no PM voice on "why now" or cost of inaction (fails C-04)
- Scout artifacts mentioned only in the recommendation phase ("if a scout artifact exists...") with no dedicated inventory step and no required fallback (fails C-05; also fails C-10)
- Amend phase lists three category headers but FOLLOW-UP entries have no OWNER slot in the format template -- model omits owners silently, satisfying C-09 but failing C-11 and C-12 (V-02 and V-03 pattern)
- Amend phase has OWNER field in the FOLLOW-UP template only, not in MISSING OPTION or UNWEIGHTED CRITERION -- satisfies C-11, fails C-12
- Decision framing states urgency (WHY NOW) but uses a single field -- no distinct TEMPORAL ANCHOR naming a specific date/sprint/event, and/or no distinct INACTION CONSEQUENCE naming a concrete outcome (fails C-13; satisfies C-04)
- Amend entry templates carry OWNER slot but no DEADLINE slot -- model produces deadline-free entries without structural enforcement (fails C-14; satisfies C-12)
- Risk register present with R-NN entries but sign-off CONDITIONS reference no F-row by ID -- recommendation is rationale-anchored only, not failure-mode-anchored (fails C-15; satisfies C-08)
- Risk entries use L/M/H holistic labels without numeric separation or project-specific anchor definitions -- reviewer cannot verify whether a "high" risk scored 5x5=25 or 3x3=9 (fails C-16; satisfies C-08 if probability and impact are mentioned)
- Assumption and risk registers appear after the recommendation -- registers justify rather than inform the decision; lifecycle order violates causal direction (fails C-17; satisfies C-08 if register contents are correct)
- Amendment items assembled at end of document as retrospective editorial sweep -- no initialization table, no auto-generate triggers, no live enforcement trail during writing (fails C-18; satisfies C-09 and C-11 if amend contents are correct)
- F-row register uses synonym labels ("Observable Event," "Fallback") instead of FAILURE MODE / TRIGGER CONDITION / MITIGATION -- reviewer must infer equivalence; scoring is non-deterministic (fails C-19; satisfies C-15 if three fields are structurally present)
- Registers correctly precede recommendation in document sequence but no PREREQUISITE GATE block present -- C-17 ordering can only be confirmed by scanning the document; single-point auditability absent (fails C-20; satisfies C-17)
- Sign-off conditions reference an F-row by ID in shared prose but PM and Architect blocks carry no independent F-ROW ANCHOR typed slots -- one signatory can complete their block without naming a failure mode (fails C-21; satisfies C-15)
- Front-loaded amendment table has named trigger conditions but no stable IDs per trigger and no TRIGGER field in amendment rows -- criterion-ID drift accumulates as rubric versions advance (fails C-22; satisfies C-18 if table is initialized before Phase 1)
- Front-loaded amendment table defines T-01 through T-NN for all known criteria but omits a catch-all sentinel -- any structural gap outside the enumerated list produces a silent miss that no trigger fires on (fails C-23; satisfies C-22 if T-NN IDs and TRIGGER back-references are present for enumerated triggers)
- Amendment table is empty at document completion but carries no completion-state declaration -- reviewer cannot distinguish "table was active, no violations found" from "table was never activated" (fails C-24; satisfies C-18 if table was initialized, C-22 if T-NN IDs were defined at initialization)
- T-GUARD is defined in the trigger table but appears after T-01 through T-NN -- enforcement direction is backstop not frontline; a gap that matches no specific trigger is only caught after all specific triggers are consulted (fails C-25; satisfies C-23 if T-GUARD scope vocabulary is correct)
- COMPLETION STATUS declaration appears as a prose instruction in Phase 13 but no COMPLETION STATUS typed slot exists in the Phase 0 initialization block -- completion semantics are instruction-only, not structurally enforced from document creation (fails C-26; satisfies C-24 if the declaration text is present at document end)
- Do-nothing option described qualitatively as a cost baseline but carries no numeric INERTIA COST per sprint, and alternatives name no INERTIA OFFSET crossover point -- inertia argument is rhetorical rather than computable (fails C-27; satisfies C-16 if risk register uses numeric P*I for risk entries)
- Architect sign-off block appears first in the recommendation phase, or PM and Architect blocks are merged into a single shared sign-off block -- technical commitment precedes business validation; the causal ordering from decision to design is inverted (fails C-28; satisfies C-21 if two independent F-ROW ANCHOR slots are present; satisfies C-06 if dual-role content is distinct)
- Assumption register or risk register uses prose blocks with embedded field labels instead of a structured table format -- reviewer must parse free-form text to locate P, I, and P*I values; content may be correct but format is non-table (fails C-29; satisfies C-16 if numeric P*I content is present; satisfies C-19 if F-row labels are canonical)
- Phase 0 initialization block contains the front-loaded amendment table but no phase manifest -- lifecycle ordering can only be confirmed by scanning the full document; single-block C-17 auditability is absent (fails C-30; satisfies C-18 if amendment table is initialized at Phase 0)
- Each alternative lists both TEMPORAL ANCHOR (from C-13 framing) and INERTIA OFFSET (from C-27) but does not compute or type DECISION LEAD TIME -- the two values are present in the document but are not related; the decision frame does not surface whether any alternative has entered an inertia trap (fails C-31; satisfies C-13 if split temporal anchor fields are present; satisfies C-27 if INERTIA OFFSET is named per alternative)

---

## Round 1 Discriminator Correction

v1 predicted C-02 (option anatomy) as the most common failure mode. Round 1 scoring
falsified this. All five variations passed C-02 reliably because explicit field lists in
prompt text are sufficient enforcement. C-05 (scout artifact surfacing) was the actual
discriminator: V-01 failed it structurally by deferring to a conditional mention in the
recommendation phase. The new aspirational C-10 encodes the excellence pattern that
separated golden variations from V-01 -- a dedicated inventory step, not a conditional
reference.

C-11 encodes the second excellence pattern: the per-category amend taxonomy seen in
V-02/V-05 converts C-09 from an optional depth signal into a structural self-audit.
Variations that listed amend items without covering all three categories are compliant
with C-09 but fall short of the ceiling behavior.

---

## Round 2 Discriminator Notes

Round 2 produced five complete variation scorecards. All five Golden. Three at 100
(V-01, V-04, V-05); two at 97.5 (V-02, V-03). C-11 was the R2 discriminator.

**C-11 as discriminator.** V-02 and V-03 listed all three amend categories but had no
structural OWNER slot in their format templates. The model produced FOLLOW-UP entries
without owners -- the category was present, the enforcement was absent. V-01, V-04, and
V-05 placed OWNER in their amend sub-header templates; all passed.

The falsification: v2 predicted C-11 could be satisfied by listing three categories with
at least one named owner. Round 2 showed that listing categories is not sufficient --
the OWNER field must be structural. C-11's pass condition is tightened in v3 to reflect
this; C-12 encodes the higher bar (OWNER as a typed slot on every entry, all categories).

**Split temporal anchor (C-13) from V-03/V-04.** V-03 (split temporal anchor, single axis)
and V-04 (amend headers + temporal anchor, conversational register) both used a four-field
decision framing form with TEMPORAL ANCHOR and INACTION CONSEQUENCE as separate typed
fields. This structural split prevents consequence-free framing that a single WHY NOW
field allows. V-01 and V-05 use three-field forms that satisfy C-04 but would fail C-13.
V-03's temporal anchor split is the strongest C-04 quality upgrade across all R2 variations.

**Register orthogonality observation.** V-04 (conversational register) reached 100 --
identical ceiling to V-05 (formal register) -- when OWNER format templates were properly
placed. Register choice is orthogonal to structural completeness. This is not encoded as a
criterion; evaluators must not penalize or reward register choice when assessing proposals.

---

## Round 3 Discriminator Notes

Round 3 produced five complete variation scorecards. All five Golden at 100. The v3
rubric was fully saturated -- C-12 and C-13 (the two new v3 criteria) were satisfied by
all five variations because all R3 variations incorporated the structural fixes before
scoring. Discrimination now lives in C-14 through C-18.

**Lifecycle resequencing (C-17) is the highest-value structural insight in R3.** V-04
placed assumption and risk registers (Phases 7-8) before the recommendation (Phase 10).
This is a qualitative change in document logic, not a field addition: registers written
before the recommendation must inform it; registers written after only justify it. The
F-row linkage requirement in C-15 (CONDITIONS must reference an F-row by ID) extends
this causal anchoring -- the recommendation is bound to its failure modes, not merely
its rationale.

**Front-loaded amendment table (C-18) gives the highest enforcement visibility.** V-05's
amendment table, initialized before Phase 1, auto-populates during writing rather than
assembling retrospectively. A reviewer can confirm rubric coverage from a single table
without re-reading the document. Gate-citation shows what a phase was supposed to close;
the front-loaded table shows what criteria were not enforced during writing and who owns
each gap. This is why V-05 ranks #1 in structural value even though all variations scored
identically against the v3 rubric.

**Gate-citation criterion ID drift is a systemic rubric versioning risk (not a criterion).**
V-02, V-04, and V-05 all annotate Phase 3 as `THIS PHASE CLOSES: [C-04, C-12]` but v3
C-12 is OWNER template enforcement and C-13 is split temporal anchor. The mislabeling is
consistent across all gate-citation variations and originates from criterion IDs shifting
between rubric versions without annotation updates. This predicts a systemic auditability
failure if gate-citation is deployed in production without pinning rubric version IDs to
criterion names. Future gate-citation variations must include both ID and name
(e.g., `[C-13 Split temporal anchor]`) to prevent accumulating mislabeling across rubric
versions.

**Variation ranking by structural value beyond rubric (R3):**

| Rank | Variation | Why |
|------|-----------|-----|
| 1 | V-05 | Front-loaded amendment table (C-18); F-rows; P*I anchors; gate-citation combined |
| 2 | V-04 | Lifecycle resequencing (C-17); F-row sign-off linkage (C-15); gate-citation |
| 3 | V-03 | Domain-specific P*I anchors (C-16); cleanest single-axis quality advance |
| 4 | V-02 | Gate-citation auditable at phase level; additive and lossless |
| 5 | V-01 | Safe minimum viable baseline; closes C-14 with zero cognitive overhead |

---

## Round 4 Discriminator Notes

Round 4 produced five complete variation scorecards. V-05 scored 100; V-01, V-02, V-04
scored 99.09; V-03 scored 98.18. The v4 rubric was not fully saturated -- C-18 remained
the ceiling discriminator. V-03 also failed C-15 by design (inertia-forward framing axis
omitted the F-row register entirely to test decision-frame quality in isolation).

**Four new excellence patterns identified in R4, each encoding a structural refinement
beyond its parent criterion.**

**C-19: Canonical label alignment eliminates reviewer inference for C-15.** R3's
"Observable Event / Invalidates / Fallback" template required a reviewer to map synonyms
to C-15's vocabulary. V-01's three-field template uses FAILURE MODE / TRIGGER CONDITION /
MITIGATION verbatim -- the field names and the criterion names match. Scoring becomes
deterministic: the field is either present with the right label or it is not. Synonym
substitution is now a named failure mode.

**C-20: PREREQUISITE GATE converts C-17 from sequence-scan to single-block audit.**
V-02 and V-04/V-05 introduce a typed checklist block immediately before Phase 11. A
reviewer can confirm C-17 compliance by reading one block, not by tracing document order.
The structural analogy: C-12 enforces C-11's owner requirement with a typed slot; C-20
enforces C-17's ordering requirement with a typed gate. Both convert a prose constraint
into a machine-checkable artifact.

**C-21: Dual-signatory F-ROW ANCHOR makes recommendation failure-mode-anchored at the
structural level.** C-15 requires at least one F-row cited in sign-off CONDITIONS; V-01
elevates this to a typed F-ROW ANCHOR slot independently required in both PM and Architect
blocks. Neither signatory can complete their block without naming a failure mode. The two
signatories may name the same F-row or different ones -- structural independence, not
content divergence, is the requirement. This closes the gap where a shared CONDITIONS
block could satisfy C-15 while allowing one signatory's perspective to be failure-mode-free.

**C-22: Named trigger IDs close the criterion-ID drift risk identified in R3.** R3 noted
that gate-citation variations mislabeled Phase 3 as closing C-12 (OWNER enforcement)
when C-13 (split temporal anchor) was the correct criterion, because ID assignment shifted
between rubric versions. C-22 requires each trigger rule in the front-loaded amendment
table to carry a stable named ID, and each amendment row to cite its source trigger ID.
The traceable chain (criterion -> trigger ID -> amendment row) is stable across rubric
versions: trigger IDs do not shift when new criteria are added, so accumulated mislabeling
cannot occur silently.

**Inertia-forward framing (V-03) is not encoded as a criterion.** V-03's INERTIA
BASELINE / INERTIA COST / INERTIA OFFSET fields represent a decision-frame quality
upgrade that is fully compatible with C-01 through C-04. It is an evaluative lens, not a
structural requirement. Evaluators may note its presence as a depth signal; they must not
penalize its absence.

**Variation ranking by structural value beyond rubric (R4):**

| Rank | Variation | Why |
|------|-----------|-----|
| 1 | V-05 | Only variation passing C-18; T-GUARD cascade seeds C-22; strongest integration |
| 2 | V-04 | V-01 + V-02 combined; PREREQUISITE GATE + F-ROW ANCHOR dual-slot; best pre-C-18 ceiling |
| 3 | V-01 | F-row 3-field explicit labels seed C-19; F-ROW ANCHOR dual-slot seeds C-21 |
| 4 | V-02 | PREREQUISITE GATE seeds C-20; single-axis clean; additive and lossless |
| 5 | V-03 | Inertia framing is highest decision-quality signal but sacrifices C-15 by design |

---

## Round 5 Discriminator Notes

Round 5 produced five complete variation scorecards. All five Golden. V-05 scored 100;
V-04 scored 99.33; V-02 and V-03 tied at 98.67; V-01 scored 98.00. Delta between
predicted and actual was 0 across all five variations -- the v5 rubric predicted all
scores exactly.

**Two new excellence patterns identified in R5, both refining the amendment table
machinery introduced in C-18 and C-22.**

**C-23: T-GUARD sentinel eliminates silent gaps without enumerating all scenarios.**
R4's C-22 requires each trigger rule to carry a stable T-NN ID and each amendment row to
cite its source trigger. V-05 introduced T-GUARD as a catch-all whose scope is "any
required typed slot, phase block, or gate item absent." The sentinel fires as a single row
for any structural gap not covered by a specific trigger. Without T-GUARD, a table that
defines T-01 through T-NN for known criteria has no defense against criteria added in
future rubric versions or structural requirements not yet identified. T-GUARD gives the
table completeness over precision: known gaps route to specific triggers; unknown gaps
route to T-GUARD. No enumeration of all possible missing-block scenarios is required.

**C-24: Empty-table completion semantics converts ambiguous state to positive signal.**
R4's C-18 requires the amendment table to show "either populated rows or explicitly empty
rows" at document completion. V-05 clarified what "explicitly empty" means: "T-GUARD
enforced all requirements successfully -- no violations detected." Without this declared
semantics, an empty table is ambiguous: it could mean the table was active and clean, or
it could mean the table was never activated. This is the same structural improvement
applied elsewhere in the rubric: C-13 split WHY NOW into TEMPORAL ANCHOR and INACTION
CONSEQUENCE to prevent consequence-free framing; C-24 splits "empty table" into
"active-and-clean" vs "not-tracked" to prevent enforcement theater.

**V-02/V-03 orthogonality confirmation.** Both scored 98.67. V-02's sole axis was C-20
(PREREQUISITE GATE); V-03's sole axis was C-21 (dual-signatory F-ROW ANCHOR). Their
identical scores confirm C-20 and C-21 are genuinely orthogonal -- neither criterion
subsumes the other. A variation can pass C-21 while failing C-20, and vice versa. The
R5 scorecard provides the clearest empirical demonstration of this independence.

**Variation ranking by structural value beyond rubric (R5):**

| Rank | Variation | Why |
|------|-----------|-----|
| 1 | V-05 | T-GUARD catch-all + empty-table semantics: seeds C-23 and C-24; only variation at 100 |
| 2 | V-04 | First variation combining C-19 + C-20 + C-21 without structural tension; seeds integration pattern |
| 3 | V-03 | Independent F-ROW ANCHOR in both signatory blocks without table machinery; C-21 single-axis clean |
| 4 | V-02 | PREREQUISITE GATE with named binaries; cleanest C-20 single-axis demonstration |
| 5 | V-01 | F-row precision cluster (C-19, C-21) without any table machinery; minimum viable ceiling |

---

## Round 6 Discriminator Notes

Round 6 produced five complete variation scorecards. All five Golden. V-04 and V-05
scored 100; V-01 and V-02 tied at 99.41; V-03 scored 98.82. Delta between predicted and
actual was 0 across all five variations -- the v6 rubric predicted all scores exactly.

**Three new excellence patterns identified in R6, each refining an element of the
amendment table lifecycle.**

**C-25: Sentinel-first ordering shifts amendment enforcement from backstop to frontline.**
R5's C-23 requires T-GUARD to be defined at initialization with correct scope vocabulary.
V-05 placed T-GUARD as the first entry in the trigger table, before T-01. This changes
enforcement direction: when T-GUARD is listed last, it is a backstop -- only fires after
all specific triggers fail to match. When T-GUARD is listed first, unenumerated gaps route
to it immediately; specific triggers handle the cases that T-GUARD would route too
broadly. The structural analogy: C-20's PREREQUISITE GATE converts C-17's ordering
requirement from a sequence-scan to a single-block audit; C-25 converts C-23's sentinel
from a last-resort catch to a first-routed catch. The improvement is verifiable from
position 1 in the trigger table alone.

**C-26: COMPLETION STATUS as a Phase 0 typed slot makes enforcement lifecycle complete.**
R5's C-24 requires an explicit completion-state declaration at document end. V-05
implemented this as a COMPLETION STATUS typed slot in the Phase 0 initialization block,
pre-populated with "PENDING." At document completion the slot is updated to the canonical
terminal value. The structural improvement: a prose instruction at Phase 13 to "write a
completion declaration" can be followed or skipped silently. A Phase 0 typed slot that
is initialized to "PENDING" is a live mandatory field from document creation -- the model
cannot reach Phase 13 without addressing it. The pattern is identical to how C-18
improved C-09: C-09 required amend items at the end; C-18 required the table to be
initialized at the start. C-26 applies the same prospective initialization logic to the
completion declaration itself.

**C-27: INERTIA COST / INERTIA OFFSET converts do-nothing from qualitative to computable.**
R4's V-03 introduced inertia-forward framing as an evaluative lens; the R4 notes
explicitly declined to encode it as a criterion. R6 V-04 operationalized the pattern
with three changes that make it structurally testable: (1) the do-nothing option carries
a numeric INERTIA COST per sprint using the C-16 P*I scale, (2) each alternative names
its INERTIA OFFSET sprint crossover point, and (3) the PREREQUISITE GATE block (C-20)
is extended with an inertia-axis binary item. The third change is the deciding factor:
a PREREQUISITE GATE item makes inertia-axis completeness machine-checkable in the same
way C-20 made register ordering machine-checkable. Without the gate item, INERTIA fields
are evaluative depth signals like V-03. With the gate item, they are structurally
required and auditability is preserved.

**C-23/C-24 structural decoupling confirmed.** V-01 (exact C-24 declaration, generic
T-GUARD scope) and V-02 (exact C-23 scope vocabulary, no completion declaration) tied at
99.41 with independent failure axes. V-03 (neither C-23 nor C-24) scored 98.82 -- each
criterion contributes exactly 0.50 points independently. No criterion subsumes the other.

**Variation ranking by structural value beyond rubric (R6):**

| Rank | Variation | Why |
|------|-----------|-----|
| 1 | V-05 | Sentinel-first (C-25) + COMPLETION STATUS slot (C-26); strongest amendment lifecycle integration |
| 2 | V-04 | INERTIA COST / INERTIA OFFSET + PREREQUISITE GATE extension (C-27); orthogonal quantification axis |
| 3 | V-01 | Exact C-24 declaration; C-23 fails by design; single-axis clean C-24 demonstration |
| 4 | V-02 | Exact C-23 scope vocabulary; C-24 fails by design; single-axis clean C-23 demonstration |
| 5 | V-03 | R5 V-05 machinery complete; neither R6 criterion addressed; lower bound confirmation |

---

## Round 7 Discriminator Notes

Round 7 produced five complete variation scorecards. V-04 and V-05 scored 100; V-01,
V-02, and V-03 scored 99.5. Delta between predicted and actual was 0 across all five
variations -- the v7 rubric predicted all scores exactly.

**Four new excellence patterns identified in R7: two from V-04's axes (PM-first,
table-dominant) and two from V-05's axes (lifecycle-heavy, inertia-forward).**

**C-28: PM-first sign-off ordering extends C-21's dual-signatory requirement with a causal
direction constraint.** V-04's "PM-first" axis placed the PM sign-off block before the
Architect sign-off block in the recommendation phase. The ordering encodes a decision
logic: whether the option is the right decision (business question) must be resolved
before whether it is the right design (technical question). C-06 requires two distinct
role contributions; C-21 requires two independent signatory blocks with F-ROW ANCHOR
slots; C-28 requires the business-facing signatory to appear first. The improvement is
independently verifiable from position 1 in the recommendation phase sign-off section
without scanning the remainder of the phase.

**C-29: Table-dominant register format extends C-19 from the failure mode register to all
three named registers.** V-04's "table-dominant" axis used structured tables with typed
column headers for the assumption register, risk register, and failure mode register.
C-19 requires canonical label alignment for the failure mode register only. C-29 requires
table-format consistency across all three registers using the canonical column header
vocabulary per register type: A-NN / ASSUMPTION / VALIDATION PLAN for assumptions;
R-NN / RISK / P / I / P*I / MITIGATION for risks; F-NN / FAILURE MODE / TRIGGER
CONDITION / MITIGATION for failure modes. A document where any register uses prose with
embedded field labels fails C-29 regardless of content correctness and regardless of
the other registers' formats.

**C-30: Phase manifest at Phase 0 extends C-18's prospective initialization to the
document's lifecycle structure itself.** V-05's "lifecycle-heavy" axis initialized a
phase manifest in Phase 0, listing every phase by sequence number and name before content
phases began. C-18 requires the amendment tracking table to be initialized at Phase 0;
C-30 requires an independent phase manifest block that catalogs the document's complete
phase sequence. This converts C-17 compliance (assumption and risk registers precede
recommendation) from a document-scan to a single-block audit: a reviewer reads the
Phase 0 manifest, confirms register phases appear before the recommendation phase in the
listed sequence, then spot-checks at most two phase boundaries. The manifest must be
complete -- any phase omitted or invented falsifies C-30 regardless of the phases it
does list.

**C-31: DECISION LEAD TIME links INERTIA OFFSET to TEMPORAL ANCHOR as a computable
urgency metric.** V-05's "inertia-forward" axis computed DECISION LEAD TIME = TEMPORAL
ANCHOR sprint minus INERTIA OFFSET sprint for each alternative, and flagged non-positive
results with a typed ESCALATION FLAG. C-27 requires INERTIA OFFSET to be named as a
sprint crossover point; C-13 requires TEMPORAL ANCHOR to be a specific named deadline;
C-31 requires these two values to be subtracted and the result typed. The computation
surfaces the inertia trap condition -- when DECISION LEAD TIME is zero or negative,
acting within the named deadline no longer pays for itself before the deadline arrives.
The ESCALATION FLAG converts this from an implicit condition to a named structural
artifact. The PREREQUISITE GATE (C-20) is extended with a lead-time binary item,
preserving the gate's single-block auditability.

**C-25/C-26/C-27 structural independence confirmed.** V-01 (T-GUARD last), V-02 (no
COMPLETION STATUS Phase 0 slot), and V-03 (no INERTIA COST/OFFSET) each failed exactly
one criterion and scored 99.5. No cascade: C-25 failure does not cause C-26 or C-27
failure. Each deduction was independent. The denominator advances from /20 to /24.

**Variation ranking by structural value beyond rubric (R7):**

| Rank | Variation | Why |
|------|-----------|-----|
| 1 | V-05 | Lifecycle-heavy + inertia-forward: seeds C-30 (phase manifest) and C-31 (lead time); both new patterns in one variation |
| 2 | V-04 | PM-first + table-dominant: seeds C-28 (sign-off ordering) and C-29 (table registers); both new patterns in one variation |
| 3 | V-03 | Full C-25/C-26 machinery; INERTIA omitted by design; clean single-axis C-27 non-demonstration |
| 4 | V-02 | Full C-25/C-27 machinery; COMPLETION STATUS omitted by design; clean single-axis C-26 non-demonstration |
| 5 | V-01 | Full C-26/C-27 machinery; T-GUARD at last position by design; clean single-axis C-25 non-demonstration |

---

## Trace Alignment Notes

The trace artifact (`plugin-draft-proposal-2026-03-14.md`) demonstrates:
- **C-01**: 4 options (A: skills-in-repo, B: plugin only, C: both, D: CREST) -- status-quo implicit in D
- **C-02**: Each option has description, pros via dimension table, cons/risk in Architect scoring
- **C-03**: Explicit recommendation (Option A for v0.1, C for v0.2), HIGH confidence, 3 conditions listed
- **C-04**: PM frames decision with 6-week all-hands deadline and cost of inaction stated
- **C-05**: Scout artifacts found -- competitors trace and feasibility trace (62/100 scoped)
- **C-06**: PM and Architect contribute distinct named sections
- **C-07**: Dimension comparison table with 6 rows across 4 options
- **C-08**: Assumption register (A1-A3) and risk register (R1-R2) both present
- **C-09**: Amend phase adds Option E, flags equal-weight criteria, notes community fork consideration
- **C-10**: Scout artifact inventory appears as a discrete pre-option step listing competitors trace and feasibility trace by name
- **C-11**: Amend phase covers all three categories -- Option E (missing option), equal-weight criteria flag (unweighted criterion), community fork follow-up (follow-up action)
- **C-12**: Not demonstrated in trace -- amend entries do not carry structural OWNER slots across all three categories; trace satisfies C-11 but does not demonstrate C-12
- **C-13**: Not demonstrated in trace -- decision framing uses a single WHY NOW field with the 6-week all-hands deadline embedded in prose; trace satisfies C-04 but would require TEMPORAL ANCHOR + INACTION CONSEQUENCE split to satisfy C-13
- **C-14**: Not demonstrated in trace -- amend entries carry no DEADLINE typed slot in any category template; trace satisfies C-12 (partially) but fails C-14
- **C-15**: Not demonstrated in trace -- no F-row register present; risk register (R1-R2) satisfies C-08 but no failure mode entries with sign-off linkage exist
- **C-16**: Not demonstrated in trace -- risk entries use qualitative framing without numeric P and I scores or project-specific anchor definitions; C-08 passes but C-16 fails
- **C-17**: Not demonstrated in trace -- assumption and risk registers appear after the recommendation section; causal ordering is inverted relative to C-17 requirement
- **C-18**: Not demonstrated in trace -- no amendment table initialized before Phase 1; all amend items are assembled retrospectively in the amend phase
- **C-19**: Not demonstrated in trace -- no F-row register present; label alignment cannot be assessed without a register
- **C-20**: Not demonstrated in trace -- no PREREQUISITE GATE block present; C-17 already fails
- **C-21**: Not demonstrated in trace -- no F-ROW ANCHOR typed slot in either PM or Architect sign-off block; C-15 already fails
- **C-22**: Not demonstrated in trace -- no front-loaded amendment table with named trigger IDs; C-18 already fails
- **C-23**: Not demonstrated in trace -- no front-loaded amendment table present; T-GUARD sentinel cannot exist without C-18 initialization; C-18 already fails
- **C-24**: Not demonstrated in trace -- no amendment table present; completion-state declaration cannot exist without C-18 initialization; C-18 and C-23 already fail
- **C-25**: Not demonstrated in trace -- no trigger table present; sentinel-first position cannot be verified without a trigger table; C-18 and C-23 already fail
- **C-26**: Not demonstrated in trace -- no Phase 0 initialization block present; COMPLETION STATUS typed slot cannot exist without C-18 table initialization; C-18, C-23, and C-24 already fail
- **C-27**: Not demonstrated in trace -- do-nothing option (D: CREST) carries no INERTIA COST field; no alternative carries an INERTIA OFFSET; PREREQUISITE GATE not present; C-16 and C-20 already fail in trace
- **C-28**: Not demonstrated in trace -- no dual-signatory sign-off blocks present in the recommendation phase; PM-first ordering cannot be assessed without independent PM and Architect sign-off blocks; C-15 and C-21 already fail
- **C-29**: Not demonstrated in trace -- assumption and risk registers use prose list format with embedded field labels, not structured tables with typed column headers; C-16 already fails so numeric column headers are not present; C-29 would fail independently even if C-16 passed
- **C-30**: Not demonstrated in trace -- no Phase 0 initialization block present; a phase manifest cannot exist without a Phase 0 initialization section; C-18 already fails
- **C-31**: Not demonstrated in trace -- no DECISION LEAD TIME field present on any alternative; no ESCALATION FLAG field present; C-27 already fails so INERTIA OFFSET is not named; C-13 also fails so TEMPORAL ANCHOR is not a typed field; C-31 would fail independently even if C-13 and C-27 both passed
