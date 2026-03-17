**v3 complete.** Here is what changed and why:

---

**New aspirational criteria:**

| ID | Criterion | Source |
|----|-----------|--------|
| C-12 | **Structural OWNER template enforcement** | V-02/V-03 failure pattern — listing three amend categories without a typed OWNER slot in each template allows silent omission. C-11 requires at least one owner in FOLLOW-UP; C-12 requires a typed OWNER slot on every entry across all three categories. |
| C-13 | **Split temporal anchor** | V-03/V-04 excellence pattern — TEMPORAL ANCHOR + INACTION CONSEQUENCE as separate typed fields prevents consequence-free framing that a single WHY NOW field allows. C-04 passes with one field; C-13 requires both. |

**Register orthogonality** (V-04 reaching 100 in conversational register) is recorded as an observation in Round 2 Discriminator Notes, not as a criterion — it is an absence of failure rather than a positive achievement.

**Scoring formula:** aspirational denominator bumped from `/4` to `/6`.

**C-11 pass condition tightened:** now explicitly states that a structural OWNER slot in the format template is required — instruction alone is insufficient (this is what V-02/V-03 violated).

**Trace gaps identified:** the trace artifact does not demonstrate C-12 or C-13 — both are live targets for Round 3 variation design.
deadline, each fail this criterion. Both fields must appear before the options section.

**Other updates:**

- Aspirational denominator bumped from `/4` to `/6` in scoring formula
- Structure summary updated: 4 aspirational -> 6 aspirational
- C-11 pass condition tightened: clarifies that structural OWNER template slot is required, not just an instruction to name owners -- this is what V-02/V-03 violated
- Common failure modes: added C-11/C-12 structural failure mode; added C-13 temporal anchor failure mode
- New "Round 2 Discriminator Notes" section added
- Trace alignment notes extended to cover C-12 and C-13
- Register orthogonality observation: V-04 conversational register reaches 100 -- the same ceiling as V-05 -- when OWNER format templates are properly placed. Register choice is orthogonal to structural completeness. This is an observation, not a criterion; evaluators must not penalize or reward register choice.

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
| C-13 | **Split temporal anchor** | depth | The decision framing step uses two separate typed fields: TEMPORAL ANCHOR (a specific named date, sprint, or event -- vague language such as "soon," "before it's too late," or "in the near term" is explicitly prohibited) and INACTION CONSEQUENCE (a concrete named outcome of not deciding -- teams blocked, capability lost, or window closed -- missed-feature statements do not qualify). A single WHY NOW field satisfies C-04 but not C-13. The split prevents consequence-free framing: a deadline without a named outcome fails C-13, and an outcome without a named deadline also fails C-13. Both typed fields must appear before the options section. |

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 6 * 10)
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
