---

## mock-all Variate — Round 1

**Skill:** mock-all | **Rubric:** v1 | **Round:** R1

---

## Variation Map

| V | Axis | What Changed | Hypothesis |
|---|------|--------------|------------|
| V-01 | role-sequence | Coverage Analyst role declared before namespace loop | Priming the model with the Coverage Analyst identity before generation improves C-02 (category classification) and C-03 (REAL-REQUIRED auto-application) because the classification mindset is set before artifact writing begins |
| V-02 | output-format | Per-namespace Coverage Verdict block + compact final table | Making the per-section artifact body a structural requirement (not a prose afterthought) improves C-07 (substantive bodies) and C-10 (actionable next steps) because each section contains its own NEXT field |
| V-03 | lifecycle-emphasis | Classification taxonomy and flag rules front-loaded before generation loop | Rules in active context when each section is written improves C-03 (REAL-REQUIRED) and C-06 (tier annotation) over inline reminders buried after the loop |
| V-04 | phrasing-register + lifecycle-emphasis | Fully imperative DO/DO NOT register with front-loaded rules | Hard prohibitions target C-01 (complete headers), C-02 (correct categories), C-03 (flags), C-08 (compliance) simultaneously |
| V-05 | inertia-framing + output-format | Gap-first framing with risk-ordered summary table | Orienting toward "what must not stay synthetic" improves C-06, C-08, C-10 by directing attention to risk before completion |

---

## V-01 — Role Sequence: Coverage Analyst First

**axis:** role-sequence
**hypothesis:** Priming the operator as Coverage Analyst before the namespace loop will improve C-02 (correct category labels) and C-03 (REAL-REQUIRED auto-application). Falsifiable: if C-02 and C-03 do not improve over baseline, the role declaration adds no value.

```
You are running `/mock:all {topic}`.

ROLE: COVERAGE ANALYST

You are the Coverage Analyst for Signal. Your job is to generate a synthetic signal artifact
for every namespace in a single pass, then produce a unified coverage picture. You classify
first and generate second — never the reverse.

---

STEP 1 — CLASSIFY ALL NAMESPACES

Before writing any artifact, assign every namespace its category and flag status:

| Namespace | Category        | Auto-flag     |
|-----------|-----------------|---------------|
| scout     | HIGH-STRUCTURE  | —             |
| draft     | HIGH-STRUCTURE  | —             |
| review    | HIGH-STRUCTURE  | —             |
| flow      | HIGH-STRUCTURE  | —             |
| trace     | HIGH-STRUCTURE  | —             |
| prove     | EVIDENCE-HEAVY  | REAL-REQUIRED |
| listen    | EVIDENCE-HEAVY  | REAL-REQUIRED |
| program   | MIXED           | —             |
| topic     | MIXED           | —             |

EVIDENCE-HEAVY namespaces (prove, listen) are auto-flagged REAL-REQUIRED regardless of
artifact quality. A synthetic artifact cannot substitute for real signal in these namespaces.

---

STEP 2 — GENERATE ARTIFACT SECTIONS

For each of the 9 namespaces, write one section:

  ## {Namespace}

  <!-- MOCK ARTIFACT -->
  Skill: {namespace}-{primary-skill}
  Topic: {topic}
  Category: {category-from-classification}
  Date: {date}
  Status: MOCK
  Flag: REAL-REQUIRED   ← include only if flag applies; omit line otherwise

  {synthetic-artifact-body — 3 or more substantive lines representing realistic signal
  content for this namespace. Not generic filler. Show what a real artifact would say
  about {topic} for this namespace's signal type.}

Write all 9 namespace sections before proceeding to Step 3.

---

STEP 3 — COVERAGE SUMMARY TABLE

Produce a Markdown table with exactly these 4 columns and 9 data rows:

| Namespace | Category | Flag | Recommended next step |
|-----------|----------|------|-----------------------|

Flag column rules:
- REAL-REQUIRED — any EVIDENCE-HEAVY namespace
- REAL-REQUIRED — scout-compliance and trace-permissions if topic has compliance tags
  (check TOPICS.md; if absent, apply conservatively)
- TIER-2-CRITICAL — trace namespace row
- TIER-3-CRITICAL — scout-feasibility and listen namespace rows
- Multiple flags: join with " | "
- — if no flag applies

Recommended next step column:
- Name a specific Signal skill invocation: e.g., `/scout:feasibility {topic}`
- Never write "gather more data" or "run the skill"

---

STEP 4 — TIER FLAG (--tier support)

--tier 2: output only sections for trace, prove, listen.
--tier 3: output only sections for prove and listen.
Default (--tier 1 or no flag): output all 9 namespace sections.

---

FINAL LINE

The last line of your output must be exactly:

  Next: /mock:review {topic} {this-file}

where {topic} is the topic name you received and {this-file} is the artifact filename
produced in this run (not a placeholder).
```

---

## V-02 — Output Format: Per-Section Verdict Block

**axis:** output-format
**hypothesis:** A Coverage Verdict block inside each section (requiring 3+ artifact lines + explicit FLAG + per-section NEXT field) will improve C-07 (substantive bodies) and C-10 (actionable next steps). Falsifiable: if C-07 and C-10 do not exceed V-01, the in-section structure adds no marginal value.

```
You are running `/mock:all {topic}`.

Generate a synthetic signal artifact for every namespace. For each namespace, write a
section containing three parts: (1) MOCK ARTIFACT header, (2) synthetic artifact body,
(3) Coverage Verdict block. Then produce a summary table and the handoff line.

---

NAMESPACE SECTIONS

Write exactly 9 sections in this order:
  scout, draft, review, flow, trace, prove, listen, program, topic.

Each section follows this structure:

  ## {Namespace}

  <!-- MOCK ARTIFACT -->
  Skill: {namespace}-{primary-skill}
  Topic: {topic}
  Category: {CATEGORY}
  Date: {date}
  Status: MOCK

  {ARTIFACT-BODY}

  <!-- COVERAGE VERDICT -->
  Flag: {FLAG}
  Confidence: SYNTHETIC
  Next: /{namespace}:{primary-skill} {topic}

CATEGORY assignment rules:
  prove and listen  → EVIDENCE-HEAVY
  scout, draft, review, flow, trace → HIGH-STRUCTURE
  program, topic → MIXED

FLAG assignment rules:
  EVIDENCE-HEAVY  → REAL-REQUIRED (mandatory — cannot be omitted)
  HIGH-STRUCTURE / MIXED → REVIEW-RECOMMENDED by default, except:
    trace namespace       → TIER-2-CRITICAL
    scout (feasibility)   → TIER-3-CRITICAL
    listen namespace      → TIER-3-CRITICAL
    compliance-tagged topics: scout-compliance, trace-permissions → REAL-REQUIRED
  Multiple flags: join with " | "

ARTIFACT-BODY rules:
  Write a minimum 3 substantive lines per section.
  Content must reflect what a real {namespace} artifact would plausibly contain for {topic}.
  Not headers. Not category labels. Not the topic name repeated.

---

COVERAGE SUMMARY TABLE

After all 9 sections:

| Namespace | Category | Flag | Recommended next step |
|-----------|----------|------|-----------------------|

9 rows. Exactly 4 columns.
Flag and Recommended next step values must match the Coverage Verdict blocks above.
No new values may appear in the table that were not declared per-section.

---

TIER FLAG

--tier 1 (default): all 9 sections and rows.
--tier 2: sections and rows for trace, prove, listen only.
--tier 3: sections and rows for prove and listen only.

---

FINAL LINE

  Next: /mock:review {topic} {this-file}

Replace {topic} and {this-file} with actual values. No placeholder tokens in output.
```

---

## V-03 — Lifecycle Emphasis: Classification Rules First

**axis:** lifecycle-emphasis
**hypothesis:** Front-loading the complete taxonomy and flag rules before the generation loop will improve C-03 (REAL-REQUIRED flag) and C-06 (tier annotation) because both are established in active context before any section is written — not discovered as footnotes mid-generation. Falsifiable: if C-03 and C-06 pass rates equal V-01, front-loading adds nothing.

```
You are running `/mock:all {topic}`.

---

CLASSIFICATION TAXONOMY — READ BEFORE WRITING ANY SECTION

  HIGH-STRUCTURE: scout, draft, review, flow, trace
    Structured artifacts (tables, scores, decision trees). Synthetic artifacts are
    plausible coverage proxies for decision support.

  EVIDENCE-HEAVY: prove, listen
    Artifacts whose value depends on real data — interviews, prototypes, usage metrics.
    SYNTHETIC ARTIFACTS CANNOT SUBSTITUTE FOR REAL SIGNAL HERE.
    Rule: every EVIDENCE-HEAVY section MUST carry Flag: REAL-REQUIRED. Unconditional.

  MIXED: program, topic
    Combination of structure and interpretation. Synthetic is a partial proxy.

---

FLAG RULES — READ BEFORE WRITING ANY SECTION

  REAL-REQUIRED
    Apply to: every EVIDENCE-HEAVY namespace (prove, listen) — no exception.
    Apply to: scout-compliance and trace-permissions if topic has compliance tags.
    Meaning: a real artifact is required before this signal can inform a decision.

  TIER-2-CRITICAL
    Apply to: trace namespace row in the summary table.
    Meaning: trace is a tier-2 foundational signal; synthetic understates risk.

  TIER-3-CRITICAL
    Apply to: scout-feasibility and listen namespace rows in the summary table.
    Meaning: tier-3 foundational signals — gaps here block downstream work.

  Multiple flags on one row: join with " | "

---

MOCK ARTIFACT HEADER FORMAT

Every section opens with:

  <!-- MOCK ARTIFACT -->
  Skill: {namespace}-{primary-skill}
  Topic: {topic}
  Category: {category}
  Date: {date}
  Status: MOCK
  Flag: {flag}       ← omit this line only if no flag applies

---

GENERATE 9 SECTIONS

Write one section per namespace in this order:
  scout, draft, review, flow, trace, prove, listen, program, topic.

Format:

  ## {Namespace}

  [Required header block]

  [Artifact body: 3 or more substantive lines. Write what a real {namespace} artifact
  would plausibly contain for {topic}. The body demonstrates the namespace's signal type —
  competitive signals, compliance constraints, flow stages, interview findings, etc.]

Write all 9 sections before the summary table.

---

COVERAGE SUMMARY TABLE

Immediately after the 9 sections:

| Namespace | Category | Flag | Recommended next step |
|-----------|----------|------|-----------------------|

  Flag column: use values assigned per FLAG RULES above.
  Recommended next step: name the specific Signal skill to run next.
    Format: /{namespace}:{skill} {topic}
    Not "run trace" or "gather evidence" — a concrete invocation.

9 rows. Exactly 4 columns.

---

TIER FLAG

--tier 1 (default): all 9 sections and rows.
--tier 2: sections and rows for trace, prove, listen only.
--tier 3: sections and rows for prove and listen only.

---

FINAL LINE

The last line of your output:

  Next: /mock:review {topic} {this-file}

{topic} = topic name supplied at invocation.
{this-file} = artifact filename written in this run.
No literal placeholder text in the output.
```

---

## V-04 — Phrasing Register + Lifecycle Emphasis: Imperative DO/DO NOT + Rules First

**axis:** phrasing-register + lifecycle-emphasis
**hypothesis:** Fully imperative DO/DO NOT register combined with front-loaded classification rules will improve C-01 (complete headers), C-02 (correct categories), C-03 (REAL-REQUIRED), and C-08 (compliance pre-flagging) simultaneously — hard stops prevent omissions that procedural phrasing leaves ambiguous. Falsifiable: if essential pass rate does not exceed V-03, imperative register adds nothing over lifecycle-emphasis alone.

```
You are running `/mock:all {topic}`.

---

CLASSIFICATION RULES — READ THESE BEFORE WRITING ANYTHING

DO classify scout, draft, review, flow, trace as HIGH-STRUCTURE.
DO classify prove, listen as EVIDENCE-HEAVY.
DO classify program, topic as MIXED.
DO NOT invent a fourth category.
DO NOT assign HIGH-STRUCTURE to prove or listen for any reason.

DO apply Flag: REAL-REQUIRED to every EVIDENCE-HEAVY section.
DO NOT omit REAL-REQUIRED from any prove or listen section.
DO NOT write a prove or listen section without a REAL-REQUIRED flag.

DO apply Flag: REAL-REQUIRED to scout-compliance and trace-permissions if the topic has
compliance tags. Check TOPICS.md; if absent, apply REAL-REQUIRED conservatively.
DO NOT assume a topic lacks compliance tags without checking.

---

REQUIRED HEADER FORMAT

Every namespace section MUST open with:

  <!-- MOCK ARTIFACT -->
  Skill: {namespace}-{primary-skill}
  Topic: {topic}
  Category: {category}
  Date: {date}
  Status: MOCK

If a flag applies, add immediately after Status: MOCK:
  Flag: {flag}

DO NOT omit any field.
DO NOT write the artifact body before the header block.
DO NOT use a different header format.

---

GENERATE THE 9 SECTIONS

Write sections in this order: scout, draft, review, flow, trace, prove, listen, program, topic.

Format:

  ## {Namespace}
  [Required header block]
  [Artifact body]

DO write a minimum 3 substantive lines per artifact body.
DO write content that reflects realistic {namespace} signal for {topic}.
DO NOT write header-only sections.
DO NOT use placeholder text in the body.
DO NOT proceed to the summary table until all 9 sections are complete.

---

TIER FLAG BEHAVIOR

DO produce all 9 sections when invoked without --tier.
DO produce only trace, prove, listen sections when invoked with --tier 2.
DO produce only prove and listen sections when invoked with --tier 3.
DO NOT produce sections outside the tier scope.

---

COVERAGE SUMMARY TABLE

After the 9 sections, write exactly:

| Namespace | Category | Flag | Recommended next step |
|-----------|----------|------|-----------------------|

DO include exactly 9 data rows.
DO NOT add, rename, or reorder columns.
DO annotate the trace row as TIER-2-CRITICAL in the Flag column.
DO annotate the scout-feasibility row and listen row as TIER-3-CRITICAL.
DO NOT omit tier annotations from trace, scout-feasibility, or listen rows.
DO write a concrete skill invocation in Recommended next step for every row.
DO NOT write generic advice in the Recommended next step column.

---

FINAL LINE

DO end your output with exactly:

  Next: /mock:review {topic} {this-file}

DO NOT end with any other line.
DO NOT emit literal placeholder tokens.
```

---

## V-05 — Inertia Framing + Output Format: Gap-First Coverage Report

**axis:** inertia-framing + output-format
**hypothesis:** Framing the output as a gap report (primary purpose: surface what must not remain synthetic) rather than an artifact catalog (primary purpose: show what was generated) will improve C-06 (tier annotations), C-08 (compliance flags), C-10 (actionable next steps) because the risk-identification frame drives specificity. A risk-ordered summary table (REAL-REQUIRED rows first) makes gaps structurally primary. Falsifiable: if C-06, C-08, C-10 do not improve over V-03, inertia framing adds nothing.

```
You are running `/mock:all {topic}`.

PURPOSE: gap detection, not coverage theater.

This skill produces a coverage gap report. You will generate synthetic mock artifacts for
all 9 namespaces so the team sees the full evidence shape at a glance. The primary
deliverable is the answer to: "Where does this topic have dangerous mock coverage that
must not stay synthetic before a real decision is made?"

Default assumption: no evidence is better than fake evidence. REAL-REQUIRED flags exist
because acting on a synthetic artifact is worse than knowing you lack the signal.

---

STEP 1 — GENERATE NAMESPACE SECTIONS

Write one section per namespace: scout, draft, review, flow, trace, prove, listen, program, topic.

Section format:

  ## {Namespace}

  <!-- MOCK ARTIFACT -->
  Skill: {namespace}-{primary-skill}
  Topic: {topic}
  Category: {category}
  Date: {date}
  Status: MOCK
  {flag-line-if-applicable}

  {artifact-body}

Category and flag rules:

  prove, listen → Category: EVIDENCE-HEAVY | Flag: REAL-REQUIRED
    These namespaces require real interviews, prototypes, or usage data.
    A synthetic artifact proves nothing. Do not let MOCK coverage here
    substitute for the absence of a real signal.

  scout, draft, review, flow, trace → Category: HIGH-STRUCTURE
    No default flag, except:
    - compliance-tagged topics: scout-compliance and trace-permissions → REAL-REQUIRED
    - trace namespace: note TIER-2-CRITICAL in the gap report
    - scout-feasibility and listen: note TIER-3-CRITICAL in the gap report

  program, topic → Category: MIXED | no default flag

Artifact body: 3 or more substantive lines per section. Show what the real artifact would
plausibly contain for {topic} — competitive signals, technical constraints, user feedback
patterns, migration risks, adoption blockers, etc. Structurally realistic, not filler.

---

STEP 2 — COVERAGE GAP REPORT

Produce a table ordered by risk: what must not stay synthetic appears first.

Ordering:
  1. REAL-REQUIRED rows first (prove, listen always; compliance rows if applicable)
  2. TIER-CRITICAL rows second (trace, scout-feasibility)
  3. Remaining rows last

Table — exactly these 4 columns:

| Namespace | Category | Flag | Recommended next step |
|-----------|----------|------|-----------------------|

Flag column values (apply all that fit, join with " | "):
  REAL-REQUIRED — evidence-heavy or compliance-tagged namespaces
  TIER-2-CRITICAL — trace namespace
  TIER-3-CRITICAL — scout-feasibility, listen namespaces
  — if no flag applies

Recommended next step column:
  Name the specific Signal skill that converts this MOCK to REAL.
  Format: /{namespace}:{skill} {topic}
  Examples: `/prove:prototype {topic}`, `/listen:adoption {topic}`, `/trace:contract {topic}`
  DO NOT write "gather more evidence", "run the skill", or any non-specific guidance.

9 rows. Exactly 4 columns. Risk-ordered.

---

STEP 3 — TIER FLAG (--tier support)

--tier 1 (default): all 9 sections and 9 summary rows.
--tier 2: sections and rows for trace, prove, listen only.
--tier 3: sections and rows for prove and listen only.
Omit sections and rows outside scope entirely.

---

FINAL LINE

End with:

  Next: /mock:review {topic} {this-file}

{topic} = topic name from invocation (no placeholder text).
{this-file} = filename of the artifact produced in this run (no placeholder text).
This line must be the last line of your output.
```

---

Written to `simulations/quest/golden/quest-rubric-variate-v1-R01-2026-03-15.md`.

**Top combination candidate for Round 2:** V-03 × V-05 — front-loaded classification rules (lifecycle-emphasis) with gap-first framing and risk-ordered table (inertia-framing + output-format). V-03 targets the structural completeness criteria (C-03, C-06); V-05 targets the specificity criteria (C-08, C-10). Neither axis interferes with the other, and the combination should produce the highest essential + aspirational composite.
