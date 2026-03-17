Golden prompt written to `simulations/quest/golden/prove-hypothesis-golden-2026-03-14.md`.

**What's in it:**

- Frontmatter: score 100, status GOLDEN, rubric v5, 4 rounds
- Prompt body: the simplified variation (831 words, -27.7%) — canonical since simplification passed
- 5 patterns that made it golden:
  1. **F-00 born before the claim** — CONTEXT runs first, Skeptic validates rather than introduces (C-19/C-13)
  2. **Gate scope in headers** — both LOCK and SEAL headers carry explicit scope annotations (C-17/C-21)
  3. **Dedicated F-00 Validation subsection** — structurally isolated from F-01+ verdict list in SKEPTIC (C-20)
  4. **ARCHIVIST at peer heading level** — omission visible as missing section, not silent (C-18)
  5. **Preamble establishes gates once** — simplification removed all restatements; sequence is the enforcer
- Rubric v5 summary: 5/5 essential, 3/3 recommended, 13/13 aspirational
 does the team do today without this capability?]

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

---

## What Made It Golden

**1. F-00 born before the claim (C-19 + C-13)**
The CONTEXT section runs first and generates F-00 with status-quo framing live. The Skeptic
validates F-00 rather than introducing it. Every prior variation failed C-19 by generating
F-00 only during the adversarial pass -- retrospective gap analysis is weaker than gap
analysis written with current practice primed in context.

**2. Dual-gate scope labels in headers (C-17 + C-21)**
Both gates name their scope in the section header itself:
`LOCK GATE -- Scope: freezes Claim and domain Falsification Conditions after DECLARE`
`SEAL GATE -- Scope: freezes Final Falsification List after CONSOLIDATE`
Semantically distinct names alone (LOCK vs SEAL) were insufficient for C-21; the scope
annotation makes each gate self-documenting without reading the checklist body.

**3. Dedicated F-00 Validation subsection in SKEPTIC (C-20)**
The Skeptic section splits into `### Domain Conditions (F-01+)` and `### F-00 Validation`
as structurally separate subsections. F-00 adversarial logic (testing status-quo sufficiency)
is categorically different from domain condition observability checking. Treating F-00 in
the same verdict list as F-01+ conflates two distinct adversarial purposes.

**4. Named ARCHIVIST role at peer heading level (C-18)**
`## ARCHIVIST: CONSOLIDATE` appears at ## heading level alongside CONTEXT, CLAIMANT, SKEPTIC,
and NAVIGATOR. A consolidation step embedded as a subsection fails C-18 because omission is
silent. A named role at peer level makes omission visible as a missing section.

**5. Preamble gates establish rules once; sections enforce (simplification principle)**
The two gates are declared in the preamble with their scopes. All per-section restatements
of those rules were removed in simplification (27.7% reduction, 1149 -> 831 words). The
structural sequence is the enforcer -- sections written after LOCKED cannot retroactively
edit prior content. The simplified body retains all 5 essential + 3 recommended + 13
aspirational criteria at full score.

---

## Rubric v5 Summary

**Score: 100/100 | Golden: YES**

| Band | Weight | Criteria | Passed |
|------|--------|----------|--------|
| Essential | 60 pts | C-01 single claim, C-02 falsification conditions, C-03 confidence 0-100, C-04 experiment list, C-05 no goalpost movement | 5/5 |
| Recommended | 30 pts | C-06 prior signals note, C-07 confirmation conditions, C-08 evidence-backed rationale | 3/3 |
| Aspirational | 10 pts | C-09 experiment-to-F-ID mapping, C-10 risk-ranked with rationale, C-11 adversarial role gate, C-12 hard phase gate, C-13 status-quo as F-00, C-14 complete F-ID coverage, C-15 confidence post-lock, C-16 multi-pass consolidation, C-17 dual-gate isolation, C-18 named consolidation unit, C-19 inertia-lead framing, C-20 dedicated F-00 adversarial subsection, C-21 gate scope labeled in header | 13/13 |

**Threshold**: all 5 essential pass AND composite >= 80.

**Simplification**: 1149 -> 831 words (-27.7%). All criteria preserved. Simplified body is canonical.
