# Variations: listen-adoption — Round 20

**Rubric:** v20 | **New criteria:** C-55, C-56, C-57 | **Max composite:** 335 | **Golden threshold (80%):** 268 pts | **Projected ceiling:** 330/335 (C-19 paradox persists)

---

## Variation Axes

| Axis | R20 Target | Description |
|------|-----------|-------------|
| Lifecycle emphasis | C-58+ candidate: Protected behavior census at phase entry | Each phase entry state declaration adds an explicit census of which I-0X Protected behaviors remain active vs. displaced at that phase entry point. The census shifts phase entry from a re-citation of the prior close ledger text to a per-behavior displacement inventory: the model must account for all five Protected behaviors at every phase entry, not just the narrative state at the prior phase boundary. |
| Output format | C-59+ candidate: ARC CORRECTION BLOCK label carries Protected behavior | When C-57 fires an ARC CORRECTION BLOCK for a phase-transition MISMATCH, the block label carries the I-0X and Protected behavior active at that boundary: `ARC CORRECTION BLOCK -- PHASE N close -> PHASE N+1 open MISMATCH -- Protected behavior at boundary: [I-0X: named behavior]`. Extends C-55's correction-label enrichment from Gate H citation failures to arc integrity failures. |
| Inertia framing | C-60+ candidate: SECTION K arc table carries Protected behavior column | The SECTION K DISPLACEMENT ARC INTEGRITY CHECK table gains a "Protected behavior at boundary: [I-0X + named behavior from SECTION A]" column per transition row. SECTION K becomes self-sufficient at the displacement-stake level for arc verification: an auditor can determine both arc consistency and what displacement commitment was at risk at each transition without reading SECTION A. |

**Single-axis (V-01, V-02, V-03):** Lifecycle emphasis · Output format · Inertia framing
**Combined (V-04):** Lifecycle emphasis + Output format
**Full (V-05):** Lifecycle emphasis + Output format + Inertia framing

---

## Baseline (all five carry from R19 V-05)

| Element | Criterion | Form |
|---|---|---|
| STRUCTURAL CONTRACT naming answer-form AND mechanism anchor as mandatory co-present | C-35 | Block before SECTION A |
| Per-gate MECHANISM STATE footers in SECTIONS H, I, J | C-34 (gate-level anchor) | `> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED -- Gate X [...]` |
| Pre-verification MECHANISM STATE declaration before `## VERIFICATION MODE` | C-34 (boundary-level anchor) | `> CORRECTION BLOCK MECHANISM ARMED -- no gate failure triggered` |
| SECTION A Named Inertia IDs, I-01 through I-05 | C-11 | Table: Inertia ID \| Archetype \| Named Inertia \| Structural reason |
| SECTION A DOWNSTREAM CITATION CONTRACT with Protected behavior column AND Gate H Status field per row | C-49, C-50, C-54 | Three-field structural slot per row: citation sinks · Protected behavior · Gate H Status |
| TABLE 1 with SLOT-KEY: row prefix AND Incumbent Dependency AND Inertia ID columns | C-43, C-41, C-37 | SLOT-KEY: row label |
| PHASE 1 fixed entry-state declaration | C-45 | "THE INCUMBENT is fully entrenched -- all Protected behavior declarations fully active" |
| PHASES 2, 4, 5, 6 with `Displacement state at phase entry:` re-citing preceding close ledger | C-45 | Verbatim re-citation |
| PHASE 3 entry-state field re-citing PHASE 2 exit state | C-45 | "Displacement state entering PHASE 3: [re-cite]" |
| PHASE 1-2, 4-6 phase-close displacement ledger footer | C-45, C-25 | `Incumbent position after this phase:` + `Inertia ID this phase overcame:` |
| PHASE 3 phase-close ledger variant | C-45, C-39 | `Inertia ID defending THE INCUMBENT at this boundary:` + Protected behavior |
| PHASE 3 with CHASM-A / CHASM-B / CHASM-C structural subsections | C-39 | Named subsection headers |
| Q-BARRIER answer-form questions per adoption phase citing Protected behavior | C-29 | Embedded question requiring I-0X as coherent answer; parenthetical names contract row Protected behavior |
| TABLE 3 typed header + SLOT-KEY: row labels | C-36, C-38, C-28 | Named transition pair rows |
| PART 2 CHASM-A/B/C EXPANSION with Named Inertia + Incumbent position per slot | C-42, C-40, C-48 | Two mandatory opening fields per subsection |
| PART 3 churn register with SLOT-KEY: row prefix + Q-TRIGGER + concrete-action field | C-46, C-27, C-15 | `SLOT-KEY: [Role] -- churn entry` |
| PART 4 champion network with SLOT-KEY: row prefix + Q-CHAMPION answer-form | C-47, C-14, C-29 | Two-anchor typed slot |
| PART 5 Incumbent Impact column AND Targets inertia: column | C-26, C-44 | Per-row displacement stake |
| C-24 Terminal Invariant names BOTH falsification cases | C-24 | No CORRECTION BLOCK at cited location, or block without BEFORE field |
| SECTION K per-gate execution stamps | C-30, C-20 | Records PASS / FAIL + revision status |
| SECTION K CITATION CONTRACT COMPLETION RECORD with Protected behavior column | C-51, C-56 | Per-I-0X compliance mirror carrying Protected behavior from SECTION A (C-56 active) |
| SECTION H per-I-0X CORRECTION BLOCK with I-0X label AND Protected behavior | C-52, C-55 | `CORRECTION BLOCK -- I-0X CITATION CONTRACT VIOLATION -- Protected behavior: [named behavior]` (C-55 active) |
| SECTION K DISPLACEMENT ARC INTEGRITY CHECK with three-state verdict and ARC CORRECTION BLOCK | C-53, C-57 | MATCH / MISMATCH / CORRECTED; MISMATCH triggers mandatory ARC CORRECTION BLOCK (C-57 active) |

---

## Axis activation map

| Variation | Axis A: Protected behavior census at phase entry | Axis B: ARC CORRECTION BLOCK label carries Protected behavior | Axis C: SECTION K arc table carries Protected behavior column | Delta from R19 V-05 baseline |
|---|---|---|---|---|
| V-01 | **Active:** phase entry census enumerates all active/displaced Protected behaviors | Baseline | Baseline | Phase entry becomes per-behavior displacement inventory |
| V-02 | Baseline | **Active:** ARC CORRECTION BLOCK label carries I-0X + Protected behavior at boundary | Baseline | Arc repair label names displacement stake at risk |
| V-03 | Baseline | Baseline | **Active:** SECTION K arc table carries Protected behavior column | Terminal arc record is self-sufficient at displacement-stake level |
| V-04 | Active (V-01) | Active (V-02) | Baseline | Census at entry + enriched arc repair labels |
| V-05 | Active (V-01) | Active (V-02) | Active (V-03) | All three: census + arc label + arc table column |

---

## V-01 -- Single Axis: Lifecycle Emphasis (Protected Behavior Census at Phase Entry)

**Variation axis:** Lifecycle emphasis -- each phase entry state declaration carries a mandatory "Protected behaviors still active at entry:" census field that enumerates all I-0X IDs whose Protected behaviors have not yet been displaced at this phase entry moment, plus a "Displaced since document open:" field listing I-0X IDs whose Protected behaviors have been partially or fully overcome by prior phases. PHASE 1 entry is fixed: all five are active. Each subsequent phase entry must update the census from the prior phase-close ledger state, making the census a running per-behavior displacement inventory maintained at every phase boundary.

**Hypothesis:** C-45 produces a per-phase displacement ledger at phase close, tracking the displacement arc as a narrative chain. C-53/C-57 verify and repair that chain at SECTION K. But there is no mechanism that makes the model explicitly account for ALL five Protected behaviors at each phase entry -- only the one most relevant to the incoming archetype is questioned (Q-BARRIER). A model can write a displacement arc that is narratively coherent for one inertia ID while leaving the others unaccounted. The Protected behavior census closes this gap at the entry side: before writing any phase body, the model must enumerate all five behaviors and classify each as active or displaced. A census that is incomplete (wrong count of active behaviors) is structurally conspicuous -- the five-row census leaves no room for silent omission. This is the phase-entry complement of C-45 (phase-close ledger) applied to the full behavior set rather than only the phase's primary inertia.

---

Simulate the adoption curve for {{topic}} across the 16 stock roles (PM, UX, C-01 through C-12, Support, SRE). Produce the artifact below in full. Every bracketed instruction is a fill contract -- complete it before proceeding to the next section.

---

## STRUCTURAL CONTRACT

This document encodes two mandatory co-present architectural requirements. No variation or omission of either is permitted.

**REQUIREMENT 1 -- ANSWER-FORM CITATION ENFORCEMENT (C-29):**
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

**REQUIREMENT 2 -- CORRECTION BLOCK MECHANISM STATE (C-32, C-34):**
A MECHANISM STATE line appears as a blockquote footer inside each of SECTIONS H, I, J (gate-level anchor) AND as a pre-verification declaration immediately before `## VERIFICATION MODE` (boundary-level anchor). Both anchors are mandatory regardless of gate outcomes. Under this variation: Gate H CORRECTION BLOCK labels carry Protected behavior (C-55 baseline). SECTION K CITATION CONTRACT COMPLETION RECORD carries Protected behavior column (C-56 baseline). Arc MISMATCH triggers ARC CORRECTION BLOCK (C-57 baseline). Phase entry states carry Protected behavior census (Axis A).

Both requirements are mandatory co-present structural features. A document satisfying only one fails C-33 and C-35.

---

## SECTION A -- Named Inertia IDs

Assign one Named Inertia ID per canonical Rogers archetype. The inertia is the structural reason that archetype resists adoption of {{topic}}.

| Inertia ID | Archetype      | Named Inertia                      | Structural reason this archetype resists |
|------------|----------------|------------------------------------|------------------------------------------|
| I-01       | Innovator      | [name the inertia for Innovators]  | [structural reason]                      |
| I-02       | Early Adopter  | [name the inertia for EA]          | [structural reason]                      |
| I-03       | Early Majority | [name the inertia for EM]          | [structural reason]                      |
| I-04       | Late Majority  | [name the inertia for LM]          | [structural reason]                      |
| I-05       | Laggard        | [name the inertia for Laggards]    | [structural reason]                      |

### SECTION A -- DOWNSTREAM CITATION CONTRACT

The Protected behavior column is filled at SECTION A generation time -- before writing any phase body. It commits the displacement stake per inertia ID. Gate H fills Gate H Status at audit time. When Gate H fires a CORRECTION BLOCK (C-52), the label carries both I-0X and Protected behavior (C-55 baseline). SECTION K CITATION CONTRACT COMPLETION RECORD carries this column (C-56 baseline). Phase entry Protected behavior census enumerates which behaviors remain active per phase (Axis A).

| Inertia ID | Mandatory downstream citation locations | Protected behavior: [specific incumbent behavior this inertia defends -- fill at generation time] | Gate H Status |
|------------|-----------------------------------------|--------------------------------------------------------------------------------------------------|---------------|
| I-01 | PHASE 1 Q-BARRIER · PHASE 1 phase-close ledger · PART 3 Q-TRIGGER (Innovator-archetype role) | [fill: what THE INCUMBENT behavior/habit I-01 protects] | Gate H Status: [PASS / FAIL -- cite satisfied location, or cite violation] |
| I-02 | PHASE 2 Q-BARRIER · PHASE 2 phase-close ledger · PART 3 Q-TRIGGER (EA-archetype role) | [fill: what THE INCUMBENT behavior/habit I-02 protects] | Gate H Status: [PASS / FAIL -- cite satisfied location, or cite violation] |
| I-03 | PHASE 3 Q-BARRIER · PHASE 3 phase-close ledger · CHASM-A EXPANSION Named Inertia · CHASM-B EXPANSION Named Inertia · PHASE 4 Q-BARRIER · PHASE 4 phase-close ledger · at least one PART 5 Targets inertia: row | [fill: what THE INCUMBENT behavior/habit I-03 protects -- core EM workflow dependency] | Gate H Status: [PASS / FAIL -- cite satisfied location, or cite violation] |
| I-04 | PHASE 5 Q-BARRIER · PHASE 5 phase-close ledger · PART 3 Q-TRIGGER (LM-archetype role) | [fill: what THE INCUMBENT behavior/habit I-04 protects] | Gate H Status: [PASS / FAIL -- cite satisfied location, or cite violation] |
| I-05 | PHASE 6 Q-BARRIER · PHASE 6 phase-close ledger · PART 3 Q-TRIGGER (Laggard-archetype role) | [fill: what THE INCUMBENT behavior/habit I-05 protects] | Gate H Status: [PASS / FAIL -- cite satisfied location, or cite violation] |

SECTION H audits against this contract row by row. When Gate H marks any row FAIL, the resulting CORRECTION BLOCK label carries both I-0X and Protected behavior (C-55): `CORRECTION BLOCK -- I-0X CITATION CONTRACT VIOLATION -- Protected behavior: [value from this row's Protected behavior column]`.

---

THE INCUMBENT is [name the current workflow, tool, or practice being displaced by {{topic}}]. All phase bodies, champion entries, churn triggers, and interventions run through the displacement lens: what does this phase do to THE INCUMBENT's position?

---

## TABLE 1 -- Role Archetype Map

TABLE 1 header contract: Each row below is prefixed SLOT-KEY: -- the row label is a typed structural slot key re-asserting the three co-present contracts (archetype assignment, Incumbent Dependency, Inertia ID citation) at this row's generation moment, independently of the column headers.

| Role (SLOT-KEY typed slot) | Rogers Archetype | Incumbent Dependency: [workflow step this role relies on THE INCUMBENT to perform] | Inertia ID: [cite I-0X from SECTION A -- named inertia explaining this role's resistance] |
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

## PHASE 1 INNOVATORS -- Month 1

Displacement state at phase entry: THE INCUMBENT is fully entrenched -- {{topic}} has not been introduced to any stock role. No displacement has occurred; all TABLE 1 Incumbent Dependency values are load-bearing; all Protected behavior declarations in the DOWNSTREAM CITATION CONTRACT are fully active.

Protected behaviors still active at entry: I-01 ([Protected behavior name]) · I-02 ([Protected behavior name]) · I-03 ([Protected behavior name]) · I-04 ([Protected behavior name]) · I-05 ([Protected behavior name])
Displaced since document open: none

Q-BARRIER: Which Named Inertia ID is the primary barrier even for Innovators?
(Cite I-01 from SECTION A -- what Protected behavior from contract row I-01 does this archetype most tightly hold?)

[Phase body: named roles, what they try, what signals they produce, displacement impact on THE INCUMBENT's position]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what workflow, process, or role dependency THE INCUMBENT retains after Month 1 -- which Protected behaviors from I-01's contract row begin to weaken]
Inertia ID this phase overcame (partially): [re-cite I-01 from Q-BARRIER above]

---

## PHASE 2 EARLY ADOPTERS -- Month 2-3

Displacement state at phase entry: [re-cite verbatim the "Incumbent position after this phase:" value from PHASE 1's phase-close ledger]

Protected behaviors still active at entry: [enumerate I-0X IDs whose Protected behaviors are not yet fully displaced -- update from PHASE 1 close ledger; at minimum I-02 through I-05 remain fully active]
Displaced since document open: [enumerate I-0X IDs whose Protected behaviors were partially overcome in PHASE 1, or "none -- I-01 only weakened, not displaced"]

Q-BARRIER: Which Named Inertia ID is the primary barrier for Early Adopters?
(Cite I-02 from SECTION A -- what Protected behavior from contract row I-02 resists these roles?)

[Phase body: named roles, what they adopt, spread mechanism from PHASE 1, incumbent displacement progress]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what THE INCUMBENT still controls after Month 3 -- which TABLE 1 Incumbent Dependency values remain load-bearing]
Inertia ID this phase overcame (partially): [re-cite I-02 from Q-BARRIER above]

---

## PHASE 3 CHASM -- Month 4 (Non-Adoption Crossing Event)

Displacement state entering PHASE 3: [re-cite verbatim the "Incumbent position after this phase:" value from PHASE 2's phase-close ledger]

Protected behaviors still active at entry: [enumerate I-0X IDs not yet displaced -- update from PHASE 2 close ledger; I-03 through I-05 remain fully active]
Displaced since document open: [enumerate I-0X IDs whose Protected behaviors were partially overcome in PHASES 1-2]

PHASE 3 is not an adoption phase. It is a crossing event. No new archetype adopts in Month 4.

Q-BARRIER: Which Named Inertia ID is driving the chasm?
(Cite I-03 from SECTION A -- what Protected behavior from contract row I-03 makes the chasm structural rather than temporal?)

### CHASM-A -- Incumbent Defense

[Named incumbent defense mechanism -- explicitly connects to Protected behavior declared for I-03 in SECTION A; why this Protected behavior prevents Early Majority adoption regardless of Early Adopter endorsement]

### CHASM-B -- Bridge Condition

[Bridge condition as testable proposition: "The chasm is crossed when [specific observable condition]." Which roles must satisfy it. What artifact or signal proves it is met.]

### CHASM-C -- Early Crossing Signal

[First observable crossing signal -- named role, artifact, or behavioral event distinguishable from Early Adopter behavior]

**Phase-close displacement ledger:**
Inertia ID defending THE INCUMBENT at this boundary: [I-03 -- and state its Protected behavior from SECTION A contract row I-03]

---

## PHASE 4 EARLY MAJORITY -- Month 5-7

Displacement state at phase entry: [re-cite verbatim the "Inertia ID defending THE INCUMBENT at this boundary:" from PHASE 3's close ledger and state what THE INCUMBENT still controlled when Month 5 began]

Protected behaviors still active at entry: [enumerate I-0X IDs not yet displaced -- I-03 still active despite chasm crossing; I-04, I-05 fully active; I-01, I-02 may be partially displaced]
Displaced since document open: [enumerate I-0X IDs whose Protected behaviors were partially overcome in PHASES 1-3]

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Early Majority?
(Cite I-03 from SECTION A -- Protected behavior from contract row I-03 still active for these roles despite chasm crossing)

[Phase body: named roles, proof from CHASM-B, TABLE 1 Incumbent Dependency values now unblocked, incumbent displacement acceleration]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what THE INCUMBENT still controls after Month 7]
Inertia ID this phase overcame (partially): [re-cite I-03 from Q-BARRIER above]

---

## PHASE 5 LATE MAJORITY -- Month 8-10

Displacement state at phase entry: [re-cite verbatim the "Incumbent position after this phase:" value from PHASE 4's phase-close ledger]

Protected behaviors still active at entry: [enumerate I-0X IDs not yet fully displaced -- I-04 and I-05 remain active; I-03 partially overcome]
Displaced since document open: [enumerate I-0X IDs whose Protected behaviors were partially or fully overcome in PHASES 1-4]

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Late Majority?
(Cite I-04 from SECTION A -- what Protected behavior from contract row I-04 holds these roles back?)

[Phase body: named roles, adoption trigger, incumbent erosion, what remains of THE INCUMBENT's position]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what THE INCUMBENT still controls after Month 10]
Inertia ID this phase overcame (partially): [re-cite I-04 from Q-BARRIER above]

---

## PHASE 6 LAGGARDS -- Month 11-12

Displacement state at phase entry: [re-cite verbatim the "Incumbent position after this phase:" value from PHASE 5's phase-close ledger]

Protected behaviors still active at entry: [enumerate I-0X IDs not yet fully displaced -- I-05 remains; others may persist partially]
Displaced since document open: [enumerate I-0X IDs whose Protected behaviors were overcome in PHASES 1-5]

Q-BARRIER: Which Named Inertia ID keeps Laggards last?
(Cite I-05 from SECTION A -- what Protected behavior from contract row I-05 is the final holdout?)

[Phase body: named roles, final adoption conditions, terminal incumbent displacement state]

**Phase-close displacement ledger:**
Incumbent position after this phase: [terminal displacement state -- which Protected behaviors, if any, persist past Month 12]
Inertia ID this phase overcame: [re-cite I-05 from Q-BARRIER above]

---

## TABLE 3 -- Spread Mechanisms

TABLE 3 header contract: Each row below is prefixed SLOT-KEY: -- a typed structural slot key naming a specific canonical transition pair. The Spread Mechanism column must be filled with a named signal, artifact, or social proof event specific to {{topic}} -- not generic word-of-mouth.

| Transition Pair (SLOT-KEY row) | Spread Mechanism: [named signal or artifact specific to {{topic}} -- not generic word-of-mouth] | Month Range |
|---|---|---|
| SLOT-KEY: Innovator -> Early Adopter      | | |
| SLOT-KEY: Early Adopter -> Early Majority | | |
| SLOT-KEY: Early Majority -> Late Majority | | |
| SLOT-KEY: Late Majority -> Laggard        | | |

---

## PART 2 -- CHASM ANALYSIS (Full Expansion)

PHASE 3 introduced a diagnostic sketch of each chasm element. PART 2 expands each element to its full specification. Each subsection carries two mandatory opening fields: (1) Named Inertia ID re-citation and (2) Incumbent position at this chasm element.

### CHASM-A EXPANSION -- Incumbent Defense (Full Diagnosis)

Expanding CHASM-A from PHASE 3 --
Named Inertia in effect: [re-cite I-03 -- required by DOWNSTREAM CITATION CONTRACT row I-03]
Incumbent position at this chasm element: [what THE INCUMBENT controls at the incumbent-defense layer]

[Full diagnosis: complete mechanism by which THE INCUMBENT defends its position at the chasm boundary]

### CHASM-B EXPANSION -- Bridge Condition (Full Specification)

Expanding CHASM-B from PHASE 3 --
Named Inertia in effect: [re-cite I-03 -- required by DOWNSTREAM CITATION CONTRACT row I-03]
Incumbent position at this chasm element: [what THE INCUMBENT holds at the bridge-condition layer]

[Full specification: bridge condition as testable proposition, precise observable state, which role or artifact produces it]

### CHASM-C EXPANSION -- Crossing Signal (Full Identification)

Expanding CHASM-C from PHASE 3 --
Named Inertia in effect: [re-cite I-03 -- the Named Inertia ID whose weakening produces the crossing signal]
Incumbent position at this chasm element: [what THE INCUMBENT has already lost and what it still retains]

[Full identification: crossing signal named with precision -- specific role, behavioral event, or artifact emission]

---

## PART 3 -- Churn Risk Register

Every role that adopts carries a reversion risk. List all roles at non-trivial churn risk.

PART 3 header contract: Each row is prefixed SLOT-KEY: -- typed structural slot key re-asserting the three churn contracts (reversion trigger | retention intervention | inertia ID) at this row's generation moment. Q-TRIGGER citations fulfill DOWNSTREAM CITATION CONTRACT rows I-01, I-02, I-04, I-05.

| Role (SLOT-KEY typed slot) | Reversion trigger: [specific condition that causes this role to revert to THE INCUMBENT] | Retention intervention: [one concrete action that reduces reversion probability -- not a surveillance flag] | Q-TRIGGER: Which Named Inertia ID drives reversion risk for this role? (Cite I-0X from SECTION A) |
|------|-----|-----|-----|
| SLOT-KEY: [Role] -- churn entry | | | |

---

## PART 4 -- Champion Network

Name at least three roles positioned to advocate for {{topic}} adoption and displace THE INCUMBENT.

PART 4 header contract: Each row is prefixed SLOT-KEY: -- typed structural slot key re-asserting the two co-present champion contracts (archetype-bridge rationale + Q-CHAMPION I-0X) at this row's generation moment.

| Champion Role (SLOT-KEY typed slot) | Archetype | Archetype-bridge rationale: [why this role's archetype position makes it an effective champion for the next tier] | Q-CHAMPION: Named Inertia ID this champion is positioned to overcome (I-0X from SECTION A) | Why this champion displaces THE INCUMBENT for the target tier |
|---|---|---|---|---|
| SLOT-KEY: [Role] -- champion entry | | | | |
| SLOT-KEY: [Role] -- champion entry | | | | |
| SLOT-KEY: [Role] -- champion entry | | | | |

---

## PART 5 -- Intervention Ranking

Rank retention interventions by adoption delta. Each entry must reference at least one named phase and one named role.

| Rank | Intervention | Adoption delta | Phase(s) affected | Role(s) affected | Incumbent Impact: [what THE INCUMBENT loses when this intervention succeeds] | Targets inertia: [I-0X -- Q-INTERVENTION: which Named Inertia ID does this intervention directly address?] |
|------|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |

---

## PART 6 -- Sensitivity Analysis

| Scenario      | Adoption outcome | Named lever | Direction of shift |
|---------------|------------------|-------------|-------------------|
| Fast Adoption |                  |             |                   |
| Slow Adoption |                  |             |                   |

---

## PART 7 -- Signal Readiness Table

| Signal name | Threshold | Interpretation: what this signal level means for {{topic}} adoption timing |
|-------------|-----------|----------------------------------------------------------------------------|
|             |           |                                                                            |

---

> CORRECTION BLOCK MECHANISM ARMED -- no gate failure triggered. If Gate H fails on any contract row, a CORRECTION BLOCK will be inserted immediately above this line labeled: `CORRECTION BLOCK -- I-0X CITATION CONTRACT VIOLATION -- Protected behavior: [value from SECTION A contract row I-0X Protected behavior column]` (C-55 baseline). If the DISPLACEMENT ARC INTEGRITY CHECK finds a MISMATCH, an ARC CORRECTION BLOCK will be inserted immediately above this line (C-57 baseline). SECTION K CITATION CONTRACT COMPLETION RECORD carries Protected behavior column (C-56 baseline).

## VERIFICATION MODE

All content generation is complete above this boundary. SECTIONS H, I, J, K are audit sections only. No content generation occurs below this line.

---

## SECTION H -- Gate: C-13 Audit (Named Inertia IDs as Downstream Backbone)

**Criterion C-13:** Named Inertia IDs from SECTION A are cited by ID (I-0X) in at least four downstream location types: bridge conditions, intervention rationale, champion rationale, and churn register entries.

**Audit against DOWNSTREAM CITATION CONTRACT -- fill Gate H Status per row:**

- I-01: PHASE 1 Q-BARRIER [Y/N] · PHASE 1 ledger [Y/N] · PART 3 Q-TRIGGER Innovator role [Y/N] -> **Fill Gate H Status in SECTION A row I-01**
- I-02: PHASE 2 Q-BARRIER [Y/N] · PHASE 2 ledger [Y/N] · PART 3 Q-TRIGGER EA role [Y/N] -> **Fill Gate H Status in SECTION A row I-02**
- I-03: PHASE 3 Q-BARRIER [Y/N] · PHASE 3 ledger [Y/N] · CHASM-A Named Inertia [Y/N] · CHASM-B Named Inertia [Y/N] · PHASE 4 Q-BARRIER [Y/N] · PHASE 4 ledger [Y/N] · PART 5 Targets inertia: [Y/N] -> **Fill Gate H Status in SECTION A row I-03**
- I-04: PHASE 5 Q-BARRIER [Y/N] · PHASE 5 ledger [Y/N] · PART 3 Q-TRIGGER LM role [Y/N] -> **Fill Gate H Status in SECTION A row I-04**
- I-05: PHASE 6 Q-BARRIER [Y/N] · PHASE 6 ledger [Y/N] · PART 3 Q-TRIGGER Laggard role [Y/N] -> **Fill Gate H Status in SECTION A row I-05**

**C-13 four-location check:** Bridge conditions [Y/N] | Intervention rationale [Y/N] | Champion rationale [Y/N] | Churn register [Y/N]

**Gate H result:** [PASS if all four C-13 location types satisfied AND all contract rows PASS | FAIL: name specific I-0X and specific missed location]

**Per-I-0X correction obligation with Protected behavior label (C-55 baseline):** If any contract row shows FAIL, produce a dedicated CORRECTION BLOCK for each failed row immediately before the pre-verification declaration, labeled: `CORRECTION BLOCK -- I-0X CITATION CONTRACT VIOLATION -- Protected behavior: [value from SECTION A contract row I-0X Protected behavior column]`. Each failed I-0X row produces its own block. Do not combine multiple I-0X failures into a single block.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED -- Gate H [PASS: no per-I-0X correction triggered | FAIL: per-I-0X CORRECTION BLOCK(s) written above pre-verification line, each carrying I-0X ID and Protected behavior in label]

---

## SECTION I -- Gate: C-14 Audit (Champion Rationale Double-Anchored)

**Criterion C-14:** Each SLOT-KEY: champion entry in PART 4 contains both (a) archetype-bridge rationale and (b) a Named Inertia ID cited by Q-CHAMPION.

- SLOT-KEY champion 1 [name]: archetype-bridge present? [Y/N] | Q-CHAMPION I-0X cited? [Y/N]
- SLOT-KEY champion 2 [name]: archetype-bridge present? [Y/N] | Q-CHAMPION I-0X cited? [Y/N]
- SLOT-KEY champion 3 [name]: archetype-bridge present? [Y/N] | Q-CHAMPION I-0X cited? [Y/N]

**Gate I result:** [PASS if both anchors present for all entries | FAIL with specific entry named]

**Revision obligation:** If Gate I FAILS, produce a CORRECTION BLOCK immediately before the pre-verification declaration. Do not proceed to SECTION J until written.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED -- Gate I [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION J -- Gate: C-15 Audit (Concrete Retention Actions)

**Criterion C-15:** Every mitigation in PART 3's churn register is a concrete retention action. Surveillance-only entries ("track usage," "monitor engagement") fail this criterion.

- [List each SLOT-KEY: churn entry and classification: concrete action or surveillance flag]

**Gate J result:** [PASS if all entries contain concrete retention actions | FAIL if any contains only a surveillance flag]

**Revision obligation:** If Gate J FAILS, produce a CORRECTION BLOCK immediately before the pre-verification declaration. Do not proceed to SECTION K until written.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED -- Gate J [PASS: no correction triggered | FAIL: CORRECTION BLOCK written above pre-verification line]

---

## SECTION K -- Terminal Audit Record

Per-gate execution stamps are recorded here for all three gates regardless of outcome.

**Terminal Invariant:** For every gate with "Revision Performed: Yes," a CORRECTION BLOCK with BEFORE and AFTER fields must exist at the cited location above the pre-verification declaration. A Yes entry whose cited location contains no CORRECTION BLOCK, or a CORRECTION BLOCK without a BEFORE field, falsifies this invariant. Gate H failures produce per-I-0X labeled CORRECTION BLOCKS carrying Protected behavior in the label (C-55). Arc MISMATCH repairs produce ARC CORRECTION BLOCKS at the same location; SECTION K records arc correction entries (C-57).

| Gate | Criterion | Initial result | Revision performed | CORRECTION BLOCK location | Final result |
|------|-----------|----------------|--------------------|--------------------------|--------------|
| H    | C-13      |                | Yes / No           |                          |              |
| I    | C-14      |                | Yes / No           |                          |              |
| J    | C-15      |                | Yes / No           |                          |              |

**CITATION CONTRACT COMPLETION RECORD (with Protected behavior column -- C-56 baseline):**

The Protected behavior column is sourced from SECTION A's DOWNSTREAM CITATION CONTRACT, declared at generation time. This record is a displacement-commitment certificate: PASS confirms that each Protected behavior's citation coverage was satisfied; FAIL names which Protected behavior's displacement accountability remains unaddressed.

| Inertia ID | Required sinks satisfied | Structural location found (or NOT FOUND) | Protected behavior: [carry from SECTION A contract row] | Gate H Status |
|------------|--------------------------|------------------------------------------|---------------------------------------------------------|---------------|
| I-01       |                          |                                          | [carry from SECTION A I-01 Protected behavior]          |               |
| I-02       |                          |                                          | [carry from SECTION A I-02 Protected behavior]          |               |
| I-03       |                          |                                          | [carry from SECTION A I-03 Protected behavior]          |               |
| I-04       |                          |                                          | [carry from SECTION A I-04 Protected behavior]          |               |
| I-05       |                          |                                          | [carry from SECTION A I-05 Protected behavior]          |               |

**DISPLACEMENT ARC INTEGRITY CHECK (with mandatory-repair protocol -- C-57 baseline):**

For each phase-transition pair, record the exit-state text from the preceding close ledger and the entry-state text from the next phase opening field. A MATCH verdict confirms verbatim re-citation. A MISMATCH triggers an ARC CORRECTION BLOCK (inserted above the pre-verification declaration) and the verdict updates to CORRECTED after repair.

| Transition | Exit state (from close ledger) | Entry state (from phase open) | Verdict |
|---|---|---|---|
| PHASE 1 close -> PHASE 2 open | [Incumbent position after PHASE 1] | [Displacement state at PHASE 2 entry] | MATCH / MISMATCH / CORRECTED |
| PHASE 2 close -> PHASE 3 entry | [Incumbent position after PHASE 2] | [Displacement state entering PHASE 3] | MATCH / MISMATCH / CORRECTED |
| PHASE 3 close -> PHASE 4 open | [Inertia defending THE INCUMBENT at PHASE 3 boundary] | [Displacement state at PHASE 4 entry] | MATCH / MISMATCH / CORRECTED |
| PHASE 4 close -> PHASE 5 open | [Incumbent position after PHASE 4] | [Displacement state at PHASE 5 entry] | MATCH / MISMATCH / CORRECTED |
| PHASE 5 close -> PHASE 6 open | [Incumbent position after PHASE 5] | [Displacement state at PHASE 6 entry] | MATCH / MISMATCH / CORRECTED |

Arc integrity: [PASS if all MATCH or CORRECTED | FAIL naming specific unrepaired discontinuity]

ARC CORRECTION BLOCK location(s): [cite location above pre-verification declaration, or "none -- all MATCH"]

---
## V-02 -- Single Axis: Output Format (ARC CORRECTION BLOCK Label Carries Protected Behavior)

**Variation axis:** Output format -- when C-57 fires an ARC CORRECTION BLOCK for a phase-transition MISMATCH, the block label carries the I-0X and Protected behavior active at that phase boundary: `ARC CORRECTION BLOCK -- PHASE N close -> PHASE N+1 open MISMATCH -- Protected behavior at boundary: [I-0X: named behavior from SECTION A]`. The Protected behavior field is sourced from the DOWNSTREAM CITATION CONTRACT row for the inertia ID active at that specific phase-close ledger (I-01 at PHASE 1 close, I-02 at PHASE 2 close, I-03 at PHASE 3/4 close, I-04 at PHASE 5 close, I-05 at PHASE 6 close). Arc correction labels now parallel Gate H correction labels: both carry I-0X and Protected behavior, making the displacement stake legible from the label without SECTION A cross-reference.

**Hypothesis:** C-55 closes the correction-label enrichment loop for citation failures: the label names the displacement stake at risk. C-57 closes the arc repair loop: MISMATCH triggers mandatory repair. But the ARC CORRECTION BLOCK is currently anonymous at the displacement-stake level -- the label names the phase boundary but not what Protected behavior was at risk when the narrative chain broke. A broken arc at PHASE 3 -> PHASE 4 means I-03 Protected behavior was the active stake -- the very behavior the chasm was attempting to overcome. Protected behavior in the ARC CORRECTION BLOCK label closes this: the repair is self-describing at the displacement-stake level, matching the C-55 standard. A reviewer reading the label alone can determine both the structural failure and its displacement consequence.

---

Simulate the adoption curve for {{topic}} across the 16 stock roles (PM, UX, C-01 through C-12, Support, SRE). Produce the artifact below in full. Every bracketed instruction is a fill contract -- complete it before proceeding to the next section.

---

## STRUCTURAL CONTRACT

This document encodes two mandatory co-present architectural requirements. No variation or omission of either is permitted.

**REQUIREMENT 1 -- ANSWER-FORM CITATION ENFORCEMENT (C-29):**
Named Inertia ID citations throughout this document are answers to explicit answer-form questions embedded in structural positions. The following questions are mandatory:

  Q-BARRIER:       Which Named Inertia ID is the primary barrier here? (Cite I-0X from SECTION A)
  Q-CHAMPION:      Named Inertia ID this champion is positioned to overcome: (Cite I-0X from SECTION A)
  Q-TRIGGER:       Which Named Inertia ID drives reversion risk for this role? (Cite I-0X from SECTION A)
  Q-INTERVENTION:  Which Named Inertia ID does this intervention directly target? (Cite I-0X from SECTION A)

**REQUIREMENT 2 -- CORRECTION BLOCK MECHANISM STATE (C-32, C-34):**
MECHANISM STATE inside each of SECTIONS H, I, J AND before VERIFICATION MODE. Gate H CORRECTION BLOCK labels carry Protected behavior (C-55 baseline). SECTION K CITATION CONTRACT COMPLETION RECORD carries Protected behavior column (C-56 baseline). Arc MISMATCH triggers ARC CORRECTION BLOCK whose label carries Protected behavior at boundary (Axis B, extending C-57 baseline).

Both requirements mandatory co-present.

---

## SECTION A -- Named Inertia IDs

| Inertia ID | Archetype      | Named Inertia | Structural reason |
|------------|----------------|---------------|-------------------|
| I-01       | Innovator      | [name]        | [reason]          |
| I-02       | Early Adopter  | [name]        | [reason]          |
| I-03       | Early Majority | [name]        | [reason]          |
| I-04       | Late Majority  | [name]        | [reason]          |
| I-05       | Laggard        | [name]        | [reason]          |

### SECTION A -- DOWNSTREAM CITATION CONTRACT

Protected behavior filled at generation time. Gate H fills Gate H Status. Gate H CORRECTION BLOCK labels carry I-0X + Protected behavior (C-55). ARC CORRECTION BLOCK labels carry I-0X + Protected behavior active at the phase-close boundary (Axis B). SECTION K carries Protected behavior column (C-56).

| Inertia ID | Mandatory downstream citation locations | Protected behavior: [fill at generation time] | Gate H Status |
|------------|-----------------------------------------|-----------------------------------------------|---------------|
| I-01 | PHASE 1 Q-BARRIER / PHASE 1 ledger / PART 3 Q-TRIGGER Innovator | [fill] | [PASS / FAIL] |
| I-02 | PHASE 2 Q-BARRIER / PHASE 2 ledger / PART 3 Q-TRIGGER EA | [fill] | [PASS / FAIL] |
| I-03 | PHASE 3 Q-BARRIER / PHASE 3 ledger / CHASM-A / CHASM-B / PHASE 4 Q-BARRIER / PHASE 4 ledger / PART 5 | [fill] | [PASS / FAIL] |
| I-04 | PHASE 5 Q-BARRIER / PHASE 5 ledger / PART 3 Q-TRIGGER LM | [fill] | [PASS / FAIL] |
| I-05 | PHASE 6 Q-BARRIER / PHASE 6 ledger / PART 3 Q-TRIGGER Laggard | [fill] | [PASS / FAIL] |

---

THE INCUMBENT is [name the current workflow, tool, or practice being displaced by {{topic}}].

---

## TABLE 1 -- Role Archetype Map

TABLE 1 header contract: Each row prefixed SLOT-KEY: -- three co-present contracts per row.

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

## PHASE 1 INNOVATORS -- Month 1

Displacement state at phase entry: THE INCUMBENT is fully entrenched -- all Protected behavior declarations fully active.

Q-BARRIER: Which Named Inertia ID is the primary barrier even for Innovators?
(Cite I-01 from SECTION A -- what Protected behavior from contract row I-01 does this archetype most tightly hold?)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what THE INCUMBENT retains after Month 1]
Inertia ID this phase overcame (partially): [re-cite I-01]

---

## PHASE 2 EARLY ADOPTERS -- Month 2-3

Displacement state at phase entry: [re-cite verbatim PHASE 1 Incumbent position after this phase:]

Q-BARRIER: Which Named Inertia ID is the primary barrier for Early Adopters?
(Cite I-02 -- what Protected behavior from contract row I-02 resists these roles?)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what THE INCUMBENT still controls after Month 3]
Inertia ID this phase overcame (partially): [re-cite I-02]

---

## PHASE 3 CHASM -- Month 4 (Non-Adoption Crossing Event)

Displacement state entering PHASE 3: [re-cite verbatim PHASE 2 Incumbent position after this phase:]

PHASE 3 is not an adoption phase. No new archetype adopts in Month 4.

Q-BARRIER: Which Named Inertia ID is driving the chasm?
(Cite I-03 -- what Protected behavior from contract row I-03 makes the chasm structural?)

### CHASM-A -- Incumbent Defense

[Named incumbent defense mechanism]

### CHASM-B -- Bridge Condition

[Bridge condition as testable proposition]

### CHASM-C -- Early Crossing Signal

[First observable crossing signal]

**Phase-close displacement ledger:**
Inertia ID defending THE INCUMBENT at this boundary: [I-03 -- and its Protected behavior from SECTION A]

---

## PHASE 4 EARLY MAJORITY -- Month 5-7

Displacement state at phase entry: [re-cite verbatim PHASE 3 close + what THE INCUMBENT still controlled entering Month 5]

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Early Majority?
(Cite I-03 -- Protected behavior from contract row I-03 still active despite chasm crossing)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what THE INCUMBENT still controls after Month 7]
Inertia ID this phase overcame (partially): [re-cite I-03]

---

## PHASE 5 LATE MAJORITY -- Month 8-10

Displacement state at phase entry: [re-cite verbatim PHASE 4 Incumbent position after this phase:]

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Late Majority?
(Cite I-04 -- what Protected behavior from contract row I-04 holds these roles back?)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what THE INCUMBENT still controls after Month 10]
Inertia ID this phase overcame (partially): [re-cite I-04]

---

## PHASE 6 LAGGARDS -- Month 11-12

Displacement state at phase entry: [re-cite verbatim PHASE 5 Incumbent position after this phase:]

Q-BARRIER: Which Named Inertia ID keeps Laggards last?
(Cite I-05 -- what Protected behavior from contract row I-05 is the final holdout?)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [terminal displacement state]
Inertia ID this phase overcame: [re-cite I-05]

---

## TABLE 3 -- Spread Mechanisms

| Transition Pair (SLOT-KEY row) | Spread Mechanism: [named signal or artifact -- not generic word-of-mouth] | Month Range |
|---|---|---|
| SLOT-KEY: Innovator -> Early Adopter      | | |
| SLOT-KEY: Early Adopter -> Early Majority | | |
| SLOT-KEY: Early Majority -> Late Majority | | |
| SLOT-KEY: Late Majority -> Laggard        | | |

---

## PART 2 -- CHASM ANALYSIS (Full Expansion)

### CHASM-A EXPANSION -- Incumbent Defense (Full Diagnosis)

Named Inertia in effect: [re-cite I-03]
Incumbent position at this chasm element: [displacement state]

[Full diagnosis]

### CHASM-B EXPANSION -- Bridge Condition (Full Specification)

Named Inertia in effect: [re-cite I-03]
Incumbent position at this chasm element: [displacement state]

[Full specification]

### CHASM-C EXPANSION -- Crossing Signal (Full Identification)

Named Inertia in effect: [re-cite I-03]
Incumbent position at this chasm element: [displacement state]

[Full identification]

---

## PART 3 -- Churn Risk Register

| Role (SLOT-KEY typed slot) | Reversion trigger: [specific condition] | Retention intervention: [concrete action -- not surveillance flag] | Q-TRIGGER: Which Named Inertia ID drives reversion risk? (Cite I-0X) |
|------|-----|-----|-----|
| SLOT-KEY: [Role] -- churn entry | | | |

---

## PART 4 -- Champion Network

| Champion Role (SLOT-KEY typed slot) | Archetype | Archetype-bridge rationale: [why this archetype position makes an effective champion] | Q-CHAMPION: Named Inertia ID this champion overcomes (I-0X) | Why this champion displaces THE INCUMBENT |
|---|---|---|---|---|
| SLOT-KEY: [Role] -- champion entry | | | | |
| SLOT-KEY: [Role] -- champion entry | | | | |
| SLOT-KEY: [Role] -- champion entry | | | | |

---

## PART 5 -- Intervention Ranking

| Rank | Intervention | Adoption delta | Phase(s) affected | Role(s) affected | Incumbent Impact: [what THE INCUMBENT loses] | Targets inertia: [I-0X -- Q-INTERVENTION] |
|------|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |

---

## PART 6 -- Sensitivity Analysis

| Scenario      | Adoption outcome | Named lever | Direction of shift |
|---------------|------------------|-------------|-------------------|
| Fast Adoption |                  |             |                   |
| Slow Adoption |                  |             |                   |

---

## PART 7 -- Signal Readiness Table

| Signal name | Threshold | Interpretation |
|-------------|-----------|----------------|
|             |           |                |

---

> CORRECTION BLOCK MECHANISM ARMED -- no gate failure triggered. If Gate H fails, CORRECTION BLOCK above: CORRECTION BLOCK -- I-0X CITATION CONTRACT VIOLATION -- Protected behavior: [value from SECTION A] (C-55 baseline). If DISPLACEMENT ARC INTEGRITY CHECK finds MISMATCH, ARC CORRECTION BLOCK above: ARC CORRECTION BLOCK -- PHASE N close -> PHASE N+1 open MISMATCH -- Protected behavior at boundary: [I-0X: value from SECTION A for inertia active at that phase close] (Axis B). SECTION K carries Protected behavior column (C-56 baseline).

## VERIFICATION MODE

All content generation complete. SECTIONS H, I, J, K are audit sections only.

---

## SECTION H -- Gate: C-13 Audit

**Audit against DOWNSTREAM CITATION CONTRACT:**

- I-01: PHASE 1 Q-BARRIER [Y/N] / ledger [Y/N] / PART 3 Q-TRIGGER Innovator [Y/N] -> Fill SECTION A row I-01
- I-02: PHASE 2 Q-BARRIER [Y/N] / ledger [Y/N] / PART 3 Q-TRIGGER EA [Y/N] -> Fill SECTION A row I-02
- I-03: PHASE 3 Q-BARRIER [Y/N] / ledger [Y/N] / CHASM-A [Y/N] / CHASM-B [Y/N] / PHASE 4 Q-BARRIER [Y/N] / PHASE 4 ledger [Y/N] / PART 5 [Y/N] -> Fill SECTION A row I-03
- I-04: PHASE 5 Q-BARRIER [Y/N] / ledger [Y/N] / PART 3 Q-TRIGGER LM [Y/N] -> Fill SECTION A row I-04
- I-05: PHASE 6 Q-BARRIER [Y/N] / ledger [Y/N] / PART 3 Q-TRIGGER Laggard [Y/N] -> Fill SECTION A row I-05

**C-13 four-location check:** Bridge [Y/N] / Intervention [Y/N] / Champion [Y/N] / Churn [Y/N]

**Gate H result:** [PASS / FAIL]

**Correction obligation (C-55 baseline):** Per-I-0X: CORRECTION BLOCK -- I-0X CITATION CONTRACT VIOLATION -- Protected behavior: [value from SECTION A].

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED -- Gate H [PASS: no correction | FAIL: per-I-0X CORRECTION BLOCK(s) above, each carrying I-0X and Protected behavior]

---

## SECTION I -- Gate: C-14 Audit

- SLOT-KEY champion 1 [name]: archetype-bridge [Y/N] / Q-CHAMPION I-0X [Y/N]
- SLOT-KEY champion 2 [name]: archetype-bridge [Y/N] / Q-CHAMPION I-0X [Y/N]
- SLOT-KEY champion 3 [name]: archetype-bridge [Y/N] / Q-CHAMPION I-0X [Y/N]

**Gate I result:** [PASS / FAIL]

**Revision obligation:** If FAIL, produce CORRECTION BLOCK before pre-verification declaration.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED -- Gate I [PASS: no correction | FAIL: CORRECTION BLOCK written above]

---

## SECTION J -- Gate: C-15 Audit

- [List each SLOT-KEY: churn entry and classification]

**Gate J result:** [PASS / FAIL]

**Revision obligation:** If FAIL, produce CORRECTION BLOCK before pre-verification declaration.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED -- Gate J [PASS: no correction | FAIL: CORRECTION BLOCK written above]

---

## SECTION K -- Terminal Audit Record

**Terminal Invariant:** For every Yes, a CORRECTION BLOCK with BEFORE and AFTER fields must exist at cited location. A Yes without a CORRECTION BLOCK, or a CORRECTION BLOCK without BEFORE field, falsifies this invariant. Gate H produces per-I-0X CORRECTION BLOCKS carrying Protected behavior (C-55). Arc MISMATCH repairs produce ARC CORRECTION BLOCKS carrying Protected behavior at boundary (Axis B); SECTION K records their labels.

| Gate | Criterion | Initial result | Revision performed | CORRECTION BLOCK location | Final result |
|------|-----------|----------------|--------------------|--------------------------|--------------|
| H    | C-13      |                | Yes / No           |                          |              |
| I    | C-14      |                | Yes / No           |                          |              |
| J    | C-15      |                | Yes / No           |                          |              |

**CITATION CONTRACT COMPLETION RECORD (C-56 baseline):**

| Inertia ID | Required sinks satisfied | Structural location (or NOT FOUND) | Protected behavior: [carry from SECTION A] | Gate H Status |
|------------|--------------------------|------------------------------------|--------------------------------------------|---------------|
| I-01       |                          |                                    |                                            |               |
| I-02       |                          |                                    |                                            |               |
| I-03       |                          |                                    |                                            |               |
| I-04       |                          |                                    |                                            |               |
| I-05       |                          |                                    |                                            |               |

**DISPLACEMENT ARC INTEGRITY CHECK (ARC CORRECTION BLOCK label carries Protected behavior -- Axis B):**

A MISMATCH triggers an ARC CORRECTION BLOCK. Label form: ARC CORRECTION BLOCK -- PHASE N close -> PHASE N+1 open MISMATCH -- Protected behavior at boundary: [I-0X: named behavior from SECTION A for inertia active at that phase close]. Verdict updates to CORRECTED after repair.

| Transition | Exit state | Entry state | Verdict |
|---|---|---|---|
| PHASE 1 close -> PHASE 2 open | | | MATCH / MISMATCH / CORRECTED |
| PHASE 2 close -> PHASE 3 entry | | | MATCH / MISMATCH / CORRECTED |
| PHASE 3 close -> PHASE 4 open | | | MATCH / MISMATCH / CORRECTED |
| PHASE 4 close -> PHASE 5 open | | | MATCH / MISMATCH / CORRECTED |
| PHASE 5 close -> PHASE 6 open | | | MATCH / MISMATCH / CORRECTED |

Arc integrity: [PASS if all MATCH or CORRECTED | FAIL naming unrepaired discontinuity]

ARC CORRECTION BLOCK location(s) and label(s): [cite location and full label text, or "none -- all MATCH"]

---

## V-03 -- Single Axis: Inertia Framing (SECTION K Arc Table Carries Protected Behavior Column)

**Variation axis:** Inertia framing -- the SECTION K DISPLACEMENT ARC INTEGRITY CHECK table gains a "Protected behavior at boundary: [I-0X + named behavior from SECTION A]" column per transition row. The Protected behavior for each row is sourced from the DOWNSTREAM CITATION CONTRACT row for the inertia ID active at that specific phase-close (I-01 at PHASE 1 close, I-02 at PHASE 2 close, I-03 at PHASE 3/4 close, I-04 at PHASE 5 close, I-05 at PHASE 6 close). SECTION K becomes self-sufficient at the displacement-stake level for arc verification: an auditor reading only SECTION K can determine both arc consistency and what displacement commitment was at risk at each transition, without navigating to SECTION A.

**Hypothesis:** C-51/C-56 make SECTION K self-sufficient as a citation compliance certificate -- an auditor can determine coverage status and Protected behavior stakes from SECTION K alone. C-53/C-57 make SECTION K self-sufficient as an arc integrity record -- an auditor can determine whether phases chain consistently and whether any discontinuity was repaired. But the arc table currently names the transition pairs and exit/entry states without naming what displacement was at stake at each boundary. An auditor reading the PHASE 3 -> PHASE 4 row must cross-reference SECTION A to know that I-03 Protected behavior was active at that boundary. The Protected behavior column closes this: the arc table is self-sufficient at the displacement-stake level, matching the C-56 standard for the citation compliance record. A reviewer reading only SECTION K can answer not just 'was the arc consistent?' but 'what displacement stake was at risk at each transition?' -- without SECTION A cross-reference.

---

Simulate the adoption curve for {{topic}} across the 16 stock roles (PM, UX, C-01 through C-12, Support, SRE). Produce the artifact below in full. Every bracketed instruction is a fill contract -- complete it before proceeding to the next section.

---

## STRUCTURAL CONTRACT

This document encodes two mandatory co-present architectural requirements. No variation or omission of either is permitted.

**REQUIREMENT 1 -- ANSWER-FORM CITATION ENFORCEMENT (C-29):**
Named Inertia ID citations throughout this document are answers to explicit answer-form questions embedded in structural positions. The following questions are mandatory:

  Q-BARRIER:       Which Named Inertia ID is the primary barrier here? (Cite I-0X from SECTION A)
  Q-CHAMPION:      Named Inertia ID this champion is positioned to overcome: (Cite I-0X from SECTION A)
  Q-TRIGGER:       Which Named Inertia ID drives reversion risk for this role? (Cite I-0X from SECTION A)
  Q-INTERVENTION:  Which Named Inertia ID does this intervention directly target? (Cite I-0X from SECTION A)

**REQUIREMENT 2 -- CORRECTION BLOCK MECHANISM STATE (C-32, C-34):**
MECHANISM STATE inside each of SECTIONS H, I, J AND before VERIFICATION MODE. Gate H CORRECTION BLOCK labels carry Protected behavior (C-55 baseline). SECTION K CITATION CONTRACT COMPLETION RECORD carries Protected behavior column (C-56 baseline). Arc MISMATCH triggers ARC CORRECTION BLOCK (C-57 baseline). SECTION K DISPLACEMENT ARC INTEGRITY CHECK table carries Protected behavior at boundary column (Axis C).

Both requirements mandatory co-present.

---

## SECTION A -- Named Inertia IDs

| Inertia ID | Archetype      | Named Inertia | Structural reason |
|------------|----------------|---------------|-------------------|
| I-01       | Innovator      | [name]        | [reason]          |
| I-02       | Early Adopter  | [name]        | [reason]          |
| I-03       | Early Majority | [name]        | [reason]          |
| I-04       | Late Majority  | [name]        | [reason]          |
| I-05       | Laggard        | [name]        | [reason]          |

### SECTION A -- DOWNSTREAM CITATION CONTRACT

Protected behavior filled at generation time. Gate H fills Gate H Status. Gate H CORRECTION BLOCK labels carry I-0X + Protected behavior (C-55). SECTION K carries Protected behavior column in CITATION CONTRACT COMPLETION RECORD (C-56). SECTION K DISPLACEMENT ARC INTEGRITY CHECK table carries Protected behavior at boundary column (Axis C).

| Inertia ID | Mandatory downstream citation locations | Protected behavior: [fill at generation time] | Gate H Status |
|------------|-----------------------------------------|-----------------------------------------------|---------------|
| I-01 | PHASE 1 Q-BARRIER / PHASE 1 ledger / PART 3 Q-TRIGGER Innovator | [fill] | [PASS / FAIL] |
| I-02 | PHASE 2 Q-BARRIER / PHASE 2 ledger / PART 3 Q-TRIGGER EA | [fill] | [PASS / FAIL] |
| I-03 | PHASE 3 Q-BARRIER / PHASE 3 ledger / CHASM-A / CHASM-B / PHASE 4 Q-BARRIER / PHASE 4 ledger / PART 5 | [fill] | [PASS / FAIL] |
| I-04 | PHASE 5 Q-BARRIER / PHASE 5 ledger / PART 3 Q-TRIGGER LM | [fill] | [PASS / FAIL] |
| I-05 | PHASE 6 Q-BARRIER / PHASE 6 ledger / PART 3 Q-TRIGGER Laggard | [fill] | [PASS / FAIL] |

---

THE INCUMBENT is [name the current workflow, tool, or practice being displaced by {{topic}}].

---

## TABLE 1 -- Role Archetype Map

TABLE 1 header contract: Each row prefixed SLOT-KEY: -- three co-present contracts per row.

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

## PHASE 1 INNOVATORS -- Month 1

Displacement state at phase entry: THE INCUMBENT is fully entrenched -- all Protected behavior declarations fully active.

Q-BARRIER: Which Named Inertia ID is the primary barrier even for Innovators?
(Cite I-01 from SECTION A -- what Protected behavior from contract row I-01 does this archetype most tightly hold?)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what THE INCUMBENT retains after Month 1]
Inertia ID this phase overcame (partially): [re-cite I-01]

---

## PHASE 2 EARLY ADOPTERS -- Month 2-3

Displacement state at phase entry: [re-cite verbatim PHASE 1 Incumbent position after this phase:]

Q-BARRIER: Which Named Inertia ID is the primary barrier for Early Adopters?
(Cite I-02 -- what Protected behavior from contract row I-02 resists these roles?)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what THE INCUMBENT still controls after Month 3]
Inertia ID this phase overcame (partially): [re-cite I-02]

---

## PHASE 3 CHASM -- Month 4 (Non-Adoption Crossing Event)

Displacement state entering PHASE 3: [re-cite verbatim PHASE 2 Incumbent position after this phase:]

PHASE 3 is not an adoption phase. No new archetype adopts in Month 4.

Q-BARRIER: Which Named Inertia ID is driving the chasm?
(Cite I-03 -- what Protected behavior from contract row I-03 makes the chasm structural?)

### CHASM-A -- Incumbent Defense

[Named incumbent defense mechanism]

### CHASM-B -- Bridge Condition

[Bridge condition as testable proposition]

### CHASM-C -- Early Crossing Signal

[First observable crossing signal]

**Phase-close displacement ledger:**
Inertia ID defending THE INCUMBENT at this boundary: [I-03 -- and its Protected behavior from SECTION A]

---

## PHASE 4 EARLY MAJORITY -- Month 5-7

Displacement state at phase entry: [re-cite verbatim PHASE 3 close + what THE INCUMBENT still controlled entering Month 5]

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Early Majority?
(Cite I-03 -- Protected behavior from contract row I-03 still active despite chasm crossing)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what THE INCUMBENT still controls after Month 7]
Inertia ID this phase overcame (partially): [re-cite I-03]

---

## PHASE 5 LATE MAJORITY -- Month 8-10

Displacement state at phase entry: [re-cite verbatim PHASE 4 Incumbent position after this phase:]

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Late Majority?
(Cite I-04 -- what Protected behavior from contract row I-04 holds these roles back?)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what THE INCUMBENT still controls after Month 10]
Inertia ID this phase overcame (partially): [re-cite I-04]

---

## PHASE 6 LAGGARDS -- Month 11-12

Displacement state at phase entry: [re-cite verbatim PHASE 5 Incumbent position after this phase:]

Q-BARRIER: Which Named Inertia ID keeps Laggards last?
(Cite I-05 -- what Protected behavior from contract row I-05 is the final holdout?)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [terminal displacement state]
Inertia ID this phase overcame: [re-cite I-05]

---

## TABLE 3 -- Spread Mechanisms

| Transition Pair (SLOT-KEY row) | Spread Mechanism: [named signal or artifact -- not generic word-of-mouth] | Month Range |
|---|---|---|
| SLOT-KEY: Innovator -> Early Adopter      | | |
| SLOT-KEY: Early Adopter -> Early Majority | | |
| SLOT-KEY: Early Majority -> Late Majority | | |
| SLOT-KEY: Late Majority -> Laggard        | | |

---

## PART 2 -- CHASM ANALYSIS (Full Expansion)

### CHASM-A EXPANSION -- Incumbent Defense (Full Diagnosis)

Named Inertia in effect: [re-cite I-03]
Incumbent position at this chasm element: [displacement state]

[Full diagnosis]

### CHASM-B EXPANSION -- Bridge Condition (Full Specification)

Named Inertia in effect: [re-cite I-03]
Incumbent position at this chasm element: [displacement state]

[Full specification]

### CHASM-C EXPANSION -- Crossing Signal (Full Identification)

Named Inertia in effect: [re-cite I-03]
Incumbent position at this chasm element: [displacement state]

[Full identification]

---

## PART 3 -- Churn Risk Register

| Role (SLOT-KEY typed slot) | Reversion trigger: [specific condition] | Retention intervention: [concrete action -- not surveillance flag] | Q-TRIGGER: Which Named Inertia ID drives reversion risk? (Cite I-0X) |
|------|-----|-----|-----|
| SLOT-KEY: [Role] -- churn entry | | | |

---

## PART 4 -- Champion Network

| Champion Role (SLOT-KEY typed slot) | Archetype | Archetype-bridge rationale: [why this archetype position makes an effective champion] | Q-CHAMPION: Named Inertia ID this champion overcomes (I-0X) | Why this champion displaces THE INCUMBENT |
|---|---|---|---|---|
| SLOT-KEY: [Role] -- champion entry | | | | |
| SLOT-KEY: [Role] -- champion entry | | | | |
| SLOT-KEY: [Role] -- champion entry | | | | |

---

## PART 5 -- Intervention Ranking

| Rank | Intervention | Adoption delta | Phase(s) affected | Role(s) affected | Incumbent Impact: [what THE INCUMBENT loses] | Targets inertia: [I-0X -- Q-INTERVENTION] |
|------|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |

---

## PART 6 -- Sensitivity Analysis

| Scenario      | Adoption outcome | Named lever | Direction of shift |
|---------------|------------------|-------------|-------------------|
| Fast Adoption |                  |             |                   |
| Slow Adoption |                  |             |                   |

---

## PART 7 -- Signal Readiness Table

| Signal name | Threshold | Interpretation |
|-------------|-----------|----------------|
|             |           |                |

---

> CORRECTION BLOCK MECHANISM ARMED -- no gate failure triggered. If Gate H fails, CORRECTION BLOCK above: CORRECTION BLOCK -- I-0X CITATION CONTRACT VIOLATION -- Protected behavior: [value from SECTION A] (C-55 baseline). If DISPLACEMENT ARC INTEGRITY CHECK finds MISMATCH, ARC CORRECTION BLOCK above (C-57 baseline). SECTION K CITATION CONTRACT COMPLETION RECORD carries Protected behavior column (C-56 baseline). SECTION K arc table carries Protected behavior at boundary column (Axis C).

## VERIFICATION MODE

All content generation complete. SECTIONS H, I, J, K are audit sections only.

---

## SECTION H -- Gate: C-13 Audit

**Audit against DOWNSTREAM CITATION CONTRACT:**

- I-01: PHASE 1 Q-BARRIER [Y/N] / ledger [Y/N] / PART 3 Q-TRIGGER Innovator [Y/N] -> Fill SECTION A row I-01
- I-02: PHASE 2 Q-BARRIER [Y/N] / ledger [Y/N] / PART 3 Q-TRIGGER EA [Y/N] -> Fill SECTION A row I-02
- I-03: PHASE 3 Q-BARRIER [Y/N] / ledger [Y/N] / CHASM-A [Y/N] / CHASM-B [Y/N] / PHASE 4 Q-BARRIER [Y/N] / PHASE 4 ledger [Y/N] / PART 5 [Y/N] -> Fill SECTION A row I-03
- I-04: PHASE 5 Q-BARRIER [Y/N] / ledger [Y/N] / PART 3 Q-TRIGGER LM [Y/N] -> Fill SECTION A row I-04
- I-05: PHASE 6 Q-BARRIER [Y/N] / ledger [Y/N] / PART 3 Q-TRIGGER Laggard [Y/N] -> Fill SECTION A row I-05

**C-13 four-location check:** Bridge [Y/N] / Intervention [Y/N] / Champion [Y/N] / Churn [Y/N]

**Gate H result:** [PASS / FAIL]

**Correction obligation (C-55 baseline):** Per-I-0X: CORRECTION BLOCK -- I-0X CITATION CONTRACT VIOLATION -- Protected behavior: [value from SECTION A].

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED -- Gate H [PASS: no correction | FAIL: per-I-0X CORRECTION BLOCK(s) above, each carrying I-0X and Protected behavior]

---

## SECTION I -- Gate: C-14 Audit

- SLOT-KEY champion 1 [name]: archetype-bridge [Y/N] / Q-CHAMPION I-0X [Y/N]
- SLOT-KEY champion 2 [name]: archetype-bridge [Y/N] / Q-CHAMPION I-0X [Y/N]
- SLOT-KEY champion 3 [name]: archetype-bridge [Y/N] / Q-CHAMPION I-0X [Y/N]

**Gate I result:** [PASS / FAIL]

**Revision obligation:** If FAIL, produce CORRECTION BLOCK before pre-verification declaration.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED -- Gate I [PASS: no correction | FAIL: CORRECTION BLOCK written above]

---

## SECTION J -- Gate: C-15 Audit

- [List each SLOT-KEY: churn entry and classification]

**Gate J result:** [PASS / FAIL]

**Revision obligation:** If FAIL, produce CORRECTION BLOCK before pre-verification declaration.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED -- Gate J [PASS: no correction | FAIL: CORRECTION BLOCK written above]

---

## SECTION K -- Terminal Audit Record

**Terminal Invariant:** For every Yes, a CORRECTION BLOCK with BEFORE and AFTER fields must exist at cited location. A Yes without a CORRECTION BLOCK, or a CORRECTION BLOCK without BEFORE field, falsifies this invariant. Gate H produces per-I-0X CORRECTION BLOCKS carrying Protected behavior (C-55). Arc MISMATCH repairs produce ARC CORRECTION BLOCKS (C-57); SECTION K records arc correction entries. SECTION K arc table carries Protected behavior at boundary (Axis C).

| Gate | Criterion | Initial result | Revision performed | CORRECTION BLOCK location | Final result |
|------|-----------|----------------|--------------------|--------------------------|--------------|
| H    | C-13      |                | Yes / No           |                          |              |
| I    | C-14      |                | Yes / No           |                          |              |
| J    | C-15      |                | Yes / No           |                          |              |

**CITATION CONTRACT COMPLETION RECORD (C-56 baseline):**

| Inertia ID | Required sinks satisfied | Structural location (or NOT FOUND) | Protected behavior: [carry from SECTION A] | Gate H Status |
|------------|--------------------------|------------------------------------|--------------------------------------------|---------------|
| I-01       |                          |                                    |                                            |               |
| I-02       |                          |                                    |                                            |               |
| I-03       |                          |                                    |                                            |               |
| I-04       |                          |                                    |                                            |               |
| I-05       |                          |                                    |                                            |               |

**DISPLACEMENT ARC INTEGRITY CHECK (Protected behavior at boundary column -- Axis C):**

For each phase-transition pair, record exit-state and entry-state texts. A MISMATCH triggers an ARC CORRECTION BLOCK (C-57 baseline). The Protected behavior at boundary column names the I-0X and Protected behavior from SECTION A active at that phase-close, making the arc record self-sufficient at the displacement-stake level without SECTION A cross-reference.

| Transition | Exit state | Entry state | Protected behavior at boundary: [I-0X + named behavior from SECTION A] | Verdict |
|---|---|---|---|---|
| PHASE 1 close -> PHASE 2 open | | | [I-01: Protected behavior] | MATCH / MISMATCH / CORRECTED |
| PHASE 2 close -> PHASE 3 entry | | | [I-02: Protected behavior] | MATCH / MISMATCH / CORRECTED |
| PHASE 3 close -> PHASE 4 open | | | [I-03: Protected behavior] | MATCH / MISMATCH / CORRECTED |
| PHASE 4 close -> PHASE 5 open | | | [I-03: Protected behavior] | MATCH / MISMATCH / CORRECTED |
| PHASE 5 close -> PHASE 6 open | | | [I-04: Protected behavior] | MATCH / MISMATCH / CORRECTED |

Arc integrity: [PASS if all MATCH or CORRECTED | FAIL naming unrepaired discontinuity]

ARC CORRECTION BLOCK location(s): [cite location, or "none -- all MATCH"]

---

## V-04 -- Combined: Lifecycle Emphasis + Output Format (Axes A + B)

**Variation axis:** V-01 + V-02 combined. Phase entry states carry Protected behavior census (Axis A). ARC CORRECTION BLOCK labels carry Protected behavior at boundary (Axis B). Axes A and B are complementary: A makes the displacement inventory explicit at every phase entry, surfacing which Protected behaviors remain active before the phase body is written; B makes every arc repair self-describing at the displacement-stake level, carrying the same information granularity as Gate H CORRECTION BLOCK labels (C-55).

**Hypothesis:** Without Axes A+B: phase entries re-cite close ledger text (chain continuity only) and ARC CORRECTION BLOCK labels name the boundary without displacement stakes. With Axis A alone: the census is present at phase entry but arc repair labels are anonymous at the stake level. With Axis B alone: arc repair labels carry Protected behavior but there is no per-phase entry census of active behaviors. With both: the displacement inventory is visible at every phase entry (Axis A) and every arc repair carries the same inventory information at the boundary level (Axis B) -- two structural positions where displacement stakes are explicitly named without SECTION A cross-reference.

---

Simulate the adoption curve for {{topic}} across the 16 stock roles (PM, UX, C-01 through C-12, Support, SRE). Produce the artifact below in full. Every bracketed instruction is a fill contract -- complete it before proceeding to the next section.

---

## STRUCTURAL CONTRACT

This document encodes two mandatory co-present architectural requirements. No variation or omission of either is permitted.

**REQUIREMENT 1 -- ANSWER-FORM CITATION ENFORCEMENT (C-29):**
Named Inertia ID citations throughout this document are answers to explicit answer-form questions embedded in structural positions. The following questions are mandatory:

  Q-BARRIER:       Which Named Inertia ID is the primary barrier here? (Cite I-0X from SECTION A)
  Q-CHAMPION:      Named Inertia ID this champion is positioned to overcome: (Cite I-0X from SECTION A)
  Q-TRIGGER:       Which Named Inertia ID drives reversion risk for this role? (Cite I-0X from SECTION A)
  Q-INTERVENTION:  Which Named Inertia ID does this intervention directly target? (Cite I-0X from SECTION A)

**REQUIREMENT 2 -- CORRECTION BLOCK MECHANISM STATE (C-32, C-34):**
MECHANISM STATE inside each of SECTIONS H, I, J AND before VERIFICATION MODE. Gate H CORRECTION BLOCK labels carry Protected behavior (C-55 baseline). SECTION K CITATION CONTRACT COMPLETION RECORD carries Protected behavior column (C-56 baseline). Arc MISMATCH triggers ARC CORRECTION BLOCK (C-57 baseline). Phase entry states carry Protected behavior census (Axis A). ARC CORRECTION BLOCK labels carry Protected behavior at boundary (Axis B).

Both requirements mandatory co-present.

---

## SECTION A -- Named Inertia IDs

| Inertia ID | Archetype      | Named Inertia | Structural reason |
|------------|----------------|---------------|-------------------|
| I-01       | Innovator      | [name]        | [reason]          |
| I-02       | Early Adopter  | [name]        | [reason]          |
| I-03       | Early Majority | [name]        | [reason]          |
| I-04       | Late Majority  | [name]        | [reason]          |
| I-05       | Laggard        | [name]        | [reason]          |

### SECTION A -- DOWNSTREAM CITATION CONTRACT

Protected behavior filled at generation time. Gate H fills Gate H Status. Gate H CORRECTION BLOCK labels carry I-0X + Protected behavior (C-55). ARC CORRECTION BLOCK labels carry I-0X + Protected behavior at boundary (Axis B). SECTION K carries Protected behavior column (C-56). Phase entry states carry Protected behavior census (Axis A).

| Inertia ID | Mandatory downstream citation locations | Protected behavior: [fill at generation time] | Gate H Status |
|------------|-----------------------------------------|-----------------------------------------------|---------------|
| I-01 | PHASE 1 Q-BARRIER / PHASE 1 ledger / PART 3 Q-TRIGGER Innovator | [fill] | [PASS / FAIL] |
| I-02 | PHASE 2 Q-BARRIER / PHASE 2 ledger / PART 3 Q-TRIGGER EA | [fill] | [PASS / FAIL] |
| I-03 | PHASE 3 Q-BARRIER / PHASE 3 ledger / CHASM-A / CHASM-B / PHASE 4 Q-BARRIER / PHASE 4 ledger / PART 5 | [fill] | [PASS / FAIL] |
| I-04 | PHASE 5 Q-BARRIER / PHASE 5 ledger / PART 3 Q-TRIGGER LM | [fill] | [PASS / FAIL] |
| I-05 | PHASE 6 Q-BARRIER / PHASE 6 ledger / PART 3 Q-TRIGGER Laggard | [fill] | [PASS / FAIL] |

---

THE INCUMBENT is [name the current workflow, tool, or practice being displaced by {{topic}}].

---

## TABLE 1 -- Role Archetype Map

TABLE 1 header contract: Each row prefixed SLOT-KEY: -- three co-present contracts per row.

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

## PHASE 1 INNOVATORS -- Month 1

Displacement state at phase entry: THE INCUMBENT is fully entrenched -- all Protected behavior declarations fully active.

Protected behaviors still active at entry: I-01 ([Protected behavior name]) / I-02 ([Protected behavior name]) / I-03 ([Protected behavior name]) / I-04 ([Protected behavior name]) / I-05 ([Protected behavior name])
Displaced since document open: none

Q-BARRIER: Which Named Inertia ID is the primary barrier even for Innovators?
(Cite I-01 from SECTION A -- what Protected behavior from contract row I-01 does this archetype most tightly hold?)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what THE INCUMBENT retains after Month 1]
Inertia ID this phase overcame (partially): [re-cite I-01]

---

## PHASE 2 EARLY ADOPTERS -- Month 2-3

Displacement state at phase entry: [re-cite verbatim PHASE 1 Incumbent position after this phase:]

Protected behaviors still active at entry: [enumerate I-0X IDs not yet fully displaced; update from PHASE 1 close]
Displaced since document open: [enumerate I-0X IDs partially overcome in PHASE 1, or "none"]

Q-BARRIER: Which Named Inertia ID is the primary barrier for Early Adopters?
(Cite I-02 -- what Protected behavior from contract row I-02 resists these roles?)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what THE INCUMBENT still controls after Month 3]
Inertia ID this phase overcame (partially): [re-cite I-02]

---

## PHASE 3 CHASM -- Month 4 (Non-Adoption Crossing Event)

Displacement state entering PHASE 3: [re-cite verbatim PHASE 2 Incumbent position after this phase:]

Protected behaviors still active at entry: [enumerate I-0X IDs not yet displaced; I-03 through I-05 fully active]
Displaced since document open: [enumerate I-0X IDs partially overcome in PHASES 1-2]

PHASE 3 is not an adoption phase. No new archetype adopts in Month 4.

Q-BARRIER: Which Named Inertia ID is driving the chasm?
(Cite I-03 -- what Protected behavior from contract row I-03 makes the chasm structural?)

### CHASM-A -- Incumbent Defense

[Named incumbent defense mechanism]

### CHASM-B -- Bridge Condition

[Bridge condition as testable proposition]

### CHASM-C -- Early Crossing Signal

[First observable crossing signal]

**Phase-close displacement ledger:**
Inertia ID defending THE INCUMBENT at this boundary: [I-03 -- and its Protected behavior from SECTION A]

---

## PHASE 4 EARLY MAJORITY -- Month 5-7

Displacement state at phase entry: [re-cite verbatim PHASE 3 close + what THE INCUMBENT still controlled entering Month 5]

Protected behaviors still active at entry: [I-03 still active despite chasm; I-04, I-05 fully active; I-01, I-02 may be partially displaced]
Displaced since document open: [enumerate I-0X IDs partially overcome in PHASES 1-3]

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Early Majority?
(Cite I-03 -- Protected behavior from contract row I-03 still active despite chasm crossing)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what THE INCUMBENT still controls after Month 7]
Inertia ID this phase overcame (partially): [re-cite I-03]

---

## PHASE 5 LATE MAJORITY -- Month 8-10

Displacement state at phase entry: [re-cite verbatim PHASE 4 Incumbent position after this phase:]

Protected behaviors still active at entry: [I-04 and I-05 remain active; I-03 partially overcome]
Displaced since document open: [enumerate I-0X IDs partially or fully overcome in PHASES 1-4]

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Late Majority?
(Cite I-04 -- what Protected behavior from contract row I-04 holds these roles back?)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what THE INCUMBENT still controls after Month 10]
Inertia ID this phase overcame (partially): [re-cite I-04]

---

## PHASE 6 LAGGARDS -- Month 11-12

Displacement state at phase entry: [re-cite verbatim PHASE 5 Incumbent position after this phase:]

Protected behaviors still active at entry: [I-05 remains; others may persist partially]
Displaced since document open: [enumerate I-0X IDs overcome in PHASES 1-5]

Q-BARRIER: Which Named Inertia ID keeps Laggards last?
(Cite I-05 -- what Protected behavior from contract row I-05 is the final holdout?)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [terminal displacement state]
Inertia ID this phase overcame: [re-cite I-05]

---

## TABLE 3 -- Spread Mechanisms

| Transition Pair (SLOT-KEY row) | Spread Mechanism: [named signal or artifact -- not generic word-of-mouth] | Month Range |
|---|---|---|
| SLOT-KEY: Innovator -> Early Adopter      | | |
| SLOT-KEY: Early Adopter -> Early Majority | | |
| SLOT-KEY: Early Majority -> Late Majority | | |
| SLOT-KEY: Late Majority -> Laggard        | | |

---

## PART 2 -- CHASM ANALYSIS (Full Expansion)

### CHASM-A EXPANSION -- Incumbent Defense (Full Diagnosis)

Named Inertia in effect: [re-cite I-03]
Incumbent position at this chasm element: [displacement state]

[Full diagnosis]

### CHASM-B EXPANSION -- Bridge Condition (Full Specification)

Named Inertia in effect: [re-cite I-03]
Incumbent position at this chasm element: [displacement state]

[Full specification]

### CHASM-C EXPANSION -- Crossing Signal (Full Identification)

Named Inertia in effect: [re-cite I-03]
Incumbent position at this chasm element: [displacement state]

[Full identification]

---

## PART 3 -- Churn Risk Register

| Role (SLOT-KEY typed slot) | Reversion trigger: [specific condition] | Retention intervention: [concrete action -- not surveillance flag] | Q-TRIGGER: Which Named Inertia ID drives reversion risk? (Cite I-0X) |
|------|-----|-----|-----|
| SLOT-KEY: [Role] -- churn entry | | | |

---

## PART 4 -- Champion Network

| Champion Role (SLOT-KEY typed slot) | Archetype | Archetype-bridge rationale: [why this archetype position makes an effective champion] | Q-CHAMPION: Named Inertia ID this champion overcomes (I-0X) | Why this champion displaces THE INCUMBENT |
|---|---|---|---|---|
| SLOT-KEY: [Role] -- champion entry | | | | |
| SLOT-KEY: [Role] -- champion entry | | | | |
| SLOT-KEY: [Role] -- champion entry | | | | |

---

## PART 5 -- Intervention Ranking

| Rank | Intervention | Adoption delta | Phase(s) affected | Role(s) affected | Incumbent Impact: [what THE INCUMBENT loses] | Targets inertia: [I-0X -- Q-INTERVENTION] |
|------|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |

---

## PART 6 -- Sensitivity Analysis

| Scenario      | Adoption outcome | Named lever | Direction of shift |
|---------------|------------------|-------------|-------------------|
| Fast Adoption |                  |             |                   |
| Slow Adoption |                  |             |                   |

---

## PART 7 -- Signal Readiness Table

| Signal name | Threshold | Interpretation |
|-------------|-----------|----------------|
|             |           |                |

---

> CORRECTION BLOCK MECHANISM ARMED -- no gate failure triggered. If Gate H fails, CORRECTION BLOCK above: CORRECTION BLOCK -- I-0X CITATION CONTRACT VIOLATION -- Protected behavior: [value from SECTION A] (C-55 baseline). If DISPLACEMENT ARC INTEGRITY CHECK finds MISMATCH, ARC CORRECTION BLOCK above: ARC CORRECTION BLOCK -- PHASE N close -> PHASE N+1 open MISMATCH -- Protected behavior at boundary: [I-0X: value from SECTION A for inertia at that phase close] (Axis B). SECTION K carries Protected behavior column (C-56 baseline).

## VERIFICATION MODE

All content generation complete. SECTIONS H, I, J, K are audit sections only.

---

## SECTION H -- Gate: C-13 Audit

**Audit against DOWNSTREAM CITATION CONTRACT:**

- I-01: PHASE 1 Q-BARRIER [Y/N] / ledger [Y/N] / PART 3 Q-TRIGGER Innovator [Y/N] -> Fill SECTION A row I-01
- I-02: PHASE 2 Q-BARRIER [Y/N] / ledger [Y/N] / PART 3 Q-TRIGGER EA [Y/N] -> Fill SECTION A row I-02
- I-03: PHASE 3 Q-BARRIER [Y/N] / ledger [Y/N] / CHASM-A [Y/N] / CHASM-B [Y/N] / PHASE 4 Q-BARRIER [Y/N] / PHASE 4 ledger [Y/N] / PART 5 [Y/N] -> Fill SECTION A row I-03
- I-04: PHASE 5 Q-BARRIER [Y/N] / ledger [Y/N] / PART 3 Q-TRIGGER LM [Y/N] -> Fill SECTION A row I-04
- I-05: PHASE 6 Q-BARRIER [Y/N] / ledger [Y/N] / PART 3 Q-TRIGGER Laggard [Y/N] -> Fill SECTION A row I-05

**C-13 four-location check:** Bridge [Y/N] / Intervention [Y/N] / Champion [Y/N] / Churn [Y/N]

**Gate H result:** [PASS / FAIL]

**Correction obligation (C-55 baseline):** Per-I-0X: CORRECTION BLOCK -- I-0X CITATION CONTRACT VIOLATION -- Protected behavior: [value from SECTION A].

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED -- Gate H [PASS: no correction | FAIL: per-I-0X CORRECTION BLOCK(s) above, each carrying I-0X and Protected behavior]

---

## SECTION I -- Gate: C-14 Audit

- SLOT-KEY champion 1 [name]: archetype-bridge [Y/N] / Q-CHAMPION I-0X [Y/N]
- SLOT-KEY champion 2 [name]: archetype-bridge [Y/N] / Q-CHAMPION I-0X [Y/N]
- SLOT-KEY champion 3 [name]: archetype-bridge [Y/N] / Q-CHAMPION I-0X [Y/N]

**Gate I result:** [PASS / FAIL]

**Revision obligation:** If FAIL, produce CORRECTION BLOCK before pre-verification declaration.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED -- Gate I [PASS: no correction | FAIL: CORRECTION BLOCK written above]

---

## SECTION J -- Gate: C-15 Audit

- [List each SLOT-KEY: churn entry and classification]

**Gate J result:** [PASS / FAIL]

**Revision obligation:** If FAIL, produce CORRECTION BLOCK before pre-verification declaration.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED -- Gate J [PASS: no correction | FAIL: CORRECTION BLOCK written above]

---

## SECTION K -- Terminal Audit Record

**Terminal Invariant:** For every Yes, a CORRECTION BLOCK with BEFORE and AFTER fields must exist at cited location. A Yes without a CORRECTION BLOCK, or a CORRECTION BLOCK without BEFORE field, falsifies this invariant. Gate H produces per-I-0X CORRECTION BLOCKS carrying Protected behavior (C-55). Arc MISMATCH repairs produce ARC CORRECTION BLOCKS carrying Protected behavior at boundary (Axis B); SECTION K records their labels.

| Gate | Criterion | Initial result | Revision performed | CORRECTION BLOCK location | Final result |
|------|-----------|----------------|--------------------|--------------------------|--------------|
| H    | C-13      |                | Yes / No           |                          |              |
| I    | C-14      |                | Yes / No           |                          |              |
| J    | C-15      |                | Yes / No           |                          |              |

**CITATION CONTRACT COMPLETION RECORD (C-56 baseline):**

| Inertia ID | Required sinks satisfied | Structural location (or NOT FOUND) | Protected behavior: [carry from SECTION A] | Gate H Status |
|------------|--------------------------|------------------------------------|--------------------------------------------|---------------|
| I-01       |                          |                                    |                                            |               |
| I-02       |                          |                                    |                                            |               |
| I-03       |                          |                                    |                                            |               |
| I-04       |                          |                                    |                                            |               |
| I-05       |                          |                                    |                                            |               |

**DISPLACEMENT ARC INTEGRITY CHECK (ARC CORRECTION BLOCK label carries Protected behavior -- Axis B):**

A MISMATCH triggers an ARC CORRECTION BLOCK. Label: ARC CORRECTION BLOCK -- PHASE N close -> PHASE N+1 open MISMATCH -- Protected behavior at boundary: [I-0X: named behavior from SECTION A for inertia at that phase close]. Verdict updates to CORRECTED.

| Transition | Exit state | Entry state | Verdict |
|---|---|---|---|
| PHASE 1 close -> PHASE 2 open | | | MATCH / MISMATCH / CORRECTED |
| PHASE 2 close -> PHASE 3 entry | | | MATCH / MISMATCH / CORRECTED |
| PHASE 3 close -> PHASE 4 open | | | MATCH / MISMATCH / CORRECTED |
| PHASE 4 close -> PHASE 5 open | | | MATCH / MISMATCH / CORRECTED |
| PHASE 5 close -> PHASE 6 open | | | MATCH / MISMATCH / CORRECTED |

Arc integrity: [PASS if all MATCH or CORRECTED | FAIL naming unrepaired discontinuity]

ARC CORRECTION BLOCK location(s) and label(s): [cite location and full label text, or "none -- all MATCH"]

---

## V-05 -- Full Combination: Lifecycle Emphasis + Output Format + Inertia Framing (Axes A + B + C)

**Variation axis:** All three axes combined. (A) Phase entry states carry Protected behavior census -- enumeration of all I-0X Protected behaviors active vs. displaced at each phase entry. (B) ARC CORRECTION BLOCK labels carry Protected behavior of the inertia active at the phase-close boundary. (C) SECTION K DISPLACEMENT ARC INTEGRITY CHECK table carries Protected behavior at boundary column per transition row. The three axes form a complete Protected behavior propagation chain across the displacement narrative: declared at generation (C-54) / carried into phase entry census (Axis A) / carried into arc repair labels if arc breaks (Axis B) / carried into terminal arc record regardless of arc outcome (Axis C).

**Hypothesis:** Without the three axes: Protected behavior lives in SECTION A (C-54) and SECTION K citation record (C-56). Phase entries re-cite close ledger text. Arc repair labels name the boundary. Terminal arc table names transitions. With all three: at every structural position where displacement progress matters -- phase entry (Axis A), arc repair (Axis B), terminal arc verification (Axis C) -- the Protected behaviors are explicitly present. A reader of a V-05 artifact can track displacement progress per behavior at phase entry, understand what displacement stake was interrupted by any arc discontinuity from the repair label, and verify displacement stakes at every arc transition from SECTION K alone. This is the maximum Protected behavior propagation density the current rubric architecture supports across the displacement narrative chain.

---

Simulate the adoption curve for {{topic}} across the 16 stock roles (PM, UX, C-01 through C-12, Support, SRE). Produce the artifact below in full. Every bracketed instruction is a fill contract -- complete it before proceeding to the next section.

---

## STRUCTURAL CONTRACT

This document encodes two mandatory co-present architectural requirements. No variation or omission of either is permitted.

**REQUIREMENT 1 -- ANSWER-FORM CITATION ENFORCEMENT (C-29):**
Named Inertia ID citations throughout this document are answers to explicit answer-form questions embedded in structural positions. The following questions are mandatory:

  Q-BARRIER:       Which Named Inertia ID is the primary barrier here? (Cite I-0X from SECTION A)
  Q-CHAMPION:      Named Inertia ID this champion is positioned to overcome: (Cite I-0X from SECTION A)
  Q-TRIGGER:       Which Named Inertia ID drives reversion risk for this role? (Cite I-0X from SECTION A)
  Q-INTERVENTION:  Which Named Inertia ID does this intervention directly target? (Cite I-0X from SECTION A)

**REQUIREMENT 2 -- CORRECTION BLOCK MECHANISM STATE (C-32, C-34):**
MECHANISM STATE inside each of SECTIONS H, I, J AND before VERIFICATION MODE. Gate H CORRECTION BLOCK labels carry Protected behavior (C-55 baseline). SECTION K CITATION CONTRACT COMPLETION RECORD carries Protected behavior column (C-56 baseline). Arc MISMATCH triggers ARC CORRECTION BLOCK (C-57 baseline). Phase entry states carry Protected behavior census (Axis A). ARC CORRECTION BLOCK labels carry Protected behavior at boundary (Axis B). SECTION K arc integrity table carries Protected behavior at boundary column (Axis C).

Both requirements mandatory co-present.

---

## SECTION A -- Named Inertia IDs

| Inertia ID | Archetype      | Named Inertia | Structural reason |
|------------|----------------|---------------|-------------------|
| I-01       | Innovator      | [name]        | [reason]          |
| I-02       | Early Adopter  | [name]        | [reason]          |
| I-03       | Early Majority | [name]        | [reason]          |
| I-04       | Late Majority  | [name]        | [reason]          |
| I-05       | Laggard        | [name]        | [reason]          |

### SECTION A -- DOWNSTREAM CITATION CONTRACT

Protected behavior filled at generation time. Gate H fills Gate H Status. Gate H CORRECTION BLOCK labels carry I-0X + Protected behavior (C-55). ARC CORRECTION BLOCK labels carry I-0X + Protected behavior at boundary (Axis B). SECTION K CITATION CONTRACT COMPLETION RECORD carries Protected behavior column (C-56). SECTION K arc integrity table carries Protected behavior at boundary column (Axis C). Phase entry states carry Protected behavior census (Axis A).

| Inertia ID | Mandatory downstream citation locations | Protected behavior: [fill at generation time] | Gate H Status |
|------------|-----------------------------------------|-----------------------------------------------|---------------|
| I-01 | PHASE 1 Q-BARRIER / PHASE 1 ledger / PART 3 Q-TRIGGER Innovator | [fill] | [PASS / FAIL] |
| I-02 | PHASE 2 Q-BARRIER / PHASE 2 ledger / PART 3 Q-TRIGGER EA | [fill] | [PASS / FAIL] |
| I-03 | PHASE 3 Q-BARRIER / PHASE 3 ledger / CHASM-A / CHASM-B / PHASE 4 Q-BARRIER / PHASE 4 ledger / PART 5 | [fill] | [PASS / FAIL] |
| I-04 | PHASE 5 Q-BARRIER / PHASE 5 ledger / PART 3 Q-TRIGGER LM | [fill] | [PASS / FAIL] |
| I-05 | PHASE 6 Q-BARRIER / PHASE 6 ledger / PART 3 Q-TRIGGER Laggard | [fill] | [PASS / FAIL] |

---

THE INCUMBENT is [name the current workflow, tool, or practice being displaced by {{topic}}].

---

## TABLE 1 -- Role Archetype Map

TABLE 1 header contract: Each row prefixed SLOT-KEY: -- three co-present contracts per row.

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

## PHASE 1 INNOVATORS -- Month 1

Displacement state at phase entry: THE INCUMBENT is fully entrenched -- all Protected behavior declarations fully active.

Protected behaviors still active at entry: I-01 ([Protected behavior name]) / I-02 ([Protected behavior name]) / I-03 ([Protected behavior name]) / I-04 ([Protected behavior name]) / I-05 ([Protected behavior name])
Displaced since document open: none

Q-BARRIER: Which Named Inertia ID is the primary barrier even for Innovators?
(Cite I-01 from SECTION A -- what Protected behavior from contract row I-01 does this archetype most tightly hold?)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what THE INCUMBENT retains after Month 1]
Inertia ID this phase overcame (partially): [re-cite I-01]

---

## PHASE 2 EARLY ADOPTERS -- Month 2-3

Displacement state at phase entry: [re-cite verbatim PHASE 1 Incumbent position after this phase:]

Protected behaviors still active at entry: [enumerate I-0X IDs not yet fully displaced; update from PHASE 1 close]
Displaced since document open: [enumerate I-0X IDs partially overcome in PHASE 1, or "none"]

Q-BARRIER: Which Named Inertia ID is the primary barrier for Early Adopters?
(Cite I-02 -- what Protected behavior from contract row I-02 resists these roles?)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what THE INCUMBENT still controls after Month 3]
Inertia ID this phase overcame (partially): [re-cite I-02]

---

## PHASE 3 CHASM -- Month 4 (Non-Adoption Crossing Event)

Displacement state entering PHASE 3: [re-cite verbatim PHASE 2 Incumbent position after this phase:]

Protected behaviors still active at entry: [enumerate I-0X IDs not yet displaced; I-03 through I-05 fully active]
Displaced since document open: [enumerate I-0X IDs partially overcome in PHASES 1-2]

PHASE 3 is not an adoption phase. No new archetype adopts in Month 4.

Q-BARRIER: Which Named Inertia ID is driving the chasm?
(Cite I-03 -- what Protected behavior from contract row I-03 makes the chasm structural?)

### CHASM-A -- Incumbent Defense

[Named incumbent defense mechanism]

### CHASM-B -- Bridge Condition

[Bridge condition as testable proposition]

### CHASM-C -- Early Crossing Signal

[First observable crossing signal]

**Phase-close displacement ledger:**
Inertia ID defending THE INCUMBENT at this boundary: [I-03 -- and its Protected behavior from SECTION A]

---

## PHASE 4 EARLY MAJORITY -- Month 5-7

Displacement state at phase entry: [re-cite verbatim PHASE 3 close + what THE INCUMBENT still controlled entering Month 5]

Protected behaviors still active at entry: [I-03 still active despite chasm; I-04, I-05 fully active; I-01, I-02 may be partially displaced]
Displaced since document open: [enumerate I-0X IDs partially overcome in PHASES 1-3]

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Early Majority?
(Cite I-03 -- Protected behavior from contract row I-03 still active despite chasm crossing)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what THE INCUMBENT still controls after Month 7]
Inertia ID this phase overcame (partially): [re-cite I-03]

---

## PHASE 5 LATE MAJORITY -- Month 8-10

Displacement state at phase entry: [re-cite verbatim PHASE 4 Incumbent position after this phase:]

Protected behaviors still active at entry: [I-04 and I-05 remain active; I-03 partially overcome]
Displaced since document open: [enumerate I-0X IDs partially or fully overcome in PHASES 1-4]

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Late Majority?
(Cite I-04 -- what Protected behavior from contract row I-04 holds these roles back?)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [what THE INCUMBENT still controls after Month 10]
Inertia ID this phase overcame (partially): [re-cite I-04]

---

## PHASE 6 LAGGARDS -- Month 11-12

Displacement state at phase entry: [re-cite verbatim PHASE 5 Incumbent position after this phase:]

Protected behaviors still active at entry: [I-05 remains; others may persist partially]
Displaced since document open: [enumerate I-0X IDs overcome in PHASES 1-5]

Q-BARRIER: Which Named Inertia ID keeps Laggards last?
(Cite I-05 -- what Protected behavior from contract row I-05 is the final holdout?)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [terminal displacement state]
Inertia ID this phase overcame: [re-cite I-05]

---

## TABLE 3 -- Spread Mechanisms

| Transition Pair (SLOT-KEY row) | Spread Mechanism: [named signal or artifact -- not generic word-of-mouth] | Month Range |
|---|---|---|
| SLOT-KEY: Innovator -> Early Adopter      | | |
| SLOT-KEY: Early Adopter -> Early Majority | | |
| SLOT-KEY: Early Majority -> Late Majority | | |
| SLOT-KEY: Late Majority -> Laggard        | | |

---

## PART 2 -- CHASM ANALYSIS (Full Expansion)

### CHASM-A EXPANSION -- Incumbent Defense (Full Diagnosis)

Named Inertia in effect: [re-cite I-03]
Incumbent position at this chasm element: [displacement state]

[Full diagnosis]

### CHASM-B EXPANSION -- Bridge Condition (Full Specification)

Named Inertia in effect: [re-cite I-03]
Incumbent position at this chasm element: [displacement state]

[Full specification]

### CHASM-C EXPANSION -- Crossing Signal (Full Identification)

Named Inertia in effect: [re-cite I-03]
Incumbent position at this chasm element: [displacement state]

[Full identification]

---

## PART 3 -- Churn Risk Register

| Role (SLOT-KEY typed slot) | Reversion trigger: [specific condition] | Retention intervention: [concrete action -- not surveillance flag] | Q-TRIGGER: Which Named Inertia ID drives reversion risk? (Cite I-0X) |
|------|-----|-----|-----|
| SLOT-KEY: [Role] -- churn entry | | | |

---

## PART 4 -- Champion Network

| Champion Role (SLOT-KEY typed slot) | Archetype | Archetype-bridge rationale: [why this archetype position makes an effective champion] | Q-CHAMPION: Named Inertia ID this champion overcomes (I-0X) | Why this champion displaces THE INCUMBENT |
|---|---|---|---|---|
| SLOT-KEY: [Role] -- champion entry | | | | |
| SLOT-KEY: [Role] -- champion entry | | | | |
| SLOT-KEY: [Role] -- champion entry | | | | |

---

## PART 5 -- Intervention Ranking

| Rank | Intervention | Adoption delta | Phase(s) affected | Role(s) affected | Incumbent Impact: [what THE INCUMBENT loses] | Targets inertia: [I-0X -- Q-INTERVENTION] |
|------|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |

---

## PART 6 -- Sensitivity Analysis

| Scenario      | Adoption outcome | Named lever | Direction of shift |
|---------------|------------------|-------------|-------------------|
| Fast Adoption |                  |             |                   |
| Slow Adoption |                  |             |                   |

---

## PART 7 -- Signal Readiness Table

| Signal name | Threshold | Interpretation |
|-------------|-----------|----------------|
|             |           |                |

---

> CORRECTION BLOCK MECHANISM ARMED -- no gate failure triggered. If Gate H fails, CORRECTION BLOCK above: CORRECTION BLOCK -- I-0X CITATION CONTRACT VIOLATION -- Protected behavior: [value from SECTION A] (C-55 baseline). If DISPLACEMENT ARC INTEGRITY CHECK finds MISMATCH, ARC CORRECTION BLOCK above: ARC CORRECTION BLOCK -- PHASE N close -> PHASE N+1 open MISMATCH -- Protected behavior at boundary: [I-0X: value from SECTION A for inertia at that phase close] (Axis B). SECTION K CITATION CONTRACT COMPLETION RECORD carries Protected behavior column (C-56 baseline). SECTION K arc table carries Protected behavior at boundary column (Axis C).

## VERIFICATION MODE

All content generation complete. SECTIONS H, I, J, K are audit sections only.

---

## SECTION H -- Gate: C-13 Audit

**Audit against DOWNSTREAM CITATION CONTRACT:**

- I-01: PHASE 1 Q-BARRIER [Y/N] / ledger [Y/N] / PART 3 Q-TRIGGER Innovator [Y/N] -> Fill SECTION A row I-01
- I-02: PHASE 2 Q-BARRIER [Y/N] / ledger [Y/N] / PART 3 Q-TRIGGER EA [Y/N] -> Fill SECTION A row I-02
- I-03: PHASE 3 Q-BARRIER [Y/N] / ledger [Y/N] / CHASM-A [Y/N] / CHASM-B [Y/N] / PHASE 4 Q-BARRIER [Y/N] / PHASE 4 ledger [Y/N] / PART 5 [Y/N] -> Fill SECTION A row I-03
- I-04: PHASE 5 Q-BARRIER [Y/N] / ledger [Y/N] / PART 3 Q-TRIGGER LM [Y/N] -> Fill SECTION A row I-04
- I-05: PHASE 6 Q-BARRIER [Y/N] / ledger [Y/N] / PART 3 Q-TRIGGER Laggard [Y/N] -> Fill SECTION A row I-05

**C-13 four-location check:** Bridge [Y/N] / Intervention [Y/N] / Champion [Y/N] / Churn [Y/N]

**Gate H result:** [PASS / FAIL]

**Correction obligation (C-55 baseline):** Per-I-0X: CORRECTION BLOCK -- I-0X CITATION CONTRACT VIOLATION -- Protected behavior: [value from SECTION A].

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED -- Gate H [PASS: no correction | FAIL: per-I-0X CORRECTION BLOCK(s) above, each carrying I-0X and Protected behavior]

---

## SECTION I -- Gate: C-14 Audit

- SLOT-KEY champion 1 [name]: archetype-bridge [Y/N] / Q-CHAMPION I-0X [Y/N]
- SLOT-KEY champion 2 [name]: archetype-bridge [Y/N] / Q-CHAMPION I-0X [Y/N]
- SLOT-KEY champion 3 [name]: archetype-bridge [Y/N] / Q-CHAMPION I-0X [Y/N]

**Gate I result:** [PASS / FAIL]

**Revision obligation:** If FAIL, produce CORRECTION BLOCK before pre-verification declaration.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED -- Gate I [PASS: no correction | FAIL: CORRECTION BLOCK written above]

---

## SECTION J -- Gate: C-15 Audit

- [List each SLOT-KEY: churn entry and classification]

**Gate J result:** [PASS / FAIL]

**Revision obligation:** If FAIL, produce CORRECTION BLOCK before pre-verification declaration.

> MECHANISM STATE: CORRECTION BLOCK MECHANISM ARMED -- Gate J [PASS: no correction | FAIL: CORRECTION BLOCK written above]

---

## SECTION K -- Terminal Audit Record

**Terminal Invariant:** For every Yes, a CORRECTION BLOCK with BEFORE and AFTER fields must exist at cited location. A Yes without a CORRECTION BLOCK, or a CORRECTION BLOCK without BEFORE field, falsifies this invariant. Gate H produces per-I-0X CORRECTION BLOCKS carrying Protected behavior (C-55). Arc MISMATCH repairs produce ARC CORRECTION BLOCKS carrying Protected behavior at boundary (Axis B). SECTION K arc table carries Protected behavior at boundary column (Axis C).

| Gate | Criterion | Initial result | Revision performed | CORRECTION BLOCK location | Final result |
|------|-----------|----------------|--------------------|--------------------------|--------------|
| H    | C-13      |                | Yes / No           |                          |              |
| I    | C-14      |                | Yes / No           |                          |              |
| J    | C-15      |                | Yes / No           |                          |              |

**CITATION CONTRACT COMPLETION RECORD (C-56 baseline):**

| Inertia ID | Required sinks satisfied | Structural location (or NOT FOUND) | Protected behavior: [carry from SECTION A] | Gate H Status |
|------------|--------------------------|------------------------------------|--------------------------------------------|---------------|
| I-01       |                          |                                    |                                            |               |
| I-02       |                          |                                    |                                            |               |
| I-03       |                          |                                    |                                            |               |
| I-04       |                          |                                    |                                            |               |
| I-05       |                          |                                    |                                            |               |

**DISPLACEMENT ARC INTEGRITY CHECK (Protected behavior at boundary column + ARC CORRECTION BLOCK label -- Axes B + C):**

A MISMATCH triggers an ARC CORRECTION BLOCK. Label: ARC CORRECTION BLOCK -- PHASE N close -> PHASE N+1 open MISMATCH -- Protected behavior at boundary: [I-0X: named behavior from SECTION A for inertia at that phase close] (Axis B). The Protected behavior at boundary column (Axis C) names the displacement stake at every transition row regardless of verdict -- making the arc record self-sufficient at the displacement-stake level for an auditor who reads only SECTION K.

| Transition | Exit state | Entry state | Protected behavior at boundary: [I-0X + named behavior from SECTION A] | Verdict |
|---|---|---|---|---|
| PHASE 1 close -> PHASE 2 open | | | [I-01: Protected behavior] | MATCH / MISMATCH / CORRECTED |
| PHASE 2 close -> PHASE 3 entry | | | [I-02: Protected behavior] | MATCH / MISMATCH / CORRECTED |
| PHASE 3 close -> PHASE 4 open | | | [I-03: Protected behavior] | MATCH / MISMATCH / CORRECTED |
| PHASE 4 close -> PHASE 5 open | | | [I-03: Protected behavior] | MATCH / MISMATCH / CORRECTED |
| PHASE 5 close -> PHASE 6 open | | | [I-04: Protected behavior] | MATCH / MISMATCH / CORRECTED |

Arc integrity: [PASS if all MATCH or CORRECTED | FAIL naming unrepaired discontinuity]

ARC CORRECTION BLOCK location(s) and label(s): [cite location and full label text, or "none -- all MATCH"]

