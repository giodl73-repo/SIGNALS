Golden document written to `simulations/quest/golden/validate-inertia-golden-2026-03-17.md`.

**What's in it:**

- **Frontmatter** as specified: skill, target, date, rounds=20, rubric_final=v21, score=500, status=GOLDEN
- **Simplified prompt body** (862 words) — Citation Architecture section stripped (the ~1500-word aspirational apparatus for C-09–C-51), with phases 1–7 + AMEND retained. C-01–C-05 all preserved: quantification gates in Phase 3, four-part kill barrier with reselection loop, LEVER POINT label, TRAJECTORY VERDICT label, AMEND causal chain.
- **What made it golden** — 5 patterns: quantification-as-disqualifier, four-part kill barrier with self-rejection, TRAJECTORY VERDICT as named label, LEVER POINT falsifiability loop, AMEND as sharpening pass.
- **Final rubric summary** — 510 pts max, 500 achieved at R20, C-51 flagged as R21 gap.
binations]
- **Low:** [condition all dimensions must satisfy]

Do not proceed to Phase 2 until written.

---

## Phase 2 -- Persona and Competitive Inventory

Identify 2--4 named personas. For each, treat the current solution as a named competitor.

- Name and role (specific)
- Current solution (named tool or method)
- Outcome the current solution delivers

**Competitive strength inventory per persona:**

| Dimension | Advantage | Durability |
|-----------|-----------|------------|

Durability must name a structural constraint. **Familiarity is not durability.** Structural
constraints: technical, organizational, integration-based, or switching-cost-based.

**Completeness gate:** For each persona: (1) all three fields present; (2) no Durability uses
familiarity/habit -- replace with structural constraint; (3) Dimension names a specific axis.
Do not proceed to Phase 3 until all personas pass all three checks.

Do not proceed to Phase 3 until written.

---

## Phase 3 -- Inertia Dimension Analysis

| Persona | Workaround satisfaction (H/M/L) | Satisfaction basis (ref. Phase 2) | Switching cost (quantified) | Habit lock-in | Social proof threshold (named condition) | Learning curve |
|---------|---------------------------------|-----------------------------------|----------------------------|---------------|------------------------------------------|----------------|

Switching cost: time, steps, rating 1--10. Qualitative-only fails.
Social proof threshold: named count, role, or condition. Binary Y/N fails.

---

## Phase 4 -- Per-Persona Inertia Scores

| Persona | Score | Methodology trace |
|---------|-------|-------------------|

Methodology trace: (a) name dimension values from Phase 3 + (b) state Phase 1 threshold
satisfied. Every persona scored individually.

---

## Phase 5 -- Kill Barrier: Four-Part Causal Analysis with Reselection Gate

**KILL BARRIER** -- four labeled, distinct sub-parts. Do not merge any two.

**(1) Barrier definition** -- observable adoption friction; state the competitive dimension.
Do not include cause.

**(2) Structural persistence** -- why the barrier persists structurally. Name the specific
Durability property by its Phase 2 label.

**(3) Intervention target** -- specific lever point. Name the target, not the intervention.

**Required lever label:**

> **LEVER POINT: [exact label -- 3--7 words]**

**Falsifiability test:**

> "At T=6mo, the absence of this lever would be observable as: [specific observable
> behavioral or measurable condition]."

Replace Part (3) and repeat if you cannot produce a specific observable condition. Do not
write Part (4) until the test passes.

**(4) Lever efficacy** -- why addressing (3) resolves (2). Explain causally. Reference (2)
by name.

**Temporal persistence confirmation:**

| T=0 exists? | T=18mo persists without structural intervention? |
|-------------|--------------------------------------------------|
| YES / NO | YES / NO |

Both must be YES to qualify. If either is NO, return to the top of this phase.

**CONFIRMED KILL BARRIER.** Name the most exposed persona.

---

## Phase 6 -- Adoption Timeline and Kill-Barrier Trajectory Verdict

**Part A: Per-Persona Timeline**

| Persona | T=0 | T=6mo | T=18mo | Trajectory | Driver of change |
|---------|-----|-------|--------|------------|-----------------|

At least one trajectory non-flat. T=6mo and T=18mo cannot copy T=0 without a stated reason.

**Part B: KILL-BARRIER TRAJECTORY VERDICT**

**Trajectory direction:** [Resolving / Stable / Worsening]

**Structural reasoning:** [Reference the structural persistence property from Phase 5(2)
by name. Argue from mechanism, not from the per-persona grid.]

**Relationship to Part A:** [Alignment or divergence -- which structural property drives both,
or why they differ.]

**Required trajectory label:**

> **TRAJECTORY VERDICT: [exact direction word -- Resolving, Stable, or Worsening]**

Do not proceed to Phase 7 until written.

---

## Phase 7 -- Overall Adoption Inertia Risk

Verdict: Low / Medium / High / Critical.

- Score distribution (e.g., "2 High, 1 Critical")
- Kill-barrier trajectory: copy the exact TRAJECTORY VERDICT label. Do not write "Phase 6 Part B."
- Competitive summary: kill barrier dimension + Phase 2 structural durability basis
- 1--2 sentence rationale tying score distribution, trajectory, and confirmed kill barrier

---

## AMEND -- Focus, Quantify, Confirm

**Focus persona:** [name -- most exposed to confirmed kill barrier]

**Switching cost (sharpened):** [most precise quantified value]

**Kill barrier for this persona:** [one sentence -- competitive dimension, most acute because]

**Mitigation with full causal chain:**

> **(a) Intervention:** [one concrete action]
>
> **(b) Root cause addressed:** [name the structural condition from Phase 5(2)]
>
> **(c) Causal mechanism:** [why this lever reaches the structural condition in (2). Reference
> the Phase 5(3) lever point by name.]
>
> **(d) Confirmation signal at T=6mo:**
>
> Lever anchor: [copy the exact LEVER POINT label from Phase 5(3)].
>
> [At T=6mo, the absence of this lever would be observable as: [specific falsifiable
> behavioral or measurable condition]. Must be possible to observe it as absent.]

---

## What Made It Golden

**1. Quantification gates in Phase 3 — not format hints.**
The switching cost and social proof threshold requirements are stated as disqualifiers
("Qualitative-only fails," "Binary Y/N fails") rather than suggestions. This forces the model
to produce scorable values, not prose descriptions that slip past C-02 and C-03.

**2. Four-part kill barrier with independent reselection gate.**
Splitting the kill barrier into four labeled sub-parts with a falsifiability test on Part (3)
makes the CONFIRMED KILL BARRIER reachable only through causal specificity. The temporal
persistence table enforces C-04's "distinct kill-barrier identification" by requiring a YES/YES
before CONFIRMED can be written. Vague barriers self-reject.

**3. TRAJECTORY VERDICT as a named label forcing C-05 evidence chain.**
The `TRAJECTORY VERDICT: [direction]` label in Phase 6 Part B, carried verbatim into Phase 7,
binds the aggregate risk verdict to a mechanism argument rather than a score average. The Part A
disqualifier (present in the full rubric version) enforces structural separation between
per-persona grids and the kill-barrier verdict -- preventing the most common C-04/C-05 conflation.

**4. LEVER POINT label with falsifiability reselection loop.**
The 3--7 word lever label forces the model to name an intervention target precisely. The
falsifiability test creates a self-rejection loop: if the model cannot state an observable
absence condition, it must replace Part (3). This is the mechanism that made V-91 (the R19
ceiling) a 490 -- the label survives simplification because it drives C-04 and AMEND(c), both
essential.

**5. AMEND as a sharpening pass, not a summary.**
AMEND focuses on the most exposed persona, requires the most precise switching cost, and
demands a full causal chain (a-b-c-d). The lever anchor in AMEND(d) forces the LEVER POINT
label to be reproduced verbatim, confirming that the falsifiability test in Phase 5 produced
a real anchor -- not a placeholder. This closes the loop between Phase 5(3) and the
confirmation signal.

---

## Final Rubric Criteria Summary

**Rubric:** `validate-inertia-rubric-v21-2026-03-17.md` | **Max score:** 510 pts

### Essential Criteria (C-01--C-05) — 50 pts

| ID | Criterion | Pass condition |
|----|-----------|---------------|
| C-01 | Per-persona inertia mapping | 2--4 named personas with inertia factors |
| C-02 | Quantified switching cost | Numeric or enumerated cost; qualitative-only fails |
| C-03 | Per-persona inertia score | Individual score for each persona |
| C-04 | Kill-barrier identification | Distinct kill barrier identified and confirmed |
| C-05 | Overall adoption inertia risk | Aggregate verdict with rationale |

### Recommended Criteria (C-06--C-08) — 30 pts

| ID | Criterion |
|----|-----------|
| C-06 | Current workaround satisfaction explicitly assessed |
| C-07 | Habit lock-in + social proof threshold covered |
| C-08 | Mitigation path named for the kill barrier |

### Aspirational Criteria (C-09--C-51) — 430 pts

43 criteria covering: scoring methodology transparency, time-dependent inertia trajectory,
status-quo competitor framing, named social proof threshold, mitigation tied to structural root
cause, kill-barrier temporal persistence test, causal chain with labeled structural sub-parts,
mitigation confirmation signal, per-score methodology trace, kill-barrier trajectory verdict,
related-output structural segregation with disqualifier, kill-barrier reselection gate,
phase-zero methodology gate, competitive strength inventory in persona phase, named intervention
target as falsifiable anchor, named boundary artifact at phase transition, structural prohibition
gate vs. format instruction, cross-phase citation chain with named anchors, self-rejection gate
for mechanism specificity, named artifact at every downstream-source boundary, exact-copy
citation instruction in downstream anchoring sections, Citation Architecture preamble as
single-read authority, citation chain completeness self-audit, evidence column converts citation
audit from assertion to demonstration, architecture-audit duality framing, preamble-declared
audit format, atomic audit format declaration, audit-first derivation, co-resident named block
for audit architecture criteria, derivation direction co-resident in named architecture block,
derivation prohibition declared at architecture-read boundary, per-axis explicit gate for
three-axis architecture block, per-axis gate declared in block body not in produced label,
gate components not split between block body and produced label, produced architecture label
cites block body as source of both gate components, split-gate failure modes named as explicit
disqualifiers in block body, gate closure named as duality of self-documenting label function
and self-enforcing block body function, non-propagation between closure criteria declared in
block instruction body, C-45 FAIL condition declared as explicit disqualifier in block
instruction body, both C-45 PARTIAL paths enumerated as distinct disqualifiers in block
instruction body, both C-48 PARTIAL shapes enumerated as distinct cases in block instruction
body, both C-45 FAIL shapes enumerated as distinct disqualifiers in block instruction body,
all three C-50 PARTIAL paths enumerated as distinct cases in block instruction body.

### Score at Golden (R20 ceiling)

| Criteria | Points |
|----------|--------|
| C-01--C-05 (essential, all PASS) | 50 |
| C-06--C-08 (recommended, all PASS) | 30 |
| C-09--C-44 (aspirational baseline) | 360 |
| C-45--C-50 (gate closure criteria) | 60 |
| **Total** | **500 / 510** |

C-51 (all three C-50 PARTIAL paths enumerated) added in v21 as the R21 gap — not yet tested.
