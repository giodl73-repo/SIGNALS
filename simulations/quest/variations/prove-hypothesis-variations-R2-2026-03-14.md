Here are the 5 Round 2 variations for `prove-hypothesis`, written to `simulations/quest/variations/prove-hypothesis-variations-R2-2026-03-14.md`.

---

### Design summary

**Context from R1**: All 5 R1 variations were golden under v1 (2 aspirationals). The v2 rubric adds 3 new aspirationals (C-11 Skeptic gate, C-12 hard gate/read-only, C-13 status-quo as F-00 with observable test). Under v2, R1's top variations would score ~96–98, not 100.

---

### Single-axis variations

**V-01 — Adversarial scope**: Skeptic runs two named passes — Pass A: status-quo verdict (SUFFICIENT/INSUFFICIENT) before any per-condition work, Pass B: per-condition PASS/REWRITE. Tests whether unifying C-11 and C-13 into one adversarial role is cleaner than separate structural elements. **Covers C-11, C-13; missing C-12.**

**V-02 — Hard gate formalism**: V-04 from R1 (three roles) with one addition — a LOCK gate checklist between Skeptic and Navigator, read-only annotation on Navigator, and an amendment note slot. Minimal change to add C-12 without restructuring to a lifecycle model. **Covers C-11, C-12; missing C-13.**

**V-03 — Status-quo depth**: F-00 pre-printed with a dedicated two-part gap analysis block (what status quo delivers / what it cannot / why it matters), plus an "Insufficient because" field inside F-00 that copies the gap. The gap analysis always provides a confidence anchor even with zero prior signal artifacts. **Covers C-13; missing C-11, C-12.**

---

### Combination variations

**V-04 — Adversarial scope + Hard gate**: Three roles. Skeptic runs Pass A (status-quo, C-13) + Pass B (per-condition, C-11), followed by a LOCK gate checklist with amendment notes (C-12). The leanest form covering all 5 aspirationals. **Predicted 100/100.**

**V-05 — Full lifecycle + Skeptic + status-quo competing hypothesis**: Four phases with GATE 2 hard checklist (C-12) + named Skeptic in Phase 3 with per-condition verdicts (C-11) + status-quo competing hypothesis block with mandatory Skeptic verdict (C-13). Maximum structural coverage. The complexity test against V-04. **Predicted 100/100.**

---

### Predicted R2 scores under v2 rubric

| Variation | Predicted | Key differentiator |
|-----------|-----------|-------------------|
| V-04 | 100 | All 5 aspirationals; three-role leanness |
| V-05 | 100 | All 5 aspirationals; strongest C-12 isolation |
| V-01 | 98 | C-11 + C-13 unified; C-12 absent |
| V-02 | 98 | C-11 + C-12 from V-04 base; C-13 absent |
| V-03 | 96 | C-13 at maximum depth; C-11, C-12 absent |

**Open R3 question**: Does V-04's three-role structure produce equivalent live-run quality to V-05's four-phase isolation, or does the phase separation in V-05 produce materially cleaner C-05 compliance in degenerate cases?
d why-insufficient explanation (C-13). Maximum structural coverage. The complexity test:
does stacking all three mechanisms produce higher live-run quality or friction?

### Key design question for R2

V-04 and V-05 both target all 5 aspirational criteria. V-04 uses three roles; V-05 uses four
phases. The research question is whether the additional lifecycle scaffolding in V-05 produces
materially better C-05 compliance and C-13 depth, or whether V-04's leaner role structure
achieves the same coverage with less friction on live runs.

---

## V-01: Adversarial Scope (Skeptic Interrogates Status-Quo + Per-Condition)

**Axis:** Adversarial role gate scope -- Skeptic runs two explicit passes: Pass A challenges
status-quo sufficiency with a named SUFFICIENT/INSUFFICIENT verdict (C-13 + C-11 scope), then
Pass B writes per-condition PASS/REWRITE verdicts on each falsification candidate (C-11 core).

**Hypothesis:** If the Skeptic interrogates status-quo sufficiency first (Pass A), the adversarial
posture is primed before per-condition review (Pass B). The two questions reinforce each other:
"is doing nothing sufficient?" surfaces the core inertia challenge before "is this condition
observable?" refines the falsification list. Unifying them avoids a separate F-00 pre-printing
step and keeps the role structure to three roles.

```
You are running /prove-hypothesis. Fill in this structured template.
Three roles execute in sequence: Claimant declares, Skeptic challenges, Navigator plans.
Do not adjust the Claimant's claim or falsification conditions after the Skeptic gate.

---

## CLAIMANT: DECLARE
[No evidence references allowed here. Declare before examining.]

Prior signals check: [Search simulations/prove/ for any prior hypothesis, analysis, or synthesis
on this topic. List files found, or write "None -- starting fresh."]

Status-quo baseline: [One sentence. What does the team do today without this capability?
The Skeptic will interrogate this in Pass A.]

Claim: [One sentence. Use "is" or "will". No hedging.]

Falsification candidates (draft -- Skeptic will challenge in Pass B):
- [Condition 1: what observable outcome would prove this false?]
- [Condition 2: what observable outcome would prove this false?]
[Add more if needed. These are drafts; Skeptic must clear them.]

---

## SKEPTIC: CHALLENGE

The Skeptic runs two passes. Both must complete before confidence is written.

### PASS A: Status-Quo Verdict

Question: Could the team get equivalent value by doing nothing -- by continuing current
practice without this feature or capability?

Skeptic verdict:
[ ] INSUFFICIENT -- the status quo cannot produce the value the claim predicts. Proceed to Pass B.
    Why insufficient: [One sentence. What specific gap does current practice leave?]
    F-00: The hypothesis is false if the team gets equivalent value from current practice.
    Observable test: [What measurable outcome would indicate status-quo sufficiency?]
[ ] SUFFICIENT -- the status quo already satisfies the need. Stop. Revise the claim before proceeding.

### PASS B: Per-Condition Observability

[Each falsification candidate from DECLARE must receive an explicit Skeptic verdict.
Conditions that depend on subjective opinion or invisible internal states must be rewritten.]

| Candidate | Skeptic verdict | Rewritten condition (if REWRITE) |
|-----------|----------------|-----------------------------------|
| [Condition 1 text] | PASS (observable: [how measured]) / REWRITE | [Rewritten version] |
| [Condition 2 text] | PASS (observable: [how measured]) / REWRITE | [Rewritten version] |
[All candidates must reach PASS before continuing.]

Confirmation conditions:
| ID | Condition (hypothesis confirmed if this occurs) |
|----|--------------------------------------------------|
| CF-01 | [Positive confirmation criterion] |

Final falsification list (Skeptic-cleared, for Navigator reference):
| ID | Condition | Observable test |
|----|-----------|-----------------|
| F-00 | Status quo is sufficient (if Pass A verdict is INSUFFICIENT) | [from Pass A] |
| F-01 | [Cleared from Pass B] | [how observed] |
| F-02 | [Cleared from Pass B] | [how observed] |

---

## CLAIMANT: CONFIDENCE
[Written after both Skeptic passes complete.]

Value: [N]/100
Rationale: [2-3 sentences. Address two elements:
  (1) Why the status-quo verdict was INSUFFICIENT -- what specifically cannot be achieved
      by current practice?
  (2) What prior signal, trace finding, or friction point anchors the numeric value?
  If no prior signals: "No prior signals -- calibration based on status-quo gap analysis:
  [reasoning from Pass A]." The Pass A why-insufficient always provides an anchor.]

---

## NAVIGATOR: EXPERIMENTS
[Order by falsification risk: rank 1 = highest probability of proving the hypothesis false.
Include F-00 if Pass A verdict was INSUFFICIENT and risk is nonzero. Name a prove sub-skill
for each. Valid: prove:interview, prove:prototype, prove:analysis, prove:websearch,
prove:publish, prove:synthesize, prove:intelligence.]

| Rank | Experiment | prove sub-skill | Falsification conditions tested | Why this risk rank |
|------|-----------|-----------------|--------------------------------|--------------------|
| 1 | [Describe experiment] | prove:[sub-skill] | [F-ID, F-ID] | [Why highest falsification risk] |
| 2 | [Describe experiment] | prove:[sub-skill] | [F-ID, F-ID] | [Why second risk] |
[Add rows as needed. Every F-ID must appear in at least one experiment.]

---

Write artifact: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
Frontmatter: skill, topic, date, claim_summary, confidence, experiment_count,
             prior_signals_found (true/false), status_quo_verdict (INSUFFICIENT/SUFFICIENT),
             skeptic_rewrites (count of Pass B rewrites).
```

---

## V-02: Hard Gate Formalism (V-04 + LOCK Checklist)

**Axis:** Hard phase gate with read-only constraint -- V-04 from R1 (three roles: Claimant /
Skeptic / Navigator) with a single addition: a LOCK gate checklist between Skeptic and
Navigator that explicitly prohibits modifying DECLARE output. Navigator carries a read-only
annotation. Post-lock observability problems are logged as amendment notes, not edits.

**Hypothesis:** V-04 achieved C-11 (Skeptic) and C-09/C-10 (experiment table) in R1 but not
C-12. Adding one hard LOCK gate checklist with read-only annotation -- without restructuring
to a four-phase model -- is the minimal change to add C-12. This tests whether minimal extension
of the strongest R1 variation covers all 5 aspirationals with less structural weight than V-05.

```
You are running /prove-hypothesis. Fill in this structured template.
Three roles execute in sequence: Claimant declares, Skeptic challenges, Navigator plans.

LOCK RULE: After the Skeptic gate, claim and falsification conditions are read-only.
If Navigator identifies an observability problem, log it as an amendment note for the next
run -- do NOT revise the locked sections.

---

## CLAIMANT: DECLARE
[No evidence references allowed here. Declare before examining anything.]

Prior signals check: [Search simulations/prove/ for any prior hypothesis, analysis, or synthesis
on this topic. List files found, or write "None -- starting fresh."]

Claim: [One sentence. Use "is" or "will". No hedging. This is what you believe.]

Falsification candidates (draft -- Skeptic will challenge these next):
- [Condition 1: what observable outcome would prove this false?]
- [Condition 2: what observable outcome would prove this false?]
[Add more if needed.]

---

## SKEPTIC: CHALLENGE

[Each candidate from DECLARE must receive an explicit verdict before the LOCK gate.
Opinion-dependent conditions cannot pass -- they require a written REWRITE verdict.]

| Candidate | Skeptic verdict | Rewritten condition (if REWRITE) |
|-----------|----------------|-----------------------------------|
| [Condition 1 text] | PASS (observable: [how measured]) / REWRITE | [Rewritten version] |
| [Condition 2 text] | PASS (observable: [how measured]) / REWRITE | [Rewritten version] |
[All must reach PASS before the gate below.]

Confirmation conditions:
| ID | Condition (hypothesis confirmed if this occurs) |
|----|--------------------------------------------------|
| CF-01 | [Positive confirmation criterion] |

### GATE: LOCK
Before Navigator proceeds, all of the following must be true:
- [ ] Every falsification candidate has an explicit Skeptic PASS verdict
- [ ] No condition was silently removed (REWRITE verdicts have a written replacement)
- [ ] Claim is one sentence with no hedging
- [ ] At least two falsification conditions reached PASS
- [ ] No evidence, findings, or Navigator results are referenced in DECLARE

LOCKED. From this point, claim and falsification conditions above cannot be modified.
If a condition proves problematic during NAVIGATE, record it as an amendment note, not an edit.

---

## CLAIMANT: CONFIDENCE
[Written after LOCK gate. The lock is in effect -- do not revise claim or conditions here.]

Value: [N]/100
Rationale: [2-3 sentences. Reference at least one specific prior signal, trace finding, or
known friction point from this codebase. If no prior signals: "No prior signals -- confidence
is prior-free. Calibration based on [reasoning]." Do not omit the prior-evidence statement.]

---

## NAVIGATOR: EXPERIMENTS
[LOCK is in effect: do not revise claim or falsification conditions in this section.
If an experiment reveals a condition is unobservable, record it as an amendment note below.]

[Order by falsification risk: rank 1 = highest probability of falsifying the hypothesis.
Name a prove sub-skill for each. Valid: prove:interview, prove:prototype, prove:analysis,
prove:websearch, prove:publish, prove:synthesize, prove:intelligence.]

| Rank | Experiment | prove sub-skill | Falsification conditions tested | Why this risk rank |
|------|-----------|-----------------|--------------------------------|--------------------|
| 1 | [Describe experiment] | prove:[sub-skill] | [F-ID, F-ID] | [Why highest falsification risk] |
| 2 | [Describe experiment] | prove:[sub-skill] | [F-ID, F-ID] | [Why second risk] |
[Add rows. Every falsification condition must appear in at least one experiment.]

Amendment notes (post-lock): [F-NN: issue -- suggested rewrite for next hypothesis run.
Write "None" if no post-lock observability problems were discovered.]

---

Write artifact: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
Frontmatter: skill, topic, date, claim_summary, confidence, experiment_count,
             prior_signals_found (true/false), skeptic_rewrites (count),
             amendment_notes (count of post-lock issues).
```

---

## V-03: Status-Quo Depth (Gap Analysis Block + F-00 with Insufficient-Because)

**Axis:** Inertia framing depth -- F-00 is pre-printed with a dedicated two-part block:
(1) a named STATUS-QUO BASELINE section that states what current practice delivers AND
what it cannot deliver, (2) an "Insufficient because" field inside F-00 that copies the
gap. The gap analysis always provides a confidence anchor even with zero prior signal artifacts.

**Hypothesis:** The weakest C-13 form is a named F-00 row in a table. The strongest form
requires the PM to articulate the gap between what status quo delivers and what the claim
requires. Making this explanation a required prose block -- named and available for downstream
use -- produces richer confidence rationale (C-08), sharper experiment selection (C-04), and
a reusable gap statement that anchors the confidence value even when prior signals are absent.

```
You are running /prove-hypothesis. Fill in this structured template.
Declare the hypothesis after the status-quo baseline but before any domain evidence.
F-00 (status-quo competitor) is always the first falsification condition.

---

## SETUP: PRIOR SIGNALS
[Search simulations/prove/ for any prior hypothesis, analysis, or synthesis on this topic.]
Prior signals found: [List files found, or write "None -- starting fresh."]

---

## STATUS-QUO BASELINE
[Before declaring, establish what the team currently does without this feature.
This block is the anchor for F-00 and the confidence rationale below.]

Current practice: [One sentence. What does the team do today without this capability?]

Gap analysis:
- What current practice delivers: [One sentence -- what value does the status quo produce?]
- What current practice cannot deliver: [One sentence -- what specific value is absent or
  degraded without the proposed feature? Be concrete and observable.]
- Why the gap matters: [One sentence connecting the gap to a user outcome, metric, or known
  friction point. This becomes the confidence anchor.]

---

## HYPOTHESIS DECLARED
[Write claim AFTER the status-quo baseline, BEFORE any domain evidence is referenced.]

Claim: [One sentence. Use "is" or "will". No hedging.]

---

## FALSIFICATION CONDITIONS

F-00 is always the status-quo competitor. It is always the first condition.

**F-00 -- Status-quo competitor**
Condition: The hypothesis is false if the team achieves equivalent value using current
practice without this feature.
Observable test: [What measurable observation would indicate status-quo sufficiency?
Reference the gap analysis: what observable outcome would mean the gap does NOT exist?]
Insufficient because: [Copy the "cannot deliver" line from the gap analysis. This is the
affirmative claim that current practice is insufficient -- it must be falsifiable.]

Domain-specific falsification conditions:
| ID | Condition (hypothesis false if this occurs) | Observable test |
|----|---------------------------------------------|-----------------|
| F-01 | [Domain-specific condition] | [Observable measurement or behavior] |
| F-02 | [Domain-specific condition] | [Observable measurement or behavior] |
[Add F-03+ if needed. Every condition must name an observable test.]

Confirmation conditions:
| ID | Condition (hypothesis confirmed if this occurs) |
|----|--------------------------------------------------|
| CF-01 | [Positive confirmation criterion] |

---

## CONFIDENCE
Value: [N]/100
Rationale: [2-3 sentences structured around two required elements:
  (1) Why F-00 is insufficient -- reference the gap analysis specifically.
      "Current practice cannot [gap from baseline] because [reason from gap analysis]."
  (2) What prior signal, trace finding, or friction point anchors the numeric value.
      If no prior signals: "No prior signals. Numeric calibration from status-quo gap:
      [quote or paraphrase the 'why the gap matters' line]." The gap analysis always
      provides an anchor -- silence on the anchor fails.]

---

## EXPERIMENTS
[Order by falsification risk: rank 1 = highest probability of proving the hypothesis false.
Include at least one experiment that tests F-00 if status-quo risk is nonzero.
Name a prove sub-skill for each. Valid: prove:interview, prove:prototype, prove:analysis,
prove:websearch, prove:publish, prove:synthesize, prove:intelligence.]

| Rank | Experiment | prove sub-skill | Falsification conditions tested | Why this risk rank |
|------|-----------|-----------------|--------------------------------|--------------------|
| 1 | [Describe experiment] | prove:[sub-skill] | [F-00, F-01, ...] | [Why highest falsification risk] |
| 2 | [Describe experiment] | prove:[sub-skill] | [F-01, F-02, ...] | [Why second risk] |
[Add rows. Every F-ID must appear in at least one experiment.]

---

Write artifact: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
Frontmatter: skill, topic, date, claim_summary, confidence, experiment_count,
             prior_signals_found (true/false),
             status_quo_gap (one-sentence copy of "cannot deliver" from gap analysis).
```

---

## V-04: Adversarial Scope + Hard Gate (Three Roles, All Five Aspirationals)

**Axes:** Adversarial role gate scope (Skeptic runs Pass A: status-quo verdict + Pass B:
per-condition observability) + hard gate formalism (LOCK checklist with read-only constraint
and amendment note slot). Three roles: Claimant / Skeptic / Navigator. Covers C-11, C-12,
C-13 without a four-phase lifecycle.

**Hypothesis:** The full stack of R1's top two variations can be achieved in three roles
rather than four phases. Skeptic Pass A covers C-13 (status-quo as named falsification
condition with insufficient-because explanation). Skeptic Pass B covers C-11 (per-condition
PASS/REWRITE verdicts). The LOCK gate covers C-12 (hard checklist, read-only, amendment notes).
The experiment table covers C-09 and C-10. This is lighter than V-05's lifecycle but achieves
the same 5/5 aspirational coverage -- the leanness test.

```
You are running /prove-hypothesis. Fill in this structured template.
Three roles execute in sequence: Claimant declares, Skeptic challenges, Navigator plans.

LOCK RULE: After the Skeptic gate, claim and falsification conditions are read-only.
Post-lock observability problems are logged as amendment notes, not retroactive edits.

---

## CLAIMANT: DECLARE
[No evidence references allowed here. Declare before examining.]

Prior signals check: [Search simulations/prove/ for any prior hypothesis, analysis, or synthesis
on this topic. List files found, or write "None -- starting fresh."]

Status-quo baseline: [One sentence. What does the team do today without this capability?
The Skeptic will interrogate this in Pass A.]

Claim: [One sentence. Use "is" or "will". No hedging.]

Falsification candidates (draft -- Skeptic will challenge in Pass B):
- [Condition 1: observable outcome that would prove this false]
- [Condition 2: observable outcome that would prove this false]
[Add more if needed.]

---

## SKEPTIC: CHALLENGE

The Skeptic runs two passes. Both must complete before the LOCK gate.

### PASS A: Status-Quo Interrogation

Does the status-quo baseline already satisfy the need the claim addresses?

Skeptic verdict:
[ ] F-00 CONFIRMED -- status quo is INSUFFICIENT: the team cannot get equivalent value from
    current practice.
    Why insufficient: [One sentence. What specific gap does current practice leave?]
    F-00: The hypothesis is false if the team gets equivalent value from current practice.
    Observable test: [What measurable outcome would indicate status-quo sufficiency?]
[ ] F-00 CHALLENGED -- status quo may be SUFFICIENT. Stop. Revise claim before proceeding.

### PASS B: Per-Condition Observability
[Each falsification candidate from DECLARE must receive an explicit Skeptic verdict.
Conditions dependent on subjective opinion or invisible internal states receive REWRITE.]

| Candidate | Skeptic verdict | Rewritten condition (if REWRITE) |
|-----------|----------------|-----------------------------------|
| [Condition 1 text] | PASS (observable: [how measured]) / REWRITE | [Rewritten version] |
| [Condition 2 text] | PASS (observable: [how measured]) / REWRITE | [Rewritten version] |
[All must reach PASS before the gate.]

Confirmation conditions:
| ID | Condition (hypothesis confirmed if this occurs) |
|----|--------------------------------------------------|
| CF-01 | [Positive confirmation criterion] |

### GATE: LOCK
Before Navigator proceeds:
- [ ] Pass A: F-00 verdict written (CONFIRMED or CHALLENGED -- not absent)
- [ ] Pass B: Every candidate has an explicit PASS verdict
- [ ] No conditions were silently removed (REWRITE verdicts have a written replacement)
- [ ] Claim is one sentence with no hedging
- [ ] No findings, evidence, or Navigator results referenced in DECLARE

LOCKED. Claim and falsification conditions above are now read-only.

Final falsification list (for Navigator reference):
| ID | Condition | Observable test |
|----|-----------|-----------------|
| F-00 | Status quo is sufficient | [from Pass A, if CONFIRMED] |
| F-01 | [Cleared from Pass B] | [how observed] |
| F-02 | [Cleared from Pass B] | [how observed] |

---

## CLAIMANT: CONFIDENCE
[Written after LOCK gate. Lock is in effect -- do not revise claim or conditions here.]

Value: [N]/100
Rationale: [2-3 sentences. Address two elements:
  (1) Why F-00 is CONFIRMED -- what specifically makes current practice insufficient?
  (2) What prior signal, trace finding, or friction point anchors the numeric value?
  If no prior signals: "No prior signals -- calibration from status-quo gap and [reasoning]."
  Do not omit either element.]

---

## NAVIGATOR: EXPERIMENTS
[LOCK is in effect. If an experiment reveals a condition is problematic, log as amendment note.
Order by falsification risk: rank 1 = highest probability of falsifying the hypothesis.
Include F-00 if risk is nonzero. Name a prove sub-skill for each.
Valid: prove:interview, prove:prototype, prove:analysis, prove:websearch,
prove:publish, prove:synthesize, prove:intelligence.]

| Rank | Experiment | prove sub-skill | Falsification conditions tested | Why this risk rank |
|------|-----------|-----------------|--------------------------------|--------------------|
| 1 | [Describe experiment] | prove:[sub-skill] | [F-00, F-01, ...] | [Why highest falsification risk] |
| 2 | [Describe experiment] | prove:[sub-skill] | [F-01, F-02, ...] | [Why second risk] |
[Add rows. Every F-ID must appear in at least one experiment.]

Amendment notes (post-lock): [F-NN: issue -- suggested rewrite for next hypothesis run.
Write "None" if no post-lock observability problems discovered.]

---

Write artifact: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
Frontmatter: skill, topic, date, claim_summary, confidence, experiment_count,
             prior_signals_found (true/false), status_quo_verdict (CONFIRMED/CHALLENGED),
             skeptic_rewrites (count of Pass B rewrites), amendment_notes (count).
```

---

## V-05: Full Lifecycle + Skeptic + Status-Quo Competing Hypothesis

**Axes:** Lifecycle emphasis (four explicit phases, hard GATE 2 checklist with read-only
annotation) + adversarial role gate (named Skeptic in Phase 3 writing per-condition
PASS/REWRITE verdicts) + inertia framing (status-quo interrogated as competing hypothesis
in Phase 3 with mandatory why-insufficient explanation and explicit Skeptic verdict).

**Hypothesis:** The strongest structural enforcement of all five aspirationals requires
separating concerns across phases: SETUP loads context (enables C-08, C-13 baseline), DECLARE
locks the hypothesis (enables C-05 with hard gate, C-01/C-02/C-03), CHALLENGE runs the Skeptic
(C-11) and interrogates status-quo (C-13) with read-only access to DECLARE (C-12), PLAN maps
experiments to conditions with rationale (C-09, C-10). The research question: does the
additional lifecycle scaffolding produce higher live-run output quality than V-04's leaner
three-role structure, or does the complexity introduce friction?

```
You are running /prove-hypothesis.
Four phases execute in order. Each phase gate must complete before the next phase begins.
PHASE 2 (DECLARE) output is LOCKED after GATE 2. Phases 3 and 4 have read-only access.
Observability failures discovered after GATE 2 are logged as amendment notes, not edits.

---

## PHASE 1: SETUP
Goal: Load context. Establish prior signal state and status-quo baseline before declaring.

Prior signals: [Search simulations/prove/ for any prior hypothesis, analysis, or synthesis on
this topic. List files found with one-line summaries. Write "None -- starting fresh" if empty.]

Status-quo baseline: [One sentence. What does the team currently do without this capability?
This baseline will be interrogated as a competing hypothesis in PHASE 3 CHALLENGE.]

GATE 1 -- required before PHASE 2:
[ ] Prior signal state declared (found with summaries, or "None" -- silence fails)
[ ] Status-quo baseline written (one sentence minimum)

---

## PHASE 2: DECLARE
Goal: Write the hypothesis. No evidence from PHASE 1 alters the claim structure.
PHASE 2 output is LOCKED after GATE 2. Phases 3 and 4 are read-only on this section.

Claim: [One sentence. Use "is" or "will". No hedging. This is what you believe.]

The claim is false if ANY of:
- F-01: [Falsification condition -- observable outcome, not an opinion]
- F-02: [Falsification condition -- observable outcome, not an opinion]
[Add F-03+ as needed. Each must describe an observable outcome.]

The claim is confirmed if ANY of:
- CF-01: [Positive confirmation criterion]

Confidence: [N]/100
Why: [2-3 sentences. Cite at least one anchor from PHASE 1 prior signals or the status-quo
     baseline. If no prior signals: "No prior signals. Confidence prior-free: calibrated from
     [reasoning and status-quo baseline]." Do not omit an explicit anchor statement.]

GATE 2 -- required before PHASE 3:
[ ] Claim is one sentence with no hedging
[ ] At least two falsification conditions present
[ ] Each condition describes an observable outcome (not "they feel confused", not an opinion)
[ ] Confidence is numeric 0-100 with rationale citing at least one anchor
[ ] No evidence, findings, or Skeptic results from later phases referenced here

LOCKED. Phases 3 and 4 may not modify claim or falsification conditions.
Observability failures discovered in later phases: log as amendment notes below, do not edit.

---

## PHASE 3: CHALLENGE
Goal: Two interrogations. (1) Skeptic challenges each falsification condition for observability.
(2) Status-quo competing hypothesis receives an explicit Skeptic verdict.

Read-only access to PHASE 2: Do not modify claim or conditions. Log problems as amendment notes.

### SKEPTIC: Per-Condition Observability
[For each F-ID from PHASE 2 DECLARE, the Skeptic writes an explicit PASS or REWRITE verdict.
Conditions dependent on subjective opinion or invisible states must be flagged.]

| F-ID | Skeptic verdict | Issue or suggested rewrite (if flagged) |
|------|-----------------|------------------------------------------|
| F-01 | PASS (observable: [how measured]) / REWRITE | [Issue and suggested rewrite] |
| F-02 | PASS (observable: [how measured]) / REWRITE | [Issue and suggested rewrite] |
[All F-IDs must receive a verdict. Flagged conditions are logged as amendment notes below.]

### SKEPTIC: Status-Quo Competing Hypothesis
[The status-quo baseline from PHASE 1 is a competing hypothesis. The Skeptic writes an
explicit verdict before PHASE 4 is allowed to proceed.]

Competing hypothesis under scrutiny: "The team achieves equivalent value by continuing
current practice ([status-quo baseline from PHASE 1]) without this feature."

Skeptic verdict:
[ ] INSUFFICIENT -- status quo cannot produce the value the claim predicts.
    Why insufficient: [One sentence. What specific gap does current practice leave?]
    F-00: The hypothesis is false if the team gets equivalent value from current practice.
    Observable test: [What measurable outcome would indicate status-quo sufficiency?]
[ ] SUFFICIENT -- status quo already satisfies the need. Stop. Return to PHASE 2 and revise.

GATE 3 -- required before PHASE 4:
[ ] All F-IDs from PHASE 2 have received an explicit Skeptic verdict
[ ] Status-quo competing hypothesis has received an explicit INSUFFICIENT or SUFFICIENT verdict
[ ] Flagged conditions recorded as amendment notes below, not edited in PHASE 2

Amendment notes from PHASE 3 (if any): [F-NN: issue -- suggested rewrite for next run.
Write "None" if no flagged conditions.]

---

## PHASE 4: PLAN
Goal: Assign prove sub-skills. Order by falsification risk. Map to F-IDs. Cover all conditions.

[Include F-00 in the experiment set if Skeptic verdict was INSUFFICIENT and F-00 risk is nonzero.
Rank 1 = highest probability of falsifying the hypothesis.
Valid sub-skills: prove:interview, prove:prototype, prove:analysis, prove:websearch,
prove:publish, prove:synthesize, prove:intelligence.]

| Rank | Experiment | prove sub-skill | Falsification conditions tested | Risk rationale |
|------|-----------|-----------------|--------------------------------|----------------|
| 1 | [Describe experiment] | prove:[sub-skill] | [F-00, F-01, ...] | [Why rank 1?] |
| 2 | [Describe experiment] | prove:[sub-skill] | [F-01, F-02, ...] | [Why rank 2?] |
[Add rows. Every falsification condition (including F-00 if declared) must be covered.]

---

Write artifact: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
Frontmatter: skill, topic, date, claim_summary, confidence, experiment_count,
             prior_signals_found (true/false), status_quo_verdict (INSUFFICIENT/SUFFICIENT),
             skeptic_rewrites (count of flagged conditions), amendment_notes (count).
```

---

## Round 2 Design Notes

### Variation axis selection

Three single-axis variations:

- **Adversarial scope (V-01)**: Tests whether extending the Skeptic role to cover status-quo
  sufficiency (Pass A) alongside per-condition observability (Pass B) is more natural than
  pre-printing F-00 as a separate structural element. The two adversarial questions prime each
  other. Chosen because the C-11/C-13 interaction is the new research question in v2.

- **Hard gate formalism (V-02)**: Tests the minimal change: add only the LOCK gate checklist
  to R1's strongest variation (V-04) without restructuring to a lifecycle model. If V-02 scores
  5/5 aspirational with less structural weight than V-05, the lifecycle model adds friction
  without benefit. Chosen as the minimal addition baseline.

- **Status-quo depth (V-03)**: Tests whether a named two-part gap analysis block (delivers /
  cannot deliver / why it matters) produces richer C-08 and C-04 than F-00 as a table row.
  The gap analysis provides a confidence anchor even with zero prior signal artifacts, solving
  a real degenerate-case problem. Chosen because it targets C-13 at maximum depth.

Two combination variations:

- **V-04 (Adversarial scope + Hard gate)**: Three roles with Skeptic running two passes (C-11,
  C-13) and a LOCK gate checklist (C-12). The leanest form that covers all 5 aspirationals.
  The R1 candidate; tests whether three roles is sufficient.

- **V-05 (Full lifecycle + Skeptic + status-quo competing hypothesis)**: Four phases with
  hard gate (C-12) + named Skeptic in CHALLENGE (C-11) + status-quo competing hypothesis with
  mandatory verdict and why-insufficient (C-13). Maximum structural coverage. The complexity test.

### v2 rubric aspirational coverage by variation

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09: exp-to-falsification mapping | Pre-printed column | Pre-printed column | Pre-printed column | Pre-printed column | Pre-printed column |
| C-10: risk-ranked with rationale | Risk rank column + "Why this risk rank" | Risk rank column + "Why this risk rank" | Risk rank column + "Why this risk rank" | Risk rank column + "Why this risk rank" | Risk rationale column |
| C-11: Skeptic PASS/REWRITE per condition | Pass B explicit per-condition verdict | Explicit per-condition verdict | Not present | Pass B explicit per-condition verdict | Named Skeptic, explicit per-condition verdict |
| C-12: Hard gate, read-only, amendment notes | Not present | LOCK gate checklist + amendment notes | Not present | LOCK gate checklist + amendment notes | GATE 2 checklist + read-only annotation + amendment notes |
| C-13: Status-quo as F-00 with observable test | Pass A: F-00 with observable test + why-insufficient | Not present | Dedicated gap analysis block + F-00 with insufficient-because | Pass A: F-00 with observable test + why-insufficient | Competing hypothesis block + explicit Skeptic verdict |

**Predicted scores under v2 rubric (aspirational only):**
- V-01: C-09 PASS, C-10 PASS, C-11 PASS, C-12 FAIL, C-13 PASS → 4/5 → 8 pts
- V-02: C-09 PASS, C-10 PASS, C-11 PASS, C-12 PASS, C-13 FAIL → 4/5 → 8 pts
- V-03: C-09 PASS, C-10 PASS, C-11 FAIL, C-12 FAIL, C-13 PASS → 3/5 → 6 pts
- V-04: C-09 PASS, C-10 PASS, C-11 PASS, C-12 PASS, C-13 PASS → 5/5 → 10 pts
- V-05: C-09 PASS, C-10 PASS, C-11 PASS, C-12 PASS, C-13 PASS → 5/5 → 10 pts

**Predicted composite scores (all 13 criteria):**
- V-01: 60 + 30 + 8 = **98** | Golden: YES
- V-02: 60 + 30 + 8 = **98** | Golden: YES
- V-03: 60 + 30 + 6 = **96** | Golden: YES
- V-04: 60 + 30 + 10 = **100** | Golden: YES
- V-05: 60 + 30 + 10 = **100** | Golden: YES

### C-05 coverage comparison (v2 baseline)

| V | How C-05 is enforced |
|---|---------------------|
| V-01 | Instruction: "Do not adjust claim or conditions after the Skeptic gate" |
| V-02 | LOCK gate checklist: explicit list of what must be true + read-only annotation on Navigator |
| V-03 | Section ordering: HYPOTHESIS DECLARED after STATUS-QUO BASELINE, before domain evidence |
| V-04 | LOCK gate checklist: same as V-02 |
| V-05 | GATE 2 hard checklist + LOCKED annotation + read-only access declared per-phase |

V-05 and V-04 have equivalent hard gate strength. V-01 and V-03 rely on ordering/instruction --
structurally weaker. V-02 is equivalent to V-04 on C-05 enforcement.

### Open research questions for R3

1. Does V-04's three-role structure produce equivalent live-run output quality to V-05's
   four-phase structure, or does the phase separation in V-05 produce materially cleaner
   PHASE 2 isolation (C-05)? The structural difference is small but may matter in degenerate
   cases where the model conflates Setup and Declare.

2. Does V-01's Pass A + Pass B sequencing (status-quo first, per-condition second) improve
   the quality of Pass B verdicts by priming the adversarial posture? Or does splitting the
   Skeptic into two passes add complexity that reduces compliance on each pass individually?

3. Does V-03's dedicated gap analysis block produce richer downstream artifacts (confidence
   rationale, experiment rationale) than V-04/V-05's single-sentence why-insufficient? The
   gap analysis block is always available as an anchor; the question is whether naming it
   explicitly changes how the model uses it.
