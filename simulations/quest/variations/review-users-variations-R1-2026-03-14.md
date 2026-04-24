Written to `simulations/quest/variations/review-users-variations-R1-2026-03-14.md`.

---

## Round 1 Variations — review-users

5 complete variations across single axes:

| V | Axis | Mechanism | Predicted strength |
|---|------|-----------|-------------------|
| **V-01** | Role sequence (Compliance-first) | Compliance leads, primes quote-discipline for all following personas | C-03, C-04 |
| **V-02** | Output format (table + prose hybrid) | Pre-printed score table committed before narrative; synthesis tables for C-04/C-07 | All essentials (C-01 through C-05) |
| **V-03** | Lifecycle emphasis (friction-typed first) | Four typed lenses (confusion/friction/fear/jargon) are the primary organizing structure | C-09 aspirational + C-03 |
| **V-04** | Phrasing register (scenario-driven, conversational) | Named characters with concrete scenarios; "what did you come to find?" grounds first-person voice | C-06, C-08 |
| **V-05** | Inertia framing (explicit do-nothing alternative) | Pre-printed "What I do today instead" field per persona; inertia summary in synthesis | C-08, C-10 |

**Predicted ceiling:** V-02 for essential pass rate (pre-printed structure prevents omission). V-05 for depth ceiling (inertia field drives conflict detection and amend loop naturalistically). V-03 for aspirational C-09 coverage.

**Key structural decision:** All 5 variations fix the stock persona set and mandate individual 1-5 scores. Single-axis variation isolates which mechanism drives each rubric criterion before combinations are tested in later rounds.
ix the stock persona set (C-01) and mandate individual scores (C-02). Single-axis variations isolate: ordering (V-01), format scaffolding (V-02), tagging discipline (V-03), narrative register (V-04), inertia surface (V-05). V-02 is predicted strongest for essential pass rate; V-03 for aspirational ceiling.

**Predicted ceiling:** V-02 — pre-printed structure prevents omission of any essential field. V-05 closest competitor for depth (C-08 conflict detection driven by explicit inertia framing).

---

## V-01: Role Sequence (Compliance-First)

**Axis:** Role sequence — Compliance persona runs first, setting a quote-grounded, regulatory tone before Maker/Developer/Supervisor/Operator follow
**Hypothesis:** Starting with the most constraint-aware persona establishes an artifact-quoting norm that all subsequent personas inherit. Compliance is most likely to flag jargon and data-handling gaps; leading with those findings primes the synthesis to surface them as universal friction rather than role-specific edge cases.

```
You are running /review-users. Walk through the target artifact with 5 persona advocates.

TARGET ARTIFACT: [paste artifact under review, or provide path]

PERSONA ORDER FOR THIS REVIEW:
1. Compliance
2. Maker
3. Developer
4. Supervisor
5. Operator

For each persona, write a first-person walkthrough. The persona narrates what they read, what
they try to do, and where they get stuck. Requirements per persona:
- Write in first person ("I read...", "I tried...", "I could not find...")
- Quote at least one exact phrase from the artifact (verbatim, in quotation marks)
- Flag each friction point with its type: confusion | friction | fear | jargon
- Give a usability score 1-5 at the end of the section

PERSONA BRIEFS:
- Compliance: focused on data handling, regulatory obligations, audit trail, liability language.
  Reads every qualifier. Flags anything that could create exposure.
- Maker: building something with this feature. Cares about speed, clarity, and whether the
  steps are in the right order. Does not read footnotes.
- Developer: integrating this into code. Cares about API contracts, edge cases, error handling.
  Reads for completeness and precision.
- Supervisor: approving work that uses this feature. Cares about visibility, control points,
  and accountability. Needs to know what their team is doing without doing it themselves.
- Operator: running this in production. Cares about monitoring, failure modes, rollback, and
  what wakes them up at 3am.

SECTION FORMAT PER PERSONA:

### [PERSONA NAME]
[First-person narrative. Flag friction inline: "(confusion) I didn't understand what X meant."
Use exact quotes from the artifact.]

**Score: [1-5]**
**Friction summary:** [2-3 sentence summary of top issues]

---

SYNTHESIS SECTION (required after all 5 personas):

### Cross-Persona Synthesis

**Universal friction (3+ personas):**
[List each finding shared by 3 or more personas. Name which personas share it.]

**Role-specific friction:**
[List friction that affected only 1-2 personas. Label which persona(s).]

**Persona conflicts:**
[Identify at least one case where a design choice that helped one persona created friction
for another. If none exist, state "No conflicts detected."]

**Aggregate usability score:** [mean of the 5 scores, shown as formula: (P1+P2+P3+P4+P5)/5 = X]

---

AMEND LOOP:
If any persona scored below 3/5, write an explicit amend proposal:
- Which persona scored below 3
- The exact artifact text causing the lowest score
- A concrete change to the artifact that would raise the score
- Re-score that persona after the proposed change
If no persona scored below 3/5, write: "Amend loop: not triggered (all scores >= 3)."
```

---

## V-02: Output Format (Structured Table + Prose Hybrid)

**Axis:** Output format — pre-printed score table at top, then prose per persona, then synthesis table
**Hypothesis:** Pre-printing the score summary table at the document head forces the model to commit all 5 scores before writing any narrative, preventing score inflation through post-hoc rationalization. The structured table format makes C-01 (all 5 personas) and C-02 (all 5 scores) structurally unfailable — they are the first thing output.

```
You are running /review-users. Fill in this structured template exactly.
All section headers are fixed. Do not reorder, rename, or remove any section or table.

TARGET ARTIFACT: [paste artifact under review, or provide path]

---

## SCORE SUMMARY TABLE

Fill this table first, before writing any persona narrative. Commit all scores upfront.

| Persona     | Score (1-5) | Top friction (one phrase) |
|-------------|-------------|---------------------------|
| Maker       |             |                           |
| Developer   |             |                           |
| Compliance  |             |                           |
| Supervisor  |             |                           |
| Operator    |             |                           |
| **Aggregate** | **(sum/5 = X)** | |

---

## PERSONA WALKTHROUGHS

For each persona below, write a first-person narrative. Requirements:
- First person throughout ("I read...", "I tried...", "I noticed...")
- At least one verbatim quote from the artifact per persona (use quotation marks)
- Flag friction inline using type tags: [confusion] [friction] [fear] [jargon]

### Maker
[First-person walkthrough. Maker is building something with this feature — cares about
speed, clear steps, what to do first. Does not read footnotes.]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Developer
[First-person walkthrough. Developer is integrating this into code — cares about API
contracts, input/output types, edge cases, what happens on failure.]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Compliance
[First-person walkthrough. Compliance is checking for regulatory exposure — reads every
qualifier, flags data-handling language, looks for audit trail, notes missing liability terms.]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Supervisor
[First-person walkthrough. Supervisor is approving team work — needs visibility and
control points without doing the work themselves. Looks for gates and accountability.]

**Score: [must match SCORE SUMMARY TABLE]**

---

### Operator
[First-person walkthrough. Operator runs this in production — cares about monitoring,
failure modes, what to do when it breaks at 3am.]

**Score: [must match SCORE SUMMARY TABLE]**

---

## CROSS-PERSONA SYNTHESIS

### Universal friction (3+ personas flagged this)
[Each row: finding | which personas | friction type]

| Finding | Personas | Type |
|---------|----------|------|
|         |          |      |

### Role-specific friction (1-2 personas only)
[Each row: finding | which persona(s) | why role-specific]

| Finding | Persona(s) | Why role-specific |
|---------|------------|-------------------|
|         |            |                   |

### Persona conflicts
[At least one conflict: what helped one persona and hurt another. Exact personas named.]
If none: "No conflicts detected — no design choice created opposing friction."

---

## AMEND LOOP

Check SCORE SUMMARY TABLE.
- If any score < 3: write one amend proposal per sub-3 persona (artifact change + re-score).
- If all scores >= 3: write "Amend loop: not triggered (all scores >= 3)."
```

---

## V-03: Lifecycle Emphasis (Friction-Typed from the Start)

**Axis:** Lifecycle emphasis — friction typing is the primary instruction, not an add-on; every persona narrates through the four signal categories explicitly
**Hypothesis:** Asking personas to narrate through four named lenses (confusion, friction, fear, jargon) rather than narrating freely and tagging later produces denser, more diagnostic output. Organizing each persona's section around the four types drives C-09 (aspirational) without sacrificing C-03 (quotes) or C-06 (first-person voice).

```
You are running /review-users. Each persona will walk through the target artifact and
report findings in four categories: confusion, friction, fear, and jargon.

TARGET ARTIFACT: [paste artifact under review, or provide path]

SIGNAL CATEGORIES (apply per persona):
- confusion: "I could not tell what this means." Something is ambiguous or unclear.
- friction: "I know what to do but it's harder than it should be." Steps, clicks, sequence.
- fear: "I am worried this will go wrong." Risk, consequence, irreversibility.
- jargon: "I don't know this word." Terminology that assumes knowledge the persona doesn't have.

STOCK PERSONAS (run all 5):
- Maker: building with this feature; speed-oriented; skips footnotes
- Developer: integrating via code; precision-oriented; reads for contracts and edge cases
- Compliance: checking for exposure; reads every qualifier; flags data and audit language
- Supervisor: approving team use; needs control points and visibility without hands-on use
- Operator: running in production; cares about failure modes and operational clarity

---

For each persona, structure the walkthrough as follows:

### [PERSONA NAME]

**Scenario:** [One sentence: what this persona is trying to accomplish with the artifact]

**Confusion findings:**
- "[exact quote from artifact]" — [why this creates confusion for this persona]
(repeat for each confusion finding; "none" if absent)

**Friction findings:**
- "[exact quote from artifact]" — [what makes this harder than it needs to be]
(repeat; "none" if absent)

**Fear findings:**
- "[exact quote from artifact]" — [what risk or consequence this surfaces]
(repeat; "none" if absent)

**Jargon findings:**
- "[exact quote from artifact]" — [term that excludes this persona]
(repeat; "none" if absent)

**Usability score: [1-5]**
Rationale: [1-2 sentences tying score to the findings above]

---

Run all 5 personas using this format, then write:

### Cross-Persona Synthesis

**Universal friction (3+ personas):**
For each finding shared by 3 or more personas: state the finding, name the personas, name
the friction type (confusion/friction/fear/jargon).

**Role-specific friction:**
Findings that appeared in only 1-2 personas. State persona and why it is role-specific.

**Persona conflicts:**
Cases where one persona's benefit is another's friction. Be specific: name the personas
and the artifact feature causing the trade-off.

**Aggregate usability score:** (Maker + Developer + Compliance + Supervisor + Operator) / 5 = X

---

### Amend Loop

If any persona scored below 3/5:
For each sub-3 persona:
1. State the persona name and score
2. Quote the artifact text with the highest friction
3. Propose a concrete change (rewrite, add, remove, restructure)
4. State the expected new score after the change

If all scores >= 3: "Amend loop: not triggered."
```

---

## V-04: Phrasing Register (Conversational, Scenario-Driven)

**Axis:** Phrasing register — conversational, scenario-grounded instructions; personas narrate a specific use-case moment rather than a generic review
**Hypothesis:** Grounding each persona in a concrete scenario ("you are about to do X") produces more specific friction findings and more authentic first-person voice than asking for a generic walkthrough. Specific scenarios surface persona conflicts more naturally because different goals create observable tension points.

```
You are running /review-users. Imagine five people who each need something different from
this artifact. Put yourself inside each one. What happens when they read it?

TARGET ARTIFACT: [paste artifact under review, or provide path]

---

Meet the five people:

**Sam (Maker)** — Sam is trying to ship a feature this week. Sam opened the artifact
because a teammate said "read this before you start." Sam has 10 minutes.

**Dev (Developer)** — Dev is writing the integration. Dev needs to know exactly what the
API expects, what it returns, and what happens when something goes wrong. Dev will read
this three times and still have questions.

**Casey (Compliance)** — Casey was asked to sign off before this goes live. Casey is
looking for two things: anything that touches user data, and anything that could create
liability. Casey reads the footnotes.

**Jordan (Supervisor)** — Jordan approved the team doing this project. Jordan doesn't
use the tool directly but will be asked "did you review the process?" Jordan needs to
be able to answer yes honestly.

**Alex (Operator)** — Alex is the one who gets paged when it breaks. Alex reads
documentation defensively — looking for the failure modes, the recovery steps, and
the things that weren't mentioned.

---

For each person, write what happens in their own words. Use first person throughout.
Each person must:
1. State what they came to find out
2. Narrate what they actually found — quote at least one exact phrase from the artifact
3. Name where they got stuck, confused, or worried
4. Give a usability score 1-5 with a one-sentence reason

### Sam (Maker)
[First-person narrative]
**Score: [1-5]** — [one sentence]

---

### Dev (Developer)
[First-person narrative]
**Score: [1-5]** — [one sentence]

---

### Casey (Compliance)
[First-person narrative]
**Score: [1-5]** — [one sentence]

---

### Jordan (Supervisor)
[First-person narrative]
**Score: [1-5]** — [one sentence]

---

### Alex (Operator)
[First-person narrative]
**Score: [1-5]** — [one sentence]

---

Now step back and look across all five accounts.

### What did they all struggle with?
List anything that came up for three or more people. These are the universal friction points.
For each: name the finding, name who flagged it, and quote the artifact text that caused it.

### What was unique to one or two people?
List friction that only affected one or two people. Explain why it's role-specific.

### Where did one person's needs work against another's?
Name at least one case where what Sam or Dev needed made things harder for Casey or Jordan
(or any cross-persona tension). If you genuinely found none, say so and explain why.

### Overall usability score
Average of the five scores: (Sam + Dev + Casey + Jordan + Alex) / 5 = X

---

### Should anything be changed?
If any person scored below 3/5, propose one specific change to the artifact for each
sub-3 score. Quote the problem text, write the fix, and estimate the new score.
If everyone scored 3 or above: "No amendments needed."
```

---

## V-05: Inertia Framing (Status-Quo Competitor Explicit)

**Axis:** Inertia framing — each persona has a pre-printed "What I do today instead" field that makes the status-quo alternative a structural artifact; drives C-08 conflict detection and amend loop
**Hypothesis:** The primary friction source for most personas is not the artifact itself but the gap between the artifact and their current workflow. Making the do-nothing alternative explicit per persona reveals persona conflicts that purely artifact-focused reviews miss (e.g., Compliance's current manual review process vs. Operator's desire to automate). The inertia field also forces the amend loop to address adoption barriers, not just usability defects.

```
You are running /review-users. Each persona will review the target artifact alongside
their current alternative — what they do today when this feature does not exist or they
choose not to use it.

TARGET ARTIFACT: [paste artifact under review, or provide path]

STOCK PERSONAS (run all 5 in this order):
1. Maker
2. Developer
3. Compliance
4. Supervisor
5. Operator

---

For each persona, fill in this template:

### [PERSONA NAME]

**What I do today instead:**
[1-2 sentences: describe the persona's current workaround or manual process.
This is the inertia baseline — the cost of not adopting.]

**First-person walkthrough:**
[Narrative of reading the artifact. First person throughout. At least one verbatim quote
from the artifact in quotation marks. Flag friction inline: (confusion) / (friction) /
(fear) / (jargon).]

**Where the artifact beats my current process:**
[What the artifact does better than the workaround. Be specific.]

**Where the artifact loses to my current process:**
[What the workaround does better. If nothing: "Current process has no advantage here."]

**Usability score: [1-5]**
Rationale: [1-2 sentences. Tie to the gap between artifact and current process.]

---

Run all 5 personas using this template, then write:

### Cross-Persona Synthesis

**Universal friction (3+ personas):**
Findings shared by 3 or more personas. For each: state the finding, name the personas,
note whether it also appeared in their "loses to current process" field (adoption risk).

**Role-specific friction:**
Friction that appeared in only 1-2 personas. State persona and why role-specific.

**Persona conflicts:**
Cases where the artifact's design helps one persona but hurts another. Look especially
at cases where the "beats current process" for one persona overlaps with the "loses to
current process" for another. Name the personas and the specific design feature causing
the trade-off.

**Inertia summary:**
Which persona has the strongest pull toward staying with their current process?
Which has the strongest pull toward adopting? What does this mean for rollout sequencing?

**Aggregate usability score:** (P1 + P2 + P3 + P4 + P5) / 5 = X

---

### Amend Loop

If any persona scored below 3/5:
For each sub-3 persona:
1. State persona name, score, and what their current workaround is
2. Quote the artifact text with the highest friction
3. Propose a concrete change that closes the gap between the artifact and the workaround
4. State the expected new score

If all scores >= 3: "Amend loop: not triggered (all scores >= 3)."
```
