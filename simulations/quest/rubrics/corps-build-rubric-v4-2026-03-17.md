Reading the R5 scorecard carefully to extract the new excellence patterns before writing the rubric.

**R5 excellence signals I'm extracting:**

1. **Phase-exit guard tokens** (all four variates): Named PASS/FAIL tokens emitted at the end of each major phase (`PARSE-PASS/FAIL`, `VALIDATE-PASS/FAIL`, `IA-PHASE-COMPLETE`, `ROLES-COMPLETE`). Control flow is gated — the model cannot proceed to phase N+1 without emitting a PASS token for phase N. Distinct from C-12 (which covers artifact check strings) — phase guards are inter-phase control flow, not intra-artifact verification.

2. **Per-artifact TRANSCRIPTION-RECEIPT** (V-02 and V-04): At the moment each artifact is written, the model emits a synchronous `VERBATIM | REVISED` status with reason. This is contemporaneous and per-file — stronger than C-12's batch cross-reference. C-12 allows one emitted check string anywhere; this requires a receipt bound to each write event.

3. **BUILD-VERIFY as a named single-purpose phase** (V-01 and V-04): A dedicated phase that does only verification — no writing, no formatting — and emits `BUILD-VERIFY-VERBATIM | BUILD-VERIFY-DRIFT` as its output. Distinct from C-12 (which is about check strings) and C-15 (which is about a named protocol section) — this is about structural phase isolation of the verification concern.

These become **C-16**, **C-17**, **C-18**. Max rises 125 → 140. Golden threshold scales proportionally (82.6% → ~116).

---

```markdown
# corps-build Rubric — v4
**Updated**: 2026-03-17  
**Based on**: Round 5 scorecard (V-01 through V-04)  
**Changes from v3**: Added C-16, C-17, C-18 from R5 excellence signals; max updated 125 → 140; thresholds scaled.

---

## What Changed

| Version | Change | Source |
|---------|--------|--------|
| v1 → v2 | Added C-11 (named invariants block), C-12 (auditable check-output), C-13 (named failure modes per criterion) | R3 excellence signals |
| v2 → v3 | Added C-14 (dedicated pre-step FAILURE MODES block), C-15 (named CHECK-OUTPUT PROTOCOL section) | R4 excellence signals |
| v3 → v4 | Added C-16 (phase-exit guard tokens), C-17 (per-artifact TRANSCRIPTION-RECEIPT), C-18 (BUILD-VERIFY single-purpose phase) | R5 excellence signals |

**R5 pattern summary**: R5 revealed three structural innovations in the BUILD-VERIFY / TRANSCRIPTION-RECEIPT family. All four variates used named phase-exit guard tokens (PARSE-PASS/FAIL, VALIDATE-PASS/FAIL, IA-PHASE-COMPLETE) to create hard inter-phase gates — the model cannot skip ahead without emitting the gate token, making control flow auditable at phase boundaries, not just artifact boundaries. V-02 and V-04 introduced the TRANSCRIPTION-RECEIPT pattern: a synchronous VERBATIM/REVISED receipt emitted at the moment of each artifact write, creating a contemporaneous per-file audit trail that a batch cross-reference cannot replicate. V-01 and V-04 introduced BUILD-VERIFY as a single-purpose phase dedicated exclusively to verification — no writing, no formatting — with its own phase-exit token, structurally isolating the verification concern from the production concern.

---

## Scoring Formula

| Category | Count | Points each | Subtotal |
|----------|-------|-------------|---------|
| Essential | 5 | 12 | 60 |
| Recommended | 3 | 10 | 30 |
| Aspirational | 10 | 5 | 50 |
| **Max** | | | **140** |

PARTIAL counts as 0.5 on any criterion.

**Golden threshold**: all 5 essential PASS + composite >= 116  
**PARTIAL pass**: composite >= 85 with all 5 essential passing — earn full pass with 2/3 recommended

---

## Criteria

### Essential (12 pts each)

| ID | Criterion | Category | Notes |
|----|-----------|----------|-------|
| C-01 | **Role file completeness** — total file count in summary equals count of files written in Step 2; gap identified and resolved before proceeding | correctness | PASS requires verification mechanism, not just count statement |
| C-02 | **org-chart.md with ASCII hierarchy** — uses `+--` / `\|` notation; all org.yaml names verbatim; nesting reflects group → team depth | format | Concrete example or INVARIANT declaration required for PASS |
| C-03 | **Inertia Advocate in every team** — one IA per team, no exceptions; enforced as a closure gate before moving to next team | correctness | "Mandatory" imperative + enforcement hook required |
| C-04 | **org.yaml structural fidelity** — files written only to subdirectories derived from org.yaml; path pattern `.craft/roles/{area-slug}/{role-slug}.md` | correctness | Pre-write path validation required for PASS |
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
| C-11 | **Named invariant block at entry point** — all enforcement mechanisms declared as `INVARIANT-N` (or `INV-N`) before any steps; each invariant referenced by name in step body and AMEND section | structure | Entry-point declaration + downstream reference required; inline-only restatement is PARTIAL |
| C-12 | **Auditable check-output statements** — at least one criterion requires the model to emit a literal verification string (`[MATCH \| MISMATCH]`, `[PASS \| FAIL]`, or equivalent) as part of its output, not silent compliance | verifiability | One emitted check string anywhere earns PASS; pure compliance-reliance is FAIL |
| C-13 | **Named failure mode per aspirational criterion** — each aspirational criterion (C-09, C-10, C-11, C-12) names at least one concrete violation example (what the wrong output looks like) | precision | All four named earns PASS; one or more named earns PARTIAL; none is FAIL |
| C-14 | **Dedicated FAILURE MODES pre-step block** — all aspirational failure modes front-loaded in a single named section before Step 1; model encounters every wrong-output anchor before producing any output | structure | Named block before Step 1 required for PASS; inline-per-step placement is PARTIAL |
| C-15 | **Named CHECK-OUTPUT PROTOCOL section** — verifiable output requirements elevated to a first-class named protocol section with explicit enumerated rules; not scattered inline compliance notes | verifiability | Named section with enumerated rules required for PASS; audit strings scattered inline is PARTIAL |
| C-16 | **Phase-exit guard tokens** — each major phase emits a named PASS/FAIL token (`PARSE-PASS/FAIL`, `VALIDATE-PASS/FAIL`, `IA-PHASE-COMPLETE`, etc.) before the next phase begins; control flow is gated, not assumed | control-flow | Three or more distinct phase gate tokens earns PASS; one or two earns PARTIAL; no gates is FAIL |
| C-17 | **Per-artifact TRANSCRIPTION-RECEIPT** — at the moment each artifact is written, the model emits a synchronous receipt (`VERBATIM \| REVISED — {reason}`) bound to that specific file; contemporaneous and per-file, not a batch post-hoc check | verifiability | Receipt on every artifact earns PASS; receipt on some artifacts earns PARTIAL; batch-only or no receipt is FAIL |
| C-18 | **BUILD-VERIFY single-purpose phase** — a named phase dedicated exclusively to verification (no writing, no formatting in the same phase); emits a `BUILD-VERIFY-PASS \| BUILD-VERIFY-DRIFT` phase-exit token; structurally isolates the verification concern | structure | Named single-purpose verification phase with phase-exit token required for PASS; verification mixed into a writing phase is PARTIAL |
```
