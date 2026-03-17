Now I have the full picture. Let me score all 5 variations against the v3 rubric.

---

# Quest Scorecard — topic-achievements — Round 3

**Rubric**: v3 (2026-03-17) — 15 criteria: 5 essential (60 pts), 3 recommended (30 pts), 7 aspirational (10 pts)

**Scoring formula**: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/7 × 10)`

---

## Criterion Reference

| ID | Tier | What it tests |
|----|------|---------------|
| C-01 | Essential | One state per achievement |
| C-02 | Essential | Falsified named as honesty signal |
| C-03 | Essential | Artifact-grounded classification |
| C-04 | Essential | In-progress shows numeric progress |
| C-05 | Essential | Next recommended action is specific |
| C-06 | Recommended | All 7 categories represented |
| C-07 | Recommended | Earned achievements carry dates |
| C-08 | Recommended | Locked achievements state unlock conditions |
| C-09 | Aspirational | Maturity synthesis before classification |
| C-10 | Aspirational | Falsified framed as positive signal |
| C-11 | Aspirational | State-column isolation |
| C-12 | Aspirational | Consequence clause present for Falsified |
| C-13 | Aspirational | Escape hatch / evidence fallback instruction |
| C-14 | Aspirational (new v3) | Consequence clause names specific canonical evasion path |
| C-15 | Aspirational (new v3) | Fallback declared as unconditional minimum (positive floor, not conditional fallback) |

---

## V-01 — Phrasing Register: Formal Imperative with Consequence Contracts

**Axis**: Formal imperative phrasing with explicit pass/fail contracts per output field. Includes the evasion surface named in the consequence clause. Fallback wrapped in conditional trigger.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | "State column uses exactly one of the three values: EARNED, IN-PROGRESS, LOCKED. Do not combine states in a row or use any other value." |
| C-02 | PASS | "The Falsified state MUST be framed as evidence of investigative rigor: 'followed evidence over assumptions' or equivalent." |
| C-03 | PASS | EARNED rule: "Cite the specific artifact(s)"; IN-PROGRESS rule cites partial artifact or count from Step 1 scan |
| C-04 | PASS | Step 2: "Express progress as `n of m` (e.g., '3 of 5 namespaces covered'). Qualitative descriptions ('partially done') fail this field." Also enforced in Step 3 rules. |
| C-05 | PASS | Step 4 has explicit three-check gate: names exact skill, artifact produced, achievement(s) advanced. Format template enforces all three. |
| C-06 | PASS | Table template pre-prints all 7 rows |
| C-07 | PASS | "EARNED rows must include the artifact path and date. A date-less EARNED row fails." |
| C-08 | PASS | "LOCKED rows must name the exact artifact type or action required. 'Not yet started' without specifics fails." |
| C-09 | FAIL | No maturity synthesis step before classification. The Falsified contract is inline to Step 2; no required narrative summary before the table. |
| C-10 | PASS | Falsified contract requires framing as investigative rigor. Table template LOCKED example includes invitational framing. |
| C-11 | PASS | Table with dedicated State column; one-value enforcement explicit |
| C-12 | PASS | Consequence clause present: "Framing falsification as absence, failure, or lack of evidence fails this requirement" |
| C-13 | PASS | Escape hatch present: "When evidence for Falsified is uncertain or partially present, namespace-level evidence from the `prove` namespace is always acceptable and is the safe floor" |
| C-14 | PASS | Evasion surface named verbatim: "fails this requirement — including as a closing reflection that notes the topic 'did not yield a falsification result.'" |
| C-15 | FAIL | Floor declaration wrapped in conditional trigger: "**When evidence for Falsified is uncertain or partially present**... is always acceptable and is the safe floor." The "when uncertain" framing classifies the floor as a conditional fallback, not a positive unconditional minimum. The declaration criterion requires the floor to stand on its own, without a conditional governing it. |

**Essential**: 5/5 → 60 pts | **Recommended**: 3/3 → 30 pts | **Aspirational**: 5/7 → 7.14 pts

**Composite: 97.14** — Gold

---

## V-02 — Output Format: Pre-Printed Template Skeleton

**Axis**: Pre-printed table with all critical text — consequence clause, evasion surface, and floor declaration — embedded verbatim in template cells. Model fills placeholders only.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Each row carries exactly one of `EARNED / IN-PROGRESS / LOCKED`; the template structure prevents combining states |
| C-02 | PASS | EARNED template: "followed evidence over assumptions: [brief evidence of hypothesis revision]" — positive framing pre-printed |
| C-03 | PASS | EARNED fill rule: "fill the evidence field with the artifact path and date"; IN-PROGRESS fill requires actual count from scan |
| C-04 | PASS | IN-PROGRESS template has `[N] of [M]` scaffold. Rule: "Do not fill an IN-PROGRESS row without `n of m` notation. Qualitative-only text fails." |
| C-05 | PASS | Next Action template pre-prints skill, artifact, and category/achievement slots; generic fills are explicitly prohibited |
| C-06 | PASS | All 7 rows pre-printed in template; model cannot omit a category |
| C-07 | PASS | "Do not fill an EARNED row without a date. A date-less EARNED detail fails." |
| C-08 | PASS | LOCKED detail text is pre-printed with specific unlock conditions per row |
| C-09 | FAIL | No synthesis step before classification. Template starts directly with the table; SCAN leads immediately to template fill. |
| C-10 | PASS | EARNED Falsified template pre-prints "followed evidence over assumptions" framing |
| C-11 | PASS | Dedicated State column; template enforces column structure |
| C-12 | PASS | Consequence clause pre-printed in Falsified LOCKED cell: "Framing falsification as absence or lack of evidence... does not earn this achievement." |
| C-13 | PASS | Fallback instruction pre-printed: "Namespace-level evidence from the prove namespace is always acceptable and is the safe floor." |
| C-14 | PASS | Evasion surface pre-printed verbatim in the Falsified LOCKED cell: "including as a closing reflection." Cannot be omitted — it is pre-printed text the model cannot change. |
| C-15 | PASS | Floor declaration pre-printed as standalone sentence with no conditional governing it: "Namespace-level evidence from the prove namespace is always acceptable and is the safe floor." Unconditional positive declaration, not conditional fallback. |

**Essential**: 5/5 → 60 pts | **Recommended**: 3/3 → 30 pts | **Aspirational**: 6/7 → 8.57 pts

**Composite: 98.57** — Gold

---

## V-03 — Lifecycle Emphasis: Four Named Phases with Gate Contracts

**Axis**: Explicit SCAN → CLASSIFY → STATE → RECOMMEND phases with gate outputs. Falsified fallback declared at phase-contract level. Floor language is unconditional in body but introduced by a conditional section label.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | STATE phase: "assign exactly one state to each achievement" |
| C-02 | PASS | Falsified state rule: "must frame this as investigative rigor ('followed evidence over assumptions'), never as absence or failure" |
| C-03 | PASS | EARNED must "Cite at least one artifact by filename and date" from the CLASSIFY LOG |
| C-04 | PASS | STATE phase: "Express progress as `n of m`. Qualitative-only text ('partially done') fails." |
| C-05 | PASS | RECOMMEND phase: explicit three-check gate before writing |
| C-06 | PASS | STATE output template pre-prints all 7 rows |
| C-07 | PASS | EARNED: "Cite at least one artifact by filename and date" |
| C-08 | PASS | LOCKED: "State the specific artifact type or count required" |
| C-09 | PASS | CLASSIFY phase runs before STATE phase; artifacts are fully classified and committed to CLASSIFY LOG before any state is assigned. Phase gate enforces this. |
| C-10 | PASS | Falsified state rule requires EARNED description to "frame this as investigative rigor" and prohibits absence/failure framing |
| C-11 | PASS | TABLE format with dedicated State column in STATE phase output |
| C-12 | PASS | Consequence clause: "Framing Falsified as absence, failure, or a reflection on what the investigation did not yield... fails this rule." |
| C-13 | PASS | Fallback present: "Namespace-level evidence from the `prove` namespace is always acceptable and is the safe floor." |
| C-14 | PASS | Evasion surface named: "Framing Falsified as absence, failure, or a reflection on what the investigation did not yield — **including as a closing reflection** — fails this rule." |
| C-15 | FAIL | Floor introduced as a labeled fallback section: "**Fallback for uncertain Falsified evidence**: Namespace-level evidence from the `prove` namespace is always acceptable and is the safe floor." The section header "Fallback for uncertain Falsified evidence" frames the floor as conditional on uncertainty. The body uses unconditional language ("always acceptable") but the conditional header governs interpretation — the model reads this as a rule that applies when evidence is uncertain, not as a universal floor. The distinction C-15 requires is a positive declaration that stands structurally independent from any conditional trigger. |

**Essential**: 5/5 → 60 pts | **Recommended**: 3/3 → 30 pts | **Aspirational**: 6/7 → 8.57 pts

**Composite: 98.57** — Gold

---

## V-04 — Role Sequence + Lifecycle (Combination)

**Axis**: Two-role separation: Artifact Analyst (evidence record only, no states) → Achievement Classifier (states from Role 1 record only). Both C-14 and C-15 targets are role-level contracts in the Classifier role.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Role 2: "assign exactly one state (EARNED, IN-PROGRESS, or LOCKED) to each of the 7 achievements" |
| C-02 | PASS | Role 2 Falsified contract: "The EARNED detail must frame this as investigative rigor: the team 'followed evidence over assumptions.'" |
| C-03 | PASS | Role 2 rule: "The Role 1 evidence record contains all required artifacts. Cite the filename and date." All state assignments trace to Role 1 evidence. |
| C-04 | PASS | "A row that says 'partially done' or 'underway' without numeric notation fails." |
| C-05 | PASS | Role 2 next-action checks: names exact skill, artifact, category and achievement name |
| C-06 | PASS | Achievement table pre-prints all 7 rows |
| C-07 | PASS | "A date-less EARNED citation fails." |
| C-08 | PASS | "A row that says 'not yet started' without specifics fails." |
| C-09 | PASS | Role 1 produces a complete evidence record before Role 2 begins. Role 2 cannot re-scan. The separation is structural, not just instructional. |
| C-10 | PASS | Falsified contract in Role 2: "It must describe the revision event, not the investigation's completeness." Framing as absence explicitly prohibited. |
| C-11 | PASS | Dedicated State column in Role 2 achievement table |
| C-12 | PASS | Consequence clause in Role 2 Falsified contract: "Framing Falsified as absence, as a goal not reached, or as a reflection on what the investigation did not find... fails this contract." |
| C-13 | PASS | Escape hatch present in Role 2: "Namespace-level evidence from the `prove` namespace is always acceptable and is the safe floor." |
| C-14 | PASS | Evasion surface named explicitly: "Framing Falsified... as a reflection on what the investigation did not find — **including as a closing reflection appended to the synthesize output** — fails this contract." |
| C-15 | PASS | Floor declaration is a standalone sentence, structurally independent: "Namespace-level evidence from the `prove` namespace is always acceptable and is the safe floor." No conditional trigger precedes or governs it. Pure positive declaration — the model reads this as a universal rule, not a conditional one. |

**Essential**: 5/5 → 60 pts | **Recommended**: 3/3 → 30 pts | **Aspirational**: 7/7 → 10 pts

**Composite: 100** — Platinum

---

## V-05 — Golden Synthesis: Pre-Printed Template + Phase Gates + Pre-Printed Falsified Block

**Axes**: Pre-printed skeleton + lifecycle phases + verbatim C-14/C-15 text in the template. Model fills placeholders; all structural compliance text is pre-printed.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Template enforces one state per row; fill is `[EARNED / IN-PROGRESS / LOCKED]` — one value |
| C-02 | PASS | EARNED Falsified template pre-prints "followed evidence over assumptions: [REVISION_EVENT]" |
| C-03 | PASS | EARNED fill rule: "fill `[EARNED_ARTIFACT]` with `filename — date`." All EARNED fills trace to scan. |
| C-04 | PASS | IN-PROGRESS fill: "fill `[N]` and `[M]` with the actual count and total. 'Partial' without numbers fails." |
| C-05 | PASS | Next Action template pre-prints skill, artifact, category, state — requires filling `[SKILL]`, `[ITEM]`, `[SPECIFIC_GAP]` |
| C-06 | PASS | All 7 rows pre-printed; model cannot omit a category |
| C-07 | PASS | "A date-less fill fails." |
| C-08 | PASS | LOCKED detail text is pre-printed with specific unlock conditions per category |
| C-09 | PASS | CLASSIFY GATE runs before Phase 3 (FILL TEMPLATE); artifacts are classified and committed before states are assigned |
| C-10 | PASS | EARNED Falsified template pre-prints the positive framing anchor ("followed evidence over assumptions") — model fills evidence, not framing |
| C-11 | PASS | Pre-printed table with dedicated State column |
| C-12 | PASS | Consequence clause pre-printed in Falsified LOCKED cell: "Framing falsification as absence or as a result the investigation did not yield... does not earn this achievement." |
| C-13 | PASS | Fallback pre-printed in Falsified LOCKED cell: "Namespace-level evidence from the prove namespace is always acceptable and is the safe floor." |
| C-14 | PASS | Evasion surface pre-printed verbatim: "including as a closing reflection." Mechanically unavoidable — pre-printed text the model cannot omit or rewrite. |
| C-15 | PASS | Floor declaration pre-printed as a standalone sentence: "Namespace-level evidence from the prove namespace is always acceptable and is the safe floor." No conditional trigger in the pre-printed text. Strongest structural guarantee of all five variations: the model cannot inadvertently wrap it in a conditional because the surrounding text is pre-printed. |

**Essential**: 5/5 → 60 pts | **Recommended**: 3/3 → 30 pts | **Aspirational**: 7/7 → 10 pts

**Composite: 100** — Platinum

---

## Scorecard Summary

| Rank | Variation | Essential | Recommended | Aspirational | Score | Grade |
|------|-----------|-----------|-------------|--------------|-------|-------|
| 1 | V-04 Role Sequence + Lifecycle | 5/5 | 3/3 | 7/7 | **100** | Platinum |
| 1 | V-05 Golden Synthesis | 5/5 | 3/3 | 7/7 | **100** | Platinum |
| 3 | V-02 Pre-Printed Template | 5/5 | 3/3 | 6/7 | **98.57** | Gold |
| 3 | V-03 Lifecycle Phases | 5/5 | 3/3 | 6/7 | **98.57** | Gold |
| 5 | V-01 Formal Imperative | 5/5 | 3/3 | 5/7 | **97.14** | Gold |

**All 5 variations pass all essential and recommended criteria.** The spread is entirely in C-09 and C-15.

---

## Discriminator Analysis

### C-15 — the dominant discriminator

The single rule separating Platinum from Gold is whether the floor declaration stands structurally independent from any conditional trigger:

| Variation | C-15 mechanism | Structural form | Result |
|-----------|---------------|-----------------|--------|
| V-05 | Pre-printed standalone sentence | No surrounding context | PASS |
| V-04 | Standalone sentence in role contract | No conditional trigger | PASS |
| V-03 | Unconditional body under conditional label | "Fallback for uncertain evidence: …always acceptable" | FAIL — label governs body |
| V-02 | Pre-printed sentence in LOCKED cell | No conditional trigger | PASS |
| V-01 | Body inside conditional clause | "When uncertain… always acceptable" | FAIL — "when" is the trigger |

The pattern: **the floor declaration must stand alone**. When the sentence containing "always acceptable and is the safe floor" is embedded in a conditional clause or introduced by a conditional section label, the model reads it as a conditional rule. The criterion requires the positive declaration to be structurally independent.

### C-09 — secondary discriminator

V-01 and V-02 also fail C-09 (synthesis / classification phase separation). Neither includes a distinct step that requires the model to commit to an evidence record before assigning states. V-03/V-04/V-05 all enforce this via phase gates (CLASSIFY before STATE) or role separation (Analyst before Classifier). This costs V-01 one additional aspirational point.

### Within the Platinum cluster

V-04 and V-05 score identically. V-05 has stronger mechanical guarantees (pre-printed text cannot be omitted or conditionally wrapped), while V-04's role separation is structurally elegant for preventing state contamination. Neither shows a defect the other would surface; the difference is generation-risk tolerance vs architectural clarity.

---

## Excellence Signals from the Platinum Cluster

**Signal 1 — Floor isolation from conditionals (V-04, V-05).** The C-15 floor is effective when the sentence is a standalone positive declaration. Both V-04 and V-05 write the floor sentence without any surrounding clause, while V-01 and V-03 embed identical language inside a conditional context. This confirms that C-15 compliance is not about the words "always acceptable" — it is about whether those words appear inside or outside a conditional frame. A v4 criterion could target *declaration isolation*: requiring the floor to appear as its own sentence with no conditional governing it.

**Signal 2 — State count audit trail in frontmatter (V-05 exclusive).** V-05 writes `earned: [n]`, `in_progress: [n]`, `locked: [n]` into the artifact frontmatter. This creates a machine-readable summary that makes the STATE GATE output durable beyond the conversation. No other variation captures post-run state distribution in the artifact itself. Candidate criterion: *artifact frontmatter includes EARNED/IN-PROGRESS/LOCKED distribution counts, enabling downstream aggregation without parsing the table.*

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Floor isolation from conditionals: C-15 compliance depends on the floor sentence appearing structurally independent — not inside a 'when uncertain' clause or under a conditional section label. Identical floor language fails when embedded in a conditional context and passes when it stands alone.", "State count audit trail in frontmatter: writing earned/in_progress/locked distribution counts into the artifact YAML frontmatter makes the STATE GATE result durable and machine-readable for downstream aggregation, without parsing the achievement table."]}
```
