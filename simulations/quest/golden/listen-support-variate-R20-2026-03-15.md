# listen-support Round 20 — Skill Body Prompt Variations

**Date:** 2026-03-15
**Rubric target:** v19 (335 pts ceiling — C-55, C-56, C-57 introduced)
**Base:** V-05 R19 (335/335 under v19 — all C-01 through C-57 at ceiling)

**Variation axes selected** (3 single-axis, then 2 combined):
1. **Role sequence** — Step 3A ROLE ALLOCATION TABLE converted to a ROLE-PHASE CROSS-MATRIX pre-committing per-phase-per-role ticket counts (V-01)
2. **Lifecycle emphasis** — Part B item 2 extended from Phase 2 verbatim quotes to all-phase verbatim quotes with phase-differentiated concreteness properties (V-02)
3. **Output format** — Part B item 2 Phase 2 concreteness property confirmations converted from prose YES/NO assertions to a structured 5-column table (V-03)
4. **V-01 + V-02 combined** (V-04)
5. **Full synthesis** — all three axes (V-05)

**R20 criterion hypothesis matrix:**

| Criterion candidate | V-01 | V-02 | V-03 | V-04 | V-05 |
|--------------------|------|------|------|------|------|
| C-01 through C-57 (all prior — 335 pt ceiling) | YES | YES | YES | YES | YES |
| C-58 candidate: Role-Phase Cross-Matrix at Step 3A | YES | -- | -- | YES | YES |
| C-59 candidate: All-Phase Template Verbatim Quotes in Part B item 2 | -- | YES | -- | YES | YES |
| C-60 candidate: Concreteness Property Table in Part B item 2 | -- | -- | YES | -- | YES |

---

## V-01: Single-Axis — Role Sequence (Role-Phase Cross-Matrix at Step 3A)

**Axis:** Role sequence — V-05 R19 Step 3A carries a ROLE ALLOCATION TABLE with two columns: Role / Tickets allocated (total per role only). V-01 R20 converts Step 3A to a ROLE-PHASE CROSS-MATRIX with columns Role / Phase 1 / Phase 2 / Phase 3 / Total, pre-committing per-phase ticket counts per role. Step 5B Constraint 1B extends to verify per-phase-per-role counts against the cross-matrix. Part B item 4 expands its table to confirm cross-matrix compliance per phase per role. All other mechanisms from V-05 R19 preserved exactly.

**Probe (C-58 candidate):** C-53 requires a ROLE ALLOCATION TABLE pre-declaring per-role total counts; C-55 requires Part B item 4 to be a 4-column table (Role / Allocated / Actual / Match) verifying those totals post-generation. Neither criterion constrains per-phase role distribution. A model satisfying C-55 can assign all SRE tickets to Phase 1 and zero to Phase 3 without any structural gate making the concentration visible before or after body generation. The ROLE-PHASE CROSS-MATRIX closes this gap: by pre-committing per-phase counts per role (e.g., "SRE: Phase 1=1, Phase 2=1, Phase 3=0, Total=2"), phase saturation per role becomes detectable at Constraint 1B before body generation and at Part B item 4 post-generation. The mechanism extends the three-gate role architecture (pre-declaration → pre-body audit → post-generation re-check) to the phase dimension, parallel to how C-45/C-48/C-50 extended phase counting across three temporal windows. C-55 passes when Part B item 4 is a 4-column table verifying role totals; C-58 passes only when Step 3A carries a full cross-matrix pre-committing per-phase-per-role counts, Constraint 1B verifies cross-matrix compliance per phase per role before body generation, and Part B item 4 extends its table to include per-phase columns.

**Hypothesis:** The ROLE ALLOCATION TABLE (C-53) + 4-column role audit table (C-55) verify per-role totals but leave the phase-concentration-per-role failure mode open. The cross-matrix probe tests whether adding the phase dimension to the role pre-commitment is independently extractable as a criterion.

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

### Step 3A -- Role-Phase Cross-Matrix Pre-Commitment

Before activating any role, declare the ticket count each role will generate PER PHASE.

ROLE-PHASE CROSS-MATRIX:
| Role | Phase 1 | Phase 2 | Phase 3 | Total |
|------|---------|---------|---------|-------|
| SRE | [N] | [N] | [N] | [N] |
| Support | [N] | [N] | [N] | [N] |
| PM | [N] | [N] | [N] | [N] |
| UX | [N] | [N] | [N] | [N] |
| Customer personas (C-01 through C-12 combined) | [N] | [N] | [N] | [N] |
| Total | [N] | [N] | [N] | [N] |

Constraints:
- SRE Total >= 1. Support Total >= 1. Customer personas Total >= 2.
- Total row must equal the Phase Distribution Target per phase from Step 1.
- Column totals must equal the Phase Distribution Target from Step 1.

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

Allowed: Category {how-to, bug, feature-request, config, integration},
Volume {high, medium, low}, Severity {P0, P1, P2, P3}.
**Lock vocabulary values here. Full card bodies follow in Step 6.**

---

## STEP 5B -- COLLECTIVE DISTRIBUTION AUDIT

Constraint 0: Phase counts must match Step 5 committed block.
State: "Phase 1: [n] committed, [n] actual -- MATCH/MISMATCH."
Also cross-check against Step 1 target: "Step 1 target vs Step 5 committed: [match/mismatch per phase]."

Constraint 1B: Role-phase counts must match Step 3A ROLE-PHASE CROSS-MATRIX.
For each role, verify per-phase count AND total:
  "SRE: Ph1 allocated [n]/actual [n] MATCH/MISMATCH. Ph2 [n]/[n] MATCH/MISMATCH.
   Ph3 [n]/[n] MATCH/MISMATCH. Total [n]/[n] MATCH/MISMATCH."
Repeat for Support, PM, UX, Customer personas, and column totals.
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
3. Phase coverage confirmation table:
   | Phase | Row count in coverage table | Represented |
   |-------|-----------------------------|-------------|
   | Phase 1 | [n] | YES/NO |
   | Phase 2 | [n] | YES/NO |
   | Phase 3 | [n] | YES/NO |
   Three-phase coverage: YES/NO.

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
   State: "Phase 1 template in: [T-NN, T-NN]. Phase 2 template in: [T-NN].
   Phase 3 template in: [T-NN]."

   For each Phase 2 ticket, quote the opening sentence of the card body verbatim:
   Ticket [T-NN] opening: "[verbatim quote]"
   Confirm:
   - Specific workflow migrated: YES/NO
   - Specific blocking event named: YES/NO
   - Competitor product name (from Step 1b-ii) present: YES/NO
   Repeat for all Phase 2 tickets.

3. Switching-friction 4-field format.
   State: "All four fields present in all entries: YES / NO."

4. Role-phase allocation compliance.
   Complete the cross-matrix verification table:
   | Role | Ph1 Alloc | Ph1 Actual | Ph2 Alloc | Ph2 Actual | Ph3 Alloc | Ph3 Actual | Total Match |
   |------|-----------|------------|-----------|------------|-----------|------------|-------------|
   | SRE | [n] | [n] | [n] | [n] | [n] | [n] | MATCH/MISMATCH |
   | Support | [n] | [n] | [n] | [n] | [n] | [n] | MATCH/MISMATCH |
   | PM | [n] | [n] | [n] | [n] | [n] | [n] | MATCH/MISMATCH |
   | UX | [n] | [n] | [n] | [n] | [n] | [n] | MATCH/MISMATCH |
   | Customer personas | [n] | [n] | [n] | [n] | [n] | [n] | MATCH/MISMATCH |
   | Total | [n] | [n] | [n] | [n] | [n] | [n] | MATCH/MISMATCH |

   If any cell shows MISMATCH: name the discrepancy and the correction needed.

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
List each entry's Migrating from: value. Flag any non-verbatim.
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

If any row shows MISMATCH: name the discrepancy, identify the Ticket ID that drifted,
and state the correction needed.

State final:
"All Step 5 values match Step 6.
Exception sign-offs complete for Phase 1, Phase 2, and Phase 3 scans.
SWITCHING-FRICTION COUNT >= 3 confirmed. Third entry covers Phase 2 barrier: YES.
Entry 3 Trigger event quoted and confirmed: post-commitment action named.
Entry 3 Prohibited: sentinel in template (field-adjacent): confirmed.
Post-generation phase distribution table: all rows MATCH.
Phase coverage confirmation table (Pass 1): all three phases represented -- confirmed.
Role-phase cross-matrix (Part B item 4): all cells MATCH.
Sub-checks 1, 2, and 3 verified. All C-01 through C-57 constraints met.
C-58 probe (role-phase cross-matrix at Step 3A): complete."
```

---

## V-02: Single-Axis — Lifecycle Emphasis (All-Phase Template Verbatim Quotes in Part B item 2)

**Axis:** Lifecycle emphasis — V-05 R19 Part B item 2 quotes the opening sentence of each Phase 2 ticket verbatim and confirms three concreteness properties (specific workflow, specific blocking event, competitor name). Phase 1 and Phase 3 template fills are declared by ticket ID only, with no verbatim quote and no concreteness verification. V-02 R20 extends Part B item 2 to require verbatim opening-sentence quotes for tickets in ALL three phases, with phase-differentiated concreteness properties (Phase 1: specific competitor scenario, dual-tool context present, first-person speaker; Phase 2: specific workflow migrated, specific blocking event, competitor name; Phase 3: specific parity gap named, competitor name, full-commitment context). All other mechanisms from V-05 R19 preserved exactly.

**Probe (C-59 candidate):** C-57 requires verbatim quotes for Phase 2 template openings and confirms three concreteness properties. Phase 1 tickets can open with a generic dual-tool sentence ("I still have [tool] open"); Phase 3 tickets can state a vague parity gap -- the template sentence structure is required but placeholder fills are not independently verified for concreteness in Part B. Extending verbatim quote + concreteness check to all three phases closes the selective-phase-verification failure mode: C-57 closes Phase 2 abstract fills; C-59 closes Phase 1 and Phase 3 abstract fills. The phase-differentiated concreteness properties ensure the check is not uniform across phases but calibrated to what each phase template is structurally supposed to produce.

**Hypothesis:** C-57 applies verbatim-quote verification to Phase 2 only because Phase 2 has the most structurally complex template (three distinct placeholder fills). Phase 1 and Phase 3 have simpler templates but are equally susceptible to generic fills. The all-phase verbatim quote extension tests whether phase-selective verification is independently extractable as a criterion gap.

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

Allowed: Category {how-to, bug, feature-request, config, integration},
Volume {high, medium, low}, Severity {P0, P1, P2, P3}.
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
3. Phase coverage confirmation table:
   | Phase | Row count in coverage table | Represented |
   |-------|-----------------------------|-------------|
   | Phase 1 | [n] | YES/NO |
   | Phase 2 | [n] | YES/NO |
   | Phase 3 | [n] | YES/NO |
   Three-phase coverage: YES/NO.

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 -- Properties Verify + Inference Audit

**PART A -- Frontmatter Verify**
Confirm Step 5 matches Step 6 for all fields.
State: "All Step 5 values match Step 6 card bodies."

**PART B -- Property Checks**

1. Tool-name fidelity.
   State: "[PRODUCT NAME] in Step 1b-ii: YES. Card bodies: [T-NN, T-NN min].
   Migrating from: field: YES."

2. Phase-differentiated templates -- ALL-PHASE VERBATIM VERIFICATION.

   For each Phase 1 ticket, quote the opening sentence of the card body verbatim:
   Ticket [T-NN] opening: "[verbatim quote]"
   Confirm Phase 1 concreteness properties:
   - Specific scenario named (not a generic situation): YES/NO
   - Inertia competitor product name (from Step 1b-ii) present: YES/NO
   - Dual-tool tension evident (old tool still open / falling back): YES/NO
   Repeat for all Phase 1 tickets.

   For each Phase 2 ticket, quote the opening sentence of the card body verbatim:
   Ticket [T-NN] opening: "[verbatim quote]"
   Confirm Phase 2 concreteness properties:
   - Specific workflow migrated named: YES/NO
   - Specific blocking event named: YES/NO
   - Competitor product name (from Step 1b-ii) present: YES/NO
   Repeat for all Phase 2 tickets.

   For each Phase 3 ticket, quote the opening sentence of the card body verbatim:
   Ticket [T-NN] opening: "[verbatim quote]"
   Confirm Phase 3 concreteness properties:
   - Specific capability the competitor has that this tool lacks (parity gap): YES/NO
   - Inertia competitor product name (from Step 1b-ii) present: YES/NO
   - Full-commitment context (no fallback available for this workflow): YES/NO
   Repeat for all Phase 3 tickets.

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
List each entry's Migrating from: value. Flag any non-verbatim.
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

If any row shows MISMATCH: name the discrepancy, identify the Ticket ID that drifted,
and state the correction needed.

State final:
"All Step 5 values match Step 6.
Exception sign-offs complete for Phase 1, Phase 2, and Phase 3 scans.
SWITCHING-FRICTION COUNT >= 3 confirmed. Third entry covers Phase 2 barrier: YES.
Entry 3 Trigger event quoted and confirmed: post-commitment action named.
Entry 3 Prohibited: sentinel in template (field-adjacent): confirmed.
Post-generation phase distribution table: all rows MATCH.
Phase coverage confirmation table (Pass 1): all three phases represented -- confirmed.
Role allocation table (Part B item 4): all rows MATCH.
All-phase verbatim quotes (Part B item 2): Phase 1 [n] tickets, Phase 2 [n] tickets,
  Phase 3 [n] tickets -- all concreteness properties confirmed.
Sub-checks 1, 2, and 3 verified. All C-01 through C-57 constraints met.
C-59 probe (all-phase template verbatim quotes in Part B item 2): complete."
```

---

## V-03: Single-Axis — Output Format (Concreteness Property Table in Part B item 2)

**Axis:** Output format — V-05 R19 Part B item 2 confirms Phase 2 concreteness properties as three prose YES/NO assertions per ticket ("Specific workflow migrated: YES/NO / Specific blocking event named: YES/NO / Competitor product name present: YES/NO"). V-03 R20 converts these per-ticket assertions to a structured table with one row per Phase 2 ticket and five columns (Ticket ID / Quoted opening sentence / Specific workflow / Blocking event / Competitor name), each property column a YES/NO cell. All other mechanisms from V-05 R19 preserved exactly.

**Probe (C-60 candidate):** C-57 requires verbatim quotes for Phase 2 template openings and confirmation of three concreteness properties. The confirmation is per-ticket prose: three YES/NO assertions after each quote. A prose confirmation can collapse two properties into one assertion ("specific workflow and blocking event both named: YES") while appearing to confirm both. A YES/NO assertion is interpretable from the ticket body, not independently checkable from a field value. A table with one row per Phase 2 ticket makes each property independently checkable per column: the scorer reads down the "Specific workflow" column and every NO is a cell value, detectable without parsing sentence structure. Property-collapse (two properties in one cell) is structurally impossible in a single-value-per-cell table. C-57 passes when verbatim quotes are present and three concreteness properties are confirmed in any format; C-60 passes only when the confirmation is a table with one row per Phase 2 ticket and one column per property, with YES/NO as cell values.

**Hypothesis:** C-57 closes Phase 2 abstract fills via verbatim quote + prose assertions. The prose confirmation format permits property-collapse in the same way prose phase-distribution comparisons permitted phase-collapse before C-50 converted Sub-check 3 to a table. The concreteness property table probe tests whether the table-format structural argument is independently extractable as a criterion for Part B item 2.

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

Allowed: Category {how-to, bug, feature-request, config, integration},
Volume {high, medium, low}, Severity {P0, P1, P2, P3}.
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
3. Phase coverage confirmation table:
   | Phase | Row count in coverage table | Represented |
   |-------|-----------------------------|-------------|
   | Phase 1 | [n] | YES/NO |
   | Phase 2 | [n] | YES/NO |
   | Phase 3 | [n] | YES/NO |
   Three-phase coverage: YES/NO.

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
   State: "Phase 1 template in: [T-NN, T-NN]. Phase 2 template in: [T-NN].
   Phase 3 template in: [T-NN]."

   For each Phase 2 ticket, quote the opening sentence of the card body verbatim, then
   complete the concreteness property table:

   | Ticket ID | Quoted opening sentence | Specific workflow named | Blocking event named | Competitor name present |
   |-----------|------------------------|------------------------|---------------------|------------------------|
   | T-NN | "[verbatim quote]" | YES/NO | YES/NO | YES/NO |

   One row per Phase 2 ticket. Each cell is an independent YES/NO -- no combined cells.
   A NO in any cell is a concreteness failure for that ticket on that property.

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
List each entry's Migrating from: value. Flag any non-verbatim.
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

If any row shows MISMATCH: name the discrepancy, identify the Ticket ID that drifted,
and state the correction needed.

State final:
"All Step 5 values match Step 6.
Exception sign-offs complete for Phase 1, Phase 2, and Phase 3 scans.
SWITCHING-FRICTION COUNT >= 3 confirmed. Third entry covers Phase 2 barrier: YES.
Entry 3 Trigger event quoted and confirmed: post-commitment action named.
Entry 3 Prohibited: sentinel in template (field-adjacent): confirmed.
Post-generation phase distribution table: all rows MATCH.
Phase coverage confirmation table (Pass 1): all three phases represented -- confirmed.
Role allocation table (Part B item 4): all rows MATCH.
Phase 2 concreteness property table (Part B item 2): [n] rows, all properties YES.
Sub-checks 1, 2, and 3 verified. All C-01 through C-57 constraints met.
C-60 probe (concreteness property table in Part B item 2): complete."
```

---

## V-04: Combined — V-01 + V-02 (Role-Phase Cross-Matrix + All-Phase Template Verbatim Quotes)

**Axes combined:** Role sequence (Role-Phase Cross-Matrix at Step 3A) + Lifecycle emphasis (all-phase verbatim quotes with phase-differentiated concreteness properties in Part B item 2).

**Hypothesis:** C-58 and C-59 are structurally independent: C-58 operates at Step 3A and Step 5B/Part B item 4 (role-phase pre-commitment dimension); C-59 operates at Part B item 2 (template fill verification dimension). No shared mechanism. V-04 tests whether both are simultaneously satisfiable without structural conflict.

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

### Step 3A -- Role-Phase Cross-Matrix Pre-Commitment

Before activating any role, declare the ticket count each role will generate PER PHASE.

ROLE-PHASE CROSS-MATRIX:
| Role | Phase 1 | Phase 2 | Phase 3 | Total |
|------|---------|---------|---------|-------|
| SRE | [N] | [N] | [N] | [N] |
| Support | [N] | [N] | [N] | [N] |
| PM | [N] | [N] | [N] | [N] |
| UX | [N] | [N] | [N] | [N] |
| Customer personas (C-01 through C-12 combined) | [N] | [N] | [N] | [N] |
| Total | [N] | [N] | [N] | [N] |

Constraints:
- SRE Total >= 1. Support Total >= 1. Customer personas Total >= 2.
- Total row must equal the Phase Distribution Target per phase from Step 1.
- Column totals must equal the Phase Distribution Target from Step 1.

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

Allowed: Category {how-to, bug, feature-request, config, integration},
Volume {high, medium, low}, Severity {P0, P1, P2, P3}.
**Lock vocabulary values here. Full card bodies follow in Step 6.**

---

## STEP 5B -- COLLECTIVE DISTRIBUTION AUDIT

Constraint 0: Phase counts must match Step 5 committed block.
State: "Phase 1: [n] committed, [n] actual -- MATCH/MISMATCH."
Also cross-check against Step 1 target: "Step 1 target vs Step 5 committed: [match/mismatch per phase]."

Constraint 1B: Role-phase counts must match Step 3A ROLE-PHASE CROSS-MATRIX.
For each role, verify per-phase count AND total:
  "SRE: Ph1 allocated [n]/actual [n] MATCH/MISMATCH. Ph2 [n]/[n] MATCH/MISMATCH.
   Ph3 [n]/[n] MATCH/MISMATCH. Total [n]/[n] MATCH/MISMATCH."
Repeat for Support, PM, UX, Customer personas, and column totals.
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
3. Phase coverage confirmation table:
   | Phase | Row count in coverage table | Represented |
   |-------|-----------------------------|-------------|
   | Phase 1 | [n] | YES/NO |
   | Phase 2 | [n] | YES/NO |
   | Phase 3 | [n] | YES/NO |
   Three-phase coverage: YES/NO.

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 -- Properties Verify + Inference Audit

**PART A -- Frontmatter Verify**
Confirm Step 5 matches Step 6 for all fields.
State: "All Step 5 values match Step 6 card bodies."

**PART B -- Property Checks**

1. Tool-name fidelity.
   State: "[PRODUCT NAME] in Step 1b-ii: YES. Card bodies: [T-NN, T-NN min].
   Migrating from: field: YES."

2. Phase-differentiated templates -- ALL-PHASE VERBATIM VERIFICATION.

   For each Phase 1 ticket, quote the opening sentence verbatim:
   Ticket [T-NN] opening: "[verbatim quote]"
   Confirm Phase 1 concreteness properties:
   - Specific scenario named (not a generic situation): YES/NO
   - Inertia competitor product name (from Step 1b-ii) present: YES/NO
   - Dual-tool tension evident (old tool still open / falling back): YES/NO
   Repeat for all Phase 1 tickets.

   For each Phase 2 ticket, quote the opening sentence verbatim:
   Ticket [T-NN] opening: "[verbatim quote]"
   Confirm Phase 2 concreteness properties:
   - Specific workflow migrated named: YES/NO
   - Specific blocking event named: YES/NO
   - Competitor product name (from Step 1b-ii) present: YES/NO
   Repeat for all Phase 2 tickets.

   For each Phase 3 ticket, quote the opening sentence verbatim:
   Ticket [T-NN] opening: "[verbatim quote]"
   Confirm Phase 3 concreteness properties:
   - Specific capability the competitor has that this tool lacks (parity gap): YES/NO
   - Inertia competitor product name (from Step 1b-ii) present: YES/NO
   - Full-commitment context (no fallback available for this workflow): YES/NO
   Repeat for all Phase 3 tickets.

3. Switching-friction 4-field format.
   State: "All four fields present in all entries: YES / NO."

4. Role-phase allocation compliance.
   Complete the cross-matrix verification table:
   | Role | Ph1 Alloc | Ph1 Actual | Ph2 Alloc | Ph2 Actual | Ph3 Alloc | Ph3 Actual | Total Match |
   |------|-----------|------------|-----------|------------|-----------|------------|-------------|
   | SRE | [n] | [n] | [n] | [n] | [n] | [n] | MATCH/MISMATCH |
   | Support | [n] | [n] | [n] | [n] | [n] | [n] | MATCH/MISMATCH |
   | PM | [n] | [n] | [n] | [n] | [n] | [n] | MATCH/MISMATCH |
   | UX | [n] | [n] | [n] | [n] | [n] | [n] | MATCH/MISMATCH |
   | Customer personas | [n] | [n] | [n] | [n] | [n] | [n] | MATCH/MISMATCH |
   | Total | [n] | [n] | [n] | [n] | [n] | [n] | MATCH/MISMATCH |

   If any cell shows MISMATCH: name the discrepancy and the correction needed.

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
List each entry's Migrating from: value. Flag any non-verbatim.
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

If any row shows MISMATCH: name the discrepancy, identify the Ticket ID that drifted,
and state the correction needed.

State final:
"All Step 5 values match Step 6.
Exception sign-offs complete for Phase 1, Phase 2, and Phase 3 scans.
SWITCHING-FRICTION COUNT >= 3 confirmed. Third entry covers Phase 2 barrier: YES.
Entry 3 Trigger event quoted and confirmed: post-commitment action named.
Entry 3 Prohibited: sentinel in template (field-adjacent): confirmed.
Post-generation phase distribution table: all rows MATCH.
Phase coverage confirmation table (Pass 1): all three phases represented -- confirmed.
Role-phase cross-matrix (Part B item 4): all cells MATCH.
All-phase verbatim quotes (Part B item 2): Phase 1 [n] tickets, Phase 2 [n] tickets,
  Phase 3 [n] tickets -- all concreteness properties confirmed.
Sub-checks 1, 2, and 3 verified. All C-01 through C-57 constraints met.
C-58 probe (role-phase cross-matrix at Step 3A): complete.
C-59 probe (all-phase template verbatim quotes in Part B item 2): complete."
```

---

## V-05: Full Synthesis — V-01 + V-02 + V-03

**Axes combined:** Role sequence (Role-Phase Cross-Matrix) + Lifecycle emphasis (all-phase verbatim quotes) + Output format (concreteness property table for Phase 2 in Part B item 2, within the all-phase verbatim structure).

**Hypothesis:** All three axes are structurally independent. C-58 operates at Step 3A / Constraint 1B / Part B item 4. C-59 operates at Part B item 2 (all-phase scope). C-60 operates at Part B item 2 (Phase 2 format within the all-phase structure). V-05 tests whether all three are simultaneously satisfiable and whether the Phase 2 table format (C-60) nests correctly inside the all-phase verification structure (C-59).

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

### Step 3A -- Role-Phase Cross-Matrix Pre-Commitment

Before activating any role, declare the ticket count each role will generate PER PHASE.

ROLE-PHASE CROSS-MATRIX:
| Role | Phase 1 | Phase 2 | Phase 3 | Total |
|------|---------|---------|---------|-------|
| SRE | [N] | [N] | [N] | [N] |
| Support | [N] | [N] | [N] | [N] |
| PM | [N] | [N] | [N] | [N] |
| UX | [N] | [N] | [N] | [N] |
| Customer personas (C-01 through C-12 combined) | [N] | [N] | [N] | [N] |
| Total | [N] | [N] | [N] | [N] |

Constraints:
- SRE Total >= 1. Support Total >= 1. Customer personas Total >= 2.
- Total row must equal the Phase Distribution Target per phase from Step 1.
- Column totals must equal the Phase Distribution Target from Step 1.

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

Allowed: Category {how-to, bug, feature-request, config, integration},
Volume {high, medium, low}, Severity {P0, P1, P2, P3}.
**Lock vocabulary values here. Full card bodies follow in Step 6.**

---

## STEP 5B -- COLLECTIVE DISTRIBUTION AUDIT

Constraint 0: Phase counts must match Step 5 committed block.
State: "Phase 1: [n] committed, [n] actual -- MATCH/MISMATCH."
Also cross-check against Step 1 target: "Step 1 target vs Step 5 committed: [match/mismatch per phase]."

Constraint 1B: Role-phase counts must match Step 3A ROLE-PHASE CROSS-MATRIX.
For each role, verify per-phase count AND total:
  "SRE: Ph1 allocated [n]/actual [n] MATCH/MISMATCH. Ph2 [n]/[n] MATCH/MISMATCH.
   Ph3 [n]/[n] MATCH/MISMATCH. Total [n]/[n] MATCH/MISMATCH."
Repeat for Support, PM, UX, Customer personas, and column totals.
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
3. Phase coverage confirmation table:
   | Phase | Row count in coverage table | Represented |
   |-------|-----------------------------|-------------|
   | Phase 1 | [n] | YES/NO |
   | Phase 2 | [n] | YES/NO |
   | Phase 3 | [n] | YES/NO |
   Three-phase coverage: YES/NO.

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 -- Properties Verify + Inference Audit

**PART A -- Frontmatter Verify**
Confirm Step 5 matches Step 6 for all fields.
State: "All Step 5 values match Step 6 card bodies."

**PART B -- Property Checks**

1. Tool-name fidelity.
   State: "[PRODUCT NAME] in Step 1b-ii: YES. Card bodies: [T-NN, T-NN min].
   Migrating from: field: YES."

2. Phase-differentiated templates -- ALL-PHASE VERBATIM VERIFICATION.

   For each Phase 1 ticket, quote the opening sentence verbatim:
   Ticket [T-NN] opening: "[verbatim quote]"
   Confirm Phase 1 concreteness properties:
   - Specific scenario named (not a generic situation): YES/NO
   - Inertia competitor product name (from Step 1b-ii) present: YES/NO
   - Dual-tool tension evident (old tool still open / falling back): YES/NO
   Repeat for all Phase 1 tickets.

   For each Phase 2 ticket, complete the concreteness property table:

   | Ticket ID | Quoted opening sentence | Specific workflow named | Blocking event named | Competitor name present |
   |-----------|------------------------|------------------------|---------------------|------------------------|
   | T-NN | "[verbatim quote]" | YES/NO | YES/NO | YES/NO |

   One row per Phase 2 ticket. Each cell is an independent YES/NO -- no combined cells.
   A NO in any cell is a concreteness failure for that ticket on that property.

   For each Phase 3 ticket, quote the opening sentence verbatim:
   Ticket [T-NN] opening: "[verbatim quote]"
   Confirm Phase 3 concreteness properties:
   - Specific capability the competitor has that this tool lacks (parity gap): YES/NO
   - Inertia competitor product name (from Step 1b-ii) present: YES/NO
   - Full-commitment context (no fallback available for this workflow): YES/NO
   Repeat for all Phase 3 tickets.

3. Switching-friction 4-field format.
   State: "All four fields present in all entries: YES / NO."

4. Role-phase allocation compliance.
   Complete the cross-matrix verification table:
   | Role | Ph1 Alloc | Ph1 Actual | Ph2 Alloc | Ph2 Actual | Ph3 Alloc | Ph3 Actual | Total Match |
   |------|-----------|------------|-----------|------------|-----------|------------|-------------|
   | SRE | [n] | [n] | [n] | [n] | [n] | [n] | MATCH/MISMATCH |
   | Support | [n] | [n] | [n] | [n] | [n] | [n] | MATCH/MISMATCH |
   | PM | [n] | [n] | [n] | [n] | [n] | [n] | MATCH/MISMATCH |
   | UX | [n] | [n] | [n] | [n] | [n] | [n] | MATCH/MISMATCH |
   | Customer personas | [n] | [n] | [n] | [n] | [n] | [n] | MATCH/MISMATCH |
   | Total | [n] | [n] | [n] | [n] | [n] | [n] | MATCH/MISMATCH |

   If any cell shows MISMATCH: name the discrepancy and the correction needed.

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
List each entry's Migrating from: value. Flag any non-verbatim.
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

If any row shows MISMATCH: name the discrepancy, identify the Ticket ID that drifted,
and state the correction needed.

State final:
"All Step 5 values match Step 6.
Exception sign-offs complete for Phase 1, Phase 2, and Phase 3 scans.
SWITCHING-FRICTION COUNT >= 3 confirmed. Third entry covers Phase 2 barrier: YES.
Entry 3 Trigger event quoted and confirmed: post-commitment action named.
Entry 3 Prohibited: sentinel in template (field-adjacent): confirmed.
Post-generation phase distribution table: all rows MATCH.
Phase coverage confirmation table (Pass 1): all three phases represented -- confirmed.
Role-phase cross-matrix (Part B item 4): all cells MATCH.
All-phase verbatim quotes (Part B item 2): Phase 1 [n] tickets confirmed, Phase 3 [n] tickets confirmed.
Phase 2 concreteness property table: [n] rows, all properties YES.
Sub-checks 1, 2, and 3 verified. All C-01 through C-57 constraints met.
C-58 probe (role-phase cross-matrix at Step 3A): complete.
C-59 probe (all-phase template verbatim quotes in Part B item 2): complete.
C-60 probe (concreteness property table in Part B item 2 for Phase 2): complete."
```
