Now I have everything I need. Let me score all five variations.

---

## discover-competitors-alt — R6 Scorecard

**Baseline:** R5 = 160/160 (all 22 criteria PASS across all five variations, rubric v4). Rubric v5 adds C-23–C-26 (4 new aspirational criteria). Max composite moves from 160 to 180.

---

### C-01 through C-22 — Inherited from R5

All five R6 variations preserve the full structural foundation of R5: C0 row in competitor table, per-row citation gate, WHITESPACE block with attribute-absence evidence, CROSS-DIMENSIONAL proof block (SOURCE / REDUCTION-1 / REDUCTION-2 / THEREFORE), findings section with structural Anchor column coercion, AMEND with exactly 3 adjustments including proof-rerun prescription, INERTIA-REF mechanism defined with per-finding citation requirement, NOT ACCEPTABLE examples for name-only anchoring, named failure states throughout, SOURCE slot declared before reduction arguments, gate-as-section with PASS/FAIL tables, and multi-gate PREFLIGHT block. **All 22 criteria: PASS across all five variations** (same structural evidence base as R5; no regression introduced in R6 revisions).

---

### C-23 — Output contract slot format specification

Pass condition: At least one output contract slot specifies both a label AND a required structural format or template for the value that fills it; label-only does not satisfy.

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | OUTPUT CONTRACT table (3-col: Slot / Label / Required format) contains five slots each with a format template: `[C0 name]: [specific mechanism]`, `Row C{N}, {attribute}: "{value}"`, `Row C{N} — {attribute}: {absent / "None" / "N/A" / uncontested value}`, `{row label}, {attribute}: "{quoted value}"`, `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}`. Every slot specifies both label and format shape. |
| V-02 | **PASS** | OUTPUT CONTRACT table (4-col: Slot / Label / Required format / Filled by phase) — the Required format column is structurally dedicated to format shapes. Each of five slots carries a distinct format template. The 4-column structure makes the format specification the primary purpose of each row rather than a secondary note. |
| V-03 | **PASS** | OUTPUT CONTRACTS subsection (inside PREFLIGHT) has a 3-col table (Slot / Label / Required format) with five slots each specifying a format template. Co-location inside PREFLIGHT means the format declarations are auditable without leaving the gate block. |
| V-04 | **PASS** | OUTPUT CONTRACT (separate section after PREFLIGHT) is a 4-col table (Slot / Label / Required format / Filled by phase). Each slot carries a format template identical in structure to V-02 but with GATE 4 as the producing phase for INERTIA-REF. Five slots, five format templates. |
| V-05 | **PASS** | OUTPUT CONTRACTS subsection (inside PREFLIGHT) is a 4-col table (Slot / Label / Required format / Filled by phase) with five format-specified slots. Maximum information density: format shapes co-located with all gates inside the single PREFLIGHT section. |

**C-23: PASS — all five.**

---

### C-24 — Phase-to-contract back-references

Pass condition: At least one producing phase explicitly names the output contract slot it fills at the point of production; bidirectional — contract must forward-declare and phase must back-reference by same label; one-directional does not satisfy.

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | OUTPUT CONTRACT forward-declares five slot labels before any phase. Phase headings back-reference by exact label: "PHASE 2: COMPETITOR TABLE (fills Anchor column value — OUTPUT CONTRACT)"; "PHASE 3: WHITESPACE (fills Absence evidence block — OUTPUT CONTRACT)"; "PHASE 4: CROSS-DIMENSIONAL FINDING (fills SOURCE slot — OUTPUT CONTRACT)"; "PHASE 5: FINDINGS TABLE (fills Anchor column value and INERTIA-REF-DELTA — OUTPUT CONTRACT)." Four producing phases, four bidirectional links. |
| V-02 | **PASS** | OUTPUT CONTRACT forward-declares slots with "Filled by phase" column naming responsible phase. Phases close the loop: "PHASE 2: INERTIA ASSESSMENT (fills INERTIA-REF slot — OUTPUT CONTRACT)"; "PHASE 3: COMPETITOR TABLE (fills Anchor column value — OUTPUT CONTRACT)"; "PHASE 4: WHITESPACE (fills Absence evidence block — OUTPUT CONTRACT)"; "PHASE 5: CROSS-DIMENSIONAL FINDING (fills SOURCE slot — OUTPUT CONTRACT)"; "PHASE 6: FINDINGS TABLE (fills Anchor column value and INERTIA-REF-DELTA column value — OUTPUT CONTRACT)." The "Filled by phase" column makes the forward link machine-readable; phase headings make the back-reference machine-readable. |
| V-03 | **PASS** | OUTPUT CONTRACTS subsection (inside PREFLIGHT) forward-declares five slot labels. Phase headings back-reference using "PREFLIGHT > OUTPUT CONTRACTS" path: "PHASE 2: COMPETITOR TABLE (fills Anchor column — PREFLIGHT > OUTPUT CONTRACTS)"; "PHASE 3: WHITESPACE (fills Absence evidence block — PREFLIGHT > OUTPUT CONTRACTS)"; "PHASE 4: CROSS-DIMENSIONAL FINDING (fills SOURCE slot — PREFLIGHT > OUTPUT CONTRACTS)"; "PHASE 5: FINDINGS TABLE (fills Anchor column and INERTIA-REF-DELTA — PREFLIGHT > OUTPUT CONTRACTS)." Full-path label reference. |
| V-04 | **PASS** | OUTPUT CONTRACT (4-col, after PREFLIGHT) forward-declares five slots with "Filled by phase" column. Phase headings close the loop: "PHASE 2: COMPETITOR TABLE (fills Anchor column value — OUTPUT CONTRACT)"; "PHASE 3: WHITESPACE (fills Absence evidence block — OUTPUT CONTRACT)"; "PHASE 4: CROSS-DIMENSIONAL FINDING (fills SOURCE slot — OUTPUT CONTRACT)"; "PHASE 5: FINDINGS TABLE (fills Anchor column value and INERTIA-REF-DELTA — OUTPUT CONTRACT)." Bidirectional tracing via table column + phase headings, as in V-02. |
| V-05 | **PASS** | OUTPUT CONTRACTS subsection (inside PREFLIGHT, 4-col) forward-declares five slots. Phase headings use full path: "PHASE 2: COMPETITOR TABLE (fills Anchor column — PREFLIGHT > OUTPUT CONTRACTS)"; "PHASE 3: WHITESPACE (fills Absence evidence block — PREFLIGHT > OUTPUT CONTRACTS)"; "PHASE 4: CROSS-DIMENSIONAL FINDING (fills SOURCE slot — PREFLIGHT > OUTPUT CONTRACTS)"; "PHASE 5: FINDINGS TABLE (fills Anchor column and INERTIA-REF-DELTA — PREFLIGHT > OUTPUT CONTRACTS)." Most explicit tracing: 4-col contract + full-path headings in every producing phase. |

**C-24: PASS — all five.**

---

### C-25 — Cross-table structural coercion

Pass condition: Structural column coercion (C-20 mechanism) applied independently in both a collection-phase table AND a synthesis/findings-phase table; single-table coercion — even with multiple coerced columns — does not satisfy.

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | Collection phase (Phase 2): "**Anchor column** (structural — fills Anchor column value, OUTPUT CONTRACT): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed and must be rewritten." Synthesis phase (Phase 5): "**Anchor column** (structural — fills Anchor column value, OUTPUT CONTRACT): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed; apply GATE 2" AND "**INERTIA-REF-DELTA column** (structural): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` — a cell with only 'N/A' or a competitor name is malformed." Independent format templates in two separate tables. |
| V-02 | **PASS** | Collection phase (Phase 3): "**Anchor column** (structural — fills Anchor column value slot, OUTPUT CONTRACT): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed." Synthesis phase (Phase 6): "**Anchor** (fills Anchor column value slot, OUTPUT CONTRACT): `Row C{N}, {attribute}: "{value}"`" AND "**INERTIA-REF-DELTA** (fills INERTIA-REF-DELTA column value slot, OUTPUT CONTRACT): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}`." Two tables, each with independently defined format templates. |
| V-03 | **PASS** | Collection phase (Phase 2): "Anchor column (structural): `Row C{N}, {attribute}: "{value}"` — syntactically malformed cells trigger GATE 2 before rule evaluation." Synthesis phase (Phase 5): "**Anchor** (structural): `Row C{N}, {attribute}: "{value}"` — GATE 2 applies; name-only cells are malformed" AND "**INERTIA-REF-DELTA** (structural): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {C0 mechanism phrase}` — GATE 4 applies; 'N/A' or empty is malformed." The collection-phase framing ("before rule evaluation") is the purest structural statement across all variations. |
| V-04 | **PASS** | Collection phase (Phase 2): "**Anchor column** (structural — OUTPUT CONTRACT, Anchor column value): `Row C{N}, {attribute}: "{value}"` — a cell containing only a competitor name is syntactically malformed." Synthesis phase (Phase 5): "**Anchor column** (structural — OUTPUT CONTRACT, Anchor column value): `Row C{N}, {attribute}: "{value}"` — apply GATE 2; name-only cells are syntactically malformed" AND "**INERTIA-REF-DELTA column** (structural — OUTPUT CONTRACT, INERTIA-REF-DELTA): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}` — apply GATE 4; 'N/A' or empty is malformed." Coercion spans collection-to-synthesis boundary. |
| V-05 | **PASS** | Collection phase (Phase 2): "**Anchor column** (structural — fills Anchor column slot, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"` — cells not conforming to this shape are syntactically malformed; GATE 2 applies before rule evaluation." Synthesis phase (Phase 5): "**Anchor column** (fills Anchor column slot, PREFLIGHT > OUTPUT CONTRACTS): `Row C{N}, {attribute}: "{value}"`" AND "**INERTIA-REF-DELTA column** (fills INERTIA-REF-DELTA slot, PREFLIGHT > OUTPUT CONTRACTS): `vs. INERTIA-REF — {reinforces / challenges / contextualizes}: {specific C0 mechanism phrase}`" — each with NOT ACCEPTABLE examples extending the C-20 constraint. Three independent format templates across two tables — maximum coercion surface area in any R6 variation. |

**C-25: PASS — all five.**

---

### C-26 — Consolidated PREFLIGHT gate block

Pass condition: All mandatory gates consolidated into a single named PREFLIGHT section before Phase 1; each gate must satisfy C-21 (named subsection with PASS/FAIL table); distributing gates across phases does not satisfy even if each satisfies C-21 individually.

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | PREFLIGHT section (before Phase 1) contains: "GATE 1: CITATION GATE" (3-col table, 2 rows), "GATE 2: ANCHOR GATE" (3-col table, 2 rows + NOT ACCEPTABLE examples), "GATE 3: PROOF GATE" (3-col table, 3 rows), "GATE 4: INERTIA-REF GATE" (3-col table, 2 rows). "All gates are defined here. No gate appears outside this block." Four gates, four C-21-compliant subsections, one PREFLIGHT block. |
| V-02 | **PASS** | PREFLIGHT section (before Phase 1) declares: "All gates are defined here before any execution phase. No gate appears outside this block." Contains GATE 1 (2-row table), GATE 2 (2-row table), GATE 3 (3-row table), GATE 4 (2-row table). All four gates in one section, each a named subsection with 3-col PASS/FAIL table. C-24 is satisfied by phase headings; C-26 is satisfied by the PREFLIGHT consolidation. |
| V-03 | **PASS** | PREFLIGHT section contains all gates AND the OUTPUT CONTRACTS subsection — the entire preamble is one block. "Everything needed to execute this skill is defined here." Contains GATE 1 (2-row table), GATE 2 (2-row table + examples), GATE 3 (3-row table), GATE 4 (2-row table), and OUTPUT CONTRACTS (slot table). All four mandatory gates are named subsections with PASS/FAIL tables inside a single PREFLIGHT section. OUTPUT CONTRACTS is also a subsection, making PREFLIGHT auditable as the single entry point. |
| V-04 | **PASS** | PREFLIGHT section: "All gates are defined here. No gate appears outside this block." Contains GATE 1 (2-row table), GATE 2 (2-row table + examples), GATE 3 (3-row table), GATE 4 (2-row table + write-token instruction). OUTPUT CONTRACT follows as a separate section after PREFLIGHT — not a gate. All four mandatory gates are in the PREFLIGHT block. The separation of gates (PREFLIGHT) from output shapes (OUTPUT CONTRACT) is this variation's architectural distinction. |
| V-05 | **PASS** | PREFLIGHT section: "All rules and output shape declarations are defined in this section. No gate appears outside this block." Contains GATE 1 (3-row table), GATE 2 (3-row table + examples), GATE 3 (3-row table), GATE 4 (2-row table + write-token instruction), and OUTPUT CONTRACTS subsection (4-col table). All four mandatory gates are in PREFLIGHT; each is a named subsection with a PASS/FAIL table. OUTPUT CONTRACTS embedded inside PREFLIGHT is the tightest possible front-loading: same location as gates, visible simultaneously. GATE 1 in V-05 adds a third row ("URL is a direct URL") not present in other variations — additional robustness that does not affect gate consolidation. |

**C-26: PASS — all five.**

---

### Per-criterion summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-01** Status quo competitor | PASS | PASS | PASS | PASS | PASS |
| **C-02** Minimum external competitors | PASS | PASS | PASS | PASS | PASS |
| **C-03** Focus dimension support | PASS | PASS | PASS | PASS | PASS |
| **C-04** Whitespace finding present | PASS | PASS | PASS | PASS | PASS |
| **C-05** Findings section present | PASS | PASS | PASS | PASS | PASS |
| **C-06** Inertia stickiness reasoning | PASS | PASS | PASS | PASS | PASS |
| **C-07** Web-verified competitive claim | PASS | PASS | PASS | PASS | PASS |
| **C-08** AMEND — 3 actionable adjustments | PASS | PASS | PASS | PASS | PASS |
| **C-09** Cross-dimensional whitespace | PASS | PASS | PASS | PASS | PASS |
| **C-10** Table-stakes grounding per finding | PASS | PASS | PASS | PASS | PASS |
| **C-11** Fully-cited competitor table | PASS | PASS | PASS | PASS | PASS |
| **C-12** Self-negating cross-dimensional | PASS | PASS | PASS | PASS | PASS |
| **C-13** Claim-level finding anchors | PASS | PASS | PASS | PASS | PASS |
| **C-14** AMEND as proof validator | PASS | PASS | PASS | PASS | PASS |
| **C-15** Inline anchor tag before proof | PASS | PASS | PASS | PASS | PASS |
| **C-16** Gate failure naming | PASS | PASS | PASS | PASS | PASS |
| **C-17** WHITESPACE by attribute absence | PASS | PASS | PASS | PASS | PASS |
| **C-18** NOT ACCEPTABLE anchoring example | PASS | PASS | PASS | PASS | PASS |
| **C-19** Synthesis-first output contracts | PASS | PASS | PASS | PASS | PASS |
| **C-20** Structural column coercion | PASS | PASS | PASS | PASS | PASS |
| **C-21** Gate-as-section PASS/FAIL table | PASS | PASS | PASS | PASS | PASS |
| **C-22** INERTIA-REF per-finding citation | PASS | PASS | PASS | PASS | PASS |
| **C-23** Output contract slot format spec | PASS | PASS | PASS | PASS | PASS |
| **C-24** Phase-to-contract back-references | PASS | PASS | PASS | PASS | PASS |
| **C-25** Cross-table structural coercion | PASS | PASS | PASS | PASS | PASS |
| **C-26** Consolidated PREFLIGHT gate block | PASS | PASS | PASS | PASS | PASS |

---

### Composite scores

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---:|---:|---:|---:|---:|
| Essential (5/5 × 60) | 60 | 60 | 60 | 60 | 60 |
| Recommended (3/3 × 30) | 30 | 30 | 30 | 30 | 30 |
| Aspirational (18/18 × 90) | 90 | 90 | 90 | 90 | 90 |
| **Composite** | **180** | **180** | **180** | **180** | **180** |
| **Grade** | Exceptional | Exceptional | Exceptional | Exceptional | Exceptional |
| **Golden threshold** | YES | YES | YES | YES | YES |

---

### Ranking

All five variations tie at 180/180. This is the expected outcome: the R6 variations were designed specifically to instantiate C-23 through C-26 while preserving the full R5 foundation. The ceiling was reached.

Structural distinction ranking (non-scoring, for rubric progression purposes):

| Rank | Variation | Distinguishing property |
|------|-----------|------------------------|
| 1 | **V-05** | Maximum density: PREFLIGHT contains all 4 gates + 4-col OUTPUT CONTRACTS; three independent coercion templates (competitor Anchor, findings Anchor, findings INERTIA-REF-DELTA); every producing phase uses full-path back-reference "PREFLIGHT > OUTPUT CONTRACTS"; most adversarially robust |
| 2 | **V-03** | Cleanest auditable structure: PREFLIGHT is the only preamble — the collection-phase Anchor coercion phrase "syntactically malformed cells trigger GATE 2 **before rule evaluation**" is the most precise structural coercion framing of any variation |
| 3 | **V-04** | Cleanest separation of concerns: PREFLIGHT = rules; OUTPUT CONTRACT = output shapes; INERTIA-REF as gate-clearing action; bidirectional 4-col tracing |
| 4 | **V-02** | Strongest forward-link architecture: "Filled by phase" column as machine-readable phase-to-slot mapping; INERTIA-REF-DELTA coerced in both tables independently; most readable bidirectional tracing |
| 5 | **V-01** | Simplest design at 180/180: 3-col OUTPUT CONTRACT + INERTIA-REF in GATE 4 + phase headings close C-24; fewer redundant signals than V-04/V-05 |

---

### Excellence signals (R6)

Patterns from R6 that represent genuine structural advances over R5:

**1. INERTIA-REF token written as the act of clearing GATE 4 (V-01, V-04, V-05)**
In R5, INERTIA-REF was defined either in Phase 0 or in an early execution phase. In R6 V-01/V-04/V-05, clearing GATE 4 IS defining the token — the act of satisfying the gate condition is simultaneously the act of establishing the reference frame. This makes the gravitational baseline inseparable from the enforcement architecture: the model cannot reach Phase 1 without having written INERTIA-REF as part of the PREFLIGHT gate-clearing sequence. The reference frame is not a preamble section; it is a gate condition.

**2. 4-column OUTPUT CONTRACT with "Filled by phase" column as machine-readable tracing (V-02, V-04, V-05)**
R5 introduced the OUTPUT CONTRACT table (Slot / Label / Required format). R6 V-02/V-04/V-05 add a fourth column ("Filled by phase") that makes the phase-to-slot assignment structurally declared rather than inferred from prose. Combined with phase headings that back-reference the slot label, the tracing is bidirectional via two table structures (contract column → phase heading → slot label) rather than prose interpretation. An auditor can verify phase-to-slot mapping by reading two cells, not two paragraphs.

**3. OUTPUT CONTRACTS embedded as a subsection inside PREFLIGHT (V-03, V-05)**
R5 placed the output contract as a standalone section after PREFLIGHT. R6 V-03/V-05 embed OUTPUT CONTRACTS as a named subsection of PREFLIGHT, making the entire preamble — all gate definitions AND all output shape declarations — readable from a single section. The practical consequence: a skill auditor verifying C-23, C-24, C-26 simultaneously can do so without leaving PREFLIGHT. The skill is preamble-complete.

**4. Cross-table coercion formalized as a first-class structural requirement (all five)**
R5 had structural column coercion in collection-phase tables (C-20 satisfied) and some variations applied it to findings tables (V-02, V-05 in R5). R6 makes this explicit and universal: every variation independently coerces the Anchor column in the competitor (collection) table AND in the findings (synthesis) table. The coercion templates are declared separately in each table, making them independently checkable format constraints that propagate through the full pipeline without relying on the collection-phase constraint to carry over.

---

### Key interactions — resolved

| Interaction | Resolution |
|---|---|
| V-01 3-col OUTPUT CONTRACT vs. V-02/V-04/V-05 4-col — does column count affect C-23? | No. C-23 requires at least one slot with both label and format template. All 3-col and 4-col tables satisfy this. The 4-col form satisfies additionally by making "Filled by phase" structurally visible, but the scoring criterion is identical. |
| V-03/V-05 OUTPUT CONTRACTS inside PREFLIGHT vs. C-26 gate-only requirement — does the subsection affect C-26? | No. C-26 requires all *gates* consolidated in PREFLIGHT. OUTPUT CONTRACTS is not a gate; it is a contract declaration. Its presence inside PREFLIGHT satisfies C-24/C-23 more tightly but does not affect C-26 compliance for any variation. |
| V-02 GATE 4 without write-token instruction — does deferred token definition (Phase 2) affect C-22? | No. C-22 requires the token to be defined and per-finding citation to be required. V-02 defines the token in Phase 2 and enforces citation via GATE 4 gate-row + INERTIA-REF-DELTA column coercion. Definition location does not affect the C-22 criterion. |
| V-05 GATE 1 with 3 rows (adds "URL is a direct URL" check) vs. others with 2 rows — scoring effect? | None. C-21 requires ≥2 rows; V-05's third row is a higher-specificity constraint that exceeds the minimum. No scoring differential but highest citation gate rigor. |

---

```json
{"top_score": 180, "all_essential_pass": true, "new_patterns": ["INERTIA-REF token written as the act of clearing GATE 4 — the reference frame is established as a gate-clearing action, making it inseparable from the enforcement architecture rather than a separate preamble section", "4-column OUTPUT CONTRACT with Filled-by-phase column creates machine-readable bidirectional phase-to-slot tracing — contract column names the phase, phase heading names the slot, auditable from two cells rather than two paragraphs", "OUTPUT CONTRACTS embedded as a subsection inside PREFLIGHT makes the preamble preamble-complete — all gate definitions and all output shape declarations auditable from a single section", "Cross-table structural coercion formalized as a universal requirement — independent format templates in both the collection-phase competitor table and the synthesis-phase findings table, propagating syntactic rejection of name-only anchoring through the full collection-to-synthesis pipeline"]}
```
