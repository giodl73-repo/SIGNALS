# listen-feedback Variate — Round 20
**Date:** 2026-03-15
**Rubric:** v17 (A-30 + A-31 introduced in R19; now fully covered by R19 V-05)
**Target criteria:** A-16 (structured inertia sub-fields), A-17 (bilateral coverage), A-21 (conjunctive framing), A-24 (sub-field cross-reference), A-28 (directional sensitivity)

---

## Round 20 Variation Map

| Variation | Axis | A-16 | A-17 | A-21 | A-24 | A-28 | A-29/30/31 |
|-----------|------|------|------|------|------|------|------------|
| V-01 | Output Format (card sub-fields) | PASS | FAIL | FAIL | FAIL | FAIL | A-29 only |
| V-02 | Output Format (conjunctive bilateral fields) | FAIL | PASS | PASS | FAIL | FAIL | A-29 only |
| V-03 | Lifecycle Emphasis (directional sensitivity phase) | FAIL | FAIL | FAIL | FAIL | PASS | A-29 only |
| V-04 | Combination: Full inertia chain | PASS | PASS | PASS | PASS | FAIL | A-29 only |
| V-05 | Combination: Full stack (R19 V-05 base + inertia chain + directional sensitivity) | PASS | PASS | PASS | PASS | PASS | A-29+30+31 |

---

## V-01 — Output Format (Structured Inertia Sub-Fields)

**Axis:** Output format — persona card field structure
**Hypothesis:** Replacing the prose `Current approach:` field with a 4-sub-field structured baseline (What it delivers / Where it falls short / Floor-level switching cost / Persona-specific workflow disruption) grounds the NPS justification in a structured delta computation rather than freeform prose. A-16 passes because the field contains at least three distinctly labeled sub-fields. A-17, A-21, A-24 do not pass — the NPS justification is still a single prose sentence and the gains/losses split is not structurally enforced. A-09 passes because the field is labeled `**Current approach:**`.

---

You are simulating customer reactions to a spec before it ships. Twelve customer personas will evaluate the spec through their specific lens. Produce a complete signal-gathering report following the protocol below. All sections are required.

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

### Step 1 — Persona Feedback Cards

Generate one card per persona, C-01 through C-12 in sequence. Use the numbered field manifest below for every card. Omitting any numbered field constitutes an incomplete card.

**C-NN — [Persona Role]**

1. **Current approach:**
   - **What it delivers:** Name the status-quo tool or workflow and what it provides this persona today.
   - **Where it falls short:** The specific gap or limitation the current approach does not address for this persona.
   - **Floor-level switching cost:** The minimum friction this persona bears when switching away from their current approach.
   - **Persona-specific workflow disruption:** How adoption of the spec's feature would disrupt this persona's specific daily workflow, beyond the general switching cost above.

2. **NPS:** [integer 1–10] — [one sentence: what this persona gains or loses relative to the inertia baseline in Field 1; reference at least one named spec element]

3. **NPS band:** [Detractor (1–6) / Passive (7–8) / Promoter (9–10)]

4. **Feedback** (severity-first: blocking → major → minor → cosmetic):
   - [blocking] [item] — *cannot ship to this persona without resolving*
   - [major] [item] — *significant friction or missing value; reduces adoption*
   - [minor] [item] — *irritant; manageable workaround exists*
   - [cosmetic] [item] — *polish issue; no functional impact*
   *(If no objections: state "No objections from this lens.")*

5. **Revision recommendation:** One sentence naming the specific spec change — referencing a named spec element — that would most improve this persona's NPS.

---

### Step 2 — Blocker Escalation

**Blockers Requiring Resolution:**

Aggregate every `blocking` severity item from all 12 cards:
- C-NN: [description]

State "None identified" if no blocking items exist across all 12 personas.

---

### Step 3 — Cross-Persona Theme Matrix

| Theme | Personas | Peak Severity | Severity Pattern | Recommended Action |
|-------|----------|---------------|-----------------|-------------------|

Identify at minimum one theme. Order themes descending by peak severity. Each row must include a severity pattern annotation.

---

### Step 4 — Professional Lens Synthesis

**Role ordering and rationale (stated here, at the ordering instruction):** The UX Read runs before the PM Read. Failure mode prevented by this ordering: if PM Read preceded UX Read, commercial framing — ROI arguments, procurement fit, adoption projections — would anchor the usability assessment, causing UX-rooted rejection to be reframed as pricing or positioning objections rather than identified as UX failures. UX signals must surface independently before PM synthesis can proceed against a known usability baseline.

**UX Read (runs first):**
Synthesize usability and accessibility signals from the 12 persona cards. 3 sentences: dominant usability risk, accessibility finding, what UX is working well.

**PM Read (runs second):**
Synthesize adoption, ROI, and purchase-intent signals. 3 sentences: primary adoption barrier, purchase intent driver, go-to-market objection.

**Convergence:**
One sentence: where do the UX and PM reads agree? Where do they diverge?

---

### Step 5 — Aggregate NPS

Compute aggregate NPS as the arithmetic mean of the 12 persona NPS scores. Both blocks below are required. A [CI BLOCK] that omits the formula notation ±1.96·[SD_value]/√12 fails output validation.

**[SCORE BLOCK]**
Persona scores: C-01=[N], C-02=[N], C-03=[N], C-04=[N], C-05=[N], C-06=[N], C-07=[N], C-08=[N], C-09=[N], C-10=[N], C-11=[N], C-12=[N]
Sum: [total]
Mean NPS: [sum / 12, to 2 decimal places]
Band distribution: Promoters (9–10): [count] | Passives (7–8): [count] | Detractors (1–6): [count]
Dominant Detractor objection: [most common blocking or major objection raised by Detractor-tier personas, with count of Detractors citing it]
Threshold: 7.0
Result: [PASS — aggregate NPS ≥ 7.0, spec ready for development] or [FAIL — aggregate NPS < 7.0, spec needs revision]

**[CI BLOCK]**
CI Formula: ±1.96·(SD/√12)
SD: [population standard deviation of the 12 persona scores, to 4 decimal places]
Margin: 1.96 × [SD] / √12 = [computed margin, to 4 decimal places]
95% CI: ([mean − margin, to 2 dp], [mean + margin, to 2 dp])
Report as: "[mean] ± [margin] using formula ±1.96·[SD_value]/√12"

---

### Step 6 — Revision Directive (FAIL only)

Include this section only if aggregate NPS < 7.0.

**Revision Required:**

*Pass 1 — Per-persona targeted changes:*
For each persona scoring below 7.0, state the single highest-priority spec change referencing a named spec element. Blocking items take priority over major items.

*Pass 2 — Cross-persona prioritized summary:*
Top 3 revisions ranked by (personas affected × maximum severity). For each: issue, personas affected, cost tier (low-cost = copy/label/wording changes; high-cost = architecture or workflow changes), minimal spec change.

---

## V-02 — Output Format (Conjunctive Bilateral Gains/Losses)

**Axis:** Output format — bifurcated NPS justification with conjunctive bilateral enforcement
**Hypothesis:** Splitting the NPS justification into two separate fields — `Gains from this spec` (Field 2) and `Losses and switching costs` (Field 3) — and writing each field instruction so it names the other field by label and explicitly prohibits completion without the other passes A-17 (bilateral coverage requirement) and A-21 (conjunctive framing) simultaneously. A-16 does not pass because Field 1 is still prose. A-24 does not pass because Field 2 and Field 3 instructions do not cross-reference named Step 0 sub-fields (there are none — Field 1 is unstructured). A-28 not addressed.

---

You are simulating customer reactions to a spec before it ships. Twelve customer personas will evaluate the spec through their specific lens. Produce a complete signal-gathering report following the protocol below. All sections are required.

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

### Step 1 — Persona Feedback Cards

Generate one card per persona, C-01 through C-12 in sequence. Use the numbered field manifest below for every card. Omitting any numbered field constitutes an incomplete card.

**C-NN — [Persona Role]**

1. **Current approach:** What this persona does today without the spec's feature. Name the status-quo workflow or tool. If no equivalent exists, state that explicitly.

2. **Gains from this spec** (this field requires a corresponding entry in **Losses and switching costs** [Field 3] — completing Gains without Losses constitutes bilateral coverage failure): One sentence naming what this persona gains from the spec relative to their current approach in Field 1. Reference at least one named spec element.

3. **Losses and switching costs** (this field requires a corresponding entry in **Gains from this spec** [Field 2] — completing Losses without Gains constitutes bilateral coverage failure): One sentence naming what this persona gives up or bears when adopting the spec. Reference the persona's current workflow from Field 1. Neither Field 2 nor Field 3 is complete without the other.

4. **NPS:** [integer 1–10] — [one sentence synthesizing the gain and loss signals from Fields 2 and 3 into a score; reference at least one named spec element]

5. **NPS band:** [Detractor (1–6) / Passive (7–8) / Promoter (9–10)]

6. **Feedback** (severity-first: blocking → major → minor → cosmetic):
   - [blocking] [item] — *cannot ship to this persona without resolving*
   - [major] [item] — *significant friction or missing value; reduces adoption*
   - [minor] [item] — *irritant; manageable workaround exists*
   - [cosmetic] [item] — *polish issue; no functional impact*
   *(If no objections: state "No objections from this lens.")*

7. **Revision recommendation:** One sentence naming the specific spec change — referencing a named spec element — that would most improve this persona's NPS.

---

### Step 2 — Blocker Escalation

**Blockers Requiring Resolution:**

Aggregate every `blocking` severity item from all 12 cards:
- C-NN: [description]

State "None identified" if no blocking items exist across all 12 personas.

---

### Step 3 — Cross-Persona Theme Matrix

| Theme | Personas | Peak Severity | Severity Pattern | Recommended Action |
|-------|----------|---------------|-----------------|-------------------|

Identify at minimum one theme. Order themes descending by peak severity. Each row must include a severity pattern annotation.

---

### Step 4 — Professional Lens Synthesis

**Role ordering and rationale (stated here, at the ordering instruction):** The UX Read runs before the PM Read. Failure mode prevented: if PM Read preceded UX Read, commercial framing would anchor the usability assessment, causing UX-rooted rejection to be reframed as pricing objections rather than identified as UX failures. Running UX first ensures usability signals surface independently of commercial framing.

**UX Read (runs first):**
Synthesize usability and accessibility signals from the 12 persona cards. 3 sentences: dominant usability risk, accessibility finding, what UX is working well.

**PM Read (runs second):**
Synthesize adoption, ROI, and purchase-intent signals. 3 sentences: primary adoption barrier, purchase intent driver, go-to-market objection.

**Convergence:**
One sentence: where do the UX and PM reads agree? Where do they diverge?

---

### Step 5 — Aggregate NPS

Compute aggregate NPS as the arithmetic mean of the 12 persona NPS scores. Both blocks below are required. A [CI BLOCK] that omits the formula notation ±1.96·[SD_value]/√12 fails output validation.

**[SCORE BLOCK]**
Persona scores: C-01=[N], C-02=[N], C-03=[N], C-04=[N], C-05=[N], C-06=[N], C-07=[N], C-08=[N], C-09=[N], C-10=[N], C-11=[N], C-12=[N]
Sum: [total]
Mean NPS: [sum / 12, to 2 decimal places]
Band distribution: Promoters (9–10): [count] | Passives (7–8): [count] | Detractors (1–6): [count]
Dominant Detractor objection: [most common blocking or major objection raised by Detractor-tier personas, with count]
Threshold: 7.0
Result: [PASS — aggregate NPS ≥ 7.0] or [FAIL — aggregate NPS < 7.0, spec needs revision]

**[CI BLOCK]**
CI Formula: ±1.96·(SD/√12)
SD: [population standard deviation of the 12 scores, to 4 decimal places]
Margin: 1.96 × [SD] / √12 = [computed margin, to 4 decimal places]
95% CI: ([mean − margin, to 2 dp], [mean + margin, to 2 dp])
Report as: "[mean] ± [margin] using formula ±1.96·[SD_value]/√12"

---

### Step 6 — Revision Directive (FAIL only)

Include this section only if aggregate NPS < 7.0.

**Revision Required:**

*Pass 1 — Per-persona targeted changes:*
For each persona scoring below 7.0, state the single highest-priority spec change referencing a named spec element. Blocking items take priority over major items.

*Pass 2 — Cross-persona prioritized summary:*
Top 3 revisions ranked by (personas affected × maximum severity). For each: issue, personas, cost tier (low-cost = copy/label/wording changes; high-cost = architecture or workflow changes), minimal spec change.

---

## V-03 — Lifecycle Emphasis (Directional Sensitivity Separation)

**Axis:** Lifecycle emphasis — explicit sensitivity analysis phase with directional separation
**Hypothesis:** Adding a dedicated sensitivity analysis phase that reports upward (+1) and downward (−1) score deltas for each high-influence persona as distinct lines — including explicit band-crossing detection per direction — satisfies A-28. A-20 is also satisfied as a side effect. The card section and CI enforcement are held constant (A-29 format only). A-16, A-17, A-21, A-24 are not addressed. The asymmetry between upward and downward swings is visible when a persona score sits at a band boundary (6/7 Detractor/Passive, 8/9 Passive/Promoter): a +1 move may cross a band while −1 stays within band, producing different narrative implications that a symmetric ±1 figure conceals.

---

You are simulating customer reactions to a spec before it ships. Twelve customer personas will evaluate the spec through their specific lens. Produce a complete signal-gathering report following the protocol below. All sections are required.

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

### Step 1 — Persona Feedback Cards

Generate one card per persona, C-01 through C-12 in sequence. Use the numbered field manifest below for every card. Omitting any numbered field constitutes an incomplete card.

**C-NN — [Persona Role]**

1. **Current approach:** What this persona does today without the spec's feature. Name the status-quo workflow or tool. If no equivalent exists, state that explicitly.

2. **NPS:** [integer 1–10] — [one sentence: compare what this persona gains or loses relative to their current approach; reference at least one named spec element]

3. **NPS band:** [Detractor (1–6) / Passive (7–8) / Promoter (9–10)]

4. **Feedback** (severity-first: blocking → major → minor → cosmetic):
   - [blocking] [item] — *cannot ship to this persona without resolving*
   - [major] [item] — *significant friction or missing value; reduces adoption*
   - [minor] [item] — *irritant; manageable workaround exists*
   - [cosmetic] [item] — *polish issue; no functional impact*
   *(If no objections: state "No objections from this lens.")*

5. **Revision recommendation:** One sentence naming the specific spec change — referencing a named spec element — that would most improve this persona's NPS.

---

### Step 2 — Blocker Escalation

**Blockers Requiring Resolution:**

Aggregate every `blocking` severity item from all 12 cards:
- C-NN: [description]

State "None identified" if no blocking items exist.

---

### Step 3 — Cross-Persona Theme Matrix

| Theme | Personas | Peak Severity | Severity Pattern | Recommended Action |
|-------|----------|---------------|-----------------|-------------------|

Identify at minimum one theme. Order themes descending by peak severity.

---

### Step 4 — Professional Lens Synthesis

**Role ordering and rationale (stated here, at the ordering instruction):** The UX Read runs before the PM Read. Failure mode prevented: if PM Read preceded UX Read, commercial framing would anchor the usability assessment, causing UX-rooted rejection to be reframed as pricing objections rather than identified as UX failures. Running UX first ensures usability signals surface independently.

**UX Read (runs first):**
Synthesize usability and accessibility signals. 3 sentences: dominant usability risk, accessibility finding, what UX is working well.

**PM Read (runs second):**
Synthesize adoption, ROI, and purchase-intent signals. 3 sentences: primary adoption barrier, purchase intent driver, go-to-market objection.

**Convergence:**
One sentence: where do the UX and PM reads agree? Where do they diverge?

---

### Step 5 — Aggregate NPS

Compute aggregate NPS as the arithmetic mean of the 12 persona NPS scores. Both blocks below are required. A [CI BLOCK] that omits the formula notation ±1.96·[SD_value]/√12 fails output validation.

**[SCORE BLOCK]**
Persona scores: C-01=[N], C-02=[N], C-03=[N], C-04=[N], C-05=[N], C-06=[N], C-07=[N], C-08=[N], C-09=[N], C-10=[N], C-11=[N], C-12=[N]
Sum: [total]
Mean NPS: [sum / 12, to 2 decimal places]
Band distribution: Promoters (9–10): [count] | Passives (7–8): [count] | Detractors (1–6): [count]
Dominant Detractor objection: [most common blocking or major objection raised by Detractor-tier personas, with count]
Threshold: 7.0
Result: [PASS — aggregate NPS ≥ 7.0] or [FAIL — aggregate NPS < 7.0, spec needs revision]

**[CI BLOCK]**
CI Formula: ±1.96·(SD/√12)
SD: [population standard deviation of the 12 scores, to 4 decimal places]
Margin: 1.96 × [SD] / √12 = [computed margin, to 4 decimal places]
95% CI: ([mean − margin, to 2 dp], [mean + margin, to 2 dp])
Report as: "[mean] ± [margin] using formula ±1.96·[SD_value]/√12"

---

### Step 6 — Sensitivity Analysis

Identify the 2–3 personas whose NPS scores have the highest absolute deviation from the aggregate mean. These are the high-influence personas.

For each high-influence persona, report **directionally separated** score deltas. Upward and downward effects must be reported as distinct lines. A symmetric ±delta figure without directional separation does not satisfy this section.

**[C-NN — Persona Role]**
- Current score: [X] | Aggregate mean: [mean to 2 dp] | Deviation: [X − mean = delta to 2 dp]
- **Upward delta (+1):** If C-NN score → [X+1], new aggregate mean = [computed to 2 dp] (Δ = +[1/12 to 3 dp])
  - Band crossing? [Yes: [X] was [band], [X+1] is [new band] — or No: score stays in [band]]
- **Downward delta (−1):** If C-NN score → [X−1], new aggregate mean = [computed to 2 dp] (Δ = −[1/12 to 3 dp])
  - Band crossing? [Yes: [X] was [band], [X−1] is [new band] — or No: score stays in [band]]
- **Asymmetry note:** One sentence describing whether the upward and downward swings have different narrative implications (e.g., one crosses a band threshold and the other does not).

NPS band thresholds for band-crossing detection: Detractor/Passive boundary at 6/7; Passive/Promoter boundary at 8/9.

---

### Step 7 — Revision Directive (FAIL only)

Include this section only if aggregate NPS < 7.0.

**Revision Required:**

*Pass 1 — Per-persona targeted changes:*
For each persona scoring below 7.0, state the single highest-priority spec change referencing a named spec element. Blocking items take priority.

*Pass 2 — Cross-persona prioritized summary:*
Top 3 revisions ranked by (personas affected × maximum severity). For each: issue, personas, cost tier (low-cost = copy/label/wording; high-cost = architecture or workflow), minimal spec change.

---

## V-04 — Combination: Full Inertia Chain

**Axis:** Combination (output format — structured sub-fields + conjunctive bilateral fields + sub-field cross-reference)
**Hypothesis:** The full inertia chain — A-16 (structured 4-sub-field baseline in Field 1) → A-21 (Gains [Field 2] names Losses [Field 3] as complement, and vice versa) → A-17 (explicit bilateral completeness rule prohibiting completion of either without the other) → A-24 (each of Fields 2/3 names a specific Field 1 sub-field by its defined label) — makes bilateral coverage structurally enforced rather than instructionally implied. A-24 adds the third enforcement layer: the evaluator cannot complete the gains or losses field without suppressing a named Step 0 sub-field reference, making omission of either side structurally detectable. A-28 (directional sensitivity) is not addressed. A-30/A-31 not targeted (CI at output-format level only).

---

You are simulating customer reactions to a spec before it ships. Twelve customer personas will evaluate the spec through their specific lens. This protocol uses a structured inertia baseline with conjunctive bilateral gains/losses field instructions. Produce a complete signal-gathering report following the protocol below. All sections are required.

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

### Step 1 — Persona Feedback Cards

Generate one card per persona, C-01 through C-12 in sequence. Use the numbered field manifest below for every card. Omitting any numbered field constitutes an incomplete card.

**C-NN — [Persona Role]**

1. **Current approach:**
   - **What it delivers:** Name the status-quo tool or workflow and what it provides this persona today.
   - **Where it falls short:** The specific gap or limitation the current approach does not address for this persona.
   - **Floor-level switching cost:** The minimum friction this persona bears when switching away from their current approach.
   - **Persona-specific workflow disruption:** How adoption of the spec's feature would disrupt this persona's specific daily workflow, beyond the general switching cost.

2. **Gains from this spec** (this field requires a corresponding entry in **Losses and switching costs** [Field 3] — completing Field 2 without Field 3 constitutes bilateral coverage failure; draw from the **"Where it falls short"** sub-field in Field 1 to anchor the gain claim): One sentence naming what this persona gains from the spec relative to their current approach. Reference at least one named spec element AND the "Where it falls short" gap identified above.

3. **Losses and switching costs** (this field requires a corresponding entry in **Gains from this spec** [Field 2] — completing Field 3 without Field 2 constitutes bilateral coverage failure; draw from the **"Floor-level switching cost"** and **"Persona-specific workflow disruption"** sub-fields in Field 1 to anchor the cost claim): One sentence naming what this persona gives up or bears when adopting. Reference the "Floor-level switching cost" or "Persona-specific workflow disruption" identified above. Neither Field 2 nor Field 3 is complete without the other.

4. **NPS:** [integer 1–10] — [one sentence synthesizing Fields 2 and 3 into a net score; reference at least one named spec element]

5. **NPS band:** [Detractor (1–6) / Passive (7–8) / Promoter (9–10)]

6. **Feedback** (severity-first: blocking → major → minor → cosmetic):
   - [blocking] [item] — *cannot ship to this persona without resolving*
   - [major] [item] — *significant friction or missing value; reduces adoption*
   - [minor] [item] — *irritant; manageable workaround exists*
   - [cosmetic] [item] — *polish issue; no functional impact*
   *(If no objections: state "No objections from this lens.")*

7. **Willingness to adopt:** [percentage or Low/Medium/High]. Clears adoption threshold (≥60%): [Yes/No].

8. **Revision recommendation:** One sentence naming the specific spec change — referencing a named spec element — that would most improve this persona's NPS.

---

### Step 2 — Blocker Escalation

**Blockers Requiring Resolution:**

Aggregate every `blocking` severity item from all 12 cards:
- C-NN: [description]

State "None identified" if no blocking items exist.

---

### Step 3 — Cross-Persona Theme Matrix

| Theme | Personas | Peak Severity | Severity Pattern | Recommended Action |
|-------|----------|---------------|-----------------|-------------------|

Identify at minimum one theme. Order themes descending by peak severity. Each row must include a severity pattern annotation.

---

### Step 4 — Professional Lens Synthesis

**Role ordering and rationale (stated here, at the ordering instruction):** The UX Read runs before the PM Read. Failure mode prevented: if PM Read preceded UX Read, commercial framing would anchor the usability assessment, causing UX-rooted rejection to be reframed as pricing objections rather than identified as UX failures. A reader following this ordering instruction encounters both the constraint and its epistemic grounding in a single pass.

**UX Read (runs first):**
Synthesize usability and accessibility signals from the 12 persona cards. 3 sentences: dominant usability risk, accessibility finding, what UX is working well.

**PM Read (runs second):**
Synthesize adoption, ROI, and purchase-intent signals. 3 sentences: primary adoption barrier, purchase intent driver, go-to-market objection.

**Convergence:**
One sentence: where do the UX and PM reads agree? Where do they diverge?

---

### Step 5 — Aggregate NPS

Compute aggregate NPS as the arithmetic mean of the 12 persona NPS scores. Both blocks below are required. A [CI BLOCK] that omits the formula notation ±1.96·[SD_value]/√12 fails output validation.

**[SCORE BLOCK]**
Persona scores: C-01=[N], C-02=[N], C-03=[N], C-04=[N], C-05=[N], C-06=[N], C-07=[N], C-08=[N], C-09=[N], C-10=[N], C-11=[N], C-12=[N]
Sum: [total]
Mean NPS: [sum / 12, to 2 decimal places]
Band distribution: Promoters (9–10): [count] | Passives (7–8): [count] | Detractors (1–6): [count]
Dominant Detractor objection: [most common blocking or major objection raised by Detractor-tier personas, with count]
Threshold: 7.0
Result: [PASS — aggregate NPS ≥ 7.0] or [FAIL — aggregate NPS < 7.0, spec needs revision]

**[CI BLOCK]**
CI Formula: ±1.96·(SD/√12)
SD: [population standard deviation of the 12 scores, to 4 decimal places]
Margin: 1.96 × [SD] / √12 = [computed margin, to 4 decimal places]
95% CI: ([mean − margin, to 2 dp], [mean + margin, to 2 dp])
Report as: "[mean] ± [margin] using formula ±1.96·[SD_value]/√12"

---

### Step 6 — Revision Directive (FAIL only)

Include this section only if aggregate NPS < 7.0.

**Revision Required:**

*Pass 1 — Per-persona targeted changes:*
For each persona scoring below 7.0, state the single highest-priority spec change referencing a named spec element. Blocking items take priority over major items.

*Pass 2 — Cross-persona prioritized summary:*
Top 3 revisions ranked by (personas affected × maximum severity). For each: issue, personas, cost tier (low-cost = copy/label/wording; high-cost = architecture or workflow), minimal spec change.

---

## V-05 — Combination: Full Stack

**Axis:** Combination (R19 V-05 derivation base + inertia chain + directional sensitivity)
**Hypothesis:** Layering the proven R19 V-05 base (A-29 + A-30 + A-31: derivation-phase CI with co-located failure mode) with the full inertia chain from V-04 (A-16 + A-17 + A-21 + A-24) and directional sensitivity separation (A-28) produces a protocol where every major structural constraint has: (1) process-level or structural enforcement, (2) bilateral grounding where applicable, and (3) co-located failure mode annotation. The inertia chain's gains/losses fields gain the same principled constraint property that A-25/A-31 established for role ordering and CI formula: a constraint that names the sub-field dependency cannot be satisfied without the referenced sub-field, and the failure mode annotation ensures the constraint cannot be reversed without contradiction. The directional sensitivity phase makes asymmetric band-crossing effects visible as distinct narrative signals rather than concealed in a symmetric ±figure.

---

You are simulating customer reactions to a spec before it ships. Twelve customer personas will evaluate the spec through their specific lens. This protocol uses a structured inertia baseline, conjunctive bilateral gains/losses field instructions, a derivation-phase CI computation with co-located failure mode annotation, and a directional sensitivity analysis. All sections are required.

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

For each persona C-01 through C-12, produce a card using the numbered field manifest below. All numbered fields are required. Omitting any numbered field constitutes an incomplete card.

**C-NN — [Persona Role]**

1. **Current approach:**
   - **What it delivers:** Name the status-quo tool or workflow and what it provides this persona today.
   - **Where it falls short:** The specific gap or limitation the current approach does not address for this persona.
   - **Floor-level switching cost:** The minimum friction this persona bears when switching away from their current approach.
   - **Persona-specific workflow disruption:** How adoption would disrupt this persona's specific daily workflow, beyond the general switching cost.

2. **Gains from this spec** (this field requires a corresponding entry in **Losses and switching costs** [Field 3] — completing Field 2 without Field 3 constitutes bilateral coverage failure; draw from the **"Where it falls short"** sub-field in Field 1 to anchor the gain): One sentence naming what this persona gains from the spec relative to their current approach, drawing from the "Where it falls short" gap. Reference at least one named spec element.

3. **Losses and switching costs** (this field requires a corresponding entry in **Gains from this spec** [Field 2] — completing Field 3 without Field 2 constitutes bilateral coverage failure; draw from the **"Floor-level switching cost"** and **"Persona-specific workflow disruption"** sub-fields in Field 1 to anchor the cost): One sentence naming what this persona gives up or bears when adopting, drawing from the "Floor-level switching cost" or "Persona-specific workflow disruption." Neither Field 2 nor Field 3 is complete without the other.

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

**Role ordering and failure mode (stated here, at the ordering instruction):** The UX Read runs before the PM Read. Failure mode prevented by this ordering: if the PM Read preceded the UX Read, commercial framing — ROI arguments, procurement fit, adoption projections — would anchor the usability assessment, causing UX-rooted rejection to be reframed as pricing or positioning objections rather than identified as UX failures. A reader following this ordering instruction encounters both the constraint (UX first) and its epistemic grounding (PM framing anchors UX if reversed) in a single pass, making the sequence a principled constraint rather than an arbitrary choice.

**UX Read (runs first):**
Synthesize usability and accessibility signals from the 12 persona cards. 3 sentences: dominant usability risk, accessibility finding, what UX is working well.

**PM Read (runs second):**
Synthesize adoption, ROI, and purchase-intent signals. 3 sentences: primary adoption barrier, purchase intent driver, go-to-market objection.

**Convergence:**
One sentence: where do the UX and PM reads agree? Where do they diverge?

---

### Section 5 — Aggregate NPS

#### S.1 — Derivation Phase

Execute steps D.1 through D.4 in sequence. Each step is a phase exit condition — the next step cannot begin until the current step is complete. A CI report produced without completing D.1 first cannot satisfy the formula requirement by adding the parenthetical after the fact. The formula must be an input to the computation, not a decoration on the output.

**D.1 — State formula and failure mode (required before D.2 can begin)**

State the CI formula before any score collection or computation proceeds:

> CI formula: Mean ± 1.96·(SD/√12), where n = 12 personas and SD is the population standard deviation of the 12 NPS scores.
>
> Failure mode this formula requirement prevents: Without the formula parenthetical (±1.96·[SD_value]/√12) alongside the reported interval, the CI annotation cannot be verified against different score inputs — a reader cannot confirm whether the interval was computed as ±1.96·SD/√12 or via a different method. The formula must appear co-located with the CI value so that any reader following this step encounters both the rule and its verification basis in a single pass. An output that reports a CI interval without the formula parenthetical fails D.1 validation regardless of whether the interval bounds are numerically correct.

D.2 cannot begin until D.1 is stated, including both the formula and the failure mode annotation above.

**D.2 — Score collection and mean**

List all 12 scores:
C-01=[N], C-02=[N], C-03=[N], C-04=[N], C-05=[N], C-06=[N],
C-07=[N], C-08=[N], C-09=[N], C-10=[N], C-11=[N], C-12=[N]

Sum: [total]
Mean NPS: [sum / 12, to 2 decimal places]

Band distribution: Promoters (9–10): [count] | Passives (7–8): [count] | Detractors (1–6): [count]
Dominant Detractor objection: [most common blocking or major objection among Detractor-tier personas, with count of personas citing it]

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
Verdict: **PASS** — aggregate NPS ≥ 7.0, spec ready for development | **FAIL** — aggregate NPS < 7.0, spec needs revision before proceeding

---

### Section 6 — Sensitivity Analysis

Identify the 2–3 personas whose NPS scores have the highest absolute deviation from the aggregate mean. These are the high-influence personas.

For each high-influence persona, report **directionally separated** score deltas. Upward (+1) and downward (−1) effects must be reported as distinct lines. A symmetric ±delta figure without directional separation does not satisfy this section — the upward and downward effects are reported as independent findings because NPS band crossings are asymmetrically distributed around the current score: a +1 move may cross a band threshold while a −1 move stays within band, producing different narrative implications.

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
For each persona scoring below 7.0, state the single highest-priority spec change referencing a named spec element. Blocking items take priority over major items.

*Pass 2 — Cross-persona prioritized summary:*
Top 3 revisions ranked by (number of personas affected × maximum severity). For each revision:
- Issue: [description]
- Personas affected: [list]
- Cost tier: low-cost (copy/label/wording changes) or high-cost (architecture or workflow changes)
- Minimal spec change: [description]
