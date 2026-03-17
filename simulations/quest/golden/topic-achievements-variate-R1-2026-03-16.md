---
skill: quest-variate
skill_target: topic-achievements
topic: topic-achievements
item: variate
date: 2026-03-16
round: 1
rubric: simulations/quest/rubrics/topic-achievements-rubric-v1-2026-03-16.md
---

# Quest Variate — topic-achievements — Round 1

**Skill description**: Scan all signal artifacts for a topic and compute earned achievements. Shows: earned (with date), in-progress (how close), locked (what still needs doing), next recommended action. Categories: exploration, depth, coverage, quality, chain, discovery, corps/crew. The Falsified achievement is the most important -- it rewards intellectual honesty. Surfaces automatically in topic-status; run directly for the full achievement picture.

**Rubric version**: v1 (10 criteria, 3 tiers)

**Variation strategy**: 3 single-axis variations (V-01 output format, V-02 lifecycle emphasis, V-03 phrasing register), then 2 combinations (V-04 format+register, V-05 role sequence+lifecycle).

---

## V-01 — Axis: Output Format (table-first with explicit state symbols)

**Hypothesis**: Tabular layout with explicit state tokens ([E]/[~]/[L]) makes classification visually unambiguous, maximizing C-01 compliance and making missing dates (C-07) and unlock conditions (C-08) immediately obvious gaps. Tables also force numeric progress into a column, reinforcing C-04.

---

Scan all signal artifacts for the given topic. Glob `simulations/**/{topic}-*` to discover every artifact. For each found, note: namespace, skill, date.

Compute achievements across all 7 categories: **exploration, depth, coverage, quality, chain, discovery, corps/crew**.

**Output format**: one table per category with columns: `Achievement | State | Evidence / Progress | Date`.

State tokens — use exactly one per row:
- `[E] EARNED` — cite the artifact(s) that unlocked it; include earned date
- `[~] IN-PROGRESS` — show a numeric ratio (e.g., "3 of 5 namespaces covered")
- `[L] LOCKED` — state the specific unlock condition (what artifact type, what count, what action)

Every achievement row must carry exactly one state token. No row may be left blank or carry two tokens.

**FALSIFIED** appears as its own named row in the **chain** category. Treat it separately from all other rows:
- It is earned when any artifact records a retracted or amended hypothesis.
- Frame it as a positive signal: earning Falsified proves the investigation was honest. It is intellectual courage made visible, not a mark against the topic.
- If `[~] IN-PROGRESS` or `[L] LOCKED`: describe what artifact type would earn it and reinforce the positive framing — this row is still available to earn.

After all 7 tables: write one sentence per category interpreting what the pattern means for topic maturity.

Close with a single **NEXT ACTION** block: one specific skill to invoke, the artifact it would produce, and which achievement(s) it would advance toward EARNED.

Write artifact to: none (terminal display only)

---

## V-02 — Axis: Lifecycle Emphasis (explicit scan → classify → synthesize → recommend phases)

**Hypothesis**: Making the artifact scan phase explicit before any classification forces citation of real artifacts into the workflow (C-03), and prevents the model from inventing progress ratios. Explicit phase labels also give the Falsified achievement a natural home in PHASE 2 where it can be treated with care before the synthesis step abstracts over it.

---

**PHASE 1 — SCAN**

Glob `simulations/**/{topic}-*` to find every signal artifact for this topic. List each artifact found: namespace, skill, date. If no artifacts exist, report: "No artifacts found for `{topic}`" — then proceed directly to PHASE 4 with the recommended first step.

**PHASE 2 — CLASSIFY**

Map findings from Phase 1 to the 7 achievement categories: **exploration, depth, coverage, quality, chain, discovery, corps/crew**.

For each achievement, assign exactly one state:
- **EARNED** — all requirements met; cite at least one artifact by namespace/skill/date from Phase 1
- **IN-PROGRESS** — partially met; state numeric progress as `n of m` (no vague language)
- **LOCKED** — not started; state the specific unlock condition

**FALSIFIED** is a named achievement in the **chain** category and the most important achievement in the system. It is earned when any artifact records a retracted hypothesis or an amended belief — evidence that the investigation encountered a real surprise. If earned: cite the artifact and celebrate it. If in-progress or locked: frame it as an open invitation, not a deficit. This achievement is proof that the work was genuine.

**PHASE 3 — SYNTHESIZE**

Write 1-3 sentences on what the achievement picture reveals about topic maturity. Name the strongest category and the most significant gap. This synthesis goes before the NEXT ACTION so the recommendation is grounded.

**PHASE 4 — RECOMMEND**

State one concrete next action: the specific skill to run, the artifact it would produce, and which locked or in-progress achievement(s) it would advance.

Write artifact to: none (terminal display only)

---

## V-03 — Axis: Phrasing Register (conversational / motivational, second person)

**Hypothesis**: Conversational second-person framing ("you've earned", "you're close to") makes the Falsified achievement easier to frame positively (C-10) because a motivational tone naturally celebrates progress rather than penalizing absence. It also lowers the risk of vague language replacing numeric ratios — the concrete numbers are *the good news* to deliver.

---

You've been running signals on this topic. Let's see what you've unlocked.

Glob `simulations/**/{topic}-*` to find every artifact for this topic.

Walk through each of the 7 achievement categories — **exploration, depth, coverage, quality, chain, discovery, corps/crew** — and for each tell the user:

- What they've **EARNED** — name the achievement, the date they earned it, and which artifact unlocked it
- What they're **CLOSE TO** — show the ratio: you have `n of m` required, here's what counts toward it
- What they **HAVEN'T STARTED YET** — say exactly what it takes to unlock it (not just "no artifacts" — what artifact type, how many, what would they do)

**FALSIFIED** is the achievement that matters most in this whole system. It's earned when you recorded that you were wrong about something — a hypothesis that didn't pan out, a belief you updated based on evidence. That's how you know the investigation was real. Tell the user:
- If earned: congratulate them. Cite the artifact. This is the rarest and most honest signal in the system.
- If not yet earned: this achievement is still available, and here's exactly what would trigger it. Frame it as an open door, not a missing badge. Intellectual honesty is the goal — it's just waiting to be earned.

End with:
- A short paragraph on what the achievement picture says about where this topic stands right now
- One concrete suggestion: the exact skill to run next, and what it will give them

Write artifact to: none (terminal display only)

---

## V-04 — Combination: Output Format (prose synthesis-first) + Phrasing Register (formal / interpretive)

**Hypothesis**: Opening with the maturity synthesis before the category detail (inverted order vs V-01/V-02) satisfies C-09 structurally and primes the reader to interpret the Falsified entry as a positive signal (C-10) because the interpretive frame is established before they reach it. Formal register reduces the risk of vague "almost there" language (C-04 failure mode).

---

You are computing the achievement profile for a Signal topic. Follow this sequence: synthesize first, then detail by category, then recommend.

**Step 1 — Discover**

Glob `simulations/**/{topic}-*` to find all signal artifacts. Record namespace, skill, and date for each.

**Step 2 — Maturity Statement (write this before the category detail)**

In 1-3 sentences: what does the current achievement picture say about this topic's investigative rigor? Name the strongest dimension and the most significant gap. This statement is the interpretive frame that all subsequent detail serves — write it before classifying individual achievements.

**Step 3 — Category Detail**

For each of the 7 categories (exploration, depth, coverage, quality, chain, discovery, corps/crew), produce a section with:
- Section header naming the category
- Each achievement classified as one of: **EARNED / IN-PROGRESS / LOCKED**
  - EARNED: artifact citation and date (required; no date = not earned)
  - IN-PROGRESS: numeric progress indicator in `n of m` form (required; no ratio = rewrite as LOCKED)
  - LOCKED: explicit unlock condition naming the artifact type or action required

**Step 4 — Falsified Treatment**

The **Falsified** achievement appears in the **chain** category and requires dedicated treatment. It is earned when any artifact records a retracted hypothesis or amended belief. Classify it using the same EARNED/IN-PROGRESS/LOCKED schema, but add a mandatory framing sentence: Falsified is evidence of intellectual honesty — it proves the investigation was rigorous enough that the team encountered a genuine surprise and updated accordingly. If earned: highlight it. If not yet earned: frame the path to earning it as an invitation to the kind of honest inquiry the system is built to reward.

**Step 5 — Next Recommended Action**

One specific skill invocation: name the skill, describe the artifact it produces, and name the achievement(s) it would advance toward EARNED.

Write artifact to: none (terminal display only)

---

## V-05 — Combination: Role Sequence (scanner → classifier → recommender) + Lifecycle Emphasis (explicit phase headers)

**Hypothesis**: Assigning a named role to each phase creates accountability within the prompt — the Scanner cannot invent artifacts (C-03), the Classifier cannot skip classification (C-01/C-04), and the Recommender must produce an actionable next step (C-05). The Falsified achievement gets explicit treatment in the Classifier phase, with its own rule, preventing it from being collapsed into the general classification loop (C-02/C-10).

---

You are running `topic-achievements` in three explicit phases. Each phase has a named role and a specific job. Do not collapse phases or skip ahead.

---

**PHASE 1 — SCANNER**
*Role: artifact discoverer*

Glob `simulations/**/{topic}-*` and list every artifact found. Group by namespace. Count total artifacts and unique namespaces covered.

Output: artifact inventory — one row per artifact: `namespace | skill | date`.

If zero artifacts found: state this clearly, skip PHASE 2, proceed to PHASE 3 with first-step recommendation.

---

**PHASE 2 — CLASSIFIER**
*Role: achievement assessor*

Using only the artifacts listed in PHASE 1, classify achievements across all 7 categories: **exploration, depth, coverage, quality, chain, discovery, corps/crew**.

For each achievement, assign exactly one state — no achievement may be unclassified:
- **EARNED**: cite the specific artifact(s) from Phase 1 by namespace/skill; include the earned date
- **IN-PROGRESS**: state numeric ratio in `n of m` form — "almost there" or "partial" alone fails this requirement
- **LOCKED**: state the specific unlock condition — what artifact type, what count, what action is required

**Falsified Rule**: The **Falsified** achievement is a named entry in the **chain** category. It is not optional and may not be collapsed into a generic entry. It is earned by any artifact that records a retracted or amended hypothesis. Apply the same EARNED/IN-PROGRESS/LOCKED classification, then add one sentence framing Falsified as a positive signal: this is the achievement that proves the investigation was honest. Earning it means the team followed the evidence, not their assumptions.

---

**PHASE 3 — RECOMMENDER**
*Role: advisor*

1. Write a narrative synthesis (1-3 sentences): what does this achievement picture reveal about topic maturity? Identify the strongest category and the most actionable gap.
2. State one **NEXT ACTION**: the specific skill to invoke, the artifact it would produce, and which achievement(s) it would move from LOCKED or IN-PROGRESS toward EARNED.

---

Write artifact to: none (terminal display only)
