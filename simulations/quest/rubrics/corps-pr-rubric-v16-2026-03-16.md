`corps-pr-rubric-v16-2026-03-17.md` written. Here is a summary of what changed:

---

## v15 → v16: Two new criteria

**C-49 — Eliminated-to-CLOSED-PATHS reverse cross-reference**

C-48 closed the audit loop from the *declaration side*: CLOSED PATHS block → Eliminated sub-entry. C-48 explicitly flagged it does not require the reverse. C-49 closes that gap: the `Eliminated [C-NN]:` sub-entry must carry a back-reference naming the CLOSED PATHS block by its label and section (e.g., `"Declaration: see 'Closed paths [C-43]:' in pipeline declaration [C-45]."`). With both C-48 and C-49 satisfied, the loop is traversable from either endpoint.

**C-50 — Bidirectional symmetry declaration**

When C-48 and C-49 are both satisfied, their bidirectional relationship is only *observable* by following both references — it is not declared. C-50 requires a named terminal element in the structural enforcement levels section explicitly asserting the loop is closed bidirectionally (e.g., `"Audit loop closed [C-50]: 'Closed paths [C-43]:' and 'Eliminated [C-46]:' cross-reference each other bidirectionally -- traversable from either endpoint without reading intervening content."`). An auditor can then confirm closure from a single read without reference traversal.

## Scoring update

| Band | Count | Per-criterion | Total |
|------|-------|--------------|-------|
| Essential (C-01–C-05) | 5 | 12.000 | 60 |
| Recommended (C-06–C-08) | 3 | 10.000 | 30 |
| Aspirational (C-09–C-50) | **42** | **~0.238** | 10 |
| **Max** | | | **100** |

**R17 against v16**: all five score 40/42 aspirational (99.52 composite). **R18 target**: add C-49 back-reference + C-50 symmetry declaration.
