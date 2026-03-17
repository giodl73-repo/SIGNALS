Here are the five complete variations for trace-contract Round 3 under rubric v3.

---

## Round 3 Variation Map

| Variation | Axis | Primary Targets | Hypothesis |
|-----------|------|-----------------|------------|
| **V-01** | output-format | C-14 | Add mandatory `connector-impact:` slot to every finding block — converts at-least-one callout (C-06) to per-finding structural enforcement (C-14) |
| **V-02** | output-format | C-15 | Separate template for breaking findings with `recommended-action:` as required fifth labeled slot — converts prose inclusion (C-09) to structural enforcement (C-15) |
| **V-03** | lifecycle-emphasis | C-13 | Replace `[CONTRACT COMMITTED]` with the exact token `[EXPECTED SEALED]` defined explicitly as a machine-parseable boundary marker — converts prose gate (C-12) to structured token (C-13) |
| **V-04** | output-format combination | C-14 + C-15 | V-01 + V-02 combined — both finding-block structural additions in one template; axes are orthogonal and additive |
| **V-05** | lifecycle-emphasis + output-format | C-13 + C-14 + C-15 | All three new criteria in one variation; anatomy-first skeleton mitigates prompt density risk by showing the complete artifact shape (including all new fields) before instructions |

---

**Key structural changes per new criterion:**

- **C-13**: `[EXPECTED SEALED]` replaces `[CONTRACT COMMITTED]`; defined in the prompt as a machine-parseable string, not a prose acknowledgment; exact string on its own line; paraphrase explicitly disallowed
- **C-14**: `connector-impact:` field added between `spec:` and `hypothesis:` in every finding block; requires either a specific impact or explicit "none — [rationale]"; no finding may omit the field
- **C-15**: Breaking findings use a separate named template (Template A); `recommended-action:` is the sixth required field; vocabulary constrained to `amend-spec | fix-impl | needs-discussion`; the field is labeled in the template definition so its absence is self-announcing

Written to: `simulations/quest/golden/trace-contract-variate-R1-v3-2026-03-15.md`
