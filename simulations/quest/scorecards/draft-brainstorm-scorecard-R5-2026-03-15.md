## R5 Scoring — draft-brainstorm

### Evaluation Framework

Point allocation (per rubric v5):
- Essential C-01..C-05: 12 pts each → max 60
- Recommended C-06..C-08: 10 pts each → max 30
- Aspirational C-09..C-10: 5 pts each → max 10
- Extended R2 C-11..C-14: 2.5 pts each → max 10
- R3 C-15..C-18: 2.5 pts each → max 10
- R4 C-19..C-20: 2.5 pts each → max 5
- R5 C-21..C-22: 2.5 pts each → max 5

---

### V-01 — Phrasing Register: Selection-Phase Advance Gate

**Axis**: Converts "before Check C" batch sequencing to an explicit phase-advance gate; no consequence clause (intentional C-20 isolation).

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 Volume | PASS | "20-40 candidates" in Phase 1b |
| C-02 Idea Anatomy | PASS | Per-idea block: name (heading), Pitch, Rationale, Dimension (section header) |
| C-03 Top-5 Marker | PASS | "Mark exactly 5 ideas with `**` on their heading" Phase 3 |
| C-04 Inertia Check | PASS | "Do Nothing" in Status Quo section; "rationale must continue the framing paragraph from 1a" |
| C-05 AMEND | PASS | 1c draft + Check C re-invocability; "3 pool-shift directions" |
| C-06 Category Grouping | PASS | "Required `##` sections per dimension; Do not collapse into flat list" |
| C-07 Rationale Specificity | PASS | "cite a real constraint, user need, or opportunity. No generic reasoning." |
| C-08 Category Diversity | PASS | 6 named dimensions with descriptions |
| C-09 AMEND Actionability | PASS | Check C: "noticeably different pool"; "different candidate distribution" |
| C-10 Top-5 Defensibility | PASS | Check A + Check B with peer sentences and batch gate |
| C-11 Sequential-Default Guard | PASS | "Do not mark top-5 yet." in Phase 1b (generation phase), imperative |
| C-12 Re-Runnability Bar | PASS | Check C: "re-ran this brainstorm, would they get a noticeably different pool?" |
| C-13 Category Dimension Taxonomy | PASS | 6 named dimension types with descriptions as required sections |
| C-14 Inertia-First Framing | PASS | Phase 1a: "appears at the top of the final artifact and precedes all ideas" |
| C-15 Structural Spine | PASS | 6 required `##` sections; "Do not collapse; do not omit any listed dimension" |
| C-16 Generation-Phase Guard | PASS | "Do not mark top-5 yet" in Phase 1b, imperative, before selection |
| C-17 Peer-Comparison Test | PASS | "complete this sentence: 'I chose [Idea Name] over [peer] because ___'" in Check B |
| C-18 Self-Review Integration | PASS | Check A → "candidates for Check B"; Check B → "marks in Phase 3"; C → "AMEND content"; D → "artifact write" |
| C-19 Peer-Test Imperative | PASS | "complete this sentence and write it in your output" + "Write all five … batch" |
| C-20 Consequence Clause | **FAIL** | No consequence clause — intentional isolation to test C-21 independently |
| C-21 Batch-Completion Gate | PASS | "Write all five completed sentences as a numbered batch (Check B Batch) before advancing to Check C. **Phase 3 is gated by batch completion: do not place any `**` marks anywhere until all five Check B sentences appear in your output.**" — explicit selection-phase advance gate, not just check-sequencing |
| C-22 Replacement Source | **FAIL** | C-20 prerequisite absent; no consequence clause to attach source specificity to |

**Score**: Essential 60 + Rec 30 + Asp 10 + R2 10 + R3 10 + R4 2.5 (C-19 only) + R5 2.5 (C-21 only) = **125**

---

### V-02 — Lifecycle Emphasis: Replacement Source Trace

**Axis**: Traces replacement source to the specific peer from this comparison; interrogative form preserved (intentional C-19 isolation).

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01..C-05 | PASS (inh) | Same base structure as V-01 |
| C-06..C-10 | PASS (inh) | Inherited: 6 dimensions, topic-specific rationale, phase structure |
| C-11..C-14 | PASS (inh) | Same anti-sequential guard, re-runnability, taxonomy, inertia-first |
| C-15..C-18 | PASS (inh) | Phase 2 checks A-D with downstream labels; same as V-01 |
| C-19 Peer-Test Imperative | **FAIL** | "can you complete this sentence" — interrogative allows silent affirmation; intentional isolation |
| C-20 Consequence Clause | PASS | "that idea must be replaced with the specific peer you attempted to name in this comparison. The replacement source is fixed: it is the peer you named here, for this specific candidate, in this specific check — not a different idea you might prefer after reconsidering the pool." Named consequence + replacement mandatory |
| C-21 Batch-Completion Gate | **FAIL** | C-19 prerequisite absent (interrogative form cannot anchor an imperative batch gate); no batch-write sequencing present |
| C-22 Replacement Source | PASS | "The replacement source is fixed: it is the peer you named here, for this specific candidate, in this specific check — not a different idea you might prefer after reconsidering the pool. Do not revise the marked idea's rationale to manufacture a distinction… the peer from this check is the only permissible replacement source." Source explicitly fixed to the peer from this specific comparison |

**Score**: Essential 60 + Rec 30 + Asp 10 + R2 10 + R3 10 + R4 2.5 (C-20 only) + R5 2.5 (C-22 only) = **125**

---

### V-03 — Output Format: Pre-Selection Batch Registry (order fixed)

**Axis**: Moves Registry to Step 2b (pre-selection), fixing R4-V-03's order inversion; schema encoding makes batch gate and source specificity structural constraints.

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 Volume | PASS | "20-40 rows total" in Step 1 |
| C-02 Idea Anatomy | PASS | Table columns: Name, Pitch, Dimension, Rationale — all 4 fields |
| C-03 Top-5 Marker | PASS | "`**YES**` in exactly 5 rows' Top-5? column, using candidates confirmed in the Registry" |
| C-04 Inertia Check | PASS | "Do Nothing" row in Dimension = Status Quo; Rationale "must describe what the current trajectory produces" |
| C-05 AMEND | PASS | Step 5 with 3 items; output of Review B; all three sub-conditions |
| C-06 Category Grouping | PASS | Step 4 Category View "required structural output… must contain a section for every Dimension. A flat list fails." |
| C-07 Rationale Specificity | PASS | "'This provides value' is not a rationale" |
| C-08 Category Diversity | PASS | 7 required dimension types with descriptions |
| C-09 AMEND Actionability | PASS | Condition (c): "is re-invocable — a reader can re-run the brainstorm from this directive and produce a noticeably different table" |
| C-10 Top-5 Defensibility | PASS | Pre-Selection Registry + Review A (anti-sequential) + substitution rule |
| C-11 Sequential-Default Guard | PASS | "Leave this column **blank during Step 1.** Do not fill in Top-5? values as you build the table. Marking during construction introduces sequential bias" |
| C-12 Re-Runnability Bar | PASS | "Re-runnable with this directive alone" as explicit condition (c) |
| C-13 Category Dimension Taxonomy | PASS | 7 named dimension types with descriptions as required Dimension values |
| C-14 Inertia-First Framing | PASS | "Preamble paragraph… must appear before the idea table in the final artifact" |
| C-15 Structural Spine | PASS | 7 required dimension types as mandatory output sections; Category View enforces `##` per dimension |
| C-16 Generation-Phase Guard | PASS | "Leave blank during Step 1" — construction phase, imperative |
| C-17 Peer-Comparison Test | PASS | Registry column: `"I chose [Candidate] over [Peer] because ___"` — sentence-completion in table schema |
| C-18 Self-Review Integration | PASS | Review A → "candidates for Step 2b"; Review B → "AMEND content in Step 5"; Review C → "Category View completeness in Step 4"; Step 2b → gates Step 3 |
| C-19 Peer-Test Imperative | PASS | Registry schema — each row IS the completed sentence; structurally cannot be skipped; "cannot be filled" gate |
| C-20 Consequence Clause | PASS | "substitution is mandatory and the replacement source is the Attempted Peer named here" — specific action named |
| C-21 Batch-Completion Gate | PASS | "**Step 3 is gated by this section: the Top-5? column cannot contain any entry until all 5 rows of this Registry are filled.**" — structural gate; section ordering enforces all-5-before-selection at document level |
| C-22 Replacement Source | PASS | "The replacement source is fixed: it is the idea in the Attempted Peer column of that row — not a different idea from the table." — Attempted Peer column is a structural anchor; replacement source = column value, not post-hoc pick |

**Score**: Essential 60 + Rec 30 + Asp 10 + R2 10 + R3 10 + R4 5 + R5 5 = **130**

---

### V-04 — Combination: Batch Gate + Source Trace + Explicit C-18

**Axis**: V-01 + V-02 combined in a single Check B; all four Phase 2 checks have explicit downstream labels.

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01..C-10 | PASS | Same base; "20-40 candidates", per-idea block, Status Quo, AMEND |
| C-11..C-14 | PASS | Generation-phase guard, re-runnability, 6 named dimensions, inertia-first |
| C-15 Structural Spine | PASS | 6 required `##` sections; "Do not collapse; do not omit" |
| C-16 Generation-Phase Guard | PASS | "Do not mark top-5 yet." in Phase 1b |
| C-17 Peer-Comparison Test | PASS | "complete this sentence and write it in your output: 'I chose [Name] over [peer] because ___'" |
| C-18 Self-Review Integration | PASS | Check A "determines candidates for Check B"; Check B "determines top-5 marks in Phase 3"; Check C "determines final AMEND content"; Check D "gates artifact write" — all four links explicitly named |
| C-19 Peer-Test Imperative | PASS | "complete this sentence and write it in your output" + "all five as numbered batch before advancing to Check C" |
| C-20 Consequence Clause | PASS | "must be replaced with the specific peer you attempted to name in this comparison… replacement is mandatory and the replacement source is the peer named here" |
| C-21 Batch-Completion Gate | PASS | "Write all five sentences as a numbered batch before advancing to Check C. **Phase 3 is gated by batch completion: do not place any `**` marks until all five Check B sentences appear in your output.**" |
| C-22 Replacement Source | PASS | "The replacement source is fixed: it is the peer from this specific Check B comparison for this specific candidate, not a different idea you might prefer after reconsidering the pool." |

**Score**: Essential 60 + Rec 30 + Asp 10 + R2 10 + R3 10 + R4 5 + R5 5 = **130**

---

### V-05 — Full Stack: R4-V-05 + R5 Patches

**Axis**: R4-V-05 architecture with explicit batch-advance gate and "attempted to name" phrasing; 7 dimensions, Self-Review Phase with four labeled reviews.

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01..C-10 | PASS | "20-40", per-idea block, Status Quo Dimension 7, AMEND with Review C |
| C-11..C-14 | PASS | "Do not mark any idea with `**` in this section" (Axis Map, generation phase); re-runnability; 7 named dimensions; Preliminary precedes alternatives |
| C-15 Structural Spine | PASS | 7 dimensions, each `##` header in Axis Map; mandated one-per-dimension |
| C-16 Generation-Phase Guard | PASS | "Do not mark any idea with `**` in this section" in Axis Map — generation-phase imperative |
| C-17 Peer-Comparison Test | PASS | "complete this sentence and write it in your output: 'I chose [Idea Name] over [peer] because ___'" in Review B |
| C-18 Self-Review Integration | PASS | Review A → "eligible for peer test"; Review B → "final top-5 marks"; Review C → "AMEND finalization"; Review D → "gates artifact write" |
| C-19 Peer-Test Imperative | PASS | "complete this sentence and write it in your output" + "full batch of five sentences" |
| C-20 Consequence Clause | PASS | "must be replaced with the specific peer you attempted to name in this review… replacement is mandatory" |
| C-21 Batch-Completion Gate | PASS | "Write all five sentences as a numbered batch before advancing to Review C. **Do not advance to the Top-5 Selection step — do not place any `**` marks — until the full batch of five sentences appears in your output.**" — double prohibition closes both phase-advance and inline-marking paths |
| C-22 Replacement Source | PASS | "The replacement source is fixed: it is the peer you attempted to name here, not a different idea you might prefer after reconsidering the pool." |

**Score**: Essential 60 + Rec 30 + Asp 10 + R2 10 + R3 10 + R4 5 + R5 5 = **130**

---

### Composite Score Table

| Variation | Ess | Rec | Asp | R2 | R3 | R4 | R5 | Total |
|-----------|-----|-----|-----|----|----|----|----|-------|
| V-01 | 60 | 30 | 10 | 10 | 10 | 2.5 | 2.5 | **125** |
| V-02 | 60 | 30 | 10 | 10 | 10 | 2.5 | 2.5 | **125** |
| V-03 | 60 | 30 | 10 | 10 | 10 | 5.0 | 5.0 | **130** |
| V-04 | 60 | 30 | 10 | 10 | 10 | 5.0 | 5.0 | **130** |
| V-05 | 60 | 30 | 10 | 10 | 10 | 5.0 | 5.0 | **130** |

**Ranking**: V-03 = V-04 = V-05 (130) > V-01 = V-02 (125)

All 5 variations pass all essential criteria.

---

### Excellence Signals — Top-Scoring Tier (V-03, V-04, V-05)

**What the 130-tier variations did that 125-tier variations did not:**

**1. Schema-position temporal gate (V-03)**
V-03's Pre-Selection Batch Registry is a required output *section* positioned between Step 2 (Self-Review) and Step 3 (marking). The batch-completion gate is not a prose prohibition — it is a section that must exist in the output before the next section can have values. "Step 3 is gated by this section" makes compliance a document-structure property: if the Registry section is missing or incomplete, the artifact is structurally incomplete regardless of model behavior. This is a qualitatively different constraint class from prose instructions.

**2. Double-prohibition gate phrasing (V-04, V-05)**
Both V-04 and V-05 use a two-part prohibition: "do not advance to [next phase]" AND "do not place any `**` marks." The dual formulation closes two distinct soft paths simultaneously — a model that argues "I haven't advanced to Phase 3 but I'm just making a preliminary note" is blocked by both prohibitions. V-05 adds a third layer: naming the step explicitly ("Top-5 Selection step"), which removes any ambiguity about what "advancing" means.

**3. "Attempted to name" specificity (V-02, V-04, V-05)**
All three C-22-passing variations use "the peer you attempted to name" rather than "the peer you named." The distinction is: "you named" still allows post-hoc substitution (model names a different peer in retrospect), while "you attempted to name" fixes the replacement source as the peer in the sentence written during the test, before any reconsideration. This phrasing was independently critical for C-22 — V-03 achieves the same effect via the Attempted Peer column (a structural anchor that cannot be retroactively altered).

---

```json
{"top_score": 130, "all_essential_pass": true, "new_patterns": ["schema-position temporal gate: placing the batch registry as a required output section before the selection step enforces the ordering via document structure rather than prose instruction", "double-prohibition phrasing: 'do not advance to [next phase] -- do not place any ** marks' closes both the phase-advance and inline-marking soft paths simultaneously", "'attempted to name' anchors the replacement source to the peer written during the failed test, not a post-hoc pick after reconsidering the pool"]}
```
