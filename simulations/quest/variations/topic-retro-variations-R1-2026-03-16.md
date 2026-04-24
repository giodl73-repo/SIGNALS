Now I have everything I need. Generating the 5 variations:

---

# `/topic-retro` — Prompt Variations V-01 through V-05

**Skill:** `topic-retro`
**Round:** R1
**Rubric:** `topic-retro-rubric-v1-2026-03-16.md`

---

## V-01 — Output Format: Table-First, Scored Scale

**Axis:** Output format (table vs prose vs list, scoring scale)
**Hypothesis:** Forcing table structure makes C-01/C-02 pass mechanically; a 0–100 accuracy score per namespace makes C-05 concrete and C-07 fall out naturally, reducing evaluator judgment calls.

---

```
You are running /topic-retro.

Post-commitment retrospective on a topic's signals. You will reconstruct the
full signal record, score prediction accuracy per namespace, identify gaps that
would have changed the decision, and surface the one unexpected learning (Echo).

---

SETUP

1. Read topic from invocation. If absent, scan simulations/ for the most recent
   topic directory and confirm with user.
2. Glob simulations/**/{{topic}}-* to collect all signal artifacts.
3. If a strategy.md or topic-new artifact exists, load it to recover the planned
   signal list and the commit decision rationale.
4. If no signals are found, output: "No signals found for topic {{topic}}. Run
   /mock-all to generate synthetic coverage before retro." Stop.

---

EXECUTE — FIVE REQUIRED SECTIONS

Output all five sections below in order. Each section has a required format.
Do not omit or merge sections.

---

### Section 1 — Signal Inventory

Produce a table of every signal gathered. One row per artifact.

| Artifact | Namespace | Date | Signal Type | Summary (1 line) |
|----------|-----------|------|-------------|-----------------|

After the table: total count by namespace as a second summary table.

| Namespace | Count |
|-----------|-------|
| scout     | N     |
| draft     | N     |
| ...       |       |
| **Total** | N     |

Flag any namespace with 0 signals as "ABSENT".

---

### Section 2 — Predicted vs Actual

For each namespace that has at least one signal, produce a table row:

| Namespace | What signals predicted | What actually happened | Match? |
|-----------|----------------------|----------------------|--------|

Match column values: CORRECT / PARTIAL / WRONG / NO-DATA (if post-ship data is
unavailable).

Use the signal artifact summaries from Section 1 as the "predicted" source.
"What actually happened" must reference a specific post-ship observable: user
behavior, support volume, adoption metric, build outcome, or stated outcome from
invoker. If invoker has not supplied post-ship data, state SELF-REPORTED and use
the invoker's account.

---

### Section 3 — Gaps

List every signal type that was absent at commit time but would have changed or
refined the decision. Format as a numbered list:

1. **Gap:** [signal type / namespace]
   **Why it would have mattered:** [1-2 sentences]
   **Skill to run next time:** [specific skill name, e.g., /listen-adoption]

If you determine there are no gaps (rare), you must argue this explicitly in 3+
sentences. A blank section is a rubric failure.

---

### Section 4 — Echo

Exactly one entry. Echo is the finding that no gathered signal predicted.
It must be post-ship observable, not a known unknown at commit time.

**Echo:** [name it in one sentence]
**Why it was unpredicted:** [which signals were closest, why they missed]
**Design implication:** [what skill, threshold, or rubric change would catch
this class of surprise earlier]

If you cannot identify a genuine Echo, state: "No Echo identified. All outcomes
were within signal bounds." This is a valid (though rare) result.

---

### Section 5 — Accuracy Verdict

Produce a per-namespace accuracy table:

| Namespace | Signals | Correct | Partial | Wrong | Score (0-100) |
|-----------|---------|---------|---------|-------|---------------|

Score formula per namespace: (Correct * 100 + Partial * 50) / (Correct + Partial + Wrong).
Namespaces with NO-DATA are excluded from denominator.

Then: overall verdict line in this format:
> Overall signal accuracy: [score]/100 — [STRONG / ADEQUATE / WEAK]
> Threshold: STRONG >= 75 | ADEQUATE 50-74 | WEAK < 50

---

AMEND

If an AMEND instruction is present in the invocation, scope all five sections to
the specified signal type or time window. State the applied scope constraint at
the top of the output before Section 1.

---

ARTIFACT

Write output to:
  simulations/topic/{{topic}}-retro-{{date}}.md

Frontmatter:
  skill: topic-retro
  topic: {{topic}}
  item: retro
  date: {{date}}
  skill_version: 1
```

---

## V-02 — Phrasing Register: Conversational

**Axis:** Phrasing register (formal/technical vs conversational, imperative vs descriptive)
**Hypothesis:** Conversational register lowers the barrier to admitting genuine surprises in the Echo section — teams that feel like they are narrating rather than auditing produce more candid, specific Echo entries.

---

```
You are running /topic-retro.

The retro is a conversation with yourself after the feature ships. You had
signals. Some of them were right. Some were wrong. Some things happened that
nobody predicted. The retro captures all of that honestly.

---

GET ORIENTED

Find the topic: look at the invocation first, then scan simulations/ for a
recent topic if nothing was specified.

Collect every signal artifact for the topic by globbing:
  simulations/**/{{topic}}-*

Pull the topic's original strategy or topic-new artifact if it exists — that
tells you what the team planned to gather and why they committed.

If there are no signals at all, say so and stop. Suggest /mock-all to generate
synthetic ones before running retro.

---

WALK THROUGH FIVE QUESTIONS

Work through these five questions in order. Write each answer as a clearly
labeled section. Be direct — the retro is read by the team that ran it, not
an auditor.

---

**Question 1: What signals did we actually gather?**

List every artifact you found. Group them by namespace. Tell us the count per
namespace. Call out any namespace that was completely empty — that absence is
itself a data point.

Don't invent signals that aren't there. If the record is thin, say it's thin.

---

**Question 2: Were we right?**

For each namespace where signals existed, compare what the signals predicted
against what actually happened after ship.

Be honest about the match: yes (we called it), partial (roughly right, off on
details), or no (we were wrong). Where you don't have post-ship data, say so
and use what the person running the retro reports.

Write this as a conversational comparison — not a table. Two or three sentences
per namespace is enough. Lead with the surprising misses.

---

**Question 3: What did we not have that we should have?**

Name the signal types that were absent at commit time but, looking back, would
have caught something real. Be specific: which skill would have generated that
signal? What would it have caught?

"We should have gathered more signals" is not an answer. Name the namespace,
name the skill, name what it would have surfaced.

---

**Question 4: What happened that nobody predicted?**

Pick exactly one thing — the most surprising post-ship observable. Not something
you vaguely knew might happen. Something that genuinely came out of nowhere
relative to the signals you had.

Call it the Echo. Name it clearly. Explain which signals came closest to
predicting it and why they missed. Then: what would you change in your signal
design to catch this class of thing earlier?

If every outcome landed inside the signal bounds, say so. That's a valid and
useful answer.

---

**Question 5: How good were our signals overall?**

Look at the full picture from Questions 1-3. Give a verdict: were the signals
strong (most predictions correct, few surprises), adequate (roughly useful but
with notable misses), or weak (predictions were mostly off or missing)?

Back the verdict with the evidence from Question 2. One paragraph. End with the
one change that would most improve signal quality on the next topic.

---

AMEND

If the retro is scoped by an AMEND instruction (specific namespace or time
window), apply that scope to all five questions and state it clearly at the top.

---

ARTIFACT

Write output to:
  simulations/topic/{{topic}}-retro-{{date}}.md

Frontmatter:
  skill: topic-retro
  topic: {{topic}}
  item: retro
  date: {{date}}
  skill_version: 1
```

---

## V-03 — Lifecycle Emphasis: Echo-First

**Axis:** Lifecycle emphasis (how much space per phase, how explicit boundaries are)
**Hypothesis:** Surfacing the Echo before running predicted-vs-actual comparison prevents rationalization — teams that discover the surprise first are less likely to quietly absorb it into the accuracy narrative and more likely to treat it as a genuine outlier.

---

```
You are running /topic-retro.

Post-commitment retrospective on a topic's signals. Execution order in this
skill is intentional: Echo is discovered before accuracy is scored. This
prevents the unexpected finding from being absorbed into the predicted-vs-actual
narrative after the fact.

---

SETUP

1. Identify topic from invocation or scan simulations/ for most recent topic.
2. Glob simulations/**/{{topic}}-* to collect all signal artifacts.
3. Load strategy.md or topic-new artifact if present to recover commit rationale
   and planned signal list.
4. If no signals found: output gap notice and stop.

---

PHASE 1 — INVENTORY (compact)

List all signals gathered. This phase is intentionally brief — its purpose is
to establish the record, not to analyze it yet.

Output: a flat list. One line per artifact.
  [namespace] / [artifact name] / [one-phrase summary]

End with: total signal count and list of empty namespaces.

---

PHASE 2 — ECHO (expanded — run before accuracy)

Before scoring any predictions, surface what nobody predicted.

Step 1: For each namespace, ask: did any post-ship outcome fall outside the
range of what these signals could have predicted, even in principle? Make a
candidate list.

Step 2: From the candidates, select exactly one — the most post-ship-observable,
most clearly outside-signal-bounds finding. Name it as the Echo.

If the candidate list is empty, state: "Signal bounds encompassed all observed
outcomes. No Echo." This is a valid result. Stop Phase 2 here.

Step 3 (only if Echo found): write the Echo entry:

**Echo:** [one-sentence name of the unexpected finding]
**Signal proximity:** [which signal came closest to predicting it; why it missed]
**Class of surprise:** [what category of signal would catch this next time]
**Design change:** [specific skill, rubric amendment, or threshold to add]

Phase 2 must complete before Phase 3 begins. The Echo must not be revised after
Phase 3 runs.

---

PHASE 3 — PREDICTED VS ACTUAL

Now score the predictions. For each namespace:

- State what the signals predicted (draw from Phase 1 artifact summaries)
- State what actually happened
- Rate the match: CORRECT / PARTIAL / WRONG / NO-DATA

Write one paragraph per namespace. Do not convert the Echo finding into a WRONG
entry — it belongs to Phase 2 and is outside the accuracy scoring scope.

---

PHASE 4 — GAPS

Identify signal types absent at commit time that would have changed or refined
the decision. Use what Phase 3 surfaced (WRONG and PARTIAL rows) as the primary
gap candidates.

For each gap:
  - Name the missing signal type
  - Name the skill that generates it
  - State specifically what it would have caught

If Echo from Phase 2 implies a structural gap (a signal type that doesn't exist
yet in the namespace catalog), flag it as a DESIGN GAP and note it separately.

---

PHASE 5 — ACCURACY VERDICT

Render a verdict for the signal set as a whole.

Format:
  Accuracy: [N correct] / [N total scored] ([percent]%)
  By namespace: [highest accuracy namespace] ... [lowest accuracy namespace]
  Overall rating: STRONG (>= 75%) / ADEQUATE (50-74%) / WEAK (< 50%)

Then: one-sentence conclusion. What single change would most improve this team's
signal accuracy on the next topic?

---

AMEND

If AMEND instruction scopes to a specific signal type or time window, apply it
throughout all phases. State applied scope before Phase 1.

---

ARTIFACT

Write output to:
  simulations/topic/{{topic}}-retro-{{date}}.md

Frontmatter:
  skill: topic-retro
  topic: {{topic}}
  item: retro
  date: {{date}}
  skill_version: 1
```

---

## V-04 — Role Sequence + Output Format: Auditor-First, Verdict Card

**Axes combined:** Role sequence (inventory auditor runs first, before accuracy analyst) + output format (structured list + compact verdict card at close)
**Hypothesis:** Separating the inventory auditor role from the accuracy analyst role prevents fabricated or misattributed signal entries from propagating into the accuracy scores; a compact verdict card at the end gives teams a scannable takeaway without reading the full retro.

---

```
You are running /topic-retro.

This retro runs two roles in sequence. The Inventory Auditor establishes what
actually exists before any scoring begins. The Accuracy Analyst scores only
what the Auditor confirmed. Roles do not overlap.

---

SETUP

Identify topic from invocation or scan simulations/ for most recent topic.
Glob simulations/**/{{topic}}-* to collect signal artifacts.
Load strategy.md or topic-new artifact if available.

---

ROLE 1 — INVENTORY AUDITOR

Your task: establish the definitive signal record. You are not scoring anything.
You are confirming what exists.

For each signal artifact found:
  - Confirm it names a real namespace skill (not a free-form note)
  - Confirm it has a date
  - Confirm it contains a findable claim or prediction

Output a confirmed inventory list:

  CONFIRMED SIGNALS
  -----------------
  [namespace] | [artifact name] | [date] | [claim or prediction in one phrase]

  EXCLUDED (not confirmed as signal artifacts):
  [any files that failed confirmation, with reason]

  NAMESPACE COVERAGE SUMMARY
  --------------------------
  Present:  [namespaces with >= 1 confirmed signal]
  Absent:   [namespaces with 0 confirmed signals]
  Total confirmed signals: N

Auditor work ends here. Do not proceed to accuracy scoring.

---

ROLE 2 — ACCURACY ANALYST

Your task: score predictions against outcomes, identify gaps, find the Echo,
and render a verdict. You work only from the Auditor's confirmed inventory.
Do not reference excluded artifacts.

**Step A — Predicted vs Actual**

For each namespace in the confirmed inventory:

  Namespace: [name]
  Predicted: [what confirmed signals claimed would happen]
  Actual:    [what post-ship observation shows — use invoker report if
              post-ship data is not in the artifact record]
  Match:     CORRECT / PARTIAL / WRONG / NO-DATA

One block per namespace. No tables. Plain blocks.

**Step B — Gaps**

Review WRONG and PARTIAL matches from Step A. For each:
  - Name the missing signal that would have caught the miss
  - Name the skill to run next time
  - One sentence on what it would have surfaced

Also: review Absent namespaces from the Auditor summary. Flag any absent
namespace whose coverage would have materially changed the commit decision.

**Step C — Echo**

Name exactly one post-ship finding that no confirmed signal predicted.
It must be outside the bounds of the confirmed inventory — not merely an
uncertain outcome. If no such finding exists, state so explicitly.

  Echo:            [one-sentence name]
  Nearest signal:  [which confirmed signal came closest; why it missed]
  Design change:   [skill, rubric amendment, or threshold addition]

**Step D — Verdict Card**

Close with a compact card. This is the scannable takeaway.

  ┌─────────────────────────────────────────────────┐
  │ TOPIC RETRO — {{topic}}                         │
  │ Date: {{date}}                                  │
  ├─────────────────────────────────────────────────┤
  │ Signals confirmed: N                            │
  │ Namespaces present: N / 9                       │
  │ Accuracy: [N correct / N scored] = [%]          │
  │ Rating: STRONG / ADEQUATE / WEAK                │
  ├─────────────────────────────────────────────────┤
  │ Top gap:   [one gap, one skill to fix it]       │
  │ Echo:      [one sentence]                       │
  │ #1 change: [single most important improvement]  │
  └─────────────────────────────────────────────────┘

---

AMEND

If AMEND instruction is present, scope both roles to the specified signal type
or time window. State applied scope before Role 1 begins.

---

ARTIFACT

Write output to:
  simulations/topic/{{topic}}-retro-{{date}}.md

Frontmatter:
  skill: topic-retro
  topic: {{topic}}
  item: retro
  date: {{date}}
  skill_version: 1
```

---

## V-05 — Full Integration: Conversational Register + Inertia Framing + Echo-Expanded Lifecycle

**Axes combined:** Phrasing register (conversational) + lifecycle emphasis (gaps phase expanded, inventory compressed) + inertia framing (explicit counterfactual: would you have made the same commit without this signal set?)
**Hypothesis:** Inertia framing — asking "what would you have done without these signals?" — produces the most actionable gap analysis because it forces the team to name specific counterfactuals rather than abstractly noting absent signal types. Conversational register sustains candor through a longer gap phase.

---

```
You are running /topic-retro.

The goal is not to audit the team. The goal is to get smarter about signals.
You shipped something. The signals either helped you make a better decision,
misled you, or failed to warn you about something real. This retro finds out
which.

The key question running through this entire retro: would you have made the
same commit without these signals? That question is the frame.

---

GET ORIENTED

Pull the topic from the invocation. If none given, find the most recent topic
in simulations/ and confirm.

Collect all signal artifacts: glob simulations/**/{{topic}}-*

Load the original topic strategy or topic-new file if present. That's where
the team recorded why they committed. The retro measures against that.

No signals? Say so. Stop. Suggest /mock-all.

---

SECTION 1 — WHAT WE HAD (keep this brief)

List the signals that existed at commit time. Group by namespace. Note which
namespaces were empty. Total count. That's it for this section — the signal
inventory is a setup step, not the point.

---

SECTION 2 — WOULD YOU HAVE COMMITTED WITHOUT THEM?

For each namespace that contributed a signal, work through this:

  1. What did this namespace's signals tell you?
  2. Did the prediction hold after ship?
  3. If you strip out this namespace's signals entirely — what changes about
     the commit decision? Would you have committed anyway? Delayed? Redesigned?

Write this as a per-namespace narrative. Two to four sentences per namespace.
Be specific. "We would have shipped later" is better than "it helped."

The mismatch between "what the signal predicted" and "what actually happened"
should be explicit here — not softened. Partial predictions count as misses
on the dimensions they missed.

---

SECTION 3 — THE GAPS (expanded — this is the main section)

Gaps are the signals you didn't have that would have changed something real.

Work through this systematically:

**Tier 1 — Gaps that would have changed the commit decision**
These are the high-value gaps. The team might have delayed, descoped, or
redesigned if they had had this signal. Name them first.

For each Tier 1 gap:
  - What signal type was missing?
  - What would it have caught? (Be specific: which outcome, which risk, which
    assumption that proved wrong.)
  - Which skill generates this signal? (Name the exact skill.)
  - Would the inertia alternative — doing nothing, gathering no signals — have
    caught this? (Usually: no. But say so explicitly.)

**Tier 2 — Gaps that would have refined the decision**
These are signals that wouldn't have changed commit/no-commit but would have
produced a better-specified feature. Name them second.

For each Tier 2 gap:
  - What would have been more precise about the outcome?
  - Which skill fills this gap?

**Tier 3 — Gaps that were nice-to-have**
Acknowledge these exist, list them briefly. Don't over-analyze.

If there are genuinely no Tier 1 or Tier 2 gaps, argue this explicitly in at
least four sentences covering: what the signal set covered, what the actual
outcomes were, and why the absence of additional signals was not consequential.

---

SECTION 4 — THE ECHO

One thing. The thing that no signal predicted and that wasn't even a named
unknown at commit time.

Name it. Say which signal came closest to it and why it missed. Then say what
you would change — a specific skill, a rubric amendment, a new threshold, or a
signal type that doesn't exist yet in the namespace catalog.

If everything landed inside signal bounds, say so honestly. That's a good
outcome — note it as evidence that the signal set was well-calibrated.

---

SECTION 5 — THE VERDICT

One paragraph. Honest overall rating: STRONG / ADEQUATE / WEAK. Grounded in
the per-namespace evidence from Section 2.

Then: one sentence answering the frame question.
"Given these signals, the team [would / would not] have made the same commit —
and that [was / was not] the right call."

Close with: the single change — one skill to add, one rubric adjustment, one
threshold — that would make the next topic's signal set materially better.

---

AMEND

If AMEND is present, apply scope throughout all sections. State the applied
scope as the first line of output.

---

ARTIFACT

Write output to:
  simulations/topic/{{topic}}-retro-{{date}}.md

Frontmatter:
  skill: topic-retro
  topic: {{topic}}
  item: retro
  date: {{date}}
  skill_version: 1
```

---

## Summary

| Variation | Primary Axis | Secondary Axes | Key Bet |
|-----------|-------------|----------------|---------|
| V-01 | Output format (table + scored scale) | — | Tables make C-01/C-02 mechanically verifiable; per-namespace 0–100 scores give C-07 for free |
| V-02 | Phrasing register (conversational) | — | Lower register barrier → more candid Echo entries |
| V-03 | Lifecycle emphasis (Echo-first) | — | Discovering the surprise before scoring accuracy prevents post-hoc rationalization |
| V-04 | Role sequence (auditor-first) | Output format (verdict card) | Separating inventory confirmation from scoring prevents fabricated signals from infecting accuracy; verdict card is the scannable takeaway |
| V-05 | Inertia framing | Conversational register + expanded gaps lifecycle | Counterfactual framing ("would you have committed without this?") forces specific gap claims instead of abstract coverage notes |
