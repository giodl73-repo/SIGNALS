# quest-rubric Variate — Round 10 (First round against rubric v7)
**Date:** 2026-03-15
**Rubric:** v7 (C-01--C-21; adds C-20: anti-overlap constraint structurally placed and names threshold escalation as prohibited; C-21: each aspirational criterion carries a required per-criterion gap claim)
**Target criteria:** C-20, C-21

**Round 10 design note:** Rounds 1--9 produced mechanisms for C-01 through C-19 across rubric tracks v1--v6. Against rubric v7, the two new aspirational criteria are C-20 and C-21. C-20 closes the gap C-19 left open: a protocol can satisfy C-19 (anti-overlap stated) while leaving the constraint unenforceable — if the statement lives in running prose, an author can proceed without consulting it, and "go beyond" remains undefined enough to permit threshold escalation ("I'm testing the same property at count >= 5 instead of >= 3, so it's aspirational"). C-20 requires two things simultaneously: (1) structural placement — the anti-overlap constraint must appear in a dedicated labeled block, a required step, or a required section that must be completed before aspirational criteria are authored; (2) threshold prohibition — the constraint must explicitly name threshold escalation as a prohibited form of aspirational distinction ("even at a higher threshold or narrower pass band — is not aspirational"). Neither alone is sufficient for PASS; either alone is PARTIAL. C-21 requires per-criterion instantiation: each aspirational criterion must carry a required structural field (labeled, non-blank) naming the specific coverage territory it fills. Protocol-level placement (C-20) prevents threshold escalation at authoring time; per-criterion instantiation (C-21) makes anti-overlap auditable per criterion by an independent evaluator. The chain from v6 to v7: C-19 (stated) → C-20 (placed + threshold named) → C-21 (per-criterion documented). This round probes three single-axis mechanisms isolating C-20 structural placement, C-20 threshold prohibition, and C-21 per-criterion field; plus two combined variations closing both criteria simultaneously.

---

## Round 10 Variation Map

| Variation | Axis | C-20 probe | C-21 probe | Notes |
|-----------|------|-----------|-----------|-------|
| V-01 | Lifecycle emphasis (SCOPE CONSTRAINT block) | Very strong -- dedicated labeled "SCOPE CONSTRAINT:" block placed as a required phase step; includes threshold prohibition language; must be completed before aspirational authoring | Strong -- "Fills gap" required field in aspirational criterion template; blank = format error | Single-axis; lifecycle structure; cleanest path: minimal additions each targeting one criterion independently; tests whether a labeled block + field annotation closes both without role decomposition |
| V-02 | Output format (Gap Audit Table before aspirational section) | Strong -- gap audit table placed before aspirational criteria in the output document; table header states threshold prohibition; structural placement via format position | Very strong -- aspirational criteria table includes a mandatory "Gap" column; each aspirational row must cite a specific uncovered territory from the table; blank cell = format violation | Single-axis; format-level structural encoding; tests whether format position alone satisfies C-20's structural placement requirement vs a labeled block; C-21 very strong via table column |
| V-03 | Role sequence (Scope Gatekeeper role) | Very strong -- dedicated pre-aspirational role whose sole deliverable is a SCOPE DECLARATION naming covered territory and threshold escalation as prohibited; role cannot be bypassed | Moderate -- no per-criterion gap field required; Scope Gatekeeper output is a protocol-level declaration, not per-criterion; C-21 intentionally absent to isolate C-20 mechanism | Single-axis; structural role; tests whether a named sequential role with a single deliverable satisfies C-20's structural placement requirement when the deliverable explicitly names threshold prohibition |
| V-04 | Role sequence + output format (Scope Gatekeeper + per-criterion Gap field) | Very strong -- Scope Gatekeeper role produces SCOPE DECLARATION with threshold prohibition before aspirational authoring; structural by role sequencing | Very strong -- "Fills gap" field required per aspirational criterion citing a specific gap from the Scope Gatekeeper's gap zone; blank = format error; C-21 per-criterion instantiation linked to C-20 structural declaration | Combined; closes C-20 and C-21 simultaneously; structural chain: SCOPE DECLARATION (C-20 placement) → "Fills gap" field (C-21 per-criterion); parallel to C-13/C-15 chain and C-19/C-21 chain |
| V-05 | Inertia framing + lifecycle emphasis (Declared-Not-Placed competitor + phase gates) | Strong -- names the specific protocol that achieves C-19 (anti-overlap stated) but fails C-20 (constraint in running prose, no threshold prohibition); builder must place constraint in a structural element AND name threshold escalation to exceed the competitor | Strong -- names the specific protocol that achieves C-20 (structurally placed) but fails C-21 (no per-criterion gap field); builder must add per-criterion "Fills gap" field to exceed second competitor | Combined; two-competitor architecture; each competitor scoped to its target criterion; tests whether naming the specific failure mode of each criterion's predecessor competitor produces the correct fix more reliably than structural or format framing alone |

---

## V-01 -- Lifecycle Emphasis (SCOPE CONSTRAINT Block)

**Axis:** Lifecycle emphasis
**Hypothesis:** Rounds 5 and 8 established that inserting a structural gate before a phase produces reliable compliance with properties that depend on ordering: R5's STOP gate before tier assignment produced C-17 compliance (traceable derivation); R8 V-03's coverage map gate before aspirational criteria produced C-19 compliance (anti-overlap stated). V-01 applies the same gate mechanism to C-20 by placing a dedicated "SCOPE CONSTRAINT:" labeled block as a required phase step immediately before aspirational authoring. The block has three required outputs: (1) the coverage summary of what essential and recommended tiers already cover, (2) the threshold prohibition statement naming escalation as a prohibited form of aspirational distinction, and (3) a named gap zone. The block cannot be skipped because Phase 3 (aspirational authoring) requires the gap zone name as input. C-21 is achieved by adding a "Fills gap:" required annotation to the aspirational criterion template, linked to the gap zone named in the SCOPE CONSTRAINT block. The prediction: C-20 very strong via structural block + threshold language; C-21 strong via per-criterion field; combined as a single-axis lifecycle variation rather than a role sequence, testing whether explicit phase structure alone closes both criteria without decomposing into named roles.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### PHASE 1 -- FAILURE MODE ANALYSIS

Read the skill spec. Name every way an output of this skill can be non-functional, degraded, or cosmetically flawed. Assign severity:

```
F-NN | failure behavior | structural gap: what the skill failed to require | blocking / suboptimal / cosmetic
```

Minimum: 3 blocking entries, 2 suboptimal entries. Do not begin Phase 2 until the failure log contains at least 5 entries.

---

### PHASE 2 -- CRITERIA (ESSENTIAL AND RECOMMENDED)

Draft essential criteria (3-5) from blocking failure modes. Draft recommended criteria (2-3) from suboptimal failure modes. Continue C-NN numbering across both tiers.

Each criterion requires five fields:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: one sentence -- what must be true in a passing output. State the downstream consequence of absence: "without [property], [failure] occurs."
- **Weight**: essential | recommended
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence with observable anchors. No "is clear" or "adequately covers" as sole criterion. Recommended criteria: pass condition tests degree, precision, or specificity -- not whether a field exists.

Do not write aspirational criteria until the SCOPE CONSTRAINT block (Phase 2.5) is complete.

---

### PHASE 2.5 -- SCOPE CONSTRAINT

**Complete this block before writing any aspirational criterion. This block is a required input to Phase 3.**

```
SCOPE CONSTRAINT:

Essential tier covers:
  [List the specific failure modes and output properties guarded by your essential
   criteria -- one line per criterion, naming the property and its C-NN reference.]

Recommended tier covers:
  [List the quality properties guarded by your recommended criteria -- one line per
   criterion, naming the dimension (degree / precision / specificity) and C-NN.]

Threshold escalation is NOT aspirational:
  A criterion that tests a property already covered by an essential or recommended
  criterion -- even at a higher threshold, a stricter count, or a narrower pass band
  -- is not aspirational. It is a tighter version of an existing lower-tier criterion.
  Tighter is not beyond.

Gap zone (what essential and recommended do NOT cover):
  [Name at least 1 specific property that an output passing essential + recommended
   could still lack. This must not be reachable by tightening any existing criterion.
   Name it precisely -- this becomes the required citation for aspirational criteria.]
```

Do not proceed to Phase 3 until this block is complete and the Gap zone contains at least 1 named gap.

---

### PHASE 3 -- ASPIRATIONAL CRITERIA (1-2)

Write aspirational criteria targeting the gap zone named in Phase 2.5. Each criterion must fall in the gap zone -- not in the essential or recommended coverage zones, not in those zones at a higher threshold.

Each aspirational criterion requires five fields plus one required annotation:

- **ID**: C-NN (continuing from recommended criteria)
- **Text**: one sentence
- **Weight**: aspirational
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence with observable anchors
- **Fills gap**: [quote or paraphrase the specific gap from the Phase 2.5 SCOPE CONSTRAINT block that this criterion addresses -- **required; blank = format error**]

A blank "Fills gap" field means the criterion cannot be verified against the anti-overlap constraint. Finalize only after confirming the cited gap is named in Phase 2.5.

---

### PHASE 4 -- SCORING

State the scoring formula:

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

PASS = 1.0, PARTIAL = 0.5, FAIL = 0.

Golden threshold: all essential criteria PASS AND composite >= 80.

Tier targets: 3-5 essential, 2-3 recommended, 1-2 aspirational. At least 3 distinct categories across the full criterion set.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences -- state the SCOPE CONSTRAINT principle: aspirational criteria fill gaps, not thresholds; the Phase 2.5 block makes threshold escalation a named prohibited form, not an inferred boundary; the "Fills gap" annotation makes anti-overlap auditable per criterion), then the SCOPE CONSTRAINT block (retained in output as the tier scope record), then criteria ordered essential -> recommended -> aspirational (Fills gap annotations retained; failure log omitted), then scoring section.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-02 -- Output Format (Gap Audit Table Before Aspirational Section)

**Axis:** Output format
**Hypothesis:** R7 V-02 showed that a structural column in a criteria table makes absent properties visible as blank cells -- structural violations rather than judgment calls. V-02 applies format-level structural enforcement to C-20 and C-21 simultaneously by placing a Gap Audit Table between the recommended and aspirational sections of the output document. The Gap Audit Table is a required output element: it lists each essential and recommended criterion with a "Coverage zone" column (what failure mode or quality property it guards), and a table header that states the threshold prohibition: "Aspirational criteria must fall OUTSIDE the zones in this table -- a criterion covering a mapped zone at a higher threshold is not aspirational." The table's placement before the aspirational criteria section satisfies C-20's structural placement requirement via document position rather than a labeled block. C-21 is achieved by requiring the aspirational criteria table to include a "Gap" column where each aspirational row must cite a specific uncovered territory from the Gap Audit Table; a blank Gap cell is a table violation, not a soft omission. The prediction: C-20 strong via table position + threshold prohibition in header; C-21 very strong via mandatory table column with blank-cell constraint; this tests whether format-level document position qualifies as C-20's "dedicated structural element" versus a labeled named block.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

**STEP 1 -- SKILL PROFILE**

Write two sentences: what does this skill produce, and what does a complete correct output contain?

**STEP 2 -- FAILURE MODES**

Name every failure mode. Assign severity:

```
F-NN | failure behavior | severity: blocking / suboptimal / cosmetic
```

Minimum: 3 blocking, 2 suboptimal.

**STEP 3 -- ESSENTIAL AND RECOMMENDED CRITERIA**

Draft essential criteria (3-5) from blocking failure modes and recommended criteria (2-3) from suboptimal failure modes.

Each criterion: ID (C-NN), Text, Weight, Category, Pass condition. Recommended criteria: each pass condition tests degree, precision, or specificity -- not presence.

**STEP 4 -- GAP AUDIT TABLE**

Before writing any aspirational criterion, produce the Gap Audit Table:

```
| C-NN | Tier | Coverage zone (what it guards) |
|------|------|-------------------------------|
| C-01 | essential | [specific failure mode or property this criterion guards] |
| C-02 | essential | [specific failure mode or property] |
...
| C-NN | recommended | [specific quality property this criterion guards] |
```

**Anti-overlap constraint (table header -- required):**

> Aspirational criteria must fall OUTSIDE the coverage zones listed in this table. A criterion covering a zone already mapped here -- even at a higher threshold, a stricter count, or a narrower pass band -- is not aspirational. Higher threshold = tighter lower tier, not new territory.

The Gap Audit Table and its anti-overlap header must appear in the output document before the aspirational criteria section. Do not write aspirational criteria until the table is complete.

After the table, write:

```
Uncovered territory (not in any row above):
  [Name at least 1 specific property an output passing essential + recommended
   could still lack. Must not be reachable by adjusting a threshold in the table.]
```

**STEP 5 -- ASPIRATIONAL CRITERIA (1-2)**

Write aspirational criteria falling in the uncovered territory identified in Step 4. Present as a table:

```
| C-NN | Text | Weight | Category | Pass condition | Gap |
|------|------|--------|----------|----------------|-----|
| C-NN | [text] | aspirational | [category] | [pass condition] | [cite the uncovered territory from Step 4 that this criterion fills -- required; blank = table violation] |
```

The Gap column is required and must be non-blank. A blank Gap cell means the aspirational criterion cannot be verified against the anti-overlap constraint. The cited territory must be named in the Step 4 "Uncovered territory" section.

**STEP 6 -- SCORING**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

PASS = 1.0, PARTIAL = 0.5, FAIL = 0.
Golden threshold: all essential criteria PASS AND composite >= 80.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences -- state the Gap Audit Table principle: the table maps what essential and recommended already cover; an aspirational criterion covering a mapped zone at any threshold is a placement error, not a stretch goal; the Gap column makes this auditable per criterion), then Gap Audit Table (retained in output as the tier scope record), then criteria ordered essential -> recommended -> aspirational (Gap column retained in aspirational table), then scoring section. Failure mode list omitted from output.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-03 -- Role Sequence (Scope Gatekeeper Role)

**Axis:** Role sequence
**Hypothesis:** R8 V-04 showed that a dedicated pre-authoring role with a hard gate produces reliable compliance with its target criterion because the role is a named structural element: an agent cannot proceed to recommended criteria without the Vocabulary Definer's output, and cannot proceed to aspirational criteria without the Coverage Mapper's output. V-03 applies the same mechanism to C-20 by introducing a Scope Gatekeeper role positioned between recommended and aspirational authoring. The Scope Gatekeeper's sole deliverable is a SCOPE DECLARATION that must name (1) what essential and recommended criteria already cover, (2) the threshold prohibition: "aspirational criteria that test a property already covered by a lower tier, even at a higher threshold or narrower pass band, are not aspirational," and (3) the gap zone with at least one named uncovered property. The Builder may not write aspirational criteria until the Scope Gatekeeper output is written. C-21 is intentionally absent from this single-axis variation: no per-criterion "Fills gap" field is required. This isolates C-20 -- testing whether structural role placement with threshold prohibition produces PASS on C-20 while leaving C-21 exposed, confirming that C-20 and C-21 are genuinely separable by mechanism.

---

You are a two-role rubric construction system. The roles run in strict sequence. **Do not begin Role 2 phase-2 until the Scope Gatekeeper output is written.**

---

### ROLE 1 -- RUBRIC BUILDER (Phase 1: Failure Analysis and Essential + Recommended Criteria)

Read the skill spec and sample outputs.

**Step 1 -- Failure analysis.** Name failure modes:

```
F-NN | failure behavior | severity: blocking / suboptimal / cosmetic
```

Minimum: 3 blocking, 2 suboptimal.

**Step 2 -- Essential criteria (3-5).** From blocking failure modes. Five fields: ID (C-NN), Text, Weight (essential), Category, Pass condition. Text states the downstream consequence of absence: "without [property], [failure]."

**Step 3 -- Recommended criteria (2-3).** From suboptimal failure modes. Pass conditions test quality properties -- degree, precision, or specificity of the output -- not whether an element exists. Annotate: **Dimension:** [degree | precision | specificity].

**⛔ BUILDER GATE:** After Step 3, Role 1 pauses. Do not write aspirational criteria. The Scope Gatekeeper runs next.

---

### SCOPE GATEKEEPER

Read the essential and recommended criteria from Role 1. Your sole deliverable is the SCOPE DECLARATION. Write it now -- nothing else.

```
SCOPE DECLARATION:

What the essential tier already covers:
  [One line per essential criterion: "C-NN: guards against [specific failure mode /
   output property]." Name the thing the criterion catches, not the criterion itself.]

What the recommended tier already covers:
  [One line per recommended criterion: "C-NN: guards the [degree/precision/
   specificity] of [specific property]."]

Threshold escalation prohibition:
  An aspirational criterion that targets a property already covered by an essential
  or recommended criterion -- even at a higher threshold, a stricter count, a
  narrower pass band, or a more precise formulation -- is NOT aspirational. It is a
  tighter version of an existing lower-tier criterion. Tighter is not beyond. Do not
  apply this form to aspirational criteria.

Gap zone -- properties NOT covered by the essential or recommended tiers:
  [Name at least 1 property that an output passing essential + recommended could
   still lack. This property must not be reachable by adjusting a threshold in the
   coverage summary above. Be specific: name the observable that would be checked.]
```

**⛔ SCOPE GATEKEEPER GATE:** Output is the SCOPE DECLARATION. Do not proceed to Role 1 Phase 2 until the SCOPE DECLARATION is written and the gap zone contains at least 1 named gap.

---

### ROLE 1 -- RUBRIC BUILDER (Phase 2: Aspirational Criteria and Scoring)

Read the SCOPE DECLARATION. Write aspirational criteria (1-2) targeting the gap zone named by the Scope Gatekeeper.

Each aspirational criterion: five fields: ID (C-NN), Text, Weight (aspirational), Category, Pass condition. The criterion must fall in the gap zone -- not in the essential or recommended coverage zones, not in those zones at a higher threshold.

**Scoring:**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

PASS = 1.0, PARTIAL = 0.5, FAIL = 0.
Golden threshold: all essential criteria PASS AND composite >= 80.

Tier targets: 3-5 essential, 2-3 recommended, 1-2 aspirational. At least 3 distinct categories.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences -- state the Scope Gatekeeper principle: the Gatekeeper's SCOPE DECLARATION names what lower tiers already cover and prohibits threshold escalation before aspirational authoring begins; an aspirational criterion must fall in the gap zone, not tighten a covered zone), then SCOPE DECLARATION (retained in output as the tier scope record), then criteria ordered essential -> recommended -> aspirational, then scoring section. Failure mode list omitted.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-04 -- Role Sequence + Output Format (Scope Gatekeeper + Per-Criterion Gap Field)

**Axes:** Role sequence + output format
**Hypothesis:** V-03 closes C-20 via a dedicated Scope Gatekeeper role with threshold prohibition but leaves C-21 exposed. V-01 closes both via lifecycle phases but without role decomposition. V-04 combines V-03's Scope Gatekeeper (C-20: structural placement via named role + threshold prohibition) with V-01's per-criterion "Fills gap" field (C-21: per-criterion instantiation). The key architectural difference from V-01: the "Fills gap" field must cite the gap zone from the Scope Gatekeeper's SCOPE DECLARATION specifically -- not a self-authored gap description. This creates a two-level chain: the Scope Gatekeeper produces the authoritative gap register (C-20), and each aspirational criterion's "Fills gap" field must reference a named entry from that register (C-21). The citation requirement makes C-21 verifiable against C-20: an evaluator can check whether the cited gap appears in the SCOPE DECLARATION and whether the declaration was produced before aspirational authoring. This is the structural parallel to C-13/C-15 (phase gate → per-criterion gate) and C-19/C-21 (stated → instantiated) applied now at the placement level: the Scope Gatekeeper places the constraint (C-20); the "Fills gap" citation instantiates it per criterion (C-21).

---

You are a three-role rubric construction system. Roles run in strict sequence: Analyst, Scope Gatekeeper, Builder. **Do not begin a role until the previous role's output is written.**

---

### ANALYST ROLE

Read the skill spec and sample outputs.

**Failure log.** Minimum 5 entries:

```
F-NN | failure behavior | severity: blocking / suboptimal / cosmetic
```

**Essential criteria (3-5).** From blocking failure modes. Five fields per criterion:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: one sentence -- "without [property], [failure] occurs because [reason]"
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence with observable anchors

**Recommended criteria (2-3).** From suboptimal failure modes. Pass conditions test degree, precision, or specificity. Required annotation per criterion: **Dimension:** [degree | precision | specificity].

**⛔ ANALYST GATE:** Output is the failure log + essential criteria + recommended criteria. Do not write aspirational criteria. Do not proceed to Scope Gatekeeper output until the Analyst output is complete.

---

### SCOPE GATEKEEPER ROLE

Read the essential and recommended criteria from the Analyst. Your sole deliverable is the SCOPE DECLARATION. Write it completely before any aspirational criteria are drafted.

```
SCOPE DECLARATION:

Essential coverage:
  [One line per essential criterion: "C-NN guards against: [specific failure mode
   or output property -- name the thing caught, not the criterion]."]

Recommended coverage:
  [One line per recommended criterion: "C-NN guards the [dimension] of [property]."]

Threshold escalation prohibition:
  An aspirational criterion targeting a property already listed in Essential coverage
  or Recommended coverage above -- even at a higher threshold, a stricter count, or
  a narrower pass band -- is not aspirational. It is a tighter version of a covered
  criterion and does not qualify for the aspirational tier regardless of how it is
  labeled.

Gap register (what essential and recommended do NOT cover):
  Gap G-01: [Specific property an output scoring full marks on essential + recommended
    could still lack. Must not be reachable by adjusting any threshold in the coverage
    sections above. Name the observable: what would an evaluator check to confirm its
    presence or absence?]
  [Add Gap G-02 if a second distinct gap is identifiable.]
```

**⛔ SCOPE GATEKEEPER GATE:** Output is the SCOPE DECLARATION. The gap register must contain at least 1 named gap (G-01). Do not proceed to Builder until the SCOPE DECLARATION is written.

---

### BUILDER ROLE

Read the SCOPE DECLARATION. Write aspirational criteria (1-2) from the gap register. Each criterion must:

1. Target a gap listed in the Scope Gatekeeper's gap register
2. Not cover territory listed in Essential coverage or Recommended coverage -- at any threshold

Required fields per aspirational criterion:

- **ID**: C-NN (continuing from recommended criteria)
- **Text**: one sentence
- **Weight**: aspirational
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence with observable anchors
- **Fills gap**: [Cite the specific gap entry (G-NN) from the Scope Gatekeeper's gap register that this criterion addresses. Quote or closely paraphrase the named gap. **Required -- blank = format error.** A criterion without a non-blank Fills gap field cannot be verified against the anti-overlap constraint and is incomplete.]

After writing each aspirational criterion, verify: "Is the gap cited in 'Fills gap' present in the Scope Gatekeeper's gap register?" If not, revise the criterion or the gap citation before finalizing.

**Scoring:**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

PASS = 1.0, PARTIAL = 0.5, FAIL = 0.
Golden threshold: all essential criteria PASS AND composite >= 80.

Tier targets: 3-5 essential, 2-3 recommended, 1-2 aspirational. At least 3 distinct categories across all criteria.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences -- state the Scope Gatekeeper + Fills gap chain: the Scope Gatekeeper produces the authoritative gap register before aspirational authoring; the Fills gap field cites a specific entry from that register, making anti-overlap auditable at the criterion level rather than only at the protocol level), then SCOPE DECLARATION (retained in output as the tier scope record), then criteria ordered essential -> recommended -> aspirational (Dimension annotations and Fills gap fields retained; failure log and role headers omitted from output), then scoring section.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-05 -- Inertia Framing + Lifecycle Emphasis (Declared-Not-Placed + Placed-Not-Instantiated Competitors)

**Axes:** Inertia framing + lifecycle emphasis
**Hypothesis:** Prior rounds established a pattern: naming a specific near-excellent competitor that fails exactly one target criterion makes that criterion's requirement concrete rather than abstract. R6 V-01 named the aspirational-tier competitor (passes essential + recommended, lacks causal reference anchor). R8 V-01 named the Imprecise-Quality Protocol (passes C-08, fails C-18 by not enumerating dimensions). R9 V-05 named the PARTIAL-09 Rubric (achieves C-09 partial, fails C-15 on causal direction). V-05 extends the pattern to C-20 and C-21 with two sequential competitors, each scoped to its target criterion. Competitor 1: the Declared-Not-Placed Protocol -- achieves C-19 (anti-overlap stated somewhere in running prose) but fails C-20 because the constraint is not in a dedicated structural element and does not name threshold escalation as a prohibited form; an author can proceed past it without noticing. Competitor 2: the Placed-Not-Instantiated Protocol -- achieves C-20 (anti-overlap constraint placed in a labeled structural block with threshold prohibition) but fails C-21 because no per-criterion "Fills gap" field exists; the anti-overlap claim is auditable at the protocol level but not at the criterion level. Each competitor is named at the phase where its failure becomes relevant: Competitor 1 before aspirational criteria are authored (C-20 authoring moment), Competitor 2 at the aspirational criterion template (C-21 authoring moment). The prediction: C-20 strong via Competitor 1 framing + lifecycle phase gate naming the structural requirement; C-21 strong via Competitor 2 framing + required "Fills gap" field; combined as a lifecycle variation with two phase-specific competitor descriptions.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden. Your protocol has two competitors. Each satisfies C-01 through C-19. Each fails exactly one of the new target criteria for rubric v7.

**Competitor 1: The Declared-Not-Placed Protocol**

Its protocol states, somewhere in running prose: "aspirational criteria must go beyond what essential and recommended already require." This satisfies C-19 (anti-overlap stated). But the statement lives in running prose -- an author reading quickly may skip it or read past it. It does not appear in a dedicated structural element that must be completed before aspirational authoring begins. It also does not name threshold escalation as a prohibited form: "go beyond" is unspecified enough that an author may write an aspirational criterion that tests the same property as an essential at count >= 5 instead of >= 3, reasoning that "more" is "beyond." The Declared-Not-Placed Protocol earns C-19 but fails C-20 because: (1) the anti-overlap constraint is in prose, not a dedicated structural element; (2) threshold escalation is not explicitly prohibited.

Your protocol must go further: the anti-overlap constraint must appear in a dedicated structural element placed before aspirational authoring, and must explicitly name threshold escalation as a prohibited form.

**Competitor 2: The Placed-Not-Instantiated Protocol**

It places the anti-overlap constraint in a dedicated structural element before aspirational authoring. The element names threshold escalation as prohibited. This satisfies C-20. But when aspirational criteria are written, no per-criterion "Fills gap" field exists. The anti-overlap claim is correct at the protocol level and auditable there -- an evaluator can read the structural element and confirm the constraint is present. But an evaluator examining an individual aspirational criterion cannot confirm, from the criterion itself, what territory it fills. The criterion may be correct (not overlapping lower tiers) without making that claim inspectable per criterion. The Placed-Not-Instantiated Protocol earns C-20 but fails C-21 because: the anti-overlap instantiation is protocol-level, not criterion-level.

Your protocol must go further: each aspirational criterion must carry a required field naming the specific coverage gap it fills.

---

**Read the skill spec.**

**PHASE 1: FAILURE MODES**

Name failure modes. Assign severity: blocking, suboptimal, cosmetic.

```
F-NN | failure behavior | severity
```

Minimum: 3 blocking, 2 suboptimal.

DO NOT proceed to Phase 2 until the failure log contains at least 5 entries.

**PHASE 2: ESSENTIAL CRITERIA (3-5)**

From blocking failure modes. Each criterion: ID (C-NN), Text, Weight (essential), Category, Pass condition. Text states the downstream consequence of absence.

**PHASE 3: RECOMMENDED CRITERIA (2-3)**

From suboptimal failure modes. Pass conditions test degree, precision, or specificity. Annotate: **Dimension:** [degree | precision | specificity].

**PHASE 3.5: SCOPE CONSTRAINT BLOCK**

Before writing aspirational criteria, go beyond the Declared-Not-Placed Protocol.

The Declared-Not-Placed Protocol puts the anti-overlap constraint in prose. Your protocol puts it in a dedicated structural block, placed here -- between Phase 3 and Phase 4 -- that must be completed before any aspirational criterion is written.

```
SCOPE CONSTRAINT:

Covered by essential + recommended (combined):
  [List all essential and recommended criteria by C-NN with a one-line coverage
   summary. This is the complete set of territories already guarded.]

Threshold escalation is NOT aspirational (explicit prohibition):
  An aspirational criterion covering a territory already listed above -- even at a
  higher count threshold, a narrower pass band, a stricter count, or a more precise
  formulation of the same property -- is not aspirational. It is a tighter version
  of a covered criterion. Tighter is not new. Do not use threshold escalation to
  make a covered criterion "aspirational."

Uncovered gap zone:
  Gap G-01: [Specific property an output passing all Phase 2 + Phase 3 criteria
    could still lack. Must not be reachable by adjusting a threshold above.]
```

DO NOT proceed to Phase 4 until this block is complete and at least 1 gap (G-01) is named.

**PHASE 4: ASPIRATIONAL CRITERIA (1-2)**

Go beyond the Placed-Not-Instantiated Protocol.

The Placed-Not-Instantiated Protocol places the constraint (like Phase 3.5 above) but does not require a per-criterion gap citation. An evaluator can verify the protocol-level constraint but cannot verify, from any individual criterion, that the criterion falls in the uncovered gap zone.

Your aspirational criteria must carry a required per-criterion "Fills gap" field that cites the specific gap from Phase 3.5.

Each aspirational criterion:

- **ID**: C-NN
- **Text**: one sentence
- **Weight**: aspirational
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence with observable anchors
- **Fills gap**: [Cite the gap entry (G-NN) from Phase 3.5 that this criterion addresses. Must be non-blank. A blank "Fills gap" field means the criterion carries the Placed-Not-Instantiated Protocol's flaw: the anti-overlap claim is present at the protocol level but not inspectable at the criterion level. Blank = format error.]

After each aspirational criterion: confirm the cited gap is named in Phase 3.5. If the cited gap is not in Phase 3.5, the criterion fails anti-overlap verification regardless of its content.

**PHASE 5: SCORING**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

PASS = 1.0, PARTIAL = 0.5, FAIL = 0.
Golden threshold: all essential criteria PASS AND composite >= 80.

Tier targets: 3-5 essential, 2-3 recommended, 1-2 aspirational. At least 3 distinct categories.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences -- name the two competitors and state what each adds: where the Declared-Not-Placed Protocol puts the constraint in prose, yours puts it in a structural block with explicit threshold prohibition; where the Placed-Not-Instantiated Protocol stops at protocol-level placement, yours requires per-criterion "Fills gap" citation; together, placement and instantiation make anti-overlap enforceable at authoring time and auditable at criterion level), then SCOPE CONSTRAINT block (Phase 3.5, retained in output), then criteria ordered essential -> recommended -> aspirational (Dimension annotations and Fills gap fields retained; competitor descriptions and failure log omitted from output), then scoring section.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}
