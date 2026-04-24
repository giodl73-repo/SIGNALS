---
skill: quest-variate
skill_target: topic-story
date: 2026-03-15
round: 9
rubric: v8
---

# Variations — topic-story (Round 9, rubric v8)

Five complete, runnable skill body prompt variations.
Single-axis first (V-01 through V-03), then two combinations (V-04, V-05).

**Design context**: v8 rubric adds C-22 (Register Lifecycle Gate) and C-23 (External
Falsification Evidence). Two extractable patterns from Round 8:

**R8 finding on C-22 (Register Lifecycle Gate — sourced from R8 V-03's axis):**
R8 V-03 introduced the `[REGISTER CLOSED — N rows, R RESOLVED, U UNRESOLVED]` count stamp
and gated Story entry on its presence. That produced the C-22 criterion. But R8 V-03
had a gap: the register had a CLOSED state but no explicit OPEN state. A lifecycle without
a named initial state is half a lifecycle — the closure is an ending without a declared
beginning, which means the register's scope is ambiguous. An evaluator cannot verify that
the register was open during signal processing and closed before Story; they can only verify
that a closed stamp appears. The stronger architecture declares OPEN at creation and CLOSED
at completion: the register is an explicit artifact with a lifecycle, not a section that
happens to end with a stamp. C-22 also specifies a reopen protocol — what happens when a
conflict surfaces during prose drafting. Without it, the lifecycle gate is brittle: the
author faces an undefined choice at the moment of mid-prose conflict, and the undefined
path creates implicit-absorption risk even when the gate is present.

**R8 finding on C-23 (External Falsification Evidence — sourced from C-14 consistent
PARTIAL across all R8 variations):**
Every R8 variation had a falsifiability test in the Pattern Gate. Every one failed C-14
as PARTIAL because all falsification conditions tested internal signal properties (cross-
signal origin provenance: "if all signals came from the same source," "if signals are not
independent"). These are quality checks on the signal set, not evidence the pattern claim
is wrong. A diverse signal set can produce a wrong world-facing prediction; provenance
diversity doesn't close that gap. C-23 requires the falsifying condition to be externally
observable in the subject domain — a measurable threshold, a behavioral indicator, a
market signal — something that, if observed in the world, would mean the pattern is
incorrect regardless of how diverse or independent the signal set is. The recurring failure
pattern is that provenance-style falsifiers feel concrete (they name a source property)
while being structurally inward — they test the quality of the evidence rather than the
truth of the claim. The fix is a format constraint that prohibits provenance conditions
explicitly and requires a domain-observable condition by format.

**Round 9 primary axes**: V-01 targets C-22 via explicit OPEN/CLOSED lifecycle — the
register declares its state at creation and at completion, and Story entry is gated on
confirming the CLOSED state; no reopen protocol yet. V-02 targets C-23 via a dedicated
"Domain Falsifier" field in the Pattern Gate — a named field that accepts only externally
observable conditions, with explicit prohibition on signal-provenance conditions. V-03
targets the full C-22 spec — lifecycle (V-01's OPEN declaration and count stamp) plus the
reopen protocol (a named interrupt procedure for mid-prose conflicts). V-04 combines V-01
(lifecycle gate) and V-02 (domain falsifier) on the R8 V-04 base (mutation ledger +
because-clause adjudication + distributed prohibition guards + pre-seeded scaffold). V-05
is the full combination: R8 V-05 base (EVALUATOR/AUTHOR phases + Signal Extract as visible
artifact section) upgraded with V-03 full lifecycle in the EVALUATOR section and V-02
domain falsifier in the AUTHOR's Pattern Gate.

---

## V-01

**Variation axis**: Lifecycle emphasis — explicit OPEN/CLOSED register state with pre-Story
confirmation gate (C-22 target, partial — lifecycle + gate without reopen protocol)
**Hypothesis**: C-22 requires the Conflict Register to have a formal open/closed lifecycle
visible in the artifact and to gate Story entry on confirmed closure. R8 V-03 introduced
the closure stamp but not an explicit OPEN declaration. A register with only a CLOSED state
has a termination point but no declared scope — an evaluator cannot verify the register was
receiving entries during signal processing, only that it eventually closed. The fix adds
an `[REGISTER: OPEN]` declaration at the register's creation and transforms the count stamp
into a formal closing act rather than a trailing annotation. The pre-Story gate becomes a
structural check: the Story section's opening instruction requires confirming the CLOSED
stamp is present before any beat is written. This tests whether the full OPEN→CLOSED
lifecycle plus the confirmation gate satisfies C-22 independently, without requiring the
reopen protocol. The reopen protocol is intentionally omitted to isolate the lifecycle
mechanism as the single axis.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### Step 2 — Hypothesis mutation ledger

Before writing the story, complete the ledger.

**Working hypothesis (S0)**: [one sentence — the specific claim the team entered with,
stated as a falsifiable assertion, not a goal or question]

For each signal artifact, in the order read:

```
- `{artifact-name}`: {key finding most relevant to the working hypothesis, one to two
  sentences}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [if MODIFIES]: Hypothesis update: [previous wording] → [updated wording]
```

After all entries:

```
Hypothesis at S3: [one sentence — working hypothesis after all stances are applied]
```

**Anti-stagnation check**: If S3 is identical to S0, state why. Silently identical S0
and S3 fails.

Do not open the Conflict Register until the ledger is complete.

---

### Step 3 — Conflict Register

Write the following line as the first line of the register section:

```
[REGISTER: OPEN]
```

The register is now in OPEN state. It accepts entries until it is formally closed.

List every tension between stances (CONFIRMS vs CONTRADICTS, or competing MODIFIES
entries pulling in different directions). For each tension, write one entry.

For RESOLVED rows:

```
| Row | Signal-A | Signal-B | Dimension | Verdict |
| {N} | `{artifact-A}` | `{artifact-B}` | [dimension of disagreement] | RESOLVED · `{signal}` because [specific evidential reason — name the element from that signal that outweighs the alternative] |
```

For UNRESOLVED rows, leave the Verdict cell blank and fill the scaffold immediately below
the row:

```
| {N} | `{artifact-A}` | `{artifact-B}` | [dimension] | — see UNRESOLVED scaffold below — |

Row {N} — UNRESOLVED:
  Gap: [what is unknown — the specific question this conflict raises]
  Most exposed finding: [which ledger entry's claim cannot be confirmed without this]
  Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

**Format identity rule**: The filled UNRESOLVED scaffold IS the gap entry. Beat 4
reproduces every UNRESOLVED scaffold verbatim — the three-line block exactly as written
here. Do not rewrite, reselect, or reformulate.

**Prohibition** (applies to all story beats): Every adjudication verdict must appear as
a named row in this register. Do not record conflict resolutions in prose narrative.

If no tensions exist, write: `Conflict Register: empty.`

When all entries are written, close the register by replacing `[REGISTER: OPEN]` with
— or appending immediately after the last row — the following closure stamp:

```
[REGISTER CLOSED — {N} rows, {R} RESOLVED, {U} UNRESOLVED]
```

Verify the counts before writing the stamp: N = total rows, R = RESOLVED rows,
U = UNRESOLVED rows, R + U = N.

---

### Step 4 — Write the story

**Pre-Story gate**: Before beginning Beat 1, confirm that the line
`[REGISTER CLOSED — ...]` is present in the register section above. Do not write Beat 1
if the closure stamp is absent. If the stamp is missing, return to Step 3 and close the
register.

Write to `simulations/{topic}/{topic}-story-{date}.md`.

**Beat 1 — What we set out to understand**
One to three sentences. The original question and the S0 working hypothesis. Name the
entering claim as a falsifiable assertion, not a goal.

**Beat 2 — What each signal revealed**
Draw from the ledger entries. For each entry: the key finding plus one editorial sentence
on what it means for the hypothesis. Two sentences maximum per signal.

**Beat 3 — What the signals say together**
The cross-signal pattern. Reference at least two ledger entries by artifact name. Draw a
conclusion derivable only from the full entry set, not from any single entry.

The register is closed — apply it. RESOLVED rows are pattern evidence; present their
because-clauses as part of the argument. UNRESOLVED rows are seated in Beat 4 — do not
re-adjudicate them; reference by row number only: "Row {N} remains open."

The S0→S3 delta is your spine — name the direction and ground it in MODIFIES entries.

Falsifiability test: *does any single ledger entry contain this conclusion?* If yes, revisit.

**Beat 4 — What remains uncertain**
Two categories, kept separate:

*Conflicts carried forward (from closed register):*
Reproduce every UNRESOLVED scaffold verbatim — the three-line block exactly as written.
Do not rewrite or condense.

*Additional gaps (not sourced from conflict):*

```
Gap: [what is unknown]
Most exposed finding: [which ledger entry's claim cannot be confirmed without this]
Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

If no additional gaps, write: `Additional gaps: none.`

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon**.
One paragraph. Acts on the S3 hypothesis, not S0. Ground the recommendation in the Beat 3
pattern and at least one RESOLVED row from the closed register (cite by row number). The
UNRESOLVED count from the closure stamp sets the risk floor — name it explicitly.
"It depends" without a stated default fails.

---

**Voice**: Active, opinionated. The `[REGISTER: OPEN]` / `[REGISTER CLOSED]` pair are
formal lifecycle markers — they are not prose. Story beats carry the editorial argument
against the closed record.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

**Working hypothesis (S0)**: [claim]

## Hypothesis Mutation Ledger
- `{artifact-name}`: {finding}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [Hypothesis update if MODIFIES]
...
**Hypothesis at S3**: [evolved claim]

## Conflict Register
[REGISTER: OPEN]

| Row | Signal-A | Signal-B | Dimension | Verdict |
| 1 | `...` | `...` | [...] | RESOLVED · `{signal}` because [...] |
| 2 | `...` | `...` | [...] | — see UNRESOLVED scaffold below — |

Row 2 — UNRESOLVED:
  Gap: [what is unknown]
  Most exposed finding: [which entry]
  Next signal: {namespace}/{skill} — [expected finding]

[REGISTER CLOSED — 2 rows, 1 RESOLVED, 1 UNRESOLVED]

## Story

### Beat 1 — What we set out to understand
[*Pre-story gate confirmed: `[REGISTER CLOSED]` present.*]
...

### Beat 2 — What each signal revealed
...

### Beat 3 — What the signals say together
[cross-signal pattern; RESOLVED rows cited with because-clauses; UNRESOLVED cited by
row number only]

### Beat 4 — What remains uncertain
*Conflicts carried forward:*
Row 2 — UNRESOLVED:
  Gap: [verbatim]
  Most exposed finding: [verbatim]
  Next signal: [verbatim]

*Additional gaps:*
[entries or "none"]

### Beat 5 — Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON** — [paragraph; UNRESOLVED count named as risk
floor; at least one RESOLVED row cited as warrant]
```

---

## V-02

**Variation axis**: Output format — dedicated Domain Falsifier field in Pattern Gate
(C-23 target)
**Hypothesis**: C-14 was PARTIAL across all R8 variations because every falsification
condition tested internal signal properties — provenance, diversity, extraction source.
These are quality checks on the evidence, not falsifying evidence for the pattern claim.
C-23 requires the falsification condition to be externally observable in the subject
domain. The fix is a format constraint on the Pattern Gate: a named "Domain Falsifier"
field that accepts only externally observable conditions, with explicit prohibition on
provenance-type conditions. The field forces the author to name a specific observable
condition — a measurable threshold, a behavioral indicator, a market signal, a system
output — that, if observed in the world, would mean the pattern is incorrect regardless
of how diverse the signal set is. The prohibition is categorical: "signal-provenance
conditions ('if all signals came from the same author') are quality checks, not domain
falsifiers." This tests whether a dedicated field with an explicit prohibition and a
domain-observable requirement satisfies C-23 without requiring changes to the broader
lifecycle structure.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### Step 2 — Hypothesis mutation ledger

**Working hypothesis (S0)**: [one sentence — the specific claim the team entered with,
stated as a falsifiable assertion, not a goal or question]

For each signal artifact, in the order read:

```
- `{artifact-name}`: {key finding most relevant to the working hypothesis, one to two
  sentences}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [if MODIFIES]: Hypothesis update: [previous wording] → [updated wording]
```

After all entries:

```
Hypothesis at S3: [one sentence — working hypothesis after all stances are applied]
```

**Anti-stagnation check**: If S3 is identical to S0, state why. Silently identical S0
and S3 fails.

---

### Step 3 — Conflict Register

List every tension between stances. For each tension, write one row.

For RESOLVED rows:

```
| Row | Signal-A | Signal-B | Dimension | Verdict |
| {N} | `{artifact-A}` | `{artifact-B}` | [dimension] | RESOLVED · `{signal}` because [specific evidential reason] |
```

For UNRESOLVED rows, fill the scaffold below the row:

```
| {N} | `{artifact-A}` | `{artifact-B}` | [dimension] | — see UNRESOLVED scaffold — |

Row {N} — UNRESOLVED:
  Gap: [what is unknown]
  Most exposed finding: [which ledger entry depends on this]
  Next signal: {namespace}/{skill} — [expected finding type]
```

**Prohibition**: Every verdict must appear as a named row in this register. Do not
record conflict resolutions in prose narrative.

If no tensions exist, write: `Conflict Register: empty.`

When all rows are written, write the closure stamp:

```
[REGISTER CLOSED — {N} rows, {R} RESOLVED, {U} UNRESOLVED]
```

---

### Step 4 — Write the story

Write to `simulations/{topic}/{topic}-story-{date}.md`.

**Beat 1 — What we set out to understand**
One to three sentences. The original question and the S0 working hypothesis.

**Beat 2 — What each signal revealed**
One key finding plus one editorial sentence per signal. Two sentences maximum.

**Beat 3 — What the signals say together**
The cross-signal pattern. Reference at least two ledger entries. Draw a conclusion
derivable only from the full entry set.

Apply the register: RESOLVED rows are pattern evidence. UNRESOLVED rows are in Beat 4;
cite by row number only.

The S0→S3 delta is your spine.

**Pattern Gate** — complete this block before writing any further sentences in Beat 3:

```
Pattern claim: [one declarative sentence naming the phenomenon]

Domain Falsifier: [one sentence naming a specific observable condition in the subject
  domain — a measurable threshold, behavioral indicator, or system output — that, if
  observed, would demonstrate the pattern claim is incorrect]

  CONSTRAINT: The falsifier must name something external to this signal set. It must
  be observable in the world, market, or system under analysis. Do not name a condition
  about signal properties (provenance, source diversity, extraction method, or author
  overlap). "If all signals came from the same author" is a quality check on the signal
  set, not evidence the pattern is wrong. A domain falsifier is falsifying regardless
  of how diverse or independent the signal set is.

  EXAMPLES OF DOMAIN FALSIFIERS (acceptable):
    - "If {measurable indicator} is observed at {threshold}, the pattern does not hold."
    - "If {observable behavior} is absent in {context} by {date or milestone}, the
      pattern claim is refuted."
    - "If {system output} shows {condition}, the claimed direction reverses."

  EXAMPLES OF PROVENANCE CONDITIONS (prohibited):
    - "If all signals came from the same author, the pattern may be biased."
    - "If the signals are not independent, the convergence is artificial."
    - "If the sample is not representative, the finding may not generalize."
```

After the Pattern Gate, continue the Beat 3 argument grounding the pattern in the S0→S3
delta and RESOLVED register rows.

Falsifiability test: *does any single ledger entry contain this conclusion?* If yes, revisit.

**Beat 4 — What remains uncertain**
*Conflicts carried forward:*
Reproduce every UNRESOLVED scaffold verbatim.

*Additional gaps:*

```
Gap: [what is unknown]
Most exposed finding: [which ledger entry's claim depends on this]
Next signal: {namespace}/{skill} — [expected finding type]
```

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon**.
One paragraph. Acts on the S3 hypothesis. Ground in the Beat 3 pattern and at least one
RESOLVED register row. The UNRESOLVED count sets the risk floor — name it.
"It depends" without a stated default fails.

---

**Voice**: Active, opinionated. The Domain Falsifier field is filled with a specific
observable condition — not a hedge, not a provenance check, not a generic "we need more
data." The pattern claim and its domain falsifier appear together in the Pattern Gate;
the falsifier is the pattern claim's accountability line.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

**Working hypothesis (S0)**: [claim]

## Hypothesis Mutation Ledger
- `{artifact-name}`: {finding}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [Hypothesis update if MODIFIES]
...
**Hypothesis at S3**: [evolved claim]

## Conflict Register
| Row | Signal-A | Signal-B | Dimension | Verdict |
| 1 | `...` | `...` | [...] | RESOLVED · `{signal}` because [...] |
[UNRESOLVED rows with scaffolds]
[REGISTER CLOSED — N rows, R RESOLVED, U UNRESOLVED]

## Story

### Beat 1 — What we set out to understand
...

### Beat 2 — What each signal revealed
...

### Beat 3 — What the signals say together

**Pattern Gate**
Pattern claim: [one declarative sentence]
Domain Falsifier: [one sentence naming an externally observable condition in the subject
  domain that would refute the pattern claim — not a signal-provenance condition]

[continuation of Beat 3 argument]

### Beat 4 — What remains uncertain
[UNRESOLVED scaffolds verbatim; then additional gaps]

### Beat 5 — Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON** — [grounding paragraph]
```

---

## V-03

**Variation axis**: Lifecycle emphasis — full C-22 specification: OPEN declaration +
count stamp + pre-Story gate + named reopen protocol for mid-prose conflicts
**Hypothesis**: V-01 adds the OPEN/CLOSED lifecycle and pre-Story gate, satisfying the
first two components of C-22. C-22's third component — the reopen protocol — is still
absent in V-01. Without a reopen protocol, the lifecycle gate is brittle at the moment
of mid-prose conflict: an author who encounters a new tension while writing Beat 3 has no
defined path. The gate is present but there's no specified procedure for getting back to
the register and returning to prose. An undefined path at high-risk moments creates
implicit-absorption risk — the author absorbs the conflict in prose simply because that's
the only available action. V-03 adds a named "REOPEN PROTOCOL" block to the register
section, defining the exact steps for mid-prose conflict handling: (1) HALT the current
beat at the point of conflict, (2) append a new row to the register, (3) apply verdict,
(4) update the closure stamp — replace it with `[REGISTER RE-CLOSED — N rows, R RESOLVED,
U UNRESOLVED]` — (5) RESUME from the halt point. The reopen stamp is distinct from the
original closure stamp: it records that the register was opened after initial closure,
which is itself an auditable event. This tests whether the full C-22 specification (V-01
lifecycle + reopen protocol) satisfies C-22 more reliably than V-01 alone.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### Step 2 — Hypothesis mutation ledger

**Working hypothesis (S0)**: [one sentence — the specific claim the team entered with,
stated as a falsifiable assertion, not a goal or question]

For each signal artifact, in the order read:

```
- `{artifact-name}`: {key finding most relevant to the working hypothesis, one to two
  sentences}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [if MODIFIES]: Hypothesis update: [previous wording] → [updated wording]
```

After all entries:

```
Hypothesis at S3: [one sentence — working hypothesis after all stances are applied]
```

**Anti-stagnation check**: If S3 is identical to S0, state why. Silently identical S0
and S3 fails.

Do not open the Conflict Register until the ledger is complete.

---

### Step 3 — Conflict Register

Write the following declaration as the first line of the register section:

```
[REGISTER: OPEN — accepting entries]
```

List every tension between stances. For each tension, write one entry.

For RESOLVED rows:

```
| Row | Signal-A | Signal-B | Dimension | Verdict |
| {N} | `{artifact-A}` | `{artifact-B}` | [dimension of disagreement] | RESOLVED · `{signal}` because [specific evidential reason — name the element from that signal that outweighs the alternative] |
```

For UNRESOLVED rows, fill the scaffold below the row:

```
| {N} | `{artifact-A}` | `{artifact-B}` | [dimension] | — see UNRESOLVED scaffold — |

Row {N} — UNRESOLVED:
  Gap: [what is unknown — the specific question this conflict raises]
  Most exposed finding: [which ledger entry's claim cannot be confirmed without this]
  Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

**Format identity rule**: The filled UNRESOLVED scaffold IS the gap entry. Beat 4
reproduces every UNRESOLVED scaffold verbatim.

**Prohibition**: Every verdict must appear as a named row in this register. Do not
record conflict resolutions in prose narrative.

If no tensions exist, write: `Conflict Register: empty.`

After all initial entries are written, replace `[REGISTER: OPEN — accepting entries]`
with the formal closure stamp:

```
[REGISTER CLOSED — {N} rows, {R} RESOLVED, {U} UNRESOLVED]
```

Verify the counts before writing the stamp.

**REOPEN PROTOCOL** — read this now, before beginning the story:

If a conflict surfaces while writing any story beat (a tension between signals that was
not identified during Step 3):

1. **HALT** — stop writing at the current sentence.
2. **APPEND** — add a new row to the register section above. Write it as a standard row
   (RESOLVED or UNRESOLVED, with scaffold if UNRESOLVED).
3. **UPDATE STAMP** — replace the current closure stamp with:
   `[REGISTER RE-CLOSED — {N} rows, {R} RESOLVED, {U} UNRESOLVED]`
   where N, R, U include the newly appended row.
4. **RESUME** — return to the beat at the halt point and continue.

The REOPEN PROTOCOL is the only valid path when a mid-prose conflict is identified.
Absorbing the conflict in prose narrative — describing the tension without entering it as
a register row — produces an unauditable commitment and violates the prohibition.

---

### Step 4 — Write the story

**Pre-Story gate**: Confirm that a closure stamp — either `[REGISTER CLOSED — ...]` or
`[REGISTER RE-CLOSED — ...]` — is present in the register section above before beginning
Beat 1. Do not write Beat 1 if the stamp is absent.

Write to `simulations/{topic}/{topic}-story-{date}.md`.

**Beat 1 — What we set out to understand**
One to three sentences. The original question and the S0 working hypothesis. Name the
entering claim as a falsifiable assertion, not a goal.

**Beat 2 — What each signal revealed**
Draw from the ledger entries. One key finding plus one editorial sentence per signal.
Two sentences maximum per signal.

**Beat 3 — What the signals say together**
The cross-signal pattern. Reference at least two ledger entries. Draw a conclusion
derivable only from the full entry set.

The register is closed — apply it. RESOLVED rows are pattern evidence; present their
because-clauses as part of the argument. UNRESOLVED rows are seated in Beat 4; reference
by row number only.

The S0→S3 delta is your spine — name the direction and ground it in MODIFIES entries.

If a conflict surfaces here: invoke the REOPEN PROTOCOL before continuing.

Falsifiability test: *does any single ledger entry contain this conclusion?* If yes, revisit.

**Beat 4 — What remains uncertain**
*Conflicts carried forward (from closed register):*
Reproduce every UNRESOLVED scaffold verbatim.

*Additional gaps:*

```
Gap: [what is unknown]
Most exposed finding: [which ledger entry's claim cannot be confirmed without this]
Next signal: {namespace}/{skill} — [expected finding type]
```

**Beat 5 — Recommendation**
One of: **proceed**, **pause**, **pivot**, **abandon**.
One paragraph. Acts on the S3 hypothesis. Ground in the Beat 3 pattern and at least one
RESOLVED register row (cite by row number). The UNRESOLVED count from the closure stamp
(most recent: CLOSED or RE-CLOSED) sets the risk floor — name it.

If a conflict surfaces here: invoke the REOPEN PROTOCOL before stating the recommendation.

"It depends" without a stated default fails.

---

**Voice**: Active, opinionated. The `[REGISTER: OPEN]` / `[REGISTER CLOSED]` /
`[REGISTER RE-CLOSED]` markers are formal lifecycle events — not prose ornaments.
The REOPEN PROTOCOL is an interrupt, not a suggestion. Story beats carry the argument.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

**Working hypothesis (S0)**: [claim]

## Hypothesis Mutation Ledger
- `{artifact-name}`: {finding}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [Hypothesis update if MODIFIES]
...
**Hypothesis at S3**: [evolved claim]

## Conflict Register
[REGISTER CLOSED — {N} rows, {R} RESOLVED, {U} UNRESOLVED]
  [or [REGISTER RE-CLOSED — ...] if reopened during story]

| Row | Signal-A | Signal-B | Dimension | Verdict |
| 1 | `...` | `...` | [...] | RESOLVED · `{signal}` because [...] |
| 2 | `...` | `...` | [...] | — see UNRESOLVED scaffold — |

Row 2 — UNRESOLVED:
  Gap: [what is unknown]
  Most exposed finding: [which entry]
  Next signal: {namespace}/{skill} — [expected finding]

## Story

### Beat 1 — What we set out to understand
[*Gate confirmed: closure stamp present.*]
...

### Beat 2 — What each signal revealed
...

### Beat 3 — What the signals say together
[cross-signal pattern; RESOLVED rows applied; UNRESOLVED by row number only; REOPEN
PROTOCOL invoked if mid-prose conflict surfaces]

### Beat 4 — What remains uncertain
*Conflicts carried forward:*
Row 2 — UNRESOLVED:
  Gap: [verbatim]
  Most exposed finding: [verbatim]
  Next signal: [verbatim]

*Additional gaps:*
[entries or "none"]

### Beat 5 — Recommendation
**PROCEED | PAUSE | PIVOT | ABANDON** — [paragraph; UNRESOLVED count from most recent
stamp as risk floor; at least one RESOLVED row cited as warrant]
```

---

## V-04

**Variation axis**: Combination — V-01 (explicit OPEN/CLOSED lifecycle + pre-Story gate,
C-22) + V-02 (Domain Falsifier field in Pattern Gate, C-23) on the R8 V-04 base (mutation
ledger + because-clause adjudication + distributed prohibition guards + pre-seeded
UNRESOLVED scaffold)
**Hypothesis**: V-01 and V-02 are orthogonal: the register lifecycle (C-22) operates at
the structural boundary between the record phase and the prose phase, while the domain
falsifier (C-23) operates within the Pattern Gate content in Beat 3. Neither mechanism
interferes with the other. The R8 V-04 base already achieved C-20 (UNRESOLVED scaffold
format identity) and C-21 (distributed prohibition guards at Beat 3 and Beat 5 entry).
V-01 upgrades the register section of that base with an explicit OPEN declaration and a
pre-Story confirmation gate, adding C-22's lifecycle gate component (without reopen
protocol). V-02 upgrades the Beat 3 Pattern Gate with a Domain Falsifier field and
explicit prohibition on provenance conditions, closing C-23. Expected profile: full
inheritance of R8 V-04's C-17 (because-clause) + C-20 (scaffold) + C-21 (distributed
guards), plus C-22 (lifecycle gate) and C-23 (domain falsifier). The reopen protocol is
intentionally absent — this tests the combination ceiling without V-03's mechanism.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

### Step 1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### Step 2 — Hypothesis mutation ledger

Before writing the story, complete the ledger. Write it as the first section of the
artifact.

**Working hypothesis (S0)**: [one sentence — the specific claim the team entered with,
stated as a falsifiable assertion, not a goal or question]

For each signal artifact, in the order read:

```
- `{artifact-name}`: {key finding most relevant to the working hypothesis, one to two
  sentences}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [if MODIFIES]: Hypothesis update: [previous wording] → [updated wording]
```

After all entries:

```
Hypothesis at S3: [one sentence — working hypothesis after all stances are applied]
```

**Anti-stagnation check**: If S3 is identical to S0, state why. Silently identical S0
and S3 fails.

Do not open the Conflict Register until the ledger is complete.

---

### Step 3 — Conflict Register

Write the following declaration as the first line of the register section:

```
[REGISTER: OPEN]
```

List every tension between stances. For each tension, write one entry.

For RESOLVED rows:

```
| Row | Signal-A | Signal-B | Dimension | Verdict |
| {N} | `{artifact-A}` | `{artifact-B}` | [dimension] | RESOLVED · `{signal}` because [specific evidential reason — name the element from that signal that outweighs the alternative] |
```

For UNRESOLVED rows, fill the pre-seeded scaffold below the table row:

```
| {N} | `{artifact-A}` | `{artifact-B}` | [dimension] | — see UNRESOLVED scaffold — |

Row {N} — UNRESOLVED:
  Gap: [what is unknown — the specific question this conflict raises]
  Most exposed finding: [which ledger entry's claim cannot be confirmed without this]
  Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

**Format identity rule**: The filled UNRESOLVED scaffold IS the gap entry. Beat 4
reproduces every UNRESOLVED scaffold verbatim.

**Prohibition** (applies to all story beats): Every adjudication verdict must appear
as a named row in this register. Do not record conflict resolutions in prose narrative.

If no tensions exist, write: `Conflict Register: empty.`

When all entries are written, close the register:

```
[REGISTER CLOSED — {N} rows, {R} RESOLVED, {U} UNRESOLVED]
```

Verify: N = total rows, R + U = N.

---

### Step 4 — Write the story

**Pre-Story gate**: Confirm `[REGISTER CLOSED — ...]` is present above before writing
Beat 1. Do not begin if absent.

Write to `simulations/{topic}/{topic}-story-{date}.md`.

**Beat 1 — What we set out to understand**
One to three sentences. The original question and the S0 working hypothesis.

**Beat 2 — What each signal revealed**
One key finding plus one editorial sentence per signal. Two sentences maximum per signal.

**Beat 3 — What the signals say together**

> **Register only. Do not introduce new verdicts here.** If a conflict surfaces while
> writing this section, stop — add the row to the register above — then return and
> continue.

The cross-signal pattern. Reference at least two ledger entries. Draw a conclusion
derivable only from the full entry set.

Apply the register: RESOLVED rows are pattern evidence; cite their because-clauses.
UNRESOLVED rows are seated in Beat 4; reference by row number only.

The S0→S3 delta is your spine.

**Pattern Gate** — complete this block before writing any further sentences in Beat 3:

```
Pattern claim: [one declarative sentence naming the phenomenon]

Domain Falsifier: [one sentence naming a specific observable condition in the subject
  domain that, if observed, would demonstrate the pattern claim is incorrect]

  CONSTRAINT: The falsifier must be externally observable — in the world, market, or
  system under analysis. Do not name a condition about signal properties (provenance,
  source diversity, author overlap, or extraction method). "If all signals came from the
  same author" is a quality check, not a domain falsifier. The falsifier must be
  falsifying regardless of signal set composition.
```

After the Pattern Gate, continue the Beat 3 argument.

Falsifiability test: *does any single ledger entry contain this conclusion?* If yes, revisit.

**Beat 4 — What remains uncertain**
*Conflicts carried forward:*
Reproduce every UNRESOLVED scaffold verbatim.

*Additional gaps:*

```
Gap: [what is unknown]
Most exposed finding: [which ledger entry's claim cannot be confirmed without this]
Next signal: {namespace}/{skill} — [expected finding type]
```

**Beat 5 — Recommendation**

> **Register only. Do not introduce new verdict reasoning here.** Cite register rows by
> row number. If new reasoning is required, return to the register.

One of: **proceed**, **pause**, **pivot**, **abandon**.
One paragraph. Acts on the S3 hypothesis. Ground in the Beat 3 pattern, the Domain
Falsifier, and at least one RESOLVED register row (cite by row number). The UNRESOLVED
count from the closure stamp sets the risk floor — name it.
"It depends" without a stated default fails.

---

**Voice**: Active, opinionated. The lifecycle markers are formal artifact events. The
Domain Falsifier in the Pattern Gate is a named, externally observable accountability
line — not a hedge. Story beats carry the argument.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

**Working hypothesis (S0)**: [claim]

## Hypothesis Mutation Ledger
- `{artifact-name}`: {finding}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [Hypothesis update if MODIFIES]
...
**Hypothesis at S3**: [evolved claim]

## Conflict Register
[REGISTER: OPEN]
| Row | Signal-A | Signal-B | Dimension | Verdict |
| 1 | `...` | `...` | [...] | RESOLVED · `{signal}` because [...] |
| 2 | `...` | `...` | [...] | — see UNRESOLVED scaffold — |

Row 2 — UNRESOLVED:
  Gap: [what is unknown]
  Most exposed finding: [which entry]
  Next signal: {namespace}/{skill} — [expected finding]

[REGISTER CLOSED — 2 rows, 1 RESOLVED, 1 UNRESOLVED]

## Story

### Beat 1 — What we set out to understand
[*Gate confirmed.*]
...

### Beat 2 — What each signal revealed
...

### Beat 3 — What the signals say together
> Register only. Do not introduce new verdicts here.

**Pattern Gate**
Pattern claim: [one declarative sentence]
Domain Falsifier: [externally observable domain condition]

[continuation — RESOLVED rows applied; UNRESOLVED by row number only]

### Beat 4 — What remains uncertain
*Conflicts carried forward:*
Row 2 — UNRESOLVED: [verbatim]

*Additional gaps:*
[entries or "none"]

### Beat 5 — Recommendation
> Register only. Do not introduce new verdict reasoning here.
**PROCEED | PAUSE | PIVOT | ABANDON** — [paragraph; risk floor named; RESOLVED row cited]
```

---

## V-05

**Variation axis**: Full combination — V-03 (full C-22: OPEN/CLOSED lifecycle + pre-Story
gate + REOPEN PROTOCOL) + V-02 (C-23: Domain Falsifier in Pattern Gate) on the R8 V-05
base (EVALUATOR/AUTHOR phase split + Signal Extract visible as artifact section)
**Hypothesis**: V-04 establishes that C-22 (lifecycle gate) and C-23 (domain falsifier)
can be added to the R8 V-04 base without structural conflict. V-05 tests whether the full
C-22 specification — including the REOPEN PROTOCOL for mid-prose conflicts — plus C-23
can be integrated into the R8 V-05 EVALUATOR/AUTHOR architecture. In the EVALUATOR/AUTHOR
split, the EVALUATOR phase produces the formal records (ledger, register) and the AUTHOR
phase writes prose against those records. The lifecycle gate belongs at the boundary: the
EVALUATOR phase formally closes the register before handing off to the AUTHOR phase. The
REOPEN PROTOCOL bridges phases: if the AUTHOR encounters a mid-prose conflict, the
protocol routes execution back to the register (EVALUATOR-domain), appends and closes,
then returns to the AUTHOR. The Domain Falsifier is an AUTHOR artifact produced in the
Pattern Gate. The hypothesis is that the EVALUATOR/AUTHOR split provides a natural
architectural home for the lifecycle transition: EVALUATOR closes the register as its
final act; AUTHOR cannot begin until EVALUATOR's closure stamp is present; the REOPEN
PROTOCOL is an AUTHOR-to-EVALUATOR interrupt with a defined return path.

---

You are running `/topic:story` for a topic. The topic name is provided.

---

## EVALUATOR PHASE

Complete the EVALUATOR phase in full before beginning the AUTHOR phase. The EVALUATOR
phase produces formal records; the AUTHOR phase writes prose against them. The AUTHOR
may not begin until all EVALUATOR records are complete and the register is closed.

---

### E1 — Gather

Glob `simulations/**/{topic}-*`. Read every artifact found.
Also read `simulations/{topic}/strategy.md` if present.

---

### E2 — Hypothesis mutation ledger

**Working hypothesis (S0)**: [one sentence — the specific claim the team entered with,
stated as a falsifiable assertion, not a goal or question]

For each artifact, in the order read:

```
- `{artifact-name}`: {key finding most relevant to the working hypothesis, one to two
  sentences}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [if MODIFIES]: Hypothesis update: [previous wording] → [updated wording]
```

```
Hypothesis at S3: [one sentence — working hypothesis after all stances are applied]
```

**Anti-stagnation check**: If S3 is identical to S0, state why. Silently identical S0
and S3 fails.

---

### E3 — Signal Extract

Write a Signal Extract table as a named section of the artifact. This section is the
AUTHOR's reference; the AUTHOR reads it rather than returning to source signals.

```
| Signal | Artifact | Key Finding | Stance | Inertia Marker |
| {label} | `{artifact-name}` | [one sentence — the claim most relevant to the hypothesis] | CONFIRMS / MODIFIES / CONTRADICTS | [what was believed or established BEFORE this signal, in one phrase; or "—" if no prior state] |
```

One row per artifact. Every artifact gets exactly one row.

---

### E4 — Conflict Register

Write the following declaration as the first line of the register section:

```
[REGISTER: OPEN — accepting entries]
```

Scan the Signal Extract for tensions (CONFIRMS vs CONTRADICTS, or competing MODIFIES
entries). For each tension, write one row.

For RESOLVED rows:

```
| Row | Signal-A | Signal-B | Dimension | Verdict |
| {N} | `{artifact-A}` | `{artifact-B}` | [dimension] | RESOLVED · `{signal}` because [specific evidential reason — name the element from that signal that outweighs the alternative] |
```

For UNRESOLVED rows, fill the pre-seeded scaffold below the table row:

```
| {N} | `{artifact-A}` | `{artifact-B}` | [dimension] | — see UNRESOLVED scaffold — |

Row {N} — UNRESOLVED:
  Gap: [what is unknown — the specific question this conflict raises]
  Most exposed finding: [which Signal Extract row's claim cannot be confirmed without this]
  Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

**Format identity rule**: The filled UNRESOLVED scaffold IS the gap entry. Beat 4
reproduces every UNRESOLVED scaffold verbatim.

**Prohibition**: Every verdict must appear as a named row in this register. No conflict
resolutions in prose.

If no tensions exist, write: `Conflict Register: empty.`

**EVALUATOR CLOSURE** — When all entries are written, formally close the register:

```
[REGISTER CLOSED — {N} rows, {R} RESOLVED, {U} UNRESOLVED]
[EVALUATOR PHASE COMPLETE — AUTHOR MAY BEGIN]
```

Verify counts before writing: N = total rows, R + U = N.

**REOPEN PROTOCOL** — if the AUTHOR encounters a mid-prose conflict during the AUTHOR
phase:

1. **HALT** — stop at the current sentence in the current beat.
2. **APPEND** — add a new row to the register (RESOLVED or UNRESOLVED with scaffold).
3. **RE-CLOSE** — replace the current stamp with:
   `[REGISTER RE-CLOSED — {N} rows, {R} RESOLVED, {U} UNRESOLVED]`
   Replace `[AUTHOR MAY BEGIN]` with `[AUTHOR MAY RESUME]`.
4. **RESUME** — return to the halt point in the beat and continue.

Absorbing a mid-prose conflict in narrative without invoking the REOPEN PROTOCOL is a
protocol violation.

---

## AUTHOR PHASE

**Phase gate**: Confirm `[EVALUATOR PHASE COMPLETE — AUTHOR MAY BEGIN]` (or
`[AUTHOR MAY RESUME]`) is present above. Do not begin Beat 1 if the gate line is absent.

Write to `simulations/{topic}/{topic}-story-{date}.md`.

The Signal Extract (E3) is your reference for signal findings. Read from it rather than
returning to source artifacts. The Conflict Register (E4) is your adjudication record —
apply it; do not expand or contradict it except via the REOPEN PROTOCOL.

---

**Beat 1 — What we set out to understand**
One to three sentences. The original question and the S0 working hypothesis. Name the
entering claim as a falsifiable assertion, not a goal.

**Beat 2 — What each signal revealed**
Draw from the Signal Extract. For each row: the key finding plus one editorial sentence
on what it means for the hypothesis — what does this signal reveal about the direction
the signals are moving? Two sentences maximum per signal.

Reference the inertia markers where they exist: a marker names what was believed before
this signal changed the picture. The contrast between the inertia marker and the finding
is itself a signal.

**Beat 3 — What the signals say together**

> **Register only. Do not introduce new verdicts here.** If a conflict surfaces while
> writing this beat, invoke the REOPEN PROTOCOL — halt, append, re-close — then resume.

The cross-signal pattern. Reference at least two Signal Extract rows by artifact name.
Draw a conclusion derivable only from the full extract, not from any single row.

Apply the register: RESOLVED rows are pattern evidence; cite their because-clauses as
part of the argument. UNRESOLVED rows are seated in Beat 4; reference by row number only.

The S0→S3 delta is your spine — name the direction and ground it in MODIFIES entries from
the ledger.

**Pattern Gate** — complete this block before writing any further sentences in Beat 3:

```
Pattern claim: [one declarative sentence naming the phenomenon]

Domain Falsifier: [one sentence naming a specific observable condition in the subject
  domain that, if observed, would demonstrate the pattern claim is incorrect]

  CONSTRAINT: Name something external to this signal set — observable in the world,
  market, or system under analysis. Do not name a signal-provenance condition (source
  diversity, author overlap, extraction method). The falsifier must apply regardless of
  how diverse or independent the signal set is. A domain falsifier answers: "what would
  we observe in the subject domain if this pattern were wrong?"
```

After the Pattern Gate, continue the Beat 3 argument grounding the pattern in the S0→S3
delta and RESOLVED register rows.

Falsifiability test: *does any single Signal Extract row contain this conclusion?* If
yes, revisit.

**Beat 4 — What remains uncertain**
Two categories, kept separate:

*Conflicts carried forward (from closed register):*
Reproduce every UNRESOLVED scaffold verbatim — the three-line block exactly as written.

*Additional gaps (not sourced from conflict):*

```
Gap: [what is unknown — not covered by any Signal Extract row and not yet adjudicated]
Most exposed finding: [which Signal Extract row's claim cannot be confirmed without this]
Next signal: {namespace}/{skill} — [one sentence: expected finding type]
```

If no additional gaps, write: `Additional gaps: none.`

Adjudicated debates from the register do not appear here. The exclusion rule is symmetric
with the inclusion rule: closed items stay in the register; open items stay in Beat 4.

**Beat 5 — Recommendation**

> **Register only. Do not introduce new verdict reasoning here.** If new reasoning
> surfaces, invoke the REOPEN PROTOCOL first. Cite register rows by row number.

One of: **proceed**, **pause**, **pivot**, **abandon**.
One paragraph. Acts on the S3 hypothesis, not S0. Ground the recommendation in the Beat 3
pattern and the Domain Falsifier (name it: what would flip the recommendation). Cite at
least one RESOLVED register row as causal warrant (row number). The UNRESOLVED count from
the most recent closure stamp (CLOSED or RE-CLOSED) is the risk floor — name it.

"It depends" without a stated default fails. "Proceed with caution" without naming the
specific risk from the UNRESOLVED count fails.

---

**Voice**: Active, opinionated. The EVALUATOR records are terse and formal. The AUTHOR's
prose is editorial — an argument built against auditable records. The lifecycle markers
(`[REGISTER: OPEN]`, `[REGISTER CLOSED]`, `[EVALUATOR PHASE COMPLETE]`) are structural
events, not prose. The Domain Falsifier in the Pattern Gate is the pattern claim's
accountability line — it is the single observable condition the author commits to as the
claim's failure mode.

Artifact: `simulations/{topic}/{topic}-story-{date}.md`

```markdown
# {Topic} Story
*As of {date}. {N} signals synthesized.*

---
## EVALUATOR RECORDS

**Working hypothesis (S0)**: [claim]

### Hypothesis Mutation Ledger
- `{artifact-name}`: {finding}
  Stance: CONFIRMS | MODIFIES | CONTRADICTS
  [Hypothesis update if MODIFIES]
...
**Hypothesis at S3**: [evolved claim]

### Signal Extract
| Signal | Artifact | Key Finding | Stance | Inertia Marker |
| S1 | `...` | [...] | CONFIRMS | [...] |
| S2 | `...` | [...] | MODIFIES | [...] |
...

### Conflict Register
[REGISTER: OPEN — accepting entries]
| Row | Signal-A | Signal-B | Dimension | Verdict |
| 1 | `...` | `...` | [...] | RESOLVED · `{signal}` because [...] |
| 2 | `...` | `...` | [...] | — see UNRESOLVED scaffold — |

Row 2 — UNRESOLVED:
  Gap: [what is unknown]
  Most exposed finding: [which row]
  Next signal: {namespace}/{skill} — [expected finding]

[REGISTER CLOSED — 2 rows, 1 RESOLVED, 1 UNRESOLVED]
[EVALUATOR PHASE COMPLETE — AUTHOR MAY BEGIN]

---
## STORY

### Beat 1 — What we set out to understand
...

### Beat 2 — What each signal revealed
[from Signal Extract; inertia markers referenced where present]

### Beat 3 — What the signals say together
> Register only. Do not introduce new verdicts here.

**Pattern Gate**
Pattern claim: [one declarative sentence]
Domain Falsifier: [externally observable condition in the subject domain]

[continuation; RESOLVED rows applied; UNRESOLVED by row number only]

### Beat 4 — What remains uncertain
*Conflicts carried forward:*
Row 2 — UNRESOLVED: [verbatim scaffold]

*Additional gaps:*
[entries or "none"]

### Beat 5 — Recommendation
> Register only. Do not introduce new verdict reasoning here.
**PROCEED | PAUSE | PIVOT | ABANDON** — [paragraph; Domain Falsifier named as flip
condition; UNRESOLVED count as risk floor; RESOLVED row cited as warrant]
```
