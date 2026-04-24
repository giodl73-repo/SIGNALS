Done. The file is at `simulations/quest/rubrics/draft-spec-rubric-v11-variate-R11-2026-03-15.md`, 1644 lines.

**Structure:**

| Section | Lines | Primary Axis |
|---------|-------|-------------|
| V-01 | 24–310 | C-33 only — Waiver Status column in [PM-COVERAGE-TABLE] on minimal base |
| V-02 | 311–597 | C-35 only — partial-population structural fail rule co-located with AMPLIFIED sub-slots (C-32 base) |
| V-03 | 598–949 | Combined C-33+C-34+C-35 on split-registers base (R10 V-04) |
| V-04 | 950–1228 | C-34 only — named chain closure declaration in [INERTIA-ANALYZED] (C-31 base) |
| V-05 | 1229–1582 | Full combination — all 35 v11 criteria |
| Scoring | 1583–1644 | Pass/fail matrix + isolation confirmation |

**Key structural additions per new criterion:**
- **C-33** (V-01, V-03, V-05): `Waiver Status` column with `COVERED / C-03 WAIVER` enumeration added to `[PM-COVERAGE-TABLE]` template definition
- **C-34** (V-03, V-04, V-05): `**Chain closed**: [PM-COVERAGE-TABLE] waiver -> "R-ID WAIVED" cell -> Condition 2 exemption` named declaration co-located in `[INERTIA-ANALYZED]`
- **C-35** (V-02, V-03, V-05): `**Partial-population structural fail rule**` enforcement statement co-located with AMPLIFIED sub-slot definition in `[IG-REGISTER]`
