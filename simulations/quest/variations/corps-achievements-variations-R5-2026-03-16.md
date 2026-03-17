Written to `simulations/quest/variations/corps-achievements-variations-R5-2026-03-16.md`.

---

## Round 5 Variations — `corps-achievements`

**Rubric:** v5 (5E + 3R + 12A) — two new aspirationals: C-19 (rank-1 worked example instruction) and C-20 (criterion-ID gate labels)

### Variation Axes

| Variation | Primary Axis | Key Problem It Solves |
|-----------|-------------|----------------------|
| **V-01** | Criterion-ID gate notation throughout | Every gate labeled `[C-xx]` satisfies C-20; combined `GATE [C-04/C-16/C-19]` on leaderboard covers C-19 in a single enforcement point |
| **V-02** | Worked example promoted to dedicated SCORE VERIFICATION sub-step | Standalone `GATE [C-19]` with active cross-check instruction makes C-19 a first-class structural output, not a trailing line |
| **V-03** | Per-section self-test gate per criterion pair (R4 V-03 upgraded) | Cleanest upgrade path: adds `[C-xx]` to all existing gates + separate `GATE [C-19]` after leaderboard — zero structural disruption |
| **V-04** | Registry-first + criterion-ID gates (R4 V-04 upgraded) | Stagnation registry preamble (strongest C-14/C-17 base) + `[C-xx]` labels + combined C-04/C-16/C-19 gate |
| **V-05** | Pre-flight maps all 12 aspirationals + criterion-ID gates per section | Pre-flight table makes the entire 12-criterion profile auditable before generation; separate `GATE [C-19]` ensures worked example is never merged into the formula instruction |

### What Changed from R4

All five variations now address the two new criteria:
- **C-19 fix**: Every variation includes an explicit instruction to render the rank-1 worked example inline — not just assert the formula is auditable
- **C-20 fix**: Every gate in every variation carries `[C-xx]` criterion-ID notation, creating direct traceable links between enforcement logic and rubric criteria

The primary differentiator across V-01/V-03/V-04 vs V-02/V-05 is **where C-19 lives**: combined into the leaderboard gate (three variations) vs promoted to a standalone `GATE [C-19]` after the table (V-02 and V-05). Both satisfy the criterion — the question is which placement makes omission least likely in practice.
 plugin's team achievement tracker.
All gate checks in this skill reference criterion IDs to make enforcement auditable against the rubric.

---

### PHASE 1 — WORKSPACE SCAN

**GATE [C-01/C-02]:** "I will only name topics I can trace to a real file path in `simulations/`. Any topic without confirmed file evidence: GATE-A: [topic-name] removed — no real file evidence. I commit to this list: every topic I name here will appear in the achievement sections."

Scan `simulations/` for artifacts matching `{topic}-{signal}-{date}.md`. Extract topic slug, namespace, contributor, date.

```
TOPIC REGISTRY
- {topic}: {n} signals | namespaces: {list} | contributors: {list} | latest: {date}
```

---

### PHASE 2 — ACHIEVEMENT AWARDS

**GATE [C-02/C-06/C-07]:** "Every topic from Phase 1 appears in the EARNED ACHIEVEMENTS or NOT YET EARNED section below. Missing: GATE-B: [topic-name] has no achievement row → halt. Two visually separate sections follow, each organized under two named categories."

#### EARNED ACHIEVEMENTS

**Category: DEPTH ACHIEVEMENTS**
- Signal Starter — {topic}: {file evidence}
- Multi-Namespace — {topic}: {namespaces list}
- Sprint Complete — {topic}: {count + sprint window}

**Category: COLLABORATION ACHIEVEMENTS**
- Pair Signal — {topic}: {contributor names}
- Cross-Fire — {topic}: {conflict description}

#### NOT YET EARNED

**Category: DEPTH ACHIEVEMENTS**
- {achievement} — {topic}: needs {exact gap}

**Category: COLLABORATION ACHIEVEMENTS**
- {achievement} — {topic}: needs {exact gap}

---

### PHASE 3 — TEAM MILESTONES

**GATE [C-03/C-08]:** "All three milestone names appear verbatim below. Sprint run date is shown."

| Milestone | Status | Evidence |
|-----------|--------|----------|
| **First Team Signal** | ✅/⬜ | {first file or gap} |
| **Shared Coverage** | ✅/⬜ | {topic + contributor names or gap} |
| **Debate Starter** | ✅/⬜ | {topic + conflicting namespaces or gap} |

Run date: {date}

---

### PHASE 4 — CONTRIBUTOR LEADERBOARD

**GATE [C-04/C-16/C-19]:** "Leaderboard is populated. Weighted formula is explicit. After the table I will render the rank-1 worked example calculation so the score is auditable from raw counts without reconstruction."

**Formula: Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)**

The multipliers encode the team's value judgment: milestone triggers are worth 5× a signal; topic breadth is worth 3×.

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
| 1 | {name} | {n} | {n} | {list} | {n} |

Rank-1 worked example: Score = {signals}×1 + {topics}×3 + {milestones}×5 = {total}

---

### PHASE 5 — 1-AWAY CALLOUTS

**GATE [C-09/C-18]:** "Dedicated section. Every row has exactly four columns: Topic, Achievement, Gap (what's missing), Exact Action Needed. No row omits a column. No prose substitution."

| Topic | Achievement | Gap (what's missing) | Exact Action Needed |
|-------|-------------|----------------------|---------------------|
| {topic} | {achievement name} | {specific — e.g., "1 more signal in flow namespace"} | Run /{namespace}:{skill} for {topic} |

(Write "No 1-away achievements this sprint" if empty — do not remove section.)

---

### PHASE 6 — STAGNATION PATTERN DIAGNOSIS

**GATE [C-14/C-15/C-17]:** "I will reference only these four labels: SOLO_ISLAND, NAMESPACE_MOAT, SPRINT_FREEZE, ORPHAN_TOPIC. No invented labels. Each active pattern names the specific topic or contributor instance. Gate failure format: GATE-C: [topic-name] — label not found in registry → halt."

| Label | Active? | Instance (name exact topic or contributor) |
|-------|---------|---------------------------------------------|
| SOLO_ISLAND | ✅/⬜ | {topic or contributor} |
| NAMESPACE_MOAT | ✅/⬜ | {topic} |
| SPRINT_FREEZE | ✅/⬜ | {topic} |
| ORPHAN_TOPIC | ✅/⬜ | {topic} |

---

### PHASE 7 — CROSS-TOPIC SYNTHESIS

**GATE [C-10/C-13]:** "The insight below is NOT a restatement of any stagnation row above. It is formatted as a named artifact with a descriptive title. It is cross-topic or cross-contributor in scope."

**TEAM INSIGHT — [Descriptive Title]:**
[2–3 sentences. Visible only when looking across all topics. Differs in substance from Phase 6 rows.]

---

### PHASE 8 — NEXT ACTIONS

**GATE [C-05/C-11/C-12]:** "Each row below names: (a) the exact action, (b) the exact achievement it unlocks, (c) the exact stagnation pattern from the Phase 6 registry it breaks. If any component is missing: rewrite before continuing."

> [Specific Action] → Unlocks **[Achievement Name]** → Breaks **[PATTERN_LABEL from registry]**

Minimum 3 actions.

---

### SPRINT SUMMARY

> Run date: {date} | Topics scanned: {n} | Signals: {n} | Achievements awarded: {n} | New milestones: {list} | Active patterns: {list}
```

---

## V-02 — Axis: Worked Example Promoted to Dedicated SCORE VERIFICATION Step

**Hypothesis:** Elevating the rank-1 calculation to a standalone sub-section with its own `GATE [C-19]` — rather than embedding it as a trailing line after the leaderboard table — makes C-19 structurally unmissable. The verification step also cross-checks the Score column, turning the calc from decoration into an active integrity check. Other gates carry `[C-xx]` labels throughout for C-20.

```markdown
You are running corps-achievements — the Signal plugin's team achievement tracker.
The leaderboard section includes a mandatory SCORE VERIFICATION step that renders the rank-1
calculation inline and cross-checks the Score column for correctness.

---

### STEP 1 — TOPIC DISCOVERY

**GATE [C-01/C-02]:** "All topics below are confirmed by real file paths in `simulations/`. Topics without file evidence: GATE-A: [topic-name] excluded — no confirmed file path. I commit to this list: every topic named here appears in Step 2."

Scan `simulations/` for `{topic}-{signal}-{date}.md`.

| Topic | Signals | Namespaces | Contributors | Latest Signal |
|-------|---------|------------|--------------|---------------|
| {topic} | {n} | {list} | {list} | {date} |

---

### STEP 2 — ACHIEVEMENT REGISTRY

**GATE [C-06/C-07]:** "Two visually separate sections: EARNED ACHIEVEMENTS and NOT YET EARNED. Each uses DEPTH ACHIEVEMENTS and COLLABORATION ACHIEVEMENTS as category labels. Every topic from Step 1 appears in at least one row. Missing: GATE-B: [topic-name] absent from both → halt."

#### EARNED ACHIEVEMENTS

**Category: DEPTH ACHIEVEMENTS**
| Achievement | Topic | Evidence |
|-------------|-------|----------|
| Signal Starter | {topic} | {file path} |
| Multi-Namespace | {topic} | {namespaces} |
| Sprint Complete | {topic} | {count + sprint window} |

**Category: COLLABORATION ACHIEVEMENTS**
| Achievement | Topic | Evidence |
|-------------|-------|----------|
| Pair Signal | {topic} | {contributor names} |
| Cross-Fire | {topic} | {conflict description} |

#### NOT YET EARNED

**Category: DEPTH ACHIEVEMENTS**
| Achievement | Topic | Gap |
|-------------|-------|-----|
| Multi-Namespace | {topic} | needs {n} more namespaces (has {list}) |
| Sprint Complete | {topic} | needs {n} more signals (has {count}) |

**Category: COLLABORATION ACHIEVEMENTS**
| Achievement | Topic | Gap |
|-------------|-------|-----|
| Pair Signal | {topic} | needs second contributor (only {name} has contributed) |
| Cross-Fire | {topic} | needs conflicting-namespace signal |

---

### STEP 3 — TEAM MILESTONES

**GATE [C-03/C-08]:** "All three milestone names appear verbatim. Sprint run date shown."

| Milestone | Status | Evidence |
|-----------|--------|----------|
| **First Team Signal** | ✅/⬜ | {first file or gap} |
| **Shared Coverage** | ✅/⬜ | {topic + contributor names or gap} |
| **Debate Starter** | ✅/⬜ | {topic + conflicting namespaces or gap} |

Run date: {date}

---

### STEP 4 — CONTRIBUTOR LEADERBOARD

**GATE [C-04/C-16]:** "Leaderboard is populated. Weighted formula is explicit and shown before the table."

**Formula: Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)**

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
| 1 | {name} | {n} | {n} | {list} | {n} |

#### SCORE VERIFICATION — Rank 1

**GATE [C-19]:** "I will now render the worked example calculation for the rank-1 contributor. Any reader must be able to verify the Score column entry without reconstruction. If the calc does not match the table, correct the table before proceeding."

Rank-1 verification: **{name}** — Score = {signals}×1 + {topics}×3 + {milestones}×5 = **{total}**

---

### STEP 5 — 1-AWAY CALLOUTS

**GATE [C-09/C-18]:** "Dedicated section. Every row has exactly four columns: Topic, Achievement, Gap (what's missing), Exact Action Needed. No prose substitution. No column omitted per row."

| Topic | Achievement | Gap (what's missing) | Exact Action Needed |
|-------|-------------|----------------------|---------------------|
| {topic} | {achievement} | {specific gap} | Run /{namespace}:{skill} for {topic} |

(Write "No 1-away achievements this sprint" if empty.)

---

### STEP 6 — STAGNATION PATTERN SCAN

**GATE [C-14/C-15/C-17]:** "Only these four labels used. No invented labels. Each active pattern names the specific instance. Gate failure: GATE-D: [topic-name] — pattern label not in registry → halt."

| Label | Pattern | Active? | Specific Instance |
|-------|---------|---------|------------------|
| SOLO_ISLAND | One contributor, no peer coverage | ✅/⬜ | {topic or contributor} |
| NAMESPACE_MOAT | Depth in only one namespace | ✅/⬜ | {topic} |
| SPRINT_FREEZE | No new signals ≥2 sprints | ✅/⬜ | {topic} |
| ORPHAN_TOPIC | Signals exist, no next-action | ✅/⬜ | {topic} |

---

### STEP 7 — TEAM INSIGHT

**GATE [C-10/C-13]:** "Insight is NOT a restatement of any stagnation row above. Formatted as a named artifact with descriptive title. Cross-topic or cross-contributor in scope."

**TEAM INSIGHT — [Descriptive Title]:**
[2–3 sentences. Visible only when looking across all topics. Differs in substance from Step 6 rows.]

---

### STEP 8 — NEXT ACTIONS

**GATE [C-05/C-11/C-12]:** "Each row names: (a) exact action, (b) exact achievement it unlocks, (c) exact stagnation pattern from the Step 6 registry it breaks. Rewrite any row missing a component."

> [Specific Action] → Unlocks **[Achievement Name]** → Breaks **[PATTERN_LABEL from registry]**

Minimum 3 actions.

---

### SPRINT SUMMARY

> Run date: {date} | Topics: {n} | Signals: {n} | Achievements awarded: {n} | Milestones: {earned}/3 | Active patterns: {list}
```

---

## V-03 — Axis: Per-Section Self-Test Gate Per Criterion Pair (Lifecycle Emphasis)

**Hypothesis:** The R4 V-03 architecture — one named self-test gate per section, each targeting its specific aspirational criterion — is already the clearest per-criterion enforcement structure. Upgrading every gate to use `[C-xx]` notation (C-20) and adding a standalone `GATE [C-19]` immediately after the leaderboard table completes the 12-criterion profile without restructuring the section order. This variation is the cleanest upgrade path from the proven R4 baseline.

```markdown
You are running corps-achievements — the Signal plugin's team achievement tracker.
This skill includes a named self-test gate before every section targeting an aspirational criterion.
Gate labels reference criterion IDs to make enforcement auditable against the rubric.

---

### SECTION 1 — WORKSPACE SCAN

**GATE [C-01/C-02]:**
"(1) Every topic I list below is traced to a real file path I observed in `simulations/`. I will not infer or guess topics.
(2) Every topic I list here will appear in the achievement section — I am committing to this list.
If either condition fails: GATE-A: [topic-name] removed — no real file evidence."

Scan `simulations/` for `{topic}-{signal}-{date}.md`. Extract topic slug, namespace, contributor, date.

```
TOPIC REGISTRY
- {topic}: {n} signals | namespaces: {list} | contributors: {list} | latest: {date}
```

---

### SECTION 2 — ACHIEVEMENT AWARDS

**GATE [C-06/C-07]:**
"(1) I will produce two visually separate sections: EARNED ACHIEVEMENTS and NOT YET EARNED.
(2) Each section uses two named category labels: DEPTH ACHIEVEMENTS and COLLABORATION ACHIEVEMENTS.
(3) Every topic from Section 1 appears in at least one row.
If any topic is missing from both sections: GATE-B: [topic-name] absent from both → halt."

**EARNED ACHIEVEMENTS**

Category: DEPTH ACHIEVEMENTS
| Achievement | Topic | Evidence |
|-------------|-------|----------|
| Signal Starter | {topic} | {file} |
| Multi-Namespace | {topic} | {namespaces} |
| Sprint Complete | {topic} | {count + window} |

Category: COLLABORATION ACHIEVEMENTS
| Achievement | Topic | Evidence |
|-------------|-------|----------|
| Pair Signal | {topic} | {contributor names} |
| Cross-Fire | {topic} | {conflict description} |

**NOT YET EARNED**

Category: DEPTH ACHIEVEMENTS
| Achievement | Topic | Gap |
|-------------|-------|-----|
| Multi-Namespace | {topic} | needs {n} more namespaces |
| Sprint Complete | {topic} | needs {n} more signals |

Category: COLLABORATION ACHIEVEMENTS
| Achievement | Topic | Gap |
|-------------|-------|-----|
| Pair Signal | {topic} | needs second contributor |

---

### SECTION 3 — TEAM MILESTONES

**GATE [C-03/C-08]:**
"All three milestone names appear verbatim in the table below. Sprint run date is included in this section."

| Milestone | Status | Evidence |
|-----------|--------|----------|
| **First Team Signal** | ✅/⬜ | {file or gap} |
| **Shared Coverage** | ✅/⬜ | {topic + contributor names or gap} |
| **Debate Starter** | ✅/⬜ | {topic + namespaces or gap} |

Run date: {date}

---

### SECTION 4 — CONTRIBUTOR LEADERBOARD

**GATE [C-04/C-16]:**
"Leaderboard is populated with contributors from the scan. Weighted formula is explicit and shown before the table."

Formula: **Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)**

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
| 1 | {name} | {n} | {n} | {list} | {n} |

**GATE [C-19]:**
"I will now show the worked example calculation for rank-1 so any reader can verify the score without reconstruction."

Rank-1 calculation: Score = {signals}×1 + {topics}×3 + {milestones}×5 = {total}

---

### SECTION 5 — 1-AWAY CALLOUTS

**GATE [C-09/C-18]:**
"(1) This is a dedicated section for achievements one action away from being earned.
(2) Every row has exactly four columns: Topic, Achievement, Gap (what's missing), Exact Action Needed.
(3) I will not use prose. I will not merge or omit any column for any row."

| Topic | Achievement | Gap (what's missing) | Exact Action Needed |
|-------|-------------|----------------------|---------------------|
| {topic} | {achievement} | {specific gap — e.g., "1 more signal in flow namespace"} | Run /{namespace}:{skill} for {topic} |

(Write "No 1-away achievements this sprint" if empty.)

---

### SECTION 6 — STAGNATION PATTERN DIAGNOSIS

**GATE [C-14/C-15/C-17]:**
"(1) I will reference only these four labels: SOLO_ISLAND, NAMESPACE_MOAT, SPRINT_FREEZE, ORPHAN_TOPIC.
(2) I will not invent new labels.
(3) Each active pattern names the specific topic or contributor instance.
(4) Gate failure format: GATE-C: [topic-name] — no matching registry label → halt."

| Label | Active? | Instance |
|-------|---------|---------|
| SOLO_ISLAND | ✅/⬜ | {topic or contributor} |
| NAMESPACE_MOAT | ✅/⬜ | {topic} |
| SPRINT_FREEZE | ✅/⬜ | {topic} |
| ORPHAN_TOPIC | ✅/⬜ | {topic} |

---

### SECTION 7 — TEAM INSIGHT

**GATE [C-10/C-13]:**
"(1) The insight below is NOT a restatement of any stagnation row from Section 6.
(2) It is formatted as a named artifact with a descriptive title using the required format.
(3) It is cross-topic or cross-contributor in scope — not derivable from any single topic view."

**TEAM INSIGHT — [Descriptive Title]:**
[2–3 sentences. Visible only when looking across all topics. Differs in substance from Section 6 rows.]

---

### SECTION 8 — NEXT ACTIONS

**GATE [C-05/C-11/C-12]:**
"(1) Each row names the exact action.
(2) Each row names the exact achievement it unlocks.
(3) Each row names the exact stagnation pattern from the Section 6 registry it breaks.
If any component is missing: rewrite before continuing."

> [Specific Action] → Unlocks **[Achievement Name]** → Breaks **[PATTERN_LABEL from registry]**

Minimum 3 actions. Pattern labels must come from Section 6 registry.

---

### SPRINT SUMMARY

> Run date: {date} | Topics: {n} | Signals: {n} | Achievements awarded: {n} | Milestones: {earned}/3 | Active patterns: {list}
```

---

## V-04 — Axis: Registry-First Architecture + Criterion-ID Gates (Combination)

**Hypothesis:** The R4 V-04 stagnation-registry preamble — vocabulary locked before any generative phase — gives the strongest C-14/C-17 foundation because downstream pattern references anchor to an already-established registry rather than an inline definition. Upgrading with `[C-xx]` gate labels (C-20) and a combined C-04/C-16/C-19 gate on the leaderboard phase closes the two new criteria without altering the registry-first structure that distinguishes this variation.

```markdown
You are running corps-achievements — the Signal plugin's team achievement tracker.

Before generating any output, internalize the following stagnation registry.
Every pattern diagnosis, every next-action label, and every synthesis reference must come from this list.
Do not invent labels. Do not paraphrase labels. Use the exact text.

---

### STAGNATION PATTERN REGISTRY (Established Before All Output)

| Label | What It Describes |
|-------|-------------------|
| SOLO_ISLAND | One contributor owns a topic — no peer has contributed |
| NAMESPACE_MOAT | A topic has depth in exactly one namespace and has not spread |
| SPRINT_FREEZE | A topic has had no new signals for two or more sprint windows |
| ORPHAN_TOPIC | A topic has signals but no next-action has ever been assigned to it |

Registry locked. All pattern references in this run must use exactly these labels.

---

### PHASE 1 — TOPIC DISCOVERY

**GATE [C-01/C-02]:** "All topics I list below are confirmed by real file paths observed in `simulations/`. Topics without a confirmed path: GATE-A: [topic-name] removed — no real file evidence. I commit to this list: every topic here will appear in Phase 2."

Scan `simulations/` for `{topic}-{signal}-{date}.md`. Extract topic slug, namespace, contributor, date.

```
TOPIC REGISTRY
- {topic}: {n} signals | namespaces: {list} | contributors: {list} | latest: {date}
```

---

### PHASE 2 — ACHIEVEMENT AWARDS

**GATE [C-02/C-06/C-07]:** "Every topic from Phase 1 appears in the EARNED or NOT YET EARNED section below. Missing: GATE-B: [topic-name] has no achievement row → halt. Two visually separate sections follow, each organized under two named category labels."

#### EARNED ACHIEVEMENTS

**Category: DEPTH ACHIEVEMENTS**
- Signal Starter — {topic}: {file evidence}
- Multi-Namespace — {topic}: {namespaces}
- Sprint Complete — {topic}: {count + window}

**Category: COLLABORATION ACHIEVEMENTS**
- Pair Signal — {topic}: {contributor names}
- Cross-Fire — {topic}: {conflict description}

#### NOT YET EARNED

**Category: DEPTH ACHIEVEMENTS**
- {achievement} — {topic}: needs {exact gap}

**Category: COLLABORATION ACHIEVEMENTS**
- {achievement} — {topic}: needs {exact gap}

#### TEAM MILESTONES

**GATE [C-03/C-08]:** "All three milestone names appear verbatim. Sprint run date shown."

| Milestone | Status | Evidence |
|-----------|--------|----------|
| **First Team Signal** | ✅/⬜ | {file or gap} |
| **Shared Coverage** | ✅/⬜ | {topic + names or gap} |
| **Debate Starter** | ✅/⬜ | {topic + namespaces or gap} |

Run date: {date}

---

### PHASE 3 — CONTRIBUTOR LEADERBOARD

**GATE [C-04/C-16/C-19]:** "Leaderboard is populated. Weighted formula is explicit. After the table I will render the rank-1 worked example calculation so the score is auditable from raw counts without reconstruction."

Formula: **Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)**

Rationale: Milestone triggers signal the highest-leverage contributions; topic breadth reflects coverage discipline; signals reflect raw activity. The formula is debatable — adjust multipliers to reflect your team's value priorities.

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
| 1 | {name} | {n} | {n} | {list} | {n} |

Rank-1 calculation: Score = {signals}×1 + {topics}×3 + {milestones}×5 = {total}

---

### PHASE 4 — 1-AWAY CALLOUTS

**GATE [C-09/C-18]:** "Dedicated section. Every row has four columns: Topic, Achievement, Gap (what's missing), Exact Action Needed. No prose substitution. No column omitted per row."

| Topic | Achievement | Gap (what's missing) | Exact Action Needed |
|-------|-------------|----------------------|---------------------|
| {topic} | {achievement} | {specific gap} | Run /{namespace}:{skill} for {topic} |

(Write "No 1-away achievements this sprint" if empty.)

---

### PHASE 5 — STAGNATION DIAGNOSIS

**GATE [C-14/C-15/C-17]:** "Reference only labels from the registry established at the top of this skill. Each active pattern names the specific topic or contributor. Gate failure: GATE-C: [topic-name] — label not found in registry → halt."

| Label | Active? | Instance (exact topic or contributor) |
|-------|---------|----------------------------------------|
| SOLO_ISLAND | ✅/⬜ | {topic or contributor} |
| NAMESPACE_MOAT | ✅/⬜ | {topic} |
| SPRINT_FREEZE | ✅/⬜ | {topic} |
| ORPHAN_TOPIC | ✅/⬜ | {topic} |

---

### PHASE 6 — CROSS-TOPIC SYNTHESIS

**GATE [C-10/C-13]:** "The insight below is NOT a restatement of any stagnation row above. It is formatted as a named artifact with a descriptive title. Cross-topic or cross-contributor in scope."

**TEAM INSIGHT — [Descriptive Title]:**
[2–3 sentences. Visible only when looking across all topics. Differs in substance from Phase 5 rows.]

---

### PHASE 7 — NEXT ACTIONS

**GATE [C-05/C-11/C-12]:** "Each row names: (a) the exact action, (b) the exact achievement it unlocks, (c) the exact label from the STAGNATION PATTERN REGISTRY (established before Phase 1) it breaks. If any component is missing: rewrite."

> [Specific Action] → Unlocks **[Achievement Name]** → Breaks **[PATTERN_LABEL from registry]**

Minimum 3 actions. All pattern labels must appear in the registry established at the top.

---

### SPRINT SUMMARY

> Run date: {date} | Topics: {n} | Signals: {n} | Achievements awarded: {n} | Milestones: {earned}/3 | Active patterns: {list}
```

---

## V-05 — Axis: Pre-Flight Maps All 12 Aspirationals + Criterion-ID Gates Per Section (Combination)

**Hypothesis:** A pre-flight table that maps every one of the 12 aspirational criteria (including the new C-19 and C-20) to its section, combined with a standalone `GATE [C-19]` after the leaderboard table, creates the highest enforcement density. The pre-flight makes the complete criterion profile auditable before generation begins; the per-section criterion-ID gates close C-20; the explicit C-19 gate after the leaderboard table ensures the worked example is rendered regardless of how the table section is structured.

```markdown
You are running corps-achievements. Dense enforcement mode.
All 12 aspirational criteria are enforced by structure. Gates reference criterion IDs throughout.

---

## PRE-FLIGHT CHECKS

Before generating any output, confirm each of the following mappings:

| Check | Criterion | Section | Confirmation |
|-------|-----------|---------|-------------|
| Topics confirmed by real file paths | C-01 | Section 1 | "All topics below are real." |
| Every topic appears in achievement rows | C-02 | Sections 2A/2B | "I commit to this list." |
| All 3 milestone names appear verbatim | C-03 | Section 3 | First Team Signal, Shared Coverage, Debate Starter |
| Leaderboard populated with contributors | C-04 | Section 4 | Present and non-empty |
| Each next action names action + achievement | C-05 | Section 8 | Enforced by GATE [C-05/C-12] |
| Earned and available are separate sections | C-06 | Sections 2A and 2B | Two distinct labeled sections |
| Achievements grouped in ≥2 named categories | C-07 | Sections 2A and 2B | DEPTH ACHIEVEMENTS and COLLABORATION ACHIEVEMENTS |
| Sprint date shown | C-08 | Section 3 + Sprint Summary | Date in both locations |
| 1-away dedicated section with 4-column table | C-09/C-18 | Section 5 | Dedicated section, four-column table |
| Named cross-topic insight, non-stagnation | C-10/C-13 | Section 7 | TEAM INSIGHT — [title]: format |
| Pre-write self-test gate per section | C-11 | All sections | One GATE [C-xx] per section |
| Anti-inertia → Unlocks → Breaks format | C-12 | Section 8 | Enforced by GATE [C-05/C-12] |
| Stagnation labels from registry only | C-14/C-17 | Section 6 | Four semantic labels, no invented |
| Gate failures name specific instance | C-15 | All gates | GATE-*: [instance-name] format |
| Weighted formula explicit | C-16 | Section 4 | Formula shown before table |
| Rank-1 worked example rendered inline | C-19 | Section 4 | Enforced by GATE [C-19] after table |
| Gate labels reference criterion IDs | C-20 | All sections | All gates use [C-xx] notation |

Pre-flight complete. Generating output.

---

## SECTION 1 — TOPIC DISCOVERY

**GATE [C-01/C-02]:** "All topics below confirmed by real file paths in `simulations/`. Topics without file evidence: GATE-A: [topic-name] removed — no real file evidence. I commit to this list."

Scan `simulations/` for `{topic}-{signal}-{date}.md`.

| Topic | Signals | Namespaces | Contributors | Latest |
|-------|---------|------------|--------------|--------|
| {topic} | {n} | {list} | {list} | {date} |

---

## SECTION 2A — EARNED ACHIEVEMENTS

**GATE [C-06/C-07]:** "This section lists ONLY earned achievements. Unearned achievements appear in 2B. Both sections use DEPTH ACHIEVEMENTS and COLLABORATION ACHIEVEMENTS as category labels. Every topic from Section 1 appears in 2A or 2B: GATE-B: [topic-name] absent from both → halt."

### DEPTH ACHIEVEMENTS — EARNED

| Achievement | Topic | Evidence |
|-------------|-------|----------|
| Signal Starter | {topic} | {file} |
| Multi-Namespace | {topic} | {namespaces} |
| Sprint Complete | {topic} | {count + window} |

### COLLABORATION ACHIEVEMENTS — EARNED

| Achievement | Topic | Evidence |
|-------------|-------|----------|
| Pair Signal | {topic} | {contributor names} |
| Cross-Fire | {topic} | {conflict description} |

---

## SECTION 2B — NOT YET EARNED

### DEPTH ACHIEVEMENTS — AVAILABLE

| Achievement | Topic | Gap |
|-------------|-------|-----|
| Multi-Namespace | {topic} | needs {n} more namespaces (has {list}) |
| Sprint Complete | {topic} | needs {n} more signals (has {count}) |

### COLLABORATION ACHIEVEMENTS — AVAILABLE

| Achievement | Topic | Gap |
|-------------|-------|-----|
| Pair Signal | {topic} | needs second contributor (only {name}) |
| Cross-Fire | {topic} | needs conflicting-namespace signal |

---

## SECTION 3 — TEAM MILESTONES

**GATE [C-03/C-08]:** "All three milestone names appear verbatim. Sprint run date shown."

| Milestone | Status | Instance |
|-----------|--------|---------|
| **First Team Signal** | ✅/⬜ | {first file or gap} |
| **Shared Coverage** | ✅/⬜ | {topic + contributor names or gap} |
| **Debate Starter** | ✅/⬜ | {topic + conflicting namespaces or gap} |

Run date: {date}

---

## SECTION 4 — CONTRIBUTOR LEADERBOARD

**GATE [C-04/C-16]:** "Leaderboard is populated. Weighted formula is explicit and shown before the table."

**Formula: Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)**

The multipliers encode the team's value judgment: milestone triggers are worth 5× a signal.

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
| 1 | {name} | {n} | {n} | {list} | {n} |

**GATE [C-19]:** "I will now render the rank-1 worked example calculation so any reader can verify the Score column without reconstruction."

Rank-1 calculation: Score = {signals}×1 + {topics}×3 + {milestones}×5 = {total}

---

## SECTION 5 — 1-AWAY ACHIEVEMENTS

**GATE [C-09/C-18]:** "Dedicated section present. Every row has exactly four columns: Topic, Achievement, Gap (what's missing), Exact Action Needed. No row may omit a column. No prose substitution."

| Topic | Achievement | Gap (what's missing) | Exact Action Needed |
|-------|-------------|----------------------|---------------------|
| {topic} | {achievement} | {specific — e.g., "1 scout signal"} | Run /{namespace}:{skill} for {topic} |

(Write "No 1-away achievements this sprint" if empty — do not remove section.)

---

## SECTION 6 — STAGNATION PATTERN SCAN

**GATE [C-14/C-15/C-17]:** "Only these four semantic labels are used. No invented labels. Each active pattern names the specific topic or contributor. Gate failure: GATE-C: [topic-name] — label not in registry → halt."

| Label | Pattern | Active? | Instance |
|-------|---------|---------|---------|
| SOLO_ISLAND | One contributor, no peer coverage | ✅/⬜ | {topic or contributor} |
| NAMESPACE_MOAT | Depth in only one namespace | ✅/⬜ | {topic} |
| SPRINT_FREEZE | No new signals ≥2 sprints | ✅/⬜ | {topic} |
| ORPHAN_TOPIC | Signals exist, no next-action | ✅/⬜ | {topic} |

---

## SECTION 7 — TEAM INSIGHT

**GATE [C-10/C-13]:** "Insight is NOT a restatement of any stagnation row above. Formatted as a named artifact with descriptive title. Cross-topic or cross-contributor in scope."

**TEAM INSIGHT — [Descriptive Title]:**
[2–3 sentences. Visible only when looking across all topics. Differs in substance from Section 6 rows.]

---

## SECTION 8 — NEXT ACTIONS

**GATE [C-05/C-11/C-12]:** "Each row names: (a) exact action, (b) exact achievement it unlocks, (c) exact pattern from Section 6 registry it breaks. Rewrite any row missing a component."

> [Specific Action] → Unlocks **[Achievement Name]** → Breaks **[PATTERN_LABEL from registry]**

Minimum 3 actions.

---

## SPRINT SUMMARY

> Run date: {date} | Topics: {n} | Signals: {n} | Achievements awarded: {n} | New milestones: {list} | Active patterns: {list}
```

---

## Variation Axes Summary

| Variation | Primary Axis | Key Additions vs R4 | New Criteria Addressed |
|-----------|-------------|---------------------|----------------------|
| V-01 | Criterion-ID gate notation throughout | `[C-xx]` label on every gate; combined C-04/C-16/C-19 gate | C-19 (inline instruction in gate), C-20 (ID notation) |
| V-02 | Worked example as dedicated SCORE VERIFICATION sub-step | Standalone `GATE [C-19]` after leaderboard table with cross-check instruction | C-19 (first-class step), C-20 (ID notation throughout) |
| V-03 | Per-section self-test gate per criterion pair | `[C-xx]` added to existing per-section gates; separate `GATE [C-19]` after table | C-19 (own gate), C-20 (ID notation per gate) |
| V-04 | Registry-first + criterion-ID gates | `[C-xx]` labels on all gates; combined C-04/C-16/C-19 gate | C-19 (inline in combined gate), C-20 (ID notation) |
| V-05 | Pre-flight maps all 12 + criterion-ID gates per section | Pre-flight row for C-19/C-20; separate `GATE [C-19]` after table | C-19 (dedicated gate), C-20 (pre-flight + all gate labels) |
