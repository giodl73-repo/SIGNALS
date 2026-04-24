v14 written to `simulations/quest/rubrics/flow-conversation-rubric-v14-2026-03-15.md`.

---

**3 new criteria extracted from R14 (+6 pts, max 222 → 228):**

| ID | What it captures | Wt | Source |
|----|------------------|----|--------|
| C-63 | Full HANDOFF_TO lifecycle chain — every role transition bidirectionally locked with outgoing `HANDOFF_TO:` and incoming `"Received …"`, covering all 5 transitions (Phase -1→TA, TA→CA, CA→Dev, Dev→Auditor, Auditor→RP); the two C-60 tokens become a complete lifecycle protocol | 2 | V-05 exclusive |
| C-64 | Manifest row-level schema-type annotation — PRE_FLIGHT_MANIFEST rows for Phase 0-A-8/9/10/11 carry `SCHEMA_TYPE: FIELD\|VALUE`; wrong format → `STATUS: WRONG_SCHEMA` (not MISSING); manifest is the enforcement origin for schema type, not the rubric | 2 | V-05 exclusive |
| C-65 | Quantitative row-count contract in CA verification — each C-62 declaration verified with parenthetical row count: `DECLARATION_NAME: PASS\|FAIL (count N rows: [named breakdown])`; partial population names missing fields; binary PASS\|FAIL without count does not satisfy | 2 | V-03 / V-05 |

**Cluster logic:** C-63 closes the lifecycle axis (extends C-60), C-64 closes the enforcement-origin axis (extends C-59), C-65 closes the verification-granularity axis (extends C-62). Together they eliminate the three remaining ambiguity zones that V-04 scored PARTIAL on in prior rounds.
