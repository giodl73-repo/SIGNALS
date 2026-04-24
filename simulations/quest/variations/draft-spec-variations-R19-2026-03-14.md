Written to `simulations/quest/golden/draft-spec-variate-R19-2026-03-15.md`.

---

## Round 19 — draft-spec Variations Summary

**Axes explored and how they differ from R18:**

| | R18 axis | R19 axis |
|-|----------|----------|
| Role sequence | Architect-first scaffolding | Post-hoc Architect — explicit `HANDOFF TO ARCHITECT` statement at Phase 3 boundary; PM owns 0-2 entirely |
| Output format | Table-dominant (pipe tables everywhere) | Numbered checklist — hierarchical `1.1.1` notation; every block/gate/directive is a list item |
| Phrasing register | Second-person transitional frame (C-42 target) | MUST/SHALL modal — compliance-style language; `->` binding preserved for C-27 |
| Lifecycle + Inertia | STATUS-QUO-SNAPSHOT as expanded Phase 2 | Competition-first framing — `[STATUS-QUO-SNAPSHOT]` opens Phase 2 with explicit "map competitors before gaps" framing; same C-36/37/45/46 cluster |
| Full extension | Strategy scoping Phase 1.5 + `[STRATEGY-SCOPE-SEAL]` | Compliance Lead Phase 1.5 + `[COMPLIANCE-SCOPE-SEAL]` — C-40 wired through compliance scope declaration cross-referencing `[STATUS-QUO-SNAPSHOT]` structural fail rule |

**Predicted scores:**

| Variation | A-pass | A-fail | A-N/A | Composite |
|-----------|--------|--------|-------|-----------|
| V-01 | 27 | 4 | 8 | **148.85** |
| V-02 | 27 | 4 | 8 | **148.85** |
| V-03 | 27 | 4 | 8 | **148.85** |
| V-04 | 31 | 4 | 4 | **157.56** |
| V-05 | 39 | 0 | 0 | **175.00** |

**Key structural choices:**

- V-01's `HANDOFF TO ARCHITECT` label tests whether an explicit phase-boundary role transition statement changes any criterion evaluation (hypothesis: no, since C-43 requires structural ROLE markers at phase entries, not handoff prose).
- V-02's checklist format tests C-05 — whether `4.4.1 PURPOSE / 4.4.2 REQUIREMENTS...` labeled items satisfy "five guided sections in prescribed order" identically to prose-labeled sections (hypothesis: yes, named sections in order regardless of formatting surface).
- V-03's MUST/SHALL register is the first modal-language variation in the series; C-27's `->` binding is explicitly preserved to avoid a false fail.
- V-04 adds a 7th FINDINGS scan item (status-quo coverage) — above the C-29 minimum of 6, so C-29 still passes; the extra scan item tests whether rubric scoring is sensitive to scan count > 6 (it isn't — C-29 passes at >=6).
- V-05 uses `[COMPLIANCE-SCOPE-SEAL]`'s INVALID IF rule to cross-reference the C-37 structural fail rule inside `[STATUS-QUO-SNAPSHOT]` by name — this is C-40's cross-block rule dependency, with a different role flavor than R18's Strategy Lead.
