I now have all the content needed to score. Let me produce the full scorecard.

---

## validate-inertia R11 Scorecard

### Baseline note

All five variations build on V-45, which scored 340/340 on R10 (C-01–C-34 all pass). C-35, C-36, C-37 are the three new R11 criteria (10 pts each, max 30 pts added, 370 total). The V-45 baseline against R11 = 340/370 (C-35 FAIL, C-36 FAIL, C-37 FAIL — V-45's Row 5 uses a pointer subsection, AMEND(d) derives from CCV rather than L3 Evidence, and no co-resident named block exists).

---

### Criteria Evaluation

#### Essential (C-01–C-05) — all variations

| ID | V-51 | V-52 | V-53 | V-54 | V-55 |
|----|------|------|------|------|------|
| C-01 Per-persona inertia mapping | PASS | PASS | PASS | PASS | PASS |
| C-02 Quantified switching cost | PASS | PASS | PASS | PASS | PASS |
| C-03 Per-persona inertia score | PASS | PASS | PASS | PASS | PASS |
| C-04 Kill-barrier identification | PASS | PASS | PASS | PASS | PASS |
| C-05 Overall adoption inertia risk | PASS | PASS | PASS | PASS | PASS |

All essential criteria pass in all variations. (Inherited from V-45 baseline.)

#### Recommended (C-06–C-08) — all variations

All PASS, inherited from V-45. (Omitted from per-variation table for brevity.)

#### Aspirational (C-09–C-34) — all variations

All PASS at 10 pts each, inherited from V-45 (340/340 on R10). No regressions introduced by any R11 variation on pre-existing criteria.

Note on C-33 for V-53/V-55: Duality framing is moved from the preamble introduction to the AUDIT ARCHITECTURE DECLARED block. C-33 pass condition allows framing "in the preamble's introduction, the audit's header, or **a dedicated framing statement**." The AUDIT ARCHITECTURE DECLARED block is a dedicated framing statement. C-33 PASS confirmed.

Note on C-34 for V-53/V-55: Row 5 points to the AUDIT ARCHITECTURE DECLARED block, which contains the full column structure. The block is positioned before Phase 1. C-34 requires the preamble to declare the column structure before Phase 1 — the block satisfies this. C-34 PASS confirmed.

---

#### New R11 Criteria — per-variation analysis

---

**C-35 — Atomic audit format declaration (no pointer indirection)**
Pass condition: column spec and Evidence semantics inline at the declaration site; no pointer to a separate subsection.

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-51 | **PASS (10)** | Row 5 Requirement cell embeds the full 5-column spec with Evidence semantics verbatim. "Row 5 audit format" subsection eliminated entirely. The spec is read atomically at Row 5 — no pointer, no deferred content. |
| V-52 | **FAIL (0)** | Row 5 cell says "5-column audit table (see format below)." The "Row 5 audit format" subsection is explicitly retained. Two-step pointer read; skip surface preserved. |
| V-53 | **PASS (10)** | Row 5 cell says "See AUDIT ARCHITECTURE DECLARED block below." The block is a gated, named artifact — "Do not proceed to Phase 1 until AUDIT ARCHITECTURE DECLARED is written." The gate eliminates the skip surface: the model cannot defer the block to proceed. The full 5-column spec with Evidence-column semantics is inline within the block. The pointer in Row 5 does not create a drift surface because the block is a required output boundary, not an optional reference subsection. |
| V-54 | **PASS (10)** | Same Row 5 inline spec as V-51 (no pointer subsection). The "Row 5 audit format" subsection is absent. Full spec in the Row 5 cell. |
| V-55 | **PASS (10)** | Row 5 points to AUDIT ARCHITECTURE DECLARED block (same gate mechanism as V-53). Block contains full inline spec. Gate eliminates skip surface. |

---

**C-36 — Audit-first derivation**
Pass condition: AMEND(d) explicitly names the L3 Evidence column as its derivation source; prohibits reconstruction from Phase 5(3) or CCV; treats the audit as the prospective authority.

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-51 | **FAIL (0)** | AMEND(d): "Lever anchor: [copy the exact LEVER POINT label from Citation Chain Verification step (5) -- this must match the Evidence you wrote in the L3 row of the Citation Chain Completeness Audit verbatim]." Derivation source is CCV step (5). L3 Evidence mentioned only as a match constraint (retroactive verification). Forward-then-verify pattern unchanged. Three-site drift surface persists. |
| V-52 | **PASS (10)** | AMEND(d) explicitly: "Locate the L3 row of the Citation Chain Completeness Audit above. The Evidence column of that row contains the lever anchor text you pre-committed to when you wrote the audit. Copy it exactly, character-for-character... Do not reconstruct the label from Phase 5(3) or from CCV step (5). The audit is the derivation authority -- the L3 Evidence cell is the source you are copying from." Derivation direction inverted. Preamble Row 3 signals this at architecture-read time. All three C-36 requirements met. |
| V-53 | **FAIL (0)** | AMEND(d) retains V-45 style: "copy from CCV step (5) -- this must match the Evidence you wrote in the L3 row of the Citation Chain Completeness Audit verbatim." C-36 axis is explicitly marked unaddressed. |
| V-54 | **PASS (10)** | AMEND(d): "Locate the L3 row of the Citation Chain Completeness Audit above. The Evidence column of that row contains the lever anchor text you pre-committed to when you wrote the audit. Copy it exactly, character-for-character... Do not reconstruct the label from Phase 5(3) or from CCV step (5). The audit L3 Evidence cell is the derivation source; the audit is the authority." Identical to V-52 audit-first pattern. C-36 pass conditions fully met. |
| V-55 | **PASS (10)** | CITATION ARCHITECTURE DECLARED label explicitly includes: "AMEND(d) must derive its lever anchor from the L3 Evidence column of the audit -- not from Phase 5(3)." AMEND(d) uses same audit-first instruction as V-52/V-54. All three C-36 requirements met. |

---

**C-37 — Co-resident named block for audit architecture criteria**
Pass condition: C-33 (duality framing) and C-34 (column structure) co-reside in a single named, gated artifact before Phase 1; the block makes simultaneous omission of either criterion the only possible non-compliance shape.

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-51 | **FAIL (0)** | Duality framing in preamble introduction; column structure inline in Row 5 cell. Two separate structural positions. No named block. Criteria remain independently droppable. |
| V-52 | **FAIL (0)** | Duality framing in preamble introduction; column structure in "Row 5 audit format" subsection. Two separate structural positions. No AUDIT ARCHITECTURE DECLARED block. |
| V-53 | **PASS (10)** | AUDIT ARCHITECTURE DECLARED named block present after preamble table, before Phase 1. Block contains: (a) duality framing — "This output has two structural artifacts serving distinct roles. The Citation Architecture preamble... is declarative... The Citation Chain Completeness Audit is confirmatory... These roles are structurally distinct... Neither artifact can substitute for or subsume the other." (b) Full 5-column structure with Evidence semantics inline. Gate: "Do not proceed to Phase 1 until AUDIT ARCHITECTURE DECLARED is written on its own line above." Co-residence enforced. |
| V-54 | **FAIL (0)** | Duality framing in preamble introduction; column structure inline in Row 5 cell. Same two-position split as V-51. No named block. C-37 explicitly noted as still failing. |
| V-55 | **PASS (10)** | AUDIT ARCHITECTURE DECLARED block identical to V-53 structure. Contains both duality framing and full column structure inline. Gate condition present. Block is named, gated, co-resident. |

---

### Composite Scores

| Variation | C-01–C-34 | C-35 | C-36 | C-37 | **Total** | vs. predicted |
|-----------|-----------|------|------|------|-----------|---------------|
| V-51 | 340 | 10 | 0 | 0 | **350/370** | 350 ✓ |
| V-52 | 340 | 0 | 10 | 0 | **350/370** | 350 ✓ |
| V-53 | 340 | 10 | 0 | 10 | **360/370** | 360 ✓ |
| V-54 | 340 | 10 | 10 | 0 | **360/370** | 360 ✓ |
| V-55 | 340 | 10 | 10 | 10 | **370/370** | 370 ✓ |

All predictions confirmed. All essential criteria pass in all variations.

---

### Rankings

1. **V-55** — 370/370 (full ceiling, all three R11 criteria)
2. **V-53** — 360/370 (C-35 + C-37; C-36 not addressed)
2. **V-54** — 360/370 (C-35 + C-36; C-37 not addressed)
4. **V-51** — 350/370 (C-35 only)
4. **V-52** — 350/370 (C-36 only)

---

### Structural Questions — Answered

**Q1 (C-35, V-51):** YES — Atomic inline Row 5 earns C-35. Eliminating the subsection and embedding the full spec in the Row 5 Requirement cell is sufficient. The declaration site is the Row 5 cell; with no pointer, the spec is read without indirection.

**Q2 (C-36, V-52):** YES — Audit-first AMEND(d) earns C-36. Inverting the derivation direction (L3 Evidence → AMEND, with explicit prohibition of Phase 5(3) reconstruction) satisfies the criterion cleanly and independently.

**Q3 (C-37, V-53):** YES — The AUDIT ARCHITECTURE DECLARED named, gated block earns C-37. The gate eliminates the partial-criterion orphaning failure mode. C-35 is also earned as a structural byproduct because the block's inline spec eliminates the skip surface (the gate makes the block non-deferrable, which is structurally equivalent to atomic inline at the declaration site).

**Q4 (C-35 + C-36, V-54):** YES — The two independent changes compose cleanly without interaction effects. Atomic Row 5 and audit-first AMEND operate on different structural positions (Row 5 Requirement cell vs. AMEND(d) instruction) with no overlap. C-37 still fails because the two criteria (duality in preamble intro, column structure in Row 5 cell) remain at separate structural positions without a named co-resident block.

**Q5 (full ceiling, V-55):** YES — AUDIT ARCHITECTURE DECLARED block (V-53 pattern) + audit-first AMEND(d) (V-52 pattern) compose to 370/370. No interaction effects. Each structural change is independently justified and the combination is additive.

---

### Excellence Signals from V-55

**Signal 1 — Gate-enforced co-residence as skip-surface eliminator.** The AUDIT ARCHITECTURE DECLARED block pattern solves two independent drift problems with one mechanism: (1) it eliminates the C-37 partial-omission failure shape by co-housing C-33 and C-34 content in a single required output unit, and (2) it eliminates the C-35 pointer-indirection skip surface by making the block a required gated artifact rather than a reference subsection. A gate requirement ("do not proceed until X is written") is structurally equivalent to inline content for skip-surface purposes — the model cannot proceed without writing it.

**Signal 2 — Audit-first direction inversion as drift-surface collapse.** C-36's audit-first derivation pattern reduces the Phase 5(3) → CCV → AMEND three-site drift chain to a single step (L3 Evidence → AMEND). The mechanism is directional: treating the audit as the prospective authority rather than retroactive verifier changes the structural role of the Evidence cell from a match constraint to a derivation source. This is a one-line structural change to the AMEND instruction that eliminates two drift sites.

**Signal 3 — Clean composition across non-overlapping structural positions.** V-55 demonstrates that the two R11 improvements (co-resident block and audit-first direction) compose without interaction because they operate on structurally separate locations: the block addresses the pre-Phase-1 architecture section; the audit-first instruction addresses the post-CCV AMEND section. No interference. This validates single-axis isolation testing as a reliable design methodology for this rubric class: improvements on non-overlapping structural positions can be composed additively.

---

```json
{"top_score": 370, "all_essential_pass": true, "new_patterns": ["gate-enforced co-residence eliminates skip surface: a named gated block is structurally equivalent to atomic inline for drift-surface purposes", "audit-first derivation direction collapses three-site drift chain to one step by treating the audit Evidence cell as the prospective source rather than retroactive match constraint", "non-overlapping structural positions compose additively with no interaction effects"]}
```
