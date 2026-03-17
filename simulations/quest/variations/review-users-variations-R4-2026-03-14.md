`review-users-variations-R4-2026-03-14.md` written.

---

## Round 4 Variations — review-users

| V | Axis | New criteria targeted | Predicted composite |
|---|------|-----------------------|---------------------|
| **V-01** | Numbered field sequence per persona | C-16 explicit enforcement | 100 |
| **V-02** | Mandatory per-section tag reminder with role-appropriate examples | C-17 explicit enforcement | 100 |
| **V-03** | Workaround-first amend template field order | C-18 ordering strengthened | 100 |
| **V-04** | Numbered steps + per-section reminders | C-16 + C-17 combined | 100 |
| **V-05** | Full R4 combination target | All 10: C-09 through C-18 | 100 |

---

**Three structural decisions:**

**V-01 — Numbered field sequence (C-16):** Each persona section becomes a 5-step numbered sequence: Step 1: workaround → Step 2: scenario brief → Step 3: walkthrough → Step 4: inertia fields → Step 5: score. Step numbers make the ordering a *rule*, not a layout convention. A model that sees "Step 1" before "Step 2" cannot reorder them without breaking the sequence — the cascade effect from C-16 is now structurally enforced rather than positionally implied.

**V-02 — Role-appropriate blockquote reminders (C-17):** Each persona section gets a visually distinct `> **Tagging reminder for [Name]'s section:**` blockquote with a correct/wrong pair drawn from that role's actual friction domain. Sam gets a build-process confusion example. Dev gets an API error-handling friction example. Casey gets a GDPR fear example. Jordan gets an approval-chain confusion example. Alex gets a rollback friction example. Domain-matched prototypes at each persona boundary are harder to skip than a global instruction block 3000 tokens back.

**V-03 — Workaround-first amend template (C-18):** Inverts R3 V-03/V-05 field order. New sequence: (1) current workaround → (2) what the workaround provides that the artifact does not (explicit gap-statement) → (3) verbatim quote → (4) proposed change → (5) new score. When the workaround is the first field written, it becomes the frame for interpreting the quote — not a parallel slot. The gap-statement field forces the model to name the specific capability gap before citing the artifact text that exposes it.

**Combination analysis:**

| Mechanism | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-17 per-section blocks | FAIL | PASS | FAIL | PASS | PASS |
| C-16 workaround before scenario brief | PASS | PASS | PASS | PASS | PASS |
| C-18 workaround slot first in amend | partial | partial | PASS | partial | PASS |

V-05 is the first variation where all three R4 criteria are structurally enforced simultaneously, on top of the full R3 V-05 foundation.
a fields, workaround-first ordering, inline tags, amend template with workaround slot). Predicted 10/10 aspirationals.

---

## V-01: Numbered Field Sequence Per Persona (C-16 explicit enforcement)

**Axis:** Structural ordering -- each persona section becomes a 5-step numbered sequence with the workaround as Step 1.
**Hypothesis:** R3 V-01 and V-05 placed the workaround field before the scenario brief through field position alone. The model could still reorder if it ignored field order. Numbering each field as a named step makes the ordering a sequence rule, not a layout preference. A model that sees "Step 1 -- Current workaround (before anything else):" followed by "Step 2 -- Scenario brief:" cannot put the scenario before the workaround without violating the numbered sequence. This targets C-16's failure mode directly: the ordering is now structural, not positional. The cascade effect (workaround in working memory when scenario is constructed) is preserved while the mechanism is made unambiguous.

```
You are running /review-users. Fill in this structured template exactly.
All section headers are fixed. Do not reorder, rename, or remove any section, step, or table.

TARGET ARTIFACT: [paste artifact under review, or provide path]

---

## SCORE SUMMARY TABLE

Fill this table FIRST, before writing any persona walkthrough. Commit all values upfront.
"Current workaround" = the specific manual process or tool each character uses today when
this feature does not exist. Name the tool or the action -- not a category.

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

Inline friction tag rule: embed (confusion) (friction) (fear) (jargon) immediately before
the friction phrase, inside the sentence -- not as sub-section headers.
  Correct: I read "deploy on merge" and (confusion) had no idea which merge event this meant.
  Wrong:   **Confusion:** "deploy on merge" -- Sam did not understand this.

---

### Sam (Maker)

**Step 1 -- Current workaround (before anything else):**
[Sam's specific manual process when this feature does not exist. Must match the SCORE SUMMARY
TABLE. Expand to 1-2 sentences: name the tool or action -- "Sam exports the report to CSV,
opens it in Excel, and reformats the columns manually before sending it to the team."]

**Step 2 -- Scenario brief:**
Sam is trying to ship a feature this week. A teammate said "read this before you start."
Sam has 10 minutes and will not read footnotes.

**Step 3 -- Walkthrough:**
[Write Sam's first-person walkthrough. Sam's Step 1 workaround is the comparison baseline.
Inline friction tags. At least one verbatim artifact quote.]

**Step 4 -- Inertia fields:**
Beats current process: [What the artifact does better than Sam's Step 1 workaround -- name it explicitly]
Loses to current process: [Where Sam's Step 1 workaround is still better -- or "No current advantage"]

**Step 5 -- Score: [must match SCORE SUMMARY TABLE]**

---

### Dev (Developer)

**Step 1 -- Current workaround (before anything else):**
[Dev's specific approach when this artifact's guidance does not exist. Must match the SCORE
SUMMARY TABLE. Name the approach -- "Dev reads the source code directly and writes integration
tests against undocumented behavior."]

**Step 2 -- Scenario brief:**
Dev is writing the integration. Dev needs to know exactly what the API expects, what it
returns, and what happens when something goes wrong. Dev will read this multiple times.

**Step 3 -- Walkthrough:**
[Write Dev's first-person walkthrough. Dev's Step 1 workaround is the comparison baseline.
Inline friction tags. At least one verbatim artifact quote.]

**Step 4 -- Inertia fields:**
Beats current process: [What the artifact does better than Dev's Step 1 workaround]
Loses to current process: [Where Dev's Step 1 workaround is still better]

**Step 5 -- Score: [must match SCORE SUMMARY TABLE]**

---

### Casey (Compliance)

**Step 1 -- Current workaround (before anything else):**
[Casey's current manual review method when no structured artifact exists. Must match the SCORE
SUMMARY TABLE. Name the method -- "Casey runs a manual keyword search for 'data', 'user',
'retain', 'delete', then flags each hit in a spreadsheet for legal review."]

**Step 2 -- Scenario brief:**
Casey was asked to sign off before this goes live. Casey is looking for data-handling
language and liability exposure. Casey reads the footnotes.

**Step 3 -- Walkthrough:**
[Write Casey's first-person walkthrough. Casey's Step 1 workaround is the comparison baseline.
Inline friction tags. At least one verbatim artifact quote.]

**Step 4 -- Inertia fields:**
Beats current process: [What the artifact does better than Casey's Step 1 workaround]
Loses to current process: [Where Casey's Step 1 workaround is still better]

**Step 5 -- Score: [must match SCORE SUMMARY TABLE]**

---

### Jordan (Supervisor)

**Step 1 -- Current workaround (before anything else):**
[Jordan's current oversight method when no structured review process exists. Must match the
SCORE SUMMARY TABLE. Name the method -- "Jordan asks the team lead for a verbal summary and
signs an email confirming 'reviewed' without seeing the underlying artifact."]

**Step 2 -- Scenario brief:**
Jordan approved this project. Jordan won't use the tool directly but will be asked
"did you review this?" Jordan needs to answer yes honestly.

**Step 3 -- Walkthrough:**
[Write Jordan's first-person walkthrough. Jordan's Step 1 workaround is the comparison
baseline. Inline friction tags. At least one verbatim artifact quote.]

**Step 4 -- Inertia fields:**
Beats current process: [What the artifact does better than Jordan's Step 1 workaround]
Loses to current process: [Where Jordan's Step 1 workaround is still better]

**Step 5 -- Score: [must match SCORE SUMMARY TABLE]**

---

### Alex (Operator)

**Step 1 -- Current workaround (before anything else):**
[Alex's current approach when no artifact guides operational behavior. Must match the SCORE
SUMMARY TABLE. Name the approach -- "Alex SSHes into the host, tail-follows the log, and
searches previous incidents in the team wiki when something breaks in production."]

**Step 2 -- Scenario brief:**
Alex gets paged when it breaks. Alex reads documentation defensively -- failure modes,
recovery steps, things not mentioned.

**Step 3 -- Walkthrough:**
[Write Alex's first-person walkthrough. Alex's Step 1 workaround is the comparison baseline.
Inline friction tags. At least one verbatim artifact quote.]

**Step 4 -- Inertia fields:**
Beats current process: [What the artifact does better than Alex's Step 1 workaround]
Loses to current process: [Where Alex's Step 1 workaround is still better]

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
Look for cases where one character's "Beats current process" aligns with another character's
"Loses to current process" -- one persona's adoption gain is another's adoption cost.
Name both characters, the artifact feature, and who gains vs. who loses.
If none: "No conflicts detected."

### Inertia summary
- **Strongest adoption pull:** [character with most "Beats" vs. "Loses" -- likeliest early adopter]
- **Highest inertia:** [character with most "Loses" entries -- highest adoption risk]
- **Rollout implication:** [one sentence: who to onboard first, who needs most change management]

---

## AMEND LOOP

Check SCORE SUMMARY TABLE.
If any score < 3: for each sub-3 character, complete this template exactly:

---
**Amend proposal -- [Character] ([Role]) scored [X]/5**

Verbatim artifact text with highest friction:
> "[exact quote from artifact]"

Current workaround being displaced (from SCORE SUMMARY TABLE):
[Copy the character's "Current workaround" cell here verbatim]

Proposed artifact change:
[Concrete text addition or revision that closes the named workaround gap.
Not "add more detail" -- state what to add and where.
The change should make the workaround unnecessary for this character's specific friction point.]

Expected new score: [X]/5
Reasoning: [One sentence: why this change beats the named workaround for this character]
---

If all scores >= 3: write "Amend loop: not triggered (all scores >= 3)."
```

---

## V-02: Mandatory Per-Section Tag Reminder with Role-Appropriate Examples (C-17 explicit enforcement)

**Axis:** Format -- each persona section contains a mandatory blockquote reminder with a role-appropriate correct/wrong pair unique to that character's friction domain.
**Hypothesis:** R3 V-02 placed per-section contrast blocks inline in the instruction paragraph. A global block placed once is far from the 4th and 5th persona; an inline block inside a long instruction paragraph can be skimmed. R4 makes the reminder a structurally distinct blockquote (`> **Tagging reminder for [Name]'s section:**`) with a correct/wrong pair drawn from that role's actual friction domain: Sam gets a build-process confusion example, Dev gets an API error-handling friction example, Casey gets a data-scope fear example, Jordan gets an approval-chain confusion example, Alex gets a recovery-step friction example. Role-appropriate examples give the model a live, relevant prototype to pattern-match within that persona's context -- not a generic template to remember from the top of the prompt. This is the strongest structural enforcement of C-17 because the reminder and its domain example arrive together, at the exact point where the model begins narrating that persona.

```
You are running /review-users. Fill in this structured template exactly.
All section headers are fixed. Do not reorder, rename, or remove any section or table.

TARGET ARTIFACT: [paste artifact under review, or provide path]

---

## SCORE SUMMARY TABLE

Fill this table FIRST, before writing any persona walkthrough. Commit all values upfront.
"Current workaround" = the specific manual process or tool each character uses today when
this feature does not exist. Name the tool or the action.

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
Complete ALL fields. At least one verbatim quote per character.

---

### Sam (Maker)

**What Sam does today instead:**
[Sam's specific workaround. Must match SCORE SUMMARY TABLE. Expand: name the tool or action --
"Sam exports the draft to Google Docs, marks feedback inline, and emails the link to the team."]

**Scenario:** Sam is trying to ship a feature this week. A teammate said "read this before
you start." Sam has 10 minutes and will not read footnotes.

> **Tagging reminder for Sam's section:**
> Embed tags INLINE within first-person sentences -- immediately before the friction phrase.
> Correct: I read "automated on merge" and (confusion) couldn't tell which branch trigger this referred to.
> Wrong:   **Confusion findings:** "automated on merge" -- Sam didn't understand this.

[Write Sam's first-person walkthrough. Sam's workaround above is the comparison baseline.
At least one verbatim artifact quote.]

**Beats current process:** [What the artifact does better than Sam's named workaround]
**Loses to current process:** [Where Sam's workaround still wins -- or "No current advantage"]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Dev (Developer)

**What Dev does today instead:**
[Dev's specific approach when this artifact's guidance does not exist. Must match SCORE
SUMMARY TABLE. Name the approach.]

**Scenario:** Dev is writing the integration. Dev needs to know exactly what the API expects,
what it returns, and what happens when something goes wrong. Dev will read this multiple times.

> **Tagging reminder for Dev's section:**
> Embed tags INLINE within first-person sentences -- immediately before the friction phrase.
> Correct: I needed the retry interval and (friction) the artifact described only the successful response.
> Wrong:   **Friction:** retry interval not documented -- Dev couldn't find it.

[Write Dev's first-person walkthrough. Dev's workaround above is the comparison baseline.
At least one verbatim artifact quote.]

**Beats current process:** [What the artifact does better than Dev's named workaround]
**Loses to current process:** [Where Dev's workaround still wins]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Casey (Compliance)

**What Casey does today instead:**
[Casey's current manual review method when no structured artifact exists. Must match SCORE
SUMMARY TABLE. Name the method.]

**Scenario:** Casey was asked to sign off before this goes live. Casey is looking for
data-handling language and liability exposure. Casey reads the footnotes.

> **Tagging reminder for Casey's section:**
> Embed tags INLINE within first-person sentences -- immediately before the friction phrase.
> Correct: I found "user content" and (fear) couldn't confirm whether this triggered GDPR scope.
> Wrong:   **Fear:** "user content" -- Casey worried about GDPR scope.

[Write Casey's first-person walkthrough. Casey's workaround above is the comparison baseline.
At least one verbatim artifact quote.]

**Beats current process:** [What the artifact does better than Casey's named workaround]
**Loses to current process:** [Where Casey's workaround still wins]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Jordan (Supervisor)

**What Jordan does today instead:**
[Jordan's current oversight method when no structured review process exists. Must match SCORE
SUMMARY TABLE. Name the method.]

**Scenario:** Jordan approved this project. Jordan won't use the tool directly but will be
asked "did you review this?" Jordan needs to answer yes honestly.

> **Tagging reminder for Jordan's section:**
> Embed tags INLINE within first-person sentences -- immediately before the friction phrase.
> Correct: I read "requires stakeholder sign-off" and (confusion) didn't know if that role applied to me.
> Wrong:   **Confusion:** "stakeholder sign-off" -- Jordan didn't know if they were the right approver.

[Write Jordan's first-person walkthrough. Jordan's workaround above is the comparison baseline.
At least one verbatim artifact quote.]

**Beats current process:** [What the artifact does better than Jordan's named workaround]
**Loses to current process:** [Where Jordan's workaround still wins]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Alex (Operator)

**What Alex does today instead:**
[Alex's current approach when no artifact guides operational behavior. Must match SCORE
SUMMARY TABLE. Name the approach.]

**Scenario:** Alex gets paged when it breaks. Alex reads documentation defensively --
failure modes, recovery steps, things not mentioned.

> **Tagging reminder for Alex's section:**
> Embed tags INLINE within first-person sentences -- immediately before the friction phrase.
> Correct: I scanned for "recovery steps" and (friction) found nothing after the deployment section.
> Wrong:   **Friction:** no recovery section -- Alex couldn't find it.

[Write Alex's first-person walkthrough. Alex's workaround above is the comparison baseline.
At least one verbatim artifact quote.]

**Beats current process:** [What the artifact does better than Alex's named workaround]
**Loses to current process:** [Where Alex's workaround still wins]

**Score: [must match SCORE SUMMARY TABLE]**

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
Look for cases where one character's "Beats current process" aligns with another character's
"Loses to current process." Name both characters, the artifact feature, and who gains vs. who loses.
If none: "No conflicts detected."

### Inertia summary
- **Strongest adoption pull:** [character with most "Beats" vs. "Loses"]
- **Highest inertia:** [character with most "Loses" entries]
- **Rollout implication:** [one sentence]

---

## AMEND LOOP

Check SCORE SUMMARY TABLE.
If any score < 3: for each sub-3 character, complete this template exactly:

---
**Amend proposal -- [Character] ([Role]) scored [X]/5**

Verbatim artifact text with highest friction:
> "[exact quote from artifact]"

Current workaround being displaced:
[Copy the character's "What [Name] does today instead:" field verbatim]

Proposed artifact change:
[Concrete text addition or revision that closes the named workaround gap.
Name what to add and where. The change should make the workaround unnecessary
for this character's specific friction point.]

Expected new score: [X]/5
Reasoning: [One sentence: why this change beats the named workaround for this character]
---

If all scores >= 3: write "Amend loop: not triggered (all scores >= 3)."
```

---

## V-03: Workaround-First Amend Template Field Order (C-18 ordering strengthened)

**Axis:** Behavior -- restructure the amend template so the workaround is the first field, before the verbatim quote. Add a gap-statement field that explicitly names what the workaround provides that the artifact does not.
**Hypothesis:** R3 V-03 and V-05 added a "Current workaround being displaced" slot to the amend template, producing more grounded proposals than R1/R2. But in both those variations the slot appeared after the verbatim artifact quote. When the quote comes first, the model frames the problem as "the artifact said X and that was a problem" -- the workaround is secondary context. When the workaround comes first, the model frames the problem as "Sam currently does Y, and the artifact does not help Sam stop doing Y because X" -- the workaround is the primary frame. R4 inverts the field order and adds a "What the workaround provides that the artifact does not:" gap-statement field between the workaround and the quote. This forces the model to name the gap explicitly before citing the artifact text that exposes it. The result is a proposal structure that reads as a workaround-replacement argument rather than an artifact annotation.

```
You are running /review-users. Fill in this structured template exactly.
All section headers are fixed. Do not reorder, rename, or remove any section or table.

TARGET ARTIFACT: [paste artifact under review, or provide path]

---

## SCORE SUMMARY TABLE

Fill this table FIRST, before writing any persona walkthrough. Commit all values upfront.
"Current workaround" = the specific manual process or tool each character uses today when
this feature does not exist. Name the tool or the action.

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
Complete ALL fields. At least one verbatim quote per character.

Inline friction tag rule: embed (confusion) (friction) (fear) (jargon) immediately before
the friction phrase, inside the sentence -- not as sub-section headers.
  Correct: I read "deploy on merge" and (confusion) had no idea which merge event this meant.
  Wrong:   **Confusion:** "deploy on merge" -- Sam did not understand this.

---

### Sam (Maker)

**What Sam does today instead:**
[Sam's specific workaround. Must match SCORE SUMMARY TABLE. Expand: name the tool or action.]

**Scenario:** Sam is trying to ship a feature this week. A teammate said "read this before
you start." Sam has 10 minutes and will not read footnotes.

[Write Sam's first-person walkthrough. Sam's workaround above is the comparison baseline.
Inline friction tags. At least one verbatim artifact quote.]

**Beats current process:** [What the artifact does better than Sam's named workaround]
**Loses to current process:** [Where Sam's workaround still wins -- or "No current advantage"]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Dev (Developer)

**What Dev does today instead:**
[Dev's specific approach when this artifact's guidance does not exist. Must match SCORE
SUMMARY TABLE. Name the approach.]

**Scenario:** Dev is writing the integration. Dev needs to know exactly what the API expects,
what it returns, and what happens when something goes wrong. Dev will read this multiple times.

[Write Dev's first-person walkthrough. Dev's workaround above is the comparison baseline.
Inline friction tags. At least one verbatim artifact quote.]

**Beats current process:** [What the artifact does better than Dev's named workaround]
**Loses to current process:** [Where Dev's workaround still wins]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Casey (Compliance)

**What Casey does today instead:**
[Casey's current manual review method when no structured artifact exists. Must match SCORE
SUMMARY TABLE. Name the method.]

**Scenario:** Casey was asked to sign off before this goes live. Casey is looking for
data-handling language and liability exposure. Casey reads the footnotes.

[Write Casey's first-person walkthrough. Casey's workaround above is the comparison baseline.
Inline friction tags. At least one verbatim artifact quote.]

**Beats current process:** [What the artifact does better than Casey's named workaround]
**Loses to current process:** [Where Casey's workaround still wins]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Jordan (Supervisor)

**What Jordan does today instead:**
[Jordan's current oversight method when no structured review process exists. Must match SCORE
SUMMARY TABLE. Name the method.]

**Scenario:** Jordan approved this project. Jordan won't use the tool directly but will be
asked "did you review this?" Jordan needs to answer yes honestly.

[Write Jordan's first-person walkthrough. Jordan's workaround above is the comparison baseline.
Inline friction tags. At least one verbatim artifact quote.]

**Beats current process:** [What the artifact does better than Jordan's named workaround]
**Loses to current process:** [Where Jordan's workaround still wins]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Alex (Operator)

**What Alex does today instead:**
[Alex's current approach when no artifact guides operational behavior. Must match SCORE
SUMMARY TABLE. Name the approach.]

**Scenario:** Alex gets paged when it breaks. Alex reads documentation defensively --
failure modes, recovery steps, things not mentioned.

[Write Alex's first-person walkthrough. Alex's workaround above is the comparison baseline.
Inline friction tags. At least one verbatim artifact quote.]

**Beats current process:** [What the artifact does better than Alex's named workaround]
**Loses to current process:** [Where Alex's workaround still wins]

**Score: [must match SCORE SUMMARY TABLE]**

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
Look for cases where one character's "Beats current process" aligns with another character's
"Loses to current process." Name both characters, the artifact feature, and who gains vs. who loses.
If none: "No conflicts detected."

### Inertia summary
- **Strongest adoption pull:** [character with most "Beats" vs. "Loses"]
- **Highest inertia:** [character with most "Loses" entries]
- **Rollout implication:** [one sentence]

---

## AMEND LOOP

Check SCORE SUMMARY TABLE.

If any score < 3: for each sub-3 character, complete this template in the EXACT field order given.
Do not reorder the fields.

---
**Amend proposal -- [Character] ([Role]) scored [X]/5**

Current workaround being displaced:
[Copy the character's "What [Name] does today instead:" field verbatim. This is the frame
for everything that follows -- the proposal must make this specific workaround unnecessary.]

What the workaround provides that the artifact does not:
[One concrete sentence naming the specific capability or guarantee the workaround gives this
character that the artifact fails to give. Name the thing, not the category.
Example: "The workaround gives Casey a structured checklist of data terms to flag; the artifact
gives Casey a narrative paragraph with no extractable checklist."]

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

---

## V-04: Numbered Steps + Per-Section Reminders (C-16 + C-17 combined)

**Axis:** Structure + Format -- numbered field sequence (C-16) combined with mandatory per-section blockquote reminders with role-appropriate examples (C-17).
**Hypothesis:** V-01 enforces C-16 through numbered steps; V-02 enforces C-17 through role-appropriate blockquote reminders. Together they address the two structural failure modes that C-16 and C-17 target: wrong-order workaround placement and per-persona friction-tag drift. The combination works because the two mechanisms operate at different levels: numbering controls the sequence of fields within a section; the blockquote reminder controls the tagging mechanic at the transition into the walkthrough narrative. Neither mechanism competes with the other. The result is a persona section where the model (1) cannot place the scenario before the workaround, and (2) receives a role-specific tagging prototype at the exact moment it begins narrating that persona.

```
You are running /review-users. Fill in this structured template exactly.
All section headers are fixed. Do not reorder, rename, or remove any section, step, or table.

TARGET ARTIFACT: [paste artifact under review, or provide path]

---

## SCORE SUMMARY TABLE

Fill this table FIRST, before writing any persona walkthrough. Commit all values upfront.
"Current workaround" = the specific manual process or tool each character uses today when
this feature does not exist. Name the tool or the action -- not a category.

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
[Sam's specific manual process when this feature does not exist. Must match the SCORE SUMMARY
TABLE. Expand to 1-2 sentences: name the tool or action -- "Sam exports the draft to Google
Docs, marks feedback inline, and emails the link to the team."]

**Step 2 -- Scenario brief:**
Sam is trying to ship a feature this week. A teammate said "read this before you start."
Sam has 10 minutes and will not read footnotes.

**Step 3 -- Walkthrough:**

> **Tagging reminder for Sam's section:**
> Embed tags INLINE within first-person sentences -- immediately before the friction phrase.
> Correct: I read "automated on merge" and (confusion) couldn't tell which branch trigger this referred to.
> Wrong:   **Confusion findings:** "automated on merge" -- Sam didn't understand this.

[Write Sam's first-person walkthrough. Sam's Step 1 workaround is the comparison baseline.
Inline friction tags as shown above. At least one verbatim artifact quote.]

**Step 4 -- Inertia fields:**
Beats current process: [What the artifact does better than Sam's Step 1 workaround -- name it]
Loses to current process: [Where Sam's Step 1 workaround is still better -- or "No current advantage"]

**Step 5 -- Score: [must match SCORE SUMMARY TABLE]**

---

### Dev (Developer)

**Step 1 -- Current workaround (before anything else):**
[Dev's specific approach when this artifact's guidance does not exist. Must match the SCORE
SUMMARY TABLE. Name the approach -- "Dev reads the source code directly and writes integration
tests against undocumented behavior."]

**Step 2 -- Scenario brief:**
Dev is writing the integration. Dev needs to know exactly what the API expects, what it
returns, and what happens when something goes wrong. Dev will read this multiple times.

**Step 3 -- Walkthrough:**

> **Tagging reminder for Dev's section:**
> Embed tags INLINE within first-person sentences -- immediately before the friction phrase.
> Correct: I needed the retry interval and (friction) the artifact described only the successful response.
> Wrong:   **Friction:** retry interval not documented -- Dev couldn't find it.

[Write Dev's first-person walkthrough. Dev's Step 1 workaround is the comparison baseline.
Inline friction tags as shown above. At least one verbatim artifact quote.]

**Step 4 -- Inertia fields:**
Beats current process: [What the artifact does better than Dev's Step 1 workaround]
Loses to current process: [Where Dev's Step 1 workaround is still better]

**Step 5 -- Score: [must match SCORE SUMMARY TABLE]**

---

### Casey (Compliance)

**Step 1 -- Current workaround (before anything else):**
[Casey's current manual review method when no structured artifact exists. Must match the SCORE
SUMMARY TABLE. Name the method -- "Casey runs a manual keyword search for 'data', 'user',
'retain', 'delete', then flags each hit in a spreadsheet for legal review."]

**Step 2 -- Scenario brief:**
Casey was asked to sign off before this goes live. Casey is looking for data-handling
language and liability exposure. Casey reads the footnotes.

**Step 3 -- Walkthrough:**

> **Tagging reminder for Casey's section:**
> Embed tags INLINE within first-person sentences -- immediately before the friction phrase.
> Correct: I found "user content" and (fear) couldn't confirm whether this triggered GDPR scope.
> Wrong:   **Fear:** "user content" -- Casey worried about GDPR scope.

[Write Casey's first-person walkthrough. Casey's Step 1 workaround is the comparison baseline.
Inline friction tags as shown above. At least one verbatim artifact quote.]

**Step 4 -- Inertia fields:**
Beats current process: [What the artifact does better than Casey's Step 1 workaround]
Loses to current process: [Where Casey's Step 1 workaround is still better]

**Step 5 -- Score: [must match SCORE SUMMARY TABLE]**

---

### Jordan (Supervisor)

**Step 1 -- Current workaround (before anything else):**
[Jordan's current oversight method when no structured review process exists. Must match the
SCORE SUMMARY TABLE. Name the method -- "Jordan asks the team lead for a verbal summary and
signs an email confirming 'reviewed' without seeing the underlying artifact."]

**Step 2 -- Scenario brief:**
Jordan approved this project. Jordan won't use the tool directly but will be asked
"did you review this?" Jordan needs to answer yes honestly.

**Step 3 -- Walkthrough:**

> **Tagging reminder for Jordan's section:**
> Embed tags INLINE within first-person sentences -- immediately before the friction phrase.
> Correct: I read "requires stakeholder sign-off" and (confusion) didn't know if that role applied to me.
> Wrong:   **Confusion:** "stakeholder sign-off" -- Jordan didn't know if they were the right approver.

[Write Jordan's first-person walkthrough. Jordan's Step 1 workaround is the comparison
baseline. Inline friction tags as shown above. At least one verbatim artifact quote.]

**Step 4 -- Inertia fields:**
Beats current process: [What the artifact does better than Jordan's Step 1 workaround]
Loses to current process: [Where Jordan's Step 1 workaround is still better]

**Step 5 -- Score: [must match SCORE SUMMARY TABLE]**

---

### Alex (Operator)

**Step 1 -- Current workaround (before anything else):**
[Alex's current approach when no artifact guides operational behavior. Must match the SCORE
SUMMARY TABLE. Name the approach -- "Alex SSHes into the host, tail-follows the log, and
searches previous incidents in the team wiki when something breaks in production."]

**Step 2 -- Scenario brief:**
Alex gets paged when it breaks. Alex reads documentation defensively -- failure modes,
recovery steps, things not mentioned.

**Step 3 -- Walkthrough:**

> **Tagging reminder for Alex's section:**
> Embed tags INLINE within first-person sentences -- immediately before the friction phrase.
> Correct: I scanned for "recovery steps" and (friction) found nothing after the deployment section.
> Wrong:   **Friction:** no recovery section -- Alex couldn't find it.

[Write Alex's first-person walkthrough. Alex's Step 1 workaround is the comparison baseline.
Inline friction tags as shown above. At least one verbatim artifact quote.]

**Step 4 -- Inertia fields:**
Beats current process: [What the artifact does better than Alex's Step 1 workaround]
Loses to current process: [Where Alex's Step 1 workaround is still better]

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
Look for cases where one character's "Beats current process" aligns with another character's
"Loses to current process" -- one persona's adoption gain is another's adoption cost.
Name both characters, the artifact feature, and who gains vs. who loses.
If none: "No conflicts detected."

### Inertia summary
- **Strongest adoption pull:** [character with most "Beats" vs. "Loses" -- likeliest early adopter]
- **Highest inertia:** [character with most "Loses" entries -- highest adoption risk]
- **Rollout implication:** [one sentence: who to onboard first, who needs most change management]

---

## AMEND LOOP

Check SCORE SUMMARY TABLE.
If any score < 3: for each sub-3 character, complete this template exactly:

---
**Amend proposal -- [Character] ([Role]) scored [X]/5**

Verbatim artifact text with highest friction:
> "[exact quote from artifact]"

Current workaround being displaced (from SCORE SUMMARY TABLE):
[Copy the character's "Current workaround" cell here verbatim]

Proposed artifact change:
[Concrete text addition or revision that closes the named workaround gap.
Not "add more detail" -- state what to add and where.
The change should make the workaround unnecessary for this character's specific friction point.]

Expected new score: [X]/5
Reasoning: [One sentence: why this change beats the named workaround for this character]
---

If all scores >= 3: write "Amend loop: not triggered (all scores >= 3)."
```

---

## V-05: Full R4 Combination Target (All 10 Aspirationals)

**Axis:** All R4 mechanisms combined -- the R4 target for 10/10 aspirationals.
**Hypothesis:** Five mechanism groups, all structurally compatible and mutually reinforcing: (1) Pre-committed score table with workaround column (C-11 + C-14 structural pre-commitment). (2) Numbered field sequence enforcing workaround-first ordering, with named characters whose workaround expands from the table (C-12 + C-14 expanded + C-16 structural). (3) Per-section blockquote reminders with role-appropriate correct/wrong pairs, enforcing inline tagging at every persona boundary (C-09 + C-15 + C-17 per-section). (4) Beats/Loses inertia fields following the walkthrough (C-13). (5) Amend loop with workaround-first field order and explicit gap-statement field (C-10 + C-18 strengthened). The five groups reinforce without competing: workaround is pre-committed in the table, sequenced first in each persona section, and the primary frame in the amend template; per-section blockquotes prevent tag drift at every boundary; inline tags inside first-person prose require no format switching; inertia fields follow mechanically from the named workaround baseline; amend proposals read as workaround-replacement arguments rather than artifact annotations.

```
You are running /review-users. Fill in this structured template exactly.
All section headers are fixed. Do not reorder, rename, or remove any section, step, or table.

TARGET ARTIFACT: [paste artifact under review, or provide path]

---

## SCORE SUMMARY TABLE

Fill this table FIRST, before writing any persona walkthrough. Commit all values upfront.
"Current workaround" = the specific manual process or tool each character uses today when
this feature does not exist. Name the tool or the action -- not a category.

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
> Embed tags INLINE within first-person sentences -- immediately before the friction phrase.
> Correct: I read "automated on merge" and (confusion) couldn't tell which branch trigger this referred to.
> Correct: I found the field name but (jargon) "idempotency key" appeared with no definition nearby.
> Wrong:   **Confusion findings:** "automated on merge" -- Sam didn't understand this.

[Write Sam's first-person walkthrough. Sam's Step 1 workaround is the comparison baseline.
Inline friction tags as shown above. At least one verbatim artifact quote.]

**Step 4 -- Inertia fields:**
Beats current process: [What the artifact does better than Sam's Step 1 workaround -- name the workaround explicitly]
Loses to current process: [Where Sam's Step 1 workaround is still better -- or "No current advantage"]

**Step 5 -- Score: [must match SCORE SUMMARY TABLE]**

---

### Dev (Developer)

**Step 1 -- Current workaround (before anything else):**
[Must match Dev's "Current workaround" cell. Expand to 1-2 sentences: name the specific
approach -- "Dev reads the source code directly and writes integration tests against
undocumented behavior."]

**Step 2 -- Scenario brief:**
Dev is writing the integration. Dev needs to know exactly what the API expects, what it
returns, and what happens when something goes wrong. Dev will read this multiple times.

**Step 3 -- Walkthrough:**

> **Tagging reminder for Dev's section:**
> Embed tags INLINE within first-person sentences -- immediately before the friction phrase.
> Correct: I searched for error codes and (friction) found only the happy-path response schema.
> Correct: The term "idempotent key" appeared once and (jargon) I had no definition to check against.
> Wrong:   **Friction:** no error codes -- Dev couldn't find failure behavior.

[Write Dev's first-person walkthrough. Dev's Step 1 workaround is the comparison baseline.
Inline friction tags as shown above. At least one verbatim artifact quote.]

**Step 4 -- Inertia fields:**
Beats current process: [What the artifact does better than Dev's Step 1 workaround]
Loses to current process: [Where Dev's Step 1 workaround is still better]

**Step 5 -- Score: [must match SCORE SUMMARY TABLE]**

---

### Casey (Compliance)

**Step 1 -- Current workaround (before anything else):**
[Must match Casey's "Current workaround" cell. Expand to 1-2 sentences: "Casey runs a
manual keyword search for 'data', 'user', 'retain', 'delete', then flags each hit in a
spreadsheet for legal review."]

**Step 2 -- Scenario brief:**
Casey was asked to sign off before this goes live. Casey is looking for data-handling
language and liability exposure. Casey reads the footnotes.

**Step 3 -- Walkthrough:**

> **Tagging reminder for Casey's section:**
> Embed tags INLINE within first-person sentences -- immediately before the friction phrase.
> Correct: I found "user-provided input" and (fear) couldn't tell if this fell under PII scope.
> Correct: The section titled "data handling" used (jargon) terms I'd need legal to translate.
> Wrong:   **Fear:** "user-provided input" -- Casey worried about PII scope.

[Write Casey's first-person walkthrough. Casey's Step 1 workaround is the comparison baseline.
Inline friction tags as shown above. At least one verbatim artifact quote.]

**Step 4 -- Inertia fields:**
Beats current process: [What the artifact does better than Casey's Step 1 workaround]
Loses to current process: [Where Casey's Step 1 workaround still wins]

**Step 5 -- Score: [must match SCORE SUMMARY TABLE]**

---

### Jordan (Supervisor)

**Step 1 -- Current workaround (before anything else):**
[Must match Jordan's "Current workaround" cell. Expand to 1-2 sentences: "Jordan asks the
team lead for a verbal summary and signs an email confirming 'reviewed' without seeing the
underlying artifact."]

**Step 2 -- Scenario brief:**
Jordan approved this project. Jordan won't use the tool directly but will be asked
"did you review this?" Jordan needs to answer yes honestly.

**Step 3 -- Walkthrough:**

> **Tagging reminder for Jordan's section:**
> Embed tags INLINE within first-person sentences -- immediately before the friction phrase.
> Correct: I read "owner approval required" and (confusion) didn't know if that meant me or the PM.
> Correct: There was no summary section and (friction) I had to read the whole document to form a view.
> Wrong:   **Confusion:** "owner approval" -- Jordan didn't know who this was.

[Write Jordan's first-person walkthrough. Jordan's Step 1 workaround is the comparison
baseline. Inline friction tags as shown above. At least one verbatim artifact quote.]

**Step 4 -- Inertia fields:**
Beats current process: [What the artifact does better than Jordan's Step 1 workaround]
Loses to current process: [Where Jordan's Step 1 workaround still wins]

**Step 5 -- Score: [must match SCORE SUMMARY TABLE]**

---

### Alex (Operator)

**Step 1 -- Current workaround (before anything else):**
[Must match Alex's "Current workaround" cell. Expand to 1-2 sentences: "Alex SSHes into
the host, tail-follows the log, and searches previous incidents in the team wiki when
something breaks in production."]

**Step 2 -- Scenario brief:**
Alex gets paged when it breaks. Alex reads documentation defensively -- failure modes,
recovery steps, things not mentioned.

**Step 3 -- Walkthrough:**

> **Tagging reminder for Alex's section:**
> Embed tags INLINE within first-person sentences -- immediately before the friction phrase.
> Correct: I looked for the "rollback" section and (friction) the document ended at deployment.
> Correct: "Circuit breaker threshold" appeared without a value and (confusion) I had no number to tune.
> Wrong:   **Friction:** no rollback section -- Alex couldn't find recovery steps.

[Write Alex's first-person walkthrough. Alex's Step 1 workaround is the comparison baseline.
Inline friction tags as shown above. At least one verbatim artifact quote.]

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
Look for cases where one character's "Beats current process" aligns with another character's
"Loses to current process" -- one persona's adoption gain is another's adoption cost.
Name both characters, the artifact feature, and who gains vs. who loses.
If none: "No conflicts detected."

### Inertia summary
- **Strongest adoption pull:** [character with most "Beats" vs. "Loses" -- likeliest early adopter]
- **Highest inertia:** [character with most "Loses" entries -- highest adoption risk]
- **Rollout implication:** [one sentence: who to onboard first, who needs most change management]

---

## AMEND LOOP

Check SCORE SUMMARY TABLE.

If any score < 3: for each sub-3 character, complete this template in the EXACT field order given.
Do not reorder the fields.

---
**Amend proposal -- [Character] ([Role]) scored [X]/5**

Current workaround being displaced:
[Copy the character's Step 1 workaround field verbatim. This is the frame for everything
that follows -- the proposal must make this specific workaround unnecessary.]

What the workaround provides that the artifact does not:
[One concrete sentence naming the specific capability or guarantee the workaround gives this
character that the artifact fails to give. Name the thing, not the category.
Example: "The workaround gives Casey a structured checklist of data terms to flag; the artifact
gives Casey a narrative paragraph with no extractable checklist."]

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

---

## R4 Combination Analysis

| Mechanism | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-11 Pre-committed score table with workaround column | PASS | PASS | PASS | PASS | PASS |
| C-12 Named characters | PASS | PASS | PASS | PASS | PASS |
| C-13 Inertia fields (Beats/Loses) | PASS | PASS | PASS | PASS | PASS |
| C-09 Friction typed with contrast block | global | per-section (role-appropriate blockquote) | global | per-section (role-appropriate blockquote) | per-section (role-appropriate blockquote, 2 examples) |
| C-14 Current-workaround context field | PASS (Step 1, table-anchored) | PASS (before scenario) | PASS (before scenario) | PASS (Step 1, table-anchored) | PASS (Step 1, table-anchored, expanded) |
| C-15 Inline tags in first-person sentences | PASS | PASS | PASS | PASS | PASS |
| C-10 Amend loop triggered correctly | PASS | PASS | PASS (workaround-first template) | PASS | PASS (workaround-first template + gap-statement) |
| C-16 Workaround-first ordering (before scenario brief) | PASS (Step 1 before Step 2) | PASS (before scenario heading) | PASS (before scenario heading) | PASS (Step 1 before Step 2) | PASS (Step 1 before Step 2) |
| C-17 Per-section contrast blocks | FAIL (global only) | PASS (role-appropriate blockquote per section) | FAIL (global only) | PASS (role-appropriate blockquote per section) | PASS (role-appropriate blockquote per section) |
| C-18 Named-workaround slot in amend template | PASS (slot present, after quote) | PASS (slot present, after quote) | PASS (slot FIRST + gap-statement field) | PASS (slot present, after quote) | PASS (slot FIRST + gap-statement field) |

**V-05 predicted score: 100 composite**

V-05 is the first variation with structural enforcement of all five mechanism groups simultaneously:
- C-16: numbered steps make workaround-before-scenario-brief a sequence rule, not a layout preference
- C-17: role-appropriate blockquote reminders with two correct examples per section, at every persona boundary
- C-18: workaround-first field order in amend template, with explicit gap-statement field before the artifact quote
- C-09 + C-15: per-section two-example blocks drive inline tag compliance deeper into long outputs
- C-11 + C-14: table pre-commits workaround names; Step 1 expands them; amend template cites them verbatim

**Key structural novelties over R3 V-05:**
1. Numbered field sequence (V-01, V-04, V-05) -- step numbers make C-16 ordering a rule, not a convention
2. Role-appropriate blockquote reminders (V-02, V-04, V-05) -- domain-matched examples enforce C-17 at every boundary
3. Workaround-first amend template with gap-statement field (V-03, V-05) -- inverts field order and adds explicit gap naming, making C-18 proposals read as workaround-replacement arguments
