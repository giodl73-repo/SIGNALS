Here is the complete updated rubric:

---

# Rubric -- topic-plan (v4)

**Skill**: `topic:plan`
**Version**: v4 (promoted from v3 after Round 3 excellence signal extraction)
**Date**: 2026-03-15

---

## Summary

| Tier | Count | Points | Criteria |
|------|-------|--------|----------|
| Essential | 5 | 60 | Read strategy, read signals, identify delta, type proposals, confirm gate |
| Recommended | 3 | 30 | Evidence citations, before/after view, all three change types |
| Aspirational | 12 | 60 | ...+ diff proposal cross-reference, delta finding column |

**Total possible: 150 pts**

---

## Two new aspirational criteria

**C-19 — Diff table includes a Proposal ID cross-reference column** | format

The before/after diff table includes a "Proposal" column cross-referencing each changed entry to its source proposal row ID (e.g., "ADD-1", "REPRIORITIZE-3"). This creates a navigational link from the user's final review surface (the diff) to the evidence (the proposal table) without requiring inline brackets on every diff row. A diff with no row anchors requires the user to rescan the full proposal section during confirmation; an anchored diff makes the confirmation review single-pass. A prompt that satisfies C-13 (full inline brackets in the diff) may satisfy C-19 simultaneously.

**C-20 — Proposal table includes a Delta Finding column for all change types** | depth

Every row in the ADD / REMOVE / REPRIORITIZE table includes a "Delta Finding" column naming the specific structured finding from the delta step that motivated it — e.g., "Finding #2: Strategy assumed exec alignment implicit / Signal revealed no exec-level champion identified." This generalizes the two-level traceability chain (C-16) from conflict-driven proposals to all proposal types. The "None proposed" rows for empty types require "Delta Finding: N/A" to keep the column structurally consistent. A table with only an Evidence column (artifact filename) but no Delta Finding column is a partial pass for C-16 and a fail for C-20.

---

## Minor pass-condition clarifications

- **C-14**: added explicit partial-pass condition — framing the correct behavior without naming the anti-pattern label ("plain inventory") is now marked partial, consistent with how Round 3 scored V-03/04/05.
- **C-17**: extended pass condition — the null-case instruction must appear regardless of whether conflicts are presented in table format or inline annotation, closing the V-01/V-04 gap.

---

## Meta-pattern

C-19 and C-20 address the same layer: *navigability*. The information exists somewhere in the output, but the reviewer cannot reach it without re-reading unrelated sections. C-19 bridges the diff to the proposal table via a pointer column. C-20 bridges each proposal row to its delta finding via a dedicated column. With both present, the entire output is navigable in two hops from any starting point — and C-16 moves from a structural aspiration to a mechanically achievable criterion.
