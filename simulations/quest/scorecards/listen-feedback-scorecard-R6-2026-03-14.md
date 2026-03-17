# /quest:score — listen-feedback R6 (v6 Rubric)

**Scoring order:** V-03 → V-01 → V-02 → V-04 → V-05 (adversarial axis first; compensation test last)

---

## V-03 — Soft synthesis phrasing

**Axis:** Phase 3 switches from imperative to guidance register ("The analysis phase synthesizes… begin with escalations… conclude with the theme matrix"). No preamble constraint. No structural nesting.

**Hypothesis under test:** Does guidance-register Phase 3 phrasing cause A-12 failure (UX-before-PM) while A-13 survives?

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | 12 personas, ascending NPS | PASS | Structural requirement unchanged from R5 V-05 baseline |
| C-02 | Card completeness | PASS | Card format block unchanged |
| C-03 | Aggregate NPS + threshold | PASS | Phase 1 aggregate logic unchanged |
| C-04 | NPS computed + threshold applied | PASS | Threshold check unchanged |
| C-05 | Theme matrix present | PASS | Phase 3 still names theme matrix |
| R-01 | Blocking items escalated | PASS | BLOCKING ITEMS section still named in Phase 3 |
| R-02 | PM and UX roles included | PASS | Both role reads still named in guidance |
| R-03 | Theme matrix severity distribution | PASS | Matrix format instruction unchanged |
| A-01 | Persona revision recs for NPS < 6 | PASS | Card format block unchanged |
| A-02 | NPS sensitivity analysis | PASS | Section still described in guidance |
| A-03 | Inline [BLOCKING] flags | PASS | Card format instruction unchanged |
| A-04 | Ascending-NPS ordering | PASS | Phase 1 ascending-order instruction unchanged |
| A-05 | Two-pass revision recs | PASS | Dual-placement instruction unchanged |
| A-06 | Inertia-baseline NPS justification | PASS | Status-quo comparison framing unchanged |
| A-07 | Severity-first within-card | PASS | "most severe first" instruction unchanged |
| A-08 | Band annotation + aggregate distribution | PASS | Band definitions + aggregate block unchanged |
| A-09 | Named `Current approach:` field | PASS | Card format unchanged |
| A-10 | `Dominant Detractor objection:` labeled field | PASS | Aggregate block instruction unchanged |
| A-11 | Card header id/name/role only | PASS | Card format unchanged |
| A-12 | UX READ precedes PM READ | **FAIL** | Guidance language — "synthesizes… begin with escalations…" — does not fix sequence. PM synthesis is the natural executive-summary default; model places PM READ first without explicit sequence lock. No preamble constraint present to override drift. |
| A-13 | Theme matrix as final synthesis section | PASS | "conclude with the theme matrix" retains unambiguous positional meaning even in descriptive register; no section mentioned after it. |

**Score:** 150 / 155 (A-12: −5)

---

## V-01 — Explicit synthesis-order constraint

**Axis:** Preamble block added before Phase 1 with exact Phase 3 section ordering (1–6) and explicit locks: "UX READ must appear before PM READ. These positions are fixed regardless of output length." No structural changes to prompt body.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-05 | All essential | PASS | Baseline structure unchanged |
| R-01–R-03 | All recommended | PASS | Baseline structure unchanged |
| A-01–A-11 | All prior aspirational | PASS | Baseline structure unchanged |
| A-12 | UX READ precedes PM READ | PASS | Preamble states "UX READ must appear before PM READ. These positions are fixed regardless of output length." Global pre-commitment before any phase begins; functions as a context-wide constraint rather than local Phase 3 instruction. |
| A-13 | Theme matrix as final synthesis section | PASS | Preamble states "THEME MATRIX is the terminal section: no substantive analysis appears after it." Phase 3 instruction echoes ("in order per the SYNTHESIS ORDER CONSTRAINT stated above"). Dual enforcement. |

**Score:** 155 / 155

---

## V-02 — Sensitivity analysis nested inside THEME MATRIX

**Axis:** NPS SENSITIVITY ANALYSIS moves from peer section (Phase 3 position 5) to a "Leverage" sub-section inside THEME MATRIX. Phase 3 reduces to 5 peer sections; THEME MATRIX is structurally last. A-02 content (2–3 leverage personas + ROI estimate) preserved inside the matrix block.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-05 | All essential | PASS | Baseline structure unchanged |
| R-01–R-03 | All recommended | PASS | Phase 3 peer structure: BLOCKING ITEMS → REVISION RECS → UX READ → PM READ → THEME MATRIX; R-01/R-02/R-03 all satisfied |
| A-01–A-11 | All prior aspirational | PASS | Card format and Phase 1/2 unchanged |
| A-02 | NPS sensitivity analysis | PASS | Content requirement ("identify 2–3 leverage personas; state highest-ROI change") is met inside THEME MATRIX. A-02 is a content criterion, not a section-boundary criterion. |
| A-12 | UX READ precedes PM READ | PASS | UX READ (peer section 3) still appears before PM READ (peer section 4). Nesting sensitivity analysis inside THEME MATRIX does not affect role-read ordering. |
| A-13 | Theme matrix as final synthesis section | PASS | By construction: sensitivity analysis is a sub-section inside THEME MATRIX, not a peer section appearing after it. Pass condition "no major analysis section appears after the theme matrix" is satisfied structurally — nothing follows the THEME MATRIX peer section. |

**Score:** 155 / 155

---

## V-04 — Combined (V-01 + V-02)

**Axis:** Preamble constraint from V-01 + nested sensitivity analysis from V-02. Double enforcement for both A-12 and A-13.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-05 | All essential | PASS | |
| R-01–R-03 | All recommended | PASS | |
| A-01–A-11 | All prior aspirational | PASS | |
| A-12 | UX READ precedes PM READ | PASS | Preamble constraint ("fixed regardless of output length") + Phase 3 peer ordering (UX at position 3, PM at position 4). Dual enforcement. |
| A-13 | Theme matrix as final synthesis section | PASS | Structural nesting from V-02 (terminal by construction) + preamble declaration ("THEME MATRIX is the terminal section") + Phase 3 "in order per constraint." Triple enforcement. |

**Score:** 155 / 155

---

## V-05 — Combined (V-01 + V-02 + V-03)

**Axis:** Compensation test — V-03 soft Phase 3 phrasing introduced alongside V-01 preamble constraint and V-02 nested structure. Does the preamble pre-commitment override soft local register for A-12?

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-05 | All essential | PASS | |
| R-01–R-03 | All recommended | PASS | |
| A-01–A-11 | All prior aspirational | PASS | |
| A-12 | UX READ precedes PM READ | PASS | Preamble states "UX READ must appear before PM READ. These positions are fixed regardless of output length." This is a global, pre-phase declaration processed before any Phase 3 guidance. V-03's soft Phase 3 phrasing does not name a sequence; it merely describes sections without ordering them. The preamble's explicit order-lock is the load-bearing constraint. V-03 alone scores 150 because it has no such lock; V-05 has the lock, so A-12 passes. |
| A-13 | Theme matrix as final synthesis section | PASS | Structural nesting (V-02) ensures terminal position by construction; preamble declaration and "conclude with" guidance provide two further layers. |

**Score:** 155 / 155

---

## Composite Scorecard

| Variation | Essential | Recommended | Aspirational A-01–A-11 | A-12 | A-13 | Total | Rank |
|-----------|-----------|-------------|------------------------|------|------|-------|------|
| V-01 | 60 | 30 | 55 | 5 | 5 | **155** | T-1 |
| V-02 | 60 | 30 | 55 | 5 | 5 | **155** | T-1 |
| V-03 | 60 | 30 | 55 | 0 | 5 | **150** | 5 |
| V-04 | 60 | 30 | 55 | 5 | 5 | **155** | T-1 |
| V-05 | 60 | 30 | 55 | 5 | 5 | **155** | T-1 |

---

## Excellence Signals

**From V-01/V-04/V-05 — Preamble pre-commitment as global ordering lock.** Stating ordering constraints before any phase begins creates a context-wide pre-commitment that persists through long outputs. Local Phase 3 instructions have shorter scope — they apply only within the phase and can be overridden by model defaults (PM-before-UX) when the generation is deep. The preamble constraint is processed first and operates as a global declaration; it cannot be overridden by local guidance-register phrasing.

**From V-02/V-04/V-05 — Structural nesting makes A-13 pass by construction.** Moving sensitivity analysis inside THEME MATRIX removes the possibility of A-13 failure: if the section containing the analysis is the same section as the matrix, nothing can appear "after" the matrix without also being after the analysis. Instruction-based approaches ("no section follows this one") can fail if the model places a closing remark or addendum; structural nesting makes it a physical impossibility.

**From V-03 vs. V-05 — Compensation test result.** The V-01 preamble constraint restores A-12 compliance even with V-03's soft Phase 3 phrasing. This confirms that preamble pre-commitments are the load-bearing mechanism for ordering reliability. Prompts that cannot be restructurally hardened (V-02 approach) can be hardened by preamble lock instead. The two techniques are independent and additive.

---

## New Patterns

None extracted. A-12 and A-13 were added to the rubric at the start of R6 and are validated by these scores. The compensation test (V-05) confirms the preamble pre-commitment pattern as a prompt-engineering reliability technique but does not reveal a new quality dimension in model output; it is a finding about prompt design, not output structure. Rubric remains at 13 aspirational criteria.

---

```json
{"top_score": 155, "all_essential_pass": true, "new_patterns": []}
```
