---
skill: quest-variate
skill_target: topic-story
date: 2026-03-15
round: 12
rubric: v11
---

# Variations — topic-story (Round 12)

Five complete, runnable skill body prompt variations.
Single-axis first (V-01 through V-03), then two combinations (V-04, V-05).

**Design context**: v11 rubric adds C-28 (Inertia Marker Row-Level Input) and C-29 (Sealed
Artifact Immutability). From Round 11:

- V-01 achieves C-26 via a named Beat 3 Output Inventory with closure stamp (R10 V-01 base).
- V-02 achieves C-27 via a format-constrained OVERRIDE field with explicit prohibitions in the
  Confidence Band Gate (R10 V-02 base).
- V-03 achieves both C-26 and C-27 via a two-phase RECORD/DERIVE architecture with a sealed
  Derivation Packet containing an OVERRIDE slot — but the immutability clause covers only the
  OVERRIDE field, not the full Packet.
- V-04 achieves C-26 and C-27 on R10 V-04 base (reconciliation table + 5-element derivation
  chain), but the reconciliation table's consistency rules operate on verdict categories
  (CONFIRMS / CONTRADICTS) without naming inertia marker values as row-level inputs.
- V-05 achieves C-26 and C-27 on R10 V-05 EVALUATOR/AUTHOR base, with the same reconciliation
  table verdict-category limitation.

**C-15 was consistent PARTIAL across V-03, V-04, V-05**: the Marker Lock mechanism (or
Vector-Verdict Reconciliation) enforced verdict-level consistency ("all CONTRADICTS must be
RESOLVED") but operated on verdict category labels derived from inertia markers — not on the
markers themselves. Two signals with identical verdict labels but different prior expectations
(one overturning a deeply held belief, one overturning a weak assumption) received identical
treatment. The lock's authority was traceable to the verdict category, not to the source marker.

**C-29 gap in V-04 and V-05**: Both achieve C-26 PASS via sealing stamps
(`[INVENTORY CLOSED — ...]`) but neither carries an explicit prohibition on post-sealing
modification. The stamp records what was enumerated; it does not bind the author to those
contents. An author who finds the sealed inventory inconvenient could silently revise it before
writing Beat 4.5 without triggering a visible violation.

**V-03 near-miss on C-29**: V-03's Derivation Packet carries "The OVERRIDE field is immutable
after sealing" — scoped to the OVERRIDE field specifically. C-29 requires immutability for the
entire enumeration artifact (all pattern claims, evidence anchors, adjudication commitments),
not only the exception-path field.

**Round 12 primary axes:**

C-28 fix: The reconciliation table (or equivalent Marker Lock check) must name inertia
markers as row-level inputs — each row cites the governing prior expectation text and derives
an explicit inertia weight (HIGH / MEDIUM / LOW) from it. The consistency rules then reference
inertia weight, not merely verdict label, so the lock's authority is traceable to the source
marker.

C-29 fix: The sealing stamp on the enumeration artifact must carry an explicit immutability
prohibition: "IMMUTABLE — contents may not be modified after sealing to accommodate narrative
preferences, recommendation stance, or prose convenience."

V-01 targets C-28 single-axis via an inertia-weight column added to the Vector-Verdict
Reconciliation table, with consistency rules updated to reference inertia weights. Base:
R11 V-04 (reconciliation table + 5-element derivation chain + Confidence Band).

V-02 targets C-29 single-axis via an explicit immutability constraint appended to the
Beat 3 Output Inventory closure stamp, with a list of named prohibitions. Base: R11 V-01
(the simplest architecture with Inventory but no reconciliation table).

V-03 targets C-28 via a structural alternative: a standalone "Marker Lock" section placed
after Beat 3 Output Inventory. Instead of embedding inertia weights in the reconciliation
table columns, V-03 keeps the reconciliation table as-is and adds a dedicated Marker Lock
section where each row maps (signal, inertia marker text, derived weight) → stance constraint
on the recommendation. The recommendation is prohibited from contradicting any HIGH-weight
marker without a named override. Base: R11 V-02 (Confidence Band Gate + OVERRIDE field).

V-04 combines V-01 (inertia-weight column in reconciliation table → C-28) with V-02
(immutability prohibition on Inventory seal → C-29) on R11 V-04 base.

V-05 is the full combination: EVALUATOR/AUTHOR phase architecture (R11 V-05 base) with
inertia-weight column in EVALUATOR's reconciliation table (C-28) and full-packet immutability
on the Derivation Packet seal (C-29), achieving C-26, C-27, C-28, and C-29 simultaneously.

---

## V-01

**Variation axis**: Output format — inertia-weight column in Vector-Verdict Reconciliation
table, with consistency rules referencing inertia weight per row (C-28 target)
**Hypothesis**: C-15 / C-28 are PARTIAL when the reconciliation table's consistency check
operates on verdict categories alone. R11 V-04's reconciliation table has columns
`Signal | Verdict type | Consistent with declared vector?` — the consistency rule "all
CONTRADICTS must be RESOLVED" applies identically to a HIGH-weight CONTRADICTS (the signal
contradicts a firmly held prior) and a LOW-weight CONTRADICTS (the signal contradicts a
weak assumption). The fix is to add an `Inertia weight` column that derives HIGH / MEDIUM /
LOW from the ledger entry's inertia marker text, and to restate consistency rules as
weight-sensitive: "a HIGH-weight CONTRADICTS that is UNRESOLVED prevents CONFIRMED; a
LOW-weight CONTRADICTS that is UNRESOLVED requires the vector to be at most QUALIFIED." The
row-level inertia weight makes the lock's authority traceable to the source marker, not to
the verdict label. This tests whether a single-column addition to the existing reconciliation
table structure achieves C-28 PASS without requiring changes to any other section.

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
[one sentence: which stances, on which dimension, drove this classification; cite at least
one ledger entry by artifact name]

Evidence trajectory: POINT-IN-TIME | DIRECTIONAL — [explicit declaration; an evaluator
cannot be required to infer this]
```

**Anti-stagnation check**: If S3 is identical to S0, state why explicitly. Silently
identical S0 and S3 fails.

**Reconciliation check**: CONFIRMED with visible unresolved CONTRADICTS, or REVERSED with
no CONTRADICTS, must be revised before proceeding.

Do not begin story beats until the ledger is complete.

---

### Step 2b — Vector-verdict reconciliation table

After declaring the vector, complete the reconciliation table. One row per ledger entry.

For each entry, derive an inertia weight from the inertia marker text:
- **HIGH** — the inertia marker names a firmly established belief, a prior measurement, an
  existing design commitment, or a strong organizational assumption
- **MEDIUM** — the inertia marker names a working assumption, a plausible expectation, or a
  belief held with moderate confidence
- **LOW** — the inertia marker names a weak prior, a default assumption, or an expectation
  held with acknowledged uncertainty

```
| Signal | Inertia weight | Verdict type | Consistent with declared vector? |
|--------|---------------|-------------|----------------------------------|
| {artifact-name} | HIGH — "{prior expectation text, quoted or paraphrased}" | CONFIRMS | YES |
| {artifact-name} | MEDIUM — "{prior expectation text}" | MODIFIES toward {dimension} | YES |
| {artifact-name} | HIGH — "{prior expectation text}" | CONTRADICTS on {dimension} — RESOLVED | YES (resolved) |
| {artifact-name} | HIGH — "{prior expectation text}" | CONTRADICTS on {dimension} — UNRESOLVED | CONFLICT |
```

**Consistency rules (weight-sensitive)**:
- **CONFIRMED**: Valid only when every CONTRADICTS entry is RESOLVED. A HIGH-weight
  CONTRADICTS that is UNRESOLVED always produces a CONFLICT row — CONFIRMED is invalid
  until it is resolved. A MEDIUM-weight CONTRADICTS that is UNRESOLVED also produces a
  CONFLICT row; the vector must be revised to QUALIFIED or the conflict resolved. A
  LOW-weight CONTRADICTS that is UNRESOLVED is a CONFLICT row and warrants revision to
  QUALIFIED unless a majority of HIGH-weight entries CONFIRM.
- **QUALIFIED**: CONFIRMS and MODIFIES entries expected. A CONTRADICTS entry is permissible
  only if RESOLVED. An UNRESOLVED CONTRADICTS at any weight level produces a CONFLICT row.
- **REVERSED**: A majority weight of CONTRADICTS entries, or reversing MODIFIES that overturn
  HIGH-weight priors. CONFIRMS entries must be in the minority by weight.
- **REDIRECTED**: Signal entries address a different evaluative frame than S0 posed; weight
  is distributed across dimensions rather than loading onto the S0 axis.

After the table:

```
Reconciliation: Vector is consistent — [reason citing inertia weights of decisive entries].
  OR: Vector revised from [X] to [Y] — [reason: which inertia weights at which verdict
  levels forced the revision].
```

Do not begin story beats until the ledger, vector, and reconciliation are all complete.

---

### Step 3 — Conflict Register

Open the Conflict Register (OPEN state).

For every pair of signal entries with opposing stances on the same dimension:

```
Conflict: `{signal-A}` vs `{signal-B}` — [dimension]
Verdict: RESOLVED in favor of `{signal}` because [specific evidential reason — name the
  ledger element and its inertia weight that outweighs the alternative]
     OR: UNRESOLVED because [what {namespace}/{skill} signal would resolve it]
```

Every verdict carries a because-clause.

**Prose prohibition**: Adjudication commitments belong in the Register with because-clauses,
not in narrative prose.

Any CONFLICT row from the reconciliation table must appear here as a named entry.

Close the Register:

```
[REGISTER CLOSED — {N} rows, {R} RESOLVED, {U} UNRESOLVED]
```

UNRESOLVED entries auto-transfer to Beat 4 as gaps. Do not begin story beats until this
stamp is written.

---

### Step 4 — Confidence Band Calculation

Count from the ledger:
- **S** = count of artifacts with CONFIRMS stance
- **N** = total signal artifacts processed
- **U** = count of UNRESOLVED entries in the Conflict Register

Band determination:

| Band   | Criteria                                          | Default stance      |
|--------|---------------------------------------------------|---------------------|
| HIGH   | S/N >= 0.70 AND U = 0                             | Per pattern direction |
| MEDIUM | 0.50 <= S/N < 0.70 OR (S/N >= 0.50 AND U <= 2)   | PAUSE               |
| LOW    | S/N < 0.50 OR U > 2                               | PAUSE or PIVOT      |

Permitted stances by band:
- HIGH: any stance allowed
- MEDIUM: any stance allowed — non-default requires OVERRIDE
- LOW: PAUSE, PIVOT, or ABANDON only — PROCEED is prohibited

**OVERRIDE rule**: If the selected stance differs from the band default, write the OVERRIDE
field in the artifact:

```
OVERRIDE: {named rationale}
```

The named rationale must name the specific gap or uncertainty being accepted as an
acceptable risk, and state why that uncertainty does not change the stance from the band
default. It must not restate the verb, restate the confidence band, or use a vague qualifier.

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
One to three sentences. The original question, S0 hypothesis, and entering default: what the
team expected and why. The entering default anchors the inertia markers in the ledger.

**Beat 2 — What each signal revealed** *(draws from the ledger)*
For each ledger entry, one editorial sentence beyond the finding — what the finding means
for the hypothesis, framed against the inertia marker. The inertia weight (HIGH / MEDIUM /
LOW from the reconciliation table) informs how significant a surprise or confirmation this
signal represents. Two sentences maximum per signal.

**Beat 3 — What the signals say together**
Open: "Across [N] signals, the hypothesis was [reconciled vector]." The reconciliation table
validates this claim.

**Anchor citation rule**: Every non-trivial Beat 3 claim must cite its ledger entry inline:
`(anchored: {artifact-name}, {stance})`.

Draw conflict/verdict entries from the Register (already adjudicated — do not re-adjudicate
in prose).

**Falsifiability gate**:

```
Falsifiability: [externally observable evidence — in the world, market, or system under
  analysis — that would falsify the pattern claim if found. Not a provenance check on the
  signal set. A domain-facing prediction that could be wrong.]
```

**Beat 4 — What remains uncertain**
RESOLVED verdicts are not gaps. UNRESOLVED verdicts auto-transfer from the Register as gaps.

```
Gap: [what is unknown]
Most exposed finding: [which ledger claim is most at risk without this]
Next signal: {namespace}/{skill} — [expected finding type]
```

Adjudicated debates from Beat 3 are not gaps.

---

### Beat 3 Output Inventory

**Complete this section before opening Beat 4.5.**

Enumerate ALL Beat 3 outputs. Beat 4.5 reads from this inventory; Beat 5 derives from it.
No new claims may enter the derivation chain that do not appear here.

```
Beat 3 Output Inventory:

Pattern claims:
1. "[verbatim declarative sentence from Beat 3]" (anchored: {artifact-name}, {stance})
2. "[additional claims — verbatim, one per distinct claim]" (anchored: ...)

Evidence anchors:
- {artifact-name} ({stance}): [one phrase — role in pattern claim]
- ...
[Every anchored artifact from Beat 3 must appear here]

Adjudication commitments (RESOLVED verdicts from Register only):
- `{signal-A}` vs `{signal-B}`: RESOLVED in favor of `{signal}` — [reason phrase]
[If none: "No adjudicated conflicts."]
```

Completeness check: count `(anchored: ...)` citations in Beat 3. The Evidence anchors list
must contain exactly that count of entries.

Closure stamp:

```
[INVENTORY CLOSED — {P} pattern claims, {A} evidence anchors, {C} adjudication commitments]
```

Do not open Beat 4.5 until this stamp is written.

**Inventory prohibition**: Beat 4.5 and Beat 5 may not introduce claims not in this
inventory. Beat 5 is a derivation surface only.

---

### Beat 4.5 — Derivation chain

Five elements. Reads from the Beat 3 Output Inventory only.

```
Anchored claim: "[exact pattern claim from Inventory, verbatim with anchor]"
  (anchored: {artifact-name}, {stance})
Net vector: {CONFIRMED | QUALIFIED | REVERSED | REDIRECTED} — [mechanism sentence from
  reconciliation table, copied verbatim — must match reconciliation conclusion exactly]
Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON} — [one sentence: what licenses
  this verb — must be consistent with the Confidence Band gate output]
Adjacent verb: {ADJ-VERB} — [one sentence: what specific element of the signal evidence,
  inertia weight distribution, or reconciled vector value would have to differ for this
  adjacent verb to apply — name the exact claim a reader who prefers the adjacent verb
  must contest, referencing the reconciliation table row that is decisive]
Conditions: [one of: CONTRADICTS count by weight / gap-closure cost / risk tolerance
  threshold / readiness signal distribution — stated as a specific value from the ledger
  and reconciliation table, referencing at least one inertia-weight designation]
```

**Conditions guidance**: The conditions clause must name at least one inertia weight
value from the reconciliation table to satisfy C-28. "QUALIFIED with 0 HIGH-weight
CONTRADICTS remaining UNRESOLVED means proceed" passes; "QUALIFIED with no conflicts"
fails.

Do not write Beat 5 until all five elements are internally consistent and derive
exclusively from the Inventory.

**Beat 5 derivation prohibition**: Beat 5 may not introduce new evidence, new patterns, or
new adjudications not already in the Inventory.

---

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon** — must match Beat 4.5 verb and Band
gate output. One paragraph. Names what to do, under what conditions, with what scope. Does
not repeat the derivation chain.

---

**Voice**: Active, opinionated. The ledger and reconciliation table read as formal records;
the Inventory as a derivation input manifest; the derivation chain as a decision frame with
weight-sensitive contestation points; the recommendation as a directive.

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
**Net mutation vector**: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED — [mechanism]
**Evidence trajectory**: POINT-IN-TIME | DIRECTIONAL — [sentence]

## Vector-Verdict Reconciliation
| Signal | Inertia weight | Verdict type | Consistent? |
|--------|---------------|-------------|-------------|
| {artifact-name} | HIGH — "{prior expectation}" | CONFIRMS | YES |
| {artifact-name} | MEDIUM — "{prior expectation}" | CONTRADICTS — RESOLVED | YES (resolved) |
...
**Reconciliation**: [conclusion — references inertia weights of decisive entries]

## Conflict Register
Conflict: `{A}` vs `{B}` — [dimension]
Verdict: RESOLVED because [reason, naming inertia weight] OR UNRESOLVED because [what]
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
[pattern — anchored claims, conflict/verdict entries, falsifiability]

### Beat 4 — What remains uncertain
Gap: ...

### Beat 3 Output Inventory
Pattern claims:
1. "[claim]" (anchored: ...)
Evidence anchors:
- {artifact-name} ({stance}): [role]
Adjudication commitments:
- `{A}` vs `{B}`: RESOLVED in favor of `{signal}` — [phrase]
[INVENTORY CLOSED — P claims, A anchors, C commitments]

### Beat 4.5 — Derivation chain
Anchored claim: "[from Inventory, verbatim]" (anchored: ...)
Net vector: {vector} — [mechanism — matches reconciliation]
Recommendation verb: {VERB} — [licensing — consistent with Band gate]
Adjacent verb: {ADJ-VERB} — [contestation claim — references reconciliation table row]
Conditions: [named weight-sensitive parameter — specific value from ledger/reconciliation]

### Beat 5 — Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON** — [directive — no new reasoning]
```

---

## V-02

**Variation axis**: Output format — explicit immutability constraint on the Beat 3 Output
Inventory closure stamp (C-29 target)
**Hypothesis**: C-29 fails when a sealing stamp records the inventory contents but does not
bind the author to those contents. R11 V-01's closure stamp is
`[INVENTORY CLOSED — {P} pattern claims, {A} anchors, {C} commitments]` — it records what
was enumerated at sealing time, but it does not state that those contents are irrevocable.
An author who finds the sealed inventory inconvenient — a pattern claim that creates an
awkward derivation, an adjudication commitment that conflicts with preferred Beat 5 prose —
could silently revise the inventory before opening Beat 4.5, and the revised inventory would
still carry a valid-looking closure stamp. The fix is to append an explicit immutability
prohibition to the stamp itself, naming the specific modification paths that are closed: "no
item may be added, modified, or removed after this stamp." The prohibition must be part of
the stamp format — not a prose instruction elsewhere in the spec — so an evaluator who reads
the stamp alone can confirm the constraint is in force. This tests whether adding an
immutability clause to the stamp format, without changing the inventory structure or the
derivation chain architecture, achieves C-29 PASS.

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

### Step 3 — Conflict Register

Open the Conflict Register (OPEN state). The Register has a formal lifecycle: OPEN while
processing signals; CLOSED before story beats begin.

For every pair of signal entries with opposing stances on the same dimension:

```
Conflict: `{signal-A}` vs `{signal-B}` — [dimension]
Verdict: RESOLVED in favor of `{signal}` because [specific evidential reason]
     OR: UNRESOLVED because [what {namespace}/{skill} signal would resolve it]
```

Every verdict carries a because-clause. A verdict without a because-clause is not a verdict.

**Prose prohibition**: Adjudication commitments live in the Register. Do not carry verdict
reasoning into narrative prose — if a verdict is reached, it appears in the Register with
a because-clause, not distributed through story text.

After all conflicts are entered, close the Register:

```
[REGISTER CLOSED — {N} rows, {R} RESOLVED, {U} UNRESOLVED]
```

Do not open the story beats until this stamp is written. UNRESOLVED entries auto-seed
Beat 4 gaps.

---

### Step 4 — Write the story beats

**Beat 1 — What we set out to understand**
One to three sentences. The original question and the S0 working hypothesis. State the
entering default: what the team expected to confirm, and why that expectation was the
reasonable prior. The entering default anchors the inertia markers in the ledger.

**Beat 2 — What each signal revealed** *(draws from the ledger)*
For each ledger entry, one editorial sentence beyond the finding — what the finding means
for the hypothesis. Draw on the inertia marker to frame each finding against prior
expectation. Two sentences maximum per signal.

**Beat 3 — What the signals say together**
The cross-signal pattern. Reference at least two ledger entries.

Open with the net mutation vector:
"Across [N] signals, the hypothesis was [CONFIRMED / QUALIFIED / REVERSED / REDIRECTED]."
Then build the pattern from there.

**Anchor citation rule**: Every non-trivial claim in Beat 3 must cite the specific ledger
entry that licenses it, inline: `(anchored: {artifact-name}, {stance})`.

Draw conflict/verdict entries from the Conflict Register (already adjudicated — do not
re-adjudicate in prose).

**Falsifiability gate**:

```
Falsifiability: [one sentence naming observable evidence — external to the signal set,
  observable in the world, market, or system under analysis — that would falsify the
  pattern claim if found. Not a quality check on the signals; a domain-facing prediction.]
```

**Beat 4 — What remains uncertain**
RESOLVED verdicts are not gaps. UNRESOLVED verdicts auto-transfer from the Register as
gaps. Additional scoped uncertainties follow.

```
Gap: [what is unknown]
Most exposed finding: [which ledger entry's claim is most at risk without this]
Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

Adjudicated debates from Beat 3 are not gaps.

---

### Beat 3 Output Inventory

**Complete this section before opening Beat 4.5.**

This is an enumeration, not a summary. Every pattern claim, every evidence anchor, and
every adjudication commitment from Beat 3 must appear here. Beat 4.5 and Beat 5 may derive
only from items in this inventory. An item absent from the inventory cannot enter the
derivation chain.

```
Beat 3 Output Inventory:

Pattern claims:
1. "[verbatim declarative sentence from Beat 3 pattern]"
   (anchored: {artifact-name}, {stance})
2. "[additional pattern claims, if any — no paraphrase, copy verbatim]"
   (anchored: ...)
[One entry per distinct pattern claim made in Beat 3]

Evidence anchors:
- {artifact-name} ({stance}): [one phrase — its role in the pattern claims above]
- ...
[Every artifact cited with (anchored: ...) in Beat 3 must appear here]

Adjudication commitments (RESOLVED verdicts from Conflict Register only):
- `{signal-A}` vs `{signal-B}`: RESOLVED in favor of `{signal}` — [reason phrase]
- ...
[If no RESOLVED conflicts: "No adjudicated conflicts."]
[UNRESOLVED entries do not appear here — they are in Beat 4 as gaps]
```

**Completeness check**: Count the `(anchored: ...)` citations in Beat 3. The Evidence
anchors list must contain exactly that count of entries — one per cited artifact. An anchor
cited in Beat 3 but absent from the inventory is an error; return to Beat 3 and verify
before proceeding.

**Inventory closure stamp**: After the inventory is written, append the closure stamp:

```
[INVENTORY CLOSED — {P} pattern claims, {A} evidence anchors, {C} adjudication commitments
 — IMMUTABLE: no item in this inventory may be added, modified, or removed after this stamp.
   The contents of this inventory are the complete and irrevocable input to the derivation
   chain. Modification to accommodate prose narrative, recommendation preference, or Beat 5
   framing is prohibited.]
```

The immutability prohibition is part of the stamp. An inventory that carries the count stamp
without the prohibition clause is not sealed.

Do not open Beat 4.5 until this stamp is written.

**Inventory prohibition**: Beat 4.5 and Beat 5 may not introduce claims not in this
inventory. Beat 5 derives; it does not reason anew.

---

### Beat 4.5 — Derivation chain

Reads from the Beat 3 Output Inventory only. Do not introduce claims not in the Inventory.

Four elements, each on its own line:

```
Anchored claim: "[exact pattern claim from the Inventory, copied verbatim with anchor]"
  (anchored: {artifact-name}, {stance})
Net vector: {CONFIRMED | QUALIFIED | REVERSED | REDIRECTED} — [mechanism sentence from
  ledger, copied verbatim]
Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON} — [one sentence: what in the
  vector and gap profile licenses this specific verb]
Adjacent verb: {PROCEED | PAUSE | PIVOT | ABANDON} — [one sentence: what specific element
  of the signal evidence, verdict distribution, or net vector value would have to differ
  for this adjacent verb to apply — name the exact claim a reader who prefers the adjacent
  verb must contest]
```

**Adjacent verb guidance**: Adjacent pairs: PROCEED <-> PAUSE (confidence), PAUSE <-> PIVOT
(commitment), PIVOT <-> ABANDON (recovery).

Do not write Beat 5 until all four elements are internally consistent and draw exclusively
from the Inventory.

**Beat 5 derivation prohibition**: Beat 5 may not introduce new evidence, new patterns, or
new adjudications not already in the Inventory. Beat 5 is a derivation surface only.

---

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon** — must match the verb in Beat 4.5.
One paragraph. Beat 5 names what to do, under what conditions, and with what scope.
"Proceed with caution" without naming the caution fails.

---

**Voice**: Active, opinionated. The ledger reads as a formal record; the Register as an
adjudication log; the Inventory as a sealed derivation input manifest; the recommendation
as a directive.

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
**Net mutation vector**: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED — [mechanism]
**Evidence trajectory**: POINT-IN-TIME | DIRECTIONAL — [declaration sentence]

## Conflict Register
Conflict: `{A}` vs `{B}` — [dimension]
Verdict: RESOLVED because [reason] OR UNRESOLVED because [what]
...
[REGISTER CLOSED — N rows, R RESOLVED, U UNRESOLVED]

## Story

### Beat 1 — What we set out to understand
...

### Beat 2 — What each signal revealed
...

### Beat 3 — What the signals say together
Across [N] signals, the hypothesis was [vector].
[pattern — anchored claims, conflict/verdict entries, falsifiability]

### Beat 4 — What remains uncertain
Gap: ...
Most exposed finding: ...
Next signal: ...

### Beat 3 Output Inventory
Pattern claims:
1. "[claim]" (anchored: ...)
Evidence anchors:
- {artifact-name} ({stance}): [role]
Adjudication commitments:
- `{A}` vs `{B}`: RESOLVED in favor of `{signal}` — [phrase]
[INVENTORY CLOSED — P claims, A anchors, C commitments
 — IMMUTABLE: no item may be added, modified, or removed after this stamp. Contents are
   the irrevocable input to the derivation chain. Modification prohibited.]

### Beat 4.5 — Derivation chain
Anchored claim: "[from Inventory, verbatim]" (anchored: ...)
Net vector: {vector} — [mechanism]
Recommendation verb: {VERB} — [licensing sentence]
Adjacent verb: {ADJ-VERB} — [specific contestation claim]

### Beat 5 — Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON** — [directive — what to do, under what conditions;
  no new reasoning]
```

---

## V-03

**Variation axis**: Lifecycle emphasis — standalone Marker Lock section with per-row inertia
marker citations and weight-to-stance constraint mapping (C-28 target via structural
alternative to reconciliation table column)
**Hypothesis**: C-28 can be achieved through a dedicated Marker Lock section rather than
by embedding inertia weight as a column in the reconciliation table. The reconciliation
table's role is to validate the declared vector against the distribution of verdict types.
The Marker Lock's role is to constrain the recommendation stance given what the high-inertia
signals say. Separating these two functions may produce a cleaner structure: the table
certifies the vector is internally consistent; the Marker Lock certifies the recommendation
does not violate the inertia profile. In the Marker Lock, each row maps a signal to its
inertia marker text, its derived weight (HIGH / MEDIUM / LOW), its verdict, and the stance
constraint that combination implies. A recommendation that contradicts a HIGH-weight
CONFIRMS entry without a named override is a Marker Lock violation and is explicitly
prohibited. This tests whether the standalone section form achieves C-28 PASS when the
reconciliation table itself uses only verdict categories — i.e., whether C-28 is satisfiable
at the Marker Lock level rather than requiring modification to the reconciliation table.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### Step 2 — Hypothesis mutation ledger

**Working hypothesis (S0)**: [one sentence — falsifiable assertion]

For each signal artifact, in the order read:

```
- `{artifact-name}`: {key finding most relevant to S0, one to two sentences}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  Inertia marker: prior expectation: {what was believed before this signal arrived}
  [if MODIFIES]: Hypothesis update: [previous] -> [updated]
```

After all entries:

```
Hypothesis at S3: [evolved claim]
Net mutation vector: CONFIRMED | QUALIFIED | REVERSED | REDIRECTED — [mechanism sentence]
Evidence trajectory: POINT-IN-TIME | DIRECTIONAL — [declaration]
```

Anti-stagnation check and reconciliation check apply.

Do not begin story beats until the ledger is complete.

---

### Step 3 — Conflict Register

Open the Register (OPEN state).

For every stance conflict:

```
Conflict: `{signal-A}` vs `{signal-B}` — [dimension]
Verdict: RESOLVED in favor of `{signal}` because [evidential reason]
     OR: UNRESOLVED because [what {namespace}/{skill} would resolve it]
```

Every verdict carries a because-clause.

**Prose prohibition**: All adjudication commitments belong in the Register with
because-clauses. Do not carry verdict reasoning into narrative prose.

After all conflicts:

```
[REGISTER CLOSED — {N} rows, {R} RESOLVED, {U} UNRESOLVED]
```

UNRESOLVED entries auto-transfer to Beat 4 as gaps.

---

### Step 4 — Confidence Band Calculation

Count: S (CONFIRMS), N (total), U (UNRESOLVED in Register).

| Band   | Criteria                              | Permitted stances               | Default |
|--------|---------------------------------------|---------------------------------|---------|
| HIGH   | S/N >= 0.70 AND U = 0                 | Any                             | Per pattern |
| MEDIUM | 0.50 <= S/N < 0.70 OR U <= 2          | Any; non-default needs OVERRIDE | PAUSE   |
| LOW    | S/N < 0.50 OR U > 2                   | PAUSE, PIVOT, ABANDON           | PAUSE or PIVOT |

LOW band: PROCEED is prohibited — no OVERRIDE can bypass this.

MEDIUM band with non-default stance: write the OVERRIDE field before Beat 4.5:

```
OVERRIDE: {named rationale — specific gap being accepted; why it does not change the
  stance from the band default. Must not restate verb, restate band, or use vague qualifier.
  Must name a specific uncertainty and state why it is bounded.}
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

**Beat 2 — What each signal revealed** *(draws from ledger)*
For each ledger entry, one editorial sentence beyond the finding — what it means for the
hypothesis, framed against the inertia marker. Two sentences maximum per signal.

**Beat 3 — What the signals say together**
Open: "Across [N] signals, the hypothesis was [vector]." Build the pattern from there.

**Anchor citation rule**: Every non-trivial Beat 3 claim cites its ledger entry:
`(anchored: {artifact-name}, {stance})`.

Draw conflict/verdict entries from the Register (already adjudicated — do not re-adjudicate
in prose).

**Falsifiability gate**:

```
Falsifiability: [externally observable evidence — in the world, market, or system under
  analysis — that would falsify the pattern claim if found]
```

**Beat 4 — What remains uncertain**
RESOLVED verdicts are not gaps. UNRESOLVED verdicts auto-transfer here.

```
Gap: [what is unknown]
Most exposed finding: [which ledger claim is most at risk]
Next signal: {namespace}/{skill} — [expected finding type]
```

---

### Beat 3 Output Inventory

**Complete this section before opening Beat 4.5.**

Enumerate ALL Beat 3 outputs. Beat 4.5 reads from this inventory; Beat 5 derives from it.

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

Completeness check: count `(anchored: ...)` citations in Beat 3; the Evidence anchors list
must contain exactly that count.

Closure stamp:

```
[INVENTORY CLOSED — {P} pattern claims, {A} evidence anchors, {C} adjudication commitments]
```

Do not open Beat 4.5 until this stamp is written.

**Inventory prohibition**: Beat 4.5 and Beat 5 may not introduce claims not in this
inventory.

---

### Marker Lock

**Complete this section after the Beat 3 Output Inventory and before Beat 4.5.**

The Marker Lock checks that the selected recommendation stance does not violate the
inertia profile of the signal set. For each ledger entry, derive an explicit inertia weight
and state the stance constraint that weight and verdict combination implies.

**Inertia weight derivation**:
- **HIGH** — the inertia marker names a firmly established belief, prior measurement,
  existing design commitment, or strong organizational assumption
- **MEDIUM** — the inertia marker names a working assumption or expectation held with
  moderate confidence
- **LOW** — the inertia marker names a weak prior, default assumption, or expectation held
  with acknowledged uncertainty

```
Marker Lock:

| Signal | Inertia marker (quoted) | Weight | Verdict | Stance constraint |
|--------|------------------------|--------|---------|-------------------|
| {artifact-name} | "prior expectation: {text}" | HIGH | CONFIRMS | Supports PROCEED or PAUSE; PIVOT/ABANDON requires override |
| {artifact-name} | "prior expectation: {text}" | MEDIUM | MODIFIES | Neutral — follow Band gate |
| {artifact-name} | "prior expectation: {text}" | HIGH | CONTRADICTS (RESOLVED) | Resolved; no additional constraint |
| {artifact-name} | "prior expectation: {text}" | HIGH | CONTRADICTS (UNRESOLVED) | Blocks PROCEED; PAUSE required minimum |
```

**Lock rules**:
- Any HIGH-weight CONFIRMS entry: PIVOT or ABANDON is prohibited without a named Marker
  Lock Override stating which HIGH-weight CONFIRMS finding is being dismissed and why.
- Any HIGH-weight CONTRADICTS (UNRESOLVED): PROCEED is prohibited. The selected stance must
  be PAUSE, PIVOT, or ABANDON.
- Any HIGH-weight CONTRADICTS (RESOLVED): constraint is lifted for that entry; apply the
  Confidence Band gate normally.
- MEDIUM and LOW-weight entries: follow the Confidence Band gate; no additional Marker Lock
  constraint.

After the table:

```
Marker Lock verdict: [one sentence — does the selected stance ({verb}) satisfy all Marker
  Lock rules? If yes: "Lock satisfied — {reasoning referencing specific HIGH-weight entries
  and their constraints}." If no: state which rule is violated and revise the stance.]

[If a Marker Lock Override was required:]
MARKER LOCK OVERRIDE: {named rationale — which HIGH-weight CONFIRMS finding is being
  dismissed, and the specific evidence or judgment that justifies dismissal. Must not
  restate the recommendation verb or use a vague qualifier.}
```

Do not open Beat 4.5 until the Marker Lock verdict is written and the stance satisfies all
lock rules.

---

### Beat 4.5 — Derivation chain

Reads from the Beat 3 Output Inventory and Marker Lock only. Four elements:

```
Anchored claim: "[exact pattern claim from Inventory, verbatim with anchor]"
  (anchored: {artifact-name}, {stance})
Net vector: {vector} — [mechanism sentence, verbatim from ledger]
Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON} — [one sentence: licensing —
  must match Confidence Band gate output and satisfy Marker Lock verdict]
Adjacent verb: {ADJ-VERB} — [one sentence: what specific entry in the Marker Lock table,
  and which inertia weight designation, would have to differ for this adjacent verb to
  apply — a reader preferring the adjacent verb must contest that specific marker row]
```

Do not write Beat 5 until all four elements are consistent with the Inventory, the Band,
and the Marker Lock verdict.

**Beat 5 derivation prohibition**: Beat 5 may not introduce new evidence, new patterns, or
new adjudications not already in the Inventory.

---

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon** — must match the Marker Lock verdict
and the Band gate output. One paragraph. Names what to do, under what conditions, with what
scope.

---

**Voice**: Active, opinionated. The Marker Lock table reads as a formal constraint record;
the recommendation reads as a directive grounded in that constraint.

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
**Hypothesis at S3**: [claim]
**Net mutation vector**: {vector} — [mechanism]
**Evidence trajectory**: POINT-IN-TIME | DIRECTIONAL — [sentence]

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
Across [N] signals, the hypothesis was [vector].
[pattern with anchors, conflict/verdict, falsifiability]

### Beat 4 — What remains uncertain
Gap: ...

### Beat 3 Output Inventory
Pattern claims:
1. "[claim]" (anchored: ...)
Evidence anchors: ...
Adjudication commitments: ...
[INVENTORY CLOSED — P claims, A anchors, C commitments]

### Marker Lock
| Signal | Inertia marker (quoted) | Weight | Verdict | Stance constraint |
|--------|------------------------|--------|---------|-------------------|
...
Marker Lock verdict: [Lock satisfied — reasoning] OR [Violation — revise stance]
[MARKER LOCK OVERRIDE: {named rationale}]  <- if required

### Beat 4.5 — Derivation chain
Anchored claim: "[from Inventory]" (anchored: ...)
Net vector: {vector} — [mechanism]
Recommendation verb: {VERB} — [licensing — consistent with Band and Marker Lock]
Adjacent verb: {ADJ-VERB} — [contestation — references specific Marker Lock row]

### Beat 5 — Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON** — [directive — no new reasoning]
```

---

## V-04

**Variation axis**: Combination — R11 V-04 base (reconciliation table + 5-element derivation
chain + Confidence Band + Beat 3 Output Inventory + OVERRIDE) + V-01's inertia-weight column
in the reconciliation table (C-28) + V-02's immutability prohibition on the Inventory stamp
(C-29)
**Hypothesis**: R11 V-04 was the strongest Round 11 architecture without C-28 and C-29:
it achieved C-26 PASS (Beat 3 Output Inventory with closure stamp), C-27 PASS (OVERRIDE
format-constrained in the Confidence Band Gate), and C-25 PASS (Band gate architecturally
wired to recommendation stance). The two residual gaps are C-28 (reconciliation table uses
verdict categories, not inertia marker values, as row-level inputs) and C-29 (Inventory
closure stamp records contents but carries no immutability prohibition). Adding V-01's
inertia-weight column to the reconciliation table closes C-28: each row now names the
governing prior expectation and derives an explicit weight, making the consistency check
traceable to source markers. Adding V-02's immutability clause to the Inventory closure
stamp closes C-29: the sealed inventory is now an irrevocable commitment, not merely a
record. Together the two additions complete the R11 V-04 enforcement chain from evidence
weight through consistency check through sealed derivation input through recommendation
stance.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### Step 2 — Hypothesis mutation ledger

**Working hypothesis (S0)**: [one sentence — falsifiable assertion, not a goal]

For each signal artifact:

```
- `{artifact-name}`: {key finding, one to two sentences}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  Inertia marker: prior expectation: {belief before this signal}
  [if MODIFIES]: Hypothesis update: [previous] -> [updated]
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
- **HIGH** — firmly established belief, prior measurement, existing commitment, or strong
  organizational assumption
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

**Weight-sensitive consistency rules**:
- **CONFIRMED**: Valid only when every CONTRADICTS entry is RESOLVED. A HIGH-weight
  CONTRADICTS that is UNRESOLVED always produces a CONFLICT row and invalidates CONFIRMED.
  A MEDIUM-weight CONTRADICTS that is UNRESOLVED produces a CONFLICT row; the vector must be
  revised to QUALIFIED or the conflict resolved. A LOW-weight CONTRADICTS that is UNRESOLVED
  produces a CONFLICT row and requires revision to QUALIFIED unless high-weight CONFIRMS
  entries form a clear majority.
- **QUALIFIED**: CONFIRMS and MODIFIES entries expected. Any CONTRADICTS entry must be
  RESOLVED. An UNRESOLVED CONTRADICTS at any weight level produces a CONFLICT row.
- **REVERSED**: Majority weight in CONTRADICTS or reversing MODIFIES that overturn
  HIGH-weight priors.
- **REDIRECTED**: Entries address a different evaluative frame than S0; weight is distributed
  across dimensions rather than loading onto the S0 axis.

After the table:

```
Reconciliation: Vector is consistent — [reason citing inertia weights of decisive entries].
  OR: Vector revised from [X] to [Y] — [reason: which weights at which verdict levels
  forced the revision].
```

Do not begin story beats until the ledger, vector, and reconciliation are all complete.

---

### Step 3 — Conflict Register

Open the Register (OPEN state).

For every stance conflict:

```
Conflict: `{signal-A}` vs `{signal-B}` — [dimension]
Verdict: RESOLVED in favor of `{signal}` because [evidential reason — name the inertia
  weight of the decisive ledger entry]
     OR: UNRESOLVED because [what {namespace}/{skill} would resolve it]
```

Every verdict carries a because-clause. Any CONFLICT row from the reconciliation table
must appear here as a named entry.

**Prose prohibition**: Adjudication commitments belong in the Register with because-clauses,
not in narrative prose.

Close:

```
[REGISTER CLOSED — {N} rows, {R} RESOLVED, {U} UNRESOLVED]
```

UNRESOLVED entries auto-transfer to Beat 4 as gaps. Do not begin story beats until this
stamp is written.

---

### Step 4 — Confidence Band Calculation

Count: S (CONFIRMS), N (total), U (UNRESOLVED in Register).

| Band   | Criteria                              | Permitted stances               | Default |
|--------|---------------------------------------|---------------------------------|---------|
| HIGH   | S/N >= 0.70 AND U = 0                 | Any                             | Per pattern |
| MEDIUM | 0.50 <= S/N < 0.70 OR U <= 2          | Any; non-default needs OVERRIDE | PAUSE   |
| LOW    | S/N < 0.50 OR U > 2                   | PAUSE, PIVOT, ABANDON           | PAUSE or PIVOT |

LOW band: PROCEED is prohibited.

MEDIUM band with non-default stance: write the format-constrained OVERRIDE field before
Beat 4.5:

```
OVERRIDE: {named rationale — specific gap being accepted; why it does not change the
  stance from the band default. Must not restate the verb, restate the band, or use a
  vague qualifier. Must not describe sentiment or conviction.}
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

**Beat 2 — What each signal revealed** *(draws from ledger)*
For each ledger entry, one editorial sentence — what the finding means for the hypothesis,
framed against the inertia marker. The inertia weight from the reconciliation table informs
how significant a confirmation or contradiction this signal represents. Two sentences max.

**Beat 3 — What the signals say together**
Open: "Across [N] signals, the hypothesis was [reconciled vector]." The reconciliation table
validates this claim.

**Anchor citation rule**: Every non-trivial Beat 3 claim cites its ledger entry:
`(anchored: {artifact-name}, {stance})`.

Draw conflict/verdict entries from the Register.

**Falsifiability gate**:

```
Falsifiability: [externally observable evidence that would falsify the pattern claim —
  not a provenance check; a domain-facing prediction]
```

**Beat 4 — What remains uncertain**
RESOLVED verdicts are not gaps. UNRESOLVED verdicts auto-transfer from the Register.

```
Gap: [what is unknown]
Most exposed finding: [which ledger claim is most at risk]
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
[Every anchored artifact from Beat 3 must appear here]

Adjudication commitments (RESOLVED verdicts from Register only):
- `{signal-A}` vs `{signal-B}`: RESOLVED in favor of `{signal}` — [reason phrase]
[If none: "No adjudicated conflicts."]
```

Completeness check: count `(anchored: ...)` citations in Beat 3; Evidence anchors must
contain exactly that count.

**Inventory closure stamp** — append immediately after inventory contents:

```
[INVENTORY CLOSED — {P} pattern claims, {A} evidence anchors, {C} adjudication commitments
 — IMMUTABLE: no item in this inventory may be added, modified, or removed after this stamp.
   The contents are the irrevocable input to the derivation chain. Modification to
   accommodate Beat 5 framing, prose narrative, or recommendation preference is prohibited.]
```

The immutability prohibition is part of the stamp format. A stamp without this clause is
not a sealed inventory.

Do not open Beat 4.5 until this stamp is written.

**Inventory prohibition**: Beat 4.5 and Beat 5 may not introduce claims not in this
inventory. Beat 5 is a derivation surface only.

---

### Beat 4.5 — Derivation chain

Five elements. Reads from the Beat 3 Output Inventory only.

```
Anchored claim: "[exact pattern claim from Inventory, verbatim with anchor]"
  (anchored: {artifact-name}, {stance})
Net vector: {CONFIRMED | QUALIFIED | REVERSED | REDIRECTED} — [mechanism sentence from
  reconciliation table, copied verbatim — must match reconciliation conclusion]
Recommendation verb: {PROCEED | PAUSE | PIVOT | ABANDON} — [one sentence: licensing —
  consistent with the Confidence Band gate output]
Adjacent verb: {ADJ-VERB} — [one sentence: what specific reconciliation table row, and
  which inertia weight designation, would have to differ for this adjacent verb to apply
  — name the exact entry a reader who prefers the adjacent verb must contest]
Conditions: [one of: CONTRADICTS count by weight / gap-closure cost / risk tolerance
  threshold / readiness signal distribution — stated as a specific value from the ledger
  and reconciliation table, citing at least one inertia-weight designation]
```

**Conditions guidance**: The conditions clause must reference at least one inertia weight
value from the reconciliation table. "QUALIFIED with 0 HIGH-weight CONTRADICTS remaining
unresolved means proceed" passes; "QUALIFIED with no remaining conflicts" fails.

Do not write Beat 5 until all five elements are internally consistent and derive exclusively
from the Inventory.

**Beat 5 derivation prohibition**: Beat 5 may not introduce new evidence, new patterns, or
new adjudications not in the Inventory.

---

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon** — must match Beat 4.5 verb and Band
gate output. One paragraph. Names what to do, under what conditions, with what scope.
Does not repeat the derivation chain.

---

**Voice**: Active, opinionated. Reconciliation table reads as a formal weight-sensitive
consistency record; Inventory as a sealed derivation manifest; derivation chain as a
decision frame with weight-traceable contestation points.

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
**Hypothesis at S3**: [claim]
**Net mutation vector**: {vector} — [mechanism]
**Evidence trajectory**: POINT-IN-TIME | DIRECTIONAL — [sentence]

## Vector-Verdict Reconciliation
| Signal | Inertia weight | Verdict type | Consistent? |
|--------|---------------|-------------|-------------|
| {artifact-name} | HIGH — "{prior expectation}" | CONFIRMS | YES |
...
**Reconciliation**: [conclusion — references inertia weights of decisive entries]

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
[pattern with anchors, conflict/verdict entries, falsifiability]

### Beat 4 — What remains uncertain
Gap: ...

### Beat 3 Output Inventory
Pattern claims:
1. "[claim]" (anchored: ...)
Evidence anchors: ...
Adjudication commitments: ...
[INVENTORY CLOSED — P claims, A anchors, C commitments
 — IMMUTABLE: no item may be added, modified, or removed after this stamp. Contents are
   the irrevocable input to the derivation chain. Modification prohibited.]

### Beat 4.5 — Derivation chain
Anchored claim: "[from Inventory, verbatim]" (anchored: ...)
Net vector: {vector} — [mechanism — matches reconciliation]
Recommendation verb: {VERB} — [licensing — consistent with Band gate]
Adjacent verb: {ADJ-VERB} — [contestation — references reconciliation row and inertia weight]
Conditions: [weight-sensitive parameter — specific value from ledger/reconciliation]

### Beat 5 — Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON** — [directive — no new reasoning; consistent with
  Band gate and OVERRIDE if present]
```

---

## V-05

**Variation axis**: Full combination — R11 V-05 EVALUATOR/AUTHOR phase architecture + V-01's
inertia-weight column in EVALUATOR's reconciliation table (C-28) + full-packet immutability
on the Derivation Packet seal (C-29), achieving C-26, C-27, C-28, and C-29 simultaneously
**Hypothesis**: R11 V-05's EVALUATOR/AUTHOR phase architecture is the cleanest enforcement
model: the EVALUATOR produces all analytical outputs and seals them in a Derivation Packet
before AUTHOR opens narrative framing. C-26 and C-27 are EVALUATOR-phase responsibilities
satisfied by the Packet's enumeration and format-constrained OVERRIDE slot. C-28 and C-29
add two further requirements to the EVALUATOR phase: (1) the reconciliation table inside
EVALUATOR must include an inertia-weight column with weight-sensitive consistency rules so
that the derivation packet's authoritativeness is traceable to source markers, not verdict
categories; (2) the Packet sealing stamp must carry an explicit immutability prohibition so
that the sealed Packet is an irrevocable commitment. With both additions, the enforcement
chain is complete: (a) inertia markers enter the reconciliation table as named row-level
inputs, (b) the reconciliation table produces a weight-certified vector, (c) the vector and
all pattern outputs are sealed into an immutable Derivation Packet, (d) AUTHOR derives from
the Packet without re-entering the evidence layer. This tests whether the phase separation
model naturally absorbs C-28 and C-29 as EVALUATOR-phase requirements without requiring
structural changes to AUTHOR's workflow.

---

You are running `/topic:story` for a topic. The topic name is provided.

This skill runs in two phases: **EVALUATOR** then **AUTHOR**. Do not begin AUTHOR until
EVALUATOR is complete and the Derivation Packet is sealed.

---

## EVALUATOR Phase

**Permitted**: Gathering artifacts. Extracting findings. Assigning stances and rationales.
Tracking hypothesis mutation. Computing the reconciliation table with inertia weights.
Adjudicating conflicts. Closing the Conflict Register. Synthesizing the cross-signal
pattern. Enumerating all pattern outputs into the Derivation Packet. Computing the
Confidence Band and writing the OVERRIDE field if required. Sealing the Packet.
**Forbidden**: Writing story prose (Beats 1–5). Narrative framing. Editorial voice.
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
- The rationale names specific evidence; general "this signal supports the hypothesis" fails
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
| {artifact-name} | HIGH — "{inertia marker text, quoted or closely paraphrased}" | CONFIRMS | YES |
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
  OR: Vector revised from [X] to [Y] — [reason citing which weights at which verdict levels
  forced the revision].
```

---

### E-6 — Conflict Register

Open the Register (OPEN state).

For every stance conflict:

```
Conflict: `{signal-A}` vs `{signal-B}` — [dimension]
Verdict: RESOLVED in favor of `{signal}` because [evidential reason — name the inertia
  weight of the decisive entry]
     OR: UNRESOLVED because [what {namespace}/{skill} would resolve it]
```

Every verdict carries a because-clause. Any CONFLICT row from the reconciliation table
must appear here.

Close:

```
[REGISTER CLOSED — {N} rows, {R} RESOLVED, {U} UNRESOLVED]
```

UNRESOLVED entries are flagged; they will appear in the Packet and transfer to Beat 4.

---

### E-7 — Pattern synthesis (raw)

Synthesize the cross-signal pattern from the ledger. This is NOT story prose — it is the
analytical product that will be enumerated into the Packet.

Open: "Across [N] signals, the hypothesis was [vector]."

For each non-trivial claim, cite the ledger entry: `(anchored: {artifact-name}, {stance})`.

Write the falsifiability condition:

```
Falsifiability: [externally observable domain evidence that would falsify the pattern claim
  — not a provenance check; a domain-facing prediction]
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

MEDIUM band with non-default stance: the OVERRIDE slot in the Packet must be filled with
a format-constrained rationale:
- Name the specific gap or uncertainty being accepted as an acceptable risk
- State why it does not change the stance from the band default
- Must NOT restate the verb, restate the band, or use a vague qualifier or sentiment

---

### E-9 — Seal the Derivation Packet

Write the Derivation Packet to the artifact. This is the complete and sole input to AUTHOR.
AUTHOR may not introduce evidence, claims, or reasoning not in the Packet.

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
[Every declarative claim from E-7, numbered, verbatim, with anchor citations]
1. "[claim]" (anchored: {artifact-name}, {stance})
2. ...

### Evidence anchors
[Every artifact cited in E-7 pattern claims]
- {artifact-name} ({stance}): [one phrase — role in pattern claim]

### Adjudication commitments
[All RESOLVED verdicts from the Conflict Register]
- `{signal-A}` vs `{signal-B}`: RESOLVED in favor of `{signal}` — [reason phrase]
[If none: "No adjudicated conflicts."]
[UNRESOLVED entries do not appear here — they are in Beat 4 as gaps]

### Confidence Band
Signals confirming: {S}/{N} ({pct}%)
Unresolved contradictions: {U}
Band: HIGH | MEDIUM | LOW
Default stance: {default}
Selected stance: {verb}
[OVERRIDE: {named rationale — specific gap being accepted, and why it does not reverse
  the stance from the default. Must not restate verb, restate band, or use vague qualifier.}]
<- Required only when selected stance differs from band default. Format-constrained.

### Falsifiability
[Verbatim from E-7]
```

After writing all sections, append the Packet seal:

```
[PACKET SEALED — {P} pattern claims, {A} evidence anchors, {C} commitments,
  Band: {band}, Selected stance: {verb}
  — IMMUTABLE: no item in this Packet may be added, modified, or removed after this stamp.
    The Pattern claims, Evidence anchors, Adjudication commitments, Confidence Band, and
    OVERRIDE field (if present) are irrevocable derivation inputs. Modification to
    accommodate AUTHOR narrative, Beat 5 framing, or prose convenience is prohibited.
    If a conflict surfaces during AUTHOR prose drafting, return to EVALUATOR: add a new
    Register entry, update the Adjudication commitments section, re-seal with a new stamp.]
```

The immutability prohibition is part of the seal. A Packet without this clause is unsealed.

---

## AUTHOR Phase

**Permitted**: Pattern derivation. Story prose. Conflict rendering from the Register.
Recommendation. Adjacent-verb contrast.
**Forbidden**: Re-reading signal artifacts — all findings, stances, and patterns are in the
Packet. Introducing evidence, claims, or reasoning not in the Packet. Revising the Packet
contents.

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

**Beat 4 — What remains uncertain**
UNRESOLVED Register entries transfer here as gaps. Additional scoped gaps follow.

```
Gap: [what is unknown]
Most exposed finding: [which Packet pattern claim is most at risk]
Next signal: {namespace}/{skill} — [expected finding type]
```

Adjudication commitments from the Packet are not gaps.

**Beat 4.5 — Derivation chain** (reads from Packet)

Five elements:

```
Anchored claim: "[exact claim from Packet's Pattern claims, verbatim with anchor]"
  (anchored: {artifact-name}, {stance})
Net vector: {vector from Packet} — [mechanism sentence, verbatim from Packet]
Recommendation verb: {verb from Packet's Selected stance} — [one sentence: licensing —
  states what in the Packet's reconciliation table and Band gate authorizes this verb]
Adjacent verb: {adjacent verb} — [one sentence: which specific row in the Packet's
  reconciliation table, and which inertia weight designation in that row, would have to
  differ for the adjacent verb to apply — a reader preferring the adjacent verb must
  contest that specific row and weight]
Conditions: [one of: CONTRADICTS count by weight / gap-closure cost / risk tolerance
  threshold / readiness signal distribution — as a specific value from the Packet,
  citing at least one inertia-weight designation from the reconciliation table]
```

Do not write Beat 5 until all five elements are consistent with the Packet.

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon** — must match the Packet's Selected
stance. One paragraph. If the Packet contains an OVERRIDE field, Beat 5 names the accepted
uncertainty once — it does not re-argue. Beat 5 may not introduce new evidence, new
patterns, or new adjudications not in the Packet.

---

**Voice**: The Packet reads as an engineering specification; the reconciliation table as a
weight-certified consistency record; the story beats as editorial narrative; the
recommendation as a directive grounded in irrevocable inputs.

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
| {artifact-name} | HIGH — "{prior expectation}" | CONFIRMS | YES |
...
Reconciliation: [conclusion — references inertia weights of decisive entries]

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
    irrevocable derivation inputs. Modification prohibited. Return to EVALUATOR if new
    conflicts surface.]

## Story

### Beat 1 — What we set out to understand
...

### Beat 2 — What each signal revealed
...

### Beat 3 — What the signals say together
Across [N] signals, the hypothesis was [vector from Packet].
[pattern from Packet — anchored claims, conflict/verdict, falsifiability verbatim]

### Beat 4 — What remains uncertain
Gap: ...
Most exposed finding: ...
Next signal: ...

### Beat 4.5 — Derivation chain
Anchored claim: "[from Packet]" (anchored: ...)
Net vector: {vector} — [mechanism, verbatim from Packet]
Recommendation verb: {VERB} — [licensing — references Packet reconciliation and Band]
Adjacent verb: {ADJ-VERB} — [contestation — references specific Packet reconciliation
  row and inertia weight designation]
Conditions: [weight-sensitive parameter from Packet — specific value with inertia weight]

### Beat 5 — Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON** — [directive; if OVERRIDE in Packet, names the
  accepted uncertainty once; no new reasoning]
```
