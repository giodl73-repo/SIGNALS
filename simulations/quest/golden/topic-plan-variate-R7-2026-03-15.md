# topic-plan Skill Variations — Round 7 (2026-03-15)

Rubric: v7 (C-01–C-24, ceiling 142 pts)
New criteria this round: C-22 (Prohibition-Repair Pairing), C-23 (Dual-Juncture Exit-Artifact Coverage), C-24 (Declaration-Structure Coherence)

---

## Round 7 Design Notes

Round 6 surfaced three discriminating signals:

1. **V-01 perfect on C-20 via repair pairing** — The strongest C-20 expression paired
   the prohibition ("no templates") with an explicit recovery action ("discard it and
   rewrite as prose"). Declaration alone leaves the model uncertain what to do when a
   violation is noticed mid-execution. C-22 generalizes this: every structural prohibition
   in the synthesis phase must carry a named repair — a detection trigger and a correction
   step — so recovery is as mechanical as prevention.

2. **V-01/V-04/V-05 dual exit artifacts** — The strongest R6 designs produced concrete
   artifacts at both critical junctures: synthesis paragraph at the synthesis gate,
   proposals table at the confirmation gate. C-23 elevates this from excellence to
   requirement: both gates must be artifact-locked.

3. **V-02 partial on C-20 via structural self-violation** — The `[Write 5–8 sentences
   here…]` placeholder inside the `=== SYNTHESIS ===` zone was a structural model of
   the prohibited form. The prohibition and a demonstration of what the prohibition
   forbids coexisted in the same zone, making the declaration architecturally incoherent.
   C-24 closes this: no element within a prohibited zone may instantiate the prohibited
   form, even as an instruction placeholder.

**Round 7 strategy:** All five variations satisfy C-23 (dual gate artifacts) and C-24
(no fill-in placeholders inside synthesis zone). C-22 is the primary discriminating
axis — each variation uses a different mechanism to pair prohibitions with repairs.

| Variation | Axis | C-22 mechanism | C-24 mechanism |
|-----------|------|----------------|----------------|
| V-01 | Lifecycle emphasis | PROHIBITION-REPAIR CATALOG before synthesis zone; 3 named entries each with detection trigger + repair | Catalog precedes zone; no fill-in inside zone |
| V-02 | Output format | Prohibition-repair pairs in synthesis preamble block; zone contains no instruction content | Architecturally evacuated zone: all instructions in preamble; markers enclose nothing but model output |
| V-03 | Phrasing register | Inline RECOVERY SCRIPT immediately after each prohibition; detection trigger + correction step named at site | Plain instruction text only; no bracketed placeholders |
| V-04 | Inertia framing + role sequence | Repair procedures with motivational grounding; COMPLIANCE AUDIT as gate condition | EVIDENCE-ONLY TERRAIN rules in pre-synthesis block; terrain contains no instruction structure |
| V-05 | Combined (all prior best + all three new criteria as skeleton) | PROHIBITION-REPAIR CATALOG as named structural primitive, declared upfront before any pass | DUAL-GATE DECLARATION + architecturally evacuated synthesis zone as skeleton elements |

---

## V-01: Lifecycle Emphasis + Prohibition-Repair Catalog

**Variation axis**: Lifecycle emphasis — the SYNTHESIS ZONE / COMPARISON ZONE
architecture from R6 V-01 is extended with a PROHIBITION-REPAIR CATALOG that precedes
the synthesis zone. Every structural prohibition in the synthesis zone has a named entry
in the catalog specifying: what is prohibited, how to detect a violation, and what
repair to apply. The synthesis zone references the catalog by name. Both critical gates
produce named exit artifacts.

**Hypothesis**: An enumerated catalog with named entries (PR-01/PR-02/PR-03) is stronger
than embedded prohibitions because it makes the repair set bounded and auditable — the
model can confirm "I checked PR-01, PR-02, PR-03" rather than inferring which prohibitions
apply. The catalog pattern also makes C-22 retroactively applicable to all prohibitions,
not just the template prohibition that C-20 already covered. The two named EXIT ARTIFACTs
(synthesis paragraph at Phase 2, proposals table at Confirmation Gate) satisfy C-23 by
making both critical gates observable.

```
You are running /topic:plan for the topic named in the user's message.

---

## Pre-phase — Anchor the reference line (date only)

Read strategy.md for this topic (locate path via simulations/TOPICS.md). Extract its
last-modified date only. Write it here:

  STRATEGY DATE: [YYYY-MM-DD]

Do not read strategy.md content. Close it after recording the date.

If strategy.md does not exist: "No strategy.md found. Run /topic:new first." Stop.

---

## SYNTHESIS ZONE RULES — PROHIBITION-REPAIR CATALOG

Read this catalog before entering the SYNTHESIS ZONE. Each entry names the prohibited
form, its detection trigger, and its repair action. All three entries apply from the
SYNTHESIS ZONE OPEN through the SYNTHESIS ZONE CLOSE. Repairs are self-correcting:
detect the violation, apply the repair, continue.

PR-01 — TEMPLATES AND STRUCTURED ELEMENTS
  Prohibition: No output templates, markdown tables, structured headers (## or ###),
    bullet points (* or -), numbered lists, or fill-in tables.
  Detection trigger: Any markdown table row (| col |); any line beginning with ## or
    ### or * or -; any bracket-enclosed instruction of the form [write X here].
  Repair action: Delete the element. Rewrite its informational content as a sentence
    in the running paragraph. The information survives; the structure does not.

PR-02 — STRATEGY REFERENCE
  Prohibition: No mention of strategy.md by name or reference to any named strategy
    dimension, declared stage, namespace name, or skill name from the plan.
  Detection trigger: The string "strategy.md" in any form; the name of any dimension
    used as an organizing label (e.g., "namespace coverage," "declared stage").
  Repair action: Delete the sentence. Rewrite using only language from the artifact
    itself — describe what the signal says, not how it relates to strategy.

PR-03 — DIMENSIONAL ORGANIZATION
  Prohibition: Do not break the synthesis into labeled sections organized by dimension
    or category. One continuous paragraph only.
  Detection trigger: More than one labeled paragraph; any paragraph that opens with a
    category name as its organizing premise.
  Repair action: Remove the label. Merge the content into the single running paragraph.

---

## SYNTHESIS ZONE (Phases 0–2)

---

### Phase 0 — Signal inventory

List every signal artifact in simulations/ matching the topic slug. For each, one line:

  [artifact-filename] | [date] | NEW (> STRATEGY DATE) or PRIOR

If no artifacts exist: "No signal artifacts found for [topic]. Cannot run /topic:plan." Stop.

---

### Phase 1 — Read NEW artifacts

Read every artifact labeled NEW in Phase 0. PRIOR artifacts are already incorporated in
strategy.md — skip them. PROHIBITION-REPAIR CATALOG is in effect.

---

### Phase 2 — Synthesis paragraph (EXIT ARTIFACT for SYNTHESIS ZONE)

Write a freeform paragraph of 5 to 8 sentences describing what the NEW signals
collectively say. PROHIBITION-REPAIR CATALOG (PR-01, PR-02, PR-03) applies throughout.
Name at least two specific artifact filenames in the text.

Self-monitoring audit: after writing, check each sentence against PR-01, PR-02, and
PR-03. For each violation: apply the named repair. When all three checks are clean,
write: "PROHIBITION AUDIT: complete."

This paragraph is the EXIT ARTIFACT for the SYNTHESIS ZONE. The COMPARISON ZONE does
not open until the EXIT ARTIFACT exists, names at least two artifacts by filename, and
the PROHIBITION AUDIT is written.

**Stop. Do not enter the COMPARISON ZONE until the Phase 2 EXIT ARTIFACT is produced
and the PROHIBITION AUDIT is written. Halt here.**

---

## COMPARISON ZONE (Phases 3–6)

Templates are permitted in the COMPARISON ZONE.

---

### Phase 3 — Read strategy.md content

Now read strategy.md fully. Extract:

| Strategy element | Content |
|------------------|---------|
| Declared stage | |
| Namespaces covered | |
| Skills planned | |
| Stated rationale | |
| Acknowledged gaps | |
| Unstated assumptions | [at least one — most important delta candidate] |

All rows must be filled before proceeding.

---

### Phase 4 — Delta detection

Using the Phase 2 synthesis paragraph as the prior, identify where NEW signals diverge
from or extend strategy.md.

A dimension is CONFIRMED NEW only if both conditions are true:
1. Present in at least one NEW artifact (date > STRATEGY DATE)
2. Absent from strategy.md

Dimensions satisfying condition 1 but failing condition 2: annotate "PRIOR-ONLY — not a delta."

| Finding ID | Strategy assumed | Signal revealed | Source artifact |
|-----------|-----------------|----------------|-----------------|
| F-01 | [what strategy said or implicitly committed to] | [what signal showed] | [filename] |

Null case: `F-00 | Strategy confirmed | No new findings | All NEW artifacts`

---

### Phase 5 — Coverage map

For every strategy.md dimension, one row. For every dimension Phase 2 synthesis
introduced not in strategy.md, one row marked [NEW DIMENSION]:

| Dimension | Status | Evidence artifact | Assessment |
|-----------|--------|-------------------|------------|
| [name] | VALIDATED / CHALLENGED / NOT COVERED | [filename] | [1 sentence] |
| [new dim] [NEW DIMENSION] | CONFIRMED NEW / PRIOR-ONLY | [filename] | [1 sentence] |

---

### Phase 6 — Change proposals

The default outcome is NO CHANGE. A proposal earns its place by beating the null.

| # | Action | Dimension | Evidence artifact | Before | After | Confidence | vs. NO CHANGE |
|---|--------|-----------|-------------------|--------|-------|------------|---------------|
| 1 | ADD / REMOVE / REPRIORITIZE | [dimension] | [filename] | [current or —] | [proposed or —] | HIGH / MEDIUM / LOW | [why this beats doing nothing] |

Requirements:
- All three action types (ADD, REMOVE, REPRIORITIZE) must appear, or each absent type
  explicitly marked NULL: "No [TYPE] proposals — [reason]"
- REPRIORITIZE rows show before-rank and after-rank as numbers
- Evidence must be a NEW artifact only (date > STRATEGY DATE)
- If no changes warranted: "NO CHANGES PROPOSED — existing strategy validated by new signals."

---

## Confirmation gate (EXIT ARTIFACT: filled proposals table)

Present the Phase 5 coverage map and Phase 6 proposals table to the user.

The filled proposals table (or the "NO CHANGES" statement) is the EXIT ARTIFACT for
the Confirmation Gate. The confirmation question is not asked until this EXIT ARTIFACT
exists.

**Stop. Do not write to strategy.md. Do not modify any file.**

Write exactly:
"Shall I apply these changes to strategy.md? Reply YES to write, NO to discard, or
edit the table and reply REVISED to apply your version."

Wait for the user's reply before proceeding.

---

## Apply phase (triggered by YES or REVISED)

Write exactly the confirmed changes to strategy.md. No additional edits. After writing:

"strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-02: Output Format + Architecturally Evacuated Synthesis Zone

**Variation axis**: Output format — the synthesis phase uses boundary markers
(`=== SYNTHESIS OPEN ===` / `=== SYNTHESIS CLOSE ===`), but unlike R6 V-02, all
synthesis instructions reside in a SYNTHESIS PREAMBLE block that explicitly closes
before the zone open marker. The zone itself contains no instruction content of any
kind — when the model encounters the zone, it finds only its own output. Prohibition-
repair pairs appear in the preamble. Both critical gates produce named exit artifacts.

**Hypothesis**: R6 V-02's failure was placing `[Write 5–8 sentences here…]` inside
the zone — that placeholder was structurally a template, demonstrating the prohibited
form alongside the prohibition. The fix is architectural: move all instructions to a
preamble that ends before the zone opens, so the zone contains only the model's written
synthesis. The model cannot instantiate a prohibited form inside the zone because the
zone has no instruction content to model from. C-22 is satisfied by explicit
prohibition-repair pairs in the preamble. C-23 is satisfied by the Block 2 EXIT
ARTIFACT and the Block 7 PENDING CONFIRMATION banner.

```
You are running /topic:plan for the topic named in the user's message.

Fill every block below in order. Do not skip a block. Do not read ahead.

---

### Block 0 — Strategy date (date only)

Open strategy.md. Extract its last-modified date. Write:

  STRATEGY DATE: [YYYY-MM-DD]

Close the file. Do not read its content yet.

If strategy.md does not exist: "No strategy.md found. Run /topic:new first." Stop.

---

### Block 1 — Signal inventory

Glob simulations/ for all artifacts matching the topic slug. For each, one line:

  [filename] | [date] | NEW (> STRATEGY DATE) or PRIOR

If no artifacts found: "No signal artifacts found. Cannot run /topic:plan." Stop.

---

### Block 2 — Synthesis preamble

Read every NEW artifact from Block 1. This block contains all instructions for
writing the synthesis. The synthesis zone that follows contains no additional
instructions — write based on this preamble alone.

WHAT TO WRITE: a freeform paragraph of 5 to 8 sentences about what the NEW signals
collectively say. One continuous paragraph of plain prose. Name at least two specific
artifact filenames in the text.

PROHIBITION-REPAIR PAIRS (apply during writing and in the self-monitoring audit):

  PR-01 (templates): If a markdown table row, bullet point, or structured header
    appears inside the zone — delete it. Rewrite its content as a sentence.
  PR-02 (strategy reference): If "strategy.md" or a named strategy dimension appears
    — delete the sentence. Rewrite using only language from the artifact itself.
  PR-03 (categorical structure): If the paragraph splits into labeled sections — remove
    the labels. Merge into one continuous paragraph.

EXIT ARTIFACT REQUIREMENT: The synthesis paragraph written in the zone below is the
EXIT ARTIFACT for Block 2. Block 3 does not open until the zone holds at least 5
sentences, names at least two artifacts by filename, and the self-monitoring audit
confirms all PR checks are clean.

SELF-MONITORING AUDIT: after writing, check PR-01, PR-02, PR-03. Apply any repair.
Write "SYNTHESIS AUDIT: clean." to confirm.

**Stop. Do not read strategy.md content until the Block 2 EXIT ARTIFACT is written
and SYNTHESIS AUDIT: clean is confirmed. Halt here.**

—— SYNTHESIS PREAMBLE ENDS. Write synthesis paragraph in the zone below. ——

=== SYNTHESIS OPEN ===
=== SYNTHESIS CLOSE ===

—— Continue to Block 3 after EXIT ARTIFACT and SYNTHESIS AUDIT are written above. ——

---

### Block 3 — Strategy content

Now read strategy.md fully. Fill:

| Field | Value |
|-------|-------|
| Declared stage | |
| Namespaces covered | |
| Skills planned | |
| Stated rationale | |
| Acknowledged gaps | |
| Unstated assumptions | [at least one] |

---

### Block 4 — Delta findings

A dimension is CONFIRMED NEW only if: (1) present in a NEW artifact AND (2) absent
from strategy.md. Condition 1 alone is not sufficient — mark failures "PRIOR-ONLY — not a delta."

| Finding ID | Strategy assumed | Signal revealed | Source artifact |
|-----------|-----------------|----------------|-----------------|
| F-01 | | | |

Null case: `F-00 | Strategy confirmed | No new findings | All NEW artifacts`

---

### Block 5 — Coverage map

| Dimension | In strategy.md | Signal coverage | Status | Primary artifact |
|-----------|---------------|-----------------|--------|------------------|
| [fill] | YES / NO | COVERED / GAP / NEW | VALIDATED / CHALLENGED / NOT COVERED / CONFIRMED NEW / PRIOR-ONLY | [filename] |

---

### Block 6 — Change proposals

The default is NO CHANGE. A proposal earns its place by beating the null.

| # | Action | Dimension | Evidence artifact | Before | After | Confidence | vs. NO CHANGE |
|---|--------|-----------|-------------------|--------|-------|------------|---------------|
| 1 | ADD / REMOVE / REPRIORITIZE | [fill] | [filename] | [fill] | [fill] | HIGH / MED / LOW | [why beats nothing] |

Requirements:
- [ ] All three action types present, or each absent type has explicit NULL row:
      "| — | ADD | No ADD proposals | N/A | — | — | — | N/A |"
      "| — | REMOVE | No REMOVE proposals | N/A | — | — | — | N/A |"
      "| — | REPRIORITIZE | No REPRIORITIZE proposals | N/A | — | — | — | N/A |"
- [ ] Every REPRIORITIZE row shows numeric Before and After ranks
- [ ] Every evidence artifact from the NEW list (date > STRATEGY DATE)

Write "[NO CHANGES]" if no changes are warranted.

---

### Block 7 — Confirmation gate (EXIT ARTIFACT: PENDING CONFIRMATION banner)

Display Block 5 and Block 6.

Produce the following PENDING CONFIRMATION banner verbatim (this banner is the
EXIT ARTIFACT for the confirmation gate — do not proceed until it is written):

---
PENDING CONFIRMATION — strategy.md has NOT been modified.

Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to discard | REVISED + edited table to apply custom version
---

**Stop here. Write nothing further until the user replies.**

---

### Block 8 — Apply (triggered by YES or REVISED)

Write only the confirmed changes to strategy.md. No reformatting of unchanged sections.
After writing:

"strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-03: Phrasing Register + Inline Recovery Scripts

**Variation axis**: Phrasing register — short imperative sentences; each prohibition
in the synthesis phase is immediately followed by a verbatim RECOVERY SCRIPT: the
exact string the model writes when it detects a violation. The recovery action is
mechanical and observable rather than discretionary — the model does not decide how
to recover, it follows a named script. Both critical gates produce named exit tokens.

**Hypothesis**: Recovery scripts paired inline with their prohibitions satisfy C-22
at the point of application — the detection trigger and correction step appear at
the prohibition site, not in a separate catalog consulted before the zone. The model
reads "Do not X. Recovery script: if X appears, write [Y] and rewrite." in one
contiguous instruction block, making the prohibition-repair pair maximally local.
The observable output of the recovery script ("REPAIR: ...") also makes violation
detection auditable in the model's output stream, not only in the self-monitoring
audit. Both exit tokens — "SYNTHESIS TEXT: complete." and the filled proposals table
— satisfy C-23 by materializing both critical gates.

```
You are running /topic:plan. The topic is in the user's message.

Do these steps in order. Output each result before moving to the next.

---

1. Find strategy.md for this topic. Open it. Read only the date — not the content.
   Write:

     STRATEGY DATE: [YYYY-MM-DD]

   Close the file. If strategy.md doesn't exist: "No strategy.md found. Run /topic:new
   first." Stop.

2. List every signal artifact in simulations/ matching the topic slug. For each, one line:

     [filename] | [date] | NEW or PRIOR

   NEW = date strictly after STRATEGY DATE. PRIOR = date on or before.
   If no artifacts: "No artifacts found. Cannot run /topic:plan." Stop.

3. Read every NEW artifact. Skip PRIOR ones — they are already reflected in strategy.md.

4. Write your SYNTHESIS TEXT.

   SYNTHESIS RULES (read before writing; recovery scripts apply during writing):

   Rule A — no structural elements:
     No tables. No bullet points. No headers. No fill-in templates.
     Recovery script: if a table row, bullet, or header appears, write
     "REPAIR A: [element type] removed, rewriting as sentence." then rewrite as prose.

   Rule B — no strategy reference:
     Do not mention strategy.md. Do not organize by strategy dimensions.
     Recovery script: if "strategy.md" or a strategy dimension name appears, write
     "REPAIR B: strategy reference removed, rewriting from signal." then rewrite
     using only language from the artifact itself.

   Rule C — single paragraph:
     Write one continuous paragraph, 5 to 8 sentences. Do not break into sections.
     Recovery script: if multiple labeled sections appear, write
     "REPAIR C: labels removed, merging to single paragraph." then merge.

   Name at least two specific artifact filenames somewhere in the text.

   When finished, write on its own line: "SYNTHESIS TEXT: complete."

   Then run the self-monitoring audit: scan each sentence against Rules A, B, C.
   For each violation: apply the named recovery script. Confirm no violations remain.

   SYNTHESIS TEXT and the self-monitoring audit are the EXIT TOKEN for this step.
   Do not proceed until SYNTHESIS TEXT is labeled complete, the audit is clean,
   and at least two artifact filenames appear in the text.

**Stop. Do not read strategy.md content until SYNTHESIS TEXT is labeled complete
and the self-monitoring audit confirms clean.**

5. Now open and read strategy.md fully. For each element, write one line:
   Stage: [declared stage]
   Namespaces: [covered]
   Skills: [planned]
   Rationale: [stated]
   Gaps: [acknowledged]
   Assumption: [at least one unstated assumption — most important delta candidate]

6. For each place where a NEW signal diverges from or extends those commitments:

     F-[N] | Strategy assumed [X] | Signal revealed [Y] | [filename]

   A dimension is genuinely new only if: (1) present in a NEW artifact AND (2) absent
   from strategy.md. Mark condition-1-only failures: "PRIOR-ONLY — not a delta."

   If no findings diverge: "F-00: Strategy confirmed — no new findings."

7. For each strategy dimension, one row in this table:

   | Dimension | Status | Primary artifact | Assessment |
   |-----------|--------|-----------------|------------|

   Status: VALIDATED / CHALLENGED / NOT COVERED.
   Mark each dimension from NEW signals not in strategy.md with [NEW DIMENSION].

8. Build proposals. Default: NO CHANGE. Every proposal must beat doing nothing.
   If a proposal doesn't clearly beat NO CHANGE, exclude it and say why.

   | # | Action | Dimension | Evidence | Before | After | Confidence | WHY BEATS NO CHANGE |
   |---|--------|-----------|----------|--------|-------|------------|---------------------|

   All three action types (ADD, REMOVE, REPRIORITIZE) must appear. For types with
   no proposals, write: "[TYPE]: No proposals — [reason or N/A]."
   REPRIORITIZE rows must show current rank and proposed rank as numbers.
   If nothing warrants change: "NO CHANGES — existing strategy validated by new signals."

   The filled proposals table (or NO CHANGES statement) is the EXIT TOKEN for this step.
   Do not ask for confirmation until this EXIT TOKEN is written.

9. Show the proposals. Write exactly:

     "Apply these changes to strategy.md? Reply YES to apply, NO to discard, or
      REVISED + edited list to apply your version."

**Stop. Do not touch strategy.md. Do not write any file.**

   Wait for the user's reply.

10. After YES or REVISED: write exactly those changes and nothing else.
    Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-04: Inertia Framing + Role Sequence + Compliance Audit as Gate Condition

**Variation axis**: Inertia framing + role sequence — NO CHANGE as the opening premise;
signals synthesized before strategy content is read; the synthesis phase is EVIDENCE-ONLY
TERRAIN with motivationally-grounded prohibition-repair rules; the self-monitoring audit
is formalized as a COMPLIANCE AUDIT checklist that is itself a gate condition before
advancing. Prohibition-repair rules in the terrain are motivated (explain why) rather
than merely mandated.

**Hypothesis**: When prohibition-repair rules are grounded in a reason (templates
contaminate evidence independence; strategy references import dimensional framing),
the model can apply the rule's spirit in cases the prompt didn't anticipate. The
COMPLIANCE AUDIT checklist formalizes C-22 as a gate condition: each prohibition is
checkable independently, and the gate does not open until all checks pass and repairs
are documented. Inertia framing from the first sentence means every proposal inherits
the NO CHANGE burden of proof before any analysis runs. The EVIDENCE SUMMARY named as
the evidentiary prior and the proposals table as the exit artifact satisfy C-23 via
motivated rather than mechanical materialization.

```
The default outcome of this skill is NO CHANGE to strategy.md. New signals must earn
their way into a change against the inertia of considered decisions.

You are running /topic:plan for the topic named in the user's message.

---

## Opening premise

Reading strategy content before inventorying signals allows the strategy's dimensional
frame to anchor the analysis and suppress findings that don't fit. For this reason:
signals are inventoried and synthesized before strategy content is read.

The synthesis phase is EVIDENCE-ONLY TERRAIN. Every structural prohibition in this
terrain is paired with a named repair procedure and a motivation explaining why the
prohibition exists. The model applies the prohibition to the letter and the spirit —
the motivation is the spirit.

---

## Step 1 — Anchor the reference line (date only)

Read strategy.md. Record its last-modified date:

  STRATEGY DATE: [YYYY-MM-DD]

Do not read the content of strategy.md. The date is all you need for now.

If strategy.md does not exist: "No strategy.md found. Run /topic:new first." Stop.

---

## Step 2 — Classify and inventory artifacts

List every signal artifact in simulations/ matching the topic. For each:
- filename
- artifact date
- classification: NEW (date > STRATEGY DATE) or PRIOR (date ≤ STRATEGY DATE)

PRIOR artifacts are already incorporated in strategy.md. They cannot serve as evidence.

If no NEW artifacts exist: "No signals since STRATEGY DATE. NO CHANGE — strategy is current." Stop.

---

## Step 3 — EVIDENCE SUMMARY (EVIDENCE-ONLY TERRAIN)

Read each NEW artifact. Write the EVIDENCE SUMMARY: a freeform paragraph of 5–8
sentences about what the NEW signals collectively say.

EVIDENCE-ONLY TERRAIN RULES WITH REPAIR PROCEDURES:

R-01 — TEMPLATES
  Why: Templates import organizational structure. Any template in the synthesis phase
    risks importing the strategy's dimensional scaffold — defeating the independence
    the terrain is meant to protect.
  Prohibition: No tables, no structured headers, no fill-in templates.
  Detection trigger: Any markdown table row; any ## or ### header; any bracketed
    instruction of the form [do X here].
  Repair: Delete the element. Rewrite its content as a sentence in the paragraph.
    Write "TERRAIN REPAIR R-01: [element] removed." before the rewritten sentence.

R-02 — STRATEGY REFERENCE
  Why: Naming strategy dimensions before synthesis completes imports the strategy's
    frame and defeats evidence independence. The signals speak first.
  Prohibition: Do not mention strategy.md. Do not organize by strategy dimensions.
  Detection trigger: The string "strategy.md"; any named dimension from the strategy
    file used as an organizing label.
  Repair: Delete the sentence. Rewrite using only language from the artifact.
    Write "TERRAIN REPAIR R-02: strategy reference removed." before the rewritten sentence.

R-03 — CATEGORICAL STRUCTURE
  Why: Multiple labeled sections impose analytical structure before synthesis completes,
    collapsing the unanchored-observation property the terrain is meant to preserve.
  Prohibition: One continuous paragraph only. No labeled sections.
  Detection trigger: More than one labeled paragraph or sub-heading.
  Repair: Remove labels. Merge into one continuous paragraph.
    Write "TERRAIN REPAIR R-03: labels removed, merged." before the merged content.

The EVIDENCE SUMMARY is the prior for all subsequent analysis. Every proposed change
must trace back to a specific observation in this summary — it is the evidentiary record.

COMPLIANCE AUDIT (gate condition — complete before advancing):
- [ ] R-01 checked: no template elements remain in the EVIDENCE SUMMARY
- [ ] R-02 checked: no strategy references remain in the EVIDENCE SUMMARY
- [ ] R-03 checked: single continuous paragraph confirmed
- [ ] Two artifact filenames named in the text
- [ ] All repairs documented with TERRAIN REPAIR tags

Write "COMPLIANCE AUDIT: complete." to clear the gate.

**Stop. Do not read strategy.md content until the EVIDENCE SUMMARY is written and
COMPLIANCE AUDIT: complete is written. Halt here.**

---

## Step 4 — Read strategy content and map signals

Now read strategy.md fully.

### 4a — Strategy commitments

For each element, one sentence:
- Declared stage
- Namespaces covered
- Skills planned
- Stated rationale
- Acknowledged gaps
- Unstated assumptions (at least one — most important delta candidate)

### 4b — Coverage map

| Dimension | Signal coverage | Assessment | Primary artifact |
|-----------|----------------|------------|------------------|
| [name] | VALIDATED / CHALLENGED / NOT COVERED | [1 sentence] | [filename] |

For each dimension the EVIDENCE SUMMARY raised not in strategy.md:

| New dimension [NEW DIMENSION] | Source artifact | Two-condition check | Confidence |
|-------------------------------|-----------------|---------------------|------------|
| [name] | [filename] | (1) In NEW artifact: YES/NO AND (2) Absent from strategy.md: YES/NO | HIGH / MED / LOW |

CONFIRMED NEW = both YES. PRIOR-ONLY = condition 1 YES, condition 2 NO.

### 4c — Delta findings

| Finding ID | Strategy assumed | Signal revealed | Source artifact |
|-----------|-----------------|----------------|-----------------|
| F-01 | [from 4a commitments] | [from EVIDENCE SUMMARY] | [filename] |

Null case: `F-00 | Strategy confirmed | No new findings | All NEW artifacts`

---

## Step 5 — Challenge proposals against NO CHANGE

For each potential change: is this clearly better than leaving strategy.md unchanged?
If yes — include it. If no or uncertain — write one sentence explaining why NO CHANGE wins.

| # | Action | Dimension | Evidence | Before | After | Confidence | Why this beats NO CHANGE |
|---|--------|-----------|----------|--------|-------|------------|--------------------------|
| [fill] | ADD / REMOVE / REPRIORITIZE | [fill] | [EVIDENCE SUMMARY claim + filename] | [fill] | [fill] | HIGH/MED/LOW | [fill] |

Requirements:
- All three action types (ADD, REMOVE, REPRIORITIZE) must appear, or each absent type
  explicitly excluded with one sentence stating why NO CHANGE wins for that type
- REPRIORITIZE rows show before and after rank as numbers
- Evidence column names both the EVIDENCE SUMMARY claim AND the source artifact filename
- "NO CHANGE — new signals validate existing strategy." if table is empty

The filled proposals table (or NO CHANGE statement) is the EXIT ARTIFACT for this step.
The confirmation question is not asked until this EXIT ARTIFACT exists.

---

## Step 6 — Confirmation gate

Present Step 4b coverage map, Step 4c delta findings, and Step 5 proposals.

**Stop. Do not write to strategy.md. Do not modify any file.**

Write:
"Proposed changes will modify strategy.md if confirmed. NO CHANGE is the default if
you take no action.
Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table."

Wait for the user's reply.

---

## Step 7 — Apply (triggered by YES or REVISED)

Write exactly the confirmed changes. Nothing extra.

"strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-05: Combined — All Three New Criteria as Structural Skeleton

**Variation axis**: Combined — the R6 V-05 skeleton (C-13+C-14+C-16+C-17+C-18+C-20+C-21)
is extended with three new structural primitives: (1) PROHIBITION-REPAIR CATALOG declared
upfront before any pass runs (C-22), (2) DUAL-GATE EXIT-ARTIFACT DECLARATION naming both
exit artifacts before any phase runs (C-23), (3) architecturally evacuated synthesis zone
where all instructions reside in a preamble block and the zone itself contains no
instruction content (C-24). All three new criteria are the skeleton alongside the seven
from R6 V-05 — no criterion is an annotation on an existing step.

**Hypothesis**: C-22 is strongest when the prohibition-repair catalog appears upfront as
a named structural element, before the zone it governs opens — this makes the catalog a
referenced contract rather than an inline instruction. C-23 is strongest when both exit
artifacts are declared upfront by name before any pass runs — the model knows from the
first block that two artifacts are required, not just one. C-24 is strongest when the
synthesis zone is architecturally evacuated: the preamble carries all instructions and
the zone is open space for model output, making it structurally impossible for instruction
content to coexist with the "no templates" prohibition inside the zone. All three
strengthen each other when encoded as skeleton: violating any one breaks the named-pass
sequence the model is explicitly following.

```
You are running /topic:plan for the topic named in the user's message.

This skill runs in three passes before any changes are proposed. The ordering is mandatory:
reading strategy content before completing Pass 1 contaminates the analysis by allowing
the strategy's dimensional framing to anchor what the signals reveal.

---

## STRUCTURAL DECLARATIONS

The following declarations govern this skill's entire lifecycle. They are stated before
any pass runs so every structural guarantee is verifiable from the opening block.

### PROHIBITION-REPAIR CATALOG (governs the Pass 1b synthesis zone)

PRC-01 — TEMPLATES AND STRUCTURED ELEMENTS
  Prohibition: No output templates, markdown tables, structured headers, bullet points,
    or bracketed instruction placeholders inside the synthesis zone.
  Detection trigger: Any markdown table row (| col |); any ## or ### heading; any
    * or - bullet; any element of the form [instruction text here].
  Repair action: Delete the element. Rewrite its content as a sentence in the paragraph.
    Log: write "REPAIR PRC-01: [element type] removed." before the rewritten sentence.

PRC-02 — STRATEGY REFERENCE
  Prohibition: No mention of strategy.md or any named strategy dimension inside the
    synthesis zone.
  Detection trigger: The string "strategy.md"; any dimension name from the strategy
    file used as an organizing label in the synthesis text.
  Repair action: Delete the sentence. Rewrite using only language from the artifact.
    Log: write "REPAIR PRC-02: strategy reference removed." before the rewritten sentence.

PRC-03 — CATEGORICAL STRUCTURE
  Prohibition: Do not break the synthesis into labeled sections by dimension or category.
  Detection trigger: More than one labeled paragraph; any paragraph opening with a
    category name as its organizing premise.
  Repair action: Remove labels. Merge into one continuous paragraph.
    Log: write "REPAIR PRC-03: merged to single paragraph." before the merged text.

### DUAL-GATE EXIT-ARTIFACT DECLARATION

This skill has two artifact-gated exits. Both are required before advancing.

GATE-1 — SYNTHESIS GATE (Pass 1b):
  Exit artifact: Synthesis paragraph — written prose, minimum 5 sentences, names at
    least 2 artifact filenames, PRC-01/PRC-02/PRC-03 audit complete.
  Advance condition: GATE-1 exit artifact exists. Strategy content is not read until
    this gate clears.

GATE-2 — CONFIRMATION GATE (Pass 3 → Apply):
  Exit artifact: Proposals table or explicit "NO CHANGES" statement.
  Advance condition: GATE-2 exit artifact exists. strategy.md is not modified until
    user confirms after reviewing this artifact.

---

## Pre-phase — Anchor the reference line (date only)

Read strategy.md. Extract its last-modified date. Write it here:

  STRATEGY DATE: [YYYY-MM-DD]

This date is the only thing you need from strategy.md right now.
Do not read the content. Close the file after recording the date.

If strategy.md does not exist: "No strategy.md found. Run /topic:new first." Stop.

---

## Pass 1 — Signal inventory and freeform synthesis (no strategy reference)

### 1a — Inventory

List every signal artifact in simulations/ matching the topic slug:

| Artifact filename | Artifact date | NEW / PRIOR |
|-------------------|---------------|-------------|
| [fill] | [fill] | NEW if > STRATEGY DATE, else PRIOR |

PRIOR artifacts are already reflected in strategy.md. Set them aside.

If no NEW artifacts: "No new signals since STRATEGY DATE. NO CHANGE." Stop.

---

### 1b — Synthesis zone preamble (instructions end before the zone opens)

Read every NEW artifact from Pass 1a. The preamble below contains everything you need
to write the synthesis. The synthesis zone that follows contains no additional
instructions — write based on this preamble alone.

WHAT TO WRITE: a freeform paragraph of 5 to 8 sentences about what the NEW signals
collectively reveal. One continuous paragraph of plain prose. Name at least two artifact
filenames in the text. Do not mention strategy.md. Do not organize by dimension names.

PROHIBITION-REPAIR CATALOG is in effect (PRC-01, PRC-02, PRC-03 — see Structural
Declarations above). Detect violations as you write. Apply repairs and log them.

SELF-MONITORING AUDIT: after writing, scan each sentence against PRC-01, PRC-02, PRC-03.
Apply any repair not yet logged. Write "SYNTHESIS AUDIT: clean." when all checks pass.

GATE-1 clears when: the synthesis paragraph exists in the zone, names at least two
artifacts, and SYNTHESIS AUDIT: clean is written.

**Stop. Do not read strategy.md content until GATE-1 is cleared. Halt here.**

—— SYNTHESIS PREAMBLE ENDS. Write synthesis paragraph in the zone below. ——

=== SYNTHESIS ZONE OPEN ===
=== SYNTHESIS ZONE CLOSE ===

—— GATE-1 clears when SYNTHESIS AUDIT: clean appears. Continue to Pass 2. ——

---

## Pass 2 — Structured strategy comparison

GATE-1 cleared. Now read strategy.md fully.

### 2a — Strategy commitments

| Strategy element | Content |
|------------------|---------|
| Declared stage | |
| Namespaces covered | |
| Skills planned | |
| Stated rationale | |
| Acknowledged gaps | |
| Unstated assumptions | [at least one — most important for delta detection] |

The "Unstated assumptions" row is the highest-value delta candidate: every unstated
assumption is a delta the strategy cannot defend.

---

### 2b — Dimension coverage map

For every strategy dimension, one row. For every dimension the Pass 1 synthesis
identified not in strategy.md, one row marked [NEW DIMENSION]:

| Dimension | In strategy.md | Signal coverage | Assessment | Primary artifact |
|-----------|---------------|-----------------|------------|------------------|
| [fill] | YES | COVERED / GAP | VALIDATED / CHALLENGED / NOT COVERED | [filename] |
| [new dim] [NEW DIMENSION] | NO | NEW | — | [filename] |

---

### 2c — Novelty gate

A dimension is CONFIRMED NEW only if both conditions are true:
1. Present in at least one NEW artifact (date > STRATEGY DATE)
2. Absent from strategy.md

Annotate each [NEW DIMENSION] row: "CONFIRMED NEW" or "PRIOR-ONLY — not a delta."
PRIOR-ONLY dimensions cannot serve as evidence for ADD proposals.

---

### 2d — Delta findings

| Finding ID | Strategy assumed | Signal revealed | Source artifact |
|-----------|-----------------|----------------|-----------------|
| F-01 | [what strategy said or implicitly committed to] | [what NEW artifact showed] | [filename] |

Null case: `F-00 | Strategy confirmed | No new findings | All NEW artifacts` — skip to Confirmation Gate.

---

## Pass 3 — Proposals

The default outcome is NO CHANGE. Only propose a change if it clearly beats doing nothing.

| # | Action | Dimension | Evidence artifact | Before | After | Confidence | vs. NO CHANGE |
|---|--------|-----------|-------------------|--------|-------|------------|---------------|
| [fill] | ADD / REMOVE / REPRIORITIZE | [fill — [NEW] if new] | [filename] | [fill] | [fill] | HIGH / MED / LOW | [fill] |

Requirements before proceeding:
- [ ] All three action types (ADD, REMOVE, REPRIORITIZE) present, or each absent type
      has an explicit NULL row: "| — | [TYPE] | No proposals | N/A | — | — | — | — |"
- [ ] Every CONFIRMED NEW dimension either appears as ADD or is explicitly excluded with reason
- [ ] Every REPRIORITIZE row shows numeric before and after ranks
- [ ] Every evidence artifact is from the NEW list (date > STRATEGY DATE)

If no changes are warranted: "NO CHANGES — new signals validate existing strategy."

---

## Confirmation gate (GATE-2 EXIT ARTIFACT: proposals table or NO CHANGES statement)

Present the 2b coverage map, 2d delta findings, and Pass 3 proposals.

The Pass 3 proposals table (or the "NO CHANGES" statement) is the GATE-2 EXIT ARTIFACT.
The confirmation prompt is not issued until GATE-2 EXIT ARTIFACT exists.

Write:
"PENDING — strategy.md has not been modified.
 Proposed: [N] additions / [N] removals / [N] reprioritizations
 Reply YES to apply | NO to discard | REVISED + edited table to apply custom version"

**Stop. Do not write to strategy.md. Do not modify any file. Halt here.**

Wait for the user's reply.

---

## Apply phase (triggered by YES or REVISED)

Write exactly the confirmed changes to strategy.md. Do not reformat unchanged sections.

"strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## Round 7 Variation Summary

| Variation | Primary axis | C-22 mechanism | C-23 mechanism | C-24 mechanism |
|-----------|-------------|----------------|----------------|----------------|
| V-01 | Lifecycle emphasis | PROHIBITION-REPAIR CATALOG block (PR-01/PR-02/PR-03) before synthesis zone; PROHIBITION AUDIT names completion | Phase 2 EXIT ARTIFACT (synthesis paragraph) + Confirmation Gate EXIT ARTIFACT (proposals table) | Catalog precedes zone; synthesis zone has instruction text but no bracketed fill-ins |
| V-02 | Output format | Prohibition-repair pairs in synthesis preamble block; preamble explicitly ends before zone open marker | Block 2 EXIT ARTIFACT (filled zone content) + PENDING CONFIRMATION banner | Architecturally evacuated zone: preamble carries all instructions; zone itself contains nothing until model writes |
| V-03 | Phrasing register | Inline RECOVERY SCRIPT (Rule A/B/C) immediately follows each prohibition; detection trigger + correction step co-located at prohibition site | SYNTHESIS TEXT: complete (synthesis gate) + filled proposals table EXIT TOKEN (confirmation gate) | Plain instruction text only; no bracketed fill-in placeholders anywhere in synthesis rules |
| V-04 | Inertia framing + role sequence | TERRAIN RULES with motivated prohibitions (R-01/R-02/R-03) + COMPLIANCE AUDIT checklist as gate condition; repair is a precondition to advance | EVIDENCE SUMMARY as evidentiary prior + proposals table as EXIT ARTIFACT | EVIDENCE-ONLY TERRAIN block carries all rules; no fill-in placeholders in terrain instructions |
| V-05 | Combined (C-22+C-23+C-24+prior skeleton) | PROHIBITION-REPAIR CATALOG declared upfront as named structural primitive before any pass | DUAL-GATE EXIT-ARTIFACT DECLARATION upfront naming both artifacts before Pass 1 | Architecturally evacuated synthesis zone as skeleton element; preamble carries all instructions |

**C-22 strategy distribution:**

- V-01 and V-05 use a named catalog as a referenced contract; the model audits against
  a bounded set of named entries. Strongest for completeness: the model knows PR-01,
  PR-02, PR-03 are the full set.
- V-04 adds motivational grounding and embeds repair as a gate condition (COMPLIANCE AUDIT
  must be written before advancing), making C-22 compliance structurally enforced.
- V-02 uses preamble-embedded pairs, architecturally aligned with the evacuated zone design.
- V-03 uses inline recovery scripts at the prohibition site — most local pairing, but
  recovery is observable in model output (REPAIR A/B/C tags appear in the output stream).

**C-24 strategy distribution:**

- V-02 and V-05 use fully evacuated zones: all instruction content in a preamble block
  that explicitly ends, then zone markers enclose only model output. Strongest architectural
  enforcement.
- V-01 and V-04 use instruction text (not bracketed fill-ins) in the synthesis section.
  The prohibition exists; the structure does not model the prohibited form.
- V-03 uses plain imperative text with no zone markers and no placeholders.

**Structural risk ranking** (lowest risk of C-22/C-23/C-24 failure first):
V-05 > V-01 > V-04 > V-02 > V-03

V-05 encodes all three new criteria as named skeleton elements declared upfront — violating
any one breaks the declared contract from the first block. V-03's inline recovery scripts
are strongest at the prohibition site but weakest in catalog completeness if the auditor
checks whether every prohibition has a detection trigger.

**Predicted discriminator:** C-22 will discriminate on whether each variation accounts
for ALL structural prohibitions in the synthesis phase (PR-01/PR-02/PR-03 all paired),
not just the template prohibition that C-20 already required. A variation that pairs
the template prohibition but leaves the strategy-reference or categorical-structure
prohibitions without explicit detection triggers will receive partial credit on C-22.
C-24 will discriminate on V-01 and V-04 if the auditor reads any parenthetical or
conditional instruction text within the synthesis section as modeling the fill-in form.

```json
{"variation_count": 5, "rubric_version": "v7", "ceiling": 142, "new_criteria": ["C-22", "C-23", "C-24"], "primary_discriminator": "C-22 completeness — all prohibitions paired vs. only template prohibition", "secondary_discriminator": "C-24 — instruction text inside synthesis zone vs. architecturally evacuated zone"}
```
