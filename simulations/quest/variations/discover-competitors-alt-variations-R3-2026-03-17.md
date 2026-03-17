Written to `simulations/quest/variations/discover-competitors-alt-variations-R3-2026-03-17.md`.

---

## discover-competitors-alt — R3 Variations

**Baseline going in:** R1/R2 V-05 architecture scores ~187.5 under v9 (PARTIAL on all three new criteria). R3 targets 195 by explicitly earning C-27, C-28, C-29.

---

### Variation Map

| Var | Axis | Key change | C-27 | C-28 | C-29 | Expected |
|-----|------|-----------|------|------|------|---------|
| V-01 | Lifecycle emphasis | Construct-role phase headers + position-agnostic statement in opening | PASS | PARTIAL | PARTIAL | **190** |
| V-02 | Phrasing register | Explicit "label format is a free variable" declaration in opening + loop | PARTIAL | PASS | PARTIAL | **190** |
| V-03 | Role sequence | Single-sentence opening — minimal sufficient form demonstrated | PARTIAL | PARTIAL | PASS | **190** |
| V-04 | C-27 + C-28 | Construct headers + label surface declaration + WRONG:/RIGHT: labels | PASS | PASS | PARTIAL | **192.5** |
| V-05 | C-27 + C-28 + C-29 | Single sentence packing all three — construct labels, label-surface-free, apparatus | PASS | PASS | PASS | **195** |

---

### Design Rationale

**Why these three axes for single-axis variations?**
- C-27, C-28, C-29 each require an *explicit declaration* — they're not satisfied by practice alone. The baseline demonstrates all three behaviors but never names them. One axis per variation isolates the scoring impact of adding each declaration.

**V-01 (Lifecycle emphasis):** Phase headers become `PHASE 1: INERTIA MECHANISM CONSTRUCT` and `PHASE 2: PRE-MAP CONSTRUCT` — role-first naming independent of ordinal. Opening assertion adds the position-agnostic sentence explicitly.

**V-02 (Phrasing register):** Second sentence of opening assertion becomes the label surface declaration: *"Bilateral pair label format is a free variable: WRONG:/RIGHT:, DO NOT/DO, FAILS/PASS, or any structural framing satisfies the bilateral pair requirement — only the bilateral structure is prescriptive."* Loop language reinforces: *"any label format — rejection example + acceptance example is the invariant."*

**V-03 (Role sequence):** Opening compressed to exactly one sentence: *"The pre-map construct (C-11), inertia mechanism construct (C-13), and whitespace table (C-12) all enforce via table schema — an absent table or empty row is an observable format failure."* No second sentence. Demonstrates C-29's minimal sufficient form.

**V-04 combination:** V-01 + V-02 signals stacked — two-sentence opening carries both declarations, WRONG:/RIGHT: labels demonstrate the freedom claimed in the C-28 declaration.

**V-05 full synthesis:** The opening sentence packs all three signals into one — position-agnostic clause, label-surface-free clause, apparatus type, all three constraint names. Phase-instruction lines add per-phase "The [construct] satisfies C-XX here; construct compliance is position-agnostic." reinforcement. Expected 195.

---

### Three Open Questions for Scoring

**Q1:** V-01 vs V-03 — does the position-agnostic statement in the opening assertion (without phase-header construct labels) earn C-27 PARTIAL or stay at FAIL? This tests whether opening-assertion language is sufficient or whether phase-level construct-role labels are required.

**Q2:** V-05's single sentence is structurally dense — does embedding position-agnostic + label-surface-free language alongside constraint names + apparatus still count as "structurally complete" for C-29, or does the extra content violate the minimal-sufficient-form reading?

**Q3:** V-04 vs V-05 — is the per-phase reinforcement line ("construct compliance is position-agnostic" repeated at each structural constraint phase) in V-05 additive for C-27, or does the opening assertion alone suffice once construct-role headers are present?
izing OR positioning framework), build the map through that lens.
The focus is a lens — not a section. Weave focus data through competitor rows, findings, and narrative. Do
not create a dedicated focus section.

Complete the pre-map table before any competitor entry:

| Map Label | Category description | Focus signal (if provided) |
|-----------|----------------------|----------------------------|
| [segment or position name] | [description] | [market size or positioning detail] |

DO NOT: Begin competitor analysis before this table is complete. Use any Map Label downstream that is not
present verbatim in this table. Create a dedicated focus section.
DO: Complete all rows. Copy row labels verbatim — unchanged — into the Map Position column in Phase 3.

---

### PHASE 3: COMPETITOR ANALYSIS

For each named competitor, add a row. Competitor 0 (inertia) goes first — Map Position sourced from Phase 2:

| Competitor | Threat | Map Position | Key differentiator | Focus lens placement |
|------------|--------|--------------|--------------------|-----------------------|

C-15 constraint: Map Position must be copied verbatim from a Phase 2 row label. An empty or paraphrased
Map Position cell is a format failure. Do not paraphrase. Do not generalize.

Run WebSearch for at least one named competitor characterization. Cite inline.

---

### PHASE 4: WHITESPACE TABLE

C-12 structural constraint. Apparatus: table schema. An absent table or single-row table fails.

| Gap | What no named competitor owns |
|-----|-------------------------------|
| Competitive gap | [uncontested space from Phase 2 map — reference a specific named row] |
| Focus gap | [unaddressed segment or category — requires Phase 2 data and focus dimension simultaneously] |

DO NOT: Build only one row. Leave either row without Phase 2 grounding. Omit the combined paragraph.
DO: Fill both rows with grounded findings. Write one combined paragraph linking both gaps.

---

### PHASE 5: FINDINGS

3–5 findings. Each must reference at least one named Phase 2 row or Phase 3 competitor by label. No
free-floating findings.

---

AMEND: Exactly 3 items. Each names (1) what the user changes, (2) what changes in the output. Specific.

---

PRE-SUBMISSION VERIFICATION
For each structural constraint, verify the output:
[ ] C-13 (inertia mechanism construct): Mechanism table present? Format-failure declared? Bilateral
    enforcement pair present (rejection example + acceptance example)?
[ ] C-11 (pre-map construct): Pre-map table present? Format-failure declared? Bilateral enforcement
    pair present (rejection example + acceptance example)?
[ ] C-12 (whitespace table): Both rows present? Format-failure declared? Bilateral enforcement pair
    present (rejection example + acceptance example)?

---

## V-02 — Bilateral Label Surface Declaration

**Axis:** Phrasing register — opening assertion explicitly declares that bilateral pair label format is a
free variable, naming the invariant (bilateral structure) and the surface (label format) as distinct
properties. Loop language reinforces the declaration.

**Hypothesis:** C-28 FULL PASS (5 pts). C-27 PARTIAL (2.5 pts — "pre-map construct" and "inertia mechanism
construct" appear in opening assertion but phase headers are standard; no explicit position-agnostic
statement). C-29 PARTIAL (2.5 pts — two-sentence opening, not demonstrably minimal). Expected: 190.

---

All three structural constraints — C-11 (pre-map construct), C-13 (inertia mechanism construct), C-12
(whitespace table) — enforce via table schema; an absent table or empty row is an observable format failure.
Bilateral pair label format is a free variable: DO NOT/DO, WRONG:/RIGHT:, FAILS/PASS, or any structural
framing (rejection example + acceptance example) satisfies the bilateral pair requirement — only the
bilateral structure is prescriptive.

SETUP: Detect the product domain from context (README, CLAUDE.md, package.json, or any Glob-discoverable
file). Do not ask. Infer domain, key features, and likely competitors automatically.

---

PRE-GENERATION INTEGRITY CHECK
Confirm all three structural constraints are present in this prompt before proceeding. For each, verify:
format artifact declared? format-failure declared? bilateral enforcement pair present?
[ ] C-13 inertia mechanism construct:
[ ] C-11 pre-map construct:
[ ] C-12 whitespace table:

---

### PHASE 1: INERTIA COMPETITOR

C-13 structural constraint. Apparatus: table schema. An absent mechanism table or empty mechanism row fails.

Assess the status quo first. Competitor 0: None / status quo. Threat level: HIGH. State explicitly.

PORTABILITY TEST: Each mechanism row must be so domain-specific it would be obviously wrong for a
different product category. Exact fail condition: if this content reads as true for a payroll tool or
a photo editor, it fails.

Populate the mechanism table (C-13 structural constraint — mechanism table required):

| Mechanism | Domain-specific behavior | Threat signal |
|-----------|--------------------------|---------------|
| WORKAROUND SATISFACTION | [the workaround teams use in this specific product context] | [threat signal] |
| SWITCHING COST | [the specific switching cost in this product context] | [threat signal] |
| HABIT LOCK-IN | [the specific habit pattern in this product context] | [threat signal] |

Table 1 above is the C-13 structural constraint (mechanism table). Apply portability test per row.

DO NOT: Omit the mechanism table. Leave any mechanism row empty. Write content that applies to a photo
editor or payroll tool.
DO: Fill all three rows with behavior so domain-specific it would be obviously wrong in a different product
category.

[Table 2 below is a portability summary — additional framing only; does not substitute for the mechanism
table for C-13 apparatus uniformity or C-19 purposes.]

| Mechanism | Portability verdict |
|-----------|---------------------|
| WORKAROUND SATISFACTION | [pass/fail + one-line reason] |
| SWITCHING COST | [pass/fail + one-line reason] |
| HABIT LOCK-IN | [pass/fail + one-line reason] |

---

### PHASE 2: COMPETITIVE LANDSCAPE MAP

C-11 structural constraint. Apparatus: table schema. An absent table or any row with an empty Map Label fails.

When a focus dimension is provided (market sizing OR positioning framework), build the map through that lens.
The focus is a lens — not a section. Weave focus data through competitor rows, findings, and narrative. Do
not create a dedicated focus section.

Complete the pre-map table before any competitor entry:

| Map Label | Category description | Focus signal (if provided) |
|-----------|----------------------|----------------------------|
| [segment or position name] | [description] | [market size or positioning detail] |

DO NOT: Begin competitor analysis before this table is complete. Use any Map Label downstream that is not
present verbatim in this table. Create a dedicated focus section.
DO: Complete all rows. Copy row labels verbatim — unchanged — into the Map Position column in Phase 3.

---

### PHASE 3: COMPETITOR ANALYSIS

For each named competitor, add a row. Competitor 0 (inertia) goes first — Map Position sourced from Phase 2:

| Competitor | Threat | Map Position | Key differentiator | Focus lens placement |
|------------|--------|--------------|--------------------|-----------------------|

C-15 constraint: Map Position must be copied verbatim from a Phase 2 row label. An empty or paraphrased
Map Position cell is a format failure. Do not paraphrase. Do not generalize.

Run WebSearch for at least one named competitor characterization. Cite inline.

---

### PHASE 4: WHITESPACE TABLE

C-12 structural constraint. Apparatus: table schema. An absent table or single-row table fails.

| Gap | What no named competitor owns |
|-----|-------------------------------|
| Competitive gap | [uncontested space from Phase 2 map — reference a specific named row] |
| Focus gap | [unaddressed segment or category — requires Phase 2 data and focus dimension simultaneously] |

DO NOT: Build only one row. Leave either row without Phase 2 grounding. Omit the combined paragraph.
DO: Fill both rows with grounded findings. Write one combined paragraph linking both gaps.

---

### PHASE 5: FINDINGS

3–5 findings. Each must reference at least one named Phase 2 row or Phase 3 competitor by label. No
free-floating findings.

---

AMEND: Exactly 3 items. Each names (1) what the user changes, (2) what changes in the output. Specific.

---

PRE-SUBMISSION VERIFICATION
For each structural constraint, verify the output:
[ ] C-13 (inertia mechanisms): Mechanism table present? Format-failure declared? Bilateral enforcement
    pair present (any label format — rejection example + acceptance example is the invariant; label
    format is a free variable)?
[ ] C-11 (pre-map): Pre-map table present? Format-failure declared? Bilateral enforcement pair present
    (any label format — rejection example + acceptance example is the invariant)?
[ ] C-12 (whitespace): Both rows present? Format-failure declared? Bilateral enforcement pair present
    (any label format — rejection example + acceptance example is the invariant)?

---

## V-03 — Single-Sentence Minimal Sufficient Form

**Axis:** Role sequence / lifecycle emphasis — opening assertion compressed to exactly one sentence that
names all three constraints and the apparatus type. No second sentence. No numbered SR block. Demonstrates
the minimal sufficient form for C-14/C-17.

**Hypothesis:** C-29 FULL PASS (5 pts). C-27 PARTIAL (2.5 pts — opening sentence uses "pre-map construct"
and "inertia mechanism construct" language but phase instructions use standard C-XX tokens without
construct-role headers; no position-agnostic statement). C-28 PARTIAL (2.5 pts — DO NOT/DO practiced,
label surface freedom not explicitly declared). Expected: 190.

---

The pre-map construct (C-11), inertia mechanism construct (C-13), and whitespace table (C-12) all enforce
via table schema — an absent table or empty row is an observable format failure.

SETUP: Detect the product domain from context (README, CLAUDE.md, package.json, or any Glob-discoverable
file). Do not ask. Infer domain, key features, and likely competitors automatically.

---

PRE-GENERATION INTEGRITY CHECK
Confirm all three structural constraints are present in this prompt before proceeding. For each, verify:
format artifact declared? format-failure declared? bilateral enforcement pair present?
[ ] C-13 inertia mechanism construct:
[ ] C-11 pre-map construct:
[ ] C-12 whitespace table:

---

### PHASE 1: INERTIA COMPETITOR

C-13 structural constraint. Apparatus: table schema. An absent mechanism table or empty mechanism row fails.

Assess the status quo first. Competitor 0: None / status quo. Threat level: HIGH. State explicitly.

PORTABILITY TEST: Each mechanism row must be so domain-specific it would be obviously wrong for a
different product category. Exact fail condition: if this content reads as true for a payroll tool or
a photo editor, it fails.

Populate the mechanism table (C-13 structural constraint — mechanism table required):

| Mechanism | Domain-specific behavior | Threat signal |
|-----------|--------------------------|---------------|
| WORKAROUND SATISFACTION | [the workaround teams use in this specific product context] | [threat signal] |
| SWITCHING COST | [the specific switching cost in this product context] | [threat signal] |
| HABIT LOCK-IN | [the specific habit pattern in this product context] | [threat signal] |

Table 1 above is the C-13 structural constraint (mechanism table). Apply portability test per row.

DO NOT: Omit the mechanism table. Leave any mechanism row empty. Write content that applies to a photo
editor or payroll tool.
DO: Fill all three rows with behavior so domain-specific it would be obviously wrong in a different product
category.

[Table 2 below is a portability summary — additional framing only; does not substitute for the mechanism
table for C-13 apparatus uniformity or C-19 purposes.]

| Mechanism | Portability verdict |
|-----------|---------------------|
| WORKAROUND SATISFACTION | [pass/fail + one-line reason] |
| SWITCHING COST | [pass/fail + one-line reason] |
| HABIT LOCK-IN | [pass/fail + one-line reason] |

---

### PHASE 2: COMPETITIVE LANDSCAPE MAP

C-11 structural constraint. Apparatus: table schema. An absent table or any row with an empty Map Label fails.

When a focus dimension is provided (market sizing OR positioning framework), build the map through that lens.
The focus is a lens — not a section. Weave focus data through competitor rows, findings, and narrative. Do
not create a dedicated focus section.

Complete the pre-map table before any competitor entry:

| Map Label | Category description | Focus signal (if provided) |
|-----------|----------------------|----------------------------|
| [segment or position name] | [description] | [market size or positioning detail] |

DO NOT: Begin competitor analysis before this table is complete. Use any Map Label downstream that is not
present verbatim in this table. Create a dedicated focus section.
DO: Complete all rows. Copy row labels verbatim — unchanged — into the Map Position column in Phase 3.

---

### PHASE 3: COMPETITOR ANALYSIS

For each named competitor, add a row. Competitor 0 (inertia) goes first — Map Position sourced from Phase 2:

| Competitor | Threat | Map Position | Key differentiator | Focus lens placement |
|------------|--------|--------------|--------------------|-----------------------|

C-15 constraint: Map Position must be copied verbatim from a Phase 2 row label. An empty or paraphrased
Map Position cell is a format failure. Do not paraphrase. Do not generalize.

Run WebSearch for at least one named competitor characterization. Cite inline.

---

### PHASE 4: WHITESPACE TABLE

C-12 structural constraint. Apparatus: table schema. An absent table or single-row table fails.

| Gap | What no named competitor owns |
|-----|-------------------------------|
| Competitive gap | [uncontested space from Phase 2 map — reference a specific named row] |
| Focus gap | [unaddressed segment or category — requires Phase 2 data and focus dimension simultaneously] |

DO NOT: Build only one row. Leave either row without Phase 2 grounding. Omit the combined paragraph.
DO: Fill both rows with grounded findings. Write one combined paragraph linking both gaps.

---

### PHASE 5: FINDINGS

3–5 findings. Each must reference at least one named Phase 2 row or Phase 3 competitor by label. No
free-floating findings.

---

AMEND: Exactly 3 items. Each names (1) what the user changes, (2) what changes in the output. Specific.

---

PRE-SUBMISSION VERIFICATION
For each structural constraint, verify the output:
[ ] C-13 (inertia mechanisms): Mechanism table present? Format-failure declared? Bilateral enforcement
    pair present (rejection example + acceptance example)?
[ ] C-11 (pre-map): Pre-map table present? Format-failure declared? Bilateral enforcement pair present
    (rejection example + acceptance example)?
[ ] C-12 (whitespace): Both rows present? Format-failure declared? Bilateral enforcement pair present
    (rejection example + acceptance example)?

---

## V-04 — Construct Labeling + Label Surface Declaration (C-27 + C-28)

**Axis:** Combination — construct-role phase headers with position-agnostic statement (C-27) AND explicit
bilateral label surface declaration (C-28). WRONG:/RIGHT: labels used throughout to demonstrate the label
surface freedom explicitly. Two-sentence opening retained.

**Hypothesis:** C-27 FULL PASS (5 pts — phase headers use construct-role names + position-agnostic
statement). C-28 FULL PASS (5 pts — explicit free-variable declaration + WRONG:/RIGHT: demonstrates
label freedom). C-29 PARTIAL (2.5 pts — two-sentence form, not demonstrably minimal). Expected: 192.5.

---

The pre-map construct (C-11), inertia mechanism construct (C-13), and whitespace table (C-12) enforce
via table schema — construct compliance is position-agnostic; these constructs satisfy C-11 and C-13
wherever they appear in the phase sequence. Bilateral pair label format is a free variable: WRONG:/RIGHT:,
DO NOT/DO, FAILS/PASS, or any structural framing (rejection example + acceptance example) satisfies the
bilateral pair requirement — only the bilateral structure (one rejection example + one acceptance example)
is prescriptive.

SETUP: Detect the product domain from context (README, CLAUDE.md, package.json, or any Glob-discoverable
file). Do not ask. Infer domain, key features, and likely competitors automatically.

---

PRE-GENERATION INTEGRITY CHECK
Confirm all three structural constraints are present in this prompt before proceeding. For each, verify:
format artifact declared? format-failure declared? bilateral enforcement pair present?
[ ] C-13 inertia mechanism construct:
[ ] C-11 pre-map construct:
[ ] C-12 whitespace table:

---

### PHASE 1: INERTIA MECHANISM CONSTRUCT

C-13 structural constraint. Apparatus: table schema. An absent mechanism table or empty mechanism row fails.

Assess the status quo first. Competitor 0: None / status quo. Threat level: HIGH. State explicitly.

PORTABILITY TEST: Each mechanism row must be so domain-specific it would be obviously wrong for a
different product category. Exact fail condition: if this content reads as true for a payroll tool or
a photo editor, it fails.

Populate the mechanism table (C-13 structural constraint — mechanism table required):

| Mechanism | Domain-specific behavior | Threat signal |
|-----------|--------------------------|---------------|
| WORKAROUND SATISFACTION | [the workaround teams use in this specific product context] | [threat signal] |
| SWITCHING COST | [the specific switching cost in this product context] | [threat signal] |
| HABIT LOCK-IN | [the specific habit pattern in this product context] | [threat signal] |

Table 1 above is the C-13 structural constraint (mechanism table). Apply portability test per row.

WRONG: Omit the mechanism table. Leave any mechanism row empty. Write content that applies to a photo
editor or payroll tool.
RIGHT: Fill all three rows with behavior so domain-specific it would be obviously wrong in a different
product category.

[Table 2 below is a portability summary — additional framing only; does not substitute for the mechanism
table for C-13 apparatus uniformity or C-19 purposes.]

| Mechanism | Portability verdict |
|-----------|---------------------|
| WORKAROUND SATISFACTION | [pass/fail + one-line reason] |
| SWITCHING COST | [pass/fail + one-line reason] |
| HABIT LOCK-IN | [pass/fail + one-line reason] |

---

### PHASE 2: PRE-MAP CONSTRUCT

C-11 structural constraint. Apparatus: table schema. An absent table or any row with an empty Map Label fails.

When a focus dimension is provided (market sizing OR positioning framework), build the map through that lens.
The focus is a lens — not a section. Weave focus data through competitor rows, findings, and narrative. Do
not create a dedicated focus section.

Complete the pre-map table before any competitor entry:

| Map Label | Category description | Focus signal (if provided) |
|-----------|----------------------|----------------------------|
| [segment or position name] | [description] | [market size or positioning detail] |

WRONG: Begin competitor analysis before this table is complete. Use any Map Label downstream that is not
present verbatim in this table. Create a dedicated focus section.
RIGHT: Complete all rows. Copy row labels verbatim — unchanged — into the Map Position column in Phase 3.

---

### PHASE 3: COMPETITOR ANALYSIS

For each named competitor, add a row. Competitor 0 (inertia) goes first — Map Position sourced from Phase 2:

| Competitor | Threat | Map Position | Key differentiator | Focus lens placement |
|------------|--------|--------------|--------------------|-----------------------|

C-15 constraint: Map Position must be copied verbatim from a Phase 2 row label. An empty or paraphrased
Map Position cell is a format failure. Do not paraphrase. Do not generalize.

Run WebSearch for at least one named competitor characterization. Cite inline.

---

### PHASE 4: WHITESPACE TABLE

C-12 structural constraint. Apparatus: table schema. An absent table or single-row table fails.

| Gap | What no named competitor owns |
|-----|-------------------------------|
| Competitive gap | [uncontested space from Phase 2 map — reference a specific named row] |
| Focus gap | [unaddressed segment or category — requires Phase 2 data and focus dimension simultaneously] |

WRONG: Build only one row. Leave either row without Phase 2 grounding. Omit the combined paragraph.
RIGHT: Fill both rows with grounded findings. Write one combined paragraph linking both gaps.

---

### PHASE 5: FINDINGS

3–5 findings. Each must reference at least one named Phase 2 row or Phase 3 competitor by label. No
free-floating findings.

---

AMEND: Exactly 3 items. Each names (1) what the user changes, (2) what changes in the output. Specific.

---

PRE-SUBMISSION VERIFICATION
For each structural constraint, verify the output:
[ ] C-13 (inertia mechanism construct): Mechanism table present? Format-failure declared? Bilateral
    enforcement pair present (any label format — rejection example + acceptance example is the invariant;
    label format is a free variable)?
[ ] C-11 (pre-map construct): Pre-map table present? Format-failure declared? Bilateral enforcement
    pair present (any label format — rejection example + acceptance example is the invariant)?
[ ] C-12 (whitespace table): Both rows present? Format-failure declared? Bilateral enforcement pair
    present (any label format — rejection example + acceptance example is the invariant)?

---

## V-05 — Full v9 Synthesis (C-27 + C-28 + C-29)

**Axis:** Full combination — single-sentence opening assertion that simultaneously names all three
constraints, apparatus type, position-agnostic statement, and bilateral label surface freedom (C-29).
Construct-role phase headers (C-27). WRONG:/RIGHT: labels with explicit free-variable declaration (C-28).

**Hypothesis:** C-27 FULL PASS (5 pts — phase headers use construct-role names + position-agnostic in
opening). C-28 FULL PASS (5 pts — explicit declaration in opening + loop language + WRONG:/RIGHT:
demonstrates freedom). C-29 FULL PASS (5 pts — single sentence, complete, names all three constraints
and apparatus type, no SR block). Expected composite: 195.

---

The pre-map construct (C-11), inertia mechanism construct (C-13), and whitespace table (C-12) enforce
via table schema — construct compliance is position-agnostic, bilateral pair label format is a free
variable (any structural framing satisfies; only the bilateral structure is prescriptive), and an absent
table or empty row is an observable format failure.

SETUP: Detect the product domain from context (README, CLAUDE.md, package.json, or any Glob-discoverable
file). Do not ask. Infer domain, key features, and likely competitors automatically.

---

PRE-GENERATION INTEGRITY CHECK
Confirm all three structural constraints are present in this prompt before proceeding. For each, verify:
format artifact declared? format-failure declared? bilateral enforcement pair present?
[ ] C-13 inertia mechanism construct:
[ ] C-11 pre-map construct:
[ ] C-12 whitespace table:

---

### PHASE 1: INERTIA MECHANISM CONSTRUCT

C-13 structural constraint. Apparatus: table schema. An absent mechanism table or empty mechanism row
fails. The inertia mechanism construct satisfies C-13 here; construct compliance is position-agnostic.

Assess the status quo first. Competitor 0: None / status quo. Threat level: HIGH. State explicitly.

PORTABILITY TEST: Each mechanism row must be so domain-specific it would be obviously wrong for a
different product category. Exact fail condition: if this content reads as true for a payroll tool or
a photo editor, it fails.

Populate the mechanism table (C-13 structural constraint — mechanism table required):

| Mechanism | Domain-specific behavior | Threat signal |
|-----------|--------------------------|---------------|
| WORKAROUND SATISFACTION | [the workaround teams use in this specific product context] | [threat signal] |
| SWITCHING COST | [the specific switching cost in this product context] | [threat signal] |
| HABIT LOCK-IN | [the specific habit pattern in this product context] | [threat signal] |

Table 1 above is the C-13 structural constraint (mechanism table). Apply portability test per row.

WRONG: Omit the mechanism table. Leave any mechanism row empty. Write content that applies to a photo
editor or payroll tool.
RIGHT: Fill all three rows with behavior so domain-specific it would be obviously wrong in a different
product category.

[Table 2 below is a portability summary — additional framing only; does not substitute for the mechanism
table for C-13 apparatus uniformity or C-19 purposes.]

| Mechanism | Portability verdict |
|-----------|---------------------|
| WORKAROUND SATISFACTION | [pass/fail + one-line reason] |
| SWITCHING COST | [pass/fail + one-line reason] |
| HABIT LOCK-IN | [pass/fail + one-line reason] |

---

### PHASE 2: PRE-MAP CONSTRUCT

C-11 structural constraint. Apparatus: table schema. An absent table or any row with an empty Map Label
fails. The pre-map construct satisfies C-11 here; construct compliance is position-agnostic.

When a focus dimension is provided (market sizing OR positioning framework), build the map through that lens.
The focus is a lens — not a section. Weave focus data through competitor rows, findings, and narrative. Do
not create a dedicated focus section.

Complete the pre-map table before any competitor entry:

| Map Label | Category description | Focus signal (if provided) |
|-----------|----------------------|----------------------------|
| [segment or position name] | [description] | [market size or positioning detail] |

WRONG: Begin competitor analysis before this table is complete. Use any Map Label downstream that is not
present verbatim in this table. Create a dedicated focus section.
RIGHT: Complete all rows. Copy row labels verbatim — unchanged — into the Map Position column in Phase 3.

---

### PHASE 3: COMPETITOR ANALYSIS

For each named competitor, add a row. Competitor 0 (inertia) goes first — Map Position sourced from Phase 2:

| Competitor | Threat | Map Position | Key differentiator | Focus lens placement |
|------------|--------|--------------|--------------------|-----------------------|

C-15 constraint: Map Position must be copied verbatim from a Phase 2 row label. An empty or paraphrased
Map Position cell is a format failure. Do not paraphrase. Do not generalize.

Run WebSearch for at least one named competitor characterization. Cite inline.

---

### PHASE 4: WHITESPACE TABLE

C-12 structural constraint. Apparatus: table schema. An absent table or single-row table fails.

| Gap | What no named competitor owns |
|-----|-------------------------------|
| Competitive gap | [uncontested space from Phase 2 map — reference a specific named row] |
| Focus gap | [unaddressed segment or category — requires Phase 2 data and focus dimension simultaneously] |

WRONG: Build only one row. Leave either row without Phase 2 grounding. Omit the combined paragraph.
RIGHT: Fill both rows with grounded findings. Write one combined paragraph linking both gaps.

---

### PHASE 5: FINDINGS

3–5 findings. Each must reference at least one named Phase 2 row or Phase 3 competitor by label. No
free-floating findings.

---

AMEND: Exactly 3 items. Each names (1) what the user changes, (2) what changes in the output. Specific.

---

PRE-SUBMISSION VERIFICATION
For each structural constraint, verify the output:
[ ] C-13 (inertia mechanism construct): Mechanism table present? Format-failure declared? Bilateral
    enforcement pair present (any label format — rejection example + acceptance example is the
    invariant; label format is a free variable)?
[ ] C-11 (pre-map construct): Pre-map table present? Format-failure declared? Bilateral enforcement
    pair present (any label format — rejection example + acceptance example is the invariant)?
[ ] C-12 (whitespace table): Both rows present? Format-failure declared? Bilateral enforcement pair
    present (any label format — rejection example + acceptance example is the invariant)?

---

## Variation Summary

| Variation | Axis | Key change | C-27 | C-28 | C-29 | Expected |
|-----------|------|------------|------|------|------|---------|
| V-01 | Lifecycle emphasis | Construct-role phase headers + position-agnostic statement | PASS (5) | PARTIAL (2.5) | PARTIAL (2.5) | 190 |
| V-02 | Phrasing register | Explicit bilateral label surface declaration in opening + loop | PARTIAL (2.5) | PASS (5) | PARTIAL (2.5) | 190 |
| V-03 | Role sequence | Single-sentence opening, minimal sufficient form | PARTIAL (2.5) | PARTIAL (2.5) | PASS (5) | 190 |
| V-04 | C-27 + C-28 | Construct headers + label surface declaration + WRONG:/RIGHT: | PASS (5) | PASS (5) | PARTIAL (2.5) | 192.5 |
| V-05 | C-27 + C-28 + C-29 | Single sentence embedding all three + construct headers + WRONG:/RIGHT: | PASS (5) | PASS (5) | PASS (5) | 195 |

**Open questions:**

Q1: Does a position-agnostic statement in the opening assertion (without phrase-level construct headers)
earn C-27 PARTIAL or PASS? V-01 vs V-03 provides differential evidence.

Q2: Does the single opening sentence in V-05 — which packs position-agnostic + label-surface-free into
one sentence alongside constraint names + apparatus — still count as "structurally complete" for C-29,
or does the additional content disqualify the minimal-form reading?

Q3: Does the phase-instruction line "The inertia mechanism construct satisfies C-13 here; construct
compliance is position-agnostic." in V-05 provide additional C-27 enforcement beyond the opening sentence,
or is it redundant?
