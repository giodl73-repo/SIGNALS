Here is the complete v16 rubric. Summary of what changed:

---

## v16 changes from v15

**Two new criteria from R17 excellence signals:**

**C-40 — Step 8b DECLARE CONTRADICTION prose token** (Tier B promoted)
- Source: V-02 (single-axis formal register) and V-05 (three-axis combined) both stably produced `DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [which arm]` in Step 8b prose before the Step 8c table populated
- Two independent variation axes = sufficient evidence to freeze the surface
- Depends on C-30 only (no C-39 dependency — the token carries its own BC-N + arm fields)

**C-41 — Pre-trace CHECKER ALGORITHM with HALT-EXPECTED-BOUNDARY reference** (Tier C promoted)
- Source: V-04's Algorithm-Declarant role (Phase 0B) emitted CHECKER ALGORITHM with a HALT-RULE that named `HALT-EXPECTED-BOUNDARY` as a structural token in the halt predicate — binding the algorithm to the specific predicted boundary before evidence exists
- Depends on C-37 AND C-39 (needs the CHECKER ALGORITHM schema and the TRACE CONTRACT to both exist)

**Scale: 250 → 260** (aspirational: 32 → 34 criteria, 160 → 170 pts). Golden threshold: 208/260 (80%).

**Signals not promoted to v16 — C-42 design surfaces:**
1. V-05's enhanced `DECLARE CONTRADICTION` with `-- matches HALT-EXPECTED-BOUNDARY: [yes/no]` intertextual field — needs multi-round evidence across axes before the three-way intertextual surface can be frozen
2. Error path category taxonomy — still no structural token vocabulary to freeze
