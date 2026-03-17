# org-review Variations -- Round 5 (v5 rubric, 2026-03-16)

Generated: 2026-03-16
Skill: org-review
Rubric: v5 (C-01 through C-19, max 145)

## Prior Round Summary

- R1 (v1): V-05 best. E-1 (verdict-preview tables -> C-11), E-2 (count constraint -> C-12).
- R2 (v2): V-05=120/120. E-3 (LIFECYCLE-before-DOMAIN -> C-14), E-4 (NULL HYPOTHESIS REGISTER -> C-13).
- R3 (v3): E-5 (SCOPE SURFACE REGISTER -> C-15), E-6 (FINDING SURFACE LINKAGE TABLE -> C-16), E-7 (§2a chain -> C-17). Max raised to 135.
- R4 (v4): E-8 (§6 HANDOFF PACKET + blank ACKNOWLEDGMENT row -> C-18), E-9 (§5a TABLE-PRIMACY + FINDING TALLY -> C-19). Max raised to 145.

## Round 5 Strategy

All R5 variants inherit R4 V-05 as non-negotiable base. C-18 and C-19 are now rubric criteria -- every
variation must satisfy both. Round 5 explores axes that have not yet been varied with C-18+C-19 baked in.

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Phrasing register (imperative/mechanical) | Numbered prohibition format with per-clause VIOLATION TABLES converts every contract rule into a testable assertion, removing editorial inference from compliance checking |
| V-02 | Lifecycle emphasis (phase sub-contracts) | Splitting LIFECYCLE into UPSTREAM and EXECUTION phases with per-phase gates and an intra-LIFECYCLE phase handoff extends the C-18 structural guarantee to intra-role phase transitions |
| V-03 | Inertia framing (org-wide INERTIA DEFEAT LEDGER) | Adding an INERTIA VERDICT column to every FINDING SURFACE LINKAGE TABLE and synthesizing an org-wide INERTIA DEFEAT LEDGER converts the review from "are there blockers?" to "did the org collectively defeat the status quo?" |
| V-04 | V-01 + V-02 | Imperative prohibitions + phase sub-contracts |
| V-05 | V-01 + V-02 + V-03 | Full integration |

---

## V-01 -- Single Axis: Phrasing Register (Imperative/Mechanical Prohibitions)

**Variation axis**: Phrasing register. Every contract rule is expressed as a numbered prohibition
with an explicit VIOLATION TYPE and HOW DETECTED entry. The instructions preamble uses imperative
second-person. No descriptive or passive clauses in the contract block.

**Hypothesis**: Declarative phrasing ("findings must appear in the table") leaves room for
editorial compliance judgment. Numbered prohibition format ("PROHIBITED: prose finding list outside
a table. VIOLATION TYPE: §5a-violation. DETECTED BY: finding absent from FINDING SURFACE LINKAGE
TABLE") makes each rule a binary pass/fail assertion. Expected excellence: the prohibition format
may surface C-20 -- per-clause violation inventory as a structural audit primitive.

---

```
depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

MANDATORY: Fill every [BRACKETED_FIELD]. Do not alter, reorder, or omit any pre-printed
heading, label, field, formula, or structural element. Do not add sections between pre-printed
headers. Do not add roles not in the manifest. If a field cannot be filled, write [N/A -- reason].

---

## SCOPE SURFACE REGISTER

Complete this register before the DISPOSITION_CONTRACT. Name each concrete surface the
artifact exposes for review. Generic descriptions ("all sections", "the full document",
"all fields") are NOT ACCEPTABLE -- they prevent surface-specific finding linkage and
violate §1. Each surface must be nameable as a specific section heading, interface
contract, behavioral claim, schema component, or named protocol.

| S-ID  | Surface Name                                                                     | Why In Scope                                                     | Primary Lens              |
|-------|----------------------------------------------------------------------------------|------------------------------------------------------------------|---------------------------|
| S-001 | [Specific section, interface, or behavioral claim -- not "all sections"]         | [One sentence: what reviewer question does this surface answer?] | [DOMAIN / LIFECYCLE / either] |
| S-002 | [Another specific surface -- not "all fields" or "the document"]                 | [One sentence]                                                   | [DOMAIN / LIFECYCLE / either] |
| S-003 | [Optional -- add rows to be exhaustive; each must name a discrete surface]       | [One sentence]                                                   | [DOMAIN / LIFECYCLE / either] |

S-IDs carry forward to §1 IN-SCOPE and to finding citations in every reviewer section.
A finding that cannot cite a registered S-ID is out-of-scope and MUST NOT appear in any
FINDING SURFACE LINKAGE TABLE or prose.

---

## NULL HYPOTHESIS REGISTER

Complete before BRACKET OPENING. Name the concrete alternative the team uses today.
Generic phrases ("do nothing", "status quo") are NOT ACCEPTABLE -- name the specific
tool, process, or workaround.

| Field                    | Value                                                                         |
|--------------------------|-------------------------------------------------------------------------------|
| What teams use today     | [Specific tool, process, or workaround -- not "do nothing"]                   |
| Why it works well enough | [One sentence -- the genuine case for continuing with the status quo]         |
| Where it breaks down     | [One sentence -- the gap or friction that motivates this artifact]            |
| Switching cost           | [HIGH / MEDIUM / LOW]                                                         |
| Null hypothesis strength | [HIGH / MEDIUM / LOW]                                                         |

This register is the source of truth for all null hypothesis fields in this review.

---

======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2 through §6;
reviewer sections may not execute until §1 COMPLETE marker is reached]
======================================================================

§1 -- SCOPE ENUMERATION
Fill this section before proceeding. Copy from SCOPE SURFACE REGISTER by S-ID and name.

IN-SCOPE (copy S-ID and name exactly; total row count must equal SCOPE SURFACE REGISTER rows):
  1. [S-001: name]
  2. [S-002: name]
  3. [S-003: name if active]

OUT-OF-SCOPE (surfaces this review will not evaluate):
  1. [SURFACE -- REASON_EXCLUDED]  (write "None" if nothing excluded)

Scope Amendment Protocol: SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]
Silent scope expansion is PROHIBITED. VIOLATION TYPE: §1-scope-expansion. DETECTED BY:
finding cites surface not in IN-SCOPE list above.

§1 COMPLETE -- role selection and reviewer execution proceeds below.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  PROHIBITED: redefining or restating these definitions at any gate or in any reviewer section.
  VIOLATION TYPE: §2-restatement. DETECTED BY: severity definition block appearing outside §2.
    HIGH   = Blocks commitment. No commitment proceeds with open HIGH findings.
    MEDIUM = Conditions commitment. Proceeds only after named resolution.
    LOW    = Advisory. Commitment may proceed.

§2a -- SEVERITY AUDIT CHAIN [IMMUTABLE -- as binding as §3]
  PROHIBITED: any gate verdict that contradicts the formula below.
  VIOLATION TYPE: §2a-override. DETECTED BY: gate verdict contradicts formula output.
  Severity tag per finding: CRITICAL | MAJOR | MINOR | ADVISORY
    CRITICAL -> gate HIGH (blocks)
    MAJOR    -> gate MEDIUM (conditions)
    MINOR    -> gate LOW (advisory)
    ADVISORY -> no gate impact
  Section Severity = worst(Severity tags in section's FINDING SURFACE LINKAGE TABLE TALLY row)
    worst() ranking: CRITICAL > MAJOR > MINOR > ADVISORY
  Gate verdict derivation (formula-mechanical):
    CRITICAL in TALLY -> gate = FAIL
    MAJOR in TALLY (no CRITICAL) -> gate = CONDITIONAL
    MINOR or ADVISORY only -> gate = PASS
    TALLY row blank or absent -> §2a-tally-missing violation; gate = CONDITIONAL until resolved

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  PROHIBITED: editorial override of this formula.
  VIOLATION TYPE: §3-override. DETECTED BY: Disposition contradicts formula output.
  G = {GOpen, G_lifecycle, G_domain_agg, GClose}
  BLOCKED      <- GClose = FAIL  (challenger override: null hypothesis holds)
               OR any Gi = FAIL
  CONDITIONAL  <- no Gi = FAIL  AND  any Gi = CONDITIONAL
  READY        <- all Gi = PASS

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  PROHIBITED: reviewer section without contract cite at section opening.
  VIOLATION TYPE: §4-cite-gap. DETECTED BY: contract cite line absent from section header.
  Each reviewer section opens with exactly: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  PROHIBITED: CH-ID table with row count != N (N = CH-ID Count declared in BRACKET OPENING).
  VIOLATION TYPE: §5-count-violation. DETECTED BY: row count in any CH-ID table != N.
  PROHIBITED: PASS verdict when any CH-ID row shows OPEN status.
  VIOLATION TYPE: §5-open-block. DETECTED BY: gate = PASS with OPEN row in CH-ID table.
  Each challenge claim receives a CH-ID: CH-001, CH-002, ... (declared in BRACKET OPENING).
  Every downstream CH-ID table must contain exactly N rows.

§5a -- TABLE-PRIMACY RULE [IMMUTABLE]
  PROHIBITED: prose finding lists (bulleted or numbered lists of findings outside a table).
  VIOLATION TYPE: §5a-prose-finding. DETECTED BY: finding appears in prose but not in any
    FINDING SURFACE LINKAGE TABLE.
  PROHIBITED: findings omitted from FINDING SURFACE LINKAGE TABLE but present in prose.
  VIOLATION TYPE: §5a-table-bypass. DETECTED BY: prose paragraph with finding language has no
    corresponding row in section's FINDING SURFACE LINKAGE TABLE.
  PERMITTED: "Detail [S-ID]: [prose]" subsection attached after a table row, contextualizing
    a CRITICAL or MAJOR finding. The table row must exist first.
  Section Severity is derived EXCLUSIVELY from the FINDING TALLY row. Prose-described
  severity does not count. A section with no FINDING SURFACE LINKAGE TABLE TALLY row
  has no defined Section Severity -- this is a §5a-tally-missing violation.

§6 -- LIFECYCLE HANDOFF PROTOCOL [IMMUTABLE]
  PROHIBITED: DOMAIN section that lacks DOMAIN HANDOFF ACKNOWLEDGMENT at section open.
  VIOLATION TYPE: §6-acknowledgment-missing. DETECTED BY: DOMAIN section header not
    immediately followed by DOMAIN HANDOFF ACKNOWLEDGMENT table.
  PROHIBITED: DOMAIN HANDOFF ACKNOWLEDGMENT with any blank Disposition cell.
  VIOLATION TYPE: §6-blank-disposition. DETECTED BY: blank cell in Disposition column.
  PROHIBITED: DOMAIN gate = PASS when any §6 violation is present.
  After LIFECYCLE completes, LIFECYCLE HANDOFF PACKET is emitted (see pre-printed section).
  The HANDOFF PACKET carries: (a) all CH-IDs with PARTIAL or OPEN lifecycle status, and
  (b) all CRITICAL and MAJOR findings from the LIFECYCLE FINDING SURFACE LINKAGE TABLE.
  DOMAIN HANDOFF ACKNOWLEDGMENT must name each item with one of:
    CARRY-FORWARD -- domain will address (requires response in CH-ID Response Table)
    DOMAIN-N/A    -- outside domain scope (reason required in same cell)
    ESCALATE      -- elevates finding severity (state new severity)

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================

---

## ROLE MANIFEST

Read `.craft/roles/`. Assign each slot from loaded roles.

| Slot                                         | Archetype            | Role       | Selection Rationale |
|----------------------------------------------|----------------------|------------|---------------------|
| CHALLENGER (bracket open + close -- fixed)   | inertia-advocate     | [ROLE_NAME] | [ONE_SENTENCE]     |
| LIFECYCLE                                    | PM/program           | [ROLE_NAME] | [ONE_SENTENCE]     |
| DOMAIN                                       | technical/domain     | [ROLE_NAME] | [ONE_SENTENCE]     |

Execution order: BRACKET OPENING -> LIFECYCLE -> LIFECYCLE HANDOFF PACKET ->
  DOMAIN HANDOFF ACKNOWLEDGMENT -> DOMAIN -> BRACKET CLOSING.

LIFECYCLE runs before DOMAIN. This is not advisory -- it is a §14 sequence requirement.
PROHIBITED: DOMAIN section that precedes LIFECYCLE section.
VIOLATION TYPE: §14-sequence. DETECTED BY: DOMAIN header appears before LIFECYCLE header.

For --depth deep: add DOMAIN-2, DOMAIN-3, etc. Each DOMAIN section receives the same
LIFECYCLE HANDOFF PACKET and opens with its own DOMAIN HANDOFF ACKNOWLEDGMENT.

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis** (from NULL HYPOTHESIS REGISTER -- name the specific tool or process):
[The team continues to use [TOOL/PROCESS from Register] because [WHY IT WORKS from Register].
One sentence. Do not substitute generic language.]

**Null hypothesis strength**: [Copy from NULL HYPOTHESIS REGISTER -- HIGH / MEDIUM / LOW]

**Challenge claims** (assign CH-IDs; carry to every downstream section per §5):

| CH-ID  | Challenge Claim                                                                         | Severity              |
|--------|-----------------------------------------------------------------------------------------|-----------------------|
| CH-001 | [CLAIM_1 -- switching cost, workaround viability, or adoption friction. One sentence.]  | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2]                                                                               | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional]                                                                   | [HIGH / MEDIUM / LOW] |

**CH-ID Count declared**: N = [count the rows above -- every downstream CH-ID table must
  contain exactly N rows per §5]

**Verify Question**: [One from challenger's lens.verify]
**Simplify**: [One from challenger's lens.simplify]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence]

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy from BRACKET OPENING]

**CH-ID Verdict Preview** (fill before writing response table -- convergence anchor):

| CH-ID  | Status                       |
|--------|------------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [ADDRESSED / PARTIAL / OPEN -- omit if not active] |

**CH-ID Response Table** (exactly N rows per §5):

| CH-ID  | Challenge Claim (copy)  | This Role's Commitment-Frame Response | Status                       |
|--------|-------------------------|---------------------------------------|------------------------------|
| CH-001 | [copy]                  | [RESPONSE_1]                          | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]                  | [RESPONSE_2]                          | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active]        | [RESPONSE_3]                          | [ADDRESSED / PARTIAL / OPEN] |

**FINDING SURFACE LINKAGE TABLE** (§5a: findings appear HERE ONLY; prose finding lists PROHIBITED):

| Finding                                         | In-Scope Surface (S-ID) | Role Lens | Severity                          |
|-------------------------------------------------|-------------------------|-----------|-----------------------------------|
| [FINDING_1 -- commitment/program concern]       | [S-00X]                 | [lens]    | [CRITICAL / MAJOR / MINOR / ADVISORY] |
| [FINDING_2]                                     | [S-00X]                 | [lens]    | [severity]                        |
| **FINDING TALLY**                               | Total: [N]              | CRITICAL: [n] / MAJOR: [n] | MINOR: [n] / ADVISORY: [n] |

PROHIBITED: blank In-Scope Surface cell or blank Role Lens cell.
VIOLATION TYPE: §16-cell-violation. DETECTED BY: blank cell in either column above.
Section Severity = derived from FINDING TALLY row (not from prose). Per §2a formula.

**Decision-readiness assessment**: [Is evidence sufficient to proceed to technical review?
One paragraph referencing GOpen explicitly. DOMAIN not yet available -- assess commitment
readiness from challenger framing alone.]

**Null hypothesis status** (from NULL HYPOTHESIS REGISTER):
[STILL VIABLE / CHALLENGED / OPEN] -- [one sentence justification]

**Verify Question**: [One from this role's lens.verify]
**Simplify**: [One from this role's lens.simplify]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL -- derive from FINDING TALLY per §2a]
**G_lifecycle Reason**: [One sentence. If FAIL: DOMAIN review may be deferred.]

---

## LIFECYCLE HANDOFF PACKET

Produced by LIFECYCLE; consumed by DOMAIN at section open per §6.
PROHIBITED: altering pre-printed column headers.

**Open CH-IDs for DOMAIN** (rows where Status = PARTIAL or OPEN above):

| CH-ID  | Lifecycle Status  | Challenge Claim (copy)  | Note for Domain                                      |
|--------|-------------------|-------------------------|------------------------------------------------------|
| [CH-00X] | [PARTIAL / OPEN] | [copy]                 | [What domain evidence would address this]            |
| (write "None -- all CH-IDs ADDRESSED" if no rows) |    |                         |                                                      |

**Escalated Findings for DOMAIN** (CRITICAL and MAJOR rows from FINDING SURFACE LINKAGE TABLE):

| Finding         | S-ID    | Lifecycle Severity      | Escalation Note                                      |
|-----------------|---------|-------------------------|------------------------------------------------------|
| [finding text]  | [S-00X] | [CRITICAL / MAJOR]      | [What domain lens might address or amplify this]     |
| (write "None" if no CRITICAL or MAJOR rows) |  |                    |                                                      |

**LIFECYCLE HANDOFF PACKET COMPLETE.** DOMAIN section begins below.

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy from BRACKET OPENING]
Received G_lifecycle: [copy from LIFECYCLE]

**DOMAIN HANDOFF ACKNOWLEDGMENT** (§6 -- blank Disposition cell = §6-blank-disposition violation):

| Item              | From Packet      | Type              | Disposition                                        |
|-------------------|------------------|-------------------|----------------------------------------------------|
| [CH-00X or text]  | Lifecycle Packet | [CH-ID / FINDING] | [CARRY-FORWARD / DOMAIN-N/A (reason) / ESCALATE]  |
| (one row per item in LIFECYCLE HANDOFF PACKET -- omitting a row is a §6 violation)          |

**CH-ID Verdict Preview** (fill before writing response table):

| CH-ID  | Status                       |
|--------|------------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [ADDRESSED / PARTIAL / OPEN -- omit if not active] |

**CH-ID Response Table** (exactly N rows per §5):

| CH-ID  | Challenge Claim (copy)                      | This Role's Technical Response | Status                       |
|--------|---------------------------------------------|--------------------------------|------------------------------|
| CH-001 | [copy from BRACKET OPENING]                 | [RESPONSE_1]                   | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]                                      | [RESPONSE_2]                   | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active]                            | [RESPONSE_3]                   | [ADDRESSED / PARTIAL / OPEN] |

**FINDING SURFACE LINKAGE TABLE** (§5a: findings appear HERE ONLY; prose finding lists PROHIBITED):

| Finding                                         | In-Scope Surface (S-ID) | Role Lens | Severity                          |
|-------------------------------------------------|-------------------------|-----------|-----------------------------------|
| [FINDING_1 -- technical/architecture concern]   | [S-00X]                 | [lens]    | [CRITICAL / MAJOR / MINOR / ADVISORY] |
| [FINDING_2]                                     | [S-00X]                 | [lens]    | [severity]                        |
| **FINDING TALLY**                               | Total: [N]              | CRITICAL: [n] / MAJOR: [n] | MINOR: [n] / ADVISORY: [n] |

PROHIBITED: blank In-Scope Surface cell or blank Role Lens cell. VIOLATION TYPE: §16-cell-violation.
Section Severity = derived from FINDING TALLY row per §2a formula.

**Verify Question**: [One from this role's lens.verify]
**Simplify**: [One from this role's lens.simplify]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL -- derive from FINDING TALLY per §2a]
**G_domain Reason**: [One sentence]

**G_domain Aggregate**: [worst verdict across all DOMAIN sections -- state explicitly]

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**CH-ID Cross-Gate Tally** (scan for convergence: same non-ADDRESSED status in both = high signal):

| CH-ID  | LIFECYCLE Status              | DOMAIN Status                | Converged? |
|--------|-------------------------------|------------------------------|------------|
| CH-001 | [copy from LIFECYCLE preview] | [copy from DOMAIN preview]   | [yes / no] |
| CH-002 | [copy]                        | [copy]                       | [yes / no] |
| CH-003 | [copy if active]              | [copy if active]             | [yes / no] |

**CH-ID Final Assessment** (exactly N rows per §5):

| CH-ID  | G_lifecycle           | G_domain             | Final Status                  | Notes             |
|--------|-----------------------|----------------------|-------------------------------|-------------------|
| CH-001 | [copy from LIFECYCLE] | [copy from DOMAIN]   | [DEFEATED / PARTIAL / HOLDS]  | [ONE_SENTENCE]    |
| CH-002 | [copy]                | [copy]               | [DEFEATED / PARTIAL / HOLDS]  | [note]            |
| CH-003 | [copy if active]      | [copy if active]     | [DEFEATED / PARTIAL / HOLDS]  | [note]            |

**Remaining gaps**: [What was not fully addressed. "None" if all CH-IDs DEFEATED.]

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
  PASS (DEFEATED): all CH-IDs DEFEATED -- record defeats null hypothesis.
  CONDITIONAL (PARTIAL): material gaps remain -- name them.
  FAIL (HOLDS): at least one CH-ID HOLDS -- null hypothesis survives.

**GClose Rationale**: [2-3 sentences referencing the specific tool/process from NULL HYPOTHESIS REGISTER.]

---

## GATE VECTOR TABLE

| Gate                         | Reviewer           | Verdict                     | Contract Cite           |
|------------------------------|--------------------|-----------------------------|-------------------------|
| GOpen -- bracket opening     | [CHALLENGER_ROLE]  | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_lifecycle -- lifecycle     | [LIFECYCLE_ROLE]   | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_domain -- domain aggregate | [DOMAIN_ROLE(S)]   | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| GClose -- bracket closing    | [CHALLENGER_ROLE]  | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Convergence** (CH-ID Cross-Gate Tally rows where Converged = yes -- highest-confidence signals):
[CH-00X: description. "None detected" if no converged rows.]

**Conflicts**: [Incompatible CH-ID responses or findings between roles. "None detected" if none.]

**Scope coverage** (scan S-IDs against findings -- uncited S-ID = coverage gap):
[S-00X: [name] -- not cited by any finding. "None" if all registered surfaces cited.]

**§6 protocol status**: [Were all HANDOFF PACKET items acknowledged? List any §6 violations.
"None -- all handoff items acknowledged." if clean.]

---

## DISPOSITION

**Gate vector** (from GATE VECTOR TABLE):
  GOpen         = [copy]
  G_lifecycle   = [copy]
  G_domain_agg  = [copy]
  GClose        = [copy]

**Apply §3 formula** (do not alter; evaluate gate vector against pre-stated formula):

```
G = {GOpen=[_], G_lifecycle=[_], G_domain_agg=[_], GClose=[_]}
GClose = FAIL? -> BLOCKED  (challenger override: null hypothesis holds)
Any other Gi = FAIL? -> BLOCKED
No FAIL, any CONDITIONAL? -> CONDITIONAL
All PASS? -> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]
**Null hypothesis defeat**: [DEFEATED / PARTIALLY DEFEATED / HOLDS -- one sentence, naming the specific tool/process.]
**Primary driver**: [Gate most responsible for this disposition.]
**Conditions** (CONDITIONAL only): [condition from first CONDITIONAL gate]
**Blocker** (BLOCKED only): [specific finding from the FAIL gate]

---

## ACTION ITEM REGISTER

One row per PARTIAL or HOLDS CH-ID from BRACKET CLOSING.

| CH-ID  | Item Description     | Disposition Class              | Owner Role  | Resolution Criterion                               |
|--------|----------------------|--------------------------------|-------------|-----------------------------------------------------|
| CH-001 | [What must be done]  | [BLOCKED / CONDITIONAL / ADV] | [ROLE_NAME] | [What must be true to close this item]              |

```

---

## V-02 -- Single Axis: Lifecycle Emphasis (Phase Sub-Contracts)

**Variation axis**: Lifecycle emphasis. The LIFECYCLE section is split into two named phases --
UPSTREAM (commitment readiness: strategy, feasibility, resource) and EXECUTION (technical
readiness: design, implementation, risk). Each phase has its own scope subset, gate, and a
phase-level HANDOFF PACKET bridging UPSTREAM->EXECUTION before the LIFECYCLE->DOMAIN packet.

**Hypothesis**: The current single LIFECYCLE gate catches lifecycle problems but blurs UPSTREAM
blockers (strategy not aligned, resources uncommitted) with EXECUTION blockers (design gaps,
technical debt). Splitting into phases creates G_upstream and G_execution that compose into
G_lifecycle per an extended §3 algebra. The UPSTREAM->EXECUTION phase handoff mirrors the §6
LIFECYCLE->DOMAIN handoff, potentially surfacing E-10: intra-LIFECYCLE phase handoffs as a
structural primitive on par with the inter-role §6 handoff.

---

```
depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every [BRACKETED_FIELD]. Do not alter, reorder, or omit any pre-printed
heading, label, field, formula, or structural element. Do not add sections between pre-printed
headers. If a field cannot be filled, write [N/A -- reason].

---

## SCOPE SURFACE REGISTER

Complete this register before the DISPOSITION_CONTRACT. Name each concrete surface the artifact
exposes for review. Generic descriptions are not acceptable. Tag each surface with the phase(s)
that should examine it: UPSTREAM | EXECUTION | DOMAIN | any combination.

| S-ID  | Surface Name                                                                     | Why In Scope      | Phase Tag                    | Primary Lens              |
|-------|----------------------------------------------------------------------------------|-------------------|------------------------------|---------------------------|
| S-001 | [Specific section, interface, or behavioral claim]                               | [One sentence]    | [UPSTREAM / EXECUTION / DOMAIN / multiple] | [LIFECYCLE / DOMAIN / either] |
| S-002 | [Another specific surface]                                                       | [One sentence]    | [phase tag]                  | [lens]                    |
| S-003 | [Optional]                                                                       | [One sentence]    | [phase tag]                  | [lens]                    |

S-IDs carry to §1 and to finding citations in every phase and reviewer section.

---

## NULL HYPOTHESIS REGISTER

| Field                    | Value                                                                    |
|--------------------------|--------------------------------------------------------------------------|
| What teams use today     | [Specific tool, process, or workaround -- not "do nothing"]              |
| Why it works well enough | [One sentence]                                                           |
| Where it breaks down     | [One sentence]                                                           |
| Switching cost           | [HIGH / MEDIUM / LOW]                                                    |
| Null hypothesis strength | [HIGH / MEDIUM / LOW]                                                    |

---

======================================================================
DISPOSITION_CONTRACT v2 (phase-extended)
[IMMUTABLE BLOCK]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE (copy S-ID and name from register; total rows must equal register rows):
  1. [S-001: name]
  2. [S-002: name]
  3. [S-003: name if active]
OUT-OF-SCOPE: [SURFACE -- REASON] ("None" if nothing excluded)
Scope Amendment Protocol: SCOPE AMENDMENT: [surface] added -- [reason]. Silent expansion violates §1.
§1 COMPLETE.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks commitment. MEDIUM = Conditions. LOW = Advisory.

§2a -- SEVERITY AUDIT CHAIN [IMMUTABLE]
  Severity tag per finding: CRITICAL | MAJOR | MINOR | ADVISORY
  Phase Severity = worst(Severity tags in phase FINDING TALLY row)
  Section Severity = worst(Phase Severities for all phases in section)
  Gate derivation (formula-mechanical):
    CRITICAL in TALLY -> gate = FAIL
    MAJOR (no CRITICAL) -> gate = CONDITIONAL
    MINOR or ADVISORY only -> gate = PASS
    No findings -> gate = PASS

§3 -- DISPOSITION ALGEBRA (phase-extended) [IMMUTABLE]
  G = {GOpen, G_upstream, G_execution, G_lifecycle, G_domain_agg, GClose}
  G_lifecycle = worst(G_upstream, G_execution)
  BLOCKED      <- GClose = FAIL  OR  any Gi = FAIL
  CONDITIONAL  <- no FAIL  AND  any Gi = CONDITIONAL
  READY        <- all Gi = PASS

§4 -- CONTRACT CITE [IMMUTABLE]
  Each reviewer section and phase opens with: "Contract: DISPOSITION_CONTRACT v2"

§5 -- CH-ID TRACING [IMMUTABLE]
  N = CH-ID Count declared in BRACKET OPENING.
  Every CH-ID table must contain exactly N rows. Count discrepancy = §5 violation.
  PASS prohibited when any CH-ID row shows OPEN status.

§5a -- TABLE-PRIMACY RULE [IMMUTABLE]
  Findings must appear in FINDING SURFACE LINKAGE TABLEs only. Prose finding lists are prohibited.
  A finding absent from a table is invisible to the §2a audit chain.
  Section Severity derives from FINDING TALLY row exclusively.
  Detail subsection [S-ID]: [prose] permitted only after the table row exists.

§6 -- LIFECYCLE HANDOFF PROTOCOL [IMMUTABLE]
  After LIFECYCLE completes (both phases), LIFECYCLE HANDOFF PACKET is emitted.
  DOMAIN section opens with DOMAIN HANDOFF ACKNOWLEDGMENT. Blank Disposition = §6 violation.
  HANDOFF PACKET carries: open/partial CH-IDs + CRITICAL/MAJOR lifecycle findings.
  ACKNOWLEDGMENT dispositions: CARRY-FORWARD | DOMAIN-N/A (reason) | ESCALATE

§6a -- PHASE HANDOFF PROTOCOL [IMMUTABLE]
  After UPSTREAM PHASE completes, UPSTREAM PHASE HANDOFF is emitted.
  EXECUTION PHASE opens with EXECUTION PHASE ACKNOWLEDGMENT. Blank = §6a violation.
  PHASE HANDOFF carries: partial/open CH-IDs from UPSTREAM + CRITICAL/MAJOR upstream findings.
  EXECUTION PHASE gate (G_execution) cannot be PASS if EXECUTION PHASE ACKNOWLEDGMENT is blank.

======================================================================
END DISPOSITION_CONTRACT v2
======================================================================

---

## ROLE MANIFEST

Read `.craft/roles/`. Assign each slot.

| Slot          | Archetype        | Role        | Selection Rationale |
|---------------|------------------|-------------|---------------------|
| CHALLENGER    | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE]      |
| LIFECYCLE     | PM/program       | [ROLE_NAME] | [ONE_SENTENCE]      |
| DOMAIN        | technical/domain | [ROLE_NAME] | [ONE_SENTENCE]      |

Execution order: BRACKET OPENING -> LIFECYCLE [UPSTREAM PHASE -> UPSTREAM PHASE HANDOFF ->
  EXECUTION PHASE] -> LIFECYCLE HANDOFF PACKET -> DOMAIN HANDOFF ACKNOWLEDGMENT -> DOMAIN -> BRACKET CLOSING.

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v2

**Null hypothesis**: [Name specific tool/process from NULL HYPOTHESIS REGISTER. One sentence.]
**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Challenge claims**:

| CH-ID  | Challenge Claim                                                                        | Severity              |
|--------|----------------------------------------------------------------------------------------|-----------------------|
| CH-001 | [CLAIM_1]                                                                              | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2]                                                                              | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional]                                                                  | [HIGH / MEDIUM / LOW] |

**CH-ID Count declared**: N = [count]

**Verify Question**: [One from challenger's lens.verify]
**Simplify**: [One from challenger's lens.simplify]
**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence]

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v2

### UPSTREAM PHASE
*(Scope: S-IDs tagged UPSTREAM. Commitment readiness: strategy alignment, resource confirmation, feasibility.)*

**CH-ID Verdict Preview** (fill before response table):

| CH-ID  | Status                       |
|--------|------------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [omit if not active]         |

**CH-ID Response Table -- UPSTREAM** (exactly N rows):

| CH-ID  | Challenge Claim (copy) | Upstream Commitment-Frame Response   | Status                       |
|--------|------------------------|--------------------------------------|------------------------------|
| CH-001 | [copy]                 | [upstream response]                  | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]                 | [upstream response]                  | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active]       | [upstream response]                  | [ADDRESSED / PARTIAL / OPEN] |

**UPSTREAM FINDING SURFACE LINKAGE TABLE** (§5a: findings here only; prose lists prohibited):

| Finding                                   | In-Scope Surface (S-ID) | Role Lens | Severity                          |
|-------------------------------------------|-------------------------|-----------|-----------------------------------|
| [FINDING -- strategy/resource concern]    | [S-00X, phase=UPSTREAM] | [lens]    | [CRITICAL / MAJOR / MINOR / ADVISORY] |
| **FINDING TALLY**                         | Total: [N]              | CRITICAL: [n] / MAJOR: [n] | MINOR: [n] / ADVISORY: [n] |

Blank In-Scope Surface or Role Lens = §16-cell-violation. Section Severity from TALLY per §2a.

**G_upstream Verdict**: [PASS / CONDITIONAL / FAIL]
**G_upstream Reason**: [One sentence]

---

### UPSTREAM PHASE HANDOFF
*(Per §6a. EXECUTION PHASE must open with EXECUTION PHASE ACKNOWLEDGMENT. Blank = §6a violation.)*

**Open CH-IDs for EXECUTION PHASE**:

| CH-ID  | Upstream Status   | Claim (copy)  | Note for Execution Phase                             |
|--------|-------------------|---------------|------------------------------------------------------|
| [CH-00X] | [PARTIAL/OPEN]  | [copy]        | [What execution-phase evidence would address this]   |
| ("None -- all ADDRESSED" if empty) |   |               |                                                      |

**Escalated Upstream Findings**:

| Finding        | S-ID    | Upstream Severity  | Note for Execution Phase                             |
|----------------|---------|--------------------|------------------------------------------------------|
| [finding]      | [S-00X] | [CRITICAL/MAJOR]   | [How execution-phase review should probe this]       |
| ("None" if no CRITICAL/MAJOR) |  |                   |                                                      |

**UPSTREAM PHASE HANDOFF COMPLETE.**

---

### EXECUTION PHASE
*(Scope: S-IDs tagged EXECUTION. Technical readiness: design, implementation, risk.)*

**EXECUTION PHASE ACKNOWLEDGMENT** (§6a -- blank = §6a violation -> G_execution cannot be PASS):

| Item           | From Handoff   | Type              | Disposition                                       |
|----------------|----------------|-------------------|---------------------------------------------------|
| [CH-00X/text]  | Upstream Handoff | [CH-ID/FINDING] | [CARRY-FORWARD / PHASE-N/A (reason) / ESCALATE]  |

**CH-ID Response Table -- EXECUTION** (exactly N rows):

| CH-ID  | Challenge Claim (copy) | Execution Technical Response         | Status                       |
|--------|------------------------|--------------------------------------|------------------------------|
| CH-001 | [copy]                 | [execution response]                 | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]                 | [execution response]                 | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active]       | [execution response]                 | [ADDRESSED / PARTIAL / OPEN] |

**EXECUTION FINDING SURFACE LINKAGE TABLE** (§5a: findings here only):

| Finding                                   | In-Scope Surface (S-ID) | Role Lens | Severity                          |
|-------------------------------------------|-------------------------|-----------|-----------------------------------|
| [FINDING -- design/implementation concern]| [S-00X, phase=EXECUTION]| [lens]    | [CRITICAL / MAJOR / MINOR / ADVISORY] |
| **FINDING TALLY**                         | Total: [N]              | CRITICAL: [n] / MAJOR: [n] | MINOR: [n] / ADVISORY: [n] |

**G_execution Verdict**: [PASS / CONDITIONAL / FAIL]
**G_execution Reason**: [One sentence]

**G_lifecycle = worst(G_upstream, G_execution)**: [PASS / CONDITIONAL / FAIL]

**Null hypothesis status**: [STILL VIABLE / CHALLENGED / OPEN] -- [one sentence]

---

## LIFECYCLE HANDOFF PACKET

*(§6. Covers both UPSTREAM and EXECUTION phases. DOMAIN opens with DOMAIN HANDOFF ACKNOWLEDGMENT.)*

**Open CH-IDs for DOMAIN**:

| CH-ID  | Phase              | Status           | Claim (copy) | Note for Domain                            |
|--------|--------------------|-----------------|--------------|--------------------------------------------|
| [CH-00X] | [UPSTREAM/EXEC] | [PARTIAL/OPEN]  | [copy]       | [What domain evidence would close this]    |
| ("None -- all CH-IDs ADDRESSED" if empty) |  |                 |              |                                            |

**Escalated Findings for DOMAIN**:

| Finding        | S-ID    | Phase       | Severity           | Escalation Note                                |
|----------------|---------|-------------|-------------------|------------------------------------------------|
| [finding]      | [S-00X] | [UP/EXEC]  | [CRITICAL/MAJOR]  | [How domain lens should probe this]            |
| ("None" if no CRITICAL/MAJOR) |  |            |                   |                                                |

**LIFECYCLE HANDOFF PACKET COMPLETE.**

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v2
Received GOpen: [copy] | G_lifecycle: [copy]

**DOMAIN HANDOFF ACKNOWLEDGMENT** (§6 -- blank Disposition = §6 violation):

| Item           | From Packet      | Type              | Disposition                                       |
|----------------|------------------|-------------------|---------------------------------------------------|
| [CH-00X/text]  | Lifecycle Packet | [CH-ID/FINDING]   | [CARRY-FORWARD / DOMAIN-N/A (reason) / ESCALATE] |

**CH-ID Verdict Preview**:

| CH-ID  | Status                       |
|--------|------------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [omit if not active]         |

**CH-ID Response Table** (exactly N rows):

| CH-ID  | Challenge Claim (copy)      | Domain Technical Response    | Status                       |
|--------|-----------------------------|------------------------------|------------------------------|
| CH-001 | [copy]                      | [RESPONSE_1]                 | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]                      | [RESPONSE_2]                 | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active]            | [RESPONSE_3]                 | [ADDRESSED / PARTIAL / OPEN] |

**FINDING SURFACE LINKAGE TABLE** (§5a: findings here only):

| Finding                                      | In-Scope Surface (S-ID) | Role Lens | Severity                          |
|----------------------------------------------|-------------------------|-----------|-----------------------------------|
| [FINDING -- domain/technical concern]        | [S-00X]                 | [lens]    | [CRITICAL / MAJOR / MINOR / ADVISORY] |
| **FINDING TALLY**                            | Total: [N]              | CRITICAL: [n] / MAJOR: [n] | MINOR: [n] / ADVISORY: [n] |

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]   **G_domain Aggregate**: [worst across all DOMAIN sections]

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v2

**CH-ID Cross-Gate Tally**:

| CH-ID  | UPSTREAM Status | EXECUTION Status | DOMAIN Status | Converged? |
|--------|-----------------|------------------|---------------|------------|
| CH-001 | [copy]          | [copy]           | [copy]        | [yes / no] |
| CH-002 | [copy]          | [copy]           | [copy]        | [yes / no] |
| CH-003 | [omit if not active]                                         | [yes / no] |

**CH-ID Final Assessment** (exactly N rows):

| CH-ID  | G_upstream | G_execution | G_domain | Final Status                 | Notes         |
|--------|------------|-------------|----------|------------------------------|---------------|
| CH-001 | [copy]     | [copy]      | [copy]   | [DEFEATED / PARTIAL / HOLDS] | [note]        |
| CH-002 | [copy]     | [copy]      | [copy]   | [DEFEATED / PARTIAL / HOLDS] | [note]        |
| CH-003 | [copy if active]                          | [DEFEATED / PARTIAL / HOLDS] | [note] |

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**GClose Rationale**: [2-3 sentences naming specific tool/process from NULL HYPOTHESIS REGISTER]

---

## GATE VECTOR TABLE

| Gate             | Reviewer        | Verdict                     | Contract Cite             |
|------------------|-----------------|-----------------------------|---------------------------|
| GOpen            | [CHALLENGER]    | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v2   |
| G_upstream       | [LIFECYCLE]     | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v2   |
| G_execution      | [LIFECYCLE]     | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v2   |
| G_lifecycle      | [derived]       | worst(G_upstream, G_exec)   | DISPOSITION_CONTRACT v2   |
| G_domain_agg     | [DOMAIN(S)]     | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v2   |
| GClose           | [CHALLENGER]    | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v2   |

---

## CROSS-ROLE SIGNALS

**Phase convergence** (CH-IDs non-ADDRESSED in both UPSTREAM and EXECUTION):
[CH-00X: description. "None" if none.]

**Cross-role convergence** (CH-IDs non-ADDRESSED in LIFECYCLE and DOMAIN):
[CH-00X: description. "None" if none.]

**Conflicts**: [Incompatible responses across phases or roles. "None" if none.]

**Scope coverage** (uncited S-IDs by phase tag):
[S-00X [phase-tag]: not cited by any phase finding. "None" if all cited.]

**§6 protocol status**: [HANDOFF PACKET acknowledged? §6a UPSTREAM->EXECUTION acknowledged?]

---

## DISPOSITION

**Gate vector**:
  GOpen = [copy] | G_upstream = [copy] | G_execution = [copy]
  G_lifecycle = worst(G_upstream, G_execution) = [copy]
  G_domain_agg = [copy] | GClose = [copy]

**Apply §3 formula**:
```
GClose = FAIL? -> BLOCKED
Any Gi = FAIL? -> BLOCKED
No FAIL, any CONDITIONAL? -> CONDITIONAL
All PASS? -> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]
**Null hypothesis defeat**: [DEFEATED / PARTIALLY DEFEATED / HOLDS]
**Primary driver**: [Gate most responsible]

---

## ACTION ITEM REGISTER

| CH-ID  | Item Description    | Disposition Class | Phase/Role Owner | Resolution Criterion                           |
|--------|---------------------|-------------------|------------------|------------------------------------------------|
| CH-001 | [What must be done] | [BLOCKED/COND/ADV]| [ROLE / PHASE]   | [What must be true to close this item]         |

```

---

## V-03 -- Single Axis: Inertia Framing (Org-Wide INERTIA DEFEAT LEDGER)

**Variation axis**: Inertia framing. The null hypothesis from the NULL HYPOTHESIS REGISTER
travels through the entire review as an org-wide competitor. Each FINDING SURFACE LINKAGE TABLE
gains an INERTIA column: each finding states whether it argues FOR (weakens inertia) or AGAINST
(strengthens inertia) defeating the status quo. BRACKET CLOSING synthesizes an INERTIA DEFEAT
LEDGER showing whether the org collectively defeated the null hypothesis.

**Hypothesis**: In the baseline template, only CHALLENGER frames the null hypothesis. LIFECYCLE
and DOMAIN reviewers implicitly operate against the status quo but never explicitly take a
position on whether their findings defeat it. Adding an INERTIA column converts every finding
into a vote. The INERTIA DEFEAT LEDGER at close is a structural summary that answers the
ultimate question ("did we gather enough evidence to change course?") independently of the gate
chain. Expected excellence signal E-10: INERTIA DEFEAT LEDGER as a structural org-level
synthesis primitive, distinct from the gate chain.

---

```
depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every [BRACKETED_FIELD]. Do not alter, reorder, or omit any pre-printed
heading, label, field, formula, or structural element. If a field cannot be filled, write [N/A -- reason].

**Inertia-framing rule**: The null hypothesis named in the NULL HYPOTHESIS REGISTER is the
org-wide status-quo competitor for this review. Every finding in every FINDING SURFACE LINKAGE
TABLE must include an INERTIA column entry stating: FOR (this finding weakens the case for the
status quo) or AGAINST (this finding strengthens the case for the status quo) or NEUTRAL. A
blank INERTIA cell is a §7 inertia-tracking violation. BRACKET CLOSING synthesizes the org-wide
INERTIA DEFEAT LEDGER from all INERTIA columns.

---

## SCOPE SURFACE REGISTER

| S-ID  | Surface Name                                                                     | Why In Scope      | Primary Lens              |
|-------|----------------------------------------------------------------------------------|-------------------|---------------------------|
| S-001 | [Specific section, interface, or behavioral claim -- not "all sections"]         | [One sentence]    | [LIFECYCLE / DOMAIN / either] |
| S-002 | [Another specific surface]                                                       | [One sentence]    | [LIFECYCLE / DOMAIN / either] |
| S-003 | [Optional]                                                                       | [One sentence]    | [LIFECYCLE / DOMAIN / either] |

---

## NULL HYPOTHESIS REGISTER

| Field                    | Value                                                          |
|--------------------------|----------------------------------------------------------------|
| What teams use today     | [Specific tool, process, or workaround -- not "do nothing"]    |
| Why it works well enough | [One sentence]                                                 |
| Where it breaks down     | [One sentence]                                                 |
| Switching cost           | [HIGH / MEDIUM / LOW]                                          |
| Null hypothesis strength | [HIGH / MEDIUM / LOW]                                          |

This register is the org-wide inertia baseline. All INERTIA columns reference it.

---

======================================================================
DISPOSITION_CONTRACT v1 + §7
[IMMUTABLE BLOCK]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE (copy S-ID and name; row count must equal register):
  1. [S-001: name]    2. [S-002: name]    3. [S-003 if active]
OUT-OF-SCOPE: [SURFACE -- REASON] ("None" if empty)
§1 COMPLETE.

§2 SEVERITY SEMANTICS: HIGH = blocks. MEDIUM = conditions. LOW = advisory.

§2a -- SEVERITY AUDIT CHAIN [IMMUTABLE]
  Severity per finding: CRITICAL | MAJOR | MINOR | ADVISORY
  Section Severity = worst(Severity tags in FINDING TALLY row)
  Gate: CRITICAL->FAIL | MAJOR->CONDITIONAL | MINOR/ADVISORY->PASS | no findings->PASS

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  G = {GOpen, G_lifecycle, G_domain_agg, GClose}
  BLOCKED: GClose=FAIL OR any Gi=FAIL
  CONDITIONAL: no FAIL AND any CONDITIONAL
  READY: all PASS

§4 CONTRACT CITE: Each section opens with "Contract: DISPOSITION_CONTRACT v1 + §7"

§5 -- CH-ID TRACING [IMMUTABLE]
  N = declared in BRACKET OPENING. Every CH-ID table has exactly N rows.
  PASS prohibited with OPEN CH-ID row.

§5a -- TABLE-PRIMACY RULE [IMMUTABLE]
  Findings in FINDING SURFACE LINKAGE TABLE only. Prose finding lists prohibited.
  Section Severity from FINDING TALLY row exclusively.

§6 -- LIFECYCLE HANDOFF PROTOCOL [IMMUTABLE]
  LIFECYCLE HANDOFF PACKET emitted after LIFECYCLE.
  DOMAIN opens with DOMAIN HANDOFF ACKNOWLEDGMENT. Blank Disposition = §6 violation.
  HANDOFF carries: partial/open CH-IDs + CRITICAL/MAJOR lifecycle findings.

§7 -- INERTIA TRACKING [IMMUTABLE]
  The NULL HYPOTHESIS REGISTER names the org-wide status-quo competitor for this review.
  Every FINDING SURFACE LINKAGE TABLE includes an INERTIA column.
  INERTIA cell values: FOR (finding weakens status quo) | AGAINST (strengthens status quo) | NEUTRAL
  A blank INERTIA cell is a §7-inertia-blank violation.
  BRACKET CLOSING synthesizes the INERTIA DEFEAT LEDGER from all INERTIA columns across roles.
  INERTIA DEFEAT LEDGER verdict: DEFEATED (FOR >> AGAINST) | CONTESTED (FOR ~ AGAINST) | HOLDS (AGAINST >> FOR)
  The INERTIA DEFEAT LEDGER verdict is advisory -- it does not override the §3 gate chain.

======================================================================
END DISPOSITION_CONTRACT v1 + §7
======================================================================

---

## ROLE MANIFEST

Read `.craft/roles/`.

| Slot        | Archetype        | Role        | Selection Rationale |
|-------------|------------------|-------------|---------------------|
| CHALLENGER  | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE]      |
| LIFECYCLE   | PM/program       | [ROLE_NAME] | [ONE_SENTENCE]      |
| DOMAIN      | technical/domain | [ROLE_NAME] | [ONE_SENTENCE]      |

Order: BRACKET OPENING -> LIFECYCLE -> LIFECYCLE HANDOFF PACKET ->
  DOMAIN HANDOFF ACKNOWLEDGMENT -> DOMAIN -> BRACKET CLOSING.

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1 + §7

**Null hypothesis** (from NULL HYPOTHESIS REGISTER -- name the specific tool or process):
[One sentence naming specific tool/process. No generic language.]

**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Challenge claims**:

| CH-ID  | Challenge Claim                                                                  | Severity              |
|--------|---------------------------------------------------------------------------------|-----------------------|
| CH-001 | [CLAIM_1]                                                                       | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2]                                                                       | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional]                                                           | [HIGH / MEDIUM / LOW] |

**CH-ID Count declared**: N = [count]
**Verify Question**: [lens.verify]   **Simplify**: [lens.simplify]
**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]   **GOpen Reason**: [One sentence]

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1 + §7
Received GOpen: [copy]

**CH-ID Verdict Preview**:

| CH-ID  | Status                       |
|--------|------------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [omit if not active]         |

**CH-ID Response Table** (exactly N rows):

| CH-ID  | Challenge Claim (copy) | Lifecycle Response           | Status                       |
|--------|------------------------|------------------------------|------------------------------|
| CH-001 | [copy]                 | [RESPONSE_1]                 | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]                 | [RESPONSE_2]                 | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active]       | [RESPONSE_3]                 | [ADDRESSED / PARTIAL / OPEN] |

**FINDING SURFACE LINKAGE TABLE** (§5a: findings here only; §7: INERTIA column required):

| Finding                                   | In-Scope Surface (S-ID) | Role Lens | Severity                          | Inertia                  |
|-------------------------------------------|-------------------------|-----------|-----------------------------------|--------------------------|
| [FINDING_1 -- commitment concern]         | [S-00X]                 | [lens]    | [CRITICAL / MAJOR / MINOR / ADVISORY] | [FOR / AGAINST / NEUTRAL] |
| [FINDING_2]                               | [S-00X]                 | [lens]    | [severity]                        | [FOR / AGAINST / NEUTRAL] |
| **FINDING TALLY**                         | Total: [N]              | CRITICAL: [n] / MAJOR: [n] | MINOR: [n] / ADVISORY: [n] | FOR: [n] / AGAINST: [n] / NEUTRAL: [n] |

Blank In-Scope Surface or Role Lens = §16-cell-violation.
Blank INERTIA cell = §7-inertia-blank violation.
Section Severity from FINDING TALLY row per §2a.

**Lifecycle inertia position**: [Overall: does lifecycle evidence support defeating the status quo?
One sentence naming the specific tool/process from NULL HYPOTHESIS REGISTER.]

**Null hypothesis status**: [STILL VIABLE / CHALLENGED / OPEN] -- [one sentence]
**Verify Question**: [lens.verify]   **Simplify**: [lens.simplify]
**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]   **G_lifecycle Reason**: [One sentence]

---

## LIFECYCLE HANDOFF PACKET

*(§6 -- DOMAIN opens with DOMAIN HANDOFF ACKNOWLEDGMENT. Blank Disposition = §6 violation.)*

**Open CH-IDs for DOMAIN**:

| CH-ID  | Lifecycle Status  | Claim (copy) | Note for Domain                                   |
|--------|-------------------|--------------|---------------------------------------------------|
| [CH-00X] | [PARTIAL/OPEN]  | [copy]       | [What domain evidence would close this]           |
| ("None -- all ADDRESSED" if empty) |   |              |                                                   |

**Escalated Findings for DOMAIN**:

| Finding       | S-ID    | Severity           | Inertia       | Escalation Note                              |
|---------------|---------|--------------------|---------------|----------------------------------------------|
| [finding]     | [S-00X] | [CRITICAL/MAJOR]   | [FOR/AGAINST] | [How domain lens should probe this]          |
| ("None" if no CRITICAL/MAJOR) |  |                   |               |                                              |

**LIFECYCLE HANDOFF PACKET COMPLETE.**

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1 + §7
Received GOpen: [copy] | G_lifecycle: [copy]

**DOMAIN HANDOFF ACKNOWLEDGMENT** (§6 -- blank Disposition = §6 violation):

| Item          | From Packet      | Type              | Disposition                                       |
|---------------|------------------|-------------------|---------------------------------------------------|
| [CH-00X/text] | Lifecycle Packet | [CH-ID/FINDING]   | [CARRY-FORWARD / DOMAIN-N/A (reason) / ESCALATE] |

**CH-ID Verdict Preview**:

| CH-ID  | Status                       |
|--------|------------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [omit if not active]         |

**CH-ID Response Table** (exactly N rows):

| CH-ID  | Challenge Claim (copy)      | Domain Technical Response    | Status                       |
|--------|-----------------------------|------------------------------|------------------------------|
| CH-001 | [copy]                      | [RESPONSE_1]                 | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]                      | [RESPONSE_2]                 | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active]            | [RESPONSE_3]                 | [ADDRESSED / PARTIAL / OPEN] |

**FINDING SURFACE LINKAGE TABLE** (§5a: findings here only; §7: INERTIA column required):

| Finding                                     | In-Scope Surface (S-ID) | Role Lens | Severity                          | Inertia                  |
|---------------------------------------------|-------------------------|-----------|-----------------------------------|--------------------------|
| [FINDING_1 -- domain/technical concern]     | [S-00X]                 | [lens]    | [CRITICAL / MAJOR / MINOR / ADVISORY] | [FOR / AGAINST / NEUTRAL] |
| [FINDING_2]                                 | [S-00X]                 | [lens]    | [severity]                        | [FOR / AGAINST / NEUTRAL] |
| **FINDING TALLY**                           | Total: [N]              | CRITICAL: [n] / MAJOR: [n] | MINOR: [n] / ADVISORY: [n] | FOR: [n] / AGAINST: [n] / NEUTRAL: [n] |

**Domain inertia position**: [Does domain evidence support defeating the status quo? One sentence.]
**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]   **G_domain Aggregate**: [worst across DOMAIN sections]

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1 + §7

**CH-ID Cross-Gate Tally**:

| CH-ID  | LIFECYCLE Status | DOMAIN Status | Converged? |
|--------|------------------|---------------|------------|
| CH-001 | [copy]           | [copy]        | [yes / no] |
| CH-002 | [copy]           | [copy]        | [yes / no] |
| CH-003 | [omit if not active]              | [yes / no] |

**CH-ID Final Assessment** (exactly N rows):

| CH-ID  | G_lifecycle | G_domain | Final Status                 | Notes      |
|--------|-------------|----------|------------------------------|------------|
| CH-001 | [copy]      | [copy]   | [DEFEATED / PARTIAL / HOLDS] | [note]     |
| CH-002 | [copy]      | [copy]   | [DEFEATED / PARTIAL / HOLDS] | [note]     |
| CH-003 | [copy if active]          | [DEFEATED / PARTIAL / HOLDS] | [note] |

**INERTIA DEFEAT LEDGER** (§7 synthesis -- aggregate INERTIA columns across all reviewer sections):

| Role       | FOR count | AGAINST count | NEUTRAL count | Role Inertia Position     |
|------------|-----------|---------------|---------------|---------------------------|
| LIFECYCLE  | [n]       | [n]           | [n]           | [DEFEATING / CONTESTED / HOLDING] |
| DOMAIN     | [n]       | [n]           | [n]           | [DEFEATING / CONTESTED / HOLDING] |
| **TOTAL**  | [sum]     | [sum]         | [sum]         | **[DEFEATED / CONTESTED / HOLDS]** |

**INERTIA DEFEAT VERDICT**: [DEFEATED / CONTESTED / HOLDS]
  DEFEATED: total FOR > 2 * AGAINST -- evidence heavily favors changing course
  CONTESTED: FOR and AGAINST within 2x of each other -- evidence mixed; switching cost is the tiebreaker
  HOLDS: AGAINST > FOR -- evidence does not support replacing [tool/process from Register]

Note: INERTIA DEFEAT VERDICT is advisory. It does not override the §3 gate chain.

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**GClose Rationale**: [2-3 sentences. Reference null hypothesis tool/process from Register.
Cross-reference INERTIA DEFEAT VERDICT: consistent with gate chain? Divergence is signal.]

---

## GATE VECTOR TABLE

| Gate         | Reviewer      | Verdict                     | Contract Cite               |
|--------------|---------------|-----------------------------|-----------------------------|
| GOpen        | [CHALLENGER]  | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 + §7 |
| G_lifecycle  | [LIFECYCLE]   | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 + §7 |
| G_domain_agg | [DOMAIN(S)]   | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 + §7 |
| GClose       | [CHALLENGER]  | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 + §7 |

---

## CROSS-ROLE SIGNALS

**Convergence**: [CH-IDs non-ADDRESSED in both LIFECYCLE and DOMAIN.]
**Conflicts**: [Incompatible responses or inertia positions between roles.]
**Inertia divergence**: [Roles with opposing inertia positions on the same finding -- high signal.]
**Scope coverage**: [Uncited S-IDs. "None" if all cited.]
**§6 protocol status**: [All handoff items acknowledged?]

---

## DISPOSITION

**Gate vector**: GOpen=[_] | G_lifecycle=[_] | G_domain_agg=[_] | GClose=[_]

**Apply §3**:
```
GClose=FAIL -> BLOCKED | any Gi=FAIL -> BLOCKED | any CONDITIONAL -> CONDITIONAL | all PASS -> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]
**Null hypothesis defeat (gate chain)**: [DEFEATED / PARTIALLY DEFEATED / HOLDS]
**Null hypothesis defeat (inertia ledger)**: [DEFEATED / CONTESTED / HOLDS]
**Alignment**: [Do gate chain and inertia ledger agree? If not, describe the divergence.]
**Primary driver**: [Gate most responsible]

---

## ACTION ITEM REGISTER

| CH-ID  | Item Description    | Disposition Class  | Owner Role  | Resolution Criterion                          |
|--------|---------------------|--------------------|-------------|-----------------------------------------------|
| CH-001 | [What must be done] | [BLOCKED/COND/ADV] | [ROLE_NAME] | [What must be true to close this item]        |

```

---

## V-04 -- Combined: V-01 + V-02 (Imperative Prohibitions + Phase Sub-Contracts)

**Variation axis**: V-01 (imperative/mechanical phrasing) + V-02 (UPSTREAM/EXECUTION phase sub-contracts).

**Hypothesis**: Imperative prohibition format applied to phase-level contracts eliminates the
ambiguity introduced by splitting LIFECYCLE into two phases. Each phase contract has its own
numbered prohibition list, making §6a intra-LIFECYCLE phase handoff violations as unambiguous
as §6 inter-role violations.

---

```
depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

MANDATORY: Fill every [BRACKETED_FIELD]. Do not alter, reorder, or omit any pre-printed
heading, label, field, formula, or structural element. Do not add sections between pre-printed
headers. Do not add roles not in the manifest. If a field cannot be filled, write [N/A -- reason].

---

## SCOPE SURFACE REGISTER

PROHIBITED: generic surface descriptions ("all sections", "the full document", "all fields").
VIOLATION TYPE: §1-generic-surface. DETECTED BY: surface name matches a generic phrase.
Tag each surface by phase: UPSTREAM | EXECUTION | DOMAIN | any combination.

| S-ID  | Surface Name                                                | Why In Scope      | Phase Tag                    | Primary Lens              |
|-------|-------------------------------------------------------------|-------------------|------------------------------|---------------------------|
| S-001 | [Specific section, interface, or behavioral claim]          | [One sentence]    | [UPSTREAM / EXECUTION / DOMAIN] | [LIFECYCLE / DOMAIN / either] |
| S-002 | [Another specific surface]                                  | [One sentence]    | [phase tag]                  | [lens]                    |
| S-003 | [Optional]                                                  | [One sentence]    | [phase tag]                  | [lens]                    |

---

## NULL HYPOTHESIS REGISTER

PROHIBITED: generic null hypothesis ("do nothing", "status quo", "the current approach").
VIOLATION TYPE: §9-generic-null. DETECTED BY: null hypothesis text matches a generic phrase.

| Field                    | Value                                                       |
|--------------------------|-------------------------------------------------------------|
| What teams use today     | [Specific tool, process, or workaround]                     |
| Why it works well enough | [One sentence]                                              |
| Where it breaks down     | [One sentence]                                              |
| Switching cost           | [HIGH / MEDIUM / LOW]                                       |
| Null hypothesis strength | [HIGH / MEDIUM / LOW]                                       |

---

======================================================================
DISPOSITION_CONTRACT v2 + prohibitions
[IMMUTABLE BLOCK]
======================================================================

§1 -- SCOPE ENUMERATION
PROHIBITED: finding citing surface not in IN-SCOPE list.
VIOLATION TYPE: §1-scope-expansion. DETECTED BY: finding cites S-ID not in list below.

IN-SCOPE: 1.[S-001] 2.[S-002] 3.[S-003 if active] (row count = register rows)
OUT-OF-SCOPE: [SURFACE -- REASON] ("None" if empty)
§1 COMPLETE.

§2 SEVERITY: HIGH=blocks. MEDIUM=conditions. LOW=advisory.
PROHIBITED: severity redefinition outside §2. VIOLATION TYPE: §2-restatement.

§2a -- SEVERITY AUDIT CHAIN [IMMUTABLE]
PROHIBITED: gate verdict contradicting formula. VIOLATION TYPE: §2a-override.
PROHIBITED: Section Severity derived from prose (not TALLY row). VIOLATION TYPE: §2a-tally-bypass.
  Finding tags: CRITICAL -> FAIL | MAJOR -> CONDITIONAL | MINOR/ADVISORY -> PASS
  Section Severity = worst(tags in FINDING TALLY row). Gate = gate_verdict(Section Severity).

§3 -- DISPOSITION ALGEBRA (phase-extended) [IMMUTABLE]
PROHIBITED: editorial override. VIOLATION TYPE: §3-override.
  G_lifecycle = worst(G_upstream, G_execution)
  G = {GOpen, G_upstream, G_execution, G_lifecycle, G_domain_agg, GClose}
  BLOCKED: GClose=FAIL OR any Gi=FAIL | CONDITIONAL: no FAIL, any CONDITIONAL | READY: all PASS

§4 CONTRACT CITE: "Contract: DISPOSITION_CONTRACT v2 + prohibitions" at each section open.
PROHIBITED: section without cite. VIOLATION TYPE: §4-cite-gap.

§5 CH-ID TRACING: N from BRACKET OPENING. All CH-ID tables = N rows.
PROHIBITED: row count != N. VIOLATION TYPE: §5-count-violation.
PROHIBITED: PASS with OPEN CH-ID row. VIOLATION TYPE: §5-open-block.

§5a TABLE-PRIMACY [IMMUTABLE]
PROHIBITED: prose finding list outside table. VIOLATION TYPE: §5a-prose-finding.
PROHIBITED: finding in prose but absent from FINDING SURFACE LINKAGE TABLE. VIOLATION TYPE: §5a-table-bypass.
PERMITTED: Detail [S-ID]: [prose] after table row for CRITICAL/MAJOR only.
Section Severity from FINDING TALLY row only. No TALLY = §5a-tally-missing violation.

§6 LIFECYCLE HANDOFF [IMMUTABLE]
PROHIBITED: DOMAIN section without DOMAIN HANDOFF ACKNOWLEDGMENT. VIOLATION TYPE: §6-acknowledgment-missing.
PROHIBITED: blank Disposition in ACKNOWLEDGMENT. VIOLATION TYPE: §6-blank-disposition.
PROHIBITED: DOMAIN gate=PASS with §6 violation present. VIOLATION TYPE: §6-pass-with-violation.
Handoff carries: partial/open CH-IDs + CRITICAL/MAJOR lifecycle findings.
Dispositions: CARRY-FORWARD | DOMAIN-N/A (reason required) | ESCALATE (new severity required)

§6a PHASE HANDOFF [IMMUTABLE]
PROHIBITED: EXECUTION PHASE without EXECUTION PHASE ACKNOWLEDGMENT. VIOLATION TYPE: §6a-acknowledgment-missing.
PROHIBITED: blank Phase-Disposition in ACKNOWLEDGMENT. VIOLATION TYPE: §6a-blank-disposition.
PROHIBITED: G_execution=PASS with §6a violation present. VIOLATION TYPE: §6a-pass-with-violation.
Phase handoff carries: partial/open CH-IDs + CRITICAL/MAJOR upstream findings.
Phase dispositions: CARRY-FORWARD | PHASE-N/A (reason required) | ESCALATE (new severity required)

======================================================================
END DISPOSITION_CONTRACT v2 + prohibitions
======================================================================

---

## ROLE MANIFEST

Read `.craft/roles/`. PROHIBITED: inventing roles not in manifest. VIOLATION TYPE: §1-invented-role.

| Slot        | Archetype        | Role        | Selection Rationale |
|-------------|------------------|-------------|---------------------|
| CHALLENGER  | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE]      |
| LIFECYCLE   | PM/program       | [ROLE_NAME] | [ONE_SENTENCE]      |
| DOMAIN      | technical/domain | [ROLE_NAME] | [ONE_SENTENCE]      |

PROHIBITED: DOMAIN section before LIFECYCLE. VIOLATION TYPE: §14-sequence.
Order: BRACKET OPENING -> LIFECYCLE [UPSTREAM -> UPSTREAM HANDOFF -> EXECUTION] ->
  LIFECYCLE HANDOFF PACKET -> DOMAIN HANDOFF ACKNOWLEDGMENT -> DOMAIN -> BRACKET CLOSING.

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v2 + prohibitions

**Null hypothesis** (from NULL HYPOTHESIS REGISTER -- name specific tool/process):
[One sentence. Generic phrasing is a §9-generic-null violation.]

**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Challenge claims**:

| CH-ID  | Challenge Claim | Severity              |
|--------|-----------------|-----------------------|
| CH-001 | [CLAIM_1]       | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2]       | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional] | [HIGH / MEDIUM / LOW] |

**CH-ID Count declared**: N = [count]
**Verify Question**: [lens.verify]   **Simplify**: [lens.simplify]
**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]   **GOpen Reason**: [One sentence]

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v2 + prohibitions

### UPSTREAM PHASE
Scope: S-IDs tagged UPSTREAM. Focus: strategy alignment, resource confirmation, feasibility.

**CH-ID Verdict Preview**:

| CH-ID  | Status                       |
|--------|------------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [omit if not active]         |

**CH-ID Response Table -- UPSTREAM** (exactly N rows):

| CH-ID  | Claim (copy) | Upstream Response | Status                       |
|--------|--------------|-------------------|------------------------------|
| CH-001 | [copy]       | [response]        | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]       | [response]        | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [response]    | [ADDRESSED / PARTIAL / OPEN] |

**UPSTREAM FINDING SURFACE LINKAGE TABLE**:
PROHIBITED: finding outside this table. VIOLATION TYPE: §5a-prose-finding.
PROHIBITED: blank In-Scope Surface or Role Lens. VIOLATION TYPE: §16-cell-violation.

| Finding                             | In-Scope Surface (S-ID)   | Role Lens | Severity                          |
|-------------------------------------|---------------------------|-----------|-----------------------------------|
| [FINDING -- strategy/resource]      | [S-00X, phase=UPSTREAM]   | [lens]    | [CRITICAL / MAJOR / MINOR / ADVISORY] |
| **FINDING TALLY**                   | Total: [N]                | CRITICAL: [n] / MAJOR: [n] | MINOR: [n] / ADVISORY: [n] |

Section Severity from TALLY. PROHIBITED: editorial derivation. G_upstream per §2a.
**G_upstream**: [PASS / CONDITIONAL / FAIL]   **G_upstream Reason**: [One sentence]

---

### UPSTREAM PHASE HANDOFF
*(§6a -- EXECUTION PHASE opens with ACKNOWLEDGMENT. Blank Phase-Disposition = §6a-blank-disposition.)*

**Open CH-IDs for EXECUTION PHASE**:

| CH-ID  | Status          | Claim (copy) | Note for Execution Phase                      |
|--------|-----------------|--------------|-----------------------------------------------|
| [CH-00X] | [PARTIAL/OPEN] | [copy]      | [Evidence needed from execution phase]        |
| ("None -- all ADDRESSED" if empty) |  |              |                                               |

**Escalated Upstream Findings**:

| Finding   | S-ID    | Severity         | Note for Execution Phase                      |
|-----------|---------|------------------|-----------------------------------------------|
| [finding] | [S-00X] | [CRITICAL/MAJOR] | [How execution phase should probe this]       |
| ("None" if no CRITICAL/MAJOR) |  |                 |                                               |

**UPSTREAM PHASE HANDOFF COMPLETE.**

---

### EXECUTION PHASE
Scope: S-IDs tagged EXECUTION. Focus: design, implementation, technical risk.

**EXECUTION PHASE ACKNOWLEDGMENT** (§6a -- blank = §6a-blank-disposition violation -> G_execution cannot be PASS):

| Item          | From Phase Handoff | Type              | Phase-Disposition                                 |
|---------------|--------------------|-------------------|---------------------------------------------------|
| [CH-00X/text] | Upstream Handoff   | [CH-ID/FINDING]   | [CARRY-FORWARD / PHASE-N/A (reason) / ESCALATE]  |

**CH-ID Response Table -- EXECUTION** (exactly N rows):

| CH-ID  | Claim (copy) | Execution Response | Status                       |
|--------|--------------|--------------------|------------------------------|
| CH-001 | [copy]       | [response]         | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]       | [response]         | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [response]     | [ADDRESSED / PARTIAL / OPEN] |

**EXECUTION FINDING SURFACE LINKAGE TABLE**:
PROHIBITED: finding outside table. PROHIBITED: blank In-Scope Surface or Role Lens.

| Finding                                  | In-Scope Surface (S-ID)    | Role Lens | Severity                          |
|------------------------------------------|----------------------------|-----------|-----------------------------------|
| [FINDING -- design/impl concern]         | [S-00X, phase=EXECUTION]   | [lens]    | [CRITICAL / MAJOR / MINOR / ADVISORY] |
| **FINDING TALLY**                        | Total: [N]                 | CRITICAL: [n] / MAJOR: [n] | MINOR: [n] / ADVISORY: [n] |

**G_execution**: [PASS / CONDITIONAL / FAIL]   **G_execution Reason**: [One sentence]
**G_lifecycle = worst(G_upstream, G_execution)**: [PASS / CONDITIONAL / FAIL]
**Null hypothesis status**: [STILL VIABLE / CHALLENGED / OPEN] -- [one sentence]

---

## LIFECYCLE HANDOFF PACKET

*(§6 -- DOMAIN opens with DOMAIN HANDOFF ACKNOWLEDGMENT. Blank Disposition = §6-blank-disposition.)*

**Open CH-IDs for DOMAIN**:

| CH-ID  | Phase       | Status          | Claim (copy) | Note for Domain                                |
|--------|-------------|-----------------|--------------|------------------------------------------------|
| [CH-00X] | [UP/EXEC]  | [PARTIAL/OPEN]  | [copy]       | [Evidence needed from domain review]           |
| ("None -- all ADDRESSED" if empty) |   |                 |              |                                                |

**Escalated Findings for DOMAIN**:

| Finding   | S-ID    | Phase     | Severity         | Escalation Note                               |
|-----------|---------|-----------|------------------|-----------------------------------------------|
| [finding] | [S-00X] | [UP/EXEC] | [CRITICAL/MAJOR] | [How domain should probe this]                |
| ("None" if no CRITICAL/MAJOR) |  |          |                  |                                               |

**LIFECYCLE HANDOFF PACKET COMPLETE.**

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v2 + prohibitions
Received GOpen: [copy] | G_lifecycle: [copy]

**DOMAIN HANDOFF ACKNOWLEDGMENT** (§6 -- blank Disposition = §6-blank-disposition):

| Item          | From Packet     | Type              | Disposition                                       |
|---------------|-----------------|-------------------|---------------------------------------------------|
| [CH-00X/text] | Lifecycle Packet | [CH-ID/FINDING]  | [CARRY-FORWARD / DOMAIN-N/A (reason) / ESCALATE] |

**CH-ID Verdict Preview**:

| CH-ID  | Status                       |
|--------|------------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [omit if not active]         |

**CH-ID Response Table** (exactly N rows):

| CH-ID  | Claim (copy)        | Domain Response  | Status                       |
|--------|---------------------|------------------|------------------------------|
| CH-001 | [copy]              | [RESPONSE_1]     | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]              | [RESPONSE_2]     | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active]    | [RESPONSE_3]     | [ADDRESSED / PARTIAL / OPEN] |

**DOMAIN FINDING SURFACE LINKAGE TABLE**:
PROHIBITED: finding outside table. PROHIBITED: blank In-Scope Surface or Role Lens.

| Finding                               | In-Scope Surface (S-ID) | Role Lens | Severity                          |
|---------------------------------------|-------------------------|-----------|-----------------------------------|
| [FINDING -- domain/technical concern] | [S-00X]                 | [lens]    | [CRITICAL / MAJOR / MINOR / ADVISORY] |
| **FINDING TALLY**                     | Total: [N]              | CRITICAL: [n] / MAJOR: [n] | MINOR: [n] / ADVISORY: [n] |

**G_domain**: [PASS / CONDITIONAL / FAIL]   **G_domain Aggregate**: [worst across all DOMAIN]

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v2 + prohibitions

**CH-ID Cross-Gate Tally**:

| CH-ID  | UPSTREAM | EXECUTION | DOMAIN | Converged? |
|--------|----------|-----------|--------|------------|
| CH-001 | [copy]   | [copy]    | [copy] | [yes / no] |
| CH-002 | [copy]   | [copy]    | [copy] | [yes / no] |
| CH-003 | [omit if not active]           | [yes / no] |

**CH-ID Final Assessment** (exactly N rows):
PROHIBITED: row count != N. VIOLATION TYPE: §5-count-violation.

| CH-ID  | G_upstream | G_execution | G_domain | Final Status                 | Notes  |
|--------|------------|-------------|----------|------------------------------|--------|
| CH-001 | [copy]     | [copy]      | [copy]   | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-002 | [copy]     | [copy]      | [copy]   | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-003 | [if active]                          | [DEFEATED / PARTIAL / HOLDS] | [note] |

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**GClose Rationale**: [2-3 sentences naming specific tool/process from NULL HYPOTHESIS REGISTER]

---

## GATE VECTOR TABLE

| Gate           | Reviewer      | Verdict                     | Contract Cite                    |
|----------------|---------------|-----------------------------|----------------------------------|
| GOpen          | [CHALLENGER]  | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v2 + prohibitions |
| G_upstream     | [LIFECYCLE]   | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v2 + prohibitions |
| G_execution    | [LIFECYCLE]   | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v2 + prohibitions |
| G_lifecycle    | [derived]     | worst(G_up, G_exec)         | DISPOSITION_CONTRACT v2 + prohibitions |
| G_domain_agg   | [DOMAIN(S)]   | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v2 + prohibitions |
| GClose         | [CHALLENGER]  | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v2 + prohibitions |

---

## CROSS-ROLE SIGNALS

**Phase convergence**: [CH-IDs non-ADDRESSED in both UPSTREAM and EXECUTION.]
**Cross-role convergence**: [CH-IDs non-ADDRESSED in LIFECYCLE phases and DOMAIN.]
**Conflicts**: [Incompatible responses across phases or roles.]
**Scope coverage**: [Uncited S-IDs by phase tag. "None" if all cited.]
**§6 status**: [LIFECYCLE->DOMAIN handoff acknowledged?]
**§6a status**: [UPSTREAM->EXECUTION phase handoff acknowledged?]

---

## DISPOSITION

**Gate vector**: GOpen=[_] G_upstream=[_] G_execution=[_] G_lifecycle=[_] G_domain_agg=[_] GClose=[_]

```
G_lifecycle = worst(G_upstream, G_execution) = [_]
GClose=FAIL -> BLOCKED | any Gi=FAIL -> BLOCKED | any CONDITIONAL -> CONDITIONAL | all PASS -> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]
**Null hypothesis defeat**: [DEFEATED / PARTIALLY DEFEATED / HOLDS]
**Primary driver**: [Gate most responsible]

---

## ACTION ITEM REGISTER

| CH-ID  | Item Description    | Disposition  | Phase/Role Owner | Resolution Criterion                    |
|--------|---------------------|--------------|------------------|-----------------------------------------|
| CH-001 | [What must be done] | [B/COND/ADV] | [ROLE / PHASE]   | [What must be true to close this item]  |

```

---

## V-05 -- Combined: V-01 + V-02 + V-03 (Full Integration)

**Variation axis**: Full integration -- V-01 (imperative prohibitions) + V-02 (phase sub-contracts) + V-03 (org-wide inertia framing).

**Hypothesis**: The three axes are complementary without interference. Prohibition format makes all
phase and inertia tracking rules binary. Phase sub-contracts extend the structural handoff guarantee
intra-LIFECYCLE. Org-wide inertia framing converts the review from a gate-chain audit to an
evidence campaign for defeating the status quo. The combination may surface E-10 (inertia column
as vote aggregator) alongside E-11 (intra-phase handoff as structural primitive) in one pass.

---

```
depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

MANDATORY: Fill every [BRACKETED_FIELD]. Do not alter, reorder, or omit any pre-printed
heading, label, field, formula, or structural element. Do not add sections between pre-printed
headers. Do not add roles not in the manifest. If a field cannot be filled, write [N/A -- reason].

**Inertia-framing rule**: The null hypothesis from the NULL HYPOTHESIS REGISTER is the org-wide
status-quo competitor. Every FINDING SURFACE LINKAGE TABLE includes an INERTIA column. Values:
FOR (weakens status quo) | AGAINST (strengthens status quo) | NEUTRAL. Blank = §7 violation.
BRACKET CLOSING synthesizes the INERTIA DEFEAT LEDGER from all INERTIA columns across all phases
and roles.

---

## SCOPE SURFACE REGISTER

PROHIBITED: generic descriptions. VIOLATION TYPE: §1-generic-surface.
Tag each surface by phase: UPSTREAM | EXECUTION | DOMAIN | any combination.

| S-ID  | Surface Name                                          | Why In Scope   | Phase Tag                    | Primary Lens              |
|-------|-------------------------------------------------------|----------------|------------------------------|---------------------------|
| S-001 | [Specific section, interface, or behavioral claim]    | [One sentence] | [UPSTREAM / EXECUTION / DOMAIN] | [LIFECYCLE / DOMAIN / either] |
| S-002 | [Another specific surface]                            | [One sentence] | [phase tag]                  | [lens]                    |
| S-003 | [Optional]                                            | [One sentence] | [phase tag]                  | [lens]                    |

---

## NULL HYPOTHESIS REGISTER

PROHIBITED: generic null hypothesis ("do nothing", "status quo").
VIOLATION TYPE: §9-generic-null. This register is the org-wide inertia baseline.

| Field                    | Value                                                       |
|--------------------------|-------------------------------------------------------------|
| What teams use today     | [Specific tool, process, or workaround]                     |
| Why it works well enough | [One sentence]                                              |
| Where it breaks down     | [One sentence]                                              |
| Switching cost           | [HIGH / MEDIUM / LOW]                                       |
| Null hypothesis strength | [HIGH / MEDIUM / LOW]                                       |

---

======================================================================
DISPOSITION_CONTRACT v3 (phase-extended + prohibitions + inertia)
[IMMUTABLE BLOCK]
======================================================================

§1 SCOPE: IN-SCOPE: 1.[S-001] 2.[S-002] 3.[S-003 if active] (row count = register).
OUT-OF-SCOPE: [SURFACE -- REASON]. §1 COMPLETE.
PROHIBITED: finding citing unlisted S-ID. VIOLATION TYPE: §1-scope-expansion.

§2 SEVERITY: HIGH=blocks. MEDIUM=conditions. LOW=advisory.
PROHIBITED: redefinition outside §2. VIOLATION TYPE: §2-restatement.

§2a SEVERITY AUDIT CHAIN [IMMUTABLE]
PROHIBITED: gate contradicting formula. VIOLATION TYPE: §2a-override.
PROHIBITED: Section Severity from prose. VIOLATION TYPE: §2a-tally-bypass.
  Tags: CRITICAL->FAIL | MAJOR->CONDITIONAL | MINOR/ADVISORY->PASS
  Section Severity = worst(FINDING TALLY row). Gate = gate_verdict(Section Severity).

§3 DISPOSITION ALGEBRA (phase-extended) [IMMUTABLE]
PROHIBITED: editorial override. VIOLATION TYPE: §3-override.
  G_lifecycle = worst(G_upstream, G_execution)
  G = {GOpen, G_upstream, G_execution, G_lifecycle, G_domain_agg, GClose}
  BLOCKED: GClose=FAIL OR any Gi=FAIL | CONDITIONAL: no FAIL, any CONDITIONAL | READY: all PASS

§4 CONTRACT CITE: "Contract: DISPOSITION_CONTRACT v3" at each section and phase open.
PROHIBITED: section without cite. VIOLATION TYPE: §4-cite-gap.

§5 CH-ID TRACING: N from BRACKET OPENING. All tables = N rows.
PROHIBITED: row count != N. VIOLATION TYPE: §5-count-violation.
PROHIBITED: PASS with OPEN CH-ID. VIOLATION TYPE: §5-open-block.

§5a TABLE-PRIMACY [IMMUTABLE]
PROHIBITED: prose finding list. VIOLATION TYPE: §5a-prose-finding.
PROHIBITED: finding in prose absent from table. VIOLATION TYPE: §5a-table-bypass.
Section Severity from FINDING TALLY row only. No TALLY = §5a-tally-missing violation.
PERMITTED: Detail [S-ID]: [prose] after CRITICAL/MAJOR row only, if table row exists.

§6 LIFECYCLE HANDOFF [IMMUTABLE]
PROHIBITED: DOMAIN without DOMAIN HANDOFF ACKNOWLEDGMENT. VIOLATION TYPE: §6-acknowledgment-missing.
PROHIBITED: blank Disposition in ACKNOWLEDGMENT. VIOLATION TYPE: §6-blank-disposition.
PROHIBITED: DOMAIN gate=PASS with §6 violation. VIOLATION TYPE: §6-pass-with-violation.
Carries: partial/open CH-IDs + CRITICAL/MAJOR lifecycle findings.
Dispositions: CARRY-FORWARD | DOMAIN-N/A (reason required) | ESCALATE (severity required)

§6a PHASE HANDOFF [IMMUTABLE]
PROHIBITED: EXECUTION PHASE without EXECUTION PHASE ACKNOWLEDGMENT. VIOLATION TYPE: §6a-acknowledgment-missing.
PROHIBITED: blank Phase-Disposition in ACKNOWLEDGMENT. VIOLATION TYPE: §6a-blank-disposition.
PROHIBITED: G_execution=PASS with §6a violation. VIOLATION TYPE: §6a-pass-with-violation.
Carries: partial/open upstream CH-IDs + CRITICAL/MAJOR upstream findings.
Phase dispositions: CARRY-FORWARD | PHASE-N/A (reason required) | ESCALATE (severity required)

§7 INERTIA TRACKING [IMMUTABLE]
PROHIBITED: FINDING SURFACE LINKAGE TABLE without INERTIA column. VIOLATION TYPE: §7-column-missing.
PROHIBITED: blank INERTIA cell. VIOLATION TYPE: §7-inertia-blank.
Values: FOR | AGAINST | NEUTRAL.
BRACKET CLOSING synthesizes INERTIA DEFEAT LEDGER across all phases and roles.
Ledger verdict: DEFEATED (FOR > 2*AGAINST) | CONTESTED (within 2x) | HOLDS (AGAINST > FOR)
Inertia verdict is advisory; does not override §3 gate chain.

======================================================================
END DISPOSITION_CONTRACT v3
======================================================================

---

## ROLE MANIFEST

Read `.craft/roles/`. PROHIBITED: inventing roles. VIOLATION TYPE: §1-invented-role.

| Slot        | Archetype        | Role        | Selection Rationale |
|-------------|------------------|-------------|---------------------|
| CHALLENGER  | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE]      |
| LIFECYCLE   | PM/program       | [ROLE_NAME] | [ONE_SENTENCE]      |
| DOMAIN      | technical/domain | [ROLE_NAME] | [ONE_SENTENCE]      |

PROHIBITED: DOMAIN before LIFECYCLE. VIOLATION TYPE: §14-sequence.
Order: BRACKET OPENING -> LIFECYCLE [UPSTREAM -> UPSTREAM HANDOFF -> EXECUTION] ->
  LIFECYCLE HANDOFF PACKET -> DOMAIN HANDOFF ACKNOWLEDGMENT -> DOMAIN -> BRACKET CLOSING.

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v3

**Null hypothesis** (from NULL HYPOTHESIS REGISTER -- name specific tool/process):
[One sentence. Generic = §9-generic-null violation.]
**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Challenge claims**:

| CH-ID  | Challenge Claim | Severity              |
|--------|-----------------|-----------------------|
| CH-001 | [CLAIM_1]       | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2]       | [HIGH / MEDIUM / LOW] |
| CH-003 | [optional]      | [HIGH / MEDIUM / LOW] |

**CH-ID Count declared**: N = [count]
**Verify Question**: [lens.verify]   **Simplify**: [lens.simplify]
**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]   **GOpen Reason**: [One sentence]

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v3

### UPSTREAM PHASE
Scope: S-IDs tagged UPSTREAM.

**CH-ID Verdict Preview**:

| CH-ID  | Status                       |
|--------|------------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [omit if not active]         |

**CH-ID Response Table -- UPSTREAM** (exactly N rows):

| CH-ID  | Claim (copy) | Upstream Response | Status                       |
|--------|--------------|-------------------|------------------------------|
| CH-001 | [copy]       | [response]        | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]       | [response]        | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [response]    | [ADDRESSED / PARTIAL / OPEN] |

**UPSTREAM FINDING SURFACE LINKAGE TABLE**:
PROHIBITED: finding outside table (§5a). PROHIBITED: blank In-Scope Surface or Role Lens (§16).
PROHIBITED: blank INERTIA cell (§7).

| Finding                         | In-Scope Surface (S-ID)   | Role Lens | Severity                          | Inertia                   |
|---------------------------------|---------------------------|-----------|-----------------------------------|---------------------------|
| [FINDING -- strategy/resource]  | [S-00X, phase=UPSTREAM]   | [lens]    | [CRITICAL / MAJOR / MINOR / ADVISORY] | [FOR / AGAINST / NEUTRAL] |
| **FINDING TALLY**               | Total: [N]                | CRITICAL: [n] / MAJOR: [n] | MINOR: [n] / ADVISORY: [n] | FOR: [n] / AGAINST: [n] / NEUTRAL: [n] |

Section Severity from TALLY. G_upstream per §2a.
**G_upstream**: [PASS / CONDITIONAL / FAIL]   **G_upstream Reason**: [One sentence]

---

### UPSTREAM PHASE HANDOFF
*(§6a -- EXECUTION opens with ACKNOWLEDGMENT. Blank Phase-Disposition = §6a-blank-disposition.)*

**Open CH-IDs for EXECUTION PHASE**:

| CH-ID  | Status          | Claim (copy) | Note for Execution Phase           |
|--------|-----------------|--------------|-------------------------------------|
| [CH-00X] | [PARTIAL/OPEN] | [copy]      | [Evidence needed from execution]   |
| ("None -- all ADDRESSED") |   |              |                                     |

**Escalated Upstream Findings**:

| Finding   | S-ID    | Severity         | Inertia       | Note for Execution Phase              |
|-----------|---------|------------------|---------------|---------------------------------------|
| [finding] | [S-00X] | [CRITICAL/MAJOR] | [FOR/AGAINST] | [How execution phase should probe]    |
| ("None") |  |                   |               |                                       |

**UPSTREAM PHASE HANDOFF COMPLETE.**

---

### EXECUTION PHASE
Scope: S-IDs tagged EXECUTION.

**EXECUTION PHASE ACKNOWLEDGMENT** (§6a -- blank = §6a-blank-disposition -> G_execution cannot be PASS):

| Item          | From Handoff  | Type              | Phase-Disposition                                 |
|---------------|---------------|-------------------|---------------------------------------------------|
| [CH-00X/text] | Upstream      | [CH-ID/FINDING]   | [CARRY-FORWARD / PHASE-N/A (reason) / ESCALATE]  |

**CH-ID Response Table -- EXECUTION** (exactly N rows):

| CH-ID  | Claim (copy)     | Execution Response | Status                       |
|--------|------------------|--------------------|------------------------------|
| CH-001 | [copy]           | [response]         | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]           | [response]         | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [response]         | [ADDRESSED / PARTIAL / OPEN] |

**EXECUTION FINDING SURFACE LINKAGE TABLE**:
PROHIBITED: finding outside table. PROHIBITED: blank In-Scope Surface, Role Lens, or INERTIA.

| Finding                               | In-Scope Surface (S-ID)    | Role Lens | Severity                          | Inertia                   |
|---------------------------------------|----------------------------|-----------|-----------------------------------|---------------------------|
| [FINDING -- design/impl concern]      | [S-00X, phase=EXECUTION]   | [lens]    | [CRITICAL / MAJOR / MINOR / ADVISORY] | [FOR / AGAINST / NEUTRAL] |
| **FINDING TALLY**                     | Total: [N]                 | CRITICAL: [n] / MAJOR: [n] | MINOR: [n] / ADVISORY: [n] | FOR: [n] / AGAINST: [n] / NEUTRAL: [n] |

**G_execution**: [PASS / CONDITIONAL / FAIL]   **G_execution Reason**: [One sentence]
**G_lifecycle = worst(G_upstream, G_execution)**: [PASS / CONDITIONAL / FAIL]
**Lifecycle inertia position**: [Does lifecycle evidence support defeating the status quo? One sentence.]
**Null hypothesis status**: [STILL VIABLE / CHALLENGED / OPEN] -- [one sentence]

---

## LIFECYCLE HANDOFF PACKET

*(§6 -- DOMAIN opens with DOMAIN HANDOFF ACKNOWLEDGMENT. Blank Disposition = §6-blank-disposition.)*

**Open CH-IDs for DOMAIN**:

| CH-ID  | Phase       | Status          | Claim (copy) | Note for Domain                          |
|--------|-------------|-----------------|--------------|------------------------------------------|
| [CH-00X] | [UP/EXEC]  | [PARTIAL/OPEN]  | [copy]       | [Evidence needed from domain review]     |
| ("None -- all ADDRESSED") |   |                 |              |                                          |

**Escalated Findings for DOMAIN**:

| Finding   | S-ID    | Phase     | Severity         | Inertia       | Escalation Note                      |
|-----------|---------|-----------|------------------|---------------|--------------------------------------|
| [finding] | [S-00X] | [UP/EXEC] | [CRITICAL/MAJOR] | [FOR/AGAINST] | [How domain should probe this]       |
| ("None") |  |           |                  |               |                                      |

**LIFECYCLE HANDOFF PACKET COMPLETE.**

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v3
Received GOpen: [copy] | G_lifecycle: [copy]

**DOMAIN HANDOFF ACKNOWLEDGMENT** (§6 -- blank Disposition = §6-blank-disposition):

| Item          | From Packet     | Type              | Disposition                                       |
|---------------|-----------------|-------------------|---------------------------------------------------|
| [CH-00X/text] | Lifecycle Packet | [CH-ID/FINDING]  | [CARRY-FORWARD / DOMAIN-N/A (reason) / ESCALATE] |

**CH-ID Verdict Preview**:

| CH-ID  | Status                       |
|--------|------------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [omit if not active]         |

**CH-ID Response Table** (exactly N rows):

| CH-ID  | Claim (copy)     | Domain Response  | Status                       |
|--------|------------------|------------------|------------------------------|
| CH-001 | [copy]           | [RESPONSE_1]     | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]           | [RESPONSE_2]     | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3]     | [ADDRESSED / PARTIAL / OPEN] |

**DOMAIN FINDING SURFACE LINKAGE TABLE**:
PROHIBITED: finding outside table. PROHIBITED: blank In-Scope Surface, Role Lens, or INERTIA.

| Finding                               | In-Scope Surface (S-ID) | Role Lens | Severity                          | Inertia                   |
|---------------------------------------|-------------------------|-----------|-----------------------------------|---------------------------|
| [FINDING -- domain/technical concern] | [S-00X]                 | [lens]    | [CRITICAL / MAJOR / MINOR / ADVISORY] | [FOR / AGAINST / NEUTRAL] |
| [FINDING_2]                           | [S-00X]                 | [lens]    | [severity]                        | [FOR / AGAINST / NEUTRAL] |
| **FINDING TALLY**                     | Total: [N]              | CRITICAL: [n] / MAJOR: [n] | MINOR: [n] / ADVISORY: [n] | FOR: [n] / AGAINST: [n] / NEUTRAL: [n] |

**Domain inertia position**: [Does domain evidence support defeating the status quo? One sentence.]
**G_domain**: [PASS / CONDITIONAL / FAIL]   **G_domain Aggregate**: [worst across all DOMAIN]

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v3

**CH-ID Cross-Gate Tally**:

| CH-ID  | UPSTREAM | EXECUTION | DOMAIN | Converged? |
|--------|----------|-----------|--------|------------|
| CH-001 | [copy]   | [copy]    | [copy] | [yes / no] |
| CH-002 | [copy]   | [copy]    | [copy] | [yes / no] |
| CH-003 | [omit if not active]           | [yes / no] |

**CH-ID Final Assessment** (exactly N rows):

| CH-ID  | G_upstream | G_execution | G_domain | Final Status                 | Notes  |
|--------|------------|-------------|----------|------------------------------|--------|
| CH-001 | [copy]     | [copy]      | [copy]   | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-002 | [copy]     | [copy]      | [copy]   | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-003 | [if active]                          | [DEFEATED / PARTIAL / HOLDS] | [note] |

**INERTIA DEFEAT LEDGER** (§7 synthesis -- aggregate all INERTIA columns across phases and roles):

| Phase/Role  | FOR | AGAINST | NEUTRAL | Position                          |
|-------------|-----|---------|---------|-----------------------------------|
| UPSTREAM    | [n] | [n]     | [n]     | [DEFEATING / CONTESTED / HOLDING] |
| EXECUTION   | [n] | [n]     | [n]     | [DEFEATING / CONTESTED / HOLDING] |
| DOMAIN      | [n] | [n]     | [n]     | [DEFEATING / CONTESTED / HOLDING] |
| **TOTAL**   | [sum] | [sum] | [sum]   | **[DEFEATED / CONTESTED / HOLDS]** |

Ledger verdict: DEFEATED (FOR > 2*AGAINST) | CONTESTED (within 2x) | HOLDS (AGAINST > FOR). Advisory only.

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**GClose Rationale**: [2-3 sentences naming specific tool/process from NULL HYPOTHESIS REGISTER.
Cross-reference INERTIA DEFEAT LEDGER: does it align with gate chain? Divergence = signal.]

---

## GATE VECTOR TABLE

| Gate           | Reviewer      | Verdict                     | Contract Cite           |
|----------------|---------------|-----------------------------|-------------------------|
| GOpen          | [CHALLENGER]  | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v3 |
| G_upstream     | [LIFECYCLE]   | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v3 |
| G_execution    | [LIFECYCLE]   | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v3 |
| G_lifecycle    | [derived]     | worst(G_up, G_exec)         | DISPOSITION_CONTRACT v3 |
| G_domain_agg   | [DOMAIN(S)]   | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v3 |
| GClose         | [CHALLENGER]  | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v3 |

---

## CROSS-ROLE SIGNALS

**Phase convergence**: [CH-IDs non-ADDRESSED in both UPSTREAM and EXECUTION.]
**Cross-role convergence**: [CH-IDs non-ADDRESSED in LIFECYCLE and DOMAIN.]
**Inertia divergence**: [Phases/roles with opposing FOR/AGAINST on the same finding.]
**Conflicts**: [Incompatible responses across phases or roles.]
**Scope coverage**: [Uncited S-IDs by phase tag. "None" if all cited.]
**§6 status**: [LIFECYCLE->DOMAIN handoff acknowledged?]
**§6a status**: [UPSTREAM->EXECUTION handoff acknowledged?]
**§7 status**: [INERTIA DEFEAT LEDGER tallied? Any §7 violations?]

---

## DISPOSITION

**Gate vector**:
  GOpen=[_] G_upstream=[_] G_execution=[_] G_lifecycle=[_] G_domain_agg=[_] GClose=[_]

**Apply §3**:
```
G_lifecycle = worst(G_upstream, G_execution) = [_]
GClose=FAIL -> BLOCKED | any Gi=FAIL -> BLOCKED | any CONDITIONAL -> CONDITIONAL | all PASS -> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]
**Null hypothesis defeat (gate chain)**: [DEFEATED / PARTIALLY DEFEATED / HOLDS]
**Null hypothesis defeat (inertia ledger)**: [DEFEATED / CONTESTED / HOLDS]
**Alignment**: [Gate chain and inertia ledger agree? If not -- describe the divergence and which to trust.]
**Primary driver**: [Gate most responsible for this disposition]
**Conditions** (CONDITIONAL only): [Condition from first CONDITIONAL gate]
**Blocker** (BLOCKED only): [Finding from the FAIL gate]

---

## ACTION ITEM REGISTER

| CH-ID  | Item Description    | Disposition  | Phase/Role Owner | Resolution Criterion                        |
|--------|---------------------|--------------|------------------|---------------------------------------------|
| CH-001 | [What must be done] | [B/COND/ADV] | [ROLE / PHASE]   | [What must be true to close this item]      |

```
