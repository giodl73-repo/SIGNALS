The file is written. Here's the summary of what R8 produces:

---

**`simulations/quest/golden/flow-dataflow-variate-R8-2026-03-15.md`** — 5 complete variations

---

### R8 Hypothesis Space

Three single-axis + two combined, all targeting C-21/C-22/C-23:

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| **V-01** | Decomposed latency columns | Separating Transport and Processing Overhead into independent numeric columns forces the model to reason about each sub-component distinctly, surfacing asymmetric values (queue-backed vs sync API) |
| **V-02** | Cumulative SLA% running total | Per-boundary % misses multi-moderate-boundary pipelines; a cumulative column identifies the precise tipping boundary, which may differ from the highest single % |
| **V-03** | Structurally separate closure gate | A closure gate table generated from the declared NH/LP set cannot self-confirm from the recovery table rows — tests whether it detects omissions rather than mirrors what's present |
| **V-04** | H1 + H2 combined | Tests whether decomposed latency + cumulative % reinforce each other for C-06 stale window precision, and whether a 8-column boundary table completes without column collapse |
| **V-05** | H2 + H3 combined | Tests whether cumulative SLA% computation (cognitive load in §3) trades off against closure gate completeness (§6) — the primary cross-mechanism failure mode to probe |

### Scenarios chosen

| Variation | Domain | Pipeline |
|-----------|--------|----------|
| V-01 | Operations/Commerce | Order fulfillment (6 stages) |
| V-02 | Finance | GL consolidation (6 stages) |
| V-03 | Operations | Inventory sync / dual-write (parallel stages 3a/3b) |
| V-04 | Finance | AR aging / DSO reporting (6 stages) |
| V-05 | Operations/Finance | Procurement-to-pay / P2P (6 stages) |

V-03 introduces a parallel-path topology (dual-write dispatcher splits into OMS + Catalog write paths) as a new structural test — the closure gate must enumerate LP identifiers from two parallel stages rather than a linear chain.
