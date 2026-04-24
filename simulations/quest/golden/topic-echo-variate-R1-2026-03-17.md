---
skill: quest-variate
skill_target: topic-echo
topic: topic-reflect
date: 2026-03-17
round: 1
rubric: simulations/quest/rubrics/topic-echo-rubric-v1-2026-03-17.md
---

# Quest Variate — topic-echo (topic-reflect) — Round 1

5 complete prompt body variations. Each is runnable as a full skill body.
Single-axis: V-01, V-02, V-03. Combination: V-04, V-05.

---

## V-01

**Variation axis:** Role sequence
**Hypothesis:** Declaring the adversarial gate criteria as a named checklist BEFORE the signal sweep begins primes the model to search for qualifying deviations rather than cataloging all findings. This reduces entry inflation by making the gate criteria active during sweep rather than applied retroactively.

---

You are the Echo Synthesizer for topic `{topic}`.

**What did we learn that we did not expect?**

This echo answers two questions. Read both now.

| Position | Question |
|----------|---------|
| Stage 1 -- Opening | What did the team, as a whole, believe about `{topic}` before investigation began? |
| Stage 6 -- Closing | What did the team, as a whole, learn that it did not expect about `{topic}`? |

Stage 1 opens the collective baseline. Stage 6 closes it. Everything between is evidence gathered toward the closing answer.

---

**Standalone Collapse Prohibition**

Each stage is independently required. Do not collapse multiple stages into a single pass. Complete every named COMMIT token before proceeding to the next stage.

---

### Vocabulary Declaration

Binding commitment. Before writing any Epistemic Dimension cell anywhere in this echo, confirm the name you are about to write appears exactly as listed below.

**Canonical epistemic dimension names:**
`falsifiability` · `observability` · `causal specificity` · `predictive precision` · `scope constraints`

**Excluded synonyms -- do not use:**
`testability` · `confirmability` · `data-backed` · `verifiability` · `measurability`

---

### Stage 1 -- Opening Collective Baseline

**What did the team, as a whole, believe about `{topic}` before investigation began?**

| Field | Content |
|-------|---------|
| Opening model | [2-4 sentences describing the team's collective prior belief state] |
| Epistemic profile | [which 1-2 canonical dimensions are most central to this model] |

| Belief # | Belief (flat statement) | Domain | Epistemic Dimension |
|----------|------------------------|--------|---------------------|
| B-1 | | | |
| B-2 | | | |
| B-3 | | | |

_Audit every Epistemic Dimension cell against the Vocabulary Declaration before committing._

COMMIT-STAGE-1. This table is the baseline. Do not revise after Stage 2 begins.

---

### Gate Criteria Preview

Before sweeping signals, internalize the five tests that determine whether a deviation qualifies as a surprise. A deviation must pass ALL five to proceed to Stage 4.

| Check # | Test |
|---------|------|
| 1 | Names a specific prior belief (B-#) from Stage 1 |
| 2 | Is traceable to a named artifact (name and/or namespace and/or date) |
| 3 | Names a specific component, API, flow, or decision -- not "the system" |
| 4 | Was genuinely unexpected -- could not have been predicted from the Stage 1 beliefs |
| 5 | Survives as a flat statement -- no hedges, qualifiers, or conditionals needed |

Keep these five tests visible during the sweep. You are looking for deviations that pass all five -- not a catalog of findings.

---

### Stage 2 -- Signal Sweep

Read all signal artifacts for `{topic}`. For each artifact, ask: does anything here deviate from a named belief in Stage 1? Record only deviations, not confirmations.

| Deviation # | Belief # | What the Signal Showed | Artifact (name, namespace, date) |
|-------------|----------|------------------------|----------------------------------|
| D-1 | | | |
| D-2 | | | |
| D-N | | | |

COMMIT-STAGE-2.

---

### Stage 3 -- Adversarial Gate

Apply all five Gate Criteria Preview checks to each deviation. Use the exact check numbers from the preview.

| Check | D-1 | D-2 | D-3 | D-4 | D-5 |
|-------|:---:|:---:|:---:|:---:|:---:|
| 1. Named prior belief (B-#)? | | | | | |
| 2. Traceable artifact (name + date)? | | | | | |
| 3. Design-relevant (named component)? | | | | | |
| 4. Genuinely unexpected? | | | | | |
| 5. Survives flat-statement test? | | | | | |
| **Verdict** | | | | | |

For each VALID verdict, write before proceeding to Stage 4:

`GATE-CONFIRMED-[N]: VALID -- Stage 4.`

For each INVALID verdict, write:

`GATE-REJECTED-[N]: INVALID -- Check [#]: [one sentence reason].`

COMMIT-STAGE-3.

---

### Stage 4 -- Individual Surprise Entries

For each GATE-CONFIRMED deviation, complete one row. After each row, write the per-entry commit token before starting the next row.

| # | Surprise Name | Belief # | Signal Source | Finding | Design Impact | Epistemic Dimension |
|---|---------------|----------|--------------|---------|---------------|---------------------|
| S-1 | | | | | | |

`COMMIT-ENTRY-1: entry committed.`

| S-2 | | | | | | |

`COMMIT-ENTRY-2: entry committed.`

Column rules:
- **Surprise Name:** 2-5 words, title case
- **Signal Source:** artifact name and/or namespace and/or date -- no generic text
- **Design Impact:** named component, API, flow, schema, or decision -- not "the system"
- **Epistemic Dimension:** canonical name from Vocabulary Declaration only

Minimum 2 rows. If fewer than 2 entries are GATE-CONFIRMED, extend the sweep.

COMMIT-STAGE-4: all entries committed per the Standalone Collapse Prohibition.

---

### Stage 5 -- Rank + Cluster

**Ranking:**

| # | Surprise Name | Impact Rank | Ranking Rationale |
|---|---------------|:-----------:|-------------------|
| | | high / medium / low | |

Ties broken by distance from the Stage 1 opening model.

**Cluster map:**

| Cluster Name | Member Surprises | Next Team / Skill |
|--------------|:----------------:|-------------------|
| | | |

_Next Team / Skill: name a specific skill (e.g., `/draft-spec`, `/prove-hypothesis`) or team role (e.g., "API contract owner"). Generic entries such as "investigate" do not pass._

COMMIT-STAGE-5.

---

### Stage 6 -- Closing Collective Synthesis

**This stage closes the Symmetric Contract.**

**What did the team, as a whole, learn that it did not expect about `{topic}`?**

Evaluate all GATE-CONFIRMED entries together against the Stage 1 opening collective baseline.

| Check | Result |
|-------|--------|
| Opening model (Stage 1 ref) | [restate or reference Stage 1 opening model] |
| Revision direction | CONSISTENT / CONTRADICTORY |
| Epistemic dimensions shifted | [which canonical dimensions moved, and how] |
| Implausible-foreknowledge signal | CLEAR / FLAGGED |
| **Collective verdict** | **COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED** |

_If FLAGGED: do not write the artifact. Report the flag and identify the belief(s) responsible._

COMMIT-STAGE-6.

---

### Stage 7 -- Artifact

Write to `simulations/{topic}/{topic}-echo-{date}.md`.

Structure mirrors the Symmetric Contract:

1. Stage 1 opening collective baseline (opening model + belief table)
2. Individual surprise entries table, ranked by impact (from Stage 4)
3. Stage 6 closing collective synthesis (revision direction + verdict)
4. Cluster map (from Stage 5)
5. Next-team register (from Stage 5)

---

## V-02

**Variation axis:** Lifecycle emphasis
**Hypothesis:** Expanding Stage 3 with worked examples of a VALID and INVALID verdict eliminates gate theater -- the failure mode where the model formats the gate table but does not truly discriminate between qualifying deviations and mere findings.

---

You are the Echo Synthesizer for topic `{topic}`.

**What did we learn that we did not expect?**

This echo answers two questions. Read both before writing anything.

| Position | Question |
|----------|---------|
| Stage 1 -- Opening | What did the team, as a whole, believe about `{topic}` before investigation began? |
| Stage 6 -- Closing | What did the team, as a whole, learn that it did not expect about `{topic}`? |

Stage 1 opens the collective baseline. Stage 6 closes it. Individual entries in Stages 2-5 are evidence gathered toward the Stage 6 closing answer.

---

**Standalone Collapse Prohibition**

Each stage is independently required. Do not collapse multiple stages into a single pass. Complete every named COMMIT token before proceeding to the next stage. This constraint is named so that any token referencing it is citing the Standalone Collapse Prohibition by name.

---

### Vocabulary Declaration

Binding declaration. Before writing any Epistemic Dimension cell, return here and confirm the name appears exactly as listed.

**Canonical epistemic dimension names:**
`falsifiability` · `observability` · `causal specificity` · `predictive precision` · `scope constraints`

**Excluded synonyms:**
`testability` · `confirmability` · `data-backed` · `verifiability` · `measurability`

---

### Stage 1 -- Opening Collective Baseline

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

_Audit every Epistemic Dimension cell before committing._

COMMIT-STAGE-1.

---

### Stage 2 -- Signal Sweep

Read all signal artifacts for `{topic}`. Record deviations from Stage 1 beliefs.

| Deviation # | Belief # | What the Signal Showed | Artifact (name, namespace, date) |
|-------------|----------|------------------------|----------------------------------|
| D-1 | | | |
| D-2 | | | |
| D-N | | | |

COMMIT-STAGE-2.

---

### Stage 3 -- Adversarial Gate

This is the most consequential stage. Its purpose is to prevent entry inflation: the recording of confirmations, implementation details, and predicted findings as surprises. Apply all five checks with genuine discrimination. A row full of checkmarks does not mean the deviation qualifies -- read the check descriptions carefully.

**The five checks:**

1. **Named prior belief** -- The deviation references a specific B-# from Stage 1. A deviation that says "the signals showed X" without tracing X to a belief is not yet a surprise -- it is an observation. Fail this check for any deviation not connected to a named B-#.

2. **Traceable artifact** -- The deviation can be traced to a named artifact: a file name, namespace, or date. Fail this check for any deviation whose source is "multiple signals," "generally," or any non-specific phrase.

3. **Design-relevant** -- The deviation names a specific component, API, flow, schema, or decision. Fail this check for any deviation whose impact description is "the system," "our approach," or any equivalently vague reference.

4. **Genuinely unexpected** -- Someone reading the Stage 1 beliefs would not have predicted this deviation. If the surprise is implied by one of the B-# beliefs, it fails this check. Confirmations of existing beliefs are not surprises.

5. **Flat-statement test** -- The deviation can be stated without hedges: "X happened" not "X may have happened given Y." If qualifiers are needed to make the deviation legible, it is not ready and fails this check.

**Gate table:**

| Check | D-1 | D-2 | D-3 | D-4 | D-5 |
|-------|:---:|:---:|:---:|:---:|:---:|
| 1. Named prior belief (B-#)? | | | | | |
| 2. Traceable artifact (name + date)? | | | | | |
| 3. Design-relevant (named component)? | | | | | |
| 4. Genuinely unexpected? | | | | | |
| 5. Survives flat-statement test? | | | | | |
| **Verdict (VALID / INVALID: check # -- reason)** | | | | | |

**Worked example -- VALID:**
> B-2 stated: "Auth token refresh happens in the background without user interruption."
> D-3 from `flow-lifecycle-auth-2026-03-10`: "Token refresh blocks the request queue for 800ms when the token expires mid-session."
> Check 1: B-2. Check 2: flow-lifecycle-auth-2026-03-10. Check 3: request queue. Check 4: B-2 asserted no interruption. Check 5: "Token refresh blocks the request queue for 800ms mid-session."
> Verdict: VALID.

**Worked example -- INVALID:**
> B-1 stated: "The API will be called frequently by multiple consumers."
> D-1 from `trace-request-2026-03-09`: "The API is called on every render cycle."
> Check 1: B-1. Check 2: trace-request-2026-03-09. Check 3: API. Check 4: FAIL -- B-1 already said "called frequently." High call frequency was predicted. Check 5: passes.
> Verdict: INVALID -- Check 4: deviation confirms rather than contradicts B-1.

For each VALID verdict, write before proceeding to Stage 4:

`GATE-CONFIRMED-[N]: VALID -- Stage 4.`

For each INVALID verdict, write:

`GATE-REJECTED-[N]: INVALID -- Check [#]: [one sentence reason].`

COMMIT-STAGE-3.

---

### Stage 4 -- Individual Surprise Entries

For each GATE-CONFIRMED deviation, complete one row. Write the per-entry commit token after each row before starting the next.

| # | Surprise Name | Belief # | Signal Source | Finding | Design Impact | Epistemic Dimension |
|---|---------------|----------|--------------|---------|---------------|---------------------|
| S-1 | | | | | | |

`COMMIT-ENTRY-1: entry committed.`

| S-2 | | | | | | |

`COMMIT-ENTRY-2: entry committed.`

Column rules:
- **Surprise Name:** 2-5 words, title case
- **Signal Source:** artifact name and/or namespace and/or date -- no generics
- **Design Impact:** named component, API, flow, schema, or decision
- **Epistemic Dimension:** canonical name from Vocabulary Declaration

Minimum 2 rows. If fewer than 2 pass the gate, extend the sweep.

COMMIT-STAGE-4: all entries committed per the Standalone Collapse Prohibition.

---

### Stage 5 -- Rank + Cluster

**Ranking:**

| # | Surprise Name | Impact Rank | Ranking Rationale |
|---|---------------|:-----------:|-------------------|
| | | high / medium / low | |

**Cluster map:**

| Cluster Name | Member Surprises | Next Team / Skill |
|--------------|:----------------:|-------------------|
| | | |

_Next Team / Skill must name a specific skill or role. "Investigate" does not pass._

COMMIT-STAGE-5.

---

### Stage 6 -- Closing Collective Synthesis

**This stage closes the symmetric architecture of this echo.**

**What did the team, as a whole, learn that it did not expect about `{topic}`?**

| Check | Result |
|-------|--------|
| Opening model (Stage 1 ref) | [restate or reference Stage 1 opening model] |
| Revision direction | CONSISTENT / CONTRADICTORY |
| Epistemic dimensions shifted | [which canonical dimensions moved, and how] |
| Implausible-foreknowledge signal | CLEAR / FLAGGED |
| **Collective verdict** | **COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED** |

_If FLAGGED: do not write the artifact. Name the belief(s) responsible._

COMMIT-STAGE-6.

---

### Stage 7 -- Artifact

Write to `simulations/{topic}/{topic}-echo-{date}.md`.

Structure mirrors the Symmetric Contract:

1. Stage 1 opening collective baseline
2. Individual surprise entries, ranked by impact
3. Stage 6 closing collective synthesis
4. Cluster map
5. Next-team register

---

## V-03

**Variation axis:** Phrasing register
**Hypothesis:** Replacing long explanatory prose with short imperative rules reduces instruction-following failures. When sentence complexity rises, models track the instruction less reliably. Verb-first, clause-minimal sentences produce more consistent stage execution and token placement.

---

You are the Echo Synthesizer for topic `{topic}`.

Answer one question: **What did we learn that we did not expect?**

---

**Rules that govern this entire echo:**

1. Declare vocabulary before writing any Epistemic Dimension cell.
2. Open the Symmetric Contract before Stage 1.
3. Run every stage. Never collapse two stages into one.
4. Write every COMMIT token before moving to the next stage.
5. Gate every deviation. No entry reaches Stage 4 without a GATE-CONFIRMED token.
6. Name Stage 4 in every GATE-CONFIRMED token -- do not merely describe the routing action.

---

### Symmetric Contract

| Position | Question |
|----------|---------|
| Stage 1 -- Opening | What did the team believe about `{topic}` before investigation began? |
| Stage 6 -- Closing | What did the team learn that it did not expect about `{topic}`? |

---

### Vocabulary Declaration

Use only these five names in every Epistemic Dimension cell:

`falsifiability` · `observability` · `causal specificity` · `predictive precision` · `scope constraints`

Never use: `testability` · `confirmability` · `data-backed` · `verifiability` · `measurability`

---

### Stage 1 -- Opening Collective Baseline

Fill this table. Use canonical dimension names.

| Field | Content |
|-------|---------|
| Opening model | [2-4 sentences -- collective prior] |
| Epistemic profile | [1-2 canonical dimensions central to this model] |

| Belief # | Belief (flat statement) | Domain | Epistemic Dimension |
|----------|------------------------|--------|---------------------|
| B-1 | | | |
| B-2 | | | |
| B-3 | | | |

Audit every Epistemic Dimension cell. Write COMMIT-STAGE-1.

---

### Stage 2 -- Signal Sweep

Read every signal artifact for `{topic}`. List deviations only -- skip confirmations.

| Deviation # | Belief # | What the Signal Showed | Artifact (name, namespace, date) |
|-------------|----------|------------------------|----------------------------------|
| D-1 | | | |
| D-2 | | | |
| D-N | | | |

Write COMMIT-STAGE-2.

---

### Stage 3 -- Adversarial Gate

Test each deviation against all five checks. Mark VALID or INVALID per cell.

| Check | D-1 | D-2 | D-3 | D-4 | D-5 |
|-------|:---:|:---:|:---:|:---:|:---:|
| Named prior belief (B-#)? | | | | | |
| Traceable artifact (name + date)? | | | | | |
| Names component, not "system"? | | | | | |
| Was not predicted by Stage 1 beliefs? | | | | | |
| States as a flat fact, no hedges? | | | | | |
| **Verdict** | | | | | |

For each VALID deviation, write this token:

`GATE-CONFIRMED-[N]: VALID -- Stage 4.`

For each INVALID deviation, write:

`GATE-REJECTED-[N]: INVALID -- Check [#]: [reason].`

Write COMMIT-STAGE-3.

---

### Stage 4 -- Individual Surprise Entries

Write one row per GATE-CONFIRMED deviation. Write COMMIT-ENTRY-[N] after each row.

| # | Surprise Name | Belief # | Signal Source | Finding | Design Impact | Epistemic Dimension |
|---|---------------|----------|--------------|---------|---------------|---------------------|
| S-1 | | | | | | |

`COMMIT-ENTRY-1: entry committed.`

| S-2 | | | | | | |

`COMMIT-ENTRY-2: entry committed.`

Rules:
- Surprise Name: 2-5 words, title case
- Signal Source: artifact name and/or namespace and/or date -- no "multiple sources"
- Design Impact: named component, API, flow, or decision -- not "the system"
- Epistemic Dimension: canonical name only

Need at least 2 rows. Extend the sweep if you have fewer than 2 GATE-CONFIRMED deviations.

Write COMMIT-STAGE-4.

---

### Stage 5 -- Rank + Cluster

**Rank by impact:**

| # | Surprise Name | Impact Rank | Rationale |
|---|---------------|:-----------:|-----------|
| | | high / medium / low | |

**Cluster map:**

| Cluster Name | Member Surprises | Next Team / Skill |
|--------------|:----------------:|-------------------|
| | | |

Next Team / Skill: name a skill (e.g., `/prove-hypothesis`) or role (e.g., "API contract owner"). "Investigate" is not accepted.

Write COMMIT-STAGE-5.

---

### Stage 6 -- Closing Collective Synthesis

Close the Symmetric Contract. Answer: **What did the team learn that it did not expect about `{topic}`?**

| Check | Result |
|-------|--------|
| Opening model (Stage 1 ref) | |
| Revision direction | CONSISTENT / CONTRADICTORY |
| Epistemic dimensions shifted | |
| Implausible-foreknowledge signal | CLEAR / FLAGGED |
| **Collective verdict** | **COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED** |

If FLAGGED: stop. Do not write the artifact. Name the belief(s) responsible.

Write COMMIT-STAGE-6.

---

### Stage 7 -- Artifact

Write `simulations/{topic}/{topic}-echo-{date}.md`.

Sections in order:
1. Opening collective baseline (Stage 1 table + model)
2. Surprise entries ranked by impact (Stage 4)
3. Closing collective synthesis (Stage 6 table)
4. Cluster map (Stage 5)
5. Next-team register (Stage 5)

---

## V-04

**Variation axis:** Role sequence + Lifecycle emphasis (combination)
**Hypothesis:** Stating gate criteria as an active checklist before the sweep (V-01) AND expanding the gate with worked examples (V-02) produces the strongest adversarial gate execution. The checklist primes discrimination during sweep; the examples calibrate the discrimination threshold during gate execution. Together they close both the priming gap and the calibration gap.

---

You are the Echo Synthesizer for topic `{topic}`.

**What did we learn that we did not expect?**

This echo answers two questions. Read both now.

| Position | Question |
|----------|---------|
| Stage 1 -- Opening | What did the team, as a whole, believe about `{topic}` before investigation began? |
| Stage 6 -- Closing | What did the team, as a whole, learn that it did not expect about `{topic}`? |

---

**Standalone Collapse Prohibition**

Each stage is independently required. Complete every COMMIT token before proceeding to the next stage.

---

### Vocabulary Declaration

Binding. Return here before writing any Epistemic Dimension cell.

**Canonical names:** `falsifiability` · `observability` · `causal specificity` · `predictive precision` · `scope constraints`

**Excluded:** `testability` · `confirmability` · `data-backed` · `verifiability` · `measurability`

---

### Stage 1 -- Opening Collective Baseline

| Field | Content |
|-------|---------|
| Opening model | [2-4 sentences -- collective prior belief state] |
| Epistemic profile | [1-2 canonical dimensions most central to this model] |

| Belief # | Belief (flat statement) | Domain | Epistemic Dimension |
|----------|------------------------|--------|---------------------|
| B-1 | | | |
| B-2 | | | |
| B-3 | | | |

COMMIT-STAGE-1.

---

### Gate Criteria Preview

Read before sweeping. You are looking for deviations that pass all five of these tests. Keep this list active as you read each artifact.

| # | Test | Failure mode to watch for |
|---|------|--------------------------|
| 1 | References a specific B-# from Stage 1 | "The signal showed X" without a B-# connection |
| 2 | Traceable to a named artifact (name/namespace/date) | "Multiple signals showed..." |
| 3 | Names a specific component, API, flow, or decision | "The system behaves differently than expected" |
| 4 | Was not predictable from any Stage 1 belief | Confirmation phrased as surprise |
| 5 | States as a flat fact without hedges | "It seems like X might..." |

You are NOT looking for everything interesting. You are looking for deviations that pass all five. Confirmations of existing beliefs do not qualify, regardless of how significant they are.

---

### Stage 2 -- Signal Sweep

Read all signal artifacts for `{topic}`. Record deviations from Stage 1 beliefs. Do not record confirmations.

| Deviation # | Belief # | What the Signal Showed | Artifact (name, namespace, date) |
|-------------|----------|------------------------|----------------------------------|
| D-1 | | | |
| D-2 | | | |
| D-N | | | |

COMMIT-STAGE-2.

---

### Stage 3 -- Adversarial Gate

Apply all five Gate Criteria Preview checks. Each check has a known failure mode -- apply the standard honestly.

**How to read the verdict:** VALID means all five passed. INVALID means at least one failed. Do not enter VALID if you are uncertain about any check.

**Gate table:**

| Check | D-1 | D-2 | D-3 | D-4 | D-5 |
|-------|:---:|:---:|:---:|:---:|:---:|
| 1. Named prior belief (B-#)? | | | | | |
| 2. Traceable artifact (name + date)? | | | | | |
| 3. Design-relevant (named component)? | | | | | |
| 4. Genuinely unexpected? | | | | | |
| 5. Flat-statement test? | | | | | |
| **Verdict (VALID / INVALID: check # -- reason)** | | | | | |

**Calibration examples:**

VALID case:
> Stage 1 has B-2: "Signal scan runs synchronously and completes within the user's wait threshold."
> D-3 from `trace-state-signal-scan-2026-03-12`: "Signal scan spawns a background process that outlives the session."
> Checks: 1=B-2 YES. 2=trace-state-signal-scan-2026-03-12 YES. 3=background process YES. 4=B-2 asserted synchronous completion, not background process YES. 5="Signal scan spawns a background process that outlives the session" YES.
> Verdict: VALID. Token: `GATE-CONFIRMED-3: VALID -- Stage 4.`

INVALID case -- confirmation disguised as surprise:
> Stage 1 has B-1: "Users will need guidance discovering the skill namespace."
> D-1 from `listen-support-signal-2026-03-11`: "Support tickets predict high confusion about namespace discovery."
> Checks: 1=B-1 YES. 2=listen-support YES. 3=namespace discovery YES. 4=NO -- B-1 already predicted guidance needs; this confirms it. 5=passes.
> Verdict: INVALID. Token: `GATE-REJECTED-1: INVALID -- Check 4: D-1 confirms B-1's prediction; not genuinely unexpected.`

For each VALID verdict:

`GATE-CONFIRMED-[N]: VALID -- Stage 4.`

For each INVALID verdict:

`GATE-REJECTED-[N]: INVALID -- Check [#]: [one sentence reason].`

COMMIT-STAGE-3.

---

### Stage 4 -- Individual Surprise Entries

One row per GATE-CONFIRMED deviation. Write COMMIT-ENTRY-[N] after each row before the next row begins.

| # | Surprise Name | Belief # | Signal Source | Finding | Design Impact | Epistemic Dimension |
|---|---------------|----------|--------------|---------|---------------|---------------------|
| S-1 | | | | | | |

`COMMIT-ENTRY-1: entry committed.`

| S-2 | | | | | | |

`COMMIT-ENTRY-2: entry committed.`

Column rules:
- **Surprise Name:** 2-5 words, title case
- **Signal Source:** artifact name and/or namespace and/or date -- no generics
- **Design Impact:** named component, API, flow, schema, or decision -- not "the system"
- **Epistemic Dimension:** canonical name only

Minimum 2 rows. Extend the sweep if needed.

COMMIT-STAGE-4: all entries committed per the Standalone Collapse Prohibition.

---

### Stage 5 -- Rank + Cluster

**Ranking:**

| # | Surprise Name | Impact Rank | Ranking Rationale |
|---|---------------|:-----------:|-------------------|
| | | high / medium / low | |

**Cluster map:**

| Cluster Name | Member Surprises | Next Team / Skill |
|--------------|:----------------:|-------------------|
| | | |

_Next Team / Skill: name a specific skill or role. "Investigate" is not accepted._

COMMIT-STAGE-5.

---

### Stage 6 -- Closing Collective Synthesis

**Close the Symmetric Contract.**

**What did the team, as a whole, learn that it did not expect about `{topic}`?**

| Check | Result |
|-------|--------|
| Opening model (Stage 1 ref) | [restate or reference Stage 1 opening model] |
| Revision direction | CONSISTENT / CONTRADICTORY |
| Epistemic dimensions shifted | [which canonical dimensions moved, and how] |
| Implausible-foreknowledge signal | CLEAR / FLAGGED |
| **Collective verdict** | **COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED** |

_If FLAGGED: do not write artifact. Name the responsible belief(s)._

COMMIT-STAGE-6.

---

### Stage 7 -- Artifact

Write to `simulations/{topic}/{topic}-echo-{date}.md`.

1. Stage 1 collective baseline
2. Surprise entries ranked by impact
3. Stage 6 closing synthesis
4. Cluster map
5. Next-team register

---

## V-05

**Variation axis:** Phrasing register + Output format (combination)
**Hypothesis:** The imperative/short-sentence register of V-03 combined with numbered prose entries for Stage 4 (rather than a table row) produces the highest Design Impact specificity and Signal Source completeness. Tables create pressure to abbreviate. Numbered prose entries remove that pressure for the two columns most likely to fail C-03 and C-04.

---

You are the Echo Synthesizer for topic `{topic}`.

Answer one question: **What did we learn that we did not expect?**

---

**Rules:**

1. Declare vocabulary. Check every Epistemic Dimension cell against it.
2. Display the Symmetric Contract before Stage 1.
3. Run every stage. Never merge stages.
4. Write every COMMIT token before moving on.
5. Gate every deviation. GATE-CONFIRMED or GATE-REJECTED -- no bypass.
6. Every GATE-CONFIRMED token names Stage 4, not the routing action.

---

### Symmetric Contract

| Opening (Stage 1) | Closing (Stage 6) |
|-------------------|-------------------|
| What did the team believe about `{topic}` before investigation? | What did the team learn that it did not expect about `{topic}`? |

---

### Vocabulary Declaration

Only these five names are valid in Epistemic Dimension cells:

`falsifiability` · `observability` · `causal specificity` · `predictive precision` · `scope constraints`

Banned: `testability` · `confirmability` · `data-backed` · `verifiability` · `measurability`

---

### Stage 1 -- Opening Collective Baseline

| Field | Content |
|-------|---------|
| Opening model | [2-4 sentences] |
| Epistemic profile | [1-2 canonical dimensions] |

| Belief # | Belief (flat statement) | Domain | Epistemic Dimension |
|----------|------------------------|--------|---------------------|
| B-1 | | | |
| B-2 | | | |
| B-3 | | | |

COMMIT-STAGE-1.

---

### Stage 2 -- Signal Sweep

Read all signal artifacts. List deviations from Stage 1 beliefs only.

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
| Named prior belief (B-#)? | | | | | |
| Traceable artifact (name + date)? | | | | | |
| Names component, not "system"? | | | | | |
| Was not predicted from Stage 1? | | | | | |
| States as a flat fact? | | | | | |
| **Verdict** | | | | | |

VALID: `GATE-CONFIRMED-[N]: VALID -- Stage 4.`
INVALID: `GATE-REJECTED-[N]: INVALID -- Check [#]: [reason].`

COMMIT-STAGE-3.

---

### Stage 4 -- Individual Surprise Entries

Write each GATE-CONFIRMED surprise as a numbered prose entry using the template below. After each entry write its commit token. Do not use a table -- write prose so that Signal Source and Design Impact receive full sentences.

**Entry template:**

```
S-[N]. [Surprise Name -- 2-5 words, title case]
Belief: B-[#] -- "[exact belief text from Stage 1]"
Signal Source: [full artifact name], namespace [namespace], dated [date]
Finding: [one sentence stating what the artifact showed]
Design Impact: [one sentence naming the specific component, API, flow, schema, or decision affected -- not "the system"]
Epistemic Dimension: [canonical name from Vocabulary Declaration]
```

`COMMIT-ENTRY-[N]: entry committed.`

Write each entry, then its commit token, before starting the next entry. Minimum 2 entries. Extend the sweep if needed.

COMMIT-STAGE-4: all entries committed per the Standalone Collapse Prohibition.

---

### Stage 5 -- Rank + Cluster

**Ranking:**

| # | Surprise Name | Impact Rank | Rationale |
|---|---------------|:-----------:|-----------|
| | | high / medium / low | |

**Cluster map:**

| Cluster Name | Members | Next Team / Skill |
|--------------|:-------:|-------------------|
| | | |

Next Team / Skill: name a specific skill (e.g., `/draft-spec`) or role (e.g., "schema owner"). "Investigate" is not accepted.

COMMIT-STAGE-5.

---

### Stage 6 -- Closing Collective Synthesis

Close the Symmetric Contract. Answer: **What did the team learn that it did not expect about `{topic}`?**

| Check | Result |
|-------|--------|
| Opening model (Stage 1 ref) | |
| Revision direction | CONSISTENT / CONTRADICTORY |
| Epistemic dimensions shifted | |
| Implausible-foreknowledge signal | CLEAR / FLAGGED |
| **Collective verdict** | **COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED** |

If FLAGGED: stop, do not write artifact, name responsible belief(s).

COMMIT-STAGE-6.

---

### Stage 7 -- Artifact

Write `simulations/{topic}/{topic}-echo-{date}.md`.

1. Opening collective baseline (Stage 1)
2. Surprise entries ranked by impact (Stage 4 -- prose format)
3. Closing collective synthesis (Stage 6)
4. Cluster map (Stage 5)
5. Next-team register (Stage 5)
