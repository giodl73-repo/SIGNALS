`review-users-variations-R3-2026-03-14.md` written. Here is the round summary:

---

## Round 3 Variations — review-users

| V | Axis | New criteria targeted | Predicted composite |
|---|------|-----------------------|---------------------|
| **V-01** | Workaround-first persona structure | C-14 prominence | 97 |
| **V-02** | Per-section contrast block reminder | C-09 tightening | 98 |
| **V-03** | Amend loop grounded in workaround | C-10 grounded in C-14 | 97 |
| **V-04** | Workaround column in score table | C-14 structural pre-commitment | 99 |
| **V-05** | Full R3 combination target | All 7: C-09+C-10+C-11+C-12+C-13+C-14+C-15 | 100 |

**Three structural decisions in R3:**

1. **Workaround-first ordering** (V-01, V-05) — moves the "What [Name] does today instead:" field before the scenario brief so the comparison baseline is in working memory when the walkthrough begins. The most recent thing written naturally colors what follows.

2. **Per-section contrast block** (V-02, V-05) — R2's correct/wrong example appeared once globally. R3 embeds a role-appropriate contrast pair inside each persona section. When the model is mid-walkthrough at persona 4, the reminder is right there. Targets the specific PARTIAL failure mode from R2 V-02/V-03.

3. **Workaround column in score table** (V-04, V-05) — pre-commits workaround names in the opening table, creating the same structural reinforcement the C-11/C-12 character-name link created in R1. The model that writes "Sam | CSV export manually" in the table carries that name into every subsequent "Sam" reference.

**V-05** combines all four R3 mechanisms plus R2 V-05's full foundation (table + named characters + inertia fields + amend template). It's the first variation where C-09 is per-section-enforced, C-14 is both pre-committed and workaround-first, and C-10's amend template has an explicit named-workaround slot. Predicted 7/7 aspirationals.


**V-05 is the R3 combination target.** All three new mechanisms layer cleanly onto R2 V-05's foundation: workaround-first ordering, per-section contrast block, workaround column in table, and amend loop explicitly referencing the workaround field. No format switching needed.

---

## V-01: Workaround-First Persona Structure (C-14 prominence)

**Axis:** Reorder the persona template so the current-workaround field comes FIRST, before the scenario brief, before the walkthrough.
**Hypothesis:** R2 V-05 placed the "What [Name] does today instead:" field between the scenario brief and the walkthrough. R3 inverts the order — workaround first — so the model establishes the comparison baseline before inhabiting the character. The walkthrough that follows will naturally reference the workaround because it was the most recent thing written. This is the strongest structure for grounding inline narrative in the named alternative, producing richer C-14 output and more concrete Beats/Loses fields.

```
You are running /review-users. Fill in this structured template exactly.
All section headers are fixed. Do not reorder, rename, or remove any section or table.

TARGET ARTIFACT: [paste artifact under review, or provide path]

---

## SCORE SUMMARY TABLE

Fill this table FIRST, before writing any persona walkthrough. Commit all scores upfront.

| Character | Role        | Score (1-5) | Top friction phrase (verbatim from artifact) |
|-----------|-------------|-------------|----------------------------------------------|
| Sam       | Maker       |             |                                              |
| Dev       | Developer   |             |                                              |
| Casey     | Compliance  |             |                                              |
| Jordan    | Supervisor  |             |                                              |
| Alex      | Operator    |             |                                              |
| —         | **Aggregate** | **(sum/5 = X)** | |

---

## PERSONA WALKTHROUGHS

Write each walkthrough in first person AS the named character. Complete ALL fields in order.
Do not reorder or skip fields.

Inline friction tag rule: embed tags within narrative sentences, not as sub-section headers.
Format: (confusion) (friction) (fear) (jargon) — placed immediately before the friction phrase.

  Correct: I read "deploy on merge" and (confusion) had no idea which merge this meant.
  Correct: The "retention policy" section used (jargon) language I could not map to our org.
  Wrong:   **Confusion:** "deploy on merge" — Sam didn't understand this.

At least one verbatim quote from the artifact per character.

---

### Sam (Maker)

**Current workaround — what Sam does today instead:**
[1-2 sentences: Sam's manual process or alternative tool when this feature doesn't exist.
Be specific: name the tool or action — "Sam exports to CSV and reformats columns by hand."]

**Scenario:** Sam is trying to ship a feature this week. A teammate said "read this before
you start." Sam has 10 minutes and will not read footnotes.

[First-person walkthrough as Sam. Inline friction tags. At least one exact quote.]

**Beats current process:** [What the artifact does better than Sam's workaround — be specific]
**Loses to current process:** [Where Sam's workaround is still better — or "No current advantage"]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Dev (Developer)

**Current workaround — what Dev does today instead:**
[Dev's current approach to integration work without this artifact's guidance. Be specific.]

**Scenario:** Dev is writing the integration code. Dev needs to know exactly what the API
expects, what it returns, and what happens when something goes wrong.

[First-person walkthrough as Dev. Inline friction tags. At least one exact quote.]

**Beats current process:** [What the artifact does better than Dev's current approach]
**Loses to current process:** [Where Dev's current approach is still better]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Casey (Compliance)

**Current workaround — what Casey does today instead:**
[Casey's current manual review method when no structured artifact like this exists.]

**Scenario:** Casey was asked to sign off before this goes live. Casey is looking for
data-handling language and liability exposure. Casey reads the footnotes.

[First-person walkthrough as Casey. Inline friction tags. At least one exact quote.]

**Beats current process:** [What the artifact does better than Casey's current review]
**Loses to current process:** [Where the manual review still wins]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Jordan (Supervisor)

**Current workaround — what Jordan does today instead:**
[Jordan's current oversight method when no structured review process exists.]

**Scenario:** Jordan approved this project. Jordan won't use the tool directly but will be
asked "did you review this?" Jordan needs to answer yes honestly.

[First-person walkthrough as Jordan. Inline friction tags. At least one exact quote.]

**Beats current process:** [What the artifact does better than Jordan's current oversight]
**Loses to current process:** [Where Jordan's current method is still better]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Alex (Operator)

**Current workaround — what Alex does today instead:**
[Alex's current approach when no artifact guides operational behavior for this feature.]

**Scenario:** Alex gets paged when it breaks. Alex reads documentation defensively —
failure modes, recovery steps, things not mentioned.

[First-person walkthrough as Alex. Inline friction tags. At least one exact quote.]

**Beats current process:** [What the artifact does better than Alex's current approach]
**Loses to current process:** [Where Alex's current approach is still better]

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
"Loses to current process" — where one persona's adoption gain is another's adoption cost.
Name both characters, the artifact feature, and who gains vs. who loses.
If none: "No conflicts detected."

### Inertia summary
- **Strongest adoption pull:** [character with most "Beats" vs. "Loses" — likeliest early adopter]
- **Highest inertia:** [character with most "Loses" entries — highest adoption risk]
- **Rollout implication:** [one sentence: who to onboard first, who needs most change management]

---

## AMEND LOOP

Check SCORE SUMMARY TABLE.
- If any score < 3: for each sub-3 character, write: (1) character name + role + score,
  (2) verbatim artifact text with the highest friction, (3) a concrete proposed change that
  closes the gap between the artifact and that character's "Loses to current process" entry,
  (4) expected new score after the change.
- If all scores >= 3: write "Amend loop: not triggered (all scores >= 3)."
```

---

## V-02: Per-Section Contrast Block Reminder (C-09 tightening)

**Axis:** Move the friction-tag contrast block from the global preamble into each persona section.
**Hypothesis:** R2's contrast block appeared once at the top of the PERSONA WALKTHROUGHS section. Models mid-walkthrough may drift to sub-section typing because the global rule is no longer in the immediate context window. Repeating the correct/wrong example inside each section's instruction line brings the mechanic back into view at every persona boundary. This targets the specific C-09 PARTIAL failure mode from R2 V-02/V-03: the model was told the rule once but stopped applying it. Per-section contrast blocks make the mechanic inescapably present at every transition.

```
You are running /review-users. Fill in this structured template exactly.
All section headers are fixed. Do not reorder, rename, or remove any section or table.

TARGET ARTIFACT: [paste artifact under review, or provide path]

---

## SCORE SUMMARY TABLE

Fill this table FIRST, before writing any persona walkthrough. Commit all scores upfront.

| Character | Role        | Score (1-5) | Top friction phrase (verbatim from artifact) |
|-----------|-------------|-------------|----------------------------------------------|
| Sam       | Maker       |             |                                              |
| Dev       | Developer   |             |                                              |
| Casey     | Compliance  |             |                                              |
| Jordan    | Supervisor  |             |                                              |
| Alex      | Operator    |             |                                              |
| —         | **Aggregate** | **(sum/5 = X)** | |

---

## PERSONA WALKTHROUGHS

Write each walkthrough in first person AS the named character. Complete ALL fields.
At least one verbatim quote from the artifact per character.

---

### Sam (Maker)
Sam is trying to ship a feature this week. A teammate said "read this before you start."
Sam has 10 minutes and will not read footnotes.

**What Sam does today instead:**
[Sam's current manual process or alternative when this feature doesn't exist. Be specific.]

[Write Sam's walkthrough in first person. Tag each friction point INLINE within the sentence,
using: (confusion) (friction) (fear) (jargon) — immediately before the friction phrase.
  Correct: I read "deploy on merge" and (confusion) had no idea which merge event this meant.
  Wrong:   **Confusion:** "deploy on merge" — Sam did not understand this.]

**Beats current process:** [What the artifact does better than Sam's workaround — specific]
**Loses to current process:** [Where Sam's workaround is still better — or "No current advantage"]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Dev (Developer)
Dev is writing the integration. Dev needs to know exactly what the API expects, what it
returns, and what happens when something goes wrong. Dev will read this multiple times.

**What Dev does today instead:**
[Dev's current approach when this artifact's guidance doesn't exist.]

[Write Dev's walkthrough in first person. Tag each friction point INLINE within the sentence,
using: (confusion) (friction) (fear) (jargon) — immediately before the friction phrase.
  Correct: I needed the retry behavior but (friction) the artifact only described the happy path.
  Wrong:   **Friction:** retry behavior not documented — Dev couldn't find it.]

**Beats current process:** [What the artifact does better than Dev's current approach]
**Loses to current process:** [Where Dev's current approach is still better]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Casey (Compliance)
Casey was asked to sign off before this goes live. Casey is looking for data-handling
language and liability exposure. Casey reads the footnotes.

**What Casey does today instead:**
[Casey's current manual review method when no structured artifact exists.]

[Write Casey's walkthrough in first person. Tag each friction point INLINE within the sentence,
using: (confusion) (friction) (fear) (jargon) — immediately before the friction phrase.
  Correct: I saw "user data" and (fear) couldn't tell if this crossed GDPR scope.
  Wrong:   **Fear:** "user data" — Casey worried about GDPR scope.]

**Beats current process:** [What the artifact does better than Casey's current review]
**Loses to current process:** [Where the manual review still wins]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Jordan (Supervisor)
Jordan approved this project. Jordan won't use the tool directly but will be asked
"did you review this?" Jordan needs to answer yes honestly.

**What Jordan does today instead:**
[Jordan's current oversight method when no structured review process exists.]

[Write Jordan's walkthrough in first person. Tag each friction point INLINE within the sentence,
using: (confusion) (friction) (fear) (jargon) — immediately before the friction phrase.
  Correct: I read "team lead approval required" and (confusion) had no idea which role this mapped to.
  Wrong:   **Confusion:** "team lead approval" — Jordan didn't know who this was.]

**Beats current process:** [What the artifact does better than Jordan's current oversight]
**Loses to current process:** [Where Jordan's current method is still better]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Alex (Operator)
Alex gets paged when it breaks. Alex reads documentation defensively — failure modes,
recovery steps, things not mentioned.

**What Alex does today instead:**
[Alex's current approach when no artifact guides operational behavior for this feature.]

[Write Alex's walkthrough in first person. Tag each friction point INLINE within the sentence,
using: (confusion) (friction) (fear) (jargon) — immediately before the friction phrase.
  Correct: I scanned for "rollback" and (friction) found nothing — the artifact ends after deployment.
  Wrong:   **Friction:** no rollback section — Alex couldn't find it.]

**Beats current process:** [What the artifact does better than Alex's current approach]
**Loses to current process:** [Where Alex's current approach is still better]

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
"Loses to current process." Name the characters, the artifact feature, and who gains vs. who loses.
If none: "No conflicts detected."

### Inertia summary
- **Strongest adoption pull:** [character with most "Beats" vs. "Loses"]
- **Highest inertia:** [character with most "Loses" entries]
- **Rollout implication:** [one sentence]

---

## AMEND LOOP

Check SCORE SUMMARY TABLE.
- If any score < 3: for each sub-3 character, write: (1) character name + role + score,
  (2) verbatim artifact text with the highest friction, (3) a concrete proposed change that
  closes the gap between the artifact and that character's "Loses to current process" entry,
  (4) expected new score after the change.
- If all scores >= 3: write "Amend loop: not triggered (all scores >= 3)."
```

---

## V-03: Amend Loop Grounded in Workaround (C-10 grounded in C-14)

**Axis:** Amend proposals use an explicit template that names the workaround as a required input field.
**Hypothesis:** R2's amend loop grounded proposals in "Loses to current process" but the instruction was one line among several. Making the workaround a named slot in an amend proposal template forces the model to write "Sam currently [workaround] — the proposed change should make this unnecessary by [change]." This targets C-10's actionability: a proposal that closes a named gap is structurally more useful than a generic "add more explanation" fix. The amend template becomes a workaround-replacement argument, not an abstract usability patch.

```
You are running /review-users. Fill in this structured template exactly.
All section headers are fixed. Do not reorder, rename, or remove any section or table.

TARGET ARTIFACT: [paste artifact under review, or provide path]

---

## SCORE SUMMARY TABLE

Fill this table FIRST, before writing any persona walkthrough. Commit all scores upfront.

| Character | Role        | Score (1-5) | Top friction phrase (verbatim from artifact) |
|-----------|-------------|-------------|----------------------------------------------|
| Sam       | Maker       |             |                                              |
| Dev       | Developer   |             |                                              |
| Casey     | Compliance  |             |                                              |
| Jordan    | Supervisor  |             |                                              |
| Alex      | Operator    |             |                                              |
| —         | **Aggregate** | **(sum/5 = X)** | |

---

## PERSONA WALKTHROUGHS

Write each walkthrough in first person AS the named character. Complete ALL fields.

Inline friction tag rule: embed tags within narrative sentences, not as sub-section headers.
Format: (confusion) (friction) (fear) (jargon) — placed immediately before the friction phrase.

  Correct: I read "deploy on merge" and (confusion) had no idea which merge this meant.
  Wrong:   **Confusion:** "deploy on merge" — Sam didn't understand this.

At least one verbatim quote from the artifact per character.

---

### Sam (Maker)
Sam is trying to ship a feature this week. A teammate said "read this before you start."
Sam has 10 minutes and will not read footnotes.

**What Sam does today instead:**
[Sam's current manual process or alternative when this feature doesn't exist. Be specific.]

[First-person walkthrough as Sam. Inline friction tags. At least one exact quote.]

**Beats current process:** [What the artifact does better than Sam's workaround — specific]
**Loses to current process:** [Where Sam's workaround is still better — or "No current advantage"]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Dev (Developer)
Dev is writing the integration. Dev needs to know exactly what the API expects, what it
returns, and what happens when something goes wrong.

**What Dev does today instead:**
[Dev's current approach when this artifact's guidance doesn't exist.]

[First-person walkthrough as Dev. Inline friction tags. At least one exact quote.]

**Beats current process:** [What the artifact does better than Dev's current approach]
**Loses to current process:** [Where Dev's current approach is still better]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Casey (Compliance)
Casey was asked to sign off before this goes live. Casey is looking for data-handling
language and liability exposure. Casey reads the footnotes.

**What Casey does today instead:**
[Casey's current manual review method when no structured artifact exists.]

[First-person walkthrough as Casey. Inline friction tags. At least one exact quote.]

**Beats current process:** [What the artifact does better than Casey's current review]
**Loses to current process:** [Where the manual review still wins]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Jordan (Supervisor)
Jordan approved this project. Jordan won't use the tool directly but will be asked
"did you review this?" Jordan needs to answer yes honestly.

**What Jordan does today instead:**
[Jordan's current oversight method when no structured review process exists.]

[First-person walkthrough as Jordan. Inline friction tags. At least one exact quote.]

**Beats current process:** [What the artifact does better than Jordan's current oversight]
**Loses to current process:** [Where Jordan's current method is still better]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Alex (Operator)
Alex gets paged when it breaks. Alex reads documentation defensively — failure modes,
recovery steps, things not mentioned.

**What Alex does today instead:**
[Alex's current approach when no artifact guides operational behavior for this feature.]

[First-person walkthrough as Alex. Inline friction tags. At least one exact quote.]

**Beats current process:** [What the artifact does better than Alex's current approach]
**Loses to current process:** [Where Alex's current approach is still better]

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
"Loses to current process." Name the characters, the artifact feature, and who gains vs. who loses.
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
**Amend proposal — [Character name] ([Role]) scored [X]/5**

Verbatim artifact text with highest friction:
> "[exact quote from artifact]"

Current workaround this proposal must beat:
[Copy the character's "What [Name] does today instead:" field here verbatim]

Proposed artifact change:
[Concrete text addition or revision that closes the named workaround gap.
Not "add more detail" — name what to say and where to say it.
The change should make the workaround unnecessary for this character's friction point.]

Expected new score: [X]/5
Reasoning: [One sentence: why this change beats the named workaround for this character]
---

If all scores >= 3: write "Amend loop: not triggered (all scores >= 3)."
```

---

## V-04: Workaround Column in Score Table (C-14 structural pre-commitment)

**Axis:** Add a "Current workaround" column to the SCORE SUMMARY TABLE.
**Hypothesis:** R1 showed that pre-committing character names in the score table (C-11/C-12 structural link) caused the model to write *as Sam* throughout the narrative. The same mechanism should work for workarounds: pre-committing "Sam: CSV export by hand" in the table keeps the named workaround in context when the walkthrough begins. Beats/Loses fields naturally reference it; amend proposals are grounded because the workaround name was already committed. This is the strongest structural driver of C-14 compliance — workaround is no longer an in-prose field to remember but a pre-committed slot in the opening table.

```
You are running /review-users. Fill in this structured template exactly.
All section headers are fixed. Do not reorder, rename, or remove any section or table.

TARGET ARTIFACT: [paste artifact under review, or provide path]

---

## SCORE SUMMARY TABLE

Fill this table FIRST, before writing any persona walkthrough. Commit all values upfront.
"Current workaround" = the specific manual process or tool each character uses today when
this feature does not exist. Be concrete — name the tool or action, not a category.

| Character | Role        | Score (1-5) | Current workaround (today, without this feature) | Top friction phrase (verbatim) |
|-----------|-------------|-------------|--------------------------------------------------|-------------------------------|
| Sam       | Maker       |             |                                                  |                               |
| Dev       | Developer   |             |                                                  |                               |
| Casey     | Compliance  |             |                                                  |                               |
| Jordan    | Supervisor  |             |                                                  |                               |
| Alex      | Operator    |             |                                                  |                               |
| —         | **Aggregate** | **(sum/5 = X)** | | |

---

## PERSONA WALKTHROUGHS

Write each walkthrough in first person AS the named character. Complete ALL fields.
Reference each character's "Current workaround" (from the SCORE SUMMARY TABLE) as the
comparison baseline throughout the walkthrough and in the Beats/Loses fields.

Inline friction tag rule: embed tags within narrative sentences, not as sub-section headers.
Format: (confusion) (friction) (fear) (jargon) — placed immediately before the friction phrase.

  Correct: I read "deploy on merge" and (confusion) had no idea which merge event this meant.
  Correct: I needed rollback steps and (friction) the artifact ended right after deployment.
  Wrong:   **Confusion findings:** "deploy on merge" — Sam did not understand this.

At least one verbatim quote from the artifact per character.

---

### Sam (Maker)
Sam is trying to ship a feature this week. A teammate said "read this before you start."
Sam has 10 minutes and will not read footnotes.

[First-person walkthrough as Sam. Reference Sam's current workaround from the SCORE SUMMARY
TABLE as the comparison baseline. Inline friction tags. At least one exact quote.]

**Beats current process:** [What the artifact does better than Sam's committed workaround — name it]
**Loses to current process:** [Where Sam's workaround is still better — or "No current advantage"]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Dev (Developer)
Dev is writing the integration. Dev needs to know exactly what the API expects, what it
returns, and what happens when something goes wrong. Dev will read this multiple times.

[First-person walkthrough as Dev. Reference Dev's current workaround from the SCORE SUMMARY
TABLE as the comparison baseline. Inline friction tags. At least one exact quote.]

**Beats current process:** [What the artifact does better than Dev's committed workaround]
**Loses to current process:** [Where Dev's workaround is still better]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Casey (Compliance)
Casey was asked to sign off before this goes live. Casey is looking for data-handling
language and liability exposure. Casey reads the footnotes.

[First-person walkthrough as Casey. Reference Casey's current workaround from the SCORE SUMMARY
TABLE as the comparison baseline. Inline friction tags. At least one exact quote.]

**Beats current process:** [What the artifact does better than Casey's committed workaround]
**Loses to current process:** [Where the manual review still wins]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Jordan (Supervisor)
Jordan approved this project. Jordan won't use the tool directly but will be asked
"did you review this?" Jordan needs to answer yes honestly.

[First-person walkthrough as Jordan. Reference Jordan's current workaround from the SCORE SUMMARY
TABLE as the comparison baseline. Inline friction tags. At least one exact quote.]

**Beats current process:** [What the artifact does better than Jordan's committed workaround]
**Loses to current process:** [Where Jordan's current method is still better]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Alex (Operator)
Alex gets paged when it breaks. Alex reads documentation defensively — failure modes,
recovery steps, things not mentioned.

[First-person walkthrough as Alex. Reference Alex's current workaround from the SCORE SUMMARY
TABLE as the comparison baseline. Inline friction tags. At least one exact quote.]

**Beats current process:** [What the artifact does better than Alex's committed workaround]
**Loses to current process:** [Where Alex's current approach is still better]

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
"Loses to current process." Name the characters, the artifact feature, and who gains vs. who loses.
If none: "No conflicts detected."

### Inertia summary
- **Strongest adoption pull:** [character with most "Beats" vs. "Loses"]
- **Highest inertia:** [character with most "Loses" entries]
- **Rollout implication:** [one sentence]

---

## AMEND LOOP

Check SCORE SUMMARY TABLE.
- If any score < 3: for each sub-3 character, write: (1) character name + role + score,
  (2) verbatim artifact text with highest friction, (3) a concrete proposed change that closes
  the gap between the artifact and that character's "Loses to current process" entry —
  explicitly referencing the workaround from the SCORE SUMMARY TABLE,
  (4) expected new score after the change.
- If all scores >= 3: write "Amend loop: not triggered (all scores >= 3)."
```

---

## V-05: Full R3 Combination Target (All 7 Aspirationals)

**Axis:** All R3 mechanisms combined — the R3 target for 7/7 aspirationals
**Hypothesis:** Pre-committed score table with workaround column (C-11 + C-14 structural link) + workaround-first persona ordering (C-14 prominence, C-12 scenario brief follows) + per-section contrast block at each persona boundary (C-09 + C-15 inescapable) + inertia fields (C-13) + amend loop with workaround-grounded proposal template (C-10 grounded in C-14). All seven aspirationals should fire simultaneously. The five mechanisms reinforce each other: workaround-first ordering gives the model the comparison baseline before narrating; per-section contrast blocks prevent inline-tag drift; named characters keep first-person voice natural; inertia fields make conflict detection mechanistic; amend proposals close named gaps not abstract ones. No format switching needed at any step.

```
You are running /review-users. Fill in this structured template exactly.
All section headers are fixed. Do not reorder, rename, or remove any section or table.

TARGET ARTIFACT: [paste artifact under review, or provide path]

---

## SCORE SUMMARY TABLE

Fill this table FIRST, before writing any persona walkthrough. Commit all values upfront.
"Current workaround" = the specific manual process or tool each character uses today when
this feature does not exist. Name the tool or action — not a category.

| Character | Role        | Score (1-5) | Current workaround (today, without this) | Top friction phrase (verbatim) |
|-----------|-------------|-------------|------------------------------------------|-------------------------------|
| Sam       | Maker       |             |                                          |                               |
| Dev       | Developer   |             |                                          |                               |
| Casey     | Compliance  |             |                                          |                               |
| Jordan    | Supervisor  |             |                                          |                               |
| Alex      | Operator    |             |                                          |                               |
| —         | **Aggregate** | **(sum/5 = X)** | | |

---

## PERSONA WALKTHROUGHS

Write each walkthrough in first person AS the named character. Complete ALL fields in order.
Do not skip or reorder any field. At least one verbatim quote from the artifact per character.

---

### Sam (Maker)

**Current workaround — what Sam does today instead:**
[Must match Sam's "Current workaround" cell in the SCORE SUMMARY TABLE. Expand to 1-2
sentences if needed: name the specific action — "Sam exports the report to CSV, opens it
in Excel, and reformats the columns manually before sending it to the team."]

**Scenario:** Sam is trying to ship a feature this week. A teammate said "read this before
you start." Sam has 10 minutes and will not read footnotes.

[Write Sam's walkthrough in first person. Tag each friction point INLINE within the sentence.
Format: (confusion) (friction) (fear) (jargon) — immediately before the friction phrase.
  Correct: I read "deploy on merge" and (confusion) had no idea which merge event this meant.
  Correct: I needed rollback steps and (friction) the artifact ended right after deployment.
  Wrong:   **Confusion findings:** "deploy on merge" — Sam did not understand this.
Include at least one verbatim quote from the artifact.]

**Beats current process:** [What the artifact does better than Sam's committed workaround — name the workaround explicitly]
**Loses to current process:** [Where Sam's workaround still wins — or "No current advantage"]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Dev (Developer)

**Current workaround — what Dev does today instead:**
[Must match Dev's "Current workaround" cell. Expand to 1-2 sentences: name the specific
approach — "Dev reads the source code directly and writes integration tests against
undocumented behavior."]

**Scenario:** Dev is writing the integration. Dev needs to know exactly what the API expects,
what it returns, and what happens when something goes wrong. Dev will read this multiple times.

[Write Dev's walkthrough in first person. Tag each friction point INLINE within the sentence.
Format: (confusion) (friction) (fear) (jargon) — immediately before the friction phrase.
  Correct: I searched for error codes and (friction) found only the happy-path response schema.
  Correct: The term "idempotent key" appeared once and (jargon) I had no definition to check.
  Wrong:   **Friction:** no error codes — Dev couldn't find failure behavior.
Include at least one verbatim quote from the artifact.]

**Beats current process:** [What the artifact does better than Dev's committed workaround]
**Loses to current process:** [Where Dev's workaround is still better]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Casey (Compliance)

**Current workaround — what Casey does today instead:**
[Must match Casey's "Current workaround" cell. Expand to 1-2 sentences: "Casey runs a
manual keyword search for 'data', 'user', 'retain', 'delete', then flags each hit in a
spreadsheet for legal review."]

**Scenario:** Casey was asked to sign off before this goes live. Casey is looking for
data-handling language and liability exposure. Casey reads the footnotes.

[Write Casey's walkthrough in first person. Tag each friction point INLINE within the sentence.
Format: (confusion) (friction) (fear) (jargon) — immediately before the friction phrase.
  Correct: I found "user-provided input" and (fear) couldn't tell if this fell under PII scope.
  Correct: The section titled "data handling" used (jargon) terms I'd need legal to translate.
  Wrong:   **Fear:** "user-provided input" — Casey worried about PII scope.
Include at least one verbatim quote from the artifact.]

**Beats current process:** [What the artifact does better than Casey's committed workaround]
**Loses to current process:** [Where the manual keyword review still wins]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Jordan (Supervisor)

**Current workaround — what Jordan does today instead:**
[Must match Jordan's "Current workaround" cell. Expand to 1-2 sentences: "Jordan asks the
team lead for a verbal summary and signs an email confirming 'reviewed' without seeing the
underlying artifact."]

**Scenario:** Jordan approved this project. Jordan won't use the tool directly but will be
asked "did you review this?" Jordan needs to answer yes honestly.

[Write Jordan's walkthrough in first person. Tag each friction point INLINE within the sentence.
Format: (confusion) (friction) (fear) (jargon) — immediately before the friction phrase.
  Correct: I read "owner approval required" and (confusion) didn't know if that meant me or the PM.
  Correct: There was no summary section and (friction) I had to read the whole document to form a view.
  Wrong:   **Confusion:** "owner approval" — Jordan didn't know who this was.
Include at least one verbatim quote from the artifact.]

**Beats current process:** [What the artifact does better than Jordan's committed workaround]
**Loses to current process:** [Where Jordan's verbal-summary approach still wins]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Alex (Operator)

**Current workaround — what Alex does today instead:**
[Must match Alex's "Current workaround" cell. Expand to 1-2 sentences: "Alex SSHes into
the host, tail-follows the log, and searches previous incidents in the team wiki when
something breaks in production."]

**Scenario:** Alex gets paged when it breaks. Alex reads documentation defensively —
failure modes, recovery steps, things not mentioned.

[Write Alex's walkthrough in first person. Tag each friction point INLINE within the sentence.
Format: (confusion) (friction) (fear) (jargon) — immediately before the friction phrase.
  Correct: I looked for the "rollback" section and (friction) the document ended at deployment.
  Correct: "Circuit breaker threshold" appeared without a value and (confusion) I had no number to tune.
  Wrong:   **Friction:** no rollback section — Alex couldn't find recovery steps.
Include at least one verbatim quote from the artifact.]

**Beats current process:** [What the artifact does better than Alex's committed workaround]
**Loses to current process:** [Where Alex's log-search approach still wins]

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
"Loses to current process" — one persona's adoption gain is another's adoption cost.
Name both characters, the artifact feature, and who gains vs. who loses.
If none: "No conflicts detected."

### Inertia summary
- **Strongest adoption pull:** [character with most "Beats" vs. "Loses" — likeliest early adopter]
- **Highest inertia:** [character with most "Loses" entries — highest adoption risk]
- **Rollout implication:** [one sentence: who to onboard first, who needs most change management]

---

## AMEND LOOP

Check SCORE SUMMARY TABLE.

If any score < 3: for each sub-3 character, complete this template exactly:

---
**Amend proposal — [Character] ([Role]) scored [X]/5**

Verbatim artifact text with highest friction:
> "[exact quote from artifact]"

Current workaround being displaced (from SCORE SUMMARY TABLE):
[Copy the character's "Current workaround" cell here verbatim]

Proposed artifact change:
[Concrete text addition or revision that closes the named workaround gap.
Not "add more detail" — state what to add and where.
The change should make the workaround unnecessary for this character's specific friction point.]

Expected new score: [X]/5
Reasoning: [One sentence: why this change beats the named workaround for this character]
---

If all scores >= 3: write "Amend loop: not triggered (all scores >= 3)."
```

---

## R3 Combination Analysis

| Mechanism | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-11 Pre-committed score table | PASS | PASS | PASS | PASS | PASS |
| C-12 Named characters | PASS | PASS | PASS | PASS | PASS |
| C-13 Inertia fields (Beats/Loses) | PASS | PASS | PASS | PASS | PASS |
| C-09 Friction typed with contrast block | global | per-section | global | global | per-section |
| C-14 Current-workaround field before walkthrough | PASS (workaround-first order) | partial (after brief) | partial (after brief) | PASS (table col + before brief) | PASS (table col + workaround-first) |
| C-15 Inline tags in first-person sentences | PASS | PASS | PASS | PASS | PASS |
| C-10 Amend loop grounded in workaround | partial | partial | PASS (template) | partial | PASS (template) |

**V-05 predicted score: 100 composite**

V-05 is the first variation with structural enforcement of:
- C-09 per-section (not just global) — contrast block at every persona boundary
- C-14 in both the table (pre-committed) and the persona section (workaround-first, expanded)
- C-10 via an explicit amend template that names the workaround field as a required input slot

**Key structural novelties over R2 V-05:**
1. Workaround column in score table — pre-commits workaround names before any narrative begins (V-04, V-05)
2. Per-section contrast block — contrast examples at each persona boundary, not only in global preamble (V-02, V-05)
3. Amend proposal template — named workaround-field slot in amend instructions (V-03, V-05)
4. Workaround-first ordering — workaround field placed before scenario brief so baseline is in context when narrative begins (V-01, V-05)
