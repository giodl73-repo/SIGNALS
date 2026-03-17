## Round 1 Scorecard — scout-stakeholders

### Summary

| Rank | Variation | Essential | Recommended | Aspirational | Score | Golden? |
|------|-----------|-----------|-------------|--------------|-------|---------|
| 1 | **V-04** Reversed + Heavy Amendment | 60/60 | 30/30 | 10/10 | **100** | YES |
| 1 | **V-01** Strategy First | 60/60 | 30/30 | 10/10 | **100** | YES |
| 1 | **V-05** Conversational + Action-Rows | 60/60 | 30/30 | 10/10 | **100** | YES |
| 4 | V-02 Prose Narrative | 60/60 | 25/30 | 10/10 | **95** | YES |
| 4 | V-03 Inertia Framing | 60/60 | 25/30 | 10/10 | **95** | YES |

All five are golden. All five clear the essential gate (C-01 through C-05).

---

### What drove the scores

**Three-way tie at 100 (V-01, V-04, V-05):** Every criterion passes. The difference is where each variation excels:

- **V-04** is the canonical recommendation — reversed role sequence (Strategy → UX → PM validates last) plus the "make the change and note it" amendment mandate. The Source column in the grid is a new structural pattern.
- **V-01** is the clean baseline — conflicts-before-grid enforced through step ordering, every criterion covered without novelty.
- **V-05** is the strongest for C-04/C-05 — action-row comms table with prefilled frame types makes it structurally impossible to repeat the same message frame.

**V-02 and V-03 both land at 95 for the same reason:** C-07 PARTIAL. Both name all three roles (PM, Strategy, UX) in prose, but neither creates a distinct UX analytical section. V-02 collapses UX into the Amendments section; V-03 collapses it into a one-liner note in Step 1. The rubric requires output structure to clearly separate these concerns.

---

### New patterns (from top-scoring variations)

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Source-tracking column in grid — tracks where each row originated (Phase 1 conflict / Phase 2 UX segment / initial inventory), making the amendment phase a traceable second-pass audit. Gap rows sourced from initial inventory that should have been conflict-discovered become visible.", "Amendment loop with update mandate — instead of prompting for observations, the instruction requires acting: if a finding changes the grid, make the change and note it. Converts amendments from an observation register into a revision loop.", "Action-row comms table with prefilled frame types per quadrant — pre-seeds each row with a distinct frame label (Risk frame, Value frame, motivating frame), making it structurally impossible to repeat the same message frame across quadrants.", "Named failure modes at each step — naming what FAIL looks like inline (Not engage the dev lead, Don't alphabetize, Don't guess) is more effective than positive instructions alone."]}
```
 gatekeepers | **PASS** | 10 | Step 1: identify critical-path gatekeepers with lead-time required. Step 2: flag as `[CRITICAL PATH]` in Notes column with the lead-time constraint. Two-step tracking. |
| C-09 | Amendment phase | **PASS** | 5 | Step 7: 4 named audit items — segment splits, missing actors, gatekeeper reframes, NOT doing language. Explicit list format. |
| C-10 | Negative-space framing | **PASS** | 5 | Step 7: "For any compliance or security gatekeeper: write one sentence describing what this product does NOT do (data it does not collect, actions it does not take) to pre-answer their likely objection." |

**Essential**: 60/60 | **Recommended**: 30/30 | **Aspirational**: 10/10
**Score: 100**

---

#### V-02 — Prose Narrative with Embedded Tables — 95

| ID | Criterion | Result | Pts | Evidence |
|----|-----------|--------|-----|----------|
| C-01 | CODEOWNERS fallback | **PASS** | 12 | "Org Context Check" is the first section. CODEOWNERS check then invocation string then "ask exactly one question." "Never infer silently" is explicit. |
| C-02 | Power/Interest grid | **PASS** | 12 | Grid embedded in Stakeholder Map section. 4-column format with quadrant column. |
| C-03 | Veto risks ranked by probability | **PASS** | 12 | "Order is strictly by probability, not grid order." Also requires a sentence explaining WHY the top-ranked veto is first — higher quality forcing function than other variations. |
| C-04 | Champion with concrete action | **PASS** | 12 | "give the concrete activation action: not a general instruction to engage, but a specific action (e.g., 'give them the live demo slot,' 'have them co-present the first case study')." |
| C-05 | Communication strategy per quadrant | **PASS** | 12 | Quadrant table present. Post-table paragraph on timing dependencies between quadrants — strongest C-05 design for sequencing awareness. |
| C-06 | Conflict identification | **PASS** | 10 | Post-grid paragraph "must name at least two conflicts: pairs of stakeholders optimizing for different outcomes, in tension with each other." |
| C-07 | Role framing | **PARTIAL** | 5 | All three roles named in Stakeholder Map intro. But UX has no dedicated section — UX journey concerns are folded into the Amendments section as a segment split check, not a distinct analytical step. Rubric requires output structure to clearly separate these concerns. PM (grid) and Strategy (post-grid paragraph) are separated; UX is not structurally traceable. |
| C-08 | Critical-path gatekeepers | **PASS** | 10 | "Critical-Path Analysis" is a dedicated section: "identify any stakeholder whose scheduling or approval decision can block the launch timeline... state the lead time required." |
| C-09 | Amendment phase | **PASS** | 5 | "Amendments" section with three prose prompts: segment splits, missing actors, "what we are NOT doing" framing. Prose format may surface richer reasoning than bullet checklist. |
| C-10 | Negative-space framing | **PASS** | 5 | Amendments section: "Does any gatekeeper require a 'what we are NOT doing' framing to reduce review friction? Write that framing here." |

**Essential**: 60/60 | **Recommended**: 25/30 | **Aspirational**: 10/10
**Score: 95**

**C-07 PARTIAL note**: V-02's prose design surfaces reasoning well (C-06 and C-09 benefit) but at the cost of structural role enforcement. UX perspective is present in intent, absent in structure.

---

#### V-03 — Inertia Framing: Status Quo as Named Stakeholder — 95

| ID | Criterion | Result | Pts | Evidence |
|----|-----------|--------|-----|----------|
| C-01 | CODEOWNERS fallback | **PASS** | 12 | "Step 0 — Org Context": CODEOWNERS check then invocation string then ask one question. "Do not infer silently." |
| C-02 | Power/Interest grid | **PASS** | 12 | Step 1: grid with Status Quo row added. Status Quo power = average of top two gatekeepers; interest = 1. Quadrant labels present. |
| C-03 | Veto risks ranked by probability | **PASS** | 12 | Step 3: "Rank by probability of the veto materializing." New "Mechanism" column (active block vs. inertia) adds precision to ranking rationale. Strongest C-03 design of all variations. |
| C-04 | Champion with concrete action | **PASS** | 12 | Step 4: "Give a concrete activation action tied to displacing the status quo." Example: "give them the demo slot so developers see the tool working before gatekeepers can reframe it as a risk." Champion role explicitly framed as inertia displacement. |
| C-05 | Communication strategy per quadrant | **PASS** | 12 | Step 5: quadrant table with Timing + Message Frame. Keep Satisfied message pre-seeded as "Risk profile: why this is safer than status quo" — inertia-breaking frame for highest-power quadrant. |
| C-06 | Conflict identification | **PASS** | 10 | Step 2: two conflicts required; Status Quo row may appear as a party (e.g., "Architects vs. Dev Lead — skeptics reinforce status quo by withholding endorsement"). |
| C-07 | Role framing | **PARTIAL** | 5 | Step 1 lists roles: "PM: places stakeholders, Strategy: identifies conflicts, UX: identifies journey friction." All three named. But all three are assigned to the same Step 1 without structural separation — no dedicated UX section exists. Roles are collapsed into a single annotation under the grid. |
| C-08 | Critical-path gatekeepers | **PASS** | 10 | Step 1: `[CRITICAL PATH — lead time: X]` in Notes column. Integrated into grid. Explicit and evaluable. |
| C-09 | Amendment phase | **PASS** | 5 | Step 6: 3 amendment prompts (bulk vs. early-adopter split, missing downstream actor, NOT doing framing). Present but leaner than V-01's 4-item list. |
| C-10 | Negative-space framing | **PASS** | 5 | Step 6: "For any compliance or security gatekeeper: one sentence on what this product does NOT do, to reduce their inertia and review friction." Explicitly ties negative-space framing to inertia reduction. |

**Essential**: 60/60 | **Recommended**: 25/30 | **Aspirational**: 10/10
**Score: 95**

**C-07 PARTIAL note**: V-03 pays a structural role enforcement cost to add the Status Quo row. The inertia framing sharpens C-03 and C-04 noticeably (predicted "++") but collapses UX into a footnote in Step 1.

---

#### V-04 — Reversed Sequence + Heavy Amendment — 100

| ID | Criterion | Result | Pts | Evidence |
|----|-----------|--------|-----|----------|
| C-01 | CODEOWNERS fallback | **PASS** | 12 | "Phase 0 — Context Gate": CODEOWNERS then invocation then ask one question. "Do not proceed without org context." Most forceful gate language of all variations. |
| C-02 | Power/Interest grid | **PASS** | 12 | Phase 3 (PM runs last): 5-column grid with Source column tracking row origin (Phase 1 conflict / Phase 2 segment / initial). Any segments identified by UX in Phase 2 are pre-populated before PM assigns quadrants. |
| C-03 | Veto risks ranked by probability | **PASS** | 12 | Phase 4: "Rank veto risks by probability. Do not follow grid order." |
| C-04 | Champion with concrete action | **PASS** | 12 | Phase 5: "Give a concrete activation action (not 'engage'). The action should be specific enough to put on a calendar." Calendar-readiness as explicit quality bar. |
| C-05 | Communication strategy per quadrant | **PASS** | 12 | Phase 6: standard quadrant table. Timing relative to named milestone. Message Frame distinct per quadrant. |
| C-06 | Conflict identification | **PASS** | 10 | Phase 1 (Strategy first): "Output: a conflict list (minimum two entries, each naming both parties in tension)." Probing questions on competing success definitions and structural incentives precede the output format. |
| C-07 | Role framing | **PASS** | 10 | Three distinct phases: Phase 1 = Strategy, Phase 2 = UX, Phase 3 = PM. Most explicit and structurally enforced role separation of all variations. Source column in grid tracks which phase each row originated from. |
| C-08 | Critical-path gatekeepers | **PASS** | 10 | Phase 1: "Which stakeholder's approval or scheduling decision is on the critical path? What is the minimum lead time they need before a launch milestone? Label these [CRITICAL PATH]." Critical-path finding flows from Strategy phase into PM grid via Source column. |
| C-09 | Amendment phase | **PASS** | 5 | Phase 7 "Amendment Loop (Full Second Pass)": 4 named audits (Landscape, Gatekeeper, Timeline, Champion). "If a finding changes the grid (adds a row, splits a row, re-ranks a veto), make the change and note it." Only variation that mandates grid updates rather than just observations. |
| C-10 | Negative-space framing | **PASS** | 5 | Phase 7 Gatekeeper Audit: "If a compliance or security gatekeeper is present, write the 'what we are NOT doing' framing — one sentence stating what data the tool does not collect or what action it does not take." |

**Essential**: 60/60 | **Recommended**: 30/30 | **Aspirational**: 10/10
**Score: 100**

**Tiebreaker note** (vs. V-01 and V-05): V-04's Source column and "make the change" mandate produce the richest amendment outputs. V-04 is the canonical recommended variation.

---

#### V-05 — Conversational Register + Action-Row Tables — 100

| ID | Criterion | Result | Pts | Evidence |
|----|-----------|--------|-----|----------|
| C-01 | CODEOWNERS fallback | **PASS** | 12 | "Check your org context first" section: CODEOWNERS then invocation then ask one question. "Don't guess. Don't infer silently." Imperative phrasing. |
| C-02 | Power/Interest grid | **PASS** | 12 | Grid with Power, Interest, Quadrant, Flag columns. CRITICAL PATH flag is in its own column (not Notes), making omission structurally visible. |
| C-03 | Veto risks ranked by probability | **PASS** | 12 | "Order strictly by probability... Don't alphabetize. Don't follow grid order. Lead with the most probable threat." Four negative instructions — strongest anti-failure-mode language for this criterion. |
| C-04 | Champion with concrete action | **PASS** | 12 | "give one specific action — something you can put on a calendar. Not 'engage the dev lead.'" Directly names the failure mode in-line. |
| C-05 | Communication strategy per quadrant | **PASS** | 12 | Action-row table with 5 columns: Quadrant, Who, Action, Timing, Message: lead with this. Template pre-seeds distinct frame types per quadrant (Risk frame, Value frame, motivating frame, tool+link+time-to-value). Structurally impossible to repeat the same frame. Strongest C-05 design. |
| C-06 | Conflict identification | **PASS** | 10 | "Name the conflicts" section: "Each entry must name both parties and the nature of the tension." "A single stakeholder's risk is not a conflict." Conflict section appears after grid — potential org-chart-default bias not mitigated (unlike V-01/V-04). PASS on criterion; note for R2. |
| C-07 | Role framing | **PASS** | 10 | "Map the stakeholders" uses three named lenses: PM lens (power/interest), Strategy lens (where interests collide), UX lens (workflow intersections and segment detection). All three perspectives defined as concurrent analytical frames. Distinct from V-01/V-04's sequential steps but satisfies "traceable in output structure." |
| C-08 | Critical-path gatekeepers | **PASS** | 10 | Flag column in grid: "mark `CRITICAL PATH — [lead time]` for any stakeholder whose approval or scheduling blocks the launch timeline regardless of their support." In-grid placement makes omission visible. |
| C-09 | Amendment phase | **PASS** | 5 | Amendment pass: 4 questions (segment splits, downstream actors, NOT doing sentence, timing sequencing check). Numbered amendment list required. |
| C-10 | Negative-space framing | **PASS** | 5 | Amendment pass: "For any compliance or security gatekeeper: write one sentence — 'What this product does NOT do: [data it doesn't collect, action it doesn't take].' This pre-answers their likely question before the review starts." Strongest framing rationale for this criterion. |

**Essential**: 60/60 | **Recommended**: 30/30 | **Aspirational**: 10/10
**Score: 100**

---

### Excellence Signals (Top-Scoring Variations: V-01, V-04, V-05)

**1. Conflicts-before-grid sequencing (V-01, V-04)**
Running Strategy role before PM assigns grid positions reduces org-chart-default bias. In the trace, the Architect skeptic cluster and Security Review timing issue were the hardest findings — both emerge from conflict discovery, not grid placement. V-01 (Strategy Step 1 then PM Step 2) and V-04 (Strategy Phase 1 then UX Phase 2 then PM Phase 3) enforce this. V-05 names conflicts after the grid — structurally correct but analytically downstream.

**2. Source-tracking column in grid (V-04)**
The Source column (Phase 1 conflict / Phase 2 segment / initial inventory) makes the analytical lineage of each grid row explicit. Any row sourced from "initial inventory" that should have been "Phase 1 conflict" is a gap the model can now see and correct in the amendment loop.

**3. "Make the change and note it" amendment mandate (V-04)**
V-01 and V-03 prompt for amendment findings. V-04 requires acting on them: "If a finding changes the grid (adds a row, splits a row, re-ranks a veto), make the change and note it." Converts the amendment section from an observation register into a revision loop — matching what the trace Phase 4 actually did (adding Agenda Coordinator to critical path, splitting developer audience, adding NOT doing summary).

**4. Action-row table with prefilled frame types (V-05)**
The comms strategy table pre-seeds each quadrant row with a distinct frame label (Risk frame, Value frame, motivating frame, one-tool-one-link). The model cannot produce the table without filling a substantively different frame per row. Eliminates the most common C-05 failure mode (same message re-phrased four times).

**5. Named failure modes at each step (V-05)**
V-05 names what FAIL looks like inline: "Not 'engage the dev lead'", "Don't alphabetize", "Don't guess. Don't infer silently." More effective than positive instructions alone because the model can pattern-match against the named bad output.

---

### Hypothesis Validation

| Variation | Hypothesis | Confirmed? |
|-----------|-----------|------------|
| V-01 | Strategy-first reduces org-chart bias; C-06/C-08 improve | **CONFIRMED** — C-06/C-08 pass with higher structural reliability than V-05 (conflicts named before grid) |
| V-02 | Prose forces reasoning gaps to surface; C-06/C-09 gain depth | **PARTIAL** — C-06/C-09 well-designed, but UX role collapse costs C-07 PARTIAL |
| V-03 | Status Quo row sharpens C-03/C-04 | **CONFIRMED** — Mechanism column and inertia-breaking champion framing are strongest of any variation; cost is C-07 PARTIAL |
| V-04 | PM validates last; amendment is full second loop | **CONFIRMED** — C-07 and C-09 are best of any variation; Source column is a new pattern |
| V-05 | Imperative register eliminates decorative language; C-04/C-05 sharpen | **CONFIRMED** — C-04 names the failure mode; C-05 template is strongest of any variation |

---

### Recommended Golden Candidate

**V-04** — reversed sequence + 4-audit amendment loop. Perfect 100/100. Source column and "make the change" mandate produce the most actionable amendment outputs. Canonical choice.

**V-05** as high-coverage alternative — action-row table with prefilled frames is the strongest comms strategy design. Preferred if model reliability on distinct message frames is the primary concern.

**V-01** as clean baseline — every criterion covered without structural novelty. Useful comparison baseline for R2.

**Not promoted**: V-02 (95, C-07 PARTIAL — UX not structurally separated), V-03 (95, C-07 PARTIAL — UX collapsed into grid step annotation).

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Source-tracking column in grid — adds a Source column to the Power/Interest grid tracking where each row originated (Phase 1 conflict discovery / Phase 2 UX segment split / initial inventory), making the amendment phase a traceable second-pass audit rather than a free-form check. Gap rows sourced from initial inventory that should have been conflict-discovered become visible.", "Amendment loop with update mandate — instead of prompting for observations, the amendment instruction requires acting: if a finding changes the grid (adds a row, splits a row, re-ranks a veto), make the change and note it. Converts amendments from an observation register into a revision loop matching what the trace Phase 4 actually executed.", "Action-row comms table with prefilled frame types per quadrant — the communication strategy table pre-seeds each quadrant row with a distinct frame label (Risk frame, Value frame, motivating frame, one-tool-one-link), making it structurally impossible to repeat the same message frame across rows. Eliminates the most common C-05 failure mode.", "Named failure modes at each step — naming what FAIL looks like inline (Not engage the dev lead, Don't alphabetize, Don't guess) is more effective than positive instructions alone. Model can pattern-match against the named bad output rather than inferring what to avoid."]}
```
