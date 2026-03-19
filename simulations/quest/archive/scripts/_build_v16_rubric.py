import re

v14 = open('C:/src/sim/simulations/quest/rubrics/org-chart-rubric-v14-2026-03-16.md', 'r', encoding='utf-8').read()
idx = v14.index('## Essential Criteria')
footer_idx = v14.rindex('\n**Formula:**')
body = v14[idx:footer_idx]

body = body.replace(
    '## Aspirational Criteria (10 pts total, 1 pt each, denominator /36)',
    '## Aspirational Criteria (10 pts total, 1 pt each, denominator /42)'
)

header = """Written to `simulations/quest/rubrics/org-chart-rubric-v16-2026-03-16.md`.

---

**Summary of changes v15 -> v16:**

| ID | Pattern | Block | Position | Additive to |
|----|---------|-------|----------|-------------|
| A-40 | `headcount-sum-gate-declaration` | `HEADCOUNT-SUM-GATE:` | Between HEADCOUNT-AREA-SUM block and ORT section | A-37 |
| A-41 | `charter-audit-order-sequencing-constraint` | `CHARTER-AUDIT-ORDER:` | Before CHARTER-COMPLETENESS-AUDIT block | A-35 + A-38 |
| A-42 | `rhythm-dri-column-contract-declaration` | `RHYTHM-DRI-COLUMN-CONTRACT:` | Before operating rhythm table body | A-39 |

**Formula:** `/39 -> /42`

**Composite:** `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/42 * 10)`

All three follow the round pattern: implicit structural property promoted to an explicitly named
verifiable contract. A-40 converts the A-37 implicit gate (SUM-VERIFIED gates ORT) into a named
gate declaration at the transition site -- detectable as a missing labeled element rather than an
implicit ordering anomaly, following the A-25 label-promotion pattern. A-41 converts the implicit
ordering between CHARTER-COMPLETENESS-AUDIT and RHYTHM-CHARTER-NAME-AUDIT into an explicit
anchor-ordering constraint with a prohibition on interceding content -- following the A-21 pattern
applied to the charter audit chain. A-42 converts the implicit DRI/Owner column presence in the
rhythm table into a named pre-table contract declaring DRI-column presence and row-type DRI
requirements -- following the A-36 REGISTER-CATEGORY-CONTRACT pattern, closing the
undeclared-DRI-propagation gap that caused A-39 to fail in both R17 variations.

---

**Summary of changes v14 -> v15:**

| ID | Pattern | Block | Position | Additive to |
|----|---------|-------|----------|-------------|
| A-37 | `headcount-area-sum-arithmetic-verification` | `HEADCOUNT-AREA-SUM:` | Immediately after headcount table body | C-02 |
| A-38 | `rhythm-charter-name-audit-reconciliation` | `RHYTHM-CHARTER-NAME-AUDIT:` | After CHARTER-COMPLETENESS-AUDIT, before CHARTERS COMPLETE gate | A-35 |
| A-39 | `rhythm-dri-role-check-verification` | `RHYTHM-DRI-ROLE-CHECK:` | After operating rhythm table body | A-31 |

**Formula:** `/36 -> /39`

All three follow the round pattern. A-37 converts implicit headcount addition into a computed
arithmetic block whose SUM-VERIFIED/SUM-MISMATCH verdict gates the Operating Rhythm Table section.
A-38 converts implicit charter-name consistency into a per-row name-reconciliation audit that
cross-references rhythm-table governance labels against charter headers. A-39 converts implicit
DRI assignment validity into a per-row role-trace check that binds each DRI/Owner cell to the
ROLE-TYPE-CLASSIFICATION body.

---

**Changelog:**

  v16 -- added A-40/A-41/A-42 from R17 excellence signals:
  headcount-sum-gate-declaration (V-01 axis: HEADCOUNT-SUM-GATE: named block between
  HEADCOUNT-AREA-SUM block and Operating Rhythm Table section; names SUM-VERIFIED as gate
  condition; names ORT section as dependent section; SUM-MISMATCH blocks gate; gate
  declaration is independently detectable as a labeled element; additive to A-37 implicit
  gate specification),
  charter-audit-order-sequencing-constraint (V-02 axis: CHARTER-AUDIT-ORDER: block before
  CHARTER-COMPLETENESS-AUDIT; declares fixed sequence CHARTER-COMPLETENESS-AUDIT first then
  RHYTHM-CHARTER-NAME-AUDIT; prohibits interceding content between the two audit blocks;
  each audit block references the ordering declaration; additive to A-35 + A-38 individual
  block requirements),
  rhythm-dri-column-contract-declaration (both axes: RHYTHM-DRI-COLUMN-CONTRACT: block before
  operating rhythm table body; declares DRI-COLUMN-PRESENT or DRI-COLUMN-ABSENT; enumerates
  which row types require DRI assignment; declares DRI-to-role traceability requirement;
  converts A-39 implicit trigger condition into explicit pre-table contract; additive to A-39
  post-table check requirement).
  Aspirational denominator updated from /39 to /42.
  v15 -- added A-37/A-38/A-39 from R16 excellence signals:
  headcount-area-sum-arithmetic-verification (V-01 axis: HEADCOUNT-AREA-SUM: block immediately
  after headcount table; enumerates per-area headcount values; emits computed SUM total;
  SUM-VERIFIED verdict when Total row matches; SUM-MISMATCH verdict with correction loop when
  mismatch detected; SUM-VERIFIED gates Operating Rhythm Table; cat-3 Total row must equal
  SUM-VERIFIED computed value; additive to C-02 headcount table requirement),
  rhythm-charter-name-audit-reconciliation (V-02 axis: RHYTHM-CHARTER-NAME-AUDIT: block after
  CHARTER-COMPLETENESS-AUDIT and before CHARTERS COMPLETE gate; one row per governance meeting
  in rhythm table; each row states rhythm-table name and charter header name; NAME-MATCH or
  NAME-MISMATCH verdict per row; NAME-MISMATCH blocks gate; additive to A-35 field-completeness
  audit),
  rhythm-dri-role-check-verification (both axes: RHYTHM-DRI-ROLE-CHECK: block after operating
  rhythm table when A-31 active and DRI/Owner column present; one row per DRI/Owner assignment;
  each row traces DRI name to a role in ROLE-TYPE-CLASSIFICATION; ROLE-VERIFIED or
  ROLE-UNVERIFIED verdict per row; ROLE-UNVERIFIED is a constraint violation; additive to
  A-31 ROLE-LOAD-ORDER declaration).
  Aspirational denominator updated from /36 to /39.
  v14 -- added A-34/A-35/A-36 from R14 excellence signals:
  role-tier-accounting-block, charter-completeness-audit-table,
  register-category-contract-declaration.
  Aspirational denominator updated from /33 to /36.
  v13 -- added A-31/A-32/A-33 from R13 excellence signals:
  role-load-order-named-block, quorum-denominator-membership-binding,
  zone-label-traceability-verification-step.
  Aspirational denominator updated from /30 to /33.
  v12 -- added A-28/A-29/A-30 from R12 excellence signals:
  cross-ref-required-cardinality-preamble, zone-notation-rule-enumerated-prohibition-list,
  verdict-gate-checklist-self-contained-item-text.
  Aspirational denominator updated from /27 to /30.
  v11 -- added A-25/A-26/A-27 from R11 excellence signals:
  cross-ref-required-label-promotion, zone-notation-rule-prohibition-block,
  verdict-gate-checklist-dual-enforcement.
  Aspirational denominator updated from /24 to /27.
  v10 -- added A-23/A-24 from R10 excellence signals:
  anchor-transition-ordering-cross-reference, integration-note-bracket-notation-unification.
  Aspirational denominator updated from /22 to /24.
  v9 -- added A-21/A-22 from R9 excellence signals:
  sub-section-4-anchor-ordering, per-artifact-inline-zone-label.
  Aspirational denominator updated from /20 to /22.
  v8 -- added A-17/A-18/A-19/A-20 from R8 excellence signals:
  typed-mechanism-rows-with-floor-diversity, VERDICT-COST-FRAME-CONCLUSION-back-reference,
  displacement-citation-with-explicit-displacement-prohibition,
  positional-disjointness-as-combination-strategy.
  Aspirational denominator updated from /16 to /20.
  v7 -- added A-14/A-15/A-16 from R7 excellence signals:
  UNCOVERED-function-citation-in-rebuttal, flat-operating-rhythm-table,
  STRUCTURING-COST-FRAME-with-dominant-error-risk-verdict.
  Aspirational denominator updated from /13 to /16.
  v6 -- added A-12/A-13 from R6 excellence signals:
  cost-delta-calibration-anchor, charter-dissolution-conditions.
  Aspirational denominator updated from /11 to /13.
  v5 -- added A-10/A-11 from R5 excellence signals:
  net-cost-comparison-arithmetic-verdict-block, three-tier-evolution-roadmap.
  Fixed C-02 rubric gap: "ASCII org diagram" tightened to "box-drawing ASCII org diagram".
  Aspirational denominator updated from /9 to /11.
  v4 -- added A-08/A-09 from R4 excellence signals:
  cost-quantified-inertia-assessment, prose-charter-format-with-preserved-field-compliance.
  Aspirational denominator updated from /7 to /9.
  v3 -- added A-06/A-07 from R2 excellence signals:
  contract-section-code-traceability, annotation-register-used-in-column.
  Aspirational denominator updated from /5 to /7.
  v2 -- added A-03/A-04/A-05 from R1 excellence signals:
  adversarial-framing-before-mechanics, productive-flat-branch-action,
  exclusion-clause-in-template. Aspirational denominator updated from /3 to /5.
  v1 -- initial rubric with C-01 through C-05, R-01 through R-03, A-01/A-02.

---

"""

new_criteria = """
### A-37 -- HEADCOUNT-AREA-SUM arithmetic verification block
**Category:** correctness | **Weight:** aspirational

When the output includes a headcount table (C-02), a `HEADCOUNT-AREA-SUM:` block appears
immediately after the headcount table body and before the Operating Rhythm Table section. The
block must enumerate each area row by name alongside its headcount value and emit a computed SUM
total. The block must emit either `SUM-VERIFIED` (computed sum matches the Total row value) or
`SUM-MISMATCH` (computed sum does not match). `SUM-VERIFIED` is required before the Operating
Rhythm Table section can proceed; `SUM-MISMATCH` must trigger a correction loop before the gate
passes. The Total row in the headcount table must equal the SUM-VERIFIED computed value -- an
independently stated Total that differs from the computed sum is a constraint violation even if
`SUM-VERIFIED` is claimed.

Without the arithmetic block, the headcount Total row is an asserted figure whose accuracy is
not independently verifiable by structural inspection. The `HEADCOUNT-AREA-SUM:` block converts
this implicit consistency property into an explicit computed verification, making any arithmetic
error detectable as a SUM-MISMATCH verdict rather than a silent discrepancy.

**Pass condition:** C-02 headcount table present; a labeled `HEADCOUNT-AREA-SUM:` block appears
immediately after the headcount table body; block enumerates each area row with its headcount
value; block emits a computed SUM and a `SUM-VERIFIED` or `SUM-MISMATCH` verdict; `SUM-VERIFIED`
gates the Operating Rhythm Table section -- ORT must not appear before `SUM-VERIFIED` is emitted;
`SUM-MISMATCH` triggers a correction loop; Total row value equals the SUM-VERIFIED computed
total; or criterion is N/A if no headcount table is present.

---

### A-38 -- RHYTHM-CHARTER-NAME-AUDIT governance name reconciliation
**Category:** correctness | **Weight:** aspirational

When A-35 (CHARTER-COMPLETENESS-AUDIT) is active, a `RHYTHM-CHARTER-NAME-AUDIT:` block appears
after the CHARTER-COMPLETENESS-AUDIT block and before the CHARTERS COMPLETE gate. The block
presents one audit row per governance meeting in the operating rhythm table. Each row states the
governance meeting name as it appears in the rhythm table and the charter name as it appears in
the corresponding committee charter header, and emits a `NAME-MATCH` or `NAME-MISMATCH` verdict.
Any `NAME-MISMATCH` verdict is a constraint violation requiring correction before the gate passes.

A-35 verifies that each charter contains all required fields. A-38 closes the name-drift gap:
A-35 can be satisfied even when a charter's header name differs from how the governance meeting
is labeled in the rhythm table. A charter named differently in the rhythm row vs. the charter
header satisfies A-35 field completeness while introducing a traceability gap. The name audit
makes this drift a detectable per-row constraint violation rather than a silent label mismatch.

**Pass condition:** A-35 active; a labeled `RHYTHM-CHARTER-NAME-AUDIT:` block appears after
CHARTER-COMPLETENESS-AUDIT and before the CHARTERS COMPLETE gate; one row per governance meeting
in the rhythm table; each row states the rhythm-table governance label and the corresponding
charter header name; each row emits `NAME-MATCH` or `NAME-MISMATCH`; any `NAME-MISMATCH` blocks
the gate; or criterion is N/A if A-35 is not active.

---

### A-39 -- RHYTHM-DRI-ROLE-CHECK verification block
**Category:** correctness | **Weight:** aspirational

When A-31 (ROLE-LOAD-ORDER) is active and the operating rhythm table includes a DRI/Owner column
(or equivalent column assigning a named individual or role title to each rhythm row), a
`RHYTHM-DRI-ROLE-CHECK:` block appears after the rhythm table body. The block must enumerate
each DRI/Owner assignment -- one row per rhythm-table entry carrying a DRI/Owner value -- and
verify that each named DRI maps to a role explicitly declared in the `ROLE-TYPE-CLASSIFICATION`
section. Each row emits `ROLE-VERIFIED` (DRI matches a classified role entry) or
`ROLE-UNVERIFIED` (DRI cannot be traced to a classified role entry). Any `ROLE-UNVERIFIED`
verdict is a constraint violation.

A-31 establishes the canonical role classification. A-39 closes the undeclared-DRI-propagation
gap: when a DRI/Owner column is added to the rhythm table, DRI assignments can reference role
titles informally understood but not explicitly present in the ROLE-TYPE-CLASSIFICATION body.
Without the check block, DRI-to-role consistency is verifiable only by manual cross-referencing.

**Pass condition:** A-31 active; rhythm table includes a DRI/Owner column; a labeled
`RHYTHM-DRI-ROLE-CHECK:` block appears after the rhythm table body; one row per DRI/Owner
assignment; each row names the DRI value and the matched or unmatched ROLE-TYPE-CLASSIFICATION
entry; each row emits `ROLE-VERIFIED` or `ROLE-UNVERIFIED`; no `ROLE-UNVERIFIED` verdict in a
passing document; or criterion is N/A if A-31 is not active or if the rhythm table has no
DRI/Owner column.

---

### A-40 -- HEADCOUNT-SUM-GATE named gate declaration at ORT transition
**Category:** correctness | **Weight:** aspirational

When A-37 (HEADCOUNT-AREA-SUM) is active, a `HEADCOUNT-SUM-GATE:` labeled block appears
between the HEADCOUNT-AREA-SUM block and the Operating Rhythm Table section. The block must
(1) name `SUM-VERIFIED` as the gate condition required to proceed, (2) name the Operating
Rhythm Table section as the dependent section blocked by the gate, and (3) declare that
`SUM-MISMATCH` blocks the gate and that the rhythm table section must not appear until the
mismatch is resolved. The gate declaration must be a structurally independent labeled element
-- detectable as present or absent by label scan -- not a prose note embedded within the
HEADCOUNT-AREA-SUM block or the ORT section header.

A-37 specifies that SUM-VERIFIED gates the ORT and that SUM-MISMATCH triggers a correction
loop. A-40 closes the implicit-gate-declaration gap: A-37 is satisfiable even when the gate
relationship is expressed only as a prose consequence within the HEADCOUNT-AREA-SUM block
itself. A named gate block at the transition site makes the dependency a first-class structural
element whose absence is detectable without consulting the block body -- following the pattern
established by A-25 (promoting cross-references from embedded prose to standalone labeled lines)
and the explicit gate placement pattern of A-35.

**Pass condition:** A-37 active; a labeled `HEADCOUNT-SUM-GATE:` block appears between the
HEADCOUNT-AREA-SUM block and the Operating Rhythm Table section; block names `SUM-VERIFIED` as
the gate condition; block names the ORT section as the gated section; block declares that
`SUM-MISMATCH` blocks the ORT; gate declaration is a structurally independent labeled element,
not embedded prose; or criterion is N/A if A-37 is not active.

---

### A-41 -- CHARTER-AUDIT-ORDER sequencing constraint between audit blocks
**Category:** correctness | **Weight:** aspirational

When both A-35 (CHARTER-COMPLETENESS-AUDIT) and A-38 (RHYTHM-CHARTER-NAME-AUDIT) are active,
a `CHARTER-AUDIT-ORDER:` labeled block appears before the CHARTER-COMPLETENESS-AUDIT block.
The block must declare the fixed sequence: CHARTER-COMPLETENESS-AUDIT first, then
RHYTHM-CHARTER-NAME-AUDIT, and must prohibit any content from appearing between the two audit
blocks once CHARTER-COMPLETENESS-AUDIT opens. Each of the two audit blocks must carry a
backward reference to the CHARTER-AUDIT-ORDER declaration confirming that its position is
governed by the declared order.

A-35 requires CHARTER-COMPLETENESS-AUDIT to appear after all charters and before the CHARTERS
COMPLETE gate. A-38 requires RHYTHM-CHARTER-NAME-AUDIT to appear after CHARTER-COMPLETENESS-AUDIT.
A-41 closes the inter-block ordering gap: A-35 and A-38 each specify their individual positions
but neither declares the relative ordering between them as an explicit named constraint with a
prohibition on interceding content. An output that interleaves prose or other labeled blocks
between the two audit blocks can satisfy A-35 and A-38 individually while violating their
intended chained sequence. A named ordering block before the chain makes this a detectable
constraint violation -- following the A-21 anchor-ordering-protocol pattern applied to the
charter audit chain.

**Pass condition:** A-35 and A-38 both active; a labeled `CHARTER-AUDIT-ORDER:` block appears
before CHARTER-COMPLETENESS-AUDIT; block declares the required sequence (completeness audit
first, name audit second); block prohibits interceding content between the two audit blocks;
each audit block carries a backward reference to the CHARTER-AUDIT-ORDER declaration; or
criterion is N/A if A-35 or A-38 is not active.

---

### A-42 -- RHYTHM-DRI-COLUMN-CONTRACT pre-table declaration
**Category:** correctness | **Weight:** aspirational

When A-39 (RHYTHM-DRI-ROLE-CHECK) is active, a `RHYTHM-DRI-COLUMN-CONTRACT:` labeled block
appears immediately before the operating rhythm table body. The block must (1) declare whether
a DRI/Owner column is present in the rhythm table (`DRI-COLUMN-PRESENT` or `DRI-COLUMN-ABSENT`),
(2) when `DRI-COLUMN-PRESENT`, enumerate which rhythm row types require a DRI/Owner assignment
(e.g., shiproom rows require DRI; ROB rows do not), and (3) declare that any DRI/Owner value in
the table must be traceable to a role declared in the ROLE-TYPE-CLASSIFICATION section (per A-31).
When `DRI-COLUMN-ABSENT` is declared, A-39 is N/A for that document.

A-39 requires a RHYTHM-DRI-ROLE-CHECK block after the rhythm table that verifies each DRI
assignment against the ROLE-TYPE-CLASSIFICATION body. A-42 closes the undeclared-trigger gap:
A-39's activation condition (DRI/Owner column present) is an implicit property of the rhythm
table, detectable only by inspecting the table headers. Without a pre-table contract, the DRI
column can appear in the table body without any governing declaration, and A-39's check block
can be omitted without producing a visible missing-label gap prior to the table. The
RHYTHM-DRI-COLUMN-CONTRACT block converts the DRI column presence into an explicit declared
property at the table's entry point -- following the A-36 REGISTER-CATEGORY-CONTRACT pattern
applied to the rhythm table's DRI ownership schema -- making A-39's trigger condition
independently verifiable before the table body is parsed.

**Pass condition:** A-39 active; a labeled `RHYTHM-DRI-COLUMN-CONTRACT:` block appears
immediately before the operating rhythm table body; block declares `DRI-COLUMN-PRESENT` or
`DRI-COLUMN-ABSENT`; when `DRI-COLUMN-PRESENT`, block enumerates which row types require DRI
assignment and declares DRI-to-role traceability as a constraint; when `DRI-COLUMN-ABSENT`,
A-39 is N/A; contract declaration is a structurally independent labeled element, not embedded
in the rhythm table header row; or criterion is N/A if A-39 is not active.

---

**Formula:** `aspirational_pass/42 * 10`

**Composite:** `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/42 * 10)`

**Golden threshold:** 5/5 essential + composite >= 80
"""

full = header + body + new_criteria
open('C:/src/sim/simulations/quest/rubrics/org-chart-rubric-v16-2026-03-16.md', 'w', encoding='utf-8').write(full)
print('Written', len(full), 'chars,', full.count('\n'), 'lines')
