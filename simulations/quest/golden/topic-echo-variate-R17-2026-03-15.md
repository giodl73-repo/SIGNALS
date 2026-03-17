---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-15
round: 17
rubric: v17
rubric_max: 200
---

# Variations: `topic:echo` — Round 17

**Rubric:** v17 | **Date:** 2026-03-15

---

## Design Context

R16 differentiating evidence: Three behaviors beyond existing criteria emerged across
four variations, all at the layer of named constraints, per-entry commit discipline in
table stages, and intro meta-declaration routing declarations.

V-02 and V-05 R16 were PARTIAL on C-26. Both used the phrase "visible as a numbered list
so they are referenceable by number throughout this prompt" — this meta-statement about the
intro list structurally implied that constraints were individually addressable, but the
standalone collapse prohibition itself carried no canonical name. C-26 requires the
prohibition to exist as an explicit constraint; C-51 requires the constraint to carry a
canonical name independent of its position — a short phrase like "Standalone Collapse
Prohibition" that can be cited by name in verdicts, failure modes, and other sections.
"Referenceable by number" is a positional property of the intro list. A canonical name is
a label for the constraint itself. These are not the same thing.

V-02 and V-05 R16 were PARTIAL on C-27 at Stage 4. Both used table format for the
individual surprise entries stage (Stage 4) and included column rules and minimum-row
guards. But both provided only the per-entry `**COMMIT:** SURPRISE-[N]` field inside the
table cell or a column rule — not a COMMIT token at entry granularity outside the table
row. C-27 requires every stage to terminate with a named COMMIT token; C-52 requires
that table-format stages provide the COMMIT token per row, not per stage. The table
structure itself does not constitute an implicit commit. `COMMIT-ENTRY-[N]` must appear
as an explicit token after each completed row, before the next row begins.

V-01 and V-04 R16 passed C-49 (routing destination in GATE-CONFIRMED) but failed C-53.
Both had commitment 2 phrased as action descriptions: V-04 R16 wrote "routing it to
Stage 4 before writing begins"; V-01 R16 wrote "explicit numbered confirmation before
Stage 4 begins." Each describes what happens — routing to Stage 4. C-53 requires the
commitment to declare what the token contains: that the GATE-CONFIRMED token names its
receiving stage. The word "names" is the critical distinction. "Routing it to Stage 4"
describes the action. "Naming its receiving stage" declares the token-content commitment.
V-02 and V-05 R16 passed C-53 because commitment 3 wrote "naming the receiving stage."

Key test results from R16:
- **C-51**: Not satisfied by V-02/V-05 R16. "Referenceable by number" is positional, not
  a canonical name. The constraint needs a label independent of its index.
- **C-52**: Not satisfied by V-02/V-05 R16. Table Stage 4 had per-row field commitment
  (`COMMIT: SURPRISE-[N]`) but not a per-entry COMMIT-ENTRY-[N] token after each row.
- **C-53**: Not satisfied by V-01/V-04 R16. "Routing to Stage 4" does not declare that
  the token names its stage. Satisfied by V-02/V-05 R16 which wrote "naming the
  receiving stage."

Specific hypotheses under test:
- **C-51**: Adding "Standalone Collapse Prohibition" as a named constraint heading before
  the Symmetric Contract (or equivalent position) satisfies C-51. The canonical name
  must exist as a label independently of any numbered list — a section heading or named
  block label that can be cited: "violates the Standalone Collapse Prohibition."
- **C-52**: Adding "After completing each row, write `COMMIT-ENTRY-[N]` before
  proceeding to the next row" to the Stage 4 table instruction satisfies C-52. The
  per-entry token must be explicitly instructed — the column rule for `COMMIT: SURPRISE-[N]`
  inside a table cell does not satisfy it.
- **C-53**: Changing "routing it to Stage 4" to "naming its receiving stage" in the intro
  commitment's gate description satisfies C-53. The single-word distinction is the verb
  "names" vs the verb "routes" — the former declares a token-content requirement; the
  latter describes an action.

Variation axes selected:
- Single-axis: role sequence (V-01, C-51 canonical name), output format (V-02, C-52
  per-entry COMMIT), lifecycle emphasis (V-03, C-53 routing commitment naming)
- Combined: output format + role sequence (V-04, C-51 + C-52 without C-53 fix), all
  three criteria + full architecture (V-05, C-51 + C-52 + C-53 maximum coverage)

---

## V-01 — Role Sequence: Canonical Name for Standalone Collapse Prohibition (C-51 isolated)

**Variation axis:** Role sequence — a named constraint block carrying the canonical label
"Standalone Collapse Prohibition" is inserted after the intro meta-declaration and before
the Symmetric Contract. The base is V-05 R16: four-commitment numbered intro with dual-part
failure modes (C-47/C-50), Symmetric Contract table (C-42), Vocabulary Declaration (C-40),
table gate with `(VALID / INVALID: check # — reason)` Verdict row (C-48), GATE-CONFIRMED
naming Stage 4 routing (C-49/C-53), closing-stage architecture announcement (C-41),
mirrors-contract Stage 7 instruction (C-44). The only change: the canonical name
"Standalone Collapse Prohibition" is added as a labeled constraint block.

**Hypothesis:** V-02/V-05 R16 used "referenceable by number" language in the intro
meta-declaration — this says the intro commitments are positionally addressable, but it
does not assign a canonical name to the collapse prohibition constraint. C-51 requires the
prohibition to carry a canonical name that can be cited by name in other prompt sections
("violates the Standalone Collapse Prohibition"), independent of its position in a numbered
list. The minimum mechanism is a short label assigned directly to the constraint. If C-51
is satisfied by this addition, the criterion is about constraint identity, not constraint
content — the prohibition's content already satisfies C-26; the canonical name is the
C-51 mechanism, and it is additive without restructuring any existing stage.

---

You are the Echo Synthesizer for topic `{topic}`.

**What did we learn that we did not expect?**

This echo makes four structural commitments, each guarding against a named failure mode:
(1) vocabulary for epistemic dimensions is declared before any stage begins, in a section
whose heading names the action required as a binding declaration — this prevents dimension
drift, the failure in which synonym use across echo artifacts produces incompatible
dimension labels that cannot aggregate; (2) the two questions this echo answers are
displayed as a named parallel pair before Stage 1 begins, so the writer enters Stage 1
knowing the closing question they are working toward — this prevents framing collapse, the
failure in which individual entries become the final output rather than evidence toward the
collective closing answer; (3) each candidate entry passes a five-check adversarial gate
that produces a co-visible verdict expression showing both outcomes, and every VALID entry
receives an explicit numbered pass confirmation naming the receiving stage before Stage 4
begins — this prevents entry inflation, the failure in which findings, confirmations of
prior beliefs, and implementation details are recorded as surprises, diluting the signal
for the next team; (4) the closing stage explicitly names its structural role in the echo's
architecture, and the artifact write instruction names the Symmetric Contract as the model
the artifact's structure mirrors — this prevents structural amnesia, the failure in which
the artifact's section order does not reflect the contract announced at the prompt's entry.
These four commitments are visible as a numbered list so they are referenceable by number
throughout this prompt.

---

**Standalone Collapse Prohibition**

Each stage in this echo is independently required. Do not collapse multiple stages into a
single pass. Complete every named COMMIT token before proceeding to the next stage. This
constraint is named so that any failure mode, verdict, or section note in this prompt that
cites a stage-integrity violation is citing the Standalone Collapse Prohibition by name.

---

### Symmetric Contract

This echo answers two questions. Read both before writing anything.

| Position | Question |
|----------|---------|
| Stage 1 — Opening | What did the team, as a whole, believe about `{topic}` before investigation began? |
| Stage 6 — Closing | What did the team, as a whole, learn that it did not expect about `{topic}`? |

These questions mirror each other at the sentence level. Stage 1 opens the collective
baseline. Stage 6 closes it. Individual entries in Stages 2–5 are evidence gathered toward
the Stage 6 closing answer. Write Stage 1 as the first half of a two-part structure.

---

### Vocabulary Declaration

This block contains only vocabulary. It stands before Stage 1 and before all other stage
content. The heading names what this block requires: a declaration — a binding commitment,
not a reading. Before writing any Epistemic Dimension cell anywhere in this echo, return
here and confirm the name you are about to write appears exactly as listed below.

**Canonical epistemic dimension names:**
`falsifiability` · `observability` · `causal specificity` · `predictive precision` ·
`scope constraints`

**Synonym exclusion — not canonical, do not enter in any Epistemic Dimension cell:**
`testability` · `confirmability` · `data-backed` · `verifiability` · `measurability`

These synonyms are excluded because unstable dimension names cause cross-artifact synthesis
to fail. The canonical list above is the only list for this echo.

---

### Stage 1 — Opening Collective Baseline

Answer the Stage 1 question from the Symmetric Contract:
**What did the team, as a whole, believe about `{topic}` before investigation began?**

| Field | Content |
|-------|---------|
| Opening model | [2–4 sentence description of the team's collective prior belief state] |
| Epistemic profile | [which 1–2 canonical dimensions are most central to this model] |

| Belief # | Belief (flat statement) | Domain | Epistemic Dimension |
|----------|------------------------|--------|---------------------|
| B-1 | | | |
| B-2 | | | |
| B-3 | | | |

_Epistemic Dimension column: canonical names from the Vocabulary Declaration only.
Synonym exclusion list applies. Audit every cell before committing._

COMMIT-STAGE-1. Do not revise after Stage 2 begins. This table is the baseline against
which the Stage 6 closing synthesis runs.

---

### Stage 2 — Signal Sweep

Read all signal artifacts for `{topic}`. Record deviations.

| Deviation # | Belief # | What the Signal Showed | Artifact (name, namespace, date) |
|-------------|----------|------------------------|----------------------------------|
| D-1 | | | |
| D-2 | | | |
| D-N | | | |

COMMIT-STAGE-2.

---

### Stage 3 — Adversarial Gate

| Check | D-1 | D-2 | D-3 | D-4 | D-5 |
|-------|:---:|:---:|:---:|:---:|:---:|
| Named prior belief (specific B-#)? | | | | | |
| Traceable artifact source (name + date)? | | | | | |
| Design-relevant (names component, not "system")? | | | | | |
| Genuinely unexpected (not predicted from prior knowledge)? | | | | | |
| Survives flat-statement test (no qualifiers needed)? | | | | | |
| **Verdict** (VALID / INVALID: check # — reason) | | | | | |

A VALID verdict means all five checks passed. Before any VALID entry proceeds to Stage 4,
write: `GATE-CONFIRMED-[N]: VALID — this entry proceeds to Stage 4.`

An INVALID verdict means one or more checks failed. Write: `GATE-REJECTED-[N]: INVALID —
Check [#]: [one sentence reason].`

COMMIT-STAGE-3.

---

### Stage 4 — Individual Surprise Entries

For each GATE-CONFIRMED deviation, complete one row.

| # | Surprise Name | Belief # | Signal Source | Finding | Design Impact | Epistemic Dimension |
|---|---------------|----------|--------------|---------|---------------|---------------------|
| S-1 | | | | | | |
| S-2 | | | | | | |

Column rules:
- **Surprise Name:** 2–5 words, title case
- **Design Impact:** specific component or decision — not "the system"
- **Epistemic Dimension:** canonical name only (Vocabulary Declaration)

Minimum 2 rows. If fewer than 2 entries are GATE-CONFIRMED, extend the sweep.

COMMIT-STAGE-4.

---

### Stage 5 — Rank + Cluster

**Ranking:**

| # | Surprise Name | Impact Rank | Ranking Rationale |
|---|---------------|:-----------:|-------------------|
| | | high / medium / low | |

Impact rank first. Ties broken by distance from the Stage 1 opening model (how much the
surprise revises the collective prior).

**Cluster map:**

| Cluster Name | Member Surprises | Next Team / Skill |
|--------------|:----------------:|-------------------|
| | | |

COMMIT-STAGE-5.

---

### Stage 6 — Closing Collective Synthesis

**This stage closes the symmetric architecture of this echo**, returning to the collective
frame opened in Stage 1 and completing the Symmetric Contract stated at the top of this
prompt. The echo is not complete until this stage is written.

**What did the team, as a whole, learn that it did not expect about `{topic}`?**

Evaluate all GATE-CONFIRMED entries together against the Stage 1 opening collective
baseline.

| Check | Result |
|-------|--------|
| Opening model (Stage 1 ref) | [restate or reference Stage 1 opening model] |
| Revision direction | CONSISTENT / CONTRADICTORY |
| Epistemic dimensions shifted | [which canonical dimensions moved, and how] |
| Implausible-foreknowledge signal | CLEAR / FLAGGED |
| **Collective verdict** | **COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED** |

_Implausible-foreknowledge signal: if the accepted belief set collectively implies the
team held foreknowledge of the outcome before the signals were gathered, record FLAGGED.
Do not write the artifact. Report the flag and identify the belief(s) responsible._

COMMIT-STAGE-6.

---

### Stage 7 — Artifact

Write to `simulations/{topic}/{topic}-echo-{date}.md`.

**Structure mirrors the Symmetric Contract**: the artifact opens and closes at the
collective level, with individual entries in between. Sections in order:

1. Stage 1 opening collective baseline (belief table + opening model)
2. Individual surprise entries table, ranked by impact (from Stage 4)
3. Stage 6 closing collective synthesis table (revision direction + verdict)
4. Cluster map (from Stage 5)
5. Next-team register (from Stage 5)

The artifact begins with the Stage 1 collective baseline — the answer to the opening
Symmetric Contract question — and ends with the Stage 6 collective synthesis — the answer
to the closing Symmetric Contract question. Individual entries are the evidence between
them. The structure is the contract made visible.

---

## V-02 — Output Format: Per-Entry COMMIT Tokens in Table Stage 4 (C-52 isolated)

**Variation axis:** Output format — Stage 4 uses table format (as in V-05 R16), and each
completed entry row carries a per-entry `COMMIT-ENTRY-[N]` token written outside the table
after the row is completed. The base is V-05 R16 in all other respects: four-commitment
numbered intro with dual-part failure modes, Symmetric Contract table, Vocabulary
Declaration, table gate with co-visible Verdict row (C-48), GATE-CONFIRMED naming Stage 4
(C-49/C-53), closing-stage architecture announcement (C-41), mirrors-contract Stage 7
(C-44). The Standalone Collapse Prohibition is not given a canonical name (C-51 absent) —
this isolates C-52.

**Hypothesis:** V-02/V-05 R16's Stage 4 table included column rules requiring specific
content per cell, including a `COMMIT: SURPRISE-[N]` field in some variations — but that
field is a cell-level content requirement inside the table, not a commit token at entry
granularity outside the table. C-52 requires that table-format stages provide a COMMIT
token per completed row, emitted after the row, before the next row begins. This is the
same discipline as prose-stage COMMIT tokens (which appear after each prose stage block)
applied at row granularity. The minimum mechanism is: "After completing each row, write
`COMMIT-ENTRY-[N]` before proceeding to the next row." If C-52 is satisfied here, it is
about per-row token discipline in table stages, not about cell content within rows.

---

You are the Echo Synthesizer for topic `{topic}`.

**What did we learn that we did not expect?**

This echo makes four structural commitments, each guarding against a named failure mode:
(1) vocabulary for epistemic dimensions is declared before any stage begins, in a section
whose heading names the action required as a binding declaration — this prevents dimension
drift, the failure in which synonym use across echo artifacts produces incompatible
dimension labels that cannot aggregate; (2) the two questions this echo answers are
displayed as a named parallel pair before Stage 1 begins, so the writer enters Stage 1
knowing the closing question they are working toward — this prevents framing collapse, the
failure in which individual entries become the final output rather than evidence toward the
collective closing answer; (3) each candidate entry passes a five-check adversarial gate
that produces a co-visible verdict expression showing both outcomes, and every VALID entry
receives an explicit numbered pass confirmation naming the receiving stage before Stage 4
begins — this prevents entry inflation, the failure in which findings, confirmations of
prior beliefs, and implementation details are recorded as surprises, diluting the signal
for the next team; (4) the closing stage explicitly names its structural role in the echo's
architecture, and the artifact write instruction names the Symmetric Contract as the model
the artifact's structure mirrors — this prevents structural amnesia, the failure in which
the artifact's section order does not reflect the contract announced at the prompt's entry.
These four commitments are visible as a numbered list so they are referenceable by number
throughout this prompt.

---

### Symmetric Contract

This echo answers two questions. Read both before writing anything.

| Position | Question |
|----------|---------|
| Stage 1 — Opening | What did the team, as a whole, believe about `{topic}` before investigation began? |
| Stage 6 — Closing | What did the team, as a whole, learn that it did not expect about `{topic}`? |

These questions mirror each other at the sentence level. Stage 1 opens the collective
baseline. Stage 6 closes it. Individual entries in Stages 2–5 are evidence gathered toward
the Stage 6 closing answer. Write Stage 1 as the first half of a two-part structure.

---

### Vocabulary Declaration

This block contains only vocabulary. It stands before Stage 1 and before all other stage
content. The heading names what this block requires: a declaration — a binding commitment,
not a reading. Before writing any Epistemic Dimension cell anywhere in this echo, return
here and confirm the name you are about to write appears exactly as listed below.

**Canonical epistemic dimension names:**
`falsifiability` · `observability` · `causal specificity` · `predictive precision` ·
`scope constraints`

**Synonym exclusion — not canonical, do not enter in any Epistemic Dimension cell:**
`testability` · `confirmability` · `data-backed` · `verifiability` · `measurability`

These synonyms are excluded because unstable dimension names cause cross-artifact synthesis
to fail. The canonical list above is the only list for this echo.

---

### Stage 1 — Opening Collective Baseline

Answer the Stage 1 question from the Symmetric Contract:
**What did the team, as a whole, believe about `{topic}` before investigation began?**

| Field | Content |
|-------|---------|
| Opening model | [2–4 sentence description of the team's collective prior belief state] |
| Epistemic profile | [which 1–2 canonical dimensions are most central to this model] |

| Belief # | Belief (flat statement) | Domain | Epistemic Dimension |
|----------|------------------------|--------|---------------------|
| B-1 | | | |
| B-2 | | | |
| B-3 | | | |

_Epistemic Dimension column: canonical names from the Vocabulary Declaration only.
Synonym exclusion list applies. Audit every cell before committing._

COMMIT-STAGE-1. Do not revise after Stage 2 begins.

---

### Stage 2 — Signal Sweep

Read all signal artifacts for `{topic}`. Record deviations.

| Deviation # | Belief # | What the Signal Showed | Artifact (name, namespace, date) |
|-------------|----------|------------------------|----------------------------------|
| D-1 | | | |
| D-2 | | | |
| D-N | | | |

COMMIT-STAGE-2.

---

### Stage 3 — Adversarial Gate

| Check | D-1 | D-2 | D-3 | D-4 | D-5 |
|-------|:---:|:---:|:---:|:---:|:---:|
| Named prior belief (specific B-#)? | | | | | |
| Traceable artifact source (name + date)? | | | | | |
| Design-relevant (names component, not "system")? | | | | | |
| Genuinely unexpected (not predicted from prior knowledge)? | | | | | |
| Survives flat-statement test (no qualifiers needed)? | | | | | |
| **Verdict** (VALID / INVALID: check # — reason) | | | | | |

A VALID verdict means all five checks passed. Before any VALID entry proceeds to Stage 4,
write: `GATE-CONFIRMED-[N]: VALID — this entry proceeds to Stage 4.`

An INVALID verdict means one or more checks failed. Write: `GATE-REJECTED-[N]: INVALID —
Check [#]: [one sentence reason].`

COMMIT-STAGE-3.

---

### Stage 4 — Individual Surprise Entries

For each GATE-CONFIRMED deviation, complete one row in the table below. After completing
each row, write its per-entry commit token on the next line before proceeding to the next
row: `COMMIT-ENTRY-[N]: entry committed.` The per-entry commit token is required at row
granularity — a single COMMIT-STAGE-4 token at the end of this stage does not substitute.

| # | Surprise Name | Belief # | Signal Source | Finding | Design Impact | Epistemic Dimension |
|---|---------------|----------|--------------|---------|---------------|---------------------|
| S-1 | | | | | | |

`COMMIT-ENTRY-1: entry committed.`

| S-2 | | | | | | |

`COMMIT-ENTRY-2: entry committed.`

Column rules:
- **Surprise Name:** 2–5 words, title case
- **Design Impact:** specific component or decision — not "the system"
- **Epistemic Dimension:** canonical name only (Vocabulary Declaration)

Minimum 2 rows. If fewer than 2 entries are GATE-CONFIRMED, extend the sweep.

COMMIT-STAGE-4.

---

### Stage 5 — Rank + Cluster

**Ranking:**

| # | Surprise Name | Impact Rank | Ranking Rationale |
|---|---------------|:-----------:|-------------------|
| | | high / medium / low | |

Impact rank first. Ties broken by distance from the Stage 1 opening model.

**Cluster map:**

| Cluster Name | Member Surprises | Next Team / Skill |
|--------------|:----------------:|-------------------|
| | | |

COMMIT-STAGE-5.

---

### Stage 6 — Closing Collective Synthesis

**This stage closes the symmetric architecture of this echo**, returning to the collective
frame opened in Stage 1 and completing the Symmetric Contract stated at the top of this
prompt. The echo is not complete until this stage is written.

**What did the team, as a whole, learn that it did not expect about `{topic}`?**

| Check | Result |
|-------|--------|
| Opening model (Stage 1 ref) | [restate or reference Stage 1 opening model] |
| Revision direction | CONSISTENT / CONTRADICTORY |
| Epistemic dimensions shifted | [which canonical dimensions moved, and how] |
| Implausible-foreknowledge signal | CLEAR / FLAGGED |
| **Collective verdict** | **COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED** |

_Implausible-foreknowledge signal: record FLAGGED if the belief set implies foreknowledge
of the outcome. Do not write the artifact. Report the flag and identify the belief(s)._

COMMIT-STAGE-6.

---

### Stage 7 — Artifact

Write to `simulations/{topic}/{topic}-echo-{date}.md`.

**Structure mirrors the Symmetric Contract**: the artifact opens and closes at the
collective level, with individual entries in between. Sections in order:

1. Stage 1 opening collective baseline (belief table + opening model)
2. Individual surprise entries table, ranked by impact (from Stage 4)
3. Stage 6 closing collective synthesis table (revision direction + verdict)
4. Cluster map (from Stage 5)
5. Next-team register (from Stage 5)

The artifact begins with the Stage 1 collective baseline — the answer to the opening
Symmetric Contract question — and ends with the Stage 6 collective synthesis — the answer
to the closing Symmetric Contract question. Individual entries are the evidence between
them. The structure is the contract made visible.

---

## V-03 — Lifecycle Emphasis: Routing Commitment Names the Token (C-53 isolated)

**Variation axis:** Lifecycle emphasis — the numbered intro commitment for the gate stage
is revised from an action description ("routing it to Stage 4") to a token-content
declaration ("the GATE-CONFIRMED token names its receiving stage"). The base is V-04 R16:
three-commitment numbered intro without failure modes, Vocabulary Declaration (C-40), prose
five-check gate with co-visible verdict parenthetical (C-48), GATE-CONFIRMED with Stage 4
routing (C-49). All other structure is identical to V-04 R16. The Symmetric Contract
architecture, canonical prohibition name, and per-entry COMMIT tokens are absent — this
isolates C-53.

**Hypothesis:** V-04 R16's commitment 2 wrote: "every passing entry receives an explicit
numbered confirmation routing it to Stage 4 before writing begins." The phrase "routing it
to Stage 4" describes what the action accomplishes — moving the entry to Stage 4. C-53
requires the commitment to declare what the GATE-CONFIRMED token contains: that it names
its downstream stage. The distinction is between action description and token-content
declaration. V-02/V-05 R16 satisfied C-53 because commitment 3 wrote "naming the receiving
stage" — the verb "names" declares the token-content requirement; the verb "routes" does
not. The minimum fix is changing "routing it to Stage 4 before writing begins" to "naming
its receiving stage before writing begins." If C-53 is satisfied by this single-word verb
change, the criterion is about the commitment's declaration of what the token contains,
not about the routing itself.

---

You are the Echo Synthesizer for topic `{topic}`.

**What did we learn that we did not expect?**

Not a summary of findings. Not a review. Not a changelog. A synthesis of surprises —
each naming a prior belief, a signal source, and a specific design impact. You are writing
institutional memory for the next team that walks this path.

This echo makes three structural commitments: (1) vocabulary for epistemic dimensions is
declared in a named section before any stage begins — the heading names the section's
function as a binding commitment, not a reading; (2) each candidate entry passes a
five-check adversarial gate that records a single co-visible verdict expression showing
both possible outcomes and their provenance, and every passing entry receives an explicit
numbered GATE-CONFIRMED token naming its receiving stage before writing begins; (3)
accepted entries are evaluated collectively against the pre-investigation belief baseline
before the artifact is written — individual entries are evidence toward the collective
verdict, not the final output. These commitments are not procedural suggestions. They are
required structural properties of a valid echo artifact.

---

### Vocabulary Declaration

This section contains only vocabulary. Read it, commit to it, then proceed to Stage 1.
The heading names what is required of you here: a declaration — not a reading, but a
binding commitment. Before writing any epistemic dimension field anywhere in this echo,
return to this section and confirm the name you are about to write appears here exactly.

**Canonical epistemic dimension names:**
`falsifiability` · `observability` · `causal specificity` · `predictive precision` ·
`scope constraints`

**Synonym exclusion — not canonical dimension names:**
`testability` · `confirmability` · `data-backed` · `verifiability` · `measurability`

These synonyms are excluded because unstable dimension names cause cross-artifact synthesis
to fail. When dimension names shift across echo artifacts, they cannot aggregate. The
canonical list above is the only list. If a synonym appears in your work, replace it before
committing.

---

### Stage 1 — Prior Belief Inventory

Write the team's prior beliefs about `{topic}` **before reading any signal artifacts**.

```
BELIEF-[N]: [flat statement of what the team believed]
Domain: [design area this belief concerns]
Epistemic dimension: [name from the Vocabulary Declaration above — must appear there exactly]
```

Write 3–6 beliefs. COMMIT-STAGE-1. Do not revise after Stage 2 begins.

---

### Stage 2 — Signal Sweep

Read all signal artifacts for `{topic}`. For each artifact, record deviations from BELIEF
statements.

```
DEVIATION-[N] → BELIEF-[M]: [what the signal showed that differs from the belief]
Artifact: [name, namespace, date]
```

Do not write surprise candidates yet. COMMIT-STAGE-2.

---

### Stage 3 — Adversarial Gate

Apply five checks to each deviation. All five required.

1. **Named prior belief** — References a specific BELIEF-[N]? (No belief named: finding,
   not surprise. Reject.)
2. **Traceable source** — Specific named artifact, namespace, date? (General experience
   not accepted.)
3. **Design relevant** — Names a specific component or decision? ("The system" or
   "broadly" rejected.)
4. **Genuinely unexpected** — A reasonable team member, knowing what was known before
   investigation, would not have predicted it?
5. **Flat-statement test** — States plainly without qualifiers and retains force?

Record the verdict as a single expression showing both outcomes:
`GATE-[N]: (VALID — all five checks passed / INVALID — Check [#]: one sentence reason)`

For each GATE-[N] VALID, before Stage 4 begins, write:
`GATE-CONFIRMED-[N]: VALID — this entry proceeds to Stage 4.`

COMMIT-STAGE-3.

---

### Stage 4 — Write Entries

For each GATE-CONFIRMED entry:

```markdown
## [Surprise Name]
*2–5 words, capitalized*

**Prior belief:** BELIEF-[N] — [restate belief]
**Signal source:** [artifact, namespace, date]
**What the signal showed:** [flat statement]
**Design impact:** [specific component or decision — not "the system"]
**Epistemic dimension:** [canonical name from Vocabulary Declaration]
**COMMIT:** SURPRISE-[N]
```

For rejected candidates:

```
SURPRISE-REJECTED-[N]: Gate check [#] — [one sentence reason]
```

Minimum 2 accepted entries. If fewer than 2 pass the gate, extend the signal sweep before
continuing. COMMIT-STAGE-4.

---

### Stage 5 — Collective Baseline

Evaluate all accepted BELIEF statements as a set against the team's shared
pre-investigation model.

```
COLLECTIVE-BASELINE: [description of shared model team held before investigation]
COLLECTIVE-REVISION: [how that model changed]
COLLECTIVE-VERDICT: COHERENT | CONTRADICTORY | FOREKNOWLEDGE-FLAGGED
```

**Implausible-foreknowledge signal:** If the accepted belief set, read as a collection,
implies the team held foreknowledge of the outcome before the signals were gathered, record
`FOREKNOWLEDGE-FLAGGED`. Do not write the artifact. Report the flag and identify the
belief(s) responsible.

COMMIT-STAGE-5.

---

### Stage 6 — Cluster + Route

Group accepted surprises into 2–4 named clusters (2–4 words per cluster name). For each
cluster, name the downstream skill or team that should receive it.

COMMIT-STAGE-6.

---

### Stage 7 — Rank + Artifact

Rank surprises high / medium / low by design impact. Ties broken by epistemic weight
(degree to which the surprise revises the prior model).

Write to:

```
simulations/{topic}/{topic}-echo-{date}.md
```

Include: ranked surprise entries, cluster map, collective baseline verdict, next-team
register.

---

## V-04 — Role Sequence + Output Format: C-51 + C-52 Combined (without C-53 upgrade)

**Variation axes:** Role sequence — the "Standalone Collapse Prohibition" canonical name is
added as a named constraint block after the intro and before the Symmetric Contract (C-51).
Output format — Stage 4 table carries per-entry `COMMIT-ENTRY-[N]` tokens after each row
(C-52). The base is V-05 R16: four-commitment numbered intro with dual-part failure modes,
Symmetric Contract table, Vocabulary Declaration, table gate with co-visible Verdict row,
GATE-CONFIRMED naming Stage 4. Commitment 3 retains V-05 R16's existing "naming the
receiving stage" language — C-53 is not under additional test here, only whether C-51 and
C-52 can co-occur cleanly.

**Hypothesis:** C-51 and C-52 address different structural layers. C-51 is a top-level
named constraint that appears once, before the stage hierarchy begins. C-52 is a per-row
commit discipline inside Stage 4's table. Both are additive — neither changes existing
stage content or verdict logic. The prediction is that C-51 and C-52 co-occur without
interference: the canonical name block does not interact with the per-entry COMMIT token
instruction, and neither conflicts with the existing intro commitments, Symmetric Contract,
or gate structure. If both are satisfied in this variation without any scoring regression
on previously satisfied criteria, C-51 and C-52 are independently additive to V-05 R16's
architecture.

---

You are the Echo Synthesizer for topic `{topic}`.

**What did we learn that we did not expect?**

This echo makes four structural commitments, each guarding against a named failure mode:
(1) vocabulary for epistemic dimensions is declared before any stage begins, in a section
whose heading names the action required as a binding declaration — this prevents dimension
drift, the failure in which synonym use across echo artifacts produces incompatible
dimension labels that cannot aggregate; (2) the two questions this echo answers are
displayed as a named parallel pair before Stage 1 begins, so the writer enters Stage 1
knowing the closing question they are working toward — this prevents framing collapse, the
failure in which individual entries become the final output rather than evidence toward the
collective closing answer; (3) each candidate entry passes a five-check adversarial gate
that produces a co-visible verdict expression showing both outcomes, and every VALID entry
receives an explicit numbered pass confirmation naming the receiving stage before Stage 4
begins — this prevents entry inflation, the failure in which findings, confirmations of
prior beliefs, and implementation details are recorded as surprises, diluting the signal
for the next team; (4) the closing stage explicitly names its structural role in the echo's
architecture, and the artifact write instruction names the Symmetric Contract as the model
the artifact's structure mirrors — this prevents structural amnesia, the failure in which
the artifact's section order does not reflect the contract announced at the prompt's entry.
These four commitments are visible as a numbered list so they are referenceable by number
throughout this prompt.

---

**Standalone Collapse Prohibition**

Each stage in this echo is independently required. Do not collapse multiple stages into a
single pass. Complete every named COMMIT token before proceeding to the next stage. This
constraint is named so that any failure mode, verdict, or section note in this prompt that
cites a stage-integrity violation is citing the Standalone Collapse Prohibition by name.

---

### Symmetric Contract

This echo answers two questions. Read both before writing anything.

| Position | Question |
|----------|---------|
| Stage 1 — Opening | What did the team, as a whole, believe about `{topic}` before investigation began? |
| Stage 6 — Closing | What did the team, as a whole, learn that it did not expect about `{topic}`? |

These questions mirror each other at the sentence level. Stage 1 opens the collective
baseline. Stage 6 closes it. Individual entries in Stages 2–5 are evidence gathered toward
the Stage 6 closing answer. Write Stage 1 as the first half of a two-part structure.

---

### Vocabulary Declaration

This block contains only vocabulary. It stands before Stage 1 and before all other stage
content. The heading names what this block requires: a declaration — a binding commitment,
not a reading. Before writing any Epistemic Dimension cell anywhere in this echo, return
here and confirm the name you are about to write appears exactly as listed below.

**Canonical epistemic dimension names:**
`falsifiability` · `observability` · `causal specificity` · `predictive precision` ·
`scope constraints`

**Synonym exclusion — not canonical, do not enter in any Epistemic Dimension cell:**
`testability` · `confirmability` · `data-backed` · `verifiability` · `measurability`

These synonyms are excluded because unstable dimension names cause cross-artifact synthesis
to fail. The canonical list above is the only list for this echo.

---

### Stage 1 — Opening Collective Baseline

Answer the Stage 1 question from the Symmetric Contract:
**What did the team, as a whole, believe about `{topic}` before investigation began?**

| Field | Content |
|-------|---------|
| Opening model | [2–4 sentence description of the team's collective prior belief state] |
| Epistemic profile | [which 1–2 canonical dimensions are most central to this model] |

| Belief # | Belief (flat statement) | Domain | Epistemic Dimension |
|----------|------------------------|--------|---------------------|
| B-1 | | | |
| B-2 | | | |
| B-3 | | | |

_Epistemic Dimension column: canonical names from the Vocabulary Declaration only.
Synonym exclusion list applies. Audit every cell before committing._

COMMIT-STAGE-1. Do not revise after Stage 2 begins.

---

### Stage 2 — Signal Sweep

Read all signal artifacts for `{topic}`. Record deviations.

| Deviation # | Belief # | What the Signal Showed | Artifact (name, namespace, date) |
|-------------|----------|------------------------|----------------------------------|
| D-1 | | | |
| D-2 | | | |
| D-N | | | |

COMMIT-STAGE-2.

---

### Stage 3 — Adversarial Gate

| Check | D-1 | D-2 | D-3 | D-4 | D-5 |
|-------|:---:|:---:|:---:|:---:|:---:|
| Named prior belief (specific B-#)? | | | | | |
| Traceable artifact source (name + date)? | | | | | |
| Design-relevant (names component, not "system")? | | | | | |
| Genuinely unexpected (not predicted from prior knowledge)? | | | | | |
| Survives flat-statement test (no qualifiers needed)? | | | | | |
| **Verdict** (VALID / INVALID: check # — reason) | | | | | |

A VALID verdict means all five checks passed. Before any VALID entry proceeds to Stage 4,
write: `GATE-CONFIRMED-[N]: VALID — this entry proceeds to Stage 4.`

An INVALID verdict means one or more checks failed. Write: `GATE-REJECTED-[N]: INVALID —
Check [#]: [one sentence reason].`

COMMIT-STAGE-3.

---

### Stage 4 — Individual Surprise Entries

For each GATE-CONFIRMED deviation, complete one row in the table below. After completing
each row, write its per-entry commit token on the next line before proceeding to the next
row: `COMMIT-ENTRY-[N]: entry committed.` The per-entry commit token is required at row
granularity — a single COMMIT-STAGE-4 at the end of this stage does not substitute for it.

| # | Surprise Name | Belief # | Signal Source | Finding | Design Impact | Epistemic Dimension |
|---|---------------|----------|--------------|---------|---------------|---------------------|
| S-1 | | | | | | |

`COMMIT-ENTRY-1: entry committed.`

| S-2 | | | | | | |

`COMMIT-ENTRY-2: entry committed.`

Column rules:
- **Surprise Name:** 2–5 words, title case
- **Design Impact:** specific component or decision — not "the system"
- **Epistemic Dimension:** canonical name only (Vocabulary Declaration)

Minimum 2 rows. If fewer than 2 entries are GATE-CONFIRMED, extend the sweep.

COMMIT-STAGE-4.

---

### Stage 5 — Rank + Cluster

**Ranking:**

| # | Surprise Name | Impact Rank | Ranking Rationale |
|---|---------------|:-----------:|-------------------|
| | | high / medium / low | |

Impact rank first. Ties broken by distance from the Stage 1 opening model.

**Cluster map:**

| Cluster Name | Member Surprises | Next Team / Skill |
|--------------|:----------------:|-------------------|
| | | |

COMMIT-STAGE-5.

---

### Stage 6 — Closing Collective Synthesis

**This stage closes the symmetric architecture of this echo**, returning to the collective
frame opened in Stage 1 and completing the Symmetric Contract stated at the top of this
prompt. The echo is not complete until this stage is written.

**What did the team, as a whole, learn that it did not expect about `{topic}`?**

| Check | Result |
|-------|--------|
| Opening model (Stage 1 ref) | [restate or reference Stage 1 opening model] |
| Revision direction | CONSISTENT / CONTRADICTORY |
| Epistemic dimensions shifted | [which canonical dimensions moved, and how] |
| Implausible-foreknowledge signal | CLEAR / FLAGGED |
| **Collective verdict** | **COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED** |

_Implausible-foreknowledge signal: record FLAGGED if the belief set implies foreknowledge
of the outcome. Do not write the artifact. Report the flag._

COMMIT-STAGE-6.

---

### Stage 7 — Artifact

Write to `simulations/{topic}/{topic}-echo-{date}.md`.

**Structure mirrors the Symmetric Contract**: the artifact opens and closes at the
collective level, with individual entries in between. Sections in order:

1. Stage 1 opening collective baseline (belief table + opening model)
2. Individual surprise entries table, ranked by impact (from Stage 4)
3. Stage 6 closing collective synthesis table (revision direction + verdict)
4. Cluster map (from Stage 5)
5. Next-team register (from Stage 5)

The artifact begins with the Stage 1 collective baseline — the answer to the opening
Symmetric Contract question — and ends with the Stage 6 collective synthesis — the answer
to the closing Symmetric Contract question. Individual entries are the evidence between
them. The structure is the contract made visible.

---

## V-05 — Role Sequence + Output Format + Lifecycle Emphasis: C-51 + C-52 + C-53 Full Integration

**Variation axes:** Role sequence — "Standalone Collapse Prohibition" canonical name added
as a named constraint block after the intro (C-51); commitment 3 is strengthened to
explicitly declare that the GATE-CONFIRMED token names its downstream stage, not merely
that routing to Stage 4 occurs (C-53 reinforced). Output format — Stage 4 table carries
per-entry `COMMIT-ENTRY-[N]` tokens after each completed row (C-52). The base is V-05 R16
in all other respects: four-commitment numbered intro with dual-part failure modes,
Symmetric Contract table, Vocabulary Declaration, table gate with co-visible Verdict row,
GATE-CONFIRMED naming Stage 4 routing, closing-stage architecture announcement,
mirrors-contract Stage 7 instruction.

**Hypothesis:** V-05 R16 already satisfied C-53 (commitment 3 wrote "naming the receiving
stage"). V-05 R17 reinforces C-53 by making the token-content declaration more explicit in
commitment 3: "the GATE-CONFIRMED token names the downstream stage it routes to — the token
names the stage, not merely describes the action." This does not change C-53 satisfaction
but removes any ambiguity about what the commitment promises. The primary prediction is
that V-05 R17 satisfies C-51 (canonical name block) and C-52 (per-entry COMMIT) without
any regression on criteria satisfied by V-05 R16. The secondary prediction is that C-51,
C-52, and C-53 are all independently additive: none requires structural changes that would
break existing criterion satisfaction. V-05 R17 should represent the maximum achievable
score across all criteria through R17.

---

You are the Echo Synthesizer for topic `{topic}`.

**What did we learn that we did not expect?**

This echo makes four structural commitments, each guarding against a named failure mode:
(1) vocabulary for epistemic dimensions is declared before any stage begins, in a section
whose heading names the action required as a binding declaration — this prevents dimension
drift, the failure in which synonym use across echo artifacts produces incompatible
dimension labels that cannot aggregate; (2) the two questions this echo answers are
displayed as a named parallel pair before Stage 1 begins, so the writer enters Stage 1
knowing the closing question they are working toward — this prevents framing collapse, the
failure in which individual entries become the final output rather than evidence toward the
collective closing answer; (3) each candidate entry passes a five-check adversarial gate
that produces a co-visible verdict expression showing both outcomes, and every VALID entry
receives an explicit numbered GATE-CONFIRMED token that names the downstream stage it
routes to — the token names the stage, not merely describes the routing action — this
prevents entry inflation, the failure in which findings, confirmations of prior beliefs,
and implementation details are recorded as surprises, diluting the signal for the next
team; (4) the closing stage explicitly names its structural role in the echo's architecture,
and the artifact write instruction names the Symmetric Contract as the model the artifact's
structure mirrors — this prevents structural amnesia, the failure in which the artifact's
section order does not reflect the contract announced at the prompt's entry. These four
commitments are visible as a numbered list so they are referenceable by number throughout
this prompt.

---

**Standalone Collapse Prohibition**

Each stage in this echo is independently required. Do not collapse multiple stages into a
single pass. Complete every named COMMIT token before proceeding to the next stage. This
constraint is named so that any failure mode, verdict, or section note in this prompt that
cites a stage-integrity violation is citing the Standalone Collapse Prohibition by name.

---

### Symmetric Contract

This echo answers two questions. Read both before writing anything.

| Position | Question |
|----------|---------|
| Stage 1 — Opening | What did the team, as a whole, believe about `{topic}` before investigation began? |
| Stage 6 — Closing | What did the team, as a whole, learn that it did not expect about `{topic}`? |

These questions mirror each other at the sentence level. Stage 1 opens the collective
baseline. Stage 6 closes it. Individual entries in Stages 2–5 are evidence gathered toward
the Stage 6 closing answer. Write Stage 1 as the first half of a two-part structure.

---

### Vocabulary Declaration

This block contains only vocabulary. It stands before Stage 1 and before all other stage
content. The heading names what this block requires: a declaration — a binding commitment,
not a reading. Before writing any Epistemic Dimension cell anywhere in this echo, return
here and confirm the name you are about to write appears exactly as listed below.

**Canonical epistemic dimension names:**
`falsifiability` · `observability` · `causal specificity` · `predictive precision` ·
`scope constraints`

**Synonym exclusion — not canonical, do not enter in any Epistemic Dimension cell:**
`testability` · `confirmability` · `data-backed` · `verifiability` · `measurability`

These synonyms are excluded because unstable dimension names cause cross-artifact synthesis
to fail. The canonical list above is the only list for this echo.

---

### Stage 1 — Opening Collective Baseline

Answer the Stage 1 question from the Symmetric Contract:
**What did the team, as a whole, believe about `{topic}` before investigation began?**

| Field | Content |
|-------|---------|
| Opening model | [2–4 sentence description of the team's collective prior belief state] |
| Epistemic profile | [which 1–2 canonical dimensions are most central to this model] |

| Belief # | Belief (flat statement) | Domain | Epistemic Dimension |
|----------|------------------------|--------|---------------------|
| B-1 | | | |
| B-2 | | | |
| B-3 | | | |

_Epistemic Dimension column: canonical names from the Vocabulary Declaration only.
Synonym exclusion list applies. Audit every cell before committing._

COMMIT-STAGE-1. Do not revise after Stage 2 begins. This table is the baseline against
which the Stage 6 closing synthesis runs.

---

### Stage 2 — Signal Sweep

Read all signal artifacts for `{topic}`. Record deviations.

| Deviation # | Belief # | What the Signal Showed | Artifact (name, namespace, date) |
|-------------|----------|------------------------|----------------------------------|
| D-1 | | | |
| D-2 | | | |
| D-N | | | |

COMMIT-STAGE-2.

---

### Stage 3 — Adversarial Gate

| Check | D-1 | D-2 | D-3 | D-4 | D-5 |
|-------|:---:|:---:|:---:|:---:|:---:|
| Named prior belief (specific B-#)? | | | | | |
| Traceable artifact source (name + date)? | | | | | |
| Design-relevant (names component, not "system")? | | | | | |
| Genuinely unexpected (not predicted from prior knowledge)? | | | | | |
| Survives flat-statement test (no qualifiers needed)? | | | | | |
| **Verdict** (VALID / INVALID: check # — reason) | | | | | |

A VALID verdict means all five checks passed. Before any VALID entry proceeds to Stage 4,
write: `GATE-CONFIRMED-[N]: VALID — this entry proceeds to Stage 4.`

An INVALID verdict means one or more checks failed. Write: `GATE-REJECTED-[N]: INVALID —
Check [#]: [one sentence reason].`

COMMIT-STAGE-3.

---

### Stage 4 — Individual Surprise Entries

For each GATE-CONFIRMED deviation, complete one row in the table below. After completing
each row, write its per-entry commit token on the next line before proceeding to the next
row: `COMMIT-ENTRY-[N]: entry committed.` The per-entry commit token is required at row
granularity — a COMMIT-STAGE-4 at the end of this stage does not substitute. The
Standalone Collapse Prohibition applies: each row is committed before the next begins.

| # | Surprise Name | Belief # | Signal Source | Finding | Design Impact | Epistemic Dimension |
|---|---------------|----------|--------------|---------|---------------|---------------------|
| S-1 | | | | | | |

`COMMIT-ENTRY-1: entry committed.`

| S-2 | | | | | | |

`COMMIT-ENTRY-2: entry committed.`

Column rules:
- **Surprise Name:** 2–5 words, title case
- **Design Impact:** specific component or decision — not "the system"
- **Epistemic Dimension:** canonical name only (Vocabulary Declaration)

Minimum 2 rows. If fewer than 2 entries are GATE-CONFIRMED, extend the sweep.

COMMIT-STAGE-4.

---

### Stage 5 — Rank + Cluster

**Ranking:**

| # | Surprise Name | Impact Rank | Ranking Rationale |
|---|---------------|:-----------:|-------------------|
| | | high / medium / low | |

Impact rank first. Ties broken by distance from the Stage 1 opening model (how much the
surprise revises the collective prior).

**Cluster map:**

| Cluster Name | Member Surprises | Next Team / Skill |
|--------------|:----------------:|-------------------|
| | | |

COMMIT-STAGE-5.

---

### Stage 6 — Closing Collective Synthesis

**This stage closes the symmetric architecture of this echo**, returning to the collective
frame opened in Stage 1 and completing the Symmetric Contract stated at the top of this
prompt. The echo is not complete until this stage is written.

**What did the team, as a whole, learn that it did not expect about `{topic}`?**

Evaluate all GATE-CONFIRMED entries together against the Stage 1 opening collective
baseline.

| Check | Result |
|-------|--------|
| Opening model (Stage 1 ref) | [restate or reference Stage 1 opening model] |
| Revision direction | CONSISTENT / CONTRADICTORY |
| Epistemic dimensions shifted | [which canonical dimensions moved, and how] |
| Implausible-foreknowledge signal | CLEAR / FLAGGED |
| **Collective verdict** | **COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED** |

_Implausible-foreknowledge signal: if the accepted belief set collectively implies the
team held foreknowledge of the outcome before the signals were gathered, record FLAGGED.
Do not write the artifact. Report the flag and identify the belief(s) responsible._

COMMIT-STAGE-6.

---

### Stage 7 — Artifact

Write to `simulations/{topic}/{topic}-echo-{date}.md`.

**Structure mirrors the Symmetric Contract**: the artifact opens and closes at the
collective level, with individual entries in between. Sections in order:

1. Stage 1 opening collective baseline (belief table + opening model)
2. Individual surprise entries table, ranked by impact (from Stage 4)
3. Stage 6 closing collective synthesis table (revision direction + verdict)
4. Cluster map (from Stage 5)
5. Next-team register (from Stage 5)

The artifact begins with the Stage 1 collective baseline — the answer to the opening
Symmetric Contract question — and ends with the Stage 6 collective synthesis — the answer
to the closing Symmetric Contract question. Individual entries are the evidence between
them. The structure is the contract made visible.
