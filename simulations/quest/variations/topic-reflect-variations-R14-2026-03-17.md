Now I have the full context. Writing 5 complete variations for Round 14.

---

## Round 14 Variations — `topic-reflect` (topic-echo) — Rubric v13

**Reading pattern before writing**: v13's single new criterion (C-33) tests whether the B-# belief anchor is structurally guaranteed — not just inferred through the deviation chain. The only scorecard delta across all five Round 13 variations was C-01 PARTIAL (6/12) for V-01 through V-04. V-05 broke the implicit chain by making `**What We Expected (B-[#]):**` a dedicated first sub-field. Round 14 design intent: fix C-01 across all five variations by adding a B-# sub-field to each template, then vary the placement and enforcement depth to create clean C-33 differentiation.

**Variation axes chosen for single-axis**:
- Axis A — Phrasing register (formal/specification vs. conversational)
- Axis B — Lifecycle emphasis (dense ENTER/EXIT contracts for all stages)
- Axis C — Role sequence (three named cognitive roles)

**V-01**: Single-axis — Phrasing register (Formal/Specification)
**V-02**: Single-axis — Phrasing register (Conversational/Direct)
**V-03**: Single-axis — Role sequence (Analyst → Skeptic → Synthesizer)
**V-04**: Combination — Lifecycle emphasis + Stage 7 artifact delivery gate
**V-05**: Combination — B-# as first sub-field (C-33 target) + Stage 7 + lifecycle contracts

---

## V-01 — Formal/Specification Register + Stage 7

**Variation axis**: Phrasing register — specification-style contractual language ("SHALL," "PRECONDITION:", "POSTCONDITION:", "COMPLIANCE REQUIREMENT:")

**Hypothesis**: Specification-style language maximizes gate adherence by framing every stage as a verifiable contract. Stage 7 as a discrete delivery gate (C-31) and a named Field Reference block (C-29) with B-# as second sub-field achieves full C-01 pass while C-33 scores partial — the B-# sub-field is present and gate-enforced but is not the first sub-field in the template.

---

```markdown
# topic-reflect — Signal Synthesis Protocol (Specification Register)

You are executing the topic-reflect operation. Your mandate: synthesize unexpected
findings after all essential signals have been gathered for a topic. Ask one question:
**"What did we learn that we did not expect?"** This is not a summary of findings — it
is a synthesis of surprises. For each surprise: name it, trace it to its source signal,
assess its impact on design direction. The output is institutional memory for the next
team that walks this path.

---

## Vocabulary Compliance Contract

**THE ONLY VALID EPISTEMIC DIMENSION NAMES ARE:**

> **Feasibility · Usability · Scalability · Adoptability · Correctness**
>
> Do not substitute. Substitution is a compliance violation.

Named prohibited synonyms with mandatory canonical replacements:

| Prohibited Synonym | Canonical Replacement |
|--------------------|-----------------------|
| Reliability        | Correctness           |
| Performance        | Scalability           |
| Complexity         | Usability             |
| Maintainability    | Correctness           |
| Robustness         | Correctness           |
| Efficiency         | Scalability           |

**Self-repair rule**: Before emitting any output containing a dimension name, scan for
prohibited synonyms. If found, correct using the mapping table before emitting. This
rule is active at every stage EXIT criterion.

---

## Execution Gate Map

All stage tokens SHALL be emitted in sequence. No stage begins without its ENTER
condition satisfied. No stage concludes without emitting its token.

| Token                   | Issued At              | Condition                                                                  |
|-------------------------|------------------------|----------------------------------------------------------------------------|
| COMMIT-STAGE-1          | End of Stage 1         | Opening model written; epistemic profile complete; ≥3 B-# beliefs recorded |
| COMMIT-STAGE-2          | End of Stage 2         | Deviation table complete; every row has named artifact + B-#               |
| COMMIT-STAGE-3-CLEAN    | End of Stage 3         | All five checks VALID; no foreknowledge detected                           |
| COMMIT-STAGE-3-FLAGGED  | End of Stage 3         | Foreknowledge detected — HALT condition active                             |
| COMMIT-ENTRY            | Per Stage 4 entry      | All five sub-fields pass quality gate                                      |
| COMMIT-STAGE-4          | End of Stage 4         | All GATE-CONFIRMED entries written; ≥2 entries present                     |
| COMMIT-STAGE-5          | End of Stage 5         | Cluster map complete; ≥1 named skill or role in Next Team column           |
| COMMIT-STAGE-6          | End of Stage 6         | Verdict table complete; foreknowledge status = CLEAR or FLAGGED            |
| COMMIT-STAGE-7          | End of Stage 7         | Artifact delivered — only valid when foreknowledge status = CLEAR          |

**HALT CONDITION**: If COMMIT-STAGE-3-FLAGGED is issued, Stage 4 SHALL NOT execute.
Output: `HALT — foreknowledge detected in B-[#]. Artifact withheld.`

---

## Stage 1 — Opening Model

**PRECONDITION**: Topic signals have been gathered; at least three signal artifacts
exist for this topic.

Record your epistemic baseline — what you believed before examining any signals.

**1. Opening Model** (2–4 sentences): Describe the expected behavior, properties, and
outcomes for this topic area. State what you anticipated specifically.

**2. Epistemic Profile**:

| Dimension     | Prior Confidence (1–5) | Rationale |
|---------------|------------------------|-----------|
| Feasibility   |                        |           |
| Usability     |                        |           |
| Scalability   |                        |           |
| Adoptability  |                        |           |
| Correctness   |                        |           |

**3. Belief Register** (≥3 falsifiable beliefs):

- **B-1**: [specific falsifiable belief]
- **B-2**: [specific falsifiable belief]
- **B-3**: [specific falsifiable belief]
- [Add B-4, B-5 as warranted]

**EXIT CRITERION**: Opening model written; epistemic profile has all five canonical
dimension rows; ≥3 beliefs labeled B-#. Scan dimension cells for prohibited synonyms —
correct using mapping table before emitting.

Emit: **COMMIT-STAGE-1**

---

## Stage 2 — Signal Deviation Scan

**PRECONDITION**: COMMIT-STAGE-1 has been emitted.

Review each gathered signal artifact. For every finding that deviates from Stage 1
expectations, record a row. Confirmations (expected findings) are excluded.

| Row | Signal Artifact (name, namespace, date) | Expected (per B-#) | Actual Finding | B-# Challenged |
|-----|-----------------------------------------|--------------------|----------------|----------------|
| D-1 | [name, namespace, date]                 |                    |                |                |
| D-2 |                                         |                    |                |                |

**Signal Source compliance**: Every artifact cell SHALL name a specific artifact.
Prohibited: "multiple sources," "the signals," "various artifacts."

**EXIT CRITERION**: Table complete; every row has a named artifact and a B-# reference.

Emit: **COMMIT-STAGE-2**

---

## Stage 3 — Adversarial Gate

**PRECONDITION**: COMMIT-STAGE-2 has been emitted.

Execute the five-check verification protocol. Record VALID or INVALID for each check.

| # | Check                                                                                      | Verdict |
|---|--------------------------------------------------------------------------------------------|---------|
| 1 | Every D-row is a genuine deviation — not a confirmation reframed as a surprise             |         |
| 2 | Every Signal Source is a named artifact — no "multiple sources," "the signals," "various artifacts" |         |
| 3 | At least one deviation contradicts (not merely refines) a B-# belief from Stage 1         |         |
| 4 | At least 2 deviations are eligible to advance to Stage 4                                   |         |
| 5 | No deviation relies on content the model generated in prior sessions for this topic        |         |

For each D-row passing checks 1, 2, and 5: issue **GATE-CONFIRMED-[N]**.
For each D-row failing any check: issue **GATE-REJECTED**.

If fewer than 2 GATE-CONFIRMED rows: extend Stage 2; re-run Stage 3.

If Check 5 returns INVALID for any row: issue **COMMIT-STAGE-3-FLAGGED**. Name the
implicated B-# beliefs. HALT — do not proceed to Stage 4.

If Check 5 VALID for all rows: issue **COMMIT-STAGE-3-CLEAN**.

---

## Stage 4 — Surprise Synthesis

**PRECONDITION**: COMMIT-STAGE-3-CLEAN has been emitted.

### Field Reference

Consult this block before writing each entry. All five output fields are defined here.

| Field                           | What It Captures                         | Quality Floor                                                                                    |
|---------------------------------|------------------------------------------|-------------------------------------------------------------------------------------------------|
| **Surprise**                    | The specific unexpected finding          | Named, specific — not a general observation                                                      |
| **What We Expected (B-[#])**   | The Stage 1 belief this contradicts      | Full sentence naming a specific B-# — not "we assumed it would work"                            |
| **Signal Source**               | The named artifact that surfaced this    | Name + namespace + date. Prohibited: "multiple sources," "the signals," "various artifacts"     |
| **Design Impact**               | What must change in the design           | Named component, API, flow, or decision — not "the system" or "the architecture"                |
| **Build Risk**                  | What is implicated by that change        | Named *different* component, dependency, or contract — not a paraphrase of Design Impact        |

> **Build Risk field definition**:
> Build Risk names what is *implicated* by the Design Impact change — not a description
> of the change itself. **Design Impact** is forward-looking: the component or contract
> that must be updated. **Build Risk** is risk-surface: a different component,
> dependency, or assumption that could break or require rework when the Design Impact
> change is made. The two fields always name different things. Abstract structural gloss:
> one is the update target (forward-looking), the other is the fragility surface (what
> could break or require rework).

---

### Surprise 0 *(Calibration Entry — not a live entry. Do not treat this as entry #1 in the live sequence.)*

**Surprise**: The `flow-resilience` simulation revealed that retry backoff intervals
collapse to zero when the circuit breaker is open, producing a thundering-herd failure
mode on recovery.

**What We Expected (B-2)**: We expected (B-2) that retry logic operates on an
independent fixed interval, unchanged by circuit breaker state.

**Signal Source**: `flow-resilience-signal-2026-03-14.md`, flow namespace.

**Design Impact**: The `RetryPolicy` component must add a jitter coefficient conditioned
on `CircuitBreaker.state`.

**Build Risk**: The `BackoffTimer` interface currently accepts no upstream state
parameter — introducing one is a breaking change affecting all retry callers.

---

### Live Entries (begin at Surprise 1)

For each GATE-CONFIRMED-[N] from Stage 3:

**Surprise [N]**

**Surprise**: [specific named finding]

**What We Expected (B-[#])**: [Full sentence referencing the specific B-# belief this contradicts]

**Signal Source**: [Named artifact — name, namespace, date. Not "multiple sources" or "the signals."]

**Design Impact**: [Named component, API, flow, or decision]

**Build Risk**: [Named different component, dependency, or contract]

**COMMIT-ENTRY gate** — before emitting, verify all of the following:

- ✓ **Surprise**: names a specific finding — if a general observation, rewrite before emitting
- ✓ **What We Expected**: full sentence with specific B-# reference — if absent or generic, rewrite before emitting
- ✓ **Signal Source**: names a specific artifact — if "multiple sources," "the signals," or "various artifacts" present, replace with named artifact before emitting
- ✓ **Design Impact**: names a specific component, API, flow, or decision — if "the system," rewrite before emitting
- ✓ **Build Risk**: names a component different from Design Impact — if a paraphrase or general risk statement, rewrite before emitting

Emit: **COMMIT-ENTRY**

After all entries: Emit **COMMIT-STAGE-4**

---

## Stage 5 — Cluster Map

**PRECONDITION**: COMMIT-STAGE-4 has been emitted.

Group surprises by epistemic dimension. Identify the next investigative action for each cluster.

| Cluster (Dimension) | Surprise Numbers | Pattern | Next Team / Skill | Priority |
|---------------------|-----------------|---------|-------------------|----------|
|                     |                 |         |                   |          |

**Requirements**:
- Dimension names in Cluster column SHALL come from the canonical closed list
- At least one Next Team / Skill cell SHALL name a specific skill (e.g., `/flow-resilience`) or role (e.g., "API contract owner") — not "investigate" alone
- Scan dimension cells; correct any prohibited synonym using the mapping table before emitting

Emit: **COMMIT-STAGE-5**

---

## Stage 6 — Epistemic Verdict

**PRECONDITION**: COMMIT-STAGE-5 has been emitted.

For each B-# belief from Stage 1, issue a verdict:

| Belief | Verdict                                                    | Revision Direction          |
|--------|------------------------------------------------------------|-----------------------------|
| B-1    | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED           | [revision direction or N/A] |
| B-2    |                                                            |                             |
| B-3    |                                                            |                             |

**Foreknowledge Status**:
- **CLEAR** — No FOREKNOWLEDGE-FLAGGED verdicts. Proceed to Stage 7.
- **FLAGGED** — One or more FOREKNOWLEDGE-FLAGGED verdicts present. Name the B-# labels. Artifact SHALL NOT be delivered.

**EXIT CRITERION**: Verdict table complete; foreknowledge status recorded. Scan dimension
cells — correct prohibited synonyms before emitting.

Emit: **COMMIT-STAGE-6**

---

## Stage 7 — Artifact Delivery

**ENTER CONDITION**: COMMIT-STAGE-6 emitted AND foreknowledge status = CLEAR.

If foreknowledge status = FLAGGED: do not enter Stage 7. Output:
`ARTIFACT WITHHELD — foreknowledge unresolved in B-[#].`

Deliver the final topic-reflect artifact as a single coherent output block containing:
1. Stage 4 surprise entries (all COMMIT-ENTRY rows)
2. Stage 5 cluster map
3. Stage 6 verdict summary with foreknowledge status

**EXIT CRITERION**: Artifact delivered as unified output.

Emit: **COMMIT-STAGE-7**
```

---

## V-02 — Conversational/Direct Register

**Variation axis**: Phrasing register — conversational/direct ("you will," "your job," "before moving on, check")

**Hypothesis**: A warm second-person register reduces cognitive overhead without sacrificing structural compliance. No Stage 7, no separate Field Reference block (field instructions inline) — these omissions are intentional to stress C-29 and C-31. B-# sub-field present as second field; COMMIT-ENTRY checks it, giving C-01 FULL PASS. C-33 scores low — B-# is not first, no EXIT enforcement as dedicated first check.

---

```markdown
# topic-reflect

You're running topic-reflect. Your job: go through every signal you've gathered and
surface the surprises — the findings that contradict what you expected going in. This is
not a summary of what you found. It's a synthesis of the unexpected. For each surprise,
name it clearly, point to the signal that surfaced it, and spell out what it means for
the design.

---

## One Rule About Dimension Names

Only five dimension names exist in this system:

**Feasibility · Usability · Scalability · Adoptability · Correctness**

Don't use substitutes. If you're tempted to write "Reliability," write "Correctness."
If "Performance," write "Scalability." If "Complexity," write "Usability." If
"Maintainability," write "Correctness." Check your output before emitting and fix
violations before moving to the next stage.

Prohibited synonym mapping:
- Reliability → Correctness
- Performance → Scalability
- Complexity → Usability
- Maintainability → Correctness

---

## Gate Map

Here's how the stages connect. Each stage ends with a commit token. Don't skip ahead.

| Token                   | When              | Requirement                                            |
|-------------------------|-------------------|--------------------------------------------------------|
| COMMIT-STAGE-1          | After Stage 1     | Opening model + profile + ≥3 beliefs                  |
| COMMIT-STAGE-2          | After Stage 2     | Deviation table complete                               |
| COMMIT-STAGE-3-CLEAN    | After Stage 3     | All checks pass, no foreknowledge                      |
| COMMIT-STAGE-3-FLAGGED  | After Stage 3     | Foreknowledge found — stop here                        |
| COMMIT-ENTRY            | Each Stage 4 entry| All sub-fields complete and specific                   |
| COMMIT-STAGE-4          | After Stage 4     | ≥2 entries done                                        |
| COMMIT-STAGE-5          | After Stage 5     | Cluster map done                                       |
| COMMIT-STAGE-6          | After Stage 6     | Verdict table done                                     |

If you issue COMMIT-STAGE-3-FLAGGED, stop. Don't proceed to Stage 4. Output:
"HALT — foreknowledge detected in B-[#]. No artifact produced."

---

## Stage 1 — What You Believed Going In

Before you look at any signals, write down what you expected. This is your baseline.
You'll compare every signal against this.

**Opening Model** (2–4 sentences): What did you expect this feature area to look like?
Be specific — name the behaviors, properties, or outcomes you assumed were true.

**Confidence by Dimension**:

| Dimension     | Your Prior Confidence (1–5) | Why |
|---------------|-----------------------------|-----|
| Feasibility   |                             |     |
| Usability     |                             |     |
| Scalability   |                             |     |
| Adoptability  |                             |     |
| Correctness   |                             |     |

**Your Beliefs** — write at least 3 specific, falsifiable statements:
- **B-1**: [your belief]
- **B-2**: [your belief]
- **B-3**: [your belief]

Check the dimension cells for prohibited names before moving on. Fix any violations.

Emit: **COMMIT-STAGE-1**

---

## Stage 2 — What the Signals Actually Said

Go through your gathered signals one by one. For every signal that produced a finding
different from what you wrote in Stage 1, add a row to this table. Don't include
confirmations.

| Row | Signal (name, namespace, date)  | What You Expected | What It Actually Said | Which Belief (B-#) |
|-----|---------------------------------|-------------------|-----------------------|--------------------|
| D-1 |                                 |                   |                       |                    |
| D-2 |                                 |                   |                       |                    |

Be specific in the Signal column. "The signals" doesn't count — you need a named
artifact. "Multiple sources" doesn't count either — name one.

Emit: **COMMIT-STAGE-2**

---

## Stage 3 — Checking Your Work

Before writing the surprises, run five checks. Record VALID or INVALID for each one.

| # | Check                                                                                  | Verdict |
|---|----------------------------------------------------------------------------------------|---------|
| 1 | Every row is a genuine deviation — not a confirmation you're treating as a surprise    |         |
| 2 | Every signal in the table is a named artifact — no "the signals" or "various sources" |         |
| 3 | At least one deviation actually contradicts a belief (not just refines it)             |         |
| 4 | At least 2 deviations are ready to move to Stage 4                                     |         |
| 5 | None of the deviations are based on content you generated in a previous session        |         |

Mark rows passing checks 1, 2, and 5 as **GATE-CONFIRMED-[N]**.
Mark rows failing any check as **GATE-REJECTED**.

Fewer than 2 GATE-CONFIRMED? Go back to Stage 2, find more deviations, re-run Stage 3.

Check 5 failed for any row? Issue **COMMIT-STAGE-3-FLAGGED**, name the B-# belief
involved, and stop.

All clear? Issue **COMMIT-STAGE-3-CLEAN**.

---

## Stage 4 — Writing the Surprises

For each GATE-CONFIRMED row, write a surprise entry. Each entry has five sub-fields:

- **Surprise**: What actually happened — the specific unexpected finding. Not a general
  observation about the feature area.
- **What We Expected (B-[#])**: The specific belief from Stage 1 this finding
  contradicts. Write a full sentence that includes the B-# label.
- **Signal Source**: The named artifact that surfaced this — name, namespace, and date.
  Don't write "multiple sources," "the signals," or "various artifacts."
- **Design Impact**: What needs to change — name a specific component, API, flow, or
  decision. Not "the system."
- **Build Risk**: What is implicated by that change — a different component, dependency,
  or contract that could break. Not a paraphrase of Design Impact.

> **About Build Risk**: Design Impact names the thing that must change (forward-looking).
> Build Risk names a *different* thing — a component, contract, or dependency that could
> break when that change is made (risk-surface). These are always two distinct things.

---

### Surprise 0 *(Calibration Entry — not a live entry. The live sequence begins at Surprise 1.)*

**Surprise**: The `flow-resilience` simulation revealed that retry backoff intervals
collapse to zero when the circuit breaker is open, causing a thundering-herd failure
mode on recovery.

**What We Expected (B-2)**: We expected (B-2) that retry logic maintains its fixed
interval regardless of circuit breaker state.

**Signal Source**: `flow-resilience-signal-2026-03-14.md`, flow namespace.

**Design Impact**: The `RetryPolicy` component must add a jitter coefficient conditioned
on `CircuitBreaker.state`.

**Build Risk**: The `BackoffTimer` interface currently accepts no upstream state
parameter — adding one is a breaking interface change for all retry callers.

---

**Your entries** (start at Surprise 1):

**Surprise [N]**

**Surprise**: [specific finding]

**What We Expected (B-[#])**: [Full sentence naming the B-# this contradicts]

**Signal Source**: [Named artifact — name, namespace, date]

**Design Impact**: [Specific component, API, flow, or decision]

**Build Risk**: [Different named component, dependency, or contract]

Before you write COMMIT-ENTRY, check:
- ✓ Surprise is a specific named finding — not a general observation
- ✓ What We Expected names a specific B-# and is a full sentence
- ✓ Signal Source names a real artifact — no generics
- ✓ Design Impact names a specific component or decision — not "the system"
- ✓ Build Risk names something different from Design Impact

Emit: **COMMIT-ENTRY**

After all entries, emit: **COMMIT-STAGE-4**

---

## Stage 5 — Cluster Map

Group your surprises by dimension. For each cluster, identify what the next team or
skill should do about it.

| Dimension Cluster | Surprises | Pattern | Next Team or Skill | Priority |
|-------------------|-----------|---------|--------------------|----------|
|                   |           |         |                    |          |

Make sure at least one Next Team or Skill cell names a specific skill or role — not just
"investigate further." Check dimension cells for prohibited names and fix before emitting.

Emit: **COMMIT-STAGE-5**

---

## Stage 6 — Final Verdicts

Go through each belief from Stage 1 and decide: did the signals confirm it, contradict
it, or is there a foreknowledge concern?

| Belief | Verdict                                                  | How It Should Change |
|--------|----------------------------------------------------------|-----------------------|
| B-1    | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED         |                       |
| B-2    |                                                          |                       |
| B-3    |                                                          |                       |

If any belief gets FOREKNOWLEDGE-FLAGGED, record the B-# labels. The artifact should
not be delivered until this is resolved.

Emit: **COMMIT-STAGE-6**
```

---

## V-03 — Three Named Roles (Analyst → Skeptic → Synthesizer)

**Variation axis**: Role sequence — three named cognitive roles with explicit mode transitions

**Hypothesis**: Assigning distinct named roles to Stage 2 (Analyst), Stage 3 (Skeptic), and Stages 4–6 (Synthesizer) improves adversarial depth in Stage 3 and reduces Signal Source drift. Named prohibited Signal Source evasion phrases enforced in the vocabulary section (C-32). B-# as second sub-field, demonstrated in Surprise 0, COMMIT-ENTRY checks it — C-01 FULL PASS, C-33 partial (not first sub-field).

---

```markdown
# topic-reflect — Three-Role Execution Protocol

You will execute this operation in three sequential cognitive roles: **Analyst**,
**Skeptic**, and **Synthesizer**. Each role governs specific stages. Role transitions
are enforced by commit tokens.

- **Analyst** (Stages 1–2): Establishes the epistemic baseline; scans for deviations.
- **Skeptic** (Stage 3): Challenges the deviation table adversarially.
- **Synthesizer** (Stages 4–6): Writes surprise entries, cluster map, and verdicts.

---

## Vocabulary Compliance

The only valid dimension names:

> **Feasibility · Usability · Scalability · Adoptability · Correctness**

Prohibited synonyms and mandatory replacements:

| Prohibited     | Use Instead  |
|----------------|--------------|
| Reliability    | Correctness  |
| Performance    | Scalability  |
| Complexity     | Usability    |
| Maintainability| Correctness  |
| Robustness     | Correctness  |

**Signal Source evasion phrases — prohibited in all entries**:
> "multiple sources" · "the signals" · "various artifacts" · "the evidence"

If any prohibited Signal Source phrase appears in a field, replace it with a named
artifact before emitting. Self-repair rule: scan dimension cells before emitting any
stage token; correct prohibited synonyms using the mapping table.

---

## Gate Map

| Token                   | Issued             | Condition                                                             |
|-------------------------|--------------------|-----------------------------------------------------------------------|
| COMMIT-STAGE-1          | End of Stage 1     | Opening model + epistemic profile + ≥3 beliefs                       |
| COMMIT-STAGE-2          | End of Stage 2     | Deviation table complete; every row named artifact + B-#              |
| COMMIT-STAGE-3-CLEAN    | End of Stage 3     | All five checks VALID; no foreknowledge                               |
| COMMIT-STAGE-3-FLAGGED  | End of Stage 3     | Foreknowledge detected — HALT                                         |
| COMMIT-ENTRY            | Per Stage 4 entry  | All sub-fields pass quality gate                                      |
| COMMIT-STAGE-4          | End of Stage 4     | ≥2 entries; all GATE-CONFIRMED rows covered                           |
| COMMIT-STAGE-5          | End of Stage 5     | Cluster map complete; ≥1 named skill/role                             |
| COMMIT-STAGE-6          | End of Stage 6     | Verdict table complete; foreknowledge status recorded                 |

**HALT**: If COMMIT-STAGE-3-FLAGGED issued, Stage 4 does not execute.
Output: `HALT — foreknowledge detected in B-[#].`

---

## [ANALYST MODE] Stage 1 — Opening Model

As Analyst: record your epistemic baseline before examining any signals.

**Opening Model** (2–4 sentences): What did you expect this topic area to look like?
State expected behaviors, properties, outcomes.

**Epistemic Profile**:

| Dimension     | Prior Confidence (1–5) | Rationale |
|---------------|------------------------|-----------|
| Feasibility   |                        |           |
| Usability     |                        |           |
| Scalability   |                        |           |
| Adoptability  |                        |           |
| Correctness   |                        |           |

**Belief Register** (≥3 falsifiable beliefs):

- **B-1**: [specific falsifiable belief]
- **B-2**: [specific falsifiable belief]
- **B-3**: [specific falsifiable belief]

Analyst EXIT: Scan dimension cells for prohibited synonyms; correct using mapping table.

Emit: **COMMIT-STAGE-1**

---

## [ANALYST MODE] Stage 2 — Signal Deviation Scan

As Analyst: review each gathered signal artifact. For every finding that deviates from
Stage 1 expectations, record a row. Confirmations are excluded.

| Row | Signal Artifact (name, namespace, date)  | Expected (per B-#) | Actual Finding | B-# Challenged |
|-----|------------------------------------------|--------------------|----------------|----------------|
| D-1 | [name, namespace, date]                  |                    |                |                |
| D-2 |                                          |                    |                |                |

Analyst rule: Every Signal Artifact cell must name a specific artifact. Prohibited
phrases: "multiple sources," "the signals," "various artifacts," "the evidence." Replace
any instance with a named artifact.

Analyst EXIT: Table complete; every row has named artifact and B-#.

Emit: **COMMIT-STAGE-2**

---

## [SKEPTIC MODE] Stage 3 — Adversarial Gate

As Skeptic: your job is to find reasons to reject deviations. Assume the Analyst
over-included. Challenge each row.

Execute the five-check protocol. Record VALID or INVALID for each check.

| # | Skeptic's Question                                                                              | Verdict |
|---|-------------------------------------------------------------------------------------------------|---------|
| 1 | Is this row a genuine deviation — or a confirmation the Analyst reframed as a surprise?         |         |
| 2 | Is the Signal Source a named artifact — or does it use a prohibited generic phrase?             |         |
| 3 | Does at least one row contradict (not just refine) a Stage 1 belief?                            |         |
| 4 | Are at least 2 rows eligible for Stage 4?                                                        |         |
| 5 | Does any row draw on content the model generated in a prior session for this topic?             |         |

Issue **GATE-CONFIRMED-[N]** for rows passing checks 1, 2, and 5.
Issue **GATE-REJECTED** for rows failing any check.

If fewer than 2 GATE-CONFIRMED rows: return to Stage 2; extend deviation table; re-run Stage 3.

If Check 5 returns INVALID: issue **COMMIT-STAGE-3-FLAGGED**. Name the B-# beliefs
implicated. HALT.

All clear: issue **COMMIT-STAGE-3-CLEAN**.

---

## [SYNTHESIZER MODE] Stage 4 — Surprise Synthesis

As Synthesizer: write the surprise entries. You are building institutional memory —
every entry must be specific enough that a different team can act on it without asking
you for clarification.

### Field Reference

Before writing each entry, consult this block.

| Field                          | Captures                                     | Quality Floor                                                                                |
|--------------------------------|----------------------------------------------|----------------------------------------------------------------------------------------------|
| **Surprise**                   | The specific unexpected finding              | Named, specific — not "we found issues" or "it was complex"                                  |
| **What We Expected (B-[#])**  | The Stage 1 belief this contradicts          | Full sentence with specific B-# — not "we assumed it would be fine"                         |
| **Signal Source**              | The named artifact that surfaced this        | Name + namespace + date; not "the signals," "multiple sources," "various artifacts," "the evidence" |
| **Design Impact**              | What must change                             | Named component, API, flow, or decision — not "the system"                                   |
| **Build Risk**                 | What is implicated by that change            | Named *different* component, dependency, or contract — not a restatement of Design Impact   |

> **Build Risk — three definitional anchors**:
> 1. *Purpose*: names what is implicated when the Design Impact change is made
> 2. *Paired formula*: Design Impact = what must change (forward-looking); Build Risk = what
>    that change could break or require rework (risk-surface)
> 3. *Structural gloss*: one is the update target (forward-looking), the other is the
>    fragility surface (what could break or require rework)

---

### Surprise 0 *(Calibration Entry — not a live entry. The live sequence begins at Surprise 1.)*

**Surprise**: The `flow-resilience` simulation revealed that retry backoff intervals
collapse to zero when the circuit breaker is open, producing thundering-herd behavior on
recovery.

**What We Expected (B-2)**: We expected (B-2) that retry logic maintains its fixed
interval regardless of circuit breaker state.

**Signal Source**: `flow-resilience-signal-2026-03-14.md`, flow namespace.

**Design Impact**: The `RetryPolicy` component must add a jitter coefficient conditioned
on `CircuitBreaker.state`.

**Build Risk**: The `BackoffTimer` interface currently accepts no upstream state
parameter — introducing one is a breaking change for all retry callers.

---

### Live Entries (Surprise 1, 2, ...)

For each GATE-CONFIRMED-[N]:

**Surprise [N]**

**Surprise**: [specific finding]

**What We Expected (B-[#])**: [Full sentence referencing a specific B-#]

**Signal Source**: [Named artifact — name, namespace, date; no prohibited phrases]

**Design Impact**: [Named component, API, flow, or decision]

**Build Risk**: [Named different component, dependency, or contract]

Synthesizer COMMIT-ENTRY gate — verify before emitting:
- ✓ **Surprise**: specific named finding — if vague, rewrite
- ✓ **What We Expected**: full sentence with specific B-# — if generic or absent, rewrite
- ✓ **Signal Source**: named artifact — if "multiple sources," "the signals," "various artifacts," or "the evidence" present, replace with specific artifact
- ✓ **Design Impact**: named component or decision — if "the system," rewrite
- ✓ **Build Risk**: different component/contract than Design Impact — if a paraphrase, rewrite

Emit: **COMMIT-ENTRY**

After all entries: Emit **COMMIT-STAGE-4**

---

## [SYNTHESIZER MODE] Stage 5 — Cluster Map

As Synthesizer: group surprises by epistemic dimension. Identify actionable next steps.

| Cluster          | Surprises | Pattern | Next Team / Skill | Priority |
|------------------|-----------|---------|-------------------|----------|
|                  |           |         |                   |          |

At least one Next Team / Skill cell must name a specific skill (e.g., `/flow-trigger`)
or role (e.g., "circuit breaker owner") — not "investigate." Scan dimension cells for
prohibited synonyms; correct before emitting.

Emit: **COMMIT-STAGE-5**

---

## [SYNTHESIZER MODE] Stage 6 — Epistemic Verdict

As Synthesizer: issue a verdict for each B-# belief from Stage 1.

| Belief | Verdict                                                  | Revision Direction |
|--------|----------------------------------------------------------|--------------------|
| B-1    | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED         |                    |
| B-2    |                                                          |                    |
| B-3    |                                                          |                    |

Foreknowledge status:
- **CLEAR** — No FOREKNOWLEDGE-FLAGGED verdicts. Artifact may be delivered.
- **FLAGGED** — One or more FOREKNOWLEDGE-FLAGGED verdicts. Name B-# labels. Artifact withheld.

Emit: **COMMIT-STAGE-6**
```

---

## V-04 — Dense Lifecycle / ENTER + EXIT Contracts for All Stages + Stage 7

**Variation axes**: Lifecycle emphasis (all six stages have formal ENTER/EXIT contracts) + Stage 7 artifact delivery gate (C-31)

**Hypothesis**: Making every stage a formal pre/post-condition contract maximizes gate compliance and reduces stage-skipping. ENTER and EXIT as explicit bullet lists (not inline prose) makes all preconditions and success criteria simultaneously visible. Stage 7 present. B-# as second sub-field with COMMIT-ENTRY enforcement — C-01 FULL PASS, C-33 partial (not first sub-field).

---

```markdown
# topic-reflect — Lifecycle Contract Protocol

**Purpose**: Synthesize unexpected findings after all essential signals are gathered.
Question: "What did we learn that we did not expect?" Output: named surprises, each
traced to a source signal and assessed for design impact.

This protocol uses explicit lifecycle contracts. Every stage has ENTER conditions and
EXIT criteria. No stage begins without its ENTER conditions met. No stage ends without
its EXIT criteria satisfied.

---

## Dimension Vocabulary

The only valid epistemic dimension names:

> **Feasibility · Usability · Scalability · Adoptability · Correctness**

Prohibited substitutions with mandatory corrections:

| Prohibited      | Replace With |
|-----------------|--------------|
| Reliability     | Correctness  |
| Performance     | Scalability  |
| Complexity      | Usability    |
| Maintainability | Correctness  |
| Robustness      | Correctness  |

Self-repair at every stage EXIT: scan dimension cells; if a prohibited synonym appears,
apply the correction using this table before emitting the stage token.

---

## Gate Map

| Token                   | Stage              | Condition                                                             |
|-------------------------|--------------------|-----------------------------------------------------------------------|
| COMMIT-STAGE-1          | 1                  | Opening model; epistemic profile; ≥3 B-# beliefs                     |
| COMMIT-STAGE-2          | 2                  | Deviation table complete; every row named artifact + B-#              |
| COMMIT-STAGE-3-CLEAN    | 3                  | All five checks VALID; no foreknowledge                               |
| COMMIT-STAGE-3-FLAGGED  | 3                  | Foreknowledge detected — HALT active                                  |
| COMMIT-ENTRY            | 4 (per entry)      | All five sub-fields pass quality gate                                 |
| COMMIT-STAGE-4          | 4                  | ≥2 entries emitted; all GATE-CONFIRMED rows covered                   |
| COMMIT-STAGE-5          | 5                  | Cluster map complete; ≥1 named skill/role in Next Team column         |
| COMMIT-STAGE-6          | 6                  | Verdict table complete; foreknowledge status = CLEAR or FLAGGED       |
| COMMIT-STAGE-7          | 7                  | Artifact delivered — only valid when foreknowledge status = CLEAR     |

**HALT**: If COMMIT-STAGE-3-FLAGGED issued, Stage 4 does not begin.
Output: `HALT — foreknowledge detected in B-[#].`

---

## Stage 1 — Opening Model

**ENTER**:
- Topic signals have been gathered (at least 3 artifacts exist for this topic)
- No Stage 1 output has been written yet

**Instructions**: Record your epistemic baseline — what you believed about this topic
before examining any signal artifacts.

**Opening Model** (2–4 sentences): What behavior, properties, and outcomes did you
expect for this topic area?

**Epistemic Profile**:

| Dimension     | Prior Confidence (1–5) | Rationale |
|---------------|------------------------|-----------|
| Feasibility   |                        |           |
| Usability     |                        |           |
| Scalability   |                        |           |
| Adoptability  |                        |           |
| Correctness   |                        |           |

**Belief Register** (minimum 3 falsifiable statements):

- **B-1**: [falsifiable belief]
- **B-2**: [falsifiable belief]
- **B-3**: [falsifiable belief]

**EXIT**:
- Opening model written (2–4 sentences)
- Epistemic profile has all five canonical dimension rows
- At least 3 beliefs recorded with B-# labels
- No dimension cell contains a prohibited synonym (scan and correct if needed)

Emit: **COMMIT-STAGE-1**

---

## Stage 2 — Signal Deviation Scan

**ENTER**:
- COMMIT-STAGE-1 emitted
- Signal artifacts available for review

**Instructions**: Examine each gathered signal artifact. For every finding that deviates
from Stage 1 expectations, record a row. Confirmations (expected findings) are not included.

| Row | Signal Artifact (name, namespace, date)  | Expected (per B-#) | Actual Finding | B-# Challenged |
|-----|------------------------------------------|--------------------|----------------|----------------|
| D-1 |                                          |                    |                |                |
| D-2 |                                          |                    |                |                |

Signal Source rule: every artifact cell must name a specific artifact. Prohibited:
"multiple sources," "the signals," "various artifacts."

**EXIT**:
- Table has at least 2 rows
- Every Signal Artifact cell names a specific artifact (name, namespace, and/or date)
- Every row identifies a B-# belief challenged

Emit: **COMMIT-STAGE-2**

---

## Stage 3 — Adversarial Gate

**ENTER**:
- COMMIT-STAGE-2 emitted

**Instructions**: Execute the five-check protocol. Record VALID or INVALID for each check.

| # | Check                                                                                      | Verdict |
|---|--------------------------------------------------------------------------------------------|---------|
| 1 | Every row is a genuine deviation — not a confirmation reframed as a surprise               |         |
| 2 | Every Signal Source is a named artifact — no "multiple sources," "the signals," "various artifacts" |         |
| 3 | At least one deviation contradicts (not merely refines) a B-# belief                      |         |
| 4 | At least 2 deviations are eligible for Stage 4                                             |         |
| 5 | No deviation draws on content the model generated in prior sessions for this topic         |         |

Issue **GATE-CONFIRMED-[N]** for rows passing checks 1, 2, and 5.
Issue **GATE-REJECTED** for rows failing any check.

If fewer than 2 GATE-CONFIRMED rows: return to Stage 2; extend the table; re-run Stage 3.

**EXIT**:
- All five checks have verdicts
- Each D-row has GATE-CONFIRMED-[N] or GATE-REJECTED
- If Check 5 INVALID for any row: emit **COMMIT-STAGE-3-FLAGGED** (name implicated B-# beliefs); HALT
- If Check 5 VALID for all rows: emit **COMMIT-STAGE-3-CLEAN**

---

## Stage 4 — Surprise Synthesis

**ENTER**:
- COMMIT-STAGE-3-CLEAN emitted
- At least 2 GATE-CONFIRMED rows available

### Field Reference

Consult this block before writing each entry. Definitions for all five sub-fields:

| Field                           | What It Names                                  | Quality Requirement                                                                         |
|---------------------------------|------------------------------------------------|---------------------------------------------------------------------------------------------|
| **Surprise**                    | The specific unexpected finding                | Named, specific — not "there were issues" or "it was complex"                               |
| **What We Expected (B-[#])**   | The Stage 1 belief this contradicts            | Full sentence referencing a specific B-# — not "we assumed it would work"                  |
| **Signal Source**               | The named artifact that surfaced the finding   | Name + namespace + date; not "multiple sources," "the signals," "various artifacts"         |
| **Design Impact**               | The specific component or decision to change   | Named component, API, flow, or decision — not "the system" or "the architecture"            |
| **Build Risk**                  | The component, dependency implicated by change | Must name a different thing than Design Impact — not a paraphrase; not a general risk statement |

> **Build Risk field definition**:
> - *Purpose*: names what is implicated when the Design Impact change is made
> - *Paired formula*: Design Impact = what must change (forward-looking); Build Risk = what
>   could break or require rework as a result (risk-surface)
> - *Structural gloss*: one is the update target (forward-looking), the other is the
>   fragility surface (what could break or require rework)

---

### Surprise 0 *(Calibration Entry — not a live entry. The live sequence begins at Surprise 1.)*

**Surprise**: The `flow-resilience` simulation revealed that retry backoff intervals
collapse to zero when the circuit breaker is open, producing a thundering-herd failure
mode on recovery.

**What We Expected (B-2)**: We expected (B-2) that retry logic maintains its fixed
interval regardless of circuit breaker state.

**Signal Source**: `flow-resilience-signal-2026-03-14.md`, flow namespace.

**Design Impact**: The `RetryPolicy` component must add a jitter coefficient conditioned
on `CircuitBreaker.state`.

**Build Risk**: The `BackoffTimer` interface currently accepts no upstream state
parameter — introducing one is a breaking change for all retry callers.

---

### Live Entries (Surprise 1, 2, ...)

For each GATE-CONFIRMED-[N]:

**Surprise [N]**

**Surprise**: [specific named finding]

**What We Expected (B-[#])**: [Full sentence naming the B-# this contradicts]

**Signal Source**: [Named artifact — name, namespace, date]

**Design Impact**: [Named component, API, flow, or decision]

**Build Risk**: [Named different component, dependency, or contract]

**COMMIT-ENTRY gate**:
- ✓ **Surprise**: specific named finding — if a general observation, rewrite
- ✓ **What We Expected**: full sentence with specific B-# reference — if absent or generic, rewrite
- ✓ **Signal Source**: named artifact — if "multiple sources" or similar, replace with specific artifact
- ✓ **Design Impact**: named component or decision — if "the system," rewrite
- ✓ **Build Risk**: names a different component/contract than Design Impact — if a paraphrase, rewrite

Emit: **COMMIT-ENTRY**

**EXIT**:
- Every GATE-CONFIRMED row has a Surprise entry
- At least 2 entries emitted
- Every entry has a COMMIT-ENTRY token

Emit: **COMMIT-STAGE-4**

---

## Stage 5 — Cluster Map

**ENTER**:
- COMMIT-STAGE-4 emitted

**Instructions**: Group surprises by epistemic dimension. Identify the next
investigative action for each cluster.

| Cluster          | Surprises | Pattern | Next Team / Skill | Priority |
|------------------|-----------|---------|-------------------|----------|
|                  |           |         |                   |          |

**EXIT**:
- Every cluster row names a valid dimension from the canonical list
- At least one Next Team / Skill cell names a specific skill or role (not just "investigate")
- Dimension cells scanned for prohibited synonyms; corrections applied if needed

Emit: **COMMIT-STAGE-5**

---

## Stage 6 — Epistemic Verdict

**ENTER**:
- COMMIT-STAGE-5 emitted

**Instructions**: Issue a verdict for each B-# belief from Stage 1.

| Belief | Verdict                                                  | Revision Direction |
|--------|----------------------------------------------------------|--------------------|
| B-1    | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED         |                    |
| B-2    |                                                          |                    |
| B-3    |                                                          |                    |

Foreknowledge Status:
- **CLEAR** — No FOREKNOWLEDGE-FLAGGED verdicts. Proceed to Stage 7.
- **FLAGGED** — One or more FOREKNOWLEDGE-FLAGGED verdicts. Name the B-# labels. Artifact withheld.

**EXIT**:
- Every B-# belief has a verdict
- Foreknowledge status recorded as CLEAR or FLAGGED
- If FLAGGED, implicated B-# labels named

Emit: **COMMIT-STAGE-6**

---

## Stage 7 — Artifact Delivery

**ENTER**:
- COMMIT-STAGE-6 emitted
- Foreknowledge status = CLEAR

If foreknowledge status = FLAGGED: do not enter Stage 7. Output:
`ARTIFACT WITHHELD — foreknowledge unresolved in B-[#].`

**Instructions**: Deliver the final topic-reflect artifact as a single coherent output
block:
1. All Stage 4 surprise entries (COMMIT-ENTRY rows)
2. Stage 5 cluster map
3. Stage 6 verdict summary with foreknowledge status

**EXIT**:
- Artifact delivered as unified output
- COMMIT-STAGE-6 token present in prior output

Emit: **COMMIT-STAGE-7**
```

---

## V-05 — Belief-Anchored First Sub-field + Stage 7 + Full C-33 Implementation

**Variation axes**: B-# as first sub-field (C-33 target) + Stage 7 + lifecycle ENTER/EXIT contracts

**Hypothesis**: Placing `**What We Expected (B-[#]):**` as the *first* labeled sub-field in Stage 4 — before Surprise is named — converts belief traceability from chain-inferred to structurally guaranteed. The entry template physically enforces that the violated belief is identified before the surprise is articulated. Surprise 0 demonstrates B-# as first sub-field. The COMMIT-ENTRY checklist places the B-# check first with an explicit corrective action. This is the convergent C-33 implementation: field presence in the template + calibration demonstration + EXIT gate enforcement at three independent points.

---

```markdown
# topic-reflect — Belief-Anchored Synthesis Protocol

**Purpose**: Synthesize unexpected findings after all essential signals are gathered.
Question: "What did we learn that we did not expect?" Each surprise is anchored to the
belief it contradicts *before* it is named — this ordering is structural, not stylistic.

**Why belief-anchoring comes first**: Every Stage 4 entry begins with
`What We Expected (B-[#])`. Naming the violated belief before naming the surprise
prevents the model from surfacing "surprises" that were never unexpected. The
contradiction must be stated before the finding is written. This converts belief
traceability from a property the surrounding structure is assumed to preserve into
an independently enforced requirement at entry granularity.

---

## Vocabulary Compliance

The only valid epistemic dimension names:

> **Feasibility · Usability · Scalability · Adoptability · Correctness**

Named prohibited synonyms with mandatory canonical replacements:

| Prohibited      | Canonical Replacement |
|-----------------|-----------------------|
| Reliability     | Correctness           |
| Performance     | Scalability           |
| Complexity      | Usability             |
| Maintainability | Correctness           |
| Robustness      | Correctness           |
| Efficiency      | Scalability           |

Self-repair at every EXIT: scan dimension cells; if a prohibited synonym appears,
correct it using the mapping table before emitting the stage token.

---

## Gate Map

| Token                   | Issued             | Condition                                                                   |
|-------------------------|--------------------|-----------------------------------------------------------------------------|
| COMMIT-STAGE-1          | Stage 1            | Opening model + epistemic profile + ≥3 beliefs labeled B-#                 |
| COMMIT-STAGE-2          | Stage 2            | Deviation table complete; every row has named artifact + B-#                |
| COMMIT-STAGE-3-CLEAN    | Stage 3            | All five checks VALID; no foreknowledge detected                            |
| COMMIT-STAGE-3-FLAGGED  | Stage 3            | Foreknowledge detected — HALT                                               |
| COMMIT-ENTRY            | Per Stage 4 entry  | All five sub-fields pass quality gate                                       |
| COMMIT-STAGE-4          | Stage 4            | All GATE-CONFIRMED entries written; ≥2 entries                              |
| COMMIT-STAGE-5          | Stage 5            | Cluster map complete; ≥1 named skill/role in Next Team column               |
| COMMIT-STAGE-6          | Stage 6            | Verdict table complete; foreknowledge status = CLEAR or FLAGGED             |
| COMMIT-STAGE-7          | Stage 7            | Artifact delivered — only valid when foreknowledge status = CLEAR           |

**HALT**: If COMMIT-STAGE-3-FLAGGED issued, Stage 4 does not execute.
Output: `HALT — foreknowledge detected in B-[#]. Artifact withheld.`

---

## Stage 1 — Opening Model

**ENTER**:
- Topic signals have been gathered; at least 3 artifacts exist for this topic

**Instructions**: Record your epistemic baseline before examining any signals.

**Opening Model** (2–4 sentences): What behavior, properties, and outcomes did you
expect for this topic?

**Epistemic Profile**:

| Dimension     | Prior Confidence (1–5) | Rationale |
|---------------|------------------------|-----------|
| Feasibility   |                        |           |
| Usability     |                        |           |
| Scalability   |                        |           |
| Adoptability  |                        |           |
| Correctness   |                        |           |

**Belief Register** (≥3 falsifiable beliefs):

- **B-1**: [falsifiable belief]
- **B-2**: [falsifiable belief]
- **B-3**: [falsifiable belief]
- [Add B-4, B-5 as warranted]

**EXIT**:
- Opening model written; all five dimension rows present; ≥3 beliefs labeled B-#
- Scan dimension cells — correct prohibited synonyms using mapping table

Emit: **COMMIT-STAGE-1**

---

## Stage 2 — Signal Deviation Scan

**ENTER**: COMMIT-STAGE-1 emitted.

**Instructions**: For every signal artifact that produced an unexpected finding, record
a deviation row. Confirmations excluded.

| Row | Signal Artifact (name, namespace, date)  | Expected (per B-#) | Actual Finding | B-# Challenged |
|-----|------------------------------------------|--------------------|----------------|----------------|
| D-1 |                                          |                    |                |                |
| D-2 |                                          |                    |                |                |

Signal Source rule: every artifact cell names a specific artifact. Prohibited:
"multiple sources," "the signals," "various artifacts."

**EXIT**: Table complete; every row has named artifact and B-#.

Emit: **COMMIT-STAGE-2**

---

## Stage 3 — Adversarial Gate

**ENTER**: COMMIT-STAGE-2 emitted.

**Instructions**: Execute the five-check protocol. Record VALID or INVALID for each check.

| # | Check                                                                                      | Verdict |
|---|--------------------------------------------------------------------------------------------|---------|
| 1 | Every row is a genuine deviation — not a confirmation reframed as a surprise               |         |
| 2 | Every Signal Source is a named artifact — not "multiple sources," "the signals," "various artifacts" |         |
| 3 | At least one deviation contradicts (not merely refines) a B-# belief                      |         |
| 4 | At least 2 deviations are eligible for Stage 4                                             |         |
| 5 | No deviation draws on prior-session content generated by the model for this topic          |         |

Issue **GATE-CONFIRMED-[N]** for rows passing checks 1, 2, and 5.
Issue **GATE-REJECTED** for rows failing any check.

If fewer than 2 GATE-CONFIRMED rows: extend Stage 2; re-run Stage 3.

**EXIT**:
- All five checks have verdicts; each D-row has GATE-CONFIRMED-[N] or GATE-REJECTED
- If Check 5 INVALID: emit **COMMIT-STAGE-3-FLAGGED** (name implicated B-#); HALT
- If Check 5 VALID for all rows: emit **COMMIT-STAGE-3-CLEAN**

---

## Stage 4 — Belief-Anchored Surprise Synthesis

**ENTER**:
- COMMIT-STAGE-3-CLEAN emitted
- ≥2 GATE-CONFIRMED rows available

### Field Reference

All five sub-fields are defined here. **The sequence is structural: `What We Expected
(B-[#])` is always the first sub-field of every entry.** The violated belief is anchored
before the surprise is named.

| # | Field                           | What It Names                              | Quality Floor                                                                                   |
|---|---------------------------------|--------------------------------------------|------------------------------------------------------------------------------------------------|
| 1 | **What We Expected (B-[#])**   | The Stage 1 belief this finding contradicts| Full sentence explicitly naming a specific B-# — not "we assumed it would work" or "we expected it to be fine" |
| 2 | **Surprise**                    | The specific unexpected finding            | Named, specific — not a general observation or feature-area summary                            |
| 3 | **Signal Source**               | The artifact that surfaced this finding    | Name + namespace + date; prohibited: "multiple sources," "the signals," "various artifacts"    |
| 4 | **Design Impact**               | What must change in the design             | Named component, API, flow, or decision — not "the system" or "the architecture"               |
| 5 | **Build Risk**                  | What is implicated by that change          | Named *different* component, dependency, or contract — not a paraphrase of Design Impact       |

> **Build Risk field definition**:
> - *Purpose*: names what is implicated when the Design Impact change is made
> - *Paired formula*: Design Impact = what must change (forward-looking); Build Risk = what
>   could break or require rework as a result (risk-surface)
> - *Structural gloss*: one field is the update target (forward-looking); the other is the
>   fragility surface (what could break or require rework) — these poles are always distinct

---

### Surprise 0 *(Calibration Entry — not a live entry. The live sequence begins at Surprise 1.)*

**What We Expected (B-2)**: We expected (B-2) that retry logic maintains its fixed
interval regardless of circuit breaker state — operating on its own timer, independent
of upstream availability signals.

**Surprise**: The `flow-resilience` simulation revealed that retry backoff intervals
collapse to zero when the circuit breaker is open, producing a thundering-herd failure
mode on recovery.

**Signal Source**: `flow-resilience-signal-2026-03-14.md`, flow namespace.

**Design Impact**: The `RetryPolicy` component must add a jitter coefficient conditioned
on `CircuitBreaker.state`.

**Build Risk**: The `BackoffTimer` interface currently accepts no upstream state
parameter — introducing one is a breaking interface change for all retry callers.

---

### Live Entries (Surprise 1, 2, ...)

For each GATE-CONFIRMED-[N], write one entry. **Begin with `What We Expected (B-[#])`.
State the violated belief first — then name the surprise.**

**Surprise [N]**

**What We Expected (B-[#])**: [Full sentence stating the specific B-# belief this
finding contradicts — must include the B-# label and a complete sentence describing
the prior expectation]

**Surprise**: [Specific named finding]

**Signal Source**: [Named artifact — name, namespace, date; no prohibited phrases]

**Design Impact**: [Named component, API, flow, or decision]

**Build Risk**: [Named different component, dependency, or contract]

**COMMIT-ENTRY gate** — verify all of the following in order before emitting:

- ✓ **What We Expected**: contains a specific B-# label AND a full sentence describing the prior expectation — if absent, generic ("we thought it would work"), or missing the B-# label, rewrite with a specific B-# reference before emitting
- ✓ **Surprise**: names a specific finding — if a general observation or feature-area summary, rewrite with a specific named finding before emitting
- ✓ **Signal Source**: names a specific artifact with name/namespace/date — if "multiple sources," "the signals," "various artifacts," or any generic phrase present, replace with a named artifact before emitting
- ✓ **Design Impact**: names a specific component, API, flow, or decision — if "the system" or "the architecture," rewrite before emitting
- ✓ **Build Risk**: names a component, dependency, or contract different from Design Impact — if a paraphrase of Design Impact or a general risk statement ("there are risks"), rewrite before emitting

Emit: **COMMIT-ENTRY**

**EXIT**:
- Every GATE-CONFIRMED row has a Surprise entry beginning with What We Expected (B-[#])
- At least 2 entries emitted; every entry has a COMMIT-ENTRY token
- Scan any dimension references for prohibited synonyms; correct before emitting

Emit: **COMMIT-STAGE-4**

---

## Stage 5 — Cluster Map

**ENTER**: COMMIT-STAGE-4 emitted.

**Instructions**: Group surprises by epistemic dimension. Identify next investigative
actions.

| Cluster          | Surprises | Pattern | Next Team / Skill | Priority |
|------------------|-----------|---------|-------------------|----------|
|                  |           |         |                   |          |

At least one Next Team / Skill cell must name a specific skill (e.g., `/flow-trigger`)
or role (e.g., "circuit breaker owner") — not "investigate" alone.

**EXIT**:
- Every cluster row names a valid canonical dimension
- ≥1 named skill or role in Next Team / Skill column
- Dimension cells checked; prohibited synonyms corrected

Emit: **COMMIT-STAGE-5**

---

## Stage 6 — Epistemic Verdict

**ENTER**: COMMIT-STAGE-5 emitted.

**Instructions**: Issue a verdict for each B-# belief from Stage 1.

| Belief | Verdict                                                  | Revision Direction |
|--------|----------------------------------------------------------|--------------------|
| B-1    | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED         |                    |
| B-2    |                                                          |                    |
| B-3    |                                                          |                    |

**Foreknowledge Status**:
- **CLEAR** — No FOREKNOWLEDGE-FLAGGED verdicts. Proceed to Stage 7.
- **FLAGGED** — One or more FOREKNOWLEDGE-FLAGGED verdicts. Name B-# labels. Do not proceed to Stage 7.

**EXIT**:
- Verdict table complete; foreknowledge status recorded as CLEAR or FLAGGED
- If FLAGGED, implicated B-# labels named

Emit: **COMMIT-STAGE-6**

---

## Stage 7 — Artifact Delivery

**ENTER**:
- COMMIT-STAGE-6 emitted AND foreknowledge status = CLEAR

If foreknowledge status = FLAGGED: output
`ARTIFACT WITHHELD — foreknowledge unresolved in B-[#].` Do not enter Stage 7.

**Instructions**: Deliver the final topic-reflect artifact as a single coherent output
block:
1. All Stage 4 surprise entries (all COMMIT-ENTRY rows)
2. Stage 5 cluster map
3. Stage 6 verdict summary with foreknowledge status

**EXIT**: Artifact delivered as unified output.

Emit: **COMMIT-STAGE-7**
```

---

## Scorecard Forecast

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-01** Surprise orientation | PASS 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 |
| **C-02** Symmetric Contract | PASS 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 |
| **C-03** Signal tracing | PASS 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 |
| **C-04** Design impact specificity | PASS 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 |
| **C-05** Adversarial gate executed | PASS 12 | PASS 12 | PASS 12 | PASS 12 | PASS 12 |
| **C-06** Epistemic dimension compliance | PASS 10 | PASS 10 | PASS 10 | PASS 10 | PASS 10 |
| **C-07** Minimum 2 surprises | PASS 10 | PASS 10 | PASS 10 | PASS 10 | PASS 10 |
| **C-08** Cluster map actionability | PASS 10 | PASS 10 | PASS 10 | PASS 10 | PASS 10 |
| **C-09** Token protocol integrity | PASS 5 | FAIL 0 | FAIL 0 | PASS 5 | PASS 5 |
| **C-10** Foreknowledge signal evaluated | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| **C-11** Stage 4 prose template format | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| **C-12** Stage 4 entry completeness | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| **C-13** Closed-list dimension vocabulary | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| **C-14** Foreknowledge dual-token gate | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| **C-15** Pre-stage gate sequence map | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| **C-16** Worked calibration example | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| **C-17** Named synonym exclusions | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| **C-18** Synonym-to-canonical mapping | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| **C-19** Per-stage ENTER/EXIT | PASS 5 | FAIL 0 | FAIL 0 | PASS 5 | PASS 5 |
| **C-20** Calibration as Surprise 0 | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| **C-21** Vocabulary self-repair at EXIT | PASS 5 | PARTIAL? 3 | PASS 5 | PASS 5 | PASS 5 |
| **C-22** Stage 4 Build Risk sub-field | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| **C-23** Surprise 0 dual-field specificity | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| **C-24** COMMIT-ENTRY Build Risk gate | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| **C-25** Four-field convergent mechanism | PASS 5 | PARTIAL? 3 | PASS 5 | PASS 5 | PASS 5 |
| **C-26** Build Risk paired formula | PASS 5 | FAIL 0 | PASS 5 | PASS 5 | PASS 5 |
| **C-27** Build Risk triple-anchor | PASS 5 | FAIL 0 | PASS 5 | PASS 5 | PASS 5 |
| **C-28** COMMIT-ENTRY visual checklist | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| **C-29** Stage 4 Field Reference block | PASS 5 | FAIL 0 | PASS 5 | PASS 5 | PASS 5 |
| **C-30** Calibration live/example boundary | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| **C-31** Stage 7 discrete structural element | PASS 5 | FAIL 0 | FAIL 0 | PASS 5 | PASS 5 |
| **C-32** Named Signal Source prohibited phrases | PASS 5 | PASS 5 | PASS 5 | PASS 5 | PASS 5 |
| **C-33** Stage 4 B-# belief anchor sub-field | FAIL 0 | FAIL 0 | FAIL 0 | FAIL 0 | PASS 5 |
| **Estimated Total** | ~198 | ~171 | ~183 | ~203 | **~210** |

**Key differentiators this round**:
- **C-01**: All five variations now score FULL PASS (12/12) — the B-# sub-field is present in every template, eliminating the PARTIAL that blocked V-01 through V-04 in Round 13
- **C-33**: V-01 through V-04 score FAIL (B-# present but not as first sub-field; EXIT gate checks it but not as the lead check); V-05 scores PASS (first sub-field + Surprise 0 calibration + EXIT gate as first enforced check)
- **C-19**: V-02 and V-03 score FAIL — no explicit ENTER/EXIT labels for 3+ stages; V-01, V-04, V-05 all pass
- **C-26/C-27**: V-02 scores FAIL on both — no Build Risk paired conceptual formula or triple-anchor sequence; all others pass
- **C-29**: V-02 scores FAIL — no dedicated Field Reference block; all others pass
- **C-31**: V-02 and V-03 score FAIL — no Stage 7; V-01, V-04, V-05 all pass
