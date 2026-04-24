`topic-retro-variate-R18-2026-03-17.md` written. Here's the summary:

---

## R18 Variations — topic-retro (Rubric v16)

**Base:** R17-V-05 (carries C-22 through C-41). **Targeting:** C-42 (bidirectional manifest citation) and C-43 (PRE-EXECUTION CONTRACT as manifest navigation index).

| ID | Axis | C-42 mechanism | C-43 mechanism |
|----|------|----------------|----------------|
| V-01 | C-42 single | `Derived Views` column added to AUDIT MANIFEST + `[DERIVED FROM: AUDIT MANIFEST \| OPERATION: ...]` headers on every downstream section | Contract unchanged (no `Manifest column` field) |
| V-02 | C-43 single | Backward citations only; no `Derived Views` column | Fourth column `Manifest column` added to PRE-EXECUTION CONTRACT, mapping each commitment to exact AUDIT MANIFEST column name |
| V-03 | Phrasing register | Inline `FEEDS:` annotations in manifest rows instead of structural column | Inline `SOURCES:` annotations in contract rows instead of structural field — tests rubric's "structural columns required, prose substitution = PARTIAL" rule |
| V-04 | C-42 + C-43 combined | `Derived Views` column from V-01 | `Manifest column` field from V-02 — zero-interference test (two changes live in separate table cells) |
| V-05 | Full integration | `Derived Views` column + bidirectional navigation check statement in Phase 0 + Phase 0 SEAL verifies both directions | `Manifest column` field + PRE-EXECUTION CONTRACT opening block with three named entry-point instructions (manifest row → downstream, downstream → manifest, contract row → manifest column) |

**Key design decisions:**
- V-03 is the deliberate PARTIAL-hypothesis test — if the rubric's structural-column requirement is correctly enforced, V-03 scores PARTIAL on C-42/C-43 while matching V-01/V-02 on all other criteria
- V-05's Phase 0 SEAL items 5-7 are the innovation: they verify navigability (specific table names in Derived Views, forward/backward check statements) not just presence — prevents the "filled with generic text" PARTIAL condition
- All five carry the full R13-R17 mechanism stack (Phase 0 AUDIT MANIFEST, reconciliation table, three-field Phase 8 SEAL, etc.)
