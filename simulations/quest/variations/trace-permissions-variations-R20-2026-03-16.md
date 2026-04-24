]:
Column security profiles not discoverable from security roles UI; missing FLS discovered only after data exposure.

STRUCTURED CLOSE:
TABLE_2 enumerates sensitive fields with explicit FLS status. Not Configured → TABLE_5 as MISSING-FLS.

**TABLE_2** *(Schema Registry TABLE_2)*

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

### SE-3 / SHALL-C — Record Access Scope

MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:
No single UI view surfaces combined role + team + OWD effective access.

STRUCTURED CLOSE:
TABLE_3 maps effective scope per role in one traceable row.

**TABLE_3** *(Schema Registry TABLE_3)*

| Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|------|--------------|----------------|-----------------|-----------|

After TABLE_3: populate CS-3 SE Cross-Reference and SE Confirmation.

### SE-4 / SHALL-D — Privilege Escalation Analysis

MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:
OWD audited entity-by-entity without cross-referencing sharing rules that silently override them.

STRUCTURED CLOSE:
TABLE_4 (filled at SE-0) surfaced escalation vectors before TABLE_1, establishing privilege ceiling first. CS-2 expectations confirmed or contradicted.

Cite: TABLE_4 (filled at SE-0) row [exact vector label from TABLE_4] — [role] privilege ceiling: [pattern or "no escalation path — [reason]"].

### SE-5 / SHALL-E — Security Gap Inventory

**TABLE_5** *(Schema Registry TABLE_5)*

| # | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation |
|---|----------|--------|---------------|------|------|----------|-------------|

*Handing to PHASE 2 — CS.*

---

## PHASE 2 — CS: Customer Success Analysis

### CS-0 — Schema Registry Acknowledgment (executes before CS-1)

- Schema ID: CS-2 — Sharing Rule Expectations. SE-updatable: SE Cross-Reference, SE Confirmation.
- Schema ID: CS-3 — Cross-Role Access Differential Expectations. SE-updatable: SE Cross-Reference, SE Confirmation.

*CS-0 complete — proceeding to CS-1.*

### CS-1 — Qualitative Baseline

Expected CRUD per entity. Expected record scope. Sensitive field access needs. Configuration risks. Business process, two personas, expected access pattern.

### CS-2 *(SE populates SE Cross-Reference and SE Confirmation)*

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation |
|-----------|---------|------------------------|-----------------------|---------------------|---------------------|-----------------|

### CS-3 *(SE populates SE Cross-Reference and SE Confirmation)*

| Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation |
|--------|-----------|------------------------|-----------------|-----------------------------|----------------------|---------------------|-----------------|

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

| CA Row | Audit Target | Criterion | Non-Overlapping Scope |
|--------|-------------|-----------|----------------------|
| CA-1.1 | TABLE_1 completeness | C-01 | Cell coverage and role enumeration |
| CA-1.2 | TABLE_2 FLS | C-02 | Sensitive field status and null-case |
| CA-1.3 | TABLE_3 scope | C-03 | Effective scope for every TABLE_1 role |
| CA-1.4 | TABLE_4 SE-0 ordering — axis A-1 | C-04 | SE-0 before SE-1; four vectors Checked? = YES |
| CA-1.5 | TABLE_5 gap inventory | C-05 | Named gap; exact remediation |
| CA-1.6 | SHALL-F structure | SHALL-F | CS-EXPECTATION-VIOLATED three-field completeness |
| CA-1.7 | MANUAL GAP labels — axis A-2 | SHALL-G | Character-for-character label at SE-2/SE-3/SE-4 |
| CA-1.8 | CS-0 acknowledgment — axis A-3 | C-33 | CS-0 before CS-1; exact Schema ID strings |
| CA-1.9 | SE-4 verbatim cite | SHALL-D-EXT-C35 | Verbatim Cite: format in SE-4 STRUCTURED CLOSE only |

NON-OVERLAP DECLARATION:
[CA-1.4]: SE-0 ordering only — not label matching or verbatim cite.
[CA-1.7]: Exact CONTEXT label at SE-2/SE-3/SE-4 only — not ordering or verbatim cite.
[CA-1.9]: SE-4 STRUCTURED CLOSE verbatim cite format only — not ordering or label matching.
[Axis declaration]: The STRUCTURAL AXIS NON-INTERFERENCE DECLARATION is a preamble-only contract, not a CA-1 audit target; verified through non-overlap of CA-1.4/CA-1.7/CA-1.8 individual scopes.

**CA-1.1** *(completing Phase 0 M4 pre-assignment CA-1.1)*:

Registry anchor — Schema ID TABLE_1: [Role, Tier, Create, Read, Write, Delete, Append, AppendTo, Assign, Share, Record Scope] — blank cells prohibited globally.

Preamble anchor — C-01 as authored by CA in Phase 0: TABLE_1 / SE-1 / SHALL-A / CA-1.1 — verifying...

Verification — TABLE_1 present? Every cell Granted/Denied/Conditional/N/A? All roles with Tier ordered? -> PASS / FAIL

**CA-1.2** *(completing Phase 0 M4 pre-assignment CA-1.2)*:

Registry anchor — Schema ID TABLE_2: [Entity, Field, Category, FLS Profile Configured?, Roles: Read, Roles: Write, Gap?] — blank cells prohibited globally.

Preamble anchor — C-02 as authored by CA in Phase 0: TABLE_2 / SE-2 / SHALL-B / CA-1.2 — verifying...

Verification — TABLE_2 present? Sensitive fields with FLS status? Null case stated? Gap? YES in TABLE_5? -> PASS / FAIL

**CA-1.3** *(completing Phase 0 M4 pre-assignment CA-1.3)*:

Registry anchor — Schema ID TABLE_3: [Role, Tier, OWD Baseline, Scope Modifier, Effective Scope, Verified?] — blank cells prohibited globally.

Preamble anchor — C-03 as authored by CA in Phase 0: TABLE_3 / SE-1+SE-3 / SHALL-C / CA-1.3 — verifying...

Verification — Every TABLE_1 role in TABLE_3? Effective Scope filled? Ambiguous in TABLE_5? -> PASS / FAIL

**CA-1.4** *(completing Phase 0 M4 pre-assignment CA-1.4; this row verifies axis A-1 — Execution order — as declared in the STRUCTURAL AXIS NON-INTERFERENCE DECLARATION, Phase 0)*:

Registry anchor — Schema ID TABLE_4: [Vector, Checked?, Finding, Severity] — all four vectors; TABLE_4 fills at SE-0 before TABLE_1.

Preamble anchor — C-04 as authored by CA in Phase 0: TABLE_4 / SE-0+SE-4 / SHALL-D / CA-1.4 — verifying SE-0 ordering only (A-1 axis scope)...

Verification — TABLE_4 present? All four vectors Checked? = YES? SE-0 header precedes SE-1 header? -> PASS / FAIL

**CA-1.5** *(completing Phase 0 M4 pre-assignment CA-1.5)*:

Registry anchor — Schema ID TABLE_5: [#, Gap Type, Entity, Field or Rule, Role, Tier, Severity, Remediation] — blank cells prohibited globally.

Preamble anchor — C-05 as authored by CA in Phase 0: TABLE_5 / SE-5 / SHALL-E / CA-1.5 — verifying...

Verification — TABLE_5 present? Named gap? Exact remediations? -> PASS / FAIL

**CA-1.6**:

Registry anchor — CS-EXPECTATION-VIOLATED row: [CS-Expected, SE-Actual, Delta] — all three required.

Preamble anchor — SHALL-F as authored by CA in Phase 0: three-field Remediation MUST be complete — verifying...

Verification — Each CS-EXPECTATION-VIOLATED row has all three fields? -> PASS / FAIL per row.

**CA-1.7** *(completing Phase 0 M4 pre-assignment CA-1.7; this row verifies axis A-2 — Closure-note format — as declared in the STRUCTURAL AXIS NON-INTERFERENCE DECLARATION, Phase 0)*:

Registry anchor — Exact CONTEXT labels: "Blind spot 1 — Post-incident FLS gap" (SE-2), "Blind spot 2 — Cumulative privilege blind spot" (SE-3), "Blind spot 3 — OWD-sharing-rule override gap" (SE-4).

Preamble anchor — SHALL-G as authored by CA in Phase 0: `MANUAL GAP [<exact label>]:` character-for-character match (A-2 axis scope; does not extend to ordering or verbatim cite)...

Verification — SE-2/SE-3/SE-4 each open with exact MANUAL GAP label and STRUCTURED CLOSE? -> PASS / FAIL per section.

**CA-1.8** *(completing Phase 0 M4 pre-assignment CA-1.8; this row verifies axis A-3 — CS self-reference — as declared in the STRUCTURAL AXIS NON-INTERFERENCE DECLARATION, Phase 0)*:

Registry anchor — Schema Registry: "CS-2 — Sharing Rule Expectations" and "CS-3 — Cross-Role Access Differential Expectations" with SE-updatable column declarations.

Preamble anchor — C-33 as authored by CA in Phase 0: CS-0 cites Schema ID: CS-2 and CS-3 by exact label before CS-1 (A-3 axis scope)...

Verification — CS-0 present? Exact Schema ID strings quoted? CS-0 before CS-1? -> PASS / FAIL

**CA-1.9** *(distinct from CA-1.4 and CA-1.7)*:

Registry anchor — Schema ID TABLE_4 note: fills at SE-0 BEFORE TABLE_1. SHALL-D-EXT-C35: SE-4 STRUCTURED CLOSE MUST contain `Cite: TABLE_4 (filled at SE-0) row [exact vector label]` verbatim.

Preamble anchor — SHALL-D-EXT-C35 as authored by CA in Phase 0: verbatim Cite: format in SE-4 STRUCTURED CLOSE (scope distinct from CA-1.4 and CA-1.7)...

Verification — SE-4 STRUCTURED CLOSE contains `Cite: TABLE_4 (filled at SE-0) row` verbatim? Exact vector label? Privilege ceiling description? -> PASS / FAIL

**CA Format Compliance Verdict (Phase 0 citation):**

Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0), Phase 0 by label.

[CA-1.1–CA-1.9 results. Overall: COMPLIANT / NON-COMPLIANT.]

**TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION** *(C-36 — V-04: verbatim section headers + A-N chain through CA-1.N rows)*:

| Axis | Dimension | Criterion | Evidence Source (verbatim output-body section header) | Status |
|------|-----------|-----------|------------------------------------------------------|--------|
| A-1 | Execution order | C-31 | `### SE-0 / SHALL-D — Escalation Vector Inventory (executes BEFORE SE-1)` precedes `### SE-1 / SHALL-A — Role-Operation Matrix`; CA-1.4 preamble anchor cites A-1 label | CONFIRMED |
| A-2 | Closure-note format | C-32 | `### SE-2 / SHALL-B — Field-Level Security Coverage` opens with `MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:` / `STRUCTURED CLOSE:`; same at SE-3/SE-4; CA-1.7 preamble anchor cites A-2 label | CONFIRMED |
| A-3 | CS self-reference | C-33 | `### CS-0 — Schema Registry Acknowledgment (executes before CS-1)` quotes `Schema ID: CS-2` and `Schema ID: CS-3` before `### CS-1 — Qualitative Baseline`; CA-1.8 preamble anchor cites A-3 label | CONFIRMED |

Three-point A-N chain: preamble STRUCTURAL AXIS NON-INTERFERENCE DECLARATION (declares A-1/A-2/A-3) → CA-1.4/CA-1.7/CA-1.8 preamble anchors (cite A-N labels by name) → attestation Evidence Source (verbatim section headers, auditable by text search). Each link independently verifiable.

---

## V-05 — Full: All Three R20 Additions (Maximum Reinforcement)

**Axis:** V-01 (CA-1.N axis back-references) + V-02 (verbatim section-header evidence sourcing) + V-03 (axis declaration self-scoping footer A-Meta) simultaneously on R19-V-05 base.
**Hypothesis:** All three R20 additions active simultaneously. The A-N label chain reaches maximum length: preamble declaration (including self-scoping footer) → CA-1.N verification rows (axis label cited in preamble anchor) → attestation table (verbatim section headers). Expected: 28/28; maximum surface area for latent v13 criteria.

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

Manual security reviews of Dataverse environments routinely miss three failure scenarios this trace is designed to surface:

**Blind spot 1 — Post-incident FLS gap.** Column security profiles are rarely audited proactively. Sensitive fields — credit limits, compensation data, SSNs, contact identifiers — remain readable and writable by any role unless a column security profile explicitly restricts them. The security roles UI does not surface which fields lack column security profiles; gaps are discovered after data exposure, not before.

**Blind spot 2 — Cumulative privilege blind spot.** A user holding a BU-scoped security role who also belongs to an owner team whose team role grants org-wide access has effective org-wide access. No single Dataverse UI view surfaces the combined effective access produced by role + team + OWD combination. Spot-checking individual roles misses cross-role accumulation through team membership.

**Blind spot 3 — OWD-sharing-rule override gap.** Administrators check OWD settings entity-by-entity without evaluating the sharing rules that silently override those baselines. A Private OWD on Case combined with a Power Automate-triggered sharing rule grants effective org-wide read to users who satisfy the trigger condition — including low-trust service accounts not intended to have broad case access.

CONTEXT BLIND SPOTS (input-level uncertainty):

| Label | Description | Impact |
|-------|-------------|--------|
| BS-U1 | Field inventory not described — sensitive fields per entity inferred from typical Dataverse deployments for {{topic}} | High |
| BS-U2 | Sharing rule list not provided | High |
| BS-U3 | Team structure not specified | Medium |

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as structural section headers in the output body.

**PHASE 0 — CA (Compliance Auditor):** CA first. Authors Schema Registry (Step 0.1: seven schemas) and preamble (Step 0.2: SHALL-A through SHALL-G with SHALL-D-EXT-C35, CEM four-column mapping CA-1.1 through CA-1.9, STRUCTURAL AXIS NON-INTERFERENCE DECLARATION with rows A-1/A-2/A-3 and self-scoping footer A-Meta, extended ATTESTATION CROSS-LINK MANDATE requiring CA-1.4/CA-1.7/CA-1.8 axis back-references and verbatim section-header Evidence Sources in attestation table). Handoff to PHASE 1 — SE.

**PHASE 1 — SE:** SE-0 first (TABLE_4 before TABLE_1), SE-1 through SE-5. SE-2/SE-3/SE-4 exact-label two-part closure blocks. SE-4 STRUCTURED CLOSE verbatim TABLE_4 cite per SHALL-D-EXT-C35. Handoff to PHASE 2 — CS.

**PHASE 2 — CS:** CS-0 first (Schema Registry acknowledgment), CS-1/CS-2/CS-3. Handoff to PHASE 3 — CA-1.

**PHASE 3 — CA-1:** Scope roster + NON-OVERLAP DECLARATION (four statements; fourth is structural consequence of A-Meta) + CA-1.1 through CA-1.9 (CA-1.4/CA-1.7/CA-1.8 cite A-N axis labels in preamble anchor). Terminal verdict with TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION (verbatim section headers, A-N labels matching preamble declaration, three-point chain closed).

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

### Step 0.1 — Schema Registry (CA-authored, Phase 0)

All table schemas declared centrally by CA. Blank-cell prohibition is global.

**Schema ID: TABLE_1 — Role-Operation Matrix**
Declared columns: `Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Tier: Admin / Custom / Restricted. Ordered Admin first. Blank-cell rule: Granted / Denied / Conditional (condition inline) / N/A.

**Schema ID: TABLE_2 — FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Blank-cell rule: Configured / Not Configured. Gap? = YES / NO.

**Schema ID: TABLE_3 — Record Scope by Role**
Declared columns: `Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Effective Scope: Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name].

**Schema ID: TABLE_4 — Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
All four vectors required. Checked? = YES. Finding never blank.
Note: TABLE_4 fills at SE-0, BEFORE TABLE_1.

**Schema ID: TABLE_5 — Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation`
Remediation = exact object + exact path + post-fix state. CS-EXPECTATION-VIOLATED: CS-Expected / SE-Actual / Delta.

**Schema ID: CS-2 — Sharing Rule Expectations**
Declared columns: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation`
SE-updatable: SE Cross-Reference (TABLE_4 row ID), SE Confirmation. Update protocol: after TABLE_4 at SE-0.

**Schema ID: CS-3 — Cross-Role Access Differential Expectations**
Declared columns: `Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation`
SE-updatable: SE Cross-Reference, SE Confirmation. Update protocol: after TABLE_1/TABLE_3.

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored, Phase 0)

**Declared rule: M1, M2, M3, M4 simultaneously active. M4 pre-assignments CA-1.1 through CA-1.9.**

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-0 + SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

**SHALL obligations (authored by CA, Phase 0):**

- SHALL-A: Complete TABLE_1 with Tier. All cells Granted/Denied/Conditional/N/A. Ordered by Tier.
- SHALL-B: TABLE_2 all sensitive fields with FLS status. Null case explicit with field list. Gap? YES → TABLE_5.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Effective Scope. Ambiguous → TABLE_5.
- SHALL-D: TABLE_4 all four vectors Checked? = YES at SE-0 before TABLE_1. Rule-outs name specific mechanism.
  - SHALL-D-EXT-C35: SE-4's STRUCTURED CLOSE MUST contain verbatim TABLE_4 row cross-reference: `Cite: TABLE_4 (filled at SE-0) row [exact vector label from TABLE_4] — [role] privilege ceiling: [escalation pattern or "no escalation path — [reason]"]`. CA-1.9 verifies as distinct target from CA-1.4 and CA-1.7.
- SHALL-E: TABLE_5 named gap. Zero-gap requires explicit evidence rows.
- SHALL-F: CS-EXPECTATION-VIOLATED three-field Remediation (CS-Expected / SE-Actual / Delta). CA-1.6 verifies.
- SHALL-G: SE-2/SE-3/SE-4 open with `MANUAL GAP [<exact CONTEXT label>]:` then `STRUCTURED CLOSE:`. CA-1.7 verifies character-for-character match.

**STRUCTURAL AXIS NON-INTERFERENCE DECLARATION** *(C-34 — V-05 adds self-scoping footer A-Meta)*

| Axis | Dimension | Criterion | Self-Evidence Mechanism | Non-Interference Statement |
|------|-----------|-----------|------------------------|---------------------------|
| A-1 | Execution order | C-31 | `### SE-0 / SHALL-D` section header precedes `### SE-1 / SHALL-A` in output body | Satisfying A-1 does not justify relaxing A-2 or A-3 |
| A-2 | Closure-note format | C-32 | `MANUAL GAP [...]:` / `STRUCTURED CLOSE:` exact-label two-part blocks open SE-2, SE-3, SE-4 | Satisfying A-2 does not justify relaxing A-1 or A-3 |
| A-3 | CS self-reference | C-33 | `### CS-0` section header cites Schema ID: CS-2 and Schema ID: CS-3 before CS-1 | Satisfying A-3 does not justify relaxing A-1 or A-2 |
| A-Meta | Declaration scope | — | This declaration is a preamble-only contract. It is NOT a CA-1 audit target. Its effect is verified exclusively through the non-overlapping scopes of CA-1.4 (A-1), CA-1.7 (A-2), and CA-1.8 (A-3). No CA-1 row should be added to audit this declaration directly. | — |

**ATTESTATION CROSS-LINK MANDATE (V-05 full extension):**

The CA terminal verdict MUST include a TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION table with rows A-1, A-2, A-3. Each row MUST name the dimension, criterion, and evidence source. The Evidence Source column MUST quote the exact output-body `###` section header string (verbatim, auditable by text search). Additionally: CA-1.4's preamble anchor MUST cite "(this row verifies axis A-1 — Execution order — as declared in the STRUCTURAL AXIS NON-INTERFERENCE DECLARATION, Phase 0)". CA-1.7's preamble anchor MUST cite "(this row verifies axis A-2 — Closure-note format — as declared in the STRUCTURAL AXIS NON-INTERFERENCE DECLARATION, Phase 0)". CA-1.8's preamble anchor MUST cite "(this row verifies axis A-3 — CS self-reference — as declared in the STRUCTURAL AXIS NON-INTERFERENCE DECLARATION, Phase 0)".

*Handing to PHASE 1 — SE.*

---

## PHASE 1 — SE: Security Analysis

### SE-0 / SHALL-D — Escalation Vector Inventory (executes BEFORE SE-1)

TABLE_4 fills here. This section header establishes the A-1 execution-order self-evidence marker in the output body.

**TABLE_4 — Escalation Vector Inventory** *(all four vectors required; Checked? = YES)*

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

Finding format for confirmed escalation: `[Role] -> [Mechanism: specific privilege name] -> [Elevated access achieved]`
Finding format for rule-out: "Checked [mechanism]: no path because [specific reason naming the exact configuration examined]."

After TABLE_4: populate SE Cross-Reference and SE Confirmation in CS-2 rows.

*SE-0 complete — handing to SE-1.*

### SE-1 / SHALL-A — Role-Operation Matrix

**TABLE_1 — Role-Operation Matrix** *(Schema Registry TABLE_1; Tier column required)*

| Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Every role with any privilege on {{topic}}. After table: cross-reference CS-3. Flag CS-EXPECTATION-VIOLATED per SHALL-F.

**Cross-role differential analysis:** Compare CS role against at least one more privileged role. State whether differential is expected or anomalous.

### SE-2 / SHALL-B — Field-Level Security Coverage

MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:
Column security profiles not discoverable from security roles UI; missing FLS discovered only after data exposure.

STRUCTURED CLOSE:
TABLE_2 enumerates every sensitive field with explicit FLS status. Not Configured → TABLE_5 as MISSING-FLS.

**TABLE_2 — FLS Coverage** *(Schema Registry TABLE_2)*

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

Null case: "No column security profiles active on {{topic}}. Sensitive fields: [list]. All entered in TABLE_5 as MISSING-FLS."

**Defense-in-depth layer check:** Identify enforcement layer for at least one sensitive field. Explain why the layer above does not override.

### SE-3 / SHALL-C — Record Access Scope

MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:
No single Dataverse UI view surfaces combined role + team + OWD effective access; spot-checking misses team-accumulated privilege.

STRUCTURED CLOSE:
TABLE_3 maps effective scope per role in one traceable row.

**TABLE_3 — Record Scope by Role** *(Schema Registry TABLE_3)*

| Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|------|--------------|----------------|-----------------|-----------|

Every TABLE_1 role MUST appear. Note team-membership scope expansions as CS-EXPECTATION-VIOLATED candidates.

After TABLE_3: populate SE Cross-Reference and SE Confirmation in CS-3 rows.

### SE-4 / SHALL-D — Privilege Escalation Analysis

MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:
OWD audited entity-by-entity without cross-referencing sharing rules that silently override them; effective org-wide access invisible in security roles UI.

STRUCTURED CLOSE:
TABLE_4 (filled at SE-0) surfaced escalation vectors before TABLE_1, establishing privilege ceiling first. CS-2 sharing rule expectations confirmed or contradicted.

Cite: TABLE_4 (filled at SE-0) row [exact vector label from TABLE_4] — [role] privilege ceiling: [escalation pattern or "no escalation path — [specific control preventing it]"].

[For each confirmed escalation path: trace to terminal access level. For each rule-out: confirm the specific control.]

### SE-5 / SHALL-E — Security Gap Inventory

**TABLE_5 — Security Gap Inventory** *(Schema Registry TABLE_5)*

| # | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation |
|---|----------|--------|---------------|------|------|----------|-------------|

Gap Types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED / CS-EXPECTATION-VIOLATED.
CS-EXPECTATION-VIOLATED: three-field Remediation (CS-Expected / SE-Actual / Delta).

*Handing to PHASE 2 — CS.*

---

## PHASE 2 — CS: Customer Success Analysis

### CS-0 — Schema Registry Acknowledgment (executes before CS-1)

This section header establishes the A-3 execution-order self-evidence marker. CS cites Schema Registry entries by exact Schema ID label before producing any analysis:

- Schema ID: CS-2 — Sharing Rule Expectations. SE-updatable columns: SE Cross-Reference (TABLE_4 row ID), SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE).
- Schema ID: CS-3 — Cross-Role Access Differential Expectations. SE-updatable columns: SE Cross-Reference (TABLE_1 or TABLE_3 row ID), SE Confirmation.

*CS-0 complete — proceeding to CS-1.*

### CS-1 — Qualitative Baseline

For each entity in {{topic}} scope: (a) Expected CRUD for CS role? (b) Expected record scope? (c) Sensitive fields CS needs, and why? (d) Configuration risks that may open access beyond job requirements? Name business process, at least two personas, expected access pattern per persona.

### CS-2 — Sharing Rule Expectations *(SE populates SE Cross-Reference and SE Confirmation)*

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation |
|-----------|---------|------------------------|-----------------------|---------------------|---------------------|-----------------|

### CS-3 — Cross-Role Access Differential Expectations *(SE populates SE Cross-Reference and SE Confirmation)*

| Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation |
|--------|-----------|------------------------|-----------------|-----------------------------|----------------------|---------------------|-----------------|

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

*CA returns.*

| CA Row | Audit Target | Criterion | Non-Overlapping Scope |
|--------|-------------|-----------|----------------------|
| CA-1.1 | TABLE_1 completeness | C-01 | Cell coverage and role enumeration |
| CA-1.2 | TABLE_2 FLS | C-02 | Sensitive field status and null-case declaration |
| CA-1.3 | TABLE_3 scope | C-03 | Effective scope completeness per TABLE_1 role |
| CA-1.4 | TABLE_4 SE-0 ordering — axis A-1 | C-04 | SE-0 before SE-1; four vectors Checked? = YES |
| CA-1.5 | TABLE_5 gap inventory | C-05 | Named gap; exact remediation |
| CA-1.6 | SHALL-F structure | SHALL-F | CS-EXPECTATION-VIOLATED three-field completeness |
| CA-1.7 | MANUAL GAP labels — axis A-2 | SHALL-G | Character-for-character label at SE-2/SE-3/SE-4 |
| CA-1.8 | CS-0 acknowledgment — axis A-3 | C-33 | CS-0 before CS-1; exact Schema ID strings |
| CA-1.9 | SE-4 verbatim cite | SHALL-D-EXT-C35 | Verbatim Cite: format in SE-4 STRUCTURED CLOSE only |

NON-OVERLAP DECLARATION:
[CA-1.4]: SE-0 ordering and four-vector presence only — not label matching or verbatim cite.
[CA-1.7]: Exact CONTEXT label carry-through at SE-2/SE-3/SE-4 only — not ordering or verbatim cite.
[CA-1.9]: SE-4 STRUCTURED CLOSE verbatim `Cite: TABLE_4 (filled at SE-0) row` format only — not ordering or label matching.
[Axis declaration]: The STRUCTURAL AXIS NON-INTERFERENCE DECLARATION's A-Meta footer row established that it is a preamble-only contract with no CA-1 audit target. This fourth non-overlap statement affirms that CA-1 honors A-Meta's self-scoping: verification routes exclusively through the non-overlap of CA-1.4/CA-1.7/CA-1.8.

**CA-1.1** *(completing Phase 0 M4 pre-assignment CA-1.1)*:

Registry anchor — Schema ID TABLE_1: [Role, Tier, Create, Read, Write, Delete, Append, AppendTo, Assign, Share, Record Scope] — blank cells prohibited globally; Tier ordered Admin/Custom/Restricted.

Preamble anchor — C-01 as authored by CA in Phase 0: TABLE_1 / SE-1 / SHALL-A / CA-1.1 — verifying...

Verification — TABLE_1 present? Every cell Granted/Denied/Conditional/N/A? All roles with Tier ordered? -> PASS / FAIL

**CA-1.2** *(completing Phase 0 M4 pre-assignment CA-1.2)*:

Registry anchor — Schema ID TABLE_2: [Entity, Field, Category, FLS Profile Configured?, Roles: Read, Roles: Write, Gap?] — blank cells prohibited globally.

Preamble anchor — C-02 as authored by CA in Phase 0: TABLE_2 / SE-2 / SHALL-B / CA-1.2 — verifying...

Verification — TABLE_2 present? Sensitive fields with FLS status? Null case stated? Gap? YES in TABLE_5? -> PASS / FAIL

**CA-1.3** *(completing Phase 0 M4 pre-assignment CA-1.3)*:

Registry anchor — Schema ID TABLE_3: [Role, Tier, OWD Baseline, Scope Modifier, Effective Scope, Verified?] — blank cells prohibited globally.

Preamble anchor — C-03 as authored by CA in Phase 0: TABLE_3 / SE-1+SE-3 / SHALL-C / CA-1.3 — verifying...

Verification — Every TABLE_1 role in TABLE_3? Effective Scope filled? Ambiguous in TABLE_5? -> PASS / FAIL

**CA-1.4** *(completing Phase 0 M4 pre-assignment CA-1.4; this row verifies axis A-1 — Execution order — as declared in the STRUCTURAL AXIS NON-INTERFERENCE DECLARATION, Phase 0)*:

Registry anchor — Schema ID TABLE_4: [Vector, Checked?, Finding, Severity] — all four vectors; TABLE_4 fills at SE-0 before TABLE_1 per Registry note.

Preamble anchor — C-04 as authored by CA in Phase 0: TABLE_4 / SE-0+SE-4 / SHALL-D / CA-1.4 — verifying SE-0 ordering only (A-1 axis scope; does not extend to label matching [CA-1.7] or verbatim cite format [CA-1.9])...

Verification — TABLE_4 present? All four vectors Checked? = YES? SE-0 section header precedes SE-1 section header in output body? -> PASS / FAIL

**CA-1.5** *(completing Phase 0 M4 pre-assignment CA-1.5)*:

Registry anchor — Schema ID TABLE_5: [#, Gap Type, Entity, Field or Rule, Role, Tier, Severity, Remediation] — blank cells prohibited globally.

Preamble anchor — C-05 as authored by CA in Phase 0: TABLE_5 / SE-5 / SHALL-E / CA-1.5 — verifying...

Verification — TABLE_5 present? Named gap with specific field/role/rule? Remediations exact (object + path + post-fix state)? -> PASS / FAIL

**CA-1.6**:

Registry anchor — CS-EXPECTATION-VIOLATED structure: [CS-Expected citing CS-2/CS-3 row ID, SE-Actual naming diverging finding, Delta stating exact configuration change] — all three fields required.

Preamble anchor — SHALL-F as authored by CA in Phase 0: three-field block mandatory; incomplete rows MUST be reopened — verifying...

Verification — Each CS-EXPECTATION-VIOLATED row has CS-Expected, SE-Actual, and Delta populated? -> PASS / FAIL per row.

**CA-1.7** *(completing Phase 0 M4 pre-assignment CA-1.7; this row verifies axis A-2 — Closure-note format — as declared in the STRUCTURAL AXIS NON-INTERFERENCE DECLARATION, Phase 0)*:

Registry anchor — CONTEXT labels verbatim: "Blind spot 1 — Post-incident FLS gap" (SE-2 target), "Blind spot 2 — Cumulative privilege blind spot" (SE-3 target), "Blind spot 3 — OWD-sharing-rule override gap" (SE-4 target). SHALL-G format: `MANUAL GAP [<exact label>]:` then `STRUCTURED CLOSE:`.

Preamble anchor — SHALL-G as authored by CA in Phase 0: Line 1 MUST begin `MANUAL GAP [<exact CONTEXT label>]:` — character-for-character match (A-2 axis scope; does not extend to ordering [CA-1.4] or verbatim cite format [CA-1.9])...

Verification — SE-2 opens with `MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:`? SE-3 opens with `MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:`? SE-4 opens with `MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:`? Each with `STRUCTURED CLOSE:`? -> PASS / FAIL per section.

**CA-1.8** *(completing Phase 0 M4 pre-assignment CA-1.8; this row verifies axis A-3 — CS self-reference — as declared in the STRUCTURAL AXIS NON-INTERFERENCE DECLARATION, Phase 0)*:

Registry anchor — Schema Registry entries: "CS-2 — Sharing Rule Expectations" with SE-updatable column declarations; "CS-3 — Cross-Role Access Differential Expectations" with SE-updatable column declarations.

Preamble anchor — C-33 as authored by CA in Phase 0: CS-0 MUST cite Schema ID: CS-2 and Schema ID: CS-3 by exact label before CS-1 content (A-3 axis scope; does not extend to ordering [CA-1.4] or label matching [CA-1.7])...

Verification — CS-0 present as labeled sub-step? Quotes exact "Schema ID: CS-2" and "Schema ID: CS-3" strings? CS-0 precedes CS-1? -> PASS / FAIL

**CA-1.9** *(completing Phase 0 M4 pre-assignment CA-1.9; distinct from CA-1.4 and CA-1.7)*:

Registry anchor — Schema ID TABLE_4 note: "fills at SE-0, BEFORE TABLE_1". SHALL-D-EXT-C35: SE-4 STRUCTURED CLOSE MUST contain `Cite: TABLE_4 (filled at SE-0) row [exact vector label] — [role] privilege ceiling: [pattern]` verbatim.

Preamble anchor — SHALL-D-EXT-C35 as authored by CA in Phase 0: verbatim Cite: format in SE-4 STRUCTURED CLOSE — scope is exclusively the verbatim cite format, distinct from CA-1.4 (SE-0 ordering) and CA-1.7 (MANUAL GAP label matching)...

Verification — SE-4 STRUCTURED CLOSE contains `Cite: TABLE_4 (filled at SE-0) row` verbatim? Followed by exact vector label from TABLE_4? Followed by privilege ceiling description? -> PASS / FAIL

**CA Format Compliance Verdict (Phase 0 citation):**

Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0), Phase 0 by label.

[C-01–C-05: CA-1.1–CA-1.5 results. SHALL-F three-field structure: CA-1.6. SHALL-G exact-label blocks: CA-1.7. CS-0 acknowledgment: CA-1.8. SE-4 STRUCTURED CLOSE verbatim cite: CA-1.9. Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

**TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION** *(C-36 — V-05 full: verbatim section headers + A-N labels in CA-1.N rows + self-scoping A-Meta footer)*:

| Axis | Dimension | Criterion | Evidence Source (verbatim output-body section header) | Status |
|------|-----------|-----------|------------------------------------------------------|--------|
| A-1 | Execution order | C-31 | `### SE-0 / SHALL-D — Escalation Vector Inventory (executes BEFORE SE-1)` precedes `### SE-1 / SHALL-A — Role-Operation Matrix`; CA-1.4 preamble anchor cites axis A-1 label completing the three-point chain | CONFIRMED |
| A-2 | Closure-note format | C-32 | `### SE-2 / SHALL-B — Field-Level Security Coverage` opens with `MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:` / `STRUCTURED CLOSE:`; same pattern at SE-3 and SE-4; CA-1.7 preamble anchor cites axis A-2 label | CONFIRMED |
| A-3 | CS self-reference | C-33 | `### CS-0 — Schema Registry Acknowledgment (executes before CS-1)` quotes `Schema ID: CS-2` and `Schema ID: CS-3` verbatim before `### CS-1 — Qualitative Baseline`; CA-1.8 preamble anchor cites axis A-3 label | CONFIRMED |

Three-point A-N label chain closed: (1) preamble STRUCTURAL AXIS NON-INTERFERENCE DECLARATION declares A-1/A-2/A-3 with A-Meta self-scoping footer — (2) CA-1.4/CA-1.7/CA-1.8 preamble anchors each cite their A-N axis label by exact string — (3) attestation Evidence Source column quotes verbatim output-body section headers auditable by text search. Each link independently verifiable without prompt inspection. A-Meta self-scoping footer established that this chain terminates at A-1/A-2/A-3 and does not require a fourth attestation row.
