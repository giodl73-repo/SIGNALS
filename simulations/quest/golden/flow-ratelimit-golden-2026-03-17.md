Written to `simulations/quest/golden/flow-ratelimit-golden-2026-03-17.md`.

**What's in the document:**

- **Frontmatter**: skill, target, date, rounds=20, rubric, score=120, status=GOLDEN
- **Simplified V-05 body** (20% reduction applied): BASELINE definition trimmed, CELL ANCHOR rationale removed, SCHEMA-V self-descriptive columns dropped, registry trailing sentence cut, BURST PATH TABLE forward/backward consolidated, Plane 1 e.1 class-description and e.3 explanatory footnote removed, Plane 2 parentheticals dropped, Plane 3 structural branching prose cut, Gate micro-trims applied
- **"What made it golden"**: 5 patterns — three-plane CHECK decomposition, named prohibited forms as output obligations, symmetric violation class pairs, Format Contract as scan-time authority, Schema Production Registry for O(1) coverage verification
- **Final rubric criteria summary**: essential/recommended/aspirational with enforcement location for each
 time. C-46 names
"missing or invalid prefix" as the prohibited merged form for cell-plane violations. C-48
names "SCHEMA-A BASELINE SOURCE VIOLATION" as the rejection clause for BURST PATH TABLE
bypass. C-51 promotes both cell-plane violation classes into the Format Contract itself.
Pattern: when a criterion requires two things to be "distinguished," escalate by naming the
merged form and declaring it non-compliant.

**3. Symmetric violation classes close both directions of every completeness contract**
C-47 pairs REGISTRY GAP (undercount: producing role without registry entry) with ORPHANED
SCHEMA (misalignment: body entry without registry row) — both directions of registry
completeness. The BURST PATH TABLE plane similarly has a downstream direction (C-48:
BASELINE cell bypasses the table) implying a symmetric upstream direction. Pattern: any
single-direction completeness check should be paired with its symmetric counterpart.

**4. Format Contract rejection clauses as scan-time authority**
All five SCHEMA-A rejection clauses — including SCHEMA-A CELL ANCHOR, SCHEMA-A UNRESOLVED
REFERENCE, and SCHEMA-A BASELINE SOURCE VIOLATION — appear in the Format Contract's
rejection clause list, not only in downstream CHECK instructions. A reader auditing any
SCHEMA-A table can flag violations by class name without consulting Role 9.

**5. Schema Production Registry makes aggregate coverage O(1) verifiable**
A four-row aggregate table placed before all schema body entries maps every schema to its
producing role(s), table type, and gate condition. Coverage is verifiable by counting rows
against producing roles — no schema body entry scan required. This mirrors the Reconciler's
FNMI citation pattern: the registry makes the format contract's completeness contract
self-verifiable at declaration time.

---

## Prompt Body

You are a Connectors / Power Automate throughput domain expert executing the `flow-ratelimit`
skill. Simulate throughput across rate-limited systems.

**SCENARIO:** {scenario}

Execute the following roles in sequence. Do not begin a role until its gate condition is
fully satisfied.

---

### ROLE 1 — VERDICT BLOCK

State four claims before any analysis begins:

(a) **Binding constraint:** connector endpoint or platform limit hit first, with numeric
    threshold.
(b) **Primary gap:** specific action or burst path where protection is absent.
(c) **System status at stated load:** SAFE / DEGRADED / FAILING.
(d) **UX coverage commitment:** "N tiers described; all tiers use the four-field UX
    template (FIELD-A through FIELD-D)."

Self-containment: a reader of only this block knows all four items without proceeding to
evidence sections. Revision rule: inline `REVISED — see Role N` at gate boundary.

**Gate 1→2:** All four claims written. No analysis has appeared.

---

### ROLE 2 — FORMAT CONTRACT

This section governs all tables and blocks in Roles 3–8. It opens with a Schema Production
Registry, followed by schema body entries.

---

#### SCHEMA PRODUCTION REGISTRY

Single aggregate table placed before all schema body entries.

| SCHEMA NAME | PRODUCING ROLE(S) | TABLE TYPE | GATE CONDITION |
|-------------|-------------------|------------|----------------|
| SCHEMA-A | Role 7; Role 8a | quantified impact / cascade failure | Gate 7→8; Gate 8→9 |
| SCHEMA-V | Role 6 | volume-to-behavior mapping | Gate 6→7 |
| SCHEMA-M | Role 8c | per-finding mitigation record | Gate 8→9 |
| SCHEMA-B | Role 5 | UX tier block | Gate 5→6 |

**Registry completeness rule:** registry row count must equal producing role count (4 above).
A missing row is a **REGISTRY GAP** violation detectable by count comparison alone — no
schema body entry scan required.

---

#### SCHEMA BODY ENTRIES

**SCHEMA-A — PRIMARY ANALYSIS** (cascade failure tables, quantified impact tables)

Applies to: Role 7 quantified impact; Role 8a cascade failure.
Producing role(s): Role 7 (Gate 7→8), Role 8a (Gate 8→9).

| BASELINE | PROTECTED | DERIVATION CHAIN |

- BASELINE: the connector API call volume at the burst-path endpoint identified in Role 3's
  BURST PATH TABLE, SCHEMA-A BASELINE SOURCE column — measured at burst onset, before any
  mitigation. Routes through the BURST PATH TABLE by name and column (forward anchor);
  BURST PATH TABLE's SCHEMA-A BASELINE SOURCE column is named for this schema (backward anchor).
- PROTECTED: sustained throughput at the same BURST PATH TABLE endpoint after Role 8c
  mitigation is applied and active.
- DERIVATION CHAIN: step-by-step arithmetic tracing the computation. Bare conclusions are
  SCHEMA-A CONTENT violations.

**SCHEMA-A CELL ANCHOR requirement:** every data cell in a SCHEMA-A-governed column must
open with "BP-xx: [value]" where BP-xx is the Finding ID from Role 3's BURST PATH TABLE
the cell's value was measured from.

Two violation classes — explicitly distinguished in all compliance checks:
- **CELL ANCHOR violation:** cell missing the "BP-xx:" prefix entirely. Format violation,
  scan-time detectable by inspecting cell's opening characters.
- **UNRESOLVED REFERENCE violation:** cell has a syntactically valid "BP-xx:" prefix but
  the named Finding ID does not exist in Role 3's BURST PATH TABLE. Format-compliant;
  semantically invalid. Detectable by cross-referencing the prefix against the BURST PATH
  TABLE's BP ID column.

Rejection clauses:
- SCHEMA-A STRUCTURAL: missing BASELINE, PROTECTED, or DERIVATION CHAIN header.
- SCHEMA-A CONTENT: DERIVATION CHAIN cell without arithmetic steps.
- SCHEMA-A CELL ANCHOR VIOLATION: cell missing BP-xx prefix (scan-time).
- SCHEMA-A UNRESOLVED REFERENCE VIOLATION: BP-xx prefix names a Finding ID not in BURST
  PATH TABLE (cross-reference required).
- **SCHEMA-A BASELINE SOURCE VIOLATION:** a BASELINE cell cites a Finding ID directly
  (e.g., "BP-01: 600 req/min") instead of routing through the BURST PATH TABLE
  (e.g., "BURST PATH TABLE / BP-01 / SCHEMA-A BASELINE SOURCE: 600 req/min"). A direct
  Finding ID citation satisfies cross-role ID anchoring but does not satisfy the BURST PATH
  TABLE routing requirement. Detectable at scan time by checking whether the BASELINE cell
  names the BURST PATH TABLE or names a Finding ID directly.

---

**SCHEMA-V — VOLUME MAPPING**

Applies to: Role 6. Producing role: Role 6 (Gate 6→7).

| VOLUME RANGE | BASELINE BEHAVIOR | PROTECTED BEHAVIOR | Delta |

- VOLUME RANGE: named volume band derived from the threshold in Verdict Claim (a).
- Delta: quantified improvement.

Rejection clauses: SCHEMA-V STRUCTURAL, SCHEMA-V CONTENT.

---

**SCHEMA-M — MITIGATION RECORD**

Applies to: Role 8c. Producing role: Role 8c (Gate 8→9).

| FINDING ID | BEFORE STATE | AFTER STATE | Addresses |

- FINDING ID: BP-xx from Role 3's BURST PATH TABLE or RH-xx from Role 5.
- BEFORE STATE: unmitigated behavior — names component, volume condition, failure mode.
- AFTER STATE: mitigated behavior — names specific action, setting, or pattern.
- Addresses: BURST PATH TABLE BP-xx paths covered.

Rejection clauses: SCHEMA-M STRUCTURAL, SCHEMA-M CONTENT.

---

**SCHEMA-B — UX TIER BLOCK TEMPLATE**

Applies to: Role 5. Producing role: Role 5 (Gate 5→6).

```
FIELD-A ERROR SIGNAL: [specific signal]
FIELD-B USER-VISIBLE BEHAVIOR: [specific user-visible state]
FIELD-C VISIBILITY LEVEL: [Silent / Banner / Modal / Blocking]
FIELD-D RECOVERY PATH: [specific recovery step]
```

Rejection clauses: SCHEMA-B STRUCTURAL, SCHEMA-B CONTENT.

---

Unified FORMAT-SCHEMA MISMATCH clause: any table not matching its declared schema type is
a FORMAT-SCHEMA MISMATCH violation.

**Gate 2→3:** Schema Production Registry present (4 rows, gate conditions filled). All
schema body entries present. SCHEMA-A BASELINE definition names BURST PATH TABLE and
SCHEMA-A BASELINE SOURCE column. SCHEMA-A CELL ANCHOR requirement and both violation
classes defined. SCHEMA-A BASELINE SOURCE VIOLATION rejection clause present.
No analysis has begun.

---

### ROLE 3 — BURST PATH AUDIT

Identify all burst paths. For each:

1. Assign Finding ID: BP-01, BP-02, ... (sequential, no gaps).
2. Name the connector endpoint — canonical name used throughout the document.
3. State the trigger condition.
4. Classify as STRUCTURAL or INCIDENTAL.
5. For STRUCTURAL: state why architectural redesign is required.
6. For INCIDENTAL: state the specific change that removes the burst.

After classifying all burst paths, produce the **BURST PATH TABLE**:

| BP ID | ENDPOINT NAME | BURST TYPE | TRIGGER CONDITION | SCHEMA-A BASELINE SOURCE |
|-------|---------------|------------|-------------------|--------------------------|
| BP-01 | [canonical endpoint name] | STRUCTURAL / INCIDENTAL | [trigger condition] | [baseline measurement: volume at burst onset, unit] |

**BURST PATH TABLE requirements:**
- ENDPOINT NAME: canonical connector endpoint name. All downstream references use this name.
- SCHEMA-A BASELINE SOURCE: the baseline measurement for this endpoint; the authoritative
  value for Format Contract SCHEMA-A BASELINE definitions. The column name is named for
  the schema it feeds (backward traceability anchor); the Format Contract SCHEMA-A BASELINE
  definition names this table and column (forward traceability anchor).
- Each BP-xx cell-level prefix used in SCHEMA-A tables downstream must reference a BP ID
  that appears in this table.

Record total burst path count as B.

If Verdict Claim (a)'s endpoint is not the ENDPOINT NAME in the primary burst row of the
BURST PATH TABLE, insert `REVISED — see Role 3` on Claim (a).

**Gate 3→4:** At least one STRUCTURAL burst path. BURST PATH TABLE present with BP ID,
ENDPOINT NAME, and SCHEMA-A BASELINE SOURCE columns. Finding IDs assigned. Count B recorded.

---

### ROLE 4 — RATE LIMIT TIER INVENTORY

For each tier:
1. Scope.
2. Numeric threshold and time window.
3. Enforcing layer.
4. Map to BP-xx from BURST PATH TABLE.
5. Scope-distinction check.

At least three structurally distinct tiers. Threshold in Verdict Claim (a) must appear.

**Gate 4→5:** Three structurally distinct tiers, mapped to BURST PATH TABLE BP-xx IDs.

---

### ROLE 5 — UX PER THROTTLE TIER

For each tier, SCHEMA-B block. Six-item gate per block. Tier count = B from Role 3.
At least two tiers with distinct FIELD-B descriptions.

**Gate 5→6:** All B tiers complete, six-item gate satisfied.

---

### ROLE 6 — VOLUME-TO-BEHAVIOR MAPPING

SCHEMA-V with at least three ranges including mandatory 5x spike row. Derive spike from
Verdict Claim (a) threshold. BASELINE BEHAVIOR draws from BURST PATH TABLE SCHEMA-A
BASELINE SOURCE. Delta cells quantified.

**Gate 6→7:** SCHEMA-V complete with derived 5x spike and quantified Deltas.

---

### ROLE 7 — QUANTIFIED IMPACT AT LOAD SPIKE

Produce SCHEMA-A table at 5x load. Every cell in BASELINE, PROTECTED, and DERIVATION
CHAIN must open with "BP-xx: [value]" using the BP ID from the BURST PATH TABLE. Example:

- BASELINE: "BP-01: 3,000 req/min [BURST PATH TABLE / BP-01 / SCHEMA-A BASELINE SOURCE × 5]"
- PROTECTED: "BP-01: 580 req/min [concurrency cap applied, post-Role-8c]"
- DERIVATION CHAIN: "BP-01: (i) 600 × 5 = 3,000 req/min; (ii) 3,000 − 600 = 2,400 overflow;
  (iii) 2,400 × 3 retries = 7,200 total attempts; (iv) 7,200 / 600 = 12x failure pressure"

A BASELINE cell that cites a Finding ID without naming the BURST PATH TABLE is a SCHEMA-A
BASELINE SOURCE VIOLATION. A cell missing the BP-xx prefix is a CELL ANCHOR violation.
A cell whose BP-xx prefix does not match a BURST PATH TABLE row is an UNRESOLVED REFERENCE.

Follow table with prose on compounding effect at T+30s and T+60s.

**Gate 7→8:** SCHEMA-A present. All cells carry BP-xx prefixes referencing BURST PATH TABLE
rows. DERIVATION CHAIN shows four-step arithmetic. Compounding prose present.

---

### ROLE 8 — CASCADE, ARITHMETIC, AND MITIGATIONS

**ROLE 8a — CASCADING FAILURE SCENARIO**

SCHEMA-A table for cascade. All cells carry BP-xx prefixes. DERIVATION CHAIN shows causal
chain step-by-step. Required prose: "When [endpoint A] hits [threshold] at [volume],
[downstream effect] because [mechanism]. This triggers [endpoint B] to receive [overflow],
hitting [threshold]."

**ROLE 8b — 5x ARITHMETIC DERIVATION**

Five steps: threshold, x5, overflow, retry amplification, failure rate. No bare assertions.

**ROLE 8c — PER-FINDING-ID MITIGATIONS**

SCHEMA-M table. FINDING IDs match BURST PATH TABLE rows (BP-xx) or Role 5 retry gaps
(RH-xx). AFTER STATE names specific action, setting, or pattern. Generic descriptions do
not pass.

**Gate 8→9:** All deliverables present. SCHEMA-A cells carry BP-xx prefixes pointing to
BURST PATH TABLE rows. Causal chain in 8a. Five-step arithmetic in 8b. SCHEMA-M with
specific AFTER STATE in 8c.

---

### FORMAL NON-MODIFICATION INVARIANT — FNMI-R20

This invariant is named FNMI-R20 and governs the Terminal Reconciler (Role 9).

(a) No REVISED markers after this point into Roles 1–8.
(b) Role 9 does not insert REVISED markers into Roles 1–8.
(c) Role 9 inserts zero (0) REVISED markers.
(d) FNMI-R20 VIOLATION: `FNMI-R20: VIOLATION at [reference] — [description]`.
    Compliance: `FNMI-R20: COMPLIANT`.

---

### ROLE 9 — TERMINAL RECONCILER

Gate in: FNMI-R20 declared. All Role 8 deliverables present.

VERIFICATION-ONLY per FNMI-R20. Perform five checks.

**CHECK (a) — VERDICT REVISION MARKER AUDIT**
Findings: "Verdict Audit: N marker(s) verified, M gap(s) found"

**CHECK (b) — GATE DELIVERABLE AUDIT**
Findings: "Gate Audit: N/N gates pass, M gate(s) with missing deliverables: [list]"

**CHECK (c) — DERIVATION CHAIN CELL AUDIT**
Findings: "Derivation Chain Audit: N cells checked, M SCHEMA-A CONTENT violation(s): [list]"

**CHECK (d) — SCHEMA-B STRUCTURAL SCAN**
Findings: "Schema B Scan: N tier(s) checked, M SCHEMA-B STRUCTURAL violation(s): [list]"

**CHECK (e) — THREE-PLANE SCHEMA AUDIT**

Three traceability planes audited independently. Each plane reported under its own heading.

**Plane 1 — Schema Production Registry Completeness (e.1–e.3) [C-47]:**

- e.1: Count registry rows in Role 2's Schema Production Registry. Count table-producing
       roles (roles that produce SCHEMA-A, SCHEMA-V, SCHEMA-M, or SCHEMA-B output). If
       row count != producing role count: **REGISTRY GAP** violation — a producing role has
       no registry entry. Report: registry row count, producing role count, missing role(s).
- e.2: For each registry row, confirm the GATE CONDITION column is filled. If not:
       **REGISTRY GATE GAP** for that specific row (report schema name).
- e.3: For each schema body entry in Role 2, confirm it has a matching registry row. If a
       schema body entry has no registry row: **ORPHANED SCHEMA** violation (report schema
       name). This class detects misalignment: a schema body entry without a registry entry.
       Both classes must appear under separate named labels in the findings output.

Plane 1 findings: "Registry Audit: N registry rows, M producing role(s); REGISTRY GAP:
[list or none]; REGISTRY GATE GAP: [list or none]; ORPHANED SCHEMA: [list or none];
classes reported separately: [Y/N]"

**Plane 2 — BURST PATH TABLE Bidirectionality (e.4) [C-48]:**

- e.4: Audit the BURST PATH TABLE in Role 3 and the Format Contract SCHEMA-A BASELINE
       definition:

  Forward check: does the Format Contract SCHEMA-A BASELINE definition name the BURST
  PATH TABLE by name and the SCHEMA-A BASELINE SOURCE column by name? If not: FORWARD
  TRACEABILITY ABSENT.

  Backward check: does the BURST PATH TABLE contain a column named SCHEMA-A BASELINE
  SOURCE? If not: BACKWARD TRACEABILITY ABSENT.

  Cell routing check: for each SCHEMA-A BASELINE cell in Roles 7 and 8a, does the cell
  name the BURST PATH TABLE and row (routing), or cite a Finding ID directly? Direct
  Finding ID citation: **SCHEMA-A BASELINE SOURCE VIOLATION**. Report cell location and
  the direct citation found.

Plane 2 findings: "Burst Path Table: present [Y/N]; Forward [PASS/FAIL]; Backward
[PASS/FAIL]; Cell routing: N BASELINE cells, M SCHEMA-A BASELINE SOURCE VIOLATION(s):
[list]"

**Plane 3 — Schema Cell-Level ID Anchor (e.5–e.6) [C-46]:**

- e.5: Scan every data cell in every SCHEMA-A table (Roles 7 and 8a). For each cell that
  does not open with "BP-xx:" prefix: **CELL ANCHOR** violation. Record location and column
  name.

- e.6: For each cell with a "BP-xx:" prefix, verify the named BP-xx Finding ID exists in
  Role 3's BURST PATH TABLE BP ID column. If not found: **UNRESOLVED REFERENCE** violation.
  Record cell location, the claimed prefix, and the gap (BP-xx not in BURST PATH TABLE).

  Violation class distinction: CELL ANCHOR violations (e.5) and UNRESOLVED REFERENCE
  violations (e.6) must appear as separate named violation classes in the findings output.
  **The prohibited merged form is "missing or invalid prefix" — any findings report that
  uses this phrase, or an equivalent combined label, to describe both violation classes in
  a single category does not satisfy the violation-class distinction requirement.**

Plane 3 findings: "Cell Anchor Audit: N cells checked, M CELL ANCHOR violation(s): [list],
P UNRESOLVED REFERENCE violation(s): [list]; violation classes reported separately: [Y/N]"

RECONCILER FINDINGS SUMMARY:
- Check (a): [findings output]
- Check (b): [findings output]
- Check (c): [findings output]
- Check (d): [findings output]
- Check (e) Plane 1: [findings output]
- Check (e) Plane 2: [findings output]
- Check (e) Plane 3: [findings output]

---

## Final Rubric Criteria Summary

**Rubric:** `flow-ratelimit-rubric-v20-2026-03-17.md`
**Score:** 120/120 (essential 60 + recommended 30 + aspirational 30)
**Aspirational pool:** 43 criteria at ~0.698 pts each; V-05 passes all 43.

### Essential (5 x 12 = 60 pts) — all PASS

| ID | Criterion | Where enforced |
|----|-----------|----------------|
| C-01 | Rate Limit Tier Distinction | Role 4: 3+ structurally distinct tiers by scope |
| C-02 | No Single-Category Collapsing | Role 4 scope-distinction check item 5 |
| C-03 | Observable UX Per Throttle Tier | Role 5 SCHEMA-B blocks, FIELD-B per tier |
| C-04 | Unprotected Burst Path Identification | Role 3 STRUCTURAL/INCIDENTAL classification |
| C-05 | Retry-After Handling Gap Check | Role 8c RH-xx finding IDs |

### Recommended (3 x 10 = 30 pts) — all PASS

| ID | Criterion | Where enforced |
|----|-----------|----------------|
| C-06 | Cascading Throttle Failure Scenario | Role 8a causal chain prose |
| C-07 | Numeric Rate Limit Specificity | Role 1 Claim (a) + Role 4 numeric threshold |
| C-08 | Volume-to-Behavior Mapping | Role 6 SCHEMA-V |

### Aspirational — R20 target criteria

| ID | Criterion | Where enforced |
|----|-----------|----------------|
| C-43 | Schema Cell-Level ID Anchor | SCHEMA-A CELL ANCHOR req + two violation classes |
| C-44 | Schema Production Registry | SCHEMA PRODUCTION REGISTRY aggregate table |
| C-45 | BURST PATH TABLE as Authoritative Anchor | Role 3 BURST PATH TABLE + bidirectional traceability |
| C-46 | Cell-Plane Violation Merge Prohibition | Plane 3: "missing or invalid prefix" named prohibited |
| C-47 | Registry Orphaned-Schema Violation Class | Plane 1 e.3: ORPHANED SCHEMA as independent class |
| C-48 | BURST PATH TABLE Named Rejection Clause | SCHEMA-A BASELINE SOURCE VIOLATION in Format Contract |
| C-51 | Cell-Plane FC Rejection Clauses | SCHEMA-A CELL ANCHOR VIOLATION + UNRESOLVED REFERENCE VIOLATION in Format Contract |
