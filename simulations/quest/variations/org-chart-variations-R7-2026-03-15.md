Written to `simulations/quest/golden/org-chart-variate-R7-2026-03-16.md`.

---

## Round 7 Summary

**R6 ceiling:** 14/16 — V-01 held C-22+C-23 (4-part + count guard), V-02 held C-21+C-24 (register + typed citations). No variation held all four.

**R7 variation map:**

| V | Axis | Single/Combined | Key Change | Target |
|---|------|-----------------|------------|--------|
| V-01 | Inertia framing | Single | **Count-anchored two-step guard** — explicit count-check directive before emitting the separator, prevents premature guard emission and wrong counts | 14/16: C-09-C-20, C-22, C-23 |
| V-02 | Output format | Single | **Inline-schema register** — category-schema table embedded in the register block output itself (`cat-1` through `cat-4` defined in the produced document), eliminating prompt-memory dependency for APW citations | 14/16: C-09-C-21, C-24 |
| V-03 | Phrasing register | Single | **Descriptive framing** for both guard and register — tests whether observable artifacts (separator line, register block) require directive DO/DO-NOT language or can be produced with conversational framing | Uncertain: 14/16 if framing is neutral, lower if directive framing is load-bearing |
| V-04 | Framing + format | Combined | V-01 count-anchored guard + V-02 inline-schema register on the full C-09-C-20 base. 4-part inertia + 9 sections. | **First 16/16 candidate** |
| V-05 | Framing + format + lifecycle | Combined | V-04 + section-verification checklist at end of prompt (post-hoc ordering guard, not inline gates) | 16/16 if guard is additive; possible degradation if it triggers compression |

**The key structural move:** V-04 achieves the 16/16 target by fusing the two designs that each scored 14/16 in R6. The inline-schema table inside the register block is the new structural bet — it makes `cat-N` codes self-documenting in the output, so the model can verify its own APW citations against the schema row it just wrote rather than relying on prompt-instruction memory.
