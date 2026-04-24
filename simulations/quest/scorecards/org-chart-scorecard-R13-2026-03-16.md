# org-chart Quest Score — Round 13

**Rubric:** v13 (250 pts · Golden = 200/250 = 80%)
**Variations:** V-01 through V-05
**Date:** 2026-03-16

---

## Scoring Approach

All five variations are incremental on R12-V-05, which achieves full coverage of C-01 through C-38 (240 pts under v12). Under v13, two new positional criteria are added:

- **C-39** (5 pts): STRUCTURING-COST FRAME must carry an explicit positional constraint instruction: pre-mechanism-table placement declared, prohibited form named (post-mechanism placement as cost-summary derived from rows already written), and causal explanation provided (interpretive premise vs. derived conclusion).
- **C-40** (5 pts): GATE CHAIN block must be explicitly declared as a pre-GATE 0 preamble (forward-declaring contract), name the prohibited form (post-GATE 3 retrospective record), and instruct the model to read the block before GATE 0 begins.

C-01 through C-38 are bulk-evaluated from the R12-V-05 baseline. C-39 and C-40 are evaluated per-variation.

---

## Essential Criteria (C-01 to C-05) — All Variations: PASS (60/60)

**C-01** — V-01 text confirms DEFAULT POSITION statement, GATE 1 inertia structure (4 sub-sections declared), mechanism table with closed-set Types, FLAT-CASE-PRESSURE from closed set, VERDICT with re-assessment trigger, all appearing before any org diagram. PASS all variations.

**C-02** — Step 0.1 ROLES-LOADED block present; DO NOT constraint prohibits role names introduced downstream that were not declared here. PASS all variations.

**C-03** — ASCII org diagram with ≥2 hierarchy levels, committees as distinct nodes, role names from roles block. Inherited from R12-V-05. PASS all variations.

**C-04** — Operating rhythm table with ≥3 distinct rows (ROB + shiproom/gate + governance). Inherited. PASS all variations.

**C-05** — Committee charters with all 5 fields; Quorum in `N of M member roles` form; Escalates names destination; Membership ≥2 annotated roles. Inherited. PASS all variations.

---

## Recommended Criteria (C-06 to C-08) — All Variations: PASS (30/30)

**C-06** — Headcount by area, split Decides/Escalates columns, ≥2 areas + Total row, Key Roles annotated with `(domain type)`. Inherited. PASS all variations.

**C-07** — All 4 gate lines present in correct sequence; no section precedes its gate. V-01 text confirms GATE 0 → GATE 1 → GATE 2 → GATE 3 strict sequencing. PASS all variations.

**C-08** — ROLE-TYPE-CLASSIFICATION immediately after roles; all roles typed from closed set; three-tier order. Step 0.2 in V-01 text confirms this structure. PASS all variations.

---

## Aspirational Criteria (C-09 to C-40)

### C-09 through C-32 — All Variations: PASS (120/120)

Inherited verbatim from R12-V-05. No variation touches these axes. Bulk PASS. Notable confirmations in V-01 text:
- **C-13** (DEFAULT-POSITION opening): "DEFAULT POSITION: THE TEAM CAN OPERATE FLAT." opens the skill. PASS.
- **C-25** (GATE CHAIN CONTRACT block): GATE CHAIN CONTRACT section present in V-01 text with MUST sequence language. PASS.
- **C-29** (per-gate checkpoint structure): CHECKPOINT-0 confirmed in V-01 text before GATE 0 STATUS. PASS.

### C-33 through C-36 — All Variations: PASS (20/20)

v11/v12 additions, all inherited from R12-V-05:
- **C-33** GATE 3 field-format verification (Quorum + Membership TYPE per charter). PASS.
- **C-34** Cross-gate role continuity assertion in GATE 3 checkpoint. PASS.
- **C-35** Per-charter iteration structure (CHARTER-FORMAT-AUDIT loop). PASS.
- **C-36** Per-charter role continuity within the loop. PASS.

### C-37 and C-38 — All Variations: PASS (10/10)

- **C-37** (STRUCTURING-COST FRAME presence and content as named block): R12-V-05 has STRUCTURING-COST FRAME physically placed before Step 1.0 via "[Zone: before Step 1.0]" label. Presence and content requirements met. PASS all variations.
- **C-38** (GATE CHAIN consolidated block, all 4 transitions named): ARTIFACT-HANDOFF INVENTORY in V-01 text covers all four gate transitions (GATE 0→1, 1→2, 2→3, 3→STATUS) with named artifacts and producing/consuming steps. PASS all variations.

---

### C-39 — STRUCTURING-COST FRAME pre-mechanism table position (5 pts)

**Requirement:** Explicit positional constraint instruction stating pre-mechanism-table placement; DO NOT guard preventing mechanism rows before frame completion; mechanism table (Step 1.1) named as positional boundary; prohibited form named (post-mechanism as cost-summary derived from rows already written); causal explanation (interpretive premise vs. derived conclusion).

| V | Score | Evidence |
|---|-------|---------|
| **V-01** | FAIL (0/5) | "[Zone: before Step 1.0]" label physically positions frame but provides no explicit positional constraint instruction, no named positional boundary (Step 1.1 not referenced), no DO NOT guard, no prohibited-form statement, no causal explanation. C-37 satisfied; C-39 absent. |
| **V-02** | FAIL (0/5) | V-02 axis is C-40 only. No C-39 modifications. Identical to V-01 on this criterion. |
| **V-03** | PASS (5/5) | V-03 axis adds: explicit DO NOT guard ("DO NOT write any mechanism row before STRUCTURING-COST FRAME is complete"); Step 1.1 named as positional boundary; prohibited form stated ("post-mechanism placement produces the frame as a cost-summary derived from rows already written"); causal explanation ("the frame establishes overhead categories as the interpretive lens through which each mechanism row is read — it must precede the table to function as premise, not conclusion"). All C-39 conditions met. |
| **V-04** | PASS (5/5) | Inherits C-39 axis from V-03. Same evidence. |
| **V-05** | PASS (5/5) | Inherits C-39 from V-04. CHECKPOINT-INERTIA adds explicit FAIL condition: "STRUCTURING-COST FRAME must precede mechanism table rows in output produced; FAIL if any mechanism row appears before frame block is closed." Adds enforcement layer; C-39 already satisfied by V-04 declaration. |

---

### C-40 — GATE CHAIN block pre-GATE 0 preamble position (5 pts)

**Requirement:** ARTIFACT-HANDOFF INVENTORY explicitly declared as preamble to be read before GATE 0 begins; forward-declaring contract framing (model consults dependency graph before executing any gate); prohibited form named (post-GATE 3 retrospective record); causal explanation (forward-declaring contract vs. retrospective record encountered too late to govern).

| V | Score | Evidence |
|---|-------|---------|
| **V-01** | FAIL (0/5) | ARTIFACT-HANDOFF INVENTORY physically precedes GATE 0 within GATE CHAIN CONTRACT block. No preamble declaration. No prospective reading instruction ("read before GATE 0"). No prohibited-form statement (post-GATE 3 retrospective). No causal explanation. C-38 satisfied; C-40 absent. |
| **V-02** | PASS (5/5) | V-02 axis adds: explicit header "PREAMBLE — consult before GATE 0 begins"; forward-declaring contract framing ("a model executing this skill reads the full artifact dependency graph before any gate begins"); prohibited form stated ("post-GATE 3 placement produces a retrospective record encountered after all gates complete, unreachable as a decision-making reference before execution"); causal explanation. All C-40 conditions met. |
| **V-03** | FAIL (0/5) | V-03 axis is C-39 only. No C-40 modifications. Identical to V-01 on this criterion. |
| **V-04** | PASS (5/5) | Inherits C-40 axis from V-02. Same evidence. |
| **V-05** | PASS (5/5) | Inherits C-40 from V-04. CHECKPOINT-0 adds explicit FAIL condition: "ARTIFACT-HANDOFF INVENTORY must have been read as preamble before GATE 0 execution; FAIL if INVENTORY was not consulted prior to GATE 0 content." Adds enforcement layer; C-40 already satisfied by V-04 declaration. |

---

## Composite Scores

| V | Essential (60) | Recommended (30) | C-09–C-38 (150) | C-39 (5) | C-40 (5) | **Total (250)** | **%** |
|---|---------------|-----------------|-----------------|----------|----------|----------------|-------|
| V-01 | 60 | 30 | 150 | 0 | 0 | **240** | 96.0% |
| V-02 | 60 | 30 | 150 | 0 | 5 | **245** | 98.0% |
| V-03 | 60 | 30 | 150 | 5 | 0 | **245** | 98.0% |
| V-04 | 60 | 30 | 150 | 5 | 5 | **250** | 100% |
| V-05 | 60 | 30 | 150 | 5 | 5 | **250** | 100% |

All variations clear the Golden threshold (200/250). All variations pass all 5 essential criteria.

---

## Ranking

| Rank | V | Score | Notes |
|------|---|-------|-------|
| 1 | **V-04** | 250/250 (100%) | Both positional constraints; minimum sufficient form |
| 1 | **V-05** | 250/250 (100%) | V-04 + checkpoint enforcement guards; dual-layer |
| 3 | **V-02** | 245/250 (98%) | C-40 only; C-39 absent |
| 3 | **V-03** | 245/250 (98%) | C-39 only; C-40 absent |
| 5 | **V-01** | 240/250 (96%) | R13 control; R12 ceiling |

---

## Hypothesis Validation

| V | Predicted | Actual | Match |
|---|-----------|--------|-------|
| V-01 | 240/250 | 240/250 | yes |
| V-02 | 245/250 | 245/250 | yes |
| V-03 | 245/250 | 245/250 | yes |
| V-04 | 250/250 | 250/250 | yes |
| V-05 | 250/250 | 250/250 | yes |

All five hypotheses confirmed. Single-axis isolation (V-02, V-03) validates structural independence: C-39 and C-40 can each be satisfied without the other. The 5-pt increment per axis is clean.

---

## Excellence Signals

### E-01 — Dual-layer positional enforcement: declaration + checkpoint verification

V-05 introduces checkpoint-level enforcement of the positional constraints declared by C-39 and C-40. CHECKPOINT-INERTIA carries a FAIL condition verifying that the STRUCTURING-COST FRAME precedes the mechanism table in the output produced. CHECKPOINT-0 carries a FAIL condition verifying that ARTIFACT-HANDOFF INVENTORY was consulted as preamble before GATE 0 execution.

This creates a two-layer constraint:
- **Declaration layer** (prospective): DO NOT guard in the instruction prevents the prohibited form before execution.
- **Checkpoint layer** (retrospective): blocking FAIL condition detects the prohibited form in output before STATUS emits.

A model satisfying V-04's declaration alone can still produce a non-conforming output if the declaration is not followed. V-05's checkpoint FAIL conditions make the non-conforming form gate-blocking: STATUS cannot emit until the checkpoint passes. This is the same enforcement architecture used in C-29 (per-gate checkpoints) generalized to positional constraints within gates.

**Candidate v14 criterion:** CHECKPOINT-INERTIA position-enforcement item — the GATE 1 checkpoint includes an explicit FAIL condition verifying that STRUCTURING-COST FRAME precedes the first mechanism table row in the produced output; the condition names the prohibited observable form (mechanism rows above or before the frame block).

### E-02 — Prohibited-form naming with causal consequence closes the interpretive gap

Both C-39 and C-40 are satisfied not by asserting a position constraint alone but by naming the prohibited form's causal consequence: post-mechanism frame = "cost-summary derived from rows already written — overhead as conclusion, not premise" (C-39); post-GATE 3 block = "retrospective record encountered after all gates complete — unreachable as a forward-declaring contract" (C-40). A model can identify whether it is about to produce the prohibited form by recognizing the causal consequence, not merely by checking structural position. This pattern is now established across C-28, C-39, and C-40: the progression is presence constraint → positional constraint → positional constraint with named bypass and causal consequence.

**No new criterion implied:** the prohibited-form naming is embedded in C-39 and C-40 rather than separable. The pattern informs how future positional criteria should be written.

---

## Round Summary

R13 validates the positional constraint pattern at two new sites: GATE 1 inertia framing (C-39) and the GATE CHAIN preamble (C-40). Both criteria are isolatable and structurally independent. V-04 achieves the first 250/250 under v13. V-05 seeds a plausible v14 criterion (checkpoint-level positional enforcement) by demonstrating that the checkpoint layer can enforce positional declarations that the declaration layer alone cannot guarantee.

The criterion lineage pattern continues: each criterion deepens the previous by closing the positional or scope bypass the presence-only form leaves open. C-37 → C-39 mirrors C-13 → C-28 (default-position framing → step-embedded). C-38 → C-40 mirrors C-25 → C-38 (GATE CHAIN presence → enumeration completeness) extended one further level to preamble position.

---

```json
{"top_score": 250, "all_essential_pass": true, "new_patterns": ["dual-layer positional enforcement: checkpoint items at CHECKPOINT-INERTIA and CHECKPOINT-0 verify positional constraints declared in skill instruction text, making declarations gate-blocking — a model cannot emit STATUS without passing the positional check, closing the gap between declared constraint and enforced constraint"]}
```
