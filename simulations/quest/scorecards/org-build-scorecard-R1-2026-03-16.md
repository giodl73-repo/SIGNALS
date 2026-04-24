```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["phase-gate with cross-artifact coherence: IA scope field references FLAT-CASE-PRESSURE rating via 3 pre-written templates, ensuring assessment shapes role design", "anti-pattern derivation from design choice: flat org produces cat-3/cat-2, deep hierarchy produces cat-1/cat-4 — aspirational artifact tied to structural decision", "single-verdict guard: 'Only one verdict. Both is an error.' prevents double-verdict failure more reliably than permissive phrasing"]}
```

---

**Key findings:**

All 5 variations are golden (all essential pass, composite >= 80). The rubric is well-calibrated for this skill — every variation covers all 10 criteria.

**Differentiation at the margin:**
- V-03 lost a half-point on C-10: "Format for..." is weaker than "MUST start with"
- V-04 lost a half-point on C-07: inline comma-separated charter fields increase omission risk vs. structured templates

**V-05 wins the qualitative tier** at 100 for a different reason than V-01 and V-02: it is the only variation where artifacts are *derived from* earlier artifacts (IA scope references the flat-case rating; anti-pattern categories reference the design depth). That cross-artifact coherence is what the combination hypothesis tested, and the prompt structure delivers it.

Scorecard saved to `simulations/quest/scorecards/org-build-scorecard-R1-2026-03-16.md`.
listed

### V-02 — Output Format (Template-First)
- C-01: Section 1.1 provides fill-in box-and-line template with 3-level example
- C-02: Role file template with multi-line YAML for all 5 fields
- C-07: Section 1.5 requires Quorum as N of M with example "3 of 5"
- C-08: Template includes FLAT-CASE-PRESSURE block + "Only one verdict. Both is an error."
- C-09: Table template has Type column; "Row 1 and Row 2 must have different Type values"
- C-10: "`Why It Applies Here` MUST start with `[element name] (cat-N) —`" (capitalized MUST)

### V-03 — Inertia Framing (Flat as Named Competitor)
- C-08: Phase 1 entirely devoted to flat-case assessment; richest C-08 framing of all 5
- C-10: PARTIAL — "Format for 'Why It Applies Here'" is descriptive not imperative ("MUST"). Model may treat as suggestion rather than requirement.

### V-04 — Phrasing Register (Conversational Imperative)
- C-01: "Don't use a flat list — use actual boxes connected by lines" is the most explicit anti-failure guard
- C-07: PARTIAL — all charter fields listed inline as comma-separated sentence. Terse presentation increases risk of abbreviated charter text rather than structured per-meeting charter.
- C-08: Format block explicitly shows closed-set scale and verdict syntax

### V-05 — Combination (Lifecycle + Inertia + Sequence)
- C-01: Structure depth derived from Phase B rating (HIGH=shallow, LOW=deeper) — unique integration
- C-03: IA scope field must reference FLAT-CASE-PRESSURE rating with 3 template mappings
- C-08: Phase B entirely devoted to assessment: B1 flat argument, B2 structure argument, B3 rating+verdict, B4 IA gate
- C-10: Anti-pattern category tied to design choice: "if flat org -> cat-3/cat-2; if deep hierarchy -> cat-1/cat-4"

## Summary

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 | 5/5 | 3/3 | 2/2 | 100 | YES |
| V-02 | 5/5 | 3/3 | 2/2 | 100 | YES |
| V-03 | 5/5 | 3/3 | 1.5/2 | 97.5 | YES |
| V-04 | 5/5 | 2.5/3 | 2/2 | 95 | YES |
| V-05 | 5/5 | 3/3 | 2/2 | 100 | YES |

Ranking: V-01 = V-02 = V-05 (100) > V-03 (97.5) > V-04 (95)

## Excellence Signals

**1. Phase-gate with cross-artifact coherence** (V-05)
IA gate in Phase B forces inertia-advocate scope field to reference the FLAT-CASE-PRESSURE rating
with three pre-written scope templates (HIGH/MEDIUM/LOW). Assessment shapes the role, not the
reverse. Ensures coherence across artifacts.

**2. Anti-pattern derivation from design choice** (V-05)
Ties anti-pattern category selection to the structure designed: flat org produces cat-3/cat-2;
deep hierarchy produces cat-1/cat-4. Only variation where an aspirational artifact is derived
from a design decision rather than generated independently.

**3. Single-verdict guard** (V-02)
"Only one verdict. Both is an error." Explicit error framing (not just "choose one") is more
reliably followed. Prevents double-verdict C-08 failure mode.
