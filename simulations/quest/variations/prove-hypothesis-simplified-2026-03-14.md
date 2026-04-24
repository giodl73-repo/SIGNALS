831 simplified vs 1149 original. Reduction: **27.7%** — within the 20-40% target.

---

## Simplification Report

**Word count:** 1149 → 831 (-318 words, -27.7%)

### What was removed

| Phrase | Why it was dead weight |
|---|---|
| "Establishes status-quo baseline and generates F-00 with current practice primed in context." | Meta-explanation of the section; the content does this |
| "What does the team do today?" (standalone) | Immediately repeated by the `Current practice:` field |
| "Be specific -- this is the practice your claim must exceed." | The observable-test constraint already enforces specificity |
| "Is current practice sufficient to deliver the value the claim will assert?" | The checkboxes express the judgment; the question is a restatement |
| "Do not write a claim for a value that status quo already delivers." | Already enforced by STOP on the SUFFICIENT branch |
| "Revise your framing before restarting." | Implicit from STOP |
| "No evidence references allowed here. No Skeptic verdicts, no consolidation output, no Navigator content in this section." | Those sections haven't been written yet; sequence is the enforcer |
| "(Skeptic will evaluate each for observability)" | SKEPTIC section + its opening line cover this |
| "Downstream sections have read-only access to DECLARE." | Restates the preamble LOCK GATE already declared above |
| "Claim and domain conditions above are now read-only." | Redundant with LOCKED; "above" is spatial noise |
| "Post-lock observability problems: log as amendment notes in NAVIGATOR. Do not edit here." | Stated in preamble; restated in NAVIGATOR amendment-notes field |
| "F-00 is established in CONTEXT -- Skeptic validates it below." | Made structurally obvious by `### F-00 Validation` |
| "Read-only access to DECLARE." (inside SKEPTIC) | Already in LOCK GATE |
| "Log problems as amendment notes; do not modify locked sections." | Already in preamble + LOCK GATE |
| "and invisible-state conditions" | Subset example, not a distinct rule |
| "A partial list -- missing any condition from either source -- is a structural failure." | Table footer enforcement note covers this |
| "Archivist role: collection and confirmation only." | Same as "No new conditions introduced here" |
| "Both are in effect -- do not revise conditions." (CONFIDENCE) | Gates are already established |
| "[LOCK GATE and SEAL GATE are in effect.]" (NAVIGATOR) | Redundant with established gates |
| "[Add rows until every F-ID from the Final Falsification List is covered.]" (NAVIGATOR) | COVERAGE RULE directly above says this |
| Parenthetical clarifiers on frontmatter fields | Field names are self-explanatory |

### Essential criteria: all PASS

| C-01 | C-02 | C-03 | C-04 | C-05 |
|---|---|---|---|---|
| YES | YES | YES | YES | YES |

Structural aspirationals preserved: dual-gate isolation (C-17), named ARCHIVIST section (C-18), CONTEXT before DECLARE (C-19), F-00 Validation subsection in SKEPTIC (C-20).

Output written to: `simulations/quest/variations/prove-hypothesis-simplified-2026-03-14.md`

```json
{"simplified_word_count": 831, "original_word_count": 1149, "all_essential_still_pass": true}
```
aims." |
| C-02 Falsification conditions | YES | F-01/F-02 table in DECLARE; "externally verifiable" constraint |
| C-03 Confidence 0-100 with rationale | YES | "Value: [N]/100" + Rationale with two required elements |
| C-04 Experiment list with sub-skills | YES | NAVIGATOR table: experiment, prove sub-skill, F-IDs, risk rationale |
| C-05 No goalpost movement | YES | LOCK GATE freezes claim+conditions before SKEPTIC; SEAL GATE before CONFIDENCE |

**All 5 essential criteria: PASS**

---

## Simplified Prompt Body

```
You are running /prove-hypothesis. Fill in this structured template.
Six sections execute in sequence: Context, Declare, Challenge, Consolidate, Confidence, Navigate.

LOCK GATE -- Scope: freezes Claim and domain Falsification Conditions after DECLARE.
SEAL GATE -- Scope: freezes Final Falsification List after CONSOLIDATE.
Post-lock problems are amendment notes only. No retroactive edits.

---

## CONTEXT: CURRENT STATE
[Complete before writing your claim. F-00 is generated here.]

Prior signals: [Search simulations/prove/ for prior hypothesis, analysis, or synthesis
on this topic. List files with one-line summaries, or write "None -- starting fresh."]

Current practice: [One sentence. What does the team do today without this capability?]

Status-quo judgment (explicit verdict required):
[ ] INSUFFICIENT: current practice leaves a gap.
    The gap: [One sentence. What specifically cannot be achieved?]
    F-00: This hypothesis is false if the team obtains equivalent value from current practice.
    F-00 observable test: [Externally measurable outcome indicating current practice is sufficient.]
[ ] SUFFICIENT: current practice satisfies the need. Stop. Revise framing before restarting.

---

## CLAIMANT: DECLARE
[Write after completing CONTEXT.]

Claim: [One sentence. Use "is" or "will". No hedging. No compound claims.]

Falsification conditions:
| ID   | Condition: hypothesis is false if this observable outcome occurs |
|------|------------------------------------------------------------------|
| F-01 | [Observable outcome] |
| F-02 | [Observable outcome] |
[Add F-03+ if needed. Each must be externally verifiable.]

Confirmation conditions:
| ID    | Condition: hypothesis is confirmed if this observable outcome occurs |
|-------|----------------------------------------------------------------------|
| CF-01 | [Positive confirmation criterion] |

### LOCK GATE
Scope: Freezes Claim and domain Falsification Conditions (F-01+). Downstream sections read-only.
- [ ] CONTEXT: F-00 candidate and observable test written (INSUFFICIENT path taken)
- [ ] Claim is one sentence with no hedging
- [ ] At least two domain conditions (F-01, F-02) present
- [ ] No Skeptic verdicts, consolidation output, or Navigator content here

LOCKED. Post-lock problems: log as amendment notes in NAVIGATOR.

---

## SKEPTIC: CHALLENGE
[Domain observability only. F-00 is from CONTEXT -- validate below.
Opinion-dependent conditions receive REWRITE verdict. Do not modify DECLARE.]

### Domain Conditions (F-01+)
| F-ID | Condition text (from DECLARE) | Skeptic verdict | Rewritten condition (if REWRITE) |
|------|-------------------------------|-----------------|----------------------------------|
| F-01 | [text from DECLARE] | PASS (observable: [how]) / REWRITE | [Issue + new condition text] |
| F-02 | [text from DECLARE] | PASS (observable: [how]) / REWRITE | [Issue + new condition text] |
[All F-IDs from DECLARE must appear. Silent omission is a coverage failure.]

### F-00 Validation
F-00 from CONTEXT: [restate condition and observable test]
Skeptic verdict: [ ] PASS -- observable via [method]
                 [ ] REWRITE -- issue: [what is wrong]. Revised: [new text]

### PRE-CONSOLIDATE CHECK
- [ ] Every domain F-ID from DECLARE has an explicit PASS or REWRITE verdict
- [ ] Every REWRITE has a complete replacement
- [ ] F-00 from CONTEXT has received an explicit verdict
- [ ] No modifications to CLAIMANT: DECLARE

Amendment notes: [F-NN: issue -- suggested rewrite. Write "None" if none.]

---

## ARCHIVIST: CONSOLIDATE
[Collect F-00 (from CONTEXT, Skeptic-validated) and cleared domain conditions
(from SKEPTIC) into one Final Falsification List. Every condition receives CONFIRMED.
F-00 first; F-01+ in order. No new conditions introduced.]

Final falsification list:
| ID   | Condition | Observable test | Verdict |
|------|-----------|-----------------|---------|
| F-00 | Status quo is sufficient | [from CONTEXT, Skeptic-validated] | CONFIRMED |
| F-01 | [Cleared condition] | [how observed] | CONFIRMED |
| F-02 | [Cleared condition] | [how observed] | CONFIRMED |
[All conditions from CONTEXT and SKEPTIC must appear. No F-ID absent.]

### SEAL GATE
Scope: Freezes Final Falsification List. Confidence and Navigator source only this list.
- [ ] F-00 present with CONFIRMED (from CONTEXT, Skeptic-validated)
- [ ] Every domain condition from SKEPTIC present with CONFIRMED
- [ ] No condition absent
- [ ] All observable tests populated

SEALED. Final Falsification List is the authoritative source for NAVIGATOR.

---

## CLAIMANT: CONFIDENCE
[Written after LOCK GATE and SEAL GATE.]

Value: [N]/100
Rationale: [2-3 sentences.
  (1) Why F-00 is INSUFFICIENT -- what gap does current practice leave? Reference CONTEXT gap.
  (2) Prior signal, trace finding, or friction point anchoring the number.
  If no prior signals: "No prior signals -- calibrated from CONTEXT gap: [reasoning]."
  Both elements required.]

---

## NAVIGATOR: EXPERIMENTS
[Source: ARCHIVIST Final Falsification List only. Rank 1 = highest falsification risk.
Valid sub-skills: prove:interview, prove:prototype, prove:analysis, prove:websearch,
prove:publish, prove:synthesize, prove:intelligence.
COVERAGE RULE: Every F-ID must appear in at least one row. Missing F-ID is explicit failure.]

| Rank | Experiment | prove sub-skill | F-IDs tested | Risk rationale |
|------|------------|-----------------|--------------|----------------|
| 1 | [Describe experiment] | prove:[sub-skill] | [F-00, F-01] | [Why highest risk] |
| 2 | [Describe experiment] | prove:[sub-skill] | [F-01, F-02] | [Why second] |
[Add rows until every F-ID is covered.]

Amendment notes (post-lock): [F-NN: issue -- suggested rewrite. Write "None" if none.]

---

Write artifact: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
Frontmatter: skill, topic, date, claim_summary, confidence, experiment_count,
             prior_signals_found (true/false), status_quo_verdict (INSUFFICIENT/SUFFICIENT),
             skeptic_rewrites (count), amendment_notes (count),
             f_id_count (total), f_id_coverage (true/false).
```
