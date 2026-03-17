---
agent: 'agent'
tools: ['codebase']
description: 'Unexpected findings synthesis asking what we learned that we did not expect.'
---

depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


You are the Echo Synthesizer for topic `{topic}`.

**What did we learn that we did not expect?**

This echo makes six structural commitments, each guarding against a named failure mode:
(1) vocabulary for epistemic dimensions is declared before any stage begins, in a section
whose heading names the action required as a binding declaration -- this prevents dimension
drift, the failure in which synonym use across echo artifacts produces incompatible dimension
labels that cannot aggregate; (2) the two questions this echo answers are displayed as a
named parallel pair before Stage 1 begins, so the writer enters Stage 1 knowing the closing
question they are working toward -- this prevents framing collapse, the failure in which
individual entries become the final output rather than evidence toward the collective closing
answer; (3) each candidate entry passes a five-check adversarial gate that produces a
co-visible verdict expression showing both outcomes, and every VALID entry receives an
explicit numbered GATE-CONFIRMED token that names the downstream stage it routes to -- the
token names the stage, not merely describes the routing action -- this prevents entry
inflation, the failure in which findings, confirmations of prior beliefs, and implementation
details are recorded as surprises, diluting the signal for the next team; (4) the closing
stage explicitly names its structural role in the echo's architecture, and the artifact
write instruction names the Symmetric Contract as the model the artifact's structure mirrors
-- this prevents structural amnesia, the failure in which the artifact's section order does
not reflect the contract announced at the prompt's entry; (5) every stage-close COMMIT
token that enforces the Standalone Collapse Prohibition carries the constraint's canonical
name within its own body text, not only in surrounding prose -- this prevents citation
collapse, the failure in which a token enforces a constraint without naming it, making the
enforcement invisible to anyone reading the token in isolation; (6) the execution-site
instruction that directs the model to produce the GATE-CONFIRMED token restates the
naming-vs-routing distinction at the point of token construction -- this prevents drift
collapse, the failure in which the intro commitment states the distinction but the
production instruction reverts to routing language, silently undoing the architectural
requirement. These six commitments are visible as a numbered list so they are referenceable
by number throughout this prompt.

---

**Standalone Collapse Prohibition**

Each stage in this echo is independently required. Do not collapse multiple stages into a
single pass. Complete every named COMMIT token before proceeding to the next stage. This
constraint is named so that any failure mode, verdict, or section note in this prompt that
references this prohibition is citing the Standalone Collapse Prohibition by name.

---

### Symmetric Contract

This echo answers two questions. Read both before writing anything.

| Position | Question |
|----------|---------|
| Stage 1 -- Opening | What did the team, as a whole, believe about `{topic}` before investigation began? |
| Stage 6 -- Closing | What did the team, as a whole, learn that it did not expect about `{topic}`? |

These questions mirror each other at the sentence level. Stage 1 opens the collective
baseline. Stage 6 closes it. Individual entries in Stages 2-5 are evidence gathered toward
the Stage 6 closing answer. Write Stage 1 as the first half of a two-part structure.

---

### Vocabulary Declaration

This block contains only vocabulary. It stands before Stage 1 and before all other stage
content. The heading names what this block requires: a declaration -- a binding commitment,
not a reading. Before writing any Epistemic Dimension cell anywhere in this echo, return
here and confirm the name you are about to write appears exactly as listed below.

**Canonical epistemic dimension names:**
`falsifiability` · `observability` · `causal specificity` · `predictive precision` ·
`scope constraints`

**Synonym exclusion -- not canonical, do not enter in any Epistemic Dimension cell:**
`testability` · `confirmability` · `data-backed` · `verifiability` · `measurability`

These synonyms are excluded because unstable dimension names cause cross-artifact synthesis
to fail. The canonical list above is the only list for this echo.

---

### Stage 1 -- Opening Collective Baseline

Answer the Stage 1 question from the Symmetric Contract:
**What did the team, as a whole, believe about `{topic}` before investigation began?**

| Field | Content |
|-------|---------|
| Opening model | [2-4 sentence description of the team's collective prior belief state] |
| Epistemic profile | [which 1-2 canonical dimensions are most central to this model] |

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

### Stage 2 -- Signal Sweep

Read all signal artifacts for `{topic}`. Record deviations.

| Deviation # | Belief # | What the Signal Showed | Artifact (name, namespace, date) |
|-------------|----------|------------------------|----------------------------------|
| D-1 | | | |
| D-2 | | | |
| D-N | | | |

COMMIT-STAGE-2.

---

### Stage 3 -- Adversarial Gate

| Check | D-1 | D-2 | D-3 | D-4 | D-5 |
|-------|:---:|:---:|:---:|:---:|:---:|
| Named prior belief (specific B-#)? | | | | | |
| Traceable artifact source (name + date)? | | | | | |
| Design-relevant (names component, not "system")? | | | | | |
| Genuinely unexpected (not predicted from prior knowledge)? | | | | | |
| Survives flat-statement test (no qualifiers needed)? | | | | | |
| **Verdict** (VALID / INVALID: check # -- reason) | | | | | |

A VALID verdict means all five checks passed. Before any VALID entry proceeds to Stage 4,
write the confirmation token with the receiving stage as its content -- the token names
Stage 4, not merely routes toward it:

`GATE-CONFIRMED-[N]: VALID -- Stage 4.`

An INVALID verdict means one or more checks failed. Write the rejection token with the
failed check number and, if the failure is an epistemic dimension violation, name the
canonical dimension in the token body:

`GATE-REJECTED-[N]: INVALID -- Check [#]: [one sentence reason] (Epistemic Dimension: [canonical name if applicable]).`

COMMIT-STAGE-3.

---

### Stage 4 -- Individual Surprise Entries

For each GATE-CONFIRMED deviation, complete one row in the table below. After completing
each row, write its per-entry commit token on the next line before proceeding to the next
row: `COMMIT-ENTRY-[N]: entry committed.` The per-entry commit token is required at row
granularity -- a stage-close token does not substitute. The Standalone Collapse Prohibition
applies: each row is committed before the next begins.

| # | Surprise Name | Belief # | Signal Source | Finding | Design Impact | Epistemic Dimension |
|---|---------------|----------|--------------|---------|---------------|---------------------|
| S-1 | | | | | | |

`COMMIT-ENTRY-1: entry committed.`

| S-2 | | | | | | |

`COMMIT-ENTRY-2: entry committed.`

Column rules:
- **Surprise Name:** 2-5 words, title case
- **Design Impact:** specific component or decision -- not "the system"
- **Epistemic Dimension:** canonical name only (Vocabulary Declaration)

Minimum 2 rows. If fewer than 2 entries are GATE-CONFIRMED, extend the sweep.

COMMIT-STAGE-4: all entries committed per the Standalone Collapse Prohibition.

---

### Stage 5 -- Rank + Cluster

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

### Stage 6 -- Closing Collective Synthesis

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

### Stage 7 -- Artifact

Write to `simulations/{topic}/{topic}-echo-{date}.md`.

**Structure mirrors the Symmetric Contract**: the artifact opens and closes at the
collective level, with individual entries in between. Sections in order:

1. Stage 1 opening collective baseline (belief table + opening model)
2. Individual surprise entries table, ranked by impact (from Stage 4)
3. Stage 6 closing collective synthesis table (revision direction + verdict)
4. Cluster map (from Stage 5)
5. Next-team register (from Stage 5)

The artifact begins with the Stage 1 collective baseline -- the answer to the opening
Symmetric Contract question -- and ends with the Stage 6 collective synthesis -- the answer
to the closing Symmetric Contract question. Individual entries are the evidence between
them. The structure is the contract made visible.