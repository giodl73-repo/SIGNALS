`trace-contract-rubric-v9-2026-03-15.md` written.

**What changed:**

**Formula:** `A/24 × 10` → `A/27 × 10`. Per-criterion weight ~0.417 → ~0.370. Ceiling unchanged.

**Three new aspirational criteria from R8 scorecard:**

| ID | Name | Source | Key distinction |
|----|------|---------|-----------------|
| C-33 | Both GATE 1 contamination paths use symmetric two-clause confirmable form | V-05 R8 | C-14 tests actual-output path confirmable form; C-31 tests inertia path confirmable form; C-33 tests both paths use equivalent structural form simultaneously — neither may be weaker than the other. Cannot be satisfied without first satisfying C-14 and C-31. |
| C-34 | Role separation explicitly declared as structurally enforced and not operationally optional | V-05 R8 | C-32 tests distinct role names are assigned; C-34 tests the template explicitly prohibits single-agent substitution with the "not operationally optional" declaration. Converts role assignment from descriptive to prescriptive. |
| C-35 | Inertia-spec-drift amendments grouped as a coherent remediation batch in CONTRACT DELTA | V-05 R8 | C-22 tests priority annotations; C-28 tests amendment type; C-35 tests a third orthogonal grouping axis — remediation origin (inertia-drift vs. independent schema gap) — making inertia-remediation work distinguishable from other P1 amendments at the same amendment type. |

**Distinction ladder gains three new rungs:**
- `C-14 + C-31 → C-33`: each path confirmable independently → both paths symmetric simultaneously
- `C-32 → C-34`: distinct roles assigned → single-agent substitution explicitly prohibited
- `C-10 → C-18 → C-22 → C-28 → C-35`: delta chain gains a third per-entry axis (remediation batch by inertia-drift origin)
