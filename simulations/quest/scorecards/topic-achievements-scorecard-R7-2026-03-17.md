## Quest Score — topic-achievements (Round 7, Rubric v7)

---

### Scoring Basis

All five variations are built on R6 V-05, which passed C-01 through C-21 under v6. Under v7, C-22 and C-23 are added (aspirational, formula updates to `/15`). The key question for each variation is whether the two new criteria are satisfied **fully** vs. structurally/partially.

**Scoring PARTIAL = 0.5 in formula.**

---

### Criterion Reference — New in v7

| Criterion | What it requires | Precondition |
|-----------|-----------------|--------------|
| C-22 | All gate schemas co-located in a single preamble registry before Phase 1, making the full contract discoverable by inspection (no cross-reference to phase instructions required) | C-20 |
| C-23 | Each gate pairs its PASS schema with a FAIL block listing at least one specific output form that does not clear the gate | C-20 |

---

### V-01 — Registry Full-Schema Expansion

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Template enforces single-state invariant (Invariant A) per row; pre-printed cell structure enforces one choice |
| C-02 | PASS | Falsified row pre-printed; Invariant B names floor; framing preserved from baseline |
| C-03 | PASS | Invariant C requires filename + date for EARNED; `n of m` for IN-PROGRESS; CLASSIFY GATE drives artifact-grounded classification |
| C-04 | PASS | "No qualitative-only descriptions" explicit in Phase 3 fill rules |
| C-05 | PASS | Next Action template requires `/[SKILL]`, artifact name, CATEGORY: ACHIEVEMENT, and a gap sentence |
| C-06 | PASS | All 7 category lines required in CLASSIFY GATE; missing line is a FAIL condition |
| C-07 | PASS | Invariant C requires `filename — date` for EARNED entries |
| C-08 | PASS | YAML frontmatter includes `earned:`, `in_progress:`, `locked:` count fields; STATE GATE outputs numeric counts |
| C-09–C-21 | 13× PASS | R6 V-05 baseline preserved — session invariants A–D, pre-printed Falsified/LOCKED cells, CLASSIFY before STATE, all 4 phases gated, FAIL conditions per gate, etc. |
| C-22 | **PASS** | Registry contains complete multi-line schemas for all 4 gates before Phase 1. Per-phase prefaces reference back ("schema declared in registry above") rather than re-stating independently. The registry IS self-sufficient for inspection — no cross-reference to phase instructions needed. Full contract discoverable from registry alone. |
| C-23 | **PASS** | FAIL blocks present per phase with specific output forms (preserved from R6 V-05). SCAN GATE has 4 named failure modes; CLASSIFY GATE has 5. PASS + at least one FAIL mode per gate: criterion met. |

**Aspirational: 15/15**

```
composite = (5/5 × 60) + (3/3 × 30) + (15/15 × 10) = 60 + 30 + 10 = 100
```

**Score: 100 — Platinum**

---

### V-02 — Registry Primacy Declaration

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-05 | 5× PASS | R6 baseline preserved |
| C-06–C-08 | 3× PASS | R6 baseline preserved |
| C-09–C-21 | 13× PASS | R6 baseline preserved |
| C-22 | **PARTIAL** | REGISTRY PRIMACY declaration added — the registry is contractually authoritative (a gate output matching the registry clears the gate regardless of phase-level elaboration). However, the registry is a pipe-delimited table with all schemas compressed inline (e.g., the CLASSIFY row is a single table cell). The variate basis explicitly identifies this as the R6 V-05 limitation: "abbreviated schemas that require cross-referencing per-phase text to be fully understood may not fully satisfy" C-22. Primacy makes co-location contractually binding but does not make abbreviated schemas self-sufficient for inspection. A reader cannot reconstruct the full CLASSIFY schema from the table cell without parsing. C-22's discoverability property is improved (binding) but not fully met (still requires mental unpacking of compressed notation). |
| C-23 | **PASS** | FAIL blocks per phase inherited from R6 V-05 (flat lists, 3–5 specific failure modes per gate). Per-gate FAIL note now carries "(authority: registry primacy)" label. PASS + specific FAIL modes per gate: criterion met. |

**Aspirational: 13 + 0.5 + 1 = 14.5/15**

```
composite = (5/5 × 60) + (3/3 × 30) + (14.5/15 × 10) = 60 + 30 + 9.67 ≈ 99.7
```

**Score: 99 — Gold**

---

### V-03 — Severity-Stratified FAIL Blocks

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-05 | 5× PASS | R6 baseline preserved |
| C-06–C-08 | 3× PASS | R6 baseline preserved |
| C-09–C-21 | 13× PASS | R6 baseline preserved |
| C-22 | **PARTIAL** | Registry format from R6 V-05 preserved — abbreviated table rows. No full-schema expansion, no primacy declaration. The registry satisfies C-22 structurally (all schemas co-located before Phase 1) but not fully (schemas are compressed; full schema for CLASSIFY requires reading the pipe-delimited cell carefully or cross-referencing per-phase prefaces). Same C-22 status as R6 V-05 baseline under v7 assessment. |
| C-23 | **PASS** | Severity-stratified FAIL blocks per gate: Tier 1 (structural — label absent), Tier 2 (completeness — fields missing), Tier 3 (semantic bypass — fields present but intent bypassed). Tier 3 is explicitly labeled as the most consequential. SCAN GATE Tier 3: floor stated "inactive" when prove artifacts exist. CLASSIFY GATE Tier 3: count without 7 labeled lines; state assignments embedded; silent omission. STATE GATE Tier 3: counts don't sum to 7. WRITE GATE Tier 3: wrong topic or date in path. C-23 is satisfied at maximum depth — this is the strongest C-23 expression in R7. |

**Aspirational: 13 + 0.5 + 1 = 14.5/15**

```
composite = (5/5 × 60) + (3/3 × 30) + (14.5/15 × 10) = 60 + 30 + 9.67 ≈ 99.7
```

**Score: 99 — Gold**

---

### V-04 — Full-Schema Registry + Primacy

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-05 | 5× PASS | R6 baseline preserved |
| C-06–C-08 | 3× PASS | R6 baseline preserved |
| C-09–C-21 | 13× PASS | R6 baseline preserved |
| C-22 | **PASS** | Full-schema expansion (V-01 axis) + REGISTRY PRIMACY (V-02 axis) combined. Registry contains complete multi-line schemas for all 4 gates, each as a named block with "— complete schema:" label. REGISTRY PRIMACY states: "These schemas are the sole authoritative gate contracts. Phase instructions implement these contracts; they do not redefine them." Per-phase prefaces are labeled "preface — restatement of registry authority; read before executing." C-22 met at two levels: (1) complete schemas — the registry is self-sufficient for inspection; (2) contractual authority — the registry is the binding source, not a parallel reference. This is the strongest structural satisfaction of C-22. |
| C-23 | **PASS** | FAIL blocks per phase preserved from R6 V-05 (flat lists). Not severity-stratified — the semantic bypass tier is not named explicitly. C-23 basic criterion met (PASS + specific FAIL modes per gate). |

**Aspirational: 15/15**

```
composite = (5/5 × 60) + (3/3 × 30) + (15/15 × 10) = 60 + 30 + 10 = 100
```

**Score: 100 — Platinum**

---

### V-05 — Golden Synthesis

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-05 | 5× PASS | R6 baseline preserved |
| C-06–C-08 | 3× PASS | R6 baseline preserved |
| C-09–C-21 | 13× PASS | R6 baseline preserved |
| C-22 | **PASS** | Full-schema expansion + REGISTRY PRIMACY ("The schemas below are the sole authoritative gate contracts... regardless of any phase-level elaboration. Retain these schemas throughout all phases.") + three-layer role differentiation: registry as contract, per-phase as labeled restatement, FAIL blocks as stratified enforcement. C-22 covered at three levels: complete (full schemas, self-sufficient), co-located (single preamble registry), authoritative (binding primacy declared). |
| C-23 | **PASS** | Severity-stratified FAIL blocks per gate (V-03 axis) combined with registry primacy. Tier 3 (semantic bypass) explicitly named per gate — SCAN GATE: floor stated inactive when prove artifacts exist; CLASSIFY GATE: count without enumeration, state assignments contaminating classify output, silent omission; STATE GATE: non-7 sum; WRITE GATE: wrong topic/date paths structurally valid but semantically incorrect. Additionally, Phase 3 fill instructions now carry inline criterion cross-references: "A date-less EARNED entry fails C-07" and "Qualitative-only text without numbers fails C-04." C-23 met at maximum depth. |

**Aspirational: 15/15**

```
composite = (5/5 × 60) + (3/3 × 30) + (15/15 × 10) = 60 + 30 + 10 = 100
```

**Score: 100 — Platinum**

---

### Summary Table

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Composite | Grade |
|-----------|---------------|-----------------|-------------------|-----------|-------|
| V-01 Registry Full-Schema | 60 | 30 | 10.00 | **100** | Platinum |
| V-02 Registry Primacy | 60 | 30 | 9.67 | **99** | Gold |
| V-03 Severity-Stratified FAIL | 60 | 30 | 9.67 | **99** | Gold |
| V-04 Full-Schema + Primacy | 60 | 30 | 10.00 | **100** | Platinum |
| V-05 Golden Synthesis | 60 | 30 | 10.00 | **100** | Platinum |

**Rank**: V-05 > V-04 > V-01 > V-02 = V-03 *(qualitative depth within same scores)*

---

### Excellence Signals — V-05

**Signal 1: Inline criterion enforcement in fill rules**

V-05 Phase 3 fill instructions add: *"A date-less EARNED entry fails C-07"* and *"Qualitative-only text without numbers fails C-04."* No prior variation — not V-01, V-02, V-03, or V-04 — names the specific scored criterion a fill error violates. This closes the gap between a model that fills placeholders mechanically and one that understands the scored consequence of each fill choice. The pattern: **name the criterion number at the point of instruction**, not just in the gate FAIL block downstream.

**Signal 2: Severity-stratified FAIL blocks with Tier 3 as explicit named class**

V-03 and V-05 both introduce stratified tiers. The key property is not just having three tiers — it is that Tier 3 (semantic bypass) is **explicitly labeled as a distinct failure class** with a definition: "fields present but intent bypassed." Without this label, a flat FAIL list forces the model to infer which failure modes are structural vs. intentional. The stratification makes the semantic bypass case as visible as the missing-label case, even though it is harder to detect. In V-05, this pairs with registry primacy: Tier 3 failures now have a named authority they violate.

---

### New Patterns Identified

1. **Inline criterion enforcement** — naming the specific criterion number (`fails C-07`, `fails C-04`) inline in template fill instructions, at the point of execution rather than only in gate FAIL blocks.
2. **Severity-stratified FAIL taxonomy with Tier 3 semantic-bypass explicitly named** — restructuring FAIL blocks into Tier 1 (structural) / Tier 2 (completeness) / Tier 3 (semantic bypass) so the hardest-to-detect failure mode is explicitly classified rather than buried in a flat list.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Inline criterion enforcement in template fill rules — naming the specific criterion number (e.g., 'fails C-07') at the point of instruction, so fill errors are tied to scored consequences rather than discovered only at gate evaluation", "Severity-stratified FAIL taxonomy with Tier 3 semantic-bypass explicitly named as a distinct class per gate — making the hardest failure mode (fields present but intent bypassed) as visible as structural failures in the FAIL block"]}
```
