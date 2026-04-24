## topic-retro — Round 12 Quest Score

**Rubric:** v10 (C-01–C-31)
**Base:** R11-V-05, carrying C-01–C-29 PASS (C-10, C-22 N/A in non-AMEND)
**Denominator:** 132 (non-AMEND: C-10 and C-22 excluded)
**Base score before C-30/C-31:** 128/132

---

## Baseline Established

R11-V-05 passed all C-01–C-29 (with C-10 and C-22 non-applicable in non-AMEND context):
- Essential (C-01–C-05): 60/60
- Recommended (C-06–C-08): 30/30
- Aspirational C-09,C-11–C-21,C-23–C-29: 38/38

**Base = 128/132.** The four open points = C-30 (2 pts) and C-31 (2 pts).

---

## Per-Variation Evaluation

### C-30 Rubric Anchor

**PASS condition:** Phase 8 SEAL carries COPY-VERIFIED label AND copy-source as **independently addressable named fields** — not fused as inline commentary on one `This score` item.

**PARTIAL condition:** Copy instruction present but SEAL lacks the field-level separation.

### C-31 Rubric Anchor

**PASS condition:** Explicit dedicated section (header + content) naming specific guarantees by mechanism — not embedded in phase text, not a trailing bullet list appended to phase content.

**PARTIAL condition:** Guarantees present in phase specs but no dedicated summary section.

---

### V-01 — SEAL Separation: Three Named Fields in Phase 8 SEAL

#### C-30

Phase 8 SEAL separates into three independent items:
```
[ ] This score: {number}/100 — value must be present and non-blank
[ ] COPY-VERIFIED: confirmed — value traced to Phase 6 verdict sentence; not recomputed from Phase 4 TOTAL
[ ] COPY-SOURCE: "Phase 6 verdict sentence" — authoritative source is Phase 6, not Phase 4; confirm by reading Phase 6 directly
```

`COPY-VERIFIED` and `COPY-SOURCE` are separate SEAL fields — independently confirmable, not inline commentary. **PASS.**

#### C-31

V-01 retains the R11-V-05 trailing bullet list: `Design guarantees: - Phase 1: Echo locked... - Phase 8: Score COPIED from Phase 6...`. No section header; appended after Phase 9 as flowing text. Content names specific mechanisms but lacks the structural separation that makes it independently locatable. **PARTIAL.**

| Criterion | Result | Pts |
|-----------|--------|-----|
| C-01–C-05 | PASS (carried) | 60 |
| C-06–C-08 | PASS (carried) | 30 |
| C-09,C-11–C-21,C-23–C-29 | PASS (carried) | 38 |
| C-30 | **PASS** | 2 |
| C-31 | **PARTIAL** | 1 |
| **Total** | | **131/132** |

---

### V-02 — Guarantees Table: `## DESIGN GUARANTEES` Section

#### C-30

Phase 8 SEAL uses the R11-V-05 single-item form:
```
[ ] This score: {number}/100 — COPY-VERIFIED: confirm this number matches the score in the Phase 6 verdict sentence by reading Phase 6 directly (do not recompute from Phase 4 TOTAL; the copy source is Phase 6 verdict, not Phase 4)
```

Both COPY-VERIFIED and "Phase 6 verdict" are present as inline commentary on one `This score` item — exactly the fusion pattern identified as the C-30 gap. **PARTIAL.**

#### C-31

V-02 replaces the trailing bullet list with:
```markdown
## DESIGN GUARANTEES

Each row names a mechanism and states the structural decision that enforces it.

| Mechanism | Structural guarantee — what is enforced and how |
|-----------|------------------------------------------------|
| Echo lock | Phase 1 runs before signal comparison; ... |
| Copy guard — body | ... |
| Copy guard — SEAL | Phase 8 SEAL carries three named fields: `This score` (value); `COPY-VERIFIED` (...); `COPY-SOURCE` (...) |
...
```

The `## DESIGN GUARANTEES` header creates a structurally dedicated section, independently locatable without reading phase specifications. Two-column table (Mechanism / Guarantee) makes each guarantee auditable by name. **PASS.**

| Criterion | Result | Pts |
|-----------|--------|-----|
| C-01–C-05 | PASS (carried) | 60 |
| C-06–C-08 | PASS (carried) | 30 |
| C-09,C-11–C-21,C-23–C-29 | PASS (carried) | 38 |
| C-30 | **PARTIAL** | 1 |
| C-31 | **PASS** | 2 |
| **Total** | | **131/132** |

---

### V-03 — Phrasing Register: SCORE TRANSFER COMMAND + EXECUTION CONTRACT

#### C-30

SCORE TRANSFER COMMAND (body):
> Step 3: Copy it verbatim into the "This score" cell. Label the cell: COPY-VERIFIED [source: Phase 6 verdict].

Phase 8 SEAL:
```
[ ] This score: {number}/100 — labeled COPY-VERIFIED [source: Phase 6 verdict]; source named as Phase 6, not Phase 4
```

Both the label and the source name are present. However, the SEAL has one item encoding both, not two independently addressable fields. C-30 requires the SEAL to encode verified state AND copy source as *named fields* (independently confirmable). The body instruction is richer than R11-V-05, but the SEAL structure does not separate them. **PARTIAL.**

Evidence: The SCORE TRANSFER COMMAND block encodes both in prose step 3; the SEAL has one item with both fused. C-30's "named fields" requirement targets the SEAL structure, not the body narrative.

#### C-31

EXECUTION CONTRACT block:
```
**EXECUTION CONTRACT — structural guarantees that must hold across all phases:**

- **Echo lock**: Do not modify the Phase 1 Echo...
- **Score copy guard**: Do not derive the Phase 8 score. Read Phase 6. Copy it. Name the source. Label the cell COPY-VERIFIED [source: Phase 6 verdict]. Any derived number — even if it matches — is a transfer failure.
- **Seal format contracts**: Do not treat seals as checklists to be acknowledged...
```

This is a dedicated section with a header (`**EXECUTION CONTRACT...**`), distinct from phase specifications, naming specific mechanisms by label (echo lock, score copy guard, seal format contracts, etc.). C-31 requires "a dedicated section or block that documents the key structural decisions... in a readable form." Prose imperative format satisfies "readable form." Specific mechanisms are named, not just asserted. **PASS.**

| Criterion | Result | Pts |
|-----------|--------|-----|
| C-01–C-05 | PASS (carried) | 60 |
| C-06–C-08 | PASS (carried) | 30 |
| C-09,C-11–C-21,C-23–C-29 | PASS (carried) | 38 |
| C-30 | **PARTIAL** | 1 |
| C-31 | **PASS** | 2 |
| **Total** | | **131/132** |

---

### V-04 — Combined: Three-Field SEAL (V-01) + Guarantees Table (V-02)

#### C-30

Phase 8 SEAL carries three separate named items — identical to V-01:
```
[ ] This score: {number}/100 — value must be present and non-blank
[ ] COPY-VERIFIED: confirmed — traced to Phase 6 verdict, not recomputed from Phase 4 TOTAL
[ ] COPY-SOURCE: "Phase 6 verdict sentence" — authoritative source is Phase 6; confirm by reading Phase 6 directly
```

Three independent, separately addressable SEAL fields. **PASS.**

#### C-31

`## DESIGN GUARANTEES` two-column table with section header — identical to V-02. Dedicated section, independently locatable, each guarantee named by mechanism. Explicitly names the three-field SEAL structure in the "Copy guard — SEAL" row. **PASS.**

No regressions: V-04 is a zero-interference combination. V-01's Phase 8 SEAL changes affect only Phase 8. V-02's design-guarantees section changes affect only the post-execution section. All prior-passing criteria unchanged.

| Criterion | Result | Pts |
|-----------|--------|-----|
| C-01–C-05 | PASS (carried) | 60 |
| C-06–C-08 | PASS (carried) | 30 |
| C-09,C-11–C-21,C-23–C-29 | PASS (carried) | 38 |
| C-30 | **PASS** | 2 |
| C-31 | **PASS** | 2 |
| **Total** | | **132/132** |

---

### V-05 — Full Integration: Three-Field SEAL + Pre-Execution Contract + Cell Format String

#### C-30

Three structural locations carry the named fields:

1. **Phase 8 body:** "COPY the accuracy score from the Phase 6 verdict sentence… Label the cell: COPY-VERIFIED [source: Phase 6 verdict]."
2. **Phase 8 table cell format string:** `{number}/100 — COPY-VERIFIED [source: Phase 6 verdict]` (inline in the table template itself)
3. **Phase 8 SEAL:** Three independent fields — `This score`, `COPY-VERIFIED` (operation confirmed), `COPY-SOURCE` ("Phase 6 verdict sentence")

SEAL structure satisfies the "named fields" requirement identically to V-04. Cell-format-string and PRE-EXECUTION CONTRACT add redundant anchors. **PASS.**

#### C-31

PRE-EXECUTION CONTRACT (placed **before Phase 1**):
```markdown
## PRE-EXECUTION CONTRACT

The following structural guarantees must hold across all phases. Read before executing Phase 1.

| Mechanism | Structural guarantee — what is enforced and how |
| Echo lock | Phase 1 runs before signal comparison; ... |
| Copy guard | Phase 8: score COPIED from Phase 6 verdict sentence verbatim; cell labeled COPY-VERIFIED [source: Phase 6 verdict]; SEAL carries three named fields: This score, COPY-VERIFIED, COPY-SOURCE |
...
```

Plus a condensed trailing "Design guarantees (audit reference)" bullet list retained post-Phase-9.

The PRE-EXECUTION CONTRACT is a dedicated section with a `##` header, positioned before Phase 1 — structurally prior to execution, not embedded in phase text. A reviewer reading the output encounters the guarantees table before any phase output. **PASS.**

No regressions: Pre-execution contract, cell-level format string, and three-field SEAL are all additive. No prior-passing criteria removed or weakened.

| Criterion | Result | Pts |
|-----------|--------|-----|
| C-01–C-05 | PASS (carried) | 60 |
| C-06–C-08 | PASS (carried) | 30 |
| C-09,C-11–C-21,C-23–C-29 | PASS (carried) | 38 |
| C-30 | **PASS** | 2 |
| C-31 | **PASS** | 2 |
| **Total** | | **132/132** |

---

## Composite Scores

| Rank | ID | C-30 | C-31 | Score | % |
|------|----|------|------|-------|---|
| 1 (tie) | **V-04** | PASS (2) | PASS (2) | **132/132** | 100% |
| 1 (tie) | **V-05** | PASS (2) | PASS (2) | **132/132** | 100% |
| 3 (tie) | V-01 | PASS (2) | PARTIAL (1) | 131/132 | 99.2% |
| 3 (tie) | V-02 | PARTIAL (1) | PASS (2) | 131/132 | 99.2% |
| 3 (tie) | V-03 | PARTIAL (1) | PASS (2) | 131/132 | 99.2% |

**All essential criteria: YES** (C-01–C-05 carried from R11-V-05 in all variations)

---

## Excellence Signals from Top-Scoring Variations

### V-04 — Minimum Integration to Ceiling

V-04 establishes the structural minimum for achieving C-30 + C-31 simultaneously:
- **C-30:** Three independent SEAL fields (`This score` / `COPY-VERIFIED` / `COPY-SOURCE`) with no other changes to Phase 8 body
- **C-31:** `## DESIGN GUARANTEES` header section with two-column table, positioned after Phase 9
- **Zero interference:** Independent locations means zero risk of phase-level regression

The V-04 pattern: *to elevate from inline annotation to named fields, split the single fused SEAL item into the minimum set of independent entries that each carry one semantic role.*

### V-05 — Prospective Contract Positioning

V-05's key structural innovation beyond V-04:

1. **PRE-EXECUTION CONTRACT pattern:** Moving the guarantees table *before Phase 1* transforms it from a retrospective summary into a prospective commitment. An auditor reads the contract before any phase output, enabling audit-before-execution rather than audit-after-completion. This is a new structural pattern not yet captured in any existing criterion.

2. **Cell-level format string as third copy-guard anchor:** The Phase 8 table template itself carries `{number}/100 — COPY-VERIFIED [source: Phase 6 verdict]` inline. This means even the empty table template signals the required label — the format string is visible before any score is copied, making the contract discoverable at the point of action rather than only in the SEAL.

3. **Guarantee-section as dual-position artifact:** PRE-EXECUTION CONTRACT (upfront commitment) + condensed trailing reference (post-execution audit check) — two roles, same content. The pre-position is prospective; the post-position is confirmatory. This pattern has no current criterion.

### Why V-01 = V-02 = V-03 < V-04

The single-axis variations achieve 131 because each targets only one of the two new criteria. V-01 PASS on C-30 but PARTIAL on C-31 (bullet list, no header section). V-02/V-03 PASS on C-31 but PARTIAL on C-30 (single fused SEAL item, not independent named fields). The single-axis experiments confirm independence: the two criteria are structurally non-interfering.

---

## New Patterns for Candidate Criteria

| Pattern | Source | Potential criterion |
|---------|--------|---------------------|
| Pre-execution contract placement | V-05 `## PRE-EXECUTION CONTRACT` before Phase 1 | Guarantees section positioned prospectively (before execution) rather than retrospectively (after phases) |
| Cell-level copy-guard format string | V-05 Phase 8 table cell `{number}/100 — COPY-VERIFIED [source: Phase 6 verdict]` | Phase 8 table template itself carries the COPY-VERIFIED label inline — third structural anchor beyond body instruction and SEAL |

---

```json
{"top_score": 132, "all_essential_pass": true, "new_patterns": ["pre-execution contract placement — guarantees section positioned before Phase 1 as a prospective commitment rather than a post-phase retrospective summary", "cell-level copy-guard format string — Phase 8 table cell template carries COPY-VERIFIED label inline, making the copy contract visible at the point of action before the SEAL is reached"]}
```
