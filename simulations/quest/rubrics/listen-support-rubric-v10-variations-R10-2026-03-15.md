# listen-support Round 10 — Skill Body Prompt Variations

**Rubric target**: v10 (205 pts)
**New criteria in scope**: C-30 (Inference Rule Paraphrase-Before-Proceed Gate), C-31 (Inference Audit in Dual-Pass Part C)
**Base**: All prior mechanisms from R9 V-05 (C-01 through C-29 at ceiling)

**Variation axes selected** (3 single-axis, then 2 combined):
1. **C-30 gate language** — named block present but no explicit "do not proceed" gate instruction (weak) vs. hard gate with gating language (strong) — (V-01 weak, V-05 strong)
2. **C-30 gate placement** — end of STEP 2C (upstream) vs. STEP 4 header (decision-adjacent, immediately before severity column) — (V-02 Step 4)
3. **C-31 Part C coverage** — sub-check (1) only [inference scan] vs. both sub-checks [(1) inference scan + (2) field completeness] — (V-03 partial)
4. **C-30 Step 4 placement + C-31 structured exception sign-off block** combined — (V-04)
5. **Full synthesis**: C-30 hard gate at STEP 2C + paraphrase recall at Step 4 + C-31 both sub-checks + structured exception block + paraphrase-consistency confirmation — (V-05)

---

## V-01: Single-Axis — C-30 Named Block Without Gate Language (Weak Paraphrase Demand)

**Axis**: C-30 gate strength — weak. STEP 2C includes the `INFERENCE RULE (stated):` named block, but without any explicit gate instruction ("Do not proceed to Step 3 until this block is filled"). The block is present and labeled, but the model can fill it and move on without a hard stop. All other mechanisms from R9 V-05 are preserved.

**Hypothesis**: Without explicit gate language, the model treats the paraphrase block as a formatting requirement rather than a structural gate. It will echo the rule text verbatim or with minimal rephrasing, satisfying the surface requirement of the named block but not demonstrating genuine re-encoding. C-30 requires a paraphrase gate — demonstrated encoding, not verbatim copy — and the absence of gate language is the single structural change that makes this variation fall short of C-30 while satisfying everything else.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 — INERTIA: STATUS QUO

Establish the current-state baseline and name the inertia competitor.

**1a. Current-state baseline**
Describe in 2–3 sentences: what are users doing today to accomplish the job
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

## STEP 2 — PHASE MAP TABLE

| Phase | Window | Expected severity range | Expected volume character |
|-------|--------|------------------------|--------------------------|
| Phase 1 | Day 0–30 | P2/P3 | high |
| Phase 2 | Day 31–60 | P1/P2 | medium |
| Phase 3 | Day 61–90 | P0/P1 | medium/low |

---

## STEP 2B — PHASE BODY TEMPLATE TABLE

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

## STEP 2C — PHASE-SEVERITY INFERENCE RULE

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

**Violation conditions (apply in Step 4B):**
- Phase 1 P0 or P1 on a non-outage ticket: violation — correct to P2/P3.
- Phase 3 P3 on a ticket where the user cannot complete a task: violation — correct to P1/P0.

**State the rule in your own words:**

```
INFERENCE RULE (stated): [write the directional rule in your own words]
Applied in: Steps 4, 4B, and Pass 2 INFERENCE AUDIT
```

---

## STEP 3 — PERFORMANCE MODE DECLARATION

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

## STEP 4 — VOCABULARY PRE-COMMITMENT TABLE

The INFERENCE RULE from Step 2C governs severity assignments here.
Phase 1 = P2/P3 (fallback available). Phase 3 = P0/P1 when blocking (fallback gone).

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

## STEP 4B — COLLECTIVE DISTRIBUTION AUDIT

Audit five constraints before writing any card body:

1. **Phase distribution** — at least two Phase 1 rows and one Phase 3 row.
2. **Category spread** — at least three distinct category values.
3. **Volume distribution** — all three volume levels present.
4. **Phase-character compliance** — each row's volume and severity match Step 2 ranges.
5. **Inference-rule compliance** — apply the INFERENCE RULE from Step 2C:
   - Scan Phase 1 rows: flag any P0 or P1 assignment on a non-outage ticket.
   - Scan Phase 3 rows: flag any P3 assignment on a blocking ticket.
   - State PASS if no violations; FAIL and name the row and correction if any found.

State PASS or FAIL per constraint.
**If any fails, correct the table and re-run. Name the correction.**

---

## STEP 5 — FULL CARD BODIES

For each row in the summary table:

```
Ticket ID: [T-NN]
Title: [descriptive title]
Category: [must match Step 4 exactly]
Persona: [must match Step 4 exactly]
Volume: [must match Step 4 exactly]
Severity: [must match Step 4 exactly]

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
```

---

## STEP 6 — CROSS-TICKET PATTERNS

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

## STEP 7 — GAP ANALYSIS

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
Migrating from: [product name from Step 1b — verbatim, grep-checkable]
Expected behavior: [one sentence — what users expected, based on the competitor's behavior]
Actual behavior: [one sentence — what this product actually does or fails to do]
Migration impact: [one sentence — what users must change, lose, or manually replicate]
```

Rules:
- `Migrating from:` MUST contain the product name from Step 1b verbatim.
  Prohibited: `Migrating from: existing tool`, `Migrating from: legacy workflow`.
- `Expected behavior:` and `Actual behavior:` define the behavior delta —
  they describe the same capability from two perspectives.
- Every entry must be independently enumerable: a reader scanning only this sub-section
  must be able to identify the competitor, the behavior delta, and the migration cost
  without reading any other part of the output.

### Pre-Launch Priority
Name the single gap to close first. Tie to specific ticket IDs, severity, and volume.
State whether it reduces switching-friction for inertia-competitor migrants.

---

## STEP 8 — DUAL-PASS VERIFICATION

### PASS 1 — Coverage Trace Table

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
1. Confirm: **"No gap from the Gap Analysis — including switching-friction gaps —
   is absent from this table."**
2. Confirm: **"The inertia competitor product name appears in at least two
   STATUS QUO element cells."**

END OF PASS 1. Switch to verification mode for properties and inference audit.

### PASS 2 — Properties Verify + Inference Audit

**PART A — Frontmatter Verify**

Confirm the summary table from Step 4 matches every Ticket ID, Phase, Category,
Persona, Volume, and Severity in the full card bodies from Step 5.
State: **"All Step 4 values match Step 5 card bodies."**

**PART B — Property Checks**

1. **Tool-name fidelity** — product name from Step 1b appears verbatim in Step 1b,
   at least two card bodies, and at least one `Migrating from:` field.
   State: **"[PRODUCT NAME] in Step 1b: YES. Card bodies: T-NN, T-NN (minimum).
   Migrating from: field: YES."**

2. **Phase-differentiated templates** — at least two Phase 1 bodies contain the
   Phase 1 template from Step 2B, and at least one Phase 3 body contains the Phase 3 template.
   State: **"Phase 1 template in: T-NN, T-NN. Phase 3 template in: T-NN."**

3. **Switching-friction 4-field format** — every entry in the Switching-Friction Gaps
   sub-section contains all four fields. Scan each entry for: Migrating from, Expected
   behavior, Actual behavior, Migration impact.
   State: **"All four fields present in all entries: YES / NO. Missing: [field list or NONE]."**

**PART C — Inference Audit**

Scan Phase 1 rows in the vocabulary table (Step 4):
- List every Phase 1 ticket assigned P0 or P1.
- For each: state whether this is an outage-level ticket. If yes, the assignment stands.
  If no, name the violation and correct it.
State: **"Phase 1 P0/P1 assignments: [list or NONE]. Violations: [list or NONE]."**

Scan Phase 3 rows in the vocabulary table (Step 4):
- List every Phase 3 ticket assigned P3.
- For each: state whether this is a non-blocking issue. If yes, state the reasoning.
  If no (it blocks a committed user), name the violation and correct it.
State: **"Phase 3 P3 assignments: [list or NONE]. Violations: [list or NONE]."**

Confirm the INFERENCE RULE stated in Step 2C has been applied consistently:
State: **"INFERENCE RULE compliance confirmed. Phase 1 → lower severity (fallback available):
[PASS/FAIL]. Phase 3 → higher severity (fallback gone, committed user): [PASS/FAIL]."**

Confirm the Switching-Friction Gaps sub-section from Step 7 exists and every entry's
`Migrating from:` field is populated with the product name from Step 1b verbatim.
State: **"Switching-Friction Gaps sub-section present: YES. All Migrating from: fields
populated with [PRODUCT NAME]: YES / NO. Missing entries: [list or NONE]."**

State final: **"All Step 4 values match Step 5. All properties and inference rule verified."**
Name and correct any issue before finalizing.
```

---

## V-02: Single-Axis — C-30 Paraphrase Gate Relocated to Step 4 Header (Decision-Adjacent)

**Axis**: C-30 gate placement — the paraphrase requirement moves from STEP 2C to the header of STEP 4, immediately before the model fills the severity column. STEP 2C contains the full rule text as an imperative (identical to V-04 from R9) but NO paraphrase block. The gate fires at the point of decision.

**Hypothesis**: Decision-adjacent placement creates tighter temporal coupling between stated understanding and application. When the model paraphrases the rule at the top of Step 4, the paraphrase is the immediately preceding generation context before severity values are filled. Upstream placement in STEP 2C forces the model to maintain the paraphrase commitment across STEP 3 and the Step 4 setup prose — the commitment can dissipate. At Step 4 the paraphrase is live. C-31 (Part C) is unchanged from R9 V-05, so this variation isolates whether placement alone changes C-30 compliance.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 — INERTIA: STATUS QUO

Establish the current-state baseline and name the inertia competitor.

**1a. Current-state baseline**
Describe in 2–3 sentences: what are users doing today to accomplish the job
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

## STEP 2 — PHASE MAP TABLE

| Phase | Window | Expected severity range | Expected volume character |
|-------|--------|------------------------|--------------------------|
| Phase 1 | Day 0–30 | P2/P3 | high |
| Phase 2 | Day 31–60 | P1/P2 | medium |
| Phase 3 | Day 61–90 | P0/P1 | medium/low |

---

## STEP 2B — PHASE BODY TEMPLATE TABLE

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

## STEP 2C — PHASE-SEVERITY INFERENCE RULE

Apply this rule when assigning severity in Step 4. Read and accept this rule before
proceeding to Step 3.

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

**Violation conditions (apply in Step 4B):**
- Phase 1 P0 or P1 on a non-outage ticket: violation — correct to P2/P3.
- Phase 3 P3 on a ticket where the user cannot complete a task: violation — correct to P1/P0.

---

## STEP 3 — PERFORMANCE MODE DECLARATION

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

## STEP 4 — VOCABULARY PRE-COMMITMENT TABLE

Before filling any severity cell, state the inference rule from Step 2C in your own words.
Do not fill the table until this line is written:

```
INFERENCE RULE (stated): [your paraphrase of the directional rule from Step 2C]
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

## STEP 4B — COLLECTIVE DISTRIBUTION AUDIT

Audit five constraints before writing any card body:

1. **Phase distribution** — at least two Phase 1 rows and one Phase 3 row.
2. **Category spread** — at least three distinct category values.
3. **Volume distribution** — all three volume levels present.
4. **Phase-character compliance** — each row's volume and severity match Step 2 ranges.
5. **Inference-rule compliance** — apply the INFERENCE RULE you stated above Step 4:
   - Scan Phase 1 rows: flag any P0 or P1 assignment on a non-outage ticket.
   - Scan Phase 3 rows: flag any P3 assignment on a blocking ticket.
   - State PASS if no violations; FAIL and name the row and correction if any found.

State PASS or FAIL per constraint.
**If any fails, correct the table and re-run. Name the correction.**

---

## STEP 5 — FULL CARD BODIES

For each row in the summary table:

```
Ticket ID: [T-NN]
Title: [descriptive title]
Category: [must match Step 4 exactly]
Persona: [must match Step 4 exactly]
Volume: [must match Step 4 exactly]
Severity: [must match Step 4 exactly]

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
```

---

## STEP 6 — CROSS-TICKET PATTERNS

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

## STEP 7 — GAP ANALYSIS

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
Migrating from: [product name from Step 1b — verbatim, grep-checkable]
Expected behavior: [one sentence — what users expected, based on the competitor's behavior]
Actual behavior: [one sentence — what this product actually does or fails to do]
Migration impact: [one sentence — what users must change, lose, or manually replicate]
```

Rules:
- `Migrating from:` MUST contain the product name from Step 1b verbatim.
  Prohibited: `Migrating from: existing tool`, `Migrating from: legacy workflow`.
- `Expected behavior:` and `Actual behavior:` define the behavior delta —
  they describe the same capability from two perspectives.
- Every entry must be independently enumerable: a reader scanning only this sub-section
  must be able to identify the competitor, the behavior delta, and the migration cost
  without reading any other part of the output.

### Pre-Launch Priority
Name the single gap to close first. Tie to specific ticket IDs, severity, and volume.
State whether it reduces switching-friction for inertia-competitor migrants.

---

## STEP 8 — DUAL-PASS VERIFICATION

### PASS 1 — Coverage Trace Table

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
1. Confirm: **"No gap from the Gap Analysis — including switching-friction gaps —
   is absent from this table."**
2. Confirm: **"The inertia competitor product name appears in at least two
   STATUS QUO element cells."**

END OF PASS 1. Switch to verification mode for properties and inference audit.

### PASS 2 — Properties Verify + Inference Audit

**PART A — Frontmatter Verify**

Confirm the summary table from Step 4 matches every Ticket ID, Phase, Category,
Persona, Volume, and Severity in the full card bodies from Step 5.
State: **"All Step 4 values match Step 5 card bodies."**

**PART B — Property Checks**

1. **Tool-name fidelity** — product name from Step 1b appears verbatim in Step 1b,
   at least two card bodies, and at least one `Migrating from:` field.
   State: **"[PRODUCT NAME] in Step 1b: YES. Card bodies: T-NN, T-NN (minimum).
   Migrating from: field: YES."**

2. **Phase-differentiated templates** — at least two Phase 1 bodies contain the
   Phase 1 template from Step 2B, and at least one Phase 3 body contains the Phase 3 template.
   State: **"Phase 1 template in: T-NN, T-NN. Phase 3 template in: T-NN."**

3. **Switching-friction 4-field format** — every entry in the Switching-Friction Gaps
   sub-section contains all four fields. Scan each entry for: Migrating from, Expected
   behavior, Actual behavior, Migration impact.
   State: **"All four fields present in all entries: YES / NO. Missing: [field list or NONE]."**

**PART C — Inference Audit**

Scan Phase 1 rows in the vocabulary table (Step 4):
- List every Phase 1 ticket assigned P0 or P1.
- For each: state whether this is an outage-level ticket. If yes, the assignment stands.
  If no, name the violation and correct it.
State: **"Phase 1 P0/P1 assignments: [list or NONE]. Violations: [list or NONE]."**

Scan Phase 3 rows in the vocabulary table (Step 4):
- List every Phase 3 ticket assigned P3.
- For each: state whether this is a non-blocking issue. If yes, state the reasoning.
  If no (it blocks a committed user), name the violation and correct it.
State: **"Phase 3 P3 assignments: [list or NONE]. Violations: [list or NONE]."**

Confirm the INFERENCE RULE stated in Step 4 (above the vocabulary table) has been
applied consistently in the severity assignments:
State: **"INFERENCE RULE compliance confirmed. Phase 1 → lower severity (fallback available):
[PASS/FAIL]. Phase 3 → higher severity (fallback gone, committed user): [PASS/FAIL]."**

Confirm the Switching-Friction Gaps sub-section from Step 7 exists and every entry's
`Migrating from:` field is populated with the product name from Step 1b verbatim.
State: **"Switching-Friction Gaps sub-section present: YES. All Migrating from: fields
populated with [PRODUCT NAME]: YES / NO. Missing entries: [list or NONE]."**

State final: **"All Step 4 values match Step 5. All properties and inference rule verified."**
Name and correct any issue before finalizing.
```

---

## V-03: Single-Axis — C-31 Part C Minimal (Inference Scan Only, No Field Completeness Sub-Check)

**Axis**: C-31 Part C audit coverage — minimal. Part C contains only sub-check (1): scan every ticket for C-28 directional compliance (Phase 1 P0/P1 violations, Phase 3 P3 violations) with exception acknowledgment. Sub-check (2) — confirm the Switching-Friction Gaps sub-section exists and all `Migrating from:` fields are populated — is NOT in Part C. Field completeness check is present in Part B but not re-verified as a Part C property. C-30 mechanisms from R9 V-05 (paraphrase gate at STEP 2C with "do not proceed" language) are preserved intact.

**Hypothesis**: Partial Part C satisfies C-31 sub-check (1) but misses sub-check (2). The rubric extraction rationale for C-31 explicitly names both: "(1) scan every ticket for C-28 directional compliance with exception acknowledgment gate, and (2) confirm the C-29 sub-section exists and all Migrating from: fields are populated." Without sub-check (2) in Part C, the field completeness property is verified only once (in Part B) and not as a Part C audit property. C-28 and C-29 are verified output properties only when both sub-checks live in Part C. This variation tests whether a single-sub-check Part C is sufficient for C-31.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 — INERTIA: STATUS QUO

Establish the current-state baseline and name the inertia competitor.

**1a. Current-state baseline**
Describe in 2–3 sentences: what are users doing today to accomplish the job
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

## STEP 2 — PHASE MAP TABLE

| Phase | Window | Expected severity range | Expected volume character |
|-------|--------|------------------------|--------------------------|
| Phase 1 | Day 0–30 | P2/P3 | high |
| Phase 2 | Day 31–60 | P1/P2 | medium |
| Phase 3 | Day 61–90 | P0/P1 | medium/low |

---

## STEP 2B — PHASE BODY TEMPLATE TABLE

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

## STEP 2C — PHASE-SEVERITY INFERENCE RULE

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

**Violation conditions (apply in Step 4B):**
- Phase 1 P0 or P1 on a non-outage ticket: violation — correct to P2/P3.
- Phase 3 P3 on a ticket where the user cannot complete a task: violation — correct to P1/P0.

**Required confirmation before proceeding:**
State the inference rule in your own words as a named constraint:

```
INFERENCE RULE (stated): [your paraphrase of the directional rule above]
Applied in: Steps 4, 4B, and Pass 2 INFERENCE AUDIT
```

Do not proceed to Step 3 until this block is filled.

---

## STEP 3 — PERFORMANCE MODE DECLARATION

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

## STEP 4 — VOCABULARY PRE-COMMITMENT TABLE

The INFERENCE RULE from Step 2C governs severity assignments here.
Phase 1 = P2/P3 (fallback available). Phase 3 = P0/P1 when blocking (fallback gone).

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

## STEP 4B — COLLECTIVE DISTRIBUTION AUDIT

Audit five constraints before writing any card body:

1. **Phase distribution** — at least two Phase 1 rows and one Phase 3 row.
2. **Category spread** — at least three distinct category values.
3. **Volume distribution** — all three volume levels present.
4. **Phase-character compliance** — each row's volume and severity match Step 2 ranges.
5. **Inference-rule compliance** — apply the INFERENCE RULE from Step 2C:
   - Scan Phase 1 rows: flag any P0 or P1 assignment on a non-outage ticket.
   - Scan Phase 3 rows: flag any P3 assignment on a blocking ticket.
   - State PASS if no violations; FAIL and name the row and correction if any found.

State PASS or FAIL per constraint.
**If any fails, correct the table and re-run. Name the correction.**

---

## STEP 5 — FULL CARD BODIES

For each row in the summary table:

```
Ticket ID: [T-NN]
Title: [descriptive title]
Category: [must match Step 4 exactly]
Persona: [must match Step 4 exactly]
Volume: [must match Step 4 exactly]
Severity: [must match Step 4 exactly]

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
```

---

## STEP 6 — CROSS-TICKET PATTERNS

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

## STEP 7 — GAP ANALYSIS

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
Migrating from: [product name from Step 1b — verbatim, grep-checkable]
Expected behavior: [one sentence — what users expected, based on the competitor's behavior]
Actual behavior: [one sentence — what this product actually does or fails to do]
Migration impact: [one sentence — what users must change, lose, or manually replicate]
```

Rules:
- `Migrating from:` MUST contain the product name from Step 1b verbatim.
  Prohibited: `Migrating from: existing tool`, `Migrating from: legacy workflow`.
- `Expected behavior:` and `Actual behavior:` define the behavior delta —
  they describe the same capability from two perspectives.
- Every entry must be independently enumerable: a reader scanning only this sub-section
  must be able to identify the competitor, the behavior delta, and the migration cost
  without reading any other part of the output.

### Pre-Launch Priority
Name the single gap to close first. Tie to specific ticket IDs, severity, and volume.
State whether it reduces switching-friction for inertia-competitor migrants.

---

## STEP 8 — DUAL-PASS VERIFICATION

### PASS 1 — Coverage Trace Table

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
1. Confirm: **"No gap from the Gap Analysis — including switching-friction gaps —
   is absent from this table."**
2. Confirm: **"The inertia competitor product name appears in at least two
   STATUS QUO element cells."**

END OF PASS 1. Switch to verification mode for properties and inference audit.

### PASS 2 — Properties Verify + Inference Audit

**PART A — Frontmatter Verify**

Confirm the summary table from Step 4 matches every Ticket ID, Phase, Category,
Persona, Volume, and Severity in the full card bodies from Step 5.
State: **"All Step 4 values match Step 5 card bodies."**

**PART B — Property Checks**

1. **Tool-name fidelity** — product name from Step 1b appears verbatim in Step 1b,
   at least two card bodies, and at least one `Migrating from:` field.
   State: **"[PRODUCT NAME] in Step 1b: YES. Card bodies: T-NN, T-NN (minimum).
   Migrating from: field: YES."**

2. **Phase-differentiated templates** — at least two Phase 1 bodies contain the
   Phase 1 template from Step 2B, and at least one Phase 3 body contains the Phase 3 template.
   State: **"Phase 1 template in: T-NN, T-NN. Phase 3 template in: T-NN."**

3. **Switching-friction 4-field format** — every entry in the Switching-Friction Gaps
   sub-section contains all four fields. Scan each entry for: Migrating from, Expected
   behavior, Actual behavior, Migration impact.
   State: **"All four fields present in all entries: YES / NO. Missing: [field list or NONE]."**

**PART C — Inference Audit**

Scan Phase 1 rows in the vocabulary table (Step 4):
- List every Phase 1 ticket assigned P0 or P1.
- For each: state whether this is an outage-level ticket. If yes, the assignment stands
  and acknowledge the exception explicitly: "Exception acknowledged: T-NN is Phase 1 P0/P1
  because [outage reason]." If no, name the violation and correct it.
State: **"Phase 1 P0/P1 assignments: [list or NONE]. Exceptions acknowledged: [list or NONE].
Violations corrected: [list or NONE]."**

Scan Phase 3 rows in the vocabulary table (Step 4):
- List every Phase 3 ticket assigned P3.
- For each: state whether this is a non-blocking issue. If yes, acknowledge the exception
  explicitly: "Exception acknowledged: T-NN is Phase 3 P3 because [non-blocking reason]."
  If no (it blocks a committed user), name the violation and correct it.
State: **"Phase 3 P3 assignments: [list or NONE]. Exceptions acknowledged: [list or NONE].
Violations corrected: [list or NONE]."**

Confirm the INFERENCE RULE stated in Step 2C has been applied consistently:
State: **"INFERENCE RULE compliance confirmed. Phase 1 → lower severity (fallback available):
[PASS/FAIL]. Phase 3 → higher severity (fallback gone, committed user): [PASS/FAIL]."**

State final: **"All Step 4 values match Step 5. Inference audit complete."**
Name and correct any issue before finalizing.
```

---

## V-04: Combined — Step 4 Decision-Adjacent Paraphrase (C-30) + Part C Structured Exception Sign-Off Block (C-31)

**Axes**: (1) C-30 paraphrase gate relocated to Step 4 header, immediately before severity column (V-02 placement) — STEP 2C has the full imperative rule but no paraphrase block; (2) C-31 Part C adds both named sub-checks AND replaces the plain prose exception acknowledgment with a structured EXCEPTION SIGN-OFF BLOCK that must be filled for every deviation.

**Hypothesis**: Decision-adjacent paraphrase (from V-02) provides the strongest temporal coupling for C-30 — the model's own-words commitment is the immediate context before severity values are generated. The structured exception sign-off block in Part C provides the strongest C-31 compliance — any C-28 or C-29 violation produces a named, field-complete exception record rather than a prose count. Together these two axes address the two root failure modes: a paraphrase that dissipates before the decision (C-30), and an exception acknowledgment that is acknowledged but not attributed (C-31).

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 — INERTIA: STATUS QUO

Establish the current-state baseline and name the inertia competitor.

**1a. Current-state baseline**
Describe in 2–3 sentences: what are users doing today to accomplish the job
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

## STEP 2 — PHASE MAP TABLE

| Phase | Window | Expected severity range | Expected volume character |
|-------|--------|------------------------|--------------------------|
| Phase 1 | Day 0–30 | P2/P3 | high |
| Phase 2 | Day 31–60 | P1/P2 | medium |
| Phase 3 | Day 61–90 | P0/P1 | medium/low |

---

## STEP 2B — PHASE BODY TEMPLATE TABLE

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

## STEP 2C — PHASE-SEVERITY INFERENCE RULE

Apply this rule when assigning severity in Step 4. Read and accept this rule before
proceeding to Step 3.

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

**Violation conditions (apply in Step 4B):**
- Phase 1 P0 or P1 on a non-outage ticket: violation — correct to P2/P3.
- Phase 3 P3 on a ticket where the user cannot complete a task: violation — correct to P1/P0.

---

## STEP 3 — PERFORMANCE MODE DECLARATION

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

## STEP 4 — VOCABULARY PRE-COMMITMENT TABLE

Before filling any severity cell, state the inference rule from Step 2C in your own words.
Do not fill the table until this line is written:

```
INFERENCE RULE (stated): [your paraphrase of the directional rule from Step 2C]
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

## STEP 4B — COLLECTIVE DISTRIBUTION AUDIT

Audit five constraints before writing any card body:

1. **Phase distribution** — at least two Phase 1 rows and one Phase 3 row.
2. **Category spread** — at least three distinct category values.
3. **Volume distribution** — all three volume levels present.
4. **Phase-character compliance** — each row's volume and severity match Step 2 ranges.
5. **Inference-rule compliance** — apply the INFERENCE RULE you stated above Step 4:
   - Scan Phase 1 rows: flag any P0 or P1 assignment on a non-outage ticket.
   - Scan Phase 3 rows: flag any P3 assignment on a blocking ticket.
   - State PASS if no violations; FAIL and name the row and correction if any found.

State PASS or FAIL per constraint.
**If any fails, correct the table and re-run. Name the correction.**

---

## STEP 5 — FULL CARD BODIES

For each row in the summary table:

```
Ticket ID: [T-NN]
Title: [descriptive title]
Category: [must match Step 4 exactly]
Persona: [must match Step 4 exactly]
Volume: [must match Step 4 exactly]
Severity: [must match Step 4 exactly]

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
```

---

## STEP 6 — CROSS-TICKET PATTERNS

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

## STEP 7 — GAP ANALYSIS

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
Migrating from: [product name from Step 1b — verbatim, grep-checkable]
Expected behavior: [one sentence — what users expected, based on the competitor's behavior]
Actual behavior: [one sentence — what this product actually does or fails to do]
Migration impact: [one sentence — what users must change, lose, or manually replicate]
```

Rules:
- `Migrating from:` MUST contain the product name from Step 1b verbatim.
  Prohibited: `Migrating from: existing tool`, `Migrating from: legacy workflow`.
- `Expected behavior:` and `Actual behavior:` define the behavior delta —
  they describe the same capability from two perspectives.
- Every entry must be independently enumerable: a reader scanning only this sub-section
  must be able to identify the competitor, the behavior delta, and the migration cost
  without reading any other part of the output.

### Pre-Launch Priority
Name the single gap to close first. Tie to specific ticket IDs, severity, and volume.
State whether it reduces switching-friction for inertia-competitor migrants.

---

## STEP 8 — DUAL-PASS VERIFICATION

### PASS 1 — Coverage Trace Table

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
1. Confirm: **"No gap from the Gap Analysis — including switching-friction gaps —
   is absent from this table."**
2. Confirm: **"The inertia competitor product name appears in at least two
   STATUS QUO element cells."**

END OF PASS 1. Switch to verification mode for properties and inference audit.

### PASS 2 — Properties Verify + Inference Audit

**PART A — Frontmatter Verify**

Confirm the summary table from Step 4 matches every Ticket ID, Phase, Category,
Persona, Volume, and Severity in the full card bodies from Step 5.
State: **"All Step 4 values match Step 5 card bodies."**

**PART B — Property Checks**

1. **Tool-name fidelity** — product name from Step 1b appears verbatim in Step 1b,
   at least two card bodies, and at least one `Migrating from:` field.
   State: **"[PRODUCT NAME] in Step 1b: YES. Card bodies: T-NN, T-NN (minimum).
   Migrating from: field: YES."**

2. **Phase-differentiated templates** — at least two Phase 1 bodies contain the
   Phase 1 template from Step 2B, and at least one Phase 3 body contains the Phase 3 template.
   State: **"Phase 1 template in: T-NN, T-NN. Phase 3 template in: T-NN."**

3. **Switching-friction 4-field format** — every entry in the Switching-Friction Gaps
   sub-section contains all four fields. Scan each entry for: Migrating from, Expected
   behavior, Actual behavior, Migration impact.
   State: **"All four fields present in all entries: YES / NO. Missing: [field list or NONE]."**

**PART C — Inference Audit**

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
Disposition: [VALID EXCEPTION — reason | VIOLATION — corrected to P2/P3]
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
Disposition: [VALID EXCEPTION — reason | VIOLATION — corrected to P1/P0]
```

If no Phase 3 P3 assignments exist, state: **"No Phase 3 P3 exceptions. PASS."**

Confirm: **"INFERENCE RULE compliance: Phase 1 → P2/P3 (fallback available): [PASS/FAIL].
Phase 3 → P0/P1 (committed user, fallback gone): [PASS/FAIL]."**

**Sub-check 2: Switching-Friction Sub-Section Field Completeness (C-29)**

Confirm the Switching-Friction Gaps sub-section from Step 7 is present.
Scan every entry for the `Migrating from:` field:
- List each entry's `Migrating from:` value.
- Flag any entry where the value does not contain the product name from Step 1b verbatim.
State: **"Switching-Friction Gaps sub-section present: YES. Migrating from: fields —
[entry 1: PRODUCT NAME | entry 2: PRODUCT NAME | ...]. All fields populated with product
name verbatim: YES / NO. Missing or non-verbatim entries: [list or NONE]."**

State final: **"All Step 4 values match Step 5. Exception sign-offs complete.
Sub-checks 1 and 2 verified."**
Name and correct any issue before finalizing.
```

---

## V-05: Full Synthesis — Maximum C-30 (Hard Gate at STEP 2C + Recall at Step 4) + Maximum C-31 (Both Sub-Checks + Structured Exception Sign-Off + Paraphrase Consistency Confirmation)

**Axes**: All mechanisms combined: (1) C-30 hard gate at STEP 2C with "do not proceed" language AND paraphrase recalled at Step 4 header (double-gating eliminates dissipation); (2) C-31 Part C has both named sub-checks plus a structured EXCEPTION SIGN-OFF BLOCK for any deviation plus a final confirmation that the Part C audit is consistent with the paraphrase committed in Step 2C.

**Hypothesis**: Double-gating the paraphrase (stated in STEP 2C, recalled at Step 4 header) eliminates the dissipation risk from V-02 — the model has two generation-time commitments both closer to and directly preceding the severity assignment decision. The full Part C with both sub-checks and a structured exception sign-off satisfies C-31 completely: sub-check (1) is verified per-ticket with a named block, sub-check (2) is verified per-entry in the switching-friction sub-section. The paraphrase consistency confirmation closes the C-30/C-31 chain — the paraphrase the model committed to in STEP 2C and recalled at Step 4 is explicitly compared against the Part C audit result, making it structurally self-contradicting for a model to state "Phase 1 = lower severity" as its paraphrase and then report a Phase 1 P0 violation as PASS.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 — INERTIA: STATUS QUO

Establish the current-state baseline and name the inertia competitor.

**1a. Current-state baseline**
Describe in 2–3 sentences: what are users doing today to accomplish the job
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

## STEP 2 — PHASE MAP TABLE

| Phase | Window | Expected severity range | Expected volume character |
|-------|--------|------------------------|--------------------------|
| Phase 1 | Day 0–30 | P2/P3 | high |
| Phase 2 | Day 31–60 | P1/P2 | medium |
| Phase 3 | Day 61–90 | P0/P1 | medium/low |

---

## STEP 2B — PHASE BODY TEMPLATE TABLE

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

## STEP 2C — PHASE-SEVERITY INFERENCE RULE

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

```
INFERENCE RULE (stated): [your paraphrase of the directional rule above]
Applied in: Steps 4, 4B, and Pass 2 INFERENCE AUDIT
```

Do not proceed to Step 3 until this block is filled with your own-words paraphrase.

---

## STEP 3 — PERFORMANCE MODE DECLARATION

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

## STEP 4 — VOCABULARY PRE-COMMITMENT TABLE

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

## STEP 4B — COLLECTIVE DISTRIBUTION AUDIT

Audit five constraints before writing any card body:

1. **Phase distribution** — at least two Phase 1 rows and one Phase 3 row.
2. **Category spread** — at least three distinct category values.
3. **Volume distribution** — all three volume levels present.
4. **Phase-character compliance** — each row's volume and severity match Step 2 ranges.
5. **Inference-rule compliance** — apply the INFERENCE RULE confirmed above Step 4:
   - Scan Phase 1 rows: flag any P0 or P1 assignment on a non-outage ticket.
   - Scan Phase 3 rows: flag any P3 assignment on a blocking ticket.
   - State PASS if no violations; FAIL and name the row and correction if any found.

State PASS or FAIL per constraint.
**If any fails, correct the table and re-run. Name the correction.**

---

## STEP 5 — FULL CARD BODIES

For each row in the summary table:

```
Ticket ID: [T-NN]
Title: [descriptive title]
Category: [must match Step 4 exactly]
Persona: [must match Step 4 exactly]
Volume: [must match Step 4 exactly]
Severity: [must match Step 4 exactly]

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
```

---

## STEP 6 — CROSS-TICKET PATTERNS

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

## STEP 7 — GAP ANALYSIS

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
Migrating from: [product name from Step 1b — verbatim, grep-checkable]
Expected behavior: [one sentence — what users expected, based on the competitor's behavior]
Actual behavior: [one sentence — what this product actually does or fails to do]
Migration impact: [one sentence — what users must change, lose, or manually replicate]
```

Rules:
- `Migrating from:` MUST contain the product name from Step 1b verbatim.
  Prohibited: `Migrating from: existing tool`, `Migrating from: legacy workflow`.
- `Expected behavior:` and `Actual behavior:` define the behavior delta —
  they describe the same capability from two perspectives.
- Every entry must be independently enumerable: a reader scanning only this sub-section
  must be able to identify the competitor, the behavior delta, and the migration cost
  without reading any other part of the output.

### Pre-Launch Priority
Name the single gap to close first. Tie to specific ticket IDs, severity, and volume.
State whether it reduces switching-friction for inertia-competitor migrants.

---

## STEP 8 — DUAL-PASS VERIFICATION

### PASS 1 — Coverage Trace Table

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
1. Confirm: **"No gap from the Gap Analysis — including switching-friction gaps —
   is absent from this table."**
2. Confirm: **"The inertia competitor product name appears in at least two
   STATUS QUO element cells."**

END OF PASS 1. Switch to verification mode for properties and inference audit.

### PASS 2 — Properties Verify + Inference Audit

**PART A — Frontmatter Verify**

Confirm the summary table from Step 4 matches every Ticket ID, Phase, Category,
Persona, Volume, and Severity in the full card bodies from Step 5.
State: **"All Step 4 values match Step 5 card bodies."**

**PART B — Property Checks**

1. **Tool-name fidelity** — product name from Step 1b appears verbatim in Step 1b,
   at least two card bodies, and at least one `Migrating from:` field.
   State: **"[PRODUCT NAME] in Step 1b: YES. Card bodies: T-NN, T-NN (minimum).
   Migrating from: field: YES."**

2. **Phase-differentiated templates** — at least two Phase 1 bodies contain the
   Phase 1 template from Step 2B, and at least one Phase 3 body contains the Phase 3 template.
   State: **"Phase 1 template in: T-NN, T-NN. Phase 3 template in: T-NN."**

3. **Switching-friction 4-field format** — every entry in the Switching-Friction Gaps
   sub-section contains all four fields. Scan each entry for: Migrating from, Expected
   behavior, Actual behavior, Migration impact.
   State: **"All four fields present in all entries: YES / NO. Missing: [field list or NONE]."**

**PART C — Inference Audit**

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
Disposition: [VALID EXCEPTION — reason | VIOLATION — corrected to P2/P3]
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
Disposition: [VALID EXCEPTION — reason | VIOLATION — corrected to P1/P0]
```

If no Phase 3 P3 assignments exist, state: **"No Phase 3 P3 exceptions. PASS."**

Confirm the INFERENCE RULE stated in Step 2C and confirmed at Step 4 has been
applied consistently. Compare the paraphrase from Step 2C against the audit results:
State: **"INFERENCE RULE paraphrase (Step 2C): [quote first 10 words of your Step 2C paraphrase].
Paraphrase confirmed at Step 4: YES.
Audit result — Phase 1 P2/P3 compliance: [PASS/FAIL].
Audit result — Phase 3 P0/P1 compliance: [PASS/FAIL].
Paraphrase consistent with audit results: YES / NO."**

**Sub-check 2: Switching-Friction Sub-Section Field Completeness (C-29)**

Confirm the Switching-Friction Gaps sub-section from Step 7 is present.
Scan every entry for the `Migrating from:` field:
- List each entry's `Migrating from:` value.
- Flag any entry where the value does not contain the product name from Step 1b verbatim.
State: **"Switching-Friction Gaps sub-section present: YES. Migrating from: fields —
[entry 1: value | entry 2: value | ...]. All fields populated with product name
verbatim: YES / NO. Missing or non-verbatim entries: [list or NONE]."**

State final: **"All Step 4 values match Step 5. Exception sign-offs complete.
Sub-checks 1 and 2 verified. Paraphrase consistency confirmed."**
Name and correct any issue before finalizing.
```

---

## Variation Summary

| Variation | C-30 mechanism | C-30 gate language | C-30 placement | C-31 Part C coverage | C-31 exception format | Hypothesis |
|-----------|---------------|-------------------|----------------|----------------------|-----------------------|------------|
| V-01 | Named block present | ABSENT — no "do not proceed" | End of STEP 2C | Both sub-checks (full) | Prose count | Block present but no gate — C-30 likely FAIL (verbatim echo, not paraphrase) |
| V-02 | Hard gate | Present — "do not proceed until written" | STEP 4 header (decision-adjacent) | Both sub-checks (full) | Prose count | Temporal coupling strongest at Step 4; dissipation between 2C and 4 eliminated |
| V-03 | Hard gate | Present — "do not proceed until filled" | End of STEP 2C | Sub-check 1 only (inference scan) | Prose count with exception acknowledgment | Partial C-31: sub-check 2 absent from Part C — C-29 field completeness unverified as Part C property |
| V-04 | Gate at Step 4 | Present | STEP 4 header | Both sub-checks | Structured EXCEPTION SIGN-OFF BLOCK | Decision-adjacent paraphrase + structured sign-off — C-30 tight; exceptions produce named records |
| V-05 | Hard gate + recall | Present at STEP 2C + recall at Step 4 | Double: STEP 2C end + Step 4 header | Both sub-checks | Structured EXCEPTION SIGN-OFF BLOCK + paraphrase consistency confirmation | Maximum C-30 + maximum C-31: paraphrase chain from 2C to Step 4 to Part C; C-28/C-29 both verified per-item |

**Expected C-30 outcomes**:
- V-01: FAIL — named block without gate language invites verbatim copy, not demonstrated encoding
- V-02: PASS — decision-adjacent gate fires immediately before severity column; paraphrase is live generation context at the point of decision
- V-03: PASS — same STEP 2C gate as R9 V-05; C-30 unchanged from the ceiling variation
- V-04: PASS — same decision-adjacent gate as V-02
- V-05: PASS + strongest — double-gated: paraphrase committed at STEP 2C, recalled at Step 4, consistency confirmed in Part C

**Expected C-31 outcomes**:
- V-01: PASS — both sub-checks present in Part C (identical to R9 V-05 structure)
- V-02: PASS — both sub-checks present (unchanged from R9 V-05 Part C)
- V-03: FAIL — sub-check 2 absent from Part C; C-29 field completeness is a Part B property only, not a Part C verified property
- V-04: PASS + stronger — both sub-checks + structured sign-off blocks produce per-exception records
- V-05: PASS + strongest — both sub-checks + structured sign-off + paraphrase consistency confirmation chains C-30 and C-31 together
