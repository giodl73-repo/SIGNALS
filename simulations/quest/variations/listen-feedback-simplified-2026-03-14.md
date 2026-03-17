I'll read the V-05 winning prompt body (lines 559–736 of R20) and do the simplification analysis directly from what I've read.

---

## Simplified Prompt Body

---

You are simulating customer reactions to a spec before it ships. Twelve customer personas will evaluate the spec through their specific lens. All sections are required.

---

### Persona Reference

| ID | Role | Primary Lens |
|----|------|-------------|
| C-01 | Enterprise IT Admin | Security, compliance, audit, IT governance, change control |
| C-02 | SMB Owner | Speed to value, cost sensitivity, minimal setup |
| C-03 | Developer / Power User | APIs, scripting, extensibility, automation pipelines |
| C-04 | Non-Technical End User | Guided onboarding, plain language, mistake tolerance |
| C-05 | Compliance Officer | Data residency, retention policies, regulatory controls, audit |
| C-06 | Buyer-Side PM | ROI, integration fit, procurement risk, adoption potential |
| C-07 | Customer Support Lead | Ticket deflection, self-service coverage, escalation clarity |
| C-08 | Data Analyst | Reporting, exports, query access, data freshness |
| C-09 | Mobile-First User | Mobile responsiveness, offline capability, push notifications |
| C-10 | Accessibility User | WCAG 2.1 AA, keyboard navigation, screen reader compatibility |
| C-11 | Security Researcher | Attack surface, auth flows, data exposure, input validation |
| C-12 | Executive Sponsor | Strategic alignment, vendor risk, business outcomes |

---

### Section 1 — Persona Feedback Cards

For each persona C-01 through C-12, produce a card using the numbered field manifest below. All numbered fields are required.

**C-NN — [Persona Role]**

1. **Current approach:**
   - **What it delivers:** Name the status-quo tool or workflow and what it provides this persona today.
   - **Where it falls short:** The specific gap or limitation the current approach does not address for this persona.
   - **Floor-level switching cost:** The minimum friction this persona bears when switching away from their current approach.
   - **Persona-specific workflow disruption:** How adoption would disrupt this persona's specific daily workflow, beyond the general switching cost.

2. **Gains from this spec** (requires corresponding **Losses and switching costs** [Field 3] — completing Field 2 without Field 3 constitutes bilateral coverage failure; anchor gain from **"Where it falls short"** in Field 1): One sentence naming what this persona gains from the spec relative to their current approach. Reference at least one named spec element.

3. **Losses and switching costs** (requires corresponding **Gains from this spec** [Field 2] — completing Field 3 without Field 2 constitutes bilateral coverage failure; anchor cost from **"Floor-level switching cost"** and **"Persona-specific workflow disruption"** in Field 1): One sentence naming what this persona gives up or bears when adopting.

4. **NPS:** [integer 1–10] — [one sentence synthesizing Fields 2 and 3 into a net score; reference at least one named spec element]

5. **NPS band:** [Detractor (1–6) / Passive (7–8) / Promoter (9–10)]

6. **Feedback** (blocking first, then major, minor, cosmetic):
   - [blocking] [item] — *cannot ship to this persona without resolving*
   - [major] [item] — *significant friction or missing value; reduces adoption*
   - [minor] [item] — *irritant; manageable workaround exists*
   - [cosmetic] [item] — *polish issue; no functional impact*
   *(If no objections: state "No objections from this lens.")*

7. **Willingness to adopt:** [percentage or Low/Medium/High]. Clears adoption threshold (≥60%): [Yes/No].

8. **Revision recommendation:** One sentence naming the specific spec change — referencing a named spec element — that would most improve this persona's NPS.

---

### Section 2 — Blocker Escalation

**Blockers Requiring Resolution:**

Aggregate every `blocking` severity item from all 12 cards:
- C-NN: [description]

State "None identified" if no blocking items exist.

---

### Section 3 — Cross-Persona Theme Matrix

| Theme | Personas | Peak Severity | Severity Pattern | Recommended Action |
|-------|----------|---------------|-----------------|-------------------|

Identify at minimum one theme. Order themes descending by peak severity. Each row must include a severity pattern annotation.

---

### Section 4 — Professional Lens Synthesis

**Role ordering and failure mode (stated here, at the ordering instruction):** The UX Read runs before the PM Read. Failure mode if reversed: commercial framing would anchor the usability assessment, causing UX-rooted rejection to be reframed as pricing objections rather than identified as UX failures.

**UX Read (runs first):**
Synthesize usability and accessibility signals. 3 sentences: dominant usability risk, accessibility finding, what UX is working well.

**PM Read (runs second):**
Synthesize adoption, ROI, and purchase-intent signals. 3 sentences: primary adoption barrier, purchase intent driver, go-to-market objection.

**Convergence:**
One sentence: where do the UX and PM reads agree? Where do they diverge?

---

### Section 5 — Aggregate NPS

#### S.1 — Derivation Phase

Execute steps D.1 through D.4 in sequence. Each step is a phase exit condition — the next step cannot begin until the current step is complete.

**D.1 — State formula and failure mode (required before D.2 can begin)**

State the CI formula before any score collection or computation proceeds:

> CI formula: Mean ± 1.96·(SD/√12), where n = 12 personas and SD is the population standard deviation of the 12 NPS scores.
>
> Failure mode this formula requirement prevents: Without the formula parenthetical (±1.96·[SD_value]/√12) alongside the reported interval, the CI annotation cannot be verified against different score inputs — a reader cannot confirm whether the interval was computed as ±1.96·SD/√12 or via a different method. The formula must appear co-located with the CI value so that any reader following this step encounters both the rule and its verification basis in a single pass.

D.2 cannot begin until D.1 is stated, including both the formula and the failure mode annotation above.

**D.2 — Score collection and mean**

List all 12 scores:
C-01=[N], C-02=[N], C-03=[N], C-04=[N], C-05=[N], C-06=[N],
C-07=[N], C-08=[N], C-09=[N], C-10=[N], C-11=[N], C-12=[N]

Sum: [total]
Mean NPS: [sum / 12, to 2 decimal places]

Band distribution: Promoters (9–10): [count] | Passives (7–8): [count] | Detractors (1–6): [count]
Dominant Detractor objection: [most common blocking or major objection among Detractor-tier personas]

**D.3 — Standard deviation computation**

For each of the 12 scores, compute (score − mean)²:
[list all 12 squared deviation values]

Sum of squared deviations: [value]
Population variance: [sum of squared deviations / 12, to 6 decimal places]
SD: √[variance] = [value to 4 decimal places]

**D.4 — Apply formula and report**

Applying the formula stated in D.1:
Margin: 1.96 × [SD] / √12 = 1.96 × [SD] / 3.4641 = [margin to 4 decimal places]
95% CI: ([mean − margin, to 2 dp], [mean + margin, to 2 dp])

Report line: "95% CI: ([lower], [upper]) using formula ±1.96·[SD_value]/√12"

#### S.2 — Threshold Evaluation

Aggregate NPS: [mean to 2 dp]
Threshold: 7.0
Verdict: **PASS** (≥7.0, spec ready for development) | **FAIL** (<7.0, spec needs revision)

---

### Section 6 — Sensitivity Analysis

Identify the 2–3 personas whose NPS scores have the highest absolute deviation from the aggregate mean.

For each high-influence persona, report **directionally separated** score deltas. Upward (+1) and downward (−1) effects must be reported as distinct lines. A symmetric ±delta figure without directional separation does not satisfy this section.

**[C-NN — Persona Role]**
- Current score: [X] | Aggregate mean: [mean to 2 dp] | Deviation: [X − mean = delta to 2 dp]
- **Upward delta (+1):** If C-NN score → [X+1], new aggregate mean = [computed to 2 dp] (Δ = +[1/12 to 3 dp])
  - Band crossing? [Yes: [X] was [band], [X+1] is [new band] — or No: score stays within [band]]
- **Downward delta (−1):** If C-NN score → [X−1], new aggregate mean = [computed to 2 dp] (Δ = −[1/12 to 3 dp])
  - Band crossing? [Yes: [X] was [band], [X−1] is [new band] — or No: score stays within [band]]
- **Asymmetry note:** One sentence describing whether the upward and downward swings have different narrative implications for spec readiness.

NPS band thresholds for band-crossing detection: Detractor/Passive boundary at 6/7; Passive/Promoter boundary at 8/9.

---

### Section 7 — Revision Directive (FAIL only)

Include this section only if aggregate NPS < 7.0.

**Revision Required:**

*Pass 1 — Per-persona targeted changes:*
For each persona scoring below 7.0, state the single highest-priority spec change referencing a named spec element. Blocking items take priority.

*Pass 2 — Cross-persona prioritized summary:*
Top 3 revisions ranked by (personas affected × maximum severity). For each: issue, personas affected, cost tier (low-cost = copy/label/wording; high-cost = architecture or workflow), minimal spec change.

---

## Simplification Report

### What was removed and why

| # | Removed | Location | Why | Words |
|---|---------|----------|-----|-------|
| 1 | "This protocol uses a structured inertia baseline, conjunctive bilateral gains/losses field instructions, a derivation-phase CI computation with co-located failure mode annotation, and a directional sensitivity analysis." | Intro sentence 3 | Meta-description of protocol design — the sections themselves do this work | ~27 |
| 2 | "Omitting any numbered field constitutes an incomplete card." | Section 1 preamble | Redundant: "All numbered fields are required" covers it | ~9 |
| 3 | Field 2 parenthetical verbose lead ("this field requires a corresponding entry in") + tail ("relative to their current approach, drawing from the 'Where it falls short' gap") | Field 2 | Lead compressed to "requires corresponding"; tail is restatement of the parenthetical's own anchor instruction | ~32 |
| 4 | Field 3 parenthetical verbose lead + tail ("drawing from the 'Floor-level switching cost' or 'Persona-specific workflow disruption.'") + "Neither Field 2 nor Field 3 is complete without the other." | Field 3 | Same pattern as Field 2; "Neither...without the other" repeats the bilateral failure statement already in both parentheticals | ~36 |
| 5 | Section 4 role ordering compression: "ROI arguments, procurement fit, adoption projections —" detail + "A reader following this ordering instruction encounters both the constraint (UX first) and its epistemic grounding (PM framing anchors UX if reversed) in a single pass, making the sequence a principled constraint rather than an arbitrary choice." | Section 4 | Detail list is illustrative not instructive; final sentence is meta-commentary on the instruction design, not an instruction | ~72 |
| 6 | "from the 12 persona cards" from UX Read | Section 4 | Implicit from context | ~4 |
| 7 | "A CI report produced without completing D.1 first cannot satisfy the formula requirement by adding the parenthetical after the fact. The formula must be an input to the computation, not a decoration on the output." | S.1 preamble | Verbatim restatement of what D.1's failure mode annotation already says | ~38 |
| 8 | "An output that reports a CI interval without the formula parenthetical fails D.1 validation regardless of whether the interval bounds are numerically correct." | D.1 failure mode | Redundant summary of the preceding two sentences; adds no new constraint | ~27 |
| 9 | "the upward and downward effects are reported as independent findings because NPS band crossings are asymmetrically distributed around the current score: a +1 move may cross a band threshold while a −1 move stays within band, producing different narrative implications." | Section 6 | Explains WHY directional separation is required; the format template that follows enforces it structurally. The "does not satisfy this section" enforcement sentence is kept. | ~47 |
| 10 | "These are the high-influence personas." | Section 6 | Restates what "Identify the 2–3 personas..." already established | ~5 |
| 11 | S.2 verdict format compressed | S.2 | "spec ready for development | FAIL — aggregate NPS < 7.0, spec needs revision before proceeding" → "(≥7.0, spec ready for development) \| FAIL (<7.0, spec needs revision)" | ~10 |
| 12 | Section 7 Pass 2: nested bullet format → inline | Section 7 | "For each revision: - Issue: [description] - Personas affected: [list]..." → "For each: issue, personas affected, cost tier..., minimal spec change." | ~14 |
| 13 | "over major items" | Section 7 Pass 1 | "Blocking items take priority" is unambiguous without it | ~3 |

**Total removed: ~324 words**

### Criteria verification

| Criterion | Mechanism preserved | Still passes? |
|-----------|--------------------|--------------:|
| A-16 | Field 1 retains all 4 labeled sub-fields | YES |
| A-17 | Field 2 and Field 3 parentheticals each name the other and declare bilateral coverage failure | YES |
| A-21 | Each field names the other by label as a conjunctive requirement | YES |
| A-24 | Field 2 cites "Where it falls short"; Field 3 cites "Floor-level switching cost" and "Persona-specific workflow disruption" | YES |
| A-28 | Section 6 enforces distinct upward/downward lines + "A symmetric ±delta figure...does not satisfy this section" | YES |
| A-29 | D.4 Report line requires "using formula ±1.96·[SD_value]/√12" | YES |
| A-30 | D.1 gate + D.1→D.4 phase sequence + "D.2 cannot begin until D.1 is stated" | YES |
| A-31 | D.1 failure mode annotation co-located within the formula constraint step | YES |

All essential criteria preserved.

```json
{"simplified_word_count": 1219, "original_word_count": 1543, "all_essential_still_pass": true}
```
