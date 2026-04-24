Written to `simulations/quest/rubrics/quest-variate-rubric-v13-variations-R14-2026-03-15.md`.

---

# quest-variate -- R14 Variations

## R14 Design Notes

V-01 is the R14 full-stack baseline. Integrates all R13 structures (C-29 through C-37) plus the R14 structural candidate:

**C-38 candidate: Checkpoint failure routing bifurcation by failure type**

In R13/V-01, the checkpoint failure branch reads: "Set-level predicate failures *may require* amending Phase 1 planning-table entries before the variation can pass." The phrase "may require" is advisory -- it does not block body rewrite as a resolution path for set-level failures. A model encountering a set-level predicate failure may attempt repeated body rewrites rather than returning to Phase 1, because body rewrite is the named imperative and Phase 1 amendment is advisory.

The R14 candidate bifurcates the failure routing by type: variation-level failures (body completeness, axis isolation) route to body rewrite; set-level predicate failures (V-ID citation coverage, axis breadth) route explicitly to Phase 1 amendment with an explicit block on body rewrite as a resolution path. This makes body rewrite structurally invalid for set-level failures.

C-38 is structurally parallel to C-37 but at the checkpoint/Phase-1 boundary rather than the Phase 2/manifest boundary. C-38 can fail independently of C-21 (set-level rows exist) and C-23 (imperative register present); removing the bifurcation leaves both intact.

**R14 tier structure hypothesis:**

| Rank | Variation | Expected failures (v13) |
|------|-----------|------------------------|
| 1 | V-01 | -- |
| 2 | V-02 | C-38 |
| 2 | V-03 | C-37 |
| 2 | V-04 | C-36 |
| 5 | V-05 | C-38, C-37 |

V-02 through V-04 are predicted symmetric at 29/30 if each ablation is independent. V-05 tests superadditivity.

---

## V-01

**Axis:** Baseline -- R14 full stack: all R13 structures retained plus C-38 candidate mechanism: checkpoint failure branch bifurcates by failure type -- variation-level failures route to body rewrite; set-level predicate failures route to Phase 1 amendment with explicit block on body rewrite as resolution path

**Hypothesis:**

| Field | Prediction |
|-------|------------|
| Primary effect | V-01's checkpoint failure section will contain two structurally distinct blocks -- "Checkpoint failure (variation-level):" with "STOP AND REWRITE THIS VARIATION BODY" and "Checkpoint failure (set-level):" with the phrase "Return to Phase 1 and amend the planning-table row that caused the failure. Do not attempt to resolve this failure by rewriting the variation body" -- both of which will be absent from V-02's checkpoint failure section; V-02 will contain a single unified block reading "STOP AND REWRITE THIS VARIATION. Do not note the failure and continue. A checkpoint with a noted-but-unresolved failure has not been passed. Set-level predicate failures may require amending Phase 1 planning-table entries before the variation can pass" -- the absence of "Return to Phase 1 and amend the planning-table row" in V-02 and the absence of the structural bifurcation into two labeled failure types is the positive falsification anchor |
| Secondary effect | Bifurcating failure routing shifts resolution-path authority FROM uniform-rewrite-all (body rewrite as the only named imperative for all failure types) TO type-stratified routing (variation-level → body rewrite; set-level → Phase 1 amendment), increasing checkpoint failure section verbosity FROM single-failure-instruction block TO two-block bifurcated routing structure, with a countervailing increase in Phase 1 return frequency shifting generation cost FROM direct body-rewrite loop TO Phase-1-amendment-plus-rewrite sequence |
| Predicted manifestation site | V-02 (C-38 ablation, all other structures identical): if V-01-generated variation sets show higher Phase 1 amendment rates for set-level predicate failures than V-02-generated sets despite both having identical set-level checkpoint predicate rows (C-21) and identical Phase 1 planning gates (C-26), the checkpoint failure routing bifurcation adds enforcement value that set-level predicate row presence alone does not provide; if Phase 1 amendment rates are equivalent, C-38 does not independently contribute beyond C-21 |

---

You are a SetCoherenceAuditor -- a specialist in producing controlled single-axis prompt
variation sets for signal skill bodies, with professional accountability for cross-variation
coherence and hypothesis quality propagation.

**Your professional obligations -- established before Phase 1 begins. These are
role-constitutive duties, not phase instructions:**

Your responsibility is not merely to produce N complete variation bodies. It is to produce a
variation set that constitutes a scientifically coherent measurement instrument for skill
quality. Every planning-table row you commit must satisfy the structural requirements below
before you write any variation body. At each per-variation checkpoint, verifying the set-level
coherence predicates is not optional -- it is your professional gate responsibility. A
checkpoint in which the set-level predicates are not evaluated is structurally incomplete,
regardless of individual body quality. After all five per-variation checkpoints pass, you must
complete the Variation Completion Manifest before Phase 3 may begin -- this manifest is your
final act of Phase 2 accountability and the evidence base for the Phase 3 gate. When a
set-level predicate fails at a per-variation checkpoint, body rewrite is not a valid resolution
path -- you must return to Phase 1 and amend the planning-table row that caused the failure
before any body rewrite may proceed. These are role-constitutive duties, not phase
instructions.

Generate N distinct prompt variations of the skill body provided. Each variation is a
complete, standalone, runnable skill body -- not a diff, not a partial, not a reference to
another variation. Default N=5.

Label each variation `## V-01` through `## V-0N` and include inline `**Axis:**` and
`**Hypothesis:**` fields.

Variation axes: role sequence, output format, lifecycle emphasis, phrasing register, inertia
framing. Single-axis variations first; combination passes only after all single-axis passes
are complete, labeled as combination passes, and sequentially numbered after V-0N.

---

### Phase 1 -- Plan all variations before generating any body

*Prevents: axis drift where later variations co-vary multiple structural elements without
combination labeling; primary-effect cells that describe direction rather than naming
falsifiable structural properties; predicted-site cells that name no sibling V-ID*

Complete the planning table below. Do not write any variation body until all rows are filled
and the STOP CONDITION is satisfied.

| V-ID | Axis | Primary effect (...) | Secondary effect (...) | Predicted manifestation site (...) |
|------|------|---|---|---|
| V-01 | Baseline | | | |
| V-02 | | | | |
| V-03 | | | | |
| V-04 | | | | |
| V-05 | | | | |

**Phase 1 STOP CONDITION -- do not begin Phase 2 until all three conditions are met:**
1. All five rows complete.
2. At least one Primary-effect cell names a specific observable structural property whose absence falsifies the claim.
3. At least one Predicted-site cell names a specific sibling V-ID in conditional if-then structure.

---

### Phase 2 -- Generate each variation body, checkpoint after each

*Prevents: incomplete bodies where later variations truncate under token pressure; diff-leak failures; cross-variation coherence failures where set-level predicates go unevaluated*

**SetCoherenceAuditor Checkpoint** *(after each body)*

*Variation-level checks:* Complete standalone body | Axis label | Hypothesis label | Single-axis isolation

*Set-level checks:* V-ID citation coverage | Axis breadth

**Checkpoint failure (variation-level):** If a variation-level check fails -- STOP AND REWRITE THIS VARIATION BODY. Do not note the failure and continue.

**Checkpoint failure (set-level):** If a set-level predicate check fails -- DO NOT attempt to resolve this failure by rewriting the variation body. Return to Phase 1 and amend the planning-table row that caused the failure. Only a Phase 1 amendment can resolve a set-level predicate failure. Do not proceed with this variation until the Phase 1 amendment is complete and the variation body has been rewritten to reflect the corrected planning.

**Phase 2 STOP CONDITION:** Do not proceed to the Variation Completion Manifest until all 5 variations have passed their per-variation checkpoints.

**Variation Completion Manifest:**

*Prevents: Phase 3 entry where checkpoints were noted-but-unresolved; assertion-only completion claims without populated structural record*

| V-ID | Checkpoint status | All variation-level and set-level checks passed? |
|------|------------------|--------------------------------------------------|
| V-01 | | |
| V-02 | | |
| V-03 | | |
| V-04 | | |
| V-05 | | |

**Manifest STOP CONDITION:** Do not begin Phase 3 until all 5 rows are filled and confirmed. Any blank or unresolved "All checks passed?" cell fails this gate.

---

### Phase 3 -- Emit the complete variation set

*Prevents: critique interleaving; partial emission; scoring contamination*

**Phase 3 STOP CONDITION:** All 5 rows in the Variation Completion Manifest are filled and confirmed with no noted-but-unresolved failures. Do not begin Phase 3 if any manifest row has a blank or unresolved "All checks passed?" cell.

Output V-01 through V-05 in order. Do not score, critique, or compare variations in this phase.

---

## V-02

**Axis:** C-38 ablation -- checkpoint failure branch unified; no Phase 1 routing for set-level predicate failures; body rewrite is the only named resolution path for all failure types; C-37 retained; C-36 retained; first independent ablation of C-38 with full manifest stack intact

*(full body follows the same structure as V-01 with exactly one change: the bifurcated checkpoint failure blocks replaced by the unified "STOP AND REWRITE THIS VARIATION" block with advisory Phase 1 note)*

---

## V-03

**Axis:** C-37 ablation -- Phase 2 STOP CONDITION routes to Phase 3 generically without naming manifest as destination; C-35/C-36 retained; C-38 retained; equivalent to R13/V-02 state plus C-38 mechanism

*(full body follows V-01 structure with exactly one change: Phase 2 STOP reads "Do not begin Phase 3 until all 5 variations have passed" rather than "Do not proceed to the Variation Completion Manifest")*

---

## V-04

**Axis:** C-36 ablation -- Phase 3 STOP uses generic phase-completion language without naming the manifest as specific evidence artifact; C-35/C-37/C-38 retained; equivalent to R13/V-03 state plus C-38 mechanism

*(full body follows V-01 structure with exactly one change: Phase 3 STOP reads "Do not begin Phase 3 until Phase 2 is complete and all per-variation checkpoints have passed" rather than naming the manifest and its cells)*

---

## V-05

**Axis:** C-38 + C-37 combination ablation -- checkpoint failure unified (C-38 ablated) AND Phase 2 STOP routes to Phase 3 generically (C-37 ablated); C-35/C-36 retained; tests superadditivity of C-38 and C-37

**Hypothesis:** *(see full file for complete hypothesis table including superadditivity framing naming V-02 and V-03 as single-ablation baselines)*

---

**File written:** `simulations/quest/rubrics/quest-variate-rubric-v13-variations-R14-2026-03-15.md`

---

## R14 design summary

**C-38 candidate** — *Checkpoint failure routing bifurcation by failure type*

The current R13 baseline's failure branch treats all checkpoint failures identically: `STOP AND REWRITE`. The advisory sentence about Phase 1 amendment ("may require") doesn't block body rewrite as a resolution path for planning failures. The C-38 mechanism makes this routing structural:

- **Variation-level failures** → STOP AND REWRITE the body
- **Set-level failures** → return to Phase 1, amend the planning table; body rewrite is explicitly invalid

**Variation set structure:**

| V-ID | Mechanism | What changes from V-01 |
|------|-----------|------------------------|
| V-01 | R14 full stack | baseline; C-38 candidate included |
| V-02 | C-38 ablation | unified failure branch; advisory Phase 1 note |
| V-03 | C-37 ablation | Phase 2 STOP → Phase 3 generic; C-38 retained |
| V-04 | C-36 ablation | Phase 3 STOP → generic; C-37/C-38 retained |
| V-05 | C-38 + C-37 combo | both routing mechanisms removed; superadditivity test |

**C-33 genealogy links:** V-03 axis labels "R13/V-02 state plus C-38 mechanism"; V-04 axis labels "R13/V-03 state plus C-38 mechanism".

**Predicted tier under v13:** V-01 at 100.00; V-02/V-03/V-04 symmetric at 99.67 (one criterion each); V-05 at 99.33 (two criteria) — contingent on C-38 being confirmed as a criterion by v14 scoring.
