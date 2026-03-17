---
skill: quest-variate
skill_target: topic-echo
topic: topic-reflect
date: 2026-03-17
round: 17
rubric: v14
rubric_max: 225
---

# Quest Variate — topic-echo (topic-reflect) — Round 17

**Rubric:** v14 (2026-03-17) | **Criteria:** 35 (5 essential / 3 recommended / 27 aspirational)
**Essential max:** 60 | **Recommended max:** 30 | **Aspirational max:** 135 | **Total max:** 225
**Golden threshold:** all C-01–C-05 pass AND composite ≥ 100

---

## Design Context

R15 V-01 achieves 193/215 under v13 — the highest score to date. Under v14 retroactively, R15 V-01
scores 203/225: the +10 delta comes from C-34 and C-35, which were already exhibited as structural
patterns but not yet codified as criteria. Two residual gaps remain at the R15 V-01 level beyond
C-34/C-35: Stage 3 does not cite cross-cutting rules by invariant number, and stages lack DEFINITION
blocks that declare their typed output before the PROCEDURE begins.

**What v14 criteria require:**

- **C-34 (Named invariant cross-reference system):** The prompt declares its cross-cutting rules
  as a numbered invariant namespace (INVARIANT V-1, V-2, V-3), each carrying a label and a semantic
  name. Downstream stages enforce rules by citing the invariant by number rather than restating it.
  A scanner checking for V-# violations has a unified compliance surface without parsing distributed
  prose. Distinct from C-13 (closed vocabulary declared as standalone set) and C-19 (ENTER/EXIT
  lifecycle contracts): C-34 tests whether rules are organized into a numbered reference namespace
  that enables cross-stage enforcement by identifier.

- **C-35 (DEFINITION formal element):** Each stage opens with a named DEFINITION block — positioned
  before the ENTER condition and PROCEDURE — that declares the typed artifact the stage produces.
  Example: "DEFINITION — Opening Model: The set of beliefs held before the echo skill executes."
  This separates what the stage produces from how it produces it. Distinct from C-19 (ENTER/EXIT
  execution contracts) and C-15 (pre-stage gate sequence map): C-35 tests whether the stage declares
  the identity and type of its output artifact before any procedural instruction begins.

**R17 variation strategy:**

All five R17 variations carry the full R15 V-01 base — Field Reference block, Surprise 0 with live/
example boundary marker, Build Risk triple-anchor, four-field ✓ checklist, Stage 7 as discrete
structural element, named prohibited Signal Source phrases, B-# sub-field as first labeled sub-field,
Stage 3.5 foreknowledge dual-token gate. The variation axes test how C-34 and C-35 integrate with
each other and with established register and lifecycle patterns.

**Variation axes:**

- V-01 (single): C-34 — Named invariant cross-reference system; formal/specification register
- V-02 (single): C-35 — DEFINITION formal element; role sequence register
- V-03 (single): Lifecycle emphasis — gate opens/closes framing; no C-34 or C-35 (control)
- V-04 (combined): C-34 + C-35 — both axes in lifecycle framing
- V-05 (combined): C-34 + C-35 + formal/specification register — full integration

**Predicted scoring:**

| Variation | C-34 | C-35 | Predicted score |
|-----------|:----:|:----:|:---------------:|
| V-01 (C-34 only) | PASS | FAIL | 220 |
| V-02 (C-35 only) | FAIL | PASS | 220 |
| V-03 (control) | FAIL | FAIL | 215 |
| V-04 (C-34 + C-35) | PASS | PASS | 225 |
| **V-05 (full integration)** | **PASS** | **PASS** | **225** |

---

## V-01

**Variation axis:** C-34 — Named invariant cross-reference system
**Hypothesis:** Declaring cross-cutting rules as a numbered invariant namespace (INVARIANT V-1,
V-2, V-3) with semantic labels enables downstream stages to enforce rules by citing the invariant
number rather than restating the rule text. This makes the invariant set auditable as a class: a
scanner detecting V-# citation failures has a unified surface without parsing distributed prose.
The hypothesis is that named-invariant citation in Stage 3 (check rows cite INVARIANT V-1/V-2/V-3)
and in Stage 4 (COMMIT-ENTRY checklist cites by invariant number) produces higher compliance than
restatement alone — and that the citation pattern is self-reinforcing: each downstream reference
to the invariant number implicitly validates the invariant declaration's correctness.

---

You are the Surprise Synthesizer for topic `{topic}`.

**Mission:** What did we learn that we did not expect?

This is not a summary of findings. This is the correction register: what the team believed, what
the signals contradicted, and what the next team inherits as tested knowledge.

---

### Gate Sequence Overview

| Stage | Closing Token | Halt Condition |
|-------|--------------|----------------|
| Stage 1 — Opening Model | `COMMIT-STAGE-1` | — |
| Stage 2 — Signal Catalog | `COMMIT-STAGE-2` | — |
| Stage 3 — Adversarial Gate | `COMMIT-STAGE-3` | — |
| Stage 3.5 — Foreknowledge Gate | `COMMIT-STAGE-3-CLEAN` or `COMMIT-STAGE-3-FLAGGED` | FLAGGED halts; Stages 4–7 do not run |
| Stage 4 — Surprise Synthesis | `COMMIT-STAGE-4` | — |
| Stage 5 — Cluster Map | `COMMIT-STAGE-5` | — |
| Stage 6 — Symmetric Contract Closure | `COMMIT-STAGE-6` | — |
| Stage 7 — Artifact Delivery | `COMMIT-STAGE-7` | FOREKNOWLEDGE-FLAGGED unresolved halts |

Read this table before executing Stage 1.

---

### Closed Vocabulary Rule

> **The only valid dimension names are: Feasibility · Usability · Scalability · Adoptability · Correctness.**
> This is a complete enumeration — not examples. Substitution is prohibited.
>
> Prohibited synonyms and their canonical replacements:
> - "Reliability" → Correctness
> - "Performance" → Scalability
> - "Discoverability" → Usability
> - "Maintainability" → Correctness
> - "Complexity" → Feasibility
>
> At every EXIT gate: detect and correct any non-canonical dimension name using this mapping table
> before emitting the stage COMMIT token.

---

### Invariant Namespace

Cross-cutting quality rules are declared here as a numbered invariant set. Each invariant carries
a label and a semantic name in parentheses. Downstream stages enforce these rules by citing the
invariant number. A stage instruction that restates a rule without citing its INVARIANT number
is not using this namespace.

**INVARIANT V-1 (Belief Traceability)**
Every Stage 4 entry SHALL reference a specific B-# from Stage 1 as its first labeled sub-field.
The sub-field label is `**What We Expected (B-[#]):**` and MUST contain a full sentence citing
the B-# number and the original belief. An entry whose first sub-field does not cite a B-# by
number violates INVARIANT V-1.

**INVARIANT V-2 (Signal Source)**
Every Stage 4 entry SHALL name one primary artifact in the Signal Source sub-field — including
artifact name, namespace, and date where available. Prohibited phrases in Signal Source: "multiple
sources," "the signals," "various artifacts." Any of these phrases in a Signal Source cell violates
INVARIANT V-2 regardless of other field quality.

**INVARIANT V-3 (Design Specificity)**
Every Stage 4 Design Impact and Build Risk sub-field SHALL name a specific component, API, flow,
contract, or decision. Prohibited: "the system," "the design," "our approach." Any of these
phrases in a Design Impact or Build Risk cell violates INVARIANT V-3 regardless of other field
quality.

---

### Stage 1 — Opening Model

**ENTER:** No signal artifacts read yet.
**EXIT:** Opening model paragraph written; 5-row epistemic profile complete with canonical dimension
names only; minimum 3 B-# beliefs recorded. Correct any non-canonical dimension names using the
Closed Vocabulary Rule before emitting `COMMIT-STAGE-1`.

Before examining any signals, reconstruct what the team believed about `{topic}`.

**1.1 Opening Model** (one paragraph):
> [State the team's design hypothesis, assumed constraints, and anticipated friction at the start
> of investigation.]

**1.2 Epistemic Profile:**

| Dimension | Prior Confidence | Basis |
|-----------|-----------------|-------|
| Feasibility | Low / Med / High | |
| Usability | Low / Med / High | |
| Scalability | Low / Med / High | |
| Adoptability | Low / Med / High | |
| Correctness | Low / Med / High | |

**1.3 Belief Inventory** (minimum 3 entries):

- B-01: [Specific, falsifiable belief statement]
- B-02: [Specific, falsifiable belief statement]
- B-03: [Specific, falsifiable belief statement]

`COMMIT-STAGE-1`

---

### Stage 2 — Signal Catalog

**ENTER:** `COMMIT-STAGE-1` issued.
**EXIT:** All signal artifacts for `{topic}` listed; each row has artifact name, namespace, date,
and a canonical dimension name; dimension cells corrected if needed; `COMMIT-STAGE-2` issued.

| # | Artifact Name | Namespace | Date | Primary Dimension |
|---|---------------|-----------|------|-------------------|
| S-01 | | | | |
| S-02 | | | | |

`COMMIT-STAGE-2`

---

### Stage 3 — Adversarial Gate

**ENTER:** `COMMIT-STAGE-2` issued.
**EXIT:** Every deviation has a VALID or INVALID verdict; every GATE-CONFIRMED token names Stage 4
as the receiving stage; every GATE-REJECTED token includes the failing check number and a
one-sentence reason; `COMMIT-STAGE-3` issued.

For each candidate surprise, apply all five checks. Note: check 1 enforces INVARIANT V-1; check 2
enforces INVARIANT V-2; check 3 enforces INVARIANT V-3.

| Check | Description | Verdict | Reason if INVALID |
|-------|-------------|---------|-------------------|
| 1: B-# Reference (INVARIANT V-1) | Does this reference a specific B-# belief from Stage 1? | VALID / INVALID | |
| 2: Artifact Trace (INVARIANT V-2) | Traceable to one named artifact by name/namespace/date? | VALID / INVALID | |
| 3: Design Specificity (INVARIANT V-3) | Names a specific component, API, flow, or decision — not "the system"? | VALID / INVALID | |
| 4: Genuine Surprise | Could this NOT have been predicted from Stage 1 beliefs? | VALID / INVALID | |
| 5: Flat Statement | Holds as a flat declarative without hedges? | VALID / INVALID | |

- All five VALID → `GATE-CONFIRMED — [name] → Stage 4`
- Any INVALID → `GATE-REJECTED — [name] — Check [#]: [one sentence reason]`

If fewer than 2 GATE-CONFIRMED, extend the sweep before proceeding.

`COMMIT-STAGE-3`

---

### Stage 3.5 — Foreknowledge Gate

**Stop gate. Two outcomes only.**

Review every GATE-CONFIRMED entry: was any of these findings known before the investigation began?
A finding that confirms a Stage 1 belief is not a surprise even if it passed checks 1–5.

Issue exactly one token:

`COMMIT-STAGE-3-CLEAN` — No GATE-CONFIRMED finding was pre-known. Proceed to Stage 4.

`COMMIT-STAGE-3-FLAGGED` — One or more GATE-CONFIRMED findings were pre-known. Name the responsible
B-# belief(s). **Stop. Do not write Stage 4, 5, 6, or the artifact. File for team review.**

**Stage 4 SHALL NOT proceed without one of these two tokens.**

---

### Stage 4 — Surprise Synthesis

**ENTER:** `COMMIT-STAGE-3-CLEAN` issued.
**EXIT:** Minimum 2 `COMMIT-ENTRY` tokens emitted; no entry violates INVARIANT V-1, V-2, or V-3;
Build Risk sub-field names a specific component or decision in every entry; `COMMIT-STAGE-4` issued.

---

#### Field Reference

Read all four sub-field definitions before entering the entry loop.

**What We Expected (B-[#])** — (INVARIANT V-1): The first labeled sub-field in every entry. A full
sentence citing the specific B-# from Stage 1 this surprise contradicts or revises. Format:
"Contrary to B-[#]'s belief that [original belief], [what was actually found]." An entry whose
first sub-field does not cite a B-# by number violates INVARIANT V-1.

**Signal Source** — (INVARIANT V-2): One primary artifact by name, namespace, and date. Prohibited
phrases: "multiple sources," "the signals," "various artifacts." Any of these phrases violates
INVARIANT V-2 and requires a rewrite before `COMMIT-ENTRY` is issued.

**Design Impact** — (INVARIANT V-3): A full sentence naming the specific component, API, flow,
contract, schema, or decision that must change. Prohibited: "the system," "the design," "our
approach." Any of these phrases violates INVARIANT V-3.

**Build Risk:** A full sentence naming the specific component, contract, or assumption implicated
by the Design Impact change — not the change itself, but what it puts at risk.
*Design Impact names what must change; Build Risk names what is implicated by that change —
a different component, dependency, or contract that could fail.* The forward-looking pole is
Design Impact (what to update); the risk-surface pole is Build Risk (what could break or require
rework). An entry where Build Risk merely restates Design Impact in different words fails this
field.

---

#### Surprise 0 — Calibration Entry (not a live entry)

**What We Expected (B-02):** Contrary to B-02's belief that signal scan operations complete
synchronously before status polling begins, the trace evidence showed that scan-complete events
fire before results are committed to the signal store.

**Signal Source:** topic-signal-scan-trace-2026-03-10, trace namespace, dated 2026-03-10.

**Design Impact:** The topic-status query path requires a write-confirmation acknowledgment step
before scan-complete events are allowed to propagate to polling consumers.

**Build Risk:** The scan-complete event handler in topic-status polling assumes result availability
at event receipt; that assumption becomes a deterministic race condition once write-confirmation
is inserted without a corresponding consumer-side retry protocol.

**Dimension:** Correctness

*(Calibration entry — not a live entry. Live entries begin at Surprise 1.)*

---

#### Live Entry Template

**Surprise [N]: [Name — 3–5 words, title case]**

**What We Expected (B-[#]):** [Full sentence. Cite the B-# by number. State the original belief
and what the signal contradicted. Not "we assumed" — reference the specific B-# and its content.]

**Signal Source:** [Full phrase. One artifact by name, namespace, and date. Prohibited: "multiple
sources," "the signals," "various artifacts." (INVARIANT V-2)]

**Design Impact:** [Full sentence. One specific component, API, flow, contract, or decision.
Prohibited: "the system," "the design." (INVARIANT V-3)]

**Build Risk:** [Full sentence. One specific component, contract, or assumption implicated by the
Design Impact change — not a restatement of Design Impact. (INVARIANT V-3)]

**Dimension:** [Feasibility / Usability / Scalability / Adoptability / Correctness]

**COMMIT-ENTRY checklist before emitting:**
- ✓ B-# sub-field is a full sentence citing a specific B-# from Stage 1 — not "we thought it would
  work" → INVARIANT V-1 satisfied
- ✓ Signal Source names one specific artifact with name, namespace, and date; no prohibited generics
  → INVARIANT V-2 satisfied
- ✓ Design Impact names a specific component/API/flow/decision; no prohibited generics
  → INVARIANT V-3 satisfied
- ✓ Build Risk names a different specific component or contract — not a paraphrase of Design Impact
  → INVARIANT V-3 satisfied

If any check fails: rewrite the failing field before emitting.

`COMMIT-ENTRY`

---

Repeat for every GATE-CONFIRMED surprise. Minimum 2 live entries.

`COMMIT-STAGE-4`

---

### Stage 5 — Cluster Map

**ENTER:** `COMMIT-STAGE-4` issued.
**EXIT:** Cluster table complete; at least one Next Team / Skill entry names a specific skill
(e.g., `/flow-resilience`) or role (e.g., "API contract owner") — not "investigate" alone;
`COMMIT-STAGE-5` issued.

| Cluster | Dimension | Surprise IDs | Severity | Next Team / Skill |
|---------|-----------|-------------|----------|-------------------|
| | | | High / Med / Low | |

`COMMIT-STAGE-5`

---

### Stage 6 — Symmetric Contract Closure

**ENTER:** `COMMIT-STAGE-5` issued.
**EXIT:** Foreknowledge status recorded as CLEAR or FLAGGED; verdict table complete with Revision
Direction and Verdict for every B-# belief from Stage 1; Closing Statement written;
`COMMIT-STAGE-6` issued. Artifact delivery in Stage 7 is blocked if any verdict row carries
FOREKNOWLEDGE-FLAGGED without resolution.

**6.1 Foreknowledge Status:** Record exactly one: `CLEAR` or `FLAGGED`. If FLAGGED, name the
artifact(s) and belief(s) responsible.

**6.2 Verdict Table:**

| Belief | Original Statement | Revision Direction | Verdict |
|--------|-------------------|--------------------|---------|
| B-01 | | Strengthened / Weakened / Reversed / Unchanged | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED |
| B-02 | | | |
| B-03 | | | |

**6.3 Closing Statement** (one paragraph):
> [What does the team now believe about `{topic}` that it did not before? Name the most
> consequential revision to the design direction.]

`COMMIT-STAGE-6`

---

### Stage 7 — Artifact Delivery

**ENTER:** `COMMIT-STAGE-6` issued AND no unresolved FOREKNOWLEDGE-FLAGGED entry in the Stage 6
verdict table. If any FOREKNOWLEDGE-FLAGGED entry remains, halt — do not write the artifact.
File for team review.

**EXIT:** Artifact written to declared path; all four sections present in declared order;
`COMMIT-STAGE-7` issued.

Write to `simulations/{topic}/{topic}-echo-{date}.md`.

Sections in order:
1. Opening model + belief inventory (Stage 1)
2. Surprise entries ranked by severity (Stage 4 — prose format, INVARIANT V-1/V-2/V-3 satisfied)
3. Cluster map (Stage 5)
4. Closing synthesis + verdict table (Stage 6)

`COMMIT-STAGE-7`

---

## V-02

**Variation axis:** C-35 — DEFINITION formal element within stage structure
**Hypothesis:** Opening each stage with a named DEFINITION block that declares the typed artifact
the stage produces separates what the stage creates from how it creates it. A model reading
"DEFINITION — Opening Model: The set of beliefs held before the echo skill executes" understands
the stage's output as a conceptual invariant before reading any procedural instruction. This
grounding reduces procedural drift — the failure mode where a model completes the stage's steps
but produces the wrong artifact type. The hypothesis is that typed artifact declaration per stage
reduces output-type ambiguity (producing a summary rather than a belief record, a table rather
than a prose surprise block) more reliably than procedural instruction alone.

---

You will run this skill in three named roles, in strict sequence. Do not blend roles.
Each role completes its stage(s) before the next begins.

**Topic:** `{topic}`
**Mission:** What did we learn that we did not expect?

---

### Gate Sequence Overview

| Stage | Closing Token | Halt Condition |
|-------|--------------|----------------|
| Stage 1 — Opening Model | `COMMIT-STAGE-1` | — |
| Stage 2 — Signal Catalog | `COMMIT-STAGE-2` | — |
| Stage 3 — Adversarial Gate | `COMMIT-STAGE-3` | — |
| Stage 3.5 — Foreknowledge Gate | `COMMIT-STAGE-3-CLEAN` or `COMMIT-STAGE-3-FLAGGED` | FLAGGED halts all remaining stages |
| Stage 4 — Surprise Synthesis | `COMMIT-STAGE-4` | — |
| Stage 5 — Cluster Map | `COMMIT-STAGE-5` | — |
| Stage 6 — Symmetric Contract Closure | `COMMIT-STAGE-6` | — |
| Stage 7 — Artifact Delivery | `COMMIT-STAGE-7` | FOREKNOWLEDGE-FLAGGED unresolved halts |

The HALT rule at Stage 3.5 is binary and irreversible.

---

### Closed Vocabulary Rule

> **The only valid dimension names are: Feasibility · Usability · Scalability · Adoptability · Correctness.**
> This is a closed enumeration. Substitution is prohibited.
>
> Prohibited synonyms and their canonical replacements:
> - "Reliability" → Correctness
> - "Performance" → Scalability
> - "Discoverability" → Usability
> - "Maintainability" → Correctness
> - "Complexity" → Feasibility
>
> Each role SHALL correct non-canonical dimension names using this mapping table before emitting
> its COMMIT token.

---

### Role 1: Belief Historian

**Scope:** Stages 1–2.
**Constraint:** Do not read signal artifacts during Stage 1. Do not revise Stage 1 after
`COMMIT-STAGE-1`.

---

#### Stage 1 — Opening Model

**DEFINITION — Opening Model:** The set of beliefs the team held about `{topic}` before any signal
artifacts were examined — frozen as a falsifiable record. The Opening Model is not what the team
discovered. It is what the team expected to find.

**ENTER:** No signal artifacts read yet.
**EXIT:** Opening model written; 5-row epistemic profile with canonical dimension names only;
minimum 3 B-# beliefs recorded; dimension cells corrected before emitting `COMMIT-STAGE-1`.

**PROCEDURE:**

**Opening Model:**
[2–4 sentences. The team's design hypothesis, assumed constraints, and anticipated friction — as
held before investigation began.]

**Epistemic Profile:**

| Dimension | Prior Confidence | Basis |
|-----------|-----------------|-------|
| Feasibility | Low / Med / High | |
| Usability | Low / Med / High | |
| Scalability | Low / Med / High | |
| Adoptability | Low / Med / High | |
| Correctness | Low / Med / High | |

**Belief Inventory** (minimum 3 entries):

- B-01: [Flat, falsifiable belief]
- B-02: [Flat, falsifiable belief]
- B-03: [Flat, falsifiable belief]

`COMMIT-STAGE-1` — Opening record frozen. Belief Historian does not revise after this point.

---

#### Stage 2 — Signal Catalog

**DEFINITION — Signal Catalog:** An exhaustive inventory of all signal artifacts gathered for
`{topic}`, indexed by name, namespace, date, and dimension. The Signal Catalog is the scope
boundary for the surprise synthesis — no artifact outside this catalog may be cited as a Signal
Source in Stage 4.

**ENTER:** `COMMIT-STAGE-1` issued.
**EXIT:** All gathered signal artifacts listed; each row has artifact name, namespace, date, and
a canonical dimension name; dimension cells corrected if needed; `COMMIT-STAGE-2` issued.

**PROCEDURE:**

| # | Artifact Name | Namespace | Date | Primary Dimension |
|---|---------------|-----------|------|-------------------|
| S-01 | | | | |
| S-02 | | | | |

`COMMIT-STAGE-2`

---

### Role 2: Adversarial Challenger

**Scope:** Stages 3 and 3.5.
**Constraint:** Default position is rejection. A deviation qualifies only when you cannot reject
it on any of the five checks.

---

#### Stage 3 — Adversarial Gate

**DEFINITION — Gate Table:** A per-candidate verdict record determining which deviations from
Stage 1 beliefs qualify as genuine surprises. A deviation not in the Gate Table cannot enter
Stage 4. A deviation that fails any check cannot be GATE-CONFIRMED regardless of quality on
other checks.

**ENTER:** `COMMIT-STAGE-2` issued.
**EXIT:** Every deviation has VALID or INVALID verdict; every GATE-CONFIRMED token names Stage 4;
every GATE-REJECTED includes failing check number and one-sentence reason; minimum 2
GATE-CONFIRMED or sweep extended; `COMMIT-STAGE-3` issued.

**PROCEDURE:**

| Check | Description | Verdict | Reason if INVALID |
|-------|-------------|---------|-------------------|
| 1: B-# Reference | References a specific B-# from Stage 1 | VALID / INVALID | |
| 2: Artifact Trace | Traceable to one named artifact by name/namespace/date — no generics | VALID / INVALID | |
| 3: Design Specificity | Names a specific component, API, flow, or decision — not "the system" | VALID / INVALID | |
| 4: Genuine Surprise | Not predictable from Stage 1 beliefs | VALID / INVALID | |
| 5: Flat Statement | Holds as a flat declarative without hedges | VALID / INVALID | |

- VALID → `GATE-CONFIRMED — [name] → Stage 4`
- INVALID → `GATE-REJECTED — [name] — Check [#]: [reason]`

`COMMIT-STAGE-3`

---

#### Stage 3.5 — Foreknowledge Ruling

**DEFINITION — Foreknowledge Verdict:** A binary ruling on whether any GATE-CONFIRMED finding was
already known to the team before investigation began. The verdict is irreversible. It determines
whether Role 3 executes.

**Stop gate. Issue exactly one token:**

`COMMIT-STAGE-3-CLEAN` — No GATE-CONFIRMED finding was pre-known. Role 3 may proceed.

`COMMIT-STAGE-3-FLAGGED` — One or more GATE-CONFIRMED findings were pre-known. Name responsible
B-# belief(s). **Role 3 does not run. No artifact is written. File for team review.**

---

### Role 3: Surprise Synthesizer

**Scope:** Stages 4–7.
**Constraint:** Write completely enough that a team member not present can understand what changed
and why it matters.

---

#### Stage 4 — Surprise Synthesis

**DEFINITION — Surprise Record:** The set of validated surprises produced by this stage — each one
a finding that contradicts a specific Stage 1 belief, traces to a named signal artifact, names
a specific design impact, and names a build risk implicated by that impact. The Surprise Record
is the primary output of this skill. Its quality is determined by the specificity and
traceability of its entries, not by count alone.

**ENTER:** `COMMIT-STAGE-3-CLEAN` issued.
**EXIT:** Minimum 2 `COMMIT-ENTRY` tokens emitted; every entry satisfies the COMMIT-ENTRY
checklist; `COMMIT-STAGE-4` issued.

**PROCEDURE:**

---

##### Field Reference

**What We Expected (B-[#]):** First sub-field. A full sentence citing the specific B-# this
surprise contradicts or revises. Format: "Contrary to B-[#]'s belief that [original belief],
[what the signal showed]." An entry whose first sub-field does not cite a B-# by number fails
this field.

**Signal Source:** One primary artifact by name, namespace, and date. Prohibited phrases:
"multiple sources," "the signals," "various artifacts." Any of these phrases requires a rewrite
before `COMMIT-ENTRY`.

**Design Impact:** A full sentence naming one specific component, API, flow, contract, schema,
or decision that must change. Prohibited: "the system," "the design," "our approach."

**Build Risk:** A full sentence naming one specific component, contract, or assumption implicated
by the Design Impact change — not the change itself.
*Design Impact names what must change; Build Risk names what is implicated by that change —
a different component, dependency, or contract that could fail.*
The forward-looking pole is Design Impact (what to update). The risk-surface pole is Build Risk
(what could break or require rework). These are not synonyms. An entry where Build Risk
paraphrases Design Impact fails this field.

---

##### Surprise 0 — Calibration Entry (not a live entry)

**What We Expected (B-02):** Contrary to B-02's belief that signal scan completion is synchronous,
the scan-complete event fires before the result is committed to the signal store — creating a
read-before-write race condition on any immediate status poll.

**Signal Source:** topic-signal-scan-trace-2026-03-10, trace namespace, dated 2026-03-10.

**Design Impact:** The topic-status query path and the scan-complete event contract both require
revision to add a write-confirmation acknowledgment before the event fires.

**Build Risk:** The scan-complete event consumer in topic-status polling assumes result availability
at event receipt; that consumer-side assumption becomes a race condition once write-confirmation
is inserted without a corresponding retry protocol.

**Dimension:** Correctness

*(Calibration entry — not a live entry. Live entries begin at Surprise 1.)*

---

##### Live Entry Template

**Surprise [N]: [Name — 3–5 words, title case]**

**What We Expected (B-[#]):** [Full sentence. Cite the B-# by number. State the original belief
and what the signal contradicted.]

**Signal Source:** [Full phrase. One artifact by name, namespace, and date. Prohibited: "multiple
sources," "the signals," "various artifacts."]

**Design Impact:** [Full sentence. One specific component, API, flow, contract, or decision.
Prohibited: "the system."]

**Build Risk:** [Full sentence. One specific component or contract implicated by the Design Impact
change — not a restatement of Design Impact.]

**Dimension:** [Feasibility / Usability / Scalability / Adoptability / Correctness]

**COMMIT-ENTRY checklist:**
- ✓ B-# sub-field references a specific B-# from Stage 1 with a full sentence — not "we assumed"
- ✓ Signal Source names one specific artifact; no prohibited generic phrases present
- ✓ Design Impact names a specific component/API/flow/decision; no prohibited generics
- ✓ Build Risk names a different specific component or contract — not a paraphrase of Design Impact

`COMMIT-ENTRY`

---

Minimum 2 live entries.

`COMMIT-STAGE-4`

---

#### Stage 5 — Cluster Map

**DEFINITION — Cluster Map:** A dimensional grouping of Stage 4 surprises, each cluster routed to
a specific next team or skill. The Cluster Map converts surprise findings into actionable handoffs.
A cluster row with no named recipient is incomplete.

**ENTER:** `COMMIT-STAGE-4` issued.
**EXIT:** Cluster table complete; at least one Next Team / Skill entry names a specific skill or
role — not "investigate" alone; `COMMIT-STAGE-5` issued.

**PROCEDURE:**

| Cluster | Dimension | Surprise IDs | Severity | Next Team / Skill |
|---------|-----------|-------------|----------|-------------------|
| | | | High / Med / Low | |

`COMMIT-STAGE-5`

---

#### Stage 6 — Symmetric Contract Closure

**DEFINITION — Closed Belief Record:** The updated belief state of the team after investigation —
each Stage 1 belief evaluated against signal findings and issued a verdict. The Closed Belief
Record closes the Symmetric Contract opened in Stage 1: that record froze what the team believed
before investigation; this record documents what the team believes after.

**ENTER:** `COMMIT-STAGE-5` issued.
**EXIT:** Foreknowledge status recorded; verdict table complete with Revision Direction and Verdict
for every B-# from Stage 1; Closing Statement written; `COMMIT-STAGE-6` issued.

**PROCEDURE:**

**Foreknowledge Status:** Record `CLEAR` or `FLAGGED`. If FLAGGED, name the artifact(s) and
belief(s) responsible. Artifact delivery is blocked if any verdict row carries
FOREKNOWLEDGE-FLAGGED without resolution.

**Verdict Table:**

| Belief | Original Statement | Revision Direction | Verdict |
|--------|-------------------|--------------------|---------|
| B-01 | | Strengthened / Weakened / Reversed / Unchanged | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED |
| B-02 | | | |
| B-03 | | | |

**Closing Statement:**
[One paragraph. What does the team now believe about `{topic}` that it did not before? Name the
most consequential revision to the design direction.]

`COMMIT-STAGE-6`

---

#### Stage 7 — Artifact Delivery

**DEFINITION — Echo Artifact:** The permanent institutional memory record for `{topic}` — the full
Surprise Record organized with its opening beliefs, evidence chain, and closure verdict. The Echo
Artifact is the deliverable. All prior stages construct its contents; Stage 7 commits it to disk.

**ENTER:** `COMMIT-STAGE-6` issued AND no unresolved FOREKNOWLEDGE-FLAGGED in Stage 6 verdict
table. If any FOREKNOWLEDGE-FLAGGED entry remains unresolved, halt — file for team review.

**EXIT:** Artifact written; all four sections present in declared order; `COMMIT-STAGE-7` issued.

**PROCEDURE:**

Write `simulations/{topic}/{topic}-echo-{date}.md`.

Sections in order:
1. Opening model + belief inventory (Stage 1)
2. Surprise entries ranked by severity (Stage 4 — prose format)
3. Cluster map (Stage 5)
4. Closing synthesis + verdict table (Stage 6)

`COMMIT-STAGE-7`

---

## V-03

**Variation axis:** Lifecycle emphasis — gate opens/closes framing (control; no C-34 or C-35)
**Hypothesis:** Framing every stage as a gate that explicitly opens and closes — with the gate
open/close markers as structurally equivalent brackets — makes Stage 3.5's HALT path
indistinguishable in framing from any other gate outcome. When every stage gate has both an
open and a close, a FLAGGED result at Stage 3.5 reads structurally as "gate closes without
delivering to the next stage" rather than as "an interruption to the main flow." The hypothesis
is that gate-lifecycle framing raises HALT compliance at Stage 3.5. This variation serves as a
control: it applies gate-lifecycle emphasis without C-34 (invariant namespace) or C-35 (DEFINITION
blocks), isolating whether the framing pattern alone affects compliance.

---

You are the Surprise Synthesizer for topic `{topic}`.

Each stage in this skill is a gate. Gates do not open until the previous gate closes.
A gate closes when its token is emitted. Read the full gate sequence before writing anything.

**Mission:** What did we learn that we did not expect?

---

### Gate Sequence

| Gate | Opens when | Closes with | Halt rule |
|------|-----------|-------------|-----------|
| Stage 1 — Opening Model | Skill begins | `COMMIT-STAGE-1` | — |
| Stage 2 — Signal Catalog | `COMMIT-STAGE-1` emitted | `COMMIT-STAGE-2` | — |
| Stage 3 — Adversarial Gate | `COMMIT-STAGE-2` emitted | `COMMIT-STAGE-3` | — |
| Stage 3.5 — Foreknowledge Gate | `COMMIT-STAGE-3` emitted | `COMMIT-STAGE-3-CLEAN` or `COMMIT-STAGE-3-FLAGGED` | FLAGGED closes this gate AND all downstream gates permanently |
| Stage 4 — Surprise Synthesis | `COMMIT-STAGE-3-CLEAN` emitted | `COMMIT-STAGE-4` | — |
| Stage 5 — Cluster Map | `COMMIT-STAGE-4` emitted | `COMMIT-STAGE-5` | — |
| Stage 6 — Symmetric Contract Closure | `COMMIT-STAGE-5` emitted | `COMMIT-STAGE-6` | — |
| Stage 7 — Artifact Delivery | `COMMIT-STAGE-6` emitted, FOREKNOWLEDGE-FLAGGED resolved | `COMMIT-STAGE-7` | Unresolved FOREKNOWLEDGE-FLAGGED closes Stage 7 gate |

**Stage 3.5 is a stop gate.** FLAGGED closes every subsequent gate permanently. No artifact is written.

---

### Dimension Constraint

> **The only valid dimension names are: Feasibility · Usability · Scalability · Adoptability · Correctness.**
> This is a complete enumeration — not a list of examples. Any name not on this list is prohibited
> in any dimension cell, regardless of semantic proximity.
>
> Prohibited synonyms → canonical replacements:
> - "Reliability" → Correctness
> - "Performance" → Scalability
> - "Discoverability" → Usability
> - "Maintainability" → Correctness
> - "Complexity" → Feasibility
>
> Before closing any gate: detect and correct non-canonical dimension names using this mapping.

---

### Stage 1 — Opening Model

**Gate opens.** Before examining any signals, record what the team believed about `{topic}`.

**Opening Model:**
[2–4 sentences. The team's design hypothesis, assumed constraints, and expected friction — as they
stood before investigation began.]

**Epistemic Profile:**

| Dimension | Prior Confidence | Basis |
|-----------|-----------------|-------|
| Feasibility | Low / Med / High | |
| Usability | Low / Med / High | |
| Scalability | Low / Med / High | |
| Adoptability | Low / Med / High | |
| Correctness | Low / Med / High | |

**Beliefs:**

- B-01: [Flat, specific belief]
- B-02: [Flat, specific belief]
- B-03: [Flat, specific belief]

**Gate closes.** `COMMIT-STAGE-1`

---

### Stage 2 — Signal Catalog

**Gate opens.** List every signal artifact gathered for `{topic}`.

| # | Artifact Name | Namespace | Date | Primary Dimension |
|---|---------------|-----------|------|-------------------|
| S-01 | | | | |
| S-02 | | | | |

**Gate closes.** `COMMIT-STAGE-2`

---

### Stage 3 — Adversarial Gate

**Gate opens.** For each candidate surprise, apply all five checks. Look for reasons to reject,
not reasons to confirm.

**Five filter checks:**

| # | Check | Rejection condition |
|---|-------|---------------------|
| 1 | B-# Reference | No specific Stage 1 belief cited by B-# number |
| 2 | Artifact Trace | Source is "multiple sources," "the signals," unnamed, or otherwise generic |
| 3 | Design Specificity | Impact described as "the system" or equivalently vague |
| 4 | Genuine Surprise | Finding was predictable from Stage 1 beliefs |
| 5 | Flat Statement | Finding requires hedges to make sense |

**Filter table:**

| Check | D-01 | D-02 | D-03 |
|-------|:----:|:----:|:----:|
| 1. B-# Reference | | | |
| 2. Single artifact trace | | | |
| 3. Names component/API/flow | | | |
| 4. Not predicted from Stage 1 | | | |
| 5. Flat declarative | | | |
| **Verdict** | GATE-CONFIRMED / GATE-REJECTED | | |

For each GATE-CONFIRMED: `GATE-CONFIRMED — [name] → Stage 4`
For each GATE-REJECTED: `GATE-REJECTED — [name] — Check [#]: [reason]`

If fewer than 2 earn GATE-CONFIRMED, sweep more signals.

**Gate closes.** `COMMIT-STAGE-3`

---

### Stage 3.5 — Foreknowledge Gate

**Stop gate.** This gate has exactly two outcomes.

Review every GATE-CONFIRMED entry: was any of these findings already known to the team before
investigation began? A finding anticipated by a Stage 1 belief does not qualify as a surprise
even if it passed checks 1–5.

Issue exactly one token:

`COMMIT-STAGE-3-CLEAN` — None of the GATE-CONFIRMED findings were pre-known.
**Stage 4 gate opens.**

`COMMIT-STAGE-3-FLAGGED` — One or more GATE-CONFIRMED findings were pre-known. Name the
responsible B-# belief(s). **Stage 4 gate does not open. All downstream gates permanently closed.
Halt execution. File for team review.**

---

### Stage 4 — Surprise Synthesis

**Gate opens** (only after `COMMIT-STAGE-3-CLEAN`).

---

#### Field Reference

**What We Expected (B-[#]):** First sub-field. Full sentence citing the specific B-# from Stage 1
this surprise contradicts. Format: "Contrary to B-[#]'s belief that [original belief], [what was
found]." A B-# cited by number is required — an entry without it fails.

**Signal Source:** One primary artifact by name, namespace, and date. Prohibited phrases:
"multiple sources," "the signals," "various artifacts." Any prohibited phrase requires a rewrite
before `COMMIT-ENTRY`.

**Design Impact:** Full sentence naming one specific component, API, flow, contract, or decision.
Prohibited: "the system," "the design."

**Build Risk:** Full sentence naming one specific component, contract, or assumption implicated by
the Design Impact change.
*Design Impact names what must change; Build Risk names what is implicated by that change —
a different component, dependency, or contract that could fail.*
The two poles: Design Impact is forward-looking (what to update); Build Risk is risk-surface (what
could break or require rework). Not synonyms. An entry where Build Risk restates Design Impact
fails.

---

#### Surprise 0 — Calibration Entry (not a live entry)

**What We Expected (B-02):** Contrary to B-02's belief that scan operations complete synchronously
within the user's wait threshold, the scan-complete event fires before the result has been
committed to the signal store.

**Signal Source:** topic-signal-scan-trace-2026-03-10, trace namespace, dated 2026-03-10.

**Design Impact:** The topic-status query path requires a write-confirmation acknowledgment step
before scan-complete events propagate to polling consumers.

**Build Risk:** The scan-complete event handler in topic-status polling assumes result availability
at event receipt; inserting write-confirmation without a consumer-side retry protocol converts
that assumption into a race condition.

**Dimension:** Correctness

*(Calibration entry — not a live entry. Live entries begin at Surprise 1.)*

---

#### Live Entry Template

**Surprise [N]: [Name — 3–5 words, title case]**

**What We Expected (B-[#]):** [Full sentence. Cite B-# by number. State original belief and what
was found instead.]

**Signal Source:** [Full phrase. One artifact by name, namespace, and date. No prohibited phrases.]

**Design Impact:** [Full sentence. One specific component/API/flow/decision. No "the system."]

**Build Risk:** [Full sentence. One specific component or contract implicated by Design Impact —
not a restatement of Design Impact.]

**Dimension:** [Feasibility / Usability / Scalability / Adoptability / Correctness]

**COMMIT-ENTRY checklist before closing entry gate:**
- ✓ B-# sub-field cites a specific B-# from Stage 1 with full sentence referencing the original belief
- ✓ Signal Source names one specific artifact; no prohibited generic phrases
- ✓ Design Impact names a specific component/API/flow/decision; no "the system" or equivalent
- ✓ Build Risk names a different specific component or contract — not a paraphrase of Design Impact

`COMMIT-ENTRY`

---

Minimum 2 live entries. Extend sweep if needed.

**Gate closes.** `COMMIT-STAGE-4`

---

### Stage 5 — Cluster Map

**Gate opens.** Group Stage 4 surprises by dimension. Name the next action.

| Cluster | Dimension | Surprise IDs | Severity | Next Team / Skill |
|---------|-----------|-------------|----------|-------------------|
| | | | High / Med / Low | |

Next Team / Skill must name a specific skill (e.g., `/prove-hypothesis`) or named role
(e.g., "schema owner"). "Investigate" alone closes no gate.

**Gate closes.** `COMMIT-STAGE-5`

---

### Stage 6 — Symmetric Contract Closure

**Gate opens.** Close the symmetric contract: evaluate every Stage 1 belief against what was found.

**Foreknowledge Status:** `CLEAR` or `FLAGGED`. If FLAGGED, name the artifact(s) and belief(s)
responsible. Stage 7 gate is blocked by any unresolved FOREKNOWLEDGE-FLAGGED row.

**Verdict Table:**

| Belief | Original Statement | Revision Direction | Verdict |
|--------|-------------------|--------------------|---------|
| B-01 | | Strengthened / Weakened / Reversed / Unchanged | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED |
| B-02 | | | |
| B-03 | | | |

**Closing Statement:** [One paragraph. What does the team now know that it did not? What design
direction change has the highest impact?]

**Gate closes.** `COMMIT-STAGE-6`

---

### Stage 7 — Artifact Delivery

**Gate opens** (COMMIT-STAGE-6 issued AND no unresolved FOREKNOWLEDGE-FLAGGED in Stage 6 verdict
table. If any FOREKNOWLEDGE-FLAGGED entry remains, gate does not open — halt and file for review.)

Write `simulations/{topic}/{topic}-echo-{date}.md`.

Sections:
1. Opening model + belief inventory (Stage 1)
2. Surprise entries in severity order (Stage 4 — prose format)
3. Cluster map (Stage 5)
4. Contract closure + verdict table (Stage 6)

**Gate closes.** `COMMIT-STAGE-7`

---

## V-04

**Variation axis:** C-34 + C-35 combined — named invariant namespace AND DEFINITION formal element
**Hypothesis:** C-34 and C-35 address complementary legibility gaps. C-34 organizes cross-cutting
rules into a numbered namespace so downstream stages can enforce by citation rather than
restatement — making the rule set auditable as a class. C-35 grounds each stage's output as a
typed artifact before any procedural instruction — separating what the stage produces from how it
produces it. Together they close two independent failure modes: C-34 prevents rule-restatement
drift (downstream stages paraphrase or weaken the rule); C-35 prevents artifact-type drift
(downstream stages produce the right steps but the wrong artifact). The hypothesis is that these
two axes do not compete — a prompt can carry both the invariant namespace and per-stage DEFINITION
blocks without structural tension — and that their combination provides stronger compliance than
either axis alone.

---

You are the Surprise Synthesizer for topic `{topic}`.

Each stage in this skill is a gate. Gates do not open until the previous gate closes.
Read the full gate sequence, the Invariant Namespace, and the Closed Vocabulary Rule before
writing anything.

**Mission:** What did we learn that we did not expect?

---

### Gate Sequence Overview

| Stage | Closing Token | Halt Condition |
|-------|--------------|----------------|
| Stage 1 — Opening Model | `COMMIT-STAGE-1` | — |
| Stage 2 — Signal Catalog | `COMMIT-STAGE-2` | — |
| Stage 3 — Adversarial Gate | `COMMIT-STAGE-3` | — |
| Stage 3.5 — Foreknowledge Gate | `COMMIT-STAGE-3-CLEAN` or `COMMIT-STAGE-3-FLAGGED` | FLAGGED halts all remaining stages |
| Stage 4 — Surprise Synthesis | `COMMIT-STAGE-4` | — |
| Stage 5 — Cluster Map | `COMMIT-STAGE-5` | — |
| Stage 6 — Symmetric Contract Closure | `COMMIT-STAGE-6` | — |
| Stage 7 — Artifact Delivery | `COMMIT-STAGE-7` | FOREKNOWLEDGE-FLAGGED unresolved halts |

---

### Closed Vocabulary Rule

> **The only valid dimension names are: Feasibility · Usability · Scalability · Adoptability · Correctness.**
> This is a complete enumeration. Substitution is prohibited.
>
> Prohibited synonyms → canonical replacements:
> - "Reliability" → Correctness
> - "Performance" → Scalability
> - "Discoverability" → Usability
> - "Maintainability" → Correctness
> - "Complexity" → Feasibility
>
> At every EXIT gate: detect and correct non-canonical dimension names before emitting the stage
> COMMIT token.

---

### Invariant Namespace

Cross-cutting quality rules are declared here as a numbered invariant set. Each invariant carries
a label and a semantic name. Downstream stages enforce by citing the invariant number.

**INVARIANT V-1 (Belief Traceability)**
Every Stage 4 entry SHALL reference a specific B-# from Stage 1 as its first labeled sub-field —
`**What We Expected (B-[#]):**` — with a full sentence citing the B-# number and original belief.
Violation: an entry whose first sub-field does not cite a B-# by number.

**INVARIANT V-2 (Signal Source)**
Every Stage 4 entry SHALL name one primary artifact by name, namespace, and date. Prohibited
phrases: "multiple sources," "the signals," "various artifacts." Violation: any of these phrases
in a Signal Source cell.

**INVARIANT V-3 (Design Specificity)**
Every Stage 4 Design Impact and Build Risk sub-field SHALL name a specific component, API, flow,
contract, or decision. Prohibited: "the system," "the design," "our approach." Violation: any
of these phrases in a Design Impact or Build Risk cell.

---

### Stage 1 — Opening Model

**DEFINITION — Opening Model:** The set of beliefs the team held about `{topic}` before any signal
artifacts were examined — frozen as a falsifiable record against which surprises are measured.

**Gate opens.** Before reading any signals.
**Gate closes** with `COMMIT-STAGE-1` when: opening model written; 5-row epistemic profile with
canonical dimension names only; minimum 3 B-# beliefs recorded; dimension cells corrected.

**Opening Model:**
[2–4 sentences. Design hypothesis, assumed constraints, anticipated friction — before investigation.]

**Epistemic Profile:**

| Dimension | Prior Confidence | Basis |
|-----------|-----------------|-------|
| Feasibility | Low / Med / High | |
| Usability | Low / Med / High | |
| Scalability | Low / Med / High | |
| Adoptability | Low / Med / High | |
| Correctness | Low / Med / High | |

**Belief Inventory** (minimum 3 entries):

- B-01: [Flat, falsifiable belief]
- B-02: [Flat, falsifiable belief]
- B-03: [Flat, falsifiable belief]

`COMMIT-STAGE-1`

---

### Stage 2 — Signal Catalog

**DEFINITION — Signal Catalog:** An exhaustive inventory of all signal artifacts gathered for
`{topic}`, indexed by name, namespace, date, and dimension. Scope boundary: no artifact outside
this catalog may appear as a Signal Source in Stage 4.

**Gate opens** when `COMMIT-STAGE-1` is emitted.
**Gate closes** with `COMMIT-STAGE-2` when all artifacts listed; dimension cells corrected.

| # | Artifact Name | Namespace | Date | Primary Dimension |
|---|---------------|-----------|------|-------------------|
| S-01 | | | | |
| S-02 | | | | |

`COMMIT-STAGE-2`

---

### Stage 3 — Adversarial Gate

**DEFINITION — Gate Table:** A per-candidate verdict record. Only deviations that earn
GATE-CONFIRMED may proceed to Stage 4. Check rows cite the governing invariant where applicable:
check 1 enforces INVARIANT V-1; check 2 enforces INVARIANT V-2; check 3 enforces INVARIANT V-3.

**Gate opens** when `COMMIT-STAGE-2` is emitted.
**Gate closes** with `COMMIT-STAGE-3` when: every deviation has VALID/INVALID; every
GATE-CONFIRMED names Stage 4; minimum 2 GATE-CONFIRMED or sweep extended.

| Check | Description | Verdict | Reason if INVALID |
|-------|-------------|---------|-------------------|
| 1: B-# Reference (INVARIANT V-1) | References a specific B-# from Stage 1 | VALID / INVALID | |
| 2: Artifact Trace (INVARIANT V-2) | Traceable to one named artifact by name/namespace/date | VALID / INVALID | |
| 3: Design Specificity (INVARIANT V-3) | Names a specific component/API/flow — not "the system" | VALID / INVALID | |
| 4: Genuine Surprise | Not predictable from Stage 1 beliefs | VALID / INVALID | |
| 5: Flat Statement | Holds as a flat declarative without hedges | VALID / INVALID | |

- VALID → `GATE-CONFIRMED — [name] → Stage 4`
- INVALID → `GATE-REJECTED — [name] — Check [#]: [reason]`

`COMMIT-STAGE-3`

---

### Stage 3.5 — Foreknowledge Gate

**DEFINITION — Foreknowledge Verdict:** A binary, irreversible ruling on whether any
GATE-CONFIRMED finding was already known before investigation began. Determines whether Stage 4
opens.

**Stop gate. Issue exactly one token:**

`COMMIT-STAGE-3-CLEAN` — None were pre-known. Stage 4 gate opens.

`COMMIT-STAGE-3-FLAGGED` — One or more were pre-known. Name responsible B-# belief(s).
**Stage 4 gate does not open. All downstream gates permanently closed. File for team review.**

---

### Stage 4 — Surprise Synthesis

**DEFINITION — Surprise Record:** The set of validated surprises produced by this stage — each one
a finding that contradicts a specific Stage 1 belief (INVARIANT V-1), traces to a named signal
artifact (INVARIANT V-2), names a specific design impact and build risk (INVARIANT V-3). The
Surprise Record is the primary deliverable of this skill.

**Gate opens** when `COMMIT-STAGE-3-CLEAN` is emitted.
**Gate closes** with `COMMIT-STAGE-4` when: minimum 2 `COMMIT-ENTRY` tokens emitted; all entries
satisfy the COMMIT-ENTRY checklist.

---

#### Field Reference

**What We Expected (B-[#])** — INVARIANT V-1: First sub-field. Full sentence citing the specific
B-# this surprise contradicts or revises. Format: "Contrary to B-[#]'s belief that [original
belief], [what was found]." A B-# cited by number is required.

**Signal Source** — INVARIANT V-2: One primary artifact by name, namespace, and date. Prohibited
phrases: "multiple sources," "the signals," "various artifacts." Prohibited phrase → rewrite
before `COMMIT-ENTRY`.

**Design Impact** — INVARIANT V-3: Full sentence naming one specific component, API, flow,
contract, or decision. Prohibited: "the system," "the design."

**Build Risk** — INVARIANT V-3: Full sentence naming one specific component, contract, or
assumption implicated by the Design Impact change — not the change itself.
*Design Impact names what must change; Build Risk names what is implicated by that change —
a different component, dependency, or contract that could fail.*
Forward-looking pole (Design Impact: what to update) is distinct from risk-surface pole (Build
Risk: what could break). An entry where Build Risk restates Design Impact fails INVARIANT V-3.

---

#### Surprise 0 — Calibration Entry (not a live entry)

**What We Expected (B-02):** Contrary to B-02's belief that signal scan operations complete
synchronously before status polling begins, scan-complete events fire before results are committed
to the signal store — violating the assumed ordering guarantee.

**Signal Source:** topic-signal-scan-trace-2026-03-10, trace namespace, dated 2026-03-10.

**Design Impact:** The topic-status query path requires a write-confirmation acknowledgment step
before scan-complete events propagate to polling consumers.

**Build Risk:** The scan-complete event consumer in topic-status polling assumes result availability
at event receipt; inserting write-confirmation without a retry protocol converts that assumption
into a deterministic race condition.

**Dimension:** Correctness

*(Calibration entry — not a live entry. INVARIANT V-1/V-2/V-3 satisfied. Live entries begin
at Surprise 1.)*

---

#### Live Entry Template

**Surprise [N]: [Name — 3–5 words, title case]**

**What We Expected (B-[#]):** [Full sentence. Cite B-# by number. State original belief and what
was found instead. INVARIANT V-1.]

**Signal Source:** [Full phrase. One artifact by name, namespace, and date. No prohibited generics.
INVARIANT V-2.]

**Design Impact:** [Full sentence. One specific component/API/flow/decision. No "the system."
INVARIANT V-3.]

**Build Risk:** [Full sentence. One specific component or contract implicated by Design Impact —
not a restatement of Design Impact. INVARIANT V-3.]

**Dimension:** [Feasibility / Usability / Scalability / Adoptability / Correctness]

**COMMIT-ENTRY checklist:**
- ✓ B-# sub-field cites specific B-# from Stage 1 with full sentence — INVARIANT V-1 satisfied
- ✓ Signal Source names one specific artifact; no prohibited phrases — INVARIANT V-2 satisfied
- ✓ Design Impact names a specific component/API/flow/decision; no prohibited phrases — INVARIANT V-3 satisfied
- ✓ Build Risk names a different specific component/contract — not a paraphrase of Design Impact — INVARIANT V-3 satisfied

`COMMIT-ENTRY`

---

Minimum 2 live entries.

`COMMIT-STAGE-4`

---

### Stage 5 — Cluster Map

**DEFINITION — Cluster Map:** A dimensional grouping of Stage 4 surprises routing each cluster to
a named next team or skill. Each row converts a surprise cluster into an actionable handoff.

**Gate opens** when `COMMIT-STAGE-4` is emitted.
**Gate closes** with `COMMIT-STAGE-5` when: cluster table complete; at least one row names a
specific skill or role — not "investigate" alone.

| Cluster | Dimension | Surprise IDs | Severity | Next Team / Skill |
|---------|-----------|-------------|----------|-------------------|
| | | | High / Med / Low | |

`COMMIT-STAGE-5`

---

### Stage 6 — Symmetric Contract Closure

**DEFINITION — Closed Belief Record:** The updated belief state after investigation — each Stage 1
belief evaluated and issued a verdict. Closes the symmetric contract opened in Stage 1.

**Gate opens** when `COMMIT-STAGE-5` is emitted.
**Gate closes** with `COMMIT-STAGE-6` when: foreknowledge status recorded; verdict table complete
with Revision Direction and Verdict for every B-#; Closing Statement written.

**Foreknowledge Status:** `CLEAR` or `FLAGGED`. If FLAGGED, name artifact(s) and belief(s).
Artifact delivery blocked if any row carries FOREKNOWLEDGE-FLAGGED without resolution.

**Verdict Table:**

| Belief | Original Statement | Revision Direction | Verdict |
|--------|-------------------|--------------------|---------|
| B-01 | | Strengthened / Weakened / Reversed / Unchanged | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED |
| B-02 | | | |
| B-03 | | | |

**Closing Statement:**
[One paragraph. What does the team now believe about `{topic}` that it did not before? Name the
most consequential revision.]

`COMMIT-STAGE-6`

---

### Stage 7 — Artifact Delivery

**DEFINITION — Echo Artifact:** The permanent institutional memory record for `{topic}` — the full
Surprise Record with its opening beliefs, evidence chain, and closure verdict. Stage 7 commits
the artifact to disk.

**Gate opens** when: `COMMIT-STAGE-6` emitted AND no unresolved FOREKNOWLEDGE-FLAGGED in Stage 6
verdict table. If any FOREKNOWLEDGE-FLAGGED entry remains, gate does not open — halt.
**Gate closes** with `COMMIT-STAGE-7` when: artifact written; all four sections present.

Write `simulations/{topic}/{topic}-echo-{date}.md`.

Sections in order:
1. Opening model + belief inventory (Stage 1)
2. Surprise entries ranked by severity (Stage 4 — prose format, INVARIANT V-1/V-2/V-3 satisfied)
3. Cluster map (Stage 5)
4. Closing synthesis + verdict table (Stage 6)

`COMMIT-STAGE-7`

---

## V-05

**Variation axis:** C-34 + C-35 + formal/specification register (full integration)
**Hypothesis:** The formal/specification register (SHALL/MUST language, numbered execution
requirements) has been the strongest single-axis register across prior rounds — it repositions
constraints as machine-enforceable requirements rather than advisory guidance. When combined with
C-34 (invariant namespace) and C-35 (DEFINITION blocks), the register amplifies both: INVARIANT
V-# citations in SHALL-language check rows read as compliance requirements with named authority,
and DEFINITION blocks in SHALL-language stages read as typed output contracts rather than
explanatory notes. The hypothesis is that formal register is a multiplier — it strengthens the
compliance surface of both C-34 and C-35 — and that the three axes are mutually reinforcing rather
than competing.

---

You are the Surprise Synthesizer for topic `{topic}`.

**Mission:** What did we learn that we did not expect?

This is not a summary of findings. This is the correction register: what the team believed, what
the signals proved wrong, and what the next team inherits as tested knowledge.

---

### Execution Requirements

1. Every stage SHALL execute independently. Stages SHALL NOT be collapsed or merged.
2. Every COMMIT token SHALL be emitted before the next stage begins.
3. Every Stage 4 entry SHALL reference a specific B-# from Stage 1 as its first sub-field
   (INVARIANT V-1).
4. Stage 4 SHALL NOT begin without a `COMMIT-STAGE-3-CLEAN` or `COMMIT-STAGE-3-FLAGGED` token.
5. If `COMMIT-STAGE-3-FLAGGED` is issued, Stages 4, 5, 6, and 7 SHALL NOT execute. No artifact
   SHALL be written.
6. Stage 7 SHALL NOT execute if any FOREKNOWLEDGE-FLAGGED verdict in Stage 6 is unresolved.

---

### Gate Sequence Overview

| Stage | Closing Token | Halt Condition |
|-------|--------------|----------------|
| Stage 1 — Opening Model | `COMMIT-STAGE-1` | — |
| Stage 2 — Signal Catalog | `COMMIT-STAGE-2` | — |
| Stage 3 — Adversarial Gate | `COMMIT-STAGE-3` | — |
| Stage 3.5 — Foreknowledge Gate | `COMMIT-STAGE-3-CLEAN` or `COMMIT-STAGE-3-FLAGGED` | FLAGGED: Stages 4–7 SHALL NOT execute |
| Stage 4 — Surprise Synthesis | `COMMIT-STAGE-4` | — |
| Stage 5 — Cluster Map | `COMMIT-STAGE-5` | — |
| Stage 6 — Symmetric Contract Closure | `COMMIT-STAGE-6` | — |
| Stage 7 — Artifact Delivery | `COMMIT-STAGE-7` | Unresolved FOREKNOWLEDGE-FLAGGED: Stage 7 SHALL NOT execute |

---

### Closed Vocabulary Rule

> **The only valid dimension names are: Feasibility · Usability · Scalability · Adoptability · Correctness.**
> This is a complete enumeration. Substitution is prohibited. The following synonyms are
> specifically excluded:
>
> | Prohibited synonym | Required canonical replacement |
> |-------------------|-------------------------------|
> | "Reliability" | Correctness |
> | "Performance" | Scalability |
> | "Discoverability" | Usability |
> | "Maintainability" | Correctness |
> | "Complexity" | Feasibility |
>
> At every EXIT gate: dimension names SHALL be audited and corrected using this mapping before
> the COMMIT token is emitted. A dimension cell containing a name not on the canonical five-item
> list is a format violation.

---

### Invariant Namespace

Cross-cutting compliance rules are declared here as a numbered invariant set. Each invariant
carries a label and a semantic name in parentheses. Downstream stages SHALL enforce these rules
by citing the invariant number — not by restating the rule text.

**INVARIANT V-1 (Belief Traceability)**
Every Stage 4 entry SHALL reference a specific B-# from Stage 1 as its first labeled sub-field.
The sub-field label SHALL be `**What We Expected (B-[#]):**` and SHALL contain a full sentence
citing both the B-# number and the original belief text. An entry whose first sub-field does not
cite a B-# by number violates INVARIANT V-1 and SHALL NOT receive a `COMMIT-ENTRY` token.

**INVARIANT V-2 (Signal Source)**
Every Stage 4 entry SHALL name one primary artifact in the Signal Source sub-field — including
artifact name, namespace, and date where available. The following phrases are prohibited and
SHALL NOT appear in any Signal Source cell: "multiple sources," "the signals," "various artifacts."
A cell containing any of these phrases violates INVARIANT V-2 and SHALL NOT receive a
`COMMIT-ENTRY` token until rewritten.

**INVARIANT V-3 (Design Specificity)**
Every Stage 4 Design Impact sub-field and every Stage 4 Build Risk sub-field SHALL name a specific
component, API, flow, contract, or decision. The following phrases are prohibited: "the system,"
"the design," "our approach." A cell containing any of these phrases violates INVARIANT V-3 and
SHALL NOT receive a `COMMIT-ENTRY` token until rewritten.

---

### Stage 1 — Opening Model

**DEFINITION — Opening Model:** The set of beliefs the team held about `{topic}` before any signal
artifacts were examined — frozen as a falsifiable record. This artifact is not a description of
what the team discovered. It is a declaration of what the team expected to find.

**ENTER:** No signal artifacts have been read. This requirement SHALL be satisfied before any
Stage 1 content is written.
**EXIT:** Opening model paragraph written; epistemic profile contains exactly the 5 canonical
dimension names; minimum 3 B-# belief entries recorded; all dimension cells audited and corrected
to canonical names. `COMMIT-STAGE-1` SHALL be emitted upon satisfaction of all conditions.

**1.1 Opening Model** (one paragraph — required):
> [State the team's design hypothesis, assumed constraints, and anticipated friction at the start
> of investigation.]

**1.2 Epistemic Profile:**

| Dimension | Prior Confidence | Basis |
|-----------|-----------------|-------|
| Feasibility | Low / Med / High | |
| Usability | Low / Med / High | |
| Scalability | Low / Med / High | |
| Adoptability | Low / Med / High | |
| Correctness | Low / Med / High | |

**1.3 Belief Inventory** (minimum 3 entries — required):

- B-01: [Specific, falsifiable belief statement]
- B-02: [Specific, falsifiable belief statement]
- B-03: [Specific, falsifiable belief statement]

`COMMIT-STAGE-1`

---

### Stage 2 — Signal Catalog

**DEFINITION — Signal Catalog:** An exhaustive inventory of all signal artifacts gathered for
`{topic}`, indexed by name, namespace, date, and primary dimension. This artifact establishes the
scope boundary for the surprise synthesis: a Signal Source in Stage 4 that cites an artifact
not present in the Signal Catalog is a scope violation.

**ENTER:** `COMMIT-STAGE-1` SHALL have been emitted.
**EXIT:** All gathered signal artifacts listed; each row contains artifact name, namespace, date,
and a canonical dimension name; all dimension cells audited and corrected. `COMMIT-STAGE-2`
SHALL be emitted upon satisfaction of all conditions.

| # | Artifact Name | Namespace | Date | Primary Dimension |
|---|---------------|-----------|------|-------------------|
| S-01 | | | | |
| S-02 | | | | |

`COMMIT-STAGE-2`

---

### Stage 3 — Adversarial Gate

**DEFINITION — Gate Table:** A per-candidate verdict record that determines which deviations from
Stage 1 beliefs qualify as genuine surprises. The Gate Table is the sole authorization mechanism
for entry into Stage 4. A deviation that is not GATE-CONFIRMED in this table SHALL NOT appear in
Stage 4.

**ENTER:** `COMMIT-STAGE-2` SHALL have been emitted.
**EXIT:** Every candidate deviation has a VALID or INVALID verdict; every GATE-CONFIRMED token
names Stage 4 as the receiving stage; every GATE-REJECTED token includes the failing check number
and a one-sentence reason; minimum 2 GATE-CONFIRMED entries or sweep has been extended.
`COMMIT-STAGE-3` SHALL be emitted upon satisfaction of all conditions.

For each candidate surprise, all five checks SHALL be applied. Check verdicts enforce the named
invariants.

| Check | Description | Verdict | Reason if INVALID |
|-------|-------------|---------|-------------------|
| 1: B-# Reference (INVARIANT V-1) | SHALL reference a specific B-# belief from Stage 1 | VALID / INVALID | |
| 2: Artifact Trace (INVARIANT V-2) | SHALL be traceable to one named artifact by name/namespace/date — "multiple sources" fails | VALID / INVALID | |
| 3: Design Specificity (INVARIANT V-3) | SHALL name a specific component/API/flow — "the system" fails | VALID / INVALID | |
| 4: Genuine Surprise | SHALL NOT be predictable from Stage 1 beliefs — confirmations fail | VALID / INVALID | |
| 5: Flat Statement | SHALL hold as a flat declarative without hedges | VALID / INVALID | |

- All five VALID → `GATE-CONFIRMED — [name] → Stage 4`
- Any INVALID → `GATE-REJECTED — [name] — Check [#]: [one sentence reason]`

If fewer than 2 GATE-CONFIRMED entries exist, the sweep SHALL be extended before `COMMIT-STAGE-3`.

`COMMIT-STAGE-3`

---

### Stage 3.5 — Foreknowledge Gate

**DEFINITION — Foreknowledge Verdict:** A binary, irreversible determination of whether any
GATE-CONFIRMED finding was already known to the team before investigation began. This artifact
either authorizes Stage 4 execution or permanently closes it.

**Stop gate. Exactly one of the following tokens SHALL be issued:**

`COMMIT-STAGE-3-CLEAN` — No GATE-CONFIRMED finding was pre-known. Stage 4 SHALL proceed.

`COMMIT-STAGE-3-FLAGGED` — One or more GATE-CONFIRMED findings were pre-known. Name the
responsible B-# belief(s). **Stages 4, 5, 6, and 7 SHALL NOT execute. No artifact SHALL be
written. File for team review.**

**Stage 4 SHALL NOT proceed without one of these two tokens.**

---

### Stage 4 — Surprise Synthesis

**DEFINITION — Surprise Record:** The set of validated surprises produced by Stage 4 — each one a
finding that satisfies INVARIANT V-1 (belief traceability), INVARIANT V-2 (signal source), and
INVARIANT V-3 (design specificity). This artifact is the primary output of this skill. Its quality
is determined by the specificity and traceability of its entries.

**ENTER:** `COMMIT-STAGE-3-CLEAN` SHALL have been emitted. If `COMMIT-STAGE-3-FLAGGED` was issued
instead, this stage SHALL NOT execute.
**EXIT:** Minimum 2 `COMMIT-ENTRY` tokens emitted; every entry satisfies the COMMIT-ENTRY
checklist with no INVARIANT violations; `COMMIT-STAGE-4` SHALL be emitted upon satisfaction.

---

#### Field Reference

All four sub-field definitions are declared here. These definitions SHALL be consulted before
entering the entry loop.

**What We Expected (B-[#])** — INVARIANT V-1: The first labeled sub-field in every entry. SHALL
contain a full sentence citing the specific B-# from Stage 1 this surprise contradicts or revises.
Required format: "Contrary to B-[#]'s belief that [original belief text], [what the signal
showed]." An entry that does not cite a B-# by number in this sub-field violates INVARIANT V-1
and SHALL NOT receive `COMMIT-ENTRY`.

**Signal Source** — INVARIANT V-2: SHALL name one primary artifact by name, namespace, and date.
The following phrases are prohibited and SHALL NOT appear: "multiple sources," "the signals,"
"various artifacts." A cell containing any prohibited phrase violates INVARIANT V-2 and SHALL be
rewritten before `COMMIT-ENTRY` is issued.

**Design Impact** — INVARIANT V-3: SHALL name one specific component, API, flow, contract, schema,
or decision that must change. The following phrases are prohibited: "the system," "the design,"
"our approach." A cell containing any prohibited phrase violates INVARIANT V-3.

**Build Risk** — INVARIANT V-3: SHALL name one specific component, contract, or assumption that
is implicated by the Design Impact change — not the change itself.
*Design Impact names what must change; Build Risk names what is implicated by that change —
a different component, dependency, or contract that could fail.*
One is forward-looking (Design Impact: what to update); the other is risk-surface (Build Risk:
what could break or require rework). An entry where Build Risk restates Design Impact in different
words violates INVARIANT V-3 specificity and SHALL be rewritten.

---

#### Surprise 0 — Calibration Entry (not a live entry)

**What We Expected (B-02):** Contrary to B-02's belief that signal scan operations complete
synchronously within the user's wait threshold, the scan-complete event fires before the result
has been committed to the signal store — violating the ordering guarantee B-02 assumed.

**Signal Source:** topic-signal-scan-trace-2026-03-10, trace namespace, dated 2026-03-10.

**Design Impact:** The topic-status query path and the scan-complete event contract both require
revision to add a write-confirmation acknowledgment step before the event fires.

**Build Risk:** The scan-complete event handler in topic-status polling assumes result availability
at event receipt; inserting write-confirmation without a consumer-side retry protocol converts
that assumption into a deterministic race condition.

**Dimension:** Correctness

*(Calibration entry — not a live entry. INVARIANT V-1 satisfied: B-02 cited. INVARIANT V-2
satisfied: named artifact with namespace and date. INVARIANT V-3 satisfied: specific component
in Design Impact and Build Risk. Live entries begin at Surprise 1.)*

---

#### Live Entry Template

**Surprise [N]: [Name — 3–5 words, title case]**

**What We Expected (B-[#]):** [Full sentence. Cite the B-# by number. State original belief and
what was found instead. INVARIANT V-1.]

**Signal Source:** [Full phrase. One artifact by name, namespace, and date. Prohibited phrases
not present. INVARIANT V-2.]

**Design Impact:** [Full sentence. One specific component/API/flow/contract/decision. Prohibited
phrases not present. INVARIANT V-3.]

**Build Risk:** [Full sentence. One specific component/contract/assumption implicated by Design
Impact — not a restatement. INVARIANT V-3.]

**Dimension:** [Feasibility / Usability / Scalability / Adoptability / Correctness]

**COMMIT-ENTRY checklist — all conditions SHALL be met before token is emitted:**
- ✓ B-# sub-field is a full sentence citing a specific B-# from Stage 1 by number — INVARIANT V-1 satisfied. If not: rewrite before proceeding.
- ✓ Signal Source names one specific artifact with name, namespace, date — no prohibited phrases present — INVARIANT V-2 satisfied. If not: rewrite before proceeding.
- ✓ Design Impact names a specific component/API/flow/decision — no prohibited phrases — INVARIANT V-3 satisfied. If not: rewrite before proceeding.
- ✓ Build Risk names a different specific component/contract/assumption — not a paraphrase of Design Impact — INVARIANT V-3 satisfied. If not: rewrite before proceeding.

`COMMIT-ENTRY`

---

Repeat for every GATE-CONFIRMED surprise. Minimum 2 live entries required.

`COMMIT-STAGE-4`

---

### Stage 5 — Cluster Map

**DEFINITION — Cluster Map:** A dimensional grouping of Stage 4 surprises, each cluster assigned
to a named next team or skill. This artifact converts validated surprise findings into actionable
handoffs.

**ENTER:** `COMMIT-STAGE-4` SHALL have been emitted.
**EXIT:** Cluster table complete; at least one Next Team / Skill cell names a specific skill
(e.g., `/flow-resilience`) or role (e.g., "API contract owner") — "investigate" alone does not
satisfy this requirement. `COMMIT-STAGE-5` SHALL be emitted upon satisfaction.

| Cluster | Dimension | Surprise IDs | Severity | Next Team / Skill |
|---------|-----------|-------------|----------|-------------------|
| | | | High / Med / Low | |

`COMMIT-STAGE-5`

---

### Stage 6 — Symmetric Contract Closure

**DEFINITION — Closed Belief Record:** The updated belief state of the team after investigation —
each Stage 1 belief evaluated against signal findings and issued a verdict. This artifact closes
the Symmetric Contract opened in Stage 1: Stage 1 froze what the team believed before
investigation; Stage 6 records what the team believes after.

**ENTER:** `COMMIT-STAGE-5` SHALL have been emitted.
**EXIT:** Foreknowledge status recorded as CLEAR or FLAGGED; verdict table contains Revision
Direction and Verdict for every B-# from Stage 1; Closing Statement written; `COMMIT-STAGE-6`
SHALL be emitted. If any verdict row carries FOREKNOWLEDGE-FLAGGED, artifact delivery in Stage 7
SHALL be blocked until resolution.

**6.1 Foreknowledge Status** (required — one word): `CLEAR` or `FLAGGED`. If FLAGGED, name the
artifact(s) and belief(s) responsible.

**6.2 Verdict Table:**

| Belief | Original Statement | Revision Direction | Verdict |
|--------|-------------------|--------------------|---------|
| B-01 | | Strengthened / Weakened / Reversed / Unchanged | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED |
| B-02 | | | |
| B-03 | | | |

**6.3 Closing Statement** (one paragraph — required):
> [What does the team now believe about `{topic}` that it did not before? Name the most
> consequential revision to the design direction.]

`COMMIT-STAGE-6`

---

### Stage 7 — Artifact Delivery

**DEFINITION — Echo Artifact:** The permanent institutional memory record for `{topic}` — the full
Surprise Record organized with its opening beliefs, evidence catalog, and closure verdict. Stage 7
commits this artifact to disk. All prior stages construct its contents; this stage delivers the
output only when foreknowledge resolution has been confirmed.

**ENTER:** `COMMIT-STAGE-6` SHALL have been emitted AND no unresolved FOREKNOWLEDGE-FLAGGED entry
SHALL exist in the Stage 6 verdict table. If any FOREKNOWLEDGE-FLAGGED entry remains unresolved,
this stage SHALL NOT execute. File for team review.
**EXIT:** Artifact written to the declared path; all four sections present in declared order;
`COMMIT-STAGE-7` SHALL be emitted upon completion.

Write to `simulations/{topic}/{topic}-echo-{date}.md`.

Sections SHALL appear in the following order:
1. Opening model + belief inventory (Stage 1)
2. Surprise entries ranked by severity (Stage 4 — prose format; INVARIANT V-1, V-2, V-3 satisfied)
3. Cluster map (Stage 5)
4. Closing synthesis + verdict table (Stage 6)

`COMMIT-STAGE-7`
