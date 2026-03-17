`topic-open-variate-R9-2026-03-17.md` written — 5 complete variations.

---

**Round 9 summary:**

| Variation | Axis | New patterns targeted |
|-----------|------|-----------------------|
| V-01 | Multi-phase exit gates | Phase 1/3/4 gain checklist gates + GATE FAILURE routing (C-35 candidate) |
| V-02 | Extended Phase 5 self-check | C-06/C-07/C-08 added with named AMEND blocks (C-36 candidate) |
| V-03 | Worked example in FIELD SCHEMA | Concrete example row + example COMMIT GATE (C-37 candidate) |
| V-04 | V-01 + V-02 | Multi-phase gates AND extended self-check |
| V-05 | V-01 + V-02 + V-03 | Full integration — all three axes |

**Three prospective criteria for the R9 scorecard:**

- **C-35** (multi-phase gate completeness): Every phase has a formal exit gate checklist and GATE FAILURE routing instruction. Phase 1's GATE FAILURE is terminal (stop + redirect to `/topic-plan` or new slug); Phases 2–4 are return-to-repair.
- **C-36** (self-check covers all 8 criteria): Phase 5 self-check includes C-06, C-07, and C-08 with named `AMEND — {CONDITION NAME}` blocks using the same uniform format as C-01–C-05.
- **C-37** (worked example in schema): FIELD SCHEMA contains a concrete filled-in example row demonstrating all five fields with a valid `{topic}-{signal}-{date}.md` item name; Phase 3 COMMIT GATE template is followed by an example with two essential signals listed by exact item name.

V-01, V-02, V-03 isolate one axis each. V-04 tests whether C-35 and C-36 compose without regression. V-05 tests whether all three compose — the scorer should check whether the Phase 3 example gate conflicts with the Phase 3 exit gate checklist (they sit adjacent; the test is whether the model reads them as complementary or treats one as redundant).
