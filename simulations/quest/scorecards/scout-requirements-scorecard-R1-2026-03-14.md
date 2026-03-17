## scout-requirements R1 Scorecard — Complete

**Rubric v5 (116 pts). 5 variations scored.**

---

### Scores

| Rank | Variation | Score | Band |
|------|-----------|-------|------|
| 1 | V-05 Template + Three-Loop | **115** | Golden |
| 2 | V-01 Role Sequence | **101** | Strong |
| 2 | V-04 Lifecycle + Inertia | **101** | Strong |
| 4 | V-02 Template-Completion | **95** | Weak* |
| 5 | V-03 Discovery Questions | **90** | Weak* |

*V-02/V-03: C-05 PARTIAL — no dedicated per-lens extraction steps; all-four-lens coverage not structurally guaranteed.

---

### Key Findings

**V-05 gets 115/116.** The only miss is C-21 PARTIAL: the charter assigns loops by structural role (declare/apply/verify) but doesn't name them as C-17/C-18/C-19 by rubric ID. One point short of perfect.

**V-05 clears all C-14 through C-20** — the entire new v5 cluster — simultaneously. Prior variations top out at C-13 (11 aspirational pts). V-05 earns 25/26.

**C-05 is the key discriminator for essential.** V-01 and V-04 both use dedicated per-lens extraction steps and reliably PASS. V-02 and V-03 skip them, creating structural risk that drops their essential totals to 54.

**V-04 and V-01 tie at 101.** V-04's lifecycle-by-construction is the stronger C-11 mechanism; V-01's structure is simpler. Both are valid R2 base candidates.

---

```json
{"top_score": 115, "all_essential_pass": true, "new_patterns": ["prevention-detection complementarity as explicit design contract: Loop 2 creates artifacts Loop 3 requires as evidence -- charter names this relationship making it a structural dependency", "three-loop enforcement applied simultaneously to multiple concurrent laws -- declare/apply/verify triplet for each law in parallel with no single-point failure", "recursive meta-loop: enforcement mechanism is self-enforcing via the same three-loop pattern it describes -- C-17/C-18/C-19 are themselves declare/apply/verify of the meta-requirement"]}
```
**Aspirational total** | **26** | **11** | **11** | **11** | **11** | **25** |
| **COMPOSITE** | **116** | **101** | **95** | **90** | **101** | **115** |
| **Band** | | Strong | Weak* | Weak* | Strong | **Golden** |

*V-02 and V-03: C-05 PARTIAL -- essential criterion not reliably satisfied; band classification conservative.

---

## Ranking

| Rank | Variation | Score | Band | Decisive Factor |
|------|-----------|-------|------|-----------------|
| 1 | **V-05 Template + Three-Loop** | **115** | Golden | Only variation to cover C-14 through C-20 simultaneously; three-loop meta-requirement enforces Laws A and B via declare/apply/verify |
| 2 | **V-01 Role Sequence** | **101** | Strong | Dedicated four-lens extraction (C-05 reliable); all essential + recommended pass; aspirational stops at C-13 |
| 2 | **V-04 Lifecycle + Inertia** | **101** | Strong | Same score as V-01; adds inertia framing to Won't Have and lifecycle phase tagging per-requirement; C-11 structurally stronger |
| 4 | **V-02 Template-Completion** | **95** | Weak* | Pre-printed closure sentences earn C-16 PASS; C-09 PARTIAL (no chain format); C-05 PARTIAL (no lens extraction steps) |
| 5 | **V-03 Discovery Questions** | **90** | Weak* | C-05 and C-08 PARTIAL; C-16 PARTIAL; strongest for C-06/C-07 by phrasing register but structure gaps prevent full essential pass |

---

## Per-Variation Analysis

### V-01 -- Role Sequence (PM -> Arch -> UX -> Comp)

**Score: 101 / 116 -- Strong**

| C | Rating | Evidence |
|---|--------|----------|
| C-01 | PASS (12) | Step 0 searches both `simulations/scout/` and `simulations/trace/skill/`; SF-01 status keyed to trace find. |
| C-02 | PASS (12) | Step 5 MoSCoW table with four named tiers; consolidates all lens outputs. |
| C-03 | PASS (12) | Step 6 requires root blocker, "state why foundational," direct + transitive chain format R-NN -> R-MM -> R-PP. |
| C-04 | PASS (12) | Step 7 AF- section with mandatory A/B/Consequence format; "zero AF- on complex input is a fail." |
| C-05 | PASS (12) | Steps 1-4 dedicate one step per lens (PM, Architect, UX, Compliance). Four explicit extraction passes guarantee all four lenses. |
| C-06 | PASS (10) | Step 8 lifecycle table with five named phases; SILENT phases flagged. |
| C-07 | PASS (10) | Step 9 SF- section with gap/contradiction format. |
| C-08 | PASS (10) | Stable R-IDs required; tier promotion note pre-printed ("Promoted R-NN from [tier] to [tier]: [reason]"). |
| C-09 | PASS (2) | "R-NN (root) -> R-MM -> R-PP. Second-order chains required. State why root blocker is foundational." Explicit chain format + foundational reasoning. |
| C-10 | PASS (2) | Step 7 AF- format: `Source: "[exact text from input]"` -- source citation required per entry. |
| C-11 | PASS (2) | Step 8 enumerates all five lifecycle phases (First-run, Core-use, Upgrade, Error, Observability) with coverage status. |
| C-12 | PASS (2) | "Carry forward all AF- from prior runs" + `Status: open / resolved / out-of-scope` field per AF- entry. |
| C-13 | PASS (2) | Step 7 AF- format pre-prints Interpretation A / Interpretation B / Consequence fields. |
| C-14 | FAIL (0) | No verification protocol step. Output ends at "Write artifact." No pre-output rubric self-check. |
| C-15 | FAIL (0) | No inline [AMBIG:] notation instruction during lens steps. Ambiguity detection deferred entirely to Step 7. |
| C-16 | PARTIAL (1) | "Carry forward all AF-/SF- from prior runs" present but no pre-printed closure sentence in the exact required format. |
| C-17 | FAIL (0) | No charter; no three-loop structure. |
| C-18 | FAIL (0) | No "Apply Law X here" cross-references at extraction steps. |
| C-19 | FAIL (0) | No verification table. |
| C-20 | FAIL (0) | No charter; no prevention-detection complementarity statement. |
| C-21 | FAIL (0) | No recursive meta-loop structure. |

**Decisive strength**: PM-first role sequence with dedicated steps per lens is the most reliable mechanism for C-05. No variation produces a stronger structural guarantee for all-four-lens coverage. Clean essential + recommended pass with low complexity.

**Decisive gap**: Aspirational ceiling at C-13; C-14/C-15/C-16 all miss. V-01 is the correct base structure but has no enforcement machinery for the new criteria.

---

### V-02 -- Template-Completion (Pre-Printed Skeleton)

**Score: 95 / 116 -- Weak***

| C | Rating | Evidence |
|---|--------|----------|
| C-01 | PASS (12) | SEARCH GATE section pre-printed with both directory slots; SF-01 status pre-printed. |
| C-02 | PASS (12) | Four tiers pre-printed as headers (MUST HAVE / SHOULD HAVE / COULD HAVE / WON'T HAVE). |
| C-03 | PASS (12) | DEPENDENCY ROOT section pre-printed with root blocker, "why foundational," direct/transitive blocks fields. |
| C-04 | PASS (12) | AF-01/AF-02 slots pre-printed with "zero AF- on complex input is a fail" reminder. |
| C-05 | PARTIAL (6) | Lens column present ("[PM / Arch / UX / Comp]") but no dedicated per-lens extraction steps. All-four-lens coverage not structurally guaranteed. |
| C-06 | PASS (10) | SUSPICIOUS SILENCES lifecycle table pre-printed with five phases. |
| C-07 | PASS (10) | SPEC-FAULT FINDINGS section pre-printed with severity + status fields. |
| C-08 | PASS (10) | IDs pre-printed as R-01, R-02 starters; TIER PROMOTIONS table pre-printed. |
| C-09 | PARTIAL (1) | "Blocks transitively: [R-IDs via chain R-NN -> R-MM -> R-PP]" field present but "second-order chains required" is not a stated rule. |
| C-10 | PASS (2) | AF- template slot: `Source: "[exact quote from input spec]"` -- pre-printed citation format. |
| C-11 | PASS (2) | Five lifecycle phases pre-printed in SUSPICIOUS SILENCES table. |
| C-12 | PASS (2) | "Prior AF- carried forward: [list IDs]" in SEARCH GATE + closure instructions in findings sections. |
| C-13 | PASS (2) | AF- template pre-prints Interpretation A / Interpretation B / Consequence / Status fields. Structure guaranteed by slot. |
| C-14 | FAIL (0) | No verification protocol. Output ends at "Write artifact." |
| C-15 | FAIL (0) | No inline notation mechanism; AF- slots are in the AF- section, not during extraction. |
| C-16 | PASS (2) | `Closure: Every entry from the prior AF- register appears above with a status. v` PRE-PRINTED in both AF- and SF- sections. Model cannot omit what it did not generate. |
| C-17 | FAIL (0) | No charter; no three-loop structure. |
| C-18 | FAIL (0) | No step-level cross-references. |
| C-19 | FAIL (0) | No verification table. |
| C-20 | FAIL (0) | No charter. |
| C-21 | FAIL (0) | No recursive meta-loop. |

**Decisive strength**: Pre-printed closure sentences are the most reliable C-16 mechanism outside of V-05. The model completes what already exists; it cannot omit the sentence by drift. C-13 slot structure likewise enforces A/B/Consequence without instruction.

**Decisive gap**: C-05 structural risk -- no lens extraction steps means all-four-lens coverage depends on model behavior, not prompt structure. This drops the essential total to 54.

---

### V-03 -- Discovery Questions (Questioning Phrasing)

**Score: 90 / 116 -- Weak***

| C | Rating | Evidence |
|---|--------|----------|
| C-01 | PASS (12) | "Before you start" section explicitly searches both directories; "if one is empty, say so." |
| C-02 | PASS (12) | Q1-Q4 map to Must/Should/Could/Won't tiers; assembled into MoSCoW table in final step. |
| C-03 | PASS (12) | Q5 asks "what single requirement, if absent, makes the most other requirements impossible?" + transitive chain format + "second-order chains required." |
| C-04 | PASS (12) | Q6 requires AF- with A/B/Consequence format; "zero AF- on complex input is a fail." |
| C-05 | PARTIAL (6) | Q1 prompts user and Architect perspectives explicitly; UX and Compliance implied via lens labels but have no dedicated extraction question. |
| C-06 | PASS (10) | Q8 lifecycle table with five phases; "for each SILENT phase, raise an SS- entry." |
| C-07 | PASS (10) | Q7 SF- section with gap/contradiction format. |
| C-08 | PARTIAL (5) | Stable IDs required per Q1; tier promotion notation ("Promoted R-NN") not explicitly stated; assembly section says "stable IDs" but no promotion note format. |
| C-09 | PASS (2) | Q5: "R-NN -> R-MM -> R-PP. Second-order chains are required." + explain foundational reasoning. |
| C-10 | PASS (2) | Q6: "Cite exact source text for each [AF- entry]." |
| C-11 | PASS (2) | Q8 lifecycle table with five named phases. |
| C-12 | PASS (2) | "If prior runs had open AF-/SF- entries, they must appear here with a status: open / resolved / out-of-scope." |
| C-13 | PASS (2) | Q6 AF- format: "what are the two most plausible interpretations?" + A/B/Consequence format. |
| C-14 | FAIL (0) | No verification protocol. Final step is "assemble output." |
| C-15 | FAIL (0) | No inline [AMBIG:] instruction during Q1-Q5. Ambiguity detection deferred to Q6. |
| C-16 | PARTIAL (1) | Q6 and Q7 both say "must appear here with a status" but no pre-printed closure sentence in the exact required format. |
| C-17 | FAIL (0) | No charter; no three-loop structure. |
| C-18 | FAIL (0) | No "Apply Law X here" cross-references. |
| C-19 | FAIL (0) | No verification table. |
| C-20 | FAIL (0) | No charter. |
| C-21 | FAIL (0) | No recursive meta-loop. |

**Decisive strength**: Discovery question framing primes gap-finding naturally. Q4 ("What are teams doing instead?") is the richest Won't Have framing in R1, grounding inertia without a dedicated lifecycle axis.

**Decisive gap**: C-05 and C-08 both PARTIAL. No explicit UX/Compliance extraction question; no tier promotion notation format.

---

### V-04 -- Lifecycle Emphasis + Inertia Framing

**Score: 101 / 116 -- Strong**

| C | Rating | Evidence |
|---|--------|----------|
| C-01 | PASS (12) | Step 0 searches both directories; SF-01 status keyed to trace find. |
| C-02 | PASS (12) | Step 2 consolidated MoSCoW table with four tiers and lifecycle Phase column. |
| C-03 | PASS (12) | Step 4 dependency graph: root blocker + foundational reason + transitive chains + inertia consequence note. |
| C-04 | PASS (12) | Step 5 AF- section with source + A/B/Consequence format; carry-forward required. |
| C-05 | PASS (12) | Steps 1-4 have four dedicated lens extraction sections (PM, Architect, UX, Compliance), each with per-phase table. |
| C-06 | PASS (10) | Step 3 lifecycle coverage audit with five phases; SILENT phases generate SS- entries by construction. |
| C-07 | PASS (10) | Step 6 SF- section with severity + affected R-IDs + status. |
| C-08 | PASS (10) | IDs continuous across lens steps; "Tier promotions: 'Promoted R-NN from [tier] to [tier]: [reason].'" |
| C-09 | PASS (2) | "Show transitive chains: R-NN -> R-MM -> R-PP." + inertia consequence note on root blocker. |
| C-10 | PASS (2) | Step 5 AF- format: `Source: "[exact quote from input spec]"`. |
| C-11 | PASS (2) | Step 3 lifecycle coverage audit names all five phases; SILENT = automatic SS-. Strongest C-11 enforcement in R1. |
| C-12 | PASS (2) | "Carry forward all open AF- and SF- entries with status: open / resolved / out-of-scope." Per-entry status in both sections. |
| C-13 | PASS (2) | Step 5 AF- format pre-prints Interpretation A / Interpretation B / Consequence. |
| C-14 | FAIL (0) | No verification protocol. Output ends at "Write artifact." |
| C-15 | FAIL (0) | No inline [AMBIG:] instruction during lens extraction steps. |
| C-16 | PARTIAL (1) | "All prior AF-/SF- entries must appear here with a status" present but no pre-printed closure sentence in the required exact format. |
| C-17 | FAIL (0) | No charter; no three-loop structure. |
| C-18 | FAIL (0) | No "Apply Law X here" cross-references. |
| C-19 | FAIL (0) | No verification table. |
| C-20 | FAIL (0) | No charter. |
| C-21 | FAIL (0) | No recursive meta-loop. |

**Decisive strength**: Lifecycle phase tagging on every requirement makes C-11 structurally infallible -- a phase with no requirements is a visible zero in the coverage table. Inertia framing enriches C-03 blocker reasoning with workaround cost.

**Decisive gap**: Identical aspirational ceiling to V-01 (11 pts). The lifecycle + inertia axes don't unlock C-14 through C-21.

**V-01 vs V-04 tie (101 each)**: V-04 has structurally stronger C-11 enforcement and richer C-03 reasoning. V-01 has simpler structure with lower compliance overhead. For R2, V-04's lifecycle tagging is the better structural base.

---

### V-05 -- Template + Three-Loop Enforcement

**Score: 115 / 116 -- Golden**

| C | Rating | Evidence |
|---|--------|----------|
| C-01 | PASS (12) | Step 0 searches both directories; "Never silently skip either directory." Verification table row C-01 audits this before artifact write. |
| C-02 | PASS (12) | Step 2 MoSCoW table with four tiers; verification table row C-02 confirms. |
| C-03 | PASS (12) | Step 3: "Name at least one root blocker. State WHY it is foundational -- not just that it blocks." Verification table row C-03. |
| C-04 | PASS (12) | Step 5 AF- mandatory entries; verification table row C-04. |
| C-05 | PASS (12) | Step 1 has four sub-sections (PM / Architect / UX / Compliance); verification table row C-05 with essential gate. |
| C-06 | PASS (10) | Step 4 lifecycle table with five phases; verification table row C-06. |
| C-07 | PASS (10) | Step 6 SF- section; verification table row C-07. |
| C-08 | PASS (10) | Stable IDs + tier promotions; verification table row C-08. |
| C-09 | PASS (2) | Step 3: "Show second-order chains: R-NN -> R-MM -> R-PP." Verification table row C-09. |
| C-10 | PASS (2) | AF- format: `Source: "[exact quote from input]"`. Verification table row C-10. |
| C-11 | PASS (2) | Step 4 five-phase lifecycle table. Verification table row C-11. |
| C-12 | PASS (2) | Law B ("Apply Law B here") at Steps 0, 5, 6; prior findings carried forward with status. Verification table row C-12. |
| C-13 | PASS (2) | [AMBIG:] notations from Steps 1/4 formalized in Step 5 with A/B/Consequence. Verification table row C-13. |
| C-14 | PASS (2) | CHARTER names "Loop 3 (verify): the pre-output verification protocol." PRE-OUTPUT VERIFICATION PROTOCOL is a named section with all 21 criteria by ID, PASS/FAIL rows before artifact write. Row C-14 is self-referential (audits its own presence). |
| C-15 | PASS (2) | CHARTER declares Format Law A: inline [AMBIG:] at first encounter during extraction. Step 1: "Apply Law A here" with full format reinstatement. Step 4 same. Step 5: "This section formalizes all [AMBIG:] notations from Steps 1 and 4. Do not introduce new ambiguities here for the first time." Verification table row C-15: "Were [AMBIG:] notations generated DURING extraction (Steps 1/4), not introduced fresh in Step 5?" |
| C-16 | PASS (2) | CHARTER declares Format Law B: exact closure sentence pre-specified. Steps 5 and 6 pre-print "Closure: Every entry from the prior open [AF-/SF-] register appears in this section with a status. v" Verification table row C-16. Three-loop enforcement: declare (charter) -> apply (Steps 5/6) -> verify (table). |
| C-17 | PASS (2) | CHARTER "Three-Loop Meta-Requirement": "Laws A and B are enforced via three loops simultaneously: Loop 1 (declare): this charter. Loop 2 (apply): step-level cross-references. Loop 3 (verify): the pre-output verification protocol." Verification table row C-17: "Are all three loops present?" |
| C-18 | PASS (2) | "Apply Law A here (Step 1)", "Apply Law B here (Step 0)", "Apply Law A here (Step 4)", "Apply Law A/B here (Steps 5/6)" -- explicit cross-references at every step that triggers a law. Verification table row C-18. |
| C-19 | PASS (2) | Verification table row C-15 audits whether [AMBIG:] notations were generated DURING extraction (process check, not output check). Row C-16 audits whether closure sentences were placed in each findings section. These are process-diagnostic rows. |
| C-20 | PASS (2) | CHARTER "Prevention-Detection Complementarity": "Loop 2 creates the execution artifacts -- inline [AMBIG:] notations and closure sentences -- that Loop 3 requires as evidence. Loop 2 prevents violations at extraction time. Loop 3 detects any violations that slipped through. The two layers are designed as a linked system: Loop 2's artifacts are Loop 3's evidence." |
| C-21 | PARTIAL (1) | Charter assigns Loop 1/2/3 by structural role (declare/apply/verify) and makes Loop 2 non-skippable: "Loop 2 is non-skippable. Loop 1 names Loop 2 as the apply layer. A model that satisfies Loop 1 while skipping Loop 2 contradicts this charter's structure." However, charter does not explicitly assign C-17 = Loop 1, C-18 = Loop 2, C-19 = Loop 3 by rubric criterion ID within the charter text. Correspondence is present structurally and visible in the verification table but not named in the charter itself. |

**Decisive strength**: V-05 is the only R1 variation to enforce C-14 through C-20 simultaneously. The three-loop pattern (declare -> apply -> verify) applied simultaneously to Laws A and B eliminates independent failure modes: if Law A is forgotten during extraction, step-level reinstatement catches it; if the step reinstatement is ignored, the verification table detects it. No single failure point can cause a miss.

**Decisive gap**: C-21 PARTIAL -- charter assigns loops by structural role but not by rubric criterion IDs within the charter text itself.

---

## Score Summary

| Variation | Essential | Recommended | Aspirational | **Total** | Band |
|-----------|-----------|-------------|--------------|-----------|------|
| V-05 Template + Three-Loop | 60 | 30 | 25 | **115** | Golden |
| V-01 Role Sequence | 60 | 30 | 11 | **101** | Strong |
| V-04 Lifecycle + Inertia | 60 | 30 | 11 | **101** | Strong |
| V-02 Template-Completion | 54 | 30 | 11 | **95** | Weak* |
| V-03 Discovery Questions | 54 | 25 | 11 | **90** | Weak* |

---

## Excellence Signals from V-05

Patterns from the top scorer not present in prior rounds:

1. **Prevention-detection complementarity as explicit design contract**: Loop 2 (step reinstatements) creates the execution artifacts -- [AMBIG:] notations and closure sentences -- that Loop 3 (verification table) requires as evidence. Charter names this relationship explicitly: "Loop 2's artifacts are Loop 3's evidence." Each loop layer cannot function without the prior layer's outputs. First appearance of this structural pattern.

2. **Three-loop enforcement applied simultaneously to multiple concurrent laws**: Laws A and B each get all three loops simultaneously, not sequentially. The charter declares both laws, each extraction step reinstates both applicable laws, the verification table has rows for both. No single-point failure can cause a miss on either law. R3 V-05 applied three loops to new criteria; R1 V-05 extends this to two concurrent laws with C-17-C-21 as the meta-criteria for the enforcement pattern itself.

3. **Recursive meta-loop: the enforcement mechanism is self-enforcing**: C-17 (three-loop declared in charter) / C-18 (applied at each step) / C-19 (verified in table) are themselves a declare/apply/verify triplet. The three-loop pattern enforces itself via the same three-loop pattern. Loop 2 is non-skippable by self-reference: Loop 1 (charter) names Loop 2 as the "apply layer," making skipping Loop 2 a logical contradiction of Loop 1.

---

## What R1 Confirmed

**C-16 PASS requires exact closure sentence format.** "Carry forward all prior runs" is insufficient -- only exact format or pre-printed sentence earns full credit. V-02 and V-05 achieve C-16 PASS; V-01/V-03/V-04 get PARTIAL.

**C-05 PARTIAL is the primary failure mode for V-02/V-03.** Template-completion and discovery-question formats both skip dedicated per-lens extraction steps. V-01 and V-04 demonstrate that explicit lens steps are the reliable mechanism for all-four-lens coverage.

**C-14 through C-21 form a coherent cluster that only V-05 addresses.** The cluster cannot be unlocked incrementally by single-axis targeting -- it requires the three-loop enforcement architecture as a system.

**V-04's lifecycle-by-construction is the strongest C-11 mechanism.** Phase tags on every requirement make silences structurally visible before the coverage audit runs. This should be preserved in any R2 base structure.

---

```json
{"top_score": 115, "all_essential_pass": true, "new_patterns": ["prevention-detection complementarity as explicit design contract: Loop 2 (step reinstatements) creates artifacts Loop 3 (verification table) requires as evidence -- charter names this relationship making it a structural dependency, not an emergent property", "three-loop enforcement applied simultaneously to multiple concurrent laws -- declare/apply/verify triplet for each law in parallel; eliminates independent failure modes across all constraints at once with no single-point failure", "recursive meta-loop: the enforcement mechanism is self-enforcing via the same three-loop pattern it describes -- C-17/C-18/C-19 are themselves declare/apply/verify of the meta-requirement, making Loop 2 non-skippable by self-reference from Loop 1"]}
```
