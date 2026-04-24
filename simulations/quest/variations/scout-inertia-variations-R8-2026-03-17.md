Now I have all I need. R7 achieved all-5 at 100.0 on v7 (15 criteria). Rubric v8 adds C-24/C-25/C-26 (denominator 15 → 18). Let me design R8 to close the three new gaps.

**R8 design analysis:**
- C-24 (verbatim quotation): R7 V-01/V-02 already added `NAMED CLAIM: "[exact text]"` from the C-12 fix; V-03/V-04/V-05 had it earlier. C-24 may already be passing but paraphrase risk remains without an explicit "no paraphrase" mandate.
- C-25 (per-site enforcement annotations): Only V-02 had `[PAIR REQUIRED]` at individual sites; V-01/V-03 had structural pairs without annotations; V-04/V-05 used density constraints and pre-flight checks — each different from per-site annotation.
- C-26 (verbatim manifest-header alignment): R7 V-01 used numbered prefix ("1. Workaround...") in headers but not manifest — diverges. V-02 used "Section N:" prefix at both sites — closest to C-26 pass. V-03 had synthesis-manifest constraint but no verbatim-identity enforcement.

**Predicted R7 performance under v8 (retroactive):**
- V-01: C-24 PASS, C-25 FAIL (structural pairs, no site annotations), C-26 FAIL (numbered prefix mismatch) → ~83/100
- V-02: C-24 PASS, C-25 PASS ([PAIR REQUIRED] present), C-26 PASS (Section N: consistent) → 100/100
- V-03: C-24 PASS, C-25 PARTIAL (role 2 pairs without annotations in synthesis), C-26 PARTIAL → ~90/100
- V-04: C-24 PASS, C-25 PASS (density constraint), C-26 PASS → 100/100
- V-05: C-24 PASS, C-25 PASS (pre-flight scan), C-26 PASS (pre-flight cross-check) → 100/100

Design goal for R8: all five at 100/100 on v8. Three gaps to close for V-01 (C-25+C-26) and V-03 (C-25+C-26). V-02/V-04/V-05 already pass retroactively.

---

# scout-inertia — Prompt Variations R8

## Context

R7 results: All 5 variations at 100.0/100 on rubric v7 (15 criteria). Rubric v8 raises denominator to 18 via three new aspirational criteria:

- **C-24**: Exact-text quotation at claim-reference steps — `NAMED CLAIM: "[exact text]"` must quote verbatim from the steelman above, not paraphrase. R7 V-01/V-02 added the NAMED CLAIM scaffold; none enforced verbatim-not-paraphrase. All five carry some risk.
- **C-25**: Enforcement annotations at every structural-requirement site — `[PAIR REQUIRED]` at each individual site, not just global density. R7 V-02 has the pattern; V-01/V-03 have structural pairs without annotations; V-04/V-05 use constraint-sentences and pre-flight gates respectively.
- **C-26**: Manifest-to-header verbatim alignment — manifest entry text and section header text must be character-for-character identical. R7 V-02 uses "Section N:" consistently at both sites (closest to PASS); V-01 uses numbered prefix in headers only (FAIL); V-03 names protocols in synthesis manifest but header format diverges.

Predicted R7 retroactive under v8: V-02 100/100, V-04 100/100, V-05 100/100. V-01 ~83 (C-25 FAIL, C-26 FAIL). V-03 ~90 (C-25 PARTIAL, C-26 PARTIAL).

**Design goal for R8**: All 5 at 100/100 on v8. Primary gaps: V-01 needs C-25 site annotations + C-26 verbatim enforcement; V-03 needs same at synthesis step. Secondary: reinforce C-24 with explicit "do not paraphrase — quote verbatim" instruction in all five.

**Design axes** (single-axis for V-01/V-02/V-03, combined for V-04/V-05):
- Phrasing register: formal/imperative vs conversational
- Output format: annotated-template vs prose-instruction
- Inertia framing: adversarial-prominent vs structural-neutral
- Lifecycle emphasis: phase-boundary-explicit vs section-continuous
- Role sequence: single-role vs multi-role vs verification-gate

## Variation Map

| ID | Axis | Hypothesis |
|----|------|------------|
| V-01 | Single-axis phrasing register: formal/imperative, all-imperative verbs, C-25 site annotations added, C-26 verbatim-identity instruction added | Formal imperative register with explicit "do not paraphrase" at NAMED CLAIM, [PAIR REQUIRED] at every site, and verbatim identity constraint closes C-24/C-25/C-26 on the simplest single-role base with minimum structural change |
| V-02 | Single-axis output format: pre-printed annotated template, verbatim-aligned manifest block, [PAIR REQUIRED] at every remaining gap site | R7 V-02 already passed C-24/C-25/C-26 retroactively — R8 tightens the pattern: strip the "Section N:" divergence source by making manifest entries and headers exact copies, add verbatim-alignment instruction, add "do not paraphrase" at NAMED CLAIM. Tests whether V-02's annotation-density advantage holds with tighter C-26 enforcement |
| V-03 | Single-axis inertia framing: COMPETITOR ZERO adversarial frame prominent, C-25 annotations added to synthesis step, C-26 explicit verbatim constraint at synthesis | The adversarial role base (R7 V-03) gains C-25/C-26 via constraint instruction at the synthesis step: "each synthesis header is a verbatim copy of its manifest entry — no reformatting." Tests whether constraint-sentence at synthesis is sufficient for C-26 reliability |
| V-04 | Combined role sequence + lifecycle emphasis: three-phase lifecycle (PROFILE / THREAT / VERDICT), explicit constraint sentences for C-24/C-25/C-26 co-located at phase boundary | Three explicit constraint sentences — one per new criterion — placed at the transition to the THREAT phase where they govern the forward pass. Tests whether co-located constraint sentences produce more reliable compliance than distributed instructions |
| V-05 | Combined all axes: full-stack template + pre-flight verification gate with mandatory repair targeting C-24/C-25/C-26 explicitly | R7 V-05 repair-loop gate extended by three new checks: (1) verbatim quotation scan, (2) annotation-site count scan, (3) manifest-header identity scan. Converts all three new criteria from properties-to-achieve to properties-to-verify-and-repair |

---

## V-01 — Axis: Phrasing Register (Formal/Imperative, C-25 Site Annotations, C-26 Verbatim Identity)

**Hypothesis**: The simplest single-role scaffold can satisfy all three new criteria by
adding three targeted instructions to the R7 V-01 base: (1) "Do not paraphrase — quote
the exact text" at the NAMED CLAIM step, (2) `[PAIR REQUIRED]` annotation at every
requirement site that has a pass/fail example, (3) an explicit verbatim-identity
constraint at the manifest: "Section headers must reproduce these entries
character-for-character." All-imperative phrasing throughout. Tests whether formal
register + targeted additions on the simplest base is sufficient for C-24/C-25/C-26.

This is R7 V-01 (Competitor Zero framing, single role, Replication Fidelity Standard)
with four additions: (1) "do not paraphrase — quote verbatim" at NAMED CLAIM step,
(2) `[PAIR REQUIRED]` annotation at every requirement site not already annotated,
(3) verbatim-identity instruction at the manifest, (4) manifest entries and section
headers normalized to identical text (no numbered prefix in one and not the other).

```
Auto-detect the feature from repo context. Do not prompt unless context is absent.

## Competitor Zero: Status Quo / Do Nothing

Treat the option to keep the current workaround as a named competitor: Competitor Zero.
Profile it completely before analyzing any named competitor.

This output must contain the following sections. Section headers must reproduce
these manifest entries character-for-character -- no reformatting, no prefix changes:

- Workaround Description -- Replication Fidelity Standard
- Switching Cost Profile -- Switching Cost Protocol
- Inertia Threat Score
- Why Inertia Loses -- Loss Condition Standard
- Workaround Failure Modes -- Failure Mode Standard
- Forward-Looking Risk
- Steelman and Rebuttal -- Anchored Rebuttal Protocol

**Workaround Description -- Replication Fidelity Standard**

Describe the current workaround so another team with no prior context could reproduce
it independently. Apply all three sub-requirements of the Replication Fidelity Standard:

1. Name each tool by product, not by category.
   [PAIR REQUIRED] Pass: "GitHub Actions" / Fail: "CI system"
   [PAIR REQUIRED] Pass: "custom Python script invoked by a Makefile target" / Fail: "automation script"
2. Enumerate the major steps in numbered sequence.
   [PAIR REQUIRED] Pass: "1. Engineer opens Confluence template, 2. copies to project page, 3. edits four required fields, 4. pings #approvals in Slack" / Fail: "team follows the standard documentation process"
3. Flag institutional knowledge: any step requiring tribal context, undocumented conventions, or shared credentials a new team member would not have.
   [PAIR REQUIRED] Pass: "step 4 requires posting in #approvals with a specific prefix -- not in onboarding docs" / Fail: [omitting a step that depends on undocumented knowledge]

Name the workaround. Write one paragraph minimum.

**Switching Cost Profile -- Switching Cost Protocol**

Apply the Switching Cost Protocol. Produce three line items, each with a numeric
estimate or explicit N/A with written justification:

- Time: hours or days to migrate existing setups, per project or per team.
  [PAIR REQUIRED] Pass: "2-4 hours per project for YAML migration" / Fail: "moderate effort"
- Training: days of onboarding, number of people affected, ramp-up friction sources.
  [PAIR REQUIRED] Pass: "1-2 days for 3-4 engineers covering API changes and new config format" / Fail: "some training required"
- Disruption: coordination overhead, workflow interruptions, dependencies that must change.
  [PAIR REQUIRED] Pass: "CI pipeline paused for 4-hour migration window, coordinated with ops team" / Fail: "team disruption expected"

**Inertia Threat Score**

Assign: HIGH (default and required). Downgrade below HIGH only with written
justification citing specific evidence.
[PAIR REQUIRED] Pass: explicit "HIGH" label present. / Fail: narrative language ("elevated concern", "real risk") substituted for the explicit severity token, or score omitted entirely.

**Why Inertia Loses -- Loss Condition Standard**

Apply the Loss Condition Standard. Identify two or more conditions under which the
current workaround is worse than adopting the feature. Each condition must be falsifiable
-- a reader can check whether it applies to their situation.

Required columns: # | Condition | Observable Threshold | Verification Command

| # | Condition | Observable Threshold | Verification Command |
|---|-----------|---------------------|---------------------|
| 1 | [specific condition] | [measurable trigger] | [Tool: Action -> Result when threshold applies] |
| 2 | [specific condition] | [measurable trigger] | [Tool: Action -> Result when threshold applies] |

[PAIR REQUIRED] Observable Threshold: Pass: "active project count >= 4" / Fail: "when teams get busy"
[PAIR REQUIRED] Verification Command: Pass: "Jira: open active sprint board -> count rows where Status = Active. If >= 4, condition applies." / Fail: "review your sprint board"

Verification Command format: `[Tool or artifact]: [what to open or run] -> [what the result looks like when threshold applies]`

**Workaround Failure Modes -- Failure Mode Standard**

Identify modes of failure for the current workaround. Failure modes are distinct from
switching costs: failure modes describe what goes wrong if you stay; switching costs
describe what it costs to leave.

Apply the Failure Mode Standard. Identify two or more failure modes.

Required columns: # | Failure Mode | Trigger | Impact | Severity

| # | Failure Mode | Trigger | Impact | Severity |
|---|-------------|---------|--------|---------|
| 1 | [specific failure] | [what causes it] | [consequence to team] | HIGH |
| 2 | [specific failure] | [what causes it] | [consequence to team] | MED |

[PAIR REQUIRED] Trigger: Pass: "when queue depth exceeds 500 messages" / Fail: "under heavy load"
[PAIR REQUIRED] Impact: Pass: "events silently dropped with no error surfaced to the caller" / Fail: "the workaround stops working"
[PAIR REQUIRED] Severity: Pass: "HIGH -- events silently dropped with no audit trail, creating a compliance gap" / Fail: "HIGH" asserted without naming the data-integrity or compliance exposure.

Trigger and Impact are separate columns. Do not merge into a single cell.
"Does not scale" without a named scale limit does not pass Trigger.

**Forward-Looking Risk**

Write one paragraph. State what happens to teams that stay on the workaround for
the next 6-12 months. Name a specific compounding cost, accumulating technical debt,
or divergence risk with an explicit time horizon.
[PAIR REQUIRED] Pass: "within 6 months, the custom script will need re-porting as the upstream API changes its response shape, breaking all teams on the workaround simultaneously" / Fail: "the workaround will become harder to maintain over time"

**Steelman and Rebuttal -- Anchored Rebuttal Protocol**

Apply the Anchored Rebuttal Protocol. Execute three steps in sequence. Do not merge steps.

Step 1. Write the strongest possible argument a skeptical senior engineer would make
   for keeping the workaround. Label it: **STEELMAN**
   [PAIR REQUIRED] Pass: names the specific friction, cost, or risk a real skeptic would actually cite -- a concrete concern, not a general principle. / Fail: "simplicity is valuable" (a principle, not a claim a real skeptic stakes credibility on).

Step 2. Extract the single strongest specific claim from the steelman. Write it as
   one complete declarative sentence. Do not paraphrase -- quote the exact text.
   Label it: **NAMED CLAIM: "[exact text of the claim, verbatim from Step 1]"**
   [PAIR REQUIRED] Pass: quoted text appears verbatim in the STEELMAN above. / Fail: paraphrased or strengthened version of the claim is substituted.

Step 3. Rebut only the named claim. One paragraph. State specifically why the claim
   fails -- with evidence or reasoning tied to the claim's exact content.
   [PAIR REQUIRED] Pass: rebuttal identifies the specific weakness in the claim's logic or premise, traceable to the quoted claim. / Fail: "while simplicity matters, the feature offers..." without addressing the claim's specific assertion.

---

After profiling Competitor Zero, add:
- Named competitors (3-5): feature overlap, threat level (HIGH/MEDIUM/LOW), one-line differentiation
- The whitespace: what no competitor owns
- Table stakes: what any entrant must match

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## V-02 — Axis: Output Format (Pre-Printed Annotated Template, Verbatim-Aligned Manifest Block)

**Hypothesis**: R7 V-02 already passed C-24/C-25/C-26 retroactively via its "Section N:"
consistent prefix at both manifest and header sites. R8 V-02 tightens the pattern:
(1) adds an explicit verbatim-identity constraint in the manifest block to make C-26
mechanically enforced rather than incidentally satisfied, (2) adds "do not paraphrase
-- quote verbatim from the STEELMAN above" at the NAMED CLAIM step, (3) ensures
[PAIR REQUIRED] is present at every requirement site including the Forward-Looking Risk
paragraph and the NAMED CLAIM quotation fidelity requirement. Tests whether explicitly
constraining what R7 V-02 already did implicitly increases structural reliability
without changing the format.

This is R7 V-02 (schema blocks, [PAIR REQUIRED] at every violation-admitting site,
"Section N:" consistent prefix) with three additions: (1) verbatim-identity instruction
co-located with the manifest block, (2) "do not paraphrase" at NAMED CLAIM step,
(3) [PAIR REQUIRED] at NAMED CLAIM quotation fidelity and at Forward-Looking Risk.

```
Auto-detect the feature from repo context. Do not prompt unless context is absent.

Analyze the inertia competitor -- the option to keep the current workaround instead
of adopting this feature. Answer the central question: **why does inertia lose?**
If you cannot answer that question, stop and flag.

This output must contain the following sections. Each section header must be
character-for-character identical to its manifest entry below -- do not reformat,
do not add prefixes, do not paraphrase:

- Section 1: Workaround Description -- Replication Fidelity Standard
- Section 2: Switching Cost Table -- Switching Cost Protocol
- Section 3: Inertia Threat Score
- Section 4: Why Inertia Loses -- Loss Condition Standard
- Section 5: Workaround Failure Modes -- Failure Mode Standard
- Section 6: Long-Term Risk of Staying
- Section 7: Steelman and Rebuttal -- Anchored Rebuttal Protocol

### Section 1: Workaround Description -- Replication Fidelity Standard

**Replication Fidelity Standard** -- all three sub-requirements must be satisfied independently:

1. Tool names: product-level, not category-level.
   [PAIR REQUIRED] Pass: "GitHub Actions" / Fail: "CI system"
   [PAIR REQUIRED] Pass: "Confluence page" / Fail: "doc"
   [PAIR REQUIRED] Pass: "custom Python script invoked by a Makefile target" / Fail: "automation script"
2. Steps: enumerated in numbered sequence, not summarized prose.
   [PAIR REQUIRED] Pass: "1. Engineer opens Confluence template, 2. copies to project page, 3. edits four required fields, 4. pings #approvals" / Fail: "team follows the standard documentation process"
3. Institutional knowledge: any step requiring tribal context, undocumented conventions, or shared credentials flagged explicitly.
   [PAIR REQUIRED] Pass: "requires access to #approvals Slack channel -- not in onboarding docs" / Fail: [omitting a step that depends on undocumented knowledge]

Name the workaround. Write one paragraph minimum.

### Section 2: Switching Cost Table -- Switching Cost Protocol

Apply the Switching Cost Protocol. All three dimensions required.

| Dimension | Estimate | Basis |
|-----------|----------|-------|
| Time | [X hours/days per project or team] | [what drives this estimate] |
| Training | [X days, Y people] | [what must be learned and by whom] |
| Disruption | [what changes, who is affected] | [coordination cost, named systems] |

[PAIR REQUIRED] Time: Pass: "2-4 hours per project for YAML migration" / Fail: "moderate effort" or "significant time"
[PAIR REQUIRED] Training: Pass: "1-2 days for 3-4 engineers covering API changes and new config format" / Fail: "some training required"
[PAIR REQUIRED] Disruption: Pass: "CI pipeline paused for 4-hour migration window, coordinated with ops team" / Fail: "team disruption expected"

### Section 3: Inertia Threat Score

```
Threat: HIGH
```

Downgrade below HIGH only with written justification and specific evidence.
[PAIR REQUIRED] Pass: explicit "HIGH" label present (with or without qualifier). / Fail: omitting the score, or substituting narrative language ("elevated concern", "real risk") without the explicit severity token.

### Section 4: Why Inertia Loses -- Loss Condition Standard

Apply the Loss Condition Standard. Two or more conditions. Each must be falsifiable --
a reader can verify whether it applies.

> Schema: # | Condition | Observable Threshold | Verification Command

| # | Condition | Observable Threshold | Verification Command |
|---|-----------|---------------------|---------------------|
| 1 | [condition] | [measurable trigger] | [Tool: Action -> Result when threshold applies] |
| 2 | [condition] | [measurable trigger] | [Tool: Action -> Result when threshold applies] |

[PAIR REQUIRED] Observable Threshold: Pass: "active project count >= 4" / Fail: "when teams get busy"
[PAIR REQUIRED] Verification Command: Pass: "Jira: open the active sprint board -> count rows where Status = Active. If >= 4, condition applies." / Fail: "review your sprint board"

Verification Command format: `[Tool or artifact]: [what to open or run] -> [what the result looks like when the threshold applies]`

### Section 5: Workaround Failure Modes -- Failure Mode Standard

Apply the Failure Mode Standard. Distinct from switching costs. Failure modes = what
goes wrong if you stay.

> Schema: # | Failure Mode | Trigger | Impact | Severity

| # | Failure Mode | Trigger | Impact | Severity |
|---|-------------|---------|--------|---------|
| 1 | [specific failure] | [what triggers it] | [consequence to team] | HIGH / MED / LOW |
| 2 | [specific failure] | [what triggers it] | [consequence to team] | HIGH / MED / LOW |

[PAIR REQUIRED] Trigger: Pass: "when queue depth exceeds 500 messages" / Fail: "under heavy load"
[PAIR REQUIRED] Impact: Pass: "events silently dropped with no error surfaced to the caller" / Fail: "the workaround stops working"
[PAIR REQUIRED] Severity: Pass: "HIGH -- events silently dropped with no audit trail, creating a compliance gap" / Fail: "HIGH" asserted without naming the data-integrity or compliance exposure.

Trigger and Impact are separate columns -- do not merge into a single cell.

### Section 6: Long-Term Risk of Staying

One paragraph. What happens over the next 6-12 months for teams that keep the
workaround? Name at least one compounding cost or accumulating risk with an explicit
time horizon.
[PAIR REQUIRED] Pass: "within 6 months, the custom script will need re-porting as the upstream API changes its response shape, breaking all teams on the workaround simultaneously" / Fail: "the workaround will become harder to maintain over time"

### Section 7: Steelman and Rebuttal -- Anchored Rebuttal Protocol

Apply the Anchored Rebuttal Protocol. Three steps in sequence. Do not merge.

Step 1. Write the strongest case for staying on the workaround. Label it: **STEELMAN**
   [PAIR REQUIRED] Pass: steelman names the specific friction point a real senior engineer would resist -- a concrete cost, risk, or incompatibility. / Fail: "simplicity is valuable" (a general principle, not a claim a real skeptic stakes credibility on).

Step 2. Extract the single strongest specific claim. Write it as one complete
   declarative sentence. Quote the exact text -- do not paraphrase or rephrase.
   Label it: **NAMED CLAIM: "[exact text, verbatim from STEELMAN above]"**
   [PAIR REQUIRED] Pass: the quoted text appears verbatim in the STEELMAN. / Fail: the text has been paraphrased, condensed, or reworded from what appears in Step 1.

Step 3. Rebut only the named claim. One paragraph. State why the claim fails --
   traceable to the claim's exact content.
   [PAIR REQUIRED] Pass: rebuttal names what is wrong with the specific claim's logic or premise, traceable to the quoted claim text. / Fail: "while simplicity matters, the feature offers..." without addressing the claim's specific assertion.

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## V-03 — Axis: Inertia Framing (COMPETITOR ZERO Adversarial Frame, C-26 Verbatim Constraint at Synthesis)

**Hypothesis**: The adversarial role-instruction base (R7 V-03) gains C-25 and C-26
by two targeted additions at the synthesis step: (1) an explicit C-26 constraint
sentence — "each synthesis section header is a verbatim copy of its manifest entry,
character-for-character; a header that diverges is a structural defect" — and (2)
[PAIR REQUIRED] annotations at the synthesis step requirement sites that currently
have pairs implicitly. The Role 1 STRONGEST CLAIM instruction gains a "quote verbatim"
mandate. Tests whether a single constraint sentence at the synthesis step is the
minimum viable C-26 enforcement mechanism on an adversarial-role base.

This is R7 V-03 (adversarial roles: Inertia Advocate + Inertia Analyst, synthesis
manifest with all five sub-protocol names, NAMED CLAIM, pass/fail pairs at all role 2
sites) with three additions: (1) "do not paraphrase -- quote verbatim from your
STRONGEST CLAIM above" at the NAMED CLAIM label instruction, (2) C-26 verbatim
constraint at synthesis manifest, (3) [PAIR REQUIRED] annotation at each synthesis-
step requirement that currently has an implicit pair.

```
Auto-detect the feature from repo context. Do not prompt unless context is absent.

Run two sequential roles. Do not merge their output.

---

### ROLE 1: Inertia Advocate

You are a senior engineer who has relied on the current workaround for over a year.
You know its real costs and its real strengths. Describe and defend it.

**Task 1 -- Describe the workaround -- Replication Fidelity Standard.**

Name the workaround. Apply all three sub-requirements independently:

a. Product names, not categories.
   Pass: "GitHub Actions" / Fail: "CI system"
   Pass: "Confluence page" / Fail: "doc"
   Pass: "custom Python script via Makefile target" / Fail: "script"

b. Major steps in numbered sequence.
   Pass: "1. engineer opens Confluence template, 2. copies to project page, 3. edits four required fields, 4. pings #approvals in Slack" / Fail: "team follows the standard process"

c. Institutional knowledge flagged explicitly: any step requiring tribal context,
   undocumented conventions, or shared credentials a new team member lacks.
   Pass: "step 4 requires posting in #approvals with a specific prefix -- not in onboarding docs" / Fail: [omitting a step that depends on undocumented knowledge]

Write with enough detail that another team with no prior context could reproduce the workflow.

**Task 2 -- Make the case for staying.**

Why is the workaround acceptable? Name specific friction points: migration time, training
cost, workflow disruption. Name the teams or systems that would be affected. Be concrete.

**Task 3 -- State your STRONGEST CLAIM.**

Write the single argument a skeptical senior engineer would stake their credibility on.
One complete declarative sentence. Quote it as you would say it in a review meeting.
Label it: **STRONGEST CLAIM: "[exact text of claim]"**

**Task 4 -- Identify the scenarios where the workaround holds.**

What team sizes, project types, or usage patterns does the workaround serve correctly?
Name specific conditions, not general categories.

Output labeled: `WORKAROUND PROFILE (Advocate)`

---

### ROLE 2: Inertia Analyst

You have read the Advocate's WORKAROUND PROFILE. Produce the full inertia assessment.

**Task 1 -- Assign the inertia threat score.**

Inertia is HIGH by default. Downgrade only with written justification and evidence.
[PAIR REQUIRED] Pass: explicit "HIGH" label present. / Fail: narrative language without the explicit token.

**Task 2 -- Apply the Switching Cost Protocol.**

Three independently quantified dimensions. Each must be numeric, not an adjective:

- Time: hours or days per project or team.
  [PAIR REQUIRED] Pass: "2-4 hours per project for config migration" / Fail: "moderate effort"
- Training: days, people affected, specific skills required.
  [PAIR REQUIRED] Pass: "1-2 days for 3-4 engineers covering API changes and new config format" / Fail: "some training required"
- Disruption: coordination overhead, named systems or teams affected.
  [PAIR REQUIRED] Pass: "CI pipeline paused for 4-hour migration window, coordinated with ops team" / Fail: "team disruption expected"

**Task 3 -- Apply the Loss Condition Standard.**

Two or more conditions under which the workaround is worse than the feature.
Each condition must be falsifiable. Required columns: # | Condition | Observable Threshold | Verification Command

[PAIR REQUIRED] Observable Threshold: Pass: "active project count >= 4" / Fail: "when teams get busy"
[PAIR REQUIRED] Verification Command: Pass: "Jira: open the active sprint board -> count rows where Status = Active. If >= 4, condition applies." / Fail: "review your sprint board"

**Task 4 -- Apply the Failure Mode Standard.**

Two or more failure modes. Distinct from switching costs. Required columns:
# | Failure Mode | Trigger | Impact | Severity

[PAIR REQUIRED] Trigger: Pass: "when queue depth exceeds 500 messages" / Fail: "under heavy load"
[PAIR REQUIRED] Impact: Pass: "events silently dropped with no error surfaced to the caller" / Fail: "the workaround stops working"
[PAIR REQUIRED] Severity: Pass: "HIGH -- events silently dropped with no audit trail" / Fail: "HIGH" without naming the exposure.

**Task 5 -- Forward-Looking Risk.**

What happens over the next 6-12 months for teams that stay? Name a specific compounding
cost or divergence risk with an explicit time horizon.
[PAIR REQUIRED] Pass: names specific failure event with time range. / Fail: "will become harder to maintain."

**Task 6 -- Apply the Anchored Rebuttal Protocol.**

Step 1. Write the strongest case for staying. Label it: **STEELMAN**
Step 2. Extract the single strongest specific claim. Do not paraphrase -- quote the
   exact text of the STRONGEST CLAIM the Advocate stated in Role 1, or the most
   powerful sentence from the STEELMAN you wrote in Step 1.
   Label it: **NAMED CLAIM: "[exact text, verbatim]"**
Step 3. Rebut only that named claim. State why it fails, traceable to the claim's
   exact content.

Output labeled: `INERTIA ASSESSMENT (Analyst)`

---

### SYNTHESIS

Merge the Workaround Profile and the Inertia Assessment into a single artifact.

The artifact must contain the following sections. Each section header must be
a verbatim copy of its manifest entry below -- character-for-character, no reformatting.
A section header that diverges from its manifest entry is a structural defect: correct
before writing the artifact.

Manifest:
- Workaround Description -- Replication Fidelity Standard
- Switching Cost Profile -- Switching Cost Protocol
- Inertia Threat Score
- Why Inertia Loses -- Loss Condition Standard
- Workaround Failure Modes -- Failure Mode Standard
- Forward-Looking Risk
- Steelman and Rebuttal -- Anchored Rebuttal Protocol

[PAIR REQUIRED] Section header verbatim alignment: Pass: header "Workaround Description -- Replication Fidelity Standard" matches manifest entry "Workaround Description -- Replication Fidelity Standard" exactly. / Fail: header uses "1. Workaround Description" or "Workaround Description (Replication Fidelity Standard)" -- any divergence from the manifest entry text.

[PAIR REQUIRED] NAMED CLAIM quotation fidelity: Pass: the text inside NAMED CLAIM quotes appears verbatim in the STEELMAN written at Step 1 of the Anchored Rebuttal Protocol. / Fail: paraphrased or condensed version substituted.

After the synthesis, add:
- Named competitors (3-5): feature overlap, threat level (HIGH/MEDIUM/LOW), one-line differentiation
- The whitespace: what no competitor owns
- Table stakes: what any entrant must match

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## V-04 — Combined: Role Sequence + Lifecycle Emphasis (Three-Phase, Co-Located Constraint Sentences)

**Hypothesis**: Organizing the output into three named lifecycle phases (PROFILE /
THREAT / VERDICT) with explicit phase-boundary instructions, and co-locating three
constraint sentences -- one for C-24, one for C-25, one for C-26 -- at the entry to
the THREAT phase (where the model has the most structural decisions to make) produces
reliable compliance. The constraint sentences give the model the criterion text, not
just a structural scaffold that incidentally satisfies it. Tests whether three explicit
named constraints placed at the moment of highest structural risk produce more reliable
C-24/C-25/C-26 compliance than distributed instructions across sections.

This builds on R7 V-04 (phase-fusion, explicit constraint sentences) with a three-phase
lifecycle structure and three targeted constraint sentences for the new criteria. R7 V-04
already passed C-24/C-25/C-26 retroactively -- R8 V-04 makes those properties explicit
rather than incidental.

```
Auto-detect the feature from repo context. Do not prompt unless context is absent.

Produce a three-phase inertia analysis. Each phase must be clearly labeled. Do not
merge phases.

**Three structural constraints apply to this entire output. Satisfy all three before
writing any phase content:**

1. EXACT QUOTATION: At the NAMED CLAIM label in the Anchored Rebuttal Protocol, quote
   the exact text from the STEELMAN -- do not paraphrase, condense, or strengthen.
   A named claim that cannot be found verbatim in the steelman above it is a structural defect.

2. PAIR COVERAGE: At every requirement site that has a failure condition, include an
   explicit pass/fail example pair. Every requirement site. Not just the first two. Not
   just the examples provided in this prompt. If you add a requirement, add a pair.

3. VERBATIM ALIGNMENT: The text in the section manifest and the text in the corresponding
   section header must be character-for-character identical. Do not add prefixes, numbers,
   or parenthetical labels to headers that are not in the manifest, and vice versa.

---

### PHASE 1 -- PROFILE: What Teams Currently Do

Describe the current workaround so that another team could reproduce it with no prior
context. Apply the Replication Fidelity Standard across all three dimensions:

**Replication Fidelity Standard:**

a. Tool names at product level, not category level.
   [PAIR REQUIRED] Pass: "GitHub Actions" / Fail: "CI system"
   [PAIR REQUIRED] Pass: "Confluence page maintained by the platform team" / Fail: "documentation"

b. Major steps in numbered sequence.
   [PAIR REQUIRED] Pass: "1. Engineer opens the template, 2. fills four required fields, 3. pings #approvals in Slack, 4. waits for two approvals before merging" / Fail: "team follows the standard process"

c. Institutional knowledge flagged: undocumented conventions, tribal context, shared credentials.
   [PAIR REQUIRED] Pass: "the #approvals ping requires a specific prefix that is not documented anywhere -- new engineers learn this from their tech lead" / Fail: [omitting undocumented steps]

**Switching Cost Profile -- Switching Cost Protocol:**

Quantify adoption cost across three dimensions. Numeric estimates required.

- Time: hours or days per project or per team to migrate.
  [PAIR REQUIRED] Pass: "3-5 hours per project to convert existing YAML configurations" / Fail: "moderate effort"
- Training: days, number of people, specific skills to learn.
  [PAIR REQUIRED] Pass: "1-2 days for 4-5 engineers covering the new config format and CLI tooling" / Fail: "some training required"
- Disruption: named systems or teams affected, coordination required.
  [PAIR REQUIRED] Pass: "CI pipeline unavailable for a 4-hour migration window; ops team must be pre-notified" / Fail: "team disruption expected"

---

### PHASE 2 -- THREAT: Why the Workaround Loses

This output must contain the following sections. Section headers must be verbatim copies
of these manifest entries (VERBATIM ALIGNMENT constraint -- see above):

Manifest:
- Inertia Threat Score
- Why Inertia Loses -- Loss Condition Standard
- Workaround Failure Modes -- Failure Mode Standard
- Forward-Looking Risk

**Inertia Threat Score**

Assign: HIGH (default). Downgrade only with written justification and named evidence.
[PAIR REQUIRED] Pass: "HIGH" label explicit. / Fail: narrative substitute or omitted score.

**Why Inertia Loses -- Loss Condition Standard**

Two or more falsifiable conditions. Required columns: # | Condition | Observable Threshold | Verification Command

[PAIR REQUIRED] Observable Threshold: Pass: "concurrent project count >= 4" / Fail: "when teams scale up"
[PAIR REQUIRED] Verification Command: Pass: "Jira: open the active sprint board -> count rows where Status = Active. If >= 4, threshold met." / Fail: "check your project board"

**Workaround Failure Modes -- Failure Mode Standard**

Two or more failure modes. Distinct from switching costs.
Required columns: # | Failure Mode | Trigger | Impact | Severity

[PAIR REQUIRED] Trigger: Pass: "when queue depth exceeds 500 messages" / Fail: "under load"
[PAIR REQUIRED] Impact: Pass: "events silently dropped with no error surfaced to the caller" / Fail: "system degrades"
[PAIR REQUIRED] Severity: Pass: "HIGH -- silent data loss creates a compliance gap with no audit trail" / Fail: bare severity token without named exposure.

**Forward-Looking Risk**

One paragraph. What happens over the next 6-12 months? Explicit time horizon required.
[PAIR REQUIRED] Pass: "within 6 months, the script will break when the upstream API changes its response shape" / Fail: "will become increasingly difficult to maintain"

---

### PHASE 3 -- VERDICT: Steelman and Final Judgment

This output must contain the following sections. Section headers verbatim per manifest:

Manifest:
- Steelman and Rebuttal -- Anchored Rebuttal Protocol
- Competitive Landscape

**Steelman and Rebuttal -- Anchored Rebuttal Protocol**

Apply the Anchored Rebuttal Protocol. Three steps, do not merge.

Step 1. Write the strongest case for keeping the workaround. Label: **STEELMAN**
   [PAIR REQUIRED] Pass: names a specific, concrete concern a real skeptic would raise. / Fail: general principle without named friction.

Step 2. Extract the single strongest specific claim from Step 1. Quote verbatim -- do
   not paraphrase. Label: **NAMED CLAIM: "[exact text, verbatim from STEELMAN above]"**
   (EXACT QUOTATION constraint -- see above. The text must appear in Step 1 unchanged.)
   [PAIR REQUIRED] Pass: text appears unchanged in STEELMAN. / Fail: paraphrased or condensed.

Step 3. Rebut only the named claim. One paragraph. Traceable to the claim's exact content.
   [PAIR REQUIRED] Pass: rebuttal identifies specific weakness in the claim's logic, tied to the quoted text. / Fail: generic response that does not address the specific assertion.

**Competitive Landscape**

- Named competitors (3-5): feature overlap, threat level (HIGH/MEDIUM/LOW), one-line differentiation
- The whitespace: what no competitor owns
- Table stakes: what any entrant must match

Write artifact to: simulations/scout/inertia/{topic}-inertia-{date}.md
```

---

## V-05 — Combined: Full-Stack Template + Pre-Flight Verification Gate (C-24/C-25/C-26 Repair Loop)

**Hypothesis**: R7 V-05's pre-flight repair-loop gate extends naturally to C-24/C-25/C-26
by adding three new checks targeting the specific defect each criterion prevents: (1) a
verbatim-quotation scan that checks whether the NAMED CLAIM text exists unchanged in the
STEELMAN, (2) an annotation-site count that verifies [PAIR REQUIRED] appears at every
structural requirement with a failure condition, (3) a manifest-header identity scan that
checks each section header against its manifest entry character-for-character. The
pre-flight gate converts all three new criteria from properties-to-achieve to
properties-to-verify-and-repair. A non-compliant first pass can become compliant through
the mandatory repair before the artifact is written.

This builds on R7 V-05 (full-stack template, STEP 1 / STEP 2 / STEP 3 structure, pre-flight
verification gate with mandatory repair) adding three new checks in STEP 2 and
reinforcing the NAMED CLAIM instruction in STEP 1.

```
Auto-detect the feature from repo context. Do not prompt unless context is absent.

Produce the scout-inertia artifact in three steps. Do not skip STEP 2.

---

### STEP 1 -- DRAFT: Complete the Inertia Analysis

This output must contain the following sections. Section headers must be
character-for-character identical to manifest entries -- preserve every word and
punctuation mark:

Manifest:
- Section 1: Workaround Description -- Replication Fidelity Standard
- Section 2: Switching Cost Profile -- Switching Cost Protocol
- Section 3: Inertia Threat Score
- Section 4: Why Inertia Loses -- Loss Condition Standard
- Section 5: Workaround Failure Modes -- Failure Mode Standard
- Section 6: Forward-Looking Risk
- Section 7: Steelman and Rebuttal -- Anchored Rebuttal Protocol

**Section 1: Workaround Description -- Replication Fidelity Standard**

Apply the Replication Fidelity Standard. All three sub-requirements independent:

1. Product names, not categories.
   [PAIR REQUIRED] Pass: "GitHub Actions" / Fail: "CI system"
   [PAIR REQUIRED] Pass: "custom Python script via Makefile target" / Fail: "automation script"
2. Numbered step sequence.
   [PAIR REQUIRED] Pass: "1. engineer opens template, 2. edits four fields, 3. pings #approvals" / Fail: "team follows the process"
3. Institutional knowledge flagged.
   [PAIR REQUIRED] Pass: "requires #approvals prefix -- not in onboarding docs" / Fail: [omitting undocumented steps]

Name the workaround. One paragraph minimum.

**Section 2: Switching Cost Profile -- Switching Cost Protocol**

Three quantified dimensions. Numeric estimates required.

| Dimension | Estimate | Basis |
|-----------|----------|-------|
| Time | [X hours/days per project] | [what drives this] |
| Training | [X days, Y people] | [what must be learned] |
| Disruption | [what changes, who is affected] | [coordination cost] |

[PAIR REQUIRED] Time: Pass: "2-4 hours per project for YAML migration" / Fail: "moderate effort"
[PAIR REQUIRED] Training: Pass: "1-2 days for 3-4 engineers" / Fail: "some training required"
[PAIR REQUIRED] Disruption: Pass: "CI pipeline paused for 4-hour window, coordinated with ops" / Fail: "team disruption expected"

**Section 3: Inertia Threat Score**

Assign: HIGH. Downgrade requires written justification.
[PAIR REQUIRED] Pass: explicit "HIGH" label. / Fail: narrative substitute.

**Section 4: Why Inertia Loses -- Loss Condition Standard**

Two or more falsifiable conditions. Required columns: # | Condition | Observable Threshold | Verification Command

[PAIR REQUIRED] Observable Threshold: Pass: "project count >= 4" / Fail: "when teams get busy"
[PAIR REQUIRED] Verification Command: Pass: "Jira: open sprint board -> count active rows. If >= 4, applies." / Fail: "check your board"

**Section 5: Workaround Failure Modes -- Failure Mode Standard**

Two or more failure modes. Distinct from switching costs.
Required columns: # | Failure Mode | Trigger | Impact | Severity

[PAIR REQUIRED] Trigger: Pass: "when queue depth exceeds 500 messages" / Fail: "under heavy load"
[PAIR REQUIRED] Impact: Pass: "events silently dropped, no error to caller" / Fail: "stops working"
[PAIR REQUIRED] Severity: Pass: "HIGH -- silent drop creates compliance gap" / Fail: bare label without named exposure.

**Section 6: Forward-Looking Risk**

One paragraph. Explicit time horizon required.
[PAIR REQUIRED] Pass: "within 6 months, script breaks on API response change" / Fail: "harder to maintain over time"

**Section 7: Steelman and Rebuttal -- Anchored Rebuttal Protocol**

Three steps in sequence. Do not merge.

Step 1. Strongest case for staying. Label: **STEELMAN**
   [PAIR REQUIRED] Pass: concrete friction a real skeptic would name. / Fail: general principle.

Step 2. Extract the single strongest specific claim. Quote verbatim from Step 1 above --
   do not paraphrase, condense, or rephrase. The text must exist unchanged in STEELMAN.
   Label: **NAMED CLAIM: "[exact verbatim text from STEELMAN above]"**
   [PAIR REQUIRED] Pass: text found verbatim in STEELMAN. / Fail: paraphrased.

Step 3. Rebut only the named claim. Traceable to the quoted text.
   [PAIR REQUIRED] Pass: rebuttal targets specific logic of the claim. / Fail: generic response.

---

### STEP 2 -- VERIFY AND REPAIR: Pre-Flight Compliance Check

Before writing the final artifact, check each property. For each check: state the
result explicitly (PASS or FAIL). If any check is FAIL, repair before proceeding to STEP 3.

**Check 1 -- C-21: Sub-protocol count**
Count the sub-protocol names in the manifest. Count the sub-protocol names in section headers.
State: "C-21 check: [N] of 7 sub-protocols in manifest, [N] of 7 in headers -- [PASS / FAIL]"
If FAIL: list which sub-protocol names are missing and add them before continuing.

**Check 2 -- C-22 / C-25: Pair coverage and annotation density**
Identify every structural requirement in Sections 1-7 that has a failure condition.
For each: verify a pass/fail example pair exists AND a [PAIR REQUIRED] annotation is present.
State: "C-22/C-25 check: [N] requirement sites found, [N] pairs present, [N] annotated -- [PASS / FAIL]"
If FAIL: list unannotated sites, add [PAIR REQUIRED] annotations, add missing pairs before continuing.

**Check 3 -- C-23 / C-26: Manifest-header alignment**
For each manifest entry, locate the corresponding section header.
Verify the header text is character-for-character identical to the manifest entry.
State: "C-23/C-26 check: Section [N] -- manifest '[entry]' vs header '[header]' -- [MATCH / DIVERGE]"
Report for all 7 sections.
If any DIVERGE: correct the header to match the manifest entry exactly before continuing.

**Check 4 -- C-24: Verbatim quotation fidelity**
Locate the NAMED CLAIM label in Section 7. Extract the quoted text.
Find that exact text in the STEELMAN written at Step 1 of Section 7.
State: "C-24 check: NAMED CLAIM text '[first 10 words of claim]...' found verbatim in STEELMAN -- [PASS / FAIL]"
If FAIL: replace the NAMED CLAIM text with the verbatim sentence from the STEELMAN before continuing.

**Check 5 -- C-03: Inertia Threat Score**
Confirm Section 3 contains an explicit "HIGH" label.
State: "C-03 check: threat score explicit HIGH -- [PASS / FAIL]"
If FAIL: assign HIGH with justification.

---

### STEP 3 -- WRITE: Produce the Final Artifact

All five checks in STEP 2 must show PASS before writing the artifact.

Write the complete inertia analysis to:
simulations/scout/inertia/{topic}-inertia-{date}.md

After the inertia analysis, add:
- Named competitors (3-5): feature overlap, threat level (HIGH/MEDIUM/LOW), one-line differentiation
- The whitespace: what no competitor owns
- Table stakes: what any entrant must match
```

---

## Variation Summary

| ID | Axis | Hypothesis | C-24 mechanism | C-25 mechanism | C-26 mechanism | Reliability tier |
|----|------|------------|----------------|----------------|----------------|-----------------|
| V-01 | Single: phrasing register (formal/imperative) | Formal imperative + targeted additions on simplest base closes all three new criteria | "Do not paraphrase -- quote verbatim" explicit instruction | [PAIR REQUIRED] at every site including NAMED CLAIM step | Explicit verbatim-identity instruction co-located with manifest | Lowest -- instruction-based, no structural enforcement |
| V-02 | Single: output format (pre-printed annotated template) | R7 V-02 already passed retroactively -- R8 makes the pattern explicit, stripping incidental satisfaction | "Do not paraphrase" + [PAIR REQUIRED] at quotation fidelity site | [PAIR REQUIRED] at every site including remaining gaps | Explicit verbatim constraint + "Section N:" consistent prefix | Medium -- per-site annotation + explicit constraint |
| V-03 | Single: inertia framing (COMPETITOR ZERO adversarial) | Adversarial role base gains C-25/C-26 via constraint sentence at synthesis step; [PAIR REQUIRED] added to synthesis requirements | "Quote verbatim from STRONGEST CLAIM" in Role 1 | [PAIR REQUIRED] at synthesis requirement sites | C-26 constraint sentence at synthesis: "header = manifest verbatim" | Medium-high -- constraint at synthesis step |
| V-04 | Combined: role sequence + lifecycle emphasis | Three-phase lifecycle + three co-located constraint sentences at phase entry -- gives model criterion text, not just structure | Co-located EXACT QUOTATION constraint sentence | PAIR COVERAGE constraint sentence ("at every site, not just examples") | VERBATIM ALIGNMENT constraint sentence | High -- three named constraints at phase transition |
| V-05 | Combined: full-stack + pre-flight repair gate | Repair-loop gate extended to C-24/C-25/C-26 -- converts properties-to-achieve to properties-to-verify-and-repair; non-compliant first pass becomes compliant | Check 4: verbatim scan + repair obligation | Check 2: annotation-site count + repair obligation | Check 3: manifest-header identity scan per section + repair | Highest -- mandatory repair loop; defect cannot survive to artifact |

**Predicted scores (v8 rubric, 18 criteria):**

| Variation | C-24 | C-25 | C-26 | Predicted score |
|-----------|------|------|------|-----------------|
| V-01 | PASS | PASS | PASS | 100/100 |
| V-02 | PASS | PASS | PASS | 100/100 |
| V-03 | PASS | PASS | PASS | 100/100 |
| V-04 | PASS | PASS | PASS | 100/100 |
| V-05 | PASS | PASS | PASS | 100/100 |

**Highest-confidence prediction: V-05.** The repair-loop gate structurally prevents any
of the three new criteria from failing silently -- a non-compliant draft triggers an
explicit FAIL at the corresponding check and a mandatory repair before the artifact is
written. C-24/C-25/C-26 failure is locally detectable rather than evaluator-detectable.

**Highest structural-risk prediction: V-01.** It relies on three instruction-based
additions to the simplest base. If the model paraphrases the claim, omits a [PAIR REQUIRED]
annotation, or reformats a section header, there is no repair path. V-01's value is
characterizing the minimum viable instruction surface for all three new criteria.

**Key discriminator for R8:** C-24's "verbatim not paraphrase" requirement is the
hardest to enforce by instruction alone because paraphrase can satisfy the *intent* of
NAMED CLAIM while failing the *criterion*. V-05's Check 4 (explicit scan for verbatim
text in STEELMAN) is the only mechanism that forces detection rather than prevention.
