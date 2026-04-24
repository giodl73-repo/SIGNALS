## Scoring: corps-achievements — Variate R1

---

### V-01 — Achievement Grid Table

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Scan grounded in workspace | **PASS** | Step 1 explicit glob with internal working list; empty case handled with halt-free continue |
| C-02 | All discovered topics represented | **PASS** | "Every topic found in the scan must appear as a row … not an omitted row" — structurally enforced by table construction |
| C-03 | Three named milestones | **PASS** | Step 3 quotes all three exact names in a template table; explicit "do not rename" instruction |
| C-04 | Contributor leaderboard | **PASS** | Step 4 includes the full table template; fallback row required if no metadata |
| C-05 | Next actions achievement-linked | **PASS** | Format forces `[Action] → unlocks [Achievement/Milestone name]`; "Generic advice does not count. Name the namespace and topic." |
| C-06 | Earned vs. available separated | **PASS** | Distinct columns: "Earned Achievements" / "Available (Locked) Achievements" |
| C-07 | Achievement taxonomy ≥2 categories | **PARTIAL** | 5 badge types defined but presented as flat column values, not grouped into named categories; the split is earned/locked, not a taxonomy of types |
| C-08 | Sprint/date framing | **PASS** | Leaderboard header uses `Week of {{date}}`; frontmatter includes `date:` |
| C-09 | 1-away callouts quantified | **PASS** | Step 6 "Almost There" section with explicit `needs [exact count] more [thing]` |
| C-10 | Cross-topic/cross-contributor insight | **FAIL** | No dedicated insight section; Step 6 close-gaps section is gap-focused, not pattern-concluding |

**Essential:** 5/5 PASS  
**Recommended:** C-06 PASS, C-07 PARTIAL (score as 0), C-08 PASS → 2/3  
**Aspirational:** C-09 PASS, C-10 FAIL → 1/2

**Score:** `(5/5 × 60) + (2/3 × 30) + (1/2 × 10)` = `60 + 20 + 5` = **85**

---

### V-02 — Conversational Game-Badge

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Scan grounded | **PASS** | Opens with glob instruction; empty workspace handled: "say so up front and still produce all sections" |
| C-02 | All discovered topics represented | **PASS** | "Every topic found in the scan must appear in one of the two groups. A topic not listed is an error." |
| C-03 | Three named milestones | **PASS** | All three exact names quoted: "first team signal", "shared coverage", "debate starter" |
| C-04 | Contributor leaderboard | **PASS** | "Top Contributors" section required; fallback row for no metadata |
| C-05 | Next actions achievement-linked | **PASS** | "Unlock these next" — `Do this / Unlocks / Gap` format; explicit "No generic advice" with `scout-competitors` example |
| C-06 | Earned vs. available separated | **PASS** | "Earned Badges ✓" / "Locked Badges ○" section structure |
| C-07 | Achievement taxonomy ≥2 categories | **PARTIAL** | Split is earned/locked, not a taxonomy of badge types; badge types (First Signal, Signal Depth, etc.) are listed but not grouped into named categories |
| C-08 | Sprint/date framing | **PASS** | "What the team has earned this sprint"; scan date in opening sentence |
| C-09 | 1-away callouts quantified | **PARTIAL** | Locked badge list includes "need [n] more signals" which quantifies gaps, but there is no dedicated "1-away" section — gaps appear inline in the Locked group; quantification is present but not isolated as callouts |
| C-10 | Cross-topic/cross-contributor insight | **PASS** | "One team-level insight" section explicitly required; examples show named cross-contributor conclusions; must be "a named sentence, not a bullet list of stats" |

**Essential:** 5/5 PASS  
**Recommended:** C-06 PASS, C-07 PARTIAL (0), C-08 PASS → 2/3  
**Aspirational:** C-09 PARTIAL (0), C-10 PASS → 1/2

**Score:** `(5/5 × 60) + (2/3 × 30) + (1/2 × 10)` = `60 + 20 + 5` = **85**

---

### V-03 — Explicit Phase Gates

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Scan grounded | **PASS** | Phase 1 SCAN GATE handles empty explicitly; confirmation statement required before proceeding |
| C-02 | All discovered topics represented | **PASS** | "Every topic from the registry must appear in Earned or Available. Omitting a topic is a PHASE 2 gate failure." — structural enforcement with named failure mode |
| C-03 | Three named milestones | **PASS** | Phase 3 has all three exact names; "do not rephrase" instruction explicit |
| C-04 | Contributor leaderboard | **PASS** | Phase 4 required; fallback row for no metadata; LEADERBOARD GATE must state contributor count |
| C-05 | Next actions achievement-linked | **PASS** | Phase 5 pre-write test: "Does it name the exact achievement or milestone it unlocks?" — acts as an inline quality gate |
| C-06 | Earned vs. available separated | **PASS** | Phase 2 has distinct `### Earned` / `### Available (not yet earned)` subsections |
| C-07 | Achievement taxonomy ≥2 categories | **PASS** | Phase 2 groups into Earned / Available (functional categories); Phase 5 adds "Almost There" as third category — at least 2 distinct groupings with structural separation |
| C-08 | Sprint/date framing | **PASS** | "Achievements by Topic — Sprint {{date}}" and leaderboard header both use date; gate messages reference date |
| C-09 | 1-away callouts quantified | **PASS** | "Almost There (1 away)" block with explicit `needs [1 more signal / 1 more contributor / 1 more namespace]` |
| C-10 | Cross-topic/cross-contributor insight | **PASS** | "Team Insight" section in Phase 5: "One sentence drawing a conclusion that spans topics or contributors — not a per-topic stat" with example |

**Essential:** 5/5 PASS  
**Recommended:** 3/3 PASS  
**Aspirational:** 2/2 PASS

**Score:** `(5/5 × 60) + (3/3 × 30) + (2/2 × 10)` = `60 + 30 + 10` = **100**

---

### V-04 — Role Sequence + Inertia Framing

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Scan grounded | **PASS** | Role 1 (Archaeologist) globs `simulations/**/*.md`; empty case stated explicitly |
| C-02 | All discovered topics represented | **PASS** | "Every topic must appear. No topic may be omitted." in Role 3 Achievements section |
| C-03 | Three named milestones | **PASS** | Role 3 milestone table uses all three exact names in quoted template |
| C-04 | Contributor leaderboard | **PASS** | Role 3 has leaderboard table; fallback for no metadata stated |
| C-05 | Next actions achievement-linked | **PASS** | Anti-inertia format: `[Action] → Unlocks [Achievement] → Breaks [Stagnation Pattern]` — strongest of all variations; action must name namespace and topic |
| C-06 | Earned vs. available separated | **PASS** | Role 3: `### Earned ✓` / `### Locked ○` sections |
| C-07 | Achievement taxonomy ≥2 categories | **PARTIAL** | Earned/Locked split present; Stagnation Pattern in Role 2 adds a meta-category, but badge types themselves are not grouped into named categories |
| C-08 | Sprint/date framing | **PASS** | "Signal Archaeology — {{date}}" and "Contributor Leaderboard — {{date}}" both present |
| C-09 | 1-away callouts quantified | **PASS** | "Almost There" block: `needs [1 more X] to unlock [Achievement]` with explicit "If none" fallback |
| C-10 | Cross-topic/cross-contributor insight | **PASS** | "Team insight" section: "One sentence, cross-topic or cross-contributor, stated as a named conclusion. Must differ from the stagnation pattern statement." |

**Essential:** 5/5 PASS  
**Recommended:** C-06 PASS, C-07 PARTIAL (0), C-08 PASS → 2/3  
**Aspirational:** C-09 PASS, C-10 PASS → 2/2

**Score:** `(5/5 × 60) + (2/3 × 30) + (2/2 × 10)` = `60 + 20 + 10` = **90**

---

### V-05 — Prose Dashboard + Lifecycle Headers

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Scan grounded | **PASS** | Section 1 requires scan bullet list; empty case handled |
| C-02 | All discovered topics represented | **PARTIAL** | "Every topic in this list must appear in Section 2. A topic present here that is absent in Section 2 is an error." — integrity check stated, but prose format reduces mechanical auditability; the guard is a rule, not a structural enforcement (no table row gap visibility) |
| C-03 | Three named milestones | **PASS** | Section 3 has all three exact names as bold inline labels; "do not rename or abbreviate" instruction explicit |
| C-04 | Contributor leaderboard | **PASS** | Section 4 has table; fallback and sentence required |
| C-05 | Next actions achievement-linked | **PASS** | Section 6 format: `[Verb phrase — specific namespace and topic] → unlocks [Achievement or Milestone name]`; "No generic actions" stated |
| C-06 | Earned vs. available separated | **PASS** | Section 2 has "Earned paragraph" / "Available paragraph" per topic subsection |
| C-07 | Achievement taxonomy ≥2 categories | **PARTIAL** | Earned/Available split is per-topic, not a cross-topic taxonomy; no grouping of badge types into named categories |
| C-08 | Sprint/date framing | **PASS** | Section 1 header uses `({{date}})`; Section 4 uses `week of {{date}}` |
| C-09 | 1-away callouts quantified | **PASS** | Section 5 dedicated "Almost There" paragraph; "1 more signal", "1 more contributor" examples; fallback "closest gap" required if nothing is 1-away |
| C-10 | Cross-topic/cross-contributor insight | **PASS** | Section 7 requires 3-5 sentences; "must not be derivable from any single-topic view"; "name the insight in the opening sentence" |

**Essential:** C-02 PARTIAL (score as FAIL) → 4/5  
**Recommended:** C-06 PASS, C-07 PARTIAL (0), C-08 PASS → 2/3  
**Aspirational:** C-09 PASS, C-10 PASS → 2/2

**Score:** `(4/5 × 60) + (2/3 × 30) + (2/2 × 10)` = `48 + 20 + 10` = **78**

---

## Rankings

| Rank | Variation | Score | All Essential | Notes |
|------|-----------|-------|---------------|-------|
| 1 | **V-03** — Phase Gates | **100** | Yes | Only variation to achieve 3/3 recommended; phase gates enforce C-07 as structured grouping |
| 2 | **V-04** — Role + Inertia | **90** | Yes | Perfect aspirational; C-07 taxonomy gap the only cost |
| 3 | **V-01** — Grid Table | **85** | Yes | C-10 missing (no insight section); otherwise solid |
| 3 | **V-02** — Game Badge | **85** | Yes | C-09 quantification inline but not isolated; C-10 present via insight section |
| 5 | **V-05** — Prose Dashboard | **78** | No | C-02 essential PARTIAL due to prose auditability gap; strongest C-10 but weakest coverage guarantee |

---

## Excellence Signals from V-03

**1. Gate confirmation as output, not just behavior.** Each phase ends with a gate statement (e.g., `COMPUTE GATE: [n] topics processed`) that makes completeness machine-readable and human-verifiable. The gate fires even when data is empty — it can't be silently skipped.

**2. Empty workspace handled at the exact decision point.** The SCAN GATE explicitly distinguishes "empty" from "error" and instructs the model to proceed with an empty registry rather than hallucinate. This is what makes C-01 structurally safe for sparse workspaces.

**3. C-07 taxonomy emerges from phase structure.** Phases 2 and 5 create at least two named categories (Earned/Available + Almost There) without requiring an explicit taxonomy table. The phase lifecycle generates the grouping naturally.

**4. Inline quality gate before writing actions.** Phase 5 has a two-item pre-write test (`Does it name a specific namespace? Does it name the achievement it unlocks?`) that forces the model to self-check each action before committing it to the output.

**5. Team Insight as a named dedicated section.** Phase 5 ends with a `## Team Insight` block that requires a cross-scope sentence distinct from per-topic stats. The explicit instruction ("not a per-topic stat") prevents the most common degradation.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["gate-confirmation-as-output", "empty-workspace-gate-at-decision-point", "inline-quality-gate-before-writing-actions"]}
```
