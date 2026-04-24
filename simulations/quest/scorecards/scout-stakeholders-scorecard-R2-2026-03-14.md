## Round 2 Scorecard — scout-stakeholders

### Rankings

| Rank | Variation | Score | Golden? |
|------|-----------|-------|---------|
| 1 | **V-04** Full combo: reversed sequence + all four new criteria | **120/120** | YES |
| 2 | V-01 Source column enforced | **115** | YES |
| 2 | V-03 Inertia framing + inline failure modes | **115** | YES |
| 2 | V-05 Conversational + all four new criteria | **115** | YES |
| 5 | V-02 Prose narrative repaired + Frame Type | **110** | YES |

All five pass all essential criteria. All five golden.

---

### Key scoring decisions

**V-04 = 120/120 (perfect)**: All four new aspirational criteria pass cleanly. The reversed sequence (Strategy → UX → PM) is structural: PM builds the grid last, so conflicts and segment splits are already identified when Source labels are assigned. Anti-pattern labels appear at all eight phase gates, not select steps.

**V-05 = 115 (not 120)**: Predicted 120 but misses C-07. The conversational format collapses PM/Strategy/UX into the "Map the stakeholders" section. Strategy gets its own "Name the conflicts" section; PM owns the grid; but UX is embedded in grid-building instructions without a structural section of its own — rubric calls this PARTIAL (5 pts). Adding two words (`**UX Analysis**` heading) would close it.

**V-01 vs V-03 tie (115)**: Different aspirational profiles. V-01 has C-11+C-12 but not C-14. V-03 has C-12+C-13+C-14 but not C-11. Each misses exactly one criterion.

**V-02 lowest (110)**: Grid template has no Source column — C-11 gap costs 5 pts vs. the V-01/V-03 tier.

---

### Excellence signals from V-04

1. **Reversed sequence as grid quality guarantee** — analysis-before-synthesis enforced structurally, not instructionally
2. **Anti-pattern at every phase gate** — per-step placement more directive than preamble warnings
3. **Source column making initial-inventory rows visibly suspicious** — artifact-level quality signal
4. **Amendment anti-pattern as before/after pair** — bad form + correct form more effective than positive rule alone

```json
{"top_score": 120, "all_essential_pass": true, "new_patterns": ["Reversed sequence (Strategy then UX then PM) as grid quality guarantee -- PM builds the grid last, after conflicts and segments are already identified, so Source column differentiation is native to first draft rather than retroactively audited. Enforces analysis-before-synthesis structurally rather than instructionally.", "Anti-pattern label at every phase gate (not select steps) -- per-step placement anchors correct behavior at the moment the model is about to execute that step; labels at step 3 prevent step 3 failures more reliably than a preamble warning covering all steps.", "Source column making initial-inventory rows visibly suspicious as an artifact property -- evaluators can audit grid completeness directly from the output without interpreting prose; the column converts a hidden quality signal into an inspectable structural property.", "Amendment anti-pattern shown as before/after pair -- bad form (observation as amendment) followed immediately by correct form (update the comms table entry, note what changed) is more directive than stating the positive rule; the bad form is recognizable as an actual common failure mode."]}
```
cking column in grid | **PASS** | 5 | "The Source column is required -- every row must have an origin label." Three labels defined with definitions. "Any row remaining as 'initial-inventory' after the amendment phase is a candidate for review." |
| C-12 | Amendment loop with update mandate | **PASS** | 5 | Step 7: "This is a revision loop. For each finding, update the grid, veto list, or comms table -- do not only observe." + "For each finding that changes the grid, re-rank list, or comms table: make the change and note it." |
| C-13 | Prefilled frame types in comms table | **PASS** | 5 | Step 6 Frame Type column prefilled with Risk-reduction / Value-demonstration / Activation / Awareness -- one distinct label per row. "Using the same frame on multiple rows = FAIL." |
| C-14 | Named failure modes inline | **FAIL** | 0 | No inline anti-pattern labels at the steps where failures occur. V-01's axis targeted C-11 and C-12 only; no named failure modes added. |

**Essential**: 60/60 | **Recommended**: 30/30 | **Aspirational**: 5+5+5+5+5+0 = 25/30
**Score: 115**

---

#### V-02: Prose Narrative Repaired + Frame Type Column -- 110

| ID | Criterion | Result | Pts | Evidence |
|----|-----------|--------|-----|----------|
| C-01 | CODEOWNERS fallback | **PASS** | 12 | "Check for a CODEOWNERS file...Never infer silently." Asks one question if neither source provides context. |
| C-02 | Power/Interest grid present | **PASS** | 12 | Grid in Stakeholder Landscape section with Power (1-5), Interest (1-5), Quadrant, Notes columns. |
| C-03 | Veto risks ranked by probability | **PASS** | 12 | "Provide the list in descending probability order." Each entry includes Probability + Impact + Mitigation. Explanation paragraph for top veto. |
| C-04 | Champion with concrete action | **PASS** | 12 | Champion Identification section: "state the concrete activation action: not a general intent to engage, but a specific action (e.g., 'give them the live demo slot at the sprint review')." |
| C-05 | Communication strategy per quadrant | **PASS** | 12 | Communication Strategy table has four quadrant rows, Frame Type column, Timing, Message. Sequencing dependency paragraph after the table. |
| C-06 | Conflict identification | **PASS** | 10 | Stakeholder Landscape paragraph: "Name at least two conflicts: pairs of stakeholder groups...Format each conflict: [Group A] vs. [Group B] -- nature of tension. A single stakeholder's risk is not a conflict." |
| C-07 | Role framing | **PASS** | 10 | "Stakeholder Landscape (Strategy + PM)" section handles PM + Strategy. Separate "UX Analysis" section with heading: "This section is analytically distinct from the stakeholder grid." Three roles represented in distinct structural sections. |
| C-08 | Critical-path gatekeepers flagged | **PASS** | 10 | Stakeholder Landscape: "any critical-path gatekeeper whose scheduling constrains the launch timeline. For each critical-path gatekeeper, state the lead time required." |
| C-09 | Amendment phase | **PASS** | 5 | Amendments section with four audit items, numbered amendments required, "If no amendments arise, write 'No amendments -- analysis is complete as stated.'" |
| C-10 | "What we are NOT doing" framing | **PASS** | 5 | Amendments section: "For any compliance or security gatekeeper: write one sentence -- 'What this product does NOT do: [data it does not collect, action it does not take].'" |
| C-11 | Source-tracking column in grid | **FAIL** | 0 | Grid template: `| Stakeholder | Power (1-5) | Interest (1-5) | Quadrant | Notes |` -- no Source column. V-02's axis did not address C-11. |
| C-12 | Amendment loop with update mandate | **PASS** | 5 | "For each finding: update the relevant section above -- do not only observe." + "Number each amendment. For each finding that changes a section: make the change and note it." |
| C-13 | Prefilled frame types in comms table | **PASS** | 5 | Frame Type column with prefilled labels: Risk-reduction / Value-demonstration / Activation / Awareness. "Each row must carry a distinct frame type label -- same frame across multiple rows = FAIL." |
| C-14 | Named failure modes inline | **FAIL** | 0 | No inline anti-pattern labels at the steps where failures occur. V-02's axis targeted C-07/C-12/C-13 only; no named failure modes added. |

**Essential**: 60/60 | **Recommended**: 30/30 | **Aspirational**: 5+5+0+5+5+0 = 20/30
**Score: 110**

---

#### V-03: Inertia Framing Repaired + Named Failure Modes Inline -- 115

| ID | Criterion | Result | Pts | Evidence |
|----|-----------|--------|-----|----------|
| C-01 | CODEOWNERS fallback | **PASS** | 12 | Step 0: "Check for CODEOWNERS...ask exactly one question...Do not infer silently." Anti-pattern named: defaulting to generic roles produces org-chart not stakeholder map. |
| C-02 | Power/Interest grid present | **PASS** | 12 | Step 2 grid includes Status Quo row, Power (1-5), Interest (1-5), Quadrant, Notes. Quadrant labels defined. Anti-pattern for Status Quo interest > 2. |
| C-03 | Veto risks ranked by probability | **PASS** | 12 | Step 4: "Rank strictly by probability." Adds Mechanism field (active-block or inertia). Probability + Impact + Mitigation per row. Anti-pattern at end. |
| C-04 | Champion with concrete action | **PASS** | 12 | Step 5: "Give one concrete activation action tied to displacing the status quo." Anti-pattern: "Have the dev lead champion the tool." Names the specific action. |
| C-05 | Communication strategy per quadrant | **PASS** | 12 | Step 6 table has four quadrant rows, Frame Type column, Timing, Message. "Each row must carry a distinct label -- same frame across rows = FAIL." |
| C-06 | Conflict identification | **PASS** | 10 | Step 1 Q1: "At least two competing definitions of success...Each entry names both parties." Format given. Anti-pattern for single-stakeholder observation. |
| C-07 | Role framing | **PASS** | 10 | Three structurally distinct steps: Step 1 (Strategy: Conflict Discovery), Step 2 (PM: Power/Interest Grid), Step 3 (UX: Experience Intersections). Each step has its own heading and clearly scoped analytical remit. |
| C-08 | Critical-path gatekeepers flagged | **PASS** | 10 | Step 1 Q3: "Which actor's scheduling or approval decision is on the critical path? State minimum lead time. Label [CRITICAL PATH]." |
| C-09 | Amendment phase | **PASS** | 5 | Step 7 with four numbered audit items including segment check, missing actors, gatekeeper reframe, Status Quo displacement check. |
| C-10 | "What we are NOT doing" framing | **PASS** | 5 | Step 7 item 3: "For any compliance or security gatekeeper, write one sentence -- 'What this product does NOT do: [data it does not collect, action it does not take].'" |
| C-11 | Source-tracking column in grid | **FAIL** | 0 | Grid template: `| Stakeholder | Power (1-5) | Interest (1-5) | Quadrant | Notes |` -- no Source column. V-03's axis did not address C-11. |
| C-12 | Amendment loop with update mandate | **PASS** | 5 | Step 7: "For each finding, make the update -- do not only observe." + "Number each amendment. Update the relevant section for each finding." Anti-pattern at end names the exact failure: "consider briefing earlier" is observation, not revision. |
| C-13 | Prefilled frame types in comms table | **PASS** | 5 | Step 6 Frame Type column with distinct prefilled labels per row: Risk-reduction / Value-demonstration / Activation / Awareness. Anti-pattern for same frame across rows. |
| C-14 | Named failure modes inline | **PASS** | 5 | Anti-pattern labels appear at every step: Step 0 (generic role names), Step 1 (single-stakeholder observation), Step 2 (Status Quo interest score), Step 3 (single bloc treatment), Step 4 (alphabetical ordering), Step 5 (generic engagement), Step 6 (uniform "highlight benefits" frame), Step 7 (observation vs. revision). Each names the specific failure at the point of risk, not a generic warning. |

**Essential**: 60/60 | **Recommended**: 30/30 | **Aspirational**: 5+5+0+5+5+5 = 25/30
**Score: 115**

---

#### V-04: Full Combo: Reversed Sequence + All Four New Aspirational Criteria -- 120

| ID | Criterion | Result | Pts | Evidence |
|----|-----------|--------|-----|----------|
| C-01 | CODEOWNERS fallback | **PASS** | 12 | Phase 0: "CODEOWNERS check...ask one question...Do not proceed without org context." Anti-pattern: proceeding with assumed org structure produces org-chart-shaped output. |
| C-02 | Power/Interest grid present | **PASS** | 12 | Phase 3 grid: Stakeholder, Power (1-5), Interest (1-5), Quadrant, Source, Notes. Grid built after conflicts (Phase 1) and segments (Phase 2) are loaded. |
| C-03 | Veto risks ranked by probability | **PASS** | 12 | Phase 4: "Rank veto risks by probability. Do not follow grid order." Probability + Impact + Mitigation per entry. Anti-pattern for alphabetical/hierarchical ordering. |
| C-04 | Champion with concrete action | **PASS** | 12 | Phase 5: "Give a concrete activation action -- specific enough to put on a calendar or assign to an owner." Anti-pattern with specific examples of what concrete looks like. |
| C-05 | Communication strategy per quadrant | **PASS** | 12 | Phase 6 table with four quadrant rows, Frame Type column, Timing (relative to named milestone), Message. "Timing must be relative to a named milestone, not an absolute date." |
| C-06 | Conflict identification | **PASS** | 10 | Phase 1 Q1: "At least two competing definitions of success...Each entry must name both parties." Anti-pattern for single-stakeholder observation. |
| C-07 | Role framing | **PASS** | 10 | Three distinct phases with own headings: Phase 1 (Strategy Role: Conflict Landscape), Phase 2 (UX Role: Experience Intersections), Phase 3 (PM Role: Power/Interest Grid). Reversed sequence but structurally separated. PM explicitly "runs last, incorporating conflicts from Phase 1 and segment data from Phase 2." |
| C-08 | Critical-path gatekeepers flagged | **PASS** | 10 | Phase 1 Q3: "Which stakeholder's approval or scheduling decision is on the critical path? What is the minimum lead time...Label these [CRITICAL PATH]." |
| C-09 | Amendment phase | **PASS** | 5 | Phase 7 Amendment Loop with five numbered audit items: landscape audit, gatekeeper audit, timeline audit, champion audit, source audit. |
| C-10 | "What we are NOT doing" framing | **PASS** | 5 | Phase 7 item 2: "For any compliance or security gatekeeper, write one sentence: 'What this product does NOT do: [data it does not collect, action it does not take].'" |
| C-11 | Source-tracking column in grid | **PASS** | 5 | Phase 3: "The Source column is required -- every row must have an origin label." Three labels with definitions. Anti-pattern: "Every row labeled 'initial-inventory'" names the gap the column is designed to surface. |
| C-12 | Amendment loop with update mandate | **PASS** | 5 | Phase 7: "This is a revision loop. For each finding, update the grid, veto list, or comms table. Do not only observe." Anti-pattern shows exact before/after: observation vs. revision with comms table update. |
| C-13 | Prefilled frame types in comms table | **PASS** | 5 | Phase 6 Frame Type column with distinct prefilled labels per row: Risk-reduction / Value-demonstration / Activation / Awareness. "Same frame across rows = FAIL." Anti-pattern: four rows all framing "highlight the value." |
| C-14 | Named failure modes inline | **PASS** | 5 | Anti-pattern labels at every phase gate: Phase 0 (assumed org structure), Phase 1 (single-stakeholder observation), Phase 2 (surface-level UX with no segment finding), Phase 3 (all initial-inventory), Phase 4 (alphabetical ordering), Phase 5 (generic engagement), Phase 6 (uniform value frame), Phase 7 (observation vs. revision). All name the specific failure at the exact point of risk. |

**Essential**: 60/60 | **Recommended**: 30/30 | **Aspirational**: 5+5+5+5+5+5 = 30/30
**Score: 120** -- all aspirational criteria pass

**Perfect aspirational score. First variation to hit 120/120.**

---

#### V-05: Conversational + Source Column + Amendment Mandate + Named Failure Modes -- 115

| ID | Criterion | Result | Pts | Evidence |
|----|-----------|--------|-----|----------|
| C-01 | CODEOWNERS fallback | **PASS** | 12 | "Does a CODEOWNERS file exist? If yes, read it...If that's also thin, ask one question...Don't guess. Don't infer silently." Anti-pattern: assuming generic roles. |
| C-02 | Power/Interest grid present | **PASS** | 12 | Grid with Source column in "Map the stakeholders" section. Power (1-5), Interest (1-5), Quadrant, Source, Flag columns. |
| C-03 | Veto risks ranked by probability | **PASS** | 12 | "Order strictly by probability -- most likely threat first." Each entry: Probability + consequence + concrete action + timing. Anti-pattern: listing in grid order. |
| C-04 | Champion with concrete action | **PASS** | 12 | "Activate the champion" section: "Give one specific action -- something you can put on a calendar or assign to an owner." Examples given. Anti-pattern: generic engagement. |
| C-05 | Communication strategy per quadrant | **PASS** | 12 | "Build the communication plan" table with five columns including Frame Type. Four quadrant rows with distinct Frame Types, Action column, Timing column, Message column. |
| C-06 | Conflict identification | **PASS** | 10 | Separate "Name the conflicts" section: "List at least two. Each entry must name both parties and the tension." Anti-pattern: single-group disposition. |
| C-07 | Role framing | **PARTIAL** | 5 | Three lenses named within "Map the stakeholders" section (PM lens / Strategy lens / UX lens) but UX is instructional context for grid-building, not a structurally distinct analytical section. Strategy gets its own "Name the conflicts" section; PM owns the grid. UX has no independent structural home -- named but not separated. |
| C-08 | Critical-path gatekeepers flagged | **PASS** | 10 | Flag column in grid: "mark CRITICAL PATH -- [lead time] for any stakeholder whose approval or scheduling blocks the launch timeline regardless of their support." |
| C-09 | Amendment phase | **PASS** | 5 | "Check your work -- amendment pass" section with five audit items and numbered amendment format. |
| C-10 | "What we are NOT doing" framing | **PASS** | 5 | Amendment pass item: "For any compliance or security gatekeeper: write one sentence -- 'What this product does NOT do: [data it doesn't collect, action it doesn't take].'" |
| C-11 | Source-tracking column in grid | **PASS** | 5 | "The Source column is required -- every row must have an origin label: (conflict-discovered / UX-segment / initial-inventory)." Anti-pattern: "a grid full of initial-inventory rows means conflict analysis and UX segment detection surfaced nothing." |
| C-12 | Amendment loop with update mandate | **PASS** | 5 | "For each finding: make the update, then note what changed. Don't only observe." Anti-pattern shows exact before/after: "Amendment 1: We should brief the security team earlier" vs. update the comms table timing entry. |
| C-13 | Prefilled frame types in comms table | **PASS** | 5 | Frame Type column with distinct prefilled labels per row: Risk-reduction / Value-demonstration / Activation / Awareness. "Anti-pattern: Every row labeled 'Value-demonstration'." |
| C-14 | Named failure modes inline | **PASS** | 5 | Anti-pattern labels at every step: org context (generic roles), grid building (all initial-inventory), conflict naming (single-group), veto ranking (grid order), champion (generic engagement), comms plan (uniform frame), amendment pass (observation vs. revision). Conversational format makes anti-patterns feel directive. All named at point of failure. |

**Essential**: 60/60 | **Recommended**: 10+5+10 = 25/30 | **Aspirational**: 5+5+5+5+5+5 = 30/30
**Score: 115**

**C-07 miss note**: V-05's conversational format collapses UX into the grid-building section rather than giving it a distinct analytical heading. The three lenses are named but only Strategy and PM have structural homes with their own sections. Adding a two-line "UX Analysis" heading before the segment detection instruction would repair this at zero cost.

---

### Key Observations

**V-04 breakthrough**: First variation to achieve all four aspirational criteria simultaneously. The reversed sequence (Strategy → UX → PM) is the structural explanation: PM builds the grid last, after conflicts and segment splits are already identified, so the Source column has meaningful differentiation from the start. Pairing this with anti-pattern labels at every phase gate produces the clean 120/120.

**V-01 vs V-03 tie (both 115)**: Different aspirational profiles. V-01 adds C-11+C-12 (source tracking + amendment mandate) but not C-14. V-03 adds C-12+C-13+C-14 (amendment mandate + frame types + failure modes) but not C-11. Both miss one aspirational criterion. V-03's inertia framing (Status Quo as explicit grid row) is a strong design signal not yet reflected in the rubric.

**V-02 lowest (110)**: C-11 gap (no Source column) costs 5 pts vs V-01/V-03. The prose narrative structure that differentiates V-02 is strong for readability but does not compensate for the missing source tracking mechanism.

**V-05 C-07 PARTIAL**: The conversational format that makes V-05 distinctive is also what prevents C-07 from passing -- UX work is embedded in grid-building instructions rather than given a structural section. Easiest fix in R3: add a two-line `**UX Analysis**` heading before the segment detection instruction in "Map the stakeholders."

---

### Prediction Delta

Predictions in the variations file had V-04/V-05 at 120/120 and V-01/V-02/V-03 at lower scores. Actuals:
- V-04: 120 -- matches prediction
- V-05: 115 vs. predicted 120 -- delta -5 from C-07 PARTIAL (conversational format collapses UX into grid section)
- V-01: 115 vs. predicted ~115 -- matches
- V-02: 110 vs. predicted ~110 -- matches
- V-03: 115 vs. predicted ~115 -- matches

The one surprise is V-05: the conversational format trades structural clarity for directness, and C-07 is the specific rubric criterion where that trade costs points.

---

### Excellence Signals

**1. Reversed sequence (Strategy → UX → PM) as grid quality guarantee (V-04)**
When PM builds the grid last, conflicts are already named and segments are already detected. The Source column has real differentiation (conflict-discovered / UX-segment) from first draft rather than retroactively audited in the amendment phase. The sequence enforces analysis-before-synthesis structurally rather than instructionally.

**2. Anti-pattern label at every phase gate -- not select steps (V-03, V-04, V-05)**
V-03 named failure modes inline at all eight steps. V-04 named them at all eight phases. The effect: each step's anti-pattern anchors the correct behavior at the moment the model is about to execute that step. Generic warnings at the top or bottom have less force. Per-step placement is the load-bearing design.

**3. Source column making gaps visible (V-01, V-04, V-05)**
"Any row remaining as 'initial-inventory' after the amendment phase is a candidate for review" converts a hidden quality signal into a visible artifact property. Evaluators and models can audit grid completeness without interpreting narrative -- initial-inventory rows are directly inspectable.

**4. Amendment anti-pattern as before/after pair (V-04, V-05)**
Both V-04 and V-05 show the exact bad form ("Amendment 1: We should consider briefing the security team earlier") followed by the correct form (update the comms table timing entry, write what changed). This before/after framing is more directive than stating the positive rule alone. The bad form is recognizable to anyone who has seen template outputs -- it names the actual failure mode, not a hypothetical one.

---

```json
{"top_score": 120, "all_essential_pass": true, "new_patterns": ["Reversed sequence (Strategy then UX then PM) as grid quality guarantee -- PM builds the grid last, after conflicts and segments are already identified, so Source column differentiation is native to first draft rather than retroactively audited. Enforces analysis-before-synthesis structurally rather than instructionally.", "Anti-pattern label at every phase gate (not select steps) -- per-step placement anchors correct behavior at the moment the model is about to execute that step; labels at step 3 prevent step 3 failures more reliably than a preamble warning covering all steps.", "Source column making initial-inventory rows visibly suspicious as an artifact property -- evaluators can audit grid completeness directly from the output without interpreting prose; the column converts a hidden quality signal into an inspectable structural property.", "Amendment anti-pattern shown as before/after pair -- bad form (observation as amendment) followed immediately by correct form (update the comms table entry, note what changed) is more directive than stating the positive rule; the bad form is recognizable as an actual common failure mode."]}
```
