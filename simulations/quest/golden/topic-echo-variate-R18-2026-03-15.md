---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-15
round: 18
rubric: v18
rubric_max: 200
---

# Variations: `topic:echo` — Round 18

**Rubric:** v18 | **Date:** 2026-03-15

---

## Design Context

R17 differentiating evidence: Three behaviors beyond existing criteria emerged across
four variations, all at the layer of canonical name propagation, token-content precision,
and cross-section citation scope.

V-01 and V-04 R17 defined "Standalone Collapse Prohibition" in the named block (C-51),
but did not cite the name inside the Stage 4 COMMIT instruction. V-05 R17 added:
"The Standalone Collapse Prohibition applies: each row is committed before the next
begins." — placing the canonical name at an enforcement site beyond the definition block.
C-51 requires the name to exist; C-54 requires it to appear wherever the model is
instructed to act on the constraint. The enforcement site is the Stage 4 inline structural
instruction, not just the definition block.

V-01 and V-04 R17 intro commitment 3 wrote "naming the receiving stage before Stage 4
begins" — satisfying C-53. V-05 R17 went further: "the GATE-CONFIRMED token names the
downstream stage it routes to — the token names the stage, not merely describes the
routing action." C-55 requires the commitment to explicitly distinguish token-content
specification (what the token must lexically carry) from behavioral description (what the
routing action does). "Naming the receiving stage" satisfies C-53; only the explicit
contrast "names the stage, not merely describes the routing action" satisfies C-55.

All V-01/V-04/V-05 R17 included a Standalone Collapse Prohibition definition block.
V-01 R17 wrote: "This constraint is named so that any failure mode, verdict, or section
note in this prompt that cites a stage-integrity violation is citing the Standalone
Collapse Prohibition by name." This scoped mandate names the categories of downstream
sections (failure modes, verdicts, section notes) that must cite by canonical name. A
definition block that says only "this constraint is named so it can be cited by name
throughout this prompt" is unscoped and does not satisfy C-56. The scope must name the
categories of downstream sections explicitly.

Key test results from R17:
- **C-54**: Satisfied by V-05 R17 (enforcement site citation in Stage 4 instruction).
  Not satisfied by V-01/V-04 R17 (canonical name confined to definition block only).
- **C-55**: Satisfied by V-05 R17 ("names the stage, not merely describes the routing
  action"). Not satisfied by V-01/V-04 R17 ("naming the receiving stage" satisfies C-53
  but lacks the explicit token-content vs behavioral description contrast).
- **C-56**: Satisfied by V-01 and V-05 R17 (scoped mandate names failure modes, verdicts,
  section notes as the propagation scope). Not satisfied by variations using unscoped
  language ("cited by name throughout this prompt" without naming where).

Specific hypotheses under test:
- **C-54**: The minimum mechanism is a single sentence inside the Stage 4 inline
  instruction citing the canonical name at the per-entry commit enforcement site. If C-54
  is satisfied by this addition alone, the criterion is about enforcement-site citation
  granularity, not about how many enforcement sites the name appears in.
- **C-55**: The minimum mechanism is the explicit contrast clause "the token names the
  stage, not merely describes the routing action" inside the intro commitment that covers
  the GATE-CONFIRMED token. If C-55 is satisfied by this clause alone, the criterion is
  about the contrast being stated — not inferred from a token example.
- **C-56**: The minimum mechanism is a scoped mandate naming specific downstream section
  categories (failure modes, verdicts, section notes). If C-56 is satisfied by this
  scoping, the criterion is about named scope — a general mandate without named categories
  does not satisfy it.

Variation axes selected:
- Single-axis: role sequence (V-01, C-54 canonical name at enforcement site), output
  format (V-02, C-55 token-content precision), lifecycle emphasis (V-03, C-56 cross-section
  mandate)
- Combined: role sequence + output format (V-04, C-54 + C-55 without C-56), all three
  criteria + R19 candidate push (V-05, C-54 + C-55 + C-56 maximum coverage)

---

## V-01 — Role Sequence: Canonical Name at Enforcement Site (C-54 isolated)

**Variation axis:** Role sequence — the canonical name "Standalone Collapse Prohibition"
is added inside the Stage 4 inline structural instruction, at the per-entry commit
enforcement site. The base is V-05 R17: four-commitment numbered intro with dual-part
failure modes (C-43/C-47/C-50), Standalone Collapse Prohibition named block (C-51),
Symmetric Contract table (C-38/C-42), Vocabulary Declaration (C-37/C-40), table gate with
co-visible Verdict row (C-48), GATE-CONFIRMED naming Stage 4 as receiving stage
(C-49/C-53), per-entry COMMIT-ENTRY-[N] tokens in Stage 4 (C-52), closing-stage
architecture announcement (C-41), mirrors-contract Stage 7 instruction (C-44).

C-55 is absent: intro commitment 3 uses "naming its receiving stage before Stage 4
begins" (C-53 satisfied) without the explicit token-content vs routing-description
contrast. C-56 is absent: the Standalone Collapse Prohibition block uses unscoped
language — "so it can be cited by name throughout this prompt" — without naming the
categories of downstream sections.

**Hypothesis:** V-01/V-04 R17 placed the canonical name only in the definition block.
V-05 R17 also cited it inside the Stage 4 instruction: "The Standalone Collapse
Prohibition applies: each row is committed before the next begins." C-54 is satisfied
when the canonical name appears at an enforcement site beyond the definition block. The
minimum mechanism is this sentence inside Stage 4's inline instruction. If C-54 is
satisfied here without C-55 or C-56, the criterion is about enforcement-site citation,
not about the number of sites or the scope of the cross-section mandate.

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
receives an explicit numbered GATE-CONFIRMED token naming its receiving stage before Stage
4 begins — this prevents entry inflation, the failure in which findings, confirmations of
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
constraint is named so it can be cited by name throughout this prompt.

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

---

## V-02 — Output Format: Token-Content Precision in Intro Commitment (C-55 isolated)

**Variation axis:** Output format — intro commitment 3 is strengthened to explicitly
distinguish between naming the receiving stage (a token-content specification) and
describing the routing action (a behavioral statement). The base is V-05 R17 in all
other respects: four-commitment numbered intro with dual-part failure modes, Standalone
Collapse Prohibition named block (C-51), Symmetric Contract table, Vocabulary Declaration,
table gate with co-visible Verdict row (C-48), GATE-CONFIRMED naming Stage 4 routing
(C-49/C-53), per-entry COMMIT-ENTRY-[N] tokens (C-52), closing-stage architecture
announcement (C-41), mirrors-contract Stage 7 instruction (C-44).

C-54 is absent: Stage 4's inline structural instruction does not cite the Standalone
Collapse Prohibition by name. C-56 is absent: the Standalone Collapse Prohibition block
uses unscoped language — "so it can be cited by name throughout this prompt" — without
naming the categories of downstream sections.

**Hypothesis:** V-04 R17 commitment 3 wrote "naming the receiving stage before Stage 4
begins" — satisfying C-53. C-55 requires the commitment to further state that the token
names the stage (token-content specification), not merely that routing occurs (behavioral
description). The minimum mechanism is the clause "the token names the stage, not merely
describes the routing action" inside the intro commitment covering the GATE-CONFIRMED
token. If C-55 is satisfied by this clause alone, the criterion is about the explicit
contrast being stated in the intro — not about the Stage 4 enforcement instruction or the
definition block mandate.

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
constraint is named so it can be cited by name throughout this prompt.

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
granularity — a COMMIT-STAGE-4 at the end of this stage does not substitute.

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

---

## V-03 — Lifecycle Emphasis: Cross-Section Citation Mandate (C-56 isolated)

**Variation axis:** Lifecycle emphasis — the Standalone Collapse Prohibition definition
block is extended with an explicit scoped mandate naming the categories of downstream
sections (failure modes, verdicts, section notes) that must cite the constraint by its
canonical name. The base is V-05 R17 in all other respects: four-commitment numbered intro
with dual-part failure modes, Standalone Collapse Prohibition named block (C-51), Symmetric
Contract table, Vocabulary Declaration, table gate with co-visible Verdict row (C-48),
GATE-CONFIRMED with Stage 4 naming (C-49/C-53), per-entry COMMIT-ENTRY-[N] tokens (C-52),
closing-stage architecture announcement (C-41), mirrors-contract Stage 7 instruction (C-44).

C-54 is absent: Stage 4's inline structural instruction does not cite "Standalone Collapse
Prohibition" by name. C-55 is absent: intro commitment 3 uses "naming its receiving stage
before Stage 4 begins" (C-53 satisfied) without the explicit "names the stage, not merely
describes the routing action" contrast.

**Hypothesis:** V-04 R17's Standalone Collapse Prohibition block said "This constraint is
named so it can be cited by name throughout this prompt" — unscoped, no named categories.
V-05 R17 (and V-01 R17) wrote: "any failure mode, verdict, or section note in this prompt
that cites a stage-integrity violation is citing the Standalone Collapse Prohibition by
name." This is a scoped mandate: it names the categories of downstream prompt sections
that must use the canonical name. C-56 is satisfied by this scoping. If C-56 is satisfied
in isolation here without C-54 or C-55, the criterion is about the definition block's
mandate scope — it is not dependent on enforcement-site propagation or intro token-content
precision.

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
receives an explicit numbered GATE-CONFIRMED token naming its receiving stage before Stage
4 begins — this prevents entry inflation, the failure in which findings, confirmations of
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
references this prohibition is citing the Standalone Collapse Prohibition by name.

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
granularity — a COMMIT-STAGE-4 at the end of this stage does not substitute.

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

---

## V-04 — Role Sequence + Output Format: C-54 + C-55 Combined (C-56 absent)

**Variation axes:** Role sequence — "Standalone Collapse Prohibition" canonical name is
cited inside the Stage 4 inline structural instruction at the enforcement site (C-54).
Output format — intro commitment 3 explicitly distinguishes token-content naming from
routing description (C-55). The base is V-05 R17 in all other respects. C-56 is absent:
the Standalone Collapse Prohibition block uses unscoped language — "so it can be cited by
name throughout this prompt" — without naming the categories of downstream sections.

**Hypothesis:** C-54 and C-55 address different structural layers. C-54 is an enforcement-
site instruction within Stage 4; C-55 is a commitment-level declaration within the intro
meta-declaration. Both are additive to V-04 R17's architecture. The prediction is that
C-54 and C-55 co-occur without interference: the Stage 4 enforcement sentence does not
conflict with the intro commitment language, and neither requires C-56's definition-block
mandate to function. If both are satisfied without C-56, C-54 and C-55 are independently
additive from the cross-section citation mandate.

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
constraint is named so it can be cited by name throughout this prompt.

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

---

## V-05 — Full Integration: C-54 + C-55 + C-56 + R19 Candidate Push

**Variation axes:** Role sequence — "Standalone Collapse Prohibition" canonical name cited
at Stage 4 enforcement site (C-54). Output format — intro commitment 3 explicitly
distinguishes token-content naming from routing description (C-55). Lifecycle emphasis —
the definition block carries a scoped cross-section citation mandate (C-56). This is V-05
R17 exactly, with two structural extensions that may surface R19 criteria:

1. COMMIT-STAGE-4 token carries an explicit canonical constraint reference: "COMMIT-STAGE-4:
   all entries committed per the Standalone Collapse Prohibition." This extends C-54 from
   the inline instruction level to the stage-close token level — a potential R19 candidate
   for stage-level COMMIT token constraint citation.
2. The GATE-CONFIRMED token body contains the receiving stage name as a standalone proper
   noun, not embedded in a routing clause: `GATE-CONFIRMED-[N]: VALID — Stage 4.` This
   makes the stage name the token's content, not a phrase object inside "proceeds to [X]"
   — a potential R19 candidate for lexical stage-name precision in confirmation tokens.

**Hypothesis:** V-05 R17 already satisfies C-54, C-55, and C-56. The primary prediction
is no regression across all criteria satisfied by V-05 R17. The secondary prediction is
that extension 1 (COMMIT-STAGE-4 constraint citation) and extension 2 (GATE-CONFIRMED
proper-noun stage content) surface as distinct behaviors that earlier variations do not
exhibit — candidates for C-57 and C-58 respectively. If both behaviors appear in V-05 R18
without regression, the two candidates are observable and independently named.

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
references this prohibition is citing the Standalone Collapse Prohibition by name.

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
write the confirmation token with the receiving stage as its content — the token names
Stage 4, not merely routes toward it:

`GATE-CONFIRMED-[N]: VALID — Stage 4.`

An INVALID verdict means one or more checks failed. Write: `GATE-REJECTED-[N]: INVALID —
Check [#]: [one sentence reason].`

COMMIT-STAGE-3.

---

### Stage 4 — Individual Surprise Entries

For each GATE-CONFIRMED deviation, complete one row in the table below. After completing
each row, write its per-entry commit token on the next line before proceeding to the next
row: `COMMIT-ENTRY-[N]: entry committed.` The per-entry commit token is required at row
granularity — a stage-close token does not substitute. The Standalone Collapse Prohibition
applies: each row is committed before the next begins.

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

COMMIT-STAGE-4: all entries committed per the Standalone Collapse Prohibition.

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
