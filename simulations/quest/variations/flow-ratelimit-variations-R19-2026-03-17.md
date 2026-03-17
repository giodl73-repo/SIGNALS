`simulations/quest/golden/flow-ratelimit-variate-R19-2026-03-17.md` written.

---

## flow-ratelimit — Variate R19 Summary

**Target criteria:** C-43, C-44, C-45

**Variation axes:**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| C-43 (cell anchor) | seed: CELL ANCHOR + UNRESOLVED REFERENCE classes in Format Contract + CHECK (e) e.1–e.3 | none | none | combined with C-44 | three-plane e.5–e.6 |
| C-44 (registry) | none | seed: Schema Production Registry at Format Contract head, REGISTRY GAP rule, CHECK (e) e.1–e.3 | none | combined with C-43 | three-plane Plane 1 e.1–e.3 |
| C-45 (BURST PATH TABLE) | none | none | seed: Role 3 produces BURST PATH TABLE, BASELINE routes through it, bidirectionality required + CHECK (e) e.1–e.4 | none | three-plane Plane 2 e.4 |

**What each variation introduces:**

- **V-01** — Single-axis C-43. Format Contract SCHEMA-A gains the CELL ANCHOR requirement and the two explicit violation classes (CELL ANCHOR = missing prefix, scan-time; UNRESOLVED REFERENCE = invalid prefix, cross-ref). Role 9 CHECK (e) audits both classes in one pass.

- **V-02** — Single-axis C-44. Format Contract opens with a Schema Production Registry table (schema → role → type → gate). REGISTRY GAP is detectable by row count comparison alone. CHECK (e) audits three registry planes: row count, gate fill, orphaned schemas.

- **V-03** — Single-axis C-45. Role 3 expands to produce a BURST PATH TABLE with ENDPOINT NAME and SCHEMA-A BASELINE SOURCE columns. The Format Contract BASELINE definition routes through this table rather than independently citing a Finding ID. CHECK (e) audits forward (definition → table column) and backward (column named for schema) traceability.

- **V-04** — C-43 + C-44 combined. Registry at Format Contract head plus cell anchor requirement on SCHEMA-A. Role 9 CHECK (e) runs two planes: Plane 1 (registry completeness, e.1–e.3), Plane 2 (cell anchor + violation-class distinction, e.4–e.6).

- **V-05** — Full integration. Registry + BURST PATH TABLE + cell anchor all active. Format Contract BASELINE definition names the BURST PATH TABLE and SCHEMA-A BASELINE SOURCE column; cell-level BP-xx prefixes resolve to BURST PATH TABLE rows. Role 9 CHECK (e) is a three-plane audit: Plane 1 (registry, e.1–e.3), Plane 2 (BURST PATH TABLE bidirectionality, e.4), Plane 3 (cell anchor + UNRESOLVED REFERENCE distinction, e.5–e.6).
