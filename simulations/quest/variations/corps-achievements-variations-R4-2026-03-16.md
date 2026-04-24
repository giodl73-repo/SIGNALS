Written to `simulations/quest/variations/corps-achievements-variations-R4-2026-03-16.md`.

---

## Round 4 Variations — `corps-achievements`

**Rubric:** v4 (5E + 3R + 10A)

### Variation Axes

| Variation | Primary Axis | Key Problem It Solves |
|-----------|-------------|----------------------|
| **V-01** | Full-stack upgrade of R3 V-01 | R3's top scorer (89) missed C-09, C-16, C-18 — adds all three |
| **V-02** | Earned/Available as top-level structure | Both R3 top variations scored PARTIAL on C-06; makes the split the primary organizing principle |
| **V-03** | Self-test gate per aspirational section | One gate per criterion-targeted section, not just per phase — closes criteria one at a time |
| **V-04** | Registry-first architecture | Stagnation registry defined before all output — strongest C-14/C-17 foundation by pre-establishing vocabulary |
| **V-05** | Maximalist dense — all 10 explicitly enforced | Pre-flight checklist maps every section to its criterion; gates per section; structured tables throughout |

### What Changed from R3

- **C-06 fix**: All five variations use two visually separate sections (`EARNED` / `NOT YET EARNED` or `AVAILABLE`) — not just ✅/⬜ interleaved in one list
- **C-16 fix**: All five variations include the explicit formula `Score = Signals×1 + Topics×3 + Milestones×5` with an auditable rank-1 calculation example
- **C-17**: Already passing in R3 (semantic labels) — retained throughout
- **C-18 fix**: All five variations include a 4-column 1-away table (Topic / Achievement / Gap / Exact Action Needed) — no prose substitution allowed
- **V-05 pre-flight**: A criterion-to-section mapping table at the top — the most aggressive enforcement structure seen across all rounds
-slug} → {count} signals → contributors: {list from git or filename metadata}
```

**GATE-A CHECK:** Does every listed topic correspond to a real file path you observed? If any topic cannot be traced to a real file, remove it and append: "GATE-A: [topic-name] removed — no real file evidence."

---

### PHASE 2 — ACHIEVEMENT AWARDS

#### TEAM MILESTONE REGISTRY
Award the following milestones by name (all three must appear by exact name):

| Milestone | Condition | Status | Evidence |
|-----------|-----------|--------|----------|
| **First Team Signal** | ≥1 signal artifact exists | ✅/⬜ | {first file or gap} |
| **Shared Coverage** | ≥2 contributors same topic | ✅/⬜ | {topic + names or gap} |
| **Debate Starter** | ≥1 topic with conflicting-namespace signals | ✅/⬜ | {topic + namespaces or gap} |

#### PER-TOPIC ACHIEVEMENTS

Present achievements in two explicit sections. **EARNED ACHIEVEMENTS** first, then **AVAILABLE BUT NOT YET EARNED**.

**EARNED ACHIEVEMENTS**

List every achievement that is earned. Organize under two named categories:

Category: DEPTH ACHIEVEMENTS (earned)
- Signal Starter — {topic}: {file evidence}
- Multi-Namespace — {topic}: {namespace list}
- Sprint Complete — {topic}: {count + sprint window}

Category: COLLABORATION ACHIEVEMENTS (earned)
- Pair Signal — {topic}: {contributor names}
- Cross-Fire — {topic}: {conflicting signal description}

(Omit any achievement with ⬜ status from this section.)

**AVAILABLE BUT NOT YET EARNED**

List every achievement not yet earned with what is missing:

Category: DEPTH ACHIEVEMENTS (not yet earned)
- Multi-Namespace — {topic}: needs {n} more namespaces (has {current})
- Sprint Complete — {topic}: needs {n} more signals this sprint (has {current})

Category: COLLABORATION ACHIEVEMENTS (not yet earned)
- Pair Signal — {topic}: needs a second contributor
- Cross-Fire — {topic}: needs conflicting signals across namespaces

(Omit any achievement with ✅ status from this section.)

**GATE-B CHECK — BEFORE rendering achievements:**
"Does every topic from Phase 1 appear in at least one achievement row (earned or not-yet-earned)? If not: GATE-B: [missing-topic] has no achievement row → halt."

---

### PHASE 3 — CONTRIBUTOR LEADERBOARD

Rank contributors using the following weighted formula:

> **Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)**

This formula encodes the team's value judgment: milestone triggers are worth 5× a signal, topic breadth is worth 3×. The score makes each contributor's rank auditable from raw counts.

Output as a ranked table:

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
| 1 | {name} | {n} | {n} | {list} | {n} |

Show formula calculation for rank-1 contributor to make the scoring auditable: e.g., "Score = 8×1 + 3×3 + 1×5 = 22."

---

### PHASE 4 — CLOSE-TO-UNLOCK CALLOUTS

Identify every achievement that is one action away from being earned. Output as a structured table — every row must have all four columns populated:

**1-AWAY ACHIEVEMENTS:**

| Topic | Achievement | Gap (what's missing) | Exact Action Needed |
|-------|-------------|----------------------|---------------------|
| {topic} | {achievement name} | {specific gap — e.g., "1 more signal in flow namespace"} | Run /{namespace}:{skill} for {topic} |

(Write "No 1-away achievements this sprint" if empty — do not omit the section.)

---

### PHASE 5 — CROSS-TOPIC SYNTHESIS

**STAGNATION PATTERN REGISTRY:**
Reference only these named patterns. Do not invent new labels.

| Label | Pattern |
|-------|---------|
| SOLO_ISLAND | One contributor owns a topic with no peer coverage |
| NAMESPACE_MOAT | Topic has depth in only one namespace |
| SPRINT_FREEZE | Topic has no new signals in ≥2 sprints |
| ORPHAN_TOPIC | Topic has signals but no next-action pointing to it |

Identify which patterns are active. For each active pattern, name the specific topic or contributor instance that exhibits it (e.g., "SOLO_ISLAND: {topic-path}" — not just "some topics are isolated").

**TEAM INSIGHT:**
State one cross-topic or cross-contributor observation not already captured by any stagnation pattern above. Format as a named artifact:

**TEAM INSIGHT — [Descriptive Title]:**
[2–3 sentences. Must differ from stagnation patterns in substance. Must be visible only when looking across all topics at once.]

---

### PHASE 6 — NEXT ACTIONS

**PRE-WRITE GATE C — BEFORE writing each action row:**
"Does this action name (a) the exact thing to do, (b) the exact achievement it unlocks, and (c) the exact stagnation pattern from the registry it breaks? If not, rewrite before continuing."

For each recommended action, use this exact format:

> [Specific Action] → Unlocks **[Achievement Name]** → Breaks **[PATTERN_LABEL from registry]**

Minimum 3 actions. Each pattern label must come from the Phase 5 registry.

---

### OUTPUT STRUCTURE (Required)

1. **Discovered Topics** (Phase 1 — grounded list)
2. **Team Milestones** (3 named, earned/not earned table)
3. **Earned Achievements** (by category — earned only)
4. **Available Achievements** (by category — not yet earned, with gaps)
5. **Contributor Leaderboard** (weighted formula, score shown)
6. **1-Away Achievements** (4-column table or "none this sprint")
7. **Stagnation Patterns** (registry labels + specific instances)
8. **Team Insight** (named artifact)
9. **Next Actions** (anti-inertia format)
10. **Sprint Summary** — date, topics scanned, signals counted, achievements awarded
```

---

## V-02 — Axis: Earned/Available as Primary Structure

**Hypothesis:** Making EARNED vs AVAILABLE the top-level organizing principle — rather than a secondary visual cue inside category lists — unambiguously satisfies C-06 and creates a cleaner team-facing mental model: "what we have" before "what we want."

```markdown
You are running corps-achievements — the Signal plugin's team achievement tracker.
Primary output structure: WHAT THE TEAM EARNED / WHAT THE TEAM CAN EARN NEXT.

---

### STEP 1 — TOPIC DISCOVERY

**PRE-LIST GATE:** "I will only name topics confirmed by real file paths. Any topic I cannot trace to an actual file is excluded. GATE-A: [topic-name] excluded — no confirmed file path."

Scan `simulations/` for artifacts matching `{topic}-{signal}-{date}.md`.

| Topic | Signals | Namespaces | Contributors | Latest Signal |
|-------|---------|------------|--------------|---------------|
| {topic} | {n} | {list} | {list} | {date} |

---

### STEP 2 — WHAT THE TEAM EARNED THIS SPRINT

All achievements the team has already unlocked. Organized by category.

**PRE-SECTION GATE:** "Every topic from Step 1 appears in at least one earned or available row. Missing: GATE-B: [topic-name] missing → halt."

#### DEPTH ACHIEVEMENTS — EARNED

| Achievement | Topic | Evidence |
|-------------|-------|----------|
| Signal Starter | {topic} | {file path} |
| Multi-Namespace | {topic} | {namespaces list} |
| Sprint Complete | {topic} | {count + window} |

(Omit rows where achievement is not earned.)

#### COLLABORATION ACHIEVEMENTS — EARNED

| Achievement | Topic | Evidence |
|-------------|-------|----------|
| Pair Signal | {topic} | {contributor names} |
| Cross-Fire | {topic} | {conflicting signal description} |

#### TEAM MILESTONES — EARNED

| Milestone | Evidence |
|-----------|----------|
| **First Team Signal** | {first file path} |
| **Shared Coverage** | {topic + contributor names} |
| **Debate Starter** | {topic + namespace conflict} |

(List only earned milestones here. All three must be checked — see NOT YET section for any not earned.)

---

### STEP 3 — WHAT THE TEAM CAN EARN NEXT

All achievements not yet earned, with exact gap and next action.

#### DEPTH ACHIEVEMENTS — NOT YET EARNED

| Achievement | Topic | What's Missing | Exact Gap |
|-------------|-------|---------------|-----------|
| Multi-Namespace | {topic} | {n} more namespaces | has {list}, needs {n} more |
| Sprint Complete | {topic} | {n} more signals | has {count}, needs 5 in window |

#### COLLABORATION ACHIEVEMENTS — NOT YET EARNED

| Achievement | Topic | What's Missing | Exact Gap |
|-------------|-------|---------------|-----------|
| Pair Signal | {topic} | Second contributor | only {name} has contributed |
| Cross-Fire | {topic} | Conflicting namespace signal | add scout or review signal |

#### TEAM MILESTONES — NOT YET EARNED

| Milestone | What's Missing |
|-----------|---------------|
| **First Team Signal** | No signal artifacts found anywhere |
| **Shared Coverage** | No topic has ≥2 contributors yet |
| **Debate Starter** | No topic has conflicting-namespace signals |

(Only list milestones NOT yet earned. If all three are earned, write "All team milestones earned this sprint.")

---

### STEP 4 — 1-AWAY CALLOUTS

Achievements where one more action closes the gap. Every row must have all four columns.

| Topic | Achievement | Gap (what's missing) | Exact Action Needed |
|-------|-------------|----------------------|---------------------|
| {topic} | {achievement} | {specific: "1 signal in flow namespace"} | Run /{namespace}:{skill} for {topic} |

(Write "No 1-away achievements this sprint" if empty.)

---

### STEP 5 — CONTRIBUTOR LEADERBOARD

Weighted formula: **Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)**

The formula makes rank auditable from raw counts and encodes the team's priorities.

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
| 1 | {name} | {n} | {n} | {list} | {n} |

---

### STEP 6 — STAGNATION PATTERNS

Use only these labels. Do not invent new labels.

| Label | Active? | Instance (name exact topic or contributor) |
|-------|---------|---------------------------------------------|
| SOLO_ISLAND | ✅/⬜ | {topic: e.g., "flow-trigger — only alex has contributed"} |
| NAMESPACE_MOAT | ✅/⬜ | {topic: e.g., "scout-feasibility — only scout namespace"} |
| SPRINT_FREEZE | ✅/⬜ | {topic: e.g., "flow-lifecycle — last signal 2026-02-28"} |
| ORPHAN_TOPIC | ✅/⬜ | {topic: e.g., "listen-support — 3 signals, no next-action"} |

---

### STEP 7 — TEAM INSIGHT

State one cross-topic or cross-contributor observation not already captured by any stagnation row above.

**TEAM INSIGHT — [Descriptive Title]:**
[2–3 sentences. Cross-topic or cross-contributor scope. Must differ in substance from the stagnation table rows.]

---

### STEP 8 — NEXT ACTIONS

**PRE-ROW GATE:** "Does this row name: (a) specific action, (b) exact achievement it unlocks, (c) stagnation pattern from the registry it breaks? If not — rewrite before continuing."

> [Specific Action] → Unlocks **[Achievement Name]** → Breaks **[PATTERN_LABEL from registry]**

Give 3–5 actions, highest impact first.

---

### SPRINT SUMMARY

> Run date: {date} | Topics scanned: {n} | Signals: {n} | Achievements awarded: {n} | New milestones: {list} | Active patterns: {list}
```

---

## V-03 — Axis: Self-Test Gate Per Aspirational Section

**Hypothesis:** Naming an explicit self-test gate for every section that targets an aspirational criterion — not just discovery and action rows — closes the criterion-by-criterion gaps that arise when gates are only at phase boundaries. A gate per aspirational section forces structural compliance one section at a time.

```markdown
You are running corps-achievements — the Signal plugin's team achievement tracker.
This skill includes a named self-test gate before every section that targets an aspirational criterion.

---

### SECTION 1 — WORKSPACE SCAN

**GATE [C-01/C-02] — Before listing topics:**
"(1) Every topic below is traced to a real file path I observed in `simulations/`. I will not infer topics.
(2) Every topic listed here will appear in the achievement section. I am committing to this list.
If either fails: GATE-A: [topic-name] removed — no real file evidence."

Scan `simulations/` for `{topic}-{signal}-{date}.md`. Extract topic slug, namespace, contributor, date.

```
TOPIC REGISTRY
- {topic}: {n} signals | namespaces: {list} | contributors: {list} | latest: {date}
```

---

### SECTION 2 — ACHIEVEMENT AWARDS

**GATE [C-06/C-07] — Before rendering achievements:**
"(1) I will produce two visually separate sections: EARNED and NOT YET EARNED.
(2) Each section is organized under two named category labels: DEPTH ACHIEVEMENTS and COLLABORATION ACHIEVEMENTS.
If any topic from Section 1 is missing from both sections: GATE-B: [topic-name] missing → halt."

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
| Pair Signal | {topic} | {names} |
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

All three must appear by exact name (C-03):

| Milestone | Status | Evidence |
|-----------|--------|----------|
| **First Team Signal** | ✅/⬜ | {file or gap} |
| **Shared Coverage** | ✅/⬜ | {topic + names or gap} |
| **Debate Starter** | ✅/⬜ | {topic + namespaces or gap} |

---

### SECTION 4 — CONTRIBUTOR LEADERBOARD

**GATE [C-16] — Before writing scores:**
"Each contributor's score is computed from the weighted formula: Score = Signals×1 + Topics×3 + Milestones×5.
I will show the formula and show the calculation for rank-1 so the score is auditable."

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
| 1 | {name} | {n} | {n} | {list} | {n} |

Rank-1 calculation: Score = {n}×1 + {n}×3 + {n}×5 = {total}.

---

### SECTION 5 — 1-AWAY CALLOUTS

**GATE [C-09/C-18] — Before writing 1-away rows:**
"(1) This section is dedicated to achievements that are one action away.
(2) Every row has four columns: Topic, Achievement, Gap (what's missing), Exact Action Needed.
I will not use prose. I will not merge or omit any column for any row."

| Topic | Achievement | Gap (what's missing) | Exact Action Needed |
|-------|-------------|----------------------|---------------------|
| {topic} | {achievement} | {specific gap} | Run /{namespace}:{skill} for {topic} |

(Write "No 1-away achievements this sprint" if empty.)

---

### SECTION 6 — STAGNATION PATTERNS

**GATE [C-14/C-17] — Before diagnosing patterns:**
"I will reference only these four labels: SOLO_ISLAND, NAMESPACE_MOAT, SPRINT_FREEZE, ORPHAN_TOPIC.
I will not invent new labels. Each active pattern names the specific topic or contributor instance.
Format: [LABEL]: {specific instance} — not a generic description."

| Label | Active? | Instance |
|-------|---------|---------|
| SOLO_ISLAND | ✅/⬜ | {topic or contributor} |
| NAMESPACE_MOAT | ✅/⬜ | {topic} |
| SPRINT_FREEZE | ✅/⬜ | {topic} |
| ORPHAN_TOPIC | ✅/⬜ | {topic} |

---

### SECTION 7 — TEAM INSIGHT

**GATE [C-10/C-13] — Before writing insight:**
"(1) The insight below is NOT a restatement of any stagnation row above.
(2) It is formatted as a named artifact with a descriptive title in the required format.
(3) It is cross-topic or cross-contributor in scope."

**TEAM INSIGHT — [Descriptive Title]:**
[2–3 sentences. Visible only by looking across all topics. Differs in substance from stagnation table.]

---

### SECTION 8 — NEXT ACTIONS

**GATE [C-05/C-11/C-12] — Before each action row:**
"(1) This action names the exact thing to do.
(2) This action names the exact achievement it unlocks.
(3) This action names the exact stagnation pattern from the registry it breaks.
If any component is missing: rewrite before continuing."

> [Specific Action] → Unlocks **[Achievement Name]** → Breaks **[PATTERN_LABEL from registry]**

Minimum 3 actions. Pattern labels must come from Section 6 registry.

---

### SPRINT SUMMARY

> Run date: {date} | Topics: {n} | Signals: {n} | Achievements awarded: {n} | Milestones: {earned} | Active patterns: {list}
```

---

## V-04 — Axis: Registry-Anchored Architecture (Stagnation Registry Defined First)

**Hypothesis:** Defining the stagnation registry as a preamble — before discovery, before awards, before any output — creates the strongest C-14/C-17 enforcement. All downstream diagnoses anchor to the registry because it was established before the model entered any generative mode. This also makes the anti-inertia framing (C-12) more natural because the registry is already in scope.

```markdown
You are running corps-achievements — the Signal plugin's team achievement tracker.

Before generating any output, internalize the following registry. Every stagnation diagnosis,
every next-action pattern reference, and every synthesis label must come from this list.
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

**PRE-LIST GATE — BEFORE naming topics:**
"All topics I list below are confirmed by real file paths observed in `simulations/`. Topics without a confirmed file path: GATE-A: [topic-name] removed — no real file evidence."

Scan `simulations/` for `{topic}-{signal}-{date}.md`. Extract topic slug, namespace, contributor, date.

```
TOPIC REGISTRY
- {topic}: {n} signals | namespaces: {list} | contributors: {list} | latest: {date}
```

---

### PHASE 2 — ACHIEVEMENT AWARDS

**GATE-B BEFORE RENDERING:**
"Every topic from Phase 1 appears in the earned or not-yet-earned sections below.
Missing: GATE-B: [topic-name] has no achievement row → halt."

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

#### TEAM MILESTONES (all three by exact name)

| Milestone | Status | Evidence |
|-----------|--------|----------|
| **First Team Signal** | ✅/⬜ | {file or gap} |
| **Shared Coverage** | ✅/⬜ | {topic + names or gap} |
| **Debate Starter** | ✅/⬜ | {topic + namespaces or gap} |

---

### PHASE 3 — CONTRIBUTOR LEADERBOARD

Formula: **Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)**

Rationale: milestone triggers signal the highest-leverage team contributions; topic breadth reflects coverage discipline; individual signals reflect raw activity. The formula is debatable — adjust multipliers to reflect your team's value priorities.

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
| 1 | {name} | {n} | {n} | {list} | {n} |

---

### PHASE 4 — 1-AWAY CALLOUTS

One-action-away achievements. Every row must have all four columns — no prose substitution.

| Topic | Achievement | Gap (what's missing) | Exact Action Needed |
|-------|-------------|----------------------|---------------------|
| {topic} | {achievement} | {specific gap} | Run /{namespace}:{skill} for {topic} |

(Write "No 1-away achievements this sprint" if empty.)

---

### PHASE 5 — STAGNATION DIAGNOSIS

Reference only labels from the registry established at the top of this skill. Each active pattern must name the specific topic or contributor that exhibits it.

| Label | Active? | Instance (exact topic or contributor) |
|-------|---------|----------------------------------------|
| SOLO_ISLAND | ✅/⬜ | {topic or contributor} |
| NAMESPACE_MOAT | ✅/⬜ | {topic} |
| SPRINT_FREEZE | ✅/⬜ | {topic} |
| ORPHAN_TOPIC | ✅/⬜ | {topic} |

---

### PHASE 6 — CROSS-TOPIC SYNTHESIS

State one observation that is visible only when looking across all topics — not a restatement of any stagnation row.

**TEAM INSIGHT — [Descriptive Title]:**
[2–3 sentences. Cross-topic or cross-contributor in scope. Must differ in substance from Phase 5 rows.]

---

### PHASE 7 — NEXT ACTIONS

**PRE-ROW GATE (run before each action):**
"Does this row name: (a) the exact action, (b) the exact achievement it unlocks, (c) the exact label from the STAGNATION PATTERN REGISTRY (established at the top) that it breaks? If any component is missing, rewrite."

> [Specific Action] → Unlocks **[Achievement Name]** → Breaks **[PATTERN_LABEL from registry]**

Minimum 3 actions. All pattern labels must appear in the registry established before Phase 1.

---

### SPRINT SUMMARY

> Run date: {date} | Topics: {n} | Signals: {n} | Achievements awarded: {n} | Milestones: {earned} | Active patterns: {list}
```

---

## V-05 — Axis: Maximalist Dense (All 10 Aspirationals Explicitly Enforced)

**Hypothesis:** A fully table-driven format that explicitly targets all 10 aspirational criteria through structural enforcement — not just prose instruction — produces the highest aspirational pass rate by leaving no room for partial or omitted sections.

```markdown
You are running corps-achievements. Dense output. Tables for all structured data.
All 10 aspirational criteria are enforced by structure.

---

## PRE-FLIGHT CHECKS

Before generating any output, confirm each of the following:

| Check | Criterion | Confirmation |
|-------|-----------|-------------|
| Topics will be confirmed by real file paths | C-01 | State: "All topics below are real." |
| Every topic will appear in achievement rows | C-02 | State: "I commit to this topic list." |
| All 3 milestone names appear verbatim | C-03 | Names: First Team Signal, Shared Coverage, Debate Starter |
| Leaderboard will be populated | C-04 | Present in Section 4 |
| Each next action names action + achievement | C-05 | Enforced by pre-row gate |
| Earned and not-yet-earned are separate sections | C-06 | Sections 2A and 2B |
| Achievements grouped in 2 named categories | C-07 | DEPTH and COLLABORATION |
| Sprint date shown | C-08 | Sprint Summary |
| 1-away dedicated section with 4-column table | C-09/C-18 | Section 5 |
| Named cross-topic insight, non-stagnation | C-10/C-13 | Section 7 |
| Pre-write self-test gate per section | C-11 | One gate per numbered section |
| Anti-inertia → Unlocks → Breaks format | C-12 | Section 8 |
| Stagnation labels from registry only | C-14/C-17 | Registry at Section 6 |
| Gate failures name specific failing instance | C-15 | All GATE-* messages |
| Weighted formula shown and auditable | C-16 | Section 4 with calc example |

Pre-flight complete. Generating output.

---

## SECTION 1 — TOPIC DISCOVERY

**GATE [C-01/C-02]:** "All topics below confirmed by real file paths. Topics without file evidence: GATE-A: [topic-name] removed — no real file evidence."

Scan `simulations/` for `{topic}-{signal}-{date}.md`.

| Topic | Signals | Namespaces | Contributors | Latest |
|-------|---------|------------|--------------|--------|
| {topic} | {n} | {list} | {list} | {date} |

---

## SECTION 2A — EARNED ACHIEVEMENTS

**GATE [C-06/C-07]:** "This section lists ONLY earned achievements. Unearned achievements appear in 2B. Both sections use DEPTH and COLLABORATION as category labels. Every topic from Section 1 appears in 2A or 2B: GATE-B: [topic-name] missing from both → halt."

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

## SECTION 2B — AVAILABLE BUT NOT YET EARNED

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

**GATE [C-03]:** "All three milestone names appear verbatim below."

| Milestone | Status | Instance |
|-----------|--------|---------|
| **First Team Signal** | ✅/⬜ | {first file or gap} |
| **Shared Coverage** | ✅/⬜ | {topic + contributor names or gap} |
| **Debate Starter** | ✅/⬜ | {topic + conflicting namespaces or gap} |

---

## SECTION 4 — CONTRIBUTOR LEADERBOARD

**GATE [C-04/C-16]:** "Leaderboard is populated. Score formula is explicit and auditable from raw counts."

**Formula: Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)**

The multipliers encode the team's value judgment: milestone triggers are worth 5× a raw signal.

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
| 1 | {name} | {n} | {n} | {list} | {n} |

Rank-1 calculation: Score = {n}×1 + {n}×3 + {n}×5 = {total}

---

## SECTION 5 — 1-AWAY ACHIEVEMENTS

**GATE [C-09/C-18]:** "Dedicated section present. Every row has exactly four columns: Topic, Achievement, Gap, Exact Action Needed. No row may omit a column. No prose substitution."

| Topic | Achievement | Gap (what's missing) | Exact Action Needed |
|-------|-------------|----------------------|---------------------|
| {topic} | {achievement} | {specific — e.g., "1 scout signal"} | Run /{namespace}:{skill} for {topic} |

(Write "No 1-away achievements this sprint" if empty — do not remove section.)

---

## SECTION 6 — STAGNATION PATTERN REGISTRY SCAN

**GATE [C-14/C-17]:** "Only these four labels are used below. No invented labels. Each active pattern names the specific topic or contributor instance."

| Label | Pattern | Active? | Instance |
|-------|---------|---------|---------|
| SOLO_ISLAND | One contributor, no peer coverage | ✅/⬜ | {topic or contributor} |
| NAMESPACE_MOAT | Depth in only one namespace | ✅/⬜ | {topic} |
| SPRINT_FREEZE | No new signals ≥2 sprints | ✅/⬜ | {topic} |
| ORPHAN_TOPIC | Signals exist, no next-action | ✅/⬜ | {topic} |

---

## SECTION 7 — TEAM INSIGHT

**GATE [C-10/C-13]:** "The insight below is NOT a restatement of any stagnation row above. It is formatted as a named artifact with a descriptive title. It is cross-topic or cross-contributor in scope."

**TEAM INSIGHT — [Descriptive Title]:**
[2–3 sentences. Visible only when looking across all topics. Differs in substance from Section 6 rows.]

---

## SECTION 8 — NEXT ACTIONS

**GATE [C-05/C-11/C-12]:** "Each row below names: (a) exact action, (b) exact achievement it unlocks, (c) exact pattern from Section 6 registry it breaks. If any component missing: rewrite."

> [Specific Action] → Unlocks **[Achievement Name]** → Breaks **[PATTERN_LABEL from registry]**

Minimum 3 actions.

---

## SPRINT SUMMARY

> Run date: {date} | Topics: {n} | Signals: {n} | Achievements awarded: {n} | New milestones: {list} | Active patterns: {list}
```

---

### Variation Axes Summary

| Variation | Primary Axis | Key Additions vs R3 | Hypothesis |
|-----------|-------------|---------------------|-----------|
| V-01 | Full-stack upgrade of R3 V-01 | C-06 (earned/available split), C-16 (formula), C-18 (4-column table) | Best R3 architecture + targeted additions = highest score |
| V-02 | Earned/Available as top-level structure | C-06 as primary organizing principle; all other v4 criteria included | Top-level split is clearer than column-level visual cue |
| V-03 | Self-test gate per aspirational section | Named gate per criterion-targeted section, not just per phase | Per-criterion gates force section-by-section structural compliance |
| V-04 | Registry-first architecture | Stagnation registry defined before all output; all downstream anchors to it | Pre-established registry creates strongest C-14/C-17 foundation |
| V-05 | Maximalist dense / all 10 aspirationals | Pre-flight checklist + gate per section + explicit formula calc | Criterion-mapped design with no gaps scores highest aspirational count |
