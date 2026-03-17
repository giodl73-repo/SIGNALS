Written to `simulations/quest/rubrics/draft-proposal-rubric-v5-2026-03-14.md`.

---

## v5 Summary

**4 new aspirational criteria from R4 excellence signals:**

| ID | Criterion | Parent | What it adds |
|----|-----------|--------|--------------|
| C-19 | **Canonical F-row field label alignment** | C-15 | FAILURE MODE / TRIGGER CONDITION / MITIGATION used as exact field labels — synonym substitution (Observable Event, Fallback) requires inference and fails; scoring becomes deterministic |
| C-20 | **PREREQUISITE GATE block for register verifiability** | C-17 | Typed checklist block immediately before Phase 11 — C-17 compliance auditable at single point without document scan; analogous to how C-12 enforces C-11 with a typed slot |
| C-21 | **Dual-signatory F-ROW ANCHOR typed slots** | C-15 | Both PM and Architect sign-off blocks each carry an independent F-ROW ANCHOR slot — shared CONDITIONS reference (C-15) is not sufficient; neither signatory can complete their block without naming a failure mode |
| C-22 | **Named amendment trigger IDs with row-level back-reference** | C-18 | Each trigger rule carries a stable ID (T-01, T-02...); each amendment row cites its source trigger ID — closes the criterion-ID drift risk identified in R3 |

**Inertia-forward framing (V-03 axis)** not encoded — evaluative lens, not structural requirement.

**New denominator:** aspirational `/15`. Ceiling remains 100 (V-05 already passes all 15 aspirational criteria via T-GUARD cascade).
s optional depth beyond C-04 and C-13.

**Scoring formula:**
```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 15 * 10)
```

**Other updates:**

- Aspirational denominator bumped from `/11` to `/15` in scoring formula
- Structure summary updated: 11 aspirational -> 15 aspirational
- Common failure modes: added C-19 label-synonym failure mode; C-20 gate-absent failure mode; C-21 shared-block failure mode; C-22 ID-drift failure mode
- New "Round 4 Discriminator Notes" section added
- Trace alignment notes extended to cover C-19 through C-22

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

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 15 * 10)
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
