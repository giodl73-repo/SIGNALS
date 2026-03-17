Written to `simulations/quest/golden/campaign-decide-variate-R5-2026-03-16.md`.

---

# Variations — campaign-decide / Round 5

**R4 → R5 diagnosis:** All three new v5 criteria (C-18, C-19, C-20) were already satisfied by R4's best variants. The only surviving scoring ambiguity is **C-12 strict** — R4 used `because F0-[seq]` (FID key only), while the rubric example is `because Phase [N], [section reference]` (Phase prefix present). That is the R5 target.

---

## V-01 — C-12 hybrid citation format
**Axis:** Change only the Because block citation format from `because F[N]-[seq]` to `because Phase N, F[N]-[seq]`. Base is R4 V-01 unchanged otherwise.

**Why it works:** The hybrid contains both tokens — Phase prefix satisfies the rubric example syntax; FID key satisfies mechanical auditability. No strict scorer can fail either requirement.

**Predicted v5:** 12/12 = **100.0** (no remaining risk).

---

## V-02 — Inertia elevation (Phase 1a / Phase 1b sub-section structure)
**Axis:** Split Phase 1 into `### Phase 1a — Inertia Analysis [COMPLETE BEFORE PHASE 1b]` and `### Phase 1b — Named Rivals`. C-04 is now enforced at the section boundary, not just by field-ordering instruction.

**C-20 bonus:** Adds a third gate annotation to the template (FINDING REGISTER + Phase 0 + Phase 1a), reinforcing the structural pattern.

**Predicted v5:** 12/12 = **100.0** liberal / 99.2 strict C-12 (citation format unchanged from R4 V-01).

---

## V-03 — C-20 graft on non-FID template (boundary test)
**Axis:** Take R4 V-02 (table format, no FIDs, hypothesis Phase 4) and add `[COMPLETE BEFORE PHASE N]` to all section headers. Tests whether C-20 is achievable without a FID system, and what its marginal value is.

**Key finding baked in:** C-20 PASS + C-13 FAIL simultaneously — C-20 is a structural format criterion (gates in headers) not an ordering correctness criterion. C-18/C-19 still FAIL because they require C-15 as prerequisite.

**Predicted v5:** 7/12 = **95.83** (+0.83 from R4 V-02's 95.0). The graft is low-yield vs. adding a FID system (+4 criteria, +3.33 pts).

---

## V-04 — Combined: C-12 hybrid + Phase 1a/1b inertia elevation
**Axes:** Both V-01 and V-02 together on the R4 V-01 base. Zero remaining ambiguity: C-12 hybrid eliminates the strict-scorer risk; Phase 1a/1b elevates C-04 to section-level enforcement.

**Predicted v5:** 12/12 = **100.0** under all scoring interpretations.

---

## V-05 — Combined: all R5 axes, conversational phrasing register
**Axes:** V-04 structure with conversational prose replacing imperative headers — FINDING REGISTER drops all-caps, Phase 0 and Phase 1a drop bracket gate annotations in favor of prose preambles (only the Finding Register header retains `[COMPLETE BEFORE PHASE 0]`).

**C-20 boundary test:** Phase 0 and Phase 1a no longer carry bracket annotations in their headers. C-20 liberal (one annotated header sufficient) → 12/12 = **100.0**. C-20 strict (all ordering headers must be annotated) → 11/12 = **99.2**. This is the predicted V-04 > V-05 differentiator.

---

**Predicted ranking:** V-04 >= V-01 > V-02 = V-05 >> V-03
