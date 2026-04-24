I now have sufficient data to score all five variations. Let me compile the full assessment.

---

## mock-accept R11 — Scorecard

**Rubric:** v11 (C-01–C-05 Essential, C-06–C-08 Recommended, C-09–C-39 Aspirational; denominator 31)
**Baseline:** R10 V-05 (31/31 → 100.0)

---

### Structural Inventory by Variation

Before scoring, one read-pass captures where each variation diverges from the baseline:

| Location | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| GATE B | R10 base (evaluation universe named) | **Three-bucket**: Auto-flagged named list + Evaluation universe named list + partition check | R10 base | Three-bucket (V-02) | Three-bucket (V-02) |
| GATE C → ROLE HANDOFF instruction | "Do not proceed to ROLE HANDOFF" | "Do not proceed to STEP 4" | "Do not proceed to STEP 4" | "Do not proceed to ROLE HANDOFF" | "Do not proceed to ROLE HANDOFF" |
| ROLE HANDOFF | **Bidirectional**: SCOREBOARD values + Arch-blocked list + Strategy universe + partition sum check | Minimal: Strategy universe only (R10 base) | Minimal: Strategy universe only (R10 base) | Bidirectional (V-01) | Bidirectional (V-01) |
| GATE D INERTIA LEDGER | Standard: REAL-REQUIRED + MOCK-ACCEPTED as flat lists | Standard | **Phase-attributed**: Architect-phase earners + Strategy-phase earners + total constraint | Standard | Phase-attributed (V-03) |
| GATE E-COST cross-reference | GATE C + GATE D tallies | GATE C + GATE D tallies | **GATE D phase-earner sub-lists** | GATE C + GATE D tallies | GATE D phase-earner sub-lists |
| GATE F | Format qualifiers (C-37 base) | Format qualifiers (C-37 base) | Format qualifiers (C-37 base) | Format qualifiers | Format qualifiers |

---

### Per-Criterion Scoring — All Variations

#### Essential (C-01–C-05) — PASS required for total composite

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| C-01 Artifact-as-subject in auto-flag rules | PASS — Rule A/B/C templates use "The mock artifact's [ns] section..." throughout | PASS — identical | PASS — identical | PASS | PASS |
| C-02 Forbidden triad completeness | PASS — All three rules present; "A two-of-three set does not satisfy this gate" guard explicit | PASS | PASS | PASS | PASS |
| C-03 CANARY ASSERTION + CANARY SUPPRESSED | PASS — CANARY ASSERTION with blank ___ target; CANARY SUPPRESSED branch defined for Edit-unavailable case | PASS | PASS | PASS | PASS |
| C-04 Single Write block for review artifact | PASS — STEP 9 instructs "Write all sections in ONE Write call. No sections outside this Write block." | PASS | PASS | PASS | PASS |
| C-05 Slot 1/Slot 2 separation with paraphrase named | PASS — STEP 7 separates Slot 1 (exact-token Reason) from Slot 2 (artifact-as-subject Basis); "paraphrase" named as violation class in both revert instructions | PASS | PASS | PASS | PASS |

**Essential verdict: PASS (all five variations)**

---

#### Recommended (C-06–C-08)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| C-06 Entity-naming in roles | PASS — Required artifact citation template: "The mock artifact's [namespace] section [field: X, token: Y, slot: Z]" in both STEP 3 and STEP 4 | PASS | PASS | PASS | PASS |
| C-07 Step sequencing and guard compliance | PASS — Named accumulator lists (Arch-blocked, Strategy-blocked) with VERDICT-ECHO; "Write 'Arch-blocked: none' if list is empty" guard | PASS | PASS | PASS | PASS |
| C-08 Eval-driven REAL-REQUIRED template | PASS — 5-field template per namespace: Namespace / Required artifact citation / Trigger condition+SQ / Artifact state / Verdict+Reason+Cost-of-MOCK / Required action; VERDICT-ECHO named | PASS | PASS | PASS | PASS |

**Recommended verdict: PASS (all five variations)**

---

#### Aspirational (C-09–C-39) — 31 total

All five variations inherit R10 V-05 as baseline (31/31 against v11). The R11 axis changes are additive — they strengthen structural verifiability without removing or weakening any existing criterion. Each criterion is assessed below with the key evidence line; where all five share identical text, the note applies universally.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|---|---|---|---|---|---|---|
| C-09 Artifact-as-subject grammar | PASS | PASS | PASS | PASS | PASS | STANDING RULE embedded at top of each variation; FAIL forms enumerated; active throughout all steps |
| C-10 Tier sourcing | PASS | PASS | PASS | PASS | PASS | STEP 1 CONSTRAINT: "Write exactly 'Tier: N (source: TOPICS.md \| --tier \| default)'" |
| C-11 Inline completeness gate | PASS | PASS | PASS | PASS | PASS | GATE A count assertion; GATE B count assertion with HALT |
| C-12 Reason-code enforcement at point of use | PASS | PASS | PASS | PASS | PASS | CONSTRAINT co-located at Verdict and Reason fields in STEP 3/STEP 4 templates |
| C-13 Phase exit assertions | PASS | PASS | PASS | PASS | PASS | "Do not proceed to STEP N until GATE X is written" language at every gate |
| C-14 Blank-line failure signal | PASS | PASS | PASS | PASS | PASS | All fill-in sites use ___ (blank) notation; absence readable by inspection |
| C-15 Forbidden-form enumeration | PASS | PASS | PASS | PASS | PASS | STANDING RULE enumerates "I found..." / "This namespace has..." / "There is no..." / "Coverage shows..." as forbidden alternatives |
| C-16 Written-gate blocking language | PASS | PASS | PASS | PASS | PASS | "HALT. Do not advance to STEP 2 until count confirmed" at every gate |
| C-17 Named gate registry | PASS | PASS | PASS | PASS | PASS | GATE A through GATE F (plus GATE E-COST) with stable sequential IDs |
| C-18 Adjacent framed CONSTRAINT co-location | PASS | PASS | PASS | PASS | PASS | Every constrained field has CONSTRAINT + HALT directly beneath, not in preamble |
| C-19 Universal blank-slot enforcement | PASS | PASS | PASS | PASS | PASS | ___ blanks in auto-flag rule output templates and CANARY ASSERTION |
| C-20 Halt-on-violation instruction | PASS | PASS | PASS | PASS | PASS | STANDING RULE includes "HALT. Delete the violating line. Rewrite in PASS form." |
| C-21 Per-section CONSTRAINT in review Write block | PASS | PASS | PASS | PASS | PASS | STEP 9 has per-section CONSTRAINT + HALT for Coverage, Structural records, Risk, Next Steps |
| C-22 Slot 1 paraphrase violation examples | PASS | PASS | PASS | PASS | PASS | Slot 1 revert names "sufficient coverage" and "domain realistic" as concrete quoted paraphrase violations |
| C-23 Three-step halt sequence | PASS | PASS | PASS | PASS | PASS | STANDING RULE: "HALT. Delete the violating line. Rewrite in PASS form." — three atomic imperatives |
| C-24 Gate-to-section traceability in GATE F | PASS | PASS | PASS | PASS | PASS | GATE F asserts each section by stable ID (Coverage / Structural records / Risk / Next Steps) |
| C-25 Slot 2 paraphrase violation examples | PASS | PASS | PASS | PASS | PASS | SLOT 2 VIOLATION TABLE contains three quoted near-miss forms with violation types |
| C-26 Halt co-location at each CONSTRAINT site | PASS | PASS | PASS | PASS | PASS | HALT lines co-located at every CONSTRAINT throughout all steps |
| C-27 GATE F as standalone dedicated numbered step | PASS | PASS | PASS | PASS | PASS | STEP 10 — GATE F COMPLETENESS CHECK occupies its own step, separate from STEP 9 Write |
| C-28 Slot 2 violation table | PASS | PASS | PASS | PASS | PASS | Structured two-column table (Quoted near-miss form / Violation type) in STEP 7 |
| C-29 Cost-of-MOCK field in evaluation record | PASS | PASS | PASS | PASS | PASS | Cost-of-MOCK field in STEP 3 and STEP 4 with constrained "Without real data for [namespace]..." format |
| C-30 DEFAULT DECISION POSITION block | PASS | PASS | PASS | PASS | PASS | DECISION SCOREBOARD declared before STEP 1 at REAL-REQUIRED: 9 / MOCK-ACCEPTED: 0 with inertia framing |
| C-31 INERTIA LEDGER at phase gates | PASS | PASS | PASS | PASS | PASS | INERTIA LEDGER — ARCHITECT PHASE EXIT at GATE C; INERTIA LEDGER — STRATEGY PHASE EXIT at GATE D; sum constraint + HALT at both |
| C-32 MOCK COST REGISTER as dedicated post-evaluation step | PASS | PASS | PASS | PASS | PASS | STEP 5 is a dedicated step with COST REGISTER ASSERTION and GATE E-COST |
| C-33 COST REGISTER phase-dimension column | PASS | PASS | PASS | PASS | PASS | Three-column table: Phase \| Namespace \| Cost-of-MOCK |
| C-34 COST REGISTER phase-first column order | PASS | PASS | PASS | PASS | PASS | Phase is leftmost; Architect rows before Strategy rows by explicit instruction |
| C-35 GATE E-COST per-phase count assertions | PASS | PASS | PASS | PASS | PASS | All variations have three-line GATE E-COST assertion (total + Architect rows + Strategy rows); V-03/V-05 reference GATE D phase-earner sub-lists directly |
| C-36 DECISION SCOREBOARD as live numeric tracker | PASS | PASS | PASS | PASS | PASS | DECISION SCOREBOARD UPDATE at GATE C; DECISION SCOREBOARD FINAL at GATE D with sum constraint |
| C-37 GATE F section format qualifiers | PASS | PASS | PASS | PASS | PASS | "Coverage: 4 columns / Structural records: 9 sentences / Risk: Urgency column / Next Steps: ordered list" in GATE F of all variations |
| C-38 GATE B enumerated partition output | PASS | PASS | PASS | PASS | PASS | All variations name the evaluation universe explicitly at GATE B; V-02/V-04/V-05 additionally enumerate the auto-flagged bucket as named list |
| C-39 ROLE HANDOFF block | PASS | PASS | PASS | PASS | PASS | Named ROLE HANDOFF block present in all variations; V-01/V-04/V-05 expanded (bidirectional); V-02/V-03 minimal (strategy universe) — both forms satisfy C-39 |

**Aspirational verdict: 31/31 PASS (all five variations)**

---

### Composite Scores

**Formula:** 90.0 (Essential + Recommended all PASS) + (Asp passes / 31) × 10

| Variation | Essential | Recommended | Asp passes | Asp score | **Total** |
|---|---|---|---|---|---|
| V-01 | 5/5 PASS | 3/3 PASS | 31/31 | 10.0 | **100.0** |
| V-02 | 5/5 PASS | 3/3 PASS | 31/31 | 10.0 | **100.0** |
| V-03 | 5/5 PASS | 3/3 PASS | 31/31 | 10.0 | **100.0** |
| V-04 | 5/5 PASS | 3/3 PASS | 31/31 | 10.0 | **100.0** |
| V-05 | 5/5 PASS | 3/3 PASS | 31/31 | 10.0 | **100.0** |

---

### Ranking

All five variations are structurally equivalent against v11. No v11 criterion distinguishes them. Ranking is by excellence signal density — how many candidate v12 criteria each variation introduces:

| Rank | Variation | C-40 candidate (bidirectional ROLE HANDOFF) | C-41 candidate (auto-flagged bucket at GATE B) | C-42 candidate (phase-attributed GATE D) | Score |
|---|---|---|---|---|---|
| 1 | **V-05** | YES | YES | YES | 100.0 — all three candidates |
| 2 | **V-04** | YES | YES | NO | 100.0 — two candidates |
| 3 | **V-01** | YES | NO | NO | 100.0 — one candidate (boundary axis) |
| 3 | **V-02** | NO | YES | NO | 100.0 — one candidate (output-format axis) |
| 3 | **V-03** | NO | NO | YES | 100.0 — one candidate (lifecycle axis) |

V-05 is the sole candidate for R11 golden. V-04 is silver. V-01/V-02/V-03 are equivalent single-axis probes at bronze.

---

### Excellence Signals from V-05

Three patterns that V-05 introduces beyond the current v11 golden:

**EX-1 — Bidirectional boundary record (C-40 candidate)**
V-05's ROLE HANDOFF carries four fields: DECISION SCOREBOARD values copied verbatim from GATE C UPDATE, Arch-blocked names (closed at REAL-REQUIRED, matched to GATE C INERTIA LEDGER), Strategy evaluation universe (entering STEP 4), and a partition sum check (`Arch-blocked + entering = GATE B non-flagged count`). The phase boundary is independently auditable without reading GATE C — not just who enters, but who was closed, how the SCOREBOARD moved, and that the two sets account for the complete evaluation universe. V-02's and V-03's minimal ROLE HANDOFF satisfies C-39 (names the entering universe) but requires reading GATE C to reconstruct the closed set. V-05 eliminates that cross-reference.

**EX-2 — Complete three-class GATE B partition record (C-41 candidate)**
V-05's GATE B names both the auto-flagged bucket (each namespace listed, count matched to total flags) and the evaluation universe bucket (each namespace listed, count matched to 9 - flags), with a partition check tying both to 9. All 9 namespaces appear at GATE B under exactly one named bucket. R10 V-05's GATE B (inherited by V-01/V-03) names only the evaluation universe — the auto-flagged namespaces must be traced back to STEP 2 Rule A/B/C outputs to verify. V-05 makes GATE B a complete three-class membership record, removing the STEP 2 cross-reference.

**EX-3 — Pre-register phase-attribution verification (C-42 candidate)**
V-05's GATE D INERTIA LEDGER breaks "Namespaces that have earned MOCK-ACCEPTED against inertia" into two sub-lists: `Architect-phase earners` (count-constrained against GATE C MOCK-ACCEPTED) and `Strategy-phase earners` (count-constrained against this gate's MOCK-ACCEPTED), plus a total sum check. This makes the Architect/Strategy MOCK-ACCEPTED split a required written assertion at GATE D, halt-blocked before STEP 5 runs. In V-01/V-02/V-04 (standard GATE D), the phase split is only verified retroactively inside GATE E-COST by cross-referencing GATE C. V-05 creates an independent verification layer one step earlier.

---

### New Patterns for v12 Rubric Extraction

| ID | Pattern | Location | What it adds over current v11 |
|---|---|---|---|
| C-40 | ROLE HANDOFF bidirectional partition record | ROLE HANDOFF | Closed set (Arch-blocked) + entering set + SCOREBOARD snapshot + sum constraint — boundary auditable without GATE C |
| C-41 | GATE B three-class named enumeration including auto-flagged | GATE B | Auto-flagged bucket named explicitly at GATE B — all 9 namespaces placed at GATE B without STEP 2 cross-reference |
| C-42 | GATE D phase-attributed INERTIA LEDGER | GATE D | Architect-earner / Strategy-earner sub-lists with count constraints — phase split verified and halt-blocked before COST REGISTER runs |

V-05 is the sole candidate R11 golden. All three candidate criteria would be extracted into v12. V-04 would score 34/34 (passes C-40, C-41, fails C-42). V-01/V-02/V-03 would score 33/34 on single axes.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["ROLE HANDOFF bidirectional partition record: closed set + entering set + SCOREBOARD snapshot + sum constraint makes phase boundary independently auditable without reading GATE C", "GATE B three-class named enumeration including auto-flagged bucket: all 9 namespaces placed under named buckets at GATE B, removing STEP 2 cross-reference for flagged namespace identity", "GATE D phase-attributed INERTIA LEDGER: Architect-earner and Strategy-earner sub-lists with count constraints create a pre-STEP-5 halt-blocked verification layer for the phase split, catching misattribution before COST REGISTER runs"]}
```
