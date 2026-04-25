Written to `sim/simulations/quest/golden/program-plan-variate-R3-2026-03-16.md`.

---

## program-plan R3 Variate Prompts (V-01 through V-05)

Rubric: v3 | Criteria targeted: C-13, C-14, C-15 | Max: 130 pts

---

### R2 retrospective under v3

| Variation | C-13 arc-spine | C-14 deletion-resist | C-15 plan YAML error |
|-----------|---------------|---------------------|----------------------|
| R2 V-04 (lifecycle bands) | PASS | PARTIAL (echo only) | PASS (single-stage bad block) |
| R2 V-05 (inertia + template) | PARTIAL | PARTIAL | FAIL |
| Others | PARTIAL | PARTIAL/FAIL | FAIL |

**Gap**: C-14 was partial in all R2 variations (only echo annotated). C-15 in R2 V-04 was minimal (one-stage bad block). The three R3 axes address these precisely.

---

### Variation map

| Variation | Axis | New criterion targeted | Key design decision | Expected C-13/14/15 |
|-----------|------|----------------------|--------------------|--------------------|
| **V-01** | Arc-as-spine | C-13 | 5 arc zones as top-level section headers — strips prose, arc still visible | PASS / PARTIAL / FAIL |
| **V-02** | Full deletion-resistance | C-14 | Every structural slot annotated — `# REQUIRED: ... DO NOT` on name/skills/gate/strategy/echo | PARTIAL / PASS / FAIL |
| **V-03** | Plan-level YAML error block | C-15 | Complete multi-stage wrong plan (4 failure modes, 3 stages, invented skills, bad echo) | PARTIAL / PARTIAL / PASS |
| **V-04** | Arc-spine + deletion-resistance | C-13 + C-14 | Zone headers + per-zone `# REQUIRED` blocks coexist without conflict | PASS / PASS / FAIL |
| **V-05** | Golden synthesis | C-13 + C-14 + C-15 | Wrong plan precedes arc zones; arc IS the document structure; all slots annotated | PASS / PASS / PASS |

---

### Key design decisions per variation

**V-01 (arc-as-spine)**: The five arc zones are markdown section headers (`# ZONE 1: DISCOVERY`, etc.). Strip all prose — headers remain, arc is navigable. Tests whether C-13 is achievable without annotating every slot. Expected C-12 PARTIAL (C-01 still single-anchored — no bad-plan block).

**V-02 (full deletion-resistance)**: Every YAML field has a `# REQUIRED: DO NOT ...` annotation, not just echo. The `program:` key, `strategy:`, `name:`, `skills:`, `gate:` all carry explicit prohibition markers. Tests whether exhaustive annotation satisfies C-14 without making the template unreadable.

**V-03 (plan-level YAML error)**: A complete 4-stage wrong plan with 8 annotated failures — invented skills, execution gates, namespace-label stage names, echo with skills. More comprehensive than R2 V-04's single-stage bad block. Provides the C-01 second anchor needed for C-12 full PASS. C-14 partial (echo annotated in output template but not exhaustively across all slots).

**V-04 (combined arc + deletion-resist)**: Arc zones ARE the prompt sections; each zone section ends with a `# REQUIRED` gate guidance block. The structural hierarchy carries deletion friction at two levels: section headers (arc spine) and per-slot annotations. C-12 partial — no bad-plan block means C-01 is still single-anchored.

**V-05 (golden synthesis)**: Wrong plan opens before any instructions. Arc zones follow. Every slot annotated. The model navigates wrong plan → arc structure → annotated template in sequence. All four essential criteria dual-anchored: wrong plan + template for C-01/C-04, arc echo zone + template annotations for C-02, zone catalogs + template namespace comments for C-03.
