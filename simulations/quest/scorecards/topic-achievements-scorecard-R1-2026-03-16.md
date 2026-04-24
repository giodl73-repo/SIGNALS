## Quest Score — topic-achievements — Round 1

### Evaluation Method

No trace artifact available; scoring against skill description + rubric criteria. Each variation is evaluated for how well the prompt *instructions* would reliably produce output satisfying each criterion.

---

## V-01 — Table-First with State Tokens

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Achievement state classification | **PASS** | "Every achievement row must carry exactly one state token. No row may be left blank or carry two tokens." — enforced structurally by the table schema. |
| C-02 | Falsified as distinct named entry | **PASS** | "**FALSIFIED** appears as its own named row in the **chain** category. Treat it separately from all other rows." — explicit separation. |
| C-03 | Artifact-grounded output | **PASS** | "cite the artifact(s) that unlocked it" in EARNED token definition; Glob instruction forces real discovery before classification. |
| C-04 | In-progress numeric progress | **PASS** | "show a numeric ratio (e.g., '3 of 5 namespaces covered')" — baked into [~] token definition. |
| C-05 | Next recommended action | **PASS** | "Close with a single **NEXT ACTION** block: one specific skill to invoke, the artifact it would produce, and which achievement(s) it would advance." — explicit and specific. |
| C-06 | All 7 categories represented | **PASS** | "Compute achievements across all 7 categories: exploration, depth, coverage, quality, chain, discovery, corps/crew" — one table per category enforced. |
| C-07 | Earned achievements carry dates | **PASS** | "`[E] EARNED` — cite the artifact(s) that unlocked it; include earned date" — explicit requirement. |
| C-08 | Locked achievements state unlock conditions | **PASS** | "`[L] LOCKED` — state the specific unlock condition (what artifact type, what count, what action)" — explicit. |
| C-09 | Narrative synthesis | **PARTIAL** | "write one sentence per category interpreting what the pattern means" — sentences present but per-category, not an integrated maturity synthesis. Criterion requires 1–3 sentences on the *overall* picture; per-category sentences fragment rather than integrate. |
| C-10 | Falsified framed positively | **PASS** | "Frame it as a positive signal: earning Falsified proves the investigation was honest. It is intellectual courage made visible" — strong, explicit positive framing. |

**Essential**: 5/5 PASS — **60 pts**
**Recommended**: 3/3 PASS — **30 pts**
**Aspirational**: 1.5/2 (C-09 PARTIAL = 0.5) — **~5 pts**

**Composite: ~95 pts** | All essential pass: YES

---

## V-02 — Lifecycle Phases (scan → classify → synthesize → recommend)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Achievement state classification | **PASS** | "assign exactly one state" with three defined options — explicit. |
| C-02 | Falsified as distinct named entry | **PASS** | "**FALSIFIED** is a named achievement in the **chain** category" — explicitly named and separated. |
| C-03 | Artifact-grounded output | **PASS** | PHASE 1 forces artifact listing before PHASE 2 classification; "cite at least one artifact by namespace/skill/date from Phase 1" — strongest citation enforcement of all variations. |
| C-04 | In-progress numeric progress | **PASS** | "state numeric progress as `n of m` (no vague language)" — explicit with anti-pattern called out. |
| C-05 | Next recommended action | **PASS** | PHASE 4 dedicated to concrete recommendation with skill + artifact + achievement target. |
| C-06 | All 7 categories represented | **PASS** | "Map findings from Phase 1 to the 7 achievement categories" lists all 7; no explicit "note absent categories" instruction — minor gap but 7 listed forces coverage. |
| C-07 | Earned achievements carry dates | **PARTIAL** | "cite at least one artifact by namespace/skill/date from Phase 1" — date is present in the cite format, but no explicit rule that EARNED state *requires* a date as a condition. |
| C-08 | Locked achievements state unlock conditions | **PASS** | "state the specific unlock condition" — explicit. |
| C-09 | Narrative synthesis | **PASS** | PHASE 3 dedicated: "Write 1-3 sentences on what the achievement picture reveals about topic maturity. Name the strongest category and the most significant gap." — matches criterion exactly. |
| C-10 | Falsified framed positively | **PASS** | "If in-progress or locked: frame it as an open invitation, not a deficit. This achievement is proof that the work was genuine." — clear positive framing. |

**Essential**: 5/5 PASS — **60 pts**
**Recommended**: 2.5/3 (C-07 PARTIAL = 0.5) — **~25 pts**
**Aspirational**: 2/2 — **10 pts**

**Composite: ~95 pts** | All essential pass: YES

---

## V-03 — Conversational / Motivational Register

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Achievement state classification | **PASS** | Three states named (EARNED / CLOSE TO / HASN'T STARTED YET) — but relabeling "in-progress" as "CLOSE TO" and "locked" as "HASN'T STARTED YET" introduces ambiguity; the rubric uses exact terms. PASS because three mutually exclusive states are enforced. |
| C-02 | Falsified as distinct named entry | **PASS** | "**FALSIFIED** is the achievement that matters most in this whole system" — dedicated paragraph, clearly separate. |
| C-03 | Artifact-grounded output | **PASS** | Glob instruction present; "which artifact unlocked it" cited in EARNED description. |
| C-04 | In-progress numeric progress | **PASS** | "show the ratio: you have `n of m` required" — explicit. |
| C-05 | Next recommended action | **PASS** | "One concrete suggestion: the exact skill to run next, and what it will give them" — present. |
| C-06 | All 7 categories represented | **PASS** | All 7 listed; "Walk through each of the 7 achievement categories" — explicit enumeration. |
| C-07 | Earned achievements carry dates | **PASS** | "name the achievement, the date they earned it, and which artifact unlocked it" — date explicitly required. |
| C-08 | Locked achievements state unlock conditions | **PASS** | "say exactly what it takes to unlock it (not just 'no artifacts' — what artifact type, how many, what would they do)" — strong and specific. |
| C-09 | Narrative synthesis | **PARTIAL** | "A short paragraph on what the achievement picture says about where this topic stands right now" — present, but "short paragraph" is weaker guidance than the rubric's "1–3 sentences interpreting overall maturity." Likely produces it but may be vague. |
| C-10 | Falsified framed positively | **PASS** | "Intellectual honesty is the goal" + "an open door, not a missing badge" + "If earned: congratulate them" — strongest positive framing of all 5 variations. |

**Essential**: 5/5 PASS — **60 pts**
**Recommended**: 3/3 PASS — **30 pts**
**Aspirational**: 1.5/2 (C-09 PARTIAL = 0.5) — **~5 pts**

**Composite: ~95 pts** | All essential pass: YES

---

## V-04 — Synthesis-First + Formal/Interpretive Register

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Achievement state classification | **PASS** | "EARNED / IN-PROGRESS / LOCKED" with explicit per-state requirements — "no date = not earned" and "no ratio = rewrite as LOCKED" are enforcement mechanisms. |
| C-02 | Falsified as distinct named entry | **PASS** | Step 4 dedicated entirely to Falsified treatment — most structurally isolated of all variations. |
| C-03 | Artifact-grounded output | **PASS** | Step 1 Glob + "EARNED: artifact citation and date (required)" — grounded. |
| C-04 | In-progress numeric progress | **PASS** | "`n of m` form (required; no ratio = rewrite as LOCKED)" — enforcement via consequence. |
| C-05 | Next recommended action | **PASS** | Step 5 dedicated, names skill + artifact + achievement target. |
| C-06 | All 7 categories represented | **PASS** | "For each of the 7 categories (exploration, depth, coverage, quality, chain, discovery, corps/crew)" — all listed. No explicit absent-category instruction, same minor gap as V-02. |
| C-07 | Earned achievements carry dates | **PASS** | "EARNED: artifact citation and date (required; no date = not earned)" — explicit with enforcement. |
| C-08 | Locked achievements state unlock conditions | **PASS** | "LOCKED: explicit unlock condition naming the artifact type or action required" — explicit. |
| C-09 | Narrative synthesis | **PASS** | Step 2 is the *opening* synthesis: "what does the current achievement picture say about this topic's investigative rigor? Name the strongest dimension and the most significant gap" — written *before* category detail. Structurally satisfies C-09 even more robustly than V-02. |
| C-10 | Falsified framed positively | **PASS** | "Falsified is evidence of intellectual honesty — it proves the investigation was rigorous enough that the team encountered a genuine surprise and updated accordingly" + separate step prevents it being absorbed into the general loop. |

**Essential**: 5/5 PASS — **60 pts**
**Recommended**: 3/3 PASS — **30 pts**
**Aspirational**: 2/2 — **10 pts**

**Composite: 100 pts** | All essential pass: YES

---

## V-05 — Role Sequence (scanner → classifier → recommender) + Lifecycle Phases

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Achievement state classification | **PASS** | "assign exactly one state — no achievement may be unclassified" — explicit and reinforced. |
| C-02 | Falsified as distinct named entry | **PASS** | "**Falsified Rule**" — named rule block, "It is not optional and may not be collapsed into a generic entry." — strongest C-02 enforcement. |
| C-03 | Artifact-grounded output | **PASS** | PHASE 1 Scanner produces explicit inventory; PHASE 2 says "Using only the artifacts listed in PHASE 1" — hardest constraint against invention. |
| C-04 | In-progress numeric progress | **PASS** | "`n of m` form — 'almost there' or 'partial' alone fails this requirement" — explicit with failure mode named. |
| C-05 | Next recommended action | **PASS** | PHASE 3 step 2: "State one **NEXT ACTION**: the specific skill to invoke, the artifact it would produce, and which achievement(s) it would move from LOCKED or IN-PROGRESS toward EARNED." — complete. |
| C-06 | All 7 categories represented | **PASS** | All 7 named in PHASE 2; "Using only the artifacts listed in PHASE 1" scopes classification but 7 categories still required. |
| C-07 | Earned achievements carry dates | **PASS** | "EARNED: cite the specific artifact(s) from Phase 1 by namespace/skill; include the earned date" — explicit. |
| C-08 | Locked achievements state unlock conditions | **PASS** | "LOCKED: state the specific unlock condition — what artifact type, what count, what action is required" — explicit. |
| C-09 | Narrative synthesis | **PASS** | PHASE 3 step 1: "Write a narrative synthesis (1-3 sentences): what does this achievement picture reveal about topic maturity? Identify the strongest category and the most actionable gap." — satisfies C-09 precisely. |
| C-10 | Falsified framed positively | **PASS** | "add one sentence framing Falsified as a positive signal: this is the achievement that proves the investigation was honest. Earning it means the team followed the evidence, not their assumptions." — explicit. |

**Essential**: 5/5 PASS — **60 pts**
**Recommended**: 3/3 PASS — **30 pts**
**Aspirational**: 2/2 — **10 pts**

**Composite: 100 pts** | All essential pass: YES

---

## Composite Score Summary

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Composite | Band |
|-----------|---------------|-----------------|-------------------|-----------|------|
| **V-01** | 60 | 30 | ~5 | **~95** | Gold |
| **V-02** | 60 | ~25 | 10 | **~95** | Gold |
| **V-03** | 60 | 30 | ~5 | **~95** | Gold |
| **V-04** | 60 | 30 | 10 | **100** | Gold |
| **V-05** | 60 | 30 | 10 | **100** | Gold |

---

## Ranking

1. **V-04** and **V-05** tied at 100 — both achieve all 10 criteria cleanly.
2. V-04 advantage: synthesis-first structure makes C-09 *structurally guaranteed* (output cannot be produced without it) and primes the reader for positive Falsified framing before encountering it. "No ratio = rewrite as LOCKED" is a uniquely strong enforcement for C-04.
3. V-05 advantage: named-role accountability creates the strongest anti-hallucination mechanism (C-03) and "may not be collapsed into a generic entry" is the strongest C-02 enforcement. Most mechanically reliable under adversarial or edge-case inputs.
4. **V-04 edges V-05** as the top variation — the synthesis-first inversion satisfies C-09 structurally rather than as a terminal step, and the interpretive frame before category detail is architecturally more coherent. V-05 is the more defensively reliable variation.

---

## Excellence Signals from V-04 and V-05

1. **Consequence-enforced classification** — "no ratio = rewrite as LOCKED" (V-04) and "alone fails this requirement" (V-05) give the model a correction path, not just a rule.
2. **Synthesis-first ordering** (V-04) — placing the maturity statement *before* category detail makes C-09 a precondition of the output, not an afterthought. The reader's interpretive frame is set before they encounter individual achievements, making positive Falsified framing land in prepared context.
3. **Structural isolation of Falsified** — both V-04 (dedicated Step 4) and V-05 (named Falsified Rule block) prevent Falsified from being absorbed into the general classification loop. This is the key pattern: Falsified needs its own step, not just a mention inside another step.
4. **"Using only the artifacts listed in PHASE 1"** (V-05) — this phrase is the most powerful C-03 enforcement across all variations. It creates a closed world: the classifier has no source other than the scanner's output.
5. **Named roles create per-phase accountability** (V-05) — Scanner / Classifier / Recommender labels make it harder for the model to skip a phase, because each phase has an identity and a specific job description.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["consequence-enforced classification: give the model a rewrite path when requirements fail (e.g., 'no ratio = rewrite as LOCKED'), not just a constraint", "synthesis-first ordering: placing the maturity synthesis before category detail makes C-09 a structural precondition, not a terminal afterthought, and primes positive framing for Falsified", "structural isolation of special entries: give Falsified its own named step or rule block — prevents it being absorbed into the general classification loop", "closed-world artifact constraint: 'using only artifacts listed in PHASE 1' is stronger than any cite instruction — it eliminates the inventory the model can draw from"]}
```
