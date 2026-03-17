---

## Simplified prompt body

```
You are running /review:customers. Work through this as a customer advisory panel. The output
structure matters: reason through each persona in prose first, then compile all results into a
scoring table afterward. The prose comes before the table -- always.
```
*(opening trimmed — 38 words vs 77)*

The remaining sections are preserved structurally with targeted cuts throughout. See the file for the full body.

---

## Simplification report

| # | What was removed | Words | Why |
|---|-----------------|-------|-----|
| 1 | "The goal is to understand what twelve different people would actually think..." | 21 | Purpose implied by "customer advisory panel" + scoring structure |
| 2 | "because the table should reflect genuine reasoning, not a scaffold..." | 17 | Justification for a rule already stated; rule stands alone |
| 3 | "Before you invite anyone into the room, make sure you know what you are showing them." | 16 | Redundant restatement of "Read the spec... Understand what the feature does" |
| 4 | Merge rationale instruction (net) | 7 | Two sentences collapsed to one without loss |
| 5 | Level 2 annotation: "'Lacks offline support' implicates the whole feature." | 9 | "Not actionable" already carries the verdict |
| 6 | Level 3 annotation specifics: "(sync step design), the specific constraint..." | 12 | Examples already in the quote; annotation restated them |
| 7 | "The goal is a rationale that a reader can traverse..." | 25 | Restates the three-part chain; the anti-pattern sentence below is stronger |
| 8 | "This is what makes the blocker a blocker and not just a limitation." | 13 | Motivational aside; stakes instruction already captures it |
| 9 | "Ask yourself: is there a specific design decision or capability constraint..." | 21 | Merged into "named causal finding: a single sub-feature property..." |
| 10 | "If so, that is the highest-leverage finding in this review..." | 28 | Motivational extension; instruction + worked example sufficient |
| 11 | "Explain how a single design intervention at that sub-feature would affect the cluster." | 13 | Pattern example demonstrates it; "State what it implies" covers it |
| 12 | "The causal chain that drove the score drives the fix." | 10 | Slogan. The two preceding sentences make the rule explicit |
| 13 | "The table is a summary of reasoning already done -- not a scoring step." | 13 | Prose-first rule established twice elsewhere |
| 14 | "Any score of 5 anywhere is worth pausing on." | 9 | "Group any 5s by dimension" already acts on 5s |
| 15 | Frontmatter tracking fields (register, output_format, c14–c19 fields) | 18 | Quest artifact metadata, not behavioral instruction |

**Total removed: ~241 words**

### Essential criteria: all still pass — YES

C-01 (all 12 personas), C-02 (3x/2x/1x weighted aggregate), C-03 (adoption blockers), C-04 (positioning leaks), C-05 (tier assignment) — all instruction text preserved.

All key V-05 aspirational mechanisms (C-14 prose-first, C-15 deferral prohibition, C-16 sub-feature worked example, C-17 amendment targets, C-18 cross-persona pattern, C-19 three-tier chain) are intact.

```json
{"simplified_word_count": 651, "original_word_count": 890, "all_essential_still_pass": true}
```
xt person.
This check is not optional and cannot be deferred:

  Is this person in the primary tier AND Would-Adopt < 3?
  If yes: add [BLOCKER] to their header line now, before writing the next person's name.

  Is this person in the non-target tier AND (Useful >= 4 OR Would-Adopt >= 3)?
  If yes: add [LEAK] to their header line now, before writing the next person's name.

  Does any score equal 5?
  If yes: add [DELIGHT: dimension] to their header line now, before writing the next person's name.

You may not write the next person's name until the current person's flags are resolved.
A flag that only appears in a summary section later -- and not in the entry where the score was
assigned -- was deferred, not applied. Deferral is not the same as inline flagging.

Do this for all twelve. Write all twelve prose entries before writing any part of the table.

---

COMPILE THE SCORING TABLE

After reasoning through all 12 personas in prose, compile the results into a summary table.
Every row is required. Scores must match the prose entries above.

| ID   | Name            | Role        | Tier       | Useful | Clarity | W-Adopt |
|------|-----------------|-------------|------------|--------|---------|---------|
| C-01 | Maria Chen      | Maker       | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-02 | James Okafor    | Builder     | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-03 | Priya Nair      | Strategist  | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-04 | Tom Bergstrom   | Operator    | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-05 | Aisha Mensah    | Researcher  | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-06 | Carlos Reyes    | Designer    | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-07 | Lin Wei         | Analyst     | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-08 | Sophie Dubois   | Manager     | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-09 | Raj Patel       | Advocate    | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-10 | Yuki Tanaka     | Evaluator   | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-11 | Elena Vasquez   | Buyer       | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-12 | Frank Hoffmann  | Regulator   | [tier]     | [1-5]  | [1-5]   | [1-5]   |

All 12 rows and all tier labels required.

---

IS ADOPTION BLOCKED?

Look at the would-adopt scores for your primary-audience personas. Did any score below 3?

If yes, write each blocker as a three-part case that a reader can follow from the persona's
situation to the exact mechanism blocking them:

  First, the stakes: what goal, workflow constraint, or responsibility makes this persona care?

  Then, the feature-level gap: what does the feature as a whole fail to support? State it plainly
  before naming the mechanism. This is the bridge -- without it, the sub-feature name is a
  technical observation floating without context.

  Then, the sub-feature mechanism: which specific capability, threshold, design decision, or
  workflow step in the feature is the reason the gap exists? Name it as the amendment target.
  This is where the fix lives -- specific enough to assign to a design decision.

Write this three-part chain for at least one blocker. An entry that names only the sub-feature
(the third part) without establishing stakes and feature-level gap is not a causal chain -- it
is a named mechanism without context.

If no primary persona scored below 3: "No adoption blockers." Do not skip the check.

---

IS THE POSITIONING LEAKING?

Check your non-target personas. Did any score surprisingly high on usefulness or would-adopt?
Or does their explanation show confusion about whether this feature is meant for them?
Name each leak by ID and describe the sub-feature or framing element causing it: what specific
property of how the feature is named, described, or scoped made this non-target persona think
it might be for them?

If no leaks: "No positioning leaks." Do not skip the check.

---

WHO IS DELIGHTED?

Group any 5s by dimension. For each: which sub-feature property produced this reaction?
What would you amplify in messaging, onboarding, or positioning?

If there are no 5s: "No delight signals."

---

WHAT DO THE NUMBERS SAY IN AGGREGATE?

Primary personas carry 3x the weight of non-target; secondary carries 2x. Compute weighted
averages for each dimension and an overall composite on a 1-5 scale. Show how you weighted it --
state the weight per tier and count per tier.

Now look across all twelve explanations for a named causal finding: a single sub-feature property
that explains a consistent reaction across a cluster of personas -- not a description of the
score distribution.

The difference between a pattern and a distribution observation:
  Distribution observation: "Role cluster X scores low on clarity."
  Pattern with feature-level cause: "Role cluster X scores low on clarity because the feature
    lacks documentation." (Names the gap; not the mechanism.)
  Pattern with sub-feature cause: "Role cluster X scores low on clarity because the feature's
    onboarding flow shows the configuration UI before the concept is introduced -- personas who
    have not seen the concept before see options without context." (Names the sub-feature
    mechanism: the onboarding flow's sequencing, not "lacks documentation".)

Name the sub-feature mechanism. State what it implies for the team.

---

WHAT SHOULD CHANGE?

Address adoption blockers first. For each blocked primary persona, the amendment target is the
sub-feature mechanism from their three-part chain -- the same one you named as L3. Project the
score movement:
"Fixing [specific sub-feature property] for [ID] likely lifts primary Would-Adopt by ~[delta],
moving weighted composite from [current] to approximately [current + effect]."

The amendment target must be the sub-feature mechanism, not a restatement of the feature-level
gap. If the chain said "the sync architecture's hard write-connection requirement," the amendment
is "add a local-cache mode to the sync step" -- not "improve offline support."

Then address positioning leaks. What specific sub-feature or framing element is causing non-target
personas to be attracted or confused? Name the change.

Then amplify delight signals. Which sub-feature property is already landing? How do you lean into
it in messaging or onboarding?

---

Write the artifact to simulations/review/customers/{topic}-customers-{date}.md.
Frontmatter: skill: review-customers, topic, date, input.
```

---

## Simplification Report

### What was removed and why

| # | Removed text | Words | Reason |
|---|-------------|-------|--------|
| 1 | "The goal is to understand what twelve different people would actually think, feel, and decide if they encountered this feature today." | 21 | Purpose implied by "customer advisory panel" + scoring structure. No behavior change. |
| 2 | "-- because the table should reflect genuine reasoning, not a scaffold that reasoning fits into after the fact" | 17 | Justification for a rule already stated. Rule stands without it. |
| 3 | "Before you invite anyone into the room, make sure you know what you are showing them." | 16 | Redundant restatement of "Read the spec... Understand what the feature does." |
| 4 | Merge rationale instruction sentences (net) | 7 | "explaining what happened. The explanation must name..." collapsed to "naming the..." without information loss. |
| 5 | Level 2 annotation: "'Lacks offline support' implicates the whole feature." | 9 | "Not actionable" already carries the verdict. |
| 6 | Level 3 annotation: "(sync step design), the specific constraint (no local-cache or queue-and-flush), the impact, and" | 12 | Specific examples are already in the quote itself; annotation became generic summary. |
| 7 | "The goal is a rationale that a reader can traverse from 'why this persona is affected' to 'exactly what to change' without inferring missing steps." | 25 | Restates the three-part chain in different words. The anti-pattern sentence is stronger and sufficient alone. |
| 8 | "This is what makes the blocker a blocker and not just a limitation." | 13 | Motivational aside. The stakes instruction already captures this. |
| 9 | "Ask yourself: is there a specific design decision or capability constraint that multiple personas are reacting to in the same way?" | 21 | Merged into the opening instruction ("named causal finding: a single sub-feature property that explains a consistent reaction..."). |
| 10 | "If so, that is the highest-leverage finding in this review -- a single sub-feature cause that explains a cluster's scores means one intervention can lift all of them simultaneously." | 28 | Motivational extension. The instruction + worked example are sufficient. |
| 11 | "Explain how a single design intervention at that sub-feature would affect the cluster." | 13 | The pattern example already demonstrates this. "State what it implies for the team" covers it. |
| 12 | "The causal chain that drove the score drives the fix." | 10 | Summary slogan. The two preceding sentences make the rule explicit. |
| 13 | "The table is a summary of reasoning already done -- not a scoring step." | 13 | Prose-first rule established twice elsewhere. |
| 14 | "Any score of 5 anywhere is worth pausing on." | 9 | "Group any 5s by dimension" already acts on 5s. |
| 15 | Frontmatter mechanism tracking fields (register, output_format, c14-c19 fields) | 18 | Artifact metadata for the quest system, not behavioral instruction. |

**Total removed: ~241 words**

### Essential criteria -- all still pass

| Criterion | Still passes? |
|-----------|---------------|
| C-01 All 12 personas present and scored | YES |
| C-02 Weighted aggregate computed (3x/2x/1x) | YES |
| C-03 Adoption blockers identified | YES |
| C-04 Positioning leaks identified | YES |
| C-05 Persona tier assignment stated | YES |

### Key aspirational criteria (V-05 mechanisms) -- all preserved

| Criterion | Mechanism |
|-----------|-----------|
| C-14 Prose-first | "prose comes before the table -- always" + close of persona section |
| C-15 Flag deferral prohibition | "Deferral is not the same as inline flagging" + cannot-advance rule |
| C-16 Sub-feature specificity | Level 1/2/3 worked example intact, "Write Level 3 for every persona" |
| C-17 Amendment sub-feature targets | "the same one you named as L3" + worked example |
| C-18 Cross-persona pattern sub-feature | Three-level pattern example (distribution/feature/sub-feature) intact |
| C-19 Three-tier blocker chain traversal | Stakes/feature-level gap/sub-feature structure + bridge explanation |
