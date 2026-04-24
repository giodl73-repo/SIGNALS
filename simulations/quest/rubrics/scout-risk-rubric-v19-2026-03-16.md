All changes verified. Here's the complete rubric written to `scout-risk-rubric-v19-2026-03-17.md`.

---

## v18 -> v19: Two new criteria from R19

### C-56 — Violation taxonomy block explicitly enumerates prohibition sites by name rather than stating a count (escalates C-49)

**Source**: V-03 pattern — Phase 0c changes "Five prohibition sites" to "(1) [site name], (2) [site name]...". Count-based coverage requires a global prompt scan to verify; enumeration-based coverage is verifiable by set membership. Adding a prohibition site without updating the taxonomy's named list is a detectable mismatch with enumeration; with a count it could stay numerically accurate while covering wrong sites.

### C-57 — Closure sentence ordering rule is declared at global scope, naming all closure instances (escalates C-54)

**Source**: V-05 pattern — ordering rule scoped as "applies to Phase 0 and Phase 0c closures" rather than embedded per-block. Per-block rules must be replicated; a new closure block can omit canonical order silently. A global rule with named scope is a single-point-of-truth: any unlisted closure block is a detectable coverage gap, and the rule is auditable from one location.

---

## Scoring delta

| Metric | v18 | v19 |
|--------|-----|-----|
| Aspirational criteria | 47 | 49 |
| Aspirational max | 94 | 98 |
| Max composite | 184 | 188 |
| Golden band | 178-184 | 182-188 |
| Strong band | 163-177 | 167-181 |
