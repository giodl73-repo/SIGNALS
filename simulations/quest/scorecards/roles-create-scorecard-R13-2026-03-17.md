Now I have everything needed. Let me score all five variations.

---

## roles-create R13 — Scorecard

**Rubric:** v11 | **Date:** 2026-03-17
**Formula:** `(essential_passed × 12) + (recommended_passed × 15) + (aspirational_passed / 22 × 10)`
**Denominator note:** 22 aspirational criteria (C-08 to C-29); each failure costs 10/22 ≈ 0.4545 pts.

---

### Scoring Formula Verification

| Passes | Formula | Score |
|--------|---------|-------|
| 22/22 aspirational | 60 + 30 + 10.000 | 100.00 |
| 21/22 aspirational | 60 + 30 + 9.5454 | 99.55 |
| 20/22 aspirational | 60 + 30 + 9.0909 | 99.09 |
| 19/22 aspirational | 60 + 30 + 8.6364 | 98.64 |

---

### Essential Criteria — All Variations

All five variations are structural probes of the skill design (phases, gates, CONTRACT ordering). Behavioral/output logic is invariant across all variations.

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Role file written to correct path | PASS | PASS | PASS | PASS | PASS |
| C-02 | All required frontmatter fields present | PASS | PASS | PASS | PASS | PASS |
| C-03 | Mode detection routes correctly | PASS | PASS | PASS | PASS | PASS |
| C-04 | Frontmatter content is domain-specific | PASS | PASS | PASS | PASS | PASS |
| C-05 | Inertia-advocate surfaced when absent | PASS | PASS | PASS | PASS | PASS |

**Essential subtotal: 5/5 for all variations.**

---

### Recommended Criteria — All Variations

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Lens.verify questions sharp and actionable | PASS | PASS | PASS | PASS | PASS |
| C-07 | Body section includes domain specializations table | PASS | PASS | PASS | PASS | PASS |

**Recommended subtotal: 2/2 for all variations.**

---

### Aspirational Criteria — Per Variation

#### C-08 to C-24 (Structural foundations — all pass across all variations)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|-----------|------|------|------|------|------|-------|
| C-08 | Archetype calibrated to area tier pattern | PASS | PASS | PASS | PASS | PASS | Archetype logic unchanged |
| C-09 | Orientation register matches stated audience | PASS | PASS | PASS | PASS | PASS | FIELD-REGISTER intact in all |
| C-10 | Body table uses domain-named column headers | PASS | PASS | PASS | PASS | PASS | COLUMN-HEADER contract intact |
| C-11 | Inertia-advocate companion file generated when absent | PASS | PASS | PASS | PASS | PASS | Phase 2 logic unchanged |
| C-12 | Interactive mode holds for all inputs before writing | PASS | PASS | PASS | PASS | PASS | INTERACTIVE-HOLD intact |
| C-13 | Pre-write self-certification phase executed | PASS | PASS | PASS | PASS | PASS | Phase 5 present in all |
| C-14 | Malformed inputs routed before mode detection | PASS | PASS | PASS | PASS | PASS | Phase 0 / INPUT-ROUTING intact |
| C-15 | Audit checks distributed as in-phase gates | PASS | PASS | PASS | PASS | PASS | Gate 3a[B], 3b[C], etc. in all |
| C-16 | Audit obligations pre-declared before generation | PASS | PASS | PASS | PASS | PASS | AUDIT-CHECKLIST CONTRACT present |
| C-17 | Hard constraints extracted into named CONTRACT sections | PASS | PASS | PASS | PASS | PASS | 6 named CONTRACT blocks in all |
| C-18 | Declaration-to-gate traceability is bidirectional | PASS | PASS | PASS | PASS | PASS | [G],[H],[B],[C],[D],[E],[F] in gates ↔ checklist |
| C-19 | Content-producing phases are thin CONTRACT citations | PASS | PASS | PASS | PASS | PASS | Retry prose / openers are process instruction, not rule restatement |
| C-20 | AUDIT-CHECKLIST items are thin CONTRACT references | PASS | PASS | PASS | PASS | PASS | Checklist items name block + scope only |
| C-21 | Every phase-cited CONTRACT block has AUDIT-CHECKLIST item | PASS | PASS | PASS | PASS | PASS | Coverage complete in all |
| C-22 | AUDIT-CHECKLIST header declares its own format constraint | PASS | PASS | PASS | PASS | PASS | Meta-statement present in all |
| C-23 | Rule content quarantined to three canonical locations | PASS | PASS | PASS | PASS | PASS | Openers are process narrative — no rule content leaks |
| C-24 | Audit gate structural form is homogeneous | PASS | PASS | PASS | PASS | PASS | All inline annotation form across all phases |

---

#### C-25 to C-29 — Discrimination Zone

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| **C-25** | Phase bodies achieve minimum surface | **PASS** | **PASS** | **FAIL** | **FAIL** | **PASS** |
| **C-26** | CONTRACTS block ordering mirrors first-citation sequence | **PASS** | **FAIL** | **PASS** | **PASS** | **PASS** |
| **C-27** | Phase body opens with CONTRACT citation | **PASS** | **PASS** | **PASS** | **FAIL** | **PASS** |
| **C-28** | Correction/retry instructions in gate fail, not body | **PASS** | **PASS** | **FAIL** | **PASS** | **PASS** |
| **C-29** | Gate fail branches carry verdict tokens only | **FAIL** | **FAIL** | **FAIL** | **FAIL** | **PASS** |

**Evidence by criterion:**

**C-25:**
- V-03 FAIL — Phase bodies carry retry text after artifact reference (e.g., "re-run the gate before advancing to Phase 5"). Body exceeds citation + artifact minimum.
- V-04 FAIL — Phase bodies carry connector openers before the citation (e.g., "FRONTMATTER GENERATION -- all 12 frontmatter fields for `.craft/roles/{area}/{subrole}.md` are generated here."). Opener text expands surface beyond minimum.
- C-25 implies C-27 and C-28: a C-25 pass means both sub-types are absent.

**C-26:**
- V-02 FAIL — CONTRACTS block orders COLUMN-HEADER third, FIELD-REGISTER fourth. Phase 3 cites FIELD-REGISTER; Phase 4 cites COLUMN-HEADER. First-citation sequence requires FIELD-REGISTER before COLUMN-HEADER. The inversion breaks the self-indexing property.
- All others PASS — CONTRACT order: INPUT-ROUTING-RULES → INTERACTIVE-HOLD → FIELD-REGISTER → COLUMN-HEADER → INERTIA-ADVOCATE-TEMPLATE → AUDIT-CHECKLIST.

**C-27:**
- V-04 FAIL — Each content-producing phase body begins with a descriptive process-narrative opener before the CONTRACT citation: Phase 0 opens with "INPUT GUARD -- this phase runs before any routing decision.", Phase 3 opens with "FRONTMATTER GENERATION -- all 12 frontmatter fields for `.craft/roles/{area}/{subrole}.md` are generated here."
- V-03 PASS — Bodies open directly with CONTRACT citation; retry text follows the artifact reference (entry point is clean).

**C-28:**
- V-03 FAIL — Phase bodies contain fix-and-retry instructions in prose after the artifact reference ("re-run the gate before advancing"). Gate fail branches also carry correction text (C-29 fires independently). The two corruption locations are orthogonal.
- V-01, V-04 PASS — No retry prose in any phase body. Correction belongs to Phase 5 or gate fail branches only.

**C-29:**
- V-01 FAIL — Every gate carries a repair directive after the verdict token: "PASS / FAIL: Add missing fields before advancing." / "PASS / FAIL: Re-prompt the user for area and subrole before advancing." The FAIL branch is not verdict-only.
- V-02 FAIL — Same gate structure as V-01. Correction clauses present in all gate FAIL branches despite body being citation-only.
- V-03 FAIL — Gate FAIL branches carry correction text (e.g., "PASS / FAIL: Resolve remaining `{area}` slots and re-run the gate before advancing.") independent of C-28 body retry failure.
- V-04 FAIL — Gate FAIL branches carry correction text throughout (e.g., "PASS / FAIL: Add missing fields before advancing.").
- V-05 PASS — Every gate reads "PASS / FAIL" with no text following. No correction instruction, repair directive, or "before advancing" clause anywhere in the gate layer.

---

### Composite Scores

| ID | Essential (5×12) | Recommended (2×15) | Aspirational | Failures | Score | Rank |
|----|------------------|--------------------|--------------|----------|-------|------|
| **V-05** | 60 | 30 | 22/22 = 10.00 | — | **100.00** | **1** |
| **V-01** | 60 | 30 | 21/22 = 9.55 | C-29 | **99.55** | **2** |
| **V-02** | 60 | 30 | 20/22 = 9.09 | C-26, C-29 | **99.09** | **3** |
| **V-03** | 60 | 30 | 19/22 = 8.64 | C-25, C-28, C-29 | **98.64** | **4=** |
| **V-04** | 60 | 30 | 19/22 = 8.64 | C-25, C-27, C-29 | **98.64** | **4=** |

All scores match the variation design hypotheses exactly.

---

### Discrimination Findings

**V-01 key finding:** C-29 fires in isolation when the body is citation-only. Gate annotation surface is a completely independent inspection axis — a skill can satisfy C-25, C-27, and C-28 (body surface clean in all three dimensions) and still fail C-29 because the gate scaffolding carries correction text. The 1-deduction result at 99.55 confirms this is the highest-scoring failing variation in the full series.

**V-02 key finding:** C-29 and C-26 are orthogonal. CONTRACTS definition ordering and gate annotation discipline do not interact. Combined: exactly 2 deductions. No cascade, no implied failures between them.

**V-03 key finding:** C-28 and C-29 are orthogonal violation sites. Body retry prose (C-28) fires independently from gate FAIL correction clauses (C-29). Both can coexist without interaction. C-25 is implied by C-28 (body surface exceeds minimum). No cascade to C-19 or C-23 — retry text is process instruction, not rule restatement.

**V-04 key finding:** C-27 and C-29 are orthogonal. Phase body entry-point violations (opener before citation) and gate annotation violations (correction in FAIL branch) do not interact. C-25 is implied by C-27. C-28 passes cleanly despite C-29 failing — no retry text in body even though gates carry correction text.

**V-03 vs V-04 symmetry:** Both score 98.64 (19/22) with different violation sites. V-03 fails C-28 (body retry) but passes C-27 (clean entry); V-04 fails C-27 (opener) but passes C-28 (no body retry). Mirrors the R12 V-01/V-02 symmetry but at a lower band (98.64 vs 99.05 under v10). The rubric's deduction space has a symmetric tiling property: different violation locations can produce equal scores.

---

### Excellence Signals — V-05

1. **Verdict-only gate annotations.** Every gate reads exactly "PASS / FAIL" — no text follows the verdict tokens. Correction prose is structurally absent from the gate layer. Phase 5 is the universal repair loop by design, not by constraint.

2. **Citation-first phase bodies with no framing.** Every content-producing phase opens immediately with the CONTRACT citation. No descriptive phrase, no activity header, no connector prose precedes the citation within the body.

3. **Minimum surface throughout.** Every phase body is exactly one CONTRACT citation plus one artifact or action reference. No retry directives, no fix-and-continue loops, no expanded narrative about what the CONTRACT does.

4. **Canonical CONTRACT ordering.** CONTRACTS block follows first-citation sequence: INPUT-ROUTING-RULES (Phase 0) → INTERACTIVE-HOLD (Phase 1) → FIELD-REGISTER (Phase 3) → COLUMN-HEADER (Phase 4) → INERTIA-ADVOCATE-TEMPLATE (Phase 2) → AUDIT-CHECKLIST (pre-declared). Self-indexing: scanning CONTRACTS top-to-bottom encounters each definition at the point its first phase reference would be reached.

5. **Correction prose is nowhere.** C-25 + C-29 together mean there is no correction prose in any location — not in the body (C-25), not in the gate annotations (C-29). Phase 5 handles repair implicitly through the AUDIT-CHECKLIST re-run. V-05 is the sole form where repair is latent rather than explicit.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-29 fires in isolation when body surface is minimal: gate annotation is an independent inspection surface distinct from phase body, and a body-clean skill (C-25/C-27/C-28 all pass) can fail C-29 without any cascade", "V-03 and V-04 tie at 98.64 with different violation sites (C-28 vs C-27), confirming a symmetric tiling property in the deduction space: orthogonal violation locations at the same depth produce identical scores"]}
```
