Written to `simulations/quest/golden/trace-component-variate-R5-2026-03-15.md`.

---

**R5 variation map summary:**

| Variation | Axis | Key targets | Expected ceiling |
|-----------|------|-------------|-----------------|
| V-01 | Role sequence | C-16 (PASS-THROUGH column), C-17 (active correction), C-08 (§8 Optimizations), C-11 (§4/§5/§6 upstream citations) | 138–140/140 |
| V-02 | Output format | C-14/C-16 (prepended vocab block), C-12 (token rows), C-11 (citation column), C-08 (TABLE-06), C-15/C-17 (stamp) | ~115–125/140 |
| V-03 | Lifecycle emphasis | C-08 (Phase 7 = Optimization), C-11 (registry-consume openings), C-12 (phase-level tokens) | ~100–115/140 |
| V-04 | Phrasing register | C-08 ("Name at least one…"), C-11 ("cite §N row"), C-12 (token mandate) | ~90–110/140 |
| V-05 | Combined: role seq + lifecycle | All 17 criteria via three-role pipeline | 138–140/140 |

**Design notes:**

- **V-01** is the targeted minimal fix to R4 V-01 — same blocking-gate structure, three surgical additions: PASS-THROUGH column in §0, §8 Optimizations table, and citation requirements in §4/§5/§6. C-11 goes from partial to full because three downstream sections now each have explicit upstream citation columns.

- **V-02** is the format-contract rehabilitation — R4 V-02's 83/130 came from format-only enforcement. The prepended vocabulary block gives C-14/C-16; token rows in every table give C-12; the "Derived From / Upstream Ref" column across §4–§7 tables gives C-11. C-13 is rated partial because table schemas cannot prevent framework jargon in cell values the way a blocking role can.

- **V-03** isolates the lifecycle axis against the new criteria — C-08 gets a dedicated Phase 7 that cannot be skipped; C-11 is enforced through the registry-consume headers (each phase must name the specific identifiers imported, making any broken chain structurally visible). Without vocabulary contract, C-13/C-14/C-16/C-17 are unaddressed — this is the controlled single-axis test.

- **V-04** tests whether the phrasing register alone (imperative, per-criterion checklist) can close the C-08/C-11 gaps without role machinery. STEP 9 explicitly mandates the optimization; every state/render instruction includes a "cite §N row" requirement. C-14/C-16/C-17 likely fail — those criteria require named pre-trace artifacts, not just correct behavior.

- **V-05** is the ceiling-targeting combined variation: Role 1's vocabulary contract gives C-14/C-16; Role 2's 7 phase-gated sections with registry-consume protocol give C-08/C-11/C-12, all bound to the vocabulary contract for C-13; Role 3's active stamp gives C-15/C-17 plus explicit vocabulary leak and evidence-chain audits. The combined mechanism creates three independent enforcement layers that together address all 17 criteria.
