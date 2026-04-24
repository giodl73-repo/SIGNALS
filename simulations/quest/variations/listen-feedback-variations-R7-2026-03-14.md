## listen-feedback Variations — Round 7 (V-01 through V-05)

---

### V-01 — Single axis: Role sequence
**Axis**: UX READ runs before the 12 persona cards; PM READ closes the simulation as final synthesis before the theme matrix  
**Hypothesis**: Opening with the UX design lens primes the subsequent persona reads to surface craft-quality friction (not just functional gaps); closing with PM READ before the theme matrix produces a richer cross-persona synthesis because both professional frames are visible when themes are drawn

---

```markdown
You are running a customer feedback simulation for a spec or design artifact.

## Inputs

- `{{spec}}` — the spec, design doc, or feature description under review
- `{{topic}}` — the feature name or topic label

## Execution Order

Run in this exact sequence:
1. UX READ
2. Persona cards C-01 through C-12
3. Blocking escalation section
4. PM READ
5. Aggregate NPS + threshold verdict
6. Cross-persona theme matrix

Do not reorder sections. The UX design read establishes craft framing that informs how
you interpret persona friction. The PM read synthesizes after you have seen all 12 persona
signals. The theme matrix closes the output.

---

## Step 1 — UX READ

Read the spec as a UX designer evaluating interaction quality, information architecture,
and user-facing language.

Output format:
```
## UX READ

**Lens**: UX design — interaction quality, IA, user-facing language

[3–5 sentences of craft-level assessment. Flag any interaction patterns that will
produce confused or anxious user behavior. Note missing affordances, ambiguous labels,
or flows that require backtracking.]

**UX concerns for persona reads**: [1–3 named concerns that the persona cards should
surface if they are real — treats this as a prediction checklist]
```

---

## Step 2 — Persona Cards (C-01 through C-12)

For each persona, produce one feedback card. Run all 12.

Card format (strict — do not reorder fields):

```
### {{PERSONA_ID}} — {{PERSONA_NAME}} ({{PERSONA_ROLE}})

**Current approach:** [What this persona currently does, uses, or relies on to accomplish
the job this spec addresses. One to two sentences. Required — do not skip.]

**NPS:** {{score}}/10 [{{band: Detractor|Passive|Promoter}}]
{{1–2 sentence justification comparing the spec against the Current approach above.
Explicitly state whether the spec net benefit exceeds the switching cost for this persona.}}

**Feedback:**
- [severity: blocking|major|minor|cosmetic] — [specific, actionable observation]
- ... (additional items in descending severity order)

**Revision recommendation (if NPS < 6):** [One concrete spec change that would raise
this persona's score. Name the section or field to change. Skip section if NPS ≥ 6.]
```

Severity definitions:
- **blocking** — prevents adoption or causes workflow failure
- **major** — significantly degrades value but has workaround
- **minor** — friction or confusion, low impact
- **cosmetic** — polish / wording

Add `[BLOCKING]` as an inline tag immediately after any blocking severity label, e.g.:
`- [severity: blocking] [BLOCKING] — …`

---

## Step 3 — Blocking Escalation

```
## Blockers Requiring Resolution

[Collect all [BLOCKING] items from persona cards. List each as:
"{{PERSONA_ID}}: [item text]"

If no blocking items exist, write: "No blocking items identified."]
```

---

## Step 4 — PM READ

Read the spec as a PM evaluating market fit, prioritization clarity, and go-to-market
readiness. You now have the full set of persona signals plus the UX read — synthesize
across them.

Output format:
```
## PM READ

**Lens**: Product management — market fit, GTM readiness, prioritization clarity

[3–5 sentences of product-level synthesis. Reference specific persona signals by ID
where relevant. Address whether the blocking or major issues, if any, are scope risks
or execution risks. State a go/no-go recommendation.]
```

---

## Step 5 — Aggregate NPS

```
## Aggregate NPS

| Metric | Value |
|--------|-------|
| Mean NPS | {{mean of C-01..C-12 NPS scores}} |
| Threshold | 7.0 |
| Result | PASS (≥7.0) / REVISE (< 7.0) |
| Detractors (1–6) | {{count}} |
| Passives (7–8) | {{count}} |
| Promoters (9–10) | {{count}} |

**Dominant Detractor objection:** [If any Detractors exist, name the specific
switching-cost or inertia pattern that unifies their low scores. Draw from the
Current approach fields. E.g., "migration cost from existing CLI workflow."
If no Detractors, write "None."]

**Verdict:** [One sentence. If REVISE, name the 1–2 highest-leverage persona changes
that would push the aggregate above 7.0.]
```

---

## Step 6 — Cross-Persona Theme Matrix

This is the final substantive section. Nothing follows it except closing remarks.

```
## Cross-Persona Theme Matrix

| Theme | Personas | Highest Severity | Notes |
|-------|----------|-----------------|-------|
| [theme name] | C-01, C-05, ... | blocking/major/minor/cosmetic | [1-line characterization] |
| ...  | ... | ... | ... |

[Identify 3–8 recurring themes. A theme requires at least 2 personas to qualify.
Name themes concisely (2–4 words). Include at least one theme per blocking or major
issue cluster.]
```

---

## Persona Reference

C-01: Early Adopter Developer — explores APIs before docs exist  
C-02: Enterprise Architect — evaluates integration and compliance surface  
C-03: Skeptical Practitioner — has been burned by similar promises before  
C-04: Power User — uses the tool daily, optimizes for speed  
C-05: New-to-Domain User — learning the domain while using the tool  
C-06: Security Reviewer — assesses exposure, credential handling, blast radius  
C-07: Ops Engineer — cares about observability, runbooks, failure modes  
C-08: Product Manager (user-side) — evaluates fit against their roadmap  
C-09: Designer/Frontend — cares about surface contracts and interaction model  
C-10: Data Analyst — wants structured outputs and queryable artifacts  
C-11: Executive Sponsor — evaluates ROI and narrative, not implementation  
C-12: Accessibility Advocate — evaluates inclusive design and assistive-tech compatibility  

PM: Product Manager (evaluation lens, not a customer persona — does not count toward NPS)  
UX: UX Designer (evaluation lens, not a customer persona — does not count toward NPS)
```

---

### V-02 — Single axis: Inertia framing
**Axis**: Every persona card requires a `Current approach:` structural field as the first body element; NPS justification must explicitly compare spec net benefit against switching cost; aggregate section computes Detractor/Passive/Promoter bands with inertia-baseline definitions  
**Hypothesis**: Making the status-quo comparison mandatory and structural — not optional prose — forces the model to reason about adoption friction before assigning any score, producing NPS scores grounded in competitive reality rather than feature enthusiasm

---

```markdown
You are running a customer feedback simulation. The purpose is to predict adoption
friction for `{{spec}}` by forcing each persona to compare the spec against what they
currently do — not against an ideal.

## Core Principle: Inertia-First Scoring

Every persona has a current approach. The spec must beat that approach by enough to
justify the switching cost. NPS scores that ignore the status quo are invalid.

NPS band definitions for this simulation:
- **Detractor (1–6)**: Switching cost exceeds net benefit. Persona likely stays with current approach.
- **Passive (7–8)**: Marginal net benefit. Persona might adopt but won't advocate.
- **Promoter (9–10)**: Net benefit clearly exceeds switching cost. Persona will adopt and recommend.

These definitions are non-negotiable. Do not use generic NPS band definitions.

---

## Persona Cards (C-01 through C-12)

Run all 12. Each card must follow this exact structure:

```
### {{PERSONA_ID}} — {{PERSONA_NAME}} ({{PERSONA_ROLE}})

**Current approach:** [Required. Name the specific tool, workflow, habit, or behavior
this persona currently uses to accomplish the job the spec addresses. Be concrete —
name tools or process steps if known. This field anchors the NPS justification.
Do not leave blank or write "N/A."]

**NPS:** {{score}}/10 — {{Detractor|Passive|Promoter}}
**Justification:** [Cite the Current approach above. Explicitly state: (a) what the spec
offers that the current approach lacks, and (b) what cost or friction switching introduces.
Conclude with which side wins and why. Minimum 2 sentences. No score is valid without
this comparison.]

**Feedback (descending severity):**
- [blocking|major|minor|cosmetic] — [observation]
- ...

**Revision for NPS < 6:** [If NPS is 5 or below, name one concrete spec change — section,
field, or behavior — that would reduce the switching cost or increase the net benefit
enough to move this persona to Passive. Skip if NPS ≥ 6.]
```

---

## Role Reads

After all 12 persona cards, run:

### UX READ
```
## UX READ

**Lens:** UX — interaction design, user-facing language, flow integrity

[3–5 sentences. Comment on whether the spec's interaction model lowers or raises the
switching cost for inertia-heavy personas. Identify any friction points that will
reinforce "my current approach is fine" thinking.]
```

### PM READ
```
## PM READ

**Lens:** PM — market fit, GTM, prioritization

[3–5 sentences. Given the inertia patterns surfaced by the persona cards, assess whether
the spec's value proposition is differentiated enough to overcome the dominant switching
cost. Reference specific personas or Detractor patterns by name.]
```

---

## Blocking Escalation

```
## Blockers Requiring Resolution

[List all blocking-severity items from persona cards. Format:
"{{PERSONA_ID}}: [item]"

If none: "No blocking items identified."]
```

---

## Aggregate NPS

```
## Aggregate NPS

**Scores:** [list all 12 NPS values]
**Mean NPS:** {{value}}
**Threshold:** 7.0
**Verdict:** PASS / REVISE

**Band distribution:**
- Promoters (9–10, net benefit wins): {{count}} — {{persona IDs}}
- Passives (7–8, marginal net benefit): {{count}} — {{persona IDs}}
- Detractors (1–6, switching cost wins): {{count}} — {{persona IDs}}

**Dominant Detractor objection:** [Required if any Detractors exist. Name the specific
inertia pattern that unifies Detractor scores. Draw directly from the Current approach
fields — the pattern should name what Detractors have in common about their existing
workflows. Example: "terminal-native CLI habit resistant to GUI-first interaction model."
A restatement of the band definition does not pass. Specific named pattern required.]

**Highest-leverage revision:** [If REVISE, identify the 1–2 Detractors whose conversion
to Passive would push the aggregate above 7.0, and name what spec change would do it.]
```

---

## Cross-Persona Theme Matrix

```
## Cross-Persona Theme Matrix

| Theme | Personas | Highest Severity | Inertia Signal |
|-------|----------|-----------------|----------------|
| [theme] | [IDs] | [level] | [Yes/No — does this theme connect to a switching cost?] |
| ...  | ... | ... | ... |

[3–8 themes minimum. Inertia Signal = Yes means the theme is connected to a Current
approach comparison, not just a feature gap. Highlight inertia-linked themes — they
predict adoption risk more reliably than pure feature gaps.]
```

---

## Persona Reference

C-01: Early Adopter Developer — current approach: directly reads source code and issues  
C-02: Enterprise Architect — current approach: architecture review boards and RFP processes  
C-03: Skeptical Practitioner — current approach: battle-tested but dated internal tooling  
C-04: Power User — current approach: keyboard-driven expert workflows with muscle memory  
C-05: New-to-Domain User — current approach: watching tutorials and copying examples  
C-06: Security Reviewer — current approach: manual audit checklists and threat models  
C-07: Ops Engineer — current approach: Grafana dashboards + on-call runbooks  
C-08: Product Manager (user-side) — current approach: spreadsheet roadmaps + Jira  
C-09: Designer/Frontend — current approach: Figma specs + ad-hoc dev handoff  
C-10: Data Analyst — current approach: SQL + CSV exports + Excel pivot tables  
C-11: Executive Sponsor — current approach: monthly status decks from direct reports  
C-12: Accessibility Advocate — current approach: WCAG checklist + manual screen-reader testing
```

---

### V-03 — Single axis: Output format
**Axis**: Persona cards are ordered ascending by NPS score (lowest first); each card header contains only ID/name/role; NPS and band appear as the first body field after `Current approach:`; theme matrix uses a structured table with severity distribution column  
**Hypothesis**: Surfacing the lowest-scoring personas first forces the reader's eye onto adoption risks before reaching comfortable promoter scores; combined with a header-clean card structure, this produces outputs that prioritize revision action over confirmation

---

```markdown
You are running a customer feedback simulation for `{{spec}}`.

## Output Ordering Rules

1. Run all 12 persona cards internally first (in any order).
2. Sort cards by NPS score ascending before writing output — lowest NPS first, highest last.
3. Within a tied NPS score, order by persona ID (C-01 before C-02, etc.).
4. Card headers contain ONLY: persona ID, name, role. No scores in the header line.
5. First body field after the header is always `Current approach:`.
6. Second field is always `NPS:` with band annotation.
7. Feedback items follow, in descending severity order.

This ordering ensures the output leads with the highest adoption risk and forces
revision decisions before reaching promoter cards.

---

## Persona Cards

Format (strictly enforced — do not reorder fields):

```
### {{PERSONA_ID}} — {{PERSONA_NAME}} — {{PERSONA_ROLE}}

**Current approach:** [What this persona currently does/uses for the job this spec
addresses. One to two sentences.]

**NPS:** {{score}}/10 — [Detractor (1–6) | Passive (7–8) | Promoter (9–10)]
[1–2 sentence justification.]

**Feedback:**
- [blocking|major|minor|cosmetic] [BLOCKING if applicable] — [item]
- [items in descending severity order]

**Revision recommendation:** [Include only if NPS ≤ 5. One concrete, named spec change.]
```

Output the cards sorted ascending by NPS score. Do not interleave role reads between cards.

---

## Blocking Escalation (follows last persona card)

```
## Blockers Requiring Resolution

[All blocking items, collected from persona cards. Format: "{{ID}}: [item]"]
[If none: "No blocking items identified."]
```

---

## UX READ

```
## UX READ

**Lens:** UX design — interaction quality, flow, user-facing language

[3–5 sentences. Reference specific cards by persona ID where the UX issues surfaced.
Note whether low-NPS cards share a common UX root cause.]
```

---

## PM READ

```
## PM READ

**Lens:** Product — market fit, GTM readiness, scope risk

[3–5 sentences. Reference the ascending-NPS ordering — what does the distribution
tell you about which segment the spec is optimized for? Name the gap.]
```

---

## Aggregate NPS

```
## Aggregate NPS

**NPS scores (ascending):** [list all 12 in the same order as the cards]
**Mean NPS:** {{value}} / 10
**Threshold:** 7.0
**Verdict:** PASS (≥7.0) / REVISE (<7.0)

| Band | Count | Persona IDs |
|------|-------|-------------|
| Detractor (1–6) | {{n}} | {{IDs}} |
| Passive (7–8) | {{n}} | {{IDs}} |
| Promoter (9–10) | {{n}} | {{IDs}} |

**Dominant Detractor objection:** [Named pattern from Detractor cards. Specific — not
a restatement of the band definition.]

**NPS sensitivity:** [Name the 2–3 personas whose scores most drive the aggregate.
What single spec change would most improve the mean? Be specific.]
```

---

## Cross-Persona Theme Matrix

This is the final major section. No analysis follows it.

```
## Cross-Persona Theme Matrix

| Theme | Personas | Count | Highest Severity | Severity Distribution |
|-------|----------|-------|-----------------|----------------------|
| [theme name] | [IDs] | {{n}} | blocking/major/minor/cosmetic | e.g., "1 blocking, 3 major" |
| ... | ... | ... | ... | ... |

[3–8 themes. Minimum 2 personas per theme. Severity distribution lists count per level
for that theme across all personas that raised it.]

**Most critical theme:** [Name the theme with the highest severity and broadest persona
coverage. One sentence on why it is the top revision priority.]
```

---

## Persona Reference

C-01: Early Adopter Developer  
C-02: Enterprise Architect  
C-03: Skeptical Practitioner  
C-04: Power User  
C-05: New-to-Domain User  
C-06: Security Reviewer  
C-07: Ops Engineer  
C-08: Product Manager (user-side)  
C-09: Designer/Frontend  
C-10: Data Analyst  
C-11: Executive Sponsor  
C-12: Accessibility Advocate

PM and UX are evaluation lenses only — not counted toward aggregate NPS.
```

---

### V-04 — Single axis: Phrasing register
**Axis**: Imperative, directive voice throughout; instructions use "Write:", "List:", "Compute:" rather than descriptive prose; structural requirements stated as explicit prohibitions ("Do not write NPS in the card header"); persona definitions embedded as terse role fragments  
**Hypothesis**: Imperative register with explicit prohibitions eliminates the hedging language that allows models to skip or abbreviate structural requirements; terse instruction style reduces token overhead while preserving constraint coverage

---

```markdown
Simulate customer feedback for this spec: `{{spec}}`
Topic label: `{{topic}}`

Run every step in order. Do not skip steps. Do not combine steps.

---

## STEP 1: UX READ

Write a UX READ section.
- Lens: UX design — interaction design, information architecture, user-facing language
- Length: 3–5 sentences
- Include: one named list of UX concerns that the persona cards should validate or refute
- Do not score. Do not reference personas yet.

---

## STEP 2: PERSONA CARDS

Write one card for each persona C-01 through C-12.

Card rules:
- Header line: ID — Name — Role only. Do not put NPS score in the header.
- Field 1: `Current approach:` — name the tool, workflow, or behavior the persona uses today for this job. Required. No exceptions.
- Field 2: `NPS: X/10 — [Detractor|Passive|Promoter]` — one line.
- Field 3: `Justification:` — compare spec against Current approach. Name the net benefit. Name the switching cost. State which wins. Two sentences minimum.
- Field 4: `Feedback:` — list items in descending severity. Use labels: blocking, major, minor, cosmetic. Tag blocking items with `[BLOCKING]` immediately after the label.
- Field 5: `Revision:` — include only if NPS ≤ 5. Name one concrete spec change. Skip entirely if NPS ≥ 6.

Band definitions:
- Detractor (1–6): switching cost beats net benefit
- Passive (7–8): marginal advantage
- Promoter (9–10): clear win over current approach

Do not deviate from this field order. Do not add extra fields.

---

## STEP 3: BLOCKERS

Write a `Blockers Requiring Resolution` section.
- List every item tagged `[BLOCKING]` from the persona cards.
- Format each as: `PERSONA_ID: [item text]`
- If zero blocking items: write "No blocking items identified."
- Do not editorialize. List only.

---

## STEP 4: PM READ

Write a PM READ section.
- Lens: product management — market fit, GTM readiness, prioritization
- Length: 3–5 sentences
- Reference at least 2 persona IDs by name.
- State a go/no-go recommendation in the final sentence.

---

## STEP 5: AGGREGATE NPS

Compute:
- List all 12 NPS scores (C-01 through C-12 only — PM and UX do not count)
- Compute the mean. Round to one decimal.
- State: PASS if mean ≥ 7.0, REVISE if mean < 7.0.
- Count Detractors, Passives, Promoters.
- Write a `Dominant Detractor objection:` field. Name the shared inertia pattern across Detractor cards. Be specific. Do not restate the band definition.
- If REVISE: name the 2–3 personas whose conversion to Passive would push the mean above 7.0 and state what change would do it.

---

## STEP 6: THEME MATRIX

Write the cross-persona theme matrix. This is the last section. Nothing follows it.

Rules:
- Table format. Columns: Theme | Personas | Highest Severity | Notes.
- 3–8 rows minimum. Each theme requires 2+ personas.
- Name themes in 2–4 words.
- Highest severity: blocking > major > minor > cosmetic.
- Notes: one-line characterization.
- Do not write any analysis section after this table.

---

## PERSONA ROSTER

C-01 Early Adopter Dev — reads source before docs  
C-02 Enterprise Architect — integration and compliance  
C-03 Skeptical Practitioner — burned by hype before  
C-04 Power User — keyboard-optimized daily workflows  
C-05 New-to-Domain — learning domain and tool simultaneously  
C-06 Security Reviewer — exposure, credentials, blast radius  
C-07 Ops Engineer — observability, runbooks, failure modes  
C-08 PM (user-side) — roadmap fit, stakeholder narrative  
C-09 Designer/Frontend — surface contracts, interaction model  
C-10 Data Analyst — structured outputs, queryable artifacts  
C-11 Executive Sponsor — ROI narrative, not implementation detail  
C-12 Accessibility Advocate — inclusive design, assistive-tech compat  

PM = evaluation lens (not counted in NPS)  
UX = evaluation lens (not counted in NPS)
```

---

### V-05 — Combined axes: Role sequence + inertia framing + format constraints
**Axes combined**:
1. **Role sequence**: UX READ before persona cards; PM READ as penultimate section; theme matrix terminal
2. **Inertia framing**: `Current approach:` is a required structural field; NPS band definitions encode switching cost explicitly; `Dominant Detractor objection:` must name a specific inertia pattern
3. **Format constraints**: Card headers are ID/name/role only; cards sorted ascending by NPS; theme matrix includes severity distribution column

**Hypothesis**: The three axes are mutually reinforcing — UX-first primes inertia-aware craft critique; mandatory `Current approach:` fields give the PM READ concrete data to synthesize; ascending card order + structured theme matrix make the combined output immediately actionable without post-processing

---

```markdown
You are running a customer feedback simulation for `{{spec}}` (topic: `{{topic}}`).

This simulation uses inertia-first scoring: every NPS score must reflect whether the
spec beats the persona's current approach by enough to justify switching. Feature
enthusiasm is not a valid NPS justification. Switching cost is always the bar.

NPS band definitions (non-negotiable):
- Detractor (1–6): switching cost exceeds net benefit — persona stays put
- Passive (7–8): marginal net benefit — conditional adoption, no advocacy
- Promoter (9–10): net benefit clearly exceeds switching cost — adoption and recommendation

---

## Section Order (enforced)

1. UX READ
2. Persona cards C-01 through C-12 (sorted ascending by NPS score)
3. Blocking escalation section
4. PM READ
5. Aggregate NPS
6. Cross-persona theme matrix ← final section, nothing follows

---

## 1. UX READ

Run this before the persona cards. Establish craft framing that the persona reads will
validate or refute.

```
## UX READ

**Lens**: UX — interaction design, information architecture, user-facing language

[3–5 sentences. Identify the 1–3 craft-level patterns most likely to create friction for
inertia-heavy personas. Frame each as a switching-cost amplifier: "This pattern will
reinforce 'my current tool handles this fine' because…"]

**Predicted persona friction points**: [Bulleted list of 2–3 specific concerns the
persona cards should surface if the UX critique is correct. Used as a verification
check after cards are complete.]
```

---

## 2. Persona Cards (ascending NPS order)

Internally score all 12 personas first, then output cards sorted lowest NPS to highest.

Card structure (strict — do not reorder, do not add fields, do not add score to header):

```
### {{PERSONA_ID}} — {{PERSONA_NAME}} — {{PERSONA_ROLE}}

**Current approach:** [Required. The specific tool, workflow, or behavior this persona
relies on today for the job this spec addresses. Name tools where known. This field
anchors every subsequent judgment in this card. Do not skip or generalize.]

**NPS:** {{score}}/10 — {{Detractor|Passive|Promoter}}
**Justification:** [Sentence 1: what the spec offers that Current approach lacks.
Sentence 2: what the switching cost is. Sentence 3: verdict — which side wins and why.
All three sentences required.]

**Feedback (descending severity):**
- [blocking] [BLOCKING] — [item]   ← tag inline if blocking
- [major] — [item]
- [minor] — [item]
- [cosmetic] — [item]
(include only applicable severities; ordering must be blocking > major > minor > cosmetic)

**Revision (NPS ≤ 5 only):** [One concrete named spec change that reduces switching cost
or increases net benefit enough to move this persona to Passive. Name the section or
behavior to change. Omit entirely if NPS ≥ 6.]
```

Output all 12 cards sorted ascending. Ties broken by persona ID order.

---

## 3. Blocking Escalation

```
## Blockers Requiring Resolution

[List every [BLOCKING] item collected from persona cards.
Format: "{{PERSONA_ID}}: [item text]"
If zero blocking items: "No blocking items identified."]
```

---

## 4. PM READ

Run after all 12 persona cards. You now have the full inertia picture.

```
## PM READ

**Lens**: Product — market fit, GTM readiness, positioning vs. inertia

[3–5 sentences. Reference at least 2 persona IDs explicitly. Answer:
(1) What segment of the 12 does this spec clearly win? (cite NPS evidence)
(2) What Detractor pattern represents the largest addressable adoption risk?
(3) Go/no-go recommendation — one sentence.]
```

---

## 5. Aggregate NPS

```
## Aggregate NPS

**NPS scores (ascending, matching card order):**
[C-XX: score, C-XX: score, … all 12]

**Mean NPS:** {{value}} / 10
**Threshold:** 7.0
**Verdict:** PASS / REVISE

| Band | Count | Personas |
|------|-------|----------|
| Promoters (9–10) | {{n}} | {{IDs}} |
| Passives (7–8) | {{n}} | {{IDs}} |
| Detractors (1–6) | {{n}} | {{IDs}} |

**Dominant Detractor objection:** [Required if any Detractors exist. Draw from the
Current approach fields. Name the specific inertia pattern that unifies Detractor
scores — the thing those personas have in common about their existing workflows.
A restatement of the band definition does not pass. Example of a passing value:
"terminal-native CLI habit creates high friction against GUI-first interaction model."]

**NPS sensitivity analysis:** [Name the 2–3 personas whose individual scores most
influence the mean. State: what single spec change would most improve the aggregate,
and by approximately how much (e.g., "moving C-03 from 4 to 7 shifts mean by +0.25").]

**Highest-leverage revision (if REVISE):** [Name the 1–2 Detractors to target first
and the specific spec change that addresses their dominant objection.]
```

---

## 6. Cross-Persona Theme Matrix

Final section. No content follows this table.

```
## Cross-Persona Theme Matrix

| Theme | Personas | Count | Highest Severity | Severity Distribution | Inertia-Linked |
|-------|----------|-------|-----------------|----------------------|----------------|
| [theme] | [IDs] | {{n}} | blocking/major/minor/cosmetic | e.g., "1 blocking, 2 major, 1 minor" | Yes/No |
| ... | ... | ... | ... | ... | ... |

[3–8 themes. Each requires 2+ personas. Inertia-Linked = Yes if this theme connects
directly to a Current approach comparison (adoption-risk themes), No if it is a pure
feature gap (quality themes). Distinguish — they require different responses.]

**Verification against UX READ predictions:** [Return to the UX READ "Predicted persona
friction points" list. State which predictions materialized as themes, which did not,
and what the persona cards surfaced that the UX READ missed.]
```

---

## Persona Reference

C-01: Early Adopter Developer — current approach: reads source + issues directly  
C-02: Enterprise Architect — current approach: architecture review boards + RFP  
C-03: Skeptical Practitioner — current approach: entrenched internal tooling  
C-04: Power User — current approach: keyboard-driven expert workflow with muscle memory  
C-05: New-to-Domain User — current approach: tutorials, examples, trial and error  
C-06: Security Reviewer — current approach: manual audit checklists + threat models  
C-07: Ops Engineer — current approach: Grafana + on-call runbooks  
C-08: PM (user-side) — current approach: spreadsheet roadmaps + Jira backlogs  
C-09: Designer/Frontend — current approach: Figma specs + ad-hoc dev handoff  
C-10: Data Analyst — current approach: SQL + CSV + Excel pivots  
C-11: Executive Sponsor — current approach: monthly status decks from reports  
C-12: Accessibility Advocate — current approach: WCAG checklist + screen-reader testing  

PM = evaluation lens only (not counted in NPS mean)  
UX = evaluation lens only (not counted in NPS mean)
```

---

## Summary Table

| Variation | Primary Axis | Secondary Axes | Key Hypothesis |
|-----------|-------------|----------------|----------------|
| V-01 | Role sequence: UX→cards→PM | — | UX framing before cards primes craft critique; PM synthesis after all signals |
| V-02 | Inertia framing: Current approach as anchor | — | Mandatory switching-cost comparison grounds NPS scores in adoption reality |
| V-03 | Output format: ascending NPS + clean headers | — | Lowest scores first forces revision priority before confidence bias sets in |
| V-04 | Phrasing register: imperative/directive | — | Prohibition-style constraints eliminate hedging that allows step skipping |
| V-05 | Role sequence + Inertia + Format | All three | Mutually reinforcing axes — UX primes inertia framing; ascending order + matrix make output immediately actionable |
