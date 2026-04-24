---

# Variate R4 — topic-achievements

**Basis**: R3 V-04 (Platinum) and V-05 (Platinum) under v3. Under v4 rubric, V-05 still passes C-16+C-17; V-04 fails C-16 (rule-stated, not pre-printed). Two new excellence signals from R3 scorecard: floor sentence must stand structurally independent, state counts in frontmatter.

---

## Variation Axes

| Axis | Single-axis | Combination |
|------|-------------|-------------|
| Phrasing register (floor as session-level preamble invariant) | V-01 | V-04, V-05 |
| Output format (pre-printed compliance block in instruction body) | V-02 | V-04, V-05 |
| Lifecycle emphasis (SCAN GATE carries floor as numbered phase invariant) | V-03 | V-05 |

---

## V-01 — Phrasing Register: Floor as Session-Level Preamble Invariant

**Axis**: Phrasing register
**Hypothesis**: Declaring the floor at the top of the prompt as "Session invariant 2: Namespace-level evidence from the prove namespace is always acceptable and is the safe floor" — before any scan, classification, or Falsified contract — eliminates C-17 by position. The governing label is "Session invariants:" (neutral), not a conditional trigger phrase. No Falsified-specific section can contaminate the floor because the floor precedes all classification work. C-16 not targeted (requirements remain rule-stated); CLASSIFY step before STATE enforces C-09.

The prompt opens with three numbered session invariants, then proceeds: Step 1 Scan → Step 2 Classify → Step 3 Assign States → Step 4 Achievement Table → Step 5 Next Action → Step 6 Write. The Falsified contract is a three-rule numbered block (Earn / Describe / Apply floor). "Apply floor" references Session invariant 2 by number — the floor sentence appears once, at preamble level, unconditionally.

---

## V-02 — Output Format: Pre-Printed Verbatim Compliance Block in Instruction Body

**Axis**: Output format
**Hypothesis**: Pre-printing the entire Falsified compliance block — consequence clause, evasion surface, and floor declaration — as a labeled verbatim callout in the instruction body achieves C-16 via a different structural mechanism than V-05's table cell. The block is labeled "FALSIFIED ACHIEVEMENT CONTRACT — PRE-PRINTED" (neutral heading), and the floor appears as Rule 3 without any conditional governing label. C-17 is achieved because Rule 3 stands inside a neutral-labeled block, not under "Fallback for uncertain evidence:" or equivalent. CLASSIFY phase runs before STATE (C-09). Model is explicitly told not to rewrite the block.

The prompt structure: Step 1 Scan → Step 2 Falsified Compliance Block (pre-printed, output verbatim) → Step 3 Classify → Step 4 Assign States and Build Table → Step 5 Next Action → Step 6 Write.

---

## V-03 — Lifecycle Emphasis: SCAN GATE Carries Floor as Numbered Phase Invariant

**Axis**: Lifecycle emphasis
**Hypothesis**: Elevating the floor to a SCAN GATE output — declared as "Phase invariant 2: Namespace-level evidence from the prove namespace is always acceptable and is the safe floor" — structurally separates the floor from the Falsified contract. The governing label is "SCAN GATE" (neutral phase marker). The floor precedes and is independent of all achievement-specific sections. C-17 is achieved by architectural position: no Falsified label can govern a rule declared at gate level, before classification begins. Phase structure: SCAN GATE → CLASSIFY GATE → STATE GATE (with Falsified rules as three numbered items, no conditional subheading) → RECOMMEND + WRITE.

---

## V-04 — Role Sequence + Output Format: Pre-Printed Block in Classifier Role

**Axes**: Role sequence (Analyst → Classifier) + output format (pre-printed compliance block in Role 2)
**Hypothesis**: R3 V-04 achieved Platinum under v3 but fails C-16 under v4 (Falsified contract is rule-stated). V-04 R4 adds a pre-printed "FALSIFIED CONTRACT — PRE-PRINTED" block to Role 2 with a neutral heading. Role 1 (Artifact Analyst) produces the evidence record. Role 2 (Achievement Classifier) carries the pre-printed block as its first element; the floor appears as Rule 3 inside the block, neutral-labeled. C-16 via pre-printing. C-17 via neutral block heading. C-09 via structural role separation (Role 2 cannot re-scan). Frontmatter carries state counts.

---

## V-05 — Golden Synthesis: Pre-Printed Skeleton + Preamble Invariant + SCAN GATE Invariant

**Axes**: Output format (pre-printed table skeleton) + phrasing register (floor as preamble invariant) + lifecycle emphasis (SCAN GATE repeats floor as phase invariant)
**Hypothesis**: Three-layer C-17 guarantee:
1. Floor declared as "Session invariant B" in the prompt preamble (neutral label, no conditional)
2. SCAN GATE outputs "Floor confirmed (Invariant B): ..." — phase marker label, no conditional
3. Floor pre-printed verbatim in the Falsified table cell — no governing section label

C-16 guaranteed by the pre-printed table skeleton: consequence clause, evasion surface ("including as a closing reflection"), and floor declaration are all pre-printed in the Falsified LOCKED cell. Model fills `[PLACEHOLDER]` fields only. CLASSIFY GATE before FILL TEMPLATE enforces C-09. STATE GATE outputs counts that are also written to frontmatter `earned:` / `in_progress:` / `locked:` fields (Signal 2 from R3 scorecard).

---

**C-16/C-17 coverage map:**

| Variation | C-16 | C-17 mechanism |
|-----------|------|----------------|
| V-01 | FAIL (rule-stated) | Preamble invariant position (neutral label) |
| V-02 | PASS (instruction-body block) | Neutral block heading "FALSIFIED CONTRACT — PRE-PRINTED" |
| V-03 | FAIL (rule-stated) | SCAN GATE invariant position (neutral phase marker) |
| V-04 | PASS (block in Role 2) | Neutral block heading in Classifier role |
| V-05 | PASS (table skeleton) | Three-layer: preamble + SCAN GATE + pre-printed cell |

**Written to**: `simulations/quest/golden/topic-achievements-variate-R4-2026-03-17.md`
