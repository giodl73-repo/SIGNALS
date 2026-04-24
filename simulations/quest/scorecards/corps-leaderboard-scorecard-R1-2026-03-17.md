## Scorecard — corps-leaderboard Variate R1

---

### V-01 — Output Format: Achievement Grid Table

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Coverage — complete topic scan | PASS | Step 1 SCAN RECORD requires every subdirectory; grid enforces one-row-per-topic; missing row is visually obvious |
| C-02 Achievement completeness per topic | PASS | Grid columns are exactly the 5 defined achievement names; every cell must be filled (earned/locked/—); column names are verbatim |
| C-03 All 3 team milestones, exact names | PASS | Step 3 uses verbatim table with exact names "first team signal", "shared coverage", "debate starter" as row labels |
| C-04 Contributor leaderboard present + ranked | PASS | Step 4 produces ranked table; explicit "no contributor metadata found" fallback row specified |
| C-05 3+ next actions with namespace+achievement | PASS | Step 6 format requires `namespace/topic` → exact achievement name; "Add more signals" without target explicitly called out as failure |
| C-06 Earned vs locked separated | PASS | Grid uses checkmark vs circle cell markers; structural separation by construction |
| C-07 1-away gap detection | PASS | Step 5 "Almost There" section with explicit format; "No single-step unlocks" fallback required |
| C-08 Empty workspace graceful handling | PASS | Step 1 handles empty explicitly; "all output sections will still be produced"; table header shown with note |
| C-09 Cross-topic synthesizing insight | PASS | Step 7 "Team Insight" required with specific number + name + implication |
| C-10 Stagnation pattern named + anti-inertia action | FAIL | No stagnation pattern role or named inertia diagnosis; closing team insight is positive/structural finding, not pattern-breaking |

**Score**: Essential 5/5 = 60 · Recommended 3/3 = 30 · Aspirational 1/2 = 5 → **95**

---

### V-02 — Phrasing Register: Conversational Sprint-Board

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Coverage — complete topic scan | PASS | "Every topic from the scan must appear in one group" explicit instruction; empty workspace handled up front |
| C-02 Achievement completeness per topic | PASS | Badge definitions listed with exact names; earned/locked groups required for every topic; "do not omit any discovered topic" |
| C-03 All 3 team milestones, exact names | PASS | All three listed with exact names as bold inline labels; renaming/paraphrasing not mentioned as forbidden but names are shown verbatim |
| C-04 Contributor leaderboard present + ranked | PASS | "Who's Leading" table first; explicit fallback row if no attribution; "Never omit this table" |
| C-05 3+ next actions with namespace+achievement | PASS | "Unlock These Next" format requires namespace+topic (`scout/competitors`, `flow/trigger`) and exact badge/milestone name; "No vague advice" stated |
| C-06 Earned vs locked separated | PASS | Two explicit groups: "Earned Badges ✓" and "Locked Badges ○" with visual markers |
| C-07 1-away gap detection | PASS | "Almost There" section with exact gap format; "Nothing on the 1-away list right now" fallback |
| C-08 Empty workspace graceful handling | PASS | Empty workspace addressed up front with "all sections — just with empty or NOT YET values" |
| C-09 Cross-topic synthesizing insight | PASS | "One thing the numbers tell us" closing section; example uses cross-topic comparison; specific numbers required |
| C-10 Stagnation pattern named + anti-inertia action | FAIL | No stagnation/inertia diagnosis; conversational register doesn't prompt pattern naming; insight section is forward-looking, not pattern identification |

**Score**: Essential 5/5 = 60 · Recommended 3/3 = 30 · Aspirational 1/2 = 5 → **95**

---

### V-03 — Lifecycle Emphasis: Explicit Phase Gates

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Coverage — complete topic scan | PASS | Phase 1 SCAN GATE output confirms n topics; Phase 2 explicitly states "omitting a topic is a PHASE 2 gate failure" |
| C-02 Achievement completeness per topic | PASS | Phase 2 table lists all 5 achievement names as conditions; earned/locked sections required per topic |
| C-03 All 3 team milestones, exact names | PASS | Phase 3 uses verbatim block for all three; "Milestone name renaming, abbreviation, or paraphrase fails C-03" stated explicitly |
| C-04 Contributor leaderboard present + ranked | PASS | Phase 4 with ranked table; explicit fallback row; "Do not omit this section" |
| C-05 3+ next actions with namespace+achievement | PASS | Phase 5 "pass this test" checklist requires namespace+topic AND exact achievement/milestone name |
| C-06 Earned vs locked separated | PASS | Phase 2 has explicit "### Earned" and "### Locked" structural sections |
| C-07 1-away gap detection | PASS | Phase 5 "Almost There (1-Away)" section; fallback requires stating closest gap even when nothing is 1-away |
| C-08 Empty workspace graceful handling | PASS | SCAN GATE explicitly handles empty case; continues with empty data; all phases still run |
| C-09 Cross-topic synthesizing insight | PASS | Phase 5 "Team Insight" with cross-topic/contributor constraint; specific number and name required |
| C-10 Stagnation pattern named + anti-inertia action | FAIL | No stagnation pattern phase or named inertia analysis; no requirement for actions to reference a pattern |

**Score**: Essential 5/5 = 60 · Recommended 3/3 = 30 · Aspirational 1/2 = 5 → **95**

---

### V-04 — Role Sequence + Inertia Framing (Combination)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Coverage — complete topic scan | PASS | Role 1 (Archaeologist) produces full inventory; Role 3 states "Every topic from Role 1 must appear. No topic may be omitted." |
| C-02 Achievement completeness per topic | PASS | Role 3 lists exact 5 achievement names; earned ✓ / locked ○ sections per topic; verbatim names stated |
| C-03 All 3 team milestones, exact names | PASS | Role 3 milestones table uses verbatim names; "exact milestone names — no renaming or paraphrasing" stated |
| C-04 Contributor leaderboard present + ranked | PASS | Role 3 leaderboard table; explicit no-metadata fallback row; "Do not omit the section" |
| C-05 3+ next actions with namespace+achievement | PASS | "Anti-Inertia Next Actions" format requires namespace+topic AND exact achievement/milestone name; 3+ required |
| C-06 Earned vs locked separated | PASS | Role 3 has "### Earned ✓" and "### Locked ○" structural sections |
| C-07 1-away gap detection | PASS | Role 3 "Almost There" section with exact gap format; fallback if none |
| C-08 Empty workspace graceful handling | PASS | Role 1 handles empty: "Proceed to Role 2 with empty data"; Role 2 and 3 proceed with empty inventory |
| C-09 Cross-topic synthesizing insight | PASS | Role 3 "Team Insight" requires cross-topic/contributor conclusion distinct from stagnation pattern; specific numbers required |
| C-10 Stagnation pattern named + anti-inertia action | PASS | Role 2 (Inertia Diagnostician) names pattern with evidence before compilation; Role 3 each action must "tie back to breaking this named pattern"; stagnation patterns enumerated (Empty Start, Lone Wolf, Namespace Tunnel, Stale Coverage, Shallow Spread) |

**Score**: Essential 5/5 = 60 · Recommended 3/3 = 30 · Aspirational 2/2 = 10 → **100**

---

### V-05 — Output Format + Lifecycle Emphasis (Combination)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Coverage — complete topic scan | PASS | Section 1 lists all topics; "Every topic listed here must appear in Section 2" stated explicitly |
| C-02 Achievement completeness per topic | PASS | Section 2 requires all 5 achievement names checked per topic; internal checklist confirmation before proceeding; explicit "paraphrasing fails" warning |
| C-03 All 3 team milestones, exact names | PASS | Section 3 uses all three verbatim names as bold inline labels; "Do not rename or abbreviate" stated |
| C-04 Contributor leaderboard present + ranked | PASS | Section 4 ranked table; no-attribution fallback row; empty workspace handled |
| C-05 3+ next actions with namespace+achievement | PASS | Section 6 format requires namespace+topic and exact achievement/milestone name; "An action without a specific target fails" |
| C-06 Earned vs locked separated | PASS | Section 2 has labeled "Earned:" and "Locked:" paragraphs per topic subsection |
| C-07 1-away gap detection | PASS | Section 5 "Almost There" with quantified gaps; fallback requires stating closest gap |
| C-08 Empty workspace graceful handling | PASS | Section 1 handles empty with explicit "NOT YET" state instruction; all 8 sections still produced |
| C-09 Cross-topic synthesizing insight | PASS | Section 7 "Team Insight" required; "synthesizing statement — not visible from any single-topic subsection"; 2-4 sentences with named insight + evidence + implication |
| C-10 Stagnation pattern named + anti-inertia action | PARTIAL | No dedicated stagnation pattern role or named diagnosis; Section 7 team insight might surface a pattern but is not required to name one; no requirement for actions to break a named pattern by name |

**Score**: Essential 5/5 = 60 · Recommended 3/3 = 30 · Aspirational 1/2 (C-09 PASS, C-10 PARTIAL=0) = 5 → **95**

---

## Summary Table

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | Score |
|-----------|------|------|------|------|------|------|------|------|------|------|-------|
| V-01 Grid Table | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | 95 |
| V-02 Sprint-Board | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | 95 |
| V-03 Phase Gates | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | 95 |
| V-04 Role+Inertia | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **100** |
| V-05 Format+Gates | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PARTIAL | 95 |

**Rank**: V-04 > V-01 = V-02 = V-03 = V-05

---

## Excellence Signals from V-04

**What made V-04 the top scorer:**

1. **Dedicated diagnostic role before compilation.** The Inertia Diagnostician runs *after* archaeology but *before* achievements — this sequencing means C-10 is a structural output of the middle role, not an optional afterthought. The stagnation pattern is produced before the leaderboard, so it's impossible to skip.

2. **Named pattern vocabulary with enumerated options.** Providing a concrete menu (Empty Start, Lone Wolf, Namespace Tunnel, Stale Coverage, Shallow Spread) plus the "or define your own" escape hatch forces the model to commit to a specific label with evidence, not a vague observation.

3. **Anti-inertia constraint on every action.** Requiring each next action to include "→ Breaks: [Pattern] because [sentence]" structurally links C-05 (specific actions) to C-10 (inertia pattern). The rubric gets two criteria satisfied by one mechanical constraint.

4. **Team Insight differentiated from stagnation pattern.** Explicitly requiring the insight to be a "structural or positive finding, not a problem statement" and to "differ from the stagnation pattern statement" prevents the two aspirational criteria from collapsing into one observation — both must be independently earned.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["dedicated inertia diagnostician role runs between archaeology and compilation — forces stagnation pattern before leaderboard, making C-10 structural not optional", "named pattern vocabulary with enumerated options prevents vague stagnation observation", "anti-inertia constraint on every action links C-05 specificity to C-10 pattern-breaking in one mechanical requirement", "team insight differentiated from stagnation pattern by requiring positive/structural finding — prevents two aspirational criteria collapsing into one observation"]}
```
