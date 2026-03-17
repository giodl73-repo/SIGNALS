**v14 written** — two new criteria, two gaps closed.

---

**What changed:**

**C-38** — *Role prohibitions appear as inline execution markers co-located at the specific phase where each role's constraint applies* (V-04 R14 excellence signal):

- **Gap it closes**: C-23 requires role prohibitions to *exist* but permits them anywhere — a container-level table at container entry satisfies C-23. V-04 demonstrated that placing each prohibition inline at the phase header ("Phase N — ROLE (writes: X; must NOT write: Y)") positions the enforcement at the exact moment contamination could occur, which is finer granularity. C-38 fails for any document that satisfies C-23 only via container-level tables.
- **Prerequisite**: C-23
- **Weight**: 7 pts

**C-39** — *Role prohibitions and phase gate markers use hard enforcement modal operators (MUST, FORBIDDEN, REQUIRED, PROHIBITED) throughout* (V-01 R14 excellence signal):

- **Gap it closes**: C-23 is satisfied by "Must NOT Write" and "should not write" equally — it has no register requirement. V-01 demonstrated that converting every prohibition and gate marker to hard modal operators produces the "strongest prohibition expression of any variation." C-39 fails if any prohibition or gate marker uses soft or mixed language, even if most use hard operators.
- **Prerequisite**: C-23
- **Weight**: 5 pts

**Updated point totals**: Aspirational 167 → 179. Total 267 → **279**.

**C-38 and C-39 are orthogonal** — independently satisfiable and independently violatable:

| | C-38 (position) | ¬C-38 (container-level only) |
|---|---|---|
| **C-39 (hard register)** | V-01+V-04 combined — maximum expression | V-01 alone — imperative table |
| **¬C-39 (mixed register)** | V-04 alone — phase-level, soft language | V-02/V-03/base — table, mixed |

**R14 seed scores 267/279** under v14. R15 seed: combine V-04's phase-level declarations with V-01's imperative register on the R14 base, expected 279.
