**trace-skill Rubric v2** -- `simulations/quest/rubrics/trace-skill-rubric-v2-2026-03-15.md`

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
| C-08 | Artifact complete — no elision markers anywhere | correctness |

**5 Aspirational** (10 pts total):
| ID | Criterion | Category |
|----|-----------|----------|
| C-09 | Gather includes Coverage Matrix table with closed-world preamble | coverage |
| C-10 | Execute relays carry (role, signal, binding, status) evidence fields; Verdict reads, not reconstructs | depth |
| C-11 | Gather enumerates spec inputs before invocation inputs — spec anchors the input space before constraints apply | ordering |
| C-12 | Coverage Matrix includes explicit BLOCKED declaration: any Gap=YES halts the trace immediately, no partial runs | coverage |
| C-13 | Execute wraps artifact with delimiter markers (`[ARTIFACT BEGINS HERE]` / `[ARTIFACT ENDS HERE]`) for unambiguous extraction | format |

**Scoring**: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/5 * 10)`  
**Golden threshold**: all 5 essential PASS + composite >= 80

---

*v2 change note: Added C-11 (spec-first enumeration), C-12 (BLOCKED gate), C-13 (artifact delimiter markers) from V-01 excellence signals. Aspirational denominator updated from 2 to 5.*
