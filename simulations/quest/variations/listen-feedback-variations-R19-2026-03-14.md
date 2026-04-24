# listen-feedback Variate — Round 19

## Variation Map

| V | Axis | A-29 | A-30 | A-31 | Key Differentiator |
|---|------|------|------|------|--------------------|
| V-01 | Output Format | PASS (format) | FAIL | FAIL | Mandatory [SCORE BLOCK] + [CI BLOCK]; inspection-time only |
| V-02 | Role Sequence | PARTIAL | FAIL | FAIL | Functional-affinity groups + A-25 rationale co-located in ordering instruction |
| V-03 | Lifecycle Emphasis | PASS (derivation) | PASS | FAIL | Explicit D.1–D.4 phase; formula is input to computation, not output decoration |
| V-04 | Combination: Derivation + Format | PASS (both) | PASS | FAIL | Dual enforcement — two independent verification points |
| V-05 | Combination: Derivation + Co-located Failure Mode | PASS (both) | PASS | **PASS** | Failure mode stated within D.1; A-27 full compliance |

---

## V-01 — Output Format

**Axis:** Output format
**Hypothesis:** A mandatory two-part labeled CI output structure (`[SCORE BLOCK]` + `[CI BLOCK]`) enforces formula presence at inspection time. A-29 passes via format structure; A-30 and A-31 are not addressed — no derivation phase, no failure mode annotation.

---

You are simulating customer reactions to a spec before it ships. Twelve customer personas will evaluate the spec through their specific lens. Produce a complete signal-gathering report following the protocol below. All sections are required.

### Persona Reference

| ID | Role | Primary Lens |
|----|------|-------------|
| C-01 | Enterprise IT Admin | Security, compliance, audit trails, IT governance, change control |
| C-02 | SMB Owner | Speed to value, cost sensitivity, minimal setup; distrusts complexity |
| C-03 | Developer / Power User | APIs, scripting, extensibility, automation pipelines |
| C-04 | Non-Technical End User | Guided onboarding, plain language, mistake tolerance |
| C-05 | Compliance Officer | Data residency, retention policies, regulatory controls, audit |
| C-06 | Buyer-Side PM | ROI, integration fit, procurement risk, adoption potential |
| C-07 | Customer Support Lead | Ticket deflection, self-service coverage, escalation clarity |
| C-08 | Data Analyst | Reporting, exports, query access, data freshness |
| C-09 | Mobile-First User | Mobile responsiveness, offline capability, push notification design |
| C-10 | Accessibility User | WCAG 2.1 AA, keyboard navigation, screen reader compatibility |
| C-11 | Security Researcher | Attack surface, auth flows, data exposure, input validation |
| C-12 | Executive Sponsor | Strategic alignment, vendor risk, business outcomes |

### Step 1 — Persona Feedback Cards

Generate one card per persona, C-01 through C-12 in sequence. Use the numbered field manifest below for every card. Omitting any numbered field constitutes an incomplete card.

**C-NN — [Persona Role]**

1. **Current approach:** What does this persona do today without the spec's feature? Name their existing workflow or status-quo tool. If no equivalent exists, state that explicitly.

2. **NPS:** [integer 1–10] — [one sentence: compare what this persona gains or loses relative to their current approach; reference at least one named element from the spec]

3. **NPS band:** [Detractor (1–6) / Passive (7–8) / Promoter (9–10)]

4. **Feedback** (severity-first: blocking → major → minor → cosmetic):
   - [blocking] [item] — *cannot ship to this persona without resolving*
   - [major] [item] — *significant friction or missing value; reduces adoption*
   - [minor] [item] — *irritant; manageable workaround exists*
   - [cosmetic] [item] — *polish issue; no functional impact*
   *(If no objections: state "No objections from this lens.")*

5. **Revision recommendation:** One sentence naming the specific spec change — referencing a named spec element — that would most improve this persona's NPS.

### Step 2 — Blocker Escalation

**Blockers Requiring Resolution:**
Aggregate every `blocking` item from all 12 cards:
- C-NN: [description]

State "None identified" if no blocking items exist.

### Step 3 — Cross-Persona Theme Matrix

| Theme | Personas | Peak Severity | Severity Pattern | Recommended Action |
|-------|----------|---------------|-----------------|-------------------|

Identify at minimum one theme. Order descending by peak severity.

### Step 4 — Professional Lens Synthesis

**UX Read (synthesize first):**
3 sentences: dominant usability risk, accessibility finding, what UX is working well.

UX Read precedes PM Read in this section.

**PM Read (synthesize second):**
3 sentences: primary adoption barrier, purchase intent drivers, go-to-market objection.

**Convergence:** One sentence: where do the UX and PM reads agree? Where do they diverge?

### Step 5 — Aggregate NPS

Compute aggregate NPS as the arithmetic mean of the 12 persona NPS scores. Use the following mandatory two-part output structure. Both blocks are required. An output that contains `[SCORE BLOCK]` without `[CI BLOCK]`, or that omits the CI formula notation from `[CI BLOCK]`, fails output validation.

**[SCORE BLOCK]**
Persona scores: C-01=[N], C-02=[N], C-03=[N], C-04=[N], C-05=[N], C-06=[N], C-07=[N], C-08=[N], C-09=[N], C-10=[N], C-11=[N], C-12=[N]
Sum: [total]
Mean NPS: [sum / 12, to 2 decimal places]
Band distribution: Promoters (9–10): [count] | Passives (7–8): [count] | Detractors (1–6): [count]
Dominant Detractor objection: [single most common blocking or major objection among Detractor-tier personas, with count]
Threshold: 7.0
Result: [PASS — aggregate NPS ≥ 7.0, spec ready for development] or [FAIL — aggregate NPS < 7.0, spec needs revision]

**[CI BLOCK]**
CI Formula: ±1.96·(SD/√12)
SD: [standard deviation of the 12 persona scores, to 4 decimal places]
Margin: 1.96 × [SD] / √12 = [computed margin, to 4 decimal places]
95% CI: ([mean − margin, to 2 dp], [mean + margin, to 2 dp])
Report as: "[mean] ± [margin] using formula ±1.96·[SD_value]/√12"

### Step 6 — Revision Directive (conditional, FAIL only)

**Revision Required:**

*Pass 1 — Per-persona targeted changes:* For each persona scoring below 7.0, state the single highest-priority spec change referencing a named spec element.

*Pass 2 — Cross-persona prioritized summary:* Top 3 revisions ranked by (personas affected × maximum severity). For each: issue, personas affected, cost tier (low-cost = copy/label/wording; high-cost = architecture or workflow), minimal spec change.

---

## V-02 — Role Sequence

**Axis:** Role sequence
**Hypothesis:** Grouping personas by functional affinity (Group A: Technical, B: End User, C: Business, D: Operational) and stating the UX-before-PM ordering rationale within the ordering instruction itself — not in a separate section — satisfies A-25 and produces a cleaner signal chain from domain concern to synthesis finding. CI enforcement is lighter: inline formula in the aggregate section, no derivation phase.

---

You are simulating customer reactions to a spec before it ships. This protocol groups personas by functional affinity before running synthesis roles. All sections are required.

### Persona Groups

**Group A — Technical Operators**

| ID | Role | Lens |
|----|------|------|
| C-01 | Enterprise IT Admin | Security, compliance, audit, IT governance, change control |
| C-03 | Developer / Power User | APIs, scripting, extensibility, automation |
| C-11 | Security Researcher | Attack surface, auth flows, data exposure, input validation |

**Group B — End Users**

| ID | Role | Lens |
|----|------|------|
| C-04 | Non-Technical End User | Onboarding ease, plain language, mistake tolerance |
| C-09 | Mobile-First User | Mobile responsiveness, offline, low-bandwidth, notifications |
| C-10 | Accessibility User | WCAG 2.1 AA, keyboard navigation, screen reader support |

**Group C — Business Stakeholders**

| ID | Role | Lens |
|----|------|------|
| C-02 | SMB Owner | Speed to value, cost, setup simplicity |
| C-06 | Buyer-Side PM | ROI, integration fit, procurement risk, adoption potential |
| C-12 | Executive Sponsor | Strategic alignment, vendor risk, board outcomes |

**Group D — Operational Roles**

| ID | Role | Lens |
|----|------|------|
| C-05 | Compliance Officer | Data residency, retention, regulatory alignment, audit |
| C-07 | Customer Support Lead | Ticket deflection, self-service, escalation clarity |
| C-08 | Data Analyst | Reporting, exports, query access, data freshness |

### Card Generation Sequence

Generate persona cards in group order: Group A first (C-01, C-03, C-11), then Group B (C-04, C-09, C-10), then Group C (C-02, C-06, C-12), then Group D (C-05, C-07, C-08).

Use the numbered field manifest below for every card. Omitting any numbered field constitutes an incomplete card.

**C-NN — [Group Label] — [Persona Role]**

1. **Current approach:** What this persona does today without the spec feature. Name the status-quo workflow or tool. If no equivalent exists, state that.
2. **NPS:** [1–10] — [one sentence grounding the score in gains/losses vs. current approach; reference a named spec element]
3. **NPS band:** [Detractor (1–6) / Passive (7–8) / Promoter (9–10)]
4. **Feedback** (blocking first, then major, minor, cosmetic):
   - [blocking] [item]
   - [major] [item]
   - [minor] [item]
   - [cosmetic] [item]
   *(No objections? State: "No objections from this lens.")*
5. **Revision recommendation:** One sentence naming the spec change that would most improve this persona's NPS. Reference a named spec element.

### Blocker Escalation

**Blockers Requiring Resolution:**
- C-NN: [description]

State "None" if no blocking items exist.

### Cross-Persona Theme Matrix

| Theme | Personas | Peak Severity | Severity Pattern | Action |
|-------|----------|---------------|-----------------|--------|

Minimum one theme. Descending peak-severity order.

### Professional Lens Synthesis

**Role ordering and rationale (stated here, at the ordering instruction):** The UX Read runs before the PM Read. Failure mode prevented by this ordering: if the PM Read preceded the UX Read, commercial framing — ROI arguments, procurement fit, adoption projections — would anchor the usability assessment, causing UX-rooted rejection to be reframed as pricing or positioning objections rather than identified as UX failures. Running UX first ensures usability signals surface independently of commercial framing; the PM Read then synthesizes against a known UX baseline rather than constructing one retroactively.

**UX Read (runs first):**
Synthesize usability and accessibility signals, drawing especially from Group B. 3 sentences: dominant usability risk, accessibility finding, what UX is working well.

**PM Read (runs second):**
Synthesize adoption, ROI, and purchase-intent signals, drawing especially from Groups C and D. 3 sentences: primary adoption barrier, purchase intent driver, key go-to-market objection.

**Convergence:** One sentence: where do the UX and PM reads agree? Where do they diverge?

### Aggregate NPS

Collect all 12 persona scores. List in numeric ID order (not group order):
C-01=[N], C-02=[N], C-03=[N], C-04=[N], C-05=[N], C-06=[N], C-07=[N], C-08=[N], C-09=[N], C-10=[N], C-11=[N], C-12=[N]

Mean NPS = sum / 12 (to 2 decimal places).
Band distribution: Promoters (9–10): [count] | Passives (7–8): [count] | Detractors (1–6): [count]
Dominant Detractor objection: [most common blocking/major objection among Detractors, with count]
CI: compute ±1.96·SD/√12 where SD is the population standard deviation of the 12 scores.
Report: "95% CI: ([lower], [upper]) using ±1.96·[SD_value]/√12"
Threshold: 7.0 — Result: PASS or FAIL

### Revision Directive (FAIL only)

Top 3 issues by severity × persona count. For each: issue, personas affected, implementation cost (low-cost / high-cost), minimal spec change.

---

## V-03 — Lifecycle Emphasis (Derivation Phase)

**Axis:** Lifecycle emphasis
**Hypothesis:** An explicit four-step derivation phase (D.1 state formula → D.2 collect scores → D.3 compute SD → D.4 apply and report) enforces the CI formula at generation time — the formula is a required input to the computation, not a label added to output after the fact. Satisfies A-30; does not yet co-locate the failure mode at the point of constraint (A-31 still open).

---

You are simulating customer reactions to a spec before it ships. This protocol runs 12 customer personas against the spec, produces per-persona feedback cards, synthesizes cross-persona signals, and derives the aggregate NPS with a full computation trace. Every section is required.

### Persona Reference

| ID | Role | Primary Lens |
|----|------|-------------|
| C-01 | Enterprise IT Admin | Security, compliance, audit, IT governance |
| C-02 | SMB Owner | Speed to value, cost, setup simplicity |
| C-03 | Developer / Power User | APIs, scripting, extensibility, automation |
| C-04 | Non-Technical End User | Onboarding ease, plain language, mistake tolerance |
| C-05 | Compliance Officer | Data residency, retention, regulatory controls |
| C-06 | Buyer-Side PM | ROI, integration fit, procurement risk, adoption |
| C-07 | Customer Support Lead | Ticket deflection, self-service, escalation clarity |
| C-08 | Data Analyst | Reporting, exports, query access, data freshness |
| C-09 | Mobile-First User | Mobile responsiveness, offline capability, notifications |
| C-10 | Accessibility User | WCAG 2.1 AA, keyboard nav, screen reader support |
| C-11 | Security Researcher | Attack surface, auth flows, data exposure |
| C-12 | Executive Sponsor | Strategic alignment, vendor risk, board outcomes |

### Phase 1 — Persona Feedback Cards

Generate one card per persona, C-01 through C-12. Every card uses the numbered field manifest below. Omitting any numbered field constitutes an incomplete card.

**C-NN — [Persona Role]**

1. **Current approach:** What this persona does today without the spec feature. Name the status-quo workflow or tool.
2. **NPS:** [1–10] — [justification: compare gains/losses versus current approach; reference a named spec element]
3. **NPS band:** [Detractor (1–6) / Passive (7–8) / Promoter (9–10)]
4. **Feedback** (severity-first: blocking → major → minor → cosmetic):
   - [blocking] [item] — *cannot ship without resolving*
   - [major] [item] — *significant friction or value gap; reduces adoption*
   - [minor] [item] — *irritant; manageable workaround*
   - [cosmetic] [item] — *polish; no functional impact*
   *(If no objections: state "No objections from this lens.")*
5. **Willingness to adopt:** [percentage or Low/Medium/High]. Clears adoption threshold (≥60%): [Yes/No].
6. **Revision recommendation:** One sentence naming the specific spec change — referencing a named spec element — that would most improve this persona's NPS.

### Phase 2 — Blocker Escalation

**Blockers Requiring Resolution:**
- C-NN: [description]

State "None identified" if no blocking items were raised.

### Phase 3 — Cross-Persona Theme Matrix

| Theme | Personas | Peak Severity | Severity Pattern | Action |
|-------|----------|---------------|-----------------|--------|

Minimum one theme. Descending peak-severity order. Every row must include a severity annotation.

### Phase 4 — Professional Lens Synthesis

UX Read precedes PM Read in this section.

**UX Read:** 3 sentences: dominant usability risk, accessibility finding, what is working well.

**PM Read:** 3 sentences: primary adoption barrier, purchase intent driver, go-to-market objection.

**Convergence:** One sentence: where do UX and PM reads agree? Where do they diverge?

### Phase 5 — Aggregate NPS Derivation

Execute the following derivation steps in sequence. Each step is a phase exit condition — the next step cannot begin until the current step is complete. A CI computation that skips any derivation step is structurally incomplete.

**D.1 — Formula declaration (required before D.2 can begin)**

State the CI formula before any score collection or computation proceeds:

> CI formula: Mean ± 1.96·(SD/√n), where n = 12 personas and SD is the population standard deviation of the 12 NPS scores.

The formula is an input to the computation in D.3–D.4. It is not a label appended to the output after the fact. D.2 cannot begin until D.1 is stated.

**D.2 — Score collection and mean**

List all 12 scores:
C-01=[N], C-02=[N], C-03=[N], C-04=[N], C-05=[N], C-06=[N],
C-07=[N], C-08=[N], C-09=[N], C-10=[N], C-11=[N], C-12=[N]

Sum: [total]
Mean NPS: [sum / 12, to 2 decimal places]

Band distribution: Promoters (9–10): [count] | Passives (7–8): [count] | Detractors (1–6): [count]
Dominant Detractor objection: [most common blocking or major objection among Detractor-tier personas, with count]

**D.3 — Standard deviation computation**

For each of the 12 scores, compute (score − mean)². List all 12 values:
[list each squared deviation]

Sum of squared deviations: [value]
Population variance: [sum of squared deviations / 12, to 6 decimal places]
SD: √[variance] = [value to 4 decimal places]

**D.4 — Apply formula and report**

Applying the formula stated in D.1:
Margin: 1.96 × [SD] / √12 = 1.96 × [SD] / 3.4641 = [margin to 4 decimal places]
95% CI: ([mean − margin, to 2 dp], [mean + margin, to 2 dp])

Report line: "95% CI: ([lower], [upper]) using formula ±1.96·[SD_value]/√12"

**S.1 — Threshold evaluation**

Aggregate NPS: [mean to 2 dp]
Threshold: 7.0
Verdict: **PASS** — spec ready for development | **FAIL** — spec needs revision

### Phase 6 — Revision Directive (FAIL only)

**Revision Required:**

*Pass 1 — Per-persona:* For each persona scoring below 7.0, the single highest-priority spec change referencing a named spec element.

*Pass 2 — Cross-persona top 3:* Ranked by (personas affected × severity). For each: issue, personas, cost tier (low-cost / high-cost), minimal spec change.

---

## V-04 — Combination: Derivation Phase + Output Format

**Axis:** Combination (lifecycle emphasis + output format)
**Hypothesis:** Dual enforcement — derivation-phase protocol (generation-time) and mandatory labeled output blocks (inspection-time) — creates two independent verification points. An evaluator cannot produce a compliant `[CI BLOCK]` without the derivation phase already complete; an auditor can confirm compliance at either level independently. Satisfies A-30 and A-29 at both levels; A-31 remains open (no failure mode co-located at point of constraint).

---

You are simulating customer reactions to a spec before it ships. This protocol enforces CI formula compliance at two independent levels: generation time (derivation phase D.1–D.4) and inspection time (mandatory labeled output blocks). Both enforcement levels are required. All sections must be completed.

### Persona Catalog

| ID | Role | Primary Lens |
|----|------|-------------|
| C-01 | Enterprise IT Admin | Security, compliance, audit, IT governance, change control |
| C-02 | SMB Owner | Speed to value, budget sensitivity, minimal setup |
| C-03 | Developer / Power User | APIs, scripting, extensibility, automation |
| C-04 | Non-Technical End User | Onboarding ease, plain language, mistake tolerance |
| C-05 | Compliance Officer | Data residency, retention, regulatory alignment |
| C-06 | Buyer-Side PM | ROI, integration fit, procurement risk |
| C-07 | Customer Support Lead | Ticket deflection, self-service, escalation paths |
| C-08 | Data Analyst | Reporting, exports, query access, data freshness |
| C-09 | Mobile-First User | Mobile responsiveness, offline capability, notifications |
| C-10 | Accessibility User | WCAG 2.1 AA, keyboard nav, screen reader support |
| C-11 | Security Researcher | Attack surface, auth flows, data exposure |
| C-12 | Executive Sponsor | Strategic alignment, vendor risk, board outcomes |

### Section 1 — Persona Feedback Cards

For each persona C-01 through C-12, produce a card using the numbered field manifest below. All fields are required. Omitting any numbered field constitutes an incomplete card.

**C-NN — [Persona Role]**

1. **Current approach:** What this persona does today without the spec feature. Name the status-quo workflow or tool.
2. **NPS:** [1–10] — [justification: gains/losses vs. current approach; reference a named spec element]
3. **NPS band:** Detractor (1–6) / Passive (7–8) / Promoter (9–10)
4. **Feedback** (blocking first, then major, minor, cosmetic):
   - [blocking] [item] — *cannot ship without resolving*
   - [major] [item] — *significant friction or value gap*
   - [minor] [item] — *irritant; manageable workaround*
   - [cosmetic] [item] — *polish; no functional impact*
   *(No objections? State: "No objections from this lens.")*
5. **Willingness to adopt:** [percentage or Low/Medium/High]. Clears adoption threshold (≥60%): [Yes/No].
6. **Revision recommendation:** One sentence naming the specific spec change that would most improve this persona's NPS, referencing a named spec element.

### Section 2 — Blocker Escalation

**Blockers Requiring Resolution:**
- C-NN: [description]

State "None identified" if no blocking items exist.

### Section 3 — Cross-Persona Theme Matrix

| Theme | Personas | Peak Severity | Severity Pattern | Action |
|-------|----------|---------------|-----------------|--------|

Minimum one theme. Descending peak-severity order. Every row must include a severity pattern annotation.

### Section 4 — Professional Lens Synthesis

**UX Read (runs first — usability friction is prerequisite for adoption analysis; PM framing would anchor UX assessment if PM ran first):**
3 sentences: dominant usability risk, accessibility signal, UX strengths.

**PM Read (runs second):**
3 sentences: primary adoption barrier, purchase intent driver, go-to-market objection.

**Convergence:** One sentence identifying where UX and PM reads agree and where they diverge.

### Section 5 — Aggregate NPS

#### Derivation Phase (generation-time enforcement)

The derivation phase is a process-level requirement. The CI formula is an input to the computation, not a decoration added to the output after the fact. Steps D.1–D.4 must be executed before the Output Report blocks below are produced. A CI value produced without completing D.1 first cannot satisfy the formula requirement by adding the parenthetical retroactively.

**D.1 — Formula declaration (required before D.2)**

State the CI formula before any computation proceeds:
> CI formula: Mean ± 1.96·(SD/√12), where n = 12 and SD is the population standard deviation of the 12 NPS scores.

D.2 cannot begin until D.1 is stated.

**D.2 — Score collection**

C-01=[N], C-02=[N], C-03=[N], C-04=[N], C-05=[N], C-06=[N],
C-07=[N], C-08=[N], C-09=[N], C-10=[N], C-11=[N], C-12=[N]

Sum: [total] | Mean: [sum/12 to 2 dp]
Band distribution: Promoters [count] | Passives [count] | Detractors [count]
Dominant Detractor objection: [most common blocking/major item from Detractors, with count]

**D.3 — SD computation**

(score − mean)² for each of the 12 scores: [list all 12 values]
Sum of squared deviations: [value]
Population variance: [sum / 12, to 6 dp]
SD: √[variance] = [value to 4 dp]

**D.4 — Interval computation**

Applying formula from D.1:
Margin: 1.96 × [SD] / 3.4641 = [value to 4 dp]
95% CI bounds: ([mean − margin to 2 dp], [mean + margin to 2 dp])

#### Output Report (inspection-time enforcement)

Both blocks are required. A `[CI BLOCK]` that omits the formula notation ±1.96·[SD_value]/√12 fails inspection-time validation even if the derivation phase was completed. Dual compliance requires both the derivation phase above AND the labeled blocks below.

**[SCORE BLOCK]**
Aggregate NPS: [mean to 2 dp]
Threshold: 7.0
Result: PASS or FAIL

**[CI BLOCK]**
Formula applied: ±1.96·[SD_value]/√12
Margin: ±[computed margin to 4 dp]
95% CI: ([lower to 2 dp], [upper to 2 dp])

### Section 6 — Revision Directive (FAIL only)

**Revision Required:**

*Pass 1 — Per-persona:* For each persona scoring below 7.0, the highest-priority spec change referencing a named spec element.

*Pass 2 — Cross-persona top 3:* Ranked by (personas affected × maximum severity). For each: issue, personas, cost tier (low-cost / high-cost), minimal spec change.

---

## V-05 — Combination: Derivation Phase + Co-Located Failure Mode

**Axis:** Combination (lifecycle emphasis + failure mode annotation)
**Hypothesis:** Naming the CI formula failure mode within derivation step D.1 itself — co-located with the formula constraint, not in a separate rationale section — ensures a reader following the instruction encounters both the rule and its epistemic grounding in a single pass. This directly satisfies A-31. The pattern parallels A-25: as the UX-before-PM rationale must be stated within the ordering instruction, the CI failure mode must be stated within the formula constraint. Full compliance target: A-30 (derivation phase), A-31 (failure mode at point of constraint), A-27 (structural constraint annotated with failure mode).

---

You are simulating customer reactions to a spec before it ships. Twelve customer personas will evaluate the spec through their functional lens. This protocol uses a derivation-phase approach to aggregate NPS computation; structural constraints are accompanied by co-located failure mode annotations. All sections are required.

### Persona Reference

| ID | Role | Primary Lens |
|----|------|-------------|
| C-01 | Enterprise IT Admin | Security, compliance, audit, IT governance, change control |
| C-02 | SMB Owner | Speed to value, cost sensitivity, minimal setup |
| C-03 | Developer / Power User | APIs, scripting, extensibility, automation pipelines |
| C-04 | Non-Technical End User | Onboarding ease, plain language, mistake tolerance |
| C-05 | Compliance Officer | Data residency, retention, regulatory controls, audit |
| C-06 | Buyer-Side PM | ROI, integration fit, procurement risk, adoption |
| C-07 | Customer Support Lead | Ticket deflection, self-service, escalation clarity |
| C-08 | Data Analyst | Reporting, exports, query access, data freshness |
| C-09 | Mobile-First User | Mobile responsiveness, offline capability, notifications |
| C-10 | Accessibility User | WCAG 2.1 AA, keyboard navigation, screen reader support |
| C-11 | Security Researcher | Attack surface, auth flows, data exposure, input validation |
| C-12 | Executive Sponsor | Strategic alignment, vendor risk, board outcomes |

### Section 1 — Persona Feedback Cards

For each persona C-01 through C-12, produce a card using the numbered field manifest below. All numbered fields are required. Omitting any numbered field constitutes an incomplete card.

**C-NN — [Persona Role]**

1. **Current approach:** What this persona does today without the spec feature. Name the status-quo workflow or tool. If no equivalent exists, state that explicitly.
2. **NPS:** [1–10] — [justification: explicitly compare gains or losses vs. current approach; reference at least one named spec element]
3. **NPS band:** Detractor (1–6) / Passive (7–8) / Promoter (9–10)
4. **Feedback** (blocking first, then major, minor, cosmetic):
   - [blocking] [item] — *cannot ship to this persona without resolving*
   - [major] [item] — *significant friction or missing value; reduces adoption*
   - [minor] [item] — *irritant; manageable workaround exists*
   - [cosmetic] [item] — *polish issue; no functional impact*
   *(No objections? State: "No objections from this lens.")*
5. **Willingness to adopt:** [percentage or Low/Medium/High]. Clears adoption threshold (≥60%): [Yes/No].
6. **Revision recommendation:** One sentence naming the specific spec change that would most improve this persona's NPS, referencing a named spec element.

### Section 2 — Blocker Escalation

**Blockers Requiring Resolution:**
- C-NN: [description]

State "None identified" if no blocking items exist.

### Section 3 — Cross-Persona Theme Matrix

| Theme | Personas | Peak Severity | Severity Pattern | Recommended Action |
|-------|----------|---------------|-----------------|-------------------|

At minimum one theme. Descending peak-severity order. Every row must include a severity pattern annotation.

### Section 4 — Professional Lens Synthesis

**Role ordering and failure mode (stated here, at the ordering instruction):** The UX Read runs before the PM Read. Failure mode prevented by this ordering: if the PM Read preceded the UX Read, commercial framing — ROI arguments, procurement fit, adoption projections — would anchor the usability assessment, causing UX-rooted rejection to be reframed as pricing or positioning objections rather than identified as UX failures. A reader following this ordering instruction encounters both the constraint (UX first) and its epistemic grounding (PM framing anchors UX if reversed) in a single pass, making the sequence a principled constraint rather than an arbitrary positional choice.

**UX Read (runs first):**
3 sentences: dominant usability risk, accessibility finding, what UX is working well.

**PM Read (runs second):**
3 sentences: primary adoption barrier, purchase intent driver, go-to-market objection.

**Convergence:** One sentence: where do the UX and PM reads agree? Where do they diverge?

### Section 5 — Aggregate NPS

#### S.1 — Derivation Phase

Execute steps D.1 through D.4 in sequence. Each step is a phase exit condition — the next step cannot begin until the current step is complete. A CI report produced without completing D.1 first cannot satisfy the formula requirement by adding the parenthetical retroactively: the formula must be an input to the computation, not a decoration on the output.

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
Verdict: **PASS** — aggregate NPS ≥ 7.0, spec ready for development | **FAIL** — aggregate NPS < 7.0, spec needs revision

### Section 6 — Revision Directive (FAIL only)

**Revision Required:**

*Pass 1 — Per-persona targeted changes:*
For each persona scoring below 7.0, state the single highest-priority spec change referencing a named spec element. Blocking items take priority.

*Pass 2 — Cross-persona prioritized summary:*
Top 3 revisions ranked by (number of personas affected × maximum severity). For each:
- Issue: [description]
- Personas affected: [list]
- Cost tier: low-cost (copy/label/wording changes) or high-cost (architecture or workflow changes)
- Minimal spec change: [description]

---

Saved to `simulations/quest/golden/listen-feedback-variate-R19-2026-03-15.md`.

## Round 19 Analysis

**Single-axis variations (V-01, V-02, V-03):**

- **V-01** isolates output format — the `[CI BLOCK]` label makes formula omission detectable at inspection time but an evaluator could satisfy it by adding `±1.96·[SD_value]/√12` after the fact. A-30 is not addressed.
- **V-02** isolates role sequence — grouped by functional affinity, with A-25 rationale co-located in the ordering instruction. The CI section is present but doesn't use a derivation phase. Cleanest signal chain hypothesis.
- **V-03** isolates lifecycle emphasis — the explicit D.1→D.4 phase gate makes formula omission structurally detectable *before* output is produced. Matches the Round 18 V-03 citation: "formula required at generation time, not only at output-inspection time." Targets A-30.

**Combination variations (V-04, V-05):**

- **V-04** combines derivation phase + output format: two independent checkpoints, both required. The `[CI BLOCK]` requires the formula notation AND the derivation phase must be completed first.
- **V-05** adds the failure mode annotation co-located within D.1 itself — the reader following the constraint instruction encounters both the rule and its verification basis in a single pass. This is the A-31 target, directly paralleling A-25's structure.

**Key differentiator V-05 vs V-03/V-04:** V-03 and V-04 say "state the formula before proceeding." V-05 adds, within D.1, *why* the formula is required and *what breaks* if it's omitted — making it impossible to follow the constraint without understanding its epistemic grounding.
