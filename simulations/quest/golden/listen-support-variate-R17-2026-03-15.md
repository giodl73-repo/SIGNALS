# listen-support Round 17 — Skill Body Prompt Variations

**Date:** 2026-03-15
**Rubric target:** v16 (295 pts ceiling — C-47, C-48, C-49 introduced)
**Base:** V-05 R16 (295/295 under v16 — all C-01 through C-49 at ceiling)

**Variation axes selected** (3 single-axis, then 2 combined):
1. **Output format** — Sub-check 3 prose replaced with a structured 4-column table; row count is self-verifying without parsing sentence structure (V-01)
2. **Lifecycle emphasis** — Entry 3 gains a dedicated `Trigger event:` field naming the specific post-commitment workflow action that surfaces the Phase 2 barrier; Sub-check 2 must quote it (V-02)
3. **Inertia framing** — Entry 3 `Prohibited:` sentinel moved from Entry-specific guidance section into the Entry 3 template body as a field-adjacent guard (V-03)
4. **V-01 + V-02 combined** — Table Sub-check 3 + trigger-event field in Entry 3 + Sub-check 2 trigger quote (V-04)
5. **Full synthesis** — All three axes: table Sub-check 3 + trigger-event field + per-template Prohibited: sentinel (V-05)

**R17 criterion hypothesis matrix:**

| Criterion candidate | V-01 | V-02 | V-03 | V-04 | V-05 |
|--------------------|------|------|------|------|------|
| C-01 through C-49 (all prior — 295 pt ceiling) | YES | YES | YES | YES | YES |
| C-50 candidate: Sub-check 3 Table Format | YES | — | — | YES | YES |
| C-51 candidate: Phase-2 Barrier Trigger-Event Field | — | YES | — | YES | YES |
| C-52 candidate: Per-Template Prohibited: Sentinel in Entry 3 | — | — | YES | — | YES |

---

## V-01: Single-Axis — Output Format (Sub-check 3 Table Format)

**Axis:** Output format — Sub-check 3 post-generation phase distribution re-verification. V-05 R16 uses a prose block ("Phase 1 bodies generated: [n]. Committed (Step 5): [n]...") with MATCH/MISMATCH embedded in a sentence. V-01 R17 replaces this with a 4-column structured table: one row per phase plus a total row. Column headers: Phase / Bodies generated / Committed (Step 5) / Step 1 target / Match. All other mechanisms from V-05 R16 are preserved exactly.

**Probe (C-50 candidate):** V-05 R16 satisfies C-48 by requiring Sub-check 3 with per-phase count comparison post-generation. The failure mode C-48 leaves open: the prose form allows a model to collapse multiple phases into a single sentence ("Phase 1 and Phase 2 both match — 3 bodies each") without producing independently verifiable per-phase rows. A table with one row per phase closes this: row count is checkable by counting rows, not by parsing sentence structure. A MISMATCH in one phase is visible as a cell value without reading the surrounding prose. The C-50 probe tests whether a table-format Sub-check 3 produces a qualitatively different structural gate than the prose form C-48 already requires.

**Hypothesis:** C-48 closes the generation-drift detection window but does not constrain the format of the verification output. A prose Sub-check 3 with embedded MATCH/MISMATCH verdicts can be satisfied by a model that generates one sentence spanning all three phases, which a scorer must parse carefully to extract per-phase results. A table row per phase makes each phase independently auditable: a scorer counts rows and reads cells. This structural independence is the same property C-15 introduced for the coverage trace table. The C-50 probe tests whether the table format for Sub-check 3 is independently extractable as a criterion from the generation-drift detection requirement C-48 already imposes.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- PHASE DISTRIBUTION TARGET (declared before STATUS QUO analysis)

Before establishing the STATUS QUO baseline, declare the target ticket distribution.

PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0–30): [N] tickets
  Phase 2 (Day 31–60): [N] tickets
  Phase 3 (Day 61–90): [N] tickets
  Total: [N] tickets

Constraint: Phase 1 count ≥ 2. Phase 3 count ≥ 1. All three phases represented.
This target will be referenced at Step 5 (committed block) and re-verified at Step 5B
and Pass 2 Part C Sub-check 3.

---

## STEP 1B -- INERTIA: STATUS QUO

**1b-i. Current-state baseline**
Describe in 2-3 sentences: what are users doing today? Frame with awareness of
the Phase Distribution Target — the baseline must generate friction across all three
phase windows.

**1b-ii. Inertia competitor declaration**
INERTIA COMPETITOR: [product name]
Prohibited: any non-grep-checkable phrase.

**1b-iii. Adoption-curve context**
Confirm consistency with the Phase Distribution Target.

---

## STEP 2 -- PHASE MAP TABLE

| Phase | Window | Expected severity range | Expected volume character |
|-------|--------|------------------------|--------------------------|
| Phase 1 | Day 0–30 | P2/P3 | high |
| Phase 2 | Day 31–60 | P1/P2 | medium |
| Phase 3 | Day 61–90 | P0/P1 | medium/low |

---

## STEP 2B -- PHASE BODY TEMPLATE TABLE

| Phase | Adoption stance | Template sentence |
|-------|----------------|-------------------|
| Phase 1 | Dual-tool tension | "I still have [INERTIA COMPETITOR] open in another tab — I keep switching back to check how it handled [specific scenario]." |
| Phase 3 | Parity gap | "In [INERTIA COMPETITOR] I could [specific action] without leaving this screen; here I cannot." |

Phase 1 and Phase 3 bodies: open with the template sentence, placeholders filled concretely.
Phase 2 bodies: reference the competitor where natural.

---

## STEP 2C -- PHASE-SEVERITY INFERENCE RULE

Phase 1 (Day 0–30): P2/P3 non-outage. Fallback available; user is learning.
Phase 3 (Day 61–90): P1/P0 blocking. No fallback; user committed and blocked.

Violation conditions:
- Phase 1 P0/P1 non-outage: violation — correct to P2/P3.
- Phase 3 P3 blocking: violation — correct to P1/P0.

INFERENCE RULE (stated): [your paraphrase of the directional rule above]
Applied in: Steps 5, 5B, and Pass 2 INFERENCE AUDIT

Do not proceed until filled with your own-words paraphrase.

---

## STEP 3 -- ROLE ACTIVATION ORDER (SRE-FIRST)

Activate roles: SRE → Support → PM → UX → C-01 through C-12.

[SRE] — First. Operational failure modes: configuration errors, deployment issues,
on-call escalation, infrastructure-level P0/P1 candidates. Identify Phase 2 escalation
patterns (transition-zone operational friction that surfaces after partial commitment).

[Support] — Second. Triage-queue patterns, documentation gaps, error messages.

[PM] — Third. Intent gaps, roadmap items, feature-request backlog.

[UX] — Fourth. Discoverability failures, onboarding friction, how-to patterns.

[C-01 through C-12] — One ticket hypothesis each. Frame each with phase awareness:
  "In which phase (1, 2, or 3) will this persona most likely encounter this issue?"

---

## STEP 4 -- PERFORMANCE MODE DECLARATION

**You ARE the persona named on each ticket card.**

Your previous primary workflow used [INERTIA COMPETITOR — product name from Step 1b-ii].
Phase 1: old tool still open, can fall back — lower stakes.
Phase 3: committed to new tool, no fallback — higher stakes.

Do not write "the user", "they", "the SRE", "the PM", "the engineer",
or any named-role title in third person.

Prohibited verb-subject forms: "the SRE ran", "the PM reviewed", "the engineer observed",
"the C-07 clicked", "the Support agent opened", or any role-title-preceding-a-verb form.

**Every action in this ticket was taken by "I".
Every old-tool reference uses the product name from Step 1b-ii.**

---

## STEP 5 -- VOCABULARY PRE-COMMITMENT TABLE

Competitor in scope: [product name from Step 1b-ii]

Do not fill any cell in the table until all three items are written:

Required item 1 — INFERENCE RULE (confirmed):
[restate in your own words]

Required item 2 — Verbatim from 2C:
[copy exact first sentence from INFERENCE RULE (stated) at Step 2C — word for word, do not paraphrase]

Required item 3 — PHASE DISTRIBUTION committed block:
Reconcile with Phase Distribution Target from Step 1.
  Phase 1 (Day 0–30): [N] tickets (Step 1 target: [N])
  Phase 2 (Day 31–60): [N] tickets (Step 1 target: [N])
  Phase 3 (Day 61–90): [N] tickets (Step 1 target: [N])
  Total: [N] tickets

Confirmation: this rule applies to every severity assignment in the table below.

| Ticket ID | Phase | Category | Persona | Volume | Severity |
|-----------|-------|----------|---------|--------|----------|
| T-01 | | | | | |
| T-02 | | | | | |
| T-03 | | | | | |
| T-04 | | | | | |
| T-05 | | | | | |
| T-06 | | | | | |
| T-07 | | | | | |
| T-08 | | | | | |

Allowed: Category {how-to, bug, feature-request, config, integration}, Volume {high, medium, low}, Severity {P0, P1, P2, P3}.
**Lock vocabulary values here. Full card bodies follow in Step 6.**

---

## STEP 5B -- COLLECTIVE DISTRIBUTION AUDIT

Constraint 0: Phase counts must match Step 5 committed block.
State: "Phase 1: [n] committed, [n] actual — MATCH/MISMATCH."
Also cross-check against Step 1 target: "Step 1 target vs Step 5 committed: [match/mismatch per phase]."

1. Phase distribution — ≥2 Phase 1, ≥1 Phase 3.
2. Category spread — ≥3 distinct categories.
3. Volume distribution — all three levels.
4. Phase-character compliance — severity/volume match Step 2.
5. Inference-rule compliance — Phase 1/Phase 3 violation scan.

**If any fails, correct and re-run.**

---

## STEP 5C -- PRE-BODY STRUCTURAL VERIFICATION (PASS 2B)

Item 1 — Category distribution check.
Item 2 — Persona distribution check.
Item 3 — Phase distribution compliance.

Item 4 — SWITCHING-FRICTION COUNT CHECK:
SWITCHING-FRICTION COUNT: [N]
N must be ≥ 3. Do not proceed to Step 6 if N < 3.
Third entry must cover a Phase 2 migration barrier (surfaces after partial commitment,
not on day one).

---

## STEP 6 -- FULL CARD BODIES (PHASE-ORGANIZED)

Organize by phase window. Complete all Phase 1 cards, then Phase 2, then Phase 3.
Within each group, ascending Ticket ID order.

### Phase 1 Cards (Day 0–30)

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [match Step 5]
Persona: [match Step 5]
Volume: [match Step 5]
Severity: [match Step 5 — P2 or P3]

Body:
[Open with Phase 1 template sentence, all placeholders filled with the inertia competitor
product name and a concrete scenario. Reference the STATUS QUO element that drives this
ticket's volume. No third-person. Every old-tool reference: product name from Step 1b-ii.]

---

### Phase 2 Cards (Day 31–60)

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [match Step 5]
Persona: [match Step 5]
Volume: [match Step 5]
Severity: [match Step 5 — P1 or P2]

Body:
[Transition framing — user is partially committed, not yet fully detached. Reference the
competitor where the framing naturally calls for it. Reference the STATUS QUO element
from Step 1b-i. No third-person. Product name for old tool.]

---

### Phase 3 Cards (Day 61–90)

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [match Step 5]
Persona: [match Step 5]
Volume: [match Step 5]
Severity: [match Step 5 — P0 or P1]

Body:
[Open with Phase 3 template sentence, all placeholders filled concretely. Reference the
STATUS QUO element that drives this ticket's severity — the user committed fully; the
competitor is not accessible for this workflow. No third-person. Product name for old tool.]

---

## STEP 7 -- CROSS-TICKET PATTERNS

Pattern name: [short name]
Tickets affected: [T-NN, ...]
Root cause: [one sentence]

Consequence — Affected segment:
Prohibited: "users in general", "the team", any unnamed group.
[Named role or cohort tied specifically to this pattern]

Consequence — Day-90 scenario:
Prohibited: "this will cause confusion", any non-pattern-specific event.
[One specific event that occurs if unaddressed by Day 90]

Consequence — Adoption cost:
Prohibited: generic friction not specific to this cohort.
[One sentence quantifying friction for the named segment]

If a pattern involves migration from the inertia competitor, name the competitor.

---

## STEP 8 -- GAP ANALYSIS

### Doc Gaps
[At least one documentation gap.]

### Design Gaps
[At least one design gap.]

### Operational Gaps
[At least one operational gap.]

### Switching-Friction Gaps

Dedicated sub-section for migration barriers only. NOT absorbed into the three sections above.
The three sections above remain present and non-empty.

SWITCHING-FRICTION COUNT: [N]
N must be ≥ 3. State this count before writing any entry.

Switching-friction gap: [short name]
Migrating from: [product name from Step 1b-ii — verbatim, grep-checkable]
Expected behavior: [one sentence]
Actual behavior: [one sentence]
Migration impact: [one sentence]

Entry-specific guidance:
- Entry 1: Cover the primary day-one migration friction (Phase 1 ticket driver).
- Entry 2: Cover the second most prominent migration barrier.
- Entry 3: Cover a Phase 2 migration barrier — a friction that only surfaces after
  partial commitment, when the user has started migrating workflows but not fully
  detached from the competitor. Prohibited: a barrier that day-one users would
  also encounter (that belongs in entries 1 or 2).

### Pre-Launch Priority
Name the single gap to close first. Tie to specific Ticket IDs, severity, and volume.
State whether it reduces switching-friction for inertia-competitor migrants.

---

## STEP 9 -- DUAL-PASS VERIFICATION

### PASS 1 -- Coverage Trace Table

| Ticket ID | STATUS QUO element referenced | Gap traced to |
|-----------|-------------------------------|---------------|

Populate one row per ticket, in Ticket ID order.

After completing:
1. Confirm: "No gap from the Gap Analysis — including switching-friction gaps — is absent."
2. Confirm: "Inertia competitor product name appears in at least two STATUS QUO element cells."

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 -- Properties Verify + Inference Audit

**PART A — Frontmatter Verify**
Confirm Step 5 matches Step 6 for all fields.
State: "All Step 5 values match Step 6 card bodies."

**PART B — Property Checks**

1. Tool-name fidelity.
   State: "[PRODUCT NAME] in Step 1b-ii: YES. Card bodies: [T-NN, T-NN min].
   Migrating from: field: YES."

2. Phase-differentiated templates.
   State: "Phase 1 template in: [T-NN, T-NN]. Phase 3 template in: [T-NN]."

3. Switching-friction 4-field format.
   State: "All four fields present in all entries: YES / NO."

**PART C — Inference Audit**

**Sub-check 1: Phase-Architecture Severity Compliance**

Scan Phase 1 cards (Phase 1 section, Step 6). Exception sign-off for any P0/P1, or:
"No Phase 1 P0/P1 exceptions. Phase 1 lifecycle: fallback available.
Governing paraphrase clause: [copy the exact Phase 1 clause from INFERENCE RULE (stated)
at Step 2C — do not paraphrase, do not summarize, copy it verbatim word-for-word]."

Scan Phase 2 cards (Phase 2 section, Step 6). Exception sign-off for any P0 escalation, or:
"No Phase 2 P0 escalation exceptions. Phase 2 lifecycle: transition (partial fallback).
Governing paraphrase clause: [copy the exact Phase 2 clause from INFERENCE RULE (stated)
at Step 2C — do not paraphrase, do not summarize, copy it verbatim word-for-word]."

Scan Phase 3 cards (Phase 3 section, Step 6). Exception sign-off for any P3, or:
"No Phase 3 P3 exceptions. Phase 3 lifecycle: no fallback.
Governing paraphrase clause: [copy the exact Phase 3 clause from INFERENCE RULE (stated)
at Step 2C — do not paraphrase, do not summarize, copy it verbatim word-for-word]."

Paraphrase consistency confirmation:
State: "INFERENCE RULE paraphrase (Step 2C): [first 10 words].
Verbatim anchor at Step 5: YES.
All three phase Paraphrase clause fields: triple-clause verbatim (do not paraphrase,
do not summarize, copy it verbatim word-for-word): YES.
Phase 1 compliance: PASS/FAIL.
Phase 2 within P1/P2 range: PASS/FAIL.
Phase 3 compliance: PASS/FAIL.
Paraphrase consistent with audit results: YES / NO."

**Sub-check 2: Switching-Friction Sub-Section Field Completeness**

Restate count: "SWITCHING-FRICTION COUNT: [N]. N ≥ 3: YES/NO."
List each entry's `Migrating from:` value. Flag any non-verbatim.
State: "Sub-section present: YES. All Migrating from: fields verbatim: YES / NO.
Third entry covers Phase 2 migration barrier (not day-one friction): YES / NO."

**Sub-check 3: Post-Generation Phase Distribution Re-Verification**

Count Phase 1, Phase 2, Phase 3 card bodies in Step 6 phase sections.
Complete the table:

| Phase | Bodies generated | Committed (Step 5) | Step 1 target | Match |
|-------|-----------------|-------------------|---------------|-------|
| Phase 1 | [n] | [n] | [n] | MATCH/MISMATCH |
| Phase 2 | [n] | [n] | [n] | MATCH/MISMATCH |
| Phase 3 | [n] | [n] | [n] | MATCH/MISMATCH |
| Total | [n] | [n] | [n] | MATCH/MISMATCH |

If any row shows MISMATCH: name the discrepancy, identify the Ticket ID that drifted
from its committed phase, and state the correction needed. A row-level MISMATCH here
means the pre-generation constraint was satisfied (5B passed) but generation-time drift
occurred — flag explicitly by row.

State final:
"All Step 5 values match Step 6.
Exception sign-offs complete for Phase 1, Phase 2, and Phase 3 scans.
SWITCHING-FRICTION COUNT ≥ 3 confirmed. Third entry covers Phase 2 barrier: YES.
Post-generation phase distribution table complete. All rows: MATCH.
Sub-checks 1, 2, and 3 verified. All C-01 through C-49 constraints met.
C-50 probe (Sub-check 3 table format): complete."
```

---

## V-02: Single-Axis — Lifecycle Emphasis (Phase-2 Barrier Trigger-Event Field)

**Axis:** Lifecycle emphasis — Entry 3 of the switching-friction sub-section. V-05 R16 requires Entry 3 to cover a Phase 2 migration barrier and Sub-check 2 confirms this with a YES/NO claim. V-02 R17 adds a dedicated `Trigger event:` field to the Entry 3 template, requiring the model to name the specific post-commitment workflow action that first surfaces the barrier. Sub-check 2 is extended to quote this trigger event verbatim. All other mechanisms from V-05 R16 are preserved exactly.

**Probe (C-51 candidate):** V-05 R16 satisfies C-49 by requiring SWITCHING-FRICTION COUNT ≥ 3, a third-entry type constraint, and Sub-check 2 confirming "Third entry covers Phase 2 migration barrier (not day-one friction): YES / NO." The failure mode C-49 leaves open: the YES/NO confirmation is declarative — a model writes YES without supplying evidence. A Surface-compliant entry can claim Phase-2-ness ("this friction surfaces after the user has begun migrating") without naming what specific workflow action triggers it. The distinction between a day-one barrier and a Phase-2 barrier is precisely the post-commitment trigger: a specific action the user takes after partial commitment that day-one users never reach. Adding a `Trigger event:` field forces the model to name this action as a standalone structural property, not as prose embedded in `Expected behavior:` or `Actual behavior:`. Sub-check 2 must quote the field verbatim, making the claim verifiable at a field-content level rather than a YES/NO level.

**Hypothesis:** C-49 imposes a type constraint on Entry 3 (Phase-2 barrier, not day-one) and requires Sub-check 2 to confirm it. The confirmation is YES/NO with no evidence requirement. A `Trigger event:` field names the post-commitment event that distinguishes Phase-2 barriers from day-one barriers at the structural level: if the trigger is a day-one action, the field value itself fails the constraint without requiring the scorer to evaluate surrounding prose. The C-51 probe tests whether the trigger-event field is independently extractable as a criterion separating evidence-backed Phase-2 barrier confirmation from the declarative YES/NO form C-49 already requires.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- PHASE DISTRIBUTION TARGET (declared before STATUS QUO analysis)

Before establishing the STATUS QUO baseline, declare the target ticket distribution.

PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0–30): [N] tickets
  Phase 2 (Day 31–60): [N] tickets
  Phase 3 (Day 61–90): [N] tickets
  Total: [N] tickets

Constraint: Phase 1 count ≥ 2. Phase 3 count ≥ 1. All three phases represented.
This target will be referenced at Step 5 (committed block) and re-verified at Step 5B
and Pass 2 Part C Sub-check 3.

---

## STEP 1B -- INERTIA: STATUS QUO

**1b-i. Current-state baseline**
Describe in 2-3 sentences: what are users doing today? Frame with awareness of
the Phase Distribution Target — the baseline must generate friction across all three
phase windows.

**1b-ii. Inertia competitor declaration**
INERTIA COMPETITOR: [product name]
Prohibited: any non-grep-checkable phrase.

**1b-iii. Adoption-curve context**
Confirm consistency with the Phase Distribution Target.

---

## STEP 2 -- PHASE MAP TABLE

| Phase | Window | Expected severity range | Expected volume character |
|-------|--------|------------------------|--------------------------|
| Phase 1 | Day 0–30 | P2/P3 | high |
| Phase 2 | Day 31–60 | P1/P2 | medium |
| Phase 3 | Day 61–90 | P0/P1 | medium/low |

---

## STEP 2B -- PHASE BODY TEMPLATE TABLE

| Phase | Adoption stance | Template sentence |
|-------|----------------|-------------------|
| Phase 1 | Dual-tool tension | "I still have [INERTIA COMPETITOR] open in another tab — I keep switching back to check how it handled [specific scenario]." |
| Phase 3 | Parity gap | "In [INERTIA COMPETITOR] I could [specific action] without leaving this screen; here I cannot." |

Phase 1 and Phase 3 bodies: open with the template sentence, placeholders filled concretely.
Phase 2 bodies: reference the competitor where natural.

---

## STEP 2C -- PHASE-SEVERITY INFERENCE RULE

Phase 1 (Day 0–30): P2/P3 non-outage. Fallback available; user is learning.
Phase 3 (Day 61–90): P1/P0 blocking. No fallback; user committed and blocked.

Violation conditions:
- Phase 1 P0/P1 non-outage: violation — correct to P2/P3.
- Phase 3 P3 blocking: violation — correct to P1/P0.

INFERENCE RULE (stated): [your paraphrase of the directional rule above]
Applied in: Steps 5, 5B, and Pass 2 INFERENCE AUDIT

Do not proceed until filled with your own-words paraphrase.

---

## STEP 3 -- ROLE ACTIVATION ORDER (SRE-FIRST)

Activate roles: SRE → Support → PM → UX → C-01 through C-12.

[SRE] — First. Operational failure modes: configuration errors, deployment issues,
on-call escalation, infrastructure-level P0/P1 candidates. Identify Phase 2 escalation
patterns (transition-zone operational friction that surfaces after partial commitment).

[Support] — Second. Triage-queue patterns, documentation gaps, error messages.

[PM] — Third. Intent gaps, roadmap items, feature-request backlog.

[UX] — Fourth. Discoverability failures, onboarding friction, how-to patterns.

[C-01 through C-12] — One ticket hypothesis each. Frame each with phase awareness:
  "In which phase (1, 2, or 3) will this persona most likely encounter this issue?"

---

## STEP 4 -- PERFORMANCE MODE DECLARATION

**You ARE the persona named on each ticket card.**

Your previous primary workflow used [INERTIA COMPETITOR — product name from Step 1b-ii].
Phase 1: old tool still open, can fall back — lower stakes.
Phase 3: committed to new tool, no fallback — higher stakes.

Do not write "the user", "they", "the SRE", "the PM", "the engineer",
or any named-role title in third person.

Prohibited verb-subject forms: "the SRE ran", "the PM reviewed", "the engineer observed",
"the C-07 clicked", "the Support agent opened", or any role-title-preceding-a-verb form.

**Every action in this ticket was taken by "I".
Every old-tool reference uses the product name from Step 1b-ii.**

---

## STEP 5 -- VOCABULARY PRE-COMMITMENT TABLE

Competitor in scope: [product name from Step 1b-ii]

Do not fill any cell in the table until all three items are written:

Required item 1 — INFERENCE RULE (confirmed):
[restate in your own words]

Required item 2 — Verbatim from 2C:
[copy exact first sentence from INFERENCE RULE (stated) at Step 2C — word for word, do not paraphrase]

Required item 3 — PHASE DISTRIBUTION committed block:
Reconcile with Phase Distribution Target from Step 1.
  Phase 1 (Day 0–30): [N] tickets (Step 1 target: [N])
  Phase 2 (Day 31–60): [N] tickets (Step 1 target: [N])
  Phase 3 (Day 61–90): [N] tickets (Step 1 target: [N])
  Total: [N] tickets

Confirmation: this rule applies to every severity assignment in the table below.

| Ticket ID | Phase | Category | Persona | Volume | Severity |
|-----------|-------|----------|---------|--------|----------|
| T-01 | | | | | |
| T-02 | | | | | |
| T-03 | | | | | |
| T-04 | | | | | |
| T-05 | | | | | |
| T-06 | | | | | |
| T-07 | | | | | |
| T-08 | | | | | |

Allowed: Category {how-to, bug, feature-request, config, integration}, Volume {high, medium, low}, Severity {P0, P1, P2, P3}.
**Lock vocabulary values here. Full card bodies follow in Step 6.**

---

## STEP 5B -- COLLECTIVE DISTRIBUTION AUDIT

Constraint 0: Phase counts must match Step 5 committed block.
State: "Phase 1: [n] committed, [n] actual — MATCH/MISMATCH."
Also cross-check against Step 1 target: "Step 1 target vs Step 5 committed: [match/mismatch per phase]."

1. Phase distribution — ≥2 Phase 1, ≥1 Phase 3.
2. Category spread — ≥3 distinct categories.
3. Volume distribution — all three levels.
4. Phase-character compliance — severity/volume match Step 2.
5. Inference-rule compliance — Phase 1/Phase 3 violation scan.

**If any fails, correct and re-run.**

---

## STEP 5C -- PRE-BODY STRUCTURAL VERIFICATION (PASS 2B)

Item 1 — Category distribution check.
Item 2 — Persona distribution check.
Item 3 — Phase distribution compliance.

Item 4 — SWITCHING-FRICTION COUNT CHECK:
SWITCHING-FRICTION COUNT: [N]
N must be ≥ 3. Do not proceed to Step 6 if N < 3.
Third entry must cover a Phase 2 migration barrier (surfaces after partial commitment,
not on day one).

---

## STEP 6 -- FULL CARD BODIES (PHASE-ORGANIZED)

Organize by phase window. Complete all Phase 1 cards, then Phase 2, then Phase 3.
Within each group, ascending Ticket ID order.

### Phase 1 Cards (Day 0–30)

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [match Step 5]
Persona: [match Step 5]
Volume: [match Step 5]
Severity: [match Step 5 — P2 or P3]

Body:
[Open with Phase 1 template sentence, all placeholders filled with the inertia competitor
product name and a concrete scenario. Reference the STATUS QUO element that drives this
ticket's volume. No third-person. Every old-tool reference: product name from Step 1b-ii.]

---

### Phase 2 Cards (Day 31–60)

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [match Step 5]
Persona: [match Step 5]
Volume: [match Step 5]
Severity: [match Step 5 — P1 or P2]

Body:
[Transition framing — user is partially committed, not yet fully detached. Reference the
competitor where the framing naturally calls for it. Reference the STATUS QUO element
from Step 1b-i. No third-person. Product name for old tool.]

---

### Phase 3 Cards (Day 61–90)

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [match Step 5]
Persona: [match Step 5]
Volume: [match Step 5]
Severity: [match Step 5 — P0 or P1]

Body:
[Open with Phase 3 template sentence, all placeholders filled concretely. Reference the
STATUS QUO element that drives this ticket's severity — the user committed fully; the
competitor is not accessible for this workflow. No third-person. Product name for old tool.]

---

## STEP 7 -- CROSS-TICKET PATTERNS

Pattern name: [short name]
Tickets affected: [T-NN, ...]
Root cause: [one sentence]

Consequence — Affected segment:
Prohibited: "users in general", "the team", any unnamed group.
[Named role or cohort tied specifically to this pattern]

Consequence — Day-90 scenario:
Prohibited: "this will cause confusion", any non-pattern-specific event.
[One specific event that occurs if unaddressed by Day 90]

Consequence — Adoption cost:
Prohibited: generic friction not specific to this cohort.
[One sentence quantifying friction for the named segment]

If a pattern involves migration from the inertia competitor, name the competitor.

---

## STEP 8 -- GAP ANALYSIS

### Doc Gaps
[At least one documentation gap.]

### Design Gaps
[At least one design gap.]

### Operational Gaps
[At least one operational gap.]

### Switching-Friction Gaps

Dedicated sub-section for migration barriers only. NOT absorbed into the three sections above.
The three sections above remain present and non-empty.

SWITCHING-FRICTION COUNT: [N]
N must be ≥ 3. State this count before writing any entry.

Template for Entries 1 and 2:

Switching-friction gap: [short name]
Migrating from: [product name from Step 1b-ii — verbatim, grep-checkable]
Expected behavior: [one sentence]
Actual behavior: [one sentence]
Migration impact: [one sentence]

Template for Entry 3 (Phase 2 barrier — extended template):

Switching-friction gap: [short name]
Migrating from: [product name from Step 1b-ii — verbatim, grep-checkable]
Trigger event: [name the specific workflow action or system state that first surfaces
  this barrier after partial commitment — must name a concrete post-commitment event
  that day-one users do not reach on first contact]
Expected behavior: [one sentence]
Actual behavior: [one sentence]
Migration impact: [one sentence]

Entry-specific guidance:
- Entry 1: Cover the primary day-one migration friction (Phase 1 ticket driver).
- Entry 2: Cover the second most prominent migration barrier.
- Entry 3: Use the extended template. The Trigger event field must name the specific
  post-commitment workflow action. Prohibited: a barrier that day-one users would also
  encounter (that belongs in entries 1 or 2).

### Pre-Launch Priority
Name the single gap to close first. Tie to specific Ticket IDs, severity, and volume.
State whether it reduces switching-friction for inertia-competitor migrants.

---

## STEP 9 -- DUAL-PASS VERIFICATION

### PASS 1 -- Coverage Trace Table

| Ticket ID | STATUS QUO element referenced | Gap traced to |
|-----------|-------------------------------|---------------|

Populate one row per ticket, in Ticket ID order.

After completing:
1. Confirm: "No gap from the Gap Analysis — including switching-friction gaps — is absent."
2. Confirm: "Inertia competitor product name appears in at least two STATUS QUO element cells."

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 -- Properties Verify + Inference Audit

**PART A — Frontmatter Verify**
Confirm Step 5 matches Step 6 for all fields.
State: "All Step 5 values match Step 6 card bodies."

**PART B — Property Checks**

1. Tool-name fidelity.
   State: "[PRODUCT NAME] in Step 1b-ii: YES. Card bodies: [T-NN, T-NN min].
   Migrating from: field: YES."

2. Phase-differentiated templates.
   State: "Phase 1 template in: [T-NN, T-NN]. Phase 3 template in: [T-NN]."

3. Switching-friction 4-field format.
   State: "All four fields present in all entries: YES / NO."

**PART C — Inference Audit**

**Sub-check 1: Phase-Architecture Severity Compliance**

Scan Phase 1 cards (Phase 1 section, Step 6). Exception sign-off for any P0/P1, or:
"No Phase 1 P0/P1 exceptions. Phase 1 lifecycle: fallback available.
Governing paraphrase clause: [copy the exact Phase 1 clause from INFERENCE RULE (stated)
at Step 2C — do not paraphrase, do not summarize, copy it verbatim word-for-word]."

Scan Phase 2 cards (Phase 2 section, Step 6). Exception sign-off for any P0 escalation, or:
"No Phase 2 P0 escalation exceptions. Phase 2 lifecycle: transition (partial fallback).
Governing paraphrase clause: [copy the exact Phase 2 clause from INFERENCE RULE (stated)
at Step 2C — do not paraphrase, do not summarize, copy it verbatim word-for-word]."

Scan Phase 3 cards (Phase 3 section, Step 6). Exception sign-off for any P3, or:
"No Phase 3 P3 exceptions. Phase 3 lifecycle: no fallback.
Governing paraphrase clause: [copy the exact Phase 3 clause from INFERENCE RULE (stated)
at Step 2C — do not paraphrase, do not summarize, copy it verbatim word-for-word]."

Paraphrase consistency confirmation:
State: "INFERENCE RULE paraphrase (Step 2C): [first 10 words].
Verbatim anchor at Step 5: YES.
All three phase Paraphrase clause fields: triple-clause verbatim (do not paraphrase,
do not summarize, copy it verbatim word-for-word): YES.
Phase 1 compliance: PASS/FAIL.
Phase 2 within P1/P2 range: PASS/FAIL.
Phase 3 compliance: PASS/FAIL.
Paraphrase consistent with audit results: YES / NO."

**Sub-check 2: Switching-Friction Sub-Section Field Completeness**

Restate count: "SWITCHING-FRICTION COUNT: [N]. N ≥ 3: YES/NO."
List each entry's `Migrating from:` value. Flag any non-verbatim.
Quote Entry 3 Trigger event field verbatim: "[quote]"
State: "Sub-section present: YES. All Migrating from: fields verbatim: YES / NO.
Third entry covers Phase 2 migration barrier (not day-one friction): YES / NO.
Entry 3 Trigger event names a post-commitment workflow action (not day-one): YES / NO."

**Sub-check 3: Post-Generation Phase Distribution Re-Verification**

Count Phase 1, Phase 2, Phase 3 card bodies in Step 6 phase sections.
State:
"Post-generation phase distribution:
Phase 1 bodies generated: [n]. Committed (Step 5): [n]. Step 1 target: [n]. MATCH / MISMATCH.
Phase 2 bodies generated: [n]. Committed (Step 5): [n]. Step 1 target: [n]. MATCH / MISMATCH.
Phase 3 bodies generated: [n]. Committed (Step 5): [n]. Step 1 target: [n]. MATCH / MISMATCH.
Total: [n] generated. Committed: [n]. Step 1 target: [n]. MATCH / MISMATCH."

If any MISMATCH: name the discrepancy, identify the Ticket ID that drifted from its
committed phase, and state the correction needed. A mismatch here means the pre-generation
constraint was satisfied (5B passed) but generation-time drift occurred — flag explicitly.

State final:
"All Step 5 values match Step 6.
Exception sign-offs complete for Phase 1, Phase 2, and Phase 3 scans.
SWITCHING-FRICTION COUNT ≥ 3 confirmed. Third entry covers Phase 2 barrier: YES.
Entry 3 Trigger event quoted and confirmed: post-commitment action named.
Post-generation phase distribution matches committed block and Step 1 target.
Sub-checks 1, 2, and 3 verified. All C-01 through C-49 constraints met.
C-51 probe (Phase-2 barrier trigger-event field): complete."
```

---

## V-03: Single-Axis — Inertia Framing (Per-Template Prohibited: Sentinel in Entry 3)

**Axis:** Inertia framing — Entry 3 of the switching-friction sub-section. V-05 R16 places the Prohibited: constraint for Entry 3 inside the Entry-specific guidance section ("Entry 3: Cover a Phase 2 migration barrier... Prohibited: a barrier that day-one users would also encounter (that belongs in entries 1 or 2)."). V-03 R17 moves the Prohibited: sentinel to the Entry 3 template body, placing it as a field-adjacent guard directly below `Migrating from:`, before `Expected behavior:`. The Entry-specific guidance section retains the Entry 3 description but no longer carries the Prohibited: note. All other mechanisms from V-05 R16 are preserved exactly.

**Probe (C-52 candidate):** V-05 R16 satisfies C-49 by requiring the third entry to be structurally constrained to a Phase 2 migration barrier, with the Prohibited: form explicitly stated in the Entry-specific guidance. The failure mode C-49 leaves open: the Prohibited: appears in a guidance section that is read before entry writing begins, not at the moment the model is writing Entry 3's content fields. Guidance-level prohibitions are spatially separated from the field they constrain. When the model reaches `Expected behavior:` for Entry 3, the Prohibited: note from the guidance section is no longer visually adjacent — it must be retrieved from a prior instruction block. A per-template Prohibited: sentinel placed directly below `Migrating from:` (and above `Expected behavior:`) is adjacent to the content fields it constrains at the exact moment those fields are written. This follows the pattern C-18 established: moving Prohibited: from a higher-scope instruction into the field-level template closes the spatial-retrieval failure mode. C-49 passes when the Prohibited: form appears in the guidance section; C-52 passes only when the Prohibited: sentinel appears in the Entry 3 template body as a field-adjacent guard.

**Hypothesis:** The guidance-level Prohibited: and the per-template Prohibited: produce structurally identical outputs in a well-behaved model. The distinction surfaces when a model processes the guidance section, writes entries, and the guidance-level prohibition fails to transfer to the active writing context for Entry 3. C-18 established that per-field sentinels close a content-genericity failure mode that higher-scope instructions leave open. C-52 probes whether the same spatial-adjacency mechanism applies to the switching-friction Entry 3 constraint. The per-template Prohibited: is independently checkable: a scorer reads the Entry 3 template and confirms the sentinel appears before `Expected behavior:`. A guidance-section-only Prohibited: requires a scorer to scan a separate section.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- PHASE DISTRIBUTION TARGET (declared before STATUS QUO analysis)

Before establishing the STATUS QUO baseline, declare the target ticket distribution.

PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0–30): [N] tickets
  Phase 2 (Day 31–60): [N] tickets
  Phase 3 (Day 61–90): [N] tickets
  Total: [N] tickets

Constraint: Phase 1 count ≥ 2. Phase 3 count ≥ 1. All three phases represented.
This target will be referenced at Step 5 (committed block) and re-verified at Step 5B
and Pass 2 Part C Sub-check 3.

---

## STEP 1B -- INERTIA: STATUS QUO

**1b-i. Current-state baseline**
Describe in 2-3 sentences: what are users doing today? Frame with awareness of
the Phase Distribution Target — the baseline must generate friction across all three
phase windows.

**1b-ii. Inertia competitor declaration**
INERTIA COMPETITOR: [product name]
Prohibited: any non-grep-checkable phrase.

**1b-iii. Adoption-curve context**
Confirm consistency with the Phase Distribution Target.

---

## STEP 2 -- PHASE MAP TABLE

| Phase | Window | Expected severity range | Expected volume character |
|-------|--------|------------------------|--------------------------|
| Phase 1 | Day 0–30 | P2/P3 | high |
| Phase 2 | Day 31–60 | P1/P2 | medium |
| Phase 3 | Day 61–90 | P0/P1 | medium/low |

---

## STEP 2B -- PHASE BODY TEMPLATE TABLE

| Phase | Adoption stance | Template sentence |
|-------|----------------|-------------------|
| Phase 1 | Dual-tool tension | "I still have [INERTIA COMPETITOR] open in another tab — I keep switching back to check how it handled [specific scenario]." |
| Phase 3 | Parity gap | "In [INERTIA COMPETITOR] I could [specific action] without leaving this screen; here I cannot." |

Phase 1 and Phase 3 bodies: open with the template sentence, placeholders filled concretely.
Phase 2 bodies: reference the competitor where natural.

---

## STEP 2C -- PHASE-SEVERITY INFERENCE RULE

Phase 1 (Day 0–30): P2/P3 non-outage. Fallback available; user is learning.
Phase 3 (Day 61–90): P1/P0 blocking. No fallback; user committed and blocked.

Violation conditions:
- Phase 1 P0/P1 non-outage: violation — correct to P2/P3.
- Phase 3 P3 blocking: violation — correct to P1/P0.

INFERENCE RULE (stated): [your paraphrase of the directional rule above]
Applied in: Steps 5, 5B, and Pass 2 INFERENCE AUDIT

Do not proceed until filled with your own-words paraphrase.

---

## STEP 3 -- ROLE ACTIVATION ORDER (SRE-FIRST)

Activate roles: SRE → Support → PM → UX → C-01 through C-12.

[SRE] — First. Operational failure modes: configuration errors, deployment issues,
on-call escalation, infrastructure-level P0/P1 candidates. Identify Phase 2 escalation
patterns (transition-zone operational friction that surfaces after partial commitment).

[Support] — Second. Triage-queue patterns, documentation gaps, error messages.

[PM] — Third. Intent gaps, roadmap items, feature-request backlog.

[UX] — Fourth. Discoverability failures, onboarding friction, how-to patterns.

[C-01 through C-12] — One ticket hypothesis each. Frame each with phase awareness:
  "In which phase (1, 2, or 3) will this persona most likely encounter this issue?"

---

## STEP 4 -- PERFORMANCE MODE DECLARATION

**You ARE the persona named on each ticket card.**

Your previous primary workflow used [INERTIA COMPETITOR — product name from Step 1b-ii].
Phase 1: old tool still open, can fall back — lower stakes.
Phase 3: committed to new tool, no fallback — higher stakes.

Do not write "the user", "they", "the SRE", "the PM", "the engineer",
or any named-role title in third person.

Prohibited verb-subject forms: "the SRE ran", "the PM reviewed", "the engineer observed",
"the C-07 clicked", "the Support agent opened", or any role-title-preceding-a-verb form.

**Every action in this ticket was taken by "I".
Every old-tool reference uses the product name from Step 1b-ii.**

---

## STEP 5 -- VOCABULARY PRE-COMMITMENT TABLE

Competitor in scope: [product name from Step 1b-ii]

Do not fill any cell in the table until all three items are written:

Required item 1 — INFERENCE RULE (confirmed):
[restate in your own words]

Required item 2 — Verbatim from 2C:
[copy exact first sentence from INFERENCE RULE (stated) at Step 2C — word for word, do not paraphrase]

Required item 3 — PHASE DISTRIBUTION committed block:
Reconcile with Phase Distribution Target from Step 1.
  Phase 1 (Day 0–30): [N] tickets (Step 1 target: [N])
  Phase 2 (Day 31–60): [N] tickets (Step 1 target: [N])
  Phase 3 (Day 61–90): [N] tickets (Step 1 target: [N])
  Total: [N] tickets

Confirmation: this rule applies to every severity assignment in the table below.

| Ticket ID | Phase | Category | Persona | Volume | Severity |
|-----------|-------|----------|---------|--------|----------|
| T-01 | | | | | |
| T-02 | | | | | |
| T-03 | | | | | |
| T-04 | | | | | |
| T-05 | | | | | |
| T-06 | | | | | |
| T-07 | | | | | |
| T-08 | | | | | |

Allowed: Category {how-to, bug, feature-request, config, integration}, Volume {high, medium, low}, Severity {P0, P1, P2, P3}.
**Lock vocabulary values here. Full card bodies follow in Step 6.**

---

## STEP 5B -- COLLECTIVE DISTRIBUTION AUDIT

Constraint 0: Phase counts must match Step 5 committed block.
State: "Phase 1: [n] committed, [n] actual — MATCH/MISMATCH."
Also cross-check against Step 1 target: "Step 1 target vs Step 5 committed: [match/mismatch per phase]."

1. Phase distribution — ≥2 Phase 1, ≥1 Phase 3.
2. Category spread — ≥3 distinct categories.
3. Volume distribution — all three levels.
4. Phase-character compliance — severity/volume match Step 2.
5. Inference-rule compliance — Phase 1/Phase 3 violation scan.

**If any fails, correct and re-run.**

---

## STEP 5C -- PRE-BODY STRUCTURAL VERIFICATION (PASS 2B)

Item 1 — Category distribution check.
Item 2 — Persona distribution check.
Item 3 — Phase distribution compliance.

Item 4 — SWITCHING-FRICTION COUNT CHECK:
SWITCHING-FRICTION COUNT: [N]
N must be ≥ 3. Do not proceed to Step 6 if N < 3.
Third entry must cover a Phase 2 migration barrier (surfaces after partial commitment,
not on day one).

---

## STEP 6 -- FULL CARD BODIES (PHASE-ORGANIZED)

Organize by phase window. Complete all Phase 1 cards, then Phase 2, then Phase 3.
Within each group, ascending Ticket ID order.

### Phase 1 Cards (Day 0–30)

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [match Step 5]
Persona: [match Step 5]
Volume: [match Step 5]
Severity: [match Step 5 — P2 or P3]

Body:
[Open with Phase 1 template sentence, all placeholders filled with the inertia competitor
product name and a concrete scenario. Reference the STATUS QUO element that drives this
ticket's volume. No third-person. Every old-tool reference: product name from Step 1b-ii.]

---

### Phase 2 Cards (Day 31–60)

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [match Step 5]
Persona: [match Step 5]
Volume: [match Step 5]
Severity: [match Step 5 — P1 or P2]

Body:
[Transition framing — user is partially committed, not yet fully detached. Reference the
competitor where the framing naturally calls for it. Reference the STATUS QUO element
from Step 1b-i. No third-person. Product name for old tool.]

---

### Phase 3 Cards (Day 61–90)

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [match Step 5]
Persona: [match Step 5]
Volume: [match Step 5]
Severity: [match Step 5 — P0 or P1]

Body:
[Open with Phase 3 template sentence, all placeholders filled concretely. Reference the
STATUS QUO element that drives this ticket's severity — the user committed fully; the
competitor is not accessible for this workflow. No third-person. Product name for old tool.]

---

## STEP 7 -- CROSS-TICKET PATTERNS

Pattern name: [short name]
Tickets affected: [T-NN, ...]
Root cause: [one sentence]

Consequence — Affected segment:
Prohibited: "users in general", "the team", any unnamed group.
[Named role or cohort tied specifically to this pattern]

Consequence — Day-90 scenario:
Prohibited: "this will cause confusion", any non-pattern-specific event.
[One specific event that occurs if unaddressed by Day 90]

Consequence — Adoption cost:
Prohibited: generic friction not specific to this cohort.
[One sentence quantifying friction for the named segment]

If a pattern involves migration from the inertia competitor, name the competitor.

---

## STEP 8 -- GAP ANALYSIS

### Doc Gaps
[At least one documentation gap.]

### Design Gaps
[At least one design gap.]

### Operational Gaps
[At least one operational gap.]

### Switching-Friction Gaps

Dedicated sub-section for migration barriers only. NOT absorbed into the three sections above.
The three sections above remain present and non-empty.

SWITCHING-FRICTION COUNT: [N]
N must be ≥ 3. State this count before writing any entry.

Switching-friction gap: [short name]
Migrating from: [product name from Step 1b-ii — verbatim, grep-checkable]
Expected behavior: [one sentence]
Actual behavior: [one sentence]
Migration impact: [one sentence]

[Use the template above for Entries 1 and 2.]

[Entry 3 — Phase 2 migration barrier — use this extended template:]

Switching-friction gap: [short name]
Migrating from: [product name from Step 1b-ii — verbatim, grep-checkable]
Prohibited: a barrier that day-one users would encounter on first contact.
  Disallowed: any friction present before workflow migration has begun; any issue
  a new user who has never committed to this tool would also file.
Expected behavior: [one sentence — the behavior the user expected based on their
  experience after partial commitment]
Actual behavior: [one sentence]
Migration impact: [one sentence]

Entry-specific guidance:
- Entry 1: Cover the primary day-one migration friction (Phase 1 ticket driver).
- Entry 2: Cover the second most prominent migration barrier.
- Entry 3: Cover a Phase 2 migration barrier. Use the extended template above.
  The Prohibited: sentinel in the template applies to this entry.

### Pre-Launch Priority
Name the single gap to close first. Tie to specific Ticket IDs, severity, and volume.
State whether it reduces switching-friction for inertia-competitor migrants.

---

## STEP 9 -- DUAL-PASS VERIFICATION

### PASS 1 -- Coverage Trace Table

| Ticket ID | STATUS QUO element referenced | Gap traced to |
|-----------|-------------------------------|---------------|

Populate one row per ticket, in Ticket ID order.

After completing:
1. Confirm: "No gap from the Gap Analysis — including switching-friction gaps — is absent."
2. Confirm: "Inertia competitor product name appears in at least two STATUS QUO element cells."

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 -- Properties Verify + Inference Audit

**PART A — Frontmatter Verify**
Confirm Step 5 matches Step 6 for all fields.
State: "All Step 5 values match Step 6 card bodies."

**PART B — Property Checks**

1. Tool-name fidelity.
   State: "[PRODUCT NAME] in Step 1b-ii: YES. Card bodies: [T-NN, T-NN min].
   Migrating from: field: YES."

2. Phase-differentiated templates.
   State: "Phase 1 template in: [T-NN, T-NN]. Phase 3 template in: [T-NN]."

3. Switching-friction 4-field format.
   State: "All four fields present in all entries: YES / NO."

**PART C — Inference Audit**

**Sub-check 1: Phase-Architecture Severity Compliance**

Scan Phase 1 cards (Phase 1 section, Step 6). Exception sign-off for any P0/P1, or:
"No Phase 1 P0/P1 exceptions. Phase 1 lifecycle: fallback available.
Governing paraphrase clause: [copy the exact Phase 1 clause from INFERENCE RULE (stated)
at Step 2C — do not paraphrase, do not summarize, copy it verbatim word-for-word]."

Scan Phase 2 cards (Phase 2 section, Step 6). Exception sign-off for any P0 escalation, or:
"No Phase 2 P0 escalation exceptions. Phase 2 lifecycle: transition (partial fallback).
Governing paraphrase clause: [copy the exact Phase 2 clause from INFERENCE RULE (stated)
at Step 2C — do not paraphrase, do not summarize, copy it verbatim word-for-word]."

Scan Phase 3 cards (Phase 3 section, Step 6). Exception sign-off for any P3, or:
"No Phase 3 P3 exceptions. Phase 3 lifecycle: no fallback.
Governing paraphrase clause: [copy the exact Phase 3 clause from INFERENCE RULE (stated)
at Step 2C — do not paraphrase, do not summarize, copy it verbatim word-for-word]."

Paraphrase consistency confirmation:
State: "INFERENCE RULE paraphrase (Step 2C): [first 10 words].
Verbatim anchor at Step 5: YES.
All three phase Paraphrase clause fields: triple-clause verbatim (do not paraphrase,
do not summarize, copy it verbatim word-for-word): YES.
Phase 1 compliance: PASS/FAIL.
Phase 2 within P1/P2 range: PASS/FAIL.
Phase 3 compliance: PASS/FAIL.
Paraphrase consistent with audit results: YES / NO."

**Sub-check 2: Switching-Friction Sub-Section Field Completeness**

Restate count: "SWITCHING-FRICTION COUNT: [N]. N ≥ 3: YES/NO."
List each entry's `Migrating from:` value. Flag any non-verbatim.
State: "Sub-section present: YES. All Migrating from: fields verbatim: YES / NO.
Third entry covers Phase 2 migration barrier (not day-one friction): YES / NO.
Entry 3 Prohibited: sentinel present in template (field-adjacent): YES / NO."

**Sub-check 3: Post-Generation Phase Distribution Re-Verification**

Count Phase 1, Phase 2, Phase 3 card bodies in Step 6 phase sections.
State:
"Post-generation phase distribution:
Phase 1 bodies generated: [n]. Committed (Step 5): [n]. Step 1 target: [n]. MATCH / MISMATCH.
Phase 2 bodies generated: [n]. Committed (Step 5): [n]. Step 1 target: [n]. MATCH / MISMATCH.
Phase 3 bodies generated: [n]. Committed (Step 5): [n]. Step 1 target: [n]. MATCH / MISMATCH.
Total: [n] generated. Committed: [n]. Step 1 target: [n]. MATCH / MISMATCH."

If any MISMATCH: name the discrepancy, identify the Ticket ID that drifted from its
committed phase, and state the correction needed. A mismatch here means the pre-generation
constraint was satisfied (5B passed) but generation-time drift occurred — flag explicitly.

State final:
"All Step 5 values match Step 6.
Exception sign-offs complete for Phase 1, Phase 2, and Phase 3 scans.
SWITCHING-FRICTION COUNT ≥ 3 confirmed. Third entry covers Phase 2 barrier: YES.
Entry 3 Prohibited: sentinel in template (field-adjacent): confirmed.
Post-generation phase distribution matches committed block and Step 1 target.
Sub-checks 1, 2, and 3 verified. All C-01 through C-49 constraints met.
C-52 probe (per-template Prohibited: sentinel in Entry 3): complete."
```

---

## V-04: Combined — V-01 + V-02 (Table Sub-check 3 + Trigger-Event Field)

**Axis:** V-01 (Sub-check 3 table format) + V-02 (Phase-2 barrier trigger-event field + Sub-check 2 trigger quote). Targets 295/295 on v16 plus potential above-ceiling credit on C-50 and C-51 candidates.

**Hypothesis:** C-50 and C-51 are structurally independent: C-50 targets the format of the post-generation phase distribution verification (table vs. prose), C-51 targets the evidence requirement for the Phase-2 barrier type constraint (trigger-event field vs. YES/NO claim). Combining both closes two distinct failure modes simultaneously: the prose-collapse failure mode in Sub-check 3, and the declarative-confirmation failure mode in Sub-check 2. V-04 tests whether both probes coexist without structural interference.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- PHASE DISTRIBUTION TARGET (declared before STATUS QUO analysis)

Before establishing the STATUS QUO baseline, declare the target ticket distribution.

PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0–30): [N] tickets
  Phase 2 (Day 31–60): [N] tickets
  Phase 3 (Day 61–90): [N] tickets
  Total: [N] tickets

Constraint: Phase 1 count ≥ 2. Phase 3 count ≥ 1. All three phases represented.
This target will be referenced at Step 5 (committed block) and re-verified at Step 5B
and Pass 2 Part C Sub-check 3.

---

## STEP 1B -- INERTIA: STATUS QUO

**1b-i. Current-state baseline**
Describe in 2-3 sentences: what are users doing today? Frame with awareness of
the Phase Distribution Target — the baseline must generate friction across all three
phase windows.

**1b-ii. Inertia competitor declaration**
INERTIA COMPETITOR: [product name]
Prohibited: any non-grep-checkable phrase.

**1b-iii. Adoption-curve context**
Confirm consistency with the Phase Distribution Target.

---

## STEP 2 -- PHASE MAP TABLE

| Phase | Window | Expected severity range | Expected volume character |
|-------|--------|------------------------|--------------------------|
| Phase 1 | Day 0–30 | P2/P3 | high |
| Phase 2 | Day 31–60 | P1/P2 | medium |
| Phase 3 | Day 61–90 | P0/P1 | medium/low |

---

## STEP 2B -- PHASE BODY TEMPLATE TABLE

| Phase | Adoption stance | Template sentence |
|-------|----------------|-------------------|
| Phase 1 | Dual-tool tension | "I still have [INERTIA COMPETITOR] open in another tab — I keep switching back to check how it handled [specific scenario]." |
| Phase 3 | Parity gap | "In [INERTIA COMPETITOR] I could [specific action] without leaving this screen; here I cannot." |

Phase 1 and Phase 3 bodies: open with the template sentence, placeholders filled concretely.
Phase 2 bodies: reference the competitor where natural.

---

## STEP 2C -- PHASE-SEVERITY INFERENCE RULE

Phase 1 (Day 0–30): P2/P3 non-outage. Fallback available; user is learning.
Phase 3 (Day 61–90): P1/P0 blocking. No fallback; user committed and blocked.

Violation conditions:
- Phase 1 P0/P1 non-outage: violation — correct to P2/P3.
- Phase 3 P3 blocking: violation — correct to P1/P0.

INFERENCE RULE (stated): [your paraphrase of the directional rule above]
Applied in: Steps 5, 5B, and Pass 2 INFERENCE AUDIT

Do not proceed until filled with your own-words paraphrase.

---

## STEP 3 -- ROLE ACTIVATION ORDER (SRE-FIRST)

Activate roles: SRE → Support → PM → UX → C-01 through C-12.

[SRE] — First. Operational failure modes: configuration errors, deployment issues,
on-call escalation, infrastructure-level P0/P1 candidates. Identify Phase 2 escalation
patterns (transition-zone operational friction that surfaces after partial commitment).

[Support] — Second. Triage-queue patterns, documentation gaps, error messages.

[PM] — Third. Intent gaps, roadmap items, feature-request backlog.

[UX] — Fourth. Discoverability failures, onboarding friction, how-to patterns.

[C-01 through C-12] — One ticket hypothesis each. Frame each with phase awareness:
  "In which phase (1, 2, or 3) will this persona most likely encounter this issue?"

---

## STEP 4 -- PERFORMANCE MODE DECLARATION

**You ARE the persona named on each ticket card.**

Your previous primary workflow used [INERTIA COMPETITOR — product name from Step 1b-ii].
Phase 1: old tool still open, can fall back — lower stakes.
Phase 3: committed to new tool, no fallback — higher stakes.

Do not write "the user", "they", "the SRE", "the PM", "the engineer",
or any named-role title in third person.

Prohibited verb-subject forms: "the SRE ran", "the PM reviewed", "the engineer observed",
"the C-07 clicked", "the Support agent opened", or any role-title-preceding-a-verb form.

**Every action in this ticket was taken by "I".
Every old-tool reference uses the product name from Step 1b-ii.**

---

## STEP 5 -- VOCABULARY PRE-COMMITMENT TABLE

Competitor in scope: [product name from Step 1b-ii]

Do not fill any cell in the table until all three items are written:

Required item 1 — INFERENCE RULE (confirmed):
[restate in your own words]

Required item 2 — Verbatim from 2C:
[copy exact first sentence from INFERENCE RULE (stated) at Step 2C — word for word, do not paraphrase]

Required item 3 — PHASE DISTRIBUTION committed block:
Reconcile with Phase Distribution Target from Step 1.
  Phase 1 (Day 0–30): [N] tickets (Step 1 target: [N])
  Phase 2 (Day 31–60): [N] tickets (Step 1 target: [N])
  Phase 3 (Day 61–90): [N] tickets (Step 1 target: [N])
  Total: [N] tickets

Confirmation: this rule applies to every severity assignment in the table below.

| Ticket ID | Phase | Category | Persona | Volume | Severity |
|-----------|-------|----------|---------|--------|----------|
| T-01 | | | | | |
| T-02 | | | | | |
| T-03 | | | | | |
| T-04 | | | | | |
| T-05 | | | | | |
| T-06 | | | | | |
| T-07 | | | | | |
| T-08 | | | | | |

Allowed: Category {how-to, bug, feature-request, config, integration}, Volume {high, medium, low}, Severity {P0, P1, P2, P3}.
**Lock vocabulary values here. Full card bodies follow in Step 6.**

---

## STEP 5B -- COLLECTIVE DISTRIBUTION AUDIT

Constraint 0: Phase counts must match Step 5 committed block.
State: "Phase 1: [n] committed, [n] actual — MATCH/MISMATCH."
Also cross-check against Step 1 target: "Step 1 target vs Step 5 committed: [match/mismatch per phase]."

1. Phase distribution — ≥2 Phase 1, ≥1 Phase 3.
2. Category spread — ≥3 distinct categories.
3. Volume distribution — all three levels.
4. Phase-character compliance — severity/volume match Step 2.
5. Inference-rule compliance — Phase 1/Phase 3 violation scan.

**If any fails, correct and re-run.**

---

## STEP 5C -- PRE-BODY STRUCTURAL VERIFICATION (PASS 2B)

Item 1 — Category distribution check.
Item 2 — Persona distribution check.
Item 3 — Phase distribution compliance.

Item 4 — SWITCHING-FRICTION COUNT CHECK:
SWITCHING-FRICTION COUNT: [N]
N must be ≥ 3. Do not proceed to Step 6 if N < 3.
Third entry must cover a Phase 2 migration barrier (surfaces after partial commitment,
not on day one).

---

## STEP 6 -- FULL CARD BODIES (PHASE-ORGANIZED)

Organize by phase window. Complete all Phase 1 cards, then Phase 2, then Phase 3.
Within each group, ascending Ticket ID order.

### Phase 1 Cards (Day 0–30)

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [match Step 5]
Persona: [match Step 5]
Volume: [match Step 5]
Severity: [match Step 5 — P2 or P3]

Body:
[Open with Phase 1 template sentence, all placeholders filled with the inertia competitor
product name and a concrete scenario. Reference the STATUS QUO element that drives this
ticket's volume. No third-person. Every old-tool reference: product name from Step 1b-ii.]

---

### Phase 2 Cards (Day 31–60)

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [match Step 5]
Persona: [match Step 5]
Volume: [match Step 5]
Severity: [match Step 5 — P1 or P2]

Body:
[Transition framing — user is partially committed, not yet fully detached. Reference the
competitor where the framing naturally calls for it. Reference the STATUS QUO element
from Step 1b-i. No third-person. Product name for old tool.]

---

### Phase 3 Cards (Day 61–90)

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [match Step 5]
Persona: [match Step 5]
Volume: [match Step 5]
Severity: [match Step 5 — P0 or P1]

Body:
[Open with Phase 3 template sentence, all placeholders filled concretely. Reference the
STATUS QUO element that drives this ticket's severity — the user committed fully; the
competitor is not accessible for this workflow. No third-person. Product name for old tool.]

---

## STEP 7 -- CROSS-TICKET PATTERNS

Pattern name: [short name]
Tickets affected: [T-NN, ...]
Root cause: [one sentence]

Consequence — Affected segment:
Prohibited: "users in general", "the team", any unnamed group.
[Named role or cohort tied specifically to this pattern]

Consequence — Day-90 scenario:
Prohibited: "this will cause confusion", any non-pattern-specific event.
[One specific event that occurs if unaddressed by Day 90]

Consequence — Adoption cost:
Prohibited: generic friction not specific to this cohort.
[One sentence quantifying friction for the named segment]

If a pattern involves migration from the inertia competitor, name the competitor.

---

## STEP 8 -- GAP ANALYSIS

### Doc Gaps
[At least one documentation gap.]

### Design Gaps
[At least one design gap.]

### Operational Gaps
[At least one operational gap.]

### Switching-Friction Gaps

Dedicated sub-section for migration barriers only. NOT absorbed into the three sections above.
The three sections above remain present and non-empty.

SWITCHING-FRICTION COUNT: [N]
N must be ≥ 3. State this count before writing any entry.

Template for Entries 1 and 2:

Switching-friction gap: [short name]
Migrating from: [product name from Step 1b-ii — verbatim, grep-checkable]
Expected behavior: [one sentence]
Actual behavior: [one sentence]
Migration impact: [one sentence]

Template for Entry 3 (Phase 2 barrier — extended template):

Switching-friction gap: [short name]
Migrating from: [product name from Step 1b-ii — verbatim, grep-checkable]
Trigger event: [name the specific workflow action or system state that first surfaces
  this barrier after partial commitment — must name a concrete post-commitment event
  that day-one users do not reach on first contact]
Expected behavior: [one sentence]
Actual behavior: [one sentence]
Migration impact: [one sentence]

Entry-specific guidance:
- Entry 1: Cover the primary day-one migration friction (Phase 1 ticket driver).
- Entry 2: Cover the second most prominent migration barrier.
- Entry 3: Use the extended template. The Trigger event field must name the specific
  post-commitment workflow action. Prohibited: a barrier that day-one users would also
  encounter (that belongs in entries 1 or 2).

### Pre-Launch Priority
Name the single gap to close first. Tie to specific Ticket IDs, severity, and volume.
State whether it reduces switching-friction for inertia-competitor migrants.

---

## STEP 9 -- DUAL-PASS VERIFICATION

### PASS 1 -- Coverage Trace Table

| Ticket ID | STATUS QUO element referenced | Gap traced to |
|-----------|-------------------------------|---------------|

Populate one row per ticket, in Ticket ID order.

After completing:
1. Confirm: "No gap from the Gap Analysis — including switching-friction gaps — is absent."
2. Confirm: "Inertia competitor product name appears in at least two STATUS QUO element cells."

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 -- Properties Verify + Inference Audit

**PART A — Frontmatter Verify**
Confirm Step 5 matches Step 6 for all fields.
State: "All Step 5 values match Step 6 card bodies."

**PART B — Property Checks**

1. Tool-name fidelity.
   State: "[PRODUCT NAME] in Step 1b-ii: YES. Card bodies: [T-NN, T-NN min].
   Migrating from: field: YES."

2. Phase-differentiated templates.
   State: "Phase 1 template in: [T-NN, T-NN]. Phase 3 template in: [T-NN]."

3. Switching-friction 4-field format.
   State: "All four fields present in all entries: YES / NO."

**PART C — Inference Audit**

**Sub-check 1: Phase-Architecture Severity Compliance**

Scan Phase 1 cards (Phase 1 section, Step 6). Exception sign-off for any P0/P1, or:
"No Phase 1 P0/P1 exceptions. Phase 1 lifecycle: fallback available.
Governing paraphrase clause: [copy the exact Phase 1 clause from INFERENCE RULE (stated)
at Step 2C — do not paraphrase, do not summarize, copy it verbatim word-for-word]."

Scan Phase 2 cards (Phase 2 section, Step 6). Exception sign-off for any P0 escalation, or:
"No Phase 2 P0 escalation exceptions. Phase 2 lifecycle: transition (partial fallback).
Governing paraphrase clause: [copy the exact Phase 2 clause from INFERENCE RULE (stated)
at Step 2C — do not paraphrase, do not summarize, copy it verbatim word-for-word]."

Scan Phase 3 cards (Phase 3 section, Step 6). Exception sign-off for any P3, or:
"No Phase 3 P3 exceptions. Phase 3 lifecycle: no fallback.
Governing paraphrase clause: [copy the exact Phase 3 clause from INFERENCE RULE (stated)
at Step 2C — do not paraphrase, do not summarize, copy it verbatim word-for-word]."

Paraphrase consistency confirmation:
State: "INFERENCE RULE paraphrase (Step 2C): [first 10 words].
Verbatim anchor at Step 5: YES.
All three phase Paraphrase clause fields: triple-clause verbatim (do not paraphrase,
do not summarize, copy it verbatim word-for-word): YES.
Phase 1 compliance: PASS/FAIL.
Phase 2 within P1/P2 range: PASS/FAIL.
Phase 3 compliance: PASS/FAIL.
Paraphrase consistent with audit results: YES / NO."

**Sub-check 2: Switching-Friction Sub-Section Field Completeness**

Restate count: "SWITCHING-FRICTION COUNT: [N]. N ≥ 3: YES/NO."
List each entry's `Migrating from:` value. Flag any non-verbatim.
Quote Entry 3 Trigger event field verbatim: "[quote]"
State: "Sub-section present: YES. All Migrating from: fields verbatim: YES / NO.
Third entry covers Phase 2 migration barrier (not day-one friction): YES / NO.
Entry 3 Trigger event names a post-commitment workflow action (not day-one): YES / NO."

**Sub-check 3: Post-Generation Phase Distribution Re-Verification**

Count Phase 1, Phase 2, Phase 3 card bodies in Step 6 phase sections.
Complete the table:

| Phase | Bodies generated | Committed (Step 5) | Step 1 target | Match |
|-------|-----------------|-------------------|---------------|-------|
| Phase 1 | [n] | [n] | [n] | MATCH/MISMATCH |
| Phase 2 | [n] | [n] | [n] | MATCH/MISMATCH |
| Phase 3 | [n] | [n] | [n] | MATCH/MISMATCH |
| Total | [n] | [n] | [n] | MATCH/MISMATCH |

If any row shows MISMATCH: name the discrepancy, identify the Ticket ID that drifted
from its committed phase, and state the correction needed. A row-level MISMATCH here
means the pre-generation constraint was satisfied (5B passed) but generation-time drift
occurred — flag explicitly by row.

State final:
"All Step 5 values match Step 6.
Exception sign-offs complete for Phase 1, Phase 2, and Phase 3 scans.
SWITCHING-FRICTION COUNT ≥ 3 confirmed. Third entry covers Phase 2 barrier: YES.
Entry 3 Trigger event quoted and confirmed: post-commitment action named.
Post-generation phase distribution table complete. All rows: MATCH.
Sub-checks 1, 2, and 3 verified. All C-01 through C-49 constraints met.
C-50 probe (Sub-check 3 table format): complete.
C-51 probe (Phase-2 barrier trigger-event field): complete."
```

---

## V-05: Full Synthesis — All Three Axes + All Three Probes

**Axis:** Full combination of V-01 (Sub-check 3 table format), V-02 (Phase-2 barrier trigger-event field + Sub-check 2 trigger quote), and V-03 (per-template Prohibited: sentinel in Entry 3). Targets 295/295 on v16 plus potential above-ceiling credit on C-50, C-51, and C-52 candidates.

**Hypothesis:** The three probes are structurally independent: C-50 targets the format of Sub-check 3 (table vs. prose), C-51 targets the evidence requirement for Entry 3 type constraint (trigger-event field vs. YES/NO), C-52 targets the spatial location of the Entry 3 Prohibited: guard (field-adjacent in template vs. guidance-section-level). Each probe addresses a distinct failure mode. C-50 prevents prose-collapse in phase distribution re-verification. C-51 prevents declarative Phase-2 barrier claims without named post-commitment trigger. C-52 prevents spatial-retrieval failure of the day-one Prohibited: guard when the model writes Entry 3 content fields. All three can coexist: the Trigger event field and the Prohibited: sentinel both belong to the Entry 3 template, the table belongs to Sub-check 3. No structural interference. V-05 tests whether all three probes coexist and whether the full combination produces a qualitatively richer switching-friction section and post-generation verification than any single-axis variation.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- PHASE DISTRIBUTION TARGET (declared before STATUS QUO analysis)

Before establishing the STATUS QUO baseline, declare the target ticket distribution.

PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0–30): [N] tickets
  Phase 2 (Day 31–60): [N] tickets
  Phase 3 (Day 61–90): [N] tickets
  Total: [N] tickets

Constraint: Phase 1 count ≥ 2. Phase 3 count ≥ 1. All three phases represented.
This target will be referenced at Step 5 (committed block) and re-verified at Step 5B
and Pass 2 Part C Sub-check 3.

---

## STEP 1B -- INERTIA: STATUS QUO

**1b-i. Current-state baseline**
Describe in 2-3 sentences: what are users doing today? Frame with awareness of
the Phase Distribution Target — the baseline must generate friction across all three
phase windows.

**1b-ii. Inertia competitor declaration**
INERTIA COMPETITOR: [product name]
Prohibited: any non-grep-checkable phrase.

**1b-iii. Adoption-curve context**
Confirm consistency with the Phase Distribution Target.

---

## STEP 2 -- PHASE MAP TABLE

| Phase | Window | Expected severity range | Expected volume character |
|-------|--------|------------------------|--------------------------|
| Phase 1 | Day 0–30 | P2/P3 | high |
| Phase 2 | Day 31–60 | P1/P2 | medium |
| Phase 3 | Day 61–90 | P0/P1 | medium/low |

---

## STEP 2B -- PHASE BODY TEMPLATE TABLE

| Phase | Adoption stance | Template sentence |
|-------|----------------|-------------------|
| Phase 1 | Dual-tool tension | "I still have [INERTIA COMPETITOR] open in another tab — I keep switching back to check how it handled [specific scenario]." |
| Phase 3 | Parity gap | "In [INERTIA COMPETITOR] I could [specific action] without leaving this screen; here I cannot." |

Phase 1 and Phase 3 bodies: open with the template sentence, placeholders filled concretely.
Phase 2 bodies: reference the competitor where natural.

---

## STEP 2C -- PHASE-SEVERITY INFERENCE RULE

Phase 1 (Day 0–30): P2/P3 non-outage. Fallback available; user is learning.
Phase 3 (Day 61–90): P1/P0 blocking. No fallback; user committed and blocked.

Violation conditions:
- Phase 1 P0/P1 non-outage: violation — correct to P2/P3.
- Phase 3 P3 blocking: violation — correct to P1/P0.

INFERENCE RULE (stated): [your paraphrase of the directional rule above]
Applied in: Steps 5, 5B, and Pass 2 INFERENCE AUDIT

Do not proceed until filled with your own-words paraphrase.

---

## STEP 3 -- ROLE ACTIVATION ORDER (SRE-FIRST)

Activate roles: SRE → Support → PM → UX → C-01 through C-12.

[SRE] — First. Operational failure modes: configuration errors, deployment issues,
on-call escalation, infrastructure-level P0/P1 candidates. Identify Phase 2 escalation
patterns (transition-zone operational friction that surfaces after partial commitment).

[Support] — Second. Triage-queue patterns, documentation gaps, error messages.

[PM] — Third. Intent gaps, roadmap items, feature-request backlog.

[UX] — Fourth. Discoverability failures, onboarding friction, how-to patterns.

[C-01 through C-12] — One ticket hypothesis each. Frame each with phase awareness:
  "In which phase (1, 2, or 3) will this persona most likely encounter this issue?"

---

## STEP 4 -- PERFORMANCE MODE DECLARATION

**You ARE the persona named on each ticket card.**

Your previous primary workflow used [INERTIA COMPETITOR — product name from Step 1b-ii].
Phase 1: old tool still open, can fall back — lower stakes.
Phase 3: committed to new tool, no fallback — higher stakes.

Do not write "the user", "they", "the SRE", "the PM", "the engineer",
or any named-role title in third person.

Prohibited verb-subject forms: "the SRE ran", "the PM reviewed", "the engineer observed",
"the C-07 clicked", "the Support agent opened", or any role-title-preceding-a-verb form.

**Every action in this ticket was taken by "I".
Every old-tool reference uses the product name from Step 1b-ii.**

---

## STEP 5 -- VOCABULARY PRE-COMMITMENT TABLE

Competitor in scope: [product name from Step 1b-ii]

Do not fill any cell in the table until all three items are written:

Required item 1 — INFERENCE RULE (confirmed):
[restate in your own words]

Required item 2 — Verbatim from 2C:
[copy exact first sentence from INFERENCE RULE (stated) at Step 2C — word for word, do not paraphrase]

Required item 3 — PHASE DISTRIBUTION committed block:
Reconcile with Phase Distribution Target from Step 1.
  Phase 1 (Day 0–30): [N] tickets (Step 1 target: [N])
  Phase 2 (Day 31–60): [N] tickets (Step 1 target: [N])
  Phase 3 (Day 61–90): [N] tickets (Step 1 target: [N])
  Total: [N] tickets

Confirmation: this rule applies to every severity assignment in the table below.

| Ticket ID | Phase | Category | Persona | Volume | Severity |
|-----------|-------|----------|---------|--------|----------|
| T-01 | | | | | |
| T-02 | | | | | |
| T-03 | | | | | |
| T-04 | | | | | |
| T-05 | | | | | |
| T-06 | | | | | |
| T-07 | | | | | |
| T-08 | | | | | |

Allowed: Category {how-to, bug, feature-request, config, integration}, Volume {high, medium, low}, Severity {P0, P1, P2, P3}.
**Lock vocabulary values here. Full card bodies follow in Step 6.**

---

## STEP 5B -- COLLECTIVE DISTRIBUTION AUDIT

Constraint 0: Phase counts must match Step 5 committed block.
State: "Phase 1: [n] committed, [n] actual — MATCH/MISMATCH."
Also cross-check against Step 1 target: "Step 1 target vs Step 5 committed: [match/mismatch per phase]."

1. Phase distribution — ≥2 Phase 1, ≥1 Phase 3.
2. Category spread — ≥3 distinct categories.
3. Volume distribution — all three levels.
4. Phase-character compliance — severity/volume match Step 2.
5. Inference-rule compliance — Phase 1/Phase 3 violation scan.

**If any fails, correct and re-run.**

---

## STEP 5C -- PRE-BODY STRUCTURAL VERIFICATION (PASS 2B)

Item 1 — Category distribution check.
Item 2 — Persona distribution check.
Item 3 — Phase distribution compliance.

Item 4 — SWITCHING-FRICTION COUNT CHECK:
SWITCHING-FRICTION COUNT: [N]
N must be ≥ 3. Do not proceed to Step 6 if N < 3.
Third entry must cover a Phase 2 migration barrier (surfaces after partial commitment,
not on day one).

---

## STEP 6 -- FULL CARD BODIES (PHASE-ORGANIZED)

Organize by phase window. Complete all Phase 1 cards, then Phase 2, then Phase 3.
Within each group, ascending Ticket ID order.

### Phase 1 Cards (Day 0–30)

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [match Step 5]
Persona: [match Step 5]
Volume: [match Step 5]
Severity: [match Step 5 — P2 or P3]

Body:
[Open with Phase 1 template sentence, all placeholders filled with the inertia competitor
product name and a concrete scenario. Reference the STATUS QUO element that drives this
ticket's volume. No third-person. Every old-tool reference: product name from Step 1b-ii.]

---

### Phase 2 Cards (Day 31–60)

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [match Step 5]
Persona: [match Step 5]
Volume: [match Step 5]
Severity: [match Step 5 — P1 or P2]

Body:
[Transition framing — user is partially committed, not yet fully detached. Reference the
competitor where the framing naturally calls for it. Reference the STATUS QUO element
from Step 1b-i. No third-person. Product name for old tool.]

---

### Phase 3 Cards (Day 61–90)

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [match Step 5]
Persona: [match Step 5]
Volume: [match Step 5]
Severity: [match Step 5 — P0 or P1]

Body:
[Open with Phase 3 template sentence, all placeholders filled concretely. Reference the
STATUS QUO element that drives this ticket's severity — the user committed fully; the
competitor is not accessible for this workflow. No third-person. Product name for old tool.]

---

## STEP 7 -- CROSS-TICKET PATTERNS

Pattern name: [short name]
Tickets affected: [T-NN, ...]
Root cause: [one sentence]

Consequence — Affected segment:
Prohibited: "users in general", "the team", any unnamed group.
[Named role or cohort tied specifically to this pattern]

Consequence — Day-90 scenario:
Prohibited: "this will cause confusion", any non-pattern-specific event.
[One specific event that occurs if unaddressed by Day 90]

Consequence — Adoption cost:
Prohibited: generic friction not specific to this cohort.
[One sentence quantifying friction for the named segment]

If a pattern involves migration from the inertia competitor, name the competitor.

---

## STEP 8 -- GAP ANALYSIS

### Doc Gaps
[At least one documentation gap.]

### Design Gaps
[At least one design gap.]

### Operational Gaps
[At least one operational gap.]

### Switching-Friction Gaps

Dedicated sub-section for migration barriers only. NOT absorbed into the three sections above.
The three sections above remain present and non-empty.

SWITCHING-FRICTION COUNT: [N]
N must be ≥ 3. State this count before writing any entry.

Template for Entries 1 and 2:

Switching-friction gap: [short name]
Migrating from: [product name from Step 1b-ii — verbatim, grep-checkable]
Expected behavior: [one sentence]
Actual behavior: [one sentence]
Migration impact: [one sentence]

Template for Entry 3 (Phase 2 barrier — extended template):

Switching-friction gap: [short name]
Migrating from: [product name from Step 1b-ii — verbatim, grep-checkable]
Prohibited: a barrier that day-one users would encounter on first contact.
  Disallowed: any friction present before workflow migration has begun; any issue
  a new user who has never committed to this tool would also file.
Trigger event: [name the specific workflow action or system state that first surfaces
  this barrier after partial commitment — must name a concrete post-commitment event
  that day-one users do not reach on first contact]
Expected behavior: [one sentence — based on the user's experience after partial commitment]
Actual behavior: [one sentence]
Migration impact: [one sentence]

Entry-specific guidance:
- Entry 1: Cover the primary day-one migration friction (Phase 1 ticket driver).
- Entry 2: Cover the second most prominent migration barrier.
- Entry 3: Use the extended template. The Prohibited: sentinel and Trigger event field
  apply. The Trigger event must name the specific post-commitment action.

### Pre-Launch Priority
Name the single gap to close first. Tie to specific Ticket IDs, severity, and volume.
State whether it reduces switching-friction for inertia-competitor migrants.

---

## STEP 9 -- DUAL-PASS VERIFICATION

### PASS 1 -- Coverage Trace Table

| Ticket ID | STATUS QUO element referenced | Gap traced to |
|-----------|-------------------------------|---------------|

Populate one row per ticket, in Ticket ID order.

After completing:
1. Confirm: "No gap from the Gap Analysis — including switching-friction gaps — is absent."
2. Confirm: "Inertia competitor product name appears in at least two STATUS QUO element cells."

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 -- Properties Verify + Inference Audit

**PART A — Frontmatter Verify**
Confirm Step 5 matches Step 6 for all fields.
State: "All Step 5 values match Step 6 card bodies."

**PART B — Property Checks**

1. Tool-name fidelity.
   State: "[PRODUCT NAME] in Step 1b-ii: YES. Card bodies: [T-NN, T-NN min].
   Migrating from: field: YES."

2. Phase-differentiated templates.
   State: "Phase 1 template in: [T-NN, T-NN]. Phase 3 template in: [T-NN]."

3. Switching-friction 4-field format.
   State: "All four fields present in all entries: YES / NO."

**PART C — Inference Audit**

**Sub-check 1: Phase-Architecture Severity Compliance**

Scan Phase 1 cards (Phase 1 section, Step 6). Exception sign-off for any P0/P1, or:
"No Phase 1 P0/P1 exceptions. Phase 1 lifecycle: fallback available.
Governing paraphrase clause: [copy the exact Phase 1 clause from INFERENCE RULE (stated)
at Step 2C — do not paraphrase, do not summarize, copy it verbatim word-for-word]."

Scan Phase 2 cards (Phase 2 section, Step 6). Exception sign-off for any P0 escalation, or:
"No Phase 2 P0 escalation exceptions. Phase 2 lifecycle: transition (partial fallback).
Governing paraphrase clause: [copy the exact Phase 2 clause from INFERENCE RULE (stated)
at Step 2C — do not paraphrase, do not summarize, copy it verbatim word-for-word]."

Scan Phase 3 cards (Phase 3 section, Step 6). Exception sign-off for any P3, or:
"No Phase 3 P3 exceptions. Phase 3 lifecycle: no fallback.
Governing paraphrase clause: [copy the exact Phase 3 clause from INFERENCE RULE (stated)
at Step 2C — do not paraphrase, do not summarize, copy it verbatim word-for-word]."

Paraphrase consistency confirmation:
State: "INFERENCE RULE paraphrase (Step 2C): [first 10 words].
Verbatim anchor at Step 5: YES.
All three phase Paraphrase clause fields: triple-clause verbatim (do not paraphrase,
do not summarize, copy it verbatim word-for-word): YES.
Phase 1 compliance: PASS/FAIL.
Phase 2 within P1/P2 range: PASS/FAIL.
Phase 3 compliance: PASS/FAIL.
Paraphrase consistent with audit results: YES / NO."

**Sub-check 2: Switching-Friction Sub-Section Field Completeness**

Restate count: "SWITCHING-FRICTION COUNT: [N]. N ≥ 3: YES/NO."
List each entry's `Migrating from:` value. Flag any non-verbatim.
Quote Entry 3 Trigger event field verbatim: "[quote]"
State: "Sub-section present: YES. All Migrating from: fields verbatim: YES / NO.
Third entry covers Phase 2 migration barrier (not day-one friction): YES / NO.
Entry 3 Prohibited: sentinel present in template (field-adjacent, before Expected behavior:): YES / NO.
Entry 3 Trigger event names a post-commitment workflow action (not day-one): YES / NO."

**Sub-check 3: Post-Generation Phase Distribution Re-Verification**

Count Phase 1, Phase 2, Phase 3 card bodies in Step 6 phase sections.
Complete the table:

| Phase | Bodies generated | Committed (Step 5) | Step 1 target | Match |
|-------|-----------------|-------------------|---------------|-------|
| Phase 1 | [n] | [n] | [n] | MATCH/MISMATCH |
| Phase 2 | [n] | [n] | [n] | MATCH/MISMATCH |
| Phase 3 | [n] | [n] | [n] | MATCH/MISMATCH |
| Total | [n] | [n] | [n] | MATCH/MISMATCH |

If any row shows MISMATCH: name the discrepancy, identify the Ticket ID that drifted
from its committed phase, and state the correction needed. A row-level MISMATCH here
means the pre-generation constraint was satisfied (5B passed) but generation-time drift
occurred — flag explicitly by row.

State final:
"All Step 5 values match Step 6.
Exception sign-offs complete for Phase 1, Phase 2, and Phase 3 scans.
SWITCHING-FRICTION COUNT ≥ 3 confirmed. Third entry covers Phase 2 barrier: YES.
Entry 3 Prohibited: sentinel field-adjacent in template: confirmed.
Entry 3 Trigger event quoted and confirmed: post-commitment action named.
Post-generation phase distribution table complete. All rows: MATCH.
Sub-checks 1, 2, and 3 verified. All C-01 through C-49 constraints met.
C-50 probe (Sub-check 3 table format): complete.
C-51 probe (Phase-2 barrier trigger-event field): complete.
C-52 probe (per-template Prohibited: sentinel in Entry 3): complete."
```
