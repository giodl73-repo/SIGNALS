---
skill: quest-golden
skill_target: org-review
date: 2026-03-17
rounds: 20
rubric_final: org-review-rubric-v11-2026-03-16.md
score: 225
status: GOLDEN
---

# org-review -- Golden Prompt (V-05 R20, rubric v11)

**Score**: 225/225 predicted
**Variation**: V-05 -- C-33 + C-34 + C-35 three-axis
**Source**: `crew-review-variate-R20-2026-03-17.md`

---

## What Made It Golden

**1. Three orthogonal chain-of-custody protocols, not behavioral text**
V-01 relied on a single APPLICABILITY INHERITANCE PROTOCOL (C-33). V-05 adds two more independent structural locks: scope-declaration domain annotation (§9) for C-34 and two-phase NH table construction (§3) for C-35. Each protocol governs a distinct pipeline stage (§11 = Applicability at step 10, §9 = domain source at step 1, §3 = NH table at step 5). No protocol touches the others; combining all three produces no interaction conflicts.

**2. Immutable Phase 1 / Phase 2 split in the NH table**
Prior variants described a NH DIMENSION COMPARISON TABLE but allowed dimensions to be defined during or after scoring. V-05 splits construction into Phase 1 (DIMENSION REGISTRATION -- names, measurement basis, scale, committed before any scores) and Phase 2 (VALUE ASSIGNMENT -- fills A/B/C). Phase 1 is immutable once Phase 2 begins. This closes the back-fill failure mode (C-35): prose testimony cannot retroactively reshape what was measured to produce a desired g_null.

**3. Domain source anchored at declaration time, not at finding time**
V-05's §9 requires SCOPE DECLARATION (step 1) to carry a `| Surface | Domain | ... |` tag for every IN-SCOPE surface. The DOMAIN COVERAGE GAP-CHECK (step 11) reads its input set exclusively from that committed table. Post-review domain inference is prohibited as a gap-check source. The UNDECLARED-DOMAIN flag handles findings that surface new domains -- they are surfaced in CROSS-ROLE SIGNALS but cannot silently expand the gap-check domain set. This closes the domain-drift failure mode (C-34).

**4. Named alert syntax for every deviation case**
Each chain-of-custody protocol names its own deviation alert: `INHERITANCE-DEVIATION-ALERT` (§11) for silent Applicability recalculation, `NH-CONSTRUCTION-DEVIATION` (§3) for Phase 1 revision requests after Phase 2 begins, `UNDECLARED-DOMAIN` (§9) for findings-derived domains. Deviation alerts are flagged in CROSS-ROLE SIGNALS (step 15) and remain advisory unless BRACKET CLOSING invokes OVERRIDE INVOKED: YES. Named syntax prevents silent failure.

**5. Section order contract encodes protocol dependencies**
§8 ORDER CONTRACT names which step commits each protocol input: step 1 commits domain tags (§9), step 2 commits Applicability authority (§10), step 4 runs Phase 1 then Phase 2 (§3). Steps 10 and 11 are required independent sections -- executing step 10 without step 11 is a section-order violation. The order contract itself enforces construction-before-scoring and registration-before-inheritance.

---

## Prompt Body

You are running `/org-review`.

Inputs:
```
{{artifact_id}}: [artifact name or path under review]
{{depth}}: [standard | deep | quick]
{{reviewer_set}}: [auto | all | comma-separated role names from .craft/roles/]
```

Acknowledge injected values before executing any section.

---

### §§ PREAMBLE CONTRACTS

**§1 DISPOSITION ALGEBRA (C-10, C-02)**
```
HIGH = blocks commitment | MEDIUM = conditions commitment | LOW = advisory
FAIL -> BLOCKED | >= 1 CONDITIONAL + no FAIL -> CONDITIONAL | All PASS -> READY
```
OVERRIDE: BRACKET CLOSING only, OVERRIDE INVOKED: YES | NO + justification.

---

**§2 CLASS DERIVATION CONTRACT (C-12)**
FAIL -> BLOCKED | CONDITIONAL -> CONDITIONAL | PASS -> ADVISORY (omit if none).
No editorial class assignment at assembly time.

---

**§3 NULL HYPOTHESIS DERIVATION RULE (C-03, C-17, C-23, C-35)**

**NH DIMENSION COMPARISON TABLE -- Two-Phase Construction Protocol**:

**Phase 1 -- DIMENSION REGISTRATION** (immutable before Phase 2 begins):
Emit DIMENSION REGISTRY before assigning any scores:
```
| # | Dimension | Measurement Basis | Scale |
```
- `Dimension`: evaluation axis, specific enough to score without further interpretation.
- `Measurement Basis`: the observable being scored (e.g., "estimated developer-days",
  "% users completing task unassisted in < 2 min").
- `Scale`: scoring range consistent across all dimensions and alternatives (e.g.,
  "1=worst, 10=best"). Declared once in Phase 1.
- Minimum 3 rows. No dimensions may be added, removed, or renamed in Phase 2.

**Phase 2 -- VALUE ASSIGNMENT** (follows Phase 1):
Score all three alternatives using Phase 1 dimensions and scale:
```
| Dimension | A: Status Quo | B: Proposed Build | C: Best Non-Build Alt | Delta B-A | Delta B-C |
```
g_null derivable from table alone:
```
g_null = PASS        if delta_B_A > 0 AND delta_B_C > 0
g_null = CONDITIONAL if exactly one delta > 0
g_null = FAIL        if delta_B_A <= 0 AND delta_B_C <= 0
```

**Prose testimony** follows Phase 2. Prose may not change Phase 1 definitions or
Phase 2 values. Table governs g_null.

**CONSTRUCTION DEVIATION CASE**: If Phase 2 reveals a Phase 1 dimension was poorly
specified, emit:
```
NH-CONSTRUCTION-DEVIATION: Dimension=[d] / Phase-1-basis=[original] /
  Issue=[issue] / Proposed-revision=[revision]
```
Phase 1 values govern unless BRACKET CLOSING invokes OVERRIDE INVOKED: YES.
Flag in CROSS-ROLE SIGNALS.

**PRIMACY DEVIATION CASE (C-35)**: prose asserting different g_null than Phase 2 formula ->
`NH-NARRATIVE-TABLE-MISMATCH: prose=[X]; table=[Y]; table governs.` Binding at both.

BRACKET CLOSING re-populates Phase 2 columns B and C (Phase 1 immutable). g_null(final)
from revised Phase 2 table per formula.

---

**§4 NULL HYPOTHESIS PROGRESSION CONTRACT (C-28)**
```
Stage 1: g_null(initial)     [BRACKET OPENING -- from Phase 2 table]
Stage 2: g_null(post-domain) [CH-ID SATURATION CHECK -- G_domain_agg formula]
         FAIL: holds | PASS: weakens one tier | CONDITIONAL: CONDITIONAL
Stage 3: g_null(final)       [BRACKET CLOSING -- same substituting G_lifecycle]
```
GClose = g_null(final) or OVERRIDE INVOKED: YES.

---

**§5 LOCAL GATE LEDGER PROTOCOL (C-18, C-19, C-21, C-25)**
Universal: BRACKET OPENING, DOMAIN sections, LIFECYCLE, BRACKET CLOSING emit one row:
```
| Gate Verdict | Section Severity | Class | Finding References |
```
Non-verdict sections: no row (see §7). MASTER ACTION REGISTER: verbatim copy.

---

**§6 VERBATIM ASSEMBLY PROHIBITION (C-20)**
Verbatim copy only. Re-derivation of Gate Verdict or Class prohibited.
Local row is point of authority.

---

**§7 NON-VERDICT SECTION EXCLUSION (C-25)**
No gate row: SCOPE DECLARATION, LENS APPLICABILITY PRE-REGISTRATION, CH-ID REGISTRATION
TABLE, CH-ID SATURATION CHECK, SCOPE COVERAGE RECONCILIATION, LENS COVERAGE TABLE,
DOMAIN COVERAGE GAP-CHECK.

---

**§8 SECTION ORDER CONTRACT (C-26)** -- immutable:
```
1.  SCOPE DECLARATION            [domain tags committed here per §9]
2.  LENS APPLICABILITY PRE-REGISTRATION   [Applicability authority per §10]
3.  CH-ID REGISTRATION TABLE
4.  BRACKET OPENING  [Phase 1 DIMENSION REGISTRY then Phase 2 VALUE ASSIGNMENT]
5.  DOMAIN REVIEWER SECTIONS (manifest order)
6.  CH-ID SATURATION CHECK
7.  LIFECYCLE REVIEWER SECTION
8.  BRACKET CLOSING  [re-populate Phase 2 columns B/C; Phase 1 immutable]
9.  SCOPE COVERAGE RECONCILIATION
10. LENS COVERAGE TABLE          [Applicability verbatim-copy from step 2 per §11]
11. DOMAIN COVERAGE GAP-CHECK    [domain input from step 1 per §9]
12. DISPOSITION + PRIMARY DRIVER
13. MASTER ACTION REGISTER
14. CROSS-ROLE SIGNALS
```
Step 2 completes before step 4. Step 7 precedes step 8. Steps 10 and 11 are required
independent sections; executing step 10 without step 11 is a section-order violation.

---

**§9 SCOPE-DECLARATION DOMAIN ANNOTATION + GAP-CHECK SOURCE PROTOCOL (C-34)** [IMMUTABLE]

At SCOPE DECLARATION (step 1), annotate every IN-SCOPE surface with a domain tag:
```
| Surface | Domain | In/Out of Scope | Note |
```
Domain list is committed at step 1 and read-only for gap-check purposes. DOMAIN
COVERAGE GAP-CHECK (step 11) iterates unique Domain values from this table as its
sole input set. Post-review domain inference is prohibited as the gap-check source.
Domains found in findings but absent from step 1: flag UNDECLARED-DOMAIN in CROSS-ROLE
SIGNALS; do not add to gap-check input set.

---

**§10 LENS APPLICABILITY PRE-REGISTRATION PROTOCOL (C-33)** [IMMUTABLE]

Before any reviewer section, emit:
```
| Reviewer Role | Lens Dimension | Pre-Committed Applicability |
```
Applicability (HIGH/MEDIUM/LOW): artifact-specific. Immutable after pre-registration.
This table is the applicability authority for all downstream steps.

---

**§11 APPLICABILITY INHERITANCE PROTOCOL (C-33)** [IMMUTABLE]

PRE-REGISTRATION TABLE (step 2, §10) is the Applicability authority. LENS COVERAGE
TABLE (step 10) Applicability column: verbatim-copy from PRE-REGISTRATION only.
No re-derivation at table-population time.

Deviation: emit INHERITANCE-DEVIATION-ALERT when pre-registered value differs from
what the model would independently assign at step 10:
```
INHERITANCE-DEVIATION-ALERT: Role=[r] / Dimension=[d] /
  Pre-Registered=[X] / Attempted=[Y] / Justification=[z]
```
Pre-registered value governs unless BRACKET CLOSING invokes OVERRIDE INVOKED: YES.
Flag as ADVISORY in CROSS-ROLE SIGNALS. Silent recalculation is a chain-of-custody error.

---

**§12 CH-ID CHALLENGE REGISTRATION (C-04, C-05)**
```
| CH-ID | Challenge Statement | Bracket Opening | [Domain roles...] | Lifecycle | Bracket Closing |
```
Every reviewer section carries a CH-ID response table.

---

**§13 CH-ID SATURATION REQUIREMENT (C-27)**
SATURATED: every CH-ID >= 1 DOMAIN response. FULLY SATURATED: + LIFECYCLE.
BRACKET CLOSING PASS blocked when UNSATURATED without waiver.

---

**§14 LIFECYCLE VERDICT INTEGRATION CONTRACT (C-22)**
LIFECYCLE (step 7) precedes BRACKET CLOSING (step 8).
`Lifecycle verdict received: g_lifecycle = [value]` as labeled input.

---

**§15 DOMAIN-AGGREGATE FORMULA (C-24)**
G_domain_agg = median(all DOMAIN gate verdicts). FAIL < CONDITIONAL < PASS. Labeled input.

---

**§16 ROLE LENS EXHAUSTION PROTOCOL (C-31)** [IMMUTABLE]

LENS COVERAGE TABLE (step 10):
```
| Reviewer Role | Lens Dimension | Applicability | Status | Finding Reference(s) |
```
Applicability: verbatim-copy from PRE-REGISTRATION per §11. Deviations require
INHERITANCE-DEVIATION-ALERT. HIGH + OPEN -> ADVISORY-OPEN-LENS in MASTER ACTION REGISTER.

**DOMAIN COVERAGE GAP-CHECK (step 11, mandatory)**: iterate unique domain values from
step 1 scope table (§9); no new domains from findings. Check HIGH Applicability per
domain. ADVISORY-GAP for uncovered; append to MASTER ACTION REGISTER.
Emit: `DOMAIN COVERAGE GAP-CHECK: [N covered at HIGH | N ADVISORY-GAP]`

---

**§17 SCOPE COVERAGE GATE PROTOCOL (C-29)**
Post-BRACKET CLOSING: SCOPE COVERAGE RECONCILIATION maps IN-SCOPE surfaces to findings.
GAP -> ADVISORY-GAP, LOW, appended. No gate row.

---

**§18 PER-FINDING SEVERITY CHAIN (C-30)** [IMMUTABLE]
Section Severity = worst(individual severities). Every finding row carries individual
Severity. No editorial section-level assignment.

---

**§19 PRIMARY DRIVER DERIVATION (C-32)** [IMMUTABLE]
First-match: BRACKET CLOSING OVERRIDE > NULL HYPOTHESIS > DOMAIN FAIL (first) >
LIFECYCLE FAIL > DOMAIN CONDITIONAL (first) > LIFECYCLE CONDITIONAL > CONSENSUS.
`Primary Driver: [value]` at DISPOSITION.

---

**§20 INPUT VARIABLE CONTRACTS (C-08, C-13, C-15)**
Variables: `{{artifact_id}}`, `{{depth}}`, `{{reviewer_set}}`. Acknowledgment block required.

---

### EXECUTION

**Step 1**: Acknowledge inputs -- emit acknowledgment block with all three variable values.

**Step 2: SCOPE DECLARATION** (§9)
Emit annotated scope table with domain tags for every IN-SCOPE surface:
`| Surface | Domain | In/Out of Scope | Note |`
Domain list committed here; read-only for gap-check. OUT-OF-SCOPE surfaces enumerated.
Mid-review discoveries: flag as scope gap.

**Step 3: LENS APPLICABILITY PRE-REGISTRATION** (§10)
Pre-commit all lens dimension Applicability ratings for every active reviewer role.
Emit PRE-REGISTRATION TABLE before CH-ID REGISTRATION. No reviewer runs until complete.
These values are the applicability authority for all downstream steps.

**Step 4: CH-ID REGISTRATION TABLE** (§12)

**Step 5: BRACKET OPENING**
- Phase 1 DIMENSION REGISTRATION (§3): emit DIMENSION REGISTRY (>= 3 dimensions with
  measurement basis and scale); Phase 1 complete before any scores.
- Phase 2 VALUE ASSIGNMENT (§3): score all three alternatives; compute deltas.
- Emit g_null(initial) from Phase 2 table per formula.
- Apply PRIMACY DEVIATION CASE if prose and table diverge.
- Apply CONSTRUCTION DEVIATION CASE if Phase 1 basis appears ill-defined after Phase 2.
- Emit OVERRIDE INVOKED: NO (default).
- CH-ID responses per §12.
- LOCAL GATE LEDGER ROW per §5.

**Step 6: DOMAIN REVIEWER SECTIONS** (one per role, manifest order)
- "As a [role], I evaluate [lens concern]."
- Finding rows: `| Severity | Surface | Finding | Recommendation |`
- CH-ID responses.
- LOCAL GATE LEDGER ROW per §5. Section Severity = worst(finding severities) per §18.

**Step 7: CH-ID SATURATION CHECK**
- Verify SATURATED tier.
- Emit g_null(post-domain) per §4 Stage 2 formula.
- No gate ledger row.

**Step 8: LIFECYCLE REVIEWER SECTION**
- Lifecycle lens over operational phases.
- Finding rows (same format).
- CH-ID responses.
- LOCAL GATE LEDGER ROW per §5 with g_lifecycle labeled.

**Step 9: BRACKET CLOSING**
- Receive G_domain_agg (§15) and g_lifecycle as labeled inputs.
- Re-populate Phase 2 NH table columns B and C (Phase 1 immutable).
- Derive g_null(final) per §3 formula (§4 Stage 3).
- Emit OVERRIDE INVOKED: YES | NO as labeled field.
- LOCAL GATE LEDGER ROW per §5.

**Step 10: SCOPE COVERAGE RECONCILIATION** (§17; no gate ledger row)

**Step 11: LENS COVERAGE TABLE** (§16; no gate ledger row)
Verbatim-copy Applicability from step 3 per §11. Emit INHERITANCE-DEVIATION-ALERT
for any deviation. HIGH + OPEN rows -> ADVISORY-OPEN-LENS in register.

**Step 12: DOMAIN COVERAGE GAP-CHECK** (§16; no gate ledger row)
Iterate unique domain values from step 2 scope table (§9). No post-review domain
inference. ADVISORY-GAP for uncovered domains; append to register.

**Step 13: DISPOSITION**
- Apply §1 DISPOSITION ALGEBRA.
- Emit `DISPOSITION: READY | CONDITIONAL | BLOCKED` as labeled field.
- Emit `Primary Driver: [value]` per §19.

**Step 14: MASTER ACTION REGISTER**
- Copy all LOCAL GATE LEDGER ROWS verbatim per §6.
- Append ADVISORY-OPEN-LENS items from step 11.
- Append ADVISORY-GAP items from step 12.
- Append ADVISORY-GAP items from step 10.
- Do not re-derive Gate Verdict or Class.

**Step 15: CROSS-ROLE SIGNALS**
- Integration narrative: name >= 1 cross-role conflict or convergence.
- Reference g_null progression through all three stages (initial, post-domain, final).
- Explain the disposition rather than restating it.
- Flag any INHERITANCE-DEVIATION-ALERTs from step 11.
- Flag any NH-CONSTRUCTION-DEVIATIONs from step 5.
- Flag any UNDECLARED-DOMAIN discoveries from step 12.

---

## Final Rubric Criteria Summary (v11, 225 pts)

### Essential -- 60 pts

| ID | Name | Pts | What it enforces |
|----|------|-----|-----------------|
| C-01 | Multi-voice Role Architecture | 12 | Named challenger + >= 1 domain role; independent frames; no cross-role aggregation at collection time |
| C-02 | Severity Carries Commit-Gate Semantics | 12 | HIGH=blocks / MEDIUM=conditions / LOW=advisory stated in output; every label interpretable |
| C-03 | Null Hypothesis Gate Before Domain | 12 | NH statement + verdict before any domain section; challenger provides it |
| C-04 | Commitment Disposition Emitted | 12 | READY / CONDITIONAL / BLOCKED as labeled field; consistent with algebra |
| C-05 | Action Items Traceable | 12 | CH-ID registration + LOCAL GATE LEDGER + MASTER ACTION REGISTER; consolidated |

### Recommended -- 30 pts

| ID | Name | Pts | What it enforces |
|----|------|-----|-----------------|
| C-06 | Artifact Scope Declared | 10 | SCOPE DECLARATION before any reviewer; OUT-OF-SCOPE named |
| C-07 | Summary with Integrating Narrative | 10 | Cross-role conflict/convergence; g_null all 3 stages; disposition explained |
| C-08 | Depth Parameter Honored | 10 | deep/standard/quick behavior defined; acknowledgment block required |

### Aspirational -- 135 pts (27 criteria x 5 pts)

| ID | Name | Category | What it enforces |
|----|------|----------|-----------------|
| C-09 | Adversarial Bracket | structure | BRACKET OPENING + BRACKET CLOSING; challenger override authority |
| C-10 | Disposition Algebra Pre-committed | correctness | §1 formula in preamble covers all combinations |
| C-11 | Override as Labeled Field | correctness | OVERRIDE INVOKED: YES\|NO in BRACKET CLOSING |
| C-12 | Class Derived Mechanically | correctness | §2 CLASS DERIVATION CONTRACT; no editorial assignment |
| C-13 | Prompt Inputs as Template Variables | structure | {{artifact_id}}, {{depth}}, {{reviewer_set}} declared |
| C-14 | Gate Verdict in Action Register | traceability | LOCAL GATE LEDGER ROWS carry Gate Verdict; verbatim-copied to MASTER |
| C-15 | Reviewer Set Injectable | structure | {{reviewer_set}} overrides depth-based selection when non-auto |
| C-16 | Alternatives Table as Bracket Anchor | correctness | NH table at bracket opening; g_null derivable from table alone |
| C-17 | All Three Contracts in Preamble | structure | §1 DISPOSITION + §2 CLASS DERIVATION + §3 NH DERIVATION all in preamble |
| C-18 | Inline Gate Ledger at Origin | traceability | LOCAL GATE LEDGER ROW at end of every verdict-emitting section |
| C-19 | Gate Ledger Protocol Pre-committed | structure | §5 syntax + timing + assembly rule in preamble |
| C-20 | Verbatim Assembly Prohibition | correctness | §6 copy-only; re-derivation prohibited; local row is authority |
| C-21 | Universal Gate Ledger Coverage | traceability | §5 names all archetypes: BRACKET OPENING, DOMAIN, LIFECYCLE, BRACKET CLOSING |
| C-22 | Lifecycle Verdict Integration | correctness | LIFECYCLE precedes BRACKET CLOSING; g_lifecycle as labeled input |
| C-23 | Multi-alternative NH Coverage | correctness | Three alternatives A/B/C; rule covers Delta B-A and Delta B-C |
| C-24 | Domain-Aggregate Formula | correctness | G_domain_agg = median(DOMAIN verdicts); labeled input to BRACKET CLOSING |
| C-25 | Non-verdict Section Excluded | traceability | §7 names excluded sections; no spurious gate rows |
| C-26 | Section Order Contract | structure | §8 immutable 14-step sequence; reordering is violation |
| C-27 | CH-ID Saturation Pre-committed | correctness | §12/§13 SATURATED + FULLY SATURATED tiers; BRACKET CLOSING blocked on UNSATURATED |
| C-28 | NH Progression Formula 3-stage | correctness | §4 g_null(initial) -> g_null(post-domain) -> g_null(final) derivation chain |
| C-29 | Scope-to-Finding Coverage Gate | traceability | §17 SCOPE COVERAGE RECONCILIATION; ADVISORY-GAP for unmapped surfaces |
| C-30 | Per-Finding Severity Chain | correctness | §18 [IMMUTABLE] Section Severity = worst(findings); no editorial assignment |
| C-31 | Role Lens Exhaustion Pre-committed | depth | §16 [IMMUTABLE] LENS COVERAGE TABLE; OPEN -> ADVISORY-OPEN-LENS |
| C-32 | Primary Driver Derivation | correctness | §19 [IMMUTABLE] 7-rule precedence; Primary Driver as labeled field |
| C-33 | Lens Applicability Rating Pre-committed | depth | §10 PRE-REGISTRATION + §11 INHERITANCE PROTOCOL; verbatim-copy; INHERITANCE-DEVIATION-ALERT |
| C-34 | ADVISORY-GAP Domain Coverage Pre-committed | depth | §9 domain tags at step 1; gap-check reads step 1 only; UNDECLARED-DOMAIN flag |
| C-35 | NH Challenger Dimension Comparison Table | correctness | §3 two-phase; Phase 1 immutable; NH-CONSTRUCTION-DEVIATION; PRIMACY DEVIATION CASE |

**Gold threshold: 190 / 225**
