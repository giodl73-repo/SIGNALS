Here are the 5 Round 13 variations, written to `simulations/quest/golden/trace-state-variate-R13-2026-03-15.md`.

---

## Round 13 Variation Map

| Var | Axis | Hypothesis | New Criteria |
|-----|------|------------|--------------|
| **V-01** | Role sequence (Finance → Sales → CS) | Finance-first ordering naturalizes disqualification vocabulary in field labels — hardest numeric failures named first (C-34); C-35 absent to isolate | C-34 single-axis |
| **V-02** | Output format (step blocks + C-35 section headers) | Consequence clauses *in* section headings (not body) make enforcement visible at navigation level before entering any section; C-34 absent from field labels | C-35 single-axis |
| **V-03** | Lifecycle emphasis (four sub-steps, C-34 on sub-element labels) | Sub-step labels are the natural C-34 carrier — each already names its criterion, so appending the disqualifying pattern is minimal-friction; most granular placement possible | C-34 single-axis |
| **V-04** | Role sequence + output format (CS → Finance → Sales) | CS-first + dual-layer annotation: C-34 in column headers AND C-35 in section headings; every structural element has both "what fails the field" and "what fails the section" | C-34 + C-35 combined |
| **V-05** | Phrasing register + inertia framing (conversational + "naive trace" foil) | Foil primes against specific failure modes; C-35 makes enforcement visible when section heading is scanned; C-34 names the exact failing pattern at cell level | C-34 + C-35 combined |

---

**Key design distinctions enforced across all 5:**

- **C-34 vs C-30**: C-30 = behavioral directive in field label ("min 2 per pass — never skip"); C-34 = disqualification condition in field label ("'ID is not null' does not qualify"). Many V-01/V-03/V-04/V-05 labels earn both from a single annotation.

- **C-35 vs C-23**: C-23 = invalidation clause *anywhere in section prose*; C-35 = consequence clause fused with criterion ID *in the section heading itself* (`### Section Name [C-ID: consequence]`). V-02/V-04/V-05 section headings carry the `[C-ID: consequence]` bracket form; body text alone would only earn C-23.

- **Single-axis isolation**: V-01 and V-03 have no `[C-ID: consequence]` section headings. V-02 has no disqualification conditions in field labels. This allows the rubric to probe each criterion independently before measuring combined contributions in V-04 and V-05.
