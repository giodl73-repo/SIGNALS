Written to `simulations/quest/golden/org-review-variate-R17-2026-03-16.md`.

---

# org-review -- Variate Round 17 (v11 rubric Round 5)

**5 variations targeting C-33 + C-34 + C-35 via fresh structural mechanisms.**

## Design target

Prior rounds R12-R16 tried: manifest applicability column, pre-review gap-check narrative, NH dimension table inside BRACKET OPENING. Round 17 diagnoses three failure modes and applies structural fixes:

| Criterion | R16 failure mode | R17 fix |
|-----------|-----------------|---------|
| **C-33** | Applicability column filled without per-artifact justification; generic capability rating | §17a APPLICABILITY CERTIFICATION BLOCK: one entry per role, must name specific artifact domain + specific `lens.verify` entry. Generic = invalid, downgrade to LOW. |
| **C-34** | Gap-check prose-structured; domain coverage requires reading narrative to verify | §17 DOMAIN-ROLE COVERAGE MATRIX: rows × columns table, gaps visible by inspection (no HIGH cell in row = DOMAIN-GAP). |
| **C-35** | NH dimension table present but g_null derived narratively; C-35 requires table-only derivation | §18 CHALLENGER PRE-ASSESSMENT: standalone section with VERDICT column per dimension; g_null = F>O→PASS, F=O→CONDITIONAL, F<O→FAIL. Zero prose required. |

## Variation axes

| Variation | Axis | Mechanism | Criteria targeted |
|-----------|------|-----------|------------------|
| **V-01** | Phrasing register | §17a APPLICABILITY CERTIFICATION STEP added after ROLE MANIFEST | C-33 |
| **V-02** | Output format | §17 DOMAIN-ROLE COVERAGE MATRIX (rows=domains, columns=roles, cells=applicability) | C-33 + C-34 |
| **V-03** | Role sequence | §17 CHALLENGER PRE-ASSESSMENT extracted as standalone section before BRACKET OPENING; VERDICT column + formula | C-35 |
| **V-04** | Register + Format | V-01 (§17a certification) + V-02 (§17 matrix) combined; §7 updated with 1.5a + 1.5b slots | C-33 + C-34 |
| **V-05** | Register + Format + Sequence | V-04 + V-03 (§18 PRE-ASSESSMENT) + §19 post-render CRITERION CHECK; 225/225 target | C-33 + C-34 + C-35 |

## Key structural difference from R16

R16 V-05 uses §17 (manifest applicability) + §18 (gap-check) + §19 (NH table inside BRACKET OPENING). R17 V-05 uses §17 (coverage matrix — 2D structure) + §17a (certification — justification layer) + §18 (PRE-ASSESSMENT — extracted from BRACKET OPENING). The PRE-ASSESSMENT is the decisive change for C-35: g_null(initial) in §9 Stage 1 now **comes from** the PRE-ASSESSMENT formula result, not from GOpen. BRACKET OPENING **inherits** g_null(initial) rather than producing it. A conflict between GOpen and g_null(initial) must be named and resolved explicitly.
