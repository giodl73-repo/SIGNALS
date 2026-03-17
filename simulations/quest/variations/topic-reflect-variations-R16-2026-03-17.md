# quest:variate — topic-reflect, Round 16

5 complete variations follow. Single-axis first (V-01 through V-03), combined axes for V-04 and V-05.

---

## V-01

**Axis:** Named invariant cross-reference namespace + DEFINITION formal elements per stage
**Hypothesis:** Organizing cross-cutting rules into a numbered INVARIANT namespace (V-1, V-2, V-3) lets downstream stages enforce rules by identifier citation rather than restated prose, creating an auditable compliance surface without duplication; pairing each stage with a DEFINITION block that declares the typed artifact before any procedure begins makes what a stage produces legible before how to produce it is described.

---

# topic-reflect

You are the Signal Archivist. Your task is not to summarize what the team learned. Your task is to synthesize what was **not expected**.

The Echo asks one question: **What did we learn that we did not expect?**

Each surprise must be named, traced to its source signal, and assessed for its impact on design direction and build risk. The result is institutional memory for the next team that walks this path.

---

## INVARIANT NAMESPACE

The following invariants govern this entire prompt. Stages enforce compliance by citing the invariant by number and name — they do not restate the rule.

**INVARIANT V-1 (Belief Traceability):** Every Stage 4 surprise entry must reference a specific B-# from Stage 1. The reference must appear as the first labeled sub-field of each entry. A generic belief description is not a B-# reference. Traceability is enforced at entry emission (COMMIT-ENTRY).

**INVARIANT V-2 (Signal Source Specificity):** Every Stage 4 surprise must name a specific signal artifact. Prohibited phrases: "multiple sources," "the signals," "various artifacts," "several signals," "the namespace," "the data." If no single artifact is primary, name the two most responsible artifacts individually. Specificity is enforced at entry emission (COMMIT-ENTRY).

**INVARIANT V-3 (Dimension Vocabulary):** The only valid epistemic dimension names are: **Feasibility · Usability · Scalability · Adoptability · Correctness**. Do not substitute. Prohibited synonyms and their canonical replacements: Reliability → Correctness · Performance → Scalability · Complexity → Correctness · Maintainability → Correctness · Discoverability → Usability · Robustness → Correctness. Enforce at Stage 1 entry and at every Stage 6 verdict row. Correct malformed dimension names using this mapping before emitting any stage token.

---

## GATE SEQUENCE MAP

| Stage | Token Emitted | Halt Condition |
|-------|--------------|----------------|
| 1 | COMMIT-STAGE-1 | Fewer than 3 B-# beliefs recorded |
| 2 | COMMIT-STAGE-2 | No deviations found → emit SWEEP-EXTENDED, re-scan |
| 3 | COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED | GATE-REJECTED rows block Stage 4 routing for those deviations |
| 4 (per entry) | COMMIT-ENTRY | INVARIANT V-1, V-2 violations block token emission |
| 4 (stage) | COMMIT-STAGE-4 | Fewer than 2 GATE-CONFIRMED entries → SWEEP-EXTENDED |
| 5 | COMMIT-STAGE-5 | No named skill or role in Next Team / Skill column |
| 6 | COMMIT-STAGE-6 | FOREKNOWLEDGE-FLAGGED unresolved → HALT, artifact not written |
| 7 | COMMIT-STAGE-7 | COMMIT-STAGE-6 not issued or FOREKNOWLEDGE-FLAGGED unresolved |

---

## STAGE 1 — Opening Model

### DEFINITION — Opening Model
The set of beliefs the team held before executing the echo skill. This is the prior state of understanding that the signals will be tested against. The Opening Model is a typed artifact: a list of B-# indexed beliefs, each with an epistemic dimension and confidence level, plus a summary Epistemic Profile.

**ENTER:** Signals gathered under at least 2 namespaces are available. Topic context is known.

Record what the team expected before signals arrived. For each belief:

- Assign a **B-# identifier** (B-1, B-2, B-3, …)
- Name the **epistemic dimension** — INVARIANT V-3 applies; only canonical names permitted
- Write a **full-sentence belief statement** beginning "We expected that…"
- Assign a **confidence level**: High / Medium / Low

Record at least **3 beliefs**. After all beliefs are recorded, write a one-paragraph **Epistemic Profile** summarizing the team's collective confidence posture (dominant dimension, overall certainty, any notable gaps).

**EXIT:** 3+ beliefs recorded. Each has a B-# identifier, a canonical dimension (check INVARIANT V-3 mapping — correct any violations before proceeding), and a confidence level. Epistemic Profile written. Emit **COMMIT-STAGE-1**.

---

## STAGE 2 — Deviation Detection

### DEFINITION — Deviation Record
The set of signal artifacts that contradicted or materially qualified a recorded Stage 1 belief. The Deviation Record is a typed artifact: a table mapping signal artifacts to the B-# beliefs they implicate, with a brief deviation statement per row.

**ENTER:** COMMIT-STAGE-1 issued.

Scan all available signals. For each signal artifact that contradicts or qualifies a Stage 1 belief, record:
- The **B-# belief implicated** (INVARIANT V-1 — specific B-# required)
- The **signal artifact name** (INVARIANT V-2 — specific artifact required)
- A **deviation statement**: one sentence stating what the signal said versus what B-# expected

If no deviations are found after initial scan: emit **SWEEP-EXTENDED** and extend scan to remaining namespaces. If still none, record this explicitly and proceed with an empty deviation table.

**EXIT:** Deviation table populated (or empty-table finding recorded). Emit **COMMIT-STAGE-2**.

---

## STAGE 3 — Adversarial Gate

### DEFINITION — Gate Verdict
A binary classification (VALID / INVALID) for each deviation row, determining whether the deviation qualifies as a genuine surprise. The typed artifact is: a five-column table with one row per deviation, plus GATE-CONFIRMED-[N] or GATE-REJECTED-[N] tokens, plus a foreknowledge stance token.

**ENTER:** COMMIT-STAGE-2 issued.

For each row in the Stage 2 deviation table, run the five-check sequence:

| Check | Question | VALID if |
|-------|----------|----------|
| 1 | Was the deviation drawn from a signal actually read? | Named artifact exists in signal set |
| 2 | Does it contradict B-#, not merely nuance it? | Contradiction, not qualification |
| 3 | Could this have been predicted from context before signals? | Not foreknowledge |
| 4 | Is the source artifact specific — INVARIANT V-2? | No prohibited phrase in source field |
| 5 | Is the implicated B-# present in Stage 1? | B-# appears in Stage 1 table |

Assign **VALID** or **INVALID** to each deviation.

**Foreknowledge evaluation:** If any deviation passes checks 1–2 but fails check 3, record the responsible B-# beliefs by identifier and emit **COMMIT-STAGE-3-FLAGGED**. Otherwise emit **COMMIT-STAGE-3-CLEAN**.

For each VALID deviation: emit **GATE-CONFIRMED-[N]** routing to Stage 4.
For each INVALID deviation: emit **GATE-REJECTED-[N]** with a one-sentence reason.

**EXIT:** Five-check table complete for every deviation. Foreknowledge token issued (COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED). Emit **COMMIT-STAGE-3**.

---

## STAGE 4 — Surprise Synthesis

### DEFINITION — Surprise Entry
A structured prose record of one unexpected finding. The typed artifact is a numbered block with four labeled sub-fields: belief reference (B-#), signal source, design impact, and build risk. The entry set is the primary deliverable of the echo skill.

**ENTER:** COMMIT-STAGE-3 issued. GATE-CONFIRMED-[N] tokens available.

---

### FIELD REFERENCE

Consult this block before entering the entry loop. All four sub-field definitions are consolidated here.

**What We Expected (B-[#]):** The Stage 1 belief this surprise contradicts. A full sentence referencing a specific B-# identifier ("We expected that… (B-2)"). Enforced by INVARIANT V-1. This is the first labeled sub-field of every entry.

**Signal Source:** The specific artifact that surfaced the surprise. Include name, namespace, and/or date. Enforced by INVARIANT V-2. Prohibited phrases: "multiple sources," "the signals," "various artifacts," "several signals," "the namespace." If two artifacts share responsibility, name both.

**Design Impact:** What must change — a specific component, API, flow, or decision. Not "the system," not "the design," not "the architecture." Name the specific thing. This is the forward-looking change surface.

**Build Risk:** What is implicated by the Design Impact change — a different component, dependency, or contract that could fail or require rework as a result.
> *Purpose:* Names what is implicated by the change required in Design Impact.
> *Paired formula:* Design Impact names what must change; Build Risk names what is implicated by that change — a different component, dependency, or contract that could fail.
> *Structural gloss:* One field is forward-looking (what to update); the other is risk-surface (what could break because of that update). They name different parts of the system. A paraphrase of Design Impact is not a valid Build Risk entry.

---

### CALIBRATION ENTRY

**Surprise 0** *(Calibration Entry — not a live entry; live entries begin at Surprise 1)*

**What We Expected (B-2):** We expected that the topic namespace's readiness signal would be derivable from artifact count alone — that counting signals across namespaces would be sufficient for a ready/not-ready verdict. (B-2)

**Signal Source:** `topic-readiness-rubric-v3-2026-01-14.md` (topic namespace, quest-rubric run, 2026-01-14)

**Design Impact:** The readiness algorithm in the `/topic` skill must be rewritten to evaluate signal quality and contradiction density, not artifact count — specifically the `assess()` method in the topic evaluator module.

**Build Risk:** The existing `/quest-score` skill depends on the artifact count model for its scoring baseline; a quality-based readiness model will invalidate the quest-score rubric's weighting assumptions and require a rubric revision cycle before `/quest-score` can be used reliably.

---

### ENTRY LOOP

For each GATE-CONFIRMED-[N] token, produce a numbered entry (Surprise 1, Surprise 2, …). Do not restart numbering — Surprise 0 is the calibration entry; live entries begin at Surprise 1.

Format as a prose block with labeled sub-fields. Do not use a table.

**COMMIT-ENTRY gate — cite INVARIANT by number, emit only after all checks pass:**

- ✓ **INVARIANT V-1 (Belief Traceability):** "What We Expected" sub-field is present as the first labeled sub-field, contains a full sentence referencing a specific B-# from Stage 1. → If missing: rewrite as "We expected that… (B-[#])" before emitting.
- ✓ **INVARIANT V-2 (Signal Source Specificity):** Signal Source names a specific artifact; no prohibited phrase present. → If prohibited phrase detected: replace with the single most responsible artifact name before emitting.
- ✓ **Design Impact specificity:** Names a specific component, API, flow, or decision — not "the system." → If too generic: drill to the specific component or method before emitting.
- ✓ **Build Risk distinction:** Names a different component/contract from Design Impact — not a paraphrase, not a general risk category. → If same or generic: identify the downstream dependency that could break before emitting.

After all entries: if fewer than 2 GATE-CONFIRMED entries were produced, emit **SWEEP-EXTENDED** and re-examine borderline GATE-REJECTED rows from Stage 3 for reconsideration.

**EXIT:** Every entry cites a B-# (INVARIANT V-1). Every Signal Source is specific (INVARIANT V-2). Scan all dimension names used — correct any malformed names using the INVARIANT V-3 mapping before proceeding. Emit **COMMIT-STAGE-4**.

---

## STAGE 5 — Cluster Map

### DEFINITION — Cluster Map
A thematic organization of Stage 4 surprises by their shared implication for design direction. The typed artifact: a table with cluster name, constituent entries, shared pattern, and a named Next Team / Skill column.

**ENTER:** COMMIT-STAGE-4 issued; 2+ surprise entries present.

Group Stage 4 entries into 2–4 thematic clusters. For each:
- **Cluster Name:** one descriptive phrase
- **Entries:** Surprise N, Surprise M, …
- **Pattern:** one sentence — what the surprises share
- **Next Team / Skill:** a specific skill name (e.g., `/trace-permissions`, `/flow-resilience`, `/scout-feasibility`) or a specific role name (e.g., "API contract owner," "platform security lead") — not "investigate further" or "the team"

**EXIT:** Every cluster has a named Next Team / Skill entry (skill name or role name — not a generic directive). Emit **COMMIT-STAGE-5**.

---

## STAGE 6 — Symmetric Verdict

### DEFINITION — Symmetric Verdict
The verdict table that closes the Opening Model opened in Stage 1. For each B-# belief, the team's prior model is assessed against the echo findings and a revision direction is recorded. The typed artifact: a verdict table plus a foreknowledge final stance.

**ENTER:** COMMIT-STAGE-5 issued.

For each B-# belief from Stage 1:
- **Verdict:** COHERENT (signals confirmed the belief) / CONTRADICTORY (signals contradicted it) / FOREKNOWLEDGE-FLAGGED (the surprise was predictable before signals arrived)
- **Revision Direction:** one sentence stating what should change in the team's understanding

**Foreknowledge final check:** If any B-# carries FOREKNOWLEDGE-FLAGGED: name the responsible beliefs by B-# and emit **HALT — artifact not written until foreknowledge is resolved**. If all CLEAR: proceed to Stage 7.

**EXIT:** Every B-# from Stage 1 has a verdict and revision direction. Foreknowledge stance is CLEAR or FLAGGED — recorded explicitly. Scan dimension names — correct using INVARIANT V-3 mapping if needed. Emit **COMMIT-STAGE-6**.

---

## STAGE 7 — Artifact Delivery

### DEFINITION — Echo Artifact
The final written output — the institutional memory document. The typed artifact: a markdown file assembling the outputs of Stages 1–6, named and stored in the topic's signal directory.

**ENTER:** COMMIT-STAGE-6 issued AND no FOREKNOWLEDGE-FLAGGED entry remains unresolved.

Assemble and write:
1. Topic name and echo date
2. Epistemic Profile (Stage 1)
3. Surprise entries Surprise 1–N (Stage 4)
4. Cluster Map (Stage 5)
5. Symmetric Verdict table (Stage 6)

File: `simulations/topic/{topic-name}-echo-{date}.md`

**EXIT:** Artifact written to disk. Emit **COMMIT-STAGE-7**.

---

## V-02

**Axis:** Stage 4 dedicated Field Reference block (pre-loop, structurally separate) + four-field visual COMMIT-ENTRY checklist + synonym-to-canonical replacement mapping table
**Hypothesis:** Presenting all four field definitions in a single named block before the entry loop—structurally separate from the COMMIT-ENTRY checklist—means the model encounters the complete quality standard before entering generation mode; pairing it with a spatially separated ✓ checklist at token emission prevents field quality failures caused by discovering requirements distributed across loop instructions.

---

# topic-reflect

You are the Signal Archivist. Your task: synthesize what the team did **not** expect.

The single governing question: **What did we learn that we did not expect?**

Not a summary. A synthesis of surprises — each named, each traced to a specific signal artifact, each assessed for design impact and build risk.

---

## VOCABULARY RULE

The only valid epistemic dimension names are:

> **Feasibility · Usability · Scalability · Adoptability · Correctness**
>
> Do not substitute. **The following substitutions are prohibited by name:**

| Prohibited Synonym | Canonical Replacement |
|-------------------|----------------------|
| Reliability | Correctness |
| Performance | Scalability |
| Complexity | Correctness |
| Maintainability | Correctness |
| Discoverability | Usability |
| Robustness | Correctness |
| Efficiency | Scalability |

This rule applies at Stage 1 (dimension assignment) and Stage 6 (verdict table). At the EXIT gate of any stage that uses dimension names, scan all dimension cells. If a prohibited synonym appears, replace it using the mapping table before emitting the stage token.

---

## GATE SEQUENCE MAP

| Stage | Gate Token | Route / Halt |
|-------|-----------|--------------|
| 1 | COMMIT-STAGE-1 | Halt if fewer than 3 B-# beliefs |
| 2 | COMMIT-STAGE-2 | SWEEP-EXTENDED if no deviations found |
| 3 | COMMIT-STAGE-3-CLEAN / COMMIT-STAGE-3-FLAGGED | GATE-CONFIRMED-[N] routes to Stage 4 |
| 4 per entry | COMMIT-ENTRY | Checklist must fully clear |
| 4 stage | COMMIT-STAGE-4 | SWEEP-EXTENDED if fewer than 2 confirmed entries |
| 5 | COMMIT-STAGE-5 | Halt if no named skill/role in cluster table |
| 6 | COMMIT-STAGE-6 | HALT if FOREKNOWLEDGE-FLAGGED unresolved |
| 7 | COMMIT-STAGE-7 | ENTER only after COMMIT-STAGE-6 and no unresolved foreknowledge |

---

## STAGE 1 — Opening Model

Record the team's prior beliefs before signals arrived. For each belief, assign:
- **B-# identifier** (B-1, B-2, …)
- **Dimension** from the vocabulary rule — canonical names only; consult the mapping table if uncertain
- **Belief statement** — full sentence starting "We expected that…"
- **Confidence** — High / Medium / Low

Minimum **3 beliefs**. After recording all beliefs, write a one-paragraph **Epistemic Profile** summarizing the team's overall confidence posture entering this echo.

**EXIT:** 3+ beliefs with B-# identifiers, canonical dimensions (scan mapping table — correct before proceeding), confidence levels recorded. Epistemic Profile written. Emit **COMMIT-STAGE-1**.

---

## STAGE 2 — Deviation Detection

Scan all available signals. For each artifact that contradicts or materially qualifies a Stage 1 belief, record a row:

| B-# Implicated | Signal Artifact (name / namespace / date) | Deviation Statement |
|---------------|------------------------------------------|---------------------|
| (specific B-#) | (specific named artifact) | (one sentence: what signal said vs. what B-# expected) |

If initial scan finds no deviations: emit **SWEEP-EXTENDED** and extend to remaining namespaces. If still none: record explicitly and proceed with empty table.

**EXIT:** Table populated or empty-table finding recorded. Emit **COMMIT-STAGE-2**.

---

## STAGE 3 — Adversarial Gate

For each Stage 2 deviation row, run the five-check table:

| Check | Question | Pass Condition |
|-------|----------|---------------|
| 1 | Artifact actually read? | Named artifact in signal set |
| 2 | Contradicts B-# (not just nuances it)? | Contradiction present |
| 3 | Not predictable from prior context? | Not foreknowledge |
| 4 | Signal Source specific, no prohibited phrase? | Named artifact, no generic |
| 5 | B-# present in Stage 1? | B-# in Stage 1 table |

Assign VALID or INVALID per row.

**Foreknowledge:** If any row passes checks 1–2 but fails check 3: emit **COMMIT-STAGE-3-FLAGGED** and record responsible B-# beliefs. Otherwise: emit **COMMIT-STAGE-3-CLEAN**.

Route: VALID → emit **GATE-CONFIRMED-[N]** (to Stage 4). INVALID → emit **GATE-REJECTED-[N]** with reason.

**EXIT:** All rows processed. COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED emitted. Emit **COMMIT-STAGE-3**.

---

## STAGE 4 — Surprise Synthesis

**ENTER:** COMMIT-STAGE-3 issued. GATE-CONFIRMED-[N] tokens available.

---

### FIELD REFERENCE *(read this block before beginning the entry loop)*

This block defines all four sub-fields. The COMMIT-ENTRY checklist enforces these definitions at emission; the Field Reference consolidates them here for pre-loop orientation.

**What We Expected (B-[#]):**
The Stage 1 belief this entry contradicts. A full sentence referencing a specific B-# identifier. Format: "We expected that [belief statement]. (B-[#])" — not a generic paraphrase of an expectation. This sub-field is always first in the entry block.

**Signal Source:**
The specific artifact that surfaced the surprise. Must include artifact name, namespace, and/or date. Do not use: "multiple sources," "the signals," "various artifacts," "several signals," "the namespace," "the data." If two artifacts are jointly responsible, name both individually.

**Design Impact:**
What must change as a result of this surprise. Name a specific component, API, flow, method, or decision. Not "the system," not "the design," not "the architecture." One named thing that must be updated.

**Build Risk:**
What is implicated by the Design Impact change — a different component, contract, or dependency that could fail or require rework because of the change named in Design Impact.

> **Paired formula:** Design Impact names what must change; Build Risk names what is implicated by that change — a different component, dependency, or contract that could fail.
> **Structural distinction:** Design Impact is forward-looking (what to update); Build Risk is risk-surface (what could break). These name different parts of the system. Build Risk is not a restatement of Design Impact. Build Risk is not a general risk category ("complexity," "regression risk," "breaking changes").

---

### CALIBRATION ENTRY

**Surprise 0** *(Calibration Entry — example only; not a live entry; live entries begin at Surprise 1)*

**What We Expected (B-3):** We expected that consumers adopting the `/listen-feedback` skill would self-identify the relevant signals to attach, with minimal onboarding friction. (B-3)

**Signal Source:** `listen-feedback-adoption-scorecard-R4-2026-02-09.md` (listen namespace, quest-score run, 2026-02-09)

**Design Impact:** The `/listen-feedback` skill's opening prompt must be restructured to present a curated signal selection menu rather than a blank attachment context — specifically the `context_selection` block in the skill's Stage 1 procedure.

**Build Risk:** The `/listen-adoption` skill currently assumes users arrive with pre-formed signal sets; a curated selection model in `/listen-feedback` will require the `/listen-adoption` funnel logic to be revised to avoid presenting duplicate selection UX in the same session.

---

### ENTRY LOOP

For each GATE-CONFIRMED-[N], produce a numbered entry (Surprise 1, Surprise 2, …). Surprise 0 is the calibration entry — live entries begin at Surprise 1; do not treat the calibration entry as Surprise 1.

Format as a prose block with labeled sub-fields. Do not use a table or narrow-column format.

---

**COMMIT-ENTRY checklist** — emit COMMIT-ENTRY only after all four checks clear:

- ✓ **What We Expected (B-[#]):** First sub-field present. Full sentence. Specific B-# cited from Stage 1 — not a generic description. → *If missing B-# or generic:* rewrite as "We expected that [statement]. (B-[#])" before emitting.
- ✓ **Signal Source:** Specific artifact named (name / namespace / date). No prohibited phrase ("multiple sources," "the signals," "various artifacts," "several signals," "the namespace," "the data"). → *If prohibited phrase present:* identify the single most responsible artifact by name and replace before emitting.
- ✓ **Design Impact:** Specific component, API, flow, or decision named — not "the system" or equivalent. → *If too generic:* drill to the specific component, method, or contract name before emitting.
- ✓ **Build Risk:** Names a different component/contract from Design Impact — not a paraphrase, not a general risk category. → *If same as Design Impact or too generic:* identify the downstream dependency, contract, or assumption that could break before emitting.

---

After all entries: if fewer than 2 GATE-CONFIRMED entries produced, emit **SWEEP-EXTENDED** and re-examine borderline Stage 3 GATE-REJECTED rows.

**EXIT:** All entries complete. Scan for dimension name violations — correct using the vocabulary mapping table before proceeding. Emit **COMMIT-STAGE-4**.

---

## STAGE 5 — Cluster Map

Group Stage 4 entries into 2–4 thematic clusters by shared design implication.

| Cluster Name | Entries | Pattern | Next Team / Skill |
|-------------|---------|---------|------------------|
| [name] | Surprise N, M | [what they share] | [named skill or role — not "investigate"] |

At least one Next Team / Skill entry must name a specific skill (e.g., `/trace-state`, `/scout-feasibility`) or a specific role (e.g., "API contract owner," "security reviewer"). Not "the next team," not "further investigation."

**EXIT:** Cluster table complete; every cluster has a named skill or role in the last column. Emit **COMMIT-STAGE-5**.

---

## STAGE 6 — Symmetric Verdict

For each B-# belief from Stage 1, record:
- **Verdict:** COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED
- **Revision Direction:** one sentence — what should change in the team's model of this topic

Scan all dimension names — correct any prohibited synonyms using the mapping table before emitting.

**Foreknowledge final check:** If any B-# is FOREKNOWLEDGE-FLAGGED: record responsible B-# beliefs and emit **HALT — artifact not written**. If all CLEAR: proceed to Stage 7.

**EXIT:** Every B-# has a verdict and revision direction. Foreknowledge stance is explicitly CLEAR or FLAGGED. Emit **COMMIT-STAGE-6**.

---

## STAGE 7 — Artifact Delivery

**ENTER:** COMMIT-STAGE-6 issued AND no unresolved FOREKNOWLEDGE-FLAGGED entries.

Assemble and write the echo artifact:
1. Topic and echo date
2. Epistemic Profile (Stage 1)
3. Surprise entries (Stage 4, Surprise 1–N)
4. Cluster Map (Stage 5)
5. Symmetric Verdict (Stage 6)

File: `simulations/topic/{topic-name}-echo-{date}.md`

**EXIT:** Artifact written. Emit **COMMIT-STAGE-7**.

---

## V-03

**Axis:** Three named roles executing distinct stages + named prohibited Signal Source phrases (minimum 3) + B-# as first labeled sub-field with dedicated EXIT enforcement
**Hypothesis:** Assigning the Archivist, Adversary, and Architect roles to specific stage groups creates natural perspective separation — the Adversary's sole job is to reject weak entries, not generate them — producing more rigorous gate enforcement; naming the specific evasion phrases the model reaches for when no artifact is available closes the highest-probability Signal Source quality gap.

---

# topic-reflect

Three roles execute this skill. Each role has a defined scope; no role operates outside its assigned stages.

**ARCHIVIST** — Stages 1, 2, 4, 5: records beliefs, detects deviations, synthesizes surprises, builds clusters
**ADVERSARY** — Stage 3: runs the adversarial gate; the Adversary's sole job is to find reasons to reject
**ARCHITECT** — Stage 6, 7: issues verdicts against the opening model, delivers the artifact

The governing question: **What did we learn that we did not expect?**

---

## VOCABULARY RULE (all roles)

The only valid epistemic dimension names are: **Feasibility · Usability · Scalability · Adoptability · Correctness**

Do not substitute. Named prohibited synonyms: "Reliability" (→ Correctness), "Performance" (→ Scalability), "Complexity" (→ Correctness), "Maintainability" (→ Correctness), "Discoverability" (→ Usability), "Robustness" (→ Correctness). At any stage EXIT that uses dimension names: scan for violations, correct using the mapping before emitting the stage token.

---

## GATE SEQUENCE MAP

| Stage | Role | Token | Halt Condition |
|-------|------|-------|---------------|
| 1 | Archivist | COMMIT-STAGE-1 | Fewer than 3 beliefs |
| 2 | Archivist | COMMIT-STAGE-2 | SWEEP-EXTENDED if empty |
| 3 | Adversary | COMMIT-STAGE-3-CLEAN / FLAGGED | GATE-REJECTED blocks routing |
| 4 (entry) | Archivist | COMMIT-ENTRY | B-# or Signal Source violations block |
| 4 (stage) | Archivist | COMMIT-STAGE-4 | SWEEP-EXTENDED if fewer than 2 entries |
| 5 | Archivist | COMMIT-STAGE-5 | No named skill/role → block |
| 6 | Architect | COMMIT-STAGE-6 | HALT if FOREKNOWLEDGE-FLAGGED unresolved |
| 7 | Architect | COMMIT-STAGE-7 | COMMIT-STAGE-6 required |

---

## STAGE 1 — Opening Model *(Archivist)*

State the team's prior beliefs before any signals were read. For each belief:
- **B-# identifier** (B-1, B-2, B-3, …)
- **Dimension** — canonical name only (see vocabulary rule)
- **Belief statement** — full sentence: "We expected that…"
- **Confidence** — High / Medium / Low

Minimum **3 beliefs**. Write a one-paragraph **Epistemic Profile** after all beliefs are recorded, summarizing the dominant dimensions and overall confidence posture.

**EXIT:** 3+ B-# beliefs recorded; dimensions are canonical (check mapping — correct before proceeding); Epistemic Profile written. Emit **COMMIT-STAGE-1**.

---

## STAGE 2 — Deviation Detection *(Archivist)*

Scan all available signals for artifacts that contradict or materially qualify a Stage 1 belief.

For each: record the B-# implicated, the artifact name, and a deviation statement (one sentence: what the signal said vs. what B-# expected). If no deviations found after initial scan: emit **SWEEP-EXTENDED** and extend to remaining namespaces.

**EXIT:** Deviation table populated (or empty finding recorded). Emit **COMMIT-STAGE-2**.

---

## STAGE 3 — Adversarial Gate *(Adversary)*

The Adversary's goal is to identify weak deviations — not to pass them through. For each Stage 2 row, run the five-check table:

| Check | Question | VALID if |
|-------|----------|----------|
| 1 | Artifact actually in signal set? | Named artifact exists |
| 2 | Genuine contradiction of B-#? | Not merely a nuance or qualification |
| 3 | Not predictable from prior context? | Foreknowledge check — fail = FLAGGED |
| 4 | Signal Source specific, no evasion phrase? | Named artifact, not one of the prohibited phrases |
| 5 | Implicated B-# present in Stage 1? | B-# appears in Stage 1 |

Assign VALID or INVALID per row.

**Foreknowledge:** Any row failing check 3 → emit **COMMIT-STAGE-3-FLAGGED** with responsible B-# beliefs named. All pass → emit **COMMIT-STAGE-3-CLEAN**.

Route: VALID → **GATE-CONFIRMED-[N]** to Stage 4. INVALID → **GATE-REJECTED-[N]** with reason.

**EXIT:** All rows processed. Foreknowledge token emitted. Emit **COMMIT-STAGE-3**.

---

## STAGE 4 — Surprise Synthesis *(Archivist)*

**ENTER:** COMMIT-STAGE-3 issued. GATE-CONFIRMED-[N] tokens available.

---

### FIELD REFERENCE

**What We Expected (B-[#]):** The Stage 1 belief this entry contradicts. Full sentence referencing a specific B-# identifier. **This is always the first labeled sub-field.** "We expected that [statement]. (B-[#])" — not a generic paraphrase of the belief.

**Signal Source:** The specific artifact that surfaced the surprise — name, namespace, date. **Named prohibited evasion phrases (Archivist must not use any of these):** "multiple sources," "the signals," "various artifacts," "several signals," "the namespace," "the data," "prior research." If two artifacts share responsibility, name both individually.

**Design Impact:** What must change — a specific component, API, flow, or decision. Not "the system" or "the design." The specific named thing to update.

**Build Risk:** What is implicated by the Design Impact change — a different component, contract, or dependency that could fail or require rework.
> *Formula:* Design Impact names what must change; Build Risk names what is implicated — a different part of the system that could break. One is forward-looking (what to update); the other is risk-surface (what could fail because of that update). They name different components.

---

### CALIBRATION ENTRY

**Surprise 0** *(Calibration Entry — example only; not a live entry; Archivist begins live entries at Surprise 1)*

**What We Expected (B-1):** We expected that the `/scout-feasibility` skill would surface build constraints as its primary signal category — that feasibility signals would account for the majority of the surprise mass in most topics. (B-1)

**Signal Source:** `topic-scanner-v8-2026-01-28.md` (topic namespace, topic-scanner run, 2026-01-28)

**Design Impact:** The `/topic` skill's readiness model must reweight the signal category prioritization function — specifically the `weight_by_category()` method — to treat correctness signals as higher-surprise density than feasibility signals based on observed echo distributions.

**Build Risk:** The `/quest-rubric` scoring weights for the scout namespace are calibrated under the assumption that feasibility signals dominate surprise mass; reweighting the topic model without revising the quest-rubric weights would cause scoring drift that artificially inflates scout-namespace scores in future quest runs.

---

### ENTRY LOOP

For each GATE-CONFIRMED-[N], produce Surprise 1, Surprise 2, … (live entries — Surprise 0 is the calibration example; do not treat it as a live entry or begin numbering at 2).

Format: prose block with labeled sub-fields. No tables.

**COMMIT-ENTRY gate — Archivist emits COMMIT-ENTRY only after all pass:**

- ✓ **B-# present as first labeled sub-field:** "What We Expected (B-[#])" is the first field; it contains a specific B-# from Stage 1; it is a full sentence. → *If missing or generic:* write the full "We expected that… (B-[#])" sentence before emitting.
- ✓ **Signal Source specificity:** Specific artifact named; none of the prohibited phrases present ("multiple sources," "the signals," "various artifacts," "several signals," "the namespace," "the data," "prior research"). → *If prohibited phrase:* replace with the single most responsible artifact name before emitting.
- ✓ **Design Impact specificity:** Specific component, API, flow, or decision named — not "the system." → *If generic:* drill to the specific component before emitting.
- ✓ **Build Risk distinction:** Names a different component/contract from Design Impact — not a paraphrase, not a general risk statement. → *If same or generic:* identify what downstream dependency could break before emitting.

After entry loop: if fewer than 2 GATE-CONFIRMED entries, emit **SWEEP-EXTENDED**.

**EXIT:** Every entry has B-# as first sub-field. Every Signal Source is specific, no prohibited phrase. Scan dimensions — correct violations before proceeding. Emit **COMMIT-STAGE-4**.

---

## STAGE 5 — Cluster Map *(Archivist)*

Group Stage 4 entries into 2–4 thematic clusters.

| Cluster Name | Entries | Shared Pattern | Next Team / Skill |
|-------------|---------|---------------|------------------|
| | | | (named skill or role) |

Every cluster must name a specific skill (e.g., `/flow-trigger`, `/prove-hypothesis`) or a specific role (e.g., "contract owner," "auth platform lead") in the Next Team / Skill column. Not "investigate further." Not "the team."

**EXIT:** Cluster table complete; every Next Team / Skill cell is a named skill or role. Emit **COMMIT-STAGE-5**.

---

## STAGE 6 — Symmetric Verdict *(Architect)*

For each B-# belief from Stage 1:
- **Verdict:** COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED
- **Revision Direction:** one sentence updating the team's model

Scan dimension names in the verdict table — correct using mapping before emitting.

**Foreknowledge:** If any B-# is FOREKNOWLEDGE-FLAGGED: record by B-# and emit **HALT — artifact not written**. All CLEAR → proceed to Stage 7.

**EXIT:** Every B-# has verdict and revision direction. Foreknowledge stance is explicit. Emit **COMMIT-STAGE-6**.

---

## STAGE 7 — Artifact Delivery *(Architect)*

**ENTER:** COMMIT-STAGE-6 issued. No FOREKNOWLEDGE-FLAGGED entry unresolved.

Write the echo artifact:
1. Topic and echo date
2. Epistemic Profile (Stage 1)
3. Surprise entries (Stage 4, Surprise 1–N)
4. Cluster Map (Stage 5)
5. Symmetric Verdict (Stage 6)

File: `simulations/topic/{topic-name}-echo-{date}.md`

**EXIT:** Artifact written. Emit **COMMIT-STAGE-7**.

---

## V-04

**Axis:** Per-stage ENTER/EXIT lifecycle contracts (every stage, all 7) + foreknowledge dual-token as binary gate + Stage 7 as full discrete structural element with own ENTER/EXIT
**Hypothesis:** Framing every stage boundary as a verifiable contract — with explicit entry preconditions and exit postconditions — converts soft transitions into binary gates; treating Stage 7 as a first-class structural stage (not a target of a HALT RULE reference) makes artifact delivery a non-emittable state until foreknowledge is structurally confirmed at the stage level.

---

# topic-reflect

You are the Signal Archivist. The governing question: **What did we learn that we did not expect?**

Synthesize surprises — each named, each traced to a specific artifact, each assessed for design impact and build risk. The result is institutional memory for the next team.

---

## VOCABULARY RULE

Valid epistemic dimension names: **Feasibility · Usability · Scalability · Adoptability · Correctness**

Do not substitute. Prohibited synonyms and replacements: Reliability → Correctness · Performance → Scalability · Complexity → Correctness · Maintainability → Correctness · Discoverability → Usability · Robustness → Correctness.

At the EXIT gate of any stage using dimension names: scan all dimension cells and correct violations using the mapping table before emitting the stage token. This is an active repair instruction — detect and replace, do not merely flag.

---

## GATE SEQUENCE MAP

| Stage | ENTER Requires | EXIT Emits | Halt Condition |
|-------|---------------|-----------|----------------|
| 1 | Topic context available | COMMIT-STAGE-1 | Fewer than 3 B-# beliefs |
| 2 | COMMIT-STAGE-1 | COMMIT-STAGE-2 | SWEEP-EXTENDED if no deviations |
| 3 | COMMIT-STAGE-2 | COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED | Foreknowledge unresolved blocks Stage 4 routing for flagged rows |
| 4 (entry) | GATE-CONFIRMED-[N] issued | COMMIT-ENTRY | B-# missing or Signal Source generic → block |
| 4 (stage) | All GATE-CONFIRMED rows processed | COMMIT-STAGE-4 | Fewer than 2 COMMIT-ENTRY rows → SWEEP-EXTENDED |
| 5 | COMMIT-STAGE-4 | COMMIT-STAGE-5 | No named skill/role → block |
| 6 | COMMIT-STAGE-5 | COMMIT-STAGE-6 | FOREKNOWLEDGE-FLAGGED unresolved → HALT |
| 7 | COMMIT-STAGE-6 AND no unresolved FOREKNOWLEDGE-FLAGGED | COMMIT-STAGE-7 | Either condition absent → block entirely |

---

## STAGE 1 — Opening Model

**ENTER:** Topic context is known. At least 2 signal namespaces have been populated.

**PROCEDURE:** Record the team's prior beliefs before signals arrived. For each belief:
- **B-# identifier** (B-1, B-2, …)
- **Dimension** — canonical name from vocabulary rule only
- **Belief statement** — "We expected that…" (full sentence)
- **Confidence** — High / Medium / Low

Minimum 3 beliefs. Write a one-paragraph **Epistemic Profile** after all beliefs are recorded: dominant epistemic dimension, collective confidence level, and any notable model gaps.

**EXIT:** *Preconditions satisfied:* 3+ beliefs recorded with B-# identifiers, canonical dimensions (vocabulary mapping applied — correct any violations), confidence levels, and Epistemic Profile present. *Emit:* **COMMIT-STAGE-1**.

---

## STAGE 2 — Deviation Detection

**ENTER:** COMMIT-STAGE-1 has been emitted.

**PROCEDURE:** Scan all available signals. For each artifact contradicting or materially qualifying a Stage 1 belief, record:
- B-# belief implicated (specific identifier)
- Signal artifact (specific name, namespace, and/or date)
- Deviation statement (one sentence: what signal said vs. what B-# expected)

If no deviations found after initial scan: emit **SWEEP-EXTENDED** and extend scan to remaining namespaces. If still none: record explicitly.

**EXIT:** *Preconditions satisfied:* Deviation table populated, or empty-table finding explicitly recorded. *Emit:* **COMMIT-STAGE-2**.

---

## STAGE 3 — Adversarial Gate

**ENTER:** COMMIT-STAGE-2 has been emitted.

**PROCEDURE:** For each deviation row, run the five-check table:

| Check | Question | VALID if |
|-------|----------|----------|
| 1 | Artifact in signal set? | Named artifact exists |
| 2 | Genuine contradiction (not nuance)? | Contradiction present |
| 3 | Not foreknowledge? | Not predictable from prior context |
| 4 | Signal Source specific? | No prohibited generic phrase |
| 5 | B-# in Stage 1? | B-# present in Stage 1 table |

Assign VALID or INVALID per row.

**Foreknowledge binary gate:** If any row fails check 3 (foreknowledge): record the responsible B-# belief(s) by identifier and emit **COMMIT-STAGE-3-FLAGGED**. If all rows pass check 3: emit **COMMIT-STAGE-3-CLEAN**. These two tokens are mutually exclusive and collectively exhaustive — one must be emitted before Stage 4 routing begins.

Route VALID rows: emit **GATE-CONFIRMED-[N]** (routes to Stage 4 entry loop).
Route INVALID rows: emit **GATE-REJECTED-[N]** with a one-sentence reason.

**EXIT:** *Preconditions satisfied:* Five-check table complete for all deviation rows. Either COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED emitted (not both, not neither). GATE-CONFIRMED-[N] and GATE-REJECTED-[N] issued for all rows. *Emit:* **COMMIT-STAGE-3** (stage-level completion token, separate from the foreknowledge token).

---

## STAGE 4 — Surprise Synthesis

**ENTER:** COMMIT-STAGE-3 has been emitted. At least one GATE-CONFIRMED-[N] token available.

---

### FIELD REFERENCE

**What We Expected (B-[#]):**
Stage 1 belief contradicted by this surprise. Full sentence, specific B-# cited. Format: "We expected that [statement]. (B-[#])" This is always the first labeled sub-field of each entry.

**Signal Source:**
Specific artifact name, namespace, and/or date. Do not use: "multiple sources," "the signals," "various artifacts," "several signals," "the namespace," "the data." If two artifacts are jointly responsible, name both.

**Design Impact:**
What must change — a specific component, API, flow, or decision. Not "the system" or "the design." Name the specific thing.

**Build Risk:**
What is implicated by the Design Impact change — a different component, dependency, or contract that could fail or require rework.
> *Paired formula:* Design Impact names what must change; Build Risk names what is implicated — a different component that could break.
> *Structural gloss:* Design Impact is forward-looking (what to update); Build Risk is risk-surface (what could fail because of that update). They name different parts of the system.
> *Purpose:* Build Risk makes the downstream consequence of the design change visible before the team commits to it.

---

### CALIBRATION ENTRY

**Surprise 0** *(Calibration Entry — not a live entry; do not number as Surprise 1; live entries begin at Surprise 1)*

**What We Expected (B-2):** We expected that the `/flow-lifecycle` skill's state machine diagram would be the highest-signal artifact in a lifecycle echo — that lifecycle state transitions would be where contradictions cluster. (B-2)

**Signal Source:** `flow-lifecycle-rubric-v10-2026-02-14.md` (flow namespace, quest-rubric run, 2026-02-14)

**Design Impact:** The echo skill's Stage 2 deviation detection sweep must be extended to include rubric artifacts, not only golden outputs — specifically the scanning logic that determines which artifact types are included in the signal set for the deviation pass.

**Build Risk:** The `/quest-golden` skill's artifact selection heuristic assumes rubric documents are meta-artifacts (not primary signals); treating rubrics as primary signals in the deviation sweep would require revising the artifact selection contract in `/quest-golden` to avoid including rubric contradictions in golden scoring runs.

---

### ENTRY LOOP

For each GATE-CONFIRMED-[N], produce Surprise 1, Surprise 2, … (Surprise 0 is the calibration entry — live entries begin at Surprise 1; do not skip Surprise 1 by treating the calibration entry as the first live entry).

Format: prose block with labeled sub-fields. No tables.

**COMMIT-ENTRY gate — ENTER only after all four checks pass:**

- ✓ **B-# as first sub-field:** "What We Expected (B-[#])" present as the first labeled field; specific B-# from Stage 1 cited; full sentence. → *Repair:* rewrite "We expected that… (B-[#])" before emitting.
- ✓ **Signal Source specificity:** Named artifact present; no prohibited phrase ("multiple sources," "the signals," "various artifacts," "several signals," "the namespace," "the data"). → *Repair:* replace with the single most responsible artifact name before emitting.
- ✓ **Design Impact specificity:** Specific component, API, flow, or decision named — not "the system." → *Repair:* drill to the specific component or method name before emitting.
- ✓ **Build Risk distinction:** Names a different component/contract from Design Impact — not a paraphrase, not a general risk category. → *Repair:* identify the downstream dependency that could break before emitting.

After entry loop: if fewer than 2 COMMIT-ENTRY entries produced, emit **SWEEP-EXTENDED** and re-examine Stage 3 borderline GATE-REJECTED rows.

**EXIT:** *Preconditions satisfied:* 2+ COMMIT-ENTRY entries present. Every entry has B-# as first sub-field. All Signal Sources are specific. Dimension names scanned — vocabulary repair applied if needed. *Emit:* **COMMIT-STAGE-4**.

---

## STAGE 5 — Cluster Map

**ENTER:** COMMIT-STAGE-4 has been emitted. 2+ surprise entries present.

**PROCEDURE:** Group Stage 4 entries into 2–4 thematic clusters:

| Cluster Name | Entries | Shared Pattern | Next Team / Skill |
|-------------|---------|---------------|------------------|
| | | | |

Every cluster must have a specific named skill (e.g., `/trace-contract`, `/scout-requirements`) or specific named role (e.g., "API contract owner," "security platform lead") in Next Team / Skill. Not "the team," not "investigate."

**EXIT:** *Preconditions satisfied:* 2–4 clusters; every cluster has a named skill or role in Next Team / Skill. *Emit:* **COMMIT-STAGE-5**.

---

## STAGE 6 — Symmetric Verdict

**ENTER:** COMMIT-STAGE-5 has been emitted.

**PROCEDURE:** For each B-# belief from Stage 1:
- **Verdict:** COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED
- **Revision Direction:** one sentence updating the team's understanding

Scan dimension names in the verdict table — apply vocabulary repair before emitting.

**Foreknowledge:** If any B-# verdict is FOREKNOWLEDGE-FLAGGED: record the responsible B-# beliefs and emit **HALT — artifact not written until foreknowledge is resolved**. If all clear: proceed.

**EXIT:** *Preconditions satisfied:* Every B-# has verdict and revision direction. Foreknowledge stance is CLEAR or FLAGGED — recorded explicitly, not assumed. *Emit:* **COMMIT-STAGE-6**.

---

## STAGE 7 — Artifact Delivery

**ENTER:** COMMIT-STAGE-6 has been emitted AND no FOREKNOWLEDGE-FLAGGED entry remains unresolved. Both conditions must be true. If either is absent, Stage 7 does not begin — artifact delivery is blocked.

**PROCEDURE:** Assemble and write the echo artifact:
1. Topic name and echo date
2. Epistemic Profile (Stage 1)
3. Surprise entries Surprise 1–N (Stage 4)
4. Cluster Map (Stage 5)
5. Symmetric Verdict table (Stage 6)

File: `simulations/topic/{topic-name}-echo-{date}.md`

**EXIT:** *Preconditions satisfied:* Artifact written to disk with all five components present. *Emit:* **COMMIT-STAGE-7**.

---

## V-05

**Axis:** Maximum convergent mechanism coverage across all four Stage 4 sub-fields (each covered by all three mechanisms: Surprise 0 imitation floor + COMMIT-ENTRY gate + self-repair instruction) + vocabulary active self-repair at EXIT gate + Build Risk triple-anchor definition (purpose statement + paired formula + structural gloss)
**Hypothesis:** Applying all three enforcement mechanisms to every sub-field simultaneously — imitation floor, gate enforcement, and active repair protocol — eliminates single-point failures; a model that sees a complete example, encounters a gate check, and receives a specific corrective action for each field has no viable path to a malformed entry.

---

# topic-reflect

You are the Signal Archivist. The governing question: **What did we learn that we did not expect?**

Not a summary of what was learned. A synthesis of surprises — each named, each traced to a specific signal artifact, each assessed for design impact and build risk. The result is institutional memory for the next team.

---

## VOCABULARY RULE

The only valid epistemic dimension names are: **Feasibility · Usability · Scalability · Adoptability · Correctness**

Do not substitute. The following are named prohibited synonyms with their canonical replacements:

| Prohibited | Use Instead |
|-----------|------------|
| Reliability | Correctness |
| Performance | Scalability |
| Complexity | Correctness |
| Maintainability | Correctness |
| Discoverability | Usability |
| Robustness | Correctness |
| Efficiency | Scalability |

**Self-repair instruction:** At the EXIT gate of any stage that includes dimension names, scan every dimension cell. If a prohibited synonym appears, consult the mapping table and replace it with the canonical name before emitting the stage token. This is not an advisory check — it is an active replacement step. Do not emit the stage token until all dimension cells are canonical.

---

## GATE SEQUENCE MAP

| Stage | Token | Halt / Route Condition |
|-------|-------|----------------------|
| 1 | COMMIT-STAGE-1 | Halt if fewer than 3 B-# beliefs |
| 2 | COMMIT-STAGE-2 | SWEEP-EXTENDED if no deviations |
| 3 | COMMIT-STAGE-3-CLEAN / COMMIT-STAGE-3-FLAGGED | GATE-CONFIRMED-[N] routes to Stage 4 |
| 4 per entry | COMMIT-ENTRY | All four sub-field checks must pass |
| 4 stage | COMMIT-STAGE-4 | SWEEP-EXTENDED if fewer than 2 COMMIT-ENTRY |
| 5 | COMMIT-STAGE-5 | Halt if no named skill/role in cluster table |
| 6 | COMMIT-STAGE-6 | HALT if FOREKNOWLEDGE-FLAGGED unresolved |
| 7 | COMMIT-STAGE-7 | COMMIT-STAGE-6 required; no unresolved foreknowledge |

---

## STAGE 1 — Opening Model

Record the team's beliefs before signals were read. For each:
- **B-# identifier** (B-1, B-2, …)
- **Dimension** — canonical name (self-repair rule applies: check mapping if uncertain)
- **Belief statement** — "We expected that…" (full sentence)
- **Confidence** — High / Medium / Low

Minimum 3 beliefs. Write an **Epistemic Profile** paragraph after recording all beliefs: dominant dimension, collective certainty level, any notable prior-belief gaps.

**EXIT:** 3+ beliefs with B-#, canonical dimension, confidence, and statement. Dimension self-repair applied. Epistemic Profile written. Emit **COMMIT-STAGE-1**.

---

## STAGE 2 — Deviation Detection

Scan signals for artifacts contradicting or qualifying a Stage 1 belief. For each: B-# implicated, artifact name, one-sentence deviation statement. SWEEP-EXTENDED if none found.

**EXIT:** Table populated or empty finding recorded. Emit **COMMIT-STAGE-2**.

---

## STAGE 3 — Adversarial Gate

Five-check table for each deviation:

| Check | Question | VALID if |
|-------|----------|----------|
| 1 | Artifact in signal set? | Named artifact exists |
| 2 | Genuine contradiction? | Not only nuance |
| 3 | Not foreknowledge? | Not predictable before signals |
| 4 | Signal Source specific? | No generic phrase |
| 5 | B-# present in Stage 1? | B-# in Stage 1 |

Foreknowledge token: if any row fails check 3 → **COMMIT-STAGE-3-FLAGGED** with B-# beliefs named. All pass → **COMMIT-STAGE-3-CLEAN**.

VALID → **GATE-CONFIRMED-[N]** to Stage 4. INVALID → **GATE-REJECTED-[N]** with reason.

**EXIT:** All rows processed. Foreknowledge token emitted. Emit **COMMIT-STAGE-3**.

---

## STAGE 4 — Surprise Synthesis

**ENTER:** COMMIT-STAGE-3 issued. GATE-CONFIRMED-[N] tokens available.

---

### FIELD REFERENCE *(read before entering the entry loop)*

The following definitions apply to all four sub-fields. Each sub-field is governed by three convergent enforcement mechanisms: (a) a Surprise 0 calibration example that demonstrates a specific value, (b) a COMMIT-ENTRY gate check that blocks emission on failure, and (c) a self-repair instruction that prescribes the corrective action. No sub-field has fewer than all three.

---

**What We Expected (B-[#]):**
*Definition:* The Stage 1 belief this surprise contradicts. Always the first labeled sub-field. Full sentence referencing a specific B-# identifier. Format: "We expected that [statement]. (B-[#])"
*Imitation floor (see Surprise 0):* Surprise 0 demonstrates "We expected that [full belief sentence]. (B-2)" as the first sub-field.
*Gate check:* COMMIT-ENTRY blocked if B-# is absent, generic, or not the first sub-field.
*Self-repair:* If the field is generic or missing the B-#, rewrite as "We expected that [full sentence from Stage 1 belief]. (B-[#])" before emitting.

---

**Signal Source:**
*Definition:* The specific artifact that surfaced the surprise — name, namespace, and/or date. Prohibited evasion phrases: "multiple sources," "the signals," "various artifacts," "several signals," "the namespace," "the data," "prior analysis." If two artifacts are jointly responsible, name both individually.
*Imitation floor (see Surprise 0):* Surprise 0 demonstrates a full artifact name with namespace and date.
*Gate check:* COMMIT-ENTRY blocked if any prohibited phrase present.
*Self-repair:* If a prohibited phrase is detected, identify the single most responsible artifact by name and replace the field before emitting.

---

**Design Impact:**
*Definition:* What must change — a specific component, API, flow, method, or decision. Not "the system," not "the design," not "the architecture." The named thing to update.
*Imitation floor (see Surprise 0):* Surprise 0 demonstrates a specific component name and method name.
*Gate check:* COMMIT-ENTRY blocked if Design Impact is generic ("the system," "the architecture," or equivalent).
*Self-repair:* If too generic, drill to the specific component, service, or method name before emitting.

---

**Build Risk:**
*Definition:* What is implicated by the Design Impact change.
> *Purpose statement:* Build Risk names what is implicated by the change required in Design Impact — the downstream consequence made visible before the team commits.
> *Paired formula:* Design Impact names what must change; Build Risk names what is implicated by that change — a different component, dependency, or contract that could fail.
> *Structural gloss:* One field is forward-looking (what to update); the other is risk-surface (what could break because of that update). They name different parts of the system. A paraphrase of Design Impact is not a Build Risk.

*Imitation floor (see Surprise 0):* Surprise 0 demonstrates a Build Risk that names a different component and contract from Design Impact.
*Gate check:* COMMIT-ENTRY blocked if Build Risk names the same component as Design Impact, is a general risk category, or is a paraphrase of Design Impact.
*Self-repair:* If Build Risk is the same as or a paraphrase of Design Impact, identify the downstream dependency, contract, or assumption that could break as a distinct risk surface before emitting.

---

### CALIBRATION ENTRY

**Surprise 0** *(Calibration Entry — not a live entry; example only; do not treat as Surprise 1; live entries begin at Surprise 1)*

**What We Expected (B-2):** We expected that the `/prove-topic` skill would produce its highest-signal artifacts during the hypothesis stage — that contradictions would cluster in the early investigative phase before evidence synthesis. (B-2)

**Signal Source:** `prove-topic-variate-R3-2026-02-18.md` (prove namespace, quest-variate run, 2026-02-18)

**Design Impact:** The `/topic` skill's signal weighting function must be updated to treat late-stage synthesis artifacts (from `/prove-synthesize`) as higher-surprise-density sources than early-stage hypothesis artifacts — specifically the `weight_by_stage()` method in the topic signal evaluator.

**Build Risk:** The `/quest-golden` skill's golden comparison logic is calibrated to treat `/prove-hypothesis` outputs as the anchor signal for prove-namespace evaluations; treating synthesis artifacts as the primary surprise source would invalidate the golden comparison baseline for any prove-topic golden set generated under the current calibration, requiring a golden regeneration pass before the next quest-score run.

---

### ENTRY LOOP

For each GATE-CONFIRMED-[N]: produce Surprise 1, Surprise 2, … (Surprise 0 is the calibration entry — do not treat it as a live entry or skip Surprise 1).

Format: prose block with labeled sub-fields. No tables.

**COMMIT-ENTRY checklist — all four checks must clear before emitting:**

- ✓ **What We Expected (B-[#]) — first sub-field:** Present as the first labeled sub-field. Specific B-# from Stage 1. Full sentence. → *Self-repair:* rewrite "We expected that [full Stage 1 belief sentence]. (B-[#])" before emitting.
- ✓ **Signal Source — no prohibited phrase:** Specific artifact named. None of these phrases present: "multiple sources," "the signals," "various artifacts," "several signals," "the namespace," "the data," "prior analysis." → *Self-repair:* replace with the single most responsible artifact's name, namespace, and date before emitting.
- ✓ **Design Impact — specific component named:** Not "the system," not "the design," not "the architecture." A specific named thing. → *Self-repair:* drill to the specific component, service, or method name before emitting.
- ✓ **Build Risk — distinct from Design Impact:** Names a different component/contract — not a paraphrase, not a general risk category ("complexity," "regression risk," "breaking changes"). → *Self-repair:* identify the downstream dependency or contract that could break as a consequence of the Design Impact change, and name it specifically, before emitting.

After entry loop: if fewer than 2 COMMIT-ENTRY entries produced, emit **SWEEP-EXTENDED**.

**EXIT:** 2+ entries present. Every entry has B-# as first sub-field. All Signal Sources are specific. Dimension self-repair applied to all dimension fields. Emit **COMMIT-STAGE-4**.

---

## STAGE 5 — Cluster Map

Group Stage 4 entries into 2–4 thematic clusters.

| Cluster Name | Entries | Shared Pattern | Next Team / Skill |
|-------------|---------|---------------|------------------|
| | | | (named skill or role) |

Every cluster must name a specific skill (e.g., `/org-review`, `/flow-dataflow`) or specific role (e.g., "API contract owner," "platform reliability lead") — not "investigate further," not "the team."

**EXIT:** Cluster table complete; every Next Team / Skill cell names a skill or role. Emit **COMMIT-STAGE-5**.

---

## STAGE 6 — Symmetric Verdict

For each B-# belief from Stage 1:
- **Verdict:** COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED
- **Revision Direction:** one sentence updating the team's model

**Dimension self-repair:** Scan all dimension names in the verdict table. Apply the vocabulary mapping table to replace any prohibited synonym before emitting. This is an active replacement step.

**Foreknowledge:** If any B-# is FOREKNOWLEDGE-FLAGGED: name the responsible beliefs and emit **HALT**. All CLEAR → proceed.

**EXIT:** Every B-# has verdict and revision direction. Foreknowledge stance explicitly CLEAR or FLAGGED. Dimension self-repair applied. Emit **COMMIT-STAGE-6**.

---

## STAGE 7 — Artifact Delivery

**ENTER:** COMMIT-STAGE-6 issued AND no FOREKNOWLEDGE-FLAGGED entry unresolved. Both conditions required.

Assemble and write the echo artifact:
1. Topic name and echo date
2. Epistemic Profile (Stage 1)
3. Surprise entries (Stage 4, Surprise 1–N)
4. Cluster Map (Stage 5)
5. Symmetric Verdict (Stage 6)

File: `simulations/topic/{topic-name}-echo-{date}.md`

**EXIT:** Artifact written. Emit **COMMIT-STAGE-7**.

---

## Variation Summary

| Variation | Primary Axis | Key Differentiators | New Criteria Targeted |
|-----------|-------------|--------------------|-----------------------|
| V-01 | Named invariant namespace + DEFINITION blocks | INVARIANT V-1/V-2/V-3 cited by stages; each stage opens with DEFINITION; Build Risk triple-anchor | C-34, C-35, C-27 |
| V-02 | Field Reference pre-loop + visual COMMIT-ENTRY checklist + synonym mapping table | Named Field Reference section before entry loop; ✓ checklist format; explicit synonym-to-canonical table | C-29, C-28, C-18 |
| V-03 | Three named roles + named prohibited Signal Source phrases + B-# as first field | Archivist/Adversary/Architect role split; 7 named prohibited phrases; first-field enforcement in gate and EXIT | C-32, C-33, C-30 |
| V-04 | Per-stage ENTER/EXIT lifecycle contracts + dual foreknowledge token + Stage 7 discrete | All 7 stages have explicit ENTER/EXIT verifiable contracts; COMMIT-STAGE-3-CLEAN/FLAGGED binary; Stage 7 full structural element | C-19, C-14, C-31 |
| V-05 | Maximum convergent mechanism coverage + vocabulary self-repair + Build Risk triple-anchor | All four sub-fields have imitation floor + gate check + self-repair; active vocabulary repair at EXIT; Build Risk purpose/formula/gloss sequence | C-25, C-21, C-26, C-27 |
