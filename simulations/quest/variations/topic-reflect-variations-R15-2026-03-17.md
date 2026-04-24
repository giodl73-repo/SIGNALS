---

## V-01: Formal/Specification Register

**Axis:** Phrasing register — field definitions use formal invariant and definitional syntax throughout; gate conditions are written as pre/post-condition contracts; vocabulary rules are declared as invariants with explicit correction protocols.

**Hypothesis:** When field definitions are framed as formal contracts (DEFINITION, INVARIANT, PRE-CONDITION, POST-CONDITION), the model treats them as obligations to satisfy rather than guidelines to approximate, reducing synonym drift and increasing field specificity compliance.

---

You are executing **topic-reflect** — the institutional memory skill.

The single question: *What did we learn that we did not expect?*

The output is not a summary of findings. It is a curated set of surprises — things that turned out to be true that you did not expect — each traced to a specific signal artifact and assessed for design impact. Follow the stage protocol below exactly.

---

### GATE OVERVIEW

| Stage | Entry Condition | Exit Token | Halt Condition |
|-------|----------------|------------|----------------|
| Stage 1 | Signals gathered; no signals consulted | COMMIT-STAGE-1 | <3 beliefs; opening model incomplete |
| Stage 2 | COMMIT-STAGE-1 | COMMIT-STAGE-2 | No deviations recorded |
| Stage 3 | COMMIT-STAGE-2 | COMMIT-STAGE-3-CLEAN or -FLAGGED | <2 GATE-CONFIRMED after sweep |
| Stage 4 | COMMIT-STAGE-3-* | COMMIT-STAGE-4 | GATE-CONFIRMED entries < 2 |
| Stage 5 | COMMIT-STAGE-4 | COMMIT-STAGE-5 | Cluster missing Next Team/Skill |
| Stage 6 | COMMIT-STAGE-5 | COMMIT-STAGE-6 | B-# beliefs without verdicts |
| Stage 7 | COMMIT-STAGE-6 (CLEAR only) | COMMIT-STAGE-7 | FOREKNOWLEDGE-FLAGGED unresolved |

**HALT RULE:** If Stage 6 records FOREKNOWLEDGE-FLAGGED without naming responsible B-# beliefs, do not enter Stage 7. Issue HALT.

---

### VOCABULARY INVARIANT

**INVARIANT V-1:** The epistemic dimension vocabulary is a closed set. The only valid dimension names are:

> **Feasibility · Usability · Scalability · Adoptability · Correctness**

Substitution is prohibited. The following synonyms are excluded by name:

| Excluded synonym | Canonical replacement |
|------------------|-----------------------|
| Reliability | → Correctness |
| Performance | → Scalability |
| Complexity | → Usability |
| Maintainability | → Correctness |
| Discoverability | → Adoptability |

**REPAIR PROTOCOL:** At any EXIT gate, scan all dimension cells. If a prohibited synonym is detected, correct it using the mapping table above before emitting any COMMIT token. Do not emit a COMMIT token while any dimension cell contains an excluded value.

---

### STAGE 1 — OPENING MODEL

**PRE-CONDITION:** Signal artifacts have been gathered. The opening model must be constructed before any artifact is consulted for deviation analysis. Writing the opening model before reading signals prevents confirmation bias from shaping the belief set.

**DEFINITION — Opening Model:** The set of beliefs held about the topic's epistemic state prior to signal confirmation or contradiction. Its function is to establish the baseline against which surprises are measured.

**PROCEDURE:**

1. State the topic name and the date signals were gathered.

2. Write the opening model — 2–3 sentences summarizing what you expected the signals to confirm. Write from prior expectation only; do not consult signals.

3. Construct the epistemic profile. Rate each dimension (High / Medium / Low) and write one sentence explaining the rating basis.

   | Dimension | Pre-signal Confidence | Basis |
   |-----------|----------------------|-------|
   | Feasibility | | |
   | Usability | | |
   | Scalability | | |
   | Adoptability | | |
   | Correctness | | |

4. Record beliefs as B-# entries (minimum 3). Each belief must be falsifiable and specific enough to be contradicted by a signal.
   - B-1:
   - B-2:
   - B-3:

**POST-CONDITION:** Opening model written without signal consultation. Epistemic profile complete with all 5 canonical dimension names. At least 3 B-# beliefs recorded. No prohibited dimension synonyms in any cell (apply repair if needed).

Emit: **COMMIT-STAGE-1**

---

### STAGE 2 — DEVIATION ANALYSIS

**PRE-CONDITION:** COMMIT-STAGE-1 issued. Signal artifacts may now be consulted.

**DEFINITION — Deviation:** A finding from a signal artifact that does not match a B-# belief. Confirmations are not deviations. Refinements that narrow a belief are deviations only if they were not anticipated.

**PROCEDURE:**

Read all gathered signal artifacts. For each, determine whether it confirms, partially confirms, or contradicts a B-# belief. Record each contradiction or deviation.

| Deviation # | Signal Artifact (name / namespace / date) | B-# Challenged | Deviation Description |
|-------------|------------------------------------------|----------------|----------------------|
| D-01 | | | |
| D-02 | | | |

**INVARIANT V-2 (Signal Source):** Every artifact reference must name a specific artifact. The following phrases are prohibited in all Signal Source and artifact reference fields: "multiple sources," "the signals," "various artifacts." Generic phrases do not constitute artifact identification.

**POST-CONDITION:** At least one deviation recorded. Every deviation names a specific artifact (non-generic) and references a specific B-#.

Emit: **COMMIT-STAGE-2**

---

### STAGE 3 — ADVERSARIAL GATE

**PRE-CONDITION:** COMMIT-STAGE-2 issued. Deviation table complete.

**PROCEDURE:**

For each deviation, apply all five checks. Assign VALID or INVALID. Passing all five checks is required for GATE-CONFIRMED.

| Deviation | Check 1: Named artifact? | Check 2: B-# referenced? | Check 3: Surprise (not confirmation)? | Check 4: Design-relevant? | Check 5: Not foreknowledge? | Verdict |
|-----------|--------------------------|--------------------------|--------------------------------------|---------------------------|----------------------------|---------|

**INVARIANT V-3 (Foreknowledge):** If Check 5 fails — the finding was known before signals were gathered — the deviation is FOREKNOWLEDGE. Issue COMMIT-STAGE-3-FLAGGED and name the responsible B-# beliefs.

**SWEEP EXTENSION (mandatory):** If fewer than 2 deviations pass all 5 checks, return to Stage 2, consult additional artifacts, and repeat Stage 3. Do not emit COMMIT-STAGE-3 until minimum 2 GATE-CONFIRMED deviations are present.

Token protocol:
- Each deviation passing all checks: emit **GATE-CONFIRMED-[N]**
- Each deviation failing at least one check: emit **GATE-REJECTED-[N]**
- All Check 5 VALID: emit **COMMIT-STAGE-3-CLEAN**
- Any Check 5 INVALID: emit **COMMIT-STAGE-3-FLAGGED**

**POST-CONDITION:** All deviations have VALID/INVALID verdicts on all 5 checks. GATE-CONFIRMED-[N] or GATE-REJECTED-[N] issued for every deviation. Stage token emitted. At least 2 GATE-CONFIRMED deviations present.

---

### STAGE 4 — SURPRISE ENTRIES

**PRE-CONDITION:** COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED issued. Proceed for all GATE-CONFIRMED deviations only.

---

**FIELD REFERENCE** *(read before writing any entry)*

> **Surprise:** What turned out to be true — framed as a contradiction or refinement of a prior belief. Full sentence. Not a label; a finding.
>
> **Signal Source:** The specific artifact that revealed this surprise. Naming requirements: artifact name and/or namespace and/or date. *Prohibited phrases: "multiple sources," "the signals," "various artifacts."* Full phrase required.
>
> **Design Impact:** The specific component, API, flow, contract, or decision that must change. NOT "the system" or "the design." A named, bounded element. Full sentence required.
>
> **Build Risk:** The specific component, dependency, contract, or assumption that could break or require rework.
> - *Purpose:* names what is implicated by the change (risk-surface), not what must update (forward-looking)
> - *Paired formula:* "Design Impact names what must change; Build Risk names what is implicated by that change — a different component, dependency, or contract that could fail"
> - *Structural gloss:* one field is forward-looking (what to update); the other is risk-surface (what could break or require rework)
> - Full sentence required; must be conceptually distinct from Design Impact

---

**Surprise 0 — Calibration Entry (not a live entry; do not treat as Surprise 1)**

**Surprise:** The topic-reflect Stage 3 sweep extension was underspecified as advisory — teams reached Stage 4 with a single GATE-CONFIRMED entry because minimum-2 was positioned as a post-check note rather than a mandatory loopback exit condition, causing single-entry artifacts.

**Signal Source:** topic-reflect-golden-2026-03-14.md (quest/golden, 2026-03-14) — adversarial gate table showed 4 GATE-REJECTED out of 6 deviations; sweep extension appeared as a note below the verdict table rather than as a loopback instruction.

**Design Impact:** Stage 3 must be restructured so the sweep extension is a mandatory binary exit condition before COMMIT-STAGE-3 can be emitted — not advisory language appended after the gate table; the SKILL.md Stage 3 section requires this structural change.

**Build Risk:** The COMMIT-STAGE-4 minimum-2-entry invariant depends on Stage 3's sweep loop executing; an advisory sweep extension leaves Stage 4 without an upstream guarantee, causing Stage 5's cluster map minimum coverage to inherit the same structural deficiency.

COMMIT-ENTRY *(Surprise 0 — calibration only)*

---

**For each GATE-CONFIRMED-[N] (N = 1, 2, … in order):**

---

**Surprise [N]**

**Surprise:** [full sentence — what turned out to be true, framed as contradiction or refinement of a B-# belief]

**Signal Source:** [specific artifact: name / namespace / date — no prohibited generics]

**Design Impact:** [specific component, API, flow, or decision that must change — full sentence; NOT "the system"]

**Build Risk:** [specific component, dependency, contract, or assumption that could break — full sentence; conceptually distinct from Design Impact]

**COMMIT-ENTRY checklist:**
- ✓ **Surprise:** full sentence; frames a contradiction or surprise (not a confirmation)
- ✓ **Signal Source:** specific artifact named; does NOT contain "multiple sources," "the signals," or "various artifacts"
- ✓ **Design Impact:** specific component/API/flow/decision; NOT "the system"; full sentence
- ✓ **Build Risk:** specific component/dependency/contract/assumption; distinct from Design Impact; NOT a general risk category; full sentence
- → If any check fails: rewrite the field before emitting

Emit: **COMMIT-ENTRY**

---

*(Repeat for each GATE-CONFIRMED deviation)*

**POST-CONDITION:** All GATE-CONFIRMED deviations have entries. Minimum 2 entries. Every entry emitted COMMIT-ENTRY. Scan all dimension references — apply repair protocol for any excluded synonyms before emitting.

Emit: **COMMIT-STAGE-4**

---

### STAGE 5 — CLUSTER MAP

**PRE-CONDITION:** COMMIT-STAGE-4 issued.

Group Stage 4 surprise entries by theme. For each cluster, identify who acts next.

| Cluster | Surprise IDs | Theme | Next Team / Skill |
|---------|-------------|-------|------------------|

**POST-CONDITION:** Every cluster has a named Next Team or specific Skill — not "investigate" or generic action. All Stage 4 entries assigned to exactly one cluster.

Emit: **COMMIT-STAGE-5**

---

### STAGE 6 — SYMMETRIC CONTRACT CLOSE

**PRE-CONDITION:** COMMIT-STAGE-5 issued.

Return to Stage 1. For each B-# belief, compare the opening model expectation to what Stage 4 revealed. Assign one of three verdicts:

- **COHERENT** — evidence consistent with the belief; no surprise from this belief
- **CONTRADICTORY** — at least one GATE-CONFIRMED surprise directly contradicts this belief
- **FOREKNOWLEDGE-FLAGGED** — belief confirmed but reveals prior knowledge, not discovery

| B-# | Belief | Verdict | Revision Direction |
|-----|--------|---------|-------------------|

**Foreknowledge verdict:**
> Foreknowledge status: [ CLEAR | FOREKNOWLEDGE-FLAGGED ]
> *(If FLAGGED: name responsible B-# beliefs. Issue HALT before Stage 7.)*

**POST-CONDITION:** All B-# beliefs have verdicts. CONTRADICTORY rows have non-empty revision direction. Foreknowledge verdict explicitly stated.

Emit: **COMMIT-STAGE-6**

---

### STAGE 7 — ARTIFACT DELIVERY

**PRE-CONDITION:** COMMIT-STAGE-6 issued. Foreknowledge verdict is CLEAR. If FOREKNOWLEDGE-FLAGGED and responsible beliefs are unnamed — issue HALT. Do not enter Stage 7.

**PROCEDURE:**

Deliver the complete topic-reflect artifact:
- Topic name and date; signal namespace coverage
- All Stage 4 surprise entries (GATE-CONFIRMED only, full format)
- Stage 5 cluster map
- Stage 6 verdict table with foreknowledge verdict

**POST-CONDITION:** Artifact complete and coherent. All sections present.

Emit: **COMMIT-STAGE-7**

---

## V-02: Visual / Checklist-Heavy Format

**Axis:** Output format — every verification point is a ✓ checklist; stage transitions are visually encoded; gate conditions are scannable discrete checks, not embedded in prose.

**Hypothesis:** When every gate condition is presented as a dedicated ✓ bullet at the point of execution, compliance rates increase because the model cannot satisfy an ambiguous "looks right" heuristic — each check is a discrete binary that either clears or requires correction before the token emits.

---

You are executing **/topic-reflect** — what did we learn that we didn't expect?

Not a summary of signals. A curated list of surprises, each traced to a specific artifact and assessed for design impact. Follow the stage protocol. Issue tokens as instructed.

---

**STAGE MAP**

| # | Stage | Entry | Exit |
|---|-------|-------|------|
| 1 | Opening Model | — | COMMIT-STAGE-1 |
| 2 | Deviation Analysis | COMMIT-STAGE-1 | COMMIT-STAGE-2 |
| 3 | Adversarial Gate | COMMIT-STAGE-2 | COMMIT-STAGE-3-CLEAN / -FLAGGED |
| 4 | Surprise Entries | COMMIT-STAGE-3-* | COMMIT-STAGE-4 |
| 5 | Cluster Map | COMMIT-STAGE-4 | COMMIT-STAGE-5 |
| 6 | Verdict Table | COMMIT-STAGE-5 | COMMIT-STAGE-6 |
| 7 | Artifact Delivery | COMMIT-STAGE-6 (CLEAR) | COMMIT-STAGE-7 |

HALT: If Stage 6 records FOREKNOWLEDGE-FLAGGED without naming responsible B-# beliefs — do not enter Stage 7.

---

**VOCABULARY RULE**

The only valid epistemic dimension names are:

> **Feasibility · Usability · Scalability · Adoptability · Correctness**

No substitutes. Excluded synonyms and canonical replacements:

| Excluded | Use instead |
|----------|-------------|
| Reliability | Correctness |
| Performance | Scalability |
| Complexity | Usability |
| Maintainability | Correctness |
| Discoverability | Adoptability |

At every stage EXIT: scan for excluded synonyms. Correct before emitting any COMMIT token.

---

**⬛ STAGE 1 — OPENING MODEL**

Write the opening model *before* consulting any signal artifact.

1. State topic name + date signals were gathered.
2. Write 2–3 sentence opening model. What did you expect signals to confirm?
3. Epistemic profile (use only canonical dimension names):

   | Dimension | Pre-signal Confidence | Basis |
   |-----------|----------------------|-------|
   | Feasibility | | |
   | Usability | | |
   | Scalability | | |
   | Adoptability | | |
   | Correctness | | |

4. Beliefs (minimum 3 — each falsifiable):
   - B-1:
   - B-2:
   - B-3:

**✓ Stage 1 exit checklist:**
- ✓ Opening model written without signal consultation
- ✓ Epistemic profile: all 5 canonical dimension names used; no excluded synonyms
- ✓ At least 3 B-# beliefs; each is falsifiable and specific
- → Correct any excluded synonym before proceeding

**→ COMMIT-STAGE-1**

---

**⬛ STAGE 2 — DEVIATION ANALYSIS**

Read all signal artifacts. Record every contradiction or deviation from a B-# belief.

| Deviation # | Signal Artifact (name / namespace / date) | B-# Challenged | What deviated |
|-------------|------------------------------------------|----------------|--------------|
| D-01 | | | |

Signal Source rule: name the specific artifact. **Prohibited in all artifact fields: "multiple sources," "the signals," "various artifacts."**

**✓ Stage 2 exit checklist:**
- ✓ At least one deviation recorded
- ✓ Every deviation has a specific artifact name (non-generic)
- ✓ Every deviation references a specific B-#

**→ COMMIT-STAGE-2**

---

**⬛ STAGE 3 — ADVERSARIAL GATE**

For each deviation, apply all 5 checks. Assign VALID / INVALID. All 5 VALID = GATE-CONFIRMED.

| Deviation | Check 1: Named artifact? | Check 2: B-# referenced? | Check 3: Surprise (not confirmation)? | Check 4: Design-relevant? | Check 5: Not foreknowledge? | Verdict |
|-----------|--------------------------|--------------------------|--------------------------------------|---------------------------|----------------------------|---------|

**GATE VERDICTS:**
- All 5 VALID → **GATE-CONFIRMED-[N]**
- Any INVALID → **GATE-REJECTED-[N]**
- All Check 5 VALID → **COMMIT-STAGE-3-CLEAN**
- Any Check 5 INVALID → **COMMIT-STAGE-3-FLAGGED** *(name responsible B-# beliefs)*

**SWEEP EXTENSION (mandatory):** If fewer than 2 GATE-CONFIRMED after first pass — return to Stage 2, consult additional artifacts, repeat Stage 3 until minimum 2 GATE-CONFIRMED.

**✓ Stage 3 exit checklist:**
- ✓ All deviations have VALID/INVALID verdicts on all 5 checks
- ✓ GATE-CONFIRMED-[N] or GATE-REJECTED-[N] issued for every deviation
- ✓ COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED emitted
- ✓ At least 2 GATE-CONFIRMED deviations present

---

**⬛ STAGE 4 — SURPRISE ENTRIES**

Proceeds for all GATE-CONFIRMED deviations only.

---

**FIELD REFERENCE** *(read before writing any entry)*

> **Surprise:** What turned out to be true — contradiction or refinement of a prior belief. Full sentence.
>
> **Signal Source:** Specific artifact: name and/or namespace and/or date. *Prohibited: "multiple sources," "the signals," "various artifacts."* Full phrase.
>
> **Design Impact:** The specific component, API, flow, or decision that must change. NOT "the system." Full sentence.
>
> **Build Risk:** The component, dependency, contract, or assumption implicated by the change.
> - *Purpose:* what could break or require rework — not what must update
> - *Paired formula:* "Design Impact names what must change; Build Risk names what is implicated — a different component, dependency, or contract that could fail"
> - *Structural distinction:* Design Impact is forward-looking (what to update); Build Risk is risk-surface (what could break)
> - Full sentence; distinct from Design Impact

---

**Surprise 0 — Calibration Entry (not a live entry — do not number live entries starting from 2)**

**Surprise:** The Stage 3 sweep-extension rule was treated as advisory — teams exited with one GATE-CONFIRMED entry because the minimum-2 requirement appeared as a note below the gate table, not as a mandatory loopback exit condition.

**Signal Source:** topic-reflect-golden-2026-03-14.md (quest/golden, 2026-03-14) — gate table showed 4 GATE-REJECTED out of 6; sweep extension appeared as a post-table note rather than a binary exit condition.

**Design Impact:** Stage 3's sweep extension must be rewritten as a mandatory loopback rule in the EXIT condition before COMMIT-STAGE-3 can be issued — the SKILL.md Stage 3 section requires restructuring.

**Build Risk:** The COMMIT-STAGE-4 minimum-2-entry invariant depends on Stage 3's loopback executing correctly; an advisory sweep creates no upstream guarantee, leaving Stage 5's cluster map minimum coverage with no structural backing.

**✓ COMMIT-ENTRY (Surprise 0 — calibration only)**

---

**For each GATE-CONFIRMED-[N]:**

---

**Surprise [N]**

**Surprise:** [full sentence — what turned out to be true]

**Signal Source:** [specific artifact: name / namespace / date]

**Design Impact:** [specific component, API, flow, or decision — NOT "the system"; full sentence]

**Build Risk:** [specific component, dependency, contract, or assumption — distinct from Design Impact; full sentence]

**✓ COMMIT-ENTRY checklist:**
- ✓ **Surprise:** full sentence; contradiction or surprise (not confirmation)
- ✓ **Signal Source:** specific artifact; none of: "multiple sources" / "the signals" / "various artifacts"
- ✓ **Design Impact:** named component/API/flow/decision; NOT "the system"; full sentence
- ✓ **Build Risk:** named component/dependency/contract/assumption; distinct from Design Impact; NOT a general risk category; full sentence
- → Rewrite any failing field before emitting

**→ COMMIT-ENTRY**

---

*(Repeat for each GATE-CONFIRMED deviation)*

**✓ Stage 4 exit checklist:**
- ✓ All GATE-CONFIRMED deviations have entries
- ✓ At least 2 entries present
- ✓ Every entry emitted COMMIT-ENTRY
- ✓ No excluded dimension synonyms anywhere — correct before proceeding

**→ COMMIT-STAGE-4**

---

**⬛ STAGE 5 — CLUSTER MAP**

Group Stage 4 surprise entries by theme. Identify who acts next.

| Cluster | Surprise IDs | Theme | Next Team / Skill |
|---------|-------------|-------|------------------|

**✓ Stage 5 exit checklist:**
- ✓ Every cluster has a named Next Team or specific Skill — NOT "investigate"
- ✓ All Stage 4 entries assigned to exactly one cluster

**→ COMMIT-STAGE-5**

---

**⬛ STAGE 6 — VERDICT TABLE**

Return to Stage 1 beliefs. Compare each to Stage 4 discoveries. Assign:
- **COHERENT** — evidence consistent with the belief
- **CONTRADICTORY** — at least one GATE-CONFIRMED surprise directly contradicts
- **FOREKNOWLEDGE-FLAGGED** — belief confirmed but reveals prior knowledge

| B-# | Belief | Verdict | Revision Direction |
|-----|--------|---------|-------------------|

Foreknowledge verdict:
> Foreknowledge status: [ CLEAR | FOREKNOWLEDGE-FLAGGED ]
> *(If FLAGGED: name responsible B-# beliefs. Issue HALT before Stage 7.)*

**✓ Stage 6 exit checklist:**
- ✓ All B-# beliefs have verdicts
- ✓ CONTRADICTORY rows have non-empty revision direction
- ✓ Foreknowledge verdict explicitly stated
- ✓ If FLAGGED: responsible beliefs named

**→ COMMIT-STAGE-6**

---

**⬛ STAGE 7 — ARTIFACT DELIVERY**

ENTER: COMMIT-STAGE-6 issued. Foreknowledge verdict CLEAR. If FOREKNOWLEDGE-FLAGGED without named responsible beliefs — HALT.

Deliver the complete topic-reflect artifact: topic and date, all Stage 4 surprise entries (full format), Stage 5 cluster map, Stage 6 verdict table with foreknowledge verdict.

**✓ Stage 7 exit checklist:**
- ✓ All Stage 4 entries included with all sub-fields
- ✓ Cluster map and verdict table complete
- ✓ Foreknowledge verdict stated

**→ COMMIT-STAGE-7**

---

## V-03: Three Named Roles

**Axis:** Role sequence — three named roles activate in explicit sequence, with visible handoff points and role-specific exit conditions.

**Hypothesis:** Named role personas create structural commitment — the model cannot elide a stage because abandoning it requires abandoning a named role. Role boundaries make stage handoffs explicit verification points where the model must confirm the prior role's work before the next activates.

---

You are executing **topic-reflect** — synthesis of institutional surprises after signal gathering.

The question: *What did we learn that we did not expect?*

Three roles execute in sequence. Each role activates at an explicit marker. Each role owns its stages and does not proceed until its exit condition is satisfied.

---

**EXECUTION ROLES**

| Role | Stages | Responsibility |
|------|--------|----------------|
| **HISTORIAN** | Stage 1–2 | Build the opening model from prior expectation. Read artifacts. Record deviations. |
| **ADVERSARY** | Stage 3 | Challenge every deviation with full skepticism. Issue gate verdicts. Let nothing through without VALID on all 5 checks. |
| **NARRATOR** | Stage 4–7 | Write the surprise entries. Cluster them. Close the symmetric contract. Deliver the artifact. |

**GATE SEQUENCE:**
`— → COMMIT-STAGE-1 → COMMIT-STAGE-2 → COMMIT-STAGE-3-CLEAN/FLAGGED → [GATE-CONFIRMED-N / GATE-REJECTED-N per deviation] → COMMIT-STAGE-4 → COMMIT-STAGE-5 → COMMIT-STAGE-6 → COMMIT-STAGE-7`

HALT: If Stage 6 records FOREKNOWLEDGE-FLAGGED without naming responsible B-# beliefs — issue HALT. Do not enter Stage 7.

---

**VOCABULARY CONTRACT**

The only valid epistemic dimension names are:

> **Feasibility · Usability · Scalability · Adoptability · Correctness**

Substitution prohibited. Excluded synonyms with canonical replacements:

| Excluded | Replace with |
|----------|-------------|
| Reliability | Correctness |
| Performance | Scalability |
| Complexity | Usability |
| Maintainability | Correctness |
| Discoverability | Adoptability |

At every role EXIT: scan for excluded synonyms. Correct using the replacement table before emitting any COMMIT token.

---

**→ HISTORIAN ACTIVATES**

---

**Stage 1 — Opening Model**

The HISTORIAN writes the opening model *before reading any signal artifact*.

1. State topic name and date signals were gathered.

2. Write 2–3 sentence opening model. What did you expect the signals to confirm? Write from prior expectation only.

3. Epistemic profile (use only canonical dimension names):

   | Dimension | Pre-signal Confidence | Basis |
   |-----------|----------------------|-------|
   | Feasibility | | |
   | Usability | | |
   | Scalability | | |
   | Adoptability | | |
   | Correctness | | |

4. Beliefs (minimum 3 — each falsifiable and specific):
   - B-1:
   - B-2:
   - B-3:

HISTORIAN exit condition: opening model written without signal consultation; 3+ B-# beliefs; all 5 canonical dimension names present; no excluded synonyms (correct before proceeding).

Emit: **COMMIT-STAGE-1**

---

**Stage 2 — Deviation Analysis**

The HISTORIAN now reads signal artifacts. Record every contradiction or deviation from a B-# belief.

| Deviation # | Signal Artifact (name / namespace / date) | B-# Challenged | What deviated |
|-------------|------------------------------------------|----------------|--------------|
| D-01 | | | |

Signal Source rule: name the specific artifact. **Prohibited in all artifact fields: "multiple sources," "the signals," "various artifacts."**

HISTORIAN exit condition: at least one deviation recorded; every deviation has a specific named artifact and a B-# reference.

Emit: **COMMIT-STAGE-2**

---

**→ ADVERSARY ACTIVATES**

---

**Stage 3 — Adversarial Gate**

The ADVERSARY challenges every deviation. Apply all 5 checks. All 5 VALID = GATE-CONFIRMED. Any INVALID = GATE-REJECTED. The ADVERSARY does not let a surprise through on reputation; every check must clear independently.

| Deviation | Check 1: Named artifact? | Check 2: B-# referenced? | Check 3: Surprise (not confirmation)? | Check 4: Design-relevant? | Check 5: Not foreknowledge? | Verdict |
|-----------|--------------------------|--------------------------|--------------------------------------|---------------------------|----------------------------|---------|

ADVERSARY token protocol:
- Each deviation passing all checks: emit **GATE-CONFIRMED-[N]**
- Each deviation failing any check: emit **GATE-REJECTED-[N]**
- All Check 5 VALID: emit **COMMIT-STAGE-3-CLEAN**
- Any Check 5 INVALID: emit **COMMIT-STAGE-3-FLAGGED** *(name responsible B-# beliefs)*

SWEEP EXTENSION (mandatory): if fewer than 2 GATE-CONFIRMED after first pass, the ADVERSARY sends the work back to the HISTORIAN for additional artifact review. Repeat until minimum 2 GATE-CONFIRMED. Do not emit the stage token until minimum 2 GATE-CONFIRMED.

ADVERSARY exit condition: all deviations have verdicts; stage token issued; at least 2 GATE-CONFIRMED.

---

**→ NARRATOR ACTIVATES**

---

**Stage 4 — Surprise Entries**

The NARRATOR writes surprise entries for all GATE-CONFIRMED deviations.

---

**FIELD REFERENCE** *(NARRATOR reads before writing any entry)*

> **Surprise:** What turned out to be true — framed as a contradiction or refinement of a prior belief. Full sentence. Not a label; a finding.
>
> **Signal Source:** The specific artifact that revealed this surprise. Name: artifact name and/or namespace and/or date. *Prohibited: "multiple sources," "the signals," "various artifacts."* Full phrase.
>
> **Design Impact:** The specific component, API, flow, or decision that must change. NOT "the system." Full sentence.
>
> **Build Risk:** What is implicated by the change.
> - *Purpose:* names what could break or require rework — not what must update
> - *Paired formula:* "Design Impact names what must change; Build Risk names what is implicated — a different component, dependency, or contract that could fail"
> - *Structural distinction:* Design Impact is forward-looking (what to update); Build Risk is risk-surface (what could break)
> - Full sentence; conceptually distinct from Design Impact

---

**Surprise 0 — Calibration Entry (not a live entry — NARRATOR treats this as example only; live entries begin at Surprise 1)**

**Surprise:** The topic-reflect Stage 3 sweep extension was treated as advisory — teams reached Stage 4 with a single GATE-CONFIRMED entry because the mandatory loopback was positioned as a note after the gate table rather than as an exit condition before the stage token.

**Signal Source:** topic-reflect-golden-2026-03-14.md (quest/golden, 2026-03-14) — gate table recorded 4 GATE-REJECTED out of 6; sweep extension appeared as a note below the table, after COMMIT-STAGE-3 emission instructions.

**Design Impact:** Stage 3's loopback rule must become a mandatory binary exit condition before COMMIT-STAGE-3 emission — the SKILL.md Stage 3 section must be restructured to make minimum-2-GATE-CONFIRMED an exit requirement, not a note.

**Build Risk:** Stage 5's cluster map requires minimum coverage of all Stage 4 entries; a single-entry Stage 4 output makes the cluster map trivially satisfiable but structurally deficient, and the COMMIT-STAGE-5 exit condition has no upstream guarantee to enforce against.

COMMIT-ENTRY *(Surprise 0 — calibration only)*

---

**For each GATE-CONFIRMED-[N] (NARRATOR writes):**

---

**Surprise [N]**

**Surprise:** [full sentence — contradiction or surprising refinement of a prior belief]

**Signal Source:** [specific artifact: name / namespace / date — no prohibited generics]

**Design Impact:** [specific component, API, flow, or decision — full sentence; NOT "the system"]

**Build Risk:** [specific component, dependency, contract, or assumption — full sentence; distinct from Design Impact]

**COMMIT-ENTRY checklist:**
- ✓ Surprise: full sentence; contradiction or surprise (not confirmation)
- ✓ Signal Source: specific artifact; none of "multiple sources" / "the signals" / "various artifacts"
- ✓ Design Impact: specific component/API/flow/decision; NOT "the system"; full sentence
- ✓ Build Risk: specific component/dependency/contract/assumption; distinct from Design Impact; NOT a general risk category; full sentence
- → Rewrite any failing field before emitting

Emit: **COMMIT-ENTRY**

---

*(Repeat for each GATE-CONFIRMED deviation)*

NARRATOR exit condition: all GATE-CONFIRMED deviations have entries; minimum 2; every entry emitted COMMIT-ENTRY; no excluded dimension synonyms.

Emit: **COMMIT-STAGE-4**

---

**Stage 5 — Cluster Map**

NARRATOR groups Stage 4 surprise entries by theme. Identifies who acts next.

| Cluster | Surprise IDs | Theme | Next Team / Skill |
|---------|-------------|-------|------------------|

NARRATOR exit condition: every cluster has a named Next Team or specific Skill (not "investigate"); all entries assigned to exactly one cluster.

Emit: **COMMIT-STAGE-5**

---

**Stage 6 — Symmetric Contract Close**

NARRATOR returns to Stage 1 beliefs. For each B-#, compare to what Stage 4 revealed. Assign:
- **COHERENT** — evidence consistent with the belief
- **CONTRADICTORY** — at least one GATE-CONFIRMED surprise directly contradicts
- **FOREKNOWLEDGE-FLAGGED** — belief confirmed but reveals prior knowledge, not discovery

| B-# | Belief | Verdict | Revision Direction |
|-----|--------|---------|-------------------|

Foreknowledge verdict:
> Foreknowledge status: [ CLEAR | FOREKNOWLEDGE-FLAGGED ]
> *(If FLAGGED: name responsible B-# beliefs. Issue HALT before Stage 7.)*

NARRATOR exit condition: all B-# beliefs have verdicts; CONTRADICTORY rows have revision direction; foreknowledge verdict explicitly stated.

Emit: **COMMIT-STAGE-6**

---

**Stage 7 — Artifact Delivery**

ENTER: COMMIT-STAGE-6 issued. Foreknowledge verdict CLEAR. If FOREKNOWLEDGE-FLAGGED without named responsible beliefs — HALT. Do not proceed.

NARRATOR delivers the complete topic-reflect artifact: topic and date context, all Stage 4 surprise entries (GATE-CONFIRMED), Stage 5 cluster map, Stage 6 verdict table with foreknowledge verdict.

NARRATOR exit condition: complete artifact delivered; all sections present.

Emit: **COMMIT-STAGE-7**

---

## V-04: Lifecycle Emphasis

**Axis:** Lifecycle emphasis — ENTER conditions and EXIT criteria are the primary organizational structure; each stage is introduced as a lifecycle contract; procedures are subordinate to pre/post-condition framing.

**Hypothesis:** When ENTER conditions are as structurally prominent as EXIT criteria, premature stage entry is prevented at the same level as undercompleted stage exit. Symmetric visibility of pre- and post-conditions reduces drift caused by the model advancing before entry requirements are satisfied.

---

You are executing **topic-reflect** — institutional surprise synthesis.

The question: *What did we learn that we did not expect?*

Each stage in this protocol is a **lifecycle unit**: it has an ENTER condition you must satisfy before beginning, a PROCEDURE for what to do, and an EXIT criterion you must satisfy before emitting the stage token. You may not enter a stage until its ENTER condition is satisfied. You may not leave until its EXIT criterion is satisfied.

---

**LIFECYCLE MAP**

| Stage | ENTER Condition | EXIT Criterion | Token |
|-------|----------------|----------------|-------|
| 1 | Signals gathered; no signal consulted yet | Opening model complete; 3+ B-# beliefs; 5 canonical dimension names | COMMIT-STAGE-1 |
| 2 | COMMIT-STAGE-1 emitted | 1+ deviations; every deviation has named artifact + B-# | COMMIT-STAGE-2 |
| 3 | COMMIT-STAGE-2 emitted | All deviations verdicted; 2+ GATE-CONFIRMED; stage token emitted | COMMIT-STAGE-3-CLEAN / -FLAGGED |
| 4 | COMMIT-STAGE-3-* emitted | All GATE-CONFIRMED entries written; 2+ entries; each passed COMMIT-ENTRY | COMMIT-STAGE-4 |
| 5 | COMMIT-STAGE-4 emitted | Cluster map complete; all entries assigned; every cluster has named Next Team/Skill | COMMIT-STAGE-5 |
| 6 | COMMIT-STAGE-5 emitted | All B-# beliefs verdicted; foreknowledge verdict stated | COMMIT-STAGE-6 |
| 7 | COMMIT-STAGE-6 emitted; verdict CLEAR | Artifact delivered; all sections present | COMMIT-STAGE-7 |

HALT: Stage 7 ENTER requires FOREKNOWLEDGE verdict CLEAR. If FOREKNOWLEDGE-FLAGGED and responsible B-# beliefs are unnamed — issue HALT.

---

**VOCABULARY LIFECYCLE RULE**

This rule applies at every stage EXIT as a pre-emission check.

The only valid epistemic dimension names: **Feasibility · Usability · Scalability · Adoptability · Correctness**

Substitution prohibited. Excluded synonyms with canonical replacements:

| Excluded | Replace with |
|----------|-------------|
| Reliability | Correctness |
| Performance | Scalability |
| Complexity | Usability |
| Maintainability | Correctness |
| Discoverability | Adoptability |

EXIT lifecycle check: before emitting any stage COMMIT token, scan all dimension cells. If a prohibited synonym appears, apply the mapping table. Do not emit until all cells are clean.

---

**STAGE 1 — OPENING MODEL**

**ENTER:** Signal artifacts have been gathered. You have not yet consulted them. Enter Stage 1 only in this pre-read state.

**PROCEDURE:**

1. State topic name and date signals were gathered.
2. Write 2–3 sentence opening model — what did you expect signals to confirm? Write from prior expectation without consulting any artifact.
3. Epistemic profile (complete all 5 rows; use only canonical dimension names):

   | Dimension | Pre-signal Confidence | Basis |
   |-----------|----------------------|-------|
   | Feasibility | | |
   | Usability | | |
   | Scalability | | |
   | Adoptability | | |
   | Correctness | | |

4. Beliefs (minimum 3 — each falsifiable):
   - B-1:
   - B-2:
   - B-3:

**EXIT:** Opening model was written before signal consultation (verify). Epistemic profile complete with all 5 canonical dimension names; no excluded synonyms (apply mapping if needed). At least 3 B-# beliefs recorded.

Emit: **COMMIT-STAGE-1**

---

**STAGE 2 — DEVIATION ANALYSIS**

**ENTER:** COMMIT-STAGE-1 emitted. Signal artifacts may now be consulted.

**PROCEDURE:**

Read all gathered signal artifacts. For each, determine whether it confirms, partially confirms, or contradicts a B-# belief. Record contradictions and deviations.

| Deviation # | Signal Artifact (name / namespace / date) | B-# Challenged | What deviated |
|-------------|------------------------------------------|----------------|--------------|
| D-01 | | | |

Signal Source rule: every artifact reference must name a specific artifact. Prohibited phrases in all artifact fields: "multiple sources," "the signals," "various artifacts."

**EXIT:** At least one deviation recorded. Every deviation has a specific named artifact (non-generic) and a referenced B-#.

Emit: **COMMIT-STAGE-2**

---

**STAGE 3 — ADVERSARIAL GATE**

**ENTER:** COMMIT-STAGE-2 emitted. Deviation table complete.

**PROCEDURE:**

Apply all 5 checks to every deviation. Assign VALID or INVALID per check.

| Deviation | Check 1: Named artifact? | Check 2: B-# referenced? | Check 3: Surprise? | Check 4: Design-relevant? | Check 5: Not foreknowledge? | Verdict |
|-----------|--------------------------|--------------------------|-------------------|---------------------------|----------------------------|---------|

Token protocol:
- All 5 VALID: **GATE-CONFIRMED-[N]**; routes to Stage 4 entry N
- Any INVALID: **GATE-REJECTED-[N]**
- All Check 5 VALID: **COMMIT-STAGE-3-CLEAN**
- Any Check 5 INVALID: **COMMIT-STAGE-3-FLAGGED** *(name responsible B-# beliefs)*

Sweep extension (mandatory): if fewer than 2 GATE-CONFIRMED after first pass — return to Stage 2 ENTER, consult additional artifacts, repeat Stage 3. Do not emit stage token until minimum 2 GATE-CONFIRMED. The minimum-2 requirement is an EXIT criterion, not an advisory note.

**EXIT:** All deviations have VALID/INVALID verdicts on all 5 checks. Every deviation has a GATE-CONFIRMED-[N] or GATE-REJECTED-[N]. COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED emitted. At least 2 GATE-CONFIRMED deviations present.

---

**STAGE 4 — SURPRISE ENTRIES**

**ENTER:** COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED emitted. Proceed for GATE-CONFIRMED deviations only.

---

**FIELD REFERENCE** *(read before entering the entry loop)*

> **Surprise:** What turned out to be true — contradiction or refinement of a prior belief. Full sentence. Not a label; a finding.
>
> **Signal Source:** Specific artifact: name and/or namespace and/or date. *Prohibited phrases: "multiple sources," "the signals," "various artifacts."* Full phrase.
>
> **Design Impact:** The specific component, API, flow, or decision that must change. NOT "the system." Full sentence.
>
> **Build Risk:** The component, dependency, contract, or assumption implicated by the change.
> - *Purpose:* captures what is implicated (risk-surface), not what must update (forward-looking)
> - *Paired formula:* "Design Impact names what must change; Build Risk names what is implicated by that change — a different component, dependency, or contract that could fail"
> - *Structural distinction:* Design Impact is forward-looking (what to update); Build Risk is risk-surface (what could break or require rework)
> - Full sentence; conceptually distinct from Design Impact

---

**Surprise 0 — Calibration Entry (not a live entry — example only; live entries begin at Surprise 1)**

**Surprise:** The topic-reflect Stage 3 sweep extension was advisory rather than a lifecycle exit condition — teams proceeded to Stage 4 with one GATE-CONFIRMED entry because minimum-2 was positioned as a post-gate note rather than an EXIT criterion that blocked stage token emission.

**Signal Source:** topic-reflect-golden-2026-03-14.md (quest/golden, 2026-03-14) — gate table showed 4 GATE-REJECTED out of 6; sweep extension note appeared after the gate verdicts, not as a precondition for COMMIT-STAGE-3 emission.

**Design Impact:** Stage 3's sweep extension must be promoted from an advisory note to a mandatory EXIT criterion — minimum-2-GATE-CONFIRMED must block COMMIT-STAGE-3 emission, not merely suggest additional review after the token is issued.

**Build Risk:** The COMMIT-STAGE-4 EXIT criterion has a direct dependency on Stage 3's loop executing correctly; if Stage 3 emits without the sweep enforcement, Stage 4's minimum-2-entry EXIT criterion inherits the gap and Stage 5's cluster map minimum has no upstream structural backing.

COMMIT-ENTRY *(Surprise 0 — calibration only)*

---

**PROCEDURE (entry loop):**

For each GATE-CONFIRMED-[N], write the following entry:

---

**Surprise [N]**

**Surprise:** [full sentence — what turned out to be true, contradiction or surprise refinement]

**Signal Source:** [specific artifact: name / namespace / date — no prohibited generics]

**Design Impact:** [specific component, API, flow, or decision — full sentence; NOT "the system"]

**Build Risk:** [specific component, dependency, contract, or assumption — full sentence; distinct from Design Impact]

**COMMIT-ENTRY checklist:**
- ✓ Surprise: full sentence; contradiction or surprise (not confirmation)
- ✓ Signal Source: specific artifact; no "multiple sources" / "the signals" / "various artifacts"
- ✓ Design Impact: named component/API/flow/decision; NOT "the system"; full sentence
- ✓ Build Risk: named component/dependency/contract/assumption; distinct from Design Impact; NOT a general risk category; full sentence
- → If any fails: rewrite before emitting

Emit: **COMMIT-ENTRY**

---

*(Repeat for each GATE-CONFIRMED deviation)*

**EXIT:** All GATE-CONFIRMED deviations have entries. Minimum 2 entries. Every entry emitted COMMIT-ENTRY. No excluded dimension synonyms — apply vocabulary lifecycle rule before emitting.

Emit: **COMMIT-STAGE-4**

---

**STAGE 5 — CLUSTER MAP**

**ENTER:** COMMIT-STAGE-4 emitted.

**PROCEDURE:**

Group Stage 4 surprise entries by theme. For each cluster, identify who acts next.

| Cluster | Surprise IDs | Theme | Next Team / Skill |
|---------|-------------|-------|------------------|

**EXIT:** Every cluster has a named Next Team or specific Skill — not "investigate." All Stage 4 entries assigned to exactly one cluster.

Emit: **COMMIT-STAGE-5**

---

**STAGE 6 — SYMMETRIC CONTRACT CLOSE**

**ENTER:** COMMIT-STAGE-5 emitted.

**PROCEDURE:**

Return to Stage 1 B-# beliefs. Compare each to what Stage 4 revealed. Assign:
- **COHERENT** — evidence consistent with the belief; no surprise
- **CONTRADICTORY** — at least one GATE-CONFIRMED surprise directly contradicts
- **FOREKNOWLEDGE-FLAGGED** — belief confirmed but confirms prior knowledge, not discovery

| B-# | Belief | Verdict | Revision Direction |
|-----|--------|---------|-------------------|

Foreknowledge verdict:
> Foreknowledge status: [ CLEAR | FOREKNOWLEDGE-FLAGGED ]
> *(If FLAGGED: name responsible B-# beliefs. Issue HALT before Stage 7.)*

**EXIT:** All B-# beliefs have verdicts. CONTRADICTORY rows have revision direction. Foreknowledge verdict explicitly stated.

Emit: **COMMIT-STAGE-6**

---

**STAGE 7 — ARTIFACT DELIVERY**

**ENTER:** COMMIT-STAGE-6 emitted. Foreknowledge verdict is CLEAR. If FOREKNOWLEDGE-FLAGGED and responsible beliefs are unnamed — issue HALT. Do not enter Stage 7.

**PROCEDURE:**

Deliver the complete topic-reflect artifact: topic name and date, all Stage 4 surprise entries (GATE-CONFIRMED, full format), Stage 5 cluster map, Stage 6 verdict table with foreknowledge verdict.

**EXIT:** Artifact complete. All Stage 4 entries present. Cluster map and verdict table included. Foreknowledge verdict stated.

Emit: **COMMIT-STAGE-7**

---

## V-05: Combined + B-# Belief Anchor Sub-field

**Axis:** Combined — formal field definitions (V-01) + visual checklist gates (V-02) + lifecycle contracts (V-04) + explicit `What We Expected (B-[#])` sub-field as first labeled item in Stage 4 entry template.

**Hypothesis:** An explicit `What We Expected (B-[#])` sub-field as the first labeled item in the Stage 4 entry template converts B-# belief traceability from an inferred structural property — carried implicitly through the deviation chain (Stage 2 records B-#, GATE-CONFIRMED-N routes to entry N) — into a per-entry structural requirement enforced at three convergent points: field presence in the template, calibration demonstration in Surprise 0, and explicit verification in the per-entry EXIT gate. Making belief contradiction the *first thing recorded* per entry prevents the chain from silently breaking when entry numbering, sweep extension, or reordering disrupts the implicit routing assumption.

---

You are executing **topic-reflect** — the institutional memory skill.

The question: *What did we learn that we did not expect?*

Each surprise must be traced to a specific signal artifact, grounded in a specific prior belief, and assessed for its impact on design direction. The artifact is not a summary — it is a curated map from prior expectation to discovered reality.

---

**GATE OVERVIEW**

| Stage | Entry Condition | Exit Token | Halt Condition |
|-------|----------------|------------|----------------|
| Stage 1 | Signals gathered; no signal consulted | COMMIT-STAGE-1 | <3 beliefs; opening model incomplete |
| Stage 2 | COMMIT-STAGE-1 | COMMIT-STAGE-2 | No deviations recorded |
| Stage 3 | COMMIT-STAGE-2 | COMMIT-STAGE-3-CLEAN / -FLAGGED | <2 GATE-CONFIRMED after sweep |
| Stage 4 | COMMIT-STAGE-3-* | COMMIT-STAGE-4 | GATE-CONFIRMED entries < 2 |
| Stage 5 | COMMIT-STAGE-4 | COMMIT-STAGE-5 | Cluster missing Next Team/Skill |
| Stage 6 | COMMIT-STAGE-5 | COMMIT-STAGE-6 | B-# beliefs without verdicts |
| Stage 7 | COMMIT-STAGE-6 (CLEAR only) | COMMIT-STAGE-7 | FOREKNOWLEDGE-FLAGGED unresolved |

HALT: If Stage 6 records FOREKNOWLEDGE-FLAGGED without naming responsible B-# beliefs — issue HALT. Do not enter Stage 7.

---

**VOCABULARY INVARIANT**

The epistemic dimension vocabulary is a closed set. The only valid names are:

> **Feasibility · Usability · Scalability · Adoptability · Correctness**

Substitution prohibited. Named excluded synonyms and canonical replacements:

| Excluded | Canonical |
|----------|-----------|
| Reliability | → Correctness |
| Performance | → Scalability |
| Complexity | → Usability |
| Maintainability | → Correctness |
| Discoverability | → Adoptability |

**Self-repair rule:** At every EXIT gate, scan all dimension cells. If a prohibited synonym is detected, correct it using the mapping table above before emitting the stage COMMIT token. This is an active runtime repair protocol — not a review note.

---

**STAGE 1 — OPENING MODEL**

**ENTER:** Signal artifacts have been gathered for the topic. You have not yet consulted them. Enter Stage 1 only in this pre-read state.

**PROCEDURE:**

1. State topic name and the date signals were gathered.
2. Write 2–3 sentence opening model — what did you expect signals to confirm? Write without consulting signals.
3. Epistemic profile (complete all 5 rows; use only canonical dimension names):

   | Dimension | Pre-signal Confidence | Basis |
   |-----------|----------------------|-------|
   | Feasibility | | |
   | Usability | | |
   | Scalability | | |
   | Adoptability | | |
   | Correctness | | |

4. Beliefs (minimum 3 — each falsifiable and specific):
   - B-1:
   - B-2:
   - B-3:

**EXIT:**
- ✓ Opening model written without signal consultation
- ✓ Epistemic profile: all 5 canonical dimension names; no excluded synonyms
- ✓ At least 3 B-# beliefs; each falsifiable
- → Correct any excluded synonym before emitting

Emit: **COMMIT-STAGE-1**

---

**STAGE 2 — DEVIATION ANALYSIS**

**ENTER:** COMMIT-STAGE-1 emitted. Signal artifacts may now be consulted.

**PROCEDURE:**

Read all gathered signal artifacts. Record every contradiction or deviation from a B-# belief.

| Deviation # | Signal Artifact (name / namespace / date) | B-# Challenged | What deviated |
|-------------|------------------------------------------|----------------|--------------|
| D-01 | | | |

**Signal Source invariant:** Every artifact reference must name a specific artifact. Prohibited phrases in all artifact fields: "multiple sources," "the signals," "various artifacts."

**EXIT:**
- ✓ At least one deviation recorded
- ✓ Every deviation names a specific artifact (non-generic)
- ✓ Every deviation references a specific B-#

Emit: **COMMIT-STAGE-2**

---

**STAGE 3 — ADVERSARIAL GATE**

**ENTER:** COMMIT-STAGE-2 emitted. Deviation table complete.

**PROCEDURE:**

Apply all 5 checks to every deviation. Assign VALID or INVALID per check.

| Deviation | Check 1: Named artifact? | Check 2: B-# referenced? | Check 3: Surprise (not confirmation)? | Check 4: Design-relevant? | Check 5: Not foreknowledge? | Verdict |
|-----------|--------------------------|--------------------------|--------------------------------------|---------------------------|----------------------------|---------|

Token protocol:
- All 5 VALID: emit **GATE-CONFIRMED-[N]**
- Any INVALID: emit **GATE-REJECTED-[N]**
- All Check 5 VALID: emit **COMMIT-STAGE-3-CLEAN**
- Any Check 5 INVALID: emit **COMMIT-STAGE-3-FLAGGED** *(name responsible B-# beliefs)*

Sweep extension (mandatory): if fewer than 2 GATE-CONFIRMED after first pass — return to Stage 2, consult additional artifacts, repeat Stage 3. Do not emit COMMIT-STAGE-3 until minimum 2 GATE-CONFIRMED.

**EXIT:**
- ✓ All deviations have VALID/INVALID verdicts on all 5 checks
- ✓ GATE-CONFIRMED-[N] or GATE-REJECTED-[N] issued for every deviation
- ✓ COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED emitted
- ✓ At least 2 GATE-CONFIRMED deviations present

---

**STAGE 4 — SURPRISE ENTRIES**

**ENTER:** COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED emitted. Proceed for all GATE-CONFIRMED deviations only.

---

**FIELD REFERENCE** *(read before writing any entry)*

> **What We Expected (B-[#]):** The specific belief from Stage 1 that this surprise contradicts or refines. Write as a full sentence: "We expected that [B-# statement]." Must reference a specific B-# from Stage 1 by number. *Prohibited:* generic belief statements ("we expected this to work," "we thought it would be straightforward"), restatements of the Surprise field, or paraphrases without a named B-#.
>
> **Surprise:** What turned out to be true — framed as a contradiction or refinement of the belief in What We Expected. Full sentence. Not a label; a finding.
>
> **Signal Source:** The specific artifact that revealed this surprise. Name: artifact name and/or namespace and/or date. *Prohibited phrases: "multiple sources," "the signals," "various artifacts."* Full phrase.
>
> **Design Impact:** The specific component, API, flow, contract, or decision that must change. NOT "the system" or "the design." Full sentence.
>
> **Build Risk:** The specific component, dependency, contract, or assumption that could break or require rework.
> - *Purpose:* names what is implicated by the change (risk-surface), not what must update (forward-looking)
> - *Paired formula:* "Design Impact names what must change; Build Risk names what is implicated by that change — a different component, dependency, or contract that could fail"
> - *Structural distinction:* Design Impact is forward-looking (what to update); Build Risk is risk-surface (what could break or require rework)
> - Full sentence; must be conceptually distinct from Design Impact

---

**Surprise 0 — Calibration Entry (not a live entry — do not treat as Surprise 1; live entries begin at Surprise 1)**

**What We Expected (B-2):** We expected that the Stage 3 adversarial gate would enforce the minimum-2-surprise requirement automatically because the gate table structure made the exit condition visible — the minimum-2 check was assumed to be enforced by the surrounding gate logic without requiring an explicit loopback instruction.

**Surprise:** The sweep extension was treated as advisory — teams reached Stage 4 with a single GATE-CONFIRMED entry because minimum-2 was positioned as a note after the gate table rather than as a mandatory exit condition that blocked COMMIT-STAGE-3 emission.

**Signal Source:** topic-reflect-golden-2026-03-14.md (quest/golden, 2026-03-14) — gate table showed 4 GATE-REJECTED out of 6 deviations; sweep extension appeared as a note below the verdict table, after COMMIT-STAGE-3 emission instructions.

**Design Impact:** Stage 3 must be restructured so the sweep extension is a mandatory binary EXIT condition before COMMIT-STAGE-3 can be emitted — the SKILL.md Stage 3 section requires the minimum-2-GATE-CONFIRMED requirement to appear as an EXIT criterion, not as advisory post-gate guidance.

**Build Risk:** The COMMIT-STAGE-4 minimum-2-entry invariant has no upstream structural guarantee if Stage 3's sweep loopback is optional; Stage 5's cluster map minimum coverage requirement inherits the same gap and cannot be structurally enforced without Stage 3 backing it.

COMMIT-ENTRY *(Surprise 0 — calibration only)*

---

**For each GATE-CONFIRMED-[N] (N = 1, 2, … in order):**

---

**Surprise [N]**

**What We Expected (B-[#]):** [full sentence — "We expected that [B-# statement]" — references a specific B-# from Stage 1; NOT a generic belief or restatement of Surprise]

**Surprise:** [full sentence — what turned out to be true, framed as contradiction or refinement of the belief above]

**Signal Source:** [specific artifact: name / namespace / date — no prohibited generics]

**Design Impact:** [specific component, API, flow, or decision — full sentence; NOT "the system"]

**Build Risk:** [specific component, dependency, contract, or assumption — full sentence; distinct from Design Impact]

**✓ COMMIT-ENTRY checklist:**
- ✓ **What We Expected (B-[#]):** full sentence beginning "We expected that..."; references a specific B-# from Stage 1 by number; NOT a generic belief or restatement of Surprise → if absent or generic: write a specific belief sentence referencing the correct B-# before emitting
- ✓ **Surprise:** full sentence; frames a contradiction or surprise refinement (not a confirmation)
- ✓ **Signal Source:** specific artifact named; does NOT contain "multiple sources," "the signals," or "various artifacts"
- ✓ **Design Impact:** specific component/API/flow/decision; NOT "the system"; full sentence
- ✓ **Build Risk:** specific component/dependency/contract/assumption; distinct from Design Impact; NOT a general risk category; full sentence
- → Rewrite any failing field before emitting

Emit: **COMMIT-ENTRY**

---

*(Repeat for each GATE-CONFIRMED deviation)*

**EXIT:**
- ✓ All GATE-CONFIRMED deviations have entries
- ✓ Minimum 2 entries
- ✓ Every entry emitted COMMIT-ENTRY
- ✓ No excluded dimension synonyms — apply self-repair rule before emitting

Emit: **COMMIT-STAGE-4**

---

**STAGE 5 — CLUSTER MAP**

**ENTER:** COMMIT-STAGE-4 emitted.

Group Stage 4 surprise entries by theme. Identify who acts next.

| Cluster | Surprise IDs | Theme | Next Team / Skill |
|---------|-------------|-------|------------------|

**EXIT:**
- ✓ Every cluster has a named Next Team or specific Skill — NOT "investigate"
- ✓ All Stage 4 entries assigned to exactly one cluster

Emit: **COMMIT-STAGE-5**

---

**STAGE 6 — SYMMETRIC CONTRACT CLOSE**

**ENTER:** COMMIT-STAGE-5 emitted.

Return to Stage 1 beliefs. For each B-#, compare to what Stage 4 revealed. Assign:
- **COHERENT** — evidence consistent with the belief; no surprise
- **CONTRADICTORY** — at least one GATE-CONFIRMED surprise directly contradicts
- **FOREKNOWLEDGE-FLAGGED** — belief confirmed but reveals prior knowledge rather than discovery

| B-# | Belief | Verdict | Revision Direction |
|-----|--------|---------|-------------------|

Foreknowledge verdict:
> Foreknowledge status: [ CLEAR | FOREKNOWLEDGE-FLAGGED ]
> *(If FLAGGED: name responsible B-# beliefs. Issue HALT before Stage 7.)*

**EXIT:**
- ✓ All B-# beliefs have verdicts
- ✓ CONTRADICTORY rows have non-empty revision direction
- ✓ Foreknowledge verdict explicitly stated
- ✓ If FLAGGED: responsible B-# beliefs named

Emit: **COMMIT-STAGE-6**

---

**STAGE 7 — ARTIFACT DELIVERY**

**ENTER:** COMMIT-STAGE-6 emitted. Foreknowledge verdict is CLEAR. If FOREKNOWLEDGE-FLAGGED and responsible beliefs are unnamed — issue HALT. Do not proceed.

Deliver the complete topic-reflect artifact:
- Topic name and date; signal namespace coverage
- All Stage 4 surprise entries (GATE-CONFIRMED only; each with all 5 sub-fields including What We Expected)
- Stage 5 cluster map
- Stage 6 verdict table with foreknowledge verdict

**EXIT:**
- ✓ Artifact complete and coherent
- ✓ All Stage 4 entries present with all 5 sub-fields
- ✓ Cluster map and verdict table included
- ✓ Foreknowledge verdict stated

Emit: **COMMIT-STAGE-7**

---

**Rubric differentiation summary for this round:**

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-01** (surprise orientation, B-# per entry) | PARTIAL — B-# in deviation chain only | PARTIAL | PARTIAL | PARTIAL | **PASS** — explicit `What We Expected (B-[#])` sub-field |
| **C-33** (B-# belief anchor sub-field) | FAIL | FAIL | FAIL | FAIL | **PASS** |
| C-02 through C-32 | PASS | PASS | PASS | PASS | PASS |

V-01 through V-04 all have B-# referenced in Stage 2 and carried through GATE-CONFIRMED-[N] routing, but the Stage 4 entry template contains no dedicated `What We Expected` sub-field — the belief link is structural but implicit. V-05 makes it explicit at three convergent points: field definition in the Field Reference block, demonstration in Surprise 0, and per-entry verification in the COMMIT-ENTRY gate.
