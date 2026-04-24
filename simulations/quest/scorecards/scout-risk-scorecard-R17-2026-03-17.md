---
skill: scout-risk
round: 17
rubric_version: v16
date: 2026-03-17
top_score: 174
golden_band: 168-174
result: GOLDEN
---

# Scout-Risk — Quest Score — Round 17

## Rubric Version: v16 | Max Composite: 174 | Golden Band: 168–174

---

## Scoring Summary

| Variation | C-01..C-47 | C-48 | C-49 | C-50 | Composite | Band |
|-----------|-----------|------|------|------|-----------|------|
| Baseline (R16 V-05) | 168/168 | PASS (2) | PASS (2) | FAIL (0) | 172/174 | Strong |
| V-01 | 168/168 | PASS (2) | PASS (2) | PARTIAL (1) | 173/174 | Strong |
| V-02 | 168/168 | PASS (2) | PASS (2) | PARTIAL (1) | 173/174 | Strong |
| V-03 | 168/168 | PASS (2) | PASS (2) | PASS (2) | **174/174** | **GOLDEN** |
| V-04 | 168/168 | PASS (2) | PASS (2) | PASS (2) | **174/174** | **GOLDEN** |
| V-05 | 168/168 | PASS (2) | PASS (2) | PASS (2) | **174/174** | **GOLDEN** |

**Rank**: V-03 = V-04 = V-05 (174/174) > V-01 = V-02 (173/174)

All essential criteria (C-01 through C-05) pass in all variations.

---

## Criterion-by-Criterion Evaluation

### C-01 through C-47 — All Variations

**Result: PASS across all variations (168/168)**

All variations inherit R16 V-05's fully-passing baseline on C-01 through C-47. The R17 changes are strictly additive — sentences appended to Phase 0c, citation text upgraded at prohibition sites — with no existing content removed or modified. No criterion in this block is affected.

---

### C-48 — Violation taxonomy block is structurally independent

**Pass condition**: Violation taxonomy is a standalone named pre-phase block of parallel structural weight to the mitigation taxonomy, not embedded as a sub-section within any existing phase.

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS (2) | Phase 0c is a `### Phase 0c —` heading at the same markdown level as Phase 0 and Phase 0b — standalone block, not embedded inside any existing phase |
| V-02 | PASS (2) | Same structural placement as V-01 |
| V-03 | PASS (2) | Same structural placement |
| V-04 | PASS (2) | Structural parity now also explicitly stated in the opening sentence: "This block is a pre-phase reference block of equal structural weight to Phase 0 — both declare a closed vocabulary before any generation phase executes." C-48 is now verifiable by local inspection without inferring from document ordering. |
| V-05 | PASS (2) | Same explicit parity statement as V-04 |

All variations: **2/2**

---

### C-49 — Each typed prohibition site carries an explicit citation to the violation taxonomy

**Pass condition**: Every typed prohibition must include an inline citation to the taxonomy block by name — drawn-from is verifiable by local inspection, not by inferring from document ordering.

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS (2) | All prohibition sites carry `(Phase 0c taxonomy)` — identical to R16 V-05 baseline |
| V-02 | PASS (2) | Same citations as V-01 |
| V-03 | PASS (2) | Same citations |
| V-04 | PASS (2) | Same citations — `(Phase 0c taxonomy)` shorthand already satisfies criterion |
| V-05 | PASS (2) | Citations upgraded to `(Phase 0c Violation Taxonomy)` at all 5 prohibition sites; Phase 0c header announces: "Every prohibition site in this prompt cites this block by its full name: Phase 0c Violation Taxonomy." C-49 is now verifiable by exact character-level matching against the block heading. |

All variations: **2/2**

Note: V-05 exceeds the pass condition — using the exact block heading name rather than a shorthand makes the citation verifiable without abbreviation resolution. C-49 was already PASS at 2 pts, so no score change.

---

### C-50 — Violation taxonomy block includes an explicit closure declaration sentence

**Pass condition (compound AND)**: The taxonomy block must contain:
1. A sentence declaring it closed
2. A prohibition on unlisted categories at any prohibition site

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PARTIAL (1) | Adds only "This taxonomy is closed." — satisfies half 1 (closure declaration) but absent the prohibition clause. C-50's AND compound is not fully satisfied. |
| V-02 | PARTIAL (1) | Adds only "No violation category outside this list may be named at any prohibition site." — satisfies half 2 (prohibition clause) but absent the closure declaration. C-50's AND compound is not fully satisfied. |
| V-03 | PASS (2) | Both sentences present: "This taxonomy is closed. No violation category outside this list may be named at any prohibition site." — compound AND requirement fully satisfied. |
| V-04 | PASS (2) | Same two-sentence closure as V-03. PASS at maximum. |
| V-05 | PASS (2) | Same two-sentence closure as V-03/V-04. PASS at maximum. |

**Key finding**: V-01 and V-02 serve as deliberate isolation tests. Both land at PARTIAL, confirming that C-50's compound requirement enforces the AND — neither half alone is sufficient. V-03 is the minimal form for PASS.

---

## Variation Profiles

### V-01 — 173/174
Single-axis: closure declaration only ("This taxonomy is closed."). C-50 half 1 present, half 2 absent. PARTIAL on C-50. Confirms the AND compound is enforced.

### V-02 — 173/174
Single-axis: prohibition clause only ("No violation category..."). C-50 half 2 present, half 1 absent. PARTIAL on C-50. Confirms neither half alone suffices.

### V-03 — 174/174 (minimal golden form)
Single-axis: full two-sentence closure. Both C-50 halves present. Minimal surgery over R16 V-05. The safe reference implementation.

### V-04 — 174/174 (structural clarity upgrade)
V-03 plus explicit structural parity sentence in Phase 0c header. C-48 is now locally verifiable by inspection, not inferred from document structure. No additional score change (C-48 was already PASS).

### V-05 — 174/174 (maximum precision)
V-04 plus fully-qualified citation names at all prohibition sites (`Phase 0c Violation Taxonomy`). C-49 is now verifiable by character-level matching against the block heading. No additional score change (C-49 was already PASS). Maximum expression of all three v16 criteria.

---

## Ranking

| Rank | Variation | Score | Rationale |
|------|-----------|-------|-----------|
| 1 (tie) | V-03 | 174/174 | Minimal golden — cleanest upgrade path |
| 1 (tie) | V-04 | 174/174 | C-48 self-evident by local inspection |
| 1 (tie) | V-05 | 174/174 | All three v16 criteria at maximum precision |
| 4 (tie) | V-01 | 173/174 | C-50 half 1 only |
| 4 (tie) | V-02 | 173/174 | C-50 half 2 only |

**Recommended canonical**: V-03 for minimal stable form; V-05 for maximum audit precision.

---

## Excellence Signals

### Signal 1 — C-50 compound isolation testing
V-01 (half 1) and V-02 (half 2) isolate each component of C-50's AND compound. Both land at PARTIAL, proving the rubric enforces the full compound — not just the stronger or more behavioral half. The isolation pattern surfaces whether "AND" means "either satisfies" or "both required." In C-50: both are required.

### Signal 2 — Explicit structural parity declaration (V-04, V-05)
C-48 requires structural independence "of parallel structural weight." In V-01 through V-03, this is inferred from document ordering (Phase 0c is a `###` sibling of Phase 0). V-04 makes the parity assertion explicit within Phase 0c's first sentence: "equal structural weight to Phase 0." No inference from outside the block is needed. This converts a structural convention to a stated constraint — the same progression as C-50 (enumeration closure → explicit closure rule).

### Signal 3 — Exact block name at citation sites (V-05)
C-49 requires that each prohibition site cite the taxonomy block "by name." In V-01 through V-04, citations use the shorthand `(Phase 0c taxonomy)` — this satisfies the criterion but requires the reader to resolve the abbreviation. V-05 upgrades all 5 prohibition sites to cite `(Phase 0c Violation Taxonomy)`, the exact string from the block heading. Verification reduces to: citation text == block heading name. The pattern generalizes: when a criterion requires "by name," using the exact declared name (not an abbreviation) maximizes verifiability precision.

---

## New Patterns Captured

1. **Compound criterion isolation testing**: Design V-01 and V-02 as deliberate isolation experiments for C-50's AND halves. Both landing at PARTIAL confirms the compound is enforced, not merely suggested.

2. **Explicit structural parity declaration**: State "equal structural weight to [peer block]" directly in the subordinate block's opening sentence — converts inferred structural equivalence to a locally verifiable stated constraint.

3. **Fully-qualified block name at prohibition sites**: Use the exact heading string as the citation text at every prohibition site — makes drawn-from verifiable by character-level match against the declared block name, eliminating abbreviation resolution.

---

```json
{"top_score": 174, "all_essential_pass": true, "new_patterns": ["compound criterion isolation testing: V-01 and V-02 prove C-50 AND compound is enforced — closure declaration alone (V-01) and prohibition clause alone (V-02) both land at PARTIAL, confirming both halves are required", "explicit structural parity declaration: stating equal structural weight to peer block within the block opening converts inferred structural equivalence to a locally verifiable stated constraint", "fully-qualified block name at citation sites: using exact block heading string as citation text makes drawn-from verifiable by character-level match, eliminating abbreviation resolution"]}
```
