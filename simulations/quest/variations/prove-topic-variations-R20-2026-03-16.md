Written to `simulations/quest/golden/prove-topic-variate-R20-v14-2026-03-16.md`.

---

## Round 20 — prove-topic Variations (rubric v14)

**Context**: R19 covered `output_format`, `inertia_framing`, `lifecycle_emphasis`. R20 uses three unexplored axes.

---

### Axis Selection

| Axis | What it changes | Primary criteria |
|------|-----------------|-----------------|
| `phrasing_register` | Formal passive → second-person direct throughout | C-01, C-03 (execution fidelity) |
| `role_sequence` | ROLE B executes first as blocking gate owner; ROLE C/A cannot run until gate clears | C-06, C-10 (structural block before hypothesis) |
| `evidence_quality_mandatory` | Mandatory `evidence_quality: [thin/moderate/strong]` per evidence stage + THIN-EVIDENCE CARRY block in Stage 5 | C-08, C-09 (gaps at discovery, carry to synthesis) |

---

### V-01 — Phrasing Register (single)

**Axis**: `phrasing_register`  
**Hypothesis**: The current prompt uses formal passive imperatives ("Fill before any role", "Confirms analysis complete", "Cannot be modified"). Second-person direct ("You fill this before any role", "You confirm the analysis is complete", "You cannot modify this") removes the ambiguity about who performs each action without changing any structural element. Tests whether C-01 and C-03 compliance depends on instruction clarity rather than structure.

*(Complete prompt body: identical R19 V-01 baseline structure with every instruction verb shifted to second-person direct; ENTRY CONDITIONS, tables, EXIT SIGNALs, count gates unchanged.)*

---

### V-02 — Role Sequence (single)

**Axis**: `role_sequence`  
**Hypothesis**: ROLE B owns the campaign-blocking gate but currently runs second. Moving ROLE B to execute first makes the most critical blocking dependency visible before any other role work begins. ROLE C and ROLE A are annotated as depending on `gate_s_cleared`. Stage 0 clearance reordered to Step 1 = `gate_s_cleared` (ROLE B), Step 2 = `incumbent_threat_locked` (ROLE C), Step 3 = `invariant_registry_confirmed` (ROLE A). If scout is absent, the campaign halts at ROLE B before any incumbent analysis is done. Directly targets C-10 (structural block before hypothesis) and C-06 (gate enforces scout presence).

*(Complete prompt body: R19 V-01 baseline with execution order changed to B → C → A, ROLE B exit-if-blocked guard added, Stage 0 steps reordered.)*

---

### V-03 — Evidence Quality Mandatory (single)

**Axis**: `evidence_quality_mandatory`  
**Hypothesis**: C-08 and C-09 remain partial because evidence quality assessment is model-organic, not structurally required. Adding `evidence_quality: [thin/moderate/strong]` and `evidence_quality_note` (required if thin) to each evidence stage (S2, S3, S4), then opening Stage 5 with a **THIN-EVIDENCE CARRY** block that enumerates thin stages, names the weakened claim, and computes a `thin_evidence_penalty` fed into the BLOCK 1 confidence chain, converts C-08 and C-09 from observed to enforced.

*(Complete prompt body: R19 V-01 baseline with evidence_quality fields added at S2/S3/S4, THIN-EVIDENCE CARRY block inserted before BLOCK 1, thin_evidence_penalty term added to chain_equation.)*

---

### V-04 — Phrasing Register + Role Sequence (combined)

**Axis**: `phrasing_register` + `role_sequence`  
**Hypothesis**: V-01 and V-02 are orthogonal. Combined, second-person direct register improves execution fidelity and ROLE B running first surfaces the blocking gate structurally. Tests additive gain on C-01, C-03, C-06, C-10 simultaneously.

---

### V-05 — All Three + Full R19 Baseline (full)

**Axis**: `phrasing_register` + `role_sequence` + `evidence_quality_mandatory`  
**Hypothesis**: All three axes on the complete R19 structural stack (RESUME AUDIT, count-gated exits S2>=5/S3>=3/S4>=3, three-block Stage 5, HANDOFF with derivation annotations). THIN-EVIDENCE CARRY precedes BLOCK 1 and feeds the confidence chain without restructuring the three-block synthesis. Tests whether the full combination simultaneously satisfies C-01, C-03, C-04, C-06, C-08, C-09, and C-10 without structural contradiction.
