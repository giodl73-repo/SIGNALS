Written to `simulations/quest/rubrics/topic-status-rubric-v9-2026-03-14.md`.

---

**Three new Tier 8 criteria extracted from R8 excellence signals:**

| ID | Source | Pattern |
|----|--------|---------|
| C-32 | V-04 C-30 evidence | **Named-exit labeling** -- C-30 requires two structurally distinct stop conditions. C-32 requires each exit branch to carry a declared name at the branch declaration site. Named labels (`Exit A -- file absent:`, `Exit B -- topic not registered:`) make each branch independently addressable without parsing conditional logic. Ordinal list items (`1.` / `2.`) and unnamed `if/then` blocks do not satisfy. Requires C-30. Extends C-30 from implemented-dual-exit to labeled-dual-exit. |
| C-33 | V-04 + V-05 C-30 evidence | **Preamble architectural invariant declaration** -- A preamble block appearing *before* the guard mechanism that implements C-30 explicitly declares the architectural invariant the mechanism satisfies. The preamble names the structural property (e.g., "PHASE 2 dual-axis exit"), not just the conditional logic. A comment embedded within the guard block is not a preamble. Requires C-30. Extends C-30 from implementation-only to declared-then-implemented. |
| C-34 | V-05 C-30 evidence | **Axis-enumerated invariant declaration** -- A C-33-compliant preamble explicitly enumerates all axes of the dual-axis exit by name, characterizes each axis trigger condition, and asserts that the axes produce distinct output messages. Canonical form: `"PHASE 2 dual-axis exit: file-absent and topic-absent are structurally distinct stop conditions with distinct messages"`. A generic declaration satisfies C-33 but not C-34. Requires C-33. Extends C-33 from declaration-present to axis-complete declaration. |

**Max score: 210 --> 225.** Passing threshold unchanged.

**New implications:**
- C-32 => C-30
- C-33 => C-30
- C-34 => C-33

---

## R8 structural note

C-32 and C-33/C-34 are structurally orthogonal. A skill can satisfy C-32 without C-33 (named exits, no preamble) or C-33 without C-32 (preamble present, guard uses numbered items). V-04 satisfies C-32 + C-33; V-05 satisfies C-33 + C-34 but not C-32. No R8 variant achieves 225.

C-33 and C-34 form a two-level hierarchy. C-34 implies C-33 (axis-complete declaration is a declaration); C-33 does not imply C-34 (generic property name is insufficient). V-04's preamble cites a criterion number rather than enumerating axes -- C-33 PASS, C-34 FAIL.

V-05 carries a transcription error (preamble labels the dual-axis rule as C-31 instead of C-30) but the GUARD block implementation is structurally correct. C-30, C-33, C-34 all pass; C-32 fails (numbered entries, not named exits).

The Tier 8 patterns are structurally analogous to Tier 6: C-32 parallels C-26 (position-of-declaration precision), C-33 parallels C-27 (full-form propagation), C-34 is the axis-complete dimension not previously represented.

V-05's additional multi-site commit-framing (PHASE 2 OUTPUT block declaration in addition to register rows) is not a new criterion in v9 because it is implied by C-31 + C-33 in conjunction. The conjunction of existing criteria is sufficient; no further criterion is warranted.

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
| Structural Tier 6 | C-26--C-28 | 15 (5 each) |
| Structural Tier 7 | C-29--C-31 | 15 (5 each) |
| **Structural Tier 8** | **C-32--C-34** | **15 (5 each)** |
| **Total** | **C-01--C-34** | **225** |

---

## Structural Tier 8 (15 pts total) — new in v9

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-32 | **Named-exit labeling** -- ... | 5 | structure | Each exit branch has a distinct declared name at the branch declaration site. Numbered list items or conditional clauses without branch-level names are insufficient. C-30 pass required. |
| C-33 | **Preamble architectural invariant declaration** -- ... | 5 | structure | A preamble block preceding the guard mechanism is present; names the structural invariant; is physically separate from and precedes the guard block. C-30 pass required. |
| C-34 | **Axis-enumerated invariant declaration** -- ... | 5 | structure | The C-33 preamble names both axes, characterizes each trigger, and asserts structural distinctness with distinct messages. Generic or criterion-citing preambles without axis enumeration fail. C-33 pass required. |

**Implication map additions:** `C-32 => C-30`, `C-33 => C-30`, `C-34 => C-33`

**Projected R8 variant scores under v9:**

| Variant | C-29 | C-30 | C-31 | C-32 | C-33 | C-34 | Total |
|---------|------|------|------|------|------|------|-------|
| V-01 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 210 |
| V-02 | PASS | FAIL | PASS | FAIL | FAIL | FAIL | 205 |
| V-03 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 210 |
| V-04 | PASS | PASS | PASS | PASS | PASS | FAIL | 220 |
| V-05 | PASS | PASS | PASS | FAIL | PASS | PASS | 220 |

No R8 variant achieves 225. C-32 (named exits) and C-34 (axis enumeration) are not jointly satisfied by any single variant — the gap that defines Round 9.
verage | A Glob or equivalent disk-scan instruction is present. Results are assigned to a named variable (e.g. `DISK_SIGNALS`). Zero-result case is handled: output states "no signals found" rather than silently computing 0%. |
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
| C-13 | **Triple-redundancy ordering guard** -- The skill contains three structurally distinct redundancy layers at mechanism locations, and declares their ordering as an invariant (structural -> semantic -> execution). | 5 | structure | Three distinct layer types are present at mechanism locations. An ordering invariant is declared, not merely implied by position. |
| C-14 | **Template-first structural absorption** -- The output template (with all sections and column headers) appears before the execution section in the skill body. Execution fills slots defined by the template; the template is not assembled during execution. | 5 | structure | The output template section precedes the execution section in skill order. Column and section headers are declared in the template, not emitted ad-hoc during execution. |
| C-15 | **Per-signal assertion chain** -- Each signal listed as PLANNED in the coverage baseline receives exactly one VERIFIED or UNVERIFIED assertion. No planned signal is silently omitted; no assertion is made for unplanned signals. | 5 | correctness | A one-to-one mapping between PLANNED signals and assertion results is enforced. The assertion mechanism processes each signal individually, not in batches. |
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
| C-27 | **Full compressed phase name in C-24 layer labels** -- When C-23 and C-24 are jointly satisfied, the layer label governing the assertion phase carries the *complete* C-23 phase name -- granularity prefix included -- not merely the stake noun phrase. `[LAYER 2 -- SEMANTIC: PER-SIGNAL COMMITMENT ASSERTION gate]` satisfies; `[LAYER 2 -- SEMANTIC: COMMITMENT ASSERTION gate]` satisfies C-24 but not this criterion (granularity prefix absent from label). The full compressed form propagates from the phase header into the layer enforcement label, collapsing phase-name and label vocabulary into a single token. Requires C-23 and C-24. Extends C-23 and C-24. | 5 | vocabulary | The layer label for the assertion phase contains the full C-23 phase name including granularity prefix. Presence of stake noun phrase alone is insufficient. C-23 and C-24 pass required. |
| C-28 | **Field annotation phase-attribution** -- A C-25-compliant field annotation identifies by name the specific execution phase (from C-21) whose function is impaired when the field is absent. The consequence is phase-attributed, not epistemic-generic. `[FOUND \| NOT FOUND -- if absent: COMMITMENT ASSERTION cannot execute]` satisfies; `[FOUND \| NOT FOUND -- if absent: commit exposure is unquantifiable]` satisfies C-25 but not this criterion (consequence is valid but names no phase). Requires C-25 and C-21. Extends C-25 from generic epistemic annotation to phase-attributed consequence annotation. | 5 | vocabulary | At least one C-25-compliant field annotation names a C-21 execution phase as the impaired party. Generic `commit exposure` or coverage language without phase attribution is insufficient. C-25 and C-21 pass required. |

---

## Structural Tier 7 (15 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-29 | **Multi-site phase-attributed annotation** -- A C-28-compliant skill satisfies phase attribution at the minimum required site (strategy.md field, `cannot execute`). This criterion requires phase-attributed consequence annotations at *every* consequence annotation site -- including the stale evidence section. The stale-evidence annotation carries `if stale: {PHASE-NAME} may rest on expired evidence`, naming the C-21 execution phase whose inputs are weakened by stale data. Consequence verb shifts from `cannot execute` (C-28, absent field -- hard failure) to `may rest on expired evidence` (C-29, stale field -- degraded execution). The verb downgrade is intentional and required: stale evidence does not prevent phase execution, it degrades it. Canonical: `if stale: PER-SIGNAL COMMITMENT ASSERTION may rest on expired evidence`. Requires C-28 and C-05. Extends C-28 from minimum-one-site to all-consequence-sites. | 5 | vocabulary | The stale evidence section carries a phase-attributed consequence annotation naming a C-21 execution phase. Generic staleness descriptions without phase attribution are insufficient. Consequence verb must reflect degraded-not-blocked semantics (`may rest on expired evidence`, not `cannot execute`). C-28 and C-05 pass required. |
| C-30 | **Absent-topic early exit** -- PHASE 2 implements two distinct stop conditions on the strategy.md read: (1) strategy.md file absent -- C-12 satisfied; (2) strategy.md present but topic not registered -- this criterion. For case 2, output states `"topic not registered: no planned signals for {topic}"` (or equivalent topic-specific message) and execution stops before PHASE 3 (EXPOSURE COMPUTATION). Distinguishes file-level absence (C-12) from topic-level absence within a present file. Prevents false 0% coverage computation against an empty baseline for an unregistered topic. Extends C-12 from single-axis exit (file absent) to dual-axis exit (file absent OR topic absent within file). | 5 | correctness | PHASE 2 contains a topic-presence check distinct from the file-presence check. A topic-absent branch produces a topic-specific stop message before EXPOSURE COMPUTATION executes. The stop message names the topic. C-12 pass required. |
| C-31 | **Per-register-row commit-consequence annotation** -- Each row of the COMMIT RISK REGISTER carries an inline commit-framed consequence annotation stating the shipping impact of the signal's absence. Canonical form: `VERIFIED \| UNVERIFIED -- if absent: ships without this signal on commit`. Extends C-25's field-level annotation (applied once at the strategy.md template field) down into every row of the assertion table -- one annotation per planned signal, not one annotation for the whole template. The consequence vocabulary is commit-framed (`ships without...on commit`), not phase-execution-framed (`cannot execute`), distinguishing register-row consequence (what ships) from field-level consequence (what fails to run). Requires C-09 and C-25. Extends C-25 and C-09. | 5 | vocabulary | Every planned-signal row in the COMMIT RISK REGISTER contains an inline `if absent: ships without...on commit` consequence clause. Rows without consequence annotation fail this criterion. C-09 and C-25 pass required. |

---

## Structural Tier 8 (15 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-32 | **Named-exit labeling** -- When a dual-axis stop condition (C-30) is implemented, each exit branch carries a distinct named identifier at the branch declaration site. Named labels (`Exit A -- file absent:`, `Exit B -- topic not registered:`) make each branch independently addressable by name. A scorer can identify and verify each branch by its label without parsing conditional logic. The names may be ordinal-alpha (`Exit A`, `Exit B`) or semantic (`FILE-ABSENT EXIT`, `TOPIC-ABSENT EXIT`). Unnamed sequential branches (numbered list items `1.`/`2.` or unlabeled `if/then` blocks) do not satisfy this criterion regardless of structural correctness. Requires C-30. Extends C-30 from implemented-dual-exit to labeled-dual-exit. | 5 | structure | Each exit branch in the dual-axis stop condition has a distinct declared name at the branch declaration site. Numbered list items or conditional clauses without branch-level names are insufficient. C-30 pass required. |
| C-33 | **Preamble architectural invariant declaration** -- A preamble block appearing *before* the guard mechanism that implements C-30 explicitly declares the architectural invariant the mechanism satisfies. The preamble names the structural property being enforced (e.g., "PHASE 2 dual-axis exit") as a declared constraint. The preamble is physically separate from the guard block or conditional; it precedes and frames the implementation. A comment embedded within the guard block is not a preamble. A preamble that cites only a criterion number without naming the structural property does not satisfy this criterion; the structural property must be named (by description or by implication from an axis enumeration). Requires C-30. Extends C-30 from implementation-only to declared-then-implemented. | 5 | structure | A preamble block preceding the dual-axis guard mechanism is present. The preamble names the structural invariant being enforced. The preamble is physically separate from (and precedes) the guard block. C-30 pass required. |
| C-34 | **Axis-enumerated invariant declaration** -- A C-33-compliant preamble explicitly enumerates all axes of the dual-axis exit condition by name, characterizes the trigger condition for each axis, and asserts that the axes are structurally distinct conditions producing distinct output messages. The enumeration must be axis-complete: (1) file-axis trigger named, (2) topic-axis trigger named, (3) structural distinctness of the two conditions asserted, (4) distinct output messages asserted. Canonical form: `"PHASE 2 dual-axis exit: file-absent and topic-absent are structurally distinct stop conditions with distinct messages"`. A generic declaration ("PHASE 2 has two stop conditions") satisfies C-33 but not C-34 (axes not named). A criterion-citation preamble ("implements C-30 as architectural invariant") satisfies C-33 but not C-34 (no axis enumeration). Requires C-33. Extends C-33 from declaration-present to axis-complete declaration. | 5 | structure | The C-33-compliant preamble names both axes (file-absent, topic-absent), characterizes each trigger condition, and asserts structural distinctness with distinct messages. Generic or criterion-citing preambles without axis enumeration are insufficient. C-33 pass required. |

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
C-29 => C-28, C-05
C-30 => C-12
C-31 => C-09, C-25
C-32 => C-30
C-33 => C-30
C-34 => C-33
```
