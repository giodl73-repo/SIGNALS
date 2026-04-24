`simulations/quest/rubrics/quest-rubric-mock-ns-v16-2026-03-15.md` written.

---

**Two new criteria extracted from Round 16:**

**C-44 — Single-task executor annotation on pre-filled confirmation record templates** (depends on C-41)
V-05 uniquely annotated each template at S-3 and A-1 with "(fill Match field only)." V-01 and V-04 pass C-41 without this annotation — the executor must infer which field is theirs. The annotation names the single residual task explicitly, reducing compliance to one labeled decision. Both use sites must carry the annotation for PASS.

**C-45 — Per-use-site anti-bypass protocol reminder at each bracket-token row** (depends on C-43)
V-05 uniquely placed a per-row protocol reminder at S-3 and A-1: "Protocol reminder: processing this row without reading the Step and Row type cells, or without performing Phase 2, is a protocol failure." V-02 and V-04 pass C-43 with preamble-only declarations. C-45 closes the recall gap by echoing the anti-bypass constraint at the exact point of use — the same pattern C-37 establishes for the confirmation trigger, applied to the anti-bypass protocol. A reminder naming only one bypass form or present at only one site scores PARTIAL.

**Scoring denominator: 35 → 37.** Formula: `aspirational_pass / 37 * 10`.
