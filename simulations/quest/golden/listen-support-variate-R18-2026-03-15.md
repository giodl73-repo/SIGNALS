# listen-support Round 18 — Skill Body Prompt Variations

**Date:** 2026-03-15
**Rubric target:** v17 (310 pts ceiling — C-50, C-51, C-52 introduced)
**Base:** V-05 R17 (310/310 under v17 — all C-01 through C-52 at ceiling)

**Variation axes selected** (3 single-axis, then 2 combined):
1. **Role sequence** — Role allocation pre-commitment table declared before role activation; Step 5B and Pass 2 Part B verify role counts match committed allocation (V-01)
2. **Output format** — Phase column added as 2nd column to Pass 1 coverage table; three-phase column coverage confirmed after table completion (V-02)
3. **Inertia framing** — Phase 2 template sentence added to Step 2B alongside Phase 1 and Phase 3; all three phases structurally enforced; Pass 2 Part B item 2 extended to verify Phase 2 template usage (V-03)
4. **V-01 + V-02 combined** — Role allocation table + Phase column in coverage table (V-04)
5. **Full synthesis** — All three axes: role allocation + Phase column + Phase 2 template sentence (V-05)

**R18 criterion hypothesis matrix:**

| Criterion candidate | V-01 | V-02 | V-03 | V-04 | V-05 |
|--------------------|------|------|------|------|------|
| C-01 through C-52 (all prior — 310 pt ceiling) | YES | YES | YES | YES | YES |
| C-53 candidate: Role Allocation Pre-Commitment Table | YES | — | — | YES | YES |
| C-54 candidate: Phase Column in Coverage Table | — | YES | — | YES | YES |
| C-55 candidate: Phase 2 Body Template Sentence | — | — | YES | — | YES |

---

## V-01: Single-Axis — Role Sequence (Role Allocation Pre-Commitment Table)

**Axis:** Role sequence — V-05 R17 activates roles SRE-first but places no pre-declared allocation governing how many tickets each role generates. V-01 R18 adds Step 3A: a ROLE ALLOCATION TABLE the model must fill before any role is activated. Step 5B gains Constraint 1B verifying Persona column counts in Step 5 match the declared allocation. Pass 2 Part B gains item 4 re-checking per-role compliance post-generation. All other mechanisms from V-05 R17 are preserved exactly.

**Probe (C-53 candidate):** V-05 R17 satisfies all phase-distribution constraints (C-45, C-48) through pre-committed phase counts and post-generation re-verification, but places no structural gate on how tickets distribute across roles. A model satisfying every existing criterion can produce 5 SRE tickets out of 8 without triggering any constraint. The failure mode: role saturation is detectable only by reading the Step 5 Persona column after the fact. A ROLE ALLOCATION TABLE pre-commits per-role counts before role activation begins; Constraint 1B fires at Step 5B before body generation, converting the implicit expectation of role diversity into an auditable structural property. Pass 2 Part B item 4 closes the post-generation window.

**Hypothesis:** Role saturation is structurally invisible under V-05 R17 — no criterion requires the Persona column to be distributed across role types, and the phase/category/volume constraints satisfied by any distribution. The C-53 probe tests whether per-role pre-commitment + Step 5B verification is independently extractable as a new criterion from the role activation sequence that V-05 R17 already requires.

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

Constraint: Phase 1 count >= 2. Phase 3 count >= 1. All three phases represented.
This target will be referenced at Step 5 (committed block) and re-verified at Step 5B
and Pass 2 Part C Sub-check 3.

---

## STEP 1B -- INERTIA: STATUS QUO

**1b-i. Current-state baseline**
Describe in 2-3 sentences: what are users doing today? Frame with awareness of
the Phase Distribution Target -- the baseline must generate friction across all three
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
| Phase 1 | Day 0-30 | P2/P3 | high |
| Phase 2 | Day 31-60 | P1/P2 | medium |
| Phase 3 | Day 61-90 | P0/P1 | medium/low |

---

## STEP 2B -- PHASE BODY TEMPLATE TABLE

| Phase | Adoption stance | Template sentence |
|-------|----------------|-------------------|
| Phase 1 | Dual-tool tension | "I still have [INERTIA COMPETITOR] open in another tab -- I keep switching back to check how it handled [specific scenario]." |
| Phase 3 | Parity gap | "In [INERTIA COMPETITOR] I could [specific action] without leaving this screen; here I cannot." |

Phase 1 and Phase 3 bodies: open with the template sentence, placeholders filled concretely.
Phase 2 bodies: reference the competitor where natural.

---

## STEP 2C -- PHASE-SEVERITY INFERENCE RULE

Phase 1 (Day 0-30): P2/P3 non-outage. Fallback available; user is learning.
Phase 3 (Day 61-90): P1/P0 blocking. No fallback; user committed and blocked.

Violation conditions:
- Phase 1 P0/P1 non-outage: violation -- correct to P2/P3.
- Phase 3 P3 blocking: violation -- correct to P1/P0.

INFERENCE RULE (stated): [your paraphrase of the directional rule above]
Applied in: Steps 5, 5B, and Pass 2 INFERENCE AUDIT

Do not proceed until filled with your own-words paraphrase.

---

## STEP 3 -- ROLE ALLOCATION + ACTIVATION (SRE-FIRST)

### Step 3A -- Role Allocation Pre-Commitment

Before activating any role, declare the ticket count each role will generate.

ROLE ALLOCATION TABLE:
| Role | Tickets allocated |
|------|------------------|
| SRE | [N] |
| Support | [N] |
| PM | [N] |
| UX | [N] |
| Customer personas (C-01 through C-12 combined) | [N] |
| Total | [N] |

Constraints:
- SRE >= 1. Support >= 1. Customer personas >= 2.
- Total must equal the Phase Distribution Target total from Step 1.

This table is re-verified at Step 5B Constraint 1B and Pass 2 Part B item 4.
Do not proceed to Step 3B until the table is complete.

### Step 3B -- Role Activation

Activate roles: SRE -> Support -> PM -> UX -> C-01 through C-12.

[SRE] -- First. Operational failure modes: configuration errors, deployment issues,
on-call escalation, infrastructure-level P0/P1 candidates. Identify Phase 2 escalation
patterns (transition-zone operational friction that surfaces after partial commitment).

[Support] -- Second. Triage-queue patterns, documentation gaps, error messages.

[PM] -- Third. Intent gaps, roadmap items, feature-request backlog.

[UX] -- Fourth. Discoverability failures, onboarding friction, how-to patterns.

[C-01 through C-12] -- One ticket hypothesis each. Frame each with phase awareness:
  "In which phase (1, 2, or 3) will this persona most likely encounter this issue?"

---

## STEP 4 -- PERFORMANCE MODE DECLARATION

**You ARE the persona named on each ticket card.**

Your previous primary workflow used [INERTIA COMPETITOR -- product name from Step 1b-ii].
Phase 1: old tool still open, can fall back -- lower stakes.
Phase 3: committed to new tool, no fallback -- higher stakes.

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

Required item 1 -- INFERENCE RULE (confirmed):
[restate in your own words]

Required item 2 -- Verbatim from 2C:
[copy exact first sentence from INFERENCE RULE (stated) at Step 2C -- word for word, do not paraphrase]

Required item 3 -- PHASE DISTRIBUTION committed block:
Reconcile with Phase Distribution Target from Step 1.
  Phase 1 (Day 0-30): [N] tickets (Step 1 target: [N])
  Phase 2 (Day 31-60): [N] tickets (Step 1 target: [N])
  Phase 3 (Day 61-90): [N] tickets (Step 1 target: [N])
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
State: "Phase 1: [n] committed, [n] actual -- MATCH/MISMATCH."
Also cross-check against Step 1 target: "Step 1 target vs Step 5 committed: [match/mismatch per phase]."

Constraint 1B: Role counts must match Step 3A ROLE ALLOCATION TABLE.
State per role: "SRE: [n] allocated, [n] in Step 5 Persona column -- MATCH/MISMATCH."
Repeat for Support, PM, UX, Customer personas, Total.
If any MISMATCH: correct Step 5 before proceeding.

1. Phase distribution -- >=2 Phase 1, >=1 Phase 3.
2. Category spread -- >=3 distinct categories.
3. Volume distribution -- all three levels.
4. Phase-character compliance -- severity/volume match Step 2.
5. Inference-rule compliance -- Phase 1/Phase 3 violation scan.

**If any fails, correct and re-run.**

---

## STEP 5C -- PRE-BODY STRUCTURAL VERIFICATION (PASS 2B)

Item 1 -- Category distribution check.
Item 2 -- Persona distribution check.
Item 3 -- Phase distribution compliance.

Item 4 -- SWITCHING-FRICTION COUNT CHECK:
SWITCHING-FRICTION COUNT: [N]
N must be >= 3. Do not proceed to Step 6 if N < 3.
Third entry must cover a Phase 2 migration barrier (surfaces after partial commitment,
not on day one).

---

## STEP 6 -- FULL CARD BODIES (PHASE-ORGANIZED)

Organize by phase window. Complete all Phase 1 cards, then Phase 2, then Phase 3.
Within each group, ascending Ticket ID order.

### Phase 1 Cards (Day 0-30)

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [match Step 5]
Persona: [match Step 5]
Volume: [match Step 5]
Severity: [match Step 5 -- P2 or P3]

Body:
[Open with Phase 1 template sentence, all placeholders filled with the inertia competitor
product name and a concrete scenario. Reference the STATUS QUO element that drives this
ticket's volume. No third-person. Every old-tool reference: product name from Step 1b-ii.]

---

### Phase 2 Cards (Day 31-60)

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [match Step 5]
Persona: [match Step 5]
Volume: [match Step 5]
Severity: [match Step 5 -- P1 or P2]

Body:
[Transition framing -- user is partially committed, not yet fully detached. Reference the
competitor where the framing naturally calls for it. Reference the STATUS QUO element
from Step 1b-i. No third-person. Product name for old tool.]

---

### Phase 3 Cards (Day 61-90)

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [match Step 5]
Persona: [match Step 5]
Volume: [match Step 5]
Severity: [match Step 5 -- P0 or P1]

Body:
[Open with Phase 3 template sentence, all placeholders filled concretely. Reference the
STATUS QUO element that drives this ticket's severity -- the user committed fully; the
competitor is not accessible for this workflow. No third-person. Product name for old tool.]

---

## STEP 7 -- CROSS-TICKET PATTERNS

Pattern name: [short name]
Tickets affected: [T-NN, ...]
Root cause: [one sentence]

Consequence -- Affected segment:
Prohibited: "users in general", "the team", any unnamed group.
[Named role or cohort tied specifically to this pattern]

Consequence -- Day-90 scenario:
Prohibited: "this will cause confusion", any non-pattern-specific event.
[One specific event that occurs if unaddressed by Day 90]

Consequence -- Adoption cost:
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
N must be >= 3. State this count before writing any entry.

Template for Entries 1 and 2:

Switching-friction gap: [short name]
Migrating from: [product name from Step 1b-ii -- verbatim, grep-checkable]
Expected behavior: [one sentence]
Actual behavior: [one sentence]
Migration impact: [one sentence]

[Entry 3 -- Phase 2 migration barrier -- use this extended template:]

Switching-friction gap: [short name]
Migrating from: [product name from Step 1b-ii -- verbatim, grep-checkable]
Trigger event: [name the specific workflow action or system state that first surfaces
  this barrier after partial commitment -- must name a concrete post-commitment event
  that day-one users do not reach on first contact]
Prohibited: a barrier that day-one users would encounter on first contact.
  Disallowed: any friction present before workflow migration has begun; any issue
  a new user who has never committed to this tool would also file.
Expected behavior: [one sentence -- the behavior the user expected based on their
  experience after partial commitment]
Actual behavior: [one sentence]
Migration impact: [one sentence]

Entry-specific guidance:
- Entry 1: Cover the primary day-one migration friction (Phase 1 ticket driver).
- Entry 2: Cover the second most prominent migration barrier.
- Entry 3: Use the extended template. The Trigger event field must name the specific
  post-commitment workflow action. The Prohibited: sentinel in the template applies
  to this entry.

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
1. Confirm: "No gap from the Gap Analysis -- including switching-friction gaps -- is absent."
2. Confirm: "Inertia competitor product name appears in at least two STATUS QUO element cells."

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 -- Properties Verify + Inference Audit

**PART A -- Frontmatter Verify**
Confirm Step 5 matches Step 6 for all fields.
State: "All Step 5 values match Step 6 card bodies."

**PART B -- Property Checks**

1. Tool-name fidelity.
   State: "[PRODUCT NAME] in Step 1b-ii: YES. Card bodies: [T-NN, T-NN min].
   Migrating from: field: YES."

2. Phase-differentiated templates.
   State: "Phase 1 template in: [T-NN, T-NN]. Phase 3 template in: [T-NN]."

3. Switching-friction 4-field format.
   State: "All four fields present in all entries: YES / NO."

4. Role allocation compliance.
   State: "Step 3A allocation vs Step 5 Persona column --
   SRE: [n] allocated / [n] actual -- MATCH/MISMATCH.
   Support: [n] / [n] -- MATCH/MISMATCH.
   PM: [n] / [n] -- MATCH/MISMATCH.
   UX: [n] / [n] -- MATCH/MISMATCH.
   Customer personas: [n] / [n] -- MATCH/MISMATCH.
   Total: [n] / [n] -- MATCH/MISMATCH."

**PART C -- Inference Audit**

**Sub-check 1: Phase-Architecture Severity Compliance**

Scan Phase 1 cards (Phase 1 section, Step 6). Exception sign-off for any P0/P1, or:
"No Phase 1 P0/P1 exceptions. Phase 1 lifecycle: fallback available.
Governing paraphrase clause: [copy the exact Phase 1 clause from INFERENCE RULE (stated)
at Step 2C -- do not paraphrase, do not summarize, copy it verbatim word-for-word]."

Scan Phase 2 cards (Phase 2 section, Step 6). Exception sign-off for any P0 escalation, or:
"No Phase 2 P0 escalation exceptions. Phase 2 lifecycle: transition (partial fallback).
Governing paraphrase clause: [copy the exact Phase 2 clause from INFERENCE RULE (stated)
at Step 2C -- do not paraphrase, do not summarize, copy it verbatim word-for-word]."

Scan Phase 3 cards (Phase 3 section, Step 6). Exception sign-off for any P3, or:
"No Phase 3 P3 exceptions. Phase 3 lifecycle: no fallback.
Governing paraphrase clause: [copy the exact Phase 3 clause from INFERENCE RULE (stated)
at Step 2C -- do not paraphrase, do not summarize, copy it verbatim word-for-word]."

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

Restate count: "SWITCHING-FRICTION COUNT: [N]. N >= 3: YES/NO."
List each entry's `Migrating from:` value. Flag any non-verbatim.
Quote Entry 3 Trigger event field verbatim: "[quote]"
State: "Sub-section present: YES. All Migrating from: fields verbatim: YES / NO.
Third entry covers Phase 2 migration barrier (not day-one friction): YES / NO.
Entry 3 Trigger event names a post-commitment workflow action (not day-one): YES / NO.
Entry 3 Prohibited: sentinel present in template (field-adjacent): YES / NO."

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
occurred -- flag explicitly by row.

State final:
"All Step 5 values match Step 6.
Exception sign-offs complete for Phase 1, Phase 2, and Phase 3 scans.
SWITCHING-FRICTION COUNT >= 3 confirmed. Third entry covers Phase 2 barrier: YES.
Entry 3 Trigger event quoted and confirmed: post-commitment action named.
Entry 3 Prohibited: sentinel in template (field-adjacent): confirmed.
Post-generation phase distribution table complete. All rows: MATCH.
Role allocation compliance (Step 3A vs Step 5): all roles MATCH.
Sub-checks 1, 2, and 3 verified. All C-01 through C-52 constraints met.
C-53 probe (role allocation pre-commitment table): complete."
```

---

## V-02: Single-Axis — Output Format (Phase Column in Coverage Table)

**Axis:** Output format -- Pass 1 coverage table. V-05 R17 produces a 3-column table (Ticket ID / STATUS QUO element / Gap traced to) with two post-table confirmations: no-orphan-gap and competitor-name presence. V-02 R18 inserts a Phase column as the second column, producing a 4-column table (Ticket ID / Phase / STATUS QUO element / Gap traced to). After completing the table, a third confirmation is added: all three phases represented in the Phase column. All other mechanisms from V-05 R17 are preserved exactly.

**Probe (C-54 candidate):** V-05 R17 satisfies C-17 (3-column gap-bridge table with no-orphan check) and C-15 (table-form coverage enumeration). The failure mode C-17 leaves open: a scorer confirming ticket-to-STATUS-QUO traces and gap coverage cannot verify phase distribution by column scan -- they must cross-reference the Phase column in the Step 5 vocabulary table. The 3-column table is silent on phase: a scorer cannot determine at a glance whether all three phases are represented in the coverage traces. A Phase column in the coverage table makes phase distribution self-verifiable by column scan: a scorer reads down the Phase column and confirms all three values appear without cross-referencing Step 5. The post-table confirmation ("All three phases represented in Phase column: YES") converts the column scan into an explicit auditable claim. C-17 passes with a 3-column table and no-orphan check; C-54 passes only when the coverage table additionally carries a Phase column and the post-table confirmations include an explicit three-phase coverage statement.

**Hypothesis:** The 3-column coverage table closes gap-orphan and competitor-presence failure modes but leaves phase-coverage verification as an implicit cross-reference task. Adding a Phase column applies the same structural independence mechanism as C-15 (table rows make per-ticket traces checkable by row) to phase distribution: a column makes per-phase presence checkable by column value, not by cross-table lookup. The C-54 probe tests whether the Phase column in the coverage table is independently extractable as a criterion from the 3-column structure C-17 already requires.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- PHASE DISTRIBUTION TARGET (declared before STATUS QUO analysis)

Before establishing the STATUS QUO baseline, declare the target ticket distribution.

PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30): [N] tickets
  Phase 2 (Day 31-60): [N] tickets
  Phase 3 (Day 61-90): [N] tickets
  Total: [N] tickets

Constraint: Phase 1 count >= 2. Phase 3 count >= 1. All three phases represented.
This target will be referenced at Step 5 (committed block) and re-verified at Step 5B
and Pass 2 Part C Sub-check 3.

---

## STEP 1B -- INERTIA: STATUS QUO

**1b-i. Current-state baseline**
Describe in 2-3 sentences: what are users doing today? Frame with awareness of
the Phase Distribution Target -- the baseline must generate friction across all three
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
| Phase 1 | Day 0-30 | P2/P3 | high |
| Phase 2 | Day 31-60 | P1/P2 | medium |
| Phase 3 | Day 61-90 | P0/P1 | medium/low |

---

## STEP 2B -- PHASE BODY TEMPLATE TABLE

| Phase | Adoption stance | Template sentence |
|-------|----------------|-------------------|
| Phase 1 | Dual-tool tension | "I still have [INERTIA COMPETITOR] open in another tab -- I keep switching back to check how it handled [specific scenario]." |
| Phase 3 | Parity gap | "In [INERTIA COMPETITOR] I could [specific action] without leaving this screen; here I cannot." |

Phase 1 and Phase 3 bodies: open with the template sentence, placeholders filled concretely.
Phase 2 bodies: reference the competitor where natural.

---

## STEP 2C -- PHASE-SEVERITY INFERENCE RULE

Phase 1 (Day 0-30): P2/P3 non-outage. Fallback available; user is learning.
Phase 3 (Day 61-90): P1/P0 blocking. No fallback; user committed and blocked.

Violation conditions:
- Phase 1 P0/P1 non-outage: violation -- correct to P2/P3.
- Phase 3 P3 blocking: violation -- correct to P1/P0.

INFERENCE RULE (stated): [your paraphrase of the directional rule above]
Applied in: Steps 5, 5B, and Pass 2 INFERENCE AUDIT

Do not proceed until filled with your own-words paraphrase.

---

## STEP 3 -- ROLE ACTIVATION ORDER (SRE-FIRST)

Activate roles: SRE -> Support -> PM -> UX -> C-01 through C-12.

[SRE] -- First. Operational failure modes: configuration errors, deployment issues,
on-call escalation, infrastructure-level P0/P1 candidates. Identify Phase 2 escalation
patterns (transition-zone operational friction that surfaces after partial commitment).

[Support] -- Second. Triage-queue patterns, documentation gaps, error messages.

[PM] -- Third. Intent gaps, roadmap items, feature-request backlog.

[UX] -- Fourth. Discoverability failures, onboarding friction, how-to patterns.

[C-01 through C-12] -- One ticket hypothesis each. Frame each with phase awareness:
  "In which phase (1, 2, or 3) will this persona most likely encounter this issue?"

---

## STEP 4 -- PERFORMANCE MODE DECLARATION

**You ARE the persona named on each ticket card.**

Your previous primary workflow used [INERTIA COMPETITOR -- product name from Step 1b-ii].
Phase 1: old tool still open, can fall back -- lower stakes.
Phase 3: committed to new tool, no fallback -- higher stakes.

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

Required item 1 -- INFERENCE RULE (confirmed):
[restate in your own words]

Required item 2 -- Verbatim from 2C:
[copy exact first sentence from INFERENCE RULE (stated) at Step 2C -- word for word, do not paraphrase]

Required item 3 -- PHASE DISTRIBUTION committed block:
Reconcile with Phase Distribution Target from Step 1.
  Phase 1 (Day 0-30): [N] tickets (Step 1 target: [N])
  Phase 2 (Day 31-60): [N] tickets (Step 1 target: [N])
  Phase 3 (Day 61-90): [N] tickets (Step 1 target: [N])
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
State: "Phase 1: [n] committed, [n] actual -- MATCH/MISMATCH."
Also cross-check against Step 1 target: "Step 1 target vs Step 5 committed: [match/mismatch per phase]."

1. Phase distribution -- >=2 Phase 1, >=1 Phase 3.
2. Category spread -- >=3 distinct categories.
3. Volume distribution -- all three levels.
4. Phase-character compliance -- severity/volume match Step 2.
5. Inference-rule compliance -- Phase 1/Phase 3 violation scan.

**If any fails, correct and re-run.**

---

## STEP 5C -- PRE-BODY STRUCTURAL VERIFICATION (PASS 2B)

Item 1 -- Category distribution check.
Item 2 -- Persona distribution check.
Item 3 -- Phase distribution compliance.

Item 4 -- SWITCHING-FRICTION COUNT CHECK:
SWITCHING-FRICTION COUNT: [N]
N must be >= 3. Do not proceed to Step 6 if N < 3.
Third entry must cover a Phase 2 migration barrier (surfaces after partial commitment,
not on day one).

---

## STEP 6 -- FULL CARD BODIES (PHASE-ORGANIZED)

Organize by phase window. Complete all Phase 1 cards, then Phase 2, then Phase 3.
Within each group, ascending Ticket ID order.

### Phase 1 Cards (Day 0-30)

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [match Step 5]
Persona: [match Step 5]
Volume: [match Step 5]
Severity: [match Step 5 -- P2 or P3]

Body:
[Open with Phase 1 template sentence, all placeholders filled with the inertia competitor
product name and a concrete scenario. Reference the STATUS QUO element that drives this
ticket's volume. No third-person. Every old-tool reference: product name from Step 1b-ii.]

---

### Phase 2 Cards (Day 31-60)

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [match Step 5]
Persona: [match Step 5]
Volume: [match Step 5]
Severity: [match Step 5 -- P1 or P2]

Body:
[Transition framing -- user is partially committed, not yet fully detached. Reference the
competitor where the framing naturally calls for it. Reference the STATUS QUO element
from Step 1b-i. No third-person. Product name for old tool.]

---

### Phase 3 Cards (Day 61-90)

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [match Step 5]
Persona: [match Step 5]
Volume: [match Step 5]
Severity: [match Step 5 -- P0 or P1]

Body:
[Open with Phase 3 template sentence, all placeholders filled concretely. Reference the
STATUS QUO element that drives this ticket's severity -- the user committed fully; the
competitor is not accessible for this workflow. No third-person. Product name for old tool.]

---

## STEP 7 -- CROSS-TICKET PATTERNS

Pattern name: [short name]
Tickets affected: [T-NN, ...]
Root cause: [one sentence]

Consequence -- Affected segment:
Prohibited: "users in general", "the team", any unnamed group.
[Named role or cohort tied specifically to this pattern]

Consequence -- Day-90 scenario:
Prohibited: "this will cause confusion", any non-pattern-specific event.
[One specific event that occurs if unaddressed by Day 90]

Consequence -- Adoption cost:
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
N must be >= 3. State this count before writing any entry.

Template for Entries 1 and 2:

Switching-friction gap: [short name]
Migrating from: [product name from Step 1b-ii -- verbatim, grep-checkable]
Expected behavior: [one sentence]
Actual behavior: [one sentence]
Migration impact: [one sentence]

[Entry 3 -- Phase 2 migration barrier -- use this extended template:]

Switching-friction gap: [short name]
Migrating from: [product name from Step 1b-ii -- verbatim, grep-checkable]
Trigger event: [name the specific workflow action or system state that first surfaces
  this barrier after partial commitment -- must name a concrete post-commitment event
  that day-one users do not reach on first contact]
Prohibited: a barrier that day-one users would encounter on first contact.
  Disallowed: any friction present before workflow migration has begun; any issue
  a new user who has never committed to this tool would also file.
Expected behavior: [one sentence -- the behavior the user expected based on their
  experience after partial commitment]
Actual behavior: [one sentence]
Migration impact: [one sentence]

Entry-specific guidance:
- Entry 1: Cover the primary day-one migration friction (Phase 1 ticket driver).
- Entry 2: Cover the second most prominent migration barrier.
- Entry 3: Use the extended template. The Trigger event field must name the specific
  post-commitment workflow action. The Prohibited: sentinel in the template applies
  to this entry.

### Pre-Launch Priority
Name the single gap to close first. Tie to specific Ticket IDs, severity, and volume.
State whether it reduces switching-friction for inertia-competitor migrants.

---

## STEP 9 -- DUAL-PASS VERIFICATION

### PASS 1 -- Coverage Trace Table

| Ticket ID | Phase | STATUS QUO element referenced | Gap traced to |
|-----------|-------|-------------------------------|---------------|

Populate one row per ticket, in Ticket ID order.

After completing:
1. Confirm: "No gap from the Gap Analysis -- including switching-friction gaps -- is absent."
2. Confirm: "Inertia competitor product name appears in at least two STATUS QUO element cells."
3. Confirm: "All three phases represented in Phase column -- Phase 1: [n] rows, Phase 2: [n] rows,
   Phase 3: [n] rows. Three-phase coverage: YES."

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 -- Properties Verify + Inference Audit

**PART A -- Frontmatter Verify**
Confirm Step 5 matches Step 6 for all fields.
State: "All Step 5 values match Step 6 card bodies."

**PART B -- Property Checks**

1. Tool-name fidelity.
   State: "[PRODUCT NAME] in Step 1b-ii: YES. Card bodies: [T-NN, T-NN min].
   Migrating from: field: YES."

2. Phase-differentiated templates.
   State: "Phase 1 template in: [T-NN, T-NN]. Phase 3 template in: [T-NN]."

3. Switching-friction 4-field format.
   State: "All four fields present in all entries: YES / NO."

**PART C -- Inference Audit**

**Sub-check 1: Phase-Architecture Severity Compliance**

Scan Phase 1 cards (Phase 1 section, Step 6). Exception sign-off for any P0/P1, or:
"No Phase 1 P0/P1 exceptions. Phase 1 lifecycle: fallback available.
Governing paraphrase clause: [copy the exact Phase 1 clause from INFERENCE RULE (stated)
at Step 2C -- do not paraphrase, do not summarize, copy it verbatim word-for-word]."

Scan Phase 2 cards (Phase 2 section, Step 6). Exception sign-off for any P0 escalation, or:
"No Phase 2 P0 escalation exceptions. Phase 2 lifecycle: transition (partial fallback).
Governing paraphrase clause: [copy the exact Phase 2 clause from INFERENCE RULE (stated)
at Step 2C -- do not paraphrase, do not summarize, copy it verbatim word-for-word]."

Scan Phase 3 cards (Phase 3 section, Step 6). Exception sign-off for any P3, or:
"No Phase 3 P3 exceptions. Phase 3 lifecycle: no fallback.
Governing paraphrase clause: [copy the exact Phase 3 clause from INFERENCE RULE (stated)
at Step 2C -- do not paraphrase, do not summarize, copy it verbatim word-for-word]."

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

Restate count: "SWITCHING-FRICTION COUNT: [N]. N >= 3: YES/NO."
List each entry's `Migrating from:` value. Flag any non-verbatim.
Quote Entry 3 Trigger event field verbatim: "[quote]"
State: "Sub-section present: YES. All Migrating from: fields verbatim: YES / NO.
Third entry covers Phase 2 migration barrier (not day-one friction): YES / NO.
Entry 3 Trigger event names a post-commitment workflow action (not day-one): YES / NO.
Entry 3 Prohibited: sentinel present in template (field-adjacent): YES / NO."

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
occurred -- flag explicitly by row.

State final:
"All Step 5 values match Step 6.
Exception sign-offs complete for Phase 1, Phase 2, and Phase 3 scans.
SWITCHING-FRICTION COUNT >= 3 confirmed. Third entry covers Phase 2 barrier: YES.
Entry 3 Trigger event quoted and confirmed: post-commitment action named.
Entry 3 Prohibited: sentinel in template (field-adjacent): confirmed.
Post-generation phase distribution table complete. All rows: MATCH.
Phase column in coverage table: all three phases represented -- confirmed.
Sub-checks 1, 2, and 3 verified. All C-01 through C-52 constraints met.
C-54 probe (Phase column in coverage table): complete."
```

---

## V-03: Single-Axis — Inertia Framing (Phase 2 Body Template Sentence)

**Axis:** Inertia framing -- Phase 2 card body generation. V-05 R17 provides structured template sentences for Phase 1 (dual-tool tension) and Phase 3 (parity gap) in the Step 2B table, and instructs Phase 2 bodies to "reference the competitor where natural." V-03 R18 adds a Phase 2 row to the Step 2B table with a "Partial migration" stance and a required opening sentence. Phase 2 bodies must open with this template sentence. Pass 2 Part B item 2 extends to verify Phase 2 template usage alongside Phase 1 and Phase 3. All other mechanisms from V-05 R17 are preserved exactly.

**Probe (C-55 candidate):** V-05 R17 satisfies C-27 (named inertia competitor phase framing) by requiring Phase 1 and Phase 3 bodies to open with structured template sentences that name the competitor and establish the adoption stance. The failure mode V-05 R17 leaves open: Phase 2 bodies reference the competitor "where natural" -- a non-structural instruction that permits omission. A Phase 2 card whose body never names the competitor satisfies no structural constraint in V-05 R17, since Part B item 2 only checks Phase 1 and Phase 3 template presence. The "partial migration" stance is the defining characteristic of Phase 2 -- the user has started migrating workflows but has not fully detached from the competitor. A Phase 2 body that does not open from this stance can satisfy all severity and volume constraints while producing competitor-free, context-free framing. A Phase 2 template sentence structurally enforces the partial-migration stance at body-open time; Part B item 2 extended to three phases makes Phase 2 template compliance independently auditable. C-27 passes when Phase 1 and Phase 3 bodies use named-competitor phase templates; C-55 passes only when Phase 2 bodies additionally open with a structured partial-migration template sentence and Part B item 2 confirms Phase 2 template usage by Ticket ID.

**Hypothesis:** Phase 1 and Phase 3 inertia framing is structurally enforced via Step 2B template sentences and Part B item 2 verification. Phase 2 inertia framing is instructional only: "reference the competitor where natural" is a content recommendation, not a structural constraint with a post-generation check. The C-55 probe tests whether a Phase 2 template sentence + Part B item 2 extension is independently extractable as a new criterion from the two-phase template structure V-05 R17 already requires.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- PHASE DISTRIBUTION TARGET (declared before STATUS QUO analysis)

Before establishing the STATUS QUO baseline, declare the target ticket distribution.

PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30): [N] tickets
  Phase 2 (Day 31-60): [N] tickets
  Phase 3 (Day 61-90): [N] tickets
  Total: [N] tickets

Constraint: Phase 1 count >= 2. Phase 3 count >= 1. All three phases represented.
This target will be referenced at Step 5 (committed block) and re-verified at Step 5B
and Pass 2 Part C Sub-check 3.

---

## STEP 1B -- INERTIA: STATUS QUO

**1b-i. Current-state baseline**
Describe in 2-3 sentences: what are users doing today? Frame with awareness of
the Phase Distribution Target -- the baseline must generate friction across all three
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
| Phase 1 | Day 0-30 | P2/P3 | high |
| Phase 2 | Day 31-60 | P1/P2 | medium |
| Phase 3 | Day 61-90 | P0/P1 | medium/low |

---

## STEP 2B -- PHASE BODY TEMPLATE TABLE

| Phase | Adoption stance | Template sentence |
|-------|----------------|-------------------|
| Phase 1 | Dual-tool tension | "I still have [INERTIA COMPETITOR] open in another tab -- I keep switching back to check how it handled [specific scenario]." |
| Phase 2 | Partial migration | "I've migrated [specific workflow] to this tool but I'm still running [specific workflow] in [INERTIA COMPETITOR] -- and today I hit a wall when [specific blocking event]." |
| Phase 3 | Parity gap | "In [INERTIA COMPETITOR] I could [specific action] without leaving this screen; here I cannot." |

All three phases: open with the template sentence, all placeholders filled concretely.
Every placeholder must name a specific workflow, scenario, or event -- no generic fills.
Every [INERTIA COMPETITOR] placeholder: use the exact product name from Step 1b-ii.

---

## STEP 2C -- PHASE-SEVERITY INFERENCE RULE

Phase 1 (Day 0-30): P2/P3 non-outage. Fallback available; user is learning.
Phase 3 (Day 61-90): P1/P0 blocking. No fallback; user committed and blocked.

Violation conditions:
- Phase 1 P0/P1 non-outage: violation -- correct to P2/P3.
- Phase 3 P3 blocking: violation -- correct to P1/P0.

INFERENCE RULE (stated): [your paraphrase of the directional rule above]
Applied in: Steps 5, 5B, and Pass 2 INFERENCE AUDIT

Do not proceed until filled with your own-words paraphrase.

---

## STEP 3 -- ROLE ACTIVATION ORDER (SRE-FIRST)

Activate roles: SRE -> Support -> PM -> UX -> C-01 through C-12.

[SRE] -- First. Operational failure modes: configuration errors, deployment issues,
on-call escalation, infrastructure-level P0/P1 candidates. Identify Phase 2 escalation
patterns (transition-zone operational friction that surfaces after partial commitment).

[Support] -- Second. Triage-queue patterns, documentation gaps, error messages.

[PM] -- Third. Intent gaps, roadmap items, feature-request backlog.

[UX] -- Fourth. Discoverability failures, onboarding friction, how-to patterns.

[C-01 through C-12] -- One ticket hypothesis each. Frame each with phase awareness:
  "In which phase (1, 2, or 3) will this persona most likely encounter this issue?"

---

## STEP 4 -- PERFORMANCE MODE DECLARATION

**You ARE the persona named on each ticket card.**

Your previous primary workflow used [INERTIA COMPETITOR -- product name from Step 1b-ii].
Phase 1: old tool still open, can fall back -- lower stakes.
Phase 3: committed to new tool, no fallback -- higher stakes.

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

Required item 1 -- INFERENCE RULE (confirmed):
[restate in your own words]

Required item 2 -- Verbatim from 2C:
[copy exact first sentence from INFERENCE RULE (stated) at Step 2C -- word for word, do not paraphrase]

Required item 3 -- PHASE DISTRIBUTION committed block:
Reconcile with Phase Distribution Target from Step 1.
  Phase 1 (Day 0-30): [N] tickets (Step 1 target: [N])
  Phase 2 (Day 31-60): [N] tickets (Step 1 target: [N])
  Phase 3 (Day 61-90): [N] tickets (Step 1 target: [N])
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
State: "Phase 1: [n] committed, [n] actual -- MATCH/MISMATCH."
Also cross-check against Step 1 target: "Step 1 target vs Step 5 committed: [match/mismatch per phase]."

1. Phase distribution -- >=2 Phase 1, >=1 Phase 3.
2. Category spread -- >=3 distinct categories.
3. Volume distribution -- all three levels.
4. Phase-character compliance -- severity/volume match Step 2.
5. Inference-rule compliance -- Phase 1/Phase 3 violation scan.

**If any fails, correct and re-run.**

---

## STEP 5C -- PRE-BODY STRUCTURAL VERIFICATION (PASS 2B)

Item 1 -- Category distribution check.
Item 2 -- Persona distribution check.
Item 3 -- Phase distribution compliance.

Item 4 -- SWITCHING-FRICTION COUNT CHECK:
SWITCHING-FRICTION COUNT: [N]
N must be >= 3. Do not proceed to Step 6 if N < 3.
Third entry must cover a Phase 2 migration barrier (surfaces after partial commitment,
not on day one).

---

## STEP 6 -- FULL CARD BODIES (PHASE-ORGANIZED)

Organize by phase window. Complete all Phase 1 cards, then Phase 2, then Phase 3.
Within each group, ascending Ticket ID order.

### Phase 1 Cards (Day 0-30)

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [match Step 5]
Persona: [match Step 5]
Volume: [match Step 5]
Severity: [match Step 5 -- P2 or P3]

Body:
[Open with Phase 1 template sentence from Step 2B, all placeholders filled with the inertia
competitor product name and a concrete scenario. Reference the STATUS QUO element that drives
this ticket's volume. No third-person. Every old-tool reference: product name from Step 1b-ii.]

---

### Phase 2 Cards (Day 31-60)

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [match Step 5]
Persona: [match Step 5]
Volume: [match Step 5]
Severity: [match Step 5 -- P1 or P2]

Body:
[Open with Phase 2 template sentence from Step 2B, all placeholders filled: name the specific
migrated workflow, the specific workflow still running in the competitor, and the specific
blocking event. Reference the STATUS QUO element from Step 1b-i. No third-person.
Product name for old tool: use verbatim product name from Step 1b-ii.]

---

### Phase 3 Cards (Day 61-90)

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [match Step 5]
Persona: [match Step 5]
Volume: [match Step 5]
Severity: [match Step 5 -- P0 or P1]

Body:
[Open with Phase 3 template sentence from Step 2B, all placeholders filled concretely.
Reference the STATUS QUO element that drives this ticket's severity -- the user committed
fully; the competitor is not accessible for this workflow. No third-person.
Product name for old tool: verbatim from Step 1b-ii.]

---

## STEP 7 -- CROSS-TICKET PATTERNS

Pattern name: [short name]
Tickets affected: [T-NN, ...]
Root cause: [one sentence]

Consequence -- Affected segment:
Prohibited: "users in general", "the team", any unnamed group.
[Named role or cohort tied specifically to this pattern]

Consequence -- Day-90 scenario:
Prohibited: "this will cause confusion", any non-pattern-specific event.
[One specific event that occurs if unaddressed by Day 90]

Consequence -- Adoption cost:
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
N must be >= 3. State this count before writing any entry.

Template for Entries 1 and 2:

Switching-friction gap: [short name]
Migrating from: [product name from Step 1b-ii -- verbatim, grep-checkable]
Expected behavior: [one sentence]
Actual behavior: [one sentence]
Migration impact: [one sentence]

[Entry 3 -- Phase 2 migration barrier -- use this extended template:]

Switching-friction gap: [short name]
Migrating from: [product name from Step 1b-ii -- verbatim, grep-checkable]
Trigger event: [name the specific workflow action or system state that first surfaces
  this barrier after partial commitment -- must name a concrete post-commitment event
  that day-one users do not reach on first contact]
Prohibited: a barrier that day-one users would encounter on first contact.
  Disallowed: any friction present before workflow migration has begun; any issue
  a new user who has never committed to this tool would also file.
Expected behavior: [one sentence -- the behavior the user expected based on their
  experience after partial commitment]
Actual behavior: [one sentence]
Migration impact: [one sentence]

Entry-specific guidance:
- Entry 1: Cover the primary day-one migration friction (Phase 1 ticket driver).
- Entry 2: Cover the second most prominent migration barrier.
- Entry 3: Use the extended template. The Trigger event field must name the specific
  post-commitment workflow action. The Prohibited: sentinel in the template applies
  to this entry.

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
1. Confirm: "No gap from the Gap Analysis -- including switching-friction gaps -- is absent."
2. Confirm: "Inertia competitor product name appears in at least two STATUS QUO element cells."

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 -- Properties Verify + Inference Audit

**PART A -- Frontmatter Verify**
Confirm Step 5 matches Step 6 for all fields.
State: "All Step 5 values match Step 6 card bodies."

**PART B -- Property Checks**

1. Tool-name fidelity.
   State: "[PRODUCT NAME] in Step 1b-ii: YES. Card bodies: [T-NN, T-NN min].
   Migrating from: field: YES."

2. Phase-differentiated templates.
   State: "Phase 1 template in: [T-NN, T-NN]. Phase 2 template in: [T-NN, T-NN].
   Phase 3 template in: [T-NN]."

3. Switching-friction 4-field format.
   State: "All four fields present in all entries: YES / NO."

**PART C -- Inference Audit**

**Sub-check 1: Phase-Architecture Severity Compliance**

Scan Phase 1 cards (Phase 1 section, Step 6). Exception sign-off for any P0/P1, or:
"No Phase 1 P0/P1 exceptions. Phase 1 lifecycle: fallback available.
Governing paraphrase clause: [copy the exact Phase 1 clause from INFERENCE RULE (stated)
at Step 2C -- do not paraphrase, do not summarize, copy it verbatim word-for-word]."

Scan Phase 2 cards (Phase 2 section, Step 6). Exception sign-off for any P0 escalation, or:
"No Phase 2 P0 escalation exceptions. Phase 2 lifecycle: transition (partial fallback).
Governing paraphrase clause: [copy the exact Phase 2 clause from INFERENCE RULE (stated)
at Step 2C -- do not paraphrase, do not summarize, copy it verbatim word-for-word]."

Scan Phase 3 cards (Phase 3 section, Step 6). Exception sign-off for any P3, or:
"No Phase 3 P3 exceptions. Phase 3 lifecycle: no fallback.
Governing paraphrase clause: [copy the exact Phase 3 clause from INFERENCE RULE (stated)
at Step 2C -- do not paraphrase, do not summarize, copy it verbatim word-for-word]."

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

Restate count: "SWITCHING-FRICTION COUNT: [N]. N >= 3: YES/NO."
List each entry's `Migrating from:` value. Flag any non-verbatim.
Quote Entry 3 Trigger event field verbatim: "[quote]"
State: "Sub-section present: YES. All Migrating from: fields verbatim: YES / NO.
Third entry covers Phase 2 migration barrier (not day-one friction): YES / NO.
Entry 3 Trigger event names a post-commitment workflow action (not day-one): YES / NO.
Entry 3 Prohibited: sentinel present in template (field-adjacent): YES / NO."

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
occurred -- flag explicitly by row.

State final:
"All Step 5 values match Step 6.
Exception sign-offs complete for Phase 1, Phase 2, and Phase 3 scans.
SWITCHING-FRICTION COUNT >= 3 confirmed. Third entry covers Phase 2 barrier: YES.
Entry 3 Trigger event quoted and confirmed: post-commitment action named.
Entry 3 Prohibited: sentinel in template (field-adjacent): confirmed.
Post-generation phase distribution table complete. All rows: MATCH.
Phase 2 template verified in: [T-NN, T-NN]. All three phase templates confirmed.
Sub-checks 1, 2, and 3 verified. All C-01 through C-52 constraints met.
C-55 probe (Phase 2 body template sentence): complete."
```

---

## V-04: Combined — V-01 + V-02 (Role Allocation Table + Phase Column in Coverage Table)

**Axis:** V-01 (Role Allocation Pre-Commitment Table) + V-02 (Phase Column in Coverage Table). Targets 310/310 on v17 plus potential above-ceiling credit on C-53 and C-54 candidates.

**Hypothesis:** C-53 and C-54 are structurally independent: C-53 targets pre-generation role distribution (how many tickets per role are pre-committed in Step 3A), C-54 targets post-generation coverage table structure (whether phase is visible as a column). Combining both closes two distinct failure modes simultaneously: role saturation undetected before body generation, and phase coverage requiring cross-table lookup after body generation. V-04 tests whether both probes coexist without structural interference.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- PHASE DISTRIBUTION TARGET (declared before STATUS QUO analysis)

Before establishing the STATUS QUO baseline, declare the target ticket distribution.

PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30): [N] tickets
  Phase 2 (Day 31-60): [N] tickets
  Phase 3 (Day 61-90): [N] tickets
  Total: [N] tickets

Constraint: Phase 1 count >= 2. Phase 3 count >= 1. All three phases represented.
This target will be referenced at Step 5 (committed block) and re-verified at Step 5B
and Pass 2 Part C Sub-check 3.

---

## STEP 1B -- INERTIA: STATUS QUO

**1b-i. Current-state baseline**
Describe in 2-3 sentences: what are users doing today? Frame with awareness of
the Phase Distribution Target -- the baseline must generate friction across all three
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
| Phase 1 | Day 0-30 | P2/P3 | high |
| Phase 2 | Day 31-60 | P1/P2 | medium |
| Phase 3 | Day 61-90 | P0/P1 | medium/low |

---

## STEP 2B -- PHASE BODY TEMPLATE TABLE

| Phase | Adoption stance | Template sentence |
|-------|----------------|-------------------|
| Phase 1 | Dual-tool tension | "I still have [INERTIA COMPETITOR] open in another tab -- I keep switching back to check how it handled [specific scenario]." |
| Phase 3 | Parity gap | "In [INERTIA COMPETITOR] I could [specific action] without leaving this screen; here I cannot." |

Phase 1 and Phase 3 bodies: open with the template sentence, placeholders filled concretely.
Phase 2 bodies: reference the competitor where natural.

---

## STEP 2C -- PHASE-SEVERITY INFERENCE RULE

Phase 1 (Day 0-30): P2/P3 non-outage. Fallback available; user is learning.
Phase 3 (Day 61-90): P1/P0 blocking. No fallback; user committed and blocked.

Violation conditions:
- Phase 1 P0/P1 non-outage: violation -- correct to P2/P3.
- Phase 3 P3 blocking: violation -- correct to P1/P0.

INFERENCE RULE (stated): [your paraphrase of the directional rule above]
Applied in: Steps 5, 5B, and Pass 2 INFERENCE AUDIT

Do not proceed until filled with your own-words paraphrase.

---

## STEP 3 -- ROLE ALLOCATION + ACTIVATION (SRE-FIRST)

### Step 3A -- Role Allocation Pre-Commitment

Before activating any role, declare the ticket count each role will generate.

ROLE ALLOCATION TABLE:
| Role | Tickets allocated |
|------|------------------|
| SRE | [N] |
| Support | [N] |
| PM | [N] |
| UX | [N] |
| Customer personas (C-01 through C-12 combined) | [N] |
| Total | [N] |

Constraints:
- SRE >= 1. Support >= 1. Customer personas >= 2.
- Total must equal the Phase Distribution Target total from Step 1.

This table is re-verified at Step 5B Constraint 1B and Pass 2 Part B item 4.
Do not proceed to Step 3B until the table is complete.

### Step 3B -- Role Activation

Activate roles: SRE -> Support -> PM -> UX -> C-01 through C-12.

[SRE] -- First. Operational failure modes: configuration errors, deployment issues,
on-call escalation, infrastructure-level P0/P1 candidates. Identify Phase 2 escalation
patterns (transition-zone operational friction that surfaces after partial commitment).

[Support] -- Second. Triage-queue patterns, documentation gaps, error messages.

[PM] -- Third. Intent gaps, roadmap items, feature-request backlog.

[UX] -- Fourth. Discoverability failures, onboarding friction, how-to patterns.

[C-01 through C-12] -- One ticket hypothesis each. Frame each with phase awareness:
  "In which phase (1, 2, or 3) will this persona most likely encounter this issue?"

---

## STEP 4 -- PERFORMANCE MODE DECLARATION

**You ARE the persona named on each ticket card.**

Your previous primary workflow used [INERTIA COMPETITOR -- product name from Step 1b-ii].
Phase 1: old tool still open, can fall back -- lower stakes.
Phase 3: committed to new tool, no fallback -- higher stakes.

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

Required item 1 -- INFERENCE RULE (confirmed):
[restate in your own words]

Required item 2 -- Verbatim from 2C:
[copy exact first sentence from INFERENCE RULE (stated) at Step 2C -- word for word, do not paraphrase]

Required item 3 -- PHASE DISTRIBUTION committed block:
Reconcile with Phase Distribution Target from Step 1.
  Phase 1 (Day 0-30): [N] tickets (Step 1 target: [N])
  Phase 2 (Day 31-60): [N] tickets (Step 1 target: [N])
  Phase 3 (Day 61-90): [N] tickets (Step 1 target: [N])
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
State: "Phase 1: [n] committed, [n] actual -- MATCH/MISMATCH."
Also cross-check against Step 1 target: "Step 1 target vs Step 5 committed: [match/mismatch per phase]."

Constraint 1B: Role counts must match Step 3A ROLE ALLOCATION TABLE.
State per role: "SRE: [n] allocated, [n] in Step 5 Persona column -- MATCH/MISMATCH."
Repeat for Support, PM, UX, Customer personas, Total.
If any MISMATCH: correct Step 5 before proceeding.

1. Phase distribution -- >=2 Phase 1, >=1 Phase 3.
2. Category spread -- >=3 distinct categories.
3. Volume distribution -- all three levels.
4. Phase-character compliance -- severity/volume match Step 2.
5. Inference-rule compliance -- Phase 1/Phase 3 violation scan.

**If any fails, correct and re-run.**

---

## STEP 5C -- PRE-BODY STRUCTURAL VERIFICATION (PASS 2B)

Item 1 -- Category distribution check.
Item 2 -- Persona distribution check.
Item 3 -- Phase distribution compliance.

Item 4 -- SWITCHING-FRICTION COUNT CHECK:
SWITCHING-FRICTION COUNT: [N]
N must be >= 3. Do not proceed to Step 6 if N < 3.
Third entry must cover a Phase 2 migration barrier (surfaces after partial commitment,
not on day one).

---

## STEP 6 -- FULL CARD BODIES (PHASE-ORGANIZED)

Organize by phase window. Complete all Phase 1 cards, then Phase 2, then Phase 3.
Within each group, ascending Ticket ID order.

### Phase 1 Cards (Day 0-30)

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [match Step 5]
Persona: [match Step 5]
Volume: [match Step 5]
Severity: [match Step 5 -- P2 or P3]

Body:
[Open with Phase 1 template sentence, all placeholders filled with the inertia competitor
product name and a concrete scenario. Reference the STATUS QUO element that drives this
ticket's volume. No third-person. Every old-tool reference: product name from Step 1b-ii.]

---

### Phase 2 Cards (Day 31-60)

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [match Step 5]
Persona: [match Step 5]
Volume: [match Step 5]
Severity: [match Step 5 -- P1 or P2]

Body:
[Transition framing -- user is partially committed, not yet fully detached. Reference the
competitor where the framing naturally calls for it. Reference the STATUS QUO element
from Step 1b-i. No third-person. Product name for old tool.]

---

### Phase 3 Cards (Day 61-90)

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [match Step 5]
Persona: [match Step 5]
Volume: [match Step 5]
Severity: [match Step 5 -- P0 or P1]

Body:
[Open with Phase 3 template sentence, all placeholders filled concretely. Reference the
STATUS QUO element that drives this ticket's severity -- the user committed fully; the
competitor is not accessible for this workflow. No third-person. Product name for old tool.]

---

## STEP 7 -- CROSS-TICKET PATTERNS

Pattern name: [short name]
Tickets affected: [T-NN, ...]
Root cause: [one sentence]

Consequence -- Affected segment:
Prohibited: "users in general", "the team", any unnamed group.
[Named role or cohort tied specifically to this pattern]

Consequence -- Day-90 scenario:
Prohibited: "this will cause confusion", any non-pattern-specific event.
[One specific event that occurs if unaddressed by Day 90]

Consequence -- Adoption cost:
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
N must be >= 3. State this count before writing any entry.

Template for Entries 1 and 2:

Switching-friction gap: [short name]
Migrating from: [product name from Step 1b-ii -- verbatim, grep-checkable]
Expected behavior: [one sentence]
Actual behavior: [one sentence]
Migration impact: [one sentence]

[Entry 3 -- Phase 2 migration barrier -- use this extended template:]

Switching-friction gap: [short name]
Migrating from: [product name from Step 1b-ii -- verbatim, grep-checkable]
Trigger event: [name the specific workflow action or system state that first surfaces
  this barrier after partial commitment -- must name a concrete post-commitment event
  that day-one users do not reach on first contact]
Prohibited: a barrier that day-one users would encounter on first contact.
  Disallowed: any friction present before workflow migration has begun; any issue
  a new user who has never committed to this tool would also file.
Expected behavior: [one sentence -- the behavior the user expected based on their
  experience after partial commitment]
Actual behavior: [one sentence]
Migration impact: [one sentence]

Entry-specific guidance:
- Entry 1: Cover the primary day-one migration friction (Phase 1 ticket driver).
- Entry 2: Cover the second most prominent migration barrier.
- Entry 3: Use the extended template. The Trigger event field must name the specific
  post-commitment workflow action. The Prohibited: sentinel in the template applies
  to this entry.

### Pre-Launch Priority
Name the single gap to close first. Tie to specific Ticket IDs, severity, and volume.
State whether it reduces switching-friction for inertia-competitor migrants.

---

## STEP 9 -- DUAL-PASS VERIFICATION

### PASS 1 -- Coverage Trace Table

| Ticket ID | Phase | STATUS QUO element referenced | Gap traced to |
|-----------|-------|-------------------------------|---------------|

Populate one row per ticket, in Ticket ID order.

After completing:
1. Confirm: "No gap from the Gap Analysis -- including switching-friction gaps -- is absent."
2. Confirm: "Inertia competitor product name appears in at least two STATUS QUO element cells."
3. Confirm: "All three phases represented in Phase column -- Phase 1: [n] rows, Phase 2: [n] rows,
   Phase 3: [n] rows. Three-phase coverage: YES."

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 -- Properties Verify + Inference Audit

**PART A -- Frontmatter Verify**
Confirm Step 5 matches Step 6 for all fields.
State: "All Step 5 values match Step 6 card bodies."

**PART B -- Property Checks**

1. Tool-name fidelity.
   State: "[PRODUCT NAME] in Step 1b-ii: YES. Card bodies: [T-NN, T-NN min].
   Migrating from: field: YES."

2. Phase-differentiated templates.
   State: "Phase 1 template in: [T-NN, T-NN]. Phase 3 template in: [T-NN]."

3. Switching-friction 4-field format.
   State: "All four fields present in all entries: YES / NO."

4. Role allocation compliance.
   State: "Step 3A allocation vs Step 5 Persona column --
   SRE: [n] allocated / [n] actual -- MATCH/MISMATCH.
   Support: [n] / [n] -- MATCH/MISMATCH.
   PM: [n] / [n] -- MATCH/MISMATCH.
   UX: [n] / [n] -- MATCH/MISMATCH.
   Customer personas: [n] / [n] -- MATCH/MISMATCH.
   Total: [n] / [n] -- MATCH/MISMATCH."

**PART C -- Inference Audit**

**Sub-check 1: Phase-Architecture Severity Compliance**

Scan Phase 1 cards (Phase 1 section, Step 6). Exception sign-off for any P0/P1, or:
"No Phase 1 P0/P1 exceptions. Phase 1 lifecycle: fallback available.
Governing paraphrase clause: [copy the exact Phase 1 clause from INFERENCE RULE (stated)
at Step 2C -- do not paraphrase, do not summarize, copy it verbatim word-for-word]."

Scan Phase 2 cards (Phase 2 section, Step 6). Exception sign-off for any P0 escalation, or:
"No Phase 2 P0 escalation exceptions. Phase 2 lifecycle: transition (partial fallback).
Governing paraphrase clause: [copy the exact Phase 2 clause from INFERENCE RULE (stated)
at Step 2C -- do not paraphrase, do not summarize, copy it verbatim word-for-word]."

Scan Phase 3 cards (Phase 3 section, Step 6). Exception sign-off for any P3, or:
"No Phase 3 P3 exceptions. Phase 3 lifecycle: no fallback.
Governing paraphrase clause: [copy the exact Phase 3 clause from INFERENCE RULE (stated)
at Step 2C -- do not paraphrase, do not summarize, copy it verbatim word-for-word]."

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

Restate count: "SWITCHING-FRICTION COUNT: [N]. N >= 3: YES/NO."
List each entry's `Migrating from:` value. Flag any non-verbatim.
Quote Entry 3 Trigger event field verbatim: "[quote]"
State: "Sub-section present: YES. All Migrating from: fields verbatim: YES / NO.
Third entry covers Phase 2 migration barrier (not day-one friction): YES / NO.
Entry 3 Trigger event names a post-commitment workflow action (not day-one): YES / NO.
Entry 3 Prohibited: sentinel present in template (field-adjacent): YES / NO."

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
occurred -- flag explicitly by row.

State final:
"All Step 5 values match Step 6.
Exception sign-offs complete for Phase 1, Phase 2, and Phase 3 scans.
SWITCHING-FRICTION COUNT >= 3 confirmed. Third entry covers Phase 2 barrier: YES.
Entry 3 Trigger event quoted and confirmed: post-commitment action named.
Entry 3 Prohibited: sentinel in template (field-adjacent): confirmed.
Post-generation phase distribution table complete. All rows: MATCH.
Role allocation compliance (Step 3A vs Step 5): all roles MATCH.
Phase column in coverage table: all three phases represented -- confirmed.
Sub-checks 1, 2, and 3 verified. All C-01 through C-52 constraints met.
C-53 probe (role allocation pre-commitment table): complete.
C-54 probe (Phase column in coverage table): complete."
```

---

## V-05: Full Synthesis — All Three Axes (Role Allocation + Phase Column + Phase 2 Template)

**Axis:** V-01 (Role Allocation Pre-Commitment Table) + V-02 (Phase Column in Coverage Table) + V-03 (Phase 2 Body Template Sentence). Targets 310/310 on v17 plus potential above-ceiling credit on C-53, C-54, and C-55 candidates.

**Hypothesis:** All three axes are structurally independent and additive. C-53 targets role distribution before body generation (Step 3A gate). C-54 targets coverage table phase visibility after body generation (Pass 1 column). C-55 targets Phase 2 body framing during body generation (Step 2B template + Step 6 instruction). No axis occupies the same structural location as another. V-05 tests whether all three probes coexist without structural interference and whether their combined presence produces an output with fully independent per-role, per-phase, and per-template-sentence auditable compliance.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- PHASE DISTRIBUTION TARGET (declared before STATUS QUO analysis)

Before establishing the STATUS QUO baseline, declare the target ticket distribution.

PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30): [N] tickets
  Phase 2 (Day 31-60): [N] tickets
  Phase 3 (Day 61-90): [N] tickets
  Total: [N] tickets

Constraint: Phase 1 count >= 2. Phase 3 count >= 1. All three phases represented.
This target will be referenced at Step 5 (committed block) and re-verified at Step 5B
and Pass 2 Part C Sub-check 3.

---

## STEP 1B -- INERTIA: STATUS QUO

**1b-i. Current-state baseline**
Describe in 2-3 sentences: what are users doing today? Frame with awareness of
the Phase Distribution Target -- the baseline must generate friction across all three
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
| Phase 1 | Day 0-30 | P2/P3 | high |
| Phase 2 | Day 31-60 | P1/P2 | medium |
| Phase 3 | Day 61-90 | P0/P1 | medium/low |

---

## STEP 2B -- PHASE BODY TEMPLATE TABLE

| Phase | Adoption stance | Template sentence |
|-------|----------------|-------------------|
| Phase 1 | Dual-tool tension | "I still have [INERTIA COMPETITOR] open in another tab -- I keep switching back to check how it handled [specific scenario]." |
| Phase 2 | Partial migration | "I've migrated [specific workflow] to this tool but I'm still running [specific workflow] in [INERTIA COMPETITOR] -- and today I hit a wall when [specific blocking event]." |
| Phase 3 | Parity gap | "In [INERTIA COMPETITOR] I could [specific action] without leaving this screen; here I cannot." |

All three phases: open with the template sentence, all placeholders filled concretely.
Every placeholder must name a specific workflow, scenario, or event -- no generic fills.
Every [INERTIA COMPETITOR] placeholder: use the exact product name from Step 1b-ii.

---

## STEP 2C -- PHASE-SEVERITY INFERENCE RULE

Phase 1 (Day 0-30): P2/P3 non-outage. Fallback available; user is learning.
Phase 3 (Day 61-90): P1/P0 blocking. No fallback; user committed and blocked.

Violation conditions:
- Phase 1 P0/P1 non-outage: violation -- correct to P2/P3.
- Phase 3 P3 blocking: violation -- correct to P1/P0.

INFERENCE RULE (stated): [your paraphrase of the directional rule above]
Applied in: Steps 5, 5B, and Pass 2 INFERENCE AUDIT

Do not proceed until filled with your own-words paraphrase.

---

## STEP 3 -- ROLE ALLOCATION + ACTIVATION (SRE-FIRST)

### Step 3A -- Role Allocation Pre-Commitment

Before activating any role, declare the ticket count each role will generate.

ROLE ALLOCATION TABLE:
| Role | Tickets allocated |
|------|------------------|
| SRE | [N] |
| Support | [N] |
| PM | [N] |
| UX | [N] |
| Customer personas (C-01 through C-12 combined) | [N] |
| Total | [N] |

Constraints:
- SRE >= 1. Support >= 1. Customer personas >= 2.
- Total must equal the Phase Distribution Target total from Step 1.

This table is re-verified at Step 5B Constraint 1B and Pass 2 Part B item 4.
Do not proceed to Step 3B until the table is complete.

### Step 3B -- Role Activation

Activate roles: SRE -> Support -> PM -> UX -> C-01 through C-12.

[SRE] -- First. Operational failure modes: configuration errors, deployment issues,
on-call escalation, infrastructure-level P0/P1 candidates. Identify Phase 2 escalation
patterns (transition-zone operational friction that surfaces after partial commitment).

[Support] -- Second. Triage-queue patterns, documentation gaps, error messages.

[PM] -- Third. Intent gaps, roadmap items, feature-request backlog.

[UX] -- Fourth. Discoverability failures, onboarding friction, how-to patterns.

[C-01 through C-12] -- One ticket hypothesis each. Frame each with phase awareness:
  "In which phase (1, 2, or 3) will this persona most likely encounter this issue?"

---

## STEP 4 -- PERFORMANCE MODE DECLARATION

**You ARE the persona named on each ticket card.**

Your previous primary workflow used [INERTIA COMPETITOR -- product name from Step 1b-ii].
Phase 1: old tool still open, can fall back -- lower stakes.
Phase 3: committed to new tool, no fallback -- higher stakes.

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

Required item 1 -- INFERENCE RULE (confirmed):
[restate in your own words]

Required item 2 -- Verbatim from 2C:
[copy exact first sentence from INFERENCE RULE (stated) at Step 2C -- word for word, do not paraphrase]

Required item 3 -- PHASE DISTRIBUTION committed block:
Reconcile with Phase Distribution Target from Step 1.
  Phase 1 (Day 0-30): [N] tickets (Step 1 target: [N])
  Phase 2 (Day 31-60): [N] tickets (Step 1 target: [N])
  Phase 3 (Day 61-90): [N] tickets (Step 1 target: [N])
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
State: "Phase 1: [n] committed, [n] actual -- MATCH/MISMATCH."
Also cross-check against Step 1 target: "Step 1 target vs Step 5 committed: [match/mismatch per phase]."

Constraint 1B: Role counts must match Step 3A ROLE ALLOCATION TABLE.
State per role: "SRE: [n] allocated, [n] in Step 5 Persona column -- MATCH/MISMATCH."
Repeat for Support, PM, UX, Customer personas, Total.
If any MISMATCH: correct Step 5 before proceeding.

1. Phase distribution -- >=2 Phase 1, >=1 Phase 3.
2. Category spread -- >=3 distinct categories.
3. Volume distribution -- all three levels.
4. Phase-character compliance -- severity/volume match Step 2.
5. Inference-rule compliance -- Phase 1/Phase 3 violation scan.

**If any fails, correct and re-run.**

---

## STEP 5C -- PRE-BODY STRUCTURAL VERIFICATION (PASS 2B)

Item 1 -- Category distribution check.
Item 2 -- Persona distribution check.
Item 3 -- Phase distribution compliance.

Item 4 -- SWITCHING-FRICTION COUNT CHECK:
SWITCHING-FRICTION COUNT: [N]
N must be >= 3. Do not proceed to Step 6 if N < 3.
Third entry must cover a Phase 2 migration barrier (surfaces after partial commitment,
not on day one).

---

## STEP 6 -- FULL CARD BODIES (PHASE-ORGANIZED)

Organize by phase window. Complete all Phase 1 cards, then Phase 2, then Phase 3.
Within each group, ascending Ticket ID order.

### Phase 1 Cards (Day 0-30)

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [match Step 5]
Persona: [match Step 5]
Volume: [match Step 5]
Severity: [match Step 5 -- P2 or P3]

Body:
[Open with Phase 1 template sentence from Step 2B, all placeholders filled with the inertia
competitor product name and a concrete scenario. Reference the STATUS QUO element that drives
this ticket's volume. No third-person. Every old-tool reference: product name from Step 1b-ii.]

---

### Phase 2 Cards (Day 31-60)

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [match Step 5]
Persona: [match Step 5]
Volume: [match Step 5]
Severity: [match Step 5 -- P1 or P2]

Body:
[Open with Phase 2 template sentence from Step 2B, all placeholders filled: name the specific
migrated workflow, the specific workflow still running in the competitor, and the specific
blocking event. Reference the STATUS QUO element from Step 1b-i. No third-person.
Product name for old tool: use verbatim product name from Step 1b-ii.]

---

### Phase 3 Cards (Day 61-90)

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [match Step 5]
Persona: [match Step 5]
Volume: [match Step 5]
Severity: [match Step 5 -- P0 or P1]

Body:
[Open with Phase 3 template sentence from Step 2B, all placeholders filled concretely.
Reference the STATUS QUO element that drives this ticket's severity -- the user committed
fully; the competitor is not accessible for this workflow. No third-person.
Product name for old tool: verbatim from Step 1b-ii.]

---

## STEP 7 -- CROSS-TICKET PATTERNS

Pattern name: [short name]
Tickets affected: [T-NN, ...]
Root cause: [one sentence]

Consequence -- Affected segment:
Prohibited: "users in general", "the team", any unnamed group.
[Named role or cohort tied specifically to this pattern]

Consequence -- Day-90 scenario:
Prohibited: "this will cause confusion", any non-pattern-specific event.
[One specific event that occurs if unaddressed by Day 90]

Consequence -- Adoption cost:
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
N must be >= 3. State this count before writing any entry.

Template for Entries 1 and 2:

Switching-friction gap: [short name]
Migrating from: [product name from Step 1b-ii -- verbatim, grep-checkable]
Expected behavior: [one sentence]
Actual behavior: [one sentence]
Migration impact: [one sentence]

[Entry 3 -- Phase 2 migration barrier -- use this extended template:]

Switching-friction gap: [short name]
Migrating from: [product name from Step 1b-ii -- verbatim, grep-checkable]
Trigger event: [name the specific workflow action or system state that first surfaces
  this barrier after partial commitment -- must name a concrete post-commitment event
  that day-one users do not reach on first contact]
Prohibited: a barrier that day-one users would encounter on first contact.
  Disallowed: any friction present before workflow migration has begun; any issue
  a new user who has never committed to this tool would also file.
Expected behavior: [one sentence -- the behavior the user expected based on their
  experience after partial commitment]
Actual behavior: [one sentence]
Migration impact: [one sentence]

Entry-specific guidance:
- Entry 1: Cover the primary day-one migration friction (Phase 1 ticket driver).
- Entry 2: Cover the second most prominent migration barrier.
- Entry 3: Use the extended template. The Trigger event field must name the specific
  post-commitment workflow action. The Prohibited: sentinel in the template applies
  to this entry.

### Pre-Launch Priority
Name the single gap to close first. Tie to specific Ticket IDs, severity, and volume.
State whether it reduces switching-friction for inertia-competitor migrants.

---

## STEP 9 -- DUAL-PASS VERIFICATION

### PASS 1 -- Coverage Trace Table

| Ticket ID | Phase | STATUS QUO element referenced | Gap traced to |
|-----------|-------|-------------------------------|---------------|

Populate one row per ticket, in Ticket ID order.

After completing:
1. Confirm: "No gap from the Gap Analysis -- including switching-friction gaps -- is absent."
2. Confirm: "Inertia competitor product name appears in at least two STATUS QUO element cells."
3. Confirm: "All three phases represented in Phase column -- Phase 1: [n] rows, Phase 2: [n] rows,
   Phase 3: [n] rows. Three-phase coverage: YES."

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 -- Properties Verify + Inference Audit

**PART A -- Frontmatter Verify**
Confirm Step 5 matches Step 6 for all fields.
State: "All Step 5 values match Step 6 card bodies."

**PART B -- Property Checks**

1. Tool-name fidelity.
   State: "[PRODUCT NAME] in Step 1b-ii: YES. Card bodies: [T-NN, T-NN min].
   Migrating from: field: YES."

2. Phase-differentiated templates.
   State: "Phase 1 template in: [T-NN, T-NN]. Phase 2 template in: [T-NN, T-NN].
   Phase 3 template in: [T-NN]."

3. Switching-friction 4-field format.
   State: "All four fields present in all entries: YES / NO."

4. Role allocation compliance.
   State: "Step 3A allocation vs Step 5 Persona column --
   SRE: [n] allocated / [n] actual -- MATCH/MISMATCH.
   Support: [n] / [n] -- MATCH/MISMATCH.
   PM: [n] / [n] -- MATCH/MISMATCH.
   UX: [n] / [n] -- MATCH/MISMATCH.
   Customer personas: [n] / [n] -- MATCH/MISMATCH.
   Total: [n] / [n] -- MATCH/MISMATCH."

**PART C -- Inference Audit**

**Sub-check 1: Phase-Architecture Severity Compliance**

Scan Phase 1 cards (Phase 1 section, Step 6). Exception sign-off for any P0/P1, or:
"No Phase 1 P0/P1 exceptions. Phase 1 lifecycle: fallback available.
Governing paraphrase clause: [copy the exact Phase 1 clause from INFERENCE RULE (stated)
at Step 2C -- do not paraphrase, do not summarize, copy it verbatim word-for-word]."

Scan Phase 2 cards (Phase 2 section, Step 6). Exception sign-off for any P0 escalation, or:
"No Phase 2 P0 escalation exceptions. Phase 2 lifecycle: transition (partial fallback).
Governing paraphrase clause: [copy the exact Phase 2 clause from INFERENCE RULE (stated)
at Step 2C -- do not paraphrase, do not summarize, copy it verbatim word-for-word]."

Scan Phase 3 cards (Phase 3 section, Step 6). Exception sign-off for any P3, or:
"No Phase 3 P3 exceptions. Phase 3 lifecycle: no fallback.
Governing paraphrase clause: [copy the exact Phase 3 clause from INFERENCE RULE (stated)
at Step 2C -- do not paraphrase, do not summarize, copy it verbatim word-for-word]."

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

Restate count: "SWITCHING-FRICTION COUNT: [N]. N >= 3: YES/NO."
List each entry's `Migrating from:` value. Flag any non-verbatim.
Quote Entry 3 Trigger event field verbatim: "[quote]"
State: "Sub-section present: YES. All Migrating from: fields verbatim: YES / NO.
Third entry covers Phase 2 migration barrier (not day-one friction): YES / NO.
Entry 3 Trigger event names a post-commitment workflow action (not day-one): YES / NO.
Entry 3 Prohibited: sentinel present in template (field-adjacent): YES / NO."

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
occurred -- flag explicitly by row.

State final:
"All Step 5 values match Step 6.
Exception sign-offs complete for Phase 1, Phase 2, and Phase 3 scans.
SWITCHING-FRICTION COUNT >= 3 confirmed. Third entry covers Phase 2 barrier: YES.
Entry 3 Trigger event quoted and confirmed: post-commitment action named.
Entry 3 Prohibited: sentinel in template (field-adjacent): confirmed.
Post-generation phase distribution table complete. All rows: MATCH.
Role allocation compliance (Step 3A vs Step 5): all roles MATCH.
Phase column in coverage table: all three phases represented -- confirmed.
Phase 2 template verified in: [T-NN, T-NN]. All three phase templates confirmed.
Sub-checks 1, 2, and 3 verified. All C-01 through C-52 constraints met.
C-53 probe (role allocation pre-commitment table): complete.
C-54 probe (Phase column in coverage table): complete.
C-55 probe (Phase 2 body template sentence): complete."
```
