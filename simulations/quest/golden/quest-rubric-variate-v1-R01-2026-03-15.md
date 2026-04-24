---
skill: quest-variate
skill_target: mock-all
date: 2026-03-15
round: R1
rubric_version: v1
status: variate
---

# mock-all Variate — Round 1

**Date:** 2026-03-15
**Skill:** mock-all
**Rubric:** v1 (C-01 through C-10; essential C-01–C-05)
**Round:** R1 — single-axis pass (V-01/V-02/V-03) + combined (V-04/V-05)

---

## Round 1 Variation Map

| V | Axis | What Changed | Hypothesis |
|---|------|--------------|------------|
| V-01 | role-sequence | Coverage Analyst role declared before namespace loop | Priming the operator with the Coverage Analyst identity before generation improves C-02 (category classification) and C-03 (REAL-REQUIRED auto-application) because the classification mindset is established before artifacts are produced |
| V-02 | output-format | Per-namespace Coverage Verdict block + compact final table | Making the per-section artifact body obligation structural improves C-07 (substantive artifact bodies) because each section requires a 3+ line synthetic artifact plus an in-section verdict |
| V-03 | lifecycle-emphasis | Classification taxonomy and flag rules appear before generation loop | Front-loading flag rules before the 9-section generation loop improves C-03 (REAL-REQUIRED) and C-06 (tier annotation) because the rules are in active context when each section is written |
| V-04 | phrasing-register + lifecycle-emphasis | Fully imperative DO/DO NOT register combined with front-loaded classification rules | Combining prohibition-register with front-loaded rules targets C-01 through C-03 simultaneously — hard stops prevent omission of headers, categories, and flags |
| V-05 | inertia-framing + output-format | Gap-first framing with risk-ordered summary table | Treating gap detection as the primary output objective (not artifact generation) improves C-06 (tier annotations), C-08 (compliance flags), and C-10 (actionable next steps) by directing attention to what is missing before what is present |

---

## V-01 — Role Sequence: Coverage Analyst First

**axis:** role-sequence
**hypothesis:** Declaring the Coverage Analyst role before the namespace loop will improve C-02 (correct category classification) and C-03 (REAL-REQUIRED auto-flag application) because the model is primed to classify before generating. Falsifiable: if C-02 and C-03 do not improve over baseline, the role declaration adds no protective value.

---

You are running `/mock:all {topic}`.

ROLE: COVERAGE ANALYST

You are the Coverage Analyst for Signal. Your job is to generate a synthetic signal artifact
for every namespace in a single pass, then produce a unified coverage picture. You classify
first and generate second -- never the reverse.

---

STEP 1 — CLASSIFY ALL NAMESPACES

Before writing any artifact, assign every namespace its category and flag status:

| Namespace | Category | Auto-flag |
|-----------|----------|-----------|
| scout | HIGH-STRUCTURE | — |
| draft | HIGH-STRUCTURE | — |
| review | HIGH-STRUCTURE | — |
| flow | HIGH-STRUCTURE | — |
| trace | HIGH-STRUCTURE | — |
| prove | EVIDENCE-HEAVY | REAL-REQUIRED |
| listen | EVIDENCE-HEAVY | REAL-REQUIRED |
| program | MIXED | — |
| topic | MIXED | — |

EVIDENCE-HEAVY namespaces (prove, listen) are auto-flagged REAL-REQUIRED regardless of
artifact quality. A synthetic artifact cannot substitute for real signal in these namespaces.

---

STEP 2 — GENERATE ARTIFACT SECTIONS

For each of the 9 namespaces, write one section in the following format:

```
## {Namespace}

<!-- MOCK ARTIFACT -->
Skill: {namespace}-{primary-skill}
Topic: {topic}
Category: {category-from-classification}
Date: {date}
Status: MOCK
{flag-line-if-applicable}

{synthetic-artifact-body — 3 or more substantive lines representing realistic signal content
for this namespace. Not generic filler. Content should reflect what a real artifact would say
about {topic}.}
```

Where {flag-line-if-applicable} is:
  `Flag: REAL-REQUIRED` — if Category is EVIDENCE-HEAVY
  (omit the Flag line if no flag applies)

Write all 9 namespace sections before proceeding to Step 3.

---

STEP 3 — COVERAGE SUMMARY TABLE

Produce a Markdown table with exactly these 4 columns and 9 data rows:

| Namespace | Category | Flag | Recommended next step |
|-----------|----------|------|-----------------------|

Rules for the Flag column:
- REAL-REQUIRED — any EVIDENCE-HEAVY namespace
- REAL-REQUIRED — scout-compliance and trace-permissions if the topic carries compliance tags
  (check TOPICS.md if available; if absent, apply REAL-REQUIRED conservatively)
- TIER-2-CRITICAL — trace namespace row
- TIER-3-CRITICAL — scout-feasibility and listen namespace rows
  (a row may carry multiple annotations, e.g., "REAL-REQUIRED | TIER-3-CRITICAL")
- — if no flag applies

Rules for the Recommended next step column:
- Name a specific Signal skill invocation (e.g., `/scout:feasibility {topic}`)
- Never write "gather more data" or "run the skill"

---

STEP 4 — TIER FLAG (--tier support)

If invoked with `--tier 2`: output only sections for trace, prove, listen.
If invoked with `--tier 3`: output only sections for prove and listen.
Default (--tier 1 or no flag): output all 9 namespace sections.

---

FINAL LINE

The last line of your output must be exactly:

Next: /mock:review {topic} {this-file}

where `{topic}` is the topic name you received and `{this-file}` is the artifact filename
produced in this run (not a placeholder).

---

## V-02 — Output Format: Per-Section Verdict Block

**axis:** output-format
**hypothesis:** Adding an explicit per-section Coverage Verdict block (requiring 3+ substantive lines in the artifact body plus a FLAG and NEXT verdict) will improve C-07 (substantive artifact bodies) because the structural requirement appears within each section rather than as a footnote. Also improves C-10 (actionable next steps) because the NEXT field is per-section, not only in the table.

---

You are running `/mock:all {topic}`.

Generate a synthetic signal artifact for every namespace. For each namespace, write a
section containing:
  1. A MOCK ARTIFACT header block
  2. A synthetic artifact body (minimum 3 substantive lines)
  3. A Coverage Verdict block

Then close with a summary table and the handoff line.

---

NAMESPACE SECTIONS

Write exactly 9 sections — one per namespace in this order:
scout, draft, review, flow, trace, prove, listen, program, topic.

Each section follows this structure:

```
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
```

CATEGORY assignment rules:
- prove-* and listen-* namespaces → EVIDENCE-HEAVY
- scout, draft, review, flow, trace → HIGH-STRUCTURE
- program, topic → MIXED

FLAG assignment rules:
- EVIDENCE-HEAVY → REAL-REQUIRED (mandatory, cannot be omitted)
- HIGH-STRUCTURE or MIXED → REVIEW-RECOMMENDED unless a compliance or tier condition applies:
    trace namespace → also annotate TIER-2-CRITICAL
    scout namespace (feasibility skill) → also annotate TIER-3-CRITICAL
    listen namespace → also annotate TIER-3-CRITICAL
    scout-compliance or trace-permissions in scope → REAL-REQUIRED regardless of category
- Multiple flags on one row: separate with " | "

ARTIFACT-BODY rules:
- Write content that a real {namespace} artifact would plausibly contain for {topic}
- Minimum 3 substantive lines — not headers, not the category label, not the topic name alone
- Content is synthetic (MOCK) but must look structurally identical to a real artifact

---

COVERAGE SUMMARY TABLE

After all 9 sections, write:

| Namespace | Category | Flag | Recommended next step |
|-----------|----------|------|-----------------------|
(9 rows, one per namespace)

The Flag and Recommended next step columns must be identical to the Coverage Verdict blocks
written above. No new values may appear in the table that were not present in a section.

---

TIER FLAG

--tier 1 (default): all 9 namespace sections.
--tier 2: sections for trace, prove, listen only.
--tier 3: sections for prove and listen only.

---

FINAL LINE

```
Next: /mock:review {topic} {this-file}
```

Replace {topic} with the actual topic name. Replace {this-file} with the artifact filename
produced. Do not emit literal placeholder text.

---

## V-03 — Lifecycle Emphasis: Classification Rules First

**axis:** lifecycle-emphasis
**hypothesis:** Front-loading the complete classification taxonomy and flag-propagation rules before the generation loop will improve C-03 (REAL-REQUIRED auto-flag) and C-06 (tier-critical annotation) because the rules are loaded into context before any artifact writing begins, not buried after. If C-03 and C-06 do not improve, front-loading provides no advantage over inline reminders.

---

You are running `/mock:all {topic}`.

---

CLASSIFICATION TAXONOMY (read before writing any section)

Every namespace section must carry one of these category labels:

  HIGH-STRUCTURE — scout, draft, review, flow, trace
    These namespaces produce structured artifacts (tables, scored lists, decision trees).
    Synthetic artifacts are plausible coverage proxies.

  EVIDENCE-HEAVY — prove, listen
    These namespaces produce artifacts whose value depends on real data (interview notes,
    prototype results, user feedback). SYNTHETIC ARTIFACTS CANNOT SUBSTITUTE.
    Every section with Category: EVIDENCE-HEAVY MUST carry Flag: REAL-REQUIRED.
    This rule is unconditional. If Category is EVIDENCE-HEAVY, Flag is REAL-REQUIRED.
    No exception.

  MIXED — program, topic
    These namespaces combine structure with interpretation. Synthetic artifacts are partial
    proxies — treat as plausible but verify before committing.

---

FLAG RULES (read before writing any section)

Apply these flags in the Flag line of the MOCK ARTIFACT header and in the summary table:

  REAL-REQUIRED
    Mandatory on: any EVIDENCE-HEAVY namespace (prove, listen).
    Mandatory on: scout-compliance and trace-permissions if the topic has compliance tags.
    Meaning: a real artifact is required before this signal can be used in a decision.

  TIER-2-CRITICAL
    Mandatory on: trace namespace row in the summary table.
    Meaning: trace is a tier-2 signal for most topics; synthetic coverage here understates risk.

  TIER-3-CRITICAL
    Mandatory on: scout-feasibility and listen namespace rows in the summary table.
    Meaning: these are tier-3 signals — foundational; gaps here block downstream work.

  Multiple flags on one row: join with " | " (e.g., "REAL-REQUIRED | TIER-3-CRITICAL")

---

MOCK ARTIFACT HEADER FORMAT

Every section opens with exactly this header block (fill in each field):

```
<!-- MOCK ARTIFACT -->
Skill: {namespace}-{primary-skill}
Topic: {topic}
Category: {category}
Date: {date}
Status: MOCK
Flag: {flag}
```

Omit the Flag line only if no flag applies (HIGH-STRUCTURE or MIXED namespace with no
compliance or tier condition).

---

GENERATION LOOP

Now write 9 sections — scout, draft, review, flow, trace, prove, listen, program, topic.

Each section:
  ## {Namespace}

  [MOCK ARTIFACT header as specified above]

  [Artifact body: 3 or more substantive lines. Write what a real {namespace} artifact would
  plausibly contain for {topic}. The body demonstrates the namespace's signal type, not
  generic filler. Example: a scout section shows competitive positioning signals; a flow
  section shows lifecycle stage signals.]

Write all 9 sections before the summary table.

---

COVERAGE SUMMARY TABLE

Produce the summary table immediately after the 9 sections:

| Namespace | Category | Flag | Recommended next step |
|-----------|----------|------|-----------------------|

  - Flag column: use the flag values assigned per the FLAG RULES above
  - Recommended next step column: name the specific Signal skill to run next
    (e.g., `/trace:contract {topic}` — not "run trace" or "gather evidence")

9 rows. Exactly these 4 columns. No extras.

---

TIER FLAG (--tier support)

--tier 1 (default): produce all 9 namespace sections and all 9 summary rows.
--tier 2: produce sections and rows for trace, prove, listen only.
--tier 3: produce sections and rows for prove and listen only.

---

FINAL LINE (mandatory)

The last line must be:

  Next: /mock:review {topic} {this-file}

{topic} = the topic name supplied at invocation.
{this-file} = the artifact filename written in this run.
No literal placeholder text in the output.

---

## V-04 — Phrasing Register + Lifecycle Emphasis: Imperative DO/DO NOT + Rules First

**axis:** phrasing-register + lifecycle-emphasis
**hypothesis:** Fully imperative DO/DO NOT register combined with front-loaded classification rules will improve C-01 (all 9 namespace headers complete), C-02 (correct category labels), C-03 (REAL-REQUIRED applied), and C-08 (compliance pre-flagging) simultaneously. Hard prohibitions prevent common omissions that procedural instruction leaves ambiguous. Falsifiable: if essential pass rate does not exceed single-axis variations, the imperative register adds no incremental value over lifecycle-emphasis alone.

---

You are running `/mock:all {topic}`.

---

CLASSIFICATION RULES — READ THESE BEFORE WRITING ANYTHING

DO classify these namespaces as HIGH-STRUCTURE: scout, draft, review, flow, trace.
DO classify these namespaces as EVIDENCE-HEAVY: prove, listen.
DO classify these namespaces as MIXED: program, topic.
DO NOT invent a fourth category.
DO NOT assign HIGH-STRUCTURE to prove or listen for any reason.

DO apply Flag: REAL-REQUIRED to every EVIDENCE-HEAVY section.
DO NOT omit the REAL-REQUIRED flag from any EVIDENCE-HEAVY section.
DO NOT write a prove or listen section without a REAL-REQUIRED flag.

DO apply Flag: REAL-REQUIRED to scout-compliance and trace-permissions sections if the topic
has compliance tags (check TOPICS.md; if absent, apply conservatively).
DO NOT assume a topic lacks compliance tags without checking.

---

REQUIRED HEADER FORMAT

Every namespace section MUST open with this exact block:

```
<!-- MOCK ARTIFACT -->
Skill: {namespace}-{primary-skill}
Topic: {topic}
Category: {category}
Date: {date}
Status: MOCK
```

If a flag applies, add immediately below Status: MOCK:
  Flag: {flag}

DO NOT omit any field from this block.
DO NOT begin a section with the artifact body before the header block.
DO NOT use a different header format.

---

GENERATE THE 9 SECTIONS

Write one section per namespace in this order: scout, draft, review, flow, trace, prove,
listen, program, topic.

Each section:
  ## {Namespace}
  [Required header block above]
  [Artifact body]

DO write a minimum of 3 substantive lines per artifact body.
DO write content that reflects realistic {namespace} signal for {topic}.
DO NOT write header-only sections with no artifact body.
DO NOT use placeholder text such as "[artifact content here]" in the body.

DO NOT proceed to the summary table until all 9 sections are complete.

---

TIER FLAG BEHAVIOR

DO produce all 9 sections when invoked without --tier (default: --tier 1).
DO produce only sections for trace, prove, listen when invoked with --tier 2.
DO produce only sections for prove and listen when invoked with --tier 3.
DO NOT produce sections for namespaces outside the tier scope.

---

COVERAGE SUMMARY TABLE

After the 9 sections, write a Markdown table with exactly these 4 columns:

  | Namespace | Category | Flag | Recommended next step |

DO include exactly 9 data rows.
DO NOT add, rename, or reorder columns.
DO annotate the trace row as TIER-2-CRITICAL in the Flag column.
DO annotate the scout-feasibility row and listen row as TIER-3-CRITICAL in the Flag column.
DO NOT omit tier annotations from these three rows.
DO write a concrete skill invocation in the Recommended next step column for every row.
DO NOT write generic advice ("run the skill", "gather more data") in that column.

---

FINAL LINE

DO end your output with exactly:

  Next: /mock:review {topic} {this-file}

DO NOT end with any other line.
DO NOT emit literal placeholder tokens in the final line.

---

## V-05 — Inertia Framing + Output Format: Gap-First Coverage Report

**axis:** inertia-framing + output-format
**hypothesis:** Framing the output as a gap report (primary purpose: surface what must not remain as mock) rather than an artifact catalog (primary purpose: show what was generated) will improve C-06 (tier-critical annotations), C-08 (compliance pre-flagging), and C-10 (actionable next steps) because the analyst is oriented toward risk identification rather than completion theater. A risk-ordered summary table (REAL-REQUIRED and TIER-CRITICAL rows first) makes gaps structurally primary. Falsifiable: if C-06, C-08, and C-10 do not improve over V-03, inertia framing adds no value.

---

You are running `/mock:all {topic}`.

PURPOSE: Gap detection, not coverage theater.

The output of this skill is a coverage gap report. You will generate synthetic mock artifacts
for all 9 namespaces so the team can see the full evidence shape at a glance — but the primary
deliverable is the answer to: "Where does this topic have dangerous mock coverage that must
not remain synthetic before a real decision is made?"

The synthetic artifacts show what a real signal would look like. The coverage summary shows
which signals cannot stay synthetic. Default assumption: no evidence is better than fake
evidence. REAL-REQUIRED flags exist because acting on a synthetic artifact is worse than
knowing you lack the signal.

---

STEP 1 — GENERATE NAMESPACE SECTIONS

Write one section per namespace: scout, draft, review, flow, trace, prove, listen, program, topic.

Each section format:

```
## {Namespace}

<!-- MOCK ARTIFACT -->
Skill: {namespace}-{primary-skill}
Topic: {topic}
Category: {category}
Date: {date}
Status: MOCK
{flag-if-applicable}

{artifact-body}
```

Category and flag rules:

  prove and listen → Category: EVIDENCE-HEAVY, Flag: REAL-REQUIRED
    (These namespaces require real interviews, prototypes, or usage data.
     A synthetic artifact proves nothing. Do not let MOCK coverage here
     substitute for the absence of a real signal.)

  scout, draft, review, flow, trace → Category: HIGH-STRUCTURE
    No flag by default, unless:
    - topic has compliance tags: scout-compliance and trace-permissions rows get REAL-REQUIRED
    - trace namespace always gets TIER-2-CRITICAL in the summary table
    - scout-feasibility and listen always get TIER-3-CRITICAL in the summary table

  program, topic → Category: MIXED
    No flag by default.

Artifact body: write 3 or more substantive lines per section. Show what the real artifact
would plausibly contain for {topic} — competitive signals, technical constraints, user
feedback patterns, etc. The body is synthetic but structurally realistic.

---

STEP 2 — COVERAGE GAP REPORT (summary table)

Produce a table that answers: "What must not stay synthetic?"

Order rows by risk:
  1. REAL-REQUIRED rows first (prove, listen — always; compliance rows if applicable)
  2. TIER-CRITICAL rows second (trace, scout-feasibility)
  3. Remaining rows last (lowest gap risk)

Table columns — exactly these 4:

  | Namespace | Category | Flag | Recommended next step |

Flag column values (apply all that fit, join with " | "):
  REAL-REQUIRED — evidence-heavy or compliance-tagged namespaces
  TIER-2-CRITICAL — trace namespace
  TIER-3-CRITICAL — scout-feasibility, listen namespaces

Recommended next step column:
  Name the specific Signal skill to run next to convert this MOCK to REAL.
  Format: `/{namespace}:{skill} {topic}`
  Examples: `/prove:prototype {topic}`, `/listen:adoption {topic}`, `/trace:contract {topic}`
  DO NOT write "gather more evidence" or "run the skill" or any non-specific guidance.

9 rows. Exactly 4 columns. Risk-ordered.

---

STEP 3 — TIER FLAG (--tier support)

--tier 1 (default): all 9 sections and 9 summary rows.
--tier 2: sections and rows for trace, prove, listen only.
--tier 3: sections and rows for prove and listen only.
When scoped by --tier, omit sections and rows outside scope entirely.

---

FINAL LINE

End with:

  Next: /mock:review {topic} {this-file}

{topic} = topic name from invocation (no placeholder text).
{this-file} = filename of the artifact produced in this run (no placeholder text).
This line must be the last line of your output.
