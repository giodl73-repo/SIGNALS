---
skill: quest-variate
skill_target: topic-story
date: 2026-03-15
round: 13
rubric: v12
---

# Variations — topic-story (Round 13)

Five complete, runnable skill body prompt variations.
Single-axis first (V-01 through V-03), then two combinations (V-04, V-05).

**Design context**: v12 rubric adds C-30 (Weight-Level Consistency Triggers), C-31
(Stamp-Format Immutability Requirement), and C-32 (Phase-Separated Immutability with
Re-Sealing Protocol). From Round 12:

- V-01 achieves C-28 via inertia-weight column with weight-sensitive rules, but the QUALIFIED
  rule is weight-blind: "An UNRESOLVED CONTRADICTS at any weight level produces a CONFLICT row"
  — HIGH and LOW produce identical outcomes, so weight level is not a named trigger condition.
- V-02 achieves C-28 + C-29 + C-31 via the inertia-marker ledger and immutability clause
  embedded inside the closure stamp brackets; the stamp format specification states "A stamp
  without this clause is not sealed." C-30 gap: no reconciliation table in V-02, so weight-level
  trigger is not tested.
- V-03 achieves C-28 via standalone Marker Lock; no stamp immutability — C-29 FAIL, C-31 FAIL.
- V-04 achieves C-28 + C-29 + C-31 on R11 V-04 base (reconciliation table + derivation chain +
  OVERRIDE + immutability in stamp). C-30 gap: QUALIFIED rule is weight-blind.
- V-05 achieves C-26 + C-27 + C-28 + C-29 + C-31 on EVALUATOR/AUTHOR base. C-30 gap: QUALIFIED
  rule is weight-blind. C-32 gap: re-sealing instruction in the PACKET SEALED stamp says "return
  to EVALUATOR: add a new Register entry, update Adjudication commitments, re-seal" — this is a
  partial update, not a full EVALUATOR-phase revisit with new signal extraction and reconciliation.

**C-30 gap**: In every R12 variation with a reconciliation table, the QUALIFIED rule states "An
UNRESOLVED CONTRADICTS at any weight level produces a CONFLICT row" — treating HIGH and LOW
identically. C-30 requires the weight levels (HIGH/MEDIUM/LOW) to be named trigger conditions
that produce genuinely graded outcomes. If the rule fires the same consequence for every weight
level, the weight column is an input annotation, not a trigger. The fix: HIGH-weight UNRESOLVED
blocks PROCEED; MEDIUM-weight UNRESOLVED transfers to Beat 4 without blocking stance; LOW-weight
UNRESOLVED is noted as gap with no stance constraint — three distinct consequences, each triggered
by the named weight level.

**C-31 gap**: R12 V-01 and V-03 have no immutability clause at all — C-29 FAIL, C-31 FAIL.
R12 V-02 and V-04 embed the prohibition inside the stamp brackets and say "a stamp without this
clause is not sealed" — C-29 PASS, C-31 PASS. C-31 is specifically the upgrade from "prohibition
exists somewhere" to "prohibition is a required FORMAT FIELD whose absence makes the stamp
structurally incomplete." R13 V-02 targets this for the V-01 base (which still has a bare count
stamp) by restructuring the stamp as an explicit FORMAT SPECIFICATION with named required fields.

**C-32 gap**: R12 V-05's re-sealing instruction covers only Register update and Adjudication
commitments update. C-32 requires the re-sealing protocol to mandate a full EVALUATOR-phase
revisit — re-running signal extraction, reconciliation, pattern synthesis, and Band calculation —
before AUTHOR continues. Silent prose absorption is not named as prohibited. The partial protocol
leaves mid-draft conflicts that are "small" without a defined path: an AUTHOR might still absorb
them into prose reasoning rather than triggering the full revisit.

**Round 13 primary axes:**

V-01 targets C-30 single-axis on R12 V-01 base — rewrites ALL consistency rules so each weight
level (HIGH/MEDIUM/LOW) is a named trigger producing a genuinely distinct outcome, particularly
fixing the QUALIFIED rule where the gap is most visible.

V-02 targets C-31 single-axis on R12 V-01 base — same minimal base, different fix: restructures
the closure stamp as a formal FORMAT SPECIFICATION with three named required fields (COUNT, IMMUTABLE,
VALIDITY), where a stamp missing the IMMUTABLE field is by definition structurally incomplete.

V-03 targets C-32 single-axis on R12 V-05 base — upgrades the partial re-sealing instruction
to a full numbered protocol that (1) names silent prose absorption as prohibited, (2) mandates
full EVALUATOR revisit (all E-steps), and (3) makes no exception for conflicts the AUTHOR judges
to be minor.

V-04 combines C-30 + C-31 on R12 V-01 base — applies V-01's weight-graded consistency rules and
V-02's formal stamp format specification together on the minimal single-phase architecture.

V-05 is the full combination: C-30 (weight-graded rules in EVALUATOR's reconciliation table) +
C-31 (formal PACKET SEALED stamp with named required fields) + C-32 (full re-sealing protocol) on
R12 V-05 EVALUATOR/AUTHOR base, targeting C-26, C-27, C-28, C-29, C-30, C-31, and C-32
simultaneously.

---

## V-01

**Variation axis**: Output format — weight-level graded consistency rules (C-30 target)
**Hypothesis**: C-30 fails when the consistency rules mention weight levels but apply the
same consequence regardless of level. R12 V-01's QUALIFIED rule states "An UNRESOLVED
CONTRADICTS at any weight level produces a CONFLICT row" — HIGH and LOW CONTRADICTS both
trigger an identical CONFLICT row outcome, making weight level an annotation rather than a
trigger. The fix is to make each weight level a named condition whose consequence differs: a
HIGH-weight UNRESOLVED CONTRADICTS blocks PROCEED (a stance restriction); a MEDIUM-weight
UNRESOLVED CONTRADICTS produces a CONFLICT row but does not constrain the Band-gate-selected
stance; a LOW-weight UNRESOLVED CONTRADICTS is a gap with no stance constraint. With three
weight levels each producing a distinct named consequence, the weight level IS the trigger, not
the verdict label. This variation also upgrades the CONFIRMED and REVERSED rules to be
weight-graded for completeness. C-29 and C-31 are NOT targeted — the stamp remains a bare count
stamp, isolating the C-30 axis.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### Step 2 — Hypothesis mutation ledger

Before writing any story section, complete the ledger. Write it to the artifact as the
first section.

**Working hypothesis (S0)**: [one sentence — the specific claim the team entered with,
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
Hypothesis at S3: [one sentence — working hypothesis after all stances applied]

Net mutation vector: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED
[one sentence: mechanism — which stances, on which dimension, drove this; cite at least
one entry by artifact name]

Evidence trajectory: POINT-IN-TIME | DIRECTIONAL — [explicit declaration]
```

**Anti-stagnation check**: If S3 is identical to S0, state why. Silently identical fails.

**Reconciliation check**: CONFIRMED with visible unresolved CONTRADICTS, or REVERSED with
no CONTRADICTS, must be revised before proceeding.

Do not begin story beats until the ledger is complete.

---

### Step 2b — Vector-verdict reconciliation table

After declaring the vector, complete the reconciliation table. One row per ledger entry.

Derive an inertia weight from each entry's inertia marker text:
- **HIGH** — the inertia marker names a firmly established belief, prior measurement, existing
  design commitment, or strong organizational assumption
- **MEDIUM** — the inertia marker names a working assumption or expectation held with moderate
  confidence
- **LOW** — the inertia marker names a weak prior, default assumption, or expectation held with
  acknowledged uncertainty

```
| Signal | Inertia weight | Verdict type | Consistent with declared vector? |
|--------|---------------|-------------|----------------------------------|
| {artifact-name} | HIGH — "{prior expectation text, quoted or paraphrased}" | CONFIRMS | YES |
| {artifact-name} | MEDIUM — "{prior expectation text}" | MODIFIES toward {dimension} | YES |
| {artifact-name} | HIGH — "{prior expectation text}" | CONTRADICTS on {dimension} — RESOLVED | YES (resolved) |
| {artifact-name} | HIGH — "{prior expectation text}" | CONTRADICTS on {dimension} — UNRESOLVED | CONFLICT |
```

**Weight-level consistency rules** — weight level is the named trigger condition; each level
produces a distinct consequence:

**CONFIRMED**:
- HIGH-weight CONTRADICTS UNRESOLVED: CONFIRMED is invalid. The vector must become QUALIFIED
  or the conflict must be resolved in Step 3. No path exists to maintain CONFIRMED while a
  HIGH-weight CONTRADICTS is unresolved.
- MEDIUM-weight CONTRADICTS UNRESOLVED: CONFIRMED is invalid. Must become QUALIFIED or resolve
  the conflict. Resolving the conflict before authoring begins restores CONFIRMED.
- LOW-weight CONTRADICTS UNRESOLVED: CONFIRMED is permissible only when HIGH-weight CONFIRMS
  entries constitute >= 70% of all CONFIRMS-stance entries. Otherwise revise to QUALIFIED.

**QUALIFIED**:
- HIGH-weight CONTRADICTS UNRESOLVED: produces a CONFLICT row; QUALIFIED remains valid but
  PROCEED is blocked — PAUSE is the minimum permitted stance from the Band gate.
- MEDIUM-weight CONTRADICTS UNRESOLVED: produces a CONFLICT row; QUALIFIED remains valid; Band
  gate applies normally with no additional stance restriction.
- LOW-weight CONTRADICTS UNRESOLVED: produces a CONFLICT row; QUALIFIED remains valid; no
  stance restriction; transfers to Beat 4 as a gap with no effect on stance selection.

**REVERSED**:
- Requires that HIGH-weight or MEDIUM-weight CONTRADICTS entries constitute a majority of
  evidence weight. A REVERSED vector driven predominantly by LOW-weight entries must name the
  cumulative mechanism explicitly — why the accumulation of low-inertia contradictions overturns
  the hypothesis — or the vector must be revised to QUALIFIED.
- HIGH-weight dominant REVERSED: strongly grounded; no additional justification required.
- MEDIUM-weight dominant REVERSED: valid; name the specific dimension where reversal occurred.

**REDIRECTED**:
- Evidence answers a different evaluative frame than S0; weight distributes across dimensions
  rather than loading onto the S0 contradiction axis. Weight-level grading does not apply to
  REDIRECTED since the frame shift is the primary mechanism.

After the table:

```
Reconciliation: Vector is consistent — [one sentence citing weight levels of decisive entries
  and naming which weight-trigger rule validates the consistency claim].
  OR: Vector revised from [X] to [Y] — [one sentence: which weight level, at which verdict,
  triggered the rule that forced revision, and what the rule required].
```

Do not begin story beats until the ledger, vector, and reconciliation are complete.

---

### Step 3 — Conflict Register

Open the Conflict Register (OPEN state).

For every pair of signal entries with opposing stances on the same dimension:

```
Conflict: `{signal-A}` vs `{signal-B}` — [dimension]
Verdict: RESOLVED in favor of `{signal}` because [specific evidential reason — name the
  inertia weight of the decisive entry]
     OR: UNRESOLVED because [what {namespace}/{skill} signal would resolve it]
```

Every verdict carries a because-clause. Any CONFLICT row from the reconciliation table must
appear here as a named entry.

**Prose prohibition**: Adjudication commitments belong in the Register with because-clauses,
not in narrative prose.

Close:

```
[REGISTER CLOSED — {N} rows, {R} RESOLVED, {U} UNRESOLVED]
```

UNRESOLVED entries auto-transfer to Beat 4. Do not begin story beats until this stamp is
written.

---

### Step 4 — Confidence Band Calculation

Count: S (CONFIRMS), N (total), U (UNRESOLVED in Register).

| Band   | Criteria                                          | Default stance      |
|--------|---------------------------------------------------|---------------------|
| HIGH   | S/N >= 0.70 AND U = 0                             | Per pattern direction |
| MEDIUM | 0.50 <= S/N < 0.70 OR (S/N >= 0.50 AND U <= 2)   | PAUSE               |
| LOW    | S/N < 0.50 OR U > 2                               | PAUSE or PIVOT      |

LOW band: PROCEED is prohibited — no override can bypass this.

Permitted stances by band:
- HIGH: any stance allowed
- MEDIUM: any stance allowed — non-default requires OVERRIDE
- LOW: PAUSE, PIVOT, or ABANDON only

**Additional constraint from weight-level rules**: If any HIGH-weight CONTRADICTS UNRESOLVED
exists (triggering the QUALIFIED HIGH rule above), PROCEED is blocked regardless of Band. The
Band gate minimum still applies; the weight-level block adds a further restriction.

MEDIUM band with non-default stance: write the OVERRIDE field before Beat 4.5:

```
OVERRIDE: {named rationale — specific gap being accepted; why it does not change the
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

### Step 5 — Write the story beats

**Beat 1 — What we set out to understand**
One to three sentences. Original question, S0 hypothesis, entering default — what the team
expected and why. The entering default anchors the inertia markers in the ledger.

**Beat 2 — What each signal revealed** *(draws from the ledger)*
For each ledger entry, one editorial sentence beyond the finding — what the finding means for
the hypothesis, framed against the inertia marker. The inertia weight informs how significant
a surprise or confirmation this signal represents. Two sentences maximum per signal.

**Beat 3 — What the signals say together**
Open: "Across [N] signals, the hypothesis was [reconciled vector]." The reconciliation table
validates this claim.

**Anchor citation rule**: Every non-trivial Beat 3 claim cites its ledger entry inline:
`(anchored: {artifact-name}, {stance})`.

Draw conflict/verdict entries from the Register. Do not re-adjudicate in prose.

**Falsifiability gate**:

```
Falsifiability: [externally observable evidence — in the world, market, or system under
  analysis — that would falsify the pattern claim if found. Not a provenance check. A
  domain-facing prediction that could be wrong.]
```

**Beat 4 — What remains uncertain**
RESOLVED verdicts are not gaps. UNRESOLVED verdicts auto-transfer from the Register.

```
Gap: [what is unknown]
Most exposed finding: [which ledger claim is most at risk without this]
Next signal: {namespace}/{skill} — [expected finding type]
```

---

### Beat 3 Output Inventory

**Complete this section before opening Beat 4.5.**

Enumerate ALL Beat 3 outputs. Beat 4.5 reads from this inventory exclusively.

```
Beat 3 Output Inventory:

Pattern claims:
1. "[verbatim declarative sentence from Beat 3]" (anchored: {artifact-name}, {stance})
2. "[additional claims — verbatim, one per distinct claim]" (anchored: ...)

Evidence anchors:
- {artifact-name} ({stance}): [one phrase — role in pattern claim]
- ...

Adjudication commitments (RESOLVED verdicts from Register only):
- `{signal-A}` vs `{signal-B}`: RESOLVED in favor of `{signal}` — [reason phrase]
[If none: "No adjudicated conflicts."]
```

Completeness check: count `(anchored: ...)` citations in Beat 3; the Evidence anchors list
must contain exactly that count.

Closure stamp:

```
[INVENTORY CLOSED — {P} pattern claims, {A} evidence anchors, {C} adjudication commitments]
```

Do not open Beat 4.5 until this stamp is written.

**Inventory prohibition**: Beat 4.5 and Beat 5 may not introduce claims not in this inventory.

---

### Beat 4.5 — Derivation chain

Five elements. Reads from the Beat 3 Output Inventory only.

```
Anchored claim: "[exact pattern claim from Inventory, verbatim with anchor]"
  (anchored: {artifact-name}, {stance})
Net vector: {CONFIRMED | QUALIFIED | REVERSED | REDIRECTED} — [mechanism sentence from
  reconciliation table, copied verbatim — must match reconciliation conclusion]
Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON} — [one sentence: licensing —
  consistent with Band gate output and weight-level constraints]
Adjacent verb: {ADJ-VERB} — [one sentence: which specific reconciliation table row, and
  which inertia weight designation in that row, would have to differ for this adjacent verb
  to apply — name the exact entry a reader preferring the adjacent verb must contest]
Conditions: [one of: CONTRADICTS count by weight / gap-closure cost / risk tolerance
  threshold / readiness signal distribution — stated as a specific value, citing at least
  one named weight level from the reconciliation table]
```

**Conditions guidance**: The conditions clause must name at least one weight level from the
reconciliation table as part of the condition. "0 HIGH-weight CONTRADICTS remaining unresolved"
passes; "no remaining conflicts" fails (weight-blind).

Do not write Beat 5 until all five elements are internally consistent and derive exclusively
from the Inventory.

---

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon** — must match Beat 4.5 verb and Band
gate output. One paragraph. Names what to do, under what conditions, with what scope. Does
not repeat the derivation chain.

---

**Voice**: Active, opinionated. Reconciliation table reads as a formal weight-sensitive
consistency record where each weight level is a named trigger; derivation chain reads as a
decision frame with weight-traceable contestation points; recommendation reads as a directive.

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
**Net mutation vector**: {vector} — [mechanism sentence]
**Evidence trajectory**: POINT-IN-TIME | DIRECTIONAL — [declaration]

## Vector-Verdict Reconciliation
| Signal | Inertia weight | Verdict type | Consistent? |
|--------|---------------|-------------|-------------|
| {artifact-name} | HIGH — "{prior expectation}" | CONFIRMS | YES |
...
**Reconciliation**: [conclusion — names weight level as trigger, cites the rule that was applied]

## Conflict Register
Conflict: `{A}` vs `{B}` — [dimension]
Verdict: RESOLVED because [reason, names inertia weight] OR UNRESOLVED because [what]
...
[REGISTER CLOSED — N rows, R RESOLVED, U UNRESOLVED]

## Confidence Band
Signals confirming: {S}/{N} ({pct}%)
Unresolved contradictions: {U}
Confidence Band: HIGH | MEDIUM | LOW
Default stance: {default}
Selected stance: {verb}
[OVERRIDE: {named rationale}]

## Story

### Beat 1 — What we set out to understand
...

### Beat 2 — What each signal revealed
...

### Beat 3 — What the signals say together
Across [N] signals, the hypothesis was [reconciled vector].
[pattern — anchored claims, conflict/verdict, falsifiability]

### Beat 4 — What remains uncertain
Gap: ...

### Beat 3 Output Inventory
Pattern claims:
1. "[claim]" (anchored: ...)
Evidence anchors: ...
Adjudication commitments: ...
[INVENTORY CLOSED — P claims, A anchors, C commitments]

### Beat 4.5 — Derivation chain
Anchored claim: "[verbatim from Inventory]" (anchored: ...)
Net vector: {vector} — [mechanism — matches reconciliation]
Recommendation verb: {VERB} — [licensing — cites Band gate and weight-level constraint]
Adjacent verb: {ADJ-VERB} — [contestation — names reconciliation row and weight designation]
Conditions: [weight-sensitive parameter — specific value citing a named weight level]

### Beat 5 — Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON** — [directive — no new reasoning]
```

---

## V-02

**Variation axis**: Output format — stamp FORMAT SPECIFICATION with named required IMMUTABLE
field (C-31 target)
**Hypothesis**: C-31 fails when the closure stamp is a bare count record — `[INVENTORY CLOSED
— P claims, A anchors, C commitments]` — because an author can produce a structurally complete
stamp without any immutability commitment. R12 V-01's stamp is this bare form: the format
specification shows only the count brackets, and the stamp is complete as-written. C-31 requires
the stamp FORMAT itself to define the IMMUTABLE field as a required named element: a stamp
template that shows three required fields (COUNT, IMMUTABLE, VALIDITY) where a stamp with only
COUNT is structurally incomplete. This differs from simply appending a prohibition note adjacent
to the stamp (C-29 PASS, C-31 PARTIAL): the prohibition must be a named field in the template,
so that evaluating whether a stamp is complete requires checking for the IMMUTABLE field, not
reading surrounding prose. This variation targets C-31 on the minimal R12 V-01 base without
adding inertia-weight columns or phase separation. C-30 is NOT targeted — the reconciliation
table (inherited from R12 V-01) retains the weight-blind QUALIFIED rule, isolating the C-31 axis.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### Step 2 — Hypothesis mutation ledger

**Working hypothesis (S0)**: [one sentence — falsifiable assertion, not a goal]

For each signal artifact, in the order read:

```
- `{artifact-name}`: {key finding most relevant to the working hypothesis, one to two sentences}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  Inertia marker: prior expectation: {what was believed before this signal arrived}
  [if MODIFIES]: Hypothesis update: [previous wording] -> [updated wording]
```

After all entries:

```
Hypothesis at S3: [one sentence — working hypothesis after all stances applied]

Net mutation vector: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED
[one sentence: mechanism — which stances, on which dimension; cite at least one entry by
artifact name]

Evidence trajectory: POINT-IN-TIME | DIRECTIONAL — [explicit declaration]
```

Anti-stagnation check and reconciliation check apply.

Do not begin story beats until the ledger is complete.

---

### Step 2b — Vector-verdict reconciliation table

After declaring the vector, complete the reconciliation table. One row per ledger entry.

Derive an inertia weight from each entry's inertia marker text:
- **HIGH** — firmly established belief, prior measurement, existing design commitment, or
  strong organizational assumption
- **MEDIUM** — working assumption or expectation held with moderate confidence
- **LOW** — weak prior, default assumption, or expectation held with acknowledged uncertainty

```
| Signal | Inertia weight | Verdict type | Consistent with declared vector? |
|--------|---------------|-------------|----------------------------------|
| {artifact-name} | HIGH — "{prior expectation text}" | CONFIRMS | YES |
| {artifact-name} | MEDIUM — "{prior expectation text}" | MODIFIES toward {dimension} | YES |
| {artifact-name} | HIGH — "{prior expectation text}" | CONTRADICTS on {dimension} — RESOLVED | YES (resolved) |
| {artifact-name} | HIGH — "{prior expectation text}" | CONTRADICTS on {dimension} — UNRESOLVED | CONFLICT |
```

**Consistency rules** (weight-sensitive):
- **CONFIRMED**: Valid only when every CONTRADICTS entry is RESOLVED. A HIGH-weight
  CONTRADICTS that is UNRESOLVED invalidates CONFIRMED and produces a CONFLICT row. A
  MEDIUM-weight CONTRADICTS that is UNRESOLVED also produces a CONFLICT row requiring vector
  revision to QUALIFIED or conflict resolution.
- **QUALIFIED**: CONFIRMS and MODIFIES entries expected. Any UNRESOLVED CONTRADICTS at any
  weight level produces a CONFLICT row.
- **REVERSED**: Majority weight in CONTRADICTS entries, or reversing MODIFIES that overturn
  HIGH-weight priors.
- **REDIRECTED**: Weight distributes across dimensions rather than loading onto the S0 axis.

After the table:

```
Reconciliation: Vector is consistent — [reason citing inertia weights of decisive entries].
  OR: Vector revised from [X] to [Y] — [reason].
```

Do not begin story beats until the ledger, vector, and reconciliation are complete.

---

### Step 3 — Conflict Register

Open the Register (OPEN state).

For every stance conflict:

```
Conflict: `{signal-A}` vs `{signal-B}` — [dimension]
Verdict: RESOLVED in favor of `{signal}` because [evidential reason — name inertia weight
  of decisive entry]
     OR: UNRESOLVED because [what {namespace}/{skill} would resolve it]
```

Every verdict carries a because-clause. Any CONFLICT row from the reconciliation table must
appear here.

**Prose prohibition**: Adjudication commitments belong in the Register, not in narrative prose.

Close:

```
[REGISTER CLOSED — {N} rows, {R} RESOLVED, {U} UNRESOLVED]
```

UNRESOLVED entries auto-transfer to Beat 4. Do not begin story beats until this stamp is written.

---

### Step 4 — Confidence Band Calculation

Count: S (CONFIRMS), N (total), U (UNRESOLVED in Register).

| Band   | Criteria                                          | Default stance      |
|--------|---------------------------------------------------|---------------------|
| HIGH   | S/N >= 0.70 AND U = 0                             | Per pattern direction |
| MEDIUM | 0.50 <= S/N < 0.70 OR (S/N >= 0.50 AND U <= 2)   | PAUSE               |
| LOW    | S/N < 0.50 OR U > 2                               | PAUSE or PIVOT      |

LOW band: PROCEED is prohibited. MEDIUM non-default requires OVERRIDE:

```
OVERRIDE: {named rationale — specific gap being accepted; why it does not change the
  stance from the band default. Must not restate verb, restate band, or use vague qualifier.}
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

### Step 5 — Write the story beats

**Beat 1 — What we set out to understand**
One to three sentences. Original question, S0 hypothesis, entering default.

**Beat 2 — What each signal revealed** *(draws from the ledger)*
One editorial sentence per entry beyond the finding — what it means for the hypothesis,
framed against the inertia marker. Two sentences maximum per signal.

**Beat 3 — What the signals say together**
Open: "Across [N] signals, the hypothesis was [reconciled vector]."

**Anchor citation rule**: Every non-trivial Beat 3 claim cites its ledger entry:
`(anchored: {artifact-name}, {stance})`.

Draw conflict/verdict entries from the Register.

**Falsifiability gate**:

```
Falsifiability: [externally observable evidence that would falsify the pattern claim —
  domain-facing prediction, not a provenance check]
```

**Beat 4 — What remains uncertain**

```
Gap: [what is unknown]
Most exposed finding: [which ledger claim is most at risk]
Next signal: {namespace}/{skill} — [expected finding type]
```

---

### Beat 3 Output Inventory

**Complete this section before opening Beat 4.5.**

Enumerate ALL Beat 3 outputs.

```
Beat 3 Output Inventory:

Pattern claims:
1. "[verbatim declarative sentence from Beat 3]" (anchored: {artifact-name}, {stance})
2. "[additional claims — verbatim]" (anchored: ...)

Evidence anchors:
- {artifact-name} ({stance}): [one phrase — role in pattern claim]
- ...

Adjudication commitments (RESOLVED verdicts from Register only):
- `{signal-A}` vs `{signal-B}`: RESOLVED in favor of `{signal}` — [reason phrase]
[If none: "No adjudicated conflicts."]
```

Completeness check: count `(anchored: ...)` citations in Beat 3; Evidence anchors must contain
exactly that count.

**Inventory closure stamp — FORMAT SPECIFICATION**

The closure stamp has three required fields. A stamp is structurally complete only when all
three fields are present. A stamp containing Field 1 but missing Field 2 is not a valid seal.

```
Stamp field definitions:

  Field 1 — COUNT (required):
    [INVENTORY CLOSED — {P} pattern claims, {A} evidence anchors, {C} adjudication commitments

  Field 2 — IMMUTABLE (required):
    IMMUTABLE — after sealing, the contents of this inventory are fixed. Beat 5 framing, prose
    narrative, and recommendation preference are each prohibited as inputs to retroactive revision
    of the pattern claims, evidence anchors, or adjudication commitments above.

  Field 3 — VALIDITY NOTICE (required):
    A stamp that contains Field 1 but omits Field 2 is structurally incomplete and does not
    constitute a valid seal.]
```

Write the complete stamp (all three fields, in sequence, within the same bracket):

```
[INVENTORY CLOSED — {P} pattern claims, {A} evidence anchors, {C} adjudication commitments
 IMMUTABLE — after sealing, the contents of this inventory are fixed. Beat 5 framing, prose
 narrative, and recommendation preference are each prohibited as inputs to retroactive revision.
 A stamp missing the IMMUTABLE field is structurally incomplete and does not constitute a valid seal.]
```

Do not open Beat 4.5 until a structurally complete stamp (all three fields) is written.

**Inventory prohibition**: Beat 4.5 and Beat 5 may not introduce claims not in this inventory.

---

### Beat 4.5 — Derivation chain

Five elements. Reads from the Beat 3 Output Inventory only.

```
Anchored claim: "[exact pattern claim from Inventory, verbatim with anchor]"
  (anchored: {artifact-name}, {stance})
Net vector: {CONFIRMED | QUALIFIED | REVERSED | REDIRECTED} — [mechanism sentence from
  reconciliation table, copied verbatim]
Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON} — [one sentence: licensing —
  consistent with Band gate output]
Adjacent verb: {ADJ-VERB} — [one sentence: what specific reconciliation table row and
  inertia weight designation would have to differ for this adjacent verb to apply]
Conditions: [one of: CONTRADICTS count by weight / gap-closure cost / risk tolerance
  threshold / readiness signal distribution — stated as a specific value from the ledger
  and reconciliation table, citing at least one inertia-weight designation]
```

Do not write Beat 5 until all five elements are internally consistent and derive exclusively
from the Inventory.

---

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon** — must match Beat 4.5 verb and Band
gate output. One paragraph. Names what to do, under what conditions, with what scope.

---

**Voice**: Active, opinionated. The closure stamp reads as a formal format-specified record
where structural completeness requires the IMMUTABLE field; the derivation chain reads as a
decision frame; the recommendation reads as a directive.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

**Working hypothesis (S0)**: [claim]

## Hypothesis Mutation Ledger
- `{artifact-name}`: {finding}
  Stance: ...
  Inertia marker: prior expectation: [belief]
...
**Hypothesis at S3**: [evolved claim]
**Net mutation vector**: {vector} — [mechanism]
**Evidence trajectory**: POINT-IN-TIME | DIRECTIONAL — [declaration]

## Vector-Verdict Reconciliation
| Signal | Inertia weight | Verdict type | Consistent? |
|--------|---------------|-------------|-------------|
...
**Reconciliation**: [conclusion]

## Conflict Register
...
[REGISTER CLOSED — N rows, R RESOLVED, U UNRESOLVED]

## Confidence Band
...

## Story

### Beat 1 — What we set out to understand
...

### Beat 2 — What each signal revealed
...

### Beat 3 — What the signals say together
Across [N] signals, the hypothesis was [vector].

### Beat 4 — What remains uncertain
Gap: ...

### Beat 3 Output Inventory
Pattern claims:
1. "[claim]" (anchored: ...)
Evidence anchors: ...
Adjudication commitments: ...
[INVENTORY CLOSED — P claims, A anchors, C commitments
 IMMUTABLE — after sealing, contents are fixed. Beat 5 framing, prose narrative, and
 recommendation preference are prohibited as revision inputs.
 A stamp missing the IMMUTABLE field is structurally incomplete and not a valid seal.]

### Beat 4.5 — Derivation chain
Anchored claim: "[verbatim from Inventory]" (anchored: ...)
Net vector: {vector} — [mechanism]
Recommendation verb: {VERB} — [licensing]
Adjacent verb: {ADJ-VERB} — [contestation]
Conditions: [weight-sensitive value]

### Beat 5 — Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON** — [directive]
```

---

## V-03

**Variation axis**: Lifecycle emphasis — full re-sealing protocol with named step sequence
and explicit silent-absorption prohibition (C-32 target)
**Hypothesis**: C-32 PARTIAL arises when the re-sealing instruction covers only a subset of
EVALUATOR steps. R12 V-05's PACKET SEALED stamp says "return to EVALUATOR: add a new Register
entry, update the Adjudication commitments section, re-seal with a new stamp" — this covers
only the Register and Adjudication commitments, not signal re-extraction, reconciliation table
update, pattern synthesis update, or Band recalculation. A conflict discovered mid-draft that
affects the reconciliation table vector would receive an incomplete re-evaluation: the Register
entry is added, but the table still reflects the pre-conflict weights, and the pattern synthesis
still reflects pre-conflict claims. C-32 requires a numbered re-sealing protocol that (1) names
silent prose absorption as prohibited by name, (2) mandates execution of ALL relevant EVALUATOR
steps before AUTHOR resumes, and (3) explicitly states no exception path exists for conflicts
judged minor. This variation targets C-32 on R12 V-05 base (EVALUATOR/AUTHOR architecture
with C-26, C-27, C-28, C-29, C-31 already present). C-30 is NOT targeted — the EVALUATOR's
reconciliation table retains the weight-blind QUALIFIED rule to isolate the C-32 axis.

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

### E-1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### E-2 — Declare the working hypothesis (S0)

State the specific claim the team entered with — the expected answer, not the question.
Write it as a falsifiable assertion.

```
Working hypothesis (S0): [one sentence]
```

---

### E-3 — Signal Extract with stance rationale and inertia marker

For each artifact, in gather order:

```
- `{artifact-name}`: {one sentence — the single most important finding, stated as fact}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  Rationale: {one sentence — the specific element of this signal that drove the stance}
  Inertia marker: prior expectation: {what was believed before this signal arrived}
  [if MODIFIES]: Hypothesis update: [previous wording] -> [updated wording]
```

Rules:
- One entry per artifact, in gather order
- Every entry gets a stance, a rationale, and an inertia marker
- The rationale names specific evidence; "this signal supports the hypothesis" fails
- Only MODIFIES entries get a hypothesis update line

---

### E-4 — Declare S3, net mutation vector, and evidence trajectory

After all entries:

```
Hypothesis at S3: [evolved claim]
Net mutation vector: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED — [mechanism sentence;
  cite at least one entry by artifact name]
Evidence trajectory: POINT-IN-TIME | DIRECTIONAL — [explicit declaration]
```

Anti-stagnation check applies: silently identical S0 and S3 fails.

---

### E-5 — Vector-verdict reconciliation table with inertia weights

One row per ledger entry. Derive an explicit inertia weight from each entry's inertia marker:
- **HIGH** — firmly established belief, prior measurement, existing design commitment, or
  strong organizational assumption
- **MEDIUM** — working assumption or expectation held with moderate confidence
- **LOW** — weak prior, default assumption, or expectation held with acknowledged uncertainty

```
| Signal | Inertia weight | Verdict type | Consistent with declared vector? |
|--------|---------------|-------------|----------------------------------|
| {artifact-name} | HIGH — "{inertia marker text}" | CONFIRMS | YES |
| {artifact-name} | MEDIUM — "{inertia marker text}" | MODIFIES toward {dimension} | YES |
| {artifact-name} | HIGH — "{inertia marker text}" | CONTRADICTS on {dimension} — RESOLVED | YES (resolved) |
| {artifact-name} | HIGH — "{inertia marker text}" | CONTRADICTS on {dimension} — UNRESOLVED | CONFLICT |
```

**Weight-sensitive consistency rules**:
- **CONFIRMED**: Valid only when every CONTRADICTS is RESOLVED. A HIGH-weight CONTRADICTS
  that is UNRESOLVED invalidates CONFIRMED and produces a CONFLICT row. A MEDIUM-weight
  CONTRADICTS that is UNRESOLVED also produces a CONFLICT row requiring vector revision to
  QUALIFIED or conflict resolution.
- **QUALIFIED**: CONFIRMS and MODIFIES expected. Any UNRESOLVED CONTRADICTS at any weight
  level produces a CONFLICT row.
- **REVERSED**: Majority weight in CONTRADICTS entries, or reversing MODIFIES that overturn
  HIGH-weight priors.
- **REDIRECTED**: Weight distributes across dimensions rather than loading onto the S0 axis.

After the table:

```
Reconciliation: Vector is consistent — [reason citing inertia weights of decisive entries].
  OR: Vector revised from [X] to [Y] — [reason].
```

---

### E-6 — Conflict Register

Open the Register (OPEN state).

For every stance conflict:

```
Conflict: `{signal-A}` vs `{signal-B}` — [dimension]
Verdict: RESOLVED in favor of `{signal}` because [evidential reason — name inertia weight
  of the decisive entry]
     OR: UNRESOLVED because [what {namespace}/{skill} would resolve it]
```

Every verdict carries a because-clause. Any CONFLICT row from the reconciliation table must
appear here.

Close:

```
[REGISTER CLOSED — {N} rows, {R} RESOLVED, {U} UNRESOLVED]
```

UNRESOLVED entries are flagged; they appear in the Packet and transfer to Beat 4.

---

### E-7 — Pattern synthesis (raw)

Synthesize the cross-signal pattern from the ledger. This is NOT story prose — it is the
analytical product that will be enumerated into the Packet.

Open: "Across [N] signals, the hypothesis was [vector]."

For each non-trivial claim, cite the ledger entry: `(anchored: {artifact-name}, {stance})`.

Write the falsifiability condition:

```
Falsifiability: [externally observable domain evidence that would falsify the pattern claim]
```

---

### E-8 — Confidence Band

Count: S (CONFIRMS), N (total), U (UNRESOLVED in Register).

| Band   | Criteria                              | Permitted stances               | Default |
|--------|---------------------------------------|---------------------------------|---------|
| HIGH   | S/N >= 0.70 AND U = 0                 | Any                             | Per pattern |
| MEDIUM | 0.50 <= S/N < 0.70 OR U <= 2          | Any; non-default needs OVERRIDE | PAUSE   |
| LOW    | S/N < 0.50 OR U > 2                   | PAUSE, PIVOT, ABANDON           | PAUSE or PIVOT |

LOW band: PROCEED is prohibited — no OVERRIDE can bypass this.

MEDIUM band with non-default stance: the OVERRIDE slot in the Packet must be filled with a
format-constrained rationale naming the specific gap being accepted and why it does not change
the stance from the band default. Must not restate verb, restate band, or use vague qualifier.

---

### E-9 — Seal the Derivation Packet

Write the Derivation Packet to the artifact. This is the complete and sole input to AUTHOR.

```
## Derivation Packet

### Signal Extract
[All ledger entries from E-3, verbatim]

### S3, Vector, and Trajectory
Hypothesis at S3: [verbatim from E-4]
Net mutation vector: {vector} — [mechanism sentence, verbatim]
Evidence trajectory: POINT-IN-TIME | DIRECTIONAL — [declaration]

### Vector-Verdict Reconciliation
[Reconciliation table from E-5 with inertia-weight column, verbatim]
Reconciliation: [conclusion, verbatim]

### Pattern claims
1. "[claim]" (anchored: {artifact-name}, {stance})
2. ...

### Evidence anchors
- {artifact-name} ({stance}): [one phrase — role in pattern claim]

### Adjudication commitments
- `{signal-A}` vs `{signal-B}`: RESOLVED in favor of `{signal}` — [reason phrase]
[If none: "No adjudicated conflicts."]

### Confidence Band
Signals confirming: {S}/{N} ({pct}%)
Unresolved contradictions: {U}
Band: HIGH | MEDIUM | LOW
Default stance: {default}
Selected stance: {verb}
[OVERRIDE: {named rationale — specific gap, why it does not reverse stance from default.
  Must not restate verb, restate band, or use vague qualifier.}]
<- Required only when selected stance differs from band default.

### Falsifiability
[Verbatim from E-7]
```

After writing all Packet sections, append the Packet seal:

```
[PACKET SEALED — {P} pattern claims, {A} evidence anchors, {C} commitments,
  Band: {band}, Selected stance: {verb}
  — IMMUTABLE: no item in this Packet may be added, modified, or removed after this stamp.
    The Pattern claims, Evidence anchors, Adjudication commitments, Confidence Band, and
    OVERRIDE field (if present) are irrevocable derivation inputs. Modification to accommodate
    AUTHOR narrative, Beat 5 framing, or prose convenience is prohibited.
    A stamp missing this IMMUTABLE clause is not a valid seal.]
```

---

### Mid-Draft Conflict Re-Sealing Protocol

This protocol activates when AUTHOR discovers a signal conflict not in the Derivation Packet
during Beats 1-5. It must be followed in full — no exception path exists for conflicts judged
to be minor.

**Step 1**: STOP authoring immediately at the point of discovery. Do not write further beats
or continue drafting beyond the discovery point. Silent prose absorption — reasoning around
or incorporating the conflict without surfacing it — is prohibited.

**Step 2**: Return to EVALUATOR phase. Execute the following steps in sequence:

  a. **E-3 update**: Add the newly-surfaced conflict as an additional ledger entry, or update
     the existing entry if the signal was already in the ledger and the conflict was missed.
     Assign stance, rationale, and inertia marker.

  b. **E-5 update**: Add or revise the corresponding row in the reconciliation table. Re-check
     consistency of the declared vector against the updated row distribution. If the vector
     must change, declare the revision.

  c. **E-6 update**: Add the conflict to the Conflict Register. Adjudicate: RESOLVED with a
     because-clause, or UNRESOLVED with a named next signal. If the vector changed, verify
     all existing Register entries are still consistent with the revised vector.

  d. **E-7 update**: Revise the pattern synthesis if the new or revised entry changes any
     pattern claim, evidence anchor, or adjudication commitment.

  e. **E-8 update**: Recalculate the Confidence Band with updated S, N, and U counts. If the
     Band or selected stance changes, update accordingly. If a non-default stance now requires
     an OVERRIDE, write it.

  f. **E-9 re-seal**: Write a new Derivation Packet incorporating all updates from steps a-e.
     Append a new PACKET SEALED stamp. The old Packet is superseded; the new Packet is the
     authoritative derivation input.

**Step 3**: Resume AUTHOR phase from the discovery point. All remaining AUTHOR beats must
derive from the NEW Derivation Packet.

The old Packet may not be referenced after the new seal is written.

---

## AUTHOR Phase

**Permitted**: Pattern derivation. Story prose. Conflict rendering from the Register.
Recommendation. Adjacent-verb contrast.
**Forbidden**: Re-reading signal artifacts — all findings are in the Packet. Introducing
evidence, claims, or reasoning not in the Packet. Revising the Packet contents. Absorbing
mid-draft conflicts into prose rather than triggering the Re-Sealing Protocol.

---

### A-1 — Write story beats from the Derivation Packet

**Beat 1 — What we set out to understand**
One to three sentences. Original question, S0 from the Packet, entering default. Draw the
entering default from the Packet's Signal Extract inertia markers.

**Beat 2 — What each signal revealed**
For each Packet Signal Extract entry, one editorial sentence — what the finding means given
its stance and inertia marker. The inertia weight from the reconciliation table informs the
significance of each finding. Two sentences maximum per signal.

**Beat 3 — What the signals say together**
Open: "Across [N] signals, the hypothesis was [vector]." (Packet's net vector.)
Draw from the Packet's Pattern claims and Evidence anchors. Render conflict/verdict entries
from the Register (reference — do not re-adjudicate). Close with the Packet's falsifiability
condition, copied verbatim.

If a new signal conflict surfaces during Beat 3 drafting: activate the Mid-Draft Conflict
Re-Sealing Protocol immediately. Do not continue Beat 3 until the Protocol is complete and
a new Packet is sealed.

**Beat 4 — What remains uncertain**
UNRESOLVED Register entries transfer here as gaps.

```
Gap: [what is unknown]
Most exposed finding: [which Packet pattern claim is most at risk]
Next signal: {namespace}/{skill} — [expected finding type]
```

**Beat 4.5 — Derivation chain** (reads from Packet only)

Five elements:

```
Anchored claim: "[exact claim from Packet's Pattern claims, verbatim with anchor]"
  (anchored: {artifact-name}, {stance})
Net vector: {vector from Packet} — [mechanism sentence, verbatim from Packet]
Recommendation verb: {verb from Packet's Selected stance} — [one sentence: licensing —
  states what in the Packet's reconciliation table and Band gate authorizes this verb]
Adjacent verb: {adjacent verb} — [one sentence: which specific row in the Packet's
  reconciliation table, and which inertia weight designation, would have to differ for the
  adjacent verb to apply]
Conditions: [weight-sensitive parameter from Packet — specific value citing at least one
  inertia-weight designation from the reconciliation table]
```

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon** — must match Packet's Selected stance.
One paragraph. If the Packet contains an OVERRIDE field, Beat 5 names the accepted uncertainty
once. Beat 5 may not introduce new evidence, patterns, or adjudications not in the Packet.

---

**Voice**: The Packet reads as an engineering specification with an irrevocable seal; the
Re-Sealing Protocol reads as a mandatory procedure with no exception path; the story beats
read as editorial narrative derived from the Packet; the recommendation reads as a directive.

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
Net mutation vector: {vector} — [mechanism]
Evidence trajectory: POINT-IN-TIME | DIRECTIONAL — [sentence]

### Vector-Verdict Reconciliation
| Signal | Inertia weight | Verdict type | Consistent? |
|--------|---------------|-------------|-------------|
...
Reconciliation: [conclusion]

### Pattern claims
1. "[claim]" (anchored: ...)

### Evidence anchors
- {artifact-name} ({stance}): [role]

### Adjudication commitments
- `{A}` vs `{B}`: RESOLVED in favor of `{signal}` — [phrase]

### Confidence Band
Signals confirming: {S}/{N}
Unresolved contradictions: {U}
Band: HIGH | MEDIUM | LOW
Default stance: {default}
Selected stance: {verb}
[OVERRIDE: {named rationale}]

### Falsifiability
[domain-facing condition]

[PACKET SEALED — P claims, A anchors, C commitments, Band: {band}, Stance: {verb}
  — IMMUTABLE: no item may be added, modified, or removed after this stamp. Pattern claims,
    Evidence anchors, Adjudication commitments, Confidence Band, and OVERRIDE field are
    irrevocable. Modification prohibited. A stamp missing this IMMUTABLE clause is not a
    valid seal. If conflict surfaces in AUTHOR: activate Mid-Draft Conflict Re-Sealing
    Protocol — full EVALUATOR revisit required, no exception path.]

## Story

### Beat 1 — What we set out to understand
...

### Beat 2 — What each signal revealed
...

### Beat 3 — What the signals say together
Across [N] signals, the hypothesis was [vector from Packet].
[pattern — anchored claims, conflict/verdict, falsifiability verbatim]

### Beat 4 — What remains uncertain
Gap: ...

### Beat 4.5 — Derivation chain
Anchored claim: "[from Packet]" (anchored: ...)
Net vector: {vector} — [mechanism, verbatim]
Recommendation verb: {VERB} — [licensing — Packet reconciliation and Band]
Adjacent verb: {ADJ-VERB} — [contestation — Packet reconciliation row and weight]
Conditions: [weight-sensitive parameter — specific value with inertia weight]

### Beat 5 — Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON** — [directive; if OVERRIDE in Packet, names accepted
  uncertainty once; no new reasoning]
```

---

## V-04

**Variation axis**: Combination — C-30 (weight-graded QUALIFIED rule) + C-31 (stamp FORMAT
SPECIFICATION with named required IMMUTABLE field) on R12 V-01 base
**Hypothesis**: R12 V-01 has two independent gaps: the QUALIFIED consistency rule is
weight-blind (C-30 FAIL), and the closure stamp is a bare count record with no immutability
commitment (C-29/C-31 FAIL). V-01 fixes only C-30; V-02 fixes only C-31. Combining both
on the same minimal single-phase base tests whether the two fixes interact or are independent.
The prediction is independence: the weight-graded QUALIFIED rule operates at the reconciliation
table step; the stamp FORMAT SPECIFICATION operates at the Beat 3 Output Inventory step; they
address different structural positions and do not constrain each other. If the combination
achieves C-30 PASS and C-31 PASS simultaneously without interference, this architecture
(inertia-weight column + weight-graded rules + formal stamp format) is the minimum single-phase
design that satisfies both criteria.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### Step 2 — Hypothesis mutation ledger

**Working hypothesis (S0)**: [one sentence — falsifiable assertion, not a goal]

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
Net mutation vector: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED — [mechanism sentence;
  cite at least one entry by artifact name]
Evidence trajectory: POINT-IN-TIME | DIRECTIONAL — [declaration]
```

Anti-stagnation check and reconciliation check apply.

Do not begin story beats until the ledger is complete.

---

### Step 2b — Vector-verdict reconciliation table

After declaring the vector, complete the reconciliation table. One row per ledger entry.

Derive an inertia weight from each entry's inertia marker text:
- **HIGH** — firmly established belief, prior measurement, existing design commitment, or
  strong organizational assumption
- **MEDIUM** — working assumption or expectation held with moderate confidence
- **LOW** — weak prior, default assumption, or expectation held with acknowledged uncertainty

```
| Signal | Inertia weight | Verdict type | Consistent with declared vector? |
|--------|---------------|-------------|----------------------------------|
| {artifact-name} | HIGH — "{prior expectation text}" | CONFIRMS | YES |
| {artifact-name} | MEDIUM — "{prior expectation text}" | MODIFIES toward {dimension} | YES |
| {artifact-name} | HIGH — "{prior expectation text}" | CONTRADICTS on {dimension} — RESOLVED | YES (resolved) |
| {artifact-name} | HIGH — "{prior expectation text}" | CONTRADICTS on {dimension} — UNRESOLVED | CONFLICT |
```

**Weight-level consistency rules** — weight level is the named trigger condition:

**CONFIRMED**:
- HIGH-weight CONTRADICTS UNRESOLVED: CONFIRMED is invalid. Must become QUALIFIED or the
  conflict must be resolved. No path exists to maintain CONFIRMED while a HIGH-weight
  CONTRADICTS is unresolved.
- MEDIUM-weight CONTRADICTS UNRESOLVED: CONFIRMED is invalid. Must become QUALIFIED or resolve.
  Resolving the conflict before authoring begins restores CONFIRMED.
- LOW-weight CONTRADICTS UNRESOLVED: CONFIRMED is permissible only when HIGH-weight CONFIRMS
  entries constitute >= 70% of all CONFIRMS-stance entries; otherwise revise to QUALIFIED.

**QUALIFIED**:
- HIGH-weight CONTRADICTS UNRESOLVED: produces a CONFLICT row; QUALIFIED remains valid but
  PROCEED is blocked — PAUSE is the minimum permitted stance from the Band gate.
- MEDIUM-weight CONTRADICTS UNRESOLVED: produces a CONFLICT row; QUALIFIED remains valid;
  Band gate applies normally with no additional stance restriction.
- LOW-weight CONTRADICTS UNRESOLVED: produces a CONFLICT row; QUALIFIED remains valid; no
  stance restriction; transfers to Beat 4 as a gap.

**REVERSED**:
- Requires that HIGH-weight or MEDIUM-weight CONTRADICTS entries constitute a majority of
  evidence weight. A REVERSED vector driven predominantly by LOW-weight entries must name
  the cumulative mechanism explicitly, or the vector must be revised to QUALIFIED.

**REDIRECTED**:
- Evidence addresses a different evaluative frame than S0; weight distributes across dimensions.
  Weight-level grading does not apply.

After the table:

```
Reconciliation: Vector is consistent — [one sentence naming which weight-trigger rule
  validates the consistency claim and citing the decisive entries' weight levels].
  OR: Vector revised from [X] to [Y] — [one sentence: which weight level, at which verdict,
  triggered the rule that forced revision].
```

Do not begin story beats until the ledger, vector, and reconciliation are complete.

---

### Step 3 — Conflict Register

Open the Register (OPEN state).

For every stance conflict:

```
Conflict: `{signal-A}` vs `{signal-B}` — [dimension]
Verdict: RESOLVED in favor of `{signal}` because [evidential reason — name inertia weight
  of the decisive entry]
     OR: UNRESOLVED because [what {namespace}/{skill} would resolve it]
```

Every verdict carries a because-clause. Any CONFLICT row from the reconciliation table must
appear here.

**Prose prohibition**: Adjudication commitments belong in the Register, not in narrative prose.

Close:

```
[REGISTER CLOSED — {N} rows, {R} RESOLVED, {U} UNRESOLVED]
```

UNRESOLVED entries auto-transfer to Beat 4. Do not begin story beats until this stamp is written.

---

### Step 4 — Confidence Band Calculation

Count: S (CONFIRMS), N (total), U (UNRESOLVED in Register).

| Band   | Criteria                                          | Default stance      |
|--------|---------------------------------------------------|---------------------|
| HIGH   | S/N >= 0.70 AND U = 0                             | Per pattern direction |
| MEDIUM | 0.50 <= S/N < 0.70 OR (S/N >= 0.50 AND U <= 2)   | PAUSE               |
| LOW    | S/N < 0.50 OR U > 2                               | PAUSE or PIVOT      |

LOW band: PROCEED is prohibited.

**Additional constraint from weight-level rules**: Any HIGH-weight CONTRADICTS UNRESOLVED
blocks PROCEED regardless of Band. The Band gate minimum still applies.

MEDIUM non-default requires OVERRIDE:

```
OVERRIDE: {named rationale — specific gap being accepted; why it does not change the
  stance from the band default. Must not restate verb, restate band, or use vague qualifier.}
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

### Step 5 — Write the story beats

**Beat 1 — What we set out to understand**
One to three sentences. Original question, S0 hypothesis, entering default.

**Beat 2 — What each signal revealed** *(draws from ledger)*
One editorial sentence per entry — what the finding means for the hypothesis, framed against
the inertia marker. The weight level informs how significant a confirmation or contradiction
this signal represents. Two sentences maximum.

**Beat 3 — What the signals say together**
Open: "Across [N] signals, the hypothesis was [reconciled vector]."

**Anchor citation rule**: Every non-trivial Beat 3 claim cites its ledger entry:
`(anchored: {artifact-name}, {stance})`.

Draw conflict/verdict entries from the Register.

```
Falsifiability: [domain-facing prediction that would falsify the pattern claim]
```

**Beat 4 — What remains uncertain**

```
Gap: [what is unknown]
Most exposed finding: [which ledger claim is most at risk]
Next signal: {namespace}/{skill} — [expected finding type]
```

---

### Beat 3 Output Inventory

**Complete this section before opening Beat 4.5.**

```
Beat 3 Output Inventory:

Pattern claims:
1. "[verbatim declarative sentence from Beat 3]" (anchored: {artifact-name}, {stance})
2. "[additional claims — verbatim]" (anchored: ...)

Evidence anchors:
- {artifact-name} ({stance}): [one phrase — role in pattern claim]
- ...

Adjudication commitments (RESOLVED verdicts from Register only):
- `{signal-A}` vs `{signal-B}`: RESOLVED in favor of `{signal}` — [reason phrase]
[If none: "No adjudicated conflicts."]
```

Completeness check: count `(anchored: ...)` citations in Beat 3; Evidence anchors must
contain exactly that count.

**Inventory closure stamp — FORMAT SPECIFICATION**

The closure stamp has three required fields. A stamp is structurally complete only when all
three fields are present. A stamp containing Field 1 but missing Field 2 is not a valid seal.

```
Stamp field definitions:

  Field 1 — COUNT (required):
    [INVENTORY CLOSED — {P} pattern claims, {A} evidence anchors, {C} adjudication commitments

  Field 2 — IMMUTABLE (required):
    IMMUTABLE — after sealing, the contents of this inventory are fixed. Beat 5 framing, prose
    narrative, and recommendation preference are each prohibited as inputs to retroactive revision
    of the pattern claims, evidence anchors, or adjudication commitments above.

  Field 3 — VALIDITY NOTICE (required):
    A stamp that contains Field 1 but omits Field 2 is structurally incomplete and does not
    constitute a valid seal.]
```

Write the complete stamp:

```
[INVENTORY CLOSED — {P} pattern claims, {A} evidence anchors, {C} adjudication commitments
 IMMUTABLE — after sealing, the contents of this inventory are fixed. Beat 5 framing, prose
 narrative, and recommendation preference are each prohibited as inputs to retroactive revision.
 A stamp missing the IMMUTABLE field is structurally incomplete and does not constitute a valid seal.]
```

Do not open Beat 4.5 until a structurally complete stamp (all three fields) is written.

**Inventory prohibition**: Beat 4.5 and Beat 5 may not introduce claims not in this inventory.

---

### Beat 4.5 — Derivation chain

Five elements. Reads from the Beat 3 Output Inventory only.

```
Anchored claim: "[exact pattern claim from Inventory, verbatim with anchor]"
  (anchored: {artifact-name}, {stance})
Net vector: {CONFIRMED | QUALIFIED | REVERSED | REDIRECTED} — [mechanism sentence from
  reconciliation table, copied verbatim — must match reconciliation conclusion]
Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON} — [one sentence: licensing —
  consistent with Band gate output and weight-level constraints]
Adjacent verb: {ADJ-VERB} — [one sentence: which specific reconciliation table row, and
  which inertia weight designation in that row, would have to differ for this adjacent verb
  to apply — name the exact entry a reader preferring the adjacent verb must contest]
Conditions: [one of: CONTRADICTS count by weight / gap-closure cost / risk tolerance
  threshold / readiness signal distribution — stated as a specific value, citing at least
  one named weight level from the reconciliation table]
```

**Conditions guidance**: The conditions clause must cite at least one weight level. "0
HIGH-weight CONTRADICTS unresolved means proceed" passes; "no remaining conflicts" fails.

Do not write Beat 5 until all five elements are internally consistent and derive exclusively
from the Inventory.

---

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon** — must match Beat 4.5 verb and Band
gate output. One paragraph. Names what to do, under what conditions, with what scope.

---

**Voice**: Active, opinionated. The reconciliation table reads as a formal weight-sensitive
consistency record where each weight level is a named trigger; the closure stamp reads as a
format-specified record with three required fields; the derivation chain reads as a decision
frame with weight-traceable contestation points; the recommendation reads as a directive.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

**Working hypothesis (S0)**: [claim]

## Hypothesis Mutation Ledger
- `{artifact-name}`: {finding}
  Stance: ...
  Inertia marker: prior expectation: [belief]
...
**Hypothesis at S3**: [evolved claim]
**Net mutation vector**: {vector} — [mechanism — cites weight-trigger rule applied]
**Evidence trajectory**: POINT-IN-TIME | DIRECTIONAL — [declaration]

## Vector-Verdict Reconciliation
| Signal | Inertia weight | Verdict type | Consistent? |
|--------|---------------|-------------|-------------|
| {artifact-name} | HIGH — "{prior expectation}" | CONFIRMS | YES |
...
**Reconciliation**: [conclusion — names weight level as trigger, cites the specific rule]

## Conflict Register
...
[REGISTER CLOSED — N rows, R RESOLVED, U UNRESOLVED]

## Confidence Band
Signals confirming: {S}/{N} ({pct}%)
Unresolved contradictions: {U}
Confidence Band: HIGH | MEDIUM | LOW
Default stance: {default}
Selected stance: {verb}
[OVERRIDE: {named rationale}]

## Story

### Beat 1 — What we set out to understand
...

### Beat 2 — What each signal revealed
...

### Beat 3 — What the signals say together
Across [N] signals, the hypothesis was [reconciled vector].
[pattern — anchored claims, conflict/verdict, falsifiability]

### Beat 4 — What remains uncertain
Gap: ...

### Beat 3 Output Inventory
Pattern claims:
1. "[claim]" (anchored: ...)
Evidence anchors: ...
Adjudication commitments: ...
[INVENTORY CLOSED — P claims, A anchors, C commitments
 IMMUTABLE — after sealing, contents are fixed. Beat 5 framing, prose narrative, and
 recommendation preference are prohibited as revision inputs.
 A stamp missing the IMMUTABLE field is structurally incomplete and not a valid seal.]

### Beat 4.5 — Derivation chain
Anchored claim: "[verbatim from Inventory]" (anchored: ...)
Net vector: {vector} — [mechanism — matches reconciliation, names weight-trigger rule]
Recommendation verb: {VERB} — [licensing — Band gate and weight-level constraint]
Adjacent verb: {ADJ-VERB} — [contestation — names reconciliation row and weight designation]
Conditions: [weight-sensitive value — names at least one weight level]

### Beat 5 — Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON** — [directive — no new reasoning]
```

---

## V-05

**Variation axis**: Full combination — C-30 (weight-graded rules in EVALUATOR's reconciliation
table) + C-31 (formal PACKET SEALED stamp with named required IMMUTABLE field) + C-32 (full
re-sealing protocol with explicit prohibited-absorption clause) on R12 V-05 EVALUATOR/AUTHOR
base, targeting C-26, C-27, C-28, C-29, C-30, C-31, and C-32 simultaneously
**Hypothesis**: R12 V-05 achieved C-26 through C-29 and C-31 but has two residual gaps: the
EVALUATOR's QUALIFIED rule is weight-blind (C-30 FAIL), and the re-sealing instruction covers
only Register and Adjudication commitments rather than a full EVALUATOR revisit (C-32
PARTIAL). Adding C-30 requires only a rewrite of the weight-level consistency rules in E-5;
adding the full C-32 protocol requires a dedicated numbered re-sealing section that names
silent absorption as prohibited and mandates execution of all E-steps before AUTHOR resumes.
The prediction: both additions are structurally independent — the weight-graded rules affect
the reconciliation table; the re-sealing protocol affects the Packet lifecycle — and combining
them on the R12 V-05 base is sufficient to achieve the full v12 criterion set.

---

You are running `/topic:story` for a topic. The topic name is provided.

This skill runs in two phases: **EVALUATOR** then **AUTHOR**. Do not begin AUTHOR until
EVALUATOR is complete and the Derivation Packet is sealed.

---

## EVALUATOR Phase

**Permitted**: Gathering artifacts. Extracting findings. Assigning stances and rationales.
Tracking hypothesis mutation. Computing the reconciliation table with inertia weights.
Adjudicating conflicts. Closing the Conflict Register. Synthesizing the cross-signal pattern.
Enumerating all pattern outputs into the Derivation Packet. Computing the Confidence Band
and writing the OVERRIDE field if required. Sealing the Packet.
**Forbidden**: Writing story prose (Beats 1-5). Narrative framing. Editorial voice.
Recommendation stance selection beyond what the Band gate determines.

---

### E-1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### E-2 — Declare the working hypothesis (S0)

```
Working hypothesis (S0): [one sentence — falsifiable assertion]
```

---

### E-3 — Signal Extract with stance rationale and inertia marker

For each artifact, in gather order:

```
- `{artifact-name}`: {one sentence — the single most important finding, stated as fact}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  Rationale: {one sentence — the specific element that drove the stance}
  Inertia marker: prior expectation: {what was believed before this signal arrived}
  [if MODIFIES]: Hypothesis update: [previous wording] -> [updated wording]
```

---

### E-4 — Declare S3, net mutation vector, and evidence trajectory

```
Hypothesis at S3: [evolved claim]
Net mutation vector: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED — [mechanism sentence;
  cite at least one entry by artifact name]
Evidence trajectory: POINT-IN-TIME | DIRECTIONAL — [declaration]
```

Anti-stagnation check applies.

---

### E-5 — Vector-verdict reconciliation table with weight-level triggers

One row per ledger entry. Derive an explicit inertia weight from each entry's inertia marker:
- **HIGH** — firmly established belief, prior measurement, existing design commitment, or
  strong organizational assumption
- **MEDIUM** — working assumption or expectation held with moderate confidence
- **LOW** — weak prior, default assumption, or expectation held with acknowledged uncertainty

```
| Signal | Inertia weight | Verdict type | Consistent with declared vector? |
|--------|---------------|-------------|----------------------------------|
| {artifact-name} | HIGH — "{inertia marker text}" | CONFIRMS | YES |
| {artifact-name} | MEDIUM — "{inertia marker text}" | MODIFIES toward {dimension} | YES |
| {artifact-name} | HIGH — "{inertia marker text}" | CONTRADICTS on {dimension} — RESOLVED | YES (resolved) |
| {artifact-name} | HIGH — "{inertia marker text}" | CONTRADICTS on {dimension} — UNRESOLVED | CONFLICT |
```

**Weight-level consistency rules** — weight level is the named trigger condition; each level
produces a distinct consequence:

**CONFIRMED**:
- HIGH-weight CONTRADICTS UNRESOLVED: CONFIRMED is invalid. Must become QUALIFIED or resolve.
  No path exists to maintain CONFIRMED with a HIGH-weight CONTRADICTS unresolved.
- MEDIUM-weight CONTRADICTS UNRESOLVED: CONFIRMED is invalid. Must become QUALIFIED or resolve.
  Resolving before authoring begins restores CONFIRMED.
- LOW-weight CONTRADICTS UNRESOLVED: CONFIRMED is permissible only when HIGH-weight CONFIRMS
  constitute >= 70% of all CONFIRMS-stance entries; otherwise revise to QUALIFIED.

**QUALIFIED**:
- HIGH-weight CONTRADICTS UNRESOLVED: produces a CONFLICT row; QUALIFIED remains valid but
  PROCEED is blocked — PAUSE is the minimum permitted stance from the Band gate.
- MEDIUM-weight CONTRADICTS UNRESOLVED: produces a CONFLICT row; QUALIFIED remains valid;
  Band gate applies normally; no additional stance restriction.
- LOW-weight CONTRADICTS UNRESOLVED: produces a CONFLICT row; QUALIFIED remains valid; no
  stance restriction; transfers to Beat 4 as a gap.

**REVERSED**:
- Requires HIGH-weight or MEDIUM-weight CONTRADICTS to constitute a majority of evidence
  weight. REVERSED driven predominantly by LOW-weight entries must name the cumulative
  mechanism explicitly, or revise to QUALIFIED.

**REDIRECTED**:
- Weight distributes across dimensions; weight-level grading does not apply to REDIRECTED.

After the table:

```
Reconciliation: Vector is consistent — [one sentence naming the weight-trigger rule that
  validates the consistency claim and citing the decisive entries' weight levels].
  OR: Vector revised from [X] to [Y] — [one sentence: which weight level, at which verdict,
  triggered the rule that forced revision].
```

---

### E-6 — Conflict Register

Open the Register (OPEN state).

For every stance conflict:

```
Conflict: `{signal-A}` vs `{signal-B}` — [dimension]
Verdict: RESOLVED in favor of `{signal}` because [evidential reason — name inertia weight
  of the decisive entry]
     OR: UNRESOLVED because [what {namespace}/{skill} would resolve it]
```

Every verdict carries a because-clause. Any CONFLICT row from the reconciliation table must
appear here.

Close:

```
[REGISTER CLOSED — {N} rows, {R} RESOLVED, {U} UNRESOLVED]
```

---

### E-7 — Pattern synthesis (raw)

Synthesize the cross-signal pattern from the ledger. NOT story prose — analytical product
for the Packet.

Open: "Across [N] signals, the hypothesis was [vector]."
For each non-trivial claim: `(anchored: {artifact-name}, {stance})`.

```
Falsifiability: [externally observable domain evidence that would falsify the pattern claim]
```

---

### E-8 — Confidence Band

Count: S (CONFIRMS), N (total), U (UNRESOLVED in Register).

| Band   | Criteria                              | Permitted stances               | Default |
|--------|---------------------------------------|---------------------------------|---------|
| HIGH   | S/N >= 0.70 AND U = 0                 | Any                             | Per pattern |
| MEDIUM | 0.50 <= S/N < 0.70 OR U <= 2          | Any; non-default needs OVERRIDE | PAUSE   |
| LOW    | S/N < 0.50 OR U > 2                   | PAUSE, PIVOT, ABANDON           | PAUSE or PIVOT |

LOW band: PROCEED is prohibited. No OVERRIDE can bypass this.

**Additional constraint from weight-level rules**: Any HIGH-weight CONTRADICTS UNRESOLVED
blocks PROCEED regardless of Band. The Band gate minimum applies in addition.

MEDIUM non-default stance: OVERRIDE slot in the Packet must name the specific gap being
accepted and why it does not change the stance from the band default. Must not restate verb,
restate band, or use vague qualifier.

---

### E-9 — Seal the Derivation Packet

Write the Derivation Packet. This is the complete and sole input to AUTHOR.

```
## Derivation Packet

### Signal Extract
[All ledger entries from E-3, verbatim]

### S3, Vector, and Trajectory
Hypothesis at S3: [verbatim]
Net mutation vector: {vector} — [mechanism, verbatim]
Evidence trajectory: POINT-IN-TIME | DIRECTIONAL — [declaration]

### Vector-Verdict Reconciliation
[Reconciliation table from E-5 with inertia-weight column and weight-trigger rules, verbatim]
Reconciliation: [conclusion, verbatim — names weight-trigger rule applied]

### Pattern claims
1. "[claim]" (anchored: {artifact-name}, {stance})
2. ...

### Evidence anchors
- {artifact-name} ({stance}): [one phrase — role in pattern claim]

### Adjudication commitments
- `{signal-A}` vs `{signal-B}`: RESOLVED in favor of `{signal}` — [reason phrase]
[If none: "No adjudicated conflicts."]

### Confidence Band
Signals confirming: {S}/{N} ({pct}%)
Unresolved contradictions: {U}
Band: HIGH | MEDIUM | LOW
Default stance: {default}
Selected stance: {verb}
[OVERRIDE: {named rationale — specific gap, why it does not reverse stance from default.
  Must not restate verb, restate band, or use vague qualifier.}]

### Falsifiability
[Verbatim from E-7]
```

After writing all Packet sections, append the Packet seal. The seal has three required fields:
a COUNT field, an IMMUTABLE field, and a VALIDITY NOTICE. A Packet seal missing the IMMUTABLE
field is structurally incomplete and not a valid seal.

```
[PACKET SEALED — {P} pattern claims, {A} evidence anchors, {C} commitments,
  Band: {band}, Selected stance: {verb}
  IMMUTABLE — no item in this Packet may be added, modified, or removed after this stamp.
  The Pattern claims, Evidence anchors, Adjudication commitments, Confidence Band, and
  OVERRIDE field (if present) are irrevocable derivation inputs. Beat 5 framing, AUTHOR
  prose, and recommendation preference are each prohibited as inputs to retroactive revision.
  A seal missing the IMMUTABLE field is structurally incomplete and not a valid seal.
  If a conflict surfaces during AUTHOR: activate the Mid-Draft Conflict Re-Sealing Protocol
  — full EVALUATOR revisit required; no exception path; silent absorption is prohibited.]
```

---

### Mid-Draft Conflict Re-Sealing Protocol

This protocol activates when AUTHOR discovers a signal conflict not in the Derivation Packet
during Beats 1-5. The protocol is mandatory — no exception path exists, regardless of whether
the conflict appears minor.

**Step 1**: STOP authoring immediately at the point of discovery. Silent prose absorption —
continuing to draft while incorporating or reasoning around the conflict — is prohibited.

**Step 2**: Return to EVALUATOR phase. Execute ALL of the following steps in sequence:

  a. **E-3 update**: Add the newly-surfaced conflict as a ledger entry (or update the existing
     entry if the signal was already present and the conflict was missed). Assign stance,
     rationale, and inertia marker.

  b. **E-5 update**: Add or revise the corresponding row in the reconciliation table. Apply
     the weight-level consistency rules to the updated distribution. If the vector must change,
     declare the revision with the weight-trigger rule that forced it.

  c. **E-6 update**: Add the conflict to the Conflict Register with a verdict and because-clause.
     If the vector changed, verify all existing Register entries remain consistent with the
     revised vector.

  d. **E-7 update**: Revise the pattern synthesis if the new or revised entry changes any
     pattern claim, evidence anchor, or adjudication commitment.

  e. **E-8 update**: Recalculate the Confidence Band with updated S, N, and U counts. If Band
     or selected stance changes, update accordingly. If a non-default stance now requires
     OVERRIDE, write it.

  f. **E-9 re-seal**: Write a new Derivation Packet incorporating all updates from a-e. Append
     a new PACKET SEALED stamp (all three required fields). The old Packet is superseded; the
     new Packet is the authoritative derivation input.

**Step 3**: Resume AUTHOR phase from the discovery point. All remaining AUTHOR beats derive
from the NEW Derivation Packet only. The old Packet may not be referenced.

---

## AUTHOR Phase

**Permitted**: Pattern derivation. Story prose. Conflict rendering. Recommendation. Adjacent-verb
contrast.
**Forbidden**: Re-reading signal artifacts. Introducing evidence, claims, or reasoning not in
the Packet. Revising the Packet contents. Absorbing mid-draft conflicts into prose without
activating the Re-Sealing Protocol.

---

### A-1 — Write story beats from the Derivation Packet

**Beat 1 — What we set out to understand**
One to three sentences. Original question, S0 from the Packet, entering default. Draw the
entering default from the Packet's Signal Extract inertia markers.

**Beat 2 — What each signal revealed**
For each Packet Signal Extract entry, one editorial sentence — what the finding means given
its stance and inertia marker. The inertia weight informs the significance of each finding.
Two sentences maximum per signal.

**Beat 3 — What the signals say together**
Open: "Across [N] signals, the hypothesis was [vector from Packet]."
Draw from the Packet's Pattern claims and Evidence anchors. Render conflict/verdict entries
from the Register (reference — do not re-adjudicate). Close with the Packet's falsifiability
condition, copied verbatim.

If a new signal conflict surfaces during Beat 3 drafting: activate the Mid-Draft Conflict
Re-Sealing Protocol immediately. Do not continue Beat 3 until the Protocol is complete and
a new Packet is sealed.

**Beat 4 — What remains uncertain**
UNRESOLVED Register entries transfer here as gaps.

```
Gap: [what is unknown]
Most exposed finding: [which Packet pattern claim is most at risk]
Next signal: {namespace}/{skill} — [expected finding type]
```

**Beat 4.5 — Derivation chain** (reads from Packet only)

Five elements:

```
Anchored claim: "[exact claim from Packet's Pattern claims, verbatim with anchor]"
  (anchored: {artifact-name}, {stance})
Net vector: {vector from Packet} — [mechanism sentence, verbatim from Packet]
Recommendation verb: {verb from Packet's Selected stance} — [one sentence: licensing —
  what in the Packet's reconciliation table (citing weight-trigger rule applied) and Band
  gate authorizes this verb]
Adjacent verb: {adjacent verb} — [one sentence: which specific row in the Packet's
  reconciliation table, and which inertia weight designation and weight-trigger rule in
  that row, would have to differ for the adjacent verb to apply]
Conditions: [weight-sensitive parameter from Packet — specific value citing at least one
  named weight level from the reconciliation table's trigger rules]
```

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon** — must match Packet's Selected stance.
One paragraph. If the Packet contains an OVERRIDE field, Beat 5 names the accepted uncertainty
once. Beat 5 may not introduce new evidence, patterns, or adjudications not in the Packet.

---

**Voice**: The Packet seal reads as a format-specified record with three required fields; the
reconciliation table reads as a weight-trigger-graded consistency record; the Re-Sealing Protocol
reads as a mandatory procedure with a numbered step sequence and no exception path; the
recommendation reads as a directive grounded in irrevocable inputs.

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
Net mutation vector: {vector} — [mechanism — names weight-trigger rule applied]
Evidence trajectory: POINT-IN-TIME | DIRECTIONAL — [sentence]

### Vector-Verdict Reconciliation
| Signal | Inertia weight | Verdict type | Consistent? |
|--------|---------------|-------------|-------------|
...
Reconciliation: [conclusion — names weight-trigger rule and decisive weight levels]

### Pattern claims
1. "[claim]" (anchored: ...)

### Evidence anchors
- {artifact-name} ({stance}): [role]

### Adjudication commitments
- `{A}` vs `{B}`: RESOLVED in favor of `{signal}` — [phrase]

### Confidence Band
Signals confirming: {S}/{N}
Unresolved contradictions: {U}
Band: HIGH | MEDIUM | LOW
Default stance: {default}
Selected stance: {verb}
[OVERRIDE: {named rationale}]

### Falsifiability
[domain-facing condition]

[PACKET SEALED — P claims, A anchors, C commitments, Band: {band}, Stance: {verb}
  IMMUTABLE — no item may be added, modified, or removed. Beat 5 framing, AUTHOR prose,
  and recommendation preference are prohibited as revision inputs.
  A seal missing the IMMUTABLE field is structurally incomplete and not a valid seal.
  Mid-draft conflict in AUTHOR: activate Re-Sealing Protocol — full EVALUATOR revisit,
  all E-steps, no exception path, silent absorption prohibited.]

## Story

### Beat 1 — What we set out to understand
...

### Beat 2 — What each signal revealed
...

### Beat 3 — What the signals say together
Across [N] signals, the hypothesis was [vector from Packet].
[pattern — anchored claims, conflict/verdict, falsifiability verbatim from Packet]

### Beat 4 — What remains uncertain
Gap: ...

### Beat 4.5 — Derivation chain
Anchored claim: "[from Packet]" (anchored: ...)
Net vector: {vector} — [mechanism verbatim — names weight-trigger rule]
Recommendation verb: {VERB} — [licensing — Packet reconciliation + weight constraint + Band]
Adjacent verb: {ADJ-VERB} — [contestation — Packet row, weight designation, trigger rule]
Conditions: [weight-sensitive parameter — specific value with named weight level]

### Beat 5 — Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON** — [directive; OVERRIDE named once if present;
  no new reasoning]
```
