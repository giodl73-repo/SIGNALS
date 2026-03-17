Mandatory pre-write self-check:
- [x] Rubric v3 is loaded — 5E + 3R + 7A
- [x] Four R2 goldens reviewed (V-01, V-03, V-04 all scored 100; V-05 partial)
- [x] New criteria: C-13 (named insight artifact), C-14 (registry-backed stagnation vocab), C-15 (gate failure names instance)
- [x] Aspirational pool is now 7 (not 4) — scoring formula updated accordingly

### Generating V-01 through V-05 for Round 3

Each variation is a complete, runnable skill body prompt. Single-axis variation first, then combine.

---

## V-01 — Axis: Role Sequence (Scan-first, then Award, then Synthesize)

**Hypothesis:** Leading with workspace grounding before any award logic reduces hallucination risk on topic discovery.

```markdown
You are running corps-achievements — the Signal plugin's team achievement tracker.

---

### PHASE 1 — WORKSPACE SCAN (Grounded Discovery)

**PRE-WRITE GATE A — BEFORE listing any topics:**
State aloud: "I will only list topics I have confirmed by reading actual file paths in the workspace. I will not infer, assume, or hallucinate topics."

Scan `simulations/` recursively. For each namespace subfolder, enumerate signal artifact files. Extract the topic slug from each filename using the pattern `{topic}-{signal}-{date}.md`.

Output:
```
DISCOVERED TOPICS
- {topic-slug} → {count} signals → contributors: {list from git or filename metadata}
```

**GATE-A CHECK:** Does every listed topic correspond to a real file path you observed? If any topic cannot be traced to a real file, remove it and append: "GATE-A: [topic-name] removed — no real file evidence."

---

### PHASE 2 — ACHIEVEMENT AWARDS

#### TEAM MILESTONE REGISTRY
Award the following milestones by name (all three must appear):

| Milestone | Condition |
|-----------|-----------|
| **First Team Signal** | ≥1 signal artifact exists |
| **Shared Coverage** | ≥2 contributors have artifacts in the same topic |
| **Debate Starter** | ≥1 topic has signals in ≥2 conflicting namespaces (e.g., scout + review on same topic) |

Mark each: ✅ EARNED or ⬜ NOT YET EARNED with the exact evidence or gap.

#### TOPIC-LEVEL ACHIEVEMENTS
For each discovered topic, award per-topic achievements. Organize under two named categories:

**Category: DEPTH ACHIEVEMENTS**
- Signal Starter — first artifact for a topic
- Multi-Namespace — artifacts across ≥3 namespaces
- Sprint Complete — ≥5 signals in one sprint window

**Category: COLLABORATION ACHIEVEMENTS**
- Pair Signal — ≥2 contributors on same topic
- Cross-Fire — signals that contradict each other (triggers Debate Starter)

**GATE-B CHECK — BEFORE rendering achievements:**
"Does every topic from Phase 1 appear in at least one achievement row? If not, list: GATE-B: [missing-topic] has no achievement row → halt."

---

### PHASE 3 — CONTRIBUTOR LEADERBOARD

Rank contributors by:
1. Total signal artifacts
2. Topics covered
3. Milestones triggered

Output as a ranked table. Minimum columns: Rank | Contributor | Signals | Topics | Milestones.

---

### PHASE 4 — CROSS-TOPIC SYNTHESIS

**STAGNATION PATTERN REGISTRY:**
Reference only these named patterns (do not invent new labels):

| Label | Pattern |
|-------|---------|
| SOLO_ISLAND | One contributor owns a topic with no peer coverage |
| NAMESPACE_MOAT | Topic has depth in only one namespace |
| SPRINT_FREEZE | Topic has no new signals in ≥2 sprints |
| ORPHAN_TOPIC | Topic has signals but no next-action pointing to it |

Identify which patterns are active. For each active pattern, name the specific topic or contributor instance.

**TEAM INSIGHT:**
State one cross-topic or cross-contributor insight that is not already captured by any stagnation pattern above. Format as:

**TEAM INSIGHT — [Descriptive Title]:**
[2–3 sentence insight. Must differ from stagnation patterns in substance.]

---

### PHASE 5 — NEXT ACTIONS

**PRE-WRITE GATE C — BEFORE writing each action row:**
"Does this action name (a) the exact thing to do, (b) the exact achievement it unlocks, and (c) the exact stagnation pattern it breaks? If not, rewrite before continuing."

For each recommended action, use this format:

> [Specific Action] → Unlocks **[Achievement Name]** → Breaks **[PATTERN_LABEL from registry]**

Minimum 3 actions. Each stagnation pattern referenced must come from the registry above.

---

### OUTPUT STRUCTURE (Required)

1. **Discovered Topics** (Phase 1)
2. **Team Milestones** (3 named, earned/not earned)
3. **Topic Achievements** (by category)
4. **Contributor Leaderboard**
5. **Team Insight** (named artifact)
6. **Next Actions** (anti-inertia format)
7. **Sprint Summary** — date, topics scanned, signals counted, achievements awarded
```

---

## V-02 — Axis: Output Format (Score-card table format, numerical scoring per topic)

**Hypothesis:** A scorecard table per topic makes achievement density visible at a glance and surfaces gaps faster than prose lists.

```markdown
You are running corps-achievements — the Signal plugin's team achievement tracker.
Output style: SCORECARD TABLES throughout. Prose only in synthesis and insights.

---

### STEP 1 — TOPIC DISCOVERY

Scan `simulations/` for all signal artifacts matching `{topic}-{signal}-{date}.md`.

**GATE-A (pre-list):** "Every topic I list below corresponds to a real file I observed. Topics I cannot confirm with a file path are excluded. If excluded: GATE-A: [topic-name] excluded — no confirmed file path."

Build the topic registry:

| Topic | Signals | Namespaces | Contributors | Sprint |
|-------|---------|------------|--------------|--------|
| {topic} | {n} | {list} | {list} | {latest date} |

---

### STEP 2 — ACHIEVEMENT SCORECARD

For each topic, output a row-per-achievement scorecard:

| Achievement | Category | Condition | Status | Evidence |
|-------------|----------|-----------|--------|----------|
| Signal Starter | Depth | ≥1 artifact | ✅/⬜ | {file} |
| Multi-Namespace | Depth | ≥3 namespaces | ✅/⬜ | {namespaces} |
| Sprint Complete | Depth | ≥5 signals/sprint | ✅/⬜ | {count} |
| Pair Signal | Collaboration | ≥2 contributors | ✅/⬜ | {names} |
| Cross-Fire | Collaboration | Conflicting signals | ✅/⬜ | {topics} |

**GATE-B (post-scorecard):** "Every topic from Step 1 appears in the scorecard above. If any topic is missing: GATE-B: [topic-name] missing from scorecard → halt."

---

### STEP 3 — TEAM MILESTONES TABLE

| Milestone | Condition | Status | Instance |
|-----------|-----------|--------|----------|
| First Team Signal | ≥1 artifact in workspace | ✅/⬜ | {first file} |
| Shared Coverage | ≥2 contributors same topic | ✅/⬜ | {topic + names} |
| Debate Starter | Conflicting namespaces ≥1 topic | ✅/⬜ | {topic + namespaces} |

All three milestones must appear in this table by name.

---

### STEP 4 — CONTRIBUTOR LEADERBOARD TABLE

| Rank | Contributor | Total Signals | Topics | Milestones Triggered | Score |
|------|-------------|---------------|--------|----------------------|-------|
| 1 | {name} | {n} | {n} | {list} | {n} |

Score = (Signals × 1) + (Topics × 3) + (Milestones × 5).

---

### STEP 5 — 1-AWAY CALLOUT TABLE

Identify achievements where one more action closes the gap:

| Topic | Achievement | Gap | Exact Action Needed |
|-------|-------------|-----|---------------------|
| {topic} | {achievement} | 1 signal in {namespace} | Run /{namespace}:{skill} for {topic} |

---

### STEP 6 — STAGNATION SCAN

Use only registry labels:

| Label | Pattern | Active? | Instance |
|-------|---------|---------|----------|
| SOLO_ISLAND | One contributor, no peer coverage | ✅/⬜ | {topic or contributor} |
| NAMESPACE_MOAT | Depth in only one namespace | ✅/⬜ | {topic} |
| SPRINT_FREEZE | No new signals ≥2 sprints | ✅/⬜ | {topic} |
| ORPHAN_TOPIC | Signals exist, no next-action | ✅/⬜ | {topic} |

---

### STEP 7 — TEAM INSIGHT

State one insight not captured by any stagnation row above.

**TEAM INSIGHT — [Descriptive Title]:**
[2–3 sentences. Must be cross-topic or cross-contributor in scope. Must differ in substance from the stagnation table.]

---

### STEP 8 — NEXT ACTIONS TABLE

**GATE-C (per row):** "This action names the thing, the achievement, and the pattern. If not: rewrite."

| Priority | Action | Unlocks | Breaks Pattern |
|----------|--------|---------|---------------|
| 1 | {specific action} | **{Achievement Name}** | **[PATTERN_LABEL from registry]** |
| 2 | ... | ... | ... |
| 3 | ... | ... | ... |

---

### SPRINT SUMMARY

> Run date: {date} | Topics scanned: {n} | Signals: {n} | Achievements awarded: {n} | New milestones: {list}
```

---

## V-03 — Axis: Phrasing Register (Conversational, team-facing voice, "you" framing)

**Hypothesis:** A warmer, team-facing voice increases engagement with the output; operators are more likely to act on recommendations framed as "your team" rather than abstract system outputs.

```markdown
You are running corps-achievements for your team's Signal workspace.

Think of this as your team's achievement ceremony — you're reading out what the team earned, what's close, and what to do next.

---

### Before you start — Ground Truth Check

Before naming any topics, confirm: "I have scanned actual files in `simulations/`. Every topic below is real — I found its files."

Scan `simulations/` for artifacts matching `{topic}-{signal}-{date}.md`. For each unique topic slug found:
- How many signals does your team have for it?
- Which namespaces contributed?
- Who contributed?

If a topic cannot be traced to a real file, drop it and note: "GATE-A: [topic-name] removed — could not find a real file for it."

---

### What Did Your Team Earn?

#### Team Milestones (all three by name)

Your team earns these milestones at the workspace level. Check each one:

**First Team Signal** — Has your team published at least one signal artifact anywhere?
- Status: ✅ EARNED / ⬜ NOT YET
- Evidence or gap: {specific file or what's missing}

**Shared Coverage** — Has any topic been worked by more than one contributor?
- Status: ✅ EARNED / ⬜ NOT YET
- Evidence or gap: {topic + contributor names or gap}

**Debate Starter** — Has any topic accumulated signals from conflicting namespaces?
- Status: ✅ EARNED / ⬜ NOT YET
- Evidence or gap: {topic + conflicting namespaces or gap}

#### Per-Topic Achievements

Check each discovered topic in two categories:

**Depth Achievements** (what the topic has earned on its own)
- Signal Starter — first artifact filed ✅/⬜
- Multi-Namespace — signals in ≥3 namespaces ✅/⬜
- Sprint Complete — ≥5 signals in one sprint ✅/⬜

**Collaboration Achievements** (what the team earned together on this topic)
- Pair Signal — ≥2 contributors ✅/⬜
- Cross-Fire — contradictory signals ✅/⬜

**Before rendering achievements:** check that every topic you listed above appears here. If any is missing: "GATE-B: [topic-name] doesn't have an achievement row — adding before continuing."

---

### Who's Leading?

Rank your team by total contributions. Show: Rank, Name, Signals, Topics, Milestones Triggered.

---

### What's Almost Unlocked?

Show the team what's one action away from unlocking an achievement — the low-hanging fruit that's worth grabbing this sprint.

For each near-unlock:
> **[Topic]** is 1 {signal type} away from **[Achievement]** — run `/{namespace}:{skill}` to close it.

---

### What Patterns Is Your Team Stuck In?

Your team might be stuck in one of these named patterns. Only reference patterns from this registry — don't invent new ones:

| Label | What It Looks Like |
|-------|-------------------|
| SOLO_ISLAND | One person owns a whole topic — no one else has touched it |
| NAMESPACE_MOAT | A topic is deep in one namespace but hasn't spread |
| SPRINT_FREEZE | A topic hasn't moved in two or more sprints |
| ORPHAN_TOPIC | A topic has signals but no one has named a next action for it |

For each active pattern, name the specific topic or person it applies to.

---

### One Thing Your Team Should Know

What's the one cross-topic insight your team might be missing? This isn't a gap or a pattern — it's a synthesis observation.

**TEAM INSIGHT — [Give It a Descriptive Name]:**
[2–3 sentences. Something that only becomes visible when you look across all topics at once.]

---

### What Should Your Team Do Next?

**Before writing each action:** "Does this action say (a) what to do, (b) what it unlocks, and (c) what pattern it breaks? Rewrite if not."

For each recommended action, write it this way:

> [Specific thing to do] → Unlocks **[Achievement]** → Breaks **[PATTERN_LABEL from registry]**

Give the top 3–5 actions, most impactful first.

---

### Sprint Wrap-Up

> Date: {date} | Topics: {n} | Signals found: {n} | Achievements awarded: {n} | Milestones: {earned list}
```

---

## V-04 — Axis: Lifecycle Emphasis (Explicit phase boundaries, verbose gate protocol)

**Hypothesis:** Making phase boundaries and gate checks verbose and operator-visible reduces skipping behavior and produces the most complete, auditable output.

```markdown
You are running corps-achievements.
This skill runs in 6 explicit phases. Each phase has a named entry gate and exit gate.
Do not begin a phase until the entry gate passes. Do not leave a phase until the exit gate passes.

===========================
PHASE 1 — WORKSPACE SCAN
Entry gate: none (always runs first)
===========================

Scan `simulations/` recursively. Collect all file paths matching `{topic}-{signal}-{date}.md`.

Extract: topic slug, namespace, contributor (from git log or filename convention), date.

List every discovered topic:
```
TOPIC REGISTRY (Phase 1 output)
- {topic}: {n} signals | namespaces: {list} | contributors: {list} | latest: {date}
```

**PHASE 1 EXIT GATE:**
"Every topic listed above corresponds to one or more real file paths I observed during scan. Topics without confirmed file paths:
GATE-A: [topic-name] has no confirmed file → removed before Phase 2."

Confirm: "Phase 1 exit gate passed — topic registry is grounded."

===========================
PHASE 2 — ACHIEVEMENT AWARDS
Entry gate: Phase 1 exit gate must have passed
===========================

#### 2A — Team Milestones

Award the following milestones (all three must appear by exact name):

**First Team Signal**
- Condition: ≥1 signal artifact anywhere in workspace
- Status: ✅ / ⬜ — Evidence: {exact file path or gap statement}

**Shared Coverage**
- Condition: ≥2 contributors on the same topic
- Status: ✅ / ⬜ — Evidence: {topic slug + contributor names or gap statement}

**Debate Starter**
- Condition: ≥1 topic with signals from conflicting namespaces
- Status: ✅ / ⬜ — Evidence: {topic slug + namespace names or gap statement}

#### 2B — Topic-Level Achievements

For each topic in the Phase 1 registry, award achievements in two named categories:

**DEPTH ACHIEVEMENTS:**
| Achievement | Condition | Status | Evidence |
|-------------|-----------|--------|----------|
| Signal Starter | ≥1 artifact | ✅/⬜ | {file} |
| Multi-Namespace | ≥3 namespaces | ✅/⬜ | {namespaces} |
| Sprint Complete | ≥5 in one sprint | ✅/⬜ | {count + sprint} |

**COLLABORATION ACHIEVEMENTS:**
| Achievement | Condition | Status | Evidence |
|-------------|-----------|--------|----------|
| Pair Signal | ≥2 contributors | ✅/⬜ | {names} |
| Cross-Fire | Conflicting signals | ✅/⬜ | {conflict description} |

**PHASE 2 EXIT GATE:**
"Every topic from the Phase 1 registry appears in section 2B.
Missing topics: GATE-B: [topic-name] missing from 2B → halt.
All three team milestones appear by exact name in 2A: [confirm].
Phase 2 exit gate passed — award section complete."

===========================
PHASE 3 — CONTRIBUTOR LEADERBOARD
Entry gate: Phase 2 exit gate must have passed
===========================

Rank contributors by: Total signals, then topics covered, then milestones triggered.

| Rank | Contributor | Signals | Topics | Milestones Triggered | Score |
|------|-------------|---------|--------|----------------------|-------|
| 1 | {name} | {n} | {n} | {list} | {n} |

Score = Signals × 1 + Topics × 3 + Milestones × 5.

**PHASE 3 EXIT GATE:** "Leaderboard contains ≥1 row. All contributors in Phase 1 registry are represented. Gate passed."

===========================
PHASE 4 — CLOSE-TO-UNLOCK CALLOUTS
Entry gate: Phase 3 exit gate must have passed
===========================

For achievements that are one action away from being earned, produce a dedicated section:

**1-AWAY ACHIEVEMENTS:**
| Topic | Achievement | What's Needed | Exact Skill to Run |
|-------|-------------|---------------|-------------------|
| {topic} | {achievement} | {exact gap} | /{namespace}:{skill} |

**PHASE 4 EXIT GATE:** "Section exists even if empty (write 'No 1-away achievements this sprint'). Gate passed."

===========================
PHASE 5 — STAGNATION AND SYNTHESIS
Entry gate: Phase 4 exit gate must have passed
===========================

#### 5A — Stagnation Scan

Reference only labels from this registry. Do not invent new pattern labels.

| Label | Description | Active? | Instance (name specific topic/contributor) |
|-------|-------------|---------|---------------------------------------------|
| SOLO_ISLAND | One contributor, no peer coverage | ✅/⬜ | {topic or contributor} |
| NAMESPACE_MOAT | Topic deep in one namespace only | ✅/⬜ | {topic} |
| SPRINT_FREEZE | No new signals ≥2 sprints | ✅/⬜ | {topic} |
| ORPHAN_TOPIC | Signals exist, no next-action | ✅/⬜ | {topic} |

#### 5B — Team Insight

State one observation visible only across topics — not a restatement of any stagnation row.

**TEAM INSIGHT — [Descriptive Title]:**
[2–3 sentences. Cross-topic or cross-contributor scope. Differs in substance from 5A.]

**PHASE 5 EXIT GATE:** "5A table complete with real instances named. 5B insight is titled and differs from 5A content. Gate passed."

===========================
PHASE 6 — NEXT ACTIONS
Entry gate: Phase 5 exit gate must have passed
===========================

**PRE-ROW GATE (run before each action row):**
"Does this row name: (a) the specific action, (b) the exact achievement it unlocks, (c) the exact pattern from the registry it breaks? If not — rewrite before continuing."

Format each action:

> [Specific Action] → Unlocks **[Achievement Name]** → Breaks **[PATTERN_LABEL from registry]**

Minimum 3 rows. Pattern labels must come from the Phase 5 registry.

**PHASE 6 EXIT GATE:** "≥3 actions present. Each action has all three components. All pattern labels exist in Phase 5 registry. Gate passed."

===========================
SPRINT SUMMARY
===========================

> Run date: {date} | Topics: {n} | Signals: {n} | Achievements awarded: {n} | Milestones: {earned} | Patterns active: {list}
```

---

## V-05 — Axis: Combined (Scorecard tables + anti-inertia framing + registry-backed patterns, compressed voice)

**Hypothesis:** Combining the table format from V-02 with the registry discipline from V-04 and the inertia framing from prior rounds in a compressed, dense output style produces the highest-signal-per-token ratio.

```markdown
You are running corps-achievements. Dense output. Tables where possible. No filler prose.

---

## GATE A — TOPIC DISCOVERY

Scan `simulations/` for `{topic}-{signal}-{date}.md`. Build topic registry table.

**Pre-list confirmation:** "All topics below are confirmed by real file paths. Unconfirmed topics: GATE-A: [topic-name] no file evidence → excluded."

| Topic | Signals | Namespaces | Contributors | Latest |
|-------|---------|------------|--------------|--------|
| {topic} | {n} | {list} | {list} | {date} |

---

## GATE B — ACHIEVEMENT SCORECARD

Two named categories per topic. Every topic from Gate A must appear.

**Pre-render check:** "All Gate A topics appear below. Missing: GATE-B: [topic-name] → halt."

### DEPTH ACHIEVEMENTS

| Topic | Signal Starter | Multi-Namespace (≥3) | Sprint Complete (≥5) |
|-------|---------------|---------------------|---------------------|
| {topic} | ✅/⬜ {file} | ✅/⬜ {namespaces} | ✅/⬜ {count} |

### COLLABORATION ACHIEVEMENTS

| Topic | Pair Signal (≥2 contrib) | Cross-Fire (conflicting) |
|-------|--------------------------|--------------------------|
| {topic} | ✅/⬜ {names} | ✅/⬜ {conflict} |

---

## TEAM MILESTONES

All three must appear by exact name:

| Milestone | Status | Evidence |
|-----------|--------|----------|
| First Team Signal | ✅/⬜ | {file or gap} |
| Shared Coverage | ✅/⬜ | {topic + names or gap} |
| Debate Starter | ✅/⬜ | {topic + namespaces or gap} |

---

## CONTRIBUTOR LEADERBOARD

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
| 1 | {name} | {n} | {n} | {list} | {n} |

Score = Signals + Topics×3 + Milestones×5.

---

## 1-AWAY ACHIEVEMENTS

| Topic | Achievement | Gap | Run |
|-------|-------------|-----|-----|
| {topic} | {achievement} | {exact} | /{ns}:{skill} |

(Write "none this sprint" if empty.)

---

## STAGNATION REGISTRY SCAN

Registry labels only — no invented labels:

| Label | Active? | Instance |
|-------|---------|---------|
| SOLO_ISLAND | ✅/⬜ | {topic/contributor} |
| NAMESPACE_MOAT | ✅/⬜ | {topic} |
| SPRINT_FREEZE | ✅/⬜ | {topic} |
| ORPHAN_TOPIC | ✅/⬜ | {topic} |

---

## TEAM INSIGHT

**TEAM INSIGHT — [Descriptive Title]:**
[2–3 sentences. Cross-topic or cross-contributor. Not a restatement of stagnation rows.]

---

## NEXT ACTIONS

**Pre-row gate:** "Row has: action + achievement + registry pattern. If not — rewrite."

| # | Action | Unlocks | Breaks |
|---|--------|---------|--------|
| 1 | {action} | **{Achievement}** | **[PATTERN_LABEL from registry]** |
| 2 | ... | ... | ... |
| 3 | ... | ... | ... |

---

## SPRINT SUMMARY

> {date} | Topics: {n} | Signals: {n} | Awarded: {n} | Milestones: {list} | Active patterns: {list}
```

---

### Variation Axes Summary

| Variation | Primary Axis | Secondary Axis | Hypothesis |
|-----------|-------------|----------------|-----------|
| V-01 | Role sequence (scan → award → synthesize) | Named phases | Grounding-first reduces hallucination |
| V-02 | Output format (scorecard tables + scoring) | Numerical scoring | Dense tables accelerate gap-spotting |
| V-03 | Phrasing register (team-facing, "your team") | Conversational gates | Warmer voice increases action uptake |
| V-04 | Lifecycle emphasis (verbose gates, auditable) | Explicit phase enter/exit | Verbose gates reduce phase-skipping |
| V-05 | Combined (tables + registry + compressed) | Multi-axis combination | Max signal-per-token in dense format |
