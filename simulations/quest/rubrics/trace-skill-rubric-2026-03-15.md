Here is the generated rubric:

---

**trace-skill Rubric v1** -- `simulations/quest/rubrics/trace-skill-rubric-v1-2026-03-15.md`

**5 Essential** (all must pass, 60 pts total):
| ID | Criterion | Category |
|----|-----------|----------|
| C-01 | Four phases present in sequence: Gather, Bind, Execute, Verdict | format |
| C-02 | Gather enumerates all inputs by name with source | correctness |
| C-03 | Bind maps every Gather input to a single resolved value | correctness |
| C-04 | Execute produces target skill artifact with correct naming and sections | behavior |
| C-05 | Verdict declares explicit PASS/FAIL with rationale | correctness |

**3 Recommended** (30 pts total):
| ID | Criterion | Category |
|----|-----------|----------|
| C-06 | Phases carry exact schema labels (Gather/Bind/Execute/Verdict) | format |
| C-07 | Verdict cites criterion IDs, not free-form prose | depth |
| C-08 | Artifact complete -- no elision markers anywhere | correctness |

**2 Aspirational** (10 pts total):
| ID | Criterion | Category |
|----|-----------|----------|
| C-09 | Gather includes Coverage Matrix with closed-world preamble | coverage |
| C-10 | Execute relays carry (role, signal, binding, status) evidence fields; Verdict reads, not reconstructs | depth |

**Scoring**: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)`
**Golden threshold**: all 5 essential PASS + composite >= 80

---

Note: The old v1 used Setup/Execute/Findings/Amend phase names from an earlier design iteration. This replaces it with the current Gather/Bind/Execute/Verdict lifecycle that the evolved rubric (v8+) confirmed as stable.
