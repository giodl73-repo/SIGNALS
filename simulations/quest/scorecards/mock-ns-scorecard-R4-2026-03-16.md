I now have everything needed. Let me score all 5 variations from the v2 file against the mock-ns rubric v4 (18 criteria: C-01–C-18).

---

## Scorecard: mock-ns Round 4 (v2) — C-17 + C-18 Targeting

**Rubric**: v4 | 5 essential (10 pts) + 3 recommended (10 pts) + 10 aspirational (2 pts) = 100 max

**Baseline note**: V-01 through V-04 share identical S-1–A-5 structure. Only S-0 varies. V-05 is fully convergent with enhanced lookups throughout.

---

### Shared Criteria Analysis (V-01 through V-04)

All four share the following S-0 components:
- CONSTRAINT: `No skill selection. No category lookup. No mock generation.` (3-op enumeration)
- 4-row FLAG table with `trace-*`, `scout-feasibility`, `listen-*` in condition column cell
- Per-field resolution bullets
- Compliance override block in S-3
- A-1 through A-5 labeled assembly steps
- Error-stop on unrecognized skill-id in S-2

| Criterion | Shared Grade | Evidence |
|-----------|-------------|---------|
| C-01 | PASS | A-1: skill, topic, category, date, status, flag — all 6 present |
| C-02 | PASS | S-2 three-group table matches registry exactly |
| C-03 | PASS | S-3 4-row table + compliance override; flag verbatim copy enforced |
| C-04 | PASS | A-2 has all three category-matched fidelity warnings |
| C-05 | PASS | A-3 instructs golden structural pattern; "body alone must identify skill" stated |
| C-06 | PASS | S-0 emits TOPICS.md status line; S-1 emits "Generating mock for..." line; both present |
| C-07 | PASS | A-4 path uses namespace (not skill-id); "Artifact written" emitted |
| C-08 | PASS | A-5 "Next: /mock:review..." is final artifact line; exception clause present |
| C-09 | PASS | S-1 table: `topic -> topic-plan (NEVER topic-status -- excluded as meta-structural)` |
| C-10 | PASS | S-3 compliance override: "If compliance tags present AND skill is scout-compliance or trace-permissions" |
| C-11 | PASS | FLAG condition row 3 names `trace-*`, `scout-feasibility`, `listen-*` explicitly; all 5 logical paths covered (cases 1+2 merged in "all other cases" — but critical namespaces enumerated, satisfying naming requirement) |
| C-12 | PASS | S-0 is structurally separate; CONSTRAINT enforces no skill selection until status line emitted |
| C-13 | PASS | S-2: "emit an error naming the unrecognized skill-id and stop. Do not assign a fallback category." |
| C-14 | PASS | A-1 (header), A-2 (fidelity warning), A-3 (body), A-4 (write), A-5 (next-step) — 5 labeled steps |
| C-15 | PASS | CONSTRAINT names 3 op types: skill selection, category lookup, mock generation |
| C-16 | PASS | FLAG row 3 condition cell: `skill-id matches trace-*, scout-feasibility, or listen-*` — in the cell, not footnote |

**Shared subtotal** (before C-17/C-18): 50 + 30 + 16 = **96 pts**

---

### V-01 — Lifecycle Emphasis: Terminal Gate (C-17 isolated, C-18 deliberate fail)

**S-0 delta**: tier bullet carries "into S-3" only; terminal sentence "Do not begin S-1 until this line is emitted."

| Criterion | Grade | Evidence |
|-----------|-------|---------|
| C-17 | PASS | "Do not begin S-1 until this line is emitted." — terminal sentence outside resolution bullets; names S-1 explicitly; emit line is the precondition |
| C-18 | FAIL | "Carry resolved tier into S-3 for flag computation." — only one consumer (S-3); C-18 requires at least two named consumers (S-2 and S-3) |

**V-01 Score: 96 + 2 + 0 = 98**  
Hypothesis confirmed: C-17 terminal gate passes; single-consumer carry fails C-18.

---

### V-02 — Role Sequence: Named-Consumer Carry (C-18 isolated, C-17 deliberate fail)

**S-0 delta**: standard tier bullet (no downstream clause); terminal "Carry the resolved tier into S-2 and S-3." No standalone gate sentence naming S-1.

| Criterion | Grade | Evidence |
|-----------|-------|---------|
| C-17 | FAIL | CONSTRAINT names operations ("skill selection, category lookup") not S-1 as a step; no standalone gate sentence naming S-1 specifically — CONSTRAINT-only does not satisfy C-17 per rubric |
| C-18 | PASS | "Carry the resolved tier into S-2 and S-3." — standalone terminal sentence; names S-2 and S-3 as consumers; handoff is inspectable |

**V-02 Score: 96 + 0 + 2 = 98**  
Hypothesis confirmed: named-consumer carry satisfies C-18; CONSTRAINT-only fails C-17.

---

### V-03 — Phrasing Register: CONSTRAINT-Embedded S-1 Name (C-17 form test, C-18 deliberate fail)

**S-0 delta**: CONSTRAINT rewritten to name steps: `Do not begin S-1, S-2, or S-3 until after the TOPICS.md status line below has been emitted.` Tier bullet: "Carry resolved tier forward." (no consumers named).

| Criterion | Grade | Evidence |
|-----------|-------|---------|
| C-17 | PASS | CONSTRAINT sentence "Do not begin S-1, S-2, or S-3 until after the TOPICS.md status line below has been emitted" — names S-1 explicitly and makes emit line the precondition; satisfies content requirement ("any phrasing that names the prohibited next step and makes the emit line a required precondition"); CONSTRAINT block is within S-0 step body |
| C-18 | FAIL | "Carry resolved tier forward." — no downstream consumers named; C-18 requires explicit consumer labeling |

**V-03 Score: 96 + 2 + 0 = 98**  
C-17 form test result: CONSTRAINT-embedded S-1 naming SATISFIES C-17. The pass condition is content-based, not form-based — the CONSTRAINT block within S-0 body qualifies.

---

### V-04 — Combined: C-17 + C-18 (the v4 Target)

**S-0 delta**: V-01 terminal gate + V-02 named-consumer carry, both present. Tier resolution bullet: "Carry resolved tier into S-2 and S-3." Terminal: "Do not begin S-1 until this line is emitted."

| Criterion | Grade | Evidence |
|-----------|-------|---------|
| C-17 | PASS | "Do not begin S-1 until this line is emitted." — terminal gate sentence naming S-1; emit line is precondition |
| C-18 | PASS | "Carry resolved tier into S-2 and S-3." — inline in tier resolution bullet; names both S-2 and S-3 as consumers; handoff contract explicit and inspectable |

**V-04 Score: 96 + 2 + 2 = 100**  
Both criteria satisfied simultaneously. No interaction effects between the two additions. Minimal structural change from V-01 (one bullet clause updated).

---

### V-05 — Convergent: All Excellence Signals at Maximum Strength

**S-0 delta**: 4-op CONSTRAINT (adds "No body generation") + pre-step sentence "Before any other step begins, emit the TOPICS.md status line below." + tabular resolution with Downstream-use column showing "Carry into S-2 and S-3" + terminal "Do not begin S-1 until this line is emitted." + standalone "Carry the resolved tier into S-2 and S-3."

**S-1**: tabular namespace defaults | **S-2**: tabular category lookup | **S-3**: 5-row FLAG table (critical tier=1 explicitly separated)

| Criterion | Grade | Evidence |
|-----------|-------|---------|
| C-01 | PASS | Same — all 6 fields present |
| C-02 | PASS | Tabular lookup in S-2 — more scannable than prose list |
| C-03 | PASS | 5-row FLAG table with full compliance override; "FLAG is now resolved. Do not recompute." |
| C-04 | PASS | Enhanced MIXED warning names specific claim types (competitor names, market data); all 3 categories present |
| C-05 | PASS | A-3 bullet structure specifies all required body elements |
| C-06 | PASS | Both emit lines present |
| C-07 | PASS | A-4 namespace-based path, "Artifact written" emitted |
| C-08 | PASS | A-5 last-line with exception clause |
| C-09 | PASS | Tabular S-1: "NEVER topic-status (excluded: meta-structural)" |
| C-10 | PASS | S-3 compliance override present |
| C-11 | PASS | 5-row FLAG table: critical tier >= 2 AND critical tier = 1 rows explicitly separated — all 5 combinations unambiguously covered |
| C-12 | PASS | S-0 separate step; 4-op CONSTRAINT |
| C-13 | PASS | S-2: error "names the unrecognized skill-id and points to the registry" — points to registry is the enhanced form |
| C-14 | PASS | A-1 through A-5 labeled |
| C-15 | PASS | 4-op CONSTRAINT: skill selection, category lookup, mock generation, body generation |
| C-16 | PASS | FLAG table condition cell row 3: `skill-id matches trace-*, scout-feasibility, or listen-*` |
| C-17 | PASS | DUAL: "Before any other step begins, emit the TOPICS.md status line below." (pre-step form) PLUS "Do not begin S-1 until this line is emitted." (named-S-1 form) — belt-and-suspenders |
| C-18 | PASS | DUAL: tabular Downstream-use cell "Carry into S-2 and S-3" PLUS standalone "Carry the resolved tier into S-2 and S-3." — belt-and-suspenders |

**V-05 Score: 50 + 30 + 20 = 100**  
First convergent to include all C-17/C-18 signals with full R1–R4 heritage. Dual-form coverage for both new criteria eliminates all known failure modes.

---

## Rankings

| Rank | Variation | Score | Key differentiator |
|------|-----------|-------|-------------------|
| 1 (tie) | V-04 | 100 | Minimal two-sentence S-0 closure; C-17 + C-18 both satisfied |
| 1 (tie) | V-05 | 100 | Belt-and-suspenders on all axes; 5-row FLAG table; registry-pointer in C-13 |
| 3 (tie) | V-01 | 98 | C-17 PASS via terminal gate; C-18 FAIL (single consumer) |
| 3 (tie) | V-02 | 98 | C-18 PASS via named-consumer carry; C-17 FAIL (CONSTRAINT-only) |
| 3 (tie) | V-03 | 98 | C-17 PASS (CONSTRAINT-embedded form passes); C-18 FAIL (unnamed carry) |

---

## Excellence Signals from Top-Scoring Variations

**From V-04** (minimal combination):
1. **Two-sentence S-0 closure is additive with no interaction**: the terminal gate (`Do not begin S-1 until this line is emitted.`) and the named-consumer carry (`Carry resolved tier into S-2 and S-3.` inline in tier bullet) coexist in S-0 without conflict. One sentence closes C-17; one clause closes C-18.
2. **Named-consumer carry in the resolution bullet itself satisfies C-18**: embedding "into S-2 and S-3" directly in the tier bullet (not a standalone sentence) is sufficient — the contract is explicit and inspectable at the consumption-site.

**From V-05** (convergent):
3. **Dual gate form provides redundant C-17 coverage**: "Before any other step begins" (pre-step pre-empt) plus "Do not begin S-1 until this line is emitted" (named-S-1 terminal) together cover both listed equivalent forms from the rubric simultaneously.
4. **5-row FLAG table makes C-11 unambiguous**: explicitly separating `critical AND tier = 1` from `critical AND tier >= 2` removes the "all other cases" fallback for critical skills — every case has a named row.

---

## C-17 Form Test Result (V-03 discriminator)

**CONSTRAINT-embedded S-1 naming satisfies C-17.** The pass condition is content-based ("any phrasing that names the prohibited next step and makes the emit line a required precondition") — it does not require a standalone sentence outside the CONSTRAINT block. V-03 confirms that both forms (standalone terminal sentence in V-01/V-04 and CONSTRAINT-embedded step list in V-03) satisfy the rubric.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Two-sentence S-0 closure: terminal gate naming S-1 (C-17) plus tier-carry naming S-2 and S-3 inline in resolution bullet (C-18) are fully additive with no interaction effects -- the minimal v4 target is achieved by exactly two sentence-level additions", "CONSTRAINT-embedded S-1 naming satisfies C-17: the pass condition is content-based not form-based -- naming S-1 inside the CONSTRAINT block within S-0 qualifies; standalone terminal sentence and CONSTRAINT-embedded form are equivalent for C-17 purposes"]}
```
ng satisfies C-17 but not C-15; op-naming satisfies C-15 but not C-17 (unless combined with a standalone gate sentence).

**V-04 is the optimal minimum**
> Two sentence additions to S-0 (gate sentence + named-consumer carry) close both C-17 and C-18 without structural changes. V-05 adds belt-and-suspenders but achieves the same score. The optimal minimal form is V-04.

---

### Failure Traps to Add to Rubric

| Trap | Criterion | Pattern |
|------|-----------|---------|
| CONSTRAINT step-prohibition loses op-type naming | C-15 | Rewriting CONSTRAINT to "Do not begin S-1, S-2, or S-3" satisfies C-17 (names S-1) but fails C-15 (no skill-selection op type named). Cannot substitute step names for operation types in the C-15 CONSTRAINT. |
| Single-consumer carry | C-18 | "Carry into S-3" (1 consumer) fails. Must name ≥2 downstream steps. Even a gate sentence + single-consumer carry leaves C-18 unaddressed. |

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-17 is content-based not form-based: CONSTRAINT-embedded sentence naming S-1 satisfies C-17 if it names S-1 and makes the emit a precondition", "CONSTRAINT step-prohibition trap: rewriting CONSTRAINT to name steps (Do not begin S-1) gains C-17 but loses C-15 op-type naming — the two criteria require separate sentences", "V-04 is the optimal minimum: two sentence additions to S-0 close both C-17 and C-18 with no structural changes — V-05 belt-and-suspenders adds robustness but no score gain"]}
```
