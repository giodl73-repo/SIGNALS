Written to `simulations/quest/rubrics/flow-ratelimit-rubric-v1-2026-03-17.md`.

---

**Rubric summary — flow-ratelimit v1**

**Essential (5 criteria, 60 pts)**
| ID | Criterion |
|----|-----------|
| C-01 | First-limit ordering — which limit binds first and why |
| C-02 | Backpressure propagation chain — causal, not just a list |
| C-03 | User experience at each throttle tier (min 2 tiers) |
| C-04 | Unprotected burst path — structurally missing, not just high-tier |
| C-05 | Retry-After handling gap check — explicit flag with failure mode |

**Recommended (3 criteria, 30 pts)**
| ID | Criterion |
|----|-----------|
| C-06 | Cascading throttle failure — second throttle triggered *by* first |
| C-07 | Numeric rate limit specificity — at least one concrete threshold |
| C-08 | Volume-to-behavior mapping — structured, not prose paragraphs |

**Aspirational (2 criteria, 10 pts)**
| ID | Criterion |
|----|-----------|
| C-09 | Per-bottleneck mitigation — specific action/setting, not generic advice |
| C-10 | Quantified impact at load spike — arithmetic grounded in C-07 limits |

**Key design decisions:**
- C-05 (Retry-After) is Essential, not Recommended — it's explicitly called out in the skill description as a required identification target
- C-01 is distinct from C-07: ordering reasoning can pass without a number; both are needed for Silver
- Cascading (C-06) is Recommended rather than Essential — a useful analysis can still identify the first bottleneck without constructing a full cascade scenario
