# Scout-Size Prompt Variations — R20

**Skill**: scout-size
**Rubric**: v20 (35 aspirational criteria C-01 through C-43, max 125 pts)
**Date**: 2026-03-17
**Round**: 20
**R19 champion**: V-01 — two-phase; `── CONFIDENCE GAP CHECKPOINT ──` standalone section; compilation table pointer row (C-40); role-tagged column headers (C-26); named prohibited content categories (C-24); three-field `── DIAGNOSTIC PATTERN ──` (C-37 + C-39); bidirectional exclusion lists (C-23 + C-29). Scored 95/100 (117/123 under v19 rubric, 33 aspirationals).
**R19 gaps under v20**:
- C-30 FAIL — defense cluster split: relational constraint in compilation table gap column header; self-test and WRONG/CORRECT in Phase 2 instruction section (different sections)
- C-32 PARTIAL — standalone gap section existed with visual delimiter but positioned *after* compilation table, creating a forward reference at pointer production time
- C-42 NEW — once C-32 is active, compilation table's gap column header is a pointer site, not a production site; it cannot serve as one of C-30's three mechanisms; all three must be inside the standalone section
- C-43 NEW — standalone gap section must appear before the output compilation table so the pointer references already-fixed content, not future content
- C-17 PARTIAL — WRONG/CORRECT present for C-15 scope only; C-11 (highest-uncertainty) and C-16 (destination tier coherence) lacked inline examples
- C-35/C-36/C-38/C-41 FAIL — no Phase 0 entry gate in R19 V-01

**R20 core fix**: Move the standalone gap section to between Phase 1 (Confidence Basis) and Phase 2 (Sensitivity Analysis), and co-locate all three defense mechanisms inside it. The compilation table appears last and carries only a pointer to the already-written gap content above.

**Axes selected**:

| Variation | Axis | Hypothesis |
|---|---|---|
| V-01 | Gap section ordering | Placing `── CONFIDENCE GAP CHECKPOINT ──` before the compilation table (not after) eliminates the forward-reference problem (C-43) and co-locates all three defense mechanisms inside the standalone section (C-42), resolving both R19 failures simultaneously |
| V-02 | Inertia-first framing | Leading with the inertia question as the anchor frame — "what does it cost to NOT build this?" — reinforces C-03 and C-10 while keeping the same structural machinery; inertia judgment becomes the context in which integration points and tier are evaluated |
| V-03 | Phrasing register (single-phase conversational) | Direct second-person imperative register with numbered plain-English steps reduces structural complexity by eliminating role-charter prose; tests whether the same enforcement outcomes (C-30, C-32, C-43) can be achieved without role-separation overhead |
| V-04 | Role sequence + table-dominant format (three roles) | A third role — Inertia Auditor — separates the status-quo cost analysis from the sizing analysis; tests whether three distinct production charters reduce field-ownership ambiguity relative to two-role designs without multiplying phase-transition overhead |
| V-05 | Lifecycle emphasis + full aspirational coverage (champion candidate) | Named transition gates between every phase, the CONFIDENCE GAP CHECKPOINT as an explicit phase gate (not just a section), and maximum structural encoding; designed to satisfy all 35 aspirationals under v20 |

---

## V-01 — Gap Section Ordering

**Variation axis**: Gap section ordering
**Hypothesis**: Placing `── CONFIDENCE GAP CHECKPOINT ──` between Phase 1 and Phase 2 — before the compilation table — eliminates the forward-reference problem (C-43) and allows all three defense mechanisms to be co-located inside the standalone section (C-42), resolving R19 V-01's C-30 FAIL and C-32 PARTIAL simultaneously. Also adds Phase 0 entry gate (fixes C-35/C-36/C-38/C-41) and inline examples for C-11 and C-16 scopes (fixes C-17 PARTIAL).

---

You are producing a **sizing signal** for a feature request. This is not a project plan — do not include task breakdowns, sprint assignments, or owner names. Your signals feed `program-plan`, which makes planning decisions downstream.

### ── ENTRY GATE ──

Evaluate two preconditions before analysis begins. If any row is BLOCKED, output the CLOSED signal for that row and stop.

| Precondition | STATUS (CLEAR / BLOCKED) | CLOSED-LABEL [fill only if BLOCKED; leave blank if CLEAR — format: "Precondition A: [named condition]" or "Precondition B: [named condition]"] |
|---|---|---|
| A — Inertia check viable: you can identify the current workaround or the cost of the feature's absence | CLEAR / BLOCKED | Precondition A: {reason} |
| B — Signal boundary intact: the input requests sizing signals, not a task plan, sprint assignments, or owner names | CLEAR / BLOCKED | Precondition B: {reason} |

Gate result: OPEN (both CLEAR) — proceed to Phase 1. CLOSED (any BLOCKED) — output the CLOSED-LABEL value and stop.

---

### Phase 1 — Sizing Analyst

**Production charter**: Inertia Check, Integration Points, Complexity Tier, Confidence Basis.
**Exclusion list — you do NOT produce**: Confidence Gap, Tier-Up Condition, Tier-Down Condition.

#### Field 1 — Inertia Check [Sizing Analyst]

Name the current workaround or the cost of the feature's absence. Assign exactly one directional label:
- **cheaper** — maintaining the workaround costs less than building
- **comparable** — costs are roughly equivalent
- **more expensive** — maintaining the workaround costs more than building

Required format: "Workaround: {name}. Maintaining it is {cheaper / comparable / more expensive} than building. Basis: {one sentence}."

A workaround mentioned in passing ("users currently use a spreadsheet") without a cost direction label fails.

#### Field 2 — Integration Points [Sizing Analyst]

List each integration point individually as named bullets. End with: "These are {N} integration points."

Example:
- API endpoint (user-facing submission)
- Auth hook (token validation)
- Event bus subscription (async delivery)

These are 3 integration points.

A general description without named points and a total count fails.

#### Field 3 — Complexity Tier [Sizing Analyst]

Assign exactly one tier: **LOW / MEDIUM / HIGH / XL** — this vocabulary only. "MODERATE", "3/5", and "complex" all fail. Downstream skills parse this vocabulary.

Justify the tier by reference to the named integration point count from Field 2. State how the count maps to the tier. Then name which integration point carries the highest implementation uncertainty — that is the risk driver, not the average.

**Read before writing your tier:**

WRONG: "Complexity: HIGH. This feature has several moving parts."
→ FAILURE CLASS: no-count-reference — no citation of integration point count; no named risk driver

CORRECT: "Complexity: HIGH. Three integration points each crossing a trust boundary — that is the threshold for HIGH. Risk driver: auth hook (signing scheme unconfirmed)."
→ PASS: count cited; risk driver named with reason

#### Field 4 — Confidence Basis [Sizing Analyst]

Name the specific evidence or reasoning behind the tier. Identify which integration point is the risk driver — the one with the highest implementation uncertainty — and explain why. A tier without named evidence is an assertion; a tier with named basis is a judgment.

**Read before writing your basis:**

WRONG: "Basis: Integration complexity is high based on general system knowledge."
→ FAILURE CLASS: no-evidence — no specific facts; no risk driver named

CORRECT: "Basis: Three external API dependencies confirmed; each requires auth handshake at the trust boundary. Risk driver: auth hook — signing scheme requires verification with the auth team; all other integration points have confirmed contracts."
→ PASS: specific evidence named; risk driver identified with explanation

---

### ── CONFIDENCE GAP CHECKPOINT ──

**Field owner**: Risk Assessor

This section is the production site for the Confidence Gap. The output compilation table below carries only a pointer to this section — write the gap here, not in the compilation table.

**Field definition** [must address a dimension NOT confirmed in Phase 1 Confidence Basis]: Name at least one open question or missing signal that, if resolved, could change the complexity tier or the inertia judgment. Name: (a) the specific open question, and (b) the action that would resolve it. The gap must address a dimension the Sizing Analyst did not confirm in Phase 1.

**Self-test** — before finalizing your gap, answer: "Is this gap derivable from my Phase 1 Confidence Basis by negating or paraphrasing something the Sizing Analyst confirmed?"
- If YES: **you have written a basis-negation — a Phase 2 charter violation.** Restate to address a dimension Phase 1 did not confirm. See DIAGNOSTIC PATTERN below.
- If NO: proceed.

── DIAGNOSTIC PATTERN ──

WRONG: "Gap: The integration point count may differ from what was estimated."
  FAILURE CLASS: basis-negation
  DETECTION PATTERN: gap is derivable by negating Phase 1 confirmed content — Sizing Analyst confirmed the integration point count; gap questions the count
  WHY IT FAILS: a basis-negation restates Phase 1 uncertainty rather than identifying a new open question; it adds no information

CORRECT: "Gap: Unknown whether the auth hook requires a custom signing scheme. Resolution action: confirm with the auth team before sprint planning."
  → names a dimension Phase 1 did not address; names the resolution action
────────────────────────────────────────

Write your Confidence Gap: "Gap: {open question — dimension not confirmed in Phase 1}. Resolution action: {named action}."

---

### Phase 2 — Risk Assessor

**Production charter**: Tier-Up Condition, Tier-Down Condition.
**Exclusion list — you do NOT produce**: Inertia Check, Integration Points, Complexity Tier, Confidence Basis, Confidence Gap.
**Non-access clause**: Do not cite the integration point list, count, tier, or rationale from Phase 1 as your Confidence Gap. Those are confirmed facts, not open questions.

#### Field 5 — Sensitivity Analysis [Risk Assessor]

**Tier-Up Condition**: Name one condition that, if true, would raise the complexity tier. Reference a specific integration point. Name the destination tier — it must be **higher** than the current tier.

**Read before writing your tier-up condition:**

WRONG (null sensitivity): "Tier-Up: If additional complexity is found, complexity remains HIGH." [current = HIGH → destination = HIGH]
  FAILURE CLASS: null-sensitivity — destination tier matches the current tier; sensitivity range is zero

CORRECT: "Tier-Up: If the auth hook requires custom signing, complexity becomes XL." [current = HIGH → destination = XL > HIGH]

Format: "Tier-Up: if {condition}, complexity becomes {destination tier [must be HIGHER than current: LOW / MEDIUM / HIGH / XL]}"

**Tier-Down Condition**: Name one condition that, if true, would lower the complexity tier. Reference a **different integration point** than the tier-up condition. Name the destination tier — it must be **lower** than the current tier.

Format: "Tier-Down: if {condition}, complexity becomes {destination tier [must be LOWER than current: LOW / MEDIUM / HIGH / XL]}"

---

### Output Compilation Table

| Field | [Sizing Analyst] | [Risk Assessor] |
|---|---|---|
| Inertia Check | {workaround} — {cheaper / comparable / more expensive} | — |
| Integration Points | {named list} — {N} points | — |
| Complexity Tier | {LOW / MEDIUM / HIGH / XL} | — |
| Confidence Basis | {specific evidence + risk driver named} | — |
| Confidence Gap [must address dimension not confirmed in Basis] | → see CONFIDENCE GAP CHECKPOINT above | — |
| Tier-Up Condition | — | if {condition}, becomes {destination tier [HIGHER than current: LOW / MEDIUM / HIGH / XL]} |
| Tier-Down Condition | — | if {condition}, becomes {destination tier [LOWER than current — different integration point from Tier-Up]} |

---

### Sizing Signals

| Complexity Tier | Team-Size Signal | Timeline Signal |
|---|---|---|
| LOW | 1 specialist | 1 sprint |
| MEDIUM | 1–2 specialists | 2–3 sprints |
| HIGH | 2–3 specialists | 3–5 sprints |
| XL | 3+ specialists | 5+ sprints |

Confidence level: {LOW / MEDIUM / HIGH} — name the primary open question from the Confidence Gap as the uncertainty driver.

---

## V-02 — Inertia-First Framing

**Variation axis**: Inertia framing
**Hypothesis**: Leading with "what does it cost to NOT build this?" as the anchor sentence makes every subsequent sizing judgment explicitly relative to the status-quo cost — the tier is not an abstract complexity score but a build/maintain comparison. The structural machinery is identical to V-01; only the emphasis changes. Inertia is the first precondition, the first sizing step, and the frame for the confidence basis.

---

You are producing a **sizing signal** for a feature request. The central question is: **what does it cost to NOT build this?** Every sizing judgment — complexity tier, confidence basis, sensitivity range — is evaluated relative to the cost of the current workaround. This is not a project plan. Do not include task breakdowns, sprint assignments, or owner names.

### ── ENTRY GATE ──

Before any analysis, evaluate two preconditions. If any row is BLOCKED, output the CLOSED signal and stop.

| Precondition | STATUS (CLEAR / BLOCKED) | CLOSED-LABEL [fill only if BLOCKED; leave blank if CLEAR — format: "Precondition A: [named condition]" or "Precondition B: [named condition]"] |
|---|---|---|
| A — Inertia check viable: you can name the current workaround (or the cost of the feature's absence) and assign a directional cost judgment | CLEAR / BLOCKED | Precondition A: {reason} |
| B — Signal boundary intact: the input requests sizing signals, not a task plan, sprint assignments, or owner names | CLEAR / BLOCKED | Precondition B: {reason} |

Gate result: OPEN (both CLEAR) — proceed. CLOSED (any BLOCKED) — output the CLOSED-LABEL and stop.

---

### Phase 1 — Sizing Analyst

**Production charter**: Inertia Anchor, Integration Points, Complexity Tier, Confidence Basis.
**Exclusion list — you do NOT produce**: Confidence Gap, Tier-Up Condition, Tier-Down Condition.

#### Field 1 — Inertia Anchor [Sizing Analyst]

This field sets the frame for all subsequent analysis. Name the current workaround (or the cost of the feature's absence). Assign exactly one directional label: **cheaper** / **comparable** / **more expensive** (maintaining the workaround vs building the feature). State the one-sentence cost basis.

Required format: "Workaround: {name}. Maintaining it is {cheaper / comparable / more expensive} than building. Cost basis: {one sentence}."

Every other field is evaluated relative to this anchor. If the workaround is cheap to maintain, the inertia argument for building is weak — complexity tier and confidence must account for this. If the workaround is expensive, the build case strengthens regardless of implementation complexity.

#### Field 2 — Integration Points [Sizing Analyst]

List each integration point individually as named bullets. End with: "These are {N} integration points." Each point names the integration surface and its role.

Example:
- API endpoint (user-facing, confirmed contract)
- Auth hook (token validation, signing scheme unconfirmed)
- Event bus subscription (async, topic confirmed)

These are 3 integration points.

#### Field 3 — Complexity Tier [Sizing Analyst]

Assign exactly one: **LOW / MEDIUM / HIGH / XL** — this vocabulary only. Justify the tier by reference to the integration point count from Field 2. Name the risk driver: the integration point with the highest implementation uncertainty.

**Read before writing:**

WRONG: "Complexity: HIGH. This feature touches several systems with variable complexity."
→ FAILURE CLASS: no-count-reference — no citation of integration point count; no named risk driver

CORRECT: "Complexity: HIGH. Three integration points each crossing a trust boundary — threshold for HIGH. Risk driver: auth hook (signing scheme unconfirmed; other two have confirmed contracts)."

#### Field 4 — Confidence Basis [Sizing Analyst]

Name the specific evidence for the tier. Among the named integration points, identify the risk driver — the one with the highest implementation uncertainty — and explain why it is the risk driver rather than an average factor.

**Read before writing:**

WRONG: "Basis: Feature complexity is high based on number of integration points and general system knowledge."
→ FAILURE CLASS: no-evidence — no specific facts; no risk driver distinguished

CORRECT: "Basis: Three external API dependencies confirmed; each requires auth handshake. Risk driver: auth hook — signing scheme requires team verification; API endpoint and event bus both have confirmed contracts and no blocking unknowns."

---

### ── CONFIDENCE GAP CHECKPOINT ──

**Field owner**: Risk Assessor

This section is the production site for the Confidence Gap. The compilation table carries only a pointer here — write the gap in this section, not in the compilation table.

**Field definition** [must address a dimension NOT confirmed in Phase 1 Confidence Basis]: Name at least one open question that, if resolved, could change the complexity tier or the inertia judgment. Name both the question and the action that would resolve it. The gap must address a dimension Phase 1 did not confirm — it cannot re-state or negate something the Sizing Analyst verified.

**Self-test** — before finalizing your gap, answer: "Is this gap derivable from my Phase 1 Confidence Basis by negating something the Sizing Analyst confirmed?"
- If YES: **you have written a basis-negation — a Phase 2 charter violation.** Choose a dimension Phase 1 did not address. See DIAGNOSTIC PATTERN.
- If NO: proceed.

── DIAGNOSTIC PATTERN ──

WRONG: "Gap: The cost direction of the workaround may be different from what was estimated."
  FAILURE CLASS: basis-negation
  DETECTION PATTERN: gap negates a Phase 1 confirmed judgment — Field 1 (Inertia Anchor) confirmed the cost direction; gap questions the same judgment
  WHY IT FAILS: restates Phase 1 uncertainty about a confirmed field; identifies no new open question; adds no information to the inertia anchor already set

CORRECT: "Gap: Unknown whether the auth hook's custom signing requirement will surface mid-sprint. Resolution action: schedule a 30-minute confirmation with the auth team before sprint planning."
  → names a dimension not addressed in Phase 1 (timing risk of late-emerging signing requirement); names the resolution action
────────────────────────────────────────

Write your Confidence Gap: "Gap: {open question — dimension Phase 1 did not address, including whether this changes the inertia judgment}. Resolution action: {named action}."

---

### Phase 2 — Risk Assessor

**Production charter**: Tier-Up Condition, Tier-Down Condition.
**Exclusion list — you do NOT produce**: Inertia Anchor, Integration Points, Complexity Tier, Confidence Basis, Confidence Gap.
**Non-access clause**: Do not cite the integration point list, count, tier, rationale, or inertia anchor judgment from Phase 1 as your Confidence Gap. Those are confirmed facts — name a dimension Phase 1 did not address.

#### Field 5 — Sensitivity Analysis [Risk Assessor]

**Tier-Up Condition**: Name one condition that, if true, would raise the complexity tier. Reference a specific integration point. State the destination tier — must be **higher** than the current tier.

Format: "Tier-Up: if {condition}, complexity becomes {destination tier [must be HIGHER than current: LOW / MEDIUM / HIGH / XL]}"

**Read before writing:**

WRONG: "Tier-Up: If the feature proves harder than expected, complexity increases to HIGH." [current = HIGH → destination = HIGH — null sensitivity]
  FAILURE CLASS: null-sensitivity — destination matches current tier

CORRECT: "Tier-Up: If the auth hook requires a custom signing library not yet in the dependency tree, complexity becomes XL." [current = HIGH → XL is higher]

**Tier-Down Condition**: Name one condition that, if true, would lower the complexity tier. Reference a **different integration point** than the tier-up condition. State the destination tier — must be **lower** than the current tier.

Format: "Tier-Down: if {condition}, complexity becomes {destination tier [must be LOWER than current: LOW / MEDIUM / HIGH / XL]}"

---

### Output Compilation Table

| Field | [Sizing Analyst] | [Risk Assessor] |
|---|---|---|
| Inertia Anchor | {workaround} — {cheaper / comparable / more expensive} | — |
| Integration Points | {named list} — {N} points | — |
| Complexity Tier | {LOW / MEDIUM / HIGH / XL} | — |
| Confidence Basis | {specific evidence + risk driver named} | — |
| Confidence Gap [must address dimension not confirmed in Basis — inertia anchor is confirmed] | → see CONFIDENCE GAP CHECKPOINT above | — |
| Tier-Up Condition | — | if {condition}, becomes {destination tier [HIGHER than current]} |
| Tier-Down Condition | — | if {condition}, becomes {destination tier [LOWER than current — different integration point from Tier-Up]} |

---

### Sizing Signals

| Complexity Tier | Team-Size Signal | Timeline Signal |
|---|---|---|
| LOW | 1 specialist | 1 sprint |
| MEDIUM | 1–2 specialists | 2–3 sprints |
| HIGH | 2–3 specialists | 3–5 sprints |
| XL | 3+ specialists | 5+ sprints |

Confidence level: {LOW / MEDIUM / HIGH}. State the primary open question from the Confidence Gap and whether its resolution would change the inertia anchor judgment.

---

## V-03 — Phrasing Register (Single-Phase Conversational)

**Variation axis**: Phrasing register
**Hypothesis**: Direct second-person imperatives with plain numbered steps achieve the same enforcement outcomes (C-30, C-32, C-43) without role-charter prose overhead. Single-phase design: no role separation (C-20 through C-29 do not apply), but the CONFIDENCE GAP CHECKPOINT standalone section with its defense cluster positioned before the compilation table still satisfies C-30/C-32/C-42/C-43. C-28 (single-phase self-test) substitutes for C-25.

---

You are running **scout-size**. Produce a sizing signal — not a project plan. No task breakdowns, sprint assignments, or owner names. Your output feeds `program-plan`. Work through each step in order.

**Tier vocabulary — exactly one**: **LOW / MEDIUM / HIGH / XL** — nothing else. "MODERATE", "3/5", and "complex" all fail.

### Step 0 — Entry Gate

Fill this table before anything else. If any row is BLOCKED, write the CLOSED-LABEL and stop.

| Precondition | STATUS (CLEAR / BLOCKED) | CLOSED-LABEL [fill only if BLOCKED; leave blank if CLEAR — format: "Precondition A: [named condition]" or "Precondition B: [named condition]"] |
|---|---|---|
| A — Can you name a workaround (or the cost of the feature's absence)? | CLEAR / BLOCKED | Precondition A: {reason} |
| B — Is the input free of task breakdowns, sprint assignments, and owner names? | CLEAR / BLOCKED | Precondition B: {reason} |

Both CLEAR → proceed to Step 1. Any BLOCKED → stop.

---

### Step 1 — Inertia Check

Name the workaround (or what it costs not to have this feature). Pick exactly one: **cheaper** / **comparable** / **more expensive** (keeping the workaround vs building).

Write: "Workaround: {name}. Keeping it is {cheaper / comparable / more expensive} than building. Why: {one sentence}."

---

### Step 2 — Integration Points

Name each integration point as a bullet. End with: "These are {N} integration points."

---

### Step 3 — Complexity Tier

Write exactly one tier: **LOW / MEDIUM / HIGH / XL**.

Explain how the count from Step 2 maps to this tier. Name the one integration point that carries the most implementation uncertainty — your risk driver.

Before you write, read this:

WRONG: "Complexity: HIGH. Feature is complex."
→ no count cited; no risk driver

CORRECT: "Complexity: HIGH. Three integration points crossing trust boundaries — HIGH threshold. Risk driver: auth hook (signing scheme unknown)."

---

### Step 4 — Confidence Basis

Name the specific evidence behind the tier. Call out which integration point is your risk driver and why it has the highest uncertainty.

Before you write, read this:

WRONG: "Basis: General integration complexity based on system experience."
→ FAILURE CLASS: no-evidence — no specific facts; no risk driver distinguished

CORRECT: "Basis: Three confirmed external API dependencies, each requiring auth handshake. Risk driver: auth hook — signing scheme not yet verified with auth team; other integration points have confirmed contracts."

---

### ── CONFIDENCE GAP CHECKPOINT ──

Name one open question that could change the tier or inertia judgment. Name the question AND the action that resolves it.

**Field rule** [must address a dimension NOT confirmed in Step 4 Confidence Basis]: The gap cannot re-state or negate something you just confirmed.

**Self-test** — ask yourself: "Could a reader derive this gap from my Step 4 Confidence Basis by negating something I confirmed?"
- If YES: **you have written a basis-negation — a gap field production violation.** Pick a dimension Step 4 did not verify. See DIAGNOSTIC PATTERN below.
- If NO: proceed.

── DIAGNOSTIC PATTERN ──

WRONG: "Gap: The integration point count might be wrong."
  FAILURE CLASS: basis-negation
  DETECTION PATTERN: gap can be derived by negating Step 4 confirmed content — you confirmed the count; gap questions the count
  WHY IT FAILS: you confirmed the count in Step 4; questioning it here adds nothing new

CORRECT: "Gap: Unknown whether the auth hook needs a custom signing library. Resolution action: 30-minute confirm with auth team."
  → new dimension (custom signing library detail not confirmed in Step 4); named resolution action
────────────────────────────────────────

Write: "Gap: {open question}. Resolution action: {action}."

---

### Step 5 — Sensitivity

**Tier-Up**: Name a condition that raises the tier. Name a specific integration point. State the destination tier — must be **higher** than your Step 3 tier.

Before writing: WRONG: destination tier = current tier (null sensitivity). CORRECT: destination tier is strictly higher.

Write: "Tier-Up: if {condition}, complexity becomes {higher tier [LOW / MEDIUM / HIGH / XL]}."

**Tier-Down**: Name a condition that lowers the tier. Name a **different integration point** than Tier-Up. Destination tier must be **lower** than Step 3.

Write: "Tier-Down: if {condition}, complexity becomes {lower tier [LOW / MEDIUM / HIGH / XL]}."

---

### Output Summary Table

| Field | Your Answer |
|---|---|
| Inertia Check | {workaround} — {cheaper / comparable / more expensive} |
| Integration Points | {named list} — {N} points |
| Complexity Tier | {LOW / MEDIUM / HIGH / XL} |
| Confidence Basis | {evidence + risk driver} |
| Confidence Gap [must address dimension not confirmed in Step 4] | → see CONFIDENCE GAP CHECKPOINT above |
| Tier-Up Condition | if {condition}, becomes {higher tier} |
| Tier-Down Condition | if {condition}, becomes {lower tier — different integration point} |
| Team-Size Signal | {1 / 1–2 / 2–3 / 3+} specialists |
| Timeline Signal | {1 / 2–3 / 3–5 / 5+} sprints |
| Confidence Level | {LOW / MEDIUM / HIGH} — primary uncertainty: {gap question} |

---

## V-04 — Three-Role Sequence + Table-Dominant Format

**Variation axis (combined)**: Role sequence + Output format
**Hypothesis**: A third role — Inertia Auditor — separates the status-quo cost analysis from the Sizing Analyst's integration-point and tier work. Three explicit charters with enumerated field ownership reduce cross-role ambiguity. Table-dominant format throughout encodes constraints structurally rather than in prose. CONFIDENCE GAP CHECKPOINT retains its standalone position before the compilation table.

---

You are producing a **sizing signal** for a feature request. This is not a project plan — do not include task breakdowns, sprint assignments, or owner names.

**Tier vocabulary — exactly one**: **LOW / MEDIUM / HIGH / XL** — nothing else.

---

### Phase 0 — Entry Gate

Evaluate both preconditions before any role begins. If any STATUS is BLOCKED, output the CLOSED-LABEL and stop.

| Precondition | STATUS (CLEAR / BLOCKED) | CLOSED-LABEL [fill only if BLOCKED; leave blank if CLEAR — format: "Precondition A: [named condition]" or "Precondition B: [named condition]"] |
|---|---|---|
| A — Inertia Auditor viable: you can name a workaround or the cost of the feature's absence | CLEAR / BLOCKED | Precondition A: {reason} |
| B — Signal boundary intact: input contains no task plan, sprint assignments, or owner names | CLEAR / BLOCKED | Precondition B: {reason} |

Gate: OPEN (both CLEAR) — proceed. CLOSED (any BLOCKED) — output CLOSED-LABEL and stop.

---

### Phase 1 — Inertia Auditor

**Production charter**: Inertia Check only.
**Exclusion list**: Integration Points, Complexity Tier, Confidence Basis, Confidence Gap, Tier-Up Condition, Tier-Down Condition.

| Inertia Check [Inertia Auditor] |
|---|
| Workaround: {name the workaround or cost of absence} |
| Cost direction [cheaper / comparable / more expensive]: {label} |
| Cost basis: {one sentence justifying the direction} |

A workaround named without a cost direction label fails Phase 1.

---

### Phase 2 — Sizing Analyst

**Production charter**: Integration Points, Complexity Tier, Confidence Basis.
**Exclusion list**: Inertia Check, Confidence Gap, Tier-Up Condition, Tier-Down Condition.

#### Field A — Integration Points [Sizing Analyst]

| Integration Points [Sizing Analyst] |
|---|
| {bullet: name + role} |
| {bullet: name + role} |
| {bullet: name + role} |
| **Count: These are {N} integration points.** |

#### Field B — Complexity Tier [Sizing Analyst]

Assign exactly one: **LOW / MEDIUM / HIGH / XL**. Justify by the count from Field A. Name the risk driver.

| Complexity Tier [Sizing Analyst] | Count-Based Justification | Risk Driver [name the highest-uncertainty integration point] |
|---|---|---|
| {LOW / MEDIUM / HIGH / XL} | {how count maps to tier} | {integration point} — {why it is highest-uncertainty} |

**Read before writing:**

WRONG (Field B): Tier = HIGH, Justification = "Feature is complex", Risk Driver = (blank)
→ fails: no count cited; no risk driver

CORRECT (Field B): Tier = HIGH, Justification = "3 points each crossing a trust boundary — HIGH threshold", Risk Driver = "auth hook — signing scheme unconfirmed; other two have confirmed contracts"

#### Field C — Confidence Basis [Sizing Analyst]

| Confidence Basis [Sizing Analyst] | Risk Driver (highest-uncertainty component and why) |
|---|---|
| {specific evidence for the tier — named facts, not general judgment} | {integration point name} — {why it is the risk driver, not others} |

**Read before writing:**

WRONG (Field C): Basis = "Integration complexity high based on system experience", Risk Driver = (blank)
→ FAILURE CLASS: no-evidence — no specific facts; no risk driver

CORRECT (Field C): Basis = "Three confirmed external API deps each requiring auth handshake", Risk Driver = "auth hook — signing scheme unverified; API endpoint and event bus have confirmed contracts"

---

### ── CONFIDENCE GAP CHECKPOINT ──

**Field owner**: Risk Assessor

This section is the production site for the Confidence Gap. The compilation table carries a pointer to this section — write the gap here.

**Field rule** [must address a dimension NOT confirmed in Phase 2 Confidence Basis]: Name at least one open question that could change the tier or inertia judgment. Name the question AND the resolution action. The gap must address a dimension not confirmed in Phase 2.

**Self-test** — before finalizing: "Is this gap derivable from Phase 2 Confidence Basis by negating something the Sizing Analyst confirmed?"
- If YES: **you have written a basis-negation — a Phase 2 Risk Assessor charter violation.** Address a dimension Phase 2 did not confirm.
- If NO: proceed.

── DIAGNOSTIC PATTERN ──

WRONG: "Gap: The integration point count may differ from what was estimated."
  FAILURE CLASS: basis-negation
  DETECTION PATTERN: gap negates Phase 2 confirmed content — Sizing Analyst confirmed the count; gap questions the count
  WHY IT FAILS: re-opens what Phase 2 settled; adds no new open question

CORRECT: "Gap: Unknown whether the auth hook requires a custom signing library not in the current dependency tree. Resolution action: confirm with auth team before sprint planning."
  → new dimension not confirmed in Phase 2; named resolution action
────────────────────────────────────────

Write your Confidence Gap: "Gap: {open question — dimension Phase 2 did not confirm}. Resolution action: {named action}."

---

### Phase 3 — Risk Assessor

**Production charter**: Tier-Up Condition, Tier-Down Condition.
**Exclusion list**: Inertia Check, Integration Points, Complexity Tier, Confidence Basis, Confidence Gap.
**Non-access clause**: Do not cite the integration point list, count, tier, or basis from Phase 2 as your Confidence Gap. Those are confirmed facts.

#### Field D — Tier-Up Condition [Risk Assessor]

Name one condition that raises the tier. Reference a specific integration point. Destination tier must be **higher** than the current tier.

| Tier-Up Condition [Risk Assessor] | Integration Point Referenced | Destination Tier [must be HIGHER than current: LOW / MEDIUM / HIGH / XL] |
|---|---|---|
| if {condition} | {integration point} | {destination tier} |

**Read before writing:**
WRONG: Current = HIGH, Destination = HIGH → null-sensitivity: no range
CORRECT: Current = HIGH, Destination = XL → valid upward sensitivity

#### Field E — Tier-Down Condition [Risk Assessor]

Name one condition that lowers the tier. Reference a **different integration point** than Field D. Destination tier must be **lower** than current.

| Tier-Down Condition [Risk Assessor] | Integration Point Referenced [must differ from Field D] | Destination Tier [must be LOWER than current: LOW / MEDIUM / HIGH / XL] |
|---|---|---|
| if {condition} | {different integration point} | {destination tier} |

---

### Output Compilation Table

| Field | [Inertia Auditor] | [Sizing Analyst] | [Risk Assessor] |
|---|---|---|---|
| Inertia Check | {workaround} — {cost direction} | — | — |
| Integration Points | — | {named list} — {N} points | — |
| Complexity Tier | — | {LOW / MEDIUM / HIGH / XL} | — |
| Confidence Basis | — | {evidence + risk driver} | — |
| Confidence Gap [must address dimension not confirmed in Phase 2 Basis] | — | → see CONFIDENCE GAP CHECKPOINT above | — |
| Tier-Up Condition | — | — | if {condition}, becomes {higher tier} |
| Tier-Down Condition | — | — | if {condition}, becomes {lower tier — different integration point} |

---

### Sizing Signals

| Complexity Tier | Team-Size Signal | Timeline Signal |
|---|---|---|
| LOW | 1 specialist | 1 sprint |
| MEDIUM | 1–2 specialists | 2–3 sprints |
| HIGH | 2–3 specialists | 3–5 sprints |
| XL | 3+ specialists | 5+ sprints |

Confidence level: {LOW / MEDIUM / HIGH} — name the primary open question from the Confidence Gap.

---

## V-05 — Maximum Lifecycle Explicitness (Champion Candidate)

**Variation axis (combined)**: Lifecycle emphasis + comprehensive aspirational coverage
**Hypothesis**: Named transition gates between every phase, with the CONFIDENCE GAP CHECKPOINT as an explicit phase gate (not just a section), achieve maximum C-42/C-43 compliance while satisfying all 35 aspirationals. Every structural constraint is encoded at the field level rather than in prose. Four-field DIAGNOSTIC PATTERN (FAILURE CLASS + DETECTION PATTERN + WHY IT FAILS + REMEDIATION) per C-37/C-39. Phase 0 formal precondition table with EVIDENCE and CLEAR-PATH columns for maximum CLOSED-LABEL traceability.

---

You are producing a **sizing signal** for a feature request. This is not a project plan — do not include task breakdowns, sprint assignments, or owner names. Your signals feed `program-plan`.

**Tier vocabulary — exactly one**: **LOW / MEDIUM / HIGH / XL** — nothing else. "MODERATE", "3/5", and "complex" all fail. Downstream skills parse this vocabulary.

Complete phases in order. Each phase gate must be OPEN before the next phase begins.

---

### ── ENTRY GATE ──

Evaluate both preconditions. If any STATUS is BLOCKED, output the CLOSED-LABEL and stop. Do not begin Phase 1.

| Precondition | STATUS (CLEAR / BLOCKED) | CLOSED-LABEL [fill only if BLOCKED; leave blank if CLEAR — format: "Precondition A: [named condition]" or "Precondition B: [named condition]"] |
|---|---|---|
| A — Inertia check viable: you can identify the current workaround or the cost of the feature's absence, and assign a directional cost judgment | CLEAR / BLOCKED | Precondition A: {reason} |
| B — Signal boundary intact: the input requests sizing signals only — no task breakdowns, sprint assignments, owner names, or milestone dates | CLEAR / BLOCKED | Precondition B: {reason} |

**Gate result [produce exactly one]**: `OPEN — both preconditions CLEAR` or `CLOSED — {CLOSED-LABEL value}`

_Phase 1 begins only when gate result = OPEN._

---

### Phase 1 — Sizing Analyst

**Production charter — you produce**: Inertia Check, Integration Points, Complexity Tier, Confidence Basis.
**Exclusion list — you do NOT produce**: Confidence Gap, Tier-Up Condition, Tier-Down Condition.

#### Step 1.1 — Inertia Check [Sizing Analyst]

Name the current workaround or the cost of the feature's absence. Assign exactly one directional label: **cheaper** / **comparable** / **more expensive** (maintaining workaround vs building). Provide a one-sentence cost basis.

Required format: "Workaround: {name}. Maintaining it is {cheaper / comparable / more expensive} than building. Cost basis: {one sentence}."

A workaround named in passing without a cost direction label fails.

#### Step 1.2 — Integration Points [Sizing Analyst]

List each integration point individually as named bullets. Close with the count sentence: "These are {N} integration points."

Example:
- API endpoint (user-facing, confirmed OpenAPI contract)
- Auth hook (token validation, signing scheme unconfirmed)
- Event bus subscription (async delivery, topic and schema confirmed)

These are 3 integration points.

#### Step 1.3 — Complexity Tier [Sizing Analyst]

Assign exactly one tier: **LOW / MEDIUM / HIGH / XL**. Justify by reference to the integration point count from Step 1.2. Name the risk driver — the integration point with the highest implementation uncertainty.

**Read before writing your tier:**

WRONG: "Complexity: HIGH. Feature has several moving parts."
  FAILURE CLASS: no-count-reference
  DETECTION PATTERN: no citation of integration point count; no named risk driver — tier floats without structural anchor
  WHY IT FAILS: downstream skills cannot validate a tier that is not derived from a named count; omitting the risk driver hides peak uncertainty behind an average judgment

CORRECT: "Complexity: HIGH. Three integration points each crossing a trust boundary — that is the threshold for HIGH. Risk driver: auth hook (signing scheme unconfirmed; other two have confirmed contracts)."

#### Step 1.4 — Confidence Basis [Sizing Analyst]

Name the specific evidence behind the tier. Identify which integration point is the risk driver and explain why it carries the highest uncertainty (not average uncertainty).

**Read before writing your basis:**

WRONG: "Basis: General integration complexity based on system knowledge."
  FAILURE CLASS: no-evidence
  DETECTION PATTERN: no specific named facts; no risk driver distinguished — could be copied verbatim to any feature
  WHY IT FAILS: an assertion without evidence cannot be updated when new information arrives; the risk driver field is where escalation decisions are made

CORRECT: "Basis: Three external API dependencies confirmed; each requires auth handshake at trust boundary. Risk driver: auth hook — signing scheme requires verification with auth team before reliable estimation; API endpoint and event bus have confirmed contracts with no blocking unknowns."

---

### ── CONFIDENCE GAP CHECKPOINT ──

**Phase gate**: This checkpoint separates Phase 1 (analysis) from Phase 2 (sensitivity). Complete this section before writing any Phase 2 content. The output compilation table below carries a pointer to this section — write the gap here, not in the compilation table.

**Field owner**: Risk Assessor

**Field definition** [must address a dimension NOT confirmed in Phase 1 Confidence Basis]: Name at least one open question or missing signal that, if resolved, could change the complexity tier or the inertia judgment. Name: (a) the specific open question, and (b) the action that would resolve it. The gap must address a dimension the Sizing Analyst did not confirm in Phase 1.

**Self-test** — before finalizing your gap, answer: "Is this gap derivable from my Phase 1 Confidence Basis by negating or paraphrasing something the Sizing Analyst confirmed?"
- If YES: **you have written a basis-negation — a Phase 2 charter violation.** Address a dimension Phase 1 did not confirm. See REMEDIATION in the DIAGNOSTIC PATTERN below.
- If NO: proceed.

── DIAGNOSTIC PATTERN ──

WRONG: "Gap: The integration point count may differ from the estimate."
  FAILURE CLASS: basis-negation
  DETECTION PATTERN: gap is derivable by negating Phase 1 confirmed content — Sizing Analyst confirmed the integration point count; this gap questions the count
  WHY IT FAILS: a basis-negation re-opens what Phase 1 settled; it names no new open question and adds no information to the sizing signal
  REMEDIATION: identify a dimension Phase 1 did not address — e.g., the operational details of the risk driver (signing scheme implementation class, not just the fact that it is unconfirmed)

CORRECT: "Gap: Unknown whether the auth hook requires a custom signing library not in the current dependency tree. Resolution action: schedule auth team confirmation before sprint planning to avoid a mid-sprint scope change."
  → new dimension (custom signing library — not confirmed in Phase 1); resolution action named
────────────────────────────────────────

Write your Confidence Gap: "Gap: {open question — dimension Phase 1 did not address}. Resolution action: {named action}."

---

### Phase 2 — Risk Assessor

**Production charter — you produce**: Tier-Up Condition, Tier-Down Condition.
**Exclusion list — you do NOT produce**: Inertia Check, Integration Points, Complexity Tier, Confidence Basis, Confidence Gap.
**Non-access clause**: Do not cite the integration point list, count, tier, or rationale from Phase 1 as your Confidence Gap. Those are confirmed facts — the gap must address a dimension not yet confirmed. Specifically: the integration point list, the count, the complexity tier, and the confidence basis rationale are ALL confirmed in Phase 1 and are prohibited as gap content.

#### Step 2.1 — Tier-Up Condition [Risk Assessor]

Name one condition that, if true, would raise the complexity tier. Reference a specific integration point. The destination tier must be **higher** than the current tier.

**Read before writing:**

WRONG: "Tier-Up: If things get more complex, tier goes to HIGH." [current = HIGH → destination = HIGH]
  FAILURE CLASS: null-sensitivity
  DETECTION PATTERN: destination tier equals current tier — sensitivity range is zero; the condition describes no change
  WHY IT FAILS: a tier-up condition where the destination equals the current tier carries no information; it does not bound the upper risk range

CORRECT: "Tier-Up: If the auth hook requires a custom signing library not in the dependency tree, complexity becomes XL." [current = HIGH → XL > HIGH]

Format: "Tier-Up: if {condition}, complexity becomes {destination tier [must be HIGHER than current: LOW / MEDIUM / HIGH / XL]}"

#### Step 2.2 — Tier-Down Condition [Risk Assessor]

Name one condition that, if true, would lower the complexity tier. Reference a **different integration point** than the tier-up condition. The destination tier must be **lower** than the current tier.

Format: "Tier-Down: if {condition}, complexity becomes {destination tier [must be LOWER than current — different integration point from Step 2.1: LOW / MEDIUM / HIGH / XL]}"

---

### ── PHASE 2 COMPLETE ──

Both sensitivity conditions are written. Proceed to the output compilation table.

---

### Output Compilation Table

| Field | [Sizing Analyst] | [Risk Assessor] |
|---|---|---|
| Inertia Check | {workaround} — {cheaper / comparable / more expensive} | — |
| Integration Points | {named list} — {N} points | — |
| Complexity Tier | {LOW / MEDIUM / HIGH / XL} | — |
| Confidence Basis | {specific evidence + risk driver named} | — |
| Confidence Gap [must address dimension not confirmed in Basis — integration points, count, tier, and rationale are all confirmed] | → see CONFIDENCE GAP CHECKPOINT above | — |
| Tier-Up Condition | — | if {condition}, becomes {destination tier [HIGHER than current: LOW / MEDIUM / HIGH / XL]} |
| Tier-Down Condition | — | if {condition}, becomes {destination tier [LOWER than current — different integration point from Tier-Up]} |

---

### Sizing Signals

| Complexity Tier | Team-Size Signal | Timeline Signal |
|---|---|---|
| LOW | 1 specialist | 1 sprint |
| MEDIUM | 1–2 specialists | 2–3 sprints |
| HIGH | 2–3 specialists | 3–5 sprints |
| XL | 3+ specialists | 5+ sprints |

Confidence level: {LOW / MEDIUM / HIGH} — name the primary open question from the Confidence Gap as the driving uncertainty. Note whether its resolution would change the inertia judgment.

---

```json
{"round": 20, "rubric": "v20", "new_criteria": ["C-42", "C-43"], "core_fix": "Standalone gap section before compilation table; defense cluster entirely within standalone section", "v01_axis": "gap-ordering", "v02_axis": "inertia-framing", "v03_axis": "register-single-phase", "v04_axis": "three-role-sequence+table-format", "v05_axis": "lifecycle-emphasis+champion", "champion_candidate": "V-05", "expected_scores": {"V-01": "100", "V-02": "100", "V-03": "87-90", "V-04": "100", "V-05": "100"}}
```
