I have everything I need. Now writing the complete R20 variations document.

---

# topic-retro -- Variations R20

**Date:** 2026-03-17
**Rubric:** v18 (C-01 through C-47; total available = 168)
**R19 top scorer:** V-05 -- discovered C-46 and C-47 as excellence patterns. Source criteria for this round.
**New criteria to target:** C-46 (SEAL-Preamble Cross-Reference Integrity Check) and C-47 (Preamble as Canonical Name Registry, Downstream Table Authority).

**Base used:** R19-V-05 -- all prior integrations carried forward:
- C-22: OOS secondary table
- C-23: Seal format-contract strings per field (all 9 phases)
- C-24: Echo why-unexpected explained
- C-25: Three-slot recommendation template
- C-26: Gap inertia columns A/B structurally isolated
- C-27: SEAL coverage extended to all phases
- C-28: `[slot:X]` token + SEAL placeholder check
- C-29: Phase 8 "do not recompute" + SEAL copy-citation check
- C-30: Three-field SEAL (This score / COPY-VERIFIED / COPY-SOURCE)
- C-31: `## PRE-EXECUTION CONTRACT` positioned before Phase 1
- C-32: Phase 8 SEAL each field has independent CHECK:/HOW: block
- C-33: PRE-EXECUTION CONTRACT three-column table with "Verified in"
- C-36: Three-pass architectural isolation as structural property
- C-37: Accuracy reconciliation cross-check (forward + backward counts must agree)
- C-38: Backward recovery table as named structural artifact
- C-39: Signal window and Mode declared as named fields in PRE-EXECUTION CONTRACT
- C-40: AUDIT MANIFEST as primary table; all downstream sections derived as views
- C-41: Named-criteria phase gate
- C-42: Bidirectional manifest citation (`Derived Views` column + `[DERIVED FROM]` headers)
- C-43: PRE-EXECUTION CONTRACT as manifest navigation index (`Manifest column` field)
- C-44: SEAL-enforced exact canonical names + FORWARD VERIFIED + BACKWARD VERIFIED declarations
- C-45: Structured ASSESSOR NAVIGATION PREAMBLE (three-row table, not prose paragraphs)

**C-46 gap analysis:** R19-V-05 has a Phase 0 SEAL item that cross-checks Derived Views names against the preamble's canonical set. But the canonical set it references is an inline enumeration inside the FORWARD VERIFIED declaration block -- not a named authority block within the preamble. C-46's pass condition is specific: the SEAL item must reference the preamble authority block by name. Inline enumeration and named authority block are structurally distinct: an inline list can silently drift; a named first-class block is a locatable, versioned single source of truth. R19-V-05's SEAL cross-check is present but its reference target (inline list in FORWARD VERIFIED) fails C-46's named-block requirement. R19-V-05 = C-46 PARTIAL.

**C-47 gap analysis:** R19-V-05's ASSESSOR NAVIGATION PREAMBLE is a three-row table where entry point 2 says "Derived Views column → The exact downstream table(s) that receive data from that manifest row." The canonical table names are distributed: some appear in the Derived Views assignment rules block; some in the FORWARD VERIFIED declaration's inline enumeration. C-47 requires a standalone named declaration block -- e.g., **Canonical downstream table set** -- positioned below the three-entry-point table, enumerating all downstream tables by their exact canonical identifiers, serving as the single source of truth. R19-V-05 has the canonical names but they are embedded in prose/inline structures, not a standalone named registry. C-45 PASS with canonical names in prose = C-47 PARTIAL.

**Single-axis:** V-01 (C-47 only), V-02 (C-46 only -- N/A condition control test), V-03 (phrasing register negative control).
**Combined:** V-04 (C-47 + C-46), V-05 (full integration with structural cross-binding).

---

## Summary Table

| ID | Primary Axis | C-47 Mechanism | C-46 Mechanism | Hypothesis |
|----|-------------|----------------|----------------|------------|
| V-01 | C-47 (single) | Standalone **Canonical downstream table set** block added after three-entry-point table; 5-row registry enumerating exact downstream table identifiers | Phase 0 SEAL cross-check retains R19-V-05 form: checks consistency with preamble but does not name the authority block explicitly | Standalone registry block satisfies C-47 (named declaration, not entry-point prose); SEAL cross-check remains PARTIAL on C-46 because it references "preamble" generically rather than the named authority block -- establishes the C-47 precondition required before C-46 can reach PASS |
| V-02 | C-46 (single, N/A control) | No standalone authority block; preamble retains R19-V-05 three-row table only | Phase 0 SEAL gains explicit item: "Derived Views entries cross-checked against **Canonical downstream table set** authority block in ASSESSOR NAVIGATION PREAMBLE (named explicitly)" -- but the block is absent | Per rubric, C-47 absent makes C-46 non-applicable; tests whether the named SEAL item alone triggers N/A correctly or produces a different failure mode; C-46 SEAL item is unreachable without its prerequisite |
| V-03 | Phrasing register (negative control) | Canonical names listed as a prose sentence in entry point 2 cell ("e.g., Phase 2 coverage table, Phase 3 accuracy table..."); informal label, no standalone named block | SEAL cross-check references "downstream table names listed in entry point 2 above" -- informal inline reference, not a named authority block | Both C-46 PARTIAL (inline reference fails named-block requirement) and C-47 PARTIAL (entry-point prose fails standalone-block requirement); confirms rubric distinction between information-present and structure-enforced |
| V-04 | C-47 + C-46 (combined) | V-01 standalone **Canonical downstream table set** block below three-entry-point table | Phase 0 SEAL gains explicit item: "Derived Views entries cross-checked against **Canonical downstream table set** authority block in ASSESSOR NAVIGATION PREAMBLE by name -- generic preamble reference or inline enumeration = FAIL this item" | Zero-interference: C-47 lives in the preamble structure below the navigation table; C-46 lives in Phase 0 SEAL; no shared modification surface; both should produce PASS simultaneously |
| V-05 | Full integration (cross-binding) | V-04 authority block + FORWARD VERIFIED declaration names "**Canonical downstream table set** declared in ASSESSOR NAVIGATION PREAMBLE" as source of canonical identifiers; Derived Views assignment rules instruct to use "exact identifiers from the **Canonical downstream table set** authority block" | V-04 SEAL cross-check + additional SEAL wording: "Cross-check must name the **Canonical downstream table set** block explicitly -- 'preamble generally' or inline enumeration = FAIL" | Mutual enforcement: SEAL validates against the registry by name; FORWARD VERIFIED cites the registry by name; registry is the single source of truth for both; any future drift (renamed downstream table, new phase) is caught at SEAL time rather than discovered during audit |

---

## V-01 -- Standalone Canonical Name Registry: C-47 via Authority Block in Preamble

**Axis:** C-47 (single). A standalone **Canonical downstream table set** authority block is added to the ASSESSOR NAVIGATION PREAMBLE, positioned below the three-entry-point table. This is a 5-row registry enumerating each downstream table by its exact canonical identifier, the phase it appears in, and what manifest rows populate it. Phase 0 SEAL cross-check item unchanged from R19-V-05 -- it requires Derived Views to use exact names from the canonical set but references the canonical set generically, not the named authority block. C-46 not addressed.

**Hypothesis:** R19-V-05 has canonical table names in the FORWARD VERIFIED inline enumeration but no standalone named registry block. C-47 requires a standalone named declaration block -- not row-embedded prose. Adding the **Canonical downstream table set** block satisfies C-47 by making the canonical set a first-class structural artifact. The Phase 0 SEAL cross-check (unchanged) references "preamble's canonical names" without naming the authority block, so C-46 remains PARTIAL -- the cross-check exists but references the wrong structural target. V-01 isolates C-47 as a net gain from the preamble structure alone, independent of SEAL wiring.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Execute
phases in order. Each phase ends with a PHASE SEAL -- a format-contract checklist where every
item specifies the required field and its required value form. Do not proceed past a phase until
every seal item is confirmed.

{{#if amend}}AMEND SCOPE: {{amend}} -- all phases operate within this constraint only. Every
table carries an explicit scope marker. Phase 2 includes an out-of-scope table.{{/if}}

---

## PRE-EXECUTION CONTRACT

Read before executing Phase 0.

### ASSESSOR NAVIGATION PREAMBLE

This audit system is navigable from three entry points. Locate the row matching your starting
position and follow the navigation field.

| # | If you are starting at... | Locate this navigation field | It takes you to... |
|---|--------------------------|-----------------------------|--------------------|
| 1 | Any row in this PRE-EXECUTION CONTRACT | `Manifest column` field (4th column of the table below) | The exact AUDIT MANIFEST column that evidences the commitment in that row |
| 2 | Any row in the AUDIT MANIFEST (Phase 0) | `Derived Views` column (last column of Phase 0 table) | The exact downstream table(s) that receive data from that manifest row |
| 3 | Any downstream section header (Phase 2, 3, 4, 7) | `[DERIVED FROM: AUDIT MANIFEST \| OPERATION: ...]` declaration in the section header | The AUDIT MANIFEST as source for that section |

**Canonical downstream table set** (standalone authority block):

All Derived Views entries must use the exact identifiers in this table. Aliases and
abbreviations are not acceptable.

| Canonical table name | Phase | Populated from |
|---------------------|-------|----------------|
| Phase 2 Signal Coverage Table | 2 | Every manifest row (grouped by Namespace) |
| Phase 3 Predicted vs Actual Table | 3 | Rows with Status = COVERED and non-ND Verdict |
| Phase 4 Namespace Accuracy Table | 4 | Scored manifest rows (Verdict != ND) |
| Phase 4 Reconciliation Table | 4 | All manifest rows (ND rows excluded from denominator) |
| Phase 7 Gap Analysis Table | 7 | Rows with Verdict = W or P; material EMPTY namespaces |

| Mechanism | Structural guarantee -- what is enforced and how | Verified in | Manifest column |
|-----------|--------------------------------------------------|-------------|-----------------|
| Signal window | Bounding date range or sprint scope. Named structural field in manifest header -- not inferred from prose. | Phase 0 SEAL item 1 | Signal window (manifest header field) |
| Mode | AMEND or FRESH flag. AMEND: scope declared top, every table scoped, Phase 2 OOS table. | Phase 0 SEAL item 2; Phase 2 SEAL item 6 if AMEND | Mode (manifest header field) |
| Echo lock | Phase 1 before signal comparison. Echo/Pattern/Why-unexpected locked. Phases 2-9 must not modify. | Phase 1 SEAL items 1-5 | Prediction (Echo is the finding absent from this column) |
| Manifest derivation | All downstream tables derived as views of AUDIT MANIFEST. Derivation stated per section. Derived Views column enables forward navigation; [DERIVED FROM] headers enable backward navigation. | Phase 0 SEAL items 3-7; [DERIVED FROM] headers in all downstream sections | (all columns -- manifest is derivation source) |
| Namespace coverage | Fixed 9-row table, COVERED/EMPTY derived by grouping manifest Namespace column. | Phase 2 SEAL items 1-5 | Namespace |
| Verdict accuracy | Weighted score and count ratio required. Reconciliation cross-check required. | Phase 4 SEAL items 4-5; RECONCILIATION TABLE | Verdict |
| Gap identification | W or P manifest rows feed gap table. Material EMPTY namespaces included. | Phase 7 SEAL items 1-2 | Verdict (filter: W or P) |
| Accuracy copy | Phase 6 copies Phase 4 TOTAL. Phase 8 copies Phase 6 verdict sentence. No recomputation. | Phase 6 SEAL; Phase 8 SEAL items 2-4 | Verdict (aggregate) |
| Gap inertia columns | Column A = prior belief; Column B = missed discovery; must not share content per row. | Phase 7 SEAL items 3-5 | Verdict (gap rows) |
| Recommendation slots | Three `[slot:X]` tokens; SEAL confirms no `[slot:` strings survive. | Phase 7 SEAL item 8 | (generated, not manifest-derived) |
| Copy guard | Phase 8 COPIED from Phase 6. Three-field SEAL: This score / COPY-VERIFIED / COPY-SOURCE each with independent CHECK:/HOW: blocks. | Phase 8 SEAL items 2-4 | Verdict (aggregate) |
| Seal format contracts | All 9 seals: explicit format-string per field; verify value form, not just presence. | All 9 SEAL blocks | (all columns) |
| AMEND scope | Every table has scope marker when AMEND set. Phase 2 OOS table present. | Phase 2 SEAL item 6 | (all columns -- scope filter applied to all manifest rows) |

---

## PHASE 0 -- AUDIT MANIFEST

Before running any phase, enumerate all signal artifacts and build the AUDIT MANIFEST. All
downstream tables are derived from this manifest. The `Derived Views` column enables forward
navigation: an assessor at any manifest row can identify which downstream tables include it
without reading phase specifications. Use the canonical table identifiers listed in the
**Canonical downstream table set** authority block in the preamble -- abbreviations and
informal aliases are not acceptable.

Signal window: [state the date range or sprint scope bounding the predictions being evaluated]
Mode: AMEND ({{amend}}) | FRESH [circle one]

Search simulations/**/[topic]-*-*.md. For each artifact record namespace, prediction, actual
outcome, verdict, and forward-navigation destinations using canonical table names only.

| # | Namespace | Artifact | Prediction (signal's claim) | Actual (post-ship) | Verdict (C/P/W/ND) | Derived Views |
|---|-----------|----------|----------------------------|-------------------|-------------------|---------------|
| 1 | [ns] | [filename] | [what signal claimed] | [what was observed] | C / P / W / ND | [Phase 2 Signal Coverage Table; Phase 3 Predicted vs Actual Table (if non-ND); Phase 4 Namespace Accuracy Table (if non-ND); Phase 4 Reconciliation Table; Phase 7 Gap Analysis Table (if W or P)] |
| ... | | | | | | |

Derived Views assignment rules (use exact names from the Canonical downstream table set):
- Every row -> "Phase 2 Signal Coverage Table"
- Non-ND rows -> add "Phase 3 Predicted vs Actual Table; Phase 4 Namespace Accuracy Table"
- W or P rows -> add "Phase 7 Gap Analysis Table"
- Every row -> add "Phase 4 Reconciliation Table"

After completing the manifest, write the bidirectional navigation verification block:

  FORWARD VERIFIED: Manifest -> downstream direction confirmed. Each manifest row's Derived Views
  column uses exact canonical table names. An assessor reading any manifest row can navigate
  forward to downstream sections without reading phase specifications.
  Forward navigation confirmed complete.

  BACKWARD VERIFIED: Downstream -> manifest direction confirmed. Each downstream section --
  Phase 2 Signal Coverage Table, Phase 3 Predicted vs Actual Table, Phase 4 Namespace Accuracy
  Table, Phase 4 Reconciliation Table, Phase 7 Gap Analysis Table -- carries a
  [DERIVED FROM: AUDIT MANIFEST | OPERATION: ...] header naming this manifest as its source.
  An assessor reading any downstream section can navigate backward to the manifest.
  Backward navigation confirmed complete.

PHASE 0 SEAL -- format contract:
  [ ] Signal window: {date range or sprint name} -- named structural field in manifest header
  [ ] Mode: {AMEND | FRESH} -- named field present; if AMEND, scope carried into all phases
  [ ] Manifest rows: one row per signal artifact; no namespace groups without individual rows
  [ ] Verdict: {C | P | W | ND} per row -- no other values, no blank
  [ ] Derived Views exact canonical names: each entry uses an exact name from the Canonical
      downstream table set -- "Phase 2 Signal Coverage Table" not "Phase 2 table" or "coverage
      table"; informal alias = FAIL this item
  [ ] FORWARD VERIFIED declaration: statement beginning with "FORWARD VERIFIED:" present after
      manifest table; explicitly declares manifest -> downstream direction as confirmed; intent
      description without verification assertion = FAIL this item
  [ ] BACKWARD VERIFIED declaration: statement beginning with "BACKWARD VERIFIED:" present after
      manifest table; explicitly declares downstream -> manifest direction as confirmed;
      future-tense statement without verification assertion = FAIL this item
All items confirmed against format? PHASE 0 COMPLETE.

---

PHASE 1 -- ECHO
Run this phase before examining signal accuracy comparisons in Phase 3.

{{#if amend}}[AMEND: {{amend}} only -- outcomes outside this scope excluded from Echo
candidacy]{{/if}}

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
  > **Pattern**: [name from taxonomy or "other: [your name]"] -- [recurring failure mode class -- not Echo restatement]
  > **Why unexpected**: [prior belief contradicted -- what was expected and why reality diverged]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap |
  scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

LOCK: Echo table, Pattern, and Why-unexpected are final. Phases 2-9 may not change them.

PHASE 1 SEAL -- format contract:
  [ ] Echo: {one sentence} OR exact string "No Echo -- all post-ship outcomes were within signal bounds"
  [ ] Nearest signal: {artifact-filename.md} OR exact string "none"
  [ ] Commit relevance: HIGH | MEDIUM | LOW | N/A -- "N/A" only valid when paired with "No Echo"
  [ ] Pattern: "> **Pattern**: {taxonomy-label or "other: name"} -- {failure class description -- not Echo restatement}"
  [ ] Why unexpected: "> **Why unexpected**: {prior belief contradicted -- names what was expected, not just that it was unexpected}"
  {{#if amend}}[ ] AMEND scope marker present immediately above table{{/if}}
All items confirmed against format? PHASE 1 COMPLETE.

---

PHASE 2 -- SIGNAL INVENTORY
[DERIVED FROM: AUDIT MANIFEST | OPERATION: group by Namespace, count rows per group, assign COVERED if count >= 1 else EMPTY]

Produce a fixed 9-row namespace coverage table. Every namespace gets exactly one row. Derive
from Phase 0 AUDIT MANIFEST -- do not re-examine artifacts independently.

{{#if amend}}[AMEND: {{amend}} only -- out-of-scope artifacts go to the OOS table below]{{/if}}

| Namespace | Status          | Artifact count | Primary artifact (or "--") | Prediction theme (or "--") |
|-----------|-----------------|----------------|---------------------------|---------------------------|
| scout     | COVERED / EMPTY | N              | [filename or "--"]         | [one phrase or "--"]       |
| draft     | COVERED / EMPTY | N              | [filename or "--"]         | [one phrase or "--"]       |
| review    | COVERED / EMPTY | N              | [filename or "--"]         | [one phrase or "--"]       |
| flow      | COVERED / EMPTY | N              | [filename or "--"]         | [one phrase or "--"]       |
| trace     | COVERED / EMPTY | N              | [filename or "--"]         | [one phrase or "--"]       |
| prove     | COVERED / EMPTY | N              | [filename or "--"]         | [one phrase or "--"]       |
| listen    | COVERED / EMPTY | N              | [filename or "--"]         | [one phrase or "--"]       |
| program   | COVERED / EMPTY | N              | [filename or "--"]         | [one phrase or "--"]       |
| topic     | COVERED / EMPTY | N              | [filename or "--"]         | [one phrase or "--"]       |
| TOTAL     |                 | N              |                           |                           |

{{#if amend}}Out-of-scope artifacts (excluded per AMEND constraint):
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside {{amend}} scope] |
If none excluded: "No artifacts excluded -- all in scope."
{{/if}}

PHASE 2 SEAL -- format contract:
  [ ] All 9 namespace rows in exact order: scout, draft, review, flow, trace, prove, listen, program, topic
  [ ] Status: {COVERED} or {EMPTY} per row -- no other value, no blank
  [ ] Artifact count: {integer} per row -- 0 valid for EMPTY
  [ ] Primary artifact: {filename.md} or "--" -- not blank
  [ ] TOTAL row: present with {integer} in Artifact count cell
  {{#if amend}}[ ] OOS table: present immediately after main table -- even if "No artifacts excluded -- all in scope."{{/if}}
  [ ] Derived From header: "[DERIVED FROM: AUDIT MANIFEST | OPERATION: group by Namespace...]" present above table
All items confirmed against format? PHASE 2 COMPLETE.

---

PHASE 3 -- PREDICTED VS ACTUAL
[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter rows where Namespace is COVERED; surface Prediction, Actual, Verdict per namespace]

For each namespace with Status = COVERED in Phase 2. Derive from AUDIT MANIFEST rows -- do
not independently re-evaluate predictions.

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted (signals' collective claim post-ship) | Actual (what was observed) | Match: C / P / W / ND |
|-----------|------------------------------------------------|---------------------------|----------------------|
| [name] | [from AUDIT MANIFEST Prediction column] | [from AUDIT MANIFEST Actual column] | [from AUDIT MANIFEST Verdict column] |

C = Correct, P = Partial (direction right, magnitude/timing off), W = Wrong, ND = No post-ship data.

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
| Backward | W={W}; +P={P}; +C={C}; total={N} | [recovery arithmetic shown] | {N} | C=total-W-P={C} | YES / NO |

Reconciliation result: Forward={N}; Backward={N}; Match: YES (proceed) / NO (recheck manifest).

PHASE 4 SEAL -- format contract:
  [ ] Row count: one row per Phase 3 namespace -- no omissions
  [ ] C, P, W, ND: {integer} per cell -- blank invalid; 0 valid
  [ ] Weighted score: {number}/100 per row OR blank with note "0 scored signals"
  [ ] TOTAL row: present, format: {number}/100
  [ ] Count-based ratio: stated in format "{N}/{M} = {X}%" immediately below scoring table
  [ ] RECONCILIATION TABLE: present with Forward and Backward rows and result row
  [ ] Reconciliation result: Match = YES before proceeding -- NO = do not continue
  [ ] Derived From header: "[DERIVED FROM: AUDIT MANIFEST | OPERATION: count Verdict values...]" present above scoring table
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed against format? PHASE 4 COMPLETE.

---

PHASE 5 -- CONFLICT AUDIT
Mandatory. Always produces exactly one of two outputs.

Review the locked Phase 1 Echo. Does any Phase 3 verdict or Phase 4 score suggest the Echo
should name a different finding?

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
Draw weighted score from Phase 4 TOTAL row. Draw count ratio from Phase 4 count-based
statement. Do not recalculate either number.

"Signal accuracy for [topic]: [TOTAL]/100 -- [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]. Count accuracy: [N/M = X%]."

PHASE 6 SEAL -- format contract:
  [ ] Verdict sentence: present in exact format "Signal accuracy for {topic}: {score}/100 -- {STRONG|ADEQUATE|WEAK}. Count accuracy: {N}/{M} = {X}%."
  [ ] Weighted score: drawn from Phase 4 TOTAL row -- same number, not recalculated
  [ ] Count ratio: drawn from Phase 4 count-based statement -- same values, not recalculated
  [ ] Tier label: STRONG if >= 75 | ADEQUATE if 50-74 | WEAK if < 50 -- must match stated score
All items confirmed against format? PHASE 6 COMPLETE.

---

PHASE 7 -- GAP ANALYSIS
[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter rows where Verdict = W or P; add EMPTY namespaces where absence is material]

For each namespace scoring W or P in Phase 3, and each EMPTY namespace (Phase 2) where
absence is material to the commit decision.

{{#if amend}}[AMEND: {{amend}} only -- gaps outside this constraint excluded]{{/if}}

Column A = "Assumption held without evidence": the inertia belief that made this gap invisible
before commit. WHY the gap existed. Framed as prior belief ("We assumed X"), not an outcome.
Column B = "Would have surfaced": the discovery missed. WHAT was missed. Different from Column A.

| Gap (signal type absent) | Namespace | Assumption held without evidence [A] | Skill to run | Would have surfaced [B] | Changed commit? YES / NO |
|--------------------------|-----------|--------------------------------------|-------------|-------------------------|--------------------------|
| [type] | [ns] | [prior belief -- "We assumed X" -- NOT an outcome] | [/exact-skill-name] | [discovery -- distinct from Column A] | YES / NO |

No gaps: "No gaps -- signal coverage was sufficient for this commit decision."

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

COPY the accuracy score from the Phase 6 verdict sentence into the "This score" cell. Do not
recompute. Label the cell: COPY-VERIFIED [source: Phase 6 verdict].

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [ref or "none"] | [score or "--"] | {N}/100 -- COPY-VERIFIED [source: Phase 6 verdict] | [+/-N or "--"] | up improving / down degrading / = stable |

No prior retro: "First retro for this topic -- this score establishes the calibration baseline."

PHASE 8 SEAL -- format contract:
  [ ] Prior retro: {topic}/{YYYY-MM-DD} OR "none"; Delta: {+/-N or 0 or "--"}; Trend: one of three values or "first retro" statement

  [ ] This score -- independent verification:
      CHECK: "This score" cell non-blank, {number}/100 format.
      HOW: Read "This score" cell in Phase 8 table only. Do not read Phase 6 or Phase 4.
      Format required: {number}/100 -- blank or wrong format = FAIL.

  [ ] COPY-VERIFIED -- independent verification:
      CHECK: Score in "This score" was copied from Phase 6, not computed.
      HOW: Open Phase 6. Read verdict sentence. Find score before "/100". Compare to "This score"
      value. "COPY-VERIFIED" label must be present. Do not read Phase 4.
      Format required: cell label contains "COPY-VERIFIED" -- absent label = FAIL.

  [ ] COPY-SOURCE -- independent verification:
      CHECK: "This score" cell names Phase 6 verdict as source, not Phase 4.
      HOW: Read cell label. Confirm it names "Phase 6 verdict". Phase 4 reference or absent = FAIL.
      Format required: label contains "source: Phase 6 verdict" -- alternative source = FAIL.

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

Execute phases in order: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9. Verify compliance
against PRE-EXECUTION CONTRACT before marking complete.

Design guarantees (audit reference):
- PRE-EXECUTION CONTRACT: ASSESSOR NAVIGATION PREAMBLE with three-row navigation table followed
  by standalone **Canonical downstream table set** authority block (5 rows, exact identifiers).
  Four-column mechanism table follows (Mechanism / Guarantee / Verified in / Manifest column).
- Phase 0: AUDIT MANIFEST with Signal window, Mode, Verdict, Derived Views per row using exact
  canonical names. FORWARD VERIFIED + BACKWARD VERIFIED declarations required. Derived Views
  assignment rules reference the Canonical downstream table set. All downstream sections carry
  [DERIVED FROM: AUDIT MANIFEST] headers.
- Phase 1: Echo locked before signal comparison. Pattern and Why-unexpected required.
- Phase 4: Weighted score AND count ratio. RECONCILIATION TABLE required.
- Phase 8: Score COPIED from Phase 6. Three-field SEAL with independent CHECK:/HOW: blocks.
- All 9 seals: explicit format-string per field.
- C-47 satisfied: standalone **Canonical downstream table set** block in preamble. C-46: PARTIAL
  (SEAL cross-check references canonical names but not the authority block by name).
```

---

## V-02 -- Named Block Cross-Reference: C-46 N/A Condition Control Test

**Axis:** C-46 (single, N/A control). The Phase 0 SEAL gains an explicit item requiring Derived Views to be cross-checked against the "**Canonical downstream table set** authority block in the ASSESSOR NAVIGATION PREAMBLE" by name. However, no standalone authority block is added to the preamble -- C-47 is not addressed. Per rubric: "Preamble absent (C-47 N/A) makes C-46 non-applicable." This variation tests whether the named SEAL cross-check item alone triggers the N/A determination correctly, or whether the absence of the required block produces a different grading outcome.

**Hypothesis:** A SEAL item that requires cross-reference against a named block that does not exist is unreachable -- it cannot PASS or FAIL in the normal sense because the reference target is absent. The rubric's N/A condition for C-46 should activate here. The SEAL item wording names the block explicitly ("**Canonical downstream table set** authority block"), which signals intent to satisfy C-46 but lacks the prerequisite structural artifact. The variation confirms that C-46 cannot be satisfied by SEAL wiring alone; the C-47 authority block must exist first. Both C-46 = N/A and C-47 = FAIL expected.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Execute
phases in order. Each phase ends with a PHASE SEAL -- a format-contract checklist where every
item specifies the required field and its required value form. Do not proceed past a phase until
every seal item is confirmed.

{{#if amend}}AMEND SCOPE: {{amend}} -- all phases operate within this constraint only. Every
table carries an explicit scope marker. Phase 2 includes an out-of-scope table.{{/if}}

---

## PRE-EXECUTION CONTRACT

Read before executing Phase 0.

### ASSESSOR NAVIGATION PREAMBLE

This audit system is navigable from three entry points. Locate the row matching your starting
position and follow the navigation field.

| # | If you are starting at... | Locate this navigation field | It takes you to... |
|---|--------------------------|-----------------------------|--------------------|
| 1 | Any row in this PRE-EXECUTION CONTRACT | `Manifest column` field (4th column of the table below) | The exact AUDIT MANIFEST column that evidences the commitment in that row |
| 2 | Any row in the AUDIT MANIFEST (Phase 0) | `Derived Views` column (last column of Phase 0 table) | The exact downstream table(s) that receive data from that manifest row |
| 3 | Any downstream section header (Phase 2, 3, 4, 7) | `[DERIVED FROM: AUDIT MANIFEST \| OPERATION: ...]` declaration in the section header | The AUDIT MANIFEST as source for that section |

A completed retro is auditable from any of these three positions without reading the full
document in sequence.

| Mechanism | Structural guarantee -- what is enforced and how | Verified in | Manifest column |
|-----------|--------------------------------------------------|-------------|-----------------|
| Signal window | Bounding date range or sprint scope. Named structural field in manifest header -- not inferred from prose. | Phase 0 SEAL item 1 | Signal window (manifest header field) |
| Mode | AMEND or FRESH flag. AMEND: scope declared top, every table scoped, Phase 2 OOS table. | Phase 0 SEAL item 2; Phase 2 SEAL item 6 if AMEND | Mode (manifest header field) |
| Echo lock | Phase 1 before signal comparison. Echo/Pattern/Why-unexpected locked. Phases 2-9 must not modify. | Phase 1 SEAL items 1-5 | Prediction (Echo is the finding absent from this column) |
| Manifest derivation | All downstream tables derived as views of AUDIT MANIFEST. Derivation stated per section. Derived Views column enables forward navigation; [DERIVED FROM] headers enable backward navigation. | Phase 0 SEAL items 3-7; [DERIVED FROM] headers in all downstream sections | (all columns) |
| Namespace coverage | Fixed 9-row table, COVERED/EMPTY derived by grouping manifest Namespace column. | Phase 2 SEAL items 1-5 | Namespace |
| Verdict accuracy | Weighted score and count ratio required. Reconciliation cross-check required. | Phase 4 SEAL items 4-5; RECONCILIATION TABLE | Verdict |
| Gap identification | W or P manifest rows feed gap table. Material EMPTY namespaces included. | Phase 7 SEAL items 1-2 | Verdict (filter: W or P) |
| Accuracy copy | Phase 6 copies Phase 4 TOTAL. Phase 8 copies Phase 6 verdict sentence. No recomputation. | Phase 6 SEAL; Phase 8 SEAL items 2-4 | Verdict (aggregate) |
| Gap inertia columns | Column A = prior belief; Column B = missed discovery; must not share content per row. | Phase 7 SEAL items 3-5 | Verdict (gap rows) |
| Recommendation slots | Three `[slot:X]` tokens; SEAL confirms no `[slot:` strings survive. | Phase 7 SEAL item 8 | (generated) |
| Copy guard | Phase 8 COPIED from Phase 6. Three-field SEAL each with independent CHECK:/HOW: blocks. | Phase 8 SEAL items 2-4 | Verdict (aggregate) |
| Seal format contracts | All 9 seals: explicit format-string per field; verify value form, not just presence. | All 9 SEAL blocks | (all columns) |
| AMEND scope | Every table has scope marker when AMEND set. Phase 2 OOS table present. | Phase 2 SEAL item 6 | (all columns) |

---

## PHASE 0 -- AUDIT MANIFEST

Before running any phase, enumerate all signal artifacts and build the AUDIT MANIFEST. All
downstream tables are derived from this manifest. The `Derived Views` column enables forward
navigation: an assessor at any manifest row can identify which downstream tables include it
without reading phase specifications. Use exact canonical table names only.

Signal window: [state the date range or sprint scope bounding the predictions being evaluated]
Mode: AMEND ({{amend}}) | FRESH [circle one]

Search simulations/**/[topic]-*-*.md. For each artifact record namespace, prediction, actual
outcome, verdict, and forward-navigation destinations using canonical table names.

| # | Namespace | Artifact | Prediction (signal's claim) | Actual (post-ship) | Verdict (C/P/W/ND) | Derived Views |
|---|-----------|----------|----------------------------|-------------------|-------------------|---------------|
| 1 | [ns] | [filename] | [what signal claimed] | [what was observed] | C / P / W / ND | [Phase 2 Signal Coverage Table; Phase 3 Predicted vs Actual Table (if non-ND); Phase 4 Namespace Accuracy Table (if non-ND); Phase 4 Reconciliation Table; Phase 7 Gap Analysis Table (if W or P)] |
| ... | | | | | | |

Canonical Derived Views assignment rules:
- Every row -> "Phase 2 Signal Coverage Table"
- Non-ND rows -> add "Phase 3 Predicted vs Actual Table; Phase 4 Namespace Accuracy Table"
- W or P rows -> add "Phase 7 Gap Analysis Table"
- Every row -> add "Phase 4 Reconciliation Table"

After completing the manifest, write the bidirectional navigation verification block:

  FORWARD VERIFIED: Manifest -> downstream direction confirmed. Each manifest row's Derived Views
  column names downstream tables using canonical identifiers from the set {Phase 2 Signal Coverage
  Table, Phase 3 Predicted vs Actual Table, Phase 4 Namespace Accuracy Table, Phase 4
  Reconciliation Table, Phase 7 Gap Analysis Table}. Forward navigation confirmed complete.

  BACKWARD VERIFIED: Downstream -> manifest direction confirmed. Each downstream section carries a
  [DERIVED FROM: AUDIT MANIFEST | OPERATION: ...] header naming this manifest as its source.
  Backward navigation confirmed complete.

PHASE 0 SEAL -- format contract:
  [ ] Signal window: {date range or sprint name} -- named structural field in manifest header
  [ ] Mode: {AMEND | FRESH} -- named field present
  [ ] Manifest rows: one row per signal artifact; no namespace groups without individual rows
  [ ] Verdict: {C | P | W | ND} per row -- no other values, no blank
  [ ] Derived Views exact canonical names: each entry uses an exact canonical table name -- informal aliases = FAIL
  [ ] FORWARD VERIFIED declaration: statement beginning with "FORWARD VERIFIED:" present; declares direction confirmed
  [ ] BACKWARD VERIFIED declaration: statement beginning with "BACKWARD VERIFIED:" present; declares direction confirmed
  [ ] SEAL-Preamble authority block cross-reference: Derived Views entries in the manifest are
      cross-checked against the canonical table names declared in the **Canonical downstream
      table set** authority block in the ASSESSOR NAVIGATION PREAMBLE. The cross-check must
      name that authority block explicitly -- generic preamble reference or inline enumeration
      = FAIL. [NOTE: If the **Canonical downstream table set** authority block is absent from
      the ASSESSOR NAVIGATION PREAMBLE, this item is NON-APPLICABLE.]
All items confirmed against format? PHASE 0 COMPLETE.

---

[PHASE 1 through PHASE 9 and design guarantees: identical to V-01 above, with design guarantees
footer noting: "C-46: SEAL cross-check item present, requires named authority block reference.
**Canonical downstream table set** authority block absent from preamble -- C-47 not satisfied,
C-46 non-applicable per rubric."]
```

---

## V-03 -- Phrasing Register: Negative Control for C-46 and C-47

**Axis:** Phrasing register (negative control). The ASSESSOR NAVIGATION PREAMBLE uses prose bold-paragraph entry points (R18-V-05 form), not the R19-V-05 structured table. Canonical table names are listed as a prose sentence embedded in the "Entry from AUDIT MANIFEST" paragraph (not a standalone block). The Phase 0 SEAL cross-check references "downstream table names listed in Entry 2 above" -- an informal inline reference. The FORWARD VERIFIED declaration describes intent rather than declaring verification.

**Hypothesis:** Prose entry points convey the navigation information but fail C-45 (not a structured block) and fail C-47 (no standalone named authority block). The inline canonical list embedded in a prose paragraph fails C-47 (not a standalone block) and the SEAL cross-check referencing "Entry 2 above" fails C-46 (not a named authority block by name). Both C-46 and C-47 score PARTIAL. This variation also regresses to C-44 PARTIAL (intent descriptions in check statements, not VERIFIED declarations), confirming that the structured enforcement of R19-V-05 is load-bearing for C-44/C-45 and V-01's authority block is load-bearing for C-47.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Execute
phases in order. Each phase ends with a PHASE SEAL -- a format-contract checklist. Do not
proceed past a phase until every seal item is confirmed.

{{#if amend}}AMEND SCOPE: {{amend}} -- all phases operate within this constraint only. Every
table carries an explicit scope marker. Phase 2 includes an out-of-scope table.{{/if}}

---

## PRE-EXECUTION CONTRACT

Read before executing Phase 0. This retro is a bidirectional audit system navigable from three
entry points:

**Entry from AUDIT MANIFEST row**: Use the `Derived Views` column to navigate forward to
downstream tables. Downstream tables you may encounter include: Phase 2 coverage table, Phase 3
predicted/actual table, Phase 4 accuracy table, Phase 4 reconciliation table, Phase 7 gap table.

**Entry from downstream section**: Use the `[DERIVED FROM: AUDIT MANIFEST | OPERATION: ...]`
header in any section to navigate backward to the manifest rows that sourced it.

**Entry from contract row**: Use the `Manifest column` field in the contract table to identify
the AUDIT MANIFEST column that will evidence fulfillment of each commitment.

| Mechanism | Structural guarantee -- what is enforced and how | Verified in | Manifest column |
|-----------|--------------------------------------------------|-------------|-----------------|
| Signal window | Bounding date range or sprint scope. Named structural field in manifest header. | Phase 0 SEAL item 1 | Signal window (manifest header field) |
| Mode | AMEND or FRESH flag. AMEND: scope declared top, every table scoped, Phase 2 OOS table. | Phase 0 SEAL item 2; Phase 2 SEAL item 6 if AMEND | Mode (manifest header field) |
| Echo lock | Phase 1 before signal comparison. Echo/Pattern/Why-unexpected locked. Phases 2-9 must not modify. | Phase 1 SEAL items 1-5 | Prediction |
| Manifest derivation | All downstream tables derived as views of AUDIT MANIFEST. Derivation stated per section. | Phase 0 SEAL items 3-7; [DERIVED FROM] headers in all downstream sections | (all columns) |
| Namespace coverage | Fixed 9-row table, COVERED/EMPTY. | Phase 2 SEAL items 1-5 | Namespace |
| Verdict accuracy | Weighted score and count ratio required. Reconciliation required. | Phase 4 SEAL items 4-5; RECONCILIATION TABLE | Verdict |
| Gap identification | W or P rows feed gap table. Material EMPTY namespaces included. | Phase 7 SEAL items 1-2 | Verdict (W or P) |
| Accuracy copy | Phase 6 copies Phase 4 TOTAL. Phase 8 copies Phase 6. No recomputation. | Phase 6 SEAL; Phase 8 SEAL items 2-4 | Verdict (aggregate) |
| Gap inertia columns | Column A = prior belief; Column B = missed discovery; must differ. | Phase 7 SEAL items 3-5 | Verdict (gap rows) |
| Recommendation slots | Three `[slot:X]` tokens; no `[slot:` strings in output. | Phase 7 SEAL item 8 | (generated) |
| Copy guard | Phase 8 COPIED from Phase 6. Three-field SEAL with independent CHECK:/HOW: blocks. | Phase 8 SEAL items 2-4 | Verdict (aggregate) |
| Seal format contracts | All 9 seals: explicit format-string per field. | All 9 SEAL blocks | (all columns) |
| AMEND scope | Every table scoped; Phase 2 OOS table when AMEND set. | Phase 2 SEAL item 6 | (all columns) |

---

## PHASE 0 -- AUDIT MANIFEST

Before running any phase, enumerate all signal artifacts and build the AUDIT MANIFEST. All
downstream tables in this retro are derived from this manifest.

Signal window: [state the date range or sprint scope bounding the predictions being evaluated]
Mode: AMEND ({{amend}}) | FRESH [circle one]

Search simulations/**/[topic]-*-*.md. For each artifact record namespace, prediction, actual
outcome, verdict, and which downstream tables it feeds.

| # | Namespace | Artifact | Prediction (signal's claim) | Actual (post-ship) | Verdict (C/P/W/ND) | Derived Views |
|---|-----------|----------|----------------------------|-------------------|-------------------|---------------|
| 1 | [ns] | [filename] | [what signal claimed] | [what was observed] | C / P / W / ND | [coverage table; predicted/actual (if non-ND); accuracy table (if non-ND); reconciliation table; gap table (if W or P)] |
| ... | | | | | | |

Derived Views values:
- Every row -> "coverage table"
- Non-ND rows -> add "predicted/actual table; accuracy table"
- W or P rows -> add "gap table"
- Every row -> add "reconciliation table"

After completing the manifest, state the navigation check:
  Forward check: "For each manifest row, Derived Views names at least one specific downstream table."
  Backward check: "Each downstream section will carry [DERIVED FROM: AUDIT MANIFEST | OPERATION: ...] header."

PHASE 0 SEAL -- format contract:
  [ ] Signal window: {date range or sprint name} -- named structural field
  [ ] Mode: {AMEND | FRESH} -- named field present
  [ ] Manifest rows: one row per signal artifact
  [ ] Verdict: {C | P | W | ND} per row -- no other values
  [ ] Derived Views: non-blank per row -- names at least one downstream table
  [ ] Forward check statement: present after manifest, confirms Derived Views naming is specific
  [ ] Backward check statement: present after manifest, confirms [DERIVED FROM] headers will appear
  [ ] Canonical name cross-reference: Derived Views entries checked against downstream table names
      listed in Entry 2 of the navigation description above -- informal aliases acceptable if
      intent is clear
All items confirmed against format? PHASE 0 COMPLETE.

---

[PHASE 1 through PHASE 9 and design guarantees: identical structure to V-01, with design
guarantees noting: "PRE-EXECUTION CONTRACT: prose bold-paragraph entry points (not structured
table). Canonical names listed inline in Entry 2 prose (not standalone authority block).
Phase 0 SEAL cross-check references Entry 2 inline list, not a named authority block.
C-44 PARTIAL (intent descriptions, not VERIFIED declarations), C-45 PARTIAL (prose not
structured block), C-46 PARTIAL (inline reference), C-47 PARTIAL (no standalone block)."]
```

---

## V-04 -- Combined: Standalone Registry Block + Named SEAL Cross-Reference

**Axis:** C-47 + C-46 (combined). V-01's **Canonical downstream table set** standalone authority block is added to the preamble. The Phase 0 SEAL gains the explicit cross-reference item from V-02 -- naming the authority block explicitly. Both changes are in non-overlapping structural locations: C-47 lives in the preamble body, C-46 lives in the Phase 0 SEAL.

**Hypothesis:** Zero-interference test. C-47's authority block requires changes only to the ASSESSOR NAVIGATION PREAMBLE section; C-46's SEAL item requires changes only to Phase 0 SEAL. No shared modification surface. Each criterion satisfies its pass condition independently: C-47 has a standalone named authority block; C-46 has a SEAL item that cross-checks against that named block. Both should produce full PASS simultaneously. The FORWARD VERIFIED declaration retains R19-V-05 inline enumeration form -- V-05 will test whether wiring FORWARD VERIFIED to the authority block adds further structural integrity.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Execute
phases in order. Each phase ends with a PHASE SEAL -- a format-contract checklist where every
item specifies the required field and its required value form. Do not proceed past a phase until
every seal item is confirmed.

{{#if amend}}AMEND SCOPE: {{amend}} -- all phases operate within this constraint only. Every
table carries an explicit scope marker. Phase 2 includes an out-of-scope table.{{/if}}

---

## PRE-EXECUTION CONTRACT

Read before executing Phase 0.

### ASSESSOR NAVIGATION PREAMBLE

This audit system is navigable from three entry points. Locate the row matching your starting
position and follow the navigation field.

| # | If you are starting at... | Locate this navigation field | It takes you to... |
|---|--------------------------|-----------------------------|--------------------|
| 1 | Any row in this PRE-EXECUTION CONTRACT | `Manifest column` field (4th column of the table below) | The exact AUDIT MANIFEST column that evidences the commitment in that row |
| 2 | Any row in the AUDIT MANIFEST (Phase 0) | `Derived Views` column (last column of Phase 0 table) | The exact downstream table(s) that receive data from that manifest row |
| 3 | Any downstream section header (Phase 2, 3, 4, 7) | `[DERIVED FROM: AUDIT MANIFEST \| OPERATION: ...]` declaration in the section header | The AUDIT MANIFEST as source for that section |

**Canonical downstream table set** (authority block -- single source of truth for all Derived Views entries):

All Derived Views entries in the AUDIT MANIFEST must use the exact canonical identifiers in this
table. Abbreviations, aliases, and informal labels are not acceptable. This block is referenced
by the Phase 0 SEAL cross-check item.

| Canonical table name | Phase | Populated from |
|---------------------|-------|----------------|
| Phase 2 Signal Coverage Table | 2 | Every manifest row (grouped by Namespace) |
| Phase 3 Predicted vs Actual Table | 3 | Rows with Status = COVERED and non-ND Verdict |
| Phase 4 Namespace Accuracy Table | 4 | Scored manifest rows (Verdict != ND) |
| Phase 4 Reconciliation Table | 4 | All manifest rows (ND rows appear; excluded from denominator) |
| Phase 7 Gap Analysis Table | 7 | Rows with Verdict = W or P; material EMPTY namespaces |

| Mechanism | Structural guarantee -- what is enforced and how | Verified in | Manifest column |
|-----------|--------------------------------------------------|-------------|-----------------|
| Signal window | Bounding date range or sprint scope. Named structural field in manifest header -- not inferred from prose. | Phase 0 SEAL item 1 | Signal window (manifest header field) |
| Mode | AMEND or FRESH flag. AMEND: scope declared top, every table scoped, Phase 2 OOS table. | Phase 0 SEAL item 2; Phase 2 SEAL item 6 if AMEND | Mode (manifest header field) |
| Echo lock | Phase 1 before signal comparison. Echo/Pattern/Why-unexpected locked. Phases 2-9 must not modify. | Phase 1 SEAL items 1-5 | Prediction (Echo is the finding absent from this column) |
| Manifest derivation | All downstream tables derived as views of AUDIT MANIFEST. Derived Views column enables forward navigation; [DERIVED FROM] headers enable backward navigation. | Phase 0 SEAL items 3-8; [DERIVED FROM] headers in all downstream sections | (all columns) |
| Namespace coverage | Fixed 9-row table, COVERED/EMPTY derived by grouping manifest Namespace column. | Phase 2 SEAL items 1-5 | Namespace |
| Verdict accuracy | Weighted score and count ratio required. Reconciliation cross-check required. | Phase 4 SEAL items 4-5; RECONCILIATION TABLE | Verdict |
| Gap identification | W or P manifest rows feed gap table. Material EMPTY namespaces included. | Phase 7 SEAL items 1-2 | Verdict (filter: W or P) |
| Accuracy copy | Phase 6 copies Phase 4 TOTAL. Phase 8 copies Phase 6 verdict. No recomputation. | Phase 6 SEAL; Phase 8 SEAL items 2-4 | Verdict (aggregate) |
| Gap inertia columns | Column A = prior belief; Column B = missed discovery; must not share content per row. | Phase 7 SEAL items 3-5 | Verdict (gap rows) |
| Recommendation slots | Three `[slot:X]` tokens; SEAL confirms no `[slot:` strings survive. | Phase 7 SEAL item 8 | (generated) |
| Copy guard | Phase 8 COPIED from Phase 6. Three-field SEAL each with independent CHECK:/HOW: blocks. | Phase 8 SEAL items 2-4 | Verdict (aggregate) |
| Seal format contracts | All 9 seals: explicit format-string per field; verify value form, not just presence. | All 9 SEAL blocks | (all columns) |
| AMEND scope | Every table has scope marker when AMEND set. Phase 2 OOS table present. | Phase 2 SEAL item 6 | (all columns) |

---

## PHASE 0 -- AUDIT MANIFEST

Before running any phase, enumerate all signal artifacts and build the AUDIT MANIFEST. All
downstream tables are derived from this manifest. The `Derived Views` column enables forward
navigation: an assessor at any manifest row can identify which downstream tables include it
without reading phase specifications. Use ONLY the exact canonical identifiers from the
**Canonical downstream table set** authority block in the ASSESSOR NAVIGATION PREAMBLE.

Signal window: [state the date range or sprint scope bounding the predictions being evaluated]
Mode: AMEND ({{amend}}) | FRESH [circle one]

Search simulations/**/[topic]-*-*.md. For each artifact record namespace, prediction, actual
outcome, verdict, and forward-navigation destinations using canonical table names.

| # | Namespace | Artifact | Prediction (signal's claim) | Actual (post-ship) | Verdict (C/P/W/ND) | Derived Views |
|---|-----------|----------|----------------------------|-------------------|-------------------|---------------|
| 1 | [ns] | [filename] | [what signal claimed] | [what was observed] | C / P / W / ND | [Phase 2 Signal Coverage Table; Phase 3 Predicted vs Actual Table (if non-ND); Phase 4 Namespace Accuracy Table (if non-ND); Phase 4 Reconciliation Table; Phase 7 Gap Analysis Table (if W or P)] |
| ... | | | | | | |

Derived Views assignment rules (use ONLY exact canonical identifiers from the Canonical downstream table set in the ASSESSOR NAVIGATION PREAMBLE):
- Every row -> "Phase 2 Signal Coverage Table"
- Non-ND rows -> add "Phase 3 Predicted vs Actual Table; Phase 4 Namespace Accuracy Table"
- W or P rows -> add "Phase 7 Gap Analysis Table"
- Every row -> add "Phase 4 Reconciliation Table"

After completing the manifest, write the bidirectional navigation verification block:

  FORWARD VERIFIED: Manifest -> downstream direction confirmed. Each manifest row's Derived Views
  column uses exact canonical table names from the set {Phase 2 Signal Coverage Table, Phase 3
  Predicted vs Actual Table, Phase 4 Namespace Accuracy Table, Phase 4 Reconciliation Table,
  Phase 7 Gap Analysis Table}. An assessor reading any manifest row can navigate forward to
  downstream sections without reading phase specifications. Forward navigation confirmed complete.

  BACKWARD VERIFIED: Downstream -> manifest direction confirmed. Each downstream section -- Phase
  2 Signal Coverage Table, Phase 3 Predicted vs Actual Table, Phase 4 Namespace Accuracy Table,
  Phase 4 Reconciliation Table, Phase 7 Gap Analysis Table -- carries a
  [DERIVED FROM: AUDIT MANIFEST | OPERATION: ...] header naming this manifest as its source.
  Backward navigation confirmed complete.

PHASE 0 SEAL -- format contract:
  [ ] Signal window: {date range or sprint name} -- named structural field in manifest header
  [ ] Mode: {AMEND | FRESH} -- named field present; if AMEND, scope carried into all phases
  [ ] Manifest rows: one row per signal artifact; no namespace groups without individual rows
  [ ] Verdict: {C | P | W | ND} per row -- no other values, no blank
  [ ] Derived Views exact canonical names: each entry uses an exact name from the Canonical
      downstream table set authority block -- "Phase 2 Signal Coverage Table" not "Phase 2
      table" or "coverage table"; informal alias = FAIL this item
  [ ] FORWARD VERIFIED declaration: statement beginning with "FORWARD VERIFIED:" present after
      manifest table; explicitly declares manifest -> downstream direction as confirmed; intent
      description without verification assertion = FAIL this item
  [ ] BACKWARD VERIFIED declaration: statement beginning with "BACKWARD VERIFIED:" present after
      manifest table; explicitly declares downstream -> manifest direction as confirmed
  [ ] SEAL-Preamble authority block cross-reference: Derived Views entries in the manifest are
      cross-checked against the **Canonical downstream table set** authority block declared in
      the ASSESSOR NAVIGATION PREAMBLE. The cross-check must name that authority block
      explicitly by its title. Generic "preamble" reference without naming the authority block =
      FAIL this item. Inline enumeration or informal list reference = FAIL this item.
All items confirmed against format? PHASE 0 COMPLETE.

---

[PHASE 1 through PHASE 9: identical to V-01 above.]

---

Execute phases in order: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9. Verify compliance
against PRE-EXECUTION CONTRACT before marking complete.

Design guarantees (audit reference):
- PRE-EXECUTION CONTRACT: ASSESSOR NAVIGATION PREAMBLE with three-row navigation table, followed
  by standalone **Canonical downstream table set** authority block (5 rows, exact identifiers,
  labeled as authority block). Four-column mechanism table follows.
- Phase 0: AUDIT MANIFEST with Signal window, Mode, Verdict, Derived Views per row using exact
  canonical names from the authority block. FORWARD VERIFIED + BACKWARD VERIFIED declarations.
  All downstream sections carry [DERIVED FROM: AUDIT MANIFEST] headers.
  SEAL item 8: explicit cross-check against **Canonical downstream table set** authority block
  by name -- generic preamble reference or inline enumeration = FAIL.
- Phase 1: Echo locked before signal comparison. Pattern and Why-unexpected required.
- Phase 4: Weighted score AND count ratio. RECONCILIATION TABLE required.
- Phase 8: Score COPIED from Phase 6. Three-field SEAL with independent CHECK:/HOW: blocks.
- All 9 seals: explicit format-string per field.
- C-47 satisfied: standalone **Canonical downstream table set** authority block in preamble.
- C-46 satisfied: SEAL item cross-checks manifest Derived Views against the named authority block.
```

---

## V-05 -- Full Integration: Mutual Enforcement via Cross-Binding

**Axis:** Full integration (structural cross-binding). V-04 mechanisms carried forward plus: (1) the FORWARD VERIFIED declaration is upgraded to name the **Canonical downstream table set** authority block explicitly as the source of canonical identifiers; (2) the Derived Views assignment rules text names the authority block as its source; (3) the SEAL cross-check item adds the negative exclusion clause -- "generic preamble reference or inline enumeration = FAIL"; (4) the design guarantees footer is updated to document the mutual enforcement relationship. This creates a closed loop: the authority block is the single source of truth, and every structural reference in the prompt names it by title.

**Hypothesis:** V-04 achieves C-46 and C-47 PASS through structural independence. V-05 closes the remaining drift gap by making the mutual enforcement relationship explicit. In V-04, the FORWARD VERIFIED declaration still uses an inline canonical set enumeration -- a second copy of the canonical names that could theoretically diverge from the authority block over time. V-05 eliminates this second copy by having FORWARD VERIFIED say "canonical identifiers declared in the **Canonical downstream table set** authority block" rather than re-enumerating them inline. This makes the authority block the sole canonical source that all three references (Derived Views rules, FORWARD VERIFIED, SEAL cross-check) point to, satisfying the structural interdependence described in the rubric design logic: "C-47's registry is only structurally enforced when C-46 wires the SEAL to it."

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Execute
phases in order. Each phase ends with a PHASE SEAL -- a format-contract checklist where every
item specifies the required field and its required value form. Do not proceed past a phase until
every seal item is confirmed.

{{#if amend}}AMEND SCOPE: {{amend}} -- all phases operate within this constraint only. Every
table carries an explicit scope marker. Phase 2 includes an out-of-scope table.{{/if}}

---

## PRE-EXECUTION CONTRACT

Read before executing Phase 0.

### ASSESSOR NAVIGATION PREAMBLE

This audit system is navigable from three entry points. Locate the row matching your starting
position and follow the navigation field.

| # | If you are starting at... | Locate this navigation field | It takes you to... |
|---|--------------------------|-----------------------------|--------------------|
| 1 | Any row in this PRE-EXECUTION CONTRACT | `Manifest column` field (4th column of the table below) | The exact AUDIT MANIFEST column that evidences the commitment in that row |
| 2 | Any row in the AUDIT MANIFEST (Phase 0) | `Derived Views` column (last column of Phase 0 table) | The exact downstream table(s) per the **Canonical downstream table set** below |
| 3 | Any downstream section header (Phase 2, 3, 4, 7) | `[DERIVED FROM: AUDIT MANIFEST \| OPERATION: ...]` declaration in the section header | The AUDIT MANIFEST as source for that section |

**Canonical downstream table set** (authority block -- sole canonical source for all Derived Views entries, FORWARD VERIFIED references, and SEAL cross-checks):

All Derived Views entries in the AUDIT MANIFEST, all FORWARD VERIFIED declarations, and all
Phase 0 SEAL cross-check items must use the exact canonical identifiers in this table. This
block is the single source of truth. Do not re-enumerate canonical names inline elsewhere in
this document -- reference this block by name instead. Any drift between this block and inline
enumerations is an integrity failure detectable at SEAL time.

| Canonical table name | Phase | Populated from |
|---------------------|-------|----------------|
| Phase 2 Signal Coverage Table | 2 | Every manifest row (grouped by Namespace) |
| Phase 3 Predicted vs Actual Table | 3 | Rows with Status = COVERED and non-ND Verdict |
| Phase 4 Namespace Accuracy Table | 4 | Scored manifest rows (Verdict != ND) |
| Phase 4 Reconciliation Table | 4 | All manifest rows (ND rows appear; excluded from denominator) |
| Phase 7 Gap Analysis Table | 7 | Rows with Verdict = W or P; material EMPTY namespaces |

| Mechanism | Structural guarantee -- what is enforced and how | Verified in | Manifest column |
|-----------|--------------------------------------------------|-------------|-----------------|
| Signal window | Bounding date range or sprint scope. Named structural field in manifest header -- not inferred from prose. | Phase 0 SEAL item 1 | Signal window (manifest header field) |
| Mode | AMEND or FRESH flag. AMEND: scope declared top, every table scoped, Phase 2 OOS table. | Phase 0 SEAL item 2; Phase 2 SEAL item 6 if AMEND | Mode (manifest header field) |
| Echo lock | Phase 1 before signal comparison. Echo/Pattern/Why-unexpected locked. Phases 2-9 must not modify. | Phase 1 SEAL items 1-5 | Prediction (Echo is the finding absent from this column) |
| Manifest derivation | All downstream tables derived as views of AUDIT MANIFEST. Derivation stated per section. Derived Views column (wired to Canonical downstream table set) enables forward navigation; [DERIVED FROM] headers enable backward navigation. | Phase 0 SEAL items 3-8; [DERIVED FROM] headers in all downstream sections | (all columns) |
| Namespace coverage | Fixed 9-row table, COVERED/EMPTY derived by grouping manifest Namespace column. | Phase 2 SEAL items 1-5 | Namespace |
| Verdict accuracy | Weighted score and count ratio required. Reconciliation cross-check required. | Phase 4 SEAL items 4-5; RECONCILIATION TABLE | Verdict |
| Gap identification | W or P manifest rows feed gap table. Material EMPTY namespaces included. | Phase 7 SEAL items 1-2 | Verdict (filter: W or P) |
| Accuracy copy | Phase 6 copies Phase 4 TOTAL. Phase 8 copies Phase 6 verdict. No recomputation at any stage. | Phase 6 SEAL; Phase 8 SEAL items 2-4 | Verdict (aggregate) |
| Gap inertia columns | Column A = prior belief; Column B = missed discovery; must not share content per row. | Phase 7 SEAL items 3-5 | Verdict (gap rows) |
| Recommendation slots | Three `[slot:X]` tokens; SEAL confirms no `[slot:` strings survive. | Phase 7 SEAL item 8 | (generated) |
| Copy guard | Phase 8 COPIED from Phase 6. Three-field SEAL each with independent CHECK:/HOW: blocks. | Phase 8 SEAL items 2-4 | Verdict (aggregate) |
| Seal format contracts | All 9 seals: explicit format-string per field; verify value form, not just presence. | All 9 SEAL blocks | (all columns) |
| AMEND scope | Every table has scope marker when AMEND set. Phase 2 OOS table present. | Phase 2 SEAL item 6 | (all columns) |

---

## PHASE 0 -- AUDIT MANIFEST

Before running any phase, enumerate all signal artifacts and build the AUDIT MANIFEST. All
downstream tables are derived from this manifest. The `Derived Views` column enables forward
navigation: an assessor at any manifest row can identify which downstream tables include it
without reading phase specifications.

Use ONLY the exact canonical identifiers declared in the **Canonical downstream table set**
authority block in the ASSESSOR NAVIGATION PREAMBLE. Do not use abbreviations, aliases, or
informal labels. Do not re-enumerate canonical names inline -- reference the authority block.

Signal window: [state the date range or sprint scope bounding the predictions being evaluated]
Mode: AMEND ({{amend}}) | FRESH [circle one]

Search simulations/**/[topic]-*-*.md. For each artifact record namespace, prediction, actual
outcome, verdict, and forward-navigation destinations using canonical table names.

| # | Namespace | Artifact | Prediction (signal's claim) | Actual (post-ship) | Verdict (C/P/W/ND) | Derived Views |
|---|-----------|----------|----------------------------|-------------------|-------------------|---------------|
| 1 | [ns] | [filename] | [what signal claimed] | [what was observed] | C / P / W / ND | [Phase 2 Signal Coverage Table; Phase 3 Predicted vs Actual Table (if non-ND); Phase 4 Namespace Accuracy Table (if non-ND); Phase 4 Reconciliation Table; Phase 7 Gap Analysis Table (if W or P)] |
| ... | | | | | | |

Derived Views assignment rules (canonical identifiers from the **Canonical downstream table set**
authority block in the ASSESSOR NAVIGATION PREAMBLE -- use no other names):
- Every row -> "Phase 2 Signal Coverage Table"
- Non-ND rows -> add "Phase 3 Predicted vs Actual Table; Phase 4 Namespace Accuracy Table"
- W or P rows -> add "Phase 7 Gap Analysis Table"
- Every row -> add "Phase 4 Reconciliation Table"

After completing the manifest, write the bidirectional navigation verification block:

  FORWARD VERIFIED: Manifest -> downstream direction confirmed. Each manifest row's Derived Views
  column uses the exact canonical identifiers declared in the **Canonical downstream table set**
  authority block in the ASSESSOR NAVIGATION PREAMBLE. An assessor reading any manifest row can
  navigate forward to downstream sections without reading phase specifications.
  Forward navigation confirmed complete.

  BACKWARD VERIFIED: Downstream -> manifest direction confirmed. Each downstream section in the
  **Canonical downstream table set** -- Phase 2 Signal Coverage Table, Phase 3 Predicted vs
  Actual Table, Phase 4 Namespace Accuracy Table, Phase 4 Reconciliation Table, Phase 7 Gap
  Analysis Table -- carries a [DERIVED FROM: AUDIT MANIFEST | OPERATION: ...] header naming
  this manifest as its source. An assessor reading any downstream section can navigate backward
  to the manifest. Backward navigation confirmed complete.

PHASE 0 SEAL -- format contract:
  [ ] Signal window: {date range or sprint name} -- named structural field in manifest header;
      not inferred from prose
  [ ] Mode: {AMEND | FRESH} -- named field present; if AMEND, scope carried into all phases
  [ ] Manifest rows: one row per signal artifact found; no namespace groups without individual rows
  [ ] Verdict: {C | P | W | ND} per row -- no other values, no blank
  [ ] Derived Views exact canonical names: each Derived Views entry in the manifest uses an exact
      canonical identifier from the **Canonical downstream table set** authority block in the
      ASSESSOR NAVIGATION PREAMBLE. Verify by checking each entry against that block directly --
      do not verify against an inline list or the FORWARD VERIFIED enumeration.
      Non-canonical alias or informal label = FAIL this item.
  [ ] FORWARD VERIFIED declaration: statement beginning with "FORWARD VERIFIED:" present after
      manifest table; explicitly declares manifest -> downstream direction as confirmed AND names
      the **Canonical downstream table set** authority block as the source of canonical identifiers;
      intent description without verification assertion = FAIL; inline enumeration without
      authority block reference = FAIL
  [ ] BACKWARD VERIFIED declaration: statement beginning with "BACKWARD VERIFIED:" present after
      manifest table; explicitly declares downstream -> manifest direction as confirmed;
      future-tense statement without verification assertion = FAIL this item
  [ ] SEAL-Preamble authority block cross-reference: Derived Views entries in the manifest are
      cross-checked against the **Canonical downstream table set** authority block declared in the
      ASSESSOR NAVIGATION PREAMBLE. The cross-check must name that authority block explicitly by
      its title -- "**Canonical downstream table set**". Generic preamble reference ("the preamble
      says...", "per the navigation section"), inline enumeration, or absent cross-check item =
      FAIL this item. Verifying against an inline list rather than the named authority block =
      FAIL this item.
All items confirmed against format? PHASE 0 COMPLETE.

---

PHASE 1 -- ECHO
Run this phase before examining signal accuracy comparisons in Phase 3.

{{#if amend}}[AMEND: {{amend}} only -- outcomes outside this scope excluded from Echo
candidacy]{{/if}}

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
  > **Pattern**: [name from taxonomy or "other: [your name]"] -- [recurring failure mode class -- not Echo restatement]
  > **Why unexpected**: [prior belief contradicted -- what was expected and why reality diverged]

  Taxonomy: adoption-assumption-gap | integration-surface-miss | timing-signal-gap |
  scale-behavior-gap | dependency-chain-miss | unknown-unknown | other: [name]

LOCK: Echo table, Pattern, and Why-unexpected are final. Phases 2-9 may not change them.

PHASE 1 SEAL -- format contract:
  [ ] Echo: {one sentence} OR exact string "No Echo -- all post-ship outcomes were within signal bounds"
  [ ] Nearest signal: {artifact-filename.md} OR exact string "none"
  [ ] Commit relevance: HIGH | MEDIUM | LOW | N/A -- "N/A" only valid when paired with "No Echo"
  [ ] Pattern: "> **Pattern**: {taxonomy-label or "other: name"} -- {failure class description -- not Echo restatement}"
  [ ] Why unexpected: "> **Why unexpected**: {prior belief contradicted -- names what was expected, not just that it was unexpected}"
  {{#if amend}}[ ] AMEND scope marker present immediately above table{{/if}}
All items confirmed against format? PHASE 1 COMPLETE.

---

PHASE 2 -- SIGNAL INVENTORY
[DERIVED FROM: AUDIT MANIFEST | OPERATION: group by Namespace, count rows per group, assign COVERED if count >= 1 else EMPTY]

Produce a fixed 9-row namespace coverage table. Every namespace gets exactly one row. Derive
from Phase 0 AUDIT MANIFEST -- do not re-examine artifacts independently.

{{#if amend}}[AMEND: {{amend}} only -- out-of-scope artifacts go to the OOS table below]{{/if}}

| Namespace | Status          | Artifact count | Primary artifact (or "--") | Prediction theme (or "--") |
|-----------|-----------------|----------------|---------------------------|---------------------------|
| scout     | COVERED / EMPTY | N              | [filename or "--"]         | [one phrase or "--"]       |
| draft     | COVERED / EMPTY | N              | [filename or "--"]         | [one phrase or "--"]       |
| review    | COVERED / EMPTY | N              | [filename or "--"]         | [one phrase or "--"]       |
| flow      | COVERED / EMPTY | N              | [filename or "--"]         | [one phrase or "--"]       |
| trace     | COVERED / EMPTY | N              | [filename or "--"]         | [one phrase or "--"]       |
| prove     | COVERED / EMPTY | N              | [filename or "--"]         | [one phrase or "--"]       |
| listen    | COVERED / EMPTY | N              | [filename or "--"]         | [one phrase or "--"]       |
| program   | COVERED / EMPTY | N              | [filename or "--"]         | [one phrase or "--"]       |
| topic     | COVERED / EMPTY | N              | [filename or "--"]         | [one phrase or "--"]       |
| TOTAL     |                 | N              |                           |                           |

{{#if amend}}Out-of-scope artifacts (excluded per AMEND constraint):
| Namespace | Artifact | Excluded because |
|-----------|----------|-----------------|
| [name] | [filename] | [outside {{amend}} scope] |
If none excluded: "No artifacts excluded -- all in scope."
{{/if}}

PHASE 2 SEAL -- format contract:
  [ ] All 9 namespace rows in exact order: scout, draft, review, flow, trace, prove, listen, program, topic
  [ ] Status: {COVERED} or {EMPTY} per row -- no other value, no blank
  [ ] Artifact count: {integer} per row -- 0 valid for EMPTY
  [ ] Primary artifact: {filename.md} or "--" -- not blank
  [ ] TOTAL row: present with {integer} in Artifact count cell
  {{#if amend}}[ ] OOS table: present immediately after main table -- even if "No artifacts excluded -- all in scope."{{/if}}
  [ ] Derived From header: "[DERIVED FROM: AUDIT MANIFEST | OPERATION: group by Namespace...]" present above table
All items confirmed against format? PHASE 2 COMPLETE.

---

PHASE 3 -- PREDICTED VS ACTUAL
[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter rows where Namespace is COVERED; surface Prediction, Actual, Verdict per namespace]

For each namespace with Status = COVERED in Phase 2. Derive from AUDIT MANIFEST rows -- do
not independently re-evaluate predictions.

{{#if amend}}[AMEND: {{amend}} only]{{/if}}

| Namespace | Predicted (signals' collective claim post-ship) | Actual (what was observed) | Match: C / P / W / ND |
|-----------|------------------------------------------------|---------------------------|----------------------|
| [name] | [from AUDIT MANIFEST Prediction column] | [from AUDIT MANIFEST Actual column] | [from AUDIT MANIFEST Verdict column] |

C = Correct, P = Partial (direction right, magnitude/timing off), W = Wrong, ND = No post-ship data.

PHASE 3 SEAL -- format contract:
  [ ] Row count: one row per COVERED namespace from Phase 2 -- no omissions, no extras
  [ ] Predicted: {one phrase or sentence} -- not blank, not "N/A", not "unknown"
  [ ] Actual: {one phrase or sentence} -- not blank, not "N/A", not "unknown"
  [ ] Match: one of exactly: C | P | W | ND
  [ ] Derived From header: "[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter COVERED namespaces]" present above table
  {{#if amend}}[ ] Scope marker present above table{{/if}}
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
| Backward | W={W}; +P={P}; +C={C}; total={N} | [recovery arithmetic shown] | {N} | C=total-W-P={C} | YES / NO |

Reconciliation result: Forward={N}; Backward={N}; Match: YES (proceed) / NO (recheck manifest).

PHASE 4 SEAL -- format contract:
  [ ] Row count: one row per Phase 3 namespace -- no omissions
  [ ] C, P, W, ND: {integer} per cell -- blank invalid; 0 valid
  [ ] Weighted score: {number}/100 per row OR blank with note "0 scored signals"
  [ ] TOTAL row: present, format: {number}/100
  [ ] Count-based ratio: stated in format "{N}/{M} = {X}%" immediately below scoring table
  [ ] RECONCILIATION TABLE: present with Forward and Backward rows and result row
  [ ] Reconciliation result: Match = YES before proceeding -- NO = do not continue
  [ ] Derived From header: "[DERIVED FROM: AUDIT MANIFEST | OPERATION: count Verdict values...]" present above scoring table
  {{#if amend}}[ ] Scope marker present{{/if}}
All items confirmed against format? PHASE 4 COMPLETE.

---

PHASE 5 -- CONFLICT AUDIT
Mandatory. Always produces exactly one of two outputs.

Review the locked Phase 1 Echo. Does any Phase 3 verdict or Phase 4 score suggest the Echo
should name a different finding?

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
Draw weighted score from Phase 4 TOTAL row. Draw count ratio from Phase 4 count-based statement.
Do not recalculate either number.

"Signal accuracy for [topic]: [TOTAL]/100 -- [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]. Count accuracy: [N/M = X%]."

PHASE 6 SEAL -- format contract:
  [ ] Verdict sentence: present in exact format "Signal accuracy for {topic}: {score}/100 -- {STRONG|ADEQUATE|WEAK}. Count accuracy: {N}/{M} = {X}%."
  [ ] Weighted score: drawn from Phase 4 TOTAL row -- same number, not recalculated
  [ ] Count ratio: drawn from Phase 4 count-based statement -- same values, not recalculated
  [ ] Tier label: STRONG if >= 75 | ADEQUATE if 50-74 | WEAK if < 50 -- must match stated score
All items confirmed against format? PHASE 6 COMPLETE.

---

PHASE 7 -- GAP ANALYSIS
[DERIVED FROM: AUDIT MANIFEST | OPERATION: filter rows where Verdict = W or P; add EMPTY namespaces where absence is material]

For each namespace scoring W or P in Phase 3, and each EMPTY namespace (Phase 2) where absence
is material to the commit decision.

{{#if amend}}[AMEND: {{amend}} only -- gaps outside this constraint excluded]{{/if}}

Column A = "Assumption held without evidence": the inertia belief that made this gap invisible
before commit. WHY the gap existed. Framed as prior belief ("We assumed X"), not an outcome.
Column B = "Would have surfaced": the discovery missed. WHAT was missed. Different from Column A.

| Gap (signal type absent) | Namespace | Assumption held without evidence [A] | Skill to run | Would have surfaced [B] | Changed commit? YES / NO |
|--------------------------|-----------|--------------------------------------|-------------|-------------------------|--------------------------|
| [type] | [ns] | [prior belief -- "We assumed X" -- NOT an outcome] | [/exact-skill-name] | [discovery -- distinct from Column A] | YES / NO |

No gaps: "No gaps -- signal coverage was sufficient for this commit decision."

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

COPY the accuracy score from the Phase 6 verdict sentence into the "This score" cell. Do not
recompute. Label the cell: COPY-VERIFIED [source: Phase 6 verdict].

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [ref or "none"] | [score or "--"] | {N}/100 -- COPY-VERIFIED [source: Phase 6 verdict] | [+/-N or "--"] | up improving / down degrading / = stable |

No prior retro: "First retro for this topic -- this score establishes the calibration baseline."

PHASE 8 SEAL -- format contract:
  [ ] Prior retro: {topic}/{YYYY-MM-DD} OR "none"; Delta: {+/-N or 0 or "--"}; Trend: one of three values or "first retro" statement

  [ ] This score -- independent verification:
      CHECK: "This score" cell non-blank, {number}/100 format.
      HOW: Read "This score" cell in Phase 8 table only. Do not read Phase 6 or Phase 4.
      Format required: {number}/100 -- blank or wrong format = FAIL.

  [ ] COPY-VERIFIED -- independent verification:
      CHECK: Score in "This score" was copied from Phase 6, not computed.
      HOW: Open Phase 6. Read verdict sentence. Find score before "/100". Compare to "This score"
      value. "COPY-VERIFIED" label must be present. Do not read Phase 4.
      Format required: cell label contains "COPY-VERIFIED" -- absent label = FAIL.

  [ ] COPY-SOURCE -- independent verification:
      CHECK: "This score" cell names Phase 6 verdict as source, not Phase 4.
      HOW: Read cell label. Confirm it names "Phase 6 verdict". Phase 4 reference or absent = FAIL.
      Format required: label contains "source: Phase 6 verdict" -- alternative source = FAIL.

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

Execute phases in order: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9. Verify compliance
against PRE-EXECUTION CONTRACT before marking complete.

Design guarantees (audit reference):
- PRE-EXECUTION CONTRACT: ASSESSOR NAVIGATION PREAMBLE with three-row navigation table (entry
  points 1/2/3). Entry point 2 references the **Canonical downstream table set** authority block
  by name. Standalone **Canonical downstream table set** authority block (5 rows, exact canonical
  identifiers, labeled as sole canonical source for Derived Views, FORWARD VERIFIED, and SEAL
  cross-checks). Four-column mechanism table follows (Mechanism / Guarantee / Verified in /
  Manifest column).
- Phase 0: AUDIT MANIFEST with Signal window, Mode, Verdict, Derived Views per row. Derived
  Views assignment rules reference the **Canonical downstream table set** authority block by
  name -- no inline re-enumeration. FORWARD VERIFIED declaration names the **Canonical downstream
  table set** authority block as the source of canonical identifiers. BACKWARD VERIFIED
  declaration. SEAL item 8 (SEAL-Preamble authority block cross-reference) explicitly names the
  **Canonical downstream table set** block -- generic preamble reference or inline enumeration
  = FAIL. All downstream sections carry [DERIVED FROM: AUDIT MANIFEST] headers.
- Phase 1: Echo locked before signal comparison. Pattern and Why-unexpected required.
- Phase 4: Weighted score AND count ratio. RECONCILIATION TABLE required.
- Phase 8: Score COPIED from Phase 6. Three-field SEAL with independent CHECK:/HOW: blocks.
- All 9 seals: explicit format-string per field.
- C-47 PASS: standalone **Canonical downstream table set** authority block in preamble below
  three-entry-point table; not entry-point prose; not inline enumeration.
- C-46 PASS: Phase 0 SEAL item 8 cross-checks Derived Views against the **Canonical downstream
  table set** authority block by name; wired to C-47 block; non-applicable if C-47 block absent.
- Mutual enforcement: C-47 registry + C-46 SEAL + FORWARD VERIFIED all reference the same named
  authority block; drift caught at SEAL time via item 8, not discovered during audit.
```

---

## Variation Axis Selection Reference

| Axis | Label | Design question |
|------|-------|----------------|
| J | C-47 standalone authority block | Does promoting the canonical name list from inline enumeration to a standalone named first-class block in the preamble satisfy C-47 independently of SEAL wiring? |
| K | C-46 named SEAL cross-reference | Does a SEAL item that names the authority block explicitly (but where the block is absent) trigger C-46 N/A correctly, confirming the prerequisite relationship? |
| L | Negative register control | Do inline authority (prose sentence in entry-point row) and informal SEAL cross-reference both produce PARTIAL, confirming structural enforcement distinguishes PASS from PARTIAL? |

Single-axis runs: V-01 (J), V-02 (K -- N/A control), V-03 (L -- negative control)
Combinations: V-04 (J+K), V-05 (J+K + FORWARD VERIFIED cross-binding + entry point 2 named reference)

Base mechanisms in all variations: all C-22 through C-45 integrations from R19-V-05
Rubric in scope: `simulations/quest/rubrics/topic-retro-rubric-v18-2026-03-17.md`
