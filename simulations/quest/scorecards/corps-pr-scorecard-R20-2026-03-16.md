Now I have all I need. Let me produce the scorecard.

---

# Quest Score — corps-pr R20 (Rubric v17)

## Rubric Bands (v17)

| Band | Criteria | Per-criterion | Total |
|------|----------|--------------|-------|
| Essential | C-01--C-05 | 12.000 | 60 |
| Recommended | C-06--C-08 | 10.000 | 30 |
| Aspirational | C-09--C-54 (46 total) | ~0.217 | 10 |
| **Max** | | | **100** |

---

## Criterion-by-Criterion Audit

### Essential Band (C-01--C-05)

**C-01 — Phase A routing table complete; every file has a row; exact scope pattern cited; coverage gaps declared**

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PASS | Routing table template present; coverage gap line present |
| V-02 | PASS | Identical routing table template |
| V-03 | PASS | Passive phrasing: "The routing table is produced as follows" — structure unchanged |
| V-04 | PASS | Identical to V-01 routing section |
| V-05 | PASS | Passive phrasing + all routing elements intact |

**C-02 — Phase C technical reviews present; per-role output sequence declared**

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PASS | Phase C template with STEP 1–4 present; security-first sequence declared |
| V-02 | PASS | Phase C template intact; domain-first sequence |
| V-03 | PASS | Passive phrasing applied to Phase C instructions; STEP structure intact |
| V-04 | PASS | Security-first sequence + all Phase C mechanisms present |
| V-05 | PASS | All three axes; Phase C structure fully intact |

**C-03 — Phase D synthesis present; consensus covers all Phase C findings**

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PASS | Prose Phase D with Agreement/Divergence/Critical fields |
| V-02 | PASS | Ranked table format; all Phase C findings ranked; Critical finding named field |
| V-03 | PASS | Passive prose Phase D; IA cost ledger + Agreement + Divergence + Critical all present |
| V-04 | PASS | Ranked table; IA ledger named fields + Critical finding |
| V-05 | PASS | Ranked table + passive phrasing; IA ledger/position named fields + Critical finding |

**C-04 — Phase E decision present; exactly one GO / NO-GO / GO WITH CONDITIONS**

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PASS | "One decision. Values: GO, NO-GO, GO WITH CONDITIONS only. Delegated decisions fail. Hedged decisions fail." |
| V-02 | PASS | Identical Phase E |
| V-03 | PASS | Passive: "One decision is produced." — same enforcement |
| V-04 | PASS | Identical Phase E |
| V-05 | PASS | Identical Phase E (passive phrasing) |

**C-05 — Minimum 2 findings per role (F-01 IA-RESPONSE + ≥1 DOMAIN)**

| Variation | Result | Evidence |
|-----------|--------|----------|
| V-01 | PASS | `[minimum 2]` enforcement in findings template; F-01 + F-02 schema |
| V-02 | PASS | Identical findings template |
| V-03 | PASS | Identical findings template |
| V-04 | PASS | Identical findings template |
| V-05 | PASS | Identical findings template |

**Essential subtotal: all 5 PASS across all variations = 60 pts each**

---

### Recommended Band (C-06--C-08)

**C-06 — Coverage gaps declared with exact format string**

All 5 variations: PASS. Format string `COVERAGE GAP: [file] -- no org.yaml scope pattern covers this path.` present in all routing sections. V-03/V-05 passive variants use: "Coverage gaps are declared as: `COVERAGE GAP:...`" — structure identical.

**C-07 — Domain-lens gate applied per finding; two-step test stated**

All 5 variations: PASS. Domain-lens gate instructions present in STEP 4 of each Phase C template, with Step A (YES → include) and Step B (revise or drop) logic.

**C-08 — Post-commitment delta declared per role**

All 5 variations: PASS. `Post-commitment delta:` block with Pre-committed / After findings / HELD or CHANGED fields present in all findings sections.

**Recommended subtotal: all 3 PASS across all variations = 30 pts each**

---

### Aspirational Band (C-09--C-54, 46 criteria)

Grouping by structural cluster for audit efficiency:

**Phase B structural criteria (C-11, C-17, C-19, C-21, C-25, C-51, C-53)**

| Criterion | Requirement | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-------------|------|------|------|------|------|
| C-11 | IA sequenced first; structured as reference object | PASS | PASS | PASS | PASS | PASS |
| C-17 | Null hypothesis stated (B1) | PASS | PASS | PASS | PASS | PASS |
| C-19 | Cost ledger 4 rows × 2 columns × Net direction (B2) | PASS | PASS | PASS | PASS | PASS |
| C-21 | Four named cost categories present | PASS | PASS | PASS | PASS | PASS |
| C-25 | Budget verdict: three labeled lines, each string-matchable | PASS | PASS | PASS | PASS | PASS |
| **C-51** | IA section header carries adversarial designation label `Status-quo champion [C-11]:` | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |
| **C-53** | Budget verdict lines carry `[C-25]` governing criterion annotation per line | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |

Evidence for C-51 (all variations):
- V-01/V-02/V-04: `Status-quo champion [C-11]: First reviewer in the pipeline.`
- V-03/V-05: `Status-quo champion [C-11]: The first reviewer in the pipeline.`
Label auditable by label-reading alone in all five.

Evidence for C-53 (all variations):
```
WORSE rows: [...]               <- B3 line 1 [C-25]
BETTER rows: [...]              <- B3 line 2 [C-25]
Conclusion: [...]               <- B3 line 3 [C-25]
```
All three annotation slots present in identical form across all five variations.

**Phase C pipeline declaration criteria (C-22, C-26, C-52)**

| Criterion | Requirement | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-------------|------|------|------|------|------|
| C-22 | Two independently auditable sub-conditions (C1/C2) with exact result tokens | PASS | PASS | PASS | PASS | PASS |
| C-26 | Named result tokens (C1 RESULT / C2 RESULT) with sub-condition scopes | PASS | PASS | PASS | PASS | PASS |
| **C-52** | C1 and C2 sub-condition headers carry bracketed criterion annotations `[C-26]` | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |

Evidence for C-52 (all variations):
```
C1 (Phase B exit pre-flight, phase-level) [C-26]:
C2 (READ RECEIPT completeness, per-role) [C-26/C-33]:
```
Both sub-condition headers annotated identically across all five variations; governing criterion traceable without consulting rubric.

**Phase C READ RECEIPT / C2 RESULT criteria (C-27, C-33, C-35, C-36, C-37, C-39, C-54)**

| Criterion | Requirement | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-------------|------|------|------|------|------|
| C-27 | PRE-COMMITMENT block precedes findings table | PASS | PASS | PASS | PASS | PASS |
| C-33 | READ RECEIPT fields (a)-(e) all present | PASS | PASS | PASS | PASS | PASS |
| C-35 | C2 RESULT must appear after READ RECEIPT in output | PASS | PASS | PASS | PASS | PASS |
| C-36 | Ordering declared as Phase C exit-condition failure | PASS | PASS | PASS | PASS | PASS |
| C-37 | C2 RESULT block enumerates (a)-(e) with PRESENT/ABSENT | PASS | PASS | PASS | PASS | PASS |
| C-39 | Evidence + terminal verdict co-appear in same C2 RESULT block | PASS | PASS | PASS | PASS | PASS |
| **C-54** | Field (e) names both valid forms as explicit disjuncts | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** |

Evidence for C-54 (all variations):
```
(e) Initial position stated:  PRESENT / ABSENT
    [valid: inline value OR cross-reference "see PRE-COMMITMENT block: [row]"]
```
Both valid evidence forms named as disjuncts in field (e) validation instruction, identical across all five variations.

**F-01 IA-RESPONSE column-header criteria (C-14, C-15, C-18, C-20, C-34, C-38, C-40)**

All 5 variations: PASS. Findings table schema `| ID | Type | Severity | [IA-VERDICT] | [ROLE-MECHANISM] | Domain-Lens | Owner | Resolution |` present in all. [IA-VERDICT] and [ROLE-MECHANISM] are column headers throughout; F-01 format rules section present in all.

**Three-level structural enforcement criteria (C-41, C-46, C-43, C-45, C-49, C-50)**

| Criterion | Requirement | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-------------|------|------|------|------|------|
| C-41 | Three-level enforcement partition declared with level names | PASS | PASS | PASS | PASS | PASS |
| C-46 | `Eliminated [C-46]:` label in enforcement declaration | PASS | PASS | PASS | PASS | PASS |
| C-43 | CLOSED PATHS section in pipeline declaration | PASS | PASS | PASS | PASS | PASS |
| C-45 | Format-rules restatement in CLOSED PATHS | PASS | PASS | PASS | PASS | PASS |
| C-49 | Eliminated carries back-reference to CLOSED PATHS | PASS | PASS | PASS | PASS | PASS |
| C-50 | Audit loop closed: bidirectional cross-reference declared | PASS | PASS | PASS | PASS | PASS |

**Phase D synthesis criteria (C-09, C-12, C-13)**

| Criterion | Requirement | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-------------|------|------|------|------|------|
| C-09 | Consensus covers all roles from Phase C | PASS | PASS | PASS | PASS | PASS |
| C-12 | Ban-to-fix check present for perspective-label phrases | PASS | PASS | PASS | PASS | PASS |
| C-13 | Mechanism naming: architectural fact required | PASS | PASS | PASS | PASS | PASS |

Note on V-02/V-04/V-05 Phase D: the ranked table format does not weaken C-12/C-13 — it strengthens them. The Mechanism column ban-to-fix reference table is embedded directly in the Phase D output template, making each cell independently auditable by column scan.

**Phase E criteria (C-10)**

All 5 variations: PASS. Conditions name sign-off role. Delegated/hedged decision failure declared.

**Remaining aspirational criteria (C-09 through C-24, C-28--C-48 not individually listed above)**

All 5 variations: PASS. The structural templates for all phases (Phase A routing format, Phase B cost ledger structure, Phase C per-role output sequence with STEP 1-4, Phase D synthesis, Phase E decision) are identical or equivalently structured across all five variations. No regression introduced by the three axes.

**Aspirational subtotal: 46/46 PASS across all variations = 10 pts each**

---

## Composite Scores

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Composite |
|-----------|---------------|-----------------|------------------|-----------|
| V-01 | 60 | 30 | 10 | **100** |
| V-02 | 60 | 30 | 10 | **100** |
| V-03 | 60 | 30 | 10 | **100** |
| V-04 | 60 | 30 | 10 | **100** |
| V-05 | 60 | 30 | 10 | **100** |

**All five variations: 100/100. Tied for first.**

---

## Hypothesis Verification

| Hypothesis | Verified? | Notes |
|-----------|-----------|-------|
| V-01: C-35/C-36 ordering is per-role, not cross-role — sequence reversal has zero impact | YES | Security-first role ordering does not disturb STEP 1 → STEP 2 within any role |
| V-02: C-12/C-13 ban-to-fix survives Phase D format substitution — Mechanism column is the new audit surface | YES | Mechanism column ban-to-fix reference table embedded in Phase D template makes check O(1) per row |
| V-03: Passive phrasing doesn't induce annotation omissions — all four patterns in self-contained schema slots | YES | C-51/C-52/C-53/C-54 annotations are in template positions untouched by prose register change |
| V-04/V-05: The three axes affect disjoint structural regions — no interaction effects | YES | Phase C order, Phase D format, surface prose are mutually independent; combination shows no degradation |

---

## Axis Independence Confirmation

**Role Sequence (V-01 axis)**: Affects only which role runs first within Phase C. The per-role STEP 1 → STEP 2 ordering constraint (C-35/C-36) is within-role, not cross-role. Security-first sequence leaves all annotation criteria untouched.

**Phase D Table (V-02 axis)**: Replaces Phase D prose paragraphs with a ranked finding table + named IA ledger fields. The C-51/C-52/C-53/C-54 annotations are embedded in Phase B and Phase C templates, which Phase D format change cannot reach. The table format makes C-12 (ban-to-fix) more auditable (O(1) per Mechanism cell), not less.

**Phrasing Register (V-03 axis)**: Converts imperative instructions to formal declarative passive. All four annotation invariants live in schema slots (Phase B header label, sub-condition headers, Budget verdict line suffixes, C2 RESULT field instruction). These slots carry no imperative framing; passive re-framing of surrounding prose leaves them intact.

---

## Excellence Signals from R20

### Signal 1: Phase D ranked table embeds inline Mechanism-column ban-to-fix reference table

In V-02/V-04/V-05, the Phase D ranked consensus table template includes the banned-phrase reference table directly adjacent to the Mechanism column declaration:

```
Mechanism column ban-to-fix:
- Each Mechanism cell must name an architectural fact. Banned phrases fail even if a code
  mechanism is also named.

| Banned phrase | Required replacement form |
|---|---|
| "different perspectives" | "[role-A] sees [mechanism X]; [role-B] sees [mechanism Y]" |
...
```

This is structurally parallel to how CLOSED PATHS in the pipeline declaration names the prohibited inline-cell-label path. Both are declaration-point enforcement: the rule is stated at the output template, not in a separate policy section. An auditor checking the Mechanism column can verify compliance by scanning each cell against the reference table co-located in the same section. C-12's ban-to-fix requirement becomes O(1) per row (read Mechanism cell, scan for banned phrases) rather than requiring prose parsing.

This pattern could ground a new criterion: **Phase D ban-to-fix reference table co-located with Mechanism column declaration** — auditable without cross-section lookup.

### Signal 2: Phase D named-field preamble achieves structural symmetry with Phase C named blocks

In V-02/V-04/V-05, the Phase D preamble is rendered as named fields:

```
IA ledger:      Budget strength [HIGH / MEDIUM / LOW]; WORSE rows [restate]; BETTER rows [restate].
IA position:    Technical roles [reinforced / challenged / defeated] the IA's estimate.
```

This mirrors the named-block convention used throughout Phase C (READ RECEIPT, C2 RESULT, PRE-COMMITMENT). Every structured output block in the pipeline has a named header. Phase D preamble as named fields extends this convention to the synthesis section, making the IA ledger summary auditable by label-matching (`IA ledger:`) rather than requiring prose parsing.

This pattern could ground a new criterion: **Phase D IA ledger summary rendered as named fields** — consistent with the pipeline-wide named-block convention.

---

## Rankings

All five tied at 100/100. Differentiation by structural contribution:

| Rank | Variation | Score | Distinguishing Feature |
|------|-----------|-------|----------------------|
| T-1 | V-05 | 100 | Full combination — confirms all three axes orthogonal; strongest axis-independence proof |
| T-1 | V-04 | 100 | Two-axis combination — security-first + Phase D table; strongest coverage of new Phase D audit surface |
| T-1 | V-02 | 100 | Phase D table introduces both new excellence signals; primary source of R20 patterns |
| T-1 | V-01 | 100 | Cleanest isolation of role-sequence invariance |
| T-1 | V-03 | 100 | Cleanest isolation of phrasing-register invariance |

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Phase D ranked table embeds inline Mechanism-column ban-to-fix reference table co-located with the Mechanism column declaration -- ban-to-fix compliance becomes O(1) per row by cell scan, parallel to CLOSED PATHS declaration-point enforcement", "Phase D IA ledger summary rendered as named fields (IA ledger:, IA position:) -- extends pipeline-wide named-block convention to synthesis preamble, making ledger summary auditable by label-matching without prose parsing"]}
```
