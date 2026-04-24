# quest-score Variations -- Round 8
**Skill**: quest-score
**Rubric**: v7 (N_essential=5, N_recommended=2, N_aspirational=17)
**Date**: 2026-03-15
**Round**: 8

---

## Design logic

### Unachieved ceilings entering R8

R7 V-05 was the full stack against the v6 rubric (N_aspirational=13, formula `/13 * 130`).
Rubric v7 adds C-21 through C-24 and updates the formula to `/17 * 170`. Against v7,
R7 V-05 scores:

| Criterion | R7 V-05 status | Gap |
|-----------|----------------|-----|
| C-03 | FAIL (formula) | Uses `aspirational_pass / 13 * 130` (v6 weights). v7 requires `/ 17 * 170`. Wrong denominator and weight produce incorrect composite. |
| C-21 | Expected PASS | R7 V-05 carries "Do not begin until [SCORER COMPLETE] appears above" in VERIFIER and "Do not begin until [VERIFIER COMPLETE] appears above" in ANALYST. Both downstream roles declare entry conditions. |
| C-22 | PARTIAL | R7 V-05 annotates three ANALYST narrative fields as "this field is required" (the C-22 source). SCORER fields (Verdict, Evidence, *Why*, *Change*) and VERIFIER fields are not annotated inline as required. C-22 requires EVERY mandatory field in EVERY phase's output schema to carry the annotation -- not just narrative fields. |
| C-23 | Expected PASS | R7 V-03/V-04/V-05 state: "No additional fields are permitted. Narrative text, synthesis language, per-output summaries, and evaluative prose are PROHIBITED." This names the complete permitted set AND prohibits named non-verdict field types. |
| C-24 | PASS in V-04/V-05 | R7 V-04/V-05 have `[SYNTHESIS OPEN]` / pre-close checklist (5 checkbox items) / `[SYNTHESIS COMPLETE]`. Gate pair with enumerated checklist present. |

Primary gap for R8: **C-22** is the only criterion where ALL R7 variations score PARTIAL
or FAIL. No variation annotated SCORER or VERIFIER fields as required at the label site.
The formula update is a forced infrastructure change. Baseline table extends to C-24.

Secondary diagnostics: (1) Does the implicit prohibition in R7 V-01 ("no additional fields
permitted") satisfy C-23, or does C-23 require named forbidden types? Single-axis V-03 (PRB)
isolates this. (2) Does R7 V-02's gate pair with preamble satisfy C-24, or does C-24 require
a numbered pre-close checklist? Single-axis V-02 (CKL) isolates this. V-01 R7 already
satisfies C-21 (bidirectional gates present in both downstream roles); R8 carries this forward.

### New axes for R8

| Axis | Label | Mechanism | Target criteria |
|------|-------|-----------|-----------------|
| REQ | Exhaustive required-field annotation | Every mandatory field in every phase output schema carries "(required)" at the field label -- SCORER: Verdict/Evidence/*Why*/*Change*; VERIFIER: each review field; ANALYST: narrative fields. Tests whether C-22 PASS requires all-phase coverage vs. narrative-only. | C-22 |
| CKL | Explicit pre-close synthesis checklist | Replace synthesis preamble gate instruction ("all sections required before closing") with a numbered checkbox pre-close checklist naming each required section; closing token cannot appear until each checkbox is confirmed. Tests C-24 against gate pair + checklist requirement vs. preamble form. | C-24 |
| PRB | Named FORBIDDEN TYPES schema prohibition | Extend SCORER schema prohibition from implicit "no additional fields" form to an explicit FORBIDDEN TYPES list naming *Why*, *Note*, narrative text, evaluative prose, mechanism analysis, and synthesis language as schema violations by type. Tests whether C-23 PASS requires named-type prohibition vs. implicit exclusion. | C-23 |

### Single-axis selections (V-01, V-02, V-03)

- **V-01 (REQ)**: R7 V-01 base (SCORER/VERIFIER/ANALYST, three-field labeled narrative,
  no anchor, no *Why*, no *Change*, no baseline). Single change: every mandatory field in
  every phase output schema carries "(required)" at the label site. Formula /17 * 170.
  Predicts: C-22 PASS (all fields annotated at label); C-21 PASS (bidirectional "do not
  begin until" carried from R7 V-01); C-23 FAIL (no SCORER schema prohibition beyond "no
  extra fields"); C-24 FAIL (ANALYST ends with [ANALYST COMPLETE], not a synthesis gate pair
  with pre-close checklist); C-11/C-13/C-14/C-15/C-16 FAIL (no *Why*/*Change*/baseline).

- **V-02 (CKL)**: R7 V-02 base (single-phase scoring, no named roles, [SYNTHESIS OPEN] /
  [SYNTHESIS COMPLETE] gate pair). Single change: replace preamble gate instruction ("all
  four sections required inside this gate") with a numbered pre-close checklist between
  [SYNTHESIS OPEN] and [SYNTHESIS COMPLETE] that itemizes each required section with a
  checkbox. Formula /17 * 170.
  Predicts: C-24 PASS (gate pair + named-section pre-close checklist); C-20 FAIL (no named
  role sequence); C-21 FAIL (no downstream roles carrying entry conditions); C-22 PARTIAL
  (narrative fields annotated, SCORER Verdict/Evidence fields not annotated); C-23 FAIL (no
  SCORER schema prohibition).

- **V-03 (PRB)**: R7 V-01 base (SCORER/VERIFIER/ANALYST, three-field narrative) PLUS
  SCORER schema prohibition extended from implicit "no additional fields" to explicit named
  FORBIDDEN TYPES list. Bidirectional gate inscription carried from R7 V-01. Formula /17*170.
  Predicts: C-23 PASS (named forbidden types close schema-ambiguity path); C-12 PASS (schema
  violation is named and format-detectable); C-21 PASS; C-22 PARTIAL (narrative fields
  annotated, SCORER fields not); C-24 FAIL (no synthesis gate pair).

### Combination selections (V-04, V-05)

- **V-04 (REQ + CKL)**: V-03 base (role architecture, named SCORER prohibition, three-field
  narrative) PLUS REQ (all mandatory fields annotated) PLUS CKL (synthesis gate pair with
  explicit pre-close checklist). C-22 and C-24 are declared orthogonal: C-22 operates on
  field-level annotation within schemas; C-24 operates on phase-level gate architecture at
  the synthesis boundary. Combined test confirms orthogonality -- satisfying both does not
  create structural conflict. Formula /17 * 170.
  Predicts: C-21 PASS, C-22 PASS, C-23 PASS, C-24 PASS, C-12 PASS, C-19 PASS, C-20 PASS;
  C-09/C-11/C-13/C-14/C-15/C-16 FAIL (no *Why*/*Change*/baseline/anchor from V-03 base).

- **V-05 (Full stack R8)**: R7 V-05 full-stack architecture (7 named mechanisms, 7 failure-mode
  blocks, *Why*, *Change*, Change Manifest, Baseline Load, synthesis gate pair, VERIFIER role,
  three-field narrative, SCORER schema prohibition, inter-role gates) PLUS: REQ (C-22, all
  fields annotated), CKL (C-24, explicit pre-close checklist), PRB (C-23, named forbidden
  types), Mechanisms 8-11 declared with Failure Modes H-K in the anchor. Formula /17 * 170.
  Baseline table extended to include C-21 through C-24.
  Predicts: all C-01 through C-24 PASS; composite 260/260.

### Variation matrix

| Element | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|------|------|------|------|------|
| Axis | REQ | CKL | PRB | REQ+CKL | Full stack |
| Formula `/17 * 170` | YES | YES | YES | YES | YES |
| Named role sequence SCORER/VERIFIER/ANALYST (C-20) | YES | NO | YES | YES | YES |
| [SCORER COMPLETE] / [VERIFIER COMPLETE] inter-role gates (C-20) | YES | NO | YES | YES | YES |
| Bidirectional "Do not begin until" in all downstream roles (C-21) | YES | NO | YES | YES | YES |
| All mandatory fields annotated "(required)" at label site (C-22) | YES | NO | NO | YES | YES |
| SCORER schema prohibition -- base form (C-12P, C-23) | NO | NO | YES | YES | YES |
| SCORER schema prohibition -- named FORBIDDEN TYPES (C-23) | NO | NO | YES | YES | YES |
| Synthesis gate pair [SYNTHESIS OPEN]/[SYNTHESIS COMPLETE] (C-10) | NO | YES | NO | YES | YES |
| Pre-close checklist with named sections (C-24) | NO | YES | NO | YES | YES |
| Three-field labeled narrative in ANALYST (C-19) | YES | YES | YES | YES | YES |
| *Why*: field per criterion (C-11) | NO | NO | NO | NO | YES |
| Mandatory *Change*: field (C-15) | NO | NO | NO | NO | YES |
| Change Manifest phase (C-16) | NO | NO | NO | NO | YES |
| Anti-pattern anchor (C-09) | NO | NO | NO | NO | YES |
| Baseline Load gate + table to C-24 (C-14) | NO | NO | NO | NO | YES |
| Mechanisms 8-11 / Failure Modes H-K | NO | NO | NO | NO | YES |
| Total named mechanisms / failure-mode blocks | 0/0 | 0/0 | 0/0 | 0/0 | 11/11 |

---

## V-01 -- Axis REQ: Exhaustive required-field annotation, minimal base

**Variation axis**: Depth -- every mandatory field in every phase output schema carries a
"(required)" annotation at the field label. R7 V-01 base architecture: SCORER/VERIFIER/ANALYST
named role sequence, three-field labeled narrative, no anchor, no *Why*, no *Change*, no
baseline load gate. Single change from R7 V-01: extend the "(required)" annotation (which
appeared only on three ANALYST narrative fields in R7 V-01) to every mandatory field in
every phase output schema -- SCORER Verdict and Evidence, VERIFIER review fields, and
ANALYST narrative fields. Formula updated to `/17 * 170`.

**Hypothesis**: C-22's pass condition requires annotation "at the field label" in "every
phase's output schema." R7 V-01 annotated only the three ANALYST narrative fields (the
behavior that caused C-22 to be derived as a new criterion). Extending the annotation to
SCORER fields (Verdict, Evidence) and VERIFIER fields reaches every mandatory field across
all three phases. Inline "(required)" at the field label makes field omission syntactically
visible at the schema site without a separate completeness audit -- a criterion block with
no Verdict line is a visibly incomplete block, not just a behavioral gap. Predicts: C-22
PASS; C-21 PASS (bidirectional "do not begin until" carried from R7 V-01); C-23 FAIL (SCORER
schema says "no additional fields" but does not name explicit forbidden types); C-24 FAIL
(ANALYST ends with [ANALYST COMPLETE], not a synthesis gate pair with pre-close checklist).

```
You are running quest-score. This run uses three sequential roles.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with a specific evidence entry,
a composite score computed from the rubric formula, and a golden-threshold
determination. The scorecard includes a ranked leaderboard, excellence signals,
failure patterns, regression signals, and per-output narrative notes.

---

ROLE 1: SCORER

The Scorer produces a per-criterion verdict and evidence entry for every output.
The Scorer does not verify evidence specificity -- that is the Verifier's role.
The Scorer does not produce narratives or synthesis -- those are the Analyst's role.

SCORER CRITERION BLOCK SCHEMA

Every criterion block in SCORER output consists of exactly these two fields:

  Verdict:  PASS | PARTIAL | FAIL  (required)
  Evidence: [specific structural observation from this output only]  (required)

No fields beyond Verdict and Evidence are permitted in SCORER criterion blocks.

For each output:

  Output: [output identifier]

  For each criterion C-01 through C-24:

  C-[NN] -- [criterion name] ([weight: E | R | A])
  Verdict:  PASS | PARTIAL | FAIL  (required)
  Evidence: [specific quote or structural observation from this output;
             uniquely identifies this output -- not a description that could
             apply to any well-designed output of this type]  (required)

  No criterion may be skipped.  (required: no cell may be blank)

  After all criteria for one output:

    essential_pass    = [count of E criteria at PASS; PARTIAL = 0.5]  (required)
    recommended_pass  = [count of R criteria at PASS; PARTIAL = 0.5]  (required)
    aspirational_pass = [count of A criteria at PASS; PARTIAL = 0.5]  (required)

    composite = (essential_pass / 5 * 60)
              + (recommended_pass / 2 * 30)
              + (aspirational_pass / 17 * 170)
              = [result]  (required)

    Golden: YES -- all 5 essentials PASS; composite >= 80  (required)
         |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.

[SCORER COMPLETE]

---

ROLE 2: VERIFIER

Do not begin until [SCORER COMPLETE] appears above.

The Verifier reviews every evidence entry produced by the Scorer and applies the
specificity test. The Verifier does not modify verdicts or composite scores.

VERIFIER REVIEW BLOCK SCHEMA

  Output: [output identifier] | C-[NN]  (required)
  Scorer evidence: [copy from SCORER output above]  (required)
  Specificity: PASS | FAIL  (required)

If Specificity is FAIL:
  Revised evidence: [rewrite with specific structural property unique to this output]  (required)

Specificity test: ask "could this evidence apply to any well-designed output of this
type?" YES = generic = FAIL = revision required before Analyst may use this cell.

After all outputs:
  Verification summary: [N cells reviewed; K revised; list revised cell IDs
                         or "none revised"]  (required)

[VERIFIER COMPLETE]

---

ROLE 3: ANALYST

Do not begin until [VERIFIER COMPLETE] appears above.

The Analyst uses the Scorer's verdicts and composite scores (substituting Verifier's
revised evidence where applicable) to produce synthesis and per-output narratives.

LEADERBOARD

Rank all outputs by composite score descending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] -- [criterion ID] -- [structural mechanism causing the
          difference; name the design property, not the criterion label]

If all outputs score identically on all criteria: "No differentiating excellence signals."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

If prior-round score data is provided, identify any criterion-output pair where
a verdict degraded (PASS to PARTIAL, PASS to FAIL, or PARTIAL to FAIL):

  Output: [output ID]
    C-[NN]: prior [verdict] --> now [verdict] -- [reason]

If no regressions: "No regressions detected this round."
If no prior data: "No prior round data; regression analysis not possible."

PER-OUTPUT NARRATIVE

For each scored output, write three prescribed labeled fields:

  Output [output identifier]:
  Primary differentiator:  [the one structural feature that explains why this output
                            scored differently from the field; name the design property,
                            not the criterion label]  (required)
  Primary miss:            [the criterion or structural mechanism this output most
                            clearly failed to implement; name the gap precisely; write
                            "None -- all criteria passed" if output is all-PASS]  (required)
  Verdict spread:          [where this output concentrated its points and why; explain
                            the distribution pattern across essential / recommended /
                            aspirational tiers]  (required)

[ANALYST COMPLETE]
```

---

## V-02 -- Axis CKL: Explicit pre-close synthesis checklist, single-phase base

**Variation axis**: Lifecycle emphasis -- the synthesis completion gate is a gate pair
([SYNTHESIS OPEN] / [SYNTHESIS COMPLETE]) enclosing a numbered pre-close checklist that
explicitly names each required section. R7 V-02 base architecture: single-phase scoring,
no named roles, no *Why*, no *Change*, no baseline, no anchor. Single change from R7 V-02:
replace the preamble gate instruction ("All four sections below are required inside this
gate. Do not write [SYNTHESIS COMPLETE] until every section is present.") with a numbered
checkbox pre-close checklist that itemizes each required section by name. Formula /17*170.

**Hypothesis**: R7 V-02 had the [SYNTHESIS OPEN] / [SYNTHESIS COMPLETE] gate pair (C-10)
but no numbered pre-close checklist -- the sections were enclosed within the gate but the
closing instruction was a preamble, not an itemized checklist. C-24's pass condition requires
"a pre-close checklist that enumerates each required synthesis section" and "explicitly
requires confirming each section before writing the closing token." A numbered checkbox list
naming failure patterns, leaderboard, and excellence signals makes section omission visible
without reading the full synthesis body: a missing section leaves a checkbox blank. Tests
whether C-24 requires the enumeration form or whether R7 V-02's preamble form already
satisfies it. Predicts: C-24 PASS (explicit gate pair + named-section pre-close checklist);
C-20 FAIL (no named role sequence); C-21 FAIL (no downstream roles carrying entry conditions);
C-22 PARTIAL (narrative fields annotated, SCORER Verdict/Evidence not); C-23 FAIL (no
SCORER schema prohibition).

```
You are running quest-score.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with a specific evidence entry,
a composite score computed from the rubric formula, and a golden-threshold
determination. The scorecard includes a ranked leaderboard, excellence signals,
failure patterns, regression signals, and per-output narrative notes.

---

SCORING PHASE

For each output, produce a criterion block for every rubric criterion:

  Output: [output identifier]

  C-[NN] -- [criterion name] ([weight: E | R | A])
  Verdict:  PASS | PARTIAL | FAIL
  Evidence: [specific quote or structural observation from this output;
             uniquely identifies this output -- not a description that could
             apply to any well-designed output of this type]

  No criterion may be skipped. No Evidence field may be blank.

  After all criteria for one output:

    essential_pass    = [count of E criteria at PASS; PARTIAL = 0.5]
    recommended_pass  = [count of R criteria at PASS; PARTIAL = 0.5]
    aspirational_pass = [count of A criteria at PASS; PARTIAL = 0.5]

    composite = (essential_pass / 5 * 60)
              + (recommended_pass / 2 * 30)
              + (aspirational_pass / 17 * 170)
              = [result]

    Golden: YES -- all 5 essentials PASS; composite >= 80
         |  NO  -- [which essential failed, or composite < 80]

  Immediately after the composite score, write the narrative scaffold:

  NARRATIVE -- [output identifier]:
  Primary differentiator:  [the one structural feature that explains why this output
                            scored differently from the field; name the design property,
                            not the criterion label]  (required)
  Primary miss:            [the criterion or structural mechanism this output most
                            clearly failed to implement; name the gap precisely]  (required)
  Verdict spread:          [where this output concentrated its points and why; explain
                            the distribution across essential / recommended /
                            aspirational tiers]  (required)

Score all N outputs, each followed by its NARRATIVE scaffold.

[SCORING COMPLETE]

---

SYNTHESIS

[SYNTHESIS OPEN]

Produce the four required sections below. Before writing [SYNTHESIS COMPLETE], work
through the pre-close checklist. Each checkbox must be confirmed present; the closing
gate token may not appear while any checkbox is unconfirmed.

LEADERBOARD

Rank all outputs by composite score descending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] -- [criterion ID] -- [structural mechanism causing the
          difference; name the design property, not the criterion label]

If all outputs score identically: "No score spread found."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

If prior-round score data is provided, identify any criterion-output pair where
a verdict degraded:

  Output: [output ID]
    C-[NN]: prior [verdict] --> now [verdict] -- [reason]

If no regressions: "No regressions detected this round."
If no prior data: "No prior round data; regression analysis not possible."

PRE-CLOSE CHECKLIST -- confirm each item before writing [SYNTHESIS COMPLETE]:

  [ ] 1. LEADERBOARD: all N outputs ranked by composite score descending;
         ties broken or noted; Golden status shown for each output.
  [ ] 2. EXCELLENCE SIGNALS: output-criterion outlier pair named with structural
         mechanism, OR "No score spread found" written explicitly.
  [ ] 3. FAILURE PATTERNS: all criteria with zero PASS across all outputs
         identified with diagnosis, OR "No failure patterns in this round" written.
  [ ] 4. REGRESSION SIGNALS: prior-round degradations listed, OR "No regressions
         detected" / "No prior round data" written explicitly.

[SYNTHESIS COMPLETE]
```

---

## V-03 -- Axis PRB: Named FORBIDDEN TYPES schema prohibition, minimal base

**Variation axis**: Phrasing register + enforcement -- the SCORER criterion block schema
names the complete permitted field set AND includes a FORBIDDEN TYPES list that names each
prohibited field type explicitly. R7 V-01 base architecture: SCORER/VERIFIER/ANALYST, three-
field labeled narrative, no anchor, no *Why*, no *Change*, no baseline. Single change from
R7 V-01: add a FORBIDDEN TYPES list to the SCORER schema that names *Note*, *Comment*,
*Observation*, narrative text, evaluative prose, mechanism analysis, and synthesis language
as schema violations. Bidirectional gate inscription ("Do not begin until") carried from R7
V-01. Formula /17 * 170.

**Hypothesis**: R7 V-01 had no SCORER schema prohibition at all (C-12 PARTIAL, spawning C-23).
R7 V-03 added "No additional fields are permitted. Narrative text, synthesis language, per-
output summaries, and evaluative prose are PROHIBITED" -- this should satisfy C-23 (names
complete permitted set + explicit prohibition on named types). Axis PRB tests this in isolation
on the minimal V-01 base, without the full role infrastructure: does schema prohibition alone
(without Change infrastructure or anchor) produce C-23 PASS? Also tests C-12: does adding a
named-type prohibition to the minimal base tip C-12 from PARTIAL to PASS? The permitted-set
naming ("exactly Verdict and Evidence") combined with the FORBIDDEN TYPES label produces a
schema where a third field is a named structural violation detectable by field-count inspection.
Predicts: C-23 PASS (named forbidden types, explicit exclusion rule stated in SCORER definition);
C-12 PASS (schema prohibition makes narrative-in-SCORER a named structural violation); C-21
PASS (carried from R7 V-01); C-22 PARTIAL (narrative fields annotated, SCORER fields not);
C-24 FAIL (no synthesis gate pair).

```
You are running quest-score. This run uses three sequential roles.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with a specific evidence entry,
a composite score computed from the rubric formula, and a golden-threshold
determination. The scorecard includes a ranked leaderboard, excellence signals,
failure patterns, regression signals, and per-output narrative notes.

---

ROLE 1: SCORER

SCORER CRITERION BLOCK SCHEMA

Every criterion block in SCORER output consists of exactly and only these two fields:

  Verdict:  PASS | PARTIAL | FAIL
  Evidence: [specific structural observation from this output]

PERMITTED FIELDS: Verdict and Evidence only.
FORBIDDEN FIELDS: *Why*, *Change*, *Note*, *Comment*, *Observation*, and any field
not in the permitted list. Narrative text, evaluative prose, mechanism analysis,
interpretation, synthesis language, structural commentary, and per-output summaries
are SCHEMA VIOLATIONS in SCORER blocks. A SCORER criterion block containing any
forbidden field or free text beyond Verdict and Evidence is structurally malformed and
can be detected by field-count inspection. All mechanism analysis, narrative, and
commentary belong exclusively in the Analyst's PER-OUTPUT NARRATIVE section.

---

For each output:

  Output: [output identifier]

  For each criterion C-01 through C-24:

  C-[NN] -- [criterion name] ([weight: E | R | A])
  Verdict:  PASS | PARTIAL | FAIL
  Evidence: [specific quote or structural observation from this output;
             uniquely identifies this output -- not a description that could
             apply to any well-designed output of this type]

  No criterion may be skipped.
  No Evidence field may be blank.
  No field beyond Verdict and Evidence may appear in a SCORER criterion block.

  After all criteria for one output:

    essential_pass    = [count of E criteria at PASS; PARTIAL = 0.5]
    recommended_pass  = [count of R criteria at PASS; PARTIAL = 0.5]
    aspirational_pass = [count of A criteria at PASS; PARTIAL = 0.5]

    composite = (essential_pass / 5 * 60)
              + (recommended_pass / 2 * 30)
              + (aspirational_pass / 17 * 170)
              = [result]

    Golden: YES -- all 5 essentials PASS; composite >= 80
         |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.

[SCORER COMPLETE]

---

ROLE 2: VERIFIER

Do not begin until [SCORER COMPLETE] appears above.

The Verifier reviews every evidence entry produced by the Scorer and applies the
specificity test. The Verifier does not modify verdicts, scores, or SCORER blocks.

Specificity test: ask "could this evidence apply to any well-designed output of this
type?" YES = generic = FAIL = revision required before Analyst may use this cell.

For each output, for each criterion:

  Output: [output identifier] | C-[NN]
  Scorer evidence: [copy from SCORER output above]
  Specificity: PASS -- uniquely identifies this output; no revision needed
             | FAIL -- could describe any well-designed output of this type;
                       revision required
  If FAIL:
    Revised evidence: [rewrite with a specific structural property unique to this
                       output in this scoring run]

After all outputs:
  Verification summary: [N cells reviewed; K revised; list revised cell IDs
                         or "none revised"]

[VERIFIER COMPLETE]

---

ROLE 3: ANALYST

Do not begin until [VERIFIER COMPLETE] appears above.

The Analyst uses the Scorer's verdicts and composite scores (substituting Verifier's
revised evidence where revision occurred) to produce synthesis and per-output narratives.

LEADERBOARD

Rank all outputs by composite score descending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] -- [criterion ID] -- [structural mechanism causing the
          difference; name the design property, not the criterion label]

If all outputs score identically: "No differentiating excellence signals."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

If prior-round score data is provided, identify any criterion-output pair where
a verdict degraded:

  Output: [output ID]
    C-[NN]: prior [verdict] --> now [verdict] -- [reason]

If no regressions: "No regressions detected this round."
If no prior data: "No prior round data; regression analysis not possible."

PER-OUTPUT NARRATIVE

For each scored output, write three prescribed labeled fields:

  Output [output identifier]:
  Primary differentiator:  [the one structural feature that explains why this output
                            scored differently from the field; name the design property,
                            not the criterion label; this field is required]
  Primary miss:            [the criterion or structural mechanism this output most
                            clearly failed to implement; name the gap precisely; write
                            "None -- all criteria passed" if output is all-PASS; required]
  Verdict spread:          [where this output concentrated its points and why; explain
                            the distribution pattern across essential / recommended /
                            aspirational tiers; this field is required]

[ANALYST COMPLETE]
```

---

## V-04 -- Combined axes REQ + CKL: All-field annotation + synthesis gate pair

**Variation axes**: V-03 base (named role sequence, SCORER schema with FORBIDDEN TYPES,
three-field labeled narrative) PLUS REQ axis (all mandatory fields in all phases annotated
"(required)" at the field label) PLUS CKL axis (synthesis gate pair with explicit pre-close
checklist). C-22 and C-24 are declared orthogonal in the rubric: C-22 operates on field-level
annotation within a phase's output schema; C-24 operates on phase-level gate architecture at
the synthesis boundary. Combined test confirms they can coexist without structural conflict
and without requiring the full Change-infrastructure stack.

**Hypothesis**: REQ annotates field schemas; CKL restructures the synthesis termination
boundary. The two axes do not share structural territory -- field annotation does not
constrain gate placement; gate pairs do not constrain field annotation. Combining both on the
V-03 base (which already satisfies C-21/C-23/C-12/C-20/C-19) produces a variation that
satisfies all four new R8 criteria (C-21/C-22/C-23/C-24) without the full Change-tracking
and anchor infrastructure. The remaining gap at this level bounds the aspirational ceiling
below V-05. Predicts: C-21 PASS, C-22 PASS, C-23 PASS, C-24 PASS; C-12 PASS, C-19 PASS,
C-20 PASS; C-09/C-11/C-13/C-14/C-15/C-16 FAIL (no *Why*/*Change*/baseline/anchor).

```
You are running quest-score. This run uses three sequential roles.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with a specific evidence entry,
a composite score computed from the rubric formula, and a golden-threshold
determination. The scorecard includes a ranked leaderboard, excellence signals,
failure patterns, regression signals, and per-output narrative notes.

---

ROLE 1: SCORER

SCORER CRITERION BLOCK SCHEMA

Every criterion block in SCORER output consists of exactly and only these two fields:

  Verdict:  PASS | PARTIAL | FAIL
  Evidence: [specific structural observation from this output]

PERMITTED FIELDS: Verdict and Evidence only.
FORBIDDEN FIELDS: *Why*, *Change*, *Note*, *Comment*, *Observation*, and any field
not in the permitted list. Narrative text, evaluative prose, mechanism analysis,
interpretation, synthesis language, structural commentary, and per-output summaries
are SCHEMA VIOLATIONS in SCORER blocks. A SCORER criterion block containing any
forbidden field or free text beyond Verdict and Evidence is structurally malformed.
All mechanism analysis and narrative belong exclusively in the Analyst's PER-OUTPUT
NARRATIVE section.

---

For each output:

  Output: [output identifier]

  For each criterion C-01 through C-24:

  C-[NN] -- [criterion name] ([weight: E | R | A])
  Verdict:  PASS | PARTIAL | FAIL  (required)
  Evidence: [specific quote or structural observation from this output;
             uniquely identifies this output -- not a description that could
             apply to any well-designed output of this type]  (required)

  No criterion may be skipped.  (required: no cell may be blank)
  No field beyond Verdict and Evidence may appear in a SCORER criterion block.

  After all criteria for one output:

    essential_pass    = [count of E criteria at PASS; PARTIAL = 0.5]  (required)
    recommended_pass  = [count of R criteria at PASS; PARTIAL = 0.5]  (required)
    aspirational_pass = [count of A criteria at PASS; PARTIAL = 0.5]  (required)

    composite = (essential_pass / 5 * 60)
              + (recommended_pass / 2 * 30)
              + (aspirational_pass / 17 * 170)
              = [result]  (required)

    Golden: YES -- all 5 essentials PASS; composite >= 80  (required)
         |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.

[SCORER COMPLETE]

---

ROLE 2: VERIFIER

Do not begin until [SCORER COMPLETE] appears above.

The Verifier reviews every evidence entry produced by the Scorer and applies the
specificity test. The Verifier does not modify verdicts, scores, or SCORER blocks.

VERIFIER REVIEW BLOCK SCHEMA

  Output: [output identifier] | C-[NN]  (required)
  Scorer evidence: [copy from SCORER output above]  (required)
  Specificity: PASS | FAIL  (required)

If Specificity is FAIL:
  Revised evidence: [specific structural property unique to this output]  (required)

Specificity test: ask "could this evidence apply to any well-designed output of this
type?" YES = generic = FAIL = revision required before Analyst may use this cell.

After all outputs:
  Verification summary: [N cells reviewed; K revised; IDs or "none revised"]  (required)

[VERIFIER COMPLETE]

---

ROLE 3: ANALYST

Do not begin until [VERIFIER COMPLETE] appears above.

The Analyst uses the Scorer's verdicts and composite scores (substituting Verifier's
revised evidence where revision occurred) to produce synthesis and per-output narratives.

[SYNTHESIS OPEN]

The four sections below are required. Work through the pre-close checklist before
writing [SYNTHESIS COMPLETE]. Each checkbox must be confirmed present; the closing
gate token may not appear while any checkbox is unconfirmed.

LEADERBOARD

Rank all outputs by composite score descending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] -- [criterion ID] -- [structural mechanism causing the
          difference; name the design property, not the criterion label]

If all outputs score identically on all criteria: "No differentiating excellence signals."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

If prior-round score data is provided, identify any criterion-output pair where
a verdict degraded:

  Output: [output ID]
    C-[NN]: prior [verdict] --> now [verdict] -- [reason]

If no regressions: "No regressions detected this round."
If no prior data: "No prior round data; regression analysis not possible."

PRE-CLOSE CHECKLIST -- confirm each item before writing [SYNTHESIS COMPLETE]:

  [ ] 1. LEADERBOARD: all N outputs ranked descending; ties noted; Golden shown.
  [ ] 2. EXCELLENCE SIGNALS: outlier pair named with mechanism, OR absence stated.
  [ ] 3. FAILURE PATTERNS: all-fail criteria with diagnosis, OR absence stated.
  [ ] 4. REGRESSION SIGNALS: degradations from prior data, OR no-data stated.

[SYNTHESIS COMPLETE]

PER-OUTPUT NARRATIVE

For each scored output, write three prescribed labeled fields:

  Output [output identifier]:
  Primary differentiator:  [the one structural feature that explains why this output
                            scored differently from the field; name the design property,
                            not the criterion label]  (required)
  Primary miss:            [the criterion or structural mechanism this output most
                            clearly failed to implement; name the gap precisely; write
                            "None -- all criteria passed" if output is all-PASS]  (required)
  Verdict spread:          [where this output concentrated its points and why; explain
                            the distribution across essential / recommended /
                            aspirational tiers]  (required)

[ANALYST COMPLETE]
```

---

## V-05 -- Full stack R8: all four new criteria + R7 V-05 architecture + mechanisms 8-11

**Variation axes**: R7 V-05 full-stack architecture (7 named mechanisms, 7 failure-mode
blocks, *Why* field, mandatory *Change* field, Change Manifest phase, Baseline Load gate,
synthesis gate pair, VERIFIER role, three-field labeled narrative, SCORER schema prohibition,
named role sequence with inter-role gates) PLUS all four new R8 criteria:

- REQ: all mandatory fields annotated "(required)" at label site (C-22)
- CKL: synthesis gate pair with explicit numbered pre-close checklist (C-24)
- PRB: SCORER schema FORBIDDEN TYPES list with named prohibited field types (C-23)
- Bidirectional gate inscription confirmed in all downstream roles (C-21)

PLUS Mechanisms 8-11 declared as named mechanisms with Failure Modes H-K added to the
anchor. 11 named mechanisms / 11 failure-mode blocks. Formula /17 * 170. Baseline table
extended to include C-21 through C-24.

**Hypothesis**: The four new R8 criteria (C-21, C-22, C-23, C-24) are each satisfied by
their respective mechanisms. The formula update fixes C-03. Eleven named mechanisms with
eleven failure-mode blocks satisfy C-18's per-mechanism coverage. All R7 criteria that
scored PASS in V-05 continue to score PASS; the formula change and four new mechanisms
are the only structural changes. Predicts: all C-01 through C-24 PASS; composite 260/260.

```
You are running quest-score. This run uses three sequential roles.

quest-score scores N skill outputs against a rubric. Each output receives a
per-criterion verdict (PASS | PARTIAL | FAIL) with evidence and a mechanism
explanation, a composite score computed from the rubric formula, and a golden-threshold
determination. The scorecard includes a ranked leaderboard, excellence signals,
failure patterns, and regression signals. Per-output narrative notes follow synthesis.

---

ANTI-PATTERN ANCHOR -- READ BEFORE SCORING

Eleven structural failure modes are prohibited. Read all eleven before Phase 0 begins.

FAILURE MODE A -- OMISSION PATH (prevented by Mechanism 1 below)

  Typical output:

    C-13 -- Inline regression annotation (A)
    Verdict:  PARTIAL
    Evidence: "Each criterion block contains a CHANGE slot that fires when the
               verdict differs from the prior round."
    [no *Change*: field present]

  Why this fails: The Change field is absent. A scorer whose verdict matches the
  baseline has no slot to fill and moves on. The omission is invisible -- no structural
  gap signals that a field is missing. The mandatory form closes this: writing NO CHANGE
  is required for every matching verdict; the field's absence is a structural gap, not
  a valid empty state.

FAILURE MODE B -- FRESH-LOOKUP PATH (prevented by Mechanism 2 below)

  Typical output:

    [SCORER COMPLETE -- no *Change*: fields written during scoring]

    ANALYST ROLE -- REGRESSION SIGNALS:
    Reviewing prior-round baseline to identify verdict changes...
    V-02 C-08: prior PARTIAL, now PASS
    V-02 C-13: prior PASS, now PARTIAL -- regression

  Why this fails: Regressions were identified by re-reading the baseline in ANALYST --
  a retrospective lookup after scoring finished. Any divergence not recorded inline is
  silently lost. The correct form records CHANGE at the scoring site; a Change Manifest
  phase collects all annotations before synthesis; synthesis reads only the manifest.

FAILURE MODE C -- MECHANISM-FREE SCORING (prevented by Mechanism 3 below)

  Typical output:

    C-10 -- Structural completion gate (A)
    Verdict:  PARTIAL
    Evidence: "Phase gates are present in the prompt."
    [no *Why*: field]

  Why this fails: "Phase gates are present" describes evidence, not mechanism. It names
  compliance, not architecture. The *Why*: field closes this: the scorer must name what
  the gate does architecturally -- what path it closes -- not merely confirm it exists.

FAILURE MODE D -- INCOMPLETE SYNTHESIS (prevented by Mechanism 4 below)

  Typical output:

    LEADERBOARD
    | 1 | V-05 | 200/220 | YES |
    EXCELLENCE SIGNALS
    V-05 -- C-09 -- anti-pattern anchor present.
    [output ends -- FAILURE PATTERNS and REGRESSION SIGNALS absent]

  Why this fails: FAILURE PATTERNS and REGRESSION SIGNALS are absent. No gate token
  marks synthesis as incomplete. The synthesis gate pair closes this: [SYNTHESIS COMPLETE]
  cannot be written until all required sections are confirmed via pre-close checklist.

FAILURE MODE E -- VERIFIER BYPASS PATH (prevented by Mechanism 5 below)

  Typical output:

    [SCORER COMPLETE]
    [VERIFIER COMPLETE -- skipped; evidence appeared specific]
    ANALYST: CHANGE MANIFEST ...

  Why this fails: The VERIFIER role was skipped by convention. Without a verification
  pass that explicitly applies the specificity test to each cell and requires revision
  where generic, a general instruction to "write specific evidence" in SCORER is intent,
  not enforcement. The VERIFIER role with gate closes this: ANALYST is structurally
  unreachable until [VERIFIER COMPLETE] appears after a completed review pass.

FAILURE MODE F -- THIN NARRATIVE PATH (prevented by Mechanism 6 below)

  Typical output:

    Output V-03:
    Primary differentiator: V-03 uses a three-role architecture which separates
    verdict production from synthesis.
    [Primary miss: absent]
    [Verdict spread: absent]

  Why this fails: The narrative names one structural feature but omits the primary miss
  and verdict spread. C-07 is satisfied (structural feature present) while C-19 fails
  (only one of three required fields written). The three-field labeled template closes
  this: each field's absence is structurally visible by label inspection.

FAILURE MODE G -- ROLE-SKIP PATH (prevented by Mechanism 7 below)

  Typical output:

    PHASE 1: SCORING ... [SCORING COMPLETE]
    PHASE 2: CHANGE MANIFEST ... [CHANGE MANIFEST COMPLETE]
    PHASE 3: SYNTHESIS ... [SYNTHESIS COMPLETE]
    Note: Evidence verification omitted; evidence appeared specific.

  Why this fails: The VERIFIER role was bypassed -- no named VERIFIER role, no [SCORER
  COMPLETE] inter-role gate before VERIFIER, no [VERIFIER COMPLETE] inter-role gate
  before ANALYST. Phase naming without named role sequence and inter-role gates leaves
  role-skip undetectable. The named role sequence (SCORER / VERIFIER / ANALYST) with
  [SCORER COMPLETE] and [VERIFIER COMPLETE] inter-role gates closes this.

FAILURE MODE H -- UNIDIRECTIONAL GATE PATH (prevented by Mechanism 8 below)

  Typical output:

    ROLE 2: VERIFIER
    Apply the specificity test to each evidence cell.
    [no "Do not begin until [SCORER COMPLETE]" in role definition]

    ... (SCORER output above includes [SCORER COMPLETE]) ...

  Why this fails: The [SCORER COMPLETE] gate is declared upstream but the VERIFIER role
  definition contains no entry condition. A model reading the VERIFIER role definition
  cannot confirm its entry condition without searching the transcript. Bidirectional
  inscription closes this: the downstream role carries its own entry condition at the
  role definition site; gate dependency is bidirectionally readable without transcript lookup.

FAILURE MODE I -- UNANNOTATED SCHEMA PATH (prevented by Mechanism 9 below)

  Typical output:

    SCORER CRITERION BLOCK SCHEMA

    Every criterion block consists of:
      Verdict: PASS | PARTIAL | FAIL
      Evidence: [specific structural observation]

    [No "(required)" annotations on Verdict or Evidence]

  Why this fails: The schema lists Verdict and Evidence but does not annotate them as
  required at the field label. A criterion block with a blank Verdict or Evidence is not
  syntactically distinguishable from a complete block without a separate audit. Inline
  "(required)" annotation closes this: field omission is visible at the schema site.

FAILURE MODE J -- IMPLICIT PROHIBITION PATH (prevented by Mechanism 10 below)

  Typical output:

    SCORER OUTPUT SCHEMA
    Every SCORER criterion block consists of exactly Verdict and Evidence.
    No additional fields are permitted.

  Why this fails: "No additional fields are permitted" does not name the specific
  prohibited field types. A model adding a *Why* field or narrative text can read
  this as a convention, not a named schema violation. The FORBIDDEN TYPES list closes
  this: each prohibited type is named -- *Why*, *Note*, *Comment*, narrative text,
  mechanism analysis -- and any addition is a named violation, not an ambiguous miss.

FAILURE MODE K -- UNCHECKED SYNTHESIS PATH (prevented by Mechanism 11 below)

  Typical output:

    ...
    If none: "No failure patterns in this round."
    [ANALYST COMPLETE]

  Why this fails: Synthesis closes with a single gate token. No pre-close checklist
  confirms that each required section is present. A missing section is detectable only
  by reading the full synthesis body. The synthesis gate pair with pre-close checklist
  closes this: each required section is named in a checkbox; a missing section leaves
  a checkbox blank visible without reading the body.

---

ENFORCEMENT ARCHITECTURE

Eleven structural mechanisms prevent the failure modes above. All are required.

MECHANISM 1 -- Mandatory bidirectional Change field (closes Failure Mode A)

  Every criterion block in SCORER carries a *Change*: field.
  Exactly three permissible values: NO CHANGE | CHANGE from [prior verdict]: [reason]
  | NO PRIOR DATA. The field is always required; it is not conditional. A criterion
  block without *Change*: is structurally incomplete.

MECHANISM 2 -- Change Manifest phase (closes Failure Mode B)

  After SCORER and VERIFIER complete, ANALYST begins with a Change Manifest phase
  that sweeps every *Change*: CHANGE entry into a structured table. SYNTHESIS draws
  from this manifest exclusively. SYNTHESIS is prohibited from re-reading the baseline
  table or SCORER blocks to derive regression data.

MECHANISM 3 -- Mandatory mechanism field (closes Failure Mode C)

  Every criterion block in SCORER carries a *Why*: field after Evidence. The field
  must name the structural mechanism or design property driving the verdict. A criterion
  block without *Why*: is structurally incomplete.

MECHANISM 4 -- Synthesis gate pair with pre-close checklist (closes Failure Mode D)

  SYNTHESIS in the ANALYST role is enclosed between [SYNTHESIS OPEN] and [SYNTHESIS
  COMPLETE]. All four synthesis sections are required within the gate. A numbered pre-
  close checklist confirms each section by name before [SYNTHESIS COMPLETE] may be
  written. [SYNTHESIS COMPLETE] cannot appear while any checkbox is unconfirmed.

MECHANISM 5 -- Evidence verification role (closes Failure Mode E)

  After SCORER and before ANALYST, a dedicated VERIFIER role revisits every evidence
  cell with an explicit specificity test: "could this evidence apply to any well-designed
  output of this type?" Cells that fail require a revised entry. ANALYST is structurally
  unreachable until [VERIFIER COMPLETE] appears.

MECHANISM 6 -- Three-field labeled narrative template (closes Failure Mode F)

  The ANALYST PER-OUTPUT NARRATIVE section requires exactly three labeled fields:
  Primary differentiator (required), Primary miss (required), Verdict spread (required).
  Each field carries "(required)" at the label. A section that names one field does not
  discharge the others; each absent field is visible by label inspection.

MECHANISM 7 -- Named role sequence with inter-role gates (closes Failure Mode G)

  The prompt defines a named role sequence: SCORER -> VERIFIER -> ANALYST. [SCORER
  COMPLETE] separates SCORER from VERIFIER. [VERIFIER COMPLETE] separates VERIFIER
  from ANALYST. Role-skipping is structurally detectable: a downstream gate cannot
  precede its upstream gate.

MECHANISM 8 -- Bidirectional gate inscription (closes Failure Mode H)

  Every downstream role definition contains an explicit entry condition naming the
  specific upstream gate token that must appear above:
    VERIFIER: "Do not begin until [SCORER COMPLETE] appears above."
    ANALYST:  "Do not begin until [VERIFIER COMPLETE] appears above."
  The entry condition is inscribed inside the downstream role definition. Gate
  dependencies are bidirectional: upstream role defines the gate; downstream role
  declares the entry condition. A gate declared only upstream does not satisfy this.

MECHANISM 9 -- Inline required-field annotation (closes Failure Mode I)

  Every mandatory field in every phase output schema carries "(required)" at the field
  label. SCORER fields: Verdict (required), Evidence (required), *Why* (required),
  *Change* (required). VERIFIER fields: each field annotated (required). ANALYST narrative
  fields: Primary differentiator (required), Primary miss (required), Verdict spread
  (required). The annotation appears at the field label, not in a preamble only.

MECHANISM 10 -- Named FORBIDDEN TYPES schema prohibition (closes Failure Mode J)

  The SCORER criterion block schema names the complete permitted field set AND includes
  a FORBIDDEN TYPES list: *Note*, *Comment*, *Observation*, narrative text, evaluative
  prose, mechanism analysis, interpretation, and synthesis language are each named as
  schema violations. A schema violation is named, not implied. Insertion of any forbidden
  type into a SCORER block is detectable by field-type inspection.

MECHANISM 11 -- Pre-close synthesis checklist (closes Failure Mode K)

  The synthesis gate pair ([SYNTHESIS OPEN] / [SYNTHESIS COMPLETE]) encloses a numbered
  pre-close checklist that itemizes each required synthesis section. Each checkbox must be
  confirmed present before [SYNTHESIS COMPLETE] may be written. A missing section leaves a
  checkbox blank; the blank is visible without reading the full synthesis body.

---

ROLE 1: SCORER

SCORER CRITERION BLOCK SCHEMA

Every criterion block in SCORER output consists of exactly and only these four fields:

  Verdict:  PASS | PARTIAL | FAIL
  Evidence: [specific structural observation from this output]
  *Why*:    [structural mechanism or design property behind the verdict]
  *Change*: NO CHANGE | CHANGE from [prior verdict]: [reason] | NO PRIOR DATA

PERMITTED FIELDS: Verdict, Evidence, *Why*, *Change* only.
FORBIDDEN FIELDS: *Note*, *Comment*, *Observation*, narrative text, evaluative prose,
structural commentary, mechanism analysis inserted as a fifth field, synthesis language,
per-output summaries, and any field not in the permitted list. A SCORER criterion block
containing any forbidden field or free text beyond the four permitted fields is a named
schema violation detectable by field-count inspection. Narrative and commentary belong
exclusively in the Analyst's PER-OUTPUT NARRATIVE section.

PHASE 0: BASELINE LOAD (within SCORER, before scoring begins)

If prior-round score data is provided, build a baseline table before any output is scored:

  | Output | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 |
  |--------|------|------|------|------|------|------|------|------|------|------|------|------|
  | Output | C-13 | C-14 | C-15 | C-16 | C-17 | C-18 | C-19 | C-20 | C-21 | C-22 | C-23 | C-24 |
  |--------|------|------|------|------|------|------|------|------|------|------|------|------|

If no prior data: write "No prior data; *Change*: fields will read NO PRIOR DATA."

[PRIOR ROUND LOAD COMPLETE]

PHASE 1: SCORING (within SCORER, after [PRIOR ROUND LOAD COMPLETE])

Do not begin until [PRIOR ROUND LOAD COMPLETE] appears above.

For each output, for each criterion C-01 through C-24:

  Output: [output identifier]

  C-[NN] -- [criterion name] ([weight: E | R | A])
  Verdict:  PASS | PARTIAL | FAIL  (required)
  Evidence: [specific quote or structural observation; uniquely identifies this
             output; fails if it could describe any well-designed output of this type]  (required)
  *Why*:    [name the structural mechanism or design property; do not restate the
             criterion; do not describe the evidence; name the architectural property
             that produces this verdict]  (required)
  *Change*: NO CHANGE
          | CHANGE from [prior verdict]: [one sentence -- what changed and why]
          | NO PRIOR DATA  (required)

  No criterion may be skipped.  (required: no cell may be blank)
  No Evidence, *Why*, or *Change* field may be blank.

  After all criteria for one output:

    essential_pass    = [count of E criteria at PASS; PARTIAL = 0.5]  (required)
    recommended_pass  = [count of R criteria at PASS; PARTIAL = 0.5]  (required)
    aspirational_pass = [count of A criteria at PASS; PARTIAL = 0.5]  (required)

    composite = (essential_pass / 5 * 60)
              + (recommended_pass / 2 * 30)
              + (aspirational_pass / 17 * 170)
              = [result]  (required)

    Golden: YES -- all 5 essentials PASS; composite >= 80  (required)
         |  NO  -- [which essential failed, or composite < 80]

Score all N outputs.

[SCORER COMPLETE]

---

ROLE 2: VERIFIER

Do not begin until [SCORER COMPLETE] appears above.

This is Mechanism 5 combined with Mechanism 8. The Verifier reviews every evidence entry
from SCORER and applies the specificity test before ANALYST may begin. ANALYST is
structurally unreachable until [VERIFIER COMPLETE] appears below.

Specificity test: ask "could this evidence entry apply to a different output in this
scoring run, or to any well-designed output of this type?" YES = specificity failure =
revision required before this role can close.

VERIFIER REVIEW BLOCK SCHEMA

  Output: [output identifier] | C-[NN]  (required)
  SCORER evidence: [copy from SCORER output above]  (required)
  Specificity: PASS | FAIL  (required)

If FAIL:
  Revised evidence: [rewrite with a specific structural property, verbatim quote,
                     or design decision unique to this output in this scoring run]  (required)

For every output, for every criterion, produce one review block.

After all outputs:
  Verification summary: [N cells reviewed; K revised; list revised cell IDs
                         or "none revised"]  (required)

[VERIFIER COMPLETE]

---

ROLE 3: ANALYST

Do not begin until [VERIFIER COMPLETE] appears above.

PHASE 2: CHANGE MANIFEST (within ANALYST, before synthesis)

Collect every *Change*: field reading CHANGE from [prior] from SCORER into this manifest.
Omit NO CHANGE and NO PRIOR DATA entries.

  | Output | Criterion | Prior verdict | Current verdict | Reason for change |  (required)
  |--------|-----------|---------------|-----------------|-------------------|

If no entries: "No changes detected; manifest is empty."

[CHANGE MANIFEST COMPLETE]

PHASE 3: SYNTHESIS (within ANALYST, after [CHANGE MANIFEST COMPLETE])

PROHIBITION: Do not re-read the baseline table or SCORER blocks to derive regression
information. All regression data must come from the Change Manifest above. Any regression
not recorded in SCORER via a *Change*: field is not a detectable regression in this round.

[SYNTHESIS OPEN]

The four sections below are required within this gate. Work through the pre-close
checklist before writing [SYNTHESIS COMPLETE]. Each checkbox must be confirmed present;
the closing gate token may not appear while any checkbox is unconfirmed.

LEADERBOARD

Rank all outputs by composite score descending:

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

EXCELLENCE SIGNALS

For each criterion where at least one output outperforms others:
  Signal: [output ID] -- [criterion ID] -- [structural mechanism causing the
          difference; name the design property, not the criterion label]

If all outputs score identically on all criteria:
  "No score spread found. All-pass rounds confirm stability but do not advance
   plateau detection. Redesign variations for divergence in the next round."

FAILURE PATTERNS

For each criterion where every output scores PARTIAL or FAIL:
  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]

If none: "No failure patterns in this round."

REGRESSION SIGNALS

From the Change Manifest in Phase 2 only:

  | Output | Criterion | Prior | Current | Reason |
  |--------|-----------|-------|---------|--------|

If manifest is empty: "No regressions detected this round."
If no prior data: "No prior round data; regression analysis not possible."

PRE-CLOSE CHECKLIST -- confirm each item before writing [SYNTHESIS COMPLETE]:

  [ ] 1. LEADERBOARD: all N outputs ranked by composite score descending;
         ties broken or noted; Golden status shown for each output.
  [ ] 2. EXCELLENCE SIGNALS: output-criterion outlier pair named with structural
         mechanism, OR "No score spread found" written.
  [ ] 3. FAILURE PATTERNS: all criteria with zero PASS across all outputs identified
         with diagnosis, OR "No failure patterns in this round" written.
  [ ] 4. REGRESSION SIGNALS: drawn from Change Manifest only; regressions listed
         or "No regressions" / "No prior data" written.

[SYNTHESIS COMPLETE]

PHASE 4: PER-OUTPUT NARRATIVE (within ANALYST, after [SYNTHESIS COMPLETE])

For each scored output, write three prescribed labeled fields:

  Output [output identifier]:
  Primary differentiator:  [the one structural feature that explains why this output
                            scored differently from the field; name the design property,
                            not the criterion label]  (required)
  Primary miss:            [the criterion or structural mechanism this output most
                            clearly failed to implement; name the gap precisely; write
                            "None -- all criteria passed" if output is all-PASS]  (required)
  Verdict spread:          [where this output concentrated its points and why; explain
                            the distribution pattern across essential / recommended /
                            aspirational tiers]  (required)

[ANALYST COMPLETE]
```
