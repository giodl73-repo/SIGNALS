# Variations: listen-adoption — Round 14

**Rubric:** v14 | **New criteria:** C-40, C-41 | **Max composite:** 255 | **Golden threshold:** 80% (~204 pts)

---

## Variation Axes

| Axis | R14 Target | Description |
|------|-----------|-------------|
| Lifecycle emphasis | C-40+: PART 2 inertia propagation | Each CHASM-X EXPANSION re-cites Named Inertia ID from PHASE 3's Q-BARRIER answer as a per-subsection structural field — extends C-40's slot enforcement into the inertia-citation dimension |
| Role sequence | TABLE 1 SLOT-KEY: row prefix | C-38 pattern applied to TABLE 1 rows — each row re-asserts the three-contract typed slot (archetype + incumbent dependency + inertia ID) independently of the header |
| Inertia framing | PART 5 inertia targeting column | Intervention ranking table gains `Targets inertia: [I-0X — Named Inertia ID this intervention directly addresses]` per entry — new downstream backbone citation location |
| Phrasing register | Baseline | Carried from R13 V-05 |
| Output format | Baseline | Carried from R13 V-05: SLOT-KEY: TABLE 3, typed TABLE 3 header, PART 5 Incumbent Impact |

**Single-axis (V-01, V-02, V-03):** Lifecycle emphasis · Role sequence · Inertia framing
**Combined (V-04):** Role sequence + Inertia framing
**Full (V-05):** Lifecycle emphasis + Role sequence + Inertia framing

**Baseline (all five carry from R13 V-05):**

| Element | Criterion | Form |
|---|---|---|
| STRUCTURAL CONTRACT naming answer-form questions AND MECHANISM STATE | C-35 | Block before SECTION A |
| Per-gate MECHANISM STATE footers in SECTIONS H, I, J | C-34 (gate-level anchor) | `> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — [state]` |
| Pre-verification MECHANISM STATE declaration before `## VERIFICATION MODE` | C-34 (boundary-level anchor) | `> CORRECTION BLOCK MECHANISM ARMED — no gate failure triggered` |
| SECTION A Named Inertia IDs, I-01 through I-05 | C-11 | Table: Inertia ID | Archetype | Named Inertia | Structural reason |
| TABLE 1 with Incumbent Dependency column (3rd) AND Inertia ID column (4th) | C-41, C-37 | Four-column table, three contracts co-present per row |
| PHASE 3 CHASM with CHASM-A / CHASM-B / CHASM-C structural subsections | C-39 | Named subsection headers per required element |
| PART 2 with CHASM-A EXPANSION / CHASM-B EXPANSION / CHASM-C EXPANSION and PHASE 3 back-references | C-40 | Three named expansion subsections with explicit "Expanding CHASM-X from PHASE 3 —" back-references |
| TABLE 3 typed header + SLOT-KEY: row labels + specificity constraint in column label | C-36, C-38, C-28 | Header names rows as typed structural slot keys |
| PART 5 intervention table with Incumbent Impact column | C-26 extension | Column: `Incumbent Impact: [what THE INCUMBENT loses when this intervention succeeds]` |

**Axis activation map:**

| Variation | Axis A: PART 2 inertia propagation | Axis B: TABLE 1 SLOT-KEY: rows | Axis C: PART 5 inertia targeting | Delta from R13 V-05 baseline |
|---|---|---|---|---|
| V-01 | **Active:** per-subsection `Named Inertia in effect: I-0X` field | Baseline (no SLOT-KEY: prefix) | Baseline (no Targets inertia column) | PART 2 expansion carries Named Inertia ID per slot |
| V-02 | Baseline | **Active:** `SLOT-KEY: [Role]` prefix on TABLE 1 rows | Baseline | TABLE 1 rows self-describing as three-contract typed slots |
| V-03 | Baseline | Baseline | **Active:** `Targets inertia: I-0X` column in PART 5 | Intervention table gains inertia-targeting structural slot |
| V-04 | Baseline | Active (V-02) | Active (V-03) | TABLE 1 row-level + intervention inertia targeting |
| V-05 | Active (V-01) | Active (V-02) | Active (V-03) | All three axes: PART 2 inertia carry-forward + TABLE 1 SLOT-KEY + PART 5 inertia targeting |

---

## V-01 — Single Axis: Lifecycle Emphasis (PART 2 Inertia ID Propagation)

**Variation axis:** Lifecycle emphasis — each CHASM-X EXPANSION subsection in PART 2 carries
the Named Inertia ID forward from PHASE 3's Q-BARRIER answer as its first structural field:
`Named Inertia in effect: [re-cite I-0X from Q-BARRIER in PHASE 3 CHASM-X]`. The PHASE 3
sketch identifies the inertia driving each chasm element; PART 2's expansion of that element
now re-asserts the same inertia citation at expansion depth, making the Named Inertia ID a
per-slot carry-forward contract rather than a once-per-phase answer.

**Hypothesis:** C-40 enforces structural slot count — three named expansion subsections, each
with a PHASE 3 back-reference. The inertia citation (I-0X from Q-BARRIER) is resolved in PHASE
3's CHASM-X subsection and is thereafter available only from memory during PART 2 generation.
Adding `Named Inertia in effect:` as the first fill-field of each expansion subsection re-asserts
the citation contract at PART 2 generation time, making inertia propagation structurally
required per slot rather than optionally carried from PHASE 3 context. A model completing
CHASM-A EXPANSION cannot omit the Named Inertia re-citation without leaving an empty structural
field, identical enforcement class to the SLOT-KEY: row pattern in TABLE 3.

---

Simulate the adoption curve for {{topic}} across the 16 stock roles (PM, UX, C-01 through C-12,
Support, SRE). Produce the artifact below in full. Every bracketed instruction is a fill
contract — complete it before proceeding to the next section.

---

## STRUCTURAL CONTRACT

This document encodes two mandatory co-present architectural requirements. No variation or
omission of either is permitted.

**REQUIREMENT 1 — ANSWER-FORM CITATION ENFORCEMENT (C-29):**
Named Inertia ID citations throughout this document are answers to explicit answer-form
questions embedded in structural positions. The following questions are mandatory; each
requires a Named Inertia ID (I-0X) as its coherent answer:

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
A MECHANISM STATE line appears as a blockquote footer inside each of SECTIONS H, I, J
(gate-level anchor) AND as a pre-verification declaration immediately before
`## VERIFICATION MODE` (boundary-level anchor). Both anchors are mandatory regardless of
gate outcomes.

Both requirements are mandatory co-present structural features. A document satisfying only
one fails C-33 and C-35.

---

## SECTION A — Named Inertia IDs

Assign one Named Inertia ID per canonical Rogers archetype. The inertia is the structural
reason that archetype resists adoption of {{topic}}. These IDs are cited by Q-BARRIER
throughout all phase bodies, expansion subsections, champion entries, churn triggers, and
intervention entries.

| Inertia ID | Archetype      | Named Inertia                      | Structural reason this archetype resists |
|------------|----------------|------------------------------------|------------------------------------------|
| I-01       | Innovator      | [name the inertia for Innovators]  | [structural reason]                      |
| I-02       | Early Adopter  | [name the inertia for EA]          | [structural reason]                      |
| I-03       | Early Majority | [name the inertia for EM]          | [structural reason]                      |
| I-04       | Late Majority  | [name the inertia for LM]          | [structural reason]                      |
| I-05       | Laggard        | [name the inertia for Laggards]    | [structural reason]                      |

---

THE INCUMBENT is [name the current workflow, tool, or practice being displaced by {{topic}}].
All phase bodies, champion entries, churn triggers, and interventions run through the
displacement lens: what does this phase do to THE INCUMBENT's position?

---

## TABLE 1 — Role Archetype Map

Assign every stock role to a canonical Rogers archetype. The Incumbent Dependency column
records the specific workflow step this role currently relies on THE INCUMBENT to perform —
the higher the dependency, the later the expected adoption phase. The Inertia ID column cites
the Named Inertia ID from SECTION A that explains this role's structural resistance at
TABLE 1 generation time.

Three contracts are co-present per row: archetype assignment (C-01), Incumbent Dependency
(C-37), and Inertia ID citation (C-41). A row is not complete until all three are filled.

| Role    | Rogers Archetype | Incumbent Dependency: [workflow step this role relies on THE INCUMBENT to perform] | Inertia ID: [cite I-0X from SECTION A — named inertia explaining this role's resistance] |
|---------|-----------------|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| PM      |                 |                                                                                    |                                                                                          |
| UX      |                 |                                                                                    |                                                                                          |
| C-01    |                 |                                                                                    |                                                                                          |
| C-02    |                 |                                                                                    |                                                                                          |
| C-03    |                 |                                                                                    |                                                                                          |
| C-04    |                 |                                                                                    |                                                                                          |
| C-05    |                 |                                                                                    |                                                                                          |
| C-06    |                 |                                                                                    |                                                                                          |
| C-07    |                 |                                                                                    |                                                                                          |
| C-08    |                 |                                                                                    |                                                                                          |
| C-09    |                 |                                                                                    |                                                                                          |
| C-10    |                 |                                                                                    |                                                                                          |
| C-11    |                 |                                                                                    |                                                                                          |
| C-12    |                 |                                                                                    |                                                                                          |
| Support |                 |                                                                                    |                                                                                          |
| SRE     |                 |                                                                                    |                                                                                          |

---

## PHASE 1 INNOVATORS — Month 1

Which roles adopt in Month 1? Name them and their archetype assignment from TABLE 1.
What does THE INCUMBENT lose in this phase?

Q-BARRIER: Which Named Inertia ID is the primary barrier even for Innovators?
(Cite I-01 from SECTION A — this question's structurally correct answer is I-01,
the Innovator inertia. A different answer requires explicit justification.)

[Phase body: named roles, what they try, what signals they produce, displacement impact on
THE INCUMBENT's position]

---

## PHASE 2 EARLY ADOPTERS — Month 2–3

Which roles adopt in Months 2–3? What evidence from PHASE 1 persuades them?

Q-BARRIER: Which Named Inertia ID is the primary barrier for Early Adopters?
(Cite I-02 from SECTION A)

[Phase body: named roles, what they adopt, spread mechanism from PHASE 1, incumbent
displacement progress]

---

## PHASE 3 CHASM — Month 4 (Non-Adoption Crossing Event)

PHASE 3 is not an adoption phase. It is a crossing event. No new archetype adopts in Month 4.
The chasm is diagnosed below using three named structural subsections.

Q-BARRIER: Which Named Inertia ID is driving the chasm?
(Cite I-03 from SECTION A — the Early Majority archetype inertia is the structural
driver of the chasm. A different answer requires explicit justification.)

### CHASM-A — Incumbent Defense

What defends THE INCUMBENT's position among the Early Majority and Late Majority?
Name the specific workflow dependency, process lock-in, or organizational force that makes
THE INCUMBENT defensible at this boundary.

[CHASM-A body: named incumbent defense mechanism, which TABLE 1 Incumbent Dependency values
are load-bearing here, why crossing requires more than Early Adopter endorsement]

### CHASM-B — Bridge Condition

What single condition must hold for the Early Majority to cross? State it as a testable
proposition: "The chasm is crossed when [specific observable condition]."

[CHASM-B body: the bridge condition, which roles must satisfy it, what artifact or signal
proves it is met, connection to THE INCUMBENT's weakest dependency point]

### CHASM-C — Early Crossing Signal

What is the first observable signal that the chasm has been crossed? Name a specific role,
artifact, or behavioral event — not a metric threshold — that indicates Early Majority
adoption has begun.

[CHASM-C body: named crossing signal, which role emits it, what it proves about the bridge
condition from CHASM-B, why it is distinguishable from Early Adopter behavior]

---

## PHASE 4 EARLY MAJORITY — Month 5–7

Which roles adopt in Months 5–7? What bridge condition from CHASM-B is now satisfied?

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Early Majority?
(Cite I-03 from SECTION A)

[Phase body: named roles, what proof from CHASM-B allows these roles to adopt, reference
TABLE 1 Incumbent Dependency values now unblocked, incumbent displacement acceleration]

---

## PHASE 5 LATE MAJORITY — Month 8–10

Which roles adopt in Months 8–10? What social proof from PHASE 4 reaches them?
Reference their high Incumbent Dependency values from TABLE 1.

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Late Majority?
(Cite I-04 from SECTION A)

[Phase body: named roles, adoption trigger, incumbent erosion, what remains of THE INCUMBENT's
position]

---

## PHASE 6 LAGGARDS — Month 11–12

Which roles adopt last? What finally moves them?

Q-BARRIER: Which Named Inertia ID keeps Laggards last?
(Cite I-05 from SECTION A — this is the only structurally correct answer)

[Phase body: named roles, final adoption conditions, terminal incumbent displacement state]

---

## TABLE 3 — Spread Mechanisms

TABLE 3 header contract: Each row below is prefixed SLOT-KEY: — the row label is a typed
structural slot key naming a specific canonical transition pair. The Spread Mechanism column
must be filled with a named signal, artifact, or social proof event that is specific to
{{topic}} — not "word of mouth," "organic growth," or any other generic mechanism. A
mechanism valid for one SLOT-KEY is not valid for another; they are not interchangeable.
A generic entry violates the slot-type contract declared by this header.

| Transition Pair (SLOT-KEY row) | Spread Mechanism: [named signal or artifact specific to {{topic}} — not generic word-of-mouth] | Month Range |
|---|---|---|
| SLOT-KEY: Innovator → Early Adopter      | | |
| SLOT-KEY: Early Adopter → Early Majority | | |
| SLOT-KEY: Early Majority → Late Majority | | |
| SLOT-KEY: Late Majority → Laggard        | | |

---

## PART 2 — CHASM ANALYSIS (Full Expansion)

PHASE 3 introduced a diagnostic sketch of each chasm element. PART 2 expands each element
to its full specification. Three named structural subsections mirror PHASE 3's CHASM-A/B/C
structure. A missing subsection here is a missing named structural slot — same enforcement
class as a missing CHASM-A/B/C subsection in PHASE 3 itself.

Each expansion subsection re-cites the Named Inertia ID from its PHASE 3 Q-BARRIER answer
as the first structural field. The model cannot complete a CHASM-X EXPANSION subsection
without re-asserting the Named Inertia ID that drives that element.

### CHASM-A EXPANSION — Incumbent Defense (Full Diagnosis)

Expanding CHASM-A from PHASE 3 —
Named Inertia in effect: [re-cite I-0X from Q-BARRIER in PHASE 3 CHASM-A — the Named Inertia
ID identified as the structural driver of the incumbent defense]

[Full diagnosis: the complete mechanism by which THE INCUMBENT defends its position at the
chasm boundary — process dependencies, organizational commitments, role-level switching costs.
Name every TABLE 1 Incumbent Dependency value that is load-bearing here. Identify which
Early Majority roles are most defended and why.]

### CHASM-B EXPANSION — Bridge Condition (Full Specification)

Expanding CHASM-B from PHASE 3 —
Named Inertia in effect: [re-cite I-0X from Q-BARRIER in PHASE 3 CHASM-B — the Named Inertia
ID whose resolution is the bridge condition]

[Full specification: the bridge condition stated as a testable proposition, the precise
observable state that satisfies it, which role or artifact produces that state, and why
that state is sufficient to unlock Early Majority adoption. Cross-reference the Incumbent
Dependency values from TABLE 1 that the bridge condition unblocks.]

### CHASM-C EXPANSION — Crossing Signal (Full Identification)

Expanding CHASM-C from PHASE 3 —
Named Inertia in effect: [re-cite I-0X from Q-BARRIER in PHASE 3 CHASM-C — the Named Inertia
ID whose weakening produces the crossing signal]

[Full identification: the crossing signal named with precision — the specific role, behavioral
event, or artifact emission that proves the chasm has been crossed. Explain why this signal
is distinguishable from Early Adopter behavior, how it connects to the bridge condition from
CHASM-B EXPANSION, and what adoption acceleration it predicts in PHASE 4.]

---

## PART 3 — Churn Risk Register

Every role that adopts carries a reversion risk: the specific condition that would cause
them to return to THE INCUMBENT. List all roles at non-trivial churn risk. Each entry must
name the reversion trigger (not a generic risk category) and a concrete retention action.

| Role | Reversion trigger: [the specific condition that causes this role to revert to THE INCUMBENT] | Retention intervention: [one concrete action that reduces reversion probability — not a surveillance flag] | Inertia ID driving reversion: [Q-TRIGGER: which Named Inertia ID? Cite I-0X from SECTION A] |
|------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
|      |                                                                                              |                                                                                                            |                                                                                              |

---

## PART 4 — Champion Network

Name at least three roles positioned to advocate for {{topic}} adoption and displace THE
INCUMBENT. For each champion, provide two structural anchors:

(a) Archetype-bridge rationale — why this role's archetype position makes it an effective
adoption champion for the next archetype tier.

(b) Q-CHAMPION: Named Inertia ID this champion is positioned to overcome:
(Cite I-0X from SECTION A — the inertia this champion's position directly addresses)

| Champion Role | Archetype | Archetype-bridge rationale | Q-CHAMPION: Named Inertia ID overcome (I-0X) | Why this champion displaces THE INCUMBENT for the target tier |
|---|---|---|---|---|
|   |   |   |   |   |

---

## PART 5 — Intervention Ranking

Rank retention interventions by their impact on adoption velocity (adoption delta: the
percentage-point increase in adoption rate the intervention produces). Each entry must
reference at least one named phase and one named role. The Incumbent Impact column names
what THE INCUMBENT loses when this intervention succeeds — the displacement accounting.

| Rank | Intervention | Adoption delta | Phase(s) affected | Role(s) affected | Incumbent Impact: [what THE INCUMBENT loses when this intervention succeeds] |
|------|--------------|---------------|-------------------|------------------|------------------------------------------------------------------------------|
| 1    |              |               |                   |                  |                                                                              |
| 2    |              |               |                   |                  |                                                                              |
| 3    |              |               |                   |                  |                                                                              |

---

## PART 6 — Sensitivity Analysis

Name two adoption scenarios with distinct outcomes. For each scenario, name at least one
lever — a specific {{topic}} feature, team behavior, or external condition — that shifts
the adoption curve between scenarios.

| Scenario        | Adoption outcome | Named lever | Direction of shift |
|-----------------|-----------------|-------------|-------------------|
| Fast Adoption   |                 |             |                   |
| Slow Adoption   |                 |             |                   |

---

## PART 7 — Signal Readiness Table

Map named signals to adoption thresholds and interpretations. Each row: signal name,
threshold value or condition, interpretation (what it means for adoption timing).

| Signal name | Threshold | Interpretation: what this signal level means for {{topic}} adoption timing |
|-------------|-----------|----------------------------------------------------------------------------|
|             |           |                                                                            |

---

> CORRECTION BLOCK MECHANISM ARMED — no gate failure triggered. If any gate below fails,
> a CORRECTION BLOCK with BEFORE and AFTER fields will be inserted immediately above this
> line before proceeding to SECTION K.

## VERIFICATION MODE

All content generation is complete above this boundary. SECTIONS H, I, J, K are audit
sections only. No content generation occurs below this line.

---

## SECTION H — Gate: C-13 Audit (Named Inertia IDs as Downstream Backbone)

**Criterion C-13:** Named Inertia IDs from SECTION A are cited by ID (I-0X) in at least
four downstream location types: (1) bridge conditions, (2) intervention rationale,
(3) champion rationale, (4) churn register entries.

**Audit:** Scan the document for I-0X citations in each of the four required location types.

- Bridge conditions (CHASM-B, CHASM-B EXPANSION): [PASS/FAIL — cite location and ID found, or name missing location]
- Intervention rationale (PART 5): [PASS/FAIL]
- Champion rationale (PART 4, Q-CHAMPION answers): [PASS/FAIL]
- Churn register (PART 3, Q-TRIGGER answers): [PASS/FAIL]

**Gate H result:** [PASS if all four location types contain at least one I-0X citation | FAIL if any location type lacks a citation]

**Revision obligation:** If Gate H FAILS, produce a CORRECTION BLOCK immediately before the
pre-verification declaration above. The CORRECTION BLOCK must contain a BEFORE field showing
the deficient content and an AFTER field showing the corrected content with I-0X citations
added. Do not proceed to SECTION I until the CORRECTION BLOCK is written.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate H [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION I — Gate: C-14 Audit (Champion Rationale Double-Anchored)

**Criterion C-14:** Each champion entry in PART 4 contains both: (a) archetype-bridge
rationale and (b) a Named Inertia ID cited by Q-CHAMPION answer (I-0X from SECTION A).

**Audit:** For each champion entry in PART 4, verify both anchors are present.

- Champion 1 [name]: archetype-bridge present? [Y/N] | Q-CHAMPION I-0X cited? [Y/N]
- Champion 2 [name]: archetype-bridge present? [Y/N] | Q-CHAMPION I-0X cited? [Y/N]
- Champion 3 [name]: archetype-bridge present? [Y/N] | Q-CHAMPION I-0X cited? [Y/N]

**Gate I result:** [PASS if both anchors present for all champions | FAIL if any champion lacks either anchor]

**Revision obligation:** If Gate I FAILS, produce a CORRECTION BLOCK immediately before the
pre-verification declaration above. Do not proceed to SECTION J until the CORRECTION BLOCK
is written.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate I [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION J — Gate: C-15 Audit (Concrete Retention Actions)

**Criterion C-15:** Every mitigation in PART 3's churn register is a concrete retention
action — something a team does to reduce reversion probability. Surveillance-only entries
("track usage," "monitor engagement") fail this criterion.

**Audit:** For each entry in PART 3, verify the Retention intervention field contains a
concrete action rather than a surveillance flag.

- [List each churn register entry and its classification: concrete action or surveillance flag]

**Gate J result:** [PASS if all entries contain concrete retention actions | FAIL if any entry contains only a surveillance flag]

**Revision obligation:** If Gate J FAILS, produce a CORRECTION BLOCK immediately before the
pre-verification declaration above. Do not proceed to SECTION K until the CORRECTION BLOCK
is written.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate J [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION K — Terminal Audit Record

Per-gate execution stamps are recorded here for all three gates regardless of outcome.
A terminal section recording only failures is incomplete; a passing gate that left no stamp
is unverified audit execution.

**Terminal Invariant:** For every gate with "Revision Performed: Yes" in this section, a
CORRECTION BLOCK with BEFORE and AFTER fields must exist in the document body at the
cited location, above the pre-verification declaration. A "Revision Performed: Yes" entry
whose cited location contains no CORRECTION BLOCK, or a CORRECTION BLOCK without a BEFORE
field, falsifies this invariant.

| Gate | Criterion | Initial result | Revision performed | CORRECTION BLOCK location | Final result |
|------|-----------|---------------|-------------------|--------------------------|-------------|
| H    | C-13      |               | Yes / No          |                          |             |
| I    | C-14      |               | Yes / No          |                          |             |
| J    | C-15      |               | Yes / No          |                          |             |

---

## V-02 — Single Axis: Role Sequence (TABLE 1 SLOT-KEY: Row Prefix)

**Variation axis:** Role sequence — TABLE 1 rows prefixed with `SLOT-KEY: [Role]`, applying
the C-38 enforcement pattern (TABLE 3 row-level contract re-assertion) to TABLE 1. Each row
re-asserts the three-contract typed slot (archetype | incumbent dependency | inertia ID) at
the row label level, independently of the column headers. The header declares the contract;
each SLOT-KEY: row re-encounters that contract at its own generation moment.

**Hypothesis:** C-41 merges three contracts into TABLE 1's column structure — the model
encounters all three contracts once at table entry and holds them across all 16 rows from
memory. The SLOT-KEY: prefix applies the C-38 re-assertion pattern: each row label carries
`SLOT-KEY: [Role] — three contracts: archetype | incumbent dependency | inertia ID`, making
the three-contract requirement continuously present at each row fill step rather than once
at table entry. A model generating row 12 (C-12) encounters the three-contract reminder
from the row label itself, not from the column headers 16 rows above. Same structural
elevation as C-38 applied to C-37/C-41.

---

Simulate the adoption curve for {{topic}} across the 16 stock roles (PM, UX, C-01 through
C-12, Support, SRE). Produce the artifact below in full.

---

## STRUCTURAL CONTRACT

This document encodes two mandatory co-present architectural requirements.

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
MECHANISM STATE blockquote footers inside SECTIONS H, I, J (gate-level) AND pre-verification
declaration before `## VERIFICATION MODE` (boundary-level). Both mandatory.

---

## SECTION A — Named Inertia IDs

| Inertia ID | Archetype      | Named Inertia                      | Structural reason |
|------------|----------------|------------------------------------|-------------------|
| I-01       | Innovator      | [name]                             | [reason]          |
| I-02       | Early Adopter  | [name]                             | [reason]          |
| I-03       | Early Majority | [name]                             | [reason]          |
| I-04       | Late Majority  | [name]                             | [reason]          |
| I-05       | Laggard        | [name]                             | [reason]          |

---

THE INCUMBENT is [name the current workflow or tool being displaced by {{topic}}].

---

## TABLE 1 — Role Archetype Map

TABLE 1 header contract: Each row below is prefixed SLOT-KEY: — the row label is a typed
structural slot key re-asserting the three co-present contracts (archetype assignment,
Incumbent Dependency, Inertia ID citation) at this row's generation moment, independently
of the column headers. A row is complete only when all three contract fields are filled.
SLOT-KEY: [Role] is not a cosmetic prefix; it re-asserts the typed slot contract at the
point of generation for that specific role.

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
(Cite I-01 from SECTION A)

[Phase body]

---

## PHASE 2 EARLY ADOPTERS — Month 2–3

Q-BARRIER: Which Named Inertia ID is the primary barrier for Early Adopters?
(Cite I-02 from SECTION A)

[Phase body]

---

## PHASE 3 CHASM — Month 4 (Non-Adoption Crossing Event)

Q-BARRIER: Which Named Inertia ID is driving the chasm?
(Cite I-03 from SECTION A)

### CHASM-A — Incumbent Defense

[What defends THE INCUMBENT's position among the Early and Late Majority?]

### CHASM-B — Bridge Condition

[What single testable condition must hold for the Early Majority to cross?]

### CHASM-C — Early Crossing Signal

[What is the first observable signal that the chasm has been crossed?]

---

## PHASE 4 EARLY MAJORITY — Month 5–7

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Early Majority?
(Cite I-03 from SECTION A)

[Phase body]

---

## PHASE 5 LATE MAJORITY — Month 8–10

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Late Majority?
(Cite I-04 from SECTION A)

[Phase body]

---

## PHASE 6 LAGGARDS — Month 11–12

Q-BARRIER: Which Named Inertia ID keeps Laggards last?
(Cite I-05 from SECTION A)

[Phase body]

---

## TABLE 3 — Spread Mechanisms

TABLE 3 header contract: Each row below is prefixed SLOT-KEY: — typed structural slot key
for its canonical transition pair. Spread Mechanism column: [named signal or artifact
specific to {{topic}} — not generic word-of-mouth]. A generic entry violates the slot-type
contract.

| Transition Pair (SLOT-KEY row) | Spread Mechanism: [named signal or artifact — not generic word-of-mouth] | Month Range |
|---|---|---|
| SLOT-KEY: Innovator → Early Adopter      | | |
| SLOT-KEY: Early Adopter → Early Majority | | |
| SLOT-KEY: Early Majority → Late Majority | | |
| SLOT-KEY: Late Majority → Laggard        | | |

---

## PART 2 — CHASM ANALYSIS (Full Expansion)

Three named structural subsections expand PHASE 3's CHASM-A/B/C diagnostic sketches.

### CHASM-A EXPANSION — Incumbent Defense (Full Diagnosis)

Expanding CHASM-A from PHASE 3 —
[Full diagnosis: named incumbent defense mechanism, TABLE 1 Incumbent Dependency values
load-bearing here, why Early Majority crossing requires more than Early Adopter endorsement]

### CHASM-B EXPANSION — Bridge Condition (Full Specification)

Expanding CHASM-B from PHASE 3 —
[Full specification: bridge condition as testable proposition, role or artifact that satisfies
it, connection to TABLE 1 Incumbent Dependency values now unblocked]

### CHASM-C EXPANSION — Crossing Signal (Full Identification)

Expanding CHASM-C from PHASE 3 —
[Full identification: named crossing signal, distinguishing it from Early Adopter behavior,
predicted adoption acceleration in PHASE 4]

---

## PART 3 — Churn Risk Register

| Role | Reversion trigger: [specific condition causing reversion to THE INCUMBENT] | Retention intervention: [one concrete action — not a surveillance flag] | Inertia ID driving reversion: [Q-TRIGGER: cite I-0X from SECTION A] |
|------|----------------------------------------------------------------------------|-------------------------------------------------------------------------|----------------------------------------------------------------------|
|      |                                                                            |                                                                         |                                                                      |

---

## PART 4 — Champion Network

| Champion Role | Archetype | Archetype-bridge rationale | Q-CHAMPION: Named Inertia ID overcome (I-0X) | Displacement rationale |
|---|---|---|---|---|
|   |   |   |   |   |

---

## PART 5 — Intervention Ranking

| Rank | Intervention | Adoption delta | Phase(s) | Role(s) | Incumbent Impact: [what THE INCUMBENT loses when this succeeds] |
|------|--------------|---------------|----------|---------|----------------------------------------------------------------|
| 1    |              |               |          |         |                                                                |
| 2    |              |               |          |         |                                                                |
| 3    |              |               |          |         |                                                                |

---

## PART 6 — Sensitivity Analysis

| Scenario      | Adoption outcome | Named lever | Direction |
|---------------|-----------------|-------------|-----------|
| Fast Adoption |                 |             |           |
| Slow Adoption |                 |             |           |

---

## PART 7 — Signal Readiness Table

| Signal name | Threshold | Interpretation |
|-------------|-----------|----------------|
|             |           |                |

---

> CORRECTION BLOCK MECHANISM ARMED — no gate failure triggered. If any gate fails,
> CORRECTION BLOCK with BEFORE and AFTER fields inserted immediately above this line.

## VERIFICATION MODE

---

## SECTION H — Gate: C-13 Audit (Named Inertia IDs as Downstream Backbone)

Verify I-0X citations in: (1) bridge conditions, (2) intervention rationale, (3) champion
rationale, (4) churn register entries. All four location types required.

[Audit per location type]

**Gate H result:** [PASS / FAIL]

**Revision obligation:** Gate H FAIL → CORRECTION BLOCK before pre-verification declaration.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate H [PASS: no correction triggered | FAIL: CORRECTION BLOCK written]

---

## SECTION I — Gate: C-14 Audit (Champion Rationale Double-Anchored)

Verify each PART 4 champion has both: archetype-bridge rationale AND Q-CHAMPION I-0X citation.

[Audit per champion]

**Gate I result:** [PASS / FAIL]

**Revision obligation:** Gate I FAIL → CORRECTION BLOCK before pre-verification declaration.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate I [PASS: no correction triggered | FAIL: CORRECTION BLOCK written]

---

## SECTION J — Gate: C-15 Audit (Concrete Retention Actions)

Verify each PART 3 entry's Retention intervention is a concrete action, not a surveillance
flag.

[Audit per entry]

**Gate J result:** [PASS / FAIL]

**Revision obligation:** Gate J FAIL → CORRECTION BLOCK before pre-verification declaration.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate J [PASS: no correction triggered | FAIL: CORRECTION BLOCK written]

---

## SECTION K — Terminal Audit Record

**Terminal Invariant:** For every "Revision Performed: Yes" row, a CORRECTION BLOCK with
BEFORE and AFTER fields must exist above the pre-verification declaration at the cited
location. A Yes row whose cited location contains no CORRECTION BLOCK, or a CORRECTION
BLOCK without a BEFORE field, falsifies this invariant.

| Gate | Criterion | Initial result | Revision performed | CORRECTION BLOCK location | Final result |
|------|-----------|---------------|-------------------|--------------------------|-------------|
| H    | C-13      |               | Yes / No          |                          |             |
| I    | C-14      |               | Yes / No          |                          |             |
| J    | C-15      |               | Yes / No          |                          |             |

---

## V-03 — Single Axis: Inertia Framing (PART 5 Inertia Targeting Column)

**Variation axis:** Inertia framing — PART 5 intervention ranking adds a `Targets inertia:
[I-0X — Named Inertia ID this intervention directly addresses]` column per ranked entry.
Each intervention is now typed as an inertia-addressing action: the model must name which
specific structural resistance the intervention breaks down, not just which phase or role
it affects. This creates a new downstream backbone citation location for Named Inertia IDs
(C-13) and transforms PART 5 from a phase/role cross-reference table into a typed
inertia-targeting structure.

**Hypothesis:** C-13 requires I-0X citations in four location types: bridge conditions,
intervention rationale, champion rationale, churn register. "Intervention rationale" is
currently satisfied when any intervention entry contains an I-0X citation somewhere in its
text body. Adding `Targets inertia: I-0X` as a typed column slot makes the citation a
per-entry structural fill contract rather than a compliance check against text content —
the model must identify which Named Inertia the intervention targets at generation time,
not reference it incidentally in a prose description. Same elevation class as Q-TRIGGER in
the churn register: the column label encodes the citation requirement at the slot level.

---

Simulate the adoption curve for {{topic}} across the 16 stock roles. Produce the artifact below.

---

## STRUCTURAL CONTRACT

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
MECHANISM STATE blockquote footers in SECTIONS H, I, J (gate-level) AND pre-verification
declaration before `## VERIFICATION MODE` (boundary-level). Both mandatory.

---

## SECTION A — Named Inertia IDs

| Inertia ID | Archetype      | Named Inertia | Structural reason |
|------------|----------------|---------------|-------------------|
| I-01       | Innovator      |               |                   |
| I-02       | Early Adopter  |               |                   |
| I-03       | Early Majority |               |                   |
| I-04       | Late Majority  |               |                   |
| I-05       | Laggard        |               |                   |

---

THE INCUMBENT is [name the workflow or tool being displaced].

---

## TABLE 1 — Role Archetype Map

Three contracts co-present per row: archetype assignment (C-01), Incumbent Dependency (C-37),
Inertia ID citation (C-41).

| Role    | Rogers Archetype | Incumbent Dependency: [step this role relies on THE INCUMBENT] | Inertia ID: [cite I-0X from SECTION A] |
|---------|-----------------|----------------------------------------------------------------|----------------------------------------|
| PM      | | | |
| UX      | | | |
| C-01    | | | |
| C-02    | | | |
| C-03    | | | |
| C-04    | | | |
| C-05    | | | |
| C-06    | | | |
| C-07    | | | |
| C-08    | | | |
| C-09    | | | |
| C-10    | | | |
| C-11    | | | |
| C-12    | | | |
| Support | | | |
| SRE     | | | |

---

## PHASE 1 INNOVATORS — Month 1

Q-BARRIER: Which Named Inertia ID is the primary barrier even for Innovators?
(Cite I-01 from SECTION A)

[Phase body]

---

## PHASE 2 EARLY ADOPTERS — Month 2–3

Q-BARRIER: Which Named Inertia ID is the primary barrier for Early Adopters?
(Cite I-02 from SECTION A)

[Phase body]

---

## PHASE 3 CHASM — Month 4 (Non-Adoption Crossing Event)

Q-BARRIER: Which Named Inertia ID is driving the chasm?
(Cite I-03 from SECTION A)

### CHASM-A — Incumbent Defense

[Incumbent defense mechanism]

### CHASM-B — Bridge Condition

[Bridge condition as testable proposition]

### CHASM-C — Early Crossing Signal

[First observable crossing signal]

---

## PHASE 4 EARLY MAJORITY — Month 5–7

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Early Majority?
(Cite I-03 from SECTION A)

[Phase body]

---

## PHASE 5 LATE MAJORITY — Month 8–10

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Late Majority?
(Cite I-04 from SECTION A)

[Phase body]

---

## PHASE 6 LAGGARDS — Month 11–12

Q-BARRIER: Which Named Inertia ID keeps Laggards last?
(Cite I-05 from SECTION A)

[Phase body]

---

## TABLE 3 — Spread Mechanisms

| Transition Pair (SLOT-KEY row) | Spread Mechanism: [named signal or artifact — not generic word-of-mouth] | Month Range |
|---|---|---|
| SLOT-KEY: Innovator → Early Adopter      | | |
| SLOT-KEY: Early Adopter → Early Majority | | |
| SLOT-KEY: Early Majority → Late Majority | | |
| SLOT-KEY: Late Majority → Laggard        | | |

---

## PART 2 — CHASM ANALYSIS (Full Expansion)

### CHASM-A EXPANSION — Incumbent Defense (Full Diagnosis)

Expanding CHASM-A from PHASE 3 —
[Full diagnosis]

### CHASM-B EXPANSION — Bridge Condition (Full Specification)

Expanding CHASM-B from PHASE 3 —
[Full specification]

### CHASM-C EXPANSION — Crossing Signal (Full Identification)

Expanding CHASM-C from PHASE 3 —
[Full identification]

---

## PART 3 — Churn Risk Register

| Role | Reversion trigger: [specific condition] | Retention intervention: [concrete action — not surveillance] | Inertia ID driving reversion: [Q-TRIGGER: I-0X] |
|------|----------------------------------------|-------------------------------------------------------------|--------------------------------------------------|
|      |                                        |                                                             |                                                  |

---

## PART 4 — Champion Network

| Champion Role | Archetype | Archetype-bridge rationale | Q-CHAMPION: Named Inertia ID overcome (I-0X) | Displacement rationale |
|---|---|---|---|---|
|   |   |   |   |   |

---

## PART 5 — Intervention Ranking

Each intervention must identify the Named Inertia ID it directly targets. The `Targets
inertia:` column encodes Q-INTERVENTION as a per-row structural fill contract, not a
text-body citation. A row without a Named Inertia ID in the Targets inertia column violates
the slot-type contract of this table.

| Rank | Intervention | Adoption delta | Phase(s) | Role(s) | Incumbent Impact: [what THE INCUMBENT loses] | Targets inertia: [I-0X — Q-INTERVENTION: which Named Inertia ID does this intervention directly address?] |
|------|--------------|---------------|----------|---------|----------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| 1    |              |               |          |         |                                              |                                                                                                           |
| 2    |              |               |          |         |                                              |                                                                                                           |
| 3    |              |               |          |         |                                              |                                                                                                           |

---

## PART 6 — Sensitivity Analysis

| Scenario      | Adoption outcome | Named lever | Direction |
|---------------|-----------------|-------------|-----------|
| Fast Adoption |                 |             |           |
| Slow Adoption |                 |             |           |

---

## PART 7 — Signal Readiness Table

| Signal name | Threshold | Interpretation |
|-------------|-----------|----------------|
|             |           |                |

---

> CORRECTION BLOCK MECHANISM ARMED — no gate failure triggered.

## VERIFICATION MODE

---

## SECTION H — Gate: C-13 Audit

I-0X citations in: (1) bridge conditions, (2) intervention rationale — note: `Targets
inertia:` column satisfies this location type structurally when filled, (3) champion
rationale, (4) churn register entries.

[Audit]

**Gate H result:** [PASS / FAIL]

**Revision obligation:** Gate H FAIL → CORRECTION BLOCK before pre-verification declaration.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate H [PASS: no correction triggered | FAIL: CORRECTION BLOCK written]

---

## SECTION I — Gate: C-14 Audit

[Audit per champion: archetype-bridge + Q-CHAMPION]

**Gate I result:** [PASS / FAIL]

**Revision obligation:** Gate I FAIL → CORRECTION BLOCK before pre-verification declaration.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate I [PASS: no correction triggered | FAIL: CORRECTION BLOCK written]

---

## SECTION J — Gate: C-15 Audit

[Audit per churn entry: concrete action vs. surveillance flag]

**Gate J result:** [PASS / FAIL]

**Revision obligation:** Gate J FAIL → CORRECTION BLOCK before pre-verification declaration.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate J [PASS: no correction triggered | FAIL: CORRECTION BLOCK written]

---

## SECTION K — Terminal Audit Record

**Terminal Invariant:** For every "Revision Performed: Yes" row, a CORRECTION BLOCK with
BEFORE and AFTER fields must exist at the cited location above the pre-verification
declaration. A Yes row with no CORRECTION BLOCK at the cited location, or a CORRECTION
BLOCK without a BEFORE field, falsifies this invariant.

| Gate | Criterion | Initial result | Revision performed | CORRECTION BLOCK location | Final result |
|------|-----------|---------------|-------------------|--------------------------|-------------|
| H    | C-13      |               | Yes / No          |                          |             |
| I    | C-14      |               | Yes / No          |                          |             |
| J    | C-15      |               | Yes / No          |                          |             |

---

## V-04 — Combined: Role Sequence + Inertia Framing (TABLE 1 SLOT-KEY + PART 5 Inertia Targeting)

**Variation axes:** V-02 (TABLE 1 SLOT-KEY: row prefix) + V-03 (PART 5 Targets inertia column)

**Hypothesis:** V-02's SLOT-KEY: row prefix and V-03's Targets inertia column operate at
different structural levels and do not interfere. V-02 enforces the three-contract re-assertion
at TABLE 1 row generation time; V-03 enforces Named Inertia citation at PART 5 intervention
generation time. Together they add two new Named Inertia re-assertion points: one at role
assignment (TABLE 1, 16 rows), one at intervention ranking (PART 5, per ranked entry). The
downstream backbone (C-13) gains a structurally encoded citation location in PART 5 via the
Targets inertia column, and TABLE 1 rows gain the C-38 re-assertion pattern for their
three-contract slots. No baseline element is modified; both axes are purely additive.

---

Simulate the adoption curve for {{topic}} across the 16 stock roles. Produce the artifact below.

---

## STRUCTURAL CONTRACT

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
MECHANISM STATE blockquote footers in SECTIONS H, I, J (gate-level) AND pre-verification
declaration before `## VERIFICATION MODE` (boundary-level). Both mandatory.

---

## SECTION A — Named Inertia IDs

| Inertia ID | Archetype      | Named Inertia | Structural reason |
|------------|----------------|---------------|-------------------|
| I-01       | Innovator      |               |                   |
| I-02       | Early Adopter  |               |                   |
| I-03       | Early Majority |               |                   |
| I-04       | Late Majority  |               |                   |
| I-05       | Laggard        |               |                   |

---

THE INCUMBENT is [name].

---

## TABLE 1 — Role Archetype Map

TABLE 1 header contract: Each row is prefixed SLOT-KEY: re-asserting three co-present
contracts at this row's generation moment: (1) archetype assignment, (2) Incumbent
Dependency, (3) Inertia ID citation. The SLOT-KEY: prefix is not cosmetic — it re-asserts
the typed-slot contract independently at each row fill step.

| Role (SLOT-KEY typed slot) | Rogers Archetype | Incumbent Dependency: [step this role relies on THE INCUMBENT] | Inertia ID: [cite I-0X from SECTION A] |
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
(Cite I-01 from SECTION A)

[Phase body]

---

## PHASE 2 EARLY ADOPTERS — Month 2–3

Q-BARRIER: Which Named Inertia ID is the primary barrier for Early Adopters?
(Cite I-02 from SECTION A)

[Phase body]

---

## PHASE 3 CHASM — Month 4 (Non-Adoption Crossing Event)

Q-BARRIER: Which Named Inertia ID is driving the chasm?
(Cite I-03 from SECTION A)

### CHASM-A — Incumbent Defense

[Incumbent defense mechanism]

### CHASM-B — Bridge Condition

[Bridge condition]

### CHASM-C — Early Crossing Signal

[Crossing signal]

---

## PHASE 4 EARLY MAJORITY — Month 5–7

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Early Majority?
(Cite I-03 from SECTION A)

[Phase body]

---

## PHASE 5 LATE MAJORITY — Month 8–10

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Late Majority?
(Cite I-04 from SECTION A)

[Phase body]

---

## PHASE 6 LAGGARDS — Month 11–12

Q-BARRIER: Which Named Inertia ID keeps Laggards last?
(Cite I-05 from SECTION A)

[Phase body]

---

## TABLE 3 — Spread Mechanisms

| Transition Pair (SLOT-KEY row) | Spread Mechanism: [named signal or artifact — not generic word-of-mouth] | Month Range |
|---|---|---|
| SLOT-KEY: Innovator → Early Adopter      | | |
| SLOT-KEY: Early Adopter → Early Majority | | |
| SLOT-KEY: Early Majority → Late Majority | | |
| SLOT-KEY: Late Majority → Laggard        | | |

---

## PART 2 — CHASM ANALYSIS (Full Expansion)

### CHASM-A EXPANSION — Incumbent Defense (Full Diagnosis)

Expanding CHASM-A from PHASE 3 —
[Full diagnosis]

### CHASM-B EXPANSION — Bridge Condition (Full Specification)

Expanding CHASM-B from PHASE 3 —
[Full specification]

### CHASM-C EXPANSION — Crossing Signal (Full Identification)

Expanding CHASM-C from PHASE 3 —
[Full identification]

---

## PART 3 — Churn Risk Register

| Role | Reversion trigger: [specific condition] | Retention intervention: [concrete action] | Inertia ID driving reversion: [Q-TRIGGER: I-0X] |
|------|----------------------------------------|------------------------------------------|--------------------------------------------------|
|      |                                        |                                          |                                                  |

---

## PART 4 — Champion Network

| Champion Role | Archetype | Archetype-bridge rationale | Q-CHAMPION: Named Inertia ID overcome (I-0X) | Displacement rationale |
|---|---|---|---|---|
|   |   |   |   |   |

---

## PART 5 — Intervention Ranking

`Targets inertia:` column encodes Q-INTERVENTION as a per-row structural fill contract.
A row without a Named Inertia ID in this column violates the slot-type contract.

| Rank | Intervention | Adoption delta | Phase(s) | Role(s) | Incumbent Impact: [what THE INCUMBENT loses] | Targets inertia: [I-0X — which Named Inertia does this intervention address?] |
|------|--------------|---------------|----------|---------|----------------------------------------------|--------------------------------------------------------------------------------|
| 1    |              |               |          |         |                                              |                                                                                |
| 2    |              |               |          |         |                                              |                                                                                |
| 3    |              |               |          |         |                                              |                                                                                |

---

## PART 6 — Sensitivity Analysis

| Scenario      | Adoption outcome | Named lever | Direction |
|---------------|-----------------|-------------|-----------|
| Fast Adoption |                 |             |           |
| Slow Adoption |                 |             |           |

---

## PART 7 — Signal Readiness Table

| Signal name | Threshold | Interpretation |
|-------------|-----------|----------------|
|             |           |                |

---

> CORRECTION BLOCK MECHANISM ARMED — no gate failure triggered.

## VERIFICATION MODE

---

## SECTION H — Gate: C-13 Audit

[Audit: I-0X in (1) bridge conditions, (2) PART 5 Targets inertia column, (3) champion,
(4) churn register]

**Gate H result:** [PASS / FAIL]

**Revision obligation:** Gate H FAIL → CORRECTION BLOCK before pre-verification declaration.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate H [PASS: no correction triggered | FAIL: CORRECTION BLOCK written]

---

## SECTION I — Gate: C-14 Audit

[Audit per champion]

**Gate I result:** [PASS / FAIL]

**Revision obligation:** Gate I FAIL → CORRECTION BLOCK before pre-verification declaration.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate I [PASS: no correction triggered | FAIL: CORRECTION BLOCK written]

---

## SECTION J — Gate: C-15 Audit

[Audit per churn entry]

**Gate J result:** [PASS / FAIL]

**Revision obligation:** Gate J FAIL → CORRECTION BLOCK before pre-verification declaration.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate J [PASS: no correction triggered | FAIL: CORRECTION BLOCK written]

---

## SECTION K — Terminal Audit Record

**Terminal Invariant:** For every "Revision Performed: Yes" row, a CORRECTION BLOCK with
BEFORE and AFTER fields must exist at the cited location above the pre-verification
declaration. A Yes row with no CORRECTION BLOCK at the cited location falsifies this invariant.

| Gate | Criterion | Initial result | Revision performed | CORRECTION BLOCK location | Final result |
|------|-----------|---------------|-------------------|--------------------------|-------------|
| H    | C-13      |               | Yes / No          |                          |             |
| I    | C-14      |               | Yes / No          |                          |             |
| J    | C-15      |               | Yes / No          |                          |             |

---

## V-05 — Full: Lifecycle Emphasis + Role Sequence + Inertia Framing

**Variation axes:** V-01 (PART 2 inertia propagation) + V-02 (TABLE 1 SLOT-KEY: rows) +
V-03 (PART 5 Targets inertia column)

**Hypothesis:** The three R14 axes target three different structural levels of the Named
Inertia ID citation chain: TABLE 1 row generation (V-02, 16 rows), PART 2 expansion slot
generation (V-01, 3 subsections), and PART 5 intervention ranking generation (V-03, per
entry). Together they make Named Inertia ID citation a structural requirement at every
major content-generation site in the document — not just at Q-BARRIER answer positions in
phase bodies. The citation chain becomes: SECTION A (definition) → TABLE 1 per-row
(SLOT-KEY re-assertion at archetype assignment) → PHASE 3 Q-BARRIER (chasm driver) →
PART 2 per-subsection (Named Inertia in effect carry-forward) → PART 4 Q-CHAMPION →
PART 3 Q-TRIGGER → PART 5 Targets inertia (intervention anchoring). No generation site
that processes Named Inertia content can complete its structural slots without a citation.
Projected score: ~250/255 (C-19 paradox persists for answer-form-strong variations).

---

Simulate the adoption curve for {{topic}} across the 16 stock roles (PM, UX, C-01 through
C-12, Support, SRE). Produce the artifact below in full. Every bracketed instruction is a
fill contract.

---

## STRUCTURAL CONTRACT

This document encodes two mandatory co-present architectural requirements. No variation or
omission is permitted.

**REQUIREMENT 1 — ANSWER-FORM CITATION ENFORCEMENT (C-29):**
Named Inertia ID citations throughout this document are answers to explicit mandatory
answer-form questions. The following questions require a Named Inertia ID (I-0X) as the
coherent answer:

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

Additionally, `Named Inertia in effect:` fields in PART 2 CHASM-X EXPANSION subsections
and `Targets inertia:` column in PART 5 are structural fill contracts requiring I-0X
citations at generation time for those sections. Both are mandatory.

**REQUIREMENT 2 — CORRECTION BLOCK MECHANISM STATE (C-32, C-34):**
A MECHANISM STATE line appears as a blockquote footer inside each of SECTIONS H, I, J
(gate-level anchor) AND as a pre-verification declaration immediately before
`## VERIFICATION MODE` (boundary-level anchor). Both anchors are mandatory.

Both requirements are mandatory co-present structural features. A document satisfying
only one fails C-33 and C-35.

---

## SECTION A — Named Inertia IDs

| Inertia ID | Archetype      | Named Inertia                      | Structural reason |
|------------|----------------|------------------------------------|-------------------|
| I-01       | Innovator      | [name the inertia for Innovators]  | [structural reason] |
| I-02       | Early Adopter  | [name the inertia for EA]          | [structural reason] |
| I-03       | Early Majority | [name the inertia for EM]          | [structural reason] |
| I-04       | Late Majority  | [name the inertia for LM]          | [structural reason] |
| I-05       | Laggard        | [name the inertia for Laggards]    | [structural reason] |

---

THE INCUMBENT is [name the current workflow or tool being displaced by {{topic}}]. Every
phase body, expansion subsection, champion entry, churn trigger, and intervention runs
through the displacement lens.

---

## TABLE 1 — Role Archetype Map

TABLE 1 header contract: Each row below is prefixed SLOT-KEY: — a typed structural slot key
re-asserting three co-present contracts at this row's generation moment, independently of
the column headers: (1) archetype assignment, (2) Incumbent Dependency, (3) Inertia ID
citation. The SLOT-KEY: prefix is not cosmetic — it makes the three-contract typed-slot
requirement continuously present at each row fill step. A row is not complete until all
three fill contracts are satisfied.

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

Which roles adopt in Month 1? What does THE INCUMBENT lose?

Q-BARRIER: Which Named Inertia ID is the primary barrier even for Innovators?
(Cite I-01 from SECTION A — this question's structurally correct answer is I-01.
A different answer requires explicit justification.)

[Phase body: named roles, signals produced, displacement impact on THE INCUMBENT's position]

---

## PHASE 2 EARLY ADOPTERS — Month 2–3

Q-BARRIER: Which Named Inertia ID is the primary barrier for Early Adopters?
(Cite I-02 from SECTION A)

[Phase body: named roles, what PHASE 1 evidence persuades them, spread mechanism, incumbent
displacement progress]

---

## PHASE 3 CHASM — Month 4 (Non-Adoption Crossing Event)

PHASE 3 is not an adoption phase. No new archetype adopts in Month 4.

Q-BARRIER: Which Named Inertia ID is driving the chasm?
(Cite I-03 from SECTION A — the Early Majority archetype inertia is the structural driver.)

### CHASM-A — Incumbent Defense

What defends THE INCUMBENT's position among the Early and Late Majority?

[CHASM-A body: named incumbent defense, TABLE 1 Incumbent Dependency values load-bearing
here, why Early Adopter endorsement is insufficient]

### CHASM-B — Bridge Condition

What single testable condition must hold for the Early Majority to cross?

[CHASM-B body: condition as testable proposition, role or artifact that satisfies it,
connection to TABLE 1 Incumbent Dependency values now unblocked]

### CHASM-C — Early Crossing Signal

What is the first observable signal that the chasm has been crossed?

[CHASM-C body: named role or behavioral event, why it is distinguishable from Early Adopter
behavior, connection to bridge condition]

---

## PHASE 4 EARLY MAJORITY — Month 5–7

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Early Majority?
(Cite I-03 from SECTION A)

[Phase body: named roles, bridge proof from CHASM-B, TABLE 1 Incumbent Dependency values
now unblocked, adoption acceleration]

---

## PHASE 5 LATE MAJORITY — Month 8–10

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Late Majority?
(Cite I-04 from SECTION A)

[Phase body: named roles, social proof trigger, TABLE 1 high-dependency roles, incumbent
erosion]

---

## PHASE 6 LAGGARDS — Month 11–12

Q-BARRIER: Which Named Inertia ID keeps Laggards last?
(Cite I-05 from SECTION A — only structurally correct answer)

[Phase body: named roles, final adoption conditions, terminal displacement state]

---

## TABLE 3 — Spread Mechanisms

TABLE 3 header contract: Each row below is prefixed SLOT-KEY: — typed structural slot key
for its canonical transition pair. Spread Mechanism column: [named signal or artifact
specific to {{topic}} — not generic word-of-mouth]. A generic entry violates the slot-type
contract declared by this header and the SLOT-KEY: row label.

| Transition Pair (SLOT-KEY row) | Spread Mechanism: [named signal or artifact specific to {{topic}} — not generic word-of-mouth] | Month Range |
|---|---|---|
| SLOT-KEY: Innovator → Early Adopter      | | |
| SLOT-KEY: Early Adopter → Early Majority | | |
| SLOT-KEY: Early Majority → Late Majority | | |
| SLOT-KEY: Late Majority → Laggard        | | |

---

## PART 2 — CHASM ANALYSIS (Full Expansion)

PHASE 3 introduced a diagnostic sketch of each chasm element. PART 2 expands each element
to full specification. Three named structural subsections mirror PHASE 3's CHASM-A/B/C. A
missing subsection here is a missing named structural slot.

Each expansion subsection re-cites the Named Inertia ID from its PHASE 3 Q-BARRIER answer
as a `Named Inertia in effect:` field — the first structural fill contract of the subsection.
This carry-forward is mandatory: completing a CHASM-X EXPANSION without re-asserting the
Named Inertia ID leaves an empty structural field.

### CHASM-A EXPANSION — Incumbent Defense (Full Diagnosis)

Expanding CHASM-A from PHASE 3 —
Named Inertia in effect: [re-cite I-0X from Q-BARRIER in PHASE 3 CHASM-A — the Named
Inertia ID identified as the structural driver of the incumbent defense]

[Full diagnosis: complete mechanism of incumbent defense at the chasm boundary — process
dependencies, organizational commitments, role-level switching costs. Name every TABLE 1
Incumbent Dependency value load-bearing here. Identify which Early Majority roles are most
defended and why. Reference the bridge condition that would overcome this defense.]

### CHASM-B EXPANSION — Bridge Condition (Full Specification)

Expanding CHASM-B from PHASE 3 —
Named Inertia in effect: [re-cite I-0X from Q-BARRIER in PHASE 3 CHASM-B — the Named
Inertia ID whose resolution is the bridge condition itself]

[Full specification: bridge condition as a precise testable proposition, the observable
state that satisfies it, which role or artifact produces that state, why it is sufficient
to unlock Early Majority adoption. Cross-reference TABLE 1 Incumbent Dependency values
that the bridge condition unblocks.]

### CHASM-C EXPANSION — Crossing Signal (Full Identification)

Expanding CHASM-C from PHASE 3 —
Named Inertia in effect: [re-cite I-0X from Q-BARRIER in PHASE 3 CHASM-C — the Named
Inertia ID whose weakening produces the crossing signal]

[Full identification: crossing signal with precision — named role, behavioral event, or
artifact emission that proves the chasm has been crossed. Why this signal is distinguishable
from Early Adopter behavior. Connection to bridge condition from CHASM-B EXPANSION. What
adoption acceleration it predicts in PHASE 4.]

---

## PART 3 — Churn Risk Register

| Role | Reversion trigger: [specific condition causing reversion to THE INCUMBENT] | Retention intervention: [one concrete action — not a surveillance flag] | Inertia ID driving reversion: [Q-TRIGGER: which I-0X?] |
|------|----------------------------------------------------------------------------|-------------------------------------------------------------------------|--------------------------------------------------------|
|      |                                                                            |                                                                         |                                                        |

---

## PART 4 — Champion Network

Name at least three roles. Two structural anchors per entry:
(a) Archetype-bridge rationale
(b) Q-CHAMPION: Named Inertia ID this champion is positioned to overcome (I-0X from SECTION A)

| Champion Role | Archetype | Archetype-bridge rationale | Q-CHAMPION: Named Inertia ID overcome (I-0X) | Why this champion displaces THE INCUMBENT for the target tier |
|---|---|---|---|---|
|   |   |   |   |   |

---

## PART 5 — Intervention Ranking

Two structural fill contracts per entry: (1) Incumbent Impact column, (2) Targets inertia
column encoding Q-INTERVENTION as a per-row fill contract. A row without a Named Inertia
ID in the Targets inertia column violates the slot-type contract of this table.

| Rank | Intervention | Adoption delta | Phase(s) | Role(s) | Incumbent Impact: [what THE INCUMBENT loses when this succeeds] | Targets inertia: [I-0X — Q-INTERVENTION: which Named Inertia ID does this directly address?] |
|------|--------------|---------------|----------|---------|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| 1    |              |               |          |         |                                                                |                                                                                               |
| 2    |              |               |          |         |                                                                |                                                                                               |
| 3    |              |               |          |         |                                                                |                                                                                               |

---

## PART 6 — Sensitivity Analysis

| Scenario      | Adoption outcome | Named lever | Direction of shift |
|---------------|-----------------|-------------|--------------------|
| Fast Adoption |                 |             |                    |
| Slow Adoption |                 |             |                    |

---

## PART 7 — Signal Readiness Table

| Signal name | Threshold | Interpretation: what this level means for {{topic}} adoption timing |
|-------------|-----------|---------------------------------------------------------------------|
|             |           |                                                                     |

---

> CORRECTION BLOCK MECHANISM ARMED — no gate failure triggered. If any gate below fails,
> a CORRECTION BLOCK with BEFORE and AFTER fields will be inserted immediately above this
> line before proceeding to SECTION K.

## VERIFICATION MODE

All content generation is complete above this boundary. SECTIONS H, I, J, K are audit
sections only.

---

## SECTION H — Gate: C-13 Audit (Named Inertia IDs as Downstream Backbone)

**Criterion C-13:** Named Inertia IDs cited by ID in all four downstream location types:
(1) bridge conditions (CHASM-B, CHASM-B EXPANSION), (2) intervention rationale (PART 5
Targets inertia column), (3) champion rationale (PART 4 Q-CHAMPION), (4) churn register
(PART 3 Q-TRIGGER). Note: PART 5 Targets inertia column satisfies location type (2)
structurally when filled.

**Audit:**
- Bridge conditions: [PASS/FAIL — cite location and I-0X found, or name missing location]
- Intervention rationale (Targets inertia column): [PASS/FAIL]
- Champion rationale (Q-CHAMPION answers): [PASS/FAIL]
- Churn register (Q-TRIGGER answers): [PASS/FAIL]

**Gate H result:** [PASS / FAIL]

**Revision obligation:** Gate H FAIL → CORRECTION BLOCK immediately before the
pre-verification declaration above. Do not proceed to SECTION I until CORRECTION BLOCK
is written.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate H [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION I — Gate: C-14 Audit (Champion Rationale Double-Anchored)

**Criterion C-14:** Each PART 4 champion entry has both: (a) archetype-bridge rationale
and (b) Q-CHAMPION I-0X citation.

**Audit:**
- Champion 1 [name]: archetype-bridge [Y/N] | Q-CHAMPION I-0X [Y/N]
- Champion 2 [name]: archetype-bridge [Y/N] | Q-CHAMPION I-0X [Y/N]
- Champion 3 [name]: archetype-bridge [Y/N] | Q-CHAMPION I-0X [Y/N]

**Gate I result:** [PASS / FAIL]

**Revision obligation:** Gate I FAIL → CORRECTION BLOCK before pre-verification declaration.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate I [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION J — Gate: C-15 Audit (Concrete Retention Actions)

**Criterion C-15:** Every PART 3 Retention intervention is a concrete action, not a
surveillance flag.

**Audit:**
- [List each entry: role | classification: concrete action or surveillance flag]

**Gate J result:** [PASS / FAIL]

**Revision obligation:** Gate J FAIL → CORRECTION BLOCK before pre-verification declaration.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED — Gate J [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION K — Terminal Audit Record

**Terminal Invariant:** For every "Revision Performed: Yes" row, a CORRECTION BLOCK with
BEFORE and AFTER fields must exist in the document body at the cited location, above the
pre-verification declaration. A "Revision Performed: Yes" entry whose cited location
contains no CORRECTION BLOCK, or a CORRECTION BLOCK without a BEFORE field, falsifies
this invariant.

**Falsification condition:** If any row records "Revision Performed: Yes" and the cited
CORRECTION BLOCK location contains no CORRECTION BLOCK element, or the CORRECTION BLOCK
at that location has no BEFORE field, this terminal section is internally inconsistent.

| Gate | Criterion | Initial result | Revision performed | CORRECTION BLOCK location | Final result |
|------|-----------|---------------|-------------------|--------------------------|-------------|
| H    | C-13      |               | Yes / No          |                          |             |
| I    | C-14      |               | Yes / No          |                          |             |
| J    | C-15      |               | Yes / No          |                          |             |
