---

## Simplification Report

**What was removed and why:**

| # | Removed | Mechanism | Words |
|---|---------|-----------|-------|
| R1 | `"Embed tags INLINE..."` from all 5 blockquotes | Correct/wrong pairs immediately below demonstrate the rule; removing the stated rule keeps only the examples | ~60 |
| R2 | `"[Name]'s Step 1 workaround is the comparison baseline."` from all 5 Step 3 brackets | Step 1 is the line immediately above; calling it a "baseline" restates what it obviously is | ~45 |
| R3 | `"Inline friction tags as shown above."` from all 5 Step 3 brackets | Blockquote directly above covers this | ~25 |
| R4 | Role-specific example in Step 1 for Dev/Casey/Jordan/Alex | Sam's example establishes the pattern; model can generalize "name the specific action" | ~75 |
| R5 | `"Check SCORE SUMMARY TABLE."` before amend loop | Implied by the `"If any score < 3"` conditional | ~4 |
| R6 | Amend `"Current workaround"` meta-explanation sentence | Field label + gap-statement field enforce this; the explanation is design rationale, not instruction | ~18 |
| R7 | Amend gap-statement example (Casey checklist) | Field label is self-describing; one-off example adds no generalizable pattern | ~27 |
| R8 | Persona conflicts verbose paragraph → two-sentence instruction | Same instruction at half the length | ~22 |
| R9 | `"Commit all values upfront."` + `"Name the tool or the action -- not a category."` → `"Name it -- not a category."` | "FIRST, before writing any persona walkthrough" already enforces upfront commitment; caption is already descriptive | ~14 |
| R10 | `"At least one verbatim artifact quote."` from each Step 3 bracket | Global header: `"At least one verbatim quote from the artifact per character"` already requires this | ~35 |
| R11 | `"Do not reorder the fields."` in amend loop | `"EXACT field order given"` in the same sentence already prohibits reordering | ~4 |
| | **Total** | | **313 words** |

**Essential criteria check — simplified version:**

| C | Requirement | Preserved? |
|---|-------------|------------|
| C-01 | All 5 personas present | YES — all 5 section headers intact |
| C-02 | 1-5 score per persona | YES — Step 5 "must match SCORE SUMMARY TABLE" ×5 |
| C-03 | Verbatim quote per persona | YES — global "At least one verbatim quote from the artifact per character" |
| C-04 | Cross-persona synthesis, 3+ persona finding | YES — CROSS-PERSONA SYNTHESIS section + Universal friction table |
| C-05 | Aggregate score | YES — Aggregate row in SCORE SUMMARY TABLE |

All essential criteria: **YES**

```json
{"simplified_word_count": 1254, "original_word_count": 1567, "all_essential_still_pass": true}
```
ble.

TARGET ARTIFACT: [paste artifact under review, or provide path]

---

## SCORE SUMMARY TABLE

Fill this table FIRST, before writing any persona walkthrough.
"Current workaround" = the specific tool or action each character uses today without this feature.
Name it -- not a category.

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
[Must match Dev's "Current workaround" cell. Expand to 1-2 sentences naming the specific action.]

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
[Must match Casey's "Current workaround" cell. Expand to 1-2 sentences naming the specific action.]

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
[Must match Jordan's "Current workaround" cell. Expand to 1-2 sentences naming the specific action.]

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
[Must match Alex's "Current workaround" cell. Expand to 1-2 sentences naming the specific action.]

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
Name any case where one character's "Beats" is another's "Loses" -- both characters, the feature, who gains and who loses.
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
[State what to add and where to fill the gap named above.
The change must make the named workaround unnecessary for this character's specific friction point.
Not "add more detail."]

Expected new score: [X]/5
Reasoning: [One sentence: why this change gives the character what the workaround was providing]
---

If all scores >= 3: write "Amend loop: not triggered (all scores >= 3)."

---

## Word Count Summary

| Version | Words | Change |
|---------|-------|--------|
| Original (V-05 R4) | 1,567 | baseline |
| Simplified | 1,254 | -313 |
| Reduction | | **20.0%** |
