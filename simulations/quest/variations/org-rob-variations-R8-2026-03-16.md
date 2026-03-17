Written to `simulations/quest/golden/corps-rob-variate-R8-2026-03-16.md`.

---

# Variate R8 -- org-rob

5 variations targeting C-21, C-22, C-23 on the R7 114/114 base.

## Variation Axes

| Variation | Axis | C-21 | C-22 | C-23 |
|-----------|------|------|------|------|
| V-01 | Inertia Anchor | ++ | o | o |
| V-02 | Extensible Violation Taxonomy | o | ++ | o |
| V-03 | Self-Documenting Violation Rationale | o | o | ++ |
| V-04 | Inertia Anchor + Extensible Taxonomy | ++ | ++ | o |
| V-05 | Full v7 Stack | ++ | ++ | ++ |

## Key structural decisions per variation

**V-01 (C-21)**: Adds a named `INERTIA BASELINE (IB-01)` block before Stage 1. Propagates IB-01 to three structural positions: `Inertia Impact` column in the finding ledger, `Inertia Link` in risk register entries, and `Inertia Pressure Summary` in synthesis. VIOLATION-08 taxonomy unchanged; no consequence paragraphs.

**V-02 (C-22)**: Extends the violation taxonomy to `VIOLATION-09` (synthesis section completeness rule) and adds an explicit extensibility statement: *"Future additions continue from VIOLATION-10+."* No inertia baseline. No consequence paragraphs. VIOLATION-09 targets a genuine new structural rule -- synthesis omitting any of its three required subsections -- making the extension non-trivial.

**V-03 (C-23)**: Keeps VIOLATION-01..08 closed but adds consequence paragraphs to VIOLATION-01 through VIOLATION-05 (5 total, exceeding the minimum 3). Each paragraph explains the downstream capability that breaks when the violation occurs, distinct from restating the rule. No inertia baseline. No VIOLATION-09+.

**V-04 (C-21 + C-22)**: Combines inertia propagation with VIOLATION-09 defined as the *inertia baseline absence violation* -- making inertia self-enforcing through the taxonomy. VIOLATION-09 states: "a review that raises displacement concerns without a named INERTIA BASELINE element before Stage 1." No consequence paragraphs.

**V-05 (C-21 + C-22 + C-23)**: Full convergence candidate. All three new criteria plus the complete R7 base. Consequence paragraphs on VIOLATION-01..05 (including VIOLATION-04 for the inertia link field, which ties C-21 and C-23 together). VIOLATION-09 as the inertia enforcement rule signals C-22 extensibility. Target: 120/120 under v7.
