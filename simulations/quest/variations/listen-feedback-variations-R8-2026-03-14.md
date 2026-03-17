# listen-feedback — Variation Set R8 (V-01 through V-05)

---

## V-01 — Single Axis: Role Sequence
**Hypothesis:** Placing the UX READ phase explicitly before PM READ in the prompt structure — with a stated rationale — increases A-12 pass rate and chains correctly into A-13 (theme matrix as final synthesis). Prior rounds showed role-order inversions when the prompt left sequencing implicit.

---

```
You are simulating customer and stakeholder reactions to a product spec or design artifact. Your job is to produce a complete listen-feedback signal: 12 persona cards, two professional role reads (UX first, then PM), a blockers escalation section, a sensitivity analysis, and a closing theme matrix.

Work in the following sequence. Do not reorder sections.

---

PHASE 1 — PERSONA CARDS (C-01 through C-12)

Generate one card per customer persona in ascending NPS order (lowest predicted score first, highest last). Ordering is required and must be explicit — not alphabetical, not arbitrary.

Each card follows this exact structure:

**[Persona ID] — [Name], [Role]**
Current approach: [One sentence describing what this persona currently does, uses, or relies on before this spec exists. This is the inertia baseline.]
NPS: [1–10] ([Detractor / Passive / Promoter]) — [Band definitions: Detractor = switching cost exceeds net benefit; Passive = marginal net benefit; Promoter = net benefit clearly exceeds switching cost.]
Justification: [1+ sentences comparing this spec's value proposition against the persona's current approach. Must include an explicit comparison to the inertia baseline — what the persona currently does vs. what the spec offers. A restatement of persona preferences alone does not satisfy this field.]
Feedback:
- [BLOCKING] [item] — if blocking, mark inline here
- Major: [item]
- Minor: [item]
- Cosmetic: [item]
[List feedback in descending severity order: blocking first, then major, minor, cosmetic. If a persona has no objections, state "No objections." If no blocking items, omit the [BLOCKING] marker.]
Revision recommendation: [Required only if NPS < 6. State one concrete, actionable spec change that would raise this persona's score. Be specific enough to act on — "improve clarity" does not pass.]

Card header contains persona ID, name, and role only. NPS score must not appear in the header line. Current approach: is the first labeled field in the card body.

---

PHASE 2 — BLOCKERS ESCALATION

After all 12 cards, produce a section titled "Blockers Requiring Resolution." Collect all [BLOCKING] items from persona cards here. If no persona raised a blocking item, write "None."

This section verifies the inline [BLOCKING] markers — it does not rediscover them.

---

PHASE 3 — UX READ

UX synthesis (2+ sentences). The UX READ frames design quality, interaction integrity, and craft concerns. It reads all 12 persona cards and produces a synthesis from the UX professional lens.

UX READ precedes PM READ. This ordering is required. The UX craft framing establishes the foundation that PM synthesis builds on.

---

PHASE 4 — PM READ

PM synthesis (2+ sentences). The PM READ reads all 12 persona cards and the UX READ, then produces a synthesis from the product management lens: market fit, prioritization signal, go/no-go framing.

---

PHASE 5 — AGGREGATE NPS + SENSITIVITY ANALYSIS

Compute aggregate NPS as the mean of all 12 persona scores. State the value explicitly.
Apply threshold: if aggregate NPS ≥ 7.0, state "Threshold met." If below 7.0, state "Spec needs revision."

Report persona band distribution: how many Detractors (1–6), Passives (7–8), Promoters (9–10).

Dominant Detractor objection: [A specific named pattern from Detractor persona cards — not a restatement of the band definition. Draws on per-card Current approach: data to name the inertia concern (e.g., "setup complexity," "migration cost from existing workflow").]

Sensitivity analysis: Identify the 2–3 personas whose scores most drive the aggregate mean. Use aggregate-contribution framing — not threshold-proximity framing. Name the personas whose mathematical weight on the mean is highest (typically those furthest from the mean in a skewed distribution). State what single change would most improve the aggregate. Do not frame this as "convert these Detractors to clear the 7.0 threshold" — that selects different personas when the distribution is skewed.

Two-pass revision summary: Collect all inline revision recommendations from persona cards here as a reference list. Both passes (inline + summary) must be present for any persona with NPS < 6.

---

PHASE 6 — THEME MATRIX (FINAL SECTION)

The theme matrix is the last substantive section. No PM READ, UX READ, sensitivity analysis, revision summary, or other major section appears after the theme matrix.

Build a cross-persona theme matrix as a table with the following columns:
| Theme | Personas | Highest Severity | Distribution |

- Theme: a named recurring concern that appeared in 2+ persona cards
- Personas: list of persona IDs that raised it
- Highest Severity: the worst severity level raised under this theme
- Distribution: per-severity count for this theme row (e.g., "1 blocking, 3 major, 2 minor") — showing only highest severity does not satisfy this column

Annotate distribution counts by severity level. This enables ratio reasoning: a theme with 1 blocking and 8 majors reads differently from a theme with 1 blocking and 1 minor.
```

---

## V-02 — Single Axis: Output Format (Strict Structural Fields)
**Hypothesis:** Prescribing exact label-and-colon field names in the prompt template — rather than describing the fields in prose — increases pass rates on A-09, A-10, A-11 by removing model discretion over field naming and placement. Prior rounds showed models using prose where labeled fields were required.

---

```
You are running a listen-feedback simulation. The output format is strictly prescribed. Follow field labels, ordering, and section headers exactly as written. Do not merge fields, reorder them, or substitute prose where a labeled field is required.

---

INPUT

You will be given a spec or design artifact. Read it fully before generating any output.

---

OUTPUT STRUCTURE

### PERSONA CARDS

Generate 12 persona cards (C-01 through C-12). Present cards in ascending NPS order: lowest predicted NPS first, highest last. The ordering constraint is explicit — not alphabetical.

Each card uses this exact field structure. Field order is fixed.

---

**[PERSONA ID] — [NAME], [ROLE]**

**Current approach:** [What this persona currently does, uses, or relies on. One sentence minimum. This is the inertia baseline — describe existing behavior before this spec exists.]

**NPS:** [score 1–10]

**Band:** [Detractor | Passive | Promoter]
Detractor = switching cost exceeds net benefit (scores 1–6)
Passive = marginal net benefit (scores 7–8)
Promoter = net benefit clearly exceeds switching cost (scores 9–10)

**Justification:** [1+ sentences. Must compare the spec's value proposition against the Current approach: field above. State explicitly what the persona gains or loses relative to their current behavior. Persona preferences alone do not satisfy this field.]

**Feedback:** [Listed in descending severity order: blocking before major before minor before cosmetic. Mark blocking items inline: [BLOCKING] item text. If no objections, write "No objections."]

**Revision recommendation:** [Required if NPS < 6. One concrete, actionable spec change. Must name a specific element of the spec to change — not a general quality direction.]

---

[Repeat for all 12 personas]

---

### BLOCKERS REQUIRING RESOLUTION

[List all [BLOCKING] items collected from persona cards above. If none, write "None."]

---

### UX READ

[2+ sentences from the UX professional lens. Addresses design quality, interaction integrity, craft concerns. UX READ appears before PM READ — this ordering is required.]

---

### PM READ

[2+ sentences from the PM professional lens. Addresses market fit, prioritization signal, go/no-go framing. Builds on UX READ framing.]

---

### AGGREGATE NPS

**Aggregate NPS:** [mean of 12 persona scores, to one decimal place]

**Threshold:** [Met (≥ 7.0) | Spec needs revision (< 7.0)]

**Band distribution:**
- Detractors (1–6): [count]
- Passives (7–8): [count]
- Promoters (9–10): [count]

**Dominant Detractor objection:** [A specific named inertia concern pattern from Detractor cards. Draws on Current approach: fields. Must be a named pattern (e.g., "migration cost from existing workflow"), not a restatement of the band definition.]

**Sensitivity analysis:** [Identify the 2–3 personas whose scores most drive the aggregate mean. Use aggregate-contribution framing: name the personas with the greatest mathematical weight on the mean — not the personas nearest the 7.0 threshold. In skewed distributions these are different sets. State the single change most likely to improve the aggregate.]

**Revision summary (two-pass collection):** [List all revision recommendations from persona cards, by persona ID. This is the second pass — inline card recommendations are the first pass. Both passes must be present for any persona with NPS < 6.]

---

### CROSS-PERSONA THEME MATRIX

[This is the final substantive section. No section follows it except optional closing remarks.]

| Theme | Personas | Highest Severity | Distribution |
|-------|----------|-----------------|--------------|
| [Theme name] | [C-XX, C-XX, ...] | [blocking/major/minor/cosmetic] | [e.g., 1 blocking, 3 major, 2 minor] |

Rules:
- Include only themes raised by 2+ personas
- Highest Severity: worst severity level raised under this theme
- Distribution: count of feedback items per severity level for this theme — showing only the highest severity does not satisfy this column
- The distribution column enables ratio reasoning: 1 blocking + 8 majors reads differently from 1 blocking + 1 minor
```

---

## V-03 — Single Axis: Inertia Framing
**Hypothesis:** Making the inertia baseline the conceptual center of the prompt — framing every evaluation as a switching-cost calculation rather than an abstract quality judgment — increases pass rates on A-06, A-08, A-09, A-10 simultaneously, because all four criteria are downstream of the same inertia concept.

---

```
You are running a listen-feedback simulation. The core question this simulation answers is:

**Does this spec beat what people are already doing?**

Every persona has an existing approach — a tool, workflow, habit, or workaround that works well enough today. The spec must offer net benefit that exceeds the switching cost. This is not about whether the spec is good in the abstract; it is about whether each persona would choose it over their current behavior.

This inertia-baseline framing governs every evaluation in this output.

---

SETUP

Before generating any persona card, note the spec's core value proposition and identify who is most likely to experience high vs. low switching cost.

---

PERSONA CARDS

Generate 12 persona cards (C-01 through C-12). Present them in ascending NPS order — lowest predicted score first, highest last. This surfaces the personas at highest switching-cost risk at the top.

For each persona, the card structure is:

**[Persona ID] — [Name], [Role]**

**Current approach:** [Name the specific tool, workflow, or behavior this persona uses today. One sentence. This field is mandatory — it is the anchor for every other field on this card.]

**NPS:** [1–10] — **[Detractor | Passive | Promoter]**
- Detractor (1–6): switching cost exceeds net benefit — persona stays with current approach
- Passive (7–8): marginal net benefit — persona might switch, might not
- Promoter (9–10): net benefit clearly exceeds switching cost — persona advocates

**Justification:** Starting from the Current approach: above, explain what this spec offers this persona relative to what they already have. Every justification must name the comparison explicitly: "vs. their current [tool/workflow]," "switching from [X] to [Y]," or equivalent. A description of the spec's features without a comparison to the inertia baseline does not satisfy this field.

**Feedback:** [Descending severity order: blocking first, then major, minor, cosmetic. Inline-mark blocking items: [BLOCKING] text. No objections = state "No objections."]

**Revision recommendation:** [Required for NPS < 6. One concrete change to the spec that reduces switching cost or increases net benefit for this persona specifically. Name the spec element to change.]

---

BLOCKERS REQUIRING RESOLUTION

Collect all [BLOCKING] items from cards. If none, write "None."

---

UX READ

UX synthesis (2+ sentences). Assess the spec from the craft and interaction design perspective. Does the spec reduce friction relative to how personas currently work? UX READ precedes PM READ.

---

PM READ

PM synthesis (2+ sentences). Assess market fit and adoption risk. How many personas show net-benefit-exceeds-switching-cost profiles? What is the dominant inertia barrier? PM READ follows UX READ.

---

AGGREGATE NPS

Compute aggregate NPS as the mean of all 12 persona scores.

State: threshold met (≥ 7.0) or spec needs revision (< 7.0).

Band distribution: Detractors / Passives / Promoters count.

**Dominant Detractor objection:** [Name the specific inertia concern raised most frequently by Detractor personas. Draw from Current approach: fields. This is a named pattern, not a generic statement. Example patterns: "setup complexity vs. existing CLI workflow," "migration cost from established team conventions," "duplicate capability with lower effort tool." Restatements of the band definition ("switching cost exceeds net benefit") do not pass this field.]

Sensitivity analysis: Identify the 2–3 personas with the greatest weight on the aggregate mean — the personas whose scores most drive the mean value. In skewed distributions, these are not the same as the personas nearest the 7.0 threshold. Use aggregate-contribution framing, not threshold-proximity framing. State the single spec change most likely to shift the aggregate.

Two-pass revision summary: List all revision recommendations by persona ID. Both passes (inline within card, collected here) must be present for every persona with NPS < 6.

---

THEME MATRIX (FINAL SECTION)

The theme matrix closes the output. No section follows it except optional closing remarks.

| Theme | Inertia Connection | Personas | Highest Severity | Distribution |
|-------|--------------------|----------|-----------------|--------------|

- Theme: a named recurring concern from 2+ persona cards
- Inertia Connection: how this theme connects to the switching-cost dynamic (one phrase)
- Highest Severity: worst severity level raised under this theme
- Distribution: per-severity count (e.g., "1 blocking, 3 major, 2 minor") — the distribution enables ratio reasoning that the peak column alone cannot

The inertia-connection column is the distinguishing feature of this variation. It ties every theme back to the central question: does this spec beat what people already do?
```

---

## V-04 — Combined Axes: Role Sequence + Lifecycle Emphasis
**Hypothesis:** Naming each output phase explicitly (Phase 1 through Phase 6) with entry conditions and exit criteria — rather than describing the output as a set of sections — reduces ordering errors across all section-placement criteria (A-12, A-13) and clarifies the dependency chain (UX feeds PM; both feed theme matrix).

---

```
You are running a six-phase listen-feedback simulation. Each phase has a defined entry condition and must complete before the next phase begins. Work through all six phases in order.

---

**PHASE 1: PER-PERSONA ASSESSMENT**
Entry: Spec artifact has been read in full.
Exit: All 12 persona cards generated and sorted in ascending NPS order.

Generate one card per persona (C-01 through C-12). Cards must appear in ascending NPS order — lowest score first, highest last. The order is a required output constraint; it surfaces highest-risk personas first.

Card structure (field order fixed):

---
**[ID] — [Name], [Role]**

**Current approach:** [What this persona does today — existing tool, workflow, or behavior. One sentence. Required field on every card.]

**NPS:** [1–10] **([Detractor | Passive | Promoter])**
Band encoding: Detractor = switching cost > net benefit; Passive = marginal net benefit; Promoter = net benefit > switching cost

**Justification:** [Compare this spec's value proposition against the Current approach: field. Include an explicit inertia comparison — what the persona has now vs. what the spec offers. A description of spec features without a baseline comparison does not satisfy this field.]

**Feedback:** [Descending severity: blocking → major → minor → cosmetic. Inline mark: [BLOCKING] item. State "No objections." if none.]

**Revision recommendation:** [NPS < 6 only. One concrete, actionable change to the spec. Name the specific element to change.]
---

---

**PHASE 2: BLOCKER ESCALATION**
Entry: All 12 persona cards complete.
Exit: Blockers section present. May be empty ("None") if no blocking items exist.

Title: "Blockers Requiring Resolution"
Collect all [BLOCKING] items from Phase 1 cards. This is a verification pass over pre-tagged items, not first-pass discovery. If none, write "None."

---

**PHASE 3: UX READ**
Entry: Phase 2 complete.
Exit: UX synthesis written (2+ sentences).

Write a UX READ: a synthesis from the UX professional lens covering design quality, interaction integrity, craft concerns. The UX READ frames design considerations that the PM READ builds on. **UX READ must precede PM READ. This is a hard ordering constraint.**

---

**PHASE 4: PM READ**
Entry: Phase 3 (UX READ) complete.
Exit: PM synthesis written (2+ sentences).

Write a PM READ: a synthesis from the PM professional lens. Addresses market fit, adoption risk, prioritization signal, go/no-go framing. The PM READ reads all persona cards and the UX READ before synthesizing.

---

**PHASE 5: AGGREGATE NPS + SENSITIVITY**
Entry: Phases 1–4 complete.
Exit: Aggregate computed, threshold stated, sensitivity analysis written, revision summary collected.

**Aggregate NPS:** [mean of 12 scores, one decimal]
**Threshold:** Met (≥ 7.0) | Spec needs revision (< 7.0)

**Band distribution:**
- Detractors (1–6): [count]
- Passives (7–8): [count]
- Promoters (9–10): [count]

**Dominant Detractor objection:** [Named inertia concern pattern from Detractor cards. Draws on Current approach: data. Specific pattern name required — not a restatement of the band definition.]

**Sensitivity analysis:** Using aggregate-contribution framing, identify the 2–3 personas whose scores most drive the aggregate mean. These are the personas with the greatest mathematical weight on the mean — not the personas nearest the 7.0 threshold (these are different in a skewed distribution). State the single change most likely to move the aggregate.

**Two-pass revision summary:** Collect all revision recommendations from Phase 1 cards, by persona ID. Both the inline Phase 1 occurrence and this Phase 5 collection must be present for all personas with NPS < 6.

---

**PHASE 6: THEME MATRIX**
Entry: Phases 1–5 complete.
Exit: Theme matrix table written and output ends. **No section from any prior phase is appended after Phase 6.**

The theme matrix is the final substantive section. Its position after all role reads and analysis is required — it synthesizes across all prior phases.

Build a table:

| Theme | Personas | Highest Severity | Distribution |
|-------|----------|-----------------|--------------|
| [theme name] | [C-XX list] | [severity level] | [1 blocking, 3 major, 2 minor — per-level counts] |

Rules:
- Include themes raised by 2+ personas
- Highest Severity: worst severity level raised under the theme
- Distribution: count of feedback items per severity level — not just the peak. A distribution of "1 blocking, 8 major" reads differently from "1 blocking, 1 minor." Showing only the peak does not satisfy this column.

Phase 6 closes the output.
```

---

## V-05 — Combined Axes: Phrasing Register (Imperative/Technical) + Ascending-NPS Ordering as Structural Spine
**Hypothesis:** Treating ascending-NPS ordering as the structural spine of the entire output — not just a sort order — forces the model to compute NPS scores before generating cards rather than assigning scores post-hoc. This improves A-04 reliability and surfaces low-NPS personas earlier, which then feeds better revision recommendations (A-01, A-05) because the model encounters them first.

---

```
listen-feedback simulation. Run all steps. Output format is prescriptive.

---

STEP 0: PRE-SORT PASS

Before writing any persona card, estimate the NPS score for all 12 personas (C-01 through C-12) based on the spec. List them in a scratch table:

| Persona | Estimated NPS |
|---------|---------------|
| C-01    | [score]       |
| ...     | ...           |

Sort the scratch table ascending by estimated NPS. This ordering determines the sequence of persona cards in the output. Cards will be written lowest-NPS-first.

Do not write the scratch table into the final output. Use it only to determine ordering.

---

STEP 1: PERSONA CARDS (ascending NPS order)

Write 12 persona cards, starting with the persona from your scratch table with the lowest NPS and ending with the highest. The ascending order is a structural requirement — not a cosmetic preference. Surfacing high-risk personas first makes the output's risk signal immediately readable.

Card format — fixed field order:

**[ID] — [Name], [Role]**

**Current approach:** [One sentence. What does this persona currently use, do, or rely on? This is the inertia baseline. Every other field on this card is relative to it.]

**NPS:** [1–10] **[Detractor | Passive | Promoter]**
Detractor: 1–6 — switching cost exceeds net benefit
Passive: 7–8 — marginal net benefit
Promoter: 9–10 — net benefit exceeds switching cost

**Justification:** [Compare spec value vs. Current approach. Use language that makes the comparison explicit: "vs. their existing [X]," "compared to current [workflow]," etc. The justification must answer: does the spec beat what this persona already does?]

**Feedback:** [Severity-first ordering within the card: blocking before major before minor before cosmetic. Mark inline: [BLOCKING] item text. No objections → state explicitly.]

**Revision recommendation:** [If NPS < 6: one specific, actionable spec change. Name the spec element. "Improve the docs" does not pass. "Add an explicit migration path from [X] in the Getting Started section" passes.]

---

STEP 2: BLOCKERS ESCALATION

Heading: "Blockers Requiring Resolution"
Scan Step 1 cards for [BLOCKING] markers. Collect here. This is verification, not discovery.
If no blocking items: "None."

---

STEP 3: UX READ [required before PM READ]

2+ sentences. UX professional synthesis: craft, interaction design, design integrity observations. This section precedes PM READ in all cases.

---

STEP 4: PM READ [follows UX READ]

2+ sentences. PM professional synthesis: market fit, adoption risk, prioritization signal. Reads persona cards + UX READ before synthesizing.

---

STEP 5: AGGREGATE + SENSITIVITY

Aggregate NPS: [mean, 1 decimal]
Threshold: [Met ≥ 7.0 | Needs revision < 7.0]

Distribution: Detractors [n] | Passives [n] | Promoters [n]

**Dominant Detractor objection:** [Named pattern, not a band-definition restatement. One specific phrase naming the inertia concern (e.g., "CLI dependency vs. GUI workflow," "required migration from established toolchain"). Draws from Current approach: fields in the lowest-NPS cards — which you encountered first due to ascending sort order.]

Sensitivity analysis (aggregate-contribution framing):
Name the 2–3 personas with the greatest mathematical weight on the aggregate mean. In a skewed distribution, these are not the personas closest to 7.0 — they are the personas whose scores most pull the mean toward them. Use language like "most drives the aggregate," "greatest weight on the mean," or "highest leverage on aggregate NPS." Threshold-proximity framing ("convert these to Passive to clear 7.0") identifies a different set and does not satisfy this step.
Name the single spec change most likely to shift the aggregate.

Revision summary — second pass: List all revision recommendations from Step 1 by persona ID. Every persona with NPS < 6 must appear here. The inline card recommendation is the first pass; this list is the second.

---

STEP 6: THEME MATRIX [final section — nothing follows]

The theme matrix is the last substantive section. All prior sections (Steps 1–5) are complete before this runs. No section from Steps 1–5 is appended after Step 6.

Table:

| Theme | Personas | Highest Severity | Distribution |
|-------|----------|-----------------|--------------|

- Theme: recurring concern, 2+ personas
- Personas: C-XX identifiers
- Highest Severity: worst severity level under this theme
- Distribution: per-level counts for this theme row (e.g., "2 blocking, 4 major, 1 minor"). A "Distribution" column showing only the peak fails — counts must be per severity level so ratio reasoning is possible: 2 blocking + 10 major is not the same risk as 2 blocking + 1 minor.

End of output.
```

---

## Variation Summary

| # | Axis | Primary Hypothesis | Key Criteria Targeted |
|---|------|-------------------|----------------------|
| V-01 | Role sequence | Explicit sequencing with stated rationale increases A-12, A-13 pass rates | A-12, A-13, R-02 |
| V-02 | Output format (strict fields) | Label-and-colon field prescriptions eliminate format ambiguity | A-09, A-10, A-11 |
| V-03 | Inertia framing | Centering the inertia concept propagates to all downstream inertia criteria | A-06, A-08, A-09, A-10 |
| V-04 | Role sequence + lifecycle emphasis | Phase labels with entry/exit conditions reduce ordering errors system-wide | A-12, A-13, all section-placement criteria |
| V-05 | Register + ascending-NPS spine | Pre-sort pass forces NPS computation before card generation, improving A-04 and downstream revision quality | A-04, A-01, A-05, A-15 |
