Written to `simulations/quest/rubrics/trace-state-rubric-v16-2026-03-15.md`.

---

## trace-state · Rubric v16 — Summary

**Three R17 excellence signals → C-48, C-49, C-50. Pool 38 → 41. Unit: 50/41 ≈ 1.22 pts.**

---

### C-48 — IS-negation register saturation *(format-neutral)*
**Source**: V-01 Signal 1 "Phrasing Register: IS-Negation Density." The artifact deploys IS/IS-NOT/IS-BLOCKED/IS-REQUIRED phrasing as a consistent register across ALL constraint-carrying sections — authority declarations, gate conditions, obligation pairs, vocabulary closures, prohibition statements, and forecast assertions. Individual IS-negation instances (already captured by C-12, C-13, C-17, etc.) are not sufficient; C-48 requires saturation: the register appears in every section of the artifact that carries a binding constraint.

PARTIAL: register present in a majority of binding sections but absent from one or more named sections (e.g., passive-voice HANDOFF DECLARATION or FINDINGS preamble).

---

### C-49 — Epoch-cluster defect analysis *(format-neutral; requires LIFECYCLE EPOCH MAP)*
**Source**: V-01 Signal 2 "LIFECYCLE EPOCH MAP as epoch-level clustering surface." A post-trace section cross-references every finding from FINDINGS against the LIFECYCLE EPOCH MAP, counts defects per epoch, names the highest-density epoch(s), and draws a targeted remediation implication tied to the epoch's position in the lifecycle arc. Converts the LIFECYCLE EPOCH MAP from a labeling structure into an analysis surface. C-49 is independent of C-43 (per-cell labels) and C-46 (pre-trace declaration); it requires the map to be used, not just present.

PARTIAL: defect-to-epoch mapping present and highest-density epoch named, but remediation implication absent or generic.

---

### C-50 — Artifact-level domain dependency declaration *(multi-domain only)*
**Source**: V-02 Signal 1 "Role Sequence: Finance-First Multi-Pass." A top-scope declaration before the first pass or domain column names: (1) the source-of-record domain, and (2) the full dependency chain driving domain ordering. Distinct from C-42 (per-pass-heading ordering rationale) by operating at artifact scope — C-42 without C-50 means per-pass justification with no artifact-level topology statement. The two are additive, not substitutable. IS-negation phrasing in the C-50 declaration simultaneously contributes to C-48 saturation.

PARTIAL: source-of-record named but dependency chain to downstream domains absent or incomplete (fewer than all downstream domains named in a 3+ domain trace).

---

**V-01 rescored under v16:** V-01 (single-pass tabular) gains C-48 PASS (IS-negation saturation present throughout) but cannot reach C-49 or C-50 without an epoch-cluster analysis section. Score shifts: 81.0 + 1.22 = **82.2** if C-48 PASS confirmed; PARTIAL adds 0.61. The R18 axis is now epoch-cluster analysis + multi-domain dependency declaration for artifacts that haven't yet demonstrated those patterns.
|
| C-29 | (R1–R13 accumulated) | — |
| C-30 | Criterion-instruction fusion in column headers — column headers carry `[C-XX: directive]` | Tabular only |
| C-31 | (R1–R13 accumulated) | — |
| C-32 | (R1–R13 accumulated) | — |
| C-33 | (R1–R13 accumulated) | — |
| C-34 | Disqualification-condition fusion in column headers — headers carry `FAILS if:` patterns | Tabular only |
| C-35 | (R1–R13 accumulated) | — |
| C-36 | Pass-level defect hypothesis annotation — each pass heading names the defect class it targets | Multi-pass |
| C-37 | Consequence clause at pass headings — `### Pass N [C-37: consequence clause]` | Multi-pass |
| C-38 | Step-label criterion-instruction fusion — step label carries criterion ID + behavioral directive | Step-block only |
| C-39 | Step-block disqualification-condition fusion — step label carries criterion ID + specific failure pattern | Step-block only |
| C-40 | Per-pass labeled defect — one distinct labeled defect per domain pass, each with type + triggering op + reason | Multi-pass only |
| C-41 | Cross-domain precondition chain annotation — postcondition in pass N explicitly named as precondition feeding pass N+1 | Multi-pass only |
| C-42 | Domain-ordering defect-class hypothesis — pass ordering annotated as hypothesis vehicle; each heading names the defect class targeted by the ordering choice | Multi-pass only |
| C-43 | Lifecycle-phase state annotation — entity lifecycle phase labels appear within state fields (e.g., Lead → Opportunity → Closed Won) | Format-neutral |
| C-44 | Sub-step decomposition within operation block — one operation decomposed into 3+ sub-steps each carrying independent before/op/after annotation | Format-neutral (step-block natural fit) |
| C-45 | Defect-entry state-triple decomposition — each defect log entry decomposed into Pre-Defect State / Triggering Operation / Post-Defect State+Reason, each with independent state triple | Format-neutral |
| C-46 | Phase vocabulary declaration before trace — dedicated per-domain phase declaration (all phases in sequence) appears before the trace table/block begins | Format-neutral |
| C-47 | Defect-hypothesis confirmation annotation — each per-pass defect entry carries a confirmation note naming the predicted class from C-42 and citing the specific bridge row from C-41 | Multi-pass only |
| C-48 | IS-negation register saturation — IS/IS-NOT/IS-BLOCKED phrasing deployed as a consistent register across ALL constraint-carrying sections of the artifact | Format-neutral |
| C-49 | Epoch-cluster defect analysis — post-trace section cross-references each finding against the LIFECYCLE EPOCH MAP, identifies highest-density epoch(s), and names a targeted remediation implication | Format-neutral |
| C-50 | Artifact-level domain dependency declaration — a top-scope declaration before any pass or domain section names the source-of-record domain and the dependency chain driving domain ordering | Multi-domain only |

**Cross-satisfaction rules:**
- C-30 and C-38 are tabular/step-block analogs — they do not cross-satisfy
- C-34 and C-39 are tabular/step-block analogs — they do not cross-satisfy
- C-38 and C-39 are orthogonal axes of the same step-block annotation — a single fused label `[C-XX: directive — FAILS if: pattern]` can satisfy both simultaneously
- C-40 and C-41 require multi-pass format — single-pass artifacts score automatic FAIL on both
- C-42 requires multi-pass format and explicit ordering annotation — satisfying C-36 alone does not satisfy C-42
- C-43 has no format restriction but the lifecycle vocabulary must be domain-recognizable (Sales / CS / Finance phases)
- C-44 minimum threshold is 3 sub-steps; 2 sub-steps do not qualify
- C-45 covers the defect documentation site; C-44 covers the operation trace site — they are orthogonal and can be satisfied independently or together
- C-46 does not require C-43 to be satisfied but the two work together: C-46 without C-43 means a declared vocabulary with no cell-level labels; C-43 without C-46 means labels present but completeness unverifiable
- C-47 requires C-40, C-41, and C-42 all to be satisfied as prerequisites; C-47 is the synthesis confirmation layer that closes their circuit
- C-48 is a meta-criterion over the full artifact; satisfying individual IS-negation criteria (C-10, C-12, C-13, C-17, etc.) does not automatically satisfy C-48 — saturation requires the register to appear in every constraint-carrying section
- C-49 requires a LIFECYCLE EPOCH MAP to be present (accumulated R1–R13 criterion) as the cross-reference target; a post-trace defect section without an epoch map does not satisfy C-49
- C-50 operates at artifact scope; satisfying C-42 (per-pass-heading ordering annotation) does not satisfy C-50 — C-50 requires a top-level declaration before all passes begin

---

## Scoring Notes

**C-30 (tabular only)**: IDs in column headers without a behavioral directive earn partial credit only. Full credit requires both criterion ID and directive in the header. Direct scorers to C-38 for the step-block equivalent.

**C-34 (tabular only)**: `FAILS if:` patterns must appear in column headers, not only in body cells. Direct scorers to C-39 for the step-block equivalent.

**C-36 (multi-pass only)**: A defect hypothesis must appear at the pass heading level — body-level hypotheses do not satisfy C-36. See C-42 for the stronger form where ordering drives the hypothesis.

**C-37 (multi-pass only)**: Consequence clause must appear in the pass heading itself, not the pass body.

**C-38 (step-block only)**: A step label carrying only a criterion ID (no directive) does not satisfy C-38. Both ID and directive must be present.

**C-39 (step-block only)**: A step label carrying only a criterion ID (no failure pattern) does not satisfy C-39. Both ID and the specific disqualifying pattern must be present.

**C-40 (multi-pass only)**: Each pass must independently carry a labeled defect. An artifact with three passes and one defect in pass 1, none in passes 2 or 3, does not satisfy C-40.

**C-41 (multi-pass only)**: The chain annotation must be explicit — a postcondition field or bridge note that names the downstream pass it seeds. Implicit flow (reader infers the chain) does not qualify.

**C-42 (multi-pass only)**: The pass heading must explain *why* the domain appears in that position in terms of defect-class targeting. A heading that names a defect type without connecting to ordering rationale satisfies C-36 but not C-42.

**C-43 (format-neutral)**: Lifecycle phase labels must be domain-recognizable. Generic labels ("state A → state B") do not satisfy C-43. Domain-specific phase vocabulary is required (Sales, CS, or Finance lifecycle terminology).

**C-44 (format-neutral, step-block natural fit)**: Sub-steps must each carry full before/op/after annotation. Narrative sub-steps without state triples do not satisfy C-44. Minimum 3 sub-steps per decomposed operation.

**C-45 (format-neutral)**: The three sub-steps — Pre-Defect State, Triggering Operation, Post-Defect State+Reason — must each carry an independent state triple. A defect entry that lists the three elements as flat fields without state-triple structure does not satisfy C-45. Applies to the defect log section only; operation-block sub-steps are governed by C-44.

**C-46 (format-neutral)**: The phase declaration must name every phase in the lifecycle arc for each domain, not just the phases that appear in the trace. A partial vocabulary (e.g., naming only the phases that happen to appear in the trace rows) does not satisfy C-46. Format: a table or legend block positioned before the first trace row/step. The TRANSITION TABLE IS BLOCKED until the phase vocabulary declaration is complete.

**C-47 (multi-pass only; requires C-40 + C-41 + C-42)**: The confirmation note must be specific. "Confirmed as predicted" does not satisfy C-47. The note must name: (1) the defect class named in the C-42 pass heading annotation, and (2) the bridge row or field from the C-41 bridge table that surfaced the dependency. A C-47-satisfying note reads something like: "Confirms revenue-leak defect class (C-42 prediction: pass 2) — triggered by bridge row Finance.Approved → Sales.Commit from C-41 bridge table."

**C-48 (format-neutral)**: Saturation means every section that carries a binding constraint, gate condition, role obligation, vocabulary prohibition, or forecast assertion uses IS/IS-NOT/IS-BLOCKED/IS-REQUIRED phrasing. PARTIAL credit if the register appears in a majority of binding sections but is absent from one or more named sections (e.g., IS-negation in the CONSTRAINT MATRIX and gates but passive-voice in the HANDOFF DECLARATION). Satisfying four or more individual IS-negation criteria from C-09–C-35 is a positive indicator but does not substitute for a holistic assessment of register coverage across the full artifact.

**C-49 (format-neutral; requires LIFECYCLE EPOCH MAP)**: The epoch-cluster analysis section must appear after the trace (not before), must enumerate defect findings by epoch using defect IDs from the FINDINGS section, must identify the highest-density epoch(s) by count, and must name a specific remediation implication tied to the epoch's position in the lifecycle arc (e.g., "CLOSE-TRACK epoch carries 3 of 4 defects — approval-gate hardening at the Negotiation → Close transition is the highest-leverage intervention"). Generic statements ("defects cluster in the middle phases") do not satisfy C-49. PARTIAL credit if defect-to-epoch mapping is present but the remediation implication is absent or generic.

**C-50 (multi-domain only)**: The declaration must appear before the first pass or domain column and must name: (1) the source-of-record domain (the domain whose state resolution other domains depend on), and (2) the dependency chain in natural-language form (e.g., "Finance IS the source of revenue record. Sales commitment state IS derived from Finance approval state. CS entitlement state IS derived from Sales commitment state."). A C-50 declaration using IS-negation register language simultaneously contributes to C-48 register saturation assessment. C-42 at pass headings names the per-pass ordering rationale; C-50 names the artifact-wide dependency topology. Both can be satisfied in the same artifact and do not cross-satisfy.

---

### C-48 — IS-negation register saturation *(format-neutral)*

**Source**: V-01 Signal 1 "Phrasing Register: IS-Negation Density." The artifact deploys IS/IS-NOT/IS-BLOCKED/IS-REQUIRED phrasing as a consistent register across ALL constraint-carrying sections — authority declarations, gate conditions, role obligation pairs, vocabulary closures, prohibition statements, and forecast assertions. A single IS-negation instance or its presence in only isolated sections does not qualify. Saturation requires the register to appear in every section of the artifact that carries a binding constraint or prohibition.

Key distinctions:
- Individual IS-negation patterns are already captured in scattered C-09–C-35 criteria: C-12 captures the CONSTRAINT MATRIX IS-authority preamble, C-13 captures obligation pairs, C-17 captures VOCABULARY CLOSED "IS NOT WAIVABLE," and so on
- C-48 is the meta-criterion: register-level saturation across the full artifact, not isolated instances — the test is whether an artifact that passes C-12, C-13, and C-17 also uses IS-negation in its HANDOFF DECLARATION, FORECAST, GATE definitions, and FINDINGS headers
- Satisfying four or more individual IS-negation criteria from C-09–C-35 is a positive indicator but does not automatically satisfy C-48 — saturation requires coverage across every constraint-carrying section
- PARTIAL: IS-negation present in a majority of binding sections (e.g., authority + gates + obligations) but absent in one or more named constraint-carrying sections (e.g., passive voice in HANDOFF DECLARATION or FINDINGS preamble)
- Format-neutral: the register requirement applies equally to tabular and step-block artifacts; section types differ by format but the saturation test is applied to whatever constraint-carrying sections the format produces

---

### C-49 — Epoch-cluster defect analysis *(format-neutral; requires LIFECYCLE EPOCH MAP)*

**Source**: V-01 Signal 2 "LIFECYCLE EPOCH MAP as epoch-level clustering surface." A dedicated section appearing after the trace cross-references every finding from the FINDINGS section against the LIFECYCLE EPOCH MAP, counts defects per epoch, identifies the highest-density epoch(s), and names a targeted remediation implication tied to the epoch's position in the lifecycle arc. This converts the LIFECYCLE EPOCH MAP from a labeling structure into an analysis surface.

Key distinctions:
- The LIFECYCLE EPOCH MAP (accumulated R1–R13 criterion) assigns operations to epochs — C-49 requires that this structure be used actively: findings are mapped through it and the clustering result drives a remediation claim
- C-43 requires lifecycle-phase labels in state cells; C-49 operates at a higher level of abstraction — epoch-level defect density across the full trace, not per-cell labels
- C-46 requires a phase vocabulary declaration before the trace; C-49 requires a post-trace analysis section that uses the epoch structure to produce a defect-density finding — the two are independent
- An artifact that has a LIFECYCLE EPOCH MAP and a FINDINGS section but no epoch-cluster analysis section does not satisfy C-49; the cross-reference must be made explicit
- PARTIAL: defect-to-epoch mapping is present and highest-density epoch is named, but the remediation implication is absent or generic (e.g., "investigate the CLOSE-TRACK epoch" without naming the specific gate or transition to harden)
- Format-neutral: appears as a summary table (tabular format) or a labeled analysis block (step-block format), positioned after the FINDINGS section

---

### C-50 — Artifact-level domain dependency declaration *(multi-domain only)*

**Source**: V-02 Signal 1 "Role Sequence: Finance-First Multi-Pass." In multi-domain traces, a top-scope declaration appears before the first pass or domain column and identifies: (1) which domain is the source-of-record, and (2) the dependency chain that drives domain ordering — naming which domains derive state from the source and in what sequence. This declaration justifies the artifact's structural choices before the trace begins.

Key distinctions:
- C-42 requires a domain-ordering rationale at each pass heading — C-50 requires a single artifact-level declaration covering all domains before any pass begins; C-42 without C-50 means per-pass justification with no artifact-level topology statement; C-50 without C-42 means the topology is declared upfront but individual pass headings lack their own ordering rationale; both are independent and additive
- C-41 requires cross-domain precondition chain annotations within bridge table rows — C-50 requires an upfront declaration of the dependency topology, not the per-row bridge annotations that implement it; C-41 and C-50 are independent
- The declaration must name the source-of-record domain explicitly (e.g., "Finance IS the source of revenue record") and trace the dependency chain to downstream domains (e.g., "Sales commitment state IS derived from Finance approval state"); generic language ("Finance comes first because it matters more") does not satisfy C-50
- IS-negation phrasing in the C-50 declaration (e.g., "Sales commitment state IS NOT valid until Finance approval IS recorded") simultaneously contributes to C-48 register saturation assessment
- Multi-domain only; single-domain traces cannot satisfy C-50
- PARTIAL: source-of-record domain is named but the dependency chain to downstream domains is absent or names only one downstream domain in a three-or-more domain trace

---

## Version History

| Version | Added | Pool | Unit |
|---------|-------|------|------|
| v01–v13 | C-09–C-35 (R1–R13 accumulated) | 27 | 1.85 |
| v14 | C-36, C-37 (R14) | 29 | 1.72 |
| v14–v15 | C-38–C-44 (R15) | 36 | 1.39 |
| v15 | C-45, C-46, C-47 (R16) | 38 | 1.32 |
| **v16** | **C-48, C-49, C-50 (R17)** | **41** | **1.22** |

---

*Rubric version: v16 | Pool: 41 aspirationals (C-09–C-50) | Aspirational unit: 50/41 ≈ 1.22 pts | PARTIAL unit: 0.61 pts | Essential unit: 10 pts × 5 = 50 pts | Total max: 100 | Golden threshold: 80*
