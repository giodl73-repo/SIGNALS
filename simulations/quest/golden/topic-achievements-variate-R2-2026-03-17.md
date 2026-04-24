---
skill: quest-variate
skill_target: topic-achievements
topic: topic-achievements
item: variate
date: 2026-03-17
round: 2
rubric: simulations/quest/rubrics/topic-achievements-rubric-v2-2026-03-17.md
---

# Quest Variate — topic-achievements — Round 2

**Skill description**: Scan all signal artifacts for a topic and compute earned achievements. Shows: earned (with date), in-progress (how close), locked (what still needs doing), next recommended action. Categories: exploration, depth, coverage, quality, chain, discovery, corps/crew. The Falsified achievement is the most important -- it rewards intellectual honesty. Surfaces automatically in topic-status; run directly for the full achievement picture.

**Rubric version**: v2 (13 criteria, 3 tiers — 3 new aspirational: C-11 state-column isolation, C-12 synthesis placement boundary, C-13 hallucination-safe fallback)

**Round 1 baseline**: V-02 (table-primary grid) scored 100 and supplied all three new criteria. The excellence signals extracted were: (1) table-column state enforcement, (2) synthesis placement boundary rule ("not buried at the end"), (3) hallucination escape hatch ("if unsure, cite namespace only"). R2 goal: isolate each new axis, then combine, to confirm each mechanism is independently necessary and jointly sufficient.

**Variation strategy**: 3 single-axis variations targeting C-11 (V-01), C-12 (V-02), C-13 (V-03), then two combinations: C-11+C-12 (V-04), all three (V-05).

**Baseline** (what each single-axis variation varies FROM): a prose-classification prompt that passes C-01 through C-10 — all essential, all recommended, and both old-aspirational — but has no state column (C-11 absent), no explicit placement boundary rule (C-12 borderline), and no namespace escape hatch (C-13 absent).

---

## V-01 — Axis: Output Format (C-11 target: State-Column Isolation)

**Hypothesis**: Adding a dedicated State column to the achievement output is the minimum change that passes C-11. Prose-embedded states ("this achievement is EARNED based on...") require parsing to verify one-state-per-achievement; a column allows verification by scanning a single axis. If V-01 passes C-11 while holding C-12 at baseline (directive synthesis ordering, no explicit boundary rule) and failing C-13 (no escape hatch), state-column structure is independently sufficient for C-11. The mechanism is format-structural — no consequence clauses required.

---

Glob `simulations/**/{topic}-*` to discover every signal artifact for this topic. Record namespace, skill, and date for each.

**Step 1 — Artifact Inventory**

List every artifact found. Group by namespace. Note total artifact count and unique namespace count.

If no artifacts are found, report: "No artifacts found for `{topic}`." Skip Step 2 and Step 3. Proceed to Step 4 with a first-step recommendation.

**Step 2 — Maturity Synthesis**

Before classifying any achievement, write 1-3 sentences interpreting what the artifact inventory reveals about this topic's investigative maturity. Name the strongest dimension and the most significant gap.

**Step 3 — Achievement Table**

Using only the artifacts from Step 1, classify achievements across all 7 categories: **exploration, depth, coverage, quality, chain, discovery, corps/crew**.

Present results as a table with columns: `Category | Achievement | State | Evidence / Progress | Date`

**State column** — write exactly one of the following per row:
- `EARNED` — Evidence: cite the artifact from Step 1 by namespace/skill. Date: earned date.
- `IN-PROGRESS` — Evidence: numeric progress in `n of m` form (e.g., "3 of 5 namespaces covered"). Date: blank.
- `LOCKED` — Evidence: the specific unlock condition (artifact type, count, or action required). Date: blank.

Every category must appear. If a category has no achievements to classify, include a row with `—` in Achievement, `LOCKED` in State, and the first unlock step in Evidence.

The **Falsified** achievement belongs in the **chain** category. It is earned when any artifact records a retracted hypothesis or amended belief. Classify it in the State column using the same rule. Add a framing note below the row: Falsified is the achievement that proves intellectual honesty — it means the investigation was rigorous enough to follow evidence over assumptions. If not yet earned, frame this as an open invitation.

**Step 4 — Next Recommended Action**

State one specific next action: the skill to invoke, the artifact it would produce, and which achievement(s) it would advance toward EARNED.

Write artifact to: none (terminal display only)

---

## V-02 — Axis: Lifecycle Emphasis (C-12 target: Synthesis Placement Boundary)

**Hypothesis**: The critical gap between C-09 (synthesis present) and C-12 (synthesis placement boundary) is whether the prompt treats position as a requirement with a stated failure mode, not just as an ordering preference. A directive like "write synthesis first" relies on the model honoring step order under normal conditions; a boundary rule like "placement after per-category detail fails this requirement" makes the wrong position visibly non-compliant. If V-02 achieves a higher C-12 compliance signal than V-01 while using prose output (no State column, C-11 absent) and no escape hatch (C-13 absent), the placement boundary rule is the mechanism — not table structure or evidence framing. The inertia hypothesis: models in list-completion mode tend to append synthesis at the end; an explicit consequence breaks that default.

---

Glob `simulations/**/{topic}-*` to discover every signal artifact for this topic. Record namespace, skill, and date for each.

**Step 1 — Artifact Inventory**

List every artifact found. Group by namespace. Note total artifact count and unique namespace count.

If no artifacts found: "No artifacts for `{topic}`." Skip Steps 2 and 3. Proceed to Step 4 with a first-step recommendation.

**Step 2 — Maturity Synthesis**

Write 1-3 sentences interpreting what the artifact inventory reveals about this topic's investigative maturity. Name the strongest dimension and the most significant gap.

**Placement rule**: This paragraph must appear before the first category section below. Placement after per-category classification — including as a closing reflection — fails this requirement. The synthesis is the interpretive frame; per-category detail fills it in.

**Step 3 — Category Classification**

Using only the artifacts from Step 1, classify achievements across all 7 categories: **exploration, depth, coverage, quality, chain, discovery, corps/crew**.

For each achievement, assign exactly one state:
- **EARNED** — cite the artifact from Step 1 by namespace and skill; include the date earned
- **IN-PROGRESS** — state numeric progress as `n of m` (e.g., "3 of 5 namespaces covered"); no vague language
- **LOCKED** — state the specific unlock condition (artifact type, count, or action)

Every category must appear. Write "No achievements yet in this category" if empty.

The **Falsified** achievement is a named entry in the **chain** category. It is earned when any artifact records a retracted hypothesis or amended belief. Classify it using the same EARNED/IN-PROGRESS/LOCKED schema. Add a framing sentence: Falsified is the achievement that proves the investigation was honest — earning it means the team followed the evidence, not their assumptions. If not yet earned, frame it as an open invitation.

**Step 4 — Next Recommended Action**

State one specific next action: the skill to invoke, the artifact it would produce, and which achievement(s) it would advance toward EARNED.

Write artifact to: none (terminal display only)

---

## V-03 — Axis: Phrasing Register (C-13 target: Hallucination-Safe Evidence Fallback)

**Hypothesis**: Adding an explicit escape hatch — "if evidence is uncertain, cite the namespace or skill only; never invent an artifact name" — is the minimum instruction needed to pass C-13. Without this clause, models under uncertainty face a false binary: fabricate a specific artifact or say nothing. The escape hatch breaks the forced-hallucination dynamic by naming namespace-level evidence as an acceptable and explicitly preferred alternative. If V-03 passes C-13 using only this clause (no table, no explicit placement boundary) while prose output (C-11 absent) and baseline synthesis ordering (C-12 structural pass) hold constant, the escape hatch is independently sufficient for C-13. The register matters: the clause must be framed as a positive permission ("cite the namespace only"), not just a prohibition.

---

Glob `simulations/**/{topic}-*` to discover every signal artifact for this topic. Record namespace, skill, and date for each.

**Step 1 — Artifact Inventory**

List every artifact found. Group by namespace. Note total artifact count and unique namespace count.

If no artifacts found: "No artifacts for `{topic}`." Skip Steps 2 and 3. Proceed to Step 4 with a first-step recommendation.

**Step 2 — Maturity Synthesis**

Before classifying any achievement, write 1-3 sentences interpreting what the artifact inventory reveals about this topic's investigative maturity. Name the strongest dimension and the most significant gap.

**Step 3 — Category Classification**

Using only the artifacts from Step 1, classify achievements across all 7 categories: **exploration, depth, coverage, quality, chain, discovery, corps/crew**.

For each achievement, assign exactly one state:
- **EARNED** — cite the artifact from Step 1 by namespace and skill; include the date earned
- **IN-PROGRESS** — state numeric progress as `n of m` (e.g., "3 of 5 namespaces covered"); no vague language
- **LOCKED** — state the specific unlock condition (artifact type, count, or action)

**Evidence citation rule**: All EARNED and IN-PROGRESS evidence must draw only from the Step 1 artifact inventory. When evidence is uncertain — when you are not sure which specific artifact supports a claim — cite the namespace or skill only (e.g., "namespace: flow" or "skill: scout-competitors"). Do not invent an artifact name to satisfy citation requirements. Namespace-level evidence is always acceptable and is the safe floor when specifics are unclear.

Every category must appear. Write "No achievements yet in this category" if empty.

The **Falsified** achievement is a named entry in the **chain** category. It is earned when any artifact records a retracted hypothesis or amended belief. Classify it using the same EARNED/IN-PROGRESS/LOCKED schema. Add a framing sentence: Falsified is the achievement that proves intellectual honesty — the investigation followed evidence, not assumptions. If not yet earned, frame it as an open invitation.

**Step 4 — Next Recommended Action**

State one specific next action: the skill to invoke, the artifact it would produce, and which achievement(s) it would advance toward EARNED.

Write artifact to: none (terminal display only)

---

## V-04 — Combination: Output Format + Lifecycle Emphasis (C-11 + C-12)

**Hypothesis**: Pairing the State column (C-11) with the explicit placement boundary rule (C-12) tests whether the two mechanisms compound without C-13. The prediction is V-04 scores identically to V-01, V-02, and V-03 (98 if the scoring formula is symmetric) — neither better nor worse than the single-axis variations — because the three new criteria carry equal weight and the absent mechanism (C-13) is worth the same as any other absent aspirational. If V-04 scores significantly higher than either single-axis variant, there is a synergy between table structure and placement framing beyond the additive model. Falsified is held at baseline (named in chain category, positively framed, not structurally isolated). No escape hatch.

---

Glob `simulations/**/{topic}-*` to discover every signal artifact for this topic. Record namespace, skill, and date for each.

**Step 1 — Artifact Inventory**

List every artifact found: namespace, skill, date. Group by namespace. Note total artifact count and unique namespace count.

If no artifacts found: "No artifacts for `{topic}`." Skip Steps 2 and 3. Proceed to Step 4 with a first-step recommendation.

**Step 2 — Maturity Synthesis**

Write 1-3 sentences interpreting what the artifact inventory reveals about this topic's investigative maturity. Name the strongest dimension and the most significant gap.

**Placement rule**: This paragraph must appear before the first row of the achievement table in Step 3. Placement after the table — or as a closing paragraph — fails this requirement. The synthesis frames what the table fills in; the order is not optional.

**Step 3 — Achievement Table**

Using only the artifacts from Step 1, classify achievements across all 7 categories: **exploration, depth, coverage, quality, chain, discovery, corps/crew**.

Present as a table with columns: `Category | Achievement | State | Evidence / Progress | Date`

**State column** — write exactly one of the following per row:
- `EARNED` — Evidence: cite the artifact from Step 1 by namespace/skill. Date: earned date.
- `IN-PROGRESS` — Evidence: numeric progress in `n of m` form. Date: blank.
- `LOCKED` — Evidence: specific unlock condition (artifact type, count, or action). Date: blank.

Every category must appear. If a category has no achievements, include a row with `—` in Achievement, `LOCKED` in State, and the first unlock step in Evidence.

The **Falsified** achievement belongs in the **chain** category. It is earned when any artifact records a retracted hypothesis or amended belief. Classify it in the State column using the same rule. Add a framing note below the Falsified row: Falsified is proof of intellectual honesty — the investigation was rigorous enough to follow evidence over assumptions. If not yet earned, frame it as an open invitation, not a deficit.

**Step 4 — Next Recommended Action**

One specific recommendation: skill to invoke, artifact it produces, achievement(s) it advances toward EARNED.

Write artifact to: none (terminal display only)

---

## V-05 — Combination: All Three Axes (C-11 + C-12 + C-13)

**Hypothesis**: Combining all three mechanisms — State column (C-11), explicit placement boundary (C-12), and namespace escape hatch (C-13) — should reproduce the R1 V-02 Gold score under the v2 rubric. The risk being tested is whether the three additions together create enough instructional surface area to crowd out attention to essentials. If V-05 achieves all 5 aspirational criteria without degrading essential compliance (all 5 essential pass), the mechanisms are compositionally safe — they can coexist without the prompt becoming too long or complex to follow reliably. A secondary test: does the explicit C-12 placement rule interact positively with the C-11 table structure? The table column enforces state; the placement boundary enforces framing order; the escape hatch enforces evidence honesty. Together they target the three most common output-quality failure modes.

---

Glob `simulations/**/{topic}-*` to discover every signal artifact for this topic. Record namespace, skill, and date for each.

**Step 1 — Artifact Inventory**

List every artifact found: namespace, skill, date. Group by namespace. Note total artifact count and unique namespace count.

If no artifacts found: "No artifacts for `{topic}`." Skip Steps 2 and 3. Proceed to Step 4 with a first-step recommendation.

**Step 2 — Maturity Synthesis**

Write 1-3 sentences interpreting what the artifact inventory reveals about this topic's investigative maturity. Name the strongest dimension and the most significant gap.

**Placement rule**: This paragraph must appear before the first row of the achievement table in Step 3. Placement after the table fails this requirement — synthesis written as a closing reflection is not acceptable regardless of its quality. Position determines compliance.

**Step 3 — Achievement Table**

Using only the artifacts from Step 1, classify achievements across all 7 categories: **exploration, depth, coverage, quality, chain, discovery, corps/crew**.

Present as a table with columns: `Category | Achievement | State | Evidence / Progress | Date`

**State column** — write exactly one of the following per row:
- `EARNED` — Evidence: cite the artifact from Step 1 by namespace/skill. Date: earned date.
- `IN-PROGRESS` — Evidence: numeric progress in `n of m` form (e.g., "3 of 6 namespaces covered"). Date: blank.
- `LOCKED` — Evidence: specific unlock condition (artifact type, count, or action required). Date: blank.

Every category must appear. If a category has no achievements, include a row with `—` in Achievement, `LOCKED` in State, and the first unlock step in Evidence.

**Evidence citation rule**: All EARNED and IN-PROGRESS evidence must draw only from the Step 1 artifact inventory. When evidence is uncertain, cite the namespace or skill only (e.g., "namespace: trace"). Do not invent artifact names. Namespace-level evidence is always acceptable and is the preferred safe floor.

The **Falsified** achievement belongs in the **chain** category. It is earned when any artifact records a retracted hypothesis or amended belief. Classify it in the State column using the same rule. Add a mandatory framing note below the Falsified row — include this regardless of classification state: Falsified is the achievement that proves intellectual honesty. Earning it means the investigation was rigorous enough to follow evidence over assumptions. If not yet earned, frame it as an open invitation, not a deficit.

**Step 4 — Next Recommended Action**

One specific recommendation: skill to invoke, artifact it produces, achievement(s) it advances toward EARNED.

Write artifact to: none (terminal display only)
