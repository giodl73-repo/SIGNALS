---
skill: quest-variate
skill_target: topic-echo
date: 2026-03-16
round: 20
rubric: v20
rubric_file: simulations/quest/rubrics/topic-echo-rubric-v20-2026-03-16.md
rubric_max: 365
---

# Variations: `topic:echo` -- Round 20 (2026-03-16)

**Rubric:** v20 (2026-03-16) | **Criteria:** 63 (5 essential / 3 recommended / 55 aspirational)

---

## Design Context

R19 V-05 achieves 350/350 under v19. All three R19 closure-layer patterns --
GATE-TOKEN-REGISTRY (C-58), MANIFEST-TOKEN-INLINE-EVIDENCE-SUFFIX (C-59), CROSS-LAYER CITATION
CONSISTENCY PROTOCOL (C-60) -- are present and formally declared. Under v20, R19 V-05 scores
365 (+15 delta). The three new v20 criteria are not new requirements -- they name structural
properties that R19 V-05 already exhibits. Their identification closes the R19 layer by capturing
the currency, comprehensiveness, and contract-parity gaps that appear at the intersection of
C-58+C-60, C-59+C-60, and C-60 alone.

**What the three R20 criteria require:**

- **C-61 (GATE-TOKEN-REGISTRY-COVERS-DERIVED-GATE, requires C-58+C-60):** When C-60 is satisfied,
  a fourth gate token (GT-04: CROSS-CITATION-CONSISTENT) is produced at Step 9. A C-58-compliant
  registry designed for the three-token world of C-55 does not automatically include GT-04. C-61
  requires the registry to self-extend: GT-04 must be listed with its step location (Step 9) and
  prerequisite criterion (C-60). Without this, token completeness for a four-token artifact cannot
  be verified by diff against the registry -- only by full-artifact scan. A registry accurate for
  GT-01..GT-03 but not current for GT-04 satisfies C-58 but fails C-61.

- **C-62 (TOKEN-CONTENT-REQUIREMENT-COMPREHENSIVE, requires C-59+C-60):** TOKEN CONTENT REQUIREMENT
  declares format contracts for gate tokens. C-55 required contracts for GT-01..GT-03. When C-60
  introduces GT-04, TOKEN CONTENT REQUIREMENT must remain comprehensive. A section that covers
  GT-01..GT-03 but omits GT-04's format contract fails C-62. A reader consulting TOKEN CONTENT
  REQUIREMENT cannot verify what columns GT-04's per-pair table must include, how the MATCH
  assertion must be stated, or what count the token must carry. C-62 requires GT-04's format
  contract alongside the three original tokens.

- **C-63 (CROSS-CITATION-TRAVERSAL-FREE-EXPLICIT, requires C-60):** C-55 established the
  self-certifying standard: each gate token's inline specifics must be sufficient to verify its
  pass condition without consulting underlying artifact sections. C-60 introduced GT-04 but did
  not require the verification contract to be stated explicitly as traversal-free. Without an
  explicit note, a reviewer new to the artifact cannot confirm from text alone whether
  CROSS-CITATION-CONSISTENT can be verified without consulting the STILL-LIVE FILTER or manifest
  table. C-63 requires Step 9 to carry an explicit verification note naming what sections are
  NOT required -- in parity with the self-certifying contracts of GT-01..GT-03.

**Gaps in R19 V-04 (the highest non-full-integration R19 variation) under v20:**

R19 V-04 satisfies C-58 (registry for GT-01..GT-03) and C-59 (MANIFEST-COMPLETE extended) but
not C-60 (no Step 9). Since all three R20 criteria require C-60, R19 V-04 scores 0 delta under
v20. R20 variations must all include C-60 as a base and then vary on C-61/C-62/C-63.

**R20 variation axes:**

- **Axis A (C-61):** GATE-TOKEN-REGISTRY self-extends for GT-04: lists GT-04 with step location
  Step 9 and prerequisite C-60. Token completeness for a four-token artifact is diff-detectable
  against the registry.

- **Axis B (C-62):** TOKEN CONTENT REQUIREMENT extended to cover all four gate tokens. GT-04
  (CROSS-CITATION-CONSISTENT) receives a full format contract: count checked, per-pair assertion,
  MATCH requirement stated, hard gate on MISMATCH.

- **Axis C (C-63):** Step 9 carries an explicit verification note naming the sections that are
  NOT required for verification: STILL-LIVE FILTER and CITATION-COMPLETENESS-MANIFEST. The note
  names both sections explicitly, making the traversal-free property as explicit as the
  self-certifying contracts of GT-01..GT-03.

**Predicted R20 scoring:**

| Variation | C-61 | C-62 | C-63 | Predicted v20 score |
|-----------|:----:|:----:|:----:|:-------------------:|
| V-01 (Axis A) | PASS | FAIL | FAIL | 355 |
| V-02 (Axis B) | FAIL | PASS | FAIL | 355 |
| V-03 (Axis C) | FAIL | FAIL | PASS | 355 |
| V-04 (A+B) | PASS | PASS | FAIL | 360 |
| **V-05 (A+B+C)** | **PASS** | **PASS** | **PASS** | **365** |

**Scoring rationale:**

- **V-01**: Registry extended for GT-04 with step location and prerequisite (C-61 PASS: C-58
  satisfied in all R20 variations; C-60 satisfied in all R20 variations; GT-04 listed). TOKEN
  CONTENT REQUIREMENT covers GT-01..GT-03 only; GT-04 format contract absent (C-62 FAIL). Step 9
  executes cross-layer check without explicit traversal-free note (C-63 FAIL). Net: 350+5 = 355.

- **V-02**: GATE-TOKEN-REGISTRY lists GT-01..GT-03 only; GT-04 absent despite C-58+C-60 both
  satisfied (C-61 FAIL). TOKEN CONTENT REQUIREMENT carries full GT-04 format contract (C-62 PASS:
  C-59+C-60 both satisfied). Step 9 without explicit verification note (C-63 FAIL). Net: 350+5 = 355.

- **V-03**: GATE-TOKEN-REGISTRY lists GT-01..GT-03 only (C-61 FAIL). TOKEN CONTENT REQUIREMENT
  covers GT-01..GT-03 only (C-62 FAIL). Step 9 carries explicit verification note naming
  STILL-LIVE FILTER and CITATION-COMPLETENESS-MANIFEST as not required (C-63 PASS: C-60 satisfied
  + explicit note present). Net: 350+5 = 355.

- **V-04**: Registry extended for GT-04 (C-61 PASS). TOKEN CONTENT REQUIREMENT covers all four
  tokens including GT-04 format contract (C-62 PASS). Step 9 executes cross-layer check but
  carries no explicit verification note (C-63 FAIL). Net: 350+10 = 360.

- **V-05**: All three axes satisfied. Registry includes GT-04 (C-61 PASS). TOKEN CONTENT
  REQUIREMENT covers all four tokens (C-62 PASS). Step 9 carries explicit traversal-free note
  (C-63 PASS). Net: 350+15 = 365 = max composite.

**Coherence:** All three R20 criteria require C-60 as prerequisite. C-60 introduces GT-04. C-61
makes the registry current for GT-04. C-62 makes the token format contracts comprehensive for
GT-04. C-63 makes the verification contract for GT-04 explicit. Together they close the
currency-comprehensiveness-contract-parity gap that appears when C-60 is added to a C-58+C-59 base.

**Gate chain extended:** ... -> R18 token inventory declared, manifest token extended for
inline-evidence, cross-layer citation consistent -> R19 registry self-extends for derived gate
tokens, token format contracts comprehensive, cross-citation verification contract traversal-free
explicit.

---

## V-01 -- Axis A: Registry Covers Derived Gate (C-61 targeted; C-62 C-63 absent)

**Variation axis:** Output format -- GATE-TOKEN-REGISTRY self-extends for GT-04 (Axis A for C-61).
TOKEN CONTENT REQUIREMENT covers GT-01..GT-03 only; GT-04 format contract not declared (C-62
absent). Step 9 executes cross-layer check but carries no explicit traversal-free verification
note (C-63 absent). All R19 properties preserved: C-58 registry for GT-01..GT-03 now extended
to GT-04, C-59 MANIFEST-COMPLETE suffix, C-60 Step 9 cross-layer check.

**Hypothesis:** When the registry lists all four gate tokens (GT-01..GT-04), token completeness
is diff-detectable for the full four-token artifact: a missing GT-04 is identifiable against the
registry without artifact scan. However, a reviewer consulting TOKEN CONTENT REQUIREMENT to verify
GT-04's format contract finds no specification -- the format-contract gap is invisible from the
section alone. And a reviewer checking Step 9's verification scope cannot confirm from text alone
whether CROSS-CITATION-CONSISTENT is traversal-free. C-61 closes the registry-currency gap; the
C-62 and C-63 gaps remain open.

**Expected v20 score:** 355 (C-61 PASS, C-62 FAIL, C-63 FAIL)

---

Topic: `{topic}`

Synthesize what was unexpected. Three roles at three exclusive phase boundaries. Every structural
commitment is named, formal, and auditable from output. This is not a summary. This is not a list
of findings. This is the correction register: what the team believed, what the signals proved wrong,
and what the next team must inherit as tested knowledge -- with every provenance claim traceable to
the artifact that generated it.

---

### GATE-TOKEN-REGISTRY [AXIS A -- C-61: REGISTRY COVERS DERIVED GATE]

Expected gate tokens for this artifact. Token absence is detectable by diff against this registry
without full-artifact traversal. A listed token absent from the artifact is missing. A token not
listed here should not appear as a gate token.

| Token-ID | Canonical Name | Step | Prerequisite Criterion |
|----------|----------------|------|------------------------|
| GT-01 | MANIFEST-COMPLETE | Step 8 | C-52 (citation-completeness manifest exhaustive) |
| GT-02 | CONSUMER-INDEX-COMPLETE | Step 7 | C-53 (declaring-section consumer index populated) |
| GT-03 | CHAIN-GROUNDING-COMPLETE | Step 7 | C-54 (citation chain PBI grounding verified) |
| GT-04 | CROSS-CITATION-CONSISTENT | Step 9 | C-60 (cross-layer citation consistency verified) |

Registry declared before Step 0. Diff GT-01..GT-04 against emitted tokens to verify completeness.
GT-04 is a derived gate token: it is produced when C-60 is satisfied at Step 9. A registry that
lists only GT-01..GT-03 fails to account for GT-04 and cannot serve as a diff-auditable inventory
for a four-token artifact.

---

### Roles

**Enforcement Framer (EF)** -- Step 0 exclusively.

```
ENFORCEMENT FRAMER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Constraint architecture only. Produces ENFORCEMENT
              MECHANISM DECLARATION at Step 0. Sets the structural
              rules downstream roles must follow. Does not execute
              any downstream step.
Input:        Scope constraints + structural directives from this
              prompt.
Out-of-scope: Any output beyond the ENFORCEMENT MECHANISM
              DECLARATION. Correction register content is IA scope.
Orienting:    "What rules must hold for this artifact to be
              non-defeatable?"
Phase scope:  Step 0 only.
----------------------------------------------------------------------
```

**Belief Cartographer (BC)** -- Step 1 exclusively.

```
BELIEF CARTOGRAPHER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Prior belief inventory only. Produces PBI and BC-
              COVERAGE-RECORD at Step 1. Executes [SCAN], [FREEZE],
              [COVERAGE AUDIT] sub-phases in declared order.
Input:        Signal artifacts for {topic} (read-only).
Out-of-scope: Any step beyond Step 1. Correction register content
              is IA scope.
Orienting:    "What did the team believe before the signals were
              gathered?"
Phase scope:  Step 1 only.
----------------------------------------------------------------------
```

**Institutional Archaeologist (IA)** -- Steps 2-9.

```
INSTITUTIONAL ARCHAEOLOGIST -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     False-assumption recovery. Correction register only.
              Each IA stage exit (Steps 2-6) produces a PHASE-
              HANDOVER-[N] table before advancing. At Step 7, emit
              CONSUMER-INDEX-COMPLETE (GT-02) and CHAIN-GROUNDING-
              COMPLETE (GT-03) as INDEPENDENT tokens per
              GATE-INDEPENDENCE-ENFORCED -- combined tokens at this
              boundary are non-conforming. Each token self-certifying
              per TOKEN CONTENT REQUIREMENT. At Step 8, produce the
              CITATION-COMPLETENESS-MANIFEST; MANIFEST-COMPLETE (GT-01)
              carries the C-59 inline-evidence suffix -- self-certifying
              for both citation accounting and inline-evidence presence;
              TYPE-C STATUS CELL carries confirming artifact per
              MANIFEST-ROW-INLINE-EVIDENCE. At Step 9, execute the
              Cross-Layer Citation Consistency Check: compare each
              TYPE-C Belief-Ref artifact against its STATUS CELL
              artifact per pair; emit CROSS-CITATION-CONSISTENT (GT-04)
              only when all rows MATCH. Four gate tokens required (see
              GATE-TOKEN-REGISTRY); any absent or non-conforming token
              is an incompletion.
Input:        Signal artifacts + frozen PBI (read-only).
Out-of-scope: PBI authorship (frozen). Enforcement section (immutable).
Orienting:    "What would the next team build wrong?"
Phase scope:  Steps 2-9 only.
----------------------------------------------------------------------
```

**Phase Handover Schema (universal -- all 7 exits, Steps 0-6):**

Six required rows, fixed field names:

| Field | Content |
|-------|---------|
| Phase-exiting | [role + step] |
| Phase-entering | [role + step] |
| Artifacts-produced | [list of outputs produced in this phase] |
| Constraints-carried | [active constraints entering the next phase] |
| Registry-Ref | [T-ID from Phase Transition Registry] |
| Notes | [any handover-specific conditions] |

---

#### TOKEN CONTENT REQUIREMENT [C-55 -- GT-01..GT-03 ONLY; GT-04 FORMAT CONTRACT ABSENT]

Every gate token emitted in this artifact must carry inline specifics sufficient to verify its
pass condition without consulting the underlying artifact sections. This requirement applies to
gate tokens GT-01, GT-02, and GT-03 declared in the GATE-TOKEN-REGISTRY.

**Required format for MANIFEST-COMPLETE (GT-01) -- extended for C-59:**

```
MANIFEST-COMPLETE: CIT-[N1]..CIT-[N2] [K] TYPE-A RESOLVED,
  CIT-[M1]..CIT-[M2] [L] TYPE-B RESOLVED,
  CIT-[P1]..CIT-[P2] [Q] TYPE-C RESOLVED
    (confirming artifact INLINE in all [Q] rows) --
  citation-completeness and inline-evidence presence verified;
  no document traversal required to confirm all addresses resolve
  or that all TYPE-C rows carry confirming artifacts.
```

A token whose TYPE-C count omits the inline-evidence suffix fails C-59. The suffix count [Q]
must match the actual TYPE-C row count in the manifest table.

**Required format for CONSUMER-INDEX-COMPLETE (GT-02):**

```
CONSUMER-INDEX-COMPLETE: [Schema-1 name] [F-ID1]..[F-IDn] Consumer-Ref POPULATED,
  [Schema-2 name] [T-ID1]..[T-IDn] Consumer-Ref POPULATED,
  [Schema-3 name] [MUST-ID1]..[MUST-IDn] Consumer-Ref POPULATED --
  bidirectional navigability confirmed across all three axes.
```

Three tables named individually with ID ranges. A token naming only "all consumer refs populated"
without table enumeration fails.

**Required format for CHAIN-GROUNDING-COMPLETE (GT-03):**

```
CHAIN-GROUNDING-COMPLETE: Belief-Ref cells EXTENDED (all MUST-[N] carry confirming
  artifact reference), F-BCR-4 SPECIFIC (names PB-[NN] through PB-[NN]) --
  citation chain verified to evidence; both C-54 conditions confirmed.
```

Both condition labels must be present. A token confirming only one condition fails.

_(GT-04 format contract: see Step 9 Cross-Layer Citation Consistency Protocol for GT-04
emission conditions. TOKEN CONTENT REQUIREMENT does not declare GT-04's format contract.)_

---

#### GATE-INDEPENDENCE-ENFORCED [C-56]

At any step boundary where two gate tokens are co-located, each token must be emitted as an
independent, separately labeled token. A combined token carrying two gate conditions at a single
boundary is non-conforming. Step 7 application: GT-02 and GT-03 must be separate independent
tokens. A combined CONSUMER-INDEX-COMPLETE + CHAIN-GROUNDING-COMPLETE token at Step 7 is
non-conforming.

---

#### MANIFEST-TOKEN-INLINE-EVIDENCE-SUFFIX [C-59]

The MANIFEST-COMPLETE token must self-certify both citation accounting (C-52) and inline-evidence
presence (C-57) from token text alone. The C-59 suffix `(confirming artifact INLINE in all [Q] rows)`
must appear in the TYPE-C RESOLVED entry. A MANIFEST-COMPLETE token that states `[Q] TYPE-C RESOLVED`
without the inline-evidence suffix fails C-59. The suffix count [Q] must match the manifest
table's actual TYPE-C row count.

---

#### MANIFEST-ROW-INLINE-EVIDENCE [C-57]

Each TYPE-C row in the CITATION-COMPLETENESS-MANIFEST must carry the confirming artifact directly
in its STATUS CELL. FORMAT: `RESOLVED (confirmed false by: [artifact name, namespace, date])`.
A bare `RESOLVED` in any TYPE-C STATUS CELL fails. The confirming artifact in the Target Address
column only (not in STATUS CELL) also fails.

---

#### Phase Transition Registry [C-50 -- Consumer-Ref column]

| T-ID | Phase | Output artifact | Consuming step | Consumer-Ref |
|------|-------|----------------|----------------|--------------|
| T-00 | EF: Step 0 | ENFORCEMENT MECHANISM DECLARATION | Step 1 (BC) | BC-Step 1 |
| T-01 | BC: Step 1 | PBI + BC-COVERAGE-RECORD | Step 2 (IA) | IA-Step 2 |
| T-02 | IA: Step 2 | HANDLE LEDGER | Step 3 (IA) | IA-Step 3 |
| T-03 | IA: Step 3 | STILL-LIVE FILTER + PHASE-HANDOVER-3 | Step 4 (IA) | IA-Step 4 |
| T-04 | IA: Step 4 | Entry Gate blocks | Step 5 (IA) | IA-Step 5 |
| T-05 | IA: Step 5 | Chain Integrity Audit | Step 6 (IA) | IA-Step 6 |
| T-06 | IA: Step 6 | Rules of Thumb | Step 7 (IA) | IA-Step 7 |

---

### BC-STEP1-PROTOCOL

Three sub-phases in order. Do not advance until the current sub-phase is complete.

**[SCAN]** Read all signal artifacts for `{topic}`. List every artifact found: name, namespace, date.

**[FREEZE]** Commit the artifact list. No new artifacts are added after this point.
`COMMIT-SCAN: [N] artifacts found and listed.`

**[COVERAGE AUDIT]** For each artifact: does it contain a prior belief the team held? Annotate.
`COMMIT-FREEZE: coverage audit complete. PBI ready.`

#### BC-COVERAGE-RECORD Schema [C-46/C-49 -- field-IDs + Consumer-Ref; F-BCR-4 specific format]

| Field-ID | Field Name | Content | Consumer-Ref |
|----------|-----------|---------|--------------|
| F-BCR-1 | Artifact count | [N] total artifacts | IA-Step 2 |
| F-BCR-2 | Namespace coverage | [namespaces represented] | IA-Step 2 |
| F-BCR-3 | Date range | [earliest] to [latest] | IA-Step 2 |
| F-BCR-4 | PBI scope | [names specific PB-[NN] through PB-[NN] entries by ID range and source material -- generic sentence fails C-54 condition 2] | IA-Step 7 |

F-BCR-4 must name specific PBI entries by ID range. "All prior beliefs captured" fails.
"PB-01 through PB-12 from [namespace] artifacts" passes.

---

### Steps 0-6

_(Each step produces a PHASE-HANDOVER table at exit. All tables use the 6-row Phase Handover
Schema with Registry-Ref row citing the T-ID from the Phase Transition Registry. All handover
tables carry Consumer-Ref entries. Steps 0-6 structure identical to R19 V-05 base.)_

### Step 3 Extension -- STILL-LIVE FILTER [C-51 extended Belief-Ref + C-53 Consumer-Ref]

Each row: MUST-ID + Scope + Action + Constraint + extended Belief-Ref + Consumer-Ref columns.

Extended Belief-Ref format: `PB-[NN] (confirmed false by: [artifact name, namespace, date])`.
A bare `PB-[NN]` without confirming artifact reference fails C-54 condition 1. A Belief-Ref
that names only an artifact type without name and date fails.

Consumer-Ref column: names the consuming step (IA-Step 7 or IA-Step 8) for each MUST row.

---

### Step 7 -- [IA] Hierarchy, Distillation, and Dual-Gate Emission [C-53+C-54+C-55+C-56]

_(Hierarchy and distillation content identical to R19 V-05 base.)_

After artifact content is complete, emit both Step 7 completeness gates as INDEPENDENT
self-certifying tokens per GATE-INDEPENDENCE-ENFORCED and TOKEN CONTENT REQUIREMENT:

Gate 1 (C-53) -- CONSUMER-INDEX-COMPLETE (GT-02):

`CONSUMER-INDEX-COMPLETE: BC-COVERAGE-RECORD Schema F-BCR-1..F-BCR-4 Consumer-Ref POPULATED, Phase Transition Registry T-00..T-06 Consumer-Ref POPULATED, STILL-LIVE FILTER MUST-1..MUST-4 Consumer-Ref POPULATED -- bidirectional navigability confirmed across all three axes.`

Gate 2 (C-54) -- CHAIN-GROUNDING-COMPLETE (GT-03):

`CHAIN-GROUNDING-COMPLETE: Belief-Ref cells EXTENDED (all MUST-[N] carry confirming artifact reference), F-BCR-4 SPECIFIC (names PB-[NN] through PB-[NN]) -- citation chain verified to evidence; both C-54 conditions confirmed.`

These two tokens are at the same step boundary. Per GATE-INDEPENDENCE-ENFORCED, they are
emitted as separate tokens. A combined token is non-conforming.

---

### Step 8 -- [IA] Citation-Completeness Manifest [C-52+C-55+C-57+C-59]

Produce CITATION-COMPLETENESS-MANIFEST. Apply all active declarations:
- TOKEN CONTENT REQUIREMENT + MANIFEST-TOKEN-INLINE-EVIDENCE-SUFFIX: MANIFEST-COMPLETE (GT-01)
  carries C-59 inline-evidence suffix.
- MANIFEST-ROW-INLINE-EVIDENCE: TYPE-C STATUS cells carry confirming artifact.

```
CITATION-COMPLETENESS-MANIFEST PROTOCOL (C-52+C-55+C-57+C-59)
----------------------------------------------------------------------
TYPE-A rows:  RESOLVED (bare) -- schema field-ID citation.
TYPE-B rows:  RESOLVED (bare) -- registry T-ID citation.
TYPE-C rows:  RESOLVED (confirmed false by: [artifact name,
              namespace, date]) -- STATUS CELL carries confirming
              artifact. Bare RESOLVED fails. Confirming artifact
              in Target Address only fails.
Gate:         Any DANGLING citation halts finalization.
Token:        MANIFEST-COMPLETE (GT-01) carries C-59 suffix:
              [Q] TYPE-C RESOLVED (confirming artifact INLINE
              in all [Q] rows).
----------------------------------------------------------------------
```

Self-certifying extended closure token:

`MANIFEST-COMPLETE: CIT-01..CIT-04 [4] TYPE-A RESOLVED, CIT-05..CIT-11 [7] TYPE-B RESOLVED, CIT-12..CIT-[N] [M] TYPE-C RESOLVED (confirming artifact INLINE in all [M] rows) -- citation-completeness and inline-evidence presence verified; no document traversal required to confirm all addresses resolve or that all TYPE-C rows carry confirming artifacts.`

---

### Step 9 -- [IA] Cross-Layer Citation Consistency Check [C-60]

After MANIFEST-COMPLETE is emitted, execute the cross-layer citation consistency check before
declaring the artifact complete. This step closes the gap between C-54 (Belief-Ref layer) and
C-57 (STATUS CELL layer): both cells reference the same physical evidence for the same belief,
but are produced at different steps and may diverge through editorial error.

```
CROSS-LAYER CITATION CONSISTENCY PROTOCOL (C-60)
----------------------------------------------------------------------
Scope:    All TYPE-C citations in the CITATION-COMPLETENESS-MANIFEST.
          TYPE-A and TYPE-B citations not evaluated.
Source 1: STILL-LIVE FILTER Belief-Ref cell for each TYPE-C
          citation's corresponding MUST-[N] row.
Source 2: CITATION-COMPLETENESS-MANIFEST STATUS column for each
          TYPE-C row.
Check:    Extract artifact name from each Belief-Ref cell.
          Extract artifact name from corresponding STATUS cell.
          Compare exactly. Record MATCH or MISMATCH per pair.
Token:    CROSS-CITATION-CONSISTENT (GT-04) -- emitted only when
          ALL rows show MATCH.
Gate:     MISMATCH IS A HARD GATE. Artifact production halts.
          Correct the discrepancy (identify which cell names the
          wrong artifact; re-populate; re-run from Step 9).
----------------------------------------------------------------------
```

**Per-citation consistency table:**

| Citation-ID | Belief-Ref-artifact (STILL-LIVE FILTER) | Status-Cell-artifact (manifest STATUS) | Verdict |
|-------------|----------------------------------------|----------------------------------------|---------|
| CIT-[N] | [artifact name from Belief-Ref cell] | [artifact name from STATUS cell] | MATCH |

If all rows show MATCH, emit CROSS-CITATION-CONSISTENT (GT-04):

`CROSS-CITATION-CONSISTENT: [K] TYPE-C citations checked; Belief-Ref artifacts and STATUS CELL artifacts verified identical per pair; all [K] rows MATCH -- cross-layer citation consistency confirmed.`

If any row shows MISMATCH: do not emit GT-04. Halt artifact production. Identify the discrepancy,
correct the source cell, and re-run the cross-layer check.

_(No explicit verification note. Whether CROSS-CITATION-CONSISTENT can be verified from the
per-citation table alone, without consulting the STILL-LIVE FILTER or manifest table, is not
stated. C-63 not satisfied.)_

== ARTIFACT STRUCTURE ============================================================

  1. ENFORCEMENT MECHANISM DECLARATION (EF; NO-ECHO COST named; C-26)
  2. EF-INVOCATION-RECORD (Step 0; C-33)
  3. PHASE-HANDOVER-0 table (6-row schema; Registry-Ref: T-00)
  4. PBI output (BC; COMMIT-SCAN + COMMIT-FREEZE tokens present)
  5. BC-COVERAGE-RECORD (F-BCR field-IDs in all headers; F-BCR-4 names specific PBI entries)
  6. PHASE-HANDOVER-1 table (6-row schema; Registry-Ref: T-01)
  7. HANDLE LEDGER output (IA)
  8. PHASE-HANDOVER-2 table (6-row schema; Registry-Ref: T-02)
  9. Corrections -- HIGH -> MEDIUM -> LOW
  10. PHASE-HANDOVER-3 table (6-row schema; Registry-Ref: T-03)
  11. Audited corrections (Register Audit output)
  12. PHASE-HANDOVER-4 table (6-row schema; Registry-Ref: T-04)
  13. Entry Gate blocks (all STATUS: CLEARED)
  14. PHASE-HANDOVER-5 table (6-row schema; Registry-Ref: T-05)
  15. Chain Integrity Audit (all CHAIN-COMPLETE)
  16. PHASE-HANDOVER-6 table (6-row schema; Registry-Ref: T-06)
  17. Rules of Thumb (RULES-ANCHORED-COMPLETE)
  18. Surprise hierarchy (ranked with rationale)
  19. Pattern of inherited errors
  20. Blind Spot Map
  21. Correction Forward Statement
  22. What this correction record excludes
  23. CONSUMER-INDEX-COMPLETE (Step 7; GT-02; independent; self-certifying) (C-53+C-55)
  24. CHAIN-GROUNDING-COMPLETE (Step 7; GT-03; independent; self-certifying) (C-54+C-55)
      Note: Gates 23 and 24 independent per GATE-INDEPENDENCE-ENFORCED (C-56)
  25. CITATION-COMPLETENESS-MANIFEST with extended MANIFEST-COMPLETE (Step 8; GT-01;
      C-59 inline-evidence suffix; TYPE-C STATUS CELL carries confirming artifact)
      (C-52+C-55+C-57+C-59)
  26. CROSS-CITATION-CONSISTENT per-citation table + token (Step 9; GT-04; all pairs MATCH)
      (C-60)
  Note: GATE-TOKEN-REGISTRY lists GT-01..GT-04 before Step 0 [AXIS A -- C-61 PASS]
        TOKEN CONTENT REQUIREMENT covers GT-01..GT-03 only [C-62 FAIL]
        Step 9 carries no explicit traversal-free verification note [C-63 FAIL]
        Items 23-26 diff against GT-01..GT-04 for completeness verification

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-02 -- Axis B: TOKEN CONTENT REQUIREMENT Comprehensive (C-62 targeted; C-61 C-63 absent)

**Variation axis:** Output format -- TOKEN CONTENT REQUIREMENT extends to cover all four gate
tokens including GT-04's full format contract (Axis B for C-62). GATE-TOKEN-REGISTRY lists
GT-01..GT-03 only; GT-04 not listed despite C-58+C-60 both satisfied (C-61 absent). Step 9
executes cross-layer check but carries no explicit traversal-free verification note (C-63 absent).

**Hypothesis:** When TOKEN CONTENT REQUIREMENT declares GT-04's format contract (count checked,
per-pair assertion required, MATCH condition), a reviewer consulting the section can verify the
full format requirement for all four tokens. However, a reviewer diffing the emitted tokens
against the registry finds GT-04 absent from the registry -- the registry is incomplete despite
C-60 being satisfied. And Step 9 carries no explicit note on traversal scope. C-62 closes the
format-contract comprehensiveness gap; the C-61 and C-63 gaps remain open.

**Expected v20 score:** 355 (C-61 FAIL, C-62 PASS, C-63 FAIL)

---

Topic: `{topic}`

_(Opening paragraph identical to V-01.)_

---

### GATE-TOKEN-REGISTRY [C-58 -- GT-01..GT-03 ONLY; GT-04 ABSENT]

Expected gate tokens for this artifact. Token absence is detectable by diff against this registry
without full-artifact traversal. A listed token absent from the artifact is missing.

| Token-ID | Canonical Name | Step | Prerequisite Criterion |
|----------|----------------|------|------------------------|
| GT-01 | MANIFEST-COMPLETE | Step 8 | C-52 (citation-completeness manifest exhaustive) |
| GT-02 | CONSUMER-INDEX-COMPLETE | Step 7 | C-53 (declaring-section consumer index populated) |
| GT-03 | CHAIN-GROUNDING-COMPLETE | Step 7 | C-54 (citation chain PBI grounding verified) |

Registry declared before Step 0. Diff GT-01..GT-03 against emitted tokens to verify completeness.
_(GT-04 is produced at Step 9 per the Cross-Layer Citation Consistency Protocol. GT-04 is not
declared in this registry. C-61 not satisfied: registry not current for derived gate token.)_

---

### Roles

_(All three role function declarations identical to V-01.)_

**Phase Handover Schema (universal):** _(Identical to V-01.)_

---

#### TOKEN CONTENT REQUIREMENT [AXIS B -- C-62: COMPREHENSIVE FOR ALL FOUR TOKENS]

Every gate token emitted in this artifact must carry inline specifics sufficient to verify its
pass condition without consulting the underlying artifact sections. This requirement applies to
all four gate tokens: GT-01, GT-02, GT-03, and GT-04.

**Required format for MANIFEST-COMPLETE (GT-01) -- extended for C-59:**

_(Identical to V-01.)_

**Required format for CONSUMER-INDEX-COMPLETE (GT-02):**

_(Identical to V-01.)_

**Required format for CHAIN-GROUNDING-COMPLETE (GT-03):**

_(Identical to V-01.)_

**Required format for CROSS-CITATION-CONSISTENT (GT-04) [AXIS B -- C-62]:**

```
CROSS-CITATION-CONSISTENT: [K] TYPE-C citations checked;
  Belief-Ref artifacts and STATUS CELL artifacts verified identical
  per pair; all [K] rows MATCH -- cross-layer citation consistency
  confirmed.
```

The token must name the count checked ([K]) and assert per-pair identity. A token stating
"all consistent" without naming the count fails. A token emitted when any row is MISMATCH
fails the hard gate condition. A token omitting the per-pair assertion fails.

---

#### GATE-INDEPENDENCE-ENFORCED [C-56]

_(Identical to V-01.)_

---

#### MANIFEST-TOKEN-INLINE-EVIDENCE-SUFFIX [C-59]

_(Identical to V-01.)_

---

#### MANIFEST-ROW-INLINE-EVIDENCE [C-57]

_(Identical to V-01.)_

---

#### Phase Transition Registry [C-50 -- Consumer-Ref column]

_(Identical to V-01: T-00 through T-06 with Consumer-Ref column.)_

---

### BC-STEP1-PROTOCOL

_(Identical to V-01.)_

#### BC-COVERAGE-RECORD Schema

_(Identical to V-01: F-BCR-1 through F-BCR-4 with Consumer-Ref column.)_

---

### Steps 0-6

_(Identical to V-01.)_

### Step 3 Extension -- STILL-LIVE FILTER

_(Identical to V-01.)_

---

### Step 7 -- [IA] Hierarchy, Distillation, and Dual-Gate Emission

_(Identical to V-01: GT-02 and GT-03 emitted as independent self-certifying tokens.)_

---

### Step 8 -- [IA] Citation-Completeness Manifest

_(Identical to V-01: MANIFEST-COMPLETE carries C-59 inline-evidence suffix; TYPE-C STATUS cells
carry confirming artifact.)_

---

### Step 9 -- [IA] Cross-Layer Citation Consistency Check [C-60]

_(Cross-layer check protocol identical to V-01. Per-citation consistency table identical to V-01.
GT-04 token emitted when all rows MATCH.)_

If all rows show MATCH, emit CROSS-CITATION-CONSISTENT (GT-04). Format per TOKEN CONTENT
REQUIREMENT [AXIS B -- C-62]:

`CROSS-CITATION-CONSISTENT: [K] TYPE-C citations checked; Belief-Ref artifacts and STATUS CELL artifacts verified identical per pair; all [K] rows MATCH -- cross-layer citation consistency confirmed.`

If any row shows MISMATCH: do not emit GT-04. Halt artifact production.

_(No explicit verification note. C-63 not satisfied.)_

== ARTIFACT STRUCTURE ============================================================

  _(Items 1-25 identical to V-01.)_
  26. CROSS-CITATION-CONSISTENT per-citation table + token (Step 9; GT-04; all pairs MATCH)
      (C-60; token format per TOKEN CONTENT REQUIREMENT GT-04 contract)
  Note: GATE-TOKEN-REGISTRY lists GT-01..GT-03 only [C-61 FAIL]
        TOKEN CONTENT REQUIREMENT covers all four tokens including GT-04 [AXIS B -- C-62 PASS]
        Step 9 carries no explicit traversal-free verification note [C-63 FAIL]

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-03 -- Axis C: Cross-Citation Traversal-Free Explicit (C-63 targeted; C-61 C-62 absent)

**Variation axis:** Output format -- Step 9 carries an explicit verification note naming what
sections are NOT required for verification (Axis C for C-63). GATE-TOKEN-REGISTRY lists
GT-01..GT-03 only; GT-04 absent despite C-58+C-60 both satisfied (C-61 absent). TOKEN CONTENT
REQUIREMENT covers GT-01..GT-03 only; GT-04 format contract absent (C-62 absent).

**Hypothesis:** When Step 9 explicitly names what the reviewer does NOT need to consult to verify
CROSS-CITATION-CONSISTENT -- "No consultation of the STILL-LIVE FILTER or manifest table is
required beyond the table rows in this step" -- the traversal-free property of GT-04 is as
explicit as the self-certifying contracts of GT-01..GT-03. However, the registry is incomplete
(no GT-04), and TOKEN CONTENT REQUIREMENT does not declare GT-04's format contract. C-63 closes
the contract-parity gap; the C-61 and C-62 gaps remain open.

**Expected v20 score:** 355 (C-61 FAIL, C-62 PASS -- NO, C-62 FAIL, C-63 PASS)

_(Correction: C-62 FAIL -- TOKEN CONTENT REQUIREMENT covers GT-01..GT-03 only. Net: 350+5 = 355.)_

---

Topic: `{topic}`

_(Opening paragraph identical to V-01.)_

---

### GATE-TOKEN-REGISTRY [C-58 -- GT-01..GT-03 ONLY; GT-04 ABSENT]

_(Identical to V-02: GT-01..GT-03 listed. GT-04 absent. C-61 not satisfied.)_

---

### Roles

_(All three role function declarations identical to V-01.)_

**Phase Handover Schema (universal):** _(Identical to V-01.)_

---

#### TOKEN CONTENT REQUIREMENT [C-55 -- GT-01..GT-03 ONLY; GT-04 FORMAT CONTRACT ABSENT]

_(Identical to V-01: GT-01..GT-03 format contracts declared. GT-04 format contract not declared.
Note appended: "GT-04 token format: see Step 9 Cross-Layer Citation Consistency Protocol for
emission conditions. TOKEN CONTENT REQUIREMENT does not declare GT-04's format contract.")_

---

#### GATE-INDEPENDENCE-ENFORCED [C-56]

_(Identical to V-01.)_

---

#### MANIFEST-TOKEN-INLINE-EVIDENCE-SUFFIX [C-59]

_(Identical to V-01.)_

---

#### MANIFEST-ROW-INLINE-EVIDENCE [C-57]

_(Identical to V-01.)_

---

#### Phase Transition Registry [C-50 -- Consumer-Ref column]

_(Identical to V-01: T-00 through T-06 with Consumer-Ref column.)_

---

### BC-STEP1-PROTOCOL

_(Identical to V-01.)_

#### BC-COVERAGE-RECORD Schema

_(Identical to V-01: F-BCR-1 through F-BCR-4 with Consumer-Ref column.)_

---

### Steps 0-6

_(Identical to V-01.)_

### Step 3 Extension -- STILL-LIVE FILTER

_(Identical to V-01.)_

---

### Step 7 -- [IA] Hierarchy, Distillation, and Dual-Gate Emission

_(Identical to V-01.)_

---

### Step 8 -- [IA] Citation-Completeness Manifest

_(Identical to V-01.)_

---

### Step 9 -- [IA] Cross-Layer Citation Consistency Check [C-60 + AXIS C -- C-63]

After MANIFEST-COMPLETE is emitted, execute the cross-layer citation consistency check before
declaring the artifact complete.

```
CROSS-LAYER CITATION CONSISTENCY PROTOCOL (C-60)
----------------------------------------------------------------------
Scope:    All TYPE-C citations in the CITATION-COMPLETENESS-MANIFEST.
          TYPE-A and TYPE-B citations not evaluated.
Source 1: STILL-LIVE FILTER Belief-Ref cell for each TYPE-C
          citation's corresponding MUST-[N] row.
Source 2: CITATION-COMPLETENESS-MANIFEST STATUS column for each
          TYPE-C row.
Check:    Extract artifact name from each Belief-Ref cell.
          Extract artifact name from corresponding STATUS cell.
          Compare exactly. Record MATCH or MISMATCH per pair.
Token:    CROSS-CITATION-CONSISTENT (GT-04) -- emitted only when
          ALL rows show MATCH.
Gate:     MISMATCH IS A HARD GATE. Artifact production halts.
          Correct the discrepancy (identify which cell names the
          wrong artifact; re-populate; re-run from Step 9).
----------------------------------------------------------------------
```

**Per-citation consistency table:**

| Citation-ID | Belief-Ref-artifact (STILL-LIVE FILTER) | Status-Cell-artifact (manifest STATUS) | Verdict |
|-------------|----------------------------------------|----------------------------------------|---------|
| CIT-[N] | [artifact name from Belief-Ref cell] | [artifact name from STATUS cell] | MATCH |

If all rows show MATCH, emit CROSS-CITATION-CONSISTENT (GT-04):

`CROSS-CITATION-CONSISTENT: [K] TYPE-C citations checked; Belief-Ref artifacts and STATUS CELL artifacts verified identical per pair; all [K] rows MATCH -- cross-layer citation consistency confirmed.`

If any row shows MISMATCH: do not emit GT-04. Halt artifact production.

**Verification note [AXIS C -- C-63: TRAVERSAL-FREE EXPLICIT]:** A reviewer can verify
CROSS-CITATION-CONSISTENT from the per-citation table alone: the table enumerates each pair
with both artifact names and the MATCH verdict. No consultation of the STILL-LIVE FILTER or
CITATION-COMPLETENESS-MANIFEST is required beyond the table rows in this step.

== ARTIFACT STRUCTURE ============================================================

  _(Items 1-25 identical to V-01.)_
  26. CROSS-CITATION-CONSISTENT per-citation table + token (Step 9; GT-04; all pairs MATCH;
      explicit traversal-free verification note present) (C-60)
  Note: GATE-TOKEN-REGISTRY lists GT-01..GT-03 only [C-61 FAIL]
        TOKEN CONTENT REQUIREMENT covers GT-01..GT-03 only [C-62 FAIL]
        Step 9 carries explicit traversal-free verification note [AXIS C -- C-63 PASS]

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-04 -- Axes A+B: Registry Covers Derived Gate + TOKEN CONTENT REQUIREMENT Comprehensive
## (C-61+C-62 targeted; C-63 absent)

**Variation axis:** Full integration of Axis A (C-61) and Axis B (C-62) -- GATE-TOKEN-REGISTRY
extended for GT-04, TOKEN CONTENT REQUIREMENT comprehensive for all four tokens -- without Axis C.
Step 9 executes cross-layer check but carries no explicit traversal-free verification note (C-63
absent). All R19 properties preserved.

**Hypothesis:** When the registry self-extends for GT-04 (C-61 PASS) and TOKEN CONTENT REQUIREMENT
declares GT-04's full format contract (C-62 PASS), the registry-to-format-contract path is closed
for all four tokens: token completeness is diff-detectable and the format requirement for each token
is declared. However, the traversal-free property of GT-04 verification remains implicit -- a
reviewer new to the artifact cannot confirm from text alone whether consulting the STILL-LIVE FILTER
or manifest table is required. C-61+C-62 corroborate: the registry declares GT-04 and the format
contract section proves GT-04's content requirements. C-63 gap remains open.

**Expected v20 score:** 360 (C-61 PASS, C-62 PASS, C-63 FAIL)

---

Topic: `{topic}`

_(Opening paragraph identical to V-01.)_

---

### GATE-TOKEN-REGISTRY [AXIS A -- C-61: REGISTRY COVERS DERIVED GATE]

_(Identical to V-01: GT-01..GT-04 listed with step locations and prerequisite criteria. GT-04
declared with Step 9 location and C-60 prerequisite. Registry declared before Step 0.)_

---

### Roles

_(All three role function declarations identical to V-01.)_

**Phase Handover Schema (universal):** _(Identical to V-01.)_

---

#### TOKEN CONTENT REQUIREMENT [AXIS B -- C-62: COMPREHENSIVE FOR ALL FOUR TOKENS]

_(Identical to V-02: covers GT-01..GT-04. GT-04 format contract present: count checked, per-pair
assertion required, MATCH condition declared, MISMATCH fails the hard gate.)_

---

#### GATE-INDEPENDENCE-ENFORCED [C-56]

_(Identical to V-01.)_

---

#### MANIFEST-TOKEN-INLINE-EVIDENCE-SUFFIX [C-59]

_(Identical to V-01.)_

---

#### MANIFEST-ROW-INLINE-EVIDENCE [C-57]

_(Identical to V-01.)_

---

#### Phase Transition Registry [C-50 -- Consumer-Ref column]

_(Identical to V-01: T-00 through T-06 with Consumer-Ref column.)_

---

### BC-STEP1-PROTOCOL

_(Identical to V-01.)_

#### BC-COVERAGE-RECORD Schema

_(Identical to V-01.)_

---

### Steps 0-6

_(Identical to V-01.)_

### Step 3 Extension -- STILL-LIVE FILTER

_(Identical to V-01.)_

---

### Step 7 -- [IA] Hierarchy, Distillation, and Dual-Gate Emission

_(Identical to V-01.)_

---

### Step 8 -- [IA] Citation-Completeness Manifest

_(Identical to V-01.)_

---

### Step 9 -- [IA] Cross-Layer Citation Consistency Check [C-60]

_(Cross-layer check protocol identical to V-01. Per-citation consistency table identical to V-01.
GT-04 token emitted when all rows MATCH. Format per TOKEN CONTENT REQUIREMENT GT-04 contract:
count named, per-pair assertion present.)_

`CROSS-CITATION-CONSISTENT: [K] TYPE-C citations checked; Belief-Ref artifacts and STATUS CELL artifacts verified identical per pair; all [K] rows MATCH -- cross-layer citation consistency confirmed.`

If any row shows MISMATCH: do not emit GT-04. Halt artifact production.

_(No explicit verification note naming what sections are not required. The traversal-free property
of CROSS-CITATION-CONSISTENT is real but undeclared. C-63 not satisfied.)_

== ARTIFACT STRUCTURE ============================================================

  _(Items 1-25 identical to V-01.)_
  26. CROSS-CITATION-CONSISTENT per-citation table + token (Step 9; GT-04; all pairs MATCH;
      token format per TOKEN CONTENT REQUIREMENT GT-04 contract) (C-60)
  Note: GATE-TOKEN-REGISTRY lists GT-01..GT-04 before Step 0 [AXIS A -- C-61 PASS]
        TOKEN CONTENT REQUIREMENT covers all four tokens including GT-04 [AXIS B -- C-62 PASS]
        Step 9 carries no explicit traversal-free verification note [C-63 FAIL]
        Items 23-26 diff against GT-01..GT-04 for completeness verification

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## V-05 -- Axes A+B+C: Full R20 Closure Layer (C-61+C-62+C-63 all targeted)

**Variation axis:** Full integration -- GATE-TOKEN-REGISTRY extended for GT-04 (Axis A for C-61),
TOKEN CONTENT REQUIREMENT comprehensive for all four tokens (Axis B for C-62), and Step 9 explicit
traversal-free verification note (Axis C for C-63) all active simultaneously. All R19 V-05
properties preserved: C-58 registry for GT-01..GT-03 extended to GT-04, C-59 MANIFEST-COMPLETE
suffix, C-60 cross-layer check. This variation is structurally equivalent to R19 V-05 with the
R20 axis labels made explicit.

**Hypothesis:** V-01, V-02, V-03 each isolate one new structural property against the R19 V-05
base. V-04 demonstrated the registry-to-format-contract path closure (C-61+C-62 corroborate: the
registry declares GT-04 and the format contract proves GT-04's content requirements). V-05 asks
whether all three simultaneously produce a closed R20 closure-layer audit:
(1) Token completeness is diff-detectable for all four tokens: the registry lists GT-01..GT-04;
    any missing token is identified by registry-vs-emitted diff. (C-61)
(2) TOKEN CONTENT REQUIREMENT is current for all four tokens: GT-04's format contract is declared
    alongside GT-01..GT-03. A reviewer can verify any token's format requirement from the section
    alone. (C-62)
(3) The traversal-free property of GT-04 is explicit: Step 9 names what sections are not required,
    in parity with the self-certifying contracts of GT-01..GT-03. (C-63)

The three properties form a coherent R20 closure-layer contract: token set auditable by registry
for all four tokens (C-61), format contracts comprehensive for all four tokens (C-62),
verification contract for GT-04 as explicit as for GT-01..GT-03 (C-63).

**Expected v20 score:** 365 (all 63 criteria: PASS; maximum achievable under v20)

---

Topic: `{topic}`

Synthesize what was unexpected. Three roles at three exclusive phase boundaries. Every structural
commitment is named, formal, and auditable from output. This is not a summary. This is not a list
of findings. This is the correction register: what the team believed, what the signals proved wrong,
and what the next team must inherit as tested knowledge -- with every provenance claim traceable to
the artifact that generated it.

---

### GATE-TOKEN-REGISTRY [AXIS A -- C-61: REGISTRY COVERS DERIVED GATE]

Expected gate tokens for this artifact. Token absence is detectable by diff against this registry
without full-artifact traversal. A listed token absent from the artifact is missing. A token not
listed here should not appear as a gate token.

| Token-ID | Canonical Name | Step | Prerequisite Criterion |
|----------|----------------|------|------------------------|
| GT-01 | MANIFEST-COMPLETE | Step 8 | C-52 (citation-completeness manifest exhaustive) |
| GT-02 | CONSUMER-INDEX-COMPLETE | Step 7 | C-53 (declaring-section consumer index populated) |
| GT-03 | CHAIN-GROUNDING-COMPLETE | Step 7 | C-54 (citation chain PBI grounding verified) |
| GT-04 | CROSS-CITATION-CONSISTENT | Step 9 | C-60 (cross-layer citation consistency verified) |

Registry declared before Step 0. Diff GT-01..GT-04 against emitted tokens to verify completeness.
GT-04 is a derived gate token produced when C-60 is satisfied at Step 9. The registry self-extends
to include GT-04: a registry listing only GT-01..GT-03 would be accurate but not current for a
four-token artifact, and token completeness for GT-04 would be scan-dependent, not diff-detectable.

---

### Roles

**Enforcement Framer (EF)** -- Step 0 exclusively.
_(Function declaration identical to V-01.)_

**Belief Cartographer (BC)** -- Step 1 exclusively.
_(Function declaration identical to V-01.)_

**Institutional Archaeologist (IA)** -- Steps 2-9.

```
INSTITUTIONAL ARCHAEOLOGIST -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     False-assumption recovery. Correction register only.
              Each IA stage exit (Steps 2-6) produces a PHASE-
              HANDOVER-[N] table before advancing. At Step 7, emit
              CONSUMER-INDEX-COMPLETE (GT-02) and CHAIN-GROUNDING-
              COMPLETE (GT-03) as INDEPENDENT tokens per
              GATE-INDEPENDENCE-ENFORCED -- combined tokens at this
              boundary are non-conforming. Each token self-certifying
              per TOKEN CONTENT REQUIREMENT. At Step 8, produce the
              CITATION-COMPLETENESS-MANIFEST; MANIFEST-COMPLETE (GT-01)
              carries the C-59 inline-evidence suffix -- self-certifying
              for both citation accounting and inline-evidence presence;
              TYPE-C STATUS CELL carries confirming artifact per
              MANIFEST-ROW-INLINE-EVIDENCE. At Step 9, execute the
              Cross-Layer Citation Consistency Check: compare each
              TYPE-C Belief-Ref artifact against its STATUS CELL
              artifact per pair; emit CROSS-CITATION-CONSISTENT (GT-04)
              only when all rows MATCH. Four gate tokens required (see
              GATE-TOKEN-REGISTRY); any absent or non-conforming token
              is an incompletion.
Input:        Signal artifacts + frozen PBI (read-only).
Out-of-scope: PBI authorship (frozen). Enforcement section (immutable).
Orienting:    "What would the next team build wrong?"
Phase scope:  Steps 2-9 only.
----------------------------------------------------------------------
```

**Phase Handover Schema (universal):** _(Identical to V-01.)_

---

#### TOKEN CONTENT REQUIREMENT [AXIS B -- C-62: COMPREHENSIVE FOR ALL FOUR TOKENS]

Every gate token emitted in this artifact must carry inline specifics sufficient to verify its
pass condition without consulting the underlying artifact sections. This requirement applies to
all four gate tokens declared in the GATE-TOKEN-REGISTRY.

**Required format for MANIFEST-COMPLETE (GT-01) -- extended for C-59:**

```
MANIFEST-COMPLETE: CIT-[N1]..CIT-[N2] [K] TYPE-A RESOLVED,
  CIT-[M1]..CIT-[M2] [L] TYPE-B RESOLVED,
  CIT-[P1]..CIT-[P2] [Q] TYPE-C RESOLVED
    (confirming artifact INLINE in all [Q] rows) --
  citation-completeness and inline-evidence presence verified;
  no document traversal required to confirm all addresses resolve
  or that all TYPE-C rows carry confirming artifacts.
```

A token whose TYPE-C count omits the inline-evidence suffix fails C-59.

**Required format for CONSUMER-INDEX-COMPLETE (GT-02):**
_(Identical to V-01: three tables named individually with ID ranges.)_

**Required format for CHAIN-GROUNDING-COMPLETE (GT-03):**
_(Identical to V-01: both condition labels present.)_

**Required format for CROSS-CITATION-CONSISTENT (GT-04) [AXIS B -- C-62]:**

```
CROSS-CITATION-CONSISTENT: [K] TYPE-C citations checked;
  Belief-Ref artifacts and STATUS CELL artifacts verified identical
  per pair; all [K] rows MATCH -- cross-layer citation consistency
  confirmed.
```

The token must name the count checked ([K]) and assert per-pair identity. A token stating
"all consistent" without naming the count fails. A token emitted when any row is MISMATCH
fails the hard gate condition.

---

#### GATE-INDEPENDENCE-ENFORCED [C-56]

_(Identical to V-01. Combined tokens non-conforming at co-located gate boundaries. Step 7
application: GT-02 and GT-03 must be separate independent tokens.)_

---

#### MANIFEST-TOKEN-INLINE-EVIDENCE-SUFFIX [C-59]

_(Identical to V-01. MANIFEST-COMPLETE self-certifies both citation accounting (C-52) and
inline-evidence presence (C-57) from token text alone.)_

---

#### MANIFEST-ROW-INLINE-EVIDENCE [C-57]

_(Identical to V-01. TYPE-C STATUS CELL carries confirming artifact. Bare RESOLVED fails.)_

---

#### Phase Transition Registry [C-50 -- Consumer-Ref column]

_(Identical to V-01: T-00 through T-06 with Consumer-Ref column.)_

---

### BC-STEP1-PROTOCOL

_(Identical to V-01: three sub-phases [SCAN], [FREEZE], [COVERAGE AUDIT].)_

#### BC-COVERAGE-RECORD Schema [C-46/C-49 -- field-IDs + Consumer-Ref; F-BCR-4 specific format]

_(Identical to V-01: F-BCR-1 through F-BCR-4 with Consumer-Ref column. F-BCR-4 names specific
PBI entries by ID range and source material -- generic sentence fails C-54 condition 2.)_

---

### Steps 0-6

_(Identical to V-01. All PHASE-HANDOVER tables carry Registry-Ref rows with T-ID citations.)_

### Step 3 Extension -- STILL-LIVE FILTER [C-51 extended Belief-Ref + C-53 Consumer-Ref]

_(Identical to V-01. MUST-ID + Scope + Action + Constraint + extended Belief-Ref
[`PB-[NN] (confirmed false by: [artifact name, namespace, date])`] + Consumer-Ref columns.)_

---

### Step 7 -- [IA] Hierarchy, Distillation, and Dual-Gate Emission [C-53+C-54+C-55+C-56]

_(Hierarchy and distillation content identical to V-01.)_

After artifact content is complete, emit both Step 7 completeness gates as INDEPENDENT
self-certifying tokens per GATE-INDEPENDENCE-ENFORCED and TOKEN CONTENT REQUIREMENT:

Gate 1 (C-53) -- CONSUMER-INDEX-COMPLETE (GT-02):

`CONSUMER-INDEX-COMPLETE: BC-COVERAGE-RECORD Schema F-BCR-1..F-BCR-4 Consumer-Ref POPULATED, Phase Transition Registry T-00..T-06 Consumer-Ref POPULATED, STILL-LIVE FILTER MUST-1..MUST-4 Consumer-Ref POPULATED -- bidirectional navigability confirmed across all three axes.`

Gate 2 (C-54) -- CHAIN-GROUNDING-COMPLETE (GT-03):

`CHAIN-GROUNDING-COMPLETE: Belief-Ref cells EXTENDED (all MUST-[N] carry confirming artifact reference), F-BCR-4 SPECIFIC (names PB-[NN] through PB-[NN]) -- citation chain verified to evidence; both C-54 conditions confirmed.`

These two tokens are at the same step boundary. Per GATE-INDEPENDENCE-ENFORCED, they are
emitted as separate tokens. A combined token is non-conforming.

---

### Step 8 -- [IA] Citation-Completeness Manifest [C-52+C-55+C-57+C-59]

Produce CITATION-COMPLETENESS-MANIFEST. Apply all active declarations:
- TOKEN CONTENT REQUIREMENT + MANIFEST-TOKEN-INLINE-EVIDENCE-SUFFIX: MANIFEST-COMPLETE (GT-01)
  carries C-59 inline-evidence suffix.
- MANIFEST-ROW-INLINE-EVIDENCE: TYPE-C STATUS cells carry confirming artifact.

```
CITATION-COMPLETENESS-MANIFEST PROTOCOL (C-52+C-55+C-57+C-59)
----------------------------------------------------------------------
TYPE-A rows:  RESOLVED (bare) -- schema field-ID citation.
TYPE-B rows:  RESOLVED (bare) -- registry T-ID citation.
TYPE-C rows:  RESOLVED (confirmed false by: [artifact name,
              namespace, date]) -- STATUS CELL carries confirming
              artifact. Bare RESOLVED fails. Confirming artifact
              in Target Address only fails.
Gate:         Any DANGLING citation halts finalization.
Token:        MANIFEST-COMPLETE (GT-01) carries C-59 suffix:
              [Q] TYPE-C RESOLVED (confirming artifact INLINE
              in all [Q] rows).
----------------------------------------------------------------------
```

Self-certifying extended closure token:

`MANIFEST-COMPLETE: CIT-01..CIT-04 [4] TYPE-A RESOLVED, CIT-05..CIT-11 [7] TYPE-B RESOLVED, CIT-12..CIT-[N] [M] TYPE-C RESOLVED (confirming artifact INLINE in all [M] rows) -- citation-completeness and inline-evidence presence verified; no document traversal required to confirm all addresses resolve or that all TYPE-C rows carry confirming artifacts.`

---

### Step 9 -- [IA] Cross-Layer Citation Consistency Check [C-60 + AXIS C -- C-63]

After MANIFEST-COMPLETE is emitted, execute the cross-layer citation consistency check before
declaring the artifact complete. This step closes the gap between C-54 (Belief-Ref layer) and
C-57 (STATUS CELL layer): both cells reference the same physical evidence for the same belief,
but are produced at different steps and may diverge through editorial error.

```
CROSS-LAYER CITATION CONSISTENCY PROTOCOL (C-60)
----------------------------------------------------------------------
Scope:    All TYPE-C citations in the CITATION-COMPLETENESS-MANIFEST.
          TYPE-A and TYPE-B citations not evaluated.
Source 1: STILL-LIVE FILTER Belief-Ref cell for each TYPE-C
          citation's corresponding MUST-[N] row.
Source 2: CITATION-COMPLETENESS-MANIFEST STATUS column for each
          TYPE-C row.
Check:    Extract artifact name from each Belief-Ref cell.
          Extract artifact name from corresponding STATUS cell.
          Compare exactly. Record MATCH or MISMATCH per pair.
Token:    CROSS-CITATION-CONSISTENT (GT-04) -- emitted only when
          ALL rows show MATCH.
Gate:     MISMATCH IS A HARD GATE. Artifact production halts.
          Correct the discrepancy (identify which cell names the
          wrong artifact; re-populate; re-run from Step 9).
----------------------------------------------------------------------
```

**Per-citation consistency table:**

| Citation-ID | Belief-Ref-artifact (STILL-LIVE FILTER) | Status-Cell-artifact (manifest STATUS) | Verdict |
|-------------|----------------------------------------|----------------------------------------|---------|
| CIT-[N] | [artifact name from Belief-Ref cell] | [artifact name from STATUS cell] | MATCH |

If all rows show MATCH, emit CROSS-CITATION-CONSISTENT (GT-04):

`CROSS-CITATION-CONSISTENT: [K] TYPE-C citations checked; Belief-Ref artifacts and STATUS CELL artifacts verified identical per pair; all [K] rows MATCH -- cross-layer citation consistency confirmed.`

If any row shows MISMATCH: do not emit GT-04. Halt artifact production. Identify the discrepancy,
correct the source cell, and re-run the cross-layer check.

**Verification note [AXIS C -- C-63: TRAVERSAL-FREE EXPLICIT]:** A reviewer can verify
CROSS-CITATION-CONSISTENT from the per-citation table alone: the table enumerates each pair
with both artifact names and the MATCH verdict. No consultation of the STILL-LIVE FILTER or
CITATION-COMPLETENESS-MANIFEST is required beyond the table rows in this step.

== ARTIFACT STRUCTURE ============================================================

  1. ENFORCEMENT MECHANISM DECLARATION (EF; NO-ECHO COST named; C-26)
  2. EF-INVOCATION-RECORD (Step 0; C-33)
  3. PHASE-HANDOVER-0 table (6-row schema; Registry-Ref: T-00)
  4. PBI output (BC; COMMIT-SCAN + COMMIT-FREEZE tokens present)
  5. BC-COVERAGE-RECORD (F-BCR field-IDs in all headers; F-BCR-4 names specific PBI entries)
  6. PHASE-HANDOVER-1 table (6-row schema; Registry-Ref: T-01)
  7. HANDLE LEDGER output (IA)
  8. PHASE-HANDOVER-2 table (6-row schema; Registry-Ref: T-02)
  9. Corrections -- HIGH -> MEDIUM -> LOW
  10. PHASE-HANDOVER-3 table (6-row schema; Registry-Ref: T-03)
  11. Audited corrections (Register Audit output)
  12. PHASE-HANDOVER-4 table (6-row schema; Registry-Ref: T-04)
  13. Entry Gate blocks (all STATUS: CLEARED)
  14. PHASE-HANDOVER-5 table (6-row schema; Registry-Ref: T-05)
  15. Chain Integrity Audit (all CHAIN-COMPLETE)
  16. PHASE-HANDOVER-6 table (6-row schema; Registry-Ref: T-06)
  17. Rules of Thumb (RULES-ANCHORED-COMPLETE)
  18. Surprise hierarchy (ranked with rationale)
  19. Pattern of inherited errors
  20. Blind Spot Map
  21. Correction Forward Statement
  22. What this correction record excludes
  23. CONSUMER-INDEX-COMPLETE (Step 7; GT-02; independent; self-certifying) (C-53+C-55)
  24. CHAIN-GROUNDING-COMPLETE (Step 7; GT-03; independent; self-certifying) (C-54+C-55)
      Note: Gates 23 and 24 independent per GATE-INDEPENDENCE-ENFORCED (C-56)
  25. CITATION-COMPLETENESS-MANIFEST with extended MANIFEST-COMPLETE (Step 8; GT-01;
      C-59 inline-evidence suffix; TYPE-C STATUS CELL carries confirming artifact)
      (C-52+C-55+C-57+C-59)
  26. CROSS-CITATION-CONSISTENT per-citation table + token (Step 9; GT-04; all pairs MATCH;
      explicit traversal-free verification note: STILL-LIVE FILTER and
      CITATION-COMPLETENESS-MANIFEST not required) (C-60)
  Note: GATE-TOKEN-REGISTRY lists GT-01..GT-04 before Step 0 [AXIS A -- C-61 PASS]
        TOKEN CONTENT REQUIREMENT covers all four tokens including GT-04 [AXIS B -- C-62 PASS]
        Step 9 carries explicit traversal-free verification note naming what sections
        are NOT required [AXIS C -- C-63 PASS]
        Items 23-26 diff against GT-01..GT-04 for completeness verification

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## Variation Summary

| # | Axis | New R20 Declarations | C-61 | C-62 | C-63 | v20 score |
|---|------|---------------------|:----:|:----:|:----:|:---------:|
| V-01 | A only | GT-04 in GATE-TOKEN-REGISTRY | PASS | FAIL | FAIL | 355 |
| V-02 | B only | GT-04 format contract in TOKEN CONTENT REQUIREMENT | FAIL | PASS | FAIL | 355 |
| V-03 | C only | Explicit traversal-free note in Step 9 | FAIL | FAIL | PASS | 355 |
| V-04 | A+B | GT-04 in registry + GT-04 format in TOKEN CONTENT REQUIREMENT | PASS | PASS | FAIL | 360 |
| **V-05** | **A+B+C** | **All three + traversal-free note in Step 9** | **PASS** | **PASS** | **PASS** | **365** |

**R20 structural contribution beyond R19:**

Each new criterion closes a gap visible only when C-60 is satisfied alongside C-58 and/or C-59:

- **C-61: GATE-TOKEN-REGISTRY-COVERS-DERIVED-GATE** -- extends the registry currency contract
  to derived gate tokens. C-58 established diff-detectable token completeness for a three-token
  world. C-61 applies the same contract to GT-04: the registry must self-extend when C-60 is
  satisfied, so the four-token artifact remains diff-auditable. Parallels C-52's citation manifest
  requirement: a manifest that accounts for TYPE-A and TYPE-B but not TYPE-C fails even if TYPE-C
  citations exist; a registry that accounts for GT-01..GT-03 but not GT-04 fails the same way.

- **C-62: TOKEN-CONTENT-REQUIREMENT-COMPREHENSIVE** -- extends the format-contract coverage
  to GT-04. C-55 required format contracts for the three original gate tokens. C-60 introduced
  GT-04. TOKEN CONTENT REQUIREMENT must remain current: a reviewer should be able to verify any
  token's format requirement from the section alone, without hunting through the producing step.
  C-62 is to TOKEN CONTENT REQUIREMENT what C-52's manifest is to citations: both require the
  declared inventory to remain current as the artifact's structure evolves.

- **C-63: CROSS-CITATION-TRAVERSAL-FREE-EXPLICIT** -- makes the traversal-free property of
  GT-04 as explicit as the self-certifying contracts of GT-01..GT-03. C-55 established that each
  gate token must carry sufficient inline specifics for verification without consulting underlying
  sections. GT-04 satisfies this by design (the per-citation table is the audit record), but the
  satisfaction was implicit -- the verification contract was not stated. C-63 requires the note to
  appear in parity with the contracts C-55 established: naming what sections are NOT required is
  the affirmative declaration that makes the traversal-free property auditable from the text.

The three declarations form a coherent R20 closure-of-the-closure set: C-61 makes the registry
current (it knew about GT-01..GT-03; it must now know about GT-04). C-62 makes the format contract
section current (TOKEN CONTENT REQUIREMENT knew about three tokens; it must now cover four). C-63
makes the verification contract explicit (GT-04's traversal-free property was implied; it must now
be stated in parity with the self-certifying standard C-55 established for GT-01..GT-03).

Gate chain: R10 output auditable -> R11 output non-defeatable -> R12 enforcement legible ->
R13 structure navigable -> R14 element addressable -> R15 address citation-activated ->
R16 citation exhaustively manifested, bidirectionally indexed, and chain-grounded ->
R17 tokens self-certifying, gates independent, manifest rows inline-evidenced ->
R18 token inventory declared, manifest token extended for inline-evidence,
cross-layer citation consistent ->
R19 registry self-extends for derived gate tokens, token format contracts comprehensive,
cross-citation verification contract traversal-free explicit.
