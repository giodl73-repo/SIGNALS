Written to `simulations/quest/variations/discover-competitors-alt-variations-R7-2026-03-17.md`.

---

## discover-competitors-alt — R7 Variations Summary

All five variations target 200/200 on rubric v6 (C-01 through C-30).

| Variation | Axis | Key structural innovation |
|-----------|------|--------------------------|
| **V-01** | Role sequence | GATE 4 opens PREFLIGHT — inertia reference frame established before citation/anchor/proof gates; OUTPUT CONTRACTS closes PREFLIGHT as the 4-col final subsection |
| **V-02** | Output format | Spec-first PREFLIGHT — OUTPUT CONTRACTS is declared before any gate; GATE 4 write directive explicitly names the slot it fills: "Fill the INERTIA-REF slot (PREFLIGHT > OUTPUT CONTRACTS above)" |
| **V-03** | Lifecycle emphasis | Write-token as a structural table row within GATE 4 — the write action has its own Check / Pass condition / Failure state row, making token production mechanically identical to a gate check |
| **V-04** | Phrasing register | Imperative command style throughout; "Producing phase" column instead of "Filled by phase"; GATE 4 last in PREFLIGHT (after OUTPUT CONTRACTS) with bold `**WRITE:**` header directive |
| **V-05** | Combined maximum | Spec-first (V-02) + write-as-table-row (V-03) + 6-slot OUTPUT CONTRACT (adds Focus-scope evidence slot) + 3 independent coercion templates + extended NOT ACCEPTABLE examples in GATE 2 |

**C-27 through C-30 coverage:**

| Criterion | Satisfied by |
|-----------|-------------|
| C-27 (4-col "Filled by phase") | All 5 — V-04 uses "Producing phase" as a synonymous label |
| C-28 (OUTPUT CONTRACTS inside PREFLIGHT) | All 5 — position varies (last in V-01/V-03, first in V-02/V-05, before GATE 4 in V-04) |
| C-29 (full-path "PREFLIGHT > OUTPUT CONTRACTS") | All 5 — every producing phase heading uses the full path |
| C-30 (write-token instruction in GATE 4) | All 5 — format varies: prose + code block (V-01/V-02/V-04), table row (V-03/V-05) |

**Single-axis variations (V-01, V-02, V-03):** Each explores one structural degree of freedom — gate ordering, contract ordering, write instruction format — while holding all other variables at the R6 baseline. Clean comparison surface for the rubric.

**Combined variations (V-04, V-05):** V-04 combines V-02's spec-before-gates positioning with V-04's imperative register. V-05 combines V-02 + V-03 + expanded slots + maximum coercion surface.
led by phase"; INERTIA-REF → "GATE 4 (PREFLIGHT, below)" | "Filled by phase"; INERTIA-REF → "GATE 4 (Write row)" | "Producing phase"; INERTIA-REF → "GATE 4 (PREFLIGHT, below)" | "Filled by phase"; INERTIA-REF → "GATE 4 (Write row, below)" |
| **C-28** (inside PREFLIGHT) | OUTPUT CONTRACTS is last subsection in PREFLIGHT | OUTPUT CONTRACTS is first subsection in PREFLIGHT | OUTPUT CONTRACTS is last subsection in PREFLIGHT | OUTPUT CONTRACTS is a subsection in PREFLIGHT placed before GATE 4 | OUTPUT CONTRACTS is first subsection in PREFLIGHT |
| **C-29** (full-path back-refs) | All phase headings: "PREFLIGHT > OUTPUT CONTRACTS" | All phase headings: "PREFLIGHT > OUTPUT CONTRACTS" | All phase headings: "PREFLIGHT > OUTPUT CONTRACTS" | All phase headings: "PREFLIGHT > OUTPUT CONTRACTS" | All phase headings: "PREFLIGHT > OUTPUT CONTRACTS" |
| **C-30** (write-token in GATE 4) | Prose directive + code block before check table | Write directive references declared slot by full path | Third row in GATE 4 table is the write action row | Imperative "**WRITE:**" header directive + code block | Third row in GATE 4 table (after OUTPUT CONTRACTS) references "PREFLIGHT > OUTPUT CONTRACTS above" |

---

## V-01 — Role sequence (GATE 4 opens PREFLIGHT)

**Axis:** Role sequence — GATE 4 is the first gate in the PREFLIGHT block. The inertia reference frame is established before citation, anchoring, or proof gates are applied. OUTPUT CONTRACTS is PREFLIGHT's closing subsection — all slots are declared after the gates that govern their content.

**Hypothesis:** Placing GATE 4 first foregrounds the gravitational baseline as the highest-priority constraint. The model must resolve what the user is already doing before it can reason about any competitor. The gate ordering signals a data dependency: INERTIA-REF is the context within which all subsequent collection (GATE 1: citations, GATE 2: anchors, GATE 3: proofs) is interpreted.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If `focus:` is set (e.g., `focus: market-sizing`, `focus: positioning-framework`), the focus dimension is active. If not supplied, no focus column is added and focus-related outputs pass by vacuous satisfaction.

---

## PREFLIGHT

All gates are defined here. No gate appears outside this block. GATE 4 clears first — the INERTIA-REF reference frame is established before citation, anchoring, and proof gates apply.

---

### GATE 4: INERTIA-REF GATE

**Clear this gate before all others.** Identify C0 — the status quo behavior, tool, or approach the target user relies on today — then write the INERTIA-REF token now, as the act of clearing this gate:

```
INERTIA-REF = [C0 name]: [specific mechanism — switching cost, habit lock-in, or workaround
satisfaction specific to C0's product behavior or feature; not a category label applied generically]
```

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Mechanism specific | Token names a concrete mechanism (switching cost, habit lock-in, or workaround satisfaction) tied to C0's product behavior or feature — not a category label such as "high familiarity" or "users are accustomed" | **Inertia naming failure** — category label is not a mechanism; rewrite INERTIA-REF before any phase begins |
| Per-finding citation | Each finding in Phase 5 cites INERTIA-REF by token name: `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` | **Inertia citation failure** — add the comparison clause before outputting the finding row |

---

### GATE 1: CITATION GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Citation cell populated | URL from WebSearch present in Citation column of this row | **Citation gate failure** — suppress row; run WebSearch before outputting |
| Citation in row, not footnote | URL is inline in the table row, not in a trailing reference block | **Citation gate failure** — relocate citation into the row before outputting |

---

### GATE 2: ANCHOR GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Anchor cell format | `Row C{N}, {attribute}: "{value}"` — row reference, attribute name, and quoted value all present | **Anchor gate failure** — name-only entries do not conform; rewrite the cell before outputting |
| Whitespace absence anchor | Per-row absence evidence: `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` per candidate attribute per row | **Whitespace gate failure** — bare assertion without attribute-level evidence does not satisfy; per-row evidence required before outputting the WHITESPACE block |

NOT ACCEPTABLE: `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE: `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "embeds all review workflow inside GitHub PR diff view — no standalone async review mode exists"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE declared first | Named cell value (row label, attribute name, quoted value) appears before REDUCTION-1 and REDUCTION-2 | **Proof structure failure** — SOURCE must precede all reduction arguments; constructing an argument before naming the evidence is not allowed |
| Both reductions present | REDUCTION-1 and REDUCTION-2 each answer YES/NO with one sentence showing what is lost when that dimension is removed | **Proof structure failure** — both reductions required; one reduction alone does not establish cross-dimensionality |
| Both reductions answer NO | Neither single-dimension reduction produces the gap | **Proof structure failure** — if either answers YES, find a different gap before outputting THEREFORE |

---

### OUTPUT CONTRACTS

All output slots required by this skill, declared after the gates that govern their content. Each slot specifies its label, required structural format, and the gate or phase responsible for filling it. Producing phases back-reference their assigned slot by this exact label at the point of production.

| Slot | Label | Required format | Filled by phase |
|------|-------|-----------------|-----------------|
| Inertia anchor | INERTIA-REF | `[C0 name]: [specific mechanism]` | GATE 4 (this PREFLIGHT block) |
| Competitor row anchor | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 — Competitor Table |
| Whitespace gap evidence | Absence evidence block | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` — one entry per row per candidate attribute | Phase 3 — Whitespace |
| Cross-dimensional source | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` | Phase 4 — Cross-Dimensional Finding |
| Per-finding inertia delta | INERTIA-REF-DELTA | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` | Phase 5 — Findings Table |

A slot arrived at in the wrong format constitutes a **collection gate failure** — return to the phase named in the rightmost column.

---

### PHASE 1: CONTEXT

Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills Anchor column value — PREFLIGHT > OUTPUT CONTRACTS)

C0 is the entity identified in GATE 4. C0 enters as Row C0 with all columns populated. For each external competitor, run WebSearch before adding its row. Apply GATE 1 and GATE 2 per row before outputting.

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural — fills Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed and must be rewritten; apply GATE 2 before outputting.

During collection, note which competitor mechanism phrases and focus-column values depart from or resemble the INERTIA-REF mechanism — this data fills the INERTIA-REF-DELTA slot at Phase 5.

---

### PHASE 3: WHITESPACE (fills Absence evidence block — PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 2 (whitespace absence anchor). For each candidate whitespace attribute, record per row:

```
Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}
```

Then confirm:

```
Gap confirmed: No row provides a non-absent value for [{attribute(s)}] — attribute-level uncontested.
vs. INERTIA-REF: {how the vacant attribute relates to the C0 mechanism established in GATE 4}
```

NOT ACCEPTABLE: "No competitor covers this space." — bare assertion — **whitespace gate failure**
NOT ACCEPTABLE: "Competitor 2 reveals a gap in..." — name-only — **anchor gate failure**

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills SOURCE slot — PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 3.

```
SOURCE: {named cell — row label, attribute name, quoted value — fill this slot before writing any
reduction argument; do not proceed to REDUCTION-1 until SOURCE is declared per
PREFLIGHT > OUTPUT CONTRACTS format}

REDUCTION-1: Competitive map alone — does the gap appear without the focus dimension?
[YES/NO + one sentence showing what is lost when focus is dropped]

REDUCTION-2: Focus dimension alone — does the gap appear without the competitive map?
[YES/NO + one sentence showing what is lost when the map is dropped]

If either answers YES, find a different gap — proceeding is a **proof structure failure**.

THEREFORE: {one sentence — the gap that requires both dimensions simultaneously}
```

---

### PHASE 5: FINDINGS TABLE (fills Anchor column value and INERTIA-REF-DELTA — PREFLIGHT > OUTPUT CONTRACTS)

Write 2–5 findings. All findings are rows in the following table. Apply GATE 2 (Anchor) and GATE 4 (INERTIA-REF-DELTA) per row before outputting.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column** (structural — fills Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed; apply GATE 2.

NOT ACCEPTABLE (Anchor): `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE (Anchor): `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE (Anchor): `Row C3, focus-column: "no SMB pricing tier — enterprise contract required for access"`

**INERTIA-REF-DELTA column** (structural — fills INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` — apply GATE 4; a cell with only "N/A" or a competitor name is malformed; every finding row must cite INERTIA-REF by token name.

For the cross-dimensional finding row: the Claim cell contains the THEREFORE sentence. An adjacent indented block contains SOURCE, REDUCTION-1, REDUCTION-2 — apply GATE 3.

---

### AMEND

Exactly 3 adjustments:

1. **Shift focus dimension**: Replace `{focus_dimension}`. Replace the SOURCE slot (PREFLIGHT > OUTPUT CONTRACTS — SOURCE slot) with the new evidentiary anchor. Rewrite REDUCTION-1 and REDUCTION-2 from scratch against the updated focus. Reconstruct THEREFORE. Apply GATE 3. Writing only a new conclusion without rerunning both reductions is a **proof rerun failure** — both single-dimension reduction arguments must be rebuilt.

2. **Add competitor**: Insert a new row after running WebSearch. Apply GATE 1 (CITATION) and GATE 2 (Anchor format — PREFLIGHT > OUTPUT CONTRACTS, Anchor column value). Update Phase 3 WHITESPACE absence evidence for all candidate attributes — apply GATE 2 (whitespace absence anchor); a new row may change vacancy status.

3. **Refine INERTIA-REF mechanism** (PREFLIGHT > GATE 4 / OUTPUT CONTRACTS — INERTIA-REF slot): Replace the INERTIA-REF mechanism sentence with more specific phrasing — name a product feature, workflow step, or workaround behavior. Apply GATE 4 to all Phase 5 findings — update INERTIA-REF-DELTA cells referencing the old mechanism phrase; updated cells must conform to column format.

---

## V-02 — Output format (spec-first PREFLIGHT: OUTPUT CONTRACTS before gates)

**Axis:** Output format — OUTPUT CONTRACTS is the first subsection within PREFLIGHT, before any gate. The model reads what it will produce before it reads what will be checked. GATE 4's write directive explicitly references the already-declared INERTIA-REF slot by full path, binding the write action to the contract rather than defining the token independently.

**Hypothesis:** Declaring outputs before rules inverts the typical "check then produce" mental model. The output contract is the first thing the model reads inside PREFLIGHT. GATE 4's write instruction names the slot it fills: "Fill the INERTIA-REF slot (PREFLIGHT > OUTPUT CONTRACTS above): Write INERTIA-REF = [...]." This makes the write action an explicit contract fulfillment, not a gate side-effect.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If `focus:` is set (e.g., `focus: market-sizing`, `focus: positioning-framework`), the focus dimension is active. If not supplied, no focus column is added and focus-related outputs pass by vacuous satisfaction.

---

## PREFLIGHT

All gates and output specifications are defined here. OUTPUT CONTRACTS is declared first — the model reads the production target before it reads the gate logic.

---

### OUTPUT CONTRACTS

All output slots required by this skill. Reading this subsection first provides the production target before any gate constraint is encountered. GATE 4 (below) fills the INERTIA-REF slot.

| Slot | Label | Required format | Filled by phase |
|------|-------|-----------------|-----------------|
| Inertia anchor | INERTIA-REF | `[C0 name]: [specific mechanism]` | GATE 4 (PREFLIGHT, below) |
| Competitor row anchor | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 — Competitor Table |
| Whitespace gap evidence | Absence evidence block | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` — one entry per row per candidate attribute | Phase 3 — Whitespace |
| Cross-dimensional source | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` | Phase 4 — Cross-Dimensional Finding |
| Per-finding inertia delta | INERTIA-REF-DELTA | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` | Phase 5 — Findings Table |

A slot arrived at in the wrong format constitutes a **collection gate failure** — return to the gate or phase named in the rightmost column.

---

### GATE 1: CITATION GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Citation cell populated | URL from WebSearch present in Citation column of this row | **Citation gate failure** — suppress row; run WebSearch before outputting |
| Citation in row, not footnote | URL is inline in the table row, not in a trailing reference block | **Citation gate failure** — relocate citation into the row before outputting |

---

### GATE 2: ANCHOR GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Anchor cell format | `Row C{N}, {attribute}: "{value}"` — row reference, attribute name, and quoted value all present | **Anchor gate failure** — name-only entries do not conform; rewrite the cell before outputting |
| Whitespace absence anchor | Per-row absence evidence: `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` per candidate attribute per row | **Whitespace gate failure** — bare assertion without attribute-level evidence does not satisfy; per-row evidence required before outputting the WHITESPACE block |

NOT ACCEPTABLE: `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE: `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "stores all task decisions in email threads — no structured decision log available to the team"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE declared first | Named cell value (row label, attribute name, quoted value) appears before REDUCTION-1 and REDUCTION-2 | **Proof structure failure** — SOURCE must precede all reduction arguments; constructing an argument before naming the evidence is not allowed |
| Both reductions present | REDUCTION-1 and REDUCTION-2 each answer YES/NO with one sentence showing what is lost when that dimension is removed | **Proof structure failure** — both reductions required; one reduction alone does not establish cross-dimensionality |
| Both reductions answer NO | Neither single-dimension reduction produces the gap | **Proof structure failure** — if either answers YES, find a different gap before outputting THEREFORE |

---

### GATE 4: INERTIA-REF GATE

**Fill the INERTIA-REF slot (PREFLIGHT > OUTPUT CONTRACTS above).** Identify C0 — the status quo behavior, tool, or approach the target user relies on today — then write the token now, as the act of clearing this gate:

```
INERTIA-REF = [C0 name]: [specific mechanism — switching cost, habit lock-in, or workaround
satisfaction specific to C0's product behavior or feature; not a category label applied generically]
```

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Mechanism specific | Token names a concrete mechanism (switching cost, habit lock-in, or workaround satisfaction) tied to C0's product behavior or feature — not a category label | **Inertia naming failure** — category label is not a mechanism; rewrite INERTIA-REF before any phase begins |
| Per-finding citation | Each finding in Phase 5 cites INERTIA-REF by token name: `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` | **Inertia citation failure** — add the comparison clause before outputting the finding row |

---

### PHASE 1: CONTEXT

Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills Anchor column value — PREFLIGHT > OUTPUT CONTRACTS)

C0 is the entity identified when clearing GATE 4. C0 enters as Row C0 with all columns populated. For each external competitor, run WebSearch before adding its row. Apply GATE 1 and GATE 2 per row before outputting.

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural — fills Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed and must be rewritten; apply GATE 2 before outputting.

Note which mechanism phrases and focus-column values relate to the INERTIA-REF mechanism — this data fills INERTIA-REF-DELTA at Phase 5.

---

### PHASE 3: WHITESPACE (fills Absence evidence block — PREFLIGHT > OUTPUT CONTRACTS)

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

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills SOURCE slot — PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 3.

```
SOURCE: {named cell — row label, attribute name, quoted value — fill this slot before writing any
reduction argument; do not proceed to REDUCTION-1 until SOURCE is declared per
PREFLIGHT > OUTPUT CONTRACTS format}

REDUCTION-1: Competitive map alone — does the gap appear without the focus dimension?
[YES/NO + one sentence showing what is lost when focus is dropped]

REDUCTION-2: Focus dimension alone — does the gap appear without the competitive map?
[YES/NO + one sentence showing what is lost when the map is dropped]

If either answers YES, find a different gap — proceeding is a **proof structure failure**.

THEREFORE: {one sentence — the gap that requires both dimensions simultaneously}
```

---

### PHASE 5: FINDINGS TABLE (fills Anchor column value and INERTIA-REF-DELTA — PREFLIGHT > OUTPUT CONTRACTS)

Write 2–5 findings. All findings are rows in the following table. Apply GATE 2 (Anchor) and GATE 4 (INERTIA-REF-DELTA) per row before outputting.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column** (structural — fills Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed; apply GATE 2.

NOT ACCEPTABLE (Anchor): `Competitor 3 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE (Anchor): `As Competitor 2 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE (Anchor): `Row C3, threat: "high — async-native API surface enables the integration pattern we lack"`

**INERTIA-REF-DELTA column** (structural — fills INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` — apply GATE 4; a cell with only "N/A" or a competitor name is malformed; every finding row must cite INERTIA-REF by token name.

For the cross-dimensional finding row: the Claim cell contains the THEREFORE sentence. An adjacent indented block contains SOURCE, REDUCTION-1, REDUCTION-2 — apply GATE 3.

---

### AMEND

Exactly 3 adjustments:

1. **Shift focus dimension**: Replace `{focus_dimension}`. Replace the SOURCE slot (PREFLIGHT > OUTPUT CONTRACTS — SOURCE slot) with the new evidentiary anchor. Rewrite REDUCTION-1 and REDUCTION-2 from scratch against the updated focus. Reconstruct THEREFORE. Apply GATE 3. Writing only a new conclusion without rerunning both reductions is a **proof rerun failure** — both single-dimension reduction arguments must be rebuilt.

2. **Add competitor**: Insert a new row after running WebSearch. Apply GATE 1 (CITATION) and GATE 2 (Anchor format — PREFLIGHT > OUTPUT CONTRACTS, Anchor column value). Update Phase 3 WHITESPACE absence evidence for all candidate attributes — apply GATE 2 (whitespace absence anchor); a new row may change vacancy status.

3. **Refine INERTIA-REF mechanism** (PREFLIGHT > GATE 4 / OUTPUT CONTRACTS — INERTIA-REF slot): Replace the INERTIA-REF mechanism sentence with more specific phrasing — name a product feature, workflow step, or workaround behavior. Apply GATE 4 to all Phase 5 findings — update INERTIA-REF-DELTA cells referencing the old mechanism phrase; updated cells must conform to column format.

---

## V-03 — Lifecycle emphasis (write-token as structural GATE 4 table row)

**Axis:** Lifecycle emphasis — the write-token instruction in GATE 4 is not a prose block or code block preceding the check table; it is a distinct row within the GATE 4 PASS/FAIL table. The write action has a Check label ("Write INERTIA-REF token"), a Pass condition (the required token format), and a Failure state ("Inertia write failure"). This makes production of INERTIA-REF structurally identical to a gate check: a row in a table, with a pass condition, and a named failure mode.

**Hypothesis:** When the write action is a gate row, it cannot be separated from the gate's check logic. The model processes it as a gate condition, not as introductory prose that might be treated as context rather than instruction. A write row is also independently checkable by a reviewer: the reviewer verifies the row the same way they verify any other gate row, without reading prose surrounding it.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If `focus:` is set (e.g., `focus: market-sizing`, `focus: positioning-framework`), the focus dimension is active. If not supplied, no focus column is added and focus-related outputs pass by vacuous satisfaction.

---

## PREFLIGHT

All gates and output specifications are defined here. No gate appears outside this block. GATE 4 includes a write action as a structural table row — token production is a gate step, not a preamble instruction.

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
| Whitespace absence anchor | Per-row absence evidence: `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` per candidate attribute per row | **Whitespace gate failure** — bare assertion without attribute-level evidence does not satisfy; per-row evidence required before outputting the WHITESPACE block |

NOT ACCEPTABLE: `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE: `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "enforces daily standup via calendar lock — no async standup pathway in the product"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE declared first | Named cell value (row label, attribute name, quoted value) appears before REDUCTION-1 and REDUCTION-2 | **Proof structure failure** — SOURCE must precede all reduction arguments |
| Both reductions present | REDUCTION-1 and REDUCTION-2 each answer YES/NO with one sentence showing what is lost when that dimension is removed | **Proof structure failure** — both reductions required; one alone does not establish cross-dimensionality |
| Both reductions answer NO | Neither single-dimension reduction produces the gap | **Proof structure failure** — if either answers YES, find a different gap before outputting THEREFORE |

---

### GATE 4: INERTIA-REF GATE

Identify C0 — the status quo behavior, tool, or approach the target user relies on today. Execute the following three steps at gate evaluation time:

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | C0's primary stickiness is a concrete mechanism: switching cost, habit lock-in, or workaround satisfaction specific to C0's product behavior or feature — not a category label | **Inertia naming failure** — category label is not a mechanism; resolve C0's specific stickiness before proceeding to the write step |
| Write INERTIA-REF token | Write at this step: `INERTIA-REF = [C0 name]: [specific mechanism phrase]` — this token is now available to all phases; do not defer token production | **Inertia write failure** — token must be written at this gate, not defined in a later phase; return to this gate and execute the write step |
| Per-finding citation required | Each finding in Phase 5 cites INERTIA-REF by token name: `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` | **Inertia citation failure** — add the comparison clause before outputting the finding row |

---

### OUTPUT CONTRACTS

All output slots required by this skill. Each slot specifies its label, required structural format, and the gate or phase responsible for filling it.

| Slot | Label | Required format | Filled by phase |
|------|-------|-----------------|-----------------|
| Inertia anchor | INERTIA-REF | `[C0 name]: [specific mechanism]` | GATE 4 (Write row) |
| Competitor row anchor | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 — Competitor Table |
| Whitespace gap evidence | Absence evidence block | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` — one entry per row per candidate attribute | Phase 3 — Whitespace |
| Cross-dimensional source | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` | Phase 4 — Cross-Dimensional Finding |
| Per-finding inertia delta | INERTIA-REF-DELTA | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` | Phase 5 — Findings Table |

A slot arrived at in the wrong format constitutes a **collection gate failure** — return to the gate or phase named in the rightmost column.

---

### PHASE 1: CONTEXT

Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills Anchor column value — PREFLIGHT > OUTPUT CONTRACTS)

C0 is the entity whose stickiness was resolved in GATE 4. C0 enters as Row C0 with all columns populated. For each external competitor, run WebSearch before adding its row. Apply GATE 1 and GATE 2 per row before outputting.

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural — fills Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed and must be rewritten; apply GATE 2 before outputting.

Note which mechanism phrases and focus-column values relate to the INERTIA-REF token written in GATE 4 — this data fills INERTIA-REF-DELTA at Phase 5.

---

### PHASE 3: WHITESPACE (fills Absence evidence block — PREFLIGHT > OUTPUT CONTRACTS)

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

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills SOURCE slot — PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 3.

```
SOURCE: {named cell — row label, attribute name, quoted value — fill this slot before writing any
reduction argument; do not proceed to REDUCTION-1 until SOURCE is declared per
PREFLIGHT > OUTPUT CONTRACTS format}

REDUCTION-1: Competitive map alone — does the gap appear without the focus dimension?
[YES/NO + one sentence showing what is lost when focus is dropped]

REDUCTION-2: Focus dimension alone — does the gap appear without the competitive map?
[YES/NO + one sentence showing what is lost when the map is dropped]

If either answers YES, find a different gap — proceeding is a **proof structure failure**.

THEREFORE: {one sentence — the gap that requires both dimensions simultaneously}
```

---

### PHASE 5: FINDINGS TABLE (fills Anchor column value and INERTIA-REF-DELTA — PREFLIGHT > OUTPUT CONTRACTS)

Write 2–5 findings. All findings are rows in the following table. Apply GATE 2 (Anchor) and GATE 4 (INERTIA-REF-DELTA) per row before outputting.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column** (structural — fills Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed; apply GATE 2.

NOT ACCEPTABLE (Anchor): `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE (Anchor): `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE (Anchor): `Row C2, mechanism: "enforces daily standup via calendar lock — no async standup pathway"`

**INERTIA-REF-DELTA column** (structural — fills INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` — apply GATE 4 (Write row — token must have been written before this phase runs); a cell with only "N/A" or a competitor name is malformed; every finding row must cite INERTIA-REF by token name.

For the cross-dimensional finding row: the Claim cell contains the THEREFORE sentence. An adjacent indented block contains SOURCE, REDUCTION-1, REDUCTION-2 — apply GATE 3.

---

### AMEND

Exactly 3 adjustments:

1. **Shift focus dimension**: Replace `{focus_dimension}`. Replace the SOURCE slot (PREFLIGHT > OUTPUT CONTRACTS — SOURCE slot) with the new evidentiary anchor. Rewrite REDUCTION-1 and REDUCTION-2 from scratch against the updated focus. Reconstruct THEREFORE. Apply GATE 3. Writing only a new conclusion without rerunning both reductions is a **proof rerun failure** — both single-dimension reduction arguments must be rebuilt.

2. **Add competitor**: Insert a new row after running WebSearch. Apply GATE 1 (CITATION) and GATE 2 (Anchor format — PREFLIGHT > OUTPUT CONTRACTS, Anchor column value). Update Phase 3 WHITESPACE absence evidence for all candidate attributes — apply GATE 2 (whitespace absence anchor); a new row may change vacancy status.

3. **Refine INERTIA-REF mechanism** (PREFLIGHT > GATE 4, Write row / OUTPUT CONTRACTS — INERTIA-REF slot): Re-execute the GATE 4 Write row with a more specific mechanism phrase — name a product feature, workflow step, or workaround behavior. Apply GATE 4 to all Phase 5 findings — update INERTIA-REF-DELTA cells referencing the old mechanism phrase; updated cells must conform to column format.

---

## V-04 — Phrasing register (imperative style; GATE 4 last, after OUTPUT CONTRACTS)

**Axis:** Phrasing register — the skill is written in imperative command style throughout ("Write", "Run", "Apply", "Insert", "Confirm") rather than declarative obligation ("must be present", "is required", "does not satisfy"). GATE 4 is the last gate in PREFLIGHT, placed after OUTPUT CONTRACTS so the write directive explicitly names the slot it fills by path ("fills INERTIA-REF slot — PREFLIGHT > OUTPUT CONTRACTS above"). The "Filled by phase" column is labeled "Producing phase" to test synonym tolerance.

**Hypothesis:** Imperative register reduces cognitive distance between instruction and action. "Write INERTIA-REF = [...]" is a directive; "INERTIA-REF must be defined" is a constraint. The variation also tests whether the GATE 4 write instruction is stronger when it can reference a previously-declared OUTPUT CONTRACTS entry — the slot was named before the gate ran, so the gate's write action resolves a known forward-declared dependency rather than creating a new one.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If `focus:` is set, the focus dimension is active. If not supplied, omit the focus column and pass focus-related criteria vacuously.

---

## PREFLIGHT

All rules and output specifications are defined here. Run this block before any phase. No gate appears outside this block.

---

### GATE 1: CITATION GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Citation populated | WebSearch URL present in Citation column of this row | **Citation gate failure** — suppress row; run WebSearch first |
| Citation inline | URL is in the row, not a trailing footnote block | **Citation gate failure** — move citation into the row |

---

### GATE 2: ANCHOR GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Anchor format | `Row C{N}, {attribute}: "{value}"` — row reference, attribute name, and quoted value present | **Anchor gate failure** — name-only cell is malformed; rewrite before outputting |
| Whitespace absence anchor | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` per row per candidate attribute | **Whitespace gate failure** — record attribute-level absence per row; bare assertion is insufficient |

NOT ACCEPTABLE: `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE: `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE: `Row C2, mechanism: "locks all review state inside GitHub PR diff — no export or standalone session mode"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE first | Named cell value (row, attribute, quoted value) precedes REDUCTION-1 and REDUCTION-2 | **Proof structure failure** — write SOURCE before any reduction argument |
| Both reductions present | REDUCTION-1 and REDUCTION-2 each give YES/NO + one sentence showing what is lost | **Proof structure failure** — both reductions required; one is insufficient |
| Both answer NO | Neither dimension alone produces the gap | **Proof structure failure** — if either is YES, find a different gap |

---

### OUTPUT CONTRACTS

Declare all output slots here. GATE 4 (below) fills the INERTIA-REF slot. Each producing phase back-references its slot label from within the phase heading.

| Slot | Label | Required format | Producing phase |
|------|-------|-----------------|-----------------|
| Inertia anchor | INERTIA-REF | `[C0 name]: [specific mechanism]` | GATE 4 (PREFLIGHT, below) |
| Competitor row anchor | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 — Competitor Table |
| Whitespace gap evidence | Absence evidence block | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` — one entry per row per candidate attribute | Phase 3 — Whitespace |
| Cross-dimensional source | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` | Phase 4 — Cross-Dimensional Finding |
| Per-finding inertia delta | INERTIA-REF-DELTA | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` | Phase 5 — Findings Table |

Wrong format at any slot = **collection gate failure** — return to the producing phase.

---

### GATE 4: INERTIA-REF GATE

Identify C0 — the status quo tool, workflow, or behavior the target user relies on today. **WRITE** the INERTIA-REF slot (PREFLIGHT > OUTPUT CONTRACTS above) now:

```
INERTIA-REF = [C0 name]: [specific mechanism — switching cost, habit lock-in, or workaround
satisfaction tied to C0's product behavior or feature; not a category label]
```

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Mechanism specific | Token names a concrete mechanism (switching cost, habit lock-in, or workaround satisfaction) specific to C0's product feature or workflow behavior — not a generic category description | **Inertia naming failure** — rewrite INERTIA-REF with a specific mechanism before any phase begins |
| Per-finding citation | Each finding in Phase 5 cites INERTIA-REF by token name: `vs. INERTIA-REF — {verdict}: {C0 mechanism phrase}` | **Inertia citation failure** — add the citation clause before outputting the finding row |

---

### PHASE 1: CONTEXT

Read repo context. Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills Anchor column value — PREFLIGHT > OUTPUT CONTRACTS)

Insert C0 as Row C0 (INERTIA-REF entity from GATE 4). Run WebSearch per external competitor. Apply GATE 1 and GATE 2 per row before outputting.

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural — fills Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — name-only cell is syntactically malformed; apply GATE 2 before outputting.

Note mechanism phrases and focus-column values per row — fills INERTIA-REF-DELTA at Phase 5.

---

### PHASE 3: WHITESPACE (fills Absence evidence block — PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 2 (whitespace absence anchor). Per candidate attribute per row:

```
Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}
```

Confirm:

```
Gap confirmed: No row provides a non-absent value for [{attribute(s)}] — attribute-level uncontested.
vs. INERTIA-REF: {relation to C0 mechanism from GATE 4}
```

NOT ACCEPTABLE: "No competitor covers this space." — bare assertion — **whitespace gate failure**

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills SOURCE slot — PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 3.

```
SOURCE: {named cell — row, attribute, quoted value — write this before any reduction argument;
apply PREFLIGHT > OUTPUT CONTRACTS, SOURCE slot format}

REDUCTION-1: Map alone — gap absent without focus? [YES/NO + one sentence — what is lost]

REDUCTION-2: Focus alone — gap absent without map? [YES/NO + one sentence — what is lost]

If either YES: find a different gap — proceeding is a **proof structure failure**.

THEREFORE: {one sentence — gap requiring both dimensions simultaneously}
```

---

### PHASE 5: FINDINGS TABLE (fills Anchor column value and INERTIA-REF-DELTA — PREFLIGHT > OUTPUT CONTRACTS)

Write 2–5 findings as table rows. Apply GATE 2 (Anchor) and GATE 4 (INERTIA-REF-DELTA) per row before outputting.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column** (structural — fills Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — name-only cell is malformed; apply GATE 2.

NOT ACCEPTABLE (Anchor): `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE (Anchor): `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE (Anchor): `Row C2, focus-column: "no SMB tier — minimum $5k/mo contract for any access"`

**INERTIA-REF-DELTA column** (structural — fills INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {C0 mechanism phrase}` — apply GATE 4; "N/A" or bare name is malformed; every row cites INERTIA-REF by token name.

Cross-dimensional finding row: Claim = THEREFORE; adjacent indented block contains SOURCE, REDUCTION-1, REDUCTION-2 — apply GATE 3.

---

### AMEND

Exactly 3 adjustments:

1. **Shift focus dimension**: Replace `{focus_dimension}`. Replace SOURCE slot (PREFLIGHT > OUTPUT CONTRACTS — SOURCE slot) with the new anchor. Rewrite REDUCTION-1 and REDUCTION-2 from scratch. Reconstruct THEREFORE. Apply GATE 3. Writing only a new THEREFORE without rerunning both reductions is a **proof rerun failure**.

2. **Add competitor**: Insert row after WebSearch. Apply GATE 1 and GATE 2 (Anchor format — PREFLIGHT > OUTPUT CONTRACTS, Anchor column value). Recheck Phase 3 absence evidence for all candidate attributes — apply GATE 2 (whitespace absence anchor).

3. **Refine INERTIA-REF mechanism** (PREFLIGHT > GATE 4 / OUTPUT CONTRACTS — INERTIA-REF slot): Re-execute GATE 4 write with a more specific mechanism phrase. Apply GATE 4 to all Phase 5 findings — rewrite INERTIA-REF-DELTA cells referencing the old phrase; updated cells must conform to column format.

---

## V-05 — Combined maximum (spec-first + write-as-table-row + 6-slot contract + 3 coercion templates)

**Axes combined:** Output format (spec-first PREFLIGHT from V-02) + Lifecycle emphasis (write-token as gate table row from V-03) + expanded 6-slot OUTPUT CONTRACTS + three independent structural coercion templates.

**Hypothesis:** The combination of spec-first (production target visible before gate logic), write-as-table-row (token production is a named, checksumable gate step), and a 6-slot contract (adds a focus-integration scope evidence slot) creates the most structurally complete variant. The 6th slot — focus-scope evidence — makes the cross-dimensional requirement forward-declared: the collection phase knows before it runs that it must produce scope evidence demonstrating why the cross-dimensional finding requires both dimensions. Combined with three independent coercion templates (competitor Anchor, findings Anchor, INERTIA-REF-DELTA), this variation maximizes adversarial robustness across all structural levels.

---

You are running **discover-competitors-alt**.

**FOCUS CHECK:** If `focus:` is set (e.g., `focus: market-sizing`, `focus: positioning-framework`), the focus dimension is active. If not supplied, no focus column is added and focus-related outputs pass by vacuous satisfaction.

---

## PREFLIGHT

All output specifications and gates are defined here. No gate appears outside this block. OUTPUT CONTRACTS is declared first — the model reads the production target before it reads the gate logic.

---

### OUTPUT CONTRACTS

All output slots required by this skill. GATE 4 (below) fills the INERTIA-REF slot. Each producing phase back-references its slot by this exact label at the point of production.

| Slot | Label | Required format | Filled by phase |
|------|-------|-----------------|-----------------|
| Inertia anchor | INERTIA-REF | `[C0 name]: [specific mechanism]` | GATE 4 (Write row, below) |
| Competitor row anchor | Anchor column value | `Row C{N}, {attribute}: "{value}"` | Phase 2 — Competitor Table |
| Whitespace gap evidence | Absence evidence block | `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` — one entry per row per candidate attribute | Phase 3 — Whitespace |
| Focus-integration scope | Focus-scope evidence | `{attribute}: neither [{competitive_attribute}] alone nor [{focus_dim}] alone produces this gap — requires both` — one entry per cross-dimensional gap candidate | Phase 4 — Cross-Dimensional Finding |
| Cross-dimensional source | SOURCE slot | `{row label}, {attribute}: "{quoted value}"` | Phase 4 — Cross-Dimensional Finding |
| Per-finding inertia delta | INERTIA-REF-DELTA | `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` | Phase 5 — Findings Table |

A slot arrived at in the wrong format constitutes a **collection gate failure** — return to the gate or phase named in the rightmost column.

---

### GATE 4: INERTIA-REF GATE

Identify C0 — the status quo behavior, tool, or approach the target user relies on today. Execute the following three steps at gate evaluation time:

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| C0 stickiness mechanism identified | C0's primary stickiness is a concrete mechanism: switching cost, habit lock-in, or workaround satisfaction specific to C0's product behavior or feature — not a category label such as "high familiarity" or "strongly habituated" | **Inertia naming failure** — category label is not a mechanism; resolve C0's specific stickiness before proceeding to the write step |
| Write INERTIA-REF token | Write at this step: `INERTIA-REF = [C0 name]: [specific mechanism phrase]` — this fills the INERTIA-REF slot (PREFLIGHT > OUTPUT CONTRACTS above); token is now available to all phases | **Inertia write failure** — token must be written at this gate, not defined in a later phase; return to this gate and execute the write step |
| Per-finding citation required | Each finding in Phase 5 cites INERTIA-REF by token name: `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` | **Inertia citation failure** — add the comparison clause before outputting the finding row |

---

### GATE 1: CITATION GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Citation cell populated | URL from WebSearch present in Citation column of this row | **Citation gate failure** — suppress row; run WebSearch before outputting |
| Citation in row, not footnote | URL is inline in the table row, not in a trailing reference block | **Citation gate failure** — relocate citation into the row before outputting |
| URL is direct | Citation is a direct URL to the source page, not a search results page | **Citation gate failure** — replace with a direct source URL |

---

### GATE 2: ANCHOR GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| Anchor cell format | `Row C{N}, {attribute}: "{value}"` — row reference, attribute name, and quoted value all present | **Anchor gate failure** — name-only entries do not conform; rewrite the cell before outputting |
| Whitespace absence anchor | Per-row absence evidence: `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}` per candidate attribute per row | **Whitespace gate failure** — bare assertion without attribute-level evidence does not satisfy; per-row evidence required before outputting the WHITESPACE block |
| Anchor cites attribute + value | Anchor cell includes both an attribute name and a quoted value from that row — competitor name alone or name + label is malformed | **Anchor gate failure** — a cell without an attribute name and quoted value does not conform; rewrite before outputting |

NOT ACCEPTABLE: `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE: `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
NOT ACCEPTABLE: `Competitor 3 — high threat to positioning` — name + label, no attribute value — **anchor gate failure**
ACCEPTABLE: `Row C3, focus-column: "no async review mode — all review actions require real-time session presence"`

---

### GATE 3: PROOF GATE

| Check | Pass condition | Failure state |
|-------|---------------|---------------|
| SOURCE declared first | Named cell value (row label, attribute name, quoted value) appears before REDUCTION-1 and REDUCTION-2 | **Proof structure failure** — SOURCE must precede all reduction arguments; constructing an argument before naming the evidence is not allowed |
| Both reductions present | REDUCTION-1 and REDUCTION-2 each answer YES/NO with one sentence showing what is lost when that dimension is removed | **Proof structure failure** — both reductions required; one reduction alone does not establish cross-dimensionality |
| Both reductions answer NO | Neither single-dimension reduction produces the gap | **Proof structure failure** — if either answers YES, find a different gap before outputting THEREFORE |

---

### PHASE 1: CONTEXT

Read repo context (README, CLAUDE.md, package.json, or equivalent). Infer:

```
Token: TOPIC: {inferred topic}
Token: FOCUS: {market-sizing | positioning-framework | none}
```

---

### PHASE 2: COMPETITOR TABLE (fills Anchor column value — PREFLIGHT > OUTPUT CONTRACTS)

C0 is the entity whose stickiness was resolved and written in GATE 4. C0 enters as Row C0 with all columns populated. For each external competitor, run WebSearch before adding its row. Apply GATE 1 and GATE 2 per row before outputting.

| Row | Competitor | Threat | Mechanism | Focus: {focus_dimension} | Anchor | Citation |
|-----|-----------|--------|-----------|--------------------------|--------|----------|

**Anchor column** (structural — fills Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed and must be rewritten; apply GATE 2 before outputting.

NOT ACCEPTABLE (Anchor): `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE (Anchor): `Competitor 3 — low threat` — name + label, no attribute value — **anchor gate failure**
ACCEPTABLE (Anchor): `Row C2, mechanism: "requires active GitHub session for all diff comments — no offline review path"`

Note which mechanism phrases and focus-column values relate to the INERTIA-REF token — this data fills the INERTIA-REF-DELTA slot at Phase 5.

---

### PHASE 3: WHITESPACE (fills Absence evidence block — PREFLIGHT > OUTPUT CONTRACTS)

Apply GATE 2 (whitespace absence anchor). For each candidate whitespace attribute, record per row:

```
Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}
```

Then confirm:

```
Gap confirmed: No row provides a non-absent value for [{attribute(s)}] — attribute-level uncontested.
vs. INERTIA-REF: {how the vacant attribute relates to the C0 mechanism written in GATE 4}
```

NOT ACCEPTABLE: "No competitor covers this space." — bare assertion — **whitespace gate failure**
NOT ACCEPTABLE: "Competitor 2 reveals a gap in..." — name-only — **anchor gate failure**

---

### PHASE 4: CROSS-DIMENSIONAL FINDING (fills Focus-scope evidence and SOURCE slot — PREFLIGHT > OUTPUT CONTRACTS)

Before running GATE 3, record focus-scope evidence for each candidate gap (fills Focus-scope evidence slot, PREFLIGHT > OUTPUT CONTRACTS):

```
{attribute}: neither [{competitive_attribute}] alone nor [{focus_dim}] alone produces this gap — requires both
```

Then apply GATE 3 for the primary cross-dimensional finding:

```
SOURCE: {named cell — row label, attribute name, quoted value — fill this slot before writing any
reduction argument; do not proceed to REDUCTION-1 until SOURCE is declared per
PREFLIGHT > OUTPUT CONTRACTS format}

REDUCTION-1: Competitive map alone — does the gap appear without the focus dimension?
[YES/NO + one sentence showing what is lost when focus is dropped]

REDUCTION-2: Focus dimension alone — does the gap appear without the competitive map?
[YES/NO + one sentence showing what is lost when the map is dropped]

If either answers YES, find a different gap — proceeding is a **proof structure failure**.

THEREFORE: {one sentence — the gap that requires both dimensions simultaneously}
```

---

### PHASE 5: FINDINGS TABLE (fills Anchor column value and INERTIA-REF-DELTA — PREFLIGHT > OUTPUT CONTRACTS)

Write 2–5 findings. All findings are rows in the following table. Apply GATE 2 (Anchor) and GATE 4 (INERTIA-REF-DELTA) per row before outputting.

| # | Claim | Anchor | INERTIA-REF-DELTA | Cross-dim? |
|---|-------|--------|-------------------|------------|

**Anchor column** (structural — fills Anchor column value, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed; apply GATE 2.

NOT ACCEPTABLE (Anchor): `Competitor 2 reveals that...` — name-only — **anchor gate failure**
NOT ACCEPTABLE (Anchor): `As Competitor 1 demonstrates...` — name-only — **anchor gate failure**
ACCEPTABLE (Anchor): `Row C3, focus-column: "no public pricing below $10k ARR — SMB segment unaddressed"`

**INERTIA-REF-DELTA column** (structural — fills INERTIA-REF-DELTA, PREFLIGHT > OUTPUT CONTRACTS): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` — apply GATE 4 (token written at Write row in GATE 4; must be available before this phase runs); a cell with only "N/A" or a competitor name is malformed; every finding row must cite INERTIA-REF by token name.

NOT ACCEPTABLE (INERTIA-REF-DELTA): `vs. INERTIA-REF — N/A` — empty comparison — **inertia citation failure**
NOT ACCEPTABLE (INERTIA-REF-DELTA): `vs. INERTIA-REF — relevant` — no mechanism phrase — **inertia citation failure**
ACCEPTABLE (INERTIA-REF-DELTA): `vs. INERTIA-REF — challenges: habit lock-in via daily standup enforcement — gap shifts cost of switching outward`

For the cross-dimensional finding row: the Claim cell contains the THEREFORE sentence. An adjacent indented block contains SOURCE, REDUCTION-1, REDUCTION-2 — apply GATE 3.

---

### AMEND

Exactly 3 adjustments:

1. **Shift focus dimension**: Replace `{focus_dimension}`. Replace the SOURCE slot (PREFLIGHT > OUTPUT CONTRACTS — SOURCE slot) with the new evidentiary anchor. Replace Focus-scope evidence entries (PREFLIGHT > OUTPUT CONTRACTS — Focus-scope evidence slot) with updated cross-dimensional scope entries for the new focus dimension. Rewrite REDUCTION-1 and REDUCTION-2 from scratch against the updated focus. Reconstruct THEREFORE. Apply GATE 3. Writing only a new conclusion without rerunning both reductions is a **proof rerun failure** — both single-dimension reduction arguments must be rebuilt.

2. **Add competitor**: Insert a new row after running WebSearch. Apply GATE 1 (CITATION), GATE 2 (Anchor format — PREFLIGHT > OUTPUT CONTRACTS, Anchor column value). Update Phase 3 WHITESPACE absence evidence for all candidate attributes — apply GATE 2 (whitespace absence anchor). Update Focus-scope evidence entries if the new row changes the cross-dimensional candidate pool.

3. **Refine INERTIA-REF mechanism** (PREFLIGHT > GATE 4, Write row / OUTPUT CONTRACTS — INERTIA-REF slot): Re-execute GATE 4 Write row with a more specific mechanism phrase — name a product feature, workflow step, or workaround behavior. Apply GATE 4 to all Phase 5 findings — update INERTIA-REF-DELTA cells referencing the old mechanism phrase; updated cells must conform to column format.
