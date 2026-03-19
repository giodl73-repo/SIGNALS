"""QU5 simplification pass: write listen-adoption simplified golden."""

body = r"""Simulate the adoption curve for {{topic}} across the 16 stock roles (PM, UX, C-01 through C-12, Support, SRE). Produce the artifact below in full. Every bracketed instruction is a fill contract -- complete it before proceeding to the next section.

---

## STRUCTURAL CONTRACT

**REQUIREMENT 1 -- ANSWER-FORM CITATION ENFORCEMENT (C-29):**
Mandatory answer-form questions -- each requires a Named Inertia ID (I-0X) as its coherent answer:

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

Protected behavior: fill at generation time. Gate H Status: fill at audit time.

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
(Cite I-01 -- what Protected behavior from row I-01 does this archetype most tightly hold?)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [residual incumbent control after Month 1]
Inertia ID overcome (partially): [I-01]

---

## PHASE 2 EARLY ADOPTERS -- Month 2-3

Displacement state at phase entry: [re-cite verbatim: PHASE 1 close ledger Incumbent position]

Protected behaviors still active at entry: [enumerate I-0X IDs not yet fully displaced; update from PHASE 1 close]
Displaced since document open: [enumerate I-0X IDs partially overcome in PHASE 1, or "none"]

Q-BARRIER: Which Named Inertia ID is the primary barrier for Early Adopters?
(Cite I-02 -- what Protected behavior from row I-02 resists these roles?)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [residual incumbent control after Month 3]
Inertia ID overcome (partially): [I-02]

---

## PHASE 3 CHASM -- Month 4 (Non-Adoption Crossing Event)

Displacement state entering PHASE 3: [re-cite verbatim: PHASE 2 close ledger Incumbent position]

Protected behaviors still active at entry: [enumerate I-0X IDs not yet displaced; I-03 through I-05 fully active]
Displaced since document open: [enumerate I-0X IDs partially overcome in PHASES 1-2]

PHASE 3 is not an adoption phase -- no archetype adopts in Month 4.

Q-BARRIER: Which Named Inertia ID is driving the chasm?
(Cite I-03 -- what Protected behavior from row I-03 makes the chasm structural?)

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

Displacement state at phase entry: [re-cite verbatim: PHASE 3 close ledger + what THE INCUMBENT still controlled entering Month 5]

Protected behaviors still active at entry: [I-03 still active despite chasm; I-04, I-05 fully active; I-01, I-02 may be partially displaced]
Displaced since document open: [enumerate I-0X IDs partially overcome in PHASES 1-3]

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Early Majority?
(Cite I-03 -- Protected behavior from row I-03 still active despite chasm crossing)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [residual incumbent control after Month 7]
Inertia ID overcome (partially): [I-03]

---

## PHASE 5 LATE MAJORITY -- Month 8-10

Displacement state at phase entry: [re-cite verbatim: PHASE 4 close ledger Incumbent position]

Protected behaviors still active at entry: [I-04 and I-05 remain active; I-03 partially overcome]
Displaced since document open: [enumerate I-0X IDs partially or fully overcome in PHASES 1-4]

Q-BARRIER: Which Named Inertia ID is the primary barrier for the Late Majority?
(Cite I-04 -- what Protected behavior from row I-04 holds these roles back?)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [residual incumbent control after Month 10]
Inertia ID overcome (partially): [I-04]

---

## PHASE 6 LAGGARDS -- Month 11-12

Displacement state at phase entry: [re-cite verbatim: PHASE 5 close ledger Incumbent position]

Protected behaviors still active at entry: [I-05 remains; others may persist partially]
Displaced since document open: [enumerate I-0X IDs overcome in PHASES 1-5]

Q-BARRIER: Which Named Inertia ID keeps Laggards last?
(Cite I-05 -- what Protected behavior from row I-05 is the final holdout?)

[Phase body]

**Phase-close displacement ledger:**
Incumbent position after this phase: [terminal displacement state]
Inertia ID overcome: [I-05]

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

### CHASM-A EXPANSION -- Incumbent Defense

Named Inertia in effect: [re-cite I-03]
Incumbent position at this chasm element: [displacement state]

[Full diagnosis]

### CHASM-B EXPANSION -- Bridge Condition

Named Inertia in effect: [re-cite I-03]
Incumbent position at this chasm element: [displacement state]

[Full specification]

### CHASM-C EXPANSION -- Crossing Signal

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

> CORRECTION BLOCK MECHANISM ARMED -- no gate failure triggered. Gate H failure inserts above: CORRECTION BLOCK -- I-0X CITATION CONTRACT VIOLATION -- Protected behavior: [value from SECTION A] (C-55). Arc MISMATCH inserts above: ARC CORRECTION BLOCK -- PHASE N close -> PHASE N+1 open MISMATCH -- Protected behavior at boundary: [I-0X: value from SECTION A] (Axis B). SECTION K carries Protected behavior in citation record (C-56) and arc table (Axis C).

## VERIFICATION MODE

All content generation complete. SECTIONS H, I, J, K are audit sections only.

---

## SECTION H -- Gate: C-13 Audit

- I-01: PHASE 1 Q-BARRIER [Y/N] / ledger [Y/N] / PART 3 Q-TRIGGER Innovator [Y/N] -> Fill SECTION A row I-01
- I-02: PHASE 2 Q-BARRIER [Y/N] / ledger [Y/N] / PART 3 Q-TRIGGER EA [Y/N] -> Fill SECTION A row I-02
- I-03: PHASE 3 Q-BARRIER [Y/N] / ledger [Y/N] / CHASM-A [Y/N] / CHASM-B [Y/N] / PHASE 4 Q-BARRIER [Y/N] / PHASE 4 ledger [Y/N] / PART 5 [Y/N] -> Fill SECTION A row I-03
- I-04: PHASE 5 Q-BARRIER [Y/N] / ledger [Y/N] / PART 3 Q-TRIGGER LM [Y/N] -> Fill SECTION A row I-04
- I-05: PHASE 6 Q-BARRIER [Y/N] / ledger [Y/N] / PART 3 Q-TRIGGER Laggard [Y/N] -> Fill SECTION A row I-05

**C-13 four-location check:** Bridge [Y/N] / Intervention [Y/N] / Champion [Y/N] / Churn [Y/N]

**Gate H result:** [PASS / FAIL]

**Correction obligation (C-55 baseline):** Per-I-0X: CORRECTION BLOCK -- I-0X CITATION CONTRACT VIOLATION -- Protected behavior: [value from SECTION A]

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

**Terminal Invariant:** For every Yes, a CORRECTION BLOCK with BEFORE and AFTER fields must exist at cited location. A Yes without a CORRECTION BLOCK, or a CORRECTION BLOCK without BEFORE field, falsifies this invariant. Gate H: per-I-0X CORRECTION BLOCK with Protected behavior (C-55). Arc repair: ARC CORRECTION BLOCK with Protected behavior at boundary (Axis B). Arc table: Protected behavior at boundary column (Axis C).

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

**DISPLACEMENT ARC INTEGRITY CHECK (Axes B + C):**

A MISMATCH triggers an ARC CORRECTION BLOCK. Label: ARC CORRECTION BLOCK -- PHASE N close -> PHASE N+1 open MISMATCH -- Protected behavior at boundary: [I-0X: named behavior from SECTION A for inertia at that phase close] (Axis B).

| Transition | Exit state | Entry state | Protected behavior at boundary: [I-0X + named behavior from SECTION A] | Verdict |
|---|---|---|---|---|
| PHASE 1 close -> PHASE 2 open | | | [I-01: Protected behavior] | MATCH / MISMATCH / CORRECTED |
| PHASE 2 close -> PHASE 3 entry | | | [I-02: Protected behavior] | MATCH / MISMATCH / CORRECTED |
| PHASE 3 close -> PHASE 4 open | | | [I-03: Protected behavior] | MATCH / MISMATCH / CORRECTED |
| PHASE 4 close -> PHASE 5 open | | | [I-03: Protected behavior] | MATCH / MISMATCH / CORRECTED |
| PHASE 5 close -> PHASE 6 open | | | [I-04: Protected behavior] | MATCH / MISMATCH / CORRECTED |

Arc integrity: [PASS if all MATCH or CORRECTED | FAIL naming unrepaired discontinuity]

ARC CORRECTION BLOCK location(s) and label(s): [cite location and full label text, or "none -- all MATCH"]
"""

outpath = 'C:/src/sim/simulations/quest/golden/listen-adoption-QU5-simplified-2026-03-15.md'
with open(outpath, 'w', encoding='utf-8') as f:
    f.write(body)

words = len(body.split())
print(f"Written: {outpath}")
print(f"Word count (simplified body): {words}")
print(f"Original V-05 body: 2656 words")
print(f"Reduction: {2656 - words} words ({(2656-words)/2656*100:.1f}%)")
