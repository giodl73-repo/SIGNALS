# listen-support Round 12 -- Skill Body Prompt Variations

**Rubric target**: v12 (245 pts)
**New criteria in scope**: C-36 (Exception Block Paraphrase-Clause Field), C-37 (Step-4 Verbatim Anchor Field), C-38 (Dual-Field Step-4 Gate), C-39 (Step-4 Every-Assignment Scope Confirmation)
**Base**: All prior mechanisms from R11 V-05 (C-01 through C-35 at ceiling)

**Variation axes selected** (3 single-axis, then 2 combined):
1. **Step-4 gate structure** -- dual-field (own-words restatement + verbatim anchor, "do not fill until both written") → targets C-37, C-38 (V-01)
2. **Exception block paraphrase linkage** -- "Paraphrase clause" 6th field + no-exception path quotes governing paraphrase → targets C-36 (V-02)
3. **Inertia framing prominence** -- competitor name confirmation gate embedded at every ticket-generating step → no new criteria (V-03)
4. **V-01 + V-03 combined** -- dual-field Step-4 gate + competitor name reminder gates → targets C-37, C-38 (V-04)
5. **Full synthesis** -- verbatim anchor + scope confirmation + exception paraphrase clause + inertia framing → targets C-36, C-37, C-39 (NOT C-38 -- verbatim+scope pair, not verbatim+own-words pair) (V-05)

---

## V-01: Single-Axis -- Dual-Field Step-4 Gate (Own-Words + Verbatim Anchor)

**Axis**: Step-4 gate structure -- tightened to dual-field. The `INFERENCE RULE (confirmed)` block requires two separately labeled fields: (1) own-words restatement, (2) verbatim anchor with "do not paraphrase" instruction. "Do not fill the table until both lines are written" makes neither field optional. Exception block remains at R11 baseline (5-field: Ticket ID, Phase, Assigned severity, Grounds, Disposition -- no Paraphrase clause). No scope confirmation at Step 4. Part C paraphrase consistency confirmation includes "Verbatim anchor at Step 4: YES" check line.

**Hypothesis**: The R11 V-05 at-ceiling baseline had a verbatim+scope Step 4 gate -- not a verbatim+own-words gate. C-38 requires both simultaneously: the own-words restatement tests encoding (the model must understand the directional logic to restate it); the verbatim anchor tests retrieval fidelity (the model must reproduce the exact Step 2C text). A verbatim-only gate allows copying without understanding; a restatement-only gate allows silent divergence. The dual-field "both lines" structure is structurally self-enforcing: a scorer counts two distinct labeled fields. V-01 isolates whether the dual-field gate satisfies C-37+C-38 without scope confirmation.

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

END OF PASS 1. Switch to verification mode for properties and inference audit.

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

## V-02: Single-Axis -- Exception Block Paraphrase-Clause Field (6th Field + No-Exception Paraphrase Quote)

**Axis**: Exception SIGN-OFF BLOCK structure -- tightened to 6-field format. A sixth field `Paraphrase clause:` is added to every EXCEPTION SIGN-OFF BLOCK, requiring a verbatim quote from the Step 2C INFERENCE RULE (stated) paraphrase that governs the phase-severity assignment under review. The no-exception path is extended: instead of "No Phase 1 P0/P1 exceptions. PASS." it states "No exceptions. Governing paraphrase clause for Phase 1: [quote from Step 2C]." -- making the rule that held auditable even when no violations occurred. The Step 4 gate remains at R11 baseline (free restatement only, no verbatim anchor). No scope confirmation is added.

**Hypothesis**: C-33 requires a structured EXCEPTION SIGN-OFF BLOCK with named fields so each exception's Grounds can be independently verified. However, Grounds states only whether a ticket qualifies as outage/non-blocking -- it does not require the model to demonstrate which clause of its Step 2C paraphrase permits the deviation. A model can fill Grounds with "this was a total service outage" and the scorer evaluates that justification in isolation, without access to the model's own governing commitment in the same view. Adding `Paraphrase clause:` places the governing commitment next to the Grounds in the same block: a scorer can verify that the Grounds text is consistent with the cited clause by reading two adjacent fields. The no-exception path extension makes the governing paraphrase auditable even when no exceptions triggered: "Governing paraphrase clause for Phase 1: [quote]" identifies which rule held, not just that it held. V-02 isolates whether the Paraphrase clause field satisfies C-36 without the Step 4 verbatim anchor changes of V-01.

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

END OF PASS 1. Switch to verification mode for properties and inference audit.

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

## V-03: Single-Axis -- Inertia Framing Prominence (Structural Competitor Name Gates)

**Axis**: Inertia competitor framing -- structurally embedded at every ticket-generating step. Steps 4, 5, and 7 each open with a mandatory one-line competitor name confirmation: "Competitor in scope: [write product name from Step 1b -- do not write 'the tool', 'my old system', or any alias]." Step 2B's template replacement becomes a mandatory fill step, not merely an instruction. Part B tool-name fidelity check is extended to require the competitor name in at least four card bodies (up from two) and in every switching-friction gap entry. The Step 4 gate remains at R11 baseline (free restatement, no verbatim anchor). Exception block remains at 5-field baseline. No scope confirmation is added.

**Hypothesis**: The inertia competitor name is declared once in Step 1b. Later steps reference it as "the product name from Step 1b" -- a description that allows a model to drift into pronouns or aliases ("my old tool", "the previous platform") across multiple card bodies as the product-name declaration recedes in context. The structural embedding re-anchors the product name at each ticket-generating step: the model writes the product name out at Steps 4, 5, and 7 before content generation begins. This increases the density of verbatim product-name occurrences, making tool-name fidelity (C-22, Part B check) harder to fail. The variation is neutral on C-36/37/38/39 -- it tests whether structural competitor reminders alone improve output quality on the inertia-fidelity dimensions, independent of the inference-rule gate changes.

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

Before writing this table: write the product name from Step 1b in place of every
[INERTIA COMPETITOR] placeholder. Do not proceed until all placeholders are filled.

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

Competitor in scope: [write the product name from Step 1b here before writing any card body --
do not write "the tool", "my old system", or any alias. This name must appear verbatim
in the body of every Phase 1 and Phase 3 ticket below.]

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

Competitor in scope: [write the product name from Step 1b here before writing any gap --
do not write "the tool" or any alias. Every Switching-Friction gap's `Migrating from:`
field must contain this exact string.]

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

END OF PASS 1. Switch to verification mode for properties and inference audit.

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

## V-04: Combined -- Dual-Field Step-4 Gate + Inertia Framing Prominence

**Axis 1** (from V-01): Step-4 dual-field gate -- own-words restatement field + verbatim anchor field with "do not fill until both written" language. Satisfies C-37, C-38.
**Axis 2** (from V-03): Competitor name structurally embedded at Steps 4, 5, and 7 with mandatory confirmation gates. Part B tool-name fidelity check extended to four card bodies minimum.

**Hypothesis**: V-01 closes the encoding/retrieval divergence failure mode at Step 4. V-03 closes the tool-name drift failure mode across card bodies. V-04 tests whether both mechanisms are jointly satisfiable without interference: the dual-field gate adds structural load at Step 4, while the competitor reminders add mandatory write operations at each ticket-generating step. The prediction is that neither mechanism disrupts the other -- the competitor gate is a short write before content generation, while the inference-rule gate is a structural requirement on the paraphrase block. The combined variation should satisfy C-37 and C-38 via the Step 4 mechanism and improve tool-name fidelity via the competitor reminders. Exception block remains at 5-field baseline. No scope confirmation.

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

Before writing this table: write the product name from Step 1b in place of every
[INERTIA COMPETITOR] placeholder. Do not proceed until all placeholders are filled.

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

Before filling any severity cell, recall the inference rule you stated in Step 2C.
Do not fill the table until both lines are written:

```
INFERENCE RULE (confirmed): [restate the rule from your Step 2C paraphrase in your own words]
Verbatim from 2C: [quote your exact first sentence from the INFERENCE RULE (stated)
  block in Step 2C -- copy it word for word, do not paraphrase]
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

Competitor in scope: [write the product name from Step 1b here before writing any card body --
do not write "the tool" or any alias. This name must appear verbatim in the body of every
Phase 1 and Phase 3 ticket below.]

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

Competitor in scope: [write the product name from Step 1b here before writing any gap --
do not write "the tool" or any alias. Every Switching-Friction gap's `Migrating from:`
field must contain this exact string.]

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

END OF PASS 1. Switch to verification mode for properties and inference audit.

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

## V-05: Full Synthesis -- Verbatim Anchor + Scope Confirmation + Exception Paraphrase Clause + Inertia Framing

**Axis 1**: Verbatim anchor at Step 4 (C-37) -- dedicated `Verbatim anchor from 2C:` field with "word for word, do not paraphrase" instruction.
**Axis 2**: Scope confirmation at Step 4 (C-39) -- "Confirmation: this rule applies to every severity assignment in the table below." immediately following the verbatim anchor.
**Axis 3**: Exception block Paraphrase clause (C-36) -- sixth field added to every EXCEPTION SIGN-OFF BLOCK; no-exception path quotes governing paraphrase clause.
**Axis 4**: Inertia framing prominence (from V-03) -- competitor name confirmation gate at Steps 4, 5, and 7.

**Note on C-38**: V-05 does NOT satisfy C-38. The Step 4 gate in V-05 pairs verbatim anchor with scope confirmation -- not verbatim anchor with own-words restatement. C-38 requires both a restatement field AND a verbatim anchor field simultaneously. V-05's gate has a verbatim anchor (satisfying C-37) and a scope confirmation (satisfying C-39) but no separately labeled own-words restatement field. A model generating V-05 cannot satisfy C-38 without also satisfying C-37, but satisfying C-37 via the verbatim+scope pairing does not trigger C-38.

**Hypothesis**: V-05 tests the full combination of C-36+C-37+C-39 minus C-38. The key structural distinction from V-04 is at Step 4: V-04's dual-field gate (own-words + verbatim) tests encoding AND retrieval simultaneously; V-05's verbatim+scope gate tests retrieval AND table-wide commitment simultaneously. The Paraphrase clause in the exception block (shared with V-02) anchors every exception to the governing paraphrase in the same view. The prediction is that V-05 achieves 20 aspirational pts (C-36: 5 + C-37: 5 + C-39: 5 + one other from prior rounds) while V-04 achieves 10 (C-37: 5 + C-38: 5). Whether C-36+C-39 or C-38 produces a higher compliance ceiling at the full output level is the primary test question for R12.

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

Before writing this table: write the product name from Step 1b in place of every
[INERTIA COMPETITOR] placeholder. Do not proceed until all placeholders are filled.

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

Before filling any severity cell, recall the inference rule you stated in Step 2C.
Do not fill the table until both lines are written:

```
Verbatim anchor from 2C: [quote your exact first sentence from the INFERENCE RULE (stated)
  block in Step 2C -- word for word, do not paraphrase]
Confirmation: this rule applies to every severity assignment in the table below.
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

Competitor in scope: [write the product name from Step 1b here before writing any card body --
do not write "the tool" or any alias. This name must appear verbatim in the body of every
Phase 1 and Phase 3 ticket below.]

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

Competitor in scope: [write the product name from Step 1b here before writing any gap --
do not write "the tool" or any alias. Every Switching-Friction gap's `Migrating from:`
field must contain this exact string.]

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

END OF PASS 1. Switch to verification mode for properties and inference audit.

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

Confirm the INFERENCE RULE stated in Step 2C and confirmed at Step 4 has been
applied consistently. Compare the paraphrase from Step 2C against the audit results:
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

## Satisfaction Matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-36 Exception block paraphrase-clause field | -- | YES | -- | -- | YES |
| C-37 Step-4 verbatim anchor field | YES | -- | -- | YES | YES |
| C-38 Dual-field Step-4 gate | YES | -- | -- | YES | -- |
| C-39 Step-4 every-assignment scope confirmation | -- | -- | -- | -- | YES |

**Structural diff per variation:**

| Location | V-01 | V-02 | V-03 | V-04 | V-05 |
|----------|------|------|------|------|------|
| Step 4 gate | dual-field (own-words + verbatim) | free restatement | free restatement | dual-field (own-words + verbatim) | verbatim + scope confirmation |
| Step 4 competitor gate | -- | -- | YES | YES | YES |
| Step 5 competitor gate | -- | -- | YES | YES | YES |
| Step 7 competitor gate | -- | -- | YES | YES | YES |
| Exception block fields | 5 (baseline) | 6 (+Paraphrase clause) | 5 (baseline) | 5 (baseline) | 6 (+Paraphrase clause) |
| No-exception path | outcome only | paraphrase quoted | outcome only | outcome only | paraphrase quoted |
| Part B tool-name fidelity threshold | 2 card bodies | 2 card bodies | 4 card bodies | 4 card bodies | 4 card bodies |
| Part C paraphrase consistency state | includes "Verbatim anchor: YES" | no verbatim anchor line | no verbatim anchor line | includes "Verbatim anchor: YES" | includes "Verbatim anchor: YES" |
