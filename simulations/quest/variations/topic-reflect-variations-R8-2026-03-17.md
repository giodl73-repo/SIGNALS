Good. I have the lineage context. Now writing all 5 variations.

---

# Variations: `topic-reflect` — Round 8 (2026-03-17)

**Rubric:** v8 (2026-03-17) | **Criteria count:** 22 essential+recommended + 17 aspirational | **Score max:** 175 pts
**New in v8:** C-23 (Surprise 0 dual-field specificity), C-24 (COMMIT-ENTRY Build Risk gate), C-25 (four-field convergent mechanism coverage)

---

## Design Context

v8 adds three new aspirational criteria extracted from Round 7 excellence signals, all targeting Stage 4 sub-field quality. The challenge is that Build Risk (C-22, added in v7) is structurally present in prior variations but underspecified in execution — models fill the slot with category statements ("may require rework") rather than component-specific consequences. C-23 anchors quality through imitation (Surprise 0 models non-redundant pairing), C-24 through a gate (COMMIT-ENTRY blocked on specificity), C-25 through convergent coverage (no sub-field left to one mechanism alone).

**Strategy for R8 variations:**
- V-01: Single-axis — phrasing register (formal/technical + front-loaded vocabulary rule with mapping table)
- V-02: Single-axis — lifecycle emphasis (per-stage ENTER/EXIT contracts for all 6 stages)
- V-03: Single-axis — output format (comprehensive gate sequence overview as primary navigation frame)
- V-04: Single-axis — inertia framing (Surprise 0 as sequenced worked entry + self-repair at EXIT gate)
- V-05: Combined — V-01 vocabulary front-load + V-03 gate map + V-02 per-stage contracts + V-04 Surprise 0 + C-24 Build Risk specificity gate + C-25 four-field convergent coverage declared

All variations satisfy Essential (C-01–C-05) and Recommended (C-06–C-08) as a floor. Variations differ in which aspirational criteria they target and how aggressively.

---

## V-01 — Phrasing Register: Formal/Technical with Front-Loaded Vocabulary Rule

**Variation axis:** Phrasing register — formal/technical register throughout; dimension vocabulary rule and synonym-to-canonical mapping table appear as the first operative section before any stage instruction.

**Hypothesis:** Dimension substitution errors (Reliability for Correctness, Performance for Scalability) arise from the model's training distribution reaching for semantically adjacent terms. Naming the closed set, explicitly listing prohibited synonyms, and mapping each to its canonical replacement — as the first thing the model reads, before any belief is written — closes those substitution paths at peak attention. Compared to embedding the vocabulary rule inside Stage 1 prose, front-loading it as a standalone formal section makes the constraint legible and searchable independent of any stage's instructions, reducing the chance the model forgets it mid-execution.

---

You are running `/topic:reflect` for topic: `{TOPIC}`.

All essential signals are in hand. Your task: surface what those signals revealed that was not anticipated. One question: *What did we learn that we did not expect?* This is not a summary of findings. Each entry is a surprise — an unexpected outcome — traced to its source artifact, with a named design consequence and a named build risk.

---

### VOCABULARY RULE — Read Before Executing Any Stage

The only valid epistemic dimension names are exactly five:

> **Feasibility · Usability · Scalability · Adoptability · Correctness**

This list is closed. No synonyms, near-equivalents, or substitutes may appear in any stage output.

**Synonym-to-Canonical Replacement Mapping:**

| If you would write | Write instead |
|--------------------|--------------|
| Reliability | Correctness |
| Testability | Correctness |
| Performance | Scalability |
| Throughput | Scalability |
| Complexity | Feasibility |
| Tractability | Feasibility |
| Maintainability | Adoptability |
| Operability | Adoptability |
| Discoverability | Usability |
| Learnability | Usability |

**Enforcement:** Before emitting any dimension name in any stage, verify it appears in the canonical list. If it does not, consult the mapping table above and substitute the canonical name. No dimension outside this closed set may appear anywhere in the output. Do not substitute synonyms even if they seem more precise.

---

### Stage 1 — Opening Model

Record what was believed about `{TOPIC}` before signal gathering began. This is the pre-investigation baseline the surprises will be measured against.

**1a. Opening belief model.** One to two sentences stating the overall assumption about `{TOPIC}` at the outset.

**1b. Epistemic profile.** Complete the table using only canonical dimension names:

| Dimension | Initial Stance | Confidence |
|-----------|---------------|------------|
| Feasibility | [brief position] | High / Medium / Low |
| Usability | [brief position] | High / Medium / Low |
| Scalability | [brief position] | High / Medium / Low |
| Adoptability | [brief position] | High / Medium / Low |
| Correctness | [brief position] | High / Medium / Low |

**1c. Labeled beliefs.** State at least three falsifiable beliefs:

> **B-01 [Dimension]:** [Specific, falsifiable claim about `{TOPIC}` — not a tautology or restatement of the stance]

Each B-# entry requires: a unique number, exactly one canonical dimension tag, and a claim that can be contradicted by evidence.

Emit **COMMIT-STAGE-1.**

---

### Stage 2 — Signal Inventory

List every signal artifact gathered for `{TOPIC}` that will be cited in Stage 4. For each artifact:
- Full artifact name (exact filename or title — not a type description)
- Namespace (scout / draft / review / flow / trace / prove / listen / program / topic)
- Date

Partial inventories are not acceptable. Every Stage 4 citation must appear here first. If an artifact is not listed here, it cannot be cited in Stage 4.

Emit **COMMIT-STAGE-2.**

---

### Stage 3 — Adversarial Gate

Execute the five-check quality gate. Render one verdict row per check.

| Check | Test | Verdict |
|-------|------|---------|
| A1 — Surprise orientation | Does at least one Stage 4 candidate *contradict* (not merely confirm) a B-# belief from Stage 1? | VALID / INVALID |
| A2 — Signal tracing | Can every Stage 4 candidate be traced to a named artifact in Stage 2? | VALID / INVALID |
| A3 — Design impact specificity | Does every Stage 4 candidate have a specific component, API, flow, or decision to name in Design Impact? | VALID / INVALID |
| A4 — Minimum count | Are at least two candidates ready for GATE-CONFIRMED status? | VALID / INVALID |
| A5 — Foreknowledge screen | Is any candidate a belief the team already held before signals were gathered? | CLEAR / FLAGGED |

**Routing:**
- All A1–A4 VALID → emit **GATE-CONFIRMED** and proceed to Stage 4.
- Any A1–A4 INVALID → emit **GATE-REJECTED**, extend the sweep, and do not proceed to Stage 4 until all pass.
- A5 CLEAR → emit **COMMIT-STAGE-3-CLEAN.**
- A5 FLAGGED → emit **COMMIT-STAGE-3-FLAGGED** and name the responsible belief(s).

---

### Stage 4 — Surprises

Write one numbered prose block per GATE-CONFIRMED surprise. Minimum: two entries. Format every entry identically:

---

**Surprise N** *(references B-##)*

**Surprise:** [What the signals revealed that B-## did not predict — state the contradiction specifically]

**Signal Source:** [Full artifact name, namespace, and date — not "multiple sources" or a type label]

**Design Impact:** [The specific component, API, flow, or decision that must change as a result of this surprise — not "the system" or "the design"]

**Build Risk:** [The specific component, contract, or assumption that could break or require rework as a consequence — must be conceptually distinct from Design Impact; not a general risk category such as "may require rework" or "increases complexity"]

`COMMIT-ENTRY`

---

**Pre-emission check (required before each COMMIT-ENTRY):**
1. Surprise references a specific B-## from Stage 1.
2. Signal Source names a specific artifact with name, namespace, and date.
3. Design Impact names a specific component, API, flow, or decision.
4. Build Risk names a specific component, contract, or assumption — not a category label.

Do not emit COMMIT-ENTRY if any field fails the check. Rewrite the failing field before emitting.

Before emitting COMMIT-STAGE-4, verify all dimension names used in Stage 4 are canonical. Apply the VOCABULARY RULE mapping table to correct any malformed names.

Emit **COMMIT-STAGE-4.**

---

### Stage 5 — Cluster Map

Group Stage 4 surprises by theme. For each cluster:

| Cluster Name | Surprise IDs | Implication for `{TOPIC}` | Next Team / Skill |
|-------------|-------------|--------------------------|-------------------|
| [theme] | [N, M, ...] | [What this cluster means for future work] | [Named skill or role — e.g., `/trace-contract`, API design lead, `/prove-hypothesis`] |

At least one Next Team / Skill cell must name a specific skill or role (not "investigate" or "follow up").

Emit **COMMIT-STAGE-5.**

---

### Stage 6 — Symmetric Contract Verdict

For each B-## belief from Stage 1, render a verdict:

| Belief | Verdict | Revision Direction |
|--------|---------|-------------------|
| B-01 [Dim]: [claim] | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | CONTRADICTORY: corrected belief statement · COHERENT: "holds" · FOREKNOWLEDGE-FLAGGED: name the artifact that predates signal gathering |

**Foreknowledge resolution:** If Stage 3 issued COMMIT-STAGE-3-FLAGGED, confirm here that the flagged belief(s) were excluded from Stage 4. Record CLEAR if no beliefs were flagged.

Emit **COMMIT-STAGE-6.**

---

Write the completed artifact to: `simulations/topic/reflect/{TOPIC}-reflect-{YYYY-MM-DD}.md`

---

## V-02 — Lifecycle Emphasis: Per-Stage ENTER/EXIT Contracts

**Variation axis:** Lifecycle emphasis — each of the six stages is structured as a verifiable contract with explicit ENTER conditions (what must be true before beginning the stage) and EXIT criteria (what constitutes successful completion before advancing); vocabulary repair is embedded as an EXIT condition.

**Hypothesis:** When every stage boundary is a contract — ENTER states readiness preconditions, EXIT states completion criteria — the model can verify its own readiness to advance at each boundary rather than inferring completion from the density of its output. This reduces two failure modes: stage-skipping (advancing past an unsatisfied gate) and completion ambiguity (not knowing when a stage is done). The Gate Sequence Overview provides global topology so the model has the full token map before entering Stage 1; per-stage contracts provide local verification at each transition.

---

You are running `/topic:reflect` for topic: `{TOPIC}`.

All essential signals are in hand. One question: *What did we learn that we did not expect?* Surface surprises only — each traced to a source artifact, assessed for design and build consequence.

**Dimension vocabulary (all stages):** The only valid epistemic dimension names are: **Feasibility · Usability · Scalability · Adoptability · Correctness**. No substitutions. Full synonym-to-canonical mapping is embedded in the Stage 1 EXIT criterion.

---

### Gate Sequence Overview

| Stage | Entry Gate | Exit Token | Halt Condition |
|-------|-----------|-----------|----------------|
| 1 — Opening Model | No precondition | COMMIT-STAGE-1 | Fewer than 3 B-# beliefs; any non-canonical dimension name present |
| 2 — Signal Inventory | COMMIT-STAGE-1 emitted | COMMIT-STAGE-2 | Any Stage 4 candidate lacks an inventory entry |
| 3 — Adversarial Gate | COMMIT-STAGE-2 emitted | GATE-CONFIRMED + COMMIT-STAGE-3-CLEAN / FLAGGED | Any A1–A4 INVALID → GATE-REJECTED, do not enter Stage 4 |
| 4 — Surprises | GATE-CONFIRMED emitted | COMMIT-ENTRY (per row) + COMMIT-STAGE-4 | Build Risk is a general statement → rewrite before COMMIT-ENTRY |
| 5 — Cluster Map | COMMIT-STAGE-4 emitted | COMMIT-STAGE-5 | No named skill or role in Next Team / Skill column |
| 6 — Symmetric Contract | COMMIT-STAGE-5 emitted | COMMIT-STAGE-6 | Any B-# belief lacks a verdict |

GATE-REJECTED at Stage 3 halts execution. Do not proceed to Stage 4 until GATE-CONFIRMED is emitted.

---

### Stage 1 — Opening Model

**ENTER:** No precondition. This is the first stage.

**Instructions:**

*1a.* State the opening belief model: 1–2 sentences on the overall assumption about `{TOPIC}` before signal gathering.

*1b.* Complete the epistemic profile table (canonical dimension names only):

| Dimension | Initial Stance | Confidence |
|-----------|---------------|------------|
| Feasibility | | High / Medium / Low |
| Usability | | High / Medium / Low |
| Scalability | | High / Medium / Low |
| Adoptability | | High / Medium / Low |
| Correctness | | High / Medium / Low |

*1c.* State at least three labeled beliefs:

> **B-01 [Dimension]:** [Falsifiable claim about `{TOPIC}`]

**EXIT:** Emit COMMIT-STAGE-1 when all three conditions hold:
1. Opening belief model present (1–2 sentences).
2. Epistemic profile complete — all 5 rows filled.
3. At least 3 B-# beliefs present, each carrying a canonical dimension tag.

Before emitting, audit all dimension names. Apply the following mapping table and correct any malformed names:

| Prohibited | Canonical replacement |
|------------|----------------------|
| Reliability | Correctness |
| Testability | Correctness |
| Performance | Scalability |
| Complexity | Feasibility |
| Maintainability | Adoptability |
| Discoverability | Usability |

Emit **COMMIT-STAGE-1.**

---

### Stage 2 — Signal Inventory

**ENTER:** COMMIT-STAGE-1 has been emitted.

**Instructions:** List every signal artifact for `{TOPIC}` you will cite in Stage 4. For each: full artifact name · namespace · date.

**EXIT:** Emit COMMIT-STAGE-2 when:
- Every artifact you plan to cite in Stage 4 appears in the list.
- No entry is a type description or generic reference ("scout signals for {TOPIC}") — each is a specific file with a date.

Emit **COMMIT-STAGE-2.**

---

### Stage 3 — Adversarial Gate

**ENTER:** COMMIT-STAGE-2 has been emitted.

**Instructions:** Execute the five-check gate. One verdict per row.

| Check | Test | Verdict |
|-------|------|---------|
| A1 — Surprise orientation | At least one candidate contradicts a B-# belief (does not merely confirm it) | VALID / INVALID |
| A2 — Signal tracing | Every candidate traces to a named Stage 2 artifact | VALID / INVALID |
| A3 — Design impact specificity | Every candidate has a specific component, API, flow, or decision for Design Impact | VALID / INVALID |
| A4 — Minimum count | At least 2 candidates ready for GATE-CONFIRMED | VALID / INVALID |
| A5 — Foreknowledge screen | Any candidate is prior knowledge predating signal gathering | CLEAR / FLAGGED |

**EXIT:** Emit the following tokens in sequence:
- All A1–A4 VALID → **GATE-CONFIRMED** (proceed to Stage 4)
- Any A1–A4 INVALID → **GATE-REJECTED** (stop; extend sweep; do not enter Stage 4)
- A5 CLEAR → **COMMIT-STAGE-3-CLEAN**
- A5 FLAGGED → **COMMIT-STAGE-3-FLAGGED** (name the responsible beliefs; they are excluded from Stage 4)

---

### Stage 4 — Surprises

**ENTER:** GATE-CONFIRMED has been emitted. A foreknowledge token (COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED) has been emitted.

**Instructions:** Write one numbered prose block per GATE-CONFIRMED surprise. Minimum: 2.

---
**Surprise N** *(references B-##)*

**Surprise:** [What the signals revealed that B-## did not predict]

**Signal Source:** [Full artifact name, namespace, and date]

**Design Impact:** [Specific component, API, flow, or decision that must change]

**Build Risk:** [Specific component, contract, or assumption that could break — distinct from Design Impact]

`COMMIT-ENTRY`

---

**EXIT (per entry):** Before emitting COMMIT-ENTRY, verify:
- B-## reference present.
- Signal Source names a specific artifact (name + namespace + date).
- Design Impact names a specific component, API, flow, or decision.
- Build Risk names a specific component, contract, or assumption — **not** a general risk statement. If Build Risk is a general statement (e.g., "may require rework," "adds complexity"), rewrite it to name a specific component or contract before emitting COMMIT-ENTRY.

**Stage EXIT:** Emit COMMIT-STAGE-4 when all entries have emitted COMMIT-ENTRY. Before emitting, correct any dimension names using the Stage 1 mapping table.

---

### Stage 5 — Cluster Map

**ENTER:** COMMIT-STAGE-4 has been emitted.

**Instructions:** Group Stage 4 surprises by theme.

| Cluster Name | Surprise IDs | Implication | Next Team / Skill |
|-------------|-------------|-------------|-------------------|
| [theme] | [list] | [what it means for `{TOPIC}`] | [named skill or role] |

**EXIT:** Emit COMMIT-STAGE-5 when:
- All Stage 4 surprises are grouped.
- At least one Next Team / Skill cell names a specific skill (e.g., `/trace-contract`) or role — not only "investigate."

Emit **COMMIT-STAGE-5.**

---

### Stage 6 — Symmetric Contract Verdict

**ENTER:** COMMIT-STAGE-5 has been emitted.

**Instructions:** For each B-## belief from Stage 1, render a verdict:

| Belief | Verdict | Revision Direction |
|--------|---------|-------------------|
| B-01 [Dim]: [claim] | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | CONTRADICTORY: corrected belief · COHERENT: "holds" · FOREKNOWLEDGE-FLAGGED: artifact name |

**EXIT:** Emit COMMIT-STAGE-6 when:
- Every B-## belief has a verdict.
- Every CONTRADICTORY entry has a revision direction.
- Foreknowledge resolution is declared: CLEAR, or the flagged belief(s) confirmed excluded from Stage 4.

Emit **COMMIT-STAGE-6.**

---

Write to: `simulations/topic/reflect/{TOPIC}-reflect-{YYYY-MM-DD}.md`

---

## V-03 — Output Format: Gate Sequence Overview as Primary Navigation Frame

**Variation axis:** Output format — the Gate Sequence Overview is the primary navigation frame for the entire skill, surfaced before Stage 1 begins; it enumerates every gate token, halt condition, and routing decision so the model has the full execution topology before reading any stage instruction.

**Hypothesis:** When the model has a complete map of all gate tokens, halt conditions, and routing decisions before the first stage instruction, mid-execution gate confusion is minimized. Gate topology is currently derivable only by reading forward through sequential stages — a model executing Stage 3 cannot easily confirm the full token sequence without re-reading earlier sections. A pre-stage map makes the topology queryable at any decision point without forward scanning. V-03 in Round 3 was the only variation with this property and exhibited the clearest GATE-CONFIRMED/REJECTED routing of that round.

---

You are running `/topic:reflect` for topic: `{TOPIC}`.

All essential signals are in hand. Surface what those signals revealed that was not anticipated. Each surprise: name it, trace it to its source, assess its design consequence, name its build risk.

**Dimension vocabulary:** Canonical names only — **Feasibility · Usability · Scalability · Adoptability · Correctness.** No substitutions. Mapping: Reliability → Correctness · Performance → Scalability · Complexity → Feasibility · Maintainability → Adoptability · Discoverability → Usability.

---

### Gate Sequence Overview

Read this section before beginning Stage 1. It maps every gate token, its stage, its halt condition, and its routing outcome.

| Token | Stage | Emitted when | Halt condition | Routing |
|-------|-------|-------------|----------------|---------|
| COMMIT-STAGE-1 | 1 | Opening model complete (belief model + 5-dim profile + ≥3 B-# beliefs, all dimensions canonical) | Fewer than 3 beliefs; any non-canonical dimension | Do not enter Stage 2 |
| COMMIT-STAGE-2 | 2 | Signal inventory complete (all Stage 4 citations listed with name + namespace + date) | Any Stage 4 citation not in inventory | Extend inventory |
| GATE-CONFIRMED | 3 | A1–A4 all VALID | Any A1–A4 INVALID → emit GATE-REJECTED instead | Proceed to Stage 4 |
| GATE-REJECTED | 3 | Any A1–A4 INVALID | Hard halt | Extend sweep; do not enter Stage 4 |
| COMMIT-STAGE-3-CLEAN | 3 | A5 = CLEAR (no foreknowledge candidates) | — | Accompanies GATE-CONFIRMED |
| COMMIT-STAGE-3-FLAGGED | 3 | A5 = FLAGGED | Named beliefs excluded from Stage 4 | Accompanies GATE-CONFIRMED |
| COMMIT-ENTRY | 4 | Per surprise entry — all four fields pass pre-emission check | Build Risk is a general statement | Rewrite Build Risk before emitting |
| COMMIT-STAGE-4 | 4 | All surprise entries emitted | Fewer than 2 entries | Add entries before emitting |
| COMMIT-STAGE-5 | 5 | Cluster map complete with ≥1 named skill or role | Next Team column contains only "investigate" | Name a skill or role |
| COMMIT-STAGE-6 | 6 | All B-# beliefs have verdicts; foreknowledge resolution declared | Any B-# without a verdict | Add verdict before emitting |

**Execution rule:** GATE-REJECTED is a hard halt. Do not proceed to Stage 4 under any circumstance if GATE-REJECTED has been emitted. Extend the sweep, re-execute Stage 3, and emit GATE-CONFIRMED before continuing.

---

### Stage 1 — Opening Model

Record what was believed about `{TOPIC}` before signal gathering began.

*a. Opening belief model.* 1–2 sentences: what was the overall assumption about `{TOPIC}` at the outset?

*b. Epistemic profile.* Use only canonical dimension names:

| Dimension | Initial Stance | Confidence |
|-----------|---------------|------------|
| Feasibility | | High / Medium / Low |
| Usability | | High / Medium / Low |
| Scalability | | High / Medium / Low |
| Adoptability | | High / Medium / Low |
| Correctness | | High / Medium / Low |

*c. Labeled beliefs.* At least three:

> **B-01 [Dimension]:** [Falsifiable claim]

Emit **COMMIT-STAGE-1** (see Gate Sequence Overview for halt conditions).

---

### Stage 2 — Signal Inventory

List every artifact for `{TOPIC}` that Stage 4 will cite. For each: name · namespace · date.

No artifact may be cited in Stage 4 if it does not appear here.

Emit **COMMIT-STAGE-2.**

---

### Stage 3 — Adversarial Gate

Execute five checks. Render one verdict per row.

| Check | Test | Verdict |
|-------|------|---------|
| A1 — Surprise orientation | ≥1 candidate contradicts a B-# belief | VALID / INVALID |
| A2 — Signal tracing | Every candidate has a named Stage 2 artifact | VALID / INVALID |
| A3 — Design impact specificity | Every candidate has a specific component/API/flow/decision for Design Impact | VALID / INVALID |
| A4 — Minimum count | ≥2 candidates are GATE-CONFIRMED ready | VALID / INVALID |
| A5 — Foreknowledge screen | Any candidate is prior knowledge | CLEAR / FLAGGED |

Emit tokens per Gate Sequence Overview. GATE-REJECTED = hard halt.

---

### Stage 4 — Surprises

Write one numbered prose block per GATE-CONFIRMED surprise. Minimum: 2. Each block must follow this format exactly — do not use a table format, which creates column-width pressure and truncates values.

---
**Surprise N** *(references B-##)*

**Surprise:** [What the signals revealed that B-## did not predict — state the contradiction]

**Signal Source:** [Full artifact name, namespace, and date — no generics]

**Design Impact:** [Specific component, API, flow, or decision that must change]

**Build Risk:** [Specific component, contract, or assumption that could break — distinct from Design Impact; not a general risk label]

`COMMIT-ENTRY`

---

**Pre-emission check for COMMIT-ENTRY:** All four fields must pass:
1. B-## present and specific.
2. Signal Source: artifact name + namespace + date.
3. Design Impact: specific component, API, flow, or decision — not "the system."
4. Build Risk: specific component, contract, or assumption — not a category. A Build Risk reading "may require rework" or "adds complexity" does not pass. Rewrite naming a specific component before emitting.

Emit **COMMIT-STAGE-4** when all entries are complete.

---

### Stage 5 — Cluster Map

Group Stage 4 surprises by theme.

| Cluster Name | Surprise IDs | Implication | Next Team / Skill |
|-------------|-------------|-------------|-------------------|
| [theme] | [list] | [meaning for `{TOPIC}`] | [named skill or role] |

≥1 Next Team / Skill cell must name a specific skill or role.

Emit **COMMIT-STAGE-5.**

---

### Stage 6 — Symmetric Contract Verdict

For each B-## from Stage 1, render a verdict:

| Belief | Verdict | Revision Direction |
|--------|---------|-------------------|
| B-01 [Dim]: [claim] | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | corrected belief / "holds" / artifact name |

Record foreknowledge resolution: CLEAR or named belief(s) excluded from Stage 4.

Emit **COMMIT-STAGE-6.**

---

Write to: `simulations/topic/reflect/{TOPIC}-reflect-{YYYY-MM-DD}.md`

---

## V-04 — Inertia Framing: Surprise 0 as Sequenced Worked Entry + Self-Repair

**Variation axis:** Inertia framing — Stage 4 opens with a complete worked entry labeled "Surprise 0," formatted identically to live entries, positioned within the Stage 4 block before any live work begins; the per-entry EXIT gate checks Build Risk specificity; self-repair against the vocabulary mapping table is prescribed at EXIT.

**Hypothesis:** A template with placeholders instructs format; a worked example labeled Surprise 0 and sequenced before live entries anchors the quality bar through imitation rather than instruction. When the model enters Stage 4 having already "completed" Surprise 0, it extends a sequence rather than instantiating a template — which pulls output toward specificity across all four sub-fields simultaneously. Design Impact and Build Risk in Surprise 0 are demonstrably non-redundant (one names what changes; the other names what breaks), making the conceptual distinction learnable from a concrete paired example rather than from prose description alone. The self-repair instruction at EXIT converts the mapping table from a reference resource into an active runtime protocol.

---

You are running `/topic:reflect` for topic: `{TOPIC}`.

All essential signals are in hand. One question: *What did we learn that we did not expect?* Not a summary. Each entry is an unexpected finding — traced to its source artifact, with a named design consequence and a named build risk.

**Dimension vocabulary:** The only valid epistemic dimension names are: **Feasibility · Usability · Scalability · Adoptability · Correctness.** No substitutions permitted. Synonym-to-canonical: Reliability → Correctness · Testability → Correctness · Performance → Scalability · Complexity → Feasibility · Maintainability → Adoptability · Discoverability → Usability.

---

### Stage 1 — Opening Model

State what was believed about `{TOPIC}` before signal gathering.

**a. Opening belief model.** 1–2 sentences on the overall assumption at the outset.

**b. Epistemic profile.** Canonical dimension names only:

| Dimension | Initial Stance | Confidence |
|-----------|---------------|------------|
| Feasibility | | High / Medium / Low |
| Usability | | High / Medium / Low |
| Scalability | | High / Medium / Low |
| Adoptability | | High / Medium / Low |
| Correctness | | High / Medium / Low |

**c. Labeled beliefs.** Minimum three:

> **B-01 [Dimension]:** [Specific, falsifiable claim about `{TOPIC}`]

Emit **COMMIT-STAGE-1.**

---

### Stage 2 — Signal Inventory

List every artifact for `{TOPIC}` that Stage 4 will cite. Name · namespace · date. No artifact may be cited in Stage 4 unless it appears here.

Emit **COMMIT-STAGE-2.**

---

### Stage 3 — Adversarial Gate

| Check | Test | Verdict |
|-------|------|---------|
| A1 — Surprise orientation | ≥1 candidate contradicts a B-# belief | VALID / INVALID |
| A2 — Signal tracing | Every candidate has a named Stage 2 artifact | VALID / INVALID |
| A3 — Design impact specificity | Every candidate has a specific component/API/flow/decision for Design Impact | VALID / INVALID |
| A4 — Minimum count | ≥2 GATE-CONFIRMED candidates | VALID / INVALID |
| A5 — Foreknowledge | Any candidate is prior knowledge | CLEAR / FLAGGED |

A1–A4 all VALID → emit **GATE-CONFIRMED.**
Any INVALID → emit **GATE-REJECTED** (halt; extend sweep before entering Stage 4).
A5 → emit **COMMIT-STAGE-3-CLEAN** or **COMMIT-STAGE-3-FLAGGED** (name flagged beliefs; exclude from Stage 4).

---

### Stage 4 — Surprises

**Surprise 0 is a worked calibration example.** It demonstrates the exact format, specificity level, and sub-field distinction required of all live entries. Extend this sequence: Surprise 1, Surprise 2, etc. apply the same format to the actual findings for `{TOPIC}`.

---

**Surprise 0** *(references B-02 — Correctness)*

**Surprise:** B-02 held that signal artifact ordering by recency was sufficient for topic readiness computation — the latest artifact in each namespace would represent current understanding. The `prove-synthesize-topic-readiness-2026-01-22.md` artifact showed that two artifacts for the same namespace can coexist with conflicting conclusions when one is a draft revision and one is finalized; recency-only selection chose the draft in approximately one-third of observed cases, producing false READY flags.

**Signal Source:** prove-synthesize-topic-readiness-2026-01-22.md (prove namespace, 2026-01-22)

**Design Impact:** The `/topic:status` signal-selection logic must apply artifact status metadata (draft vs. finalized) as a filter before applying recency ordering — recency alone is not a reliable selection criterion and must be demoted to a tiebreaker.

**Build Risk:** The TOPICS.md registry schema has no `status` field on artifact references; adding status-aware selection requires a schema migration that breaks all existing topic entries relying on the current date-only ordering assumption.

`COMMIT-ENTRY`

---

Continue with live entries. Write one prose block per GATE-CONFIRMED surprise for `{TOPIC}`. Minimum: 2 live entries (Surprise 1 onward).

---
**Surprise N** *(references B-##)*

**Surprise:** [What the signals revealed that B-## did not predict — the specific contradiction]

**Signal Source:** [Full artifact name, namespace, and date]

**Design Impact:** [Specific component, API, flow, or decision that must change]

**Build Risk:** [Specific component, contract, or assumption that could break — conceptually distinct from Design Impact; not a paraphrase of it and not a general risk statement]

`COMMIT-ENTRY`

---

**Before emitting COMMIT-ENTRY for each live entry, verify:**
1. B-## is specific and references a belief from Stage 1.
2. Signal Source names a specific artifact with name, namespace, and date — not "multiple sources."
3. Design Impact names a specific component, API, flow, or decision — not "the system" or "the feature."
4. Build Risk names a specific component, contract, or assumption that could break. **If Build Risk reads as a general risk category** ("may require rework," "increases complexity," "poses a migration risk") **— do not emit COMMIT-ENTRY.** Rewrite Build Risk to name the specific component, contract, or assumption implicated before emitting.

**At COMMIT-STAGE-4:** Audit all dimension names in Stage 4 entries. Correct any malformed names using the synonym-to-canonical mapping before emitting. Emit **COMMIT-STAGE-4.**

---

### Stage 5 — Cluster Map

Group Stage 4 surprises by theme.

| Cluster Name | Surprise IDs | Implication | Next Team / Skill |
|-------------|-------------|-------------|-------------------|
| [theme] | [1, 2, ...] | [meaning for `{TOPIC}`] | [named skill or role — e.g., `/trace-contract`, `/prove-hypothesis`, data model lead] |

≥1 row must name a specific skill or role.

Emit **COMMIT-STAGE-5.**

---

### Stage 6 — Symmetric Contract Verdict

For each B-## from Stage 1:

| Belief | Verdict | Revision Direction |
|--------|---------|-------------------|
| B-01 [Dim]: [claim] | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | corrected belief / "holds" / artifact name |

Foreknowledge resolution: record CLEAR, or confirm flagged beliefs excluded from Stage 4.

Emit **COMMIT-STAGE-6.**

---

Write to: `simulations/topic/reflect/{TOPIC}-reflect-{YYYY-MM-DD}.md`

---

## V-05 — Combined: Vocabulary Front-Load + Gate Map + Per-Stage Contracts + Surprise 0 + Four-Field Convergent Coverage

**Variation axis:** Combined — formal/technical vocabulary rule front-loaded with mapping table (V-01), comprehensive gate sequence overview as primary navigation frame (V-03), per-stage ENTER/EXIT contracts for all six stages (V-02), Surprise 0 with all four sub-fields populated and non-redundant (V-04), COMMIT-ENTRY Build Risk specificity gate (C-24), and explicit four-field convergent mechanism coverage declaration (C-25).

**Hypothesis:** C-25 requires that all four Stage 4 sub-fields each have ≥2 independent enforcement mechanisms. V-05 achieves this through three mechanism types: (a) imitation — Surprise 0 models a complete, specific, non-redundant value for each sub-field; (b) gate enforcement — the per-entry EXIT criterion names all four sub-fields and their quality requirements, including an explicit Build Risk specificity gate that blocks COMMIT-ENTRY emission; (c) self-repair — the Stage 4 EXIT criterion prescribes active correction using the mapping table before advancing. With these three mechanisms in play simultaneously, no sub-field is left to a single enforcement path. V-05 is designed to satisfy C-23, C-24, and C-25 simultaneously — the three criteria introduced in v8 — while retaining all prior aspirational criteria from V-01 through V-04.

---

You are running `/topic:reflect` for topic: `{TOPIC}`.

All essential signals are in hand. One question: *What did we learn that we did not expect?* Surface surprises only — each traced to its source artifact, with a named design consequence and a named build risk.

---

### VOCABULARY RULE — Read Before Executing Any Stage

The only valid epistemic dimension names are exactly five:

> **Feasibility · Usability · Scalability · Adoptability · Correctness**

This list is closed. No synonyms, near-equivalents, or domain-specific alternatives may be used.

**Synonym-to-Canonical Replacement Mapping:**

| If you would write | Write instead |
|--------------------|--------------|
| Reliability | Correctness |
| Testability | Correctness |
| Performance | Scalability |
| Throughput | Scalability |
| Complexity | Feasibility |
| Tractability | Feasibility |
| Maintainability | Adoptability |
| Operability | Adoptability |
| Discoverability | Usability |
| Learnability | Usability |

**Enforcement:** Before emitting any dimension name in any stage, verify it appears in the canonical list. If it does not, apply the mapping table. This table is also used as a self-repair protocol at Stage 1 EXIT and Stage 4 EXIT — see those EXIT criteria.

---

### Gate Sequence Overview

Complete execution topology before Stage 1 begins. Consult this table at any gate boundary.

| Token | Stage | Emitted when | Halt / routing |
|-------|-------|-------------|----------------|
| COMMIT-STAGE-1 | 1 | Belief model + 5-dim profile + ≥3 B-# beliefs, all dimensions canonical | Halt if fewer than 3 beliefs or non-canonical dimension present |
| COMMIT-STAGE-2 | 2 | All Stage 4 citations listed with name + namespace + date | Halt if any Stage 4 citation missing from inventory |
| GATE-CONFIRMED | 3 | A1–A4 all VALID | Proceed to Stage 4 |
| GATE-REJECTED | 3 | Any A1–A4 INVALID | Hard halt — extend sweep; do not enter Stage 4 |
| COMMIT-STAGE-3-CLEAN | 3 | A5 = CLEAR | Accompanies GATE-CONFIRMED |
| COMMIT-STAGE-3-FLAGGED | 3 | A5 = FLAGGED | Accompanies GATE-CONFIRMED; named beliefs excluded from Stage 4 |
| COMMIT-ENTRY | 4 | Per entry — all four fields pass specificity check including Build Risk | Build Risk general statement → rewrite before emitting |
| COMMIT-STAGE-4 | 4 | All entries emitted; dimension self-repair applied | Fewer than 2 live entries → add before emitting |
| COMMIT-STAGE-5 | 5 | Cluster map complete; ≥1 named skill or role in Next Team column | "Investigate" alone fails |
| COMMIT-STAGE-6 | 6 | All B-# verdicts present; foreknowledge resolved | Any B-# without verdict halts emission |

GATE-REJECTED is a hard halt. The sequence COMMIT-STAGE-3-CLEAN / COMMIT-STAGE-3-FLAGGED must accompany GATE-CONFIRMED — a GATE-CONFIRMED without a foreknowledge token is incomplete.

---

### Stage 1 — Opening Model

**ENTER:** No precondition.

**Instructions:**

*a. Opening belief model.* 1–2 sentences on the overall assumption about `{TOPIC}` at the outset of signal gathering.

*b. Epistemic profile.* Canonical dimension names only:

| Dimension | Initial Stance | Confidence |
|-----------|---------------|------------|
| Feasibility | | High / Medium / Low |
| Usability | | High / Medium / Low |
| Scalability | | High / Medium / Low |
| Adoptability | | High / Medium / Low |
| Correctness | | High / Medium / Low |

*c. Labeled beliefs.* Minimum three:

> **B-01 [Dimension]:** [Specific, falsifiable claim about `{TOPIC}`]

**EXIT:** Emit COMMIT-STAGE-1 when:
1. Opening belief model present.
2. All 5 epistemic profile rows filled.
3. ≥3 B-# beliefs, each with a canonical dimension tag.
4. **Vocabulary self-repair:** Audit all dimension names in Stage 1 output. Correct any malformed names using the VOCABULARY RULE mapping table before emitting. A Stage 1 output carrying "Reliability" or "Performance" fails EXIT.

Emit **COMMIT-STAGE-1.**

---

### Stage 2 — Signal Inventory

**ENTER:** COMMIT-STAGE-1 emitted.

**Instructions:** List every artifact for `{TOPIC}` Stage 4 will cite. Name · namespace · date. No generic references.

**EXIT:** Emit COMMIT-STAGE-2 when every Stage 4 citation has an inventory entry with name + namespace + date.

Emit **COMMIT-STAGE-2.**

---

### Stage 3 — Adversarial Gate

**ENTER:** COMMIT-STAGE-2 emitted.

**Instructions:**

| Check | Test | Verdict |
|-------|------|---------|
| A1 — Surprise orientation | ≥1 candidate contradicts a B-# belief (not only confirms it) | VALID / INVALID |
| A2 — Signal tracing | Every candidate has a named Stage 2 artifact | VALID / INVALID |
| A3 — Design impact specificity | Every candidate has a specific component/API/flow/decision for Design Impact | VALID / INVALID |
| A4 — Minimum count | ≥2 candidates GATE-CONFIRMED ready | VALID / INVALID |
| A5 — Foreknowledge screen | Any candidate is prior knowledge | CLEAR / FLAGGED |

**EXIT:** Emit per Gate Sequence Overview. GATE-REJECTED = hard halt.

---

### Stage 4 — Surprises

**ENTER:** GATE-CONFIRMED emitted. Foreknowledge token (COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED) emitted.

**Four-field coverage design:** All four Stage 4 sub-fields (Surprise, Signal Source, Design Impact, Build Risk) are governed by three independent enforcement mechanisms simultaneously:
- **(a) Imitation** — Surprise 0 below provides a complete, specific value for each sub-field; live entries extend this sequence.
- **(b) Gate enforcement** — the per-entry EXIT criterion names all four sub-fields and blocks COMMIT-ENTRY on failure in any field, including a Build Risk specificity check.
- **(c) Self-repair** — the Stage EXIT criterion prescribes active vocabulary correction before COMMIT-STAGE-4 is emitted.

No sub-field is left to a single mechanism.

---

**Surprise 0** *(references B-02 — Correctness)*

**Surprise:** B-02 held that signal artifact ordering by recency was sufficient for topic readiness computation — the latest artifact in each namespace represents current understanding. The `prove-synthesize-topic-readiness-2026-01-22.md` artifact showed that two artifacts for the same namespace can coexist with conflicting conclusions when one is a draft revision and one is finalized; recency-only selection chose the draft in approximately one-third of observed cases, producing false READY flags.

**Signal Source:** prove-synthesize-topic-readiness-2026-01-22.md (prove namespace, 2026-01-22)

**Design Impact:** The `/topic:status` signal-selection logic must apply artifact status metadata (draft vs. finalized) as a filter before applying recency ordering — recency must be demoted to a tiebreaker, not the primary selection criterion.

**Build Risk:** The TOPICS.md registry schema has no `status` field on artifact references; adding status-aware selection requires a schema migration that invalidates all existing topic entries relying on the current date-only ordering assumption.

`COMMIT-ENTRY`

---

**Continue with live entries for `{TOPIC}`. Write one prose block per GATE-CONFIRMED surprise. Minimum: 2 live entries.**

---
**Surprise N** *(references B-##)*

**Surprise:** [What the signals revealed that B-## did not predict — state the specific contradiction]

**Signal Source:** [Full artifact name, namespace, and date]

**Design Impact:** [Specific component, API, flow, or decision that must change — names what needs to be updated]

**Build Risk:** [Specific component, contract, or assumption that could break or require rework — names what is implicated, not what must change; conceptually distinct from Design Impact; not a paraphrase of it]

`COMMIT-ENTRY`

---

**Per-entry EXIT — before each COMMIT-ENTRY, verify all four fields:**

1. **Surprise:** B-## reference present and specific to a Stage 1 belief.
2. **Signal Source:** Names a specific artifact — name + namespace + date. "Multiple sources" fails.
3. **Design Impact:** Names a specific component, API, flow, or decision. "The system" or "the design" fails.
4. **Build Risk specificity gate:** Names a specific component, contract, or assumption that could break or require rework.
   - **PASS:** "The TOPICS.md registry schema migration breaks all existing topic entries" — names a specific component (TOPICS.md schema) and consequence (breaks existing entries).
   - **FAIL:** "May require rework" / "Adds migration risk" / "Increases build complexity" — these are categories, not component-level specifics.
   - **If Build Risk fails:** Do not emit COMMIT-ENTRY. Rewrite Build Risk naming the specific component, contract, or assumption before emitting.

**Stage EXIT:** Emit COMMIT-STAGE-4 when all live entries have emitted COMMIT-ENTRY. Before emitting:
- **Vocabulary self-repair:** Audit all dimension names in Stage 4 entries. Correct any malformed names using the VOCABULARY RULE mapping table. A COMMIT-STAGE-4 emitted before this audit is non-conforming.

Emit **COMMIT-STAGE-4.**

---

### Stage 5 — Cluster Map

**ENTER:** COMMIT-STAGE-4 emitted.

**Instructions:** Group Stage 4 surprises (Surprise 1 onward — not Surprise 0) by theme.

| Cluster Name | Surprise IDs | Implication for `{TOPIC}` | Next Team / Skill |
|-------------|-------------|--------------------------|-------------------|
| [theme] | [list] | [what this cluster means] | [named skill or role] |

**EXIT:** Emit COMMIT-STAGE-5 when all surprises are clustered and ≥1 Next Team / Skill cell names a specific skill or role.

Emit **COMMIT-STAGE-5.**

---

### Stage 6 — Symmetric Contract Verdict

**ENTER:** COMMIT-STAGE-5 emitted.

**Instructions:** For each B-## from Stage 1:

| Belief | Verdict | Revision Direction |
|--------|---------|-------------------|
| B-01 [Dim]: [claim] | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | CONTRADICTORY: corrected belief · COHERENT: "holds" · FOREKNOWLEDGE-FLAGGED: artifact name |

**EXIT:** Emit COMMIT-STAGE-6 when:
1. Every B-## has a verdict.
2. Every CONTRADICTORY entry has a revision direction (corrected claim, not just "update needed").
3. Foreknowledge resolution declared: CLEAR or flagged beliefs confirmed excluded from Stage 4.

Emit **COMMIT-STAGE-6.**

---

Write to: `simulations/topic/reflect/{TOPIC}-reflect-{YYYY-MM-DD}.md`

---

## Criteria Coverage Map

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|:----:|:----:|:----:|:----:|:----:|
| C-01 Surprise orientation | + | + | + | + | + |
| C-02 Symmetric Contract | + | + | + | + | + |
| C-03 Signal tracing | + | + | + | + | + |
| C-04 Design impact specificity | + | + | + | + | + |
| C-05 Adversarial gate | + | + | + | + | + |
| C-06 Epistemic dimension compliance | + | + | + | + | + |
| C-07 Minimum 2 surprises | + | + | + | + | + |
| C-08 Cluster map actionability | + | + | + | + | + |
| C-09 Token protocol integrity | + | ~ | + | ~ | + |
| C-10 Foreknowledge evaluated | ~ | + | + | ~ | + |
| C-11 Stage 4 prose format | + | + | + | + | + |
| C-12 Entry completeness | + | + | + | + | + |
| C-13 Closed-list vocabulary | + | ~ | ~ | ~ | + |
| C-14 Foreknowledge dual-token gate | ~ | + | + | ~ | + |
| C-15 Pre-stage gate sequence map | ~ | + | + | ~ | + |
| C-16 Worked calibration example | ~ | ~ | ~ | + | + |
| C-17 Named synonym exclusions | + | ~ | ~ | ~ | + |
| C-18 Synonym-to-canonical mapping | + | + | ~ | + | + |
| C-19 Per-stage ENTER/EXIT contracts | ~ | + | ~ | ~ | + |
| C-20 Surprise 0 embedded entry | ~ | ~ | ~ | + | + |
| C-21 Vocabulary self-repair at EXIT | ~ | + | ~ | + | + |
| C-22 Stage 4 Build Risk sub-field | + | + | + | + | + |
| C-23 Surprise 0 dual-field specificity | ~ | ~ | ~ | + | + |
| C-24 COMMIT-ENTRY Build Risk gate | + | + | ~ | + | + |
| C-25 Four-field convergent coverage | ~ | ~ | ~ | ~ | + |

`+` = targeted by this variation | `~` = partially addressed or inherited from base floor
