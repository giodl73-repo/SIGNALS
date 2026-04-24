File written. Here's the R17 summary:

---

## R17 Variate Summary — campaign-evidence

**File:** `simulations/quest/golden/campaign-evidence-variate-R17-2026-03-17.md`

**What changed from R16:** All five variations now carry V-05's named-table physical separation (C-37/C-38) as the baseline. The R17 challenge is combining that with the two new criteria.

### Variation axes

| Variation | Axis | Rules | Checksum | C-41 | C-42 |
|-----------|------|-------|----------|------|------|
| V-01 | Output format: multi-column rule-named interrogative headers | 5 (SEQUENCING single) | 40 | **Target** | — |
| V-02 | Lifecycle emphasis: SEQUENCING decomposed, generic headers | 6 (HYPO+ORDER) | 47 | — | **Target** |
| V-03 | Phrasing register: conversational rule-named headers | 5 (SEQUENCING single) | 40 | **Boundary test** | — |
| V-04 | Combined: role reversal + C-41 + C-42 | 6 (HYPO+ORDER) | 47 | ✓ | ✓ |
| V-05 | Combined: inertia framing + C-41 + C-42 | 6 (HYPO+ORDER) | 47 | ✓ | ✓ |

### Key structural decisions

**C-41 implementation (V-01, V-03, V-04, V-05):** Each applicable rule gets its own column with a rule-named header — "Will ATTRIBUTION hold? [Stage N of 5]" — rather than a rule-as-row with a generic "Will this rule hold?" column. The column header makes each checkpoint table self-describing when detached from context.

**C-42 implementation (V-02, V-04, V-05):** SEQUENCING-HYPO governs hypothesis placement; SEQUENCING-ORDER governs evidence-stage relative ordering. Independent coverage-map rows, independent invocation trails. Checksum shift from 40→47 is automatic (7 new artifacts: 2 positive × 2 phases + 3 negative).

**V-03 boundary test:** Conversational phrasing ("Will every ATTRIBUTION claim be labeled with its source stage?") still names ATTRIBUTION explicitly. Tests whether C-41 requires exact "Will X hold?" form or just rule identity in the header.

**V-04 live demonstration:** Intel-first ordering declared at S1's SEQUENCING-ORDER PRE invocation — the rule governs a real reversal, not just the default convention.

**V-05 antipattern taxonomy:** Named excluded antipatterns in every rule declaration (hypothesis-first mode, unordered collection, uniform confidence, attribution collapse, unconstrained synthesis, unfalsifiable hypothesis) plus an antipattern-absence confirmation section in ARTIFACT-S5.
