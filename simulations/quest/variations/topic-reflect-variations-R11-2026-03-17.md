# /quest:variate — topic-reflect Round 11

## Variation Summary

| Var | Axis | Hypothesis |
|---|---|---|
| V-01 | Lifecycle Emphasis | Positioning the Build Risk triple-anchor in a dedicated field-reference block before Stage 4's entry loop—rather than inline in per-field instructions—gives the model a complete schema read-through before any entry is written, improving triple-anchor retention across all live entries |
| V-02 | Phrasing Register | Imperative second-person ("Do not emit," "Rewrite before continuing") with short sentences increases gate compliance on C-27 and C-28 compared to V-01's explanatory register, because commands reduce parsing load at the point of gate execution |
| V-03 | Output Format | Leading with a Gate Topology Map table (all tokens, halt conditions, flow) before any stage prose reduces mid-execution gate confusion; pairing it with a visual COMMIT-ENTRY checklist (✓ per bullet) maximizes C-28 compliance |
| V-04 | Inertia Framing | Making the failure mode (summarization) explicit throughout—naming the inertia competitor at each gate and labeling "not this / this" contrasts—increases surprise-orientation compliance (C-01, C-07) by preventing the model from drifting into confirmation-reporting |
| V-05 | Combination (V-01 + V-03 + V-04) | Combining ENTER/EXIT lifecycle depth, visual gate topology, and inertia framing produces the highest overall score by closing all four Stage 4 enforcement gaps simultaneously while orienting the model against the default summarization failure |

---

## V-01

**Axis:** Lifecycle Emphasis
**Hypothesis:** Positioning the Build Risk triple-anchor in a dedicated Field Reference block before Stage 4's entry loop—rather than inline in field instructions—gives the model a complete schema read-through before any entry is written, improving triple-anchor retention across all live entries.

---

You are running /topic:reflect for the topic: {topic}

This skill asks one question: What did we learn that we did not expect?

It is not a summary of findings. It is a synthesis of surprises — each surprise named, traced to a source signal, and assessed for its design impact. When enough signals exist, the surprises tell you what the next team needs to know.

---

### Vocabulary Rule — Closed Dimension Set

The only valid epistemic dimension names are:

**Feasibility · Usability · Scalability · Adoptability · Correctness**

Substitution is prohibited. Do not use synonyms, paraphrases, or adjacent terms.

Explicitly prohibited synonyms and their canonical replacements:

| Prohibited | Use Instead |
|---|---|
| Reliability | Correctness |
| Performance | Scalability |
| Complexity | Correctness or Feasibility |
| Maintainability | Adoptability |
| Discoverability | Usability or Adoptability |
| Testability | Correctness or Feasibility |

At every EXIT gate, audit all dimension names against this table and correct any malformed names before emitting the stage token.

---

### Gate Sequence Overview

| Token | Stage | Condition | Effect |
|---|---|---|---|
| COMMIT-STAGE-1 | 1 | Opening model recorded; 3+ beliefs labeled B-#; vulnerable belief identified | Advance to Stage 2 |
| COMMIT-STAGE-2 | 2 | Signal inventory complete; no signal dismissed without written reason | Advance to Stage 3 |
| COMMIT-STAGE-3-CLEAN | 3 | All five adversarial checks pass; no INVALID verdicts | Advance to Stage 4 |
| COMMIT-STAGE-3-FLAGGED | 3 | Any INVALID verdict where foreknowledge is present | Halt; do not advance to Stage 4 |
| COMMIT-ENTRY | 4 | Per-entry: all four sub-field checks pass | Advance to next entry |
| COMMIT-STAGE-4 | 4 | At least 2 GATE-CONFIRMED entries recorded | Advance to Stage 5 |
| COMMIT-STAGE-5 | 5 | Cluster map complete; Next Team column has at least one named skill or role | Advance to Stage 6 |
| COMMIT-STAGE-6 | 6 | Verdict table complete; foreknowledge status explicitly resolved | Artifact complete |

**HALT CONDITION:** If COMMIT-STAGE-3-FLAGGED is emitted, do not emit any further stage tokens. Record the flagged beliefs and close the artifact with a FOREKNOWLEDGE-FLAGGED notation.

---

### Stage 1 — Opening Model

**ENTER:** No prerequisites. Begin here.

Record what you believe before examining what the signals say. This creates the symmetric contract that Stage 6 closes.

1. Write an epistemic profile: your confidence entering this reflection (HIGH / MEDIUM / LOW) and the primary dimension under examination (canonical names only).

2. Record at least 3 beliefs about {topic} held before signals were gathered. Label each B-1, B-2, B-3 in order. Each belief must be a full sentence stating a checkable expectation. Note the dimension each belief addresses.

3. Identify your "vulnerable belief" — the one you expect the signals to contradict most strongly.

**EXIT:** Epistemic profile recorded; 3+ beliefs labeled B-1 through B-N; vulnerable belief identified. Audit dimension names. Emit **COMMIT-STAGE-1**.

---

### Stage 2 — Signal Inventory

**ENTER:** COMMIT-STAGE-1 emitted.

List every artifact gathered for {topic}: namespace, artifact name or description, and date. Write "date unknown" if the date is unavailable. Do not dismiss any signal without a written reason.

**EXIT:** All signals cataloged. No signal dismissed without written reason. Emit **COMMIT-STAGE-2**.

---

### Stage 3 — Adversarial Gate

**ENTER:** COMMIT-STAGE-2 emitted.

Run the five-check table. Every check requires a VALID or INVALID verdict. For each INVALID verdict: state the deviation and the corrective action you will take.

| Check | Question | Verdict |
|---|---|---|
| 1. Surprise vs. confirmation | Do signals contradict at least one Stage 1 belief, or do they only confirm? | |
| 2. Signal specificity | Is every Stage 2 artifact named (not "various sources")? | |
| 3. Foreknowledge audit | Did you hold any Stage 1 belief as already-true knowledge before signals were gathered? | |
| 4. Completeness | Are there at least 2 signals capable of producing GATE-CONFIRMED surprises? | |
| 5. Scope | Does at least one signal address a dimension other than the Stage 1 primary dimension? | |

**EXIT:**
- All five VALID → emit **COMMIT-STAGE-3-CLEAN** → advance to Stage 4.
- Any INVALID and Check 3 is INVALID (foreknowledge present) → emit **COMMIT-STAGE-3-FLAGGED** → halt.
- Any INVALID but Check 3 is VALID → apply corrective action, re-run table, emit COMMIT-STAGE-3-CLEAN only when all checks pass.

---

### Stage 4 — Surprise Synthesis

**ENTER:** COMMIT-STAGE-3-CLEAN emitted.

---

**Field Reference — Read this block before writing any entry.**

Each entry has four sub-fields. Read all four definitions before beginning.

**Surprise:** The unexpected finding. Must reference a specific B-# from Stage 1 and name the gap between what that belief predicted and what the signals showed. Not a summary — a named contradiction or extension.

**Signal Source:** The specific artifact that produced this surprise. Name: artifact name, namespace, and/or date. Do not write "multiple sources." If multiple signals contributed, name the primary one.

**Design Impact:** What must change in the design. Names a specific component, API, flow, or decision. Do not write "the system" — identify the specific element that must be updated.

**Build Risk:** What is implicated by the Design Impact change.

*Triple-anchor definition:*
- **Purpose:** Names the exposure surface opened by the change — what the Design Impact update puts at risk in the existing build.
- **Paired formula:** Design Impact names what must change; Build Risk names what is implicated by that change — a different component, dependency, or contract that could fail.
- **Structural gloss:** One field is forward-looking (what to update); the other is risk-surface (what could break or require rework). They are not paraphrases. The two values must name different elements.

Build Risk must name a specific component, decision, or risk surface — not a general risk category (e.g., "performance risk" is insufficient; "the signal fanout router's backpressure contract" is sufficient).

---

**Surprise 0 — Calibration Entry (not a live entry)**

*Your live entries (Surprise 1, Surprise 2, …) must meet the standard shown here.*

**Surprise 0**

Surprise: B-2 predicted the signal namespace would resolve artifact conflicts at query time using a most-recent-wins rule. The scout-naming signals showed that three production teams enforced conflict resolution at write time via topic registry locks — the opposite sequencing from what B-2 assumed.

Signal Source: scout-naming-{topic}-2024-11-14.md (scout namespace)

Design Impact: The artifact deduplication component in the topic registry must be refactored to support write-time conflict detection, replacing the current query-time merge logic.

Build Risk: The signal lifecycle state machine assumes query-time resolution as its terminal state — write-time detection changes the state transition contract, risking silent inconsistency in any consumer flow that skips the lock step.

COMMIT-ENTRY

---

**Entry instructions:**

For each surprise (GATE-CONFIRMED only):
1. State CONTRADICTS or EXTENDS relative to a specific B-# belief.
2. Write the four sub-fields using the Field Reference above.
3. Run the COMMIT-ENTRY checklist before advancing.

**COMMIT-ENTRY checklist** (run for every entry before emitting the token):

```
[ ] Surprise: Full sentence referencing a specific B-# and naming the expectation-evidence gap
    — if absent or generic: rewrite before continuing
[ ] Signal Source: Named artifact with name, namespace, and/or date
    — if "multiple sources" or unnamed: identify the primary artifact and rewrite
[ ] Design Impact: Names a specific component, API, flow, or decision (not "the system")
    — if vague: identify the specific element and rewrite
[ ] Build Risk: Names a specific component, decision, or risk surface (not a general risk category)
    — if abstract or categorical: identify the specific risk surface and rewrite
```

If all four checks pass: emit **COMMIT-ENTRY**. Proceed to the next surprise.
If any check fails: apply the inline corrective action, re-verify, then emit.

Extend the sweep if fewer than 2 entries pass all checks after the initial scan.

**EXIT:** At least 2 GATE-CONFIRMED entries recorded, all with COMMIT-ENTRY emitted. Audit dimension names. Emit **COMMIT-STAGE-4**.

---

### Stage 5 — Cluster Map

**ENTER:** COMMIT-STAGE-4 emitted.

Group Stage 4 surprises by theme. Produce:

| Cluster | Surprises Included | Dimension | Next Team / Skill | Priority |
|---|---|---|---|---|

Every surprise must appear in exactly one cluster. The Next Team / Skill column must name at least one specific skill (e.g., /flow:trigger) or team role (e.g., "Flow engineer") — not just "investigate."

**EXIT:** Every surprise clustered; Next Team / Skill populated with at least one specific name. Audit dimension names. Emit **COMMIT-STAGE-5**.

---

### Stage 6 — Symmetric Contract Verdict

**ENTER:** COMMIT-STAGE-5 emitted.

Close the symmetric contract from Stage 1. Produce:

| Belief | Verdict | Revision Direction |
|---|---|---|
| B-1: [text] | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | [required if CONTRADICTORY: name a specific update] |

Verdicts:
- **COHERENT** — signals confirmed or did not contradict this belief.
- **CONTRADICTORY** — signals directly contradict this belief. Revision Direction must name a specific change to a design component, spec section, or artifact.
- **FOREKNOWLEDGE-FLAGGED** — this belief was held as already-true knowledge before signals were gathered. If any belief receives this verdict: do not emit COMMIT-STAGE-6; record the flagged belief(s) and close with FOREKNOWLEDGE-FLAGGED.

Explicitly record: **CLEAR** (no foreknowledge) or **FLAGGED** (foreknowledge present).

**EXIT:** All beliefs assessed; foreknowledge status explicitly recorded. Audit dimension names one final time. Emit **COMMIT-STAGE-6**.

---

Artifact complete. Write the topic-reflect artifact for {topic}.

---

## V-02

**Axis:** Phrasing Register
**Hypothesis:** Imperative second-person commands with short sentences increase gate compliance on C-27 and C-28 compared to V-01's explanatory register, because commands reduce parsing load at the point of gate execution and remove hedging language that can defer model action.

---

You are /topic:reflect. Your topic: {topic}

One question: What did we learn that we did not expect?

Do not summarize. Synthesize. Every entry names a surprise, traces it to a signal, and names what changes and what breaks.

---

### Vocabulary — Non-Negotiable

Use only these five dimension names:

**Feasibility · Usability · Scalability · Adoptability · Correctness**

Do not substitute. These specific words are prohibited — replace with the canonical name shown:

| Prohibited | Replace With |
|---|---|
| Reliability | Correctness |
| Performance | Scalability |
| Complexity | Correctness or Feasibility |
| Maintainability | Adoptability |
| Discoverability | Usability or Adoptability |
| Testability | Correctness or Feasibility |

At every EXIT gate: audit all dimension names. Correct malformed names using this table before emitting. Do not emit until all names are canonical.

---

### Gate Map

Read before Stage 1. These are your only tokens.

| Token | When to Emit | If Blocked |
|---|---|---|
| COMMIT-STAGE-1 | Opening model complete, 3+ beliefs labeled | Do not advance |
| COMMIT-STAGE-2 | Signal inventory complete | Do not advance |
| COMMIT-STAGE-3-CLEAN | All 5 checks VALID | Advance to Stage 4 |
| COMMIT-STAGE-3-FLAGGED | Foreknowledge detected | Halt. Do not continue. |
| COMMIT-ENTRY | All 4 sub-field checks pass | Rewrite failing fields, then emit |
| COMMIT-STAGE-4 | 2+ GATE-CONFIRMED entries | Do not advance with fewer |
| COMMIT-STAGE-5 | Cluster map done, Next Team populated | Do not advance |
| COMMIT-STAGE-6 | Verdict table done, foreknowledge resolved | Do not advance |

---

### Stage 1 — Opening Model

**ENTER:** No prerequisites.
**EXIT:** 3+ beliefs labeled, profile complete. Emit **COMMIT-STAGE-1**.

Do this:

1. State your epistemic profile: confidence (HIGH / MEDIUM / LOW), primary dimension (canonical name only).
2. Write 3+ beliefs labeled B-1, B-2, B-3. Each must be a full sentence. Each must be checkable. Each must name a dimension.
3. Name your vulnerable belief — the one the signals will most likely contradict.

Do not skip the vulnerable belief. It is the first signal that Stage 4 must address.

---

### Stage 2 — Signal Inventory

**ENTER:** COMMIT-STAGE-1 emitted.
**EXIT:** All signals listed, no signal dismissed without a written reason. Emit **COMMIT-STAGE-2**.

List every artifact: namespace, name or description, date. Write "date unknown" if unavailable. Do not dismiss any signal silently.

---

### Stage 3 — Adversarial Gate

**ENTER:** COMMIT-STAGE-2 emitted.
**EXIT:** All five checks VALID → emit **COMMIT-STAGE-3-CLEAN**. Foreknowledge present → emit **COMMIT-STAGE-3-FLAGGED** and halt.

Run this table. Verdict must be VALID or INVALID. For every INVALID: write the deviation and the corrective action.

| # | Check | Verdict |
|---|---|---|
| 1 | At least one signal contradicts (not confirms) a Stage 1 belief | |
| 2 | Every Stage 2 artifact is named — no "various sources" | |
| 3 | No Stage 1 belief was held as already-known before signals were gathered | |
| 4 | At least 2 signals can produce GATE-CONFIRMED surprises | |
| 5 | At least one signal addresses a dimension outside the Stage 1 primary | |

If any check is INVALID and Check 3 is INVALID: foreknowledge is present. Emit **COMMIT-STAGE-3-FLAGGED**. Stop.
If any other check is INVALID: apply corrective action. Re-run. Emit COMMIT-STAGE-3-CLEAN only when all five pass.

---

### Stage 4 — Surprise Synthesis

**ENTER:** COMMIT-STAGE-3-CLEAN emitted.
**EXIT:** 2+ GATE-CONFIRMED entries, all with COMMIT-ENTRY emitted. Emit **COMMIT-STAGE-4**.

---

**Four sub-fields. Know each before writing.**

**Surprise:** Name the gap. Reference a specific B-#. State what the belief predicted and what the signal showed instead.

**Signal Source:** Name the artifact. Give name, namespace, and/or date. Do not write "multiple sources."

**Design Impact:** Name what must change. A specific component, API, flow, or decision. Not "the system."

**Build Risk:** Name what the change puts at risk.
- Purpose: identifies the exposure surface opened by the Design Impact change.
- Paired formula: Design Impact names what must change; Build Risk names what is implicated by that change — a different component, dependency, or contract that could fail.
- Structural gloss: Design Impact is forward-looking (what to update); Build Risk is risk-surface (what could break or require rework). They name different elements. They are not paraphrases.

Do not write a general risk category for Build Risk. Name a specific component, decision, or risk surface. "Performance risk" fails. "The auth token cache's TTL contract" passes.

---

**Surprise 0 — Read this first. Your entries must reach this standard.**

Surprise: B-3 predicted the topic registry would assign namespace ownership at creation time, locking ownership permanently. The trace-permissions signals showed that 4 of 6 production namespaces had undergone ownership transfer post-creation using an undocumented admin override path — B-3's assumption of permanent lock-at-creation was wrong.

Signal Source: trace-permissions-{topic}-2024-12-02.md (trace namespace)

Design Impact: The namespace ownership model in the topic registry must be redesigned to support explicit ownership transfer events with an audit trail, replacing the implicit lock-at-creation assumption.

Build Risk: The signal routing layer uses namespace ownership as a static key for fan-out decisions — dynamic ownership transfer invalidates cached routing tables and can silently send signals to the previous owner's consumers.

COMMIT-ENTRY

---

**Entry checklist — Run before every COMMIT-ENTRY:**

```
[ ] Surprise references a specific B-# and names the expectation-evidence gap
    FAIL: rewrite with a B-# reference and the specific gap before continuing
[ ] Signal Source names a specific artifact (name, namespace, date)
    FAIL: identify the primary artifact and rewrite — "multiple sources" is not acceptable
[ ] Design Impact names a specific component, API, flow, or decision
    FAIL: remove "the system" — name the specific element and rewrite
[ ] Build Risk names a specific component, decision, or risk surface (not a category)
    FAIL: remove the generic category — name the specific risk surface and rewrite
```

All four pass: emit **COMMIT-ENTRY**. Any check fails: apply the corrective action at that bullet, then re-verify.

Write Surprise 1, Surprise 2, and any further GATE-CONFIRMED surprises. Extend the sweep if fewer than 2 pass after the initial scan.

---

### Stage 5 — Cluster Map

**ENTER:** COMMIT-STAGE-4 emitted.
**EXIT:** Every surprise clustered; Next Team column has at least one named skill or role. Audit dimension names. Emit **COMMIT-STAGE-5**.

Produce:

| Cluster | Surprises | Dimension | Next Team / Skill | Priority |
|---|---|---|---|---|

Every surprise goes into exactly one cluster. Name a skill (e.g., /trace:permissions) or a role (e.g., "Platform engineer") in Next Team / Skill. "Investigate" is not acceptable.

---

### Stage 6 — Symmetric Contract Verdict

**ENTER:** COMMIT-STAGE-5 emitted.
**EXIT:** All beliefs assessed; foreknowledge status recorded as CLEAR or FLAGGED. Audit dimension names. Emit **COMMIT-STAGE-6**.

Produce:

| Belief | Verdict | Revision Direction |
|---|---|---|
| B-1: [text] | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | [specific update if CONTRADICTORY] |

CONTRADICTORY requires a revision direction naming a specific design component, spec section, or artifact.
FOREKNOWLEDGE-FLAGGED: do not emit COMMIT-STAGE-6. Record the belief and close with FOREKNOWLEDGE-FLAGGED.

State explicitly: **CLEAR** or **FLAGGED**.

---

Artifact complete. Write the topic-reflect artifact for {topic}.

---

## V-03

**Axis:** Output Format
**Hypothesis:** Leading with a Gate Topology Map table before any stage prose, and rendering the COMMIT-ENTRY gate as a ✓ checklist with per-bullet corrective actions, increases gate compliance (C-15, C-28) more than embedding the same information in stage prose, because the model can scan the full gate topology before entering any stage and re-read the checklist without parsing prose at the point of emission.

---

You are running /topic:reflect for the topic: {topic}

---

## GATE TOPOLOGY MAP

*Read this table before entering Stage 1. It maps every token, condition, and halt in this skill.*

| Token | Emitted At End Of | Pass Condition | Effect on Execution |
|---|---|---|---|
| COMMIT-STAGE-1 | Stage 1 | Epistemic profile + 3+ B-# beliefs + vulnerable belief recorded | Advance to Stage 2 |
| COMMIT-STAGE-2 | Stage 2 | Signal inventory complete, no silent dismissals | Advance to Stage 3 |
| COMMIT-STAGE-3-CLEAN | Stage 3 | All 5 adversarial checks VALID | Advance to Stage 4 |
| COMMIT-STAGE-3-FLAGGED | Stage 3 | Foreknowledge detected (Check 3 INVALID) | **HALT** — do not advance; close artifact with FOREKNOWLEDGE-FLAGGED |
| COMMIT-ENTRY | Stage 4, per entry | All 4 sub-field ✓ checks pass | Advance to next entry |
| COMMIT-STAGE-4 | Stage 4 | 2+ GATE-CONFIRMED entries emitted | Advance to Stage 5 |
| COMMIT-STAGE-5 | Stage 5 | Cluster map complete, Next Team populated | Advance to Stage 6 |
| COMMIT-STAGE-6 | Stage 6 | Verdict table complete, foreknowledge resolved | Artifact complete |

---

## VOCABULARY TABLE

*This table is the complete and closed list of valid epistemic dimension names.*

| Valid (use only these) | Prohibited (never use) | If you wrote the prohibited form... |
|---|---|---|
| Correctness | Reliability, Testability, Accuracy | → replace with Correctness |
| Scalability | Performance, Throughput | → replace with Scalability |
| Feasibility | Complexity, Buildability | → replace with Feasibility |
| Adoptability | Maintainability, Discoverability | → replace with Adoptability |
| Usability | Discoverability, Learnability | → replace with Usability |

**Rule:** At every EXIT gate, scan all dimension names. For any name not in the "Valid" column, find its replacement in the third column and correct it before emitting the stage token.

---

## SKILL PURPOSE

This skill synthesizes surprises — not findings. The question is not "what did the signals show?" It is "what did we learn that we did not expect?"

Every Stage 4 entry names a surprise, traces it to a named artifact, and identifies what must change and what is placed at risk by that change.

---

## Stage 1 — Opening Model

**ENTER:** No prerequisites. Begin here.

Produce three elements:

**1. Epistemic Profile**
| Field | Value |
|---|---|
| Confidence entering this reflection | HIGH / MEDIUM / LOW |
| Primary dimension under examination | [canonical name] |

**2. Belief Inventory** — at least 3 beliefs, labeled B-1, B-2, B-3, ...

Each belief: one full checkable sentence. Label its dimension.

**3. Vulnerable Belief** — name the B-# most likely to be contradicted by the signals.

**EXIT:** Profile + 3+ beliefs + vulnerable belief recorded. Scan dimension names. Emit **COMMIT-STAGE-1**.

---

## Stage 2 — Signal Inventory

**ENTER:** COMMIT-STAGE-1 emitted.

List all gathered artifacts for {topic}:

| Artifact Name / Description | Namespace | Date |
|---|---|---|

Do not dismiss any signal without writing a reason.

**EXIT:** All signals cataloged, no silent dismissals. Emit **COMMIT-STAGE-2**.

---

## Stage 3 — Adversarial Gate

**ENTER:** COMMIT-STAGE-2 emitted.

| # | Check | VALID / INVALID | Deviation + Corrective Action (if INVALID) |
|---|---|---|---|
| 1 | Signals contradict at least one Stage 1 belief (not merely confirm) | | |
| 2 | All Stage 2 artifacts are named — no "various sources" entries | | |
| 3 | No Stage 1 belief was held as already-known before signal gathering | | |
| 4 | At least 2 signals can support GATE-CONFIRMED surprises | | |
| 5 | At least one signal addresses a dimension outside the Stage 1 primary | | |

**EXIT routing:**

```
All 5 VALID?
  Yes → emit COMMIT-STAGE-3-CLEAN → advance to Stage 4
  No, Check 3 INVALID → emit COMMIT-STAGE-3-FLAGGED → HALT
  No, other check INVALID → apply corrective action → re-run table → repeat until COMMIT-STAGE-3-CLEAN
```

---

## Stage 4 — Surprise Synthesis

**ENTER:** COMMIT-STAGE-3-CLEAN emitted.

---

### Stage 4 Field Definitions

**Surprise**
Full sentence naming the unexpected finding. Must reference a specific B-# from Stage 1. Must name the gap between what the belief predicted and what the signal showed.

**Signal Source**
The artifact that produced this surprise. Must include name, namespace, and/or date. "Multiple sources" is not acceptable.

**Design Impact**
The specific component, API, flow, or decision that must change. Not "the system." One specific element.

**Build Risk**
What is implicated by the Design Impact change.

```
Build Risk — three-anchor definition:

  ANCHOR 1 (purpose):    Names the exposure surface opened by the Design Impact change
                         — what the change puts at risk in the existing build.

  ANCHOR 2 (formula):    Design Impact names what must change;
                         Build Risk names what is implicated by that change
                         — a different component, dependency, or contract that could fail.

  ANCHOR 3 (structure):  One field is forward-looking (what to update).
                         The other is risk-surface (what could break or require rework).
                         They name different elements. They are not paraphrases of each other.
```

Build Risk must name a specific component, decision, or risk surface. A general risk category (e.g., "performance risk," "data integrity") fails the COMMIT-ENTRY check.

---

### Surprise 0 — Calibration Entry

*This entry is not live. It demonstrates the exact format and quality bar for all four sub-fields. Write Surprise 1 and beyond at this standard.*

**Surprise 0**

Surprise: B-1 predicted that the /flow:trigger skill would be the only integration point for external event producers. The flow-integration signals showed that 5 of 8 teams were routing events directly to the signal bus, bypassing /flow:trigger entirely — B-1's assumption of a single integration point was false.

Signal Source: flow-integration-{topic}-2025-01-08.md (flow namespace)

Design Impact: The /flow:trigger contract must be refactored to include a bus-native event schema so that direct bus producers can be brought under a single contract boundary rather than operating outside the skill's governance.

Build Risk: The event schema validator in the signal bus assumes all producers use /flow:trigger's field encoding — direct bus producers use a different field layout, so the validator's field-mapping rules will reject valid signals once the contract is enforced.

COMMIT-ENTRY

---

### Entry Instructions

For each GATE-CONFIRMED surprise:
1. State CONTRADICTS or EXTENDS relative to a specific B-# belief.
2. Fill in all four sub-fields.
3. Run the COMMIT-ENTRY checklist.

**COMMIT-ENTRY checklist:**

```
✓ Surprise
  PASS: Full sentence with specific B-# reference and named expectation-evidence gap
  FAIL: Rewrite with B-# reference and the specific gap before emitting

✓ Signal Source
  PASS: Named artifact with name, namespace, and/or date
  FAIL: Identify the primary artifact — replace "multiple sources" or unnamed reference, then rewrite

✓ Design Impact
  PASS: Names a specific component, API, flow, or decision (not "the system")
  FAIL: Identify the specific element — remove vague scope, rewrite

✓ Build Risk
  PASS: Names a specific component, decision, or risk surface (not a risk category)
  FAIL: Identify the specific risk surface — remove general category, rewrite
```

All four ✓: emit **COMMIT-ENTRY**. Any fail: apply corrective action at that bullet, re-verify.

Extend sweep if fewer than 2 entries pass.

**EXIT:** 2+ GATE-CONFIRMED entries, all with COMMIT-ENTRY. Scan dimension names. Emit **COMMIT-STAGE-4**.

---

## Stage 5 — Cluster Map

**ENTER:** COMMIT-STAGE-4 emitted.

| Cluster Name | Surprises | Dimension | Next Team / Skill | Priority |
|---|---|---|---|---|

Every surprise in exactly one cluster. Next Team / Skill must name a specific skill (e.g., /scout:feasibility) or role (e.g., "API designer") — not "investigate."

**EXIT:** All surprises clustered, Next Team populated with specific skill or role. Scan dimension names. Emit **COMMIT-STAGE-5**.

---

## Stage 6 — Symmetric Contract Verdict

**ENTER:** COMMIT-STAGE-5 emitted.

| Belief | Verdict | Revision Direction |
|---|---|---|
| B-1: [text] | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | [specific update required if CONTRADICTORY] |

- **COHERENT:** signals confirmed or did not contradict.
- **CONTRADICTORY:** signals directly contradict. Name a specific design update.
- **FOREKNOWLEDGE-FLAGGED:** held as already-known before gathering. Do not emit COMMIT-STAGE-6. Record belief. Close with FOREKNOWLEDGE-FLAGGED.

Explicit foreknowledge resolution: **CLEAR** or **FLAGGED**.

**EXIT:** All beliefs assessed, foreknowledge explicitly stated. Scan dimension names. Emit **COMMIT-STAGE-6**.

---

Artifact complete. Write the topic-reflect artifact for {topic}.

---

## V-04

**Axis:** Inertia Framing
**Hypothesis:** Naming the summarization failure mode explicitly at the skill opening and at each gate—"the inertia version of this skill does X; this skill does Y"—prevents the model from drifting into confirmation-reporting, increasing surprise-orientation compliance (C-01) and Stage 4 entry quality across the sweep.

---

You are running /topic:reflect for the topic: {topic}

---

### What This Skill Is Not

The inertia version of this skill produces a summary: a list of what the signals showed, organized by namespace. It confirms the opening model. It provides no new information to the next team.

This skill does none of that.

This skill asks one question: **What did we learn that we did not expect?**

Every Stage 4 entry names a surprise — a finding that contradicts or materially extends a belief recorded before the signals were gathered. If an entry confirms a belief, it is not a surprise. If a belief was already known before the signals existed, the entire artifact is flagged and not emitted.

The inertia failure mode reappears at three gates. Each gate names it explicitly and instructs you to stop.

---

### Vocabulary Rule

The only valid epistemic dimension names are:

**Feasibility · Usability · Scalability · Adoptability · Correctness**

The following are prohibited and must be replaced:

| Prohibited | Replace With |
|---|---|
| Reliability | Correctness |
| Performance | Scalability |
| Complexity | Correctness or Feasibility |
| Maintainability | Adoptability |
| Discoverability | Usability or Adoptability |
| Testability | Correctness or Feasibility |

At every EXIT gate: scan all dimension names; correct any malformed name using this table before emitting.

---

### Gate Sequence

| Token | Stage | Condition | Effect |
|---|---|---|---|
| COMMIT-STAGE-1 | 1 | Opening model complete | Advance |
| COMMIT-STAGE-2 | 2 | Signal inventory complete | Advance |
| COMMIT-STAGE-3-CLEAN | 3 | All 5 checks VALID | Advance to Stage 4 |
| COMMIT-STAGE-3-FLAGGED | 3 | Foreknowledge detected | Halt |
| COMMIT-ENTRY | 4 | All 4 sub-field checks pass | Next entry |
| COMMIT-STAGE-4 | 4 | 2+ GATE-CONFIRMED entries | Advance |
| COMMIT-STAGE-5 | 5 | Cluster map done | Advance |
| COMMIT-STAGE-6 | 6 | Verdict table done | Artifact complete |

---

### Stage 1 — Opening Model

**ENTER:** No prerequisites.

*Inertia failure mode at this stage:* recording beliefs so vague that no signal could contradict them. Each belief must be checkable — it either survived the signals or it did not.

1. Epistemic profile: confidence (HIGH / MEDIUM / LOW); primary dimension (canonical name only).
2. At least 3 beliefs, labeled B-1, B-2, B-3. Each: a full sentence, a named dimension, a checkable expectation.
3. Vulnerable belief: the B-# most likely to be directly contradicted by the signals.

**EXIT:** Profile, 3+ beliefs, vulnerable belief recorded. Dimension names canonical. Emit **COMMIT-STAGE-1**.

---

### Stage 2 — Signal Inventory

**ENTER:** COMMIT-STAGE-1 emitted.

*Inertia failure mode:* selecting only signals that support the opening model. Catalog all signals, including those that may contradict Stage 1 beliefs.

List every artifact: namespace, name/description, date. No signal dismissed without a written reason.

**EXIT:** All signals cataloged. Emit **COMMIT-STAGE-2**.

---

### Stage 3 — Adversarial Gate

**ENTER:** COMMIT-STAGE-2 emitted.

*Inertia failure mode:* advancing to Stage 4 when the signals only confirm the opening model. Check 1 blocks this directly.

Run the five-check table:

| # | Check | Verdict |
|---|---|---|
| 1 | At least one signal contradicts (not confirms) a Stage 1 belief — if only confirmations exist, Stage 4 cannot produce genuine surprises | |
| 2 | All Stage 2 artifacts are named — no "various sources" | |
| 3 | No Stage 1 belief was held as already-known before signal gathering | |
| 4 | At least 2 signals can produce GATE-CONFIRMED surprises | |
| 5 | At least one signal addresses a dimension outside the Stage 1 primary | |

VALID / INVALID for each. For each INVALID: state deviation and corrective action.

**EXIT:**
- All VALID → emit **COMMIT-STAGE-3-CLEAN** → Stage 4.
- Check 3 INVALID (foreknowledge) → emit **COMMIT-STAGE-3-FLAGGED** → halt; record flagged beliefs; close artifact.
- Other INVALID → apply corrective action; re-run; emit COMMIT-STAGE-3-CLEAN only when all VALID.

---

### Stage 4 — Surprise Synthesis

**ENTER:** COMMIT-STAGE-3-CLEAN emitted.

*Inertia failure mode at Stage 4:* entries that describe what a signal showed without naming the contradiction to a specific belief. Every entry must name the gap — what the belief predicted versus what the signal showed instead. An entry with no B-# reference has drifted into summary territory. Stop and rewrite it.

---

**Sub-field definitions:**

**Surprise:** The named gap. References a specific B-# from Stage 1. States what the belief predicted and what the signal showed instead. Not a finding — a contradiction or extension.

**Signal Source:** The artifact that produced the surprise. Name, namespace, and/or date. Not "multiple sources."

**Design Impact:** What must change. A specific component, API, flow, or decision. Not "the system."

**Build Risk:** The exposure surface opened by the Design Impact change.

*Triple-anchor definition:*
- *Purpose:* Names what the change puts at risk — the component or contract made vulnerable by the Design Impact update.
- *Formula:* Design Impact names what must change; Build Risk names what is implicated by that change — a different component, dependency, or contract that could fail.
- *Structural gloss:* Design Impact is forward-looking (what to update). Build Risk is risk-surface (what could break or require rework). The two fields name different elements. Writing a paraphrase of Design Impact as Build Risk is the inertia failure for this sub-field.

Build Risk must name a specific component, decision, or risk surface. A general risk category (e.g., "introduces scalability risk") fails the entry gate.

---

**Surprise 0 — Calibration Entry (not live)**

*This entry models every sub-field at the required quality bar. Note: Surprise names a specific B-#; Signal Source names a real artifact; Design Impact names a specific component; Build Risk names a different specific element from Design Impact.*

Surprise: B-2 predicted the topic registry would accept namespace registrations idempotently, allowing re-registration without side effects. The listen-adoption signals showed that 6 of 10 teams had encountered silent state corruption on second registration — re-registration overwrites the namespace owner field without an event being emitted, contradicting B-2's idempotency assumption.

Signal Source: listen-adoption-{topic}-2025-02-11.md (listen namespace)

Design Impact: The topic registry's namespace registration handler must be refactored to detect re-registration and emit an explicit ownership-update event rather than overwriting state silently.

Build Risk: The signal-lifecycle state machine indexes namespace state by owner at registration time — silent overwrites produce a stale owner reference that persists in the lifecycle index, causing fan-out to deliver signals to the previous owner's consumers indefinitely.

COMMIT-ENTRY

---

**Entry instructions:**

For each GATE-CONFIRMED surprise (not summaries, not confirmations):
1. State CONTRADICTS or EXTENDS relative to a specific B-#.
2. Fill in all four sub-fields using the definitions above.
3. Run the COMMIT-ENTRY checklist.

**COMMIT-ENTRY checklist:**

```
[ ] Surprise: references a specific B-# and names the expectation-evidence gap
    Inertia check: if no B-# or if the entry reads as a finding rather than a gap, rewrite

[ ] Signal Source: named artifact with name, namespace, and/or date
    Inertia check: "multiple sources" or unnamed = not a specific source; identify and rewrite

[ ] Design Impact: names a specific component, API, flow, or decision
    Inertia check: "the system" or scope-less language = rewrite naming the specific element

[ ] Build Risk: names a specific component, decision, or risk surface
    Inertia check: if Build Risk paraphrases Design Impact or names a category, rewrite
    naming the specific risk surface opened by the change
```

All four pass: emit **COMMIT-ENTRY**. Any fail: apply the corrective action, re-verify.

Extend sweep if fewer than 2 pass.

**EXIT:** 2+ GATE-CONFIRMED entries, all COMMIT-ENTRY emitted. Scan dimensions. Emit **COMMIT-STAGE-4**.

---

### Stage 5 — Cluster Map

**ENTER:** COMMIT-STAGE-4 emitted.

*Inertia failure mode:* Next Team column reads "investigate further." Name a specific skill or role.

| Cluster | Surprises | Dimension | Next Team / Skill | Priority |
|---|---|---|---|---|

Every surprise in exactly one cluster. Next Team: at least one specific skill (e.g., /prove:hypothesis) or role (e.g., "Namespace architect").

**EXIT:** All clustered; Next Team specific. Scan dimensions. Emit **COMMIT-STAGE-5**.

---

### Stage 6 — Symmetric Contract Verdict

**ENTER:** COMMIT-STAGE-5 emitted.

Close the symmetric contract from Stage 1. Assess every belief against what the signals showed.

*Inertia failure mode:* marking every belief COHERENT. At least one belief should be CONTRADICTORY if Stage 4 produced genuine surprises.

| Belief | Verdict | Revision Direction |
|---|---|---|
| B-1: [text] | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | [required if CONTRADICTORY] |

- **COHERENT:** signals confirmed or did not contradict.
- **CONTRADICTORY:** signals directly contradict. Name a specific update to a design component, spec, or artifact.
- **FOREKNOWLEDGE-FLAGGED:** held as already-known before signals. Do not emit COMMIT-STAGE-6. Record. Close with FOREKNOWLEDGE-FLAGGED.

Explicit record: **CLEAR** or **FLAGGED**.

**EXIT:** All beliefs assessed; foreknowledge stated. Scan dimensions. Emit **COMMIT-STAGE-6**.

---

Artifact complete. Write the topic-reflect artifact for {topic}.

---

## V-05

**Axis:** Combination (V-01 Lifecycle Depth + V-03 Visual Gate Map + V-04 Inertia Framing)
**Hypothesis:** Combining a Gate Topology Map before Stage 1 (V-03), explicit ENTER/EXIT lifecycle contracts per stage (V-01), and inertia-failure-mode callouts at each gate (V-04) closes all four enforcement gaps for Stage 4 simultaneously — structural scanning support (C-15), lifecycle verification (C-19), and surprise-orientation reinforcement (C-01, C-07) — while C-27 and C-28 are jointly maximized by the Field Reference block and the ✓ checklist format.

---

You are running /topic:reflect for the topic: {topic}

This skill synthesizes surprises. Not summaries. Not confirmations. The question is: **What did we learn that we did not expect?**

The inertia version of this skill summarizes what signals showed. This skill names what contradicted the opening model, traces each contradiction to its source, and identifies what must change and what the change puts at risk.

---

## GATE TOPOLOGY MAP

*Read before entering Stage 1.*

| Token | End Of | Pass Condition | Failure Condition | Effect |
|---|---|---|---|---|
| COMMIT-STAGE-1 | Stage 1 | 3+ beliefs labeled B-#, epistemic profile complete, vulnerable belief named | Missing beliefs or profile | Do not advance |
| COMMIT-STAGE-2 | Stage 2 | Signal inventory complete, no silent dismissals | Any signal dismissed without reason | Do not advance |
| COMMIT-STAGE-3-CLEAN | Stage 3 | All 5 adversarial checks VALID | Any INVALID check | Advance to Stage 4 |
| COMMIT-STAGE-3-FLAGGED | Stage 3 | Foreknowledge detected (Check 3 INVALID) | — | **HALT — do not continue** |
| COMMIT-ENTRY | Stage 4 per-entry | All 4 sub-field ✓ checks pass | Any sub-field fails its check | Apply inline corrective action and re-verify |
| COMMIT-STAGE-4 | Stage 4 | 2+ GATE-CONFIRMED entries | Fewer than 2 | Extend sweep; do not advance |
| COMMIT-STAGE-5 | Stage 5 | Cluster map done, Next Team specific | "Investigate" in Next Team | Do not advance |
| COMMIT-STAGE-6 | Stage 6 | Verdict table done, foreknowledge resolved | Missing verdict or unresolved status | Do not advance |

---

## VOCABULARY

**Valid dimension names (closed set — no others):**

Feasibility · Usability · Scalability · Adoptability · Correctness

**Prohibited terms and canonical replacements:**

| Prohibited | Replace With |
|---|---|
| Reliability | Correctness |
| Performance | Scalability |
| Complexity | Correctness or Feasibility |
| Maintainability | Adoptability |
| Discoverability | Usability or Adoptability |
| Testability | Correctness or Feasibility |

At every EXIT gate: scan all dimension names; correct any prohibited term using this table before emitting the token.

---

## Stage 1 — Opening Model

**ENTER:** No prerequisites.

*Inertia failure mode:* beliefs so vague that no signal could contradict them. Each belief must state a checkable expectation.

Produce:

1. **Epistemic profile:** confidence (HIGH / MEDIUM / LOW); primary dimension (canonical name only).
2. **Belief inventory:** at least 3 beliefs, labeled B-1, B-2, B-3, …. Each: a full sentence, a named dimension, a verifiable claim.
3. **Vulnerable belief:** the B-# you expect the signals to directly contradict.

**EXIT:** Epistemic profile + 3+ labeled beliefs + vulnerable belief recorded. Scan dimension names. Emit **COMMIT-STAGE-1**.

---

## Stage 2 — Signal Inventory

**ENTER:** COMMIT-STAGE-1 emitted.

*Inertia failure mode:* inventorying only supporting signals. Catalog all signals, including potential contradictions.

List every artifact: namespace, name/description, date ("date unknown" if unavailable). No signal dismissed without a written reason.

**EXIT:** All signals cataloged, no silent dismissals. Emit **COMMIT-STAGE-2**.

---

## Stage 3 — Adversarial Gate

**ENTER:** COMMIT-STAGE-2 emitted.

*Inertia failure mode:* advancing to Stage 4 when signals only confirm the model. Check 1 blocks this.

| # | Check | Verdict | Deviation + Corrective Action |
|---|---|---|---|
| 1 | At least one signal contradicts (not merely confirms) a Stage 1 belief | | |
| 2 | All Stage 2 artifacts are named — no "various sources" entries | | |
| 3 | No Stage 1 belief was already-known before signal gathering | | |
| 4 | At least 2 signals can support GATE-CONFIRMED surprises | | |
| 5 | At least one signal addresses a non-primary dimension | | |

**EXIT:**
- All 5 VALID → emit **COMMIT-STAGE-3-CLEAN** → advance to Stage 4.
- Check 3 INVALID → emit **COMMIT-STAGE-3-FLAGGED** → halt; record flagged beliefs; close artifact with FOREKNOWLEDGE-FLAGGED.
- Other INVALID → apply corrective action; re-run table; emit COMMIT-STAGE-3-CLEAN only when all pass.

---

## Stage 4 — Surprise Synthesis

**ENTER:** COMMIT-STAGE-3-CLEAN emitted.

---

### Stage 4 Field Reference

*Read this block before writing any entry. All four field definitions apply to every entry.*

**Surprise**
Names the gap between what a Stage 1 belief predicted and what the signal showed instead. Must reference a specific B-# label. Must state the contradiction or extension explicitly. Not a finding — not what the signal showed; what it showed *instead of what was expected*.

**Signal Source**
The artifact that produced this surprise. Must include name, namespace, and/or date. "Multiple sources" is not acceptable — name the primary artifact.

**Design Impact**
What must change in the design as a result of this surprise. Must name a specific component, API, flow, or decision. Not "the system," not scope-less language.

**Build Risk**
What is implicated by the Design Impact change.

```
Build Risk — three-anchor definition:

  ANCHOR 1 (purpose):
    Names the exposure surface opened by the Design Impact change.
    What the change puts at risk in the existing build.

  ANCHOR 2 (paired formula):
    Design Impact names what must change;
    Build Risk names what is implicated by that change —
    a different component, dependency, or contract that could fail.

  ANCHOR 3 (structural gloss):
    Design Impact is forward-looking: what to update.
    Build Risk is risk-surface: what could break or require rework.
    The two fields name different elements.
    Writing a paraphrase of Design Impact as Build Risk is the
    inertia failure for this sub-field.
```

Build Risk must name a specific component, decision, or risk surface — not a general risk category. "Introduces reliability risk" fails. "The retry policy in the signal delivery contract assumes idempotent receipt" passes.

---

### Surprise 0 — Calibration Entry

*This is a complete worked entry at the required quality standard. Write Surprise 1 and beyond at this standard. Observe: Surprise references B-2 specifically; Signal Source names a real artifact; Design Impact names one component; Build Risk names a different component in a structural relationship to Design Impact — not a paraphrase.*

Surprise: B-2 predicted that /topic:plan would be the sole entry point for creating new topic registrations, enforcing a single creation contract. The topic-scanner signals showed that teams were bypassing /topic:plan and writing registrations directly to the signal bus registry via an undocumented admin endpoint, producing duplicate entries outside the canonical topic contract — B-2's assumption of a single creation entry point was false.

Signal Source: topic-scanner-{topic}-2025-01-22.md (topic namespace)

Design Impact: The /topic:plan skill contract must be extended to include a registry lock that prevents direct-write registration, replacing the current advisory-only enforcement with a hard contract boundary.

Build Risk: The topic deduplication service uses the /topic:plan creation timestamp as the canonical record key — direct-write registrations bypass this timestamp assignment, causing the deduplication service to miss duplicate entries that share a name but lack a plan-assigned key.

COMMIT-ENTRY

---

### Entry Instructions

For each GATE-CONFIRMED surprise:
1. State CONTRADICTS or EXTENDS relative to a specific B-#.
2. Fill in all four sub-fields using the Field Reference above.
3. Run the COMMIT-ENTRY checklist before emitting.

**COMMIT-ENTRY checklist:**

```
✓ Surprise
  PASS:  Full sentence with B-# reference and named expectation-evidence gap
  FAIL:  Rewrite — add B-# reference and state what the signal showed instead
         of what the belief predicted

✓ Signal Source
  PASS:  Named artifact with name, namespace, and/or date
  FAIL:  Replace "multiple sources" or unnamed reference — identify the
         primary artifact and rewrite

✓ Design Impact
  PASS:  Names a specific component, API, flow, or decision
  FAIL:  Remove "the system" or scope-less language — identify the specific
         element that must change and rewrite

✓ Build Risk
  PASS:  Names a specific component, decision, or risk surface (not a category)
  FAIL:  Remove the general category — consult the three-anchor definition,
         identify the specific risk surface opened by the Design Impact change,
         and rewrite
```

All four ✓: emit **COMMIT-ENTRY**. Proceed to next entry.
Any ✗: apply inline corrective action at that bullet; re-verify before emitting.
Extend sweep if fewer than 2 entries pass.

**EXIT:** 2+ GATE-CONFIRMED entries, all COMMIT-ENTRY emitted. Scan dimension names. Emit **COMMIT-STAGE-4**.

---

## Stage 5 — Cluster Map

**ENTER:** COMMIT-STAGE-4 emitted.

*Inertia failure mode:* Next Team / Skill column reads "investigate" — name a specific skill or role.

| Cluster | Surprises Included | Dimension | Next Team / Skill | Priority |
|---|---|---|---|---|

Every surprise in exactly one cluster. Next Team / Skill: at least one named skill (e.g., /flow:resilience) or team role (e.g., "Signal bus engineer").

**EXIT:** All surprises clustered; Next Team populated with at least one specific name. Scan dimension names. Emit **COMMIT-STAGE-5**.

---

## Stage 6 — Symmetric Contract Verdict

**ENTER:** COMMIT-STAGE-5 emitted.

*Inertia failure mode:* marking every belief COHERENT. If Stage 4 produced genuine surprises, at least one belief should be CONTRADICTORY.

Close the symmetric contract from Stage 1:

| Belief | Verdict | Revision Direction |
|---|---|---|
| B-1: [text] | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | [specific update if CONTRADICTORY] |

- **COHERENT** — signals confirmed or did not contradict.
- **CONTRADICTORY** — signals directly contradict. Revision Direction must name a specific design component, spec section, or artifact to update.
- **FOREKNOWLEDGE-FLAGGED** — held as already-known before signals were gathered. Do not emit COMMIT-STAGE-6. Record belief. Close artifact with FOREKNOWLEDGE-FLAGGED.

Explicit foreknowledge resolution: **CLEAR** or **FLAGGED**.

**EXIT:** All beliefs assessed; foreknowledge status explicit. Scan dimension names; correct malformed names using the vocabulary table before emitting. Emit **COMMIT-STAGE-6**.

---

Artifact complete. Write the topic-reflect artifact for {topic}.
