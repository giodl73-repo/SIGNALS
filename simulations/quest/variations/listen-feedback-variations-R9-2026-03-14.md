Looking at the rubric (v8) and the skill description, I'll design 5 complete variations targeting the key gaps surfaced in previous rounds — especially A-16 (Band as separate field) and A-17 (bilateral gains+losses). Let me pick the 3 single-axis variations and 2 combinations.

**Single-axis picks:** Role sequence, Inertia framing, Output format  
**Combinations:** Role sequence + Inertia framing (V-04), Output format + Lifecycle emphasis (V-05)

---

# listen-feedback Variations — Round 9

---

## V-01 — Role Sequence Axis

**Hypothesis:** Running PM and UX reads *before* customer personas anchors severity judgments in professional framing. PM names the inertia baseline once; UX identifies the friction surface once; personas then score against those shared anchors rather than each constructing their own context.

---

```
You are running the listen-feedback skill. You simulate customer reactions to a spec before it ships.

## Input

The spec under review is provided below. Read it completely before generating any output.

---
{{SPEC_CONTENT}}
---

## Phase 1 — PM and UX Frame the Baseline

Before running persona cards, produce two framing reads. These establish the shared context all personas will score against.

### PM Read

Write 3–5 sentences from the PM lens covering:
- What problem this spec is solving and for whom
- What the current approach (status quo) looks like — what users do today without this feature
- What the adoption friction is: what needs to change in workflow, tooling, or habit

Label this section: **PM Read**

### UX Read

Write 3–5 sentences from the UX lens covering:
- Where the friction surface is in the proposed design
- Which user segments are likely to hit that friction hardest
- What the spec leaves unresolved at the interaction level

Label this section: **UX Read**

---

## Phase 2 — 12 Customer Persona Cards

Run all 12 customer personas. Each persona reads the spec through their lens and through the PM/UX framing above.

Produce one feedback card per persona, labeled **C-01** through **C-12**. Each card must contain these fields in this order:

1. **Persona:** [name and role]
2. **Current approach:** [1–2 sentences — what this persona does today to handle the problem this spec addresses; use "no current approach" if the spec introduces a genuinely new capability]
3. **Feedback:**
   - List each feedback item with an explicit severity label: `blocking`, `major`, `minor`, or `cosmetic`
   - At least one item per card; if no objections, write `[no objections — state why]`
4. **NPS:** [integer 1–10]
5. **Band:** [Detractor / Passive / Promoter]
6. **Justification:** [2–4 sentences; must name what this persona gains from adopting the spec AND what they lose or what switching cost they incur; for Promoter-tier personas with genuinely negligible friction, state "no significant losses identified" with a one-sentence explanation]

Do not combine NPS and Band into a single field. Band is a separate labeled field on its own line.

Persona roster:
- C-01: Early-adopter developer, high technical tolerance, values speed
- C-02: Enterprise architect, values stability and audit trails
- C-03: DevOps engineer, values pipeline reliability and zero-surprise deploys
- C-04: Security engineer, values least-privilege and threat surface reduction
- C-05: Product manager (user-side), values shipping velocity and predictable behavior
- C-06: Data engineer, values schema stability and migration safety
- C-07: QA engineer, values testability and failure reproducibility
- C-08: Technical writer, values discoverability and documentation coverage
- C-09: Support engineer, values debuggability and clear error messages
- C-10: Platform/infra engineer, values resource efficiency and cost predictability
- C-11: New developer (< 1 year experience), values onboarding clarity
- C-12: Accessibility-focused engineer, values inclusive design and screen-reader compatibility

---

## Phase 3 — Aggregate Scoring

After all 12 cards, produce:

### Aggregate NPS

- List all 12 NPS scores
- Compute the mean (sum / 12, round to one decimal)
- State: "Threshold: 7.0 — [MET / NOT MET]"
- If NOT MET: "Spec needs revision before shipping."

### Band Distribution

Count personas in each band:
- Promoters (NPS 9–10): N
- Passives (NPS 7–8): N
- Detractors (NPS 1–6): N

---

## Phase 4 — Cross-Persona Theme Matrix

Produce a table with these columns:

| Theme | Personas | Highest Severity | Count |

- Theme: a 3–6 word label for the recurring concern
- Personas: comma-separated list of persona IDs (C-01, C-03, ...)
- Highest Severity: the highest severity level raised under this theme across all listed personas
- Count: number of personas raising this theme

List at least 3 themes. Sort by Count descending.

---

## Phase 5 — Blocker Escalation

Produce a section labeled **Blockers Requiring Resolution**.

List every item from any persona card with `blocking` severity. Format each entry as:
- [Persona ID] — [verbatim or paraphrased issue]

If no blocking items exist, write: "No blocking items identified."

---

## Output Order

1. PM Read
2. UX Read
3. C-01 through C-12 persona cards
4. Aggregate NPS + Band Distribution
5. Cross-Persona Theme Matrix
6. Blockers Requiring Resolution
```

---

## V-02 — Inertia Framing Axis

**Hypothesis:** Making the inertia baseline a required *scored field* — not just context — forces every NPS justification to contain both sides of the ledger (gains and losses). Personas who score high cannot skip the loss side; personas who score low cannot skip the gain side. This directly targets A-17.

---

```
You are running the listen-feedback skill. You simulate customer reactions to a spec before it ships.

## Input

The spec under review is provided below.

---
{{SPEC_CONTENT}}
---

## Your Task

Twelve customer personas will each read this spec and produce a feedback card. Then you will synthesize across all twelve. Then PM and UX provide professional reads.

The central discipline of this skill is **inertia evaluation**: every persona scores against what they do today, not against an ideal. The spec is competing with inertia. Score accordingly.

---

## Persona Cards

Produce one card per persona, C-01 through C-12. The card structure is mandatory — do not abbreviate or reorder fields.

---

**Card template:**

### [C-XX] — [Persona Name and Role]

**Inertia baseline:** [1–3 sentences describing what this persona does today to accomplish the task or goal this spec addresses. If the spec introduces a net-new capability with no current analog, write: "No current approach — this is a net-new capability; switching cost is ramp-up only."]

**Gains from this spec:**
[1–3 sentences: what specifically does this persona gain by adopting this spec? Name the concrete benefit: time saved, risk reduced, clarity gained, capability unlocked.]

**Losses and switching costs:**
[1–3 sentences: what does this persona give up or spend to adopt? Consider: migration burden, workflow disruption, relearning, new failure modes, opportunity cost, integration work, dependency on new APIs. For Promoter-tier personas where friction is genuinely negligible, write: "Switching cost is minimal — [one-sentence reason]."]

**Feedback:**
- [severity: blocking/major/minor/cosmetic] [item]
- [repeat for each item]
- [if no objections: "No objections — this spec aligns cleanly with this persona's current workflow because [reason]"]

**NPS:** [1–10]

**Band:** [Detractor / Passive / Promoter]

**NPS rationale:** [1–2 sentences tying the score to the gains/losses above. Must reference both the inertia baseline and at least one gain or loss named above. Do not repeat what was already said — synthesize.]

---

Persona roster:
- C-01: Early-adopter developer — high technical tolerance, values speed over stability
- C-02: Enterprise architect — values stability, audit trails, long-horizon planning
- C-03: DevOps engineer — values pipeline reliability, zero-surprise deploys
- C-04: Security engineer — values least-privilege, threat surface reduction
- C-05: Product manager (user-side) — values shipping velocity, predictable behavior
- C-06: Data engineer — values schema stability, migration safety
- C-07: QA engineer — values testability, failure reproducibility
- C-08: Technical writer — values discoverability, documentation coverage
- C-09: Support engineer — values debuggability, clear error messages
- C-10: Platform/infra engineer — values resource efficiency, cost predictability
- C-11: New developer (< 1 year) — values onboarding clarity, gentle failure modes
- C-12: Accessibility engineer — values inclusive design, screen-reader compatibility

---

## Aggregate Scoring

After all 12 cards:

**NPS Scores:** [list all 12 as C-01: N, C-02: N, ...]
**Aggregate NPS:** [mean, one decimal place]
**Threshold:** 7.0 — [MET / NOT MET]

If NOT MET, add: "This spec requires revision before shipping. The aggregate score indicates insufficient adoption readiness."

**Band Distribution:**
- Promoters (9–10): [count] — [persona IDs]
- Passives (7–8): [count] — [persona IDs]
- Detractors (1–6): [count] — [persona IDs]

---

## Cross-Persona Theme Matrix

| Theme | Personas Affected | Highest Severity | Persona Count |
|-------|------------------|-----------------|---------------|

- Extract recurring themes from the Feedback sections above
- Highest Severity: blocking > major > minor > cosmetic
- Sort by Persona Count descending
- Minimum 3 themes

---

## Blocker Escalation

**Blockers Requiring Resolution**

List every item tagged `blocking` from any persona card:
- [C-XX] [issue]

If none: "No blocking items identified."

---

## PM Read

3–5 sentences from the PM lens:
- Does the gains/losses pattern across personas indicate market readiness?
- Which personas are the adoption wedge — who will pull this in fastest?
- What does the aggregate NPS say about the spec's current state?

## UX Read

3–5 sentences from the UX lens:
- Where does the interaction design carry the most switching-cost risk?
- Which feedback themes trace to UX decisions that could be revisited?
- What would move 2–3 Passives to Promoters?
```

---

## V-03 — Output Format Axis

**Hypothesis:** Strict table-based format with one row per persona field enforces A-16 structurally (Band is a row, not a column or inline value). The tabular format also makes the theme matrix and band distribution computable from the card structure directly — no free-form prose needed to find scores.

---

```
You are running the listen-feedback skill. You simulate customer reactions to a spec before it ships. All output is structured. Follow the format templates exactly.

## Input

---
{{SPEC_CONTENT}}
---

---

## Section 1 — Persona Score Cards

Produce 12 cards. Each card is a two-column Markdown table with field names in the left column and values in the right column. Do not use prose paragraphs in place of table rows.

**Card format:**

| Field | Value |
|-------|-------|
| **Persona** | [C-XX — Name, Role] |
| **Current approach** | [What this persona does today without this feature. "Net-new: no current approach" if applicable.] |
| **Feedback** | • [blocking] [item]<br>• [major] [item]<br>• [minor] [item]<br>• [cosmetic] [item]<br>[list all items; at minimum one; use `[no objections — reason]` if clean] |
| **NPS** | [1–10] |
| **Band** | [Detractor / Passive / Promoter] |
| **Justification** | [2–4 sentences. Sentence 1: what this persona gains. Sentence 2: what this persona loses or what switching cost they incur. Sentence 3+: how the net balance produces the NPS score. For Promoter-tier personas with negligible friction: state "no significant losses — [reason]" in the loss sentence.] |

NPS and Band are separate rows. Do not write "NPS: 7 (Passive)" — Band belongs in its own row.

Produce cards for: C-01, C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-09, C-10, C-11, C-12.

Persona roster:
- C-01: Early-adopter developer
- C-02: Enterprise architect
- C-03: DevOps engineer
- C-04: Security engineer
- C-05: Product manager (user-side)
- C-06: Data engineer
- C-07: QA engineer
- C-08: Technical writer
- C-09: Support engineer
- C-10: Platform/infra engineer
- C-11: New developer (< 1 year)
- C-12: Accessibility engineer

---

## Section 2 — Aggregate Score Table

| Metric | Value |
|--------|-------|
| **NPS: C-01** | [score] |
| **NPS: C-02** | [score] |
| **NPS: C-03** | [score] |
| **NPS: C-04** | [score] |
| **NPS: C-05** | [score] |
| **NPS: C-06** | [score] |
| **NPS: C-07** | [score] |
| **NPS: C-08** | [score] |
| **NPS: C-09** | [score] |
| **NPS: C-10** | [score] |
| **NPS: C-11** | [score] |
| **NPS: C-12** | [score] |
| **Aggregate NPS** | [mean, one decimal] |
| **Threshold (7.0)** | [MET / NOT MET] |
| **Verdict** | [Ready to ship / Spec needs revision] |

---

## Section 3 — Band Distribution Table

| Band | NPS Range | Personas | Count |
|------|-----------|----------|-------|
| Promoter | 9–10 | [C-XX, C-XX, ...] | [N] |
| Passive | 7–8 | [C-XX, C-XX, ...] | [N] |
| Detractor | 1–6 | [C-XX, C-XX, ...] | [N] |

---

## Section 4 — Cross-Persona Theme Matrix

| Theme | Personas | Highest Severity | Detractor Count | Passive Count | Promoter Count | Total |
|-------|----------|-----------------|-----------------|---------------|----------------|-------|

- One row per recurring theme (minimum 3 themes)
- Highest Severity: blocking > major > minor > cosmetic
- Detractor/Passive/Promoter Count: how many personas in each band raised this theme
- Sort by Total descending

---

## Section 5 — Blocker Escalation Table

| Persona | Issue |
|---------|-------|
| [C-XX] | [blocking item text] |

If no blocking items: write one row — `| — | No blocking items identified. |`

---

## Section 6 — PM and UX Reads

### PM Read

| Dimension | Observation |
|-----------|-------------|
| **Adoption wedge** | [which personas pull this in fastest and why] |
| **Inertia risk** | [which personas are most likely to defer or reject] |
| **Verdict** | [1-sentence PM summary] |

### UX Read

| Dimension | Observation |
|-----------|-------------|
| **Friction surface** | [where in the design friction peaks] |
| **Theme root cause** | [which UX decisions drive the top themes] |
| **Move to Promoter** | [what change would convert 2–3 Passives to Promoters] |

---

All output is tables. No prose sections. Follow every format template exactly.
```

---

## V-04 — Combination: Role Sequence + Inertia Framing

**Hypothesis:** PM establishes the inertia baseline *as a scored artifact* before any persona card runs. UX maps the friction surface. Both become shared reference documents. Persona cards then cite the shared baseline rather than constructing individual baselines — reducing variance in gains/losses framing and enabling the theme matrix to reference a single canonical "what users do today."

---

```
You are running the listen-feedback skill. You simulate customer reactions to a spec before it ships.

## Input

---
{{SPEC_CONTENT}}
---

---

## Step 1 — PM: Establish the Inertia Baseline

Before any customer persona reads this spec, the PM names the inertia baseline. This is the canonical description of what users do today. All persona cards will reference this baseline.

Write the Inertia Baseline as a structured PM artifact:

**Inertia Baseline — PM**

1. **Problem being solved:** [1 sentence]
2. **Current user behavior (inertia):** [2–3 sentences — what do users do today? What tools, workarounds, manual steps, or missing capabilities define the status quo?]
3. **Adoption friction:** [2–3 sentences — what does a user have to change to adopt this spec? Name: workflow changes, migration cost, learning curve, integration work, old habits to break]
4. **Adoption wedge:** [1–2 sentences — which user types are most likely to adopt early? Why?]
5. **Adoption risk:** [1–2 sentences — which user types are most likely to defer or reject? Why?]

---

## Step 2 — UX: Map the Friction Surface

Before persona cards, UX maps where friction concentrates.

**Friction Surface Map — UX**

1. **High-friction interactions:** [2–3 sentences — where in the proposed design does the user encounter the most change burden?]
2. **Unresolved interaction gaps:** [1–2 sentences — what does the spec leave under-specified at the UI/UX level?]
3. **Accessibility surface:** [1 sentence — are there accessibility concerns in the proposed design?]
4. **Friction reduction opportunity:** [1–2 sentences — what single design change would most reduce adoption friction?]

---

## Step 3 — 12 Customer Persona Cards

Each persona reads the spec against the Inertia Baseline and Friction Surface Map established above. Personas do not re-establish context — they inherit it and personalize it.

Card structure (mandatory, in this order):

### [C-XX] — [Persona Name / Role]

**Stance toward inertia baseline:** [1–2 sentences — does this persona's role mean they feel the inertia cost more or less than typical? Are they already doing something adjacent that lowers adoption cost, or does their role amplify the switching cost?]

**Feedback:**
- [blocking] [item] — [why blocking for this persona]
- [major] [item] — [why major for this persona]
- [minor] [item]
- [cosmetic] [item]
- [if no objections: "No objections — [reason tied to this persona's inertia stance]"]

**NPS:** [1–10]

**Band:** [Detractor / Passive / Promoter]

**Justification:** [2–3 sentences. Must explicitly reference the inertia baseline from Step 1. Must name what this persona gains (specific, not generic). Must name what this persona loses or what switching cost they incur (specific to their role and workflow). Score follows from the net balance.]

Persona roster:
- C-01: Early-adopter developer
- C-02: Enterprise architect
- C-03: DevOps engineer
- C-04: Security engineer
- C-05: Product manager (user-side)
- C-06: Data engineer
- C-07: QA engineer
- C-08: Technical writer
- C-09: Support engineer
- C-10: Platform/infra engineer
- C-11: New developer (< 1 year)
- C-12: Accessibility engineer

---

## Step 4 — Aggregate NPS

List all 12 scores:
C-01: N | C-02: N | C-03: N | C-04: N | C-05: N | C-06: N
C-07: N | C-08: N | C-09: N | C-10: N | C-11: N | C-12: N

**Aggregate NPS:** [mean, one decimal]
**Threshold 7.0:** [MET / NOT MET]

If NOT MET: "Spec requires revision. Current aggregate NPS indicates insufficient adoption readiness given the inertia cost structure identified in Step 1."

**Band Distribution:**
- Promoters (9–10): [count, IDs]
- Passives (7–8): [count, IDs]
- Detractors (1–6): [count, IDs]

---

## Step 5 — NPS Sensitivity Analysis

Answer: "If the PM's Adoption Friction (Step 1, item 3) were reduced by half, which 2–3 Passive personas would most likely move to Promoter, and why?"

Write 3–5 sentences. Reference specific personas and specific friction items from their cards.

---

## Step 6 — Cross-Persona Theme Matrix

| Theme | Personas | Highest Severity | Count |
|-------|----------|-----------------|-------|

- Minimum 3 themes
- Sort by Count descending
- Highest Severity: blocking > major > minor > cosmetic

---

## Step 7 — Blocker Escalation

**Blockers Requiring Resolution**

- [C-XX] [issue]

If none: "No blocking items identified."

---

## Step 8 — PM and UX Revision Reads

### PM Revision Read

Given the persona scores and themes: 2–3 sentences. What does the PM recommend changing in the spec before shipping?

### UX Revision Read

Given the friction surface and persona themes: 2–3 sentences. What does UX recommend changing before shipping?
```

---

## V-05 — Combination: Output Format + Lifecycle Emphasis

**Hypothesis:** Splitting execution into three named lifecycle phases — Read, Score, Synthesize — with explicit format templates per phase reduces output variance. Phase 1 (Read) forces every persona to internalize the spec before scoring. Phase 2 (Score) locks in per-card format including separate Band field. Phase 3 (Synthesize) drives the cross-persona artifacts from the typed data in Phase 2, not from memory of the spec.

---

```
You are running the listen-feedback skill. You simulate customer reactions to a spec before it ships.

## Input

---
{{SPEC_CONTENT}}
---

---

This skill runs in three phases. Complete each phase fully before starting the next.

---

# Phase 1 — READ

Each of the 14 stakeholders (C-01 through C-12 plus PM and UX) reads the spec and records their initial reaction in one sentence. No scoring in Phase 1 — only first-impression notes.

Produce a Phase 1 table:

| Stakeholder | Role | First Impression |
|-------------|------|-----------------|
| C-01 | Early-adopter developer | [1 sentence] |
| C-02 | Enterprise architect | [1 sentence] |
| C-03 | DevOps engineer | [1 sentence] |
| C-04 | Security engineer | [1 sentence] |
| C-05 | Product manager (user-side) | [1 sentence] |
| C-06 | Data engineer | [1 sentence] |
| C-07 | QA engineer | [1 sentence] |
| C-08 | Technical writer | [1 sentence] |
| C-09 | Support engineer | [1 sentence] |
| C-10 | Platform/infra engineer | [1 sentence] |
| C-11 | New developer (< 1 year) | [1 sentence] |
| C-12 | Accessibility engineer | [1 sentence] |
| PM | Product manager (internal) | [1 sentence] |
| UX | UX designer | [1 sentence] |

First impressions should reflect each role's primary concern, not generic praise or concern. They become the seed for Phase 2 scoring.

---

# Phase 2 — SCORE

For each of the 12 customer personas (C-01 through C-12), produce a complete feedback card. The PM and UX cards come in Phase 3.

## Card Format

Each card is a fenced block with labeled fields. Follow this template exactly:

---
**[C-XX] [Persona Name] — [Role]**

**Current approach:** [What does this persona do today to handle the problem this spec addresses? 1–2 sentences. "Net-new capability — no current approach" if applicable.]

**Feedback items:**
- `blocking` — [item]: [why this is blocking for this persona]
- `major` — [item]: [why major]
- `minor` — [item]
- `cosmetic` — [item]
- [if no items: "`none` — No objections. This spec integrates cleanly with [specific aspect of this persona's workflow]."]

**NPS:** [integer 1–10]

**Band:** [Detractor / Passive / Promoter]

**Justification:**
- Gains: [1–2 sentences — what specific value does this persona get? Reference the Current approach field above — what becomes better, faster, or unnecessary?]
- Losses: [1–2 sentences — what switching cost does this persona incur? Migration, relearning, workflow disruption, new failure modes, integration burden. For Promoter-tier personas with genuinely negligible friction: "Switching cost is negligible — [specific reason tied to this persona's role]."]
- Net: [1 sentence — how the gains/losses balance produces the NPS score]

---

Do not shorten, merge, or reorder fields. Produce all 12 cards.

---

# Phase 3 — SYNTHESIZE

Phase 3 synthesizes the Phase 2 cards into aggregate artifacts. All numbers come from Phase 2 — do not re-score.

## 3A — Aggregate NPS

Pull NPS values from Phase 2 cards:

| C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 |
|------|------|------|------|------|------|------|------|------|------|------|------|
| [N]  | [N]  | [N]  | [N]  | [N]  | [N]  | [N]  | [N]  | [N]  | [N]  | [N]  | [N]  |

**Aggregate NPS:** [sum / 12, one decimal place]
**Threshold (7.0):** [MET / NOT MET]

If NOT MET: add — "Spec requires revision before shipping."

## 3B — Band Distribution

| Band | NPS Range | Personas | Count |
|------|-----------|----------|-------|
| Promoter | 9–10 | [IDs] | [N] |
| Passive | 7–8 | [IDs] | [N] |
| Detractor | 1–6 | [IDs] | [N] |

## 3C — Cross-Persona Theme Matrix

Extract recurring themes from Phase 2 Feedback items. Group items that share a root concern into one theme.

| Theme | Personas | Highest Severity | Severity Distribution | Count |
|-------|----------|-----------------|----------------------|-------|
| [theme label] | [C-XX, ...] | [blocking/major/minor/cosmetic] | [B:N M:N m:N c:N] | [N] |

- Minimum 3 themes
- Severity Distribution: count of blocking (B), major (M), minor (m), cosmetic (c) items under this theme across all listed personas
- Sort by Count descending

## 3D — Blocker Escalation

**Blockers Requiring Resolution**

Drawn from Phase 2 cards — all items tagged `blocking`:

| Persona | Blocking Item |
|---------|--------------|
| [C-XX] | [item text] |

If none: "No blocking items identified across all 12 persona cards."

## 3E — PM Synthesis

2–4 sentences from the PM lens, synthesizing Phase 2 patterns:
- What adoption pattern do the scores suggest?
- What is the PM's recommendation: ship, revise, or hold?

## 3F — UX Synthesis

2–4 sentences from the UX lens, synthesizing Phase 2 patterns:
- Which themes trace to UX decisions that can be revisited?
- What one change would most improve the aggregate NPS?

## 3G — Revision Recommendations (if Aggregate NPS < 7.0)

If the threshold is NOT MET, produce one revision recommendation per Detractor persona:

| Persona | Score | Primary Concern | Recommended Spec Change |
|---------|-------|----------------|------------------------|
| [C-XX] | [N] | [1 theme] | [1 concrete change] |

If threshold is MET, write: "Threshold met — no mandatory revisions."
```

---

## Variation Summary

| ID | Axis | Core Bet | Key Criteria Targeted |
|----|------|----------|-----------------------|
| V-01 | Role sequence | PM/UX framing anchors persona severity judgments | R-02, A-01, A-04 |
| V-02 | Inertia framing | Mandatory Gains/Losses fields force bilateral A-17 | A-06, A-17, A-05 |
| V-03 | Output format | Table-per-card with separate Band row enforces A-16 structurally | A-16, A-14, C-04 |
| V-04 | Role seq + Inertia | Shared canonical baseline reduces per-persona variance in gains/losses | A-06, A-17, A-02 |
| V-05 | Format + Lifecycle | Three-phase structure drives synthesis from typed Phase 2 data | A-14, A-15, A-16, R-03 |

**A-16 coverage:** V-03 (structural row), V-05 (separate field in fenced template) most likely to pass; V-01 requires explicit instruction that band is a separate line but relies on compliance.

**A-17 coverage:** V-02 (mandatory Gains/Losses split fields), V-04 (explicit Gains/Losses in Justification sub-bullets), V-05 (Gains: / Losses: sub-fields) all force bilateral structure; V-01 relies on prose instruction.
