Written to `simulations/quest/variations/discover-competitors-alt-variations-R6-2026-03-17.md`.

---

## discover-competitors-alt — R6 Variations Summary

All five variations incorporate C-23 through C-26. Target: 180/180.

| Variation | Axis | Key structural innovation |
|-----------|------|--------------------------|
| **V-01** | Role sequence | INERTIA-REF defined inside GATE 4 — clearing the gate IS writing the token; separate 3-col OUTPUT CONTRACT table after PREFLIGHT |
| **V-02** | Output format | 4-column OUTPUT CONTRACT (Slot / Label / Required format / Filled by phase) — "Filled by phase" column creates a forward-link; phases back-reference to close the loop |
| **V-03** | Lifecycle emphasis | OUTPUT CONTRACTS is a subsection inside PREFLIGHT — the entire preamble is one block; phases are pure execution references |
| **V-04** | Combined: V-01 + V-02 | INERTIA-REF in GATE 4 + 4-column OUTPUT CONTRACT — inertia-as-gate + format-specified contract |
| **V-05** | Combined: maximum | PREFLIGHT contains GATE 1–4 + embedded OUTPUT CONTRACTS (4-col); every producing phase annotates its slot; independent coercion templates in competitor Anchor, findings Anchor, and findings INERTIA-REF-DELTA |

**How each new criterion is satisfied across all variations:**

- **C-23**: Every OUTPUT CONTRACT table has a "Required format" column — each slot specifies both a label and a structural format template, not just a name.
- **C-24**: Every producing phase heading includes "(fills [SLOT LABEL] — OUTPUT CONTRACT)" or "(fills [SLOT LABEL] — PREFLIGHT > OUTPUT CONTRACTS)" — back-referencing the exact label declared in the contract.
- **C-25**: Both the competitor table Anchor column (collection phase) and the findings table Anchor column (synthesis phase) carry independent structural format templates — coercion spans the collection-to-synthesis boundary in every variation.
- **C-26**: All four gates (CITATION, ANCHOR, PROOF, INERTIA-REF) are consolidated in a single named PREFLIGHT section before Phase 1 in every variation.
ves them:**

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-23** (slot format spec) | Separate 3-col OUTPUT CONTRACT table with Required format column | 4-col table; Required format is a dedicated column | OUTPUT CONTRACTS subsection inside PREFLIGHT; 3-col table with format per slot | 4-col table after PREFLIGHT | 4-col table embedded in PREFLIGHT with format + producing-phase column |
| **C-24** (phase back-reference) | Phase headings include "(fills [SLOT LABEL] — OUTPUT CONTRACT)" | Phases back-reference slot labels named in "Filled by phase" column | Phase headings cite slot labels from the embedded OUTPUT CONTRACTS subsection | Phase headings carry "(fills [SLOT LABEL] — OUTPUT CONTRACT)" | All producing phases carry "(fills [SLOT LABEL] — PREFLIGHT > OUTPUT CONTRACTS)" |
| **C-25** (cross-table coercion) | Anchor coercion in competitor table (collection) + findings table (synthesis) | Anchor + INERTIA-REF-DELTA coercion in both tables | Anchor coercion in both tables | Anchor coercion in both tables + INERTIA-REF-DELTA coercion in findings table | Independent format templates: competitor Anchor + findings Anchor + findings INERTIA-REF-DELTA |
| **C-26** (consolidated PREFLIGHT) | All 4 gates in PREFLIGHT block before Phase 1 | All 4 gates in PREFLIGHT block | PREFLIGHT contains all 4 gates + OUTPUT CONTRACTS subsection | All 4 gates in PREFLIGHT | PREFLIGHT contains all 4 gates + OUTPUT CONTRACTS subsection |

**Key structural decisions by variation:**

- **V-01:** GATE 4 IS the INERTIA-REF checkpoint — the model writes the token as part of clearing the gate, before any phase. OUTPUT CONTRACT is a separate 3-column table after PREFLIGHT. Phase headings back-reference slot labels (C-24). Anchor coercion in both tables (C-25).
- **V-02:** All gates in PREFLIGHT (C-26). OUTPUT CONTRACT is 4-column (Slot / Label / Required format / Filled by phase) — the "Filled by phase" column creates a forward link; phases close the loop with back-reference annotations (C-24). Both tables coerced on Anchor + INERTIA-REF-DELTA columns (C-25).
- **V-03:** PREFLIGHT is the only preamble section — contains GATE 1–4 (with INERTIA-REF in GATE 4) and an OUTPUT CONTRACTS subsection. Phases are maximally concise. C-24 via phase heading annotations. Both tables coerced (C-25). Most front-loaded variation.
- **V-04:** Combines V-01 (INERTIA-REF in GATE 4) + V-02 (4-column OUTPUT CONTRACT). Preamble is: PREFLIGHT (GATE 1–4, INERTIA-REF in GATE 4) then OUTPUT CONTRACT table. Phase back-references close C-24. Both tables coerced; findings table adds INERTIA-REF-DELTA column coercion.
- **V-05:** Maximum density. PREFLIGHT contains GATE 1–4 (INERTIA-REF in GATE 4) + OUTPUT CONTRACTS subsection (4-column with format + producing-phase). Every producing phase annotates its slot. Competitor table and findings table each have their own independent coercion templates covering Anchor AND INERTIA-REF-DELTA. Most adversarially robust structure.

---

## V-01 — Role sequence (INERTIA-REF defined inside GATE 4)

**Axis:** Role sequence — INERTIA-REF is defined as part of clearing GATE 4 inside the PREFLIGHT block, before any phase begins. The inertia reference frame is not a separate preamble section — it is a gate condition the model must satisfy before execution starts.

**Hypothesis:** Co-locating the INERTIA-REF definition with its enforcement gate (GATE 4) inside PREFLIGHT makes inertia feel integral to the rule architecture rather than bolted on as a separate phase or section. Satisfies C-26 (all gates in PREFLIGHT) and C-22 (token defined once, per-finding citation required) through the same structural move: clearing GATE 4 IS defining the token.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If `focus:` is set (e.g., `focus: market-sizing`, `focus: positioning-framework`), the focus dimension is active. If not supplied, no focus column is added and focus-related outputs pass by vacuous satisfaction.

---

## PREFLIGHT

All gates are defined here. No gate appears outside this block. Phase instructions reference gates by name — apply the named gate when directed.

---

### GATE 1: CITATION GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Citation cell populated | URL from WebSearch present in Citation column of this row | **Citation gate failure** — suppress row; run WebSearch before outputting |
| Citation in row, not footnote | URL is inline in the table row, not in a trailing reference block | **Citation gate failure** — relocate citation into the row |

---

### GATE 2: ANCHOR GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Anchor cell format | `Row C{N}, {attribute}: "{value}"` — row reference, attribute name, and quoted value all present | **Anchor gate failure** — name-only entries do not conform; rewrite the cell before outputting |
| Whitespace absence anchor | Per-row absence evidence: `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested}` per candidate attribute per row | **Whitespace gate failure** — bare assertion without attribute-level evidence does not satisfy; per-row evidence required before outputting the WHITESPACE finding |

NOT ACCEPTABLE: `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE: `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "requires active browser session for all review steps — no async review path"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE declared first | Named cell value (row label, attribute name, quoted value) appears before REDUCTION-1 and REDUCTION-2 | **Proof structure failure** — SOURCE must precede all reduction arguments; constructing an argument before naming the evidence is not allowed |
| Both reductions present | REDUCTION-1 and REDUCTION-2 each answer YES/NO with one sentence showing what is lost when that dimension is removed | **Proof structure failure** — both reductions required; one reduction alone does not establish cross-dimensionality |
| Both reductions answer NO | Neither single-dimension reduction produces the gap | **Proof structure failure** — if either answers YES, find a different gap before outputting THEREFORE |

---

### GATE 4: INERTIA-REF GATE

**Clear this gate before any phase begins.** Write the INERTIA-REF token now, as the act of clearing this gate:

```
INERTIA-REF = [C0 name]: [specific mechanism — switching cost, habit lock-in, or workaround
satisfaction specific to C0's behavior or product feature; not a category label applied generically]
```

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Mechanism specific | Token names a concrete mechanism (switching cost, habit lock-in, or workaround satisfaction) tied to C0's product behavior or feature | **Inertia naming failure** — category label ("high inertia," "strong familiarity," "users are accustomed") is not a mechanism; rewrite INERTIA-REF before any collection begins |
| Per-finding citation | Each finding in Phase 5 cites INERTIA-REF by token name with a verdict and specific C0 mechanism phrase | **Inertia citation failure** — add `vs. INERTIA-REF — [reinforces / challenges / contextualizes]: {C0 mechanism phrase}` before outputting the finding |

---

## OUTPUT CONTRACT

Before any data collection, this skill commits to the following output slots. Each slot specifies its label and required format — arriving at synthesis with a slot in the wrong format constitutes a **collection gate failure**; return to the relevant collecting phase.

| Slot | Label | Required format |
|------|-------|-----------------|
| Inertia anchor | INERTIA-REF | `[C0 name]: [specific mechanism]` — defined in GATE 4 above |
| Competitor row anchor | Anchor column value | `Row C{N}, {attribute}: "{value}"` — row reference + attribute name + quoted value |
| Whitespace gap evidence | Absence evidence block | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` — one line per row per candidate attribute |
| Cross-dimensional source | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` — named cell declared before any reduction argument |
| Per-finding inertia comparison | INERTIA-REF-DELTA | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` |

---

### PHASE 1: CONTEXT

Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills Anchor column value — OUTPUT CONTRACT)

C0 (INERTIA-REF, defined in GATE 4) enters as Row C0 with all columns populated. Run WebSearch for each external competitor before adding its row. Apply GATE 1 and GATE 2 per row before outputting.

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural — fills Anchor column value, OUTPUT CONTRACT): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed and must be rewritten; apply GATE 2 before outputting.

During this phase, also note the specific C0 mechanism phrase from INERTIA-REF that each competitor's mechanism departs from or resembles — this data fills the INERTIA-REF-DELTA slot at Phase 5.

---

### PHASE 3: WHITESPACE (fills Absence evidence block — OUTPUT CONTRACT)

Apply GATE 2 (whitespace absence anchor). For each candidate whitespace attribute, record per row:

```
Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}
```

Then confirm:

```
Gap confirmed: No row provides a non-absent value for [{attribute(s)}] — attribute-level uncontested.
vs. INERTIA-REF: {how the vacant attribute relates to the C0 mechanism from GATE 4}
```

NOT ACCEPTABLE: "No competitor covers this space." — bare assertion — **whitespace gate failure**
NOT ACCEPTABLE: "Competitor 2 reveals a gap in..." — name-only — **anchor gate failure**

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills SOURCE slot — OUTPUT CONTRACT)

Apply GATE 3.

```
SOURCE: {named cell — row label, attribute name, quoted value — fill this slot before writing any
reduction argument; do not proceed to REDUCTION-1 until SOURCE is declared per OUTPUT CONTRACT format}

REDUCTION-1: Competitive map alone — does the gap appear without the focus dimension?
[YES/NO + one sentence showing what is lost when focus is dropped]

REDUCTION-2: Focus dimension alone — does the gap appear without the competitive map?
[YES/NO + one sentence showing what is lost when the map is dropped]

If either answers YES, find a different gap — proceeding is a **proof structure failure**.

THEREFORE: {one sentence — the gap that requires both dimensions simultaneously}
```

---

### PHASE 5: FINDINGS TABLE (fills Anchor column value and INERTIA-REF-DELTA — OUTPUT CONTRACT)

Write 2–5 findings. All findings are rows in the following table. Apply GATE 2 (Anchor) and GATE 4 (INERTIA-REF-DELTA) per row before outputting.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column** (structural — fills Anchor column value, OUTPUT CONTRACT): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed; apply GATE 2.

NOT ACCEPTABLE (Anchor): `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE (Anchor): `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE (Anchor): `Row C3, focus-column: "no SMB pricing tier — enterprise-only positioning visible on pricing page"`

**INERTIA-REF-DELTA column** (structural — fills INERTIA-REF-DELTA, OUTPUT CONTRACT): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` — apply GATE 4; a cell with only "N/A" or a competitor name is malformed; every finding row must cite INERTIA-REF by token name.

For the cross-dimensional finding row: the Claim cell contains the THEREFORE sentence. An adjacent indented block contains SOURCE, REDUCTION-1, REDUCTION-2 — apply GATE 3.

---

### AMEND

Exactly 3 adjustments:

1. **Shift focus dimension**: Replace `{focus_dimension}`. Replace the SOURCE slot (OUTPUT CONTRACT — SOURCE slot) with the new evidentiary anchor. Rewrite REDUCTION-1 and REDUCTION-2 from scratch against the updated focus. Reconstruct THEREFORE. Apply GATE 3 to the rebuilt proof. Writing only a new conclusion without rerunning both reductions is a **proof rerun failure** — both single-dimension reduction arguments must be rebuilt.

2. **Add competitor**: Insert a new row after WebSearch. Apply GATE 1 (CITATION) and GATE 2 (Anchor format — OUTPUT CONTRACT, Anchor column value). Update Phase 3 WHITESPACE absence evidence for all candidate attributes — apply GATE 2 (whitespace absence anchor); a new row may change vacancy status.

3. **Refine INERTIA-REF mechanism** (OUTPUT CONTRACT — INERTIA-REF slot): Replace the INERTIA-REF mechanism sentence with more specific phrasing — name a product feature, workflow step, or workaround behavior. Apply GATE 4 to all Phase 5 findings — update INERTIA-REF-DELTA cells referencing the old mechanism phrase; updated cells must conform to column format.

---

## V-02 — Output format (4-column OUTPUT CONTRACT with bidirectional phase tracing)

**Axis:** Output format — the OUTPUT CONTRACT is a 4-column table (Slot / Label / Required format / Filled by phase). The "Filled by phase" column creates a forward declaration: the contract names which phase is responsible for each slot. Each named phase back-references its slot label to close the bidirectional link. C-23 is satisfied by the Required format column; C-24 is satisfied by the forward-link column plus phase back-references.

**Hypothesis:** A "Filled by phase" column in the OUTPUT CONTRACT makes the phase-to-slot mapping machine-readable. When a phase heading cites its slot label, the tracing is visible in both directions without reading prose — the contract names the phase, the phase names the slot. This produces C-24 compliance through table structure rather than prose annotation.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If `focus:` is set, the focus dimension is active. If not supplied, no focus column is added.

---

## PREFLIGHT

All gates are defined here before any execution phase. No gate appears outside this block.

---

### GATE 1: CITATION GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Citation cell populated | URL from WebSearch present in Citation column of this row | **Citation gate failure** — suppress row; run WebSearch before outputting |
| Citation in row, not footnote | URL is inline in the table row, not in a trailing reference block | **Citation gate failure** — relocate citation into the row |

---

### GATE 2: ANCHOR GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Anchor cell format | `Row C{N}, {attribute}: "{value}"` — row reference, attribute name, and quoted value all present | **Anchor gate failure** — name-only entries do not conform; rewrite before outputting |
| Whitespace absence anchor | Per-row evidence: `Row C{N} — {attribute}: {absent}` per candidate attribute | **Whitespace gate failure** — bare assertion does not satisfy; attribute-level per-row evidence required |

NOT ACCEPTABLE: `Competitor 2 reveals that...` — name-only — **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "embeds review workflow into GitHub PR threads — no standalone async review mode"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE declared first | Named cell value appears before REDUCTION-1 and REDUCTION-2 | **Proof structure failure** — SOURCE must precede all reduction arguments |
| Both reductions present | REDUCTION-1 and REDUCTION-2 each answer YES/NO with one sentence showing what is lost | **Proof structure failure** — both required; one reduction does not establish cross-dimensionality |
| Both reductions answer NO | Neither single-dimension reduction produces the gap | **Proof structure failure** — if either YES, find a different gap |

---

### GATE 4: INERTIA-REF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Mechanism specific | INERTIA-REF names a concrete mechanism (switching cost, habit lock-in, or workaround satisfaction) tied to C0's product behavior or feature — not a category label | **Inertia naming failure** — rewrite INERTIA-REF before any collection begins |
| Per-finding citation | Each finding cites INERTIA-REF by token name: `vs. INERTIA-REF — {verdict}: {mechanism phrase}` | **Inertia citation failure** — add the comparison clause before outputting the finding |

---

## OUTPUT CONTRACT

Before any data collection, this skill commits to the following output slots. Each slot specifies its label, the required format for the value that fills it, and the phase responsible for filling it. That phase back-references this slot by its exact label at the point of production.

| Slot | Label | Required format | Filled by phase |
|------|-------|-----------------|-----------------|
| Inertia anchor | INERTIA-REF | `[C0 name]: [specific mechanism]` | Phase 2 — Inertia Assessment |
| Competitor row anchor | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 3 — Competitor Table |
| Whitespace gap evidence | Absence evidence block | `Row C{N} — {attribute}: {absent / "None" / "N/A"}` per row per attribute | Phase 4 — Whitespace |
| Cross-dimensional source | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` | Phase 5 — Cross-Dimensional Finding |
| Per-finding inertia comparison | INERTIA-REF-DELTA column value | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {C0 mechanism phrase}` | Phase 6 — Findings Table |

A slot filled in the wrong format constitutes a **collection gate failure** — return to the named producing phase.

---

### PHASE 1: CONTEXT

Read repo context. Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: INERTIA ASSESSMENT (fills INERTIA-REF slot — OUTPUT CONTRACT)

Identify C0 — the status quo behavior, tool, or approach the target user relies on today. Define:

```
INERTIA-REF = [C0 name]: [specific mechanism — switching cost, habit lock-in, or workaround
satisfaction; specific to C0's product behavior or feature, not a generic category label]
```

Apply GATE 4 (mechanism check) before continuing. C0 enters the competitor table as Row C0.

---

### PHASE 3: COMPETITOR TABLE (fills Anchor column value — OUTPUT CONTRACT)

Run WebSearch per external competitor. Apply GATE 1 and GATE 2 per row before outputting.

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural — fills Anchor column value slot, OUTPUT CONTRACT): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed; apply GATE 2.

NOT ACCEPTABLE: `Competitor 3` or `Competitor 3 — high threat` — name-only — **anchor gate failure**
ACCEPTABLE: `Row C3, focus-column: "positions as developer-first; no manager dashboards in published feature set"`

---

### PHASE 4: WHITESPACE (fills Absence evidence block — OUTPUT CONTRACT)

Apply GATE 2 (whitespace absence anchor). Per candidate whitespace attribute per row:

```
Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}
```

Then confirm:

```
Gap confirmed: No row provides a non-absent value for [{attribute(s)}] — attribute-level uncontested.
vs. INERTIA-REF: {how the vacant attribute relates to the C0 mechanism}
```

NOT ACCEPTABLE: "No competitor covers this space." — bare assertion — **whitespace gate failure**

---

### PHASE 5: CROSS-DIMENSIONAL FINDING (fills SOURCE slot — OUTPUT CONTRACT)

Apply GATE 3.

```
SOURCE: {named cell — row label, attribute name, quoted value — declare before any reduction argument;
do not proceed to REDUCTION-1 until SOURCE is filled per OUTPUT CONTRACT format}

REDUCTION-1: Competitive map alone — gap absent without focus? [YES/NO + one sentence showing what is lost]

REDUCTION-2: Focus dimension alone — gap absent without map? [YES/NO + one sentence showing what is lost]

If either answers YES, find a different gap — proceeding is a **proof structure failure**.

THEREFORE: {one sentence requiring both dimensions simultaneously}
```

---

### PHASE 6: FINDINGS TABLE (fills Anchor column value and INERTIA-REF-DELTA column value — OUTPUT CONTRACT)

All findings are rows in the following table. Apply GATE 2 (Anchor) and GATE 4 (INERTIA-REF-DELTA) per row before outputting.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Column format constraints (structural — entries not matching these shapes are syntactically malformed; apply the named gate before outputting the row):**

- **Anchor** (fills Anchor column value slot, OUTPUT CONTRACT): `Row C{N}, {attribute}: "{value}"` — apply GATE 2
  - NOT ACCEPTABLE: `Competitor 2 reveals that...` — name-only — **anchor gate failure**
  - NOT ACCEPTABLE: `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
  - ACCEPTABLE: `Row C2, mechanism: "enforces daily standup via calendar lock — no async standup mode"`

- **INERTIA-REF-DELTA** (fills INERTIA-REF-DELTA column value slot, OUTPUT CONTRACT): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` — apply GATE 4; "N/A" or a competitor name is malformed; every finding row must cite INERTIA-REF by token name

For the cross-dimensional finding row: Claim cell contains THEREFORE. An adjacent indented block contains SOURCE, REDUCTION-1, REDUCTION-2 — apply GATE 3.

---

### AMEND

Exactly 3 adjustments:

1. **Shift focus dimension**: Replace `{focus_dimension}`. Replace SOURCE slot (OUTPUT CONTRACT — SOURCE slot, Filled by Phase 5) with new evidentiary anchor. Rewrite REDUCTION-1 and REDUCTION-2 from scratch against the updated focus. Reconstruct THEREFORE. Apply GATE 3. Writing only a new THEREFORE clause without rerunning both reductions is a **proof rerun failure**.

2. **Add competitor**: Insert new row after WebSearch. Apply GATE 1 (CITATION) and GATE 2 (Anchor format — OUTPUT CONTRACT, Anchor column value). Update Phase 4 WHITESPACE absence evidence for all candidate attributes; apply GATE 2 (whitespace absence anchor).

3. **Refine INERTIA-REF mechanism** (OUTPUT CONTRACT — INERTIA-REF slot, Filled by Phase 2): Replace mechanism sentence with more specific phrasing. Apply GATE 4 to all Phase 6 findings — rewrite INERTIA-REF-DELTA cells referencing the old mechanism phrase; updated cells must conform to column format.

---

## V-03 — Lifecycle emphasis (OUTPUT CONTRACTS embedded inside PREFLIGHT)

**Axis:** Lifecycle emphasis — the entire preamble (all gates plus OUTPUT CONTRACTS) is a single PREFLIGHT section. INERTIA-REF is defined inside GATE 4. OUTPUT CONTRACTS is a named subsection of PREFLIGHT, not a separate block. Phases are the most concise execution instructions of any variation.

**Hypothesis:** When PREFLIGHT is the only preamble section and contains all rule definitions plus all output shape declarations, the skill is auditable from the preamble alone. A reviewer can verify compliance without reading any execution phase. The test is whether this ultra-concentrated front-loading is cleaner or impenetrable.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If `focus:` is set, the focus dimension is active. If not supplied, no focus column is added.

---

## PREFLIGHT

Everything needed to execute this skill is defined here: all gates and all output shape declarations. Phases are execution instructions only — they apply gates and fill slots named in this section.

---

### GATE 1: CITATION GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Citation cell populated | URL from WebSearch in Citation column of this row | **Citation gate failure** — suppress row; run WebSearch first |
| Citation in row, not footnote | URL is inline in the row, not in trailing reference block | **Citation gate failure** — relocate into the row |

---

### GATE 2: ANCHOR GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Anchor cell format | `Row C{N}, {attribute}: "{value}"` — row reference + attribute name + quoted value all present | **Anchor gate failure** — name-only entries do not conform; rewrite before outputting |
| Whitespace absence anchor | `Row C{N} — {attribute}: {absent}` per row per candidate attribute | **Whitespace gate failure** — per-row attribute evidence required; bare assertion does not satisfy |

NOT ACCEPTABLE: `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE: `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "locks review workflow inside PR diff view — no standalone review session"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE first | Named cell (row, attribute, quoted value) appears before REDUCTION-1 | **Proof structure failure** — SOURCE must precede all reductions |
| Both reductions present | REDUCTION-1 and REDUCTION-2 each answer YES/NO + one sentence showing what is lost | **Proof structure failure** — both required |
| Both answer NO | Neither dimension alone produces the gap | **Proof structure failure** — if either YES, find a different gap |

---

### GATE 4: INERTIA-REF GATE

Before any phase executes, define the reference frame. Write the token as part of clearing this gate:

```
INERTIA-REF = [C0 name]: [specific mechanism — switching cost, habit lock-in, or workaround
satisfaction; tied to C0's specific product feature or behavior, not a category label]
```

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Mechanism specific | Token names a concrete mechanism specific to C0's product behavior or feature | **Inertia naming failure** — category label is not a mechanism; rewrite before any phase begins |
| Per-finding citation | Each finding cites INERTIA-REF by token name with verdict + C0 mechanism phrase | **Inertia citation failure** — add `vs. INERTIA-REF — {verdict}: {phrase}` before outputting |

---

### OUTPUT CONTRACTS

Output slots required by synthesis phases. Each slot specifies its label and required format. Producing phases fill these slots by name and back-reference them at the point of production.

| Slot | Label | Required format |
|------|-------|-----------------|
| Inertia anchor | INERTIA-REF | `[C0 name]: [specific mechanism]` — defined in GATE 4 |
| Competitor row anchor | Anchor column | `Row C{N}, {attribute}: "{value}"` |
| Whitespace evidence | Absence evidence block | `Row C{N} — {attribute}: {absent / "None" / "N/A"}` per row per attribute |
| Cross-dimensional source | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` |
| Per-finding inertia delta | INERTIA-REF-DELTA | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {C0 mechanism phrase}` |

A slot arrived at in the wrong format constitutes a **collection gate failure** — return to the producing phase.

---

### PHASE 1: CONTEXT

Read repo context. Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills Anchor column — PREFLIGHT > OUTPUT CONTRACTS)

C0 (INERTIA-REF, defined in GATE 4) is Row C0. Run WebSearch per external competitor. Apply GATE 1 and GATE 2 per row.

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

Anchor column (structural): `Row C{N}, {attribute}: "{value}"` — syntactically malformed cells trigger GATE 2 before rule evaluation.

---

### PHASE 3: WHITESPACE (fills Absence evidence block — PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 2 (whitespace absence anchor). Per candidate attribute per row:

```
Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}
```

Then confirm:

```
Gap confirmed: No row provides a non-absent value for [{attribute(s)}] — attribute-level uncontested.
vs. INERTIA-REF: {how the vacant attribute relates to the C0 mechanism from GATE 4}
```

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills SOURCE slot — PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 3.

```
SOURCE: {named cell — row, attribute, quoted value — fill before writing any reduction argument}

REDUCTION-1: Map alone — gap absent without focus? [YES/NO + one sentence showing what is lost]
REDUCTION-2: Focus alone — gap absent without map? [YES/NO + one sentence showing what is lost]

THEREFORE: {one sentence requiring both dimensions simultaneously}
```

---

### PHASE 5: FINDINGS TABLE (fills Anchor column and INERTIA-REF-DELTA — PREFLIGHT > OUTPUT CONTRACTS)

All findings are rows in the following table. Apply GATE 2 (Anchor) and GATE 4 (INERTIA-REF-DELTA) per row.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor** (structural): `Row C{N}, {attribute}: "{value}"` — GATE 2 applies; name-only cells are malformed.

**INERTIA-REF-DELTA** (structural): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {C0 mechanism phrase}` — GATE 4 applies; "N/A" or empty is malformed.

For the cross-dimensional finding row: Claim contains THEREFORE; adjacent block contains SOURCE, REDUCTION-1, REDUCTION-2 — apply GATE 3.

---

### AMEND

Exactly 3 adjustments:

1. **Shift focus dimension**: Replace `{focus_dimension}`. Replace SOURCE slot (PREFLIGHT > OUTPUT CONTRACTS — SOURCE slot) with new anchor. Rewrite REDUCTION-1 and REDUCTION-2 from scratch. Reconstruct THEREFORE. Apply GATE 3. Writing only a new conclusion without rerunning both reductions is a **proof rerun failure**.

2. **Add competitor**: Insert row after WebSearch. Apply GATE 1 and GATE 2. Recheck Phase 3 absence evidence for all candidate attributes — apply GATE 2 (whitespace absence anchor).

3. **Refine INERTIA-REF mechanism** (PREFLIGHT > GATE 4 / OUTPUT CONTRACTS — INERTIA-REF slot): Replace mechanism sentence with more specific phrasing. Apply GATE 4 to all Phase 5 findings — update INERTIA-REF-DELTA cells referencing the old mechanism phrase; updated cells must conform to column format.

---

## V-04 — Combined: INERTIA-REF in GATE 4 + 4-column OUTPUT CONTRACT table

**Axes combined:** Role sequence (INERTIA-REF defined inside GATE 4 of PREFLIGHT, as in V-01) + Output format (4-column OUTPUT CONTRACT table with "Filled by phase" column, as in V-02).

**Hypothesis:** Combining inertia-as-gate with a format-specified 4-column contract creates the strongest preamble: the gravitational reference frame (INERTIA-REF) is established inside its enforcement gate (GATE 4), and the output shape is a machine-checkable table where each slot names its producing phase. Phase back-references close the bidirectional link. The preamble is more coherent than either axis alone because each element has a defined purpose — PREFLIGHT is rules, OUTPUT CONTRACT is shapes.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If `focus:` is set, the focus dimension is active. If not supplied, no focus column is added.

---

## PREFLIGHT

All gates are defined here. No gate appears outside this block.

---

### GATE 1: CITATION GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Citation cell populated | URL from WebSearch present in Citation column of this row | **Citation gate failure** — suppress row; run WebSearch before outputting |
| Citation in row, not footnote | URL is inline in the table row, not in a trailing reference block | **Citation gate failure** — relocate into the row |

---

### GATE 2: ANCHOR GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Anchor cell format | `Row C{N}, {attribute}: "{value}"` — row reference, attribute name, and quoted value all present | **Anchor gate failure** — name-only entries do not conform; rewrite before outputting |
| Whitespace absence anchor | Per-row evidence: `Row C{N} — {attribute}: {absent}` per candidate attribute | **Whitespace gate failure** — attribute-level per-row evidence required before outputting WHITESPACE finding |

NOT ACCEPTABLE: `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE: `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "stores all decisions in email threads — no structured decision log available"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE declared first | Named cell value appears before REDUCTION-1 and REDUCTION-2 | **Proof structure failure** — SOURCE must precede all reduction arguments |
| Both reductions present | REDUCTION-1 and REDUCTION-2 each answer YES/NO with one sentence showing what is lost | **Proof structure failure** — both reductions required |
| Both reductions answer NO | Neither single-dimension reduction produces the gap | **Proof structure failure** — if either YES, find a different gap before outputting THEREFORE |

---

### GATE 4: INERTIA-REF GATE

**Clear this gate before any phase begins.** Write the INERTIA-REF token now, as the act of clearing this gate:

```
INERTIA-REF = [C0 name]: [specific mechanism — switching cost, habit lock-in, or workaround
satisfaction specific to C0's behavior or product feature; not a category label]
```

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Mechanism specific | Token names a concrete mechanism tied to C0's product behavior or feature | **Inertia naming failure** — category label is not a mechanism; rewrite before any phase begins |
| Per-finding citation | Each finding cites INERTIA-REF by token name with verdict and specific C0 mechanism phrase | **Inertia citation failure** — add `vs. INERTIA-REF — {verdict}: {phrase}` before outputting |

---

## OUTPUT CONTRACT

| Slot | Label | Required format | Filled by phase |
|------|-------|-----------------|-----------------|
| Inertia anchor | INERTIA-REF | `[C0 name]: [specific mechanism]` | GATE 4 (PREFLIGHT, above) |
| Competitor row anchor | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 — Competitor Table |
| Whitespace evidence | Absence evidence block | `Row C{N} — {attribute}: {absent / "None" / "N/A"}` per row per attribute | Phase 3 — Whitespace |
| Cross-dimensional source | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` | Phase 4 — Cross-Dimensional Finding |
| Per-finding inertia comparison | INERTIA-REF-DELTA | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {C0 mechanism phrase}` | Phase 5 — Findings Table |

A slot filled in the wrong format constitutes a **collection gate failure**. The producing phase named in the rightmost column is responsible; return to it.

---

### PHASE 1: CONTEXT

Read repo context. Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills Anchor column value — OUTPUT CONTRACT)

C0 (INERTIA-REF, defined in GATE 4) is Row C0. Run WebSearch per external competitor. Apply GATE 1 and GATE 2 per row before outputting.

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural — OUTPUT CONTRACT, Anchor column value): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed; apply GATE 2 before outputting.

During collection, note mechanism phrases and focus-column values per row — this data fills the INERTIA-REF-DELTA slot in Phase 5.

---

### PHASE 3: WHITESPACE (fills Absence evidence block — OUTPUT CONTRACT)

Apply GATE 2 (whitespace absence anchor). Per candidate attribute per row:

```
Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}
```

Then confirm:

```
Gap confirmed: No row provides a non-absent value for [{attribute(s)}] — attribute-level uncontested.
vs. INERTIA-REF: {how the vacant attribute relates to the C0 mechanism from GATE 4}
```

NOT ACCEPTABLE: "No competitor covers this space." — bare assertion — **whitespace gate failure**

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills SOURCE slot — OUTPUT CONTRACT)

Apply GATE 3.

```
SOURCE: {named cell — row label, attribute name, quoted value — declared first, before any
reduction argument; do not proceed to REDUCTION-1 until this slot is filled per OUTPUT CONTRACT format}

REDUCTION-1: Map alone — gap absent without focus? [YES/NO + one sentence showing what is lost]

REDUCTION-2: Focus alone — gap absent without map? [YES/NO + one sentence showing what is lost]

If either answers YES, find a different gap — proceeding is a **proof structure failure**.

THEREFORE: {one sentence requiring both dimensions simultaneously}
```

---

### PHASE 5: FINDINGS TABLE (fills Anchor column value and INERTIA-REF-DELTA — OUTPUT CONTRACT)

All findings are rows in the following table. Apply GATE 2 (Anchor) and GATE 4 (INERTIA-REF-DELTA) per row before outputting.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column** (structural — OUTPUT CONTRACT, Anchor column value): `Row C{N}, {attribute}: "{value}"` — apply GATE 2; name-only cells are syntactically malformed.

NOT ACCEPTABLE (Anchor): `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE (Anchor): `As Competitor 3 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE (Anchor): `Row C3, focus-column: "no free tier in public pricing — minimum contract required for access"`

**INERTIA-REF-DELTA column** (structural — OUTPUT CONTRACT, INERTIA-REF-DELTA): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` — apply GATE 4; "N/A" or empty is malformed; every finding row must cite INERTIA-REF by token name.

For the cross-dimensional finding row: Claim cell contains THEREFORE; adjacent indented block contains SOURCE, REDUCTION-1, REDUCTION-2 — apply GATE 3.

---

### AMEND

Exactly 3 adjustments:

1. **Shift focus dimension**: Replace `{focus_dimension}`. Replace SOURCE slot (OUTPUT CONTRACT — SOURCE slot, Filled by Phase 4) with new evidentiary anchor. Rewrite REDUCTION-1 and REDUCTION-2 from scratch against the updated focus. Reconstruct THEREFORE. Apply GATE 3. Writing only a new conclusion without rerunning both reductions is a **proof rerun failure** — both single-dimension reduction arguments must be rebuilt.

2. **Add competitor**: Insert new row after WebSearch. Apply GATE 1 (CITATION) and GATE 2 (Anchor format — OUTPUT CONTRACT, Anchor column value, Filled by Phase 2). Update Phase 3 absence evidence for all candidate attributes — apply GATE 2 (whitespace absence anchor).

3. **Refine INERTIA-REF mechanism** (OUTPUT CONTRACT — INERTIA-REF, Filled by GATE 4): Replace mechanism sentence with more specific phrasing — name a product feature, workaround step, or workflow behavior. Apply GATE 4 to all Phase 5 findings — rewrite INERTIA-REF-DELTA cells referencing the old mechanism phrase; updated cells must conform to column format.

---

## V-05 — Combined: maximum density (all four new patterns at peak expression)

**Axes combined:** Role sequence (INERTIA-REF in GATE 4 of PREFLIGHT) + Lifecycle emphasis (OUTPUT CONTRACTS embedded inside PREFLIGHT as a subsection) + Output format (4-column OUTPUT CONTRACT with format shapes + producing-phase column) + Cross-table coercion (independent format templates in competitor table Anchor column, findings table Anchor column, and findings table INERTIA-REF-DELTA column) + Phase back-references (every producing phase annotates the slot it fills using the exact label from OUTPUT CONTRACTS).

**Hypothesis:** When all four new patterns operate simultaneously at maximum expression — inertia co-located with its gate, output shapes co-located with the gate block, bidirectional tracing, and structural coercion propagated independently across both collection and synthesis tables — the skill becomes self-documenting and self-enforcing. The test is whether maximum integration remains readable or collapses under formalism density.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If `focus:` is set, the focus dimension is active. If not supplied, no focus column is added.

---

## PREFLIGHT

All rules and output shape declarations are defined in this section. No gate appears outside this block. Phases are execution instructions that reference this section by name.

---

### GATE 1: CITATION GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Citation cell populated | URL from WebSearch present in Citation column of this row | **Citation gate failure** — suppress row; run WebSearch before outputting |
| Citation in row, not footnote | URL is inline in the table row, not in a trailing reference block | **Citation gate failure** — relocate into the row |
| URL is a direct URL | Cell contains an actual URL — not "official site," bare domain, or prose reference | **Citation gate failure** — replace with a direct URL from WebSearch |

---

### GATE 2: ANCHOR GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Anchor cell format | `Row C{N}, {attribute}: "{value}"` — row reference, attribute name, and quoted value all present | **Anchor gate failure** — name-only or label-only entries do not conform; rewrite before outputting |
| Attribute explicitly named | Anchor cell names the attribute type (threat, mechanism, focus column, etc.) | **Anchor gate failure** — attribute type must be present in addition to the quoted value |
| Whitespace absence anchor | `Row C{N} — {attribute}: {absent}` per row per candidate attribute | **Whitespace gate failure** — per-row attribute-level evidence required |

NOT ACCEPTABLE: `Competitor 2 — mechanism: "high"` — no Row prefix, no quoted value — **anchor gate failure**
NOT ACCEPTABLE: `Competitor 3` — name-only — **anchor gate failure**
ACCEPTABLE: `Row C3, mechanism: "bundles review workflow into CI pipeline — review not separable from build status"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE declared first | Named cell value (row, attribute, quoted value) appears before REDUCTION-1 and REDUCTION-2 | **Proof structure failure** — SOURCE must precede all reduction arguments; argument-before-evidence not allowed |
| Both reductions present | REDUCTION-1 and REDUCTION-2 each answer YES/NO with one sentence showing what is lost when that dimension is removed | **Proof structure failure** — both required; one reduction alone does not establish cross-dimensionality |
| Both answer NO | Neither dimension alone produces the gap | **Proof structure failure** — if either YES, find a different gap before outputting THEREFORE |

---

### GATE 4: INERTIA-REF GATE

**Clear this gate before any phase begins.** Write the INERTIA-REF token as part of clearing this gate:

```
INERTIA-REF = [C0 name]: [specific mechanism — switching cost, habit lock-in, or workaround
satisfaction specific to C0's behavior or product feature; not a category label applied generically]
```

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Mechanism specific | Token names a concrete mechanism (switching cost, habit lock-in, or workaround satisfaction) tied to C0's product behavior or feature | **Inertia naming failure** — category label is not a mechanism; rewrite INERTIA-REF before any collection begins |
| Per-finding citation | Each finding cites INERTIA-REF by token name: `vs. INERTIA-REF — {verdict}: {C0 mechanism phrase}` | **Inertia citation failure** — add the comparison clause before outputting the finding |

---

### OUTPUT CONTRACTS

Output slots required by synthesis phases. Each slot specifies its label, the required format for the value that fills it, and the phase responsible for filling it. That phase back-references this slot by its exact label at the point of production.

| Slot | Label | Required format | Filled by phase |
|------|-------|-----------------|-----------------|
| Inertia anchor | INERTIA-REF | `[C0 name]: [specific mechanism]` | GATE 4 (this section) |
| Competitor row anchor | Anchor column | `Row C{N}, {attribute}: "{value}"` | Phase 2 — Competitor Table |
| Whitespace evidence | Absence evidence block | `Row C{N} — {attribute}: {absent / "None" / "N/A"}` per row per attribute | Phase 3 — Whitespace |
| Cross-dimensional source | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` | Phase 4 — Cross-Dimensional Finding |
| Per-finding inertia delta | INERTIA-REF-DELTA | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {C0 mechanism phrase}` | Phase 5 — Findings Table |

A slot arrived at in the wrong format constitutes a **collection gate failure** — return to the named phase.

---

### PHASE 1: CONTEXT

Read repo context. Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills Anchor column — PREFLIGHT > OUTPUT CONTRACTS)

C0 (INERTIA-REF, defined in GATE 4) is Row C0. Run WebSearch per external competitor. Apply GATE 1 and GATE 2 per row before outputting.

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural — fills Anchor column slot, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — cells not conforming to this shape are syntactically malformed; GATE 2 applies before rule evaluation.

During collection, note mechanism phrases, focus-column values, and the specific C0 mechanism contrast for each row — this data fills the INERTIA-REF-DELTA slot at Phase 5.

---

### PHASE 3: WHITESPACE (fills Absence evidence block — PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 2 (whitespace absence anchor). Per candidate attribute per row:

```
Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}
```

Then confirm:

```
Gap confirmed: No row provides a non-absent value for [{attribute(s)}] — attribute-level uncontested.
vs. INERTIA-REF: {how the vacant attribute relates to the C0 mechanism from GATE 4}
```

NOT ACCEPTABLE: "No competitor covers this space." — bare assertion — **whitespace gate failure**
NOT ACCEPTABLE: "Competitor 2 reveals a gap in..." — name-only — **anchor gate failure**

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills SOURCE slot — PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 3.

```
SOURCE: {named cell — row label, attribute name, quoted value — declared first, before any reduction
argument; do not proceed to REDUCTION-1 until this slot is filled per OUTPUT CONTRACTS format}

REDUCTION-1: Competitive map alone — gap absent without focus? [YES/NO + one sentence showing what is lost]

REDUCTION-2: Focus dimension alone — gap absent without map? [YES/NO + one sentence showing what is lost]

If either answers YES, find a different gap — proceeding is a **proof structure failure**.

THEREFORE: {one sentence requiring both dimensions simultaneously}
```

---

### PHASE 5: FINDINGS TABLE (fills Anchor column and INERTIA-REF-DELTA — PREFLIGHT > OUTPUT CONTRACTS)

All findings are rows in the following table. Apply GATE 2 (Anchor) and GATE 4 (INERTIA-REF-DELTA) per row before outputting.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Column format constraints (structural — entries not matching these shapes are syntactically malformed; apply the named gate before outputting the row):**

- **Anchor column** (fills Anchor column slot, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — apply GATE 2
  - NOT ACCEPTABLE: `Competitor 2 reveals that...` — name-only — **anchor gate failure**
  - NOT ACCEPTABLE: `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
  - ACCEPTABLE: `Row C2, mechanism: "enforces synchronous daily standup via calendar lock — no async alternative"`

- **INERTIA-REF-DELTA column** (fills INERTIA-REF-DELTA slot, PREFLIGHT > OUTPUT CONTRACTS): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` — apply GATE 4; "N/A," empty, or a competitor name is malformed; every finding row must cite INERTIA-REF by token name
  - NOT ACCEPTABLE: `N/A` — empty comparison — **inertia citation failure**
  - NOT ACCEPTABLE: `Competitor 2 uses a different approach` — no token citation — **inertia citation failure**
  - ACCEPTABLE: `vs. INERTIA-REF — challenges: C0 uses spreadsheet habit lock-in; C2 uses calendar scheduling lock-in instead`

For the cross-dimensional finding row: Claim cell contains THEREFORE; adjacent indented block contains SOURCE, REDUCTION-1, REDUCTION-2 — apply GATE 3.

---

### AMEND

Exactly 3 adjustments:

1. **Shift focus dimension**: Replace `{focus_dimension}`. Replace SOURCE slot (PREFLIGHT > OUTPUT CONTRACTS — SOURCE slot, Filled by Phase 4) with new evidentiary anchor. Rewrite REDUCTION-1 and REDUCTION-2 from scratch against the updated focus. Reconstruct THEREFORE. Apply GATE 3 to the rebuilt proof block. Writing only a new THEREFORE clause without rerunning both reductions is a **proof rerun failure** — the reconstruction of both single-dimension reduction arguments is what makes the proof valid; the conclusion alone does not.

2. **Add competitor**: Insert new row after WebSearch. Apply GATE 1 (CITATION) and GATE 2 (Anchor format — PREFLIGHT > OUTPUT CONTRACTS, Anchor column slot, Filled by Phase 2) to the new row. Update Phase 3 absence evidence for all candidate attributes — apply GATE 2 (whitespace absence anchor); a new row may change vacancy status for any attribute.

3. **Refine INERTIA-REF mechanism** (PREFLIGHT > OUTPUT CONTRACTS — INERTIA-REF slot, Filled by GATE 4): Replace mechanism sentence with more specific phrasing — name a product feature, workflow step, or workaround behavior rather than a category. Apply GATE 4 to all Phase 5 findings — rewrite all INERTIA-REF-DELTA cells referencing the old mechanism phrase; updated cells must conform to column format before outputting.
