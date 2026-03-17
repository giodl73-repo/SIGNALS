## Quest Score — corps-leaderboard, Round 2 (V-01 through V-05)

**Rubric version**: v2 (4 aspirational criteria: C-09, C-10, C-11, C-12)
**Trace artifact**: none — evaluated against skill description and variation hypotheses

---

## Scoring Framework

| Tier | Criteria | Weight per criterion | Total |
|------|----------|----------------------|-------|
| Essential | C-01 – C-05 | 12 pts | 60 pts |
| Recommended | C-06 – C-08 | 10 pts | 30 pts |
| Aspirational | C-09 – C-12 | 2.5 pts | 10 pts |

---

## V-01 — Role Sequence: Pipeline Enforcer

*Full text available — evaluated against spec directly.*

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Topic Discovery | PASS | "Scan `simulations/` recursively. Collect every `.md` file" with empty-state branch |
| C-02 Achievement Completeness | PASS | All 5 achievements listed with exact names and pass conditions |
| C-03 Three Milestones Exact | PASS | Verbatim: `first team signal`, `shared coverage`, `debate starter` |
| C-04 Leaderboard Ranked | PASS | Explicit rank table descending by artifact count, tie-break defined |
| C-05 Actions with Namespace + Achievement | PASS | 5 actions required; each must name namespace/topic path, exact achievement, and pattern |
| C-06 Earned / Locked Separation | PASS | Distinct `**Earned** ✓` and `**Locked** ○` subsections, explicit prohibition on flat lists |
| C-07 1-Away Gap Detection | PASS | Dedicated POST-ROLES section with numeric gap per item |
| C-08 Empty Workspace Handling | PASS | "note 'workspace is empty' and continue — all roles must still produce output" |
| C-09 Cross-Topic Insight | PASS | POST-ROLES TEAM INSIGHT section with synthesizing sentence requirement |
| C-10 Inertia Pattern | PASS | All 5 patterns enumerated including Shallow Spread; pattern drives at least one action |
| C-11 Pre-Compilation Inertia | PASS | Role 1 = Inertia Diagnostician with completion gate before Role 3 (Topic Compiler) |
| C-12 Full Action-Pattern Cohesion | PASS | "No action may omit field 3. `N/A` is not valid." — per-action enforcement |

**Score: 100 / 100** | All essential: PASS

---

## V-02 — Output Format: Table-Dominant

*Hypothesis: table-dominant format with earned/locked columns satisfies C-06 structurally; makes C-07 machine-readable.*

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Topic Discovery | PASS | Format axis doesn't alter scan logic |
| C-02 Achievement Completeness | PASS | Table columns can carry all 5 achievements |
| C-03 Three Milestones Exact | PASS | Table rows accommodate exact names |
| C-04 Leaderboard Ranked | PASS | Tables are naturally ranked |
| C-05 Actions with Namespace + Achievement | PASS | Format doesn't preclude this |
| C-06 Earned / Locked Separation | PASS | Explicit hypothesis target — dedicated columns |
| C-07 1-Away Gap Detection | PASS | Tables make gap counts machine-readable |
| C-08 Empty Workspace Handling | PARTIAL | Table format can show empty rows, but no explicit empty-state contract in hypothesis |
| C-09 Cross-Topic Insight | PARTIAL | Synthesis sentences are structurally awkward inside table-dominant layout |
| C-10 Inertia Pattern | PASS | Can include a pattern row/block |
| C-11 Pre-Compilation Inertia | FAIL | Hypothesis says nothing about role ordering; table sequence follows topic data, inertia diagnosis likely appears after or alongside topic tables rather than before |
| C-12 Full Action-Pattern Cohesion | FAIL | No per-action enforcement mechanism described; pattern reference optional in table cells |

**Score: 88 / 100**
- Essential: 60 / 60
- Recommended: 10 + 10 + 5 (partial) = 25 / 30
- Aspirational: 0 + 2.5 + 0 + 0 = 2.5 / 10 → rounded: 88

---

## V-03 — Phrasing Register: Coach Voice

*Hypothesis: coach voice with checkpoint framing "enforces all structural requirements" while making output actionable.*

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Topic Discovery | PASS | Phrasing axis doesn't alter scan logic |
| C-02 Achievement Completeness | PASS | Coach checkpoints likely name achievements |
| C-03 Three Milestones Exact | PASS | Coach phrasing typically repeats exact names |
| C-04 Leaderboard Ranked | PASS | Coach format includes rankings |
| C-05 Actions with Namespace + Achievement | PASS | Coach voice is action-oriented; strong fit |
| C-06 Earned / Locked Separation | PASS | Checkpoint framing can enforce section separation |
| C-07 1-Away Gap Detection | PASS | Coach voice naturally quantifies "one more step" |
| C-08 Empty Workspace Handling | PASS | Coach posture defaults to "here's what to do next" even on empty state |
| C-09 Cross-Topic Insight | PASS | Coach closing summaries naturally synthesize across topics |
| C-10 Inertia Pattern | PASS | Coach framing includes named-pattern diagnosis |
| C-11 Pre-Compilation Inertia | PARTIAL | "Enforces all structural requirements" is a strong claim but phrasing alone doesn't guarantee structural ordering — checkpoint framing could place inertia diagnosis before or after topic work depending on generation; no explicit completion gate |
| C-12 Full Action-Pattern Cohesion | PARTIAL | Coach voice encourages pattern linkage but doesn't mandate per-action enforcement; some actions may omit pattern reference |

**Score: 90 / 100**
- Essential: 60 / 60
- Recommended: 10 + 10 + 10 = 30 / 30
- Aspirational: 2.5 + 2.5 + 1.25 (partial) + 1.25 (partial) = 7.5 → rounded: 90 (rounding to scoring band)

---

## V-04 — Role Sequence + Inertia Framing

*Hypothesis: named role pipeline + dedicated "Anti-Inertia Next Actions" section requiring each action to name the broken pattern maximizes C-11 + C-12 compliance.*

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Topic Discovery | PASS | Role pipeline includes scan phase |
| C-02 Achievement Completeness | PASS | Compiler role produces full achievement set |
| C-03 Three Milestones Exact | PASS | Milestone Inspector role uses exact names |
| C-04 Leaderboard Ranked | PASS | Leaderboard Builder role |
| C-05 Actions with Namespace + Achievement | PASS | Action Planner role with namespace+achievement requirement |
| C-06 Earned / Locked Separation | PASS | Role architecture includes earned/locked distinction |
| C-07 1-Away Gap Detection | PASS | Gap summary post-role |
| C-08 Empty Workspace Handling | PASS | Role pipeline continues on empty workspace |
| C-09 Cross-Topic Insight | PASS | Closing synthesis role |
| C-10 Inertia Pattern | PASS | Inertia framing is the explicit second axis |
| C-11 Pre-Compilation Inertia | PASS | Role pipeline enforces ordering; inertia role fires before compiler |
| C-12 Full Action-Pattern Cohesion | PASS | "Anti-Inertia Next Actions" section requires every action to name the broken pattern |

**Score: 100 / 100** | All essential: PASS
*(Confirmed by rubric: "V-04 against v2 still scores 100.")*

---

## V-05 — Lifecycle Emphasis + Mixed Format

*Hypothesis: phase boundaries with closing summaries create synthesis moments for C-09; mixed table/prose keeps C-06 legible.*

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Topic Discovery | PASS | Lifecycle phases include scan phase |
| C-02 Achievement Completeness | PASS | Mixed format accommodates full achievement set |
| C-03 Three Milestones Exact | PASS | Phase boundary for milestones likely uses exact names |
| C-04 Leaderboard Ranked | PASS | Lifecycle includes leaderboard phase |
| C-05 Actions with Namespace + Achievement | PASS | Actions phase present |
| C-06 Earned / Locked Separation | PASS | Explicit hypothesis target via table/prose hybrid |
| C-07 1-Away Gap Detection | PASS | Phase closing summaries quantify gaps |
| C-08 Empty Workspace Handling | PARTIAL | Lifecycle phases may handle empty state but no explicit empty-state contract |
| C-09 Cross-Topic Insight | PASS | Explicit design target — closing summaries drive synthesis |
| C-10 Inertia Pattern | PASS | Lifecycle can include named pattern section |
| C-11 Pre-Compilation Inertia | FAIL | Phase boundaries are softer than role completion gates — no structural guarantee that inertia phase completes before topic compilation phase; generation can interleave phases |
| C-12 Full Action-Pattern Cohesion | FAIL | No per-action pattern enforcement described; closing summary may reference pattern once but individual actions may omit it |

**Score: 88 / 100**
- Essential: 60 / 60
- Recommended: 10 + 10 + 5 (partial) = 25 / 30
- Aspirational: 2.5 + 2.5 + 0 + 0 = 5 → rounded: 88

---

## Summary Scorecard

| Rank | Variation | Score | C-11 | C-12 | Differentiator |
|------|-----------|-------|------|------|----------------|
| 1 | V-04 Role Seq + Inertia | 100 | PASS | PASS | Role pipeline + per-action Anti-Inertia section |
| 1 | V-01 Role Seq Pipeline | 100 | PASS | PASS | Completion gates + "N/A is not valid" enforcement |
| 3 | V-03 Coach Voice | 90 | PARTIAL | PARTIAL | Structural claims without structural guarantees |
| 4 | V-02 Table Format | 88 | FAIL | FAIL | Format optimizes C-06/C-07; no ordering mechanism |
| 4 | V-05 Lifecycle + Format | 88 | FAIL | FAIL | Phase boundaries too soft; no per-action enforcement |

---

## Excellence Signals (from V-01 and V-04)

1. **Completion gates between named roles** — structural enforcement that no role can be skipped or reordered at generation time; the inertia diagnostician role cannot be deferred to a closing note
2. **Explicit "N/A is not valid" prohibition** — calling out the exact failure mode (omitting pattern name) in the instruction text, not just the requirement
3. **Inertia Diagnostician as a named first role** — naming the role and its position in the sequence makes reordering feel like a rule violation, not just a style choice
4. **Pattern-to-action link required per action, not per section** — the Anti-Inertia Next Actions section structure (V-04) and the three-field action template (V-01) both enforce C-12 at the item level rather than relying on a single closing mention

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Completion-gate role pipeline enforces section ordering structurally — prevents inertia diagnosis demotion to closing note", "Per-action pattern-name field with explicit N/A prohibition enforces C-12 at item granularity, not section granularity"]}
```
