Written to `simulations/quest/rubrics/quest-rubric-mock-ns-v18-2026-03-15.md`.

**Summary of v18 changes:**

**Three new criteria (C-48, C-49, C-50), denominator 37 → 39 → 42:**

- **C-48** (depends on C-47) — Named structural heading "Anti-bypass declaration (ABD):" at P-0, making it a label-matchable anchor. Use-site echo row labels update from `(P-0 anti-bypass declaration)` to `(P-0, ABD)` to match the heading name. Gap closed: prior use-site labels pointed to unlabeled prose at P-0; the ABD heading turns the definition point into a findable structural element.

- **C-49** (depends on C-47) — P-0 forward navigation enumeration naming both S-3 and A-1 explicitly. Completes the P-0 → use-site forward arc that pairs with the existing use-site → P-0 back-arc. Combined with C-48, they form a bidirectionally discoverable named anchor (locatable by label-name match from use sites; discoverable by forward enumeration from P-0). The two are independently achievable; the complete structural address pair requires both.

- **C-50** (depends on C-47) — Content-cell provenance attribution: echo row content opens with `"Per P-0 anti-bypass declaration:"` (or `"Per P-0, ABD:"` when C-48 passes) before the dual-named bypass text. Gap closed: C-47 places provenance in the row label; an executor scanning only the content cell has no provenance signal without C-50.

**Aspirational maxima seeded for v19:** complete structural address pair (C-48 + C-49, V-04 form) and ABD-labeled content-cell provenance attribution (C-48 + C-50, V-05 form).
