I now have sufficient context to score all five variations. Let me do the full evaluation.

---

# Quest Score — corps-scan R12 (Rubric v11, 270 pts)

## Scoring Notes

**Invariants (C-41–C-44)**: All five variations treat these as structurally required. The variation axes govern HOW they are implemented, not whether. I verify each independently.

**Scoring key**: PASS = full pts | PARTIAL = half pts | FAIL = 0

---

## V-01 — Typed Field Declarations

### Essential (12 pts each)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Draft org.yaml block present | PASS | YAML block with org:/exec-office:/groups:/teams:/roles: present |
| C-02 | Team areas derived from repo | PASS | YAML names from Signal Schema "YAML name (C-02)" column; schema-traced |
| C-03 | Group structure present | PASS | groups: section with named group containers |
| C-04 | Standard roles per team | PASS | Named roles from schema; Inertia Advocate excluded and marked auto-added |
| C-05 | Does not write .craft/roles/ | PASS | ACKNOWLEDGED constraint + "no .craft/roles/ content here" in traceability statement |

**Essential subtotal: 60/60**

### Recommended (10 pts each)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-06 | Pivot mode declared with rationale | PASS | Net Score delta + DARK SIGNALS eliminator named in ROLE 3 as rationale |
| C-07 | Exec office placeholder present | PASS | exec-office: section with name and confirm note |
| C-08 | Amend options listed | PASS | AMEND-A/B/C with actionable commands |

**Recommended subtotal: 30/30**

### Aspirational (5 pts each)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-09 | Detection rationale per area | PASS | Signal Schema has Detection evidence (C-09) column per row |
| C-10 | Inertia Advocate noted | PASS | "# Inertia Advocate: auto-added by corps-build" in YAML + C-10 SCHEDULED in pre-check |
| C-11 | Pre-YAML scan inventory | PASS | Signal Schema before YAML block |
| C-12 | Draft boundary front-loaded | PASS | HARD BOUNDARY block is first substantive line |
| C-13 | Self-referential compliance check | PASS | "[ ] C-12 ... STATUS: CONFIRMED" in GATE pre-check |
| C-14 | Dual-stage YAML bracketing | PASS | GATE pre-check (pre-YAML) + POST-WRITE VERIFICATION (post-YAML) |
| C-15 | Rubric criteria embedded as skill requirements | PASS | Pre-check lists 10+ C-NN bundles as required outputs |
| C-16 | Debt-framed amend options | PASS | "Debt if skipped:" on all three amend options |
| C-17 | Forward commitment to future-section criteria | PASS | SCHEDULED items name delivering role |
| C-18 | Criterion ID as primary compliance key | PASS | C-NN IDs as primary keys throughout pre-check |
| C-19 | Post-write criterion self-labeling | PASS | POST-WRITE cites C-19/C-30/C-33/C-34 at point of satisfaction |
| C-20 | Structural role ordering as mechanical enforcement | PASS | "ROLE 2, ROLE 3, and ROLE 4 are blocked until ROLE 1 outputs" |
| C-21 | Schema-typed inventory with criterion-labeled columns | PASS | "YAML name (C-02)", "Proposed roles (C-04)", "Detection evidence (C-09)" in headers |
| C-22 | Pre-write section criterion self-labeling | PASS | Signal Schema header: "C-26: C-11 satisfier... C-22: criterion purpose declared in header" |
| C-23 | Pivot deliberation before selection | PASS | DELIBERATE PHASE / ROLE 3 runs before DRAFT PHASE |
| C-24 | Inertia Advocate at group level | PASS | "# Inertia Advocate governance (C-24):" on each group in YAML |
| C-25 | Universal output section self-labeling | PASS | Every section header carries C-NN annotation; "Universal labeling rule (C-25)" declared |
| C-26 | Multi-criterion section header | PASS | Signal Schema: "C-26: C-11+C-21 satisfier"; Post-Write: "C-14+C-30 satisfier" |
| C-27 | Pivot deliberation tri-part | PASS | Weight table: Evidence For / DARK SIGNALS Penalty / Net+Verdict = tri-part equivalent |
| C-28 | Forward-committed items carry exec-state marker | PASS | CONFIRMED/SCHEDULED/ACKNOWLEDGED on every item |
| C-29 | Criterion-pair bundling in pre-check | PASS | Compound bundles: "C-38+C-41", "C-11+C-21+C-22+C-25+C-26", etc. |
| C-30 | Post-write as multi-criterion declaration | PASS | POST-WRITE cites 10 criteria simultaneously |
| C-31 | Purpose-named phase pipeline | PASS | GATE PHASE / SCAN PHASE / DELIBERATE PHASE / DRAFT+FINALIZE PHASE |
| C-32 | Three-state execution vocabulary | PASS | CONFIRMED / SCHEDULED / ACKNOWLEDGED all present on items |
| C-33 | Multi-criterion headers at pre-YAML and post-YAML | PASS | "C-11+C-21" at SCAN (pre-YAML); "C-14+C-30" at POST-WRITE (post-YAML) |
| C-34 | Post-write includes essential-tier criterion | PASS | C-02 cited in POST-WRITE alongside aspirational criteria |
| C-35 | ACKNOWLEDGED on essential boundary constraint | PASS | "C-05 STATUS: ACKNOWLEDGED — essential failure if violated" |
| C-36 | DARK SIGNALS structured inventory | PASS | Four typed entry types with mode impact per entry |
| C-37 | DARK SIGNALS cross-referenced in deliberation+amend | PASS | Penalty column uses labels; AMEND-A cites "DARK SIGNALS basis (C-37)" |
| C-38 | Hypothesis in gate phase before scan | PASS | Typed Hypothesis Claim precedes SCAN PHASE |
| C-39 | DARK SIGNALS per-entry hypothesis relation | PASS | "Hypothesis Relation: [apply STATE_ENUM above]" on every entry |
| C-40 | Amend options carry hypothesis status | PASS | AMEND-A: "Hypothesis verdict (C-40): YES -- CONFIRMED / YES -- OVERTURNED" |
| C-41 | Hypothesis as 3-field contract | PASS | PREDICTED-MODE / STRUCTURAL-PREDICTION / FALSIFICATION-SIGNAL with type annotations |
| C-42 | IS-FALSIFICATION-SIGNAL 4-state | PASS | STATE_ENUM declared at DARK SIGNALS header; all 4 states defined |
| C-43 | Weight-scoring table with DARK SIGNALS Penalty | PASS | Column "DARK SIGNALS Penalty [label:string, magnitude:0-4]" with labeled cells |
| C-44 | Amend carries Net Score delta | PASS | AMEND-A: "Net Score arithmetic (C-44): selected Net=N vs runner-up Net=N; delta=N (independently verifiable)" |

**Aspirational subtotal: 180/180**

**V-01 Total: 270/270**

---

## V-02 — Inertia-First Framing

### Essential: 60/60 (same structural pattern; all pass)

### Recommended: 30/30 (all pass)

### Aspirational

| ID | Result | Note |
|----|--------|------|
| C-09–C-25 | PASS | Same foundations; Inertia framing adds to, does not break, any criterion |
| C-26 | PASS | "C-11+C-21" pre-YAML; "C-14+C-30" post-YAML |
| C-27 | PASS | Weight table covers tri-part; Inertia Cost column adds a 5th dimension |
| C-28–C-35 | PASS | Three-state vocabulary; compound bundles; 10-criteria post-write with C-02 essential; ACKNOWLEDGED on C-05 |
| C-36 | PASS | DARK SIGNALS section with mode impact per entry |
| C-37 | PASS | DARK SIGNALS labels in Penalty column; AMEND-A cites label |
| C-38–C-40 | PASS | Hypothesis in GATE; per-entry Hypothesis Relation; hypothesis verdict in AMEND-A |
| C-41 | PASS | 3-field contract with Inertia Advocate context framing in GATE |
| C-42 | PASS | 4-state vocabulary inline in DARK SIGNALS header; Inertia Implication sub-field additional |
| C-43 | PASS | Weight table with DARK SIGNALS Penalty column AND Inertia Cost column (exceeds criterion) |
| C-44 | PASS | AMEND-A: Net Score delta + Inertia Advocate migration burden (exceeds criterion) |

**V-02 Total: 270/270**

**V-02 distinctive feature**: Inertia Cost column in C-43 table is the only new structural column not required by any current criterion. Inertia migration burden in AMEND-A exceeds C-44 minimum. C-24 implemented at GATE/DARK SIGNALS/deliberation/YAML levels simultaneously — strongest C-24 implementation across all variations.

---

## V-03 — Scan-Compressed, Deliberation-Expanded

### Essential: 60/60 (standard structure; all pass)

### Recommended: 30/30 (all pass)

### Aspirational

| ID | Result | Note |
|----|--------|------|
| C-09–C-25 | PASS | Minimal GATE/SCAN still satisfies all pre-YAML criteria |
| C-26 | PASS | "C-11+C-21" at SCAN header; "C-14+C-30" at POST-WRITE |
| C-27 | PASS | 8-column table covers tri-part assessment |
| C-28–C-35 | PASS | Same structural vocabulary as V-01/V-02; compound bundles; C-35 confirmed |
| C-36 | PASS | DARK SIGNALS section (compact form) |
| C-37 | PASS | Labels in Penalty column; AMEND-A cites label |
| C-38–C-40 | PASS | Hypothesis in GATE; Hypothesis Relation per entry; verdict in AMEND-A |
| C-41 | PASS | Compact 3-field claim (no type annotations — still all 3 fields labeled) |
| C-42 | PASS | 4-state vocabulary declared at DARK SIGNALS header: "YES -- CONFIRMED / YES -- OVERTURNED / NO -- corroborates-alternative / NO -- neutral" |
| C-43 | PASS | 8-column table: Evidence For + Signal Strength sub-scoring + DARK SIGNALS Penalty + Base/Penalty/Net/Verdict |
| C-44 | PASS | AMEND-A: "Selection Proof delta (C-44): Delta=N ... (see ROLE 3 Selection Proof — independently verifiable)" |

**V-03 Total: 270/270**

**V-03 distinctive feature**: Selection Proof block in DELIBERATE PHASE traces full Net Score arithmetic for winner and runner-up before AMEND-A references it — the delta is independently verifiable from a source artifact rather than appearing first in the amend option. This exceeds C-44 minimum. Signal Strength sub-column in 8-column table adds sub-scoring granularity not required by C-43.

---

## V-04 — Conversational Imperative Register

### Essential: 60/60

### Recommended: 30/30

### Aspirational — key register-transformation checks

| ID | Result | Note |
|----|--------|------|
| C-25 | PASS | Every section carries C-NN annotation even in imperative register: `(C-20: structural gate; C-31: GATE PHASE; C-25: self-labeled)` |
| C-31 | PASS | "STEP 1 — GATE: Make Your Pre-Check and Claim" — semantic purpose name present after STEP prefix; annotation confirms "C-31: GATE PHASE" |
| C-32 | PASS | Three-state vocabulary preserved: "Three states: CONFIRMED = done now / SCHEDULED = done in a later step / ACKNOWLEDGED = noted" |
| C-42 | PASS | 4-state vocabulary presented as numbered "choose one:" list — all four states defined; meets definition + 2-distinct-state requirement |
| C-43 | PASS | Weight table preserves "DARK SIGNALS Penalty" column label with DARK SIGNALS label cells; plain-English scoring guide satisfies quantitative requirement |
| C-44 | PASS | AMEND-A: "What the scoring said (C-40+C-44): hypothesis was ...; winner Net=N vs runner-up Net=N; delta=N" |
| C-29 | PASS | Compound bundles preserved in conversational pre-check: "C-38+C-41", "C-11+C-21+C-22+C-25+C-26", etc. |
| C-41 | PASS | "HYPOTHESIS CLAIM" block uses 3-field structure as "fill in" prompts; all three fields explicitly labeled |
| C-09–C-24, C-26–C-28, C-30, C-33–C-40 | PASS | Register transformation preserves all structural criterion implementations |

**V-04 Total: 270/270**

**V-04 distinctive feature**: Demonstrates that criterion coverage is register-invariant — no criterion structurally requires formal technical prose. The numbered "choose one:" list for C-42 vocabulary is the most accessible presentation pattern across all variations. No new structural patterns beyond register transformation.

---

## V-05 — Combination (V-01 + V-02 + V-03)

### Essential: 60/60

### Recommended: 30/30

### Aspirational

| ID | Result | Note |
|----|--------|------|
| C-09–C-25 | PASS | Inherits all pre-YAML foundations from constituent axes |
| C-26 | PASS | "C-11+C-21" at SCAN header; "C-14+C-30" at POST-WRITE |
| C-27 | PASS | 9-column table covers tri-part and more |
| C-28–C-35 | PASS | Three-state vocabulary; compound bundles; C-35 confirmed; 10-criteria post-write |
| C-36 | PASS | DARK SIGNALS section with mode impact |
| C-37 | PASS | Labels in Penalty column (structural enforcement); AMEND-A cites label |
| C-38–C-40 | PASS | Full hypothesis lifecycle: GATE claim → DARK SIGNALS per-entry → verdict in AMEND-A |
| C-41 | PASS | Typed 3-field contract with Inertia Advocate context framing: STRUCTURAL-PREDICTION type note includes Inertia framing |
| C-42 | PASS | STATE_ENUM declared at DARK SIGNALS header (V-01 pattern) + Inertia Implication sub-field (V-02 pattern) on every entry |
| C-43 | PASS | 9-column table: Signal Strength + DARK SIGNALS Penalty [label:string, magnitude:0-4] + Inertia Cost — typed column annotations on all columns |
| C-44 | PASS | AMEND-A carries Selection Proof delta (V-03 reference pattern) AND Inertia migration burden (V-02 pattern) simultaneously |

**V-05 Total: 270/270**

---

## Composite Scores and Ranking

| Rank | Variation | Score | Key differentiator |
|------|-----------|-------|--------------------|
| 1 | **V-05** (Combination) | **270/270** | Highest criterion-density output; 3 new patterns not in any existing criterion |
| 2 | **V-01** (Typed field declarations) | **270/270** | Type annotations make C-41/C-42/C-43 machine-readable at definition sites |
| 3 | **V-02** (Inertia-first) | **270/270** | Inertia Cost column + migration burden in AMEND-A exceed C-43/C-44 minimum |
| 3 | **V-03** (Deliberation-expanded) | **270/270** | Selection Proof block makes C-44 delta independently verifiable pre-AMEND |
| 5 | **V-04** (Conversational) | **270/270** | Register transformation demonstration; no new structural patterns |

All 5 essential criteria pass in all variations. No variation drops below 270.

---

## Excellence Signals (V-05 top scorer)

Three patterns from V-05 exceed all existing criteria and are candidates for R13 codification:

**Signal 1 — Selection Proof as standalone delta-trace artifact**
V-03/V-05 produce a named "Selection Proof" block in DELIBERATE PHASE that traces full Net Score arithmetic for winner and runner-up before AMEND-A references it. C-44 requires the delta in AMEND-A; V-05 makes the delta independently verifiable from a primary source (Selection Proof) that the amend option cites by name. Pattern: "C-44 delta appears first as a named arithmetic trace in DELIBERATE PHASE; AMEND-A reproduces it by reference, not by repetition."

**Signal 2 — Inertia Cost column as second structural column in weight table**
V-02/V-05 add an Inertia Cost column alongside the DARK SIGNALS Penalty column. C-43 requires only the DARK SIGNALS Penalty column. The Inertia Cost column captures what the Inertia Advocate structurally loses if each mode is selected — a second non-bypassable column type whose cell values are forced by the presence of the Advocate in prior phases. Pattern: "C-43 table carries two structural columns: DARK SIGNALS Penalty (evidence-driven) + Inertia Cost (governance-driven)."

**Signal 3 — 3-dimension DARK SIGNALS entry: mode impact + IS-FALSIFICATION-SIGNAL + Inertia Implication**
V-02/V-05 give each DARK SIGNALS entry three orthogonal analytical dimensions: (1) which pivot mode(s) the absence rules out or weakens (C-36); (2) the IS-FALSIFICATION-SIGNAL STATE_ENUM classification (C-42); (3) the Inertia Implication sub-field — what the Inertia Advocate loses if the signal is absent. The third dimension is not required by any current criterion and makes the DARK SIGNALS section simultaneously a pivot evidence instrument, a hypothesis testing instrument, and an Advocate planning instrument.

---

```json
{"top_score": 270, "all_essential_pass": true, "new_patterns": ["Selection Proof block in DELIBERATE PHASE as primary delta-trace artifact — AMEND-A reproduces it by reference, making C-44 delta independently verifiable before the amend option cites it", "Inertia Cost column as second structural column in C-43 weight table alongside DARK SIGNALS Penalty — forces Advocate governance consequence at data-entry stage", "3-dimension DARK SIGNALS entry: mode-impact (C-36) + IS-FALSIFICATION-SIGNAL STATE_ENUM (C-42) + Inertia Implication sub-field — DARK SIGNALS as simultaneous pivot evidence, hypothesis testing, and Advocate planning instrument"]}
```
