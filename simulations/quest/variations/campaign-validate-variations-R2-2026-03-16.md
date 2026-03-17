Now I have all the context I need. R1 scores were V-01: 93, V-02: 98, V-03: unscored. The v2 rubric adds C-11/C-12/C-13 and C-09 partial was the persistent weak point (qualitative tags, not segment-specific). Generating 5 complete variations now.

---

# campaign-validate — Quest Variate R2

**Skill**: campaign-validate
**Round**: 2
**Rubric**: v2 (115 pts max)
**R1 baseline**: V-01: 93, V-02: 98 (both golden; C-09 partial in both; C-11/C-12/C-13 not yet in scope)
**R2 target**: Address C-09 specificity gap, lock in C-11/C-12/C-13, probe remaining axes

**Axes selected for single-axis (3)**: phrasing register, inertia framing, lifecycle emphasis
**Combined (2)**: output format + v2 template encoding; listen-first sequence + quantified adoption impact

---

## V-01 — Phrasing Register (Conversational/Narrative)

**Axis**: Phrasing register — conversational, first-person narrative; the model narrates the investigation rather than executes phase commands.
**Hypothesis**: A narrative register reduces structural brittleness by encouraging the model to weave sub-skill findings into a coherent story rather than treating each section as an isolated task. Cross-signal synthesis (C-06) should emerge naturally from storytelling. Risk: listen-adoption may get folded silently into the narrative if the model treats the two listen sub-skills as one voice.

---

You are validating a design before the team commits to spec. Work through five lenses — each one a distinct signal — then synthesize what you find into a brief that tells the team whether to go, wait, or stop.

**The five lenses, in this order:**

Start by imagining the people who will actually use this. Run **review-users**: five user personas each walk through the design looking for friction, confusion, or moments where they would abandon the task. Write down what each persona says they would struggle with and give each finding a severity (P1 = blocks core use case, P2 = major friction, P3 = minor annoyance).

Next, zoom out to the design itself. Run **review-design**: six discipline reviewers (architect, code-quality, documentation, testing, process, implementation) plus domain-selected experts examine the design for structural problems. Add their findings to the pile.

Now hear from the market. Run **review-customers**: twelve customer personas evaluate the feature for usefulness, clarity, and whether they would adopt. Note which customer segments are enthusiastic and which are skeptical.

Then ask the support desk. Run **listen-feedback**: predict the top customer reactions before the feature ships — NPS predictions, frustration themes, and the signals that would show up in post-launch feedback. This is not the same as adoption; it is the emotional response to the design.

Finally, trace the adoption path. Run **listen-adoption**: simulate the Rogers adoption curve for this feature. Which innovators pick it up? Where is the chasm? What must be true for early majority to cross? For each segment (innovators, early adopters, early majority, late majority, laggards) estimate the percentage who would adopt and what would block the rest.

**Important**: listen-feedback and listen-adoption are separate lenses. Feedback is reaction; adoption is trajectory. Do not merge them.

**After all five lenses**, write the validation brief:

Open with a verdict: **GO**, **NO-GO**, or **CONDITIONAL GO** (if conditional, name the condition explicitly — never write "it depends" without completing the sentence).

For the findings section, rank every finding by adoption impact, not by severity. A P2 design flaw that would block 60% of early majority from crossing the chasm ranks above a P1 usability issue affecting only 2% of innovators. Use these adoption impact labels, each with a segment and an estimated percentage affected: "blocks chasm crossing (early majority, ~45%)", "impedes innovators only (~3%)", "majority-blocking but recoverable post-v1 (~35%)". Severity (P1/P2/P3) appears as a secondary attribute, not the sort key.

For the top blockers section (only needed on NO-GO or CONDITIONAL GO): list the top 3 blockers. For each: the blocker text, which sub-skill surfaced it, what change would resolve it, and which sub-skill's finding supports that resolution path.

For the synthesis section: identify at least one pattern or tension that appears across two or more lenses. Format: "Finding [X] surfaced in [sub-skill A] is confirmed/contradicted by [Y] surfaced in [sub-skill B]." A list of five separate sections is not a synthesis; a connection is.

Label each sub-skill's findings under its own heading so readers can navigate directly. Use P1/P2/P3 throughout.

Write the complete brief to `simulations/{topic}/validate-{date}.md`.

After writing, confirm: `Artifact written: simulations/{topic}/validate-{date}.md`

---

## V-02 — Inertia Framing (Status-Quo as Primary Anchor)

**Axis**: Inertia framing — the status quo (what users do today without this feature) is the explicit anchor at every sub-skill stage. Every finding is framed as a delta from inertia.
**Hypothesis**: Anchoring each sub-skill against "what users do today" forces the model to name specific switching costs and friction, making adoption impact quantification (C-09) automatic at the segment level — the model must say "early majority who currently use [X workaround]" not just "high adoption impact." Risk: inertia framing may crowd out forward-looking cross-signal synthesis (C-06) if every finding is backward-looking.

---

Before you evaluate this design, establish the baseline: what do users do today without it? The inertia baseline is the primary competitor. Every finding in this validation measures the delta from that baseline.

**Step 1 — Establish the inertia baseline.**
Name the current workaround or status-quo behavior. Identify who does it (which segments), how often, and what they pay in time, error rate, or friction. This baseline will anchor every sub-skill that follows.

**Step 2 — review-users (against inertia).**
Five user personas each walk through the new design. For each persona, ask: does this design remove enough friction from their current workaround to cause switching? Rate each friction point as P1 (the workaround is easier), P2 (comparable, user may not switch), or P3 (new design has minor edge). For each finding, estimate which Rogers segment this persona represents and whether this friction point is chasm-blocking for that segment.

**Step 3 — review-design (against inertia).**
Six discipline reviewers examine the design. For each structural concern, ask: does this problem make the inertia baseline look better by comparison? A design flaw that replicates existing workaround behavior at parity is a P2. A flaw that makes the new feature strictly harder than the workaround is a P1. Add domain experts as appropriate.

**Step 4 — review-customers (against inertia).**
Twelve customer personas evaluate the feature. For each persona, record: their current workaround, their switching threshold, and whether the design clears that threshold. Would-adopt scores are meaningful only relative to inertia — a persona who says "maybe" is not the same as a persona who says "this doesn't solve my problem any better."

**Step 5 — listen-feedback (reaction to the delta).**
Predict the top emotional reactions to the design. Specifically: which users feel the delta from inertia is worth the switching cost, and which feel the new design asks more of them than their current workaround demands? Predict NPS per persona with the switching cost framing. This is the emotional response to the design, not the adoption trajectory.

**Step 6 — listen-adoption (Rogers curve against inertia).**
Simulate the Rogers adoption curve. For each archetype, name:
- The segment percentage (approximate: innovators ~2.5%, early adopters ~13.5%, early majority ~34%, late majority ~34%, laggards ~16%)
- What they currently do instead (their inertia behavior)
- What must change in the design for them to cross
- Whether the design as reviewed clears their switching threshold

The chasm is the gap between early adopters (who tolerate rough edges) and early majority (who will not switch unless the new design is clearly better than their current workaround for their main job). State whether the design crosses the chasm and why.

**Step 7 — Validation Brief.**

**Verdict**: GO / NO-GO / CONDITIONAL GO (with explicit condition).

**Ranked Findings** — sorted by adoption impact, not severity. Adoption impact uses this format: "[Segment] ([%]): [what must be true for them to adopt]". Severity (P1/P2/P3) is a secondary column.

**Top 3 Blockers** (NO-GO and CONDITIONAL GO only): Each blocker includes: the blocker, the sub-skill source, the inertia comparison (why it keeps users in their workaround), and the remediation path (what design change resolves it).

**Cross-Signal Synthesis**: At least one pattern that appears across two or more sub-skills. Specifically look for: a usability finding (review-users) that maps to a support prediction (listen-feedback) for the same user action; a customer skepticism (review-customers) that corresponds to a chasm-blocking inertia behavior (listen-adoption).

Each sub-skill under its own labeled heading. P1/P2/P3 throughout.

Write complete brief to `simulations/{topic}/validate-{date}.md`.

Emit: `Artifact written: simulations/{topic}/validate-{date}.md`

---

## V-03 — Lifecycle Emphasis (Strict Phase-Gate)

**Axis**: Lifecycle emphasis — strict phase gates; each sub-skill phase must complete and emit a named section before the next phase is permitted to begin. No phase may borrow from or reference a prior phase's work until the synthesis gate.
**Hypothesis**: The phase-gate structure enforces C-01 completeness structurally — listen-adoption cannot be silently merged with listen-feedback because each has its own gate that must produce distinct content. Risk: rigid phase enforcement may impede the organic cross-signal synthesis (C-06) that comes from seeing all findings simultaneously.

---

This skill runs in six phases. Each phase has a gate. You may not proceed to the next phase until the current phase gate is satisfied. Gate satisfaction means: the required section heading exists and contains distinct findings.

**Output path**: `simulations/{topic}/validate-{date}.md`
**Ranking rule**: all findings ranked by adoption impact (segment + estimated percentage affected), not by severity. Severity (P1/P2/P3) is a secondary attribute.

---

**Phase 1 — review-users**
Gate: Section `## review-users Findings` exists with findings from at least 3 user personas. Each finding has: persona name, friction description, severity (P1/P2/P3), and initial adoption impact estimate (which Rogers segment this affects and whether it is chasm-blocking).

Do not proceed to Phase 2 until Phase 1 gate is satisfied.

---

**Phase 2 — review-design**
Gate: Section `## review-design Findings` exists with findings from all 6 discipline reviewers plus any domain-selected experts. Each finding has: reviewer role, concern, severity, and structural impact (does this concern make the design harder to adopt?).

Do not proceed to Phase 3 until Phase 2 gate is satisfied.

---

**Phase 3 — review-customers**
Gate: Section `## review-customers Findings` exists with findings from at least 8 customer personas. Each finding has: persona name, current workaround, would-adopt signal (yes/no/conditional), and the condition blocking adoption if conditional.

Do not proceed to Phase 4 until Phase 3 gate is satisfied.

---

**Phase 4 — listen-feedback**
Gate: Section `## listen-feedback Findings` exists with at least 5 distinct findings. Each finding has: feedback theme, customer segment affected, predicted NPS direction, and whether this theme appears in Phase 1 or 3 findings (mark "confirmed by review-users" or "new signal" as appropriate).

NOTE: listen-feedback is about pre-ship customer *reaction*. It is not the same as adoption trajectory. Do not merge this section with Phase 5.

Do not proceed to Phase 5 until Phase 4 gate is satisfied.

---

**Phase 5 — listen-adoption**
Gate: Section `## listen-adoption Findings` exists with a Rogers curve simulation. Required rows: innovators, early adopters, early majority, late majority, laggards. Each row: segment name, estimated adoption % for this feature, what blocks the remaining %, and whether the chasm (early adopter → early majority) is crossed. The chasm crossing verdict must be explicit: CROSSED / NOT CROSSED / CONDITIONAL.

NOTE: listen-adoption is about adoption trajectory over time across archetypes. It is categorically different from listen-feedback. Each row must contain distinct content from Phase 4.

Do not proceed to Phase 6 until Phase 5 gate is satisfied.

---

**Phase 6 — Synthesis and Brief**
All 5 phase gates are now satisfied. Produce the validation brief.

**Verdict** (required, first line of brief): GO / NO-GO / CONDITIONAL GO. If conditional, complete the sentence: "CONDITIONAL GO if [specific condition]."

**Ranked Findings Table** — all findings from Phases 1–5, sorted by adoption impact descending. Columns: Finding | Sub-Skill | Severity | Adoption Impact (segment, %). A P2 that blocks chasm crossing (early majority, ~34%) must appear above a P1 affecting innovators (~2.5%).

**Top 3 Blockers** (NO-GO and CONDITIONAL GO only):

| Rank | Blocker | Sub-Skill Source | Adoption Impact | Remediation Path |
|------|---------|-----------------|-----------------|-----------------|
| 1 | ... | Phase N | ... | ... |

**Cross-Signal Synthesis** — at least one finding pattern linking two or more phases. Template: "Finding [X] from Phase [N] is [confirmed / contradicted / amplified] by Finding [Y] from Phase [M]." At least one synthesis point required; three preferred.

**Go/No-Go Summary**: one sentence per sub-skill summarizing its signal. Five sentences total, one per phase.

Write the complete brief to `simulations/{topic}/validate-{date}.md`.

Emit: `Artifact written: simulations/{topic}/validate-{date}.md`

---

## V-04 — Output Format (Full v2 Template — C-11/C-12/C-13 Encoded)

**Axis**: Output format — all three new v2 aspirational criteria (C-11 table skeleton, C-12 separate Severity and Adoption Impact columns, C-13 confirmation string) plus C-09 segment specificity are structurally encoded into the template. The model fills slots; the structure enforces correctness.
**Hypothesis**: Pre-defining table skeletons with all five sub-skill rows (C-11) means a skipped sub-skill appears as a blank table row rather than invisible absence. Separate Severity and Adoption Impact columns in every table (C-12) prevents rank-by-severity errors at the layout level. The confirmation string requirement (C-13) closes C-05 with a machine-detectable signal. Forcing "(segment, ~N%)" notation in every Adoption Impact cell (C-09) eliminates the "high/medium/low" generic that blocked full C-09 credit in R1.

---

Run the full design validation campaign. Output format is strictly defined below. Fill every table slot — a blank cell is acceptable; a missing row is not.

**Output path**: `simulations/{topic}/validate-{date}.md`
**Adoption impact notation**: always "(segment, ~N%)" — e.g., "chasm-blocking (early majority, ~34%)", "innovator-only (~2.5%)". Generic "high/medium/low" is not acceptable.

---

### Section 1 — Sub-Skill Findings Tables

For each of the five sub-skills below, populate the findings table. If a sub-skill produces no findings, the row must appear with "No findings" in the Finding column. An absent table for any sub-skill is a completeness failure.

**1.1 review-users**

Run 5 user persona advocates through the design.

| Persona | Finding | Severity | Adoption Impact (segment, ~N%) | Remediation Path |
|---------|---------|----------|-------------------------------|-----------------|
| (persona 1) | | | | |
| (persona 2) | | | | |
| (persona 3) | | | | |
| (persona 4) | | | | |
| (persona 5) | | | | |

**1.2 review-design**

Run 6 discipline reviewers plus domain-selected experts.

| Reviewer Role | Finding | Severity | Adoption Impact (segment, ~N%) | Remediation Path |
|--------------|---------|----------|-------------------------------|-----------------|
| Architect | | | | |
| Code Quality | | | | |
| Documentation | | | | |
| Testing | | | | |
| Process | | | | |
| Implementation | | | | |
| [Domain Expert] | | | | |

**1.3 review-customers**

Run 12 customer personas.

| Persona | Would Adopt | Condition if Conditional | Finding | Severity | Adoption Impact (segment, ~N%) | Remediation Path |
|---------|------------|--------------------------|---------|----------|-------------------------------|-----------------|
| (C-01) | | | | | | |
| (C-02) | | | | | | |
| ... (12 rows) | | | | | | |

**1.4 listen-feedback**

Predict top pre-ship customer reactions. NOTE: feedback is reaction, not adoption trajectory. Distinct from 1.5.

| Feedback Theme | Segment Affected | Predicted NPS Direction | Severity | Adoption Impact (segment, ~N%) | Remediation Path |
|--------------|-----------------|------------------------|----------|-------------------------------|-----------------|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

**1.5 listen-adoption**

Rogers archetype simulation. NOTE: adoption trajectory, not reaction. Each row must have distinct content from 1.4.

| Archetype | Est. Adoption % | What Blocks Remainder | Severity | Adoption Impact (segment, ~N%) | Remediation Path |
|-----------|----------------|----------------------|----------|-------------------------------|-----------------|
| Innovators (~2.5%) | | | | | |
| Early Adopters (~13.5%) | | | | | |
| Early Majority (~34%) | | | | | |
| Late Majority (~34%) | | | | | |
| Laggards (~16%) | | | | | |
| **Chasm verdict** | CROSSED / NOT CROSSED / CONDITIONAL | Condition: | | | |

---

### Section 2 — Master Ranked Findings Table

All findings from Sections 1.1–1.5 consolidated and sorted by Adoption Impact descending. Severity is a secondary sort key only — never the primary.

| Rank | Finding | Sub-Skill | Severity | Adoption Impact (segment, ~N%) | Remediation Path |
|------|---------|-----------|----------|-------------------------------|-----------------|
| 1 | | | | chasm-blocking (early majority, ~34%) | |
| 2 | | | | | |
| ... | | | | | |

---

### Section 3 — Cross-Signal Synthesis

Identify at least one finding that appears or is amplified across two or more sub-skills.

**Pattern 1**: [Finding] appears in [sub-skill A] and is [confirmed / contradicted / amplified] in [sub-skill B]. Implication: [what this means for the verdict].

*(add more patterns as found)*

---

### Section 4 — Top 3 Blockers (NO-GO and CONDITIONAL GO only; omit on GO)

| Rank | Blocker | Sub-Skill Source | Adoption Impact (segment, ~N%) | Remediation Path |
|------|---------|-----------------|-------------------------------|-----------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

---

### Section 5 — Verdict

**Go/No-Go**: [GO | NO-GO | CONDITIONAL GO — if conditional: "CONDITIONAL GO if [specific condition]"]

**Rationale**: one sentence per sub-skill. Five sentences total.

---

Write the complete artifact (all sections above) to `simulations/{topic}/validate-{date}.md`.

Emit this exact string after writing:
`Artifact written: simulations/{topic}/validate-{date}.md`

---

## V-05 — Combined: Listen-First Sequence + Quantified Adoption Impact Mandate

**Axis**: Role sequence (listen-first: adoption baseline before design review) + adoption impact quantification mandate (Rogers segments with percentages required throughout).
**Hypothesis**: Running listen-adoption first establishes the Rogers segment baseline before any design evaluation begins. Every subsequent sub-skill evaluates findings against a pre-defined archetype map with percentages, making C-09 adoption impact quantification automatic — the segment names and percentages are already in scope when review-users and review-design run. This also sets up cross-signal synthesis (C-06) organically because each review sub-skill explicitly references the adoption baseline established in Phase 1.

---

Validate the design using a listen-first sequence. The adoption map comes first; all subsequent sub-skills evaluate against it.

**Output path**: `simulations/{topic}/validate-{date}.md`
**Sequencing rationale**: adoption impact is the ranking criterion. Establishing the Rogers segment baseline first ensures every finding is evaluated with segment percentages in scope, not added retroactively.

---

**Phase 1 — Adoption Baseline (listen-adoption)**

Before reviewing the design, simulate the adoption curve. This is the map every subsequent finding will reference.

Produce the Rogers Baseline Table:

| Archetype | Est. Population % | Adoption Threshold | Chasm Position |
|-----------|------------------|-------------------|----------------|
| Innovators | ~2.5% | [what they need] | Pre-chasm |
| Early Adopters | ~13.5% | [what they need] | Pre-chasm |
| Early Majority | ~34% | [what they need] | Chasm gate |
| Late Majority | ~34% | [what they need] | Post-chasm |
| Laggards | ~16% | [what they need] | Post-chasm |

**Chasm verdict**: CROSSED / NOT CROSSED / CONDITIONAL (condition named explicitly).

This table is the adoption map. Every finding in Phases 2–5 must reference a row from this table.

---

**Phase 2 — User Reactions (review-users)**

Five user personas walk through the design. For each friction finding, tag it to an archetype row from the Phase 1 baseline: which segment does this persona represent, and does this finding move or preserve the chasm verdict?

| Persona | Archetype (from Phase 1) | Finding | Severity | Adoption Impact: segment (~N%) | Chasm Effect |
|---------|------------------------|---------|----------|-------------------------------|--------------|
| | | | | | CROSSES / BLOCKS / NEUTRAL |

---

**Phase 3 — Design Concerns (review-design)**

Six discipline reviewers plus domain experts. For each structural finding, tag it to the Phase 1 baseline: which segment is affected, and does this concern threaten chasm crossing?

| Reviewer | Finding | Severity | Adoption Impact: segment (~N%) | Chasm Effect |
|---------|---------|----------|-------------------------------|--------------|
| | | | | CROSSES / BLOCKS / NEUTRAL |

---

**Phase 4 — Customer Signals (review-customers)**

Twelve customer personas. For each persona, record: archetype from Phase 1, would-adopt signal, and — critically — whether their adoption threshold from Phase 1 is met by the current design.

| Persona | Archetype | Phase 1 Threshold Met? | Would Adopt | Finding | Adoption Impact: segment (~N%) |
|---------|-----------|----------------------|------------|---------|-------------------------------|
| | | YES / NO / PARTIAL | | | |

---

**Phase 5 — Pre-Ship Reactions (listen-feedback)**

Predict the top 5 customer reactions. For each, reference the archetype and the Phase 1 adoption threshold: does this reaction suggest the threshold will be met or missed?

NOTE: listen-feedback is reaction, not adoption trajectory. Phases 5 and 1 are distinct sub-skills producing distinct findings.

| Feedback Theme | Archetype | Phase 1 Threshold Signal | NPS Direction | Adoption Impact: segment (~N%) |
|---------------|-----------|-------------------------|--------------|-------------------------------|
| | | CONFIRMS / UNDERMINES / NEUTRAL | | |

---

**Phase 6 — Validation Brief**

All five sub-skills have run. Produce the brief.

**Verdict**: GO / NO-GO / CONDITIONAL GO (condition named explicitly if conditional).

**Chasm Status**: restate Phase 1 chasm verdict, now updated with evidence from Phases 2–5. If the chasm verdict changed, explain what sub-skill finding changed it.

**Ranked Findings** — sorted by adoption impact descending. Use Phase 1 segment names and percentages throughout. A finding that blocks early majority (~34%) outranks a finding that affects only innovators (~2.5%) regardless of severity.

| Rank | Finding | Sub-Skill | Severity | Adoption Impact: archetype (~N%) | Remediation Path |
|------|---------|-----------|----------|----------------------------------|-----------------|

**Cross-Signal Synthesis** — at least one pattern linking two or more phases. The listen-first structure naturally surfaces adoption-confirmed patterns: "Finding X (Phase 2, review-users) matches the early majority adoption threshold identified in Phase 1 and is further confirmed by Y (Phase 5, listen-feedback)."

**Top 3 Blockers** (NO-GO and CONDITIONAL GO only): blocker, sub-skill source, archetype affected (~N%), remediation path.

Write complete brief to `simulations/{topic}/validate-{date}.md`.

Emit: `Artifact written: simulations/{topic}/validate-{date}.md`

---

## Variation Summary

| V | Axis | Hypothesis | Primary C-09 Strategy | C-11 | C-12 | C-13 |
|---|------|------------|----------------------|------|------|------|
| V-01 | Phrasing register (conversational) | Narrative register improves synthesis (C-06) | Explicit segment+% format mandated in ranked section | None | None | Required |
| V-02 | Inertia framing (status-quo anchor) | Switching cost framing forces segment naming naturally | "(segment, ~N%)" emerges from inertia comparison | None | None | Required |
| V-03 | Lifecycle emphasis (phase-gate) | Phase gates enforce C-01 completeness structurally | Adoption impact estimate required at each phase gate | None | None | Required |
| V-04 | Output format (full v2 template) | Pre-built table skeleton forces all criteria at layout level | "(segment, ~N%)" as required cell notation | Encoded | Encoded | Encoded |
| V-05 | Role sequence + quantified adoption | Listen-first puts segment %s in scope before review runs | Phase 1 table creates segment vocabulary reused by all phases | None | Partial | Required |

**Predictions**:
- V-04 is the ceiling attempt — all three new criteria encoded; should reach 110+ if C-09 cell notation holds
- V-05 is the highest-risk, highest-reward: if listen-first works, C-09 becomes structurally automatic; if not, the rigid sequence may impede synthesis
- V-01 is the lowest-ceiling solo-axis variation but the most natural for a practitioner to actually write; good probe of whether structural encoding is necessary for correctness
- V-02 should fix C-09 via inertia framing at the cost of some synthesis depth — worth scoring to see if the tradeoff is favorable
- V-03 is the phase-gate test that was unscored in R1; now has explicit adoption impact requirements per gate
