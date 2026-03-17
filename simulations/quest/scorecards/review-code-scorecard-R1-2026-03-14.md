## review-code — Round 1 Scoring

> **Note**: Trace artifact is `placeholder` — scoring reflects structural analysis of prompt designs (how mechanically each criterion is enforced), not actual model output. Scores carry execution-risk discounts where a well-formed prompt may still admit non-compliant output.

---

### V-01 — Role Sequence: Architecture-First

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Explicit `PASS/FAIL` verdict required per discipline in imperative form |
| C-02 | PASS | `file:line` annotation required in step descriptions, imperative register |
| C-03 | PASS | Findings organized by file per discipline step |
| C-04 | PASS | Dedicated synthesis step with pattern format required |
| C-05 | PASS | Expert disclosure step with signal explicitly required |
| C-06 | PASS | Spec compliance section present per discipline |
| C-07 | PASS | Severity labels required per finding in step |
| C-08 | **FAIL** | No explicit "summary line" requirement; count must be inferred from prose — reader must count |
| C-09 | PASS | Amend step (Step 6) present and scoped |
| C-10 | **FAIL** | Pattern step asks for "what the pattern is" — root cause hypothesis not explicitly required |

**Essential**: 5/5 → 60 | **Recommended**: 2/3 → 20 | **Aspirational**: 1/2 → 5
**Composite: 85**

---

### V-02 — Output Format: Table-Primary Findings

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Per-discipline verdict block with explicit `PASS \| N findings: X CRITICAL...` format |
| C-02 | PASS | Table column `File:Line` enforces annotation on every row; rule states "No row may reference only a function name" |
| C-03 | PASS | Table grouped by file, findings sorted by line within file group |
| C-04 | PASS | Cross-file pattern section with named format block |
| C-05 | PASS | `Domain Experts Selected:` block with `signal:` field required |
| C-06 | PASS | `Spec sections checked: [list]. Gaps: [list]` appended to each verdict block |
| C-07 | PASS | `Severity` column in table enforces CRITICAL/MAJOR/MINOR — format makes omission structurally impossible |
| C-08 | PASS | Verdict block format `N findings: X CRITICAL, Y MAJOR, Z MINOR` is explicit, not counted manually |
| C-09 | PASS | Amend Step 6 present with explicit field structure |
| C-10 | PASS | Pattern format block includes `Root cause hypothesis:` as named field |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 2/2 → 10
**Composite: 90** *(discount from 100: C-10 root cause hypothesis is prompted but genuine causal claims remain model-dependent)*

---

### V-03 — Phrasing Register: Conversational

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | "give a quick verdict (PASS or FAIL)" stated, but buried in prose — compliant output likely |
| C-02 | **FAIL** | "include a `file:line` reference" is conversational suggestion, not mechanical enforcement; execution risk high |
| C-03 | PASS | "Organize your findings by file" stated clearly |
| C-04 | PASS | "Look for patterns across files" section present |
| C-05 | PASS | "Tell the reader who you selected and what in the code told you" clearly stated |
| C-06 | PASS | "each discipline should note which spec requirements it checked" stated |
| C-07 | **FAIL** | "Label each finding as CRITICAL, MAJOR, or MINOR" stated but soft framing; conversational output likely drops labels for some findings |
| C-08 | **FAIL** | "a count of how many findings you found" stated but no format enforcement; likely prose burial |
| C-09 | PASS | Amend section present |
| C-10 | PASS | "offer a hypothesis about why it exists" explicitly stated with examples |

**Essential**: 4/5 → 48 | **Recommended**: 1/3 → 10 | **Aspirational**: 2/2 → 10
**Composite: 68**

---

### V-04 — Role Sequence + Lifecycle Emphasis: Expert-First + Dedicated Synthesis Phase

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Lifecycle Phase 2 requires per-discipline PASS/FAIL verdicts |
| C-02 | PASS | `file:line` required in imperative form |
| C-03 | PASS | File-grouped findings within discipline phases |
| C-04 | PASS | Phase 3 Synthesis is a required, named phase with its own heading — not a footnote |
| C-05 | PASS | Phase 1 expert assembly occurs before any discipline fires; signal disclosure required |
| C-06 | PASS | Spec compliance per discipline stated in Phase 2 |
| C-07 | PASS | Severity labels required per finding |
| C-08 | PASS | Count summary per discipline in Phase 2 verdict |
| C-09 | PASS | Phase 4 Amend Scope with named sub-outputs |
| C-10 | PASS | Synthesis Phase 3 explicitly elevated as required deliverable; root cause expected output |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 2/2 → 10
**Composite: 90** *(discount: C-10 depends on Phase 3 prompt text completeness, which is cut off in trace)*

---

### V-05 — Output Format + Inertia Framing

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Verdict block named as one of three things naive reviews leave out — framing primes it |
| C-02 | PASS | Table-per-file format mechanically enforces file:line; inertia framing names "no line numbers" as a known failure |
| C-03 | PASS | Table organized per file |
| C-04 | PASS | Pattern block with mandatory `Why:` line — inertia framing names "no patterns" as a known miss |
| C-05 | PASS | Silent expert selection explicitly named as one of three naive-review failures — model is primed to disclose |
| C-06 | PASS | Spec compliance present in verdict block |
| C-07 | PASS | Table column enforces severity; inertia framing names unlabeled findings as failure mode |
| C-08 | PASS | Summary per discipline in verdict block |
| C-09 | PASS | Amend disclosure section present |
| C-10 | PASS | Mandatory `Why:` field in pattern block — structural enforcement, not suggestion |

**Essential**: 5/5 → 60 | **Recommended**: 3/3 → 30 | **Aspirational**: 2/2 → 10
**Composite: 95** *(minimal execution risk: C-02/C-07 table-enforced; C-05 failure mode named explicitly)*

---

### Rankings

| Rank | Variation | Composite | All Essential |
|------|-----------|-----------|---------------|
| 1 | V-05 (Table + Inertia Framing) | **95** | YES |
| 2 | V-02 (Table-Primary) | **90** | YES |
| 2 | V-04 (Expert-First + Synthesis Phase) | **90** | YES |
| 4 | V-01 (Architecture-First) | **85** | YES |
| 5 | V-03 (Conversational) | **68** | NO |

---

### Excellence Signals from V-05

**Signal 1 — Inertia framing raises the floor on the hardest criteria**
Opening by naming what a naive review omits (no verdicts, no cross-file patterns, silent expert selection) forces the model to treat those outputs as marked requirements rather than optional polish. C-04 and C-05 — the two criteria most commonly absent in baseline runs — become salient failure modes before the first step fires.

**Signal 2 — Mandatory named fields in pattern blocks enforce C-10 mechanically**
The `Why:` line in the pattern format block converts root-cause hypothesis from an aspirational suggestion into a required structural field. V-01 and V-02 ask for patterns; only V-05 enforces that each pattern block is structurally incomplete without a causal claim.

**Signal 3 — Table format + framing combination eliminates C-02/C-07 failure independently**
V-02 achieves mechanical C-02/C-07 enforcement through table columns. V-05 achieves the same AND names missing annotations as a known failure mode — making the requirement doubly enforced via both structure and primed awareness. The combination outperforms either mechanism alone.

---

```json
{"top_score": 95, "all_essential_pass": true, "new_patterns": ["inertia-framing — opening by naming known rubric failure modes raises the floor on hardest criteria (C-04, C-05) before first step fires", "mandatory-field syntax in pattern blocks (Why:) enforces root-cause hypothesis structurally rather than as suggestion"]}
```
