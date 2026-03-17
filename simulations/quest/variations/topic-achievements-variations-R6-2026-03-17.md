Written to `simulations/quest/golden/topic-achievements-variate-R6-2026-03-17.md`.

---

## Variate R6 — topic-achievements

**Basis**: R5 V-05 was golden under v5 (C-01–C-19). v6 adds C-20 (each gate declares a specific inspectable output schema) and C-21 (all phases uniformly gated — no steps anywhere). R5 V-05 meets both at baseline but with varying schema precision and no explicit failure surfaces. R6 isolates three new dimensions.

---

### Variation axes selected

| Axis | Targets | Used in |
|------|---------|---------|
| **Lifecycle emphasis** — schema preface (gate schema declared BEFORE phase instructions, as goal state) | C-20 | V-01, V-04, V-05 |
| **Output format** — gate registry table (all 4 schemas declared upfront in a single pre-printed table before Phase 1) | C-20, C-21 | V-02, V-04, V-05 |
| **Phrasing register** — fail-surface closure (each gate adds explicit FAIL conditions alongside PASS format) | C-20 | V-03, V-04, V-05 |

---

### Variation summary

**V-01 — Schema Preface** (lifecycle emphasis alone)
Each phase section opens with its gate schema as a named block — *before* the phase instructions. The model reads what it must produce before it starts working. Tests whether goal-state-first placement produces more reliable C-20 compliance than R5's terminal-schema placement. C-21 met by uniform 4-phase gate architecture.

**V-02 — Gate Registry Table** (output format alone)
A pre-printed registry table at the prompt preamble lists all 4 gates and their PASS schemas before Phase 1 begins. C-21 structural visibility is established at the first line of the prompt. C-20 schemas are discoverable without scanning through phases. Per-phase gate instructions reference the registry.

**V-03 — Fail-Surface Closure** (phrasing register alone)
Every gate adds an explicit `FAIL:` block listing specific output shapes that do NOT clear the gate ("summary count without category lines does not clear CLASSIFY GATE"). Tests whether two-sided contracts produce stronger C-20 compliance than PASS-only schemas. The schema becomes verifiable in both directions.

**V-04 — Combination: Registry + FAIL conditions**
Registry gives upfront C-21 architectural visibility. Per-phase FAIL conditions close the failure surfaces positive-only schemas leave open. C-20 now satisfied by two simultaneous mechanisms: registry declares structure, FAIL block declares what breaks the schema.

**V-05 — Golden Synthesis: Registry + Schema Preface + FAIL conditions + all R5 V-05 wins**
Three layers simultaneously: (1) registry — all schemas visible before Phase 1; (2) schema preface — each phase opens with goal state before instructions; (3) FAIL conditions — defensive closure per gate. All R5 V-05 baseline (session invariants A-D, pre-printed Falsified row, pre-printed LOCKED cell text, pre-printed table skeleton, CLASSIFY before STATE, uniform 4-phase gate architecture) preserved unchanged.
