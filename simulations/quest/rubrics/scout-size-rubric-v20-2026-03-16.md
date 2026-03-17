Two new criteria added from R19 excellence signals:

**C-42 — Defense cluster co-located entirely within standalone gap section when C-32 is active**
Derived from V-01's C-30 FAIL. Once C-32 promotes the gap to a standalone section, the compilation table's gap column becomes a pointer (C-40) — not a production site. V-01 used the compilation table's column header as the structural-label mechanism (one of C-30's three) while the self-test and WRONG/CORRECT lived in the Phase 2 instruction section. C-42 closes this: all three defense mechanisms must be inside the standalone section itself.

**C-43 — Standalone gap section precedes output compilation table in prompt order**
Derived from V-01's C-32 PARTIAL. V-01 had the visual delimiter and standalone section but positioned it *after* the compilation table. That means the model writes a pointer before generating the content it points to — a forward reference. C-43 requires the standalone section to appear earlier in prompt order than the compilation table, so the pointer always follows already-fixed content.

Scoring changes: 35 aspirational criteria (was 33), max 125 pts (was 123).
