Written to `simulations/quest/golden/flow-ratelimit-variate-R1-2026-03-17.md`.

---

# flow-ratelimit — Variate R1

Five complete, runnable skill body prompt variations for `flow-ratelimit`.

---

## V-01 — Table-Dominant Format

**Axis:** Output format
**Hypothesis:** Enforcing a named table schema for every section forces numeric specificity (C-07) and structured volume-to-behavior mapping (C-08). Column names act as type constraints — you cannot fill a `Limit (req/min)` cell with "limited throughput" the way you can in prose.

**Structure:** Six tables in strict order: Throttle Tier Registry → Binding Order → Backpressure Propagation → UX Per Tier → Burst Paths + Retry-After Gaps → Volume-to-Behavior Summary. Each table has violation-type rules embedded in the column definitions (e.g., `Limit` = number required; `Mechanism` = named-set-only; `Error code` = specific identifier). Closes with a free-form Mitigation Section that requires named parameters.

**Rubric coverage design:**
- C-01: TABLE 2 binding-order column requires causal reason, not just tier ID
- C-02: TABLE 3 mechanism column enforces named-set; hop minimum = 2
- C-03: TABLE 4 requires ≥2 tiers and specific error codes
- C-04: TABLE 5A requires structural-absence language, not just high-headroom
- C-05: TABLE 5B requires PASS/FAIL per caller with failure mode for FAIL
- C-06: TABLE 6 `Cascading effect` column requires second-tier causation
- C-07: TABLE 1 `Limit` column rejects vague labels at the schema level
- C-08: TABLE 6 is the explicit volume-to-behavior mapping
- C-09: Mitigation section requires named parameter per gap
- C-10: Mitigation section has arithmetic requirement anchored to TABLE 1 limits

---

## V-02 — Three Named Analyst Roles

**Axis:** Role sequence
**Hypothesis:** Separating the throttle-inventory analyst (Role A), the UX/backpressure analyst (Role B), and the gap analyst (Role C) into distinct named roles with explicit handoffs prevents early-role work from crowding out later-role work. Each role owns exactly the rubric criteria it is best positioned to produce.

**Structure:** Role A → ROLE A COMPLETE → Role B → ROLE B COMPLETE → Role C → ROLE C COMPLETE. No role activates without the prior handoff. Role C has the heaviest lifting: unprotected burst paths, Retry-After assessment, quantified spike (arithmetic), and per-gap mitigation.

**Rubric coverage design:**
- C-01, C-07: Role A owns tier inventory with numeric limits and causal binding order
- C-02, C-03, C-06: Role B owns backpressure chain, UX per tier, and cascade scenario
- C-04, C-05: Role C owns structural gap identification with explicit absence language
- C-09: Role C mitigation step requires named parameter
- C-10: Role C quantified-spike step requires arithmetic derivation from Role A limits

**Key difference from V-01:** The handoff mechanism enforces sequential completeness rather than table-column constraints. A model that skips Role B's cascade scenario cannot satisfy Role C's cascade confirmation.

---

## V-03 — Conversational Imperative

**Axis:** Phrasing register
**Hypothesis:** Shorter, direct commands with minimal scaffolding reduce model distraction. When the prompt stops explaining itself and just tells the model what to do, the model spends more tokens on analysis. This may improve causal reasoning quality (C-01, C-02) at some cost to structural guarantees.

**Structure:** Ten numbered imperative commands. No formal role names. No gate language. No handoff signals. Each command is 1–3 sentences. The model receives its instructions at a conversational register: "Walk through it," "Follow the pressure," "Find the unprotected paths."

**Rubric coverage design:**
- C-01: Step 2 ("Find the first bottleneck") requires causal explanation
- C-02: Step 3 ("Follow the pressure") requires named mechanisms and ≥2 hops
- C-03: Step 4 requires specific error codes and ≥2 tiers
- C-04: Step 5 explicitly filters out high-headroom paths
- C-05: Step 6 requires header-level evaluation and named failure mode
- C-06: Step 8 ("Name the cascade") requires causation, not coincidence
- C-07: Step 1 requires "number + unit — not 'limited', not 'throttled'"
- C-08: Step 7 is an explicit load table with one row per volume band
- C-09: Step 9 requires named parameter per gap
- C-10: Step 10 requires arithmetic with derivation steps

**Key difference from V-01/V-02:** Zero structural enforcement machinery. The hypothesis is that the analysis quality is in the question, not the scaffolding. The risk is that without table schemas or handoffs, the model defaults to prose for C-07/C-08.

---

## V-04 — Finding-First / Inverted Structure

**Axis:** Lifecycle emphasis
**Hypothesis:** Leading with the verdict block forces the model to commit to a stance before assembling evidence. This inverted structure produces cleaner C-01 binding-constraint naming (the model must state it as a claim, then defend it) and more explicit C-04/C-05 gap identification (gaps are declared upfront, not discovered incidentally during analysis). The risk is that an underpowered verdict block becomes a self-fulfilling evidence search.

**Structure:** Section 1 (Verdict Block — 5 fields to fill before any analysis) → Section 2 (Evidence subsections 2.1–2.6) → Section 3 (Volume-to-Behavior Table) → Section 4 (Mitigation Table with named-parameter column) → Section 5 (Quantified Spike with derivation requirement).

**Rubric coverage design:**
- C-01: VERDICT 1.1 names the binding constraint; 2.1 provides causal evidence
- C-02: Section 2.2 requires named mechanisms and ≥2 hops
- C-03: Section 2.3 requires specific error codes and ≥2 tiers, tied to VERDICT 1.3
- C-04: Section 2.4 requires structural-absence language
- C-05: Section 2.5 requires PASS/FAIL with failure mode for FAIL rows
- C-06: Section 2.6 cascade evidence confirms or revises VERDICT 1.5
- C-07: Section 2.1 tier inventory requires number + unit
- C-08: Section 3 is the explicit volume-to-behavior table
- C-09: Section 4 Mitigation Table has a named-parameter column that rejects generic advice
- C-10: Section 5 requires arithmetic derivation from 2.1 limits

**Key difference from V-01–V-03:** The verdict block creates a commitment that the evidence must resolve. If the model commits to "T-01 is the binding constraint at 1x" in VERDICT 1.1, the 2.1 evidence section must produce the causal argument. This surfaces inconsistencies earlier than a purely forward structure.

---

## V-05 — Inertia-Framed + Multi-Role + Mixed Format (Combination)

**Axes:** Role sequence + inertia framing + output format
**Hypothesis:** Framing the status-quo ("do nothing") as a named inertia baseline before analysis primes the model to treat every finding as a gap from baseline rather than a neutral observation. The inertia baseline concept (borrowed from `/scout-competitors`) should sharpen C-04 (burst paths are gaps from baseline, not accidents) and C-05 (Retry-After handling is a binary: you either improved from baseline or you didn't). Combined with a three-role chain (Throttle Analyst → Backpressure/UX Analyst → Gap Analyst) and a TABLE A with named-set failure modes.

**Structure:** Inertia Baseline prose (written before roles activate) → Role 1 (TABLE A + binding order) → ROLE 1 COMPLETE → Role 2 (backpressure chain, UX, cascade) → ROLE 2 COMPLETE → Role 3 (gap analysis with inertia framing, Retry-After, quantified spike) → ROLE 3 COMPLETE → Synthesis Table (inertia vs. protected comparison) → Mitigation Table (with `Improvement over inertia` column).

**Rubric coverage design:**
- C-01: Role 1 requires causal binding-order reasoning
- C-02: Role 2 Part A requires named mechanisms and ≥2 hops
- C-03: Role 2 Part B requires specific error codes and ≥2 tiers
- C-04: Role 3 Gap 1 filters high-headroom paths; inertia framing asks "is this gap structural or incidental?"
- C-05: Role 3 Gap 2 requires PASS/FAIL with failure mode; inertia framing asks "does the baseline handle this by default?"
- C-06: Role 2 Part C requires causation, not coincidence; explicitly distinguishes cascade from coincident throttling
- C-07: TABLE A rejects vague labels at the schema level
- C-08: Synthesis Table rows cover 1x/2x/5x with inertia vs. protected comparison
- C-09: Mitigation Table requires named parameter; rejects category descriptions
- C-10: Role 3 Gap 3 requires arithmetic with derivation from TABLE A limits; compares to inertia-baseline behavior

**Key difference from V-01–V-04:** The inertia framing adds a dimension no other variation has — every finding must be categorized as "expected baseline behavior" or "unexpected gap even from baseline." This primes sharper C-04 language and produces the Synthesis Table's `Delta` column, which is a unique structural answer to C-08 that no other variation generates.

---

## Variation Comparison

| Axis varied | V-01 | V-02 | V-03 | V-04 | V-05 |
|-------------|------|------|------|------|------|
| Output format | Table-dominant | Mixed table+narrative | Prose imperative | Mixed (verdict+tables) | Mixed with inertia columns |
| Role structure | None | 3 named roles + handoffs | None | None | 3 named roles + handoffs |
| Lifecycle order | Forward | Forward with gates | Forward | Inverted (verdict-first) | Forward with inertia pre-step |
| Inertia framing | Absent | Absent | Absent | Absent | Explicit baseline section |
| Phrasing register | Formal/technical | Formal with role framing | Conversational imperative | Formal | Formal with inertia framing |

**Predicted strengths by criterion:**
- C-07 (numeric limits): V-01 > V-05 > V-04 > V-02 > V-03 (table schemas force precision; imperative may drift)
- C-01 (binding order causation): V-04 > V-02 > V-05 > V-01 > V-03 (commitment before evidence vs. schema enforcement)
- C-04 (unprotected burst paths): V-05 > V-03 > V-04 > V-02 > V-01 (inertia framing sharpens structural-absence language)
- C-10 (quantified spike): V-02 > V-04 > V-05 > V-01 > V-03 (role with dedicated arithmetic step vs. tacked-on mitigation section)
