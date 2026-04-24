Written to `simulations/quest/rubrics/trace-inspect-rubric-v12-2026-03-17.md`.

---

**New criteria extracted from R15:**

| ID | Name | Pattern | Source |
|----|------|---------|--------|
| C-34 | **Inertia bilateral closure** | When both C-32 and C-33 are satisfied, both INERTIA entries must appear in the same named INERTIA block. V-01 and V-02 each closed only one item — leaving the INERTIA block asymmetrically closed — while V-03 closed both in the same pass, signaling that C-30/C-31 are a structural pair, not independent items. | V-03 vs V-01/V-02 in R15 |
| C-35 | **Inertia consequence clause** | The why-sentence in both C-32 and C-33 INERTIA items must conclude with an explicit structural consequence clause naming what the mechanism makes visible, impossible, or self-certifying. V-03's forms: *"making phantom references visible regardless of count correctness"* / *"make each block self-certifying without a manual document scan."* A why-sentence that explains the mechanism without asserting its consequence fails. | V-03 in R15 |

**Grand total**: 105.5 + 0.5 + 0.5 = **106.5**

**Design logic:** C-34 mirrors C-27's PROMOTION COMPLETENESS GATE principle — just as all SA gaps must complete their lifecycle together, all INERTIA closure items for a structural pair must be co-present. C-35 addresses the same durability gap one level deeper: an INERTIA item that explains *what* the mechanism does but not *what property it guarantees* forces a future maintainer to reason from mechanism to consequence themselves. The consequence clause makes the durability claim directly verifiable.
--------|--------|----------|----------------|
| C-01 | **Phase completeness** | essential | correctness | All four phases are present and structurally closed. Phase 1 (Setup) produces per-role schema binding blocks with explicit Schema 1 and Schema 2 binding fields and per-role gap attribution. Phase 2 (Execute) runs at least one role relay. Phase 3 (Findings) runs all four sub-steps in order (3a -> 3b -> 3c -> 3d). Phase 4 (Amend) produces at least one change or dismissal entry. A trace missing any phase, or a phase present but producing no required output, fails. |
| C-02 | **Artifact produced** | essential | correctness | Phase 2 (Execute) writes a hand-compiled artifact file at `simulations/trace/skill/{topic}-skill-trace-{date}.md` (or equivalent declared path). The artifact contains every section the skill's artifact contract requires. An Execute phase that produces role relays without a written artifact fails. |
| C-03 | **Schema 1 + Schema 2 compliance** | essential | correctness | Every severity label used anywhere in the trace is from {P1, P2, P3}. Every Source label used anywhere in the trace is from {SA, SG, EG, QO}. A promoted SA gap uses the SG label in all phases after SA-TO-SG PROMOTION. Any label outside these sets, or a promoted gap retaining SA, is a structural violation and fails this criterion. |
| C-04 | **Enforcement gates checked** | essential | behavior | Step 3c records an explicit PASS or FAIL result for each of G-1, G-2, and G-3. G-1: >= 2 distinct Source types in Step 3b table. G-2: no two same-Source findings share identical Action text. G-3: all Step 3b entries use only {P1, P2, P3}. A trace where any gate is omitted, implicitly assumed to pass, or advanced past despite a FAIL result fails this criterion. |
| C-05 | **Verdict present and classified** | essential | correctness | Phase 5 (or Verdict section) delivers one of three classifications: USEFUL, NEEDS-REDESIGN, or NEEDS-SPEC-REVISION, with the decision rationale. The classification follows the defined rules: NEEDS-SPEC-REVISION if any P1 SA gap remains SA after promotion; NEEDS-REDESIGN if EG gaps exceed 3 and indicate a structural role gap; USEFUL otherwise. A trace ending without a verdict, or with a verdict that contradicts the gap inventory, fails. |

---

## Recommended Criteria

> Output is better with these. Failing one degrades quality but does not make the trace
> useless.

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-06 | **SA-TO-SG promotion evaluated** | recommended | depth | Every SA gap from the Stage 1 relay is evaluated at the SA-TO-SG PROMOTION lifecycle event. Each gap records PROMOTES TO SG or REMAINS SA with a one-sentence reason. The post-promotion inventory states SA remaining count and SG from promotion count. A trace with SA gaps that skip this evaluation, or where all SA gaps silently disappear without a promotion record, fails this criterion. |
| C-07 | **Per-role relays complete** | recommended | coverage | Each role in the execution sequence has a relay in Phase 2 with all required fields: Received from, Received values, Schema 2 compliance (Source labels used and YES/NO conformance), SA/SG gaps affecting this role, Produced (artifact content added), EG gaps encountered. A relay missing the "Schema 2 compliance" field, or a relay summarized as "role ran normally" without field-level detail, fails this criterion. |
| C-08 | **Findings table depth** | recommended | depth | The Step 3b findings table contains >= 3 distinct findings covering at least 2 different Source types. Each finding has a distinct Action (not a restatement of the finding). A table with only spec-layer (SA) findings or only execution-layer (EG) findings, or with Action cells that repeat the Finding text verbatim, fails this criterion. |

---

## Aspirational Criteria

> Raise the bar once essential and recommended are stable. C-09 and C-10 were present in v1.
> C-11, C-12, and C-13 were added in v2 from R1 excellence signals. C-14 was added in v3 from
> R2 signals. C-15 through C-18 were added in v4 from R6 signals. C-19 through C-21 were added
> in v5 from R7 signals. C-22 and C-23 were added in v6 from R9 excellence signals. C-24 and
> C-25 were added in v7 from R10 excellence signals (V-05 structural linkage moves exceeding the
> base combination of C-22 + C-23). C-26 and C-27 were added in v8 from R11 excellence signals:
> C-26 from the NEEDS-REDESIGN EVIDENCE ANCHOR pattern (V-01/V-04/V-05 in R11) and C-27 from
> the PROMOTION COMPLETENESS GATE pattern (V-02/V-04/V-05 in R11). C-28 and C-29 were added in
> v9 from R12 excellence signals: C-28 from the VERDICT-TO-TABLE TRACEABILITY pattern
> (V-01/V-04 in R12 — when the verdict enumerates EG finding IDs under C-26, each cited ID must
> resolve to a specific Step 3b row) and C-29 from the PROMOTION COUNT FORWARD-REFERENCE pattern
> (V-02/V-04 in R12 — when both C-26 and C-27 are satisfied, the Phase 5 evidence summary must
> carry the SA remaining count from the promotion arithmetic alongside the EG count). C-30 and
> C-31 were added in v10 from R13 excellence signals: C-30 from the COUNT COMPLETENESS CHECK
> pattern (V-05 in R13 — the EVIDENCE ANCHOR block must perform per-ID membership verification
> against Step 3b row labels, closing the ID-substitution attack vector that COUNT RECONCILIATION
> CHECK leaves open) and C-31 from the EXPANDED BIDIRECTIONAL ANNOTATION pattern (V-05 in R13 —
> the bidirectional annotation introduced on the PROMOTION COMPLETENESS GATE in R11 is extended
> to all forward-referencing blocks in the trace, making C-26 through C-29 self-certifying for
> future inheritance). C-32 and C-33 were added in v11 from R14 excellence signals: C-32 from
> the INERTIA CHECKLIST CLOSURE FOR C-30 pattern (V-05 in R14 — when C-30 is satisfied, a named
> INERTIA checklist entry must document the ID-substitution attack vector and explicitly state it
> closes C-30, making C-30 self-certifying for future round inheritance without re-reading the
> criterion text) and C-33 from the INERTIA CHECKLIST CLOSURE FOR C-31 pattern (V-05 in R14 —
> when C-31 is satisfied, a named INERTIA checklist entry must document the forward-reference
> opacity anti-pattern and explicitly state it closes C-31, making C-31 self-certifying for
> future round inheritance). C-34 and C-35 are new in v12, extracted from R15 excellence
> signals: C-34 from the INERTIA BILATERAL CLOSURE pattern (V-03 in R15 — the first variation
> to satisfy both C-32 and C-33 in the same pass, versus V-01 and V-02 which each closed only
> one; co-presence in the same INERTIA block signals that the author treats C-30/C-31 as a
> structural pair, not independent items) and C-35 from the INERTIA CONSEQUENCE CLAUSE pattern
> (V-03 in R15 — the why-sentence in both C-32 and C-33 INERTIA items concludes with an
> explicit structural consequence naming what the mechanism makes visible, impossible, or
> self-certifying, anchoring the durability claim so a future maintainer can verify the
> mechanism is working without re-reading the criterion text).

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-09 | *(aspirational — see v1)* | 2 | aspirational | *(pass condition unchanged from v1)* |
| C-10 | *(aspirational — see v1)* | 2 | aspirational | *(pass condition unchanged from v1)* |
| C-11 | *(aspirational — see v2)* | 0.5 | aspirational | *(pass condition unchanged from v2)* |
| C-12 | *(aspirational — see v2)* | 0.5 | aspirational | *(pass condition unchanged from v2)* |
| C-13 | *(aspirational — see v2)* | 0.5 | aspirational | *(pass condition unchanged from v2)* |
| C-14 | *(aspirational — see v3)* | 0.5 | aspirational | *(pass condition unchanged from v3)* |
| C-15 | *(aspirational — see v4)* | 0.5 | aspirational | *(pass condition unchanged from v4)* |
| C-16 | *(aspirational — see v4)* | 0.5 | aspirational | *(pass condition unchanged from v4)* |
| C-17 | *(aspirational — see v4)* | 0.5 | aspirational | *(pass condition unchanged from v4)* |
| C-18 | *(aspirational — see v4)* | 0.5 | aspirational | *(pass condition unchanged from v4)* |
| C-19 | *(aspirational — see v5)* | 0.5 | aspirational | *(pass condition unchanged from v5)* |
| C-20 | *(aspirational — see v5)* | 0.5 | aspirational | *(pass condition unchanged from v5)* |
| C-21 | *(aspirational — see v5)* | 0.5 | aspirational | *(pass condition unchanged from v5)* |
| C-22 | *(aspirational — see v6)* | 0.5 | aspirational | *(pass condition unchanged from v6)* |
| C-23 | *(aspirational — see v6)* | 0.5 | aspirational | *(pass condition unchanged from v6)* |
| C-24 | *(aspirational — see v7)* | 0.5 | aspirational | *(pass condition unchanged from v7)* |
| C-25 | *(aspirational — see v7)* | 0.5 | aspirational | *(pass condition unchanged from v7)* |
| C-26 | **NEEDS-REDESIGN evidence anchor** | 0.5 | aspirational | When the verdict classification is NEEDS-REDESIGN, the Phase 5 verdict section contains a NEEDS-REDESIGN EVIDENCE ANCHOR block that enumerates the specific EG finding IDs from Step 3b that drove the classification, with a count of EG findings cited. A NEEDS-REDESIGN verdict that states only the count or restates the classification rationale without citing specific finding IDs fails this criterion. |
| C-27 | **Promotion completeness gate** | 0.5 | aspirational | The SA-TO-SG PROMOTION block closes with a PROMOTION COMPLETENESS GATE that explicitly certifies: (a) all SA gaps from Stage 1 have been evaluated, (b) the SA remaining count after promotion, and (c) the SG from promotion count. The gate must be a named block, not inline text within the promotion evaluation. A trace where promotion arithmetic is present but uncertified — counts visible but not asserted as complete — fails this criterion. |
| C-28 | **Verdict-to-table traceability** | 0.5 | aspirational | When the verdict enumerates EG finding IDs under C-26, the Phase 5 verdict section contains a VERDICT-TO-TABLE TRACEABILITY sub-table with one row per cited ID, each row recording: cited ID, the corresponding Step 3b finding excerpt, Source, and Severity. The classification is explicitly blocked if any cited ID lacks a resolution row. A verdict block that lists EG IDs in prose or in a count-only check without this per-ID resolution sub-table fails this criterion. A COUNT RECONCILIATION CHECK (comparing Step 3b EG row count to EVIDENCE ANCHOR list length) does not satisfy this criterion: count equality does not detect ID substitution (cited IDs that number correctly but do not match actual Step 3b row labels). |
| C-29 | **Promotion count forward-reference** | 0.5 | aspirational | When both C-26 and C-27 are satisfied, the Phase 5 verdict section contains a VERDICT EVIDENCE SUMMARY block co-locating two rows: (a) EG count sourced from the EVIDENCE ANCHOR list and (b) SA remaining count sourced from the PROMOTION COMPLETENESS GATE. Both classification inputs must appear in the same named block so the verdict is self-contained without requiring re-inspection of Phase 2. A trace where SA remaining is visible in the PROMOTION COMPLETENESS GATE but not carried forward into Phase 5 fails this criterion. |
| C-30 | **Count completeness check** | 0.5 | aspirational | The NEEDS-REDESIGN EVIDENCE ANCHOR block contains a COUNT COMPLETENESS CHECK that performs per-ID membership verification: each ID cited in the EVIDENCE ANCHOR list is individually cross-checked against the Step 3b findings table row labels, confirming the cited ID exists as an actual row key. The check must be auditable ID by ID — enumerating each cited ID and its resolution status (YES / NOT FOUND) — not merely asserting count equality between Step 3b EG rows and ANCHOR list length. The block must classify as BLOCKED if any cited ID resolves to NOT FOUND. A block that states "Step 3b EG rows = N, ANCHOR list length = N, match" without enumerating the ID-to-row mapping fails this criterion, as count equality cannot detect ID substitution (a model may cite F-03 when Step 3b has F-02 and the counts still match). |
| C-31 | **Expanded bidirectional annotation** | 0.5 | aspirational | Every block in the trace that forward-references another block carries an explicit inline annotation of the form "forward-referenced in [block name]" (or equivalent), and the referenced target block carries a corresponding back-reference annotation identifying its source block. This bidirectional annotation must cover at minimum: the PROMOTION COMPLETENESS GATE annotating its SA remaining count as forward-referenced in the Phase 5 VERDICT EVIDENCE SUMMARY, the NEEDS-REDESIGN EVIDENCE ANCHOR annotating its EG finding IDs as resolved in the VERDICT-TO-TABLE TRACEABILITY sub-table, and the VERDICT-TO-TABLE TRACEABILITY sub-table annotating its source as the Step 3b findings table. A trace where any qualifying forward-reference or back-reference annotation is absent fails this criterion. Bidirectional annotation makes C-26 through C-29 self-certifying for future round inheritance: a reviewer can confirm each criterion is met from the annotation alone without re-tracing the full document. |
| C-32 | **Inertia checklist closure for C-30** | 0.5 | aspirational | When C-30 is satisfied, the trace includes a named INERTIA checklist entry that: (a) identifies the attack vector as "ID substitution" (or equivalent phrasing), (b) states what the attack makes possible — that a model may cite EG IDs that number correctly but do not match actual Step 3b row labels, causing count equality to pass while per-ID membership fails, and (c) explicitly references C-30 as the criterion it closes. The INERTIA entry must be a named item in a checklist block, not inline commentary at the point of use. A trace where C-30 passes but carries no corresponding INERTIA entry fails this criterion. An INERTIA entry that merely re-states the C-30 pass condition without naming the attack vector also fails. |
| C-33 | **Inertia checklist closure for C-31** | 0.5 | aspirational | When C-31 is satisfied, the trace includes a named INERTIA checklist entry that: (a) identifies the anti-pattern as "forward-reference opacity" (or equivalent phrasing), (b) states what the anti-pattern causes — that forward-referencing blocks without bidirectional annotations force a future reviewer to re-inspect the full document to verify that C-26 through C-29 are satisfied, and (c) explicitly references C-31 as the criterion it closes. The INERTIA entry must be a named item in a checklist block, not inline commentary. A trace where C-31 passes but carries no corresponding INERTIA entry fails this criterion. |
| C-34 | **Inertia bilateral closure** | 0.5 | aspirational | When both C-32 and C-33 are satisfied, the corresponding INERTIA entries for both must appear in the same named INERTIA block within the same trace. A trace whose INERTIA block contains the C-30 closure item (C-32) but not the C-31 closure item (C-33), or vice versa, creates an asymmetric durability record: one vulnerability is self-documented and self-certifying, the other requires criterion-text lookup. Because C-30 and C-31 address the same structural phase — the durability of per-ID verification and bidirectional annotation across round boundaries — their INERTIA entries must be co-present. A trace that satisfies C-32 without C-33 (or C-33 without C-32) in the same INERTIA block fails this criterion regardless of whether each entry is individually well-formed. |
| C-35 | **Inertia consequence clause** | 0.5 | aspirational | When both C-32 and C-33 are satisfied, the why-sentence in each INERTIA entry must conclude with an explicit structural consequence clause — a statement of what the mechanism makes visible, impossible, or self-certifying. The consequence clause must name the specific property the mechanism guarantees, not merely restate the mechanism. Acceptable forms: "making phantom references visible regardless of count correctness" (C-32 item), "make each block self-certifying without a manual document scan" (C-33 item), or equivalent. A why-sentence that explains the mechanism without asserting its structural consequence (e.g., "per-ID membership exists because count equality is insufficient" without the "making phantom references visible" conclusion) fails this criterion. The consequence clause anchors the durability claim: a future maintainer can verify the mechanism is working by checking whether the named property holds, without re-reading the criterion text. Pass: both the C-32 INERTIA item and the C-33 INERTIA item contain a why-sentence whose final clause names the structural consequence of the mechanism. |
