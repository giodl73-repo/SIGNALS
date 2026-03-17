Here is the complete updated rubric:

---

## trace-state · Rubric v17 — Summary

**Three R18 excellence signals → C-51, C-52, C-53. Pool 41 → 44. Unit: 50/44 ≈ 1.14 pts.**

---

### C-51 — Epoch arc-position structural role annotation *(format-neutral; tabular natural fit)*
**Source**: V-02 Signal "Arc Position column grounds C-49 remediation in epoch structural role." A dedicated column (tabular) or per-epoch structural role tag assigns each epoch its position in the lifecycle arc — Entry boundary, Gate boundary, Approval event, or Terminal settlement. Enables C-49 remediation implications to cite structural role rather than epoch name alone. Orthogonal to C-49: either can be satisfied without the other, but together they elevate remediation from epoch-name-grounded to epoch-role-grounded.

PARTIAL: Arc Position column or tags present, but fewer than all epoch rows carry a structural role annotation.

---

### C-52 — Cross-domain epoch vocabulary synthesis *(multi-domain only; requires C-49 per domain)*
**Source**: V-04 and V-05. The EPOCH-CLUSTER section synthesizes epoch vocabularies from ALL domains, identifies the highest-density epoch across the combined cross-domain vocabulary, and names a remediation implication at an inter-domain handoff boundary — not within a single domain's arc. The diagnostic insight C-52 unlocks: Finance and Sales defects that appear in separate epoch arcs may represent the same handoff failure, only visible through cross-domain synthesis.

PARTIAL: All domain vocabularies present in the analysis, highest-density epoch named, but remediation implication targets a within-domain epoch rather than a handoff boundary.

---

### C-53 — Named bridge structure for cross-domain precondition chain *(multi-pass only; extends C-41)*
**Source**: V-04 "Finance postcondition explicitly named as Sales precondition in BRIDGE TABLE" and V-05 "both bridge rows cited." The C-41 precondition chain is surfaced in a named, dedicated structure (BRIDGE TABLE or equivalent) with one row per inter-domain handoff, source-domain and target-domain labeled on each row, and the structure referenceable by C-47 confirmation annotations. Transforms C-41 from scattered inline annotations into a centralized dependency map. C-47 precision upgrade: confirmation notes can cite named bridge rows ("BRIDGE TABLE row F→S") rather than unnamed chain references.

PARTIAL: Named bridge structure present with at least one fully labeled handoff row, but fewer than all domain-to-domain handoffs represented in a 3+ domain trace.

---

**New scoring rules added:**
- C-51 and C-49 are orthogonal but synergistic — neither requires the other; together they activate role-grounded remediation
- C-52 requires C-49 as a prerequisite and multi-domain format — single-domain auto-FAIL
- C-53 requires C-41 as a prerequisite and multi-pass format — single-pass auto-FAIL
- C-47 does not require C-53 but C-53 raises C-47 citation precision; scorers should flag C-47 annotations that still use unnamed chain references when a BRIDGE TABLE row is available

---

**R18 scores under v17 (unit = 1.14):**

| Variant | New PASS | Total PASS | Score |
|---------|----------|------------|-------|
| V-01 (Sales, single-pass tabular) | — | 27 | **80.8** |
| V-02 (Finance, single-pass + Arc Position) | C-51 | 28 | **81.9** |
| V-03 (CS, step-block) | — | 27 | **80.8** |
| V-04 (Finance→Sales, two-pass) | C-52, C-53 | 36 | **91.0** |
| V-05 (Finance→Sales→CS, three-pass) | C-52, C-53 | 36 | **91.0** |

V-04 and V-05 tie at 36 PASS — three-pass depth increases quality in C-49/C-52/C-53 but not PASS count under current criteria. **R19 gap for both: C-51** — adding Arc Position structural role annotation yields 37 PASS = 92.2.

Written to `simulations/quest/rubrics/trace-state-rubric-v17-2026-03-15.md`.
lumn) gains C-51 PASS in addition to the 27-criterion baseline, yielding 28 PASS × 1.14 + 50 = **81.9**. Single-domain artifacts without Arc Position (V-01, V-03) score 27 PASS = **80.8**. Multi-domain artifacts (V-04, V-05) gain C-52 and C-53 over the v16 34-PASS baseline, yielding 36 PASS × 1.14 + 50 = **91.0**. The R19 axis is epoch arc-position structural role annotation for single-domain artifacts with C-49 but not C-51, plus C-51 integration into multi-domain traces that already carry C-52.

---

## Criteria Table

| Criterion | Description | Format constraint |
|-----------|-------------|-------------------|
| C-09 | (R1–R13 accumulated) | — |
| C-10 | (R1–R13 accumulated) | — |
| C-11 | (R1–R13 accumulated) | — |
| C-12 | (R1–R13 accumulated) | — |
| C-13 | (R1–R13 accumulated) | — |
| C-14 | (R1–R13 accumulated) | — |
| C-15 | (R1–R13 accumulated) | — |
| C-16 | (R1–R13 accumulated) | — |
| C-17 | (R1–R13 accumulated) | — |
| C-18 | (R1–R13 accumulated) | — |
| C-19 | (R1–R13 accumulated) | — |
| C-20 | (R1–R13 accumulated) | — |
| C-21 | (R1–R13 accumulated) | — |
| C-22 | (R1–R13 accumulated) | — |
| C-23 | (R1–R13 accumulated) | — |
| C-24 | (R1–R13 accumulated) | — |
| C-25 | (R1–R13 accumulated) | — |
| C-26 | (R1–R13 accumulated) | — |
| C-27 | (R1–R13 accumulated) | — |
| C-28 | (R1–R13 accumulated) | — |
| C-29 | (R1–R13 accumulated) | — |
| C-30 | Criterion-instruction fusion in column headers — column headers carry `[C-XX: directive]` | Tabular only |
| C-31 | (R1–R13 accumulated) | — |
| C-32 | (R1–R13 accumulated) | — |
| C-33 | (R1–R13 accumulated) | — |
| C-34 | Disqualification-condition fusion in column headers — headers carry `FAILS if:` patterns | Tabular only |
| C-35 | (R1–R13 accumulated) | — |
| C-36 | Pass-level defect hypothesis annotation — each pass heading names the defect class it targets | Multi-pass only |
| C-37 | Consequence clause at pass headings — `### Pass N [C-37: consequence clause]` | Multi-pass only |
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
| C-51 | Epoch arc-position structural role annotation — each epoch carries an Arc Position tag (Entry boundary / Gate boundary / Approval event / Terminal settlement), enabling role-grounded C-49 remediation implications | Format-neutral; tabular natural fit |
| C-52 | Cross-domain epoch vocabulary synthesis — EPOCH-CLUSTER section synthesizes epoch vocabularies from ALL domains, identifies highest-density epoch across the combined vocabulary, and names a remediation implication at an inter-domain handoff boundary | Multi-domain only |
| C-53 | Named bridge structure for cross-domain precondition chain — the C-41 precondition chain is surfaced in a named dedicated structure (e.g., BRIDGE TABLE) with source-domain + target-domain labeling on every handoff row, referenceable by C-47 annotations | Multi-pass only |

---

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
- C-51 and C-49 are orthogonal but synergistic — C-51 without C-49 means arc-position labels are present but never used as a defect analysis surface; C-49 without C-51 means defect clustering is present but remediation implications are epoch-name-grounded rather than epoch-role-grounded; satisfying both simultaneously elevates remediation specificity to role-grounded
- C-52 requires C-49 as a logical prerequisite — an artifact that has not satisfied single-domain C-49 cannot satisfy multi-domain C-52; C-52 is an extension of C-49 scope, not a replacement
- C-52 requires multi-domain format — single-domain artifacts score automatic FAIL regardless of EPOCH-CLUSTER depth or quality
- C-53 requires C-41 as a logical prerequisite — a BRIDGE TABLE structure without the underlying C-41 chain annotations does not satisfy C-53; the named structure must be the surface expression of the C-41 chain, not a substitute for it
- C-53 requires multi-pass format — single-pass artifacts score automatic FAIL
- C-47 citations gain specificity when C-53 is also satisfied — the confirmation note can cite named bridge rows (e.g., "BRIDGE TABLE row F→S") rather than unnamed chain references; C-47 does not require C-53 to be satisfied, but C-53 raises C-47 citation precision
- C-51 applied to multi-domain traces contributes to C-52 quality by providing role-anchors for the inter-domain handoff remediation implication, but C-51 and C-52 are independently scored — a multi-domain trace can satisfy C-52 without C-51 (cross-domain synthesis with generic epoch names) or C-51 without C-52 (arc-position labels present but epoch-cluster analysis confined to a single domain)

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

**C-47 (multi-pass only; requires C-40 + C-41 + C-42)**: The confirmation note must be specific. "Confirmed as predicted" does not satisfy C-47. The note must name: (1) the defect class named in the C-42 pass heading annotation, and (2) the bridge row or field from the C-41 chain (or C-53 BRIDGE TABLE row reference when present) that surfaced the dependency. A C-47-satisfying note reads: "Confirms revenue-leak defect class (C-42 prediction: pass 2) — triggered by bridge row Finance.Approved → Sales.Commit from C-41 bridge table."

**C-48 (format-neutral)**: Saturation means every section that carries a binding constraint, gate condition, role obligation, vocabulary prohibition, or forecast assertion uses IS/IS-NOT/IS-BLOCKED/IS-REQUIRED phrasing. PARTIAL credit if the register appears in a majority of binding sections but is absent from one or more named sections (e.g., IS-negation in the CONSTRAINT MATRIX and gates but passive-voice in the HANDOFF DECLARATION). Satisfying four or more individual IS-negation criteria from C-09–C-35 is a positive indicator but does not substitute for a holistic assessment of register coverage across the full artifact.

**C-49 (format-neutral; requires LIFECYCLE EPOCH MAP)**: The epoch-cluster analysis section must appear after the trace (not before), must enumerate defect findings by epoch using defect IDs from the FINDINGS section, must identify the highest-density epoch(s) by count, and must name a specific remediation implication tied to the epoch's position in the lifecycle arc (e.g., "CLOSE-TRACK epoch carries 3 of 4 defects — approval-gate hardening at the Negotiation → Close transition is the highest-leverage intervention"). Generic statements ("defects cluster in the middle phases") do not satisfy C-49. PARTIAL credit if defect-to-epoch mapping is present but the remediation implication is absent or generic. When C-51 is also satisfied, the remediation implication should cite the epoch's arc-position structural role to confirm synergy is activated — failure to do so when C-51 labels are present is a C-49 quality gap but does not retroactively fail C-49 itself.

**C-50 (multi-domain only)**: The declaration must appear before the first pass or domain column and must name: (1) the source-of-record domain (the domain whose state resolution other domains depend on), and (2) the dependency chain in natural-language form (e.g., "Finance IS the source of revenue record. Sales commitment state IS derived from Finance approval state. CS entitlement state IS derived from Sales commitment state."). A C-50 declaration using IS-negation register language simultaneously contributes to C-48 register saturation assessment. C-42 at pass headings names the per-pass ordering rationale; C-50 names the artifact-wide dependency topology. Both can be satisfied in the same artifact and do not cross-satisfy.

**C-51 (format-neutral; tabular natural fit)**: Arc Position tags must assign a structural role from the canonical vocabulary: Entry boundary, Gate boundary, Approval event, or Terminal settlement. Custom or narrative role labels ("where things start getting complex") do not satisfy C-51. In tabular format, the Arc Position column appears as a dedicated column adjacent to the epoch label or within the epoch cell. In step-block format, the structural role tag appears in the epoch header line. PARTIAL credit if the column or tags are present but fewer than all epoch rows carry a role assignment. When C-51 is satisfied alongside C-49, scorers should verify that C-49 remediation implications reference structural roles rather than epoch names alone to confirm synergy is activated.

**C-52 (multi-domain only; requires C-49 per domain and LIFECYCLE EPOCH MAP per domain)**: The cross-domain synthesis must cover ALL domains in the artifact — a two-of-three-domain analysis in a three-domain trace does not satisfy C-52. The inter-domain handoff remediation implication must name a specific handoff boundary (e.g., "Finance→Sales approval-commit synchronization point") as the defect concentration site, not a within-domain epoch. PARTIAL credit if all domain epoch vocabularies appear in the analysis but the highest-density epoch is named within a single domain (no cross-domain synthesis). Scorers should distinguish C-49 PASS (single-domain epoch cluster analysis) from C-52 PASS (cross-domain synthesis that yields an inter-domain handoff as the remediation target) — they are additive, not substitutable.

**C-53 (multi-pass only; requires C-41)**: The named structure must use an explicit heading or section label (BRIDGE TABLE or equivalent) visible to a reader scanning the artifact. A bridge annotation embedded in a cell of the trace table without a dedicated section heading does not satisfy C-53 even if the C-41 chain is present. Each row in the named structure must label the source domain and target domain explicitly (e.g., "Finance → Sales: Approved-quota IS the Sales.Commit precondition"). PARTIAL credit if the named structure is present with at least one fully labeled row but the structure is incomplete (missing rows for one or more inter-domain handoffs in a 3+ domain trace). When C-53 is satisfied, C-47 citations gain a precision upgrade opportunity — scorers should flag C-47 annotations that still use unnamed chain references when a BRIDGE TABLE row reference is available.

---

## Criterion Detail — C-51, C-52, C-53

### C-51 — Epoch arc-position structural role annotation *(format-neutral; tabular natural fit)*

**Source**: V-02 R18 Signal "Arc Position column (Entry boundary / Gate boundary / Approval event / Terminal settlement) grounds the C-49 remediation implication in epoch structural role."

A dedicated column (tabular format) or per-epoch structural role tag (step-block or other format) assigns each epoch its position in the lifecycle arc. The four canonical arc positions are:
- **Entry boundary** — the epoch where entities enter the tracked domain (lead capture, case open, invoice creation)
- **Gate boundary** — the epoch where a formal approval or qualification decision is made
- **Approval event** — the epoch where a binding commitment or authorization is issued
- **Terminal settlement** — the epoch where the entity exits the domain (closed won/lost, case resolved, payment settled)

The Arc Position annotation enables C-49 remediation implications to be role-grounded: "highest defect density is at the Gate boundary epoch — approval-gate hardening at this structural chokepoint is the targeted intervention" rather than naming only the epoch ("OPPORTUNITY-GATE epoch carries the most defects"). Role-grounded remediation is more portable across domain vocabulary changes and more precise for intervention targeting.

Key distinctions:
- C-43 requires lifecycle-phase labels in state cells (domain-recognizable vocabulary); C-51 requires arc-position structural role labels at the epoch level — they operate at different abstraction levels and are independent
- C-49 requires a post-trace defect analysis section; C-51 requires structural role tags on epoch entries; neither requires the other, but when both are present the C-49 remediation implication should incorporate the C-51 structural role vocabulary
- Format-neutral: the structural role tag can appear as a dedicated column in a tabular LIFECYCLE EPOCH MAP, as a parenthetical in an epoch heading, or as a labeled field in a step-block epoch declaration; the requirement is that every epoch carries a structural role assignment

---

### C-52 — Cross-domain epoch vocabulary synthesis *(multi-domain only; requires C-49 and LIFECYCLE EPOCH MAP per domain)*

**Source**: V-04 R18 "EPOCH-CLUSTER spans both Finance and Sales epoch vocabularies; highest-density epoch named; cross-domain remediation implication" and V-05 R18 "EPOCH-CLUSTER spans three epoch vocabularies; remediation implication names the inter-domain handoff as the defect concentration boundary."

In a multi-domain trace, the EPOCH-CLUSTER section is extended from single-domain analysis to cross-domain synthesis by:
1. Enumerating defect findings across ALL domain epoch vocabularies (not just the primary domain)
2. Computing defect density across the combined multi-domain vocabulary to identify the highest-density epoch regardless of which domain it belongs to
3. Drawing a remediation implication that targets an inter-domain handoff boundary as the defect concentration site

The diagnostic value of cross-domain synthesis is that inter-domain handoffs are structurally invisible when each domain's EPOCH-CLUSTER is analyzed separately — a Finance defect in the APPROVAL-EVENT epoch and a Sales defect in the COMMIT epoch may represent the same Finance→Sales handoff failure, only visible when both epoch vocabularies are synthesized.

Key distinctions:
- C-49 (single-domain) requires defect-to-epoch mapping + highest-density epoch + targeted remediation; C-52 extends this to cross-domain scope and specifically requires the remediation implication to cross a domain boundary — an EPOCH-CLUSTER that analyzes Finance and Sales epochs separately and names a Finance epoch as highest-density with a Finance-internal remediation implication satisfies C-49 twice but not C-52
- C-52 PARTIAL: all domain epoch vocabularies present in the analysis, highest-density epoch named, but remediation implication stays within a single domain without naming an inter-domain handoff boundary
- Multi-domain only; single-domain artifacts auto-FAIL

---

### C-53 — Named bridge structure for cross-domain precondition chain *(multi-pass only; extends C-41)*

**Source**: V-04 R18 "Finance postcondition explicitly named as Sales precondition in BRIDGE TABLE" and V-05 R18 "both bridge rows cited" (Finance→Sales and Sales→CS).

C-41 requires that the postcondition of pass N be explicitly named as the precondition feeding pass N+1. C-53 requires that this chain be surfaced in a named, dedicated structure — a BRIDGE TABLE or equivalent — with the following properties:
- A section-level heading or label that identifies it as the bridge structure
- One row per inter-domain handoff (all domain-to-domain transitions represented)
- Each row explicitly names the source domain, the postcondition state, the target domain, and the precondition state
- The structure is positioned such that it can be cited by reference (e.g., "BRIDGE TABLE row F→S") from C-47 confirmation annotations

A BRIDGE TABLE transforms C-41 from scattered inline annotations into a centralized, referenceable dependency map. This is significant for C-47: confirmation notes can cite specific bridge rows by name, yielding precise defect-class hypothesis confirmations rather than generic chain references.

Key distinctions:
- C-41 without C-53: precondition chain exists as inline bridge fields, postcondition annotations, or pass-heading notes — present and satisfying C-41 but not gathered into a named structure
- C-53 without C-41: a BRIDGE TABLE heading with no underlying explicit chain annotations does not satisfy C-53 — the chain must exist (C-41 satisfied) before the structure that names it earns credit
- In a three-or-more-domain trace (e.g., Finance → Sales → CS), the BRIDGE TABLE must contain rows for Finance→Sales AND Sales→CS to earn full C-53 credit; missing any inter-domain handoff earns PARTIAL
- C-53 is multi-pass only; single-pass artifacts auto-FAIL (there is no inter-domain chain to name)

---

## Version History

| Version | Added | Pool | Unit |
|---------|-------|------|------|
| v01–v13 | C-09–C-35 (R1–R13 accumulated) | 27 | 1.85 |
| v14 | C-36, C-37 (R14) | 29 | 1.72 |
| v14–v15 | C-38–C-44 (R15) | 36 | 1.39 |
| v15 | C-45, C-46, C-47 (R16) | 38 | 1.32 |
| v16 | C-48, C-49, C-50 (R17) | 41 | 1.22 |
| **v17** | **C-51, C-52, C-53 (R18)** | **44** | **1.14** |

---

## trace-state · R18 Score · Rubric v17

**Scoring baseline:** R17 V-01 rescored under v17 unit (1.14): 26 PASS × 1.14 + 50 = **79.6**. R18 scores follow below.

---

### V-01 — Sales, single-pass tabular

| Criterion | Result | Note |
|-----------|--------|------|
| C-30 | PASS | Column headers carry criterion IDs + directives |
| C-34 | PASS | `FAILS if:` patterns in headers |
| C-36, C-37, C-40, C-41, C-42, C-47 | FAIL | Multi-pass format required |
| C-38, C-39 | FAIL | Step-block format required |
| C-43 | PASS | Lead → Opportunity → Closed Won labels in cells |
| C-44 | PASS | Sub-step decomposition present |
| C-45 | PASS | Pre-Defect / Triggering Op / Post-Defect+Reason |
| C-46 | PASS | Phase vocabulary declared before table |
| C-48 | PASS | IS/IS-NOT/IS-BLOCKED across all constraint-carrying sections |
| C-49 | PASS | EPOCH-CLUSTER ANALYSIS section maps F-NN → epoch, names highest-density epoch, states targeted remediation implication |
| C-50 | FAIL | Single-domain |
| C-51 | FAIL | No Arc Position structural role column present |
| C-52 | FAIL | Single-domain |
| C-53 | FAIL | Single-pass |
| R1–C-28 accumulated | ~23 PASS | Confirmed by R17 baseline |

**PASS count:** 27 · **Score:** 50 + 27 × 1.14 = **80.8**

---

### V-02 — Finance, single-pass tabular + Arc Position column

Arc Position column (Entry boundary / Gate boundary / Approval event / Terminal settlement) grounds the C-49 remediation implication in epoch structural role — remediation specificity elevated above generic.

| Criterion | Result | Note |
|-----------|--------|------|
| C-48 | PASS | IS-NOT register in GATE definitions, FINDINGS preamble, EPOCH-CLUSTER preamble |
| C-49 | PASS | Arc Position column enables epoch-role-specific remediation (not generic) |
| C-50 | FAIL | Single-domain |
| C-51 | PASS | Arc Position column present; all epoch rows carry structural role annotation |
| C-52 | FAIL | Single-domain |
| C-53 | FAIL | Single-pass |

**PASS count:** 28 · **Score:** 50 + 28 × 1.14 = **81.9**
*(Arc Position elevates both C-49 remediation quality and earns independent C-51 credit)*

---

### V-03 — Customer Service, step-block format

Swaps tabular criteria for step-block analogs. C-49 delivered as labeled step-block (ECL-1 through ECL-4). No Arc Position structural role tags evidenced in step-block ECL entries.

| Criterion | Result | Note |
|-----------|--------|------|
| C-30 | FAIL | Tabular format not used |
| C-34 | FAIL | Tabular format not used |
| C-38 | PASS | Step labels carry `[C-XX: directive]` |
| C-39 | PASS | Step labels carry `FAILS if:` pattern |
| C-48 | PASS | Register saturates all constraint-carrying sections including ECL preamble |
| C-49 | PASS | ECL-1 → ECL-4 step-block satisfies format-neutral C-49 requirement |
| C-50 | FAIL | Single-domain |
| C-51 | FAIL | No structural role tags evidenced in ECL epoch entries |
| C-52 | FAIL | Single-domain |
| C-53 | FAIL | Single-pass |

Net swap from V-01: C-30/C-34 → C-38/C-39. Count unchanged.

**PASS count:** 27 · **Score:** 50 + 27 × 1.14 = **80.8**

---

### V-04 — Finance → Sales, two-pass multi-domain

Multi-pass unlocks C-36, C-37, C-40, C-41, C-42, C-47. Multi-domain unlocks C-50. BRIDGE TABLE unlocks C-53. Cross-domain EPOCH-CLUSTER unlocks C-52.

| Criterion | Result | Note |
|-----------|--------|------|
| C-36 | PASS | Pass headings name defect class targeted |
| C-37 | PASS | Consequence clause at each pass heading |
| C-40 | PASS | One distinct labeled defect per domain pass with type + triggering op + reason |
| C-41 | PASS | Finance postcondition explicitly named as Sales precondition in BRIDGE TABLE |
| C-42 | PASS | Finance-first ordering annotated as defect-class hypothesis vehicle |
| C-47 | PASS | Defect-hypothesis confirmation cites predicted class from C-42 + bridge row from C-41 |
| C-48 | PASS | IS-negation register + C-50 declaration written in IS-NOT form |
| C-49 | PASS | EPOCH-CLUSTER spans both Finance and Sales epoch vocabularies; highest-density epoch named; cross-domain remediation implication |
| C-50 | PASS | Top-scope DOMAIN DEPENDENCY DECLARATION before Pass 1: Finance IS the state authority → Sales IS the downstream consumer; two-hop chain complete |
| C-51 | FAIL | Arc Position structural role column not evidenced |
| C-52 | PASS | EPOCH-CLUSTER synthesizes Finance + Sales epoch vocabularies; inter-domain Finance→Sales handoff named as defect concentration boundary |
| C-53 | PASS | BRIDGE TABLE present; Finance→Sales handoff row explicitly labels source domain, postcondition, target domain, precondition |

+6 multi-pass (C-36, C-37, C-40, C-41, C-42, C-47) + C-50 + C-52 + C-53 vs V-01 base of 27.

**PASS count:** 36 · **Score:** 50 + 36 × 1.14 = **91.0**

---

### V-05 — Finance → Sales → CS, three-pass multi-domain

Full three-pass synthesis. C-50 explicitly names all three domains and both dependency hops, directly targeting the PARTIAL boundary. C-52 inter-domain remediation implication names the Finance→Sales handoff as the defect concentration boundary across the three-domain vocabulary. C-53 BRIDGE TABLE carries both Finance→Sales and Sales→CS rows — full credit for three-domain trace.

| Criterion | Result | Note |
|-----------|--------|------|
| C-36 | PASS | Three pass headings, each with defect class |
| C-37 | PASS | Three consequence clauses |
| C-40 | PASS | Three distinct labeled defects (one per pass) |
| C-41 | PASS | Finance→Sales bridge + Sales→CS bridge, both explicit |
| C-42 | PASS | Three-pass ordering annotated as hypothesis vehicle |
| C-47 | PASS | Both bridge rows cited; three defect-hypothesis confirmations present |
| C-48 | PASS | IS-negation saturates DOMAIN DEPENDENCY DECLARATION + all three GATE definitions + FINDINGS preamble + EPOCH-CLUSTER preamble |
| C-49 | PASS | EPOCH-CLUSTER spans three epoch vocabularies; cross-domain highest-density epoch identified; remediation implication names the inter-domain handoff as the defect concentration boundary |
| C-50 | PASS | Full chain declared: "Finance IS the state authority; Sales IS NOT independent — it IS the Finance-downstream consumer; CS IS the terminal settlement domain dependent on both" |
| C-51 | FAIL | Arc Position structural role column not evidenced |
| C-52 | PASS | Three-domain epoch vocabulary synthesis; inter-domain handoff as defect concentration boundary explicitly named |
| C-53 | PASS | BRIDGE TABLE carries Finance→Sales row and Sales→CS row; both domain-to-domain handoffs represented; C-47 citations reference named rows |

C-50 PARTIAL risk (fewer than all downstream domains named) explicitly avoided by naming all three.

**PASS count:** 36 · **Score:** 50 + 36 × 1.14 = **91.0**

*(V-04 and V-05 reach the same score under v17 — the three-pass depth of V-05 increases C-49/C-52/C-53 quality depth but does not increase PASS count under current criteria. The R19 gap for both is C-51: adding Arc Position structural role annotation would yield 37 PASS = 92.2.)*

---

*Rubric version: v17 | Pool: 44 aspirationals (C-09–C-53) | Aspirational unit: 50/44 ≈ 1.14 pts | PARTIAL unit: 0.57 pts | Essential unit: 10 pts × 5 = 50 pts | Total max: 100 | Golden threshold: 80*
