---
skill: quest-variate
skill_target: topic-story
date: 2026-03-15
round: 14
rubric: v13
---

# Variations — topic-story (Round 14)

Five complete, runnable skill body prompt variations.
Single-axis first (V-01 through V-03), then two combinations (V-04, V-05).

**Design context**: v13 rubric adds C-33 (Weight-Trigger Rule Citation in Decision Outputs) and
C-34 (Re-Sealing Protocol Weight-Trigger Compliance). From Round 13:

- V-01 achieves C-30 via weight-graded consistency rules. C-33 gap: the reconciliation
  conclusion says "naming which weight-trigger rule validates the consistency claim" — prose
  guidance only. An author can write "HIGH-weight CONFIRMS dominate, LOW-weight CONTRADICTS
  produce CONFLICT rows" without labeling the rule (e.g., "QUALIFIED/LOW rule"). The authority
  trace breaks at the rule-name link: weight level cited, rule label absent.
- V-02 achieves C-28 + C-29 + C-31 but has no reconciliation table; C-33 N/A.
- V-03 achieves C-28 via Marker Lock; no reconciliation table; C-33 N/A.
- V-04 achieves C-30 + C-31 on single-phase base. C-33 gap: same as V-01.
- V-05 achieves C-26 through C-32. C-33 gap: E-5 reconciliation conclusion is instructional
  ("naming the weight-trigger rule") not format-constrained. C-34 gap: re-sealing step b says
  "declare the revision with the weight-trigger rule that forced it" — instructional. An author
  who follows all steps can write "the new MEDIUM-weight CONTRADICTS means the CONFIRMED vector
  must become QUALIFIED" — all relevant content present, but no labeled rule field. Structurally
  correct; weight-trigger-blind at the format level.

**C-33 gap**: In every R13 variation with a reconciliation table, the conclusion is instructed
to name the weight-trigger rule but no FORMAT FIELD enforces this. A conclusion that writes
"the QUALIFIED vector is consistent because HIGH-weight CONFIRMS outweigh the LOW-weight
UNRESOLVED CONTRADICTS" names weight levels (C-30 compliant) but does not label the rule
("QUALIFIED/LOW rule: transfers to Beat 4 as a gap, no stance restriction"). Without a required
`Rule applied:` field, the conclusion can be weight-level-aware and rule-label-blind. Similarly,
Beat 4.5 Adjacent verb is instructed to name "the weight-trigger rule in that row" but without
a `Contestation rule:` format field an author can name the row and weight without the rule label.

**C-34 gap**: R13 V-05 re-sealing step b: "Apply the weight-level consistency rules to the
updated distribution. If the vector must change, declare the revision with the weight-trigger
rule that forced it." Instruction, not FORMAT. A re-sealing that correctly executes all E-steps
but renders the rule application as prose satisfies C-32 (all steps executed) but fails C-34
(no format-constrained Re-sealing Reconciliation Decision with labeled rule fields).

**Rule label scheme**: `{VECTOR}/{WEIGHT_LEVEL}` where VECTOR is the declared vector and
WEIGHT_LEVEL is the triggering weight level. Examples: QUALIFIED/HIGH, CONFIRMED/MEDIUM,
REVERSED/LOW-dominant, CONFIRMED/CLEAR (no unresolved CONTRADICTS). These labels correspond
directly to the named subsections of the weight-level consistency rules.

**Round 14 primary axes:**

V-01 targets C-33 single-axis on R13 V-01 base — adds `Rule applied:` as a required FORMAT
FIELD after the reconciliation table and `Contestation rule:` as a required element in Beat
4.5. C-31 NOT targeted (bare count stamp retained). C-34 N/A (no re-sealing protocol).

V-02 targets C-33 single-axis on R13 V-05 EVALUATOR/AUTHOR base — same C-33 additions applied
to the two-phase architecture. C-34 NOT targeted (re-sealing step b remains instructional).

V-03 targets C-34 single-axis on R13 V-05 base — upgrades re-sealing protocol step b to a
FORMAT-constrained `Re-sealing Reconciliation Decision` block with labeled rule fields.
C-33 NOT targeted (regular reconciliation conclusion remains instruction-based).

V-04 combines C-33 with R13 V-04 base (C-30+C-31 already present on single-phase) — tests
whether C-33's rule citation requirement interacts with C-31's stamp FORMAT specification.
C-34 is N/A (no re-sealing protocol in single-phase architecture).

V-05 is the full combination: C-33 + C-34 on R13 V-05 EVALUATOR/AUTHOR base, targeting
C-26 through C-34 simultaneously. Authority trace: E-3 inertia marker text -> E-5 weight
level derivation -> weight-level consistency rule -> `Rule applied: {VECTOR}/{WEIGHT_LEVEL}`
-> reconciliation conclusion -> Packet -> A-1 Beat 4.5 Recommendation verb (citing Rule
applied:) + `Contestation rule:`. Re-sealing path: new conflict -> E-5 -> `Re-sealing
Reconciliation Decision` block with `Rule re-executed:` + `Vector status:` + `Trigger:`.

---

## V-01

**Variation axis**: Output format -- rule-label citation as required FORMAT FIELD (C-33 target)
**Hypothesis**: C-33 fails when the reconciliation conclusion names weight levels without
labeling the specific rule triggered. R13 V-01 says "naming which weight-trigger rule validates
the consistency claim" -- prose guidance, not a format requirement. An author satisfies R13
V-01 by citing weight levels ("HIGH-weight CONFIRMS dominate") without labeling the rule
("QUALIFIED/LOW rule: transfers to Beat 4 as a gap, no stance restriction"). C-33 requires
`Rule applied: {VECTOR}/{WEIGHT_LEVEL} rule` as a required FORMAT FIELD before the
reconciliation sentence. Without this field, the authority trace breaks between weight level
and rule name. Similarly, Beat 4.5 Adjacent verb names a row and weight designation but
without a `Contestation rule:` field can omit the rule label entirely. This variation adds
both FORMAT FIELDS on the R13 V-01 base. C-31 is NOT targeted -- the closure stamp remains
a bare count record, isolating the C-33 axis. C-34 is N/A -- no re-sealing protocol present.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 -- Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### Step 2 -- Hypothesis mutation ledger

Before writing any story section, complete the ledger. Write it to the artifact as the
first section.

**Working hypothesis (S0)**: [one sentence -- the specific claim the team entered with,
stated as a falsifiable assertion, not a goal or question]

For each signal artifact, in the order read:

```
- `{artifact-name}`: {key finding most relevant to the working hypothesis, one to two sentences}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  Inertia marker: prior expectation: {what was believed before this signal arrived}
  [if MODIFIES]: Hypothesis update: [previous wording] -> [updated wording]
```

After all entries:

```
Hypothesis at S3: [one sentence -- working hypothesis after all stances applied]

Net mutation vector: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED
[one sentence: mechanism -- which stances, on which dimension, drove this; cite at least
one entry by artifact name]

Evidence trajectory: POINT-IN-TIME | DIRECTIONAL -- [explicit declaration]
```

**Anti-stagnation check**: If S3 is identical to S0, state why. Silently identical fails.

**Reconciliation check**: CONFIRMED with visible unresolved CONTRADICTS, or REVERSED with
no CONTRADICTS, must be revised before proceeding.

Do not begin story beats until the ledger is complete.

---

### Step 2b -- Vector-verdict reconciliation table

After declaring the vector, complete the reconciliation table. One row per ledger entry.

Derive an inertia weight from each entry's inertia marker text:
- **HIGH** -- the inertia marker names a firmly established belief, prior measurement, existing
  design commitment, or strong organizational assumption
- **MEDIUM** -- the inertia marker names a working assumption or expectation held with moderate
  confidence
- **LOW** -- the inertia marker names a weak prior, default assumption, or expectation held
  with acknowledged uncertainty

```
| Signal | Inertia weight | Verdict type | Consistent with declared vector? |
|--------|----------------|--------------|----------------------------------|
| {artifact-name} | HIGH -- "{prior expectation text}" | CONFIRMS | YES |
| {artifact-name} | MEDIUM -- "{prior expectation text}" | MODIFIES toward {dimension} | YES |
| {artifact-name} | HIGH -- "{prior expectation text}" | CONTRADICTS on {dimension} -- RESOLVED | YES (resolved) |
| {artifact-name} | HIGH -- "{prior expectation text}" | CONTRADICTS on {dimension} -- UNRESOLVED | CONFLICT |
```

**Weight-level consistency rules** -- weight level is the named trigger condition; each level
produces a distinct consequence. Rule labels follow the `{VECTOR}/{WEIGHT_LEVEL}` scheme:

**CONFIRMED**:
- CONFIRMED/HIGH: HIGH-weight CONTRADICTS UNRESOLVED -- CONFIRMED is invalid. The vector must
  become QUALIFIED or the conflict must be resolved. No path exists to maintain CONFIRMED while
  a HIGH-weight CONTRADICTS is unresolved.
- CONFIRMED/MEDIUM: MEDIUM-weight CONTRADICTS UNRESOLVED -- CONFIRMED is invalid. Must become
  QUALIFIED or resolve. Resolving the conflict before authoring begins restores CONFIRMED.
- CONFIRMED/LOW: LOW-weight CONTRADICTS UNRESOLVED -- CONFIRMED is permissible only when
  HIGH-weight CONFIRMS entries constitute >= 70% of all CONFIRMS-stance entries; otherwise
  revise to QUALIFIED.
- CONFIRMED/CLEAR: No unresolved CONTRADICTS -- CONFIRMED is valid; no additional constraint.

**QUALIFIED**:
- QUALIFIED/HIGH: HIGH-weight CONTRADICTS UNRESOLVED -- produces a CONFLICT row; QUALIFIED
  remains valid but PROCEED is blocked; PAUSE is the minimum permitted stance from the Band gate.
- QUALIFIED/MEDIUM: MEDIUM-weight CONTRADICTS UNRESOLVED -- produces a CONFLICT row; QUALIFIED
  remains valid; Band gate applies normally; no additional stance restriction.
- QUALIFIED/LOW: LOW-weight CONTRADICTS UNRESOLVED -- produces a CONFLICT row; QUALIFIED
  remains valid; no stance restriction; transfers to Beat 4 as a gap with no effect on stance.

**REVERSED**:
- REVERSED/HIGH-dominant: HIGH-weight CONTRADICTS constitute a majority of evidence weight --
  strongly grounded; no additional justification required.
- REVERSED/MEDIUM-dominant: MEDIUM-weight CONTRADICTS constitute a majority -- valid; name the
  specific dimension where reversal occurred.
- REVERSED/LOW-dominant: Predominantly LOW-weight CONTRADICTS -- must name the cumulative
  mechanism explicitly, or revise the vector to QUALIFIED.

**REDIRECTED**:
- REDIRECTED/ANY: Evidence answers a different evaluative frame than S0; weight distributes
  across dimensions. Weight-level grading does not apply to REDIRECTED.

After the table, write the rule citation block and reconciliation conclusion:

```
Rule applied: {VECTOR}/{WEIGHT_LEVEL} rule -- [the specific consequence this rule triggered
  for the declared vector. Use the label names from the rule table above: e.g., QUALIFIED/HIGH,
  CONFIRMED/LOW, REVERSED/MEDIUM-dominant, CONFIRMED/CLEAR. This field is required -- a
  conclusion written without the Rule applied: field fails C-33 even when the narrative
  sentence references weight levels.]
Reconciliation: Vector is consistent -- [one sentence: which decisive entries' weight levels
  triggered the named rule, and what the rule required. Must reference the Rule applied: label.]
  OR: Vector revised from [X] to [Y] -- [one sentence: the named rule forced revision because
  {weight level} {verdict type} at [{artifact-name}] triggered the rule's consequence].
```

**Rule label guidance**: A conclusion that writes "the weight evidence supports QUALIFIED"
names the vector but not the weight-level rule -- fails C-33. A conclusion that cites
"HIGH-weight CONFIRMS dominate" names a weight level but not the rule -- also fails. The
`Rule applied:` field must appear as a labeled field, not embedded only in the narrative
sentence.

Do not begin story beats until the ledger, vector, rule citation, and reconciliation are
complete.

---

### Step 3 -- Conflict Register

Open the Conflict Register (OPEN state).

For every pair of signal entries with opposing stances on the same dimension:

```
Conflict: `{signal-A}` vs `{signal-B}` -- [dimension]
Verdict: RESOLVED in favor of `{signal}` because [specific evidential reason -- name the
  inertia weight of the decisive entry]
     OR: UNRESOLVED because [what {namespace}/{skill} signal would resolve it]
```

Every verdict carries a because-clause. Any CONFLICT row from the reconciliation table must
appear here as a named entry.

**Prose prohibition**: Adjudication commitments belong in the Register with because-clauses,
not in narrative prose.

Close:

```
[REGISTER CLOSED -- {N} rows, {R} RESOLVED, {U} UNRESOLVED]
```

UNRESOLVED entries auto-transfer to Beat 4. Do not begin story beats until this stamp is
written.

---

### Step 4 -- Confidence Band Calculation

Count: S (CONFIRMS), N (total), U (UNRESOLVED in Register).

| Band   | Criteria                                          | Default stance        |
|--------|---------------------------------------------------|-----------------------|
| HIGH   | S/N >= 0.70 AND U = 0                             | Per pattern direction |
| MEDIUM | 0.50 <= S/N < 0.70 OR (S/N >= 0.50 AND U <= 2)   | PAUSE                 |
| LOW    | S/N < 0.50 OR U > 2                               | PAUSE or PIVOT        |

LOW band: PROCEED is prohibited -- no override can bypass this.

Permitted stances by band:
- HIGH: any stance allowed
- MEDIUM: any stance allowed -- non-default requires OVERRIDE
- LOW: PAUSE, PIVOT, or ABANDON only

**Additional constraint from weight-level rules**: If any HIGH-weight CONTRADICTS UNRESOLVED
exists (triggering the QUALIFIED/HIGH rule), PROCEED is blocked regardless of Band. The Band
gate minimum still applies; the weight-level block adds a further restriction.

MEDIUM band with non-default stance: write the OVERRIDE field before Beat 4.5:

```
OVERRIDE: {named rationale -- specific gap being accepted; why it does not change the
  stance from the band default. Must not restate the verb, restate the band, or use a vague
  qualifier. Must name a specific uncertainty and state why it is bounded.}
```

Write to artifact before Beat 4.5:

```
Confidence Band: HIGH | MEDIUM | LOW
Signals confirming: {S}/{N} ({pct}%)
Unresolved contradictions: {U}
Default stance: {default}
Selected stance: {verb}
[OVERRIDE: {named rationale}]  <- if non-default
```

---

### Step 5 -- Write the story beats

**Beat 1 -- What we set out to understand**
One to three sentences. Original question, S0 hypothesis, entering default.

**Beat 2 -- What each signal revealed** (draws from the ledger)
One editorial sentence beyond the finding -- what the finding means for the hypothesis,
framed against the inertia marker. The inertia weight informs how significant a surprise or
confirmation this signal represents. Two sentences maximum per signal.

**Beat 3 -- What the signals say together**
Open: "Across [N] signals, the hypothesis was [reconciled vector]."

**Anchor citation rule**: Every non-trivial Beat 3 claim cites its ledger entry inline:
`(anchored: {artifact-name}, {stance})`.

Draw conflict/verdict entries from the Register. Do not re-adjudicate in prose.

**Falsifiability gate**:

```
Falsifiability: [externally observable evidence -- in the world, market, or system under
  analysis -- that would falsify the pattern claim if found. Not a provenance check. A
  domain-facing prediction that could be wrong.]
```

**Beat 4 -- What remains uncertain**
RESOLVED verdicts are not gaps. UNRESOLVED verdicts auto-transfer from the Register.

```
Gap: [what is unknown]
Most exposed finding: [which ledger claim is most at risk without this]
Next signal: {namespace}/{skill} -- [expected finding type]
```

---

### Beat 3 Output Inventory

**Complete this section before opening Beat 4.5.**

Enumerate ALL Beat 3 outputs. Beat 4.5 reads from this inventory exclusively.

```
Beat 3 Output Inventory:

Pattern claims:
1. "[verbatim declarative sentence from Beat 3]" (anchored: {artifact-name}, {stance})
2. "[additional claims -- verbatim, one per distinct claim]" (anchored: ...)

Evidence anchors:
- {artifact-name} ({stance}): [one phrase -- role in pattern claim]
- ...

Adjudication commitments (RESOLVED verdicts from Register only):
- `{signal-A}` vs `{signal-B}`: RESOLVED in favor of `{signal}` -- [reason phrase]
[If none: "No adjudicated conflicts."]
```

Completeness check: count `(anchored: ...)` citations in Beat 3; the Evidence anchors list
must contain exactly that count.

Closure stamp:

```
[INVENTORY CLOSED -- {P} pattern claims, {A} evidence anchors, {C} adjudication commitments]
```

Do not open Beat 4.5 until this stamp is written.

**Inventory prohibition**: Beat 4.5 and Beat 5 may not introduce claims not in this inventory.

---

### Beat 4.5 -- Derivation chain

Six elements. Reads from the Beat 3 Output Inventory only.

```
Anchored claim: "[exact pattern claim from Inventory, verbatim with anchor]"
  (anchored: {artifact-name}, {stance})
Net vector: {CONFIRMED | QUALIFIED | REVERSED | REDIRECTED} -- [mechanism sentence from
  reconciliation table, copied verbatim -- must match reconciliation conclusion]
Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON} -- [one sentence: licensing --
  consistent with Band gate output and weight-level constraints including the Rule applied: field]
Adjacent verb: {ADJ-VERB} -- [one sentence: which specific reconciliation table row, and
  which inertia weight designation in that row, would have to differ for this adjacent verb
  to apply -- name the exact entry a reader preferring the adjacent verb must contest]
Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule -- [the specific rule that would need to
  produce a different consequence for the adjacent verb to become licensed. Must use the same
  label scheme as the Rule applied: field in the reconciliation conclusion. A contestation
  citing a row and weight without naming the rule label fails C-33.]
Conditions: [one of: CONTRADICTS count by weight / gap-closure cost / risk tolerance
  threshold / readiness signal distribution -- stated as a specific value, citing at least
  one named weight level from the reconciliation table]
```

**Contestation rule guidance**: Label must match the weight-level consistency rule table.
If the adjacent verb requires that QUALIFIED/HIGH not block PROCEED, the field reads:
`Contestation rule: QUALIFIED/HIGH rule -- the HIGH-weight CONTRADICTS UNRESOLVED consequence
(PROCEED blocked) would need to not apply for [ADJ-VERB] to be licensed.` Vague labels
("the weight rule") fail; rule labels without the consequence clause also fail.

**Conditions guidance**: Must name at least one weight level. "0 HIGH-weight CONTRADICTS
remaining unresolved" passes; "no remaining conflicts" fails (weight-blind).

Do not write Beat 5 until all six elements are internally consistent and derive exclusively
from the Inventory.

---

**Beat 5 -- Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon** -- must match Beat 4.5 verb and Band
gate output. One paragraph. Names what to do, under what conditions, with what scope. Does
not repeat the derivation chain.

---

**Voice**: Active, opinionated. Rule applied: reads as a formally labeled decision record;
the derivation chain reads as a decision frame with rule-traceable contestation points via
Contestation rule:; recommendation reads as a directive.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

**Working hypothesis (S0)**: [claim]

## Hypothesis Mutation Ledger
- `{artifact-name}`: {finding}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  Inertia marker: prior expectation: [belief]
  [Hypothesis update if MODIFIES]
...
**Hypothesis at S3**: [evolved claim]
**Net mutation vector**: {vector} -- [mechanism sentence]
**Evidence trajectory**: POINT-IN-TIME | DIRECTIONAL -- [declaration]

## Vector-Verdict Reconciliation
| Signal | Inertia weight | Verdict type | Consistent? |
|--------|----------------|--------------|-------------|
| {artifact-name} | HIGH -- "{prior expectation}" | CONFIRMS | YES |
...
**Rule applied**: {VECTOR}/{WEIGHT_LEVEL} rule -- [consequence triggered]
**Reconciliation**: [conclusion -- references Rule applied: label, cites decisive weight levels]

## Conflict Register
Conflict: `{A}` vs `{B}` -- [dimension]
Verdict: RESOLVED because [reason, names inertia weight] OR UNRESOLVED because [what]
...
[REGISTER CLOSED -- N rows, R RESOLVED, U UNRESOLVED]

## Confidence Band
Signals confirming: {S}/{N} ({pct}%)
Unresolved contradictions: {U}
Confidence Band: HIGH | MEDIUM | LOW
Default stance: {default}
Selected stance: {verb}
[OVERRIDE: {named rationale}]

## Story

### Beat 1 -- What we set out to understand
...

### Beat 2 -- What each signal revealed
...

### Beat 3 -- What the signals say together
Across [N] signals, the hypothesis was [reconciled vector].
[pattern -- anchored claims, conflict/verdict, falsifiability]

### Beat 4 -- What remains uncertain
Gap: ...

### Beat 3 Output Inventory
Pattern claims:
1. "[claim]" (anchored: ...)
Evidence anchors: ...
Adjudication commitments: ...
[INVENTORY CLOSED -- P claims, A anchors, C commitments]

### Beat 4.5 -- Derivation chain
Anchored claim: "[verbatim from Inventory]" (anchored: ...)
Net vector: {vector} -- [mechanism -- matches reconciliation]
Recommendation verb: {VERB} -- [licensing -- Band gate, weight constraint, Rule applied: cited]
Adjacent verb: {ADJ-VERB} -- [contestation -- reconciliation row and weight designation]
Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule -- [rule that must differ for ADJ-VERB]
Conditions: [weight-sensitive parameter -- specific value citing a named weight level]

### Beat 5 -- Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON** -- [directive -- no new reasoning]
```

---

## V-02

**Variation axis**: Role sequence -- rule-label citation as required FORMAT FIELD on
EVALUATOR/AUTHOR base (C-33 target)
**Hypothesis**: R13 V-05 achieves C-30 through C-32 but the reconciliation conclusion in E-5
is still instructional for rule citation. The same C-33 gap present in V-01 appears in the
EVALUATOR architecture: E-5's conclusion can cite weight levels without labeling the specific
rule. Additionally, Beat 4.5 (AUTHOR) names the weight-trigger rule in Adjacent verb as
guidance but not as a required format field. This variation applies the C-33 additions from
V-01 to the R13 V-05 EVALUATOR/AUTHOR base: adds `Rule applied:` to E-5, carries it into
the Packet template, and adds `Contestation rule:` to Beat 4.5. C-34 is NOT targeted: the
re-sealing step b remains instructional, isolating the C-33 axis.

---

You are running `/topic:story` for a topic. The topic name is provided.

This skill runs in two phases: **EVALUATOR** then **AUTHOR**. Do not begin AUTHOR until
EVALUATOR is complete and the Derivation Packet is sealed.

---

## EVALUATOR Phase

**Permitted**: Gathering artifacts. Extracting findings. Assigning stances and rationales.
Tracking hypothesis mutation. Computing the reconciliation table with inertia weights.
Adjudicating conflicts. Closing the Conflict Register. Synthesizing the cross-signal pattern.
Enumerating all pattern outputs into the Derivation Packet. Computing the Confidence Band and
writing the OVERRIDE field if required. Sealing the Packet.
**Forbidden**: Writing story prose (Beats 1-5). Narrative framing. Editorial voice.
Recommendation stance selection beyond what the Band gate determines.

---

### E-1 -- Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### E-2 -- Declare the working hypothesis (S0)

```
Working hypothesis (S0): [one sentence -- falsifiable assertion]
```

---

### E-3 -- Signal Extract with stance rationale and inertia marker

For each artifact, in gather order:

```
- `{artifact-name}`: {one sentence -- the single most important finding, stated as fact}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  Rationale: {one sentence -- the specific element of this signal that drove the stance}
  Inertia marker: prior expectation: {what was believed before this signal arrived}
  [if MODIFIES]: Hypothesis update: [previous wording] -> [updated wording]
```

Rules: one entry per artifact; every entry gets stance, rationale, and inertia marker; the
rationale names specific evidence; only MODIFIES entries get a hypothesis update line.

---

### E-4 -- Declare S3, net mutation vector, and evidence trajectory

```
Hypothesis at S3: [evolved claim]
Net mutation vector: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED -- [mechanism sentence;
  cite at least one entry by artifact name]
Evidence trajectory: POINT-IN-TIME | DIRECTIONAL -- [declaration]
```

Anti-stagnation check applies.

---

### E-5 -- Vector-verdict reconciliation table with weight-level triggers

One row per ledger entry. Derive an explicit inertia weight from each entry's inertia marker:
- **HIGH** -- firmly established belief, prior measurement, existing design commitment, or
  strong organizational assumption
- **MEDIUM** -- working assumption or expectation held with moderate confidence
- **LOW** -- weak prior, default assumption, or expectation held with acknowledged uncertainty

```
| Signal | Inertia weight | Verdict type | Consistent with declared vector? |
|--------|----------------|--------------|----------------------------------|
| {artifact-name} | HIGH -- "{inertia marker text}" | CONFIRMS | YES |
| {artifact-name} | MEDIUM -- "{inertia marker text}" | MODIFIES toward {dimension} | YES |
| {artifact-name} | HIGH -- "{inertia marker text}" | CONTRADICTS on {dimension} -- RESOLVED | YES (resolved) |
| {artifact-name} | HIGH -- "{inertia marker text}" | CONTRADICTS on {dimension} -- UNRESOLVED | CONFLICT |
```

**Weight-level consistency rules** -- weight level is the named trigger condition:

**CONFIRMED**:
- CONFIRMED/HIGH: HIGH-weight CONTRADICTS UNRESOLVED -- CONFIRMED invalid; must become QUALIFIED
  or resolve. No path to maintain CONFIRMED with a HIGH-weight CONTRADICTS unresolved.
- CONFIRMED/MEDIUM: MEDIUM-weight CONTRADICTS UNRESOLVED -- CONFIRMED invalid; must become
  QUALIFIED or resolve. Resolving before authoring begins restores CONFIRMED.
- CONFIRMED/LOW: LOW-weight CONTRADICTS UNRESOLVED -- CONFIRMED permissible only when
  HIGH-weight CONFIRMS >= 70% of all CONFIRMS entries; otherwise revise to QUALIFIED.
- CONFIRMED/CLEAR: No unresolved CONTRADICTS -- CONFIRMED valid; no constraint.

**QUALIFIED**:
- QUALIFIED/HIGH: HIGH-weight CONTRADICTS UNRESOLVED -- CONFLICT row; QUALIFIED valid; PROCEED
  blocked; PAUSE is minimum permitted stance.
- QUALIFIED/MEDIUM: MEDIUM-weight CONTRADICTS UNRESOLVED -- CONFLICT row; QUALIFIED valid;
  Band gate applies normally; no additional stance restriction.
- QUALIFIED/LOW: LOW-weight CONTRADICTS UNRESOLVED -- CONFLICT row; QUALIFIED valid; no
  stance restriction; transfers to Beat 4 as gap.

**REVERSED**:
- REVERSED/HIGH-dominant: HIGH-weight CONTRADICTS majority -- strongly grounded.
- REVERSED/MEDIUM-dominant: MEDIUM-weight CONTRADICTS majority -- valid; name the dimension.
- REVERSED/LOW-dominant: LOW-weight majority -- must name cumulative mechanism or revise to
  QUALIFIED.

**REDIRECTED**:
- REDIRECTED/ANY: Weight distributes across dimensions; grading does not apply.

After the table, write the rule citation block and reconciliation conclusion:

```
Rule applied: {VECTOR}/{WEIGHT_LEVEL} rule -- [the specific consequence this rule triggered.
  Use the label names from the rule table above. This field is required -- a conclusion without
  a Rule applied: field fails C-33 even when the narrative sentence references weight levels.]
Reconciliation: Vector is consistent -- [one sentence: which decisive entries' weight levels
  triggered the named rule, and what the rule required. Must reference the Rule applied: label.]
  OR: Vector revised from [X] to [Y] -- [one sentence: the named rule forced revision because
  {weight level} {verdict type} at [{artifact-name}] triggered the rule's consequence].
```

---

### E-6 -- Conflict Register

Open the Register (OPEN state).

For every stance conflict:

```
Conflict: `{signal-A}` vs `{signal-B}` -- [dimension]
Verdict: RESOLVED in favor of `{signal}` because [evidential reason -- name inertia weight
  of the decisive entry]
     OR: UNRESOLVED because [what {namespace}/{skill} would resolve it]
```

Every verdict carries a because-clause. Any CONFLICT row from the reconciliation table must
appear here.

Close:

```
[REGISTER CLOSED -- {N} rows, {R} RESOLVED, {U} UNRESOLVED]
```

---

### E-7 -- Pattern synthesis (raw)

Synthesize the cross-signal pattern. NOT story prose -- analytical product for the Packet.

Open: "Across [N] signals, the hypothesis was [vector]."
For each non-trivial claim: `(anchored: {artifact-name}, {stance})`.

```
Falsifiability: [externally observable domain evidence that would falsify the pattern claim]
```

---

### E-8 -- Confidence Band

Count: S (CONFIRMS), N (total), U (UNRESOLVED in Register).

| Band   | Criteria                              | Permitted stances               | Default     |
|--------|---------------------------------------|---------------------------------|-------------|
| HIGH   | S/N >= 0.70 AND U = 0                 | Any                             | Per pattern |
| MEDIUM | 0.50 <= S/N < 0.70 OR U <= 2          | Any; non-default needs OVERRIDE | PAUSE       |
| LOW    | S/N < 0.50 OR U > 2                   | PAUSE, PIVOT, ABANDON           | PAUSE/PIVOT |

LOW band: PROCEED is prohibited. No OVERRIDE can bypass this.
**Additional constraint**: Any HIGH-weight CONTRADICTS UNRESOLVED (QUALIFIED/HIGH rule) blocks
PROCEED regardless of Band.

MEDIUM non-default: OVERRIDE slot must name the specific gap being accepted and why it does
not change the stance. Must not restate verb, restate band, or use vague qualifier.

---

### E-9 -- Seal the Derivation Packet

Write the Derivation Packet. This is the complete and sole input to AUTHOR.

```
## Derivation Packet

### Signal Extract
[All ledger entries from E-3, verbatim]

### S3, Vector, and Trajectory
Hypothesis at S3: [verbatim from E-4]
Net mutation vector: {vector} -- [mechanism sentence, verbatim]
Evidence trajectory: POINT-IN-TIME | DIRECTIONAL -- [declaration]

### Vector-Verdict Reconciliation
[Reconciliation table from E-5, verbatim]
Rule applied: {VECTOR}/{WEIGHT_LEVEL} rule -- [consequence triggered, verbatim from E-5]
Reconciliation: [conclusion, verbatim from E-5]

### Pattern claims
1. "[claim]" (anchored: {artifact-name}, {stance})
2. ...

### Evidence anchors
- {artifact-name} ({stance}): [one phrase -- role in pattern claim]

### Adjudication commitments
- `{signal-A}` vs `{signal-B}`: RESOLVED in favor of `{signal}` -- [reason phrase]
[If none: "No adjudicated conflicts."]

### Confidence Band
Signals confirming: {S}/{N} ({pct}%)
Unresolved contradictions: {U}
Band: HIGH | MEDIUM | LOW
Default stance: {default}
Selected stance: {verb}
[OVERRIDE: {named rationale}]

### Falsifiability
[Verbatim from E-7]
```

Append the Packet seal. Three required fields: COUNT, IMMUTABLE, VALIDITY NOTICE. A seal
missing the IMMUTABLE field is not a valid seal.

```
[PACKET SEALED -- {P} pattern claims, {A} evidence anchors, {C} commitments,
  Band: {band}, Selected stance: {verb}
  IMMUTABLE -- no item in this Packet may be added, modified, or removed after this stamp.
  The Pattern claims, Evidence anchors, Adjudication commitments, Rule applied: field,
  Confidence Band, and OVERRIDE field (if present) are irrevocable derivation inputs.
  Beat 5 framing, AUTHOR prose, and recommendation preference are each prohibited as inputs
  to retroactive revision. A seal missing the IMMUTABLE field is structurally incomplete
  and not a valid seal. If a conflict surfaces during AUTHOR: activate the Mid-Draft Conflict
  Re-Sealing Protocol -- full EVALUATOR revisit required; no exception path.]
```

---

### Mid-Draft Conflict Re-Sealing Protocol

This protocol activates when AUTHOR discovers a signal conflict not in the Derivation Packet
during Beats 1-5. The protocol is mandatory -- no exception path exists, regardless of whether
the conflict appears minor.

**Step 1**: STOP authoring immediately. Silent prose absorption -- continuing to draft while
incorporating or reasoning around the conflict -- is prohibited.

**Step 2**: Return to EVALUATOR phase. Execute ALL of the following steps in sequence:

  a. **E-3 update**: Add the newly-surfaced conflict as a ledger entry (or update the existing
     entry if already present and the conflict was missed). Assign stance, rationale, inertia
     marker.

  b. **E-5 update**: Add or revise the corresponding row in the reconciliation table. Apply
     the weight-level consistency rules to the updated distribution. Write updated `Rule
     applied:` and `Reconciliation:` fields for the revised distribution.

  c. **E-6 update**: Add the conflict to the Conflict Register with verdict and because-clause.
     If the vector changed, verify all existing Register entries remain consistent.

  d. **E-7 update**: Revise the pattern synthesis if the new or revised entry changes any
     pattern claim, evidence anchor, or adjudication commitment.

  e. **E-8 update**: Recalculate the Confidence Band with updated S, N, U counts.

  f. **E-9 re-seal**: Write a new Derivation Packet incorporating all updates from a-e.
     Append a new PACKET SEALED stamp (all three required fields). The old Packet is superseded.

**Step 3**: Resume AUTHOR from the discovery point. All remaining AUTHOR beats derive from
the NEW Derivation Packet only.

---

## AUTHOR Phase

**Permitted**: Pattern derivation. Story prose. Conflict rendering. Recommendation.
Adjacent-verb contrast.
**Forbidden**: Re-reading signal artifacts. Introducing evidence or claims not in the Packet.
Revising the Packet. Absorbing mid-draft conflicts into prose without activating the Protocol.

---

### A-1 -- Write story beats from the Derivation Packet

**Beat 1 -- What we set out to understand**
One to three sentences. Original question, S0 from the Packet, entering default.

**Beat 2 -- What each signal revealed**
One editorial sentence per Packet Signal Extract entry -- what the finding means given its
stance and inertia marker. Two sentences maximum per signal.

**Beat 3 -- What the signals say together**
Open: "Across [N] signals, the hypothesis was [vector from Packet]."
Draw from the Packet's Pattern claims and Evidence anchors. Render conflict/verdict entries
from the Register (reference -- do not re-adjudicate). Close with the Packet's falsifiability
condition, copied verbatim.

If a new signal conflict surfaces during Beat 3: activate the Mid-Draft Conflict Re-Sealing
Protocol immediately.

**Beat 4 -- What remains uncertain**
UNRESOLVED Register entries transfer here as gaps.

```
Gap: [what is unknown]
Most exposed finding: [which Packet pattern claim is most at risk]
Next signal: {namespace}/{skill} -- [expected finding type]
```

**Beat 4.5 -- Derivation chain** (reads from Packet only)

Six elements:

```
Anchored claim: "[exact claim from Packet's Pattern claims, verbatim with anchor]"
  (anchored: {artifact-name}, {stance})
Net vector: {vector from Packet} -- [mechanism sentence, verbatim from Packet]
Recommendation verb: {verb from Packet's Selected stance} -- [one sentence: licensing --
  states what in the Packet's reconciliation table (citing the Packet's Rule applied: label
  by name) and Band gate authorizes this verb]
Adjacent verb: {adjacent verb} -- [one sentence: which specific row in the Packet's
  reconciliation table, and which inertia weight designation in that row, would have to
  differ for the adjacent verb to apply]
Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule -- [the specific rule from the Packet's
  rule table that would need to produce a different consequence for the adjacent verb to
  become licensed. Must use the same label scheme as the Packet's Rule applied: field.]
Conditions: [weight-sensitive parameter from Packet -- specific value citing at least one
  inertia-weight designation from the reconciliation table]
```

**Beat 5 -- Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon** -- must match Packet's Selected stance.
One paragraph. Names accepted uncertainty if OVERRIDE present. No new evidence or reasoning.

---

**Voice**: The Packet reads as an engineering specification with irrevocable seal; Rule applied:
reads as a formally labeled decision record where the specific rule is named; the derivation
chain reads as a decision frame with rule-labeled contestation points; recommendation reads as
a directive.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

## Derivation Packet

### Signal Extract
- `{artifact-name}`: {finding}
  Stance: ...
  Rationale: ...
  Inertia marker: prior expectation: [belief]
...

### S3, Vector, and Trajectory
Hypothesis at S3: [claim]
Net mutation vector: {vector} -- [mechanism]
Evidence trajectory: POINT-IN-TIME | DIRECTIONAL -- [sentence]

### Vector-Verdict Reconciliation
| Signal | Inertia weight | Verdict type | Consistent? |
...
Rule applied: {VECTOR}/{WEIGHT_LEVEL} rule -- [consequence triggered]
Reconciliation: [conclusion -- references Rule applied: label]

### Pattern claims / Evidence anchors / Adjudication commitments / Confidence Band /
### Falsifiability
[verbatim from E-steps]

[PACKET SEALED -- P claims, A anchors, C commitments, Band: {band}, Stance: {verb}
  IMMUTABLE -- irrevocable. A stamp missing this IMMUTABLE clause is not a valid seal.
  If conflict surfaces in AUTHOR: activate Mid-Draft Conflict Re-Sealing Protocol.]

## Story
### Beat 1-4 ...

### Beat 4.5 -- Derivation chain
Anchored claim: "[from Packet]" (anchored: ...)
Net vector: {vector} -- [mechanism verbatim]
Recommendation verb: {VERB} -- [licensing -- cites Packet Rule applied: label and Band]
Adjacent verb: {ADJ-VERB} -- [contestation -- row and weight designation]
Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule -- [rule that must differ for ADJ-VERB]
Conditions: [weight-sensitive value with inertia weight]

### Beat 5 -- Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON** -- [directive]
```

---

## V-03

**Variation axis**: Lifecycle emphasis -- FORMAT-constrained Re-sealing Reconciliation
Decision (C-34 target)
**Hypothesis**: C-34 PARTIAL arises when the re-sealing protocol step b instructs "apply the
weight-level consistency rules and declare the revision with the weight-trigger rule that
forced it" without requiring a FORMAT-constrained output. R13 V-05's re-sealing step b is
exactly this. An author who follows all steps correctly can write "the newly-added MEDIUM-weight
CONTRADICTS means the CONFIRMED vector must become QUALIFIED" -- all relevant content present,
but no labeled field. C-34 requires a `Re-sealing Reconciliation Decision` FORMAT BLOCK with
three required sub-fields: `Rule re-executed:` (rule label applied), `Vector status:`
(UNCHANGED or REVISED), and `Trigger:` (required only when REVISED -- names the artifact,
weight level, verdict type, and specific rule consequence triggered). Without this block, a
re-sealing can be C-32-compliant (all steps executed) while being C-34-non-compliant (weight-
trigger re-evaluation rendered in prose). C-33 is NOT targeted -- E-5's regular reconciliation
conclusion and Beat 4.5 Adjacent verb remain instruction-based, isolating the C-34 axis.

---

You are running `/topic:story` for a topic. The topic name is provided.

This skill runs in two phases: **EVALUATOR** then **AUTHOR**. Do not begin AUTHOR until
EVALUATOR is complete and the Derivation Packet is sealed.

---

## EVALUATOR Phase

**Permitted**: Gathering artifacts. Extracting findings. Assigning stances and rationales.
Tracking hypothesis mutation. Computing the reconciliation table with inertia weights.
Adjudicating conflicts. Closing the Conflict Register. Synthesizing the cross-signal pattern.
Enumerating all pattern outputs into the Derivation Packet. Computing the Confidence Band and
writing the OVERRIDE field if required. Sealing the Packet.
**Forbidden**: Writing story prose (Beats 1-5). Narrative framing. Editorial voice.
Recommendation stance selection beyond what the Band gate determines.

---

### E-1 -- Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### E-2 -- Declare the working hypothesis (S0)

```
Working hypothesis (S0): [one sentence -- falsifiable assertion]
```

---

### E-3 -- Signal Extract with stance rationale and inertia marker

For each artifact, in gather order:

```
- `{artifact-name}`: {one sentence -- the single most important finding, stated as fact}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  Rationale: {one sentence -- the specific element that drove the stance}
  Inertia marker: prior expectation: {what was believed before this signal arrived}
  [if MODIFIES]: Hypothesis update: [previous wording] -> [updated wording]
```

---

### E-4 -- Declare S3, net mutation vector, and evidence trajectory

```
Hypothesis at S3: [evolved claim]
Net mutation vector: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED -- [mechanism sentence]
Evidence trajectory: POINT-IN-TIME | DIRECTIONAL -- [declaration]
```

Anti-stagnation check applies.

---

### E-5 -- Vector-verdict reconciliation table with weight-level triggers

One row per ledger entry.

Inertia weight derivation:
- **HIGH** -- firmly established belief, prior measurement, existing design commitment, or
  strong organizational assumption
- **MEDIUM** -- working assumption held with moderate confidence
- **LOW** -- weak prior or expectation held with acknowledged uncertainty

```
| Signal | Inertia weight | Verdict type | Consistent with declared vector? |
|--------|----------------|--------------|----------------------------------|
| {artifact-name} | HIGH -- "{inertia marker text}" | CONFIRMS | YES |
| {artifact-name} | MEDIUM -- "{inertia marker text}" | MODIFIES toward {dimension} | YES |
| {artifact-name} | HIGH -- "{inertia marker text}" | CONTRADICTS on {dimension} -- RESOLVED | YES (resolved) |
| {artifact-name} | HIGH -- "{inertia marker text}" | CONTRADICTS on {dimension} -- UNRESOLVED | CONFLICT |
```

**Weight-level consistency rules** -- weight level is the named trigger condition:

**CONFIRMED**:
- HIGH-weight CONTRADICTS UNRESOLVED: CONFIRMED invalid; must become QUALIFIED or resolve.
- MEDIUM-weight CONTRADICTS UNRESOLVED: CONFIRMED invalid; must become QUALIFIED or resolve.
- LOW-weight CONTRADICTS UNRESOLVED: CONFIRMED permissible only when HIGH-weight CONFIRMS
  >= 70% of all CONFIRMS entries; otherwise revise to QUALIFIED.

**QUALIFIED**:
- HIGH-weight CONTRADICTS UNRESOLVED: CONFLICT row; QUALIFIED valid; PROCEED blocked; PAUSE
  is minimum permitted stance.
- MEDIUM-weight CONTRADICTS UNRESOLVED: CONFLICT row; QUALIFIED valid; Band gate applies
  normally; no additional stance restriction.
- LOW-weight CONTRADICTS UNRESOLVED: CONFLICT row; QUALIFIED valid; no stance restriction;
  transfers to Beat 4 as gap.

**REVERSED**:
- Requires HIGH-weight or MEDIUM-weight CONTRADICTS majority. LOW-weight dominant REVERSED
  must name cumulative mechanism or revise to QUALIFIED.

**REDIRECTED**:
- Weight distributes across dimensions; grading does not apply.

After the table:

```
Reconciliation: Vector is consistent -- [one sentence naming the weight-trigger rule that
  validates the consistency claim and citing the decisive entries' weight levels].
  OR: Vector revised from [X] to [Y] -- [one sentence: which weight level, at which verdict,
  triggered the rule that forced revision].
```

---

### E-6 -- Conflict Register

Open the Register (OPEN state).

For every stance conflict:

```
Conflict: `{signal-A}` vs `{signal-B}` -- [dimension]
Verdict: RESOLVED in favor of `{signal}` because [evidential reason -- name inertia weight]
     OR: UNRESOLVED because [what {namespace}/{skill} would resolve it]
```

Close:

```
[REGISTER CLOSED -- {N} rows, {R} RESOLVED, {U} UNRESOLVED]
```

---

### E-7 -- Pattern synthesis (raw)

NOT story prose -- analytical product for the Packet.

Open: "Across [N] signals, the hypothesis was [vector]."
For each non-trivial claim: `(anchored: {artifact-name}, {stance})`.

```
Falsifiability: [externally observable domain evidence that would falsify the pattern claim]
```

---

### E-8 -- Confidence Band

| Band   | Criteria                              | Permitted stances               | Default     |
|--------|---------------------------------------|---------------------------------|-------------|
| HIGH   | S/N >= 0.70 AND U = 0                 | Any                             | Per pattern |
| MEDIUM | 0.50 <= S/N < 0.70 OR U <= 2          | Any; non-default needs OVERRIDE | PAUSE       |
| LOW    | S/N < 0.50 OR U > 2                   | PAUSE, PIVOT, ABANDON           | PAUSE/PIVOT |

LOW band: PROCEED prohibited. No OVERRIDE can bypass this.
Any HIGH-weight CONTRADICTS UNRESOLVED blocks PROCEED regardless of Band.

---

### E-9 -- Seal the Derivation Packet

Write the Derivation Packet. This is the complete and sole input to AUTHOR.

```
## Derivation Packet

### Signal Extract
[All ledger entries from E-3, verbatim]

### S3, Vector, and Trajectory
Hypothesis at S3: [verbatim]
Net mutation vector: {vector} -- [mechanism, verbatim]
Evidence trajectory: POINT-IN-TIME | DIRECTIONAL -- [declaration]

### Vector-Verdict Reconciliation
[Table from E-5, verbatim]
Reconciliation: [conclusion, verbatim from E-5]

### Pattern claims
1. "[claim]" (anchored: {artifact-name}, {stance})

### Evidence anchors
- {artifact-name} ({stance}): [role]

### Adjudication commitments
[RESOLVED verdicts from Register, or "No adjudicated conflicts."]

### Confidence Band
Signals confirming: {S}/{N} ({pct}%)
Unresolved contradictions: {U}
Band: HIGH | MEDIUM | LOW
Default stance: {default}
Selected stance: {verb}
[OVERRIDE: {named rationale}]

### Falsifiability
[Verbatim from E-7]
```

Append the Packet seal. Three required fields: COUNT, IMMUTABLE, VALIDITY NOTICE.

```
[PACKET SEALED -- {P} pattern claims, {A} evidence anchors, {C} commitments,
  Band: {band}, Selected stance: {verb}
  IMMUTABLE -- no item in this Packet may be added, modified, or removed after this stamp.
  Pattern claims, Evidence anchors, Adjudication commitments, Confidence Band, and OVERRIDE
  field are irrevocable. A seal missing the IMMUTABLE field is structurally incomplete and
  not a valid seal. If a conflict surfaces during AUTHOR: activate the Mid-Draft Conflict
  Re-Sealing Protocol -- full EVALUATOR revisit required; no exception path.]
```

---

### Mid-Draft Conflict Re-Sealing Protocol

This protocol activates when AUTHOR discovers a signal conflict not in the Derivation Packet
during Beats 1-5. The protocol is mandatory -- no exception path exists, regardless of whether
the conflict appears minor.

**Step 1**: STOP authoring immediately. Silent prose absorption -- continuing to draft while
incorporating or reasoning around the conflict -- is prohibited.

**Step 2**: Return to EVALUATOR phase. Execute ALL of the following steps in sequence:

  a. **E-3 update**: Add the newly-surfaced conflict as a ledger entry (or update the existing
     entry if already present and the conflict was missed). Assign stance, rationale, and
     inertia marker.

  b. **E-5 update**: Add or revise the corresponding row in the reconciliation table.
     Re-execute the weight-level consistency rules against the updated row distribution.
     Immediately after the updated table row, write the Re-sealing Reconciliation Decision
     as a required FORMAT BLOCK:

     ```
     Re-sealing Reconciliation Decision:
       Rule re-executed: {VECTOR}/{WEIGHT_LEVEL} rule -- [the specific consistency rule
         applied to the updated distribution. Use label format: e.g., QUALIFIED/HIGH,
         CONFIRMED/MEDIUM, REVERSED/LOW-dominant, CONFIRMED/CLEAR. Required regardless
         of whether the vector changed.]
       Vector status: UNCHANGED | REVISED from {OLD} to {NEW}
       [If REVISED]: Trigger: {artifact-name} ({weight level}, {verdict type}) triggered
         the {VECTOR}/{WEIGHT_LEVEL} rule -- consequence: [the specific consequence stated
         in the rule: e.g., "PROCEED blocked; PAUSE is the minimum permitted stance from
         the Band gate" or "CONFIRMED invalid; must become QUALIFIED or resolve the conflict".]
     ```

     A re-sealing that applies the weight-level consistency rules but renders the result in
     prose -- "the new MEDIUM-weight CONTRADICTS means the vector must become QUALIFIED" --
     satisfies C-32 but fails C-34. The `Rule re-executed:` and `Vector status:` sub-fields
     are always required. The `Trigger:` sub-field is required only when Vector status is
     REVISED.

  c. **E-6 update**: Add the conflict to the Conflict Register with verdict and because-clause.
     If the vector changed, verify all existing Register entries remain consistent.

  d. **E-7 update**: Revise the pattern synthesis if any pattern claim, evidence anchor, or
     adjudication commitment changes.

  e. **E-8 update**: Recalculate the Confidence Band with updated S, N, U counts.

  f. **E-9 re-seal**: Write a new Derivation Packet incorporating all updates from a-e.
     Append a new PACKET SEALED stamp (all three required fields). The old Packet is
     superseded; the new Packet is the authoritative derivation input.

**Step 3**: Resume AUTHOR from the discovery point. All remaining AUTHOR beats derive from
the NEW Derivation Packet only. The old Packet may not be referenced.

---

## AUTHOR Phase

**Permitted**: Pattern derivation. Story prose. Conflict rendering. Recommendation.
Adjacent-verb contrast.
**Forbidden**: Re-reading signal artifacts. Introducing evidence or claims not in the Packet.
Revising the Packet. Absorbing mid-draft conflicts into prose without activating the Protocol.

---

### A-1 -- Write story beats from the Derivation Packet

**Beat 1 -- What we set out to understand**
One to three sentences. Original question, S0 from the Packet, entering default.

**Beat 2 -- What each signal revealed**
One editorial sentence per Packet Signal Extract entry. Two sentences maximum per signal.

**Beat 3 -- What the signals say together**
Open: "Across [N] signals, the hypothesis was [vector from Packet]."
Draw from Packet's Pattern claims and Evidence anchors. Render conflict/verdict entries from
the Register. Close with the Packet's falsifiability condition, copied verbatim.

If a new signal conflict surfaces during Beat 3: activate the Mid-Draft Conflict Re-Sealing
Protocol immediately.

**Beat 4 -- What remains uncertain**

```
Gap: [what is unknown]
Most exposed finding: [which Packet pattern claim is most at risk]
Next signal: {namespace}/{skill} -- [expected finding type]
```

**Beat 4.5 -- Derivation chain** (reads from Packet only)

Five elements:

```
Anchored claim: "[exact claim from Packet's Pattern claims, verbatim with anchor]"
  (anchored: {artifact-name}, {stance})
Net vector: {vector from Packet} -- [mechanism sentence, verbatim from Packet]
Recommendation verb: {verb from Packet's Selected stance} -- [one sentence: licensing --
  states what in the Packet's reconciliation table and Band gate authorizes this verb]
Adjacent verb: {adjacent verb} -- [one sentence: which specific row in the Packet's
  reconciliation table, and which inertia weight designation and weight-trigger rule in
  that row, would have to differ for the adjacent verb to apply]
Conditions: [weight-sensitive parameter from Packet -- specific value citing at least one
  inertia-weight designation from the reconciliation table]
```

**Beat 5 -- Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon** -- must match Packet's Selected stance.
One paragraph. Names accepted uncertainty if OVERRIDE present. No new evidence or reasoning.

---

**Voice**: The Packet reads as an engineering specification with irrevocable seal; the
Re-Sealing Protocol reads as a mandatory procedure with a format-constrained Re-sealing
Reconciliation Decision block that closes the weight-blind re-evaluation gap; story beats
read as editorial narrative; recommendation reads as a directive.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

## Derivation Packet
[Signal Extract / S3 Vector Trajectory / Vector-Verdict Reconciliation with Reconciliation
conclusion / Pattern claims / Evidence anchors / Adjudication commitments / Confidence Band /
Falsifiability -- all verbatim from E-steps]

[PACKET SEALED -- P claims, A anchors, C commitments, Band: {band}, Stance: {verb}
  IMMUTABLE -- irrevocable. Not a valid seal without IMMUTABLE clause. If conflict surfaces
  in AUTHOR: activate Mid-Draft Conflict Re-Sealing Protocol -- Re-sealing Reconciliation
  Decision block required at E-5 step b.]

## Story
### Beat 1-4 ...

### Beat 4.5 -- Derivation chain
Anchored claim: "[from Packet]" (anchored: ...)
Net vector: {vector} -- [mechanism verbatim]
Recommendation verb: {VERB} -- [licensing]
Adjacent verb: {ADJ-VERB} -- [contestation -- row, weight, weight-trigger rule]
Conditions: [weight-sensitive value]

### Beat 5 -- Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON** -- [directive]
```

---

## V-04

**Variation axis**: Combination -- C-33 (rule-label citation) on R13 V-04 base (C-30+C-31
already present on single-phase)
**Hypothesis**: R13 V-04 achieves C-30 (weight-graded consistency rules) and C-31 (stamp
FORMAT SPECIFICATION with named required IMMUTABLE field) on the minimal single-phase
architecture. The C-33 gap is present: the reconciliation conclusion cites weight levels and
is instructed to name the rule, but no `Rule applied:` FORMAT FIELD enforces the label. This
variation adds C-33 to R13 V-04, testing whether the rule citation requirement interacts with
C-31's stamp FORMAT specification. The prediction: they are independent -- C-33 operates at
the reconciliation table step (Step 2b); C-31 operates at the inventory closure step (Beat 3
Output Inventory); they address different structural positions and do not constrain each other.
If the combination achieves C-30, C-31, and C-33 PASS simultaneously without interference,
this architecture is the minimum single-phase design satisfying all three criteria. C-34 is
N/A (no re-sealing protocol in single-phase architecture).

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 -- Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### Step 2 -- Hypothesis mutation ledger

**Working hypothesis (S0)**: [one sentence -- falsifiable assertion, not a goal]

For each signal artifact, in the order read:

```
- `{artifact-name}`: {key finding most relevant to the working hypothesis, one to two sentences}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  Inertia marker: prior expectation: {what was believed before this signal arrived}
  [if MODIFIES]: Hypothesis update: [previous wording] -> [updated wording]
```

After all entries:

```
Hypothesis at S3: [evolved claim]
Net mutation vector: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED -- [mechanism sentence;
  cite at least one entry by artifact name]
Evidence trajectory: POINT-IN-TIME | DIRECTIONAL -- [declaration]
```

Anti-stagnation check and reconciliation check apply.

Do not begin story beats until the ledger is complete.

---

### Step 2b -- Vector-verdict reconciliation table

After declaring the vector, complete the reconciliation table. One row per ledger entry.

Derive an inertia weight from each entry's inertia marker text:
- **HIGH** -- firmly established belief, prior measurement, existing design commitment, or
  strong organizational assumption
- **MEDIUM** -- working assumption held with moderate confidence
- **LOW** -- weak prior or expectation held with acknowledged uncertainty

```
| Signal | Inertia weight | Verdict type | Consistent with declared vector? |
|--------|----------------|--------------|----------------------------------|
| {artifact-name} | HIGH -- "{prior expectation text}" | CONFIRMS | YES |
| {artifact-name} | MEDIUM -- "{prior expectation text}" | MODIFIES toward {dimension} | YES |
| {artifact-name} | HIGH -- "{prior expectation text}" | CONTRADICTS on {dimension} -- RESOLVED | YES (resolved) |
| {artifact-name} | HIGH -- "{prior expectation text}" | CONTRADICTS on {dimension} -- UNRESOLVED | CONFLICT |
```

**Weight-level consistency rules** -- weight level is the named trigger condition:

**CONFIRMED**:
- CONFIRMED/HIGH: HIGH-weight CONTRADICTS UNRESOLVED -- CONFIRMED invalid; must become QUALIFIED
  or resolve. No path to maintain CONFIRMED with a HIGH-weight CONTRADICTS unresolved.
- CONFIRMED/MEDIUM: MEDIUM-weight CONTRADICTS UNRESOLVED -- CONFIRMED invalid; must become
  QUALIFIED or resolve.
- CONFIRMED/LOW: LOW-weight CONTRADICTS UNRESOLVED -- CONFIRMED permissible only when
  HIGH-weight CONFIRMS >= 70% of all CONFIRMS entries; otherwise revise to QUALIFIED.
- CONFIRMED/CLEAR: No unresolved CONTRADICTS -- CONFIRMED valid; no constraint.

**QUALIFIED**:
- QUALIFIED/HIGH: HIGH-weight CONTRADICTS UNRESOLVED -- CONFLICT row; QUALIFIED valid; PROCEED
  blocked; PAUSE is minimum permitted stance from Band gate.
- QUALIFIED/MEDIUM: MEDIUM-weight CONTRADICTS UNRESOLVED -- CONFLICT row; QUALIFIED valid;
  Band gate applies normally; no additional stance restriction.
- QUALIFIED/LOW: LOW-weight CONTRADICTS UNRESOLVED -- CONFLICT row; QUALIFIED valid; no
  stance restriction; transfers to Beat 4 as gap.

**REVERSED**:
- REVERSED/HIGH-dominant: HIGH-weight CONTRADICTS majority -- strongly grounded.
- REVERSED/MEDIUM-dominant: MEDIUM-weight CONTRADICTS majority -- valid; name the dimension.
- REVERSED/LOW-dominant: Predominantly LOW-weight -- must name cumulative mechanism or revise
  to QUALIFIED.

**REDIRECTED**:
- REDIRECTED/ANY: Weight distributes across dimensions; grading does not apply.

After the table, write the rule citation block and reconciliation conclusion:

```
Rule applied: {VECTOR}/{WEIGHT_LEVEL} rule -- [the specific consequence this rule triggered.
  Use the label names above: e.g., QUALIFIED/HIGH, CONFIRMED/LOW, CONFIRMED/CLEAR.]
Reconciliation: Vector is consistent -- [one sentence: which decisive entries' weight levels
  triggered the named rule, and what the rule required. Must reference the Rule applied: label.]
  OR: Vector revised from [X] to [Y] -- [one sentence: the named rule forced revision because
  {weight level} {verdict type} at [{artifact-name}] triggered the rule's consequence].
```

Do not begin story beats until the ledger, vector, rule citation, and reconciliation are
complete.

---

### Step 3 -- Conflict Register

Open the Register (OPEN state).

For every stance conflict:

```
Conflict: `{signal-A}` vs `{signal-B}` -- [dimension]
Verdict: RESOLVED in favor of `{signal}` because [evidential reason -- name inertia weight]
     OR: UNRESOLVED because [what {namespace}/{skill} would resolve it]
```

Every verdict carries a because-clause. Any CONFLICT row from the reconciliation table must
appear here.

**Prose prohibition**: Adjudication commitments belong in the Register, not in narrative prose.

Close:

```
[REGISTER CLOSED -- {N} rows, {R} RESOLVED, {U} UNRESOLVED]
```

UNRESOLVED entries auto-transfer to Beat 4. Do not begin story beats until this stamp is
written.

---

### Step 4 -- Confidence Band Calculation

| Band   | Criteria                                          | Default stance        |
|--------|---------------------------------------------------|-----------------------|
| HIGH   | S/N >= 0.70 AND U = 0                             | Per pattern direction |
| MEDIUM | 0.50 <= S/N < 0.70 OR (S/N >= 0.50 AND U <= 2)   | PAUSE                 |
| LOW    | S/N < 0.50 OR U > 2                               | PAUSE or PIVOT        |

LOW band: PROCEED is prohibited.
**Additional constraint**: Any HIGH-weight CONTRADICTS UNRESOLVED (QUALIFIED/HIGH rule) blocks
PROCEED regardless of Band.

MEDIUM non-default requires OVERRIDE:

```
OVERRIDE: {named rationale -- specific gap being accepted; why it does not change the stance.
  Must not restate verb, restate band, or use vague qualifier.}
```

Write to artifact before Beat 4.5:

```
Confidence Band: HIGH | MEDIUM | LOW
Signals confirming: {S}/{N} ({pct}%)
Unresolved contradictions: {U}
Default stance: {default}
Selected stance: {verb}
[OVERRIDE: {named rationale}]
```

---

### Step 5 -- Write the story beats

**Beat 1 -- What we set out to understand**
One to three sentences. Original question, S0 hypothesis, entering default.

**Beat 2 -- What each signal revealed** (draws from ledger)
One editorial sentence per entry -- what the finding means for the hypothesis, framed against
the inertia marker. Weight level informs significance. Two sentences maximum.

**Beat 3 -- What the signals say together**
Open: "Across [N] signals, the hypothesis was [reconciled vector]."

**Anchor citation rule**: Every non-trivial Beat 3 claim cites its ledger entry:
`(anchored: {artifact-name}, {stance})`.

Draw conflict/verdict entries from the Register. Do not re-adjudicate in prose.

```
Falsifiability: [domain-facing prediction that would falsify the pattern claim]
```

**Beat 4 -- What remains uncertain**

```
Gap: [what is unknown]
Most exposed finding: [which ledger claim is most at risk]
Next signal: {namespace}/{skill} -- [expected finding type]
```

---

### Beat 3 Output Inventory

**Complete this section before opening Beat 4.5.**

```
Beat 3 Output Inventory:

Pattern claims:
1. "[verbatim declarative sentence from Beat 3]" (anchored: {artifact-name}, {stance})
2. "[additional claims -- verbatim]" (anchored: ...)

Evidence anchors:
- {artifact-name} ({stance}): [one phrase -- role in pattern claim]
- ...

Adjudication commitments (RESOLVED verdicts from Register only):
- `{signal-A}` vs `{signal-B}`: RESOLVED in favor of `{signal}` -- [reason phrase]
[If none: "No adjudicated conflicts."]
```

Completeness check: count `(anchored: ...)` citations in Beat 3; Evidence anchors must
contain exactly that count.

**Inventory closure stamp -- FORMAT SPECIFICATION**

The closure stamp has three required fields. A stamp is structurally complete only when all
three fields are present. A stamp containing Field 1 but missing Field 2 is not a valid seal.

```
Stamp field definitions:

  Field 1 -- COUNT (required):
    [INVENTORY CLOSED -- {P} pattern claims, {A} evidence anchors, {C} adjudication commitments

  Field 2 -- IMMUTABLE (required):
    IMMUTABLE -- after sealing, the contents of this inventory are fixed. Beat 5 framing, prose
    narrative, and recommendation preference are each prohibited as inputs to retroactive revision
    of the pattern claims, evidence anchors, or adjudication commitments above.

  Field 3 -- VALIDITY NOTICE (required):
    A stamp that contains Field 1 but omits Field 2 is structurally incomplete and does not
    constitute a valid seal.]
```

Write the complete stamp (all three fields, in sequence, within the same bracket):

```
[INVENTORY CLOSED -- {P} pattern claims, {A} evidence anchors, {C} adjudication commitments
 IMMUTABLE -- after sealing, the contents of this inventory are fixed. Beat 5 framing, prose
 narrative, and recommendation preference are each prohibited as inputs to retroactive revision.
 A stamp missing the IMMUTABLE field is structurally incomplete and does not constitute a valid seal.]
```

Do not open Beat 4.5 until a structurally complete stamp (all three fields) is written.

**Inventory prohibition**: Beat 4.5 and Beat 5 may not introduce claims not in this inventory.

---

### Beat 4.5 -- Derivation chain

Six elements. Reads from the Beat 3 Output Inventory only.

```
Anchored claim: "[exact pattern claim from Inventory, verbatim with anchor]"
  (anchored: {artifact-name}, {stance})
Net vector: {CONFIRMED | QUALIFIED | REVERSED | REDIRECTED} -- [mechanism sentence from
  reconciliation table, copied verbatim -- must match reconciliation conclusion]
Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON} -- [one sentence: licensing --
  consistent with Band gate output and weight-level constraints including Rule applied: field]
Adjacent verb: {ADJ-VERB} -- [one sentence: which specific reconciliation table row, and
  which inertia weight designation in that row, would have to differ for this adjacent verb
  to apply -- name the exact entry a reader preferring the adjacent verb must contest]
Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule -- [the specific rule that would need to
  produce a different consequence for the adjacent verb to become licensed. Must use the same
  label scheme as the Rule applied: field in the reconciliation conclusion.]
Conditions: [one of: CONTRADICTS count by weight / gap-closure cost / risk tolerance
  threshold / readiness signal distribution -- stated as a specific value, citing at least
  one named weight level from the reconciliation table]
```

Do not write Beat 5 until all six elements are internally consistent and derive exclusively
from the Inventory.

---

**Beat 5 -- Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon** -- must match Beat 4.5 verb and Band
gate output. One paragraph. Names what to do, under what conditions, with what scope.

---

**Voice**: Active, opinionated. The reconciliation conclusion reads as a formally labeled
decision record where Rule applied: names the specific rule triggered; the closure stamp reads
as a format-specified record with three required fields; the derivation chain reads as a
decision frame with rule-labeled contestation points; recommendation reads as a directive.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

**Working hypothesis (S0)**: [claim]

## Hypothesis Mutation Ledger
...
**Hypothesis at S3**: [evolved claim]
**Net mutation vector**: {vector} -- [mechanism]
**Evidence trajectory**: POINT-IN-TIME | DIRECTIONAL -- [declaration]

## Vector-Verdict Reconciliation
| Signal | Inertia weight | Verdict type | Consistent? |
...
**Rule applied**: {VECTOR}/{WEIGHT_LEVEL} rule -- [consequence triggered]
**Reconciliation**: [conclusion -- references Rule applied: label]

## Conflict Register
...
[REGISTER CLOSED -- N rows, R RESOLVED, U UNRESOLVED]

## Confidence Band
...
Confidence Band: HIGH | MEDIUM | LOW
Selected stance: {verb}

## Story
### Beat 1-4 ...

### Beat 3 Output Inventory
Pattern claims: ...
Evidence anchors: ...
Adjudication commitments: ...
[INVENTORY CLOSED -- P claims, A anchors, C commitments
 IMMUTABLE -- after sealing, contents are fixed. Beat 5 framing, prose narrative, and
 recommendation preference are prohibited as revision inputs.
 A stamp missing the IMMUTABLE field is structurally incomplete and not a valid seal.]

### Beat 4.5 -- Derivation chain
Anchored claim: "[verbatim from Inventory]" (anchored: ...)
Net vector: {vector} -- [mechanism -- matches reconciliation, Rule applied: label cited]
Recommendation verb: {VERB} -- [licensing -- Band gate, weight constraint, Rule applied:]
Adjacent verb: {ADJ-VERB} -- [contestation -- row and weight designation]
Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule -- [rule that must differ for ADJ-VERB]
Conditions: [weight-sensitive value -- at least one weight level named]

### Beat 5 -- Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON** -- [directive -- no new reasoning]
```

---

## V-05

**Variation axis**: Full combination -- C-33 (rule-label citation FORMAT FIELDS) + C-34
(Re-sealing Reconciliation Decision FORMAT BLOCK) on R13 V-05 EVALUATOR/AUTHOR base,
targeting C-26, C-27, C-28, C-29, C-30, C-31, C-32, C-33, and C-34 simultaneously
**Hypothesis**: R13 V-05 achieves C-26 through C-32 but has two residual gaps. V-02 adds
C-33 in isolation; V-03 adds C-34 in isolation. Combining them on R13 V-05: adding C-33
requires `Rule applied:` in E-5 and `Contestation rule:` in Beat 4.5; adding C-34 requires
the re-sealing protocol step b to produce a format-constrained Re-sealing Reconciliation
Decision block. The prediction: both additions are structurally independent -- C-33 operates
at the reconciliation table step; C-34 operates at the re-sealing lifecycle -- and combining
them on R13 V-05 is sufficient to achieve the full v13 criterion set. Authority trace is
end-to-end: E-3 inertia marker text -> E-5 weight level -> rule label -> `Rule applied:
{VECTOR}/{WEIGHT_LEVEL}` -> reconciliation conclusion -> Packet -> A-1 Beat 4.5
Recommendation verb (citing Rule applied: by name) + `Contestation rule:`. Re-sealing path:
new conflict -> E-5 Re-sealing Reconciliation Decision block with `Rule re-executed:` label
+ `Vector status:` + `Trigger:` -> new Packet.

---

You are running `/topic:story` for a topic. The topic name is provided.

This skill runs in two phases: **EVALUATOR** then **AUTHOR**. Do not begin AUTHOR until
EVALUATOR is complete and the Derivation Packet is sealed.

---

## EVALUATOR Phase

**Permitted**: Gathering artifacts. Extracting findings. Assigning stances and rationales.
Tracking hypothesis mutation. Computing the reconciliation table with inertia weights.
Adjudicating conflicts. Closing the Conflict Register. Synthesizing the cross-signal pattern.
Enumerating all pattern outputs into the Derivation Packet. Computing the Confidence Band and
writing the OVERRIDE field if required. Sealing the Packet.
**Forbidden**: Writing story prose (Beats 1-5). Narrative framing. Editorial voice.
Recommendation stance selection beyond what the Band gate determines.

---

### E-1 -- Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### E-2 -- Declare the working hypothesis (S0)

```
Working hypothesis (S0): [one sentence -- falsifiable assertion]
```

---

### E-3 -- Signal Extract with stance rationale and inertia marker

For each artifact, in gather order:

```
- `{artifact-name}`: {one sentence -- the single most important finding, stated as fact}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  Rationale: {one sentence -- the specific element that drove the stance}
  Inertia marker: prior expectation: {what was believed before this signal arrived}
  [if MODIFIES]: Hypothesis update: [previous wording] -> [updated wording]
```

---

### E-4 -- Declare S3, net mutation vector, and evidence trajectory

```
Hypothesis at S3: [evolved claim]
Net mutation vector: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED -- [mechanism sentence;
  cite at least one entry by artifact name]
Evidence trajectory: POINT-IN-TIME | DIRECTIONAL -- [declaration]
```

Anti-stagnation check applies.

---

### E-5 -- Vector-verdict reconciliation table with weight-level triggers

One row per ledger entry. Derive an explicit inertia weight from each entry's inertia marker:
- **HIGH** -- firmly established belief, prior measurement, existing design commitment, or
  strong organizational assumption
- **MEDIUM** -- working assumption held with moderate confidence
- **LOW** -- weak prior or expectation held with acknowledged uncertainty

```
| Signal | Inertia weight | Verdict type | Consistent with declared vector? |
|--------|----------------|--------------|----------------------------------|
| {artifact-name} | HIGH -- "{inertia marker text}" | CONFIRMS | YES |
| {artifact-name} | MEDIUM -- "{inertia marker text}" | MODIFIES toward {dimension} | YES |
| {artifact-name} | HIGH -- "{inertia marker text}" | CONTRADICTS on {dimension} -- RESOLVED | YES (resolved) |
| {artifact-name} | HIGH -- "{inertia marker text}" | CONTRADICTS on {dimension} -- UNRESOLVED | CONFLICT |
```

**Weight-level consistency rules** -- weight level is the named trigger condition:

**CONFIRMED**:
- CONFIRMED/HIGH: HIGH-weight CONTRADICTS UNRESOLVED -- CONFIRMED invalid; must become QUALIFIED
  or resolve. No path to maintain CONFIRMED with a HIGH-weight CONTRADICTS unresolved.
- CONFIRMED/MEDIUM: MEDIUM-weight CONTRADICTS UNRESOLVED -- CONFIRMED invalid; must become
  QUALIFIED or resolve. Resolving before authoring begins restores CONFIRMED.
- CONFIRMED/LOW: LOW-weight CONTRADICTS UNRESOLVED -- CONFIRMED permissible only when
  HIGH-weight CONFIRMS >= 70% of all CONFIRMS entries; otherwise revise to QUALIFIED.
- CONFIRMED/CLEAR: No unresolved CONTRADICTS -- CONFIRMED valid; no constraint.

**QUALIFIED**:
- QUALIFIED/HIGH: HIGH-weight CONTRADICTS UNRESOLVED -- CONFLICT row; QUALIFIED valid; PROCEED
  blocked; PAUSE is minimum permitted stance from Band gate.
- QUALIFIED/MEDIUM: MEDIUM-weight CONTRADICTS UNRESOLVED -- CONFLICT row; QUALIFIED valid;
  Band gate applies normally; no additional stance restriction.
- QUALIFIED/LOW: LOW-weight CONTRADICTS UNRESOLVED -- CONFLICT row; QUALIFIED valid; no
  stance restriction; transfers to Beat 4 as gap.

**REVERSED**:
- REVERSED/HIGH-dominant: HIGH-weight CONTRADICTS majority -- strongly grounded.
- REVERSED/MEDIUM-dominant: MEDIUM-weight CONTRADICTS majority -- valid; name the dimension.
- REVERSED/LOW-dominant: LOW-weight majority -- must name cumulative mechanism or revise to
  QUALIFIED.

**REDIRECTED**:
- REDIRECTED/ANY: Weight distributes across dimensions; grading does not apply.

After the table, write the rule citation block and reconciliation conclusion:

```
Rule applied: {VECTOR}/{WEIGHT_LEVEL} rule -- [the specific consequence this rule triggered.
  Use the label names from the rule table above. This field is required -- a conclusion without
  a Rule applied: field fails C-33 even when the narrative references weight levels.]
Reconciliation: Vector is consistent -- [one sentence: which decisive entries' weight levels
  triggered the named rule, and what the rule required. Must reference the Rule applied: label.]
  OR: Vector revised from [X] to [Y] -- [one sentence: the named rule forced revision because
  {weight level} {verdict type} at [{artifact-name}] triggered the rule's consequence].
```

---

### E-6 -- Conflict Register

Open the Register (OPEN state).

For every stance conflict:

```
Conflict: `{signal-A}` vs `{signal-B}` -- [dimension]
Verdict: RESOLVED in favor of `{signal}` because [evidential reason -- name inertia weight]
     OR: UNRESOLVED because [what {namespace}/{skill} would resolve it]
```

Close:

```
[REGISTER CLOSED -- {N} rows, {R} RESOLVED, {U} UNRESOLVED]
```

---

### E-7 -- Pattern synthesis (raw)

NOT story prose -- analytical product for the Packet.

Open: "Across [N] signals, the hypothesis was [vector]."
For each non-trivial claim: `(anchored: {artifact-name}, {stance})`.

```
Falsifiability: [externally observable domain evidence that would falsify the pattern claim]
```

---

### E-8 -- Confidence Band

| Band   | Criteria                              | Permitted stances               | Default     |
|--------|---------------------------------------|---------------------------------|-------------|
| HIGH   | S/N >= 0.70 AND U = 0                 | Any                             | Per pattern |
| MEDIUM | 0.50 <= S/N < 0.70 OR U <= 2          | Any; non-default needs OVERRIDE | PAUSE       |
| LOW    | S/N < 0.50 OR U > 2                   | PAUSE, PIVOT, ABANDON           | PAUSE/PIVOT |

LOW band: PROCEED prohibited. No OVERRIDE can bypass this.
Any HIGH-weight CONTRADICTS UNRESOLVED (QUALIFIED/HIGH rule) blocks PROCEED regardless of Band.
MEDIUM non-default: OVERRIDE must name the specific gap being accepted and why it does not
change the stance. Must not restate verb, restate band, or use vague qualifier.

---

### E-9 -- Seal the Derivation Packet

Write the Derivation Packet. This is the complete and sole input to AUTHOR.

```
## Derivation Packet

### Signal Extract
[All ledger entries from E-3, verbatim]

### S3, Vector, and Trajectory
Hypothesis at S3: [verbatim from E-4]
Net mutation vector: {vector} -- [mechanism sentence, verbatim]
Evidence trajectory: POINT-IN-TIME | DIRECTIONAL -- [declaration]

### Vector-Verdict Reconciliation
[Table from E-5 with inertia-weight column, verbatim]
Rule applied: {VECTOR}/{WEIGHT_LEVEL} rule -- [consequence triggered, verbatim from E-5]
Reconciliation: [conclusion, verbatim from E-5]

### Pattern claims
1. "[claim]" (anchored: {artifact-name}, {stance})
2. ...

### Evidence anchors
- {artifact-name} ({stance}): [one phrase -- role in pattern claim]

### Adjudication commitments
- `{signal-A}` vs `{signal-B}`: RESOLVED in favor of `{signal}` -- [reason phrase]
[If none: "No adjudicated conflicts."]

### Confidence Band
Signals confirming: {S}/{N} ({pct}%)
Unresolved contradictions: {U}
Band: HIGH | MEDIUM | LOW
Default stance: {default}
Selected stance: {verb}
[OVERRIDE: {named rationale}]

### Falsifiability
[Verbatim from E-7]
```

Append the Packet seal. Three required fields: COUNT, IMMUTABLE, VALIDITY NOTICE. A seal
missing the IMMUTABLE field is not a valid seal.

```
[PACKET SEALED -- {P} pattern claims, {A} evidence anchors, {C} commitments,
  Band: {band}, Selected stance: {verb}
  IMMUTABLE -- no item in this Packet may be added, modified, or removed after this stamp.
  The Pattern claims, Evidence anchors, Adjudication commitments, Rule applied: field,
  Confidence Band, and OVERRIDE field (if present) are irrevocable derivation inputs.
  Beat 5 framing, AUTHOR prose, and recommendation preference are each prohibited as inputs
  to retroactive revision. A seal missing the IMMUTABLE field is structurally incomplete and
  not a valid seal. If a conflict surfaces during AUTHOR: activate the Mid-Draft Conflict
  Re-Sealing Protocol -- full EVALUATOR revisit required; Re-sealing Reconciliation Decision
  block required at E-5; no exception path; silent absorption is prohibited.]
```

---

### Mid-Draft Conflict Re-Sealing Protocol

This protocol activates when AUTHOR discovers a signal conflict not in the Derivation Packet
during Beats 1-5. The protocol is mandatory -- no exception path exists, regardless of whether
the conflict appears minor.

**Step 1**: STOP authoring immediately. Silent prose absorption -- continuing to draft while
incorporating or reasoning around the conflict -- is prohibited.

**Step 2**: Return to EVALUATOR phase. Execute ALL of the following steps in sequence:

  a. **E-3 update**: Add the newly-surfaced conflict as a ledger entry (or update the existing
     entry if already present and the conflict was missed). Assign stance, rationale, and
     inertia marker.

  b. **E-5 update**: Add or revise the corresponding row in the reconciliation table.
     Re-execute the weight-level consistency rules against the updated row distribution.
     Immediately after the updated table row, write the Re-sealing Reconciliation Decision
     as a required FORMAT BLOCK:

     ```
     Re-sealing Reconciliation Decision:
       Rule re-executed: {VECTOR}/{WEIGHT_LEVEL} rule -- [the specific consistency rule
         applied to the updated distribution. Use the same label format as E-5: e.g.,
         QUALIFIED/HIGH, CONFIRMED/MEDIUM, REVERSED/LOW-dominant, CONFIRMED/CLEAR.
         Required regardless of whether the vector changed.]
       Vector status: UNCHANGED | REVISED from {OLD} to {NEW}
       [If REVISED]: Trigger: {artifact-name} ({weight level}, {verdict type}) triggered
         the {VECTOR}/{WEIGHT_LEVEL} rule -- consequence: [the specific consequence stated
         in the rule: e.g., "PROCEED blocked; PAUSE is the minimum permitted stance from
         the Band gate" or "CONFIRMED invalid; must become QUALIFIED or resolve the conflict".]
     ```

     A re-sealing that renders the weight-level rule application as prose rather than producing
     this FORMAT BLOCK satisfies C-32 but fails C-34. The `Rule re-executed:` and `Vector
     status:` sub-fields are always required. The `Trigger:` sub-field is required only when
     Vector status is REVISED.

  c. **E-6 update**: Add the conflict to the Conflict Register with verdict and because-clause.
     If the vector changed, verify all existing Register entries remain consistent.

  d. **E-7 update**: Revise the pattern synthesis if any pattern claim, evidence anchor, or
     adjudication commitment changes.

  e. **E-8 update**: Recalculate the Confidence Band with updated S, N, U counts.

  f. **E-9 re-seal**: Write a new Derivation Packet incorporating all updates from a-e,
     including the updated `Rule applied:` field from E-5. Append a new PACKET SEALED stamp
     (all three required fields). The old Packet is superseded; the new Packet is the
     authoritative derivation input.

**Step 3**: Resume AUTHOR from the discovery point. All remaining AUTHOR beats derive from
the NEW Derivation Packet only. The old Packet may not be referenced.

---

## AUTHOR Phase

**Permitted**: Pattern derivation. Story prose. Conflict rendering. Recommendation.
Adjacent-verb contrast.
**Forbidden**: Re-reading signal artifacts. Introducing evidence or claims not in the Packet.
Revising the Packet. Absorbing mid-draft conflicts into prose without activating the Protocol.

---

### A-1 -- Write story beats from the Derivation Packet

**Beat 1 -- What we set out to understand**
One to three sentences. Original question, S0 from the Packet, entering default.

**Beat 2 -- What each signal revealed**
One editorial sentence per Packet Signal Extract entry -- what the finding means given its
stance and inertia marker. Two sentences maximum per signal.

**Beat 3 -- What the signals say together**
Open: "Across [N] signals, the hypothesis was [vector from Packet]."
Draw from the Packet's Pattern claims and Evidence anchors. Render conflict/verdict entries
from the Register. Close with the Packet's falsifiability condition, copied verbatim.

If a new signal conflict surfaces during Beat 3: activate the Mid-Draft Conflict Re-Sealing
Protocol immediately.

**Beat 4 -- What remains uncertain**

```
Gap: [what is unknown]
Most exposed finding: [which Packet pattern claim is most at risk]
Next signal: {namespace}/{skill} -- [expected finding type]
```

**Beat 4.5 -- Derivation chain** (reads from Packet only)

Six elements:

```
Anchored claim: "[exact claim from Packet's Pattern claims, verbatim with anchor]"
  (anchored: {artifact-name}, {stance})
Net vector: {vector from Packet} -- [mechanism sentence, verbatim from Packet]
Recommendation verb: {verb from Packet's Selected stance} -- [one sentence: licensing --
  states what in the Packet's reconciliation table (citing the Packet's Rule applied: label
  by name) and Band gate authorizes this verb. A licensing sentence that cites weight levels
  without naming the Rule applied: label fails C-33.]
Adjacent verb: {adjacent verb} -- [one sentence: which specific row in the Packet's
  reconciliation table, and which inertia weight designation in that row, would have to
  differ for the adjacent verb to apply]
Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule -- [the specific rule from the Packet's
  rule table that would need to produce a different consequence for the adjacent verb to
  become licensed. Must use the same label scheme as the Packet's Rule applied: field.
  A contestation naming a row and weight without the rule label fails C-33.]
Conditions: [weight-sensitive parameter from Packet -- specific value citing at least one
  inertia-weight designation from the reconciliation table]
```

**Beat 5 -- Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon** -- must match Packet's Selected stance.
One paragraph. Names accepted uncertainty if OVERRIDE present. No new evidence or reasoning.

---

**Voice**: The Packet reads as an engineering specification with irrevocable seal; Rule applied:
is a required format field naming the specific rule triggered; the Re-Sealing Protocol reads
as a mandatory procedure with a format-constrained Re-sealing Reconciliation Decision block
closing the weight-blind re-evaluation gap; the derivation chain reads as a decision frame
with rule-labeled contestation points; recommendation reads as a directive.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

## Derivation Packet

### Signal Extract
- `{artifact-name}`: {finding}
  Stance: ...
  Rationale: ...
  Inertia marker: prior expectation: [belief]
...

### S3, Vector, and Trajectory
Hypothesis at S3: [claim]
Net mutation vector: {vector} -- [mechanism]
Evidence trajectory: POINT-IN-TIME | DIRECTIONAL -- [sentence]

### Vector-Verdict Reconciliation
| Signal | Inertia weight | Verdict type | Consistent? |
...
Rule applied: {VECTOR}/{WEIGHT_LEVEL} rule -- [consequence triggered]
Reconciliation: [conclusion -- references Rule applied: label]

### Pattern claims
1. "[claim]" (anchored: ...)

### Evidence anchors / Adjudication commitments / Confidence Band / Falsifiability
[verbatim from E-steps]

[PACKET SEALED -- P claims, A anchors, C commitments, Band: {band}, Stance: {verb}
  IMMUTABLE -- irrevocable. Rule applied: field, Pattern claims, Evidence anchors, and
  all other Packet contents are irrevocable. A stamp missing this IMMUTABLE clause is not
  a valid seal. If conflict surfaces in AUTHOR: activate Mid-Draft Conflict Re-Sealing
  Protocol -- Re-sealing Reconciliation Decision block required at E-5 step b; full
  EVALUATOR revisit; no exception path; silent absorption prohibited.]

## Story

### Beat 1 -- What we set out to understand
...

### Beat 2 -- What each signal revealed
...

### Beat 3 -- What the signals say together
Across [N] signals, the hypothesis was [vector from Packet].
[pattern -- anchored claims, conflict/verdict, falsifiability verbatim]

### Beat 4 -- What remains uncertain
Gap: ...

### Beat 4.5 -- Derivation chain
Anchored claim: "[from Packet]" (anchored: ...)
Net vector: {vector} -- [mechanism, verbatim from Packet]
Recommendation verb: {VERB} -- [licensing -- cites Packet Rule applied: label by name and
  Band gate]
Adjacent verb: {ADJ-VERB} -- [contestation -- Packet reconciliation row and weight]
Contestation rule: {VECTOR}/{WEIGHT_LEVEL} rule -- [rule that must differ for ADJ-VERB]
Conditions: [weight-sensitive parameter with inertia weight]

### Beat 5 -- Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON** -- [directive; no new reasoning]
```
