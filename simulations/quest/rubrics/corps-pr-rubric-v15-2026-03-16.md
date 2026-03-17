Here is the complete updated rubric — `corps-pr-rubric-v15-2026-03-17.md`.

---

## Two new criteria extracted from R16

**C-47 — C-46 named-entry elevation gap**

R16 showed two forms of C-46 compliance:
- **Inline clause** (V-01, V-02): `; no inline-cell alternative path [C-46]` appended to C-40's description — satisfies C-46, but finding the negation requires parsing C-40's text.
- **Named sub-entry** (V-03, V-04, V-05): `Eliminated [C-46]:` as a distinct labeled entry with the self-declaration "auditable by label-matching 'Eliminated [C-46]:' without parsing C-40" — satisfies C-47.

C-47 is the structural enforcement analog of C-45: C-45 elevated C-43's prohibition from format rules to a named CLOSED PATHS block; C-47 elevates C-46's negation from an inline clause to an independently-labeled sub-entry separately reachable by label.

**C-48 — C-45/C-47 cross-link gap**

When both C-45 and C-47 are satisfied, the audit loop is still open: an auditor at the CLOSED PATHS block cannot directly reach the Eliminated sub-entry without structural knowledge of the document. V-05 closed it: the CLOSED PATHS block adds `"Path negation: see 'Eliminated [C-46]:' in structural enforcement levels above [C-46]."` C-48 requires exactly this cross-reference — one-directional from declaration to enforcement.

---

## Scoring update

| Band | Count | Per-criterion | Total |
|------|-------|--------------|-------|
| Essential (C-01–C-05) | 5 | 12.000 | 60 |
| Recommended (C-06–C-08) | 3 | 10.000 | 30 |
| Aspirational (C-09–C-48) | **40** | **0.250** | 10 |
| **Max** | | | **100** |

**R16 scores against v15**: V-01 and V-02 score 38/40 (99.5); V-03 and V-04 score 39/40 (99.75, pass C-47, miss C-48); V-05 scores 40/40 (100, passes both). **R17 target**: replicate V-05's named sub-entry + CLOSED PATHS cross-reference pattern across all variations.
