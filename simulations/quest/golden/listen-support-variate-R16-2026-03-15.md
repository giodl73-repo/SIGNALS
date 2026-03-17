# listen-support Round 16 — Skill Body Prompt Variations

**Date:** 2026-03-15
**Rubric target:** v15 (280 pts ceiling — C-44, C-45, C-46 introduced)
**Base:** V-05 R15 (280/280 under v15 — all C-01 through C-46 at ceiling)

**Variation axes selected** (3 single-axis, then 2 combined):
1. **Role sequence** — SRE activates before Support; Phase 2 no-exception confirmation added with triple-clause (V-01)
2. **Output format** — card bodies organized by phase window rather than ticket-ID sequence; Part C gains a post-generation PHASE DISTRIBUTION re-verification step (V-02)
3. **Lifecycle emphasis** — equal allocation pre-declared before STATUS QUO analysis; switching-friction minimum count raised from 2 to 3 (V-03)
4. **V-01 + V-02 combined** — SRE-first + phase-organized output + Phase 2 no-exception triple-clause + PHASE DISTRIBUTION re-verification (V-04)
5. **Full synthesis** — all three axes: SRE-first + phase-organized + Phase 2 no-exception + re-verification + switching-friction count ≥ 3 (V-05)

**R16 criterion hypothesis matrix:**

| Criterion candidate | V-01 | V-02 | V-03 | V-04 | V-05 |
|--------------------|------|------|------|------|------|
| C-01 through C-46 (all prior — 280 pt ceiling) | YES | YES | YES | YES | YES |
| C-47 candidate: Phase-2 No-Exception Triple-Clause | YES | — | — | YES | YES |
| C-48 candidate: Post-Generation Phase Distribution Re-Verify | — | YES | — | YES | YES |
| C-49 candidate: Switching-Friction Count Floor ≥ 3 | — | — | YES | — | YES |

---

## V-01: Single-Axis — Role Sequence (SRE-First) + Phase-2 No-Exception Triple-Clause

**Axis:** Role sequence — SRE activates before Support in role analysis. V-05 R15 runs analysis in Support → PM → UX → SRE → C-01..C-12 order. V-01 R16 reorders to SRE → Support → PM → UX → C-01..C-12. All other mechanisms from V-05 R15 are preserved exactly.

**Probe (C-47 candidate):** V-05 R15 upgrades the Phase 1 and Phase 3 no-exception confirmation paths to triple-clause verbatim (satisfying C-44). Phase 2 tickets sit between these two audit passes — when no Phase 2 anomalies exist, the model writes no confirmation statement for Phase 2. V-01 R16 adds a third no-exception confirmation path for Phase 2 tickets, requiring the same triple-clause form as Phase 1 and Phase 3: "No Phase 2 P0/P1 escalation exceptions. Phase 2 lifecycle: transition (partial fallback). Governing paraphrase clause: [do not paraphrase, do not summarize, copy it verbatim word-for-word]." This closes the asymmetry C-44 leaves open: the triple-clause standard now applies to all three phase scan paths, not only Phase 1 and Phase 3.

**Hypothesis:** C-44 closes the condensation path on the Phase 1 and Phase 3 no-exception confirmations but leaves Phase 2 on an unspecified verbatim standard. Because Phase 2 is the transition zone — tickets may escalate upward toward P0/P1 or stay in P1/P2 — the Phase 2 confirmation is exercised differently than Phases 1 or 3. SRE-first role activation is hypothesized to generate more Phase 2 escalation patterns (operational concerns surface before user-experience friction), producing a non-trivial Phase 2 audit result. The C-47 probe tests whether the triple-clause standard on the Phase 2 no-exception path is independently extractable.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- INERTIA: STATUS QUO

Establish the current-state baseline and name the inertia competitor.

**1a. Current-state baseline**
Describe in 2-3 sentences: what are users doing today to accomplish the job
this feature addresses? Where is friction highest? What workarounds exist
and what do they cost?

**1b. Inertia competitor declaration**

INERTIA COMPETITOR: [product name]
Prohibited: "existing tooling", "their current system", "legacy workflow",
or any phrase that does not produce a grep-checkable product name string.

This product name will be embedded in the performance mode declaration in Step 3,
appear verbatim in every Phase 1 and Phase 3 ticket body, and appear verbatim in
the `Migrating from:` field of every switching-friction gap. Record it once here.

**1c. Adoption-curve context**
Note where the user population sits: early (dual-tool phase), mid-transition, or late
(parity-gap phase). This drives phase distribution in Step 4.

---

## STEP 2 -- PHASE MAP TABLE

| Phase | Window | Expected severity range | Expected volume character |
|-------|--------|------------------------|--------------------------|
| Phase 1 | Day 0–30 | P2/P3 | high |
| Phase 2 | Day 31–60 | P1/P2 | medium |
| Phase 3 | Day 61–90 | P0/P1 | medium/low |

---

## STEP 2B -- PHASE BODY TEMPLATE TABLE

Replace [INERTIA COMPETITOR] with the product name from Step 1b before writing this table.

| Phase | Adoption stance | Pre-printed template sentence |
|-------|----------------|-------------------------------|
| Phase 1 | Dual-tool tension | "I still have [INERTIA COMPETITOR] open in another tab while working through this — I keep switching back to check how it handled [specific scenario]." |
| Phase 3 | Parity gap | "In [INERTIA COMPETITOR] I could [specific action] without leaving this screen; here I cannot find a way to do it at all." |

Instructions:
- Phase 1 bodies: include the Phase 1 sentence with all placeholders filled concretely.
- Phase 3 bodies: include the Phase 3 sentence with all placeholders filled concretely.
- Phase 2 bodies: reference the competitor where it naturally fits; no template required.

---

## STEP 2C -- PHASE-SEVERITY INFERENCE RULE

Do not proceed to Step 3 until this step is complete.

**The directional rule:**

Phase 1 tickets (Day 0–30) MUST be P2 or P3 for non-outage issues.
- Reason: The inertia competitor is still available. Adoption friction is expected.
  A workaround exists — return to the competitor and complete the task there.
  Lower severity reflects that the user is not blocked; they are learning.

Phase 3 tickets (Day 61–90) that block task completion MUST be P1 or P0.
- Reason: Phase 3 users have committed to the new product. The inertia competitor
  is no longer in their daily workflow. Parity gaps that prevent task completion
  have no fallback path. Higher severity reflects that the user is blocked with
  no alternative.

**Violation conditions (apply in Steps 4, 4B, and Pass 2 INFERENCE AUDIT):**
- Phase 1 P0 or P1 on a non-outage ticket: violation — correct to P2/P3.
- Phase 3 P3 on a ticket where the user cannot complete a task: violation — correct to P1/P0.

**Required confirmation before proceeding:**
State the inference rule in your own words as a named constraint. This paraphrase will
be recalled at Step 4 and verified in Pass 2 Part C. Write a genuine restatement —
not a copy of the rule above:

INFERENCE RULE (stated): [your paraphrase of the directional rule above]
Applied in: Steps 4, 4B, and Pass 2 INFERENCE AUDIT

Do not proceed to Step 3 until this block is filled with your own-words paraphrase.

---

## STEP 3 -- ROLE ACTIVATION ORDER

Activate roles in the following order. Each role contributes ticket hypotheses before
the next role activates. Role order affects which concerns dominate Phase 1 vs Phase 3.

Order: SRE → Support → PM → UX → C-01 through C-12

[SRE] — Activate first. Focus on operational failure modes: configuration errors,
deployment issues, on-call escalation scenarios, infrastructure-level P0/P1 candidates.

[Support] — Activate second. Focus on triage-queue patterns: first-call resolution
blockers, documentation gaps, error message clarity, category distribution.

[PM] — Activate third. Focus on intent gaps: what the feature promised vs what shipped,
roadmap items surfacing as Phase 3 tickets, feature-request backlog.

[UX] — Activate fourth. Focus on discoverability failures, onboarding friction, and
how-to ticket patterns driven by interface ambiguity.

[C-01 through C-12] — Activate in ID order, each contributing one ticket hypothesis
from their archetype.

---

## STEP 4 -- PERFORMANCE MODE DECLARATION

**You ARE the persona named on each ticket card.**

Your previous primary workflow used [INERTIA COMPETITOR — insert product name from Step 1b].
You recently started using this new product. You are in some stage of migration:
Phase 1 tickets are written when you still have the old tool open — lower stakes because
you can fall back. Phase 3 tickets are written when you have committed to the new tool
and cannot fall back — higher stakes because you are blocked.

Do not write "the user", "they", "the SRE", "the PM", "the engineer",
or any named-role title referring to yourself in third person.

Prohibited verb-subject forms: "the SRE ran", "the PM reviewed", "the engineer observed",
"the C-07 clicked", "the Support agent opened", or any construction where a role title
precedes a verb.

**Every action in this ticket was taken by "I". Every reference to the old tool
uses its product name, not a pronoun or generic description.**

---

## STEP 5 -- VOCABULARY PRE-COMMITMENT TABLE

Competitor in scope: [write the product name from Step 1b here — do not write "the tool",
"my old system", or any alias. This name must appear verbatim in every Phase 1 and Phase 3
ticket body in Step 6.]

Do not fill any cell in the table until all three items are written:

Required item 1 — INFERENCE RULE (confirmed):
[restate the directional rule from your Step 2C paraphrase in your own words]

Required item 2 — Verbatim from 2C:
[copy your exact first sentence from the INFERENCE RULE (stated) block in Step 2C —
word for word, do not paraphrase]

Required item 3 — PHASE DISTRIBUTION committed block:
  Phase 1 (Day 0–30): [N] tickets
  Phase 2 (Day 31–60): [N] tickets
  Phase 3 (Day 61–90): [N] tickets
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

Allowed values:
- Category: {how-to, bug, feature-request, config, integration}
- Volume: {high, medium, low}
- Severity: {P0, P1, P2, P3}

**Lock vocabulary values here. Full card bodies follow in Step 6.**

---

## STEP 5B -- COLLECTIVE DISTRIBUTION AUDIT

Audit five constraints before writing any card body:

Constraint 0: PHASE DISTRIBUTION count-match check — the Phase 1, Phase 2, and Phase 3
row counts in the table above must equal the Phase Distribution committed block in Step 5.
If they do not match, correct the table now. State: "Phase 1: [n] committed, [n] actual —
MATCH/MISMATCH. Phase 2: MATCH/MISMATCH. Phase 3: MATCH/MISMATCH."

1. **Phase distribution** — at least two Phase 1 rows and one Phase 3 row.
2. **Category spread** — at least three distinct category values.
3. **Volume distribution** — all three volume levels present.
4. **Phase-character compliance** — each row's volume and severity match Step 2 ranges.
5. **Inference-rule compliance** — apply the INFERENCE RULE confirmed above Step 5:
   - Scan Phase 1 rows: flag any P0 or P1 assignment on a non-outage ticket.
   - Scan Phase 3 rows: flag any P3 assignment on a blocking ticket.
   - State PASS if no violations; FAIL and name the row and correction if any found.

State PASS or FAIL per constraint.
**If any fails, correct the table and re-run. Name the correction.**

---

## STEP 5C -- PRE-BODY STRUCTURAL VERIFICATION (PASS 2B)

Before writing the first card body, verify four structural properties:

Item 1 — CATEGORY DISTRIBUTION CHECK:
Count tickets per category. If any single category exceeds 60% of total tickets, reconsider.
State: "[category]: [count] / [total] — PASS/WARN."

Item 2 — PERSONA DISTRIBUTION CHECK:
Confirm at least one ticket is attributed to a role activated in Step 3 (SRE, Support, PM,
UX, or C-01..C-12). State: "Role coverage: [list one ticket ID per role group]."

Item 3 — PHASE DISTRIBUTION COMPLIANCE:
Confirm the table row counts match the PHASE DISTRIBUTION committed block from Step 5.
State: "Phase 1: [n]. Phase 2: [n]. Phase 3: [n]. Total: [n]. Matches committed block: YES/NO."

Item 4 — SWITCHING-FRICTION COUNT CHECK:
SWITCHING-FRICTION COUNT: [N]
N must be ≥ 2. If you have fewer than 2 switching-friction gap entries prepared, add entries
before continuing. State: "SWITCHING-FRICTION COUNT: [N]. Minimum satisfied (N ≥ 2): YES/NO."
Do not proceed to Step 6 if N < 2.

---

## STEP 6 -- FULL CARD BODIES

For each row in the vocabulary table, in ticket-ID order:

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [must match Step 5 exactly]
Persona: [must match Step 5 exactly]
Volume: [must match Step 5 exactly]
Severity: [must match Step 5 exactly]

Body:
[You ARE this persona. You previously used [INERTIA COMPETITOR — product name].
- Phase 1 tickets: open with the Phase 1 template sentence from Step 2B,
  placeholders filled concretely. Severity is P2/P3 because the competitor
  is still available; you are learning, not blocked.
- Phase 3 tickets: open with the Phase 3 template sentence from Step 2B,
  placeholders filled concretely. Severity is P0/P1 because you have committed
  to this tool and cannot fall back to the competitor for this workflow.
- All tickets: reference the STATUS QUO element from Step 1 that drives
  this ticket's volume and severity.
- No third-person references to yourself. Use the product name every time
  you mention the old tool.]

---

## STEP 7 -- CROSS-TICKET PATTERNS

For each pattern, use this flat field structure with no parent "Consequence:" container:

Pattern name: [short name]
Tickets affected: [T-NN, T-NN, ...]
Root cause: [one sentence]

Consequence — Affected segment:
Prohibited: "users in general", "the team", or any unnamed group.
[Named role or cohort tied specifically to this pattern]

Consequence — Day-90 scenario:
Prohibited: "this will cause confusion" or any non-pattern-specific event.
[One specific event that occurs if this pattern is not addressed by Day 90]

Consequence — Adoption cost:
Prohibited: generic friction not specific to this cohort.
[One sentence quantifying the friction for the named segment]

If a pattern involves migration from the inertia competitor, name the competitor
in the root cause or consequence fields.

---

## STEP 8 -- GAP ANALYSIS

### Doc Gaps
[At least one documentation gap.]

### Design Gaps
[At least one design gap.]

### Operational Gaps
[At least one operational gap.]

### Switching-Friction Gaps

Dedicated sub-section for migration barriers only. NOT absorbed into the three sections
above. The three sections above remain present and non-empty.

SWITCHING-FRICTION COUNT: [N]
N must be ≥ 2. State this before writing any entry.

Use this exact format for every entry:

Switching-friction gap: [short name]
Migrating from: [product name from Step 1b — verbatim, grep-checkable]
Expected behavior: [one sentence — what users expected, based on competitor behavior]
Actual behavior: [one sentence — what this product actually does or fails to do]
Migration impact: [one sentence — what users must change, lose, or manually replicate]

Rules:
- `Migrating from:` MUST contain the product name from Step 1b verbatim.
  Prohibited: `Migrating from: existing tool`, `Migrating from: legacy workflow`.
- Every entry must be independently enumerable without reading other sections.

### Pre-Launch Priority
Name the single gap to close first. Tie to specific ticket IDs, severity, and volume.
State whether it reduces switching-friction for inertia-competitor migrants.

---

## STEP 9 -- DUAL-PASS VERIFICATION

### PASS 1 -- Coverage Trace Table

| Ticket ID | STATUS QUO element referenced | Gap traced to |
|-----------|-------------------------------|---------------|
| T-01 | | |
| T-02 | | |
| T-03 | | |
| T-04 | | |
| T-05 | | |
| T-06 | | |
| T-07 | | |
| T-08 | | |

After completing the table:
1. Confirm: "No gap from the Gap Analysis — including switching-friction gaps —
   is absent from this table."
2. Confirm: "The inertia competitor product name appears in at least two
   STATUS QUO element cells."

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 -- Properties Verify + Inference Audit

**PART A — Frontmatter Verify**

Confirm the summary table from Step 5 matches every Ticket ID, Phase, Category,
Persona, Volume, and Severity in the full card bodies from Step 6.
State: "All Step 5 values match Step 6 card bodies."

**PART B — Property Checks**

1. **Tool-name fidelity** — product name from Step 1b appears verbatim in Step 1b,
   at least two card bodies, and at least one `Migrating from:` field.
   State: "[PRODUCT NAME] in Step 1b: YES. Card bodies: T-NN, T-NN (minimum).
   Migrating from: field: YES."

2. **Phase-differentiated templates** — at least two Phase 1 bodies contain the
   Phase 1 template from Step 2B, and at least one Phase 3 body contains the Phase 3 template.
   State: "Phase 1 template in: T-NN, T-NN. Phase 3 template in: T-NN."

3. **Switching-friction 4-field format** — every entry in the Switching-Friction Gaps
   sub-section contains all four fields.
   State: "All four fields present in all entries: YES / NO. Missing: [field list or NONE]."

**PART C — Inference Audit**

**Sub-check 1: Phase-Architecture Severity Compliance**

Scan Phase 1 rows in the vocabulary table (Step 5):
- List every Phase 1 ticket assigned P0 or P1.
- For each, fill a Phase 1 EXCEPTION SIGN-OFF BLOCK:

EXCEPTION SIGN-OFF (Phase 1 — fallback available):
Ticket ID: [T-NN]
Phase: 1
Fallback status: Inertia competitor still in active use (fallback available)
Assigned severity: [P0 or P1]
Grounds: [outage-level? YES / NO — only an outage justifies P0/P1 when fallback exists]
Paraphrase clause: [copy the exact Phase 1 clause from your INFERENCE RULE (stated) at
  Step 2C verbatim — do not paraphrase, do not summarize, copy it word-for-word]
Disposition: [VALID EXCEPTION — reason | VIOLATION — corrected to P2/P3]

If no Phase 1 P0/P1 assignments exist, state:
"No Phase 1 P0/P1 exceptions. Phase 1 lifecycle: fallback available (inertia competitor
in active use). Governing paraphrase clause: [copy the exact Phase 1 clause from your
INFERENCE RULE (stated) at Step 2C — do not paraphrase, do not summarize, copy it
verbatim word-for-word]."

Scan Phase 2 rows in the vocabulary table (Step 5):
- List every Phase 2 ticket assigned P0 (escalation above expected Phase 2 range).
- For each, fill a Phase 2 EXCEPTION SIGN-OFF BLOCK:

EXCEPTION SIGN-OFF (Phase 2 — partial fallback):
Ticket ID: [T-NN]
Phase: 2
Fallback status: Partial — inertia competitor accessible but not primary workflow
Assigned severity: P0
Grounds: [outage-level? YES / NO — P0 in Phase 2 requires active service unavailability]
Paraphrase clause: [copy the exact Phase 2 clause from your INFERENCE RULE (stated) at
  Step 2C verbatim — do not paraphrase, do not summarize, copy it verbatim word-for-word]
Disposition: [VALID EXCEPTION — reason | VIOLATION — corrected to P1/P2]

If no Phase 2 P0 escalation exceptions exist, state:
"No Phase 2 P0 escalation exceptions. Phase 2 lifecycle: transition (partial fallback).
Governing paraphrase clause: [copy the exact Phase 2 clause from your INFERENCE RULE
(stated) at Step 2C — do not paraphrase, do not summarize, copy it verbatim word-for-word]."

Scan Phase 3 rows in the vocabulary table (Step 5):
- List every Phase 3 ticket assigned P3.
- For each, fill a Phase 3 EXCEPTION SIGN-OFF BLOCK:

EXCEPTION SIGN-OFF (Phase 3 — no fallback):
Ticket ID: [T-NN]
Phase: 3
Fallback status: Inertia competitor out of daily workflow (no fallback)
Assigned severity: P3
Grounds: [non-blocking issue? YES / NO — P3 only valid if user is not blocked]
Paraphrase clause: [copy the exact Phase 3 clause from your INFERENCE RULE (stated) at
  Step 2C verbatim — do not paraphrase, do not summarize, copy it word-for-word]
Disposition: [VALID EXCEPTION — reason | VIOLATION — corrected to P1/P0]

If no Phase 3 P3 assignments exist, state:
"No Phase 3 P3 exceptions. Phase 3 lifecycle: no fallback (inertia competitor out of
daily workflow). Governing paraphrase clause: [copy the exact Phase 3 clause from your
INFERENCE RULE (stated) at Step 2C — do not paraphrase, do not summarize, copy it
verbatim word-for-word]."

Confirm the INFERENCE RULE stated in Step 2C and confirmed at Step 5 has been
applied consistently. Compare the paraphrase from Step 2C against the audit results:
State: "INFERENCE RULE paraphrase (Step 2C): [quote first 10 words of your Step 2C paraphrase].
Verbatim anchor at Step 5: YES.
Verbatim instruction in all three phase Paraphrase clause fields: YES.
Audit result — Phase 1 P2/P3 compliance: [PASS/FAIL].
Audit result — Phase 2 within P1/P2 range: [PASS/FAIL].
Audit result — Phase 3 P0/P1 compliance: [PASS/FAIL].
Paraphrase consistent with audit results: YES / NO."

**Sub-check 2: Switching-Friction Sub-Section Field Completeness**

Confirm the Switching-Friction Gaps sub-section from Step 8 is present.
Scan every entry for the `Migrating from:` field:
- List each entry's `Migrating from:` value.
- Flag any entry where the value does not contain the product name from Step 1b verbatim.
State: "Switching-Friction Gaps sub-section present: YES. Migrating from: fields —
[entry 1: value | entry 2: value | ...]. All fields populated with product name
verbatim: YES / NO. Missing or non-verbatim entries: [list or NONE]."

State final: "All Step 5 values match Step 6. Exception sign-offs complete for all
three phase scans. Sub-checks 1 and 2 verified. Paraphrase consistency confirmed."
Name and correct any issue before finalizing.
```

---

## V-02: Single-Axis — Output Format (Phase-Organized Bodies) + Post-Generation Phase Distribution Re-Verify

**Axis:** Output format — card bodies in Step 6 are organized by lifecycle phase window (all Phase 1 tickets as a group, then all Phase 2 tickets as a group, then all Phase 3 tickets as a group) rather than sequential T-01 through T-08 order. Section headers mark the phase boundaries. All other mechanisms from V-05 R15 are preserved exactly. Role activation remains Support → PM → UX → SRE → C-01..C-12.

**Probe (C-48 candidate):** V-05 R15 adds the PHASE DISTRIBUTION committed block to Step 5 (C-45) and verifies the count match at Step 5B constraint 0 before body generation. The verification is pre-generation only: once body generation begins, no structural gate re-verifies that the generated phase distribution matches the committed block. A model may drift — generating an extra Phase 2 ticket while dropping a Phase 3 — without triggering any post-generation structural constraint. V-02 R16 adds a post-generation PHASE DISTRIBUTION re-verification step in Part C sub-check 3: count actual Phase 1, Phase 2, Phase 3 bodies, compare to the Step 5 committed block, and name any discrepancy as a structural violation. This closes the generation-drift gap that pre-generation-only verification leaves open.

**Hypothesis:** Phase-organized output format enforces generation-time phase awareness: the model cannot casually add a Phase 2 ticket while writing Phase 3 cards because the section header makes the phase boundary structurally visible. Combined with post-generation re-verification in Part C, the probability of phase drift across the full output approaches zero. V-02 tests whether C-48 (requiring post-generation re-verify of the committed distribution) is independently extractable from C-45 (requiring pre-generation commitment), and whether phase-organized output produces measurably more consistent phase distribution than ticket-ID-sequential output.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- INERTIA: STATUS QUO

Establish the current-state baseline and name the inertia competitor.

**1a. Current-state baseline**
Describe in 2-3 sentences: what are users doing today to accomplish the job
this feature addresses? Where is friction highest? What workarounds exist
and what do they cost?

**1b. Inertia competitor declaration**

INERTIA COMPETITOR: [product name]
Prohibited: "existing tooling", "their current system", "legacy workflow",
or any phrase that does not produce a grep-checkable product name string.

This product name will be embedded in the performance mode declaration in Step 4,
appear verbatim in every Phase 1 and Phase 3 ticket body, and appear verbatim in
the `Migrating from:` field of every switching-friction gap. Record it once here.

**1c. Adoption-curve context**
Note where the user population sits: early (dual-tool phase), mid-transition, or late
(parity-gap phase). This drives phase distribution in Step 5.

---

## STEP 2 -- PHASE MAP TABLE

| Phase | Window | Expected severity range | Expected volume character |
|-------|--------|------------------------|--------------------------|
| Phase 1 | Day 0–30 | P2/P3 | high |
| Phase 2 | Day 31–60 | P1/P2 | medium |
| Phase 3 | Day 61–90 | P0/P1 | medium/low |

---

## STEP 2B -- PHASE BODY TEMPLATE TABLE

Replace [INERTIA COMPETITOR] with the product name from Step 1b before writing this table.

| Phase | Adoption stance | Pre-printed template sentence |
|-------|----------------|-------------------------------|
| Phase 1 | Dual-tool tension | "I still have [INERTIA COMPETITOR] open in another tab while working through this — I keep switching back to check how it handled [specific scenario]." |
| Phase 3 | Parity gap | "In [INERTIA COMPETITOR] I could [specific action] without leaving this screen; here I cannot find a way to do it at all." |

Instructions:
- Phase 1 bodies: include the Phase 1 sentence with all placeholders filled concretely.
- Phase 3 bodies: include the Phase 3 sentence with all placeholders filled concretely.
- Phase 2 bodies: reference the competitor where it naturally fits; no template required.

---

## STEP 2C -- PHASE-SEVERITY INFERENCE RULE

Do not proceed to Step 3 until this step is complete.

**The directional rule:**

Phase 1 tickets (Day 0–30) MUST be P2 or P3 for non-outage issues.
- Reason: The inertia competitor is still available. Adoption friction is expected.
  A workaround exists — return to the competitor and complete the task there.
  Lower severity reflects that the user is not blocked; they are learning.

Phase 3 tickets (Day 61–90) that block task completion MUST be P1 or P0.
- Reason: Phase 3 users have committed to the new product. The inertia competitor
  is no longer in their daily workflow. Parity gaps that prevent task completion
  have no fallback path. Higher severity reflects that the user is blocked with
  no alternative.

**Violation conditions (apply in Steps 5, 5B, and Pass 2 INFERENCE AUDIT):**
- Phase 1 P0 or P1 on a non-outage ticket: violation — correct to P2/P3.
- Phase 3 P3 on a ticket where the user cannot complete a task: violation — correct to P1/P0.

**Required confirmation before proceeding:**
State the inference rule in your own words as a named constraint. This paraphrase will
be recalled at Step 5 and verified in Pass 2 Part C. Write a genuine restatement —
not a copy of the rule above:

INFERENCE RULE (stated): [your paraphrase of the directional rule above]
Applied in: Steps 5, 5B, and Pass 2 INFERENCE AUDIT

Do not proceed to Step 3 until this block is filled with your own-words paraphrase.

---

## STEP 3 -- ROLE ACTIVATION ORDER

Activate roles in order: Support → PM → UX → SRE → C-01 through C-12.
Each role contributes ticket hypotheses before the next role activates.

[Support] — Activate first. Focus on triage-queue patterns, first-call resolution
blockers, documentation gaps, error message clarity, and category distribution.

[PM] — Activate second. Focus on intent gaps: what the feature promised vs what
shipped, roadmap items surfacing as Phase 3 tickets, feature-request backlog.

[UX] — Activate third. Focus on discoverability failures, onboarding friction,
and how-to ticket patterns driven by interface ambiguity.

[SRE] — Activate fourth. Focus on operational failure modes: configuration errors,
deployment issues, on-call escalation scenarios, infrastructure-level P0/P1 candidates.

[C-01 through C-12] — Activate in ID order, each contributing one ticket hypothesis
from their archetype.

---

## STEP 4 -- PERFORMANCE MODE DECLARATION

**You ARE the persona named on each ticket card.**

Your previous primary workflow used [INERTIA COMPETITOR — insert product name from Step 1b].
You recently started using this new product. You are in some stage of migration:
Phase 1 tickets are written when you still have the old tool open — lower stakes because
you can fall back. Phase 3 tickets are written when you have committed to the new tool
and cannot fall back — higher stakes because you are blocked.

Do not write "the user", "they", "the SRE", "the PM", "the engineer",
or any named-role title referring to yourself in third person.

Prohibited verb-subject forms: "the SRE ran", "the PM reviewed", "the engineer observed",
"the C-07 clicked", "the Support agent opened", or any construction where a role title
precedes a verb.

**Every action in this ticket was taken by "I". Every reference to the old tool
uses its product name, not a pronoun or generic description.**

---

## STEP 5 -- VOCABULARY PRE-COMMITMENT TABLE

Competitor in scope: [write the product name from Step 1b here — do not write "the tool",
"my old system", or any alias. This name must appear verbatim in every Phase 1 and Phase 3
ticket body in Step 6.]

Do not fill any cell in the table until all three items are written:

Required item 1 — INFERENCE RULE (confirmed):
[restate the directional rule from your Step 2C paraphrase in your own words]

Required item 2 — Verbatim from 2C:
[copy your exact first sentence from the INFERENCE RULE (stated) block in Step 2C —
word for word, do not paraphrase]

Required item 3 — PHASE DISTRIBUTION committed block:
  Phase 1 (Day 0–30): [N] tickets
  Phase 2 (Day 31–60): [N] tickets
  Phase 3 (Day 61–90): [N] tickets
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

Allowed values:
- Category: {how-to, bug, feature-request, config, integration}
- Volume: {high, medium, low}
- Severity: {P0, P1, P2, P3}

**Lock vocabulary values here. Full card bodies follow in Step 6.**

---

## STEP 5B -- COLLECTIVE DISTRIBUTION AUDIT

Audit five constraints before writing any card body:

Constraint 0: PHASE DISTRIBUTION count-match check — Phase 1, Phase 2, and Phase 3
row counts must equal the Phase Distribution committed block in Step 5.
If they do not match, correct the table now. State: "Phase 1: [n] committed, [n] actual —
MATCH/MISMATCH. Phase 2: MATCH/MISMATCH. Phase 3: MATCH/MISMATCH."

1. **Phase distribution** — at least two Phase 1 rows and one Phase 3 row.
2. **Category spread** — at least three distinct category values.
3. **Volume distribution** — all three volume levels present.
4. **Phase-character compliance** — each row's volume and severity match Step 2 ranges.
5. **Inference-rule compliance** — scan Phase 1 rows for P0/P1 on non-outage tickets;
   scan Phase 3 rows for P3 on blocking tickets.
   State PASS if no violations; FAIL and name the row and correction if any found.

State PASS or FAIL per constraint.
**If any fails, correct the table and re-run. Name the correction.**

---

## STEP 5C -- PRE-BODY STRUCTURAL VERIFICATION (PASS 2B)

Before writing the first card body, verify four structural properties:

Item 1 — CATEGORY DISTRIBUTION CHECK:
Count tickets per category. If any single category exceeds 60% of total tickets, reconsider.

Item 2 — PERSONA DISTRIBUTION CHECK:
Confirm at least one ticket is attributed to each role group activated in Step 3.

Item 3 — PHASE DISTRIBUTION COMPLIANCE:
Confirm the table row counts match the PHASE DISTRIBUTION committed block from Step 5.
State: "Phase 1: [n]. Phase 2: [n]. Phase 3: [n]. Total: [n]. Matches committed block: YES/NO."

Item 4 — SWITCHING-FRICTION COUNT CHECK:
SWITCHING-FRICTION COUNT: [N]
N must be ≥ 2. State before continuing.
Do not proceed to Step 6 if N < 2.

---

## STEP 6 -- FULL CARD BODIES (PHASE-ORGANIZED)

Card bodies are organized by lifecycle phase. Complete all Phase 1 cards first,
then all Phase 2 cards, then all Phase 3 cards. Within each phase group, cards
appear in ascending Ticket ID order.

---

### Phase 1 Cards (Day 0–30)

For each Phase 1 row from the vocabulary table:

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [must match Step 5 exactly]
Persona: [must match Step 5 exactly]
Volume: [must match Step 5 exactly]
Severity: [must match Step 5 exactly — P2 or P3]

Body:
[You ARE this persona. Open with the Phase 1 template sentence from Step 2B,
placeholders filled concretely with the inertia competitor product name.
Reference the STATUS QUO element from Step 1 that drives this ticket's volume.
No third-person references to yourself. Every old-tool mention uses the product name.]

---

### Phase 2 Cards (Day 31–60)

For each Phase 2 row from the vocabulary table:

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [must match Step 5 exactly]
Persona: [must match Step 5 exactly]
Volume: [must match Step 5 exactly]
Severity: [must match Step 5 exactly — P1 or P2]

Body:
[You ARE this persona. Reference the competitor where it naturally fits — the user
is in transition, partially committed to the new tool but not fully detached from
the competitor. Reference the STATUS QUO element from Step 1.
No third-person references to yourself.]

---

### Phase 3 Cards (Day 61–90)

For each Phase 3 row from the vocabulary table:

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [must match Step 5 exactly]
Persona: [must match Step 5 exactly]
Volume: [must match Step 5 exactly]
Severity: [must match Step 5 exactly — P0 or P1]

Body:
[You ARE this persona. Open with the Phase 3 template sentence from Step 2B,
placeholders filled concretely with the inertia competitor product name.
Reference the STATUS QUO element from Step 1 that drives this ticket's severity.
No third-person references to yourself. Every old-tool mention uses the product name.]

---

## STEP 7 -- CROSS-TICKET PATTERNS

For each pattern, use this flat field structure with no parent "Consequence:" container:

Pattern name: [short name]
Tickets affected: [T-NN, T-NN, ...]
Root cause: [one sentence]

Consequence — Affected segment:
Prohibited: "users in general", "the team", or any unnamed group.
[Named role or cohort tied specifically to this pattern]

Consequence — Day-90 scenario:
Prohibited: "this will cause confusion" or any non-pattern-specific event.
[One specific event that occurs if this pattern is not addressed by Day 90]

Consequence — Adoption cost:
Prohibited: generic friction not specific to this cohort.
[One sentence quantifying the friction for the named segment]

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

SWITCHING-FRICTION COUNT: [N]
N must be ≥ 2. State this before writing any entry.

Switching-friction gap: [short name]
Migrating from: [product name from Step 1b — verbatim, grep-checkable]
Expected behavior: [one sentence]
Actual behavior: [one sentence]
Migration impact: [one sentence]

### Pre-Launch Priority
Name the single gap to close first. Tie to specific ticket IDs, severity, and volume.

---

## STEP 9 -- DUAL-PASS VERIFICATION

### PASS 1 -- Coverage Trace Table

| Ticket ID | STATUS QUO element referenced | Gap traced to |
|-----------|-------------------------------|---------------|

Populate one row per ticket, in Ticket ID order.

After completing the table:
1. Confirm: "No gap from the Gap Analysis — including switching-friction gaps — is absent from this table."
2. Confirm: "The inertia competitor product name appears in at least two STATUS QUO element cells."

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 -- Properties Verify + Inference Audit

**PART A — Frontmatter Verify**

Confirm the summary table from Step 5 matches every Ticket ID, Phase, Category,
Persona, Volume, and Severity in the full card bodies from Step 6.
State: "All Step 5 values match Step 6 card bodies."

**PART B — Property Checks**

1. Tool-name fidelity check.
   State: "[PRODUCT NAME] in Step 1b: YES. Card bodies: [T-NN, T-NN minimum].
   Migrating from: field: YES."

2. Phase-differentiated templates check.
   State: "Phase 1 template in: [T-NN, T-NN]. Phase 3 template in: [T-NN]."

3. Switching-friction 4-field format check.
   State: "All four fields present in all entries: YES / NO."

**PART C — Inference Audit**

**Sub-check 1: Phase-Architecture Severity Compliance**

Scan Phase 1 rows (from Phase 1 card section in Step 6):
- Exception block for any Phase 1 P0/P1 ticket, or no-exception confirmation:

"No Phase 1 P0/P1 exceptions. Phase 1 lifecycle: fallback available.
Governing paraphrase clause: [copy the exact Phase 1 clause from INFERENCE RULE (stated)
at Step 2C — do not paraphrase, do not summarize, copy it verbatim word-for-word]."

Scan Phase 3 rows (from Phase 3 card section in Step 6):
- Exception block for any Phase 3 P3 ticket, or no-exception confirmation:

"No Phase 3 P3 exceptions. Phase 3 lifecycle: no fallback.
Governing paraphrase clause: [copy the exact Phase 3 clause from INFERENCE RULE (stated)
at Step 2C — do not paraphrase, do not summarize, copy it verbatim word-for-word]."

Paraphrase consistency confirmation:
State: "INFERENCE RULE paraphrase (Step 2C): [quote first 10 words].
Verbatim anchor at Step 5: YES.
Phase 1 compliance: PASS/FAIL. Phase 3 compliance: PASS/FAIL.
Paraphrase consistent with audit results: YES / NO."

**Sub-check 2: Switching-Friction Sub-Section Field Completeness**

Scan every entry in the Switching-Friction Gaps sub-section.
State: "Switching-Friction Gaps sub-section present: YES.
Migrating from: fields — [entry 1: value | entry 2: value | ...].
All fields populated with product name verbatim: YES / NO."

**Sub-check 3: Post-Generation Phase Distribution Re-Verification**

Count the actual Phase 1, Phase 2, and Phase 3 card bodies generated in Step 6.
Compare each count to the PHASE DISTRIBUTION committed block from Step 5.

State: "Post-generation phase distribution:
Phase 1 bodies generated: [n]. Committed: [n]. MATCH / MISMATCH.
Phase 2 bodies generated: [n]. Committed: [n]. MATCH / MISMATCH.
Phase 3 bodies generated: [n]. Committed: [n]. MATCH / MISMATCH.
Total: [n] generated. Committed: [n]. MATCH / MISMATCH."

If any MISMATCH: name the discrepancy, identify which ticket ID drifted, and state
the correction needed. A phase distribution that matched at Step 5B but mismatches
here indicates a generation-time drift — name it explicitly.

State final: "All Step 5 values match Step 6. Exception sign-offs complete.
Sub-checks 1, 2, and 3 verified."
```

---

## V-03: Single-Axis — Lifecycle Emphasis (Equal Allocation Pre-Declared Before STATUS QUO) + Switching-Friction Count Floor ≥ 3

**Axis:** Lifecycle emphasis — the phase distribution target is declared in Step 1 (before STATUS QUO analysis), not at Step 5 (before table-filling). The pre-declaration constrains STATUS QUO analysis: the model must frame the current-state baseline with awareness of the planned phase distribution. All other mechanisms from V-05 R15 are preserved exactly. Role activation remains Support → PM → UX → SRE → C-01..C-12.

**Probe (C-49 candidate):** V-05 R15 raises the switching-friction minimum count from 1 to 2 (C-46). The floor of 2 prevents token compliance (a single entry) but permits a two-entry sub-section that covers only the most obvious migration barriers, leaving secondary competitor barriers uncaptured. V-03 R16 raises the minimum from 2 to 3, adds "SWITCHING-FRICTION COUNT: [N] — N must be ≥ 3" as the pre-count declaration in Step 8, and updates Pass 2B item 4 to verify N ≥ 3.

**Hypothesis:** A floor of 2 closes the single-entry token compliance path. A floor of 3 closes the dual-entry surface-coverage path: two entries typically cover the primary and the most obvious secondary barrier; a third entry forces the model to identify a less obvious migration friction point — the type more likely to generate tickets in Phase 2 (transition) rather than Phase 1 (day-one friction). V-03 tests whether C-49 (switching-friction floor ≥ 3) is independently extractable from C-46 (floor ≥ 2), and whether lifecycle-first framing (distribution declared before STATUS QUO) produces more evenly distributed switching-friction entries across phases.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- PHASE DISTRIBUTION TARGET (declared before STATUS QUO analysis)

Before establishing the STATUS QUO baseline, declare the target ticket distribution
across lifecycle phases. This commitment constrains how you frame the current-state
baseline in Step 1b: the baseline must be rich enough to generate tickets across
all three phases.

PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0–30): [N] tickets (Day-one friction — high volume, low severity)
  Phase 2 (Day 31–60): [N] tickets (Transition friction — medium volume, medium severity)
  Phase 3 (Day 61–90): [N] tickets (Parity gaps — lower volume, high severity)
  Total: [N] tickets

Constraint: Phase 1 count ≥ 2. Phase 3 count ≥ 1. All three phases represented.
This PHASE DISTRIBUTION TARGET will be referenced at Step 5 (vocabulary pre-commitment)
and re-verified at Step 5B (distribution audit) and Pass 2 Part C.

---

## STEP 1B -- INERTIA: STATUS QUO

Establish the current-state baseline and name the inertia competitor.

**1b-i. Current-state baseline**
Describe in 2-3 sentences: what are users doing today to accomplish the job this
feature addresses? Frame the baseline with awareness of the Phase Distribution Target
above — the current-state friction must be rich enough to generate tickets in each
declared phase window.

**1b-ii. Inertia competitor declaration**

INERTIA COMPETITOR: [product name]
Prohibited: "existing tooling", "their current system", "legacy workflow",
or any phrase that does not produce a grep-checkable product name string.

**1b-iii. Adoption-curve context**
Note where the user population sits: early (dual-tool phase), mid-transition, or late
(parity-gap phase). Confirm this is consistent with the Phase Distribution Target above.

---

## STEP 2 -- PHASE MAP TABLE

| Phase | Window | Expected severity range | Expected volume character |
|-------|--------|------------------------|--------------------------|
| Phase 1 | Day 0–30 | P2/P3 | high |
| Phase 2 | Day 31–60 | P1/P2 | medium |
| Phase 3 | Day 61–90 | P0/P1 | medium/low |

---

## STEP 2B -- PHASE BODY TEMPLATE TABLE

Replace [INERTIA COMPETITOR] with the product name from Step 1b-ii.

| Phase | Adoption stance | Pre-printed template sentence |
|-------|----------------|-------------------------------|
| Phase 1 | Dual-tool tension | "I still have [INERTIA COMPETITOR] open in another tab while working through this — I keep switching back to check how it handled [specific scenario]." |
| Phase 3 | Parity gap | "In [INERTIA COMPETITOR] I could [specific action] without leaving this screen; here I cannot find a way to do it at all." |

---

## STEP 2C -- PHASE-SEVERITY INFERENCE RULE

Do not proceed to Step 3 until this step is complete.

**The directional rule:**

Phase 1 tickets (Day 0–30) MUST be P2 or P3 for non-outage issues.
- Reason: The inertia competitor is still available. Adoption friction is expected.
  Lower severity reflects that the user is not blocked; they are learning.

Phase 3 tickets (Day 61–90) that block task completion MUST be P1 or P0.
- Reason: Phase 3 users have committed to the new product. No fallback available.
  Higher severity reflects a blocked user with no alternative.

**Violation conditions:**
- Phase 1 P0/P1 on a non-outage ticket: violation — correct to P2/P3.
- Phase 3 P3 on a blocking ticket: violation — correct to P1/P0.

**Required confirmation:**
INFERENCE RULE (stated): [your paraphrase of the directional rule above]
Applied in: Steps 5, 5B, and Pass 2 INFERENCE AUDIT

Do not proceed until this block is filled with your own-words paraphrase.

---

## STEP 3 -- PERFORMANCE MODE DECLARATION

**You ARE the persona named on each ticket card.**

Your previous primary workflow used [INERTIA COMPETITOR — insert product name from Step 1b-ii].

Do not write "the user", "they", "the SRE", "the PM", "the engineer",
or any named-role title referring to yourself in third person.

Prohibited verb-subject forms: "the SRE ran", "the PM reviewed", "the engineer observed",
"the C-07 clicked", "the Support agent opened", or any construction where a role title
precedes a verb.

**Every action in this ticket was taken by "I".**

---

## STEP 4 -- ROLE ACTIVATION ORDER

Activate roles: Support → PM → UX → SRE → C-01 through C-12.
Each role contributes ticket hypotheses, framed with awareness of the Phase Distribution
Target from Step 1 — each role should identify at least one ticket per phase window
in their analysis.

---

## STEP 5 -- VOCABULARY PRE-COMMITMENT TABLE

Competitor in scope: [product name from Step 1b-ii]

Do not fill any cell in the table until all three items are written:

Required item 1 — INFERENCE RULE (confirmed):
[restate the directional rule from your Step 2C paraphrase in your own words]

Required item 2 — Verbatim from 2C:
[copy your exact first sentence from the INFERENCE RULE (stated) block in Step 2C —
word for word, do not paraphrase]

Required item 3 — PHASE DISTRIBUTION committed block:
Reconcile with the Phase Distribution Target from Step 1. If the numbers differ from
Step 1, name the reconciliation reason.
  Phase 1 (Day 0–30): [N] tickets (Target was [N])
  Phase 2 (Day 31–60): [N] tickets (Target was [N])
  Phase 3 (Day 61–90): [N] tickets (Target was [N])
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

Allowed values:
- Category: {how-to, bug, feature-request, config, integration}
- Volume: {high, medium, low}
- Severity: {P0, P1, P2, P3}

**Lock vocabulary values here. Full card bodies follow in Step 6.**

---

## STEP 5B -- COLLECTIVE DISTRIBUTION AUDIT

Audit five constraints before writing any card body:

Constraint 0: PHASE DISTRIBUTION count-match check — row counts must equal the
Phase Distribution committed block in Step 5.
State: "Phase 1: [n] committed, [n] actual — MATCH/MISMATCH.
Phase 2: MATCH/MISMATCH. Phase 3: MATCH/MISMATCH."
Cross-check against Phase Distribution Target from Step 1:
"Step 1 target vs Step 5 committed: Phase 1 [n] vs [n]. Phase 2 [n] vs [n]. Phase 3 [n] vs [n].
Any reconciliation applied: YES/NO. Reason: [if YES]."

1. **Phase distribution** — at least two Phase 1 rows and one Phase 3 row.
2. **Category spread** — at least three distinct category values.
3. **Volume distribution** — all three volume levels present.
4. **Phase-character compliance** — each row's volume and severity match Step 2 ranges.
5. **Inference-rule compliance** — scan Phase 1/Phase 3 rows for violations.

State PASS or FAIL per constraint.
**If any fails, correct the table and re-run. Name the correction.**

---

## STEP 5C -- PRE-BODY STRUCTURAL VERIFICATION (PASS 2B)

Item 1 — CATEGORY DISTRIBUTION CHECK: Count per category.
Item 2 — PERSONA DISTRIBUTION CHECK: Confirm role coverage.
Item 3 — PHASE DISTRIBUTION COMPLIANCE: Confirm counts match committed block.

Item 4 — SWITCHING-FRICTION COUNT CHECK:
SWITCHING-FRICTION COUNT: [N]
N must be ≥ 3. If you have fewer than 3 switching-friction gap entries prepared, add entries
before continuing. State: "SWITCHING-FRICTION COUNT: [N]. Minimum satisfied (N ≥ 3): YES/NO."
Do not proceed to Step 6 if N < 3.

---

## STEP 6 -- FULL CARD BODIES

For each row in the vocabulary table, in ticket-ID order:

Ticket ID: [T-NN]
Title: [descriptive title]
Category: [must match Step 5 exactly]
Persona: [must match Step 5 exactly]
Volume: [must match Step 5 exactly]
Severity: [must match Step 5 exactly]

Body:
[You ARE this persona. Phase 1: open with Phase 1 template sentence, placeholders filled.
Phase 3: open with Phase 3 template sentence, placeholders filled.
All tickets: reference the STATUS QUO element from Step 1b-i.
No third-person references. Every old-tool mention uses the product name.]

---

## STEP 7 -- CROSS-TICKET PATTERNS

Pattern name: [short name]
Tickets affected: [T-NN, T-NN, ...]
Root cause: [one sentence]

Consequence — Affected segment:
Prohibited: "users in general", "the team", or any unnamed group.
[Named role or cohort]

Consequence — Day-90 scenario:
Prohibited: "this will cause confusion" or any non-pattern-specific event.
[One specific event if unaddressed by Day 90]

Consequence — Adoption cost:
Prohibited: generic friction not specific to this cohort.
[One sentence quantifying friction for the named segment]

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

SWITCHING-FRICTION COUNT: [N]
N must be ≥ 3. State this count before writing any entry.

Switching-friction gap: [short name]
Migrating from: [product name from Step 1b-ii — verbatim, grep-checkable]
Expected behavior: [one sentence]
Actual behavior: [one sentence]
Migration impact: [one sentence]

Include at minimum three entries. Third entry must cover a migration barrier that
surfaces in Phase 2 (transition) rather than Phase 1 (day-one friction) — a barrier
that only becomes visible after partial commitment, not on the first day.

### Pre-Launch Priority
Name the single gap to close first. Tie to specific ticket IDs, severity, and volume.

---

## STEP 9 -- DUAL-PASS VERIFICATION

### PASS 1 -- Coverage Trace Table

| Ticket ID | STATUS QUO element referenced | Gap traced to |
|-----------|-------------------------------|---------------|

Populate one row per ticket.

After completing:
1. Confirm: "No gap from the Gap Analysis — including switching-friction gaps — is absent."
2. Confirm: "The inertia competitor product name appears in at least two STATUS QUO element cells."

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 -- Properties Verify + Inference Audit

**PART A — Frontmatter Verify**
Confirm Step 5 matches Step 6 card bodies for all fields.
State: "All Step 5 values match Step 6 card bodies."

**PART B — Property Checks**
1. Tool-name fidelity.
2. Phase-differentiated templates.
3. Switching-friction 4-field format.

**PART C — Inference Audit**

**Sub-check 1: Phase-Architecture Severity Compliance**

Scan Phase 1 rows. Exception sign-off or no-exception confirmation:

"No Phase 1 P0/P1 exceptions. Governing paraphrase clause: [copy the exact Phase 1 clause
from INFERENCE RULE (stated) at Step 2C — do not paraphrase, do not summarize, copy it
verbatim word-for-word]."

Scan Phase 3 rows. Exception sign-off or no-exception confirmation:

"No Phase 3 P3 exceptions. Governing paraphrase clause: [copy the exact Phase 3 clause
from INFERENCE RULE (stated) at Step 2C — do not paraphrase, do not summarize, copy it
verbatim word-for-word]."

Paraphrase consistency confirmation:
"INFERENCE RULE paraphrase (Step 2C): [first 10 words].
Phase 1 compliance: PASS/FAIL. Phase 3 compliance: PASS/FAIL.
Paraphrase consistent with audit results: YES / NO."

**Sub-check 2: Switching-Friction Sub-Section Field Completeness**

Confirm the Switching-Friction Gaps sub-section is present.
Restate the declared count: "SWITCHING-FRICTION COUNT: [N]. N ≥ 3: YES/NO."
List each entry's `Migrating from:` value. Flag any non-verbatim value.
State: "All fields populated with product name verbatim: YES / NO."

State final: "All Step 5 values match Step 6. Exception sign-offs complete.
SWITCHING-FRICTION COUNT ≥ 3 confirmed. Sub-checks 1 and 2 verified."
```

---

## V-04: Combined — Role Sequence + Output Format + Phase-2 No-Exception + Post-Generation Re-Verify

**Axis:** Combination of V-01 (SRE-first role sequence + Phase 2 no-exception triple-clause probe) and V-02 (phase-organized output format + post-generation PHASE DISTRIBUTION re-verification probe). All other mechanisms from V-05 R15 preserved.

**Hypothesis:** V-01 generates a Phase 2 no-exception confirmation that must be triple-clause verbatim; V-02 adds a post-generation re-verify of phase distribution in Part C. Combining them means Part C contains three phase scans (Phase 1, Phase 2, Phase 3 no-exception or exception blocks) AND a post-generation count re-verification. The SRE-first ordering is expected to produce non-trivial Phase 2 escalation patterns, making the Phase 2 scan in Part C a meaningful rather than trivial audit. The phase-organized output format makes the post-generation count verification visually self-confirming: the scorer counts section headers rather than parsing individual ticket IDs.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- INERTIA: STATUS QUO

**1a. Current-state baseline**
Describe in 2-3 sentences: what are users doing today? Where is friction highest?
What workarounds exist?

**1b. Inertia competitor declaration**
INERTIA COMPETITOR: [product name]
Prohibited: any phrase that does not produce a grep-checkable product name string.

**1c. Adoption-curve context**
Note user population position: early (dual-tool phase), mid-transition, or late
(parity-gap phase).

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
Phase 2 bodies: reference the competitor where natural; no template required.

---

## STEP 2C -- PHASE-SEVERITY INFERENCE RULE

Phase 1 (Day 0–30): P2/P3 on non-outage tickets. Fallback available; user is learning.
Phase 3 (Day 61–90): P1/P0 on blocking tickets. No fallback; user is committed and blocked.

Violation conditions:
- Phase 1 P0/P1 non-outage: violation.
- Phase 3 P3 blocking: violation.

INFERENCE RULE (stated): [your paraphrase of the directional rule above]
Applied in: Steps 5, 5B, and Pass 2 INFERENCE AUDIT

Do not proceed until this block is filled.

---

## STEP 3 -- ROLE ACTIVATION ORDER (SRE-FIRST)

Activate roles in this order: SRE → Support → PM → UX → C-01 through C-12.

[SRE] — Activate first. Operational failure modes: configuration, deployment, on-call
escalation, infrastructure-level P0/P1 candidates. Identify Phase 2 escalation patterns.

[Support] — Activate second. Triage-queue patterns, documentation gaps, error message
clarity, category distribution.

[PM] — Activate third. Intent gaps, roadmap tickets, feature-request patterns.

[UX] — Activate fourth. Discoverability failures, onboarding friction, how-to patterns.

[C-01 through C-12] — One ticket hypothesis each, in ID order.

---

## STEP 4 -- PERFORMANCE MODE DECLARATION

**You ARE the persona named on each ticket card.**

Your previous primary workflow used [INERTIA COMPETITOR — product name from Step 1b].
Phase 1: old tool still open, can fall back. Phase 3: committed, no fallback.

Prohibited third-person forms: "the user", "they", "the SRE", "the PM", "the engineer".
Prohibited verb-subject forms: "the SRE ran", "the PM reviewed", "the engineer observed",
"the C-07 clicked", "the Support agent opened".
**Every action: "I". Every old-tool reference: product name.**

---

## STEP 5 -- VOCABULARY PRE-COMMITMENT TABLE

Competitor in scope: [product name from Step 1b]

Do not fill any cell in the table until all three items are written:

Required item 1 — INFERENCE RULE (confirmed):
[restate in your own words]

Required item 2 — Verbatim from 2C:
[copy exact first sentence from INFERENCE RULE (stated) at Step 2C — word for word, do not paraphrase]

Required item 3 — PHASE DISTRIBUTION committed block:
  Phase 1 (Day 0–30): [N] tickets
  Phase 2 (Day 31–60): [N] tickets
  Phase 3 (Day 61–90): [N] tickets
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
State: "Phase 1: [n] committed, [n] actual — MATCH/MISMATCH. Phase 2: … Phase 3: …"

1. Phase distribution — ≥2 Phase 1 rows, ≥1 Phase 3 row.
2. Category spread — ≥3 distinct categories.
3. Volume distribution — all three levels present.
4. Phase-character compliance — severity/volume match Step 2 ranges.
5. Inference-rule compliance — scan Phase 1/Phase 3 for violations.

**If any fails, correct and re-run.**

---

## STEP 5C -- PRE-BODY STRUCTURAL VERIFICATION (PASS 2B)

Item 1 — Category distribution check.
Item 2 — Persona distribution check.
Item 3 — Phase distribution compliance.

Item 4 — SWITCHING-FRICTION COUNT CHECK:
SWITCHING-FRICTION COUNT: [N]
N must be ≥ 2. Do not proceed to Step 6 if N < 2.

---

## STEP 6 -- FULL CARD BODIES (PHASE-ORGANIZED)

Organize bodies by phase window. Complete all Phase 1 cards, then Phase 2, then Phase 3.
Within each phase, ascending Ticket ID order.

### Phase 1 Cards (Day 0–30)

Ticket ID: [T-NN] | Category: [match Step 5] | Persona: [match Step 5] | Volume: [match Step 5] | Severity: [P2/P3]
Title: [descriptive title]
Body: [Open with Phase 1 template sentence, placeholders filled. No third-person. Product name for old tool.]

### Phase 2 Cards (Day 31–60)

Ticket ID: [T-NN] | Category: [match Step 5] | Persona: [match Step 5] | Volume: [match Step 5] | Severity: [P1/P2]
Title: [descriptive title]
Body: [Transition framing. Reference competitor where natural. No third-person. Product name for old tool.]

### Phase 3 Cards (Day 61–90)

Ticket ID: [T-NN] | Category: [match Step 5] | Persona: [match Step 5] | Volume: [match Step 5] | Severity: [P0/P1]
Title: [descriptive title]
Body: [Open with Phase 3 template sentence, placeholders filled. No third-person. Product name for old tool.]

---

## STEP 7 -- CROSS-TICKET PATTERNS

Pattern name: [short name]
Tickets affected: [T-NN, ...]
Root cause: [one sentence]

Consequence — Affected segment:
Prohibited: "users in general", "the team", any unnamed group.
[Named cohort]

Consequence — Day-90 scenario:
Prohibited: "this will cause confusion", any non-specific event.
[One specific event if unaddressed]

Consequence — Adoption cost:
Prohibited: generic friction.
[One sentence quantifying friction for the named segment]

---

## STEP 8 -- GAP ANALYSIS

### Doc Gaps
### Design Gaps
### Operational Gaps

### Switching-Friction Gaps
SWITCHING-FRICTION COUNT: [N] — N must be ≥ 2.

Switching-friction gap: [name]
Migrating from: [product name — verbatim]
Expected behavior: [one sentence]
Actual behavior: [one sentence]
Migration impact: [one sentence]

### Pre-Launch Priority

---

## STEP 9 -- DUAL-PASS VERIFICATION

### PASS 1 -- Coverage Trace Table

| Ticket ID | STATUS QUO element referenced | Gap traced to |
|-----------|-------------------------------|---------------|

Confirm: no gap absent from table. Inertia competitor in ≥2 STATUS QUO cells.

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 -- Properties Verify + Inference Audit

**PART A — Frontmatter Verify**
Confirm Step 5 matches Step 6 card bodies.
State: "All Step 5 values match Step 6 card bodies."

**PART B — Property Checks**
1. Tool-name fidelity.
2. Phase-differentiated templates.
3. Switching-friction 4-field format.

**PART C — Inference Audit**

**Sub-check 1: Phase-Architecture Severity Compliance**

Scan Phase 1 cards (Phase 1 section, Step 6). Exception sign-off for any P0/P1, or:
"No Phase 1 P0/P1 exceptions. Governing paraphrase clause: [copy exact Phase 1 clause
from INFERENCE RULE (stated) at Step 2C — do not paraphrase, do not summarize, copy it
verbatim word-for-word]."

Scan Phase 2 cards (Phase 2 section, Step 6). Exception sign-off for any P0 escalation, or:
"No Phase 2 P0 escalation exceptions. Phase 2 lifecycle: transition (partial fallback).
Governing paraphrase clause: [copy exact Phase 2 clause from INFERENCE RULE (stated)
at Step 2C — do not paraphrase, do not summarize, copy it verbatim word-for-word]."

Scan Phase 3 cards (Phase 3 section, Step 6). Exception sign-off for any P3, or:
"No Phase 3 P3 exceptions. Governing paraphrase clause: [copy exact Phase 3 clause
from INFERENCE RULE (stated) at Step 2C — do not paraphrase, do not summarize, copy it
verbatim word-for-word]."

Paraphrase consistency confirmation:
"INFERENCE RULE paraphrase (Step 2C): [first 10 words]. Verbatim anchor at Step 5: YES.
All three phase Paraphrase clause fields carry triple-clause verbatim: YES.
Phase 1 compliance: PASS/FAIL. Phase 2 within range: PASS/FAIL. Phase 3 compliance: PASS/FAIL.
Paraphrase consistent with audit results: YES / NO."

**Sub-check 2: Switching-Friction Sub-Section Field Completeness**
State: "Sub-section present: YES. Migrating from fields: [entry 1 | entry 2 | ...].
All verbatim: YES / NO."

**Sub-check 3: Post-Generation Phase Distribution Re-Verification**
Count Phase 1, Phase 2, Phase 3 card sections in Step 6.
State: "Phase 1 generated: [n]. Committed: [n]. MATCH/MISMATCH.
Phase 2 generated: [n]. Committed: [n]. MATCH/MISMATCH.
Phase 3 generated: [n]. Committed: [n]. MATCH/MISMATCH.
Total: [n] generated. Committed: [n]. MATCH/MISMATCH."
If MISMATCH: name the discrepancy and correction needed.

State final: "All Step 5 values match Step 6. Exception sign-offs complete for all
three phase scans. Sub-checks 1, 2, and 3 verified."
```

---

## V-05: Full Synthesis — All Three Axes + All Three Probes

**Axis:** Full combination of V-01 (SRE-first + Phase 2 no-exception triple-clause), V-02 (phase-organized output + post-generation re-verify), and V-03 (lifecycle emphasis + switching-friction count ≥ 3). Targets 280/280 on v15 plus potential above-ceiling credit on C-47, C-48, and C-49 candidates.

**Hypothesis:** The three probes are structurally independent: C-47 targets the Phase 2 no-exception confirmation path (new scan location), C-48 targets post-generation phase distribution verification (new temporal gate), C-49 targets switching-friction count floor (new minimum threshold). Combining all three closes three simultaneously: Phase 2 audit path, phase drift detection after body generation, and surface-coverage floor for switching-friction entries. V-05 tests whether all three probes can coexist in a single prompt without structural interference, and whether the full combination generates a qualitatively richer output than any single-axis variation.

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
and Pass 2 Part C sub-check 3.

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
competitor where the framing naturally calls for it (e.g., "I tried the approach that worked
in [INERTIA COMPETITOR]..."). Reference the STATUS QUO element from Step 1b-i.
No third-person. Product name for old tool.]

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
Post-generation phase distribution matches committed block and Step 1 target.
Sub-checks 1, 2, and 3 verified. All C-01 through C-46 constraints met.
C-47 probe (Phase 2 no-exception triple-clause): complete.
C-48 probe (post-generation phase distribution re-verify): complete.
C-49 probe (switching-friction count ≥ 3): complete."
```
