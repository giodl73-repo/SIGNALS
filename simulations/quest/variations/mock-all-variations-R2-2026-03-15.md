Good. I have full context. Writing the 5 variations now.

---

```
skill: quest-variate
skill_target: mock-all
date: 2026-03-15
round: 2
rubric_version: v2
status: VARIATE
```

# mock-all Variate — Round 2

**Date:** 2026-03-15
**Skill:** mock-all
**Rubric:** v2 (C-01 through C-13; essential C-01–C-05)
**Round:** R2 — single-axis pass (V-01 through V-03), then two-axis combinations (V-04, V-05)

---

## Axis-Assignment Plan

New rubric criteria C-11/C-12/C-13 are the primary targets. Single-axis variations isolate
the structural intervention each criterion requires; combinations test whether two fixes can
coexist without interference.

| Plan | Axis | Source signal | Target criteria | Predicted |
|------|------|---------------|-----------------|-----------|
| V-01 | output-format | C-11 failure: classification interleaved per section rather than pre-committed | C-11, C-02 | Pre-classification table forces category lock before artifact body; C-11 always passes |
| V-02 | lifecycle-emphasis | C-12 failure: handoff buried as last paragraph of coverage table | C-12, C-05 | Dedicated HANDOFF phase with explicit label separates handoff from summary; C-12 passes |
| V-03 | phrasing-register | C-13 failure: REAL-REQUIRED applied without rationale | C-13, C-03 | Preamble rule with required rationale string prevents bare flag; C-13 passes |
| V-04 | output-format + lifecycle-emphasis | Combine V-01 pre-classification table with V-02 named phases; C-11 and C-12 structurally guaranteed | C-11, C-12, C-07 | Phase 1 = table, Phase 2 = bodies, Phase 3 = summary, Phase 4 = handoff; all three aspirational criteria pass |
| V-05 | phrasing-register + role-sequence | Evidence-heavy namespaces generated first; rationale preamble from V-03; conversational register | C-13, C-03, C-06 | Evidence-first ordering ensures rationale is written consistently; C-13 + C-06 both pass |

---

## V-01 — Output Format: Pre-Classification Table Before First Artifact Body

**axis:** output-format
**hypothesis:** Generating a nine-row category classification table as the first output block —
before any artifact body is written — satisfies C-11 and prevents the interleaved-classification
failure mode. When classification is interleaved (category decided per section, just before the
body for that section), there is no prior commitment to the full classification, allowing
per-section drift. A pre-committed table locks every namespace's category and flag before the
first artifact body is written; any subsequent deviation from the table is detectable. The table
also surfaces REAL-REQUIRED flags early enough that the compliance-check line (C-08) can reference
them without requiring a second pass. Failure condition: if the model still interleaves
classification within bodies despite the table existing, the table adds overhead without preventing
drift, and C-11 should target a stricter DO-NOT gate instead.

---

You are executing `/mock:all`.

**Inputs**
- `{topic}` — required
- `--tier 1|2|3` — optional; default 1
- `--compliance` — optional; activates compliance pre-flagging

**Setup**

Read `simulations/TOPICS.md` if present. Extract: tier (overridden by `--tier` if provided),
compliance tags. Determine active tier and whether compliance context is active.

Emit one line:
```
> TOPICS.md: {found — topic {topic} tier:{N} compliance:{none|list} | not found — defaults apply}
> Active tier: {N} | Compliance: {active | inactive}
```

**STEP 1 — PRE-CLASSIFICATION TABLE**

Before writing any namespace artifact body, classify all nine namespaces.

Write this table in full. Every row is required. Every row must be complete before Step 2 begins.

| Namespace | Default skill | Category | REAL-REQUIRED? | Flag source |
|-----------|--------------|----------|----------------|-------------|
| scout     | scout-feasibility | HIGH-STRUCTURE | — | — |
| draft     | draft-spec   | HIGH-STRUCTURE | — | — |
| review    | review-design | HIGH-STRUCTURE | — | — |
| flow      | flow-resilience | HIGH-STRUCTURE | — | — |
| trace     | trace-contract | HIGH-STRUCTURE | — at Tier 1; REAL-REQUIRED at Tier 2+ | TIER-CRITICAL if tier >= 2 |
| prove     | prove-hypothesis | EVIDENCE-HEAVY | REAL-REQUIRED | EVIDENCE-HEAVY |
| listen    | listen-support | EVIDENCE-HEAVY | REAL-REQUIRED | EVIDENCE-HEAVY + TIER-CRITICAL |
| program   | program-plan | HIGH-STRUCTURE | — | — |
| topic     | topic-plan   | MIXED | — | — |

Apply these rules to complete the REAL-REQUIRED? and Flag source columns for the active tier
and compliance context:

- **EVIDENCE-HEAVY rule (all tiers):** prove, listen → REAL-REQUIRED; Flag: EVIDENCE-HEAVY
- **TIER-CRITICAL rule (tier >= 2 only):** trace, scout-feasibility subskill context, listen
  → REAL-REQUIRED (or add TIER-CRITICAL to existing REAL-REQUIRED flags)
- **COMPLIANCE rule (compliance context active):** scout-compliance and trace-permissions
  subskill context → REAL-REQUIRED; Flag: COMPLIANCE. Note: at default skills (scout-feasibility,
  trace-contract), flag only if `--compliance` is present or TOPICS.md tags are present.

RATIONALE PREAMBLE (referenced by all REAL-REQUIRED entries in this output):
> A synthetic artifact cannot substitute for real signal where the rubric criterion is
> EVIDENCE-HEAVY (no fabricated data can serve as evidence) or TIER-CRITICAL at the
> active tier (structural mock cannot surface real constraints at commit-gate fidelity).

Do not begin writing namespace artifact bodies until this table is complete and every
REAL-REQUIRED? cell is filled.

**STEP 2 — NAMESPACE ARTIFACT BODIES**

Write all nine namespace sections in this order: scout, draft, review, flow, trace, prove,
listen, program, topic.

Each section must contain:

```
## {Namespace}

[MOCK ARTIFACT]
Skill: {default skill for this namespace}
Topic: {topic}
Category: {category — must match the pre-classification table from Step 1}
Date: {date}
Status: MOCK
```

Followed by a category-appropriate fidelity note:
- HIGH-STRUCTURE: `NOTE: Structure and enforcement mechanisms are synthetic but reliable.
  Content is representative. Adequate for Tier 1 planning.`
- EVIDENCE-HEAVY: `WARNING: Content is structurally correct but evidentially fabricated.
  Real {skill} run required. (See rationale preamble in Step 1.)`
- MIXED: `CAUTION: Tables and gates are reliable. Specific claims may be fabricated.
  Review for plausibility.`

Followed by a plausible synthetic artifact body that uses the section headings and structural
elements specific to the default skill (not generic headings). Minimum 3 substantive lines of
skill-specific content per section.

**STEP 3 — COVERAGE SUMMARY TABLE**

After all nine artifact bodies, write:

```
## Coverage Summary
```

| Namespace | Category | REAL-REQUIRED? | Tier flag | Recommended next step |
|-----------|----------|----------------|-----------|----------------------|
| scout     | ... | ... | ... | ... |
| draft     | ... | ... | ... | ... |
| review    | ... | ... | ... | ... |
| flow      | ... | ... | ... | ... |
| trace     | ... | ... | ... | ... |
| prove     | ... | ... | ... | ... |
| listen    | ... | ... | ... | ... |
| program   | ... | ... | ... | ... |
| topic     | ... | ... | ... | ... |

Tier flag column: mark trace, scout-feasibility, listen as `TIER-2/3-CRITICAL`.
Recommended next step: namespace-specific skill command, e.g. `/prove:hypothesis {topic}`.
REAL-REQUIRED rows should reference the rationale preamble established in Step 1.

**STEP 4 — HANDOFF**

Write a dedicated block labelled:

```
## FINAL LINE
```

Then write exactly:

```
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md
```

Replace `{topic}` and `{date}` with their actual values. Do not leave these as placeholders.
This line must appear in its own section, separate from the coverage table.

Write the complete artifact to `simulations/mock/{topic}-mock-all-{date}.md`.

---

## V-02 — Lifecycle Emphasis: Named Phases with Stop Gates

**axis:** lifecycle-emphasis
**hypothesis:** Structuring mock-all as four explicitly named, numbered phases — CLASSIFY,
GENERATE, SUMMARIZE, HANDOFF — with stop gates between each phase satisfies C-12 by making
the handoff a required Phase 4 with its own section label, rather than a line that gets
absorbed into the coverage table or the last artifact body. The stop-gate mechanism: the model
cannot write the coverage summary until all nine bodies are complete, and cannot write the
handoff until the summary table is complete. Each phase has a defined output; the handoff phase
has exactly one output (the `Next:` line), which prevents it from being collapsed into the
summary. Failure condition: if the model ignores the stop gates and still embeds the handoff
in the summary, the phase scaffold adds structure without enforcing C-12, and a DO-NOT gate
should be added to the HANDOFF phase instruction.

---

You are executing `/mock:all`.

**Inputs:** `{topic}` (required), `--tier 1|2|3` (default 1), `--compliance` (optional).

Read `simulations/TOPICS.md` if present. Extract tier (--tier overrides) and compliance tags.
State: `Active tier: {N} | Compliance: {active|inactive}`

---

### PHASE 1 — CLASSIFY

Determine the category and flag for every namespace before writing any artifact body.

Category rules:
- EVIDENCE-HEAVY: prove (all prove-* skills), listen (all listen-* skills)
- MIXED: topic namespace (topic-plan and topic-story default to MIXED signal; topic-echo
  and topic-report are HIGH-STRUCTURE — use MIXED for the namespace level summary)
- HIGH-STRUCTURE: scout, draft, review, flow, trace, program

Flag rules (apply in order; multiple flags can apply):
1. EVIDENCE-HEAVY namespace → REAL-REQUIRED. Flag: EVIDENCE-HEAVY.
   Rationale: A synthetic artifact cannot substitute for real evidence signal; fabricated
   interview quotes, user feedback, or prototype results cannot inform real decisions.
2. Tier >= 2 AND namespace in {trace, listen, scout (feasibility/competitors context)}
   → REAL-REQUIRED. Flag: TIER-CRITICAL.
   Rationale: At Tier 2+, structural coverage is insufficient; real constraint-surface runs
   are required at these namespaces before a commit-gate decision.
3. Compliance context active AND namespace in {scout-compliance context, trace-permissions
   context} → REAL-REQUIRED. Flag: COMPLIANCE.
   Rationale: Compliance-sensitive artifacts cannot be fabricated; regulatory and permissions
   signals require verified, real runs regardless of structural quality.

Output of Phase 1 — Classification Table:

| Namespace | Category | Flag | REAL-REQUIRED? |
|-----------|----------|------|----------------|
| scout | HIGH-STRUCTURE | {none | TIER-CRITICAL | COMPLIANCE} | {— | REAL-REQUIRED} |
| draft | HIGH-STRUCTURE | none | — |
| review | HIGH-STRUCTURE | none | — |
| flow | HIGH-STRUCTURE | none | — |
| trace | HIGH-STRUCTURE | {none | TIER-CRITICAL | COMPLIANCE} | {— | REAL-REQUIRED} |
| prove | EVIDENCE-HEAVY | EVIDENCE-HEAVY | REAL-REQUIRED |
| listen | EVIDENCE-HEAVY | EVIDENCE-HEAVY {+ TIER-CRITICAL at tier>=2} | REAL-REQUIRED |
| program | HIGH-STRUCTURE | none | — |
| topic | MIXED | none | — |

STOP. Complete and verify the classification table before entering Phase 2.
Every namespace must have a Category and Flag value. No cell may be blank.

---

### PHASE 2 — GENERATE

Write artifact body sections for all nine namespaces in this order:
scout → draft → review → flow → trace → prove → listen → program → topic.

For each namespace, write a section with:

1. Section header: `## {Namespace}`
2. MOCK ARTIFACT block:
   ```
   [MOCK ARTIFACT]
   Skill: {default skill}
   Topic: {topic}
   Category: {from Phase 1 table}
   Date: {date}
   Status: MOCK
   ```
   Default skills: scout=scout-feasibility, draft=draft-spec, review=review-design,
   flow=flow-resilience, trace=trace-contract, prove=prove-hypothesis,
   listen=listen-support, program=program-plan, topic=topic-plan

3. Category fidelity note:
   - HIGH-STRUCTURE: `Structure and mechanisms are representative. Content is synthetic.`
   - EVIDENCE-HEAVY: `WARNING: Evidentially fabricated. Real run required. (Rationale: see Phase 1.)`
   - MIXED: `CAUTION: Gates reliable; specific claims may be fabricated.`

4. Synthetic artifact body: at least 3 substantive lines using the section headings and
   structural elements specific to the default skill. Use skill-specific vocabulary, not
   generic headings. A reader who has run the skill must recognize the structure.

STOP. All nine namespace sections must be complete before entering Phase 3.

---

### PHASE 3 — SUMMARIZE

Write the coverage summary section:

```
## Coverage Summary
```

| Namespace | Category | REAL-REQUIRED? | Tier flag | Recommended next step |
|-----------|----------|----------------|-----------|----------------------|

- Tier flag: mark trace, listen, and scout (when TIER-CRITICAL) as `TIER-2/3-CRITICAL`.
- Recommended next step: a specific, runnable skill command for this topic.
  - For REAL-REQUIRED rows: the real skill command that replaces the mock.
  - For non-REAL-REQUIRED rows: `/mock:review {topic}` or the appropriate follow-on skill.

STOP. The coverage summary must be complete before entering Phase 4.

---

### PHASE 4 — HANDOFF

This phase produces one output: the handoff instruction. It is a required phase, not a
closing note, not a table row, and not embedded in Phase 3.

Write a dedicated section header:

```
## FINAL LINE
```

Then write:

```
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md
```

Use actual values for `{topic}` and `{date}`. Do not leave template placeholders.

Phase 4 is complete when this line is written. There are no other outputs in Phase 4.

---

Write the complete artifact to `simulations/mock/{topic}-mock-all-{date}.md`.
Emit: `> Artifact written: simulations/mock/{topic}-mock-all-{date}.md`

---

## V-03 — Phrasing Register: Strict Imperative with Rationale Gates

**axis:** phrasing-register
**hypothesis:** Strict imperative phrasing — DO NOT, MUST, NEVER — applied at the specific
decision points where C-13 failures occur (applying REAL-REQUIRED without rationale) satisfies
C-13 without requiring a structural overhaul. The mechanism: a preamble rule block that names
the exact required rationale string for each REAL-REQUIRED trigger. When the preamble establishes
the rationale as a mandatory accompaniment to the flag, the model cannot write REAL-REQUIRED
without copying or paraphrasing the preamble rule. This is a narrower fix than V-01 or V-02:
it does not reorder the output structure, it adds DO-NOT language at the specific failure point.
Failure condition: if the model still applies bare REAL-REQUIRED flags despite the preamble,
the preamble approach is insufficient and a structural gate (V-01 or V-02) is needed.

---

Execute `/mock:all`.

INPUTS: `{topic}` (required), `--tier 1|2|3` (default: 1), `--compliance` (optional).

Read `simulations/TOPICS.md` if present. Extract tier (--tier overrides) and compliance tags.
Emit: `Active tier: {N} | Compliance: {active|inactive}`

---

**REAL-REQUIRED RATIONALE RULES (mandatory — read before writing any REAL-REQUIRED flag)**

Every time you write REAL-REQUIRED anywhere in this output, you MUST accompany it with a
one-line rationale. Use the pre-approved rationale strings below. DO NOT write REAL-REQUIRED
without a rationale. DO NOT invent new rationale strings.

```
EVIDENCE-HEAVY rationale:
"A synthetic artifact cannot substitute for real signal — fabricated content has no
evidential value for evidence-heavy namespaces regardless of structural quality."

TIER-CRITICAL rationale:
"At Tier {N}, structural mock coverage is insufficient — critical namespaces require real
constraint-surface runs before a commit-gate decision can be made."

COMPLIANCE rationale:
"Compliance-sensitive artifacts must be verified — regulatory and permissions signals
cannot be fabricated regardless of topic or tier."
```

These rationale strings may appear once in a preamble block (scoped to all REAL-REQUIRED
uses) or per-occurrence. If placed in a preamble, label the block `RATIONALE PREAMBLE` and
reference it wherever REAL-REQUIRED appears: "(see RATIONALE PREAMBLE)".

DO NOT write a coverage summary row, a namespace header block, or a final line with
REAL-REQUIRED unless the applicable rationale is visible somewhere in the output.

---

**PRE-CLASSIFY ALL NINE NAMESPACES**

Before writing any artifact body, write a classification table. This table must appear
before the first namespace artifact section.

| Namespace | Category | REAL-REQUIRED? | Rationale |
|-----------|----------|----------------|-----------|
| scout | HIGH-STRUCTURE | See tier + compliance rules | ... |
| draft | HIGH-STRUCTURE | — | — |
| review | HIGH-STRUCTURE | — | — |
| flow | HIGH-STRUCTURE | — | — |
| trace | HIGH-STRUCTURE | See tier + compliance rules | ... |
| prove | EVIDENCE-HEAVY | REAL-REQUIRED | [EVIDENCE-HEAVY rationale] |
| listen | EVIDENCE-HEAVY | REAL-REQUIRED | [EVIDENCE-HEAVY rationale + TIER-CRITICAL rationale if tier>=2] |
| program | HIGH-STRUCTURE | — | — |
| topic | MIXED | — | — |

FILL the Rationale column with the rationale string(s) from the RATIONALE PREAMBLE above.
DO NOT leave the Rationale column blank for any REAL-REQUIRED row.
DO NOT proceed to artifact bodies until this table is complete.

---

**NAMESPACE ARTIFACT SECTIONS**

Write all nine namespace sections. Order: scout, draft, review, flow, trace, prove, listen,
program, topic.

Each section MUST contain:

1. `## {Namespace}` header
2. MOCK ARTIFACT header block (all five fields: Skill, Topic, Category, Date, Status)
3. Category fidelity note — DO NOT omit:
   - HIGH-STRUCTURE: `NOTE: Structure and enforcement mechanisms are representative. Content is synthetic. Adequate Tier 1 planning.`
   - EVIDENCE-HEAVY: `WARNING: EVIDENCE-HEAVY mock. Evidentially fabricated — real run REQUIRED. [EVIDENCE-HEAVY rationale]`
   - MIXED: `CAUTION: MIXED mock. Gates reliable; specific claims may require real verification.`
4. Synthetic artifact body using skill-specific structure (minimum 3 substantive content lines)

Default skills: scout=scout-feasibility, draft=draft-spec, review=review-design,
flow=flow-resilience, trace=trace-contract, prove=prove-hypothesis, listen=listen-support,
program=program-plan, topic=topic-plan.

NEVER produce a namespace section without a fidelity note. NEVER produce a fidelity note
without an appropriate category warning for EVIDENCE-HEAVY sections.

---

**COVERAGE SUMMARY TABLE**

After all nine artifact bodies, write:

```
## Coverage Summary
```

| Namespace | Category | REAL-REQUIRED? | Tier flag | Recommended next step |
|-----------|----------|----------------|-----------|----------------------|

Tier flag column: MUST mark trace, listen, and applicable scout subskills as `TIER-2/3-CRITICAL`.
DO NOT leave the Tier flag column blank for these namespaces.
REAL-REQUIRED column: MUST reference the rationale string or "(see RATIONALE PREAMBLE)".

Recommended next step: namespace-specific and actionable (a runnable skill command, not a
generic note like "run real skill"). Format: `/{skill} {topic} — {one-line reason}`.

---

**FINAL LINE**

Write this section with its own header, separate from the coverage table:

```
## FINAL LINE
```

Write exactly:

```
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md
```

MUST use actual values for `{topic}` and `{date}`. NEVER leave template placeholders.
This line MUST appear in a dedicated section. DO NOT embed it in the coverage table.

Write the complete artifact to `simulations/mock/{topic}-mock-all-{date}.md`.

---

## V-04 (Combined) — Output Format + Lifecycle Emphasis: Phase Scaffold with Table-First Phase 1

**axes:** output-format + lifecycle-emphasis
**hypothesis:** Combining V-01's mandatory pre-classification table with V-02's four-phase
scaffold guarantees C-11, C-12, and C-13 simultaneously: Phase 1 produces the classification
table before any artifact body (C-11); Phase 4 is a dedicated HANDOFF phase with its own
section header (C-12); the classification table requires a Rationale column for all
REAL-REQUIRED rows (C-13). The risk of combining these two axes is additive prompt length.
The test is whether the model follows a four-phase scaffold with a mandatory table-phase
without taking shortcuts on later phases. Failure condition: if Phase 3 artifacts become
structurally thin because the model front-loaded effort into Phase 1, the combined prompt
trades C-11/C-12 compliance for C-07 failures.

---

You are executing `/mock:all`. Single-pass. No prompts.

**Inputs:** `{topic}` (required), `--tier 1|2|3` (default 1), `--compliance` (optional).

Read `simulations/TOPICS.md` if present. Extract tier and compliance tags. --tier overrides TOPICS.md.
Emit: `Active tier: {N} | Compliance: {active|inactive}`

---

### PHASE 1 — PRE-CLASSIFICATION (write before any artifact body)

The first block written in this output is the classification table.
No artifact body section may appear before this table is complete.

**Classification rules:**

Categories:
- EVIDENCE-HEAVY: prove namespace (all prove-* defaults), listen namespace (all listen-* defaults)
- MIXED: topic namespace
- HIGH-STRUCTURE: scout, draft, review, flow, trace, program

REAL-REQUIRED rules (apply all that match):
- EVIDENCE-HEAVY category → REAL-REQUIRED at all tiers
- Tier >= 2 AND namespace in {trace, listen} → REAL-REQUIRED (additional or sole flag)
- Compliance context active AND namespace in {scout-compliance context, trace-permissions context}
  → REAL-REQUIRED

Rationale strings (write in Rationale column for every REAL-REQUIRED row):
- EVIDENCE-HEAVY: "Synthetic content cannot substitute for real evidence signal."
- TIER-CRITICAL: "At Tier {N}, critical namespaces require real constraint-surface runs."
- COMPLIANCE: "Compliance-sensitive signals must be verified, not fabricated."

Write this table now — complete, all nine rows, Rationale column filled for REAL-REQUIRED rows:

| Namespace | Default skill | Category | REAL-REQUIRED? | Rationale |
|-----------|--------------|----------|----------------|-----------|
| scout | scout-feasibility | HIGH-STRUCTURE | {—|REAL-REQUIRED} | {—|rationale} |
| draft | draft-spec | HIGH-STRUCTURE | — | — |
| review | review-design | HIGH-STRUCTURE | — | — |
| flow | flow-resilience | HIGH-STRUCTURE | — | — |
| trace | trace-contract | HIGH-STRUCTURE | {—|REAL-REQUIRED} | {—|rationale} |
| prove | prove-hypothesis | EVIDENCE-HEAVY | REAL-REQUIRED | [evidence rationale] |
| listen | listen-support | EVIDENCE-HEAVY | REAL-REQUIRED {+TIER-CRITICAL if tier>=2} | [evidence rationale + tier rationale] |
| program | program-plan | HIGH-STRUCTURE | — | — |
| topic | topic-plan | MIXED | — | — |

STOP. This table must be written and complete before Phase 2 begins.

---

### PHASE 2 — GENERATE ARTIFACT BODIES

Write nine namespace sections in order: scout, draft, review, flow, trace, prove, listen, program, topic.

Each section structure:

```
## {Namespace}

[MOCK ARTIFACT]
Skill: {default skill from Phase 1 table}
Topic: {topic}
Category: {from Phase 1 table — must match exactly}
Date: {date}
Status: MOCK
```

Category fidelity note (required after header block):
- HIGH-STRUCTURE: `NOTE: Structure and enforcement mechanisms are synthetic but reliable. Content representative. Adequate for Tier 1 planning.`
- EVIDENCE-HEAVY: `WARNING: Evidentially fabricated. Real run required. (Rationale: see Phase 1.)`
- MIXED: `CAUTION: Gates reliable; specific claims may be fabricated.`

Synthetic body:
- Use section headings specific to the default skill (not generic headings)
- Include all structural elements the skill produces: tables, gates, verdict lines, role cards,
  named outputs, confidence levels, severity labels — whatever the skill normally generates
- Write at least 3 substantive lines of skill-specific synthetic content per section
- Content must be plausible for {topic}, not placeholder text

STOP. All nine sections must be complete before Phase 3 begins.

---

### PHASE 3 — COVERAGE SUMMARY

Write one section:

```
## Coverage Summary
```

| Namespace | Category | REAL-REQUIRED? | Tier flag | Recommended next step |
|-----------|----------|----------------|-----------|----------------------|

- Tier flag: mark trace and listen as `TIER-2/3-CRITICAL`; mark scout as `TIER-2/3-CRITICAL`
  if scout-feasibility or scout-competitors is the active context at tier >= 2
- REAL-REQUIRED column: include rationale reference "(see Phase 1)" for REAL-REQUIRED rows
- Recommended next step: runnable skill command, e.g. `/listen:support {topic}`.
  For non-REAL-REQUIRED rows: `/mock:review {topic}` or appropriate follow-on skill.

STOP. Coverage summary must be complete before Phase 4 begins.

---

### PHASE 4 — HANDOFF

This phase contains one output only. Do not add other content.

```
## FINAL LINE
```

```
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md
```

Substitute actual values for `{topic}` and `{date}`. No placeholders in this line.

---

Write the complete artifact to `simulations/mock/{topic}-mock-all-{date}.md`.
Emit: `> Artifact written: simulations/mock/{topic}-mock-all-{date}.md`

---

## V-05 (Combined) — Phrasing Register + Role Sequence: Evidence-First with Conversational Rationale

**axes:** phrasing-register + role-sequence
**hypothesis:** Generating EVIDENCE-HEAVY namespace bodies first (prove, then listen) before
the seven HIGH-STRUCTURE/MIXED namespaces changes the output sequence so that REAL-REQUIRED
flags and their rationales are written early, when the model is most likely to treat them as
intentional decisions rather than afterthoughts. The conversational register ("here is why this
namespace needs a real run before you can trust it") makes the rationale feel native to each
artifact body, which satisfies C-13 more naturally than an appended rationale field. The
coverage summary at the end re-orders the namespaces back to the canonical sequence so the
table is consistent for readers. Failure condition: if C-07 (plausible body content) degrades
because evidence-first ordering front-loads the hardest namespace to generate structurally,
the sequence benefit for C-13 is purchased at the cost of C-07 quality in the prove and listen
sections.

---

You are running `/mock:all` for topic: `{topic}`.

Read `simulations/TOPICS.md` if present. Note: tier (use `--tier` if provided, else TOPICS.md,
else default 1) and compliance tags if any.

**Before writing anything:** classify all nine namespaces. Write the classification table first.

| Namespace | Category | REAL-REQUIRED? | Why (one line) |
|-----------|----------|----------------|----------------|
| scout | HIGH-STRUCTURE | {varies by tier/compliance} | {structural coverage sufficient at Tier 1; real run at Tier 2+ for feasibility and competitors} |
| draft | HIGH-STRUCTURE | — | Structure is deterministic; synthetic content representative |
| review | HIGH-STRUCTURE | — | Structure is deterministic; synthetic content representative |
| flow | HIGH-STRUCTURE | — | Structure is deterministic; synthetic content representative |
| trace | HIGH-STRUCTURE | {varies by tier/compliance} | {structural at Tier 1; real run at Tier 2+ because constraint-surface matters} |
| prove | EVIDENCE-HEAVY | REAL-REQUIRED | Fabricated evidence has no decision value; real signal only |
| listen | EVIDENCE-HEAVY | REAL-REQUIRED | Fabricated user signals mislead adoption decisions; real data only |
| program | HIGH-STRUCTURE | — | Structure is deterministic; synthetic content representative |
| topic | MIXED | — | Structure reliable; specific story and plan content may need review |

This table must be written before the first artifact body. Fill the Why column for every row —
it does not need to be long, but it cannot be empty.

---

**Artifact bodies — evidence-heavy namespaces first**

Write artifact bodies in this order: **prove → listen → scout → draft → review → flow → trace →
program → topic**. The evidence-heavy namespaces come first because their REAL-REQUIRED status
is the most important signal in this output and should be established with full rationale before
structural namespaces are generated.

For each namespace, write:

```
## {Namespace}
```

Then the MOCK ARTIFACT header block:
```
[MOCK ARTIFACT]
Skill: {default skill}
Topic: {topic}
Category: {HIGH-STRUCTURE | EVIDENCE-HEAVY | MIXED}
Date: {date}
Status: MOCK
```

Default skills:
prove=prove-hypothesis, listen=listen-support, scout=scout-feasibility, draft=draft-spec,
review=review-design, flow=flow-resilience, trace=trace-contract, program=program-plan,
topic=topic-plan.

Then a category fidelity note appropriate to the namespace — write it in a way that makes the
implication clear to a reader who has not read the classification table:

- For EVIDENCE-HEAVY: Explain what you can trust about this artifact (the structure) and
  what you cannot (the content). Be direct: "The sections here are the ones you'd see in a
  real prove run. The content is invented. Don't treat this as evidence for {topic}."
- For HIGH-STRUCTURE: Note that structure and enforcement mechanisms are representative.
  If the namespace is trace or scout at tier >= 2, note the real run requirement.
- For MIXED: Note that tables and gates are reliable but specific claims warrant review.

Then write the synthetic artifact body. Use the section headings and structural elements
specific to the default skill — not generic document structure. Include tables, gate lines,
verdict statements, or role outputs as appropriate for the skill. At least 3 substantive
content lines that demonstrate skill-specific structure.

---

**Coverage summary**

After all nine artifact bodies, write the coverage summary. Present the namespaces in the
canonical order (scout, draft, review, flow, trace, prove, listen, program, topic) — not the
generation order — so the table is consistent for downstream tools.

```
## Coverage Summary
```

| Namespace | Category | REAL-REQUIRED? | Tier flag | Recommended next step |
|-----------|----------|----------------|-----------|----------------------|

- Tier flag: mark trace and listen as `TIER-2/3-CRITICAL`; mark scout if TIER-CRITICAL applies
- Recommended next step: specific and runnable — `/prove:hypothesis {topic}` not "run prove"
- For REAL-REQUIRED rows: include a brief rationale note in the Recommended next step cell

---

**FINAL LINE**

```
## FINAL LINE
```

```
Next: /mock:review {topic} simulations/mock/{topic}-mock-all-{date}.md
```

Replace `{topic}` and `{date}` with actual values. This line belongs in its own section.

Write the complete artifact to `simulations/mock/{topic}-mock-all-{date}.md`.

---

## Variation Map Summary

| V | Axes | What changed | Target criteria | Predicted |
|---|------|--------------|-----------------|-----------|
| V-01 | output-format | Mandatory pre-classification table as Step 1; artifact bodies in Step 2; table must complete before any body written | C-11, C-02 | Pre-classification table fires before first body; C-11 always passes; category lock prevents per-section drift |
| V-02 | lifecycle-emphasis | Four named phases (CLASSIFY, GENERATE, SUMMARIZE, HANDOFF) with explicit STOP gates; HANDOFF is Phase 4 with its own header | C-12, C-05 | Phase 4 structurally isolated; handoff cannot be absorbed into summary table; C-12 passes |
| V-03 | phrasing-register | RATIONALE PREAMBLE block; DO NOT / MUST / NEVER gates; Rationale column required in pre-classification table; REAL-REQUIRED forbidden without rationale | C-13, C-03 | Bare REAL-REQUIRED flag is directly prohibited; rationale string referenced per occurrence; C-13 passes |
| V-04 | output-format + lifecycle-emphasis | Phase 1 = classification table; Phase 2 = nine bodies; Phase 3 = summary; Phase 4 = HANDOFF only; table's Rationale column required for REAL-REQUIRED rows | C-11, C-12, C-13 | All three new aspirational criteria structurally guaranteed; risk is C-07 degradation under additive length |
| V-05 | phrasing-register + role-sequence | Evidence-heavy namespaces generated first (prove→listen); conversational rationale integrated into fidelity note; summary reverts to canonical order | C-13, C-03, C-06 | Evidence-first ordering makes rationale feel native; C-13 satisfied organically; tier-critical flagging (C-06) for listen fires in generation order |

**Top combination candidate for Round 3:**
V-02 (phase scaffold) + V-03 (rationale gates) — if V-02 satisfies C-12 and V-03 satisfies C-13,
combining them produces a prompt where every criterion has a named structural home without
requiring the table-first output reordering of V-01/V-04. Predict: C-11 through C-13 all pass;
C-07 quality depends on whether Phase 2 instructions provide enough per-skill body guidance
independent of the Phase 1 table.
