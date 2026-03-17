**5 complete variations written** to `simulations/quest/rubrics/prove-prototype-rubric-v5-variate-R5-2026-03-15.md`.

---

## Round 5 Variations — prove-prototype (v5 rubric)

**Test variable**: C-20 (model-written gate completion artifact) and C-21 (trailing section gate coverage). All 5 variations target full C-19/C-20/C-21 compliance — closing the gap that caused V-01, V-03, V-05 in Round 4 to score partial on C-19.

| Var | Axis | C-20 mechanism | Key structural difference |
|-----|------|----------------|--------------------------|
| **V-01** | Single — Role Sequence | Role-attributed completion lines (`PHASE N COMPLETE — DEFINER: ...`) | 3 roles (DEFINER/EXPERIMENTER/EVALUATOR); each phase's completion is owned by a named role |
| **V-02** | Single — Output Format | Completion as trailing table row (`[SECTION N COMPLETE — ...]`) | Gate and completion live as structural rows inside each section table; same row-scan mechanism as C-11 |
| **V-03** | Single — Phrasing Register | "Establishment record" phrasing (`Establishment record — Phase N: ...`) | Formal/structural register throughout; "The following must be established..." rather than imperative |
| **V-04** | Combined — Lifecycle + Inertia | Completion lines carry B-00 values (`B-00 = [value]` named in Phase 1, 3, 5, 7) | Three lifecycle containers (DEFINE/RUN/EVALUATE) + B-00 baseline declared in Phase 1 and frozen |
| **V-05** | Combined — Role Sequence + Format | Bold role-attributed completion (`**PHASE N COMPLETE — ANALYST: ...**`) | 2 roles (DESIGNER/ANALYST) + labeled-pair blocks; tests whether 2-role split achieves adjudication isolation |

**C-21 fix vs Round 4**: Every variation explicitly gates phases 8 and 9 inline — no variation scopes its gate scheme to "phases 1–7." V-02 uses gate rows in the sections 8–9 tables; V-03 uses "may not be produced until Phase N establishment record is present"; V-04 uses execute-after with lifecycle container framing; V-01 and V-05 use explicit EVALUATOR/ANALYST execute-after markers.

**Design probes**:
- V-02 tests whether table-row gates produce the same C-20 audit path as standalone bold/italic completion lines
- V-03 tests whether formal "establishment record" phrasing is a structurally valid C-20 completion artifact
- V-04's completion lines are information-rich (they name B-00 values) — tests whether richer completion lines raise a new ceiling criterion
- V-05 probes whether a 2-role architecture (vs. V-01's 3-role) satisfies adjudication isolation without the DEFINER/EXPERIMENTER split
