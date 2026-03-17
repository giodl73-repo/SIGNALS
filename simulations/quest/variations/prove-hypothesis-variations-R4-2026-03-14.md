**R4 variations written** to `simulations/quest/variations/prove-hypothesis-variations-R4-2026-03-14.md`.

---

## R4 Variation Summary

All five variations address the three new criteria. Here's what each does differently:

| Variation | Axis | C-17 mechanism | C-18 mechanism | C-19 mechanism |
|-----------|------|----------------|----------------|----------------|
| **V-01** | Role sequence (CONTEXT + Archivist) | LOCK GATE / SEAL GATE, separate checklists | `## ARCHIVIST: CONSOLIDATE` | `## CONTEXT: CURRENT STATE` before DECLARE — F-00 born there |
| **V-02** | Output format (prose-only) | DECLARE GATE / COLLECTOR GATE, named in header | `## COLLECTOR: CONSOLIDATE` | `## OPENING: CURRENT STATE` before DECLARE — F-00 born there |
| **V-03** | Lifecycle emphasis (7 phases) | GATE 3: DECLARE LOCK / GATE 5: CONSOLIDATE SEAL | `## PHASE 5: CONSOLIDATE` | `## PHASE 2: INERTIA` before PHASE 3: DECLARE — F-00 born in INERTIA |
| **V-04** | Phrasing register (formal, explicit scope declarations) | `DECLARE GATE (LOCK): Scope -- freezes Claim...` / `CONSOLIDATE GATE (SEAL): Scope -- freezes Final list...` | `## ARCHIVIST: CONSOLIDATE` | `## CLAIMANT: CONTEXT` before CLAIMANT: DECLARE — F-00 born there |
| **V-05** | Conversational + inertia-lead + named COLLECTOR | Two plain-language freeze moments, separate checklists | `## Step 4: COLLECTOR -- Assemble the Final list` | Steps 1-2 interrogate current state before Step 3 claim — F-00 born in Step 2 |

**Key structural insight for R4:** All R3 variations introduced F-00 during the Skeptic pass (C-19 fail). R4 moves F-00 generation to a pre-declare section in every variation — the Skeptic now *validates* F-00 rather than *introducing* it. This single change also naturally strengthens Confidence rationale quality: the gap explanation is written with status-quo context live, not reconstructed retrospectively.
: PRIOR / INERTIA / DECLARE / CHALLENGE / CONSOLIDATE / CONFIDENCE / NAVIGATE) | INERTIA as a named phase before DECLARE makes C-19 structurally unskippable; CONSOLIDATE phase + dual gates satisfies C-17/C-18 by phase sequence |
| **V-04** | Phrasing register (formal/technical with explicit gate scope declarations) | Each gate explicitly names its scope ("freezes X before Y") -- eliminates ambiguity about what each gate covers; strongest C-17 evidence |
| **V-05** | Conversational register + inertia-lead + named COLLECTOR | Opens with "What does the team do today?" before claim; two explicit lock moments in plain language; COLLECTOR as named step makes C-18 visible in numbered format |

### Predicted R4 scores under v4 rubric (denominator /11)

| Variation | C-17 | C-18 | C-19 | All 11 asp? | Essential | Predicted | Golden |
|-----------|------|------|------|-------------|-----------|-----------|--------|
| V-01 | LOCK (claim) + SEAL (Final list) -- separate checklists | ARCHIVIST: CONSOLIDATE at ## level | CONTEXT section before DECLARE asks "What does the team do today?", F-00 born there | YES | 5/5 | 100 | YES |
| V-02 | DECLARE GATE + COLLECTOR GATE -- separate checklists | COLLECTOR: CONSOLIDATE at ## level | OPENING: CURRENT STATE before DECLARE, F-00 born there | YES | 5/5 | 100 | YES |
| V-03 | GATE 3: DECLARE LOCK + GATE 5: CONSOLIDATE SEAL -- separate checklists | PHASE 5: CONSOLIDATE at ## phase level | PHASE 2: INERTIA before PHASE 3: DECLARE, F-00 born in INERTIA | YES | 5/5 | 100 | YES |
| V-04 | DECLARE GATE (LOCK) with explicit scope + CONSOLIDATE GATE (SEAL) with explicit scope | ARCHIVIST: CONSOLIDATE at ## level | CLAIMANT: CONTEXT before CLAIMANT: DECLARE, F-00 born in CONTEXT | YES | 5/5 | 100 | YES |
| V-05 | LOCKED after Step 3 (claim) + SEALED after Step 4 COLLECTOR -- separate checklists | Step 4: COLLECTOR at ## level, named role | Steps 1-2 interrogate status-quo before Step 3 claim; F-00 born in Step 2 | YES | 5/5 | 100 | YES |

---

## V-01: Role Sequence -- CONTEXT Section + Archivist Consolidates

**Axis:** Role sequence -- A CONTEXT section before CLAIMANT: DECLARE generates F-00 with
current-state primed. The Skeptic runs only domain observability (no Pass 2 status-quo
interrogation -- F-00 already exists). The Archivist collects F-00 from CONTEXT and cleared
domain conditions from SKEPTIC into the Final list. Two independent gates: LOCK GATE (after
DECLARE, freezes claim + domain conditions) and SEAL GATE (after ARCHIVIST, freezes Final list).

**Hypothesis:** When F-00 is born before the claim is written (CONTEXT section), the gap
analysis in Confidence is more grounded -- the Claimant writes the "why insufficient"
explanation while status-quo framing is live, not reconstructed from memory. The Skeptic's
cognitive load decreases: one pass (domain observability only) instead of two. The Archivist's
single-purpose role makes C-18 structurally visible: omitting the Archivist section means
omitting a named role at peer heading level.

```
You are running /prove-hypothesis. Fill in this structured template.
Five sections execute in sequence: Context interrogation, Claimant declares, Skeptic
challenges domain conditions, Archivist consolidates, Navigator plans.

LOCK GATE: Scope -- freezes Claim and all domain Falsification Conditions after DECLARE.
SEAL GATE: Scope -- freezes Final Falsification List after CONSOLIDATE.
Post-lock observability problems are recorded as amendment notes only.
Retroactive condition edits are prohibited.

---

## CONTEXT: CURRENT STATE
[Complete this section before writing your claim. Establishes status-quo baseline and
generates F-00 with current practice primed in context.]

Prior signals: [Search simulations/prove/ for any prior hypothesis, analysis, or synthesis
on this topic. List files found with one-line summaries, or write "None -- starting fresh."]

What does the team do today?
Current practice: [One sentence. What does the team currently do without this capability?
Be specific -- this is the practice your claim must exceed.]

Is current practice sufficient to deliver the value the claim will assert?
[ ] INSUFFICIENT: current practice leaves a gap.
    The gap: [One sentence. What specifically cannot be achieved with current practice?]
    F-00 candidate: This hypothesis is false if the team obtains equivalent value from
    current practice without this capability.
    F-00 observable test: [What measurable outcome would indicate that current practice
    is sufficient? Must be an external, verifiable observation -- not an opinion.]
[ ] SUFFICIENT: current practice already satisfies the need. Stop. Do not write a claim
    for a value that status quo already delivers. Revise your framing before restarting.

---

## CLAIMANT: DECLARE
[Write your claim after completing CONTEXT. No evidence references allowed here.
No Skeptic verdicts, no consolidation output, no Navigator content in this section.]

Claim: [One sentence. Use "is" or "will". No hedging. No compound claims.]

Domain falsification candidates (Skeptic will evaluate each for observability):
| ID   | Condition: hypothesis is false if this observable outcome occurs |
|------|------------------------------------------------------------------|
| F-01 | [Observable outcome that would prove the claim false] |
| F-02 | [Observable outcome that would prove the claim false] |
[Add F-03+ if needed. Each must describe an externally verifiable outcome.]

Confirmation conditions:
| ID    | Condition: hypothesis is confirmed if this observable outcome occurs |
|-------|----------------------------------------------------------------------|
| CF-01 | [Positive confirmation criterion] |

### LOCK GATE
Scope: Freezes Claim and all domain Falsification Conditions (F-01+).
Downstream sections have read-only access to DECLARE.
- [ ] CONTEXT: F-00 candidate and observable test are written (INSUFFICIENT path taken)
- [ ] Claim is one sentence with no hedging
- [ ] At least two domain conditions (F-01, F-02) present
- [ ] No Skeptic verdicts, consolidation output, or Navigator content referenced here

LOCKED. Claim and domain conditions above are now read-only.
Post-lock observability problems: log as amendment notes in NAVIGATOR. Do not edit here.

---

## SKEPTIC: CHALLENGE
[Domain observability only. F-00 is established in CONTEXT -- Skeptic validates it below.
Read-only access to DECLARE. Log problems as amendment notes; do not modify locked sections.
Opinion-dependent and invisible-state conditions receive REWRITE verdict.]

### Domain Conditions (F-01+)
| F-ID | Condition text (from DECLARE) | Skeptic verdict | Rewritten condition (if REWRITE) |
|------|-------------------------------|-----------------|----------------------------------|
| F-01 | [text from DECLARE] | PASS (observable: [how measured]) / REWRITE | [Issue + new condition text] |
| F-02 | [text from DECLARE] | PASS (observable: [how measured]) / REWRITE | [Issue + new condition text] |
[All F-IDs from DECLARE must appear. Silent omission is a coverage failure.]

### F-00 Validation
F-00 from CONTEXT: [restate condition and observable test]
Skeptic verdict: [ ] PASS -- observable test is externally verifiable via [method]
                 [ ] REWRITE -- issue: [what is wrong with the observable test].
                     Revised observable test: [new text]

### PRE-CONSOLIDATE CHECK
- [ ] Every domain F-ID from DECLARE has an explicit PASS or REWRITE verdict
- [ ] Every REWRITE has a complete replacement (not left blank)
- [ ] F-00 from CONTEXT has received an explicit Skeptic verdict
- [ ] No modifications made to CLAIMANT: DECLARE

Amendment notes from SKEPTIC: [F-NN: observability issue -- suggested rewrite for next run.
Write "None" if no flagged conditions.]

---

## ARCHIVIST: CONSOLIDATE
[Collect F-00 (from CONTEXT, Skeptic-validated) and all cleared domain conditions
(from SKEPTIC: CHALLENGE) into one enumerated Final Falsification List.
Every condition receives an explicit CONFIRMED verdict.
F-00 goes first (status-quo competitor); domain conditions follow in F-01+ order.
A partial list -- missing any condition from either source -- is a structural failure.
Archivist role: collection and confirmation only. No new conditions introduced here.]

Final falsification list:
| ID   | Condition | Observable test | Verdict |
|------|-----------|-----------------|---------|
| F-00 | Status quo is sufficient | [from CONTEXT, confirmed by Skeptic] | CONFIRMED |
| F-01 | [Cleared from SKEPTIC domain pass] | [how observed] | CONFIRMED |
| F-02 | [Cleared from SKEPTIC domain pass] | [how observed] | CONFIRMED |
[All conditions from CONTEXT and SKEPTIC must appear. No F-ID may be absent.]

### SEAL GATE
Scope: Freezes Final Falsification List. Confidence and Navigator use this list exclusively.
- [ ] F-00 present with CONFIRMED (sourced from CONTEXT, Skeptic-validated)
- [ ] Every domain condition from SKEPTIC present with CONFIRMED
- [ ] No condition from either source absent from the Final list
- [ ] All observable tests populated (no blank cells)

SEALED. The Final Falsification List above is the authoritative source for NAVIGATOR.

---

## CLAIMANT: CONFIDENCE
[Written after LOCK GATE and SEAL GATE. Both are in effect -- do not revise conditions.]

Value: [N]/100
Rationale: [2-3 sentences. Two required elements:
  (1) Why F-00 is INSUFFICIENT -- what specific gap does current practice leave?
      Reference the CONTEXT gap statement.
  (2) What prior signal, trace finding, or friction point anchors the numeric value?
  If no prior signals: "No prior signals -- calibrated from CONTEXT gap: [reasoning]."
  Both elements required; silence on either fails.]

---

## NAVIGATOR: EXPERIMENTS
[LOCK GATE and SEAL GATE are in effect. Source: ARCHIVIST Final Falsification List only.
Rank 1 = highest probability of falsifying the hypothesis.
Valid sub-skills: prove:interview, prove:prototype, prove:analysis, prove:websearch,
prove:publish, prove:synthesize, prove:intelligence.
COVERAGE RULE: Every F-ID in the Final Falsification List must appear in at least one
experiment row. Any F-ID with no experiment row is an explicit failure -- do not write
the artifact until all F-IDs are covered.]

| Rank | Experiment | prove sub-skill | F-IDs tested | Why this risk rank |
|------|-----------|-----------------|--------------|-------------------|
| 1 | [Describe experiment] | prove:[sub-skill] | [F-00, F-01] | [Why highest falsification risk] |
| 2 | [Describe experiment] | prove:[sub-skill] | [F-01, F-02] | [Why second risk] |
[Add rows until every F-ID from the Final Falsification List is covered.]

Amendment notes (post-lock): [F-NN: issue -- suggested rewrite for next hypothesis run.
Write "None" if no post-lock problems discovered.]

---

Write artifact: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
Frontmatter: skill, topic, date, claim_summary, confidence, experiment_count,
             prior_signals_found (true/false), status_quo_verdict (INSUFFICIENT/SUFFICIENT),
             skeptic_rewrites (count of REWRITE verdicts), amendment_notes (count),
             f_id_count (total in Final list), f_id_coverage (all covered: true/false).
```

---

## V-02: Output Format -- Prose-Only + Named COLLECTOR Section

**Axis:** Output format -- All structure expressed in prose and numbered lists. No tables
except the Final falsification list (where row structure is load-bearing for C-09/C-14). The
three new criteria satisfied without tables: OPENING section before DECLARE generates F-00
(C-19); COLLECTOR: CONSOLIDATE section at ## heading level (C-18); two named gates in prose
(C-17). Tests whether format-neutrality extends to the full 11-aspirational rubric.

**Hypothesis:** The v4 structural guarantees (C-17 dual gates, C-18 named consolidation unit,
C-19 inertia-lead framing) are achievable with prose. The COLLECTOR section at ## level
makes C-18 visible in prose format: omitting the section is a missing heading, not a missing
table row. DECLARE GATE and COLLECTOR GATE as named prose gates each carry their own
checklists, satisfying C-17's non-overlapping scope requirement.

```
You are running /prove-hypothesis. Fill in this structured template.
Format: prose and numbered lists throughout. Final list uses table format only.
Six named sections execute in order: Opening, Declare, Challenge, Collector, Confidence, Navigate.

DECLARE GATE: Scope -- freezes Claim and all Falsification Conditions before any Skeptic pass.
COLLECTOR GATE: Scope -- freezes Final Falsification List after consolidation, before
Confidence and Navigate are populated.
Post-lock problems are recorded as amendment notes only. No retroactive edits.

---

## OPENING: CURRENT STATE
[Complete this section before writing your claim. This is the status-quo interrogation.
F-00 is generated here, not during the Skeptic pass.]

1. Prior signals: [Search simulations/prove/ for any prior hypothesis, analysis, or synthesis
on this topic. List file names and one-line summaries, or write "None -- starting fresh."]

2. Current practice: [One sentence. What does the team currently do without this capability?]

3. Status-quo judgment -- give an explicit verdict (silence fails):
   [ ] INSUFFICIENT: current practice leaves a gap.
       The gap: [One sentence. What specifically cannot be achieved today?]
       F-00: This hypothesis is false if the team obtains equivalent value from current practice.
       How to observe F-00: [What measurable outcome would indicate current practice is sufficient?]
   [ ] SUFFICIENT: current practice already satisfies the need. Stop. Revise framing before continuing.

---

## DECLARE: HYPOTHESIS
[Write your claim after completing OPENING. No evidence references here.
No Skeptic verdicts, no collector output, no Navigator content in this section.]

Claim: [One sentence. Use "is" or "will". No hedging. This is your commitment.]

What would prove you wrong:
1. F-01: [Observable outcome that would prove the claim false]
2. F-02: [Observable outcome that would prove the claim false]
[Add more. Each must name something externally observable or measurable.]

What would confirm you right:
1. CF-01: [Positive confirmation criterion]

### DECLARE GATE
Scope: Freezes Claim and all Falsification Conditions (F-01+). Challenge pass has read-only access.
- [ ] OPENING: Status-quo judgment written (INSUFFICIENT or SUFFICIENT -- not absent)
- [ ] OPENING: F-00 and observable test written (required if INSUFFICIENT)
- [ ] Claim is one sentence with no hedging
- [ ] At least two domain conditions (F-01+) present
- [ ] No Skeptic verdicts, Collector output, or Navigator content referenced here

LOCKED. Claim and conditions above are now read-only.
Post-lock problems discovered during Challenge or later: log as amendment notes in Navigate.

---

## CHALLENGE: SKEPTIC
[For each domain condition from DECLARE, write an explicit observability annotation.
Format when passing:
  "F-NN [condition text]: PASS -- observable via [how you would observe or measure this]"
Format when rewriting:
  "F-NN [condition text]: REWRITE -- [what is wrong]. Revised: [new condition text]"
All conditions must reach PASS before the Collector proceeds. None may be silently omitted.]

F-01 [condition text]: [PASS -- observable via ... / REWRITE -- problem. Revised: ...]
F-02 [condition text]: [PASS -- observable via ... / REWRITE -- problem. Revised: ...]
[Continue for every condition from DECLARE. Every F-ID must appear.]

F-00 validation (from OPENING): [PASS -- observable test is measurable via [method] /
REWRITE -- problem: [what is wrong]. Revised observable test: [new text]]

### PRE-COLLECTOR CHECK
- [ ] Every F-ID from DECLARE has an explicit PASS annotation
- [ ] Every REWRITE has a complete written replacement (not left blank)
- [ ] F-00 from OPENING has received an explicit verdict
- [ ] No modifications made to DECLARE section

Amendment notes from Challenge: [F-NN: issue -- suggested rewrite for next run.
Write "None" if no flagged conditions.]

---

## COLLECTOR: CONSOLIDATE
[Gather all cleared conditions from OPENING (F-00) and CHALLENGE (F-01+) into one
Final Falsification List. Every condition receives an explicit CONFIRMED verdict.
F-00 goes first (status-quo competitor); domain conditions follow in F-01+ order.
Missing any condition from either source is a structural failure. Collector does not
introduce new conditions -- collection and confirmation only.]

Final falsification list:
| ID   | Condition | Observable test | Verdict |
|------|-----------|-----------------|---------|
| F-00 | Status quo is sufficient | [from OPENING, confirmed by Skeptic] | CONFIRMED |
| F-01 | [Cleared domain condition] | [from CHALLENGE annotation] | CONFIRMED |
| F-02 | [Cleared domain condition] | [from CHALLENGE annotation] | CONFIRMED |
[All conditions from OPENING and CHALLENGE must appear. No F-ID may be absent.]

### COLLECTOR GATE
Scope: Freezes Final Falsification List. Confidence and Navigate use this list exclusively.
- [ ] F-00 present with CONFIRMED (from OPENING, Skeptic-validated)
- [ ] Every domain condition from CHALLENGE present with CONFIRMED
- [ ] No condition from either source absent
- [ ] All observable tests populated (no blank entries)

SEALED. The Final Falsification List above is the authoritative source for Navigate.

---

## CONFIDENCE: ASSESSMENT
[Written after DECLARE GATE and COLLECTOR GATE. Both are in effect -- do not revise conditions.]

Confidence: [N]/100

Rationale: [2-3 sentences. Two required elements:
  (1) Why F-00 is INSUFFICIENT -- what specific gap does current practice leave?
      Reference the OPENING gap statement.
  (2) At least one prior signal, trace finding, or friction point anchoring the number.
  If no prior signals: "No prior signals -- calibrated from OPENING gap: [reasoning]."
  Both elements required; silence on either fails.]

---

## NAVIGATE: EXPERIMENTS
[Order from most likely to falsify (rank 1) to least. Source: COLLECTOR Final list only.
Valid sub-skills: prove:interview, prove:prototype, prove:analysis, prove:websearch,
prove:publish, prove:synthesize, prove:intelligence.

COVERAGE RULE: Before writing the artifact, verify every F-ID from the COLLECTOR Final
list appears under at least one experiment. Any F-ID with no experiment is an explicit
failure -- add an experiment before writing the artifact.]

1. [Describe experiment]
   Sub-skill: prove:[sub-skill]
   F-IDs tested: [F-00, F-01, ...]
   Risk rationale: [Why is this ranked 1? What would this experiment falsify first?]

2. [Describe experiment]
   Sub-skill: prove:[sub-skill]
   F-IDs tested: [F-01, F-02, ...]
   Risk rationale: [Why is this ranked 2?]

[Add experiments until every F-ID in the COLLECTOR Final list is covered.]

Amendment notes: [F-NN: issue discovered post-lock -- suggested rewrite for next run.
Write "None" if no post-lock problems discovered.]

---

Write artifact: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
Frontmatter: skill, topic, date, claim_summary, confidence, experiment_count,
             prior_signals_found (true/false), status_quo_verdict (INSUFFICIENT/SUFFICIENT),
             skeptic_rewrites (count of REWRITE annotations), amendment_notes (count),
             f_id_count (total in Final list), f_id_coverage (all covered: true/false).
```

---

## V-03: Lifecycle Emphasis -- 7 Phases with INERTIA Before DECLARE

**Axis:** Lifecycle emphasis -- Seven phases: PRIOR / INERTIA / DECLARE / CHALLENGE /
CONSOLIDATE / CONFIDENCE / NAVIGATE. The INERTIA phase is a dedicated named phase that
runs before DECLARE, making status-quo interrogation and F-00 generation structurally
impossible to skip (omitting INERTIA is a missing phase). CONSOLIDATE is a named phase
(C-18). Two independent gates: GATE 3 (DECLARE LOCK, freezes claim + domain conditions)
and GATE 5 (CONSOLIDATE SEAL, freezes Final list) with non-overlapping scopes (C-17).

**Hypothesis:** Making status-quo interrogation a named phase peer (not a subsection of
DECLARE or CHALLENGE) is the strongest structural guarantee for C-19: the model cannot
write a claim before completing a phase whose only job is establishing current practice and
generating F-00. Combined with CONSOLIDATE as its own phase and two explicit gate events,
all three v4 criteria are structurally unskippable by phase sequence alone.

```
You are running /prove-hypothesis.
Seven phases execute in strict sequence. Each gate must complete before the next phase begins.
GATE 3 (DECLARE LOCK) freezes Claim and domain Falsification Conditions.
GATE 5 (CONSOLIDATE SEAL) freezes the Final Falsification List.
Phases 4-7 have read-only access to PHASE 3. PHASES 6-7 source only from the PHASE 5 Final list.

---

## PHASE 1: PRIOR
Goal: Establish signal context before any framing begins.

Prior signals: [Search simulations/prove/ for any prior hypothesis, analysis, or synthesis
on this topic. List files found with one-line summaries. Write "None -- starting fresh" if empty.]

GATE 1 -- required before PHASE 2:
- [ ] Prior signal state declared (files listed, or explicit "None" -- silence fails)

---

## PHASE 2: INERTIA
Goal: Interrogate the status quo before the claim is declared. F-00 is born here.
This phase must complete before any claim is written.

What does the team do today?
Current practice: [One sentence. What does the team currently do without this capability?
Be concrete -- this is the baseline the claim must exceed.]

Status-quo judgment (explicit verdict required -- silence fails):
[ ] INSUFFICIENT: current practice leaves a gap.
    The gap: [One sentence. What specifically cannot be achieved with current practice?]
    F-00 candidate: This hypothesis is false if the team obtains equivalent value from
    current practice without this capability.
    F-00 observable test: [What measurable outcome would indicate status-quo sufficiency?
    Must be an externally verifiable observation.]
[ ] SUFFICIENT: current practice already delivers the claimed value. Stop. Do not proceed
    to PHASE 3. Revise the claim framing and restart PHASE 2.

GATE 2 -- required before PHASE 3:
- [ ] Current practice written (one concrete sentence -- no vague placeholders)
- [ ] Status-quo judgment written (INSUFFICIENT or SUFFICIENT -- silence fails)
- [ ] If INSUFFICIENT: F-00 candidate written with observable test

---

## PHASE 3: DECLARE
Goal: Write the hypothesis. No evidence references here. PHASE 2 established the baseline;
this phase declares the claim. PHASE 3 output is LOCKED after GATE 3.

Claim: [One sentence. Use "is" or "will". No hedging.]

Domain falsification candidates (PHASE 4 Skeptic will evaluate observability):
| ID   | Condition: hypothesis is false if this observable outcome occurs |
|------|------------------------------------------------------------------|
| F-01 | [Observable outcome that would prove the claim false] |
| F-02 | [Observable outcome that would prove the claim false] |
[Add F-03+ if needed. Each must describe an externally verifiable outcome.]

Confirmation conditions:
| ID    | Condition: hypothesis is confirmed if this observable outcome occurs |
|-------|----------------------------------------------------------------------|
| CF-01 | [Positive confirmation criterion] |

GATE 3: DECLARE LOCK
Scope: Freezes Claim and all domain Falsification Conditions (F-01+). PHASES 4-7 are read-only.
- [ ] Claim is one sentence with no hedging
- [ ] At least two domain conditions (F-01, F-02) present
- [ ] No Skeptic verdicts, PHASE 5 content, or Navigator content referenced here
- [ ] F-00 is NOT listed here -- it comes from PHASE 2 and will be merged in PHASE 5

LOCKED. PHASES 4-7 may not modify Claim or domain Conditions.
Post-lock problems: log as amendment notes in PHASE 7. Do not edit here.

---

## PHASE 4: CHALLENGE
Goal: Skeptic evaluates observability of domain conditions and validates F-00 from PHASE 2.
Read-only access to PHASE 3. F-00 was generated in PHASE 2 -- Skeptic validates, not introduces.

### 4A: Domain Observability
[Each F-ID from PHASE 3 must receive an explicit verdict.
Opinion-dependent and invisible-state conditions receive REWRITE.]

| F-ID | Condition text (from PHASE 3) | Skeptic verdict | Rewritten condition (if REWRITE) |
|------|-------------------------------|-----------------|----------------------------------|
| F-01 | [from PHASE 3] | PASS (observable: [how measured]) / REWRITE | [Issue + new text] |
| F-02 | [from PHASE 3] | PASS (observable: [how measured]) / REWRITE | [Issue + new text] |
[All F-IDs from PHASE 3 must appear. Silent omission is a coverage failure.]

### 4B: F-00 Validation
F-00 from PHASE 2: [restate the F-00 candidate text and observable test]
Skeptic verdict: [ ] PASS -- observable test is externally verifiable via [method]
                 [ ] REWRITE -- issue: [what is wrong]. Revised observable test: [new text]

GATE 4 -- required before PHASE 5:
- [ ] Every F-ID from PHASE 3 has received an explicit PASS or REWRITE verdict
- [ ] Every REWRITE has a complete replacement (not left blank)
- [ ] F-00 from PHASE 2 has received an explicit Skeptic verdict (4B)
- [ ] No modifications made to PHASE 3

Amendment notes from PHASE 4: [F-NN: issue -- suggested rewrite for next run.
Write "None" if no flagged conditions.]

---

## PHASE 5: CONSOLIDATE
Goal: Merge all Skeptic-cleared conditions into one Final Falsification List before
Confidence and Navigator. F-00 (from PHASE 2, validated in PHASE 4B) and all cleared
domain conditions (from PHASE 4A) receive explicit CONFIRMED verdicts. This is the
only source Navigator may reference.

[Collect F-00 from PHASE 2 (Skeptic verdict from PHASE 4B) and all cleared conditions
from PHASE 4A. F-00 goes first; domain conditions follow in F-01+ order.
A partial list -- missing any F-ID from either source -- is a structural failure.]

Final falsification list:
| ID   | Condition | Observable test | Verdict |
|------|-----------|-----------------|---------|
| F-00 | Status quo is sufficient | [from PHASE 2, validated in PHASE 4B] | CONFIRMED |
| F-01 | [Cleared from PHASE 4A] | [how observed] | CONFIRMED |
| F-02 | [Cleared from PHASE 4A] | [how observed] | CONFIRMED |
[Add rows until every condition from PHASE 2 and PHASE 4 is present.]

GATE 5: CONSOLIDATE SEAL
Scope: Freezes Final Falsification List. PHASES 6-7 source only from this list.
- [ ] F-00 present with CONFIRMED (from PHASE 2, validated by PHASE 4B)
- [ ] Every domain condition from PHASE 4A present with CONFIRMED
- [ ] No F-ID from either source absent from the Final list
- [ ] All observable tests populated (no blank cells)

SEALED. The Final Falsification List above is the authoritative source for PHASES 6-7.

---

## PHASE 6: CONFIDENCE
Goal: Record confidence after GATE 3 (DECLARE LOCK) and GATE 5 (CONSOLIDATE SEAL) are confirmed.
[Both gates are in effect. Do not revise Claim or Conditions here.]

Value: [N]/100
Rationale: [2-3 sentences. Two required elements:
  (1) Why F-00 is INSUFFICIENT -- what specific gap does current practice leave?
      Reference the PHASE 2 current-practice baseline and gap statement.
  (2) At least one prior signal, trace finding, or friction point anchoring the number.
  If no prior signals: "No prior signals -- calibrated from PHASE 2 gap: [reasoning]."
  Both elements required; silence on either fails.]

---

## PHASE 7: NAVIGATE
Goal: Assign prove sub-skills, ordered by falsification risk. Source: PHASE 5 Final list only.

[Rank 1 = highest probability of falsifying the hypothesis. Name a prove sub-skill for each.
Valid sub-skills: prove:interview, prove:prototype, prove:analysis, prove:websearch,
prove:publish, prove:synthesize, prove:intelligence.
COVERAGE RULE: Every F-ID in the PHASE 5 Final list must appear in at least one
experiment row. Any F-ID with no experiment row is an explicit failure -- do not write
the artifact until all F-IDs are covered.]

| Rank | Experiment | prove sub-skill | F-IDs tested | Risk rationale |
|------|-----------|-----------------|--------------|----------------|
| 1 | [Describe experiment] | prove:[sub-skill] | [F-00, F-01] | [Why highest falsification risk] |
| 2 | [Describe experiment] | prove:[sub-skill] | [F-01, F-02] | [Why second risk] |
[Add rows until all F-IDs from the PHASE 5 Final list are covered.]

---

Write artifact: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
Frontmatter: skill, topic, date, claim_summary, confidence, experiment_count,
             prior_signals_found (true/false), status_quo_verdict (INSUFFICIENT/SUFFICIENT),
             skeptic_rewrites (count of REWRITE verdicts in 4A), amendment_notes (count),
             f_id_count (total F-IDs in Final list), f_id_coverage (all covered: true/false).
```

---

## V-04: Phrasing Register -- Formal/Technical with Explicit Gate Scope Declarations

**Axis:** Phrasing register -- Most formal, technical language. Each gate explicitly declares
its scope ("freezes X before Y") and the artifacts it covers. Every constraint is stated as
a rule, not an instruction. Named roles: Claimant / Skeptic / Archivist / Navigator. The
CONTEXT section before DECLARE generates F-00 before the Claim is declared (C-19). The
ARCHIVIST role is at ## heading level (C-18). Two gates with non-overlapping scope
declarations form the strongest C-17 evidence across the five variations.

**Hypothesis:** Explicit scope declarations on each gate ("DECLARE GATE (LOCK): freezes
Claim and all Falsification Conditions" / "CONSOLIDATE GATE (SEAL): freezes Final
Falsification List") make C-17's dual-gate requirement self-documenting. A reviewer reading
the template can confirm non-overlapping scopes from the gate header text alone, without
inspecting checklist contents. The formal register makes this declaration more precise than
conversational alternatives.

```
You are running /prove-hypothesis.
Four roles execute in strict sequence. Gate compliance is mandatory before advancing.

DECLARE GATE (LOCK): Scope -- freezes Claim and all Falsification Conditions before any
adversarial review pass begins. No downstream section may modify Claim or Conditions.
Post-lock modifications are prohibited. Post-lock observability failures are recorded
as amendment notes only.

CONSOLIDATE GATE (SEAL): Scope -- freezes Final Falsification List after multi-pass
consolidation and before Confidence and Navigator are populated. Navigator sources
exclusively from the Final Falsification List produced by this gate.

---

## CLAIMANT: CONTEXT
[Execute before DECLARE. Establish current-state facts. F-00 is generated here.]

Prior Signals:
Search simulations/prove/ for prior hypothesis, analysis, or synthesis on this topic.
Document: [list files with one-line summaries, or "None -- starting fresh"]

Current Practice:
[One sentence. What does the team do today without this capability?
Be specific -- this is the baseline practice the claim must exceed.]

Status-Quo Assessment:
Does current practice already deliver the value the claim will assert?
- Assessment: [ ] INSUFFICIENT -- current practice cannot deliver the claimed value
               [ ] SUFFICIENT -- current practice already satisfies the need [STOP and revise]

If INSUFFICIENT:
  Gap: [One sentence. What specifically does current practice fail to deliver?]
  F-00 Candidate: The hypothesis is false if the team obtains equivalent value from
  current practice ([Current Practice]) without this capability.
  F-00 Observable Test: [Measurable outcome that would indicate current practice is sufficient.
  Must be externally verifiable -- not an internal state or qualitative judgment.]

---

## CLAIMANT: DECLARE
[Execute after CONTEXT. Declare Claim before any adversarial review begins.
No Skeptic findings, Archivist output, or Navigator content permitted here.]

Claim: [One declarative sentence. Predicate form: "X is Y" or "X will Z". No hedging.]

Domain Falsification Conditions (candidates -- Skeptic will evaluate observability):
| ID   | Condition: The hypothesis is false if this observable outcome occurs |
|------|----------------------------------------------------------------------|
| F-01 | [Observable outcome] |
| F-02 | [Observable outcome] |
[Add F-03+ as needed. Each condition must describe an externally verifiable outcome.]

Confirmation Conditions:
| ID    | Condition: The hypothesis is confirmed if this observable outcome occurs |
|-------|--------------------------------------------------------------------------|
| CF-01 | [Positive confirmation criterion] |

### DECLARE GATE (LOCK)
Scope: Freezes Claim + all domain Falsification Conditions (F-01+).
Adversarial review begins after this gate. All downstream sections are read-only.
Criteria:
- [ ] CONTEXT: Status-Quo Assessment written (INSUFFICIENT or SUFFICIENT -- not absent)
- [ ] CONTEXT: F-00 Candidate and Observable Test written (required if INSUFFICIENT)
- [ ] Claim is a single declarative sentence with no hedging
- [ ] Minimum two Falsification Conditions (F-01, F-02) present
- [ ] No Skeptic verdicts, Archivist output, or Navigator content present in DECLARE

LOCKED. Claim and Falsification Conditions above are frozen.
Modifications prohibited in all downstream sections.
Post-lock observability failures: record as amendment notes in NAVIGATOR. Do not edit here.

---

## SKEPTIC: CHALLENGE
[Read-only access to DECLARE. Evaluate observability of each condition.
Scope: F-00 from CONTEXT + all domain conditions from DECLARE.
Opinion-dependent and invisible-state conditions receive REWRITE verdict.]

### Domain Observability (F-01+)
| F-ID | Condition Text (from DECLARE) | Verdict | Notes or Rewritten Condition |
|------|-------------------------------|---------|-------------------------------|
| F-01 | [from DECLARE] | PASS (observable: [measurement method]) / REWRITE | [If REWRITE: issue + new text] |
| F-02 | [from DECLARE] | PASS (observable: [measurement method]) / REWRITE | [If REWRITE: issue + new text] |
[All F-IDs from DECLARE must appear. Silent omission is a coverage failure.]

### F-00 Observability
F-00 (from CONTEXT): [restate condition text and observable test]
Verdict: [ ] PASS -- Observable Test is measurable via [confirmed method]
         [ ] REWRITE -- Issue: [what is wrong]. Revised Observable Test: [new text]

### PRE-CONSOLIDATE GATE
- [ ] Every domain F-ID from DECLARE has an explicit PASS or REWRITE verdict
- [ ] Every REWRITE has a complete replacement condition
- [ ] F-00 from CONTEXT has received an explicit Skeptic verdict
- [ ] No modifications made to CLAIMANT: DECLARE

Amendment notes from CHALLENGE: [F-NN: issue -- suggested rewrite for next run.
Write "None" if no flagged conditions.]

---

## ARCHIVIST: CONSOLIDATE
[Collect all Skeptic-validated conditions from CONTEXT (F-00) and CHALLENGE (F-01+) into
one enumerated Final Falsification List. Assign CONFIRMED verdict to each condition.
F-00 listed first (status-quo competitor); cleared domain conditions follow (F-01+).
A partial list -- omitting any condition from either source -- is a structural failure.
Archivist responsibility: collection and verification only. No new conditions introduced here.]

Final Falsification List:
| ID   | Condition | Observable Test | Verdict |
|------|-----------|-----------------|---------|
| F-00 | Status quo is sufficient | [from CONTEXT, validated by Skeptic] | CONFIRMED |
| F-01 | [Cleared domain condition] | [measurement method from CHALLENGE] | CONFIRMED |
| F-02 | [Cleared domain condition] | [measurement method from CHALLENGE] | CONFIRMED |
[All conditions from CONTEXT and CHALLENGE must appear. No F-ID absent.]

### CONSOLIDATE GATE (SEAL)
Scope: Freezes Final Falsification List. Confidence and Navigator source only from this list.
Criteria:
- [ ] F-00 present with CONFIRMED verdict (sourced from CONTEXT, validated by Skeptic)
- [ ] Every domain condition from CHALLENGE present with CONFIRMED verdict
- [ ] No condition from either source absent from the Final list
- [ ] All Observable Tests populated (no empty cells)

SEALED. Final Falsification List above is frozen.
Confidence and Navigator use this list exclusively.

---

## CLAIMANT: CONFIDENCE
[Written after DECLARE GATE (LOCK) and CONSOLIDATE GATE (SEAL) are both confirmed.
Both gates are in effect. Claim and Final Falsification List may not be modified here.]

Confidence Value: [N]/100

Rationale: [2-3 sentences. Two mandatory elements:
  (1) Explain why F-00 is INSUFFICIENT: what specific capability gap does current practice
      leave that the claim addresses? Reference the CONTEXT Gap statement.
  (2) Cite the prior signal, trace finding, or named friction point anchoring the numeric
      value. If no prior signals exist: "No prior signals. Calibrated from CONTEXT gap:
      [explicit reasoning for the chosen value]."
  Both elements are mandatory; omitting either element fails this section.]

---

## NAVIGATOR: EXPERIMENTS
[DECLARE GATE (LOCK) and CONSOLIDATE GATE (SEAL) are in effect.
Source: ARCHIVIST Final Falsification List exclusively.
Ordering: rank 1 = highest falsification probability (most likely to disprove the Claim).
Valid prove sub-skills: prove:interview, prove:prototype, prove:analysis, prove:websearch,
prove:publish, prove:synthesize, prove:intelligence.
COVERAGE RULE: Every F-ID in the Final Falsification List must appear in at least one
Experiment row. Any F-ID with zero experiment coverage is an explicit failure -- add an
experiment before writing the artifact.]

| Rank | Experiment Description | Prove Sub-Skill | F-IDs Tested | Falsification Risk Rationale |
|------|------------------------|-----------------|--------------|------------------------------|
| 1 | [Experiment description] | prove:[sub-skill] | [F-00, F-01] | [Why highest falsification probability] |
| 2 | [Experiment description] | prove:[sub-skill] | [F-01, F-02] | [Why ranked second] |
[Add rows until all F-IDs from the Final Falsification List are covered.]

Amendment Notes (post-lock):
[F-NN: observability issue discovered post-lock -- suggested rewrite for next hypothesis.
Write "None" if no post-lock issues encountered.]

---

Write artifact: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
Frontmatter: skill, topic, date, claim_summary, confidence, experiment_count,
             prior_signals_found (true/false), status_quo_verdict (INSUFFICIENT/SUFFICIENT),
             skeptic_rewrites (count of REWRITE verdicts), amendment_notes (count),
             f_id_count (total F-IDs in Final list), f_id_coverage (all covered: true/false).
```

---

## V-05: Combined -- Conversational Register + Inertia-Lead + Named COLLECTOR

**Axes:** Phrasing register (second-person, plain language, numbered steps) + inertia-lead
framing (Steps 1-2 interrogate current practice before Step 3 declares the claim) + named
COLLECTOR step at ## heading level (C-18). Two explicit freeze moments in plain language:
LOCKED after Step 3 (claim + domain conditions), SEALED after Step 4 COLLECTOR (Final list),
each with its own checklist (C-17).

**Hypothesis:** Conversational register with all three v4 criteria satisfied tests whether
plain-language freeze instructions ("LOCKED. Your claim and domain conditions are frozen.")
and a colloquially named step ("COLLECTOR") carry the same structural guarantees as formal
role-name variations. C-19 is satisfied by the step sequence itself: Steps 1-2 are the
status-quo interrogation; the claim appears in Step 3. The COLLECTOR step header at the
same ## level as other steps makes C-18 visible in the numbered format.

```
You are running /prove-hypothesis.
Answer each question in order. You cannot skip a step or go back.
There are two freeze moments:
  - After Step 3: your claim and domain conditions are frozen (LOCKED)
  - After Step 4: your Final list is frozen (SEALED)
After the second freeze, your experiments can only reference the Final list from Step 4.

---

## Step 1: What exists before this?

Prior signals: [Search simulations/prove/ for any prior hypothesis, analysis, or synthesis
on this topic. List file names and one-line summaries. If nothing exists, write "None found."]

---

## Step 2: What does the team do today?

Current practice: [One sentence. What does the team currently do without this capability?
Be concrete -- you will be asked whether this is already good enough.]

Is current practice sufficient to deliver the value you are about to claim?
Give an explicit verdict -- silence is a failure.

[ ] Not good enough (INSUFFICIENT): there is a real gap.
    The gap: [One sentence. What exactly can the team not achieve with current practice?]
    F-00: This hypothesis is false if the team gets equivalent value from current practice.
    How you would know F-00 is true: [What measurable outcome would show that current
    practice is actually sufficient? Must be something you could observe or measure externally.]

[ ] Already good enough (SUFFICIENT): the status quo covers the need.
    If SUFFICIENT: Stop here. Rethink your claim framing before continuing.

---

## Step 3: What do you believe?

[Write your claim here, after answering Steps 1-2, before examining any domain evidence.
This is the commitment you cannot revise after seeing results.]

Claim: [One sentence. Use "is" or "will". No "might", no hedging, no compound claims.]

What would prove you wrong (domain conditions):
1. F-01: [Observable outcome that would prove the claim false]
2. F-02: [Observable outcome that would prove the claim false]
[Add more if needed. Each must be something observable or measurable -- not a feeling.]

What would confirm you right:
1. CF-01: [Positive confirmation criterion]

A Skeptic reviews each domain condition for observability:
F-01 [condition text]: [PASS -- observable via [how you would observe this] /
                        REWRITE -- problem: [what is wrong]. Revised: [new condition text]]
F-02 [condition text]: [PASS -- observable via [how you would observe this] /
                        REWRITE -- problem: [what is wrong]. Revised: [new condition text]]
[Review every condition. None may be skipped.]

First freeze -- confirm before continuing:
- [ ] Step 2: Status-quo verdict written (INSUFFICIENT or SUFFICIENT -- not absent)
- [ ] Step 2: F-00 and observable test written (required if INSUFFICIENT)
- [ ] Step 3: Every domain condition has an explicit PASS annotation
- [ ] Every REWRITE has a written replacement (no silent removal)
- [ ] Claim is one sentence with no hedging
- [ ] Nothing from Steps 4-6 has leaked into Step 3

LOCKED. Your claim and domain conditions above are frozen from this point.
Post-lock observability problems: log as amendment notes in Step 6, not edits here.

---

## Step 4: COLLECTOR -- Assemble the Final list

[This is the consolidation step. Bring together F-00 from Step 2 and all cleared domain
conditions from Step 3 into one Final list. Every condition gets an explicit CONFIRMED verdict.
F-00 goes first; domain conditions follow in F-01+ order. This Final list -- not the
conditions listed above -- is what your experiments will reference.
Missing any condition from Step 2 or Step 3 is a failure.]

Final list:
| # | Condition | How you would observe it | Verdict |
|---|-----------|--------------------------|---------|
| F-00 | Status quo is sufficient | [from Step 2 observable test] | CONFIRMED |
| F-01 | [Cleared from Step 3] | [from Step 3 PASS annotation] | CONFIRMED |
| F-02 | [Cleared from Step 3] | [from Step 3 PASS annotation] | CONFIRMED |
[Add a row for every condition from Steps 2 and 3. No condition may be absent.]

Second freeze -- confirm before Step 5:
- [ ] F-00 present with CONFIRMED (from Step 2)
- [ ] Every domain condition from Step 3 present with CONFIRMED
- [ ] No condition from either step is absent
- [ ] All observation methods filled in (no blank cells)

SEALED. The Final list above is frozen. Your experiments reference only this list.

---

## Step 5: How confident are you?

[Write your confidence after both freezes are in effect. Do not revise any conditions here.]

Confidence: [N]/100

Why: [2-3 sentences. Two required elements:
  (1) Why the gap from Step 2 is real -- what exactly can current practice not deliver?
      Cross-reference your Step 2 gap statement.
  (2) Something from your prior work (signal files, trace findings, known friction) that
      anchors the number. If you have no prior work: "No prior signals. Calibrated from
      the Step 2 gap: [your reasoning]."
  Both elements required; silence on either fails.]

---

## Step 6: Plan the experiments

[Order your experiments from most likely to falsify your hypothesis (rank 1) to least.
Use F-IDs from the Step 4 Final list only -- do not reference conditions from Steps 2-3 directly.
Valid sub-skills: prove:interview, prove:prototype, prove:analysis, prove:websearch,
prove:publish, prove:synthesize, prove:intelligence.

COVERAGE CHECK: Before writing the artifact, verify every F-ID from the Step 4 Final list
appears under at least one experiment. An F-ID with no experiment is an uncovered blind spot --
add an experiment before completing the artifact.]

| Rank | What you will do | prove sub-skill | F-IDs it tests | Why this rank |
|------|-----------------|-----------------|----------------|---------------|
| 1 | [Describe experiment] | prove:[sub-skill] | [F-00, F-01] | [Why most likely to falsify?] |
| 2 | [Describe experiment] | prove:[sub-skill] | [F-01, F-02] | [Why second?] |
[Add rows until every F-ID from the Step 4 Final list is covered.]

Amendment notes: [F-NN: problem found after first freeze -- suggested rewrite for next run.
Write "None" if no post-freeze problems discovered.]

---

Write artifact: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
Frontmatter: skill, topic, date, claim_summary, confidence, experiment_count,
             prior_signals_found (true/false), status_quo_verdict (INSUFFICIENT/SUFFICIENT),
             skeptic_rewrites (count of REWRITE annotations in Step 3), amendment_notes (count),
             f_id_count (total in Final list), f_id_coverage (all covered: true/false).
```

---

## R4 Design Notes

### Three criteria coverage by variation

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-17: Dual-gate phase isolation | LOCK GATE (claim) + SEAL GATE (Final list) -- separate checklists, non-overlapping scopes | DECLARE GATE + COLLECTOR GATE -- separate checklists, scopes named in header | GATE 3 (DECLARE LOCK, scope stated) + GATE 5 (CONSOLIDATE SEAL, scope stated) | DECLARE GATE (LOCK) + CONSOLIDATE GATE (SEAL) -- explicit scope declarations in gate headers | First freeze (claim + domain conditions) + second freeze (Final list) -- separate checklists |
| C-18: Named consolidation unit | ARCHIVIST: CONSOLIDATE at ## level | COLLECTOR: CONSOLIDATE at ## level | PHASE 5: CONSOLIDATE at ## phase level | ARCHIVIST: CONSOLIDATE at ## level | Step 4: COLLECTOR at ## level, named role |
| C-19: Inertia-lead framing | CONTEXT section before DECLARE; "What does the team do today?"; F-00 born in CONTEXT | OPENING: CURRENT STATE before DECLARE; status-quo judgment + F-00 generated in OPENING | PHASE 2: INERTIA before PHASE 3: DECLARE; F-00 born in INERTIA phase | CLAIMANT: CONTEXT before CLAIMANT: DECLARE; F-00 born in CONTEXT | Steps 1-2 before Step 3; Step 2 asks "What does the team do today?" + generates F-00 |

### What changed from R3

R3 V-01/V-02/V-05 had a single LOCK gate covering both freeze events and consolidation
embedded as a subsection. These fail C-17 (single gate, overlapping scope) and C-18
(subsection omission is silent). R3 V-03/V-04 already had dual gates and named consolidation
units -- they would pass C-17 and C-18 under v4. None of the R3 variations satisfied C-19:
F-00 was generated during the Skeptic pass (or in a baseline field within DECLARE), not in
a status-quo interrogation section that precedes the claim.

R4 makes three structural moves across all five variations:
1. **Separate the freeze events**: LOCK after DECLARE (claim + conditions) and SEAL after
   CONSOLIDATE (Final list) are distinct gates with explicit, non-overlapping scope text.
2. **Name the consolidation unit at peer heading level**: ARCHIVIST (V-01/V-04), COLLECTOR
   (V-02/V-05), or PHASE 5: CONSOLIDATE (V-03) at the same ## heading level as other roles
   or phases. Omitting the named section is a visible structural failure, not a silent skip.
3. **Generate F-00 before the claim**: A dedicated section (CONTEXT, OPENING, INERTIA, or
   numbered Steps 1-2) runs before DECLARE and produces F-00 with current practice already
   established in context. The Skeptic validates F-00 but does not introduce it.

### Open R5 questions

1. Does generating F-00 before the claim (V-01/V-02/V-03/V-04/V-05 all do this now) produce
   richer gap rationale in CONFIDENCE than retrospective F-00 generation during the Skeptic
   pass (R3 V-01/V-02/V-03/V-04)? Degenerate runs would show this in the gap-explanation
   quality of the Confidence section.

2. V-05's plain-language "COLLECTOR" step header: does it hold as well as the formal
   "ARCHIVIST: CONSOLIDATE" naming under context pressure? A model compressing or skipping
   steps under long-prompt conditions would show different failure modes between V-05 (missing
   a numbered step) and V-01/V-04 (missing a named role).

3. V-03's INERTIA phase as a mandatory gate-blocked step: does forcing the model to complete
   GATE 2 (current practice written, status-quo judgment written, F-00 candidate written)
   before DECLARE reduce C-19 degenerate failures more than the CONTEXT sections in V-01/V-04,
   which don't have their own named gate?

4. V-04's explicit gate scope declarations ("DECLARE GATE (LOCK): Scope -- freezes Claim and
   all Falsification Conditions before any adversarial review pass begins"): does the self-
   documenting scope text reduce C-17 violations in degenerate runs compared to variations
   whose gates are named but not scope-declared?

---

```json
{"top_score_predicted": 100, "all_essential_pass": true, "new_v4_patterns": ["F-00 born in pre-declare section (CONTEXT/OPENING/INERTIA/Step2) -- not introduced during Skeptic pass", "dual-gate with explicit scope declarations: LOCK scope='claim+conditions', SEAL scope='Final list'", "named consolidation unit at peer heading level: ARCHIVIST/COLLECTOR/PHASE 5 -- all make omission a visible structural failure"]}
```
