`trace-contract-variate-R9-2026-03-15.md` written.

---

## Round 9 Variations — Design Notes

**New criteria targeted:** C-33, C-34, C-35.

**Single-axis variations (V-01 to V-03):** Role Sequence, Output Format, Lifecycle Emphasis.
**Combination variations (V-04 to V-05):** Inertia Framing (single axis), Combined Full Integration.

---

### V-01 — Role Sequence

**Hypothesis:** When the role contract is the opening structural document — with a "Cannot Own" column and an explicit single-agent-substitution prohibition before any phase description — C-34 is a structural property of the template rather than a prose declaration buried in a phase. A GATE 1 header stating "symmetry required — neither path may use weaker attestation form than the other" satisfies C-33 by making the equal-treatment requirement a gate-level enforcement condition. C-35 is satisfied by a named `Remediation Origin` column in the delta table plus a batch grouping step triggered by that column.

**C-34 mechanism:** Pre-printed "Cannot Own" column in role table + "structurally enforced — not operationally optional" in role table header + "Single-agent substitution is prohibited by this template" sentence.

**C-33 mechanism:** GATE 1 header names symmetry as a gate requirement ("Neither path may use weaker attestation form than the other"). Both clauses use two-clause confirmable form.

**C-35 mechanism:** `Remediation Origin` column in delta table (inertia-spec-drift | independent-schema-gap) + batch grouping instruction after the table.

---

### V-02 — Output Format

**Hypothesis:** Pre-printed template surfaces make C-33, C-34, and C-35 structurally unavoidable — the model transcribes pre-printed content rather than generating it. Both GATE 1 contamination-path clauses are physically identical in the template, making asymmetry impossible without actively modifying pre-printed text. The inertia-batch section header is pre-printed in Phase 5; omitting it requires deletion, not omission.

**C-34 mechanism:** "Role separation is structurally enforced — it is not operationally optional. Single-agent substitution is prohibited by this template." pre-printed in role table header.

**C-33 mechanism:** Both GATE 1 clauses pre-printed in identical two-clause form — model transcribes both, cannot produce asymmetric output.

**C-35 mechanism:** `INERTIA-SPEC-DRIFT REMEDIATION BATCH` section header pre-printed in Phase 5 with pre-printed batch template fields.

---

### V-03 — Lifecycle Emphasis

**Hypothesis:** Framing C-33 as a lifecycle guarantee ("dual structural guarantee at the Phase 1A close") makes the symmetry requirement legible as a lifecycle property: both contamination paths are first-class inputs to Phase 1B, and Phase 1B's external validation is only meaningful if both inputs were attested with equal rigor. C-34 is satisfied by the lifecycle explanation of why Phase 1B role separation is structurally required — it names substitution as the lifecycle failure mode. C-35 is satisfied by a named Phase 5 two-sub-stage structure where Stage 5-B has its own lifecycle purpose declaration.

**C-34 mechanism:** Phase 1A STOP marker: "Phase 1B is a different lifecycle stage owned by a different role. Phase 1B's purpose is defeated if the Phase 1A author also certifies GATE 1B. Single-agent substitution at this lifecycle boundary is the failure mode this template structurally prevents."

**C-33 mechanism:** GATE 1 header: "Dual structural guarantee at Phase 1A close — neither clause may use weaker attestation form than the other. The two-clause confirmable form applies identically to both paths."

**C-35 mechanism:** Phase 5 has named "Stage 5-A" and "Stage 5-B" with distinct lifecycle purpose declarations; Stage 5-B is the inertia batch grouping step with "lifecycle purpose" framing.

---

### V-04 — Inertia Framing

**Hypothesis:** When the inertia contamination model is the primary organizing concept, C-33 emerges as the "equal-treatment rule" — two contamination paths, both first-class, both requiring equivalent attestation form — stated at the top of the artifact before Phase 0. C-34 is framed as the structural mechanism that makes Phase 1B's challenge review meaningful: substitution defeats the inertia model. C-35 is the "inertia accounting layer" at the delta — a required second step that distinguishes catch-up amendments from new requirements.

**C-34 mechanism:** Inertia model table has a "Contamination Responsibility" column; role contract explains "Expert cannot certify GATE 1B. This is not a preference — it is the mechanism that makes Phase 1B's contamination check meaningful."

**C-33 mechanism:** "The equal-treatment rule" declared in the inertia model preamble before Phase 0 begins; GATE 1 header cites it: "Equal-treatment rule applied."

**C-35 mechanism:** Phase 5 described as "inertia accounting layer" with two distinct remediation categories and a dedicated "Step 5-B" with rationale about different downstream remediation tracks.

---

### V-05 — Combined Full Integration

**Hypothesis:** Combining all four axes gives C-33, C-34, and C-35 each at least two independent structural enforcement mechanisms — no criterion depends on a single instruction or a single structural device.

| Criterion | Mechanism 1 | Mechanism 2 | Mechanism 3 |
|-----------|-------------|-------------|-------------|
| C-33 | GATE 1 header names equal-treatment rule | Both clauses pre-printed in identical form | Inertia model preamble declares equal-treatment before Phase 0 |
| C-34 | Role contract "Cannot Own" column | "Not operationally optional" + "explicitly prohibited" in role contract header | Phase 1A STOP marker names substitution as the prohibited action |
| C-35 | Phase 5A/5B two-sub-stage structure with distinct lifecycle purposes | Pre-printed `INERTIA-SPEC-DRIFT REMEDIATION BATCH` section header | Inertia model preamble describes the two remediation categories before Phase 0 |

**Distinction from R8 V-05:** R8 V-05 had the "not operationally optional" language and the inertia-batch grouping as a note. R9 V-05 promotes both to structural elements: the prohibition is in the role contract "Cannot Own" column and repeated at every STOP marker; the inertia batch is a named Phase 5B with a lifecycle purpose declaration and pre-printed batch template.
