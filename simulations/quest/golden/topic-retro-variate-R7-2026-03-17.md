# topic-retro — Variations R7
**Date:** 2026-03-17
**Rubric:** v5 (C-01 through C-21; total available = 116)
**R6 top scorer:** V-05 (108/112, 96.4%) — phase seals + baseline assumption column. V-02 scored 107/112 (95.5%).
**New criteria to target:** C-20 (gap-inertia-assumption-named) and C-21 (phase-seal-explicit).

**Persistent PARTIAL criteria from R6:**
- C-10 (AMEND per-table): all variations PARTIAL — scope declared at top, not per-table
- C-13 → promoted to C-20: only V-05 got PARTIAL via baseline assumption; no variation achieved PASS
- C-15 (accuracy ratio): all PARTIAL — weighted formula used, not N/M=X% count
- C-16 (namespace coverage table): all PARTIAL — text lists, not 9-row status table

R7 base: V-02 (Phase-Seal, R6) — strongest non-combined baseline at 107/112.
Single-axis: V-01 (C-20), V-02 (C-10), V-03 (C-16).
Combined: V-04 (C-20 + C-10), V-05 (C-20 + C-10 + C-15 + C-16 + C-21 strengthened).

---

## V-01 — Assumption-Column: C-20 via Dedicated Gap Table Column

**Axis:** C-20 mechanism — the Phase 7 gap table adds a dedicated "Assumption held without evidence" column between Namespace and "Would have surfaced". The assumption names the inertia belief that made the gap invisible; "Would have surfaced" names what the signal would have revealed. These are different statements and must remain distinct.

**Hypothesis:** Structurally separating the assumption (why the gap existed) from the outcome (what was missed) satisfies C-20. Both fields are required per gap row and are positioned in separate columns so they cannot be merged. The Phase 7 SEAL confirms both columns populated with distinct content. This is the minimal change from V-02 R6 that directly targets C-20 — all other phases unchanged.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Each phase ends with a PHASE SEAL — a required-field checklist. The phase is not complete until every seal item is confirmed.

{{#if amend}}AMEND SCOPE: {{amend}} — all phases operate within this constraint only.{{/if}}

---

PHASE 1 — ECHO
Run this phase before any signal comparison.

Search simulations/{namespace}/ for all artifacts associated with this topic.

The Echo is the single post-ship observable satisfying all three conditions:
  (a) Not predicted by any gathered signal — not even partially
  (b) Not a named risk or acknowledged unknown at commit time
  (c) Observable only after the feature shipped

Procedure:
  Step 1: List every post-ship outcome for this topic.
  Step 2: Eliminate any predicted by a gathered signal (fully or partially).
  Step 3: Eliminate any that were named risks or known unknowns.
  Step 4: From remaining candidates, select exactly one with highest commit-decision impact.
  Step 5: If no candidates remain: Echo = "No Echo — all post-ship outcomes were within signal bounds."

Output this table:

| Echo (one sentence) | Nearest signal artifact | Commit relevance: HIGH / MEDIUM / LOW |
|---------------------|------------------------|--------------------------------------|
| [finding or "No Echo — all post-ship outcomes were within signal bounds"] | [name or "none"] | [level or "N/A"] |

After the table, name the systemic pattern:
  > **Pattern**: [name] — [description of the recurring failure mode this Echo represents, not just this instance]

Pattern examples: adoption-assumption-gap, integration-surface-miss, timing-signal-gap, scale-behavior-gap, dependency-chain-miss, unknown-unknown, or name your own.

LOCK: This table and Pattern entry are final. Phases 2–8 may not alter them.
If Phase 5 analysis would revise the Echo, record the conflict in Phase 5 — do not edit this phase.

PHASE 1 SEAL — confirm before proceeding to Phase 2:
  [ ] Echo cell: one sentence (or explicit "No Echo" statement — not a restatement of a wrong prediction)
  [ ] Nearest signal: named artifact or "none"
  [ ] Commit relevance: HIGH, MEDIUM, or LOW (or "N/A" with "No Echo")
  [ ] Pattern entry: uses > **Pattern**: [name] — [description] format (not blank, not generic)
All items confirmed? PHASE 1 COMPLETE.

---

PHASE 2 — SIGNAL INVENTORY
List every artifact gathered before commit, one row per file.

| Namespace | Artifact | Date | Prediction summary |
|-----------|----------|------|--------------------|
| [name] | [filename] | [YYYY-MM-DD] | [one phrase] |

After the table:
  Namespaces with signals: [list]
  Empty namespaces (from: scout, draft, review, flow, trace, prove, listen, program, topic): [list]
  Total: N signals across M namespaces

PHASE 2 SEAL — confirm before proceeding to Phase 3:
  [ ] Every artifact from simulations/ for this topic has a row
  [ ] Empty namespace list accounts for all 9 namespaces not in "with signals"
  [ ] Total count stated
All items confirmed? PHASE 2 COMPLETE.

---

PHASE 3 — PREDICTED VS ACTUAL
For each namespace with at least one Phase 2 artifact:

| Namespace | Predicted (what signals claimed post-ship) | Actual (what was observed) | Match: C / P / W / ND |
|-----------|--------------------------------------------|----------------------------|-----------------------|
| [name] | [required — cannot be blank] | [required — cannot be blank] | [verdict] |

Verdict: C = Correct, P = Partial (directionally right, wrong magnitude/timing), W = Wrong, ND = No data.
Both Predicted and Actual must be explicitly stated for every row.

PHASE 3 SEAL — confirm before proceeding to Phase 4:
  [ ] Every namespace from Phase 2 has a row
  [ ] No Predicted cell is blank
  [ ] No Actual cell is blank
  [ ] Every row has a verdict label (C / P / W / ND)
All items confirmed? PHASE 3 COMPLETE.

---

PHASE 4 — NAMESPACE ACCURACY
Score each namespace from Phase 3 using the formula in the column header.

| Namespace | C | P | W | ND | Score: (C×100 + P×50) ÷ (C+P+W) |
|-----------|---|---|---|-----|----------------------------------|
| [name] | | | | | |
| TOTAL | | | | | |

ND entries excluded from denominator. Leave Score blank if denominator = 0.

PHASE 4 SEAL — confirm before proceeding to Phase 5:
  [ ] Every Phase 3 namespace has a row
  [ ] TOTAL row present
  [ ] Score column: formula applied to each row (blank only when denominator = 0, noted as such)
All items confirmed? PHASE 4 COMPLETE.

---

PHASE 5 — CONFLICT AUDIT
This phase is mandatory. It always produces output.

Review the locked Echo from Phase 1.
Question: Does anything in Phase 3 (match verdicts) or Phase 4 (namespace scores) suggest the Echo finding should be revised?

If YES — emit:
  CONFLICT DETECTED
  Source: [Phase 3 / Phase 4 — which finding creates the tension]
  Proposed revision: [what the Echo would become under this analysis]
  Resolution: Echo from Phase 1 is preserved unchanged. This is the conflict artifact.

If NO — emit:
  CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 findings are consistent with the locked Echo.

PHASE 5 SEAL — confirm before proceeding to Phase 6:
  [ ] Conflict audit question answered
  [ ] If YES: conflict artifact present with Source, Proposed revision, Resolution
  [ ] If NO: explicit "No conflict" declaration present
All items confirmed? PHASE 5 COMPLETE.

---

PHASE 6 — ACCURACY VERDICT
State the overall accuracy judgment, grounded in Phase 4 totals:

  "Signal accuracy for [topic]: [TOTAL score]/100 — [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]"

Do not introduce new observations. Reference Phase 4 TOTAL row only.

PHASE 6 SEAL — confirm before proceeding to Phase 7:
  [ ] Verdict sentence present in the required format
  [ ] Score drawn from Phase 4 TOTAL (not recalculated here)
  [ ] Tier label correct for stated score
All items confirmed? PHASE 6 COMPLETE.

---

PHASE 7 — GAP ANALYSIS
For each namespace scoring W or P in Phase 3, and each empty namespace where absence is material:

A gap entry requires two distinct explanatory fields:
  - "Assumption held without evidence" — the inertia belief that made this gap invisible before commit (why it was not gathered)
  - "Would have surfaced" — what this signal would have revealed (what was missed)
These are different statements and must not be merged.

| Gap (signal type absent) | Namespace | Assumption held without evidence | Skill to run | Would have surfaced | Changed commit? YES / NO |
|--------------------------|-----------|----------------------------------|-------------|---------------------|--------------------------|
| [type] | [namespace] | [the prior belief the team held without evidence — explains why the gap existed] | [exact skill, e.g., /flow-resilience] | [what the signal would have revealed — distinct from the Assumption column] | [verdict] |

"Gather more data" does not satisfy the Skill column. Name an exact skill from the Signal namespace catalog.
If no gaps: "No gaps — signal coverage was sufficient for this commit decision."

Use this template exactly:
  > **Recommendation**: Addresses [Gap: name / Echo: pattern name] by [specific practice change].

PHASE 7 SEAL — confirm before proceeding to Phase 8:
  [ ] Every W or P namespace from Phase 3 has a gap row (or explicit "no gaps")
  [ ] Assumption column: a prior belief per row (not an outcome, not "unknown", not blank)
  [ ] "Would have surfaced" column: a discovery statement distinct from the Assumption (different content)
  [ ] Skill column: exact named skill per row (not generic)
  [ ] Changed commit: YES or NO per row
  [ ] Recommendation template present
All items confirmed? PHASE 7 COMPLETE.

---

PHASE 8 — CALIBRATION TREND

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [reference or "none"] | | | | ↑ improving / ↓ degrading / = stable |

No prior retro: "First retro for this topic — this score establishes the calibration baseline."

PHASE 8 SEAL — confirm before proceeding to Phase 9:
  [ ] Prior retro: named or "none"
  [ ] This score matches Phase 4 TOTAL
  [ ] Trend label present (or "first retro" statement)
All items confirmed? PHASE 8 COMPLETE.

---

PHASE 9 — ECHO → SIGNAL DESIGN
Translate the Phase 1 Echo and its Pattern classification into one concrete change to signal gathering practice.

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [finding] | [pattern name — must match Phase 1 exactly] | [specific change] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL — retro complete when confirmed:
  [ ] Echo finding matches Phase 1 (not paraphrased)
  [ ] Pattern matches Phase 1 Pattern entry (same name)
  [ ] Proposed change: specific (not "gather more data")
  [ ] Change type: one of the three options
All items confirmed? RETRO COMPLETE.

---

Execute phases in order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9.
Each phase seal is a self-containedness contract — the phase cannot defer required fields to a later phase or continuation.
The Assumption column in Phase 7 names the belief that made the gap invisible. It is structurally distinct from "Would have surfaced" — the two columns must state different things. A gap row where both columns say the same thing is incomplete.
```

---

## V-02 — AMEND-Per-Table: C-10 via Per-Table Out-of-Scope Notation

**Axis:** C-10 mechanism — when AMEND scope is set, every table carries an explicit scope marker immediately above it naming the constraint and what is excluded. Phase 2 adds a secondary out-of-scope table listing artifacts that fall outside the AMEND boundary. Phase seals include a conditional AMEND check item.

**Hypothesis:** C-10 scores PARTIAL in all R6 variations because AMEND is declared at the top but not enforced per-table. The rubric's pass condition requires "every table includes an explicit out-of-scope notation." Adding a `{{#if amend}}` conditional scope marker above each table satisfies this structurally — the notation is invisible in normal runs and appears only when AMEND is active. The per-table marker is the mechanism; the top-level declaration alone is not sufficient.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Each phase ends with a PHASE SEAL — a required-field checklist. The phase is not complete until every seal item is confirmed.

{{#if amend}}AMEND SCOPE: {{amend}} — all phases operate within this constraint only. Every table below carries a scope marker.{{/if}}

---

PHASE 1 — ECHO
Run this phase before any signal comparison.

{{#if amend}}[SCOPE: {{amend}} only — outcomes outside this scope are excluded from Echo candidacy]{{/if}}

Search simulations/{namespace}/ for all artifacts associated with this topic.

The Echo is the single post-ship observable satisfying all three conditions:
  (a) Not predicted by any gathered signal — not even partially
  (b) Not a named risk or acknowledged unknown at commit time
  (c) Observable only after the feature shipped

Procedure:
  Step 1: List every post-ship outcome for this topic (within AMEND scope if set).
  Step 2: Eliminate any predicted by a gathered signal (fully or partially).
  Step 3: Eliminate any that were named risks or known unknowns.
  Step 4: From remaining candidates, select exactly one with highest commit-decision impact.
  Step 5: If no candidates remain: Echo = "No Echo — all post-ship outcomes were within signal bounds."

| Echo (one sentence) | Nearest signal artifact | Commit relevance: HIGH / MEDIUM / LOW |
|---------------------|------------------------|--------------------------------------|
| [finding or "No Echo"] | [name or "none"] | [level or "N/A"] |

After the table:
  > **Pattern**: [name] — [description of the recurring failure mode this Echo represents, not just this instance]

Pattern examples: adoption-assumption-gap, integration-surface-miss, timing-signal-gap, scale-behavior-gap, dependency-chain-miss, unknown-unknown, or name your own.

LOCK: This table and Pattern entry are final.

PHASE 1 SEAL — confirm before proceeding to Phase 2:
  [ ] Echo cell: one sentence (or explicit "No Echo" — not a restatement of a wrong prediction)
  [ ] Nearest signal: named artifact or "none"
  [ ] Commit relevance: HIGH, MEDIUM, or LOW (or "N/A")
  [ ] Pattern entry: > **Pattern**: [name] — [description] format (not blank)
  {{#if amend}}[ ] Scope marker present above table naming "{{amend}}"{{/if}}
All items confirmed? PHASE 1 COMPLETE.

---

PHASE 2 — SIGNAL INVENTORY
{{#if amend}}[SCOPE: {{amend}} only — artifacts outside this scope are listed in the out-of-scope table below, not in the main table]{{/if}}

| Namespace | Artifact | Date | Prediction summary |
|-----------|----------|------|--------------------|
| [name] | [filename] | [YYYY-MM-DD] | [one phrase] |

{{#if amend}}Out-of-scope artifacts (excluded per AMEND constraint):
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name if any] | [filename] | [outside {{amend}} scope] |
If none excluded: write "No artifacts excluded — all in scope."
{{/if}}

Namespaces with signals (in scope): [list]
Empty namespaces (from: scout, draft, review, flow, trace, prove, listen, program, topic): [list]
Total: N signals across M namespaces

PHASE 2 SEAL — confirm before proceeding to Phase 3:
  [ ] Every artifact from simulations/ for this topic has a row (in main table or OOS-noted)
  [ ] Empty namespace list accounts for all 9 not in "with signals"
  [ ] Total count stated
  {{#if amend}}[ ] Out-of-scope table present (even if "No artifacts excluded"){{/if}}
All items confirmed? PHASE 2 COMPLETE.

---

PHASE 3 — PREDICTED VS ACTUAL
{{#if amend}}[SCOPE: {{amend}} only — namespaces outside this constraint not included]{{/if}}

For each namespace with at least one Phase 2 in-scope artifact:

| Namespace | Predicted (what signals claimed post-ship) | Actual (what was observed) | Match: C / P / W / ND |
|-----------|--------------------------------------------|----------------------------|-----------------------|
| [name] | [required — cannot be blank] | [required — cannot be blank] | [verdict] |

Verdict: C = Correct, P = Partial, W = Wrong, ND = No data.

PHASE 3 SEAL — confirm before proceeding to Phase 4:
  [ ] Every in-scope namespace from Phase 2 has a row
  [ ] No Predicted cell is blank
  [ ] No Actual cell is blank
  [ ] Every row has a verdict label (C / P / W / ND)
  {{#if amend}}[ ] Scope marker present above table{{/if}}
All items confirmed? PHASE 3 COMPLETE.

---

PHASE 4 — NAMESPACE ACCURACY
{{#if amend}}[SCOPE: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Score: (C×100 + P×50) ÷ (C+P+W) |
|-----------|---|---|---|-----|----------------------------------|
| [name] | | | | | |
| TOTAL | | | | | |

ND excluded from denominator. Score blank if denominator = 0.

PHASE 4 SEAL — confirm before proceeding to Phase 5:
  [ ] Every Phase 3 namespace has a row
  [ ] TOTAL row present
  [ ] Score column: formula applied (blank only when denominator = 0)
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed? PHASE 4 COMPLETE.

---

PHASE 5 — CONFLICT AUDIT
This phase is mandatory. It always produces output.

Review the locked Phase 1 Echo.
Does anything in Phase 3 or Phase 4 suggest the Echo finding should be revised?

If YES — emit:
  CONFLICT DETECTED
  Source: [which finding creates the tension]
  Proposed revision: [what the Echo would become]
  Resolution: Echo preserved unchanged.

If NO — emit:
  CONFLICT AUDIT: No conflict.

PHASE 5 SEAL — confirm before proceeding to Phase 6:
  [ ] Conflict audit question answered
  [ ] Either CONFLICT DETECTED block (with Source, Proposed revision, Resolution) or "No conflict" declaration present
All items confirmed? PHASE 5 COMPLETE.

---

PHASE 6 — ACCURACY VERDICT
  "Signal accuracy for [topic]: [TOTAL score]/100 — [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]"

Reference Phase 4 TOTAL only.

PHASE 6 SEAL — confirm before proceeding to Phase 7:
  [ ] Verdict sentence in required format
  [ ] Score from Phase 4 TOTAL
  [ ] Tier label correct
All items confirmed? PHASE 6 COMPLETE.

---

PHASE 7 — GAP ANALYSIS
{{#if amend}}[SCOPE: {{amend}} only — gaps from outside this constraint excluded]{{/if}}

For each namespace scoring W or P in Phase 3, and each empty namespace where absence is material:

| Gap (signal type absent) | Namespace | Skill to run | Would have surfaced | Changed commit? YES / NO |
|--------------------------|-----------|-------------|---------------------|--------------------------|
| [type] | [namespace] | [exact skill, e.g., /flow-resilience] | [one sentence] | [verdict] |

"Gather more data" does not satisfy the Skill column. Name an exact skill.
If no gaps: "No gaps — coverage sufficient."

> **Recommendation**: Addresses [Gap: name / Echo: pattern name] by [specific practice change].

PHASE 7 SEAL — confirm before proceeding to Phase 8:
  [ ] Every W or P namespace from Phase 3 has a gap row (or "no gaps")
  [ ] Skill column: exact named skill per row
  [ ] Changed commit: YES or NO per row
  [ ] Recommendation template present
  {{#if amend}}[ ] Scope marker present above table{{/if}}
All items confirmed? PHASE 7 COMPLETE.

---

PHASE 8 — CALIBRATION TREND

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [reference or "none"] | | | | ↑ / ↓ / = |

No prior retro: "First retro — this score is the baseline."

PHASE 8 SEAL — confirm before proceeding to Phase 9:
  [ ] Prior retro: named or "none"
  [ ] This score matches Phase 4 TOTAL
  [ ] Trend label or "first retro" statement
All items confirmed? PHASE 8 COMPLETE.

---

PHASE 9 — ECHO → SIGNAL DESIGN

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [finding] | [pattern name — must match Phase 1] | [specific change] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL — retro complete when confirmed:
  [ ] Echo matches Phase 1 (not paraphrased)
  [ ] Pattern matches Phase 1 (same name)
  [ ] Proposed change: specific
  [ ] Change type: one of three options
All items confirmed? RETRO COMPLETE.

---

Execute phases in order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9.
Each phase seal is a self-containedness contract — do not proceed past a phase until its seal passes.
When AMEND is set: every table carries a scope marker naming the constraint, and Phase 2 includes an explicit out-of-scope table. A retro with AMEND declared at the top but without per-table markers has not enforced its scope.
```

---

## V-03 — Namespace-9Row: C-16 via Fixed 9-Row Coverage Table

**Axis:** C-16 mechanism — Phase 2 outputs a fixed 9-row namespace status table (one row per namespace in fixed order: scout, draft, review, flow, trace, prove, listen, program, topic) instead of text lists. Every namespace gets an explicit COVERED / EMPTY status cell and an artifact count.

**Hypothesis:** Text lists can silently omit namespaces; a fixed 9-row table cannot — each row must exist and must have a status. C-16's pass condition requires "a structured table with one explicit row per namespace (all 9)." The fixed-order table satisfies this structurally. The Phase 2 SEAL checks for all 9 rows explicitly, making omission visible as a missing seal item rather than a missing list entry.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Each phase ends with a PHASE SEAL — a required-field checklist.

{{#if amend}}AMEND SCOPE: {{amend}} — all phases operate within this constraint only.{{/if}}

---

PHASE 1 — ECHO
Run this phase before any signal comparison.

Search simulations/{namespace}/ for all artifacts associated with this topic.

The Echo is the single post-ship observable satisfying all three conditions:
  (a) Not predicted by any gathered signal — not even partially
  (b) Not a named risk or acknowledged unknown at commit time
  (c) Observable only after the feature shipped

Procedure:
  Step 1: List every post-ship outcome.
  Step 2: Eliminate any predicted by a gathered signal.
  Step 3: Eliminate named risks or known unknowns.
  Step 4: Select the one with highest commit-decision impact.
  Step 5: No candidates: Echo = "No Echo — all post-ship outcomes were within signal bounds."

| Echo (one sentence) | Nearest signal artifact | Commit relevance: HIGH / MEDIUM / LOW |
|---------------------|------------------------|--------------------------------------|
| [finding or "No Echo"] | [name or "none"] | [level or "N/A"] |

> **Pattern**: [name] — [recurring failure mode this Echo represents, not just this instance]

Pattern examples: adoption-assumption-gap, integration-surface-miss, timing-signal-gap, scale-behavior-gap, dependency-chain-miss, unknown-unknown, or name your own.

LOCK: Echo table and Pattern entry are final.

PHASE 1 SEAL:
  [ ] Echo cell: one sentence (or "No Echo" — not a restatement of a wrong prediction)
  [ ] Nearest signal: named or "none"
  [ ] Commit relevance: HIGH / MEDIUM / LOW (or N/A)
  [ ] Pattern: > **Pattern**: [name] — [description] (not blank)
All items confirmed? PHASE 1 COMPLETE.

---

PHASE 2 — SIGNAL INVENTORY
Produce a fixed 9-row namespace coverage table. Every namespace gets exactly one row regardless of status.

| Namespace | Status | Artifact count | Primary artifact (or "—") | Prediction theme (or "—") |
|-----------|--------|----------------|--------------------------|--------------------------|
| scout     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| draft     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| review    | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| flow      | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| trace     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| prove     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| listen    | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| program   | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| topic     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| TOTAL     |                 | N |                   |                    |

If a namespace has more than one artifact, list additional files in continuation rows immediately below that namespace row.

PHASE 2 SEAL:
  [ ] All 9 namespace rows present in exact order: scout, draft, review, flow, trace, prove, listen, program, topic
  [ ] Every Status cell: exactly "COVERED" or "EMPTY" (not blank)
  [ ] Every Artifact count cell: a number (0 for EMPTY rows)
  [ ] TOTAL row present
All items confirmed? PHASE 2 COMPLETE.

---

PHASE 3 — PREDICTED VS ACTUAL
For each namespace with Status = COVERED in Phase 2:

| Namespace | Predicted (what signals claimed post-ship) | Actual (what was observed) | Match: C / P / W / ND |
|-----------|--------------------------------------------|----------------------------|-----------------------|
| [name] | [required] | [required] | [verdict] |

Verdict: C = Correct, P = Partial, W = Wrong, ND = No data.
Both columns must be explicitly stated for every row.

PHASE 3 SEAL:
  [ ] Every COVERED namespace from Phase 2 has a row
  [ ] No Predicted cell blank
  [ ] No Actual cell blank
  [ ] Verdict label per row (C / P / W / ND)
All items confirmed? PHASE 3 COMPLETE.

---

PHASE 4 — NAMESPACE ACCURACY

| Namespace | C | P | W | ND | Score: (C×100 + P×50) ÷ (C+P+W) |
|-----------|---|---|---|-----|----------------------------------|
| [name] | | | | | |
| TOTAL | | | | | |

ND excluded from denominator. Score blank if denominator = 0.

PHASE 4 SEAL:
  [ ] Every Phase 3 namespace has a row
  [ ] TOTAL row present
  [ ] Score formula applied per row
All items confirmed? PHASE 4 COMPLETE.

---

PHASE 5 — CONFLICT AUDIT
Mandatory. Always produces output.

Does Phase 3 or Phase 4 suggest the Phase 1 Echo should be revised?

If YES:
  CONFLICT DETECTED
  Source: [which finding creates tension]
  Proposed revision: [what Echo would become]
  Resolution: Echo preserved unchanged.

If NO:
  CONFLICT AUDIT: No conflict.

PHASE 5 SEAL:
  [ ] Question answered
  [ ] CONFLICT DETECTED block (Source + Proposed revision + Resolution) or "No conflict" present
All items confirmed? PHASE 5 COMPLETE.

---

PHASE 6 — ACCURACY VERDICT
  "Signal accuracy for [topic]: [TOTAL score]/100 — [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]"

Reference Phase 4 TOTAL only.

PHASE 6 SEAL:
  [ ] Verdict in required format
  [ ] Score from Phase 4 TOTAL
  [ ] Tier label correct
All items confirmed? PHASE 6 COMPLETE.

---

PHASE 7 — GAP ANALYSIS
For each namespace scoring W or P in Phase 3, and each EMPTY namespace (Phase 2) where absence is material:

| Gap (signal type absent) | Namespace | Skill to run | Would have surfaced | Changed commit? YES / NO |
|--------------------------|-----------|-------------|---------------------|--------------------------|
| [type] | [namespace] | [exact skill, e.g., /listen-adoption] | [one sentence] | [verdict] |

Exact Signal skill required per row. "Gather more data" fails.
No gaps: "No gaps — coverage sufficient."

> **Recommendation**: Addresses [Gap: name / Echo: pattern name] by [specific practice change].

PHASE 7 SEAL:
  [ ] Every W or P namespace (Phase 3) has a gap row (or "no gaps")
  [ ] Every EMPTY namespace with material absence has a gap row
  [ ] Skill column: exact skill name per row
  [ ] Changed commit: YES or NO
  [ ] Recommendation template present
All items confirmed? PHASE 7 COMPLETE.

---

PHASE 8 — CALIBRATION TREND

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [reference or "none"] | | | | ↑ / ↓ / = |

No prior retro: "First retro — this score is the baseline."

PHASE 8 SEAL:
  [ ] Prior retro: named or "none"
  [ ] This score matches Phase 4 TOTAL
  [ ] Trend label or "first retro"
All items confirmed? PHASE 8 COMPLETE.

---

PHASE 9 — ECHO → SIGNAL DESIGN

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [finding] | [name — must match Phase 1] | [specific] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL:
  [ ] Echo matches Phase 1 (not paraphrased)
  [ ] Pattern name matches Phase 1
  [ ] Proposed change: specific
  [ ] Change type: one of three
All items confirmed? RETRO COMPLETE.

---

Execute phases in order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9.
Phase 2 uses a fixed 9-row namespace table — every namespace has an explicit row in fixed order. COVERED and EMPTY are the only valid status values. This eliminates namespace-list drift and makes coverage auditable row by row.
Each phase seal is a self-containedness contract — do not proceed until every item is confirmed.
```

---

## V-04 — Assumption+AMEND: C-20 + C-10 Combined

**Axes:** C-20 (assumption column in gap table) + C-10 (AMEND per-table notation). Combines the single-axis changes from V-01 and V-02.

**Hypothesis:** Both mechanisms are structurally independent. The assumption column modifies only Phase 7; AMEND notation adds conditional scope markers above each table. No interference is expected. The combination tests whether both criteria can be satisfied simultaneously without degrading scores on other criteria — if the combined variation scores at or above the individual single-axis variations, it confirms zero interference.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Each phase ends with a PHASE SEAL — a required-field checklist. The phase is not complete until every seal item is confirmed.

{{#if amend}}AMEND SCOPE: {{amend}} — all phases operate within this constraint only. Every table carries an explicit scope marker.{{/if}}

---

PHASE 1 — ECHO
{{#if amend}}[SCOPE: {{amend}} only — outcomes outside this scope excluded]{{/if}}

Run this phase before any signal comparison.
Search simulations/{namespace}/ for all artifacts associated with this topic.

The Echo is the single post-ship observable satisfying all three conditions:
  (a) Not predicted by any gathered signal — not even partially
  (b) Not a named risk or acknowledged unknown at commit time
  (c) Observable only after the feature shipped

Procedure:
  Step 1: List every post-ship outcome (within AMEND scope if set).
  Step 2: Eliminate any predicted by a gathered signal.
  Step 3: Eliminate named risks or known unknowns.
  Step 4: Select the one with highest commit-decision impact.
  Step 5: No candidates: Echo = "No Echo — all post-ship outcomes were within signal bounds."

| Echo (one sentence) | Nearest signal artifact | Commit relevance: HIGH / MEDIUM / LOW |
|---------------------|------------------------|--------------------------------------|
| [finding or "No Echo"] | [name or "none"] | [level or "N/A"] |

> **Pattern**: [name] — [recurring failure mode this Echo represents, not just this instance]

Pattern examples: adoption-assumption-gap, integration-surface-miss, timing-signal-gap, scale-behavior-gap, dependency-chain-miss, unknown-unknown, or name your own.

LOCK: Echo table and Pattern entry final.

PHASE 1 SEAL:
  [ ] Echo cell: one sentence (or "No Echo" — not a restatement of a wrong prediction)
  [ ] Nearest signal: named or "none"
  [ ] Commit relevance: HIGH / MEDIUM / LOW (or N/A)
  [ ] Pattern: > **Pattern**: [name] — [description] (not blank, not generic)
  {{#if amend}}[ ] AMEND scope marker present above table naming "{{amend}}"{{/if}}
All items confirmed? PHASE 1 COMPLETE.

---

PHASE 2 — SIGNAL INVENTORY
{{#if amend}}[SCOPE: {{amend}} only — out-of-scope artifacts listed below with OOS marker]{{/if}}

| Namespace | Artifact | Date | Prediction summary |
|-----------|----------|------|--------------------|
| [name] | [filename] | [YYYY-MM-DD] | [one phrase] |

{{#if amend}}Out-of-scope artifacts:
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name if any] | [filename] | [outside {{amend}} scope] |
If none: "No artifacts excluded — all in scope."
{{/if}}

Namespaces with signals (in scope): [list]
Empty namespaces (from: scout, draft, review, flow, trace, prove, listen, program, topic): [list]
Total: N signals across M namespaces

PHASE 2 SEAL:
  [ ] Every artifact has a row (in scope or OOS-noted)
  [ ] Empty namespace list accounts for all 9
  [ ] Total count stated
  {{#if amend}}[ ] OOS table present (even if "No artifacts excluded"){{/if}}
All items confirmed? PHASE 2 COMPLETE.

---

PHASE 3 — PREDICTED VS ACTUAL
{{#if amend}}[SCOPE: {{amend}} only]{{/if}}

| Namespace | Predicted (what signals claimed post-ship) | Actual (what was observed) | Match: C / P / W / ND |
|-----------|--------------------------------------------|----------------------------|-----------------------|
| [name] | [required] | [required] | [verdict] |

C = Correct, P = Partial, W = Wrong, ND = No data.

PHASE 3 SEAL:
  [ ] Every in-scope namespace has a row
  [ ] No Predicted blank
  [ ] No Actual blank
  [ ] Verdict label per row
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed? PHASE 3 COMPLETE.

---

PHASE 4 — NAMESPACE ACCURACY
{{#if amend}}[SCOPE: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Score: (C×100 + P×50) ÷ (C+P+W) |
|-----------|---|---|---|-----|----------------------------------|
| [name] | | | | | |
| TOTAL | | | | | |

ND excluded from denominator. Score blank if denominator = 0.

PHASE 4 SEAL:
  [ ] Every Phase 3 namespace has a row
  [ ] TOTAL row present
  [ ] Score formula applied
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed? PHASE 4 COMPLETE.

---

PHASE 5 — CONFLICT AUDIT
Mandatory.

Does Phase 3 or Phase 4 suggest the Phase 1 Echo should be revised?

If YES:
  CONFLICT DETECTED
  Source: [finding]
  Proposed revision: [what Echo would become]
  Resolution: Echo preserved.

If NO:
  CONFLICT AUDIT: No conflict.

PHASE 5 SEAL:
  [ ] Question answered
  [ ] CONFLICT DETECTED block or "No conflict" present
All items confirmed? PHASE 5 COMPLETE.

---

PHASE 6 — ACCURACY VERDICT
  "Signal accuracy for [topic]: [TOTAL score]/100 — [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]"

PHASE 6 SEAL:
  [ ] Verdict in required format
  [ ] Score from Phase 4 TOTAL
  [ ] Tier label correct
All items confirmed? PHASE 6 COMPLETE.

---

PHASE 7 — GAP ANALYSIS
{{#if amend}}[SCOPE: {{amend}} only — gaps outside this constraint excluded]{{/if}}

A gap entry has two required fields that must state different things:
  - "Assumption held without evidence": the belief that made this gap invisible before commit — why the team did not gather this signal
  - "Would have surfaced": what this signal would have revealed — the discovery that was missed

| Gap (signal type absent) | Namespace | Assumption held without evidence | Skill to run | Would have surfaced | Changed commit? YES / NO |
|--------------------------|-----------|----------------------------------|-------------|---------------------|--------------------------|
| [type] | [ns] | [prior belief — "We assumed X" or equivalent inertia framing — not an outcome] | [exact skill] | [what the signal would have revealed — distinct from Assumption] | YES / NO |

The Assumption and "Would have surfaced" columns must contain different statements. A row where both say the same thing has collapsed the distinction and is incomplete.

"Gather more data" does not satisfy Skill. Name an exact Signal skill.
No gaps: "No gaps — coverage sufficient."

> **Recommendation**: Addresses [Gap: name / Echo: pattern name] by [specific practice change].

PHASE 7 SEAL:
  [ ] Every W or P namespace (Phase 3) has a gap row (or "no gaps")
  [ ] Assumption column: a prior belief per row (not an outcome, not blank)
  [ ] "Would have surfaced": distinct from Assumption (different content)
  [ ] Skill column: exact named skill per row
  [ ] Changed commit: YES or NO per row
  [ ] Recommendation template present
  {{#if amend}}[ ] Scope marker present above table{{/if}}
All items confirmed? PHASE 7 COMPLETE.

---

PHASE 8 — CALIBRATION TREND

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [reference or "none"] | | | | ↑ / ↓ / = |

No prior retro: "First retro — this score is the baseline."

PHASE 8 SEAL:
  [ ] Prior retro: named or "none"
  [ ] This score matches Phase 4 TOTAL
  [ ] Trend label or "first retro"
All items confirmed? PHASE 8 COMPLETE.

---

PHASE 9 — ECHO → SIGNAL DESIGN

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [finding] | [name — must match Phase 1 exactly] | [specific] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL:
  [ ] Echo matches Phase 1 (not paraphrased)
  [ ] Pattern matches Phase 1 (same name)
  [ ] Change: specific
  [ ] Change type: one of three
All items confirmed? RETRO COMPLETE.

---

Execute phases in order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9.
Each phase seal is a self-containedness contract — do not proceed past a phase until its seal passes.
When AMEND is set: every table carries a scope marker, and Phase 2 includes an OOS table. Top-level declaration alone is not enforcement.
Phase 7 Assumption column names the belief that made the gap invisible. It is structurally distinct from "Would have surfaced." Both columns are required and must contain different content.
```

---

## V-05 — Full-Integration: C-20 + C-10 + C-15 + C-16 + C-21 Strengthened

**Axes:** All four persistent PARTIAL criteria from R6 addressed simultaneously, plus C-21 seal strengthening:
- C-20: dedicated "Assumption held without evidence" column in Phase 7 gap table
- C-10: per-table AMEND scope markers + OOS secondary table in Phase 2
- C-15: explicit N/M=X% count ratio in Phase 4 alongside weighted formula
- C-16: fixed 9-row namespace status table in Phase 2
- C-21: seals with maximally explicit format strings (not just field names — exact required format per field)

**Hypothesis:** All five mechanisms are structurally independent with no shared phase. The primary risk is prompt volume reducing salience of critical instructions — the Phase 7 assumption column must remain prominently framed despite the length added by 9-row coverage, AMEND tables, and ratio calculations. If V-05 scores lower on any prior-passing criterion, the regression identifies which mechanism introduced the interference.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, identify gaps. Each phase ends with a PHASE SEAL — an explicit field-enumerated checklist confirming all required outputs are populated in their required format. Do not proceed past a phase until its seal passes.

{{#if amend}}AMEND SCOPE: {{amend}} — all phases operate within this constraint only. Every table carries an explicit scope marker. Phase 2 includes an out-of-scope table.{{/if}}

---

PHASE 1 — ECHO
Run this phase before examining any signal predictions.

{{#if amend}}[AMEND: {{amend}} only — outcomes outside this scope excluded from Echo candidacy]{{/if}}

Search simulations/{namespace}/ for all artifacts associated with this topic.

The Echo is the single post-ship observable satisfying all three conditions:
  (a) Not predicted by any gathered signal — not even partially
  (b) Not a named risk or acknowledged unknown at commit time
  (c) Observable only after the feature shipped

Procedure:
  Step 1: List every post-ship outcome (within AMEND scope if set).
  Step 2: Eliminate outcomes predicted by gathered signals.
  Step 3: Eliminate named risks or known unknowns.
  Step 4: Select the one with highest commit-decision impact.
  Step 5: No candidates: Echo = "No Echo — all post-ship outcomes were within signal bounds."

| Echo (one sentence) | Nearest signal artifact | Commit relevance: HIGH / MEDIUM / LOW |
|---------------------|------------------------|--------------------------------------|
| [finding or "No Echo — all post-ship outcomes were within signal bounds"] | [name or "none"] | [HIGH / MEDIUM / LOW or "N/A"] |

Immediately after the table, name the systemic pattern:
  > **Pattern**: [name from taxonomy or "other: [your name]"] — [description of the recurring failure mode this Echo represents — not a restatement of the Echo, but the class of failure it belongs to]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

LOCK: Echo table and Pattern entry are final. Phases 2–8 may not change them.

PHASE 1 SEAL — all four fields must be explicitly populated before Phase 2 begins:
  [ ] Echo cell: exactly one sentence OR the exact string "No Echo — all post-ship outcomes were within signal bounds" (not blank, not a paraphrase of a wrong prediction)
  [ ] Nearest signal: a named artifact filename OR the exact string "none" (not blank, not "N/A")
  [ ] Commit relevance: exactly HIGH, MEDIUM, or LOW (or "N/A" only when paired with "No Echo")
  [ ] Pattern: exactly "> **Pattern**: [name from taxonomy or "other: [name]"] — [description that names the failure class, not the Echo instance]" (not blank, not generic, not a restatement of the Echo sentence)
  {{#if amend}}[ ] AMEND scope marker present immediately above table naming "{{amend}}"{{/if}}
All items confirmed? PHASE 1 COMPLETE.

---

PHASE 2 — SIGNAL INVENTORY
Produce a fixed 9-row namespace coverage table. Every namespace gets exactly one row.

{{#if amend}}[AMEND: {{amend}} only — out-of-scope artifacts go to the OOS table below, not the main table]{{/if}}

| Namespace | Status     | Artifact count | Primary artifact (or "—") | Prediction theme (or "—") |
|-----------|------------|----------------|--------------------------|--------------------------|
| scout     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| draft     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| review    | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| flow      | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| trace     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| prove     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| listen    | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| program   | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| topic     | COVERED / EMPTY | N | [filename or "—"] | [one phrase or "—"] |
| TOTAL     |            | N |                   |                    |

If a namespace has more than one artifact, list additional files in continuation rows below that row.

{{#if amend}}Out-of-scope artifacts (excluded per AMEND constraint):
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside {{amend}} scope] |
If none excluded: "No artifacts excluded — all in scope."
{{/if}}

PHASE 2 SEAL — all items required before Phase 3 begins:
  [ ] All 9 namespace rows present in exact order: scout, draft, review, flow, trace, prove, listen, program, topic
  [ ] Every Status cell: exactly "COVERED" or "EMPTY" (no other value, no blank)
  [ ] Every Artifact count cell: a number (0 is valid for EMPTY; blank is not)
  [ ] TOTAL row present with summed count
  {{#if amend}}[ ] OOS table present immediately after main table (even if "No artifacts excluded"){{/if}}
All items confirmed? PHASE 2 COMPLETE.

---

PHASE 3 — PREDICTED VS ACTUAL
For each namespace with Status = COVERED in Phase 2:

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted (signals' collective claim post-ship) | Actual (what was observed post-ship) | Match: C / P / W / ND |
|-----------|------------------------------------------------|--------------------------------------|----------------------|
| [name] | [required — non-blank statement] | [required — non-blank statement] | [C / P / W / ND] |

C = Correct, P = Partial (direction right, magnitude/timing off), W = Wrong, ND = No post-ship data yet.

PHASE 3 SEAL:
  [ ] Every COVERED namespace from Phase 2 has exactly one row
  [ ] No Predicted cell is blank or contains only "N/A"
  [ ] No Actual cell is blank or contains only "N/A"
  [ ] Every Match cell: exactly C, P, W, or ND (no other values)
  {{#if amend}}[ ] Scope marker present above table{{/if}}
All items confirmed? PHASE 3 COMPLETE.

---

PHASE 4 — NAMESPACE ACCURACY
{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Weighted score: (C×100 + P×50) ÷ (C+P+W) |
|-----------|---|---|---|-----|------------------------------------------|
| [name] | | | | | |
| TOTAL | | | | | |

ND excluded from denominator. Score blank if denominator = 0.

After the scoring table, state the simple count-based accuracy ratio:
  Correct signals: [count of C rows] / [count of C+P+W rows] = X%
  (Count-based ratio — not weighted. Both numbers required.)

PHASE 4 SEAL:
  [ ] Every Phase 3 namespace has a row
  [ ] TOTAL row present with weighted formula applied
  [ ] Count-based accuracy ratio stated in N/M = X% format immediately below scoring table
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed? PHASE 4 COMPLETE.

---

PHASE 5 — CONFLICT AUDIT
Mandatory. Always produces one of two outputs.

Review the locked Phase 1 Echo.
Does any Phase 3 verdict or Phase 4 score suggest the Echo should name a different finding?

If YES:
  CONFLICT DETECTED
  Source: [Phase 3 row / Phase 4 score — which specific finding creates the tension]
  Analysis: [what the finding suggests the Echo should be]
  Resolution: Phase 1 Echo is preserved unchanged. This block is the conflict artifact.

If NO:
  CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo.

PHASE 5 SEAL:
  [ ] One of the two outputs present: either CONFLICT DETECTED block (with Source, Analysis, Resolution all present) or the exact "No conflict" declaration
  [ ] Nothing in Phase 5 modifies the Phase 1 Echo table or Pattern entry
All items confirmed? PHASE 5 COMPLETE.

---

PHASE 6 — ACCURACY VERDICT
  "Signal accuracy for [topic]: [TOTAL weighted score]/100 — [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]. Count accuracy: [N/M = X%]."

Draw the weighted score from Phase 4 TOTAL row. Draw the count ratio from Phase 4 count-based statement. Do not recalculate.

PHASE 6 SEAL:
  [ ] Verdict sentence present in the exact required format (both weighted score and count ratio)
  [ ] Weighted score matches Phase 4 TOTAL row (same number, not recalculated)
  [ ] Count ratio matches Phase 4 N/M = X% statement (same values)
  [ ] Tier label (STRONG / ADEQUATE / WEAK) matches the stated weighted score
All items confirmed? PHASE 6 COMPLETE.

---

PHASE 7 — GAP ANALYSIS
For each namespace scoring W or P in Phase 3, and each EMPTY namespace (Phase 2) where absence is material to the commit decision:

{{#if amend}}[AMEND: {{amend}} only — gaps outside this constraint excluded]{{/if}}

A gap entry has two required explanatory fields that must state different things:
  - "Assumption held without evidence": the inertia belief that made this gap invisible before commit. Why the team did not gather this signal. Framed as a prior belief ("We assumed X" or equivalent), not as an outcome.
  - "Would have surfaced": what this signal would have revealed. The discovery that was missed. This is the outcome; the Assumption is the belief that prevented gathering it.

| Gap (signal type absent) | Namespace | Assumption held without evidence | Skill to run | Would have surfaced | Changed commit? YES / NO |
|--------------------------|-----------|----------------------------------|-------------|---------------------|--------------------------|
| [type] | [ns] | [prior belief, e.g., "We assumed X was true without evidence"] | [exact skill, e.g., /listen-support] | [what the signal would have revealed — distinct from the Assumption column] | YES / NO |

Validation: the Assumption and "Would have surfaced" columns must contain different statements addressing different questions. If they are the same statement, one column is wrong.

"Gather more data" does not satisfy the Skill column. Name an exact Signal namespace skill.
No gaps: "No gaps — signal coverage was sufficient for this commit decision."

> **Recommendation**: Addresses [Gap: name / Echo: pattern name] by [specific practice change].

PHASE 7 SEAL:
  [ ] Every W or P namespace from Phase 3 has a gap row (or "no gaps" statement)
  [ ] Every EMPTY namespace with material absence has a gap row
  [ ] Assumption column: a prior belief per row — framed as a belief ("We assumed X"), not as an outcome, not blank, not "unknown"
  [ ] "Would have surfaced" column: a discovery statement per row — distinct from the Assumption (answers "what", not "why")
  [ ] Skill column: exact Signal skill name per row (not a namespace name, not "gather more data")
  [ ] Changed commit: exactly YES or NO per row
  [ ] Recommendation template present with Gap/Echo name and practice change filled in
  {{#if amend}}[ ] AMEND scope marker present above gap table{{/if}}
All items confirmed? PHASE 7 COMPLETE.

---

PHASE 8 — CALIBRATION TREND

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [reference or "none"] | | | | ↑ improving / ↓ degrading / = stable |

No prior retro: "First retro for this topic — this score establishes the calibration baseline."

PHASE 8 SEAL:
  [ ] Prior retro: named topic/date or exactly "none"
  [ ] This score: matches Phase 4 TOTAL weighted score (same number)
  [ ] Trend: exactly ↑, ↓, or = with a label, or "first retro" statement
All items confirmed? PHASE 8 COMPLETE.

---

PHASE 9 — ECHO → SIGNAL DESIGN
Translate the Phase 1 Echo and Pattern into one concrete practice change.

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [exact Echo cell content — not paraphrased] | [exact Pattern name from Phase 1 — same taxonomy label, not a synonym] | [one specific practice change — not "gather more signals"] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL — retro is complete when all confirmed:
  [ ] Echo cell: matches Phase 1 Echo cell content exactly (not paraphrased, not summarized)
  [ ] Pattern cell: matches Phase 1 Pattern name exactly (same taxonomy label used in Phase 1)
  [ ] Proposed change: specific and actionable (not generic, not "gather more data")
  [ ] Change type: exactly one of: new skill, rubric amendment, threshold adjustment
All items confirmed? RETRO COMPLETE.

---

Execute phases in order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9.

Design guarantees:
- Phase 2: fixed 9-row namespace table (all 9 accounted for explicitly; COVERED or EMPTY only).
- Phase 4: both weighted score AND N/M=X% count ratio — two accuracy formats, both required.
- Phase 6: verdict sentence must include both score formats drawn from Phase 4.
- Phase 7: two distinct columns per gap — Assumption (why it was invisible) and Would have surfaced (what was missed).
- Every phase seal enumerates exact required content with format strings, not just field names.
- When AMEND is set: every table has a scope marker and Phase 2 has an OOS secondary table.

Each phase seal is a self-containedness contract. A phase that cannot pass its own seal is incomplete — do not proceed.
```

---

## Summary Table

| ID | Primary Axes | C-20 Mechanism | C-10 Mechanism | C-15 Mechanism | C-16 Mechanism | C-21 Mechanism | Hypothesis |
|----|-------------|----------------|----------------|----------------|----------------|----------------|------------|
| V-01 | C-20 (single axis) | Dedicated "Assumption held without evidence" column in Phase 7 gap table; Phase 7 SEAL checks that Assumption and "Would have surfaced" are distinct | None (scope declared at top only) | None (weighted formula only) | None (text lists) | Phase seals from R6-V02 baseline | Structural column forces assumption to be stated per gap row — same mechanism as C-14 (verdict label via column) now applied to inertia framing |
| V-02 | C-10 (single axis) | None (Phase 7 unchanged from R6-V02) | {{#if amend}} scope marker above every table + OOS secondary table in Phase 2; phase seals include AMEND-conditional item | None | None | Phase seals from R6-V02 baseline | Per-table scope markers satisfy "every table includes out-of-scope notation" — top-level AMEND declaration is necessary but not sufficient |
| V-03 | C-16 (single axis) | None | None | None | Fixed 9-row namespace table in Phase 2 with COVERED/EMPTY status per row; TOTAL row required | Phase seals from R6-V02 baseline | Fixed-order 9-row table prevents namespace omission — a missing row is a visible structural gap, not a missing list entry |
| V-04 | C-20 + C-10 (combined) | Assumption column in Phase 7; Assumption vs surfaced distinction enforced by SEAL | Per-table AMEND markers + Phase 2 OOS table + SEAL items | None | None | Phase seals from R6-V02 baseline | Tests zero-interference assumption: both mechanisms modify different phases and different tables |
| V-05 | C-20 + C-10 + C-15 + C-16 + C-21 (full integration) | Assumption column with "We assumed X" framing; SEAL requires belief-vs-outcome distinction per row | Per-table AMEND markers + Phase 2 OOS table | N/M=X% count ratio in Phase 4 + both formats in Phase 6 verdict | Fixed 9-row namespace table in Phase 2 | Seals use exact format strings per field (not just field names) across all 9 phases | Maximum ceiling test — all four PARTIAL criteria addressed plus seal strengthening; regression on any prior-passing criterion identifies interference |
