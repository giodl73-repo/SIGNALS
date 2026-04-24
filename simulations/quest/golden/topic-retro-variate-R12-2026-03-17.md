# topic-retro — Variations R12
**Date:** 2026-03-17
**Rubric:** v10 (C-01 through C-31; total available = 136)
**R11 top scorer:** V-05 (source of C-30, C-31 criteria) — Phase 8 SEAL COPY-VERIFIED label + design-guarantees summary.
**New criteria to target:** C-30 (phase-8-seal-copy-verified-label-and-source) and C-31 (design-guarantees-summary-explicit).

**Base used:** R11-V-05 — all R11 integrations carried forward:
- C-22: OOS secondary table
- C-23: Seal format-contract strings per field (all 9 phases)
- C-24: Echo why-unexpected explained
- C-25: Three-slot recommendation template
- C-26: Gap inertia columns A/B structurally isolated
- C-27: SEAL coverage extended to all phases
- C-28: `[slot:X]` token + SEAL placeholder check
- C-29: Phase 8 "do not recompute" + SEAL copy-citation check

**C-30 gap analysis:** R11-V-05's Phase 8 SEAL already carries "COPY-VERIFIED" as a label and "Phase 6 verdict" as a named source, but both are embedded as inline commentary on the single "This score" checklist item. C-30 requires the SEAL to encode the verified state AND the origin as *named fields* — elevating from inline annotation to two independent, addressable items. A scorer auditing C-30 looks for two discrete entries; finding them merged into one item = PARTIAL.

**C-31 gap analysis:** R11-V-05's design-guarantees block is a trailing bullet list positioned after Phase 9. It names specific mechanisms (slot template, SEAL slot check, copy guard) and satisfies the content requirement. The gap is structural: a bullet list appended to a long prompt reads as a summary note, not a "dedicated section." C-31 requires a section clearly separated from the phase specifications — a header-titled block or table that a reviewer can locate without reading to the end.

**Single-axis:** V-01 (C-30), V-02 (C-31), V-03 (phrasing register).
**Combined:** V-04 (C-30 + C-31), V-05 (C-30 + C-31 + pre-execution contract placement).

---

## Summary Table

| ID | Primary Axis | C-30 Mechanism | C-31 Mechanism | Placement | Hypothesis |
|----|-------------|----------------|----------------|-----------|------------|
| V-01 | C-30 (single) | Phase 8 SEAL: three separate named items — `This score`, `COPY-VERIFIED`, `COPY-SOURCE` | R11-V-05 trailing bullet list | Post-phases | Splitting the merged checklist item into three independent entries makes each independently addressable; COPY-VERIFIED and COPY-SOURCE become named fields, not inline commentary |
| V-02 | C-31 (single) | R11-V-05 SEAL structure (COPY-VERIFIED inline on "This score" item) | Trailing bullet list replaced by `## DESIGN GUARANTEES` two-column table with header | Post-phases | A header-titled table creates a structurally dedicated section; a reviewer can locate it without reading to the end; two-column form (Mechanism / Guarantee) makes each guarantee auditable by name |
| V-03 | Phrasing register (single) | Phase 8 SCORE TRANSFER COMMAND block: four imperative steps, step 3 names COPY-VERIFIED and Phase 6 verdict explicitly | EXECUTION CONTRACT header block with imperative lines per mechanism | Post-phases | Command-register prose without structural tokens tests whether behavioral compliance framing achieves C-30 and C-31 without additional checklist complexity |
| V-04 | C-30 + C-31 (combined) | Three-field SEAL (from V-01) | `## DESIGN GUARANTEES` table (from V-02) | Post-phases | Zero-interference test: C-30 lives in Phase 8 SEAL; C-31 lives in design-guarantees section; independent locations |
| V-05 | Full integration | Three-field SEAL (from V-01) + Phase 8 table cell carries inline COPY-VERIFIED [Phase 6 verdict] format string | `## DESIGN GUARANTEES` table promoted to pre-Phase-1 position as PRE-EXECUTION CONTRACT; trailing reference block retained | Pre-phases (contract) + post-phases (reference) | Positioning the guarantees before Phase 1 makes them structurally prior to execution — a prospective contract, not a retrospective summary. Maximum structural redundancy for C-30: three independent locations (body instruction, SEAL field, table-cell format string) |

---

## V-01 — SEAL Separation: C-30 via Three Named Fields in Phase 8 SEAL

**Axis:** C-30 mechanism. The Phase 8 SEAL restructures the score-transfer check from one item with inline commentary into three separate, independently addressable items: `This score`, `COPY-VERIFIED`, and `COPY-SOURCE`. Each is a named checklist field with its own format constraint. The Phase 8 body adds an explicit instruction to label the "This score" cell with the verification state and source.

**Hypothesis:** R11-V-05 embeds COPY-VERIFIED as a modifier clause on the "This score" item: `[ ] This score: {number}/100 — COPY-VERIFIED: confirm...`. A rubric auditor looking for "both a named verification label and an explicit copy-source specification as named fields" finds both present but fused. Splitting them into three distinct items (`This score` / `COPY-VERIFIED` / `COPY-SOURCE`) makes each independently confirmable and removes the ambiguity about whether they constitute "named fields." All phases outside Phase 8 SEAL are unchanged from R11-V-05.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Each phase ends with a PHASE SEAL — a format-contract checklist. Every seal item specifies both the required field and its required value form. Do not proceed past a phase until every seal item is confirmed against the stated format.

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

Immediately after the table:
  > **Pattern**: [name from taxonomy or "other: [your name]"] — [description of the recurring failure mode — not a restatement of the Echo, but the class of failure it belongs to]
  > **Why unexpected**: [which prior belief, model, or assumption this finding contradicted — what the author expected, and why reality diverged]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

LOCK: Echo table, Pattern, and Why-unexpected are final. Phases 2–9 may not change them.

PHASE 1 SEAL — format contract:
  [ ] Echo: {one sentence describing post-ship finding} OR the exact string "No Echo — all post-ship outcomes were within signal bounds" — not blank, not a restatement of a wrong prediction
  [ ] Nearest signal: {artifact-filename.md} OR the exact string "none" — not blank, not "N/A", not a namespace name
  [ ] Commit relevance: one of exactly: HIGH | MEDIUM | LOW | N/A — "N/A" only valid when paired with "No Echo"
  [ ] Pattern: "> **Pattern**: {taxonomy-label or "other: name"} — {description of failure class, not the Echo instance}" — not blank; description not a restatement of the Echo sentence
  [ ] Why unexpected: "> **Why unexpected**: {prior belief or model contradicted} — must identify what was expected, not just assert unexpectedness"
  {{#if amend}}[ ] AMEND scope marker: "[AMEND: {{amend}} only — ...]" present immediately above table{{/if}}
All items confirmed against format? PHASE 1 COMPLETE.

---

PHASE 2 — SIGNAL INVENTORY
Produce a fixed 9-row namespace coverage table. Every namespace gets exactly one row.

{{#if amend}}[AMEND: {{amend}} only — out-of-scope artifacts go to the OOS table below, not the main table]{{/if}}

| Namespace | Status          | Artifact count | Primary artifact (or "—") | Prediction theme (or "—") |
|-----------|-----------------|----------------|--------------------------|--------------------------|
| scout     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| draft     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| review    | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| flow      | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| trace     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| prove     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| listen    | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| program   | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| topic     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| TOTAL     |                 | N              |                          |                          |

If a namespace has more than one artifact, list additional files in continuation rows below that row.

{{#if amend}}Out-of-scope artifacts (excluded per AMEND constraint):
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside {{amend}} scope] |
If none excluded: "No artifacts excluded — all in scope."
{{/if}}

PHASE 2 SEAL — format contract:
  [ ] All 9 namespace rows present in exact order: scout, draft, review, flow, trace, prove, listen, program, topic — missing row = incomplete
  [ ] Status: {COVERED} or {EMPTY} per row — no other value, no blank
  [ ] Artifact count: {integer} per row — blank invalid; 0 valid for EMPTY
  [ ] Primary artifact: {filename.md} or the string "—" — not blank
  [ ] TOTAL row: present with format {integer} in Artifact count cell
  {{#if amend}}[ ] OOS table: present immediately after main table — even if "No artifacts excluded — all in scope."{{/if}}
All items confirmed against format? PHASE 2 COMPLETE.

---

PHASE 3 — PREDICTED VS ACTUAL
For each namespace with Status = COVERED in Phase 2:

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted (signals' collective claim post-ship) | Actual (what was observed post-ship) | Match: C / P / W / ND |
|-----------|------------------------------------------------|--------------------------------------|----------------------|
| [name] | [required — non-blank statement] | [required — non-blank statement] | [C / P / W / ND] |

C = Correct, P = Partial (direction right, magnitude/timing off), W = Wrong, ND = No post-ship data yet.

PHASE 3 SEAL — format contract:
  [ ] Row count: one row per COVERED namespace from Phase 2 — no omissions, no extras
  [ ] Predicted: {one phrase or sentence describing what signals claimed} — not blank, not "N/A", not "unknown"
  [ ] Actual: {one phrase or sentence describing what was observed} — not blank, not "N/A", not "unknown"
  [ ] Match: one of exactly: C | P | W | ND — no other values, no blank
  {{#if amend}}[ ] Scope marker: "[AMEND: {{amend}} only]" present above table{{/if}}
All items confirmed against format? PHASE 3 COMPLETE.

---

PHASE 4 — NAMESPACE ACCURACY
{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Weighted score: (C×100 + P×50) ÷ (C+P+W) |
|-----------|---|---|---|-----|------------------------------------------|
| [name]    |   |   |   |     |                                          |
| TOTAL     |   |   |   |     |                                          |

ND excluded from denominator. Score blank if denominator = 0 (note as "0 scored signals").

After the scoring table, state the count-based accuracy ratio:
  Correct signals: {C count} / {C+P+W count} = X%
  (Count-based, not weighted. Both numbers required.)

PHASE 4 SEAL — format contract:
  [ ] Row count: one row per Phase 3 namespace — no omissions
  [ ] C, P, W, ND columns: {integer} per cell — blank invalid; 0 valid
  [ ] Weighted score: {number}/100 per row OR blank with note "0 scored signals" when denominator = 0
  [ ] TOTAL row: present with weighted formula applied — format: {number}/100
  [ ] Count-based ratio: stated immediately below scoring table in exact format "{N}/{M} = {X}%" — both N and M required
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed against format? PHASE 4 COMPLETE.

---

PHASE 5 — CONFLICT AUDIT
Mandatory. Always produces exactly one of two outputs.

Review the locked Phase 1 Echo. Does any Phase 3 verdict or Phase 4 score suggest the Echo should name a different finding?

If YES:
  CONFLICT DETECTED
  Source: {Phase 3 row namespace / Phase 4 score — specific finding that creates the tension}
  Analysis: {what the finding suggests the Echo should become}
  Resolution: Phase 1 Echo is preserved unchanged. This block is the conflict artifact.

If NO:
  CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo.

PHASE 5 SEAL — format contract:
  [ ] Output: exactly one of — CONFLICT DETECTED block (with Source, Analysis, Resolution all present and non-blank) OR the exact string "CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo."
  [ ] Phase 1 modification: none — Echo table, Pattern, and Why-unexpected must be unchanged
All items confirmed against format? PHASE 5 COMPLETE.

---

PHASE 6 — ACCURACY VERDICT
Draw the weighted score from Phase 4 TOTAL row. Draw the count ratio from Phase 4 count-based statement. Do not recalculate either number.

State the verdict:
  "Signal accuracy for [topic]: [TOTAL weighted score]/100 — [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]. Count accuracy: [N/M = X%]."

PHASE 6 SEAL — format contract:
  [ ] Verdict sentence: present in exact format "Signal accuracy for {topic}: {score}/100 — {STRONG|ADEQUATE|WEAK}. Count accuracy: {N}/{M} = {X}%."
  [ ] Weighted score: {score} drawn from Phase 4 TOTAL row — same number, not recalculated (verify by reading Phase 4 TOTAL)
  [ ] Count ratio: {N}/{M} = {X}% drawn from Phase 4 count-based statement — same values, not recalculated
  [ ] Tier label: STRONG if score >= 75 | ADEQUATE if 50 <= score < 75 | WEAK if score < 50 — must match stated score
All items confirmed against format? PHASE 6 COMPLETE.

---

PHASE 7 — GAP ANALYSIS
For each namespace scoring W or P in Phase 3, and each EMPTY namespace (Phase 2) where absence is material to the commit decision:

{{#if amend}}[AMEND: {{amend}} only — gaps outside this constraint excluded]{{/if}}

The gap table carries two structurally isolated columns that must contain different statements:
  - Column A — "Assumption held without evidence": the inertia belief that made this gap invisible before commit. WHY the gap existed. Framed as a prior belief ("We assumed X"), not as an outcome.
  - Column B — "Would have surfaced": the discovery missed. WHAT was missed. Different statement from Column A.
  Validation: if Column A and Column B contain the same statement, one column is wrong. Do not proceed with a merged row.

| Gap (signal type absent) | Namespace | Assumption held without evidence [A] | Skill to run | Would have surfaced [B] | Changed commit? YES / NO |
|--------------------------|-----------|--------------------------------------|-------------|-------------------------|--------------------------|
| [type] | [ns] | [prior belief — "We assumed X" — NOT an outcome] | [exact Signal skill, e.g., /listen-support] | [discovery statement — distinct from Column A] | YES / NO |

No gaps: "No gaps — signal coverage was sufficient for this commit decision."

Improvement recommendation — three required slots. Replace each `[slot:X]` token with specific content. The final output must not contain any `[slot:` strings — their presence indicates an unfilled slot.

  > **Recommendation**: Addresses [slot:gap-or-echo — name the specific gap type or Echo pattern addressed] by [slot:practice-change — name the specific practice change, not generic] so that [slot:measurable-outcome — state what would be observably different if this practice change succeeded].

PHASE 7 SEAL — format contract:
  [ ] Gap rows: every W or P namespace from Phase 3 has a row OR explicit "no gaps" statement — no silent omissions
  [ ] Material EMPTY namespaces: every one with commit-relevant absence has a row
  [ ] Column A format: {prior belief} framed as "We assumed X was true" or equivalent — NOT an outcome statement, NOT blank, NOT "unknown"
  [ ] Column B format: {discovery statement} — different content from Column A; answers "what was missed", not "why the gap existed"
  [ ] Column A != Column B: both columns must state different things per row — same statement in both = incomplete
  [ ] Skill format: {/exact-skill-name} — an exact Signal namespace skill name, not a namespace name, not "gather more data"
  [ ] Changed commit: exactly {YES} or {NO} per row — no other values
  [ ] Recommendation slot check: output does not contain the literal strings "[slot:gap-or-echo]", "[slot:practice-change]", or "[slot:measurable-outcome]" — all three tokens replaced with specific content
  {{#if amend}}[ ] AMEND scope marker: "[AMEND: {{amend}} only — ...]" present above gap table{{/if}}
All items confirmed against format? PHASE 7 COMPLETE.

---

PHASE 8 — CALIBRATION TREND

COPY the accuracy score from the Phase 6 verdict sentence into the "This score" cell. Do not recompute or derive this number. The Phase 6 verdict sentence is the authoritative source for the score — transfer the number verbatim. Label the cell to record the copy operation and name the source: "COPY-VERIFIED [Phase 6 verdict]".

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [reference or "none"] | [prior score or "—"] | [copied from Phase 6 verdict — COPY-VERIFIED [Phase 6 verdict]] | [delta or "—"] | ↑ improving / ↓ degrading / = stable |

No prior retro: "First retro for this topic — this score establishes the calibration baseline."

PHASE 8 SEAL — format contract:
  [ ] Prior retro: {topic-name} / {YYYY-MM-DD} OR the exact string "none" — not blank, not "N/A"
  [ ] This score: {number}/100 — value must be present and non-blank
  [ ] COPY-VERIFIED: confirmed — the "This score" value was traced to the Phase 6 verdict sentence directly; it was not recomputed from Phase 4 TOTAL
  [ ] COPY-SOURCE: "Phase 6 verdict sentence" — the authoritative source is Phase 6, not Phase 4; confirm by reading Phase 6 directly
  [ ] Delta: {+N or -N or 0} OR "—" when no prior retro
  [ ] Trend: one of exactly: ↑ improving | ↓ degrading | = stable OR the "first retro" statement
All items confirmed against format? PHASE 8 COMPLETE.

---

PHASE 9 — ECHO → SIGNAL DESIGN
Translate the Phase 1 Echo and Pattern into one concrete practice change.

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [exact Echo cell content — not paraphrased] | [exact Pattern name from Phase 1 — same taxonomy label, not a synonym] | [one specific practice change — not "gather more signals"] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL — format contract:
  [ ] Echo cell: {Phase 1 Echo copied verbatim} — must match Phase 1 Echo cell character-for-character; paraphrase = incomplete
  [ ] Pattern cell: {Phase 1 taxonomy label copied verbatim} — must match Phase 1 Pattern name exactly; synonym = incomplete
  [ ] Proposed change: {one specific actionable change} — not "gather more signals", not generic
  [ ] Change type: exactly one of: new skill | rubric amendment | threshold adjustment
All items confirmed against format? RETRO COMPLETE.

---

Execute phases in order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9.

Design guarantees:
- Phase 1: Echo locked before signal comparison. Pattern and Why-unexpected required.
- Phase 2: Fixed 9-row table; COVERED/EMPTY only. AMEND adds OOS secondary table.
- Phase 4: Weighted score AND N/M=X% count ratio — both required.
- Phase 6: Verdict sentence draws both formats from Phase 4. No recalculation.
- Phase 7: Two structurally isolated gap columns (Column A = belief, Column B = outcome); must not share content. Three-slot `[slot:X]` recommendation; SEAL confirms no `[slot:` strings survive.
- Phase 8: Score COPIED from Phase 6 verdict sentence. Explicit "do not recompute." SEAL carries three named fields: `This score` (value), `COPY-VERIFIED` (operation confirmed), `COPY-SOURCE` (origin named as "Phase 6 verdict sentence").
- All 9 seals use explicit format-contract strings per field (not just field names).
- AMEND: every table has a scope marker; Phase 2 has OOS secondary table.

Each phase seal is a format contract, not a checklist. Verify each item against its stated format before proceeding.
```

---

## V-02 — Guarantees Table: C-31 via Dedicated `## DESIGN GUARANTEES` Section

**Axis:** C-31 mechanism. The trailing "Design guarantees:" bullet list is replaced with a formal `## DESIGN GUARANTEES` section using a two-column table: `Mechanism` and `Structural guarantee — what is enforced and how`. Each row names a mechanism by type and states the specific structural decision that enforces it, including the named elements (slot tokens, SEAL fields, column labels, copy instructions). The section appears at the end of the prompt under its own header, making it visually and structurally distinct from the phase specifications.

**Hypothesis:** R11-V-05's bullet list satisfies C-31 content requirements (specific mechanisms named) but may score PARTIAL because it reads as a summary note appended to phase content, not as a "dedicated section." A header-titled table creates the structural separation that makes the section independently locatable. The two-column form (Mechanism / Guarantee) also supports C-31's requirement that "a reviewer can audit the key guarantees without reconstructing them from phase text" — each guarantee is accessible by mechanism name without reading phase specifications. Phase 8 SEAL unchanged from R11-V-05.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Each phase ends with a PHASE SEAL — a format-contract checklist. Every seal item specifies both the required field and its required value form. Do not proceed past a phase until every seal item is confirmed against the stated format.

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

Immediately after the table:
  > **Pattern**: [name from taxonomy or "other: [your name]"] — [description of the recurring failure mode — not a restatement of the Echo, but the class of failure it belongs to]
  > **Why unexpected**: [which prior belief, model, or assumption this finding contradicted — what the author expected, and why reality diverged]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

LOCK: Echo table, Pattern, and Why-unexpected are final. Phases 2–9 may not change them.

PHASE 1 SEAL — format contract:
  [ ] Echo: {one sentence describing post-ship finding} OR the exact string "No Echo — all post-ship outcomes were within signal bounds" — not blank, not a restatement of a wrong prediction
  [ ] Nearest signal: {artifact-filename.md} OR the exact string "none" — not blank, not "N/A", not a namespace name
  [ ] Commit relevance: one of exactly: HIGH | MEDIUM | LOW | N/A — "N/A" only valid when paired with "No Echo"
  [ ] Pattern: "> **Pattern**: {taxonomy-label or "other: name"} — {description of failure class, not the Echo instance}" — not blank; description not a restatement of the Echo sentence
  [ ] Why unexpected: "> **Why unexpected**: {prior belief or model contradicted} — must identify what was expected, not just assert unexpectedness"
  {{#if amend}}[ ] AMEND scope marker: "[AMEND: {{amend}} only — ...]" present immediately above table{{/if}}
All items confirmed against format? PHASE 1 COMPLETE.

---

PHASE 2 — SIGNAL INVENTORY
Produce a fixed 9-row namespace coverage table. Every namespace gets exactly one row.

{{#if amend}}[AMEND: {{amend}} only — out-of-scope artifacts go to the OOS table below, not the main table]{{/if}}

| Namespace | Status          | Artifact count | Primary artifact (or "—") | Prediction theme (or "—") |
|-----------|-----------------|----------------|--------------------------|--------------------------|
| scout     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| draft     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| review    | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| flow      | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| trace     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| prove     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| listen    | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| program   | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| topic     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| TOTAL     |                 | N              |                          |                          |

If a namespace has more than one artifact, list additional files in continuation rows below that row.

{{#if amend}}Out-of-scope artifacts (excluded per AMEND constraint):
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside {{amend}} scope] |
If none excluded: "No artifacts excluded — all in scope."
{{/if}}

PHASE 2 SEAL — format contract:
  [ ] All 9 namespace rows present in exact order: scout, draft, review, flow, trace, prove, listen, program, topic — missing row = incomplete
  [ ] Status: {COVERED} or {EMPTY} per row — no other value, no blank
  [ ] Artifact count: {integer} per row — blank invalid; 0 valid for EMPTY
  [ ] Primary artifact: {filename.md} or the string "—" — not blank
  [ ] TOTAL row: present with format {integer} in Artifact count cell
  {{#if amend}}[ ] OOS table: present immediately after main table — even if "No artifacts excluded — all in scope."{{/if}}
All items confirmed against format? PHASE 2 COMPLETE.

---

PHASE 3 — PREDICTED VS ACTUAL
For each namespace with Status = COVERED in Phase 2:

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted (signals' collective claim post-ship) | Actual (what was observed post-ship) | Match: C / P / W / ND |
|-----------|------------------------------------------------|--------------------------------------|----------------------|
| [name] | [required — non-blank statement] | [required — non-blank statement] | [C / P / W / ND] |

C = Correct, P = Partial (direction right, magnitude/timing off), W = Wrong, ND = No post-ship data yet.

PHASE 3 SEAL — format contract:
  [ ] Row count: one row per COVERED namespace from Phase 2 — no omissions, no extras
  [ ] Predicted: {one phrase or sentence describing what signals claimed} — not blank, not "N/A", not "unknown"
  [ ] Actual: {one phrase or sentence describing what was observed} — not blank, not "N/A", not "unknown"
  [ ] Match: one of exactly: C | P | W | ND — no other values, no blank
  {{#if amend}}[ ] Scope marker: "[AMEND: {{amend}} only]" present above table{{/if}}
All items confirmed against format? PHASE 3 COMPLETE.

---

PHASE 4 — NAMESPACE ACCURACY
{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Weighted score: (C×100 + P×50) ÷ (C+P+W) |
|-----------|---|---|---|-----|------------------------------------------|
| [name]    |   |   |   |     |                                          |
| TOTAL     |   |   |   |     |                                          |

ND excluded from denominator. Score blank if denominator = 0 (note as "0 scored signals").

After the scoring table, state the count-based accuracy ratio:
  Correct signals: {C count} / {C+P+W count} = X%
  (Count-based, not weighted. Both numbers required.)

PHASE 4 SEAL — format contract:
  [ ] Row count: one row per Phase 3 namespace — no omissions
  [ ] C, P, W, ND columns: {integer} per cell — blank invalid; 0 valid
  [ ] Weighted score: {number}/100 per row OR blank with note "0 scored signals" when denominator = 0
  [ ] TOTAL row: present with weighted formula applied — format: {number}/100
  [ ] Count-based ratio: stated immediately below scoring table in exact format "{N}/{M} = {X}%" — both N and M required
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed against format? PHASE 4 COMPLETE.

---

PHASE 5 — CONFLICT AUDIT
Mandatory. Always produces exactly one of two outputs.

Review the locked Phase 1 Echo. Does any Phase 3 verdict or Phase 4 score suggest the Echo should name a different finding?

If YES:
  CONFLICT DETECTED
  Source: {Phase 3 row namespace / Phase 4 score — specific finding that creates the tension}
  Analysis: {what the finding suggests the Echo should become}
  Resolution: Phase 1 Echo is preserved unchanged. This block is the conflict artifact.

If NO:
  CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo.

PHASE 5 SEAL — format contract:
  [ ] Output: exactly one of — CONFLICT DETECTED block (with Source, Analysis, Resolution all present and non-blank) OR the exact string "CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo."
  [ ] Phase 1 modification: none — Echo table, Pattern, and Why-unexpected must be unchanged
All items confirmed against format? PHASE 5 COMPLETE.

---

PHASE 6 — ACCURACY VERDICT
Draw the weighted score from Phase 4 TOTAL row. Draw the count ratio from Phase 4 count-based statement. Do not recalculate either number.

State the verdict:
  "Signal accuracy for [topic]: [TOTAL weighted score]/100 — [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]. Count accuracy: [N/M = X%]."

PHASE 6 SEAL — format contract:
  [ ] Verdict sentence: present in exact format "Signal accuracy for {topic}: {score}/100 — {STRONG|ADEQUATE|WEAK}. Count accuracy: {N}/{M} = {X}%."
  [ ] Weighted score: {score} drawn from Phase 4 TOTAL row — same number, not recalculated (verify by reading Phase 4 TOTAL)
  [ ] Count ratio: {N}/{M} = {X}% drawn from Phase 4 count-based statement — same values, not recalculated
  [ ] Tier label: STRONG if score >= 75 | ADEQUATE if 50 <= score < 75 | WEAK if score < 50 — must match stated score
All items confirmed against format? PHASE 6 COMPLETE.

---

PHASE 7 — GAP ANALYSIS
For each namespace scoring W or P in Phase 3, and each EMPTY namespace (Phase 2) where absence is material to the commit decision:

{{#if amend}}[AMEND: {{amend}} only — gaps outside this constraint excluded]{{/if}}

The gap table carries two structurally isolated columns that must contain different statements:
  - Column A — "Assumption held without evidence": the inertia belief that made this gap invisible before commit. WHY the gap existed. Framed as a prior belief ("We assumed X"), not as an outcome.
  - Column B — "Would have surfaced": the discovery missed. WHAT was missed. Different statement from Column A.
  Validation: if Column A and Column B contain the same statement, one column is wrong. Do not proceed with a merged row.

| Gap (signal type absent) | Namespace | Assumption held without evidence [A] | Skill to run | Would have surfaced [B] | Changed commit? YES / NO |
|--------------------------|-----------|--------------------------------------|-------------|-------------------------|--------------------------|
| [type] | [ns] | [prior belief — "We assumed X" — NOT an outcome] | [exact Signal skill, e.g., /listen-support] | [discovery statement — distinct from Column A] | YES / NO |

No gaps: "No gaps — signal coverage was sufficient for this commit decision."

Improvement recommendation — three required slots. Replace each `[slot:X]` token with specific content. The final output must not contain any `[slot:` strings — their presence indicates an unfilled slot.

  > **Recommendation**: Addresses [slot:gap-or-echo — name the specific gap type or Echo pattern addressed] by [slot:practice-change — name the specific practice change, not generic] so that [slot:measurable-outcome — state what would be observably different if this practice change succeeded].

PHASE 7 SEAL — format contract:
  [ ] Gap rows: every W or P namespace from Phase 3 has a row OR explicit "no gaps" statement — no silent omissions
  [ ] Material EMPTY namespaces: every one with commit-relevant absence has a row
  [ ] Column A format: {prior belief} framed as "We assumed X was true" or equivalent — NOT an outcome statement, NOT blank, NOT "unknown"
  [ ] Column B format: {discovery statement} — different content from Column A; answers "what was missed", not "why the gap existed"
  [ ] Column A != Column B: both columns must state different things per row — same statement in both = incomplete
  [ ] Skill format: {/exact-skill-name} — an exact Signal namespace skill name, not a namespace name, not "gather more data"
  [ ] Changed commit: exactly {YES} or {NO} per row — no other values
  [ ] Recommendation slot check: output does not contain the literal strings "[slot:gap-or-echo]", "[slot:practice-change]", or "[slot:measurable-outcome]" — all three tokens replaced with specific content
  {{#if amend}}[ ] AMEND scope marker: "[AMEND: {{amend}} only — ...]" present above gap table{{/if}}
All items confirmed against format? PHASE 7 COMPLETE.

---

PHASE 8 — CALIBRATION TREND

COPY the accuracy score from the Phase 6 verdict sentence into the "This score" cell. Do not recompute or derive this number. The Phase 6 verdict sentence is the authoritative source for the score in this phase — transfer the number verbatim.

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [reference or "none"] | [prior score or "—"] | [copied from Phase 6 verdict sentence — do not recompute] | [delta or "—"] | ↑ improving / ↓ degrading / = stable |

No prior retro: "First retro for this topic — this score establishes the calibration baseline."

PHASE 8 SEAL — format contract:
  [ ] Prior retro: {topic-name} / {YYYY-MM-DD} OR the exact string "none" — not blank, not "N/A"
  [ ] This score: {number}/100 — COPY-VERIFIED: confirm this number matches the score in the Phase 6 verdict sentence by reading Phase 6 directly (do not recompute from Phase 4 TOTAL; the copy source is Phase 6 verdict, not Phase 4)
  [ ] Delta: {+N or -N or 0} OR "—" when no prior retro
  [ ] Trend: one of exactly: ↑ improving | ↓ degrading | = stable OR the "first retro" statement
All items confirmed against format? PHASE 8 COMPLETE.

---

PHASE 9 — ECHO → SIGNAL DESIGN
Translate the Phase 1 Echo and Pattern into one concrete practice change.

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [exact Echo cell content — not paraphrased] | [exact Pattern name from Phase 1 — same taxonomy label, not a synonym] | [one specific practice change — not "gather more signals"] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL — format contract:
  [ ] Echo cell: {Phase 1 Echo copied verbatim} — must match Phase 1 Echo cell character-for-character; paraphrase = incomplete
  [ ] Pattern cell: {Phase 1 taxonomy label copied verbatim} — must match Phase 1 Pattern name exactly; synonym = incomplete
  [ ] Proposed change: {one specific actionable change} — not "gather more signals", not generic
  [ ] Change type: exactly one of: new skill | rubric amendment | threshold adjustment
All items confirmed against format? RETRO COMPLETE.

---

Execute phases in order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9.

---

## DESIGN GUARANTEES

Each row names a mechanism and states the structural decision that enforces it. A reviewer can confirm any guarantee by reading the named phase and field — no reconstruction from phase text required.

| Mechanism | Structural guarantee — what is enforced and how |
|-----------|------------------------------------------------|
| Echo lock | Phase 1 runs before signal comparison; Echo, Pattern, and Why-unexpected are finalized in Phase 1 SEAL and locked against modification by Phases 2–9 |
| Namespace table | Fixed 9-row table with rows in canonical order (scout through topic); Status accepts only COVERED or EMPTY; any other value = incomplete |
| Accuracy ratio | Phase 4 requires both a weighted formula score ({N}/100) AND a count-based ratio ({N}/{M} = {X}%) — the ratio is required in the Phase 4 SEAL as a named format-string field |
| Verdict sentence | Phase 6 draws both score formats from Phase 4 (no recalculation); verdict format is a named format-contract string; tier label (STRONG/ADEQUATE/WEAK) is checked against stated score |
| Gap columns | Phase 7 gap table has two structurally isolated columns: Column A = prior belief ("We assumed X"), Column B = discovery missed; columns must contain different statements; merged rows = incomplete |
| Recommendation slots | Three `[slot:X]` tokens (`[slot:gap-or-echo]`, `[slot:practice-change]`, `[slot:measurable-outcome]`) in the Phase 7 recommendation template; Phase 7 SEAL confirms no `[slot:` strings survive to output |
| Copy guard | Phase 8 body: "COPY from Phase 6 verdict sentence. Do not recompute." Phase 8 SEAL: "COPY-VERIFIED: confirm this number matches Phase 6 verdict sentence by reading Phase 6 directly (copy source is Phase 6, not Phase 4)" |
| Seal format contracts | All 9 phase seals carry explicit format-string specifications per field — not just field names; each seal item states both what must be present and what it must look like |
| AMEND scope markers | When AMEND flag is set: every phase table carries a "[AMEND: {scope} only]" marker; Phase 2 includes a dedicated OOS secondary table for excluded artifacts |
```

---

## V-03 — Phrasing Register: Imperative Prohibition Mode for C-30 and C-31

**Axis:** Phrasing register (single). C-30 and C-31 mechanisms are expressed in hard imperative prohibition style. Phase 8 introduces a `SCORE TRANSFER COMMAND` block with four numbered imperative steps, the third of which names COPY-VERIFIED and Phase 6 verdict explicitly as the required cell label and source. The design-guarantees section uses a bold `EXECUTION CONTRACT` header with headline-imperative lines per mechanism. No additional structural tokens or table restructuring beyond R11-V-05.

**Hypothesis:** The structural token approach (COPY-VERIFIED as named SEAL fields) targets mechanical compliance — the LLM or scorer checks field names. The imperative prohibition approach targets behavioral compliance — the executing agent reads the prohibition as a behavioral constraint and avoids the forbidden action. V-03 tests whether command-register prose achieves C-30 and C-31 without additional checklist complexity. The risk: C-30 requires "named fields" structurally; strong prose may be evaluated as PARTIAL if a rubric scorer requires field-level separation. C-31 requires a "dedicated section"; a bold header above an imperative list may satisfy this without a full table.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Each phase ends with a PHASE SEAL — a format-contract checklist. Every seal item specifies both the required field and its required value form. Do not proceed past a phase until every seal item is confirmed against the stated format.

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

Immediately after the table:
  > **Pattern**: [name from taxonomy or "other: [your name]"] — [description of the recurring failure mode — not a restatement of the Echo, but the class of failure it belongs to]
  > **Why unexpected**: [which prior belief, model, or assumption this finding contradicted — what the author expected, and why reality diverged]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

LOCK: Echo table, Pattern, and Why-unexpected are final. Phases 2–9 may not change them.

PHASE 1 SEAL — format contract:
  [ ] Echo: {one sentence describing post-ship finding} OR the exact string "No Echo — all post-ship outcomes were within signal bounds" — not blank, not a restatement of a wrong prediction
  [ ] Nearest signal: {artifact-filename.md} OR the exact string "none" — not blank, not "N/A", not a namespace name
  [ ] Commit relevance: one of exactly: HIGH | MEDIUM | LOW | N/A — "N/A" only valid when paired with "No Echo"
  [ ] Pattern: "> **Pattern**: {taxonomy-label or "other: name"} — {description of failure class, not the Echo instance}" — not blank; description not a restatement of the Echo sentence
  [ ] Why unexpected: "> **Why unexpected**: {prior belief or model contradicted} — must identify what was expected, not just assert unexpectedness"
  {{#if amend}}[ ] AMEND scope marker: "[AMEND: {{amend}} only — ...]" present immediately above table{{/if}}
All items confirmed against format? PHASE 1 COMPLETE.

---

PHASE 2 — SIGNAL INVENTORY
Produce a fixed 9-row namespace coverage table. Every namespace gets exactly one row.

{{#if amend}}[AMEND: {{amend}} only — out-of-scope artifacts go to the OOS table below, not the main table]{{/if}}

| Namespace | Status          | Artifact count | Primary artifact (or "—") | Prediction theme (or "—") |
|-----------|-----------------|----------------|--------------------------|--------------------------|
| scout     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| draft     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| review    | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| flow      | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| trace     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| prove     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| listen    | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| program   | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| topic     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| TOTAL     |                 | N              |                          |                          |

If a namespace has more than one artifact, list additional files in continuation rows below that row.

{{#if amend}}Out-of-scope artifacts (excluded per AMEND constraint):
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside {{amend}} scope] |
If none excluded: "No artifacts excluded — all in scope."
{{/if}}

PHASE 2 SEAL — format contract:
  [ ] All 9 namespace rows present in exact order: scout, draft, review, flow, trace, prove, listen, program, topic — missing row = incomplete
  [ ] Status: {COVERED} or {EMPTY} per row — no other value, no blank
  [ ] Artifact count: {integer} per row — blank invalid; 0 valid for EMPTY
  [ ] Primary artifact: {filename.md} or the string "—" — not blank
  [ ] TOTAL row: present with format {integer} in Artifact count cell
  {{#if amend}}[ ] OOS table: present immediately after main table — even if "No artifacts excluded — all in scope."{{/if}}
All items confirmed against format? PHASE 2 COMPLETE.

---

PHASE 3 — PREDICTED VS ACTUAL
For each namespace with Status = COVERED in Phase 2:

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted (signals' collective claim post-ship) | Actual (what was observed post-ship) | Match: C / P / W / ND |
|-----------|------------------------------------------------|--------------------------------------|----------------------|
| [name] | [required — non-blank statement] | [required — non-blank statement] | [C / P / W / ND] |

C = Correct, P = Partial (direction right, magnitude/timing off), W = Wrong, ND = No post-ship data yet.

PHASE 3 SEAL — format contract:
  [ ] Row count: one row per COVERED namespace from Phase 2 — no omissions, no extras
  [ ] Predicted: {one phrase or sentence describing what signals claimed} — not blank, not "N/A", not "unknown"
  [ ] Actual: {one phrase or sentence describing what was observed} — not blank, not "N/A", not "unknown"
  [ ] Match: one of exactly: C | P | W | ND — no other values, no blank
  {{#if amend}}[ ] Scope marker: "[AMEND: {{amend}} only]" present above table{{/if}}
All items confirmed against format? PHASE 3 COMPLETE.

---

PHASE 4 — NAMESPACE ACCURACY
{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Weighted score: (C×100 + P×50) ÷ (C+P+W) |
|-----------|---|---|---|-----|------------------------------------------|
| [name]    |   |   |   |     |                                          |
| TOTAL     |   |   |   |     |                                          |

ND excluded from denominator. Score blank if denominator = 0 (note as "0 scored signals").

After the scoring table, state the count-based accuracy ratio:
  Correct signals: {C count} / {C+P+W count} = X%
  (Count-based, not weighted. Both numbers required.)

PHASE 4 SEAL — format contract:
  [ ] Row count: one row per Phase 3 namespace — no omissions
  [ ] C, P, W, ND columns: {integer} per cell — blank invalid; 0 valid
  [ ] Weighted score: {number}/100 per row OR blank with note "0 scored signals" when denominator = 0
  [ ] TOTAL row: present with weighted formula applied — format: {number}/100
  [ ] Count-based ratio: stated immediately below scoring table in exact format "{N}/{M} = {X}%" — both N and M required
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed against format? PHASE 4 COMPLETE.

---

PHASE 5 — CONFLICT AUDIT
Mandatory. Always produces exactly one of two outputs.

Review the locked Phase 1 Echo. Does any Phase 3 verdict or Phase 4 score suggest the Echo should name a different finding?

If YES:
  CONFLICT DETECTED
  Source: {Phase 3 row namespace / Phase 4 score — specific finding that creates the tension}
  Analysis: {what the finding suggests the Echo should become}
  Resolution: Phase 1 Echo is preserved unchanged. This block is the conflict artifact.

If NO:
  CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo.

PHASE 5 SEAL — format contract:
  [ ] Output: exactly one of — CONFLICT DETECTED block (with Source, Analysis, Resolution all present and non-blank) OR the exact string "CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo."
  [ ] Phase 1 modification: none — Echo table, Pattern, and Why-unexpected must be unchanged
All items confirmed against format? PHASE 5 COMPLETE.

---

PHASE 6 — ACCURACY VERDICT
Draw the weighted score from Phase 4 TOTAL row. Draw the count ratio from Phase 4 count-based statement. Do not recalculate either number.

State the verdict:
  "Signal accuracy for [topic]: [TOTAL weighted score]/100 — [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]. Count accuracy: [N/M = X%]."

PHASE 6 SEAL — format contract:
  [ ] Verdict sentence: present in exact format "Signal accuracy for {topic}: {score}/100 — {STRONG|ADEQUATE|WEAK}. Count accuracy: {N}/{M} = {X}%."
  [ ] Weighted score: {score} drawn from Phase 4 TOTAL row — same number, not recalculated (verify by reading Phase 4 TOTAL)
  [ ] Count ratio: {N}/{M} = {X}% drawn from Phase 4 count-based statement — same values, not recalculated
  [ ] Tier label: STRONG if score >= 75 | ADEQUATE if 50 <= score < 75 | WEAK if score < 50 — must match stated score
All items confirmed against format? PHASE 6 COMPLETE.

---

PHASE 7 — GAP ANALYSIS
For each namespace scoring W or P in Phase 3, and each EMPTY namespace (Phase 2) where absence is material to the commit decision:

{{#if amend}}[AMEND: {{amend}} only — gaps outside this constraint excluded]{{/if}}

The gap table carries two structurally isolated columns that must contain different statements:
  - Column A — "Assumption held without evidence": the inertia belief that made this gap invisible before commit. WHY the gap existed. Framed as a prior belief ("We assumed X"), not as an outcome.
  - Column B — "Would have surfaced": the discovery missed. WHAT was missed. Different statement from Column A.
  Validation: if Column A and Column B contain the same statement, one column is wrong. Do not proceed with a merged row.

| Gap (signal type absent) | Namespace | Assumption held without evidence [A] | Skill to run | Would have surfaced [B] | Changed commit? YES / NO |
|--------------------------|-----------|--------------------------------------|-------------|-------------------------|--------------------------|
| [type] | [ns] | [prior belief — "We assumed X" — NOT an outcome] | [exact Signal skill, e.g., /listen-support] | [discovery statement — distinct from Column A] | YES / NO |

No gaps: "No gaps — signal coverage was sufficient for this commit decision."

Improvement recommendation — three required slots. Replace each `[slot:X]` token with specific content. The final output must not contain any `[slot:` strings — their presence indicates an unfilled slot.

  > **Recommendation**: Addresses [slot:gap-or-echo — name the specific gap type or Echo pattern addressed] by [slot:practice-change — name the specific practice change, not generic] so that [slot:measurable-outcome — state what would be observably different if this practice change succeeded].

PHASE 7 SEAL — format contract:
  [ ] Gap rows: every W or P namespace from Phase 3 has a row OR explicit "no gaps" statement — no silent omissions
  [ ] Material EMPTY namespaces: every one with commit-relevant absence has a row
  [ ] Column A format: {prior belief} framed as "We assumed X was true" or equivalent — NOT an outcome statement, NOT blank, NOT "unknown"
  [ ] Column B format: {discovery statement} — different content from Column A; answers "what was missed", not "why the gap existed"
  [ ] Column A != Column B: both columns must state different things per row — same statement in both = incomplete
  [ ] Skill format: {/exact-skill-name} — an exact Signal namespace skill name, not a namespace name, not "gather more data"
  [ ] Changed commit: exactly {YES} or {NO} per row — no other values
  [ ] Recommendation slot check: output does not contain the literal strings "[slot:gap-or-echo]", "[slot:practice-change]", or "[slot:measurable-outcome]" — all three tokens replaced with specific content
  {{#if amend}}[ ] AMEND scope marker: "[AMEND: {{amend}} only — ...]" present above gap table{{/if}}
All items confirmed against format? PHASE 7 COMPLETE.

---

PHASE 8 — CALIBRATION TREND

SCORE TRANSFER COMMAND:
  1. Open Phase 6. Read the verdict sentence.
  2. Locate the score number (the value before "/100").
  3. Copy it verbatim into the "This score" cell. Label the cell: COPY-VERIFIED [source: Phase 6 verdict].
  4. Do not look at Phase 4. Do not recompute. Any number that was derived instead of copied is a transfer failure — reopen Phase 6 and copy again.

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [reference or "none"] | [prior score or "—"] | [COPY-VERIFIED — copied from Phase 6 verdict, labeled with source] | [delta or "—"] | ↑ improving / ↓ degrading / = stable |

No prior retro: "First retro for this topic — this score establishes the calibration baseline."

PHASE 8 SEAL — format contract:
  [ ] Prior retro: {topic-name} / {YYYY-MM-DD} OR the exact string "none" — not blank, not "N/A"
  [ ] This score: {number}/100 — labeled COPY-VERIFIED [source: Phase 6 verdict]; source named as Phase 6, not Phase 4
  [ ] Delta: {+N or -N or 0} OR "—" when no prior retro
  [ ] Trend: one of exactly: ↑ improving | ↓ degrading | = stable OR the "first retro" statement
All items confirmed against format? PHASE 8 COMPLETE.

---

PHASE 9 — ECHO → SIGNAL DESIGN
Translate the Phase 1 Echo and Pattern into one concrete practice change.

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [exact Echo cell content — not paraphrased] | [exact Pattern name from Phase 1 — same taxonomy label, not a synonym] | [one specific practice change — not "gather more signals"] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL — format contract:
  [ ] Echo cell: {Phase 1 Echo copied verbatim} — must match Phase 1 Echo cell character-for-character; paraphrase = incomplete
  [ ] Pattern cell: {Phase 1 taxonomy label copied verbatim} — must match Phase 1 Pattern name exactly; synonym = incomplete
  [ ] Proposed change: {one specific actionable change} — not "gather more signals", not generic
  [ ] Change type: exactly one of: new skill | rubric amendment | threshold adjustment
All items confirmed against format? RETRO COMPLETE.

---

Execute phases in order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9.

**EXECUTION CONTRACT — structural guarantees that must hold across all phases:**

- **Echo lock**: Do not modify the Phase 1 Echo, Pattern, or Why-unexpected after Phase 1 SEAL passes. Any phase that changes these fields violates this contract.
- **Namespace table**: Every run produces exactly 9 rows in the canonical order. COVERED and EMPTY are the only valid Status values. A missing row is an incomplete phase — do not proceed.
- **Accuracy ratio**: Do not report a score without the count-based ratio. Both the weighted formula score and the N/M = X% ratio are required in Phase 4. A score without a ratio is an incomplete phase.
- **Verdict copy**: Do not recalculate in Phase 6. Read Phase 4 TOTAL and Phase 4 count-based statement. Copy both numbers verbatim. Recomputation produces a different (potentially wrong) number.
- **Gap columns**: Do not merge Column A and Column B. They answer different questions. A merged row is an incomplete row — do not proceed past it.
- **Recommendation slots**: Do not leave `[slot:` strings in output. Each one represents an unfilled slot. The recommendation phase is not complete until all three tokens are replaced with specific content.
- **Score copy guard**: Do not derive the Phase 8 score. Read Phase 6. Copy it. Name the source. Label the cell COPY-VERIFIED [source: Phase 6 verdict]. Any derived number — even if it matches — is a transfer failure.
- **Seal format contracts**: Do not treat seals as checklists to be acknowledged. Verify each item against its stated format before marking it confirmed.
```

---

## V-04 — Combined: C-30 Three-Field SEAL + C-31 Guarantees Table

**Axes:** C-30 mechanism from V-01 (Phase 8 SEAL: three separate named fields — `This score`, `COPY-VERIFIED`, `COPY-SOURCE`) combined with C-31 mechanism from V-02 (`## DESIGN GUARANTEES` two-column table). No additional changes beyond V-01 + V-02. All other phases identical to R11-V-05.

**Hypothesis:** V-01 and V-02 are structurally independent — V-01 modifies Phase 8 SEAL only; V-02 modifies the post-execution design section only. No phase-level interference. Combined, they should achieve both C-30 and C-31 without regression on any prior-passing criterion. This is the minimum integration needed to target both new criteria simultaneously.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Each phase ends with a PHASE SEAL — a format-contract checklist. Every seal item specifies both the required field and its required value form. Do not proceed past a phase until every seal item is confirmed against the stated format.

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

Immediately after the table:
  > **Pattern**: [name from taxonomy or "other: [your name]"] — [description of the recurring failure mode — not a restatement of the Echo, but the class of failure it belongs to]
  > **Why unexpected**: [which prior belief, model, or assumption this finding contradicted — what the author expected, and why reality diverged]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

LOCK: Echo table, Pattern, and Why-unexpected are final. Phases 2–9 may not change them.

PHASE 1 SEAL — format contract:
  [ ] Echo: {one sentence describing post-ship finding} OR the exact string "No Echo — all post-ship outcomes were within signal bounds" — not blank, not a restatement of a wrong prediction
  [ ] Nearest signal: {artifact-filename.md} OR the exact string "none" — not blank, not "N/A", not a namespace name
  [ ] Commit relevance: one of exactly: HIGH | MEDIUM | LOW | N/A — "N/A" only valid when paired with "No Echo"
  [ ] Pattern: "> **Pattern**: {taxonomy-label or "other: name"} — {description of failure class, not the Echo instance}" — not blank; description not a restatement of the Echo sentence
  [ ] Why unexpected: "> **Why unexpected**: {prior belief or model contradicted} — must identify what was expected, not just assert unexpectedness"
  {{#if amend}}[ ] AMEND scope marker: "[AMEND: {{amend}} only — ...]" present immediately above table{{/if}}
All items confirmed against format? PHASE 1 COMPLETE.

---

PHASE 2 — SIGNAL INVENTORY
Produce a fixed 9-row namespace coverage table. Every namespace gets exactly one row.

{{#if amend}}[AMEND: {{amend}} only — out-of-scope artifacts go to the OOS table below, not the main table]{{/if}}

| Namespace | Status          | Artifact count | Primary artifact (or "—") | Prediction theme (or "—") |
|-----------|-----------------|----------------|--------------------------|--------------------------|
| scout     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| draft     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| review    | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| flow      | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| trace     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| prove     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| listen    | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| program   | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| topic     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| TOTAL     |                 | N              |                          |                          |

If a namespace has more than one artifact, list additional files in continuation rows below that row.

{{#if amend}}Out-of-scope artifacts (excluded per AMEND constraint):
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside {{amend}} scope] |
If none excluded: "No artifacts excluded — all in scope."
{{/if}}

PHASE 2 SEAL — format contract:
  [ ] All 9 namespace rows present in exact order: scout, draft, review, flow, trace, prove, listen, program, topic — missing row = incomplete
  [ ] Status: {COVERED} or {EMPTY} per row — no other value, no blank
  [ ] Artifact count: {integer} per row — blank invalid; 0 valid for EMPTY
  [ ] Primary artifact: {filename.md} or the string "—" — not blank
  [ ] TOTAL row: present with format {integer} in Artifact count cell
  {{#if amend}}[ ] OOS table: present immediately after main table — even if "No artifacts excluded — all in scope."{{/if}}
All items confirmed against format? PHASE 2 COMPLETE.

---

PHASE 3 — PREDICTED VS ACTUAL
For each namespace with Status = COVERED in Phase 2:

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted (signals' collective claim post-ship) | Actual (what was observed post-ship) | Match: C / P / W / ND |
|-----------|------------------------------------------------|--------------------------------------|----------------------|
| [name] | [required — non-blank statement] | [required — non-blank statement] | [C / P / W / ND] |

C = Correct, P = Partial (direction right, magnitude/timing off), W = Wrong, ND = No post-ship data yet.

PHASE 3 SEAL — format contract:
  [ ] Row count: one row per COVERED namespace from Phase 2 — no omissions, no extras
  [ ] Predicted: {one phrase or sentence describing what signals claimed} — not blank, not "N/A", not "unknown"
  [ ] Actual: {one phrase or sentence describing what was observed} — not blank, not "N/A", not "unknown"
  [ ] Match: one of exactly: C | P | W | ND — no other values, no blank
  {{#if amend}}[ ] Scope marker: "[AMEND: {{amend}} only]" present above table{{/if}}
All items confirmed against format? PHASE 3 COMPLETE.

---

PHASE 4 — NAMESPACE ACCURACY
{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Weighted score: (C×100 + P×50) ÷ (C+P+W) |
|-----------|---|---|---|-----|------------------------------------------|
| [name]    |   |   |   |     |                                          |
| TOTAL     |   |   |   |     |                                          |

ND excluded from denominator. Score blank if denominator = 0 (note as "0 scored signals").

After the scoring table, state the count-based accuracy ratio:
  Correct signals: {C count} / {C+P+W count} = X%
  (Count-based, not weighted. Both numbers required.)

PHASE 4 SEAL — format contract:
  [ ] Row count: one row per Phase 3 namespace — no omissions
  [ ] C, P, W, ND columns: {integer} per cell — blank invalid; 0 valid
  [ ] Weighted score: {number}/100 per row OR blank with note "0 scored signals" when denominator = 0
  [ ] TOTAL row: present with weighted formula applied — format: {number}/100
  [ ] Count-based ratio: stated immediately below scoring table in exact format "{N}/{M} = {X}%" — both N and M required
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed against format? PHASE 4 COMPLETE.

---

PHASE 5 — CONFLICT AUDIT
Mandatory. Always produces exactly one of two outputs.

Review the locked Phase 1 Echo. Does any Phase 3 verdict or Phase 4 score suggest the Echo should name a different finding?

If YES:
  CONFLICT DETECTED
  Source: {Phase 3 row namespace / Phase 4 score — specific finding that creates the tension}
  Analysis: {what the finding suggests the Echo should become}
  Resolution: Phase 1 Echo is preserved unchanged. This block is the conflict artifact.

If NO:
  CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo.

PHASE 5 SEAL — format contract:
  [ ] Output: exactly one of — CONFLICT DETECTED block (with Source, Analysis, Resolution all present and non-blank) OR the exact string "CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo."
  [ ] Phase 1 modification: none — Echo table, Pattern, and Why-unexpected must be unchanged
All items confirmed against format? PHASE 5 COMPLETE.

---

PHASE 6 — ACCURACY VERDICT
Draw the weighted score from Phase 4 TOTAL row. Draw the count ratio from Phase 4 count-based statement. Do not recalculate either number.

State the verdict:
  "Signal accuracy for [topic]: [TOTAL weighted score]/100 — [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]. Count accuracy: [N/M = X%]."

PHASE 6 SEAL — format contract:
  [ ] Verdict sentence: present in exact format "Signal accuracy for {topic}: {score}/100 — {STRONG|ADEQUATE|WEAK}. Count accuracy: {N}/{M} = {X}%."
  [ ] Weighted score: {score} drawn from Phase 4 TOTAL row — same number, not recalculated (verify by reading Phase 4 TOTAL)
  [ ] Count ratio: {N}/{M} = {X}% drawn from Phase 4 count-based statement — same values, not recalculated
  [ ] Tier label: STRONG if score >= 75 | ADEQUATE if 50 <= score < 75 | WEAK if score < 50 — must match stated score
All items confirmed against format? PHASE 6 COMPLETE.

---

PHASE 7 — GAP ANALYSIS
For each namespace scoring W or P in Phase 3, and each EMPTY namespace (Phase 2) where absence is material to the commit decision:

{{#if amend}}[AMEND: {{amend}} only — gaps outside this constraint excluded]{{/if}}

The gap table carries two structurally isolated columns that must contain different statements:
  - Column A — "Assumption held without evidence": the inertia belief that made this gap invisible before commit. WHY the gap existed. Framed as a prior belief ("We assumed X"), not as an outcome.
  - Column B — "Would have surfaced": the discovery missed. WHAT was missed. Different statement from Column A.
  Validation: if Column A and Column B contain the same statement, one column is wrong. Do not proceed with a merged row.

| Gap (signal type absent) | Namespace | Assumption held without evidence [A] | Skill to run | Would have surfaced [B] | Changed commit? YES / NO |
|--------------------------|-----------|--------------------------------------|-------------|-------------------------|--------------------------|
| [type] | [ns] | [prior belief — "We assumed X" — NOT an outcome] | [exact Signal skill, e.g., /listen-support] | [discovery statement — distinct from Column A] | YES / NO |

No gaps: "No gaps — signal coverage was sufficient for this commit decision."

Improvement recommendation — three required slots. Replace each `[slot:X]` token with specific content. The final output must not contain any `[slot:` strings — their presence indicates an unfilled slot.

  > **Recommendation**: Addresses [slot:gap-or-echo — name the specific gap type or Echo pattern addressed] by [slot:practice-change — name the specific practice change, not generic] so that [slot:measurable-outcome — state what would be observably different if this practice change succeeded].

PHASE 7 SEAL — format contract:
  [ ] Gap rows: every W or P namespace from Phase 3 has a row OR explicit "no gaps" statement — no silent omissions
  [ ] Material EMPTY namespaces: every one with commit-relevant absence has a row
  [ ] Column A format: {prior belief} framed as "We assumed X was true" or equivalent — NOT an outcome statement, NOT blank, NOT "unknown"
  [ ] Column B format: {discovery statement} — different content from Column A; answers "what was missed", not "why the gap existed"
  [ ] Column A != Column B: both columns must state different things per row — same statement in both = incomplete
  [ ] Skill format: {/exact-skill-name} — an exact Signal namespace skill name, not a namespace name, not "gather more data"
  [ ] Changed commit: exactly {YES} or {NO} per row — no other values
  [ ] Recommendation slot check: output does not contain the literal strings "[slot:gap-or-echo]", "[slot:practice-change]", or "[slot:measurable-outcome]" — all three tokens replaced with specific content
  {{#if amend}}[ ] AMEND scope marker: "[AMEND: {{amend}} only — ...]" present above gap table{{/if}}
All items confirmed against format? PHASE 7 COMPLETE.

---

PHASE 8 — CALIBRATION TREND

COPY the accuracy score from the Phase 6 verdict sentence into the "This score" cell. Do not recompute or derive this number. The Phase 6 verdict sentence is the authoritative source for the score — transfer the number verbatim. Label the cell to record the copy operation and name the source.

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [reference or "none"] | [prior score or "—"] | [copied from Phase 6 verdict — COPY-VERIFIED [Phase 6 verdict]] | [delta or "—"] | ↑ improving / ↓ degrading / = stable |

No prior retro: "First retro for this topic — this score establishes the calibration baseline."

PHASE 8 SEAL — format contract:
  [ ] Prior retro: {topic-name} / {YYYY-MM-DD} OR the exact string "none" — not blank, not "N/A"
  [ ] This score: {number}/100 — value must be present and non-blank
  [ ] COPY-VERIFIED: confirmed — the "This score" value was traced to the Phase 6 verdict sentence directly; it was not recomputed from Phase 4 TOTAL
  [ ] COPY-SOURCE: "Phase 6 verdict sentence" — the authoritative source is Phase 6, not Phase 4; confirm by reading Phase 6 directly before marking this item
  [ ] Delta: {+N or -N or 0} OR "—" when no prior retro
  [ ] Trend: one of exactly: ↑ improving | ↓ degrading | = stable OR the "first retro" statement
All items confirmed against format? PHASE 8 COMPLETE.

---

PHASE 9 — ECHO → SIGNAL DESIGN
Translate the Phase 1 Echo and Pattern into one concrete practice change.

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [exact Echo cell content — not paraphrased] | [exact Pattern name from Phase 1 — same taxonomy label, not a synonym] | [one specific practice change — not "gather more signals"] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL — format contract:
  [ ] Echo cell: {Phase 1 Echo copied verbatim} — must match Phase 1 Echo cell character-for-character; paraphrase = incomplete
  [ ] Pattern cell: {Phase 1 taxonomy label copied verbatim} — must match Phase 1 Pattern name exactly; synonym = incomplete
  [ ] Proposed change: {one specific actionable change} — not "gather more signals", not generic
  [ ] Change type: exactly one of: new skill | rubric amendment | threshold adjustment
All items confirmed against format? RETRO COMPLETE.

---

Execute phases in order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9.

---

## DESIGN GUARANTEES

Each row names a mechanism and states the structural decision that enforces it. A reviewer can audit any guarantee by reading the named phase and field — no reconstruction from phase text required.

| Mechanism | Structural guarantee — what is enforced and how |
|-----------|------------------------------------------------|
| Echo lock | Phase 1 runs before signal comparison; Echo, Pattern, and Why-unexpected are finalized in Phase 1 SEAL and locked against modification by Phases 2–9 |
| Namespace table | Fixed 9-row table in canonical order (scout through topic); Status accepts only COVERED or EMPTY; missing row = Phase 2 incomplete |
| Accuracy ratio | Phase 4 requires both weighted formula score ({N}/100) AND count-based ratio ({N}/{M} = {X}%); both are named format-string fields in the Phase 4 SEAL |
| Verdict sentence | Phase 6 draws both score formats from Phase 4 (no recalculation); format-contract string enforces exact sentence structure; tier label checked against stated score |
| Gap columns | Phase 7 gap table carries two structurally isolated columns: Column A = prior belief ("We assumed X"), Column B = discovery missed; columns must contain different statements; merged rows = incomplete |
| Recommendation slots | Three `[slot:X]` tokens in Phase 7 recommendation template; Phase 7 SEAL confirms no `[slot:` strings survive to output; all three tokens must be replaced with specific content |
| Copy guard — body | Phase 8 body: "COPY the accuracy score from Phase 6 verdict sentence. Do not recompute or derive this number." Cell carries COPY-VERIFIED [Phase 6 verdict] label |
| Copy guard — SEAL | Phase 8 SEAL carries three named fields: `This score` (value); `COPY-VERIFIED` (operation confirmed — traced to Phase 6 verdict, not recomputed from Phase 4); `COPY-SOURCE` (origin named as "Phase 6 verdict sentence") |
| Seal format contracts | All 9 phase seals carry explicit format-string specifications per field — not just field names; each seal item states both what must be present and what it must look like |
| AMEND scope markers | When AMEND flag set: every phase table carries "[AMEND: {scope} only]" marker; Phase 2 includes dedicated OOS secondary table for excluded artifacts |
```

---

## V-05 — Full Integration: C-30 + C-31 + Pre-Execution Contract + Phase 8 Cell Label

**Axes:** All of V-04 (C-30 three-field SEAL + C-31 guarantees table), plus two structural innovations:

1. **Pre-execution contract placement**: The `## DESIGN GUARANTEES` table is duplicated to appear *before Phase 1* as a `## PRE-EXECUTION CONTRACT`, promoting it from a trailing reference into an upfront commitment that the execution must honor. A trailing copy (condensed) is retained for post-execution audit reference. This tests whether positioning the guarantees section before the phase specifications strengthens C-31 by making the "dedicated section" structurally prior to (not embedded within) the execution flow.

2. **Phase 8 table-cell format string**: The Phase 8 calibration table template carries an explicit inline cell format string for "This score": `{number}/100 — COPY-VERIFIED [source: Phase 6 verdict]`. This adds a third structural location for the COPY-VERIFIED label and source: the table-cell format string (in addition to the body instruction and the SEAL fields). A scorer auditing C-30 finds the named label and source in three independently checkable locations.

**Hypothesis:** V-04 achieves C-30 and C-31 at minimum complexity. V-05 tests whether maximum structural redundancy — pre-execution positioning, cell-level inline labels, and three-field SEAL — produces ceiling-level scoring on C-30 and C-31 without volume-induced regression on earlier criteria. The pre-execution contract is the key structural innovation: it makes the guarantees a prospective contract (read before execution) rather than a retrospective summary (read after all phases are complete). A reviewer auditing a completed retro against C-31 sees the guarantees section before Phase 1 output, not after Phase 9.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Each phase ends with a PHASE SEAL — a format-contract checklist. Every seal item specifies both the required field and its required value form. Do not proceed past a phase until every seal item is confirmed against the stated format.

{{#if amend}}AMEND SCOPE: {{amend}} — all phases operate within this constraint only. Every table carries an explicit scope marker. Phase 2 includes an out-of-scope table.{{/if}}

---

## PRE-EXECUTION CONTRACT

The following structural guarantees must hold across all phases. Read before executing Phase 1. A completed retro is auditable against this contract without reading individual phase specifications.

| Mechanism | Structural guarantee — what is enforced and how |
|-----------|------------------------------------------------|
| Echo lock | Phase 1 runs before signal comparison; Echo, Pattern, and Why-unexpected locked in Phase 1 SEAL; Phases 2–9 must not modify them |
| Namespace table | Fixed 9-row table in canonical order; Status: COVERED or EMPTY only; missing row = Phase 2 incomplete |
| Accuracy ratio | Phase 4: both weighted formula score ({N}/100) and count-based ratio ({N}/{M} = {X}%) required; both are named SEAL fields |
| Verdict sentence | Phase 6: both score formats copied from Phase 4; exact sentence format enforced; tier label (STRONG/ADEQUATE/WEAK) checked against stated score |
| Gap columns | Phase 7: Column A = prior belief ("We assumed X"), Column B = discovery missed; structurally isolated; must contain different statements |
| Recommendation slots | Phase 7: three `[slot:X]` tokens; SEAL confirms no `[slot:` strings survive |
| Copy guard | Phase 8: score COPIED from Phase 6 verdict sentence verbatim; cell labeled COPY-VERIFIED [source: Phase 6 verdict]; SEAL carries three named fields: `This score`, `COPY-VERIFIED`, `COPY-SOURCE` |
| Seal format contracts | All 9 seals: explicit format-string per field; verify value form, not just presence |
| AMEND scope | When set: every table has scope marker; Phase 2 has OOS secondary table |

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

Immediately after the table:
  > **Pattern**: [name from taxonomy or "other: [your name]"] — [description of the recurring failure mode — not a restatement of the Echo, but the class of failure it belongs to]
  > **Why unexpected**: [which prior belief, model, or assumption this finding contradicted — what the author expected, and why reality diverged]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

LOCK: Echo table, Pattern, and Why-unexpected are final. Phases 2–9 may not change them.

PHASE 1 SEAL — format contract:
  [ ] Echo: {one sentence describing post-ship finding} OR the exact string "No Echo — all post-ship outcomes were within signal bounds" — not blank, not a restatement of a wrong prediction
  [ ] Nearest signal: {artifact-filename.md} OR the exact string "none" — not blank, not "N/A", not a namespace name
  [ ] Commit relevance: one of exactly: HIGH | MEDIUM | LOW | N/A — "N/A" only valid when paired with "No Echo"
  [ ] Pattern: "> **Pattern**: {taxonomy-label or "other: name"} — {description of failure class, not the Echo instance}" — not blank; description not a restatement of the Echo sentence
  [ ] Why unexpected: "> **Why unexpected**: {prior belief or model contradicted} — must identify what was expected, not just assert unexpectedness"
  {{#if amend}}[ ] AMEND scope marker: "[AMEND: {{amend}} only — ...]" present immediately above table{{/if}}
All items confirmed against format? PHASE 1 COMPLETE.

---

PHASE 2 — SIGNAL INVENTORY
Produce a fixed 9-row namespace coverage table. Every namespace gets exactly one row.

{{#if amend}}[AMEND: {{amend}} only — out-of-scope artifacts go to the OOS table below, not the main table]{{/if}}

| Namespace | Status          | Artifact count | Primary artifact (or "—") | Prediction theme (or "—") |
|-----------|-----------------|----------------|--------------------------|--------------------------|
| scout     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| draft     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| review    | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| flow      | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| trace     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| prove     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| listen    | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| program   | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| topic     | COVERED / EMPTY | N              | [filename or "—"]        | [one phrase or "—"]      |
| TOTAL     |                 | N              |                          |                          |

If a namespace has more than one artifact, list additional files in continuation rows below that row.

{{#if amend}}Out-of-scope artifacts (excluded per AMEND constraint):
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside {{amend}} scope] |
If none excluded: "No artifacts excluded — all in scope."
{{/if}}

PHASE 2 SEAL — format contract:
  [ ] All 9 namespace rows present in exact order: scout, draft, review, flow, trace, prove, listen, program, topic — missing row = incomplete
  [ ] Status: {COVERED} or {EMPTY} per row — no other value, no blank
  [ ] Artifact count: {integer} per row — blank invalid; 0 valid for EMPTY
  [ ] Primary artifact: {filename.md} or the string "—" — not blank
  [ ] TOTAL row: present with format {integer} in Artifact count cell
  {{#if amend}}[ ] OOS table: present immediately after main table — even if "No artifacts excluded — all in scope."{{/if}}
All items confirmed against format? PHASE 2 COMPLETE.

---

PHASE 3 — PREDICTED VS ACTUAL
For each namespace with Status = COVERED in Phase 2:

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted (signals' collective claim post-ship) | Actual (what was observed post-ship) | Match: C / P / W / ND |
|-----------|------------------------------------------------|--------------------------------------|----------------------|
| [name] | [required — non-blank statement] | [required — non-blank statement] | [C / P / W / ND] |

C = Correct, P = Partial (direction right, magnitude/timing off), W = Wrong, ND = No post-ship data yet.

PHASE 3 SEAL — format contract:
  [ ] Row count: one row per COVERED namespace from Phase 2 — no omissions, no extras
  [ ] Predicted: {one phrase or sentence describing what signals claimed} — not blank, not "N/A", not "unknown"
  [ ] Actual: {one phrase or sentence describing what was observed} — not blank, not "N/A", not "unknown"
  [ ] Match: one of exactly: C | P | W | ND — no other values, no blank
  {{#if amend}}[ ] Scope marker: "[AMEND: {{amend}} only]" present above table{{/if}}
All items confirmed against format? PHASE 3 COMPLETE.

---

PHASE 4 — NAMESPACE ACCURACY
{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Weighted score: (C×100 + P×50) ÷ (C+P+W) |
|-----------|---|---|---|-----|------------------------------------------|
| [name]    |   |   |   |     |                                          |
| TOTAL     |   |   |   |     |                                          |

ND excluded from denominator. Score blank if denominator = 0 (note as "0 scored signals").

After the scoring table, state the count-based accuracy ratio:
  Correct signals: {C count} / {C+P+W count} = X%
  (Count-based, not weighted. Both numbers required.)

PHASE 4 SEAL — format contract:
  [ ] Row count: one row per Phase 3 namespace — no omissions
  [ ] C, P, W, ND columns: {integer} per cell — blank invalid; 0 valid
  [ ] Weighted score: {number}/100 per row OR blank with note "0 scored signals" when denominator = 0
  [ ] TOTAL row: present with weighted formula applied — format: {number}/100
  [ ] Count-based ratio: stated immediately below scoring table in exact format "{N}/{M} = {X}%" — both N and M required
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed against format? PHASE 4 COMPLETE.

---

PHASE 5 — CONFLICT AUDIT
Mandatory. Always produces exactly one of two outputs.

Review the locked Phase 1 Echo. Does any Phase 3 verdict or Phase 4 score suggest the Echo should name a different finding?

If YES:
  CONFLICT DETECTED
  Source: {Phase 3 row namespace / Phase 4 score — specific finding that creates the tension}
  Analysis: {what the finding suggests the Echo should become}
  Resolution: Phase 1 Echo is preserved unchanged. This block is the conflict artifact.

If NO:
  CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo.

PHASE 5 SEAL — format contract:
  [ ] Output: exactly one of — CONFLICT DETECTED block (with Source, Analysis, Resolution all present and non-blank) OR the exact string "CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo."
  [ ] Phase 1 modification: none — Echo table, Pattern, and Why-unexpected must be unchanged
All items confirmed against format? PHASE 5 COMPLETE.

---

PHASE 6 — ACCURACY VERDICT
Draw the weighted score from Phase 4 TOTAL row. Draw the count ratio from Phase 4 count-based statement. Do not recalculate either number.

State the verdict:
  "Signal accuracy for [topic]: [TOTAL weighted score]/100 — [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]. Count accuracy: [N/M = X%]."

PHASE 6 SEAL — format contract:
  [ ] Verdict sentence: present in exact format "Signal accuracy for {topic}: {score}/100 — {STRONG|ADEQUATE|WEAK}. Count accuracy: {N}/{M} = {X}%."
  [ ] Weighted score: {score} drawn from Phase 4 TOTAL row — same number, not recalculated (verify by reading Phase 4 TOTAL)
  [ ] Count ratio: {N}/{M} = {X}% drawn from Phase 4 count-based statement — same values, not recalculated
  [ ] Tier label: STRONG if score >= 75 | ADEQUATE if 50 <= score < 75 | WEAK if score < 50 — must match stated score
All items confirmed against format? PHASE 6 COMPLETE.

---

PHASE 7 — GAP ANALYSIS
For each namespace scoring W or P in Phase 3, and each EMPTY namespace (Phase 2) where absence is material to the commit decision:

{{#if amend}}[AMEND: {{amend}} only — gaps outside this constraint excluded]{{/if}}

The gap table carries two structurally isolated columns that must contain different statements:
  - Column A — "Assumption held without evidence": the inertia belief that made this gap invisible before commit. WHY the gap existed. Framed as a prior belief ("We assumed X"), not as an outcome.
  - Column B — "Would have surfaced": the discovery missed. WHAT was missed. Different statement from Column A.
  Validation: if Column A and Column B contain the same statement, one column is wrong. Do not proceed with a merged row.

| Gap (signal type absent) | Namespace | Assumption held without evidence [A] | Skill to run | Would have surfaced [B] | Changed commit? YES / NO |
|--------------------------|-----------|--------------------------------------|-------------|-------------------------|--------------------------|
| [type] | [ns] | [prior belief — "We assumed X" — NOT an outcome] | [exact Signal skill, e.g., /listen-support] | [discovery statement — distinct from Column A] | YES / NO |

No gaps: "No gaps — signal coverage was sufficient for this commit decision."

Improvement recommendation — three required slots. Replace each `[slot:X]` token with specific content. The final output must not contain any `[slot:` strings — their presence indicates an unfilled slot.

  > **Recommendation**: Addresses [slot:gap-or-echo — name the specific gap type or Echo pattern addressed] by [slot:practice-change — name the specific practice change, not generic] so that [slot:measurable-outcome — state what would be observably different if this practice change succeeded].

PHASE 7 SEAL — format contract:
  [ ] Gap rows: every W or P namespace from Phase 3 has a row OR explicit "no gaps" statement — no silent omissions
  [ ] Material EMPTY namespaces: every one with commit-relevant absence has a row
  [ ] Column A format: {prior belief} framed as "We assumed X was true" or equivalent — NOT an outcome statement, NOT blank, NOT "unknown"
  [ ] Column B format: {discovery statement} — different content from Column A; answers "what was missed", not "why the gap existed"
  [ ] Column A != Column B: both columns must state different things per row — same statement in both = incomplete
  [ ] Skill format: {/exact-skill-name} — an exact Signal namespace skill name, not a namespace name, not "gather more data"
  [ ] Changed commit: exactly {YES} or {NO} per row — no other values
  [ ] Recommendation slot check: output does not contain the literal strings "[slot:gap-or-echo]", "[slot:practice-change]", or "[slot:measurable-outcome]" — all three tokens replaced with specific content
  {{#if amend}}[ ] AMEND scope marker: "[AMEND: {{amend}} only — ...]" present above gap table{{/if}}
All items confirmed against format? PHASE 7 COMPLETE.

---

PHASE 8 — CALIBRATION TREND

COPY the accuracy score from the Phase 6 verdict sentence into the "This score" cell. Do not recompute or derive this number. The Phase 6 verdict sentence is the authoritative source — transfer the number verbatim. Label the cell: COPY-VERIFIED [source: Phase 6 verdict].

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [reference or "none"] | [prior score or "—"] | {number}/100 — COPY-VERIFIED [source: Phase 6 verdict] | [delta or "—"] | ↑ improving / ↓ degrading / = stable |

No prior retro: "First retro for this topic — this score establishes the calibration baseline."

PHASE 8 SEAL — format contract:
  [ ] Prior retro: {topic-name} / {YYYY-MM-DD} OR the exact string "none" — not blank, not "N/A"
  [ ] This score: {number}/100 — value must be present and non-blank
  [ ] COPY-VERIFIED: confirmed — the "This score" value was traced to the Phase 6 verdict sentence directly; it was not recomputed from Phase 4 TOTAL; the cell carries the label "COPY-VERIFIED [source: Phase 6 verdict]"
  [ ] COPY-SOURCE: "Phase 6 verdict sentence" — the authoritative source is Phase 6, not Phase 4; confirm by opening Phase 6 and reading the verdict sentence before marking this item complete
  [ ] Delta: {+N or -N or 0} OR "—" when no prior retro
  [ ] Trend: one of exactly: ↑ improving | ↓ degrading | = stable OR the "first retro" statement
All items confirmed against format? PHASE 8 COMPLETE.

---

PHASE 9 — ECHO → SIGNAL DESIGN
Translate the Phase 1 Echo and Pattern into one concrete practice change.

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [exact Echo cell content — not paraphrased] | [exact Pattern name from Phase 1 — same taxonomy label, not a synonym] | [one specific practice change — not "gather more signals"] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL — format contract:
  [ ] Echo cell: {Phase 1 Echo copied verbatim} — must match Phase 1 Echo cell character-for-character; paraphrase = incomplete
  [ ] Pattern cell: {Phase 1 taxonomy label copied verbatim} — must match Phase 1 Pattern name exactly; synonym = incomplete
  [ ] Proposed change: {one specific actionable change} — not "gather more signals", not generic
  [ ] Change type: exactly one of: new skill | rubric amendment | threshold adjustment
All items confirmed against format? RETRO COMPLETE.

---

Execute phases in order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9. Verify compliance against PRE-EXECUTION CONTRACT before marking complete.

Design guarantees (audit reference):
- Phase 1: Echo locked. Pattern and Why-unexpected required. Locked before signal comparison.
- Phase 2: Fixed 9-row table; COVERED/EMPTY only. AMEND adds OOS secondary table.
- Phase 4: Weighted score AND N/M=X% count ratio — both required, both named SEAL fields.
- Phase 6: Verdict copies both formats from Phase 4. No recalculation. Exact sentence format.
- Phase 7: Column A = belief, Column B = outcome; must not share content. Three-slot `[slot:X]` recommendation; no `[slot:` strings in output.
- Phase 8: Score COPIED from Phase 6 verdict sentence. Cell: COPY-VERIFIED [source: Phase 6 verdict]. SEAL: three fields (`This score`, `COPY-VERIFIED`, `COPY-SOURCE` = "Phase 6 verdict sentence").
- All 9 seals: explicit format-string per field (not just field names).
- AMEND: scope marker on every table; Phase 2 OOS secondary table.
```
