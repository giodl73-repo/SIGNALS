# listen-support Round 9 — Skill Body Prompt Variations

**Rubric target**: v9 (195 pts)
**New criteria in scope**: C-28 (Phase-Architecture Severity Inference Rule), C-29 (Dedicated Switching-Friction Gap Sub-Section with `Migrating from:` field)
**Base**: All prior mechanisms from R8 V-05 (C-01 through C-27 at ceiling)

**Variation axes selected** (3 single-axis, then 2 combined):
1. **C-28 mechanism placement** — annotation inside Phase Map Table (weak) vs. dedicated STEP 2C (strong) — (V-01 weak, V-04/V-05 strong)
2. **C-29 format depth** — minimal `Migrating from:` + one field vs. 4-field structured entry — (V-02 rich)
3. **Phrasing register** — descriptive/explanatory inference rule vs. imperative/directional constraint — (V-03 descriptive, V-04/V-05 imperative)
4. **C-28 dedicated step + C-29 rich format** combined — (V-04)
5. **Full synthesis**: C-28 dedicated step + C-29 rich format + Pass 2 verification of both — (V-05)

---

## V-01: Single-Axis — C-28 as Phase Map Annotation (Weak)

**Axis**: C-28 mechanism placement — weak: the phase-severity inference rule reasoning (why early = lower severity, late = higher severity) is added as a prose annotation immediately below the Phase Map Table in STEP 2. No dedicated step. C-29 gets a dedicated Switching-Friction Gaps sub-section with minimal `Migrating from:` field per entry.

**Hypothesis**: The annotation placement is unlikely to satisfy C-28 because the directional reasoning is embedded in descriptive prose without structural isolation. The model reads the note but has no structural anchor preventing a Phase 3 ticket at P3 without stated justification — the rule is present but not operationally bound to severity assignment. C-29 will be satisfied (dedicated sub-section with `Migrating from:` field). This establishes the minimum-annotation baseline for C-28 failure diagnosis.

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

This product name will be embedded in the performance mode declaration in Step 3.
It will appear verbatim in every Phase 1 and Phase 3 ticket body and in at least one
gap from the Gap Analysis. Record it once here; reference it by name everywhere else.

**1c. Adoption-curve context**
Note where the user population sits: early (mostly still on the competitor, dual-tool phase)
or late (partially migrated, parity-gap phase). This drives phase distribution in Step 4.

---

## STEP 2 — PHASE MAP TABLE

| Phase | Window | Expected severity range | Expected volume character |
|-------|--------|------------------------|--------------------------|
| Phase 1 | Day 0–30 | P2/P3 | high |
| Phase 2 | Day 31–60 | P1/P2 | medium |
| Phase 3 | Day 61–90 | P0/P1 | medium/low |

**Severity inference note:**
Phase 1 tickets trend toward lower severity because adoption friction is expected,
the inertia competitor remains available as a fallback, and workarounds exist —
a user can switch back to the competitor to complete their task.
Phase 3 tickets trend toward higher severity because users have committed to the new product,
parity gaps block workflows that have no fallback, and the competitor is no longer
in the daily workflow.
Assigning P0/P1 to a Phase 1 ticket for a non-blocking issue, or P3 to a Phase 3 ticket
for a blocking parity gap, is a phase-architecture mismatch.

---

## STEP 2B — PHASE BODY TEMPLATE TABLE

Replace [INERTIA COMPETITOR] with the product name from Step 1b before writing this table.
These pre-printed template sentences are the required opening stance for
Phase 1 and Phase 3 card bodies. Placeholders must be filled concretely in Step 5.

| Phase | Adoption stance | Pre-printed template sentence |
|-------|----------------|-------------------------------|
| Phase 1 | Dual-tool tension | "I still have [INERTIA COMPETITOR] open in another tab while working through this — I keep switching back to check how it handled [specific scenario]." |
| Phase 3 | Parity gap | "In [INERTIA COMPETITOR] I could [specific action] without leaving this screen; here I cannot find a way to do it at all." |

Instructions:
- Phase 1 bodies: include the Phase 1 sentence with all placeholders filled concretely.
- Phase 3 bodies: include the Phase 3 sentence with all placeholders filled concretely.
- Phase 2 bodies: reference the competitor where it naturally fits; no template required.

---

## STEP 3 — PERFORMANCE MODE DECLARATION

**You ARE the persona named on each ticket card.**

Your previous primary workflow used [INERTIA COMPETITOR — insert product name from Step 1b].
You recently started using this new product. You are in some stage of migration:
Phase 1 tickets are written when you still have the old tool open. Phase 3 tickets
are written when you have committed to the new tool but are discovering what it cannot do.

Do not write "the user", "they", "the SRE", "the PM", "the engineer",
or any named-role title referring to yourself in third person.

Prohibited verb-subject forms: "the SRE ran", "the PM reviewed", "the engineer observed",
"the C-07 clicked", "the Support agent opened", or any construction where a role title
precedes a verb.

**Every action in this ticket was taken by "I". Every reference to the old tool
uses its product name, not a pronoun or generic description.**

---

## STEP 4 — VOCABULARY PRE-COMMITMENT TABLE

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

Audit four constraints before writing any card body:

1. **Phase distribution** — at least two Phase 1 rows and one Phase 3 row.
   Rationale: the adoption-curve context from Step 1c must produce at least two
   dual-tool-tension bodies and at least one parity-gap body.
2. **Category spread** — at least three distinct category values.
3. **Volume distribution** — all three volume levels present.
4. **Phase-character compliance** — each row's volume and severity match the
   expected ranges in Step 2.

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
  placeholders filled concretely.
- Phase 3 tickets: open with the Phase 3 template sentence from Step 2B,
  placeholders filled concretely.
- All tickets: reference the STATUS QUO element from Step 1 that drives
  this ticket's volume and severity.
- No third-person references to yourself. No unnamed references to the old tool —
  use the product name from Step 1b every time you mention it.]
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
Dedicated sub-section for migration barriers only. Gaps here are not duplicated in the
doc, design, or operational sub-sections above. At least one entry required.

Required format per entry:
```
Switching-friction gap: [short name]
Migrating from: [product name from Step 1b — verbatim, grep-checkable]
Barrier: [one sentence describing what the competitor provided that this feature does not]
Migration impact: [one sentence on what users must change or lose when switching]
```

Prohibited: `Migrating from: existing tooling`, `Migrating from: previous workflow`,
or any entry where the "Migrating from:" field does not contain the product name
from Step 1b verbatim.

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
2. Confirm: **"The inertia competitor product name from Step 1b appears in at least
   two STATUS QUO element cells in this table."**

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 — Frontmatter Verify

Confirm the summary table from Step 4 matches every Ticket ID, Phase, Category,
Persona, Volume, and Severity in the full card bodies from Step 5.

Also confirm the following properties hold in the completed output:
1. **Tool-name fidelity** — the inertia competitor product name from Step 1b
   appears verbatim in Step 1b, at least two card bodies, and at least one
   switching-friction gap. State: **"[PRODUCT NAME] appears in Step 1b: YES.
   Card bodies: T-NN, T-NN (at minimum). Switching-friction gap: YES."**
2. **Phase-differentiated templates** — at least two Phase 1 bodies contain the
   Phase 1 template sentence from Step 2B, and at least one Phase 3 body contains
   the Phase 3 template sentence. State: **"Phase 1 template confirmed in: T-NN, T-NN.
   Phase 3 template confirmed in: T-NN."**
3. **Switching-friction sub-section** — the Switching-Friction Gaps sub-section in
   Step 7 contains at least one entry with a `Migrating from:` field containing
   the product name verbatim. State: **"Switching-friction gap with Migrating from:
   field present: YES."**

State: **"All Step 4 values match Step 5. All properties verified."**
Name and correct any mismatch before finalizing.
```

---

## V-02: Single-Axis — C-29 Rich Format (4-Field Structured Entry)

**Axis**: C-29 format depth — rich: the Switching-Friction Gaps sub-section requires a 4-field structured entry (`Migrating from:`, `Expected behavior:`, `Actual behavior:`, `Migration impact:`), making each entry both grep-checkable by tool name and enumerable by behavior delta as two separate fields. C-28 uses the same weak annotation placement as V-01 (note in STEP 2).

**Hypothesis**: The 4-field format is the strongest C-29 mechanism because it separates the competitor name (grep-checkable in `Migrating from:`) from the behavior delta (enumerable across two fields: expected vs. actual) from the cost (migration impact). Whether the richer format produces better gap quality or just more structural overhead is the testable question. C-28 will likely partially fail (annotation present but not operationally bound to the severity assignment decision) as in V-01.

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

This product name will appear verbatim in every Phase 1 and Phase 3 ticket body
and in every switching-friction gap entry. Record it once here; reference by name everywhere.

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

**Severity inference note:**
Phase 1 tickets trend toward lower severity because adoption friction is expected and
the inertia competitor provides a fallback — users can complete tasks in the old tool.
Phase 3 tickets trend toward higher severity because committed users have left the
old tool behind; parity gaps block workflows with no alternative path.

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

## STEP 3 — PERFORMANCE MODE DECLARATION

**You ARE the persona named on each ticket card.**

Your previous primary workflow used [INERTIA COMPETITOR — insert product name from Step 1b].
You recently started using this new product. Phase 1 tickets are written when you still
have the old tool open. Phase 3 tickets are written when you have committed to the new
tool but are discovering what it cannot do.

Do not write "the user", "they", "the SRE", "the PM", "the engineer",
or any named-role title referring to yourself in third person.

Prohibited verb-subject forms: "the SRE ran", "the PM reviewed", "the engineer observed",
"the C-07 clicked", "the Support agent opened", or any role title preceding a verb.

**Every action in this ticket was taken by "I". Every reference to the old tool
uses its product name, not a pronoun or generic description.**

---

## STEP 4 — VOCABULARY PRE-COMMITMENT TABLE

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

Audit four constraints before writing any card body:

1. **Phase distribution** — at least two Phase 1 rows and one Phase 3 row.
2. **Category spread** — at least three distinct category values.
3. **Volume distribution** — all three volume levels present.
4. **Phase-character compliance** — each row's volume and severity match Step 2 ranges.

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
  placeholders filled concretely.
- Phase 3 tickets: open with the Phase 3 template sentence from Step 2B,
  placeholders filled concretely.
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

---

## STEP 7 — GAP ANALYSIS

### Doc Gaps
[At least one documentation gap.]

### Design Gaps
[At least one design gap.]

### Operational Gaps
[At least one operational gap.]

### Switching-Friction Gaps
Dedicated sub-section for migration barriers only. Not a subset of the above sections.
At least one entry required. Use this exact 4-field format for every entry:

```
Switching-friction gap: [short name]
Migrating from: [product name from Step 1b — verbatim, grep-checkable]
Expected behavior: [one sentence — what users expected, based on how the competitor handled it]
Actual behavior: [one sentence — what the new product actually does instead]
Migration impact: [one sentence on what users must change, lose, or manually replicate]
```

Rules:
- `Migrating from:` must contain the product name from Step 1b verbatim.
  Prohibited: `Migrating from: previous tooling`, `Migrating from: legacy system`.
- `Expected behavior:` and `Actual behavior:` must describe the same capability from
  two perspectives — these fields create the behavior delta.
- Two entries are recommended; one is the minimum.

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

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 — Frontmatter Verify

Confirm the summary table from Step 4 matches every Ticket ID, Phase, Category,
Persona, Volume, and Severity in the full card bodies from Step 5.

Confirm:
1. **Tool-name fidelity** — product name from Step 1b appears verbatim in Step 1b,
   at least two card bodies, and at least one switching-friction gap `Migrating from:` field.
   State: **"[PRODUCT NAME] in Step 1b: YES. Card bodies: T-NN, T-NN. Migrating from: YES."**
2. **Phase templates** — at least two Phase 1 bodies and one Phase 3 body use their templates.
   State: **"Phase 1 template in: T-NN, T-NN. Phase 3 template in: T-NN."**
3. **Switching-friction 4-field format** — every switching-friction gap entry contains
   all four fields: Migrating from, Expected behavior, Actual behavior, Migration impact.
   State: **"All switching-friction entries have all four fields: YES."**

State: **"All Step 4 values match Step 5. All properties verified."**
Name and correct any mismatch before finalizing.
```

---

## V-03: Single-Axis — C-28 Phrasing Register (Descriptive/Explanatory)

**Axis**: Phrasing register — the C-28 inference rule is stated in descriptive, explanatory prose ("Early-phase users still have the competitor tool available, which means...") rather than as an imperative constraint ("Phase 1 tickets MUST NOT be assigned P0 unless..."). The explanatory form articulates the causal logic behind the directionality. C-29 uses the dedicated sub-section with `Migrating from:` field as in V-01.

**Hypothesis**: Descriptive/explanatory framing of the C-28 inference rule may produce better reasoning (the model understands the cause) but weaker compliance (no hard rule prevents a reversal). When a model reads "early-phase users have a fallback, so severity tends lower," it may still assign P1 to a Phase 1 frustration ticket because no constraint fires. Imperative framing in V-04 will likely outperform this variation for C-28. This variation tests whether causal explanation alone is a sufficient structural guarantee.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 — INERTIA: STATUS QUO

Establish the current-state baseline and name the inertia competitor.

**1a. Current-state baseline**
Describe in 2–3 sentences: what are users doing today? Where is friction highest?
What workarounds exist and what do they cost?

**1b. Inertia competitor declaration**

```
INERTIA COMPETITOR: [product name]
Prohibited: "existing tooling", "their current system", "legacy workflow",
or any phrase that does not produce a grep-checkable product name string.
```

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

**Why the severity direction runs this way:**

Early-phase users (Phase 1) are still mid-migration. The inertia competitor is open
in another tab. When something is unclear or friction is high, they can fall back to
the old tool and complete their task. Because a workaround exists and friction is
expected during adoption, early-phase issues are lower-severity — the user is not blocked.

Late-phase users (Phase 3) have committed to the new product. They have stopped running
the competitor in parallel. When a parity gap surfaces, there is no fallback — the feature
they relied on in the competitor does not exist here, and they cannot complete their task.
Because committed users are blocked without recourse, late-phase issues are higher-severity.

This explains the upward severity gradient: Phase 1 → P2/P3 (fallback available),
Phase 3 → P0/P1 (fallback gone, committed user blocked). Assign severity with this
logic in mind when completing the vocabulary table in Step 4.

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

## STEP 3 — PERFORMANCE MODE DECLARATION

**You ARE the persona named on each ticket card.**

Your previous primary workflow used [INERTIA COMPETITOR — insert product name from Step 1b].
You recently started using this new product. Phase 1 tickets are written when you still
have the old tool open. Phase 3 tickets are written when you have committed to the new
tool but are discovering what it cannot do.

Do not write "the user", "they", "the SRE", "the PM", "the engineer",
or any named-role title referring to yourself in third person.

Prohibited verb-subject forms: "the SRE ran", "the PM reviewed", "the engineer observed",
"the C-07 clicked", "the Support agent opened", or any role title preceding a verb.

**Every action in this ticket was taken by "I". Every reference to the old tool
uses its product name, not a pronoun or generic description.**

---

## STEP 4 — VOCABULARY PRE-COMMITMENT TABLE

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

When assigning severity, apply the reasoning from Step 2: Phase 1 tickets about expected
friction or learning curve should be P2/P3 (fallback available). Phase 3 tickets that
block committed users from completing a task should be P1/P0 (no fallback).

**Lock vocabulary values here. Full card bodies follow in Step 5.**

---

## STEP 4B — COLLECTIVE DISTRIBUTION AUDIT

Audit four constraints before writing any card body:

1. **Phase distribution** — at least two Phase 1 rows and one Phase 3 row.
2. **Category spread** — at least three distinct category values.
3. **Volume distribution** — all three volume levels present.
4. **Phase-character compliance** — each row's severity reflects the inference logic
   from Step 2: Phase 1 rows should be P2/P3; Phase 3 rows should be P0/P1.
   Flag any row where severity contradicts the fallback-availability reasoning.

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
  placeholders filled concretely.
- Phase 3 tickets: open with the Phase 3 template sentence from Step 2B,
  placeholders filled concretely.
- All tickets: reference the STATUS QUO element from Step 1 that drives
  this ticket's volume and severity. Where severity feels surprising, let the
  persona's situation (fallback available vs. committed user) explain it.
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

---

## STEP 7 — GAP ANALYSIS

### Doc Gaps
[At least one documentation gap.]

### Design Gaps
[At least one design gap.]

### Operational Gaps
[At least one operational gap.]

### Switching-Friction Gaps
Dedicated sub-section for migration barriers only. Not absorbed into the above sections.
At least one entry required. Use this format for every entry:

```
Switching-friction gap: [short name]
Migrating from: [product name from Step 1b — verbatim]
Barrier: [one sentence describing what the competitor provided that this feature does not]
Migration impact: [one sentence on what users must change or lose when switching]
```

The `Migrating from:` field must contain the product name verbatim.
Prohibited: any entry where the field reads "existing tool", "legacy system",
or any phrase that does not contain the product name from Step 1b.

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

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 — Frontmatter Verify

Confirm the summary table from Step 4 matches every Ticket ID, Phase, Category,
Persona, Volume, and Severity in the full card bodies from Step 5.

Also confirm:
1. **Severity inference consistency** — scan Phase 3 rows: do any have P3 assigned?
   If so, state the fallback-availability reasoning that justifies it (per Step 2 logic).
   State: **"Phase 3 P3 assignments: [count]. Justifications: [list or NONE]."**
2. **Phase templates** — at least two Phase 1 bodies and one Phase 3 body use their templates.
   State: **"Phase 1 template in: T-NN, T-NN. Phase 3 template in: T-NN."**
3. **Switching-friction Migrating from: field** — every entry in the Switching-Friction Gaps
   sub-section contains the product name verbatim in `Migrating from:`.
   State: **"All Migrating from: fields contain product name: YES."**

State: **"All Step 4 values match Step 5. All properties verified."**
Name and correct any mismatch before finalizing.
```

---

## V-04: Combined — C-28 Dedicated Step (Imperative) + C-29 Rich Format (4-Field)

**Axes**: C-28 as dedicated STEP 2C "PHASE-SEVERITY INFERENCE RULE" with imperative, directional constraints (Phase 1 tickets MUST be P2/P3 because fallback available; Phase 3 tickets MUST be P0/P1 when blocking because fallback gone) + C-29 with a dedicated Switching-Friction Gaps sub-section using 4-field structured entry (`Migrating from:`, `Expected behavior:`, `Actual behavior:`, `Migration impact:`).

**Hypothesis**: Making C-28 a named, structurally isolated step with imperative directional constraints closes the gap from V-01/V-02/V-03. The model cannot skip STEP 2C without violating the "do not skip steps" instruction, and the imperative rule binds severity direction structurally. Combined with C-29's 4-field format, this variation should satisfy both new criteria simultaneously with maximum structural enforcement. The dedicated STEP 2C also forces the model to explicitly state the inference rule before filling the vocabulary table in Step 4, making the rule operationally upstream of the severity assignments it governs.

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

This product name will be embedded in the performance mode declaration in Step 3.
It will appear verbatim in every Phase 1 and Phase 3 ticket body and in every
switching-friction gap entry. Record it once here; reference it by name everywhere else.

**1c. Adoption-curve context**
Note where the user population sits: early (mostly still on the competitor, dual-tool phase)
or late (partially migrated, parity-gap phase). This drives phase distribution in Step 4.

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

Apply this rule when assigning severity in Step 4. Do not proceed to Step 3 until
you have read and accepted this rule.

**Rule:**
Phase 1 tickets MUST be assigned P2 or P3 for any issue that is not a complete
feature outage or data loss. Reason: Phase 1 users still have the inertia competitor
available as a fallback. Adoption friction is expected. A workaround exists: use the
competitor to complete the task. A Phase 1 how-to or config ticket is P2/P3, not P1.

Phase 3 tickets that block a committed user MUST be assigned P0 or P1. Reason: Phase 3
users have stopped running the competitor in parallel. Parity gaps that prevent task
completion have no fallback. A committed user who cannot complete a core workflow is
P1 at minimum.

**Directional constraint (state before filling the vocabulary table in Step 4):**
- Phase 1 → lower severity because the inertia competitor provides a fallback.
- Phase 3 → higher severity because the fallback is gone and the user is committed.

**Violation conditions:**
- A Phase 1 P0/P1 assignment for a ticket that is not a total outage is a rule violation.
  Correct it to P2/P3 before proceeding.
- A Phase 3 P3 assignment for a ticket describing a committed user who cannot complete
  a task is a rule violation. Correct it to P1/P0 before proceeding.

State this rule in your own words before proceeding:
**"I understand: Phase 1 = lower severity (fallback available); Phase 3 = higher severity
(fallback gone, user committed). I will apply this in Step 4."**

---

## STEP 3 — PERFORMANCE MODE DECLARATION

**You ARE the persona named on each ticket card.**

Your previous primary workflow used [INERTIA COMPETITOR — insert product name from Step 1b].
You recently started using this new product. You are in some stage of migration:
Phase 1 tickets are written when you still have the old tool open. Phase 3 tickets
are written when you have committed to the new tool but are discovering what it cannot do.

Do not write "the user", "they", "the SRE", "the PM", "the engineer",
or any named-role title referring to yourself in third person.

Prohibited verb-subject forms: "the SRE ran", "the PM reviewed", "the engineer observed",
"the C-07 clicked", "the Support agent opened", or any construction where a role title
precedes a verb.

**Every action in this ticket was taken by "I". Every reference to the old tool
uses its product name, not a pronoun or generic description.**

---

## STEP 4 — VOCABULARY PRE-COMMITMENT TABLE

Before filling this table, recall the directional rule from Step 2C:
Phase 1 = P2/P3 (fallback available). Phase 3 = P0/P1 (committed user, fallback gone).

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
   Rationale: the adoption-curve context from Step 1c must produce at least two
   dual-tool-tension bodies and at least one parity-gap body.
2. **Category spread** — at least three distinct category values.
3. **Volume distribution** — all three volume levels present.
4. **Phase-character compliance** — each row's volume and severity match Step 2 ranges.
5. **Inference-rule compliance** — apply Step 2C: scan Phase 1 rows for P0/P1 assignments
   and Phase 3 rows for P3 assignments. Flag violations. State: PASS if no violations found;
   FAIL and name the violation if any row contradicts the directional rule.

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
  placeholders filled concretely. Your severity is P2/P3 because the competitor
  is still available to you as a fallback.
- Phase 3 tickets: open with the Phase 3 template sentence from Step 2B,
  placeholders filled concretely. Your severity is P0/P1 because you have
  stopped using the competitor and this gap blocks your work.
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
Dedicated sub-section for migration barriers only. These gaps are NOT duplicated in
the doc, design, or operational sub-sections above. At least one entry required.
Use this exact 4-field format for every entry:

```
Switching-friction gap: [short name]
Migrating from: [product name from Step 1b — verbatim, grep-checkable]
Expected behavior: [one sentence — what users expected, based on how the competitor handled it]
Actual behavior: [one sentence — what the new product actually does or fails to do]
Migration impact: [one sentence on what users must change, lose, or manually replicate]
```

Rules:
- `Migrating from:` MUST contain the product name from Step 1b verbatim.
  Prohibited: `Migrating from: legacy tool`, `Migrating from: previous system`.
- `Expected behavior:` and `Actual behavior:` describe the same capability from two angles.
  Together they define the behavior delta that creates the friction.
- At least one entry is required; two are recommended for coverage.

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

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 — Frontmatter Verify

Confirm the summary table from Step 4 matches every Ticket ID, Phase, Category,
Persona, Volume, and Severity in the full card bodies from Step 5.

Also confirm all four properties hold:
1. **Tool-name fidelity** — product name from Step 1b appears verbatim in Step 1b,
   at least two card bodies, and at least one switching-friction gap `Migrating from:` field.
   State: **"[PRODUCT NAME] in Step 1b: YES. Card bodies: T-NN, T-NN. Migrating from: YES."**
2. **Phase-differentiated templates** — at least two Phase 1 bodies contain the Phase 1
   template, and at least one Phase 3 body contains the Phase 3 template from Step 2B.
   State: **"Phase 1 template in: T-NN, T-NN. Phase 3 template in: T-NN."**
3. **Switching-friction 4-field format** — every switching-friction entry contains
   all four fields (Migrating from, Expected behavior, Actual behavior, Migration impact).
   State: **"All four fields present in all entries: YES."**
4. **Inference-rule compliance** — scan Phase 1 rows for P0/P1 and Phase 3 rows for P3.
   State: **"Phase 1 P0/P1 violations: [count or NONE]. Phase 3 P3 violations: [count or NONE]."**

State: **"All Step 4 values match Step 5. All four properties verified."**
Name and correct any mismatch before finalizing.
```

---

## V-05: Full Synthesis — C-28 Dedicated Step + C-29 Rich Format + Pass 2 Inference Audit

**Axes**: All mechanisms from V-04 + two additions: (1) the Phase-Severity Inference Rule in STEP 2C requires the model to explicitly state the inference rule in its own words and record it as a named constraint, making it a first-class output element rather than a read-and-apply instruction; (2) Pass 2 includes a dedicated INFERENCE AUDIT step that checks whether any Phase 1 P0/P1 or Phase 3 P3 assignment exists and, if so, requires the model to cite the exception reasoning rather than silently accept the value from Step 4.

**Hypothesis**: The Pass 2 inference audit closes the compliance loop in a different way than the STEP 2C rule alone. Even if a model writes a semantically valid Phase 3 P2 ticket (edge case: a non-blocking parity gap), the audit step forces explicit acknowledgment of the exception and traces it back to the inference rule. This makes C-28 a verified output property rather than a stated input constraint — the model cannot complete Pass 2 without demonstrating that it applied the directional rule. Combined with C-29's 4-field format and the `Migrating from:` scan in Pass 2, all C-28 and C-29 properties are structurally verified rather than assumed.

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

State final: **"All Step 4 values match Step 5. All properties and inference rule verified."**
Name and correct any issue before finalizing.
```

---

## Variation Summary

| Variation | C-28 mechanism | C-28 placement | C-29 format | C-29 `Migrating from:` | Pass 2 inference audit | Hypothesis |
|-----------|---------------|----------------|-------------|----------------------|------------------------|------------|
| V-01 | Prose annotation | Inside Step 2 note | Dedicated sub-section, 2-field | Required per entry | None | Annotation present but not operationally bound — C-28 likely FAIL |
| V-02 | Prose annotation | Inside Step 2 note | Dedicated sub-section, 4-field | Required per entry | None | C-29 richest format; C-28 still unbound — same C-28 failure mode as V-01 |
| V-03 | Descriptive/explanatory prose | Inside Step 2, worded causally | Dedicated sub-section, 2-field | Required per entry | Soft check (count P3 Phase 3) | Causal explanation produces understanding but not compliance for C-28 |
| V-04 | Imperative rule, dedicated step | STEP 2C | Dedicated sub-section, 4-field | Required per entry | Count-and-flag in Step 4B | Dedicated step + imperative constraint closes C-28; 4-field closes C-29 |
| V-05 | Imperative rule + stated paraphrase | STEP 2C | Dedicated sub-section, 4-field | Required per entry | Full INFERENCE AUDIT in Pass 2 Part C | Pass 2 audit makes C-28 a verified output property, not just a stated constraint |

**Expected C-28 outcomes**:
- V-01: FAIL (annotation not operationally bound to severity assignment)
- V-02: FAIL (same as V-01 — annotation, not rule)
- V-03: PARTIAL (causal explanation present; may improve compliance rate but no hard constraint)
- V-04: PASS (dedicated step + imperative rule fires before Step 4 vocabulary assignment)
- V-05: PASS + verified (inference audit in Pass 2 makes violations grep-checkable in output)

**Expected C-29 outcomes**:
- V-01: PASS (dedicated sub-section + `Migrating from:` field per entry)
- V-02: PASS + richer (4-field format exceeds minimum; behavior delta explicitly enumerable)
- V-03: PASS (dedicated sub-section + `Migrating from:` field per entry)
- V-04: PASS + richer (4-field format; per-entry field explicitly required)
- V-05: PASS + verified (Pass 2 Part B scans for all four fields and reports missing fields)
