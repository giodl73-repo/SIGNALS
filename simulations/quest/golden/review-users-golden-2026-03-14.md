`review-users-golden-2026-03-14.md` written.

---

**What was extracted and why:**

- **Prompt body**: V-05 (R4 winning variation, composite 100), with simplification applied (313 words removed, PASS)
- **Simplification applied**: 11 rules — removed explicit tag-rule sentence from blockquotes (examples alone suffice), collapsed redundant meta-explanations in Step 3 brackets, kept only Sam's Step 1 example (model generalizes the pattern), tightened table preamble, pruned amend loop explanatory sentences, condensed persona-conflicts instruction to two sentences
- **All essential criteria preserved**: C-01 through C-05 unaffected

**Five golden patterns:**

| Pattern | Criterion | Effect |
|---------|-----------|--------|
| Numbered steps | C-19 | Workaround-before-brief becomes a sequence rule, not a convention |
| Domain-matched per-section blockquotes | C-20 | Role-appropriate prototype at each persona boundary |
| Workaround-first + gap-statement amend | C-21 | Forces workaround-replacement framing, not artifact annotation |
| Pre-committed table + Step 1 expansion | C-11/C-14 | Closed chain: table -> persona -> amend |
| Two correct examples per blockquote | C-17/C-20 | Deeper tag grounding across 5 personas + 1500+ token span |
not:" gap-statement field, then the verbatim quote, then the proposed change. Proposals are structurally forced to read as workaround-replacement arguments rather than artifact annotations.

4. **Pre-committed score table with workaround column (C-11 + C-14)** -- All five workarounds are named in the table before any narrative begins. Step 1 in each persona section expands the table entry to 1-2 sentences. The amend template then cites the Step 1 field verbatim, creating a closed workaround chain from table -> persona -> amend.

5. **Two correct examples per per-section blockquote** -- V-05 gives two correct examples per persona (V-02/V-04 gave one). Two domain-matched examples per boundary provide stronger friction-tag grounding across a long multi-persona output.

---

## Final Rubric Criteria Summary

### Essential (all 5 must pass)

| # | Criterion | Weight |
|---|-----------|--------|
| C-01 | All 5 stock personas present | essential |
| C-02 | Each persona gives a 1-5 usability score | essential |
| C-03 | Each persona quotes exact text from the artifact | essential |
| C-04 | Cross-persona synthesis present (3+ persona finding) | essential |
| C-05 | Aggregate usability score computed | essential |

### Recommended

| # | Criterion | Weight |
|---|-----------|--------|
| C-06 | First-person narrative voice per persona | recommended |
| C-07 | Role-specific friction distinguished from universal | recommended |
| C-08 | Persona conflicts identified | recommended |

### Aspirational (13 criteria, capped at 10 points)

| # | Criterion | Source |
|---|-----------|--------|
| C-09 | Friction typed with contrast block | v1 |
| C-10 | Amend loop triggered correctly | v1 |
| C-11 | Score table pre-committed before narrative | R1 V-02 |
| C-12 | Named-character grounding per persona | R1 V-04 |
| C-13 | Inertia fields (Beats/Loses) | R1 V-05 |
| C-14 | Pre-walkthrough "current workaround" field | R2 V-05 |
| C-15 | Inline friction tags in first-person sentences | R2 V-05 |
| C-16 | Workaround-first ordering (before scenario brief) | R3 V-01/V-05 |
| C-17 | Per-section contrast blocks | R3 V-02/V-05 |
| C-18 | Named-workaround slot in amend template | R3 V-03/V-05 |
| C-19 | Numbered step sequence for workaround-before-brief | R4 V-04/V-05 |
| C-20 | Domain-matched per-section contrast examples | R4 V-05 |
| C-21 | Explicit gap-statement in amend template | R4 V-03/V-05 |

### Score Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 13 * 10)
```

Golden threshold: all 5 essential pass AND composite >= 80.
V-05 composite: **100** (5/5 essential + 3/3 recommended + 13/13 aspirational).

---

## Golden Prompt Body

```
You are running /review-users. Fill in this structured template exactly.
All section headers are fixed. Do not reorder, rename, or remove any section, step, or table.

TARGET ARTIFACT: [paste artifact under review, or provide path]

---

## SCORE SUMMARY TABLE

Fill this table FIRST, before writing any persona walkthrough.
"Current workaround" = the specific manual process or tool each character uses today when
this feature does not exist. Name it -- not a category.

| Character | Role        | Score (1-5) | Current workaround (today, without this) | Top friction phrase (verbatim) |
|-----------|-------------|-------------|------------------------------------------|-------------------------------|
| Sam       | Maker       |             |                                          |                               |
| Dev       | Developer   |             |                                          |                               |
| Casey     | Compliance  |             |                                          |                               |
| Jordan    | Supervisor  |             |                                          |                               |
| Alex      | Operator    |             |                                          |                               |
| --        | **Aggregate** | **(sum/5 = X)** | | |

---

## PERSONA WALKTHROUGHS

Write each walkthrough in first person AS the named character.
Complete ALL numbered steps in the order given. Do not skip or reorder steps.
At least one verbatim quote from the artifact per character.

---

### Sam (Maker)

**Step 1 -- Current workaround (before anything else):**
[Must match Sam's "Current workaround" cell in the SCORE SUMMARY TABLE. Expand to 1-2
sentences: name the specific action -- "Sam exports the report to CSV, opens it in Excel,
and reformats the columns manually before sending it to the team."]

**Step 2 -- Scenario brief:**
Sam is trying to ship a feature this week. A teammate said "read this before you start."
Sam has 10 minutes and will not read footnotes.

**Step 3 -- Walkthrough:**

> **Tagging reminder for Sam's section:**
> Correct: I read "automated on merge" and (confusion) couldn't tell which branch trigger this referred to.
> Correct: I found the field name but (jargon) "idempotency key" appeared with no definition nearby.
> Wrong:   **Confusion findings:** "automated on merge" -- Sam didn't understand this.

[Write Sam's first-person walkthrough.]

**Step 4 -- Inertia fields:**
Beats current process: [What the artifact does better than Sam's Step 1 workaround -- name the workaround explicitly]
Loses to current process: [Where Sam's Step 1 workaround is still better -- or "No current advantage"]

**Step 5 -- Score: [must match SCORE SUMMARY TABLE]**

---

### Dev (Developer)

**Step 1 -- Current workaround (before anything else):**
[Must match Dev's "Current workaround" cell. Expand to 1-2 sentences.]

**Step 2 -- Scenario brief:**
Dev is writing the integration. Dev needs to know exactly what the API expects, what it
returns, and what happens when something goes wrong. Dev will read this multiple times.

**Step 3 -- Walkthrough:**

> **Tagging reminder for Dev's section:**
> Correct: I searched for error codes and (friction) found only the happy-path response schema.
> Correct: The term "idempotent key" appeared once and (jargon) I had no definition to check against.
> Wrong:   **Friction:** no error codes -- Dev couldn't find failure behavior.

[Write Dev's first-person walkthrough.]

**Step 4 -- Inertia fields:**
Beats current process: [What the artifact does better than Dev's Step 1 workaround]
Loses to current process: [Where Dev's Step 1 workaround is still better]

**Step 5 -- Score: [must match SCORE SUMMARY TABLE]**

---

### Casey (Compliance)

**Step 1 -- Current workaround (before anything else):**
[Must match Casey's "Current workaround" cell. Expand to 1-2 sentences.]

**Step 2 -- Scenario brief:**
Casey was asked to sign off before this goes live. Casey is looking for data-handling
language and liability exposure. Casey reads the footnotes.

**Step 3 -- Walkthrough:**

> **Tagging reminder for Casey's section:**
> Correct: I found "user-provided input" and (fear) couldn't tell if this fell under PII scope.
> Correct: The section titled "data handling" used (jargon) terms I'd need legal to translate.
> Wrong:   **Fear:** "user-provided input" -- Casey worried about PII scope.

[Write Casey's first-person walkthrough.]

**Step 4 -- Inertia fields:**
Beats current process: [What the artifact does better than Casey's Step 1 workaround]
Loses to current process: [Where Casey's Step 1 workaround still wins]

**Step 5 -- Score: [must match SCORE SUMMARY TABLE]**

---

### Jordan (Supervisor)

**Step 1 -- Current workaround (before anything else):**
[Must match Jordan's "Current workaround" cell. Expand to 1-2 sentences.]

**Step 2 -- Scenario brief:**
Jordan approved this project. Jordan won't use the tool directly but will be asked
"did you review this?" Jordan needs to answer yes honestly.

**Step 3 -- Walkthrough:**

> **Tagging reminder for Jordan's section:**
> Correct: I read "owner approval required" and (confusion) didn't know if that meant me or the PM.
> Correct: There was no summary section and (friction) I had to read the whole document to form a view.
> Wrong:   **Confusion:** "owner approval" -- Jordan didn't know who this was.

[Write Jordan's first-person walkthrough.]

**Step 4 -- Inertia fields:**
Beats current process: [What the artifact does better than Jordan's Step 1 workaround]
Loses to current process: [Where Jordan's Step 1 workaround still wins]

**Step 5 -- Score: [must match SCORE SUMMARY TABLE]**

---

### Alex (Operator)

**Step 1 -- Current workaround (before anything else):**
[Must match Alex's "Current workaround" cell. Expand to 1-2 sentences.]

**Step 2 -- Scenario brief:**
Alex gets paged when it breaks. Alex reads documentation defensively -- failure modes,
recovery steps, things not mentioned.

**Step 3 -- Walkthrough:**

> **Tagging reminder for Alex's section:**
> Correct: I looked for the "rollback" section and (friction) the document ended at deployment.
> Correct: "Circuit breaker threshold" appeared without a value and (confusion) I had no number to tune.
> Wrong:   **Friction:** no rollback section -- Alex couldn't find recovery steps.

[Write Alex's first-person walkthrough.]

**Step 4 -- Inertia fields:**
Beats current process: [What the artifact does better than Alex's Step 1 workaround]
Loses to current process: [Where Alex's Step 1 workaround still wins]

**Step 5 -- Score: [must match SCORE SUMMARY TABLE]**

---

## CROSS-PERSONA SYNTHESIS

### Universal friction (3+ personas flagged this)

| Finding | Personas | Friction type |
|---------|----------|---------------|
|         |          |               |

### Role-specific friction (1-2 personas only)

| Finding | Persona(s) | Why role-specific |
|---------|------------|-------------------|
|         |            |                   |

### Persona conflicts
Look for cases where one character's "Beats" is another's "Loses" -- name both characters,
the artifact feature, and who gains vs. who loses.
If none: "No conflicts detected."

### Inertia summary
- **Strongest adoption pull:** [character with most "Beats" vs. "Loses" -- likeliest early adopter]
- **Highest inertia:** [character with most "Loses" entries -- highest adoption risk]
- **Rollout implication:** [one sentence: who to onboard first, who needs most change management]

---

## AMEND LOOP

If any score < 3: for each sub-3 character, complete this template in the EXACT field order given.

---
**Amend proposal -- [Character] ([Role]) scored [X]/5**

Current workaround being displaced:
[Copy the character's Step 1 workaround field verbatim.]

What the workaround provides that the artifact does not:
[One concrete sentence naming the specific capability or guarantee the workaround gives this
character that the artifact fails to give. Name the thing, not the category.]

Verbatim artifact text with highest friction:
> "[exact quote from artifact that exposes the gap named above]"

Proposed artifact change:
[Text addition or revision that fills the gap named above.
State what to add and where. The change must make the named workaround unnecessary
for this character's specific friction point. Not "add more detail."]

Expected new score: [X]/5
Reasoning: [One sentence: why this change gives the character what the workaround was providing]
---

If all scores >= 3: write "Amend loop: not triggered (all scores >= 3)."
```
