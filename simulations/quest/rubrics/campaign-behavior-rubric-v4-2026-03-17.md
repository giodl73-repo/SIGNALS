Now I have all five variations in full. Let me identify the genuinely new patterns from Round 3 not yet captured by C-01 through C-14.

**New patterns observed:**

1. **V-01, V-04**: Explicit `EXIT CRITERIA:` gate per phase — not the same as C-14 (which is post-execution calibration). This is a phase-completion gate requiring affirmative clean-state declarations.

2. **V-02**: `CONFIRMED?` distinction — runtime findings cross-referenced against contract topology findings, creating a stronger/weaker evidence tier. Structurally distinct from C-09 (systemic) and C-14 (calibration).

3. **V-03**: Interrogative calibration register — Q1–Q5 questions as the calibration mechanism rather than a named phase block. Achieves perfect score through a different architectural form than C-14's phase-based pattern.

4. **V-01, V-04, V-05**: Pre-execution topology census (Phase 0) — *pre*-execution component cataloging vs. C-14's *post*-execution re-grounding. V-02's C-11 failure traces directly to its absence.

These four are structurally independent of each other and of existing criteria. Here is the complete v4 rubric:

---

```markdown
# Quest Rubric — campaign-behavior (org-review)
**Version:** v4
**Updated:** 2026-03-17
**Author:** Quest Engine

---

## Scoring Formula

| Tier        | Criteria                        | Max pts |
|-------------|---------------------------------|---------|
| Essential   | C-01–C-05 (10 pts each)         | 50      |
| Recommended | C-06–C-08 (10 pts each)         | 30      |
| Aspirational | C-09–C-18 — (passed/10) × 10   | 10      |
| **Total**   |                                 | **90**  |

PASS = full credit. PARTIAL = half credit. FAIL = 0.
Aspirational tier is binary PASS/FAIL per criterion; score = (count passed / 10) × 10,
rounded to nearest integer.

---

## Essential Criteria (50 pts total)

### C-01 — All 5 sub-skills executed
- **Weight:** essential
- **Category:** coverage
- **Text:** The campaign runs all five sub-skills: trace-contract, trace-state,
  trace-permissions, flow-lifecycle, and flow-trigger. Partial execution invalidates
  blast radius ranking because findings from skipped sub-skills are absent.
- **Pass condition:** All five sub-skills are named in the output with evidence of
  execution (findings, tables, or explicit "none found" statements). Fewer than five
  named = FAIL.

---

### C-02 — Findings ranked by blast radius
- **Weight:** essential
- **Category:** correctness
- **Text:** The consolidated report presents findings ordered by blast radius
  (highest impact / widest system effect first). Blast radius is not interchangeable
  with severity or priority — it specifically captures how broadly a failure propagates
  across the system.
- **Pass condition:** Output includes a ranked findings list where ranking criterion is
  explicitly stated as blast radius (or equivalent: propagation scope, system-wide
  impact). Random order or severity-only ranking = FAIL.

---

### C-03 — Spec gaps identified or explicitly cleared
- **Weight:** essential
- **Category:** coverage
- **Text:** The report either names at least one spec gap found during the campaign, or
  explicitly states that no spec gaps were detected. A spec gap is a condition, state
  transition, or contract term that the spec does not address but the simulation exposes.
- **Pass condition:** Output contains a labeled "spec gaps" section (or equivalent
  heading) with findings or a clear "none found" statement. Omitting the section
  entirely = FAIL.

---

### C-04 — Contract violations surfaced or explicitly cleared
- **Weight:** essential
- **Category:** coverage
- **Text:** The report either names at least one contract violation (expected vs actual
  mismatch between components) or explicitly states that no violations were found.
  Contract violations come primarily from trace-contract but may surface in any
  sub-skill.
- **Pass condition:** Output contains a labeled "contract violations" section (or
  equivalent) with findings or a clear "none found" statement. Omitting the section
  = FAIL.

---

### C-05 — Single consolidated report
- **Weight:** essential
- **Category:** structure
- **Text:** The campaign produces one synthesized report, not five concatenated sub-skill
  outputs. The consolidation integrates findings from all sub-skills into a unified
  narrative with a single ranked findings list and a single verdict.
- **Pass condition:** Output has one CONSOLIDATE section (or equivalent) containing the
  ranked list and verdict. Five separate sub-skill outputs presented sequentially without
  synthesis = FAIL.

---

## Recommended Criteria (30 pts total)

### C-06 — Source attribution per finding
- **Weight:** recommended
- **Category:** traceability
- **Text:** Each finding in the consolidated report identifies which sub-skill surfaced it.
  Attribution enables readers to trace a finding back to its simulation method and
  evaluate its credibility accordingly.
- **Pass condition:** Every finding entry includes a labeled source field (e.g.,
  "Sub-skill source: trace-contract" or "Source: [phase]"). Findings without source
  attribution = FAIL.

---

### C-07 — Remediation hint per finding
- **Weight:** recommended
- **Category:** actionability
- **Text:** Each finding includes a direction for what must change to resolve it — a
  concrete fix direction, not a restatement of the problem. The hint is a single clear
  action, not a list.
- **Pass condition:** Every finding has a labeled "What must change" or "Fix direction"
  field with actionable content. Vague restatements ("fix this") or absent hints = FAIL.

---

### C-08 — Severity explicit per finding
- **Weight:** recommended
- **Category:** completeness
- **Text:** Each finding in the consolidated report explicitly states the severity at
  the epicenter (high / med / low). Severity is distinct from blast radius and must
  appear as a separate labeled field.
- **Pass condition:** Every finding entry has a labeled severity field. Absent or
  merged into blast radius = FAIL.

---

## Aspirational Criteria — (passed/10) × 10 pts

### C-09 — Systemic cross-skill findings elevated
- **Weight:** aspirational
- **Category:** signal quality
- **Text:** Findings corroborated by two or more sub-skills are labeled SYSTEMIC and
  ranked above isolated findings of equivalent blast radius. Systemic label indicates
  the same root cause propagates across independent simulation boundaries, increasing
  finding credibility.
- **Pass condition:** Output includes a mechanism for identifying cross-sub-skill
  corroboration (e.g., calibration step, cross-ref section) and marks matching findings
  SYSTEMIC. No corroboration mechanism = FAIL.

---

### C-10 — Verdict names specific component
- **Weight:** aspirational
- **Category:** precision
- **Text:** The VERDICT sentence names the specific component from the calibration table
  or census that anchors the highest-blast-radius finding. A verdict that says "wide
  blast radius finding detected" without naming the component does not satisfy this
  criterion.
- **Pass condition:** VERDICT sentence includes a specific component name (e.g., a
  service, schema, cache, or queue from the census). Generic language without component
  name = FAIL.

---

### C-11 — Blast radius operationalized via component names
- **Weight:** aspirational
- **Category:** precision
- **Text:** Blast radius assessments throughout the report reference specific named
  components from the topology, not generic descriptions. "Wide blast radius" must be
  accompanied by the component that makes it wide. Generic blast radius language
  (e.g., "affects multiple systems") without a named component does not satisfy this
  criterion.
- **Pass condition:** Finding entries include census or spec component names in their
  blast radius assessments. Generic descriptions without component names = FAIL.

---

### C-12 — Per-sub-skill schema typed with sub-skill vocabulary
- **Weight:** aspirational
- **Category:** fidelity
- **Text:** Each sub-skill's findings use a vocabulary and column schema distinct to
  that sub-skill. trace-contract uses Producer/Consumer/Contract term/Expected/Actual.
  trace-state uses State/Invariant/Violated. trace-permissions uses Role/Resource/Action.
  flow-lifecycle uses Phase/Entry contract/Exit contract. flow-trigger uses
  Trigger/Fire order/Race condition. A uniform generic schema across all five = FAIL.
- **Pass condition:** At least four of five sub-skills use distinct typed column
  vocabularies. One-size-fits-all schema = FAIL.

---

### C-13 — Severity and blast radius co-located as distinct fields
- **Weight:** aspirational
- **Category:** integrity
- **Text:** Blast radius and severity appear as separate labeled fields in every
  consolidated finding entry. They are never merged into a single "impact," "priority,"
  or "risk" field. Wide blast radius with low severity and narrow blast radius with
  high severity are both valid combinations that a merged field cannot represent.
- **Pass condition:** Every finding in CONSOLIDATE has both a "Blast radius" field and
  a "Severity" field as distinct labels. Merged = FAIL. One field present without the
  other = PARTIAL.

---

### C-14 — Calibration block (post-execution blast-radius re-grounding)
- **Weight:** aspirational
- **Category:** process architecture
- **Text:** A named calibration section exists after all five sub-skills complete and
  before the consolidated ranking is written. Its purpose is to re-ground blast radius
  in actual findings rather than pre-declared topology or spec expectations. The
  calibration must explicitly reconcile anticipated topology against found evidence —
  upgrading, downgrading, or confirming blast radius assessments based on what the
  simulation actually surfaced. The interrogative calibration variant (Q1–Q5 questions)
  satisfies this criterion equally with the phase-block variant.
- **Pass condition:** Output contains a named calibration section (CALIBRATION BLOCK,
  calibration questions, or equivalent) positioned after sub-skill execution and before
  CONSOLIDATE, with content that explicitly re-evaluates blast radius from evidence.
  No such section = FAIL.

---

### C-15 — Pre-execution topology census (Phase 0)
- **Weight:** aspirational
- **Category:** process architecture
- **Text:** Before any sub-skill runs, the campaign produces a named Phase 0 that
  catalogs all components in scope, shared state surfaces, downstream callers, and
  role-resource pairs. This census becomes the controlled vocabulary for all blast
  radius claims in subsequent phases. Without a census, blast radius claims reference
  generic descriptions rather than specific named system artifacts. The census
  complements the post-execution calibration block: Phase 0 declares expected topology;
  calibration reconciles expected against found.
- **Pass condition:** Output includes a named pre-execution section (Phase 0, topology
  census, or equivalent) listing components, shared state surfaces, and downstream
  dependencies before any sub-skill findings appear. No such section, or a census
  inserted after sub-skill execution, = FAIL.

---

### C-16 — Per-phase exit criteria gates
- **Weight:** aspirational
- **Category:** process architecture
- **Text:** Each sub-skill phase ends with an explicit EXIT CRITERIA statement specifying
  what constitutes a complete phase execution. Clean outcomes must be affirmatively
  declared (e.g., "trace-contract: clean — no mismatches detected"), not left implicit
  through silence. Exit gates prevent partial execution from being mistaken for a
  complete campaign and enforce that "nothing found" is a positive result, not an
  omission.
- **Pass condition:** At least four of five sub-skill phases include an explicit EXIT
  CRITERIA or equivalent named completion gate with an affirmative clean-state statement.
  Checkpoints that gate on confirmation without specifying clean outcomes are PARTIAL.
  No gates at all = FAIL.

---

### C-17 — Contract-baseline reconciliation (CONFIRMED? distinction)
- **Weight:** aspirational
- **Category:** signal quality
- **Text:** Runtime findings from flow-lifecycle and flow-trigger are explicitly
  cross-referenced against contract topology findings from trace-contract, trace-state,
  and trace-permissions. A finding that matches both a contract topology entry and a
  runtime simulation is elevated to CONFIRMED status, distinguishing it from a RUNTIME
  ANOMALY with no contract precedent. CONFIRMED violations have higher credibility
  because two independent simulation methods independently produced the same finding.
  This distinction goes beyond SYSTEMIC labeling (which only requires two sub-skills)
  by specifically requiring a contract-layer corroboration.
- **Pass condition:** Calibration or consolidation step includes a CONFIRMED / unconfirmed
  distinction for findings, with evidence of cross-referencing runtime sub-skill outputs
  against contract topology sub-skill outputs. No distinction = FAIL.

---

### C-18 — Interrogative calibration register (Q1–Qn question-driven synthesis)
- **Weight:** aspirational
- **Category:** process architecture
- **Text:** Calibration is structured as a numbered series of explicit named questions
  answered from sub-skill evidence, each targeting a specific evidence-extraction step:
  which components appeared in findings (Q1), which touch shared state (Q2), which are
  corroborated across sub-skills (Q3), which are spec-gap amplified (Q4), what is the
  blast-radius anchor (Q5). The interrogative form forces explicit reasoning steps
  before ranking begins, making component naming and blast radius re-grounding a
  deliberate act rather than an implicit output. The interrogative register is an
  architectural alternative to a phase-block calibration structure, not a complement
  to it — a prompt satisfying C-18 will typically satisfy C-14 via the same mechanism.
- **Pass condition:** Output contains at least four named interrogative calibration
  questions (Q1, Q2, ...) answered from sub-skill evidence before the consolidated
  ranking is written, covering at minimum: component identification from findings,
  shared state identification, cross-sub-skill corroboration, and a named blast-radius
  anchor finding. Fewer than four questions = FAIL.
```

---

**What changed from v3:**

| Change | Detail |
|--------|--------|
| Aspirational denominator | 6 → 10 (four new criteria added) |
| C-14 updated | Pass condition now explicitly accepts interrogative calibration (V-03 pattern) as equal to phase-block variant |
| C-15 new | Pre-execution topology census — the Phase 0 pre-declaration that enables calibration to reconcile expected vs. found |
| C-16 new | Per-phase exit criteria gates — affirmative completion declarations that make "clean" a positive result |
| C-17 new | Contract-baseline reconciliation — CONFIRMED? distinction elevating runtime findings that match contract topology entries |
| C-18 new | Interrogative calibration register — Q1–Qn question-driven synthesis as an independent architectural alternative to the phase-block calibration |

The four new criteria are process-architecture criteria — each specifies a structural mechanism, not an output property. C-14 (the existing calibration block criterion) was also updated to make explicit that the interrogative form (V-03) and the phase-block form (V-04) are both valid implementations, since the scorecard confirmed both achieve the evidence-grounding intent.
