Written to `simulations/quest/rubrics/mock-accept-rubric-v9-2026-03-17.md`.

---

## Summary of v9 changes

| What | v8 | v9 |
|------|----|----|
| New criteria | C-31, C-32 (from R7) | C-33 (from R8) |
| Denominator | 24 | 25 |
| C-09 absent denom | 19 | 20 |
| New failure modes | MA-29, MA-30 | MA-31 |
| Golden | R7 V-05 sole golden (24/24 = 100.0) | R8 V-01 sole golden (25/25 = 100.0) |

**C-33** — COST REGISTER PHASE-DIMENSION COLUMN: the MOCK COST REGISTER table adds an explicit Phase column (Architect | Strategy) alongside Namespace and Cost-of-MOCK. Each row is cross-verifiable against the INERTIA LEDGER tally for its corresponding phase gate (GATE C → Architect rows; GATE D → Strategy rows). A flat list or two-column table satisfies C-32 if count assertion and GATE E-COST are present, but not C-33. The Phase column binds the register to the per-phase inertia tallies — both dimensions (what was accepted and in which phase) become verifiable by column inspection without prose parsing.

**R8 V-01 re-scored against v9:**

| Variation | C-33 | Asp passes | Asp score | Total |
|-----------|------|------------|-----------|-------|
| V-01 (3-column table: Namespace \| Phase \| Cost-of-MOCK) | PASS | 25/25 | 10.0 | **100.0** |
| R7 V-05 (field-list; no Phase column) | FAIL | 24/25 | 9.6 | **99.6** |

R7 V-05 is demoted to silver. R8 V-01 is the sole golden.
lf to carry phase attribution so both dimensions (what was accepted and in which phase) are verifiable by column inspection without prose parsing.

---

## R8 ceiling re-scored against v9

| Variation | C-33 | Asp passes | Asp score | Total |
|-----------|------|------------|-----------|-------|
| V-01 (3-column COST REGISTER: Namespace \| Phase \| Cost-of-MOCK) | PASS | 25/25 | 10.0 | **100.0** |
| R7 V-05 (field-list COST REGISTER; no Phase column) | FAIL | 24/25 | 9.6 | **99.6** |

R8 V-01 is the sole golden. R7 V-05 is demoted to silver at 99.6.

---

## Failure modes

| ID | Criterion | Failure Pattern |
|----|-----------|----------------|
| MA-01 | C-01 | Auto-flag rules use "I found..." or evaluator-subject phrasing |
| MA-02 | C-02 | Forbidden triad incomplete; two-of-three accepted without completeness guard |
| MA-03 | C-03 | CANARY ASSERTION absent or CANARY SUPPRESSED branch undefined |
| MA-04 | C-04 | Review sections orphaned outside the single Write block |
| MA-05 | C-05 | Slot 1 / Slot 2 merged; paraphrase not named as violation class |
| MA-06 | C-06 | Role output uses yes/no verdicts without artifact citation template |
| MA-07 | C-07 | Accumulator lists unnamed; empty-list acknowledgment omitted |
| MA-08 | C-08 | REAL-REQUIRED template missing one or more of the 5 required fields |
| MA-09 | C-09 | No standing rule; evaluator-subject form present in phase output |
| MA-10 | C-10 | Tier sourcing omitted or implicit; source not named |
| MA-11 | C-11 | Phase transition proceeds without written count assertion |
| MA-12 | C-12 | CONSTRAINT appears only in preamble; not co-located at point of use |
| MA-13 | C-13 | Phase exit assertion absent or lacks N+M count; interleave not blocked |
| MA-14 | C-14 | Fill-in sites use `[bracket]` notation; absence requires prose parsing |
| MA-15 | C-15 | Standing rule states positive form only; forbidden alternatives not enumerated |
| MA-16 | C-16 | Gate language advisory-only; "Do not proceed until written" absent |
| MA-17 | C-17 | Gates unnamed or ordinal-only; IDs not referenceable across phases |
| MA-18 | C-18 | CONSTRAINT embedded inline within template prose; no adjacent framed block |
| MA-19 | C-19 | Auto-flag templates or CANARY use `[bracket]` notation; fill-in sites not structurally visible |
| MA-20 | C-20 | Forbidden-form enumeration enumerates violations without naming a stop action |
| MA-21 | C-23 | Halt instruction uses two-step or combined phrasing; three-step atomic sequence absent |
| MA-22 | C-24 | Phase 6 gate uses anonymous count assertion; review artifact section IDs not cited by name |
| MA-23 | C-25 | Slot 2 revert names violation class only; no quoted near-miss paraphrase examples |
| MA-24 | C-26 | Halt instruction present in Standing Rule but absent at CONSTRAINT sites; evaluator must cross-reference to detect violation |
| MA-25 | C-27 | GATE F embedded within an existing step; no dedicated step number; gate not independently referenceable |
| MA-26 | C-28 | Slot 2 paraphrase examples listed inline in prose; no structured two-column table; examples require prose parsing to locate |
| MA-27 | C-29 | Evaluation record has no `Cost-of-MOCK:` field; verdict collapses to two-part form (Slot 1 + Slot 2 only) without naming the counterfactual validation risk |
| MA-28 | C-30 | No DEFAULT DECISION POSITION block before STEP 1; evaluation starts from neutral ground; MOCK-ACCEPTED confirmed by absence of disqualification rather than earned against named inertia |
| MA-29 | C-31 | Phase exit gates (GATE C, GATE D) have no INERTIA LEDGER; inertia state is not tracked as a running tally at phase boundaries; progress of earned MOCK-ACCEPTED against inertia is unobservable between evaluation phase and writeback |
| MA-30 | C-32 | No dedicated MOCK COST REGISTER step after GATE D; Cost-of-MOCK entries remain distributed across up to 9 evaluation records with no aggregated count assertion and no pre-writeback audit surface |
| MA-31 | C-33 | MOCK COST REGISTER has no Phase column; entries are attributed to namespace only; cross-verification against per-phase INERTIA LEDGER tallies requires prose parsing rather than column inspection |

---

## Criteria (33 total)

### Essential — C-01 to C-05

| ID | Criterion | Description |
|----|-----------|-------------|
| C-01 | Artifact-as-subject in auto-flag rules | All three auto-flag rules use artifact-as-subject phrasing ("The mock artifact's [ns] section..."); evaluator-subject phrasing disqualifies |
| C-02 | Forbidden triad completeness | All three auto-flag rules (COMPLETE, EMPTY, PARTIAL) are present; "two-of-three does not satisfy" guard required |
| C-03 | CANARY ASSERTION + CANARY SUPPRESSED branch | STATUS WRITEBACK includes CANARY ASSERTION with blank `___` target and a defined CANARY SUPPRESSED branch for false-positive suppression |
| C-04 | Single Write block for review artifact | All review artifact sections are written in one Write call; no sections outside the single Write block |
| C-05 | Slot 1 / Slot 2 separation with paraphrase named | Slot 1 (exact-token reason code) and Slot 2 (artifact-as-subject coverage basis) are structurally separated; paraphrase is named as a violation class in each slot's revert instruction |

### Recommended — C-06 to C-08

| ID | Criterion | Description |
|----|-----------|-------------|
| C-06 | Entity-naming in roles | Each role output uses a "Required artifact citation" template naming specific elements (field name, token, slot) verbatim; yes/no verdicts alone do not satisfy |
| C-07 | Step sequencing and guard compliance | Named accumulator lists (Arch-blocked, Strategy-blocked) populated during evaluation phase; partition explicit before phase exit; empty list must be stated ("Arch-blocked: none") |
| C-08 | Eval-driven REAL-REQUIRED template | 5-field template per role evaluation: trigger condition / SQ answer (artifact as subject) / Artifact state / verdict / required action; VERDICT-ECHO named |

### Aspirational — C-09 to C-33

**Scoring:** `(passes / 25) × 10`

**C-09 N/A cascade:** C-09 → C-15 → C-20 → C-23 → C-26; denominator when C-09 absent = 20 (25 − 5). C-24, C-25, C-27, C-28, C-29, C-30, C-31, C-32, and C-33 are independent of C-09 status.

| ID | Criterion | Description |
|----|-----------|-------------|
| C-09 | Artifact-as-subject grammar | Standing rule embedded at top of spec; auto-flag rules and role evaluations use "The mock artifact's [ns] section [records/shows/lacks]..." form throughout all phases |
| C-10 | Tier sourcing | Opening step output includes "Tier: N (source: TOPICS.md \| --tier \| default)"; instruction tier governing current phase is explicit, not implicit |
| C-11 | Inline completeness gate | Named completeness checkpoint with count assertion: "N + M = [total]. Expected: 9." or equivalent halt condition before phase transitions; anonymous narrative checks do not satisfy |
| C-12 | Reason-code enforcement at point of use | Exact-token constraint co-located with column rule or checkbox at the point of use -- not in preamble or instructions section only |
| C-13 | Phase exit assertions | Explicit named PHASE N EXIT ASSERTION before each phase transition; each includes N+M count; "Do not proceed until" language; blocks interleave of auto-flag and evaluation phases |
| C-14 | Blank-line failure signal | Incomplete slots are structurally visible as fill-in blanks ("Your codes: ___" / "Your statement: ___") without requiring prose parsing; absence readable by inspection |
| C-15 | Forbidden-form enumeration | The artifact-as-subject standing rule enumerates specific forbidden alternatives (e.g., "FAIL: 'I found...' / 'This namespace has...'") alongside the positive form; rule is self-diagnosing without requiring the evaluator to infer violations |
| C-16 | Written-gate blocking language | Phase exit assertions include "Do not proceed to Phase N+1 until written" or equivalent; the assertion must be committed as output text before progression; advisory-only language does not satisfy |
| C-17 | Named gate registry | Completeness gates carry stable sequential IDs (GATE A, GATE B, GATE C...) forming a named registry; IDs are referenceable from other phases and from the review artifact; anonymous or ordinal-only gates do not satisfy |
| C-18 | Adjacent framed CONSTRAINT co-location | Each constrained field is immediately followed by a standalone framed `CONSTRAINT:` line; the constraint appears as a visually distinct block adjacent to its target field; inline embedding within template description text or preamble does not satisfy; applies to all phases containing constrained fields |
| C-19 | Universal blank-slot enforcement | Blank `___` targets appear in auto-flag rule output templates and in the CANARY ASSERTION, not only in MOCK-ACCEPTED slots; every evaluator fill-in site is structurally visible by inspection; bracket notation `[placeholder]` does not satisfy (looks filled even when unmodified) |
| C-20 | Halt-on-violation instruction | The forbidden-form enumeration (C-15) includes an explicit halt or stop instruction naming the action to take when a violation is detected; diagnostic enumeration alone (self-diagnosing without stop action) does not satisfy |
| C-21 | Per-section CONSTRAINT in review Write block | Each named section within the review artifact Write block carries its own co-located CONSTRAINT block; a single top-level Write instruction without per-section constraints does not satisfy; extends C-12 to the review artifact structure |
| C-22 | Slot 1 paraphrase violation examples | Slot 1 revert-on-violation includes at least two quoted concrete paraphrase examples (altered token forms); naming "paraphrase" as a violation class without examples does not satisfy |
| C-23 | Three-step halt sequence | The Standing Rule halt instruction names three sequential atomic steps using imperatives (HALT / DELETE / REWRITE or equivalent); two-step phrasing ("halt and rewrite") satisfies C-20 but not C-23; the three-step form eliminates evaluator discretion about intermediate steps; advisory phrasing or combined gerunds do not satisfy |
| C-24 | Gate-to-section traceability in Phase 6 gate | The Phase 6 completeness gate (GATE F or equivalent) explicitly names the review artifact sections it covers (e.g., Coverage, Structural records, Risk, Next Steps) by their stable IDs; an anonymous count assertion or generic "all sections" phrasing does not satisfy; creates verifiable traceability from gate assertion to artifact structure |
| C-25 | Slot 2 paraphrase violation examples | Slot 2 revert-on-violation includes at least two quoted near-miss paraphrase examples (altered-token forms); relying on forbidden-form class labels or generic violation categories without concrete quoted examples does not satisfy; extends C-22 to cover both MOCK-ACCEPTED slots |
| C-26 | Halt co-location at each CONSTRAINT site | The three-step halt instruction from the Standing Rule (C-23) is also repeated inline at every CONSTRAINT block throughout all phases; having the halt instruction only in the opening Standing Rule satisfies C-23 but not C-26; the per-site form eliminates the need to cross-reference the Standing Rule from within a constrained field; applies to all phases containing constrained fields |
| C-27 | GATE F as standalone dedicated numbered step | The Phase 6 completeness gate (GATE F or equivalent) occupies its own step with a distinct step number, separate from the review artifact Write instruction; embedding GATE F within an existing step satisfies C-24 but not C-27; a dedicated step makes the gate independently referenceable by step number and resistant to context compression |
| C-28 | Slot 2 violation table | The Slot 2 paraphrase examples (C-25) are presented as a structured two-column table (quoted near-miss form / violation type); a prose note referencing the violation class or listing examples inline satisfies C-25 if >= 2 quoted forms are present, but does not satisfy C-28; the table format makes violation examples scannable by inspection without parsing prose |
| C-29 | Cost-of-MOCK field in evaluation record | Each MOCK-ACCEPTED verdict in the evaluation record (STEP 3, STEP 4) includes a dedicated `Cost-of-MOCK:` field producing a constrained counterfactual statement: "Without real data for [namespace], [specific type] remains unvalidated by production evidence at Tier [N]."; the field is structurally separate from Slot 1 (exact-token reason code) and Slot 2 (artifact-as-subject coverage basis); naming a risk class or generic caveat without the constrained forward-facing format does not satisfy; extends the evaluation record from a two-part verdict to a three-part verdict |
| C-30 | DEFAULT DECISION POSITION block as pre-phase inertia anchor | A named block placed before STEP 1 declares that every namespace begins at REAL-REQUIRED; MOCK-ACCEPTED is described as earned against named inertia -- not confirmed by the absence of a disqualification; the block must be structurally present before the evaluation phase (STEP 3, STEP 4) and govern those steps; a note within STEP 6 or elsewhere in the positive-argument phase does not satisfy; structurally distinct from C-05 (MOCK-ACCEPTED positive argument in STEP 6) because it sets the epistemic default for the evaluation phase, not the documentation phase |
| C-31 | INERTIA LEDGER at phase gates | Within GATE C and GATE D, a named INERTIA LEDGER -- [PHASE] PHASE EXIT block records a per-phase running tally: namespaces still at REAL-REQUIRED default and namespaces that have earned MOCK-ACCEPTED against inertia; a constrained sum assertion ties the tally to the non-auto-flagged count from GATE B with an explicit HALT if the sum does not match; the block must appear inside the gate at phase exit -- a note at phase entry or inline text does not satisfy; structurally distinct from C-30 (initial state declaration) and C-29 (per-namespace cost in evaluation record) |
| C-32 | MOCK COST REGISTER as dedicated post-evaluation step | A dedicated step inserted after GATE D and before STATUS WRITEBACK enumerates all MOCK-ACCEPTED namespaces from both Architect and Strategy phases, copies the Cost-of-MOCK entry verbatim from each evaluation record, fires a COST REGISTER ASSERTION count assertion (Expected: N = total MOCK-ACCEPTED), and closes with a standalone gate (GATE E-COST -- COST REGISTER COMPLETE); the register aggregates distributed inline cost statements into a single independently verifiable pre-writeback audit surface; a summary table appended to the final review artifact does not satisfy -- the register must be a distinct numbered step with its own gate placed before writeback; not reducible to C-29 (aggregation vs inline), C-30 (initial state), or C-31 (per-gate inertia tally) |
| C-33 | COST REGISTER phase-dimension column | The MOCK COST REGISTER table includes an explicit Phase column (Architect \| Strategy) alongside Namespace and Cost-of-MOCK; each entry is thereby cross-verifiable against the INERTIA LEDGER tally for its corresponding phase gate (GATE C → Architect rows; GATE D → Strategy rows); a flat enumeration or two-column table without phase attribution satisfies C-32 if count assertion and GATE E-COST are present, but does not satisfy C-33; the Phase column binds the register to the per-phase inertia tallies so both dimensions (what was accepted and in which phase) are verifiable by column inspection without prose parsing; distinct from C-31 (inertia state tally at phase gates) and C-32 (aggregated audit surface before writeback) |

**C-09 N/A cascade:** if C-09 is absent → C-15 N/A → C-20 N/A → C-23 N/A → C-26 N/A; active denominator becomes 20 (25 − 5). C-24, C-25, C-27, C-28, C-29, C-30, C-31, C-32, and C-33 are independent of C-09 status.
