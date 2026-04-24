# listen-support Round 15 -- Skill Body Prompt Variations

**Rubric target**: v14 (265 pts)
**New criteria probed**: C-44 candidate (No-Exception Path Triple-Clause), C-45 candidate (Phase Distribution Pre-Commitment Gate), C-46 candidate (Switching-Friction Minimum Count Gate)
**Base**: V-04 from R14 (265/265 under v14 -- all C-01 through C-43 at ceiling)

**Variation axes selected** (3 single-axis, then 2 combined):
1. **Phrasing register** -- no-exception path verbatim instruction upgraded from single-clause "do not paraphrase" to triple-clause "do not paraphrase, do not summarize, copy it verbatim word-for-word" (V-01)
2. **Lifecycle emphasis** -- phase distribution pre-commitment gate added to Step 4 header; model must declare planned phase counts before filling any cell (V-02)
3. **Output format** -- switching-friction gap minimum upgraded from "one required, two recommended" to "minimum two required" with pre-count declaration gate before the section (V-03)
4. **V-01 + V-02 combined** -- no-exception triple-clause + phase distribution pre-commitment gate (V-04)
5. **Full synthesis** -- all three new axes: no-exception triple-clause + phase pre-commitment + switching-friction count gate (V-05)

**R15 criterion hypothesis matrix:**

| Criterion candidate | V-01 | V-02 | V-03 | V-04 | V-05 |
|--------------------|------|------|------|------|------|
| C-01 through C-43 (all prior) | YES | YES | YES | YES | YES |
| C-44 candidate: No-Exception Triple-Clause | YES | -- | -- | YES | YES |
| C-45 candidate: Phase Distribution Pre-Commitment | -- | YES | -- | YES | YES |
| C-46 candidate: Switching-Friction Count Gate | -- | -- | YES | -- | YES |

---

## V-01: Single-Axis -- No-Exception Path Triple-Clause Verbatim (Phrasing Register)

**Axis**: Phrasing register of the no-exception verbatim instruction in Pass 2 Part C. In V-04 R14, the EXCEPTION SIGN-OFF BLOCK's Paraphrase clause field carries the full triple-clause verbatim prohibition ("do not paraphrase, do not summarize, copy it word-for-word") satisfying C-43. The no-exception path -- used whenever a ticket set has no Phase 1 P0/P1 assignments and no Phase 3 P3 assignments, which is the common case -- carries only a single clause ("do not paraphrase"). V-01 upgrades both no-exception confirmation statements (Phase 1 and Phase 3) to the full triple-clause form: "do not paraphrase, do not summarize, copy it verbatim word-for-word." All other mechanisms from V-04 R14 are preserved without modification.

**Hypothesis**: C-43 closes the condensation path (summary) in the exception block by adding "do not summarize" alongside "do not paraphrase" and "copy it word-for-word." The no-exception path appears more frequently than the exception path: most ticket sets have no Phase 1 P0/P1 exceptions and no Phase 3 P3 exceptions, meaning the no-exception confirmation is executed for both phase scans on nearly every run. Each no-exception write is a verbatim-retrieval task -- the model must copy the governing clause from the INFERENCE RULE (stated) at Step 2C. The condensation path C-43 closes in the exception block is equally available in the no-exception path: "short form: Phase 1 no P0/P1" is neither a paraphrase nor a verbatim copy, but it is a summary, and "do not paraphrase" does not prohibit it. Upgrading the no-exception path to triple-clause mirrors C-43's fix at the location where it is exercised most often. V-01 tests whether a new criterion analogous to C-43 but targeting the no-exception path (C-44 candidate) is reachable, and whether the no-exception path produces meaningfully different output under single-clause vs triple-clause instruction.

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

```
INERTIA COMPETITOR: [product name]
Prohibited: "existing tooling", "their current system", "legacy workflow",
or any phrase that does not produce a grep-checkable product name string.
```

This product name will be embedded in the performance mode declaration in Step 3,
appear verbatim in every Phase 1 and Phase 3 ticket body, and appear verbatim in
the `Migrating from:` field of every switching-friction gap. Record it once here.

**1c. Adoption-curve context**
Note where the user population sits: early (dual-tool phase) or late (parity-gap phase).
This drives phase distribution in Step 4.

---

## STEP 2 -- PHASE MAP TABLE

| Phase | Window | Expected severity range | Expected volume character |
|-------|--------|------------------------|--------------------------|
| Phase 1 | Day 0-30 | P2/P3 | high |
| Phase 2 | Day 31-60 | P1/P2 | medium |
| Phase 3 | Day 61-90 | P0/P1 | medium/low |

---

## STEP 2B -- PHASE BODY TEMPLATE TABLE

Replace [INERTIA COMPETITOR] with the product name from Step 1b before writing this table.

| Phase | Adoption stance | Pre-printed template sentence |
|-------|----------------|-------------------------------|
| Phase 1 | Dual-tool tension | "I still have [INERTIA COMPETITOR] open in another tab while working through this -- I keep switching back to check how it handled [specific scenario]." |
| Phase 3 | Parity gap | "In [INERTIA COMPETITOR] I could [specific action] without leaving this screen; here I cannot find a way to do it at all." |

Instructions:
- Phase 1 bodies: include the Phase 1 sentence with all placeholders filled concretely.
- Phase 3 bodies: include the Phase 3 sentence with all placeholders filled concretely.
- Phase 2 bodies: reference the competitor where it naturally fits; no template required.

---

## STEP 2C -- PHASE-SEVERITY INFERENCE RULE

Do not proceed to Step 3 until this step is complete.

**The directional rule:**

Phase 1 tickets (Day 0-30) MUST be P2 or P3 for non-outage issues.
- Reason: The inertia competitor is still available. Adoption friction is expected.
  A workaround exists -- return to the competitor and complete the task there.
  Lower severity reflects that the user is not blocked; they are learning.

Phase 3 tickets (Day 61-90) that block task completion MUST be P1 or P0.
- Reason: Phase 3 users have committed to the new product. The inertia competitor
  is no longer in their daily workflow. Parity gaps that prevent task completion
  have no fallback path. Higher severity reflects that the user is blocked with
  no alternative.

**Violation conditions (apply in Steps 4, 4B, and Pass 2 INFERENCE AUDIT):**
- Phase 1 P0 or P1 on a non-outage ticket: violation -- correct to P2/P3.
- Phase 3 P3 on a ticket where the user cannot complete a task: violation -- correct to P1/P0.

**Required confirmation before proceeding:**
State the inference rule in your own words as a named constraint. This paraphrase will
be recalled at Step 4 and verified in Pass 2 Part C. Write a genuine restatement --
not a copy of the rule above:

```
INFERENCE RULE (stated): [your paraphrase of the directional rule above]
Applied in: Steps 4, 4B, and Pass 2 INFERENCE AUDIT
```

Do not proceed to Step 3 until this block is filled with your own-words paraphrase.

---

## STEP 3 -- PERFORMANCE MODE DECLARATION

**You ARE the persona named on each ticket card.**

Your previous primary workflow used [INERTIA COMPETITOR -- insert product name from Step 1b].
You recently started using this new product. You are in some stage of migration:
Phase 1 tickets are written when you still have the old tool open -- lower stakes because
you can fall back. Phase 3 tickets are written when you have committed to the new tool
and cannot fall back -- higher stakes because you are blocked.

Do not write "the user", "they", "the SRE", "the PM", "the engineer",
or any named-role title referring to yourself in third person.

Prohibited verb-subject forms: "the SRE ran", "the PM reviewed", "the engineer observed",
"the C-07 clicked", "the Support agent opened", or any construction where a role title
precedes a verb.

**Every action in this ticket was taken by "I". Every reference to the old tool
uses its product name, not a pronoun or generic description.**

---

## STEP 4 -- VOCABULARY PRE-COMMITMENT TABLE

Competitor in scope: [write the product name from Step 1b here -- do not write "the tool",
"my old system", or any alias. This name must appear verbatim in every Phase 1 and Phase 3
ticket body in Step 5.]

Before filling any severity cell, complete both required items below.
Do not fill any cell in the table until both items are written:

Required item 1 -- INFERENCE RULE (confirmed):
[restate the directional rule from your Step 2C paraphrase in your own words]

Required item 2 -- Verbatim from 2C:
[copy your exact first sentence from the INFERENCE RULE (stated) block in Step 2C --
word for word, do not paraphrase]

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

**Lock vocabulary values here. Full card bodies follow in Step 5.**

---

## STEP 4B -- COLLECTIVE DISTRIBUTION AUDIT

Audit five constraints before writing any card body:

1. **Phase distribution** -- at least two Phase 1 rows and one Phase 3 row.
2. **Category spread** -- at least three distinct category values.
3. **Volume distribution** -- all three volume levels present.
4. **Phase-character compliance** -- each row's volume and severity match Step 2 ranges.
5. **Inference-rule compliance** -- apply the INFERENCE RULE confirmed above Step 4:
   - Scan Phase 1 rows: flag any P0 or P1 assignment on a non-outage ticket.
   - Scan Phase 3 rows: flag any P3 assignment on a blocking ticket.
   - State PASS if no violations; FAIL and name the row and correction if any found.

State PASS or FAIL per constraint.
**If any fails, correct the table and re-run. Name the correction.**

---

## STEP 5 -- FULL CARD BODIES

For each row in the summary table:

```
Ticket ID: [T-NN]
Title: [descriptive title]
Category: [must match Step 4 exactly]
Persona: [must match Step 4 exactly]
Volume: [must match Step 4 exactly]
Severity: [must match Step 4 exactly]

Body:
[You ARE this persona. You previously used [INERTIA COMPETITOR -- product name].
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
```

---

## STEP 6 -- CROSS-TICKET PATTERNS

For each pattern, use this flat field structure with no parent "Consequence:" container:

```
Pattern name: [short name]
Tickets affected: [T-NN, T-NN, ...]
Root cause: [one sentence]

Consequence -- Affected segment:
Prohibited: "users in general", "the team", or any unnamed group.
[Named role or cohort tied specifically to this pattern]

Consequence -- Day-90 scenario:
Prohibited: "this will cause confusion" or any non-pattern-specific event.
[One specific event that occurs if this pattern is not addressed by Day 90]

Consequence -- Adoption cost:
Prohibited: generic friction not specific to this cohort.
[One sentence quantifying the friction for the named segment]
```

If a pattern involves migration from the inertia competitor, name the competitor
in the root cause or consequence fields.

---

## STEP 7 -- GAP ANALYSIS

### Doc Gaps
[At least one documentation gap.]

### Design Gaps
[At least one design gap.]

### Operational Gaps
[At least one operational gap.]

### Switching-Friction Gaps
Dedicated sub-section for migration barriers only. NOT absorbed into the above three
sections. At least one entry required. At least two are recommended.

Use this exact 4-field format for every entry:

```
Switching-friction gap: [short name]
Migrating from: [product name from Step 1b -- verbatim, grep-checkable]
Expected behavior: [one sentence -- what users expected, based on the competitor's behavior]
Actual behavior: [one sentence -- what this product actually does or fails to do]
Migration impact: [one sentence -- what users must change, lose, or manually replicate]
```

Rules:
- `Migrating from:` MUST contain the product name from Step 1b verbatim.
  Prohibited: `Migrating from: existing tool`, `Migrating from: legacy workflow`.
- `Expected behavior:` and `Actual behavior:` define the behavior delta --
  they describe the same capability from two perspectives.
- Every entry must be independently enumerable: a reader scanning only this sub-section
  must be able to identify the competitor, the behavior delta, and the migration cost
  without reading any other part of the output.

### Pre-Launch Priority
Name the single gap to close first. Tie to specific ticket IDs, severity, and volume.
State whether it reduces switching-friction for inertia-competitor migrants.

---

## STEP 8 -- DUAL-PASS VERIFICATION

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
1. Confirm: **"No gap from the Gap Analysis -- including switching-friction gaps --
   is absent from this table."**
2. Confirm: **"The inertia competitor product name appears in at least two
   STATUS QUO element cells."**

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 -- Properties Verify + Inference Audit

**PART A -- Frontmatter Verify**

Confirm the summary table from Step 4 matches every Ticket ID, Phase, Category,
Persona, Volume, and Severity in the full card bodies from Step 5.
State: **"All Step 4 values match Step 5 card bodies."**

**PART B -- Property Checks**

1. **Tool-name fidelity** -- product name from Step 1b appears verbatim in Step 1b,
   at least two card bodies, and at least one `Migrating from:` field.
   State: **"[PRODUCT NAME] in Step 1b: YES. Card bodies: T-NN, T-NN (minimum).
   Migrating from: field: YES."**

2. **Phase-differentiated templates** -- at least two Phase 1 bodies contain the
   Phase 1 template from Step 2B, and at least one Phase 3 body contains the Phase 3 template.
   State: **"Phase 1 template in: T-NN, T-NN. Phase 3 template in: T-NN."**

3. **Switching-friction 4-field format** -- every entry in the Switching-Friction Gaps
   sub-section contains all four fields. Scan each entry for: Migrating from, Expected
   behavior, Actual behavior, Migration impact.
   State: **"All four fields present in all entries: YES / NO. Missing: [field list or NONE]."**

**PART C -- Inference Audit**

**Sub-check 1: Phase-Architecture Severity Compliance**

Scan Phase 1 rows in the vocabulary table (Step 4):
- List every Phase 1 ticket assigned P0 or P1.
- For each, fill a Phase 1 EXCEPTION SIGN-OFF BLOCK:

```
EXCEPTION SIGN-OFF (Phase 1 -- fallback available):
Ticket ID: [T-NN]
Phase: 1
Fallback status: Inertia competitor still in active use (fallback available)
Assigned severity: [P0 or P1]
Grounds: [outage-level? YES / NO -- only an outage justifies P0/P1 when fallback exists]
Paraphrase clause: [copy the exact Phase 1 clause from your INFERENCE RULE (stated) at
  Step 2C verbatim -- do not paraphrase, do not summarize, copy it word-for-word]
Disposition: [VALID EXCEPTION -- reason | VIOLATION -- corrected to P2/P3]
```

If no Phase 1 P0/P1 assignments exist, state:
**"No Phase 1 P0/P1 exceptions. Phase 1 lifecycle: fallback available (inertia competitor
in active use). Governing paraphrase clause: [copy the exact Phase 1 clause from your
INFERENCE RULE (stated) at Step 2C -- do not paraphrase, do not summarize, copy it
verbatim word-for-word]."**

Scan Phase 3 rows in the vocabulary table (Step 4):
- List every Phase 3 ticket assigned P3.
- For each, fill a Phase 3 EXCEPTION SIGN-OFF BLOCK:

```
EXCEPTION SIGN-OFF (Phase 3 -- no fallback):
Ticket ID: [T-NN]
Phase: 3
Fallback status: Inertia competitor out of daily workflow (no fallback)
Assigned severity: P3
Grounds: [non-blocking issue? YES / NO -- P3 only valid if user is not blocked]
Paraphrase clause: [copy the exact Phase 3 clause from your INFERENCE RULE (stated) at
  Step 2C verbatim -- do not paraphrase, do not summarize, copy it word-for-word]
Disposition: [VALID EXCEPTION -- reason | VIOLATION -- corrected to P1/P0]
```

If no Phase 3 P3 assignments exist, state:
**"No Phase 3 P3 exceptions. Phase 3 lifecycle: no fallback (inertia competitor out of
daily workflow). Governing paraphrase clause: [copy the exact Phase 3 clause from your
INFERENCE RULE (stated) at Step 2C -- do not paraphrase, do not summarize, copy it
verbatim word-for-word]."**

Confirm the INFERENCE RULE stated in Step 2C and confirmed at Step 4 has been
applied consistently. Compare the paraphrase from Step 2C against the audit results:
State: **"INFERENCE RULE paraphrase (Step 2C): [quote first 10 words of your Step 2C paraphrase].
Verbatim anchor at Step 4: YES.
Verbatim instruction in exception block Paraphrase clause: YES. [Governing clause copied
word-for-word from Step 2C; no paraphrase permitted.]
Audit result -- Phase 1 P2/P3 compliance: [PASS/FAIL].
Audit result -- Phase 3 P0/P1 compliance: [PASS/FAIL].
Paraphrase consistent with audit results: YES / NO."**

**Sub-check 2: Switching-Friction Sub-Section Field Completeness**

Confirm the Switching-Friction Gaps sub-section from Step 7 is present.
Scan every entry for the `Migrating from:` field:
- List each entry's `Migrating from:` value.
- Flag any entry where the value does not contain the product name from Step 1b verbatim.
State: **"Switching-Friction Gaps sub-section present: YES. Migrating from: fields --
[entry 1: value | entry 2: value | ...]. All fields populated with product name
verbatim: YES / NO. Missing or non-verbatim entries: [list or NONE]."**

State final: **"All Step 4 values match Step 5. Exception sign-offs complete.
Sub-checks 1 and 2 verified. Paraphrase consistency confirmed."**
Name and correct any issue before finalizing.
```

---

## V-02: Single-Axis -- Phase Distribution Pre-Commitment Gate (Lifecycle Emphasis)

**Axis**: Lifecycle emphasis -- the Step 4 vocabulary pre-commitment table acquires a third required item before any cell may be filled: a PHASE DISTRIBUTION PRE-COMMITMENT block in which the model declares the planned count of Phase 1, Phase 2, and Phase 3 tickets before filling a single cell. The gate becomes three-item: (1) phase distribution declaration, (2) inference rule restatement, (3) verbatim from Step 2C. Step 4B acquires a new constraint 0 that verifies the table's actual phase distribution matches the declared commitment. All other mechanisms from V-04 R14 are preserved without modification.

**Hypothesis**: Step 4B audits phase distribution post-fill (constraint 1: "at least two Phase 1 rows and one Phase 3 row"). The audit fires after all 8 cells in the Phase column are written. A model that fills T-01 through T-08 as all Phase 1 or all Phase 2 discovers the violation only at 4B, requiring a correction pass. The inference rule pre-commitment gate in V-04 R14 demonstrates that a pre-fill declaration reduces post-hoc correction: the model commits to the rule before any severity cell is written, making violations visible before table-fill completes. A phase distribution pre-commitment creates the same structural contract for phase distribution: the model declares "N Phase 1, M Phase 2, K Phase 3" before any Phase cell is written. The declaration is testable at 4B constraint 0 (match check) without reading the body content -- a scorer counts Phase 1 rows and compares to the committed value. The pre-commitment also forces the model to reason about phase distribution as a plan rather than discovering it post-hoc. V-02 tests whether C-45 (requiring a pre-fill phase distribution contract) is reachable and whether this structural gate produces more consistent phase distribution across the ticket set.

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

```
INERTIA COMPETITOR: [product name]
Prohibited: "existing tooling", "their current system", "legacy workflow",
or any phrase that does not produce a grep-checkable product name string.
```

This product name will be embedded in the performance mode declaration in Step 3,
appear verbatim in every Phase 1 and Phase 3 ticket body, and appear verbatim in
the `Migrating from:` field of every switching-friction gap. Record it once here.

**1c. Adoption-curve context**
Note where the user population sits: early (dual-tool phase) or late (parity-gap phase).
This drives phase distribution in Step 4.

---

## STEP 2 -- PHASE MAP TABLE

| Phase | Window | Expected severity range | Expected volume character |
|-------|--------|------------------------|--------------------------|
| Phase 1 | Day 0-30 | P2/P3 | high |
| Phase 2 | Day 31-60 | P1/P2 | medium |
| Phase 3 | Day 61-90 | P0/P1 | medium/low |

---

## STEP 2B -- PHASE BODY TEMPLATE TABLE

Replace [INERTIA COMPETITOR] with the product name from Step 1b before writing this table.

| Phase | Adoption stance | Pre-printed template sentence |
|-------|----------------|-------------------------------|
| Phase 1 | Dual-tool tension | "I still have [INERTIA COMPETITOR] open in another tab while working through this -- I keep switching back to check how it handled [specific scenario]." |
| Phase 3 | Parity gap | "In [INERTIA COMPETITOR] I could [specific action] without leaving this screen; here I cannot find a way to do it at all." |

Instructions:
- Phase 1 bodies: include the Phase 1 sentence with all placeholders filled concretely.
- Phase 3 bodies: include the Phase 3 sentence with all placeholders filled concretely.
- Phase 2 bodies: reference the competitor where it naturally fits; no template required.

---

## STEP 2C -- PHASE-SEVERITY INFERENCE RULE

Do not proceed to Step 3 until this step is complete.

**The directional rule:**

Phase 1 tickets (Day 0-30) MUST be P2 or P3 for non-outage issues.
- Reason: The inertia competitor is still available. Adoption friction is expected.
  A workaround exists -- return to the competitor and complete the task there.
  Lower severity reflects that the user is not blocked; they are learning.

Phase 3 tickets (Day 61-90) that block task completion MUST be P1 or P0.
- Reason: Phase 3 users have committed to the new product. The inertia competitor
  is no longer in their daily workflow. Parity gaps that prevent task completion
  have no fallback path. Higher severity reflects that the user is blocked with
  no alternative.

**Violation conditions (apply in Steps 4, 4B, and Pass 2 INFERENCE AUDIT):**
- Phase 1 P0 or P1 on a non-outage ticket: violation -- correct to P2/P3.
- Phase 3 P3 on a ticket where the user cannot complete a task: violation -- correct to P1/P0.

**Required confirmation before proceeding:**
State the inference rule in your own words as a named constraint. This paraphrase will
be recalled at Step 4 and verified in Pass 2 Part C. Write a genuine restatement --
not a copy of the rule above:

```
INFERENCE RULE (stated): [your paraphrase of the directional rule above]
Applied in: Steps 4, 4B, and Pass 2 INFERENCE AUDIT
```

Do not proceed to Step 3 until this block is filled with your own-words paraphrase.

---

## STEP 3 -- PERFORMANCE MODE DECLARATION

**You ARE the persona named on each ticket card.**

Your previous primary workflow used [INERTIA COMPETITOR -- insert product name from Step 1b].
You recently started using this new product. You are in some stage of migration:
Phase 1 tickets are written when you still have the old tool open -- lower stakes because
you can fall back. Phase 3 tickets are written when you have committed to the new tool
and cannot fall back -- higher stakes because you are blocked.

Do not write "the user", "they", "the SRE", "the PM", "the engineer",
or any named-role title referring to yourself in third person.

Prohibited verb-subject forms: "the SRE ran", "the PM reviewed", "the engineer observed",
"the C-07 clicked", "the Support agent opened", or any construction where a role title
precedes a verb.

**Every action in this ticket was taken by "I". Every reference to the old tool
uses its product name, not a pronoun or generic description.**

---

## STEP 4 -- VOCABULARY PRE-COMMITMENT TABLE

Competitor in scope: [write the product name from Step 1b here -- do not write "the tool",
"my old system", or any alias. This name must appear verbatim in every Phase 1 and Phase 3
ticket body in Step 5.]

Before filling any cell in the table, complete all three required items below.
Do not fill any cell in the table until all three items are written:

Required item 1 -- PHASE DISTRIBUTION (committed):
```
Phase 1 tickets (Day 0-30): [N -- minimum 2]
Phase 2 tickets (Day 31-60): [N]
Phase 3 tickets (Day 61-90): [N -- minimum 1]
Total: [must equal 8]
```
This distribution will be verified against the table in Step 4B constraint 0.

Required item 2 -- INFERENCE RULE (confirmed):
[restate the directional rule from your Step 2C paraphrase in your own words]

Required item 3 -- Verbatim from 2C:
[copy your exact first sentence from the INFERENCE RULE (stated) block in Step 2C --
word for word, do not paraphrase]

Confirmation: the inference rule applies to every severity assignment in the table below.

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

**Lock vocabulary values here. Full card bodies follow in Step 5.**

---

## STEP 4B -- COLLECTIVE DISTRIBUTION AUDIT

Audit six constraints before writing any card body:

0. **Phase pre-commitment match** -- the phase counts committed in Required item 1 above
   match the Phase column counts in this table.
   State: **"Phase 1: [N committed] planned / [N actual] in table -- MATCH/MISMATCH.
   Phase 2: [N committed] planned / [N actual] in table -- MATCH/MISMATCH.
   Phase 3: [N committed] planned / [N actual] in table -- MATCH/MISMATCH."**
   If MISMATCH: name which phase is off and correct the table before proceeding.

1. **Phase distribution** -- at least two Phase 1 rows and one Phase 3 row.
2. **Category spread** -- at least three distinct category values.
3. **Volume distribution** -- all three volume levels present.
4. **Phase-character compliance** -- each row's volume and severity match Step 2 ranges.
5. **Inference-rule compliance** -- apply the INFERENCE RULE confirmed above Step 4:
   - Scan Phase 1 rows: flag any P0 or P1 assignment on a non-outage ticket.
   - Scan Phase 3 rows: flag any P3 assignment on a blocking ticket.
   - State PASS if no violations; FAIL and name the row and correction if any found.

State PASS or FAIL per constraint.
**If any fails, correct the table and re-run. Name the correction.**

---

## STEP 5 -- FULL CARD BODIES

For each row in the summary table:

```
Ticket ID: [T-NN]
Title: [descriptive title]
Category: [must match Step 4 exactly]
Persona: [must match Step 4 exactly]
Volume: [must match Step 4 exactly]
Severity: [must match Step 4 exactly]

Body:
[You ARE this persona. You previously used [INERTIA COMPETITOR -- product name].
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
```

---

## STEP 6 -- CROSS-TICKET PATTERNS

For each pattern, use this flat field structure with no parent "Consequence:" container:

```
Pattern name: [short name]
Tickets affected: [T-NN, T-NN, ...]
Root cause: [one sentence]

Consequence -- Affected segment:
Prohibited: "users in general", "the team", or any unnamed group.
[Named role or cohort tied specifically to this pattern]

Consequence -- Day-90 scenario:
Prohibited: "this will cause confusion" or any non-pattern-specific event.
[One specific event that occurs if this pattern is not addressed by Day 90]

Consequence -- Adoption cost:
Prohibited: generic friction not specific to this cohort.
[One sentence quantifying the friction for the named segment]
```

If a pattern involves migration from the inertia competitor, name the competitor
in the root cause or consequence fields.

---

## STEP 7 -- GAP ANALYSIS

### Doc Gaps
[At least one documentation gap.]

### Design Gaps
[At least one design gap.]

### Operational Gaps
[At least one operational gap.]

### Switching-Friction Gaps
Dedicated sub-section for migration barriers only. NOT absorbed into the above three
sections. At least one entry required. At least two are recommended.

Use this exact 4-field format for every entry:

```
Switching-friction gap: [short name]
Migrating from: [product name from Step 1b -- verbatim, grep-checkable]
Expected behavior: [one sentence -- what users expected, based on the competitor's behavior]
Actual behavior: [one sentence -- what this product actually does or fails to do]
Migration impact: [one sentence -- what users must change, lose, or manually replicate]
```

Rules:
- `Migrating from:` MUST contain the product name from Step 1b verbatim.
  Prohibited: `Migrating from: existing tool`, `Migrating from: legacy workflow`.
- `Expected behavior:` and `Actual behavior:` define the behavior delta --
  they describe the same capability from two perspectives.
- Every entry must be independently enumerable: a reader scanning only this sub-section
  must be able to identify the competitor, the behavior delta, and the migration cost
  without reading any other part of the output.

### Pre-Launch Priority
Name the single gap to close first. Tie to specific ticket IDs, severity, and volume.
State whether it reduces switching-friction for inertia-competitor migrants.

---

## STEP 8 -- DUAL-PASS VERIFICATION

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
1. Confirm: **"No gap from the Gap Analysis -- including switching-friction gaps --
   is absent from this table."**
2. Confirm: **"The inertia competitor product name appears in at least two
   STATUS QUO element cells."**

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 -- Properties Verify + Inference Audit

**PART A -- Frontmatter Verify**

Confirm the summary table from Step 4 matches every Ticket ID, Phase, Category,
Persona, Volume, and Severity in the full card bodies from Step 5.
State: **"All Step 4 values match Step 5 card bodies."**

**PART B -- Property Checks**

1. **Tool-name fidelity** -- product name from Step 1b appears verbatim in Step 1b,
   at least two card bodies, and at least one `Migrating from:` field.
   State: **"[PRODUCT NAME] in Step 1b: YES. Card bodies: T-NN, T-NN (minimum).
   Migrating from: field: YES."**

2. **Phase-differentiated templates** -- at least two Phase 1 bodies contain the
   Phase 1 template from Step 2B, and at least one Phase 3 body contains the Phase 3 template.
   State: **"Phase 1 template in: T-NN, T-NN. Phase 3 template in: T-NN."**

3. **Switching-friction 4-field format** -- every entry in the Switching-Friction Gaps
   sub-section contains all four fields. Scan each entry for: Migrating from, Expected
   behavior, Actual behavior, Migration impact.
   State: **"All four fields present in all entries: YES / NO. Missing: [field list or NONE]."**

**PART C -- Inference Audit**

**Sub-check 1: Phase-Architecture Severity Compliance**

Scan Phase 1 rows in the vocabulary table (Step 4):
- List every Phase 1 ticket assigned P0 or P1.
- For each, fill a Phase 1 EXCEPTION SIGN-OFF BLOCK:

```
EXCEPTION SIGN-OFF (Phase 1 -- fallback available):
Ticket ID: [T-NN]
Phase: 1
Fallback status: Inertia competitor still in active use (fallback available)
Assigned severity: [P0 or P1]
Grounds: [outage-level? YES / NO -- only an outage justifies P0/P1 when fallback exists]
Paraphrase clause: [copy the exact Phase 1 clause from your INFERENCE RULE (stated) at
  Step 2C verbatim -- do not paraphrase, do not summarize, copy it word-for-word]
Disposition: [VALID EXCEPTION -- reason | VIOLATION -- corrected to P2/P3]
```

If no Phase 1 P0/P1 assignments exist, state:
**"No Phase 1 P0/P1 exceptions. Phase 1 lifecycle: fallback available (inertia competitor
in active use). Governing paraphrase clause: [copy the exact Phase 1 clause from your
INFERENCE RULE (stated) at Step 2C verbatim -- do not paraphrase]."**

Scan Phase 3 rows in the vocabulary table (Step 4):
- List every Phase 3 ticket assigned P3.
- For each, fill a Phase 3 EXCEPTION SIGN-OFF BLOCK:

```
EXCEPTION SIGN-OFF (Phase 3 -- no fallback):
Ticket ID: [T-NN]
Phase: 3
Fallback status: Inertia competitor out of daily workflow (no fallback)
Assigned severity: P3
Grounds: [non-blocking issue? YES / NO -- P3 only valid if user is not blocked]
Paraphrase clause: [copy the exact Phase 3 clause from your INFERENCE RULE (stated) at
  Step 2C verbatim -- do not paraphrase, do not summarize, copy it word-for-word]
Disposition: [VALID EXCEPTION -- reason | VIOLATION -- corrected to P1/P0]
```

If no Phase 3 P3 assignments exist, state:
**"No Phase 3 P3 exceptions. Phase 3 lifecycle: no fallback (inertia competitor out of
daily workflow). Governing paraphrase clause: [copy the exact Phase 3 clause from your
INFERENCE RULE (stated) at Step 2C verbatim -- do not paraphrase]."**

Confirm the INFERENCE RULE stated in Step 2C and confirmed at Step 4 has been
applied consistently. Compare the paraphrase from Step 2C against the audit results:
State: **"INFERENCE RULE paraphrase (Step 2C): [quote first 10 words of your Step 2C paraphrase].
Verbatim anchor at Step 4: YES.
Verbatim instruction in exception block Paraphrase clause: YES. [Governing clause copied
word-for-word from Step 2C; no paraphrase permitted.]
Audit result -- Phase 1 P2/P3 compliance: [PASS/FAIL].
Audit result -- Phase 3 P0/P1 compliance: [PASS/FAIL].
Paraphrase consistent with audit results: YES / NO."**

**Sub-check 2: Switching-Friction Sub-Section Field Completeness**

Confirm the Switching-Friction Gaps sub-section from Step 7 is present.
Scan every entry for the `Migrating from:` field:
- List each entry's `Migrating from:` value.
- Flag any entry where the value does not contain the product name from Step 1b verbatim.
State: **"Switching-Friction Gaps sub-section present: YES. Migrating from: fields --
[entry 1: value | entry 2: value | ...]. All fields populated with product name
verbatim: YES / NO. Missing or non-verbatim entries: [list or NONE]."**

State final: **"All Step 4 values match Step 5. Exception sign-offs complete.
Sub-checks 1 and 2 verified. Paraphrase consistency confirmed."**
Name and correct any issue before finalizing.
```

---

## V-03: Single-Axis -- Switching-Friction Minimum Count Gate (Output Format)

**Axis**: Output format of the Switching-Friction Gaps sub-section. V-04 R14 specifies "at least one entry required. At least two are recommended." V-03 upgrades this to a hard minimum of two entries and adds a pre-count declaration gate that must be written before any entry: the model declares "SWITCHING-FRICTION COUNT: [N -- minimum 2]" and the product name before writing the first entry. The recommendation language is removed; the count is now a required gate. Pass 2 Sub-check 2 acquires a count-match verification step. All other mechanisms from V-04 R14 are preserved without modification.

**Hypothesis**: "At least one required, at least two recommended" is advisory for the second entry. A model that writes one complete, well-formed switching-friction entry satisfies the current rubric's C-04 (gap analysis present) and the explicit minimum. The "at least two recommended" language creates an expectation without a gate. A pre-count declaration gate closes the single-entry shortfall by two mechanisms: (1) it forces the model to plan the count before writing, making a count-of-one declaration structurally visible before any entry is written; (2) Pass 2 Sub-check 2 verifies the count against the declaration, giving the scorer a numeric match check without needing to count entries in prose. The distinction from merely changing "recommended" to "required": the pre-count declaration makes the count a contract, not just a rule. A model can satisfy "required" by writing two weak entries; a model making a count declaration writes toward a committed target. V-03 tests whether C-46 (requiring a pre-count switching-friction contract) is reachable and whether the gate produces consistently richer gap sections.

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

```
INERTIA COMPETITOR: [product name]
Prohibited: "existing tooling", "their current system", "legacy workflow",
or any phrase that does not produce a grep-checkable product name string.
```

This product name will be embedded in the performance mode declaration in Step 3,
appear verbatim in every Phase 1 and Phase 3 ticket body, and appear verbatim in
the `Migrating from:` field of every switching-friction gap. Record it once here.

**1c. Adoption-curve context**
Note where the user population sits: early (dual-tool phase) or late (parity-gap phase).
This drives phase distribution in Step 4.

---

## STEP 2 -- PHASE MAP TABLE

| Phase | Window | Expected severity range | Expected volume character |
|-------|--------|------------------------|--------------------------|
| Phase 1 | Day 0-30 | P2/P3 | high |
| Phase 2 | Day 31-60 | P1/P2 | medium |
| Phase 3 | Day 61-90 | P0/P1 | medium/low |

---

## STEP 2B -- PHASE BODY TEMPLATE TABLE

Replace [INERTIA COMPETITOR] with the product name from Step 1b before writing this table.

| Phase | Adoption stance | Pre-printed template sentence |
|-------|----------------|-------------------------------|
| Phase 1 | Dual-tool tension | "I still have [INERTIA COMPETITOR] open in another tab while working through this -- I keep switching back to check how it handled [specific scenario]." |
| Phase 3 | Parity gap | "In [INERTIA COMPETITOR] I could [specific action] without leaving this screen; here I cannot find a way to do it at all." |

Instructions:
- Phase 1 bodies: include the Phase 1 sentence with all placeholders filled concretely.
- Phase 3 bodies: include the Phase 3 sentence with all placeholders filled concretely.
- Phase 2 bodies: reference the competitor where it naturally fits; no template required.

---

## STEP 2C -- PHASE-SEVERITY INFERENCE RULE

Do not proceed to Step 3 until this step is complete.

**The directional rule:**

Phase 1 tickets (Day 0-30) MUST be P2 or P3 for non-outage issues.
- Reason: The inertia competitor is still available. Adoption friction is expected.
  A workaround exists -- return to the competitor and complete the task there.
  Lower severity reflects that the user is not blocked; they are learning.

Phase 3 tickets (Day 61-90) that block task completion MUST be P1 or P0.
- Reason: Phase 3 users have committed to the new product. The inertia competitor
  is no longer in their daily workflow. Parity gaps that prevent task completion
  have no fallback path. Higher severity reflects that the user is blocked with
  no alternative.

**Violation conditions (apply in Steps 4, 4B, and Pass 2 INFERENCE AUDIT):**
- Phase 1 P0 or P1 on a non-outage ticket: violation -- correct to P2/P3.
- Phase 3 P3 on a ticket where the user cannot complete a task: violation -- correct to P1/P0.

**Required confirmation before proceeding:**
State the inference rule in your own words as a named constraint. This paraphrase will
be recalled at Step 4 and verified in Pass 2 Part C. Write a genuine restatement --
not a copy of the rule above:

```
INFERENCE RULE (stated): [your paraphrase of the directional rule above]
Applied in: Steps 4, 4B, and Pass 2 INFERENCE AUDIT
```

Do not proceed to Step 3 until this block is filled with your own-words paraphrase.

---

## STEP 3 -- PERFORMANCE MODE DECLARATION

**You ARE the persona named on each ticket card.**

Your previous primary workflow used [INERTIA COMPETITOR -- insert product name from Step 1b].
You recently started using this new product. You are in some stage of migration:
Phase 1 tickets are written when you still have the old tool open -- lower stakes because
you can fall back. Phase 3 tickets are written when you have committed to the new tool
and cannot fall back -- higher stakes because you are blocked.

Do not write "the user", "they", "the SRE", "the PM", "the engineer",
or any named-role title referring to yourself in third person.

Prohibited verb-subject forms: "the SRE ran", "the PM reviewed", "the engineer observed",
"the C-07 clicked", "the Support agent opened", or any construction where a role title
precedes a verb.

**Every action in this ticket was taken by "I". Every reference to the old tool
uses its product name, not a pronoun or generic description.**

---

## STEP 4 -- VOCABULARY PRE-COMMITMENT TABLE

Competitor in scope: [write the product name from Step 1b here -- do not write "the tool",
"my old system", or any alias. This name must appear verbatim in every Phase 1 and Phase 3
ticket body in Step 5.]

Before filling any severity cell, complete both required items below.
Do not fill any cell in the table until both items are written:

Required item 1 -- INFERENCE RULE (confirmed):
[restate the directional rule from your Step 2C paraphrase in your own words]

Required item 2 -- Verbatim from 2C:
[copy your exact first sentence from the INFERENCE RULE (stated) block in Step 2C --
word for word, do not paraphrase]

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

**Lock vocabulary values here. Full card bodies follow in Step 5.**

---

## STEP 4B -- COLLECTIVE DISTRIBUTION AUDIT

Audit five constraints before writing any card body:

1. **Phase distribution** -- at least two Phase 1 rows and one Phase 3 row.
2. **Category spread** -- at least three distinct category values.
3. **Volume distribution** -- all three volume levels present.
4. **Phase-character compliance** -- each row's volume and severity match Step 2 ranges.
5. **Inference-rule compliance** -- apply the INFERENCE RULE confirmed above Step 4:
   - Scan Phase 1 rows: flag any P0 or P1 assignment on a non-outage ticket.
   - Scan Phase 3 rows: flag any P3 assignment on a blocking ticket.
   - State PASS if no violations; FAIL and name the row and correction if any found.

State PASS or FAIL per constraint.
**If any fails, correct the table and re-run. Name the correction.**

---

## STEP 5 -- FULL CARD BODIES

For each row in the summary table:

```
Ticket ID: [T-NN]
Title: [descriptive title]
Category: [must match Step 4 exactly]
Persona: [must match Step 4 exactly]
Volume: [must match Step 4 exactly]
Severity: [must match Step 4 exactly]

Body:
[You ARE this persona. You previously used [INERTIA COMPETITOR -- product name].
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
```

---

## STEP 6 -- CROSS-TICKET PATTERNS

For each pattern, use this flat field structure with no parent "Consequence:" container:

```
Pattern name: [short name]
Tickets affected: [T-NN, T-NN, ...]
Root cause: [one sentence]

Consequence -- Affected segment:
Prohibited: "users in general", "the team", or any unnamed group.
[Named role or cohort tied specifically to this pattern]

Consequence -- Day-90 scenario:
Prohibited: "this will cause confusion" or any non-pattern-specific event.
[One specific event that occurs if this pattern is not addressed by Day 90]

Consequence -- Adoption cost:
Prohibited: generic friction not specific to this cohort.
[One sentence quantifying the friction for the named segment]
```

If a pattern involves migration from the inertia competitor, name the competitor
in the root cause or consequence fields.

---

## STEP 7 -- GAP ANALYSIS

### Doc Gaps
[At least one documentation gap.]

### Design Gaps
[At least one design gap.]

### Operational Gaps
[At least one operational gap.]

### Switching-Friction Gaps
Dedicated sub-section for migration barriers only. NOT absorbed into the above three
sections. Minimum two entries required.

Before writing any entry, state:

```
SWITCHING-FRICTION COUNT: [N -- minimum 2]
Migrating from (product name): [product name from Step 1b -- verbatim]
```

Do not write any entry until this count and product name are declared.

Use this exact 4-field format for every entry:

```
Switching-friction gap: [short name]
Migrating from: [product name from Step 1b -- verbatim, grep-checkable]
Expected behavior: [one sentence -- what users expected, based on the competitor's behavior]
Actual behavior: [one sentence -- what this product actually does or fails to do]
Migration impact: [one sentence -- what users must change, lose, or manually replicate]
```

Rules:
- `Migrating from:` MUST contain the product name from Step 1b verbatim.
  Prohibited: `Migrating from: existing tool`, `Migrating from: legacy workflow`.
- `Expected behavior:` and `Actual behavior:` define the behavior delta --
  they describe the same capability from two perspectives.
- Every entry must be independently enumerable: a reader scanning only this sub-section
  must be able to identify the competitor, the behavior delta, and the migration cost
  without reading any other part of the output.

### Pre-Launch Priority
Name the single gap to close first. Tie to specific ticket IDs, severity, and volume.
State whether it reduces switching-friction for inertia-competitor migrants.

---

## STEP 8 -- DUAL-PASS VERIFICATION

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
1. Confirm: **"No gap from the Gap Analysis -- including switching-friction gaps --
   is absent from this table."**
2. Confirm: **"The inertia competitor product name appears in at least two
   STATUS QUO element cells."**

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 -- Properties Verify + Inference Audit

**PART A -- Frontmatter Verify**

Confirm the summary table from Step 4 matches every Ticket ID, Phase, Category,
Persona, Volume, and Severity in the full card bodies from Step 5.
State: **"All Step 4 values match Step 5 card bodies."**

**PART B -- Property Checks**

1. **Tool-name fidelity** -- product name from Step 1b appears verbatim in Step 1b,
   at least two card bodies, and at least one `Migrating from:` field.
   State: **"[PRODUCT NAME] in Step 1b: YES. Card bodies: T-NN, T-NN (minimum).
   Migrating from: field: YES."**

2. **Phase-differentiated templates** -- at least two Phase 1 bodies contain the
   Phase 1 template from Step 2B, and at least one Phase 3 body contains the Phase 3 template.
   State: **"Phase 1 template in: T-NN, T-NN. Phase 3 template in: T-NN."**

3. **Switching-friction 4-field format** -- every entry in the Switching-Friction Gaps
   sub-section contains all four fields. Scan each entry for: Migrating from, Expected
   behavior, Actual behavior, Migration impact.
   State: **"All four fields present in all entries: YES / NO. Missing: [field list or NONE]."**

4. **Switching-friction count match** -- the number of entries in the Switching-Friction Gaps
   sub-section matches the SWITCHING-FRICTION COUNT declared before the entries in Step 7.
   State: **"SWITCHING-FRICTION COUNT declared: [N]. Entries in sub-section: [N actual].
   Count match: YES / NO."**
   If NO: name and write the missing entry before finalizing.

**PART C -- Inference Audit**

**Sub-check 1: Phase-Architecture Severity Compliance**

Scan Phase 1 rows in the vocabulary table (Step 4):
- List every Phase 1 ticket assigned P0 or P1.
- For each, fill a Phase 1 EXCEPTION SIGN-OFF BLOCK:

```
EXCEPTION SIGN-OFF (Phase 1 -- fallback available):
Ticket ID: [T-NN]
Phase: 1
Fallback status: Inertia competitor still in active use (fallback available)
Assigned severity: [P0 or P1]
Grounds: [outage-level? YES / NO -- only an outage justifies P0/P1 when fallback exists]
Paraphrase clause: [copy the exact Phase 1 clause from your INFERENCE RULE (stated) at
  Step 2C verbatim -- do not paraphrase, do not summarize, copy it word-for-word]
Disposition: [VALID EXCEPTION -- reason | VIOLATION -- corrected to P2/P3]
```

If no Phase 1 P0/P1 assignments exist, state:
**"No Phase 1 P0/P1 exceptions. Phase 1 lifecycle: fallback available (inertia competitor
in active use). Governing paraphrase clause: [copy the exact Phase 1 clause from your
INFERENCE RULE (stated) at Step 2C verbatim -- do not paraphrase]."**

Scan Phase 3 rows in the vocabulary table (Step 4):
- List every Phase 3 ticket assigned P3.
- For each, fill a Phase 3 EXCEPTION SIGN-OFF BLOCK:

```
EXCEPTION SIGN-OFF (Phase 3 -- no fallback):
Ticket ID: [T-NN]
Phase: 3
Fallback status: Inertia competitor out of daily workflow (no fallback)
Assigned severity: P3
Grounds: [non-blocking issue? YES / NO -- P3 only valid if user is not blocked]
Paraphrase clause: [copy the exact Phase 3 clause from your INFERENCE RULE (stated) at
  Step 2C verbatim -- do not paraphrase, do not summarize, copy it word-for-word]
Disposition: [VALID EXCEPTION -- reason | VIOLATION -- corrected to P1/P0]
```

If no Phase 3 P3 assignments exist, state:
**"No Phase 3 P3 exceptions. Phase 3 lifecycle: no fallback (inertia competitor out of
daily workflow). Governing paraphrase clause: [copy the exact Phase 3 clause from your
INFERENCE RULE (stated) at Step 2C verbatim -- do not paraphrase]."**

Confirm the INFERENCE RULE stated in Step 2C and confirmed at Step 4 has been
applied consistently. Compare the paraphrase from Step 2C against the audit results:
State: **"INFERENCE RULE paraphrase (Step 2C): [quote first 10 words of your Step 2C paraphrase].
Verbatim anchor at Step 4: YES.
Verbatim instruction in exception block Paraphrase clause: YES. [Governing clause copied
word-for-word from Step 2C; no paraphrase permitted.]
Audit result -- Phase 1 P2/P3 compliance: [PASS/FAIL].
Audit result -- Phase 3 P0/P1 compliance: [PASS/FAIL].
Paraphrase consistent with audit results: YES / NO."**

**Sub-check 2: Switching-Friction Sub-Section Field Completeness**

Confirm the Switching-Friction Gaps sub-section from Step 7 is present.
Scan every entry for the `Migrating from:` field:
- List each entry's `Migrating from:` value.
- Flag any entry where the value does not contain the product name from Step 1b verbatim.
State: **"Switching-Friction Gaps sub-section present: YES. Migrating from: fields --
[entry 1: value | entry 2: value | ...]. All fields populated with product name
verbatim: YES / NO. Missing or non-verbatim entries: [list or NONE]."**

State final: **"All Step 4 values match Step 5. Exception sign-offs complete.
Sub-checks 1 and 2 verified. Paraphrase consistency confirmed."**
Name and correct any issue before finalizing.
```

---

## V-04: Combined (V-01 + V-02) -- No-Exception Triple-Clause + Phase Distribution Pre-Commitment

**Axes combined**: V-01's triple-clause upgrade to both no-exception confirmation statements (Phase 1 and Phase 3) with V-02's three-item phase distribution pre-commitment gate at Step 4. The two changes operate in distinct structural slots: V-01 modifies two sentences in Pass 2C (the no-exception confirmation text for Phase 1 and Phase 3); V-02 adds a Required item 1 block to Step 4's pre-commitment gate and adds constraint 0 to Step 4B. There is no instruction overlap between the two axes. All other mechanisms from V-04 R14 are preserved.

**Hypothesis**: V-01 closes the no-exception condensation path by adding "do not summarize" where V-04 R14 carries only "do not paraphrase." V-02 closes the phase distribution post-hoc correction path by adding a pre-fill phase count contract. Both failure modes are structurally independent: a model could satisfy V-01 without V-02 (triple-clause in no-exception path, but phase distribution still planned post-hoc) and vice versa. The combination tests whether both C-44 and C-45 candidates are achievable simultaneously without the additional instruction weight causing interference. The cell-level gate "Do not fill any cell in the table until all three items are written" (V-02's form) preserves C-42 compliance: the unit of prohibition is the individual cell, same as V-04 R14.

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

```
INERTIA COMPETITOR: [product name]
Prohibited: "existing tooling", "their current system", "legacy workflow",
or any phrase that does not produce a grep-checkable product name string.
```

This product name will be embedded in the performance mode declaration in Step 3,
appear verbatim in every Phase 1 and Phase 3 ticket body, and appear verbatim in
the `Migrating from:` field of every switching-friction gap. Record it once here.

**1c. Adoption-curve context**
Note where the user population sits: early (dual-tool phase) or late (parity-gap phase).
This drives phase distribution in Step 4.

---

## STEP 2 -- PHASE MAP TABLE

| Phase | Window | Expected severity range | Expected volume character |
|-------|--------|------------------------|--------------------------|
| Phase 1 | Day 0-30 | P2/P3 | high |
| Phase 2 | Day 31-60 | P1/P2 | medium |
| Phase 3 | Day 61-90 | P0/P1 | medium/low |

---

## STEP 2B -- PHASE BODY TEMPLATE TABLE

Replace [INERTIA COMPETITOR] with the product name from Step 1b before writing this table.

| Phase | Adoption stance | Pre-printed template sentence |
|-------|----------------|-------------------------------|
| Phase 1 | Dual-tool tension | "I still have [INERTIA COMPETITOR] open in another tab while working through this -- I keep switching back to check how it handled [specific scenario]." |
| Phase 3 | Parity gap | "In [INERTIA COMPETITOR] I could [specific action] without leaving this screen; here I cannot find a way to do it at all." |

Instructions:
- Phase 1 bodies: include the Phase 1 sentence with all placeholders filled concretely.
- Phase 3 bodies: include the Phase 3 sentence with all placeholders filled concretely.
- Phase 2 bodies: reference the competitor where it naturally fits; no template required.

---

## STEP 2C -- PHASE-SEVERITY INFERENCE RULE

Do not proceed to Step 3 until this step is complete.

**The directional rule:**

Phase 1 tickets (Day 0-30) MUST be P2 or P3 for non-outage issues.
- Reason: The inertia competitor is still available. Adoption friction is expected.
  A workaround exists -- return to the competitor and complete the task there.
  Lower severity reflects that the user is not blocked; they are learning.

Phase 3 tickets (Day 61-90) that block task completion MUST be P1 or P0.
- Reason: Phase 3 users have committed to the new product. The inertia competitor
  is no longer in their daily workflow. Parity gaps that prevent task completion
  have no fallback path. Higher severity reflects that the user is blocked with
  no alternative.

**Violation conditions (apply in Steps 4, 4B, and Pass 2 INFERENCE AUDIT):**
- Phase 1 P0 or P1 on a non-outage ticket: violation -- correct to P2/P3.
- Phase 3 P3 on a ticket where the user cannot complete a task: violation -- correct to P1/P0.

**Required confirmation before proceeding:**
State the inference rule in your own words as a named constraint. This paraphrase will
be recalled at Step 4 and verified in Pass 2 Part C. Write a genuine restatement --
not a copy of the rule above:

```
INFERENCE RULE (stated): [your paraphrase of the directional rule above]
Applied in: Steps 4, 4B, and Pass 2 INFERENCE AUDIT
```

Do not proceed to Step 3 until this block is filled with your own-words paraphrase.

---

## STEP 3 -- PERFORMANCE MODE DECLARATION

**You ARE the persona named on each ticket card.**

Your previous primary workflow used [INERTIA COMPETITOR -- insert product name from Step 1b].
You recently started using this new product. You are in some stage of migration:
Phase 1 tickets are written when you still have the old tool open -- lower stakes because
you can fall back. Phase 3 tickets are written when you have committed to the new tool
and cannot fall back -- higher stakes because you are blocked.

Do not write "the user", "they", "the SRE", "the PM", "the engineer",
or any named-role title referring to yourself in third person.

Prohibited verb-subject forms: "the SRE ran", "the PM reviewed", "the engineer observed",
"the C-07 clicked", "the Support agent opened", or any construction where a role title
precedes a verb.

**Every action in this ticket was taken by "I". Every reference to the old tool
uses its product name, not a pronoun or generic description.**

---

## STEP 4 -- VOCABULARY PRE-COMMITMENT TABLE

Competitor in scope: [write the product name from Step 1b here -- do not write "the tool",
"my old system", or any alias. This name must appear verbatim in every Phase 1 and Phase 3
ticket body in Step 5.]

Before filling any cell in the table, complete all three required items below.
Do not fill any cell in the table until all three items are written:

Required item 1 -- PHASE DISTRIBUTION (committed):
```
Phase 1 tickets (Day 0-30): [N -- minimum 2]
Phase 2 tickets (Day 31-60): [N]
Phase 3 tickets (Day 61-90): [N -- minimum 1]
Total: [must equal 8]
```
This distribution will be verified against the table in Step 4B constraint 0.

Required item 2 -- INFERENCE RULE (confirmed):
[restate the directional rule from your Step 2C paraphrase in your own words]

Required item 3 -- Verbatim from 2C:
[copy your exact first sentence from the INFERENCE RULE (stated) block in Step 2C --
word for word, do not paraphrase]

Confirmation: the inference rule applies to every severity assignment in the table below.

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

**Lock vocabulary values here. Full card bodies follow in Step 5.**

---

## STEP 4B -- COLLECTIVE DISTRIBUTION AUDIT

Audit six constraints before writing any card body:

0. **Phase pre-commitment match** -- the phase counts committed in Required item 1 above
   match the Phase column counts in this table.
   State: **"Phase 1: [N committed] planned / [N actual] in table -- MATCH/MISMATCH.
   Phase 2: [N committed] planned / [N actual] in table -- MATCH/MISMATCH.
   Phase 3: [N committed] planned / [N actual] in table -- MATCH/MISMATCH."**
   If MISMATCH: name which phase is off and correct the table before proceeding.

1. **Phase distribution** -- at least two Phase 1 rows and one Phase 3 row.
2. **Category spread** -- at least three distinct category values.
3. **Volume distribution** -- all three volume levels present.
4. **Phase-character compliance** -- each row's volume and severity match Step 2 ranges.
5. **Inference-rule compliance** -- apply the INFERENCE RULE confirmed above Step 4:
   - Scan Phase 1 rows: flag any P0 or P1 assignment on a non-outage ticket.
   - Scan Phase 3 rows: flag any P3 assignment on a blocking ticket.
   - State PASS if no violations; FAIL and name the row and correction if any found.

State PASS or FAIL per constraint.
**If any fails, correct the table and re-run. Name the correction.**

---

## STEP 5 -- FULL CARD BODIES

For each row in the summary table:

```
Ticket ID: [T-NN]
Title: [descriptive title]
Category: [must match Step 4 exactly]
Persona: [must match Step 4 exactly]
Volume: [must match Step 4 exactly]
Severity: [must match Step 4 exactly]

Body:
[You ARE this persona. You previously used [INERTIA COMPETITOR -- product name].
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
```

---

## STEP 6 -- CROSS-TICKET PATTERNS

For each pattern, use this flat field structure with no parent "Consequence:" container:

```
Pattern name: [short name]
Tickets affected: [T-NN, T-NN, ...]
Root cause: [one sentence]

Consequence -- Affected segment:
Prohibited: "users in general", "the team", or any unnamed group.
[Named role or cohort tied specifically to this pattern]

Consequence -- Day-90 scenario:
Prohibited: "this will cause confusion" or any non-pattern-specific event.
[One specific event that occurs if this pattern is not addressed by Day 90]

Consequence -- Adoption cost:
Prohibited: generic friction not specific to this cohort.
[One sentence quantifying the friction for the named segment]
```

If a pattern involves migration from the inertia competitor, name the competitor
in the root cause or consequence fields.

---

## STEP 7 -- GAP ANALYSIS

### Doc Gaps
[At least one documentation gap.]

### Design Gaps
[At least one design gap.]

### Operational Gaps
[At least one operational gap.]

### Switching-Friction Gaps
Dedicated sub-section for migration barriers only. NOT absorbed into the above three
sections. At least one entry required. At least two are recommended.

Use this exact 4-field format for every entry:

```
Switching-friction gap: [short name]
Migrating from: [product name from Step 1b -- verbatim, grep-checkable]
Expected behavior: [one sentence -- what users expected, based on the competitor's behavior]
Actual behavior: [one sentence -- what this product actually does or fails to do]
Migration impact: [one sentence -- what users must change, lose, or manually replicate]
```

Rules:
- `Migrating from:` MUST contain the product name from Step 1b verbatim.
  Prohibited: `Migrating from: existing tool`, `Migrating from: legacy workflow`.
- `Expected behavior:` and `Actual behavior:` define the behavior delta --
  they describe the same capability from two perspectives.
- Every entry must be independently enumerable: a reader scanning only this sub-section
  must be able to identify the competitor, the behavior delta, and the migration cost
  without reading any other part of the output.

### Pre-Launch Priority
Name the single gap to close first. Tie to specific ticket IDs, severity, and volume.
State whether it reduces switching-friction for inertia-competitor migrants.

---

## STEP 8 -- DUAL-PASS VERIFICATION

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
1. Confirm: **"No gap from the Gap Analysis -- including switching-friction gaps --
   is absent from this table."**
2. Confirm: **"The inertia competitor product name appears in at least two
   STATUS QUO element cells."**

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 -- Properties Verify + Inference Audit

**PART A -- Frontmatter Verify**

Confirm the summary table from Step 4 matches every Ticket ID, Phase, Category,
Persona, Volume, and Severity in the full card bodies from Step 5.
State: **"All Step 4 values match Step 5 card bodies."**

**PART B -- Property Checks**

1. **Tool-name fidelity** -- product name from Step 1b appears verbatim in Step 1b,
   at least two card bodies, and at least one `Migrating from:` field.
   State: **"[PRODUCT NAME] in Step 1b: YES. Card bodies: T-NN, T-NN (minimum).
   Migrating from: field: YES."**

2. **Phase-differentiated templates** -- at least two Phase 1 bodies contain the
   Phase 1 template from Step 2B, and at least one Phase 3 body contains the Phase 3 template.
   State: **"Phase 1 template in: T-NN, T-NN. Phase 3 template in: T-NN."**

3. **Switching-friction 4-field format** -- every entry in the Switching-Friction Gaps
   sub-section contains all four fields. Scan each entry for: Migrating from, Expected
   behavior, Actual behavior, Migration impact.
   State: **"All four fields present in all entries: YES / NO. Missing: [field list or NONE]."**

**PART C -- Inference Audit**

**Sub-check 1: Phase-Architecture Severity Compliance**

Scan Phase 1 rows in the vocabulary table (Step 4):
- List every Phase 1 ticket assigned P0 or P1.
- For each, fill a Phase 1 EXCEPTION SIGN-OFF BLOCK:

```
EXCEPTION SIGN-OFF (Phase 1 -- fallback available):
Ticket ID: [T-NN]
Phase: 1
Fallback status: Inertia competitor still in active use (fallback available)
Assigned severity: [P0 or P1]
Grounds: [outage-level? YES / NO -- only an outage justifies P0/P1 when fallback exists]
Paraphrase clause: [copy the exact Phase 1 clause from your INFERENCE RULE (stated) at
  Step 2C verbatim -- do not paraphrase, do not summarize, copy it word-for-word]
Disposition: [VALID EXCEPTION -- reason | VIOLATION -- corrected to P2/P3]
```

If no Phase 1 P0/P1 assignments exist, state:
**"No Phase 1 P0/P1 exceptions. Phase 1 lifecycle: fallback available (inertia competitor
in active use). Governing paraphrase clause: [copy the exact Phase 1 clause from your
INFERENCE RULE (stated) at Step 2C -- do not paraphrase, do not summarize, copy it
verbatim word-for-word]."**

Scan Phase 3 rows in the vocabulary table (Step 4):
- List every Phase 3 ticket assigned P3.
- For each, fill a Phase 3 EXCEPTION SIGN-OFF BLOCK:

```
EXCEPTION SIGN-OFF (Phase 3 -- no fallback):
Ticket ID: [T-NN]
Phase: 3
Fallback status: Inertia competitor out of daily workflow (no fallback)
Assigned severity: P3
Grounds: [non-blocking issue? YES / NO -- P3 only valid if user is not blocked]
Paraphrase clause: [copy the exact Phase 3 clause from your INFERENCE RULE (stated) at
  Step 2C verbatim -- do not paraphrase, do not summarize, copy it word-for-word]
Disposition: [VALID EXCEPTION -- reason | VIOLATION -- corrected to P1/P0]
```

If no Phase 3 P3 assignments exist, state:
**"No Phase 3 P3 exceptions. Phase 3 lifecycle: no fallback (inertia competitor out of
daily workflow). Governing paraphrase clause: [copy the exact Phase 3 clause from your
INFERENCE RULE (stated) at Step 2C -- do not paraphrase, do not summarize, copy it
verbatim word-for-word]."**

Confirm the INFERENCE RULE stated in Step 2C and confirmed at Step 4 has been
applied consistently. Compare the paraphrase from Step 2C against the audit results:
State: **"INFERENCE RULE paraphrase (Step 2C): [quote first 10 words of your Step 2C paraphrase].
Verbatim anchor at Step 4: YES.
Verbatim instruction in exception block Paraphrase clause: YES. [Governing clause copied
word-for-word from Step 2C; no paraphrase permitted.]
Audit result -- Phase 1 P2/P3 compliance: [PASS/FAIL].
Audit result -- Phase 3 P0/P1 compliance: [PASS/FAIL].
Paraphrase consistent with audit results: YES / NO."**

**Sub-check 2: Switching-Friction Sub-Section Field Completeness**

Confirm the Switching-Friction Gaps sub-section from Step 7 is present.
Scan every entry for the `Migrating from:` field:
- List each entry's `Migrating from:` value.
- Flag any entry where the value does not contain the product name from Step 1b verbatim.
State: **"Switching-Friction Gaps sub-section present: YES. Migrating from: fields --
[entry 1: value | entry 2: value | ...]. All fields populated with product name
verbatim: YES / NO. Missing or non-verbatim entries: [list or NONE]."**

State final: **"All Step 4 values match Step 5. Exception sign-offs complete.
Sub-checks 1 and 2 verified. Paraphrase consistency confirmed."**
Name and correct any issue before finalizing.
```

---

## V-05: Full Synthesis (V-01 + V-02 + V-03) -- All Three New Axes

**Axes combined**: All three R15 single-axis changes simultaneously applied to V-04 R14: (1) V-01's no-exception path triple-clause upgrade; (2) V-02's phase distribution pre-commitment gate at Step 4 (three required items, cell-level gate, constraint 0 at Step 4B); (3) V-03's switching-friction minimum count gate with pre-count declaration and count-match check in Pass 2B. All three axes operate in distinct structural slots with no overlap. All other mechanisms from V-04 R14 are preserved.

**Hypothesis**: All three axes are structurally independent: V-01 modifies two sentence-level no-exception confirmations; V-02 adds a pre-fill planning block and a distribution audit step; V-03 modifies the gap sub-section header and adds a count check. No single instruction in any axis touches the same structural slot as another. The full synthesis tests whether all three C-44/C-45/C-46 candidates are simultaneously achievable and whether the additional instruction weight (three more required items across three different steps) degrades performance on prior criteria. If V-05 reaches ceiling on all forty-six criteria, the three new candidates can be codified in rubric v15. If V-05 shows degradation on any prior criterion, the degraded criterion identifies which axis is load-bearing for that interference.

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

```
INERTIA COMPETITOR: [product name]
Prohibited: "existing tooling", "their current system", "legacy workflow",
or any phrase that does not produce a grep-checkable product name string.
```

This product name will be embedded in the performance mode declaration in Step 3,
appear verbatim in every Phase 1 and Phase 3 ticket body, and appear verbatim in
the `Migrating from:` field of every switching-friction gap. Record it once here.

**1c. Adoption-curve context**
Note where the user population sits: early (dual-tool phase) or late (parity-gap phase).
This drives phase distribution in Step 4.

---

## STEP 2 -- PHASE MAP TABLE

| Phase | Window | Expected severity range | Expected volume character |
|-------|--------|------------------------|--------------------------|
| Phase 1 | Day 0-30 | P2/P3 | high |
| Phase 2 | Day 31-60 | P1/P2 | medium |
| Phase 3 | Day 61-90 | P0/P1 | medium/low |

---

## STEP 2B -- PHASE BODY TEMPLATE TABLE

Replace [INERTIA COMPETITOR] with the product name from Step 1b before writing this table.

| Phase | Adoption stance | Pre-printed template sentence |
|-------|----------------|-------------------------------|
| Phase 1 | Dual-tool tension | "I still have [INERTIA COMPETITOR] open in another tab while working through this -- I keep switching back to check how it handled [specific scenario]." |
| Phase 3 | Parity gap | "In [INERTIA COMPETITOR] I could [specific action] without leaving this screen; here I cannot find a way to do it at all." |

Instructions:
- Phase 1 bodies: include the Phase 1 sentence with all placeholders filled concretely.
- Phase 3 bodies: include the Phase 3 sentence with all placeholders filled concretely.
- Phase 2 bodies: reference the competitor where it naturally fits; no template required.

---

## STEP 2C -- PHASE-SEVERITY INFERENCE RULE

Do not proceed to Step 3 until this step is complete.

**The directional rule:**

Phase 1 tickets (Day 0-30) MUST be P2 or P3 for non-outage issues.
- Reason: The inertia competitor is still available. Adoption friction is expected.
  A workaround exists -- return to the competitor and complete the task there.
  Lower severity reflects that the user is not blocked; they are learning.

Phase 3 tickets (Day 61-90) that block task completion MUST be P1 or P0.
- Reason: Phase 3 users have committed to the new product. The inertia competitor
  is no longer in their daily workflow. Parity gaps that prevent task completion
  have no fallback path. Higher severity reflects that the user is blocked with
  no alternative.

**Violation conditions (apply in Steps 4, 4B, and Pass 2 INFERENCE AUDIT):**
- Phase 1 P0 or P1 on a non-outage ticket: violation -- correct to P2/P3.
- Phase 3 P3 on a ticket where the user cannot complete a task: violation -- correct to P1/P0.

**Required confirmation before proceeding:**
State the inference rule in your own words as a named constraint. This paraphrase will
be recalled at Step 4 and verified in Pass 2 Part C. Write a genuine restatement --
not a copy of the rule above:

```
INFERENCE RULE (stated): [your paraphrase of the directional rule above]
Applied in: Steps 4, 4B, and Pass 2 INFERENCE AUDIT
```

Do not proceed to Step 3 until this block is filled with your own-words paraphrase.

---

## STEP 3 -- PERFORMANCE MODE DECLARATION

**You ARE the persona named on each ticket card.**

Your previous primary workflow used [INERTIA COMPETITOR -- insert product name from Step 1b].
You recently started using this new product. You are in some stage of migration:
Phase 1 tickets are written when you still have the old tool open -- lower stakes because
you can fall back. Phase 3 tickets are written when you have committed to the new tool
and cannot fall back -- higher stakes because you are blocked.

Do not write "the user", "they", "the SRE", "the PM", "the engineer",
or any named-role title referring to yourself in third person.

Prohibited verb-subject forms: "the SRE ran", "the PM reviewed", "the engineer observed",
"the C-07 clicked", "the Support agent opened", or any construction where a role title
precedes a verb.

**Every action in this ticket was taken by "I". Every reference to the old tool
uses its product name, not a pronoun or generic description.**

---

## STEP 4 -- VOCABULARY PRE-COMMITMENT TABLE

Competitor in scope: [write the product name from Step 1b here -- do not write "the tool",
"my old system", or any alias. This name must appear verbatim in every Phase 1 and Phase 3
ticket body in Step 5.]

Before filling any cell in the table, complete all three required items below.
Do not fill any cell in the table until all three items are written:

Required item 1 -- PHASE DISTRIBUTION (committed):
```
Phase 1 tickets (Day 0-30): [N -- minimum 2]
Phase 2 tickets (Day 31-60): [N]
Phase 3 tickets (Day 61-90): [N -- minimum 1]
Total: [must equal 8]
```
This distribution will be verified against the table in Step 4B constraint 0.

Required item 2 -- INFERENCE RULE (confirmed):
[restate the directional rule from your Step 2C paraphrase in your own words]

Required item 3 -- Verbatim from 2C:
[copy your exact first sentence from the INFERENCE RULE (stated) block in Step 2C --
word for word, do not paraphrase]

Confirmation: the inference rule applies to every severity assignment in the table below.

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

**Lock vocabulary values here. Full card bodies follow in Step 5.**

---

## STEP 4B -- COLLECTIVE DISTRIBUTION AUDIT

Audit six constraints before writing any card body:

0. **Phase pre-commitment match** -- the phase counts committed in Required item 1 above
   match the Phase column counts in this table.
   State: **"Phase 1: [N committed] planned / [N actual] in table -- MATCH/MISMATCH.
   Phase 2: [N committed] planned / [N actual] in table -- MATCH/MISMATCH.
   Phase 3: [N committed] planned / [N actual] in table -- MATCH/MISMATCH."**
   If MISMATCH: name which phase is off and correct the table before proceeding.

1. **Phase distribution** -- at least two Phase 1 rows and one Phase 3 row.
2. **Category spread** -- at least three distinct category values.
3. **Volume distribution** -- all three volume levels present.
4. **Phase-character compliance** -- each row's volume and severity match Step 2 ranges.
5. **Inference-rule compliance** -- apply the INFERENCE RULE confirmed above Step 4:
   - Scan Phase 1 rows: flag any P0 or P1 assignment on a non-outage ticket.
   - Scan Phase 3 rows: flag any P3 assignment on a blocking ticket.
   - State PASS if no violations; FAIL and name the row and correction if any found.

State PASS or FAIL per constraint.
**If any fails, correct the table and re-run. Name the correction.**

---

## STEP 5 -- FULL CARD BODIES

For each row in the summary table:

```
Ticket ID: [T-NN]
Title: [descriptive title]
Category: [must match Step 4 exactly]
Persona: [must match Step 4 exactly]
Volume: [must match Step 4 exactly]
Severity: [must match Step 4 exactly]

Body:
[You ARE this persona. You previously used [INERTIA COMPETITOR -- product name].
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
```

---

## STEP 6 -- CROSS-TICKET PATTERNS

For each pattern, use this flat field structure with no parent "Consequence:" container:

```
Pattern name: [short name]
Tickets affected: [T-NN, T-NN, ...]
Root cause: [one sentence]

Consequence -- Affected segment:
Prohibited: "users in general", "the team", or any unnamed group.
[Named role or cohort tied specifically to this pattern]

Consequence -- Day-90 scenario:
Prohibited: "this will cause confusion" or any non-pattern-specific event.
[One specific event that occurs if this pattern is not addressed by Day 90]

Consequence -- Adoption cost:
Prohibited: generic friction not specific to this cohort.
[One sentence quantifying the friction for the named segment]
```

If a pattern involves migration from the inertia competitor, name the competitor
in the root cause or consequence fields.

---

## STEP 7 -- GAP ANALYSIS

### Doc Gaps
[At least one documentation gap.]

### Design Gaps
[At least one design gap.]

### Operational Gaps
[At least one operational gap.]

### Switching-Friction Gaps
Dedicated sub-section for migration barriers only. NOT absorbed into the above three
sections. Minimum two entries required.

Before writing any entry, state:

```
SWITCHING-FRICTION COUNT: [N -- minimum 2]
Migrating from (product name): [product name from Step 1b -- verbatim]
```

Do not write any entry until this count and product name are declared.

Use this exact 4-field format for every entry:

```
Switching-friction gap: [short name]
Migrating from: [product name from Step 1b -- verbatim, grep-checkable]
Expected behavior: [one sentence -- what users expected, based on the competitor's behavior]
Actual behavior: [one sentence -- what this product actually does or fails to do]
Migration impact: [one sentence -- what users must change, lose, or manually replicate]
```

Rules:
- `Migrating from:` MUST contain the product name from Step 1b verbatim.
  Prohibited: `Migrating from: existing tool`, `Migrating from: legacy workflow`.
- `Expected behavior:` and `Actual behavior:` define the behavior delta --
  they describe the same capability from two perspectives.
- Every entry must be independently enumerable: a reader scanning only this sub-section
  must be able to identify the competitor, the behavior delta, and the migration cost
  without reading any other part of the output.

### Pre-Launch Priority
Name the single gap to close first. Tie to specific ticket IDs, severity, and volume.
State whether it reduces switching-friction for inertia-competitor migrants.

---

## STEP 8 -- DUAL-PASS VERIFICATION

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
1. Confirm: **"No gap from the Gap Analysis -- including switching-friction gaps --
   is absent from this table."**
2. Confirm: **"The inertia competitor product name appears in at least two
   STATUS QUO element cells."**

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 -- Properties Verify + Inference Audit

**PART A -- Frontmatter Verify**

Confirm the summary table from Step 4 matches every Ticket ID, Phase, Category,
Persona, Volume, and Severity in the full card bodies from Step 5.
State: **"All Step 4 values match Step 5 card bodies."**

**PART B -- Property Checks**

1. **Tool-name fidelity** -- product name from Step 1b appears verbatim in Step 1b,
   at least two card bodies, and at least one `Migrating from:` field.
   State: **"[PRODUCT NAME] in Step 1b: YES. Card bodies: T-NN, T-NN (minimum).
   Migrating from: field: YES."**

2. **Phase-differentiated templates** -- at least two Phase 1 bodies contain the
   Phase 1 template from Step 2B, and at least one Phase 3 body contains the Phase 3 template.
   State: **"Phase 1 template in: T-NN, T-NN. Phase 3 template in: T-NN."**

3. **Switching-friction 4-field format** -- every entry in the Switching-Friction Gaps
   sub-section contains all four fields. Scan each entry for: Migrating from, Expected
   behavior, Actual behavior, Migration impact.
   State: **"All four fields present in all entries: YES / NO. Missing: [field list or NONE]."**

4. **Switching-friction count match** -- the number of entries in the Switching-Friction Gaps
   sub-section matches the SWITCHING-FRICTION COUNT declared before the entries in Step 7.
   State: **"SWITCHING-FRICTION COUNT declared: [N]. Entries in sub-section: [N actual].
   Count match: YES / NO."**
   If NO: name and write the missing entry before finalizing.

**PART C -- Inference Audit**

**Sub-check 1: Phase-Architecture Severity Compliance**

Scan Phase 1 rows in the vocabulary table (Step 4):
- List every Phase 1 ticket assigned P0 or P1.
- For each, fill a Phase 1 EXCEPTION SIGN-OFF BLOCK:

```
EXCEPTION SIGN-OFF (Phase 1 -- fallback available):
Ticket ID: [T-NN]
Phase: 1
Fallback status: Inertia competitor still in active use (fallback available)
Assigned severity: [P0 or P1]
Grounds: [outage-level? YES / NO -- only an outage justifies P0/P1 when fallback exists]
Paraphrase clause: [copy the exact Phase 1 clause from your INFERENCE RULE (stated) at
  Step 2C verbatim -- do not paraphrase, do not summarize, copy it word-for-word]
Disposition: [VALID EXCEPTION -- reason | VIOLATION -- corrected to P2/P3]
```

If no Phase 1 P0/P1 assignments exist, state:
**"No Phase 1 P0/P1 exceptions. Phase 1 lifecycle: fallback available (inertia competitor
in active use). Governing paraphrase clause: [copy the exact Phase 1 clause from your
INFERENCE RULE (stated) at Step 2C -- do not paraphrase, do not summarize, copy it
verbatim word-for-word]."**

Scan Phase 3 rows in the vocabulary table (Step 4):
- List every Phase 3 ticket assigned P3.
- For each, fill a Phase 3 EXCEPTION SIGN-OFF BLOCK:

```
EXCEPTION SIGN-OFF (Phase 3 -- no fallback):
Ticket ID: [T-NN]
Phase: 3
Fallback status: Inertia competitor out of daily workflow (no fallback)
Assigned severity: P3
Grounds: [non-blocking issue? YES / NO -- P3 only valid if user is not blocked]
Paraphrase clause: [copy the exact Phase 3 clause from your INFERENCE RULE (stated) at
  Step 2C verbatim -- do not paraphrase, do not summarize, copy it word-for-word]
Disposition: [VALID EXCEPTION -- reason | VIOLATION -- corrected to P1/P0]
```

If no Phase 3 P3 assignments exist, state:
**"No Phase 3 P3 exceptions. Phase 3 lifecycle: no fallback (inertia competitor out of
daily workflow). Governing paraphrase clause: [copy the exact Phase 3 clause from your
INFERENCE RULE (stated) at Step 2C -- do not paraphrase, do not summarize, copy it
verbatim word-for-word]."**

Confirm the INFERENCE RULE stated in Step 2C and confirmed at Step 4 has been
applied consistently. Compare the paraphrase from Step 2C against the audit results:
State: **"INFERENCE RULE paraphrase (Step 2C): [quote first 10 words of your Step 2C paraphrase].
Verbatim anchor at Step 4: YES.
Verbatim instruction in exception block Paraphrase clause: YES. [Governing clause copied
word-for-word from Step 2C; no paraphrase permitted.]
Audit result -- Phase 1 P2/P3 compliance: [PASS/FAIL].
Audit result -- Phase 3 P0/P1 compliance: [PASS/FAIL].
Paraphrase consistent with audit results: YES / NO."**

**Sub-check 2: Switching-Friction Sub-Section Field Completeness**

Confirm the Switching-Friction Gaps sub-section from Step 7 is present.
Scan every entry for the `Migrating from:` field:
- List each entry's `Migrating from:` value.
- Flag any entry where the value does not contain the product name from Step 1b verbatim.
State: **"Switching-Friction Gaps sub-section present: YES. Migrating from: fields --
[entry 1: value | entry 2: value | ...]. All fields populated with product name
verbatim: YES / NO. Missing or non-verbatim entries: [list or NONE]."**

State final: **"All Step 4 values match Step 5. Exception sign-offs complete.
Sub-checks 1 and 2 verified. Paraphrase consistency confirmed."**
Name and correct any issue before finalizing.
```
