Written to `simulations/quest/golden/review-customers-golden-2026-03-14.md`.

**What's in the file:**

- **Frontmatter**: score 100, status GOLDEN, rubric_final v5, rounds 4
- **Prompt body**: the simplified V-05 (651 words, 27% reduction from original 890) — conversational opening, tier assignment, per-persona reasoning with the Level 1/2/3 worked example, flag resolution block, scoring table, and all five post-persona sections (adoption blocked, positioning leaks, delight, aggregate + pattern synthesis, amendments)
- **What made it golden** (5 patterns):
  1. Narrative three-part chain tests traversal, not label presence
  2. Integrated aggregate + synthesis in one section prevents sub-feature decay at the task switch
  3. Anti-example closes C-17 without a rote-satisfiable template
  4. Three-level worked example makes sub-feature the mandatory floor with no escape clause
  5. Conversational register applied across all sections, not just per-persona blocks
- **Rubric summary**: all 22 criteria, weights, categories, and round-added lineage
EACH PERSON

Take each person through the feature one at a time. For each:

1. Header line (tier; flags will be added after scoring):
   [C-NN] [Name] ([Role]) | Tier: [tier]

2. Scores:
   - Usefulness [1-5]: [score]
   - Clarity [1-5]: [score]
   - Would-Adopt [1-5]: [score]

3. Rationale: 2-3 sentences naming what about the feature produced these scores.
   Level 1 (avoid): "This persona values efficiency, so the feature appeals to them."
     -- contextual, not causal; implicates the persona, not the feature.
   Level 2 (better): "The feature lacks offline support, which blocks this persona's workflow."
     -- causal but feature-level; names a gap without naming the mechanism.
   Level 3 (required): "The feature's sync architecture requires a live write connection at
     every step -- there is no local-cache or queue-and-flush mode -- which means any
     interruption aborts the workflow. For a persona who frequently works in low-connectivity
     environments, this is a hard stop, not a friction point."
     -- names the sub-feature mechanism (sync architecture's connection requirement), the
     specific constraint (no local-cache or queue-and-flush), the impact, and the severity.
   Write Level 3 for every persona.

4. Flag resolution -- check all three before advancing to the next person.
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

## What Made It Golden

**1. Narrative three-part chain (stakes / gap / mechanism) tests causal traversal, not label presence**
V-03 used explicit L1/L2/L3 labels and passed C-19, but label compliance and traversal are not
the same thing. V-05 replaced the label requirement with a narrative framing: "First, the
stakes... Then, the feature-level gap... Then, the sub-feature mechanism." This sequences the
reasoning as something a reader must follow end-to-end. The closing failure-mode instruction
("An entry that names only the sub-feature without establishing stakes and feature-level gap is
not a causal chain -- it is a named mechanism without context") names the skip pattern directly.
The result is traversal rather than checklist compliance.

**2. Integrated aggregate + pattern synthesis in one section prevents sub-feature decay during task switch**
V-04 treated WEIGHTED AGGREGATE and CROSS-PERSONA PATTERNS as separate sections. V-05 combined
them into WHAT DO THE NUMBERS SAY? -- compute the aggregate, then pivot directly to "Now look
across all twelve explanations for a named causal finding." This keeps the sub-feature
specificity frame active when the model transitions from scoring to synthesis, reducing the
regression to feature-level pattern observations that separate sections invite.

**3. Amendment chain parity via anti-example closes C-17 without a rigid template**
Rather than a per-item field template, V-05 closes C-17 with an explicit wrong-answer example
adjacent to the correct form: "If the chain said 'the sync architecture's hard write-connection
requirement,' the amendment is 'add a local-cache mode to the sync step' -- not 'improve offline
support.'" The same mechanism drove C-16 compliance in R3 V-02: showing what the wrong form
looks like makes the correct form unambiguous without a template that can be satisfied by rote.

**4. Three-level worked example makes sub-feature the named floor for every persona**
Rather than an abstract instruction, V-05 shows all three rationale levels side-by-side with
"why it fails" commentary for Level 1 and Level 2, then closes: "Write Level 3 for every
persona." There is no escape clause ("where possible" in V-01 and V-03 introduced the precision
regression). The worked example makes the distinction between feature-level and sub-feature
rationale inspectable, not inferential.

**5. Conversational register sustains depth across all 12 persona blocks and all post-persona sections**
"Work through this as a customer advisory panel" and "Take each person through the feature one
at a time" establish a social reasoning frame that resists the compression that flattens later
persona entries. R3 confirmed conversational register as the strongest depth predictor; V-05
applies it to all three R4 sections (per-persona rationale, blocker chains, aggregate synthesis)
without displacing R3's structural rules (prose-first, deferral prohibition, flag checks).

---

## Final Rubric Criteria Summary

**rubric_final**: review-customers-rubric-v5-2026-03-14.md
**22 criteria total** | 4 rounds

| ID   | Criterion                                               | Weight       | Category    | Added |
|------|---------------------------------------------------------|--------------|-------------|-------|
| C-01 | All 12 personas present and scored                      | essential    | correctness | v1    |
| C-02 | Weighted aggregate score computed (3x/2x/1x)            | essential    | correctness | v1    |
| C-03 | Adoption blockers identified                            | essential    | correctness | v1    |
| C-04 | Positioning leaks identified                            | essential    | coverage    | v1    |
| C-05 | Persona tier assignment stated                          | essential    | format      | v1    |
| C-06 | Delight signals identified                              | recommended  | coverage    | v1    |
| C-07 | Amendment guidance order: blockers then leaks           | recommended  | behavior    | v1    |
| C-08 | Per-persona rationale provided                          | recommended  | depth       | v1    |
| C-09 | Cross-persona pattern synthesis                         | aspirational | depth       | v1    |
| C-10 | Amend-to-score projection                               | aspirational | behavior    | v1    |
| C-11 | Inline blocker/leak flags at scoring                    | aspirational | reliability | v2    |
| C-12 | Hybrid table+prose format                               | aspirational | format      | v2    |
| C-13 | Causal rationale: feature gap named as mechanism        | aspirational | depth       | v2    |
| C-14 | Prose-first scoring order                               | aspirational | reliability | v3    |
| C-15 | Flag deferral prohibition                               | aspirational | reliability | v3    |
| C-16 | Causal precision: sub-feature specific                  | aspirational | depth       | v3    |
| C-17 | Amendment specificity: sub-feature targets              | aspirational | behavior    | v4    |
| C-18 | Cross-persona pattern at sub-feature resolution         | aspirational | depth       | v4    |
| C-19 | Three-tier causal chain traversal in blockers           | aspirational | depth       | v4    |
| C-20 | Explicit causal tier labeling in three-tier traversal   | aspirational | depth       | v5    |
| C-21 | L3-to-amendment traceability                            | aspirational | behavior    | v5    |
| C-22 | Cross-persona contrast framing: feature-level dismissal | aspirational | depth       | v5    |

**V-05 score**: 51 / 51 = 100 -- all essential, recommended, and aspirational criteria pass.
