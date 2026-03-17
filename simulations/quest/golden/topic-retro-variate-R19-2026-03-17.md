# topic-retro -- Variations R19
**Date:** 2026-03-17
**Rubric:** v17 (C-01 through C-45; total available = 164)
**R18 top scorer:** V-05 -- discovered C-44 and C-45 as excellence patterns. Source criteria for this round.
**New criteria to target:** C-44 (SEAL-enforced bidirectional navigation completeness) and C-45 (assessor navigation preamble, three-entry-point declaration).

**Base used:** R18-V-05 -- all prior integrations carried forward:
- C-22: OOS secondary table
- C-23: Seal format-contract strings per field (all 9 phases)
- C-24: Echo why-unexpected explained
- C-25: Three-slot recommendation template
- C-26: Gap inertia columns A/B structurally isolated
- C-27: SEAL coverage extended to all phases
- C-28: `[slot:X]` token + SEAL placeholder check
- C-29: Phase 8 "do not recompute" + SEAL copy-citation check
- C-30: Three-field SEAL (This score / COPY-VERIFIED / COPY-SOURCE)
- C-31: `## PRE-EXECUTION CONTRACT` two-column table positioned before Phase 1
- C-32: Phase 8 SEAL each field has independent CHECK:/HOW: block with self-contained source
- C-33: PRE-EXECUTION CONTRACT three-column table with "Verified in" enforcement pointer
- C-36: Three-pass architectural isolation as structural property
- C-37: Accuracy reconciliation cross-check (forward count + backward count must agree)
- C-38: Backward recovery table as named structural artifact
- C-39: Signal window and Mode declared as named fields in PRE-EXECUTION CONTRACT
- C-40: AUDIT MANIFEST as primary table; all downstream sections derived as views
- C-41: Named-criteria phase gate
- C-42: Bidirectional manifest citation (`Derived Views` column + `[DERIVED FROM]` headers)
- C-43: PRE-EXECUTION CONTRACT as manifest navigation index (`Manifest column` field)

**C-44 gap analysis:** R18-V-05 has the Derived Views column and downstream DERIVED FROM headers (satisfying C-42), and Phase 0 SEAL items for check statements. C-44 requires three upgrades the R18-V-05 SEAL does not enforce: (a) Derived Views entries must use EXACT canonical table identifiers ("Phase 2 Signal Coverage Table" not "Phase 2 coverage table"), (b) the forward check statement must explicitly DECLARE the direction as VERIFIED -- not describe future intent ("Derived Views will name tables"), and (c) the backward check statement must explicitly DECLARE the direction as VERIFIED -- not state what headers will appear. R18-V-05's check statements say "Derived Views names at least one specific downstream table" and "downstream sections will carry [DERIVED FROM] headers" -- these are intent descriptions, not verified declarations. C-44 requires the stronger form: "FORWARD VERIFIED: manifest -> downstream navigation confirmed" and "BACKWARD VERIFIED: downstream -> manifest navigation confirmed" as explicit output assertions.

**C-45 gap analysis:** R18-V-05's PRE-EXECUTION CONTRACT opening contains entry-point information in prose bold paragraphs: "**Entry from AUDIT MANIFEST row**: Use the `Derived Views` column..." etc. C-45 requires a structured block (not prose) naming all three entry points. Bold paragraph format = PARTIAL per rubric. A structured table (or equivalent labeled block) naming all three navigation paths is required for PASS. R18-V-05 has the content but not the structure.

**Single-axis:** V-01 (C-44), V-02 (C-45), V-03 (phrasing register negative control).
**Combined:** V-04 (C-44 + C-45), V-05 (C-44 + C-45 + preamble/SEAL cross-reference).

---

## Summary Table

| ID | Primary Axis | C-44 Mechanism | C-45 Mechanism | Hypothesis |
|----|-------------|----------------|----------------|------------|
| V-01 | C-44 (single) | Phase 0 Derived Views uses canonical table identifiers; post-manifest FORWARD VERIFIED + BACKWARD VERIFIED declarations; SEAL items require exact names and explicit verification declarations | R18-V-05 prose entry points unchanged (no structured preamble block) | Upgrading check statements from intent-description to verified-declaration satisfies C-44; prose entry points remain PARTIAL on C-45 |
| V-02 | C-45 (single) | R18-V-05 check statements unchanged; Derived Views uses existing exact-name requirement | ASSESSOR NAVIGATION PREAMBLE table added before PRE-EXECUTION CONTRACT mechanism table; three entry points in a structured block (not prose) | Replacing prose entry points with a structured three-row navigation table satisfies C-45; existing check statements remain at C-44 level |
| V-03 | Phrasing register (negative control) | Derived Views uses informal aliases ("coverage table", "accuracy table"); post-manifest statements describe intent rather than declare verification; SEAL items test for presence, not declaration strength | Entry points remain as prose bold paragraphs from R18-V-05 | Both C-44 and C-45 score PARTIAL: informal table names fail C-44a; intent descriptions fail C-44b/c; prose blocks fail C-45; confirms structural enforcement distinguishes PASS from PARTIAL |
| V-04 | C-44 + C-45 (combined) | V-01 canonical names + FORWARD/BACKWARD VERIFIED declarations | V-02 structured ASSESSOR NAVIGATION PREAMBLE table | Zero-interference test: C-44 lives in Phase 0 SEAL; C-45 lives in PRE-EXECUTION CONTRACT preamble; no shared modification surface; adding both simultaneously should produce full PASS on both |
| V-05 | Full integration (preamble/SEAL cross-reference) | Phase 0 canonical names + VERIFIED declarations reference "per canonical table names declared in ASSESSOR NAVIGATION PREAMBLE"; SEAL adds cross-check item confirming Derived Views names match preamble's declared canonical set | ASSESSOR NAVIGATION PREAMBLE table names exact canonical table identifiers for entry point 2; preamble is the single source of truth that both SEAL and VERIFIED declarations reference | Cross-referencing closes drift: if a Derived Views entry uses a non-canonical name, the preamble cross-check SEAL item catches it; preamble and SEAL mutually enforce each other |

---

## V-01 -- SEAL-Enforced Bidirectional Navigation: C-44 via Exact Names and Verified Declarations

**Axis:** C-44 mechanism (single). Phase 0 Derived Views assignment rules use canonical table identifiers. Post-manifest block writes explicit FORWARD VERIFIED and BACKWARD VERIFIED declarations (not intent descriptions). Phase 0 SEAL upgrades items for exact canonical names and verified-declaration requirement. PRE-EXECUTION CONTRACT retained from R18-V-05 with prose entry points and Manifest column -- C-45 NOT addressed.

**Hypothesis:** R18-V-05's check statements describe what the Derived Views column will contain and what headers will appear -- this satisfies C-42 but falls short of C-44 because they are intent descriptions, not verification declarations. Upgrading to "FORWARD VERIFIED: ... confirmed" and "BACKWARD VERIFIED: ... confirmed" with exact canonical table names in both the Derived Views entries and the declarations satisfies C-44's three sub-conditions. Prose entry points remain PARTIAL on C-45, so the variation isolates the C-44 gain.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Execute phases in order. Each phase ends with a PHASE SEAL -- a format-contract checklist where every item specifies the required field and its required value form. Do not proceed past a phase until every seal item is confirmed.

{{#if amend}}AMEND SCOPE: {{amend}} -- all phases operate within this constraint only. Every table carries an explicit scope marker. Phase 2 includes an out-of-scope table.{{/if}}

---

## PRE-EXECUTION CONTRACT

Read before executing Phase 0. This retro is a bidirectional audit system navigable from three entry points:

**Entry from AUDIT MANIFEST row**: Use the `Derived Views` column to identify which downstream tables the row feeds. Navigate forward without reading phase specifications.
**Entry from downstream section**: Use the `[DERIVED FROM: AUDIT MANIFEST | OPERATION: ...]` header to navigate backward to the manifest rows that sourced the section.
**Entry from contract row**: Use the `Manifest column` field to identify the exact AUDIT MANIFEST column that will evidence fulfillment of each commitment. Navigate to the manifest before execution begins.

| Mechanism | Structural guarantee -- what is enforced and how | Verified in | Manifest column |
|-----------|------------------------------------------------|-------------|-----------------|
| Signal window | Bounding date range or sprint scope. Named structural field in manifest header -- not inferred from prose. | Phase 0 SEAL item 1 | Signal window (manifest header field) |
| Mode | AMEND or FRESH flag. AMEND: scope declared top, every table scoped, Phase 2 OOS table. | Phase 0 SEAL item 2; Phase 2 SEAL item 6 if AMEND | Mode (manifest header field) |
| Echo lock | Phase 1 before signal comparison. Echo/Pattern/Why-unexpected locked. Phases 2-9 must not modify. | Phase 1 SEAL items 1-5 | Prediction (Echo is the finding absent from this column) |
| Manifest derivation | All downstream tables derived as views of AUDIT MANIFEST. Derivation stated per section. Derived Views column present in manifest. | Phase 0 SEAL items 3-7; [DERIVED FROM] headers in all downstream sections | (all columns -- manifest is the derivation source) |
| Namespace coverage | Fixed 9-row table, COVERED/EMPTY derived by grouping manifest Namespace column. | Phase 2 SEAL items 1-5 | Namespace |
| Verdict accuracy | Weighted score and count ratio required. Reconciliation cross-check required. | Phase 4 SEAL items 4-5; RECONCILIATION TABLE | Verdict |
| Gap identification | W or P manifest rows feed gap table. Material EMPTY namespaces included. | Phase 7 SEAL items 1-2 | Verdict (filter: W or P) |
| Accuracy copy | Phase 6 copies Phase 4 TOTAL. Phase 8 copies Phase 6 verdict sentence. No recomputation at any stage. | Phase 6 SEAL; Phase 8 SEAL items 2-4 | Verdict (aggregate: TOTAL weighted score) |
| Gap inertia columns | Column A = prior belief; Column B = missed discovery; must not share content per row. | Phase 7 SEAL items 3-5 | Verdict (gap rows; Column A frames the assumption behind a W/P verdict) |
| Recommendation slots | Three `[slot:X]` tokens; SEAL confirms no `[slot:` strings survive. | Phase 7 SEAL item 8 | (generated, not manifest-derived) |
| Copy guard | Phase 8 COPIED from Phase 6. Three-field SEAL: This score / COPY-VERIFIED / COPY-SOURCE each with independent CHECK/HOW. | Phase 8 SEAL items 2-4 | Verdict (aggregate) |
| Seal format contracts | All 9 seals: explicit format-string per field; verify value form, not just presence. | All 9 SEAL blocks | (all columns) |
| AMEND scope | Every table has scope marker when AMEND set. Phase 2 OOS table present. | Phase 2 SEAL item 6 | (all columns -- scope filter applied to all manifest rows) |

---

## PHASE 0 -- AUDIT MANIFEST

Before running any phase, enumerate all signal artifacts and build the AUDIT MANIFEST. All downstream tables are derived from this manifest. The `Derived Views` column enables forward navigation: an assessor at any manifest row can identify which downstream tables include it without reading phase specifications. Use the canonical table identifiers below -- abbreviations and informal aliases are not acceptable.

Signal window: [state the date range or sprint scope bounding the predictions being evaluated]
Mode: AMEND ({{amend}}) | FRESH [circle one]

Search simulations/**/[topic]-*-*.md. For each artifact record namespace, prediction, actual outcome, verdict, and forward-navigation destinations using canonical table names only.

| # | Namespace | Artifact | Prediction (signal's claim) | Actual (post-ship) | Verdict (C/P/W/ND) | Derived Views |
|---|-----------|----------|----------------------------|-------------------|-------------------|---------------|
| 1 | [ns] | [filename] | [what signal claimed would happen] | [what was observed post-ship] | C / P / W / ND | [Phase 2 Signal Coverage Table; Phase 3 Predicted vs Actual Table (if non-ND); Phase 4 Namespace Accuracy Table (if non-ND); Phase 4 Reconciliation Table; Phase 7 Gap Analysis Table (if W or P)] |
| ... | | | | | | |

Canonical Derived Views assignment rules (use these exact table names):
- Every row -> "Phase 2 Signal Coverage Table"
- Rows with non-ND verdict -> add "Phase 3 Predicted vs Actual Table; Phase 4 Namespace Accuracy Table"
- Rows with Verdict = W -> add "Phase 7 Gap Analysis Table"
- Rows with Verdict = P -> add "Phase 7 Gap Analysis Table"
- Every row -> add "Phase 4 Reconciliation Table" (ND rows are excluded from denominator but still appear in Reconciliation)

After completing the manifest, write the bidirectional navigation verification block:

  FORWARD VERIFIED: Manifest -> downstream direction confirmed. Each manifest row's Derived Views column names downstream tables using canonical identifiers from the set {Phase 2 Signal Coverage Table, Phase 3 Predicted vs Actual Table, Phase 4 Namespace Accuracy Table, Phase 4 Reconciliation Table, Phase 7 Gap Analysis Table}. An assessor reading any manifest row can navigate forward to downstream sections without reading phase specifications. Forward navigation confirmed complete.

  BACKWARD VERIFIED: Downstream -> manifest direction confirmed. Each downstream section -- Phase 2 Signal Coverage Table, Phase 3 Predicted vs Actual Table, Phase 4 Namespace Accuracy Table, Phase 4 Reconciliation Table, Phase 7 Gap Analysis Table -- carries a [DERIVED FROM: AUDIT MANIFEST | OPERATION: ...] header that names this manifest as its source. An assessor reading any downstream section can navigate backward to the manifest. Backward navigation confirmed complete.

PHASE 0 SEAL -- format contract:
  [ ] Signal window: {date range or sprint name} -- named structural field in manifest header; not inferred from prose
  [ ] Mode: {AMEND | FRESH} -- named field present; if AMEND, {{amend}} scope carried into all phases
  [ ] Manifest rows: one row per signal artifact found; no namespace groups without individual rows
  [ ] Verdict: {C | P | W | ND} per row -- no other values, no blank
  [ ] Derived Views exact canonical names: each entry uses a name from the canonical set exactly -- "Phase 2 Signal Coverage Table" not "Phase 2 table", "Phase 2 coverage table", or "coverage"; "Phase 7 Gap Analysis Table" not "Phase 7 gap table" or "gap table"; non-canonical alias = FAIL this item
  [ ] FORWARD VERIFIED declaration: statement beginning with "FORWARD VERIFIED:" present after manifest table; explicitly declares manifest -> downstream direction as confirmed; intent description ("Derived Views names tables") without the verification assertion = FAIL this item
  [ ] BACKWARD VERIFIED declaration: statement beginning with "BACKWARD VERIFIED:" present after manifest table; explicitly declares downstream -> manifest direction as confirmed; future-tense statement ("headers will carry") without the verification assertion = FAIL this item
All items confirmed against format? PHASE 0 COMPLETE.

---

PHASE 1 -- ECHO
Run this phase before examining signal accuracy comparisons in Phase 3.

{{#if amend}}[AMEND: {{amend}} only -- outcomes outside this scope excluded from Echo candidacy]{{/if}}

The Echo is the single post-ship observable satisfying all three conditions:
  (a) Not predicted by any gathered signal -- not even partially
  (b) Not a named risk or acknowledged unknown at commit time
  (c) Observable only after the feature shipped

Procedure:
  Step 1: List every post-ship outcome (within AMEND scope if set).
  Step 2: Eliminate outcomes predicted by gathered signals.
  Step 3: Eliminate named risks or known unknowns.
  Step 4: Select the one with highest commit-decision impact.
  Step 5: No candidates: Echo = "No Echo -- all post-ship outcomes were within signal bounds."

| Echo (one sentence) | Nearest signal artifact | Commit relevance: HIGH / MEDIUM / LOW |
|---------------------|------------------------|--------------------------------------|
| [finding or "No Echo -- all post-ship outcomes were within signal bounds"] | [name or "none"] | [HIGH / MEDIUM / LOW or "N/A"] |

Immediately after the table:
  > **Pattern**: [name from taxonomy or "other: [your name]"] -- [description of recurring failure mode -- not Echo restatement]
  > **Why unexpected**: [prior belief contradicted -- what was expected and why reality diverged]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

LOCK: Echo table, Pattern, and Why-unexpected are final. Phases 2-9 may not change them.

PHASE 1 SEAL -- format contract:
  [ ] Echo: {one sentence} OR exact string "No Echo -- all post-ship outcomes were within signal bounds"
  [ ] Nearest signal: {artifact-filename.md} OR exact string "none"
  [ ] Commit relevance: HIGH | MEDIUM | LOW | N/A -- "N/A" only valid when paired with "No Echo"
  [ ] Pattern: "> **Pattern**: {taxonomy-label or "other: name"} -- {failure class description -- not Echo restatement}"
  [ ] Why unexpected: "> **Why unexpected**: {prior belief contradicted -- names what was expected, not just that it was unexpected}"
  {{#if amend}}[ ] AMEND scope marker: "[AMEND: {{amend}} only -- ...]" present immediately above table{{/if}}
All items confirmed against format? PHASE 1 COMPLETE.

---

PHASE 2 -- SIGNAL INVENTORY
[DERIVED FROM: AUDIT MANIFEST | OPERATION: group by Namespace, count rows per group, assign COVERED if count >= 1 else EMPTY]

Produce a fixed 9-row namespace coverage table. Every namespace gets exactly one row. Derive from Phase 0 AUDIT MANIFEST -- do not re-examine artifacts independently.

{{#if amend}}[AMEND: {{amend}} only -- out-of-scope artifacts go to the OOS table below, not the main table]{{/if}}

| Namespace | Status          | Artifact count | Primary artifact (or "--") | Prediction theme (or "--") |
|-----------|-----------------|----------------|--------------------------|--------------------------|
| scout     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| draft     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| review    | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| flow      | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| trace     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| prove     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| listen    | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| program   | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| topic     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| TOTAL     |                 | N              |                          |                          |

{{#if amend}}Out-of-scope artifacts (excluded per AMEND constraint):
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside {{amend}} scope] |
If none excluded: "No artifacts excluded -- all in scope."
{{/if}}

PHASE 2 SEAL -- format contract:
  [ ] All 9 namespace rows present in exact order: scout, draft, review, flow, trace, prove, listen, program, topic
  [ ] Status: {COVERED} or {EMPTY} per row -- no other value, no blank
  [ ] Artifact count: {integer} per row -- 0 valid for EMPTY
  [ ] Primary artifact: {filename.md} or the string "--" -- not blank
  [ ] TOTAL row: present with {integer} in Artifact count cell
  {{#if amend}}[ ] OOS table: present immediately after main table -- even if "No artifacts excluded -- all in scope."{{/if}}
  [ ] Derived From header: "[DERIVED FROM: AUDIT MANIFEST | OPERATION: group by Namespace...]" present above table
All items confirmed against format? PHASE 2 COMPLETE.

---

PHASE 3 -- PREDICTED VS ACTUAL
[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter rows where Namespace is COVERED; surface Prediction, Actual, Verdict per namespace]

For each namespace with Status = COVERED in Phase 2. Derive from AUDIT MANIFEST rows -- do not independently re-evaluate predictions.

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted (signals' collective claim post-ship) | Actual (what was observed) | Match: C / P / W / ND |
|-----------|------------------------------------------------|---------------------------|----------------------|
| [name] | [required -- from AUDIT MANIFEST Prediction column] | [required -- from AUDIT MANIFEST Actual column] | [from AUDIT MANIFEST Verdict column] |

C = Correct, P = Partial (direction right, magnitude/timing off), W = Wrong, ND = No post-ship data yet.

PHASE 3 SEAL -- format contract:
  [ ] Row count: one row per COVERED namespace from Phase 2 -- no omissions, no extras
  [ ] Predicted: {one phrase or sentence} -- not blank, not "N/A", not "unknown"
  [ ] Actual: {one phrase or sentence} -- not blank, not "N/A", not "unknown"
  [ ] Match: one of exactly: C | P | W | ND
  [ ] Derived From header: "[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter COVERED namespaces]" present above table
  {{#if amend}}[ ] Scope marker: "[AMEND: {{amend}} only]" present above table{{/if}}
All items confirmed against format? PHASE 3 COMPLETE.

---

PHASE 4 -- NAMESPACE ACCURACY
[DERIVED FROM: AUDIT MANIFEST | OPERATION: count Verdict values by Namespace; exclude ND from denominator]

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Weighted score: (Cx100 + Px50) / (C+P+W) |
|-----------|---|---|---|-----|------------------------------------------|
| [name]    |   |   |   |     |                                          |
| TOTAL     |   |   |   |     |                                          |

ND excluded from denominator. Score blank if denominator = 0 (note as "0 scored signals").

After the scoring table, state the count-based accuracy ratio:
  Correct signals: {C count} / {C+P+W count} = X%

RECONCILIATION TABLE:
[DERIVED FROM: AUDIT MANIFEST | OPERATION: forward sequential count vs backward recovery from Verdict = W]

| Direction | Starting point | Steps | Total scored | Correct | Match? |
|-----------|---------------|-------|--------------|---------|--------|
| Forward | Manifest row 1, count each scored verdict sequentially | [+1 C, +1 W, etc.] | {N} | {C} | -- |
| Backward | W count = {W}; +P = {P}; +C = {C}; total scored = {N} | [recovery arithmetic shown] | {N} | C = total - W - P = {C} | YES / NO |

Reconciliation result: Forward = {N}; Backward = {N}; Match: YES (proceed) / NO (recheck manifest).

PHASE 4 SEAL -- format contract:
  [ ] Row count: one row per Phase 3 namespace -- no omissions
  [ ] C, P, W, ND: {integer} per cell -- blank invalid; 0 valid
  [ ] Weighted score: {number}/100 per row OR blank with note "0 scored signals"
  [ ] TOTAL row: present, format: {number}/100
  [ ] Count-based ratio: stated in format "{N}/{M} = {X}%" immediately below scoring table
  [ ] RECONCILIATION TABLE: present with Forward and Backward rows and result row
  [ ] Reconciliation result: Match = YES before proceeding -- NO = reconciliation failure, do not continue
  [ ] Derived From header: "[DERIVED FROM: AUDIT MANIFEST | OPERATION: count Verdict values...]" present above scoring table
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed against format? PHASE 4 COMPLETE.

---

PHASE 5 -- CONFLICT AUDIT
Mandatory. Always produces exactly one of two outputs.

Review the locked Phase 1 Echo. Does any Phase 3 verdict or Phase 4 score suggest the Echo should name a different finding?

If YES:
  CONFLICT DETECTED
  Source: {Phase 3 row namespace / Phase 4 score -- specific finding creating tension}
  Analysis: {what the finding suggests the Echo should become}
  Resolution: Phase 1 Echo is preserved unchanged. This block is the conflict artifact.

If NO:
  CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo.

PHASE 5 SEAL -- format contract:
  [ ] Output: exactly one of -- CONFLICT DETECTED block (Source/Analysis/Resolution non-blank) OR exact string "CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo."
  [ ] Phase 1 modification: none -- Echo table, Pattern, and Why-unexpected unchanged
All items confirmed against format? PHASE 5 COMPLETE.

---

PHASE 6 -- ACCURACY VERDICT
Draw weighted score from Phase 4 TOTAL row. Draw count ratio from Phase 4 count-based statement. Do not recalculate either number.

State the verdict:
  "Signal accuracy for [topic]: [TOTAL weighted score]/100 -- [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]. Count accuracy: [N/M = X%]."

PHASE 6 SEAL -- format contract:
  [ ] Verdict sentence: present in exact format "Signal accuracy for {topic}: {score}/100 -- {STRONG|ADEQUATE|WEAK}. Count accuracy: {N}/{M} = {X}%."
  [ ] Weighted score: drawn from Phase 4 TOTAL row -- same number, not recalculated
  [ ] Count ratio: drawn from Phase 4 count-based statement -- same values, not recalculated
  [ ] Tier label: STRONG if >= 75 | ADEQUATE if 50-74 | WEAK if < 50 -- must match stated score
All items confirmed against format? PHASE 6 COMPLETE.

---

PHASE 7 -- GAP ANALYSIS
[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter rows where Verdict = W or P; add EMPTY namespaces where absence is material]

For each namespace scoring W or P in Phase 3, and each EMPTY namespace (Phase 2) where absence is material to the commit decision.

{{#if amend}}[AMEND: {{amend}} only -- gaps outside this constraint excluded]{{/if}}

Column A = "Assumption held without evidence": the inertia belief that made this gap invisible before commit. WHY the gap existed. Framed as prior belief ("We assumed X"), not an outcome.
Column B = "Would have surfaced": the discovery missed. WHAT was missed. Different statement from Column A.

| Gap (signal type absent) | Namespace | Assumption held without evidence [A] | Skill to run | Would have surfaced [B] | Changed commit? YES / NO |
|--------------------------|-----------|--------------------------------------|-------------|-------------------------|--------------------------|
| [type] | [ns] | [prior belief -- "We assumed X" -- NOT an outcome] | [/exact-skill-name] | [discovery -- distinct from Column A] | YES / NO |

No gaps: "No gaps -- signal coverage was sufficient for this commit decision."

Improvement recommendation -- three required slots. Replace each `[slot:X]` token. Output must contain no `[slot:` strings.

  > **Recommendation**: Addresses [slot:gap-or-echo -- name the specific gap type or Echo pattern] by [slot:practice-change -- name the specific practice change, not generic] so that [slot:measurable-outcome -- state what would be observably different if this practice change succeeded].

PHASE 7 SEAL -- format contract:
  [ ] Gap rows: every W or P namespace from Phase 3 has a row OR explicit "no gaps" statement
  [ ] Material EMPTY namespaces: every one with commit-relevant absence has a row
  [ ] Column A format: {prior belief} framed as "We assumed X" -- NOT an outcome statement, NOT blank
  [ ] Column B format: {discovery statement} -- different content from Column A
  [ ] Column A != Column B: both columns state different things per row
  [ ] Skill format: {/exact-skill-name} -- exact Signal skill, not a namespace name
  [ ] Changed commit: {YES} or {NO} per row
  [ ] Recommendation slot check: output does not contain "[slot:gap-or-echo]", "[slot:practice-change]", or "[slot:measurable-outcome]"
  [ ] Derived From header: "[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter W or P rows; add material EMPTY namespaces]" present above gap table
  {{#if amend}}[ ] AMEND scope marker present above gap table{{/if}}
All items confirmed against format? PHASE 7 COMPLETE.

---

PHASE 8 -- CALIBRATION TREND

COPY the accuracy score from the Phase 6 verdict sentence into the "This score" cell. Do not recompute or derive this number. The Phase 6 verdict sentence is the authoritative source -- transfer the number verbatim. Label the cell: COPY-VERIFIED [source: Phase 6 verdict].

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [reference or "none"] | [prior score or "--"] | {number}/100 -- COPY-VERIFIED [source: Phase 6 verdict] | [delta or "--"] | up improving / down degrading / = stable |

No prior retro: "First retro for this topic -- this score establishes the calibration baseline."

PHASE 8 SEAL -- format contract:
  [ ] Prior retro: {topic-name} / {YYYY-MM-DD} OR exact string "none"
      Delta: {+N or -N or 0} OR "--" when no prior retro
      Trend: up improving | down degrading | = stable OR the "first retro" statement

  [ ] This score -- independent verification:
      CHECK: The Phase 8 calibration table "This score" cell contains a value.
      HOW: Read the "This score" cell in the Phase 8 calibration table above. Confirm it is non-blank and in {number}/100 format. Do not read Phase 6 or Phase 4 to verify this item -- this check is about the cell itself only.
      Format required: {number}/100 -- blank or wrong format = FAIL.

  [ ] COPY-VERIFIED -- independent verification:
      CHECK: The score in "This score" was copied from Phase 6, not computed.
      HOW: Open Phase 6. Read the verdict sentence. Find the score number (value before "/100"). Compare to "This score" cell value. If they match AND the cell label contains "COPY-VERIFIED", this item passes. Do not read Phase 4 to perform this check.
      Format required: cell label contains "COPY-VERIFIED" -- absent label = FAIL regardless of number match.

  [ ] COPY-SOURCE -- independent verification:
      CHECK: "This score" cell names Phase 6 verdict as the copy source, not Phase 4.
      HOW: Read the "This score" cell label. Confirm it names "Phase 6 verdict" or equivalent. A label naming Phase 4, absent label, or label saying "computed" = FAIL. Arriving at the same number via Phase 4 does not satisfy this check -- the source is the label, not the value's mathematical origin.
      Format required: cell label contains "source: Phase 6 verdict" -- alternative source or blank = FAIL.

All items confirmed against format? PHASE 8 COMPLETE.

---

PHASE 9 -- ECHO -> SIGNAL DESIGN
Translate the Phase 1 Echo and Pattern into one concrete practice change.

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [exact Echo cell content -- not paraphrased] | [exact Pattern name -- same taxonomy label] | [one specific practice change] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL -- format contract:
  [ ] Echo cell: {Phase 1 Echo copied verbatim} -- must match Phase 1 Echo cell character-for-character
  [ ] Pattern cell: {Phase 1 taxonomy label copied verbatim} -- exact match, not synonym
  [ ] Proposed change: {one specific actionable change} -- not "gather more signals", not generic
  [ ] Change type: one of: new skill | rubric amendment | threshold adjustment
All items confirmed against format? RETRO COMPLETE.

---

Execute phases in order: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9. Verify compliance against PRE-EXECUTION CONTRACT before marking complete.

Design guarantees (audit reference):
- PRE-EXECUTION CONTRACT: four-column table (Mechanism / Guarantee / Verified in / Manifest column). Prose entry points (three bold paragraphs) above contract table.
- Phase 0: AUDIT MANIFEST with Signal window, Mode, Verdict per row, Derived Views per row using canonical table identifiers. FORWARD VERIFIED and BACKWARD VERIFIED declarations required after manifest. All downstream tables derived from this manifest.
- Phase 1: Echo locked before signal comparison. Pattern and Why-unexpected required.
- Phase 2: Fixed 9-row table. AMEND adds OOS secondary table. [DERIVED FROM: AUDIT MANIFEST] header required.
- Phase 3: [DERIVED FROM: AUDIT MANIFEST] header required. One row per COVERED namespace.
- Phase 4: Weighted score AND count ratio. RECONCILIATION TABLE required. [DERIVED FROM: AUDIT MANIFEST] header required.
- Phase 6: Verdict copies both formats from Phase 4. No recalculation. Exact sentence format.
- Phase 7: Column A = belief, Column B = outcome; must not share content. Three-slot [slot:X]; no [slot: strings in output. [DERIVED FROM: AUDIT MANIFEST] header required.
- Phase 8: Score COPIED from Phase 6 verdict sentence. Cell: COPY-VERIFIED [source: Phase 6 verdict]. SEAL: three independent fields each with CHECK:/HOW: blocks.
- All 9 seals: explicit format-string per field.
```

---

## V-02 -- Assessor Navigation Preamble: C-45 via Structured Three-Entry-Point Block

**Axis:** C-45 mechanism (single). PRE-EXECUTION CONTRACT gains an ASSESSOR NAVIGATION PREAMBLE structured table naming all three valid audit entry points, positioned before the mechanism rows. This replaces the prose bold-paragraph entry descriptions from R18-V-05 with a structured block. Phase 0 Derived Views and SEAL items unchanged from R18-V-05 -- C-44 NOT addressed.

**Hypothesis:** R18-V-05's bold-paragraph entry points convey the same information as a structured preamble but fail C-45 because they are prose, not a structural block. A three-row navigation table where each row declares a starting position, a navigation field, and a destination constitutes the "structured block" C-45 requires. Phase 0 check statements remain at R18-V-05 level (intent descriptions, not VERIFIED declarations), so C-44 remains PARTIAL, isolating the C-45 gain.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Execute phases in order. Each phase ends with a PHASE SEAL -- a format-contract checklist where every item specifies the required field and its required value form. Do not proceed past a phase until every seal item is confirmed.

{{#if amend}}AMEND SCOPE: {{amend}} -- all phases operate within this constraint only. Every table carries an explicit scope marker. Phase 2 includes an out-of-scope table.{{/if}}

---

## PRE-EXECUTION CONTRACT

Read before executing Phase 0.

### ASSESSOR NAVIGATION PREAMBLE

This audit system supports three entry points. No prior knowledge of the architecture is required. Locate the row matching your starting position and follow the navigation field.

| # | If you are starting at... | Locate this navigation field | It takes you to... |
|---|--------------------------|-----------------------------|--------------------|
| 1 | Any row in this PRE-EXECUTION CONTRACT | `Manifest column` field (4th column of this table) | The exact AUDIT MANIFEST column that evidences the commitment in that row |
| 2 | Any row in the AUDIT MANIFEST (Phase 0) | `Derived Views` column (last column of the Phase 0 table) | The exact downstream table(s) that receive data from that manifest row |
| 3 | Any downstream section header (Phase 2, Phase 3, Phase 4, Phase 7) | `[DERIVED FROM: AUDIT MANIFEST \| OPERATION: ...]` declaration in the section header | The AUDIT MANIFEST as the data source for that section |

A completed retro is auditable from any of these three positions without reading the full document in sequence.

| Mechanism | Structural guarantee -- what is enforced and how | Verified in | Manifest column |
|-----------|------------------------------------------------|-------------|-----------------|
| Signal window | Bounding date range or sprint scope. Named structural field in manifest header -- not inferred from prose. | Phase 0 SEAL item 1 | Signal window (manifest header field) |
| Mode | AMEND or FRESH flag. AMEND: scope declared top, every table scoped, Phase 2 OOS table. | Phase 0 SEAL item 2; Phase 2 SEAL item 6 if AMEND | Mode (manifest header field) |
| Echo lock | Phase 1 before signal comparison. Echo/Pattern/Why-unexpected locked. Phases 2-9 must not modify. | Phase 1 SEAL items 1-5 | Prediction (Echo is the finding absent from this column) |
| Manifest derivation | All downstream tables derived as views of AUDIT MANIFEST. Derivation stated per section. Derived Views column in manifest enables forward navigation; [DERIVED FROM] headers enable backward navigation. | Phase 0 SEAL items 3-7; [DERIVED FROM] headers in all downstream sections | (all columns -- manifest is the derivation source) |
| Namespace coverage | Fixed 9-row table, COVERED/EMPTY derived by grouping manifest Namespace column. | Phase 2 SEAL items 1-5 | Namespace |
| Verdict accuracy | Weighted score and count ratio required. Reconciliation cross-check required. | Phase 4 SEAL items 4-5; RECONCILIATION TABLE | Verdict |
| Gap identification | W or P manifest rows feed gap table. Material EMPTY namespaces included. | Phase 7 SEAL items 1-2 | Verdict (filter: W or P) |
| Accuracy copy | Phase 6 copies Phase 4 TOTAL. Phase 8 copies Phase 6 verdict sentence. No recomputation at any stage. | Phase 6 SEAL; Phase 8 SEAL items 2-4 | Verdict (aggregate: TOTAL weighted score) |
| Gap inertia columns | Column A = prior belief; Column B = missed discovery; must not share content per row. | Phase 7 SEAL items 3-5 | Verdict (gap rows) |
| Recommendation slots | Three `[slot:X]` tokens; SEAL confirms no `[slot:` strings survive. | Phase 7 SEAL item 8 | (generated, not manifest-derived) |
| Copy guard | Phase 8 COPIED from Phase 6. Three-field SEAL: This score / COPY-VERIFIED / COPY-SOURCE each with independent CHECK/HOW. | Phase 8 SEAL items 2-4 | Verdict (aggregate) |
| Seal format contracts | All 9 seals: explicit format-string per field; verify value form, not just presence. | All 9 SEAL blocks | (all columns) |
| AMEND scope | Every table has scope marker when AMEND set. Phase 2 OOS table present. | Phase 2 SEAL item 6 | (all columns -- scope filter applied to all manifest rows) |

---

## PHASE 0 -- AUDIT MANIFEST

Before running any phase, enumerate all signal artifacts and build the AUDIT MANIFEST. All downstream tables are derived from this manifest. The `Derived Views` column enables forward navigation: an assessor at any manifest row can identify which downstream tables include it without reading phase specifications.

Signal window: [state the date range or sprint scope bounding the predictions being evaluated]
Mode: AMEND ({{amend}}) | FRESH [circle one]

Search simulations/**/[topic]-*-*.md. For each artifact record namespace, prediction, actual outcome, verdict, and which downstream tables the row feeds.

| # | Namespace | Artifact | Prediction (signal's claim) | Actual (post-ship) | Verdict (C/P/W/ND) | Derived Views |
|---|-----------|----------|----------------------------|-------------------|-------------------|---------------|
| 1 | [ns] | [filename] | [what signal claimed would happen] | [what was observed post-ship] | C / P / W / ND | [Phase 2 coverage table (Namespace count); Phase 3 predicted/actual; Phase 4 accuracy scoring (if scored); Phase 7 gap table (if W or P)] |
| ... | | | | | | |

Derived Views values:
- Every row -> "Phase 2 coverage table (Namespace count)"
- Rows with non-ND verdict -> add "Phase 3 predicted/actual; Phase 4 accuracy scoring"
- Rows with Verdict = W or P -> add "Phase 7 gap table"
- Rows with Verdict = ND -> add "Phase 4 accuracy scoring (ND -- excluded from denominator)"

After completing the manifest, state the bidirectional navigation check:
  Forward check: "For each manifest row, Derived Views names at least one specific downstream table by exact table name."
  Backward check: "Each downstream section (Phase 2, Phase 3, Phase 4, Phase 7) will carry [DERIVED FROM: AUDIT MANIFEST | OPERATION: ...] header naming this manifest as its source."

PHASE 0 SEAL -- format contract:
  [ ] Signal window: {date range or sprint name} -- named structural field in manifest header; not inferred from prose
  [ ] Mode: {AMEND | FRESH} -- named field present; if AMEND, {{amend}} scope carried into all phases
  [ ] Manifest rows: one row per signal artifact found; no namespace groups without individual rows
  [ ] Verdict: {C | P | W | ND} per row -- no other values, no blank
  [ ] Derived Views: non-blank per row -- names at least one downstream table by exact table name; "downstream tables" alone = incomplete; generic text = incomplete
  [ ] Forward check statement: present after manifest, confirms Derived Views naming is specific
  [ ] Backward check statement: present after manifest, confirms [DERIVED FROM] headers will appear in downstream sections
All items confirmed against format? PHASE 0 COMPLETE.

---

PHASE 1 -- ECHO
Run this phase before examining signal accuracy comparisons in Phase 3.

{{#if amend}}[AMEND: {{amend}} only -- outcomes outside this scope excluded from Echo candidacy]{{/if}}

The Echo is the single post-ship observable satisfying all three conditions:
  (a) Not predicted by any gathered signal -- not even partially
  (b) Not a named risk or acknowledged unknown at commit time
  (c) Observable only after the feature shipped

Procedure:
  Step 1: List every post-ship outcome (within AMEND scope if set).
  Step 2: Eliminate outcomes predicted by gathered signals.
  Step 3: Eliminate named risks or known unknowns.
  Step 4: Select the one with highest commit-decision impact.
  Step 5: No candidates: Echo = "No Echo -- all post-ship outcomes were within signal bounds."

| Echo (one sentence) | Nearest signal artifact | Commit relevance: HIGH / MEDIUM / LOW |
|---------------------|------------------------|--------------------------------------|
| [finding or "No Echo -- all post-ship outcomes were within signal bounds"] | [name or "none"] | [HIGH / MEDIUM / LOW or "N/A"] |

Immediately after the table:
  > **Pattern**: [name from taxonomy or "other: [your name]"] -- [description of recurring failure mode -- not Echo restatement]
  > **Why unexpected**: [prior belief contradicted -- what was expected and why reality diverged]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

LOCK: Echo table, Pattern, and Why-unexpected are final. Phases 2-9 may not change them.

PHASE 1 SEAL -- format contract:
  [ ] Echo: {one sentence} OR exact string "No Echo -- all post-ship outcomes were within signal bounds"
  [ ] Nearest signal: {artifact-filename.md} OR exact string "none"
  [ ] Commit relevance: HIGH | MEDIUM | LOW | N/A
  [ ] Pattern: "> **Pattern**: {taxonomy-label or "other: name"} -- {failure class description -- not Echo restatement}"
  [ ] Why unexpected: "> **Why unexpected**: {prior belief contradicted}"
  {{#if amend}}[ ] AMEND scope marker present immediately above table{{/if}}
All items confirmed against format? PHASE 1 COMPLETE.

---

PHASE 2 -- SIGNAL INVENTORY
[DERIVED FROM: AUDIT MANIFEST | OPERATION: group by Namespace, count rows per group, assign COVERED if count >= 1 else EMPTY]

Produce a fixed 9-row namespace coverage table. Every namespace gets exactly one row. Derive from Phase 0 AUDIT MANIFEST.

{{#if amend}}[AMEND: {{amend}} only -- out-of-scope artifacts go to the OOS table below]{{/if}}

| Namespace | Status          | Artifact count | Primary artifact (or "--") | Prediction theme (or "--") |
|-----------|-----------------|----------------|--------------------------|--------------------------|
| scout     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| draft     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| review    | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| flow      | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| trace     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| prove     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| listen    | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| program   | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| topic     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| TOTAL     |                 | N              |                          |                          |

{{#if amend}}Out-of-scope artifacts:
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside {{amend}} scope] |
If none: "No artifacts excluded -- all in scope."
{{/if}}

PHASE 2 SEAL -- format contract:
  [ ] All 9 namespace rows in exact order
  [ ] Status: {COVERED} or {EMPTY} per row
  [ ] Artifact count: {integer} per row
  [ ] Primary artifact: {filename.md} or "--"
  [ ] TOTAL row present
  {{#if amend}}[ ] OOS table present immediately after main table{{/if}}
  [ ] Derived From header: "[DERIVED FROM: AUDIT MANIFEST | OPERATION: group by Namespace...]" present above table
All items confirmed against format? PHASE 2 COMPLETE.

---

PHASE 3 -- PREDICTED VS ACTUAL
[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter rows where Namespace is COVERED; surface Prediction, Actual, Verdict per namespace]

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted (signals' collective claim post-ship) | Actual (what was observed) | Match: C / P / W / ND |
|-----------|------------------------------------------------|---------------------------|----------------------|
| [name] | [from AUDIT MANIFEST Prediction column] | [from AUDIT MANIFEST Actual column] | [from AUDIT MANIFEST Verdict column] |

C = Correct, P = Partial, W = Wrong, ND = No post-ship data yet.

PHASE 3 SEAL -- format contract:
  [ ] Row count: one per COVERED namespace -- no omissions
  [ ] Predicted: {statement} -- not blank, not "N/A"
  [ ] Actual: {statement} -- not blank, not "N/A"
  [ ] Match: C | P | W | ND
  [ ] Derived From header present above table
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed against format? PHASE 3 COMPLETE.

---

PHASE 4 -- NAMESPACE ACCURACY
[DERIVED FROM: AUDIT MANIFEST | OPERATION: count Verdict values by Namespace; exclude ND from denominator]

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Weighted score: (Cx100 + Px50) / (C+P+W) |
|-----------|---|---|---|-----|------------------------------------------|
| [name]    |   |   |   |     |                                          |
| TOTAL     |   |   |   |     |                                          |

Correct signals: {C} / {C+P+W} = X%

RECONCILIATION TABLE:
[DERIVED FROM: AUDIT MANIFEST | OPERATION: forward sequential count vs backward recovery from Verdict = W]

| Direction | Starting point | Steps | Total scored | Correct | Match? |
|-----------|---------------|-------|--------------|---------|--------|
| Forward | Manifest row 1, count each scored verdict | [+1 C, +1 W, etc.] | {N} | {C} | -- |
| Backward | W={W}; +P={P}; +C={C}; total={N} | [arithmetic shown] | {N} | C=total-W-P | YES / NO |

Reconciliation result: Forward={N}; Backward={N}; Match: YES (proceed) / NO (recheck manifest).

PHASE 4 SEAL -- format contract:
  [ ] Row count: one per Phase 3 namespace
  [ ] C, P, W, ND: {integer} per cell
  [ ] Weighted score: {number}/100 or "0 scored signals"
  [ ] TOTAL row: {number}/100
  [ ] Count ratio: "{N}/{M} = {X}%" below scoring table
  [ ] RECONCILIATION TABLE present with Forward, Backward, and result rows
  [ ] Reconciliation Match = YES before proceeding
  [ ] Derived From header present above scoring table
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed against format? PHASE 4 COMPLETE.

---

PHASE 5 -- CONFLICT AUDIT
Does any Phase 3 or Phase 4 finding suggest the locked Echo should change?

If YES: CONFLICT DETECTED / Source / Analysis / Resolution: Phase 1 Echo preserved.
If NO: "CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo."

PHASE 5 SEAL: one of two exact outputs; no Phase 1 modification.
All items confirmed? PHASE 5 COMPLETE.

---

PHASE 6 -- ACCURACY VERDICT
Draw from Phase 4 TOTAL and count ratio. Do not recalculate.
"Signal accuracy for [topic]: [TOTAL]/100 -- [STRONG/ADEQUATE/WEAK]. Count accuracy: [N/M = X%]."

PHASE 6 SEAL: verdict in exact format; both values drawn from Phase 4; tier label matches score.
All items confirmed? PHASE 6 COMPLETE.

---

PHASE 7 -- GAP ANALYSIS
[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter rows where Verdict = W or P; add material EMPTY namespaces]

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

Column A = prior belief ("We assumed X"). Column B = discovery missed. Must differ per row.

| Gap (signal type absent) | Namespace | Assumption held without evidence [A] | Skill to run | Would have surfaced [B] | Changed commit? YES / NO |
|--------------------------|-----------|--------------------------------------|-------------|-------------------------|--------------------------|
| [type] | [ns] | [prior belief -- "We assumed X"] | [/exact-skill-name] | [discovery -- distinct from A] | YES / NO |

No gaps: "No gaps -- signal coverage was sufficient for this commit decision."

  > **Recommendation**: Addresses [slot:gap-or-echo] by [slot:practice-change] so that [slot:measurable-outcome].

PHASE 7 SEAL -- format contract:
  [ ] Gap rows: every W or P namespace from Phase 3 OR "no gaps"
  [ ] Material EMPTY namespaces with rows
  [ ] Column A: "We assumed X" -- not outcome, not blank
  [ ] Column B: different from Column A per row
  [ ] Skill: {/exact-skill-name}
  [ ] Changed commit: YES | NO per row
  [ ] Slot check: no "[slot:" strings in output
  [ ] Derived From header present above gap table
  {{#if amend}}[ ] AMEND scope marker present{{/if}}
All items confirmed against format? PHASE 7 COMPLETE.

---

PHASE 8 -- CALIBRATION TREND

COPY score from Phase 6 verdict sentence. Do not recompute. Label: COPY-VERIFIED [source: Phase 6 verdict].

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [ref or "none"] | [score or "--"] | {N}/100 -- COPY-VERIFIED [source: Phase 6 verdict] | [+/-N or "--"] | up improving / down degrading / = stable |

No prior: "First retro for this topic -- this score establishes the calibration baseline."

PHASE 8 SEAL -- format contract:
  [ ] Prior retro: {topic}/{YYYY-MM-DD} or "none"; Delta: {+/-N or 0 or "--"}; Trend: one of three values or "first retro" statement

  [ ] This score -- independent verification:
      CHECK: "This score" cell non-blank, {number}/100 format.
      HOW: Read "This score" cell in Phase 8 table only. Do not read Phase 6 or Phase 4.
      Format required: {number}/100.

  [ ] COPY-VERIFIED -- independent verification:
      CHECK: Score in "This score" was copied from Phase 6, not computed.
      HOW: Open Phase 6 verdict sentence. Find score before "/100". Compare to "This score" value. "COPY-VERIFIED" label must be present. Do not read Phase 4.
      Format required: cell label contains "COPY-VERIFIED".

  [ ] COPY-SOURCE -- independent verification:
      CHECK: "This score" cell names Phase 6 verdict as source, not Phase 4.
      HOW: Read cell label. Confirm "Phase 6 verdict". Phase 4 reference or absent label = FAIL.
      Format required: label contains "source: Phase 6 verdict".

All items confirmed against format? PHASE 8 COMPLETE.

---

PHASE 9 -- ECHO -> SIGNAL DESIGN

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [exact Echo cell -- verbatim] | [exact taxonomy label -- verbatim] | [one specific practice change] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL: Echo verbatim; Pattern verbatim; change specific; change type = one of three values.
All items confirmed against format? RETRO COMPLETE.

---

Execute phases in order: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9. Verify compliance against PRE-EXECUTION CONTRACT before marking complete.

Design guarantees:
- PRE-EXECUTION CONTRACT: ASSESSOR NAVIGATION PREAMBLE (three-row structured table naming entry points 1/2/3) followed by four-column mechanism table (Mechanism / Guarantee / Verified in / Manifest column).
- Phase 0: AUDIT MANIFEST with Signal window, Mode, Verdict, Derived Views per row. Forward/backward check statements (R18-V-05 form). All downstream sections carry [DERIVED FROM: AUDIT MANIFEST] headers.
- Phase 1: Echo locked before signal comparison.
- Phase 4: Weighted score AND count ratio. RECONCILIATION TABLE required.
- Phase 8: Score COPIED from Phase 6. Three-field SEAL with independent CHECK/HOW blocks.
- All 9 seals: explicit format-string per field.
```

---

## V-03 -- Phrasing Register: Negative Control for C-44 and C-45

**Axis:** Phrasing register (single). Derived Views uses informal aliases ("coverage table", "accuracy table"). Post-manifest statements use intent descriptions rather than verification declarations. PRE-EXECUTION CONTRACT uses prose bold-paragraph entry points (R18-V-05 form, not a structured block). Tests whether these weaker forms satisfy C-44 and C-45 -- hypothesis is they do not (PARTIAL only), confirming that structural enforcement is what distinguishes the criteria.

**Hypothesis:** Informal table name aliases satisfy C-42 (columns are present) but fail C-44a (aliases "coverage table" are not exact canonical identifiers). Intent descriptions satisfy C-42 (check statements exist) but fail C-44b/c (not verification declarations). Prose entry points convey navigation information but fail C-45 (not a structured block). All three fail their respective criteria for the same reason: information is present but structural enforcement is absent. This variation scores identically to R18-V-05 on all essential/recommended criteria, providing a clean baseline for scoring the structural gap.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Execute phases in order. Each phase ends with a PHASE SEAL -- a format-contract checklist. Do not proceed past a phase until every seal item is confirmed.

{{#if amend}}AMEND SCOPE: {{amend}} -- all phases operate within this constraint only. Every table carries an explicit scope marker. Phase 2 includes an out-of-scope table.{{/if}}

---

## PRE-EXECUTION CONTRACT

Read before executing Phase 0. This retro is a bidirectional audit system navigable from three entry points:

**Entry from AUDIT MANIFEST row**: Use the `Derived Views` column to identify which downstream tables the row feeds. Navigate forward without reading phase specifications.
**Entry from downstream section**: Use the `[DERIVED FROM: AUDIT MANIFEST | OPERATION: ...]` header to navigate backward to the manifest rows that sourced the section.
**Entry from contract row**: Use the `Manifest column` field to identify the exact AUDIT MANIFEST column that will evidence fulfillment of each commitment. Navigate to the manifest before execution begins.

| Mechanism | Structural guarantee -- what is enforced and how | Verified in | Manifest column |
|-----------|------------------------------------------------|-------------|-----------------|
| Signal window | Bounding date range or sprint scope. Named structural field in manifest header. | Phase 0 SEAL item 1 | Signal window (manifest header field) |
| Mode | AMEND or FRESH flag. AMEND: scope declared top, every table scoped, Phase 2 OOS table. | Phase 0 SEAL item 2; Phase 2 SEAL item 6 if AMEND | Mode (manifest header field) |
| Echo lock | Phase 1 before signal comparison. Echo/Pattern/Why-unexpected locked. Phases 2-9 must not modify. | Phase 1 SEAL items 1-5 | Prediction (Echo is absent from this column) |
| Manifest derivation | All downstream tables derived as views of AUDIT MANIFEST. Derived Views column in manifest. [DERIVED FROM] headers in downstream sections. | Phase 0 SEAL items 3-7; [DERIVED FROM] headers | (all columns) |
| Namespace coverage | Fixed 9-row table, COVERED/EMPTY derived by grouping manifest on Namespace. | Phase 2 SEAL items 1-5 | Namespace |
| Verdict accuracy | Weighted score and count ratio required. Reconciliation cross-check required. | Phase 4 SEAL items 4-5; RECONCILIATION TABLE | Verdict |
| Gap identification | W or P manifest rows feed gap table. Material EMPTY namespaces included. | Phase 7 SEAL items 1-2 | Verdict (filter: W or P) |
| Accuracy copy | Phase 6 copies Phase 4 TOTAL. Phase 8 copies Phase 6. No recomputation. | Phase 6 SEAL; Phase 8 SEAL items 2-4 | Verdict (aggregate) |
| Gap inertia columns | Column A = prior belief; Column B = missed discovery; must not share content. | Phase 7 SEAL items 3-5 | Verdict (gap rows) |
| Recommendation slots | Three `[slot:X]` tokens; SEAL confirms no `[slot:` strings survive. | Phase 7 SEAL item 8 | (generated, not manifest-derived) |
| Copy guard | Phase 8 COPIED from Phase 6. Three-field SEAL with independent CHECK/HOW per field. | Phase 8 SEAL items 2-4 | Verdict (aggregate) |
| Seal format contracts | All 9 seals: explicit format-string per field. | All 9 SEAL blocks | (all columns) |
| AMEND scope | Every table scoped when AMEND set. Phase 2 OOS table present. | Phase 2 SEAL item 6 | (all columns) |

---

## PHASE 0 -- AUDIT MANIFEST

Before running any phase, enumerate all signal artifacts and build the AUDIT MANIFEST. All downstream tables are derived from this manifest.

Signal window: [state the date range or sprint scope]
Mode: AMEND ({{amend}}) | FRESH [circle one]

Search simulations/**/[topic]-*-*.md. For each artifact record namespace, prediction, actual, verdict, and downstream navigation.

| # | Namespace | Artifact | Prediction (signal's claim) | Actual (post-ship) | Verdict (C/P/W/ND) | Derived Views |
|---|-----------|----------|----------------------------|-------------------|-------------------|---------------|
| 1 | [ns] | [filename] | [what signal claimed] | [what was observed] | C / P / W / ND | [coverage table; predicted/actual (if non-ND); accuracy table (if non-ND); gap table (if W or P)] |
| ... | | | | | | |

Derived Views notes:
- All rows -> coverage table; accuracy table (denominator)
- Non-ND rows -> predicted/actual table
- W or P rows -> gap table

After completing the manifest:
  Navigation note: Derived Views entries name downstream tables. Downstream sections reference this manifest via [DERIVED FROM] headers.

PHASE 0 SEAL -- format contract:
  [ ] Signal window: {date range or sprint name} -- named field, not inferred from prose
  [ ] Mode: {AMEND | FRESH} -- named field present
  [ ] Manifest rows: one per signal artifact
  [ ] Verdict: {C | P | W | ND} per row
  [ ] Derived Views: non-blank per row -- names at least one downstream destination
  [ ] Navigation note: present after manifest
All items confirmed against format? PHASE 0 COMPLETE.

---

PHASE 1 -- ECHO
Run this phase before examining signal accuracy comparisons.

{{#if amend}}[AMEND: {{amend}} only -- outcomes outside this scope excluded from Echo candidacy]{{/if}}

The Echo is the single post-ship observable satisfying all three conditions:
  (a) Not predicted by any gathered signal -- not even partially
  (b) Not a named risk or acknowledged unknown at commit time
  (c) Observable only after the feature shipped

Procedure:
  Step 1: List every post-ship outcome (within AMEND scope if set).
  Step 2: Eliminate outcomes predicted by gathered signals.
  Step 3: Eliminate named risks or known unknowns.
  Step 4: Select the one with highest commit-decision impact.
  Step 5: No candidates: Echo = "No Echo -- all post-ship outcomes were within signal bounds."

| Echo (one sentence) | Nearest signal artifact | Commit relevance: HIGH / MEDIUM / LOW |
|---------------------|------------------------|--------------------------------------|
| [finding or "No Echo -- all post-ship outcomes were within signal bounds"] | [name or "none"] | [HIGH / MEDIUM / LOW or "N/A"] |

  > **Pattern**: [taxonomy label] -- [failure class description -- not Echo restatement]
  > **Why unexpected**: [prior belief contradicted -- what was expected and why reality diverged]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

LOCK: Echo table, Pattern, and Why-unexpected are final.

PHASE 1 SEAL -- format contract:
  [ ] Echo: {one sentence} OR "No Echo -- all post-ship outcomes were within signal bounds"
  [ ] Nearest signal: {filename.md} OR "none"
  [ ] Commit relevance: HIGH | MEDIUM | LOW | N/A
  [ ] Pattern: "> **Pattern**: {label} -- {failure class description}"
  [ ] Why unexpected: "> **Why unexpected**: {prior belief contradicted}"
  {{#if amend}}[ ] AMEND scope marker present above table{{/if}}
All items confirmed against format? PHASE 1 COMPLETE.

---

PHASE 2 -- SIGNAL INVENTORY
[DERIVED FROM: AUDIT MANIFEST | OPERATION: group by Namespace, count rows, assign COVERED if count >= 1 else EMPTY]

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Status          | Artifact count | Primary artifact (or "--") | Prediction theme (or "--") |
|-----------|-----------------|----------------|--------------------------|--------------------------|
| scout     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| draft     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| review    | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| flow      | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| trace     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| prove     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| listen    | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| program   | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| topic     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| TOTAL     |                 | N              |                          |                          |

{{#if amend}}OOS artifacts: table or "No artifacts excluded -- all in scope."{{/if}}

PHASE 2 SEAL:
  [ ] All 9 namespace rows in exact order
  [ ] Status: COVERED or EMPTY per row
  [ ] Artifact count: {integer}
  [ ] Primary artifact: {filename.md} or "--"
  [ ] TOTAL row present
  {{#if amend}}[ ] OOS table present{{/if}}
  [ ] Derived From header present above table
All items confirmed? PHASE 2 COMPLETE.

---

PHASE 3 -- PREDICTED VS ACTUAL
[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter COVERED namespaces]

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted | Actual | Match: C / P / W / ND |
|-----------|-----------|--------|----------------------|
| [name] | [from AUDIT MANIFEST] | [from AUDIT MANIFEST] | [from AUDIT MANIFEST] |

PHASE 3 SEAL:
  [ ] One row per COVERED namespace
  [ ] Predicted: {statement} -- not blank
  [ ] Actual: {statement} -- not blank
  [ ] Match: C | P | W | ND
  [ ] Derived From header present
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed? PHASE 3 COMPLETE.

---

PHASE 4 -- NAMESPACE ACCURACY
[DERIVED FROM: AUDIT MANIFEST | OPERATION: count Verdict values by Namespace; exclude ND from denominator]

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Weighted score: (Cx100 + Px50) / (C+P+W) |
|-----------|---|---|---|-----|------------------------------------------|
| [name]    |   |   |   |     |                                          |
| TOTAL     |   |   |   |     |                                          |

Correct signals: {C} / {C+P+W} = X%

RECONCILIATION TABLE:
[DERIVED FROM: AUDIT MANIFEST | OPERATION: forward sequential count vs backward recovery from Verdict = W]

| Direction | Starting point | Steps | Total scored | Correct | Match? |
|-----------|---------------|-------|--------------|---------|--------|
| Forward | Row 1 sequentially | [+1 C, etc.] | {N} | {C} | -- |
| Backward | W={W}; +P={P}; +C={C}; total={N} | [shown] | {N} | {C} | YES / NO |

Reconciliation result: Match = YES / NO.

PHASE 4 SEAL:
  [ ] One row per Phase 3 namespace
  [ ] C, P, W, ND: {integer}
  [ ] Weighted score: {number}/100 or "0 scored signals"
  [ ] TOTAL row: {number}/100
  [ ] Count ratio: "{N}/{M} = {X}%"
  [ ] RECONCILIATION TABLE present; Match = YES before proceeding
  [ ] Derived From header present
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed? PHASE 4 COMPLETE.

---

PHASE 5 -- CONFLICT AUDIT
Does any Phase 3/Phase 4 finding suggest the locked Echo should change?
If YES: CONFLICT DETECTED / Source / Analysis / Resolution.
If NO: "CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo."
PHASE 5 SEAL: one of two outputs; no Phase 1 modification.

---

PHASE 6 -- ACCURACY VERDICT
"Signal accuracy for [topic]: [TOTAL]/100 -- [STRONG/ADEQUATE/WEAK]. Count accuracy: [N/M = X%]."
PHASE 6 SEAL: exact format; both values from Phase 4; tier label matches score.

---

PHASE 7 -- GAP ANALYSIS
[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter W or P rows; add material EMPTY namespaces]

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

Column A = prior belief ("We assumed X"). Column B = discovery missed. Must differ per row.

| Gap | Namespace | Assumption [A] | Skill | Would have surfaced [B] | Changed commit? |
|-----|-----------|---------------|-------|------------------------|----------------|
| [type] | [ns] | [prior belief] | [/skill] | [discovery] | YES / NO |

No gaps: "No gaps -- signal coverage was sufficient for this commit decision."
  > **Recommendation**: Addresses [slot:gap-or-echo] by [slot:practice-change] so that [slot:measurable-outcome].

PHASE 7 SEAL:
  [ ] Gap rows: W/P namespaces OR "no gaps"
  [ ] Material EMPTY namespaces included
  [ ] Column A: "We assumed X"
  [ ] Column B: different from A
  [ ] Skill: {/exact-skill-name}
  [ ] Changed commit: YES | NO
  [ ] Slot check: no "[slot:" strings
  [ ] Derived From header present
  {{#if amend}}[ ] AMEND scope marker present{{/if}}
All items confirmed? PHASE 7 COMPLETE.

---

PHASE 8 -- CALIBRATION TREND
COPY from Phase 6. Label: COPY-VERIFIED [source: Phase 6 verdict].

| Prior retro | Prior score | This score | Delta | Trend |
|-------------|-------------|------------|-------|-------|
| [ref or "none"] | [score or "--"] | {N}/100 -- COPY-VERIFIED [source: Phase 6 verdict] | [delta or "--"] | up improving / down degrading / = stable |

PHASE 8 SEAL:
  [ ] Prior: {topic}/{date} or "none"; Delta: {+/-N or "--"}; Trend stated
  [ ] This score (independent): CHECK cell is {number}/100; HOW: read cell only
  [ ] COPY-VERIFIED (independent): CHECK copied from Phase 6; HOW: compare to Phase 6 sentence; label contains "COPY-VERIFIED"
  [ ] COPY-SOURCE (independent): CHECK names Phase 6, not Phase 4; HOW: read label; confirm "Phase 6 verdict"
All items confirmed? PHASE 8 COMPLETE.

---

PHASE 9 -- ECHO -> SIGNAL DESIGN

| Echo (verbatim) | Pattern (verbatim) | Proposed change | Change type |
|-----------------|--------------------|----------------|-------------|
| [Phase 1 Echo verbatim] | [Phase 1 taxonomy label verbatim] | [specific change] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL: Echo verbatim; Pattern verbatim; change specific; change type one of three values.
All items confirmed? RETRO COMPLETE.

---

Execute phases in order: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9.
```

---

## V-04 -- `Derived Views` Canonical Names + VERIFIED Declarations + Navigation Preamble: C-44 + C-45 Combined

**Axis:** C-44 + C-45 combined. Phase 0 uses canonical table identifiers and FORWARD/BACKWARD VERIFIED declarations (V-01 mechanism). PRE-EXECUTION CONTRACT gains ASSESSOR NAVIGATION PREAMBLE structured table (V-02 mechanism). Zero-interference test: C-44 lives in Phase 0 SEAL; C-45 lives in the PRE-EXECUTION CONTRACT preamble; no shared modification surface.

**Hypothesis:** C-44 and C-45 target independent structural locations with no overlap -- Phase 0 SEAL items vs PRE-EXECUTION CONTRACT preamble. Adding both simultaneously should produce PASS on both without any interference between the mechanisms. The canonical table names in Derived Views are not referenced by the preamble, so neither mechanism constrains the other.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Execute phases in order. Each phase ends with a PHASE SEAL -- a format-contract checklist where every item specifies the required field and its required value form. Do not proceed past a phase until every seal item is confirmed.

{{#if amend}}AMEND SCOPE: {{amend}} -- all phases operate within this constraint only. Every table carries an explicit scope marker. Phase 2 includes an out-of-scope table.{{/if}}

---

## PRE-EXECUTION CONTRACT

Read before executing Phase 0.

### ASSESSOR NAVIGATION PREAMBLE

This audit system supports three entry points. No prior knowledge of the architecture is required. Locate the row matching your starting position and follow the navigation field.

| # | If you are starting at... | Locate this navigation field | It takes you to... |
|---|--------------------------|-----------------------------|--------------------|
| 1 | Any row in this PRE-EXECUTION CONTRACT | `Manifest column` field (4th column of this table) | The exact AUDIT MANIFEST column that evidences the commitment in that row |
| 2 | Any row in the AUDIT MANIFEST (Phase 0) | `Derived Views` column (last column of the Phase 0 table) | The exact downstream table(s) that receive data from that manifest row |
| 3 | Any downstream section header (Phase 2, Phase 3, Phase 4, Phase 7) | `[DERIVED FROM: AUDIT MANIFEST \| OPERATION: ...]` declaration in the section header | The AUDIT MANIFEST as the data source for that section |

A completed retro is auditable from any of these three positions without reading the full document in sequence.

| Mechanism | Structural guarantee -- what is enforced and how | Verified in | Manifest column |
|-----------|------------------------------------------------|-------------|-----------------|
| Signal window | Bounding date range or sprint scope. Named structural field in manifest header -- not inferred from prose. | Phase 0 SEAL item 1 | Signal window (manifest header field) |
| Mode | AMEND or FRESH flag. AMEND: scope declared top, every table scoped, Phase 2 OOS table. | Phase 0 SEAL item 2; Phase 2 SEAL item 6 if AMEND | Mode (manifest header field) |
| Echo lock | Phase 1 before signal comparison. Echo/Pattern/Why-unexpected locked. Phases 2-9 must not modify. | Phase 1 SEAL items 1-5 | Prediction (Echo is the finding absent from this column) |
| Manifest derivation | All downstream tables derived as views of AUDIT MANIFEST. Derived Views column present in manifest; canonical table names required. FORWARD VERIFIED + BACKWARD VERIFIED declarations required after manifest. | Phase 0 SEAL items 3-7; [DERIVED FROM] headers in all downstream sections | (all columns -- manifest is the derivation source) |
| Namespace coverage | Fixed 9-row table, COVERED/EMPTY derived by grouping manifest Namespace column. | Phase 2 SEAL items 1-5 | Namespace |
| Verdict accuracy | Weighted score and count ratio required. Reconciliation cross-check required. | Phase 4 SEAL items 4-5; RECONCILIATION TABLE | Verdict |
| Gap identification | W or P manifest rows feed gap table. Material EMPTY namespaces included. | Phase 7 SEAL items 1-2 | Verdict (filter: W or P) |
| Accuracy copy | Phase 6 copies Phase 4 TOTAL. Phase 8 copies Phase 6 verdict sentence. No recomputation at any stage. | Phase 6 SEAL; Phase 8 SEAL items 2-4 | Verdict (aggregate: TOTAL weighted score) |
| Gap inertia columns | Column A = prior belief; Column B = missed discovery; must not share content per row. | Phase 7 SEAL items 3-5 | Verdict (gap rows) |
| Recommendation slots | Three `[slot:X]` tokens; SEAL confirms no `[slot:` strings survive. | Phase 7 SEAL item 8 | (generated, not manifest-derived) |
| Copy guard | Phase 8 COPIED from Phase 6. Three-field SEAL: This score / COPY-VERIFIED / COPY-SOURCE each with independent CHECK/HOW. | Phase 8 SEAL items 2-4 | Verdict (aggregate) |
| Seal format contracts | All 9 seals: explicit format-string per field; verify value form, not just presence. | All 9 SEAL blocks | (all columns) |
| AMEND scope | Every table has scope marker when AMEND set. Phase 2 OOS table present. | Phase 2 SEAL item 6 | (all columns -- scope filter applied to all manifest rows) |

---

## PHASE 0 -- AUDIT MANIFEST

Before running any phase, enumerate all signal artifacts and build the AUDIT MANIFEST. All downstream tables are derived from this manifest. The `Derived Views` column enables forward navigation: use the canonical table identifiers below so an assessor can navigate directly to the named downstream artifact.

Signal window: [state the date range or sprint scope bounding the predictions being evaluated]
Mode: AMEND ({{amend}}) | FRESH [circle one]

Search simulations/**/[topic]-*-*.md. For each artifact record namespace, prediction, actual outcome, verdict, and forward-navigation destinations using canonical table names only.

| # | Namespace | Artifact | Prediction (signal's claim) | Actual (post-ship) | Verdict (C/P/W/ND) | Derived Views |
|---|-----------|----------|----------------------------|-------------------|-------------------|---------------|
| 1 | [ns] | [filename] | [what signal claimed would happen] | [what was observed post-ship] | C / P / W / ND | [Phase 2 Signal Coverage Table; Phase 3 Predicted vs Actual Table (if non-ND); Phase 4 Namespace Accuracy Table (if non-ND); Phase 4 Reconciliation Table; Phase 7 Gap Analysis Table (if W or P)] |
| ... | | | | | | |

Canonical Derived Views assignment rules (use these exact table names):
- Every row -> "Phase 2 Signal Coverage Table"
- Rows with non-ND verdict -> add "Phase 3 Predicted vs Actual Table; Phase 4 Namespace Accuracy Table"
- Rows with Verdict = W -> add "Phase 7 Gap Analysis Table"
- Rows with Verdict = P -> add "Phase 7 Gap Analysis Table"
- Every row -> add "Phase 4 Reconciliation Table" (ND rows excluded from denominator but appear in Reconciliation)

After completing the manifest, write the bidirectional navigation verification block:

  FORWARD VERIFIED: Manifest -> downstream direction confirmed. Each manifest row's Derived Views column names downstream tables using canonical identifiers from the set {Phase 2 Signal Coverage Table, Phase 3 Predicted vs Actual Table, Phase 4 Namespace Accuracy Table, Phase 4 Reconciliation Table, Phase 7 Gap Analysis Table}. An assessor reading any manifest row can navigate forward to downstream sections without reading phase specifications. Forward navigation confirmed complete.

  BACKWARD VERIFIED: Downstream -> manifest direction confirmed. Each downstream section -- Phase 2 Signal Coverage Table, Phase 3 Predicted vs Actual Table, Phase 4 Namespace Accuracy Table, Phase 4 Reconciliation Table, Phase 7 Gap Analysis Table -- carries a [DERIVED FROM: AUDIT MANIFEST | OPERATION: ...] header that names this manifest as its source. An assessor reading any downstream section can navigate backward to the manifest. Backward navigation confirmed complete.

PHASE 0 SEAL -- format contract:
  [ ] Signal window: {date range or sprint name} -- named structural field; not inferred from prose
  [ ] Mode: {AMEND | FRESH} -- named field present; if AMEND, {{amend}} scope carried into all phases
  [ ] Manifest rows: one per signal artifact; no namespace groups without individual rows
  [ ] Verdict: {C | P | W | ND} per row -- no other values, no blank
  [ ] Derived Views exact canonical names: each entry uses a name from the canonical set exactly -- "Phase 2 Signal Coverage Table" not "Phase 2 table" or "Phase 2 coverage table"; non-canonical alias = FAIL this item
  [ ] FORWARD VERIFIED declaration: statement beginning with "FORWARD VERIFIED:" present after manifest table; explicitly declares manifest -> downstream direction as confirmed; intent description without verification assertion = FAIL
  [ ] BACKWARD VERIFIED declaration: statement beginning with "BACKWARD VERIFIED:" present after manifest table; explicitly declares downstream -> manifest direction as confirmed; future-tense statement without verification assertion = FAIL
All items confirmed against format? PHASE 0 COMPLETE.

---

PHASE 1 -- ECHO
Run this phase before examining signal accuracy comparisons in Phase 3.

{{#if amend}}[AMEND: {{amend}} only -- outcomes outside this scope excluded from Echo candidacy]{{/if}}

The Echo is the single post-ship observable satisfying all three conditions:
  (a) Not predicted by any gathered signal -- not even partially
  (b) Not a named risk or acknowledged unknown at commit time
  (c) Observable only after the feature shipped

Procedure:
  Step 1: List every post-ship outcome (within AMEND scope if set).
  Step 2: Eliminate outcomes predicted by gathered signals.
  Step 3: Eliminate named risks or known unknowns.
  Step 4: Select the one with highest commit-decision impact.
  Step 5: No candidates: Echo = "No Echo -- all post-ship outcomes were within signal bounds."

| Echo (one sentence) | Nearest signal artifact | Commit relevance: HIGH / MEDIUM / LOW |
|---------------------|------------------------|--------------------------------------|
| [finding or "No Echo -- all post-ship outcomes were within signal bounds"] | [name or "none"] | [HIGH / MEDIUM / LOW or "N/A"] |

  > **Pattern**: [taxonomy label or "other: name"] -- [failure class description -- not Echo restatement]
  > **Why unexpected**: [prior belief contradicted -- what was expected and why reality diverged]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

LOCK: Echo table, Pattern, and Why-unexpected are final. Phases 2-9 may not change them.

PHASE 1 SEAL -- format contract:
  [ ] Echo: {one sentence} OR "No Echo -- all post-ship outcomes were within signal bounds"
  [ ] Nearest signal: {filename.md} OR "none"
  [ ] Commit relevance: HIGH | MEDIUM | LOW | N/A
  [ ] Pattern: "> **Pattern**: {label} -- {failure class description, not Echo restatement}"
  [ ] Why unexpected: "> **Why unexpected**: {prior belief contradicted}"
  {{#if amend}}[ ] AMEND scope marker present above table{{/if}}
All items confirmed against format? PHASE 1 COMPLETE.

---

PHASE 2 -- SIGNAL INVENTORY
[DERIVED FROM: AUDIT MANIFEST | OPERATION: group by Namespace, count rows per group, assign COVERED if count >= 1 else EMPTY]

Produce a fixed 9-row namespace coverage table. Derive from Phase 0 AUDIT MANIFEST.

{{#if amend}}[AMEND: {{amend}} only -- out-of-scope artifacts go to OOS table below]{{/if}}

| Namespace | Status          | Artifact count | Primary artifact (or "--") | Prediction theme (or "--") |
|-----------|-----------------|----------------|--------------------------|--------------------------|
| scout     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| draft     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| review    | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| flow      | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| trace     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| prove     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| listen    | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| program   | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| topic     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| TOTAL     |                 | N              |                          |                          |

{{#if amend}}Out-of-scope artifacts:
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside {{amend}} scope] |
If none: "No artifacts excluded -- all in scope."
{{/if}}

PHASE 2 SEAL -- format contract:
  [ ] All 9 namespace rows in exact order: scout, draft, review, flow, trace, prove, listen, program, topic
  [ ] Status: {COVERED} or {EMPTY} per row
  [ ] Artifact count: {integer} per row
  [ ] Primary artifact: {filename.md} or "--"
  [ ] TOTAL row present
  {{#if amend}}[ ] OOS table present immediately after main table{{/if}}
  [ ] Derived From header: "[DERIVED FROM: AUDIT MANIFEST | OPERATION: group by Namespace...]" present above table
All items confirmed against format? PHASE 2 COMPLETE.

---

PHASE 3 -- PREDICTED VS ACTUAL
[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter rows where Namespace is COVERED; surface Prediction, Actual, Verdict per namespace]

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted (signals' collective claim post-ship) | Actual (what was observed) | Match: C / P / W / ND |
|-----------|------------------------------------------------|---------------------------|----------------------|
| [name] | [from AUDIT MANIFEST Prediction column] | [from AUDIT MANIFEST Actual column] | [from AUDIT MANIFEST Verdict column] |

PHASE 3 SEAL -- format contract:
  [ ] Row count: one per COVERED namespace from Phase 2
  [ ] Predicted: {statement} -- not blank, not "N/A"
  [ ] Actual: {statement} -- not blank, not "N/A"
  [ ] Match: C | P | W | ND
  [ ] Derived From header present above table
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed against format? PHASE 3 COMPLETE.

---

PHASE 4 -- NAMESPACE ACCURACY
[DERIVED FROM: AUDIT MANIFEST | OPERATION: count Verdict values by Namespace; exclude ND from denominator]

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Weighted score: (Cx100 + Px50) / (C+P+W) |
|-----------|---|---|---|-----|------------------------------------------|
| [name]    |   |   |   |     |                                          |
| TOTAL     |   |   |   |     |                                          |

Correct signals: {C} / {C+P+W} = X%

RECONCILIATION TABLE:
[DERIVED FROM: AUDIT MANIFEST | OPERATION: forward sequential count vs backward recovery from Verdict = W]

| Direction | Starting point | Steps | Total scored | Correct | Match? |
|-----------|---------------|-------|--------------|---------|--------|
| Forward | Manifest row 1, count each scored verdict sequentially | [+1 C, +1 W, etc.] | {N} | {C} | -- |
| Backward | W={W}; +P={P}; +C={C}; total={N} | [arithmetic shown] | {N} | C=total-W-P | YES / NO |

Reconciliation result: Forward={N}; Backward={N}; Match: YES (proceed) / NO (recheck manifest).

PHASE 4 SEAL -- format contract:
  [ ] Row count: one per Phase 3 namespace
  [ ] C, P, W, ND: {integer} per cell
  [ ] Weighted score: {number}/100 or "0 scored signals"
  [ ] TOTAL row: {number}/100
  [ ] Count ratio: "{N}/{M} = {X}%" below scoring table
  [ ] RECONCILIATION TABLE present with Forward, Backward, and result rows
  [ ] Reconciliation Match = YES before proceeding
  [ ] Derived From header present above scoring table
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed against format? PHASE 4 COMPLETE.

---

PHASE 5 -- CONFLICT AUDIT
Does any Phase 3 or Phase 4 finding suggest the locked Echo should change?
If YES: CONFLICT DETECTED / Source / Analysis / Resolution: Phase 1 Echo preserved.
If NO: "CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo."
PHASE 5 SEAL: one of two exact outputs; no Phase 1 modification.
All items confirmed? PHASE 5 COMPLETE.

---

PHASE 6 -- ACCURACY VERDICT
Draw from Phase 4 TOTAL and count ratio. Do not recalculate.
"Signal accuracy for [topic]: [TOTAL]/100 -- [STRONG/ADEQUATE/WEAK]. Count accuracy: [N/M = X%]."
PHASE 6 SEAL: exact format; both values from Phase 4; tier label matches score.
All items confirmed? PHASE 6 COMPLETE.

---

PHASE 7 -- GAP ANALYSIS
[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter rows where Verdict = W or P; add material EMPTY namespaces]

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

Column A = prior belief ("We assumed X"). Column B = discovery missed. Must differ per row.

| Gap (signal type absent) | Namespace | Assumption held without evidence [A] | Skill to run | Would have surfaced [B] | Changed commit? YES / NO |
|--------------------------|-----------|--------------------------------------|-------------|-------------------------|--------------------------|
| [type] | [ns] | [prior belief -- "We assumed X"] | [/exact-skill-name] | [discovery -- distinct from A] | YES / NO |

No gaps: "No gaps -- signal coverage was sufficient for this commit decision."

  > **Recommendation**: Addresses [slot:gap-or-echo] by [slot:practice-change] so that [slot:measurable-outcome].

PHASE 7 SEAL -- format contract:
  [ ] Gap rows: every W or P namespace from Phase 3 OR "no gaps"
  [ ] Material EMPTY namespaces with rows
  [ ] Column A: "We assumed X" -- not outcome, not blank
  [ ] Column B: different from Column A per row
  [ ] Skill: {/exact-skill-name}
  [ ] Changed commit: YES | NO per row
  [ ] Slot check: no "[slot:" strings in output
  [ ] Derived From header present above gap table
  {{#if amend}}[ ] AMEND scope marker present{{/if}}
All items confirmed against format? PHASE 7 COMPLETE.

---

PHASE 8 -- CALIBRATION TREND

COPY score from Phase 6 verdict sentence. Do not recompute. Label: COPY-VERIFIED [source: Phase 6 verdict].

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [ref or "none"] | [score or "--"] | {N}/100 -- COPY-VERIFIED [source: Phase 6 verdict] | [+/-N or "--"] | up improving / down degrading / = stable |

No prior: "First retro for this topic -- this score establishes the calibration baseline."

PHASE 8 SEAL -- format contract:
  [ ] Prior retro: {topic}/{YYYY-MM-DD} or "none"; Delta: {+/-N or 0 or "--"}; Trend: one of three values or "first retro" statement

  [ ] This score -- independent verification:
      CHECK: "This score" cell non-blank, {number}/100 format.
      HOW: Read "This score" cell in Phase 8 table only. Do not read Phase 6 or Phase 4.
      Format required: {number}/100.

  [ ] COPY-VERIFIED -- independent verification:
      CHECK: Score copied from Phase 6, not computed.
      HOW: Open Phase 6 verdict sentence. Find score before "/100". Compare to "This score" value. "COPY-VERIFIED" label must be present. Do not read Phase 4.
      Format required: cell label contains "COPY-VERIFIED".

  [ ] COPY-SOURCE -- independent verification:
      CHECK: "This score" cell names Phase 6 verdict as source, not Phase 4.
      HOW: Read cell label. Confirm "Phase 6 verdict". Phase 4 reference or absent label = FAIL.
      Format required: label contains "source: Phase 6 verdict".

All items confirmed against format? PHASE 8 COMPLETE.

---

PHASE 9 -- ECHO -> SIGNAL DESIGN

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [exact Phase 1 Echo cell -- verbatim] | [exact Phase 1 taxonomy label -- verbatim] | [one specific practice change] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL: Echo verbatim; Pattern verbatim; change specific; change type = one of three values.
All items confirmed against format? RETRO COMPLETE.

---

Execute phases in order: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9. Verify compliance against PRE-EXECUTION CONTRACT before marking complete.

Design guarantees:
- PRE-EXECUTION CONTRACT: ASSESSOR NAVIGATION PREAMBLE (three-row structured table) followed by four-column mechanism table (Mechanism / Guarantee / Verified in / Manifest column).
- Phase 0: AUDIT MANIFEST with Signal window, Mode, Verdict per row, Derived Views per row using canonical table names. FORWARD VERIFIED and BACKWARD VERIFIED declarations required after manifest. All downstream sections carry [DERIVED FROM: AUDIT MANIFEST] headers.
- Phase 1: Echo locked before signal comparison.
- Phase 4: Weighted score AND count ratio. RECONCILIATION TABLE required.
- Phase 8: Score COPIED from Phase 6. Three-field SEAL with independent CHECK/HOW blocks.
- All 9 seals: explicit format-string per field.
```

---

## V-05 -- Full Integration: C-44 + C-45 + Preamble/SEAL Cross-Reference

**Axis:** Full integration. Adds V-04 mechanisms (canonical names, VERIFIED declarations, ASSESSOR NAVIGATION PREAMBLE), plus cross-reference enforcement: (1) the ASSESSOR NAVIGATION PREAMBLE's entry point 2 explicitly names the canonical table set, making the preamble the single declared source of truth; (2) the FORWARD/BACKWARD VERIFIED declarations reference "per canonical table names declared in ASSESSOR NAVIGATION PREAMBLE entry point 2"; (3) Phase 0 SEAL adds a cross-check item verifying Derived Views names match the preamble's declared canonical set. This closes the drift gap: if a Derived Views entry uses a non-canonical alias, the SEAL's cross-check item catches it; if the preamble's canonical set drifts, the VERIFIED declarations that reference it become incorrect.

**Hypothesis:** V-04 satisfies C-44 and C-45 independently. V-05 makes them mutually reinforcing: the preamble's canonical table list is the authority that both the SEAL and VERIFIED declarations cite. An assessor starting from the preamble sees the canonical set; an assessor checking a VERIFIED declaration traces it to the preamble; a scorer checking the SEAL finds the cross-reference item. The three mechanisms converge on the same authority rather than providing parallel but disconnected assertions. This is the highest structural integrity achievable -- neither mechanism can degrade without the other catching it.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Execute phases in order. Each phase ends with a PHASE SEAL -- a format-contract checklist where every item specifies the required field and its required value form. Do not proceed past a phase until every seal item is confirmed.

{{#if amend}}AMEND SCOPE: {{amend}} -- all phases operate within this constraint only. Every table carries an explicit scope marker. Phase 2 includes an out-of-scope table.{{/if}}

---

## PRE-EXECUTION CONTRACT

Read before executing Phase 0.

### ASSESSOR NAVIGATION PREAMBLE

This audit system supports three entry points. No prior knowledge of the architecture is required. Use the table below to enter from any starting position.

| # | If you are starting at... | Locate this navigation field | It takes you to... |
|---|--------------------------|-----------------------------|--------------------|
| 1 | Any row in this PRE-EXECUTION CONTRACT | `Manifest column` field (4th column of this table) | The exact AUDIT MANIFEST column that evidences the commitment in that row |
| 2 | Any row in the AUDIT MANIFEST (Phase 0) | `Derived Views` column (last column of the Phase 0 table) | One of the five canonical downstream tables: Phase 2 Signal Coverage Table \| Phase 3 Predicted vs Actual Table \| Phase 4 Namespace Accuracy Table \| Phase 4 Reconciliation Table \| Phase 7 Gap Analysis Table |
| 3 | Any downstream section header (Phase 2, Phase 3, Phase 4, Phase 7) | `[DERIVED FROM: AUDIT MANIFEST \| OPERATION: ...]` declaration in the section header | The AUDIT MANIFEST as the data source for that section |

**Canonical downstream table set** (declared here; Phase 0 Derived Views column must use these exact identifiers; Phase 0 SEAL cross-checks against this set):
1. Phase 2 Signal Coverage Table
2. Phase 3 Predicted vs Actual Table
3. Phase 4 Namespace Accuracy Table
4. Phase 4 Reconciliation Table
5. Phase 7 Gap Analysis Table

| Mechanism | Structural guarantee -- what is enforced and how | Verified in | Manifest column |
|-----------|------------------------------------------------|-------------|-----------------|
| Signal window | Bounding date range or sprint scope. Named structural field in manifest header -- not inferred from prose. | Phase 0 SEAL item 1 | Signal window (manifest header field) |
| Mode | AMEND or FRESH flag. AMEND: scope declared top, every table scoped, Phase 2 OOS table. | Phase 0 SEAL item 2; Phase 2 SEAL item 6 if AMEND | Mode (manifest header field) |
| Echo lock | Phase 1 before signal comparison. Echo/Pattern/Why-unexpected locked. Phases 2-9 must not modify. | Phase 1 SEAL items 1-5 | Prediction (Echo is the finding absent from this column) |
| Manifest derivation | All downstream tables derived as views of AUDIT MANIFEST. Derived Views column in manifest uses canonical table names from ASSESSOR NAVIGATION PREAMBLE entry point 2. FORWARD VERIFIED + BACKWARD VERIFIED declarations required. | Phase 0 SEAL items 3-8; [DERIVED FROM] headers in all downstream sections | (all columns -- manifest is the derivation source) |
| Namespace coverage | Fixed 9-row table, COVERED/EMPTY derived by grouping manifest Namespace column. | Phase 2 SEAL items 1-5 | Namespace |
| Verdict accuracy | Weighted score and count ratio required. Reconciliation cross-check required. | Phase 4 SEAL items 4-5; RECONCILIATION TABLE | Verdict |
| Gap identification | W or P manifest rows feed gap table. Material EMPTY namespaces included. | Phase 7 SEAL items 1-2 | Verdict (filter: W or P) |
| Accuracy copy | Phase 6 copies Phase 4 TOTAL. Phase 8 copies Phase 6 verdict sentence. No recomputation at any stage. | Phase 6 SEAL; Phase 8 SEAL items 2-4 | Verdict (aggregate: TOTAL weighted score) |
| Gap inertia columns | Column A = prior belief; Column B = missed discovery; must not share content per row. | Phase 7 SEAL items 3-5 | Verdict (gap rows) |
| Recommendation slots | Three `[slot:X]` tokens; SEAL confirms no `[slot:` strings survive. | Phase 7 SEAL item 8 | (generated, not manifest-derived) |
| Copy guard | Phase 8 COPIED from Phase 6. Three-field SEAL: This score / COPY-VERIFIED / COPY-SOURCE each with independent CHECK/HOW. | Phase 8 SEAL items 2-4 | Verdict (aggregate) |
| Seal format contracts | All 9 seals: explicit format-string per field; verify value form, not just presence. | All 9 SEAL blocks | (all columns) |
| AMEND scope | Every table has scope marker when AMEND set. Phase 2 OOS table present. | Phase 2 SEAL item 6 | (all columns) |

---

## PHASE 0 -- AUDIT MANIFEST

Before running any phase, enumerate all signal artifacts and build the AUDIT MANIFEST. All downstream tables are derived from this manifest. The `Derived Views` column enables forward navigation using the canonical table names declared in ASSESSOR NAVIGATION PREAMBLE entry point 2 -- use those exact identifiers; no aliases.

Signal window: [state the date range or sprint scope bounding the predictions being evaluated]
Mode: AMEND ({{amend}}) | FRESH [circle one]

Search simulations/**/[topic]-*-*.md. For each artifact record namespace, prediction, actual outcome, verdict, and forward-navigation destinations using canonical table names from ASSESSOR NAVIGATION PREAMBLE entry point 2 only.

| # | Namespace | Artifact | Prediction (signal's claim) | Actual (post-ship) | Verdict (C/P/W/ND) | Derived Views |
|---|-----------|----------|----------------------------|-------------------|-------------------|---------------|
| 1 | [ns] | [filename] | [what signal claimed would happen] | [what was observed post-ship] | C / P / W / ND | [Phase 2 Signal Coverage Table; Phase 3 Predicted vs Actual Table (if non-ND); Phase 4 Namespace Accuracy Table (if non-ND); Phase 4 Reconciliation Table; Phase 7 Gap Analysis Table (if W or P)] |
| ... | | | | | | |

Derived Views assignment rules (use canonical names from ASSESSOR NAVIGATION PREAMBLE entry point 2):
- Every row -> "Phase 2 Signal Coverage Table"
- Rows with non-ND verdict -> add "Phase 3 Predicted vs Actual Table; Phase 4 Namespace Accuracy Table"
- Rows with Verdict = W -> add "Phase 7 Gap Analysis Table"
- Rows with Verdict = P -> add "Phase 7 Gap Analysis Table"
- Every row -> add "Phase 4 Reconciliation Table" (ND rows excluded from denominator but appear in Reconciliation)

After completing the manifest, write the bidirectional navigation verification block, referencing the canonical table set from ASSESSOR NAVIGATION PREAMBLE entry point 2:

  FORWARD VERIFIED: Manifest -> downstream direction confirmed. Each manifest row's Derived Views column names downstream tables using canonical identifiers declared in ASSESSOR NAVIGATION PREAMBLE entry point 2: {Phase 2 Signal Coverage Table, Phase 3 Predicted vs Actual Table, Phase 4 Namespace Accuracy Table, Phase 4 Reconciliation Table, Phase 7 Gap Analysis Table}. An assessor reading any manifest row can navigate forward to the named downstream artifact without reading phase specifications. Forward navigation confirmed complete.

  BACKWARD VERIFIED: Downstream -> manifest direction confirmed. Each canonical downstream table -- Phase 2 Signal Coverage Table, Phase 3 Predicted vs Actual Table, Phase 4 Namespace Accuracy Table, Phase 4 Reconciliation Table, Phase 7 Gap Analysis Table -- carries a [DERIVED FROM: AUDIT MANIFEST | OPERATION: ...] header naming this manifest as its source. An assessor at any downstream section can navigate backward to the manifest. Backward navigation confirmed complete.

PHASE 0 SEAL -- format contract:
  [ ] Signal window: {date range or sprint name} -- named structural field; not inferred from prose
  [ ] Mode: {AMEND | FRESH} -- named field present; if AMEND, {{amend}} scope carried into all phases
  [ ] Manifest rows: one per signal artifact; no namespace groups without individual rows
  [ ] Verdict: {C | P | W | ND} per row -- no other values, no blank
  [ ] Derived Views exact canonical names: each entry uses a name from the canonical set -- cross-check against ASSESSOR NAVIGATION PREAMBLE entry point 2 canonical table list; any name not in that list = FAIL this item (e.g., "Phase 2 coverage table" is not in the list; "Phase 2 Signal Coverage Table" is)
  [ ] FORWARD VERIFIED declaration: statement beginning with "FORWARD VERIFIED:" present after manifest; explicitly declares manifest -> downstream direction as confirmed and references canonical table names; intent description without the verification assertion = FAIL
  [ ] BACKWARD VERIFIED declaration: statement beginning with "BACKWARD VERIFIED:" present after manifest; explicitly declares downstream -> manifest direction as confirmed and references canonical table names; future-tense statement without the verification assertion = FAIL
  [ ] Preamble cross-check: Derived Views table names in this manifest match the canonical set listed in ASSESSOR NAVIGATION PREAMBLE entry point 2 -- if canonical set has 5 entries, Derived Views uses names drawn from those 5 entries only
All items confirmed against format? PHASE 0 COMPLETE.

---

PHASE 1 -- ECHO
Run this phase before examining signal accuracy comparisons in Phase 3.

{{#if amend}}[AMEND: {{amend}} only -- outcomes outside this scope excluded from Echo candidacy]{{/if}}

The Echo is the single post-ship observable satisfying all three conditions:
  (a) Not predicted by any gathered signal -- not even partially
  (b) Not a named risk or acknowledged unknown at commit time
  (c) Observable only after the feature shipped

Procedure:
  Step 1: List every post-ship outcome (within AMEND scope if set).
  Step 2: Eliminate outcomes predicted by gathered signals.
  Step 3: Eliminate named risks or known unknowns.
  Step 4: Select the one with highest commit-decision impact.
  Step 5: No candidates: Echo = "No Echo -- all post-ship outcomes were within signal bounds."

| Echo (one sentence) | Nearest signal artifact | Commit relevance: HIGH / MEDIUM / LOW |
|---------------------|------------------------|--------------------------------------|
| [finding or "No Echo -- all post-ship outcomes were within signal bounds"] | [name or "none"] | [HIGH / MEDIUM / LOW or "N/A"] |

  > **Pattern**: [taxonomy label or "other: name"] -- [description of recurring failure mode -- not Echo restatement]
  > **Why unexpected**: [prior belief contradicted -- what was expected and why reality diverged]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap | scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

LOCK: Echo table, Pattern, and Why-unexpected are final. Phases 2-9 may not change them.

PHASE 1 SEAL -- format contract:
  [ ] Echo: {one sentence} OR "No Echo -- all post-ship outcomes were within signal bounds"
  [ ] Nearest signal: {artifact-filename.md} OR "none"
  [ ] Commit relevance: HIGH | MEDIUM | LOW | N/A
  [ ] Pattern: "> **Pattern**: {label} -- {failure class description, not Echo restatement}"
  [ ] Why unexpected: "> **Why unexpected**: {prior belief contradicted}"
  {{#if amend}}[ ] AMEND scope marker present above table{{/if}}
All items confirmed against format? PHASE 1 COMPLETE.

---

PHASE 2 -- SIGNAL INVENTORY
[DERIVED FROM: AUDIT MANIFEST | OPERATION: group by Namespace, count rows per group, assign COVERED if count >= 1 else EMPTY]

Produce a fixed 9-row namespace coverage table. Every namespace gets exactly one row. Derive from Phase 0 AUDIT MANIFEST.

{{#if amend}}[AMEND: {{amend}} only -- out-of-scope artifacts go to OOS table below]{{/if}}

| Namespace | Status          | Artifact count | Primary artifact (or "--") | Prediction theme (or "--") |
|-----------|-----------------|----------------|--------------------------|--------------------------|
| scout     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| draft     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| review    | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| flow      | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| trace     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| prove     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| listen    | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| program   | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| topic     | COVERED / EMPTY | N              | [filename or "--"]        | [one phrase or "--"]      |
| TOTAL     |                 | N              |                          |                          |

{{#if amend}}Out-of-scope artifacts:
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside {{amend}} scope] |
If none: "No artifacts excluded -- all in scope."
{{/if}}

PHASE 2 SEAL -- format contract:
  [ ] All 9 namespace rows in exact order: scout, draft, review, flow, trace, prove, listen, program, topic
  [ ] Status: {COVERED} or {EMPTY} per row -- no other value, no blank
  [ ] Artifact count: {integer} per row
  [ ] Primary artifact: {filename.md} or "--"
  [ ] TOTAL row present with {integer} in Artifact count cell
  {{#if amend}}[ ] OOS table present immediately after main table{{/if}}
  [ ] Derived From header: "[DERIVED FROM: AUDIT MANIFEST | OPERATION: group by Namespace, count rows per group, assign COVERED if count >= 1 else EMPTY]" present above table
All items confirmed against format? PHASE 2 COMPLETE.

---

PHASE 3 -- PREDICTED VS ACTUAL
[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter rows where Namespace is COVERED; surface Prediction, Actual, Verdict per namespace]

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted (signals' collective claim post-ship) | Actual (what was observed) | Match: C / P / W / ND |
|-----------|------------------------------------------------|---------------------------|----------------------|
| [name] | [from AUDIT MANIFEST Prediction column] | [from AUDIT MANIFEST Actual column] | [from AUDIT MANIFEST Verdict column] |

C = Correct, P = Partial, W = Wrong, ND = No post-ship data yet.

PHASE 3 SEAL -- format contract:
  [ ] Row count: one per COVERED namespace from Phase 2 -- no omissions
  [ ] Predicted: {statement} -- not blank, not "N/A"
  [ ] Actual: {statement} -- not blank, not "N/A"
  [ ] Match: C | P | W | ND
  [ ] Derived From header: "[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter COVERED namespaces]" present above table
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed against format? PHASE 3 COMPLETE.

---

PHASE 4 -- NAMESPACE ACCURACY
[DERIVED FROM: AUDIT MANIFEST | OPERATION: count Verdict values by Namespace; exclude ND from denominator]

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | C | P | W | ND | Weighted score: (Cx100 + Px50) / (C+P+W) |
|-----------|---|---|---|-----|------------------------------------------|
| [name]    |   |   |   |     |                                          |
| TOTAL     |   |   |   |     |                                          |

Correct signals: {C} / {C+P+W} = X%

RECONCILIATION TABLE:
[DERIVED FROM: AUDIT MANIFEST | OPERATION: forward sequential count vs backward recovery from Verdict = W]

| Direction | Starting point | Steps | Total scored | Correct | Match? |
|-----------|---------------|-------|--------------|---------|--------|
| Forward | Manifest row 1, count each scored verdict sequentially | [+1 C, +1 W, etc.] | {N} | {C} | -- |
| Backward | W={W}; +P={P}; +C={C}; total scored={N} | [arithmetic shown] | {N} | C=total-W-P | YES / NO |

Reconciliation result: Forward={N}; Backward={N}; Match: YES (proceed) / NO (recheck manifest).

PHASE 4 SEAL -- format contract:
  [ ] Row count: one per Phase 3 namespace -- no omissions
  [ ] C, P, W, ND: {integer} per cell -- blank invalid; 0 valid
  [ ] Weighted score: {number}/100 per row OR "0 scored signals"
  [ ] TOTAL row: {number}/100
  [ ] Count ratio: "{N}/{M} = {X}%" immediately below scoring table
  [ ] RECONCILIATION TABLE: present with Forward and Backward rows and result row
  [ ] Reconciliation Match = YES before proceeding
  [ ] Derived From header present above scoring table
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed against format? PHASE 4 COMPLETE.

---

PHASE 5 -- CONFLICT AUDIT
Does any Phase 3 or Phase 4 finding suggest the locked Phase 1 Echo should change?

If YES: CONFLICT DETECTED / Source / Analysis / Resolution: Phase 1 Echo preserved.
If NO: "CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 are consistent with the locked Echo."

PHASE 5 SEAL: one of two exact outputs; no Phase 1 modification.
All items confirmed? PHASE 5 COMPLETE.

---

PHASE 6 -- ACCURACY VERDICT
Draw from Phase 4 TOTAL and count ratio. Do not recalculate.
"Signal accuracy for [topic]: [TOTAL]/100 -- [STRONG/ADEQUATE/WEAK]. Count accuracy: [N/M = X%]."

PHASE 6 SEAL: exact format; both values from Phase 4; tier label matches score.
All items confirmed? PHASE 6 COMPLETE.

---

PHASE 7 -- GAP ANALYSIS
[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter rows where Verdict = W or P; add EMPTY namespaces where absence is material]

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

Column A = prior belief ("We assumed X"). Column B = discovery missed. Must differ per row.

| Gap (signal type absent) | Namespace | Assumption held without evidence [A] | Skill to run | Would have surfaced [B] | Changed commit? YES / NO |
|--------------------------|-----------|--------------------------------------|-------------|-------------------------|--------------------------|
| [type] | [ns] | [prior belief -- "We assumed X" -- NOT an outcome] | [/exact-skill-name] | [discovery -- distinct from A] | YES / NO |

No gaps: "No gaps -- signal coverage was sufficient for this commit decision."

  > **Recommendation**: Addresses [slot:gap-or-echo] by [slot:practice-change] so that [slot:measurable-outcome].

PHASE 7 SEAL -- format contract:
  [ ] Gap rows: every W or P namespace from Phase 3 OR "no gaps"
  [ ] Material EMPTY namespaces: every one with commit-relevant absence has a row
  [ ] Column A: "We assumed X" -- not outcome, not blank
  [ ] Column B: different from Column A per row
  [ ] Column A != Column B per row
  [ ] Skill: {/exact-skill-name}
  [ ] Changed commit: YES | NO per row
  [ ] Slot check: no "[slot:" strings in output
  [ ] Derived From header: "[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter W or P rows; add material EMPTY namespaces]" present above gap table
  {{#if amend}}[ ] AMEND scope marker present above gap table{{/if}}
All items confirmed against format? PHASE 7 COMPLETE.

---

PHASE 8 -- CALIBRATION TREND

COPY the accuracy score from the Phase 6 verdict sentence. Do not recompute. Label the cell: COPY-VERIFIED [source: Phase 6 verdict].

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [ref or "none"] | [score or "--"] | {N}/100 -- COPY-VERIFIED [source: Phase 6 verdict] | [+/-N or "--"] | up improving / down degrading / = stable |

No prior: "First retro for this topic -- this score establishes the calibration baseline."

PHASE 8 SEAL -- format contract:
  [ ] Prior retro: {topic}/{YYYY-MM-DD} or "none"; Delta: {+/-N or 0 or "--"}; Trend: one of three values or "first retro" statement

  [ ] This score -- independent verification:
      CHECK: "This score" cell non-blank, {number}/100 format.
      HOW: Read "This score" cell in Phase 8 table only. Do not read Phase 6 or Phase 4.
      Format required: {number}/100.

  [ ] COPY-VERIFIED -- independent verification:
      CHECK: Score in "This score" was copied from Phase 6, not computed.
      HOW: Open Phase 6 verdict sentence. Find score before "/100". Compare to "This score" value. "COPY-VERIFIED" label must be present. Do not read Phase 4.
      Format required: cell label contains "COPY-VERIFIED".

  [ ] COPY-SOURCE -- independent verification:
      CHECK: "This score" cell names Phase 6 verdict as source, not Phase 4.
      HOW: Read cell label. Confirm "Phase 6 verdict". Phase 4 reference or absent label = FAIL.
      Format required: label contains "source: Phase 6 verdict".

All items confirmed against format? PHASE 8 COMPLETE.

---

PHASE 9 -- ECHO -> SIGNAL DESIGN
Translate the Phase 1 Echo and Pattern into one concrete practice change.

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [exact Echo cell content -- not paraphrased] | [exact Pattern taxonomy label -- verbatim] | [one specific practice change] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL -- format contract:
  [ ] Echo cell: {Phase 1 Echo copied verbatim} -- character-for-character match
  [ ] Pattern cell: {Phase 1 taxonomy label copied verbatim} -- exact match, not synonym
  [ ] Proposed change: {one specific actionable change} -- not "gather more signals", not generic
  [ ] Change type: one of: new skill | rubric amendment | threshold adjustment
All items confirmed against format? RETRO COMPLETE.

---

Execute phases in order: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9. Verify compliance against PRE-EXECUTION CONTRACT before marking complete.

Design guarantees (audit reference):
- PRE-EXECUTION CONTRACT: ASSESSOR NAVIGATION PREAMBLE (three-row structured table + canonical table set declaration) followed by four-column mechanism table. Preamble entry point 2 declares the canonical set; all other mechanisms reference it.
- Phase 0: AUDIT MANIFEST with Signal window, Mode, Verdict per row, Derived Views per row using canonical names from preamble entry point 2. FORWARD VERIFIED and BACKWARD VERIFIED declarations reference preamble canonical set. Phase 0 SEAL cross-checks Derived Views names against preamble canonical set (item 8). All downstream sections carry [DERIVED FROM: AUDIT MANIFEST] headers.
- Phase 1: Echo locked before signal comparison. Pattern and Why-unexpected required.
- Phase 2: Fixed 9-row table. AMEND adds OOS secondary table. [DERIVED FROM: AUDIT MANIFEST] header required.
- Phase 3: [DERIVED FROM: AUDIT MANIFEST] header required. One row per COVERED namespace.
- Phase 4: Weighted score AND count ratio. RECONCILIATION TABLE required. [DERIVED FROM: AUDIT MANIFEST] header required.
- Phase 6: Verdict copies both formats from Phase 4. No recalculation.
- Phase 7: Column A = belief, Column B = outcome. Three-slot [slot:X]. [DERIVED FROM: AUDIT MANIFEST] header required.
- Phase 8: Score COPIED from Phase 6. Three-field SEAL with independent CHECK/HOW blocks.
- All 9 seals: explicit format-string per field.
```
