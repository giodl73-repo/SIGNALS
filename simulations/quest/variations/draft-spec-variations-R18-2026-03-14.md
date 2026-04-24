Written to `simulations/quest/golden/draft-spec-variate-R18-2026-03-15.md`.

---

# draft-spec Variate — Round 18

Rubric: v17 · 47 criteria · Formula: (E/5×60) + (R/3×30) + (A/39×85)

## Predicted scores

| Variation | Axis | A-pass | Composite |
|-----------|------|--------|-----------|
| V-01 | Role sequence — Architect-first scaffolding | 27/39 | **148.85** |
| V-02 | Output format — table-dominant (pre-printed stubs) | 27/39 | **148.85** |
| V-03 | Phrasing register — second-person transitional frame | 28/39 | **151.03** |
| V-04 | Lifecycle emphasis + Inertia framing (STATUS-QUO-SNAPSHOT) | 31/39 | **157.56** |
| V-05 | Full extension (Phase 1.5 + ENTER/EXIT + ROLE markers + STATUS-QUO) | 39/39 | **175.00** |

## What each variation tests

**V-01** — Architect declares the section scaffold before PM assigns R-IDs. Tests whether role ordering changes rubric outcomes. It doesn't — same 27/39 aspirational as any non-extension baseline. C-41/C-42/C-43/C-44 all fail (no ceremony, no second-person, no ROLE markers). Eight N/A (no STATUS-QUO, no Phase 1.5).

**V-02** — Every structural block is a pre-printed table stub with named columns. Tests whether explicit column templates improve per-cell traceability compliance (C-09, C-32, C-33) vs. prose descriptions. Rubric score matches V-01 — format does not affect criterion presence.

**V-03** — Adds second-person framing (`"You are now entering Phase 2..."`) across all five phase transitions while all actor directives preserve the `"PM: scan → "` form. C-42 passes (multi-phase second-person + C-27 precondition met). C-41/C-43/C-44 still fail — C-42 is independent of ceremony.

**V-04** — `[STATUS-QUO-SNAPSHOT]` is a first-class block in Phase 2, required before `[IG-REGISTER]`. Adds C-36 (Condition 1 extended to snapshot), C-37 (structural fail rule co-located), C-45 (dual-form fail rule: negative + positive), C-46 (scope qualifier: "absent from this phase block"). Phase 1.5 cluster remains N/A (C-38/C-39/C-40/C-47). `[STRATEGY-SCOPE-SEAL]` INVALID IF references the C-37 structural rule by name (C-40).

**V-05** — Full five-cluster extension. Phase 1.5 (STRATEGY INERTIA SCOPING) inserts between Phase 1 and Phase 2, emitting `[STRATEGY-SCOPE-SEAL]`. ENTER/EXIT ceremony at all five numbered phases with chained notation. Phase 2 ENTER absorbs both `[PM-CONTRACT-SEAL]` (Phase 1 EXIT) and `[STRATEGY-SCOPE-SEAL]` (Phase 1.5 EXIT). ROLE markers at every numbered phase entry. Second-person framing throughout. STATUS-QUO-SNAPSHOT active with C-36/C-37/C-45/C-46. Targets 175/175.

## Key structural invariants maintained across all five variations

- Five numbered phases (0–4) in prescribed order — C-01
- `[SCOUT-STATUS-TABLE]` 7 rows in Phase 0 — C-02
- `[PM-COVERAGE-TABLE]` with Waiver Status column — C-03
- `[IG-REGISTER]` + `[ID-REGISTER]` with ≥2 IG-ID rows — C-04
- Five guided sections in Phase 3 in order — C-05
- All fallback branches A/B-1/B-2/B-3/B-catch with VERBATIM RESPONSE blocks — C-06/C-07
- Three gate tokens defined with INVALID IF rules — C-08
