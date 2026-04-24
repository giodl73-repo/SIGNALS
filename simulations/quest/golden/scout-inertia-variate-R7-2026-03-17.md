---
skill: quest-variate
skill_target: scout-inertia
date: 2026-03-17
round: 7
rubric: v7
variations: 5
---

# scout-inertia -- Prompt Variations R7

## Context

R6 results: V-03, V-04, V-05 scored 100/100 on rubric v6. V-01 and V-02 scored 99.6
due to C-12 PARTIAL -- missing NAMED CLAIM scaffold and Anchored Rebuttal Protocol label.

Rubric v7 adds three new aspirational criteria (denominator 12 -> 15):

- **C-21**: All multi-component requirements named as sub-protocols (upgrades C-19's
  "at least one" to "all five"). R6 V-01/V-02 fail -- only Replication Fidelity Standard
  was named. R6 V-03/V-04/V-05 already pass.
- **C-22**: Counter-example pairs at every failure condition (upgrades C-20's "at least
  two" to maximum density). R6 V-01 and V-03 fail -- pairs present at a subset of sites
  only. R6 V-02, V-04, V-05 already pass or are close.
- **C-23**: Protocol names double-declared in both manifest and section header. R6 V-01
  and V-02 fail -- manifest names sections without sub-protocol names. R6 V-03 fails --
  synthesis manifest omits sub-protocol names. R6 V-04 and V-05 already pass.

R6 performance under v7 rubric (retroactive):
- V-01: C-12 PARTIAL, C-21 FAIL, C-22 FAIL, C-23 FAIL -> ~76/100
- V-02: C-12 PARTIAL, C-21 FAIL, C-22 PASS, C-23 FAIL -> ~82/100
- V-03: C-21 PASS, C-22 PARTIAL (3+ pairs, not maximum density), C-23 FAIL -> ~92/100
- V-04: C-21 PASS, C-22 PASS, C-23 PASS -> 100/100
- V-05: C-21 PASS, C-22 PASS, C-23 PASS -> 100/100

**Design goal for R7**: All 5 variations pass C-21, C-22, C-23, plus fix C-12 in V-01
and V-02. Four structural gaps to close across the three non-passing variations.

**Design axes available**:
- C-23 compliance mechanism: manifest-plus-header vs explicit constraint instruction
  vs phase-header-fusion
- C-22 enforcement style: per-site annotation vs explicit density constraint instruction
  vs pre-flight verification gate
- C-12 fix: adding NAMED CLAIM scaffold + Anchored Rebuttal Protocol label to V-01/V-02
- Register: inertia-first (V-01), schema-block (V-02), adversarial roles (V-03),
  phase-structured (V-04), full-stack with verification (V-05)

Single-axis choices: C-23 minimum viable on simple base (V-01), C-22 per-site
enforcement (V-02), C-23 via explicit synthesis constraint (V-03). Combined: explicit
declaration+density constraints on phase-fusion base (V-04), pre-flight verification
gate on full-stack base (V-05).

## Variation Map

| ID | Axis | Hypothesis |
|----|------|------------|
| V-01 | Single-axis C-23 minimum viable on inertia-framing base | Adding sub-protocol names to both the heading manifest and section headers, plus the Anchored Rebuttal Protocol label (fixing C-12), satisfies C-23 and C-21 with minimal scaffold change on the simplest base. Tests whether C-23 is achievable without roles or phases -- just two aligned structural sites. |
| V-02 | Single-axis C-22 per-site enforcement on schema-block base | Adding [PAIR REQUIRED] annotations at every requirement site that admits a predictable violation converts C-22 from a density goal to an explicit per-site constraint. Tests whether site-level enforcement notation increases C-22 reliability over density-by-example. |
| V-03 | Single-axis C-23 via explicit constraint instruction on role-instruction base | Updating the synthesis manifest to include sub-protocol names AND adding an explicit constraint ("each sub-protocol name must appear in both this manifest and its section heading") satisfies C-23 on the adversarial role base. Tests whether naming the double-declaration as a constraint produces structural compliance. |
| V-04 | Combined C-21+C-22+C-23: explicit constraint sentences on phase-fusion base | R6 V-04 already passes all three new criteria implicitly. R7 V-04 makes all three properties explicit instructions: a structural constraint for C-23 matching, a density constraint for C-22, and a count-all-five reminder for C-21. Tests whether explicit constraint sentences increase adversarial robustness without structural change. |
| V-05 | Combined all axes: pre-flight verification gate enforcing C-21+C-22+C-23 | R6 V-05 passes all three new criteria but relies on implicit compliance. R7 V-05 adds a mandatory pre-flight verification step where the model must check and confirm each property before writing the artifact. Converts C-21/C-22/C-23 from properties-to-achieve to properties-to-verify. |

---

## V-01 -- Axis: C-23 Minimum Viable (Double-Declaration on Inertia-Framing Base)

**Hypothesis**: The simplest single-role scaffold can satisfy C-23 by placing sub-protocol
names in both the global heading manifest and each corresponding section header. Adding
the Anchored Rebuttal Protocol label and NAMED CLAIM scaffold simultaneously fixes the
R6 C-12 PARTIAL gap. Tests whether C-23 is achievable at the lowest structural cost --
no roles, no phases, no schema blocks -- just consistent naming at two sites.

This is R6 V-01 (Competitor Zero framing, single role, inline "Required columns" manifests)
with four additions: (1) all five sub-protocol names in the heading manifest, (2) all five
sub-protocol names in section headers, (3) Anchored Rebuttal Protocol as a named three-step
construct in section 7, (4) pass/fail pairs at every requirement site that admits a
predictable violation (C-22 upgrade from R6 V-01's minimum pairs).

```
Auto-detect the feature from repo context. Do not prompt unless context is absent.

## Competitor Zero: Status Quo / Do Nothing

Before any named competitor, analyze the primary competitor: the option to do
nothing and keep the current workaround. Treat inertia as a named competitor.
Profile it fully.

This output must contain the following sections:
- Workaround Description -- Replication Fidelity Standard
- Switching Cost Profile -- Switching Cost Protocol
- Inertia Threat Score
- Why Inertia Loses -- Loss Condition Standard
- Workaround Failure Modes -- Failure Mode Standard
- Forward-Looking Risk
- Steelman and Rebuttal -- Anchored Rebuttal Protocol

**1. Workaround Description -- Replication Fidelity Standard**

Describe the workaround so that another team with no prior context could reproduce
it independently. Apply the Replication Fidelity Standard:

1. Name each tool by product, not by category.
   Pass: "GitHub Actions" / Fail: "CI system"
   Pass: "custom Python script invoked by a Makefile target" / Fail: "automation script"
2. Enumerate the major steps in numbered sequence.
   Pass: "1. engineer opens template, 2. edits four fields, 3. pings #approvals" /
   Fail: "team follows the documentation process"
3. Flag institutional knowledge: any step requiring tribal context, undocumented
   conventions, or shared credentials a new team member would not have.
   Pass: "step 3 requires posting in #approvals with a specific prefix -- not in
   onboarding docs" / Fail: [omitting an undocumented step]

All three sub-requirements of the Replication Fidelity Standard must be satisfied
independently. Name the workaround. One paragraph minimum.

**2. Switching Cost Profile -- Switching Cost Protocol**

Apply the Switching Cost Protocol. Three line items, each with a numeric estimate
or explicit N/A with justification:
- Time: hours or days to migrate existing setups, per project or per team.
  Pass: "2-4 hours per project for YAML migration" / Fail: "moderate effort"
- Training: days of onboarding, number of people affected, ramp-up friction.
  Pass: "1-2 days for 3-4 engineers covering API changes and new config format" /
  Fail: "some training required"
- Disruption: coordination overhead, workflow interruption, dependencies that must change.
  Pass: "CI pipeline paused for 4-hour migration window, coordinated with ops team" /
  Fail: "team disruption expected"

**3. Inertia Threat Score**

Assign: HIGH (default and required). Downgrading below HIGH requires a written
justification with evidence. Absence of a score is an automatic analysis failure.
Pass: explicit "HIGH" label present. / Fail: narrative language ("elevated concern",
"real risk") substituted for the explicit severity token.

**4. Why Inertia Loses -- Loss Condition Standard**

Apply the Loss Condition Standard. Two or more conditions. Each must be falsifiable.

Required columns for this table: # | Condition | Observable Threshold | Verification Command

| # | Condition | Observable Threshold | Verification Command |
|---|-----------|---------------------|---------------------|
| 1 | [condition] | [measurable trigger] | [Tool: Action -> Result when threshold applies] |
| 2 | [condition] | [measurable trigger] | [Tool: Action -> Result when threshold applies] |

Observable Threshold:
Pass: "active project count >= 4" / Fail: "when teams get busy"

Verification Command format: `[Tool or artifact]: [what to open or run] ->
[what the result looks like when threshold applies]`
Pass: "Jira: open the active sprint board -> count rows where Status = Active.
If >= 4, condition applies."
Pass: "GitHub: run `gh pr list --state open | wc -l` -> if output >= 10, threshold met."
Fail: "you can check project count" / Fail: "review your sprint board"

**5. Workaround Failure Modes -- Failure Mode Standard**

Distinct from switching costs. Failure modes = what goes wrong if you stay.
Apply the Failure Mode Standard. Two or more required.

Required columns for this table: # | Failure Mode | Trigger | Impact | Severity

| # | Failure Mode | Trigger | Impact | Severity |
|---|-------------|---------|--------|---------|
| 1 | [specific failure] | [what causes it] | [consequence to team] | HIGH |
| 2 | [specific failure] | [what causes it] | [consequence to team] | MED |

Trigger: Pass: "when queue depth exceeds 500 messages" / Fail: "under heavy load"
Impact: Pass: "events silently dropped with no error surfaced to the caller" /
Fail: "the workaround stops working"
Severity: Pass: "HIGH -- events silently dropped with no audit trail, creating a
compliance gap" / Fail: "HIGH" without specifying the data-integrity or compliance
exposure.
Trigger and Impact are separate columns -- do not merge.
"Does not scale" without a named scale limit does not pass.

**6. Forward-Looking Risk**

What happens to teams that stay on the workaround for the next 6-12 months? Name
a specific compounding cost, accumulating debt, or divergence risk with a time horizon.
Pass: "within 6 months, the custom script will need re-porting as the upstream API
changes its response shape, breaking all teams on the workaround simultaneously" /
Fail: "the workaround will become harder to maintain over time"

**7. Steelman and Rebuttal -- Anchored Rebuttal Protocol**

Apply the Anchored Rebuttal Protocol -- three steps in sequence, do not merge:

1. Write the strongest possible argument a skeptical senior engineer would make for
   staying on the workaround. Label it: **STEELMAN**
   Pass: names the specific friction, cost, or risk a real skeptic would actually
   cite -- a concrete concern, not a general principle. /
   Fail: "simplicity is valuable" (a principle, not a claim a real skeptic would
   stake credibility on).

2. Extract the single strongest specific claim. One complete declarative sentence.
   Label it: **NAMED CLAIM: "[exact text of claim]"**

3. Rebut only that named claim. One paragraph. State specifically why it fails --
   with evidence or reasoning tied to the claim's content.
   Pass: rebuttal names the specific weakness in the claim's logic or premise. /
   Fail: "while simplicity matters, the feature offers..." without addressing the
   claim's specific assertion.

---

After profiling Competitor Zero, add:
- Named competitors (3-5): feature overlap, threat level (HIGH/MEDIUM/LOW),
  one-line differentiation
- The whitespace: what no competitor owns
- Table stakes: what any entrant must match

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## V-02 -- Axis: C-22 Per-Site Enforcement (Annotated Schema-Block Base)

**Hypothesis**: Adding [PAIR REQUIRED] annotations at every requirement site that
admits a predictable violation converts C-22 from a density expectation to an
explicit per-site constraint. Each annotated site is a structural enforcement point --
the model must produce a pass/fail pair at that position or the annotation flags a
missed requirement. Tests whether site-level enforcement notation produces more
reliable C-22 compliance than density-by-example alone.

This is R6 V-02 (schema blocks, "Required Output Structure", maximum C-20 density)
with four additions: (1) all five sub-protocol names in the heading manifest and
section headers (C-23, C-21), (2) [PAIR REQUIRED] annotation added before every
requirement site, (3) Anchored Rebuttal Protocol as a named three-step construct with
NAMED CLAIM label (fixing C-12), (4) Long-Term Risk section given an explicit
pass/fail pair.

```
Auto-detect the feature from repo context. Do not prompt unless context is absent.

Analyze the inertia competitor -- the option to keep the current workaround instead
of adopting this feature. Answer the central question: **why does inertia lose?**
If you cannot answer it, stop and flag.

This output must contain the following sections:
- Section 1: Workaround Description -- Replication Fidelity Standard
- Section 2: Switching Cost Table -- Switching Cost Protocol
- Section 3: Inertia Threat Score
- Section 4: Why Inertia Loses -- Loss Condition Standard
- Section 5: Workaround Failure Modes -- Failure Mode Standard
- Section 6: Long-Term Risk of Staying
- Section 7: Steelman and Rebuttal -- Anchored Rebuttal Protocol

### Section 1: Workaround Description -- Replication Fidelity Standard

**Replication Fidelity Standard:**
1. Tool names: product-level, not category-level.
   [PAIR REQUIRED] Pass: "GitHub Actions" / Fail: "CI system"
   [PAIR REQUIRED] Pass: "Confluence page" / Fail: "doc"
   [PAIR REQUIRED] Pass: "custom Python script invoked by a Makefile target" /
   Fail: "automation script"
2. Steps: enumerated in numbered sequence, not summarized prose.
   [PAIR REQUIRED] Pass: "1. Engineer opens Confluence template, 2. copies to
   project page, 3. edits four required fields, 4. pings #approvals" /
   Fail: "team follows the standard documentation process"
3. Institutional knowledge: any step requiring tribal context flagged explicitly.
   [PAIR REQUIRED] Pass: "requires access to #approvals Slack channel -- not in
   onboarding docs" / Fail: [omitting a step that depends on undocumented knowledge]

Name the workaround. Write one paragraph minimum.

### Section 2: Switching Cost Table -- Switching Cost Protocol

Apply the Switching Cost Protocol. All three dimensions required.

| Dimension | Estimate | Basis |
|-----------|----------|-------|
| Time | [X hours/days per project] | [what drives this] |
| Training | [X days, Y people] | [what must be learned] |
| Disruption | [what changes, who is affected] | [coordination cost] |

[PAIR REQUIRED] Time: Pass: "2-4 hours per project for YAML migration" /
Fail: "moderate effort" or "significant time"
[PAIR REQUIRED] Training: Pass: "1-2 days for 3-4 engineers covering X and Y" /
Fail: "some training required"
[PAIR REQUIRED] Disruption: Pass: "CI pipeline paused for 4-hour migration window,
coordinated with ops" / Fail: "team disruption expected"

### Section 3: Inertia Threat Score

```
Threat: HIGH
```

Downgrade below HIGH only with written justification and evidence.
[PAIR REQUIRED] Pass: explicit "HIGH" label with any qualifier. / Fail: omitting
the score or substituting narrative language ("elevated concern", "real risk")
without the explicit severity token.

### Section 4: Why Inertia Loses -- Loss Condition Standard

Apply the Loss Condition Standard. Two or more conditions. Each must be falsifiable.

> Schema: # | Condition | Observable Threshold | Verification Command

| # | Condition | Observable Threshold | Verification Command |
|---|-----------|---------------------|---------------------|
| 1 | [condition] | [measurable trigger] | [see format below] |
| 2 | [condition] | [measurable trigger] | [see format below] |

[PAIR REQUIRED] Observable Threshold: Pass: "active project count >= 4" /
Fail: "when teams get busy"
[PAIR REQUIRED] Verification Command format: `[Tool or artifact]: [what you open
or run] -> [what the result looks like when the threshold applies]`
Pass: "Jira: open the active sprint board -> count rows where Status = Active.
If >= 4, condition applies."
Pass: "GitHub: run `gh pr list --state open | wc -l` -> if output >= 10, threshold met."
Fail: "You can check project count" / Fail: "Review your sprint board"

The command must name a specific tool and a concrete action without requiring a
follow-up question.

### Section 5: Workaround Failure Modes -- Failure Mode Standard

Apply the Failure Mode Standard. Distinct from switching costs. Failure modes =
what goes wrong if you stay.

> Schema: # | Failure Mode | Trigger | Impact | Severity

| # | Failure Mode | Trigger | Impact | Severity |
|---|-------------|---------|--------|---------|
| 1 | [specific failure] | [what triggers it] | [consequence to team] | HIGH / MED / LOW |
| 2 | [specific failure] | [what triggers it] | [consequence to team] | HIGH / MED / LOW |

[PAIR REQUIRED] Trigger: Pass: "when queue depth exceeds 500 messages" /
Fail: "under heavy load"
[PAIR REQUIRED] Impact: Pass: "events silently dropped with no error surfaced to
the caller" / Fail: "the workaround stops working"
[PAIR REQUIRED] Severity: Pass: "HIGH -- events silently dropped with no audit
trail, creating a compliance gap" / Fail: "HIGH" asserted without specifying the
data-integrity or compliance exposure.

Trigger and Impact are separate columns -- do not merge into a single cell.

### Section 6: Long-Term Risk of Staying

One paragraph. What happens over the next 6-12 months for teams that keep the
workaround? Name at least one compounding cost or accumulating risk with a time horizon.
[PAIR REQUIRED] Pass: "within 6 months, the custom script will need re-porting as
the upstream API changes its response shape, breaking all teams on the workaround
simultaneously" / Fail: "the workaround will become harder to maintain over time"

### Section 7: Steelman and Rebuttal -- Anchored Rebuttal Protocol

Apply the Anchored Rebuttal Protocol -- three steps in sequence, do not merge:

1. Write the strongest case for staying. Label it: **STEELMAN**
   [PAIR REQUIRED] Pass: steelman names the specific friction point a real senior
   engineer would resist -- a concrete cost, risk, or incompatibility. /
   Fail: "simplicity is valuable" (a general principle, not a claim a real skeptic
   stakes credibility on).

2. Extract the single strongest specific claim. One declarative sentence.
   Label it: **NAMED CLAIM: "[exact text]"**

3. Rebut only that named claim. State specifically why it fails.
   [PAIR REQUIRED] Pass: rebuttal names what is wrong with the specific claim's
   logic or premise, traceable to the claim's content. /
   Fail: "while simplicity matters, the feature offers..." without addressing the
   claim's specific assertion.

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## V-03 -- Axis: C-23 via Explicit Constraint Instruction (Role-Instruction Base)

**Hypothesis**: The adversarial role-instruction base (R6 V-03) fails C-23 because its
synthesis manifest names sections by function ("Workaround Profile", "Switching Cost
Profile") without including sub-protocol names. Two changes close the gap: (1) update
the synthesis manifest to include all five sub-protocol names in each entry, (2) add
an explicit constraint instruction: "each sub-protocol name must appear in both this
synthesis manifest and the rendered section heading -- a name present at only one site
fails the constraint." Tests whether naming C-23 as a structural constraint in the
synthesis instructions produces reliable double-declaration.

This is R6 V-03 (adversarial roles, NAMED CLAIM anchor, five sub-protocols in role
instructions) with three additions: (1) synthesis manifest updated to include all five
sub-protocol names, (2) explicit C-23 constraint instruction in the synthesis step,
(3) pass/fail pairs added to remaining requirement sites in role 2 to achieve maximum
density (C-22 upgrade from R6 V-03's partial coverage).

```
Auto-detect the feature from repo context. Do not prompt unless context is absent.

Run two sequential roles. Do not merge their output.

---

### ROLE 1: Inertia Advocate

You are a senior engineer who has used the current workaround for over a year.
You believe it is good enough. Your job is to describe and defend it.

1. **Describe the workaround -- Replication Fidelity Standard.** Name the
   workaround. Apply all three sub-requirements independently:
   a. Product names, not categories.
      Pass: "GitHub Actions" / Fail: "CI system"
      Pass: "Confluence page" / Fail: "doc"
      Pass: "custom Python script via Makefile" / Fail: "script"
   b. Major steps in numbered sequence.
      Pass: "1. engineer opens template, 2. copies to project page, 3. edits
      four fields, 4. pings #approvals" / Fail: "team follows the standard process"
   c. Institutional knowledge flagged: any step requiring tribal context,
      undocumented conventions, or shared credentials a new team member lacks.
      Pass: "step 4 requires posting in #approvals with a specific prefix -- not
      in onboarding docs" / Fail: [omitting the undocumented step]
   Enough detail that another team with no prior context could reproduce the workflow.

2. **Make the case for staying.** Why is the workaround acceptable? Name real
   friction points and switching costs.

3. **State your STRONGEST CLAIM.** Write the single argument a skeptical engineer
   would stake their credibility on -- one complete declarative sentence.
   Label it: **STRONGEST CLAIM: [exact text of claim]**

4. **Identify the scenarios where the workaround holds.** What team sizes, project
   types, or usage patterns does it serve correctly?

Output labeled: `WORKAROUND PROFILE (Advocate)`

---

### ROLE 2: Inertia Analyst

You have read the Advocate's Workaround Profile. Produce the full inertia assessment.

1. **Assign the threat score.** Inertia threat is HIGH by default. Only downgrade
   with written justification. State the score explicitly.
   Pass: explicit "HIGH" label present. / Fail: narrative language without the
   explicit token.

2. **Apply the Switching Cost Protocol.** Three independently quantified dimensions
   -- each must be a numeric estimate, not an adjective:
   - Time: hours or days per project or team.
     Pass: "2-4 hours per project for config migration" / Fail: "moderate effort"
   - Training: days, people affected, ramp friction.
     Pass: "1-2 days for 3-4 engineers covering X and Y" / Fail: "some training required"
   - Disruption: coordination overhead, dependencies changed -- name specific
     systems or teams affected.
     Pass: "CI pipeline paused for 4-hour migration window, coordinated with ops" /
     Fail: "team disruption expected"

3. **Apply the Failure Mode Standard.** What goes wrong if teams stay?
   Before writing the table, write this line:
   Required columns for this table: # | Failure Mode | Trigger | Impact | Severity

   | # | Failure Mode | Trigger | Impact | Severity |
   |---|-------------|---------|--------|---------|
   | 1 | [specific failure] | [what triggers it] | [what happens to team] | HIGH |
   | 2 | [specific failure] | [what triggers it] | [what happens to team] | MED |

   Trigger: Pass: "when queue depth exceeds 500 messages" / Fail: "under heavy load"
   Impact: Pass: "events silently dropped with no error surfaced to the caller" /
   Fail: "the workaround stops working"
   Severity: Pass: "HIGH -- events silently dropped with no audit trail" /
   Fail: "HIGH" without specifying the data-integrity or compliance exposure.
   Minimum 2 rows. Trigger and Impact are separate columns.

4. **Apply the Loss Condition Standard.** When does inertia lose?
   Before writing the table, write this line:
   Required columns for this table: # | Condition | Observable Threshold | Verification Command

   | # | Condition | Observable Threshold | Verification Command |
   |---|-----------|---------------------|---------------------|
   | 1 | [scenario] | [measurable trigger] | [Tool: Action -> Result] |
   | 2 | [scenario] | [measurable trigger] | [Tool: Action -> Result] |

   Observable Threshold: Pass: "active project count >= 4" / Fail: "when teams get busy"
   Verification Command: `[Tool or artifact]: [action] -> [result when threshold applies]`
   Pass: "Jira: open active sprint -> count rows Status=Active -> if >= 4, applies"
   Pass: "GitHub: run `gh pr list --state open | wc -l` -> if >= 10, threshold met"
   Fail: "you can check" without naming a specific tool and concrete action.

5. **Long-term risk.** What accumulates over 6-12 months for teams that stay? Name
   a specific compounding cost or divergence risk with a time horizon.
   Pass: "within 6 months, the custom script will need re-porting as the upstream
   API changes its response shape" / Fail: "the workaround will become harder to maintain"

6. **Apply the Anchored Rebuttal Protocol.** Execute in order -- do not compress:
   a. Copy the STRONGEST CLAIM from the Advocate's Workaround Profile word-for-word.
      Label it: `NAMED CLAIM: "[exact text]"`
   b. Rebut only that claim. One paragraph. Explain specifically why it fails --
      with evidence or reasoning tied to the claim's content.
      Pass: rebuttal names the specific weakness in the claim's logic or premise. /
      Fail: redirect to general feature benefits without addressing the claim.
   c. Constraint: the rebuttal must be traceable to the named claim. Do not address
      a weaker point.

Output labeled: `ANALYST VERDICT`

---

Synthesize both outputs into the final artifact. The artifact must contain the
following sections -- each heading must match the name in this list exactly:

- Workaround Description -- Replication Fidelity Standard
- Switching Cost Profile -- Switching Cost Protocol
- Inertia Threat Score
- Workaround Failure Modes -- Failure Mode Standard
- Why Inertia Loses -- Loss Condition Standard
- Long-Term Risk
- Anchored Rebuttal -- Anchored Rebuttal Protocol

Structural constraint: each sub-protocol name (Replication Fidelity Standard,
Switching Cost Protocol, Failure Mode Standard, Loss Condition Standard, Anchored
Rebuttal Protocol) must appear in both this synthesis manifest listing above and
the rendered section heading for that section. A sub-protocol name present at only
one structural site fails this constraint -- correct before writing the artifact.

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## V-04 -- Combined: Explicit C-21+C-22+C-23 Constraints on Phase-Fusion Base

**Hypothesis**: R6 V-04 passes C-21, C-22, and C-23 because the phase-header-as-protocol
pattern satisfies all three properties implicitly. R7 V-04 makes all three properties
explicit constraint sentences rather than implicit consequences of phase structure. A
structural constraint declares that protocol names must match between manifest and phase
headers (C-23). A density constraint declares that every requirement admitting a
predictable violation receives a pass/fail pair at that site (C-22). A count constraint
names all five sub-protocols and states that none may be omitted (C-21). Tests whether
explicit constraint sentences increase adversarial robustness over implicit structural
compliance -- whether the model is harder to destabilize when properties are stated as
rules rather than demonstrated through format.

This is R6 V-04 (phase structure, five named protocols as phase headers, pass/fail
pairs throughout) with three additions: (1) an explicit C-23 structural constraint
before the phase sequence, (2) an explicit C-22 density constraint before the phase
sequence, (3) explicit naming of all five sub-protocols in the structural constraint
block (C-21 enforcement).

```
Auto-detect the feature from repo context. Do not prompt unless context absent.

You are running the inertia analysis. This is the most important analysis in the
Signal system. Every feature decision must answer: **why does inertia lose?**
If you cannot answer it, stop.

This output must contain the following sections -- sub-protocol names are listed
here and must also appear as phase headings:
- Phase 1: Workaround Map -- Replication Fidelity Standard
- Phase 2: Switching Cost -- Switching Cost Protocol
- Phase 3: Failure Mode Table -- Failure Mode Standard
- Phase 4A: Why Inertia Loses -- Loss Condition Standard
- Phase 4B: Steelman and Anchored Rebuttal -- Anchored Rebuttal Protocol
- Phase 4C: Long-Term Risk

Structural constraint: the five sub-protocol names (Replication Fidelity Standard,
Switching Cost Protocol, Failure Mode Standard, Loss Condition Standard, Anchored
Rebuttal Protocol) appear in the section listing above and must appear again in each
corresponding phase heading. A sub-protocol name absent from either site is a
structural error.

Density constraint: every requirement statement that admits a predictable violation
-- tool naming, step enumeration format, quantification, threshold specificity,
verification command format, steelman quality -- receives a pass/fail pair directly
at that requirement site. An unpaired violation-admitting requirement is a density
gap.

Work through phases in order. Do not compress phases together.

---

### PHASE 1: MAP THE WORKAROUND -- Replication Fidelity Standard

What are teams actually doing today instead of using this feature?

Apply the Replication Fidelity Standard -- three independently required properties:

1. Tool names: product-level, not category-level.
   Pass: "GitHub Actions" / Fail: "CI system"
   Pass: "custom Python script invoked by a Makefile target" / Fail: "automation script"
2. Steps: enumerated in numbered sequence.
   Pass: "1. engineer runs script, 2. manually edits YAML, 3. commits and pushes" /
   Fail: "team follows the deployment process"
3. Institutional knowledge: flagged explicitly.
   Pass: "step 3 requires posting in #deploy with a specific prefix -- not in
   onboarding docs" / Fail: [omitting an undocumented step]

Minimum: one named workaround, all three sub-requirements satisfied independently.

---

### PHASE 2: COST THE SWITCH -- Switching Cost Protocol

What would it cost a team to abandon the workaround and adopt the feature?

Apply the Switching Cost Protocol -- three independently quantified dimensions:

- **Time**: hours or days of migration work per project or per team.
  Pass: "2-4 hours per project for config migration" / Fail: "moderate effort"
- **Training**: days of learning, number of people affected, ramp-up friction.
  Pass: "1-2 days for 3-4 engineers, covering API changes and new config format" /
  Fail: "some training required"
- **Disruption**: workflow interruption, coordination overhead, dependencies changed.
  Pass: "CI pipeline paused for 4-hour migration window, coordinated with ops team" /
  Fail: "team disruption expected"

Threat score: **HIGH**. Required. Do not omit. Downgrade only with written
justification including evidence. Omitting = analysis failure.
Pass: explicit "HIGH" token present. / Fail: narrative language ("elevated concern")
substituted for the explicit token.

---

### PHASE 3: BREAK THE WORKAROUND -- Failure Mode Standard

Where does the workaround fail if teams stay on it?

Apply the Failure Mode Standard -- two independently required properties per row:

- Trigger: the specific observable event or threshold that causes failure.
  Pass: "when queue depth exceeds 500 messages" / Fail: "under heavy load"
- Impact: what happens to the team when failure occurs.
  Pass: "events silently dropped with no error surfaced to the caller" /
  Fail: "the workaround stops working"
- Severity: Pass: "HIGH -- events silently dropped with no audit trail, constituting
  a compliance gap" / Fail: "HIGH" asserted without naming the data-integrity or
  compliance exposure.

Required columns for this table: # | Failure Mode | Trigger | Impact | Severity

| # | Failure Mode | Trigger | Impact | Severity |
|---|-------------|---------|--------|---------|
| 1 | [specific failure] | [what triggers it] | [what happens to the team] | HIGH |
| 2 | [specific failure] | [what triggers it] | [what happens to the team] | MED |

Minimum 2 rows. Trigger and Impact are separate columns -- do not merge.
Severity: HIGH = data loss or compliance risk; MED = incorrect results; LOW = inefficiency.

---

### PHASE 4: ANSWER THE QUESTION

**Part A -- Why Inertia Loses -- Loss Condition Standard**

Apply the Loss Condition Standard -- two independently required properties per row:

- Observable Threshold: measurable enough that a team can check it.
  Pass: "active project count >= 4" / Fail: "when teams get busy"
- Verification Command: names specific tool, concrete action, result when
  threshold applies.
  Pass: "Jira: open sprint board -> count Status=Active rows -> if >= 4, applies" /
  Fail: "you can check project count"
  Pass: "GitHub: run `gh pr list --state open | wc -l` -> if >= 10, threshold met" /
  Fail: "review your sprint board"

Required columns for this table: # | Condition | Observable Threshold | Verification Command

| # | Condition | Observable Threshold | Verification Command |
|---|-----------|---------------------|---------------------|
| 1 | [scenario] | [measurable trigger] | [Tool: Action -> Result] |
| 2 | [scenario] | [measurable trigger] | [Tool: Action -> Result] |

**Part B -- Steelman and Anchored Rebuttal -- Anchored Rebuttal Protocol**

Apply the Anchored Rebuttal Protocol -- three steps in sequence, do not merge:

1. Write the strongest argument for staying on the workaround.
   Label it: **STEELMAN**
   Pass: names a specific friction, cost, or risk a real skeptic would actually cite. /
   Fail: "simplicity is valuable" (a principle, not a claim a real skeptic stakes
   credibility on).
2. Extract the single strongest specific claim. One declarative sentence.
   Label it: **NAMED CLAIM: "[exact text]"**
3. Rebut only that named claim. State specifically why it fails.
   Pass: rebuttal names the specific weakness in the claim's premise and ties the
   counter-argument to the claim's content. /
   Fail: "while simplicity matters, the feature offers..." without addressing the
   claim's specific assertion.

**Part C -- Long-Term Risk**

What accumulates over 6-12 months for teams that stay? Name a specific compounding
cost or divergence risk with a time horizon.
Pass: "within 6 months, the custom script will need re-porting as the upstream API
changes its response shape" / Fail: "the workaround will become harder to maintain"

---

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## V-05 -- Combined: Pre-Flight Verification Gate (All Axes)

**Hypothesis**: R6 V-05 passes C-21, C-22, and C-23 because the scaffold provides
strong implicit structural support. The failure mode is adversarial: a model under
context pressure might omit a sub-protocol name from one site, skip a pair at a
difficult requirement, or compress the Anchored Rebuttal Protocol. R7 V-05 adds a
mandatory pre-flight verification step between content generation and artifact writing.
The model must check and confirm each property explicitly before writing -- C-21 is
verified by counting sub-protocols, C-23 is verified by cross-checking manifest against
section headings, C-22 is verified by scanning for unpaired violation-admitting
requirements. This converts the three new criteria from properties-to-achieve to
properties-to-verify, creating a double-pass structure where detection failures require
two independent omissions.

This is R6 V-05 (full scaffold: Competitor Zero framing, advocate/analyst roles,
Replication Fidelity Standard, NAMED CLAIM anchor, per-table column manifests, section
heading manifest, pass/fail pairs at all requirements) with one addition: a mandatory
STEP 3 pre-flight verification block between the analyst pass and the artifact write.

```
Auto-detect the feature from repo context. Do not prompt unless context absent.

## Inertia Analysis -- Competitor Zero

The primary competitor is not another product. It is the option to do nothing and
keep the current workaround. This analysis must answer one question: **why does
inertia lose?** If you cannot answer it, stop.

This output must contain the following sections -- sub-protocol names are listed
here and must match section headings exactly:
- WORKAROUND PROFILE (Advocate)
- A. Switching Cost Table -- Switching Cost Protocol
- B. Threat Score
- C. Workaround Failure Mode Table -- Failure Mode Standard
- D. Why Inertia Loses -- Loss Condition Standard
- E. Long-Term Risk of Staying
- F. Anchored Rebuttal -- Anchored Rebuttal Protocol

---

### STEP 1 -- ADVOCATE PASS

Take the role of a team member who has used the current workaround for 12+ months
and finds it acceptable.

**Workaround Profile -- Replication Fidelity Standard**

Describe the workaround so that another team with no prior context could reproduce
it independently. Apply all three sub-requirements:

1. Name each tool by product, not by category.
   Pass: "GitHub Actions" / Fail: "CI system"
   Pass: "Confluence page" / Fail: "doc"
   Pass: "custom Python script invoked by a Makefile target" / Fail: "automation script"
2. Enumerate the major steps in numbered sequence.
   Pass: "1. engineer opens Confluence template, 2. copies to project page, 3. edits
   four required fields, 4. pings #approvals" /
   Fail: "team follows the standard documentation process"
3. Flag institutional knowledge: any step requiring tribal context, undocumented
   conventions, or shared credentials a new team member would not have.
   Pass: "step 4 requires posting in #approvals with a specific prefix -- documented
   only in the team wiki, not in company onboarding" /
   Fail: [omitting the undocumented step or treating it as common knowledge]

State why the workaround is good enough: what it handles correctly, for which team
sizes and usage patterns.

**Strongest Objection to Switching**

Write the single strongest argument for staying on the workaround -- the one a
skeptical senior engineer would stake their credibility on. One complete declarative
sentence.
Pass: names a specific friction, cost, or incompatibility a real skeptic would cite. /
Fail: "simplicity is valuable" (a principle, not a concrete claim)
Label it: **STRONGEST CLAIM: [exact text of claim]**

Label this section: `WORKAROUND PROFILE (Advocate)`

---

### STEP 2 -- ANALYST PASS

You have read the Advocate Pass. Produce the full inertia assessment.

**A. Switching Cost Table -- Switching Cost Protocol**

Three independently quantified dimensions. Apply the Switching Cost Protocol:
Pass: "2-4 hours per project for config migration" / Fail: "moderate effort"
Pass: "1-2 days for 3-4 engineers" / Fail: "some training required"
Pass: "CI pipeline paused for 4-hour window, coordinated with ops" /
Fail: "team disruption"

| Dimension | Estimate | What Drives This |
|-----------|----------|-----------------|
| Time | [X hours/days per project] | [migration steps] |
| Training | [X days, Y people] | [what must be learned] |
| Disruption | [coordination impact] | [who and what changes] |

All three rows required. Numeric or range-based estimates required.

**B. Threat Score**

```
Inertia Threat: HIGH
```

Required. Downgrade below HIGH only with written justification and supporting
evidence. Omitting this field = analysis failure.
Pass: explicit "HIGH" token present. / Fail: narrative language substituted for
the explicit token.

**C. Workaround Failure Mode Table -- Failure Mode Standard**

Failure modes = what goes wrong if teams stay. Distinct from switching costs.
Apply the Failure Mode Standard -- two independently required properties per row:

Trigger: Pass: "when queue depth exceeds 500 messages" / Fail: "under heavy load"
Impact: Pass: "events silently dropped with no error surfaced to the caller" /
Fail: "the workaround stops working correctly"
Severity: Pass: "HIGH -- events silently dropped with no audit trail" /
Fail: "HIGH" without specifying data-integrity or compliance exposure.

Required columns for this table: # | Failure Mode | Trigger | Impact | Severity

| # | Failure Mode | Trigger | Impact | Severity |
|---|-------------|---------|--------|---------|
| 1 | [specific failure] | [edge case or threshold] | [what happens, to whom] | HIGH |
| 2 | [specific failure] | [edge case or threshold] | [what happens, to whom] | MED |
| + | ... | | | |

Minimum 2 rows. Trigger and Impact are separate columns -- do not merge.
Severity: HIGH = data loss or compliance risk; MED = incorrect results; LOW = inefficiency.
"Does not scale" without a named scale limit does not pass.

**D. Why Inertia Loses -- Loss Condition Standard**

Apply the Loss Condition Standard -- two independently required properties per row:
Observable Threshold: Pass: "active project count >= 4" / Fail: "when teams get busy"
Verification Command:
Pass: "Jira: open active sprint -> count Status=Active rows -> if >= 4, applies"
Pass: "GitHub: run `gh pr list --state open | wc -l` -> if >= 10, threshold met"
Fail: "you can check project count" / Fail: "review your sprint board"

Required columns for this table: # | Condition | Observable Threshold | Verification Command

| # | Condition | Observable Threshold | Verification Command |
|---|-----------|---------------------|---------------------|
| 1 | [specific scenario] | [measurable trigger] | [see format] |
| 2 | [specific scenario] | [measurable trigger] | [see format] |

Minimum 2 rows. Each condition must be falsifiable. The Verification Command must
name a specific tool and concrete action without requiring a follow-up question.

**E. Long-Term Risk of Staying**

One paragraph. What accumulates over 6-12 months? Name a specific compounding cost,
growing debt, or divergence risk with a time horizon.
Pass: "within 6 months, the custom script will need re-porting as the upstream API
changes its response shape, breaking all teams on the workaround simultaneously" /
Fail: "the workaround will become harder to maintain over time"

**F. Anchored Rebuttal -- Anchored Rebuttal Protocol**

Apply the Anchored Rebuttal Protocol -- three steps in sequence, do not merge:

1. Copy the STRONGEST CLAIM from the Advocate Pass word-for-word.
   Label it: `NAMED CLAIM: "[exact text from Advocate Pass]"`

2. Rebut only that named claim. One paragraph. State specifically why it fails --
   with evidence or reasoning tied to the claim's content.
   Pass: rebuttal names the specific weakness in the claim's premise and ties the
   counter-argument to the claim's content. /
   Fail: "while simplicity is valuable, the feature offers..." without addressing
   the claim's specific assertion.

3. Constraint: do not redirect to a different benefit. The rebuttal must be
   traceable to the named claim.

---

### STEP 3 -- PRE-FLIGHT VERIFICATION

Before writing the artifact, verify these three properties. State each check
explicitly with PASS or FAIL.

**Check 1 -- C-21 (All Sub-Protocols Named):**
The five required sub-protocols are: Replication Fidelity Standard, Switching Cost
Protocol, Failure Mode Standard, Loss Condition Standard, Anchored Rebuttal Protocol.
State: "C-21 check: [count] of 5 sub-protocols present -- [PASS] or [FAIL: list
any missing names]"

**Check 2 -- C-23 (Double-Declaration):**
Each sub-protocol name must appear in (a) the heading manifest at the top of this
prompt and (b) the corresponding section heading in the output. For each protocol:
State: "C-23 check: [protocol name] -- manifest: [yes/no], section heading: [yes/no]"
If any protocol is absent from either site, add it before writing the artifact.

**Check 3 -- C-22 (Maximum Pair Density):**
Scan Sections A, C, D, E, and F for any requirement statement that admits a
predictable violation but does not have a pass/fail pair at that site. If any
found, add the missing pair. State: "C-22 check: [N] sites verified with pairs,
[N] pairs added / none needed"

If any check produces FAIL or identifies a gap, correct the output before
writing the artifact.

---

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## Predicted R7 Scores (rubric v7)

**Rubric v7 formula**: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/15 * 10)`

PARTIAL counts as 0.5.

### New criteria compliance by variation

| Variation | C-21 mechanism | C-21 | C-22 mechanism | C-22 | C-23 mechanism | C-23 |
|-----------|---------------|------|----------------|------|----------------|------|
| V-01 | All 5 sub-protocol names in manifest + section headers | PASS | Pairs at every requirement site including trigger/impact/severity/threshold/verification/steelman | PASS | Protocol names in heading manifest AND section headers | PASS |
| V-02 | All 5 sub-protocol names in manifest + section headers | PASS | [PAIR REQUIRED] annotation at every violation-admitting site | PASS | Protocol names in manifest + "Section N:" prefixed headers | PASS |
| V-03 | All 5 sub-protocols in role instructions + synthesis manifest | PASS | Pairs at all role 2 requirement sites (full coverage) | PASS | Synthesis manifest names protocols + explicit C-23 constraint instruction | PASS |
| V-04 | Explicit structural constraint names all 5 protocols | PASS | Explicit density constraint + pairs at every phase requirement | PASS | Structural constraint requires manifest/header match + phase headers include protocol names | PASS |
| V-05 | Pre-flight Check 1 counts and verifies all 5 | PASS | Pre-flight Check 3 scans and repairs any missing pairs | PASS | Pre-flight Check 2 cross-verifies manifest vs. section headings per protocol | PASS |

### Also fixing R6 C-12 gaps in V-01 and V-02

| Variation | C-12 mechanism | C-12 prediction |
|-----------|---------------|-----------------|
| V-01 | Section 7 header "Steelman and Rebuttal -- Anchored Rebuttal Protocol" + three-step sequence with explicit NAMED CLAIM label | PASS |
| V-02 | Section 7 header "Steelman and Rebuttal -- Anchored Rebuttal Protocol" + three-step sequence with explicit NAMED CLAIM label | PASS |
| V-03 | Unchanged from R6 -- Anchored Rebuttal Protocol in Role 2 Step 6, word-for-word copy enforced | PASS |
| V-04 | Unchanged from R6 -- Phase 4B header and three-step NAMED CLAIM sequence | PASS |
| V-05 | Unchanged from R6 -- Section F heading manifest + three-step NAMED CLAIM sequence in analyst pass | PASS |

### Full score predictions

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Essential | PASS | PASS | PASS | PASS | PASS |
| C-02 Essential | PASS | PASS | PASS | PASS | PASS |
| C-03 Essential | PASS | PASS | PASS | PASS | PASS |
| C-04 Essential | PASS | PASS | PASS | PASS | PASS |
| C-05 Essential | PASS | PASS | PASS | PASS | PASS |
| C-06 Recommended | PASS | PASS | PASS | PASS | PASS |
| C-07 Recommended | PASS | PASS | PASS | PASS | PASS |
| C-08 Recommended | PASS | PASS | PASS | PASS | PASS |
| C-09 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-10 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-11 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-12 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-13 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-14 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-15 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-16 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-17 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-18 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-19 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-20 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-21 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-22 Aspirational | PASS | PASS | PASS | PASS | PASS |
| C-23 Aspirational | PASS | PASS | PASS | PASS | PASS |
| **Predicted total** | **100.0** | **100.0** | **100.0** | **100.0** | **100.0** |

### Reliability Gradient Analysis

All 5 variations predicted at 100. Adversarial robustness is the differentiator:

| Variation | C-21 robustness | C-22 robustness | C-23 robustness | C-12 robustness | Overall |
|-----------|----------------|----------------|----------------|----------------|---------|
| V-01 | Protocol names in manifest + headers; omission detectable at 2 sites | Pairs at every site -- omission leaves a structural gap; no per-site annotation to flag it | Two structural sites without explicit constraint; relies on consistent naming | Named 3-step Anchored Rebuttal Protocol; NAMED CLAIM label enforced | Lowest -- compliance structural but not explicitly constrained |
| V-02 | Same as V-01 | [PAIR REQUIRED] annotation at every site -- omission creates an orphaned annotation | Same 2-site structure as V-01 | Same as V-01 | Higher on C-22 axis -- per-site annotation flags omissions |
| V-03 | 5 protocols in role instructions + synthesis manifest; explicit C-23 constraint names the requirement | Pairs at all role 2 sites -- full coverage via role instructions | Explicit constraint instruction + synthesis manifest match requirement | Role 2 Step 6 enforces word-for-word copy | Higher on C-23 axis -- explicit constraint instruction |
| V-04 | Explicit structural constraint names all 5 protocols | Explicit density constraint sentence + per-phase pairs | Structural constraint requires match; phase headers fuse protocol name and boundary | Phase 4B enforces NAMED CLAIM sequence | High -- two explicit constraint sentences |
| V-05 | Pre-flight Check 1 counts all 5 and flags missing | Pre-flight Check 3 scans and forces repair before artifact write | Pre-flight Check 2 cross-verifies manifest vs headers per protocol | Analyst pass enforces word-for-word copy; pre-flight does not specifically check C-12 | Highest -- mandatory repair loop before artifact write |

**R7 design conclusion**: All five variations close the R6 gaps (C-12, C-21, C-22, C-23).
The reliability gradient now tracks enforcement mechanism rather than criterion presence:
structural naming (V-01/V-02), explicit constraint (V-03/V-04), verified repair loop (V-05).
V-05's pre-flight gate is qualitatively different -- it converts "did the model comply?"
from an evaluation question to an in-prompt check with mandatory remediation.

**Cross-variation insights**:
- C-22 and C-21 co-reinforce: naming all 5 sub-protocols (C-21) creates numbered
  sub-requirements that are natural C-22 anchor sites. V-04 and V-05 demonstrate this
  co-occurrence at maximum density.
- C-23 changes the verification topology: with double-declaration, any omission creates
  an observable mismatch at one of two sites, not just absence at one. V-05's pre-flight
  Check 2 explicitly tests this by cross-checking both sites independently.
- The pre-flight gate (V-05) is the first variation where the model is instructed to
  self-correct before writing -- not just produce correctly from the start. This creates
  a repair path for adversarial or context-pressure failures that no prior variation had.
