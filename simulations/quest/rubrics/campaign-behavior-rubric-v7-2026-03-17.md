Reading the scorecard differential analysis carefully to identify the three new excellence patterns before writing the updated rubric.

From the V-05 differential, three structural reinforcements emerge that are independent of C-22/C-23 and of each other:

1. **`[ANCHOR:]` tags on Ph1/Ph2 headers** — makes anchor dependency scannable from headers without reading body text → **C-24**
2. **Q6 sequence integrity gate** — a calibration question that self-validates anchor ordering at runtime → **C-25**
3. **Propagation chain in field 3** (+ VERDICT + DEFINITIONS + Q1 chain tracing) — makes blast radius claims mechanically auditable rather than asserted → **C-26**

Denominator bumps from 15 → 18.

---

```markdown
# Quest Rubric — campaign-behavior (org-review)
**Version:** v7
**Updated:** 2026-03-17
**Author:** Quest Engine

---

## Scoring Formula

| Tier         | Criteria                         | Max pts |
|--------------|----------------------------------|---------|
| Essential    | C-01–C-05 (10 pts each)          | 50      |
| Recommended  | C-06–C-08 (10 pts each)          | 30      |
| Aspirational | C-09–C-26 — (passed/18) × 10    | 10      |
| **Total**    |                                  | **90**  |

PASS = full credit. PARTIAL = half credit. FAIL = 0.
Aspirational tier is binary PASS/FAIL per criterion; score = (count passed / 18) × 10,
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
- **Category:** correctness
- **Text:** The report either names at least one contract violation found during the
  campaign, or explicitly states that no violations were detected. A contract violation
  is a producer/consumer mismatch, broken invariant, or privilege boundary crossed.
- **Pass condition:** Output contains a labeled "contract violations" section (or
  equivalent heading) with findings or a clear "none detected" statement, naming both
  producer and consumer for each violation. Omitting the section entirely = FAIL.

---

### C-05 — Lifecycle violations surfaced or explicitly cleared
- **Weight:** essential
- **Category:** correctness
- **Text:** The flow-lifecycle sub-skill evaluates exception paths for each lifecycle
  phase, not only the happy path. The report either names lifecycle violations found
  or explicitly states that none were detected.
- **Pass condition:** flow-lifecycle output includes an exception path column or
  equivalent evaluation. Exit criteria requires all phases evaluated. Omitting
  exception paths entirely = FAIL.

---

## Recommended Criteria (30 pts total)

### C-06 — Blast radius label per finding
- **Weight:** recommended
- **Category:** correctness
- **Text:** Every finding carries an explicit blast radius label. The label must use a
  named tier: WIDE / MEDIUM / NARROW (or equivalent: SYSTEMIC / ISOLATED / LOCAL).
  Unlabeled findings cannot be ranked and cannot be compared across campaigns.
- **Pass condition:** Every finding block includes a blast radius field with a named
  tier value. Any finding missing the label = FAIL.

---

### C-07 — Confirmation status per finding
- **Weight:** recommended
- **Category:** correctness
- **Text:** Every finding carries an explicit confirmation status: CONFIRMED, RUNTIME
  ANOMALY, or equivalent named tier. Status must appear as a labeled field, not
  inferred from prose.
- **Pass condition:** Every finding block includes a confirmation status field with a
  named value. Any finding missing the field = FAIL.

---

### C-08 — Sub-skill attribution per finding
- **Weight:** recommended
- **Category:** coverage
- **Text:** Every finding identifies the sub-skill (source phase) that produced it.
  Attribution enables traceability back to the originating analysis and supports
  compound finding detection across phases.
- **Pass condition:** Every finding block includes a source phase field naming the
  sub-skill. Any finding missing attribution = FAIL.

---

## Aspirational Criteria (18 criteria, score = passed/18 × 10)

### C-09 — F-NN sequential finding IDs
- **Category:** structure
- **Text:** Findings are assigned sequential IDs (F-01, F-02, … or Finding 1, Finding
  2, …) in blast-radius order. Sequential IDs enable cross-referencing in spec gap
  citations, compound finding declarations, and post-campaign tracking.
- **Pass condition:** All findings carry sequenced numeric IDs. IDs align with
  blast-radius ranking order. Unsequenced or missing IDs = FAIL.

---

### C-10 — Lifecycle phase tag per flow finding
- **Category:** structure
- **Text:** Flow-lifecycle and flow-trigger findings include a lifecycle phase tag
  (e.g., INIT, ACTIVE, SUSPENDED, TERMINAL) indicating which phase the finding
  belongs to. Phase tags enable phase-specific blast radius comparison.
- **Pass condition:** Phase tag column or field present in both flow sub-skill outputs.
  Phase values use named lifecycle tiers, not free text. Missing column = FAIL.

---

### C-11 — Compound findings identified
- **Category:** correctness
- **Text:** The campaign identifies findings that originate from multiple sub-skills
  (compound findings). A compound finding is one whose blast radius can only be
  determined by combining evidence from two or more phases.
- **Pass condition:** Exit criteria or CONSOLIDATE section explicitly tracks compound
  anchor hits or multi-source attributions. Absence of any compound tracking = FAIL.

---

### C-12 — Spec gap missing-clause citation
- **Category:** correctness
- **Text:** Each spec gap finding includes a citation to the specific clause, section,
  or contract term that is absent from the spec. "Gap exists" without locating the
  missing clause is incomplete.
- **Pass condition:** Every spec gap finding names the missing clause (or states
  "clause not present" with enough specificity to locate it). Gaps without citations
  = FAIL.

---

### C-13 — Contract violations name producer and consumer
- **Category:** correctness
- **Text:** Each contract violation finding names both the producing component and the
  consuming component. Violations identified without both parties cannot be resolved
  because ownership is ambiguous.
- **Pass condition:** Every contract violation finding names producer and consumer.
  Violations missing either party = FAIL.

---

### C-14 — Privilege escalation paths surfaced or cleared
- **Category:** coverage
- **Text:** The trace-permissions sub-skill tracks privilege escalation paths
  explicitly. The report either names escalation paths found or states "none
  detected."
- **Pass condition:** A labeled "privilege escalation paths" field or section appears
  in the output with findings or a clear "none detected" statement. Omitting the
  field entirely = FAIL.

---

### C-15 — Severity with defined scale
- **Category:** structure
- **Text:** Each finding includes a severity rating using a defined scale (high / med
  / low or equivalent). The scale definition must appear in the output (DEFINITIONS
  section or equivalent) so reviewers can interpret ratings consistently.
- **Pass condition:** Severity field present in every finding block; scale definition
  present in output. Any finding missing severity, or scale undefined, = FAIL.

---

### C-16 — Executive summary top-3 surfaced
- **Category:** communication
- **Text:** A reader assessing campaign risk can identify the three highest-impact
  findings without reading the full report. This may be satisfied by a dedicated
  Executive Summary section or by a ranked findings list where the top three appear
  first with blast radius and confirmation labeled.
- **Pass condition:** Top three findings are identifiable (by position or explicit
  labeling) with blast radius and confirmation status present for each. No way to
  identify top three = FAIL.

---

### C-17 — Evidence basis per CONFIRMED finding
- **Category:** correctness
- **Text:** Every finding classified CONFIRMED cites the matching evidence from
  earlier phases (e.g., "matches Phase 1 finding F-03"). CONFIRMED without an
  evidence citation is an unverified assertion.
- **Pass condition:** Every CONFIRMED finding names the matching prior-phase finding
  or evidence source. CONFIRMED without citation = FAIL.

---

### C-18 — Q1–Qn calibration questions (n ≥ 3)
- **Category:** rigor
- **Text:** The campaign includes at least three named calibration questions (Q1–Qn)
  with specific re-grounding targets. Calibration questions serve as explicit
  checkpoints that prevent the campaign from drifting into generic analysis.
- **Pass condition:** n ≥ 3 calibration questions present, each with a named
  re-grounding target. Fewer than three, or questions without targets, = FAIL.

---

### C-19 — Atomic 7-field finding block
- **Category:** structure
- **Text:** Each finding uses a standardized atomic block with exactly seven labeled
  fields: (1) finding name/title, (2) source phase, (3) blast radius, (4) severity,
  (5) description, (6) confirmation status, (7) recommendation or next action.
  Consistent structure enables mechanical comparison across findings and campaigns.
- **Pass condition:** All seven fields explicitly numbered and labeled in every
  finding block. Missing or merged fields = FAIL.

---

### C-20 — Tiebreaker protocol stated and applied
- **Category:** correctness
- **Text:** When two findings have equal blast radius, a tiebreaker protocol
  determines their relative order. The protocol must be stated in the output and
  its application documented (stating whether any ties were encountered).
- **Pass condition:** Tiebreaker protocol appears in DEFINITIONS or equivalent; output
  states whether ties occurred and how they were resolved. Protocol absent = FAIL.

---

### C-21 — SYSTEMIC findings enumerate affected phases
- **Category:** correctness
- **Text:** Any finding classified SYSTEMIC must enumerate the specific lifecycle
  phases affected. Binary "SYSTEMIC: yes" without a phase list is not valid because
  it cannot be verified or compared. Phase enumeration is what distinguishes a
  genuine SYSTEMIC classification from an inflated one.
- **Pass condition:** Every SYSTEMIC finding lists the affected phases by name.
  SYSTEMIC without phase list = FAIL.

---

### C-22 — State-anchor execution order
- **Category:** structure
- **Text:** trace-state is designated as the first sub-skill to execute, with explicit
  rationale that it pre-classifies blast radius candidates from shared-state topology
  before contract, access, or flow analysis begins. This sequencing ensures downstream
  sub-skills inherit the state topology classification rather than producing
  independent and potentially inconsistent blast radius assessments.
- **Pass condition:** trace-state is identified as Phase 1 (or equivalent first
  position) with stated rationale linking its execution order to blast radius
  pre-classification. Any ordering that places trace-state after other analytical
  sub-skills = FAIL. Rationale without explicit first-position designation = PARTIAL.

---

### C-23 — Permissions-anchor positioned before flow sub-skills
- **Category:** structure
- **Text:** trace-permissions is designated before flow-lifecycle and flow-trigger,
  with explicit rationale that flow violations crossing a privilege boundary are
  SYSTEMIC by definition. Without the permissions anchor in place, flow sub-skills
  cannot correctly classify blast radius for privilege-crossing findings.
- **Pass condition:** trace-permissions is identified as executing before all flow
  sub-skills, with stated rationale linking privilege boundary classification to
  flow blast radius correctness. Any ordering that places trace-permissions after a
  flow sub-skill = FAIL. Rationale without explicit ordering statement = PARTIAL.

---

### C-24 — Anchor tags on phase headers
- **Category:** structure
- **Text:** Phase headers for the state anchor (Ph1) and permissions anchor (Ph2)
  carry explicit `[ANCHOR:...]` tags identifying their role in the execution
  dependency chain. Anchor tags make the dependency scannable from headers alone —
  a reviewer can confirm anchor ordering without reading phase body text.
- **Pass condition:** Ph1 and Ph2 headers (or equivalent anchor-phase designations)
  include an `[ANCHOR:...]` tag or equivalent inline marker naming the anchor role.
  Anchor rationale present only in body text, with no scannable header marker = FAIL.

---

### C-25 — Q6 sequence integrity gate
- **Category:** rigor
- **Text:** A dedicated calibration question (Q6 or equivalent named gate) validates
  anchor ordering at runtime: it asks whether Ph1 ran before Ph2, Ph2 ran before
  Ph3–Ph5, and whether the ordering produced the intended pre-classification benefits.
  The sequence integrity gate is a self-check that fires after the phases complete,
  not a structural declaration made before execution begins.
- **Pass condition:** A calibration question explicitly validates anchor execution
  order and asks whether the pre-classification benefit was realized. Structural
  ordering stated in DEFINITIONS without a post-execution validation question = FAIL.

---

### C-26 — Propagation chain in blast radius field
- **Category:** correctness
- **Text:** Field 3 (blast radius) of each finding block includes an explicit
  propagation chain tracing the failure path from origin to terminus
  (e.g., "ComponentA → ServiceB → ConsumerC → terminus"). The chain makes the blast
  radius classification mechanically auditable: a reviewer can follow each hop and
  verify the WIDE / MEDIUM / NARROW tier assignment rather than accepting an
  asserted label. The chain must also appear in the finding's VERDICT and in the
  campaign DEFINITIONS, and Q1 must trace the chain to terminus.
- **Pass condition:** Field 3 includes a propagation chain with named hops. VERDICT
  restates the chain. DEFINITIONS establish chain format. Q1 traces to terminus.
  All four elements required. Blast radius label without a chain = FAIL. Chain in
  field 3 only, without VERDICT and Q1 restatement = PARTIAL.

---

## Version History

| Version | Date       | Changes |
|---------|------------|---------|
| v1      | 2026-03-14 | Initial rubric (C-01–C-08, essential + recommended only) |
| v2      | 2026-03-14 | Added aspirational tier C-09–C-13 (denominator 5) |
| v3      | 2026-03-15 | Extended aspirational to C-09–C-16 (denominator 8) |
| v4      | 2026-03-15 | Extended aspirational to C-09–C-19 (denominator 11) |
| v5      | 2026-03-16 | Extended aspirational to C-09–C-21 (denominator 13) |
| v6      | 2026-03-17 | Added C-22 state-anchor order, C-23 permissions-anchor position (denominator 15) |
| v7      | 2026-03-17 | Added C-24 anchor tags, C-25 Q6 gate, C-26 propagation chain (denominator 18) |
```

---

**What changed v6 → v7:**

| Criterion | Source | What it captures |
|-----------|--------|-----------------|
| C-24 | V-01/V-04/V-05 `[ANCHOR:]` tags | Anchor dependency scannable from headers, not just body text |
| C-25 | V-02/V-04/V-05 Q6 | Post-execution self-check that validates ordering produced its intended benefit |
| C-26 | V-03/V-05 field 3 chain | Blast radius claims become mechanically auditable via named propagation hops |

C-26 is the strictest new criterion — it requires four independent locations (field 3, VERDICT, DEFINITIONS, Q1) to all carry the chain. Partial credit is available when field 3 has the chain but VERDICT/Q1 do not restate it.
