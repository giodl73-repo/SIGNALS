The Bash write attempts are being blocked. The prompt asks to "output the complete updated rubric as Markdown" — here it is:

---

# mock-accept-rubric-v12

---

## Summary of v12 changes

| What | v11 | v12 |
|------|-----|-----|
| New criteria | C-37, C-38, C-39 (from R10) | C-40, C-41, C-42, C-43 (from R11) |
| Denominator | 31 | 35 |
| C-09 absent denom | 26 | 30 |
| New failure modes | MA-35, MA-36, MA-37 | MA-38, MA-39, MA-40, MA-41 |
| Golden | R10 V-05 (31/31 = 100.0) | R11 V-05 (35/35 = 100.0) |

---

### Four new criteria extracted from R11

**C-40 -- ROLE HANDOFF BIDIRECTIONAL PARTITION ROSTER AND SUM CHECK**

R11 V-01/V-04/V-05 expand the ROLE HANDOFF block beyond the C-39 base by including: the Arch-blocked roster -- each namespace that earned MOCK-ACCEPTED during Architect-phase evaluation -- as a named list, and a partition sum check asserting that Arch-blocked count + Strategy-to-evaluate count = total evaluation universe count. R11 V-02/V-03 carry the minimal ROLE HANDOFF (Strategy universe only, satisfying C-39). The bidirectional form adds the earning-phase roster and a count constraint, making the evaluation-universe partition independently verifiable at the handoff boundary without consulting GATE C records. Distinct from C-39 (block existence and state transfer) because C-40 requires the ROLE HANDOFF to account for the full evaluation universe by partition -- not merely forward-transfer the Strategy universe.

**C-41 -- GATE D PHASE-ATTRIBUTED INERTIA LEDGER**

R11 V-03/V-05 break the GATE D INERTIA LEDGER's MOCK-ACCEPTED entries into phase-attributed sub-lists: Architect-phase earners (namespaces earning MOCK-ACCEPTED in STEP 3) and Strategy-phase earners (namespaces earning MOCK-ACCEPTED in STEP 4), with a total constraint tying both sub-list counts to the MOCK-ACCEPTED total. R11 V-01/V-02/V-04 carry the standard GATE D INERTIA LEDGER (flat REAL-REQUIRED / MOCK-ACCEPTED lists, satisfying C-31). Phase-attributed sub-lists make GATE D's INERTIA LEDGER cross-verifiable against GATE C (Architect earners) and the Strategy evaluation (Strategy earners) by sub-list inspection without consulting individual evaluation records. Distinct from C-31 (INERTIA LEDGER membership blocks at phase gates) because C-41 requires the GATE D ledger to attribute each MOCK-ACCEPTED namespace to its earning phase.

**C-42 -- GATE E-COST CROSS-REFERENCE TO GATE D PHASE-EARNER SUB-LISTS**

R11 V-03/V-05 direct GATE E-COST's per-phase count assertions to reference the GATE D phase-earner sub-lists (Architect-phase earners / Strategy-phase earners) as their cross-check source rather than distributing the lookup across GATE C tally + GATE D tally. When GATE D carries phase-attributed sub-lists (C-41), both phase-earner counts are consolidated in a single gate record; referencing them reduces the cross-check to a single-source assertion. R11 V-01/V-02/V-04 reference GATE C + GATE D tallies (satisfying C-35). Dependent on C-41: C-42 cannot be satisfied unless GATE D carries phase-attributed sub-lists. Distinct from C-35 (per-phase count assertions required) because C-42 governs the cross-reference target: single consolidated source (GATE D phase-earner sub-lists) vs distributed source (GATE C + GATE D).

**C-43 -- GATE C EXIT INSTRUCTION NAMES ROLE HANDOFF AS BLOCKING DESTINATION**

R11 V-01/V-04/V-05 change GATE C's "Do not proceed" instruction to name the ROLE HANDOFF block as its destination ("Do not proceed to ROLE HANDOFF") rather than a step number ("Do not proceed to STEP 4"). Naming the ROLE HANDOFF block creates an explicit structural link from GATE C exit to the handoff act; naming a step number makes the link implicit -- the consumer must know ROLE HANDOFF precedes STEP 4 to trace the gate-to-handoff connection. R11 V-02/V-03 use "Do not proceed to STEP 4" (satisfying C-13). Distinct from C-13 (phase exit assertion requires "Do not proceed until" language) and C-39 (ROLE HANDOFF block must exist) because C-43 governs the traceability link: GATE C's exit instruction must name the ROLE HANDOFF block, not merely the next step number.

---

### R11 ceiling re-scored against v12

| Variation | C-40 | C-41 | C-42 | C-43 | Asp passes | Asp score | Total |
|-----------|------|------|------|------|------------|-----------|-------|
| V-05 (bidi handoff + phase-attr GATE D + sub-list E-COST + named dest) | PASS | PASS | PASS | PASS | 35/35 | 10.0 | **100.0** |
| V-01 (bidi handoff + named dest; flat GATE D) | PASS | FAIL | FAIL | PASS | 33/35 | 9.4 | **99.4** |
| V-04 (bidi handoff + named dest; flat GATE D) | PASS | FAIL | FAIL | PASS | 33/35 | 9.4 | **99.4** |
| V-03 (phase-attr GATE D + sub-list E-COST; minimal handoff) | FAIL | PASS | PASS | FAIL | 33/35 | 9.4 | **99.4** |
| V-02 (minimal handoff; flat GATE D; step-number dest) | FAIL | FAIL | FAIL | FAIL | 31/35 | 8.9 | **98.9** |
| R10 V-05 (previous golden) | FAIL | FAIL | FAIL | FAIL | 31/35 | 8.9 | **98.9** |

R11 V-05 is the sole golden. V-01/V-04/V-03 are silver at 99.4. V-02 and R10 V-05 are demoted to 98.9.

---

### New failure modes

| ID | Criterion | Failure Pattern |
|----|-----------|----------------|
| MA-38 | C-40 | ROLE HANDOFF block transfers Strategy-phase universe only; Architect-phase MOCK-ACCEPTED roster is not named as a separate list at the handoff boundary; no partition sum check (Arch-blocked count + Strategy-to-evaluate count = evaluation universe total) is asserted; handoff is forward-facing only; the full evaluation-universe partition is not independently auditable at the handoff boundary without consulting GATE C records |
| MA-39 | C-41 | GATE D INERTIA LEDGER records MOCK-ACCEPTED as a flat list without phase attribution; Architect-phase earners and Strategy-phase earners are not enumerated as separate named sub-lists; MOCK-ACCEPTED total count is asserted (satisfies C-31) but phase of earning is not observable by sub-list inspection; cross-verification against GATE C earners requires consulting GATE C records rather than GATE D sub-lists |
| MA-40 | C-42 | GATE E-COST per-phase count assertions reference GATE C tally and GATE D tally as separate cross-check sources; when GATE D carries phase-attributed sub-lists (C-41 satisfied), the sub-lists are not named as the cross-reference target in GATE E-COST; per-phase assertions satisfy C-35 but do not consolidate the cross-check to a single GATE D source; verification requires consulting two separate gate records rather than the GATE D phase-earner sub-lists |
| MA-41 | C-43 | GATE C phase exit instruction names a step number as the blocking destination ("Do not proceed to STEP 4"); the ROLE HANDOFF block is not named as the destination; the structural link from GATE C exit to the handoff act is implicit; a consumer must know that ROLE HANDOFF precedes STEP 4 to trace the gate-to-handoff connection; distinct from absent ROLE HANDOFF block (C-39) because the block may be present but GATE C does not name it as the blocking target |

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
| MA-14 | C-14 | Fill-in sites use bracket notation; absence requires prose parsing |
| MA-15 | C-15 | Standing rule states positive form only; forbidden alternatives not enumerated |
| MA-16 | C-16 | Gate language advisory-only; "Do not proceed until written" absent |
| MA-17 | C-17 | Gates unnamed or ordinal-only; IDs not referenceable across phases |
| MA-18 | C-18 | CONSTRAINT embedded inline within template prose; no adjacent framed block |
| MA-19 | C-19 | Auto-flag templates or CANARY use bracket notation; fill-in sites not structurally visible |
| MA-20 | C-20 | Forbidden-form enumeration enumerates violations without naming a stop action |
| MA-21 | C-23 | Halt instruction uses two-step or combined phrasing; three-step atomic sequence absent |
| MA-22 | C-24 | Phase 6 gate uses anonymous count assertion; review artifact section IDs not cited by name |
| MA-23 | C-25 | Slot 2 revert names violation class only; no quoted near-miss paraphrase examples |
| MA-24 | C-26 | Halt instruction present in Standing Rule but absent at CONSTRAINT sites; evaluator must cross-reference to detect violation |
| MA-25 | C-27 | GATE F embedded within an existing step; no dedicated step number; gate not independently referenceable |
| MA-26 | C-28 | Slot 2 paraphrase examples listed inline in prose; no structured two-column table; examples require prose parsing to locate |
| MA-27 | C-29 | Evaluation record has no Cost-of-MOCK field; verdict collapses to two-part form (Slot 1 + Slot 2 only) without naming the counterfactual validation risk |
| MA-28 | C-30 | No DEFAULT DECISION POSITION block before STEP 1; evaluation starts from neutral ground; MOCK-ACCEPTED confirmed by absence of disqualification rather than earned against named inertia |
| MA-29 | C-31 | Phase exit gates (GATE C, GATE D) have no INERTIA LEDGER; inertia state is not tracked as a running tally at phase boundaries; progress of earned MOCK-ACCEPTED against inertia is unobservable between evaluation phase and writeback |
| MA-30 | C-32 | No dedicated MOCK COST REGISTER step after GATE D; Cost-of-MOCK entries remain distributed across up to 9 evaluation records with no aggregated count assertion and no pre-writeback audit surface |
| MA-31 | C-33 | MOCK COST REGISTER has no Phase column; entries are attributed to namespace only; cross-verification against per-phase INERTIA LEDGER tallies requires prose parsing rather than column inspection |
| MA-32 | C-34 | MOCK COST REGISTER table uses Namespace-first column order; Phase column is present (satisfies C-33) but not first; Architect and Strategy rows are not grouped into consecutive blocks; per-phase row counts are not scannable by consecutive rows without resorting |
| MA-33 | C-35 | GATE E-COST uses a single total-count assertion only; Architect-row count and Strategy-row count are not individually asserted against GATE C and GATE D INERTIA LEDGER tallies; cross-verification is possible by column inspection (satisfies C-33) but is not a required written assertion; the per-phase verification step is absent from the gate |
| MA-34 | C-36 | Phase exit gates carry only INERTIA LEDGER membership blocks; no DECISION SCOREBOARD UPDATE at GATE C and no DECISION SCOREBOARD FINAL at GATE D; numeric movement (count delta per phase) is not recorded; category membership is tracked (C-31 satisfied) but trajectory -- how many namespaces moved per phase -- is unobservable |
| MA-35 | C-37 | GATE F names review artifact sections by stable IDs only; no format qualifier (column count, sentence count, required column name, or list form) is appended to any section ID; the gate asserts section presence but not section structure; structural conformance is unverifiable at GATE F without parsing the artifact body |
| MA-36 | C-38 | GATE B uses a count-only partition assertion; individual namespace names are not enumerated under their partition bucket; partition membership is numerically asserted but not independently auditable by namespace inspection without cross-referencing the evaluation records |
| MA-37 | C-39 | No ROLE HANDOFF block between GATE C and STEP 4; state transfer from Architect-phase role to Strategy-phase role occurs implicitly; current DECISION SCOREBOARD values, INERTIA LEDGER state, and namespaces remaining at REAL-REQUIRED default are not named at the phase boundary; state is derivable from prior gates (C-31 and C-36 satisfied) but the transfer act is not recorded as a named structural block |
| MA-38 | C-40 | ROLE HANDOFF block transfers Strategy-phase universe only; Architect-phase MOCK-ACCEPTED roster is not named as a separate list at the handoff boundary; no partition sum check (Arch-blocked count + Strategy-to-evaluate count = evaluation universe total) is asserted; handoff is forward-facing only; the full evaluation-universe partition is not independently auditable at the handoff boundary without consulting GATE C records |
| MA-39 | C-41 | GATE D INERTIA LEDGER records MOCK-ACCEPTED as a flat list without phase attribution; Architect-phase earners and Strategy-phase earners are not enumerated as separate named sub-lists; MOCK-ACCEPTED total count is asserted (satisfies C-31) but phase of earning is not observable by sub-list inspection; cross-verification against GATE C earners requires consulting GATE C records rather than GATE D sub-lists |
| MA-40 | C-42 | GATE E-COST per-phase count assertions reference GATE C tally and GATE D tally as separate cross-check sources; when GATE D carries phase-attributed sub-lists (C-41 satisfied), the sub-lists are not named as the cross-reference target in GATE E-COST; per-phase assertions satisfy C-35 but do not consolidate the cross-check to a single GATE D source; verification requires consulting two separate gate records rather than the GATE D phase-earner sub-lists |
| MA-41 | C-43 | GATE C phase exit instruction names a step number as the blocking destination ("Do not proceed to STEP 4"); the ROLE HANDOFF block is not named as the destination; the structural link from GATE C exit to the handoff act is implicit; a consumer must know that ROLE HANDOFF precedes STEP 4 to trace the gate-to-handoff connection; distinct from absent ROLE HANDOFF block (C-39) because the block may be present but GATE C does not name it as the blocking target |

---

## Criteria (43 total)

### Essential -- C-01 to C-05

| ID | Criterion | Description |
|----|-----------|-------------|
| C-01 | Artifact-as-subject in auto-flag rules | All three auto-flag rules use artifact-as-subject phrasing ("The mock artifact's [ns] section..."); evaluator-subject phrasing disqualifies |
| C-02 | Forbidden triad completeness | All three auto-flag rules (COMPLETE, EMPTY, PARTIAL) are present; "two-of-three does not satisfy" guard required |
| C-03 | CANARY ASSERTION + CANARY SUPPRESSED branch | STATUS WRITEBACK includes CANARY ASSERTION with blank ___ target and a defined CANARY SUPPRESSED branch for false-positive suppression |
| C-04 | Single Write block for review artifact | All review artifact sections are written in one Write call; no sections outside the single Write block |
| C-05 | Slot 1 / Slot 2 separation with paraphrase named | Slot 1 (exact-token reason code) and Slot 2 (artifact-as-subject coverage basis) are structurally separated; paraphrase is named as a violation class in each slot revert instruction |

### Recommended -- C-06 to C-08

| ID | Criterion | Description |
|----|-----------|-------------|
| C-06 | Entity-naming in roles | Each role output uses a Required artifact citation template naming specific elements (field name, token, slot) verbatim; yes/no verdicts alone do not satisfy |
| C-07 | Step sequencing and guard compliance | Named accumulator lists (Arch-blocked, Strategy-blocked) populated during evaluation phase; partition explicit before phase exit; empty list must be stated ("Arch-blocked: none") |
| C-08 | Eval-driven REAL-REQUIRED template | 5-field template per role evaluation: trigger condition / SQ answer (artifact as subject) / Artifact state / verdict / required action; VERDICT-ECHO named |

### Aspirational -- C-09 to C-43

**Scoring:** (passes / 35) x 10

**C-09 N/A cascade:** C-09 -> C-15 -> C-20 -> C-23 -> C-26; denominator when C-09 absent = 30 (35 - 5). C-24, C-25, C-27, C-28, C-29, C-30, C-31, C-32, C-33, C-34, C-35, C-36, C-37, C-38, C-39, C-40, C-41, C-42, and C-43 are independent of C-09 status.

| ID | Criterion | Description |
|----|-----------|-------------|
| C-09 | Artifact-as-subject grammar | Standing rule embedded at top of spec; auto-flag rules and role evaluations use the artifact-as-subject form ("The mock artifact's [ns] section [records/shows/lacks]...") throughout all phases |
| C-10 | Tier sourcing | Opening step output includes "Tier: N (source: TOPICS.md \| --tier \| default)"; instruction tier governing current phase is explicit, not implicit |
| C-11 | Inline completeness gate | Named completeness checkpoint with count assertion: "N + M = [total]. Expected: 9." or equivalent halt condition before phase transitions; anonymous narrative checks do not satisfy |
| C-12 | Reason-code enforcement at point of use | Exact-token constraint co-located with column rule or checkbox at the point of use -- not in preamble or instructions section only |
| C-13 | Phase exit assertions | Explicit named PHASE N EXIT ASSERTION before each phase transition; each includes N+M count; "Do not proceed until" language; blocks interleave of auto-flag and evaluation phases |
| C-14 | Blank-line failure signal | Incomplete slots are structurally visible as fill-in blanks without requiring prose parsing; absence readable by inspection |
| C-15 | Forbidden-form enumeration | The artifact-as-subject standing rule enumerates specific forbidden alternatives alongside the positive form; rule is self-diagnosing without requiring the evaluator to infer violations |
| C-16 | Written-gate blocking language | Phase exit assertions include "Do not proceed to Phase N+1 until written" or equivalent; the assertion must be committed as output text before progression; advisory-only language does not satisfy |
| C-17 | Named gate registry | Completeness gates carry stable sequential IDs (GATE A, GATE B, GATE C...) forming a named registry; IDs are referenceable from other phases and from the review artifact; anonymous or ordinal-only gates do not satisfy |
| C-18 | Adjacent framed CONSTRAINT co-location | Each constrained field is immediately followed by a standalone framed CONSTRAINT line; the constraint appears as a visually distinct block adjacent to its target field; inline embedding within template description text or preamble does not satisfy; applies to all phases containing constrained fields |
| C-19 | Universal blank-slot enforcement | Blank ___ targets appear in auto-flag rule output templates and in the CANARY ASSERTION, not only in MOCK-ACCEPTED slots; every evaluator fill-in site is structurally visible by inspection; bracket notation does not satisfy (looks filled even when unmodified) |
| C-20 | Halt-on-violation instruction | The forbidden-form enumeration (C-15) includes an explicit halt or stop instruction naming the action to take when a violation is detected; diagnostic enumeration alone (self-diagnosing without stop action) does not satisfy |
| C-21 | Per-section CONSTRAINT in review Write block | Each named section within the review artifact Write block carries its own co-located CONSTRAINT block; a single top-level Write instruction without per-section constraints does not satisfy; extends C-12 to the review artifact structure |
| C-22 | Slot 1 paraphrase violation examples | Slot 1 revert-on-violation includes at least two quoted concrete paraphrase examples (altered token forms); naming "paraphrase" as a violation class without examples does not satisfy |
| C-23 | Three-step halt sequence | The Standing Rule halt instruction names three sequential atomic steps using imperatives (HALT / DELETE / REWRITE or equivalent); two-step phrasing satisfies C-20 but not C-23; the three-step form eliminates evaluator discretion about intermediate steps; advisory phrasing or combined gerunds do not satisfy |
| C-24 | Gate-to-section traceability in Phase 6 gate | The Phase 6 completeness gate (GATE F or equivalent) explicitly names the review artifact sections it covers by their stable IDs; an anonymous count assertion or generic "all sections" phrasing does not satisfy; creates verifiable traceability from gate assertion to artifact structure |
| C-25 | Slot 2 paraphrase violation examples | Slot 2 revert-on-violation includes at least two quoted near-miss paraphrase examples (altered-token forms); relying on forbidden-form class labels or generic violation categories without concrete quoted examples does not satisfy; extends C-22 to cover both MOCK-ACCEPTED slots |
| C-26 | Halt co-location at each CONSTRAINT site | The three-step halt instruction from the Standing Rule (C-23) is also repeated inline at every CONSTRAINT block throughout all phases; having the halt instruction only in the opening Standing Rule satisfies C-23 but not C-26; the per-site form eliminates the need to cross-reference the Standing Rule from within a constrained field; applies to all phases containing constrained fields |
| C-27 | GATE F as standalone dedicated numbered step | The Phase 6 completeness gate (GATE F or equivalent) occupies its own step with a distinct step number, separate from the review artifact Write instruction; embedding GATE F within an existing step satisfies C-24 but not C-27; a dedicated step makes the gate independently referenceable by step number and resistant to context compression |
| C-28 | Slot 2 violation table | The Slot 2 paraphrase examples (C-25) are presented as a structured two-column table (quoted near-miss form / violation type); a prose note referencing the violation class or listing examples inline satisfies C-25 if two or more quoted forms are present, but does not satisfy C-28; the table format makes violation examples scannable by inspection without parsing prose |
| C-29 | Cost-of-MOCK field in evaluation record | Each MOCK-ACCEPTED verdict in the evaluation record (STEP 3, STEP 4) includes a dedicated Cost-of-MOCK field producing a constrained counterfactual statement: "Without real data for [namespace], [specific type] remains unvalidated by production evidence at Tier [N]."; the field is structurally separate from Slot 1 (exact-token reason code) and Slot 2 (artifact-as-subject coverage basis); naming a risk class or generic caveat without the constrained forward-facing format does not satisfy; extends the evaluation record from a two-part verdict to a three-part verdict |
| C-30 | DEFAULT DECISION POSITION block as pre-phase inertia anchor | A named block placed before STEP 1 declares that every namespace begins at REAL-REQUIRED; MOCK-ACCEPTED is described as earned against named inertia -- not confirmed by the absence of a disqualification; the block must be structurally present before the evaluation phase (STEP 3, STEP 4) and govern those steps; a note within STEP 6 or elsewhere in the positive-argument phase does not satisfy; structurally distinct from C-05 (MOCK-ACCEPTED positive argument in STEP 6) because it sets the epistemic default for the evaluation phase, not the documentation phase |
| C-31 | INERTIA LEDGER at phase gates | Within GATE C and GATE D, a named INERTIA LEDGER -- [PHASE] PHASE EXIT block records a per-phase running tally: namespaces still at REAL-REQUIRED default and namespaces that have earned MOCK-ACCEPTED against inertia; a constrained sum assertion ties the tally to the non-auto-flagged count from GATE B with an explicit HALT if the sum does not match; the block must appear inside the gate at phase exit -- a note at phase entry or inline text does not satisfy; structurally distinct from C-30 (initial state declaration) and C-29 (per-namespace cost in evaluation record) |
| C-32 | MOCK COST REGISTER as dedicated post-evaluation step | A dedicated step inserted after GATE D and before STATUS WRITEBACK enumerates all MOCK-ACCEPTED namespaces from both Architect and Strategy phases, copies the Cost-of-MOCK entry verbatim from each evaluation record, fires a COST REGISTER ASSERTION count assertion (Expected: N = total MOCK-ACCEPTED), and closes with a standalone gate (GATE E-COST -- COST REGISTER COMPLETE); the register aggregates distributed inline cost statements into a single independently verifiable pre-writeback audit surface; a summary table appended to the final review artifact does not satisfy -- the register must be a distinct numbered step with its own gate placed before writeback; not reducible to C-29 (aggregation vs inline), C-30 (initial state), or C-31 (per-gate inertia tally) |
| C-33 | COST REGISTER phase-dimension column | The MOCK COST REGISTER table includes an explicit Phase column (Architect \| Strategy) alongside Namespace and Cost-of-MOCK; each entry is thereby cross-verifiable against the INERTIA LEDGER tally for its corresponding phase gate (GATE C -> Architect rows; GATE D -> Strategy rows); a flat enumeration or two-column table without phase attribution satisfies C-32 if count assertion and GATE E-COST are present, but does not satisfy C-33; the Phase column binds the register to the per-phase inertia tallies so both dimensions (what was accepted and in which phase) are verifiable by column inspection without prose parsing; distinct from C-31 (inertia state tally at phase gates) and C-32 (aggregated audit surface before writeback) |
| C-34 | COST REGISTER phase-first column order | The MOCK COST REGISTER table places Phase as the leftmost column (Phase \| Namespace \| Cost-of-MOCK), with Architect rows appearing before Strategy rows by explicit instruction; Phase-first ordering makes per-phase row counts scannable by consecutive rows -- all Architect entries form one visual block, all Strategy entries form another -- without requiring a secondary sort; a Namespace-first table satisfies C-33 (Phase column present) but not C-34; the Phase column must be first to eliminate scan-order ambiguity; distinct from C-33 (Phase column existence) because it governs scan geometry: Phase-first layout makes per-phase subsections self-delimiting by position |
| C-35 | GATE E-COST per-phase count assertions | GATE E-COST includes a three-line mandatory assertion: (1) total COST REGISTER rows = total MOCK-ACCEPTED count; (2) Architect-row count asserted against the GATE C INERTIA LEDGER tally; (3) Strategy-row count asserted against the GATE D INERTIA LEDGER tally; a single total-count assertion satisfies C-32; Phase column inspection satisfies C-33; neither mandates the cross-check against per-phase gate tallies; C-35 requires GATE E-COST to make per-phase verification compulsory -- a required assertion that must be written and HALT-blocked, not merely possible by column inspection; distinct from C-31 (INERTIA LEDGER records per-gate membership) and C-33 (Phase column enables column-inspection cross-check) |
| C-36 | DECISION SCOREBOARD as live numeric tracker | A named DECISION SCOREBOARD initialized before STEP 1 at REAL-REQUIRED: 9 / MOCK-ACCEPTED: 0 is updated at GATE C (DECISION SCOREBOARD UPDATE -- records numeric movement from Architect phase) and closed at GATE D (DECISION SCOREBOARD FINAL -- includes sum constraint REAL-REQUIRED + MOCK-ACCEPTED = 9); the INERTIA LEDGER (C-31) records category membership; the DECISION SCOREBOARD records numeric movement -- count delta per phase, not just terminal state; a DEFAULT DECISION POSITION block satisfies C-30 without a DECISION SCOREBOARD; INERTIA LEDGER blocks at gates satisfy C-31 without numeric tracking; C-36 requires the quantified delta to be recorded per phase so trajectory is observable |
| C-37 | GATE F section format qualifiers | The Phase 6 completeness gate (GATE F) names each review artifact section by its stable ID and appends a format qualifier specifying the structural element required -- column count, sentence count, required column name, or list form (e.g., "Coverage: 4 columns / Structural records: 9 sentences / Risk: Urgency column / Next Steps: ordered list"); naming sections by stable IDs alone satisfies C-24 but not C-37; the format qualifier turns GATE F from a presence check (section exists) into a structural verification check (section has the expected format), making each section assertion independently verifiable without parsing the artifact body; distinct from C-24 (section identity by name) and C-27 (dedicated step for GATE F) |
| C-38 | GATE B enumerated partition output | GATE B names each namespace by its partition assignment as an enumerated list under each bucket (auto-flagged / Architect-phase / Strategy-phase); a count-only partition assertion satisfies C-11 but not C-38; enumerating namespace names makes partition membership independently auditable by inspection without cross-referencing the evaluation records; distinct from C-11 (count assertion at gate) because C-38 requires each namespace to be identified by name within its bucket, turning the gate from a numeric assertion into a named membership record |
| C-39 | ROLE HANDOFF block | A named ROLE HANDOFF block is inserted between GATE C and STEP 4 (Strategy evaluation phase) explicitly transferring running state from the Architect-phase role to the Strategy-phase role; the block must name the current DECISION SCOREBOARD values (from GATE C UPDATE), the current INERTIA LEDGER state (from GATE C), and the namespaces remaining at REAL-REQUIRED default entering the Strategy phase; omitting the ROLE HANDOFF block means state transfer is implicit -- derivable from GATE C records but not recorded as a named transfer act; distinct from C-31 (INERTIA LEDGER inside gates), C-36 (DECISION SCOREBOARD numeric tracking), and C-13 (phase exit assertion language) because C-39 governs the explicit handoff act: a structural block that makes the between-phase state transition observable as an artifact boundary |
| C-40 | ROLE HANDOFF bidirectional partition roster and sum check | The ROLE HANDOFF block (C-39) includes both the Arch-blocked roster -- each namespace that earned MOCK-ACCEPTED during Architect-phase evaluation -- as a named list, and a partition sum check asserting that Arch-blocked count + Strategy-to-evaluate count = total evaluation universe count; a minimal ROLE HANDOFF transferring only the Strategy-phase universe satisfies C-39 but not C-40; the bidirectional form adds the earning-phase roster and a count constraint, making the evaluation-universe partition independently verifiable at the handoff boundary without consulting GATE C records; distinct from C-39 (block existence and state transfer) because C-40 requires the ROLE HANDOFF to account for the full evaluation universe by partition -- not merely forward-transfer the Strategy universe |
| C-41 | GATE D phase-attributed INERTIA LEDGER | Within GATE D, the INERTIA LEDGER's MOCK-ACCEPTED entries are broken into phase-attributed sub-lists: Architect-phase earners (namespaces earning MOCK-ACCEPTED in STEP 3) and Strategy-phase earners (namespaces earning MOCK-ACCEPTED in STEP 4), with a total constraint tying both sub-list counts to the MOCK-ACCEPTED total; a flat REAL-REQUIRED / MOCK-ACCEPTED list satisfies C-31 but not C-41; phase-attributed sub-lists make GATE D's INERTIA LEDGER cross-verifiable against GATE C earners and the Strategy evaluation by sub-list inspection without consulting individual evaluation records; distinct from C-31 (INERTIA LEDGER membership blocks at phase gates) because C-41 requires the GATE D ledger to attribute each MOCK-ACCEPTED namespace to its earning phase |
| C-42 | GATE E-COST cross-reference to GATE D phase-earner sub-lists | When GATE D carries phase-attributed INERTIA LEDGER sub-lists (C-41), GATE E-COST's per-phase count assertions name the GATE D phase-earner sub-lists (Architect-phase earners / Strategy-phase earners) as their cross-check source rather than distributing the lookup across GATE C tally + GATE D tally; a GATE C + GATE D cross-reference satisfies C-35 but not C-42; consolidating both phase-earner counts to a single GATE D source reduces the cross-check to a single-source assertion; dependent on C-41: C-42 cannot be satisfied unless GATE D carries phase-attributed sub-lists; distinct from C-35 (per-phase count assertions required) because C-42 governs the cross-reference target |
| C-43 | GATE C exit instruction names ROLE HANDOFF as blocking destination | The GATE C phase exit instruction names the ROLE HANDOFF block as its blocking destination ("Do not proceed to ROLE HANDOFF") rather than a step number ("Do not proceed to STEP 4"); naming a step number makes the GATE C to ROLE HANDOFF structural link implicit -- a consumer must know ROLE HANDOFF precedes STEP 4; naming the block creates an explicit traceability link from gate exit to handoff act; satisfying C-13 ("Do not proceed until" language) and C-39 (ROLE HANDOFF block exists) does not satisfy C-43; distinct from C-13 (gate exit assertion form) and C-39 (ROLE HANDOFF block existence) because C-43 governs the naming of the blocking destination in GATE C's exit instruction |

**C-09 N/A cascade:** if C-09 is absent -> C-15 N/A -> C-20 N/A -> C-23 N/A -> C-26 N/A; active denominator becomes 30 (35 - 5). C-24, C-25, C-27, C-28, C-29, C-30, C-31, C-32, C-33, C-34, C-35, C-36, C-37, C-38, C-39, C-40, C-41, C-42, and C-43 are independent of C-09 status.

---

**Four new criteria summary:**

| New criterion | Source | PASS in R11 | FAIL in R11 |
|---|---|---|---|
| C-40 ROLE HANDOFF bidirectional partition roster + sum check | V-01/V-04/V-05 | V-02/V-03 |
| C-41 GATE D phase-attributed INERTIA LEDGER | V-03/V-05 | V-01/V-02/V-04 |
| C-42 GATE E-COST references GATE D phase-earner sub-lists | V-03/V-05 | V-01/V-02/V-04 |
| C-43 GATE C exit names ROLE HANDOFF as blocking dest | V-01/V-04/V-05 | V-02/V-03 |

Note on C-42 dependency: C-42 is only reachable when C-41 is satisfied (GATE D must carry phase-attributed sub-lists for the sub-list cross-reference to be possible). V-05 satisfies both; V-03 satisfies both; all others satisfy neither.
