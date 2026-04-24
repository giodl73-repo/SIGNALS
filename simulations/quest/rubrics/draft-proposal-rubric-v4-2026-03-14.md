Here is the complete v4 rubric:

---

**v4 adds 5 new aspirational criteria, bumps aspirational denominator from `/6` to `/11`.**

**New criteria extracted from R3 scorecard:**

| ID | Criterion | Source pattern |
|----|-----------|----------------|
| C-14 | **Amend entry deadline enforcement** | V-01 discriminator: "Closes C-14 (deadline on all amend categories)" — DEADLINE typed slot required in every amend category template alongside OWNER (C-12). Specific sprint/date/milestone only; TBD fails. |
| C-15 | **F-row failure mode register with sign-off linkage** | V-04 discriminator: "CONDITIONS must reference an F-row by ID" — failure mode register (F-NN) distinct from the risk register; at least one F-row cited by ID in recommendation CONDITIONS. C-08 passing does not satisfy C-15. |
| C-16 | **Numeric P*I risk scoring with project-specific anchors** | V-03 discriminator: "Seeds C-16" — separate numeric P and I (1-5 each), compound P*I score, and project-specific anchor definitions (what does P=3 mean *here*?) required before scoring. L/M/H labels fail C-16. |
| C-17 | **Registers-before-recommendation lifecycle ordering** | R3 assessment: "most discriminating advance in R3" — both assumption and risk registers must precede the recommendation in document sequence. Post-hoc registers can only justify; pre-recommendation registers must inform. C-08 correct content does not satisfy C-17. |
| C-18 | **Front-loaded amendment table** | R3 excellence signal #1, V-05 ranked #1 — amendment table initialized before Phase 1 with auto-generate trigger rules; reviewer confirms coverage from table alone. C-09/C-11 correct contents do not satisfy C-18. |

**Gate-citation ID drift** (Phase 3 mislabeled as closing C-12 instead of C-13 across V-02/V-04/V-05) is a Round 3 discriminator observation, not a criterion. Prescription: future gate-citation variations must pin criterion names alongside IDs.

**Scoring formula:**
```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 11 * 10)
```

Written to `simulations/quest/rubrics/draft-proposal-rubric-v4-2026-03-14.md`.
s a rubric versioning risk, not a positive quality behavior to evaluate in proposals.

**Scoring formula:** aspirational denominator bumped from `/6` to `/11`.

**Other updates:**

- Aspirational denominator bumped from `/6` to `/11` in scoring formula
- Structure summary updated: 6 aspirational -> 11 aspirational
- Common failure modes: added C-14 amend deadline failure mode; C-15 F-row sign-off failure mode; C-16 holistic risk label collapse; C-17 registers-after-recommendation ordering; C-18 retrospective-only amendment
- New "Round 3 Discriminator Notes" section added
- Trace alignment notes extended to cover C-14 through C-18

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

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 11 * 10)
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
