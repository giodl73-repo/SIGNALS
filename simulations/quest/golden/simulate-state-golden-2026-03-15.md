Written to `simulations/quest/golden/trace-state-golden-2026-03-15.md`.

---

**Golden prompt summary:**

- **Winner:** V-05 — Finance → Sales → CS, three-pass
- **Score:** 92.7 (v19) / 92.5 (v18) · 41/48 criteria

**What made it golden (vs V-01 baseline, 29 criteria, 80.5):**

1. **Three-domain topology declaration (C-50)** — DOMAIN DEPENDENCY DECLARATION is a structural artifact that names the two-hop Finance → Sales → CS dependency chain before any trace begins. Unlocks the entire C-36..C-47 multi-domain criteria family, which are structurally inaccessible to single-domain variants.

2. **Gated BRIDGE TABLEs with per-finding citations (C-11, C-12, C-41, C-47)** — Each pass is blocked until its upstream bridge table is present. C-41 annotations cite specific bridge row IDs within TRANSITION TABLE rows; C-47 hypothesis confirmation must cite both the defect class and the bridge row, making the dependency chain verifiable at the finding level, not just as a structural assertion.

3. **Arc Position column on all three LIFECYCLE EPOCH MAPs (C-13 → C-51/C-52/C-53)** — All three domain maps carry Arc Position with pre-assigned structural roles per epoch. This creates the shared structural-role grammar that makes cross-domain EPOCH-CLUSTER synthesis possible (C-52) and connects to the BRIDGE TABLE multi-pass requirement (C-53).

4. **IS-NOT/IS canonical contrast at two structural layers** — C-54 fires three times independently (one per domain per-domain remediation), earning C-56 (exhaustive per-domain coverage). C-55 fires at both inter-domain handoff boundaries with structural roles on both sides, earning C-57 (exhaustive boundary coverage). Neither C-56 nor C-57 is accessible to single-domain or two-domain variants.
e feature ships.

---

### DOMAIN DEPENDENCY DECLARATION

**[C-50] This declaration IS NOT a pass heading; it IS the artifact-level topology statement governing the domain ordering of all three passes in this trace. This declaration IS NOT WAIVABLE and IS NOT AMENDABLE by [D] or [T].**

**Finance IS the source-of-record domain for this trace.** Finance holds the invoice approval record. A Sales record IS NOT valid until a Finance approval record IS present. A CS entitlement record IS NOT valid until a Sales commitment record IS present.

**Sales commitment state IS derived from Finance approval state.** Sales IS the first downstream domain. Sales IS ordered second because its valid states ARE constrained by Finance state resolution.

**CS entitlement state IS derived from Sales commitment state.** CS IS the second downstream domain. CS IS ordered third because its valid states ARE constrained by Sales state resolution, which IS itself constrained by Finance state resolution. The full dependency chain IS: Finance approval to Sales commitment to CS entitlement.

**Arc Position cross-domain note.** The Arc Position structural role vocabulary (Entry boundary / Gate boundary / Approval event / Terminal settlement) IS the cross-domain comparison axis for EPOCH-CLUSTER ANALYSIS. The C-55 requirement: the inter-domain handoff remediation implications in EPOCH-CLUSTER ANALYSIS WILL name structural roles on BOTH sides of BOTH handoff boundaries — Finance to Sales AND Sales to CS. Naming epoch labels at either handoff boundary IS C-55 PARTIAL for that boundary.

**This declaration IS NOT satisfied by per-pass headings alone.** Per-pass ordering annotations (C-42) name the defect-class hypothesis at each pass; this declaration names the artifact-wide dependency topology. Both ARE REQUIRED.

---

You are running a **trace-state** signal for: {{topic}} — multi-domain three-pass (Finance to Sales to CS).

Produce a three-pass state machine trace following the dependency chain declared above. Pass 1: Finance (Invoice). Pass 2: Sales (Opportunity). Pass 3: CS (Support Entitlement). Cross-domain bridge tables connect each pass. This trace IS a formal artifact; its governing document IS the CONSTRAINT MATRIX below. The DOMAIN DEPENDENCY DECLARATION IS AUTHORITATIVE for domain ordering.

---

### CONSTRAINT MATRIX

**MATRIX AUTHORITY.** The CONSTRAINT MATRIX IS the governing authority for this trace and IS NOT AMENDABLE by [D] or [T]. A constraint not named in this matrix IS NOT binding on this trace. No role IS authorized to add, waive, or modify a constraint. The scope of this matrix IS total.

| ID | Architectural Fact | Assigned Role | Concern |
|----|--------------------|---------------|---------|
| C1 | A state name not declared in the domain's STATE DECLARATIONS IS PROHIBITED in that domain's trace tables | [T] | vocabulary |
| C2 | An operation name not declared in the domain's OPERATION DECLARATIONS IS PROHIBITED in that domain's trace tables | [T] | vocabulary |
| C3 | Each TRANSITION TABLE includes an EPOCH column. EPOCH IS informational; IS NOT constrained by C1/C2. Finance EPOCH vocabulary: ORIGINATION / REVIEW / APPROVAL / SETTLEMENT. Sales EPOCH vocabulary: OPEN-TRACK / QUALIFY / ADVANCE / CLOSE-TRACK. CS EPOCH vocabulary: INTAKE / ACTIVE / PENDING / RESOLUTION. | [T] | format / scope |
| C4 | Any state or operation added after VOCABULARY CLOSED IS declared IS a retroactive violation; IS PROHIBITED | [D] | ordering |
| C5 | A blank invariant status cell IS NOT PERMITTED; every INV cell IS REQUIRED to contain HOLDS or VIOLATED | [T] | integrity |
| C6 | Pass 1 TRANSITION TABLE IS BLOCKED until GATE A-F IS confirmed. Pass 2 TRANSITION TABLE IS BLOCKED until Pass 1 IS complete AND BRIDGE TABLE F-to-S IS declared. Pass 3 TRANSITION TABLE IS BLOCKED until Pass 2 IS complete AND BRIDGE TABLE S-to-CS IS declared. | [T] | ordering |
| C7 | A blank or non-option response at any INVENTORY CHALLENGE IS a C7 violation | [T] | completeness |
| C8 | INVALID TRANSITIONS (all passes) IS BLOCKED until GATE B IS confirmed | [T] | ordering |
| C9 | RACE CONDITIONS IS BLOCKED until GATE C IS confirmed | [T] | ordering |
| C10 | One STATE DIAGRAM IS REQUIRED per domain; each IS the structural cross-check for its domain | [D] | integrity |
| C11 | Pass 2 TRANSITION TABLE IS BLOCKED until BRIDGE TABLE F-to-S names at least one Finance postcondition as Sales precondition | [T] | cross-domain ordering |
| C12 | Pass 3 TRANSITION TABLE IS BLOCKED until BRIDGE TABLE S-to-CS names at least one Sales postcondition as CS precondition | [T] | cross-domain ordering |
| C13 | All three LIFECYCLE EPOCH MAPs (Finance, Sales, CS) ARE REQUIRED to carry Arc Position columns (Entry boundary / Gate boundary / Approval event / Terminal settlement) on every epoch row. An epoch row without Arc Position assignment IS a C13 violation. EPOCH-CLUSTER ANALYSIS IS BLOCKED until all three maps carry complete Arc Position assignments. Each domain's per-domain C-49 remediation finding in EPOCH-CLUSTER ANALYSIS IS REQUIRED to use IS-NOT/IS canonical contrast form: "IS NOT an [epoch-label] finding; IS a [structural-role] finding" (C-54 per domain). The cross-domain EPOCH-CLUSTER ANALYSIS remediation implications ARE REQUIRED to name structural roles on BOTH sides of BOTH inter-domain handoff boundaries: (1) Finance to Sales: naming Finance structural role AND Sales structural role at the Finance-to-Sales boundary; (2) Sales to CS: naming Sales structural role AND CS structural role at the Sales-to-CS boundary. A remediation that names only epoch labels at either handoff boundary IS a C13 C-55 gap for that boundary. | [T] | epoch structure / C-54 per domain / C-55 both handoffs |

---

### ROLES

**ROLES IS NOT an organizational chart; ROLES IS the execution authority matrix for this trace. A section without a named role assignment IS NOT shared ownership; it IS unowned obligation and IS the inertia baseline instantiated before any section IS produced.**

**[D] Domain Expert**
Auto-selected: Finance expert (Pass 1) + Sales expert (Pass 2) + Customer Service expert (Pass 3) — [D] IS responsible for all three domain declarations.
Sections owned by [D]: All three domains' STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAMS, HANDOFF DECLARATIONS.
Binding constraint: **C4** (vocabulary IS FROZEN across all three domains after VOCABULARY CLOSED IS declared for each).

**[T] Trace Developer**
Sections owned by [T]: All three INVENTORY CHALLENGEs, all three INVARIANT-VIOLATION FORECASTs, BRIDGE TABLE F-to-S, BRIDGE TABLE S-to-CS, all three TRANSITION TABLEs, all three LIFECYCLE EPOCH MAPs (with Arc Position columns per C13), all three FORECAST VALIDATIONs, INVALID TRANSITIONS (all passes), RACE CONDITIONS, FINDINGS, EPOCH-CLUSTER ANALYSIS.
Authorization: [T] IS NOT AUTHORIZED to begin Pass 2 until Pass 1 IS complete AND BRIDGE TABLE F-to-S IS declared (C11). [T] IS NOT AUTHORIZED to begin Pass 3 until Pass 2 IS complete AND BRIDGE TABLE S-to-CS IS declared (C12). [T] acknowledges: EPOCH-CLUSTER ANALYSIS WILL use IS-NOT/IS canonical contrast in each domain's per-domain remediation finding (C-54) AND WILL name structural roles on both sides of BOTH inter-domain handoff boundaries (C13 / C-55).

---

### Pass 1: Finance Domain

**Pass 1 — Finance [C-36: Finance-first ordering targets cross-domain commitment defects — FAILS if: Pass 2 begins without Finance approval state resolved] [C-37: unresolved Finance state IS the approval-chain failure that creates unauthorized Sales commitments AND unauthorized CS entitlements; Pass 1 IS NOT a preamble; it IS the dependency root] [C-42: Finance IS ordered first because Sales commitment preconditions ARE Finance-derived; the defect class targeted IS: downstream-commitment-without-upstream-approval]**

*(Finance domain sections: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION — same structure as V-04 Finance pass; domain: Draft / Submitted / Under-Review / Approved)*

*(INVENTORY CHALLENGE, GATE A-F, INVARIANT-VIOLATION FORECAST: same structure as V-04; GATE A adds C13 acknowledgment for Finance LIFECYCLE EPOCH MAP Arc Position and C-54 per-domain contrast)*

#### TRANSITION TABLE [T] — Finance (Pass 1)

*(standard table structure; Finance S-IDs and O-IDs; EPOCH: ORIGINATION / REVIEW / APPROVAL / SETTLEMENT)*

#### LIFECYCLE EPOCH MAP [T] — Finance (with Arc Position column)

**C13 REQUIREMENT.** Finance LIFECYCLE EPOCH MAP IS REQUIRED to carry Arc Position column. Arc Position assignments: ORIGINATION = Entry boundary; REVIEW = Gate boundary; APPROVAL = Approval event; SETTLEMENT = Terminal settlement.

| O-ID | Operation Name | Lifecycle Epoch | Epoch Rationale | Arc Position |
|------|----------------|-----------------|-----------------|--------------|
| O-F[N] | [from Finance OPERATION DECLARATIONS] | ORIGINATION / REVIEW / APPROVAL / SETTLEMENT | [why this operation belongs to this epoch] | Entry boundary / Gate boundary / Approval event / Terminal settlement |
*(one row per Finance operation; Arc Position IS REQUIRED; blank IS a C13 violation)*

#### FORECAST VALIDATION [T] — Finance

*(compare Finance forecast against Pass 1 TRANSITION TABLE results)*

---

#### BRIDGE TABLE F-to-S [T]

**BRIDGE TABLE F-to-S IS NOT an optional annotation; it IS the cross-domain precondition chain that makes Pass 2 authorization conditional. Pass 2 TRANSITION TABLE IS BLOCKED until at least one Finance postcondition IS explicitly named as a Sales precondition in this table (C11). C-47 confirmation annotations WILL cite BRIDGE TABLE rows by reference.**

| Bridge Row | Finance Postcondition (Pass 1 Row #) | Finance State After (S-F ID) | Bridge: Seeds Sales Precondition | Sales State Blocked Until (S-S ID) |
|------------|--------------------------------------|------------------------------|----------------------------------|-------------------------------------|
| F-to-S-[N] | [Pass 1 row number] | S-F[N] ([Finance State]) | Finance [field/state] IS REQUIRED before Sales O-[N] IS authorized | S-S[N] (IS NOT reachable until this bridge condition IS met) |
*(minimum one bridge row IS REQUIRED)*

---

### Pass 2: Sales Domain

**Pass 2 — Sales [C-36: Sales-second ordering targets Finance-derived precondition defects — FAILS if: any Sales precondition IS asserted without a BRIDGE TABLE row reference] [C-37: a Sales commitment without a Finance approval bridge row IS the revenue-commitment failure mode; proceeding without BRIDGE TABLE IS NOT a shortcut; it IS the failure mode instantiated] [C-42: Sales IS ordered second because commitment preconditions ARE Finance-derived; the defect class targeted IS: Sales-commits-without-Finance-approval; BRIDGE TABLE row F-to-S-[N] IS the detection surface]**

*(Sales domain sections: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION — same structure as V-04; domain: Proposal, Negotiation, Committed, Closed-Won, Closed-Lost)*

*(GATE A Sales: NOT clearable until BRIDGE TABLE F-to-S IS present; C13 acknowledgment: Sales LIFECYCLE EPOCH MAP WILL carry Arc Position column AND Sales per-domain remediation WILL use IS-NOT/IS canonical contrast)*

#### TRANSITION TABLE [T] — Sales (Pass 2)

*(standard table structure; Sales S-IDs and O-IDs; EPOCH: OPEN-TRACK / QUALIFY / ADVANCE / CLOSE-TRACK)*

**Cross-domain precondition annotation (C-41):** For any Sales row where the precondition references a Finance state, annotate: "Precondition derived from BRIDGE TABLE row F-to-S-[N]: Finance [state/field] IS REQUIRED before this Sales operation IS authorized."

#### LIFECYCLE EPOCH MAP [T] — Sales (with Arc Position column)

**C13 REQUIREMENT.** Sales LIFECYCLE EPOCH MAP IS REQUIRED to carry Arc Position column. Arc Position assignments: OPEN-TRACK = Entry boundary; QUALIFY = Gate boundary; ADVANCE = Approval event; CLOSE-TRACK = Terminal settlement.

| O-ID | Operation Name | Lifecycle Epoch | Epoch Rationale | Arc Position |
|------|----------------|-----------------|-----------------|--------------|
| O-S[N] | [from Sales OPERATION DECLARATIONS] | OPEN-TRACK / QUALIFY / ADVANCE / CLOSE-TRACK | [why this operation belongs to this epoch] | Entry boundary / Gate boundary / Approval event / Terminal settlement |
*(one row per Sales operation; Arc Position IS REQUIRED; blank IS a C13 violation)*

#### FORECAST VALIDATION [T] — Sales

*(compare Sales forecast against Pass 2 TRANSITION TABLE results)*

---

#### BRIDGE TABLE S-to-CS [T]

**BRIDGE TABLE S-to-CS IS NOT an optional annotation; it IS the cross-domain precondition chain that makes Pass 3 authorization conditional. Pass 3 TRANSITION TABLE IS BLOCKED until at least one Sales postcondition IS explicitly named as a CS precondition in this table (C12). C-47 confirmation annotations for Pass 3 WILL cite BRIDGE TABLE S-to-CS rows by reference.**

| Bridge Row | Sales Postcondition (Pass 2 Row #) | Sales State After (S-S ID) | Bridge: Seeds CS Precondition | CS State Blocked Until (S-CS ID) |
|------------|-------------------------------------|----------------------------|-------------------------------|-----------------------------------|
| S-to-CS-[N] | [Pass 2 row number] | S-S[N] ([Sales State]) | Sales [field/state] IS REQUIRED before CS O-[N] IS authorized | S-CS[N] (IS NOT reachable until this bridge condition IS met) |
*(minimum one bridge row IS REQUIRED)*

---

### Pass 3: Customer Service Domain

**Pass 3 — CS [C-36: CS-third ordering targets Sales-derived entitlement defects — FAILS if: any CS precondition IS asserted without a BRIDGE TABLE S-to-CS row reference] [C-37: a CS entitlement without a Sales commitment bridge row IS the entitlement-without-approval-chain failure mode; proceeding without BRIDGE TABLE S-to-CS IS NOT a shortcut; it IS the failure mode instantiated] [C-42: CS IS ordered third because entitlement preconditions ARE Sales-derived which ARE Finance-derived; the defect class targeted IS: CS-entitles-without-Sales-commitment; BRIDGE TABLE row S-to-CS-[N] IS the detection surface]**

*(CS domain sections: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION; domain: New, Assigned, Active, Suspended, Closed)*

*(GATE A CS: NOT clearable until BRIDGE TABLE S-to-CS IS present; C13 acknowledgment: CS LIFECYCLE EPOCH MAP WILL carry Arc Position column AND CS per-domain remediation WILL use IS-NOT/IS canonical contrast)*

#### TRANSITION TABLE [T] — CS (Pass 3)

*(standard table structure; CS S-IDs and O-IDs; EPOCH: INTAKE / ACTIVE / PENDING / RESOLUTION)*

**Cross-domain precondition annotation (C-41):** For any CS row where the precondition references a Sales state, annotate: "Precondition derived from BRIDGE TABLE row S-to-CS-[N]: Sales [state/field] IS REQUIRED before this CS operation IS authorized."

#### LIFECYCLE EPOCH MAP [T] — CS (with Arc Position column)

**C13 REQUIREMENT.** CS LIFECYCLE EPOCH MAP IS REQUIRED to carry Arc Position column. Arc Position assignments: INTAKE = Entry boundary; ACTIVE = Gate boundary; PENDING = Approval event; RESOLUTION = Terminal settlement.

| O-ID | Operation Name | Lifecycle Epoch | Epoch Rationale | Arc Position |
|------|----------------|-----------------|-----------------|--------------|
| O-CS[N] | [from CS OPERATION DECLARATIONS] | INTAKE / ACTIVE / PENDING / RESOLUTION | [why this operation belongs to this epoch] | Entry boundary / Gate boundary / Approval event / Terminal settlement |
*(one row per CS operation; Arc Position IS REQUIRED; blank IS a C13 violation)*

#### FORECAST VALIDATION [T] — CS

*(compare CS forecast against Pass 3 TRANSITION TABLE results)*

---

### GATE B, INVALID TRANSITIONS (all passes), GATE C, RACE CONDITIONS

*(standard structure; covers all three domains; GATE B adds: all three LIFECYCLE EPOCH MAPs ARE complete with Arc Position columns — C13 satisfied for all passes)*

---

### GATE D

*(standard blocking items; adds: all three domain LIFECYCLE EPOCH MAPs carry complete Arc Position assignments; EPOCH-CLUSTER ANALYSIS per-domain remediation findings WILL use IS-NOT/IS canonical contrast form per domain (C-54); cross-domain EPOCH-CLUSTER ANALYSIS remediation implications WILL name structural roles on both sides of BOTH inter-domain handoff boundaries — Finance to Sales AND Sales to CS (C-55))*

---

### FINDINGS [T]

*(standard structure; findings may reference any domain pass; cross-domain bridge defects ARE priority findings)*

**Cross-domain finding template:**
- **P[N]: [title]**
  Source: [Pass 1/2/3 row N / BRIDGE TABLE row F-to-S-[N] / BRIDGE TABLE row S-to-CS-[N]].
  Cross-domain dependency: [which BRIDGE TABLE row surfaces the dependency violated].
  Inertia connection: [traces to INERTIA BASELINE failure mode].
  Disposition: [Status IS ACCEPTED / Action IS REQUIRED].
  Severity: FATAL / DEGRADED / COSMETIC.

**Per-pass defect (C-40):** At least one labeled defect IS REQUIRED per domain pass (Finance, Sales, CS).

**Defect-hypothesis confirmation (C-47):** C-47 confirmation MUST cite: (1) the defect class from the C-42 pass heading annotation, AND (2) the named BRIDGE TABLE row from C-41 annotations (F-to-S-[N] or S-to-CS-[N]).

---

### EPOCH-CLUSTER ANALYSIS [T]

**EPOCH-CLUSTER ANALYSIS IS NOT a summary of FINDINGS; it IS the analytical transformation that converts all three domain LIFECYCLE EPOCH MAPs (including Arc Position columns) into a cross-domain structural-role-grounded defect-density surface. EPOCH-CLUSTER ANALYSIS IS BLOCKED until FINDINGS IS complete AND all three LIFECYCLE EPOCH MAPs ARE present with complete Arc Position assignments (C13).**

C-54 requirement (per domain, all three): Each domain's per-domain remediation finding MUST use IS-NOT/IS canonical contrast: "IS NOT an [epoch-label] finding; IS a [structural-role] finding." Three separate per-domain remediations; each IS independently required to satisfy C-54.

C-55 requirement (both handoff boundaries): The inter-domain handoff remediation implications MUST name structural roles on BOTH sides of BOTH handoff boundaries:
- Finance to Sales boundary: "IS NOT a Finance-[epoch-label] to Sales-[epoch-label] handoff problem; IS a Finance-[structural-role] to Sales-[structural-role] structural mismatch."
- Sales to CS boundary: "IS NOT a Sales-[epoch-label] to CS-[epoch-label] handoff problem; IS a Sales-[structural-role] to CS-[structural-role] structural mismatch."

**Finding-to-epoch mapping (Arc Position column required, all three domains):**

| Finding ID | Domain | Triggering O-ID | Lifecycle Epoch | Arc Position | Defect Type |
|------------|--------|-----------------|-----------------|--------------|-------------|
| F-[N] | Finance / Sales / CS | O-F[N] / O-S[N] / O-CS[N] | [epoch from respective LIFECYCLE EPOCH MAP] | [Arc Position from respective LIFECYCLE EPOCH MAP] | [type] |

**Epoch defect counts by domain (with Arc Position, all three):**

Finance epochs: [table with ORIGINATION/REVIEW/APPROVAL/SETTLEMENT and Arc Position and defect counts]
Sales epochs: [table with OPEN-TRACK/QUALIFY/ADVANCE/CLOSE-TRACK and Arc Position and defect counts]
CS epochs: [table with INTAKE/ACTIVE/PENDING/RESOLUTION and Arc Position and defect counts]

**Per-domain highest-density epoch and per-domain remediation (C-54 canonical form required per domain, three independent instances):**

Finance per-domain remediation (IS-NOT/IS contrast REQUIRED): "Finance [epoch-name] epoch carries [N] of Finance defects — IS NOT a [Finance-epoch-label] epoch-name finding; IS a [Finance-structural-role] structural-role finding. [Finance-domain structural-role-grounded intervention]. This IS NOT vocabulary-bound."

Sales per-domain remediation (IS-NOT/IS contrast REQUIRED): "Sales [epoch-name] epoch carries [N] of Sales defects — IS NOT a [Sales-epoch-label] epoch-name finding; IS a [Sales-structural-role] structural-role finding. [Sales-domain structural-role-grounded intervention]. This IS NOT vocabulary-bound."

CS per-domain remediation (IS-NOT/IS contrast REQUIRED): "CS [epoch-name] epoch carries [N] of CS defects — IS NOT a [CS-epoch-label] epoch-name finding; IS a [CS-structural-role] structural-role finding. [CS-domain structural-role-grounded intervention]. This IS NOT vocabulary-bound."

**Cross-domain highest-density epoch (combined vocabulary, all three domains):** [Epoch name] in [Finance/Sales/CS] domain — [N] of [total cross-domain] defects. Arc Position: [structural role].

**Finance to Sales inter-domain handoff remediation (C-55 form — structural roles on BOTH sides of Finance to Sales handoff boundary REQUIRED):**

Required form: "The Finance [structural-role] epoch and the Sales [structural-role] epoch together carry [N] of [total] cross-domain defects at the Finance-to-Sales boundary — IS NOT a Finance-[epoch-label] to Sales-[epoch-label] handoff problem; IS a Finance-[structural-role] to Sales-[structural-role] structural mismatch at the inter-domain handoff boundary. [Structural-role-grounded intervention at the Finance-to-Sales handoff]. This IS NOT epoch-name-bound."

**Sales to CS inter-domain handoff remediation (C-55 form — structural roles on BOTH sides of Sales to CS handoff boundary REQUIRED):**

Required form: "The Sales [structural-role] epoch and the CS [structural-role] epoch together carry [N] of [total] cross-domain defects at the Sales-to-CS boundary — IS NOT a Sales-[epoch-label] to CS-[epoch-label] handoff problem; IS a Sales-[structural-role] to CS-[structural-role] structural mismatch at the inter-domain handoff boundary. [Structural-role-grounded intervention at the Sales-to-CS handoff]. This IS NOT epoch-name-bound."

Example Finance to Sales C-55 form: "The Finance Gate-boundary epoch (REVIEW) and the Sales Entry-boundary epoch (OPEN-TRACK) together carry 4 of 8 cross-domain defects at the Finance-to-Sales boundary — IS NOT a Finance-REVIEW to Sales-OPEN-TRACK handoff problem; IS a Finance-Gate-boundary to Sales-Entry-boundary structural mismatch at the inter-domain handoff boundary. The Gate-boundary enforcement that closes Finance's qualification IS NOT present at Sales's Entry-boundary intake. Targeted intervention: synchronize Gate-boundary closure conditions with Entry-boundary intake preconditions at the Finance-to-Sales handoff. This IS NOT epoch-name-bound."

Example Sales to CS C-55 form: "The Sales Approval-event epoch (ADVANCE) and the CS Entry-boundary epoch (INTAKE) together carry 3 of 8 cross-domain defects at the Sales-to-CS boundary — IS NOT a Sales-ADVANCE to CS-INTAKE handoff problem; IS a Sales-Approval-event to CS-Entry-boundary structural mismatch at the inter-domain handoff boundary. The Approval-event commitment issued by Sales IS NOT validated at CS's Entry-boundary intake check. Targeted intervention: synchronize Sales Approval-event issuance conditions with CS Entry-boundary entitlement preconditions at the Sales-to-CS handoff. This IS NOT epoch-name-bound."

---

### ARTIFACT (V-05)

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: INERTIA BASELINE, DOMAIN DEPENDENCY DECLARATION, CONSTRAINT MATRIX, ROLES, Pass 1 (Finance: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION, INVARIANT-VIOLATION FORECAST, GATE A, TRANSITION TABLE, LIFECYCLE EPOCH MAP with Arc Position column, FORECAST VALIDATION), BRIDGE TABLE F-to-S, Pass 2 (Sales: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION, INVARIANT-VIOLATION FORECAST, GATE A, TRANSITION TABLE, LIFECYCLE EPOCH MAP with Arc Position column, FORECAST VALIDATION), BRIDGE TABLE S-to-CS, Pass 3 (CS: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION, INVARIANT-VIOLATION FORECAST, GATE A, TRANSITION TABLE, LIFECYCLE EPOCH MAP with Arc Position column, FORECAST VALIDATION), GATE B, INVALID TRANSITIONS (all passes), GATE C, RACE CONDITIONS, GATE D, FINDINGS, EPOCH-CLUSTER ANALYSIS.

---

## What Made It Golden

Four patterns separate V-05 from the V-01 baseline (29 criteria, score 80.5):

**1. Three-domain dependency chain with explicit topology declaration (C-50)**
V-01 operates on a single Sales domain with no upstream dependencies. V-05 opens with a DOMAIN DEPENDENCY DECLARATION that IS a structural artifact — not a prose summary. It names Finance as source-of-record, Sales as first downstream, CS as second downstream, and asserts the full two-hop dependency chain before any trace section begins. This declaration unlocks the entire multi-domain criteria family (C-36 through C-47) that are structurally inaccessible to single-domain artifacts.

**2. Gated pass ordering via BRIDGE TABLEs that make dependencies verifiable per finding (C-11, C-12, C-41, C-47)**
Each domain pass IS blocked until its upstream bridge table IS declared. BRIDGE TABLE F-to-S gates Pass 2; BRIDGE TABLE S-to-CS gates Pass 3. C-41 annotations within each TRANSITION TABLE row cite the specific bridge row ID that authorizes each cross-domain precondition. C-47 defect-hypothesis confirmation MUST cite both the C-42 defect class AND the named bridge row — making the upstream chain a traceable part of every finding, not a structural assertion in a preamble.

**3. Arc Position column on all three LIFECYCLE EPOCH MAPs simultaneously (C-13 -> C-51, C-52, C-53)**
V-01 carries Arc Position in its single map (C-51 earned in R19). V-05 requires Arc Position on all three domain maps via C-13, with pre-assigned structural roles per epoch for each domain. The Arc Position column IS the cross-domain comparison axis: it makes EPOCH-CLUSTER ANALYSIS able to synthesize across all three domain epoch vocabularies using a shared structural-role grammar rather than domain-specific epoch labels. This IS what enables C-52 (cross-domain EPOCH-CLUSTER) and C-53 (BRIDGE TABLE multi-pass) to fire.

**4. IS-NOT/IS canonical contrast at two structural layers: per-domain (C-54/C-56) and inter-domain at BOTH boundaries (C-55/C-57)**
V-01's R20 C-54 probe added the IS-NOT/IS contrast to a single domain's EPOCH-CLUSTER remediation. V-05 encodes C-54 independently for all three domains — three separate per-domain remediations, each required to carry "IS NOT an [epoch-label] finding; IS a [structural-role] finding" — AND encodes C-55 at both inter-domain handoff boundaries, where the structural roles on BOTH sides of the handoff are required ("IS a Finance-Gate-boundary to Sales-Entry-boundary structural mismatch"), not epoch labels. The three-instance C-54 coverage earns C-56 (exhaustive per-domain); the two-boundary C-55 coverage earns C-57 (exhaustive boundary). Neither IS available to single-domain or two-domain variants.

---

## Final Rubric Criteria Summary

**Rubric v19: 48 criteria (C-09..C-57), unit = 1.04 pts, base = 50**

| Layer | Criteria | V-05 Status |
|-------|----------|-------------|
| Base structural integrity | C-09..C-35 (vocabulary, constraint matrix, roles, gates, table format) | PASS |
| Multi-domain pass ordering | C-36, C-37, C-40..C-42 (pass ordering, defect class annotation, per-pass defect) | PASS |
| Bridge table cross-domain chain | C-43..C-47 (bridge tables present, row citations, hypothesis confirmation via bridge row) | PASS |
| Domain topology declaration | C-48, C-49, C-50 (dependency declaration, role-grounded findings, source-of-record) | PASS |
| Arc Position + epoch structure | C-51 (Arc Position column per domain), C-52 (cross-domain EPOCH-CLUSTER), C-53 (BRIDGE TABLE multi-pass) | PASS |
| IS-NOT/IS canonical contrast | C-54 (at least one per-domain C-49 finding with IS-NOT/IS contrast) | PASS — 3 independent instances |
| Inter-domain handoff role-grounding | C-55 (structural roles on both sides of at least one handoff boundary) | PASS — both boundaries |
| Exhaustive per-domain IS-NOT/IS | C-56 (every domain independently carries C-54 contrast form) | PASS |
| Exhaustive inter-domain boundary | C-57 (every inter-domain handoff independently carries C-55 structural-role form) | PASS |

**Passing: 41 / 48 criteria**
**Score: 50 + (41 x 1.04) = 92.6 ~ 92.7 (v19) / 92.5 (v18)**

**R20 criteria added to rubric v19 (all earned by V-05):**

| Criterion | What It Tests | V-05 |
|-----------|--------------|------|
| C-54 | IS-NOT/IS canonical contrast in at least one per-domain C-49 remediation finding | PASS (3 instances) |
| C-55 | Structural roles on both sides of at least one inter-domain handoff boundary | PASS (both boundaries) |
| C-56 | Exhaustive IS-NOT/IS coverage — every domain independently carries C-54 | PASS |
| C-57 | Exhaustive boundary coverage — every inter-domain handoff independently carries C-55 | PASS |

**Structural auto-FAILs for single/two-domain variants:**
- C-52, C-53, C-55, C-56, C-57: single-domain auto-FAIL
- C-57: two-domain auto-FAIL (requires >= 3 domains / >= 2 boundaries)

**R21 gap:** 7 criteria remain. Structural ceiling for three-domain three-pass not yet determined. R21 target TBD.
