## Quest Score — topic-reflect (Round 5, v5 rubric)

**Skill**: topic-echo (topic-reflect)
**Rubric**: v5-2026-03-17 (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-19 aspirational)
**Variations**: V-01 through V-05
**Max score**: 145 (60 essential + 30 recommended + 55 aspirational)
**Golden threshold**: all C-01–C-05 pass AND composite >= 100

---

### Evaluation

#### C-01 — Surprise orientation (Essential, 12 pts)

**V-01** PASS — Stage 4 instructions: "Name the specific B-# it contradicts or substantially extends." Contradicts requirement enforced ("A finding that confirms a prior belief is not a surprise. It is excluded.")

**V-02** PASS — "Name the specific B-# it contradicts or substantially extends. Full sentence — not a fragment." Both requirement and exclusion present.

**V-03** PASS — Stage 4 template field: "[What was learned. Name the specific B-# contradicted or extended. Full sentence.]"

**V-04** PASS — Matches V-01/V-02 formulation exactly.

**V-05** PASS — Calibration example (Surprise 0) models the B-# reference concretely: "contradicts B-3" visible in the worked instance.

---

#### C-02 — Symmetric Contract present (Essential, 12 pts)

**V-01** PASS — Stage 1 has opening model + 5-row epistemic profile + numbered belief inventory (min 3). Stage 6 verdict table has Belief / Resolution (COHERENT/CONTRADICTORY/FOREKNOWLEDGE-FLAGGED) / Revision Direction / Foreknowledge columns.

**V-02** PASS — Same structure; Stage 6 EXIT explicitly requires "Every Stage 1 belief has a resolution row."

**V-03** PASS — Identical structure with Stage 6 referencing Gate Sequence Overview for halt semantics.

**V-04** PASS — Full symmetric contract; Stage 6 EXIT: "No FOREKNOWLEDGE-FLAGGED row present (or artifact halted and not written)."

**V-05** PASS — Same as V-04; closing verdict requirement intact.

---

#### C-03 — Signal tracing (Essential, 12 pts)

**V-01** PASS — "Name the artifact: full artifact name, namespace, date. One primary source per entry. 'Multiple sources' or 'various artifacts' is not acceptable."

**V-02** PASS — "Primary artifact: name, namespace, date. One source per entry. 'Multiple sources' is not acceptable." EXIT criterion reinforces: "Signal Source names a specific artifact with date."

**V-03** PASS — Template: "[Artifact name, namespace, date. One specific source per entry.]"

**V-04** PASS — Identical prohibitions; EXIT criterion reinforces specificity.

**V-05** PASS — Calibration example models the requirement: `topic-registry-trace-contract-2026-02-14.md`, trace namespace, 2026-02-14. Unambiguous quality floor set.

---

#### C-04 — Design impact specificity (Essential, 12 pts)

**V-01** PASS — "Name the specific component, API, contract, flow, or decision affected. Complete sentence. 'The system' or 'the overall design' is not acceptable."

**V-02** PASS — Identical prohibition. EXIT: "Design Impact names a specific component or contract."

**V-03** PASS — "[Specific component, API, contract, flow, or decision. Full sentence. Not 'the system.']"

**V-04** PASS — Same prohibitions; EXIT reinforces.

**V-05** PASS — Calibration example demonstrates: "The /topic-story skill must issue sequential per-namespace reads and merge results client-side; the single-query assumption must be removed from the skill contract before implementation begins." Specificity floor observable.

---

#### C-05 — Adversarial gate executed (Essential, 12 pts)

**V-01** PASS — Stage 3 five-check table FC-1 through FC-5 with VALID/INVALID cells. GATE-CONFIRMED-[N] and GATE-REJECTED-[N] tokens defined with format strings.

**V-02** PASS — Same table; EXIT requires every candidate to have a verdict token before COMMIT-STAGE-3-CLEAN/FLAGGED.

**V-03** PASS — Same table; Gate Sequence Overview lists GATE-CONFIRMED and GATE-REJECTED in token glossary.

**V-04** PASS — Same table; EXIT enforces token emission.

**V-05** PASS — Gate Sequence Overview glossary + Stage 3 EXIT + same five-check table.

---

#### C-06 — Epistemic dimension compliance (Recommended, 10 pts)

**V-01** PASS — Vocabulary Declaration lists the 5 canonical names as the only valid set. Stage 1 epistemic profile table pre-populated with exactly those 5 rows.

**V-02** PASS — "These names are fixed. Do not substitute." Stage 1 table uses only canonical rows.

**V-03** PASS — "These are the only valid names. Do not substitute." Stage 1 table correct.

**V-04** PASS — EXIT criterion for Stage 1: "All dimension names canonical (correct malformed names using the mapping table if needed before emitting)."

**V-05** PASS — Same as V-04.

---

#### C-07 — Minimum 2 surprises (Recommended, 10 pts)

**V-01** PASS — Stage 4 explicit minimum: "Minimum 2 entries." Stage 3 halt condition: "if GATE-CONFIRMED count < 2 after full sweep, extend Stage 2 before proceeding."

**V-02** PASS — Stage 3 EXIT: "GATE-CONFIRMED count verified. If count < 2: halt, return to Stage 2, extend inventory, re-execute Stage 3."

**V-03** PASS — Stage 4 "Minimum 2 entries." Stage 3 directs to Gate Sequence Overview for halt, which specifies the same condition.

**V-04** PASS — Stage 3 EXIT identical to V-02.

**V-05** PASS — Stage 3 EXIT references Gate Sequence Overview for halt; Stage 4 ENTER: "At least 2 GATE-CONFIRMED entries confirmed."

---

#### C-08 — Cluster map actionability (Recommended, 10 pts)

**V-01** PASS — Stage 5 table header: "[Named skill, e.g. /flow-trigger, or specific role — not 'investigate']". Rule: "At least one row must name a specific skill or role."

**V-02** PASS — "At least one row must name a specific skill (e.g., /trace-contract) or role — not 'investigate.'"

**V-03** PASS — "At least one row must name a specific skill (e.g., /trace-permissions) or role."

**V-04** PASS — Same.

**V-05** PASS — Same; example name `/flow-trigger` given.

---

#### C-09 — Token protocol integrity (Aspirational, 5 pts)

**V-01** PASS — GATE-CONFIRMED-[N]: VALID — Stage 4 (names Stage 4). COMMIT-ENTRY-[N] per Stage 4 entry. Output section: "All tokens (COMMIT-STAGE-1 through COMMIT-STAGE-6, GATE-CONFIRMED-[N], GATE-REJECTED-[N], COMMIT-ENTRY-[N]) must appear in the artifact."

**V-02** PASS — GATE-CONFIRMED-[N]: VALID — Stage 4. COMMIT-ENTRY-[N] per entry. Output: "All 6 stages in sequence. All tokens present."

**V-03** PASS — Gate Sequence Overview token glossary enumerates all 6 COMMIT-STAGE tokens plus GATE-CONFIRMED, GATE-REJECTED, COMMIT-ENTRY.

**V-04** PASS — Same as V-01.

**V-05** PASS — Gate Sequence Overview glossary + all tokens enforced.

---

#### C-10 — Foreknowledge signal evaluated (Aspirational, 5 pts)

**V-01** PASS — Stage 6 verdict table has Foreknowledge column (CLEAR / FLAGGED). Halt condition: "if any belief row is FOREKNOWLEDGE-FLAGGED, do not write the artifact."

**V-02** PASS — Same column; EXIT: implied by halt. Stage 3 FLAGGED token: "COMMIT-STAGE-3-FLAGGED — [B-#] anticipated [finding]."

**V-03** PASS — Foreknowledge column in Stage 6. Stage 6 refers to Gate Sequence Overview for halt semantics. Gate map shows Stage 6 halt: "If any belief is FOREKNOWLEDGE-FLAGGED: halt, do not write artifact."

**V-04** PASS — Stage 6 EXIT: "No FOREKNOWLEDGE-FLAGGED row present (or artifact halted and not written)."

**V-05** PASS — Same as V-04.

---

#### C-11 — Stage 4 prose template format (Aspirational, 5 pts)

**V-01** PASS — "A table row is not acceptable for this stage; the prose block format is mandatory." Template shows **Surprise N: [Title]** with labeled sub-fields.

**V-02** PASS — "Write a numbered prose block for each GATE-CONFIRMED entry." Template with labeled sub-fields.

**V-03** PASS — "For each GATE-CONFIRMED entry, write a numbered prose block."

**V-04** PASS — Numbered prose block format with labeled sub-fields; "A table row is not acceptable" not stated but format constraint enforced via EXIT: "No field is a fragment or a single noun phrase."

Actually V-04 does not include the "table row is not acceptable" prohibition explicitly. Let me re-check. Lines 727-744: "For each GATE-CONFIRMED entry, write a numbered prose block: **Surprise N: [Title — 3–6 words, title case]** ... EXIT per entry: All three fields populated." The numbered prose block format is specified. There's no explicit "table is not acceptable" line as in V-01. However, the instruction to "write a numbered prose block" is a positive constraint that implies the format. PASS — prose block format mandated.

**V-05** PASS — Same as V-04; plus calibration example demonstrates the format concretely.

---

#### C-12 — Stage 4 entry completeness (Aspirational, 5 pts)

**V-01** PASS — Signal Source requires "full artifact name, namespace, date." Design Impact requires "Complete sentence." These structurally prevent single-word entries.

**V-02** PASS — EXIT per entry: "No field is a fragment or a single noun phrase." Explicit completeness gate.

**V-03** PASS — Signal Source template: "[Artifact name, namespace, date. One specific source per entry.]" Design Impact: "[Specific component, API, contract, flow, or decision. Full sentence.]" Structural enforcement present; no explicit fragment prohibition.

**V-04** PASS — EXIT per entry: "No field is a fragment or a single noun phrase." Same as V-02.

**V-05** PASS — Calibration example sets concrete floor: Signal Source is a full artifact name + namespace + date; Design Impact is a 2-clause sentence naming the skill, the operation, and the implication.

---

#### C-13 — Closed-list dimension vocabulary (Aspirational, 5 pts)

**V-01** PASS — Standalone Vocabulary Declaration section: "**The only valid epistemic dimension names are:** Feasibility · Usability · Scalability · Adoptability · Correctness." Explicit substitution prohibition separate from Stage 1 prose.

**V-02** PASS — Standalone Vocabulary section with closed-list rule and explicit substitution prohibition: "These names are fixed. Do not substitute."

**V-03** PASS — Same standalone structure: "**Feasibility · Usability · Scalability · Adoptability · Correctness** — These are the only valid names. Do not substitute."

**V-04** PASS — Vocabulary Declaration: "**The only valid epistemic dimension names are:**" with closed list.

**V-05** PASS — Same as V-04.

---

#### C-14 — Foreknowledge dual-token gate (Aspirational, 5 pts)

**V-01** PASS — Stage 3: both COMMIT-STAGE-3-CLEAN and COMMIT-STAGE-3-FLAGGED paths defined. Foreknowledge resolution section makes the binary explicit.

**V-02** PASS — Same binary; Stage 3 EXIT requires one of the two tokens before Stage 4 proceeds: "COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED emitted."

**V-03** PASS — Gate Sequence Overview lists Stage 3 emits: "COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED." Binary established before Stage 1.

**V-04** PASS — Stage 3 EXIT same as V-02.

**V-05** PASS — Gate Sequence Overview + Stage 3 EXIT enforce binary.

---

#### C-15 — Pre-stage gate sequence map (Aspirational, 5 pts)

**V-01** FAIL — No gate sequence map. Stages are self-contained; no top-level navigation table.

**V-02** FAIL — No gate sequence map. ENTER/EXIT contracts provide local context but no global orientation table.

**V-03** PASS — Gate Sequence Overview table present before Stage 1. Lists Stage / Name / Emits / Halt Condition for all 6 stages. Token glossary included. Instruction: "Read this before Stage 1. It is the complete execution model for this skill."

**V-04** FAIL — No gate sequence map. Combines C-18 + C-19 but not C-15.

**V-05** PASS — Gate Sequence Overview table identical to V-03. Positioned after function description but before any stage instructions.

---

#### C-16 — Worked calibration example (Aspirational, 5 pts)

**V-01** FAIL — No worked example. Template placeholders only.

**V-02** FAIL — No worked example.

**V-03** FAIL — No worked example.

**V-04** FAIL — No worked example.

**V-05** PASS — Calibration example "Surprise 0: Namespace Isolation Blocks Cross-Signal Composition" is a complete filled-in Stage 4 block with realistic artifact reference (`topic-registry-trace-contract-2026-02-14.md`, trace namespace, 2026-02-14) and full-sentence Design Impact naming a specific skill and operation.

---

#### C-17 — Named synonym exclusions (Aspirational, 5 pts)

**V-01** PASS — Mapping table names 6 prohibited synonyms: Reliability, Performance, Complexity, Maintainability, Discoverability, Testability.

**V-02** PASS — Inline vocabulary: "Prohibited synonyms: 'Reliability' (use Correctness), 'Performance' (use Scalability), 'Maintainability' (use Adoptability)." 3 named synonyms — exceeds minimum of 2.

**V-03** PASS — Same inline format as V-02: Reliability, Performance, Maintainability named.

**V-04** PASS — Mapping table with 6 named synonyms, same as V-01.

**V-05** PASS — Same mapping table as V-01/V-04.

---

#### C-18 — Synonym-to-canonical replacement mapping (Aspirational, 5 pts)

The criterion requires mapping each prohibited synonym to its canonical replacement; at least 2 mappings. A table is not required — inline "(use X)" notation achieves the mapping.

**V-01** PASS — Formal mapping table: Reliability→Correctness, Performance→Scalability, Complexity→Correctness/Feasibility, Maintainability→Adoptability, Discoverability→Usability/Adoptability, Testability→Correctness/Feasibility. 6 mappings.

**V-02** PASS — Inline mappings: "Reliability" (use Correctness), "Performance" (use Scalability), "Maintainability" (use Adoptability). 3 mappings. Canonical targets specified, substitution loop closed. Passes even though format is prose rather than table.

**V-03** PASS — Same inline format as V-02. 3 mappings: Reliability→Correctness, Performance→Scalability, Maintainability→Adoptability.

**V-04** PASS — Formal mapping table identical to V-01.

**V-05** PASS — Same mapping table as V-01/V-04.

> **Observation**: V-02 and V-03 were designed as single-axis variations that did not target C-18, yet both pass it. The inline "(use X)" notation that became the base vocabulary pattern in R5 inherently satisfies C-18 without requiring a formal table. C-18 is no longer aspirational-discriminating for single-axis variations; only C-16 and C-19 (and C-15) remain differentiating.

---

#### C-19 — Per-stage ENTER/EXIT lifecycle contract (Aspirational, 5 pts)

**V-01** FAIL — No ENTER/EXIT contracts. Stages have instructions but no explicit pre/post-condition framing.

**V-02** PASS — All 6 stages have ENTER and EXIT. Stage 1: ENTER (no artifacts read) + EXIT (5 rows populated, 3 beliefs numbered). Stage 2: ENTER (Stage 1 committed) + EXIT (all artifacts listed). Stage 3: ENTER (Stage 2 committed, candidates identified) + EXIT (all candidates have verdict tokens). Stage 4: ENTER (COMMIT-STAGE-3 emitted, ≥2 GATE-CONFIRMED) + EXIT per entry (no fragments). Stage 5: ENTER (all Stage 4 entries committed) + EXIT (all surprises in clusters). Stage 6: ENTER (all prior stages committed) + EXIT (every belief has resolution row).

**V-03** FAIL — No ENTER/EXIT contracts. Gate map provides global orientation but stages have no local pre/post conditions.

**V-04** PASS — All 6 stages have ENTER and EXIT; same structure as V-02. Stage 1 EXIT explicitly links to the mapping table: "All dimension names canonical (correct malformed names using the mapping table before emitting)."

**V-05** PASS — Same ENTER/EXIT structure as V-02/V-04. Stage 4 ENTER mirrors Stage 3 EXIT ("At least 2 GATE-CONFIRMED entries confirmed"). Stage 3 EXIT references Gate Sequence Overview for halt condition, creating a cross-reference rather than duplicating the condition inline.

---

### Scorecards

| Criterion | Tier | Pts | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|-----|------|------|------|------|------|
| C-01 Surprise orientation | E | 12 | PASS | PASS | PASS | PASS | PASS |
| C-02 Symmetric Contract | E | 12 | PASS | PASS | PASS | PASS | PASS |
| C-03 Signal tracing | E | 12 | PASS | PASS | PASS | PASS | PASS |
| C-04 Design impact specificity | E | 12 | PASS | PASS | PASS | PASS | PASS |
| C-05 Adversarial gate | E | 12 | PASS | PASS | PASS | PASS | PASS |
| C-06 Dimension compliance | R | 10 | PASS | PASS | PASS | PASS | PASS |
| C-07 Min 2 surprises | R | 10 | PASS | PASS | PASS | PASS | PASS |
| C-08 Cluster actionability | R | 10 | PASS | PASS | PASS | PASS | PASS |
| C-09 Token protocol | A | 5 | PASS | PASS | PASS | PASS | PASS |
| C-10 Foreknowledge signal | A | 5 | PASS | PASS | PASS | PASS | PASS |
| C-11 Stage 4 prose format | A | 5 | PASS | PASS | PASS | PASS | PASS |
| C-12 Entry completeness | A | 5 | PASS | PASS | PASS | PASS | PASS |
| C-13 Closed-list vocab | A | 5 | PASS | PASS | PASS | PASS | PASS |
| C-14 Dual-token gate | A | 5 | PASS | PASS | PASS | PASS | PASS |
| C-15 Gate sequence map | A | 5 | FAIL | FAIL | PASS | FAIL | PASS |
| C-16 Worked calibration | A | 5 | FAIL | FAIL | FAIL | FAIL | PASS |
| C-17 Named synonyms | A | 5 | PASS | PASS | PASS | PASS | PASS |
| C-18 Synonym mapping | A | 5 | PASS | PASS | PASS | PASS | PASS |
| C-19 ENTER/EXIT contracts | A | 5 | FAIL | PASS | FAIL | PASS | PASS |

| Component | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| Essential (60) | 60 | 60 | 60 | 60 | 60 |
| Recommended (30) | 30 | 30 | 30 | 30 | 30 |
| Aspirational (55) | 40 | 45 | 45 | 45 | 55 |
| **Total** | **130** | **135** | **135** | **135** | **145** |
| All essential pass | YES | YES | YES | YES | YES |
| Golden | YES | YES | YES | YES | YES |

---

### Rankings

| Rank | Variation | Score | Axis |
|------|-----------|-------|------|
| 1 | **V-05** | 145 | Gate map + synonym mapping + ENTER/EXIT + worked example |
| 2 (tie) | **V-02** | 135 | ENTER/EXIT contracts |
| 2 (tie) | **V-03** | 135 | Gate sequence map |
| 2 (tie) | **V-04** | 135 | Synonym mapping + ENTER/EXIT |
| 5 | **V-01** | 130 | Synonym mapping only |

---

### Excellence Signals — V-05

V-05 scores 145 (perfect) by accumulating the only two differentiating aspirational criteria (C-15 gate map, C-16 worked example) atop the full C-09 through C-19 base. Three patterns account for its margin over the 135-point cluster:

**1. Gate map as live cross-reference, not orientation-only preamble.**
V-03 introduced the gate map (C-15) but stages are self-contained — the map is read once at the top and not consulted again. V-05 has Stage 3 EXIT: "Refer to the Gate Sequence Overview for the halt condition if GATE-CONFIRMED count < 2" and Stage 6: "Refer to the Gate Sequence Overview for the FOREKNOWLEDGE-FLAGGED halt condition." The map becomes a referenced authority during execution, not optional preamble. This prevents the risk named in V-03's hypothesis: if the model treats the map as skippable, C-15 passes but the orientation benefit evaporates. V-05 closes that failure mode by making specific stages depend on the map.

**2. Worked example as vocabulary anchor, not only quality floor.**
C-16 is written as a quality calibration for Signal Source specificity and Design Impact concreteness. V-05's example demonstrates a skill name (`/topic-story`) as the Design Impact referent — showing that the "specific component, API, contract, flow, or decision" category includes skill invocations. This expands the model's sense of what counts as specific without changing the criterion, and anchors the vocabulary of the design layer (skills, contracts, registries) rather than abstract system components.

**3. Stage-to-stage handoff alignment.**
V-02 and V-04 introduced ENTER/EXIT contracts (C-19). V-05 adds an additional layer: Stage 3 EXIT verifies GATE-CONFIRMED count, and Stage 4 ENTER restates the same requirement ("At least 2 GATE-CONFIRMED entries confirmed"). The EXIT of one stage is the mirror of the ENTER of the next — the stages do not merely terminate and begin, they explicitly hand off verified state. This converts the ENTER/EXIT structure from a local completeness check into an inter-stage contract chain. Not captured by C-19, which only requires per-stage ENTER/EXIT presence.

---

### Round 5 Observation

All five variations achieve Golden status. The scoring distribution was flatter than predicted: V-02 and V-03 both scored 135 rather than the predicted 125, because both carry inline synonym-to-canonical mappings in their base vocabulary ("Reliability" (use Correctness), etc.) that satisfy C-18 — a criterion R5 had designated as the discriminating axis for V-01. As of R5, C-18 compliance is achieved by inline notation across all variations, not only by formal mapping tables. The only remaining differentiators at the aspirational tier are C-15 (gate map), C-16 (worked example), and C-19 (ENTER/EXIT contracts). V-05 captures all three; the 135-tier variations each capture at most two.

---

```json
{"top_score": 145, "all_essential_pass": true, "new_patterns": ["Gate map as live cross-reference: stages cite the Gate Sequence Overview for specific halt conditions rather than repeating them inline — making the map an active execution authority rather than skippable preamble", "Stage-to-stage handoff alignment: Stage N EXIT verifies the same condition that Stage N+1 ENTER requires, creating a mirrored inter-stage contract chain rather than independent local contracts"]}
```
