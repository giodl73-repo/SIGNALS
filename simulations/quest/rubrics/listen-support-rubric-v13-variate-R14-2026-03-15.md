# listen-support Round 14 -- Skill Body Prompt Variations

**Rubric target**: v13 (255 pts)
**New criteria in scope**: C-40 (Exception Block Verbatim-Clause Instruction), C-41 (Imperative Dual-Field Gate Language)
**Base**: All prior mechanisms from R13 V-04 (C-01 through C-39 at ceiling, C-40/C-41 split across R13 variations)

**Variation axes selected** (3 single-axis, then 2 combined):
1. **Exception block verbatim instruction tightening** -- C-40 direct fix from R13 V-04 base; all other mechanisms preserved (V-01)
2. **Output format** -- numbered checklist replaces fenced code block for Step-4 gate; imperative prohibition maintained (V-02)
3. **Lifecycle emphasis** -- phase-separated exception blocks with lifecycle framing fields; C-39+C-41 dropped to isolate axis (V-03)
4. **V-01 + V-02 combined** -- tightest verbatim instruction + numbered checklist format + competitor name gate at Step 4 (V-04)
5. **Full synthesis** -- all six criteria + conversational register + inertia framing gates at Steps 4 and 5 (V-05)

**R14 coverage matrix:**

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-36 (exception paraphrase-clause field) | YES | YES | YES | YES | YES |
| C-37 (verbatim anchor at Step 4) | YES | YES | YES | YES | YES |
| C-38 (dual-field "both lines" gate) | YES | YES | YES | YES | YES |
| C-39 (every-assignment scope confirmation) | YES | YES | -- | YES | YES |
| C-40 (verbatim instruction in exception block) | YES | YES | YES | YES | YES |
| C-41 (imperative dual-field gate language) | YES | YES | -- | YES | YES |

---

## V-01: Single-Axis -- Exception Block Verbatim-Clause Instruction (C-40 Direct Fix)

**Axis**: Exception block Paraphrase clause instruction tightening. The Paraphrase clause field in every EXCEPTION SIGN-OFF BLOCK is upgraded from a faithful-restatement instruction ("quote the specific clause") to an explicit string-retrieval mandate: "do not paraphrase, do not summarize, copy it verbatim word-for-word from your Step 2C block." The no-exception path likewise carries a verbatim mandate. All other mechanisms from R13 V-04 are preserved without modification: dual-field Step-4 gate (C-37+C-38), scope confirmation (C-39), imperative prohibition form "Do not fill the table until both lines are written" (C-41), and 6-field exception block (C-36).

**Hypothesis**: R13 V-04 scored 250/255 failing only C-40. The Paraphrase clause field was present and instructed the model to "quote the specific clause" -- a faithful-restatement requirement that permits the model to select wording. C-40 requires the instruction to mandate verbatim reproduction, converting the field from "I must faithfully represent this clause" to "I must reproduce this clause character-for-character." The upgrade: adding "do not paraphrase, do not summarize, copy it verbatim word-for-word" makes the Paraphrase clause a string-retrieval requirement. A scorer can verify compliance by string comparison without semantic interpretation. V-01 tests whether this minimal surgical addition to R13 V-04 achieves ceiling.

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
Paraphrase clause: [copy the exact clause from your INFERENCE RULE (stated) at Step 2C
  that governs this phase-severity decision -- do not paraphrase, do not summarize,
  copy it verbatim word-for-word from your Step 2C block]
Disposition: [VALID EXCEPTION -- reason | VIOLATION -- corrected to P2/P3]
```

If no Phase 1 P0/P1 assignments exist, state:
**"No Phase 1 P0/P1 exceptions. Governing paraphrase clause for Phase 1: [copy the
exact Phase 1 clause from your INFERENCE RULE (stated) at Step 2C verbatim --
do not paraphrase]."**

Scan Phase 3 rows in the vocabulary table (Step 4):
- List every Phase 3 ticket assigned P3.
- For each, fill an EXCEPTION SIGN-OFF BLOCK:

```
EXCEPTION SIGN-OFF:
Ticket ID: [T-NN]
Phase: 3
Assigned severity: P3
Grounds: [non-blocking issue? YES / NO]
Paraphrase clause: [copy the exact clause from your INFERENCE RULE (stated) at Step 2C
  that governs this phase-severity decision -- do not paraphrase, do not summarize,
  copy it verbatim word-for-word from your Step 2C block]
Disposition: [VALID EXCEPTION -- reason | VIOLATION -- corrected to P1/P0]
```

If no Phase 3 P3 assignments exist, state:
**"No Phase 3 P3 exceptions. Governing paraphrase clause for Phase 3: [copy the
exact Phase 3 clause from your INFERENCE RULE (stated) at Step 2C verbatim --
do not paraphrase]."**

Confirm the INFERENCE RULE stated in Step 2C and confirmed at Step 4 has been
applied consistently. Compare the paraphrase from Step 2C against the audit results:
State: **"INFERENCE RULE paraphrase (Step 2C): [quote first 10 words of your Step 2C paraphrase].
Verbatim anchor at Step 4: YES.
Scope confirmation at Step 4: YES. [This rule applies to every severity assignment in the table.]
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

## V-02: Single-Axis -- Output Format (Numbered Checklist for Step-4 Gate)

**Axis**: Output format -- the Step-4 dual-field pre-commitment gate is presented as a numbered checklist with an explicit "Required before table:" header, replacing the fenced code block format of all prior variations. Each field is a numbered item. The imperative prohibition is reformulated as "Do not fill any cell until both items above are complete." Exception block uses numbered field labels (1-6) instead of named fields in sequence. C-40 verbatim instruction is carried in item 5. C-39 scope confirmation follows both items as a declarative closure. C-41 imperative prohibition is preserved in the "Do not fill" form.

**Hypothesis**: The fenced code block format in prior variations presents the dual fields as a template-to-fill, which may encourage mechanical copying rather than genuine restatement. A numbered checklist makes the two-field requirement more cognitively explicit: the model must complete item 1 (own-words restatement) and item 2 (verbatim retrieval) as distinct checklist actions before proceeding. C-38 requires two distinct labeled fields with "both fields/lines" instruction; numbered items satisfy the "distinct labeled" requirement while the "Do not fill any cell until both items above are complete" satisfies the imperative prohibition. The format change tests whether presentation affects compliance quality independently of the instruction content.

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
- For each, fill an EXCEPTION SIGN-OFF BLOCK using numbered fields:

```
EXCEPTION SIGN-OFF:
  1. Ticket ID: [T-NN]
  2. Phase: 1
  3. Assigned severity: [P0 or P1]
  4. Grounds: [outage-level? YES / NO]
  5. Paraphrase clause: [copy the exact clause from your INFERENCE RULE (stated) at Step 2C
       that governs this phase-severity decision -- copy it verbatim from your Step 2C block,
       do not paraphrase]
  6. Disposition: [VALID EXCEPTION -- reason | VIOLATION -- corrected to P2/P3]
```

If no Phase 1 P0/P1 assignments exist, state:
**"No Phase 1 P0/P1 exceptions. Governing paraphrase clause for Phase 1: [copy the
exact Phase 1 clause from your INFERENCE RULE (stated) at Step 2C verbatim --
do not paraphrase]."**

Scan Phase 3 rows in the vocabulary table (Step 4):
- List every Phase 3 ticket assigned P3.
- For each, fill an EXCEPTION SIGN-OFF BLOCK using numbered fields:

```
EXCEPTION SIGN-OFF:
  1. Ticket ID: [T-NN]
  2. Phase: 3
  3. Assigned severity: P3
  4. Grounds: [non-blocking issue? YES / NO]
  5. Paraphrase clause: [copy the exact clause from your INFERENCE RULE (stated) at Step 2C
       that governs this phase-severity decision -- copy it verbatim from your Step 2C block,
       do not paraphrase]
  6. Disposition: [VALID EXCEPTION -- reason | VIOLATION -- corrected to P1/P0]
```

If no Phase 3 P3 assignments exist, state:
**"No Phase 3 P3 exceptions. Governing paraphrase clause for Phase 3: [copy the
exact Phase 3 clause from your INFERENCE RULE (stated) at Step 2C verbatim --
do not paraphrase]."**

Confirm the INFERENCE RULE stated in Step 2C and confirmed at Step 4 has been
applied consistently. Compare the paraphrase from Step 2C against the audit results:
State: **"INFERENCE RULE paraphrase (Step 2C): [quote first 10 words of your Step 2C paraphrase].
Verbatim anchor at Step 4 (Required item 2): YES.
Scope confirmation at Step 4: YES. [This rule applies to every severity assignment in the table.]
Verbatim instruction in exception block Paraphrase clause (item 5): YES. [Governing clause copied
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

## V-03: Single-Axis -- Lifecycle Emphasis (Phase-Separated Exception Blocks, C-39+C-41 dropped)

**Axis**: Lifecycle emphasis -- Phase 1 and Phase 3 exception blocks are structurally differentiated with lifecycle framing fields. Each phase's exception block opens with a named "Fallback status:" field that restates the lifecycle position before Grounds is evaluated: Phase 1 blocks carry "Fallback status: Inertia competitor still in active use (fallback available)"; Phase 3 blocks carry "Fallback status: Inertia competitor out of daily workflow (no fallback)". The no-exception path likewise names the lifecycle position. C-39 (scope confirmation) is dropped. C-41 imperative gate is dropped in favor of declarative form, to isolate the lifecycle emphasis axis.

**Hypothesis**: Prior variations required the model to recall the fallback rationale implicitly from the Step 2C paraphrase. By embedding the fallback status as a named field in each exception block, the block becomes self-documenting: a scorer verifying Grounds can see the phase, the fallback state, and the governing clause in one view without cross-referencing the inference rule. The lifecycle framing fields test whether making the severity rationale explicit in each block improves Grounds quality independently of gate-form changes. C-39 and C-41 are dropped to isolate this axis: the only new structural element is the lifecycle framing field.

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
| Phase 1 | Day 0-30 | P2/P3 -- fallback available | high |
| Phase 2 | Day 31-60 | P1/P2 -- transition window | medium |
| Phase 3 | Day 61-90 | P0/P1 -- no fallback | medium/low |

Lifecycle rationale:
- Phase 1: The inertia competitor is still open. Friction is expected. Fallback exists.
  Severity is lower because the user is not blocked -- they can return to the old tool.
- Phase 2: Migration is in progress. The competitor may still be available in some workflows.
  Severity rises as commitment increases.
- Phase 3: The user has committed to the new product. The competitor is out of daily workflow.
  Blocking issues have no fallback. Severity is highest.

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
Both of the following lines must be written before any row in the table is populated:

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
4. **Phase-character compliance** -- each row's volume and severity match Step 2 ranges
   and the lifecycle rationale (Phase 1 = fallback available, Phase 3 = no fallback).
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

## V-04: Combined (V-01 + V-02) -- Tightest Verbatim + Numbered Format + Competitor Gate

**Axes combined**: V-01's tightest verbatim mandate in exception block (C-40) with V-02's numbered checklist format for Step-4 gate (C-38 output format). Additionally: a competitor name gate at Step 4 header (from R12 V-03) anchors the product name immediately before the severity table. All six criteria are targeted: C-36 (exception Paraphrase clause field), C-37 (verbatim anchor), C-38 (dual-field "both items" gate with imperative), C-39 (scope confirmation), C-40 (verbatim instruction in Paraphrase clause), C-41 (imperative: "Do not fill any cell until both items are complete").

**Hypothesis**: V-01 fixes C-40 in isolation; V-02 tests whether numbered checklist format improves compliance. The combination tests two independent structural changes simultaneously -- format and verbatim mandate depth -- to determine if they compound or interfere. The competitor gate at Step 4 header (from R12 V-03) re-anchors the product name in generation context immediately before severity assignment, reducing tool-name fidelity drift across eight cards. The three additions (verbatim mandate, numbered format, competitor gate) all operate in distinct instruction slots and should not compete. V-04 tests whether ceiling is reachable with this combined structure.

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
- For each, fill an EXCEPTION SIGN-OFF BLOCK using numbered fields:

```
EXCEPTION SIGN-OFF:
  1. Ticket ID: [T-NN]
  2. Phase: 1
  3. Assigned severity: [P0 or P1]
  4. Grounds: [outage-level? YES / NO]
  5. Paraphrase clause: [copy the exact clause from your INFERENCE RULE (stated) at Step 2C
       that governs this phase-severity decision -- do not paraphrase, do not summarize,
       copy it verbatim word-for-word from your Step 2C block]
  6. Disposition: [VALID EXCEPTION -- reason | VIOLATION -- corrected to P2/P3]
```

If no Phase 1 P0/P1 assignments exist, state:
**"No Phase 1 P0/P1 exceptions. Governing paraphrase clause for Phase 1: [copy the
exact Phase 1 clause from your INFERENCE RULE (stated) at Step 2C verbatim --
do not paraphrase]."**

Scan Phase 3 rows in the vocabulary table (Step 4):
- List every Phase 3 ticket assigned P3.
- For each, fill an EXCEPTION SIGN-OFF BLOCK using numbered fields:

```
EXCEPTION SIGN-OFF:
  1. Ticket ID: [T-NN]
  2. Phase: 3
  3. Assigned severity: P3
  4. Grounds: [non-blocking issue? YES / NO]
  5. Paraphrase clause: [copy the exact clause from your INFERENCE RULE (stated) at Step 2C
       that governs this phase-severity decision -- do not paraphrase, do not summarize,
       copy it verbatim word-for-word from your Step 2C block]
  6. Disposition: [VALID EXCEPTION -- reason | VIOLATION -- corrected to P1/P0]
```

If no Phase 3 P3 assignments exist, state:
**"No Phase 3 P3 exceptions. Governing paraphrase clause for Phase 3: [copy the
exact Phase 3 clause from your INFERENCE RULE (stated) at Step 2C verbatim --
do not paraphrase]."**

Confirm the INFERENCE RULE stated in Step 2C and confirmed at Step 4 has been
applied consistently. Compare the paraphrase from Step 2C against the audit results:
State: **"INFERENCE RULE paraphrase (Step 2C): [quote first 10 words of your Step 2C paraphrase].
Verbatim anchor at Step 4 (Required item 2): YES.
Scope confirmation at Step 4: YES. [This rule applies to every severity assignment in the table.]
Verbatim instruction in exception block Paraphrase clause (item 5): YES. [Governing clause
copied word-for-word from Step 2C; no paraphrase permitted.]
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

## V-05: Full Synthesis -- All Six Criteria + Conversational Register + Inertia Framing Gates

**Axes combined**: V-01's tightest verbatim mandate (C-40) + imperative prohibition at Step 4 (C-41) + all prior criteria (C-36/37/38/39) + conversational register from R13 V-03/V-05 + inertia framing gates at Steps 4 and 5 (from R12 V-03). This is the ceiling variation for R14: six criteria in a conversational register with embedded competitor-name re-anchoring. The Step-4 gate uses imperative prohibition in conversational voice. The exception block Paraphrase clause carries the full verbatim mandate in conversational framing.

**Hypothesis**: All six criteria are register-independent structural mechanisms: labeled fields, code blocks, imperative sentences. Conversational framing should not degrade any criterion's satisfiability -- it affects prose sections (1a, 3, 2C rationale) without touching the structural templates. C-41 is the most register-sensitive criterion: the imperative prohibition "Do not fill the table until both lines are written" reads as direct and unconditional in both formal and conversational registers. The inertia gates at Steps 4 and 5 (writing the competitor name before each generation step) test whether competitor-name density affects scoring on tool-name fidelity criteria independent of gate-form changes. V-05 tests whether all six criteria survive the full combination.

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

Before you fill any severity cell, look back at what you wrote in Step 2C.
Do not fill the table until both lines are written:

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
not "the tool", not "my old system". This name must appear verbatim in every Phase 1
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

### Doc Gaps
[At least one documentation gap.]

### Design Gaps
[At least one design gap.]

### Operational Gaps
[At least one operational gap.]

### Switching-Friction Gaps
This sub-section covers migration barriers only. It is separate from the three
sections above -- not absorbed into any of them. At least one entry required.
At least two are recommended.

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
Paraphrase clause: [copy the exact clause from your INFERENCE RULE (stated) at Step 2C
  that governs this phase-severity decision -- do not paraphrase, do not summarize,
  copy it verbatim word-for-word from your Step 2C block]
Disposition: [VALID EXCEPTION -- reason | VIOLATION -- corrected to P2/P3]
```

If no Phase 1 P0/P1 assignments exist, state:
**"No Phase 1 P0/P1 exceptions. Governing paraphrase clause for Phase 1: [copy the
exact Phase 1 clause from your INFERENCE RULE (stated) at Step 2C verbatim --
do not paraphrase]."**

Scan Phase 3 rows in the vocabulary table (Step 4):
- List every Phase 3 ticket assigned P3.
- For each, fill an EXCEPTION SIGN-OFF BLOCK:

```
EXCEPTION SIGN-OFF:
Ticket ID: [T-NN]
Phase: 3
Assigned severity: P3
Grounds: [non-blocking issue? YES / NO]
Paraphrase clause: [copy the exact clause from your INFERENCE RULE (stated) at Step 2C
  that governs this phase-severity decision -- do not paraphrase, do not summarize,
  copy it verbatim word-for-word from your Step 2C block]
Disposition: [VALID EXCEPTION -- reason | VIOLATION -- corrected to P1/P0]
```

If no Phase 3 P3 assignments exist, state:
**"No Phase 3 P3 exceptions. Governing paraphrase clause for Phase 3: [copy the
exact Phase 3 clause from your INFERENCE RULE (stated) at Step 2C verbatim --
do not paraphrase]."**

Check that what you wrote in INFERENCE RULE (confirmed) and the verbatim anchor at Step 4
is consistent with the ticket severity assignments you just scanned.
State: **"INFERENCE RULE paraphrase (Step 2C): [quote first 10 words of your Step 2C paraphrase].
Verbatim anchor at Step 4: YES.
Scope confirmation at Step 4: YES. [This rule applies to every severity assignment in the table.]
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
