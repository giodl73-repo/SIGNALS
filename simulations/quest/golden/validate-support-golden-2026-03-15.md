---
skill: quest-golden
skill_target: listen-support
date: 2026-03-14
rounds: 20
rubric_final: listen-support-rubric-v20-2026-03-14.md
score: 350
status: GOLDEN
---

# listen-support — Golden Prompt (R20 V-05, Simplified)

**Winning variation:** V-05 (full synthesis: C-58 + C-59 + C-60)
**Simplification:** PASS — 2,851 words (6.4% reduction from 3,046)
**Score:** 350/350 — ceiling on all 60 criteria

---

## Prompt Body

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
ticket's volume.]

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
STATUS QUO element from Step 1b-i.]

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
competitor is not accessible for this workflow.]

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
All three governing paraphrase clauses verbatim: YES.
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
Sub-checks 1, 2, and 3 verified. All C-01 through C-60 constraints met."
```

---

## What Made It Golden

**1. Role-Phase Cross-Matrix replaces the flat role table (C-58)**
V-01 through V-04 pre-committed per-role totals at Step 3A but left phase distribution within each role unconstrained — a model could assign all Support tickets to Phase 1 without any gate firing. V-05 expands Step 3A to a 5-column ROLE-PHASE CROSS-MATRIX (Role / Ph1 / Ph2 / Ph3 / Total). Constraint 1B in Step 5B fires on per-phase-per-role counts, not just totals. Part B item 4 in Pass 2 extends to a 7-column cross-matrix verification table. Role-phase concentration is detected before body generation and re-checked after.

**2. All-phase verbatim quotes close the Phase 1 / Phase 3 evidence gap (C-59)**
C-57 required verbatim quotes only for Phase 2 tickets. Phase 1 and Phase 3 template fills were verified by ticket ID listing — a scorer had to navigate to each card body to confirm concreteness. V-05 extends Part B item 2 to all three phases: verbatim quotes per ticket for every phase, each with independently named phase-differentiated concreteness properties. Phase 1 properties (scenario / competitor / dual-tool tension) and Phase 3 properties (parity gap / competitor / full-commitment) are confirmed in the verification output, not inferred from the card body.

**3. Phase 2 concreteness property table eliminates property-collapse (C-60)**
C-57's prose YES/NO format allowed "Specific workflow and blocking event both named: YES" — two properties in one sentence, one failure hidden. V-05 converts Phase 2 concreteness confirmations to a 5-column table (Ticket ID / Quoted opening sentence / Specific workflow named / Blocking event named / Competitor name present). Each property occupies its own column; a NO is a cell value, not a clause to parse. The Phase 2 table is nested inside the all-phase structure from C-59, with verbatim quote as column 2.

**4. Full synthesis — the only variation scoring all three R20 criteria simultaneously**
V-01 scored C-58 only. V-02 scored C-59 only. V-03 scored C-60 only. V-04 scored C-58 + C-59 but left Phase 2 properties in prose (no table). V-05 is the only variation that satisfies all three: the C-58 cross-matrix at Step 3A, the C-59 all-phase verbatim structure in Part B item 2, and the C-60 table nested inside that structure for Phase 2 tickets. No criterion was degraded to satisfy another.

**5. Prose-to-table pattern repeated across all new criteria**
Each R20 criterion follows the same structural argument used to create C-15, C-50, C-55, and C-56: prose YES/NO checks allow sentence-collapse; table rows with one item per cell do not. C-58 converts role allocation audit to a cross-matrix. C-59 converts phase-ID listing to per-ticket verbatim quotes. C-60 converts Phase 2 property sentences to a 5-column table. The pattern is not accidental — it is the mechanism that makes each new criterion load-bearing rather than decorative.

---

## Final Rubric Criteria Summary (v20 — 350 pts ceiling)

### Essential (60 pts — output fails below this line)

| ID | Name | Pts |
|----|------|-----|
| C-01 | All Five Ticket Fields Present | 12 |
| C-02 | Controlled Vocabulary Compliance | 12 |
| C-03 | Persona Grounding in Stock Roles | 12 |
| C-04 | Gap Analysis Present and Structured | 12 |
| C-05 | Minimum Ticket Count and Category Spread | 12 |

### Recommended (30 pts)

| ID | Name | Pts |
|----|------|-----|
| C-06 | Severity Calibration | 10 |
| C-07 | Volume Differentiated by Role and Phase | 10 |
| C-08 | Persona-Authentic Ticket Bodies | 10 |

### Aspirational (260 pts — 52 criteria at 5 pts each)

**Foundational structure (C-09 through C-22):** Cross-ticket patterns, prioritized gap signal, STATUS QUO grounding, pattern consequence decomposition, self-verification gate, table-form enumeration, container-free fields, gap-bridged coverage table, per-field Prohibited sentinels.

**Phase architecture (C-45 through C-50):** Phase distribution pre-declared before STATUS QUO analysis; phase committed block reconciled before vocabulary table; phase count table replaces prose comparison; post-generation phase re-verification table with Step 1 and Step 5 columns.

**Switching-friction (C-51 through C-52):** Dedicated sub-section; Phase 2 migration barrier with Trigger event field and Prohibited sentinel for Entry 3.

**Role architecture (C-53 through C-55):** Role allocation table pre-declares per-role counts at Step 3A; Constraint 1B fires before body generation; Part B item 4 re-checks post-generation in 4-column table format.

**Coverage and phase audit (C-54, C-56):** Phase column in coverage table (4-column); post-table phase confirmation in 3-row structured table.

**Verbatim enforcement (C-57 through C-60):**

| ID | Name | What it closes |
|----|------|----------------|
| C-57 | Phase 2 Verbatim Quotes | Declarative ticket-ID listing for Phase 2 |
| C-58 | Role-Phase Cross-Matrix at Step 3A | Per-role phase concentration before body generation |
| C-59 | All-Phase Template Verbatim Quotes | Phase 1 and Phase 3 concreteness unverifiable without navigating card bodies |
| C-60 | Concreteness Property Table Phase 2 | Property-collapse in Phase 2 prose YES/NO assertions |

**Score breakdown:**

| Tier | Criteria | Max pts |
|------|----------|---------|
| Essential | C-01 to C-05 | 60 |
| Recommended | C-06 to C-08 | 30 |
| Aspirational | C-09 to C-60 | 260 |
| **Total** | **60 criteria** | **350** |
