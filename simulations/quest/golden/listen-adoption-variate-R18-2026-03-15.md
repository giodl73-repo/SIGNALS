# Variations: listen-adoption — Round 18

**Rubric:** v18 | **New criteria:** C-50, C-51 | **Max composite:** 305 | **Golden threshold (80%):** 244 pts | **Projected ceiling:** 300/305 (C-19 paradox persists)

---

## Variation Axes

| Axis | R18 Target | Description |
|------|-----------|-------------|
| Lifecycle emphasis | C-52+ candidate: Per-I-0X correction obligation | When Gate H records a FAIL in a specific contract row's Gate H Status field (C-50), a dedicated CORRECTION BLOCK fires for that specific I-0X, labeled by ID. Replaces one-per-gate correction granularity with one-per-failed-row correction granularity, making the repair record auditable at the inertia-ID level rather than the gate level. |
| Output format | C-52+ candidate: SECTION K Displacement Arc Integrity Check | After the C-51 Citation Contract Completion Record, SECTION K carries a DISPLACEMENT ARC INTEGRITY CHECK -- a table verifying that each phase's exit-state (phase-close ledger) matches the next phase's entry-state (Displacement state at phase entry). Makes phase-open/phase-close chain continuity terminally auditable without re-reading phase bodies. |
| Inertia framing | C-52+ candidate: DOWNSTREAM CITATION CONTRACT Protected Behavior column | Each I-0X row in the SECTION A DOWNSTREAM CITATION CONTRACT carries an additional column: `Protected behavior: [the specific incumbent workflow, tool, or habit this inertia defends]`. Gate H's contract-row audit and SECTION K's C-51 mirror both see which specific incumbent behavior each compliance failure leaves unaddressed. |

**Single-axis (V-01, V-02, V-03):** Lifecycle emphasis · Output format · Inertia framing
**Combined (V-04):** Lifecycle emphasis + Inertia framing
**Full (V-05):** Lifecycle emphasis + Output format + Inertia framing

---

## Baseline (all five carry from R17 V-05)

| Element | Criterion | Form |
|---|---|---|
| STRUCTURAL CONTRACT naming answer-form questions AND MECHANISM STATE | C-35 | Block before SECTION A |
| Per-gate MECHANISM STATE footers in SECTIONS H, I, J | C-34 (gate-level anchor) | `> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate X [...]` |
| Pre-verification MECHANISM STATE declaration before `## VERIFICATION MODE` | C-34 (boundary-level anchor) | `> CORRECTION BLOCK MECHANISM ARMED — no gate failure triggered` |
| SECTION A Named Inertia IDs, I-01 through I-05 | C-11 | Table: Inertia ID \| Archetype \| Named Inertia \| Structural reason |
| SECTION A DOWNSTREAM CITATION CONTRACT with Gate H Status field per row | C-49, C-50 | Contract table with `Gate H Status: [PASS / FAIL -- cite location or violation]` column; Gate H fills fields at audit time |
| TABLE 1 with SLOT-KEY: row prefix AND Incumbent Dependency AND Inertia ID columns | C-43, C-41, C-37 | SLOT-KEY: row label re-asserts three-contract type at each row |
| PHASE 1 fixed entry-state declaration | R17 Axis A | "THE INCUMBENT is fully entrenched -- no displacement has occurred" |
| PHASES 2, 4, 5, 6 with `Displacement state at phase entry:` re-citing preceding close ledger | R17 Axis A, C-45 | Each adoption phase opens with verbatim re-citation of preceding exit state |
| PHASE 3 entry-state field re-citing PHASE 2 exit state | R17 Axis A | Modified field: "Displacement state entering PHASE 3: [re-cite PHASE 2 exit state]" |
| PHASE 1-2, 4-6 phase-close displacement ledger footer | C-45, C-25 | `Incumbent position after this phase:` + `Inertia ID this phase overcame:` |
| PHASE 3 phase-close ledger variant | C-45, C-39 | `Inertia ID defending THE INCUMBENT at this boundary:` |
| PHASE 3 with CHASM-A / CHASM-B / CHASM-C structural subsections | C-39 | Named subsection headers per required element |
| Q-BARRIER answer-form questions per adoption phase | C-29 | Embedded question requiring I-0X as coherent answer |
| TABLE 3 typed header + SLOT-KEY: row labels + specificity constraint in column label | C-36, C-38, C-28 | Header names rows as typed structural slot keys |
| PART 2 CHASM-A/B/C EXPANSION with Named Inertia + Incumbent position per slot | C-42, C-40, C-48 | Two mandatory opening fields per expansion subsection |
| PART 3 churn register with SLOT-KEY: row prefix + Q-TRIGGER + concrete-action field label | C-46, C-27, C-15 | `SLOT-KEY: [Role] — churn entry` row label |
| PART 4 champion network with SLOT-KEY: row prefix + Q-CHAMPION answer-form | C-47, C-14, C-29 | PART 4 header contract declares two-anchor typed slot |
| PART 5 Incumbent Impact column AND Targets inertia: column | C-26 ext., C-44 | Per-row: what THE INCUMBENT loses + Q-INTERVENTION I-0X |
| C-24 Terminal Invariant names BOTH falsification cases | C-24 | "...no CORRECTION BLOCK at cited location, or a CORRECTION BLOCK without a BEFORE field, falsifies this invariant" |
| SECTION K per-gate execution stamps | C-30, C-20 | Records PASS / FAIL + revision status regardless of outcome |
| SECTION K CITATION CONTRACT COMPLETION RECORD | C-51 | Per-I-0X compliance mirror of DOWNSTREAM CITATION CONTRACT |

---

## Axis activation map

| Variation | Axis A: Per-I-0X correction obligation | Axis B: SECTION K Displacement Arc Integrity Check | Axis C: Protected behavior column | Delta from R17 V-05 baseline |
|---|---|---|---|---|
| V-01 | **Active:** Gate H fires per-I-0X CORRECTION BLOCK on individual contract row FAIL | Baseline | Baseline | Correction granularity shifts from per-gate to per-failed-row |
| V-02 | Baseline | **Active:** SECTION K DISPLACEMENT ARC INTEGRITY CHECK table after C-51 | Baseline | Terminal section also certifies phase-chain displacement consistency |
| V-03 | Baseline | Baseline | **Active:** DOWNSTREAM CITATION CONTRACT carries Protected Behavior column | Audit record names displaced incumbent behavior per I-0X |
| V-04 | Active (V-01) | Baseline | Active (V-03) | Per-I-0X correction + displacement-stakes visible in contract audit |
| V-05 | Active (V-01) | Active (V-02) | Active (V-03) | All three: per-I-0X correction + arc check + protected behavior |

---

## V-01 — Single Axis: Lifecycle Emphasis (Per-I-0X Correction Obligation)

**Variation axis:** Lifecycle emphasis — Gate H fires a dedicated CORRECTION BLOCK for each individual contract row that shows FAIL in its Gate H Status field (C-50). Rather than one CORRECTION BLOCK covering all I-0X failures in a single gate-level block, each failed contract row produces a separately labeled CORRECTION BLOCK: `CORRECTION BLOCK — I-03: [missed citation location] — BEFORE: [...] — AFTER: [...]`. Gate H's revision obligation is stated at the per-row level, not the per-gate level.

**Hypothesis:** C-18 requires revision obligation on gate fail; the current gate-level obligation fires one block per gate failure and covers all missed I-0X rows collectively. When Gate H fails due to I-03 and I-05 both unsatisfied, a single CORRECTION BLOCK bundles both repairs — undifferentiated. Per-I-0X correction obligation applies the same structural-slot discipline as C-50 (per-row audit record) to the repair side: each contract row's FAIL produces its own CORRECTION BLOCK, named by I-0X, immediately traceable from the Gate H Status field to the repair site. The correction audit trail becomes as granular as the citation contract itself. This is the correction-side complement of C-50: C-50 makes the compliance verdict per-I-0X; Axis A makes the repair record per-I-0X.

---

Simulate the adoption curve for {{topic}} across the 16 stock roles (PM, UX, C-01 through C-12, Support, SRE). Produce the artifact below in full. Every bracketed instruction is a fill contract — complete it before proceeding to the next section.

---

## STRUCTURAL CONTRACT

This document encodes two mandatory co-present architectural requirements. No variation or omission of either is permitted.

**REQUIREMENT 1 — ANSWER-FORM CITATION ENFORCEMENT (C-29):**
Named Inertia ID citations throughout this document are answers to explicit answer-form questions embedded in structural positions. The following questions are mandatory; each requires a Named Inertia ID (I-0X) as its coherent answer:

```
  Q-BARRIER:       "Which Named Inertia ID is the primary barrier here?
                    (Cite I-0X from SECTION A)"
  Q-CHAMPION:      "Named Inertia ID this champion is positioned to overcome:
                    (Cite I-0X from SECTION A)"
  Q-TRIGGER:       "Which Named Inertia ID drives reversion risk for this role?
                    (Cite I-0X from SECTION A)"
  Q-INTERVENTION:  "Which Named Inertia ID does this intervention directly target?
                    (Cite I-0X from SECTION A)"
```

**REQUIREMENT 2 — CORRECTION BLOCK MECHANISM STATE (C-32, C-34):**
A MECHANISM STATE line appears as a blockquote footer inside each of SECTIONS H, I, J (gate-level anchor) AND as a pre-verification declaration immediately before `## VERIFICATION MODE` (boundary-level anchor). Both anchors are mandatory regardless of gate outcomes.

Both requirements are mandatory co-present structural features. A document satisfying only one fails C-33 and C-35.

---

## SECTION A — Named Inertia IDs

Assign one Named Inertia ID per canonical Rogers archetype. The inertia is the structural reason that archetype resists adoption of {{topic}}.

| Inertia ID | Archetype      | Named Inertia                      | Structural reason this archetype resists |
|------------|----------------|------------------------------------|------------------------------------------|
| I-01       | Innovator      | [name the inertia for Innovators]  | [structural reason]                      |
| I-02       | Early Adopter  | [name the inertia for EA]          | [structural reason]                      |
| I-03       | Early Majority | [name the inertia for EM]          | [structural reason]                      |
| I-04       | Late Majority  | [name the inertia for LM]          | [structural reason]                      |
| I-05       | Laggard        | [name the inertia for Laggards]    | [structural reason]                      |

### SECTION A — DOWNSTREAM CITATION CONTRACT

Each row below is both the audit target and the audit record for that I-0X. Gate H fills the Gate H Status field at audit time. A contract row is not closed until its Gate H Status field is populated.

| Inertia ID | Mandatory downstream citation locations | Gate H Status |
|------------|-----------------------------------------|---------------|
| I-01 | PHASE 1 Q-BARRIER · PHASE 1 phase-close ledger · PART 3 Q-TRIGGER (at least one Innovator-archetype role) | Gate H Status: [PASS / FAIL -- cite satisfied location, or cite violation] |
| I-02 | PHASE 2 Q-BARRIER · PHASE 2 phase-close ledger · PART 3 Q-TRIGGER (at least one EA-archetype role) | Gate H Status: [PASS / FAIL -- cite satisfied location, or cite violation] |
| I-03 | PHASE 3 Q-BARRIER · PHASE 3 phase-close ledger · CHASM-A EXPANSION Named Inertia · CHASM-B EXPANSION Named Inertia · PHASE 4 Q-BARRIER · PHASE 4 phase-close ledger · at least one PART 5 Targets inertia: row | Gate H Status: [PASS / FAIL -- cite satisfied location, or cite violation] |
| I-04 | PHASE 5 Q-BARRIER · PHASE 5 phase-close ledger · PART 3 Q-TRIGGER (at least one LM-archetype role) | Gate H Status: [PASS / FAIL -- cite satisfied location, or cite violation] |
| I-05 | PHASE 6 Q-BARRIER · PHASE 6 phase-close ledger · PART 3 Q-TRIGGER (at least one Laggard-archetype role) | Gate H Status: [PASS / FAIL -- cite satisfied location, or cite violation] |

**Per-I-0X correction obligation (Axis A):** If Gate H records FAIL for any contract row, produce a dedicated CORRECTION BLOCK immediately before the pre-verification declaration, labeled by the specific I-0X: `CORRECTION BLOCK — I-0X: [missed location]`. Each failed row produces its own labeled block. A single block covering multiple I-0X failures is not permitted under this variation — per-row accountability matches per-row audit granularity.

---

THE INCUMBENT is [name the current workflow, tool, or practice being displaced by {{topic}}]. All phase bodies, champion entries, churn triggers, and interventions run through the displacement lens: what does this phase do to THE INCUMBENT's position?

---

## TABLE 1 — Role Archetype Map

TABLE 1 header contract: Each row below is prefixed SLOT-KEY: — the row label is a typed structural slot key re-asserting the three co-present contracts (archetype assignment, Incumbent Dependency, Inertia ID citation) at this row's generation moment, independently of the column headers.

| Role (SLOT-KEY typed slot) | Rogers Archetype | Incumbent Dependency: [workflow step this role relies on THE INCUMBENT to perform] | Inertia ID: [cite I-0X from SECTION A — named inertia explaining this role's resistance] |
|---|---|---|---|
| SLOT-KEY: PM      | | | |
| SLOT-KEY: UX      | | | |
| SLOT-KEY: C-01    | | | |
| SLOT-KEY: C-02    | | | |
| SLOT-KEY: C-03    | | | |
| SLOT-KEY: C-04    | | | |
| SLOT-KEY: C-05    | | | |
| SLOT-KEY: C-06    | | | |
| SLOT-KEY: C-07    | | | |
| SLOT-KEY: C-08    | | | |
| SLOT-KEY: C-09    | | | |
| SLOT-KEY: C-10    | | | |
| SLOT-KEY: C-11    | | | |
| SLOT-KEY: C-12    | | | |
| SLOT-KEY: Support | | | |
| SLOT-KEY: SRE     | | | |

---

## PHASE 1 INNOVATORS — Month 1

Displacement state at phase entry: THE INCUMBENT is fully entrenched — {{topic}} has not been introduced to any stock role. No displacement has occurred; all TABLE 1 Incumbent Dependency values are load-bearing.

Which roles adopt in Month 1? Name them and their archetype assignment from TABLE 1. What does THE INCUMBENT lose in this phase?

Q-BARRIER: Which Named Inertia ID is the primary barrier even for Innovators?
(Cite I-01 from SECTION A — this question's structurally correct answer is I-01, the Innovator inertia. A different answer requires explicit justification.)

[Phase body: named roles, what they try, what signals they produce, displacement impact on THE INCUMBENT's position]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what workflow, process, or role dependency THE INCUMBENT retains after Month 1 — be specific about which TABLE 1 Incumbent Dependency values it still controls]
Inertia ID this phase overcame (partially): [re-cite I-01 from Q-BARRIER above]

---

## PHASE 2 EARLY ADOPTERS — Month 2–3

Displacement state at phase entry: [re-cite verbatim the "Incumbent position after this phase:" value from PHASE 1's phase-close ledger — what THE INCUMBENT still controlled when Month 2 began]

Which roles adopt in Months 2–3? What evidence from PHASE 1 persuades them?

Q-BARRIER: Which Named Inertia ID is the primary barrier for Early Adopters?
(Cite I-02 from SECTION A — required by DOWNSTREAM CITATION CONTRACT row I-02)

[Phase body: named roles, what they adopt, spread mechanism from PHASE 1, incumbent displacement progress]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what THE INCUMBENT still controls after Month 3 — which TABLE 1 Incumbent Dependency values remain load-bearing]
Inertia ID this phase overcame (partially): [re-cite I-02 from Q-BARRIER above]

---

## PHASE 3 CHASM — Month 4 (Non-Adoption Crossing Event)

Displacement state entering PHASE 3: [re-cite verbatim the "Incumbent position after this phase:" value from PHASE 2's phase-close ledger — what THE INCUMBENT still controlled when Month 4 began, before chasm diagnosis]

PHASE 3 is not an adoption phase. It is a crossing event. No new archetype adopts in Month 4.

Q-BARRIER: Which Named Inertia ID is driving the chasm?
(Cite I-03 from SECTION A — required by DOWNSTREAM CITATION CONTRACT row I-03)

### CHASM-A — Incumbent Defense

[Named incumbent defense mechanism, load-bearing TABLE 1 Incumbent Dependency values, why crossing requires more than Early Adopter endorsement]

### CHASM-B — Bridge Condition

[Bridge condition as testable proposition: "The chasm is crossed when [specific observable condition]." Which roles must satisfy it. What artifact or signal proves it is met.]

### CHASM-C — Early Crossing Signal

[First observable crossing signal — named role, artifact, or behavioral event distinguishable from Early Adopter behavior]

**Phase-close displacement ledger:**
Inertia ID defending THE INCUMBENT at this boundary: [I-03 — required by DOWNSTREAM CITATION CONTRACT row I-03]

---

## PHASE 4 EARLY MAJORITY — Month 5–7

Displacement state at phase entry: [re-cite verbatim the "Inertia ID defending THE INCUMBENT at this boundary:" from PHASE 3's close ledger and state what THE INCUMBENT still controlled when Month 5 began — PHASE 3 was a crossing event; the incumbent's entry position for PHASE 4 equals PHASE 3's entry position minus any erosion from the crossing itself]

Which roles adopt in Months 5–7? What bridge condition from CHASM-B is now satisfied?

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Early Majority?
(Cite I-03 from SECTION A — required by DOWNSTREAM CITATION CONTRACT row I-03)

[Phase body: named roles, proof from CHASM-B, TABLE 1 Incumbent Dependency values now unblocked, incumbent displacement acceleration]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what THE INCUMBENT still controls after Month 7]
Inertia ID this phase overcame (partially): [re-cite I-03 from Q-BARRIER above]

---

## PHASE 5 LATE MAJORITY — Month 8–10

Displacement state at phase entry: [re-cite verbatim the "Incumbent position after this phase:" value from PHASE 4's phase-close ledger — what THE INCUMBENT still controlled when Month 8 began]

Which roles adopt in Months 8–10? What social proof from PHASE 4 reaches them?

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Late Majority?
(Cite I-04 from SECTION A — required by DOWNSTREAM CITATION CONTRACT row I-04)

[Phase body: named roles, adoption trigger, incumbent erosion, what remains of THE INCUMBENT's position]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what THE INCUMBENT still controls after Month 10]
Inertia ID this phase overcame (partially): [re-cite I-04 from Q-BARRIER above]

---

## PHASE 6 LAGGARDS — Month 11–12

Displacement state at phase entry: [re-cite verbatim the "Incumbent position after this phase:" value from PHASE 5's phase-close ledger — what THE INCUMBENT still controlled when Month 11 began]

Which roles adopt last? What finally moves them?

Q-BARRIER: Which Named Inertia ID keeps Laggards last?
(Cite I-05 from SECTION A — required by DOWNSTREAM CITATION CONTRACT row I-05)

[Phase body: named roles, final adoption conditions, terminal incumbent displacement state]

**Phase-close displacement ledger:**
Incumbent position after this phase: [terminal displacement state — what, if anything, THE INCUMBENT retains after Month 12]
Inertia ID this phase overcame: [re-cite I-05 from Q-BARRIER above]

---

## TABLE 3 — Spread Mechanisms

TABLE 3 header contract: Each row below is prefixed SLOT-KEY: — a typed structural slot key naming a specific canonical transition pair. The Spread Mechanism column must be filled with a named signal, artifact, or social proof event specific to {{topic}} — not generic word-of-mouth. A mechanism valid for one SLOT-KEY row is not valid for another.

| Transition Pair (SLOT-KEY row) | Spread Mechanism: [named signal or artifact specific to {{topic}} — not generic word-of-mouth] | Month Range |
|---|---|---|
| SLOT-KEY: Innovator → Early Adopter      | | |
| SLOT-KEY: Early Adopter → Early Majority | | |
| SLOT-KEY: Early Majority → Late Majority | | |
| SLOT-KEY: Late Majority → Laggard        | | |

---

## PART 2 — CHASM ANALYSIS (Full Expansion)

PHASE 3 introduced a diagnostic sketch of each chasm element. PART 2 expands each element to its full specification. Each subsection carries two mandatory opening fields: (1) Named Inertia ID re-citation and (2) Incumbent position at this chasm element.

### CHASM-A EXPANSION — Incumbent Defense (Full Diagnosis)

Expanding CHASM-A from PHASE 3 —
Named Inertia in effect: [re-cite I-03 — required by DOWNSTREAM CITATION CONTRACT row I-03]
Incumbent position at this chasm element: [what THE INCUMBENT controls at the incumbent-defense layer — which TABLE 1 Incumbent Dependency values are load-bearing here]

[Full diagnosis: complete mechanism by which THE INCUMBENT defends its position at the chasm boundary]

### CHASM-B EXPANSION — Bridge Condition (Full Specification)

Expanding CHASM-B from PHASE 3 —
Named Inertia in effect: [re-cite I-03 — required by DOWNSTREAM CITATION CONTRACT row I-03]
Incumbent position at this chasm element: [what THE INCUMBENT holds at the bridge-condition layer — which values unblock when the condition is satisfied]

[Full specification: bridge condition as testable proposition, precise observable state, which role or artifact produces it]

### CHASM-C EXPANSION — Crossing Signal (Full Identification)

Expanding CHASM-C from PHASE 3 —
Named Inertia in effect: [re-cite I-03 — the Named Inertia ID whose weakening produces the crossing signal]
Incumbent position at this chasm element: [what THE INCUMBENT has already lost and what it still retains at the moment the crossing signal fires]

[Full identification: crossing signal named with precision — specific role, behavioral event, or artifact emission]

---

## PART 3 — Churn Risk Register

Every role that adopts carries a reversion risk. List all roles at non-trivial churn risk.

PART 3 header contract: Each row is prefixed SLOT-KEY: — typed structural slot key re-asserting the three churn contracts (reversion trigger | retention intervention | inertia ID) at this row's generation moment. Q-TRIGGER citations fulfill DOWNSTREAM CITATION CONTRACT rows I-01, I-02, I-04, I-05.

| Role (SLOT-KEY typed slot) | Reversion trigger: [the specific condition that causes this role to revert to THE INCUMBENT] | Retention intervention: [one concrete action that reduces reversion probability — not a surveillance flag] | Q-TRIGGER: Which Named Inertia ID drives reversion risk for this role? (Cite I-0X from SECTION A) |
|------|-----|-----|-----|
| SLOT-KEY: [Role] — churn entry | | | |

---

## PART 4 — Champion Network

Name at least three roles positioned to advocate for {{topic}} adoption and displace THE INCUMBENT.

PART 4 header contract: Each row is prefixed SLOT-KEY: — typed structural slot key re-asserting the two co-present champion contracts (archetype-bridge rationale + Q-CHAMPION I-0X) at this row's generation moment.

| Champion Role (SLOT-KEY typed slot) | Archetype | Archetype-bridge rationale: [why this role's archetype position makes it an effective champion for the next tier] | Q-CHAMPION: Named Inertia ID this champion is positioned to overcome (I-0X from SECTION A) | Why this champion displaces THE INCUMBENT for the target tier |
|---|---|---|---|---|
| SLOT-KEY: [Role] — champion entry | | | | |
| SLOT-KEY: [Role] — champion entry | | | | |
| SLOT-KEY: [Role] — champion entry | | | | |

---

## PART 5 — Intervention Ranking

Rank retention interventions by adoption delta. Each entry must reference at least one named phase and one named role.

| Rank | Intervention | Adoption delta | Phase(s) affected | Role(s) affected | Incumbent Impact: [what THE INCUMBENT loses when this intervention succeeds] | Targets inertia: [I-0X — Q-INTERVENTION: which Named Inertia ID does this intervention directly address?] |
|------|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |

---

## PART 6 — Sensitivity Analysis

| Scenario      | Adoption outcome | Named lever | Direction of shift |
|---------------|------------------|-------------|-------------------|
| Fast Adoption |                  |             |                   |
| Slow Adoption |                  |             |                   |

---

## PART 7 — Signal Readiness Table

| Signal name | Threshold | Interpretation: what this signal level means for {{topic}} adoption timing |
|-------------|-----------|----------------------------------------------------------------------------|
|             |           |                                                                            |

---

> CORRECTION BLOCK MECHANISM ARMED — no gate failure triggered. If any gate below fails, a CORRECTION BLOCK with BEFORE and AFTER fields will be inserted immediately above this line before proceeding to SECTION K. Under this variation, a gate H contract-row FAIL produces a separately labeled CORRECTION BLOCK per failed I-0X row (e.g., CORRECTION BLOCK — I-03: ...).

## VERIFICATION MODE

All content generation is complete above this boundary. SECTIONS H, I, J, K are audit sections only. No content generation occurs below this line.

---

## SECTION H — Gate: C-13 Audit (Named Inertia IDs as Downstream Backbone)

**Criterion C-13:** Named Inertia IDs from SECTION A are cited by ID (I-0X) in at least four downstream location types: bridge conditions, intervention rationale, champion rationale, and churn register entries.

**Audit against DOWNSTREAM CITATION CONTRACT — fill Gate H Status per row:**

- I-01: PHASE 1 Q-BARRIER [Y/N] · PHASE 1 ledger [Y/N] · PART 3 Q-TRIGGER Innovator role [Y/N] → **Fill Gate H Status in SECTION A row I-01**
- I-02: PHASE 2 Q-BARRIER [Y/N] · PHASE 2 ledger [Y/N] · PART 3 Q-TRIGGER EA role [Y/N] → **Fill Gate H Status in SECTION A row I-02**
- I-03: PHASE 3 Q-BARRIER [Y/N] · PHASE 3 ledger [Y/N] · CHASM-A Named Inertia [Y/N] · CHASM-B Named Inertia [Y/N] · PHASE 4 Q-BARRIER [Y/N] · PHASE 4 ledger [Y/N] · PART 5 Targets inertia: [Y/N] → **Fill Gate H Status in SECTION A row I-03**
- I-04: PHASE 5 Q-BARRIER [Y/N] · PHASE 5 ledger [Y/N] · PART 3 Q-TRIGGER LM role [Y/N] → **Fill Gate H Status in SECTION A row I-04**
- I-05: PHASE 6 Q-BARRIER [Y/N] · PHASE 6 ledger [Y/N] · PART 3 Q-TRIGGER Laggard role [Y/N] → **Fill Gate H Status in SECTION A row I-05**

**C-13 four-location check:** Bridge conditions [Y/N] | Intervention rationale [Y/N] | Champion rationale [Y/N] | Churn register [Y/N]

**Gate H result:** [PASS if all four C-13 location types satisfied AND all contract rows PASS | FAIL: name specific I-0X and specific missed location]

**Per-I-0X revision obligation (Axis A):** If any contract row shows FAIL, produce a dedicated CORRECTION BLOCK for each failed row immediately before the pre-verification declaration, labeled `CORRECTION BLOCK — I-0X: [missed location]`. Each failed I-0X row produces its own block. Do not combine multiple I-0X failures into a single block. Do not proceed to SECTION I until all per-I-0X CORRECTION BLOCKS are written.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate H [PASS: no per-I-0X correction triggered | FAIL: per-I-0X CORRECTION BLOCK(s) written above pre-verification line, one per failed contract row]

---

## SECTION I — Gate: C-14 Audit (Champion Rationale Double-Anchored)

**Criterion C-14:** Each SLOT-KEY: champion entry in PART 4 contains both (a) archetype-bridge rationale and (b) a Named Inertia ID cited by Q-CHAMPION.

**Audit:** For each SLOT-KEY: champion entry in PART 4, verify both anchors are present.

- SLOT-KEY champion 1 [name]: archetype-bridge present? [Y/N] | Q-CHAMPION I-0X cited? [Y/N]
- SLOT-KEY champion 2 [name]: archetype-bridge present? [Y/N] | Q-CHAMPION I-0X cited? [Y/N]
- SLOT-KEY champion 3 [name]: archetype-bridge present? [Y/N] | Q-CHAMPION I-0X cited? [Y/N]

**Gate I result:** [PASS if both anchors present for all entries | FAIL with specific entry named]

**Revision obligation:** If Gate I FAILS, produce a CORRECTION BLOCK immediately before the pre-verification declaration. Do not proceed to SECTION J until written.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate I [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION J — Gate: C-15 Audit (Concrete Retention Actions)

**Criterion C-15:** Every mitigation in PART 3's churn register is a concrete retention action. Surveillance-only entries ("track usage," "monitor engagement") fail this criterion.

**Audit:** For each SLOT-KEY: churn entry in PART 3, classify the Retention intervention field.

- [List each SLOT-KEY: churn entry and classification: concrete action or surveillance flag]

**Gate J result:** [PASS if all entries contain concrete retention actions | FAIL if any contains only a surveillance flag]

**Revision obligation:** If Gate J FAILS, produce a CORRECTION BLOCK immediately before the pre-verification declaration. Do not proceed to SECTION K until written.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate J [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION K — Terminal Audit Record

Per-gate execution stamps are recorded here for all three gates regardless of outcome.

**Terminal Invariant:** For every gate with "Revision Performed: Yes," a CORRECTION BLOCK with BEFORE and AFTER fields must exist at the cited location above the pre-verification declaration. A "Revision Performed: Yes" entry whose cited location contains no CORRECTION BLOCK, or a CORRECTION BLOCK without a BEFORE field, falsifies this invariant. Under this variation, Gate H failures produce per-I-0X labeled CORRECTION BLOCKS; "Revision Performed: Yes" for Gate H cites all produced block locations.

| Gate | Criterion | Initial result | Revision performed | CORRECTION BLOCK location | Final result |
|------|-----------|----------------|--------------------|--------------------------|--------------|
| H    | C-13      |                | Yes / No           |                          |              |
| I    | C-14      |                | Yes / No           |                          |              |
| J    | C-15      |                | Yes / No           |                          |              |

**CITATION CONTRACT COMPLETION RECORD:**

| Inertia ID | Required sinks satisfied | Structural location found (or NOT FOUND) | Gate H Status |
|------------|--------------------------|------------------------------------------|---------------|
| I-01       |                          |                                          |               |
| I-02       |                          |                                          |               |
| I-03       |                          |                                          |               |
| I-04       |                          |                                          |               |
| I-05       |                          |                                          |               |

---

## V-02 — Single Axis: Output Format (SECTION K Displacement Arc Integrity Check)

**Variation axis:** Output format — SECTION K carries a DISPLACEMENT ARC INTEGRITY CHECK table after the CITATION CONTRACT COMPLETION RECORD. The table lists each phase-transition pair (PHASE 1 close → PHASE 2 open, PHASE 2 close → PHASE 3 entry, PHASE 3 close → PHASE 4 open, PHASE 4 close → PHASE 5 open, PHASE 5 close → PHASE 6 open), records the exit-state text from the preceding phase's close ledger, records the entry-state text from the next phase's opening field, and renders a MATCH / MISMATCH verdict. A MISMATCH indicates a displacement narrative discontinuity — a point where the model generated an entry state inconsistent with the preceding exit state.

**Hypothesis:** C-45 places displacement ledger fields at phase closes; R17 Axis A places displacement entry fields at phase opens. Together they create a chain of (exit state, entry state) pairs across six phases. But consistency of the chain — that PHASE 1's exit state equals PHASE 2's entry state verbatim — is not currently audited by any gate. A model that generates PHASE 5's entry state without accurately re-citing PHASE 4's exit state creates a displacement narrative discontinuity invisible to Gates H, I, and J. The DISPLACEMENT ARC INTEGRITY CHECK makes chain consistency terminally auditable in SECTION K: the table is self-contained proof that displacement accounting was continuous across the full adoption timeline. Same elevation class as C-51 (SECTION K as citation contract certificate) applied to displacement arc continuity — both make SECTION K self-sufficient for a distinct audit dimension without requiring the reader to re-read phase bodies.

---

Simulate the adoption curve for {{topic}} across the 16 stock roles (PM, UX, C-01 through C-12, Support, SRE). Produce the artifact below in full. Every bracketed instruction is a fill contract — complete it before proceeding to the next section.

---

## STRUCTURAL CONTRACT

This document encodes two mandatory co-present architectural requirements. No variation or omission of either is permitted.

**REQUIREMENT 1 — ANSWER-FORM CITATION ENFORCEMENT (C-29):**
Named Inertia ID citations throughout this document are answers to explicit answer-form questions embedded in structural positions. The following questions are mandatory:

```
  Q-BARRIER:       "Which Named Inertia ID is the primary barrier here?
                    (Cite I-0X from SECTION A)"
  Q-CHAMPION:      "Named Inertia ID this champion is positioned to overcome:
                    (Cite I-0X from SECTION A)"
  Q-TRIGGER:       "Which Named Inertia ID drives reversion risk for this role?
                    (Cite I-0X from SECTION A)"
  Q-INTERVENTION:  "Which Named Inertia ID does this intervention directly target?
                    (Cite I-0X from SECTION A)"
```

**REQUIREMENT 2 — CORRECTION BLOCK MECHANISM STATE (C-32, C-34):**
A MECHANISM STATE line appears inside each of SECTIONS H, I, J (gate-level anchor) AND immediately before `## VERIFICATION MODE` (boundary-level anchor). Both anchors are mandatory regardless of gate outcomes.

Both requirements are mandatory co-present structural features.

---

## SECTION A — Named Inertia IDs

| Inertia ID | Archetype      | Named Inertia                      | Structural reason this archetype resists |
|------------|----------------|------------------------------------|------------------------------------------|
| I-01       | Innovator      | [name the inertia for Innovators]  | [structural reason]                      |
| I-02       | Early Adopter  | [name the inertia for EA]          | [structural reason]                      |
| I-03       | Early Majority | [name the inertia for EM]          | [structural reason]                      |
| I-04       | Late Majority  | [name the inertia for LM]          | [structural reason]                      |
| I-05       | Laggard        | [name the inertia for Laggards]    | [structural reason]                      |

### SECTION A — DOWNSTREAM CITATION CONTRACT

| Inertia ID | Mandatory downstream citation locations | Gate H Status |
|------------|-----------------------------------------|---------------|
| I-01 | PHASE 1 Q-BARRIER · PHASE 1 phase-close ledger · PART 3 Q-TRIGGER (Innovator-archetype role) | Gate H Status: [PASS / FAIL -- cite satisfied location, or cite violation] |
| I-02 | PHASE 2 Q-BARRIER · PHASE 2 phase-close ledger · PART 3 Q-TRIGGER (EA-archetype role) | Gate H Status: [PASS / FAIL -- cite satisfied location, or cite violation] |
| I-03 | PHASE 3 Q-BARRIER · PHASE 3 phase-close ledger · CHASM-A EXPANSION Named Inertia · CHASM-B EXPANSION Named Inertia · PHASE 4 Q-BARRIER · PHASE 4 phase-close ledger · at least one PART 5 Targets inertia: row | Gate H Status: [PASS / FAIL -- cite satisfied location, or cite violation] |
| I-04 | PHASE 5 Q-BARRIER · PHASE 5 phase-close ledger · PART 3 Q-TRIGGER (LM-archetype role) | Gate H Status: [PASS / FAIL -- cite satisfied location, or cite violation] |
| I-05 | PHASE 6 Q-BARRIER · PHASE 6 phase-close ledger · PART 3 Q-TRIGGER (Laggard-archetype role) | Gate H Status: [PASS / FAIL -- cite satisfied location, or cite violation] |

SECTION H audits against this contract row by row and fills Gate H Status. SECTION K records both gate execution stamps and citation contract completion status.

---

THE INCUMBENT is [name the current workflow, tool, or practice being displaced by {{topic}}].

---

## TABLE 1 — Role Archetype Map

| Role (SLOT-KEY typed slot) | Rogers Archetype | Incumbent Dependency: [workflow step this role relies on THE INCUMBENT to perform] | Inertia ID: [cite I-0X from SECTION A] |
|---|---|---|---|
| SLOT-KEY: PM      | | | |
| SLOT-KEY: UX      | | | |
| SLOT-KEY: C-01    | | | |
| SLOT-KEY: C-02    | | | |
| SLOT-KEY: C-03    | | | |
| SLOT-KEY: C-04    | | | |
| SLOT-KEY: C-05    | | | |
| SLOT-KEY: C-06    | | | |
| SLOT-KEY: C-07    | | | |
| SLOT-KEY: C-08    | | | |
| SLOT-KEY: C-09    | | | |
| SLOT-KEY: C-10    | | | |
| SLOT-KEY: C-11    | | | |
| SLOT-KEY: C-12    | | | |
| SLOT-KEY: Support | | | |
| SLOT-KEY: SRE     | | | |

---

## PHASE 1 INNOVATORS — Month 1

Displacement state at phase entry: THE INCUMBENT is fully entrenched — {{topic}} has not been introduced to any stock role. No displacement has occurred; all TABLE 1 Incumbent Dependency values are load-bearing.

Q-BARRIER: Which Named Inertia ID is the primary barrier even for Innovators?
(Cite I-01 from SECTION A)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [specific displacement state after Month 1]
Inertia ID this phase overcame (partially): [re-cite I-01]

---

## PHASE 2 EARLY ADOPTERS — Month 2–3

Displacement state at phase entry: [re-cite verbatim "Incumbent position after this phase:" from PHASE 1 close ledger]

Q-BARRIER: Which Named Inertia ID is the primary barrier for Early Adopters?
(Cite I-02 from SECTION A)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [specific displacement state after Month 3]
Inertia ID this phase overcame (partially): [re-cite I-02]

---

## PHASE 3 CHASM — Month 4 (Non-Adoption Crossing Event)

Displacement state entering PHASE 3: [re-cite verbatim "Incumbent position after this phase:" from PHASE 2 close ledger]

PHASE 3 is not an adoption phase. No new archetype adopts in Month 4.

Q-BARRIER: Which Named Inertia ID is driving the chasm?
(Cite I-03 from SECTION A)

### CHASM-A — Incumbent Defense

[Named incumbent defense mechanism]

### CHASM-B — Bridge Condition

[Bridge condition as testable proposition]

### CHASM-C — Early Crossing Signal

[First observable crossing signal]

**Phase-close displacement ledger:**
Inertia ID defending THE INCUMBENT at this boundary: [I-03]

---

## PHASE 4 EARLY MAJORITY — Month 5–7

Displacement state at phase entry: [re-cite PHASE 3 close state + what THE INCUMBENT still controlled entering Month 5]

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Early Majority?
(Cite I-03 from SECTION A)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [specific displacement state after Month 7]
Inertia ID this phase overcame (partially): [re-cite I-03]

---

## PHASE 5 LATE MAJORITY — Month 8–10

Displacement state at phase entry: [re-cite verbatim "Incumbent position after this phase:" from PHASE 4 close ledger]

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Late Majority?
(Cite I-04 from SECTION A)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [specific displacement state after Month 10]
Inertia ID this phase overcame (partially): [re-cite I-04]

---

## PHASE 6 LAGGARDS — Month 11–12

Displacement state at phase entry: [re-cite verbatim "Incumbent position after this phase:" from PHASE 5 close ledger]

Q-BARRIER: Which Named Inertia ID keeps Laggards last?
(Cite I-05 from SECTION A)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [terminal displacement state]
Inertia ID this phase overcame: [re-cite I-05]

---

## TABLE 3 — Spread Mechanisms

| Transition Pair (SLOT-KEY row) | Spread Mechanism: [named signal or artifact specific to {{topic}} — not generic word-of-mouth] | Month Range |
|---|---|---|
| SLOT-KEY: Innovator → Early Adopter      | | |
| SLOT-KEY: Early Adopter → Early Majority | | |
| SLOT-KEY: Early Majority → Late Majority | | |
| SLOT-KEY: Late Majority → Laggard        | | |

---

## PART 2 — CHASM ANALYSIS (Full Expansion)

### CHASM-A EXPANSION — Incumbent Defense (Full Diagnosis)

Expanding CHASM-A from PHASE 3 —
Named Inertia in effect: [re-cite I-03]
Incumbent position at this chasm element: [displacement state at incumbent-defense layer]

[Full diagnosis]

### CHASM-B EXPANSION — Bridge Condition (Full Specification)

Expanding CHASM-B from PHASE 3 —
Named Inertia in effect: [re-cite I-03]
Incumbent position at this chasm element: [displacement state at bridge-condition layer]

[Full specification]

### CHASM-C EXPANSION — Crossing Signal (Full Identification)

Expanding CHASM-C from PHASE 3 —
Named Inertia in effect: [re-cite I-03]
Incumbent position at this chasm element: [displacement state at crossing-signal moment]

[Full identification]

---

## PART 3 — Churn Risk Register

| Role (SLOT-KEY typed slot) | Reversion trigger | Retention intervention: [one concrete action — not a surveillance flag] | Q-TRIGGER: Which Named Inertia ID drives reversion risk? (Cite I-0X) |
|------|-----|-----|-----|
| SLOT-KEY: [Role] — churn entry | | | |

---

## PART 4 — Champion Network

| Champion Role (SLOT-KEY typed slot) | Archetype | Archetype-bridge rationale | Q-CHAMPION: Named Inertia ID this champion overcomes (I-0X) | Why this champion displaces THE INCUMBENT |
|---|---|---|---|---|
| SLOT-KEY: [Role] — champion entry | | | | |
| SLOT-KEY: [Role] — champion entry | | | | |
| SLOT-KEY: [Role] — champion entry | | | | |

---

## PART 5 — Intervention Ranking

| Rank | Intervention | Adoption delta | Phase(s) affected | Role(s) affected | Incumbent Impact | Targets inertia: [I-0X — Q-INTERVENTION] |
|------|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |

---

## PART 6 — Sensitivity Analysis

| Scenario      | Adoption outcome | Named lever | Direction of shift |
|---------------|------------------|-------------|-------------------|
| Fast Adoption |                  |             |                   |
| Slow Adoption |                  |             |                   |

---

## PART 7 — Signal Readiness Table

| Signal name | Threshold | Interpretation |
|-------------|-----------|----------------|
|             |           |                |

---

> CORRECTION BLOCK MECHANISM ARMED — no gate failure triggered. If any gate below fails, a CORRECTION BLOCK with BEFORE and AFTER fields will be inserted immediately above this line before proceeding to SECTION K.

## VERIFICATION MODE

All content generation is complete above this boundary. SECTIONS H, I, J, K are audit sections only.

---

## SECTION H — Gate: C-13 Audit

**Audit against DOWNSTREAM CITATION CONTRACT — fill Gate H Status per row:**

- I-01: PHASE 1 Q-BARRIER [Y/N] · ledger [Y/N] · PART 3 Q-TRIGGER Innovator [Y/N] → Fill SECTION A row I-01
- I-02: PHASE 2 Q-BARRIER [Y/N] · ledger [Y/N] · PART 3 Q-TRIGGER EA [Y/N] → Fill SECTION A row I-02
- I-03: PHASE 3 Q-BARRIER [Y/N] · ledger [Y/N] · CHASM-A [Y/N] · CHASM-B [Y/N] · PHASE 4 Q-BARRIER [Y/N] · PHASE 4 ledger [Y/N] · PART 5 [Y/N] → Fill SECTION A row I-03
- I-04: PHASE 5 Q-BARRIER [Y/N] · ledger [Y/N] · PART 3 Q-TRIGGER LM [Y/N] → Fill SECTION A row I-04
- I-05: PHASE 6 Q-BARRIER [Y/N] · ledger [Y/N] · PART 3 Q-TRIGGER Laggard [Y/N] → Fill SECTION A row I-05

**Gate H result:** [PASS / FAIL with specific I-0X and location if failing]

**Revision obligation:** If Gate H FAILS, produce CORRECTION BLOCK before pre-verification declaration. Do not proceed to SECTION I until written.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate H [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION I — Gate: C-14 Audit

- SLOT-KEY champion 1 [name]: archetype-bridge [Y/N] | Q-CHAMPION I-0X [Y/N]
- SLOT-KEY champion 2 [name]: archetype-bridge [Y/N] | Q-CHAMPION I-0X [Y/N]
- SLOT-KEY champion 3 [name]: archetype-bridge [Y/N] | Q-CHAMPION I-0X [Y/N]

**Gate I result:** [PASS / FAIL]

**Revision obligation:** If Gate I FAILS, produce CORRECTION BLOCK before pre-verification declaration.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate I [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION J — Gate: C-15 Audit

- [List each SLOT-KEY: churn entry and classification: concrete action or surveillance flag]

**Gate J result:** [PASS / FAIL]

**Revision obligation:** If Gate J FAILS, produce CORRECTION BLOCK before pre-verification declaration.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate J [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION K — Terminal Audit Record

**Terminal Invariant:** For every "Revision Performed: Yes" entry, a CORRECTION BLOCK with BEFORE and AFTER fields must exist at the cited location above the pre-verification declaration. A Yes entry whose cited location contains no CORRECTION BLOCK, or a CORRECTION BLOCK without a BEFORE field, falsifies this invariant.

| Gate | Criterion | Initial result | Revision performed | CORRECTION BLOCK location | Final result |
|------|-----------|----------------|--------------------|--------------------------|--------------|
| H    | C-13      |                | Yes / No           |                          |              |
| I    | C-14      |                | Yes / No           |                          |              |
| J    | C-15      |                | Yes / No           |                          |              |

**CITATION CONTRACT COMPLETION RECORD:**

| Inertia ID | Required sinks satisfied | Structural location found | Gate H Status |
|------------|--------------------------|--------------------------|---------------|
| I-01       |                          |                          |               |
| I-02       |                          |                          |               |
| I-03       |                          |                          |               |
| I-04       |                          |                          |               |
| I-05       |                          |                          |               |

**DISPLACEMENT ARC INTEGRITY CHECK (Axis B):**

For each phase-transition pair, record the exit-state text from the preceding close ledger and the entry-state text from the next phase opening field. A MATCH verdict confirms verbatim re-citation. A MISMATCH names the discontinuity.

| Transition | Exit state (from close ledger) | Entry state (from phase open) | Verdict |
|---|---|---|---|
| PHASE 1 close → PHASE 2 open | [Incumbent position after PHASE 1] | [Displacement state at PHASE 2 entry] | MATCH / MISMATCH |
| PHASE 2 close → PHASE 3 entry | [Incumbent position after PHASE 2] | [Displacement state entering PHASE 3] | MATCH / MISMATCH |
| PHASE 3 close → PHASE 4 open | [Inertia defending THE INCUMBENT at PHASE 3 boundary + context] | [Displacement state at PHASE 4 entry] | MATCH / MISMATCH |
| PHASE 4 close → PHASE 5 open | [Incumbent position after PHASE 4] | [Displacement state at PHASE 5 entry] | MATCH / MISMATCH |
| PHASE 5 close → PHASE 6 open | [Incumbent position after PHASE 5] | [Displacement state at PHASE 6 entry] | MATCH / MISMATCH |

Arc integrity: [PASS if all transitions MATCH | FAIL naming the specific discontinuity]

---

## V-03 — Single Axis: Inertia Framing (DOWNSTREAM CITATION CONTRACT Protected Behavior Column)

**Variation axis:** Inertia framing — each I-0X row in the SECTION A DOWNSTREAM CITATION CONTRACT carries an additional column: `Protected behavior: [the specific incumbent workflow, tool, or habit this inertia defends]`. Gate H fills the Gate H Status field as before; but now the audit record names the specific incumbent behavior each citation compliance decision affects. When SECTION K's C-51 mirror records I-04 as PASS or FAIL, it also records which Late Majority habit's displacement accountability the citation compliance was protecting. The protected behavior column is generated at SECTION A time — the model commits to what each inertia defends before writing any phase body — making the displacement stakes visible at the source rather than only discoverable through phase narratives.

**Hypothesis:** C-26 establishes THE INCUMBENT by name before archetype assignment; C-37 places Incumbent Dependency per role in TABLE 1; C-45 tracks THE INCUMBENT's displacement arc per phase close. But the link from each specific inertia ID to the specific incumbent behavior it defends lives only in SECTION A's structural-reason column — not in the citation contract. When Gate H audits contract row I-04 and finds a missing citation in PHASE 5 Q-BARRIER, the compliance record is "I-04: FAIL -- PHASE 5 Q-BARRIER missing." The Protected behavior column elevates this to: "I-04 -- Protected behavior: [specific Late Majority habit] -- FAIL: PHASE 5 Q-BARRIER missing." The audit record now names what is at risk of being unaddressed, not just which contract row was violated. SECTION K's C-51 mirror carries the same column, making the terminal audit a displacement-stakes certificate rather than a structural compliance certificate.

---

Simulate the adoption curve for {{topic}} across the 16 stock roles (PM, UX, C-01 through C-12, Support, SRE). Produce the artifact below in full. Every bracketed instruction is a fill contract — complete it before proceeding to the next section.

---

## STRUCTURAL CONTRACT

This document encodes two mandatory co-present architectural requirements. No variation or omission of either is permitted.

**REQUIREMENT 1 — ANSWER-FORM CITATION ENFORCEMENT (C-29):**

```
  Q-BARRIER:       "Which Named Inertia ID is the primary barrier here?
                    (Cite I-0X from SECTION A)"
  Q-CHAMPION:      "Named Inertia ID this champion is positioned to overcome:
                    (Cite I-0X from SECTION A)"
  Q-TRIGGER:       "Which Named Inertia ID drives reversion risk for this role?
                    (Cite I-0X from SECTION A)"
  Q-INTERVENTION:  "Which Named Inertia ID does this intervention directly target?
                    (Cite I-0X from SECTION A)"
```

**REQUIREMENT 2 — CORRECTION BLOCK MECHANISM STATE (C-32, C-34):**
MECHANISM STATE line inside each of SECTIONS H, I, J AND immediately before `## VERIFICATION MODE`. Both anchors mandatory regardless of gate outcomes.

---

## SECTION A — Named Inertia IDs

| Inertia ID | Archetype      | Named Inertia                      | Structural reason this archetype resists |
|------------|----------------|------------------------------------|------------------------------------------|
| I-01       | Innovator      | [name the inertia for Innovators]  | [structural reason]                      |
| I-02       | Early Adopter  | [name the inertia for EA]          | [structural reason]                      |
| I-03       | Early Majority | [name the inertia for EM]          | [structural reason]                      |
| I-04       | Late Majority  | [name the inertia for LM]          | [structural reason]                      |
| I-05       | Laggard        | [name the inertia for Laggards]    | [structural reason]                      |

### SECTION A — DOWNSTREAM CITATION CONTRACT

The Protected behavior column is filled at SECTION A generation time — before writing any phase body. It names the specific incumbent workflow, tool, or habit each inertia defends. Gate H fills the Gate H Status field at audit time. SECTION K's C-51 mirror carries both columns.

| Inertia ID | Mandatory downstream citation locations | Protected behavior: [specific incumbent behavior this inertia defends — fill at generation time] | Gate H Status |
|------------|-----------------------------------------|--------------------------------------------------------------------------------------------------|---------------|
| I-01 | PHASE 1 Q-BARRIER · PHASE 1 phase-close ledger · PART 3 Q-TRIGGER (Innovator-archetype role) | [fill: what THE INCUMBENT behavior/habit I-01 protects] | Gate H Status: [PASS / FAIL -- cite location or violation] |
| I-02 | PHASE 2 Q-BARRIER · PHASE 2 phase-close ledger · PART 3 Q-TRIGGER (EA-archetype role) | [fill: what THE INCUMBENT behavior/habit I-02 protects] | Gate H Status: [PASS / FAIL -- cite location or violation] |
| I-03 | PHASE 3 Q-BARRIER · PHASE 3 phase-close ledger · CHASM-A EXPANSION Named Inertia · CHASM-B EXPANSION Named Inertia · PHASE 4 Q-BARRIER · PHASE 4 phase-close ledger · at least one PART 5 Targets inertia: row | [fill: what THE INCUMBENT behavior/habit I-03 protects — the core EM workflow dependency] | Gate H Status: [PASS / FAIL -- cite location or violation] |
| I-04 | PHASE 5 Q-BARRIER · PHASE 5 phase-close ledger · PART 3 Q-TRIGGER (LM-archetype role) | [fill: what THE INCUMBENT behavior/habit I-04 protects] | Gate H Status: [PASS / FAIL -- cite location or violation] |
| I-05 | PHASE 6 Q-BARRIER · PHASE 6 phase-close ledger · PART 3 Q-TRIGGER (Laggard-archetype role) | [fill: what THE INCUMBENT behavior/habit I-05 protects] | Gate H Status: [PASS / FAIL -- cite location or violation] |

SECTION H fills Gate H Status and names which Protected behavior remains unaddressed for any FAIL row. SECTION K CITATION CONTRACT COMPLETION RECORD carries the Protected behavior column.

---

THE INCUMBENT is [name the current workflow, tool, or practice being displaced by {{topic}}].

---

## TABLE 1 — Role Archetype Map

| Role (SLOT-KEY typed slot) | Rogers Archetype | Incumbent Dependency: [workflow step this role relies on THE INCUMBENT to perform] | Inertia ID: [cite I-0X from SECTION A] |
|---|---|---|---|
| SLOT-KEY: PM      | | | |
| SLOT-KEY: UX      | | | |
| SLOT-KEY: C-01    | | | |
| SLOT-KEY: C-02    | | | |
| SLOT-KEY: C-03    | | | |
| SLOT-KEY: C-04    | | | |
| SLOT-KEY: C-05    | | | |
| SLOT-KEY: C-06    | | | |
| SLOT-KEY: C-07    | | | |
| SLOT-KEY: C-08    | | | |
| SLOT-KEY: C-09    | | | |
| SLOT-KEY: C-10    | | | |
| SLOT-KEY: C-11    | | | |
| SLOT-KEY: C-12    | | | |
| SLOT-KEY: Support | | | |
| SLOT-KEY: SRE     | | | |

---

## PHASE 1 INNOVATORS — Month 1

Displacement state at phase entry: THE INCUMBENT is fully entrenched. No displacement has occurred. All TABLE 1 Incumbent Dependency values are load-bearing; all Protected behavior declarations in the DOWNSTREAM CITATION CONTRACT are fully active.

Q-BARRIER: Which Named Inertia ID is the primary barrier even for Innovators?
(Cite I-01 from SECTION A — what Protected behavior from the contract row I-01 does this archetype most tightly hold?)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [specific displacement state — which Protected behaviors from I-01's contract row begin to weaken]
Inertia ID this phase overcame (partially): [re-cite I-01]

---

## PHASE 2 EARLY ADOPTERS — Month 2–3

Displacement state at phase entry: [re-cite verbatim PHASE 1 "Incumbent position after this phase:"]

Q-BARRIER: Which Named Inertia ID is the primary barrier for Early Adopters?
(Cite I-02 from SECTION A — what Protected behavior from contract row I-02 resists these roles?)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [specific displacement state]
Inertia ID this phase overcame (partially): [re-cite I-02]

---

## PHASE 3 CHASM — Month 4 (Non-Adoption Crossing Event)

Displacement state entering PHASE 3: [re-cite verbatim PHASE 2 "Incumbent position after this phase:"]

PHASE 3 is not an adoption phase. No new archetype adopts in Month 4.

Q-BARRIER: Which Named Inertia ID is driving the chasm?
(Cite I-03 from SECTION A — what Protected behavior from contract row I-03 makes the chasm structural rather than temporal?)

### CHASM-A — Incumbent Defense

[Named incumbent defense mechanism — explicitly connects to Protected behavior declared for I-03 in SECTION A]

### CHASM-B — Bridge Condition

[Bridge condition as testable proposition]

### CHASM-C — Early Crossing Signal

[First observable crossing signal]

**Phase-close displacement ledger:**
Inertia ID defending THE INCUMBENT at this boundary: [I-03 — and its Protected behavior from SECTION A contract row]

---

## PHASE 4 EARLY MAJORITY — Month 5–7

Displacement state at phase entry: [re-cite PHASE 3 close + what THE INCUMBENT still controlled entering Month 5]

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Early Majority?
(Cite I-03 — Protected behavior from contract row I-03 still active for these roles despite chasm crossing)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [specific displacement state]
Inertia ID this phase overcame (partially): [re-cite I-03]

---

## PHASE 5 LATE MAJORITY — Month 8–10

Displacement state at phase entry: [re-cite verbatim PHASE 4 "Incumbent position after this phase:"]

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Late Majority?
(Cite I-04 — what Protected behavior from contract row I-04 holds these roles back?)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [specific displacement state]
Inertia ID this phase overcame (partially): [re-cite I-04]

---

## PHASE 6 LAGGARDS — Month 11–12

Displacement state at phase entry: [re-cite verbatim PHASE 5 "Incumbent position after this phase:"]

Q-BARRIER: Which Named Inertia ID keeps Laggards last?
(Cite I-05 — what Protected behavior from contract row I-05 is the final holdout?)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [terminal displacement state — which Protected behaviors, if any, persist past Month 12]
Inertia ID this phase overcame: [re-cite I-05]

---

## TABLE 3 — Spread Mechanisms

| Transition Pair (SLOT-KEY row) | Spread Mechanism: [named signal or artifact specific to {{topic}} — not generic word-of-mouth] | Month Range |
|---|---|---|
| SLOT-KEY: Innovator → Early Adopter      | | |
| SLOT-KEY: Early Adopter → Early Majority | | |
| SLOT-KEY: Early Majority → Late Majority | | |
| SLOT-KEY: Late Majority → Laggard        | | |

---

## PART 2 — CHASM ANALYSIS (Full Expansion)

### CHASM-A EXPANSION — Incumbent Defense (Full Diagnosis)

Expanding CHASM-A from PHASE 3 —
Named Inertia in effect: [re-cite I-03]
Incumbent position at this chasm element: [displacement state at incumbent-defense layer]

[Full diagnosis — names the specific Protected behavior from SECTION A contract row I-03 that is load-bearing at this element]

### CHASM-B EXPANSION — Bridge Condition (Full Specification)

Expanding CHASM-B from PHASE 3 —
Named Inertia in effect: [re-cite I-03]
Incumbent position at this chasm element: [displacement state at bridge-condition layer]

[Full specification]

### CHASM-C EXPANSION — Crossing Signal (Full Identification)

Expanding CHASM-C from PHASE 3 —
Named Inertia in effect: [re-cite I-03]
Incumbent position at this chasm element: [displacement state at crossing-signal moment — what Protected behavior from I-03 row weakens at this signal]

[Full identification]

---

## PART 3 — Churn Risk Register

| Role (SLOT-KEY typed slot) | Reversion trigger: [condition causing reversion to THE INCUMBENT — name the Protected behavior from SECTION A being re-activated] | Retention intervention: [one concrete action — not a surveillance flag] | Q-TRIGGER: Named Inertia ID driving reversion (I-0X) |
|------|-----|-----|-----|
| SLOT-KEY: [Role] — churn entry | | | |

---

## PART 4 — Champion Network

| Champion Role (SLOT-KEY typed slot) | Archetype | Archetype-bridge rationale | Q-CHAMPION: Named Inertia ID this champion overcomes (I-0X) | Why this champion displaces the Protected behavior from the I-0X contract row |
|---|---|---|---|---|
| SLOT-KEY: [Role] — champion entry | | | | |
| SLOT-KEY: [Role] — champion entry | | | | |
| SLOT-KEY: [Role] — champion entry | | | | |

---

## PART 5 — Intervention Ranking

| Rank | Intervention | Adoption delta | Phase(s) | Role(s) | Incumbent Impact | Targets inertia: [I-0X — names the Protected behavior this intervention displaces] |
|------|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |

---

## PART 6 — Sensitivity Analysis

| Scenario      | Adoption outcome | Named lever | Direction of shift |
|---------------|------------------|-------------|-------------------|
| Fast Adoption |                  |             |                   |
| Slow Adoption |                  |             |                   |

---

## PART 7 — Signal Readiness Table

| Signal name | Threshold | Interpretation |
|-------------|-----------|----------------|
|             |           |                |

---

> CORRECTION BLOCK MECHANISM ARMED — no gate failure triggered. If any gate below fails, a CORRECTION BLOCK with BEFORE and AFTER fields will be inserted immediately above this line before proceeding to SECTION K.

## VERIFICATION MODE

All content generation is complete above this boundary. SECTIONS H, I, J, K are audit sections only.

---

## SECTION H — Gate: C-13 Audit

**Audit against DOWNSTREAM CITATION CONTRACT — fill Gate H Status AND note Protected behavior at risk for any FAIL row:**

- I-01 [Protected behavior: see SECTION A]: PHASE 1 Q-BARRIER [Y/N] · ledger [Y/N] · PART 3 Q-TRIGGER Innovator [Y/N] → Fill SECTION A row I-01 Gate H Status + note Protected behavior if FAIL
- I-02 [Protected behavior: see SECTION A]: PHASE 2 Q-BARRIER [Y/N] · ledger [Y/N] · PART 3 Q-TRIGGER EA [Y/N] → Fill SECTION A row I-02
- I-03 [Protected behavior: see SECTION A]: PHASE 3 Q-BARRIER [Y/N] · ledger [Y/N] · CHASM-A [Y/N] · CHASM-B [Y/N] · PHASE 4 Q-BARRIER [Y/N] · PHASE 4 ledger [Y/N] · PART 5 [Y/N] → Fill SECTION A row I-03
- I-04 [Protected behavior: see SECTION A]: PHASE 5 Q-BARRIER [Y/N] · ledger [Y/N] · PART 3 Q-TRIGGER LM [Y/N] → Fill SECTION A row I-04
- I-05 [Protected behavior: see SECTION A]: PHASE 6 Q-BARRIER [Y/N] · ledger [Y/N] · PART 3 Q-TRIGGER Laggard [Y/N] → Fill SECTION A row I-05

**Gate H result:** [PASS / FAIL — for any FAIL, state: "I-0X [Protected behavior: ...] missing citation at [location]"]

**Revision obligation:** If Gate H FAILS, produce CORRECTION BLOCK before pre-verification declaration.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate H [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION I — Gate: C-14 Audit

- SLOT-KEY champion 1 [name]: archetype-bridge [Y/N] | Q-CHAMPION I-0X [Y/N]
- SLOT-KEY champion 2 [name]: archetype-bridge [Y/N] | Q-CHAMPION I-0X [Y/N]
- SLOT-KEY champion 3 [name]: archetype-bridge [Y/N] | Q-CHAMPION I-0X [Y/N]

**Gate I result:** [PASS / FAIL]

**Revision obligation:** If Gate I FAILS, produce CORRECTION BLOCK before pre-verification declaration.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate I [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION J — Gate: C-15 Audit

- [List each SLOT-KEY: churn entry and classification]

**Gate J result:** [PASS / FAIL]

**Revision obligation:** If Gate J FAILS, produce CORRECTION BLOCK before pre-verification declaration.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate J [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION K — Terminal Audit Record

**Terminal Invariant:** For every "Revision Performed: Yes," a CORRECTION BLOCK with BEFORE and AFTER fields must exist at the cited location above the pre-verification declaration. A Yes entry without a matching CORRECTION BLOCK, or a CORRECTION BLOCK without a BEFORE field, falsifies this invariant.

| Gate | Criterion | Initial result | Revision performed | CORRECTION BLOCK location | Final result |
|------|-----------|----------------|--------------------|--------------------------|--------------|
| H    | C-13      |                | Yes / No           |                          |              |
| I    | C-14      |                | Yes / No           |                          |              |
| J    | C-15      |                | Yes / No           |                          |              |

**CITATION CONTRACT COMPLETION RECORD (with Protected behavior column — Axis C):**

| Inertia ID | Protected behavior (from SECTION A) | Required sinks satisfied | Structural location found | Gate H Status |
|------------|-------------------------------------|--------------------------|--------------------------|---------------|
| I-01       |                                     |                          |                          |               |
| I-02       |                                     |                          |                          |               |
| I-03       |                                     |                          |                          |               |
| I-04       |                                     |                          |                          |               |
| I-05       |                                     |                          |                          |               |

---

## V-04 — Combined: Lifecycle Emphasis + Inertia Framing (Axes A + C)

**Variation axes:** Axis A (per-I-0X correction obligation) + Axis C (Protected behavior column in DOWNSTREAM CITATION CONTRACT).

**Hypothesis:** Axis A makes the repair record as granular as the citation contract: each failed I-0X row produces its own labeled CORRECTION BLOCK. Axis C makes the audit record name the displacement stakes: each contract row carries the specific Protected behavior at risk. The combination means that when Gate H fires a per-I-0X CORRECTION BLOCK for I-04, the correction block is labeled not only "I-04: PHASE 5 Q-BARRIER missing" but implicitly addresses the Protected behavior declared in the I-04 contract row — the displacement-stakes context is visible at the repair site. The repair is no longer just a structural compliance correction; it is a targeted displacement-commitment repair. Axis A makes correction granularity match citation granularity; Axis C makes displacement stakes visible at the citation source; together they make displacement-stakes visible at the correction site.

---

Simulate the adoption curve for {{topic}} across the 16 stock roles (PM, UX, C-01 through C-12, Support, SRE). Produce the artifact below in full. Every bracketed instruction is a fill contract — complete it before proceeding to the next section.

---

## STRUCTURAL CONTRACT

This document encodes two mandatory co-present architectural requirements. No variation or omission of either is permitted.

**REQUIREMENT 1 — ANSWER-FORM CITATION ENFORCEMENT (C-29):**

```
  Q-BARRIER:       "Which Named Inertia ID is the primary barrier here?
                    (Cite I-0X from SECTION A)"
  Q-CHAMPION:      "Named Inertia ID this champion is positioned to overcome:
                    (Cite I-0X from SECTION A)"
  Q-TRIGGER:       "Which Named Inertia ID drives reversion risk for this role?
                    (Cite I-0X from SECTION A)"
  Q-INTERVENTION:  "Which Named Inertia ID does this intervention directly target?
                    (Cite I-0X from SECTION A)"
```

**REQUIREMENT 2 — CORRECTION BLOCK MECHANISM STATE (C-32, C-34):**
MECHANISM STATE line inside each of SECTIONS H, I, J AND immediately before `## VERIFICATION MODE`. Both anchors mandatory regardless of gate outcomes.

---

## SECTION A — Named Inertia IDs

| Inertia ID | Archetype      | Named Inertia                      | Structural reason this archetype resists |
|------------|----------------|------------------------------------|------------------------------------------|
| I-01       | Innovator      | [name the inertia for Innovators]  | [structural reason]                      |
| I-02       | Early Adopter  | [name the inertia for EA]          | [structural reason]                      |
| I-03       | Early Majority | [name the inertia for EM]          | [structural reason]                      |
| I-04       | Late Majority  | [name the inertia for LM]          | [structural reason]                      |
| I-05       | Laggard        | [name the inertia for Laggards]    | [structural reason]                      |

### SECTION A — DOWNSTREAM CITATION CONTRACT

Protected behavior column is filled at SECTION A generation time. Gate H Status is filled at audit time. For any FAIL row, Gate H fires a dedicated CORRECTION BLOCK labeled by the specific I-0X (Axis A). SECTION K CITATION CONTRACT COMPLETION RECORD carries both Protected behavior and Gate H Status (Axis C).

| Inertia ID | Mandatory downstream citation locations | Protected behavior: [specific incumbent behavior this inertia defends — fill at generation time] | Gate H Status |
|------------|-----------------------------------------|--------------------------------------------------------------------------------------------------|---------------|
| I-01 | PHASE 1 Q-BARRIER · PHASE 1 phase-close ledger · PART 3 Q-TRIGGER (Innovator-archetype role) | [fill: Protected behavior for I-01] | Gate H Status: [PASS / FAIL -- cite location or violation] |
| I-02 | PHASE 2 Q-BARRIER · PHASE 2 phase-close ledger · PART 3 Q-TRIGGER (EA-archetype role) | [fill: Protected behavior for I-02] | Gate H Status: [PASS / FAIL -- cite location or violation] |
| I-03 | PHASE 3 Q-BARRIER · PHASE 3 phase-close ledger · CHASM-A EXPANSION Named Inertia · CHASM-B EXPANSION Named Inertia · PHASE 4 Q-BARRIER · PHASE 4 phase-close ledger · at least one PART 5 Targets inertia: row | [fill: Protected behavior for I-03] | Gate H Status: [PASS / FAIL -- cite location or violation] |
| I-04 | PHASE 5 Q-BARRIER · PHASE 5 phase-close ledger · PART 3 Q-TRIGGER (LM-archetype role) | [fill: Protected behavior for I-04] | Gate H Status: [PASS / FAIL -- cite location or violation] |
| I-05 | PHASE 6 Q-BARRIER · PHASE 6 phase-close ledger · PART 3 Q-TRIGGER (Laggard-archetype role) | [fill: Protected behavior for I-05] | Gate H Status: [PASS / FAIL -- cite location or violation] |

**Per-I-0X correction obligation (Axis A):** If Gate H records FAIL for any contract row, produce a dedicated CORRECTION BLOCK immediately before the pre-verification declaration, labeled `CORRECTION BLOCK — I-0X [Protected behavior: ...]: [missed location]`. Each failed row produces its own labeled block; the label includes the Protected behavior from the contract row, connecting the structural repair to the displacement commitment it addresses.

---

THE INCUMBENT is [name the current workflow, tool, or practice being displaced by {{topic}}].

---

## TABLE 1 — Role Archetype Map

| Role (SLOT-KEY typed slot) | Rogers Archetype | Incumbent Dependency: [workflow step this role relies on THE INCUMBENT to perform] | Inertia ID: [cite I-0X from SECTION A] |
|---|---|---|---|
| SLOT-KEY: PM      | | | |
| SLOT-KEY: UX      | | | |
| SLOT-KEY: C-01    | | | |
| SLOT-KEY: C-02    | | | |
| SLOT-KEY: C-03    | | | |
| SLOT-KEY: C-04    | | | |
| SLOT-KEY: C-05    | | | |
| SLOT-KEY: C-06    | | | |
| SLOT-KEY: C-07    | | | |
| SLOT-KEY: C-08    | | | |
| SLOT-KEY: C-09    | | | |
| SLOT-KEY: C-10    | | | |
| SLOT-KEY: C-11    | | | |
| SLOT-KEY: C-12    | | | |
| SLOT-KEY: Support | | | |
| SLOT-KEY: SRE     | | | |

---

## PHASE 1 INNOVATORS — Month 1

Displacement state at phase entry: THE INCUMBENT is fully entrenched. All TABLE 1 Incumbent Dependency values load-bearing; all Protected behaviors in SECTION A DOWNSTREAM CITATION CONTRACT fully active.

Q-BARRIER: Which Named Inertia ID is the primary barrier even for Innovators?
(Cite I-01 — what Protected behavior from SECTION A contract row I-01 do Innovators hold most tightly?)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [which Protected behaviors from I-01's contract row begin to weaken]
Inertia ID this phase overcame (partially): [re-cite I-01]

---

## PHASE 2 EARLY ADOPTERS — Month 2–3

Displacement state at phase entry: [re-cite verbatim PHASE 1 "Incumbent position after this phase:"]

Q-BARRIER: Which Named Inertia ID is the primary barrier for Early Adopters?
(Cite I-02 — Protected behavior from SECTION A contract row I-02)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [specific displacement state]
Inertia ID this phase overcame (partially): [re-cite I-02]

---

## PHASE 3 CHASM — Month 4 (Non-Adoption Crossing Event)

Displacement state entering PHASE 3: [re-cite verbatim PHASE 2 "Incumbent position after this phase:"]

PHASE 3 is not an adoption phase. No new archetype adopts in Month 4.

Q-BARRIER: Which Named Inertia ID is driving the chasm?
(Cite I-03 — what Protected behavior from SECTION A contract row I-03 makes this chasm structural?)

### CHASM-A — Incumbent Defense

[Named defense mechanism — explicitly connects to Protected behavior declared for I-03]

### CHASM-B — Bridge Condition

[Bridge condition as testable proposition]

### CHASM-C — Early Crossing Signal

[First observable crossing signal]

**Phase-close displacement ledger:**
Inertia ID defending THE INCUMBENT at this boundary: [I-03 and its Protected behavior from SECTION A]

---

## PHASE 4 EARLY MAJORITY — Month 5–7

Displacement state at phase entry: [re-cite PHASE 3 close state + what THE INCUMBENT still controlled entering Month 5]

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Early Majority?
(Cite I-03 — Protected behavior still active for these roles)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [specific displacement state]
Inertia ID this phase overcame (partially): [re-cite I-03]

---

## PHASE 5 LATE MAJORITY — Month 8–10

Displacement state at phase entry: [re-cite verbatim PHASE 4 "Incumbent position after this phase:"]

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Late Majority?
(Cite I-04 — Protected behavior from SECTION A contract row I-04)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [specific displacement state]
Inertia ID this phase overcame (partially): [re-cite I-04]

---

## PHASE 6 LAGGARDS — Month 11–12

Displacement state at phase entry: [re-cite verbatim PHASE 5 "Incumbent position after this phase:"]

Q-BARRIER: Which Named Inertia ID keeps Laggards last?
(Cite I-05 — Protected behavior from SECTION A contract row I-05 as final holdout)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [terminal displacement state — which Protected behaviors persist past Month 12]
Inertia ID this phase overcame: [re-cite I-05]

---

## TABLE 3 — Spread Mechanisms

| Transition Pair (SLOT-KEY row) | Spread Mechanism: [named signal or artifact specific to {{topic}} — not generic word-of-mouth] | Month Range |
|---|---|---|
| SLOT-KEY: Innovator → Early Adopter      | | |
| SLOT-KEY: Early Adopter → Early Majority | | |
| SLOT-KEY: Early Majority → Late Majority | | |
| SLOT-KEY: Late Majority → Laggard        | | |

---

## PART 2 — CHASM ANALYSIS (Full Expansion)

### CHASM-A EXPANSION — Incumbent Defense (Full Diagnosis)

Expanding CHASM-A from PHASE 3 —
Named Inertia in effect: [re-cite I-03]
Incumbent position at this chasm element: [displacement state — which Protected behavior from I-03 contract row is load-bearing here]

[Full diagnosis]

### CHASM-B EXPANSION — Bridge Condition (Full Specification)

Expanding CHASM-B from PHASE 3 —
Named Inertia in effect: [re-cite I-03]
Incumbent position at this chasm element: [displacement state — which Protected behavior unblocks when bridge condition is satisfied]

[Full specification]

### CHASM-C EXPANSION — Crossing Signal (Full Identification)

Expanding CHASM-C from PHASE 3 —
Named Inertia in effect: [re-cite I-03]
Incumbent position at this chasm element: [displacement state — which Protected behavior weakens at the crossing signal moment]

[Full identification]

---

## PART 3 — Churn Risk Register

| Role (SLOT-KEY typed slot) | Reversion trigger: [names the Protected behavior from SECTION A being re-activated] | Retention intervention: [one concrete action — not a surveillance flag] | Q-TRIGGER: Named Inertia ID driving reversion (I-0X) |
|------|-----|-----|-----|
| SLOT-KEY: [Role] — churn entry | | | |

---

## PART 4 — Champion Network

| Champion Role (SLOT-KEY typed slot) | Archetype | Archetype-bridge rationale | Q-CHAMPION: Named Inertia ID this champion overcomes (I-0X) | Why this champion displaces the Protected behavior from the I-0X contract row |
|---|---|---|---|---|
| SLOT-KEY: [Role] — champion entry | | | | |
| SLOT-KEY: [Role] — champion entry | | | | |
| SLOT-KEY: [Role] — champion entry | | | | |

---

## PART 5 — Intervention Ranking

| Rank | Intervention | Adoption delta | Phase(s) | Role(s) | Incumbent Impact | Targets inertia: [I-0X — names the Protected behavior this intervention displaces] |
|------|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |

---

## PART 6 — Sensitivity Analysis

| Scenario      | Adoption outcome | Named lever | Direction of shift |
|---------------|------------------|-------------|-------------------|
| Fast Adoption |                  |             |                   |
| Slow Adoption |                  |             |                   |

---

## PART 7 — Signal Readiness Table

| Signal name | Threshold | Interpretation |
|-------------|-----------|----------------|
|             |           |                |

---

> CORRECTION BLOCK MECHANISM ARMED — no gate failure triggered. If any gate below fails, a CORRECTION BLOCK with BEFORE and AFTER fields will be inserted immediately above this line. Under this variation, a Gate H contract-row FAIL produces a separately labeled CORRECTION BLOCK per failed I-0X row, with the label including the Protected behavior from that contract row.

## VERIFICATION MODE

All content generation is complete above this boundary. SECTIONS H, I, J, K are audit sections only.

---

## SECTION H — Gate: C-13 Audit

**Audit against DOWNSTREAM CITATION CONTRACT — fill Gate H Status per row; for any FAIL, name the Protected behavior left unaddressed:**

- I-01 [Protected behavior: see SECTION A]: PHASE 1 Q-BARRIER [Y/N] · ledger [Y/N] · PART 3 Q-TRIGGER Innovator [Y/N] → Fill SECTION A row I-01
- I-02 [Protected behavior: see SECTION A]: PHASE 2 Q-BARRIER [Y/N] · ledger [Y/N] · PART 3 Q-TRIGGER EA [Y/N] → Fill SECTION A row I-02
- I-03 [Protected behavior: see SECTION A]: PHASE 3 Q-BARRIER [Y/N] · ledger [Y/N] · CHASM-A [Y/N] · CHASM-B [Y/N] · PHASE 4 Q-BARRIER [Y/N] · PHASE 4 ledger [Y/N] · PART 5 [Y/N] → Fill SECTION A row I-03
- I-04 [Protected behavior: see SECTION A]: PHASE 5 Q-BARRIER [Y/N] · ledger [Y/N] · PART 3 Q-TRIGGER LM [Y/N] → Fill SECTION A row I-04
- I-05 [Protected behavior: see SECTION A]: PHASE 6 Q-BARRIER [Y/N] · ledger [Y/N] · PART 3 Q-TRIGGER Laggard [Y/N] → Fill SECTION A row I-05

**Gate H result:** [PASS / FAIL — for any FAIL: "I-0X [Protected behavior: ...] missing citation at [location]"]

**Per-I-0X revision obligation (Axis A):** If any contract row shows FAIL, produce a dedicated CORRECTION BLOCK for each failed row immediately before the pre-verification declaration: `CORRECTION BLOCK — I-0X [Protected behavior: ...]: [missed location] — BEFORE: [...] — AFTER: [...]`. Each failed I-0X row produces its own block.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate H [PASS: no per-I-0X correction triggered | FAIL: per-I-0X CORRECTION BLOCK(s) written above pre-verification line]

---

## SECTION I — Gate: C-14 Audit

- SLOT-KEY champion 1 [name]: archetype-bridge [Y/N] | Q-CHAMPION I-0X [Y/N]
- SLOT-KEY champion 2 [name]: archetype-bridge [Y/N] | Q-CHAMPION I-0X [Y/N]
- SLOT-KEY champion 3 [name]: archetype-bridge [Y/N] | Q-CHAMPION I-0X [Y/N]

**Gate I result:** [PASS / FAIL]

**Revision obligation:** If Gate I FAILS, produce CORRECTION BLOCK before pre-verification declaration.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate I [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION J — Gate: C-15 Audit

- [List each SLOT-KEY: churn entry and classification]

**Gate J result:** [PASS / FAIL]

**Revision obligation:** If Gate J FAILS, produce CORRECTION BLOCK before pre-verification declaration.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate J [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION K — Terminal Audit Record

**Terminal Invariant:** For every "Revision Performed: Yes," a CORRECTION BLOCK with BEFORE and AFTER fields must exist at the cited location. Under this variation, Gate H failures produce per-I-0X labeled blocks; "Revision Performed: Yes" for Gate H cites all produced block locations.

| Gate | Criterion | Initial result | Revision performed | CORRECTION BLOCK location | Final result |
|------|-----------|----------------|--------------------|--------------------------|--------------|
| H    | C-13      |                | Yes / No           |                          |              |
| I    | C-14      |                | Yes / No           |                          |              |
| J    | C-15      |                | Yes / No           |                          |              |

**CITATION CONTRACT COMPLETION RECORD (with Protected behavior column — Axis C):**

| Inertia ID | Protected behavior (from SECTION A) | Required sinks satisfied | Structural location found | Gate H Status |
|------------|-------------------------------------|--------------------------|--------------------------|---------------|
| I-01       |                                     |                          |                          |               |
| I-02       |                                     |                          |                          |               |
| I-03       |                                     |                          |                          |               |
| I-04       |                                     |                          |                          |               |
| I-05       |                                     |                          |                          |               |

---

## V-05 — Full: Lifecycle Emphasis + Output Format + Inertia Framing (Axes A + B + C)

**Variation axes:** All three — Axis A (per-I-0X correction obligation) + Axis B (SECTION K Displacement Arc Integrity Check) + Axis C (Protected behavior column).

**Hypothesis:** The three axes address three distinct audit gaps that survive R17 V-05. Axis A makes correction granularity match citation granularity: one repair per failed I-0X, not one repair per gate. Axis B makes displacement arc continuity terminally auditable: SECTION K proves the phase-open/phase-close chain was internally consistent without requiring phase body re-reads. Axis C makes displacement stakes visible at the citation source and audit record: each contract row names what it is protecting, and SECTION K's completion record carries that context. Together, SECTION K becomes sufficient for three independent audit dimensions: gate execution proof (C-30), citation contract compliance (C-51), and displacement arc continuity (Axis B) — while SECTION A becomes sufficient as both citation source and displacement-stakes declaration. The full variation tests whether all three enhancements are structurally compatible and whether their combined presence introduces any new interactions (e.g., whether per-I-0X correction blocks labeled with Protected behavior create additional audit burden in SECTION K).

---

Simulate the adoption curve for {{topic}} across the 16 stock roles (PM, UX, C-01 through C-12, Support, SRE). Produce the artifact below in full. Every bracketed instruction is a fill contract — complete it before proceeding to the next section.

---

## STRUCTURAL CONTRACT

This document encodes two mandatory co-present architectural requirements. No variation or omission of either is permitted.

**REQUIREMENT 1 — ANSWER-FORM CITATION ENFORCEMENT (C-29):**

```
  Q-BARRIER:       "Which Named Inertia ID is the primary barrier here?
                    (Cite I-0X from SECTION A)"
  Q-CHAMPION:      "Named Inertia ID this champion is positioned to overcome:
                    (Cite I-0X from SECTION A)"
  Q-TRIGGER:       "Which Named Inertia ID drives reversion risk for this role?
                    (Cite I-0X from SECTION A)"
  Q-INTERVENTION:  "Which Named Inertia ID does this intervention directly target?
                    (Cite I-0X from SECTION A)"
```

**REQUIREMENT 2 — CORRECTION BLOCK MECHANISM STATE (C-32, C-34):**
MECHANISM STATE line inside each of SECTIONS H, I, J AND immediately before `## VERIFICATION MODE`. Both anchors mandatory regardless of gate outcomes.

---

## SECTION A — Named Inertia IDs

| Inertia ID | Archetype      | Named Inertia                      | Structural reason this archetype resists |
|------------|----------------|------------------------------------|------------------------------------------|
| I-01       | Innovator      | [name the inertia for Innovators]  | [structural reason]                      |
| I-02       | Early Adopter  | [name the inertia for EA]          | [structural reason]                      |
| I-03       | Early Majority | [name the inertia for EM]          | [structural reason]                      |
| I-04       | Late Majority  | [name the inertia for LM]          | [structural reason]                      |
| I-05       | Laggard        | [name the inertia for Laggards]    | [structural reason]                      |

### SECTION A — DOWNSTREAM CITATION CONTRACT

Protected behavior column is filled at SECTION A generation time — before writing any phase body. Gate H Status is filled at audit time. For any FAIL row, Gate H fires a dedicated per-I-0X CORRECTION BLOCK labeled with the I-0X and its Protected behavior (Axis A). SECTION K CITATION CONTRACT COMPLETION RECORD carries Protected behavior and Gate H Status alongside the displacement arc check (Axes B and C).

| Inertia ID | Mandatory downstream citation locations | Protected behavior: [specific incumbent behavior this inertia defends — fill at generation time] | Gate H Status |
|------------|-----------------------------------------|--------------------------------------------------------------------------------------------------|---------------|
| I-01 | PHASE 1 Q-BARRIER · PHASE 1 phase-close ledger · PART 3 Q-TRIGGER (Innovator-archetype role) | [fill: Protected behavior for I-01] | Gate H Status: [PASS / FAIL -- cite location or violation] |
| I-02 | PHASE 2 Q-BARRIER · PHASE 2 phase-close ledger · PART 3 Q-TRIGGER (EA-archetype role) | [fill: Protected behavior for I-02] | Gate H Status: [PASS / FAIL -- cite location or violation] |
| I-03 | PHASE 3 Q-BARRIER · PHASE 3 phase-close ledger · CHASM-A EXPANSION Named Inertia · CHASM-B EXPANSION Named Inertia · PHASE 4 Q-BARRIER · PHASE 4 phase-close ledger · at least one PART 5 Targets inertia: row | [fill: Protected behavior for I-03] | Gate H Status: [PASS / FAIL -- cite location or violation] |
| I-04 | PHASE 5 Q-BARRIER · PHASE 5 phase-close ledger · PART 3 Q-TRIGGER (LM-archetype role) | [fill: Protected behavior for I-04] | Gate H Status: [PASS / FAIL -- cite location or violation] |
| I-05 | PHASE 6 Q-BARRIER · PHASE 6 phase-close ledger · PART 3 Q-TRIGGER (Laggard-archetype role) | [fill: Protected behavior for I-05] | Gate H Status: [PASS / FAIL -- cite location or violation] |

**Per-I-0X correction obligation (Axis A):** If Gate H records FAIL for any contract row, produce a dedicated CORRECTION BLOCK for that row immediately before the pre-verification declaration: `CORRECTION BLOCK — I-0X [Protected behavior: ...]: [missed location] — BEFORE: [...] — AFTER: [...]`. Each failed row produces its own block. Separate blocks for each failed I-0X are mandatory.

---

THE INCUMBENT is [name the current workflow, tool, or practice being displaced by {{topic}}].

---

## TABLE 1 — Role Archetype Map

| Role (SLOT-KEY typed slot) | Rogers Archetype | Incumbent Dependency: [workflow step this role relies on THE INCUMBENT to perform] | Inertia ID: [cite I-0X from SECTION A] |
|---|---|---|---|
| SLOT-KEY: PM      | | | |
| SLOT-KEY: UX      | | | |
| SLOT-KEY: C-01    | | | |
| SLOT-KEY: C-02    | | | |
| SLOT-KEY: C-03    | | | |
| SLOT-KEY: C-04    | | | |
| SLOT-KEY: C-05    | | | |
| SLOT-KEY: C-06    | | | |
| SLOT-KEY: C-07    | | | |
| SLOT-KEY: C-08    | | | |
| SLOT-KEY: C-09    | | | |
| SLOT-KEY: C-10    | | | |
| SLOT-KEY: C-11    | | | |
| SLOT-KEY: C-12    | | | |
| SLOT-KEY: Support | | | |
| SLOT-KEY: SRE     | | | |

---

## PHASE 1 INNOVATORS — Month 1

Displacement state at phase entry: THE INCUMBENT is fully entrenched. All TABLE 1 Incumbent Dependency values load-bearing; all Protected behaviors in SECTION A DOWNSTREAM CITATION CONTRACT fully active.

Q-BARRIER: Which Named Inertia ID is the primary barrier even for Innovators?
(Cite I-01 — what Protected behavior from SECTION A contract row I-01 do Innovators hold most tightly?)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [which Protected behaviors from I-01's contract row begin to weaken]
Inertia ID this phase overcame (partially): [re-cite I-01]

---

## PHASE 2 EARLY ADOPTERS — Month 2–3

Displacement state at phase entry: [re-cite verbatim PHASE 1 "Incumbent position after this phase:"]

Q-BARRIER: Which Named Inertia ID is the primary barrier for Early Adopters?
(Cite I-02 — Protected behavior from SECTION A contract row I-02)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [specific displacement state]
Inertia ID this phase overcame (partially): [re-cite I-02]

---

## PHASE 3 CHASM — Month 4 (Non-Adoption Crossing Event)

Displacement state entering PHASE 3: [re-cite verbatim PHASE 2 "Incumbent position after this phase:"]

PHASE 3 is not an adoption phase. No new archetype adopts in Month 4.

Q-BARRIER: Which Named Inertia ID is driving the chasm?
(Cite I-03 — what Protected behavior from SECTION A contract row I-03 makes this chasm structural?)

### CHASM-A — Incumbent Defense

[Named defense mechanism — explicitly connects to Protected behavior declared for I-03]

### CHASM-B — Bridge Condition

[Bridge condition as testable proposition]

### CHASM-C — Early Crossing Signal

[First observable crossing signal]

**Phase-close displacement ledger:**
Inertia ID defending THE INCUMBENT at this boundary: [I-03 and its Protected behavior from SECTION A]

---

## PHASE 4 EARLY MAJORITY — Month 5–7

Displacement state at phase entry: [re-cite PHASE 3 close state + what THE INCUMBENT still controlled entering Month 5]

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Early Majority?
(Cite I-03 — Protected behavior still active for these roles)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [specific displacement state]
Inertia ID this phase overcame (partially): [re-cite I-03]

---

## PHASE 5 LATE MAJORITY — Month 8–10

Displacement state at phase entry: [re-cite verbatim PHASE 4 "Incumbent position after this phase:"]

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Late Majority?
(Cite I-04 — Protected behavior from SECTION A contract row I-04)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [specific displacement state]
Inertia ID this phase overcame (partially): [re-cite I-04]

---

## PHASE 6 LAGGARDS — Month 11–12

Displacement state at phase entry: [re-cite verbatim PHASE 5 "Incumbent position after this phase:"]

Q-BARRIER: Which Named Inertia ID keeps Laggards last?
(Cite I-05 — Protected behavior from SECTION A contract row I-05 as final holdout)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [terminal displacement state — which Protected behaviors persist past Month 12]
Inertia ID this phase overcame: [re-cite I-05]

---

## TABLE 3 — Spread Mechanisms

| Transition Pair (SLOT-KEY row) | Spread Mechanism: [named signal or artifact specific to {{topic}} — not generic word-of-mouth] | Month Range |
|---|---|---|
| SLOT-KEY: Innovator → Early Adopter      | | |
| SLOT-KEY: Early Adopter → Early Majority | | |
| SLOT-KEY: Early Majority → Late Majority | | |
| SLOT-KEY: Late Majority → Laggard        | | |

---

## PART 2 — CHASM ANALYSIS (Full Expansion)

### CHASM-A EXPANSION — Incumbent Defense (Full Diagnosis)

Expanding CHASM-A from PHASE 3 —
Named Inertia in effect: [re-cite I-03]
Incumbent position at this chasm element: [displacement state — which Protected behavior from I-03 contract row is load-bearing here]

[Full diagnosis]

### CHASM-B EXPANSION — Bridge Condition (Full Specification)

Expanding CHASM-B from PHASE 3 —
Named Inertia in effect: [re-cite I-03]
Incumbent position at this chasm element: [displacement state — which Protected behavior unblocks when bridge condition is satisfied]

[Full specification]

### CHASM-C EXPANSION — Crossing Signal (Full Identification)

Expanding CHASM-C from PHASE 3 —
Named Inertia in effect: [re-cite I-03]
Incumbent position at this chasm element: [displacement state — which Protected behavior weakens at the crossing signal moment]

[Full identification]

---

## PART 3 — Churn Risk Register

| Role (SLOT-KEY typed slot) | Reversion trigger: [names the Protected behavior from SECTION A being re-activated] | Retention intervention: [one concrete action — not a surveillance flag] | Q-TRIGGER: Named Inertia ID driving reversion (I-0X) |
|------|-----|-----|-----|
| SLOT-KEY: [Role] — churn entry | | | |

---

## PART 4 — Champion Network

| Champion Role (SLOT-KEY typed slot) | Archetype | Archetype-bridge rationale | Q-CHAMPION: Named Inertia ID this champion overcomes (I-0X) | Why this champion displaces the Protected behavior from the I-0X contract row |
|---|---|---|---|---|
| SLOT-KEY: [Role] — champion entry | | | | |
| SLOT-KEY: [Role] — champion entry | | | | |
| SLOT-KEY: [Role] — champion entry | | | | |

---

## PART 5 — Intervention Ranking

| Rank | Intervention | Adoption delta | Phase(s) | Role(s) | Incumbent Impact | Targets inertia: [I-0X — names the Protected behavior this intervention displaces] |
|------|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |

---

## PART 6 — Sensitivity Analysis

| Scenario      | Adoption outcome | Named lever | Direction of shift |
|---------------|------------------|-------------|-------------------|
| Fast Adoption |                  |             |                   |
| Slow Adoption |                  |             |                   |

---

## PART 7 — Signal Readiness Table

| Signal name | Threshold | Interpretation |
|-------------|-----------|----------------|
|             |           |                |

---

> CORRECTION BLOCK MECHANISM ARMED — no gate failure triggered. If any gate below fails, a CORRECTION BLOCK with BEFORE and AFTER fields will be inserted immediately above this line. Under this variation, a Gate H contract-row FAIL produces a separately labeled CORRECTION BLOCK per failed I-0X row, with the label including the Protected behavior from that contract row.

## VERIFICATION MODE

All content generation is complete above this boundary. SECTIONS H, I, J, K are audit sections only.

---

## SECTION H — Gate: C-13 Audit

**Audit against DOWNSTREAM CITATION CONTRACT — fill Gate H Status per row; for any FAIL, name the Protected behavior left unaddressed and produce a per-I-0X CORRECTION BLOCK:**

- I-01 [Protected behavior: see SECTION A]: PHASE 1 Q-BARRIER [Y/N] · ledger [Y/N] · PART 3 Q-TRIGGER Innovator [Y/N] → Fill SECTION A row I-01
- I-02 [Protected behavior: see SECTION A]: PHASE 2 Q-BARRIER [Y/N] · ledger [Y/N] · PART 3 Q-TRIGGER EA [Y/N] → Fill SECTION A row I-02
- I-03 [Protected behavior: see SECTION A]: PHASE 3 Q-BARRIER [Y/N] · ledger [Y/N] · CHASM-A [Y/N] · CHASM-B [Y/N] · PHASE 4 Q-BARRIER [Y/N] · PHASE 4 ledger [Y/N] · PART 5 [Y/N] → Fill SECTION A row I-03
- I-04 [Protected behavior: see SECTION A]: PHASE 5 Q-BARRIER [Y/N] · ledger [Y/N] · PART 3 Q-TRIGGER LM [Y/N] → Fill SECTION A row I-04
- I-05 [Protected behavior: see SECTION A]: PHASE 6 Q-BARRIER [Y/N] · ledger [Y/N] · PART 3 Q-TRIGGER Laggard [Y/N] → Fill SECTION A row I-05

**Gate H result:** [PASS / FAIL — for any FAIL: "I-0X [Protected behavior: ...] missing citation at [location]"]

**Per-I-0X revision obligation (Axis A):** For each failed contract row, produce `CORRECTION BLOCK — I-0X [Protected behavior: ...]: [missed location] — BEFORE: [...] — AFTER: [...]` immediately before the pre-verification declaration. One block per failed row; no bundling.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate H [PASS: no per-I-0X correction triggered | FAIL: per-I-0X CORRECTION BLOCK(s) written above pre-verification line, labeled by I-0X and Protected behavior]

---

## SECTION I — Gate: C-14 Audit

- SLOT-KEY champion 1 [name]: archetype-bridge [Y/N] | Q-CHAMPION I-0X [Y/N]
- SLOT-KEY champion 2 [name]: archetype-bridge [Y/N] | Q-CHAMPION I-0X [Y/N]
- SLOT-KEY champion 3 [name]: archetype-bridge [Y/N] | Q-CHAMPION I-0X [Y/N]

**Gate I result:** [PASS / FAIL]

**Revision obligation:** If Gate I FAILS, produce CORRECTION BLOCK before pre-verification declaration.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate I [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION J — Gate: C-15 Audit

- [List each SLOT-KEY: churn entry and classification]

**Gate J result:** [PASS / FAIL]

**Revision obligation:** If Gate J FAILS, produce CORRECTION BLOCK before pre-verification declaration.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate J [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION K — Terminal Audit Record

**Terminal Invariant:** For every "Revision Performed: Yes," a CORRECTION BLOCK with BEFORE and AFTER fields must exist at the cited location above the pre-verification declaration. Under this variation, Gate H failures produce per-I-0X labeled blocks; "Revision Performed: Yes" for Gate H cites all produced block locations (one per failed I-0X row, each labeled with its Protected behavior). A Yes entry without matching per-I-0X CORRECTION BLOCK(s), or a CORRECTION BLOCK without a BEFORE field, falsifies this invariant.

| Gate | Criterion | Initial result | Revision performed | CORRECTION BLOCK location | Final result |
|------|-----------|----------------|--------------------|--------------------------|--------------|
| H    | C-13      |                | Yes / No           |                          |              |
| I    | C-14      |                | Yes / No           |                          |              |
| J    | C-15      |                | Yes / No           |                          |              |

**CITATION CONTRACT COMPLETION RECORD (with Protected behavior column — Axis C):**

| Inertia ID | Protected behavior (from SECTION A) | Required sinks satisfied | Structural location found | Gate H Status |
|------------|-------------------------------------|--------------------------|--------------------------|---------------|
| I-01       |                                     |                          |                          |               |
| I-02       |                                     |                          |                          |               |
| I-03       |                                     |                          |                          |               |
| I-04       |                                     |                          |                          |               |
| I-05       |                                     |                          |                          |               |

**DISPLACEMENT ARC INTEGRITY CHECK (Axis B):**

| Transition | Exit state (from close ledger) | Entry state (from phase open) | Verdict |
|---|---|---|---|
| PHASE 1 close → PHASE 2 open | [Incumbent position after PHASE 1] | [Displacement state at PHASE 2 entry] | MATCH / MISMATCH |
| PHASE 2 close → PHASE 3 entry | [Incumbent position after PHASE 2] | [Displacement state entering PHASE 3] | MATCH / MISMATCH |
| PHASE 3 close → PHASE 4 open | [Inertia defending THE INCUMBENT at PHASE 3 boundary + context] | [Displacement state at PHASE 4 entry] | MATCH / MISMATCH |
| PHASE 4 close → PHASE 5 open | [Incumbent position after PHASE 4] | [Displacement state at PHASE 5 entry] | MATCH / MISMATCH |
| PHASE 5 close → PHASE 6 open | [Incumbent position after PHASE 5] | [Displacement state at PHASE 6 entry] | MATCH / MISMATCH |

Arc integrity: [PASS if all transitions MATCH | FAIL naming the specific discontinuity and which Protected behavior the narrative inconsistency affects]
