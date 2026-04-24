Written to `simulations/quest/golden/mock-accept-variate-R4-2026-03-16.md`.

---

## mock-accept Variate — Round 4

**Baseline:** R3 V-05 (all prior mechanisms carried forward)
**New criteria targeted:** C-17, C-18, C-19 from v4 rubric

### Axis-Assignment Plan

| Variation | Axis | Target | Core change |
|-----------|------|--------|-------------|
| **V-01** | lifecycle-emphasis | C-17 | BRANCH B gains `Semantics: SUCCESS — correct disclosure output, not an error` as a labeled parseable field, not embedded prose |
| **V-02** | output-format | C-18 | CANARY TERMINOLOGY TABLE (2-row structured table) inserted before BRANCH A/B definitions — separates disambiguation from instruction prose |
| **V-03** | phrasing-register | C-19 | `Subject-check:` metacognitive sub-step inserted before `Error-code:` — forces explicit identification of grammatical subject before emitting VERDICT-ECHO vs NONE |
| **V-04** | lifecycle-emphasis + output-format | C-17 + C-18 | V-01 Semantics field + V-02 terminology table (non-overlapping: BRANCH B interior + pre-branch table) |
| **V-05** | all three axes | C-17 + C-18 + C-19 | Full R4 integration: Semantics field + terminology table + metacognitive subject-check + all R3 bases |

### Key design decisions

- **C-17 mechanism**: Prose "not an error" wasn't checkable. `Semantics: SUCCESS` is a field.
- **C-18 mechanism**: Inline "Do NOT conflate" sentence could be paraphrased past. A 2-row table with explicit Type column (Correct output / Named error) forces distinct labeling per term.
- **C-19 mechanism**: Models can write `Error-code: NONE` by default without checking the subject. The `Subject-check:` sub-step forces the test to happen explicitly before the field is emitted — the NONE branch becomes a deliberate result, not a fallback.
