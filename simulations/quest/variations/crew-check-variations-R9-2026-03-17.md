`crew-check-variate-R9-2026-03-17.md` written to `simulations/quest/golden/`.

---

## crew-check — Variate R9

**Base**: R8 V-05 (128/128 under v7). All 5 variations carry the full R8 V-05 contracts (C-24, C-25, C-26, C-27, IC-CHALLENGED) and extend them.

**New criteria targeted (v8 rubric)**:

| ID | Name | PASS condition |
|----|------|---------------|
| C-28 | SOLO disposition protocol | Gate 9 emits SOLO FINDINGS table; each entry carries ESCALATE / DISMISS:rationale / ROLE-SPECIFIC tag |
| C-29 | Mid-run convergence snapshot gate | Gate 5.5 emits tier counts; early-abort HALT [G5.5] if CONFIRMED=0 AND CORROBORATED=0; `--amend waive:convergence` for bypass |
| C-30 | Stage-aware RUN HEALTH | Stage field + SCOPE DISTRIBUTION table (YES / ADVISORY / NO / DEPRECATED counts) in BOTH clean and failed variants |

**Variation map**:

| Variation | Axis | Hypothesis summary |
|-----------|------|--------------------|
| V-01 | C-28 only | SOLO findings have a mandatory exit path at Gate 9 rather than silent synthesis absorption |
| V-02 | C-29 only | Gate 5.5 becomes a genuine mid-run checkpoint with counts and early-abort, not an accumulation step |
| V-03 | C-30 only | RUN HEALTH is a standalone diagnostic artifact in both clean and failed variants; NO vs DEPRECATED distinguished |
| V-04 | C-28 + C-29 | Snapshot detects SOLO-only runs; disposition contract handles every SOLO finding when waive path is taken |
| V-05 | C-28 + C-29 + C-30 | Three independent enforcement axes (Gate 9, Gate 5.5, RUN HEALTH) compose without contract conflict |

**Structural key decisions**:

- **C-29 waive path** (`--amend waive:convergence`) deliberately activates C-28 mandatory disposition — a run with zero convergence that proceeds anyway must explicitly explain every non-converging signal. The two criteria are co-reinforcing under the waive path.
- **C-30 failed variant** carries Stage + SCOPE DISTRIBUTION because failures happen most often mid-execution when scope is already partially resolved; omitting these from the failed cert forces transcript re-reading.
- **G5.5 placement** is after Gate 4.5 (CHALLENGE RESPONSE MAP) and Gate 5 (matrix assembly), before Gate 6 — it reads the fully-assembled YES-scope matrix before synthesis is attempted, not during domain reviews.
