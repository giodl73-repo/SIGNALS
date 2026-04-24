# listen-support Round 11 -- Skill Body Prompt Variations

**Rubric target**: v11 (225 pts)
**New criteria in scope**: C-32 (Decision-Adjacent Paraphrase Gate), C-33 (Structured Exception Sign-Off Block in Part C), C-34 (Paraphrase Double-Gate with Step-4 Recall), C-35 (Part C Paraphrase Consistency Confirmation)
**Base**: All prior mechanisms from R10 V-05 (C-01 through C-35 at ceiling)

**Variation axes selected** (3 single-axis, then 2 combined):
1. **Step 4 anchor mode** -- the `INFERENCE RULE (confirmed)` block requires verbatim quotation of the Step 2C paraphrase first sentence rather than a free restatement -- (V-01 strong anchor, V-02/V-03 unchanged)
2. **Exception SIGN-OFF BLOCK Grounds-to-paraphrase citation** -- Grounds field must cite the paraphrase clause governing the assignment, not just state outage/non-blocking status -- (V-02)
3. **Step 4B paraphrase echo before constraint 5** -- Step 4B echoes the confirmed paraphrase text verbatim before running the inference-rule compliance scan -- (V-03)
4. **Verbatim anchor (V-01) + Step 4B echo (V-03)** combined -- (V-04)
5. **Full synthesis**: verbatim anchor at Step 4 + Grounds-to-paraphrase citation in exception blocks + Step 4B echo + Part C sub-check 1 text-match confirmation between Step 4 confirmed block and Step 2C paraphrase -- (V-05)

---

## V-01: Single-Axis -- Step 4 Verbatim Anchor (Hard Retrieval Gate)

**Axis**: Step 4 anchor mode -- strong. The `INFERENCE RULE (confirmed)` block at Step 4 requires the model to quote the exact first sentence from its Step 2C `INFERENCE RULE (stated)` block verbatim in a labeled bracket before writing the confirmation. Free restatement is replaced by a two-part structure: first, verbatim quote from 2C; second, confirmation that the rule applies. All other mechanisms from R10 V-05 are preserved intact.

**Hypothesis**: The current R10 V-05 Step 4 gate says "restate from your Step 2C paraphrase" -- a free restatement. The model can satisfy this by generating any paraphrase consistent with the underlying rule text without genuinely retrieving its 2C commitment. C-34 requires the cross-reference to prevent divergence, but labels a cross-reference structurally without testing whether retrieval occurred. Requiring verbatim quotation of the 2C text forces actual retrieval: the model must reproduce its own earlier generation text. If it cannot, the block is incomplete. This variation isolates whether the verbatim anchor changes compliance in practice -- C-34 passes with the free-restatement Step 4 gate; a potential C-36 would require the verbatim anchor.

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
INFERENCE RULE (confirmed):
  Verbatim from 2C: "[quote your exact first sentence from the INFERENCE RULE (stated)
  block in Step 2C -- copy it word for word, do not paraphrase]"
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

**Sub-check 1: Phase-Architecture Severity Compliance (C-28)**

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

If no Phase 1 P0/P1 assignments exist, state: **"No Phase 1 P0/P1 exceptions. PASS."**

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

If no Phase 3 P3 assignments exist, state: **"No Phase 3 P3 exceptions. PASS."**

Confirm the INFERENCE RULE stated in Step 2C and confirmed at Step 4 has been
applied consistently. Compare the paraphrase from Step 2C against the audit results:
State: **"INFERENCE RULE paraphrase (Step 2C): [quote first 10 words of your Step 2C paraphrase].
Verbatim anchor at Step 4: YES.
Audit result -- Phase 1 P2/P3 compliance: [PASS/FAIL].
Audit result -- Phase 3 P0/P1 compliance: [PASS/FAIL].
Paraphrase consistent with audit results: YES / NO."**

**Sub-check 2: Switching-Friction Sub-Section Field Completeness (C-29)**

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

## V-02: Single-Axis -- Exception SIGN-OFF BLOCK Grounds-to-Paraphrase Citation (5th Field)

**Axis**: Exception SIGN-OFF BLOCK structure -- tightened. A 5th field is added to every EXCEPTION SIGN-OFF BLOCK: `Paraphrase clause:` requires quoting the specific clause from the Step 2C paraphrase that governs the phase-severity assignment under review. The existing four fields (Ticket ID, Phase, Assigned severity, Grounds) are preserved. The no-exception path is also tightened: if no exceptions exist, the model must still state which paraphrase clause would govern Phase 1 P0/P1 and Phase 3 P3 assignments if any were found. All other mechanisms from R10 V-05 are preserved.

**Hypothesis**: C-33 requires a structured EXCEPTION SIGN-OFF BLOCK with at least four named fields so each exception's Grounds can be independently verified without parsing prose. Grounds currently states only whether a ticket qualifies as an outage/non-blocking -- it does not require the model to demonstrate it knows which clause of its paraphrase permits the deviation. A model can fill Grounds with generic justification ("this was an outage") without connecting to the specific commitment it made in Step 2C. Adding `Paraphrase clause:` forces traceability: the model must identify the clause in its own paraphrase that explains why this exception is valid or invalid. Without the 5th field, exception verification is independent of the paraphrase; with the 5th field, every exception is anchored to the paraphrase commitment. C-33 passes with four fields; a potential C-37 would require the paraphrase clause citation.

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

**Sub-check 1: Phase-Architecture Severity Compliance (C-28)**

Scan Phase 1 rows in the vocabulary table (Step 4):
- List every Phase 1 ticket assigned P0 or P1.
- For each, fill an EXCEPTION SIGN-OFF BLOCK (5 fields required):

```
EXCEPTION SIGN-OFF:
Ticket ID: [T-NN]
Phase: 1
Assigned severity: [P0 or P1]
Grounds: [outage-level? YES / NO -- state the outage or blocking condition]
Paraphrase clause: [quote the clause from your Step 2C INFERENCE RULE (stated) block
  that governs Phase 1 severity -- the specific phrase that permits or prohibits P0/P1]
Disposition: [VALID EXCEPTION -- grounds match paraphrase clause | VIOLATION -- corrected to P2/P3]
```

If no Phase 1 P0/P1 assignments exist:
State: **"No Phase 1 P0/P1 exceptions. PASS."**
State also: **"Governing paraphrase clause for Phase 1: [quote the Phase 1 clause
  from your Step 2C paraphrase]."**

Scan Phase 3 rows in the vocabulary table (Step 4):
- List every Phase 3 ticket assigned P3.
- For each, fill an EXCEPTION SIGN-OFF BLOCK (5 fields required):

```
EXCEPTION SIGN-OFF:
Ticket ID: [T-NN]
Phase: 3
Assigned severity: P3
Grounds: [non-blocking issue? YES / NO -- state the non-blocking condition]
Paraphrase clause: [quote the clause from your Step 2C INFERENCE RULE (stated) block
  that governs Phase 3 severity -- the specific phrase that permits or prohibits P3]
Disposition: [VALID EXCEPTION -- grounds match paraphrase clause | VIOLATION -- corrected to P1/P0]
```

If no Phase 3 P3 assignments exist:
State: **"No Phase 3 P3 exceptions. PASS."**
State also: **"Governing paraphrase clause for Phase 3: [quote the Phase 3 clause
  from your Step 2C paraphrase]."**

Confirm the INFERENCE RULE stated in Step 2C and confirmed at Step 4 has been
applied consistently. Compare the paraphrase from Step 2C against the audit results:
State: **"INFERENCE RULE paraphrase (Step 2C): [quote first 10 words of your Step 2C paraphrase].
Paraphrase confirmed at Step 4: YES.
Audit result -- Phase 1 P2/P3 compliance: [PASS/FAIL].
Audit result -- Phase 3 P0/P1 compliance: [PASS/FAIL].
Paraphrase consistent with audit results: YES / NO."**

**Sub-check 2: Switching-Friction Sub-Section Field Completeness (C-29)**

Confirm the Switching-Friction Gaps sub-section from Step 7 is present.
Scan every entry for the `Migrating from:` field:
- List each entry's `Migrating from:` value.
- Flag any entry where the value does not contain the product name from Step 1b verbatim.
State: **"Switching-Friction Gaps sub-section present: YES. Migrating from: fields --
[entry 1: value | entry 2: value | ...]. All fields populated with product name
verbatim: YES / NO. Missing or non-verbatim entries: [list or NONE]."**

State final: **"All Step 4 values match Step 5. Exception sign-offs complete.
Paraphrase clauses cited per exception. Sub-checks 1 and 2 verified. Paraphrase consistency confirmed."**
Name and correct any issue before finalizing.
```

---

## V-03: Single-Axis -- Step 4B Paraphrase Echo Before Constraint 5

**Axis**: Step 4B paraphrase echo -- a new block is inserted at the top of Step 4B, immediately before constraint 5, requiring the model to echo the confirmed paraphrase text verbatim from Step 4. Constraint 5 then references this echo rather than the upstream Step 4 confirmed block. All other mechanisms from R10 V-05 are preserved.

**Hypothesis**: C-32 established that the paraphrase gate must fire at the severity-assignment step (Step 4 header) because paraphrase committed upstream decays before the decision. The same decay risk applies to Step 4B constraint 5: the Step 4 confirmed block is generated at the Step 4 header, but Step 4B runs after the full vocabulary table is filled -- the confirmed text is no longer in immediate generation context. The inference-rule compliance scan in constraint 5 operates with the paraphrase as a background label ("apply the INFERENCE RULE confirmed above Step 4"), not live text. An echo at Step 4B makes the paraphrase text live at the scan decision point, the same logic C-32 applied to the vocabulary table itself. C-32 passes with the Step 4 gate alone; a potential C-38 would require the paraphrase to be echoed immediately before any inference-rule compliance scan.

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

Before running constraint 5, echo the confirmed inference rule:

```
INFERENCE RULE (4B echo): [copy the text of INFERENCE RULE (confirmed) from Step 4 verbatim]
```

Audit five constraints before writing any card body:

1. **Phase distribution** -- at least two Phase 1 rows and one Phase 3 row.
2. **Category spread** -- at least three distinct category values.
3. **Volume distribution** -- all three volume levels present.
4. **Phase-character compliance** -- each row's volume and severity match Step 2 ranges.
5. **Inference-rule compliance** -- apply the INFERENCE RULE echoed above:
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

**Sub-check 1: Phase-Architecture Severity Compliance (C-28)**

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

If no Phase 1 P0/P1 assignments exist, state: **"No Phase 1 P0/P1 exceptions. PASS."**

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

If no Phase 3 P3 assignments exist, state: **"No Phase 3 P3 exceptions. PASS."**

Confirm the INFERENCE RULE stated in Step 2C, confirmed at Step 4, and echoed at Step 4B
has been applied consistently. Compare the paraphrase from Step 2C against the audit results:
State: **"INFERENCE RULE paraphrase (Step 2C): [quote first 10 words of your Step 2C paraphrase].
Paraphrase confirmed at Step 4: YES. Paraphrase echoed at Step 4B: YES.
Audit result -- Phase 1 P2/P3 compliance: [PASS/FAIL].
Audit result -- Phase 3 P0/P1 compliance: [PASS/FAIL].
Paraphrase consistent with audit results: YES / NO."**

**Sub-check 2: Switching-Friction Sub-Section Field Completeness (C-29)**

Confirm the Switching-Friction Gaps sub-section from Step 7 is present.
Scan every entry for the `Migrating from:` field:
- List each entry's `Migrating from:` value.
- Flag any entry where the value does not contain the product name from Step 1b verbatim.
State: **"Switching-Friction Gaps sub-section present: YES. Migrating from: fields --
[entry 1: value | entry 2: value | ...]. All fields populated with product name
verbatim: YES / NO. Missing or non-verbatim entries: [list or NONE]."**

State final: **"All Step 4 values match Step 5. Exception sign-offs complete.
Sub-checks 1 and 2 verified. Paraphrase echoed at Step 4B. Paraphrase consistency confirmed."**
Name and correct any issue before finalizing.
```

---

## V-04: Combined -- Step 4 Verbatim Anchor (V-01) + Step 4B Paraphrase Echo (V-03)

**Axes**: (1) Step 4 anchor mode -- the `INFERENCE RULE (confirmed)` block requires verbatim quotation of the Step 2C paraphrase first sentence before the confirmation, replacing free restatement; (2) Step 4B echo -- the model echoes the confirmed paraphrase text verbatim at the top of Step 4B immediately before constraint 5. Both mechanisms address the same decay risk at different decision points: Step 4 vocabulary table and Step 4B distribution audit constraint 5.

**Hypothesis**: The verbatim anchor at Step 4 (V-01) forces genuine retrieval at severity assignment. The echo at Step 4B (V-03) makes the retrieved text live context at the collective distribution scan. Together, every inference-rule-bearing decision point in the prompt (Step 4 severity column and Step 4B constraint 5) has the paraphrase as active generation context, not as a decayed upstream commitment. V-01 alone ensures the severity table gets accurate enforcement; V-03 alone ensures the collective audit gets accurate enforcement; V-04 ensures both. The combination isolates whether two-point anchoring reduces violation rates at either decision point compared to single-point anchoring.

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
INFERENCE RULE (confirmed):
  Verbatim from 2C: "[quote your exact first sentence from the INFERENCE RULE (stated)
  block in Step 2C -- copy it word for word, do not paraphrase]"
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

Before running constraint 5, echo the confirmed inference rule:

```
INFERENCE RULE (4B echo): [copy the verbatim-from-2C text of INFERENCE RULE (confirmed)
from Step 4 -- the quoted first sentence -- verbatim]
```

Audit five constraints before writing any card body:

1. **Phase distribution** -- at least two Phase 1 rows and one Phase 3 row.
2. **Category spread** -- at least three distinct category values.
3. **Volume distribution** -- all three volume levels present.
4. **Phase-character compliance** -- each row's volume and severity match Step 2 ranges.
5. **Inference-rule compliance** -- apply the INFERENCE RULE echoed above:
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

**Sub-check 1: Phase-Architecture Severity Compliance (C-28)**

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

If no Phase 1 P0/P1 assignments exist, state: **"No Phase 1 P0/P1 exceptions. PASS."**

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

If no Phase 3 P3 assignments exist, state: **"No Phase 3 P3 exceptions. PASS."**

Confirm the INFERENCE RULE stated in Step 2C, verbatim-anchored at Step 4, and echoed
at Step 4B has been applied consistently. Compare the paraphrase from Step 2C against
the audit results:
State: **"INFERENCE RULE paraphrase (Step 2C): [quote first 10 words of your Step 2C paraphrase].
Verbatim anchor at Step 4: YES. Echo at Step 4B: YES.
Audit result -- Phase 1 P2/P3 compliance: [PASS/FAIL].
Audit result -- Phase 3 P0/P1 compliance: [PASS/FAIL].
Paraphrase consistent with audit results: YES / NO."**

**Sub-check 2: Switching-Friction Sub-Section Field Completeness (C-29)**

Confirm the Switching-Friction Gaps sub-section from Step 7 is present.
Scan every entry for the `Migrating from:` field:
- List each entry's `Migrating from:` value.
- Flag any entry where the value does not contain the product name from Step 1b verbatim.
State: **"Switching-Friction Gaps sub-section present: YES. Migrating from: fields --
[entry 1: value | entry 2: value | ...]. All fields populated with product name
verbatim: YES / NO. Missing or non-verbatim entries: [list or NONE]."**

State final: **"All Step 4 values match Step 5. Exception sign-offs complete.
Sub-checks 1 and 2 verified. Verbatim anchor confirmed at Step 4. Echo confirmed at Step 4B."**
Name and correct any issue before finalizing.
```

---

## V-05: Full Synthesis -- Verbatim Anchor (V-01) + Grounds-to-Paraphrase Citation (V-02) + Step 4B Echo (V-03) + Part C Text-Match Confirmation

**Axes**: All three single-axis mechanisms combined, plus a fourth mechanism added exclusively in V-05: Part C sub-check 1 closes the text chain by confirming the verbatim text in the Step 4 confirmed block matches the Step 2C paraphrase first sentence character-for-character. The four mechanisms together form a closed loop: (1) paraphrase committed at Step 2C with "do not proceed" gate; (2) verbatim first sentence quoted at Step 4 header before severity column, forcing retrieval not fresh generation; (3) quoted text echoed at Step 4B before constraint 5 scan; (4) each exception's Grounds field cites the governing paraphrase clause; (5) Part C sub-check 1 quotes both the 2C paraphrase first sentence and the Step 4 verbatim anchor side by side and confirms they match.

**Hypothesis**: C-34 requires double-gate with "restate from 2C" cross-reference; C-35 requires Part C to quote the 2C paraphrase and confirm audit consistency. The C-35 consistency check is directional (did the audit find what the paraphrase predicted?) but not textual (does the Step 4 confirmed block contain the same text as the 2C paraphrase?). Without a text-match check, a model can produce a paraphrase at 2C, produce a different paraphrase at Step 4, satisfy the "restate from 2C" label by virtue of topical similarity, and satisfy the Part C consistency check by virtue of correct audit outcomes -- never proving the two paraphrases are the same commitment. The verbatim anchor at Step 4 makes retrieval testable; the text-match confirmation in Part C makes divergence structurally self-exposing. A model that produced different paraphrases at 2C and Step 4 cannot pass the text-match check without explicitly flagging the divergence or fabricating a match. The Grounds-to-paraphrase citation in exception blocks connects every deviation to the specific clause in the paraphrase chain, making the entire inference-rule commitment auditable from end to end.

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
be verbatim-anchored at Step 4, echoed at Step 4B, and text-matched in Pass 2 Part C.
Write a genuine restatement -- not a copy of the rule above. The first sentence of your
paraphrase is the anchor sentence: it will be quoted verbatim at Step 4 and Step 4B:

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
Do not fill the table until both fields are written:

```
INFERENCE RULE (confirmed):
  Verbatim anchor from 2C: "[quote your exact first sentence from the INFERENCE RULE
  (stated) block in Step 2C -- copy it word for word, do not paraphrase]"
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

Before running constraint 5, echo the verbatim anchor from Step 4:

```
INFERENCE RULE (4B echo): [copy the "Verbatim anchor from 2C" text from INFERENCE RULE
(confirmed) in Step 4 -- the quoted first sentence -- verbatim, unchanged]
```

Audit five constraints before writing any card body:

1. **Phase distribution** -- at least two Phase 1 rows and one Phase 3 row.
2. **Category spread** -- at least three distinct category values.
3. **Volume distribution** -- all three volume levels present.
4. **Phase-character compliance** -- each row's volume and severity match Step 2 ranges.
5. **Inference-rule compliance** -- apply the INFERENCE RULE echoed above:
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

**Sub-check 1: Phase-Architecture Severity Compliance (C-28)**

Scan Phase 1 rows in the vocabulary table (Step 4):
- List every Phase 1 ticket assigned P0 or P1.
- For each, fill an EXCEPTION SIGN-OFF BLOCK (5 fields required):

```
EXCEPTION SIGN-OFF:
Ticket ID: [T-NN]
Phase: 1
Assigned severity: [P0 or P1]
Grounds: [outage-level? YES / NO -- state the outage or blocking condition]
Paraphrase clause: [quote the clause from your Step 2C INFERENCE RULE (stated) block
  that governs Phase 1 severity -- the specific phrase that permits or prohibits P0/P1]
Disposition: [VALID EXCEPTION -- grounds match paraphrase clause | VIOLATION -- corrected to P2/P3]
```

If no Phase 1 P0/P1 assignments exist:
State: **"No Phase 1 P0/P1 exceptions. PASS."**
State also: **"Governing paraphrase clause for Phase 1: [quote the Phase 1 clause
  from your Step 2C paraphrase]."**

Scan Phase 3 rows in the vocabulary table (Step 4):
- List every Phase 3 ticket assigned P3.
- For each, fill an EXCEPTION SIGN-OFF BLOCK (5 fields required):

```
EXCEPTION SIGN-OFF:
Ticket ID: [T-NN]
Phase: 3
Assigned severity: P3
Grounds: [non-blocking issue? YES / NO -- state the non-blocking condition]
Paraphrase clause: [quote the clause from your Step 2C INFERENCE RULE (stated) block
  that governs Phase 3 severity -- the specific phrase that permits or prohibits P3]
Disposition: [VALID EXCEPTION -- grounds match paraphrase clause | VIOLATION -- corrected to P1/P0]
```

If no Phase 3 P3 assignments exist:
State: **"No Phase 3 P3 exceptions. PASS."**
State also: **"Governing paraphrase clause for Phase 3: [quote the Phase 3 clause
  from your Step 2C paraphrase]."**

Confirm the paraphrase chain is internally consistent across Step 2C, Step 4, and Step 4B:
State: **"Step 2C INFERENCE RULE (stated) -- first sentence: [quote verbatim].
Step 4 INFERENCE RULE (confirmed) -- Verbatim anchor: [quote verbatim].
Step 4B INFERENCE RULE (4B echo): [quote verbatim].
Text-match Step 2C vs Step 4 anchor: [MATCH / DIVERGENCE -- identify deviation].
Text-match Step 4 anchor vs Step 4B echo: [MATCH / DIVERGENCE -- identify deviation].
Audit result -- Phase 1 P2/P3 compliance: [PASS/FAIL].
Audit result -- Phase 3 P0/P1 compliance: [PASS/FAIL].
Paraphrase chain consistent with audit results: YES / NO."**

If any text divergence is found, state the divergence explicitly and correct the offending
block to match the Step 2C paraphrase before finalizing.

**Sub-check 2: Switching-Friction Sub-Section Field Completeness (C-29)**

Confirm the Switching-Friction Gaps sub-section from Step 7 is present.
Scan every entry for the `Migrating from:` field:
- List each entry's `Migrating from:` value.
- Flag any entry where the value does not contain the product name from Step 1b verbatim.
State: **"Switching-Friction Gaps sub-section present: YES. Migrating from: fields --
[entry 1: value | entry 2: value | ...]. All fields populated with product name
verbatim: YES / NO. Missing or non-verbatim entries: [list or NONE]."**

State final: **"All Step 4 values match Step 5. Exception sign-offs complete with
paraphrase clause citations. Sub-checks 1 and 2 verified. Verbatim anchor at Step 4.
Echo at Step 4B. Text-match confirmed across 2C, Step 4, and Step 4B. Paraphrase
chain consistent with audit results."**
Name and correct any issue before finalizing.
```

---

## Variation Summary

| Variation | Step 4 anchor mode | Exception block fields | Step 4B echo | Part C text-match | Potential new criteria |
|-----------|-------------------|----------------------|--------------|-------------------|------------------------|
| V-01 | Verbatim first-sentence quote from 2C (hard retrieval) | 4 fields (existing) | Absent | Absent | C-36: Step 4 confirmed block must verbatim-quote 2C paraphrase first sentence |
| V-02 | Free restatement (R10 V-05) | 5 fields: Grounds + Paraphrase clause | Absent | Absent | C-37: Exception SIGN-OFF BLOCK Grounds cites governing paraphrase clause |
| V-03 | Free restatement (R10 V-05) | 4 fields (existing) | Present -- echoes confirmed text before constraint 5 | Absent | C-38: Step 4B echoes confirmed paraphrase text verbatim before inference-rule compliance scan |
| V-04 | Verbatim first-sentence quote from 2C | 4 fields (existing) | Present -- echoes verbatim anchor text | Absent | C-36 + C-38 combined |
| V-05 | Verbatim first-sentence quote from 2C | 5 fields: Grounds + Paraphrase clause | Present -- echoes verbatim anchor text | Present -- quotes 2C, Step 4, Step 4B side-by-side and flags divergence | C-36 + C-37 + C-38 + C-39: full text-chain verification |

**Expected C-36 outcomes (verbatim anchor)**:
- V-01: PASS -- explicit "Verbatim from 2C:" field with copy instruction forces retrieval
- V-02: FAIL -- free restatement; model can satisfy "restate from 2C" by generating consistent content without retrieving exact text
- V-03: FAIL -- same as V-02
- V-04: PASS -- same mechanism as V-01
- V-05: PASS + strongest -- verbatim anchor produced, then echoed at Step 4B, then text-matched in Part C

**Expected C-37 outcomes (Grounds-to-paraphrase citation)**:
- V-01: FAIL -- four-field exception block; Grounds states outage/non-blocking without citing paraphrase clause
- V-02: PASS -- five-field block; Paraphrase clause field forces citation of governing clause for every exception
- V-03: FAIL -- four-field exception block; no paraphrase clause field
- V-04: FAIL -- four-field exception block; no paraphrase clause field
- V-05: PASS + strongest -- five-field block with paraphrase clause citation; governing clauses also quoted on the no-exception path

**Expected C-38 outcomes (Step 4B echo)**:
- V-01: FAIL -- no 4B echo block; constraint 5 operates with paraphrase as upstream label, not live text
- V-02: FAIL -- no 4B echo block
- V-03: PASS -- explicit `INFERENCE RULE (4B echo):` block placed immediately before constraint 5
- V-04: PASS -- same mechanism as V-03, with verbatim anchor as the echoed text
- V-05: PASS + strongest -- 4B echo of verbatim anchor, then Part C confirms echo text matches 2C paraphrase

**Expected C-39 outcomes (Part C text-match)**:
- V-01: FAIL -- Part C quotes first 10 words of 2C paraphrase but does not compare against Step 4 verbatim anchor
- V-02: FAIL -- no text-match; Part C paraphrase consistency is directional (audit result matches paraphrase direction), not textual
- V-03: FAIL -- no text-match
- V-04: FAIL -- no text-match; verbatim anchor and echo are present but not cross-verified in Part C
- V-05: PASS -- Part C quotes 2C, Step 4 anchor, and Step 4B echo side by side, states MATCH or DIVERGENCE for each pair, and requires correction before finalizing if any divergence found
