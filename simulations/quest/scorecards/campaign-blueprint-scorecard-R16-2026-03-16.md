# campaign-blueprint — Round 16 Scorecard (Rubric v16)

---

## Evaluation

### Structural Inventory

| Element | V-01 | V-02 |
|---------|------|------|
| SETUP: Scout Traceability Table (6-col, R-01/R-02/R-03 named) | ✓ | ✓ |
| SETUP: Inertia Model Map (4-col, CT-Spec/CT-Prop/CT-Pitch) | ✓ | ✓ |
| SETUP: Explicit match directive for CONVICTION DELTA | ✓ prose | ✓ prose (conversational) |
| SETUP: In-table RULE sentinel row inside MAP | ✗ | ✗ |
| REFLECTION: Conviction Delta (4-col, CT-named rows, in-cell Amplification template) | ✓ | ✓ (implied by hypothesis) |
| REFLECTION: Conviction Gap Diagnosis (6-col, CT-named rows, register-split) | ✓ | ✓ (implied) |
| REFLECTION: Traceability Audit (6-col, R-ID named rows, Scout Friction from SETUP, match directive) | ✓ | ✓ (implied) |
| REFLECTION: In-table RULE sentinel row inside CONVICTION DELTA | ✗ | ✗ |

---

### Criterion-Level Evaluation

| Criterion | V-01 | V-02 | Notes |
|-----------|------|------|-------|
| **C-34** — 4-col CONVICTION DELTA, in-cell Amplification chain template | FULL | FULL | CT-Spec/Prop/Pitch rows; `[trigger] → [signal] → [amplification] → [outcome]` template present in each |
| **C-35** — 6-col CONVICTION GAP DIAGNOSIS, pre-declared CT rows, register-split columns | FULL | FULL | Technical / Business / Executive column split; CT-Spec/Prop/Pitch pre-declared |
| **C-36** — 6-col TRACEABILITY AUDIT, correct column names | FULL | FULL | Req-ID / Requirement / Scout Friction / Spec Coverage / Proposal Coverage / Pitch Coverage |
| **C-38** — Traceability Audit named Req-ID rows, SETUP match directive | FULL | FULL | R-01/R-02/R-03 from SETUP; Scout Friction sourced from SETUP; explicit match directive present |
| **C-39** — Three-table structural chain (C-34 + C-35 + C-38 simultaneously) | FULL | FULL | All three pass |
| **C-40** — Conviction Delta INERTIA-MAP SETUP Linkage | FULL | FULL | 4-col MAP in SETUP; CONVICTION DELTA rows pre-named CT-Spec/Prop/Pitch; explicit prose match directive; D15 two-step inspection passes for both |
| **C-41** — Inertia-Linked Four-Table Structural Chain | FULL | FULL | C-34 ✓ + C-35 ✓ + C-38 ✓ + C-40 ✓ simultaneously |
| **C-42** — INERTIA MODEL MAP In-Table Enforcement Sentinel | **NO CREDIT** | **NO CREDIT** | V-01: match directive is a prose paragraph following the MAP table, not a non-data RULE sentinel row inside the MAP's row structure. D16 structural inspection: scan MAP rows for non-data enforcement row → absent. V-02: conversational prose directive ("One thing to remember…") is outside the MAP boundary; register invariance (D16) does not rescue this — the structural test is presence/absence of an in-table sentinel row, not register |
| **C-43** — Dual In-Table Sentinel Chain | **NO CREDIT** | **NO CREDIT** | C-42 fails for both → C-43 unreachable (strict superset of C-41 + C-42) |

---

### Composite Scores

| Variant | Axis | C-40 | C-41 | C-42 | C-43 | Score |
|---------|------|------|------|------|------|-------|
| V-01 — Pitch-First Role Sequence | Role sequence reorder | +5 | +5 | 0 | 0 | **243** |
| V-02 — Conversational Register | Phrasing register | +5 | +5 | 0 | 0 | **243** |

Both match their stated hypotheses exactly.

---

### Ranking

| Rank | Variant | Score | Ceiling Delta |
|------|---------|-------|---------------|
| 1 (tie) | V-01 | 243 | −10 |
| 1 (tie) | V-02 | 243 | −10 |

No R16 variant breaks the v15 ceiling. Neither introduces an in-table RULE sentinel, so C-42 and C-43 remain blocked for both.

---

### Diagnostic Summary

**V-01** confirms that changing the artifact generation sequence (Pitch → Spec → Proposal rather than Spec → Proposal → Pitch) produces no structural effect on the rubric evaluation. The SETUP tables and REFLECTION tables are isomorphic to the v15 ceiling pattern regardless of which artifact is generated first. Role sequence is not a rubric-relevant axis.

**V-02** re-instantiates the D16 register invariance principle from a different surface: the conversational first-person-plural frame ("Let's build", "One thing to remember", "we'll follow") delivers a semantically equivalent prose match directive with no loss on C-40 or C-41. The conversational register is not a rubric-relevant axis. However, D16's invariance extends in both directions — register cannot hurt a structurally correct blueprint, and it cannot rescue a structurally incomplete one. V-02's MAP carries no in-table sentinel, so C-42 fails regardless of how naturally the surrounding prose reads.

Both variants confirm the R15 finding: the prose/sentinel distinction is the only C-42-relevant axis.

---

### Excellence Signals

**Top-scoring variant:** V-01 and V-02 (tied, 243)

**New patterns from R16:**

1. **Role-sequence invariance**: The artifact generation order (Pitch-first vs. Spec-first vs. any permutation) has no effect on structural table scoring. SETUP table structure and REFLECTION table structure are evaluated independently of which artifact is produced first. A ceiling-breaking variant cannot be constructed by reordering generation phases — structural sentinels must appear inside the tables themselves regardless of sequence.

2. **Re-confirmation of register invariance under probe**: V-02 extends D16's register invariance finding under explicit conversational-register framing across the full blueprint including the SETUP match directive. The conversational directive ("one thing to remember…") is both semantically equivalent to V-01's formal directive and equally ineligible for C-42 — confirming that in-table vs. prose-only is a strictly structural distinction, not a prose-quality or register distinction.

---

```json
{"top_score": 243, "all_essential_pass": true, "new_patterns": ["role-sequence invariance: artifact generation order (pitch-first, spec-first, any permutation) does not affect structural table scoring; ceiling cannot be broken by reordering generation phases", "register invariance re-confirmed under full conversational framing: the in-table vs prose-only distinction for C-42 is strictly structural, independent of register and directive naturalness"]}
```
