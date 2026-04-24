Reading the R6 scorecard carefully before writing the updated rubric.

The differentiating evidence from R6 is concentrated in Tier 5:

- **C-23**: V-02 passes (`PER-SIGNAL COMMITMENT ASSERTION`), V-01/V-03/V-04 fail (`COMMITMENT ASSERTION (per signal -- ...)`)
- The failure analysis is specific: the granularity qualifier in failing variants is a *parenthetical annotation*, not an integral left-edge prefix

Three extractable patterns:

1. **Prefix left-edge position** — V-02's granularity term is the leftmost token, establishing scope *before* stake. Other variants have the vocabulary present but as trailing decoration. This is a positional property not captured by C-23 (which requires both terms present, but not their order).

2. **C-23 phrase propagates into C-24 layer labels** — When C-23 is satisfied with a full compressed name (`PER-SIGNAL COMMITMENT ASSERTION`), a C-24-compliant label should carry the *full* compressed form, not just the stake noun phrase. A variant that passes C-23 but whose layer label drops the granularity prefix satisfies C-24 incompletely.

3. **Field annotation phase-attribution** — C-25 requires inline consequence annotation. The natural extension: the annotation names the *specific execution phase* (from C-21) that is impaired by the field's absence, rather than a generic epistemic consequence. This tightens C-25 from section-level consequence to phase-attributed consequence.

---

```markdown
# Rubric: `topic:status` — v7
**Updated:** 2026-03-14
**Max Score:** 195
**Passing Threshold:** All essential criteria pass + score >= 80

---

## Change History

| Version | Max | Notes |
|---------|-----|-------|
| v1 | 90 | Initial: essential + recommended |
| v2 | 115 | Added aspirational C-08--C-12 |
| v3 | 135 | Added aspirational-2 C-13--C-16 |
| v4 | 150 | Added aspirational-3 C-17--C-19 from R3 excellence |
| v5 | 165 | Added aspirational-4 C-20--C-22 from R4 excellence signals |
| v6 | 180 | Added aspirational-5 C-23--C-25 from R5 excellence signals |
| v7 | 195 | Added structural tier 6 C-26--C-28 from R6 excellence signals |

---

## v6 -> v7 Changes

Three new structural tier 6 criteria (15 pts):

| ID | Origin | Pattern |
|----|--------|---------|
| C-26 | V-02 R6 (C-23 positional analysis) | **Granularity-prefix left-edge declaration** — In a C-23-compliant phase name, the evaluation-granularity term occupies the leftmost position, establishing quantifier scope before the decision-stake noun phrase. `PER-SIGNAL COMMITMENT ASSERTION` satisfies (prefix precedes stake); a hypothetical `COMMITMENT PER-SIGNAL ASSERTION` would contain both required terms (satisfying C-23) but fail left-edge position (stake precedes scope). Left-edge position makes scope the first token encountered in name-scanning order, not a later modifier. Extends C-23. |
| C-27 | V-02 R6 (C-23 + C-24 interaction) | **Full compressed phase name in C-24 layer labels** — When C-23 and C-24 are jointly satisfied, the layer label governing the assertion phase carries the *complete* C-23 phase name — granularity prefix included — not merely the stake noun phrase. `[LAYER 2 -- SEMANTIC: PER-SIGNAL COMMITMENT ASSERTION gate]` satisfies; `[LAYER 2 -- SEMANTIC: COMMITMENT ASSERTION gate]` satisfies C-24 but not this criterion (stake phrase present, granularity prefix absent from label). The compressed C-23 form propagates into the C-24 enforcement label, collapsing phase-name and layer-label vocabulary into one token. Requires C-23 ∧ C-24. Extends C-23 and C-24. |
| C-28 | V-02 R6 (C-25 + C-21 interaction) | **Field annotation phase-attribution** — A C-25-compliant field annotation identifies by name the specific execution phase (from C-21) whose function is impaired when the field is absent. The consequence is phase-attributed, not epistemic-generic. `[FOUND | NOT FOUND -- if absent: COMMITMENT ASSERTION cannot execute]` satisfies; `[FOUND | NOT FOUND -- if absent: commit exposure is unquantifiable]` satisfies C-25 but not this criterion — the consequence is valid but names no phase. Requires C-25 ∧ C-21. Extends C-25 from epistemic annotation to phase-attributed annotation. |

**Max score:** 180 → **195**. Passing threshold unchanged.

**New implications:**
- C-26 => C-23
- C-27 => C-23, C-27 => C-24
- C-28 => C-25, C-28 => C-21

---

## R6 structural note

C-26 and C-27 are architecturally chained: C-26 establishes that the granularity prefix is left-edge in the phase name; C-27 establishes that this full form (including the left-edge prefix) propagates into layer labels. A skill can satisfy C-27 without C-26 only if the layer label carries the full C-23 name but the phase name itself did not put the prefix at left-edge — a structurally incoherent state. In practice, C-26 ∧ C-24 implies C-27 when the implementation is self-consistent.

C-28 is independent of C-26 and C-27. It applies along the C-25 → C-22 → C-07 chain and has no entailment relationship with the prefix-position chain (C-23 → C-26 → C-27).

The R6 failure mode for C-23 — granularity qualifier as parenthetical annotation — does not generate C-26 directly. C-26 captures the finer property (left-edge vs. any-position) that the R6 pass/fail evidence implies but that C-23 does not require.

---

## Score Distribution

| Section | Criteria | Points |
|---------|----------|--------|
| Essential | C-01--C-04 | 60 (15 each) |
| Recommended | C-05--C-07 | 30 (10 each) |
| Aspirational | C-08--C-12 | 25 (5 each) |
| Structural Tier 2 | C-13--C-16 | 20 (5 each) |
| Structural Tier 3 | C-17--C-19 | 15 (5 each) |
| Structural Tier 4 | C-20--C-22 | 15 (5 each) |
| Structural Tier 5 | C-23--C-25 | 15 (5 each) |
| **Structural Tier 6** | **C-26--C-28** | **15 (5 each)** |
| **Total** | **C-01--C-28** | **195** |

---

## Essential Criteria (60 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-01 | **Signal discovery** -- The skill scans the `simulations/` directory for existing signal files matching the topic, using a Glob pattern. The scan is explicit and disk-based, not inferred from memory. | 15 | coverage | A Glob or equivalent disk-scan instruction is present. Results are assigned to a named variable (e.g. `DISK_SIGNALS`). Zero-result case is handled: output states "no signals found" rather than silently computing 0%. |
| C-02 | **Coverage percentage** -- Output reports a numeric coverage percentage derived from signals found on disk versus signals planned in `strategy.md`. The percentage is mathematically consistent with the gap list. | 15 | coverage | A percentage formula is present (`found / planned * 100` or equivalent). A consistency check guards against the contradiction failure mode: if the gap list is non-empty and percentage equals 100%, execution halts and recomputes. |
| C-03 | **Gap identification** -- Signals planned in `strategy.md` but not yet present on disk are listed as open gaps. | 15 | coverage | At least one gap section exists. If all planned signals are present, output explicitly states "no gaps". Gaps are named (namespace + signal type), not just counted. |
| C-04 | **Display-only behavior** -- The skill writes nothing to disk. No file is created or modified. | 15 | behavior | After execution, `git status` shows no new or modified files. Output is terminal-only. |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-05 | **Readiness verdict** -- Output provides a clear readiness signal for the stated target outcome (e.g. "NOT READY -- 3 essential gaps remain", "READY -- all scout + draft signals present"). | 10 | depth | A readiness label or verdict is present and connected to the gap list. Not just a coverage number -- a qualitative judgment. |
| C-06 | **Namespace breakdown** -- Coverage is shown per namespace (scout, draft, review, flow, trace, prove, listen, program, topic), not only as a single aggregate. | 10 | format | At least namespace-level grouping visible in output. Namespaces with zero signals are shown as empty, not omitted. |
| C-07 | **Strategy cross-reference** -- Output names the `strategy.md` file used as the planned-signal baseline and notes if `strategy.md` is missing or has no planned signals for this topic. | 10 | correctness | `strategy.md` reference appears in output. If missing, output says so explicitly rather than silently computing against zero. |

---

## Aspirational Criteria (25 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-08 | **Recency awareness** -- Output identifies the most recently modified signal file and flags any signals not modified within the last N days as potentially stale. | 5 | depth | A STALE EVIDENCE section or equivalent is present. Signal file dates are surfaced, not just counts. |
| C-09 | **Actionable next step** -- Output names the single highest-priority gap and the specific skill invocation that would close it. | 5 | depth | A HIGHEST PRIORITY RISK section or equivalent is present. It contains a concrete skill invocation (e.g. `/scout:feasibility {topic}`), not a generic recommendation. |
| C-10 | **Structural namespace completeness** -- The namespace breakdown table contains a row for all nine namespaces. Namespaces with zero planned or zero found signals are shown with explicit zeros, not omitted. | 5 | format | All nine namespaces present in the table. Zero rows display `0 \| 0 \| --` rather than being suppressed. |
| C-11 | **Phase-gated execution** -- The skill defines named execution phases and includes a DISPLAY GATE phase that performs a pre-display check before producing output. | 5 | structure | Named phases are declared in the skill. A DISPLAY GATE phase or equivalent explicitly gates display on a pre-condition check. |
| C-12 | **Gap-first output ordering** -- The output template places the risk register (gap list) before the aggregate summary. Gaps are seen before the rolled-up percentage. | 5 | format | The COMMIT RISK REGISTER or equivalent gap artifact appears before the EXPOSURE SUMMARY or equivalent aggregate. The template ordering is fixed, not conditional. |

---

## Structural Tier 2 (20 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-13 | **Triple-redundancy ordering guard** -- The skill contains three structurally distinct redundancy layers at mechanism locations, and declares their ordering as an invariant (structural → semantic → execution). | 5 | structure | Three distinct layer types are present at mechanism locations. An ordering invariant is declared, not merely implied by position. |
| C-14 | **Template-first structural absorption** -- The output template (with all sections and column headers) appears before the execution section in the skill body. Execution fills slots defined by the template; the template is not assembled during execution. | 5 | structure | The output template section precedes the execution section in skill order. Column and section headers are declared in the template, not emitted ad-hoc during execution. |
| C-15 | **Per-signal assertion chain** -- Each signal listed as PLANNED in the coverage baseline receives exactly one VERIFIED or UNVERIFIED assertion. No planned signal is silently omitted; no assertion is made for unplanned signals. | 5 | correctness | A one-to-one mapping between PLANNED signals and assertion results is enforced. The assertion mechanism processes each P individually, not in batches. |
| C-16 | **Consequence-framed readiness verdict** -- The readiness verdict is stated as a shipping consequence, not a coverage label. "Committing now means shipping without: {list}" rather than "Coverage: 60%." | 5 | depth | A consequence-framed verdict is present. The verdict names specific missing items in the context of a commit or ship action, not just a percentage. |

---

## Structural Tier 3 (15 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-17 | **Labeled redundancy layers** -- Each of the three redundancy layers (structural, semantic, execution) carries an explicit label at the location in the skill where it operates: `[LAYER 1 -- STRUCTURAL]`, `[LAYER 2 -- SEMANTIC]`, `[LAYER 3 -- EXECUTION]`. | 5 | structure | All three layer labels are present at their mechanism locations in the skill body. Labels are not in comments or headers only -- they appear at the point of the mechanism. |
| C-18 | **Assertion table pre-seeded in template** -- The COMMIT RISK REGISTER (or equivalent assertion table) with VERIFIED and UNVERIFIED column headers is defined in the output template section, not constructed during execution. The table structure is part of the pre-execution template. | 5 | structure | The assertion table with column headers appears in the output template section. The execution section fills rows into a pre-existing table structure. |
| C-19 | **Consequence vocabulary saturation** -- All output section headers use consequence vocabulary (COMMIT RISK REGISTER, COMMIT RISKS, EXPOSURE SUMMARY, COMMIT DECISION, HIGHEST PRIORITY RISK). No section header uses neutral or descriptive vocabulary (Coverage Summary, Gap List, Status). | 5 | vocabulary | Every top-level output section header uses a word from the consequence domain (COMMIT, EXPOSURE, RISK). Neutral section titles are absent. |

---

## Structural Tier 4 (15 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-20 | **Assertion table as primary gap display artifact** -- The COMMIT RISK REGISTER is labeled as the primary gap artifact and is structurally designated as the first output section, preceding the EXPOSURE SUMMARY. Its label explicitly states its role: `[LAYER 1 -- STRUCTURAL: primary gap artifact; first section; precedes EXPOSURE SUMMARY]`. | 5 | structure | The COMMIT RISK REGISTER label contains both `primary gap artifact` and `precedes EXPOSURE SUMMARY` (or equivalent). It is the first output section. |
| C-21 | **Execution phase names in consequence vocabulary** -- All execution phases are named using consequence vocabulary drawn from the commit/exposure domain. Canonical example: SIGNAL ACQUISITION, COMMITMENT ASSERTION, EXPOSURE COMPUTATION, DISPLAY GATE. No phase is named with neutral or ordinal vocabulary (Phase 1, Step 2, Data Collection). | 5 | vocabulary | All execution phase names use consequence-domain vocabulary. Ordinal or neutral phase names are absent. |
| C-22 | **Missing baseline as epistemic consequence** -- When `strategy.md` is absent or contains no planned signals for the topic, the output does not silently compute against zero. It explicitly states that the epistemic consequence of the missing baseline is that commit exposure cannot be quantified: "No planned baseline -- commit exposure is unquantifiable." | 5 | correctness | The missing-baseline branch produces an explicit epistemic-consequence statement, not a zero-coverage result or a silent skip. |

---

## Structural Tier 5 (15 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-23 | **Phase name as compressed criterion statement** -- The assertion phase name encodes both the evaluation granularity (per-signal, not batch) and the decision stake (commitment), compressing the C-15 per-signal requirement into the execution architecture label. The phase name is a structural specification, not a description. Canonical example: `PER-SIGNAL COMMITMENT ASSERTION`. Extends C-21. | 5 | vocabulary | The assertion phase name contains both an evaluation-granularity term and a decision-stake term. The terms are in the phase name itself, not in a parenthetical annotation. C-21 pass required. |
| C-24 | **Cross-layer vocabulary coherence** -- Structural enforcement labels use the same vocabulary as the active phase names they govern. When C-21 is satisfied, `[LAYER 3]` reads `DISPLAY GATE render order:` not `Phase 4 render order:`. Consequence-phase vocabulary flows into structural enforcement mechanism labels, collapsing two parallel vocabulary systems into one. Extends C-17 and C-21. | 5 | vocabulary | Each `[LAYER N]` label at an enforcement location uses vocabulary from the phase name it governs, not ordinal or neutral vocabulary. C-17 and C-21 pass required. |
| C-25 | **Template field inline consequence annotation** -- Template fields contain their epistemic consequence inline within the field format string itself, making each field self-documenting about decision impact. Canonical example: `[FOUND \| NOT FOUND -- if absent: commit exposure is unquantifiable]`. The annotation is structurally inseparable from the field. Extends C-22 from section-level to field-level consequence. | 5 | vocabulary | At least one template field contains an inline `if absent:` consequence clause. The clause is in the field format string, not in a separate note. The consequence uses commit-domain vocabulary. |

---

## Structural Tier 6 (15 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-26 | **Granularity-prefix left-edge declaration** -- In a C-23-compliant phase name, the evaluation-granularity term occupies the leftmost position, establishing quantifier scope before the decision-stake noun phrase. `PER-SIGNAL COMMITMENT ASSERTION` satisfies (granularity prefix precedes stake); a hypothetical `COMMITMENT PER-SIGNAL ASSERTION` would contain both required terms (passing C-23) but fail this criterion (stake precedes scope). Left-edge position makes scope the first token in name-scanning order, not a later modifier or infix qualifier. Extends C-23. | 5 | vocabulary | The granularity term is the leftmost token in the assertion phase name. Stake noun phrase follows granularity prefix. C-23 pass required. |
| C-27 | **Full compressed phase name in C-24 layer labels** -- When C-23 and C-24 are jointly satisfied, the layer label governing the assertion phase carries the *complete* C-23 phase name -- granularity prefix included -- not merely the stake noun phrase. `[LAYER 2 -- SEMANTIC: PER-SIGNAL COMMITMENT ASSERTION gate]` satisfies; `[LAYER 2 -- SEMANTIC: COMMITMENT ASSERTION gate]` satisfies C-24 but not this criterion (granularity prefix absent from label). The full compressed form propagates from the phase header into the layer enforcement label, collapsing phase-name and label vocabulary into a single token. Requires C-23 ∧ C-24. Extends C-23 and C-24. | 5 | vocabulary | The layer label for the assertion phase contains the full C-23 phase name including granularity prefix. Presence of stake noun phrase alone is insufficient. C-23 and C-24 pass required. |
| C-28 | **Field annotation phase-attribution** -- A C-25-compliant field annotation identifies by name the specific execution phase (from C-21) whose function is impaired when the field is absent. The consequence is phase-attributed, not epistemic-generic. `[FOUND \| NOT FOUND -- if absent: COMMITMENT ASSERTION cannot execute]` satisfies; `[FOUND \| NOT FOUND -- if absent: commit exposure is unquantifiable]` satisfies C-25 but not this criterion (consequence is valid but names no phase). Requires C-25 ∧ C-21. Extends C-25 from generic epistemic annotation to phase-attributed consequence annotation. | 5 | vocabulary | At least one C-25-compliant field annotation names a C-21 execution phase as the impaired party. Generic `commit exposure` or coverage language without phase attribution is insufficient. C-25 and C-21 pass required. |

---

## Implication Map

```
C-02 => C-01
C-03 => C-01
C-05 => C-03
C-09 => C-05
C-13 => C-11
C-14 => C-11
C-15 => C-11
C-16 => C-05
C-17 => C-13
C-18 => C-14, C-17
C-19 => C-16
C-20 => C-18, C-12
C-21 => C-11, C-19
C-22 => C-07
C-23 => C-21
C-24 => C-17, C-21
C-25 => C-22
C-26 => C-23
C-27 => C-23, C-24
C-28 => C-25, C-21
```
```
