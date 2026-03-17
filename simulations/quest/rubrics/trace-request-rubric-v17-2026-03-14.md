`trace-request-rubric-v17-2026-03-15.md` written. Here is a summary of what changed:

---

## v17 changes from v16

**Two new criteria from R18 excellence signals:**

**C-42 — Step 8b DECLARE CONTRADICTION intertextual HALT-EXPECTED-BOUNDARY match flag** (Tier B+ promoted)
- Source: V-02 (single-axis C-42 surface 1) and V-05 (combined) both stably produced the four-field form `DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [which arm] -- matches HALT-EXPECTED-BOUNDARY: [yes/no]` in Step 8b prose before Step 8c was populated
- Two independent variation axes = sufficient evidence to freeze the surface
- Depends on C-40 AND C-39 (needs the three-field prose token AND the HALT-EXPECTED-BOUNDARY pre-declaration to cross-reference)

**C-43 — Step 12 FAIL-CATEGORY closed-vocabulary token per finding row** (Tier D promoted to Tier C)
- Source: V-03 (single-axis) and V-05 (combined) both produced `FAIL-CATEGORY: [AUTH / BOUNDARY / CONTRACT / TIMEOUT / STATE / PERMISSION]` on every Step 12 finding row with values drawn exclusively from the frozen six-item vocabulary
- Two independent variation axes = sufficient evidence to freeze vocabulary and surface
- Depends on C-06 (first cross-tier dependency — Step 12 Findings structure is a Recommended criterion; FAIL-CATEGORY extends that structure)

**Scale: 260 → 270** (aspirational: 34 → 36 criteria, 170 → 180 pts). Golden threshold: 216/270 (80%).

**Signal not promoted to v17 — C-44 design surface:**
- TRACE CONTRACT validation outcome structurally derivable from DECLARE CONTRADICTION `matches HALT-EXPECTED-BOUNDARY: [yes/no]` value — R18 V-02 surfaced the falsification path (`matches HALT-EXPECTED-BOUNDARY: no` → "falsified" validation token) but live paired-execution evidence showing matching token values across both confirmation and falsification branches is needed before the consistency constraint can be frozen
