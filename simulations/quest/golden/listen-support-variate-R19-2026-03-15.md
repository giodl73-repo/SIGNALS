# listen-support Round 19 — Skill Body Prompt Variations

**Date:** 2026-03-15
**Rubric target:** v18 (320 pts ceiling — C-53, C-54 introduced)
**Base:** V-05 R18 (320/320 under v18 — all C-01 through C-54 at ceiling; C-55 candidate also baked in)

**Variation axes selected** (3 single-axis, then 2 combined):
1. **Role sequence** — Part B item 4 role allocation re-check converted from prose per-role statements to a table with one row per role (Role / Allocated / Actual / Match) (V-01)
2. **Output format** — Pass 1 Confirmation 3 three-phase coverage converted from prose to a table (Phase / Row count / Represented) (V-02)
3. **Lifecycle emphasis** — Part B item 2 extended to require verbatim quote of the Phase 2 template opening sentence used in each Phase 2 card body, parallel to Sub-check 2 Trigger event quote requirement (V-03)
4. **V-01 + V-02 combined** — Role audit table + Phase column confirmation table (V-04)
5. **Full synthesis** — All three axes: role audit table + Phase column confirmation table + Phase 2 template verbatim quote (V-05)

**R19 criterion hypothesis matrix:**

| Criterion candidate | V-01 | V-02 | V-03 | V-04 | V-05 |
|--------------------|------|------|------|------|------|
| C-01 through C-54 (all prior -- 320 pt ceiling) | YES | YES | YES | YES | YES |
| C-55 candidate: Role Audit Table Format in Part B item 4 | YES | -- | -- | YES | YES |
| C-56 candidate: Phase Column Confirmation Table in Pass 1 | -- | YES | -- | YES | YES |
| C-57 candidate: Phase 2 Template Verbatim Quote in Part B item 2 | -- | -- | YES | -- | YES |

---

## V-01: Single-Axis -- Role Sequence (Role Audit Table Format in Part B item 4)

**Axis:** Role sequence -- V-05 R18 Part B item 4 post-generation role allocation re-check fires as prose per-role statements ("SRE: [n] allocated / [n] actual -- MATCH/MISMATCH. Support: [n] / [n]..."). V-01 R19 converts Part B item 4 to a table with one row per role and four columns (Role / Allocated (Step 3A) / Actual (Step 5 Persona column) / Match). All other mechanisms from V-05 R18 are preserved exactly.

**Probe (C-55 candidate):** V-05 R18 satisfies C-53 (Role Allocation Pre-Commitment Table) with a three-gate architecture: Step 3A pre-declaration table, Step 5B Constraint 1B pre-body prose audit, and Part B item 4 post-generation prose re-check. The failure mode the prose format leaves open: per-role prose statements can collapse multiple roles into one sentence or embed counts in a narrative. A MISMATCH in a prose Part B item 4 is a clause to extract from sentence structure; a scorer must parse sentence structure to identify which role drifted. C-50 established the same argument for Sub-check 3 phase distribution -- converting prose to a table makes compliance self-verifying by row count. A table row per role in Part B item 4 applies the same structural mechanism: MISMATCH is a cell value in the Match column, readable without sentence parsing. Row count is self-verifying: five rows for five role types (SRE, Support, PM, UX, Customer personas) means all roles are independently represented and none can be silently collapsed.

**Hypothesis:** The C-53 post-generation role audit in Part B item 4 uses prose per-role statements that allow role-collapse in the same way C-48's prose Sub-check 3 allowed phase-collapse before C-50 converted it to a table. The C-55 probe tests whether converting Part B item 4 to a table format is independently extractable as a criterion from the three-gate role architecture C-53 already requires.

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
[Open with Phase 2 template sentence, all placeholders filled concretely: specific workflow
migrated, specific workflow still in competitor, specific blocking event. Reference the
STATUS QUO element from Step 1b-i. No third-person. Product name for old tool.]

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
   State: "Phase 1 template in: [T-NN, T-NN]. Phase 2 template in: [T-NN]. Phase 3 template in: [T-NN]."

3. Switching-friction 4-field format.
   State: "All four fields present in all entries: YES / NO."

4. Role allocation compliance.
   Complete the table:

   | Role | Allocated (Step 3A) | Actual (Step 5 Persona column) | Match |
   |------|---------------------|-------------------------------|-------|
   | SRE | [n] | [n] | MATCH/MISMATCH |
   | Support | [n] | [n] | MATCH/MISMATCH |
   | PM | [n] | [n] | MATCH/MISMATCH |
   | UX | [n] | [n] | MATCH/MISMATCH |
   | Customer personas | [n] | [n] | MATCH/MISMATCH |
   | Total | [n] | [n] | MATCH/MISMATCH |

   If any row shows MISMATCH: name the discrepancy and identify the correction needed.

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
from its committed phase, and state the correction needed.

State final:
"All Step 5 values match Step 6.
Exception sign-offs complete for Phase 1, Phase 2, and Phase 3 scans.
SWITCHING-FRICTION COUNT >= 3 confirmed. Third entry covers Phase 2 barrier: YES.
Entry 3 Trigger event quoted and confirmed: post-commitment action named.
Entry 3 Prohibited: sentinel in template (field-adjacent): confirmed.
Post-generation phase distribution table complete. All rows: MATCH.
Phase column in coverage table: all three phases represented -- confirmed.
Role allocation table (Part B item 4): all rows MATCH.
Sub-checks 1, 2, and 3 verified. All C-01 through C-54 constraints met.
C-55 probe (role audit table format in Part B item 4): complete."
```

---

## V-02: Single-Axis -- Output Format (Phase Column Confirmation Table in Pass 1)

**Axis:** Output format -- Pass 1 Confirmation 3. V-05 R18 Confirmation 3 uses prose: "All three phases represented in Phase column -- Phase 1: [n] rows, Phase 2: [n] rows, Phase 3: [n] rows. Three-phase coverage: YES." V-02 R19 converts Confirmation 3 to a table with one row per phase and three columns (Phase / Row count in coverage table / Represented), followed by an explicit "Three-phase coverage: YES/NO" statement. All other mechanisms from V-05 R18 are preserved exactly.

**Probe (C-56 candidate):** V-05 R18 satisfies C-54 (Phase Column in Coverage Table) by adding Phase as column 2 and providing a prose post-table confirmation that counts per-phase rows and states three-phase coverage. The failure mode the prose confirmation leaves open: the per-phase counts can be collapsed into a single sentence ("Phase 1 and Phase 2: 4 and 2 rows; Phase 3: 2 rows. Three-phase coverage: YES") where two phases share a clause. A scorer must parse sentence structure to extract the count for each phase independently. A table with one row per phase makes phase-collapse structurally impossible: each phase occupies its own row, and row count is self-verifying at three rows for three phases. The mechanism is identical to C-50 (which converted Sub-check 3 from prose to table): phase-collapse in prose becomes structurally impossible in table form.

**Hypothesis:** C-54 converts phase-concentration detection in the coverage trace table to a column scan. The post-table prose confirmation can still collapse phases; a confirmation table closes the same sentence-collapse failure mode that C-50 closed for Sub-check 3. The C-56 probe tests whether converting Confirmation 3 to a table format is independently extractable as a criterion from the Phase column addition C-54 already requires.

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
[Open with Phase 2 template sentence, all placeholders filled concretely: specific workflow
migrated, specific workflow still in competitor, specific blocking event. Reference the
STATUS QUO element from Step 1b-i. No third-person. Product name for old tool.]

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
3. Phase column coverage confirmation -- complete the table:

   | Phase | Row count in coverage table | Represented |
   |-------|-----------------------------|-------------|
   | Phase 1 | [n] | YES/NO |
   | Phase 2 | [n] | YES/NO |
   | Phase 3 | [n] | YES/NO |

   State: "Three-phase coverage: YES/NO."

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
   State: "Phase 1 template in: [T-NN, T-NN]. Phase 2 template in: [T-NN]. Phase 3 template in: [T-NN]."

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
from its committed phase, and state the correction needed.

State final:
"All Step 5 values match Step 6.
Exception sign-offs complete for Phase 1, Phase 2, and Phase 3 scans.
SWITCHING-FRICTION COUNT >= 3 confirmed. Third entry covers Phase 2 barrier: YES.
Entry 3 Trigger event quoted and confirmed: post-commitment action named.
Entry 3 Prohibited: sentinel in template (field-adjacent): confirmed.
Post-generation phase distribution table complete. All rows: MATCH.
Phase column coverage confirmation table complete. All three phases represented: YES.
Role allocation compliance: all roles MATCH.
Sub-checks 1, 2, and 3 verified. All C-01 through C-54 constraints met.
C-56 probe (Phase column confirmation table in Pass 1): complete."
```

---

## V-03: Single-Axis -- Lifecycle Emphasis (Phase 2 Template Verbatim Quote in Part B item 2)

**Axis:** Lifecycle emphasis -- how Phase 2 template compliance is verified in Part B item 2. V-05 R18 Part B item 2 states "Phase 1 template in: [T-NN, T-NN]. Phase 2 template in: [T-NN]. Phase 3 template in: [T-NN]." -- a declarative list of Ticket IDs. V-03 R19 extends Part B item 2 to additionally require a verbatim quote of the Phase 2 template opening sentence as it appears in each Phase 2 card body. All other mechanisms from V-05 R18 are preserved exactly.

**Probe (C-57 candidate):** V-05 R18 Part B item 2 confirms Phase 2 template usage by stating which Ticket IDs opened with the Phase 2 template. The failure mode the declarative confirmation leaves open: a declarative "Phase 2 template in: T-04" is a self-report. A scorer must navigate to T-04's card body and read the opening sentence to confirm the template was used correctly -- that placeholders were filled concretely, that the exact product name appears, and that the blocking event is specific rather than generic. The confirmation carries no independent evidence. Sub-check 2 established the same argument for the Entry 3 Trigger event field: quoting the field value verbatim converts a declarative YES/NO into an evidence-backed property -- a scorer can evaluate the quote without reading the full card body. Applying the same mechanism to Part B item 2 Phase 2 template verification: requiring a verbatim quote of the Phase 2 body opening sentence for each Phase 2 ticket makes template compliance independently falsifiable. A scorer reads the quoted sentence and confirms the placeholder fills are concrete (specific workflow named, specific blocking event named, inertia competitor product name present) without cross-referencing the card body.

**Hypothesis:** Part B item 2 Phase 2 verification is structurally parallel to Sub-check 2 Trigger event verification: both confirm a required field in a specific structural context, both currently use declarative self-reports, and both could be converted to evidence-backed confirmations by quoting the relevant field value. The C-57 probe tests whether requiring a verbatim quote of the Phase 2 body opening sentence in Part B item 2 is independently extractable as a criterion from the Phase 2 template mechanism V-03 R18 already requires.

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
[Open with Phase 2 template sentence, all placeholders filled concretely: specific workflow
migrated, specific workflow still in competitor, specific blocking event. Reference the
STATUS QUO element from Step 1b-i. No third-person. Product name for old tool.]

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
   For Phase 2 -- quote the opening sentence of each Phase 2 card body verbatim:
   "Phase 2 template in: [T-NN]. Opening sentence quoted: '[exact opening sentence from
   T-NN body as written]'. Placeholders filled concretely (specific workflow named,
   specific blocking event named, inertia competitor product name present): YES / NO."
   Repeat for each Phase 2 Ticket ID.
   A declarative "Phase 2 template used" without quoting the opening sentence does not pass.

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
from its committed phase, and state the correction needed.

State final:
"All Step 5 values match Step 6.
Exception sign-offs complete for Phase 1, Phase 2, and Phase 3 scans.
SWITCHING-FRICTION COUNT >= 3 confirmed. Third entry covers Phase 2 barrier: YES.
Entry 3 Trigger event quoted and confirmed: post-commitment action named.
Entry 3 Prohibited: sentinel in template (field-adjacent): confirmed.
Post-generation phase distribution table complete. All rows: MATCH.
Phase column in coverage table: all three phases represented -- confirmed.
Phase 2 template verbatim quote(s) in Part B item 2: all Phase 2 tickets quoted.
Placeholder concreteness confirmed: YES.
Role allocation compliance: all roles MATCH.
Sub-checks 1, 2, and 3 verified. All C-01 through C-54 constraints met.
C-57 probe (Phase 2 template verbatim quote in Part B item 2): complete."
```

---

## V-04: Combined -- V-01 + V-02 (Role Audit Table + Phase Column Confirmation Table)

**Axes combined:** Role sequence (Part B item 4 table format) + Output format (Pass 1 Confirmation 3 table format). V-04 R19 applies both table-format conversions simultaneously. All other mechanisms from V-05 R18 are preserved exactly.

**Probe:** V-04 tests whether C-55 and C-56 are compatible and mutually reinforcing -- both apply the same structural mechanism (table row per unit makes collapse impossible) to different dimensional audits (role distribution and phase distribution in the coverage trace).

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
[Open with Phase 2 template sentence, all placeholders filled concretely: specific workflow
migrated, specific workflow still in competitor, specific blocking event. Reference the
STATUS QUO element from Step 1b-i. No third-person. Product name for old tool.]

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
3. Phase column coverage confirmation -- complete the table:

   | Phase | Row count in coverage table | Represented |
   |-------|-----------------------------|-------------|
   | Phase 1 | [n] | YES/NO |
   | Phase 2 | [n] | YES/NO |
   | Phase 3 | [n] | YES/NO |

   State: "Three-phase coverage: YES/NO."

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
   State: "Phase 1 template in: [T-NN, T-NN]. Phase 2 template in: [T-NN]. Phase 3 template in: [T-NN]."

3. Switching-friction 4-field format.
   State: "All four fields present in all entries: YES / NO."

4. Role allocation compliance.
   Complete the table:

   | Role | Allocated (Step 3A) | Actual (Step 5 Persona column) | Match |
   |------|---------------------|-------------------------------|-------|
   | SRE | [n] | [n] | MATCH/MISMATCH |
   | Support | [n] | [n] | MATCH/MISMATCH |
   | PM | [n] | [n] | MATCH/MISMATCH |
   | UX | [n] | [n] | MATCH/MISMATCH |
   | Customer personas | [n] | [n] | MATCH/MISMATCH |
   | Total | [n] | [n] | MATCH/MISMATCH |

   If any row shows MISMATCH: name the discrepancy and identify the correction needed.

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
from its committed phase, and state the correction needed.

State final:
"All Step 5 values match Step 6.
Exception sign-offs complete for Phase 1, Phase 2, and Phase 3 scans.
SWITCHING-FRICTION COUNT >= 3 confirmed. Third entry covers Phase 2 barrier: YES.
Entry 3 Trigger event quoted and confirmed: post-commitment action named.
Entry 3 Prohibited: sentinel in template (field-adjacent): confirmed.
Post-generation phase distribution table complete. All rows: MATCH.
Phase column coverage confirmation table complete. All three phases represented: YES.
Role allocation table (Part B item 4): all rows MATCH.
Sub-checks 1, 2, and 3 verified. All C-01 through C-54 constraints met.
C-55 probe (role audit table format in Part B item 4): complete.
C-56 probe (Phase column confirmation table in Pass 1): complete."
```

---

## V-05: Full Synthesis -- V-01 + V-02 + V-03

**Axes combined:** All three -- role audit table (Part B item 4) + Phase column confirmation table (Pass 1 Confirmation 3) + Phase 2 template verbatim quote (Part B item 2). V-05 R19 is the full synthesis ceiling achiever for all C-01 through C-54 plus the three new probe candidates.

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
[Open with Phase 2 template sentence, all placeholders filled concretely: specific workflow
migrated, specific workflow still in competitor, specific blocking event. Reference the
STATUS QUO element from Step 1b-i. No third-person. Product name for old tool.]

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
3. Phase column coverage confirmation -- complete the table:

   | Phase | Row count in coverage table | Represented |
   |-------|-----------------------------|-------------|
   | Phase 1 | [n] | YES/NO |
   | Phase 2 | [n] | YES/NO |
   | Phase 3 | [n] | YES/NO |

   State: "Three-phase coverage: YES/NO."

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
   For Phase 2 -- quote the opening sentence of each Phase 2 card body verbatim:
   "Phase 2 template in: [T-NN]. Opening sentence quoted: '[exact opening sentence from
   T-NN body as written]'. Placeholders filled concretely (specific workflow named,
   specific blocking event named, inertia competitor product name present): YES / NO."
   Repeat for each Phase 2 Ticket ID.
   A declarative "Phase 2 template used" without quoting the opening sentence does not pass.

3. Switching-friction 4-field format.
   State: "All four fields present in all entries: YES / NO."

4. Role allocation compliance.
   Complete the table:

   | Role | Allocated (Step 3A) | Actual (Step 5 Persona column) | Match |
   |------|---------------------|-------------------------------|-------|
   | SRE | [n] | [n] | MATCH/MISMATCH |
   | Support | [n] | [n] | MATCH/MISMATCH |
   | PM | [n] | [n] | MATCH/MISMATCH |
   | UX | [n] | [n] | MATCH/MISMATCH |
   | Customer personas | [n] | [n] | MATCH/MISMATCH |
   | Total | [n] | [n] | MATCH/MISMATCH |

   If any row shows MISMATCH: name the discrepancy and identify the correction needed.

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
from its committed phase, and state the correction needed.

State final:
"All Step 5 values match Step 6.
Exception sign-offs complete for Phase 1, Phase 2, and Phase 3 scans.
SWITCHING-FRICTION COUNT >= 3 confirmed. Third entry covers Phase 2 barrier: YES.
Entry 3 Trigger event quoted and confirmed: post-commitment action named.
Entry 3 Prohibited: sentinel in template (field-adjacent): confirmed.
Post-generation phase distribution table complete. All rows: MATCH.
Phase column coverage confirmation table complete. All three phases represented: YES.
Phase 2 template verbatim quote(s) in Part B item 2: all Phase 2 tickets quoted.
Placeholder concreteness confirmed: YES.
Role allocation table (Part B item 4): all rows MATCH.
Sub-checks 1, 2, and 3 verified. All C-01 through C-54 constraints met.
C-55 probe (role audit table format in Part B item 4): complete.
C-56 probe (Phase column confirmation table in Pass 1): complete.
C-57 probe (Phase 2 template verbatim quote in Part B item 2): complete."
```
