Written to `simulations/quest/golden/campaign-track-variate-R3-2026-03-16.md`.

---

# Variations -- campaign-track / Round 3

Five complete variations targeting the three new R2 aspirational criteria. First variate run for this skill.

---

## V-01 -- Per-role prohibition lists (C-14)
**Axis**: Each named persona (Registrar / Planner / Analyst / Narrator) carries 5 explicitly enumerated forbidden actions.  
**Covers**: C-01..C-09, C-11..C-14 = **14/16**  
**Misses**: C-15 (no type specs), C-16 (no terminal checklist)  
**Hypothesis**: Named prohibitions per role prevent the most common failure mode -- a model blurring role boundaries by synthesizing in the planning phase or planning in the narrative phase.

---

## V-02 -- Typed output contracts (C-15)
**Axis**: Each phase declares exact value types: `integer` for table cells, `enumerated string` for verdict and readiness fields, required field lists.  
**Covers**: C-01..C-09, C-11..C-13, C-15 = **14/16**  
**Misses**: C-14 (roles described but not prohibited), C-16 (no terminal checklist)  
**Hypothesis**: Typed contracts make every field independently verifiable -- `planned: integer` eliminates "several signals" as a valid response.

---

## V-03 -- Terminal completion checklist (C-16)
**Axis**: A named `TERMINAL` section after Phase 4 requiring explicit PASS/FAIL per phase postcondition before the campaign is marked complete.  
**Covers**: C-01..C-09, C-11..C-13, C-16 = **14/16**  
**Misses**: C-14 (no prohibitions), C-15 (no type specs)  
**Hypothesis**: Active PASS/FAIL confirmation per phase closes the failure mode of claiming completion after running only 2-3 phases.

---

## V-04 -- Combined: prohibitions + typed contracts (C-14 + C-15)
**Axes**: V-01 prohibition lists + V-02 typed contracts  
**Covers**: C-01..C-15 = **15/16**  
**Misses**: C-16 only  
**Hypothesis**: Role bleed (behavioral) and artifact ambiguity (structural) are independent failure modes; combining their fixes is additive.

---

## V-05 -- Full stack: prohibitions + contracts + terminal checklist + lifecycle emphasis (C-14 + C-15 + C-16)
**Axes**: All three new axes plus heavy per-phase lifecycle structure  
**Covers**: All 16 criteria = **16/16**  
**Hypothesis**: Each axis contributes independently -- prohibitions close role bleed, typed contracts close artifact ambiguity, TERMINAL checklist closes premature completion, lifecycle emphasis communicates the four-phase structure to a model that might otherwise compress phases.

---

**Predicted leaderboard**: V-05 > V-04 > V-01 = V-02 = V-03

Key open scoring question: does C-14 require explicit enumerated forbidden actions (rubric says "named forbidden actions, not just a role description") -- V-02 and V-03 have role descriptions only and will fail C-14 on a strict read.
