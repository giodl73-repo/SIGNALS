Reading the scorecard's excellence signals and extracting two new criteria:

**C-11** — from: *"Format enforces specificity; instruction cannot"* → Stage 4 uses prose template format (numbered entries with labeled fields), not a table.

**C-12** — from: *"Stage 4 is the highest-leverage rewrite target"* → No fragment entries anywhere in Stage 4 (every Signal Source and Design Impact is a full phrase, not an abbreviation).

---

## Rubric: topic-echo (topic-reflect) — v2

**12 criteria across 3 tiers. Score = essential(60) + recommended(30) + aspirational(20).**

> v2 changes: Added C-11 and C-12 (aspirational) from Round 1 excellence signals. Aspirational tier expands from 10 → 20 pts. Golden threshold raised to 90.

---

### Essential (all must pass — 12 pts each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Surprise orientation** | correctness | Every Stage 4 row references a specific B-# from Stage 1; at least one entry contradicts (not confirms) the opening model |
| C-02 | **Symmetric Contract present** | correctness | Stage 1 has opening model + epistemic profile + 3+ beliefs; Stage 6 has verdict table with revision direction and COHERENT/CONTRADICTORY/FOREKNOWLEDGE-FLAGGED |
| C-03 | **Signal tracing** | correctness | Every Stage 4 surprise has a named artifact in Signal Source (name and/or namespace and/or date) — no "multiple sources" generics |
| C-04 | **Design impact specificity** | depth | Every Stage 4 Design Impact cell names a specific component, API, flow, or decision — not "the system" |
| C-05 | **Adversarial gate executed** | correctness | Stage 3 five-check table present; every deviation has a VALID/INVALID verdict; GATE-CONFIRMED or GATE-REJECTED tokens present |

---

### Recommended (10 pts each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Epistemic dimension compliance** | correctness | Only the 5 canonical names used in all dimension cells; no excluded synonyms |
| C-07 | **Minimum 2 surprises** | coverage | At least 2 GATE-CONFIRMED rows in Stage 4; sweep extended if gate initially yields fewer |
| C-08 | **Cluster map actionability** | behavior | Stage 5 Next Team / Skill column has at least one named skill or role (not just "investigate") |

---

### Aspirational (5 pts each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Token protocol integrity** | format | GATE-CONFIRMED tokens name Stage 4 (not just route to it); COMMIT-ENTRY per row in Stage 4; COMMIT-STAGE-1 through 6 all present |
| C-10 | **Foreknowledge signal evaluated** | depth | Stage 6 explicitly records CLEAR or FLAGGED; if FLAGGED, artifact not written and responsible belief(s) named |
| C-11 | **Stage 4 prose template format** | format | Stage 4 surprise entries are numbered prose blocks with labeled sub-fields (Surprise, Signal Source, Design Impact) — not a markdown table; no narrow-cell format pressure possible |
| C-12 | **Stage 4 entry completeness** | depth | No single-word or two-word entries appear in any Signal Source or Design Impact field across all Stage 4 entries; every field is a full phrase or sentence |

> **Rationale (C-11 / C-12):** Round 1 showed that table cell pressure was the root cause of C-03 and C-04 failures across four of five variations. Instruction-level reminders ("name the artifact") were insufficient against narrow-cell syntax. Prose template format structurally prevents the failure mode. C-11 checks the format choice; C-12 checks that no fragments slipped through regardless of format.

---

**Golden threshold:** all C-01 – C-05 pass AND composite >= 90 (requires all essential + at least 2/3 recommended + at least 2/4 aspirational).
