# Variations: listen-adoption — Round 15

**Rubric:** v15 | **New criteria:** C-42, C-43, C-44 | **Max composite:** 270 | **Golden threshold (80%):** 216 pts | **Projected ceiling:** 265/270 (C-19 paradox persists)

---

## Variation Axes

| Axis | R15 Target | Description |
|------|-----------|-------------|
| Lifecycle emphasis | C-42+: Phase-close displacement ledger | Each adoption PHASE (1,2,4,5,6) closes with a mandatory `Incumbent position after this phase:` + `Inertia ID this phase overcame:` structured field — extends the inertia-displacement chain from PHASE-level Q-BARRIER (top anchor) to PHASE-level displacement accounting (bottom anchor), making inertia carry continuous through every phase boundary |
| Output format / Role sequence | PART 3 SLOT-KEY: row prefix | C-43 pattern (TABLE 1 row-level SLOT-KEY: re-assertion) applied to the churn register — each row re-asserts the three churn contracts (reversion trigger | retention intervention | inertia ID) at row generation time, independent of column headers |
| Inertia framing | SECTION A Downstream Citation Contract | A declared citation-map block added immediately after the Named Inertia table — SECTION A announces where each I-0X must appear downstream (Q-BARRIER phases, Q-CHAMPION, Q-TRIGGER, Q-INTERVENTION). SECTION H audits against this declared contract rather than performing a free-form scan |
| Phrasing register | Baseline | Carried from R14 V-05 |
| Output format (scale/table) | Baseline | Carried from R14 V-05: SLOT-KEY: TABLE 1+TABLE 3, PART 2 Named Inertia in effect:, PART 5 Targets inertia: |

**Single-axis (V-01, V-02, V-03):** Lifecycle emphasis · Output format/Role sequence · Inertia framing
**Combined (V-04):** Output format + Inertia framing
**Full (V-05):** Lifecycle emphasis + Output format + Inertia framing

**Baseline (all five carry from R14 V-05):**

| Element | Criterion | Form |
|---|---|---|
| STRUCTURAL CONTRACT naming answer-form questions AND MECHANISM STATE | C-35 | Block before SECTION A |
| Per-gate MECHANISM STATE footers in SECTIONS H, I, J | C-34 (gate-level anchor) | `> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate X [...]` |
| Pre-verification MECHANISM STATE declaration before `## VERIFICATION MODE` | C-34 (boundary-level anchor) | `> CORRECTION BLOCK MECHANISM ARMED — no gate failure triggered` |
| SECTION A Named Inertia IDs, I-01 through I-05 | C-11 | Table: Inertia ID | Archetype | Named Inertia | Structural reason |
| TABLE 1 with SLOT-KEY: row prefix AND Incumbent Dependency AND Inertia ID columns | C-43, C-41, C-37 | SLOT-KEY: row label re-asserts three-contract type at each row |
| PHASE 3 CHASM with CHASM-A / CHASM-B / CHASM-C structural subsections | C-39 | Named subsection headers per required element |
| PART 2 with CHASM-A/B/C EXPANSION + "Named Inertia in effect:" per slot | C-42, C-40 | First structural field of each expansion subsection re-cites I-0X from PHASE 3 Q-BARRIER |
| TABLE 3 typed header + SLOT-KEY: row labels + specificity constraint in column label | C-36, C-38, C-28 | Header names rows as typed structural slot keys |
| PART 5 Incumbent Impact column AND Targets inertia: column | C-26 ext., C-44 | Per-row: what THE INCUMBENT loses + which I-0X this intervention addresses |
| C-24 Terminal Invariant names BOTH falsification cases | C-24 | "...no CORRECTION BLOCK at cited location, or a CORRECTION BLOCK without a BEFORE field, falsifies this invariant" |

**Axis activation map:**

| Variation | Axis A: Phase-close displacement ledger | Axis B: PART 3 SLOT-KEY: rows | Axis C: SECTION A citation contract | Delta from R14 V-05 baseline |
|---|---|---|---|---|
| V-01 | **Active:** `Incumbent position after this phase:` + `Inertia ID this phase overcame:` closing fields per adoption phase | Baseline | Baseline | Phases close with displacement accounting + inertia citation |
| V-02 | Baseline | **Active:** `SLOT-KEY: [Role] — churn entry` prefix on PART 3 rows | Baseline | Churn register rows self-describing as three-contract typed slots |
| V-03 | Baseline | Baseline | **Active:** SECTION A DOWNSTREAM CITATION CONTRACT block | Named Inertia IDs pre-announce their downstream positions at SECTION A generation time |
| V-04 | Baseline | Active (V-02) | Active (V-03) | Churn register SLOT-KEY: rows + SECTION A citation contract |
| V-05 | Active (V-01) | Active (V-02) | Active (V-03) | All three: phase-close accounting + PART 3 SLOT-KEY: + SECTION A contract |

---

## V-01 — Single Axis: Lifecycle Emphasis (Phase-Close Displacement Ledger)

**Variation axis:** Lifecycle emphasis — each adoption phase (PHASES 1, 2, 4, 5, 6) closes with a mandatory two-field displacement ledger immediately before the phase separator: `Incumbent position after this phase: [what THE INCUMBENT still controls — state specifically what workflow, process, or role dependency it retains after this phase's adoption]` and `Inertia ID this phase overcame: [re-cite I-0X from this phase's Q-BARRIER — the Named Inertia whose partial weakening enabled this phase's adoption]`. PHASE 3 (non-adoption) closes with a single field: `Inertia ID defending THE INCUMBENT at this boundary: [I-03]`.

**Hypothesis:** Each phase body currently opens with Q-BARRIER (answer-form inertia citation at generation entry) but has no closing structural anchor. The model generates the phase body with the inertia ID present at entry, but there is no generation-time pressure to track displacement progress or confirm which inertia the phase's events overcame before proceeding to the next phase. Adding a phase-close displacement ledger creates a second mandatory answer-form anchor at phase exit: the model must assess displacement progress (what THE INCUMBENT still holds) and confirm inertia carry-forward (which I-0X this phase weakened) before proceeding. This creates a continuous inertia-displacement accounting thread running through all six phases — the inertia backbone is not just cited at phase entry via Q-BARRIER but accounted for at phase exit via the ledger, making omission of displacement progress structurally equivalent to leaving a fill contract empty.

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

Assign one Named Inertia ID per canonical Rogers archetype. The inertia is the structural reason that archetype resists adoption of {{topic}}. These IDs are cited by Q-BARRIER throughout all phase bodies, expansion subsections, champion entries, churn triggers, and intervention entries.

| Inertia ID | Archetype      | Named Inertia                      | Structural reason this archetype resists |
|------------|----------------|------------------------------------|------------------------------------------|
| I-01       | Innovator      | [name the inertia for Innovators]  | [structural reason]                      |
| I-02       | Early Adopter  | [name the inertia for EA]          | [structural reason]                      |
| I-03       | Early Majority | [name the inertia for EM]          | [structural reason]                      |
| I-04       | Late Majority  | [name the inertia for LM]          | [structural reason]                      |
| I-05       | Laggard        | [name the inertia for Laggards]    | [structural reason]                      |

---

THE INCUMBENT is [name the current workflow, tool, or practice being displaced by {{topic}}]. All phase bodies, champion entries, churn triggers, and interventions run through the displacement lens: what does this phase do to THE INCUMBENT's position?

---

## TABLE 1 — Role Archetype Map

TABLE 1 header contract: Each row below is prefixed SLOT-KEY: — the row label is a typed structural slot key re-asserting the three co-present contracts (archetype assignment, Incumbent Dependency, Inertia ID citation) at this row's generation moment, independently of the column headers. A row is complete only when all three contract fields are filled. SLOT-KEY: [Role] is not a cosmetic prefix; it re-asserts the typed slot contract at the point of generation for that specific role.

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

Which roles adopt in Month 1? Name them and their archetype assignment from TABLE 1. What does THE INCUMBENT lose in this phase?

Q-BARRIER: Which Named Inertia ID is the primary barrier even for Innovators?
(Cite I-01 from SECTION A — this question's structurally correct answer is I-01, the Innovator inertia. A different answer requires explicit justification.)

[Phase body: named roles, what they try, what signals they produce, displacement impact on THE INCUMBENT's position]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what workflow, process, or role dependency THE INCUMBENT retains after Month 1 — be specific about what it still controls]
Inertia ID this phase overcame (partially): [re-cite I-01 from Q-BARRIER above — the Named Inertia whose weakening enabled Month 1 adoption]

---

## PHASE 2 EARLY ADOPTERS — Month 2–3

Which roles adopt in Months 2–3? What evidence from PHASE 1 persuades them?

Q-BARRIER: Which Named Inertia ID is the primary barrier for Early Adopters?
(Cite I-02 from SECTION A)

[Phase body: named roles, what they adopt, spread mechanism from PHASE 1, incumbent displacement progress]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what THE INCUMBENT still controls after Month 3 — which TABLE 1 Incumbent Dependency values remain load-bearing]
Inertia ID this phase overcame (partially): [re-cite I-02 from Q-BARRIER above]

---

## PHASE 3 CHASM — Month 4 (Non-Adoption Crossing Event)

PHASE 3 is not an adoption phase. It is a crossing event. No new archetype adopts in Month 4. The chasm is diagnosed below using three named structural subsections.

Q-BARRIER: Which Named Inertia ID is driving the chasm?
(Cite I-03 from SECTION A — the Early Majority archetype inertia is the structural driver of the chasm. A different answer requires explicit justification.)

### CHASM-A — Incumbent Defense

What defends THE INCUMBENT's position among the Early Majority and Late Majority? Name the specific workflow dependency, process lock-in, or organizational force that makes THE INCUMBENT defensible at this boundary.

[CHASM-A body: named incumbent defense mechanism, which TABLE 1 Incumbent Dependency values are load-bearing here, why crossing requires more than Early Adopter endorsement]

### CHASM-B — Bridge Condition

What single condition must hold for the Early Majority to cross? State it as a testable proposition: "The chasm is crossed when [specific observable condition]."

[CHASM-B body: the bridge condition, which roles must satisfy it, what artifact or signal proves it is met, connection to THE INCUMBENT's weakest dependency point]

### CHASM-C — Early Crossing Signal

What is the first observable signal that the chasm has been crossed? Name a specific role, artifact, or behavioral event — not a metric threshold — that indicates Early Majority adoption has begun.

[CHASM-C body: named crossing signal, which role emits it, what it proves about the bridge condition from CHASM-B, why it is distinguishable from Early Adopter behavior]

**Phase-close displacement ledger:**
Inertia ID defending THE INCUMBENT at this boundary: [I-03 — the Early Majority inertia that makes the chasm a structural barrier rather than a timing gap]

---

## PHASE 4 EARLY MAJORITY — Month 5–7

Which roles adopt in Months 5–7? What bridge condition from CHASM-B is now satisfied?

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Early Majority?
(Cite I-03 from SECTION A)

[Phase body: named roles, what proof from CHASM-B allows these roles to adopt, reference TABLE 1 Incumbent Dependency values now unblocked, incumbent displacement acceleration]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what THE INCUMBENT still controls after Month 7 — name any remaining TABLE 1 Incumbent Dependency values that persist]
Inertia ID this phase overcame (partially): [re-cite I-03 from Q-BARRIER above — I-03's weakening is what unlocked Early Majority adoption]

---

## PHASE 5 LATE MAJORITY — Month 8–10

Which roles adopt in Months 8–10? What social proof from PHASE 4 reaches them? Reference their high Incumbent Dependency values from TABLE 1.

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Late Majority?
(Cite I-04 from SECTION A)

[Phase body: named roles, adoption trigger, incumbent erosion, what remains of THE INCUMBENT's position]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what THE INCUMBENT still controls after Month 10 — which roles or workflow steps remain unconverted]
Inertia ID this phase overcame (partially): [re-cite I-04 from Q-BARRIER above]

---

## PHASE 6 LAGGARDS — Month 11–12

Which roles adopt last? What finally moves them?

Q-BARRIER: Which Named Inertia ID keeps Laggards last?
(Cite I-05 from SECTION A — this is the only structurally correct answer)

[Phase body: named roles, final adoption conditions, terminal incumbent displacement state]

**Phase-close displacement ledger:**
Incumbent position after this phase: [terminal displacement state — what, if anything, THE INCUMBENT retains after Month 12]
Inertia ID this phase overcame: [re-cite I-05 from Q-BARRIER above — I-05's weakening is what finally moved Laggards]

---

## TABLE 3 — Spread Mechanisms

TABLE 3 header contract: Each row below is prefixed SLOT-KEY: — the row label is a typed structural slot key naming a specific canonical transition pair. The Spread Mechanism column must be filled with a named signal, artifact, or social proof event that is specific to {{topic}} — not "word of mouth," "organic growth," or any other generic mechanism. A mechanism valid for one SLOT-KEY is not valid for another; they are not interchangeable. A generic entry violates the slot-type contract declared by this header.

| Transition Pair (SLOT-KEY row) | Spread Mechanism: [named signal or artifact specific to {{topic}} — not generic word-of-mouth] | Month Range |
|---|---|---|
| SLOT-KEY: Innovator → Early Adopter      | | |
| SLOT-KEY: Early Adopter → Early Majority | | |
| SLOT-KEY: Early Majority → Late Majority | | |
| SLOT-KEY: Late Majority → Laggard        | | |

---

## PART 2 — CHASM ANALYSIS (Full Expansion)

PHASE 3 introduced a diagnostic sketch of each chasm element. PART 2 expands each element to its full specification. Three named structural subsections mirror PHASE 3's CHASM-A/B/C structure. A missing subsection here is a missing named structural slot — same enforcement class as a missing CHASM-A/B/C subsection in PHASE 3 itself.

Each expansion subsection re-cites the Named Inertia ID from its PHASE 3 Q-BARRIER answer as the first structural field. The model cannot complete a CHASM-X EXPANSION subsection without re-asserting the Named Inertia ID that drives that element.

### CHASM-A EXPANSION — Incumbent Defense (Full Diagnosis)

Expanding CHASM-A from PHASE 3 —
Named Inertia in effect: [re-cite I-0X from Q-BARRIER in PHASE 3 CHASM-A — the Named Inertia ID identified as the structural driver of the incumbent defense]

[Full diagnosis: the complete mechanism by which THE INCUMBENT defends its position at the chasm boundary — process dependencies, organizational commitments, role-level switching costs. Name every TABLE 1 Incumbent Dependency value that is load-bearing here. Identify which Early Majority roles are most defended and why.]

### CHASM-B EXPANSION — Bridge Condition (Full Specification)

Expanding CHASM-B from PHASE 3 —
Named Inertia in effect: [re-cite I-0X from Q-BARRIER in PHASE 3 CHASM-B — the Named Inertia ID whose resolution is the bridge condition]

[Full specification: the bridge condition stated as a testable proposition, the precise observable state that satisfies it, which role or artifact produces that state, and why that state is sufficient to unlock Early Majority adoption. Cross-reference the Incumbent Dependency values from TABLE 1 that the bridge condition unblocks.]

### CHASM-C EXPANSION — Crossing Signal (Full Identification)

Expanding CHASM-C from PHASE 3 —
Named Inertia in effect: [re-cite I-0X from Q-BARRIER in PHASE 3 CHASM-C — the Named Inertia ID whose weakening produces the crossing signal]

[Full identification: the crossing signal named with precision — the specific role, behavioral event, or artifact emission that proves the chasm has been crossed. Explain why this signal is distinguishable from Early Adopter behavior, how it connects to the bridge condition from CHASM-B EXPANSION, and what adoption acceleration it predicts in PHASE 4.]

---

## PART 3 — Churn Risk Register

Every role that adopts carries a reversion risk: the specific condition that would cause them to return to THE INCUMBENT. List all roles at non-trivial churn risk. Each entry must name the reversion trigger (not a generic risk category) and a concrete retention action.

| Role | Reversion trigger: [the specific condition that causes this role to revert to THE INCUMBENT] | Retention intervention: [one concrete action that reduces reversion probability — not a surveillance flag] | Inertia ID driving reversion: [Q-TRIGGER: which Named Inertia ID drives reversion risk for this role? Cite I-0X from SECTION A] |
|------|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
|      |                                                                                              |                                                                                                             |                                                                                                                                  |

---

## PART 4 — Champion Network

Name at least three roles positioned to advocate for {{topic}} adoption and displace THE INCUMBENT. For each champion, provide two structural anchors:

(a) Archetype-bridge rationale — why this role's archetype position makes it an effective adoption champion for the next archetype tier.

(b) Q-CHAMPION: Named Inertia ID this champion is positioned to overcome:
(Cite I-0X from SECTION A — the inertia this champion's position directly addresses)

| Champion Role | Archetype | Archetype-bridge rationale | Q-CHAMPION: Named Inertia ID overcome (I-0X) | Why this champion displaces THE INCUMBENT for the target tier |
|---|---|---|---|---|
|   |   |   |   |   |

---

## PART 5 — Intervention Ranking

Rank retention interventions by their impact on adoption velocity (adoption delta: the percentage-point increase in adoption rate the intervention produces). Each entry must reference at least one named phase and one named role. The Incumbent Impact column names what THE INCUMBENT loses when this intervention succeeds. The Targets inertia column encodes Q-INTERVENTION as a per-row structural fill contract — a row without a Named Inertia ID in this column violates the slot-type contract of this table.

| Rank | Intervention | Adoption delta | Phase(s) affected | Role(s) affected | Incumbent Impact: [what THE INCUMBENT loses when this intervention succeeds] | Targets inertia: [I-0X — Q-INTERVENTION: which Named Inertia ID does this intervention directly address?] |
|------|--------------|----------------|-------------------|------------------|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| 1    |              |                |                   |                  |                                                                              |                                                                                                          |
| 2    |              |                |                   |                  |                                                                              |                                                                                                          |
| 3    |              |                |                   |                  |                                                                              |                                                                                                          |

---

## PART 6 — Sensitivity Analysis

| Scenario        | Adoption outcome | Named lever | Direction of shift |
|-----------------|------------------|-------------|-------------------|
| Fast Adoption   |                  |             |                   |
| Slow Adoption   |                  |             |                   |

---

## PART 7 — Signal Readiness Table

| Signal name | Threshold | Interpretation: what this signal level means for {{topic}} adoption timing |
|-------------|-----------|----------------------------------------------------------------------------|
|             |           |                                                                            |

---

> CORRECTION BLOCK MECHANISM ARMED — no gate failure triggered. If any gate below fails, a CORRECTION BLOCK with BEFORE and AFTER fields will be inserted immediately above this line before proceeding to SECTION K.

## VERIFICATION MODE

All content generation is complete above this boundary. SECTIONS H, I, J, K are audit sections only. No content generation occurs below this line.

---

## SECTION H — Gate: C-13 Audit (Named Inertia IDs as Downstream Backbone)

**Criterion C-13:** Named Inertia IDs from SECTION A are cited by ID (I-0X) in at least four downstream location types: (1) bridge conditions, (2) intervention rationale — note: `Targets inertia:` column satisfies this location type structurally when filled, (3) champion rationale, (4) churn register entries.

**Audit:** Scan the document for I-0X citations in each of the four required location types.

- Bridge conditions (CHASM-B, CHASM-B EXPANSION): [PASS/FAIL — cite location and ID found, or name missing location]
- Intervention rationale (PART 5, Targets inertia: column): [PASS/FAIL]
- Champion rationale (PART 4, Q-CHAMPION answers): [PASS/FAIL]
- Churn register (PART 3, Q-TRIGGER answers): [PASS/FAIL]

**Gate H result:** [PASS if all four location types contain at least one I-0X citation | FAIL if any location type lacks a citation]

**Revision obligation:** If Gate H FAILS, produce a CORRECTION BLOCK immediately before the pre-verification declaration above. The CORRECTION BLOCK must contain a BEFORE field showing the deficient content and an AFTER field showing the corrected content with I-0X citations added. Do not proceed to SECTION I until the CORRECTION BLOCK is written.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate H [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION I — Gate: C-14 Audit (Champion Rationale Double-Anchored)

**Criterion C-14:** Each champion entry in PART 4 contains both: (a) archetype-bridge rationale and (b) a Named Inertia ID cited by Q-CHAMPION answer (I-0X from SECTION A).

**Audit:** For each champion entry in PART 4, verify both anchors are present.

- Champion 1 [name]: archetype-bridge present? [Y/N] | Q-CHAMPION I-0X cited? [Y/N]
- Champion 2 [name]: archetype-bridge present? [Y/N] | Q-CHAMPION I-0X cited? [Y/N]
- Champion 3 [name]: archetype-bridge present? [Y/N] | Q-CHAMPION I-0X cited? [Y/N]

**Gate I result:** [PASS if both anchors present for all champions | FAIL if any champion lacks either anchor]

**Revision obligation:** If Gate I FAILS, produce a CORRECTION BLOCK immediately before the pre-verification declaration above. Do not proceed to SECTION J until the CORRECTION BLOCK is written.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate I [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION J — Gate: C-15 Audit (Concrete Retention Actions)

**Criterion C-15:** Every mitigation in PART 3's churn register is a concrete retention action — something a team does to reduce reversion probability. Surveillance-only entries ("track usage," "monitor engagement") fail this criterion.

**Audit:** For each entry in PART 3, verify the Retention intervention field contains a concrete action rather than a surveillance flag.

- [List each churn register entry and its classification: concrete action or surveillance flag]

**Gate J result:** [PASS if all entries contain concrete retention actions | FAIL if any entry contains only a surveillance flag]

**Revision obligation:** If Gate J FAILS, produce a CORRECTION BLOCK immediately before the pre-verification declaration above. Do not proceed to SECTION K until the CORRECTION BLOCK is written.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate J [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION K — Terminal Audit Record

Per-gate execution stamps are recorded here for all three gates regardless of outcome. A terminal section recording only failures is incomplete; a passing gate that left no stamp is unverified audit execution.

**Terminal Invariant:** For every gate with "Revision Performed: Yes" in this section, a CORRECTION BLOCK with BEFORE and AFTER fields must exist in the document body at the cited location, above the pre-verification declaration. A "Revision Performed: Yes" entry whose cited location contains no CORRECTION BLOCK, or a CORRECTION BLOCK that contains no BEFORE field, falsifies this invariant.

| Gate | Criterion | Initial result | Revision performed | CORRECTION BLOCK location | Final result |
|------|-----------|----------------|--------------------|--------------------------|--------------|
| H    | C-13      |                | Yes / No           |                          |              |
| I    | C-14      |                | Yes / No           |                          |              |
| J    | C-15      |                | Yes / No           |                          |              |

---

## V-02 — Single Axis: Output Format / Role Sequence (PART 3 SLOT-KEY: Row Prefix)

**Variation axis:** Output format / Role sequence — PART 3 churn register rows prefixed with `SLOT-KEY: [Role] — churn entry`, applying the C-43 enforcement pattern (TABLE 1 row-level three-contract re-assertion) to the churn register. Each churn row re-asserts the three churn contracts (reversion trigger | retention intervention | inertia ID) at the row generation moment, independently of the column headers. The SLOT-KEY: prefix is declared in a PART 3 header contract, mirroring TABLE 1's header contract.

**Hypothesis:** PART 3 currently has typed column labels (Q-TRIGGER, concrete-action constraint in "Retention intervention:") that establish the three-contract requirement at table entry. A model generating the eighth churn entry relies on column headers set 8+ rows above. The SLOT-KEY: prefix applies the same generation-time re-assertion pattern that C-43 applies to TABLE 1: each row label `SLOT-KEY: [Role] — churn entry` re-asserts the three-contract type independently, making a model generating the churn entry for a late-adopting role encounter the three-contract reminder from the row label itself rather than from memory of the column header. Same structural elevation class as C-43 applied to C-27/C-15's concrete-action constraint and Q-TRIGGER's citation requirement.

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

Assign one Named Inertia ID per canonical Rogers archetype. The inertia is the structural reason that archetype resists adoption of {{topic}}. These IDs are cited by Q-BARRIER throughout all phase bodies, expansion subsections, champion entries, churn triggers, and intervention entries.

| Inertia ID | Archetype      | Named Inertia                      | Structural reason this archetype resists |
|------------|----------------|------------------------------------|------------------------------------------|
| I-01       | Innovator      | [name the inertia for Innovators]  | [structural reason]                      |
| I-02       | Early Adopter  | [name the inertia for EA]          | [structural reason]                      |
| I-03       | Early Majority | [name the inertia for EM]          | [structural reason]                      |
| I-04       | Late Majority  | [name the inertia for LM]          | [structural reason]                      |
| I-05       | Laggard        | [name the inertia for Laggards]    | [structural reason]                      |

---

THE INCUMBENT is [name the current workflow, tool, or practice being displaced by {{topic}}]. All phase bodies, champion entries, churn triggers, and interventions run through the displacement lens: what does this phase do to THE INCUMBENT's position?

---

## TABLE 1 — Role Archetype Map

TABLE 1 header contract: Each row below is prefixed SLOT-KEY: — the row label is a typed structural slot key re-asserting the three co-present contracts (archetype assignment, Incumbent Dependency, Inertia ID citation) at this row's generation moment, independently of the column headers. A row is complete only when all three contract fields are filled. SLOT-KEY: [Role] is not a cosmetic prefix; it re-asserts the typed slot contract at the point of generation for that specific role.

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

Which roles adopt in Month 1? Name them and their archetype assignment from TABLE 1. What does THE INCUMBENT lose in this phase?

Q-BARRIER: Which Named Inertia ID is the primary barrier even for Innovators?
(Cite I-01 from SECTION A — this question's structurally correct answer is I-01. A different answer requires explicit justification.)

[Phase body: named roles, what they try, what signals they produce, displacement impact on THE INCUMBENT's position]

---

## PHASE 2 EARLY ADOPTERS — Month 2–3

Which roles adopt in Months 2–3? What evidence from PHASE 1 persuades them?

Q-BARRIER: Which Named Inertia ID is the primary barrier for Early Adopters?
(Cite I-02 from SECTION A)

[Phase body: named roles, what they adopt, spread mechanism from PHASE 1, incumbent displacement progress]

---

## PHASE 3 CHASM — Month 4 (Non-Adoption Crossing Event)

PHASE 3 is not an adoption phase. It is a crossing event. No new archetype adopts in Month 4.

Q-BARRIER: Which Named Inertia ID is driving the chasm?
(Cite I-03 from SECTION A — the Early Majority archetype inertia is the structural driver. A different answer requires explicit justification.)

### CHASM-A — Incumbent Defense

[Named incumbent defense mechanism, load-bearing TABLE 1 Incumbent Dependency values, why crossing requires more than Early Adopter endorsement]

### CHASM-B — Bridge Condition

[Bridge condition as testable proposition — state which specific observable condition must hold]

### CHASM-C — Early Crossing Signal

[First observable crossing signal — named role, artifact, or behavioral event; why distinguishable from Early Adopter behavior]

---

## PHASE 4 EARLY MAJORITY — Month 5–7

Which roles adopt in Months 5–7? What bridge condition from CHASM-B is now satisfied?

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Early Majority?
(Cite I-03 from SECTION A)

[Phase body: named roles, proof from CHASM-B, TABLE 1 Incumbent Dependency values now unblocked, incumbent displacement acceleration]

---

## PHASE 5 LATE MAJORITY — Month 8–10

Which roles adopt in Months 8–10? Reference their high Incumbent Dependency values from TABLE 1.

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Late Majority?
(Cite I-04 from SECTION A)

[Phase body: named roles, adoption trigger, incumbent erosion]

---

## PHASE 6 LAGGARDS — Month 11–12

Which roles adopt last? What finally moves them?

Q-BARRIER: Which Named Inertia ID keeps Laggards last?
(Cite I-05 from SECTION A — this is the only structurally correct answer)

[Phase body: named roles, final adoption conditions, terminal incumbent displacement state]

---

## TABLE 3 — Spread Mechanisms

TABLE 3 header contract: Each row below is prefixed SLOT-KEY: — the row label is a typed structural slot key naming a specific canonical transition pair. The Spread Mechanism column must be filled with a named signal, artifact, or social proof event specific to {{topic}} — not generic word-of-mouth. A generic entry violates the slot-type contract.

| Transition Pair (SLOT-KEY row) | Spread Mechanism: [named signal or artifact specific to {{topic}} — not generic word-of-mouth] | Month Range |
|---|---|---|
| SLOT-KEY: Innovator → Early Adopter      | | |
| SLOT-KEY: Early Adopter → Early Majority | | |
| SLOT-KEY: Early Majority → Late Majority | | |
| SLOT-KEY: Late Majority → Laggard        | | |

---

## PART 2 — CHASM ANALYSIS (Full Expansion)

Three named structural subsections expand PHASE 3's CHASM-A/B/C sketches. Each re-cites the Named Inertia ID from its PHASE 3 Q-BARRIER as the first structural field.

### CHASM-A EXPANSION — Incumbent Defense (Full Diagnosis)

Expanding CHASM-A from PHASE 3 —
Named Inertia in effect: [re-cite I-0X from Q-BARRIER in PHASE 3 CHASM-A — the Named Inertia ID driving the incumbent defense]

[Full diagnosis: complete mechanism — process dependencies, organizational commitments, role-level switching costs. Name every load-bearing TABLE 1 Incumbent Dependency value.]

### CHASM-B EXPANSION — Bridge Condition (Full Specification)

Expanding CHASM-B from PHASE 3 —
Named Inertia in effect: [re-cite I-0X from Q-BARRIER in PHASE 3 CHASM-B — the Named Inertia ID whose resolution is the bridge condition]

[Full specification: bridge condition as testable proposition, precise observable state satisfying it, role or artifact producing that state, TABLE 1 Incumbent Dependency values unblocked.]

### CHASM-C EXPANSION — Crossing Signal (Full Identification)

Expanding CHASM-C from PHASE 3 —
Named Inertia in effect: [re-cite I-0X from Q-BARRIER in PHASE 3 CHASM-C — the Named Inertia ID whose weakening produces the crossing signal]

[Full identification: named crossing signal, why distinguishable from Early Adopter behavior, connection to CHASM-B EXPANSION bridge condition, adoption acceleration predicted in PHASE 4.]

---

## PART 3 — Churn Risk Register

PART 3 header contract: Each row below is prefixed SLOT-KEY: — the row label is a typed structural churn slot re-asserting the three co-present churn contracts (reversion trigger | retention intervention | inertia ID) at this row's generation moment, independently of the column headers. SLOT-KEY: [Role] — churn entry is not a cosmetic prefix; it re-asserts the typed three-contract requirement at the point of generation for that specific role's churn entry.

| Role (SLOT-KEY typed churn slot) | Reversion trigger: [the specific condition that causes this role to revert to THE INCUMBENT] | Retention intervention: [one concrete action that reduces reversion probability — not a surveillance flag] | Inertia ID driving reversion: [Q-TRIGGER: which Named Inertia ID drives reversion risk for this role? Cite I-0X from SECTION A] |
|----------------------------------|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| SLOT-KEY: [Role] — churn entry   |                                                                                              |                                                                                                             |                                                                                                                                  |

---

## PART 4 — Champion Network

Name at least three roles positioned to advocate for {{topic}} adoption and displace THE INCUMBENT. For each champion, provide two structural anchors:

(a) Archetype-bridge rationale — why this role's archetype position makes it an effective adoption champion.
(b) Q-CHAMPION: Named Inertia ID this champion is positioned to overcome (Cite I-0X from SECTION A)

| Champion Role | Archetype | Archetype-bridge rationale | Q-CHAMPION: Named Inertia ID overcome (I-0X) | Why this champion displaces THE INCUMBENT for the target tier |
|---|---|---|---|---|
|   |   |   |   |   |

---

## PART 5 — Intervention Ranking

Rank by adoption delta. The Targets inertia column encodes Q-INTERVENTION as a per-row structural fill contract — a row without a Named Inertia ID in this column violates the slot-type contract.

| Rank | Intervention | Adoption delta | Phase(s) affected | Role(s) affected | Incumbent Impact: [what THE INCUMBENT loses when this intervention succeeds] | Targets inertia: [I-0X — Q-INTERVENTION: which Named Inertia ID does this intervention directly address?] |
|------|--------------|----------------|-------------------|------------------|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| 1    |              |                |                   |                  |                                                                              |                                                                                                          |
| 2    |              |                |                   |                  |                                                                              |                                                                                                          |
| 3    |              |                |                   |                  |                                                                              |                                                                                                          |

---

## PART 6 — Sensitivity Analysis

| Scenario        | Adoption outcome | Named lever | Direction of shift |
|-----------------|------------------|-------------|-------------------|
| Fast Adoption   |                  |             |                   |
| Slow Adoption   |                  |             |                   |

---

## PART 7 — Signal Readiness Table

| Signal name | Threshold | Interpretation: what this signal level means for {{topic}} adoption timing |
|-------------|-----------|----------------------------------------------------------------------------|
|             |           |                                                                            |

---

> CORRECTION BLOCK MECHANISM ARMED — no gate failure triggered. If any gate below fails, a CORRECTION BLOCK with BEFORE and AFTER fields will be inserted immediately above this line before proceeding to SECTION K.

## VERIFICATION MODE

All content generation is complete above this boundary. SECTIONS H, I, J, K are audit sections only. No content generation occurs below this line.

---

## SECTION H — Gate: C-13 Audit (Named Inertia IDs as Downstream Backbone)

**Criterion C-13:** I-0X citations in at least four downstream location types: (1) bridge conditions, (2) intervention rationale — Targets inertia: column satisfies this structurally when filled, (3) champion rationale, (4) churn register entries.

**Audit:**

- Bridge conditions (CHASM-B, CHASM-B EXPANSION): [PASS/FAIL]
- Intervention rationale (PART 5, Targets inertia: column): [PASS/FAIL]
- Champion rationale (PART 4, Q-CHAMPION answers): [PASS/FAIL]
- Churn register (PART 3, Q-TRIGGER answers): [PASS/FAIL]

**Gate H result:** [PASS if all four location types contain at least one I-0X citation | FAIL if any location type lacks a citation]

**Revision obligation:** Gate H FAIL → CORRECTION BLOCK with BEFORE and AFTER fields immediately before pre-verification declaration. Do not proceed to SECTION I until written.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate H [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION I — Gate: C-14 Audit (Champion Rationale Double-Anchored)

**Audit:** For each champion, verify archetype-bridge + Q-CHAMPION I-0X both present.

- Champion 1 [name]: archetype-bridge [Y/N] | Q-CHAMPION I-0X [Y/N]
- Champion 2 [name]: archetype-bridge [Y/N] | Q-CHAMPION I-0X [Y/N]
- Champion 3 [name]: archetype-bridge [Y/N] | Q-CHAMPION I-0X [Y/N]

**Gate I result:** [PASS / FAIL]

**Revision obligation:** Gate I FAIL → CORRECTION BLOCK before pre-verification declaration. Do not proceed to SECTION J until written.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate I [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION J — Gate: C-15 Audit (Concrete Retention Actions)

**Audit:** For each SLOT-KEY: churn entry in PART 3, classify Retention intervention: concrete action or surveillance flag.

- [List each SLOT-KEY: [Role] — churn entry and its classification]

**Gate J result:** [PASS / FAIL]

**Revision obligation:** Gate J FAIL → CORRECTION BLOCK before pre-verification declaration. Do not proceed to SECTION K until written.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate J [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION K — Terminal Audit Record

Per-gate execution stamps recorded regardless of outcome. A passing gate with no stamp is unverified.

**Terminal Invariant:** For every gate with "Revision Performed: Yes" in this section, a CORRECTION BLOCK with BEFORE and AFTER fields must exist in the document body at the cited location, above the pre-verification declaration. A "Revision Performed: Yes" entry whose cited location contains no CORRECTION BLOCK, or a CORRECTION BLOCK that contains no BEFORE field, falsifies this invariant.

| Gate | Criterion | Initial result | Revision performed | CORRECTION BLOCK location | Final result |
|------|-----------|----------------|--------------------|--------------------------|--------------|
| H    | C-13      |                | Yes / No           |                          |              |
| I    | C-14      |                | Yes / No           |                          |              |
| J    | C-15      |                | Yes / No           |                          |              |

---

## V-03 — Single Axis: Inertia Framing (SECTION A Downstream Citation Contract)

**Variation axis:** Inertia framing — SECTION A gains a "DOWNSTREAM CITATION CONTRACT" block immediately after the Named Inertia table. This block declares, per I-0X, the structural positions where that ID must appear downstream: which Q-BARRIER phase(s), which champion entries, which churn register entries, and the PART 5 Targets inertia: column. SECTION H's audit is reframed as a check against this declared contract rather than a free-form scan.

**Hypothesis:** SECTION A currently assigns I-01 through I-05 but makes no downstream commitment at assignment time. A model generating PART 3 churn entries has no structural reminder at SECTION A level that I-04 must appear in Late Majority churn entries — it carries that expectation from SECTION H's audit instructions, which appear much later. Adding the DOWNSTREAM CITATION CONTRACT re-asserts the citation expectation at SECTION A generation time: as the model writes `I-04 | Late Majority | [inertia] | [reason]`, the immediately following contract block declares `I-04 expected in: Q-BARRIER PHASE 5, Q-TRIGGER for Late Majority churn entries, PART 5 Targets inertia: column`. The contract creates generation-time pressure across the full document length because citation obligations are declared before any downstream section is written, making the model's citation behavior contract-bound from SECTION A generation. This is the SECTION A analogue of the STRUCTURAL CONTRACT's mandatory co-presence declaration.

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
MECHANISM STATE blockquote footers in SECTIONS H, I, J (gate-level) AND pre-verification declaration before `## VERIFICATION MODE` (boundary-level). Both mandatory regardless of gate outcomes.

Both requirements are mandatory co-present structural features. A document satisfying only one fails C-33 and C-35.

---

## SECTION A — Named Inertia IDs

Assign one Named Inertia ID per canonical Rogers archetype. These IDs are cited throughout all phase bodies, expansion subsections, champion entries, churn triggers, and intervention entries.

| Inertia ID | Archetype      | Named Inertia                      | Structural reason this archetype resists |
|------------|----------------|------------------------------------|------------------------------------------|
| I-01       | Innovator      | [name the inertia for Innovators]  | [structural reason]                      |
| I-02       | Early Adopter  | [name the inertia for EA]          | [structural reason]                      |
| I-03       | Early Majority | [name the inertia for EM]          | [structural reason]                      |
| I-04       | Late Majority  | [name the inertia for LM]          | [structural reason]                      |
| I-05       | Laggard        | [name the inertia for Laggards]    | [structural reason]                      |

**SECTION A DOWNSTREAM CITATION CONTRACT:**
Each Named Inertia ID assigned above is contractually required to appear in the following downstream structural positions. SECTION H will audit against this declared contract.

```
I-01 expected in:
  - Q-BARRIER answer in PHASE 1 INNOVATORS
  - Q-TRIGGER in PART 3 for any Innovator-archetype roles
    (no Innovator roles in PART 3: note exemption)

I-02 expected in:
  - Q-BARRIER answer in PHASE 2 EARLY ADOPTERS
  - Q-CHAMPION answer in PART 4 for any Early Adopter champion
  - Q-TRIGGER in PART 3 for any Early Adopter-archetype roles
    (no EA roles in PART 3: note exemption)

I-03 expected in:
  - Q-BARRIER answers in PHASE 3 CHASM and PHASE 4 EARLY MAJORITY
  - CHASM-B bridge condition body (I-03 is the structural driver of the crossing barrier)
  - PART 2 CHASM-A/B/C EXPANSION Named Inertia in effect: fields
  - Q-TRIGGER in PART 3 for any Early Majority-archetype roles
  - Q-INTERVENTION in at least one PART 5 intervention entry

I-04 expected in:
  - Q-BARRIER answer in PHASE 5 LATE MAJORITY
  - Q-TRIGGER in PART 3 for any Late Majority-archetype roles
  - Q-INTERVENTION in at least one PART 5 intervention entry

I-05 expected in:
  - Q-BARRIER answer in PHASE 6 LAGGARDS
  - Q-TRIGGER in PART 3 for any Laggard-archetype roles
    (no Laggard roles in PART 3: note exemption)
```

An I-0X absent from a declared position represents a backbone gap. SECTION H gate failure is the structural consequence of an unmet contract position.

---

THE INCUMBENT is [name the current workflow, tool, or practice being displaced by {{topic}}]. All phase bodies, champion entries, churn triggers, and interventions run through the displacement lens.

---

## TABLE 1 — Role Archetype Map

TABLE 1 header contract: Each row prefixed SLOT-KEY: — typed structural slot key re-asserting three co-present contracts (archetype assignment, Incumbent Dependency, Inertia ID citation) at this row's generation moment, independently of column headers.

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

Q-BARRIER: Which Named Inertia ID is the primary barrier even for Innovators?
(Cite I-01 from SECTION A — DOWNSTREAM CITATION CONTRACT: I-01 Q-BARRIER position fulfilled here. A different answer requires explicit justification.)

[Phase body: named roles, what they try, signals produced, displacement impact on THE INCUMBENT]

---

## PHASE 2 EARLY ADOPTERS — Month 2–3

Q-BARRIER: Which Named Inertia ID is the primary barrier for Early Adopters?
(Cite I-02 from SECTION A — DOWNSTREAM CITATION CONTRACT: I-02 Q-BARRIER position fulfilled here)

[Phase body: named roles, what they adopt, spread from PHASE 1, incumbent displacement progress]

---

## PHASE 3 CHASM — Month 4 (Non-Adoption Crossing Event)

PHASE 3 is not an adoption phase. No new archetype adopts in Month 4.

Q-BARRIER: Which Named Inertia ID is driving the chasm?
(Cite I-03 from SECTION A — DOWNSTREAM CITATION CONTRACT: I-03's first Q-BARRIER position fulfilled here. A different answer requires explicit justification.)

### CHASM-A — Incumbent Defense

[Named incumbent defense mechanism, load-bearing TABLE 1 Incumbent Dependency values, why crossing requires more than Early Adopter endorsement]

### CHASM-B — Bridge Condition

[Bridge condition as testable proposition — DOWNSTREAM CITATION CONTRACT: I-03's bridge condition citation position fulfilled here. State which I-03 inertia's resolution constitutes the bridge condition.]

### CHASM-C — Early Crossing Signal

[Named crossing signal — role, artifact, or behavioral event; why distinguishable from Early Adopter behavior]

---

## PHASE 4 EARLY MAJORITY — Month 5–7

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Early Majority?
(Cite I-03 from SECTION A — DOWNSTREAM CITATION CONTRACT: I-03's second Q-BARRIER position fulfilled here)

[Phase body: named roles, proof from CHASM-B, TABLE 1 Incumbent Dependency values unblocked, displacement acceleration]

---

## PHASE 5 LATE MAJORITY — Month 8–10

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Late Majority?
(Cite I-04 from SECTION A — DOWNSTREAM CITATION CONTRACT: I-04 Q-BARRIER position fulfilled here)

[Phase body: named roles, adoption trigger, incumbent erosion]

---

## PHASE 6 LAGGARDS — Month 11–12

Q-BARRIER: Which Named Inertia ID keeps Laggards last?
(Cite I-05 from SECTION A — DOWNSTREAM CITATION CONTRACT: I-05 Q-BARRIER position fulfilled here. This is the only structurally correct answer.)

[Phase body: named roles, final adoption conditions, terminal incumbent displacement state]

---

## TABLE 3 — Spread Mechanisms

TABLE 3 header contract: Each row prefixed SLOT-KEY: — typed structural slot key for its canonical transition pair. Spread Mechanism: [named signal or artifact specific to {{topic}} — not generic word-of-mouth]. Generic entries violate the slot-type contract.

| Transition Pair (SLOT-KEY row) | Spread Mechanism: [named signal or artifact specific to {{topic}} — not generic word-of-mouth] | Month Range |
|---|---|---|
| SLOT-KEY: Innovator → Early Adopter      | | |
| SLOT-KEY: Early Adopter → Early Majority | | |
| SLOT-KEY: Early Majority → Late Majority | | |
| SLOT-KEY: Late Majority → Laggard        | | |

---

## PART 2 — CHASM ANALYSIS (Full Expansion)

Three named structural subsections expand PHASE 3's CHASM-A/B/C. Each re-cites the Named Inertia ID from its PHASE 3 Q-BARRIER as the first structural field.

### CHASM-A EXPANSION — Incumbent Defense (Full Diagnosis)

Expanding CHASM-A from PHASE 3 —
Named Inertia in effect: [re-cite I-0X from Q-BARRIER in PHASE 3 CHASM-A — DOWNSTREAM CITATION CONTRACT: I-03's PART 2 CHASM-A EXPANSION position fulfilled here]

[Full diagnosis: complete mechanism — process dependencies, organizational commitments, role-level switching costs. Name every load-bearing TABLE 1 Incumbent Dependency value.]

### CHASM-B EXPANSION — Bridge Condition (Full Specification)

Expanding CHASM-B from PHASE 3 —
Named Inertia in effect: [re-cite I-0X from Q-BARRIER in PHASE 3 CHASM-B — DOWNSTREAM CITATION CONTRACT: I-03's PART 2 CHASM-B EXPANSION position fulfilled here]

[Full specification: bridge condition as testable proposition, precise observable state satisfying it, role or artifact producing that state, TABLE 1 Incumbent Dependency values unblocked.]

### CHASM-C EXPANSION — Crossing Signal (Full Identification)

Expanding CHASM-C from PHASE 3 —
Named Inertia in effect: [re-cite I-0X from Q-BARRIER in PHASE 3 CHASM-C — DOWNSTREAM CITATION CONTRACT: I-03's PART 2 CHASM-C EXPANSION position fulfilled here]

[Full identification: named crossing signal, why distinguishable from Early Adopter behavior, connection to CHASM-B EXPANSION bridge condition, adoption acceleration in PHASE 4.]

---

## PART 3 — Churn Risk Register

Every role at non-trivial churn risk. DOWNSTREAM CITATION CONTRACT: each Q-TRIGGER answer fulfills the corresponding I-0X's churn register citation position.

| Role | Reversion trigger: [specific condition causing reversion to THE INCUMBENT] | Retention intervention: [one concrete action that reduces reversion probability — not a surveillance flag] | Inertia ID driving reversion: [Q-TRIGGER: cite I-0X from SECTION A] |
|------|----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
|      |                                                                            |                                                                                                             |                                                                      |

---

## PART 4 — Champion Network

Name at least three roles. DOWNSTREAM CITATION CONTRACT: each Q-CHAMPION answer fulfills the corresponding I-0X's champion citation position.

(a) Archetype-bridge rationale.
(b) Q-CHAMPION: Named Inertia ID this champion is positioned to overcome (Cite I-0X from SECTION A)

| Champion Role | Archetype | Archetype-bridge rationale | Q-CHAMPION: Named Inertia ID overcome (I-0X) | Why this champion displaces THE INCUMBENT |
|---|---|---|---|---|
|   |   |   |   |   |

---

## PART 5 — Intervention Ranking

DOWNSTREAM CITATION CONTRACT: each Targets inertia: answer fulfills the corresponding I-0X's Q-INTERVENTION citation position. A row without a Named Inertia ID in the Targets inertia column is a contract gap.

| Rank | Intervention | Adoption delta | Phase(s) affected | Role(s) affected | Incumbent Impact: [what THE INCUMBENT loses] | Targets inertia: [I-0X — Q-INTERVENTION: which Named Inertia ID does this intervention directly address?] |
|------|--------------|----------------|-------------------|------------------|----------------------------------------------|----------------------------------------------------------------------------------------------------------|
| 1    |              |                |                   |                  |                                              |                                                                                                          |
| 2    |              |                |                   |                  |                                              |                                                                                                          |
| 3    |              |                |                   |                  |                                              |                                                                                                          |

---

## PART 6 — Sensitivity Analysis

| Scenario        | Adoption outcome | Named lever | Direction of shift |
|-----------------|------------------|-------------|-------------------|
| Fast Adoption   |                  |             |                   |
| Slow Adoption   |                  |             |                   |

---

## PART 7 — Signal Readiness Table

| Signal name | Threshold | Interpretation: what this signal level means for {{topic}} adoption timing |
|-------------|-----------|----------------------------------------------------------------------------|
|             |           |                                                                            |

---

> CORRECTION BLOCK MECHANISM ARMED — no gate failure triggered. If any gate below fails, a CORRECTION BLOCK with BEFORE and AFTER fields will be inserted immediately above this line before proceeding to SECTION K.

## VERIFICATION MODE

All content generation is complete above this boundary. SECTIONS H, I, J, K are audit sections only.

---

## SECTION H — Gate: C-13 Audit (Named Inertia IDs as Downstream Backbone)

**Criterion C-13:** I-0X citations in at least four downstream location types: (1) bridge conditions, (2) intervention rationale, (3) champion rationale, (4) churn register entries.

**Audit against SECTION A DOWNSTREAM CITATION CONTRACT:** For each I-0X, verify declared positions are filled.

- I-01 positions: [PASS/FAIL per declared position]
- I-02 positions: [PASS/FAIL per declared position]
- I-03 positions: [PASS/FAIL per declared position — bridge condition, PART 2 expansions, Q-BARRIER phases]
- I-04 positions: [PASS/FAIL per declared position]
- I-05 positions: [PASS/FAIL per declared position]

**Gate H result:** [PASS if all four location types contain at least one I-0X citation | FAIL if any location type lacks a citation]

**Revision obligation:** Gate H FAIL → CORRECTION BLOCK with BEFORE and AFTER fields before pre-verification declaration. Do not proceed to SECTION I until written.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate H [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION I — Gate: C-14 Audit (Champion Rationale Double-Anchored)

**Audit:** For each champion, verify archetype-bridge + Q-CHAMPION I-0X both present.

- Champion 1 [name]: archetype-bridge [Y/N] | Q-CHAMPION I-0X [Y/N]
- Champion 2 [name]: archetype-bridge [Y/N] | Q-CHAMPION I-0X [Y/N]
- Champion 3 [name]: archetype-bridge [Y/N] | Q-CHAMPION I-0X [Y/N]

**Gate I result:** [PASS / FAIL]

**Revision obligation:** Gate I FAIL → CORRECTION BLOCK before pre-verification declaration. Do not proceed to SECTION J until written.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate I [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION J — Gate: C-15 Audit (Concrete Retention Actions)

**Audit:** For each churn register entry, classify Retention intervention: concrete action or surveillance flag.

- [List each entry and its classification]

**Gate J result:** [PASS / FAIL]

**Revision obligation:** Gate J FAIL → CORRECTION BLOCK before pre-verification declaration. Do not proceed to SECTION K until written.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate J [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION K — Terminal Audit Record

Per-gate execution stamps recorded regardless of outcome.

**Terminal Invariant:** For every gate with "Revision Performed: Yes" in this section, a CORRECTION BLOCK with BEFORE and AFTER fields must exist in the document body at the cited location, above the pre-verification declaration. A "Revision Performed: Yes" entry whose cited location contains no CORRECTION BLOCK, or a CORRECTION BLOCK that contains no BEFORE field, falsifies this invariant.

| Gate | Criterion | Initial result | Revision performed | CORRECTION BLOCK location | Final result |
|------|-----------|----------------|--------------------|--------------------------|--------------|
| H    | C-13      |                | Yes / No           |                          |              |
| I    | C-14      |                | Yes / No           |                          |              |
| J    | C-15      |                | Yes / No           |                          |              |

---

## V-04 — Combined: Output Format + Inertia Framing (PART 3 SLOT-KEY: Rows + SECTION A Citation Contract)

**Variation axes:** V-02 (PART 3 SLOT-KEY: row prefix) + V-03 (SECTION A DOWNSTREAM CITATION CONTRACT)

**Hypothesis:** V-02 and V-03 operate at complementary structural levels without interference. V-03's citation contract is established at SECTION A generation time — before TABLE 1, phases, PART 2, PART 3, PART 4, PART 5 are generated. V-02's SLOT-KEY: prefix operates at PART 3 row generation time — after the contract is established. Together: the contract pre-announces where each I-0X must appear (V-03 effect), and the churn register rows re-assert the three-contract requirement at the point of generation for each specific role (V-02 effect). The two mechanisms create a citation-obligation envelope around churn entries: the model knows at SECTION A that I-04 must appear in Late Majority churn entries (contract), and when generating the Late Majority churn row, the SLOT-KEY: prefix re-asserts the three-contract requirement at that moment. Forward declaration at SECTION A plus backward re-assertion at row level — the PART 3 analogue of the STRUCTURAL CONTRACT's mandatory co-presence pattern.

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
MECHANISM STATE blockquote footers in SECTIONS H, I, J (gate-level) AND pre-verification declaration before `## VERIFICATION MODE` (boundary-level). Both mandatory regardless of gate outcomes.

Both requirements are mandatory co-present structural features. A document satisfying only one fails C-33 and C-35.

---

## SECTION A — Named Inertia IDs

| Inertia ID | Archetype      | Named Inertia                      | Structural reason this archetype resists |
|------------|----------------|------------------------------------|------------------------------------------|
| I-01       | Innovator      | [name the inertia for Innovators]  | [structural reason]                      |
| I-02       | Early Adopter  | [name the inertia for EA]          | [structural reason]                      |
| I-03       | Early Majority | [name the inertia for EM]          | [structural reason]                      |
| I-04       | Late Majority  | [name the inertia for LM]          | [structural reason]                      |
| I-05       | Laggard        | [name the inertia for Laggards]    | [structural reason]                      |

**SECTION A DOWNSTREAM CITATION CONTRACT:**

```
I-01 expected in:
  - Q-BARRIER in PHASE 1 INNOVATORS
  - Q-TRIGGER in PART 3 for any Innovator-archetype roles
    (no Innovator roles in PART 3: note exemption)

I-02 expected in:
  - Q-BARRIER in PHASE 2 EARLY ADOPTERS
  - Q-CHAMPION in PART 4 for any Early Adopter champion
  - Q-TRIGGER in PART 3 for any Early Adopter-archetype roles
    (no EA roles in PART 3: note exemption)

I-03 expected in:
  - Q-BARRIER in PHASE 3 CHASM and PHASE 4 EARLY MAJORITY
  - CHASM-B bridge condition body
  - PART 2 CHASM-A/B/C EXPANSION Named Inertia in effect: fields
  - Q-TRIGGER in PART 3 for any Early Majority-archetype roles
  - Q-INTERVENTION in at least one PART 5 intervention

I-04 expected in:
  - Q-BARRIER in PHASE 5 LATE MAJORITY
  - Q-TRIGGER in PART 3 for any Late Majority-archetype roles
  - Q-INTERVENTION in at least one PART 5 intervention

I-05 expected in:
  - Q-BARRIER in PHASE 6 LAGGARDS
  - Q-TRIGGER in PART 3 for any Laggard-archetype roles
    (no Laggard roles in PART 3: note exemption)
```

SECTION H audits against this declared contract. An I-0X absent from a declared position represents a backbone gap.

---

THE INCUMBENT is [name the current workflow, tool, or practice being displaced by {{topic}}]. All phase bodies, champion entries, churn triggers, and interventions run through the displacement lens.

---

## TABLE 1 — Role Archetype Map

TABLE 1 header contract: Each row prefixed SLOT-KEY: — typed structural slot key re-asserting three co-present contracts (archetype assignment, Incumbent Dependency, Inertia ID citation) at this row's generation moment, independently of column headers.

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

Q-BARRIER: Which Named Inertia ID is the primary barrier even for Innovators?
(Cite I-01 from SECTION A — DOWNSTREAM CITATION CONTRACT: I-01 Q-BARRIER position fulfilled here. A different answer requires explicit justification.)

[Phase body: named roles, what they try, signals produced, displacement impact on THE INCUMBENT]

---

## PHASE 2 EARLY ADOPTERS — Month 2–3

Q-BARRIER: Which Named Inertia ID is the primary barrier for Early Adopters?
(Cite I-02 from SECTION A — DOWNSTREAM CITATION CONTRACT: I-02 Q-BARRIER position fulfilled here)

[Phase body: named roles, what they adopt, spread from PHASE 1, incumbent displacement progress]

---

## PHASE 3 CHASM — Month 4 (Non-Adoption Crossing Event)

PHASE 3 is not an adoption phase. No new archetype adopts in Month 4.

Q-BARRIER: Which Named Inertia ID is driving the chasm?
(Cite I-03 from SECTION A — DOWNSTREAM CITATION CONTRACT: I-03's first Q-BARRIER position fulfilled here. A different answer requires explicit justification.)

### CHASM-A — Incumbent Defense

[Named incumbent defense mechanism, load-bearing TABLE 1 Incumbent Dependency values]

### CHASM-B — Bridge Condition

[Bridge condition as testable proposition — DOWNSTREAM CITATION CONTRACT: I-03's bridge condition position fulfilled here. State which I-03 inertia's resolution constitutes the bridge condition.]

### CHASM-C — Early Crossing Signal

[First observable crossing signal — named role, artifact, or behavioral event]

---

## PHASE 4 EARLY MAJORITY — Month 5–7

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Early Majority?
(Cite I-03 from SECTION A — DOWNSTREAM CITATION CONTRACT: I-03's second Q-BARRIER position fulfilled here)

[Phase body: named roles, proof from CHASM-B, TABLE 1 values unblocked, displacement acceleration]

---

## PHASE 5 LATE MAJORITY — Month 8–10

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Late Majority?
(Cite I-04 from SECTION A — DOWNSTREAM CITATION CONTRACT: I-04 Q-BARRIER position fulfilled here)

[Phase body: named roles, adoption trigger, incumbent erosion]

---

## PHASE 6 LAGGARDS — Month 11–12

Q-BARRIER: Which Named Inertia ID keeps Laggards last?
(Cite I-05 from SECTION A — DOWNSTREAM CITATION CONTRACT: I-05 Q-BARRIER position fulfilled here. This is the only structurally correct answer.)

[Phase body: named roles, final adoption conditions, terminal incumbent displacement state]

---

## TABLE 3 — Spread Mechanisms

TABLE 3 header contract: Each row prefixed SLOT-KEY: — typed structural slot key for its canonical transition pair. Spread Mechanism: [named signal or artifact specific to {{topic}} — not generic word-of-mouth]. Generic entries violate the slot-type contract.

| Transition Pair (SLOT-KEY row) | Spread Mechanism: [named signal or artifact specific to {{topic}} — not generic word-of-mouth] | Month Range |
|---|---|---|
| SLOT-KEY: Innovator → Early Adopter      | | |
| SLOT-KEY: Early Adopter → Early Majority | | |
| SLOT-KEY: Early Majority → Late Majority | | |
| SLOT-KEY: Late Majority → Laggard        | | |

---

## PART 2 — CHASM ANALYSIS (Full Expansion)

Three named structural subsections expand PHASE 3's CHASM-A/B/C. Each re-cites the Named Inertia ID from its PHASE 3 Q-BARRIER as the first structural field.

### CHASM-A EXPANSION — Incumbent Defense (Full Diagnosis)

Expanding CHASM-A from PHASE 3 —
Named Inertia in effect: [re-cite I-0X from Q-BARRIER in PHASE 3 CHASM-A — DOWNSTREAM CITATION CONTRACT: I-03's PART 2 CHASM-A EXPANSION position fulfilled here]

[Full diagnosis: complete mechanism — process dependencies, organizational commitments, role-level switching costs. Name every load-bearing TABLE 1 Incumbent Dependency value.]

### CHASM-B EXPANSION — Bridge Condition (Full Specification)

Expanding CHASM-B from PHASE 3 —
Named Inertia in effect: [re-cite I-0X from Q-BARRIER in PHASE 3 CHASM-B — DOWNSTREAM CITATION CONTRACT: I-03's PART 2 CHASM-B EXPANSION position fulfilled here]

[Full specification: bridge condition as testable proposition, precise observable state satisfying it, role or artifact producing that state, TABLE 1 Incumbent Dependency values unblocked.]

### CHASM-C EXPANSION — Crossing Signal (Full Identification)

Expanding CHASM-C from PHASE 3 —
Named Inertia in effect: [re-cite I-0X from Q-BARRIER in PHASE 3 CHASM-C — DOWNSTREAM CITATION CONTRACT: I-03's PART 2 CHASM-C EXPANSION position fulfilled here]

[Full identification: named crossing signal, why distinguishable from Early Adopter behavior, adoption acceleration in PHASE 4.]

---

## PART 3 — Churn Risk Register

PART 3 header contract: Each row prefixed SLOT-KEY: — typed structural churn slot re-asserting three co-present contracts (reversion trigger | retention intervention | inertia ID) at this row's generation moment, independently of column headers. SECTION A DOWNSTREAM CITATION CONTRACT: each Q-TRIGGER answer fulfills the corresponding I-0X's churn register citation position.

| Role (SLOT-KEY typed churn slot) | Reversion trigger: [specific condition causing reversion to THE INCUMBENT] | Retention intervention: [one concrete action that reduces reversion probability — not a surveillance flag] | Inertia ID driving reversion: [Q-TRIGGER: cite I-0X from SECTION A] |
|----------------------------------|----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| SLOT-KEY: [Role] — churn entry   |                                                                            |                                                                                                             |                                                                      |

---

## PART 4 — Champion Network

Name at least three roles. SECTION A DOWNSTREAM CITATION CONTRACT: each Q-CHAMPION answer fulfills the corresponding I-0X's champion citation position.

(a) Archetype-bridge rationale.
(b) Q-CHAMPION: Named Inertia ID this champion is positioned to overcome (Cite I-0X from SECTION A)

| Champion Role | Archetype | Archetype-bridge rationale | Q-CHAMPION: Named Inertia ID overcome (I-0X) | Why this champion displaces THE INCUMBENT |
|---|---|---|---|---|
|   |   |   |   |   |

---

## PART 5 — Intervention Ranking

SECTION A DOWNSTREAM CITATION CONTRACT: each Targets inertia: answer fulfills the corresponding I-0X's Q-INTERVENTION position. A row without a Named Inertia ID in Targets inertia is a contract gap.

| Rank | Intervention | Adoption delta | Phase(s) affected | Role(s) affected | Incumbent Impact: [what THE INCUMBENT loses] | Targets inertia: [I-0X — Q-INTERVENTION: which Named Inertia ID does this intervention directly address?] |
|------|--------------|----------------|-------------------|------------------|----------------------------------------------|----------------------------------------------------------------------------------------------------------|
| 1    |              |                |                   |                  |                                              |                                                                                                          |
| 2    |              |                |                   |                  |                                              |                                                                                                          |
| 3    |              |                |                   |                  |                                              |                                                                                                          |

---

## PART 6 — Sensitivity Analysis

| Scenario        | Adoption outcome | Named lever | Direction of shift |
|-----------------|------------------|-------------|-------------------|
| Fast Adoption   |                  |             |                   |
| Slow Adoption   |                  |             |                   |

---

## PART 7 — Signal Readiness Table

| Signal name | Threshold | Interpretation: what this signal level means for {{topic}} adoption timing |
|-------------|-----------|----------------------------------------------------------------------------|
|             |           |                                                                            |

---

> CORRECTION BLOCK MECHANISM ARMED — no gate failure triggered. If any gate below fails, a CORRECTION BLOCK with BEFORE and AFTER fields will be inserted immediately above this line before proceeding to SECTION K.

## VERIFICATION MODE

All content generation is complete above this boundary. SECTIONS H, I, J, K are audit sections only.

---

## SECTION H — Gate: C-13 Audit (Named Inertia IDs as Downstream Backbone)

**Criterion C-13:** I-0X citations in at least four downstream location types: (1) bridge conditions, (2) intervention rationale, (3) champion rationale, (4) churn register entries.

**Audit against SECTION A DOWNSTREAM CITATION CONTRACT:**

- I-01 positions: [PASS/FAIL per declared position]
- I-02 positions: [PASS/FAIL per declared position]
- I-03 positions: [PASS/FAIL per declared position — bridge condition, PART 2 expansions, Q-BARRIER phases]
- I-04 positions: [PASS/FAIL per declared position]
- I-05 positions: [PASS/FAIL per declared position]

**Gate H result:** [PASS if all four location types contain at least one I-0X citation | FAIL if any location type lacks a citation]

**Revision obligation:** Gate H FAIL → CORRECTION BLOCK with BEFORE and AFTER fields before pre-verification declaration. Do not proceed to SECTION I until written.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate H [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION I — Gate: C-14 Audit (Champion Rationale Double-Anchored)

**Audit:** For each champion, verify archetype-bridge + Q-CHAMPION I-0X both present.

- Champion 1 [name]: archetype-bridge [Y/N] | Q-CHAMPION I-0X [Y/N]
- Champion 2 [name]: archetype-bridge [Y/N] | Q-CHAMPION I-0X [Y/N]
- Champion 3 [name]: archetype-bridge [Y/N] | Q-CHAMPION I-0X [Y/N]

**Gate I result:** [PASS / FAIL]

**Revision obligation:** Gate I FAIL → CORRECTION BLOCK before pre-verification declaration. Do not proceed to SECTION J until written.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate I [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION J — Gate: C-15 Audit (Concrete Retention Actions)

**Audit:** For each SLOT-KEY: churn entry, classify Retention intervention: concrete action or surveillance flag.

- [List each SLOT-KEY: [Role] — churn entry and its classification]

**Gate J result:** [PASS / FAIL]

**Revision obligation:** Gate J FAIL → CORRECTION BLOCK before pre-verification declaration. Do not proceed to SECTION K until written.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate J [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION K — Terminal Audit Record

**Terminal Invariant:** For every gate with "Revision Performed: Yes," a CORRECTION BLOCK with BEFORE and AFTER fields must exist at the cited location above the pre-verification declaration. A "Revision Performed: Yes" entry whose cited location contains no CORRECTION BLOCK, or a CORRECTION BLOCK that contains no BEFORE field, falsifies this invariant.

| Gate | Criterion | Initial result | Revision performed | CORRECTION BLOCK location | Final result |
|------|-----------|----------------|--------------------|--------------------------|--------------|
| H    | C-13      |                | Yes / No           |                          |              |
| I    | C-14      |                | Yes / No           |                          |              |
| J    | C-15      |                | Yes / No           |                          |              |

---

## V-05 — Full: All Three Axes (Phase-Close Ledger + PART 3 SLOT-KEY: + SECTION A Citation Contract)

**Variation axes:** V-01 (phase-close displacement ledger) + V-02 (PART 3 SLOT-KEY: row prefix) + V-03 (SECTION A DOWNSTREAM CITATION CONTRACT)

**Hypothesis:** All three axes are purely additive and operate at non-overlapping structural levels. V-03's citation contract is established at SECTION A generation time — it pre-announces citation obligations for the entire document before any downstream section is generated. V-01's phase-close ledger creates a mandatory inertia accounting step at phase exit — after the phase body and before the phase separator — adding a second per-phase answer-form anchor in addition to Q-BARRIER at phase entry. V-02's PART 3 SLOT-KEY: prefix re-asserts the three churn contracts at each churn row generation moment. Together, these three axes create citation-enforcement pressure at four structural levels: (1) pre-document via SECTION A contract, (2) phase-entry via Q-BARRIER, (3) phase-exit via displacement ledger, (4) PART 3 row-level via SLOT-KEY: re-assertion. The inertia backbone is enforced from its first assignment through every downstream usage location — pre-announced, phase-tracked, and row-level re-asserted. Projected ceiling: 265/270 (C-19 paradox persists in architecturally strong designs where all gates pass on first attempt).

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

Assign one Named Inertia ID per canonical Rogers archetype. These IDs are cited throughout all phase bodies, expansion subsections, champion entries, churn triggers, and intervention entries.

| Inertia ID | Archetype      | Named Inertia                      | Structural reason this archetype resists |
|------------|----------------|------------------------------------|------------------------------------------|
| I-01       | Innovator      | [name the inertia for Innovators]  | [structural reason]                      |
| I-02       | Early Adopter  | [name the inertia for EA]          | [structural reason]                      |
| I-03       | Early Majority | [name the inertia for EM]          | [structural reason]                      |
| I-04       | Late Majority  | [name the inertia for LM]          | [structural reason]                      |
| I-05       | Laggard        | [name the inertia for Laggards]    | [structural reason]                      |

**SECTION A DOWNSTREAM CITATION CONTRACT:**

```
I-01 expected in:
  - Q-BARRIER in PHASE 1 INNOVATORS
  - Phase-close displacement ledger in PHASE 1 (Inertia ID this phase overcame:)
  - Q-TRIGGER in PART 3 for any Innovator-archetype roles
    (no Innovator roles in PART 3: note exemption)

I-02 expected in:
  - Q-BARRIER in PHASE 2 EARLY ADOPTERS
  - Phase-close displacement ledger in PHASE 2 (Inertia ID this phase overcame:)
  - Q-CHAMPION in PART 4 for any Early Adopter champion
  - Q-TRIGGER in PART 3 for any Early Adopter-archetype roles
    (no EA roles in PART 3: note exemption)

I-03 expected in:
  - Q-BARRIER in PHASE 3 CHASM and PHASE 4 EARLY MAJORITY
  - Phase-close displacement ledger in PHASE 3 (Inertia ID defending THE INCUMBENT:)
  - Phase-close displacement ledger in PHASE 4 (Inertia ID this phase overcame:)
  - CHASM-B bridge condition body
  - PART 2 CHASM-A/B/C EXPANSION Named Inertia in effect: fields
  - Q-TRIGGER in PART 3 for any Early Majority-archetype roles
  - Q-INTERVENTION in at least one PART 5 intervention

I-04 expected in:
  - Q-BARRIER in PHASE 5 LATE MAJORITY
  - Phase-close displacement ledger in PHASE 5 (Inertia ID this phase overcame:)
  - Q-TRIGGER in PART 3 for any Late Majority-archetype roles
  - Q-INTERVENTION in at least one PART 5 intervention

I-05 expected in:
  - Q-BARRIER in PHASE 6 LAGGARDS
  - Phase-close displacement ledger in PHASE 6 (Inertia ID this phase overcame:)
  - Q-TRIGGER in PART 3 for any Laggard-archetype roles
    (no Laggard roles in PART 3: note exemption)
```

SECTION H audits against this declared contract. An I-0X absent from a declared position represents a backbone gap.

---

THE INCUMBENT is [name the current workflow, tool, or practice being displaced by {{topic}}]. All phase bodies, champion entries, churn triggers, and interventions run through the displacement lens: what does this phase do to THE INCUMBENT's position?

---

## TABLE 1 — Role Archetype Map

TABLE 1 header contract: Each row prefixed SLOT-KEY: — typed structural slot key re-asserting three co-present contracts (archetype assignment, Incumbent Dependency, Inertia ID citation) at this row's generation moment, independently of column headers.

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

Which roles adopt in Month 1? Name them and their archetype assignment from TABLE 1. What does THE INCUMBENT lose in this phase?

Q-BARRIER: Which Named Inertia ID is the primary barrier even for Innovators?
(Cite I-01 from SECTION A — DOWNSTREAM CITATION CONTRACT: I-01 Q-BARRIER position fulfilled here. A different answer requires explicit justification.)

[Phase body: named roles, what they try, signals produced, displacement impact on THE INCUMBENT]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what workflow, process, or role dependency THE INCUMBENT retains after Month 1 — be specific]
Inertia ID this phase overcame (partially): [re-cite I-01 from Q-BARRIER — DOWNSTREAM CITATION CONTRACT: I-01 phase-close ledger position fulfilled here]

---

## PHASE 2 EARLY ADOPTERS — Month 2–3

Which roles adopt in Months 2–3? What evidence from PHASE 1 persuades them?

Q-BARRIER: Which Named Inertia ID is the primary barrier for Early Adopters?
(Cite I-02 from SECTION A — DOWNSTREAM CITATION CONTRACT: I-02 Q-BARRIER position fulfilled here)

[Phase body: named roles, what they adopt, spread from PHASE 1, incumbent displacement progress]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what THE INCUMBENT still controls after Month 3 — which TABLE 1 Incumbent Dependency values remain load-bearing]
Inertia ID this phase overcame (partially): [re-cite I-02 — DOWNSTREAM CITATION CONTRACT: I-02 phase-close ledger position fulfilled here]

---

## PHASE 3 CHASM — Month 4 (Non-Adoption Crossing Event)

PHASE 3 is not an adoption phase. No new archetype adopts in Month 4.

Q-BARRIER: Which Named Inertia ID is driving the chasm?
(Cite I-03 from SECTION A — DOWNSTREAM CITATION CONTRACT: I-03's first Q-BARRIER position fulfilled here. A different answer requires explicit justification.)

### CHASM-A — Incumbent Defense

[Named defense mechanism, load-bearing TABLE 1 Incumbent Dependency values, why crossing requires more than Early Adopter endorsement]

### CHASM-B — Bridge Condition

[Bridge condition as testable proposition — DOWNSTREAM CITATION CONTRACT: I-03's bridge condition position fulfilled here. State which I-03 inertia's resolution constitutes the bridge condition.]

### CHASM-C — Early Crossing Signal

[Named crossing signal — role, artifact, or behavioral event; why distinguishable from Early Adopter behavior]

**Phase-close displacement ledger:**
Inertia ID defending THE INCUMBENT at this boundary: [I-03 — DOWNSTREAM CITATION CONTRACT: I-03 PHASE 3 phase-close ledger position fulfilled here]

---

## PHASE 4 EARLY MAJORITY — Month 5–7

Which roles adopt in Months 5–7? What bridge condition from CHASM-B is now satisfied?

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Early Majority?
(Cite I-03 from SECTION A — DOWNSTREAM CITATION CONTRACT: I-03's second Q-BARRIER position fulfilled here)

[Phase body: named roles, proof from CHASM-B, TABLE 1 Incumbent Dependency values now unblocked, displacement acceleration]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what THE INCUMBENT still controls after Month 7 — remaining TABLE 1 Incumbent Dependency values]
Inertia ID this phase overcame (partially): [re-cite I-03 — DOWNSTREAM CITATION CONTRACT: I-03 PHASE 4 phase-close ledger position fulfilled here]

---

## PHASE 5 LATE MAJORITY — Month 8–10

Which roles adopt in Months 8–10? Reference their high Incumbent Dependency values from TABLE 1.

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Late Majority?
(Cite I-04 from SECTION A — DOWNSTREAM CITATION CONTRACT: I-04 Q-BARRIER position fulfilled here)

[Phase body: named roles, adoption trigger, incumbent erosion]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what THE INCUMBENT still controls after Month 10]
Inertia ID this phase overcame (partially): [re-cite I-04 — DOWNSTREAM CITATION CONTRACT: I-04 phase-close ledger position fulfilled here]

---

## PHASE 6 LAGGARDS — Month 11–12

Which roles adopt last? What finally moves them?

Q-BARRIER: Which Named Inertia ID keeps Laggards last?
(Cite I-05 from SECTION A — DOWNSTREAM CITATION CONTRACT: I-05 Q-BARRIER position fulfilled here. This is the only structurally correct answer.)

[Phase body: named roles, final adoption conditions, terminal incumbent displacement state]

**Phase-close displacement ledger:**
Incumbent position after this phase: [terminal displacement state — what, if anything, THE INCUMBENT retains after Month 12]
Inertia ID this phase overcame: [re-cite I-05 — DOWNSTREAM CITATION CONTRACT: I-05 phase-close ledger position fulfilled here]

---

## TABLE 3 — Spread Mechanisms

TABLE 3 header contract: Each row prefixed SLOT-KEY: — typed structural slot key for its canonical transition pair. Spread Mechanism: [named signal or artifact specific to {{topic}} — not generic word-of-mouth]. Generic entries violate the slot-type contract.

| Transition Pair (SLOT-KEY row) | Spread Mechanism: [named signal or artifact specific to {{topic}} — not generic word-of-mouth] | Month Range |
|---|---|---|
| SLOT-KEY: Innovator → Early Adopter      | | |
| SLOT-KEY: Early Adopter → Early Majority | | |
| SLOT-KEY: Early Majority → Late Majority | | |
| SLOT-KEY: Late Majority → Laggard        | | |

---

## PART 2 — CHASM ANALYSIS (Full Expansion)

Three named structural subsections expand PHASE 3's CHASM-A/B/C. Each re-cites the Named Inertia ID from its PHASE 3 Q-BARRIER as the first structural field.

### CHASM-A EXPANSION — Incumbent Defense (Full Diagnosis)

Expanding CHASM-A from PHASE 3 —
Named Inertia in effect: [re-cite I-0X from Q-BARRIER in PHASE 3 CHASM-A — DOWNSTREAM CITATION CONTRACT: I-03's PART 2 CHASM-A EXPANSION position fulfilled here]

[Full diagnosis: complete mechanism — process dependencies, organizational commitments, role-level switching costs. Name every load-bearing TABLE 1 Incumbent Dependency value. Identify which Early Majority roles are most defended.]

### CHASM-B EXPANSION — Bridge Condition (Full Specification)

Expanding CHASM-B from PHASE 3 —
Named Inertia in effect: [re-cite I-0X from Q-BARRIER in PHASE 3 CHASM-B — DOWNSTREAM CITATION CONTRACT: I-03's PART 2 CHASM-B EXPANSION position fulfilled here]

[Full specification: bridge condition as testable proposition, precise observable state satisfying it, role or artifact producing that state, TABLE 1 Incumbent Dependency values unblocked.]

### CHASM-C EXPANSION — Crossing Signal (Full Identification)

Expanding CHASM-C from PHASE 3 —
Named Inertia in effect: [re-cite I-0X from Q-BARRIER in PHASE 3 CHASM-C — DOWNSTREAM CITATION CONTRACT: I-03's PART 2 CHASM-C EXPANSION position fulfilled here]

[Full identification: named crossing signal, why distinguishable from Early Adopter behavior, connection to CHASM-B EXPANSION bridge condition, adoption acceleration in PHASE 4.]

---

## PART 3 — Churn Risk Register

PART 3 header contract: Each row prefixed SLOT-KEY: — typed structural churn slot re-asserting three co-present contracts (reversion trigger | retention intervention | inertia ID) at this row's generation moment, independently of column headers. SECTION A DOWNSTREAM CITATION CONTRACT: each Q-TRIGGER answer fulfills the corresponding I-0X's churn register citation position.

| Role (SLOT-KEY typed churn slot) | Reversion trigger: [specific condition causing reversion to THE INCUMBENT] | Retention intervention: [one concrete action that reduces reversion probability — not a surveillance flag] | Inertia ID driving reversion: [Q-TRIGGER: cite I-0X from SECTION A] |
|----------------------------------|----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| SLOT-KEY: [Role] — churn entry   |                                                                            |                                                                                                             |                                                                      |

---

## PART 4 — Champion Network

Name at least three roles. SECTION A DOWNSTREAM CITATION CONTRACT: each Q-CHAMPION answer fulfills the corresponding I-0X's champion citation position.

(a) Archetype-bridge rationale.
(b) Q-CHAMPION: Named Inertia ID this champion is positioned to overcome (Cite I-0X from SECTION A)

| Champion Role | Archetype | Archetype-bridge rationale | Q-CHAMPION: Named Inertia ID overcome (I-0X) | Why this champion displaces THE INCUMBENT for the target tier |
|---|---|---|---|---|
|   |   |   |   |   |

---

## PART 5 — Intervention Ranking

SECTION A DOWNSTREAM CITATION CONTRACT: each Targets inertia: answer fulfills the corresponding I-0X's Q-INTERVENTION position. A row without a Named Inertia ID in Targets inertia is a contract gap.

| Rank | Intervention | Adoption delta | Phase(s) affected | Role(s) affected | Incumbent Impact: [what THE INCUMBENT loses when this intervention succeeds] | Targets inertia: [I-0X — Q-INTERVENTION: which Named Inertia ID does this intervention directly address?] |
|------|--------------|----------------|-------------------|------------------|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| 1    |              |                |                   |                  |                                                                              |                                                                                                          |
| 2    |              |                |                   |                  |                                                                              |                                                                                                          |
| 3    |              |                |                   |                  |                                                                              |                                                                                                          |

---

## PART 6 — Sensitivity Analysis

| Scenario        | Adoption outcome | Named lever | Direction of shift |
|-----------------|------------------|-------------|-------------------|
| Fast Adoption   |                  |             |                   |
| Slow Adoption   |                  |             |                   |

---

## PART 7 — Signal Readiness Table

| Signal name | Threshold | Interpretation: what this signal level means for {{topic}} adoption timing |
|-------------|-----------|----------------------------------------------------------------------------|
|             |           |                                                                            |

---

> CORRECTION BLOCK MECHANISM ARMED — no gate failure triggered. If any gate below fails, a CORRECTION BLOCK with BEFORE and AFTER fields will be inserted immediately above this line before proceeding to SECTION K.

## VERIFICATION MODE

All content generation is complete above this boundary. SECTIONS H, I, J, K are audit sections only. No content generation occurs below this line.

---

## SECTION H — Gate: C-13 Audit (Named Inertia IDs as Downstream Backbone)

**Criterion C-13:** I-0X citations in at least four downstream location types: (1) bridge conditions, (2) intervention rationale, (3) champion rationale, (4) churn register entries.

**Audit against SECTION A DOWNSTREAM CITATION CONTRACT:** For each I-0X, verify declared positions are filled. Phase-close ledger positions count as additional citation evidence but do not substitute for the four C-13 location types.

- I-01 positions: [PASS/FAIL per declared position — note phase-close ledger entry if present]
- I-02 positions: [PASS/FAIL per declared position — note phase-close ledger entry if present]
- I-03 positions: [PASS/FAIL per declared position — bridge condition, PART 2 expansions, Q-BARRIER phases, phase-close ledgers]
- I-04 positions: [PASS/FAIL per declared position — note phase-close ledger entry if present]
- I-05 positions: [PASS/FAIL per declared position — note phase-close ledger entry if present]

**C-13 location type summary:**
- Bridge conditions (CHASM-B, CHASM-B EXPANSION): [PASS/FAIL]
- Intervention rationale (PART 5, Targets inertia: column): [PASS/FAIL]
- Champion rationale (PART 4, Q-CHAMPION answers): [PASS/FAIL]
- Churn register (PART 3, Q-TRIGGER answers): [PASS/FAIL]

**Gate H result:** [PASS if all four location types contain at least one I-0X citation | FAIL if any location type lacks a citation]

**Revision obligation:** Gate H FAIL → CORRECTION BLOCK with BEFORE and AFTER fields before pre-verification declaration. Do not proceed to SECTION I until written.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate H [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION I — Gate: C-14 Audit (Champion Rationale Double-Anchored)

**Audit:** For each champion, verify archetype-bridge + Q-CHAMPION I-0X both present.

- Champion 1 [name]: archetype-bridge [Y/N] | Q-CHAMPION I-0X [Y/N]
- Champion 2 [name]: archetype-bridge [Y/N] | Q-CHAMPION I-0X [Y/N]
- Champion 3 [name]: archetype-bridge [Y/N] | Q-CHAMPION I-0X [Y/N]

**Gate I result:** [PASS / FAIL]

**Revision obligation:** Gate I FAIL → CORRECTION BLOCK before pre-verification declaration. Do not proceed to SECTION J until written.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate I [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION J — Gate: C-15 Audit (Concrete Retention Actions)

**Audit:** For each SLOT-KEY: churn entry in PART 3, classify Retention intervention: concrete action or surveillance flag.

- [List each SLOT-KEY: [Role] — churn entry and its classification]

**Gate J result:** [PASS / FAIL]

**Revision obligation:** Gate J FAIL → CORRECTION BLOCK before pre-verification declaration. Do not proceed to SECTION K until written.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate J [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION K — Terminal Audit Record

Per-gate execution stamps recorded regardless of outcome. A terminal section recording only failures is incomplete; a passing gate with no stamp is unverified audit execution.

**Terminal Invariant:** For every gate with "Revision Performed: Yes" in this section, a CORRECTION BLOCK with BEFORE and AFTER fields must exist in the document body at the cited location, above the pre-verification declaration. A "Revision Performed: Yes" entry whose cited location contains no CORRECTION BLOCK, or a CORRECTION BLOCK that contains no BEFORE field, falsifies this invariant.

| Gate | Criterion | Initial result | Revision performed | CORRECTION BLOCK location | Final result |
|------|-----------|----------------|--------------------|--------------------------|--------------|
| H    | C-13      |                | Yes / No           |                          |              |
| I    | C-14      |                | Yes / No           |                          |              |
| J    | C-15      |                | Yes / No           |                          |              |
