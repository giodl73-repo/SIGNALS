Reading the rubric and scorecard carefully before writing.

The R6 excellence signals are the `(++)` markers in the scorecard — criteria where the variates went beyond the existing bar. From the scorecard evidence:

- **C-19**: TRANSCRIPTION-RECEIPT in-phase remediation — REVISED verdict triggers immediate rewrite + updated receipt within the same phase; phase cannot close with any REVISED outstanding
- **C-20**: BUILD-VERIFY exclusion manifest — explicit named list of what the phase must NOT do (no file writes, no comparisons, no AMEND generation, no summary rows); scope defined by enumerated prohibition, not just purpose statement
- **C-21**: TRANSCRIPTION-CLEAR all-artifact re-audit — dedicated re-audit step that confirms all three artifacts individually (A/B/C) in one pass, including previously VERBATIM ones; PATH-B exit token cannot emit until all-VERBATIM

Scoring update: 10 aspirational → 13 aspirational; 10 × 5 = 50 → 13 × 5 = 65; max 140 → 155; golden scales 82.9% × 155 ≈ 128; partial scales 85/140 × 155 ≈ 94.

---

```markdown
# corps-build Rubric — v5
**Updated**: 2026-03-17
**Based on**: Round 6 scorecard (V-01 through V-05)
**Changes from v4**: Added C-19, C-20, C-21 from R6 excellence signals; max updated 140 → 155; thresholds scaled.

---

## What Changed

| Version | Change | Source |
|---------|--------|--------|
| v1 → v2 | Added C-11 (named invariants block), C-12 (auditable check-output), C-13 (named failure modes per criterion) | R3 excellence signals |
| v2 → v3 | Added C-14 (dedicated pre-step FAILURE MODES block), C-15 (named CHECK-OUTPUT PROTOCOL section) | R4 excellence signals |
| v3 → v4 | Added C-16 (phase-exit guard tokens), C-17 (per-artifact TRANSCRIPTION-RECEIPT), C-18 (BUILD-VERIFY single-purpose phase) | R5 excellence signals |
| v4 → v5 | Added C-19 (TRANSCRIPTION-RECEIPT in-phase remediation), C-20 (BUILD-VERIFY exclusion manifest), C-21 (TRANSCRIPTION-CLEAR all-artifact re-audit) | R6 excellence signals |

**R6 pattern summary**: R6 revealed three structural innovations that close the remaining gaps between emitting a receipt and guaranteeing clean closure. C-19 (in-phase remediation) converts the TRANSCRIPTION-RECEIPT from an observation into an enforcement gate — a REVISED verdict triggers an immediate rewrite within the same phase; the phase cannot close while any REVISED remains outstanding. C-20 (BUILD-VERIFY exclusion manifest) requires the BUILD-VERIFY phase to enumerate what it must NOT do — file writes, structural checks, AMEND generation, summary rows — defining scope by prohibition rather than purpose, making out-of-scope behavior structurally visible as a build error. C-21 (TRANSCRIPTION-CLEAR all-artifact re-audit) requires a dedicated re-audit step that confirms all three artifacts in one pass, including those already VERBATIM before any rewrites, before the PATH-B exit token can be emitted — closing the gap where partial VERBATIM status could mask post-rewrite drift.

---

## Scoring Formula

| Category | Count | Points each | Subtotal |
|----------|-------|-------------|---------|
| Essential | 5 | 12 | 60 |
| Recommended | 3 | 10 | 30 |
| Aspirational | 13 | 5 | 65 |
| **Max** | | | **155** |

PARTIAL counts as 0.5 on any criterion.

**Golden threshold**: all 5 essential PASS + composite >= 128
**PARTIAL pass**: composite >= 94 with all 5 essential passing — earn full pass with 2/3 recommended

---

## Criteria

### Essential (12 pts each)

| ID | Criterion | Category | Notes |
|----|-----------|----------|-------|
| C-01 | **Role file completeness** — total file count in summary equals count of files written in Step 2; gap identified and resolved before proceeding | correctness | PASS requires verification mechanism, not just count statement |
| C-02 | **org-chart.md with ASCII hierarchy** — uses `+--` / `\|` notation; all org.yaml names verbatim; nesting reflects group → team depth | format | Concrete example or INVARIANT declaration required for PASS |
| C-03 | **Inertia Advocate in every team** — one IA per team, no exceptions; enforced as a closure gate before moving to next team | correctness | "Mandatory" imperative + enforcement hook required |
| C-04 | **org.yaml structural fidelity** — files written only to subdirectories derived from org.yaml; path pattern `.roles/{area-slug}/{role-slug}.md` | correctness | Pre-write path validation required for PASS |
| C-05 | **Role file typed fields present** — all five fields (`title`, `role-type`, `area`, `lens`, `expertise`) present with substantive bodies | coverage | Example files or field descriptions with quality bar required |

---

### Recommended (10 pts each)

| ID | Criterion | Category | Notes |
|----|-----------|----------|-------|
| C-06 | **Headcount by group table + levels** — table includes group, standard count, specialized count, IA count, total, and Levels column | depth | Column structure must be explicit; IA count column required for PASS |
| C-07 | **Standard vs specialized distinction** — `role-type` in frontmatter; write sequence orders standard → specialized → IA | correctness | Sequence must be stated; specialized distinctness must be enforced (not copyable from standard) |
| C-08 | **AMEND section with three options** — close with named repair options: specific area regeneration, level-term update, group-node addition | behavior | Area regeneration option should reference invariant re-checks |

---

### Aspirational (5 pts each)

| ID | Criterion | Category | Notes |
|----|-----------|----------|-------|
| C-09 | **Inertia Advocate team-contextualized** — IA lens and expertise drawn from this team's declared domain vocabulary; generic resistance language fails | depth | Named failure mode earns full PASS (see C-13) |
| C-10 | **Cross-reference integrity chart/roles** — explicit check statement: `Table Total = [n], files written = [n] — [MATCH \| MISMATCH]`; format is literal and auditable | correctness | Silent compliance is PARTIAL; emitted check string is PASS |
| C-11 | **Named invariants block** — a dedicated INVARIANTS (or equivalent) block naming structural rules as machine-checkable conditions; each invariant is yes/no against output, not descriptive prose | structure | Prose restatement of rules is PARTIAL; named enumerable block is PASS |
| C-12 | **Auditable check-output strings** — at least one output token in `[label]: [value] -- [PASS\|FAIL]` format emitted in the output stream where a reviewer can locate and compare; silent compliance is PARTIAL | auditability | Token must appear in actual emitted output, not just in the prompt instructions |
| C-13 | **Named failure modes per criterion** — for each Essential or Recommended criterion, the prompt names the specific failure mode (e.g., "FAIL: generic IA lens transplantable to any team"); criteria with no named failure mode score PARTIAL | robustness | At least one named failure mode per essential criterion required for PASS |
| C-14 | **Dedicated pre-step FAILURE MODES block** — a standalone named block before each write step enumerating what would cause that step to fail; not embedded in step prose; named section with scannable list | structure | Inline failure-mode prose is PARTIAL; separate named block is PASS |
| C-15 | **Named CHECK-OUTPUT PROTOCOL section** — a named protocol section (not prose) specifying the verification protocol; aggregates check strings in one named place; scattered or implicit checks score PARTIAL | auditability | Section must be named and locatable; distributed checks without a protocol section are PARTIAL |
| C-16 | **Phase-exit guard tokens** — named PASS/FAIL tokens emitted at the end of each major phase (e.g., `PARSE-PASS`, `VALIDATE-PASS`, `IA-PHASE-COMPLETE`); model cannot proceed to phase N+1 without emitting the PASS token for phase N; control flow auditable at phase boundaries | control-flow | Per-artifact guards (C-17) do not substitute; these are inter-phase gates |
| C-17 | **Per-artifact TRANSCRIPTION-RECEIPT** — at the moment each artifact is written, the model emits a synchronous `VERBATIM \| REVISED` status with reason; receipt is bound to the write event (contemporaneous), not a post-hoc batch check; one receipt per file write | auditability | Batch cross-reference is PARTIAL; contemporaneous per-write receipt is PASS |
| C-18 | **BUILD-VERIFY as named single-purpose phase** — a dedicated phase for verification only (no writing, no formatting, no new content); emits `BUILD-VERIFY-VERBATIM` or `BUILD-VERIFY-DRIFT` as output; structurally isolates the verification concern from production | structure | Verification embedded in a write phase is PARTIAL; dedicated named phase is PASS |
| C-19 | **TRANSCRIPTION-RECEIPT in-phase remediation** — a REVISED verdict on any receipt triggers an immediate rewrite of the artifact and an updated receipt within the same phase; the phase cannot close while any REVISED verdict remains outstanding; in-flight correction, not post-hoc repair | control-flow | Receipt without remediation gate is PARTIAL; in-phase rewrite + re-emit before phase close is PASS |
| C-20 | **BUILD-VERIFY exclusion manifest** — the BUILD-VERIFY phase includes an explicit named list of actions the phase must NOT perform (e.g., no file writes, no directory comparisons, no headcount verifications, no AMEND generation, no summary rows); any content outside the exclusion boundary is declared a build error; scope defined by enumerated prohibition, not just purpose statement | structure | Purpose-only statement ("verification only") is PARTIAL; explicit named exclusion list is PASS |
| C-21 | **TRANSCRIPTION-CLEAR all-artifact re-audit** — a dedicated re-audit step (`TRANSCRIPTION-CLEAR`) that enumerates all three artifacts individually (ARTIFACT-A, ARTIFACT-B, ARTIFACT-C) with `VERBATIM \| REVISED` verdict in one pass, including artifacts already VERBATIM before any rewrites; PATH-B exit token cannot be emitted until this block emits all-VERBATIM confirmation | control-flow | Re-audit of only REVISED artifacts is PARTIAL; full enumeration of all three before PATH-B exit is PASS |
```
