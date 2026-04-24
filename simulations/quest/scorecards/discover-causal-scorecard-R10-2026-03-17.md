Now I have everything needed. Let me score all five variations.

---

## discover-causal R10 Scorecard (Rubric v10)

**Base:** R9 V-05 -- 205/205 under v10 (all criteria pass)
**New criterion under test:** C-31 -- Phase 3 CONDITIONAL BRANCH carries stale-anchor prohibited form
**Maximum:** 205 pts | **Golden:** >= 200 | **Acceptable:** 185-199 | **Passing:** 170-184

---

### Shared Baseline (all five variations)

All variations preserve the full R9 V-05 structure except for the Phase 3 CONDITIONAL BRANCH anchor-update block. Every criterion from C-01 through C-30 passes identically across all five.

**Gradeability chain for C-30 and C-31:**
- C-11 PASS -- Phase 1 includes incompleteness declaration path with SUB-STEP 1 format
- C-12 PASS -- Phase 3 requires step-labeled falsification anchors matching Phase 2 labels
- C-18 PASS -- C-24 PROHIBITED FORM block enforces step-anchor in all cases (no deferral allowed)
- C-24 PASS -- explicit "deferring or omitting step-level falsification does not pass" at Phase 3
- C-26 PASS -- Phase 1 SUB-STEP 2 produces preliminary anchor at the declaration point before Phase 2
- C-27 PASS -- Phase 1 PROHIBITED FORM block includes "does not pass" language at sub-step 2
- C-28 PASS -- Phase 3 uses "already on record from Phase 1 SUB-STEP 2" prior-record framing
- C-29 PASS -- Phase 6 integration rules include C-26 cross-phase integrity detection rule
- **C-30 PASS (all variations)** -- Phase 6 carries stale-anchor integration rule + `anchor_updated_from_phase1: true | false | n/a` ARTIFACT field
- **C-31 gradeable** -- C-30 PASS in all five variations

---

### Full Criterion Table

#### Essential Criteria -- 60 pts (C-01 through C-05, 12 pts each)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence note |
|----|------|------|------|------|------|---------------|
| C-01 | PASS | PASS | PASS | PASS | PASS | Phase 2 requires step-labeled pathway: "Step N -- [Name]: What changes. Who acts. Observable indicator." |
| C-02 | PASS | PASS | PASS | PASS | PASS | Phase 3 requires mechanism-break format: "The mechanism fails if Step [N] -- [Name] -- does not occur, observable as [indicator]." |
| C-03 | PASS | PASS | PASS | PASS | PASS | Phase 0 INERTIA GATE mandates verdict before mechanism work; all three verdict values must shape Phase 6 |
| C-04 | PASS | PASS | PASS | PASS | PASS | Phase 6 AMEND requires narrowed claim with mechanism qualifier + scope condition |
| C-05 | PASS | PASS | PASS | PASS | PASS | Phase 4 CONTEXT EVIDENCE requires team-specific evidence per pathway step; "no evidence" is a valid value |

**Essential subtotal: 60/60 all variations**

---

#### Recommended Criteria -- 30 pts (C-06 through C-08, 10 pts each)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence note |
|----|------|------|------|------|------|---------------|
| C-06 | PASS | PASS | PASS | PASS | PASS | Step labeling requirement ("named agent and observable indicator") makes pathway testable by construction |
| C-07 | PASS | PASS | PASS | PASS | PASS | Phase 5 CONFOUNDER CHECK explicitly requires at least one non-inertia alternative cause |
| C-08 | PASS | PASS | PASS | PASS | PASS | Phase 6 AMEND requires mechanism qualifier + scope condition (bounded scope enforced) |

**Recommended subtotal: 30/30 all variations**

---

#### Aspirational Criteria -- 115 pts (C-09 through C-31, 5 pts each)

Shared baseline (C-09 through C-29): PASS in all five variations -- R9 V-05 established these.

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence note |
|----|------|------|------|------|------|---------------|
| C-09 | PASS | PASS | PASS | PASS | PASS | Phase 4 T1/T2/T3 tier classification required per step |
| C-10 | PASS | PASS | PASS | PASS | PASS | Phase 2 asks: "is there more than one plausible causal pathway?" -- complementary/competing/nested required |
| C-11 | PASS | PASS | PASS | PASS | PASS | Phase 1 PATHWAY INCOMPLETE declaration with exact required format; "producing thin steps to clear gate fails" |
| C-12 | PASS | PASS | PASS | PASS | PASS | Phase 3 step-label requirement: "Step number and name must match a labeled row in Phase 2 exactly" |
| C-13 | PASS | PASS | PASS | PASS | PASS | Phase 4 FIELD INDEPENDENCE NOTE requires two named entries: Evidence gap steps + Aggregate evidence tier |
| C-14 | PASS | PASS | PASS | PASS | PASS | Phase 6 Amended field requires inertia incorporation via verdict-specific forms |
| C-15 | PASS | PASS | PASS | PASS | PASS | Phase 6 requires all prior phase outputs as named fields (Original, Inertia verdict, Mechanism completeness, Evidence tier, Evidence gap, Confounder finding, Falsification) |
| C-16 | PASS | PASS | PASS | PASS | PASS | Phase 2 STEP LABELING REQUIREMENT: "not a presentational preference -- structural prerequisite" |
| C-17 | PASS | PASS | PASS | PASS | PASS | Phase 5 explicitly excludes inertia from confounder analysis: "The inertia case (Phase 0) is EXCLUDED" |
| C-18 | PASS | PASS | PASS | PASS | PASS | C-24 block enforces step-anchor in incomplete pathway; deferral form named as failure mode |
| C-19 | PASS | PASS | PASS | PASS | PASS | Phase 4 NULL-GAP COUNTEREXAMPLE demonstrates orthogonality; Phase 6 requires both as separate named fields |
| C-20 | PASS | PASS | PASS | PASS | PASS | Phase 0 PROHIBITED FORM: "conditioning inertia incorporation on verdict being Competing or Unclear does not pass" |
| C-21 | PASS | PASS | PASS | PASS | PASS | Phase 4 NULL-GAP COUNTEREXAMPLE instantiated as required output state: `Evidence gap steps: none / Aggregate evidence tier: T1` |
| C-22 | PASS | PASS | PASS | PASS | PASS | Phase 0 PROHIBITED FORM names the escape hatch: "'Not competing -- no adjustment needed' is the conditional form that fails" |
| C-23 | PASS | PASS | PASS | PASS | PASS | Phase 6 Mechanism completeness is a standalone named field with explicit prohibition on embedding in amended clause |
| C-24 | PASS | PASS | PASS | PASS | PASS | Phase 3 PROHIBITED FORM (C-24): "declaring incompleteness and deferring or omitting step-level falsification does not pass" |
| C-25 | PASS | PASS | PASS | PASS | PASS | Phase 4 PROPAGATION REQUIREMENT + Phase 6 Evidence gap as standalone named field |
| C-26 | PASS | PASS | PASS | PASS | PASS | Phase 1 SUB-STEP 2 required PRELIMINARY ANCHOR at declaration point; PROHIBITED FORM names deferral-to-Phase-3 as failure |
| C-27 | PASS | PASS | PASS | PASS | PASS | Phase 1 PROHIBITED FORM block: "deferring the anchor to Phase 3 ... does not satisfy this sub-step regardless of how accurately incompleteness was declared" |
| C-28 | PASS | PASS | PASS | PASS | PASS | Phase 3: "If PATHWAY INCOMPLETE was declared in Phase 1, a PRELIMINARY ANCHOR is already on record from Phase 1 SUB-STEP 2. This branch confirms and extends it." |
| C-29 | PASS | PASS | PASS | PASS | PASS | Phase 6 integration rule: "a Falsification field that first names the anchor here without a corresponding Phase 1 PRELIMINARY ANCHOR does not pass C-26" |
| C-30 | PASS | PASS | PASS | PASS | PASS | Phase 6 stale-anchor integration rule present in all five + `anchor_updated_from_phase1: true\|false\|n/a` ARTIFACT field |

---

#### C-31: The Discriminating Criterion

**Pass condition:** Phase 3 CONDITIONAL BRANCH must carry a PROHIBITED FORM explicitly naming that *recording the updated BEST-TRACEABLE ANCHOR at Phase 3 does not complete the Phase 6 propagation requirement*. The self-referential phrase ("here does not close Phase 6") is the load-bearing element.

| Variation | C-31 | Evidence |
|-----------|------|----------|
| **V-01** | **FAIL** | Phase 3 carries ANCHOR-UPDATE INSTRUCTION: "carry the updated BEST-TRACEABLE ANCHOR step to Phase 6 Falsification." Positive instruction only. No PROHIBITED FORM block. No "does not complete" or "does not pass" language at Phase 3 update point. C-31 requires the prohibited form co-located at Phase 3; a positive instruction is the exact C-31 fail case per the rubric. C-30 intact (Phase 6 integration rule + ARTIFACT field), so C-30 PASS / C-31 FAIL. |
| **V-02** | **FAIL** | Phase 3 carries ANCHOR-UPDATE NOTE: "recording the updated BEST-TRACEABLE ANCHOR here is necessary but not sufficient for the Phase 6 propagation requirement." Block present, but no "does not pass" or "does not complete" explicit failure-mode language. Parallel to C-22/C-20: softened framing ("necessary but not sufficient") does not name the failure mode. C-31 requires explicit prohibited form language; the softened qualifier is not equivalent. |
| **V-03** | **FAIL** | Phase 3 carries positive ANCHOR-UPDATE INSTRUCTION (identical to V-01). The stale-anchor self-referential rule ("correctly recording the update at Phase 3 does not close this Phase 6 propagation requirement") is moved to Phase 6 integration rules as an additional bullet. C-31 is a co-location criterion: the prohibited form must be at Phase 3. Phase 6 placement satisfies C-30 (and provides additional C-30 depth) but does not substitute for Phase 3 co-location. |
| **V-04** | **FAIL** | Phase 3 carries ANCHOR-UPDATE PROHIBITED FORM block with "does not pass" language: "Carrying the Phase 1 preliminary anchor verbatim in Phase 6 when this branch recorded a higher-confidence step does not pass -- Phase 6 must reflect the Phase 3 update." Forward-looking form: names what Phase 6 must do and what Phase 6 failure looks like. Does NOT include: "recording the updated BEST-TRACEABLE ANCHOR here does not complete the propagation requirement." The self-referential phrase -- Phase 3 naming that its own record is insufficient -- is absent. C-31 specifically requires this self-referential form; forward-looking form is necessary but not sufficient. |
| **V-05** | **PASS** | Phase 3 carries: "recording the updated BEST-TRACEABLE ANCHOR here does not complete the propagation requirement. Phase 6 Falsification must also carry the updated step -- correctly recording the update here does not close the Phase 6 propagation requirement." Full self-referential form present. Additionally: Phase 6 integration rule explicitly names C-31 structural requirement (v11 signal); `phase3_anchor_update_prohibited_form: true\|false\|n/a` ARTIFACT field added (v11 signal). C-31 PASS. |

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational | Total | Delta | Tier |
|-----------|-----------|-------------|--------------|-------|-------|------|
| V-05 | 60/60 | 30/30 | 115/115 | **205/205** | baseline | Golden (ceiling) |
| V-01 | 60/60 | 30/30 | 110/115 | **200/205** | -5 (C-31) | Golden (floor) |
| V-02 | 60/60 | 30/30 | 110/115 | **200/205** | -5 (C-31) | Golden (floor) |
| V-03 | 60/60 | 30/30 | 110/115 | **200/205** | -5 (C-31) | Golden (floor) |
| V-04 | 60/60 | 30/30 | 110/115 | **200/205** | -5 (C-31) | Golden (floor) |

**Rank:** V-05 (205) > V-01 = V-02 = V-03 = V-04 (200, tied)

All five: all essential pass.

---

### Isolation Test Results

| Test | Hypothesis | Result | Verdict |
|------|-----------|--------|---------|
| V-01: Is Phase 3 PROHIBITED FORM independently required, or does Phase 6 C-30 enforcement alone cover it? | Phase 6 integration rule alone is sufficient | **FAIL** -- C-31 requires co-location at Phase 3; Phase 6 coverage is C-30, not C-31 |
| V-02: Does C-31 require "does not pass" / "does not complete" language, or does "necessary but not sufficient" satisfy? | Softened framing satisfies C-31 | **FAIL** -- parallel to C-22/C-20 and C-24/C-18; softened framing is not failure-mode naming |
| V-03: Does C-31 require Phase 3 co-location, or does Phase 6 equivalent rule satisfy? | Phase 6 placement satisfies C-31 | **FAIL** -- co-location at Phase 3 is the criterion; Phase 6 placement satisfies C-30/adds depth, not C-31 |
| V-04: Is the self-referential form ("recording here does not close Phase 6") load-bearing, or does forward-looking ("Phase 6 must carry") suffice? | Forward-looking form satisfies C-31 | **FAIL** -- naming the Phase 6 violation is necessary but not sufficient; Phase 3 must name its own record as insufficient |

All four hypotheses rejected. The discriminating elements are exactly as predicted.

---

### Excellence Signals from V-05

**1. Self-referential prohibited form at the update point is the load-bearing phrase.**
The phrase "recording the updated BEST-TRACEABLE ANCHOR here does not complete the propagation requirement" explicitly names Phase 3 as the site of insufficiency -- not Phase 6. This closes the escape hatch where a model treats Phase 3 update as the terminal requirement. V-01's positive instruction, V-02's softened note, V-03's Phase 6 placement, and V-04's forward-looking form all leave this escape hatch open in different ways.

**2. Dual-site enforcement achieves co-location symmetry.**
C-26/C-27 established the pattern: declaration point (Phase 1) must carry both the structural requirement AND the prohibition for omitting it. C-30/C-31 now achieves the same structure at the update point (Phase 3): C-30 requires the stale-anchor rule at Phase 6 (synthesis); C-31 requires the prohibited form at Phase 3 (update). V-05 completes this symmetric co-location chain.

**3. Phase 6 C-31 symmetry rule as v11 signal (fourth enforcement site).**
V-05 adds a Phase 6 integration rule explicitly naming the C-31 structural requirement -- that a Phase 3 positive-instruction-only without a PROHIBITED FORM does not pass C-31 even when C-30 passes. This mirrors C-29's role for C-26: Phase 6 detects the absence of the Phase 3 PROHIBITED FORM at the synthesis point. The pattern is: for each structural requirement at an earlier phase (C-26 at Phase 1, C-31 at Phase 3), Phase 6 integration rules should include a detection rule for the corresponding co-location violation.

**4. Machine-readable ARTIFACT field as v11 signal.**
`phase3_anchor_update_prohibited_form: true | false | n/a` extends the ARTIFACT layer to track C-31 compliance alongside `anchor_updated_from_phase1` (C-30). The pair makes the entire anchor propagation chain machine-auditable: did Phase 3 update the anchor, and did Phase 3 name that its own record is insufficient? These two fields together capture the C-30/C-31 status in the artifact frontmatter.

---

### V-11 Candidate Signals (from V-05)

V-05 scouts two potential v11 criteria:

| Signal | Structural parallel | V-05 element |
|--------|--------------------|----|
| C-31 symmetry rule at Phase 6 | C-29 (Phase 6 detects C-26 first-appearance violation) | Phase 6 integration rule: "a Phase 3 CONDITIONAL BRANCH carrying only a positive update instruction without a PROHIBITED FORM...does not pass C-31" |
| `phase3_anchor_update_prohibited_form` ARTIFACT field | `anchor_updated_from_phase1` for C-30 | ARTIFACT frontmatter: `phase3_anchor_update_prohibited_form: true \| false \| n/a` |

If v11 targets either, V-05 scores above 205 while V-01 through V-04 do not include these elements.

---

```json
{"top_score": 205, "all_essential_pass": true, "new_patterns": ["self-referential prohibited form at update point: Phase 3 must name that its own record is insufficient (recording here does not close Phase 6) -- forward-looking form naming Phase 6 failure is necessary but not sufficient for C-31", "dual-site co-location symmetry complete: C-26/C-27 govern the declaration point (Phase 1); C-30/C-31 govern the update point (Phase 3); each production point now carries both a structural requirement and a co-located prohibited form", "Phase 6 C-31 symmetry rule as v11 signal: Phase 6 integration rules should detect the absence of the Phase 3 PROHIBITED FORM at the synthesis point, paralleling C-29's detection of C-26 first-appearance-at-synthesis violation"]}
```
