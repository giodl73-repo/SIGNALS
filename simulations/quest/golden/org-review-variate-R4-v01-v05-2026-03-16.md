# org-review Variations -- Round 4 (v4 rubric, 2026-03-16)

Generated: 2026-03-16
Skill: org-review
Rubric: simulations/quest/rubrics/org-review-rubric-v4-2026-03-16.md

## Prior Round Summary

- R1 (v1 rubric): V-05 best. E-1 (verdict-preview tables -> C-11) and E-2 (count constraint -> C-12) identified.
- R2 (v2 rubric): V-05=120/120. E-3 (LIFECYCLE-before-DOMAIN -> C-14) and E-4 (NULL HYPOTHESIS REGISTER -> C-13) confirmed. v3 raised max to 120.
- R3 (v3 rubric): V-05=120/120 entering R3. E-5 (SCOPE SURFACE REGISTER -> C-15), E-6 (FINDING SURFACE LINKAGE TABLE -> C-16), E-7 (§2a severity chain -> C-17) identified. v4 raises max to 135.
- R3 retroactive (v4 rubric): V-05 R3 carries all 17 criteria. Baseline for R4 = V-05 R3 at 135/135.

## Round 4 Strategy

All R4 variants inherit V-05 R3 as non-negotiable base. Round 4 is a frontier-extension round.

V-05 R3 satisfies all 17 criteria (max 135 under v4). Round 4 explores axes that could surface C-18+ patterns for a future v5 rubric.

Three new single-axis hypotheses, then two combinations:

| Variation | Axis | New Hypothesis |
|-----------|------|----------------|
| V-01 | Role sequence | A formal LIFECYCLE HANDOFF PACKET -- produced after LIFECYCLE and consumed by DOMAIN at section open -- prevents DOMAIN from running without acknowledging lifecycle-identified gaps; converts C-14 from ordering guarantee to ordering + handoff guarantee |
| V-02 | Output format | Making the FINDING SURFACE LINKAGE TABLE the *primary* finding record (prose disallowed except as attached detail for CRITICAL rows) elevates C-16 from structural presence to structural primacy; adds a FINDING TALLY row at table foot for §2a aggregation verification |
| V-03 | Inertia framing | Expanding challenger inertia framing into every reviewer section (each role explicitly assesses whether the status-quo from the NULL HYPOTHESIS REGISTER survives their lens) creates a per-role inertia verdict column and a final INERTIA DEFEAT LEDGER; converts the null hypothesis from challenger-only to org-wide |
| V-04 | V-01 + V-02 | Handoff packet + table-primary format; the handoff packet uses the FINDING SURFACE LINKAGE TABLE schema, so LIFECYCLE open findings are directly forwarded as pre-filled rows in DOMAIN's table |
| V-05 | V-01 + V-02 + V-03 | Full integration: handoff packet, table-primary format, per-role inertia verdict; the handoff packet carries both open-findings rows AND the LIFECYCLE inertia verdict as prior context for DOMAIN |

---

## V-01 -- Single Axis: Role Sequence (LIFECYCLE HANDOFF PACKET)

**Variation axis**: Role sequence. After the LIFECYCLE section completes, a LIFECYCLE HANDOFF
PACKET is emitted containing all OPEN/PARTIAL CH-IDs and any HIGH findings. The DOMAIN section
must open with a DOMAIN HANDOFF ACKNOWLEDGMENT that explicitly names each item in the packet
before proceeding to CH-ID response tables.

**Hypothesis**: The current V-05 R3 template guarantees ordering (LIFECYCLE runs first -- C-14)
but does not guarantee that DOMAIN reads or acknowledges lifecycle findings. A DOMAIN reviewer
can produce a complete-looking DOMAIN section that entirely ignores LIFECYCLE gaps. The HANDOFF
PACKET + ACKNOWLEDGMENT pattern makes ignoring lifecycle output a visible template violation:
a blank acknowledgment row is detectable as a structural gap, not a scoring inference. Expected
excellence pattern: E-8 (v5 candidate C-18) -- LIFECYCLE-to-DOMAIN handoff as a structural
primitive; elevates C-14 from ordering to ordering + acknowledged handoff.

---

```
depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any pre-printed
heading, label, field, formula, or structural element. Do not add sections between pre-printed
headers. If a field cannot be filled, write `[N/A -- reason]`.

---

## SCOPE SURFACE REGISTER

*Complete this register before the DISPOSITION_CONTRACT. Name each concrete surface the artifact
exposes for review. Generic descriptions ("all sections", "the full document", "all fields",
"entire spec", "all content") are not acceptable -- they prevent surface-specific finding linkage
and violate the audit trail. Each surface must be nameable as a specific section heading,
interface contract, behavioral claim, schema component, or named protocol.*

| S-ID  | Surface Name                                                                   | Why In Scope                                                   | Primary Lens          |
|-------|--------------------------------------------------------------------------------|----------------------------------------------------------------|-----------------------|
| S-001 | [Specific section, interface, or behavioral claim -- not "all sections"]       | [One sentence: what reviewer question does this surface answer?] | [DOMAIN / LIFECYCLE / either] |
| S-002 | [Another specific surface -- not "all fields" or "the document"]               | [One sentence]                                                 | [DOMAIN / LIFECYCLE / either] |
| S-003 | [Optional -- add rows to be exhaustive; each must name a discrete surface]     | [One sentence]                                                 | [DOMAIN / LIFECYCLE / either] |

*S-IDs (S-001, S-002, ...) carry to §1 IN-SCOPE and to finding citations in every reviewer
section. A finding that cannot cite a registered S-ID is out-of-scope and must not appear in
Additional Findings or the FINDING SURFACE LINKAGE TABLE.*

---

## NULL HYPOTHESIS REGISTER

*Complete before BRACKET OPENING. Name the concrete alternative the team uses today. Generic
phrases ("do nothing", "status quo", "the current approach") are not acceptable -- name the
specific tool, process, or workaround.*

| Field | Value |
|-------|-------|
| What teams use today | [Specific tool, process, or workaround the team relies on instead of building this -- not "do nothing"] |
| Why it works well enough | [One sentence -- the genuine case for continuing with the status quo] |
| Where it breaks down | [One sentence -- the gap or friction that motivates this artifact] |
| Switching cost | [HIGH / MEDIUM / LOW] |
| Null hypothesis strength | [HIGH / MEDIUM / LOW -- how viable is the current approach overall?] |

*This register is the source of truth for all null hypothesis fields in this review.*

---

======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§6;
reviewer sections may not execute until §1 COMPLETE marker is reached]
======================================================================

§1 -- SCOPE ENUMERATION
[Fill this section before proceeding. Copy from SCOPE SURFACE REGISTER above by S-ID and name.
Do not add surfaces not in the register. Do not substitute generic descriptions for S-ID values.]

IN-SCOPE -- surfaces this review will evaluate (from SCOPE SURFACE REGISTER -- copy S-ID and name
exactly; do not add unlisted surfaces; do not substitute "all sections" or similar generic text):
  1. [S-001: copy name from register]
  2. [S-002: copy name from register]
  3. [S-003: copy if active]
  (Total row count must equal non-empty rows in SCOPE SURFACE REGISTER.)

OUT-OF-SCOPE -- surfaces this review will not evaluate:
  1. [SURFACE -- REASON_EXCLUDED]
  (Write "None" if nothing is excluded.)

Scope Amendment Protocol:
  SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]
  Silent scope expansion violates this contract.

§1 COMPLETE -- role selection and reviewer gates proceed below.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH   = Blocks commitment. No commitment proceeds with open HIGH findings.
  MEDIUM = Conditions commitment. Proceeds only after named resolution.
  LOW    = Advisory. Commitment may proceed.
  These definitions apply universally. They may not be restated at any gate.

§2a -- SEVERITY AUDIT CHAIN [IMMUTABLE]
  Each finding in any FINDING SURFACE LINKAGE TABLE carries a Severity tag:
    CRITICAL = maps to gate HIGH. Blocks commitment. Must be resolved before any downstream gate.
    MAJOR    = maps to gate MEDIUM. Conditions commitment. Named resolution path required.
    MINOR    = maps to gate LOW. Advisory. Commitment may proceed.
    ADVISORY = no gate impact. Informational, inertia-context, or style.
  Section Severity = worst(Severity tags) over all rows in the section's FINDING SURFACE LINKAGE TABLE.
  Gate Severity = worst(Section Severities) over LIFECYCLE and DOMAIN.
  Gate verdict derivation (formula-mechanical -- no editorial override):
    CRITICAL in any section -> Gate = FAIL
    MAJOR in any section (no CRITICAL) -> Gate = CONDITIONAL
    MINOR or ADVISORY only -> Gate = PASS
    No findings -> Gate = PASS
  This chain is as binding as §3. A PASS verdict that contradicts this formula is a contract violation.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE -- evaluated at DISPOSITION section]
  G = {GOpen, G_domain_agg, G_lifecycle, GClose}
  BLOCKED      <-- GClose = FAIL  [override: null hypothesis holds]
                OR  exists Gi = FAIL
  CONDITIONAL  <-- no Gi = FAIL  AND  exists Gi = CONDITIONAL
  READY        <-- all Gi = PASS

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"
  A missing cite is an audit-trail gap.

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim in BRACKET OPENING receives a CH-ID (CH-001, CH-002, ...).
  CH-ID COUNT: N = the number of CH-IDs declared in BRACKET OPENING. Record N
    in the "CH-ID Count declared" field immediately after the Challenge Claims table.
  Every downstream CH-ID table must contain exactly N rows -- one row per declared CH-ID.
    A table with fewer than N rows is a §5 count violation regardless of other completeness.
    A table with more than N rows invents claims not in evidence -- also a §5 violation.
  A PASS verdict is prohibited if any CH-ID row shows OPEN status.

§6 -- HANDOFF PROTOCOL [IMMUTABLE]
  After LIFECYCLE completes, the LIFECYCLE HANDOFF PACKET is emitted.
  The DOMAIN section must open with DOMAIN HANDOFF ACKNOWLEDGMENT before any other field.
  A DOMAIN section that lacks the HANDOFF ACKNOWLEDGMENT or leaves any packet row blank
  is a §6 protocol violation -- equivalent to a §4 contract cite gap.
  The HANDOFF PACKET carries: (a) all CH-IDs with PARTIAL or OPEN lifecycle status, and
  (b) all CRITICAL and MAJOR findings from the LIFECYCLE FINDING SURFACE LINKAGE TABLE.
  The DOMAIN ACKNOWLEDGMENT must name each item and state: CARRY-FORWARD (domain will
  address), DOMAIN-N/A (outside domain scope -- reason required), or ESCALATE (elevates severity).

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================

---

## ROLE MANIFEST

Read `.craft/roles/signal/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close -- fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |

*Execution order: BRACKET OPENING -> LIFECYCLE -> LIFECYCLE HANDOFF PACKET -> DOMAIN HANDOFF ACKNOWLEDGMENT -> DOMAIN -> BRACKET CLOSING.*
*LIFECYCLE runs first to surface commitment-readiness blockers before technical depth (§6 protocol).*
*(For `--depth deep`: add DOMAIN-2, DOMAIN-3, etc. Each DOMAIN section receives the same HANDOFF PACKET.
CHALLENGER positions remain fixed. State total count.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis** *(from NULL HYPOTHESIS REGISTER -- name the specific tool or process)*:
[The team continues to use [TOOL/PROCESS from Register] because [WHY IT WORKS from Register].
One sentence. Do not substitute generic language.]

**Null hypothesis strength**: [Copy from NULL HYPOTHESIS REGISTER -- HIGH / MEDIUM / LOW]

**Challenge claims** *(assign CH-IDs; carry to every downstream section per contract §5)*:

| CH-ID  | Challenge Claim                                                                           | Severity              |
|--------|-------------------------------------------------------------------------------------------|-----------------------|
| CH-001 | [CLAIM_1 -- switching cost, workaround viability, or adoption friction. One sentence.]    | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2]                                                                                 | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional]                                                                     | [HIGH / MEDIUM / LOW] |

**CH-ID Count declared**: N = [fill -- count the rows above. Every downstream CH-ID table
  must contain exactly N rows per contract §5.]

**Verify Question**: [One from challenger's `lens.verify`.]

**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]

*GOpen and all N CH-IDs above carry forward. Execution continues: LIFECYCLE -> LIFECYCLE HANDOFF PACKET -> DOMAIN HANDOFF ACKNOWLEDGMENT -> DOMAIN -> BRACKET CLOSING.*

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [PASS / CONDITIONAL / FAIL -- copy from BRACKET OPENING]
*(DOMAIN has not yet run. LIFECYCLE assesses commitment readiness from GOpen alone.)*

**CH-ID Verdict Preview** *(fill the Status column now -- before writing the full response table)*:

| CH-ID  | Status                         |
|--------|--------------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN]   |
| CH-002 | [ADDRESSED / PARTIAL / OPEN]   |
| CH-003 | [ADDRESSED / PARTIAL / OPEN -- omit if not active] |

**CH-ID Response Table** *(exactly N rows -- N from BRACKET OPENING "CH-ID Count declared" --
a row count other than N is a §5 contract violation)*:

| CH-ID  | Challenge Claim (copy) | This Role's Commitment-Frame Response | Status                       |
|--------|------------------------|---------------------------------------|------------------------------|
| CH-001 | [copy]                 | [RESPONSE_1]                          | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]                 | [RESPONSE_2]                          | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active]       | [RESPONSE_3]                          | [ADDRESSED / PARTIAL / OPEN] |

**FINDING SURFACE LINKAGE TABLE** *(one row per finding; cite S-ID from SCOPE SURFACE REGISTER;
a blank In-Scope Surface or Role Lens cell is a structural violation -- finding is not counted)*:

| Finding | In-Scope Surface (S-ID) | Role Lens | Severity |
|---------|------------------------|-----------|----------|
| [FINDING_1 -- commitment/program concern] | [S-00X] | [lens.verify or lens.simplify from this role] | [CRITICAL / MAJOR / MINOR / ADVISORY] |
| [FINDING_2] | [S-00X] | [lens] | [severity] |

**Section Severity**: [worst(Severity column) per §2a -- CRITICAL / MAJOR / MINOR / ADVISORY]

**Decision-readiness assessment**: [Is evidence sufficient to proceed to technical review?
One paragraph referencing GOpen explicitly. Note: G_domain is not yet available -- assess
commitment readiness from challenger framing alone.]

**Null hypothesis status** *(reference NULL HYPOTHESIS REGISTER)*:
Given GOpen, the null hypothesis -- [restate: specific tool/process from Register] -- is:
[STILL VIABLE / CHALLENGED / OPEN]. Justification: [one sentence.]

**Verify Question**: [One from this role's `lens.verify`.]

**Simplify**: [One from this role's `lens.simplify`.]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL -- derive from Section Severity per §2a]
**G_lifecycle Reason**: [One sentence. If FAIL: execution should pause -- DOMAIN review may
be deferred until this gate is resolved.]

---

## LIFECYCLE HANDOFF PACKET

*Produced by LIFECYCLE; consumed by DOMAIN at section open (§6 protocol). Do not alter
pre-printed column headers. A blank Disposition cell in DOMAIN HANDOFF ACKNOWLEDGMENT is
a §6 violation.*

**Open CH-IDs for DOMAIN** *(rows where Status = PARTIAL or OPEN in the Response Table above)*:

| CH-ID  | Lifecycle Status | Challenge Claim (copy) | Note for Domain |
|--------|-----------------|------------------------|-----------------|
| [CH-00X] | [PARTIAL / OPEN] | [copy] | [One sentence: what domain evidence would address this] |
| (rows for each PARTIAL/OPEN CH-ID; write "None -- all CH-IDs ADDRESSED" if no rows) |

**Escalated Findings for DOMAIN** *(CRITICAL and MAJOR rows from FINDING SURFACE LINKAGE TABLE)*:

| Finding | S-ID | Lifecycle Severity | Escalation Note |
|---------|----|-------------------|-----------------|
| [finding text] | [S-00X] | [CRITICAL / MAJOR] | [What domain lens might address or amplify this] |
| (rows for CRITICAL/MAJOR findings; write "None" if no CRITICAL or MAJOR rows) |

**LIFECYCLE HANDOFF PACKET COMPLETE.** DOMAIN section begins below.

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [PASS / CONDITIONAL / FAIL -- copy from BRACKET OPENING]
Received G_lifecycle: [PASS / CONDITIONAL / FAIL -- copy from LIFECYCLE]

**DOMAIN HANDOFF ACKNOWLEDGMENT** *(§6 protocol -- complete before any CH-ID table; a row with
blank Disposition is a §6 contract violation)*:

| Item | From Packet | Type | Disposition |
|------|-------------|------|-------------|
| [CH-00X or finding text] | [Lifecycle Handoff Packet] | [CH-ID / FINDING] | [CARRY-FORWARD / DOMAIN-N/A (reason) / ESCALATE] |
| (one row per item in the Lifecycle Handoff Packet -- do not omit rows) |

**CH-ID Verdict Preview** *(fill now -- before writing response table; convergence anchor vs LIFECYCLE)*:

| CH-ID  | Status                         |
|--------|--------------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN]   |
| CH-002 | [ADDRESSED / PARTIAL / OPEN]   |
| CH-003 | [ADDRESSED / PARTIAL / OPEN -- omit if not active] |

**CH-ID Response Table** *(exactly N rows per contract §5)*:

| CH-ID  | Challenge Claim (copy)               | This Role's Technical Response | Status                       |
|--------|--------------------------------------|-------------------------------|------------------------------|
| CH-001 | [copy full claim from BRACKET OPENING] | [RESPONSE_1]                | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]                               | [RESPONSE_2]                  | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active]                     | [RESPONSE_3]                  | [ADDRESSED / PARTIAL / OPEN] |

*(PARTIAL requires a named resolution path. OPEN = claim not addressable from this role's frame.)*

**FINDING SURFACE LINKAGE TABLE** *(one row per finding; cite S-ID from SCOPE SURFACE REGISTER;
blank In-Scope Surface or Role Lens = structural violation; finding is not counted)*:

| Finding | In-Scope Surface (S-ID) | Role Lens | Severity |
|---------|------------------------|-----------|----------|
| [FINDING_1 -- technical/architecture concern] | [S-00X] | [lens] | [CRITICAL / MAJOR / MINOR / ADVISORY] |
| [FINDING_2] | [S-00X] | [lens] | [severity] |
| [FINDING_3 -- optional] | [S-00X] | [lens] | [severity] |

**Section Severity**: [worst(Severity column) per §2a]

**Verify Question**: [One from this role's `lens.verify`.]

**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL -- derive from Section Severity per §2a]
**G_domain Reason**: [One sentence. If CONDITIONAL: name condition. If FAIL: name gap.]

*(For `--depth deep`: repeat labeled DOMAIN-2, DOMAIN-3. Each opens with its own HANDOFF ACKNOWLEDGMENT.
G_domain Aggregate = worst verdict among all DOMAIN rows. State aggregate explicitly.)*

**G_domain Aggregate**: [PASS / CONDITIONAL / FAIL]

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
*Full record received: scope declaration, all CH-ID tables, all gate verdicts.*

**CH-ID Cross-Gate Tally** *(copy from LIFECYCLE and DOMAIN Verdict Preview tables --
scan for convergence: same non-ADDRESSED status in both columns = high-confidence signal)*:

| CH-ID  | LIFECYCLE Status              | DOMAIN Status                | Converged? |
|--------|-------------------------------|------------------------------|------------|
| CH-001 | [copy from LIFECYCLE preview] | [copy from DOMAIN preview]   | [yes / no] |
| CH-002 | [copy]                        | [copy]                       | [yes / no] |
| CH-003 | [copy if active]              | [copy if active]             | [yes / no] |

**CH-ID Final Assessment** *(exactly N rows per contract §5)*:

| CH-ID  | G_lifecycle Status    | G_domain Status      | Final Status                 | Notes              |
|--------|-----------------------|----------------------|------------------------------|--------------------|
| CH-001 | [copy from LIFECYCLE] | [copy from DOMAIN]   | [DEFEATED / PARTIAL / HOLDS] | [ONE_SENTENCE_NOTE]|
| CH-002 | [copy]                | [copy]               | [DEFEATED / PARTIAL / HOLDS] | [note]             |
| CH-003 | [copy if active]      | [copy]               | [DEFEATED / PARTIAL / HOLDS] | [note]             |

**Remaining gaps**: [What was not fully addressed. If none: "None -- all CH-IDs DEFEATED."]

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
- PASS (= DEFEATED): All CH-IDs DEFEATED -- accumulated record defeats the null hypothesis.
- CONDITIONAL (= PARTIAL): Some CH-IDs PARTIAL -- material gaps remain; name them.
- FAIL (= HOLDS): At least one CH-ID HOLDS -- null hypothesis survives.

**GClose override authority**: GClose = FAIL overrides all prior gate verdicts per §3.

**GClose Rationale**: [2-3 sentences. Reference the specific tool/process from NULL HYPOTHESIS
REGISTER when stating whether it has been defeated.]

---

## GATE VECTOR TABLE

| Gate                         | Reviewer          | Verdict                     | Contract Cite           |
|------------------------------|-------------------|-----------------------------|-------------------------|
| GOpen -- bracket opening     | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_lifecycle -- lifecycle     | [LIFECYCLE_ROLE]  | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_domain -- domain aggregate | [DOMAIN_ROLE(S)]  | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| GClose -- bracket closing    | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Convergence** *(scan CH-ID Cross-Gate Tally -- rows where Converged = yes are highest-confidence
signals; name by CH-ID. "None detected" if no converged rows.)*:

**Conflicts**: [Two reviewers with incompatible CH-ID responses or findings -- name roles and
tension. "None detected" if none.]

**Scope coverage** *(scan SCOPE SURFACE REGISTER S-IDs against findings in all reviewer sections --
any S-ID not cited by any finding is a coverage gap)*:
[S-00X: [name] -- no reviewer cited this surface. OR "None -- all registered surfaces cited."]

**§6 protocol status**: [Were all HANDOFF PACKET items acknowledged in the DOMAIN section?
List any §6 violations here if present. "None -- all handoff items acknowledged." if clean.]

---

## DISPOSITION

**Gate vector** *(fill from GATE VECTOR TABLE)*:
- GOpen = [copy]
- G_domain_agg = [copy]
- G_lifecycle = [copy]
- GClose = [copy]

**Apply contract §3 formula** *(do not alter; evaluate gate vector against pre-stated formula)*:

```
G = {GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]}
GClose = FAIL? --> BLOCKED  (challenger override: null hypothesis holds)
Any other Gi = FAIL? --> BLOCKED
No FAIL, any CONDITIONAL? --> CONDITIONAL
All PASS? --> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**Null hypothesis defeat** *(from GClose and NULL HYPOTHESIS REGISTER)*:
[DEFEATED / PARTIALLY DEFEATED / HOLDS -- one sentence citing the specific tool/process.]

**Primary driver**: [The gate verdict most responsible for this disposition -- one sentence.]

**Conditions** *(CONDITIONAL only)*:
1. [Condition from first CONDITIONAL gate.]

**Blocker** *(BLOCKED only)*: [Specific finding from the FAIL gate.]

---

## ACTION ITEM REGISTER

*One row per PARTIAL or HOLDS CH-ID from BRACKET CLOSING.*

| CH-ID  | Item Description   | Disposition Class                    | Owner Role  | Resolution Criterion                                    |
|--------|--------------------|--------------------------------------|-------------|---------------------------------------------------------|
| CH-001 | [What must be done] | [BLOCKED / CONDITIONAL / ADVISORY] | [ROLE_NAME] | [One sentence: what must be true to close this item]    |

---

## SCORING

```
Composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 9 * 45)
```

Golden threshold: all 5 essential criteria pass AND composite >= 80.
```

---

## V-02 -- Single Axis: Output Format (Table-Primary Mode)

**Variation axis**: Output format. In each reviewer section the FINDING SURFACE LINKAGE TABLE
is the primary and complete finding record. Prose findings are not permitted as a separate list.
CRITICAL and MAJOR rows may have a Detail subsection attached, but no finding may appear
outside the table. A FINDING TALLY row at the table foot counts by severity for §2a audit
verification.

**Hypothesis**: V-05 R3 has the FINDING SURFACE LINKAGE TABLE structurally present (C-16 PASS)
but reviewers may still produce "Additional Findings" prose lists alongside the table, diluting
the template-determined nature of C-16. Making the table the exclusive finding record with an
explicit prohibition on prose findings forces every finding into the table schema. The FINDING
TALLY row makes §2a Section Severity derivation a count operation rather than an inference.
Expected excellence pattern: E-9 (v5 candidate C-18) -- table-primacy rule + finding tally row
as a structural pair; together they make the §2a audit chain fully mechanical end-to-end.

---

```
depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any pre-printed
heading, label, field, formula, or structural element. Do not add sections between pre-printed
headers. If a field cannot be filled, write `[N/A -- reason]`.

**Table-primary rule**: Findings must appear ONLY in FINDING SURFACE LINKAGE TABLEs. No prose
finding lists ("Additional Findings" bullet lists) are permitted. A finding not in a table is
invisible to the §2a audit chain and does not count toward severity. CRITICAL and MAJOR rows
may have a Detail subsection (format: "Detail [CH-ID or S-ID]: [prose]") attached after the
table, but the table row must exist first.

---

## SCOPE SURFACE REGISTER

*Complete this register before the DISPOSITION_CONTRACT. Name each concrete surface. Generic
descriptions ("all sections", "the full document") are not acceptable.*

| S-ID  | Surface Name                                                                   | Why In Scope                                                   | Primary Lens          |
|-------|--------------------------------------------------------------------------------|----------------------------------------------------------------|-----------------------|
| S-001 | [Specific section, interface, or behavioral claim -- not "all sections"]       | [One sentence]                                                 | [DOMAIN / LIFECYCLE / either] |
| S-002 | [Another specific surface]                                                     | [One sentence]                                                 | [DOMAIN / LIFECYCLE / either] |
| S-003 | [Optional]                                                                     | [One sentence]                                                 | [DOMAIN / LIFECYCLE / either] |

*A finding that cannot cite a registered S-ID is out-of-scope and must not appear in any table.*

---

## NULL HYPOTHESIS REGISTER

*Complete before BRACKET OPENING. Name the concrete alternative in use today. Generic phrases
are not acceptable.*

| Field | Value |
|-------|-------|
| What teams use today | [Specific tool, process, or workaround -- not "do nothing"] |
| Why it works well enough | [One sentence] |
| Where it breaks down | [One sentence] |
| Switching cost | [HIGH / MEDIUM / LOW] |
| Null hypothesis strength | [HIGH / MEDIUM / LOW] |

---

======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK -- complete §1 before proceeding; do not alter §2-§5]
======================================================================

§1 -- SCOPE ENUMERATION
[Copy from SCOPE SURFACE REGISTER by S-ID and name. Do not use generic text.]

IN-SCOPE (copy S-ID and name from register; total rows must equal register rows):
  1. [S-001: copy name]
  2. [S-002: copy name]
  3. [S-003: copy if active]

OUT-OF-SCOPE:
  1. [SURFACE -- REASON]

§1 COMPLETE.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH   = Blocks commitment. MEDIUM = Conditions commitment. LOW = Advisory.

§2a -- SEVERITY AUDIT CHAIN [IMMUTABLE]
  Finding-level severity tags: CRITICAL / MAJOR / MINOR / ADVISORY.
    CRITICAL -> gate HIGH (FAIL).   MAJOR -> gate MEDIUM (CONDITIONAL).
    MINOR / ADVISORY -> gate LOW (PASS).
  Section Severity = worst(Severity column) in that section's FINDING SURFACE LINKAGE TABLE.
    Verify using the FINDING TALLY row at table foot: max-severity tag determines Section Severity.
  Gate verdict from Section Severity (formula-mechanical):
    CRITICAL in section -> Gate = FAIL
    MAJOR in section (no CRITICAL) -> Gate = CONDITIONAL
    MINOR / ADVISORY / empty -> Gate = PASS

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  G = {GOpen, G_domain_agg, G_lifecycle, GClose}
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND any CONDITIONAL
  READY <-- all PASS

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each CH-ID in BRACKET OPENING must appear in exactly N rows downstream (N = CH-ID Count declared).
  Count violation = §5 breach. PASS prohibited if any row = OPEN.

§5a -- TABLE-PRIMACY RULE [IMMUTABLE]
  Findings exist only in FINDING SURFACE LINKAGE TABLEs. Prose finding lists violate the
  audit trail. CRITICAL/MAJOR rows may have an attached Detail subsection; all other findings
  are complete within the table row. Severity is derived exclusively from the table Severity
  column; prose mentions of severity are not counted.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================

---

## ROLE MANIFEST

Read `.craft/roles/signal/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |

*Execution order: BRACKET OPENING -> LIFECYCLE -> DOMAIN -> BRACKET CLOSING.*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis** *(from NULL HYPOTHESIS REGISTER -- name the specific tool or process)*:
[The team continues to use [TOOL/PROCESS] because [WHY IT WORKS]. One sentence.]

**Null hypothesis strength**: [Copy from NULL HYPOTHESIS REGISTER]

**Challenge claims**:

| CH-ID  | Challenge Claim                                                                        | Severity              |
|--------|----------------------------------------------------------------------------------------|-----------------------|
| CH-001 | [CLAIM_1]                                                                              | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2]                                                                              | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional]                                                                  | [HIGH / MEDIUM / LOW] |

**CH-ID Count declared**: N = [count rows above]

**Verify Question**: [One from challenger's `lens.verify`.]
**Simplify**: [One from challenger's `lens.simplify`.]
**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]

**CH-ID Verdict Preview**:

| CH-ID  | Status                       |
|--------|------------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [omit if inactive]           |

**CH-ID Response Table** *(exactly N rows)*:

| CH-ID  | Challenge Claim (copy) | Commitment-Frame Response | Status                       |
|--------|------------------------|---------------------------|------------------------------|
| CH-001 | [copy]                 | [RESPONSE]                | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]                 | [RESPONSE]                | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active]       | [RESPONSE]                | [ADDRESSED / PARTIAL / OPEN] |

**FINDING SURFACE LINKAGE TABLE** *(all findings appear here and only here per §5a; no prose list)*:

| # | Finding | In-Scope Surface (S-ID) | Role Lens | Severity |
|---|---------|------------------------|-----------|----------|
| 1 | [Commitment/program concern -- one sentence] | [S-00X] | [lens.verify or lens.simplify from this role] | [CRITICAL / MAJOR / MINOR / ADVISORY] |
| 2 | [Finding] | [S-00X] | [lens] | [severity] |
| **TALLY** | **CRITICAL: [n] / MAJOR: [n] / MINOR: [n] / ADVISORY: [n]** | | | |

*Section Severity = worst tag in Severity column = [CRITICAL / MAJOR / MINOR / ADVISORY] per §2a.*

*(If a finding row has CRITICAL or MAJOR severity, attach a Detail subsection here:)*
*Detail [S-00X]: [Prose elaboration for CRITICAL or MAJOR rows only.]*

**Decision-readiness assessment**: [One paragraph referencing GOpen. G_domain not yet available.]

**Null hypothesis status** *(reference NULL HYPOTHESIS REGISTER)*:
Given GOpen, [specific tool/process from Register] is: [STILL VIABLE / CHALLENGED / OPEN].

**Verify Question**: [One from this role's `lens.verify`.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL -- derived from Section Severity per §2a]
**G_lifecycle Reason**: [One sentence.]

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]
Received G_lifecycle: [copy]

**CH-ID Verdict Preview**:

| CH-ID  | Status                       |
|--------|------------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [omit if inactive]           |

**CH-ID Response Table** *(exactly N rows per §5)*:

| CH-ID  | Challenge Claim (copy)           | Technical Response | Status                       |
|--------|----------------------------------|--------------------|------------------------------|
| CH-001 | [copy from BRACKET OPENING]      | [RESPONSE]         | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]                           | [RESPONSE]         | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active]                 | [RESPONSE]         | [ADDRESSED / PARTIAL / OPEN] |

**FINDING SURFACE LINKAGE TABLE** *(all findings here and only here per §5a)*:

| # | Finding | In-Scope Surface (S-ID) | Role Lens | Severity |
|---|---------|------------------------|-----------|----------|
| 1 | [Technical/architecture concern] | [S-00X] | [lens] | [CRITICAL / MAJOR / MINOR / ADVISORY] |
| 2 | [Finding] | [S-00X] | [lens] | [severity] |
| 3 | [optional] | [S-00X] | [lens] | [severity] |
| **TALLY** | **CRITICAL: [n] / MAJOR: [n] / MINOR: [n] / ADVISORY: [n]** | | | |

*Section Severity = worst tag in Severity column = [CRITICAL / MAJOR / MINOR / ADVISORY] per §2a.*

*(Attach Detail subsections for CRITICAL or MAJOR rows only.)*

**Verify Question**: [One from this role's `lens.verify`.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL -- derived from Section Severity per §2a]
**G_domain Reason**: [One sentence.]

**G_domain Aggregate**: [PASS / CONDITIONAL / FAIL]

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**CH-ID Cross-Gate Tally**:

| CH-ID  | LIFECYCLE Status              | DOMAIN Status              | Converged? |
|--------|-------------------------------|----------------------------|------------|
| CH-001 | [copy from LIFECYCLE preview] | [copy from DOMAIN preview] | [yes / no] |
| CH-002 | [copy]                        | [copy]                     | [yes / no] |
| CH-003 | [copy if active]              | [copy if active]           | [yes / no] |

**CH-ID Final Assessment** *(exactly N rows)*:

| CH-ID  | G_lifecycle | G_domain | Final Status                 | Notes |
|--------|-------------|----------|------------------------------|-------|
| CH-001 | [copy]      | [copy]   | [DEFEATED / PARTIAL / HOLDS] | [note]|
| CH-002 | [copy]      | [copy]   | [DEFEATED / PARTIAL / HOLDS] | [note]|
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note]|

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**GClose Rationale**: [2-3 sentences citing specific tool/process from NULL HYPOTHESIS REGISTER.]

---

## GATE VECTOR TABLE

| Gate                         | Reviewer          | Verdict                     | Contract Cite           |
|------------------------------|-------------------|-----------------------------|-------------------------|
| GOpen                        | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_lifecycle                  | [LIFECYCLE_ROLE]  | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_domain aggregate           | [DOMAIN_ROLE(S)]  | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| GClose                       | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Convergence** *(CH-ID Cross-Gate Tally converged rows)*:

**Conflicts** *(incompatible responses or findings across roles)*:

**Scope coverage** *(S-IDs not cited in any finding table)*:
[S-00X: [name] -- uncited. OR "None -- all registered surfaces cited."]

**Finding tally cross-check** *(LIFECYCLE TALLY + DOMAIN TALLY; flag if totals don't match
table rows; inconsistency = §5a audit trail gap)*:
[LIFECYCLE: CRITICAL=[n] MAJOR=[n] | DOMAIN: CRITICAL=[n] MAJOR=[n] | Gate-driving severity: [worst]]

---

## DISPOSITION

**Gate vector**:
- GOpen = [copy]
- G_domain_agg = [copy]
- G_lifecycle = [copy]
- GClose = [copy]

**Apply contract §3 formula**:

```
G = {GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]}
GClose = FAIL? --> BLOCKED
Any Gi = FAIL? --> BLOCKED
No FAIL, any CONDITIONAL? --> CONDITIONAL
All PASS? --> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**Null hypothesis defeat**: [DEFEATED / PARTIALLY DEFEATED / HOLDS -- one sentence.]

**Primary driver**: [One sentence.]

**Conditions** *(CONDITIONAL only)*: [condition(s)]

**Blocker** *(BLOCKED only)*: [specific finding]

---

## ACTION ITEM REGISTER

| CH-ID  | Item Description    | Disposition Class                    | Owner Role  | Resolution Criterion                                 |
|--------|---------------------|--------------------------------------|-------------|------------------------------------------------------|
| CH-001 | [What must be done] | [BLOCKED / CONDITIONAL / ADVISORY]   | [ROLE_NAME] | [One sentence: what closes this item]                |

---

## SCORING

```
Composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 9 * 45)
```
```

---

## V-03 -- Single Axis: Inertia Framing (Per-Role Inertia Verdict)

**Variation axis**: Inertia framing. The status-quo competitor from the NULL HYPOTHESIS REGISTER
is not limited to the BRACKET OPENING challenger. Every reviewer section includes a mandatory
PER-ROLE INERTIA ASSESSMENT: given this role's lens, does the status-quo alternative still
satisfy the need? Each role produces an INERTIA VERDICT (SURVIVES / WEAKENED / DEFEATED) and
a one-sentence justification. After BRACKET CLOSING, a INERTIA DEFEAT LEDGER aggregates
all per-role verdicts into a final null-hypothesis defeat state.

**Hypothesis**: Currently the null hypothesis is evaluated only by the challenger. A domain
expert or lifecycle PM may see aspects of the status-quo that the challenger's inertia-advocate
lens misses or overstates. Distributing the inertia assessment to every role creates a
multi-perspective null hypothesis defeat record. The INERTIA DEFEAT LEDGER makes the final
defeat state a table scan rather than editorial synthesis. Expected excellence pattern: E-10
(v5 candidate C-19) -- per-role inertia verdict + INERTIA DEFEAT LEDGER; elevates C-09 null
hypothesis assessment from challenger-only to org-wide and makes the defeat state auditable.

---

```
depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any pre-printed
heading, label, field, formula, or structural element. Do not add sections between pre-printed
headers. If a field cannot be filled, write `[N/A -- reason]`.

---

## SCOPE SURFACE REGISTER

*Complete before the DISPOSITION_CONTRACT. Each surface must be concrete and nameable.*

| S-ID  | Surface Name                                                               | Why In Scope                                                   | Primary Lens          |
|-------|----------------------------------------------------------------------------|----------------------------------------------------------------|-----------------------|
| S-001 | [Specific section, interface, or behavioral claim]                         | [One sentence]                                                 | [DOMAIN / LIFECYCLE / either] |
| S-002 | [Another specific surface]                                                 | [One sentence]                                                 | [DOMAIN / LIFECYCLE / either] |
| S-003 | [Optional]                                                                 | [One sentence]                                                 | [DOMAIN / LIFECYCLE / either] |

*Generic surface descriptions ("all sections", "the full document") are not acceptable.*

---

## NULL HYPOTHESIS REGISTER

*Complete before BRACKET OPENING. The null hypothesis tool/process named here is distributed
to every reviewer section for per-role inertia assessment.*

| Field | Value |
|-------|-------|
| What teams use today | [Specific tool, process, or workaround -- not "do nothing"] |
| Why it works well enough | [One sentence] |
| Where it breaks down | [One sentence] |
| Switching cost | [HIGH / MEDIUM / LOW] |
| Null hypothesis strength | [HIGH / MEDIUM / LOW] |

*The tool/process named in "What teams use today" carries to every reviewer section's
PER-ROLE INERTIA ASSESSMENT. Reviewers must evaluate it from their specific lens.*

---

======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK -- do not alter §2-§6; §1 must be completed first]
======================================================================

§1 -- SCOPE ENUMERATION
[Copy from SCOPE SURFACE REGISTER by S-ID and name.]

IN-SCOPE:
  1. [S-001: copy name]
  2. [S-002: copy name]
  3. [S-003: if active]

OUT-OF-SCOPE:
  1. [SURFACE -- REASON]

§1 COMPLETE.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks. MEDIUM = Conditions. LOW = Advisory.

§2a -- SEVERITY AUDIT CHAIN [IMMUTABLE]
  Finding-level: CRITICAL / MAJOR / MINOR / ADVISORY.
    CRITICAL -> HIGH (FAIL). MAJOR -> MEDIUM (CONDITIONAL). MINOR/ADVISORY -> LOW (PASS).
  Section Severity = worst(Severity column) in section's FINDING SURFACE LINKAGE TABLE.
  Gate verdict (formula-mechanical): CRITICAL -> FAIL; MAJOR (no CRITICAL) -> CONDITIONAL;
  MINOR/ADVISORY/empty -> PASS.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  G = {GOpen, G_domain_agg, G_lifecycle, GClose}
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND any CONDITIONAL
  READY <-- all PASS

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  CH-ID Count = N (declared in BRACKET OPENING). Every downstream table = exactly N rows.
  PASS prohibited if any row = OPEN.

§6 -- INERTIA DISTRIBUTION REQUIREMENT [IMMUTABLE]
  Every reviewer section must include a PER-ROLE INERTIA ASSESSMENT evaluating the specific
  tool/process named in the NULL HYPOTHESIS REGISTER from that role's lens. The INERTIA VERDICT
  must be one of: SURVIVES / WEAKENED / DEFEATED. A section that lacks a PER-ROLE INERTIA
  ASSESSMENT is a §6 violation. The INERTIA DEFEAT LEDGER after BRACKET CLOSING aggregates
  all per-role verdicts. Final null hypothesis defeat state = worst(INERTIA VERDICTs):
    All DEFEATED -> DEFEATED; any SURVIVES -> HOLDS; otherwise -> PARTIALLY DEFEATED.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================

---

## ROLE MANIFEST

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |

*Execution order: BRACKET OPENING -> LIFECYCLE -> DOMAIN -> BRACKET CLOSING -> INERTIA DEFEAT LEDGER.*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis** *(from NULL HYPOTHESIS REGISTER)*:
[The team continues to use [TOOL/PROCESS] because [WHY IT WORKS]. One sentence.]

**Null hypothesis strength**: [copy]

**Challenge claims**:

| CH-ID  | Challenge Claim                                                                        | Severity              |
|--------|----------------------------------------------------------------------------------------|-----------------------|
| CH-001 | [CLAIM_1]                                                                              | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2]                                                                              | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional]                                                                  | [HIGH / MEDIUM / LOW] |

**CH-ID Count declared**: N = [count]

**PER-ROLE INERTIA ASSESSMENT -- CHALLENGER** *(§6 requirement)*:
Status-quo evaluated: [tool/process from NULL HYPOTHESIS REGISTER]
Challenger lens: inertia strength, switching cost, viable workaround persistence
INERTIA VERDICT: [SURVIVES / WEAKENED / DEFEATED]
Justification: [One sentence from challenger lens.]

**Verify Question**: [One from `lens.verify`.]
**Simplify**: [One from `lens.simplify`.]
**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]

**PER-ROLE INERTIA ASSESSMENT -- LIFECYCLE** *(§6 requirement)*:
Status-quo evaluated: [copy tool/process name from NULL HYPOTHESIS REGISTER -- do not substitute]
This role's lens: commitment readiness, program timelines, decision process friction
INERTIA VERDICT: [SURVIVES / WEAKENED / DEFEATED]
Justification: [One sentence from this role's commitment-frame lens. Does the status-quo satisfy
  the program's decision needs well enough to avoid commitment?]

**CH-ID Verdict Preview**:

| CH-ID  | Status                       |
|--------|------------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [omit if inactive]           |

**CH-ID Response Table** *(exactly N rows)*:

| CH-ID  | Challenge Claim (copy) | Commitment-Frame Response | Status                       |
|--------|------------------------|---------------------------|------------------------------|
| CH-001 | [copy]                 | [RESPONSE]                | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]                 | [RESPONSE]                | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active]       | [RESPONSE]                | [ADDRESSED / PARTIAL / OPEN] |

**FINDING SURFACE LINKAGE TABLE**:

| Finding | In-Scope Surface (S-ID) | Role Lens | Severity |
|---------|------------------------|-----------|----------|
| [Commitment/program concern] | [S-00X] | [lens] | [CRITICAL / MAJOR / MINOR / ADVISORY] |
| [Finding] | [S-00X] | [lens] | [severity] |

**Section Severity**: [worst(Severity column) per §2a]

**Decision-readiness assessment**: [One paragraph referencing GOpen.]

**Verify Question**: [One from `lens.verify`.]
**Simplify**: [One from `lens.simplify`.]
**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL -- from Section Severity per §2a]
**G_lifecycle Reason**: [One sentence.]

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]
Received G_lifecycle: [copy]

**PER-ROLE INERTIA ASSESSMENT -- DOMAIN** *(§6 requirement)*:
Status-quo evaluated: [copy tool/process name from NULL HYPOTHESIS REGISTER -- do not substitute]
This role's lens: technical feasibility, architecture soundness, implementation cost
INERTIA VERDICT: [SURVIVES / WEAKENED / DEFEATED]
Justification: [One sentence from this role's technical lens. Does the status-quo satisfy the
  technical need well enough that building this is unjustified?]

**CH-ID Verdict Preview**:

| CH-ID  | Status                       |
|--------|------------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [omit if inactive]           |

**CH-ID Response Table** *(exactly N rows per §5)*:

| CH-ID  | Challenge Claim (copy)           | Technical Response | Status                       |
|--------|----------------------------------|--------------------|------------------------------|
| CH-001 | [copy]                           | [RESPONSE]         | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]                           | [RESPONSE]         | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active]                 | [RESPONSE]         | [ADDRESSED / PARTIAL / OPEN] |

**FINDING SURFACE LINKAGE TABLE**:

| Finding | In-Scope Surface (S-ID) | Role Lens | Severity |
|---------|------------------------|-----------|----------|
| [Technical concern] | [S-00X] | [lens] | [CRITICAL / MAJOR / MINOR / ADVISORY] |
| [Finding] | [S-00X] | [lens] | [severity] |
| [optional] | [S-00X] | [lens] | [severity] |

**Section Severity**: [worst(Severity column) per §2a]

**Verify Question**: [One from `lens.verify`.]
**Simplify**: [One from `lens.simplify`.]
**G_domain Verdict**: [PASS / CONDITIONAL / FAIL -- from Section Severity per §2a]
**G_domain Reason**: [One sentence.]
**G_domain Aggregate**: [PASS / CONDITIONAL / FAIL]

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**CH-ID Cross-Gate Tally**:

| CH-ID  | LIFECYCLE Status | DOMAIN Status | Converged? |
|--------|-----------------|---------------|------------|
| CH-001 | [copy]          | [copy]        | [yes / no] |
| CH-002 | [copy]          | [copy]        | [yes / no] |
| CH-003 | [copy if active]| [copy]        | [yes / no] |

**CH-ID Final Assessment** *(exactly N rows)*:

| CH-ID  | G_lifecycle | G_domain | Final Status                 | Notes |
|--------|-------------|----------|------------------------------|-------|
| CH-001 | [copy]      | [copy]   | [DEFEATED / PARTIAL / HOLDS] | [note]|
| CH-002 | [copy]      | [copy]   | [DEFEATED / PARTIAL / HOLDS] | [note]|
| CH-003 | [copy]      | [copy]   | [DEFEATED / PARTIAL / HOLDS] | [note]|

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**GClose Rationale**: [2-3 sentences citing the specific tool/process from NULL HYPOTHESIS REGISTER.]

---

## INERTIA DEFEAT LEDGER

*(Aggregate all PER-ROLE INERTIA ASSESSMENTs from this review per §6)*

| Role | Lens | INERTIA VERDICT | Justification Summary |
|------|------|-----------------|-----------------------|
| CHALLENGER | inertia-advocate | [copy from BRACKET OPENING] | [copy one-sentence justification] |
| LIFECYCLE  | PM/program       | [copy from LIFECYCLE]       | [copy] |
| DOMAIN     | technical        | [copy from DOMAIN]          | [copy] |

**Final null hypothesis defeat state** *(derived per §6 formula -- worst of all INERTIA VERDICTs)*:
All DEFEATED -> DEFEATED | any SURVIVES -> HOLDS | otherwise -> PARTIALLY DEFEATED

**Final null hypothesis defeat state**: [DEFEATED / PARTIALLY DEFEATED / HOLDS]

**Narrative**: [One sentence. Reference the specific tool/process from NULL HYPOTHESIS REGISTER.
Example: "[Tool] HOLDS -- the DOMAIN reviewer finds it technically sufficient; CH-ID defeat is
insufficient without domain-level defeat."]

---

## GATE VECTOR TABLE

| Gate             | Reviewer          | Verdict                     | Contract Cite           |
|------------------|-------------------|-----------------------------|-------------------------|
| GOpen            | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_lifecycle      | [LIFECYCLE_ROLE]  | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_domain agg     | [DOMAIN_ROLE(S)]  | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| GClose           | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Convergence** *(CH-ID Cross-Gate Tally converged rows)*:

**Conflicts** *(incompatible findings or responses)*:

**Scope coverage** *(uncited S-IDs)*:

**Inertia signal** *(cross-role null hypothesis pattern from INERTIA DEFEAT LEDGER)*:
[Roles that diverge on INERTIA VERDICT (e.g., CHALLENGER=DEFEATED, DOMAIN=SURVIVES) are
high-signal conflicts. Name the divergence here.]

---

## DISPOSITION

**Gate vector**:
- GOpen = [copy]
- G_domain_agg = [copy]
- G_lifecycle = [copy]
- GClose = [copy]

**Apply contract §3**:

```
G = {GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]}
GClose=FAIL? --> BLOCKED  Any Gi=FAIL? --> BLOCKED
No FAIL, any CONDITIONAL? --> CONDITIONAL  All PASS? --> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**Null hypothesis defeat** *(from INERTIA DEFEAT LEDGER final state and GClose)*:
[DEFEATED / PARTIALLY DEFEATED / HOLDS -- one sentence citing specific tool/process.]

**Primary driver**: [One sentence.]

---

## ACTION ITEM REGISTER

| CH-ID  | Item                | Disposition Class | Owner       | Resolution Criterion |
|--------|---------------------|-------------------|-------------|----------------------|
| CH-001 | [what must be done] | [BLOCKED/COND/ADV]| [ROLE_NAME] | [what closes it]     |

---

## SCORING

```
Composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 9 * 45)
```
```

---

## V-04 -- Combined: Role Sequence + Output Format

**Variation axis**: V-01 (LIFECYCLE HANDOFF PACKET) + V-02 (table-primary mode).

**Hypothesis**: The handoff packet in V-01 lists LIFECYCLE open findings as prose items.
When combined with V-02's table-primary format, the HANDOFF PACKET uses the FINDING SURFACE
LINKAGE TABLE schema directly: LIFECYCLE's CRITICAL/MAJOR rows are forwarded as pre-filled table
rows in the DOMAIN HANDOFF ACKNOWLEDGMENT section. DOMAIN either inherits each row
(CARRY-FORWARD) or disputes it (DOMAIN-N/A / ESCALATE). The combination creates a
single-schema finding chain from LIFECYCLE table -> HANDOFF PACKET -> DOMAIN acknowledgment
table -> DOMAIN table. Expected excellence pattern: E-11 (v5 candidate C-20) -- cross-reviewer
finding schema continuity; the same table schema (Finding / S-ID / Role Lens / Severity)
carrying from LIFECYCLE to DOMAIN via the HANDOFF PACKET makes finding lineage traceable
without schema translation.

---

```
depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any pre-printed
heading, label, field, formula, or structural element. Do not add sections between pre-printed
headers. If a field cannot be filled, write `[N/A -- reason]`.

**Table-primary rule**: All findings appear in FINDING SURFACE LINKAGE TABLEs only. Prose finding
lists are prohibited. CRITICAL/MAJOR rows may have an attached Detail subsection. Severity derives
exclusively from the table Severity column.

---

## SCOPE SURFACE REGISTER

| S-ID  | Surface Name                                                             | Why In Scope   | Primary Lens          |
|-------|--------------------------------------------------------------------------|----------------|-----------------------|
| S-001 | [Specific surface -- not "all sections"]                                 | [One sentence] | [DOMAIN / LIFECYCLE / either] |
| S-002 | [Specific surface]                                                       | [One sentence] | [DOMAIN / LIFECYCLE / either] |
| S-003 | [Optional]                                                               | [One sentence] | [DOMAIN / LIFECYCLE / either] |

---

## NULL HYPOTHESIS REGISTER

| Field | Value |
|-------|-------|
| What teams use today | [Specific tool/process -- not "do nothing"] |
| Why it works well enough | [One sentence] |
| Where it breaks down | [One sentence] |
| Switching cost | [HIGH / MEDIUM / LOW] |
| Null hypothesis strength | [HIGH / MEDIUM / LOW] |

---

======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE (copy from SCOPE SURFACE REGISTER by S-ID):
  1. [S-001: name]  2. [S-002: name]  3. [S-003: if active]
OUT-OF-SCOPE: [surface -- reason]
§1 COMPLETE.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks. MEDIUM = Conditions. LOW = Advisory.

§2a -- SEVERITY AUDIT CHAIN [IMMUTABLE]
  CRITICAL -> FAIL. MAJOR -> CONDITIONAL. MINOR/ADVISORY -> PASS.
  Section Severity = worst(Severity column). Gate from Section Severity (formula-mechanical).

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND any CONDITIONAL
  READY <-- all PASS

§4 -- CONTRACT CITE [IMMUTABLE]
  Each section opens with: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING [IMMUTABLE]
  N = CH-ID Count declared. Every downstream table = exactly N rows. PASS prohibited if OPEN row.

§5a -- TABLE-PRIMACY RULE [IMMUTABLE]
  Findings exist only in FINDING SURFACE LINKAGE TABLEs. Severity from table only.

§6 -- HANDOFF PROTOCOL [IMMUTABLE]
  After LIFECYCLE, a LIFECYCLE HANDOFF PACKET is emitted carrying CRITICAL/MAJOR rows
  from the LIFECYCLE FINDING SURFACE LINKAGE TABLE using the same schema.
  DOMAIN opens with DOMAIN HANDOFF ACKNOWLEDGMENT before any other field.
  Each packet row must appear in the ACKNOWLEDGMENT with Disposition:
    CARRY-FORWARD (domain inherits finding), DOMAIN-N/A (reason required), ESCALATE (severity raised).
  A blank Disposition cell = §6 violation.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================

---

## ROLE MANIFEST

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |

*Order: BRACKET OPENING -> LIFECYCLE -> LIFECYCLE HANDOFF PACKET -> DOMAIN -> BRACKET CLOSING.*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis** *(from NULL HYPOTHESIS REGISTER)*: [specific tool/process because why it works. One sentence.]
**Null hypothesis strength**: [copy]

**Challenge claims**:

| CH-ID  | Claim                 | Severity              |
|--------|-----------------------|-----------------------|
| CH-001 | [CLAIM_1]             | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2]             | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional] | [HIGH / MEDIUM / LOW] |

**CH-ID Count declared**: N = [count]
**Verify Question**: [One from `lens.verify`.]
**Simplify**: [One from `lens.simplify`.]
**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]

**CH-ID Verdict Preview**:

| CH-ID  | Status                       |
|--------|------------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [omit if inactive]           |

**CH-ID Response Table** *(exactly N rows)*:

| CH-ID  | Claim (copy) | Commitment Response | Status                       |
|--------|--------------|---------------------|------------------------------|
| CH-001 | [copy]       | [RESPONSE]          | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]       | [RESPONSE]          | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE]      | [ADDRESSED / PARTIAL / OPEN] |

**FINDING SURFACE LINKAGE TABLE** *(per §5a: all findings here only; TALLY row at foot)*:

| # | Finding | In-Scope Surface (S-ID) | Role Lens | Severity |
|---|---------|------------------------|-----------|----------|
| 1 | [Commitment concern] | [S-00X] | [lens] | [CRITICAL / MAJOR / MINOR / ADVISORY] |
| 2 | [Finding] | [S-00X] | [lens] | [severity] |
| **TALLY** | **CRITICAL: [n] / MAJOR: [n] / MINOR: [n] / ADVISORY: [n]** | | | |

*Section Severity = [worst tag] per §2a.*

**Decision-readiness**: [One paragraph referencing GOpen.]
**Null hypothesis status**: [STILL VIABLE / CHALLENGED / OPEN] -- [one sentence.]
**Verify Question**: [One.] **Simplify**: [One.]
**G_lifecycle**: [PASS / CONDITIONAL / FAIL] -- [one sentence reason.]

---

## LIFECYCLE HANDOFF PACKET

*(§6 protocol. Carries CRITICAL/MAJOR rows from LIFECYCLE table in the same schema.
DOMAIN opens with DOMAIN HANDOFF ACKNOWLEDGMENT referencing each row below.)*

**CRITICAL/MAJOR findings forwarded** *(copy rows with Severity = CRITICAL or MAJOR from
LIFECYCLE FINDING SURFACE LINKAGE TABLE; write "None" if no CRITICAL or MAJOR rows)*:

| # | Finding (copy) | In-Scope Surface (S-ID) | Lifecycle Role Lens | Severity |
|---|---------------|------------------------|---------------------|----------|
| [row from lifecycle table] | [copy finding] | [copy S-ID] | [copy lens] | [CRITICAL / MAJOR] |

**Open CH-IDs forwarded** *(PARTIAL/OPEN from lifecycle CH-ID Response Table)*:

| CH-ID | Lifecycle Status | Note for Domain |
|-------|-----------------|-----------------|
| [CH-00X] | [PARTIAL / OPEN] | [One sentence: domain evidence that would address this] |
| (write "None" if all ADDRESSED) |

**HANDOFF PACKET COMPLETE.** Domain section begins below.

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]
Received G_lifecycle: [copy]

**DOMAIN HANDOFF ACKNOWLEDGMENT** *(§6 protocol -- one row per handoff packet item;
blank Disposition = §6 violation)*:

| # | Item (from Handoff Packet) | Type | Domain Disposition |
|---|---------------------------|------|--------------------|
| [row number] | [finding or CH-ID from packet] | [FINDING / CH-ID] | [CARRY-FORWARD / DOMAIN-N/A: reason / ESCALATE] |

**CH-ID Verdict Preview**:

| CH-ID  | Status                       |
|--------|------------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [omit if inactive]           |

**CH-ID Response Table** *(exactly N rows per §5)*:

| CH-ID  | Claim (copy)          | Technical Response | Status                       |
|--------|-----------------------|--------------------|------------------------------|
| CH-001 | [copy]                | [RESPONSE]         | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]                | [RESPONSE]         | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active]      | [RESPONSE]         | [ADDRESSED / PARTIAL / OPEN] |

**FINDING SURFACE LINKAGE TABLE** *(per §5a: all findings here only; TALLY at foot)*:

| # | Finding | In-Scope Surface (S-ID) | Role Lens | Severity |
|---|---------|------------------------|-----------|----------|
| 1 | [Technical concern] | [S-00X] | [lens] | [CRITICAL / MAJOR / MINOR / ADVISORY] |
| 2 | [Finding] | [S-00X] | [lens] | [severity] |
| 3 | [optional] | [S-00X] | [lens] | [severity] |
| **TALLY** | **CRITICAL: [n] / MAJOR: [n] / MINOR: [n] / ADVISORY: [n]** | | | |

*Section Severity = [worst tag] per §2a.*

**Verify Question**: [One.] **Simplify**: [One.]
**G_domain**: [PASS / CONDITIONAL / FAIL] -- [reason.]
**G_domain Aggregate**: [PASS / CONDITIONAL / FAIL]

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**CH-ID Cross-Gate Tally**:

| CH-ID | LIFECYCLE | DOMAIN | Converged? |
|-------|-----------|--------|------------|
| CH-001 | [copy]   | [copy] | [yes/no]   |
| CH-002 | [copy]   | [copy] | [yes/no]   |
| CH-003 | [copy]   | [copy] | [yes/no]   |

**CH-ID Final Assessment** *(N rows)*:

| CH-ID | G_lifecycle | G_domain | Final                        | Notes  |
|-------|-------------|----------|------------------------------|--------|
| CH-001| [copy]      | [copy]   | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-002| [copy]      | [copy]   | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-003| [copy]      | [copy]   | [DEFEATED / PARTIAL / HOLDS] | [note] |

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**GClose Rationale**: [2-3 sentences citing specific tool/process.]

---

## GATE VECTOR TABLE

| Gate        | Reviewer       | Verdict                     | Contract Cite           |
|-------------|----------------|-----------------------------|-------------------------|
| GOpen       | [CHALLENGER]   | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE]    | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_domain    | [DOMAIN(S)]    | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| GClose      | [CHALLENGER]   | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Convergence**: **Conflicts**: **Scope coverage**:

**Finding lineage check** *(LIFECYCLE CRITICAL/MAJOR rows that appear in DOMAIN HANDOFF
ACKNOWLEDGMENT with CARRY-FORWARD are the highest-confidence cross-reviewer signals;
list by finding # and S-ID)*:

**§6 status**: [All handoff items acknowledged? List violations if present.]

**Finding tally cross-check** *(LIFECYCLE + DOMAIN tallies; worst tag drives gate)*:

---

## DISPOSITION

**Gate vector**: GOpen=[_] G_domain_agg=[_] G_lifecycle=[_] GClose=[_]

**§3 formula**:
```
GClose=FAIL -> BLOCKED  Any Gi=FAIL -> BLOCKED
No FAIL, any CONDITIONAL -> CONDITIONAL  All PASS -> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]
**Null hypothesis defeat**: [DEFEATED / PARTIALLY / HOLDS -- one sentence.]
**Primary driver**: [One sentence.]

---

## ACTION ITEM REGISTER

| CH-ID | Item | Disposition | Owner | Resolution Criterion |
|-------|------|-------------|-------|----------------------|
| CH-001 | [what] | [class] | [role] | [what closes it] |

---

## SCORING

```
Composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 9 * 45)
```
```

---

## V-05 -- Full Integration: Role Sequence + Output Format + Inertia Framing

**Variation axis**: All three single-axis hypotheses combined: V-01 (LIFECYCLE HANDOFF PACKET)
+ V-02 (table-primary mode with FINDING TALLY) + V-03 (per-role inertia verdict and INERTIA
DEFEAT LEDGER).

**Hypothesis**: Full integration creates three mutually reinforcing structural chains:
(1) finding lineage chain -- LIFECYCLE table -> HANDOFF PACKET (same schema) -> DOMAIN
ACKNOWLEDGMENT -> DOMAIN table; (2) severity audit chain -- table Severity tag -> TALLY row ->
Section Severity -> §2a gate verdict (formula-mechanical, no editorial step);
(3) inertia defeat chain -- NULL HYPOTHESIS REGISTER -> per-role INERTIA VERDICT ->
INERTIA DEFEAT LEDGER -> final defeat state. Together these three chains close all three
major audit gaps in V-05 R3: cross-reviewer finding traceability (chain 1), severity derivation
without inference (chain 2), and multi-perspective null hypothesis defeat (chain 3). Expected
excellence pattern: E-12 -- triple-chain integration; candidate for C-20 (finding lineage),
C-19 (inertia ledger), and confirmation of C-18 (handoff packet).

---

```
depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any pre-printed
heading, label, field, formula, or structural element. Do not add sections between pre-printed
headers. If a field cannot be filled, write `[N/A -- reason]`.

**Table-primary rule**: All findings appear in FINDING SURFACE LINKAGE TABLEs only per §5a.
No prose finding lists. Severity derives only from table Severity column.

---

## SCOPE SURFACE REGISTER

*Complete before DISPOSITION_CONTRACT. Each surface must be nameable as a specific section,
interface, behavioral claim, schema component, or named protocol. Generic descriptions
("all sections", "the full document") are not acceptable.*

| S-ID  | Surface Name                                                             | Why In Scope   | Primary Lens          |
|-------|--------------------------------------------------------------------------|----------------|-----------------------|
| S-001 | [Specific surface]                                                       | [One sentence] | [DOMAIN / LIFECYCLE / either] |
| S-002 | [Specific surface]                                                       | [One sentence] | [DOMAIN / LIFECYCLE / either] |
| S-003 | [Optional]                                                               | [One sentence] | [DOMAIN / LIFECYCLE / either] |

*S-IDs carry to §1 IN-SCOPE and to every FINDING SURFACE LINKAGE TABLE. A finding without a
registered S-ID is out-of-scope and must not appear in any table.*

---

## NULL HYPOTHESIS REGISTER

*Complete before BRACKET OPENING. The tool/process named here is distributed to every
reviewer section for per-role inertia assessment (§6). Generic phrases not acceptable.*

| Field | Value |
|-------|-------|
| What teams use today | [Specific tool, process, or workaround] |
| Why it works well enough | [One sentence] |
| Where it breaks down | [One sentence] |
| Switching cost | [HIGH / MEDIUM / LOW] |
| Null hypothesis strength | [HIGH / MEDIUM / LOW] |

---

======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK -- complete §1 before proceeding; do not alter §2-§7]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE (copy from SCOPE SURFACE REGISTER by S-ID and name; rows = register rows):
  1. [S-001: name]
  2. [S-002: name]
  3. [S-003: if active]
OUT-OF-SCOPE: [surface -- reason. "None" if nothing excluded.]
Scope Amendment Protocol: SCOPE AMENDMENT: [surface] -- [reason]. Silent expansion violates.
§1 COMPLETE.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks commitment. MEDIUM = Conditions. LOW = Advisory.

§2a -- SEVERITY AUDIT CHAIN [IMMUTABLE]
  Each finding row in any FINDING SURFACE LINKAGE TABLE carries a Severity tag:
    CRITICAL = HIGH (FAIL gate). MAJOR = MEDIUM (CONDITIONAL gate).
    MINOR = LOW (PASS gate). ADVISORY = no gate impact.
  Section Severity = worst(Severity column) over all rows in that section's table.
    Verify using FINDING TALLY row at table foot.
  Gate verdict (formula-mechanical -- no editorial override):
    Any CRITICAL in section -> Gate = FAIL
    Any MAJOR (no CRITICAL) -> Gate = CONDITIONAL
    MINOR / ADVISORY / empty -> Gate = PASS
  This chain is as binding as §3.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  G = {GOpen, G_domain_agg, G_lifecycle, GClose}
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND any CONDITIONAL
  READY <-- all PASS

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  N = CH-ID Count declared in BRACKET OPENING. Every downstream CH-ID table = exactly N rows.
  Count violation = §5 breach. PASS prohibited if any row = OPEN.

§5a -- TABLE-PRIMACY RULE [IMMUTABLE]
  Findings exist only in FINDING SURFACE LINKAGE TABLEs. Prose finding lists violate the
  audit trail. CRITICAL/MAJOR rows may have attached Detail subsections; all other findings
  are complete in the table row. Severity from table Severity column only.

§6 -- HANDOFF PROTOCOL [IMMUTABLE]
  After LIFECYCLE, a LIFECYCLE HANDOFF PACKET carries CRITICAL/MAJOR rows from the
  LIFECYCLE FINDING SURFACE LINKAGE TABLE in the same schema (Finding / S-ID / Role Lens /
  Severity). DOMAIN opens with DOMAIN HANDOFF ACKNOWLEDGMENT. Every packet row receives a
  Disposition: CARRY-FORWARD / DOMAIN-N/A (reason) / ESCALATE. Blank = §6 violation.

§7 -- INERTIA DISTRIBUTION REQUIREMENT [IMMUTABLE]
  Every reviewer section must include a PER-ROLE INERTIA ASSESSMENT evaluating the specific
  tool/process from the NULL HYPOTHESIS REGISTER from that role's lens. Verdict:
  SURVIVES / WEAKENED / DEFEATED. Missing assessment = §7 violation. INERTIA DEFEAT LEDGER
  after BRACKET CLOSING aggregates all verdicts. Final defeat state = worst(verdicts):
  all DEFEATED -> DEFEATED; any SURVIVES -> HOLDS; otherwise -> PARTIALLY DEFEATED.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================

---

## ROLE MANIFEST

Read `.craft/roles/signal/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |

*Order: BRACKET OPENING -> LIFECYCLE -> LIFECYCLE HANDOFF PACKET -> DOMAIN HANDOFF ACKNOWLEDGMENT
-> DOMAIN -> BRACKET CLOSING -> INERTIA DEFEAT LEDGER.*
*(--depth deep: add DOMAIN-2, DOMAIN-3. Each receives the same HANDOFF PACKET and produces its
own HANDOFF ACKNOWLEDGMENT and PER-ROLE INERTIA ASSESSMENT.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis** *(from NULL HYPOTHESIS REGISTER -- name the specific tool or process)*:
[The team continues to use [TOOL/PROCESS from Register] because [WHY IT WORKS from Register].
One sentence. Do not substitute generic language.]

**Null hypothesis strength**: [copy from register]

**Challenge claims**:

| CH-ID  | Challenge Claim                                                                        | Severity              |
|--------|----------------------------------------------------------------------------------------|-----------------------|
| CH-001 | [Switching cost, workaround viability, or adoption friction. One sentence.]            | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2]                                                                              | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional]                                                                  | [HIGH / MEDIUM / LOW] |

**CH-ID Count declared**: N = [count the rows above]

**PER-ROLE INERTIA ASSESSMENT -- CHALLENGER** *(§7 requirement)*:
Status-quo evaluated: [copy tool/process from NULL HYPOTHESIS REGISTER -- do not substitute]
Lens: inertia strength, switching cost, workaround persistence
INERTIA VERDICT: [SURVIVES / WEAKENED / DEFEATED]
Justification: [One sentence from challenger lens.]

**Verify Question**: [One from `lens.verify`.]
**Simplify**: [One from `lens.simplify`.]
**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]

*GOpen and all CH-IDs carry forward. Order: LIFECYCLE -> LIFECYCLE HANDOFF PACKET -> DOMAIN.*

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy from BRACKET OPENING]
*(DOMAIN has not run. Assess commitment readiness from GOpen alone.)*

**PER-ROLE INERTIA ASSESSMENT -- LIFECYCLE** *(§7 requirement)*:
Status-quo evaluated: [copy tool/process from NULL HYPOTHESIS REGISTER -- do not substitute]
Lens: commitment readiness, program timelines, decision-process friction
INERTIA VERDICT: [SURVIVES / WEAKENED / DEFEATED]
Justification: [One sentence. Does the status-quo satisfy this role's decision-process needs?]

**CH-ID Verdict Preview**:

| CH-ID  | Status                       |
|--------|------------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [omit if inactive]           |

**CH-ID Response Table** *(exactly N rows per §5)*:

| CH-ID  | Claim (copy) | Commitment Response | Status                       |
|--------|--------------|---------------------|------------------------------|
| CH-001 | [copy]       | [RESPONSE]          | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]       | [RESPONSE]          | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE]      | [ADDRESSED / PARTIAL / OPEN] |

**FINDING SURFACE LINKAGE TABLE** *(§5a: findings here only; TALLY at foot)*:

| # | Finding | In-Scope Surface (S-ID) | Role Lens | Severity |
|---|---------|------------------------|-----------|----------|
| 1 | [Commitment/program concern] | [S-00X] | [lens.verify or lens.simplify] | [CRITICAL / MAJOR / MINOR / ADVISORY] |
| 2 | [Finding] | [S-00X] | [lens] | [severity] |
| **TALLY** | **CRITICAL: [n] / MAJOR: [n] / MINOR: [n] / ADVISORY: [n]** | | | |

*Section Severity = [worst tag in Severity column] per §2a.*

*(Attach Detail subsections for CRITICAL/MAJOR rows only: "Detail [S-ID]: [prose elaboration]")*

**Decision-readiness**: [One paragraph referencing GOpen explicitly. G_domain not yet available.]

**Verify Question**: [One from `lens.verify`.]
**Simplify**: [One from `lens.simplify`.]
**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL -- derived from Section Severity per §2a]
**G_lifecycle Reason**: [One sentence.]

---

## LIFECYCLE HANDOFF PACKET

*(§6 protocol. Same schema as LIFECYCLE FINDING SURFACE LINKAGE TABLE. DOMAIN opens with
DOMAIN HANDOFF ACKNOWLEDGMENT referencing each row. Blank Disposition = §6 violation.)*

**CRITICAL/MAJOR findings forwarded** *(rows where Severity = CRITICAL or MAJOR from LIFECYCLE
FINDING SURFACE LINKAGE TABLE -- same schema preserved)*:

| # | Finding (copy) | In-Scope Surface (S-ID) | Lifecycle Role Lens | Severity |
|---|---------------|------------------------|---------------------|----------|
| [#] | [copy finding] | [copy S-ID] | [copy lens] | [CRITICAL / MAJOR] |
| *(write "None -- no CRITICAL or MAJOR rows in LIFECYCLE table" if applicable)* |

**Open CH-IDs forwarded** *(PARTIAL/OPEN from lifecycle CH-ID Response Table)*:

| CH-ID | Lifecycle Status | Note for Domain |
|-------|-----------------|-----------------|
| [CH-00X] | [PARTIAL / OPEN] | [Domain evidence that would address this] |
| *(write "None" if all ADDRESSED)* |

**LIFECYCLE HANDOFF PACKET COMPLETE.** Domain section begins below.

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy from BRACKET OPENING]
Received G_lifecycle: [copy from LIFECYCLE]

**DOMAIN HANDOFF ACKNOWLEDGMENT** *(§6 protocol -- one row per packet item; blank = violation)*:

| # | Item (from Handoff Packet) | Type | Domain Disposition |
|---|---------------------------|------|--------------------|
| [#] | [finding or CH-ID from packet] | [FINDING / CH-ID] | [CARRY-FORWARD / DOMAIN-N/A: reason / ESCALATE] |
| *(one row per item; do not omit rows)* |

**PER-ROLE INERTIA ASSESSMENT -- DOMAIN** *(§7 requirement)*:
Status-quo evaluated: [copy tool/process from NULL HYPOTHESIS REGISTER -- do not substitute]
Lens: technical feasibility, architecture soundness, implementation cost
INERTIA VERDICT: [SURVIVES / WEAKENED / DEFEATED]
Justification: [One sentence from technical lens.]

**CH-ID Verdict Preview**:

| CH-ID  | Status                       |
|--------|------------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [omit if inactive]           |

**CH-ID Response Table** *(exactly N rows per §5)*:

| CH-ID  | Claim (copy)              | Technical Response | Status                       |
|--------|---------------------------|--------------------|------------------------------|
| CH-001 | [copy from BRACKET OPENING] | [RESPONSE]       | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]                    | [RESPONSE]         | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active]          | [RESPONSE]         | [ADDRESSED / PARTIAL / OPEN] |

**FINDING SURFACE LINKAGE TABLE** *(§5a: findings here only; TALLY at foot)*:

| # | Finding | In-Scope Surface (S-ID) | Role Lens | Severity |
|---|---------|------------------------|-----------|----------|
| 1 | [Technical/architecture concern] | [S-00X] | [lens] | [CRITICAL / MAJOR / MINOR / ADVISORY] |
| 2 | [Finding] | [S-00X] | [lens] | [severity] |
| 3 | [optional] | [S-00X] | [lens] | [severity] |
| **TALLY** | **CRITICAL: [n] / MAJOR: [n] / MINOR: [n] / ADVISORY: [n]** | | | |

*Section Severity = [worst tag] per §2a.*

*(Attach Detail subsections for CRITICAL/MAJOR rows only.)*

**Verify Question**: [One from `lens.verify`.]
**Simplify**: [One from `lens.simplify`.]
**G_domain Verdict**: [PASS / CONDITIONAL / FAIL -- from Section Severity per §2a]
**G_domain Reason**: [One sentence. CONDITIONAL: name condition. FAIL: name gap.]

*(--depth deep: repeat DOMAIN-2, DOMAIN-3. Each receives HANDOFF PACKET, produces
ACKNOWLEDGMENT, PER-ROLE INERTIA ASSESSMENT, FINDING TABLE, TALLY. G_domain Aggregate = worst.)*

**G_domain Aggregate**: [PASS / CONDITIONAL / FAIL]

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
*Full record: scope, CH-ID tables, gate verdicts, all finding tables received.*

**CH-ID Cross-Gate Tally** *(scan for convergence: same non-ADDRESSED status in both = high signal)*:

| CH-ID  | LIFECYCLE Status              | DOMAIN Status              | Converged? |
|--------|-------------------------------|----------------------------|------------|
| CH-001 | [copy from LIFECYCLE preview] | [copy from DOMAIN preview] | [yes / no] |
| CH-002 | [copy]                        | [copy]                     | [yes / no] |
| CH-003 | [copy if active]              | [copy if active]           | [yes / no] |

**CH-ID Final Assessment** *(exactly N rows per §5)*:

| CH-ID  | G_lifecycle    | G_domain      | Final Status                 | Notes              |
|--------|----------------|---------------|------------------------------|--------------------|
| CH-001 | [copy]         | [copy]        | [DEFEATED / PARTIAL / HOLDS] | [ONE_SENTENCE_NOTE]|
| CH-002 | [copy]         | [copy]        | [DEFEATED / PARTIAL / HOLDS] | [note]             |
| CH-003 | [copy if active] | [copy]      | [DEFEATED / PARTIAL / HOLDS] | [note]             |

**Remaining gaps**: ["None -- all CH-IDs DEFEATED." or list gaps.]

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**GClose Rationale**: [2-3 sentences citing the specific tool/process from NULL HYPOTHESIS REGISTER.]

---

## INERTIA DEFEAT LEDGER

*(Aggregates all PER-ROLE INERTIA ASSESSMENTs per §7. Final defeat state = worst of all verdicts.)*

| Role | Lens | INERTIA VERDICT | Justification |
|------|------|-----------------|-----------------------|
| CHALLENGER | inertia-advocate | [copy from BRACKET OPENING] | [copy justification] |
| LIFECYCLE  | PM/program       | [copy from LIFECYCLE]       | [copy justification] |
| DOMAIN     | technical        | [copy from DOMAIN]          | [copy justification] |

**Final null hypothesis defeat state** *(§7 formula -- worst of all verdicts)*:
All DEFEATED -> DEFEATED | any SURVIVES -> HOLDS | otherwise -> PARTIALLY DEFEATED

**Final defeat state**: [DEFEATED / PARTIALLY DEFEATED / HOLDS]

**Narrative**: [One sentence. Reference the specific tool/process from NULL HYPOTHESIS REGISTER.
Example: "[Tool] PARTIALLY DEFEATED -- LIFECYCLE and CHALLENGER see it weakened, but DOMAIN
finds it technically viable for current scale."]

---

## GATE VECTOR TABLE

| Gate                         | Reviewer          | Verdict                     | Contract Cite           |
|------------------------------|-------------------|-----------------------------|-------------------------|
| GOpen -- bracket opening     | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_lifecycle -- lifecycle     | [LIFECYCLE_ROLE]  | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_domain -- domain aggregate | [DOMAIN_ROLE(S)]  | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| GClose -- bracket closing    | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Convergence** *(CH-ID Cross-Gate Tally converged rows -- highest-confidence signals)*:

**Conflicts** *(incompatible responses or findings; name roles and tension)*:

**Scope coverage** *(S-IDs not cited in any finding table -- coverage gaps)*:
[S-00X: [name] -- no reviewer cited this surface. OR "None -- all registered surfaces cited."]

**Inertia signal** *(cross-role divergence from INERTIA DEFEAT LEDGER)*:
[Roles with divergent INERTIA VERDICTs (e.g., CHALLENGER=DEFEATED vs DOMAIN=SURVIVES) are the
strongest inertia signal -- name roles and divergence here.]

**Finding lineage** *(LIFECYCLE CRITICAL/MAJOR rows forwarded via HANDOFF PACKET; list by # and S-ID;
note if domain CARRY-FORWARD or DOMAIN-N/A for each)*:

**Tally cross-check** *(LIFECYCLE + DOMAIN tallies; worst tag determines gate)*:
[LIFECYCLE: C=[n] M=[n] | DOMAIN: C=[n] M=[n] | Gate-driving: [tag]]

**§6 status**: [All handoff items acknowledged? Violations if any. "None." if clean.]

---

## DISPOSITION

**Gate vector** *(copy from GATE VECTOR TABLE)*:
- GOpen = [copy]
- G_domain_agg = [copy]
- G_lifecycle = [copy]
- GClose = [copy]

**Apply contract §3 formula** *(do not alter; evaluate gate vector against pre-stated formula)*:

```
G = {GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]}
GClose = FAIL? --> BLOCKED  (challenger override: null hypothesis holds)
Any other Gi = FAIL? --> BLOCKED
No FAIL, any CONDITIONAL? --> CONDITIONAL
All PASS? --> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**Null hypothesis defeat** *(from INERTIA DEFEAT LEDGER final defeat state and GClose)*:
[DEFEATED / PARTIALLY DEFEATED / HOLDS -- one sentence citing specific tool/process.]

**Primary driver**: [The gate and finding most responsible for this disposition -- one sentence.]

**Conditions** *(CONDITIONAL only)*:
1. [Condition from first CONDITIONAL gate, in gate resolution order: GOpen -> G_lifecycle -> G_domain -> GClose.]

**Blocker** *(BLOCKED only)*: [Specific finding from the FAIL gate.]

---

## ACTION ITEM REGISTER

*One row per PARTIAL or HOLDS CH-ID from BRACKET CLOSING. Items not sourced from a CH-ID
are marked ADVISORY-OBS.*

| CH-ID  | Item Description    | Disposition Class                    | Owner Role  | Resolution Criterion                             |
|--------|---------------------|--------------------------------------|-------------|--------------------------------------------------|
| CH-001 | [What must be done] | [BLOCKED / CONDITIONAL / ADVISORY]   | [ROLE_NAME] | [What must be true to close this item]           |

---

## SCORING

```
Composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 9 * 45)
```

Golden threshold: all 5 essential criteria pass AND composite >= 80. Max composite: 135.
```
