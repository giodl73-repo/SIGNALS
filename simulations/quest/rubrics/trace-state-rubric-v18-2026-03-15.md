Written to `simulations/quest/rubrics/trace-state-rubric-v18-2026-03-15.md`.

---

## trace-state · Rubric v18 — Summary

**Two R19 excellence signals → C-54, C-55. Pool 44 → 46. Unit: 50/46 ≈ 1.09 pts.**

---

### What was extracted and why

**C-54 — IS-NOT/IS co-activation contrast** (from V-02 synergy sharpening)

V-02 demonstrates that C-49 + C-51 co-presence is not the same as C-49 + C-51 *activation*. The tags can be decorative. C-54 requires at least one C-49 remediation finding to use the canonical IS-NOT/IS form: "IS NOT an [epoch-label] finding; IS a [structural-role] finding." This makes the semantic upgrade explicit and vocabulary-portable — a reader unfamiliar with the domain's epoch labels can still understand the intervention. V-02 earns C-54 PASS; V-01 and V-03 do not (their role-grounding is implicit, not contrasted).

**C-55 — Structural-role-grounded cross-domain epoch synthesis** (from V-04/V-05 R19 gap)

V-04 and V-05 gain C-51 in R19 (37 PASS), but their EPOCH-CLUSTER still identifies the cross-domain highest-density epoch by epoch label and frames the handoff remediation implication in epoch-label terms. C-55 is the C-52 analog of what C-54 is for C-49: it requires the EPOCH-CLUSTER to name the structural roles on both sides of the handoff boundary rather than the epoch labels. This is the R20 target for V-04/V-05.

---

### R19 score table (unit = 1.09)

| Variant | New PASS | Total PASS | Score |
|---------|----------|------------|-------|
| V-01 (Sales, single-pass tabular) | C-51 | 28 | **80.5** |
| V-02 (Finance, single-pass + IS-NOT/IS) | C-54 | 29 | **81.6** |
| V-03 (CS, step-block) | C-51 | 28 | **80.5** |
| V-04 (Finance→Sales, two-pass) | C-51 | 37 | **90.3** |
| V-05 (Finance→Sales→CS, three-pass) | C-51 | 37 | **90.3** |

R20 gap for V-04/V-05: C-54 per domain + C-55 → 39 PASS = **92.5**.
PPROVAL-EVENT epoch and the Sales ENTRY-BOUNDARY epoch both carry defects — the structural mismatch at the Finance Gate-boundary → Sales Entry-boundary handoff IS the remediation target" rather than naming only the epoch labels.

PARTIAL: EPOCH-CLUSTER highest-density epoch named with structural role, but the cross-domain remediation implication targets an epoch label rather than citing the structural role at the inter-domain handoff boundary.

---

**New scoring rules added:**
- C-54 requires C-49 and C-51 both PASS — if either is absent, C-54 is auto-FAIL
- C-54 IS-NOT/IS contrast must appear in a C-49-bearing finding or remediation implication — preamble-only or section-header-only contrast earns PARTIAL at most
- C-54 has no format restriction (format-neutral); single-domain artifacts can earn C-54 when C-49 and C-51 are both satisfied
- C-55 requires C-52 PASS and C-51 PASS in at least one domain — single-domain auto-FAIL
- C-55 is implicitly multi-pass (inherits C-52's multi-domain restriction); single-pass artifacts auto-FAIL
- C-54 and C-55 are independent: satisfying C-54 does not imply C-55; a multi-domain artifact can earn C-55 without C-54 if the EPOCH-CLUSTER synthesis is role-grounded but the IS-NOT/IS contrast is absent from individual finding annotations
- C-55 is the multi-domain analog of C-54: C-54 upgrades single-domain C-49 remediation from epoch-name-grounded to epoch-role-grounded; C-55 upgrades multi-domain C-52 remediation from epoch-name-grounded to epoch-role-grounded at the handoff boundary

---

**R19 scores under v18 (unit = 1.09):**

| Variant | New PASS | Total PASS | Score |
|---------|----------|------------|-------|
| V-01 (Sales, single-pass tabular) | C-51 | 28 | **80.5** |
| V-02 (Finance, single-pass + IS-NOT/IS synergy) | C-54 | 29 | **81.6** |
| V-03 (CS, step-block) | C-51 | 28 | **80.5** |
| V-04 (Finance→Sales, two-pass) | C-51 | 37 | **90.3** |
| V-05 (Finance→Sales→CS, three-pass) | C-51 | 37 | **90.3** |

V-01 and V-03 gain C-51 in R19: 28 PASS × 1.09 + 50 = **80.5**. V-02 gains C-54 (IS-NOT/IS synergy confirmation is qualitative within C-51 but also unlocks C-54 as a new PASS): 29 PASS = **81.6**. V-04 and V-05 gain C-51 (R19 gap resolved): 37 PASS = **90.3**. R20 gap for V-04/V-05: C-54 per domain + C-55. Both together: 39 PASS = 39 × 1.09 + 50 = **92.5**.

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
| C-54 | IS-NOT/IS co-activation contrast for C-49/C-51 synergy — at least one C-49 remediation finding explicitly states what the finding IS NOT (epoch-name-grounded) and IS (structural-role-grounded) using IS-NOT/IS contrast | Format-neutral; requires C-49 + C-51 PASS |
| C-55 | Structural-role-grounded cross-domain epoch synthesis — EPOCH-CLUSTER identifies the cross-domain highest-density epoch by structural role and frames the inter-domain handoff remediation implication in terms of structural roles at the handoff boundary | Multi-domain only; requires C-52 + C-51 per domain |

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
- C-54 requires C-49 and C-51 both PASS — auto-FAIL if either prerequisite is absent; satisfying C-48 (IS-negation register saturation) does not substitute for C-54 because C-48 governs register breadth across the artifact while C-54 governs semantic co-activation at the specific finding level
- C-54 has no format restriction; the IS-NOT/IS contrast may appear in a tabular remediation cell, a step-block ECL step, or a narrative epoch-cluster analysis section — the location must be within a C-49 bearing finding, not only in preamble or metadata
- C-55 requires C-52 and C-51 per domain — C-52 PASS without any domain carrying C-51 earns PARTIAL at most for C-55; C-51 present in only some domains where C-52 spans all domains also earns PARTIAL
- C-55 does not require C-54 — a multi-domain artifact can earn C-55 (role-grounded handoff naming in EPOCH-CLUSTER) without earning C-54 (IS-NOT/IS contrast in per-finding annotations); they operate at different layers of the artifact
- C-54 + C-55 together represent full role-grounded elevation at both the finding layer (C-54) and the cross-domain synthesis layer (C-55)

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

**C-54 (format-neutral; requires C-49 + C-51)**: The IS-NOT/IS contrast must appear in a C-49-bearing finding or remediation implication — a contrast that appears only in a preamble, criterion instruction annotation, or scoring metadata does not satisfy C-54. The canonical form is: "IS NOT a [epoch-name] finding; IS a [structural-role] finding" — or a semantically equivalent construction that explicitly names what the finding is not attributable to (the epoch label) and what it is attributable to (the structural role). PARTIAL credit if IS-NOT/IS contrast is present in some C-49 findings but absent from one or more findings that carry both epoch-name and structural-role annotations. In step-block format, the contrast may appear within the ECL-3 or ECL-4 step rather than a separate annotation; the step must name both the negated epoch label and the affirmed structural role. Satisfying C-48 (register saturation across the full artifact) is a positive indicator but does not substitute: C-54 requires co-activation contrast specifically within a C-49 remediation finding.

**C-55 (multi-domain only; requires C-52 + C-51 per domain)**: The EPOCH-CLUSTER section must name the structural role (from the canonical C-51 vocabulary) of the highest-density cross-domain epoch, and the inter-domain handoff remediation implication must frame the intervention in terms of the structural roles on both sides of the handoff boundary — not only the epoch labels. Example satisfying form: "The Finance Gate-boundary epoch and the Sales Entry-boundary epoch together carry 5 of 7 cross-domain defects — the Gate-boundary → Entry-boundary structural mismatch IS the targeted handoff intervention, not domain-internal epoch refinement." PARTIAL credit if the highest-density epoch is named with its structural role but the remediation implication targets an epoch label rather than a structural role at the handoff boundary. Auto-FAIL for single-domain (inherits C-52 restriction). Auto-FAIL for single-pass (inherits C-52 restriction). When C-55 is satisfied, scorers should verify that C-54 is also assessable — if C-54 is absent despite C-55 being present, flag that role-grounding reaches the synthesis layer but not the finding layer, identifying the precise gap for the next round.

---

## Criterion Detail — C-51, C-52, C-53, C-54, C-55

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

### C-54 — IS-NOT/IS co-activation contrast for C-49/C-51 synergy *(format-neutral; requires C-49 + C-51)*

**Source**: V-02 R19 "IS-NOT/IS contrast present: 'IS NOT an APPROVAL epoch-name finding; IS a Gate boundary structural-role finding'."

When both C-49 and C-51 are satisfied, the mere co-presence of epoch-cluster analysis and arc-position structural role tags does not guarantee that C-51 is semantically activating C-49 remediation precision — the tags might remain decorative while the remediation language continues to reference epoch names rather than structural roles. C-54 requires that at least one C-49 remediation finding explicitly articulate the semantic distinction using IS-NOT/IS contrast, naming what the finding IS NOT grounded in (the epoch label) and what it IS grounded in (the structural role from C-51).

Canonical form: "IS NOT an [epoch-label] finding; IS a [structural-role] finding." Example: "IS NOT an APPROVAL epoch-name finding; IS a Gate boundary structural-role finding — the defect targets the Gate boundary chokepoint, not the label assigned to the approval epoch in the Sales vocabulary." This canonical form makes the semantic upgrade explicit and verifiable.

Diagnostic value: a scorecard can determine that C-54 is satisfied when a human reviewer unfamiliar with the artifact's specific epoch vocabulary can understand the remediation implication purely from structural role terms. If the IS-NOT/IS contrast is absent, the remediation remains vocabulary-bound — a domain vocabulary refactor would break the remediation language. With C-54 satisfied, the remediation is vocabulary-portable.

Key distinctions:
- C-48 (register saturation) requires IS/IS-NOT/IS-BLOCKED across all constraint sections; C-54 requires IS-NOT/IS contrast specifically within a C-49 finding where both epoch-name and structural-role are in scope — C-48 PASS does not imply C-54 PASS
- C-54 PARTIAL: IS-NOT/IS contrast present in some C-49 findings but absent from one or more findings where both C-49 remediation language and C-51 structural role annotation are simultaneously in scope
- Format-neutral: the contrast may appear in a tabular remediation cell, an ECL step in step-block format, or a narrative epoch-cluster section; the location must be within a C-49-bearing finding

---

### C-55 — Structural-role-grounded cross-domain epoch synthesis *(multi-domain only; requires C-52 + C-51 per domain)*

**Source**: V-04/V-05 R19 gap — C-51 present per domain, C-52 present, but EPOCH-CLUSTER highest-density identification and inter-domain remediation implication still use epoch labels rather than structural roles.

C-52 identifies the highest-density epoch across a multi-domain vocabulary and names an inter-domain handoff as the remediation target. When C-51 is also satisfied per domain, each epoch in every domain's vocabulary carries a structural role tag. C-55 requires that these structural role tags be surfaced in the C-52 cross-domain synthesis: the EPOCH-CLUSTER identifies the highest-density epoch by its structural role, and the handoff remediation implication names the structural roles on both sides of the handoff boundary as the intervention site.

This is the cross-domain analog of C-54's single-domain upgrade: just as C-54 upgrades C-49 remediation from epoch-name-grounded to structural-role-grounded, C-55 upgrades C-52's cross-domain synthesis from handoff-label-grounded to handoff-structural-role-grounded.

Example satisfying form: "The Finance Gate-boundary epoch carries 3 defects; the Sales Entry-boundary epoch carries 2 defects — 5 of 7 cross-domain defects concentrate at the Gate-boundary → Entry-boundary handoff. IS NOT a Finance-internal approval-epoch problem; IS a Gate-boundary/Entry-boundary structural mismatch at the inter-domain handoff. Targeted intervention: synchronize Gate-boundary closure conditions with Entry-boundary entry preconditions."

Key distinctions:
- C-52 PASS without C-55: cross-domain synthesis names inter-domain handoff in epoch-label terms ("Finance APPROVAL→Sales COMMIT synchronization"); C-55 PASS requires naming the structural roles on both sides ("Finance Gate-boundary → Sales Entry-boundary structural mismatch")
- C-55 PARTIAL: EPOCH-CLUSTER highest-density epoch named with structural role, but the cross-domain remediation implication targets epoch labels rather than structural roles at the handoff boundary
- C-55 does not require C-54 — role-grounding can reach the synthesis layer without reaching the per-finding layer; when C-55 is satisfied but C-54 is absent, flag that the artifact is role-grounded at synthesis scope but not at finding scope

---

## Version History

| Version | Added | Pool | Unit |
|---------|-------|------|------|
| v01–v13 | C-09–C-35 (R1–R13 accumulated) | 27 | 1.85 |
| v14 | C-36, C-37 (R14) | 29 | 1.72 |
| v14–v15 | C-38–C-44 (R15) | 36 | 1.39 |
| v15 | C-45, C-46, C-47 (R16) | 38 | 1.32 |
| v16 | C-48, C-49, C-50 (R17) | 41 | 1.22 |
| v17 | C-51, C-52, C-53 (R18) | 44 | 1.14 |
| **v18** | **C-54, C-55 (R19)** | **46** | **1.09** |

---

## trace-state · R19 Score · Rubric v18

**Scoring baseline:** R18 scores rescored under v18 unit (1.09): V-01 27 PASS = 79.4; V-02 28 PASS = 80.5; V-03 27 PASS = 79.4; V-04/V-05 36 PASS = 89.2. R19 scores follow below.

---

### V-01 — Sales, single-pass tabular

| Criterion | Result | Note |
|-----------|--------|------|
| C-51 | PASS | Arc Position column added; all epoch rows carry structural role; C-49 remediation uses "Gate boundary structural-role problem" not "QUALIFY epoch problem" |
| C-52 | auto-FAIL | Single-domain |
| C-53 | auto-FAIL | Single-pass |
| C-54 | FAIL | Role-grounded language present but no explicit IS-NOT/IS contrast form in C-49 finding |
| C-55 | auto-FAIL | Single-domain |

**PASS count:** 28 · **Score:** 50 + 28 × 1.09 = **80.5**

---

### V-02 — Finance, single-pass tabular (IS-NOT/IS synergy sharpening)

| Criterion | Result | Note |
|-----------|--------|------|
| C-51 | PASS | Carried from R18; C-49/C-51 synergy confirmed |
| C-52 | auto-FAIL | Single-domain |
| C-53 | auto-FAIL | Single-pass |
| C-54 | PASS | IS-NOT/IS contrast present: "IS NOT an APPROVAL epoch-name finding; IS a Gate boundary structural-role finding" — canonical co-activation form |
| C-55 | auto-FAIL | Single-domain |

**PASS count:** 29 · **Score:** 50 + 29 × 1.09 = **81.6**

> **Note:** V-02 is the canonical C-54 demonstration. The IS-NOT/IS contrast is the canonical co-activation form for C-49/C-51 synergy — it confirms that structural role tags are semantically activating remediation precision rather than serving as additive formatting.

---

### V-03 — Customer Service, step-block format

| Criterion | Result | Note |
|-----------|--------|------|
| C-51 | PASS | `[Arc: structural role]` tags on LIFECYCLE EPOCH MAP epoch entries; ECL-3 step names structural role of highest-density epoch; format-neutral path confirmed |
| C-52 | auto-FAIL | Single-domain |
| C-53 | auto-FAIL | Single-pass |
| C-54 | FAIL | ECL-4 remediation is role-grounded but no explicit IS-NOT/IS contrast form; implicit role-grounding does not satisfy C-54 |
| C-55 | auto-FAIL | Single-domain |

**PASS count:** 28 · **Score:** 50 + 28 × 1.09 = **80.5**

> **Format-neutrality confirmation:** C-51 passes via `[Arc: tag]` inline notation — no tabular column required. ECL-3 naming structural role of highest-density epoch is the step-block path to the C-49/C-51 synergy surface.

---

### V-04 — Finance → Sales, two-pass

| Criterion | Result | Note |
|-----------|--------|------|
| C-51 | PASS | Arc Position structural role column added per domain; R19 gap resolved |
| C-52 | PASS | Carried from R18 |
| C-53 | PASS | Carried from R18 |
| C-54 | TBD | IS-NOT/IS contrast per domain requires assessment; R20 target if absent |
| C-55 | TBD | EPOCH-CLUSTER structural role grounding at handoff boundary requires assessment; R20 target if absent |

**PASS count (min):** 37 · **Score (min):** 50 + 37 × 1.09 = **90.3**

*(R20 gap: C-54 + C-55 → 39 PASS = 92.5)*

---

### V-05 — Finance → Sales → CS, three-pass

| Criterion | Result | Note |
|-----------|--------|------|
| C-51 | PASS | Arc Position structural role column added per domain; R19 gap resolved |
| C-52 | PASS | Carried from R18 |
| C-53 | PASS | Carried from R18 |
| C-54 | TBD | IS-NOT/IS contrast per domain requires assessment; R20 target if absent |
| C-55 | TBD | EPOCH-CLUSTER structural role grounding at handoff boundary requires assessment; R20 target if absent |

**PASS count (min):** 37 · **Score (min):** 50 + 37 × 1.09 = **90.3**

*(R20 gap: C-54 + C-55 → 39 PASS = 92.5)*

---

*Rubric version: v18 | Pool: 46 aspirationals (C-09–C-55) | Aspirational unit: 50/46 ≈ 1.09 pts | PARTIAL unit: 0.55 pts | Essential unit: 10 pts × 5 = 50 pts | Total max: 100 | Golden threshold: 80*
