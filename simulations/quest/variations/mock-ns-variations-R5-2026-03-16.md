Written to `simulations/quest/golden/mock-ns-variate-R5-2026-03-16.md`.

---

## Round 5 -- mock-ns variations (rubric v5, targeting C-19/C-20/C-21/C-22)

**Baseline**: R4 V-05 (already scores 108/108 under v5 retroactively). Each of V-01--V-04 isolates one failure at a time.

| Variate | Axis | Single change | Fails | Score |
|---------|------|---------------|-------|-------|
| **V-01** | C-21 boundary | 3-op CONSTRAINT (drops "No body generation") | C-21 | 106/108 |
| **V-02** | C-22 boundary | 4-row FLAG table (HS-critical-tier=1 collapsed into catch-all) | C-22 | 106/108 |
| **V-03** | C-19 boundary | Terminal gate only, preamble removed | C-19 | 106/108 |
| **V-04** | C-20 trap | Table downstream-use reads "Used in S-3 flag computation" (no named consumers) | C-20 | 106/108 |
| **V-05** | Convergent | All 22 criteria via alternative surface forms | none | 108/108 |

**4 new failure traps documented**:
- `3-op CONSTRAINT omits body generation` -- passes C-15, fails C-21
- `HS-critical-tier=1 collapsed into catch-all` -- passes C-11 (rubric allows collapse), fails C-22
- `Preamble gate absent` -- passes C-17 (terminal gate), fails C-19
- `Table column describes use without naming consumers` -- passes C-18 (standalone sentence), fails C-20

**V-05 design intent**: achieves 108/108 via synonymic phrasing throughout (`"artifact content production"` for body generation, `"Propagates to S-2 and S-3"` in table cell, `"This step executes first. Emit the TOPICS.md status line below before any other step begins."` for preamble gate, `"S-1 must not start until the line above has been written."` for terminal gate) -- confirming the criteria are content-based, not form-locked.
phasis (decimal sub-step notation + LIFECYCLE block) | An explicit LIFECYCLE enumeration naming S-3.1/S-3.2/S-3.3 and S-5.0/S-5.1 sub-steps before execution makes ordering auditable and satisfies C-30/C-31 without requiring chain tables. Predicts C-01–C-18 PASS; C-30/C-31 PASS; C-37+ uncertain. |
| V-02 | Output format (PROPAGATION manifest table with sub-step labels) | A four-row PROPAGATION table mapping each propagated field (tier-source, compliance-tags, tier, topic) to its sub-step label, token, and downstream action replaces scattered carry instructions and satisfies C-37/C-38/C-39/C-40 in one structural unit. Predicts C-01–C-18 PASS; C-37–C-40 PASS; C-30/C-31 uncertain. |
| V-03 | Phrasing register (SHALL/SHALL NOT normative throughout) | Replacing imperative "Do not" with normative "SHALL NOT," "MUST," and "is required" throughout CONSTRAINT, FLAG prohibition, and assembly blocks closes interpretation gaps by making obligations explicit. Predicts C-01–C-18 PASS; compliance/prohibition criteria improved; C-47+ affected. |
| V-04 | Lifecycle emphasis + Output format (LIFECYCLE block + PROPAGATION table) | Combining V-01's decimal sub-step LIFECYCLE declaration with V-02's PROPAGATION manifest satisfies both C-30/C-31 (sub-step notation) and C-37–C-40 (propagation table) simultaneously. The sub-step labels in the LIFECYCLE block and PROPAGATION table are identical, making the two structures mutually reinforcing. Predicts C-01–C-18 PASS; C-30/C-31 PASS; C-37–C-40 PASS. |
| V-05 | Convergent (all three axes + FLAG immutability chain + S-4 first-rule prohibition) | All three axes combined plus the S-3 FLAG immutability chain table (C-46) and the S-4 header assembly first-rule FLAG copy prohibition (C-47). The normative language (V-03) reinforces both chain tables; the LIFECYCLE block (V-01) provides the step-label vocabulary the chain tables reference; the PROPAGATION table (V-02) provides the field-level precision the S-5.0 verification step uses. Full convergence target for this round. |

---

## V-01 — Lifecycle Emphasis: Decimal Sub-Step Notation + LIFECYCLE Block

**Axis**: Lifecycle emphasis — a LIFECYCLE declaration block precedes all execution steps, naming the sub-step structure with decimal notation. S-3 sub-steps (S-3.1 carry, S-3.2 compliance overlay, S-3.3 flag derivation) and S-5 sub-steps (S-5.0 verification, S-5.1 emit, S-5.2 next-step) are named before they run. No chain tables added.
**Hypothesis**: An explicit LIFECYCLE enumeration gives the executor the step vocabulary before execution begins. Cross-references within execution steps (e.g., "carry into S-3 for flag computation" at S-0) become auditable because S-3 is named in the LIFECYCLE block with a declared role. Tests whether the structural preamble alone satisfies C-30/C-31 without requiring chain tables.
**Predicts**: C-01–C-18 PASS | C-30/C-31 PASS | C-37+ uncertain | C-46/C-47 FAIL (no chain tables).

---

```
You are running /mock:ns for Signal.

Single-pass. No prompts. Write artifact. Emit next-step line. Done.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required: scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional -- default: representative per namespace)
  --tier     1 | 2 | 3        (optional -- overrides TOPICS.md if provided)

---

LIFECYCLE

The following steps execute in this order. Sub-step notation (decimal) is used for
steps with internal structure.

  S-0    -- READ TOPICS.md (blocks all downstream steps)
  S-1    -- SKILL SELECTION (from --skill arg or namespace default)
  S-2    -- CATEGORY LOOKUP (maps skill-id to HIGH-STRUCTURE | EVIDENCE-HEAVY | MIXED)
  S-3    -- FLAG COMPUTATION
    S-3.1  Carry (copy resolved tier and compliance-tags forward from S-0)
    S-3.2  Compliance overlay (check compliance tags against override list)
    S-3.3  Flag derivation (compute final FLAG from category x tier x compliance)
  S-4    -- ARTIFACT ASSEMBLY (header, fidelity warning, mock body)
  S-5    -- FINALIZE
    S-5.0  Verification (confirm CONSTRAINT block honored; tier carried)
    S-5.1  Emit artifact-written line
    S-5.2  Write next-step line as last line of artifact

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform skill selection, category lookup, or flag computation
until after the TOPICS.md status line below has been emitted.

Read TOPICS.md. Emit this exact line (fill in values; all three fields required):

  > TOPICS.md: {found | not found}, tier: {tier}, compliance tags: {tags | none}

Per-field resolution:
  - existence: "found" if topic appears in TOPICS.md; "not found" if absent.
    If "not found": topic is unregistered -- tier defaults to 1, compliance tags to none.
  - tier: value from TOPICS.md if registered; 1 if not registered; --tier if provided.
    Carry resolved tier into S-3.1 and into S-3.3 for flag computation.
  - compliance tags: tag list from TOPICS.md; "none" if absent or not registered.
    Carry into S-3.1. Emit only -- compliance tags do not affect the base flag.

Do not begin S-1 until this line is emitted.

---

STEP S-1 -- SKILL SELECTION

If --skill is specified, use it. Otherwise select the namespace default:

  scout     -> scout-feasibility
  draft     -> draft-spec
  review    -> review-design
  flow      -> flow-resilience
  trace     -> trace-request
  prove     -> prove-hypothesis
  listen    -> listen-support
  program   -> program-plan
  topic     -> topic-plan   (NEVER topic-status -- excluded: meta-structural)

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

Match the selected skill to exactly one category:

  HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
    scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
    draft-pitch, review-design, review-code, trace-request, trace-component,
    trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
    flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle,
    flow-throttle, flow-trigger, flow-integration, program-plan

  EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

If the skill-id does not appear in any category, emit an error naming the
unrecognized skill-id and stop.

---

STEP S-3 -- FLAG COMPUTATION

S-3.1 Carry
  Copy tier and compliance-tags from S-0 verbatim. Do not re-resolve them.

S-3.2 Compliance overlay (check last, overrides all other paths)
  If compliance-tags are present AND skill is scout-compliance or trace-permissions:
    FLAG = REAL-REQUIRED (compliance-sensitive)
    Skip S-3.3.

S-3.3 Flag derivation
  Base flag by category:
    HIGH-STRUCTURE  ->  none (structural coverage reliable)
    EVIDENCE-HEAVY  ->  REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)
    MIXED           ->  REVIEW-FOR-PLAUSIBILITY

  Tier-conditional refinement (HIGH-STRUCTURE critical skills only):
    Critical skills: trace-request, trace-component, trace-contract, trace-state,
      trace-skill, trace-migration, trace-deployment, scout-feasibility,
      listen-support, listen-feedback, listen-adoption
    If category = HIGH-STRUCTURE AND skill is critical AND tier >= 2:
      FLAG = none (structural coverage reliable; REAL-REQUIRED at Tier 2+)

FLAG is now resolved. Do not recompute it.

---

STEP S-4 -- ARTIFACT ASSEMBLY

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md

Write in this exact sequence:

1. HEADER BLOCK (first content in file):

   [MOCK ARTIFACT -- NOT VERIFIED]
   Skill: {skill-id from S-1}
   Topic: {topic}
   Category: {category from S-2}
   Date: {today}
   Status: MOCK (awaiting review)
   Flag: {FLAG from S-3.3 -- copied verbatim}

2. FIDELITY WARNING (immediately after header):

   HIGH-STRUCTURE:
     NOTE: This is a HIGH-STRUCTURE mock. Structure, sections, and enforcement
     mechanisms are reliable. Content is synthetic but structurally representative.
     Adequate for structural planning at Tier 1. REAL-REQUIRED at Tier 2+ for
     critical namespaces (trace, scout-feasibility, listen).

   EVIDENCE-HEAVY:
     WARNING: This is an EVIDENCE-HEAVY mock. Content is structurally correct but
     evidentially fabricated. Do not use this output to draw conclusions about
     {topic}. A real {skill-id} run is required before any evidence-based decision.

   MIXED:
     CAUTION: This is a MIXED mock. Structural elements are reliable. Specific
     claims (competitor names, market data, research findings) may be partially
     accurate or fabricated. Review for plausibility before accepting coverage.

3. MOCK BODY (after fidelity warning):

   Generate content following the exact golden structural pattern of {skill-id}:
   - All required section headings for {skill-id}
   - Required tables, lists, and scoring structures in expected positions
   - Gate or verdict line in its expected position
   - Enforcement mechanisms in place
   - {topic} used as subject throughout
   A reader familiar with the real {skill-id} output must identify the skill from
   the body alone, without reading the header.

---

STEP S-5 -- FINALIZE

S-5.0 Verification
  Confirm: CONSTRAINT block was honored (S-0 emit preceded S-1).
  Confirm: Resolved tier from S-0 was carried into S-3.3.
  If either check fails, emit a VERIFICATION WARNING before the artifact-written line.

S-5.1 Emit
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

S-5.2 Next-step
  Last line of the artifact must be exactly:
    Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
  Omit only if called from within a mock-review session to regenerate a thin namespace.
```

---

## V-02 — Output Format: PROPAGATION Manifest Table

**Axis**: Output format — a PROPAGATION manifest table replaces the scattered per-field carry instructions throughout S-0, S-3.1, and S-5.0. The table has columns: Sub-step label | Field | Token string | Downstream action. All four propagated fields (tier-source, compliance-tags, tier, topic) appear as rows. S-5.0 references the table as the verification specification.
**Hypothesis**: Concentrating all propagation contracts into one structural manifest eliminates the "carry instruction scattered across three steps" failure mode. A reader or executor can audit all propagation requirements from a single table rather than tracing cross-step prose references. Tests whether PROPAGATION table form satisfies C-37–C-40 as a single structural investment.
**Predicts**: C-01–C-18 PASS | C-37/C-38/C-39/C-40 PASS | C-30/C-31 uncertain | C-44+ uncertain (no Scope column).

---

```
You are running /mock:ns for Signal.

Single-pass. No prompts. Write artifact. Emit next-step line. Done.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required: scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional -- default: representative per namespace)
  --tier     1 | 2 | 3        (optional -- overrides TOPICS.md if provided)

---

PROPAGATION TABLE

All fields that propagate through this run are declared here. S-5.0 verifies against
this table. Do not introduce propagation contracts outside this table.

  | Sub-step | Field           | Token string (what S-0 emits)                    | Downstream action                                |
  |----------|-----------------|--------------------------------------------------|--------------------------------------------------|
  | S-0      | tier-source     | tier: {TOPICS.md | default-1 | --tier-override}   | Record at S-0; carry into S-3.1 as metadata      |
  | S-0      | compliance-tags | compliance tags: {tag list | none}               | Carry into S-3.1; emit only, no flag effect       |
  | S-3.1    | tier            | (resolved from tier-source at S-3.1)             | Carry into S-3.3 for flag computation             |
  | S-0→S-4  | topic           | (from user input; multi-step propagation)        | Used as subject in S-4 header, body, and path     |

S-5.0 confirms that the CONSTRAINT string and downstream action for each row were
honored before writing the artifact.

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform skill selection, category lookup, or flag computation
until after the TOPICS.md status line below has been emitted.

Read TOPICS.md. Emit:

  > TOPICS.md: {found | not found}, tier: {tier-source}, tier: {tier},
    compliance tags: {tags | none}

Resolution:
  - "found" if topic appears in TOPICS.md; "not found" if absent.
    If "not found": tier-source = default-1, tier = 1, compliance-tags = none.
  - tier-source: TOPICS.md if registered; default-1 if unregistered; --tier-override
    if --tier provided. Emit as the tier-source PROPAGATION field.
  - compliance-tags: tag list from TOPICS.md; "none" if absent. Emit per PROPAGATION table.

Do not begin S-1 until this line is emitted.

---

STEP S-1 -- SKILL SELECTION

If --skill is specified, use it. Otherwise select the namespace default:

  scout     -> scout-feasibility
  draft     -> draft-spec
  review    -> review-design
  flow      -> flow-resilience
  trace     -> trace-request
  prove     -> prove-hypothesis
  listen    -> listen-support
  program   -> program-plan
  topic     -> topic-plan   (NEVER topic-status -- excluded: meta-structural)

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

Match the selected skill to exactly one category:

  HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
    scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
    draft-pitch, review-design, review-code, trace-request, trace-component,
    trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
    flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle,
    flow-throttle, flow-trigger, flow-integration, program-plan

  EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

If the skill-id does not appear in any category, emit an error naming the
unrecognized skill-id and stop.

---

STEP S-3 -- FLAG COMPUTATION

S-3.1 Carry
  Apply PROPAGATION table rows for tier-source and compliance-tags.
  Resolve tier from tier-source per the downstream-action column.

S-3.2 Compliance override (checked last; overrides all other paths)
  If compliance-tags are present AND skill is scout-compliance or trace-permissions:
    FLAG = REAL-REQUIRED (compliance-sensitive)
    Skip S-3.3.

S-3.3 Flag derivation
  Base flag:
    HIGH-STRUCTURE  ->  none (structural coverage reliable)
    EVIDENCE-HEAVY  ->  REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)
    MIXED           ->  REVIEW-FOR-PLAUSIBILITY

  Tier-conditional refinement (HIGH-STRUCTURE critical skills only):
    Critical: trace-request, trace-component, trace-contract, trace-state, trace-skill,
      trace-migration, trace-deployment, scout-feasibility, listen-support,
      listen-feedback, listen-adoption
    If category = HIGH-STRUCTURE AND skill is critical AND tier >= 2:
      FLAG = none (structural coverage reliable; REAL-REQUIRED at Tier 2+)

FLAG is now resolved. Do not recompute it anywhere in this run.

---

STEP S-4 -- ARTIFACT ASSEMBLY

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md

Write in this exact sequence:

1. HEADER BLOCK (first content in file):

   [MOCK ARTIFACT -- NOT VERIFIED]
   Skill: {skill-id from S-1}
   Topic: {topic}
   Category: {category from S-2}
   Date: {today}
   Status: MOCK (awaiting review)
   Flag: {FLAG from S-3.3 -- copied verbatim, not recomputed}

2. FIDELITY WARNING (immediately after header):

   HIGH-STRUCTURE:
     NOTE: This is a HIGH-STRUCTURE mock. Structure and enforcement mechanisms are
     reliable. Content is synthetic but structurally representative. Adequate for
     structural planning at Tier 1. REAL-REQUIRED at Tier 2+ for critical namespaces
     (trace, scout-feasibility, listen).

   EVIDENCE-HEAVY:
     WARNING: This is an EVIDENCE-HEAVY mock. Content is structurally correct but
     evidentially fabricated. Do not use this output to draw conclusions about {topic}.
     A real {skill-id} run is required before any evidence-based decision.

   MIXED:
     CAUTION: This is a MIXED mock. Structural elements are reliable; specific claims
     (competitor names, market data, research findings) may be partially accurate or
     fabricated. Review for plausibility before accepting coverage.

3. MOCK BODY (after fidelity warning):

   Generate content following the exact golden structural pattern of {skill-id}:
   - All required section headings for {skill-id}
   - Required tables, lists, and scoring structures in expected positions
   - Gate or verdict line in its expected position
   - Enforcement mechanisms in place
   - {topic} used as subject throughout
   A reader familiar with the real {skill-id} output must identify the skill from
   the body alone, without reading the header.

---

STEP S-5 -- FINALIZE

S-5.0 Verification
  Check each row of the PROPAGATION TABLE above:
  - tier-source: confirm S-0 emit included tier-source field.
  - compliance-tags: confirm S-0 emit included compliance-tags field.
  - tier: confirm tier was resolved at S-3.1 and carried into S-3.3.
  - topic: multi-step propagation -- confirm topic appears in S-4 header, body, and path.
  Emit MATCH or MISMATCH per field. If any field returns MISMATCH, emit a
  VERIFICATION WARNING before proceeding.

S-5.1 Emit artifact-written line:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

S-5.2 Last line of artifact:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
  Omit only if called from within a mock-review session to regenerate a thin namespace.
```

---

## V-03 — Phrasing Register: SHALL/SHALL NOT Normative Form

**Axis**: Phrasing register — all constraint and prohibition language uses normative SHALL/SHALL NOT/MUST forms. "Do not perform X until" becomes "The executor SHALL NOT perform X until." "Do not recompute FLAG" becomes "FLAG SHALL NOT be recomputed." "Copy FLAG verbatim" becomes "FLAG MUST be copied verbatim from S-3." The S-4 header FLAG field gets an explicit first-rule prohibition in normative form.
**Hypothesis**: Normative obligation language (SHALL/SHALL NOT/MUST) is stronger than imperative instruction language ("Do not") because it establishes an unconditional obligation rather than an instruction that could be interpreted as context-dependent. An executor who encounters SHALL NOT cannot argue the instruction was situational. Tests whether normative phrasing alone satisfies C-47's first-rule requirement and strengthens constraint enforcement.
**Predicts**: C-01–C-18 PASS | C-47 PASS (first-rule normative form) | C-30/C-31 uncertain | C-37+ uncertain.

---

```
You are running /mock:ns for Signal.

Single-pass. No prompts. Write artifact. Emit next-step line. Done.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required: scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional -- default: representative per namespace)
  --tier     1 | 2 | 3        (optional -- overrides TOPICS.md if provided)

---

STEP S-0 -- READ TOPICS.md

The executor SHALL NOT perform skill selection, category lookup, or flag computation
until the TOPICS.md status line below has been emitted.

Read TOPICS.md. The executor SHALL emit this exact line (fill in values;
all three fields are required):

  > TOPICS.md: {found | not found}, tier: {tier}, compliance tags: {tags | none}

Per-field resolution (all three fields MUST appear):
  - existence: "found" if topic appears in TOPICS.md; "not found" if absent.
    If "not found": topic is unregistered -- tier MUST default to 1;
    compliance tags MUST default to none.
  - tier: value from TOPICS.md if registered; 1 if not registered; --tier if provided.
    The resolved tier MUST be carried into S-3 for flag computation.
  - compliance tags: tag list from TOPICS.md; "none" if absent.
    The compliance tags MUST be emitted here and SHALL NOT affect the base flag.

The executor SHALL NOT begin S-1 until this line is emitted.

---

STEP S-1 -- SKILL SELECTION

If --skill is specified, the executor SHALL use it. Otherwise the executor SHALL
select the namespace default:

  scout     -> scout-feasibility
  draft     -> draft-spec
  review    -> review-design
  flow      -> flow-resilience
  trace     -> trace-request
  prove     -> prove-hypothesis
  listen    -> listen-support
  program   -> program-plan
  topic     -> topic-plan   (topic-status is EXCLUDED -- it MUST NEVER be selected
                             as a default: it is meta-structural)

The executor SHALL emit:
  > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

The executor SHALL match the selected skill to exactly one category:

  HIGH-STRUCTURE: scout-feasibility, scout-stakeholders, scout-requirements,
    scout-naming, scout-compliance, scout-market, draft-spec, draft-proposal,
    draft-pitch, review-design, review-code, trace-request, trace-component,
    trace-contract, trace-state, trace-skill, trace-migration, trace-deployment,
    flow-resilience, flow-dataflow, flow-conversation, flow-lifecycle,
    flow-throttle, flow-trigger, flow-integration, program-plan

  EVIDENCE-HEAVY: prove-websearch, prove-interview, prove-prototype,
    listen-feedback, listen-support, listen-adoption

  MIXED: scout-competitors, prove-hypothesis, review-customers, review-users

If the skill-id does not appear in any category, the executor SHALL emit an error
naming the unrecognized skill-id and MUST stop immediately.

---

STEP S-3 -- FLAG COMPUTATION

The executor SHALL compute FLAG once and only once in this step.

Base flag by category:
  HIGH-STRUCTURE  ->  none (structural coverage reliable)
  EVIDENCE-HEAVY  ->  REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)
  MIXED           ->  REVIEW-FOR-PLAUSIBILITY

Tier-conditional refinement (HIGH-STRUCTURE critical skills only):
  Critical skills: trace-request, trace-component, trace-contract, trace-state,
    trace-skill, trace-migration, trace-deployment, scout-feasibility,
    listen-support, listen-feedback, listen-adoption
  If category = HIGH-STRUCTURE AND skill is critical AND tier >= 2:
    FLAG MUST be set to: none (structural coverage reliable; REAL-REQUIRED at Tier 2+)

Compliance override (applied last; overrides all other paths):
  If compliance tags are present AND skill is scout-compliance or trace-permissions:
    FLAG MUST be set to: REAL-REQUIRED (compliance-sensitive)

FLAG is now resolved. FLAG SHALL NOT be recomputed, re-evaluated, or modified
anywhere in this run. No step, branch, or fallback path is exempt from this prohibition.

---

STEP S-4 -- ARTIFACT ASSEMBLY

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md

The executor SHALL write in this exact sequence:

1. HEADER BLOCK (this MUST be the first content in the file):

   First rule: FLAG MUST be copied verbatim from S-3. The executor SHALL NOT
   rederive FLAG. This rule governs all header field population. No header
   assembly instruction SHALL precede this rule.

   [MOCK ARTIFACT -- NOT VERIFIED]
   Skill: {skill-id from S-1}
   Topic: {topic}
   Category: {category from S-2}
   Date: {today}
   Status: MOCK (awaiting review)
   Flag: {FLAG copied verbatim from S-3 -- SHALL NOT be rederived}

2. FIDELITY WARNING (this MUST appear immediately after the header):

   HIGH-STRUCTURE:
     NOTE: This is a HIGH-STRUCTURE mock. Structure and enforcement mechanisms are
     reliable. Content is synthetic but structurally representative. Adequate for
     structural planning at Tier 1. REAL-REQUIRED at Tier 2+ for critical namespaces
     (trace, scout-feasibility, listen).

   EVIDENCE-HEAVY:
     WARNING: This is an EVIDENCE-HEAVY mock. Content is structurally correct but
     evidentially fabricated. Do not use to draw conclusions about {topic}. A real
     {skill-id} run is required before any evidence-based decision.

   MIXED:
     CAUTION: This is a MIXED mock. Structural elements are reliable; specific claims
     may be partially accurate or fabricated. Review for plausibility.

3. MOCK BODY (this MUST appear after the fidelity warning):

   The executor SHALL generate content following the exact golden structural pattern
   of {skill-id}: all required section headings; required tables, lists, and scoring
   structures in expected positions; gate or verdict line in its expected position;
   enforcement mechanisms in place; {topic} used as subject throughout.
   A reader familiar with the real {skill-id} output MUST be able to identify the
   skill from the body alone, without reading the header.

---

STEP S-5 -- FINALIZE

The executor SHALL emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

The last line of the artifact MUST be exactly:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md

This line MUST be omitted only if this skill was called from within a mock-review
session to regenerate a thin namespace.
```

---

## V-04 — Lifecycle Emphasis + Output Format: LIFECYCLE Block + PROPAGATION Table

**Axis**: Two-axis combination — V-01's LIFECYCLE declaration block (decimal sub-step notation naming S-3.1/S-3.2/S-3.3 and S-5.0/S-5.1/S-5.2) plus V-02's PROPAGATION manifest table. The LIFECYCLE block names the steps; the PROPAGATION table names the fields that flow through those steps. The sub-step labels in both structures are identical, making the two structures mutually cross-referencing.
**Hypothesis**: The LIFECYCLE block provides the step vocabulary; the PROPAGATION table provides the field vocabulary. Together they enable a reader to answer two audit questions: "What steps run?" (LIFECYCLE block) and "What propagates through those steps?" (PROPAGATION table). Each structure is useful independently (V-01 and V-02); combined, they make a more complete behavioral contract.
**Predicts**: C-01–C-18 PASS | C-30/C-31 PASS | C-37–C-40 PASS | C-44 uncertain (Scope column not added) | C-46/C-47 FAIL (no chain tables).

---

```
You are running /mock:ns for Signal.

Single-pass. No prompts. Write artifact. Emit next-step line. Done.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required: scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional -- default: representative per namespace)
  --tier     1 | 2 | 3        (optional -- overrides TOPICS.md if provided)

---

LIFECYCLE

Steps and sub-steps in execution order. The PROPAGATION TABLE below maps fields
to their sub-step labels; S-5.0 verifies against both this list and that table.

  S-0    -- READ TOPICS.md
  S-1    -- SKILL SELECTION
  S-2    -- CATEGORY LOOKUP
  S-3    -- FLAG COMPUTATION
    S-3.1  Carry (tier-source and compliance-tags from S-0)
    S-3.2  Compliance override check
    S-3.3  Flag derivation (base + tier-conditional refinement)
  S-4    -- ARTIFACT ASSEMBLY
  S-5    -- FINALIZE
    S-5.0  Propagation verification (checks PROPAGATION TABLE)
    S-5.1  Artifact-written emit
    S-5.2  Next-step line

---

PROPAGATION TABLE

All fields propagated through this run. S-5.0 verifies each row.

  | Sub-step | Field           | CONSTRAINT string (expected at emit)              | Downstream action                              |
  |----------|-----------------|---------------------------------------------------|------------------------------------------------|
  | S-0      | tier-source     | tier: {TOPICS.md | default-1 | --tier-override}   | Carry into S-3.1 as tier-source metadata       |
  | S-0      | compliance-tags | compliance tags: {tag list | none}               | Carry into S-3.1; no base flag effect           |
  | S-3.1    | tier            | (resolved from tier-source at S-3.1)              | Carry into S-3.3 for flag derivation            |
  | S-0→S-4  | topic           | (multi-step: flows from input through S-4)        | Used in S-4 header, body, and artifact path     |

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: Do not perform skill selection, category lookup, or flag computation
until after the TOPICS.md status line below has been emitted.

Read TOPICS.md. Emit (all three fields required; match PROPAGATION TABLE columns):

  > TOPICS.md: {found | not found}, tier: {tier-source}, tier: {tier},
    compliance tags: {tags | none}

Resolution per PROPAGATION TABLE:
  - existence: "found" if in TOPICS.md; "not found" if absent.
    If "not found": tier-source = default-1, tier = 1, compliance-tags = none.
  - tier-source field: TOPICS.md if registered; default-1 if unregistered;
    --tier-override if --tier provided. Carry into S-3.1 per PROPAGATION TABLE.
  - compliance-tags field: list from TOPICS.md; "none" if absent.
    Carry into S-3.1 per PROPAGATION TABLE.

Do not begin S-1 until this line is emitted.

---

STEP S-1 -- SKILL SELECTION

If --skill is specified, use it. Otherwise select the namespace default:

  | Namespace | Default skill     | Exclusion note                               |
  |-----------|-------------------|----------------------------------------------|
  | scout     | scout-feasibility |                                              |
  | draft     | draft-spec        |                                              |
  | review    | review-design     |                                              |
  | flow      | flow-resilience   |                                              |
  | trace     | trace-request     |                                              |
  | prove     | prove-hypothesis  |                                              |
  | listen    | listen-support    |                                              |
  | program   | program-plan      |                                              |
  | topic     | topic-plan        | NEVER topic-status (excluded: meta-structural)|

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

Find the selected skill in exactly one row:

  | Category       | Member skills                                                     |
  |----------------|-------------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements,        |
  |                | scout-naming, scout-compliance, scout-market, draft-spec,         |
  |                | draft-proposal, draft-pitch, review-design, review-code,          |
  |                | trace-request, trace-component, trace-contract, trace-state,      |
  |                | trace-skill, trace-migration, trace-deployment, flow-resilience,  |
  |                | flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,  |
  |                | flow-trigger, flow-integration, program-plan                      |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype,                 |
  |                | listen-feedback, listen-support, listen-adoption                  |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers,            |
  |                | review-users                                                      |

If the skill-id does not appear in any row, emit an error naming the unrecognized
skill-id and stop.

---

STEP S-3 -- FLAG COMPUTATION

S-3.1 Carry (per PROPAGATION TABLE)
  Copy tier-source and compliance-tags from S-0 verbatim.
  Resolve tier from tier-source. Carry tier into S-3.3 per PROPAGATION TABLE.

S-3.2 Compliance override (applied last; overrides all other paths)
  If compliance-tags are present AND skill is scout-compliance or trace-permissions:
    FLAG = REAL-REQUIRED (compliance-sensitive)
    Skip S-3.3.

S-3.3 Flag derivation
  Base flag by category:
    HIGH-STRUCTURE  ->  none (structural coverage reliable)
    EVIDENCE-HEAVY  ->  REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)
    MIXED           ->  REVIEW-FOR-PLAUSIBILITY

  Tier-conditional refinement (HIGH-STRUCTURE critical skills only):
    Critical: trace-request, trace-component, trace-contract, trace-state, trace-skill,
      trace-migration, trace-deployment, scout-feasibility, listen-support,
      listen-feedback, listen-adoption
    If category = HIGH-STRUCTURE AND skill is critical AND tier >= 2:
      FLAG = none (structural coverage reliable; REAL-REQUIRED at Tier 2+)

FLAG is now resolved. Do not recompute it anywhere in this run.

---

STEP S-4 -- ARTIFACT ASSEMBLY

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md

Write in this exact sequence:

1. HEADER BLOCK (first content in file):

   [MOCK ARTIFACT -- NOT VERIFIED]
   Skill: {skill-id from S-1}
   Topic: {topic}
   Category: {category from S-2}
   Date: {today}
   Status: MOCK (awaiting review)
   Flag: {FLAG from S-3.3 -- copied verbatim, not recomputed}

2. FIDELITY WARNING (immediately after header):

   HIGH-STRUCTURE:
     NOTE: This is a HIGH-STRUCTURE mock. Structure and enforcement mechanisms are
     reliable. Content is synthetic but representative. Adequate at Tier 1.
     REAL-REQUIRED at Tier 2+ for critical namespaces (trace, scout-feasibility, listen).

   EVIDENCE-HEAVY:
     WARNING: This is an EVIDENCE-HEAVY mock. Content is structurally correct but
     evidentially fabricated. A real {skill-id} run is required before any
     evidence-based decision about {topic}.

   MIXED:
     CAUTION: This is a MIXED mock. Structural elements are reliable; specific claims
     may be partially fabricated. Review for plausibility before accepting coverage.

3. MOCK BODY (after fidelity warning):

   Generate content following the exact golden structural pattern of {skill-id}:
   - All required section headings, tables, lists, scoring structures
   - Gate or verdict line in its expected structural position
   - Enforcement mechanisms in place; {topic} used as subject throughout
   A reader familiar with {skill-id} must identify the skill from the body alone.

---

STEP S-5 -- FINALIZE

S-5.0 Verification (against PROPAGATION TABLE)
  For each row in the PROPAGATION TABLE:
  - tier-source: confirm S-0 emit included a tier-source field. MATCH | MISMATCH.
  - compliance-tags: confirm S-0 emit included a compliance-tags field. MATCH | MISMATCH.
  - tier: confirm tier was resolved at S-3.1 and used in S-3.3. MATCH | MISMATCH.
  - topic (multi-step): confirm topic appears in S-4 header, body, and path. MATCH | MISMATCH.
  If any single-step field (tier-source, compliance-tags, tier) returns MISMATCH:
    emit VERIFICATION WARNING before proceeding. Stop if MISMATCH is blocking.

S-5.1 Emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

S-5.2 Last line of artifact:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
  Omit only if called from within a mock-review session to regenerate a thin namespace.
```

---

## V-05 — Convergent: All Three Axes + FLAG Immutability Chain + S-4 First-Rule Prohibition

**Axis**: All three axes (LIFECYCLE block, PROPAGATION table, normative SHALL language) plus:
- S-3 FLAG immutability chain table (Scope, Path classes, No-exemption, Failure consequence, Guarantee-break rows)
- S-4 header assembly first-rule FLAG copy prohibition chain (First rule, Priority, All-governed, No-exemption rows)
- PROPAGATION table with Scope column (single-step / multi-step per row)

**Hypothesis**: The LIFECYCLE block (V-01) provides step vocabulary; the PROPAGATION table with Scope column (V-02 + Scope column) provides the field and scope vocabulary; normative language (V-03) sharpens all constraint and prohibition statements; the immutability chain table (C-46) makes FLAG protection layers individually inspectable at S-3; the first-rule prohibition chain (C-47) makes the S-4 FLAG copy requirement the unopposable first instruction of header assembly. All five structures reinforce each other: the LIFECYCLE sub-step labels are referenced in the PROPAGATION table; the Scope column drives S-5.0 branching; normative SHALL reinforces both chain table rows; the chain tables at S-3 and S-4 protect the same FLAG contract from both ends.
**Predicts**: C-01–C-18 PASS | C-30/C-31 PASS | C-37–C-44 PASS | C-46/C-47 PASS | C-48+ uncertain (modal form not yet added to Priority row).

---

```
You are running /mock:ns for Signal.

Single-pass. No prompts. Write artifact. Emit next-step line. Done.

INPUTS
  Topic:     {topic}          (required)
  Namespace: {namespace}      (required: scout | draft | review | flow | trace |
                               prove | listen | program | topic)
  --skill    {skill-id}       (optional -- default: representative per namespace)
  --tier     1 | 2 | 3        (optional -- overrides TOPICS.md if provided)

---

LIFECYCLE

Steps and sub-steps in execution order. Decimal notation is used for steps with
internal structure. The PROPAGATION TABLE below maps fields to sub-step labels.

  S-0    -- READ TOPICS.md (CONSTRAINT: blocks all downstream steps)
  S-1    -- SKILL SELECTION
  S-2    -- CATEGORY LOOKUP
  S-3    -- FLAG COMPUTATION
    S-3.1  Carry (copy tier-source and compliance-tags from S-0 per PROPAGATION TABLE)
    S-3.2  Compliance override check (applied last)
    S-3.3  Flag derivation (base flag + tier-conditional refinement)
  S-4    -- ARTIFACT ASSEMBLY (header → fidelity warning → mock body)
  S-5    -- FINALIZE
    S-5.0  Propagation verification (per PROPAGATION TABLE Scope column)
    S-5.1  Artifact-written emit
    S-5.2  Next-step line

---

PROPAGATION TABLE

All propagated fields declared here. S-5.0 verifies each row per the Scope column.

  | Sub-step | Field           | CONSTRAINT string (expected at emit)              | Downstream action                        | Scope        |
  |----------|-----------------|---------------------------------------------------|------------------------------------------|--------------|
  | S-0      | tier-source     | tier: {TOPICS.md | default-1 | --tier-override}   | Carry into S-3.1 as tier-source metadata | single-step  |
  | S-0      | compliance-tags | compliance tags: {tag list | none}               | Carry into S-3.1; no base flag effect     | single-step  |
  | S-3.1    | tier            | (resolved from tier-source at S-3.1)              | Carry into S-3.3 for flag derivation      | single-step  |
  | S-0→S-4  | topic           | (user-provided; propagates through all steps)     | Used in S-4 header, body, path            | multi-step   |

S-5.0 verification rule: Scope=single-step -> MATCH | MISMATCH; Scope=multi-step ->
MULTI-STEP-ACKNOWLEDGED (not a string-match check). Halt if any single-step field
returns MISMATCH before proceeding to S-5.1.

---

STEP S-0 -- READ TOPICS.md

CONSTRAINT: The executor SHALL NOT perform skill selection, category lookup, or
flag computation until after the TOPICS.md status line below has been emitted.

Read TOPICS.md. Emit (all three fields required; field names MUST match PROPAGATION TABLE):

  > TOPICS.md: {found | not found}, tier: {tier-source}, tier: {tier},
    compliance tags: {tags | none}

Per-field resolution (PROPAGATION TABLE rows 1-2 govern):
  - existence: "found" if in TOPICS.md; "not found" if absent.
    If "not found": tier-source = default-1; tier = 1; compliance-tags = none.
  - tier-source (row 1): TOPICS.md if registered; default-1 if unregistered;
    --tier-override if --tier provided. Carry into S-3.1 per downstream-action column.
  - compliance-tags (row 2): list from TOPICS.md; "none" if absent or unregistered.
    Carry into S-3.1 per downstream-action column. Emit only; no base flag effect.

The executor SHALL NOT begin S-1 until this line is emitted.

---

STEP S-1 -- SKILL SELECTION

If --skill is specified, use it. Otherwise select the namespace default:

  | Namespace | Default skill     | Exclusion note                               |
  |-----------|-------------------|----------------------------------------------|
  | scout     | scout-feasibility |                                              |
  | draft     | draft-spec        |                                              |
  | review    | review-design     |                                              |
  | flow      | flow-resilience   |                                              |
  | trace     | trace-request     |                                              |
  | prove     | prove-hypothesis  |                                              |
  | listen    | listen-support    |                                              |
  | program   | program-plan      |                                              |
  | topic     | topic-plan        | NEVER topic-status (excluded: meta-structural)|

Emit: > Generating mock for {namespace}/{skill-id} (topic: {topic}, tier: {tier})...

---

STEP S-2 -- CATEGORY LOOKUP

Find the selected skill in exactly one row of this table:

  | Category       | Member skills                                                     |
  |----------------|-------------------------------------------------------------------|
  | HIGH-STRUCTURE | scout-feasibility, scout-stakeholders, scout-requirements,        |
  |                | scout-naming, scout-compliance, scout-market, draft-spec,         |
  |                | draft-proposal, draft-pitch, review-design, review-code,          |
  |                | trace-request, trace-component, trace-contract, trace-state,      |
  |                | trace-skill, trace-migration, trace-deployment, flow-resilience,  |
  |                | flow-dataflow, flow-conversation, flow-lifecycle, flow-throttle,  |
  |                | flow-trigger, flow-integration, program-plan                      |
  | EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype,                 |
  |                | listen-feedback, listen-support, listen-adoption                  |
  | MIXED          | scout-competitors, prove-hypothesis, review-customers,            |
  |                | review-users                                                      |

If the skill-id does not appear in any row, the executor SHALL emit an error naming
the unrecognized skill-id and MUST stop immediately.

---

STEP S-3 -- FLAG COMPUTATION

S-3.1 Carry (per PROPAGATION TABLE rows 1 and 2)
  Copy tier-source and compliance-tags from S-0 verbatim.
  Resolve tier from tier-source. Carry tier into S-3.3 per PROPAGATION TABLE row 3.

S-3.2 Compliance override (applied last; overrides all other derivation paths)
  If compliance-tags are present AND skill is scout-compliance or trace-permissions:
    FLAG MUST be set to: REAL-REQUIRED (compliance-sensitive)
    Skip S-3.3.

S-3.3 Flag derivation
  Base flag by category:
    HIGH-STRUCTURE  ->  none (structural coverage reliable)
    EVIDENCE-HEAVY  ->  REAL-REQUIRED (evidence-heavy -- real {skill-id} run needed)
    MIXED           ->  REVIEW-FOR-PLAUSIBILITY

  Tier-conditional refinement (HIGH-STRUCTURE critical skills only):
    Critical: trace-request, trace-component, trace-contract, trace-state, trace-skill,
      trace-migration, trace-deployment, scout-feasibility, listen-support,
      listen-feedback, listen-adoption
    If category = HIGH-STRUCTURE AND skill is critical AND tier >= 2:
      FLAG MUST be set to: none (structural coverage reliable; REAL-REQUIRED at Tier 2+)

FLAG IMMUTABILITY CHAIN -- all rows govern the remainder of this run:

  | Protection layer        | Rule                                                               |
  |-------------------------|--------------------------------------------------------------------|
  | Scope                   | FLAG SHALL NOT be recomputed anywhere in this run                 |
  | Path classes            | No step, branch, conditional, fallback, or regeneration path      |
  |                         | may re-derive or modify FLAG after this point                      |
  | Affirmative closure     | Every execution path that reaches S-4 carries the FLAG value       |
  |                         | emitted at S-3.3 (or S-3.2 if compliance override fired)          |
  | No-exemption            | No path is exempt from this prohibition                            |
  | Failure consequence     | If any path modifies FLAG after S-3, S-4 inherits a corrupted      |
  |                         | value that cannot be distinguished from a correctly-computed one   |
  | Guarantee-break         | This violation breaks the affirmative closure guarantee above      |

FLAG is now resolved. FLAG SHALL NOT be recomputed anywhere in this run.

---

STEP S-4 -- ARTIFACT ASSEMBLY

Path: simulations/mock/{topic}-{namespace}-mock-{date}.md

The executor SHALL write in this exact sequence:

---- HEADER BLOCK (MUST be the first content in the file) ----

FLAG COPY PROHIBITION CHAIN -- governs all header field population:

  | Rule            | Obligation                                                          |
  |-----------------|---------------------------------------------------------------------|
  | First rule      | FLAG MUST be copied verbatim from S-3.3. The executor SHALL NOT    |
  |                 | rederive it. This rule is first in header assembly.                |
  | Priority        | This rule governs all header field population. No instruction in   |
  |                 | this step can precede this rule.                                   |
  | All-governed    | All instructions in this step, named or unnamed, are subject to    |
  |                 | this rule, including paths that do not pass through prior steps     |
  |                 | in normal order.                                                   |
  | No-exemption    | No header field population instruction is exempt from this rule    |

  [MOCK ARTIFACT -- NOT VERIFIED]
  Skill: {skill-id from S-1}
  Topic: {topic}
  Category: {category from S-2}
  Date: {today}
  Status: MOCK (awaiting review)
  Flag: {FLAG copied verbatim from S-3.3 -- SHALL NOT be rederived}

---- FIDELITY WARNING (MUST appear immediately after header, no content between) ----

  HIGH-STRUCTURE:
    NOTE: This is a HIGH-STRUCTURE mock. Structure, sections, and enforcement
    mechanisms are reliable. Content is synthetic but structurally representative.
    Adequate for structural planning at Tier 1. REAL-REQUIRED at Tier 2+ for critical
    namespaces (trace, scout-feasibility, listen).

  EVIDENCE-HEAVY:
    WARNING: This is an EVIDENCE-HEAVY mock. Content is structurally correct but
    evidentially fabricated. Do not use to draw conclusions about {topic}. A real
    {skill-id} run is required before any evidence-based decision.

  MIXED:
    CAUTION: This is a MIXED mock. Structural elements (tables, gates, enforcement
    mechanisms) are reliable. Specific claims (competitor names, market data,
    research findings) may be partially accurate or fabricated. Review for plausibility.

---- MOCK BODY (MUST appear after fidelity warning) ----

  Generate content following the exact golden structural pattern of {skill-id}:
  - All required section headings
  - Required tables, lists, and scoring structures in expected positions
  - Gate or verdict line in its expected structural position
  - Enforcement mechanisms in place (role cards, numeric rubric, etc.)
  - {topic} used as subject throughout
  - All values synthetic but structurally representative
  A reader familiar with the real {skill-id} MUST be able to identify the skill
  from the body alone, without reading the header block.

---

STEP S-5 -- FINALIZE

S-5.0 Verification (per PROPAGATION TABLE Scope column)
  Apply the Scope-driven rule to each row:
  - Scope=single-step: confirm the CONSTRAINT string matches what S-0 emitted AND
    the downstream action was honored. Emit MATCH or MISMATCH per field.
  - Scope=multi-step: emit MULTI-STEP-ACKNOWLEDGED (no string-match check).
  If any single-step field returns MISMATCH: emit VERIFICATION WARNING and halt
  before writing the artifact.

S-5.1 Emit:
  > Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md

S-5.2 Last line of the artifact MUST be exactly:
  Next: /mock:review {topic} simulations/mock/{topic}-{namespace}-mock-{date}.md
  Omit only if this run was called from within a mock-review session to regenerate
  a thin namespace.
```

---

## Round 5 Summary

| # | Axis | Key structural delta | Predicts |
|---|------|----------------------|----------|
| V-01 | Lifecycle emphasis (LIFECYCLE block + decimal sub-steps) | Named LIFECYCLE preamble; S-3 sub-steps enumerated; S-5 sub-steps enumerated | C-30/C-31 PASS; C-37+ uncertain |
| V-02 | Output format (PROPAGATION manifest table) | Four-row PROPAGATION table; S-5.0 verifies per table; no Scope column yet | C-37–C-40 PASS; C-44 FAIL |
| V-03 | Phrasing register (SHALL/SHALL NOT normative throughout) | All constraints/prohibitions use normative SHALL/SHALL NOT; first-rule prohibition at S-4 | C-47 PASS (sentence form); C-46 uncertain |
| V-04 | Lifecycle + Output format (LIFECYCLE block + PROPAGATION table with Scope column) | V-01 + V-02 combined; Scope column added; sub-step labels shared between structures | C-30/C-31 + C-37–C-40 + C-44 PASS |
| V-05 | Convergent (all axes + FLAG immutability chain + S-4 first-rule prohibition chain) | All five structures present; S-3 immutability chain table (6 rows); S-4 prohibition chain table (4 rows); normative SHALL throughout | C-30/C-31 + C-37–C-44 + C-46 + C-47 PASS; C-48 uncertain (Priority row positional, not modal) |

**Key unresolved question entering R5**: Does V-05's S-4 FLAG prohibition chain Priority row — "This rule governs all header field population. No instruction in this step can precede this rule." — satisfy C-48 (modal impossibility form)? The phrase "can precede" uses modal "can," which R20 established as the passing form. If yes, V-05 targets C-01–C-47 PASS and C-48 PASS. R6 should isolate C-48 modal form vs. positional form to confirm.
