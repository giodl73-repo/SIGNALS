Now I have full context. R3 all-100 baseline, R4 adds C-16 (run-scoped) and C-17 (first-rule at consumption) with aspirational denominator = 9. V-01 is provided; I need to write V-02–V-05 on the described axes, then score all five.

---

## Round 4 Scoring — mock-ns (Rubric v4)

**Date:** 2026-03-15
**Rubric:** v4 (C-01–C-17, aspirational denominator = 9)
**R4 baked-in:** V-04 named gates (-- S-N GATE --) + V-05 inertia framing in exclusion row and FIDELITY CONTEXT
**New targets:** C-16 (run-scoped at compute site) + C-17 (prohibition is first-stated rule at consumption)

---

### Variation Designs

All five variations carry the R4 baseline baked-in. The only axis varied is the S-4/A-1 enforcement language for C-16 and C-17.

---

**V-01 — RULE Labels + Exhaustive Path Enumeration** *(provided in prompt)*

Key S-4 language:
> RULE 1 of S-4: FLAG is final after this emit. MUST NOT be recomputed in any step, any conditional branch, any fallback path, any regeneration sequence, or any other execution context anywhere in this run — including paths that do not pass through prior steps in normal order.

Key A-1 language:
> RULE 1 of this step: Copy FLAG from S-4 verbatim. Do not re-derive it. This rule is first — it applies before any field is listed, before any category lookup, before any formatting instruction in this step. No instruction in A-1 precedes this rule.

---

**V-02 — Run-Scoped Gate Only (C-16 single-axis)**

Baked-in baseline. C-16 targeted; C-17 deliberately NOT prioritized — gate prohibition appears after field-listing instruction.

Key S-4 language:
> -- S-4 GATE -- FLAG IS FINAL. MUST NOT be recomputed anywhere in this run — not in any step, any conditional branch, any fallback path, or any regeneration sequence. STATUS: LOCKED. -- END S-4 GATE --

Key A-1 language:
> Write the following six-field block immediately after any frontmatter: [MOCK ARTIFACT -- NOT VERIFIED], Skill:, Topic:, Category:, Date:, Status:, Flag: ...
> -- A-1 GATE -- Copy FLAG verbatim from S-4. Do not re-derive it here. -- END A-1 GATE --

*(C-17 gap: prohibition in A-1 gate appears after the field-listing instruction, not before it.)*

---

**V-03 — First-Rule Priority Only (C-17 single-axis)**

Baked-in baseline. C-17 targeted; C-16 uses step-sequential language only.

Key S-4 language:
> -- S-4 GATE -- FLAG IS FINAL. MUST NOT modify FLAG in any subsequent step, including header assembly. Do not re-evaluate or re-derive FLAG after this emit. STATUS: LOCKED. -- END S-4 GATE --

Key A-1 language:
> The first rule of this step: Copy FLAG from S-4 verbatim. Do not re-derive it. This rule precedes all field-listing and formatting instructions in A-1. No other A-1 instruction is processed before this rule.
> [Then: six-field block]

*(C-16 gap: "any subsequent step" is step-sequential, not run-scoped — conditional branches and regeneration paths not covered.)*

---

**V-04 — Natural Combination (C-16 + C-17 without RULE labels)**

Baked-in baseline. Run-scoped language at compute site; explicit first-rule framing at consumption. No RULE-label numbering system — natural prose.

Key S-4 language:
> -- S-4 GATE -- FLAG IS FINAL. MUST NOT be recomputed anywhere in this run — not in any step, any conditional branch, any fallback path, or any regeneration sequence. STATUS: LOCKED. -- END S-4 GATE --

Key A-1 language:
> -- A-1 GATE -- The first rule of this step: Copy FLAG from S-4 verbatim. Do not re-derive it. This rule precedes all other A-1 instructions. -- END A-1 GATE --
> [Then: six-field block]

---

**V-05 — Full Synthesis (RULE labels + Gates + Inertia + Run-Scoped + First-Rule)**

Combines V-01's RULE-label register with V-04's gate fences and V-05's inertia framing. Every enforcement mechanism from R3–R4 appears simultaneously.

Key S-4 language:
> -- S-4 GATE --
> RULE 1: FLAG is resolved in this step and nowhere else.
> RULE 2: FLAG is final after the emit below. MUST NOT be recomputed anywhere in this run — not in any step, any conditional branch, any fallback path, any regeneration sequence, or any other execution context. Including paths that bypass normal step order.
> RULE 3: Do not proceed to A-1 without the `> FLAG:` emit present.
> STATUS: LOCKED after emit.
> -- END S-4 GATE --

Key A-1 language:
> -- A-1 GATE --
> RULE 1 of A-1 (processed first, before any field is listed): Copy FLAG from S-4 verbatim. Do not re-derive it. Inertia risk: re-deriving FLAG here produces a category mismatch that is invisible to downstream tooling and silently corrupts the artifact's trust tier.
> -- END A-1 GATE --
> [Then: six-field block]

---

### Scoring

**Criteria C-01–C-15: stable across all R4 variations** (all carry R4 baseline with full R3 coverage).

The only discriminators are **C-16** and **C-17**.

---

#### V-01 — RULE Labels + Exhaustive Path Enumeration

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|----------|
| C-01 | essential | PASS | Header block present with all seven fields including Flag |
| C-02 | essential | PASS | Category table correct; three-branch + compliance override |
| C-03 | essential | PASS | A-3 requires skill-specific headings and all structural elements |
| C-04 | essential | PASS | Flag in header; S-4 resolution logic covers all branches |
| C-05 | essential | PASS | `{namespace}` in filename; skill-id excluded |
| C-06 | recommended | PASS | Default table; topic → topic-plan (not topic-status) |
| C-07 | recommended | PASS | All three fidelity variants present; HIGH-STRUCTURE carries "REAL-REQUIRED at Tier 2+ for critical namespaces (trace, scout-feasibility, listen)" |
| C-08 | recommended | PASS | A-4 closing next-step line present |
| C-09 | aspirational | PASS | Critical-namespace tier branch in S-4 |
| C-10 | aspirational | PASS | Dedicated `> TOPICS.md: {...}` emit in S-1 |
| C-11 | aspirational | PASS | S-4 is a discrete named step; header references S-4 by step name |
| C-12 | aspirational | PASS | Three-column Exclusion table; "Do NOT use topic-status. Hard exclusion: meta-structural. Zero new signal, zero readiness advance." |
| C-13 | aspirational | PASS | A-2: "first section of the artifact body... delimited by `---` on both sides" |
| C-14 | aspirational | PASS | Compute site: RULE 1 of S-4 prohibits re-derivation. Header site: RULE 1 of A-1 prohibits re-derivation. Dual-site present. |
| C-15 | aspirational | PASS | Named Exclusion column; hard-constraint language in topic row |
| C-16 | aspirational | PASS | "MUST NOT be recomputed in any step, any conditional branch, any fallback path, any regeneration sequence, or any other execution context anywhere in this run — including paths that do not pass through prior steps in normal order." Run-scoped + exhaustive path enumeration. |
| C-17 | aspirational | PASS | "RULE 1 of this step: Copy FLAG from S-4 verbatim. Do not re-derive it. This rule is first — it applies before any field is listed, before any category lookup, before any formatting instruction in this step. No instruction in A-1 precedes this rule." Prohibition is the numbered RULE 1, declared first with explicit priority over all other A-1 instructions. |

**Essential:** 5/5 × 60 = **60**
**Recommended:** 3/3 × 30 = **30**
**Aspirational:** 9/9 × 10 = **10**
**Composite: 100**

---

#### V-02 — Run-Scoped Gate Only

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|----------|
| C-01–C-05 | essential | PASS (5/5) | Baseline carries all essentials |
| C-06–C-08 | recommended | PASS (3/3) | Baseline carries all recommended |
| C-09–C-15 | aspirational | PASS (7/7) | Stable from R3; baseline carries named gates and inertia framing |
| C-16 | aspirational | PASS | "MUST NOT be recomputed anywhere in this run — not in any step, any conditional branch, any fallback path, or any regeneration sequence." Run-scoped language explicit. |
| C-17 | aspirational | FAIL | A-1 gate prohibition appears *after* the six-field listing instruction. The first stated instruction of A-1 is "Write the following six-field block," not the prohibition. Prohibition is present (C-14 passes) but not first. |

**Essential:** 5/5 × 60 = **60**
**Recommended:** 3/3 × 30 = **30**
**Aspirational:** 8/9 × 10 = **8.89**
**Composite: 98.9**

---

#### V-03 — First-Rule Priority Only

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|----------|
| C-01–C-05 | essential | PASS (5/5) | Baseline |
| C-06–C-08 | recommended | PASS (3/3) | Baseline |
| C-09–C-15 | aspirational | PASS (7/7) | Baseline |
| C-16 | aspirational | FAIL | S-4 gate: "MUST NOT modify FLAG in any subsequent step, including header assembly." Step-sequential scoping — covers downstream steps in normal order but not conditional branches or regeneration paths that bypass step sequence. |
| C-17 | aspirational | PASS | "The first rule of this step: Copy FLAG from S-4 verbatim. Do not re-derive it. This rule precedes all field-listing and formatting instructions in A-1. No other A-1 instruction is processed before this rule." Explicit first-rule framing; prohibition precedes the six-field block. |

**Essential:** 5/5 × 60 = **60**
**Recommended:** 3/3 × 30 = **30**
**Aspirational:** 8/9 × 10 = **8.89**
**Composite: 98.9**

---

#### V-04 — Natural Combination

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|----------|
| C-01–C-05 | essential | PASS (5/5) | Baseline |
| C-06–C-08 | recommended | PASS (3/3) | Baseline |
| C-09–C-15 | aspirational | PASS (7/7) | Baseline |
| C-16 | aspirational | PASS | "MUST NOT be recomputed anywhere in this run — not in any step, any conditional branch, any fallback path, or any regeneration sequence." Run-scoped; identical coverage to V-02 compute site. |
| C-17 | aspirational | PASS | A-1 gate opens with: "The first rule of this step: Copy FLAG from S-4 verbatim. Do not re-derive it. This rule precedes all other A-1 instructions." Gate is structurally first; prohibition is first instruction within gate; six-field block follows. |

**Essential:** 5/5 × 60 = **60**
**Recommended:** 3/3 × 30 = **30**
**Aspirational:** 9/9 × 10 = **10**
**Composite: 100**

---

#### V-05 — Full Synthesis

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|----------|
| C-01–C-05 | essential | PASS (5/5) | Baseline |
| C-06–C-08 | recommended | PASS (3/3) | Baseline |
| C-09–C-15 | aspirational | PASS (7/7) | Baseline; inertia framing appears in both exclusion row and FIDELITY CONTEXT warnings |
| C-16 | aspirational | PASS | RULE 2 of S-4 gate: "MUST NOT be recomputed anywhere in this run — not in any step, any conditional branch, any fallback path, any regeneration sequence, or any other execution context. Including paths that bypass normal step order." Run-scoped + exhaustive enumeration. |
| C-17 | aspirational | PASS | A-1 gate opens with: "RULE 1 of A-1 (processed first, before any field is listed): Copy FLAG from S-4 verbatim. Do not re-derive it." Prohibition carries RULE 1 label with explicit "(processed first, before any field is listed)" parenthetical. |

**Essential:** 5/5 × 60 = **60**
**Recommended:** 3/3 × 30 = **30**
**Aspirational:** 9/9 × 10 = **10**
**Composite: 100**

---

### Summary Scorecard

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Band |
|------|-----------|-----------|-------------|--------------|-----------|------|
| 1 | V-01 RULE Labels + Exhaustive Paths | 5/5 (60) | 3/3 (30) | 9/9 (10) | **100** | Gold |
| 1 | V-04 Natural Combination | 5/5 (60) | 3/3 (30) | 9/9 (10) | **100** | Gold |
| 1 | V-05 Full Synthesis | 5/5 (60) | 3/3 (30) | 9/9 (10) | **100** | Gold |
| 4 | V-02 Run-Scoped Gate Only | 5/5 (60) | 3/3 (30) | 8/9 (8.89) | **98.9** | Gold |
| 4 | V-03 First-Rule Priority Only | 5/5 (60) | 3/3 (30) | 8/9 (8.89) | **98.9** | Gold |

**Round 4 verdict: three variations reach 100. The new C-16/C-17 criteria are jointly satisfiable. The single discriminator is whether BOTH run-scoped language and first-rule prioritization appear together — each alone scores 98.9.**

---

### C-16/C-17 as a Conjunction Requirement

| What's present | C-16 | C-17 | Score |
|----------------|------|------|-------|
| Run-scoped only (V-02) | PASS | FAIL | 98.9 |
| First-rule only (V-03) | FAIL | PASS | 98.9 |
| Both, natural prose (V-04) | PASS | PASS | 100 |
| Both, RULE labels (V-01) | PASS | PASS | 100 |
| Both + inertia on prohibition (V-05) | PASS | PASS | 100 |

The 1.1-point gap is structurally clean: **C-16 and C-17 are independent; each requires its own enforcement phrase; neither implies the other.** V-02 proves a run-scoped compute gate does not force first-rule at consumption. V-03 proves first-rule at consumption does not force run-scope at compute.

---

### Within the 100 Cluster

| Variation | C-16 mechanism | C-17 mechanism | Collapse risk |
|-----------|---------------|----------------|---------------|
| V-01 | Exhaustive path enumeration ("any conditional branch, any fallback path, any regeneration sequence...") | RULE 1 label + explicit "No instruction in A-1 precedes this rule" | Lowest — numbered rules create ordered processing; path list forecloses ambiguity about what "anywhere" means |
| V-04 | Bare run-scoped language ("anywhere in this run") | "The first rule of this step" inside gate | Low — gate structure enforces priority; "first rule" phrase is clear |
| V-05 | Exhaustive enumeration + RULE 2 inside gate | RULE 1 label + inertia risk note | Low — maximum mechanism stacking; inertia-risk note at consumption site adds consequence framing not present in V-01/V-04 |

**V-05 distinguisher** — the A-1 RULE 1 carries an inertia-risk parenthetical: "Inertia risk: re-deriving FLAG here produces a category mismatch that is invisible to downstream tooling and silently corrupts the artifact's trust tier." This converts the prohibition from syntactic instruction to consequence-grounded rule — the same pattern that made V-05's exclusion row superior in R3.

---

### Excellence Signals

**S-1 — Exhaustive path enumeration closes C-16 more tightly than bare "anywhere"**
V-01 and V-05 both name the specific paths covered: "any step, any conditional branch, any fallback path, any regeneration sequence, or any other execution context." The enumeration makes "anywhere in this run" concrete and non-deniable — a model cannot reason that its execution context is unlisted because the list ends with "any other execution context." V-02 and V-04's bare "anywhere in this run" satisfy C-16 but leave the interpretation of "anywhere" as a model inference; V-01/V-05 remove that inference.

**S-2 — Inertia-risk note at the consumption site converts prohibition into consequence rule**
V-05's A-1 RULE 1 includes: "Inertia risk: re-deriving FLAG here produces a category mismatch that is invisible to downstream tooling and silently corrupts the artifact's trust tier." This grounds the prohibition in system consequences rather than syntactic rule. The same consequence-grounding pattern appeared in V-05 R3 for the exclusion row — it now extends to the enforcement site, making both sites consequence-driven rather than rule-driven.

**R5 candidate:** V-01's exhaustive path enumeration merged with V-05's inertia-risk note at the consumption site. The two signals are orthogonal and jointly available — no architectural tension. The combination would produce a variation where C-16 is closed by explicit path enumeration AND C-17 is closed by consequence-grounded first-rule framing. Risk is prompt length; editorial compression preserving both patterns is the natural R5 task.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Exhaustive path enumeration at compute site closes C-16 more tightly than bare run-scoped language by naming every execution context including conditional branches and regeneration paths that bypass normal step order", "Inertia-risk note at the FLAG consumption site converts the first-rule prohibition from a syntactic instruction into a consequence-grounded rule — category mismatch invisible to downstream tooling is the named cost"]}
```
