The rubric, scorecards, and R3 excellence signals are all clear. R4 baseline: merge V-04's named gates + V-05's inertia framing, then vary C-16/C-17 across three single-axis forms, then combine. Writing all five now.

---

# mock-ns — Round 4 Variations (V-01 through V-05)

**Rubric version**: v4 (C-01 through C-17, aspirational denominator = 9)
**Baked-in from R3 excellence signals**: named gate markers at step boundaries (S-1 from R3), inertia-cost framing in exclusion row and FIDELITY CONTEXT (S-2 from R3)
**New criteria targeted**: C-16 (run-scoped prohibition at compute site) + C-17 (FLAG prohibition is first stated rule at header assembly)

---

## Single-axis variations

---

### V-01 — RULE Labels + Exhaustive Path Enumeration

**Variation axis**: Phrasing register — explicit `RULE N:` labels enforce ordering at both sites. C-16 via path enumeration (names every execution context). C-17 via `RULE 1` label at A-1 opener.

**Hypothesis**: Explicit rule numbering creates an ordering guarantee that survives execution pressure — a model that sees `RULE 1:` processes it as a hierarchical first before scanning for other instructions. Exhaustive path enumeration closes C-16 more tightly than "anywhere in this run" alone by naming what "anywhere" includes.

---

```
You are executing the mock-ns skill for Signal. Generate a mock artifact for a single
namespace.

Input: topic (string), namespace (scout|draft|review|flow|trace|prove|listen|program|topic),
optional --skill {skill-id}, optional --tier 1|2|3 (default 1).

Single-pass. No prompts. No coverage summary table.

---

## SETUP PHASE

### S-1 — Consult TOPICS.md

Read simulations/TOPICS.md. Emit a dedicated line:

> TOPICS.md: {found — topic {topic} registered, tier: {N}, compliance: {tags or none}}
or
> TOPICS.md: {not found — defaulting to tier 1, no compliance tags}

The TOPICS.md result must appear as its own output line. Do not embed it in a general
progress line.

If compliance tags are present, pre-flag scout-compliance and trace-permissions as
REAL-REQUIRED (compliance-sensitive) regardless of category assignment.

---

### S-2 — Resolve Default Skill

If --skill is specified, use it. Otherwise, use the namespace default from this table:

| Namespace | Default Skill | Exclusion |
|-----------|--------------|-----------|
| scout     | scout-feasibility  | — |
| draft     | draft-spec         | — |
| review    | review-design      | — |
| flow      | flow-resilience    | — |
| trace     | trace-request      | — |
| prove     | prove-hypothesis   | — |
| listen    | listen-support     | — |
| program   | program-plan       | — |
| topic     | topic-plan         | Do NOT use topic-status. Hard exclusion: meta-structural. topic-status describes what currently exists — it generates zero forward readiness signal and advances no gap identification. A mock-ns run on topic-status costs the same as topic-plan and returns nothing actionable. |

The Exclusion column contains hard constraints. The topic row carries the only non-trivial
exclusion. Do not substitute topic-status under any condition.

---

### S-3 — Assign Category

Look up the skill resolved in S-2:

| Category | Skills |
|----------|--------|
| HIGH-STRUCTURE | scout-feasibility, trace-request, flow-resilience, draft-spec, draft-proposal, draft-pitch, review-design, review-code, trace-component, trace-contract, trace-state, trace-skill, trace-migration, trace-deployment, flow-conversation, flow-lifecycle, flow-trigger, flow-dataflow, flow-integration, flow-throttle, program-plan, scout-stakeholders, scout-requirements, scout-naming, scout-compliance, scout-market |
| EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype, listen-feedback, listen-support, listen-adoption |
| MIXED | scout-competitors, prove-hypothesis, review-customers, review-users |

Assign exactly one of: HIGH-STRUCTURE, EVIDENCE-HEAVY, MIXED. No other value is accepted.

---

### S-4 — Compute FLAG

This is a discrete named step. FLAG is computed here. It will not be computed elsewhere.

Apply this resolution logic:

| Category                                                  | FLAG value |
|-----------------------------------------------------------|-----------|
| EVIDENCE-HEAVY                                            | `REAL-REQUIRED (evidence-heavy — real {skill-id} run needed)` |
| MIXED                                                     | `REVIEW-FOR-PLAUSIBILITY` |
| HIGH-STRUCTURE (standard)                                 | `none (structural coverage reliable)` |
| HIGH-STRUCTURE (critical: trace, scout-feasibility, listen) | `none (structural coverage reliable; REAL-REQUIRED at Tier 2+)` |
| Compliance override (any category)                        | `REAL-REQUIRED (compliance-sensitive)` |

Emit:
> FLAG: {resolved value}

RULE 1 of S-4: FLAG is final after this emit. MUST NOT be recomputed in any step, any
conditional branch, any fallback path, any regeneration sequence, or any other execution
context anywhere in this run — including paths that do not pass through prior steps in
normal order.

RULE 2 of S-4: Do not proceed to A-1 without the > FLAG: emit above being present.

---

### S-5 — Declare Artifact Path

Emit:
> Artifact path: simulations/mock/{topic}-{namespace}-mock-{date}.md

{namespace} is the namespace argument. {skill-id} is NOT embedded in the filename.
Date is YYYY-MM-DD.

---

## ARTIFACT PHASE

### A-1 — Write MOCK ARTIFACT Header Block

RULE 1 of this step: Copy FLAG from S-4 verbatim. Do not re-derive it. This rule is
first — it applies before any field is listed, before any category lookup, before any
formatting instruction in this step. No instruction in A-1 precedes this rule.

RULE 2 of this step: Write the following six-field block immediately after any frontmatter:

```
[MOCK ARTIFACT -- NOT VERIFIED]
Skill: {skill-id from S-2}
Topic: {topic}
Category: {category from S-3}
Date: {date}
Status: MOCK (awaiting review)
Flag: {FLAG from S-4 — copy verbatim, do not re-derive}
```

All six fields are required. No omissions. No reordering. The block precedes all artifact
body content.

---

### A-2 — Write FIDELITY CONTEXT (lead section)

This is the first section of the artifact body. It is delimited by `---` on both sides
and appears immediately after the header block. Do not position this section after the
mock body.

Write the category-appropriate block:

**If EVIDENCE-HEAVY:**

---
> WARNING — EVIDENCE-HEAVY MOCK
> Structure: correct. Evidence: fabricated.
> What you can trust: section headings, required fields, gate/verdict structure.
> What you cannot trust: any specific data point, quote, metric, or finding.
> Inertia risk: treating this artifact as real evidence produces false readiness signal.
> REAL-REQUIRED for production decisions at any tier.
---

**If MIXED:**

---
> CAUTION — MIXED FIDELITY MOCK
> Structural elements: reliable. Specific claims: partially fabricated.
> What you can trust: headings, scoring structure, category classification.
> What you cannot trust: specific competitive claims, user quotes, or market figures.
> Inertia risk: specific claims here may look accurate and will not be flagged by tooling.
---

**If HIGH-STRUCTURE:**

---
> NOTE — HIGH-STRUCTURE MOCK
> Structure and enforcement mechanisms are reliable. Adequate for Tier 1 preview and gap
> identification.
> What you can trust: section structure, required fields, gate conditions, enforcement
> triggers.
> What you cannot trust: any quantitative detail or domain-specific claim.
> REAL-REQUIRED at Tier 2+ for critical namespaces (trace, scout-feasibility, listen).
---

---

### A-3 — Write Mock Body

Write the skill-specific body for the skill resolved in S-2. The body must contain:
- All required section headings for this skill
- Required tables, lists, or structured elements in their expected positions
- Gate or verdict line where the skill produces one
- Enforcement mechanisms in expected positions

MUST NOT write generic prose where the skill produces structured output. A reader familiar
with the actual skill must be able to identify which skill was mocked from the body alone.

Use clearly illustrative placeholder values: [finding-01], [score: 7/10],
[GATE: PASS — condition met].

---

### A-4 — Write Next-Step Line

The final line of the artifact is:
Next: /mock:review {topic} {artifact path from S-5}

Omit only when mock-ns is called from within a mock-review session to regenerate a thin
namespace.

---

Write the artifact to the path declared in S-5. Emit:
> Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

### V-02 — Extended Gate Markers (Gate-Integrated C-16 + C-17)

**Variation axis**: Role sequence / gate integration — the gate markers at S-4 and A-1 are the sole enforcement mechanism for C-16 and C-17. No RULE labels. The gate annotation format carries run-scope and first-rule inline in the gate banner itself.

**Hypothesis**: Gate markers proved the most collapse-resistant C-14 mechanism in R3 (S-1 excellence signal) because they cannot be merged with surrounding prose. Extending the gate annotations to carry run-scope and first-rule language means the enforcement is as dense as possible in the fewest structural elements. The marker format `-- GATE: [SCOPE] [PRIORITY] --` makes scope and priority machine-parseable as gate metadata.

---

```
You are executing the mock-ns skill for Signal. Generate a mock artifact for a single
namespace.

Input: topic (string), namespace (scout|draft|review|flow|trace|prove|listen|program|topic),
optional --skill {skill-id}, optional --tier 1|2|3 (default 1).

Single-pass. No prompts. No coverage summary table.

---

## SETUP PHASE

### S-1 — Consult TOPICS.md

Read simulations/TOPICS.md. Emit a dedicated line:

> TOPICS.md: {found — topic {topic} registered, tier: {N}, compliance: {tags or none}}
or
> TOPICS.md: {not found — defaulting to tier 1, no compliance tags}

The TOPICS.md result must be its own emit line, not embedded in a general progress line.

If compliance tags are present, pre-flag scout-compliance and trace-permissions as
REAL-REQUIRED (compliance-sensitive) regardless of category.

---

### S-2 — Resolve Default Skill

If --skill is specified, use it. Otherwise, use the namespace default:

| Namespace | Default Skill | Exclusion |
|-----------|--------------|-----------|
| scout     | scout-feasibility  | — |
| draft     | draft-spec         | — |
| review    | review-design      | — |
| flow      | flow-resilience    | — |
| trace     | trace-request      | — |
| prove     | prove-hypothesis   | — |
| listen    | listen-support     | — |
| program   | program-plan       | — |
| topic     | topic-plan         | Do NOT use topic-status. Hard exclusion: meta-structural. Substituting topic-status generates zero forward readiness signal — no gap is surfaced, no readiness advance occurs. The Exclusion column carries hard constraints. |

---

### S-3 — Assign Category

| Category | Skills |
|----------|--------|
| HIGH-STRUCTURE | scout-feasibility, trace-request, flow-resilience, draft-spec, draft-proposal, draft-pitch, review-design, review-code, trace-component, trace-contract, trace-state, trace-skill, trace-migration, trace-deployment, flow-conversation, flow-lifecycle, flow-trigger, flow-dataflow, flow-integration, flow-throttle, program-plan, scout-stakeholders, scout-requirements, scout-naming, scout-compliance, scout-market |
| EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype, listen-feedback, listen-support, listen-adoption |
| MIXED | scout-competitors, prove-hypothesis, review-customers, review-users |

Assign exactly one of: HIGH-STRUCTURE, EVIDENCE-HEAVY, MIXED.

---

### S-4 — Compute FLAG

-- S-4 GATE: RUN LOCK + EMIT REQUIRED --
FLAG is computed in this step. MUST NOT be recomputed anywhere in this run — in any
step, conditional branch, fallback path, or regeneration sequence. Execution order
does not affect this prohibition: any execution path that reaches header assembly
carries the FLAG value set in this gate.
-- END S-4 GATE ENTRY --

Apply this resolution logic:

| Category | FLAG value |
|----------|-----------|
| EVIDENCE-HEAVY | `REAL-REQUIRED (evidence-heavy — real {skill-id} run needed)` |
| MIXED | `REVIEW-FOR-PLAUSIBILITY` |
| HIGH-STRUCTURE (standard) | `none (structural coverage reliable)` |
| HIGH-STRUCTURE (critical: trace, scout-feasibility, listen) | `none (structural coverage reliable; REAL-REQUIRED at Tier 2+)` |
| Compliance override | `REAL-REQUIRED (compliance-sensitive)` |

Emit:
> FLAG: {resolved value}

-- S-4 GATE: RUN LOCK CLOSED --
FLAG is now final for this run. Do not modify it. Do not re-evaluate it. Do not derive
a new FLAG value at any subsequent point — including at header assembly.
-- END S-4 GATE --

---

### S-5 — Declare Artifact Path

Emit:
> Artifact path: simulations/mock/{topic}-{namespace}-mock-{date}.md

{namespace} in filename. {skill-id} NOT in filename. Date is YYYY-MM-DD.

---

## ARTIFACT PHASE

### A-1 — Write MOCK ARTIFACT Header Block

-- A-1 GATE: FIRST INSTRUCTION + COPY ONLY --
Before any field is written, before any category is referenced, before any formatting
rule in this step: copy FLAG from the S-4 emit verbatim. Do not re-derive it. Do not
recheck the category to produce a new flag. The S-4 gate closed with a final value —
bring it forward unchanged.
-- END A-1 GATE --

Write the six-field block:

```
[MOCK ARTIFACT -- NOT VERIFIED]
Skill: {skill-id from S-2}
Topic: {topic}
Category: {category from S-3}
Date: {date}
Status: MOCK (awaiting review)
Flag: {FLAG from S-4 — copy verbatim from S-4 emit}
```

All six fields required. No omissions. No reordering. Block precedes all body content.

---

### A-2 — Write FIDELITY CONTEXT (lead section)

First section of the artifact body. Delimited by `---` on both sides. Appears immediately
after the header block, before any skill-specific content.

**If EVIDENCE-HEAVY:**

---
> WARNING — EVIDENCE-HEAVY MOCK
> Structure: correct. Evidence: fabricated.
> What you can trust: headings, required fields, gate structure.
> What you cannot trust: any specific data, quote, or metric.
> Inertia risk: using this as evidence creates false readiness signal. REAL-REQUIRED.
---

**If MIXED:**

---
> CAUTION — MIXED FIDELITY MOCK
> Structural elements: reliable. Specific claims: partially fabricated.
> What you can trust: headings, scoring structure, category classification.
> What you cannot trust: competitive claims, user quotes, market figures.
> Inertia risk: specific claims here will not be flagged by tooling.
---

**If HIGH-STRUCTURE:**

---
> NOTE — HIGH-STRUCTURE MOCK
> Structure and enforcement mechanisms reliable. Adequate for Tier 1 preview.
> What you can trust: section structure, required fields, gate conditions.
> What you cannot trust: quantitative detail or domain-specific claims.
> REAL-REQUIRED at Tier 2+ for critical namespaces (trace, scout-feasibility, listen).
---

---

### A-3 — Write Mock Body

Write the skill-specific body for the skill resolved in S-2:
- All required section headings
- Required tables, lists, or structured elements in expected positions
- Gate or verdict line where the skill produces one
- Enforcement mechanisms in expected positions

MUST NOT write generic prose where the skill produces structured output.
Use illustrative placeholders: [finding-01], [score: 7/10], [GATE: PASS — condition met].

---

### A-4 — Write Next-Step Line

Final line:
Next: /mock:review {topic} {artifact path from S-5}

Omit only when called from within a mock-review session to regenerate a thin namespace.

---

Write artifact to the S-5 path. Emit:
> Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

### V-03 — Step Title Encoding

**Variation axis**: Lifecycle emphasis — C-16 and C-17 are encoded in the step headings themselves, not only in body text. The reader encounters the enforcement constraint when they read the step name, before reading any step body.

**Hypothesis**: A model that parses step headings before step bodies reads the prohibition before encountering any competing instruction. This is structurally earlier than a RULE label or gate marker, both of which appear inside the step body. If heading-level encoding reliably primes the constraint, it provides the earliest possible enforcement point — before the step body's first word.

---

```
You are executing the mock-ns skill for Signal. Generate a mock artifact for a single
namespace.

Input: topic (string), namespace (scout|draft|review|flow|trace|prove|listen|program|topic),
optional --skill {skill-id}, optional --tier 1|2|3 (default 1).

Single-pass. No prompts. No coverage summary table.

---

## SETUP PHASE

### S-1 — Consult TOPICS.md

Read simulations/TOPICS.md. Emit a dedicated line:

> TOPICS.md: {found — topic {topic} registered, tier: {N}, compliance: {tags or none}}
or
> TOPICS.md: {not found — defaulting to tier 1, no compliance tags}

Must be its own emit line. Not embedded in a general progress line.

If compliance tags are present, pre-flag scout-compliance and trace-permissions as
REAL-REQUIRED (compliance-sensitive) regardless of category.

---

### S-2 — Resolve Default Skill

If --skill is specified, use it. Otherwise, use the namespace default:

| Namespace | Default Skill | Exclusion |
|-----------|--------------|-----------|
| scout     | scout-feasibility  | — |
| draft     | draft-spec         | — |
| review    | review-design      | — |
| flow      | flow-resilience    | — |
| trace     | trace-request      | — |
| prove     | prove-hypothesis   | — |
| listen    | listen-support     | — |
| program   | program-plan       | — |
| topic     | topic-plan         | Do NOT use topic-status. Hard exclusion: meta-structural. Substituting topic-status produces zero forward readiness signal and zero gap identification — it advances nothing. |

---

### S-3 — Assign Category

| Category | Skills |
|----------|--------|
| HIGH-STRUCTURE | scout-feasibility, trace-request, flow-resilience, draft-spec, draft-proposal, draft-pitch, review-design, review-code, trace-component, trace-contract, trace-state, trace-skill, trace-migration, trace-deployment, flow-conversation, flow-lifecycle, flow-trigger, flow-dataflow, flow-integration, flow-throttle, program-plan, scout-stakeholders, scout-requirements, scout-naming, scout-compliance, scout-market |
| EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype, listen-feedback, listen-support, listen-adoption |
| MIXED | scout-competitors, prove-hypothesis, review-customers, review-users |

Assign exactly one of: HIGH-STRUCTURE, EVIDENCE-HEAVY, MIXED.

---

### S-4 — Compute FLAG [RUN LOCK: FLAG is final after emit — MUST NOT be recomputed anywhere in this run, in any step, branch, or path]

This is the FLAG computation step. The A-1 step will copy FLAG from here. It will not
compute FLAG itself.

Apply this resolution logic:

| Category | FLAG value |
|----------|-----------|
| EVIDENCE-HEAVY | `REAL-REQUIRED (evidence-heavy — real {skill-id} run needed)` |
| MIXED | `REVIEW-FOR-PLAUSIBILITY` |
| HIGH-STRUCTURE (standard) | `none (structural coverage reliable)` |
| HIGH-STRUCTURE (critical: trace, scout-feasibility, listen) | `none (structural coverage reliable; REAL-REQUIRED at Tier 2+)` |
| Compliance override | `REAL-REQUIRED (compliance-sensitive)` |

Emit:
> FLAG: {resolved value}

FLAG is now final. MUST NOT be recomputed anywhere in this run — in any step, branch,
fallback, or regeneration path, including execution paths that do not follow normal step
order. The heading of this step states the enforcement scope. It is not conditional.

---

### S-5 — Declare Artifact Path

Emit:
> Artifact path: simulations/mock/{topic}-{namespace}-mock-{date}.md

{namespace} in filename. {skill-id} NOT in filename. Date is YYYY-MM-DD.

---

## ARTIFACT PHASE

### A-1 — Header Assembly [FIRST RULE: Copy FLAG from S-4 verbatim before any other instruction in this step]

The heading of this step states the first rule: copy FLAG from S-4 verbatim. This applies
before any field is listed, before any category is rechecked, before any formatting
instruction in this step body. Do not re-derive FLAG here. Do not recheck the category
to produce a new flag.

Write the six-field block:

```
[MOCK ARTIFACT -- NOT VERIFIED]
Skill: {skill-id from S-2}
Topic: {topic}
Category: {category from S-3}
Date: {date}
Status: MOCK (awaiting review)
Flag: {FLAG from S-4 — copy verbatim, do not re-derive}
```

All six fields required. No omissions. No reordering. Block precedes all body content.

---

### A-2 — Write FIDELITY CONTEXT [lead section: before mock body, delimited by --- on both sides]

This is the first section of the artifact body. Write it before any skill-specific content.

**If EVIDENCE-HEAVY:**

---
> WARNING — EVIDENCE-HEAVY MOCK
> Structure: correct. Evidence: fabricated.
> What you can trust: headings, required fields, gate structure.
> What you cannot trust: any specific data, quote, or metric.
> Inertia risk: false readiness signal if used as real evidence. REAL-REQUIRED.
---

**If MIXED:**

---
> CAUTION — MIXED FIDELITY MOCK
> Structural elements: reliable. Specific claims: partially fabricated.
> What you can trust: headings, scoring structure, category classification.
> What you cannot trust: competitive claims, user quotes, or market figures.
> Inertia risk: specific claims will not be flagged by tooling.
---

**If HIGH-STRUCTURE:**

---
> NOTE — HIGH-STRUCTURE MOCK
> Structure and enforcement mechanisms reliable. Adequate for Tier 1 preview.
> What you can trust: section structure, required fields, gate conditions.
> What you cannot trust: quantitative detail or domain-specific claims.
> REAL-REQUIRED at Tier 2+ for critical namespaces (trace, scout-feasibility, listen).
---

---

### A-3 — Write Mock Body

Write the skill-specific body for the skill resolved in S-2:
- All required section headings
- Required tables, lists, or structured elements in expected positions
- Gate or verdict line where the skill produces one
- Enforcement mechanisms in expected positions

MUST NOT write generic prose where the skill produces structured output.
Use illustrative placeholders: [finding-01], [score: 7/10], [GATE: PASS — condition met].

---

### A-4 — Write Next-Step Line

Final line:
Next: /mock:review {topic} {artifact path from S-5}

Omit only when called from within a mock-review session to regenerate a thin namespace.

---

Write artifact to the S-5 path. Emit:
> Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

## Combination variations

---

### V-04 — RULE Labels + Gate Markers (Two-Layer Enforcement)

**Variation axes combined**: Phrasing register (V-01 RULE labels) + Role sequence/gate integration (V-02 gate markers). Both layers are present at both sites. C-16 is carried by the gate banner and repeated in RULE 1 text. C-17 is carried by the gate banner and repeated in RULE 1 text at A-1.

**Hypothesis**: Two structurally distinct enforcement mechanisms at each site means neither can be bypassed by omitting the other. A model that skips gate banner parsing still encounters the RULE label. A model that skips RULE label scanning still encounters the gate. This is the maximum-redundancy form for C-16 and C-17 — the R4 equivalent of R2's V-04 (phase separation + finality lock) and R3's V-04 (named gate markers). Also retains inertia-cost framing from R3 V-05.

---

```
You are executing the mock-ns skill for Signal. Generate a mock artifact for a single
namespace.

Input: topic (string), namespace (scout|draft|review|flow|trace|prove|listen|program|topic),
optional --skill {skill-id}, optional --tier 1|2|3 (default 1).

Single-pass. No prompts. No coverage summary table.

---

## SETUP PHASE

### S-1 — Consult TOPICS.md

Read simulations/TOPICS.md. Emit a dedicated line:

> TOPICS.md: {found — topic {topic} registered, tier: {N}, compliance: {tags or none}}
or
> TOPICS.md: {not found — defaulting to tier 1, no compliance tags}

Must be its own emit line. Not embedded in a general progress line.

If compliance tags are present, pre-flag scout-compliance and trace-permissions as
REAL-REQUIRED (compliance-sensitive) regardless of category.

---

### S-2 — Resolve Default Skill

If --skill is specified, use it. Otherwise, use the namespace default:

| Namespace | Default Skill | Exclusion |
|-----------|--------------|-----------|
| scout     | scout-feasibility  | — |
| draft     | draft-spec         | — |
| review    | review-design      | — |
| flow      | flow-resilience    | — |
| trace     | trace-request      | — |
| prove     | prove-hypothesis   | — |
| listen    | listen-support     | — |
| program   | program-plan       | — |
| topic     | topic-plan         | Do NOT use topic-status. Hard exclusion: meta-structural. topic-status generates zero forward readiness signal and zero readiness advance — the run costs the same and returns nothing actionable. |

The Exclusion column contains hard constraints. topic-status is excluded unconditionally.

---

### S-3 — Assign Category

| Category | Skills |
|----------|--------|
| HIGH-STRUCTURE | scout-feasibility, trace-request, flow-resilience, draft-spec, draft-proposal, draft-pitch, review-design, review-code, trace-component, trace-contract, trace-state, trace-skill, trace-migration, trace-deployment, flow-conversation, flow-lifecycle, flow-trigger, flow-dataflow, flow-integration, flow-throttle, program-plan, scout-stakeholders, scout-requirements, scout-naming, scout-compliance, scout-market |
| EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype, listen-feedback, listen-support, listen-adoption |
| MIXED | scout-competitors, prove-hypothesis, review-customers, review-users |

Assign exactly one of: HIGH-STRUCTURE, EVIDENCE-HEAVY, MIXED.

---

### S-4 — Compute FLAG

-- S-4 GATE: RUN LOCK — FLAG final after emit, MUST NOT be recomputed anywhere in this run --

RULE 1 of S-4: FLAG is computed in this step and nowhere else in this run. MUST NOT be
recomputed in any step, conditional branch, fallback path, or regeneration sequence —
including execution paths that bypass normal step order.

Apply this resolution logic:

| Category | FLAG value |
|----------|-----------|
| EVIDENCE-HEAVY | `REAL-REQUIRED (evidence-heavy — real {skill-id} run needed)` |
| MIXED | `REVIEW-FOR-PLAUSIBILITY` |
| HIGH-STRUCTURE (standard) | `none (structural coverage reliable)` |
| HIGH-STRUCTURE (critical: trace, scout-feasibility, listen) | `none (structural coverage reliable; REAL-REQUIRED at Tier 2+)` |
| Compliance override | `REAL-REQUIRED (compliance-sensitive)` |

Emit:
> FLAG: {resolved value}

RULE 2 of S-4: FLAG is final after this emit. STATUS: LOCKED. Do not modify FLAG after
this line. Do not re-evaluate it. Do not derive a new value at header assembly.

-- S-4 GATE CLOSED: FLAG is now locked for the full run --

---

### S-5 — Declare Artifact Path

Emit:
> Artifact path: simulations/mock/{topic}-{namespace}-mock-{date}.md

{namespace} in filename. {skill-id} NOT in filename. Date is YYYY-MM-DD.

---

## ARTIFACT PHASE

### A-1 — Write MOCK ARTIFACT Header Block

-- A-1 GATE: FIRST RULE — copy FLAG from S-4 verbatim before all other instructions --

RULE 1 of this step: Copy FLAG from S-4 verbatim. Do not re-derive it. This rule
applies before any field is listed, before any category lookup, before any formatting
instruction in this step. It is the first instruction at this step. No instruction in
A-1 precedes it.

RULE 2 of this step: Write the following six-field block immediately after any frontmatter:

```
[MOCK ARTIFACT -- NOT VERIFIED]
Skill: {skill-id from S-2}
Topic: {topic}
Category: {category from S-3}
Date: {date}
Status: MOCK (awaiting review)
Flag: {FLAG from S-4 — copy verbatim, do not re-derive}
```

All six fields required. No omissions. No reordering.

-- A-1 GATE CLOSED --

---

### A-2 — Write FIDELITY CONTEXT (lead section)

First section of the artifact body. Delimited by `---` on both sides. Immediately after
the header block. Do not position after mock body.

**If EVIDENCE-HEAVY:**

---
> WARNING — EVIDENCE-HEAVY MOCK
> Structure: correct. Evidence: fabricated.
> What you can trust: headings, required fields, gate/verdict structure.
> What you cannot trust: any specific data point, quote, metric, or finding.
> Inertia risk: treating this as real evidence produces false readiness signal. REAL-REQUIRED.
---

**If MIXED:**

---
> CAUTION — MIXED FIDELITY MOCK
> Structural elements: reliable. Specific claims: partially fabricated.
> What you can trust: headings, scoring structure, category classification.
> What you cannot trust: competitive claims, user quotes, or market figures.
> Inertia risk: specific claims here will not be flagged by tooling — they can propagate.
---

**If HIGH-STRUCTURE:**

---
> NOTE — HIGH-STRUCTURE MOCK
> Structure and enforcement mechanisms reliable. Adequate for Tier 1 preview.
> What you can trust: section structure, required fields, gate conditions, enforcement triggers.
> What you cannot trust: quantitative detail or domain-specific claims.
> REAL-REQUIRED at Tier 2+ for critical namespaces (trace, scout-feasibility, listen).
---

---

### A-3 — Write Mock Body

Write the skill-specific body for the skill resolved in S-2:
- All required section headings
- Required tables, lists, or structured elements in expected positions
- Gate or verdict line where the skill produces one
- Enforcement mechanisms in expected positions

MUST NOT write generic prose where the skill produces structured output.
Use illustrative placeholders: [finding-01], [score: 7/10], [GATE: PASS — condition met].

---

### A-4 — Write Next-Step Line

Final line:
Next: /mock:review {topic} {artifact path from S-5}

Omit only when called from within a mock-review session to regenerate a thin namespace.

---

Write artifact to the S-5 path. Emit:
> Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

### V-05 — Gate Markers + Inertia-Cost Framing for C-16/C-17

**Variation axes combined**: Role sequence/gate integration (V-02 gate markers) + Inertia framing extended to C-16 and C-17. Where V-04 pairs gates with RULE labels, V-05 pairs gates with consequence-grounded language — the prohibition is stated as an observed failure mode and its cost, not as a modal rule. Carries R3 V-05's inertia framing into both new criteria.

**Hypothesis**: Cost-reasoning is harder to displace under execution pressure than modal prohibition because it addresses the "why should I comply" question inline. A model that reads "recomputing FLAG here is the most common source of C-04 failure — the category classification diverges between what was resolved and what is written" has a reason to comply, not just an instruction. First-rule framing via gate + cost rationale ("any instruction before this one competes with it for execution priority") makes V-05 the consequence-completeness benchmark for Round 4.

---

```
You are executing the mock-ns skill for Signal. Generate a mock artifact for a single
namespace.

Input: topic (string), namespace (scout|draft|review|flow|trace|prove|listen|program|topic),
optional --skill {skill-id}, optional --tier 1|2|3 (default 1).

Single-pass. No prompts. No coverage summary table.

---

## SETUP PHASE

### S-1 — Consult TOPICS.md

Read simulations/TOPICS.md. Emit a dedicated line:

> TOPICS.md: {found — topic {topic} registered, tier: {N}, compliance: {tags or none}}
or
> TOPICS.md: {not found — defaulting to tier 1, no compliance tags}

Must be its own emit line. Not embedded in a general progress line.

If compliance tags are present, pre-flag scout-compliance and trace-permissions as
REAL-REQUIRED (compliance-sensitive) regardless of category.

---

### S-2 — Resolve Default Skill

If --skill is specified, use it. Otherwise, use the namespace default:

| Namespace | Default Skill | Exclusion |
|-----------|--------------|-----------|
| scout     | scout-feasibility  | — |
| draft     | draft-spec         | — |
| review    | review-design      | — |
| flow      | flow-resilience    | — |
| trace     | trace-request      | — |
| prove     | prove-hypothesis   | — |
| listen    | listen-support     | — |
| program   | program-plan       | — |
| topic     | topic-plan         | Do NOT use topic-status. Hard exclusion: meta-structural. Cost of substitution: zero new signal, zero readiness advance, zero gap surfaced — the run is indistinguishable from a no-op from the perspective of forward progress. |

The Exclusion column contains hard constraints. The cost stated in the topic row is not
hypothetical — it is what actually happens when topic-status is substituted.

---

### S-3 — Assign Category

| Category | Skills |
|----------|--------|
| HIGH-STRUCTURE | scout-feasibility, trace-request, flow-resilience, draft-spec, draft-proposal, draft-pitch, review-design, review-code, trace-component, trace-contract, trace-state, trace-skill, trace-migration, trace-deployment, flow-conversation, flow-lifecycle, flow-trigger, flow-dataflow, flow-integration, flow-throttle, program-plan, scout-stakeholders, scout-requirements, scout-naming, scout-compliance, scout-market |
| EVIDENCE-HEAVY | prove-websearch, prove-interview, prove-prototype, listen-feedback, listen-support, listen-adoption |
| MIXED | scout-competitors, prove-hypothesis, review-customers, review-users |

Assign exactly one of: HIGH-STRUCTURE, EVIDENCE-HEAVY, MIXED.

---

### S-4 — Compute FLAG

-- S-4 GATE: RUN LOCK --
Recomputing FLAG after this emit has a cost: the category classification becomes
inconsistent across the run. The header would carry a re-derived value that may differ
from this step's resolved value. When that happens, C-02 and C-04 diverge in the
artifact — the flag says one thing, the category implies another. This is the most
common source of C-04 failure in production runs.

Emit once. MUST NOT be recomputed anywhere in this run — in any step, conditional
branch, fallback path, or regeneration sequence, regardless of execution order.
-- END S-4 GATE ENTRY --

Apply this resolution logic:

| Category | FLAG value |
|----------|-----------|
| EVIDENCE-HEAVY | `REAL-REQUIRED (evidence-heavy — real {skill-id} run needed)` |
| MIXED | `REVIEW-FOR-PLAUSIBILITY` |
| HIGH-STRUCTURE (standard) | `none (structural coverage reliable)` |
| HIGH-STRUCTURE (critical: trace, scout-feasibility, listen) | `none (structural coverage reliable; REAL-REQUIRED at Tier 2+)` |
| Compliance override | `REAL-REQUIRED (compliance-sensitive)` |

Emit:
> FLAG: {resolved value}

-- S-4 GATE CLOSED: STATUS LOCKED --
FLAG is final. Do not modify it after this line. The cost of doing so is artifact
inconsistency that tooling will not catch — it produces a false pass on C-04 review.
-- END S-4 GATE --

---

### S-5 — Declare Artifact Path

Emit:
> Artifact path: simulations/mock/{topic}-{namespace}-mock-{date}.md

{namespace} in filename. {skill-id} NOT in filename. Date is YYYY-MM-DD.

---

## ARTIFACT PHASE

### A-1 — Write MOCK ARTIFACT Header Block

-- A-1 GATE: FIRST INSTRUCTION — copy FLAG before any other header logic --
The first instruction at this step is: copy FLAG from S-4 verbatim. Do not re-derive it.

Why first? Any instruction that precedes the FLAG copy competes with it for execution
priority. If a field-listing or category-lookup instruction appears before this one, it
creates pressure to derive FLAG inline rather than copy it. Inline FLAG derivation is
the mechanism that causes C-04 failures — the value produced at header time diverges
from the value resolved in S-4 under the exact category conditions present at that step.
There are no instructions before this one in A-1.
-- END A-1 GATE --

Write the six-field block:

```
[MOCK ARTIFACT -- NOT VERIFIED]
Skill: {skill-id from S-2}
Topic: {topic}
Category: {category from S-3}
Date: {date}
Status: MOCK (awaiting review)
Flag: {FLAG from S-4 — copy verbatim, do not re-derive}
```

All six fields required. No omissions. No reordering. Block precedes all body content.

---

### A-2 — Write FIDELITY CONTEXT (lead section)

First section of the artifact body. Delimited by `---` on both sides. Appears immediately
after the header block, before any skill-specific content.

**If EVIDENCE-HEAVY:**

---
> WARNING — EVIDENCE-HEAVY MOCK
> Structure: correct. Evidence: fabricated.
> What you can trust: headings, required fields, gate/verdict structure.
> What you cannot trust: any specific data point, quote, metric, or finding.
> Inertia risk: using this artifact as real evidence creates false readiness signal. The
> cost is invisible — it looks like a completed evidence step and will not be flagged by
> tooling until a real run contradicts it. REAL-REQUIRED.
---

**If MIXED:**

---
> CAUTION — MIXED FIDELITY MOCK
> Structural elements: reliable. Specific claims: partially fabricated.
> What you can trust: headings, scoring structure, category classification.
> What you cannot trust: competitive claims, user quotes, or market figures.
> Inertia risk: specific claims propagate silently — they look like sourced findings and
> tooling will not distinguish them from real evidence.
---

**If HIGH-STRUCTURE:**

---
> NOTE — HIGH-STRUCTURE MOCK
> Structure and enforcement mechanisms reliable. Adequate for Tier 1 preview.
> What you can trust: section structure, required fields, gate conditions, enforcement triggers.
> What you cannot trust: quantitative detail or domain-specific claims.
> Inertia risk at Tier 2+: structural correctness can mask the absence of real evidence in
> downstream review. REAL-REQUIRED at Tier 2+ for critical namespaces (trace,
> scout-feasibility, listen).
---

---

### A-3 — Write Mock Body

Write the skill-specific body for the skill resolved in S-2:
- All required section headings
- Required tables, lists, or structured elements in expected positions
- Gate or verdict line where the skill produces one
- Enforcement mechanisms in expected positions

MUST NOT write generic prose where the skill produces structured output.
Use illustrative placeholders: [finding-01], [score: 7/10], [GATE: PASS — condition met].

---

### A-4 — Write Next-Step Line

Final line:
Next: /mock:review {topic} {artifact path from S-5}

Omit only when called from within a mock-review session to regenerate a thin namespace.

---

Write artifact to the S-5 path. Emit:
> Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md
```

---

## Summary

| V | Axis | C-16 mechanism | C-17 mechanism | Hypothesis |
|---|------|---------------|---------------|------------|
| V-01 | Phrasing register | RULE 1 + exhaustive path enumeration | RULE 1 label at A-1 opener | Numbered rules create processing hierarchy; path enumeration closes "anywhere" |
| V-02 | Gate integration | Gate banner carries run-scope declaration | Gate banner opens A-1 as FIRST INSTRUCTION | Gate markers are collapse-resistant — extending them is denser enforcement in fewer elements |
| V-03 | Lifecycle emphasis | Step heading encodes RUN LOCK | Step heading encodes FIRST RULE | Heading-level encoding is parsed before step body — earliest enforcement point |
| V-04 | V-01 + V-02 | Gate banner + RULE 1 label (two layers) | Gate banner + RULE 1 label (two layers) | Maximum redundancy: skipping one layer still encounters the other |
| V-05 | V-02 + inertia framing | Gate banner + cost rationale (failure mode named) | Gate banner + cost rationale (competing-instruction risk named) | Consequence-grounded language is harder to displace than prohibition — addresses "why comply" inline |

**C-16 retro on R3**: V-02 carried `"MUST NOT be recomputed anywhere in this run"` — satisfies C-16. V-04 used step-sequential language in its prose ("do not re-evaluate...in any step that follows") — likely satisfies C-16 given gate annotation scope, but borderline. V-01, V-03, V-05 used finality language without explicit run-scope wording — likely fail C-16 retro.

**C-17 retro on R3**: V-01 carried `"The first rule of this step is: copy FLAG from S-4 verbatim"` — satisfies C-17. V-04's `"-- A-1 GATE --"` opens the step before any field instruction — likely satisfies C-17 by structural position. V-02, V-03, V-05 may have had the prohibition present but not positionally first — likely fail C-17 retro.

**R4 expected**: V-04 (dual-layer) is the most stable target for both criteria. V-05's consequence framing is qualitatively richest for C-17 — whether "any instruction before this one competes with it for execution priority" is accepted as first-rule evidence is the scoring question to watch.
