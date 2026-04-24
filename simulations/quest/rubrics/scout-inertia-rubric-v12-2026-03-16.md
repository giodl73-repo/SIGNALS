`scout-inertia-rubric-v12-2026-03-17.md` written. Ceiling 180 → 195.

---

**v11 -> v12: three new criteria**

| # | Criterion | Source signal |
|---|-----------|---------------|
| A-26 | **Analytical axis vocabulary in section heading subtitles** | R11 V-03: `## FAIL-FIRST DECLARATION -- THE UNNAMED COMPETITOR` and `## SECTION 1 -- THE STATUS QUO'S VULNERABILITIES: FAILURE MODE INVENTORY`. A-10 and A-14 require these sections to exist; A-26 requires their heading subtitles to encode the template's analytical axis vocabulary. A-26 implies A-10 and A-14. |
| A-27 | **Decision-question bridge gate heading** | R11 V-03: `## BRIDGE COMPLETION GATE -- READY TO PROCEED?` A-22 requires the gate block in position; A-25 requires an active directive inside it; A-27 requires the heading line itself to carry an interrogative decision marker. A-27 implies A-22; A-27 is independent of A-25. |
| A-28 | **Criterion ID in trailing checklist item labels** | Extension of A-23 traceability pattern. A-23 places criterion IDs in integrity rule labels (integrity chain); A-28 places criterion IDs in trailing checklist item labels (verification chain). `C-01: Workaround named specifically (Y/N)` passes; `Workaround named specifically (Y/N)` fails. A-28 implies A-18. R12 will confirm whether R11 variations already satisfy this retroactively. |

**Updated implication chain**: A-27 implies A-22 implies A-12. A-25 implies A-22 implies A-12. A-26 implies A-10 and A-14. A-28 implies A-18 implies A-15. All prior chains unchanged.

**Structural note added on A-23**: R11 V-03 stress test explicitly confirmed — domain-prefix form (`STATUS QUO LOCK RULE [A-16]`) is valid alongside bracket-prefix and bracket-suffix forms.
