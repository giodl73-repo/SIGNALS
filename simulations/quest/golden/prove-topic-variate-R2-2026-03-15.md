---
skill: quest-variate
skill_target: prove-topic
round: R2
date: 2026-03-15
rubric: prove-topic-rubric-v2-2026-03-15.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [inertia_framing, phrasing_register, per_artifact_path_enforcement]
  combined: [V-04, V-05]
r1_high_score: V-01 (96) — GATE S pattern, per-path naming
r2_targets: C-11 (hard gate), C-12 (status-quo anchor at open), C-13 (per-instruction paths)
---

# prove-topic — Variation Round R2

Five complete, runnable skill body prompts. Each is self-contained — no diff, no cross-references.

Round 2 builds on the R1 excellence signals now formalized as C-11, C-12, C-13 in rubric v2.
Single-axis variations (V-01, V-02, V-03) isolate one design decision each.
Combined variations (V-04, V-05) compound the highest-signal combinations.

---

## V-01 — Axis: Inertia Framing (status-quo comparator anchored at session open)

**Variation axis**: Inertia framing — the status-quo comparator is named and registered before
any evidence gathering begins. Each evidence stage is required to reference it. Synthesis
confidence is calibrated against it rather than stated in isolation.

**Hypothesis**: Registering the incumbent approach at session open produces confidence levels
that are grounded in a concrete alternative at every stage, rather than appearing as
untethered hedges introduced only at synthesis.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
Five stages execute in order. Each stage writes its artifact before the next begins.

---

## SESSION OPEN — Inertia Registration

Before loading scout signals or framing a hypothesis, register the status-quo comparator.

  Status-quo comparator:
    What does the team do today without this capability?
    Name it in one sentence: [current_practice]

    This comparator is the inertia anchor. Every evidence stage will reference it.
    If evidence does not clearly beat this baseline, the synthesis confidence ceiling is 50.

  Scout load:
    Search: simulations/scout/**/{topic}-*.md
    | Artifact slug | Namespace | Key finding (one sentence) |
    |--------------|-----------|---------------------------|
    | [slug]       | [ns]      | [finding]                 |

    If no scout artifacts found: "No prior signals — hypothesis proceeds from assumption."

---

## STAGE 1 — prove-hypothesis

Frame the claim. The hypothesis must reference the inertia anchor and at least one scout finding.

  Inertia anchor (carry forward from Session Open):
    [current_practice]

  Scout anchor (name the slug and finding that grounds this claim):
    [slug] — [finding]
    If no scout: "No prior signals — stated assumption: [assumption]"

  Claim: [One sentence. "is" or "will". No hedging.]

  Why the inertia anchor is insufficient:
    [One sentence. What gap does the claim address that current_practice cannot?]

  Falsification conditions:
    | ID   | Observable outcome that falsifies the claim |
    |------|---------------------------------------------|
    | F-01 | [outcome] |
    | F-02 | [outcome] |
    | F-00 | [Evidence that current_practice is sufficient — the null hypothesis observable.] |

  Initial confidence: [N]/100
  Rationale: [3 sentences: (1) scout anchor or absence, (2) gap vs. inertia anchor, (3) confidence basis]

Write to: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
Frontmatter fields: skill, topic, date, claim_summary, confidence, scout_anchor,
                   inertia_anchor (text), inertia_gap (text).

Confirm artifact written. Proceed to STAGE 2.

---

## STAGE 2 — prove-websearch

Gather external evidence. At each search block, assess whether findings beat the inertia anchor.

  Hypothesis (carry forward verbatim from STAGE 1 Claim):
    [claim]

  Inertia anchor (carry forward from Session Open):
    [current_practice]

  For each search block:
    Query: [search string]
    | # | Title | URL | Finding | Beats inertia anchor? (Y/N/Unclear) |
    |---|-------|-----|---------|--------------------------------------|

    Rule: Minimum 2 distinct source URLs. If fewer, run supplemental search immediately.

  Inertia assessment:
    Sources confirming claim beats inertia anchor: [N]
    Sources neutral or unclear: [N]
    Sources suggesting inertia anchor is sufficient: [N]

  Verdict token:
    [ ] SUPPORTS hypothesis  [ ] CONTRADICTS hypothesis  [ ] INCONCLUSIVE
    Inertia signal: [BEATS / INSUFFICIENT / CONFLICTED]
    Confidence delta: [+N / -N / 0]

Write to: simulations/prove/websearch/{topic}-websearch-{date}.md
Frontmatter fields: skill, topic, date, verdict_token, confidence_delta,
                   inertia_signal (BEATS/INSUFFICIENT/CONFLICTED), source_count.

Confirm artifact written. Proceed to STAGE 3.

---

## STAGE 3 — prove-interview

Scan internal sources. For each signal, note whether it establishes advantage over the
inertia anchor or merely describes the proposed approach in isolation.

  Inertia anchor (carry forward from Session Open):
    [current_practice]

  Sources to check (in order):
    1. simulations/scout/**/{topic}-*.md    (already loaded — summarize, do not re-derive)
    2. simulations/trace/**/{topic}-*.md
    3. simulations/review/**/{topic}-*.md
    4. simulations/draft/**/{topic}-*.md

  For each artifact found:
    | Source slug | Finding (one sentence) | Inertia status (BEATS/MATCHES/ABSENT) |
    |-------------|------------------------|---------------------------------------|

  If a namespace has no artifacts: write "No {namespace} artifacts found."

  Internal verdict:
    Total signals: [N]
    Signals establishing inertia advantage: [N]
    Gaps: [what the internal record cannot establish for this hypothesis]

Write to: simulations/prove/interview/{topic}-interview-{date}.md
Frontmatter fields: skill, topic, date, signal_count, inertia_advantage_count, gaps_count.

Confirm artifact written. Proceed to STAGE 4.

---

## STAGE 4 — prove-prototype

Construct and run the minimum test that exposes whether the claim holds against the inertia anchor.

  Inertia anchor (carry forward from Session Open):
    [current_practice]

  Hypothesis (carry forward from STAGE 1 Claim):
    [claim]

  Test design:
    What is the smallest test that distinguishes the claim from the inertia anchor?
    Test: [one-sentence test description]

    Expected result if claim is TRUE:  [observable outcome that beats inertia anchor]
    Expected result if claim is FALSE: [observable outcome matching inertia anchor or worse]

  Test execution:
    Method: [how to run the test given available information]
    Outcome: [what was observed]

  Inertia verdict at prototype:
    Does the test result beat the inertia anchor? [BEATS / MATCHES / DEGRADES / UNCLEAR]
    If UNCLEAR: name the specific gap and carry it forward as a thin-evidence flag.

  Confidence ceiling update:
    | Prior ceiling | Prototype verdict | Updated ceiling |
    |---------------|-------------------|-----------------|
    | [N]           | [BEATS/MATCHES/DEGRADES/UNCLEAR] | [N] |

Write to: simulations/prove/prototype/{topic}-prototype-{date}.md
Frontmatter fields: skill, topic, date, test_outcome, inertia_verdict,
                   confidence_ceiling, thin_evidence_flag (text or "none").

Confirm artifact written. Proceed to STAGE 5.

---

## STAGE 5 — prove-synthesize

Write the final evidence brief. This is the terminal artifact. It takes a position.
Synthesis MUST NOT begin until all four prior artifacts are confirmed written.

  Inertia anchor (carry forward from Session Open):
    [current_practice]

  Confidence ceiling (carry forward from STAGE 4):
    [N]

  Write six prose sections under these headers:

  **Inertia Verdict**
    Does the combined evidence establish clear advantage over [current_practice]?
    State the verdict in the first sentence. Name the inertia anchor explicitly.

  **Confidence**
    Score (0-100, must not exceed ceiling). Name which signals drove it up, what held it down.
    If any stage returned thin evidence, name the stage and its confidence effect.

  **Key Evidence**
    Top 3 signals. For each: finding, stage source, and whether it beats the inertia anchor.

  **Counter-Evidence**
    The strongest argument that the inertia anchor remains sufficient. Name source and stage.
    This section is mandatory. Omitting it is not permitted.

  **Caveats**
    Contexts where the inertia anchor may still be preferable. Be specific — avoid generic hedges.

  **Handoff**
    ready_for_topic_story: true
    Topic: {topic}
    Confidence: [score] / 100 — [yes / no / maybe]
    Inertia anchor defeated: [true / false / uncertain]
    Recommended next skill: /topic:story

Write to: simulations/prove/synthesize/{topic}-synthesize-{date}.md
Frontmatter fields: skill, topic, date, verdict (yes/no/maybe), confidence, ceiling_applied,
                   inertia_anchor_defeated (true/false/uncertain),
                   ready_for_topic_story: true,
                   stages_completed: [hypothesis, websearch, interview, prototype, synthesize].

Confirm artifact written. Campaign complete.

---

## Completion Check

- [ ] Session Open: Inertia anchor registered (current_practice on file)
- [ ] Session Open: Scout record loaded
- [ ] STAGE 1: {topic}-hypothesis-{date}.md written
- [ ] STAGE 2: {topic}-websearch-{date}.md written
- [ ] STAGE 3: {topic}-interview-{date}.md written
- [ ] STAGE 4: {topic}-prototype-{date}.md written
- [ ] STAGE 5: {topic}-synthesize-{date}.md written
- [ ] Synthesis references inertia anchor by name
- [ ] Synthesis includes Handoff with ready_for_topic_story: true

If any item is unchecked, complete it before reporting done.
```

---

## V-02 — Axis: Phrasing Register (conversational, task-as-guidance)

**Variation axis**: Phrasing register — instructions are written in second-person conversational
tone ("You've loaded the scout record. Now frame your hypothesis.") rather than gated block
notation. Stage transitions are narrative bridges, not structural walls.

**Hypothesis**: Conversational instruction prose produces more natural stage completions with
fewer mechanical skips because the model follows reasoning continuity rather than template
fill-in, reducing the cognitive overhead that causes structural shortcuts.

---

```
Topic: {topic}
Date:  {date}

You're running the full prove evidence campaign for {topic}. Think of this as a five-act
investigation — each act produces one artifact, and the next act can't begin until the
current one is written. Let's go in order.

---

### Before you start — load what you already know

Look up any scout artifacts for this topic:
  simulations/scout/**/{topic}-*.md

If you find any, list them in a quick table — slug, namespace, and the one finding that
matters most. If you find nothing, note that and flag that the hypothesis will start from
stated assumptions.

Then write down, in plain language, what the team does today without this capability.
That's your inertia anchor — you'll come back to it at every stage.

---

### Act 1 — Frame the hypothesis (prove-hypothesis)

Now that you know what the scout found and what the status quo looks like, write the claim.

Name your scout anchor — the specific artifact and finding that grounds your claim. If
there's no scout record, say so and name the assumption you're starting from instead.

Then write the claim itself: one sentence, "is" or "will", no hedging.

Below the claim, note why the status quo is insufficient — what gap does your claim address
that the current approach can't? Then give two falsification conditions: observable outcomes
that would prove the claim wrong. Add an F-00: what would you need to see to be convinced
the status quo is actually fine?

Close with a confidence score (0-100) and three sentences explaining it: what the scout
anchor says, where the status-quo gap lies, and why your starting confidence is where it is.

Now write the artifact:
  simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
Include in frontmatter: skill, topic, date, claim_summary, confidence, scout_anchor (slug
or "none"), inertia_anchor (the status-quo text), inertia_gap.

Say "hypothesis artifact written" before moving to Act 2.

---

### Act 2 — Search for external evidence (prove-websearch)

You have a claim. Now find out what the wider world says about it.

Run at least two search blocks. For each, write the query, then a table with the results —
title, URL, what they found, and whether each finding beats the inertia anchor you defined
in Act 1. If a search returns fewer than two distinct sources, run a supplemental query
immediately and document it.

After the searches, give me a quick tally: how many sources confirm the claim beats the
status quo, how many are neutral, and how many suggest the status quo might be enough.

Then set a verdict token — SUPPORTS, CONTRADICTS, or INCONCLUSIVE — and state an inertia
signal: BEATS, INSUFFICIENT, or CONFLICTED. Adjust your confidence score accordingly.

Write the artifact:
  simulations/prove/websearch/{topic}-websearch-{date}.md
Frontmatter: skill, topic, date, verdict_token, confidence_delta, inertia_signal, source_count.

Say "websearch artifact written" before moving to Act 3.

---

### Act 3 — Interview internal sources (prove-interview)

Now scan what your own project already knows. Check these in order:
  1. Scout artifacts (already loaded — just summarize, don't re-derive)
  2. simulations/trace/**/{topic}-*.md
  3. simulations/review/**/{topic}-*.md
  4. simulations/draft/**/{topic}-*.md

For each artifact you find, give me a row: slug, key finding, and whether it establishes
advantage over the inertia anchor (BEATS / MATCHES / ABSENT). If a namespace is empty,
note it explicitly — "No trace artifacts found" is fine.

At the end, tell me how many total signals you found, how many establish inertia advantage,
and what the internal record still can't tell you about this hypothesis.

Write the artifact:
  simulations/prove/interview/{topic}-interview-{date}.md
Frontmatter: skill, topic, date, signal_count, inertia_advantage_count, gaps_count.

Say "interview artifact written" before moving to Act 4.

---

### Act 4 — Run a prototype test (prove-prototype)

You've seen what the outside world says and what your own project knows. Now design the
smallest test that could settle the question against the inertia anchor.

Describe the test in one sentence. Then write out what you'd expect to see if the claim is
true vs. if the status quo is still sufficient. Run the test using whatever information
you have, and report the outcome.

Then make a call: does the result BEAT, MATCH, DEGRADE, or leave UNCLEAR the inertia
anchor? If unclear, name the specific gap — that becomes a thin-evidence flag that carries
into synthesis.

Update the confidence ceiling based on the prototype verdict and write it down.

Write the artifact:
  simulations/prove/prototype/{topic}-prototype-{date}.md
Frontmatter: skill, topic, date, test_outcome, inertia_verdict, confidence_ceiling,
             thin_evidence_flag (text or "none").

Say "prototype artifact written" before moving to Act 5.

---

### Act 5 — Synthesize the case (prove-synthesize)

This is the final act. You've run four stages — now make the case.

Start with the inertia verdict: does the combined evidence establish clear advantage over
the status quo you named at the start? Say so in the first sentence, and name the status quo.

Then give a confidence score (0-100, can't exceed the ceiling from Act 4). Say what drove
it up and what held it down. If any stage came back thin, name it and explain its effect.

Write your top three pieces of evidence — what they found, which stage they came from, and
whether they beat the inertia anchor. Then write the strongest argument for why the status
quo might still be fine. Don't skip this; it's required.

Note any contexts where the status quo might still be the better choice. Be specific.

Close with the handoff block:
  ready_for_topic_story: true
  Topic: {topic}
  Confidence: [score] / 100 — [yes / no / maybe]
  Inertia anchor defeated: [true / false / uncertain]
  Recommended next skill: /topic:story

Write the artifact:
  simulations/prove/synthesize/{topic}-synthesize-{date}.md
Frontmatter: skill, topic, date, verdict (yes/no/maybe), confidence, ceiling_applied,
             inertia_anchor_defeated (true/false/uncertain),
             ready_for_topic_story: true,
             stages_completed: [hypothesis, websearch, interview, prototype, synthesize].

Say "campaign complete" once the synthesis artifact is written.

---

### Quick check before you finish

Run through this list. If anything is missing, go back and fix it:
- Scout record loaded (or absence noted)
- Inertia anchor named at session open, referenced in every artifact
- hypothesis artifact written
- websearch artifact written
- interview artifact written
- prototype artifact written
- synthesize artifact written
- Synthesis has the handoff block with ready_for_topic_story: true
```

---

## V-03 — Axis: Per-Artifact Path Enforcement (every write instruction names the full path)

**Variation axis**: Per-artifact path enforcement — every single write instruction in the
prompt names the exact target file path in `{topic}-{stage}-{date}.md` form. No prefixes
are defined once and relied upon. Each stage carries its own path instruction.

**Hypothesis**: Naming the exact artifact path in every write instruction eliminates prefix
drift and silent-skip failures without requiring the model to recall a rule stated earlier —
because the path is present at the point of use, not only at the session opening.

---

```
Topic: {topic}
Date:  {date}

Prove evidence campaign. Five stages. One artifact per stage. Forward only.

---

## STAGE 0 — SCOUT LOAD

Search: simulations/scout/**/{topic}-*.md

Record findings:
  | Artifact slug | Namespace | Key finding (one sentence) |
  |--------------|-----------|---------------------------|
  | [slug]       | [ns]      | [finding]                 |

  If none found: "No prior scout signals."

Status-quo anchor:
  What does the team do today without this capability? [current_practice — one sentence]

This anchor carries forward to every stage. Do not restate it from memory; copy it forward.

---

## STAGE 1 — HYPOTHESIS

Scout anchor (from STAGE 0 — name the slug):
  [slug] — [finding]
  If no scout: "No prior signals. Assumption: [assumption]"

Status-quo anchor (copy from STAGE 0):
  [current_practice]

Claim: [One sentence. "is" or "will". No hedging.]

Status-quo gap (why the anchor is insufficient):
  [One sentence.]

Falsification:
  | ID   | Observable outcome that falsifies the claim |
  |------|---------------------------------------------|
  | F-01 | |
  | F-02 | |
  | F-00 | [Evidence that status-quo anchor is sufficient] |

Confidence: [N]/100
Rationale: [(1) scout anchor, (2) status-quo gap, (3) confidence basis — 3 sentences]

WRITE ARTIFACT:
  Path: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
  Frontmatter: skill=prove-hypothesis, topic={topic}, date={date},
               claim_summary=[claim], confidence=[N], scout_anchor=[slug or "none"],
               status_quo_anchor=[current_practice], status_quo_gap=[gap text].

Confirm: "{topic}-hypothesis-{date}.md written."
Proceed to STAGE 2 only after confirming.

---

## STAGE 2 — WEB SEARCH

Hypothesis (copy verbatim from STAGE 1 Claim):
  [claim]

Status-quo anchor (copy from STAGE 0):
  [current_practice]

Search Block A:
  Query: [search string — targets claim directly]
  | # | Title | URL | Finding | Beats status-quo anchor? (Y/N/Unclear) |
  |---|-------|-----|---------|----------------------------------------|

Search Block B:
  Query: [search string — targets inertia / alternatives]
  | # | Title | URL | Finding | Beats status-quo anchor? (Y/N/Unclear) |
  |---|-------|-----|---------|----------------------------------------|

Rule: Minimum 2 distinct source URLs per block. If fewer: run supplemental query immediately.
  Supplemental query: [string]
  Additional source: [title — URL — finding]

Verdict:
  Token: [ ] SUPPORTS  [ ] CONTRADICTS  [ ] INCONCLUSIVE
  Inertia signal: [BEATS / INSUFFICIENT / CONFLICTED]
  Confidence delta: [+N / -N / 0]
  Thin-evidence flag: [stage 2 thin evidence description, or "none"]

WRITE ARTIFACT:
  Path: simulations/prove/websearch/{topic}-websearch-{date}.md
  Frontmatter: skill=prove-websearch, topic={topic}, date={date},
               verdict_token=[token], confidence_delta=[N],
               inertia_signal=[BEATS/INSUFFICIENT/CONFLICTED],
               source_count=[N], thin_evidence_flag=[text or "none"].

Confirm: "{topic}-websearch-{date}.md written."
Proceed to STAGE 3 only after confirming.

---

## STAGE 3 — INTERVIEW

Status-quo anchor (copy from STAGE 0):
  [current_practice]

Sources (check in order):
  1. simulations/scout/**/{topic}-*.md     (summarize from STAGE 0 load — do not re-derive)
  2. simulations/trace/**/{topic}-*.md
  3. simulations/review/**/{topic}-*.md
  4. simulations/draft/**/{topic}-*.md

For each artifact found:
  | Source slug | Finding (one sentence) | Beats status-quo anchor? (BEATS/MATCHES/ABSENT) |
  |-------------|------------------------|--------------------------------------------------|

  If namespace empty: "No {namespace} artifacts found."

Summary:
  Total signals found: [N]
  Signals beating status-quo anchor: [N]
  Gaps (what internal record cannot establish): [list]
  Thin-evidence flag: [stage 3 thin evidence description, or "none"]

WRITE ARTIFACT:
  Path: simulations/prove/interview/{topic}-interview-{date}.md
  Frontmatter: skill=prove-interview, topic={topic}, date={date},
               signal_count=[N], inertia_advantage_count=[N],
               gaps_count=[N], thin_evidence_flag=[text or "none"].

Confirm: "{topic}-interview-{date}.md written."
Proceed to STAGE 4 only after confirming.

---

## STAGE 4 — PROTOTYPE

Status-quo anchor (copy from STAGE 0):
  [current_practice]

Hypothesis (copy from STAGE 1 Claim):
  [claim]

Test (smallest test that distinguishes claim from status-quo anchor):
  Design: [one sentence]
  Expected if TRUE:  [outcome beating status-quo anchor]
  Expected if FALSE: [outcome matching status-quo anchor or worse]

Execution:
  Method: [how to run given available information]
  Outcome: [what was observed]

Prototype verdict:
  [ ] BEATS status-quo anchor
  [ ] MATCHES status-quo anchor (no improvement)
  [ ] DEGRADES vs status-quo anchor
  [ ] UNCLEAR — gap: [specific gap that makes verdict ambiguous]

Confidence ceiling:
  | Phase coverage | Inertia verdict | Ceiling |
  |----------------|-----------------|---------|
  | [phases]       | [BEATS/MATCHES/DEGRADES/UNCLEAR] | [N] |

Thin-evidence flag: [stage 4 gap description if UNCLEAR, or "none"]

WRITE ARTIFACT:
  Path: simulations/prove/prototype/{topic}-prototype-{date}.md
  Frontmatter: skill=prove-prototype, topic={topic}, date={date},
               test_outcome=[outcome], inertia_verdict=[BEATS/MATCHES/DEGRADES/UNCLEAR],
               confidence_ceiling=[N], thin_evidence_flag=[text or "none"].

Confirm: "{topic}-prototype-{date}.md written."
Proceed to STAGE 5 only after confirming.

---

## STAGE 5 — SYNTHESIS

Status-quo anchor (copy from STAGE 0):
  [current_practice]

Confidence ceiling (copy from STAGE 4):
  [N]

Thin-evidence flags from all stages (enumerate):
  Stage 2: [flag or "none"]
  Stage 3: [flag or "none"]
  Stage 4: [flag or "none"]

Synthesis sections (prose, in order):

  **Inertia Verdict**
    [Does the combined evidence establish advantage over {current_practice}? First sentence states verdict. Names the anchor explicitly.]

  **Confidence**
    [Score (0-100, must not exceed ceiling). What drove it up. What held it down. Per-stage thin-evidence effect if any.]

  **Key Evidence**
    [Top 3 signals. For each: finding, source stage, whether it beats the anchor.]

  **Counter-Evidence**
    [Strongest argument that the status-quo anchor remains sufficient. Source and stage required. This section is mandatory.]

  **Caveats**
    [Contexts where the status-quo anchor may still be preferable. Specific, not generic.]

  **Handoff**
    ready_for_topic_story: true
    Topic: {topic}
    Confidence: [score] / 100 — [yes / no / maybe]
    Inertia anchor defeated: [true / false / uncertain]
    Recommended next skill: /topic:story

WRITE ARTIFACT:
  Path: simulations/prove/synthesize/{topic}-synthesize-{date}.md
  Frontmatter: skill=prove-synthesize, topic={topic}, date={date},
               verdict=[yes/no/maybe], confidence=[N], ceiling_applied=[N],
               inertia_anchor_defeated=[true/false/uncertain],
               ready_for_topic_story=true,
               stages_completed=[hypothesis, websearch, interview, prototype, synthesize].

Confirm: "{topic}-synthesize-{date}.md written. Campaign complete."

---

## ARTIFACT REGISTRY (complete at campaign close)

| Stage | Artifact path | Written |
|-------|---------------|---------|
| 1 | simulations/prove/hypothesis/{topic}-hypothesis-{date}.md | [ ] |
| 2 | simulations/prove/websearch/{topic}-websearch-{date}.md   | [ ] |
| 3 | simulations/prove/interview/{topic}-interview-{date}.md   | [ ] |
| 4 | simulations/prove/prototype/{topic}-prototype-{date}.md   | [ ] |
| 5 | simulations/prove/synthesize/{topic}-synthesize-{date}.md | [ ] |

Fill this table at campaign close. If any cell is unchecked, complete the missing artifact.
```

---

## V-04 — Combined: GATE S + Inertia Framing (C-11 + C-12)

**Variation axis**: Combined — GATE S hard-blocks hypothesis formation until the scout artifact
is confirmed (C-11), and the status-quo comparator is registered at session open and referenced
at each evidence stage (C-12). Both protections are active simultaneously.

**Hypothesis**: The C-11 gate and C-12 anchor address two independent failure modes — a
hypothesis formed before the scout is loaded, and a confidence judgment made without a concrete
baseline — and combining them is the minimum configuration that prevents both simultaneously.

---

```
Topic: {topic}
Date:  {date}

Prove evidence campaign. Five stages in order. One artifact per stage.
Two session-open registrations are required before any evidence work begins.

---

## SESSION OPEN — REGISTRATIONS

Before any hypothesis formation, complete both registrations.

REGISTRATION 1 — SCOUT LOAD

  Search: simulations/scout/**/{topic}-*.md

  | Artifact slug | Namespace | Key finding (one sentence) |
  |--------------|-----------|---------------------------|
  | [slug]       | [ns]      | [finding]                 |

  If no artifacts found: "No prior scout signals."

REGISTRATION 2 — INERTIA ANCHOR

  What does the team do today without this capability?
  Anchor: [current_practice — one sentence]

  This anchor is registered now and must be referenced at each subsequent stage.
  A synthesis confidence level that does not reference this anchor is invalid.

GATE S:
  [ ] Scout record on file (or absence noted)
  [ ] Inertia anchor registered

  Do not begin Stage 1 until both checkboxes can be checked.
  Check them now, explicitly, before proceeding.

---

## STAGE 1 — prove-hypothesis

GATE S must be complete before this stage opens.

Scout anchor (from REGISTRATION 1 — name the slug):
  [slug] — [finding]
  If no scout: "No prior signals. Assumption: [state it]."

Inertia anchor (copy from REGISTRATION 2):
  [current_practice]

Claim: [One sentence. "is" or "will". No hedging.]

Why inertia anchor is insufficient for this capability:
  [One sentence naming the specific gap.]

Falsification:
  | ID   | Observable outcome falsifying the claim |
  |------|------------------------------------------|
  | F-01 | [outcome] |
  | F-02 | [outcome] |
  | F-00 | [Evidence showing current_practice is sufficient — the null.] |

Confidence: [N]/100
Rationale: [3 sentences: (1) scout anchor, (2) inertia gap, (3) confidence basis]

Write to: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
Frontmatter: skill, topic, date, claim_summary, confidence, scout_anchor,
             inertia_anchor, inertia_gap, gate_s_cleared: true.

Confirm artifact written. Proceed to STAGE 2.

---

## STAGE 2 — prove-websearch

Inertia anchor (copy from SESSION OPEN REGISTRATION 2):
  [current_practice]

Hypothesis (copy verbatim from STAGE 1 Claim):
  [claim]

For each search block:
  Query: [search string]
  | # | Title | URL | Finding | vs. inertia anchor (BEATS/MATCHES/DEGRADES/UNCLEAR) |
  |---|-------|-----|---------|------------------------------------------------------|

  Rule: Minimum 2 distinct source URLs per block. If fewer: run supplemental query.

Inertia assessment at Stage 2:
  [ ] Evidence beats inertia anchor on balance
  [ ] Evidence matches inertia anchor (no clear improvement)
  [ ] Evidence conflicts — cannot determine
  Inertia signal: [BEATS / INSUFFICIENT / CONFLICTED]

Thin-evidence check:
  If fewer than 4 distinct sources found: set thin_evidence_flag = "Stage 2 thin — [reason]"
  Otherwise: thin_evidence_flag = "none"

Verdict token:
  [ ] SUPPORTS  [ ] CONTRADICTS  [ ] INCONCLUSIVE
  Confidence delta: [+N / -N / 0]

Write to: simulations/prove/websearch/{topic}-websearch-{date}.md
Frontmatter: skill, topic, date, verdict_token, confidence_delta, inertia_signal,
             source_count, thin_evidence_flag.

Confirm artifact written. Proceed to STAGE 3.

---

## STAGE 3 — prove-interview

Inertia anchor (copy from SESSION OPEN REGISTRATION 2):
  [current_practice]

Sources (check in order):
  1. simulations/scout/**/{topic}-*.md     (summarize from REGISTRATION 1 — do not re-derive)
  2. simulations/trace/**/{topic}-*.md
  3. simulations/review/**/{topic}-*.md
  4. simulations/draft/**/{topic}-*.md

For each artifact found:
  | Slug | Finding | vs. inertia anchor (BEATS/MATCHES/ABSENT) |
  |------|---------|-------------------------------------------|

  If namespace empty: "No {namespace} artifacts found."

Inertia assessment at Stage 3:
  Total signals: [N]
  Signals establishing advantage over inertia anchor: [N]
  Thin-evidence check: [gap if thin, or "none"]

Write to: simulations/prove/interview/{topic}-interview-{date}.md
Frontmatter: skill, topic, date, signal_count, inertia_advantage_count,
             gaps_count, thin_evidence_flag.

Confirm artifact written. Proceed to STAGE 4.

---

## STAGE 4 — prove-prototype

Inertia anchor (copy from SESSION OPEN REGISTRATION 2):
  [current_practice]

Hypothesis (copy from STAGE 1 Claim):
  [claim]

Test (distinguishes claim from inertia anchor):
  Design:         [one sentence]
  Expected TRUE:  [outcome beating inertia anchor]
  Expected FALSE: [outcome matching inertia anchor or worse]
  Outcome:        [what was observed]

Prototype verdict:
  vs. inertia anchor: [ ] BEATS  [ ] MATCHES  [ ] DEGRADES  [ ] UNCLEAR
  If UNCLEAR: gap = [specific ambiguity — carry to synthesis]

Thin-evidence flags from all stages (propagate forward):
  Stage 2: [flag or "none"]
  Stage 3: [flag or "none"]
  Stage 4: [flag or "none"]

Confidence ceiling:
  Phase coverage: [phases reached]
  Inertia verdict: [BEATS/MATCHES/DEGRADES/UNCLEAR]
  Ceiling: [N]

Write to: simulations/prove/prototype/{topic}-prototype-{date}.md
Frontmatter: skill, topic, date, test_outcome, inertia_verdict, confidence_ceiling,
             thin_evidence_flags (Stage2/Stage3/Stage4 — enumerate or "none").

Confirm artifact written. Proceed to STAGE 5.

---

## STAGE 5 — prove-synthesize

Terminal artifact. No further stages follow.

  Inertia anchor (copy from SESSION OPEN REGISTRATION 2):
    [current_practice]

  Confidence ceiling (copy from STAGE 4):
    [N]

  Thin-evidence flags (from STAGE 4 aggregate):
    [list or "none"]

Synthesis sections:

  **Inertia Verdict**
    Does evidence from all four stages establish advantage over [current_practice]?
    State verdict in first sentence. Name the inertia anchor explicitly.
    Reference at least one finding from each of the four evidence stages.

  **Confidence**
    Score (0-100, must not exceed ceiling). Signal drivers (up and down).
    Each thin-evidence flag from the propagation chain: name it and its confidence effect.

  **Key Evidence**
    Top 3 signals. For each: finding, stage, and inertia verdict (BEATS/MATCHES/ABSENT).

  **Counter-Evidence**
    Strongest case for retaining the inertia anchor. Source and stage required. Mandatory.

  **Caveats**
    Contexts where the inertia anchor remains preferable. Specific.

  **Handoff**
    ready_for_topic_story: true
    Topic: {topic}
    Confidence: [score] / 100 — [yes / no / maybe]
    Inertia anchor defeated: [true / false / uncertain]
    Thin-evidence stages: [list or "none"]
    Recommended next skill: /topic:story

Write to: simulations/prove/synthesize/{topic}-synthesize-{date}.md
Frontmatter: skill, topic, date, verdict (yes/no/maybe), confidence, ceiling_applied,
             inertia_anchor_defeated (true/false/uncertain),
             ready_for_topic_story: true,
             stages_completed: [hypothesis, websearch, interview, prototype, synthesize],
             gate_s_cleared: true.

Confirm artifact written. Campaign complete.

---

## Completion Checklist

- [ ] GATE S: scout record on file (or absence noted)
- [ ] GATE S: inertia anchor registered
- [ ] GATE S: both boxes checked before Stage 1 opened
- [ ] {topic}-hypothesis-{date}.md written — gate_s_cleared: true in frontmatter
- [ ] {topic}-websearch-{date}.md written — inertia anchor referenced
- [ ] {topic}-interview-{date}.md written — inertia anchor referenced
- [ ] {topic}-prototype-{date}.md written — inertia anchor referenced
- [ ] {topic}-synthesize-{date}.md written — inertia anchor named in first sentence
- [ ] Thin-evidence flags propagated from each stage through to synthesis
- [ ] Synthesis handoff includes ready_for_topic_story: true

If any item is unchecked, complete it before reporting done.
```

---

## V-05 — Combined: GATE S + Inertia Framing + Per-Artifact Path Enforcement (C-11 + C-12 + C-13)

**Variation axis**: Combined — all three R2 excellence targets active simultaneously. The scout
gate hard-blocks hypothesis formation (C-11), the status-quo comparator is anchored at session
open (C-12), and every write instruction names the exact artifact path (C-13). This is the
aspirational ceiling configuration.

**Hypothesis**: The three protections address three independent failure modes at three different
points in the campaign — hypothesis before scout load, evidence calibrated without a baseline,
and prefix drift in multi-stage sessions. Compounding all three produces a campaign where each
failure mode is blocked at its point of origin rather than caught downstream.

---

```
Topic: {topic}
Date:  {date}

Prove evidence campaign — five stages, forward only.
Three protections are active throughout: scout gate, inertia anchor, per-path write enforcement.

---

## SESSION OPEN

Complete both registrations. Do not begin Stage 1 until GATE S clears.

REGISTRATION 1 — SCOUT RECORD
  Search: simulations/scout/**/{topic}-*.md
  | Artifact slug | Namespace | Key finding (one sentence) |
  |--------------|-----------|---------------------------|
  | [slug]       | [ns]      | [finding]                 |
  If none found: "No prior scout signals. Hypothesis proceeds from stated assumption."

REGISTRATION 2 — INERTIA ANCHOR
  What does the team do today without this capability? (one sentence)
  ANCHOR: [current_practice]
  This anchor is fixed for the session. Copy it forward verbatim at each stage.

GATE S
  [ ] REGISTRATION 1 complete (scout record on file or absence noted)
  [ ] REGISTRATION 2 complete (inertia anchor registered)
  State both boxes checked. Do not write the hypothesis until you have done so.

---

## STAGE 1 — prove-hypothesis

GATE S required before this stage.

  Scout anchor (from REGISTRATION 1):
    [Slug] — [one-sentence finding]
    If no scout: "No prior signals. Starting assumption: [state it]."

  Inertia anchor (copy verbatim from REGISTRATION 2):
    [current_practice]

  Claim: [One sentence. "is" or "will". No hedging.]

  Inertia gap (why the anchor is insufficient):
    [One sentence.]

  Falsification:
    | ID   | Observable outcome falsifying the claim |
    |------|------------------------------------------|
    | F-01 | [outcome] |
    | F-02 | [outcome] |
    | F-00 | [Evidence that current_practice is sufficient — the null.] |

  Confidence: [N]/100
  Rationale: [(1) scout anchor or absence, (2) inertia gap, (3) confidence basis — 3 sentences]

  WRITE:
    File: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
    Frontmatter: skill=prove-hypothesis, topic={topic}, date={date},
                 claim_summary=[claim], confidence=[N], scout_anchor=[slug or "none"],
                 inertia_anchor=[current_practice], inertia_gap=[gap], gate_s_cleared=true.
    Confirm: "Written: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md"

Do not open Stage 2 until write is confirmed.

---

## STAGE 2 — prove-websearch

  Hypothesis (copy verbatim from Stage 1 Claim): [claim]

  Inertia anchor (copy verbatim from REGISTRATION 2): [current_practice]

  Search Block A:
    Query: [search string — claim-direct]
    | # | Title | URL | Finding | vs. inertia anchor |
    |---|-------|-----|---------|---------------------|
    (Y = BEATS, N = MATCHES or worse, ? = UNCLEAR)

  Search Block B:
    Query: [search string — inertia / alternatives]
    | # | Title | URL | Finding | vs. inertia anchor |
    |---|-------|-----|---------|---------------------|

  Rule: If any block has fewer than 2 distinct URLs, run supplemental search:
    Supplemental query: [string]
    Source: [title — URL — finding — vs. anchor]

  Inertia signal: [BEATS / INSUFFICIENT / CONFLICTED]
  Verdict token: [ ] SUPPORTS  [ ] CONTRADICTS  [ ] INCONCLUSIVE
  Confidence delta: [+N / -N / 0]
  Thin-evidence flag: [description if < 4 distinct sources total, else "none"]

  WRITE:
    File: simulations/prove/websearch/{topic}-websearch-{date}.md
    Frontmatter: skill=prove-websearch, topic={topic}, date={date},
                 verdict_token=[token], confidence_delta=[N],
                 inertia_signal=[BEATS/INSUFFICIENT/CONFLICTED],
                 source_count=[N], thin_evidence_flag=[text or "none"].
    Confirm: "Written: simulations/prove/websearch/{topic}-websearch-{date}.md"

Do not open Stage 3 until write is confirmed.

---

## STAGE 3 — prove-interview

  Inertia anchor (copy verbatim from REGISTRATION 2): [current_practice]

  Sources (check in order):
    1. simulations/scout/**/{topic}-*.md     (summarize from REGISTRATION 1)
    2. simulations/trace/**/{topic}-*.md
    3. simulations/review/**/{topic}-*.md
    4. simulations/draft/**/{topic}-*.md

  For each artifact:
    | Slug | Finding | vs. inertia anchor (BEATS/MATCHES/ABSENT) |
    |------|---------|-------------------------------------------|

  If namespace empty: "No {namespace} artifacts found."

  Summary:
    Total signals: [N]
    Inertia advantage signals: [N]
    Gaps: [what internal record cannot establish]
    Thin-evidence flag: [description or "none"]

  WRITE:
    File: simulations/prove/interview/{topic}-interview-{date}.md
    Frontmatter: skill=prove-interview, topic={topic}, date={date},
                 signal_count=[N], inertia_advantage_count=[N],
                 gaps_count=[N], thin_evidence_flag=[text or "none"].
    Confirm: "Written: simulations/prove/interview/{topic}-interview-{date}.md"

Do not open Stage 4 until write is confirmed.

---

## STAGE 4 — prove-prototype

  Inertia anchor (copy verbatim from REGISTRATION 2): [current_practice]
  Hypothesis (copy verbatim from Stage 1 Claim): [claim]

  Test design:
    Smallest test distinguishing claim from inertia anchor:
    Design:         [one sentence]
    Expected TRUE:  [observable outcome that beats inertia anchor]
    Expected FALSE: [observable outcome matching inertia anchor or worse]

  Test execution:
    Method:  [how to run with available information]
    Outcome: [what was observed]

  Prototype verdict:
    vs. inertia anchor: [ ] BEATS  [ ] MATCHES  [ ] DEGRADES  [ ] UNCLEAR
    If UNCLEAR: gap = [specific ambiguity — this becomes a thin-evidence flag]

  Thin-evidence propagation (carry all flags from prior stages):
    Stage 2: [flag or "none"]
    Stage 3: [flag or "none"]
    Stage 4: [flag or "none from prototype, or gap text"]

  Confidence ceiling derivation:
    Phase coverage:  [phases reached]
    Inertia verdict: [BEATS/MATCHES/DEGRADES/UNCLEAR]
    Ceiling:         [N]

  WRITE:
    File: simulations/prove/prototype/{topic}-prototype-{date}.md
    Frontmatter: skill=prove-prototype, topic={topic}, date={date},
                 test_outcome=[outcome], inertia_verdict=[verdict], confidence_ceiling=[N],
                 thin_evidence_stage2=[text or "none"],
                 thin_evidence_stage3=[text or "none"],
                 thin_evidence_stage4=[text or "none"].
    Confirm: "Written: simulations/prove/prototype/{topic}-prototype-{date}.md"

Do not open Stage 5 until write is confirmed.

---

## STAGE 5 — prove-synthesize

Terminal stage. No further stages follow this one.

  Inertia anchor (copy verbatim from REGISTRATION 2): [current_practice]
  Confidence ceiling (copy from Stage 4): [N]
  Thin-evidence flags (copy from Stage 4 propagation aggregate):
    Stage 2: [flag or "none"]
    Stage 3: [flag or "none"]
    Stage 4: [flag or "none"]

  Write the following six sections in order:

  **Inertia Verdict**
    Does the combined four-stage evidence establish advantage over [current_practice]?
    State verdict in the first sentence. Name the inertia anchor by its exact registered text.
    Reference at least one evidence finding from each prior stage.

  **Confidence**
    Score 0-100 (must not exceed [N] ceiling). Name what drove it up and what held it down.
    For each non-"none" thin-evidence flag: name the stage and its effect on the score.

  **Key Evidence**
    Top 3 signals. For each: stage source, one-sentence finding, inertia verdict
    (BEATS / MATCHES / ABSENT).

  **Counter-Evidence**
    Strongest argument that [current_practice] remains sufficient.
    Name the source artifact and its stage. This section is mandatory — omission is a
    campaign failure.

  **Caveats**
    Contexts where [current_practice] may still be preferable. Specific — no generic hedges.

  **Handoff**
    ready_for_topic_story: true
    Topic: {topic}
    Confidence: [score] / 100 — [yes / no / maybe]
    Inertia anchor defeated: [true / false / uncertain]
    Thin-evidence stages: [list or "none"]
    Recommended next skill: /topic:story

  WRITE:
    File: simulations/prove/synthesize/{topic}-synthesize-{date}.md
    Frontmatter: skill=prove-synthesize, topic={topic}, date={date},
                 verdict=[yes/no/maybe], confidence=[N], ceiling_applied=[N],
                 inertia_anchor_defeated=[true/false/uncertain],
                 ready_for_topic_story=true,
                 stages_completed=[hypothesis, websearch, interview, prototype, synthesize],
                 gate_s_cleared=true,
                 thin_evidence_stages=[list or "none"].
    Confirm: "Written: simulations/prove/synthesize/{topic}-synthesize-{date}.md"

Campaign complete.

---

## CAMPAIGN CLOSE — ARTIFACT REGISTRY

Fill this table after the synthesis confirm:

| Stage | Artifact | Written |
|-------|----------|---------|
| 0 | Scout record (REGISTRATION 1) | [ ] |
| 0 | Inertia anchor (REGISTRATION 2) | [ ] |
| 1 | simulations/prove/hypothesis/{topic}-hypothesis-{date}.md | [ ] |
| 2 | simulations/prove/websearch/{topic}-websearch-{date}.md   | [ ] |
| 3 | simulations/prove/interview/{topic}-interview-{date}.md   | [ ] |
| 4 | simulations/prove/prototype/{topic}-prototype-{date}.md   | [ ] |
| 5 | simulations/prove/synthesize/{topic}-synthesize-{date}.md | [ ] |

Protections active:
  [ ] GATE S enforced (Stage 1 did not open before GATE S confirmed)
  [ ] Inertia anchor referenced in every stage artifact
  [ ] Every WRITE instruction named the exact {topic}-{stage}-{date}.md path

If any item is unchecked, complete it before reporting done.
```
