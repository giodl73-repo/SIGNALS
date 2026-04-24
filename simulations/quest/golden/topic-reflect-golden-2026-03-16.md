Golden prompt written to `simulations/quest/golden/topic-echo-golden-2026-03-16.md`.

**What's in the file:**

- **Frontmatter** — skill, target, date, rounds 20, rubric v21, score 365, status GOLDEN
- **Prompt body** — verbatim from the QU5 simplified variation (PASS, 1943 words, 21% reduction from V-05's 2446)
- **What made it golden** — four patterns distinguishing V-05 from V-01:
  1. Four-token registry currency (C-61, Axis A) — GT-04 listed with step + prerequisite, making completeness diff-detectable
  2. Format contract comprehensiveness (C-62, Axis B) — TOKEN CONTENT REQUIREMENT covers all four tokens including GT-04's count + per-pair identity requirement
  3. Traversal-free scope explicit (C-63, Axis C) — Step 9 verification note names what sections are NOT required
  4. Simultaneous closure at all three axis intersections — V-01/V-02/V-03 each score 355; only V-05 scores 365/365 by satisfying all three gates that depend on C-60
- **Final rubric summary** — essential C-01..C-05, R20 closure layer C-58..C-63 (all PASS), R21 target layer C-64..C-66 (all FAIL, open for R21), and the full gate chain R10->R20
| GT-01 | MANIFEST-COMPLETE | Step 8 | C-52 (citation-completeness manifest exhaustive) |
| GT-02 | CONSUMER-INDEX-COMPLETE | Step 7 | C-53 (declaring-section consumer index populated) |
| GT-03 | CHAIN-GROUNDING-COMPLETE | Step 7 | C-54 (citation chain PBI grounding verified) |
| GT-04 | CROSS-CITATION-CONSISTENT | Step 9 | C-60 (cross-layer citation consistency verified) |

Registry declared before Step 0. Diff GT-01..GT-04 against emitted tokens to verify completeness.

---

### Roles

**Enforcement Framer (EF)** -- Step 0 exclusively.

```
ENFORCEMENT FRAMER -- FUNCTION DECLARATION
----------------------------------------------------------------------
Function:     Constraint architecture only. Produces ENFORCEMENT
              MECHANISM DECLARATION at Step 0. Sets the structural
              rules downstream roles must follow.
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
              COVERAGE-RECORD at Step 1.
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

| Field | Content |
|-------|---------|
| Phase-exiting | [role + step] |
| Phase-entering | [role + step] |
| Artifacts-produced | [list of outputs produced in this phase] |
| Constraints-carried | [active constraints entering the next phase] |
| Registry-Ref | [T-ID from Phase Transition Registry] |
| Notes | [any handover-specific conditions] |

---

#### TOKEN CONTENT REQUIREMENT

Every gate token emitted in this artifact must carry inline specifics sufficient to verify its
pass condition without consulting the underlying artifact sections.

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

**Required format for CROSS-CITATION-CONSISTENT (GT-04):**

```
CROSS-CITATION-CONSISTENT: [K] TYPE-C citations checked;
  Belief-Ref artifacts and STATUS CELL artifacts verified identical
  per pair; all [K] rows MATCH -- cross-layer citation consistency
  confirmed.
```

The token must name the count checked ([K]) and assert per-pair identity. A token stating
"all consistent" without naming the count fails.

---

#### GATE-INDEPENDENCE-ENFORCED [C-56]

At any step boundary, each gate token must be emitted as an independent, separately labeled
token. Step 7: GT-02 and GT-03 are separate independent tokens.

---

#### MANIFEST-TOKEN-INLINE-EVIDENCE-SUFFIX [C-59]

MANIFEST-COMPLETE must self-certify citation accounting (C-52) and inline-evidence presence (C-57)
from token text alone. The C-59 suffix `(confirming artifact INLINE in all [Q] rows)` must appear
in TYPE-C RESOLVED. Suffix count [Q] must match actual TYPE-C row count.

---

#### MANIFEST-ROW-INLINE-EVIDENCE [C-57]

Each TYPE-C row must carry the confirming artifact in its STATUS CELL.
FORMAT: `RESOLVED (confirmed false by: [artifact name, namespace, date])`.
A bare `RESOLVED` fails.

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

---

### Steps 0-6

Each step produces a PHASE-HANDOVER table at exit. All tables use the 6-row Phase Handover
Schema with Registry-Ref row citing the T-ID from the Phase Transition Registry. All handover
tables carry Consumer-Ref entries.

### Step 3 Extension -- STILL-LIVE FILTER [C-51 extended Belief-Ref + C-53 Consumer-Ref]

Each row: MUST-ID + Scope + Action + Constraint + extended Belief-Ref + Consumer-Ref columns.

Extended Belief-Ref format: `PB-[NN] (confirmed false by: [artifact name, namespace, date])`.
A bare `PB-[NN]` without confirming artifact reference fails C-54 condition 1. A Belief-Ref
that names only an artifact type without name and date fails.

Consumer-Ref column: names the consuming step (IA-Step 7 or IA-Step 8) for each MUST row.

---

### Step 7 -- [IA] Hierarchy, Distillation, and Dual-Gate Emission [C-53+C-54+C-55+C-56]

After artifact content is complete, emit both Step 7 completeness gates as INDEPENDENT
self-certifying tokens per GATE-INDEPENDENCE-ENFORCED and TOKEN CONTENT REQUIREMENT:

Gate 1 (C-53) -- CONSUMER-INDEX-COMPLETE (GT-02):

`CONSUMER-INDEX-COMPLETE: BC-COVERAGE-RECORD Schema F-BCR-1..F-BCR-4 Consumer-Ref POPULATED, Phase Transition Registry T-00..T-06 Consumer-Ref POPULATED, STILL-LIVE FILTER MUST-1..MUST-4 Consumer-Ref POPULATED -- bidirectional navigability confirmed across all three axes.`

Gate 2 (C-54) -- CHAIN-GROUNDING-COMPLETE (GT-03):

`CHAIN-GROUNDING-COMPLETE: Belief-Ref cells EXTENDED (all MUST-[N] carry confirming artifact reference), F-BCR-4 SPECIFIC (names PB-[NN] through PB-[NN]) -- citation chain verified to evidence; both C-54 conditions confirmed.`

---

### Step 8 -- [IA] Citation-Completeness Manifest [C-52+C-55+C-57+C-59]

Produce CITATION-COMPLETENESS-MANIFEST:

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

---

### Step 9 -- [IA] Cross-Layer Citation Consistency Check [C-60]

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

If all rows MATCH, emit GT-04 per TOKEN CONTENT REQUIREMENT.

If any row shows MISMATCH: do not emit GT-04. Halt artifact production. Identify the discrepancy,
correct the source cell, and re-run the cross-layer check.

**Verification note:** A reviewer can verify CROSS-CITATION-CONSISTENT from the per-citation
table alone: the table enumerates each pair with both artifact names and the MATCH verdict.
No consultation of the STILL-LIVE FILTER or CITATION-COMPLETENESS-MANIFEST is required beyond
the table rows in this step.

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
  25. CITATION-COMPLETENESS-MANIFEST with MANIFEST-COMPLETE (Step 8; GT-01;
      C-59 inline-evidence suffix; TYPE-C STATUS CELL carries confirming artifact)
      (C-52+C-55+C-57+C-59)
  26. CROSS-CITATION-CONSISTENT per-citation table + token (Step 9; GT-04) (C-60)

Write to: simulations/topic/echo/{topic}-echo-{YYYY-MM-DD}.md

---

## What Made It Golden

**V-05 (A+B+C) vs V-01 (A only) -- four distinguishing patterns:**

### 1. Four-token registry currency (C-61, Axis A)

V-01 already had a three-token GATE-TOKEN-REGISTRY from R18 (C-58). V-05 self-extends the
registry to include GT-04 with step location (Step 9) and prerequisite criterion (C-60). Without
this, token completeness for GT-04 is scan-dependent -- a reviewer must traverse the full artifact
to confirm it exists. With the registry listing all four tokens, completeness is diff-detectable:
absent token = missing entry = instantly visible. This is the same diff-detectable completeness
contract that C-58 establishes for GT-01..GT-03, now extended to GT-04.

### 2. Format contract comprehensiveness (C-62, Axis B)

V-01 had TOKEN CONTENT REQUIREMENT covering GT-01..GT-03 only. V-05 adds the GT-04 format
contract: the token must name the count checked ([K]) and assert per-pair identity. "All
consistent" without naming the count fails. This closes the format-contract comprehensiveness gap
-- a reviewer auditing whether GT-04's token is self-certifying now has a declared standard to
diff against, not just a narrative to interpret.

### 3. Traversal-free verification scope declared explicit (C-63, Axis C)

V-01 produced the per-citation table at Step 9 but left the verification contract implicit. V-05
adds an explicit verification note naming what sections are NOT required: "No consultation of the
STILL-LIVE FILTER or CITATION-COMPLETENESS-MANIFEST is required beyond the table rows in this
step." This mirrors the C-55 self-certifying standard applied to GT-04's structural verification,
making the traversal-free guarantee explicit and auditable rather than implied.

### 4. Structural closure at all three axis intersections simultaneously

Each single-axis variation (V-01, V-02, V-03) scores 355 -- one criterion gained. V-04 (A+B)
reaches 360. V-05 alone closes all three simultaneously, reaching 365/365. The structural insight
is that C-61, C-62, and C-63 are all gated on C-60 (Step 9): any variation not including C-60
as its base cannot satisfy any of them. V-05 is the minimal prompt satisfying C-60 plus all
three axis improvements, making it the unique maximal point under v20.

---

## Final Rubric Criteria Summary

**Rubric:** v21 | **File:** `topic-echo-rubric-v21-2026-03-16.md`
**Score model:** 380 max (60 essential + 30 recommended + 290 aspirational / 58 criteria)
**V-05 under v21:** 365/380 -- R21 floor

### Essential (60 pts -- 12 each -- all must pass)

| ID | Criterion | Weight |
|----|-----------|:------:|
| C-01 | Named surprise with departure framing | 12 |
| C-02 | Signal tracing per surprise | 12 |
| C-03 | Design impact assessed per surprise | 12 |
| C-04 | Synthesis not summary | 12 |
| C-05 | Surprise specificity | 12 |

### R20 closure layer -- all PASS in golden (C-58..C-63, 5 each)

| ID | Pattern | Gate |
|----|---------|------|
| C-58 | GATE-TOKEN-REGISTRY-DECLARED | -- |
| C-59 | MANIFEST-TOKEN-INLINE-EVIDENCE-SUFFIX | C-52+C-57 |
| C-60 | CROSS-LAYER-CITATION-CONSISTENCY | C-51+C-52 |
| C-61 | GATE-TOKEN-REGISTRY-COVERS-DERIVED-GATE | C-58+C-60 |
| C-62 | TOKEN-CONTENT-REQUIREMENT-COMPREHENSIVE | C-59+C-60 |
| C-63 | CROSS-CITATION-TRAVERSAL-FREE-EXPLICIT | C-60 |

### R21 target layer -- all FAIL in golden (C-64..C-66, 5 each)

| ID | Pattern | Gap description |
|----|---------|-----------------|
| C-64 | GATE-TOKEN-REGISTRY-FORMAT-CROSS-REFERENCED | GT-04 registry entry and TOKEN CONTENT REQUIREMENT entry lack mutual cross-references |
| C-65 | TOKEN-CONTENT-REQUIREMENT-COVERAGE-DECLARED | TOKEN CONTENT REQUIREMENT header carries no explicit coverage declaration listing all 4 tokens |
| C-66 | TRAVERSAL-FREE-NOTE-SECTION-LIST-EXHAUSTIVE | Step 9 note names 2 sections not required; GATE-TOKEN-REGISTRY status left undeclared |

**Gate chain (R10 -> R20):**
R10 output auditable -> R11 non-defeatable -> R12 enforcement legible -> R13 structure navigable
-> R14 element addressable -> R15 address citation-activated -> R16 citation exhaustively
manifested, bidirectionally indexed, chain-grounded -> R17 tokens self-certifying, gates
independent, manifest rows inline-evidenced -> R18 token inventory declared, manifest token
extended, cross-layer citation consistent -> R19 registry self-extends for derived gate tokens,
token format contracts comprehensive, cross-citation verification traversal-free explicit ->
**R20 gate-token registry and format contract mutually cross-referenced, token format contract
coverage declared diff-detectable, traversal-free verification scope exhaustively enumerated.**
