---
skill: quest-variate
skill_target: topic-achievements
topic: topic-achievements
item: variate
date: 2026-03-16
round: 2
rubric: simulations/quest/rubrics/topic-achievements-rubric-v2-2026-03-16.md
---

# Quest Variate — topic-achievements — Round 2

**Skill description**: Scan all signal artifacts for a topic and compute earned achievements. Shows: earned (with date), in-progress (how close), locked (what still needs doing), next recommended action. Categories: exploration, depth, coverage, quality, chain, discovery, corps/crew. The Falsified achievement is the most important -- it rewards intellectual honesty. Surfaces automatically in topic-status; run directly for the full achievement picture.

**Rubric version**: v2 (13 criteria, 3 tiers — 3 new aspirational: C-11 synthesis position, C-12 consequence-backed rules, C-13 Falsified isolation)

**Round 1 baseline**: V-04 scored 100 and supplied all three new criteria. R2 goal: isolate each new axis, then combine, to learn which mechanism carries the most v2 scoring weight.

**Variation strategy**: 3 single-axis variations targeting C-11 (V-01), C-12 (V-02), C-13 (V-03), then two combinations: C-11+C-12 (V-04), all three (V-05).

---

## V-01 — Axis: Synthesis Position (C-11 target)

**Hypothesis**: Inserting a hard gate — "write the synthesis before you open any category section" — forces C-11 compliance structurally. The gate is a numbered step with an explicit dependency ("complete Step 2 before proceeding to Step 3"), making it a blocking instruction rather than advice. If this single structural constraint is sufficient to move C-11 from FAIL to PASS without additional changes, C-11 is primarily a sequencing problem, not a quality problem. All other aspects (rules, Falsified) are held at R1 V-04 baseline.

---

Glob `simulations/**/{topic}-*` to discover every signal artifact for this topic. For each found, record: namespace, skill, date.

**Step 1 — Artifact Inventory**

List every artifact found. Group by namespace. Note total artifact count and unique namespace count.

If no artifacts are found, report: "No artifacts found for `{topic}`." Skip Step 2 and Step 3. Proceed directly to Step 4 with a first-step recommendation.

**Step 2 — Maturity Synthesis (write this before opening any category section)**

Before classifying a single achievement, write 1-3 sentences interpreting what the artifact inventory reveals about this topic's investigative maturity. Name the strongest dimension and the most significant gap. This synthesis is the frame that all per-category detail serves.

Do not proceed to Step 3 until this paragraph is written.

**Step 3 — Category Classification**

Using only the artifacts listed in Step 1, classify achievements across all 7 categories: **exploration, depth, coverage, quality, chain, discovery, corps/crew**.

For each achievement, assign exactly one state:
- **EARNED** — cite the artifact(s) from Step 1 by namespace/skill; include the date earned
- **IN-PROGRESS** — state numeric progress as `n of m` (example: "3 of 5 namespaces covered"); no vague language
- **LOCKED** — state the specific unlock condition: what artifact type, what count, or what action is required

Every category must appear. If a category has no achievements to show, write: "No achievements yet in this category."

The **Falsified** achievement belongs in the **chain** category. It is earned when any artifact records a retracted hypothesis or amended belief. Classify it using the EARNED/IN-PROGRESS/LOCKED schema and add a framing sentence: Falsified is the achievement that proves the investigation encountered real surprises — it signals intellectual honesty, not failure. If not yet earned, frame it as an open invitation.

**Step 4 — Next Recommended Action**

State one specific next action: the skill to invoke, the artifact it would produce, and which achievement(s) it would advance toward EARNED.

Write artifact to: none (terminal display only)

---

## V-02 — Axis: Consequence-Backed Rules (C-12 target)

**Hypothesis**: Writing every classification rule as a consequence clause — "if not present, then demote to LOCKED" — makes compliance structurally difficult to violate. An advisory instruction ("include a date") can be silently ignored; a consequence clause ("no date = this entry is demoted to LOCKED, not EARNED") cannot be satisfied without visible rule-breaking. If C-12 compliance alone is sufficient to raise scores on C-07 and C-04 (which share the same failure mode — silent omission), consequence framing is doing double duty. Falsified placement and synthesis position are held at R1 V-04 baseline.

---

Glob `simulations/**/{topic}-*` to discover every signal artifact. Record namespace, skill, date for each.

**Scan**

List every artifact found. If none found, state: "No artifacts for `{topic}`." Proceed directly to the NEXT ACTION block.

**Maturity Statement**

In 1-3 sentences: what does the artifact picture say about this topic's investigative maturity? Name the strongest dimension and the most significant gap. Write this before the category detail.

**Step 2 — Maturity Statement (write this before opening any category section)**

Write 1-3 sentences interpreting the artifact inventory: strongest dimension, most significant gap. Write this before classifying any individual achievement.

**Category Classification**

For each of the 7 categories (**exploration, depth, coverage, quality, chain, discovery, corps/crew**), classify each achievement under one of these states. The following rules carry enforcement consequences — violating a rule requires the stated correction, not discretionary judgment:

- **EARNED**: cite the specific artifact by namespace and skill, and include the date earned.
  *Enforcement: if no artifact citation is present, the entry is not EARNED — demote it to LOCKED and state the unlock condition.*
  *Enforcement: if no earned date is present, the entry is not EARNED — demote it to LOCKED.*

- **IN-PROGRESS**: state numeric progress in `n of m` form (example: "2 of 4 namespaces covered").
  *Enforcement: if no numeric ratio is present, the entry is not IN-PROGRESS — demote it to LOCKED.*

- **LOCKED**: state the specific unlock condition — name the artifact type, count, or action required.
  *Enforcement: if no unlock condition is stated, the locked entry is incomplete — add the condition before finalizing.*

Every category must appear. Write "No achievements yet in this category" for any category with nothing to show.

**Falsified Treatment**

The **Falsified** achievement is a named entry in the **chain** category with its own dedicated treatment. It is earned when any artifact records a retracted hypothesis or amended belief. Classify using the EARNED/IN-PROGRESS/LOCKED schema — apply the same enforcement consequences as above. Add one mandatory framing sentence: Falsified is the achievement that proves the investigation was honest. Earning it means the team followed the evidence, not their assumptions. If not yet earned, frame it as an invitation to the kind of rigorous inquiry the system rewards.

*Enforcement: if this framing sentence is absent, the Falsified entry is incomplete — add it before finalizing.*

**NEXT ACTION**

One specific recommendation: skill to invoke, artifact it produces, achievement(s) it would advance.

Write artifact to: none (terminal display only)

---

## V-03 — Axis: Falsified Structural Isolation (C-13 target)

**Hypothesis**: Moving Falsified into its own numbered step, explicitly outside the 7-category block, prevents it from being compressed or skipped when the model is in list-enumeration mode. The mechanism is a two-part instruction in the category step: "classify the 6 non-chain categories; for chain, classify all chain achievements except Falsified." Falsified then appears in a separate step with its own heading. If this isolation is sufficient to guarantee Falsified full treatment (C-13 pass), the skipping problem is an enumeration-mode attention problem, not a framing problem. Synthesis position and enforcement rules are held at R1 V-04 baseline.

---

Glob `simulations/**/{topic}-*` to discover every signal artifact. Record namespace, skill, date for each.

**Step 1 — Discover**

List every artifact found by namespace, skill, and date. If none found: "No artifacts for `{topic}`." Skip Steps 2-4. Proceed to Step 5 with a first-step recommendation.

**Step 2 — Maturity Statement**

In 1-3 sentences: what does the artifact picture say about this topic's investigative maturity? Name the strongest dimension and the most significant gap. Write this before any per-category detail.

**Step 3 — Category Classification (all categories except Falsified)**

Using only the artifacts from Step 1, classify achievements across these categories: **exploration, depth, coverage, quality, chain (non-Falsified achievements only), discovery, corps/crew**.

For each achievement, assign one state:
- **EARNED**: cite the artifact by namespace/skill and include the date earned
- **IN-PROGRESS**: state numeric progress as `n of m`; no vague language
- **LOCKED**: state the specific unlock condition (artifact type, count, or action)

Every category must appear. Write "No achievements yet in this category" if empty. In the **chain** category, classify all chain achievements except Falsified — leave a placeholder: "Falsified: see Step 4."

**Step 4 — Falsified (dedicated)**

This step handles the Falsified achievement exclusively. It is not part of the category enumeration in Step 3.

Falsified is earned when any artifact records a retracted hypothesis or amended belief — evidence that the investigation hit a genuine surprise and updated accordingly. Classify it:
- **EARNED**: cite the artifact, state the date, and celebrate it — this is the rarest and most honest signal in the system
- **IN-PROGRESS**: state how close (e.g., "hypothesis recorded, no retraction or amendment yet"); keep the frame positive
- **LOCKED**: state exactly what artifact type would trigger it; frame this as an open door — the achievement is available and waiting

Mandatory framing: Falsified is the achievement that proves intellectual honesty. It cannot be earned without real investigation. A team that earns it followed the evidence, not their assumptions.

**Step 5 — Next Recommended Action**

One specific recommendation: skill to invoke, artifact it produces, achievement(s) it would advance toward EARNED.

Write artifact to: none (terminal display only)

---

## V-04 — Combination: Synthesis Position + Consequence-Backed Rules (C-11 + C-12)

**Hypothesis**: Pairing the synthesis gate (C-11) with enforcement clauses (C-12) while leaving Falsified inside the chain category tests whether the two architectural changes are independently sufficient or whether they reinforce each other. If V-04 scores higher than V-01 and V-02 but lower than V-05, the combination is synergistic but not complete. Falsified placement is held at R1 V-04 baseline (chain category, dedicated treatment but not isolated step) to isolate the C-11+C-12 combination effect.

---

Glob `simulations/**/{topic}-*` to discover every signal artifact. Record namespace, skill, date for each.

**Step 1 — Artifact Inventory**

List every artifact found: namespace, skill, date. Count total artifacts and unique namespaces.

If no artifacts found: "No artifacts for `{topic}`." Skip Steps 2 and 3. Proceed to Step 4.

**Step 2 — Maturity Synthesis (required before Step 3)**

Write 1-3 sentences: what does the artifact inventory reveal about this topic's investigative maturity? Identify the strongest dimension and the most significant gap. This is the interpretive frame that all per-category detail serves.

You may not begin Step 3 until this synthesis is written. Per-category sentences in Step 3 supplement this synthesis; they do not replace it.

**Step 3 — Category Classification**

Using only the artifacts from Step 1, classify achievements across all 7 categories: **exploration, depth, coverage, quality, chain, discovery, corps/crew**.

Classification rules — each rule carries an enforcement consequence:

**EARNED**
State: all requirements met.
Requirements: cite the specific artifact from Step 1 (namespace/skill); include the date earned.
*If no artifact citation is present: demote to LOCKED and state the unlock condition.*
*If no earned date is present: demote to LOCKED.*

**IN-PROGRESS**
State: partially met.
Requirements: state numeric progress in `n of m` form.
*If no numeric ratio is present: demote to LOCKED.*

**LOCKED**
State: not started or unmet.
Requirements: state the specific unlock condition (artifact type, count, or action).
*If no unlock condition is stated: the entry is incomplete — add the condition before finalizing.*

Every category must appear. Write "No achievements yet in this category" for any empty category.

**Falsified** is a named achievement in the **chain** category. It is earned by any artifact recording a retracted hypothesis or amended belief. Apply the same classification rules and enforcement consequences. Add a mandatory framing sentence: Falsified is the achievement that proves the investigation was honest — it signals intellectual courage, not failure. If not yet earned, name the artifact type that would earn it and frame it as an open invitation.
*If this framing sentence is absent: the Falsified entry is incomplete — add it before finalizing.*

**Step 4 — Next Recommended Action**

One specific recommendation: skill to invoke, artifact it produces, achievement(s) it would advance toward EARNED.

Write artifact to: none (terminal display only)

---

## V-05 — Combination: All Three New Axes (C-11 + C-12 + C-13)

**Hypothesis**: Combining synthesis-first gate (C-11), consequence-backed rules (C-12), and Falsified structural isolation (C-13) targets all five aspirational criteria simultaneously (C-09 through C-13). If V-05 achieves Gold on v2 rubric, the three mechanisms together are the complete solution. The risk is that the prompt becomes verbose enough to degrade essential criterion compliance — if V-05 scores lower on essentials than simpler variations, structural complexity is the culprit and the mechanisms need to be simplified without losing their enforcement character.

---

Glob `simulations/**/{topic}-*` to discover every signal artifact. Record namespace, skill, date for each.

**Step 1 — Artifact Inventory**

List every artifact found: namespace, skill, date. Group by namespace. Record total artifact count and unique namespace count.

If no artifacts found: state "No artifacts for `{topic}`." Skip Steps 2-4. Proceed to Step 5 with a first-step recommendation.

**Step 2 — Maturity Synthesis (required before Step 3 — do not skip)**

Before classifying any individual achievement, write 1-3 sentences interpreting the overall achievement picture: what does the artifact inventory reveal about this topic's investigative maturity? Name the strongest dimension and the most significant gap. This is the integrated opening frame — per-category interpretation in Step 3 supplements it but cannot replace it.

Complete this step in full before proceeding to Step 3.

**Step 3 — Category Classification (all categories; Falsified is handled in Step 4)**

Using only the artifacts from Step 1, classify achievements across these 7 categories: **exploration, depth, coverage, quality, chain (non-Falsified achievements only), discovery, corps/crew**.

Every category must appear. Write "No achievements yet in this category" for any empty category. In the **chain** category: classify all chain achievements except Falsified. Leave a placeholder line: "Falsified: classified in Step 4."

Classification rules with enforcement consequences:

**EARNED**
Requirements: cite the specific artifact from Step 1 by namespace and skill; include the date earned.
*Enforcement: if no artifact citation — demote to LOCKED; state the unlock condition.*
*Enforcement: if no earned date — demote to LOCKED.*

**IN-PROGRESS**
Requirements: state numeric progress in `n of m` form (e.g., "3 of 6 namespaces covered").
*Enforcement: if no numeric ratio — demote to LOCKED.*

**LOCKED**
Requirements: state the specific unlock condition naming artifact type, count, or action required.
*Enforcement: if no unlock condition stated — entry is incomplete; add the condition before continuing.*

**Step 4 — Falsified (dedicated step, outside the category loop)**

This step is exclusively for the Falsified achievement. It is structurally separate from the category classification in Step 3 and cannot be satisfied by a Falsified row appearing within the chain category section.

Falsified is earned when any artifact records a retracted hypothesis or amended belief — evidence that the investigation hit a genuine surprise and the team updated their understanding accordingly. This is the most important achievement in the system: not because it is rare, but because it proves the work was real.

Classify Falsified using the same EARNED/IN-PROGRESS/LOCKED schema:
- **EARNED**: cite the artifact (namespace, skill, date); celebrate it explicitly — this is intellectual honesty made visible
- **IN-PROGRESS**: describe what exists and what is still needed; state progress numerically if possible; keep the frame positive
- **LOCKED**: state exactly what artifact type or action would trigger it; frame it as an open invitation, not a deficit

Mandatory framing — include this regardless of classification state: Falsified is the achievement that proves the investigation was honest. Earning it means the team followed the evidence, not their assumptions. A rigorous investigation earns it. An investigation that confirms what it expected does not.

*Enforcement: if the mandatory framing sentence is absent — the Falsified step is incomplete; add it before finalizing.*
*Enforcement: if Falsified appears only as a row within the Step 3 chain category — this step is not satisfied; the dedicated Step 4 treatment is required.*

**Step 5 — Next Recommended Action**

One specific recommendation: the skill to invoke, the artifact it would produce, and which achievement(s) it would advance toward EARNED.

Write artifact to: none (terminal display only)
