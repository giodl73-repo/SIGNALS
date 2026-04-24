## corps-leaderboard — Quest Scorecard R4

---

### Criterion Reference (v4)

| ID | Tier | Weight | Name |
|----|------|--------|------|
| C-01 | Essential | 12 | All topics listed with named gap term |
| C-02 | Essential | 12 | Per-topic achievements with exact names |
| C-03 | Essential | 12 | Three team milestones with exact names |
| C-04 | Essential | 12 | Contributor leaderboard ranked |
| C-05 | Essential | 12 | Next actions naming namespace + achievement |
| C-06 | Recommended | 10 | Earned / locked achievement separation |
| C-07 | Recommended | 10 | 1-Away Gaps section |
| C-08 | Recommended | 10 | Team Synthesis sentence |
| C-09 | Aspirational | 1.11 | Leaderboard cited in stagnation evidence |
| C-10 | Aspirational | 1.11 | Named stagnation pattern in diagnosis |
| C-11 | Aspirational | 1.11 | Health diagnosis precedes topic compilation |
| C-12 | Aspirational | 1.11 | Workspace-empty path handled |
| C-13 | Aspirational | 1.11 | Ordering constraint present |
| C-14 | Aspirational | 1.11 | Breaks field unpopulatable with N/A |
| C-15 | Aspirational | 1.11 | Section-boundary gate (NEW v4) |
| C-16 | Aspirational | 1.11 | Quantified inertia with urgency tiers (NEW v4) |
| C-17 | Aspirational | 1.11 | Evidence-first leaderboard before diagnosis (NEW v4) |

---

### V-01 — All-Tables Scorecard

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 | PASS | "a topic present in the artifact table but absent from the matrix is a **matrix gap**" |
| C-02 | PASS | Achievement Matrix table uses exact column names; * vs -N notation per cell |
| C-03 | PASS | TEAM MILESTONES table uses exact names verbatim |
| C-04 | PASS | CONTRIBUTOR LEADERBOARD ranked descending by signal count |
| C-05 | PASS | `{namespace}/{topic}` + `Unlocks: {exact achievement or milestone name}` template |
| C-06 | PASS | Matrix columns distinguish earned (*) from locked (-N sig / -N ns / -N contrib / ?); table-column separation |
| C-07 | PASS | "1-AWAY GAPS" section present |
| C-08 | PASS | "TEAM SYNTHESIS" section with cross-row constraint |
| C-09 | PASS | "Where the Contributor Leaderboard corroborates a fired condition, reference the leaderboard row explicitly in the Evidence column" |
| C-10 | PASS | Five named conditions (Empty Start, Lone Wolf, Namespace Tunnel, Stale Coverage, Shallow Spread) |
| C-11 | PASS | SIGNAL HEALTH SCORECARD precedes ACHIEVEMENT MATRIX structurally |
| C-12 | PASS | "If workspace was empty: output the column headers with note 'No topics found — all cells empty.'" |
| C-13 | PASS | Section gate sequence enforced |
| C-14 | PASS | "No action may omit the Breaks field. 'N/A' is not valid." |
| C-15 | PASS | "SIGNAL HEALTH SCORECARD must close before ACHIEVEMENT MATRIX opens. No exceptions." — named section labels on both sides of gate |
| C-16 | PASS | Score row `[n]/5` + Tiers table (Healthy / Monitor / Alert / Critical) + `Priority: [Tier] — score [n]/5` in actions |
| C-17 | PASS | CONTRIBUTOR LEADERBOARD is first named section; SIGNAL HEALTH SCORECARD follows |

**Score: 100.0 / 100**

---

### V-02 — Triple-Gate Pipeline

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 | PASS | "A topic in the scan result but absent from the compilation is a **compilation gap**" |
| C-02 | PASS | Achievement definitions with exact names; per-topic Earned/Locked subsections |
| C-03 | PASS | TEAM MILESTONES table uses exact names verbatim |
| C-04 | PASS | CONTRIBUTOR LEADERBOARD ranked descending |
| C-05 | PASS | `{namespace}/{topic}` + `Unlocks:` + `Breaks:` + `Priority:` template; all fields required |
| C-06 | PASS | `**Earned**` / `**Locked**` subsections per topic — structural subsection separation |
| C-07 | PASS | "1-AWAY GAPS" section present |
| C-08 | PASS | "TEAM INSIGHT" section with cross-output synthesizing sentence |
| C-09 | PASS | "reference Contributor Leaderboard row if applicable" for Lone Wolf evidence |
| C-10 | PASS | Five named conditions with exact labels |
| C-11 | PASS | SIGNAL HEALTH SCORE precedes ACHIEVEMENT COMPILATION |
| C-12 | PASS | "If workspace was empty: write all section headers with 'no topics found.'" |
| C-13 | PASS | Three sequential gates enforce pipeline |
| C-14 | PASS | "No action may omit the Breaks field. 'N/A' is not valid." |
| C-15 | PASS | `[GATE 2: SIGNAL HEALTH SCORE closed. ACHIEVEMENT COMPILATION opens now.]` appears as literal output line + declarative rule — the strongest possible enforcement; skipped gate leaves visible output gap |
| C-16 | PASS | Score field `**Score: [n]/5**` + Tiers block with named levels + `Priority: [Current Tier] — score [n]/5` in actions |
| C-17 | PASS | CONTRIBUTOR LEADERBOARD runs first; `[GATE 1: CONTRIBUTOR LEADERBOARD closed. SIGNAL HEALTH SCORE opens now.]` makes ordering machine-auditable |

**Score: 100.0 / 100**

---

### V-03 — Conversational Coach

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 | PASS | "A topic that appears in the workspace but is missing from this section is a **topic gap**" |
| C-02 | PASS | "use these exact names — any other phrasing fails" with full exact-name list; per-topic subsections |
| C-03 | PASS | TEAM MILESTONES table uses exact names "first team signal", "shared coverage", "debate starter" |
| C-04 | PASS | "WHO'S CONTRIBUTING" ranked by signal count descending |
| C-05 | PASS | `{namespace}/{topic}` + `Unlocks:` + `Breaks:` + `Health:` template; all fields required |
| C-06 | PASS | `**Earned**` / `**Locked**` subsections per topic; structural separation |
| C-07 | PASS | "ALMOST THERE" section (1-away gaps equivalent) |
| C-08 | PASS | "TEAM PICTURE" synthesizing sentence with >= 2 topics/contributors + specific number |
| C-09 | PASS | "reference Who's Contributing if applicable" in Lone Wolf evidence instruction |
| C-10 | PASS | Five named conditions with exact labels in TEAM HEALTH SCORE |
| C-11 | PASS | TEAM HEALTH SCORE precedes TOPIC ACHIEVEMENTS |
| C-12 | PASS | "If the workspace is empty, write the section header with 'no topics found.'" |
| C-13 | PASS | Section gate sequence in conversational form |
| C-14 | PASS | "Don't leave the Breaks field blank. 'N/A' is not valid." |
| C-15 | PASS | "TEAM HEALTH SCORE must be complete before TOPIC ACHIEVEMENTS begins. No exceptions." — both section labels named |
| C-16 | PASS | `**Score: [n] out of 5**` + Health levels block with Healthy / Monitor / Alert / Critical tiers + `-> Health: [level] — score [n]/5` in actions |
| C-17 | PASS | WHO'S CONTRIBUTING is first section; TEAM HEALTH SCORE explicitly references it ("look at the WHO'S CONTRIBUTING table above") |

**Score: 100.0 / 100**

---

### V-04 — SITREP + Health Score

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 | PASS | "A missing topic is a **findings gap**" in FINDINGS section |
| C-02 | PASS | "exact names required" with full exact-name list; **Earned** / **Locked** subsections |
| C-03 | PASS | FINDINGS — Team Milestones table uses exact names verbatim |
| C-04 | PASS | SITUATION — Contributor Leaderboard ranked descending |
| C-05 | PASS | ACTIONS template with `{namespace}/{topic}` + `Unlocks:` + `Breaks:` + `Priority:` |
| C-06 | PASS | `**Earned** (check)` / `**Locked** (circle)` labels per topic; check/circle notation adds visual layering |
| C-07 | PASS | FINDINGS — 1-Away Gaps section |
| C-08 | PASS | DEBRIEF synthesizing statement, visible only from full briefing |
| C-09 | PASS | "cite SITUATION Contributor Leaderboard row if applicable" for Lone Wolf |
| C-10 | PASS | Five named conditions in ASSESSMENT |
| C-11 | PASS | ASSESSMENT precedes FINDINGS |
| C-12 | PASS | "If workspace is empty or absent, record empty and produce all sections with empty state." |
| C-13 | PASS | Five named sections in explicit sequence |
| C-14 | PASS | "No action may omit the Breaks field. 'N/A' is not valid." |
| C-15 | PASS | "ASSESSMENT must close before FINDINGS opens. No exceptions." — inherited strongest R3 gate language; also "ASSESSMENT closes here. FINDINGS opens next." closing marker |
| C-16 | PASS | `**Signal Health Score: [n]/5**` + Tier block + `Priority: [ASSESSMENT Current Tier] — score [n]/5` in ACTIONS; unique "Decision risk" field converts tier into actionable business signal |
| C-17 | PASS | SITUATION (section 1) contains contributor leaderboard; ASSESSMENT (section 2) follows and cites it; "What to watch for in FINDINGS" bridges diagnosis back to evidence |

**Score: 100.0 / 100**

---

### V-05 — Cascading Contracts

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-01 | PASS | "A topic in the artifact table but absent from this section is a **log gap**" |
| C-02 | PASS | "exact names required — paraphrasing fails"; **Earned** / **Locked** subsections |
| C-03 | PASS | MILESTONE CHECK table uses exact names verbatim |
| C-04 | PASS | CONTRIBUTOR ROSTER ranked descending; ties broken by topics covered |
| C-05 | PASS | RECOMMENDED ACTIONS template with `{namespace}/{topic}` + all three fields required |
| C-06 | PASS | `**Earned**` / `**Locked**` subsections per topic in ACHIEVEMENT LOG |
| C-07 | PASS | "1-AWAY GAPS" section with entry contract |
| C-08 | PASS | TEAM SYNTHESIS with cross-output constraint |
| C-09 | PASS | "reference the roster row explicitly" for Lone Wolf in SIGNAL HEALTH |
| C-10 | PASS | Five named conditions in SIGNAL HEALTH |
| C-11 | PASS | SIGNAL HEALTH precedes ACHIEVEMENT LOG |
| C-12 | PASS | "If simulations/ is empty or absent, record workspace: empty and produce all sections with empty state." |
| C-13 | PASS | Entry + closing contracts enforce sequence |
| C-14 | PASS | "No action may omit the Breaks field. 'N/A' is not valid." |
| C-15 | PASS | "Closing contract: SIGNAL HEALTH must close before ACHIEVEMENT LOG opens. No exceptions." — bidirectional contracts make this the **only variation where a skip violates two contracts simultaneously** (preceding section's close AND skipped section's open) |
| C-16 | PASS | `**Health Score: [n]/5**` + Severity Tiers block + `Priority: [Signal Health Current Tier] — score [n]/5` in RECOMMENDED ACTIONS |
| C-17 | PASS | CONTRIBUTOR ROSTER is first section; "Closing contract: CONTRIBUTOR ROSTER must close before SIGNAL HEALTH opens." — both close contract and entry contract enforce this ordering |

**Score: 100.0 / 100**

---

## Summary Ranking

| Rank | Variation | Score | C-15 Strength | C-16 Strength | C-17 Strength |
|------|-----------|-------|--------------|--------------|--------------|
| 1 (tied) | V-02 Triple-Gate Pipeline | 100.0 | Strongest — gate lines as output artifacts; gap visible if skipped | Full | Full + GATE 1 auditable |
| 1 (tied) | V-05 Cascading Contracts | 100.0 | Strongest — bidirectional contracts; skip violates two rules | Full | Full + close contract enforces ordering twice |
| 3 | V-04 SITREP + Health Score | 100.0 | Strong — dual-statement close ("closes here / opens next") | Full + Decision Risk field | Full + FINDINGS preview bridges back |
| 4 (tied) | V-01 All-Tables Scorecard | 100.0 | Full | Full | Full |
| 4 (tied) | V-03 Conversational Coach | 100.0 | Full | Full | Full |

---

## Excellence Signals

Three patterns from the top-scoring variations that made them better:

**1. Gate-as-output-artifact (V-02)**
Writing `[GATE N: X closed. Y opens now.]` as a literal output line converts the gate from an instruction into an observable artifact. A skipped gate leaves a visible structural hole in the output — the gate line is simply absent. This makes compliance self-auditing without requiring a human to trace section order. No other variation achieves this.

**2. Bidirectional section contracts (V-05)**
Every section in V-05 names both its predecessor (entry contract) and its successor (closing contract). A single skipped section violates two rules instead of one: the preceding section's closing contract AND the skipped section's entry contract. Redundant enforcement at every boundary means the model must make two simultaneous errors to bypass the gate, not one.

**3. Decision-risk field in diagnosis (V-04)**
V-04's ASSESSMENT adds "Decision risk: which commitment or decision the team cannot safely make at current signal coverage." This converts the health score from a diagnostic label into an actionable business signal — the reader knows not just the score tier but what that tier blocks them from deciding. The companion "What to watch for in FINDINGS" field links the ASSESSMENT pattern to specific FINDINGS outcomes, creating cross-section coherence not present in other variations.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["gate-as-output-artifact: writing gate transitions as literal output lines makes skipped gates visibly absent rather than silently violated", "bidirectional-section-contracts: each section names both predecessor and successor so a single skip violates two constraints simultaneously", "decision-risk-field: extending health score diagnosis with a named commitment-or-decision the current tier blocks converts severity into actionable business signal"]}
```
