Written to `simulations/quest/variations/prove-hypothesis-variations-R3-2026-03-14.md`.

---

## R3 Variations — Design Summary

**Three single-axis, two combined. All five predicted 100/100 under v3.**

### What the three new v3 criteria forced

| Criterion | What every R3 variation adds vs R2 |
|-----------|-------------------------------------|
| C-14 | Explicit `COVERAGE RULE` note in Navigator: every F-ID must appear in at least one row or it is an explicit failure |
| C-15 | Confidence section placed in document order **after** the LOCK gate (some variations use a dual LOCK+SEAL gate before Confidence) |
| C-16 | Explicit consolidation step merging Pass A (status-quo F-00) + Pass B (domain F-01+) into one `Final falsification list` with `CONFIRMED` per row, before Navigator |

### Variation axes

| Variation | Axis(es) | Key structural bet |
|-----------|----------|--------------------|
| **V-01** | Role sequence (domain-first) | Pass 1 per-condition before Pass 2 status-quo — cleared conditions prime the gap analysis |
| **V-02** | Output format (prose-only) | All 8 aspirationals achievable with numbered lists + inline annotation, no tables |
| **V-03** | Lifecycle emphasis (6 phases) | CONSOLIDATE as a named phase with its own SEAL gate makes C-16 structurally unskippable |
| **V-04** | Role sequence + Archivist role | Four named roles (Claimant / Skeptic / Archivist / Navigator) — omitting Archivist is a visible role skip, not a missed subsection |
| **V-05** | Conversational register + inertia-lead | Status-quo question leads before claim; plain-language LOCKED — tests whether register shift degrades C-05 |

### Open R4 questions
- Does a named role (V-04) or phase (V-03) enforce C-16 better than an embedded subsection (V-01/V-02/V-05) under context pressure?
- Does V-05's conversational freeze ("LOCKED. Your claim...cannot change") hold as well as formal LOCK RULE headers?
- Does domain-first pass order (V-01/V-04) produce richer F-00 gap analysis than status-quo-first (V-03/V-05)?
e -- not in Skeptic verdicts, not in the
Final falsification list, not in the Navigator. Hypothesis: structural guarantees (C-14,
C-15, C-16) hold in prose format; inline annotation satisfies C-09/C-10/C-11. **Tests
whether format-neutrality is achievable for all 8 aspirationals.**

**V-03 -- Lifecycle emphasis (CONSOLIDATE as explicit phase)**: Six phases: SETUP / DECLARE /
CHALLENGE / CONSOLIDATE / CONFIDENCE / NAVIGATE. Consolidation is a named phase with its own
gate (SEAL), making C-16 structurally impossible to skip. Confidence appears in a phase
explicitly sequenced after LOCK and SEAL, satisfying C-15 by phase order. **Tests whether
a dedicated CONSOLIDATE phase reduces degenerate-case C-16 failures vs embedding
consolidation inside the Skeptic section.**

---

### Combination variations

**V-04 -- Role sequence (reversed) + Consolidation role (Archivist)**: Four roles: Claimant /
Skeptic (per-condition first, status-quo second) / Archivist (consolidates) / Navigator. The
Archivist is a named role whose only job is producing the Final falsification list with
CONFIRMED verdicts and enforcing the SEAL gate. Hypothesis: separating consolidation into its
own named role removes cognitive load from the Skeptic and makes C-16 structurally
impossible to omit. **Tests whether a four-role structure achieves equivalent coverage to
V-03's six-phase lifecycle with less structural weight.**

**V-05 -- Phrasing register (conversational) + Inertia framing (lead question)**: The
artifact opens by asking "What exists today and why is it not enough?" before the claim is
stated. All instructions use second-person direct address and plain language. Status-quo
interrogation leads the flow, priming inertia awareness before the claim is committed.
Hypothesis: conversational register reduces first-run friction while all structural guarantees
(C-12 lock, C-14 coverage, C-15 post-lock confidence, C-16 consolidation) remain intact.
**Tests whether register shift degrades C-05 compliance in degenerate cases.**

---

### Predicted R3 scores under v3 rubric

| Variation | C-14 | C-15 | C-16 | All 8 asp? | Predicted | Golden |
|-----------|------|------|------|------------|-----------|--------|
| V-01 | Coverage rule note in Navigator | Confidence after LOCK + consolidation | Final list after both passes w/ CONFIRMED | YES | 100 | YES |
| V-02 | Coverage rule in prose Navigator | Confidence after LOCK + consolidation | Prose Final list w/ CONFIRMED | YES | 100 | YES |
| V-03 | Coverage rule in NAVIGATE phase | CONFIDENCE phase after SEAL | CONSOLIDATE phase + SEAL gate | YES | 100 | YES |
| V-04 | Coverage rule note in Navigator | Confidence after LOCK + SEAL | Archivist role produces Final list | YES | 100 | YES |
| V-05 | Coverage check before Step 7 submit | Confidence in Step 6, post-lock | Step 5 Final list w/ CONFIRMED | YES | 100 | YES |

**Open R3 questions**:
1. Does naming consolidation as an explicit phase (V-03) or role (V-04) produce stronger
   C-16 compliance than embedding it as a subsection (V-01/V-02/V-05) in degenerate runs?
2. Does V-05's conversational register maintain C-05 (no goalpost movement) as reliably as
   formal variations where "LOCK RULE" is a header, not a plain-language note?
3. Does V-01/V-04's reversed pass order (domain-first) produce richer F-00 gap analysis
   than V-03/V-05's status-quo-first sequencing?

---

## V-01: Role Sequence -- Per-Condition First, Status-Quo Second

**Axis:** Role sequence -- Skeptic runs Pass 1 (per-condition observability) before Pass 2
(status-quo interrogation), reversing the order used in R2's V-04. With domain conditions
cleared first, the Skeptic enters Pass 2 knowing what specific outcomes the claim predicts,
making the status-quo gap analysis sharper and more grounded.

**Hypothesis:** Per-condition work primes the adversarial posture for the status-quo
interrogation: once the Skeptic has forced each condition into observable form, the question
"could current practice already satisfy these conditions?" is more precisely answerable.
The reversed order is the single structural change from R2 V-04; all consolidation and
coverage mechanics are identical.

```
You are running /prove-hypothesis. Fill in this structured template.
Three roles execute in sequence: Claimant declares, Skeptic challenges, Navigator plans.

LOCK RULE: After the Skeptic gate, claim and falsification conditions are read-only.
Post-lock observability problems are logged as amendment notes, not retroactive edits.

---

## CLAIMANT: DECLARE
[No evidence references allowed here. Declare before examining.]

Prior signals check: [Search simulations/prove/ for any prior hypothesis, analysis, or
synthesis on this topic. List files found, or write "None -- starting fresh."]

Status-quo baseline: [One sentence. What does the team currently do without this capability?
The Skeptic will interrogate sufficiency in Pass 2, after domain conditions are cleared.]

Claim: [One sentence. Use "is" or "will". No hedging.]

Domain falsification candidates (draft -- Skeptic will challenge in Pass 1):
- [Condition 1: observable outcome that would prove this false]
- [Condition 2: observable outcome that would prove this false]
[Add more if needed.]

---

## SKEPTIC: CHALLENGE

The Skeptic runs two passes. Pass 1 clears domain conditions; Pass 2 interrogates
status-quo. Both must complete before the LOCK gate and consolidation.

### Pass 1: Per-Condition Observability
[Each domain falsification candidate from DECLARE receives an explicit verdict.
Conditions dependent on subjective opinion or invisible internal states receive REWRITE.]

| Candidate | Skeptic verdict | Rewritten condition (if REWRITE) |
|-----------|----------------|-----------------------------------|
| [Condition 1 text] | PASS (observable: [how measured]) / REWRITE | [Rewritten version] |
| [Condition 2 text] | PASS (observable: [how measured]) / REWRITE | [Rewritten version] |
[All candidates must reach PASS before Pass 2.]

Confirmation conditions:
| ID | Condition (hypothesis confirmed if this occurs) |
|----|--------------------------------------------------|
| CF-01 | [Positive confirmation criterion] |

### Pass 2: Status-Quo Interrogation
[With domain conditions cleared, interrogate whether current practice satisfies the need.
Reference cleared domain conditions to make the gap claim concrete.]

Competing hypothesis: "The team achieves equivalent value from current practice
([status-quo baseline from DECLARE]) without this feature."

Skeptic verdict:
[ ] INSUFFICIENT -- current practice cannot produce the value the claim predicts.
    Why insufficient: [One sentence. What specific gap does current practice leave?]
    F-00: The hypothesis is false if the team gets equivalent value from current practice.
    Observable test: [What measurable outcome would indicate status-quo sufficiency?]
[ ] SUFFICIENT -- status quo already satisfies the need. Stop. Revise claim before proceeding.

### GATE: LOCK
Before consolidation proceeds:
- [ ] Pass 1: Every domain candidate has an explicit PASS verdict
- [ ] Pass 1: Rewritten conditions have written replacements (no silent removal)
- [ ] Pass 2: Status-quo verdict written (INSUFFICIENT or SUFFICIENT -- not absent)
- [ ] Claim is one sentence with no hedging
- [ ] No findings or Navigator content referenced in DECLARE

LOCKED. Claim and falsification conditions above are now read-only.

### Consolidation
[Merge Pass 1 cleared domain conditions and Pass 2 F-00 into one enumerated Final
falsification list. Every condition receives an explicit CONFIRMED verdict.
F-00 goes first; cleared domain conditions follow in F-01+ order.
A partial list -- missing any condition from either pass -- is an explicit failure.]

Final falsification list:
| ID | Condition | Observable test | Verdict |
|----|-----------|-----------------|---------|
| F-00 | Status quo is sufficient | [from Pass 2 observable test] | CONFIRMED |
| F-01 | [Cleared from Pass 1] | [how observed] | CONFIRMED |
| F-02 | [Cleared from Pass 1] | [how observed] | CONFIRMED |
[Include every condition from Pass 1 and Pass 2. No F-ID may be absent.]

---

## CLAIMANT: CONFIDENCE
[Written after LOCK gate and consolidation. Lock is in effect -- do not revise conditions.]

Value: [N]/100
Rationale: [2-3 sentences. Address two elements:
  (1) Why F-00 is INSUFFICIENT -- what specific gap makes current practice not enough?
  (2) What prior signal, trace finding, or friction point anchors the numeric value?
  If no prior signals: "No prior signals -- calibration from status-quo gap: [reasoning]."
  Both elements required; silence on either fails.]

---

## NAVIGATOR: EXPERIMENTS
[LOCK is in effect. Order by falsification risk: rank 1 = highest probability of falsifying
the hypothesis. Use F-IDs from the Final falsification list only.
Valid sub-skills: prove:interview, prove:prototype, prove:analysis, prove:websearch,
prove:publish, prove:synthesize, prove:intelligence.
COVERAGE RULE: Every F-ID in the Final falsification list must appear in at least one
experiment row. Any F-ID with no experiment row is an explicit failure -- do not submit
the Navigator until all F-IDs are covered.]

| Rank | Experiment | prove sub-skill | F-IDs tested | Why this risk rank |
|------|-----------|-----------------|--------------|-------------------|
| 1 | [Describe experiment] | prove:[sub-skill] | [F-00, F-01] | [Why highest falsification risk] |
| 2 | [Describe experiment] | prove:[sub-skill] | [F-01, F-02] | [Why second risk] |
[Add rows until every F-ID from the Final falsification list is covered.]

Amendment notes (post-lock): [F-NN: issue -- suggested rewrite for next hypothesis run.
Write "None" if no post-lock observability problems were discovered.]

---

Write artifact: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
Frontmatter: skill, topic, date, claim_summary, confidence, experiment_count,
             prior_signals_found (true/false), status_quo_verdict (INSUFFICIENT/SUFFICIENT),
             skeptic_rewrites (count of Pass 1 rewrites), amendment_notes (count),
             f_id_count (total in Final list), f_id_coverage (all covered: true/false).
```

---

## V-02: Output Format -- Prose-First, No Tables

**Axis:** Output format -- All structure expressed as numbered lists and inline annotations.
No tabular format anywhere: not in Skeptic verdicts, not in the Final falsification list,
not in the Navigator experiment plan.

**Hypothesis:** The v3 structural guarantees (C-09 mapping, C-10 risk rank, C-11 Skeptic
verdicts, C-12 lock gate, C-14 coverage enforcement, C-15 confidence post-lock, C-16
consolidation) can all be satisfied via prose and numbered lists. Rubric language explicitly
permits "inline annotation" for C-09/C-10 and does not require tables for any criterion.
If true, prose-format artifacts are equally valid and impose lower template overhead for
authors who find tables cognitively heavy.

```
You are running /prove-hypothesis. Fill in this structured template.
Three roles execute in sequence: Claimant declares, Skeptic challenges, Navigator plans.
Format: prose and numbered lists only. No tables.

LOCK RULE: After the Skeptic gate, claim and falsification conditions are read-only.
Post-lock problems are logged as amendment notes, not retroactive edits.

---

## CLAIMANT: DECLARE

Prior signals: [Search simulations/prove/ for any prior hypothesis, analysis, or synthesis
on this topic. List file names found, or write "None -- starting fresh."]

Status-quo baseline: [One sentence. What does the team currently do without this capability?]

Claim: [One sentence. Use "is" or "will". No hedging. This is what you believe.]

Domain falsification candidates (draft -- Skeptic will review each):
1. F-01: [Observable outcome that would prove this false]
2. F-02: [Observable outcome that would prove this false]
[Add F-03+ if needed. Each must describe an observable, measurable outcome.]

---

## SKEPTIC: CHALLENGE

### Pass A: Status-Quo Interrogation

Could the team get equivalent value by continuing current practice without this feature?

Status-quo verdict: [INSUFFICIENT or SUFFICIENT]

If INSUFFICIENT:
  The gap: [One sentence. What specific value does current practice fail to deliver?]
  F-00: The hypothesis is false if the team gets equivalent value from current practice.
  Observable test for F-00: [What measurable outcome would indicate status-quo sufficiency?]

If SUFFICIENT: Stop. Return to DECLARE and revise the claim.

### Pass B: Per-Condition Observability

[For each domain condition from DECLARE, annotate it with an explicit Skeptic verdict.
Format for a passing condition:
  "F-NN [condition text]: PASS -- observable via [how you would observe or measure this]"
Format for a condition that requires rewriting:
  "F-NN [condition text]: REWRITE -- [what is wrong with it]. Revised: [new condition text]"
All conditions must reach PASS before the LOCK gate.]

F-01 [condition 1 text]: [PASS -- observable via / REWRITE -- problem. Revised: ...]
F-02 [condition 2 text]: [PASS -- observable via / REWRITE -- problem. Revised: ...]
[Continue for every candidate. No condition may be skipped.]

Confirmation conditions:
1. CF-01: [Positive confirmation criterion -- hypothesis confirmed if this occurs]

### GATE: LOCK

Confirm all before proceeding:
- [ ] Pass A: Status-quo verdict written (INSUFFICIENT or SUFFICIENT -- not absent)
- [ ] Pass B: Every F-NN candidate has an explicit PASS annotation
- [ ] Every REWRITE has a written replacement (no silent removal)
- [ ] Claim is one sentence with no hedging
- [ ] No findings or Navigator content referenced in DECLARE

LOCKED. Claim and conditions above are now read-only.

### Consolidation

[Collect all cleared conditions from Pass A (F-00) and Pass B (F-01+) into one Final
falsification list. Every condition receives an explicit CONFIRMED verdict. List F-00
first, then F-01+ in order. Missing any condition from either pass is an explicit failure.]

Final falsification list:
- F-00: [Status-quo condition text] -- observable via [test from Pass A] -- CONFIRMED
- F-01: [Cleared condition text] -- observable via [Pass B annotation] -- CONFIRMED
- F-02: [Cleared condition text] -- observable via [Pass B annotation] -- CONFIRMED
[Add a line for every condition from Pass A and Pass B. No F-ID may be absent.]

---

## CLAIMANT: CONFIDENCE
[Written after LOCK gate and consolidation. Lock is in effect -- do not revise conditions.]

Confidence: [N]/100

Rationale: [2-3 sentences. Two required elements:
  (1) Why F-00 is INSUFFICIENT -- what specific gap does current practice leave?
  (2) At least one prior signal, trace finding, or friction point anchoring the number.
  If no prior signals: "No prior signals -- calibrated from status-quo gap: [reasoning]."
  Both elements required; silence on either fails.]

---

## NAVIGATOR: EXPERIMENTS

[Order experiments from most likely to falsify the hypothesis (rank 1) to least.
Name a prove sub-skill for each. Map F-IDs from the Final falsification list above.
Valid sub-skills: prove:interview, prove:prototype, prove:analysis, prove:websearch,
prove:publish, prove:synthesize, prove:intelligence.

COVERAGE RULE: Before submitting, verify every F-ID in the Final falsification list
appears under at least one experiment. Any F-ID with no experiment is an explicit
failure -- add an experiment before writing the artifact.]

1. [Describe experiment]
   Sub-skill: prove:[sub-skill]
   F-IDs tested: [F-00, F-01, ...]
   Risk rationale: [Why is this ranked 1? What would this experiment falsify first?]

2. [Describe experiment]
   Sub-skill: prove:[sub-skill]
   F-IDs tested: [F-01, F-02, ...]
   Risk rationale: [Why is this ranked 2?]

[Add experiments until every F-ID in the Final falsification list is covered.]

Amendment notes: [F-NN: issue -- suggested rewrite for next hypothesis run.
Write "None" if no post-lock problems discovered.]

---

Write artifact: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
Frontmatter: skill, topic, date, claim_summary, confidence, experiment_count,
             prior_signals_found (true/false), status_quo_verdict (INSUFFICIENT/SUFFICIENT),
             skeptic_rewrites (count), amendment_notes (count),
             f_id_count (total in Final list), f_id_coverage (all covered: true/false).
```

---

## V-03: Lifecycle Emphasis -- CONSOLIDATE as Explicit Phase

**Axis:** Lifecycle emphasis -- Six phases: SETUP / DECLARE / CHALLENGE / CONSOLIDATE /
CONFIDENCE / NAVIGATE. Consolidation is a named phase with its own gate (SEAL), making C-16
structurally impossible to skip. Confidence appears in a phase explicitly ordered after both
LOCK (end of DECLARE) and SEAL (end of CONSOLIDATE), satisfying C-15 by phase structure
rather than by section placement instruction.

**Hypothesis:** When consolidation is a phase peer (not an appendix to the Skeptic section),
the model cannot produce a Navigator before producing a complete Final falsification list.
The SEAL gate forces full accountability: it checks that every F-ID from both Skeptic passes
is present with a CONFIRMED verdict before any downstream work proceeds. This structural
separation produces higher C-16 compliance in degenerate cases than embedding consolidation
as a subsection of the Skeptic role.

```
You are running /prove-hypothesis.
Six phases execute in order. Each gate must complete before the next phase begins.
PHASE 2 output is LOCKED after GATE 2. Phases 3-6 have read-only access to PHASE 2.
PHASE 4 produces the Final falsification list. Navigator may only reference this list.

---

## PHASE 1: SETUP
Goal: Load context. Establish prior signal state and status-quo baseline.

Prior signals: [Search simulations/prove/ for any prior hypothesis, analysis, or synthesis
on this topic. List files found with one-line summaries. Write "None -- starting fresh" if empty.]

Status-quo baseline: [One sentence. What does the team currently do without this capability?
This baseline will be interrogated as a competing hypothesis in PHASE 3.]

GATE 1 -- required before PHASE 2:
- [ ] Prior signal state declared (files listed, or explicit "None" -- silence fails)
- [ ] Status-quo baseline written (one sentence minimum)

---

## PHASE 2: DECLARE
Goal: Write the hypothesis. No prior-evidence anchoring of conditions here.
PHASE 2 output is LOCKED after GATE 2. Phases 3-6 may not modify this section.

Claim: [One sentence. Use "is" or "will". No hedging.]

Domain falsification candidates (PHASE 3 Skeptic will challenge these):
| ID | Condition (hypothesis false if this occurs) |
|----|---------------------------------------------|
| F-01 | [Observable outcome that would prove the claim false] |
| F-02 | [Observable outcome that would prove the claim false] |
[Add F-03+ if needed. Each must describe an observable outcome.]

Confirmation conditions:
| ID | Condition (hypothesis confirmed if this occurs) |
|----|--------------------------------------------------|
| CF-01 | [Positive confirmation criterion] |

GATE 2 -- required before PHASE 3:
- [ ] Claim is one sentence with no hedging
- [ ] At least two falsification conditions present
- [ ] Each condition describes an observable outcome (not an opinion, not invisible state)
- [ ] No findings, Skeptic verdicts, or Navigator content referenced here

LOCKED. Phases 3-6 may not modify claim or conditions.
Problems discovered in later phases: log as amendment notes -- do not edit here.

---

## PHASE 3: CHALLENGE
Goal: Skeptic interrogates (A) status-quo sufficiency and (B) each domain condition.
Read-only access to PHASE 2. Log problems as amendment notes; do not edit locked sections.

### 3A: Status-Quo Interrogation
Competing hypothesis: "The team achieves equivalent value from current practice
([status-quo baseline from PHASE 1]) without this feature."

Skeptic verdict:
[ ] INSUFFICIENT -- current practice cannot deliver the value the claim predicts.
    Why insufficient: [One sentence. What specific gap does current practice leave?]
    F-00: The hypothesis is false if the team gets equivalent value from current practice.
    Observable test: [What measurable outcome would indicate status-quo sufficiency?]
[ ] SUFFICIENT -- status quo already satisfies the need. Stop. Return to PHASE 2 and revise.

### 3B: Per-Condition Observability
[Each F-ID from PHASE 2 must receive an explicit Skeptic verdict.
Opinion-dependent or invisible-state conditions must be flagged REWRITE.]

| F-ID | Skeptic verdict | Issue or rewritten condition (if REWRITE) |
|------|-----------------|-------------------------------------------|
| F-01 | PASS (observable: [how measured]) / REWRITE | [Issue and rewrite] |
| F-02 | PASS (observable: [how measured]) / REWRITE | [Issue and rewrite] |
[All F-IDs from PHASE 2 must appear here. None may be silently omitted.]

GATE 3 -- required before PHASE 4:
- [ ] 3A: Status-quo verdict written (INSUFFICIENT or SUFFICIENT -- not absent)
- [ ] 3B: Every F-ID from PHASE 2 has received an explicit verdict
- [ ] Rewritten conditions have written replacements (no silent removal)
- [ ] No modifications made to PHASE 2 sections

Amendment notes from PHASE 3: [F-NN: issue -- suggested rewrite for next hypothesis run.
Write "None" if no flagged conditions.]

---

## PHASE 4: CONSOLIDATE
Goal: Merge all Skeptic-cleared conditions into one Final falsification list before
Navigator population. Every condition receives an explicit CONFIRMED verdict.

[Collect F-00 from PHASE 3A and all cleared conditions from PHASE 3B.
F-00 goes first; cleared domain conditions follow in F-01+ order.
Every condition from both PHASE 3A and PHASE 3B must appear.
A partial list -- missing any F-ID from either pass -- is an explicit failure.]

Final falsification list:
| ID | Condition | Observable test | Verdict |
|----|-----------|-----------------|---------|
| F-00 | Status quo is sufficient | [from PHASE 3A observable test] | CONFIRMED |
| F-01 | [Cleared from PHASE 3B] | [how observed] | CONFIRMED |
| F-02 | [Cleared from PHASE 3B] | [how observed] | CONFIRMED |
[Add rows until every condition from PHASE 3A and PHASE 3B is present.]

SEAL -- required before PHASE 5:
- [ ] F-00 present with CONFIRMED verdict (from PHASE 3A)
- [ ] Every F-ID from PHASE 3B present with CONFIRMED verdict
- [ ] No F-ID from either pass is absent from the Final list
- [ ] All observable tests are filled in (no blank cells)

SEALED. The Final falsification list above is the authoritative source for PHASES 5-6.

---

## PHASE 5: CONFIDENCE
Goal: Record confidence after LOCK (GATE 2) and SEAL are both confirmed.
[Both gates are in effect. Do not revise claim or conditions here.]

Value: [N]/100
Rationale: [2-3 sentences. Two required elements:
  (1) Why F-00 is INSUFFICIENT -- what specific gap does current practice leave?
      Reference the PHASE 1 status-quo baseline and the PHASE 3A why-insufficient.
  (2) At least one prior signal, trace finding, or friction point anchoring the number.
  If no prior signals: "No prior signals -- calibrated from status-quo gap: [reasoning]."
  Both elements required; silence on either fails.]

---

## PHASE 6: NAVIGATE
Goal: Assign prove sub-skills, ordered by falsification risk. Source: PHASE 4 Final list only.

[Rank 1 = highest probability of falsifying the hypothesis. Name a prove sub-skill for each.
Valid sub-skills: prove:interview, prove:prototype, prove:analysis, prove:websearch,
prove:publish, prove:synthesize, prove:intelligence.
COVERAGE RULE: Every F-ID in the PHASE 4 Final falsification list must appear in at least
one experiment row. Any F-ID with no experiment row is an explicit failure -- do not write
the artifact until all F-IDs from the Final list are covered.]

| Rank | Experiment | prove sub-skill | F-IDs tested | Risk rationale |
|------|-----------|-----------------|--------------|----------------|
| 1 | [Describe experiment] | prove:[sub-skill] | [F-00, F-01] | [Why highest risk] |
| 2 | [Describe experiment] | prove:[sub-skill] | [F-01, F-02] | [Why second risk] |
[Add rows until all F-IDs from the PHASE 4 Final falsification list are covered.]

---

Write artifact: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
Frontmatter: skill, topic, date, claim_summary, confidence, experiment_count,
             prior_signals_found (true/false), status_quo_verdict (INSUFFICIENT/SUFFICIENT),
             skeptic_rewrites (count of REWRITE verdicts in 3B), amendment_notes (count),
             f_id_count (total F-IDs in Final list), f_id_coverage (all covered: true/false).
```

---

## V-04: Combined -- Reversed Pass Order + Archivist Role

**Axes:** Role sequence (per-condition first, status-quo second) + consolidation assigned to
a new named role (Archivist), separating merge responsibility from the Skeptic.

**Hypothesis:** Giving consolidation its own named role removes cognitive load from the
Skeptic (who already runs two non-trivial passes) and makes the C-16 consolidation step
structurally impossible to skip: the Archivist's only job is producing the SEALED Final
falsification list. A model that omits the Archivist section omits a named role, which is
more visibly a failure than omitting a sub-subsection within the Skeptic. The reversed pass
order (domain-first) improves status-quo interrogation quality by giving the Skeptic
concrete domain conditions to reference when evaluating the gap claim. Four roles: Claimant /
Skeptic / Archivist / Navigator -- a lean alternative to V-03's six-phase structure.

```
You are running /prove-hypothesis. Fill in this structured template.
Four roles execute in sequence: Claimant declares, Skeptic challenges, Archivist
consolidates, Navigator plans.

LOCK RULE: After the Skeptic gate, claim and falsification conditions are read-only.
SEAL RULE: After the Archivist gate, the Final falsification list is the authoritative
source for the Navigator. Navigator may only reference F-IDs from the Final list.
Post-lock problems are logged as amendment notes, not retroactive edits.

---

## CLAIMANT: DECLARE
[No evidence references allowed here. Declare before examining.]

Prior signals check: [Search simulations/prove/ for any prior hypothesis, analysis, or
synthesis on this topic. List files found, or write "None -- starting fresh."]

Status-quo baseline: [One sentence. What does the team currently do without this capability?
The Skeptic will interrogate sufficiency in Pass 2, after domain conditions are cleared.]

Claim: [One sentence. Use "is" or "will". No hedging.]

Domain falsification candidates (draft -- Skeptic will challenge in Pass 1):
- [Condition 1: observable outcome that would prove this false]
- [Condition 2: observable outcome that would prove this false]
[Add more if needed.]

---

## SKEPTIC: CHALLENGE

The Skeptic runs two passes. Pass 1 clears domain conditions; Pass 2 interrogates
status-quo. Both must complete before the LOCK gate.

### Pass 1: Per-Condition Observability
[Each domain falsification candidate from DECLARE receives an explicit verdict.
Opinion-dependent or invisible-state conditions must be rewritten.]

| Candidate | Skeptic verdict | Rewritten condition (if REWRITE) |
|-----------|----------------|-----------------------------------|
| [Condition 1 text] | PASS (observable: [how measured]) / REWRITE | [Rewritten version] |
| [Condition 2 text] | PASS (observable: [how measured]) / REWRITE | [Rewritten version] |
[All candidates must reach PASS before Pass 2.]

Confirmation conditions:
| ID | Condition (hypothesis confirmed if this occurs) |
|----|--------------------------------------------------|
| CF-01 | [Positive confirmation criterion] |

### Pass 2: Status-Quo Interrogation
[With domain conditions cleared, interrogate whether current practice already satisfies
the need. Reference cleared domain conditions to make the gap analysis concrete.]

Competing hypothesis: "The team achieves equivalent value from current practice
([status-quo baseline from DECLARE]) without this feature."

Skeptic verdict:
[ ] INSUFFICIENT -- current practice cannot produce the value the claim predicts.
    Why insufficient: [One sentence. What specific gap does current practice leave?]
    F-00: The hypothesis is false if the team gets equivalent value from current practice.
    Observable test: [What measurable outcome would indicate status-quo sufficiency?]
[ ] SUFFICIENT -- status quo already satisfies the need. Stop. Revise claim before proceeding.

### GATE: LOCK
Before the Archivist proceeds:
- [ ] Pass 1: Every domain candidate has an explicit PASS verdict
- [ ] Pass 1: Rewritten conditions have written replacements (no silent removal)
- [ ] Pass 2: Status-quo verdict written (INSUFFICIENT or SUFFICIENT -- not absent)
- [ ] Claim is one sentence with no hedging
- [ ] No findings or Navigator content referenced in DECLARE

LOCKED. Claim and falsification conditions above are now read-only.

---

## ARCHIVIST: CONSOLIDATE
[Merge Pass 1 cleared domain conditions and Pass 2 F-00 into one enumerated Final
falsification list. Every condition receives an explicit CONFIRMED verdict.
F-00 goes first (status-quo competitor); cleared domain conditions follow in F-01+ order.
A partial list -- missing any condition from either pass -- is an explicit failure.
The Archivist does not add new conditions; it only collects and confirms what the Skeptic produced.]

Final falsification list:
| ID | Condition | Observable test | Verdict |
|----|-----------|-----------------|---------|
| F-00 | Status quo is sufficient | [from Skeptic Pass 2 observable test] | CONFIRMED |
| F-01 | [Cleared from Pass 1] | [how observed] | CONFIRMED |
| F-02 | [Cleared from Pass 1] | [how observed] | CONFIRMED |
[Include every condition from Pass 1 and Pass 2. No F-ID may be absent.]

### GATE: SEAL
Before Confidence and Navigator proceed:
- [ ] F-00 present with CONFIRMED verdict (from Pass 2)
- [ ] Every domain condition from Pass 1 present with CONFIRMED verdict
- [ ] No condition from either pass is absent from the Final list
- [ ] All observable tests filled in (no blank cells)

SEALED. The Final falsification list above is the authoritative source for Navigator.

---

## CLAIMANT: CONFIDENCE
[Written after LOCK gate and SEAL gate. Both are in effect -- do not revise conditions here.]

Value: [N]/100
Rationale: [2-3 sentences. Address two elements:
  (1) Why F-00 is INSUFFICIENT -- what specific gap makes current practice not enough?
      Reference the Pass 2 why-insufficient explanation.
  (2) What prior signal, trace finding, or friction point anchors the numeric value?
  If no prior signals: "No prior signals -- calibration from status-quo gap: [reasoning]."
  Both elements required; silence on either fails.]

---

## NAVIGATOR: EXPERIMENTS
[LOCK and SEAL are in effect. Use F-IDs from the Archivist's Final falsification list only.
Order by falsification risk: rank 1 = highest probability of falsifying the hypothesis.
Valid sub-skills: prove:interview, prove:prototype, prove:analysis, prove:websearch,
prove:publish, prove:synthesize, prove:intelligence.
COVERAGE RULE: Every F-ID in the Final falsification list must appear in at least one
experiment row. Any F-ID with no experiment row is an explicit failure -- do not write
the artifact until all F-IDs are covered.]

| Rank | Experiment | prove sub-skill | F-IDs tested | Why this risk rank |
|------|-----------|-----------------|--------------|-------------------|
| 1 | [Describe experiment] | prove:[sub-skill] | [F-00, F-01] | [Why highest falsification risk] |
| 2 | [Describe experiment] | prove:[sub-skill] | [F-01, F-02] | [Why second risk] |
[Add rows until every F-ID from the Final falsification list is covered.]

Amendment notes (post-lock): [F-NN: issue -- suggested rewrite for next hypothesis run.
Write "None" if no post-lock observability problems were discovered.]

---

Write artifact: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
Frontmatter: skill, topic, date, claim_summary, confidence, experiment_count,
             prior_signals_found (true/false), status_quo_verdict (INSUFFICIENT/SUFFICIENT),
             skeptic_rewrites (count of Pass 1 rewrites), amendment_notes (count),
             f_id_count (total F-IDs in Final list), f_id_coverage (all covered: true/false).
```

---

## V-05: Combined -- Conversational Register + Inertia-Lead Framing

**Axes:** Phrasing register (second-person direct address, plain language, numbered steps
instead of named roles) + inertia framing as the lead question ("What exists today and why
is it not enough?" precedes the claim in document order).

**Hypothesis:** Conversational register reduces first-run friction: the artifact reads as a
guided interview rather than a form to fill out. Opening with the status-quo question primes
inertia-awareness before the claim is committed, making F-00's "why insufficient" explanation
feel organic rather than procedural. All structural guarantees (C-12 lock, C-14 coverage,
C-15 post-lock confidence, C-16 consolidation) are preserved through embedded gate checklists
and coverage notes written in plain language. Primary risk: does "LOCKED" in a plain-language
checklist carry the same freeze semantics as "LOCKED" in a formal role template, or does
C-05 compliance degrade in degenerate cases?

```
You are running /prove-hypothesis.
Answer each question in order. Each step must complete before the next begins.
After the lock in Step 4, your claim and conditions are frozen -- you cannot move the
goalposts. After Step 5, the Final list is the only source for your experiments.

---

## Step 1: What prior work exists?

[Search simulations/prove/ for any prior hypothesis, analysis, or synthesis on this topic.
List the file names and one-line summaries. If nothing exists, write "None found."]

---

## Step 2: What does the team do today?

Current practice: [One sentence. What does the team currently do without this capability?
Be specific -- you will be asked to defend whether this is sufficient.]

---

## Step 3: Is the current practice good enough?

Could the team keep doing that and still get the value you are about to claim to deliver?
Give an explicit verdict -- silence fails.

[ ] Not good enough (INSUFFICIENT): current practice leaves a real gap.
    The gap: [One sentence. What specifically can the team NOT do or achieve today?]
    F-00: This hypothesis is false if the team gets equivalent value from current practice.
    How you would know F-00 is true: [What measurable outcome would indicate that current
    practice is actually sufficient?]

[ ] Already good enough (SUFFICIENT): the status quo satisfies the need.
    If SUFFICIENT: Stop. Revise your claim in Step 4 before proceeding.

---

## Step 4: What do you believe?

[Write your claim here, after establishing current practice above but before examining any
domain evidence. This is your commitment. You cannot revise it after seeing results.]

Claim: [One sentence. Use "is" or "will". No "might", no hedging, no compound claims.]

What would prove you wrong:
1. F-01: [Observable outcome that would prove the claim false]
2. F-02: [Observable outcome that would prove the claim false]
[Add more. Each must name something observable or measurable -- not a feeling or opinion.]

What would confirm you right:
1. CF-01: [Positive confirmation criterion]

A Skeptic reviews each condition -- can it actually be observed?

F-01 [condition text]: [PASS -- you can observe this via [how] /
                        REWRITE -- problem: [what is wrong]. Revised: [new condition text]]
F-02 [condition text]: [PASS -- you can observe this via [how] /
                        REWRITE -- problem: [what is wrong]. Revised: [new condition text]]
[Continue for every condition. None may be skipped.]

Before continuing, confirm:
- [ ] Step 3: Status-quo verdict is written (INSUFFICIENT or SUFFICIENT -- not absent)
- [ ] Step 4: Every condition has an explicit PASS annotation
- [ ] Every REWRITE has a written replacement (no silent removal)
- [ ] Your claim is one sentence with no hedging
- [ ] Nothing from Steps 5-7 has leaked into Step 4

LOCKED. Your claim and conditions above cannot change from this point.
If you discover a problem with a condition later, log it as an amendment note in Step 7.

---

## Step 5: Collect all conditions

[Bring together everything from Steps 3 and 4 into one Final list.
F-00 (from Step 3) goes first; F-01+ (from Step 4) follow in order.
Every condition gets an explicit CONFIRMED verdict.
This is the only list your experiments will reference.
Missing any condition from either step is an explicit failure.]

Final falsification list:
| # | Condition | How you would observe it | Verdict |
|---|-----------|--------------------------|---------|
| F-00 | Status quo is sufficient | [from Step 3] | CONFIRMED |
| F-01 | [Cleared from Step 4] | [from Step 4 PASS annotation] | CONFIRMED |
| F-02 | [Cleared from Step 4] | [from Step 4 PASS annotation] | CONFIRMED |
[Add a row for every condition from Steps 3 and 4. No condition may be absent.]

---

## Step 6: How confident are you?

[Write your confidence after the lock above is in effect.]

Confidence: [N]/100

Why: [2-3 sentences. Two required elements:
  (1) Why the gap from Step 3 is real -- what specifically can current practice not deliver?
  (2) Something from your prior work (signal files, known friction, a trace finding) that
      anchors the number. If you have nothing prior: "No prior signals. Calibrated from the
      Step 3 gap: [your reasoning]."
  Both elements required; silence on either fails.]

---

## Step 7: Plan the experiments

[Order your experiments from most likely to falsify your hypothesis (rank 1) to least.
Pick a prove sub-skill for each. Map each to F-IDs from the Step 5 Final list.
Valid sub-skills: prove:interview, prove:prototype, prove:analysis, prove:websearch,
prove:publish, prove:synthesize, prove:intelligence.
COVERAGE CHECK: Before submitting, verify that every F-ID in Step 5 appears under at
least one experiment. An F-ID with no experiment is a blind spot in your plan --
add an experiment before writing the artifact.]

| Rank | What you will do | prove sub-skill | F-IDs it tests | Why this risk rank |
|------|-----------------|-----------------|----------------|-------------------|
| 1 | [Describe experiment] | prove:[sub-skill] | [F-00, F-01] | [Why most likely to falsify?] |
| 2 | [Describe experiment] | prove:[sub-skill] | [F-01, F-02] | [Why second?] |
[Add rows until every F-ID from Step 5 is covered.]

Amendment notes: [F-NN: problem found post-lock -- suggested rewrite for next run.
Write "None" if no problems discovered.]

---

Write artifact: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
Frontmatter: skill, topic, date, claim_summary, confidence, experiment_count,
             prior_signals_found (true/false), status_quo_verdict (INSUFFICIENT/SUFFICIENT),
             skeptic_rewrites (count), amendment_notes (count),
             f_id_count (total in Final list), f_id_coverage (all covered: true/false).
```

---

## Round 3 Design Notes

### Variation axis selection

Three single-axis variations:

- **Role sequence reversed (V-01)**: Tests pass order effect on Skeptic output quality.
  Per-condition work first gives the Skeptic concrete observable conditions before the
  status-quo question. R2 V-04 used status-quo-first (Pass A before Pass B); this variation
  inverts it. Chosen because R2's open question was whether Pass A primes Pass B or whether
  the reverse is true.

- **Prose-first format (V-02)**: Tests format neutrality across all 8 aspirationals. All v3
  rubric criteria have prose-compatible pass conditions (C-09 "inline annotation acceptable",
  C-16 "enumerated list"). If V-02 scores 100/100, the rubric is format-neutral; if not, the
  failing criteria reveal implicit table dependencies that should be made explicit.

- **CONSOLIDATE as explicit phase (V-03)**: Tests whether naming consolidation as a phase
  peer reduces C-16 degenerate-case failures. Six phases force a structural SEAL gate; the
  model cannot populate the Navigator without completing a named phase. Chosen because C-16
  is the hardest new criterion to enforce -- it requires a step easy to declare "done" without
  actually merging both pass outputs with verdicts.

Two combination variations:

- **V-04 (reversed order + Archivist role)**: Extends V-01's reversed pass order with a
  dedicated Archivist role for consolidation. Tests whether four roles (Claimant / Skeptic /
  Archivist / Navigator) achieve equivalent C-16 compliance to V-03's six phases with less
  structural overhead. The key bet: a model that omits the Archivist section skips a named
  role (a visible failure), whereas one that omits a Skeptic subsection skips a sub-heading
  (a less visible failure).

- **V-05 (conversational + inertia-lead)**: Tests the outer boundary of register variation.
  If the same structural guarantees hold in a plain-language numbered-steps format, the
  skill's structural properties are robust across surface variations. Primary risk: whether
  "LOCKED" in a confirmation checklist carries the same cognitive freeze signal as "LOCKED"
  in a named-role LOCK RULE header.

### v3 rubric aspirational coverage by variation

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09: exp-to-F mapping | "F-IDs tested" column | "F-IDs tested" inline | "F-IDs tested" column | "F-IDs tested" column | "F-IDs it tests" column |
| C-10: risk-ranked + rationale | Risk rank + "Why" column | Risk rationale inline | Risk rationale column | Risk rationale column | Risk rank + "Why" column |
| C-11: Skeptic PASS/REWRITE | Pass 1 explicit per-condition | Pass B inline annotations | 3B explicit per-condition | Pass 1 explicit per-condition | Inline per-condition in Step 4 |
| C-12: Hard gate + read-only + amendments | LOCK gate checklist + amendment notes | LOCK gate checklist + amendment notes | GATE 2 checklist + LOCKED annotation + amendment notes | LOCK + SEAL gate checklists + amendment notes | Confirmation checklist + LOCKED + amendment notes |
| C-13: Status-quo as F-00 | Pass 2 F-00 + why-insufficient | Pass A F-00 + gap + observable test | 3A F-00 + why-insufficient | Pass 2 F-00 + why-insufficient | Step 3 F-00 + gap + observable test |
| C-14: Complete F-ID coverage | COVERAGE RULE enforcement note | COVERAGE RULE in prose | COVERAGE RULE in NAVIGATE | COVERAGE RULE enforcement note | COVERAGE CHECK before submit |
| C-15: Confidence post-lock | Confidence section after LOCK + consolidation | Confidence section after LOCK + consolidation | CONFIDENCE phase after SEAL | Confidence after LOCK + SEAL | Step 6 after Step 4 LOCKED |
| C-16: Multi-pass consolidation | Consolidation subsection + CONFIRMED | Prose Final list + CONFIRMED per item | CONSOLIDATE phase + SEAL gate | Archivist role + SEAL gate | Step 5 Final list + CONFIRMED column |

**Predicted composite scores (all 16 criteria):**
- V-01: 60 + 30 + 10 = **100** | Golden: YES
- V-02: 60 + 30 + 10 = **100** | Golden: YES
- V-03: 60 + 30 + 10 = **100** | Golden: YES
- V-04: 60 + 30 + 10 = **100** | Golden: YES
- V-05: 60 + 30 + 10 = **100** | Golden: YES

### Open research questions for R4

1. **C-16 compliance under pressure**: Does a named Archivist role (V-04) or named
   CONSOLIDATE phase (V-03) produce stronger C-16 compliance in degenerate runs (trivial
   topic, context pressure) compared to a Skeptic-embedded consolidation subsection (V-01,
   V-02) or numbered step (V-05)?

2. **C-05 under register variation**: Does V-05's plain-language confirmation checklist
   ("LOCKED. Your claim and conditions above cannot change from this point.") enforce
   no-goalpost-movement as reliably as V-01/V-04's formal "LOCK RULE" header? The structural
   freeze point is identical; the surface signal differs.

3. **Pass order effect on F-00 depth (C-13)**: Does V-01/V-04's domain-first pass order
   produce richer why-insufficient explanations than V-03/V-05's status-quo-first approach?
   Hypothesis: cleared domain conditions give the Skeptic more material to reference when
   assessing the gap, producing a more grounded INSUFFICIENT rationale.

4. **Format neutrality across C-14**: Does V-02's prose Navigator (coverage rule embedded
   in instructions before the numbered list) enforce F-ID coverage as reliably as V-01/V-03/
   V-04's tabular Navigator with an explicit coverage rule note at the top?
