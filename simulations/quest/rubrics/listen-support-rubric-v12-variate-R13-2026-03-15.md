# listen-support Round 13 -- Skill Body Prompt Variations

**Rubric target**: v12 (245 pts)
**New criteria in scope**: C-36 (Exception Block Paraphrase-Clause Field), C-37 (Step-4 Verbatim Anchor Field), C-38 (Dual-Field Step-4 Gate), C-39 (Step-4 Every-Assignment Scope Confirmation)
**Base**: All prior mechanisms from R12 (C-01 through C-35 at ceiling, C-36/37/38/39 split across R12 variations)

**Variation axes selected** (3 single-axis, then 2 combined):
1. **Step-4 gate structure** -- dual-field (C-37+C-38) with scope confirmation (C-39) added; exception block stays at 5-field baseline (V-01)
2. **Exception block structure** -- 6-field with Paraphrase clause (C-36); Step 4 gate stays at single-restatement baseline (V-02)
3. **Phrasing register** -- conversational/descriptive register carrying dual-field gate (C-37+C-38); no scope confirmation, no paraphrase clause (V-03)
4. **V-01 + V-02 combined** -- dual-field + scope confirmation + Paraphrase clause in exception block = all four (V-04)
5. **Full synthesis** -- all four criteria + conversational register from V-03 + inertia framing gates from R12 V-03 (V-05)

**R13 coverage matrix:**

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-36 (exception paraphrase-clause field) | -- | YES | -- | YES | YES |
| C-37 (verbatim anchor at Step 4) | YES | -- | YES | YES | YES |
| C-38 (dual-field "both lines" gate) | YES | -- | YES | YES | YES |
| C-39 (every-assignment scope confirmation) | YES | -- | -- | YES | YES |

---

## V-01: Single-Axis -- Step-4 Gate Structure (C-38 + C-39 Together)

**Axis**: Step-4 gate structure -- R12 V-01's dual-field gate (own-words + verbatim, "both lines") extended with scope confirmation. After both fields are written, the gate closes with: "Confirmation: this rule applies to every severity assignment in the table below." Exception block remains at 5-field baseline (no Paraphrase clause). Part C closing confirmation adds a "Scope confirmation at Step 4: YES" check line.

**Hypothesis**: R12 V-01 achieved C-37+C-38 but not C-39. The missing mechanism was a scope confirmation following the dual fields. The question is whether adding a third element to the gate -- a scope confirmation that follows the verbatim anchor -- degrades C-38 compliance (which requires "both lines" language referencing exactly two fields) or whether the three-element gate is parseable. C-38's pass condition requires two distinct labeled fields with "both fields/lines" instruction; the scope confirmation is not a labeled field but a declarative closure statement following the fields. V-01 tests whether dual-field+scope is structurally distinguishable from a three-field gate that might dilute the "both lines" instruction.

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

Before filling any severity cell, recall the inference rule you stated in Step 2C.
Do not fill the table until both lines are written:

```
INFERENCE RULE (confirmed): [restate the rule from your Step 2C paraphrase in your own words]
Verbatim from 2C: [quote your exact first sentence from the INFERENCE RULE (stated)
  block in Step 2C -- copy it word for word, do not paraphrase]
```

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
- For each, fill an EXCEPTION SIGN-OFF BLOCK:

```
EXCEPTION SIGN-OFF:
Ticket ID: [T-NN]
Phase: 1
Assigned severity: [P0 or P1]
Grounds: [outage-level? YES / NO]
Disposition: [VALID EXCEPTION -- reason | VIOLATION -- corrected to P2/P3]
```

If no Phase 1 P0/P1 assignments exist, state:
**"No Phase 1 P0/P1 exceptions. PASS."**

Scan Phase 3 rows in the vocabulary table (Step 4):
- List every Phase 3 ticket assigned P3.
- For each, fill an EXCEPTION SIGN-OFF BLOCK:

```
EXCEPTION SIGN-OFF:
Ticket ID: [T-NN]
Phase: 3
Assigned severity: P3
Grounds: [non-blocking issue? YES / NO]
Disposition: [VALID EXCEPTION -- reason | VIOLATION -- corrected to P1/P0]
```

If no Phase 3 P3 assignments exist, state:
**"No Phase 3 P3 exceptions. PASS."**

Confirm the INFERENCE RULE stated in Step 2C and confirmed at Step 4 has been
applied consistently. Compare the paraphrase from Step 2C against the audit results:
State: **"INFERENCE RULE paraphrase (Step 2C): [quote first 10 words of your Step 2C paraphrase].
Verbatim anchor at Step 4: YES.
Scope confirmation at Step 4: YES. [This rule applies to every severity assignment in the table.]
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

## V-02: Single-Axis -- Exception Block Structure (C-36 in Isolation)

**Axis**: Exception SIGN-OFF BLOCK structure only -- 6-field form with Paraphrase clause. Step 4 gate stays at single-restatement baseline (own-words restatement only, no verbatim anchor, no scope confirmation). The no-exception path quotes the governing paraphrase clause instead of stating only "PASS." This isolates C-36 from C-37/C-38/C-39 to test independent satisfiability.

**Hypothesis**: C-36 requires the exception block to cite the governing Step 2C paraphrase clause alongside the Grounds -- so a scorer can verify Grounds consistency against the model's own commitment without cross-document lookup. C-37/C-38/C-39 are all Step 4 gate mechanisms; none of them appear in or depend on the exception block. V-02 tests whether C-36 is independently satisfiable in the absence of the Step 4 verbatim anchor. If C-36 requires C-37 to work (because the paraphrase clause in the exception block can only be verified against a Step 4 verbatim anchor), that dependency would be visible in scoring. The no-exception paraphrase-quote extension tests a parallel mechanism: does quoting the governing clause even when no exceptions fired add audit value independent of the exception path?

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

Before filling any severity cell, recall the inference rule you stated in Step 2C.
Do not fill the table until this line is written:

```
INFERENCE RULE (confirmed): [restate the rule from your Step 2C paraphrase]
```

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
- For each, fill an EXCEPTION SIGN-OFF BLOCK:

```
EXCEPTION SIGN-OFF:
Ticket ID: [T-NN]
Phase: 1
Assigned severity: [P0 or P1]
Grounds: [outage-level? YES / NO]
Paraphrase clause: [quote the specific clause from your INFERENCE RULE (stated) at Step 2C
  that governs this phase-severity decision -- copy it verbatim from your Step 2C block]
Disposition: [VALID EXCEPTION -- reason | VIOLATION -- corrected to P2/P3]
```

If no Phase 1 P0/P1 assignments exist, state:
**"No exceptions. Governing paraphrase clause for Phase 1: [quote the Phase 1 clause
from your INFERENCE RULE (stated) at Step 2C]."**

Scan Phase 3 rows in the vocabulary table (Step 4):
- List every Phase 3 ticket assigned P3.
- For each, fill an EXCEPTION SIGN-OFF BLOCK:

```
EXCEPTION SIGN-OFF:
Ticket ID: [T-NN]
Phase: 3
Assigned severity: P3
Grounds: [non-blocking issue? YES / NO]
Paraphrase clause: [quote the specific clause from your INFERENCE RULE (stated) at Step 2C
  that governs this phase-severity decision -- copy it verbatim from your Step 2C block]
Disposition: [VALID EXCEPTION -- reason | VIOLATION -- corrected to P1/P0]
```

If no Phase 3 P3 assignments exist, state:
**"No exceptions. Governing paraphrase clause for Phase 3: [quote the Phase 3 clause
from your INFERENCE RULE (stated) at Step 2C]."**

Confirm the INFERENCE RULE stated in Step 2C and confirmed at Step 4 has been
applied consistently. Compare the paraphrase from Step 2C against the audit results:
State: **"INFERENCE RULE paraphrase (Step 2C): [quote first 10 words of your Step 2C paraphrase].
Paraphrase clause in exception blocks: YES. [Cited in each exception SIGN-OFF; governing
clause quoted in no-exception paths.]
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

## V-03: Single-Axis -- Phrasing Register (Conversational, Carrying C-37+C-38)

**Axis**: Phrasing register shifted from formal imperative to descriptive/conversational throughout. The same structural mechanisms as R12 V-01 (dual-field Step 4 gate with own-words + verbatim anchor, "both lines" enforcement) are preserved, but the surrounding prose is rewritten to describe intent rather than issue directives. No scope confirmation (C-39) is added. No Paraphrase clause (C-36) is added.

**Hypothesis**: Structural mechanisms (labeled fields, "both lines" instruction, "do not paraphrase" clause) are the load-bearing elements for C-37 and C-38 -- the surrounding prose register should not affect whether those mechanisms fire. If a model following conversational instructions produces the same two labeled fields at Step 4, register is neutral. If the gentler register produces fewer instances of the required fields (because "both of these need to be written" is less forceful than "do not fill the table until both lines are written"), register would be load-bearing and the hypothesis fails. This tests whether the structural enforcements from C-37/C-38 survive a register shift, providing evidence about which part of the prompt is actually doing the work.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps or combine them.

---

## STEP 1 -- INERTIA: STATUS QUO

Start by grounding the ticket predictions in a real current-state scenario.

**1a. Current-state baseline**
In 2-3 sentences, describe what users are doing today to accomplish this job.
Where does it take the longest? What workarounds exist, and what do those cost
in time, context-switching, or accuracy?

**1b. Inertia competitor declaration**

Before going further, name the specific product users are migrating from.
This name will appear throughout your output -- in ticket bodies, gap entries,
and verification checks.

```
INERTIA COMPETITOR: [product name]
Prohibited: "existing tooling", "their current system", "legacy workflow",
or any phrase that does not produce a grep-checkable product name string.
```

**1c. Adoption-curve context**
Note whether the user population is still in the dual-tool phase (early) or
has committed to the new product and is hitting parity gaps (late).
This shapes the phase distribution and severity calibration.

---

## STEP 2 -- PHASE MAP TABLE

Before generating any ticket, lay out the expected severity and volume shape
per lifecycle window. This table becomes the distribution constraint for Step 4.

| Phase | Window | Expected severity range | Expected volume character |
|-------|--------|------------------------|--------------------------|
| Phase 1 | Day 0-30 | P2/P3 | high |
| Phase 2 | Day 31-60 | P1/P2 | medium |
| Phase 3 | Day 61-90 | P0/P1 | medium/low |

---

## STEP 2B -- PHASE BODY TEMPLATE TABLE

Replace [INERTIA COMPETITOR] with the product name you recorded in Step 1b.
These two sentences are the opening lines for Phase 1 and Phase 3 ticket bodies.

| Phase | Adoption stance | Pre-printed template sentence |
|-------|----------------|-------------------------------|
| Phase 1 | Dual-tool tension | "I still have [INERTIA COMPETITOR] open in another tab while working through this -- I keep switching back to check how it handled [specific scenario]." |
| Phase 3 | Parity gap | "In [INERTIA COMPETITOR] I could [specific action] without leaving this screen; here I cannot find a way to do it at all." |

How to use these templates:
- Phase 1 bodies: open with the Phase 1 sentence, all placeholders filled with specifics.
- Phase 3 bodies: open with the Phase 3 sentence, all placeholders filled with specifics.
- Phase 2 bodies: mention the competitor where it fits naturally; no set template.

---

## STEP 2C -- PHASE-SEVERITY INFERENCE RULE

This rule governs how phase position maps to severity. Read it carefully,
then restate it in your own words before moving on.

**The directional rule:**

Phase 1 tickets (Day 0-30): P2 or P3 for non-outage issues.
Why: the old tool is still open. Adoption friction is normal and survivable.
The user has a fallback -- they can complete the task in the competitor.
Lower severity reflects friction, not blockage.

Phase 3 tickets (Day 61-90) that block task completion: P1 or P0.
Why: the old tool is gone from the user's daily workflow. A capability gap
at this stage has no fallback. The user is blocked, not just slowed.
Higher severity reflects genuine blockage.

**Violations to flag later (in Steps 4, 4B, and Pass 2 Part C):**
- Phase 1 P0 or P1 on a non-outage ticket: this is a directional violation. Correct to P2/P3.
- Phase 3 P3 on a blocking ticket: this is a directional violation. Correct to P1/P0.

**Before moving on, restate this rule in your own words:**
The paraphrase you write here will be recalled at Step 4 and verified in Pass 2 Part C.
Write what you understood -- not a copy of the text above.

```
INFERENCE RULE (stated): [your paraphrase of the directional rule above]
Applied in: Steps 4, 4B, and Pass 2 INFERENCE AUDIT
```

Stay on this step until the paraphrase block is filled with your own words.

---

## STEP 3 -- PERFORMANCE MODE DECLARATION

When writing ticket bodies, you are the persona -- not an analyst describing the persona.

**You ARE the persona named on each ticket card.**

Your old workflow ran on [INERTIA COMPETITOR -- insert product name from Step 1b].
You recently started using this new product. Your perspective shifts across phases:
- Phase 1: you still have the old tool open in another tab. You're learning.
  You can fall back. That's why Phase 1 tickets are lower severity.
- Phase 3: you've committed to the new tool. The old one is out of your workflow.
  You're blocked. That's why Phase 3 tickets are higher severity.

Third-person forms that are off-limits in your ticket bodies:
"the user", "they", "the SRE", "the PM", "the engineer" -- any named-role title
referring to yourself from the outside.

Verb-subject forms that are off-limits:
"the SRE ran", "the PM reviewed", "the engineer observed", "the C-07 clicked",
"the Support agent opened" -- any construction where a role title precedes a verb.

Every action in your ticket happened to "I". Every mention of the old tool
uses its product name -- never a pronoun, never a description.

---

## STEP 4 -- VOCABULARY PRE-COMMITMENT TABLE

Before filling any severity cell, look back at what you wrote in Step 2C.
You need to write two things first, and both need to be filled in before
the table is populated:

```
INFERENCE RULE (confirmed): [restate what you wrote in INFERENCE RULE (stated) -- in your own words]
Verbatim from 2C: [copy your exact first sentence from the INFERENCE RULE (stated)
  block in Step 2C -- word for word, do not paraphrase]
```

Both of those lines need to be written before you fill any row in the table below.

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

Lock all vocabulary values in this table. Full card bodies come next in Step 5.

---

## STEP 4B -- COLLECTIVE DISTRIBUTION AUDIT

Before writing any card body, check these five constraints against the table:

1. **Phase distribution** -- at least two Phase 1 rows and one Phase 3 row.
2. **Category spread** -- at least three distinct category values.
3. **Volume distribution** -- all three volume levels present.
4. **Phase-character compliance** -- each row's volume and severity match the Step 2 ranges.
5. **Inference-rule compliance** -- use the rule you confirmed above the table:
   - Scan Phase 1 rows: flag any P0 or P1 on a non-outage ticket.
   - Scan Phase 3 rows: flag any P3 on a blocking ticket.
   - State PASS if none found; FAIL and name the row and correction if any found.

State PASS or FAIL for each constraint.
If any constraint fails, correct the table and re-run. Name what you changed.

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
[You ARE this persona. Your previous workflow used [INERTIA COMPETITOR -- product name].
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

For each pattern you identify, use this flat field structure.
No parent "Consequence:" label over the three consequence fields --
each field stands on its own at the same level as Pattern name and Root cause.

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
This sub-section covers migration barriers only. It is separate from the three
sections above -- not absorbed into any of them. At least one entry required.

Format for every entry:

```
Switching-friction gap: [short name]
Migrating from: [product name from Step 1b -- verbatim, grep-checkable]
Expected behavior: [one sentence -- what users expected, based on the competitor's behavior]
Actual behavior: [one sentence -- what this product actually does or fails to do]
Migration impact: [one sentence -- what users must change, lose, or manually replicate]
```

Rules:
- `Migrating from:` must contain the product name from Step 1b verbatim.
  Not "existing tool", not "legacy workflow" -- the actual product name.
- `Expected behavior:` and `Actual behavior:` describe the same capability from two sides.
- Each entry should stand alone: a reader scanning only this sub-section should be able
  to identify the competitor, the behavior delta, and the migration cost without reading
  anything else.

### Pre-Launch Priority
Name the single gap to close first. Connect it to specific ticket IDs, severity, and volume.
Say whether it reduces switching-friction for users coming from the inertia competitor.

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
- For each, fill an EXCEPTION SIGN-OFF BLOCK:

```
EXCEPTION SIGN-OFF:
Ticket ID: [T-NN]
Phase: 1
Assigned severity: [P0 or P1]
Grounds: [outage-level? YES / NO]
Disposition: [VALID EXCEPTION -- reason | VIOLATION -- corrected to P2/P3]
```

If no Phase 1 P0/P1 assignments exist, state:
**"No Phase 1 P0/P1 exceptions. PASS."**

Scan Phase 3 rows in the vocabulary table (Step 4):
- List every Phase 3 ticket assigned P3.
- For each, fill an EXCEPTION SIGN-OFF BLOCK:

```
EXCEPTION SIGN-OFF:
Ticket ID: [T-NN]
Phase: 3
Assigned severity: P3
Grounds: [non-blocking issue? YES / NO]
Disposition: [VALID EXCEPTION -- reason | VIOLATION -- corrected to P1/P0]
```

If no Phase 3 P3 assignments exist, state:
**"No Phase 3 P3 exceptions. PASS."**

Check that what you wrote in INFERENCE RULE (confirmed) and the verbatim anchor at Step 4
is consistent with the ticket severity assignments you just scanned.
State: **"INFERENCE RULE paraphrase (Step 2C): [quote first 10 words of your Step 2C paraphrase].
Verbatim anchor at Step 4: YES.
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

## V-04: Combined (V-01 + V-02) -- All Four New Criteria

**Axes combined**: Step-4 gate structure (V-01: dual-field + scope confirmation) AND exception block structure (V-02: 6-field with Paraphrase clause). This is the first variation that targets all four new criteria simultaneously: C-37+C-38 from the dual-field gate, C-39 from the scope confirmation, C-36 from the exception block Paraphrase clause field.

**Hypothesis**: All four new criteria are independently satisfiable and can coexist in one variation without structural conflict. C-36 (exception block) and C-37/C-38/C-39 (Step 4 gate) operate on different structural locations -- the exception block in Part C and the severity table header in Step 4. The mechanisms do not compete for the same instruction slot. The scope confirmation (C-39) closes after the dual-field gate and before the table header, making the three-element gate sequence: INFERENCE RULE (confirmed) + Verbatim from 2C + Confirmation. This tests whether a scorer can count both labeled fields for C-38 when a third declarative line follows them.

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

Before filling any severity cell, recall the inference rule you stated in Step 2C.
Do not fill the table until both lines are written:

```
INFERENCE RULE (confirmed): [restate the rule from your Step 2C paraphrase in your own words]
Verbatim from 2C: [quote your exact first sentence from the INFERENCE RULE (stated)
  block in Step 2C -- copy it word for word, do not paraphrase]
```

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
- For each, fill an EXCEPTION SIGN-OFF BLOCK:

```
EXCEPTION SIGN-OFF:
Ticket ID: [T-NN]
Phase: 1
Assigned severity: [P0 or P1]
Grounds: [outage-level? YES / NO]
Paraphrase clause: [quote the specific clause from your INFERENCE RULE (stated) at Step 2C
  that governs this phase-severity decision -- copy it verbatim from your Step 2C block]
Disposition: [VALID EXCEPTION -- reason | VIOLATION -- corrected to P2/P3]
```

If no Phase 1 P0/P1 assignments exist, state:
**"No exceptions. Governing paraphrase clause for Phase 1: [quote the Phase 1 clause
from your INFERENCE RULE (stated) at Step 2C]."**

Scan Phase 3 rows in the vocabulary table (Step 4):
- List every Phase 3 ticket assigned P3.
- For each, fill an EXCEPTION SIGN-OFF BLOCK:

```
EXCEPTION SIGN-OFF:
Ticket ID: [T-NN]
Phase: 3
Assigned severity: P3
Grounds: [non-blocking issue? YES / NO]
Paraphrase clause: [quote the specific clause from your INFERENCE RULE (stated) at Step 2C
  that governs this phase-severity decision -- copy it verbatim from your Step 2C block]
Disposition: [VALID EXCEPTION -- reason | VIOLATION -- corrected to P1/P0]
```

If no Phase 3 P3 assignments exist, state:
**"No exceptions. Governing paraphrase clause for Phase 3: [quote the Phase 3 clause
from your INFERENCE RULE (stated) at Step 2C]."**

Confirm the INFERENCE RULE stated in Step 2C and confirmed at Step 4 has been
applied consistently. Compare the paraphrase from Step 2C against the audit results:
State: **"INFERENCE RULE paraphrase (Step 2C): [quote first 10 words of your Step 2C paraphrase].
Verbatim anchor at Step 4: YES.
Scope confirmation at Step 4: YES. [This rule applies to every severity assignment in the table.]
Paraphrase clause in exception blocks: YES. [Cited in each SIGN-OFF; governing clause
quoted in each no-exception path.]
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

## V-05: Full Synthesis -- All Four + Conversational Register + Inertia Framing Gates

**Axes combined**: V-01 (dual-field + scope, C-37+C-38+C-39) + V-02 (exception Paraphrase clause, C-36) + V-03 (conversational register) + R12 V-03 (inertia competitor confirmation gates at Steps 4, 5, 7). This is the ceiling variation for R13, targeting all four new criteria in a conversational register with embedded competitor-name re-anchoring.

**Hypothesis**: Register and inertia framing are orthogonal to the four new structural mechanisms. The conversational register from V-03 should preserve C-37+C-38 compliance (labeled fields are structural, not register-dependent). The scope confirmation (C-39) is declarative rather than imperative -- it may actually survive a register shift better than the "both lines" instruction. The Paraphrase clause in the exception block (C-36) is a field label, register-independent. The inertia gates at Steps 4 and 5 re-anchor the product name in generation context, making competitor-name fidelity more durable. V-05 tests whether all four criteria survive the full combination, and whether register + inertia framing creates any interaction effects on the structural gates.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps or combine them.

---

## STEP 1 -- INERTIA: STATUS QUO

Start by grounding the ticket predictions in a real current-state scenario.

**1a. Current-state baseline**
In 2-3 sentences, describe what users are doing today to accomplish this job.
Where does it take the longest? What workarounds exist, and what do those cost
in time, context-switching, or accuracy?

**1b. Inertia competitor declaration**

Before going further, name the specific product users are migrating from.
This name will appear throughout your output -- in ticket bodies, gap entries,
and verification checks.

```
INERTIA COMPETITOR: [product name]
Prohibited: "existing tooling", "their current system", "legacy workflow",
or any phrase that does not produce a grep-checkable product name string.
```

**1c. Adoption-curve context**
Note whether the user population is still in the dual-tool phase (early) or
has committed to the new product and is hitting parity gaps (late).
This shapes the phase distribution and severity calibration.

---

## STEP 2 -- PHASE MAP TABLE

Before generating any ticket, lay out the expected severity and volume shape
per lifecycle window.

| Phase | Window | Expected severity range | Expected volume character |
|-------|--------|------------------------|--------------------------|
| Phase 1 | Day 0-30 | P2/P3 | high |
| Phase 2 | Day 31-60 | P1/P2 | medium |
| Phase 3 | Day 61-90 | P0/P1 | medium/low |

---

## STEP 2B -- PHASE BODY TEMPLATE TABLE

Replace [INERTIA COMPETITOR] with the product name from Step 1b.

| Phase | Adoption stance | Pre-printed template sentence |
|-------|----------------|-------------------------------|
| Phase 1 | Dual-tool tension | "I still have [INERTIA COMPETITOR] open in another tab while working through this -- I keep switching back to check how it handled [specific scenario]." |
| Phase 3 | Parity gap | "In [INERTIA COMPETITOR] I could [specific action] without leaving this screen; here I cannot find a way to do it at all." |

How to use these templates:
- Phase 1 bodies: open with the Phase 1 sentence, all placeholders filled with specifics.
- Phase 3 bodies: open with the Phase 3 sentence, all placeholders filled with specifics.
- Phase 2 bodies: mention the competitor where it fits naturally; no set template.

---

## STEP 2C -- PHASE-SEVERITY INFERENCE RULE

This rule governs how phase position maps to severity. Read it carefully,
then restate it in your own words before moving on.

**The directional rule:**

Phase 1 tickets (Day 0-30): P2 or P3 for non-outage issues.
Why: the old tool is still open. Adoption friction is normal and survivable.
The user has a fallback -- they can complete the task in the competitor.
Lower severity reflects friction, not blockage.

Phase 3 tickets (Day 61-90) that block task completion: P1 or P0.
Why: the old tool is gone from the user's daily workflow. A capability gap
at this stage has no fallback. The user is blocked, not just slowed.
Higher severity reflects genuine blockage.

**Violations to flag later (in Steps 4, 4B, and Pass 2 Part C):**
- Phase 1 P0 or P1 on a non-outage ticket: directional violation. Correct to P2/P3.
- Phase 3 P3 on a blocking ticket: directional violation. Correct to P1/P0.

**Before moving on, restate this rule in your own words:**
The paraphrase you write here will be recalled at Step 4 and verified in Pass 2 Part C.
Write what you understood -- not a copy of the text above.

```
INFERENCE RULE (stated): [your paraphrase of the directional rule above]
Applied in: Steps 4, 4B, and Pass 2 INFERENCE AUDIT
```

Stay on this step until the paraphrase block is filled with your own words.

---

## STEP 3 -- PERFORMANCE MODE DECLARATION

When writing ticket bodies, you are the persona -- not an analyst describing the persona.

**You ARE the persona named on each ticket card.**

Your old workflow ran on [INERTIA COMPETITOR -- insert product name from Step 1b].
You recently started using this new product. Your perspective shifts across phases:
- Phase 1: you still have the old tool open in another tab. You're learning.
  You can fall back. That's why Phase 1 tickets are lower severity.
- Phase 3: you've committed to the new tool. The old one is out of your workflow.
  You're blocked. That's why Phase 3 tickets are higher severity.

Third-person forms that are off-limits in your ticket bodies:
"the user", "they", "the SRE", "the PM", "the engineer" -- any named-role title
referring to yourself from the outside.

Verb-subject forms that are off-limits:
"the SRE ran", "the PM reviewed", "the engineer observed", "the C-07 clicked",
"the Support agent opened" -- any construction where a role title precedes a verb.

Every action in your ticket happened to "I". Every mention of the old tool
uses its product name -- never a pronoun, never a description.

---

## STEP 4 -- VOCABULARY PRE-COMMITMENT TABLE

Competitor in scope: [write the product name from Step 1b here -- not "the tool",
not "my old system". This exact string must appear verbatim in every Phase 1
and Phase 3 ticket body in Step 5.]

Before filling any severity cell, look back at what you wrote in Step 2C.
You need to write two things first. Both need to be filled in before
any row in the table is populated:

```
INFERENCE RULE (confirmed): [restate what you wrote in INFERENCE RULE (stated) -- in your own words]
Verbatim from 2C: [copy your exact first sentence from the INFERENCE RULE (stated)
  block in Step 2C -- word for word, do not paraphrase]
```

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

Lock all vocabulary values in this table. Full card bodies come next in Step 5.

---

## STEP 4B -- COLLECTIVE DISTRIBUTION AUDIT

Before writing any card body, check these five constraints against the table:

1. **Phase distribution** -- at least two Phase 1 rows and one Phase 3 row.
2. **Category spread** -- at least three distinct category values.
3. **Volume distribution** -- all three volume levels present.
4. **Phase-character compliance** -- each row's volume and severity match the Step 2 ranges.
5. **Inference-rule compliance** -- use the rule you confirmed above the table:
   - Scan Phase 1 rows: flag any P0 or P1 on a non-outage ticket.
   - Scan Phase 3 rows: flag any P3 on a blocking ticket.
   - State PASS if none found; FAIL and name the row and correction if any found.

State PASS or FAIL for each constraint.
If any constraint fails, correct the table and re-run. Name what you changed.

---

## STEP 5 -- FULL CARD BODIES

Competitor in scope: [write the product name from Step 1b here before writing any card body --
not "the tool", not "my old system". This exact string must appear in every Phase 1
and Phase 3 ticket body below.]

For each row in the summary table:

```
Ticket ID: [T-NN]
Title: [descriptive title]
Category: [must match Step 4 exactly]
Persona: [must match Step 4 exactly]
Volume: [must match Step 4 exactly]
Severity: [must match Step 4 exactly]

Body:
[You ARE this persona. Your previous workflow used [INERTIA COMPETITOR -- product name].
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

For each pattern you identify, use this flat field structure.
No parent "Consequence:" label over the three consequence fields --
each field stands on its own at the same level as Pattern name and Root cause.

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

Competitor in scope: [write the product name from Step 1b here before writing any gap --
not "the tool" or any alias. Every Switching-Friction gap's `Migrating from:` field
must contain this exact string.]

### Doc Gaps
[At least one documentation gap.]

### Design Gaps
[At least one design gap.]

### Operational Gaps
[At least one operational gap.]

### Switching-Friction Gaps
This sub-section covers migration barriers only. It is separate from the three
sections above -- not absorbed into any of them. At least one entry required.

Format for every entry:

```
Switching-friction gap: [short name]
Migrating from: [product name from Step 1b -- verbatim, grep-checkable]
Expected behavior: [one sentence -- what users expected, based on the competitor's behavior]
Actual behavior: [one sentence -- what this product actually does or fails to do]
Migration impact: [one sentence -- what users must change, lose, or manually replicate]
```

Rules:
- `Migrating from:` must contain the product name from Step 1b verbatim.
  Not "existing tool", not "legacy workflow" -- the actual product name.
- `Expected behavior:` and `Actual behavior:` describe the same capability from two sides.
- Each entry should stand alone: a reader scanning only this sub-section should be able
  to identify the competitor, the behavior delta, and the migration cost without reading
  anything else.

### Pre-Launch Priority
Name the single gap to close first. Connect it to specific ticket IDs, severity, and volume.
Say whether it reduces switching-friction for users coming from the inertia competitor.

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
   at least four card bodies, and in every `Migrating from:` field.
   State: **"[PRODUCT NAME] in Step 1b: YES. Card bodies: T-NN, T-NN, T-NN, T-NN (minimum four).
   Migrating from: fields: [list all entries -- each must contain the verbatim name]."**

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
- For each, fill an EXCEPTION SIGN-OFF BLOCK:

```
EXCEPTION SIGN-OFF:
Ticket ID: [T-NN]
Phase: 1
Assigned severity: [P0 or P1]
Grounds: [outage-level? YES / NO]
Paraphrase clause: [quote the specific clause from your INFERENCE RULE (stated) at Step 2C
  that governs this phase-severity decision -- copy it verbatim from your Step 2C block]
Disposition: [VALID EXCEPTION -- reason | VIOLATION -- corrected to P2/P3]
```

If no Phase 1 P0/P1 assignments exist, state:
**"No exceptions. Governing paraphrase clause for Phase 1: [quote the Phase 1 clause
from your INFERENCE RULE (stated) at Step 2C]."**

Scan Phase 3 rows in the vocabulary table (Step 4):
- List every Phase 3 ticket assigned P3.
- For each, fill an EXCEPTION SIGN-OFF BLOCK:

```
EXCEPTION SIGN-OFF:
Ticket ID: [T-NN]
Phase: 3
Assigned severity: P3
Grounds: [non-blocking issue? YES / NO]
Paraphrase clause: [quote the specific clause from your INFERENCE RULE (stated) at Step 2C
  that governs this phase-severity decision -- copy it verbatim from your Step 2C block]
Disposition: [VALID EXCEPTION -- reason | VIOLATION -- corrected to P1/P0]
```

If no Phase 3 P3 assignments exist, state:
**"No exceptions. Governing paraphrase clause for Phase 3: [quote the Phase 3 clause
from your INFERENCE RULE (stated) at Step 2C]."**

Check that what you wrote in both Step 4 fields is consistent with the ticket severity
assignments you just scanned.
State: **"INFERENCE RULE paraphrase (Step 2C): [quote first 10 words of your Step 2C paraphrase].
Verbatim anchor at Step 4: YES.
Scope confirmation at Step 4: YES. [This rule applies to every severity assignment in the table.]
Paraphrase clause in exception blocks: YES. [Cited in each SIGN-OFF; governing clause
quoted in each no-exception path.]
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
