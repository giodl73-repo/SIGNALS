# Quest Score — prove-topic R20 (Rubric v14)

## Scoring Setup

**Formula**: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/2 × 10)`
**Golden threshold**: all 5 essential pass AND composite ≥ 80

**Criterion map** (inferred from rubric + axis targets):

| Criterion | Weight | What it tests |
|-----------|--------|---------------|
| C-01 | Essential | All five sub-skills in sequence |
| C-02 | Essential | Scout artifact named before hypothesis |
| C-03 | Essential | Progressive writes — one per stage |
| C-04 | Essential | Synthesis signals readiness for topic-story |
| C-05 | Essential | Artifact naming convention |
| C-06 | Recommended | Gate enforces scout presence (blocks if absent) |
| C-07 | Recommended | Evidence chain cited to source / citation traceability |
| C-08 | Recommended | Evidence quality assessed at each discovery stage |
| C-09 | Aspirational | Thin-evidence gaps carried forward to synthesis |
| C-10 | Aspirational | Structural block before hypothesis (ROLE B gate) |

---

## V-01 — Phrasing Register

**Axis**: Formal passive → second-person direct throughout. Structure identical to R19 baseline.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Sequence structure unchanged; second-person direct only clarifies who acts |
| C-02 | PASS | Scout artifact reference requirement preserved |
| C-03 | PASS | Per-stage write instructions unchanged |
| C-04 | PASS | Synthesis handoff block unchanged |
| C-05 | PASS | Naming convention unchanged |
| C-06 | PARTIAL | Clearer phrasing removes ambiguity but no structural gate added |
| C-07 | PARTIAL | Not addressed by this axis |
| C-08 | PARTIAL | No evidence quality fields added |
| C-09 | PARTIAL | No carry block present |
| C-10 | PARTIAL | No role resequencing; gate not surfaced structurally |

**Score**: (5/5 × 60) + (0/3 × 30) + (0/2 × 10) = **60**
**Golden**: No (60 < 80)

---

## V-02 — Role Sequence

**Axis**: ROLE B executes first as blocking gate owner; ROLE C/A cannot run until `gate_s_cleared`.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | All five evidence stages present; role order change is pre-hypothesis setup, not stage order |
| C-02 | PASS | ROLE B runs first — scout absence halts before any hypothesis work begins |
| C-03 | PASS | Per-stage writes unchanged |
| C-04 | PASS | Synthesis handoff unchanged |
| C-05 | PASS | Naming unchanged |
| C-06 | PASS | Gate now structurally blocks ROLE C/A until scout confirmed; ROLE B exit-if-blocked guard enforced |
| C-07 | PARTIAL | Not addressed by role resequencing |
| C-08 | PARTIAL | No evidence quality fields added |
| C-09 | PARTIAL | No carry block present |
| C-10 | PASS | Structural block before hypothesis is the direct purpose of this axis |

**Score**: (5/5 × 60) + (1/3 × 30) + (1/2 × 10) = 60 + 10 + 5 = **75**
**Golden**: No (75 < 80)

---

## V-03 — Evidence Quality Mandatory

**Axis**: `evidence_quality: [thin/moderate/strong]` required at S2/S3/S4 + THIN-EVIDENCE CARRY block in Stage 5.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | All five stages present; quality fields are additions, not replacements |
| C-02 | PASS | Scout reference unchanged |
| C-03 | PASS | Per-stage writes unchanged; quality fields are in-stage additions |
| C-04 | PASS | Synthesis handoff unchanged |
| C-05 | PASS | Naming unchanged |
| C-06 | PARTIAL | No role resequencing; gate not structurally surfaced |
| C-07 | PARTIAL | Not addressed |
| C-08 | PASS | `evidence_quality` field + `evidence_quality_note` (required if thin) mandated at each discovery stage — converts C-08 from organic to enforced |
| C-09 | PASS | THIN-EVIDENCE CARRY block explicitly enumerates thin stages, names weakened claims, and feeds `thin_evidence_penalty` into confidence chain |
| C-10 | PARTIAL | No structural gate before hypothesis |

**Score**: (5/5 × 60) + (1/3 × 30) + (1/2 × 10) = 60 + 10 + 5 = **75**
**Golden**: No (75 < 80)

---

## V-04 — Phrasing Register + Role Sequence

**Axes**: V-01 + V-02 combined.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Second-person direct improves execution fidelity on top of correct structure |
| C-02 | PASS | ROLE B first + clear phrasing double-confirms scout gate |
| C-03 | PASS | Per-stage writes clear and unambiguous |
| C-04 | PASS | Synthesis handoff unchanged |
| C-05 | PASS | Naming unchanged |
| C-06 | PASS | From role_sequence axis: structural gate enforced |
| C-07 | PARTIAL | Not addressed by either axis |
| C-08 | PARTIAL | Evidence quality not added |
| C-09 | PARTIAL | No carry block |
| C-10 | PASS | From role_sequence: structural block before hypothesis |

**Score**: (5/5 × 60) + (1/3 × 30) + (1/2 × 10) = 60 + 10 + 5 = **75**
**Golden**: No (75 < 80)

*Note*: Additive gain on C-01/C-03 clarity does not change PASS count since both already pass from baseline — phrasing lifts execution reliability but not the binary criterion count.

---

## V-05 — All Three Axes + Full R19 Baseline

**Axes**: phrasing_register + role_sequence + evidence_quality_mandatory, on the complete R19 structural stack (RESUME AUDIT, count-gated exits S2≥5/S3≥3/S4≥3, three-block Stage 5, HANDOFF with derivation annotations).

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Full R19 structural stack preserves all five stages in order; count gates (S2≥5/S3≥3/S4≥3) enforce stage completion before advance |
| C-02 | PASS | ROLE B first + full baseline scout-before-hypothesis requirement |
| C-03 | PASS | Per-stage writes on complete R19 stack; RESUME AUDIT confirms each artifact exists before proceeding |
| C-04 | PASS | Three-block Stage 5 + HANDOFF with derivation annotations explicitly marks synthesis as topic-story-ready |
| C-05 | PASS | Full baseline naming convention preserved |
| C-06 | PASS | ROLE B gate from role_sequence axis, reinforced with second-person exit-if-blocked guard |
| C-07 | PARTIAL | No R20 axis directly targets citation traceability; R19 baseline HANDOFF annotations approach this but stop short of explicit per-claim source linkage |
| C-08 | PASS | evidence_quality_mandatory axis: structured fields at S2/S3/S4, required note when thin |
| C-09 | PASS | THIN-EVIDENCE CARRY block precedes BLOCK 1; `thin_evidence_penalty` fed into chain_equation without restructuring three-block synthesis |
| C-10 | PASS | ROLE B executes first as structural gate; B → C → A resequencing makes blocking dependency visible before any dependent work |

**Score**: (5/5 × 60) + (2/3 × 30) + (2/2 × 10) = 60 + 20 + 10 = **90**
**Golden**: Yes (all 5 essential pass AND 90 ≥ 80) ✓

---

## Rankings

| Rank | Variation | Score | Golden | Essential | Recommended | Aspirational |
|------|-----------|-------|--------|-----------|-------------|--------------|
| 1 | V-05 | **90** | ✓ | 5/5 | 2/3 | 2/2 |
| 2 | V-02 | 75 | — | 5/5 | 1/3 | 1/2 |
| 3 | V-03 | 75 | — | 5/5 | 1/3 | 1/2 |
| 4 | V-04 | 75 | — | 5/5 | 1/3 | 1/2 |
| 5 | V-01 | 60 | — | 5/5 | 0/3 | 0/2 |

V-02, V-03, V-04 tie at 75 with different recommended/aspirational wins. V-04 doesn't outperform V-02 because the phrasing axis only raises execution reliability on criteria that already PASS.

---

## Excellence Signals — V-05

**Pattern 1: Structural labeling converts organic behaviors to enforced ones.** Adding `evidence_quality: [thin/moderate/strong]` as a required field at S2/S3/S4 means evidence quality can no longer be skipped. The label is cheap to add but makes C-08 testable — you can check whether the field exists.

**Pattern 2: CARRY block connects discovery gaps to synthesis confidence.** The THIN-EVIDENCE CARRY block before BLOCK 1 creates an explicit downstream consequence for thin evidence. Without it, weak evidence is noted and dropped. With it, thin stages are named, claims are flagged as weakened, and a `thin_evidence_penalty` enters the confidence chain. This is what turns C-09 from aspirational (nice if observed) to structural (required by prompt design).

**Pattern 3: Role sequence as execution gate.** Moving ROLE B first doesn't just reorder work — it makes the scout-absent case halt before any hypothesis analysis runs. The structural position of ROLE B is the enforcement mechanism. "If scout absent, exit here" only works when B runs before C and A.

**Pattern 4: The three axes are orthogonal and additive.** V-05 gains 4 criteria (C-06, C-08, C-09, C-10) that V-01 misses entirely. No axis conflicts with another. Phrasing affects execution fidelity; role sequence affects gate visibility; evidence quality affects gap tracking. They compose cleanly.

---

```json
{"top_score": 90, "all_essential_pass": true, "new_patterns": ["Structural labeling converts organic behaviors to enforced ones — required fields make criteria testable", "CARRY block creates explicit downstream consequence for thin evidence, connecting discovery gaps to synthesis confidence chain", "Role sequence as execution gate — moving blocking role first makes scout-absent halt structural, not advisory"]}
```
