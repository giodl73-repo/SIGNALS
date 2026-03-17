# Scout-Size Prompt Variations — R12

**Skill**: scout-size
**Rubric**: v12 (27 aspirational criteria, C-09 through C-35)
**Date**: 2026-03-17
**Round**: 12
**R11 champion**: V-05 (27/27 under v12 — Phase 0 inertia gate + 4-field inertia + inline constraint tags on C-01/C-02)
**R11 gaps**: C-35 satisfied at minimum threshold (C-01/C-02 only); no quantified Cost Trajectory; no phase close-out artifacts; self-check coverage of C-33/C-34/C-35 unverified in multi-phase designs

---

## Context: What R12 Addresses

V-05 R11 achieves 100.00 under v12 by combining: inertia as Phase 0 gate (C-33), 4-field cost analysis (C-34), and point-of-use constraint tags on C-01/C-02 (C-35). R12 explores what lies beyond the v12 ceiling — excellence signals that could seed v13 criteria.

**R11 residual gaps (potential v13 seeds):**

| Gap | Observation | Potential v13 criterion |
|-----|-------------|------------------------|
| G-01 | C-35 requires tags on C-01/C-02 only; Confidence Level, Cost Direction, Tier-Destination are uncovered at write time | C-35 extension: tags on ALL vocab-constrained fields |
| G-02 | C-34 requires Cost Direction (trend) but not a quantified rate | Cost Trajectory: quantified rate converts "getting worse" into "getting worse at +~N%/quarter" |
| G-03 | Phase transitions use verbal handoffs; no confirmation that all charter deliverables were populated | Phase SEALED blocks: explicit close-out checklist before next phase opens |
| G-04 | Multi-phase designs in R11 omit per-criterion self-check ("C-28 N/A in three-phase design") | Self-check must be present in multi-phase designs — C-28 has no architectural exemption |

**Axes selected:**

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Output format (C-35 extended to all vocab-constrained fields) | C-35 passes at minimum when only C-01/C-02 carry [FAIL: ...] tags. Confidence Level, Cost Direction, Tier-Destination, and FTE notation accept controlled vocabulary but are unguarded at write time. V-01 extends tags to all constrained fields. Hypothesis: selective C-35 coverage creates an inconsistent compliance surface — a model encountering tags on two fields but not others may treat uncovered fields as vocabulary-free. |
| V-02 | Inertia framing (5-field inertia with quantified Cost Trajectory) | C-34 formalizes 4 fields including Cost Direction (trend). V-02 adds Cost Trajectory as a 5th field: estimated rate of change ("+~15%/quarter", "~constant"). Rate converts directional intent into a forecasting signal — the answer to "how urgently must this be built?" |
| V-03 | Lifecycle emphasis (PHASE SEALED blocks with completion checklists) | R11 V-05 phase transitions are verbal ("Phase N complete. Proceed."). V-03 adds PHASE N SEALED blocks: a short checklist requiring explicit confirmation that all charter deliverables are populated before the next phase opens. Hypothesis: verbal handoffs allow silent phase-boundary violations; sealed blocks prevent them structurally. |
| V-04 | Combined: Output format + Lifecycle emphasis (V-01 + V-03) | C-35 extension and Phase SEALED blocks address orthogonal failure modes: field-level vocabulary violations (write time) vs. phase-completion violations (transition time). Combined, they create a two-layer prevention system. |
| V-05 | Combined: all axes + phrasing register (V-01 + V-02 + V-03 + examiner voice) | Maximum structural and vocabulary encoding. Adds examiner-voice register (third-person institutional: "The Sizing Engineer produces...") alongside all four mechanisms. Tests whether institutional voice produces more consistent adherence than second-person imperative at maximum encoding density. |

---

## V-01 — Axis: Output format (C-35 extended to all vocabulary-constrained fields)

**Variation axis**: Output format — inline `[FAIL: ...]` constraint tags extended from minimum coverage (C-01/C-02) to every vocabulary-constrained field in the prompt

**Hypothesis**: C-35 passes at minimum when complexity tier and timeline columns carry point-of-use constraint tags. Confidence Level, Cost Direction, Tier-Destination (sensitivity rows), and FTE notation each accept controlled vocabulary but carry no write-time constraint. V-01 extends `[FAIL: ...]` tags to all constrained fields. Selective coverage produces an inconsistent compliance surface; comprehensive coverage eliminates the inconsistency.

---

You are running a **scout-size** sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. This signal feeds `program-plan`; downstream skills parse the tier vocabulary.

**Tier vocabulary**: **LOW / MEDIUM / HIGH / XL** — exactly one. No substitutions.

This signal is produced in three phases. Each phase has a role with a charter. Complete each phase fully before reading the next.

---

### Phase 0 — Inertia Analyst

**Charter — you own exactly this section: Inertia Check.**
**Charter — you do NOT produce**: Surface Area, Complexity Tier, Primary Driver, Team-Size Signal, Timeline Signal, Confidence Level, Confidence Basis, Confidence Gap, Tier Sensitivities, Confidence Calibration.

The cost of building must be compared against the cost of NOT building before any analysis dimension is assigned. A sizing estimate produced without this baseline is calibrated against an unknown reference.

> **WRONG**: "Teams currently use spreadsheets." — Workaround named; ongoing cost absent; direction absent; key driver absent. Fails.
> **CORRECT**: "Manual CSV export + re-import per team — building is **cheaper** long-term; workaround requires ~45 min/sprint/team scaling linearly with team count. Key Driver: team-count growth makes the workaround cost non-linear."

| Workaround [Phase 0: Inertia Analyst — name the specific substitute; "None" requires cost-of-absence justification] | Ongoing Cost [Phase 0: friction absorbed today — at minimum: time or error rate] | Cost Direction [Phase 0 — FAIL: "neutral", "similar", "moderate impact", "a wash", "unclear" — exactly one: cheaper / comparable / more expensive] | Key Driver [Phase 0: one sentence — what removing the workaround actually fixes] |
|---|---|---|---|
| | | | |

---

**Phase 0 complete. Phase 1 OPENS.**

---

### Phase 1 — Sizing Analyst

**Charter — you own these fields:**
1. Surface Area (named integration points + total count)
2. Complexity Tier (LOW / MEDIUM / HIGH / XL)
3. Primary Complexity Driver (1–2 named factors)
4. Team-Size Signal (specialist disciplines + FTE fractions)
5. Timeline Signal (sprint range)
6. Confidence Level + Basis (what IS established)
7. Tier-Up Sensitivity (single named falsifiable condition → explicit tier destination)
8. Tier-Down Sensitivity (single named falsifiable condition → explicit tier destination)
9. Confidence Calibration

**Charter — you do NOT produce**: Inertia Check (Phase 0). Confidence Gap (Phase 2).

---

**PRE-FLIGHT GATE — complete before any Phase 1 analysis section**

Resolve all three fields now from repo/context. Do not fill any section below until this gate is complete. "TBD" or blank fails any field.

Out-of-scope boundary:
[Name at least one sub-system, phase, or integration explicitly NOT covered. If full scope: "No exclusions — full scope assumed." Do not say "TBD."]

Break-even signal:
[At what usage level, team count, or time horizon does building recover cost vs. continuing the workaround? Rough signal acceptable. "Cannot assess — [specific reason]" is valid.]

Preliminary hypothesis:
Tier: [LOW / MEDIUM / HIGH / XL — commit now, before any section is filled]
Timeline: [N–M sprints — commit now]
Reasoning: [one sentence — what signals the scope before detailed analysis?]

Enforcement contract:
- Scope exclusions committed here are enforced in: Surface Area (prohibits scope exclusions), Complexity (prohibits scope exclusions), Synthesis (prohibits scope exclusions).
- Preliminary hypothesis is confirmed or revised in Synthesis, which names PRE-FLIGHT GATE by label at both the anchor and the verdict.

STOP: Do not proceed to Surface Area until all three fields have specific responses.

---

#### Surface Area [Phase 1: Sizing Analyst]

> **WRONG**: "Several API layers and UI components." — No named points; no count. Fails.
> **CORRECT**: "Auth endpoint, event-bus subscription (order.placed), DB migration (orders table) — **3 integration points**"

Do not include scope exclusions here — scope was resolved in PRE-FLIGHT GATE.

| Integration Point [Phase 1: Sizing Analyst — name each individually — "several API layers" fails] | Type [API / hook / event / DB / UI / service / other] |
|---|---|
| | |
| | |
| **Total** | **[N] integration points** |

---

#### Complexity [Phase 1: Sizing Analyst]

> **WRONG tier**: "MODERATE" / "medium-high" / "3/5" — Off-vocabulary. Fails.
> **CORRECT tier**: "HIGH"
> **WRONG driver**: "Complex feature with many moving parts." — No named factor. Fails.
> **CORRECT driver**: "Cross-service transaction semantics — three services must agree on rollback without a distributed coordinator."

Do not include scope exclusions or unknowns here — scope was resolved in PRE-FLIGHT GATE; unknowns belong in Phase 2.

| Complexity Tier [Phase 1: Sizing Analyst — FAIL: MODERATE, medium-high, 3/5, or any non-vocabulary term — exactly one: LOW / MEDIUM / HIGH / XL] | Primary Driver [Phase 1: Sizing Analyst — 1–2 named causal factors — vague descriptions fail] |
|---|---|
| | |

---

#### Team-Size Signal [Phase 1: Sizing Analyst]

> **WRONG**: "3 engineers" — Disciplines not named; ownership absent. Fails.
> **CORRECT**: "1 backend engineer (owns event schema + API layer), 1 infra engineer (owns deployment pipeline), 0.5 PM (owns stakeholder coordination)"

| Specialist Discipline [Phase 1: Sizing Analyst] | FTE [Phase 1 — FAIL: "part-time", "TBD", "as needed" — numeric fraction required] | Implementation Ownership |
|---|---|---|
| | | |
| **Total** | | |

---

#### Timeline Signal [Phase 1: Sizing Analyst]

> **WRONG**: "Q3 2026" — Calendar reference. Fails.
> **WRONG**: "4 sprints" — Point estimate, not a range. Fails.
> **CORRECT**: "3–5 sprints"

| Sprint Range [Phase 1: Sizing Analyst — FAIL: any calendar reference, any single-number estimate, "a few sprints" — N–M format required] |
|---|
| |

---

#### Confidence Level + Basis [Phase 1: Sizing Analyst]

> **WRONG**: "Confidence: MEDIUM." — No basis. Fails.
> **CORRECT**: "MEDIUM — integration points bounded at three stable endpoints with documented contracts; auth coordination pattern is established."

Name only what IS established here. What is NOT yet known belongs to Phase 2.

Do not list unknowns here — unknowns belong in Phase 2 (Confidence Gap).

| Confidence Level [Phase 1: Sizing Analyst — FAIL: MEDIUM-HIGH, 3/5, "acceptable", "moderate confidence", or any non-tier label — exactly one: HIGH / MEDIUM / LOW] | Confidence Basis [Phase 1: Sizing Analyst — what IS verified — do not include what is unknown] |
|---|---|
| | |

---

#### Tier Sensitivity [Phase 1: Sizing Analyst]

> **WRONG up**: "Tier rises if the scope grows." — Not falsifiable. Fails.
> **CORRECT up**: "Tier rises to XL if real-time sync is required — confirm by reviewing the PRD sync section."
>
> **WRONG down**: "Tier drops if things simplify." — Not named; not falsifiable. Fails.
> **CORRECT down**: "Tier drops to MEDIUM if the auth layer exposes a documented webhook API — confirm by reading the auth reference."

| Direction | Single Named Condition [Phase 1: Sizing Analyst — one scenario — name what settles it] | Destination Tier [Phase 1 — FAIL: same as current tier, MODERATE, medium-high, or non-vocabulary — must differ from current tier: LOW / MEDIUM / HIGH / XL] |
|---|---|---|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

#### Confidence Calibration [Phase 1: Sizing Analyst]

| What would raise confidence [Phase 1: Sizing Analyst] | What would lower confidence [Phase 1: Sizing Analyst] |
|---|---|
| | |

---

**Phase 1 complete. Phase 2 OPENS.**

---

### Phase 2 — Risk Assessor

**Charter — you own exactly one field: Confidence Gap.**
**Charter — you do NOT produce**: Inertia Check (Phase 0), Surface Area, Complexity Tier, Primary Driver, Team-Size Signal, Timeline Signal, Confidence Level, Confidence Basis, Tier Sensitivities, Confidence Calibration (Phase 1).

**Non-access rule — prohibited content categories:**
You are explicitly prohibited from citing as the gap any of the following categories Phase 1 confirmed:
- The **integration points** the Sizing Analyst enumerated in Surface Area
- The **API contract status** the Sizing Analyst confirmed as established
- The **complexity tier drivers** the Sizing Analyst named
- The **team and timeline signals** the Sizing Analyst produced

**Self-test — apply before writing your gap:**
Ask: "Could a reader look only at Phase 1 output and derive my gap by reversing something the Sizing Analyst confirmed — turning 'X is established' into 'X has not been confirmed'?" If yes: charter violation. Name a dimension Phase 1 did not reach.

> **WRONG gap** (basis negation):
> Phase 1 basis: "Auth API contract is stable — established baseline."
> Gap: "Auth API contract has not been confirmed." — Same dimension, negated. Derivable from Phase 1 by negation. Charter violation.

> **CORRECT gap** (new dimension Phase 1 did not reach):
> Phase 1 basis: "Auth API contract is stable — three endpoints documented."
> Gap: "Auth API rate-limiting under sustained concurrent event load is undocumented — if the rate limit falls below expected event volume, a backpressure layer becomes a required integration point, expanding surface area."

| Confidence Gap [Phase 2: Risk Assessor — FAIL: any integration point Phase 1 enumerated, any contract status Phase 1 confirmed, any complexity driver Phase 1 named — must name a dimension Phase 1 did not reach — verify it cannot be derived from Phase 1 by negation before writing] |
|---|
| Gap: [specific named unknown] — [why it matters to the sizing] |

**Before finalizing your Confidence Gap**: Run the self-test again. If your gap negates anything Phase 1 confirmed, restate to name a genuinely different dimension.

---

### Output Compilation

**SIZING SIGNAL — [feature name]**

| Field | Phase | Value |
|---|---|---|
| Inertia Check | 0 | [workaround — cost direction — key driver] |
| Surface Area | 1 | [named points — N integration points] |
| Complexity Tier [FAIL: MODERATE, medium-high, 3/5 — only: LOW / MEDIUM / HIGH / XL] | 1 | [tier] |
| Primary Complexity Driver | 1 | [1–2 named factors] |
| Team-Size Signal | 1 | [disciplines + fractions] |
| Timeline Signal [FAIL: calendar reference, point estimate — only: N–M sprints] | 1 | [N–M sprints] |
| Confidence Level [FAIL: MEDIUM-HIGH, 3/5 — only: HIGH / MEDIUM / LOW] | 1 | [level — basis] |
| Confidence Gap [Phase 2 field — must name a dimension Phase 1 did not reach — not a negation of Phase 1 Confidence Basis] | 2 | [unknown — why it matters] |
| Tier-Up Sensitivity | 1 | Tier rises to [ ] if [ ] |
| Tier-Down Sensitivity | 1 | Tier drops to [ ] if [ ] |
| Confidence Calibration | 1 | [what raises / lowers confidence] |

Signal boundary check: no task breakdowns, sprint assignments, owner names, or milestone dates.

---

### Open Unknowns

> **FAILURE MODE**: "Dependencies may exist" is not an unknown — it is a hedge. Name a specific unverified dependency, decision, or contract. Do not include scope exclusions here — scope was resolved in PRE-FLIGHT GATE.

For each open unknown:
Unknown: [specific unverified item]
Impact: [complexity / timeline / team / confidence]
Movement: [what closes this unknown]

---

### Synthesis

> **FAILURE MODE**: Restating sections in sequence — "Complexity is HIGH. Timeline is 4–6 sprints. Confidence is MEDIUM." — is juxtaposition, not synthesis. The conclusion must require two or more dimensions to state.

Look back at PRE-FLIGHT GATE — the preliminary hypothesis committed there was [tier] at [N–M sprints]. State whether the analysis confirms, revises, or partially revises that commitment using a structured commitment-chain trace. All three labeled lines must appear on separate lines.

Commitment chain:
Gate commitment: [tier / sprint range from PRE-FLIGHT GATE]
Analysis: [key evidence from Phases 0–2 bearing on the commitment — name at least two dimensions]
Verdict: [exactly one of the three forms — the phrase "committed in PRE-FLIGHT GATE" is required]
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is confirmed: [cross-signal observation combining at least two dimensions]."
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is revised: [dimension] moved from [prior] to [current] because [reason]."
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is partially revised: [what held]; [what changed] because [reason]."

After the verdict, state the cross-signal directional observation combining at least two dimensions (complexity, timeline, confidence, inertia cost).

Do not include scope exclusions here — scope was resolved in PRE-FLIGHT GATE.

**STRUCTURAL AMEND RE-EVALUATION DIRECTIVE**: When AMEND is absent — confirm no active amendment and proceed. When AMEND is present and the amended dimension appears in the cross-signal conclusion or verdict — re-evaluate that conclusion before closing this section. Update it or explicitly reaffirm it still holds. This is a structural property of this section's template, not a conditional check.

---

### Per-Criterion Self-Check

Evaluate each criterion with PASS / PARTIAL / FAIL and evidence. Self-check is a separate artifact — do not collapse it into the content sections above.

**Essential criteria (C-01 through C-05):**

| ID | Criterion | Pass condition | Disqualifying form | Verdict | Evidence |
|---|---|---|---|---|---|
| C-01 | Complexity tier vocabulary | Exactly one of LOW / MEDIUM / HIGH / XL | "MODERATE", "medium-high", "3/5", "complex" as the tier label | | |
| C-02 | Timeline sprint range | N–M sprints with both bounds | Calendar date, "4 sprints" (point estimate), "a few sprints" | | |
| C-03 | Surface area quantified | Named or counted integration points (min 2, or 0–1 with reasoning) | "Moderate surface area", "several integrations" with no named points | | |
| C-04 | Inertia check present | Labeled section names workaround + at least one cost dimension | Section absent, or names only the feature without workaround | | |
| C-05 | Confidence level with basis | Level stated AND at least one reason given | "Confidence: MEDIUM" with no supporting sentence | | |

**Recommended criteria (C-06 through C-08):**

| ID | Criterion | Pass condition | Disqualifying form | Verdict | Evidence |
|---|---|---|---|---|---|
| C-06 | Team-size names specializations | At least one role or discipline named, not just headcount | "3 engineers" or "2 people" with no role labels | | |
| C-07 | Complexity justified with driver | At least one sentence names what pushed the tier | Bare tier label with no follow-on sentence | | |
| C-08 | AMEND cascades to output | If AMEND present: substantive change traceable to it; if absent: default PASS | AMEND invoked but output unchanged from non-amended run | | |

**Aspirational criteria (C-09 through C-35):**

| ID | Criterion | Pass condition | Disqualifying form | Verdict | Evidence |
|---|---|---|---|---|---|
| C-09 | Scopes what is NOT included | At least one explicit exclusion, assumption, or out-of-scope boundary | Output that names only what is included with no boundary statement | | |
| C-10 | Break-even signal | Break-even estimate OR explicit "cannot assess — [reason]" | Inertia cost described with no break-even reference | | |
| C-11 | Each specialization states ownership | At least one named role includes implementation scope | Role list with no ownership scope ("1 backend, 1 infra" only) | | |
| C-12 | Confidence names specific unknowns | At least one concrete unknown that would move confidence if resolved | "Confidence is LOW due to uncertainty" with no named unknown | | |
| C-13 | Synthesis integrates, not restates | At least one sentence cross-referencing two+ dimensions | "Complexity is HIGH. Timeline is 4–6 sprints." (sequential restatement) | | |
| C-14 | Open unknowns in dedicated section with typed fields | Named section with Unknown/Impact/Movement fields (or explicit "no open unknowns") | Unknowns embedded in confidence basis with no separate section | | |
| C-15 | Synthesis confirms or revises prior hypothesis | Prior hypothesis stated before analysis; synthesis explicitly confirms, revises, or partially revises | Synthesis that produces a conclusion matching the hypothesis with no explicit confirmation statement | | |
| C-16 | AMEND cascades to synthesis | If AMEND changes a dimension cited in synthesis: synthesis re-evaluated; if not: default PASS | AMEND changes complexity tier; synthesis cross-signal conclusion unchanged | | |
| C-17 | Aspirational sections name failure mode | At least one aspirational section names the anti-pattern being avoided | Section that avoids the failure mode without stating it | | |
| C-18 | Pre-flight gate before first dimension | Self-check / gate fires before Surface Area and before Complexity section | Inline reminder inside Surface Area ("don't forget scope") substituted for a gate | | |
| C-19 | Adjacent sections carry prohibition guards | When canonical section exists for a field type, at least one adjacent section carries explicit prohibition | Confidence basis with no prohibition against unknowns when OPEN UNKNOWNS section exists | | |
| C-20 | Complete closure mesh | Every section that could receive a canonical field type is closed from all directions | Synthesis section has no prohibition against scope exclusions when PRE-FLIGHT GATE owns scope | | |
| C-21 | Pre-flight gate elicits preliminary hypothesis | Gate requires tier + timeline commitment before first analysis section | Gate that asks for scope boundary only, with no hypothesis commitment | | |
| C-22 | Synthesis names gate at both ends | Synthesis names PRE-FLIGHT GATE when anchoring prior commitment AND when stating verdict | Synthesis references "my earlier estimate" without naming the structural label | | |
| C-23 | Prohibition guards name canonical home | At least one prohibition guard names the canonical home by label ("scope was resolved in PRE-FLIGHT GATE") | "Do not include scope here" without naming where scope belongs | | |
| C-24 | Synthesis has structured commitment-chain trace | Gate commitment, analysis evidence, and verdict on separate labeled lines (scannable, not prose paragraph) | Single prose paragraph that mentions gate, evidence, and verdict all in one sentence | | |
| C-25 | PRE-FLIGHT GATE forward-references enforcement sections | Gate names at least two downstream sections responsible for enforcing its commitments | Gate that lists scope exclusions with no mention of which sections enforce them | | |
| C-26 | Synthesis embeds AMEND re-evaluation directive | Synthesis section contains written directive requiring re-evaluation when AMEND affects a cited dimension | Synthesis with C-16 compliance behavior but no written structural directive | | |
| C-27 | Every aspirational section has FAILURE MODE block | Every aspirational section with nontrivial pass condition has dedicated labeled FAILURE MODE block | Synthesis section with anti-pattern awareness embedded in prose, no dedicated block | | |
| C-28 | Per-criterion self-check trace covering all aspirational criteria | Separate artifact evaluating each aspirational criterion by ID with pass/fail + evidence | Self-check absent from the output entirely | | |
| C-29 | Structural criteria self-check items have exact disqualifying forms | C-18 through C-27, C-33, C-35: each self-check item has both pass condition and named disqualifying form | Structural criterion self-check entry with pass condition only | | |
| C-30 | Depth/behavior criteria self-check items have exact disqualifying forms | C-09 through C-17, C-34: each item has both pass condition and named disqualifying form | Depth criterion self-check entry with pass condition only | | |
| C-31 | Self-check covers all weight classes | Self-check includes C-01 through C-08 in addition to aspirational criteria | Self-check that covers C-09-C-35 but omits essential and recommended criteria | | |
| C-32 | Essential/recommended self-check items have exact disqualifying forms | C-01 through C-08: each item has both pass condition and named disqualifying form | Essential criterion entry with pass condition and evidence but no disqualifying form | | |
| C-33 | Inertia check is structural opener | Inertia section appears before complexity tier, timeline, surface area, and confidence level fields | Inertia section appearing after PRE-FLIGHT GATE baseline tier is committed, or after Surface Area | | |
| C-34 | Inertia uses 4-field format | Inertia entry contains Workaround, Ongoing Cost, Cost Direction, and Key Driver as named fields | Inertia entry with workaround + cost direction but omitting Key Driver field | | |
| C-35 | Disqualifying forms as write-time constraint tags on all vocab-constrained fields | [FAIL: ...] tags on Complexity Tier, Timeline, Confidence Level, Cost Direction, Tier-Destination, FTE columns | Prompt with [FAIL:] tags on C-01/C-02 only; Confidence Level column untagged | | |

---

## V-02 — Axis: Inertia framing (5-field inertia format with quantified Cost Trajectory)

**Variation axis**: Inertia framing — inertia table extended from 4 fields (C-34 minimum) to 5 fields by adding Cost Trajectory (quantified rate of change alongside directional Cost Direction)

**Hypothesis**: C-34 requires four named fields including Cost Direction — a directional signal (cheaper / comparable / more expensive). Direction tells you the trend; it does not tell you how fast the trend is moving. A workaround that is "more expensive and getting worse" and one that is "more expensive but stable" have different investment urgency. Cost Trajectory adds the rate: "+~15%/quarter as team count scales", "~constant", "declining ~10%/year as tooling improves". Rate converts a static directional observation into a forecasting signal. If adopted as a v13 criterion, this becomes: "Inertia check uses a 5-field format with quantified trajectory."

---

You are running a **scout-size** sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. This signal feeds `program-plan`; downstream skills parse the tier vocabulary.

**Tier vocabulary**: **LOW / MEDIUM / HIGH / XL** — exactly one. No substitutions.

This signal is produced in three phases. Each phase has a role with a charter. Complete each phase fully before reading the next.

---

### Phase 0 — Inertia Analyst

**Charter — you own exactly this section: Inertia Check.**
**Charter — you do NOT produce**: Surface Area, Complexity Tier, Primary Driver, Team-Size Signal, Timeline Signal, Confidence Level, Confidence Basis, Confidence Gap, Tier Sensitivities, Confidence Calibration.

The cost of building must be compared against the cost of NOT building before any analysis dimension is assigned. The 5-field format establishes: what is being done today, how much it costs, whether that cost is growing or shrinking, at what rate, and what the root cause is.

> **WRONG**: "Teams use spreadsheets and it's getting worse." — Trajectory stated in prose with no rate quantification. Fails C-34 minimum (no structured format). Fails C-35 potential (no named rate field).
> **CORRECT**:
> Workaround: Manual CSV export + re-import per team
> Ongoing Cost: ~45 min/sprint/team
> Cost Direction: more expensive [to maintain vs. build]
> Cost Trajectory: worsening at +~20%/quarter as team count scales linearly
> Key Driver: team headcount growth — each new team adds a fixed workaround burden with no offset

| Workaround [Phase 0: Inertia Analyst — name the specific substitute] | Ongoing Cost [Phase 0: friction absorbed today — at minimum: time or error rate] | Cost Direction [Phase 0 — FAIL: "neutral", "similar", "a wash" — exactly one: cheaper / comparable / more expensive] | Cost Trajectory [Phase 0: quantified rate — e.g., "+~15%/quarter", "~constant", "declining ~10%/year" — directional statement without rate fails] | Key Driver [Phase 0: one causal sentence — what removing the workaround actually fixes] |
|---|---|---|---|---|
| | | | | |

---

**Phase 0 complete. Phase 1 OPENS.**

---

### Phase 1 — Sizing Analyst

**Charter — you own these fields:**
1. Surface Area (named integration points + total count)
2. Complexity Tier (LOW / MEDIUM / HIGH / XL)
3. Primary Complexity Driver (1–2 named factors)
4. Team-Size Signal (specialist disciplines + FTE fractions)
5. Timeline Signal (sprint range)
6. Confidence Level + Basis (what IS established)
7. Tier-Up Sensitivity (single named falsifiable condition → explicit tier destination)
8. Tier-Down Sensitivity (single named falsifiable condition → explicit tier destination)
9. Confidence Calibration

**Charter — you do NOT produce**: Inertia Check (Phase 0). Confidence Gap (Phase 2).

---

**PRE-FLIGHT GATE — complete before any Phase 1 analysis section**

Out-of-scope boundary:
[Name at least one sub-system or integration explicitly NOT covered. If full scope: "No exclusions — full scope assumed."]

Break-even signal:
[At what usage level, team count, or time horizon does building recover cost vs. continuing the workaround? "Cannot assess — [specific reason]" is valid.]

Preliminary hypothesis:
Tier: [LOW / MEDIUM / HIGH / XL — commit now]
Timeline: [N–M sprints — commit now]
Reasoning: [one sentence]

Enforcement contract:
- Scope exclusions enforced in: Surface Area, Complexity, Synthesis.
- Hypothesis confirmed or revised in Synthesis, naming PRE-FLIGHT GATE at anchor and verdict.

STOP: Do not proceed to Surface Area until all three fields have specific responses.

---

#### Surface Area [Phase 1: Sizing Analyst]

> **WRONG**: "Several API layers and UI components." — No named points; no count. Fails.
> **CORRECT**: "Auth endpoint, event-bus subscription (order.placed), DB migration (orders table) — **3 integration points**"

Do not include scope exclusions here — scope was resolved in PRE-FLIGHT GATE.

| Integration Point [Phase 1: Sizing Analyst — name each individually] | Type [API / hook / event / DB / UI / service / other] |
|---|---|
| | |
| **Total** | **[N] integration points** |

---

#### Complexity [Phase 1: Sizing Analyst]

> **WRONG tier**: "MODERATE" / "medium-high" / "3/5" — Off-vocabulary. Fails.
> **CORRECT tier**: "HIGH"

| Complexity Tier [Phase 1: Sizing Analyst — FAIL: MODERATE, medium-high, 3/5, or any non-vocabulary term — exactly one: LOW / MEDIUM / HIGH / XL] | Primary Driver [Phase 1: Sizing Analyst — 1–2 named causal factors] |
|---|---|
| | |

---

#### Team-Size Signal [Phase 1: Sizing Analyst]

> **WRONG**: "3 engineers" — Disciplines not named; ownership absent. Fails.
> **CORRECT**: "1 backend (owns event schema + API layer), 1 infra (owns deployment pipeline), 0.5 PM"

| Specialist Discipline [Phase 1: Sizing Analyst] | FTE | Implementation Ownership |
|---|---|---|
| | | |
| **Total** | | |

---

#### Timeline Signal [Phase 1: Sizing Analyst]

> **WRONG**: "Q3 2026" — Calendar reference. Fails.
> **WRONG**: "4 sprints" — Point estimate. Fails.
> **CORRECT**: "3–5 sprints"

| Sprint Range [Phase 1: Sizing Analyst — FAIL: calendar reference, point estimate — N–M format required] |
|---|
| |

---

#### Confidence Level + Basis [Phase 1: Sizing Analyst]

> **WRONG**: "Confidence: MEDIUM" — No basis. Fails.
> **CORRECT**: "MEDIUM — three stable endpoints with documented contracts; auth pattern established."

| Confidence Level [Phase 1: Sizing Analyst — FAIL: MEDIUM-HIGH, 3/5, "acceptable" — exactly one: HIGH / MEDIUM / LOW] | Confidence Basis [Phase 1: what IS verified — do not include unknowns] |
|---|---|
| | |

---

#### Tier Sensitivity [Phase 1: Sizing Analyst]

| Direction | Single Named Condition [Phase 1: Sizing Analyst] | Destination Tier [Phase 1 — FAIL: same as current tier, non-vocabulary term — must differ from current: LOW / MEDIUM / HIGH / XL] |
|---|---|---|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

#### Confidence Calibration [Phase 1: Sizing Analyst]

| What would raise confidence | What would lower confidence |
|---|---|
| | |

---

**Phase 1 complete. Phase 2 OPENS.**

---

### Phase 2 — Risk Assessor

**Charter — you own exactly one field: Confidence Gap.**
**Charter — you do NOT produce**: Inertia Check (Phase 0), all Phase 1 fields.

**Non-access rule**: You are prohibited from citing as the gap: integration points Phase 1 enumerated, API contract status Phase 1 confirmed, complexity drivers Phase 1 named, team/timeline signals Phase 1 produced.

**Self-test**: "Could a reader derive my gap from Phase 1 by negating something Phase 1 confirmed?" If yes: charter violation. Name a dimension Phase 1 did not reach.

> **WRONG gap**: "Auth API contract has not been confirmed." — Derivable from Phase 1 by negation. Charter violation.
> **CORRECT gap**: "Auth API rate-limiting under concurrent event load is undocumented — backpressure layer may become a required integration point." — Phase 1 did not reach this dimension.

| Confidence Gap [Phase 2: Risk Assessor — must name a dimension Phase 1 did not reach — not derivable from Phase 1 by negation] |
|---|
| Gap: [specific named unknown] — [why it matters] |

**Before finalizing**: Run the self-test again. Restate if gap negates Phase 1.

---

### Output Compilation

**SIZING SIGNAL — [feature name]**

| Field | Phase | Value |
|---|---|---|
| Inertia Check (5-field) | 0 | [workaround] / [ongoing cost] / [cost direction] / [cost trajectory] / [key driver] |
| Surface Area | 1 | [named points — N integration points] |
| Complexity Tier [FAIL: MODERATE, medium-high, 3/5] | 1 | [tier] |
| Primary Complexity Driver | 1 | [1–2 named factors] |
| Team-Size Signal | 1 | [disciplines + fractions] |
| Timeline Signal [FAIL: calendar reference, point estimate] | 1 | [N–M sprints] |
| Confidence Level [FAIL: MEDIUM-HIGH, 3/5] | 1 | [level — basis] |
| Confidence Gap [must name dimension Phase 1 did not reach] | 2 | [unknown — why it matters] |
| Tier-Up Sensitivity | 1 | Tier rises to [ ] if [ ] |
| Tier-Down Sensitivity | 1 | Tier drops to [ ] if [ ] |
| Confidence Calibration | 1 | [what raises / lowers confidence] |

---

### Open Unknowns

> **FAILURE MODE**: Named hedges ("dependencies may exist") are not unknowns. Each entry must name a specific unverified item. Do not include scope exclusions — scope was resolved in PRE-FLIGHT GATE.

Unknown: / Impact: / Movement: [for each; or: "No open unknowns."]

---

### Synthesis

> **FAILURE MODE**: Sequential restatement is not synthesis. The conclusion must require two dimensions to state.

Commitment chain:
Gate commitment: [tier / sprint range from PRE-FLIGHT GATE]
Analysis: [key evidence from Phases 0–2 — at least two dimensions]
Verdict: [one of the three exact forms; "committed in PRE-FLIGHT GATE" required]

After the verdict, state the cross-signal directional observation.

**STRUCTURAL AMEND RE-EVALUATION DIRECTIVE**: When AMEND is absent — confirm no active amendment and proceed. When AMEND is present and the amended dimension appears in the cross-signal conclusion or verdict — re-evaluate that conclusion before closing.

---

### Per-Criterion Self-Check

*(Same structure as V-01 self-check above; C-34 disqualifying form updated to:)*

**C-34** — Inertia uses 4-field format: Pass condition: Workaround, Ongoing Cost, Cost Direction, AND Key Driver all present as named fields. Disqualifying form: Workaround + cost named, Cost Direction present, but Cost Trajectory field absent (V-02 extends to 5-field; C-34 minimum is 4 — V-02 passes C-34 by exceeding it). | | |

*(All other C-01 through C-35 entries identical to V-01 self-check.)*

---

## V-03 — Axis: Lifecycle emphasis (PHASE SEALED blocks with completion checklists)

**Variation axis**: Lifecycle emphasis — explicit PHASE N SEALED close-out blocks with field-completion checklists inserted between each phase transition

**Hypothesis**: R11 V-05 phase transitions use verbal handoffs: "Phase N complete. Proceed to Phase N+1." A verbal handoff provides no structural confirmation that all charter deliverables were actually populated. A model can technically read "Phase 0 complete" and proceed with an empty inertia table. PHASE SEALED blocks require explicit per-field confirmation before the next phase opens — each charter deliverable is listed with a checkbox, and the prompt declares the phase closed only when all boxes are confirmed. This creates two benefits: (1) silent phase-boundary violations become structurally impossible because the checklist makes omission visible; (2) the sealed record is an auditable artifact proving all phase commitments were honored.

---

You are running a **scout-size** sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. This signal feeds `program-plan`; downstream skills parse the tier vocabulary.

**Tier vocabulary**: **LOW / MEDIUM / HIGH / XL** — exactly one. No substitutions.

This signal is produced in three phases. Complete each phase's SEALED block before reading the next phase.

---

### Phase 0 — Inertia Analyst

**Charter — you own exactly this section: Inertia Check.**
**Charter — you do NOT produce**: Surface Area, Complexity Tier, Primary Driver, Team-Size Signal, Timeline Signal, Confidence Level, Confidence Basis, Confidence Gap, Tier Sensitivities, Confidence Calibration.

> **WRONG**: "Teams use spreadsheets." — Workaround named; cost, direction, key driver absent. Fails.
> **CORRECT**: "Manual CSV export + re-import — building is **cheaper** long-term; ~45 min/sprint/team scaling with team count. Key Driver: team-count growth makes workaround cost non-linear."

| Workaround [Phase 0: Inertia Analyst — name the specific substitute] | Ongoing Cost [Phase 0: friction absorbed today] | Cost Direction [Phase 0 — FAIL: "neutral", "similar" — exactly one: cheaper / comparable / more expensive] | Key Driver [Phase 0: one causal sentence] |
|---|---|---|---|
| | | | |

---

```
── PHASE 0 SEALED ──

Before Phase 1 opens, confirm ALL of the following:

  [ ] Workaround is specifically named (not vague — "spreadsheets" is named; "manual process" is not)
  [ ] Ongoing Cost has at least one dimension (time, error rate, or manual effort)
  [ ] Cost Direction uses exact vocabulary: cheaper / comparable / more expensive
  [ ] Key Driver names the causal factor (not a restatement of the cost)

If any item is unchecked: complete Phase 0 before proceeding.

Phase 1 OPENS only when all four items are confirmed.
── PHASE 0 CLOSED ──
```

---

### Phase 1 — Sizing Analyst

**Charter — you own these fields:**
1. Surface Area (named integration points + total count)
2. Complexity Tier (LOW / MEDIUM / HIGH / XL)
3. Primary Complexity Driver (1–2 named factors)
4. Team-Size Signal (specialist disciplines + FTE fractions)
5. Timeline Signal (sprint range)
6. Confidence Level + Basis
7. Tier-Up Sensitivity
8. Tier-Down Sensitivity
9. Confidence Calibration

**Charter — you do NOT produce**: Inertia Check (Phase 0). Confidence Gap (Phase 2).

---

**PRE-FLIGHT GATE — complete before any Phase 1 analysis section**

Out-of-scope boundary: [at least one named exclusion, or "No exclusions — full scope assumed."]
Break-even signal: [at what usage level / team count building recovers cost, or "Cannot assess — [reason]"]
Preliminary hypothesis:
  Tier: [LOW / MEDIUM / HIGH / XL — commit now]
  Timeline: [N–M sprints — commit now]
  Reasoning: [one sentence]

Enforcement contract:
- Scope exclusions enforced in: Surface Area (prohibits scope exclusions), Complexity (prohibits scope exclusions), Synthesis (prohibits scope exclusions).
- Hypothesis confirmed or revised in Synthesis, naming PRE-FLIGHT GATE at anchor and verdict.

STOP: Do not proceed until all three fields have specific responses.

---

#### Surface Area [Phase 1: Sizing Analyst]

> **WRONG**: "Several API layers." — No named points; no count. Fails.
> **CORRECT**: "Auth endpoint, event-bus subscription (order.placed), DB migration — **3 integration points**"

Do not include scope exclusions here — scope was resolved in PRE-FLIGHT GATE.

| Integration Point [Phase 1: Sizing Analyst — name each individually] | Type [API / hook / event / DB / UI / service / other] |
|---|---|
| | |
| **Total** | **[N] integration points** |

---

#### Complexity [Phase 1: Sizing Analyst]

> **WRONG tier**: "MODERATE" / "medium-high" — Off-vocabulary. Fails.

| Complexity Tier [Phase 1: Sizing Analyst — FAIL: MODERATE, medium-high, 3/5 — exactly one: LOW / MEDIUM / HIGH / XL] | Primary Driver [Phase 1: 1–2 named causal factors] |
|---|---|
| | |

---

#### Team-Size Signal [Phase 1: Sizing Analyst]

| Specialist Discipline [Phase 1: Sizing Analyst] | FTE | Implementation Ownership |
|---|---|---|
| | | |
| **Total** | | |

---

#### Timeline Signal [Phase 1: Sizing Analyst]

> **WRONG**: "Q3" — Calendar. "4 sprints" — Point estimate. Fails.

| Sprint Range [Phase 1: Sizing Analyst — FAIL: calendar reference, point estimate — N–M format required] |
|---|
| |

---

#### Confidence Level + Basis [Phase 1: Sizing Analyst]

| Confidence Level [Phase 1: Sizing Analyst — FAIL: MEDIUM-HIGH, 3/5 — exactly one: HIGH / MEDIUM / LOW] | Confidence Basis [what IS verified — do not include unknowns] |
|---|---|
| | |

---

#### Tier Sensitivity [Phase 1: Sizing Analyst]

| Direction | Single Named Condition | Destination Tier [must differ from current: LOW / MEDIUM / HIGH / XL] |
|---|---|---|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

#### Confidence Calibration [Phase 1: Sizing Analyst]

| What would raise confidence | What would lower confidence |
|---|---|
| | |

---

```
── PHASE 1 SEALED ──

Before Phase 2 opens, confirm ALL of the following:

  [ ] Surface Area: at least 2 named integration points with a total count
  [ ] Complexity Tier: exactly one of LOW / MEDIUM / HIGH / XL (no other form)
  [ ] Primary Driver: at least one named causal factor (not a vague description)
  [ ] Team-Size Signal: at least one specialist discipline named (not just headcount)
  [ ] Timeline Signal: sprint range in N–M format (not a calendar date, not a point estimate)
  [ ] Confidence Level: exactly one of HIGH / MEDIUM / LOW with at least one basis sentence
  [ ] Tier-Up Sensitivity: one named falsifiable condition with a higher destination tier
  [ ] Tier-Down Sensitivity: one named falsifiable condition with a lower destination tier
  [ ] Confidence Calibration: at least one entry per column

If any item is unchecked: complete Phase 1 before proceeding.

Phase 2 OPENS only when all nine items are confirmed.
── PHASE 1 CLOSED ──
```

---

### Phase 2 — Risk Assessor

**Charter — you own exactly one field: Confidence Gap.**
**Charter — you do NOT produce**: Inertia Check (Phase 0), all Phase 1 fields.

**Non-access rule**: Prohibited from citing as the gap: integration points Phase 1 enumerated, API contract status Phase 1 confirmed, complexity drivers Phase 1 named, team/timeline signals Phase 1 produced.

**Self-test**: "Could a reader derive my gap from Phase 1 by negating something Phase 1 confirmed?" If yes: charter violation.

> **WRONG gap**: "Auth API contract has not been confirmed." — Basis negation. Charter violation.
> **CORRECT gap**: "Auth API rate-limiting under concurrent event load is undocumented — backpressure layer may become required." — Phase 1 did not reach this dimension.

| Confidence Gap [Phase 2: Risk Assessor — must name a dimension Phase 1 did not reach — not derivable from Phase 1 by negation] |
|---|
| Gap: [specific named unknown] — [why it matters] |

**Before finalizing**: Run the self-test again.

---

```
── PHASE 2 SEALED ──

Before Output Compilation, confirm the following:

  [ ] Confidence Gap names a specific unknown (not a category hedge)
  [ ] Gap cannot be derived from Phase 1 Confidence Basis by negation
  [ ] Gap names the dimension Phase 1 did not reach

If any item is unchecked: restate the gap before proceeding.

Output Compilation OPENS only when all three items are confirmed.
── PHASE 2 CLOSED ──
```

---

### Output Compilation

**SIZING SIGNAL — [feature name]**

| Field | Phase | Value |
|---|---|---|
| Inertia Check | 0 | [workaround — cost direction — key driver] |
| Surface Area | 1 | [named points — N integration points] |
| Complexity Tier [FAIL: MODERATE, medium-high, 3/5] | 1 | [tier] |
| Primary Complexity Driver | 1 | [1–2 named factors] |
| Team-Size Signal | 1 | [disciplines + fractions] |
| Timeline Signal [FAIL: calendar reference, point estimate] | 1 | [N–M sprints] |
| Confidence Level [FAIL: MEDIUM-HIGH, 3/5] | 1 | [level — basis] |
| Confidence Gap [must name dimension Phase 1 did not reach] | 2 | [unknown — why it matters] |
| Tier-Up Sensitivity | 1 | Tier rises to [ ] if [ ] |
| Tier-Down Sensitivity | 1 | Tier drops to [ ] if [ ] |
| Confidence Calibration | 1 | [what raises / lowers confidence] |

---

### Open Unknowns

> **FAILURE MODE**: Named hedges are not unknowns. Each entry names a specific unverified item. Do not include scope exclusions — scope was resolved in PRE-FLIGHT GATE.

Unknown: / Impact: / Movement: [for each; or: "No open unknowns."]

---

### Synthesis

> **FAILURE MODE**: Sequential restatement is not synthesis.

Commitment chain:
Gate commitment: [tier / sprint range from PRE-FLIGHT GATE]
Analysis: [evidence from Phases 0–2 — at least two dimensions]
Verdict: [one exact form; "committed in PRE-FLIGHT GATE" required]

Cross-signal directional observation after the verdict.

**STRUCTURAL AMEND RE-EVALUATION DIRECTIVE**: When AMEND is absent — confirm no active amendment and proceed. When AMEND is present and amended dimension appears in cross-signal conclusion — re-evaluate before closing.

---

### Per-Criterion Self-Check

*(Same structure as V-01 self-check; C-35 disqualifying form reflects V-03 minimum coverage: C-01/C-02 + C-34 Cost Direction column carry [FAIL:] tags; no full-field extension in V-03. C-35 PASS: complexity tier + timeline carry constraint tags. C-35 DISQUALIFYING FORM: no [FAIL:] tags on any column header at all.)*

*(All other entries identical to V-01 self-check.)*

---

## V-04 — Combined: Output format + Lifecycle emphasis (V-01 + V-03)

**Variation axis**: Output format (C-35 extended to all vocab-constrained fields) + Lifecycle emphasis (PHASE SEALED blocks)

**Hypothesis**: V-01 prevents vocabulary violations at write time through comprehensive [FAIL: ...] constraint tags; V-03 prevents phase-completion violations at transition time through PHASE SEALED checklists. These address orthogonal failure modes. Combined, they create a two-layer prevention system: field-level prevention (tags) and phase-level prevention (sealed blocks). The hypothesis: a model operating under both systems encounters write-time constraint enforcement AND close-out enforcement, reducing both vocabulary drift and silent phase incompleteness simultaneously. Neither system interferes with the other's mechanism; the overhead is additive but not redundant.

---

You are running a **scout-size** sizing signal — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates. This signal feeds `program-plan`; downstream skills parse the tier vocabulary.

**Tier vocabulary**: **LOW / MEDIUM / HIGH / XL** — exactly one. No substitutions.

This signal is produced in three phases. Each phase has a SEALED close-out block that must be confirmed before the next phase opens.

---

### Phase 0 — Inertia Analyst

**Charter — you own exactly this section: Inertia Check.**
**Charter — you do NOT produce**: Surface Area, Complexity Tier, Primary Driver, Team-Size Signal, Timeline Signal, Confidence Level, Confidence Basis, Confidence Gap, Tier Sensitivities, Confidence Calibration.

> **WRONG**: "Teams use manual exports." — No cost direction; no key driver. Fails.
> **CORRECT**: "Manual CSV export + re-import — building is **cheaper** long-term; ~45 min/sprint/team. Key Driver: team-count growth makes the workaround cost non-linear."

| Workaround [Phase 0: Inertia Analyst — name the specific substitute] | Ongoing Cost [Phase 0: friction today — at minimum: time or error rate] | Cost Direction [Phase 0 — FAIL: "neutral", "similar", "moderate impact", "a wash" — exactly one: cheaper / comparable / more expensive] | Key Driver [Phase 0: one causal sentence — what removing this fixes] |
|---|---|---|---|
| | | | |

---

```
── PHASE 0 SEALED ──

  [ ] Workaround is specifically named
  [ ] Ongoing Cost has at least one dimension
  [ ] Cost Direction uses exact vocabulary: cheaper / comparable / more expensive
  [ ] Key Driver names the causal factor

Phase 1 OPENS only when all four items are confirmed.
── PHASE 0 CLOSED ──
```

---

### Phase 1 — Sizing Analyst

**Charter — you own these fields:**
1. Surface Area (named integration points + total count)
2. Complexity Tier (LOW / MEDIUM / HIGH / XL)
3. Primary Complexity Driver (1–2 named factors)
4. Team-Size Signal (specialist disciplines + FTE fractions + ownership)
5. Timeline Signal (sprint range)
6. Confidence Level + Basis
7. Tier-Up Sensitivity
8. Tier-Down Sensitivity
9. Confidence Calibration

**Charter — you do NOT produce**: Inertia Check (Phase 0). Confidence Gap (Phase 2).

---

**PRE-FLIGHT GATE — complete before any Phase 1 analysis section**

Out-of-scope boundary: [at least one named exclusion, or "No exclusions — full scope assumed."]
Break-even signal: [at what level building recovers cost, or "Cannot assess — [reason]"]
Preliminary hypothesis:
  Tier: [LOW / MEDIUM / HIGH / XL — commit now]
  Timeline: [N–M sprints — commit now]
  Reasoning: [one sentence]

Enforcement contract:
- Scope exclusions enforced in: Surface Area (prohibits scope exclusions), Complexity (prohibits scope exclusions), Synthesis (prohibits scope exclusions).
- Hypothesis confirmed or revised in Synthesis, naming PRE-FLIGHT GATE at anchor and verdict.

STOP: Do not proceed until gate is complete.

---

#### Surface Area [Phase 1: Sizing Analyst]

> **WRONG**: "Several API layers." — No named points; no count. Fails.
> **CORRECT**: "Auth endpoint, event-bus subscription (order.placed), DB migration — **3 integration points**"

Do not include scope exclusions here — scope was resolved in PRE-FLIGHT GATE.

| Integration Point [Phase 1: Sizing Analyst — name each individually] | Type [API / hook / event / DB / UI / service / other] |
|---|---|
| | |
| **Total** | **[N] integration points** |

---

#### Complexity [Phase 1: Sizing Analyst]

> **WRONG tier**: "MODERATE" / "medium-high" / "3/5" — Off-vocabulary. Fails.

| Complexity Tier [Phase 1: Sizing Analyst — FAIL: MODERATE, medium-high, 3/5, or any non-vocabulary term — exactly one: LOW / MEDIUM / HIGH / XL] | Primary Driver [Phase 1: 1–2 named causal factors — vague descriptions fail] |
|---|---|
| | |

---

#### Team-Size Signal [Phase 1: Sizing Analyst]

| Specialist Discipline [Phase 1: Sizing Analyst] | FTE [Phase 1 — FAIL: "part-time", "TBD", "as needed" — numeric fraction required] | Implementation Ownership |
|---|---|---|
| | | |
| **Total** | | |

---

#### Timeline Signal [Phase 1: Sizing Analyst]

| Sprint Range [Phase 1: Sizing Analyst — FAIL: any calendar reference, any point estimate — N–M format required] |
|---|
| |

---

#### Confidence Level + Basis [Phase 1: Sizing Analyst]

| Confidence Level [Phase 1: Sizing Analyst — FAIL: MEDIUM-HIGH, 3/5, "acceptable", "moderate confidence" — exactly one: HIGH / MEDIUM / LOW] | Confidence Basis [what IS verified — do not include unknowns] |
|---|---|
| | |

---

#### Tier Sensitivity [Phase 1: Sizing Analyst]

| Direction | Single Named Condition [Phase 1: one scenario] | Destination Tier [Phase 1 — FAIL: same as current, MODERATE, or non-vocabulary — must differ: LOW / MEDIUM / HIGH / XL] |
|---|---|---|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

#### Confidence Calibration [Phase 1: Sizing Analyst]

| What would raise confidence [Phase 1] | What would lower confidence [Phase 1] |
|---|---|
| | |

---

```
── PHASE 1 SEALED ──

  [ ] Surface Area: at least 2 named integration points with total count
  [ ] Complexity Tier: exactly LOW / MEDIUM / HIGH / XL
  [ ] Primary Driver: at least one named causal factor
  [ ] Team-Size: at least one discipline named with FTE
  [ ] Timeline: N–M sprint range (not calendar, not point estimate)
  [ ] Confidence Level + Basis: level + at least one basis sentence
  [ ] Tier-Up Sensitivity: one falsifiable condition + higher destination tier
  [ ] Tier-Down Sensitivity: one falsifiable condition + lower destination tier
  [ ] Confidence Calibration: at least one entry per column

Phase 2 OPENS only when all nine items are confirmed.
── PHASE 1 CLOSED ──
```

---

### Phase 2 — Risk Assessor

**Charter — you own exactly one field: Confidence Gap.**
**Charter — you do NOT produce**: Inertia Check (Phase 0), all Phase 1 fields.

**Non-access rule**: Prohibited from citing as the gap: integration points Phase 1 enumerated, API contract status Phase 1 confirmed, complexity drivers Phase 1 named, team/timeline signals Phase 1 produced.

**Self-test**: "Could a reader derive my gap from Phase 1 by negation?" If yes: charter violation.

> **WRONG gap**: "Auth API contract has not been confirmed." — Basis negation. Charter violation.
> **CORRECT gap**: "Auth API rate-limiting under concurrent event load is undocumented — backpressure layer may become required." — New dimension.

| Confidence Gap [Phase 2: Risk Assessor — FAIL: any dimension Phase 1 confirmed — must name a dimension Phase 1 did not reach — not derivable by negation] |
|---|
| Gap: [specific named unknown] — [why it matters] |

**Before finalizing**: Run the self-test again.

---

```
── PHASE 2 SEALED ──

  [ ] Gap names a specific unknown (not a hedge)
  [ ] Gap cannot be derived from Phase 1 Confidence Basis by negation
  [ ] Gap names the dimension Phase 1 did not reach

Output Compilation OPENS only when all three items are confirmed.
── PHASE 2 CLOSED ──
```

---

### Output Compilation

**SIZING SIGNAL — [feature name]**

| Field | Phase | Value |
|---|---|---|
| Inertia Check | 0 | [workaround — cost direction — key driver] |
| Surface Area | 1 | [named points — N integration points] |
| Complexity Tier [FAIL: MODERATE, medium-high, 3/5 — only: LOW / MEDIUM / HIGH / XL] | 1 | [tier] |
| Primary Complexity Driver | 1 | [1–2 named factors] |
| Team-Size Signal | 1 | [disciplines + fractions] |
| Timeline Signal [FAIL: calendar reference, point estimate — only: N–M sprints] | 1 | [N–M sprints] |
| Confidence Level [FAIL: MEDIUM-HIGH, 3/5 — only: HIGH / MEDIUM / LOW] | 1 | [level — basis] |
| Confidence Gap [must name dimension Phase 1 did not reach] | 2 | [unknown — why it matters] |
| Tier-Up Sensitivity | 1 | Tier rises to [ ] if [ ] |
| Tier-Down Sensitivity | 1 | Tier drops to [ ] if [ ] |
| Confidence Calibration | 1 | [what raises / lowers confidence] |

---

### Open Unknowns

> **FAILURE MODE**: Named hedges are not unknowns. Do not include scope exclusions — scope was resolved in PRE-FLIGHT GATE.

Unknown: / Impact: / Movement: [for each; or: "No open unknowns."]

---

### Synthesis

> **FAILURE MODE**: Sequential restatement is not synthesis.

Commitment chain:
Gate commitment: [tier / sprint range from PRE-FLIGHT GATE]
Analysis: [evidence from Phases 0–2 — at least two dimensions]
Verdict: [one exact form; "committed in PRE-FLIGHT GATE" required]

**STRUCTURAL AMEND RE-EVALUATION DIRECTIVE**: When AMEND is absent — confirm no active amendment and proceed. When AMEND is present and amended dimension appears in cross-signal conclusion — re-evaluate before closing.

---

### Per-Criterion Self-Check

*(C-35 disqualifying form: tags present on C-01/C-02 and all vocab-constrained fields; DISQUALIFYING FORM: any vocabulary-constrained field header that carries no [FAIL:] tag.)*
*(PHASE SEALED self-check note: C-29 and C-30 entries note that sealed blocks are structural artifacts; their absence would be a structural gap detectable in this self-check.)*

*(All other entries identical to V-01 self-check.)*

---

## V-05 — Combined: All axes + phrasing register (C-35 all fields + 5-field inertia + PHASE SEALED + examiner voice)

**Variation axis**: Output format (C-35 all fields) + Inertia framing (5-field with Cost Trajectory) + Lifecycle emphasis (PHASE SEALED blocks) + Phrasing register (examiner voice — third-person institutional)

**Hypothesis**: Maximum structural and vocabulary encoding. The first four axes address: (1) write-time constraint coverage, (2) inertia analysis depth, (3) phase-transition integrity, and (4) all combined. Phrasing register is the fourth single-axis dimension not yet explored. Examiner voice shifts from second-person imperative ("You are running...") to third-person institutional: "The Sizing Engineer produces a scout-size signal for the named feature. The following phases govern production." The hypothesis: second-person imperative makes the constraint feel like instruction to the reader; third-person institutional makes it feel like a specification the output must satisfy. The register shift may change the model's orientation from rule-follower to specification-satisfier, producing stronger compliance at maximum encoding density where individual constraints compete for attention.

---

The Sizing Engineer produces a **scout-size** sizing signal for the named feature — not a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates appear in this signal. The signal feeds `program-plan`; downstream parsers depend on exact tier vocabulary.

**Tier vocabulary governs all tier fields**: **LOW / MEDIUM / HIGH / XL** — exactly one form. Any other phrasing invalidates the field.

This signal is produced in three phases. Each phase is governed by a role charter. Phase N does not open until Phase N-1 is SEALED. The SEALED block is not optional — it is a structural gate.

---

### Phase 0 — Inertia Analyst

**Charter governs this role. The Inertia Analyst produces exactly one section: Inertia Check.**
**The Inertia Analyst does NOT produce**: Surface Area, Complexity Tier, Primary Driver, Team-Size Signal, Timeline Signal, Confidence Level, Confidence Basis, Confidence Gap, Tier Sensitivities, Confidence Calibration.

The build-cost estimate is undefined without a status-quo baseline. The Inertia Check establishes: what the team currently does without this feature, what it costs, the directional trend of that cost, the rate at which the trend is moving, and the causal factor driving it. The five-field format encodes all five dimensions.

> **WRONG**: "Teams use manual exports and things are getting harder." — Ongoing cost absent; direction absent; trajectory absent (rate unquantified); key driver absent. Fails all precision criteria.
> **CORRECT**:
> Workaround: Manual CSV export + re-import, one cycle per sprint per team
> Ongoing Cost: ~45 min/sprint/team
> Cost Direction: more expensive [to maintain vs. build]
> Cost Trajectory: worsening at +~20%/quarter as team count scales
> Key Driver: team-count growth — each new team adds a fixed workaround burden; building eliminates the per-team variable

| Workaround [Inertia Analyst — name the specific substitute; "None" requires cost-of-absence justification] | Ongoing Cost [Inertia Analyst — friction absorbed today — at minimum: time or error rate] | Cost Direction [Inertia Analyst — FAIL: "neutral", "similar", "a wash", "moderate impact", any paraphrase — exactly one: cheaper / comparable / more expensive] | Cost Trajectory [Inertia Analyst — FAIL: directional statement without rate ("getting worse" alone fails) — quantified rate required: "+~N%/quarter", "~constant", "declining ~N%/year"] | Key Driver [Inertia Analyst — one causal sentence — what removing the workaround fixes at the root] |
|---|---|---|---|---|
| | | | | |

---

```
── PHASE 0 SEALED ──

The Inertia Analyst confirms ALL of the following before Phase 1 opens:

  [ ] Workaround: specifically named (not a category label)
  [ ] Ongoing Cost: at least one dimension present (time, error rate, or manual effort)
  [ ] Cost Direction: exactly one of: cheaper / comparable / more expensive
  [ ] Cost Trajectory: quantified rate present (not directional statement alone)
  [ ] Key Driver: names the causal factor (not a restatement of the cost)

Phase 1 does NOT open until all five items are confirmed.
── PHASE 0 CLOSED ──
```

---

### Phase 1 — Sizing Analyst

**Charter governs this role. The Sizing Analyst produces these fields:**
1. Surface Area (named integration points + total count)
2. Complexity Tier (LOW / MEDIUM / HIGH / XL)
3. Primary Complexity Driver (1–2 named factors)
4. Team-Size Signal (specialist disciplines + FTE fractions + ownership)
5. Timeline Signal (sprint range)
6. Confidence Level + Basis (what IS established)
7. Tier-Up Sensitivity (single named falsifiable condition → explicit higher tier)
8. Tier-Down Sensitivity (single named falsifiable condition → explicit lower tier)
9. Confidence Calibration

**The Sizing Analyst does NOT produce**: Inertia Check (governed by Phase 0). Confidence Gap (governed by Phase 2).

---

**PRE-FLIGHT GATE — the Sizing Analyst resolves these preconditions before any analysis field is populated**

Out-of-scope boundary:
[Name at least one sub-system, phase, or integration explicitly NOT covered. If full scope: "No exclusions — full scope assumed." "TBD" fails this field.]

Break-even signal:
[At what usage level, team count, or time horizon does building recover cost vs. the workaround? "Cannot assess — [specific reason]" is valid. Absence fails C-10.]

Preliminary hypothesis:
Tier: [LOW / MEDIUM / HIGH / XL — committed before any analysis field is populated]
Timeline: [N–M sprints — committed before any analysis field is populated]
Reasoning: [one sentence — what signals scope at this pre-analysis stage]

Enforcement contract:
- Scope exclusions committed here are enforced in: Surface Area (prohibits scope exclusions), Complexity (prohibits scope exclusions), Synthesis (prohibits scope exclusions).
- Preliminary hypothesis is confirmed or revised in Synthesis; Synthesis names PRE-FLIGHT GATE by label at the commitment anchor and at the verdict close.

The Sizing Analyst does not populate any field below until this gate contains specific responses.

---

#### Surface Area [Sizing Analyst]

> **WRONG**: "Several API layers and UI integrations." — No named points; no count. Fails.
> **CORRECT**: "Auth endpoint, event-bus subscription (order.placed), DB migration (orders table) — **3 integration points**"

Scope exclusions do not appear here — scope was resolved in PRE-FLIGHT GATE.

| Integration Point [Sizing Analyst — name each individually — "several API layers" fails] | Type [API / hook / event / DB / UI / service / other] |
|---|---|
| | |
| | |
| **Total** | **[N] integration points** |

---

#### Complexity [Sizing Analyst]

> **WRONG tier**: "MODERATE" / "medium-high" / "3/5" — Off-vocabulary. The field is invalid.
> **CORRECT tier**: "HIGH"
> **WRONG driver**: "Complex feature with multiple dependencies." — No named factor. Fails.
> **CORRECT driver**: "Cross-service transaction semantics — three services must agree on rollback without a distributed coordinator."

Scope exclusions and unknowns do not appear here — scope was resolved in PRE-FLIGHT GATE; unknowns are governed by Phase 2.

| Complexity Tier [Sizing Analyst — FAIL: MODERATE, medium-high, 3/5, or any non-vocabulary term — exactly one: LOW / MEDIUM / HIGH / XL] | Primary Driver [Sizing Analyst — 1–2 named causal factors — vague descriptions fail] |
|---|---|
| | |

---

#### Team-Size Signal [Sizing Analyst]

> **WRONG**: "3 engineers" — Disciplines absent; ownership absent. Fails.
> **CORRECT**: "1 backend (owns event schema + API layer), 1 infra (owns deployment pipeline), 0.5 PM (owns stakeholder coordination)"

| Specialist Discipline [Sizing Analyst] | FTE [Sizing Analyst — FAIL: "part-time", "TBD", "as needed" — numeric fraction required] | Implementation Ownership [Sizing Analyst — what this role owns] |
|---|---|---|
| | | |
| **Total** | | |

---

#### Timeline Signal [Sizing Analyst]

> **WRONG**: "Q3 2026" — Calendar reference. The field is invalid.
> **WRONG**: "4 sprints" — Point estimate. The field is invalid.
> **CORRECT**: "3–5 sprints"

| Sprint Range [Sizing Analyst — FAIL: any calendar reference, any single-number estimate, "a few sprints" — N–M format is the only valid form] |
|---|
| |

---

#### Confidence Level + Basis [Sizing Analyst]

> **WRONG**: "Confidence: MEDIUM." — No basis. Fails.
> **CORRECT**: "MEDIUM — three stable endpoints with documented contracts; auth coordination pattern is established."

What IS established is named here. What is NOT yet known is governed by Phase 2.

| Confidence Level [Sizing Analyst — FAIL: MEDIUM-HIGH, 3/5, "acceptable", "moderate confidence", or any non-tier label — exactly one: HIGH / MEDIUM / LOW] | Confidence Basis [Sizing Analyst — what IS verified — unknowns do not appear here] |
|---|---|
| | |

---

#### Tier Sensitivity [Sizing Analyst]

> **WRONG up**: "Tier rises if scope expands." — Not falsifiable. Fails.
> **CORRECT up**: "Tier rises to XL if real-time sync is required — confirm by reviewing the PRD sync section."

| Direction | Single Named Condition [Sizing Analyst — one scenario — name what settles it] | Destination Tier [Sizing Analyst — FAIL: same as current tier, MODERATE, medium-high, or non-vocabulary — must differ from current tier: LOW / MEDIUM / HIGH / XL] |
|---|---|---|
| Tier-up | | Tier rises to [ ] |
| Tier-down | | Tier drops to [ ] |

---

#### Confidence Calibration [Sizing Analyst]

| What would raise confidence [Sizing Analyst] | What would lower confidence [Sizing Analyst] |
|---|---|
| | |

---

```
── PHASE 1 SEALED ──

The Sizing Analyst confirms ALL of the following before Phase 2 opens:

  [ ] Surface Area: at least 2 named integration points with a numeric total
  [ ] Complexity Tier: exactly one of LOW / MEDIUM / HIGH / XL (no other form present)
  [ ] Primary Driver: at least one named causal factor (not a description of complexity)
  [ ] Team-Size: at least one specialist discipline named with numeric FTE
  [ ] Timeline: sprint range in N–M format (calendar and point estimates disqualify)
  [ ] Confidence Level + Basis: one of HIGH / MEDIUM / LOW with at least one basis sentence
  [ ] Tier-Up Sensitivity: one named falsifiable condition with destination tier higher than current
  [ ] Tier-Down Sensitivity: one named falsifiable condition with destination tier lower than current
  [ ] Confidence Calibration: at least one entry in each column

Phase 2 does NOT open until all nine items are confirmed.
── PHASE 1 CLOSED ──
```

---

### Phase 2 — Risk Assessor

**Charter governs this role. The Risk Assessor produces exactly one field: Confidence Gap.**
**The Risk Assessor does NOT produce**: Inertia Check (governed by Phase 0), or any of the nine fields governed by Phase 1.

**Non-access rule — the Risk Assessor is explicitly prohibited from citing as the gap:**
- The **integration points** the Sizing Analyst enumerated in Surface Area
- The **API contract status** the Sizing Analyst confirmed as established
- The **complexity tier drivers** the Sizing Analyst named
- The **team and timeline signals** the Sizing Analyst produced

These are confirmed dimensions. The Confidence Gap must identify a dimension Phase 1 did not reach.

**Self-test — the Risk Assessor applies this test before writing the gap:**
Ask: "Could a reader look only at the Sizing Analyst's Phase 1 output and derive this gap by reversing something the Sizing Analyst confirmed — turning 'X is established' into 'X has not been confirmed'?" If yes: charter violation. Name a dimension Phase 1 did not reach.

> **WRONG gap** (basis negation — charter violation):
> Phase 1 basis: "Auth API contract is stable — established baseline."
> Gap: "Auth API contract has not been confirmed." — Same dimension, negated. Directly derivable from Phase 1 by reversal.

> **CORRECT gap** (new dimension Phase 1 did not reach):
> Phase 1 basis: "Auth API contract is stable — three endpoints with documented schemas."
> Gap: "Auth API rate-limiting under sustained concurrent event load is undocumented — if the rate limit falls below expected event volume, a backpressure layer becomes a required integration point, expanding surface area and potentially shifting the tier." — Phase 1 did not reach this dimension.

| Confidence Gap [Risk Assessor — FAIL: any integration point Phase 1 enumerated, any contract Phase 1 confirmed, any driver Phase 1 named — must name a dimension Phase 1 did not reach — must survive the self-test before being written] |
|---|
| Gap: [specific named unknown] — [why it matters to the sizing] |

**Before finalizing the Confidence Gap**: The Risk Assessor runs the self-test one final time. If the gap negates anything the Sizing Analyst confirmed, the Risk Assessor restates it to name a genuinely new dimension.

---

```
── PHASE 2 SEALED ──

The Risk Assessor confirms ALL of the following before Output Compilation opens:

  [ ] Gap names a specific unknown (not a category hedge or vague statement)
  [ ] Gap cannot be derived from Phase 1 Confidence Basis by negation
  [ ] Gap identifies the dimension Phase 1 did not reach
  [ ] Self-test was applied and the gap survived it

Output Compilation does NOT open until all four items are confirmed.
── PHASE 2 CLOSED ──
```

---

### Output Compilation

**SIZING SIGNAL — [feature name]**

| Field | Phase | Value |
|---|---|---|
| Inertia Check (5-field) | 0 | [workaround] / [ongoing cost] / [cost direction] / [cost trajectory] / [key driver] |
| Surface Area | 1 | [named points — N integration points] |
| Complexity Tier [FAIL: MODERATE, medium-high, 3/5 — only: LOW / MEDIUM / HIGH / XL] | 1 | [tier] |
| Primary Complexity Driver | 1 | [1–2 named factors] |
| Team-Size Signal | 1 | [disciplines + fractions + ownership] |
| Timeline Signal [FAIL: calendar reference, point estimate — only: N–M sprints] | 1 | [N–M sprints] |
| Confidence Level [FAIL: MEDIUM-HIGH, 3/5 — only: HIGH / MEDIUM / LOW] | 1 | [level — basis] |
| Confidence Gap [must name dimension Phase 1 did not reach — not a negation of Phase 1 Confidence Basis] | 2 | [unknown — why it matters] |
| Tier-Up Sensitivity | 1 | Tier rises to [ ] if [ ] |
| Tier-Down Sensitivity | 1 | Tier drops to [ ] if [ ] |
| Confidence Calibration | 1 | [what raises / lowers confidence] |

Signal boundary check: no task breakdowns, sprint assignments, owner names, or milestone dates.

---

### Open Unknowns

> **FAILURE MODE**: Named hedges are not unknowns. Each entry names a specific unverified item with testable movement. Scope exclusions do not appear here — scope was resolved in PRE-FLIGHT GATE.

Unknown: [specific unverified item]
Impact: [complexity / timeline / team / confidence]
Movement: [what closes this unknown]

[or: "No open unknowns."]

---

### Synthesis

> **FAILURE MODE**: Restating sections in sequence — "Complexity is HIGH. Timeline is 4–6 sprints. Confidence is MEDIUM." — is juxtaposition, not synthesis. The cross-signal conclusion must require two or more dimensions to state.

The Synthesis confirms or revises the preliminary hypothesis committed in PRE-FLIGHT GATE using a structured commitment-chain trace. All three labeled lines appear on separate lines. A prose paragraph containing all three chain steps fails C-24.

Commitment chain:
Gate commitment: [tier committed in PRE-FLIGHT GATE] / [sprint range committed in PRE-FLIGHT GATE]
Analysis: [key evidence from Phases 0–2 bearing on the commitment — name at least two signal dimensions]
Verdict: [exactly one of the following three forms — the phrase "committed in PRE-FLIGHT GATE" is required]
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is confirmed: [cross-signal observation combining at least two dimensions]."
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is revised: [dimension] moved from [prior] to [current] because [reason]."
  — "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N–M sprints]) is partially revised: [what held]; [what changed] because [reason]."

After the verdict, state the cross-signal directional observation combining at least two dimensions (complexity, timeline, confidence, inertia cost, inertia trajectory).

Scope exclusions do not appear here — scope was resolved in PRE-FLIGHT GATE.

**STRUCTURAL AMEND RE-EVALUATION DIRECTIVE**: When AMEND is absent — the Sizing Engineer confirms no active amendment and proceeds. When AMEND is present and the amended dimension appears in the cross-signal conclusion or verdict above — the Sizing Engineer re-evaluates that conclusion before closing this section, updating it or explicitly reaffirming it still holds under the amendment. This directive is a structural property of the Synthesis section — it applies on every invocation regardless of whether AMEND is present.

---

### Per-Criterion Self-Check

The Sizing Engineer evaluates each criterion with PASS / PARTIAL / FAIL and cites evidence. This self-check is a separate verification artifact — it does not collapse into the content sections above.

**Essential criteria (C-01 through C-05):**

| ID | Criterion | Pass condition | Disqualifying form | Verdict | Evidence |
|---|---|---|---|---|---|
| C-01 | Complexity tier vocabulary | Exactly one of LOW / MEDIUM / HIGH / XL | "MODERATE", "medium-high", "3/5", "complex", "intermediate" as the tier label | | |
| C-02 | Timeline sprint range | N–M sprints with both bounds | Calendar date ("Q3 2026"), single number ("4 sprints"), "a few sprints" | | |
| C-03 | Surface area quantified | Named or counted integration points (min 2, or 0–1 with reasoning) | "Moderate surface area", "several integrations" with no named points | | |
| C-04 | Inertia check present | Labeled section naming workaround + at least one cost dimension | Section absent; or section present naming only the feature, not the workaround | | |
| C-05 | Confidence level with basis | Level stated AND at least one reason given | "Confidence: MEDIUM" with no follow-on sentence | | |

**Recommended criteria (C-06 through C-08):**

| ID | Criterion | Pass condition | Disqualifying form | Verdict | Evidence |
|---|---|---|---|---|---|
| C-06 | Team-size names specializations | At least one role or discipline named, not just headcount | "3 engineers" or "2 people" with no role labels | | |
| C-07 | Complexity justified with driver | At least one sentence names what pushed the tier to that level | Bare tier label with no follow-on justification | | |
| C-08 | AMEND cascades to output | If AMEND present: substantive change traceable to directive; if absent: default PASS | AMEND invoked but output is identical to non-amended run | | |

**Aspirational criteria (C-09 through C-35):**

| ID | Criterion | Pass condition | Disqualifying form | Verdict | Evidence |
|---|---|---|---|---|---|
| C-09 | Scopes what is NOT included | At least one explicit exclusion, assumption, or out-of-scope boundary named | Output naming only what is included with no boundary statement | | |
| C-10 | Break-even signal | Break-even estimate OR explicit "cannot assess — [reason]" | Inertia cost described with no break-even reference | | |
| C-11 | Each specialization states ownership | At least one named role includes implementation scope | Role list with no ownership scope ("1 backend, 1 infra" only) | | |
| C-12 | Confidence names specific unknowns | At least one concrete unknown that would move confidence if resolved | "Confidence is LOW due to uncertainty" with no named unknown | | |
| C-13 | Synthesis integrates, not restates | At least one sentence cross-referencing two+ dimensions | "Complexity is HIGH. Timeline is 4–6 sprints." (sequential restatement) | | |
| C-14 | Open unknowns in dedicated section with typed fields | Named section with Unknown/Impact/Movement fields or "No open unknowns" | Unknowns embedded in confidence basis with no separate section | | |
| C-15 | Synthesis confirms or revises prior hypothesis | Prior hypothesis stated before analysis; synthesis explicitly confirms, revises, or partially revises with the exact phrase | Synthesis conclusion that matches the hypothesis with no explicit confirmation statement | | |
| C-16 | AMEND cascades to synthesis | If AMEND changes a dimension cited in synthesis: synthesis re-evaluated; if not: default PASS | AMEND changes complexity tier; synthesis cross-signal conclusion unchanged and unreaffirmed | | |
| C-17 | Aspirational sections name failure mode | At least one aspirational section names the anti-pattern being avoided | Section that silently avoids the failure mode with no statement of what it is | | |
| C-18 | Pre-flight gate before first dimension | Gate fires before Surface Area and before Complexity field | Inline reminder inside Surface Area ("don't forget scope") substituted for a structural gate | | |
| C-19 | Adjacent sections carry prohibition guards | At least one adjacent section carries explicit prohibition against canonical field type | Confidence basis with no prohibition against unknowns when OPEN UNKNOWNS section exists | | |
| C-20 | Complete closure mesh | Every section that could receive a canonical field type is explicitly closed | Synthesis with no prohibition against scope exclusions when PRE-FLIGHT GATE owns scope | | |
| C-21 | Gate elicits preliminary hypothesis | Gate requires tier + timeline commitment before first analysis section | Gate asking for scope boundary only, no hypothesis commitment | | |
| C-22 | Synthesis names gate at both ends | Synthesis names PRE-FLIGHT GATE when anchoring prior commitment AND when stating verdict | "my earlier estimate" without naming the structural label | | |
| C-23 | Prohibition guards name canonical home | At least one prohibition guard names home by label: "scope was resolved in PRE-FLIGHT GATE" | "Do not include scope here" without naming where scope belongs | | |
| C-24 | Synthesis has structured commitment-chain trace | Gate commitment, analysis evidence, and verdict on separate labeled lines | Single prose paragraph containing all three chain steps | | |
| C-25 | PRE-FLIGHT GATE forward-references enforcement sections | Gate names at least two downstream sections enforcing its commitments | Gate with scope exclusions but no mention of which sections enforce them | | |
| C-26 | Synthesis embeds AMEND re-evaluation directive | Synthesis contains written directive requiring re-evaluation when AMEND affects a cited dimension | Synthesis with C-16 behavioral compliance but no written structural directive | | |
| C-27 | Every aspirational section has FAILURE MODE block | Every aspirational section with nontrivial pass condition has dedicated labeled FAILURE MODE block | Synthesis with anti-pattern awareness embedded in prose, no dedicated block | | |
| C-28 | Per-criterion self-check trace | Separate artifact evaluating each aspirational criterion by ID with pass/fail + evidence | Self-check absent from the output | | |
| C-29 | Structural criteria have exact disqualifying forms in self-check | C-18 through C-27, C-33, C-35: each item has pass condition + named disqualifying form | Structural criterion self-check entry with pass condition only | | |
| C-30 | Depth/behavior criteria have exact disqualifying forms in self-check | C-09 through C-17, C-34: each item has pass condition + named disqualifying form | Depth criterion self-check entry with pass condition only | | |
| C-31 | Self-check covers all weight classes | Self-check includes C-01 through C-08 in addition to C-09–C-35 | Self-check covering C-09–C-35 with C-01–C-08 absent | | |
| C-32 | Essential/recommended self-check items have exact disqualifying forms | C-01 through C-08: each item has pass condition + named disqualifying form | Essential criterion entry with evidence but no disqualifying form | | |
| C-33 | Inertia check is structural opener | Inertia section appears in document order before complexity tier, timeline, surface area, and confidence level fields | Inertia section appearing after PRE-FLIGHT GATE preliminary hypothesis is committed, or after Surface Area | | |
| C-34 | Inertia uses 4-field structured format | Inertia entry contains Workaround, Ongoing Cost, Cost Direction, and Key Driver as named fields or columns | Inertia entry with workaround + cost direction but omitting Key Driver field | | |
| C-35 | Disqualifying forms as write-time constraint tags on all vocab-constrained fields | [FAIL: ...] tags present on: Complexity Tier (C-01), Timeline (C-02), Confidence Level, Cost Direction, Tier-Destination (both sensitivity rows), FTE column | Any vocabulary-constrained field header carrying no [FAIL:] tag | | |

---

```json
{
  "skill": "scout-size",
  "round": 12,
  "rubric": "v12",
  "variations": 5,
  "aspirational_denominator": 27,
  "r11_champion": "V-05 (27/27, 100.00 under v12)",
  "r12_excellence_signals": {
    "G-01": "C-35 extended to all vocab-constrained fields — explored in V-01, V-04, V-05",
    "G-02": "5-field inertia with Cost Trajectory rate — explored in V-02, V-05",
    "G-03": "PHASE SEALED blocks as close-out artifacts — explored in V-03, V-04, V-05",
    "G-04": "Per-criterion self-check present in multi-phase design — all five variations"
  },
  "axes": {
    "V-01": "output-format-C35-extended-all-vocab-fields",
    "V-02": "inertia-framing-5-field-with-cost-trajectory",
    "V-03": "lifecycle-emphasis-phase-sealed-blocks",
    "V-04": "combined-C35-all-fields-plus-phase-sealed",
    "V-05": "combined-all-axes-plus-examiner-voice"
  },
  "potential_v13_criteria": {
    "C-36": "C-35 extended — all vocabulary-constrained fields carry [FAIL:] tags (not just C-01/C-02)",
    "C-37": "Inertia uses 5-field format with quantified Cost Trajectory (rate of change)",
    "C-38": "Phase SEALED blocks with completion checklists required between all phase transitions"
  },
  "expected_v12_scores": {
    "V-01": "27/27 — satisfies all v12 criteria; C-35 extended beyond minimum is not a new v12 pass, it is a v13 seed",
    "V-02": "27/27 — satisfies all v12 criteria; 5-field inertia exceeds C-34 minimum without failing it",
    "V-03": "27/27 — satisfies all v12 criteria; PHASE SEALED blocks exceed verbal handoff without conflicting with existing criteria",
    "V-04": "27/27 — satisfies all v12 criteria; combined orthogonal mechanisms",
    "V-05": "27/27 — satisfies all v12 criteria; examiner voice is register variation with no criterion conflict"
  }
}
```
