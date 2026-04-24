`campaign-decide-rubric-v16-2026-03-17.md` written.

**Two new criteria added:**

| ID | Pattern | Source | Implies |
|----|---------|--------|---------|
| C-41 | Named-schema enumeration in Phase 5 fill-forward directive | R16 V-01 — `[SCHEMAS: hypothesis-resolution, recommendation-record, because-block — from SCHEMA PREAMBLE]` vs. generic "all" | C-39, C-37, C-35, C-13 |
| C-42 | Per-column temporal commit annotation in bracket notation | R16 V-02 — `(fill-now)` / `(defer-to-Phase-5)` per column in closure directives | C-40, C-38, C-36 |

**Scoring model update:**

| Tier | v15 | v16 |
|------|-----|-----|
| Aspirational denominator | /32 | /34 |
| Aspirational total pts | 16.0 | 17.0 |
| Max composite | 106.0 | 107.0 |

**Interaction chains extended:**

- C-41 closes the C-13 → C-35 → C-37 → C-39 → C-41 chain: prior anchored at Phase 0, into Phase 5 resolution, schema in preamble, fill-forward in section header, each schema individually named in that directive (per-schema verifiability vs. collective "all")
- C-42 extends the C-36 → C-38 → C-40 → C-42 chain: closure exists, columns named, bracket notation, each column annotated with its temporal commit phase (two-pass audit gate: fill-now at Phase N, deferred at Phase 5)

**Design note on C-41 vs C-39:** C-39 requires the directive to be in the Phase 5 section header; C-41 hardens the directive's *content* from a collective reference (`all`) to a per-schema enumeration. The R16 V-01 evidence makes the distinction explicit — `[SCHEMAS: hypothesis-resolution, recommendation-record, because-block]` produces three independently verifiable fill-forward relationships, while "all" is a single binary check.

**Design note on C-42 vs C-40:** C-40 requires bracket notation for the column list; C-42 adds per-column temporal role. The R16 V-02 innovation — `FID (key, fill-now)` / `Actual Outcome (defer-to-Phase-5)` — turns each closure directive into a two-pass audit gate without any additional structural elements.

**C-43 candidate noted** (R16 Excellence Signal 3): Deferred-column annotation at schema *definition* time (encoding fill-now vs. deferred in the SCHEMA PREAMBLE itself, not just at closure directives) — one definition, propagation to all downstream gates automatically.
