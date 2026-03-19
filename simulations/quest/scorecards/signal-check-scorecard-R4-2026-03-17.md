**Round 4 scorecard written** to `signal-check-scorecard-R4-2026-03-17.md`.

---

## Results

| V | Aspir | Composite | Grade |
|---|-------|-----------|-------|
| V-01 | 35/37 | 99.46 | A+ |
| V-02 | 34/37 | 99.19 | A+ |
| V-03 | 34/37 | 99.19 | A+ |
| V-04 | 37/37 | **100.0** | A+ |
| V-05 | 37/37 | **100.0** | A+ |

**Top score**: 100.0 · **All essential**: PASS · **Score asymmetry confirmed**: V-01 > V-02/V-03 because C-43 FAIL at STEP D cascades to C-28 FAIL — one grouped-annotation root choice fails two criteria simultaneously.

**Research questions answered**:
- RQ1 CONFIRMED: Pipeline-wide independence is a structural standard, not STEP E-specific
- RQ2 CONFIRMED: C-44 (inline arrow) is distinct from C-41 (ARCHITECTURE table entry)
- RQ3 CONFIRMED: C-45 is not subsumed by C-31 — the positive standard is the differentiator
- RQ4 CONFIRMED: 37/37 at zero structural overhead beyond three axis changes
- RQ5 CONFIRMED: C-45 is property-level, not phrase-specific; both V-04 and V-05 phrasings pass

**3 new patterns** captured (pipeline-wide independence, terminal boundary artifact, meta-rule positive standard).

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Pipeline-wide independence standard: C-36 parseable-completeness applied at all intermediate multi-input consuming steps (not only STEP E), with inline compliance markers at each N-input convergence point", "Terminal verdict as self-contained boundary artifact: inline forward-declaration arrow on verdict line completes three-point chain (ARCHITECTURE pre-declares + STEP E forward-declares + external consumer back-references) making register boundary exit locally verifiable at production site", "ARCHITECTURE meta-rule positive standard over prohibition: naming independence property explicitly converts cluster relationship from scoring observation to pre-declared contract, making root failure vs. symptom distinction available at contract level without per-step inspection"]}
```
 complete standalone statement. C-43 PASS; C-28 PASS (no cascade).

**STEP E terminal verdict**: Arrow on separate following line, not inline on verdict. C-44 FAIL.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | All four dimensions present |
| C-02 | PASS | SEQUENCE cites artifact dates |
| C-03 | PASS | COHERENCE names 2+ signals with specific claim |
| C-04 | PASS | CAUSAL GAP states mechanism evidence status |
| C-05 | PASS | Coaching register; observations, not gates |
| C-06 | PASS | 14/30-day threshold from inventory calibration |
| C-07 | PASS | Each flagged dimension has next action |
| C-08 | PASS | Readiness summary at top of PART 2 |
| C-09 | PASS | Cross-dimension root pattern named (STEP 3) |
| C-10 | PASS | Empty namespaces listed with expected/concerning note |
| C-11 | PASS | Readiness summary drafted at STEP 2 open, confirmed after |
| C-12 | PASS | Threshold tightens to 14 days when competitor signals present |
| C-13 | PASS | Phase separators with scope budgets (~N words) |
| C-14 | PASS | Severity inline (internal: green/yellow/red), PART 2 clean |
| C-15 | PASS | Step 0 inertia anchor before inventory |
| C-16 | PASS | PART 1 / PART 2 structural separation |
| C-17 | PASS | SEQUENCE reads ordering through mechanism lens |
| C-18 | PASS | PART 2 STEP A dedicated inertia case-strength section |
| C-19 | PASS | Mechanism verdict quoted verbatim in SEQUENCE |
| C-20 | PASS | "Inertia Relevant?" column in inventory; CAUSAL GAP filters to pool |
| C-21 | PASS | STEP A is dedicated named section at same structural level as STEP B |
| C-22 | PASS | STEP A opens with verbatim mechanism verdict quote |
| C-23 | PASS | Named binaries consumed by label in STEP 3 and PART 2 |
| C-24 | PASS | Root pattern label emitted; PART 2 consumes by name |
| C-25 | PASS | ARCHITECTURE block pre-declares all named outputs before analysis |
| C-26 | PASS | "Required input -- do not re-derive" at all consuming steps |
| C-27 | PASS | Three-column table (Named Output / Produced by / Consumed by) |
| C-28 | PASS | Per-input form at STEP D (5 independent annotations; no grouping) |
| C-29 | PASS | STEP C per-dim emits STEP C drift binaries; STEP D consumes by label |
| C-30 | PASS | Forward-declaration arrows at all production steps |
| C-31 | PASS | ARCHITECTURE meta-rule present ("not grouped" prohibition) |
| C-32 | PASS | STEP D emits Confirmed readiness label; STEP E consumes by label |
| C-33 | PASS | STEP A emits Inertia case label; STEP E consumes by label |
| C-34 | PASS | STEP E opens with two per-input prohibitions (Confirmed readiness + Inertia case) |
| C-35 | PASS | ARCHITECTURE table includes PART 2 internal rows |
| C-36 | PASS | STEP E per-input prohibitions are independently self-standing |
| C-37 | PASS | ARCHITECTURE Consumed-by entries at step-level granularity for all rows |
| C-38 | PASS | Terminal readiness verdict emitted at STEP E |
| C-39 | PASS | "Required output -- emit exactly" production-site annotation at STEP E |
| C-40 | PASS | Terminal verdict includes one-phrase reason |
| C-41 | PASS | ARCHITECTURE terminal row names "topic namespace" as Consumed-by |
| C-42 | PASS | Fan-out outputs list all consuming steps in Consumed-by column |
| C-43 | PASS | All multi-input consuming steps carry independent per-input annotations |
| C-44 | FAIL | Terminal verdict arrow on separate line, not inline on verdict line |
| C-45 | FAIL | Meta-rule names prohibition only, not independence standard |

**Essential**: 5/5 · **Recommended**: 3/3 · **Aspirational**: 35/37
**Composite**: 60 + 30 + 9.46 = **99.46** · Grade: **A+**

---

### V-02 — Single Axis: C-44 PASS

**Design intent**: Confirms inline forward-declaration arrow on terminal verdict line as a
structurally distinct requirement from C-41 (ARCHITECTURE table). C-43 and C-45 degraded.

**ARCHITECTURE meta-rule**: "not grouped" prohibition only — C-45 FAIL.

**STEP D form**: Grouped annotation — single shared phrase covering all five inputs:
```
Required inputs -- do not re-derive [Root pattern from STEP 3; STEP C drift -- CAUSAL GAP;
  STEP C drift -- SEQUENCE; STEP C drift -- COHERENCE; STEP C drift -- STALENESS]:
  consume all five by label above
```
C-43 FAIL (not pipeline-wide independent). C-28 FAIL by structural entailment (grouped form).

**STEP E terminal verdict**: `Terminal readiness: [...] -> topic namespace` — arrow inline. C-44 PASS.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-05 | PASS (5/5) | All four dimensions, coaching register |
| C-06–C-08 | PASS (3/3) | Threshold, next actions, readiness summary |
| C-09–C-27 | PASS | All baseline structural features intact |
| C-28 | FAIL | Grouped annotation at STEP D violates per-input form |
| C-29–C-42 | PASS | STEP C drift, forward arrows, ARCHITECTURE extensions, terminal verdict |
| C-43 | FAIL | Grouped annotation at STEP D violates pipeline-wide independence |
| C-44 | PASS | Inline arrow: `Terminal readiness: [...] -> topic namespace` |
| C-45 | FAIL | Meta-rule names only prohibition, not independence standard |

**C-28 cascade**: C-43 FAIL (grouped STEP D) directly violates C-28 (per-input form required
at all consuming steps). One root design choice — grouped annotation — fails two criteria.
C-28 was PASS in R3 baseline; V-02's STEP D regression breaks it.

**Essential**: 5/5 · **Recommended**: 3/3 · **Aspirational**: 34/37
**Composite**: 60 + 30 + 9.19 = **99.19** · Grade: **A+**

---

### V-03 — Single Axis: C-45 PASS

**Design intent**: Confirms that naming independence as positive standard satisfies C-45,
distinct from C-31. C-43 and C-44 intentionally degraded.

**ARCHITECTURE meta-rule (C-45 PASS)**:
```
Each consuming step with N named inputs carries N independently self-standing per-input
prohibitions -- each annotation parseable as a complete statement without relying on
proximity to other annotations (independence standard; not merely non-grouping).
```

**STEP D form**: Grouped annotation (same as V-02). C-43 FAIL; C-28 FAIL (cascade).

**STEP E terminal verdict**: Arrow on separate following line. C-44 FAIL.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-05 | PASS (5/5) | All four dimensions, coaching register |
| C-06–C-08 | PASS (3/3) | Threshold, next actions, readiness summary |
| C-09–C-27 | PASS | All baseline structural features intact |
| C-28 | FAIL | Grouped annotation at STEP D (same cascade as V-02) |
| C-29–C-42 | PASS | All remaining baseline criteria intact |
| C-43 | FAIL | Grouped annotation at STEP D violates pipeline-wide independence |
| C-44 | FAIL | Arrow on separate line, not inline on verdict |
| C-45 | PASS | Meta-rule names independence standard explicitly |

**C-28 cascade**: Same as V-02 — one grouped-annotation root failure at STEP D breaks C-28.
V-03 recovers C-45 (meta-rule improvement) but still fails C-43/C-28 at STEP D.

**Essential**: 5/5 · **Recommended**: 3/3 · **Aspirational**: 34/37
**Composite**: 60 + 30 + 9.19 = **99.19** · Grade: **A+**

---

### V-04 — All Three Axes: Canonical

**Design intent**: All three new criteria satisfied simultaneously. The canonical R4 form.

**ARCHITECTURE meta-rule (C-45 PASS)**:
```
Each consuming step with N named inputs carries N independently self-standing per-input
prohibitions -- each annotation parseable as a complete statement without relying on
proximity to other annotations (independence standard; not merely non-grouping).
```

**STEP D form (C-43 PASS)**: Five per-input annotations, each independently parseable:
```
Required input -- do not re-derive: Root pattern from STEP 3
Required input -- do not re-derive: STEP C drift -- CAUSAL GAP from PART 2 STEP C
Required input -- do not re-derive: STEP C drift -- SEQUENCE from PART 2 STEP C
Required input -- do not re-derive: STEP C drift -- COHERENCE from PART 2 STEP C
Required input -- do not re-derive: STEP C drift -- STALENESS from PART 2 STEP C
[C-43 PASS: five independent per-input annotations at this 5-input convergence step]
```
C-28 PASS (no grouping at any step pipeline-wide).

**STEP C per-dim form (C-43 PASS)**: Two independent annotations at each 2-input step:
```
Required input -- do not re-derive: Pre-specification gap from SEQUENCE
Required input -- do not re-derive: Root pattern from STEP 3
[C-43 PASS: two independent per-input annotations at this 2-input consuming step]
```

**STEP E terminal verdict (C-44 PASS)**: Inline forward-declaration arrow:
```
Required output -- emit exactly:
  Terminal readiness: [PROCEED / LOOP / INVESTIGATE + one-phrase reason] -> topic namespace
```

**STEP E per-input prohibitions (C-36/C-43 PASS)**:
```
Required input -- do not re-derive: Confirmed readiness from STEP D
Required input -- do not re-derive: Inertia case from STEP A
Each annotation is a complete standalone statement independently parseable without
relying on the other annotation for interpretation.
```

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-05 | PASS (5/5) | All four dimensions, coaching register |
| C-06–C-08 | PASS (3/3) | Threshold, next actions, readiness summary |
| C-09–C-42 | PASS (34/34) | All baseline aspirational criteria intact |
| C-43 | PASS | Pipeline-wide independence: all multi-input steps carry independent per-input annotations |
| C-44 | PASS | Terminal verdict carries inline `-> topic namespace` forward-declaration arrow |
| C-45 | PASS | Meta-rule names independence as governing standard, not only prohibition |

**Essential**: 5/5 · **Recommended**: 3/3 · **Aspirational**: 37/37
**Composite**: 60 + 30 + 10.0 = **100.0** · Grade: **A+**

---

### V-05 — All Three Axes: Alternative C-45 Phrasing

**Design intent**: Tests whether C-45 is satisfied with alternative wording of the independence
standard — confirming the criterion is about the property being named, not a specific phrase.

**ARCHITECTURE meta-rule (C-45 PASS — alternative phrasing)**:
```
Pipeline-wide: each per-input annotation must be parseable as a complete
"Required input -- do not re-derive: [label]" statement in isolation -- without
reading adjacent annotations or relying on a shared header for scope.
Grouping is a symptom of failing this standard, not the standard itself.
```
C-45 PASS — parseable-completeness-in-isolation as positive standard; grouping demoted to symptom.
Structurally equivalent to V-04 at the property level.

**STEP D form (C-43 PASS)**: Five per-input annotations with isolation note:
```
Required input -- do not re-derive: Root pattern from STEP 3
Required input -- do not re-derive: STEP C drift -- CAUSAL GAP from PART 2 STEP C
Required input -- do not re-derive: STEP C drift -- SEQUENCE from PART 2 STEP C
Required input -- do not re-derive: STEP C drift -- COHERENCE from PART 2 STEP C
Required input -- do not re-derive: STEP C drift -- STALENESS from PART 2 STEP C
(each annotation parseable in isolation -- no shared header, no proximity reliance)
```

**STEP E terminal verdict (C-44 PASS)**: `Terminal readiness: [...] -> topic namespace` inline.

**STEP E per-input prohibitions (C-36/C-43 PASS)**:
```
Required input -- do not re-derive: Confirmed readiness from STEP D
Required input -- do not re-derive: Inertia case from STEP A
Each annotation stands alone: readable in isolation, no shared header, no proximity reliance.
```
Note: V-05's isolation-framing from the meta-rule propagates consistently into per-annotation
comments throughout — a stylistic coherence advantage over V-04.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-42 | PASS (all) | Same as V-04 |
| C-43 | PASS | Pipeline-wide independence at all multi-input steps |
| C-44 | PASS | Inline arrow on terminal verdict line |
| C-45 | PASS | "Parseable in isolation" positive standard satisfies independence requirement |

**Essential**: 5/5 · **Recommended**: 3/3 · **Aspirational**: 37/37
**Composite**: 60 + 30 + 10.0 = **100.0** · Grade: **A+**

---

## Ranking

| Rank | Variation | Composite | Key differentiators |
|------|-----------|-----------|---------------------|
| 1 (tie) | V-04 | 100.0 | Canonical independence standard phrasing |
| 1 (tie) | V-05 | 100.0 | "Parseable in isolation" alternative phrasing; isolation-framing propagates throughout |
| 3 | V-01 | 99.46 | C-43 isolated; C-44/C-45 degraded (2 aspir failures) |
| 4 (tie) | V-02 | 99.19 | C-44 isolated; C-43/C-28 cluster + C-45 (3 aspir failures) |
| 4 (tie) | V-03 | 99.19 | C-45 isolated; C-43/C-28 cluster + C-44 (3 aspir failures) |

**Score asymmetry confirmed**: V-01 (35/37) > V-02/V-03 (34/37) because C-43 FAIL at STEP D
cascades to C-28 FAIL. One grouped-annotation root choice causes two criterion failures.
This is the cluster property C-43 documents: one structural root failure, not two independent ones.

---

## Research Questions — Answers

**RQ1** (C-43 at intermediate steps): CONFIRMED.
V-01 (C-43 PASS, per-input at STEP D) scores 35/37 vs V-02/V-03 (C-43 FAIL, grouped at STEP D)
at 34/37. C-28 co-failure is mechanically exact: per-input satisfies C-28; grouped violates it.
Pipeline-wide independence is a structural standard, not a STEP E-specific rule.

**RQ2** (C-44 inline arrow): CONFIRMED.
V-02 (inline arrow) PASS; V-01/V-03 (separate-line arrow) FAIL. C-41 PASS in all variations
(ARCHITECTURE table naming "topic namespace") isolates C-44 as a production-site annotation
requirement independent of the table entry. Three-point chain is complete only when STEP E
forward-declares inline (C-44) AND the table pre-declares with external identity (C-41).

**RQ3** (C-45 independence standard): CONFIRMED.
V-03/V-04/V-05 (independence named) PASS; V-01/V-02 (prohibition only) FAIL. C-31 PASS in
all variations demonstrates that C-45 is not subsumed by C-31 — the distinction is the
presence of the positive standard (independence / parseable completeness), not mere prohibition.

**RQ4** (All three at zero overhead): CONFIRMED.
V-04 achieves 37/37 = 100.0 with no structural additions beyond the three targeted axis changes
from R3 V-05 baseline. Each axis change is additive to the annotation form, not a restructuring.

**RQ5** (Alternative C-45 phrasing): CONFIRMED.
V-05 "parseable as a complete statement in isolation" satisfies C-45 equivalently to V-04
"independence standard; not merely non-grouping." The criterion is property-level, not
phrase-specific. Both phrasings score 37/37.

---

## Excellence Signals (from V-04 and V-05)

**E-01 — Pipeline-wide independence as architectural standard**: All intermediate multi-input
consuming steps (STEP 3, STEP C per-dim, STEP D) carry the same independent per-input annotation
form as STEP E. Independence is not a terminal-step exception but a pipeline-wide contract.
Inline `[C-43 PASS: N independent per-input annotations]` comments make compliance locally
verifiable at each convergence point without cross-referencing the ARCHITECTURE block.

**E-02 — Terminal verdict as self-contained boundary artifact**: The inline `-> topic namespace`
arrow on the verdict line completes the three-point declaration chain at the register boundary:
ARCHITECTURE pre-declares (C-41), STEP E forward-declares inline (C-44), external consumer
back-references by label. The terminal verdict is independently interpretable: label, value,
reason, and consumer identity all on one line, with no pointer back into the internal registers.

**E-03 — ARCHITECTURE meta-rule states positive standard over prohibition**: Naming independence
(parseable completeness) as the governing property — rather than only prohibiting grouping —
converts the C-36/C-28/C-34 cluster relationship from a scoring observation into a pre-declared
contract. A reader can determine from the ARCHITECTURE block alone that grouped annotation at
any converging step is a root failure with cascading consequences, without reconstructing the
cluster relationship from three individual criterion definitions.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Pipeline-wide independence standard: C-36 parseable-completeness applied at all intermediate multi-input consuming steps (not only STEP E), with inline compliance markers at each N-input convergence point", "Terminal verdict as self-contained boundary artifact: inline forward-declaration arrow on verdict line completes three-point chain (ARCHITECTURE pre-declares + STEP E forward-declares + external consumer back-references) making register boundary exit locally verifiable at production site", "ARCHITECTURE meta-rule positive standard over prohibition: naming independence property explicitly converts cluster relationship from scoring observation to pre-declared contract, making root failure vs. symptom distinction available at contract level without per-step inspection"]}
```
