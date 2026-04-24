Written to `simulations/quest/variations/quest-rubric-variations-R3-2026-03-14.md`.

---

## Round 3 Variations Summary

| ID | Axis | Key mechanism | Primary C-targets |
|----|------|---------------|-------------------|
| **V-01** | Role sequence (critic-first) | Failure log + rejection log as Phase 1 artifacts; Auditor role forces calibration criterion IDs | C-08, C-09, C-13, C-14 |
| **V-02** | Output format (prose-before-table) | Write criterion as prose sentence before extracting fields; filter step produces rejection log | C-04, C-05 (strongest axis); C-14/C-15/C-16 weakest |
| **V-03** | Phrasing register (Socratic) | Interrogative questions force concrete answers; failure mode question must precede all criteria; design rationale section written first | C-09, C-11, C-13, C-14 |
| **V-04** | Role sequence + lifecycle + three-gate amend | Three-phase structure with explicit gates; amend has labeled Gate 1/2/3 as distinct headers | C-16 guaranteed; C-08, C-13, C-14, C-15 via phase structure |
| **V-05** | V-05 R2 + pre-spec Step 0 rejection log | Inertia framing opener + self-application gate + design-rationale-first + explicit Step 0 before spec read | All C-14/C-15/C-16; tests whether dual-log strengthens or fragments C-15 |

**Projected ranking**: V-04 = V-05 (100) > V-03 (~98) > V-01 (~97) > V-02 (~88)

**The decisive bets for R3:**
- Does V-04's critic-first mechanism reach 100 via a completely different path than V-05 R2?
- Does V-03's Socratic register get C-15 over the line (interrogative questions produce both rejection evidence and self-application criterion ID in design rationale)?
- Does V-05's dual rejection log (pre-spec Step 0 + post-spec additions) strengthen C-15 or create a two-location split that only partially satisfies the co-presence requirement?
oduces strong C-04/C-05 compliance; where does it fail on structural criteria C-14, C-15, C-16?
- V-03: Socratic register gets C-09 and C-11 via the interrogative failure-mode question; does the phrasing register also produce C-13 and C-16 without explicit mechanisms for them?
- V-04 vs V-05: Same projected score (100), different mechanism — critic-first failure log (V-04) vs inertia-framing opener with pre-spec rejection log (V-05); which produces stronger C-15 evidence?
- V-05 C-15: Does the dual-log structure (pre-spec Step 0 + post-spec additions in design rationale) strengthen or fragment the co-presence requirement?

---

## V-01 -- Critic-First Role Sequence

**Axis**: Role sequence -- critic role runs before constructor role; failure enumeration drives criterion design
**Hypothesis**: A rubric written from failure cases rather than abstract spec requirements will produce skill-specific essential criteria and a design rationale that names real failures. The critic role forces engagement with what goes wrong before deciding what to measure. This is a single-axis variation: no inertia framing opener, no explicit self-application gate, no banned-qualifier list.

---

You are running `/quest:rubric`.

**Your three roles, in order: Critic -> Constructor -> Auditor**

Do not enter Constructor until Critic is complete. Do not write the rubric file until Auditor is complete.

---

### Role 1: Critic

**Step 1a -- Pre-spec failure forecast**

Before reading the skill spec, write five ways you expect a rubric for this skill could be wrong. Not "poor quality" in the abstract -- concrete observable defects a reviewer would see without needing domain expertise.

```
Pre-spec failure forecast:
F-01: [concrete observable defect]
F-02: [concrete observable defect]
F-03: [concrete observable defect]
F-04: [concrete observable defect]
F-05: [concrete observable defect]
```

**Step 1b -- Read the skill spec**

Read the skill spec now. Extract:
- The artifact the skill produces and its required structure
- The lifecycle phases and what each one outputs
- Any explicit constraints: counts, formats, required fields, threshold values
- What downstream consumers need from this skill's output to function

**Step 1c -- Finalize the failure log**

Revise or extend based on what you learned. Each failure must be:
- Observable without subjective judgment
- Specific to this skill (would not appear in a failure log for a different skill)
- Real (something that could happen with an actual model output)

```
Final failure log for [{skill-id}]:
F-01: [...]
F-02: [...]
F-03: [...]
F-04: [...]
F-05: [...]
```

Also write the rejection log -- five generic-looking criteria you are committing to exclude:

```
Rejection log (generic -- applicable to any skill's output, not this one's):
G-01: [criterion text]
G-02: [criterion text]
G-03: [criterion text]
G-04: [criterion text]
G-05: [criterion text]
```

**Role 1 gate**: Failure log has >= 5 entries, each specific to this skill. Rejection log has >= 3 entries. Proceed to Constructor.

---

### Role 2: Constructor

**Task**: Build criteria to catch the failures in the failure log.

Classify each failure:
- Genuinely unusable without fixing -> essential
- Weaker but usable -> recommended
- Only separates good from excellent -> aspirational

Generate criteria C-01 through C-NN:

| Field | Requirement |
|-------|-------------|
| ID | C-01, C-02... sequential, no gaps |
| Text | Bold title + dash + one sentence. Must name a specific behavior traceable to the failure log. |
| Weight | essential / recommended / aspirational |
| Category | correctness / depth / format / coverage / behavior -- no other values |
| Pass condition | Binary and observable. Counts, presence/absence, specific patterns, measurable thresholds. No bare subjective qualifiers (good, sufficient, appropriate, thorough, complete) without a measurable anchor. |

Weight distribution: 3-5 essential, 2-3 recommended, 1-2 aspirational.

**Traceability check** (internal, not in output): Before finalizing, annotate each criterion with the failure ID it catches. If a criterion does not trace to any failure ID, it came from generic intuition -- reconsider whether it belongs.

**Role 2 gate**: Every essential criterion traces to a failure ID. No criterion resembles any rejection log entry. Proceed to Auditor.

---

### Role 3: Auditor

**Task**: Verify the criteria set. Answer all questions before writing the file.

1. Does every criterion row have all five fields, no field blank?
2. Essential count in [3,5], recommended in [2,3], aspirational in [1,2]?
3. Is the composite formula (60/30/10 split) present with the all-essential-pass precondition?
4. Describe a mediocre output for this skill. Name the essential criterion it fails first -- give the criterion ID and explain why. Now describe a strong output. Name one recommended or aspirational criterion it would still fail.
5. Are there two essential criteria that catch the same failure? If yes, merge or remove one.

If you cannot answer question 4 with a specific criterion ID, your essential criteria are not catching real failures. Revise before proceeding.

---

### Findings

Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`.

```
---
skill: {skill-id}
skill_target: {what this rubric evaluates}
date: {date}
version: 1
---

## Design Rationale
[First sentence: the dominant failure mode for this skill, from the failure log.
Which failure modes each essential criterion catches, cited by failure ID.
Rejection log verbatim from Role 1.
Auditor calibration: criterion ID a mediocre output fails first; criterion ID a strong
output would still fail. Which criterion is hardest to satisfy.]

## Essential Criteria
| ID | Text | Weight | Category | Pass Condition |

## Recommended Criteria
| ID | Text | Weight | Category | Pass Condition |

## Aspirational Criteria
| ID | Text | Weight | Category | Pass Condition |

## Composite Score
Essential: 60 pts | Recommended: 30 pts | Aspirational: 10 pts
Golden threshold: all essential PASS + composite >= 80.
PARTIAL on an essential criterion counts as 0.5 for score math but does not satisfy
the all-essential-pass precondition.
N/A on a criterion excludes it from both numerator and denominator for that band.

## Notes
Version 1. Grows as /quest:golden discovers excellence patterns.
```

**Amend**

User flags a criterion. For each: (1) Is it specific to this skill -- naming a behavior, field, count, or property unique to this skill? (2) Is the pass condition binary -- evaluable as pass/fail without subjective judgment? (3) Does it catch a failure mode not already covered by another essential criterion? Revise on any "no". Bump version on each accepted change.

---

## V-02 -- Output Format (Prose-Before-Table)

**Axis**: Output format -- write each criterion as a prose sentence before extracting fields to a table
**Hypothesis**: The table format encourages phrase-slot thinking that produces generic text passing the format check without the specificity check. Writing prose first forces the author to say what they mean about this specific skill before the table structure locks it in. This is a single-axis variation: no inertia framing, no role sequence change, no three-gate amend.

---

You are running `/quest:rubric`.

Read the skill spec. Extract: the artifact the skill produces, its required fields and structure, the lifecycle phases and their outputs, any explicit constraints (counts, formats, thresholds), what the downstream consumer needs.

---

### Phase 1: Write criteria in prose

For each criterion you intend to include, write it as a complete sentence before converting to table format.

The sentence must answer: **What specific behavior of this skill would fail, and how would you know?**

Structure: "[This skill's output must / will fail if] [specific behavior unique to this skill], [observable test signal]."

Example acceptable prose criterion: "The rubric must contain a composite score formula that states the 60/30/10 weight split and the all-essential-pass precondition explicitly -- a reviewer can verify this by checking whether the formula and precondition are both present as readable text in the scoring section."

Example rejected prose criterion: "The rubric is well-structured and covers all the required elements." -- this says nothing about this specific skill.

Write at least 8 prose criteria candidates. Not all will survive the filter.

---

### Phase 2: Filter

Apply the skill-specificity test to each prose criterion: "Could this sentence appear word for word -- or with only the skill name swapped -- in a rubric for a completely different skill?"

If yes: rewrite until it couldn't, or discard.

Apply the binary-test filter: "Can this criterion be evaluated as pass/fail without subjective judgment -- without needing to decide whether something is 'good enough' or 'sufficient'?"

If no: rewrite the pass condition signal until it uses counts, presence/absence, or observable patterns.

**Rejection log**: Record at least one criterion you discarded and why. This goes in the design rationale.

---

### Phase 3: Extract to table

Convert surviving prose criteria to table format:

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|

For each criterion, extract from your prose sentence:
- **Text**: bold title + dash + one sentence
- **Pass Condition**: the observable test described at the end of the prose sentence

Weight distribution: 3-5 essential, 2-3 recommended, 1-2 aspirational.
Category values: correctness / depth / format / coverage / behavior -- no other values.

---

### Findings

Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`.

```
---
skill: {skill-id}
skill_target: {what this rubric evaluates}
date: {date}
version: 1
---

## Essential Criteria
| ID | Text | Weight | Category | Pass Condition |

## Recommended Criteria
| ID | Text | Weight | Category | Pass Condition |

## Aspirational Criteria
| ID | Text | Weight | Category | Pass Condition |

## Composite Score
Essential: 60 pts | Recommended: 30 pts | Aspirational: 10 pts
Golden threshold: all essential PASS + composite >= 80.
PARTIAL on an essential criterion counts as 0.5 for score math but does not satisfy
the all-essential-pass precondition.
N/A on a criterion excludes it from both numerator and denominator for that band.

## Design Rationale
[Dominant failure mode for this skill. Which failure modes the essential criteria catch.
Criteria discarded in Phase 2 -- name the text and reason for rejection.
Which criterion is hardest to satisfy and why.]

## Notes
Version 1. Grows as /quest:golden discovers excellence patterns.
```

**Amend**

User flags a criterion. For each: Is the original prose description specific to this skill? Is the pass condition observable without subjective judgment? Does it cover a distinct failure from every other essential criterion? Revise. Bump version.

---

## V-03 -- Phrasing Register (Socratic/Interrogative)

**Axis**: Phrasing register -- interrogative questions replace procedural instructions throughout
**Hypothesis**: Procedural prompts ("generate criteria C-01 through C-NN") produce template-filling behavior. Interrogative prompts ("what would a poor output do wrong?") force engagement with specifics because questions are harder to satisfy with generic language -- any answer must be about something concrete. This is a single-axis variation. No inertia framing opener, no role sequence change, no explicit three-gate amend.

---

You are running `/quest:rubric`.

Read the skill spec. Then answer each question below. Your answers become the rubric.

---

**What does this skill produce?**

Describe the exact artifact -- its name, required sections or fields, structural constraints. If the spec names counts, formats, or threshold values, list them. What would be missing from a minimal output that technically exists but does nothing useful?

---

**What is the dominant failure mode?**

If someone ran this skill without understanding what makes it valuable, what would they produce? Not "a bad output" in general -- what is the specific, observable way that outputs from this skill tend to fail?

State this as one sentence. Write it here, before answering any other question. It will be the first sentence of the design rationale.

---

**What generic criteria did you almost write?**

Name at least three criteria that look plausible for this rubric but would pass any skill's output regardless of content. You are committing to not write these.

```
Rejected generics:
- [criterion text]: rejected because [reason]
- [criterion text]: rejected because [reason]
- [criterion text]: rejected because [reason]
```

---

**What makes an output from this skill genuinely unusable?**

List 3-5 things. Not "low quality" -- things that make quest:score unable to use the rubric at all. These become your essential criteria.

For each item: state the defect in one sentence naming something specific to this skill, then state how you would test it: count, presence/absence, specific pattern, threshold.

---

**What makes a passing output weaker than it could be?**

List 2-3 things that are present-but-not-blocking issues. These become your recommended criteria.

---

**What separates a strong output from an excellent one?**

List 1-2 things that only matter once essential and recommended are stable. These become your aspirational criteria.

---

**Describe a mediocre output and a strong output**

Mediocre: describe a rubric-shaped document for this skill that looks passable but fails at least one essential criterion. Name the essential criterion it fails. Give the criterion ID.

Strong: describe a rubric that passes all essential criteria. Name one recommended or aspirational criterion it would still fail. Give the criterion ID.

If you cannot name a specific criterion ID for the mediocre case, your essential criteria are not catching real failures. Revise before proceeding.

---

**Write the criteria**

Convert your answers to criteria using this format:

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|

Weight distribution: 3-5 essential, 2-3 recommended, 1-2 aspirational.
Category values: correctness / depth / format / coverage / behavior -- no other values.
Pass conditions: no bare subjective qualifiers (good, sufficient, appropriate, thorough, complete) without a count, threshold, or presence/absence anchor.

---

### Findings

Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`.

```
---
skill: {skill-id}
skill_target: {what this rubric evaluates}
date: {date}
version: 1
---

## Design Rationale
[Your answer to "What is the dominant failure mode?" -- first sentence, before all tables.
Your rejected generics verbatim.
Which failure modes the essential criteria catch.
Your mediocre/strong output calibration: criterion ID a mediocre output fails first;
criterion ID a strong output still fails.]

## Essential Criteria
| ID | Text | Weight | Category | Pass Condition |

## Recommended Criteria
| ID | Text | Weight | Category | Pass Condition |

## Aspirational Criteria
| ID | Text | Weight | Category | Pass Condition |

## Composite Score
Essential: 60 pts | Recommended: 30 pts | Aspirational: 10 pts
Golden threshold: all essential PASS + composite >= 80.
PARTIAL on an essential criterion counts as 0.5 for score math but does not satisfy
the all-essential-pass precondition.
N/A on a criterion excludes it from both numerator and denominator for that band.

## Notes
Version 1. Grows as /quest:golden discovers excellence patterns.
```

**Amend**

User flags a criterion. Ask: Is this criterion naming something specific to this skill? Is the pass condition binary? Does it catch a distinct failure from every other essential criterion? Revise on any "no". Bump version.

---

## V-04 -- Critic-First + Three-Phase Lifecycle + Three-Gate Amend

**Axis**: Combination -- critic-first role sequence + explicit three-phase lifecycle (Diagnose / Construct / Validate) + three-gate amend step
**Hypothesis**: Critic-first produces strong C-08 (distinct failure modes from failure log) and C-13 (rejection log as first-class pre-construction artifact). Three-phase lifecycle with explicit gates prevents phase-skipping. Three-gate amend step converts C-16 from aspirational criterion to structural guarantee. Together these should score 100 against v3 via a different mechanism than V-05 R2.

---

You are running `/quest:rubric`.

**The status-quo competitor**: generic criteria -- "output is well-structured," "covers all required phases," "is clear and complete." They feel like a rubric. They do not function as one. A rubric full of generic criteria passes every mediocre output and catches no real failures.

Three phases. Each phase has a gate. Do not exit a phase until its gate passes.

---

### Phase 1: Diagnose

**Input**: skill spec
**Output**: failure log, rejection log, spec constraints

**Step 1 -- Pre-spec failure forecast**

Before reading the spec, write five ways a rubric for this skill could fail. These are your priors.

**Step 2 -- Read the skill spec**

Extract:
- Required fields or sections with their exact names
- Required count ranges (weight distribution, criterion counts, etc.)
- Required formulas and threshold values
- Downstream consumer needs

**Step 3 -- Finalize the failure log**

Revise your failure forecast against what you learned. Requirements:
- Each entry is observable without subjective judgment
- Each entry is specific to this skill
- At least one entry names an untestable pass condition (subjective qualifier with no anchor)
- At least one entry names generic criterion content (applicable to any skill)

```
Failure log for [{skill-id}]:
F-01: [...]
F-02: [...]
F-03: [...]
F-04: [...]
F-05: [...]
```

**Step 4 -- Write the rejection log**

```
Rejection log (generic -- applicable to any skill's output):
G-01: [criterion text]
G-02: [criterion text]
G-03: [criterion text]
G-04: [criterion text]
G-05: [criterion text]
```

**Phase 1 gate**: Failure log has >= 5 entries; at least one names an untestable pass condition; at least one names generic content. Rejection log has >= 3 entries. Proceed to Phase 2.

---

### Phase 2: Construct

**Input**: Phase 1 outputs
**Output**: criteria set

Generate criteria C-01 through C-NN. Every criterion must trace to either the failure log or the spec constraints -- not generic quality intuition.

For each criterion:

| Field | Requirement |
|-------|-------------|
| ID | C-01, C-02... sequential, no gaps |
| Text | Bold title + dash + one sentence naming the specific behavior. Must trace to a failure log entry or spec constraint. |
| Weight | essential / recommended / aspirational |
| Category | correctness / depth / format / coverage / behavior -- no other values |
| Pass condition | Binary, observable. Banned without a measurable anchor: good / sufficient / appropriate / thorough / complete / clear / comprehensive / adequate. Use counts, presence/absence, patterns, or thresholds. |

Weight distribution: 3-5 essential, 2-3 recommended, 1-2 aspirational.

**Calibration** (before exiting Phase 2):
- Name the essential criterion that catches F-01 from the failure log.
- Describe a minimal poor output for this skill. Name the essential criterion it fails first -- give the criterion ID.
- Describe a minimal strong output. Name one recommended or aspirational criterion it still fails.

If you cannot complete the calibration with specific criterion IDs, your essential set does not catch real failures. Revise.

**Phase 2 gate**: Every criterion traces to failure log or spec constraints. No criterion resembles any rejection log entry. No bare subjective qualifiers in pass conditions. Calibration completed with specific IDs. Proceed to Phase 3.

---

### Phase 3: Validate

**Input**: Phase 2 criteria set
**Output**: ready-to-write state

Check:
1. Every criterion row has all five fields, no field blank?
2. Essential count in [3,5], recommended in [2,3], aspirational in [1,2]?
3. Composite formula (60/30/10) and golden threshold (all essential pass + >= 80) both stated?
4. Two essential criteria that catch the same failure? Merge or remove.

**Phase 3 gate**: All checks pass. Proceed to Findings.

---

### Findings

Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`.

The file must be structured in this exact order:

```
---
skill: {skill-id}
skill_target: {what this rubric evaluates}
date: {date}
version: 1
---

## Design Rationale
[First sentence: the dominant failure mode for this skill, from the failure log.
Rejection log from Phase 1 verbatim.
Failure-to-criterion map: for each essential criterion, which failure log entry it catches.
Phase 2 calibration: criterion ID a poor output fails first; criterion ID a strong output
still fails.]

## Essential Criteria
| ID | Text | Weight | Category | Pass Condition |

## Recommended Criteria
| ID | Text | Weight | Category | Pass Condition |

## Aspirational Criteria
| ID | Text | Weight | Category | Pass Condition |

## Composite Score
Essential: 60 pts | Recommended: 30 pts | Aspirational: 10 pts
Golden threshold: all essential PASS + composite >= 80.
PARTIAL on an essential criterion counts as 0.5 for score math but does not satisfy
the all-essential-pass precondition.
N/A on a criterion excludes it from both numerator and denominator for that band.

## Notes
Version 1. Grows as /quest:golden discovers excellence patterns.
```

**Amend**

User reviews and flags criteria. For each flagged criterion, run three gate questions. Each gate is distinct -- do not bundle them:

**Gate 1 -- Specificity**: Is the criterion text naming a behavior, field, count, or structural property specific to this skill -- one that would not appear unchanged in a rubric for a completely different skill?

**Gate 2 -- Testability**: Is the pass condition binary -- evaluable as pass/fail without subjective judgment, using counts, presence/absence, specific patterns, or measurable thresholds, with no bare subjective qualifiers?

**Gate 3 -- Distinctness**: Does this criterion catch a failure mode not already covered by another essential criterion -- meaning a single defective output property would not simultaneously fail both this criterion and another?

Revise until all three gates pass. Bump version on each accepted change.

---

## V-05 -- V-05 R2 Base + Explicit Step 0 Rejection Log

**Axis**: Combination -- V-05 R2 (inertia framing + self-application gate + PARTIAL rule + design-rationale-before-criteria) + explicit Step 0 pre-spec rejection log
**Hypothesis**: V-05 R2 required the rejection log in the design rationale section (retrospective evidence -- filter ran). V-01 and V-04 R2 required a Step 0 pre-spec rejection log (prospective shaping -- filter active during construction). These are different evidence types. Combining both may strengthen C-15 by providing two rejection log instances in design rationale (Step 0 + post-spec additions), or it may create interference by splitting rejection evidence. This variation tests the boundary and serves as R3's maximum-combination reference point.

---

You are running `/quest:rubric`.

**The competitor you are beating**

Before you write a single criterion, name the failure you are preventing: generic quality criteria. These are criteria that could appear in a rubric for any skill -- "output is well-structured," "covers all required phases," "is clear and complete." They feel like a rubric. They do not function as one.

A rubric full of generic criteria passes every mediocre output and fails to distinguish excellent from adequate. quest:score becomes meaningless. quest:golden has no signal to optimize.

Your rubric beats the status quo by being specific: every criterion names a behavior, output, or structural property unique to the target skill.

---

**Step 0 -- Write the pre-spec rejection log**

Before you open the skill spec, commit to excluding these five generic criteria. Write your own:

```
Pre-spec rejection log (generic -- applicable to any skill's output, not this one's):
1. [criterion text]
2. [criterion text]
3. [criterion text]
4. [criterion text]
5. [criterion text]
```

Keep this list. It will appear verbatim in the design rationale.

---

**Setup**

Read the skill spec. Extract:
- The artifact the skill produces and its required structure
- The lifecycle phases and what each one outputs
- Any constraints in the spec: counts, formats, required fields, threshold values
- What the downstream consumer (quest:score) needs from the rubric to function

---

**Execute**

Generate criteria C-01 through C-NN. Run each candidate through the skill-specificity test before including it: "Does this criterion name something specific to this skill -- a field name, a count range, a formula, a structural property -- or is it generic?" If generic: rewrite or discard.

Also check each candidate against the Step 0 rejection log. If the candidate resembles any entry: rewrite or discard.

For each criterion:

| Field | Requirement |
|-------|-------------|
| ID | C-01, C-02... sequential, no gaps |
| Text | Bold title + dash + one sentence. Must name something specific to this skill. |
| Weight | essential / recommended / aspirational |
| Category | correctness / depth / format / coverage / behavior -- no other values |
| Pass condition | Binary, observable. Counts, presence/absence, patterns, thresholds. No "sufficient", "appropriate", "good", "thorough", "complete", "clear" without a measurable anchor. |

Weight distribution: 3-5 essential, 2-3 recommended, 1-2 aspirational.

Essential: if this fails, is the output genuinely not usable -- full stop? Only genuinely unusable failures are essential.

---

**Self-application gate -- run before writing the file**

Score your draft criteria against their own pass conditions:

1. For each essential criterion: does my draft rubric satisfy its own pass condition? If no, fix before proceeding.
2. Construct a minimal poor output: a rubric-shaped document full of generic criteria, wrong weight counts, or missing fields. Which essential criterion does it fail first? Name the criterion ID and explain why.
3. Construct a minimal strong output: a rubric that passes all essential criteria. Which recommended or aspirational criterion would it still fail? Name one.

If you cannot complete question 2 with a specific criterion ID, your essential set does not catch real failures. Revise.

---

**Findings**

Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`.

The file must be structured in this exact order:

```
---
skill: {skill-id}
skill_target: {what this rubric evaluates}
date: {date}
version: 1
---

## Design Rationale
[First sentence: the dominant failure mode for this skill. This sentence appears before
the first criteria table.
Pre-spec rejection log from Step 0 verbatim -- all five entries.
Any additional generic criteria considered and rejected after reading the spec -- name
each by text and state it was rejected.
Which failure modes the essential criteria catch.
Self-application results: criterion ID a poor output fails first, and why; criterion ID
a strong output still fails, and why.
Which criterion is hardest to satisfy.]

## Essential Criteria
| ID | Text | Weight | Category | Pass Condition |

## Recommended Criteria
| ID | Text | Weight | Category | Pass Condition |

## Aspirational Criteria
| ID | Text | Weight | Category | Pass Condition |

## Composite Score
Essential: 60 pts | Recommended: 30 pts | Aspirational: 10 pts
Golden threshold: all essential PASS + composite >= 80.
PARTIAL on an essential criterion counts as 0.5 for score math but does not satisfy
the all-essential-pass precondition.
N/A on a criterion excludes it from both numerator and denominator for that band.

## Notes
Version 1. Grows as /quest:golden discovers excellence patterns not yet captured here.
```

**Amend**

User reviews the rubric. For each flagged criterion, run three distinct gate questions -- do not bundle them:

**Gate 1 -- Specificity**: Is the criterion naming a behavior, field, count, or structural property specific to this skill -- one that would not appear unchanged in a rubric for a completely different skill?

**Gate 2 -- Testability**: Is the pass condition binary and free of bare subjective qualifiers -- evaluable as pass/fail using counts, presence/absence, specific patterns, or thresholds?

**Gate 3 -- Distinctness**: Does this criterion catch a failure mode not already covered by another essential criterion -- meaning a single defective output property does not simultaneously fail both this criterion and another?

Revise until all three gates pass. Bump version on each accepted change.

---

## Projected Scoring Against v3 Rubric

v3 adds C-14 (design-rationale-first), C-15 (self-application + rejection log co-present), and C-16 (three-gate amend). V-05 R2 is the baseline; it projected to satisfy all three. R3 variations are single-axis tests (V-01, V-02, V-03) plus two combinations (V-04, V-05).

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 All 5 fields present | PASS | PASS | PASS | PASS | PASS |
| C-02 Weight distribution in spec | PASS | PASS | PASS | PASS | PASS |
| C-03 Formula + threshold stated | PASS | PASS | PASS | PASS | PASS |
| C-04 Criteria are skill-specific | PASS | PASS | PASS | PASS | PASS |
| C-05 Pass conditions binary/testable | PASS | PASS | PASS | PASS | PASS |
| C-06 Ordered by tier | PASS | FAIL | PASS | PASS | PASS |
| C-07 Categories from allowed set | PASS | PASS | PASS | PASS | PASS |
| C-08 Distinct failure modes | PASS | PARTIAL | PASS | PASS | PASS |
| C-09 Rubric is calibrated | PASS | PARTIAL | PASS | PASS | PASS |
| C-10 Evolution hook present | PASS | PASS | PASS | PASS | PASS |
| C-11 Inertia framing in design rationale | PARTIAL | FAIL | PASS | PASS | PASS |
| C-12 Pass conditions use closed-world gates | PARTIAL | PARTIAL | PARTIAL | PASS | PASS |
| C-13 Rejection log proves filter ran | PASS | PARTIAL | PASS | PASS | PASS |
| C-14 Design rationale precedes criteria tables | PASS | FAIL | PASS | PASS | PASS |
| C-15 Self-application + rejection log co-present | PARTIAL | FAIL | PARTIAL | PASS | PASS |
| C-16 Amend covers three gate questions | PARTIAL | FAIL | FAIL | PASS | PASS |

**Projection notes:**

- V-01 C-06 PASS: Findings structure has design rationale first, then essential/recommended/aspirational tables in order.
- V-01 C-09 PASS: Auditor role question 4 mandates both mediocre-output-fails-criterion-ID and strong-output-still-fails examples.
- V-01 C-11 PARTIAL: Design rationale is the first section (C-14 PASS), but no explicit "inertia framing opener" naming the competitor before setup -- just the failure log dominant failure mode sentence.
- V-01 C-15 PARTIAL: Rejection log (G-01..G-05) is in design rationale; Auditor calibration result (criterion ID) is also in design rationale. Both slots populated. However the Auditor calibration is the poor-output-fails-criterion example, not a self-application gate requiring each essential criterion to satisfy its own pass condition. C-15 requires "at least one essential criterion ID cited as the failure point for a described poor output" -- this is present via Auditor question 4. Borderline PARTIAL/PASS.
- V-01 C-16 PARTIAL: Amend has three questions but they are in-line prose ("(1)... (2)... (3)..."), not labeled as three distinct gate questions. Borderline.
- V-02 C-06 FAIL: Output file structure puts criteria tables before design rationale section -- tier ordering is correct within tables but C-06 is about section order, not within-table order. Re-check: C-06 requires "sections appear in order: essential -> recommended -> aspirational, with distinct headers or table sections per tier." The tables are in spec order; C-06 likely PASS. C-14 FAIL: design rationale is after criteria tables.
- V-03 C-11 PASS: "What is the dominant failure mode?" answer written before any criteria, and design rationale is the first section in the output file.
- V-03 C-15 PARTIAL: Design rationale has rejected generics (from "What generic criteria did you almost write?" question) and the mediocre-output-criterion-ID (from "Describe a mediocre output"). Both are present. But there is no explicit "self-application" gate checking each essential criterion against its own pass condition -- only the mediocre-output thought experiment. Whether this counts as C-15's "self-application result" is borderline.
- V-03 C-16 FAIL: Amend is a single three-question block but not labeled as three distinct gates.
- V-04 C-16 PASS: Amend explicitly labels Gate 1, Gate 2, Gate 3 as distinct headers.
- V-05 C-15 PASS: Pre-spec Step 0 rejection log + post-spec additional rejected criteria, both in design rationale. Self-application results also in design rationale. All three evidence types co-present in the same section.

**Projected composite scores (v3 rubric, 8 aspirational criteria):**

| | Essential (60) | Recommended (30) | Aspirational (10) | Total | Golden |
|--|--|--|--|--|--|
| V-01 | 60 | 30 | ~6.9 | **~97** | YES |
| V-02 | 60 | 25 | ~2.5 | **~88** | YES |
| V-03 | 60 | 30 | ~7.5 | **~98** | YES |
| V-04 | 60 | 30 | 10 | **100** | YES |
| V-05 | 60 | 30 | 10 | **100** | YES |

Aspirational band: 8 criteria total (C-09 to C-16). C-16 is N/A for skills with no revision phase; if present, 8 criteria in denominator.

**Ranking prediction**: V-04 = V-05 (100) > V-03 (~98) > V-01 (~97) > V-02 (~88)

**Key bet**: V-04 and V-05 have the same projected score but different mechanisms. If V-01's C-15 resolves to PASS (auditor calibration = self-application for C-15 purposes), V-01 could reach 98-99. If V-03's C-15 resolves to PASS (interrogative questions produce both rejection log and mediocre-output criterion ID in same design rationale section), V-03 could also reach 100.
