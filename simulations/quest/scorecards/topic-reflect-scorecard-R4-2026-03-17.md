## Quest Score — Round 4: topic-reflect (v4 rubric)

---

### Scoring Method

```
composite = (essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/9 × 45)
Golden: all C-01–C-05 pass AND composite >= 100
```

---

## V-01 — Phrasing Register (Formal/Technical)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Surprise orientation | **PASS** | Opening framing explicitly excludes confirmations ("A finding that confirms a prior belief is not a surprise. It is excluded."); Stage 4 requires "Name the specific B-# it contradicts or substantially extends." |
| C-02 | Symmetric Contract present | **PASS** | Stage 1: opening model + epistemic profile + ≥3 beliefs. Stage 6: verdict table with COHERENT/CONTRADICTORY/FOREKNOWLEDGE-FLAGGED + Revision Direction column. |
| C-03 | Signal tracing | **PASS** | "full artifact name, namespace, date. One primary source per entry. 'Multiple sources' or 'various artifacts' is not acceptable." |
| C-04 | Design impact specificity | **PASS** | "Name the specific component, API, contract, flow, or decision affected. Complete sentence. 'The system' or 'the overall design' is not acceptable." |
| C-05 | Adversarial gate executed | **PASS** | Full five-check table; GATE-CONFIRMED-[N]/GATE-REJECTED-[N] tokens; COMMIT-STAGE-3-CLEAN/FLAGGED binary present. |
| C-06 | Epistemic dimension compliance | **PASS** | Vocabulary Declaration table uses exactly the 5 canonical names; Stage 1 profile table matches. |
| C-07 | Minimum 2 surprises | **PASS** | "Minimum 2 entries. If fewer than 2 GATE-CONFIRMED entries exist…extend Stage 2 and re-execute Stage 3." |
| C-08 | Cluster map actionability | **PASS** | Stage 5: "[Named skill, e.g. `/flow-trigger`, or specific role — not 'investigate']" |
| C-09 | Token protocol integrity | **PASS** | GATE-CONFIRMED names Stage 4; COMMIT-ENTRY per entry; Output requires COMMIT-STAGE-1 through 6 all present. |
| C-10 | Foreknowledge signal evaluated | **PASS** | Stage 6 Foreknowledge column (CLEAR/FLAGGED); halt condition: "do not write the artifact. Report the flag and name the responsible beliefs." |
| C-11 | Stage 4 prose template format | **PASS** | "A table row is not acceptable for this stage; the prose block format is mandatory." Sub-fields labeled. |
| C-12 | Stage 4 entry completeness | **PASS** | Signal Source requires full artifact name + date; Design Impact requires "Complete sentence." |
| C-13 | Closed-list dimension vocabulary | **PASS** | Standalone Vocabulary Declaration section before Stage 1 with explicit prohibition: "Any dimension cell containing a term not in the canonical list is malformed." |
| C-14 | Foreknowledge dual-token gate | **PASS** | Stage 3 emits COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED after all candidates evaluated — binary, not advisory. |
| C-15 | Pre-stage gate sequence map | **FAIL** | No top-level gate topology table before Stage 1. Vocabulary Declaration leads, then Stage 1 directly. |
| C-16 | Worked calibration example | **FAIL** | Stage 4 uses template placeholders only — no filled-in example instance. |
| C-17 | Named synonym exclusions | **PASS** | Six prohibited terms named in table: Reliability→Correctness, Performance→Scalability, Complexity→Correctness/Feasibility, Maintainability→Adoptability, Discoverability→Usability/Adoptability, Testability→Correctness/Feasibility. |

**Essential**: 5/5 × 60 = **60** | **Recommended**: 3/3 × 30 = **30** | **Aspirational**: 7/9 × 45 = **35**
**V-01 Composite: 125** | Golden: ✓

---

## V-02 — Lifecycle Emphasis (ENTER/EXIT per Stage)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Surprise orientation | **PASS** | Opening: "Not summaries. Not confirmations. Surprises — findings that contradicted or substantially extended the prior model." Stage 4 requires B-# reference. |
| C-02 | Symmetric Contract present | **PASS** | Stage 1 opening model + profile + ≥3 beliefs; Stage 6 verdict table with all required columns. |
| C-03 | Signal tracing | **PASS** | "Primary artifact: name, namespace, date. One source per entry. 'Multiple sources' is not acceptable." |
| C-04 | Design impact specificity | **PASS** | "Specific component, API, contract, flow, or decision affected. Full sentence. 'The system' or 'the design generally' is not acceptable." |
| C-05 | Adversarial gate executed | **PASS** | Five-check table; GATE-CONFIRMED/REJECTED tokens; binary foreknowledge gate present. |
| C-06 | Epistemic dimension compliance | **PASS** | Standalone vocabulary section; 5 canonical names declared; "Do not substitute. Any other term in a dimension cell is malformed." |
| C-07 | Minimum 2 surprises | **PASS** | Stage 3 EXIT: "If count < 2: halt, return to Stage 2, extend inventory, re-execute Stage 3." |
| C-08 | Cluster map actionability | **PASS** | "At least one row must name a specific skill (e.g., `/trace-contract`) or role — not 'investigate.'" |
| C-09 | Token protocol integrity | **PASS** | GATE-CONFIRMED names Stage 4; COMMIT-ENTRY per entry; Output: "All tokens present." |
| C-10 | Foreknowledge signal evaluated | **PASS** | Stage 6 Foreknowledge column; EXIT: "Every Stage 1 belief has a resolution row." Halt condition named. |
| C-11 | Stage 4 prose template format | **PASS** | Numbered prose blocks with labeled sub-fields. EXIT per entry enforces no table format. |
| C-12 | Stage 4 entry completeness | **PASS** | EXIT per entry: "No field is a fragment or a single noun phrase." Strongest explicit completeness enforcement across all variations. |
| C-13 | Closed-list dimension vocabulary | **PASS** | Standalone Vocabulary section before Stage 1; "These names are fixed. Do not substitute. Any other term in a dimension cell is malformed." |
| C-14 | Foreknowledge dual-token gate | **PASS** | Stage 3 EXIT: "COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED emitted" — binary structurally enforced. |
| C-15 | Pre-stage gate sequence map | **FAIL** | No top-level gate topology table. Vocabulary section leads, no gate map before Stage 1. |
| C-16 | Worked calibration example | **FAIL** | No filled-in Stage 4 example. Templates only. |
| C-17 | Named synonym exclusions | **FAIL** | Vocabulary section uses only "These names are fixed. Do not substitute." — general prohibition, no specific synonyms named. |

**Essential**: 5/5 × 60 = **60** | **Recommended**: 3/3 × 30 = **30** | **Aspirational**: 6/9 × 45 = **30**
**V-02 Composite: 120** | Golden: ✓

---

## V-03 — Output Format: Pre-Stage Gate Sequence Map

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Surprise orientation | **PASS** | "The single question this skill answers: What did we learn that we did not expect?" Stage 4 requires B-# reference per entry. |
| C-02 | Symmetric Contract present | **PASS** | Stage 1: opening model + profile + ≥3 beliefs. Stage 6: verdict table with all required resolution columns. |
| C-03 | Signal tracing | **PASS** | "[Artifact name, namespace, date. One specific source per entry.]" |
| C-04 | Design impact specificity | **PASS** | "[Specific component, API, contract, flow, or decision. Full sentence. Not 'the system.']" |
| C-05 | Adversarial gate executed | **PASS** | Five-check table; GATE-CONFIRMED names Stage 4; binary foreknowledge tokens; halt condition in Gate Sequence Overview. |
| C-06 | Epistemic dimension compliance | **PASS** | Vocabulary section: "These are the only valid names. Do not substitute." Stage 1 profile uses canonical names. |
| C-07 | Minimum 2 surprises | **PASS** | Gate Sequence Overview: Stage 3 halt — "GATE-CONFIRMED count < 2 after full sweep: halt, extend Stage 2, re-execute Stage 3." |
| C-08 | Cluster map actionability | **PASS** | "At least one row must name a specific skill (e.g., `/trace-permissions`) or role." |
| C-09 | Token protocol integrity | **PASS** | Token glossary in Gate Sequence Overview enumerates all tokens with semantics. GATE-CONFIRMED names Stage 4. COMMIT-ENTRY per entry. |
| C-10 | Foreknowledge signal evaluated | **PASS** | Stage 6 Foreknowledge column; "Refer to the Gate Sequence Overview for the FOREKNOWLEDGE-FLAGGED halt condition." Gate map makes halt explicit. |
| C-11 | Stage 4 prose template format | **PASS** | "write a numbered prose block." Sub-fields labeled. Prose block format enforced. |
| C-12 | Stage 4 entry completeness | **PASS** | "Full sentence" and "Not 'the system.'" instructions present. Template format precludes fragment entries. |
| C-13 | Closed-list dimension vocabulary | **PASS** | Standalone Vocabulary section before Stage 1: "These are the only valid names. Do not substitute." |
| C-14 | Foreknowledge dual-token gate | **PASS** | Stage 3 and Gate Sequence Overview both enumerate COMMIT-STAGE-3-CLEAN and COMMIT-STAGE-3-FLAGGED as binary alternatives. |
| C-15 | Pre-stage gate sequence map | **PASS** | "Gate Sequence Overview" table before Stage 1 enumerates all 6 stages with tokens and halt conditions. "Read this before Stage 1. It is the complete execution model for this skill." |
| C-16 | Worked calibration example | **FAIL** | No filled-in Stage 4 example. Templates only. |
| C-17 | Named synonym exclusions | **FAIL** | "Do not substitute" only — no specific prohibited synonyms named. |

**Essential**: 5/5 × 60 = **60** | **Recommended**: 3/3 × 30 = **30** | **Aspirational**: 7/9 × 45 = **35**
**V-03 Composite: 125** | Golden: ✓

---

## V-04 — Combined: Formal Register + Worked Calibration Example

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Surprise orientation | **PASS** | "Surprises only. A finding that confirms a prior belief is not a surprise and must not appear in Stage 4." Stage 4 requires B-# reference. |
| C-02 | Symmetric Contract present | **PASS** | Stage 1: opening model + epistemic profile + ≥3 beliefs. Stage 6: verdict table with Revision Direction and Foreknowledge columns. |
| C-03 | Signal tracing | **PASS** | Template: "[Artifact name, namespace, date. One primary source per entry.]" Calibration example shows: "`topic-registry-trace-contract-2026-02-14.md`, trace namespace, 2026-02-14." |
| C-04 | Design impact specificity | **PASS** | Template: "[Specific component, API, contract, flow, or decision affected. Full sentence.]" Calibration example: "The `/topic-story` skill must issue sequential per-namespace reads…" |
| C-05 | Adversarial gate executed | **PASS** | Five-check table; GATE-CONFIRMED-[N]: VALID — Stage 4.; binary foreknowledge gate. |
| C-06 | Epistemic dimension compliance | **PASS** | Vocabulary Declaration closed list; table uses canonical names only. |
| C-07 | Minimum 2 surprises | **PASS** | "Halt: if GATE-CONFIRMED count < 2, extend Stage 2 before proceeding." |
| C-08 | Cluster map actionability | **PASS** | "At least one row must name a specific skill or role." |
| C-09 | Token protocol integrity | **PASS** | GATE-CONFIRMED names Stage 4; COMMIT-ENTRY per entry; "All 6 stages in sequence. All tokens present." |
| C-10 | Foreknowledge signal evaluated | **PASS** | Stage 6 Foreknowledge column; "Halt condition: if any row is FOREKNOWLEDGE-FLAGGED, do not write the artifact. Name the flagged beliefs." |
| C-11 | Stage 4 prose template format | **PASS** | Calibration example is a prose block with labeled sub-fields. Template follows same format. |
| C-12 | Stage 4 entry completeness | **PASS** | Calibration example anchors quality: Signal Source is a specific artifact name+namespace+date; Design Impact is a full sentence naming `/topic-story` skill contract specifically. |
| C-13 | Closed-list dimension vocabulary | **PASS** | Standalone Vocabulary Declaration before Stage 1; "Any dimension cell containing a name not in the canonical list is malformed. Rewrite it before emitting the stage commit token." |
| C-14 | Foreknowledge dual-token gate | **PASS** | Stage 3: "No anticipated findings → COMMIT-STAGE-3-CLEAN" / "Any finding anticipated → COMMIT-STAGE-3-FLAGGED" — binary, enforced in Stage 3. |
| C-15 | Pre-stage gate sequence map | **FAIL** | No top-level gate topology table before Stage 1. Vocabulary Declaration leads directly into Stage 1. |
| C-16 | Worked calibration example | **PASS** | Complete filled-in "Surprise 0" instance with: realistic artifact reference (`topic-registry-trace-contract-2026-02-14.md`, trace namespace, 2026-02-14) and specific Design Impact naming `/topic-story` skill contract modification. Framed as "quality floor" not template. |
| C-17 | Named synonym exclusions | **PASS** | Six prohibited terms explicitly named: Reliability, Performance, Complexity, Maintainability, Discoverability, Testability — each with canonical substitute. |

**Essential**: 5/5 × 60 = **60** | **Recommended**: 3/3 × 30 = **30** | **Aspirational**: 8/9 × 45 = **40**
**V-04 Composite: 130** | Golden: ✓

---

## V-05 — Combined: Gate Map + Inertia Framing + Conversational Register

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Surprise orientation | **PASS** | "Just the surprises — the places where the signals came back different from what the team thought it knew." Stage 4 requires B-# reference. |
| C-02 | Symmetric Contract present | **PASS** | Stage 1: opening model + profile + ≥3 beliefs. Stage 6: verdict table with COHERENT/CONTRADICTORY/FOREKNOWLEDGE-FLAGGED + Foreknowledge column. |
| C-03 | Signal tracing | **PASS** | "Name the artifact — full name, namespace, date. One source per entry. 'Multiple sources' or 'several signals' is not acceptable." |
| C-04 | Design impact specificity | **PASS** | "Name the specific component, contract, flow, API, or decision. Complete sentence. 'The system' or 'the overall design' is not acceptable." |
| C-05 | Adversarial gate executed | **PASS** | Five-check table; GATE-CONFIRMED/REJECTED tokens; COMMIT-STAGE-3-CLEAN/FLAGGED binary; Gate Map reinforces halt. |
| C-06 | Epistemic dimension compliance | **PASS** | "Dimension Names (closed list — no substitutions)" section; Stage 1 profile table uses canonical names only. |
| C-07 | Minimum 2 surprises | **PASS** | "Check the Gate Map if fewer than 2 pass — you need to extend Stage 2 before proceeding." Gate Map shows Stage 3 halt condition. |
| C-08 | Cluster map actionability | **PASS** | "Named skill (e.g., `/flow-trigger`) or specific role — not 'investigate'" in table template; "At least one row needs a named next step." |
| C-09 | Token protocol integrity | **PASS** | Gate Map: "GATE-CONFIRMED-[N]: VALID — Stage 4." names destination. "All six COMMIT-STAGE-[N] tokens must appear in the artifact. A missing token means an incomplete run." |
| C-10 | Foreknowledge signal evaluated | **PASS** | Stage 6 Foreknowledge column; "Check the Gate Map for the FOREKNOWLEDGE-FLAGGED halt condition." Gate Map: "Any FOREKNOWLEDGE-FLAGGED belief: don't write the artifact." |
| C-11 | Stage 4 prose template format | **PASS** | Numbered prose blocks with labeled sub-fields (Surprise, Signal Source, Design Impact). Conversational framing does not change format structure. |
| C-12 | Stage 4 entry completeness | **PASS** | "Complete sentence." prohibitions for both fields; "Would the next engineer know exactly what to look at from this entry? If not, it's not ready." — pragmatic completeness heuristic reinforces C-12 from a utility angle. |
| C-13 | Closed-list dimension vocabulary | **PASS** | Standalone "Dimension Names (closed list — no substitutions)" section before Stage 1. |
| C-14 | Foreknowledge dual-token gate | **PASS** | Stage 3 binary tokens; Gate Map enumerates both COMMIT-STAGE-3-CLEAN and COMMIT-STAGE-3-FLAGGED with semantics. |
| C-15 | Pre-stage gate sequence map | **PASS** | "Before You Start: Gate Map" table enumerating all 6 stages — what happens, what gets emitted, what can stop you. Placed before Stage 1 with "Read it once before Stage 1." |
| C-16 | Worked calibration example | **FAIL** | No filled-in Stage 4 example. Prose instructions and heuristic check only. |
| C-17 | Named synonym exclusions | **PASS** | "Not 'Reliability' — that's Correctness. Not 'Performance' — that's Scalability. Not 'Maintainability' — that's Adoptability." Three prohibited synonyms named alongside general "replace it" rule. |

**Essential**: 5/5 × 60 = **60** | **Recommended**: 3/3 × 30 = **30** | **Aspirational**: 8/9 × 45 = **40**
**V-05 Composite: 130** | Golden: ✓

---

## Round 4 Rankings

| Rank | Variation | Score | Golden | Aspirational Pass | Unique strength |
|------|-----------|-------|--------|-------------------|-----------------|
| 1 (tie) | **V-04** | **130** | ✓ | C-09–C-14 + C-16 + C-17 (8/9) | C-16 + C-17 together; calibration example anchors quality to domain reality |
| 1 (tie) | **V-05** | **130** | ✓ | C-09–C-15 + C-17 (8/9) | C-15 + C-17; inertia framing sharpens CONTRADICTORY detection; utility heuristic in Stage 4 |
| 3 (tie) | **V-01** | **125** | ✓ | C-09–C-14 + C-17 (7/9) | Deepest synonym table (6 prohibited terms); strongest register discipline |
| 3 (tie) | **V-03** | **125** | ✓ | C-09–C-15 (7/9) | Gate map with full token glossary; cross-references from Stage 3 and Stage 6 back to map |
| 5 | **V-02** | **120** | ✓ | C-09–C-14 (6/9) | Strongest per-entry completeness enforcement (EXIT per entry with "no fragment" rule) |

---

## Excellence Signals from Top Scorers

**Why V-04 and V-05 each reach 130 while V-01 and V-03 stop at 125:**

The 5-point gap is the second new aspirational criterion each unlocks. V-01 has C-17 but not C-15 or C-16. V-03 has C-15 but not C-16 or C-17. V-04 adds C-16 to C-17. V-05 adds C-15 to C-17.

**V-04 excellence signal — calibration example self-reference:**
The worked Surprise 0 uses a real Signal-domain artifact name (`topic-registry-trace-contract-2026-02-14.md`, trace namespace, 2026-02-14) and names a specific plugin skill (`/topic-story`). The example is not a generic fill-in — it instantiates the domain vocabulary the model will be working in. This means the quality bar is anchored to an instance that looks like what real output should look like, not a placeholder like "[full sentence here]."

**V-05 excellence signal — inertia baseline framing:**
Stage 1 reframed as "write down the inertia baseline — what the team would have shipped if no signals had been gathered" gives the model a concrete foil for CONTRADICTORY verdicts in Stage 6. "What we believed" is abstract; "what we would have shipped" is a concrete decision that signals can directly overturn. This sharpens C-01 execution probability without adding a new structural requirement.

**V-05 excellence signal — Stage 4 utility self-check:**
"Would the next engineer know exactly what to look at from this entry? If not, it's not ready." This is a pragmatic readability gate embedded in Stage 4 that enforces C-12 from a utility angle rather than a format-compliance angle. A model following format rules can still produce thin entries that satisfy the template; a model applying this heuristic must ask whether the entry is actually useful.

**Missing combination — Round 5 target:**
No Round 4 variation achieved C-15 + C-16 + C-17 simultaneously. V-04 has C-16 + C-17 (missing C-15). V-05 has C-15 + C-17 (missing C-16). A variation combining the gate map (V-03/V-05), the domain-anchored calibration example (V-04), and named synonym exclusions (V-01/V-04/V-05) would be the first to achieve all three new aspirational criteria and could reach 135/135.

---

```json
{"top_score": 130, "all_essential_pass": true, "new_patterns": ["Inertia baseline framing for Stage 1 — reframing prior beliefs as 'what the team would have shipped without signals' gives the model a concrete decision-foil for CONTRADICTORY verdicts, sharpening C-01 execution without adding structural requirements", "Stage 4 utility self-check — 'Would the next engineer know exactly what to look at from this entry? If not, it's not ready' enforces C-12 completeness from a pragmatic usefulness angle rather than format-compliance alone, catching entries that satisfy template structure but are semantically thin"]}
```
