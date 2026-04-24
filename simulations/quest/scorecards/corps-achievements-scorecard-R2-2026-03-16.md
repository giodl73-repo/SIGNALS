Now I have all 5 variations. Scoring against v2 rubric.

---

## Scoring — corps-achievements R2 vs Rubric v2

### V-01 — Baseline Structured

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Scan grounded in real workspace files | PASS | Explicit search paths: `simulations/{namespace}/{skill}/`, `quest/golden/`, `quest/scorecards/` |
| C-02 | Every discovered topic appears in output | PASS | "Omitting a topic is a PHASE 2 gate failure" — explicit halt |
| C-03 | All three milestone names present | PASS | "First Team Signal", "Shared Coverage", "Debate Starter" by exact name in PHASE 3 |
| C-04 | Contributor leaderboard exists and populated | PASS | PHASE 4 required with rank, artifacts, topics, namespaces |
| C-05 | Next actions name action AND achievement | PASS | Format: `[Action] → Unlocks [Achievement] → Breaks [Stagnation Pattern]` |
| C-06 | Earned vs. available visually separated | PASS | OUTPUT FORMAT: "grouped: Earned / Available" |
| C-07 | Achievements grouped into ≥2 categories | PASS | "Coverage achievements" and "Contributor achievements" explicitly labeled |
| C-08 | Sprint/date framing present | PASS | "Use today's date... Include sprint framing if determinable" |
| C-09 | Dedicated 1-away section with exact counts | PASS | PHASE 5: "Exact count or condition currently satisfied / Exact 1 thing needed" |
| C-10 | Named cross-topic insight, differs from gap statements | PASS | "Differ from any gap or stagnation pattern statement already made" — constraint explicit |
| C-11 | At least one inline pre-write self-test gate | PASS | 3 gates: after scan, before close-to-unlock, before each action |
| C-12 | Anti-inertia action framing `[Action] → Unlocks → Breaks` | PASS | Format string in PHASE 7 matches exactly |

**Essential: 5/5 → 60 | Recommended: 3/3 → 30 | Aspirational: 4/4 → 10**
**Score: 100** | Golden: YES

---

### V-02 — Table-Heavy Output Format

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Scan grounded in real workspace files | PASS | Same explicit search paths |
| C-02 | Every discovered topic appears in output | PASS | "One row per topic. No topics may be omitted." + PRE-WRITE SELF-TEST |
| C-03 | All three milestone names present | PASS | "First Team Signal", "Shared Coverage", "Debate Starter" in STEP 3 table |
| C-04 | Contributor leaderboard exists and populated | PASS | STEP 4 table, "Sort descending by Artifacts. Include all contributors found." |
| C-05 | Next actions name action AND achievement | PASS | STEP 7 table: Unlocks column required, "Every row must have a value in all four columns" |
| C-06 | Earned vs. available visually separated | PASS | Status column: EARNED / AVAILABLE / PARTIAL — machine-readable separation |
| C-07 | Achievements grouped into ≥2 categories | PARTIAL | Coverage/Contributor types exist in row values but no explicit category headers or sections — implicit grouping only |
| C-08 | Sprint/date framing present | PASS | "Sprint [date range]" in Scan section header if ≥7 days; Date Range column in table |
| C-09 | Dedicated 1-away section with exact counts | PASS | STEP 5: "Only include rows where Gap = 1" — table enforces quantification |
| C-10 | Named cross-topic insight, differs from gap statements | PASS | "Must not restate any gap or stagnation pattern already mentioned… visible only when looking across topics" |
| C-11 | At least one inline pre-write self-test gate | PASS | 3 gates: before scan table, before close-to-unlock table, before next-actions table |
| C-12 | Anti-inertia action framing `[Action] → Unlocks → Breaks` | PASS | STEP 7 table columns: Action | Unlocks | Breaks Pattern — functional equivalent of inline format |

**Essential: 5/5 → 60 | Recommended: 2/3 → 20 | Aspirational: 4/4 → 10**
**Score: 90** | Golden: YES (≥80 + all essential)

---

### V-03 — Conversational/Imperative Register

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Scan grounded in real workspace files | PASS | "Check these locations: simulations/{namespace}/{skill}/, simulations/quest/golden/, simulations/quest/scorecards/" |
| C-02 | Every discovered topic appears in output | PASS | "Don't skip a topic. If a topic was in your scan, it's in this section. Missing a topic here is a mistake — catch it." |
| C-03 | All three milestone names present | PASS | "**First Team Signal**", "**Shared Coverage**", "**Debate Starter**" by exact name |
| C-04 | Contributor leaderboard exists and populated | PASS | "Show the leaderboard" section required with rank, artifacts, topics, namespaces |
| C-05 | Next actions name action AND achievement | PASS | Format: `[What to do] → Unlocks [Achievement name] → Breaks [Name the rut]` |
| C-06 | Earned vs. available visually separated | PASS | "Show earned achievements and available ones separately. Label them EARNED and AVAILABLE." |
| C-07 | Achievements grouped into ≥2 categories | PASS | "**Coverage achievements:**" and "**Contributor achievements:**" explicitly bold-labeled |
| C-08 | Sprint/date framing present | PASS | "Today's date goes at the top. If you can tell what sprint it is from the artifact dates, say so." |
| C-09 | Dedicated 1-away section with exact counts | PASS | "Find what's close" section: "What you currently have / Exactly what's needed" |
| C-10 | Named cross-topic insight, differs from gap statements | PASS | "It can't be something you already said." + "Format: **TEAM INSIGHT — [name it]:**" |
| C-11 | At least one inline pre-write self-test gate | PASS | 3 self-directed questions: before topic listing, before close-to-unlock, before each action |
| C-12 | Anti-inertia action framing `[Action] → Unlocks → Breaks` | PASS | `[What to do] → Unlocks [Achievement name] → Breaks [Name the rut]` |

**Essential: 5/5 → 60 | Recommended: 3/3 → 30 | Aspirational: 4/4 → 10**
**Score: 100** | Golden: YES

---

### V-04 — Inertia Framing Foregrounded

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Scan grounded in real workspace files | PASS | Real search paths; PRE-WRITE SELF-TEST: "no invented topics" |
| C-02 | Every discovered topic appears in output | PASS | "GATE: A missing topic is a PHASE 2 gate failure. Stop and rescan." |
| C-03 | All three milestone names present | PASS | SECTION 3: "**First Team Signal**", "**Shared Coverage**", "**Debate Starter**" |
| C-04 | Contributor leaderboard exists and populated | PASS | SECTION 4 with rank, artifacts, topics, namespaces |
| C-05 | Next actions name action AND achievement | PASS | `[Action] → Unlocks [Achievement] → Breaks [PATTERN_LABEL from registry]` |
| C-06 | Earned vs. available visually separated | PASS | "Display as: EARNED / AVAILABLE, visually separated per topic." |
| C-07 | Achievements grouped into ≥2 categories | PASS | "Coverage achievements:" and "Contributor achievements:" explicit labels in SECTION 2 |
| C-08 | Sprint/date framing present | PASS | "Report header (date + sprint if determinable)" in OUTPUT STRUCTURE |
| C-09 | Dedicated 1-away section with exact counts | PASS | SECTION 5: "Name of achievement, Current count, Exact thing needed" |
| C-10 | Named cross-topic insight, differs from gap statements | PASS | "Differs from every stagnation pattern already named in the registry" — strongest uniqueness constraint of all five variations |
| C-11 | At least one inline pre-write self-test gate | PASS | 3 gates: after scan, before close-to-unlock, before each action |
| C-12 | Anti-inertia action framing `[Action] → Unlocks → Breaks` | PASS | Registry-backed: `[Action] → Unlocks [Achievement] → Breaks [PATTERN_LABEL from registry]` — labeled patterns prevent invention at write time |

**Essential: 5/5 → 60 | Recommended: 3/3 → 30 | Aspirational: 4/4 → 10**
**Score: 100** | Golden: YES

---

### V-05 — Combined: Lifecycle + Inverted Role Sequence

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Scan grounded in real workspace files | PASS | Real search paths; GATE-A enforces at least 1 topic found |
| C-02 | Every discovered topic appears in output | PASS | GATE-B: "Is every topic from Phase 1 present? NO → halt" with named topic in error message |
| C-03 | All three milestone names present | PASS | PHASE 3a: "**First Team Signal**", "**Shared Coverage**", "**Debate Starter**"; GATE-C enforces all 3 assessed |
| C-04 | Contributor leaderboard exists and populated | PASS | PHASE 4, enforced by GATE-D verification table |
| C-05 | Next actions name action AND achievement | PASS | `[Action] → Unlocks [Achievement] → Breaks [Stagnation Pattern]` |
| C-06 | Earned vs. available visually separated | PASS | "grouped blocks: EARNED (bold), then AVAILABLE (normal weight), per topic" |
| C-07 | Achievements grouped into ≥2 categories | PASS | "Coverage achievements" and "Contributor achievements" in PHASE 2 |
| C-08 | Sprint/date framing present | PASS | "State today's date and sprint context if determinable" in PHASE 0 |
| C-09 | Dedicated 1-away section with exact counts | PASS | PHASE 5: "achievement name, current count, exact gap"; PRE-WRITE SELF-TEST guards accuracy |
| C-10 | Named cross-topic insight, differs from gap statements | PASS | PHASE 3b: "must differ from any gap statement already made"; HYPOTHESIS OUTCOME tracking adds discipline — strongest C-10 mechanism |
| C-11 | At least one inline pre-write self-test gate | PASS | 4 gates: after scan, before insight, before close-to-unlock, before each action |
| C-12 | Anti-inertia action framing `[Action] → Unlocks → Breaks` | PASS | `[Action] → Unlocks [Achievement] → Breaks [Stagnation Pattern]` + inline YES/NO per action |

**Essential: 5/5 → 60 | Recommended: 3/3 → 30 | Aspirational: 4/4 → 10**
**Score: 100** | Golden: YES

---

## Summary Scorecard

| Variation | Essential | Recommended | Aspirational | Score | Golden |
|-----------|-----------|-------------|--------------|-------|--------|
| V-01 — Baseline Structured | 5/5 | 3/3 | 4/4 | **100** | YES |
| V-02 — Table-Heavy | 5/5 | 2/3 | 4/4 | **90** | YES |
| V-03 — Conversational | 5/5 | 3/3 | 4/4 | **100** | YES |
| V-04 — Inertia Foregrounded | 5/5 | 3/3 | 4/4 | **100** | YES |
| V-05 — Combined Lifecycle | 5/5 | 3/3 | 4/4 | **100** | YES |

**V-02 weakness:** C-07 PARTIAL — achievement types (coverage vs. contributor) are embedded in row values but not separated by explicit category headers or sections. Every other variation explicitly labels the two categories with bold or section headers.

## Excellence Signals

**R2-specific patterns not yet in rubric:**

1. **V-04 — Named stagnation registry:** Defines pattern labels (SOLO_DRIFT, SCOUT_TRAP, SHALLOW_CLUSTER, DEBATE_DEFICIT, COVERAGE_PLATEAU) before the report runs. C-12 actions cross-reference the registry instead of inventing patterns at write time. Additional constraint: "Actions must address different stagnation patterns — do not list 5 actions that all break SOLO_DRIFT." This makes anti-inertia diversity enforceable.

2. **V-05 — Hypothesis-before-scan commitment:** PHASE 0 forces the model to commit to a cross-topic hypothesis before reading any files. PHASE 3b requires the insight to confirm, refine, or refute that hypothesis and say which. This disciplines C-10 by making the insight a falsifiable claim rather than a post-hoc observation.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["named stagnation pattern registry with diversity constraint — C-12 actions cross-reference predefined patterns rather than inventing at write time", "hypothesis-before-scan commitment — model states expected cross-topic pattern before reading files, then confirms/refines/refutes in insight phase"]}
```
