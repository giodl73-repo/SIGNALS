Done. Here's the R7 design summary:

---

## Round 7 — 5 Variations

**Target:** 16/16 aspirational (100.0) under v7. Three new criteria implemented in every variation.

| V | Axis | A-14 (I-NN pool) | A-15 (inertia observability) | A-16 (routing table role) |
|---|------|------------------|------------------------------|---------------------------|
| **V-01** | Role sequence | FRAMER Step 3: 2+ I-NN rows, same columns as F-NN | Dedicated `Inertia pathway observability` field in FRAMER | SYNTHESIZER role, 5-row routing table |
| **V-02** | Output format | Parallel dual-pool tables (F-NN / I-NN identical columns throughout) | Pool-level header block: first field before I-NN rows | AUDITOR role, 4-row routing table |
| **V-03** | Lifecycle emphasis | I-NN pool generated in Step 2 — before claim extraction exists | Step 1: inertia observability label before any F-NN work | EVALUATOR role, 5-row routing table (adds inertia-observability as 5th row) |
| **V-04** | Phrasing register | Q3.5 interrogative ("What pathways could produce Y without X?") elicits pool | Q3.3 direct question ("Can we detect whether Y occurs without X?") | EXAMINER role, 4-row routing table |
| **V-05** | Combination | I-NN derived from counter-hypothesis chain hop challenges | Aggregate of counter-hypothesis hop labels (emergent) | AUDITOR role, 5-row routing table + triple-gap diagnostic |

**Key new structural innovations in R7:**

- **V-01 SYNTHESIZER vs R6-V-02 AUDITOR:** SYNTHESIZER adds a 5th routing row (I-NN pool coverage → Mechanism slot) and explicitly owns all four new criteria simultaneously, not just A-12/A-13.

- **V-03 inertia-first lifecycle:** The first variation where I-NN conditions are generated without knowledge of the F-NN pool. Tests whether independence from the claim produces more mechanistically diverse inertia conditions.

- **V-05 counter-hypothesis chain:** I-NN conditions derive from CH-Hop challenges rather than table seeding. Each I-NN condition is structurally anchored to a specific inertia mechanism hop. Inertia pathway observability emerges as an aggregate (same computation as chain observability pattern, applied to the counter-hypothesis chain).

- **V-05 triple-gap diagnostic:** New joint finding beyond R6-V-05's double-blind gap. A triple gap is a condition where mechanism hop is Opaque AND testability is Unknown AND an I-NN condition with overlapping scope exists — all three simultaneously. Neither A-12, A-13, nor A-14 surfaces this co-occurrence alone.

**R8 question seeded:** Does chain-seeded I-NN derivation (V-05) produce more mechanistically specific conditions than table-seeded derivation (V-01–V-04)? Test by running same hypothesis through both and comparing I-NN condition quality.
 inertia, I-NN pool)
- V-02: AUDITOR role, 4-row routing table (chain-obs, testability, evidence, inertia)
- V-03: EVALUATOR role, 5-row routing table (adds inertia-observability as 5th row)
- V-04: EXAMINER role, 4-row routing table — same rows as V-02 AUDITOR
- V-05: AUDITOR role, 5-row routing table including triple-gap diagnostic

**R7 questions seeded from R6 excellence signals:**
- Does SYNTHESIZER (V-01) produce more coherent routing decisions than AUDITOR (V-02) because it
  explicitly owns all four diagnostics simultaneously vs. two?
- Does the parallel dual-pool table architecture (V-02) help analysts generate richer I-NN pools
  by making the structural parallelism with F-NN visually explicit?
- Does inertia-first ordering (V-03) change the mechanism pathway analysis — does seeing the
  counter-hypothesis first cause analysts to weight inertia evidence more heavily?
- Does interrogative phrasing (V-04) surface I-NN conditions that imperative prompts suppress?
  Specifically, does "What else might cause Y without X?" generate different conditions than
  a table template starting from "I-01: Y occurs at [baseline] without X via..."?
- Does the counter-hypothesis mini-chain (V-05) produce more mechanistically specific I-NN
  conditions (tied to identifiable causal steps) than a table-seeded approach (V-01–V-04)?

---

## V-01: SYNTHESIZER Role (Unified Diagnostic Aggregator)

**Axis:** Role sequence — a named SYNTHESIZER role runs between SKEPTIC and FRAMER (closing).
SYNTHESIZER owns all four diagnostic computations simultaneously: chain observability aggregate
(A-12), testability refinement yield (A-13), I-NN pool synthesis (A-14), and inertia pathway
observability confirmation (A-15). SYNTHESIZER produces a single consolidated 5-row AMEND
routing table (A-16). No other role computes aggregates or routes AMEND slots. FRAMER (closing)
constructs the AMEND block mechanically from SYNTHESIZER's routing table.

**Hypothesis:** Distributing diagnostic aggregation across sections (V-01–V-05 in R6) produces
correct outputs but requires the analyst to track diagnostic signals in separate locations.
Consolidating all four diagnostics into a single named role — one that runs with simultaneous
visibility into FRAMER's falsification pools and ANALYST's hop labels — produces a diagnostic
layer with less tracking overhead and stronger routing coherence. The cost is a longer role
sequence (five roles vs. four in R6-V-02); the benefit is that A-14/A-15/A-16 are co-located
in a single role output rather than scattered across sections and role outputs.

```
You are running /discover-causal.
Your input is a feature hypothesis of the form "X causes Y."
Five roles in sequence. Complete each role fully before advancing.
Every classification judgment uses a discrete label from a fixed set with a rationale line.

Roles:
  FRAMER (opening): claim, F-NN pool, I-NN pool, inertia observability, evidence,
    testability refinement, baseline estimate.
  ANALYST: mechanism chain with hop observability. Does not compute aggregates.
  SKEPTIC: adversarial challenge, confidence labels, final mechanism strength.
  SYNTHESIZER: all four diagnostic aggregations plus consolidated AMEND routing table.
    Runs after SKEPTIC, before FRAMER (closing). Does not challenge mechanism.
  FRAMER (closing): scoped claim, AMEND from SYNTHESIZER routing table.

Two-pool falsification design:
  F-NN pool: claim-derived conditions. Generated in FRAMER Step 2. Testability = Unknown.
  I-NN pool: inertia-derived conditions. Generated in FRAMER Step 3. Testability = Unknown.
Both pools undergo testability refinement in FRAMER Step 4 (evidence).
Both pools receive confidence labels from SKEPTIC.
SYNTHESIZER synthesizes both pools into diagnostic outputs.

---

## FRAMER (OPENING)

[Establish the claim, generate both falsification pools, label inertia pathway observability,
gather evidence, and run testability refinement. All conditions start testability = Unknown.
FRAMER does not assign confidence (SKEPTIC's job) or compute aggregates (SYNTHESIZER's job).]

### Step 1: Claim

X (the cause): [Extract from input]
Y (the claimed outcome): [Extract from input]
Full claim: ["X causes Y" -- one sentence, no mechanism embedded]

### Step 2: F-NN Pool (claim-derived falsification conditions)

[From the claim alone. At least two conditions. Testability = Unknown at generation.
No confidence column -- SKEPTIC fills that in Step 5.]

| ID   | Falsification condition (claim false if observed)     | Testability          | Rationale |
|------|-------------------------------------------------------|----------------------|-----------|
| F-01 | [What observable state would show X does not cause Y?] | Unknown (see Step 4) | [1 sentence: what mechanism failure does this expose?] |
| F-02 | [A second distinct condition. Add F-NN as needed.]     | Unknown (see Step 4) | [1 sentence] |

### Step 3: I-NN Pool and Inertia Analysis

[Establish the baseline. Generate at least two I-NN conditions naming distinct pathways by
which Y could occur without X. Each I-NN condition identifies a specific inertia mechanism.
Then label the inertia pathway observability: can we detect whether status quo produces Y?]

Status-quo description: [One sentence: what happens today without X?]
Baseline rate: [Estimate or bound: "Y occurs in approximately __% of cases without X."
  Or: "Unknown -- no measurement available."]

I-NN Pool (inertia falsification conditions):
[At least two I-NN conditions. Each names a specific pathway by which Y occurs without X.
Same structure as F-NN: testability = Unknown at genesis, no confidence yet.]

| ID   | Inertia falsification condition                          | Testability          | Rationale |
|------|----------------------------------------------------------|----------------------|-----------|
| I-01 | Y occurs at [baseline rate] without X via [mechanism 1]  | Unknown (see Step 4) | [1 sentence: what makes this pathway plausible?] |
| I-02 | [Distinct inertia pathway: Y via [mechanism 2] without X] | Unknown (see Step 4) | [1 sentence] |
[Add I-NN as the inertia analysis generates more pathways. Each condition should name a distinct mechanism.]

Inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP
  (SAFE = status quo does not produce Y;
   ADVISORY = partially produces Y for some users or conditions;
   STOP = status quo plausibly already produces Y at a meaningful rate)
Inertia severity rationale: [1 sentence]

Inertia pathway observability: [ ] Observable  [ ] Partial  [ ] Opaque
  (Observable = direct measurement of Y rate without X is available;
   Partial = proxy data available, no direct measurement;
   Opaque = no path to observe whether status quo produces Y without X)
Inertia observability rationale: [1 sentence: what instrumentation or data would close this gap?]
Inertia observability note: [This label is independent of mechanism hop observability.
  A mechanism chain may be fully Observable while the inertia path is Opaque -- they answer
  different questions: "how does X cause Y?" vs. "can we see whether Y already occurs?"]

[I-NN conditions added here; return to Step 4 to fill their testability.]

### Step 4: Evidence and Testability Refinement

[At least one context-specific observation, OR explicit "None found" -- no skipping.]

Evidence entry 1:
  Source type: [ ] Prior result  [ ] Analogous case  [ ] Domain observation  [ ] Counter-evidence
  Observation: [What was seen, where, when?]
  Bearing on X->Y: [1 sentence: supports, complicates, or challenges the claim?]

[Add entries as needed.]

Evidence quality: [ ] Strong  [ ] Moderate  [ ] Weak  [ ] None
Evidence quality rationale: [1 sentence]

Testability refinement pass -- all F-NN and I-NN conditions:
[For each condition, record testability determination after evidence.]

| ID   | Testability after evidence       | Refinement rationale |
|------|----------------------------------|---------------------|
| F-01 | [ ] Easy  [ ] Hard  [ ] Unknown  | [1 sentence: what enabled or blocked the determination?] |
| F-02 | [ ] Easy  [ ] Hard  [ ] Unknown  | [1 sentence] |
| I-01 | [ ] Easy  [ ] Hard  [ ] Unknown  | [1 sentence] |
| I-02 | [ ] Easy  [ ] Hard  [ ] Unknown  | [1 sentence] |
[Mirror all F-NN and I-NN conditions.]

Testability refinement yield:
  testability_refined_count: [Count of conditions moved from Unknown to Easy or Hard]
  testability_residual_unknown_count: [Count still Unknown after evidence]
  Residual Unknown IDs: [List by ID, or "None"]
  F-NN residual count: [Count]
  I-NN residual count: [Count]
  [SYNTHESIZER will aggregate these pool-level breakdowns.]

Confidence revisions: [Any F-NN/I-NN confidence label updates from evidence. Or: "None."]

FRAMER (OPENING) GATE:
[ ] X and Y extracted separately
[ ] At least two F-NN conditions (testability Unknown, no confidence column)
[ ] At least two I-NN conditions with IDs, testability Unknown, and rationale
[ ] Baseline rate declared (estimate, bound, or explicit "Unknown")
[ ] Inertia severity label assigned with rationale
[ ] Inertia pathway observability label assigned with rationale (Observable/Partial/Opaque)
[ ] Evidence populated (or explicit "None found" -- not skipped)
[ ] Evidence quality label assigned with rationale
[ ] Testability refinement completed for all F-NN and I-NN conditions
[ ] testability_refined_count and testability_residual_unknown_count declared with pool breakdown

--- Do not advance to ANALYST until all gate items are checked. ---
--- IF inertia severity is STOP: skip ANALYST; advance to SKEPTIC. ---

---

## ANALYST

[Map the causal chain from X to Y. Two hops minimum. Every hop carries: observability label,
observability rationale, evidence coherence, falsification connection to an F-NN or I-NN.
ANALYST does NOT assign confidence (SKEPTIC), testability (FRAMER), or aggregates (SYNTHESIZER).
ANALYST does NOT compute the chain observability aggregate -- SYNTHESIZER does that.]

Mechanism chain: [Two hops minimum. State mechanism only -- no adversarial content here.]

  Hop 1: X [name] -> [intermediate A]: [How does X produce A?]
    Observability: [ ] Observable  [ ] Partial  [ ] Opaque
    Observability rationale: [1 sentence: how directly can this intermediate be detected?]
    Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
    Falsification connection: [F-NN or I-NN ID. One sentence: if this hop fails, this condition holds.]

  Hop 2: [intermediate A] -> Y: [How does A produce Y?]
    Observability: [ ] Observable  [ ] Partial  [ ] Opaque
    Observability rationale: [1 sentence]
    Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
    Falsification connection: [F-NN or I-NN ID. One sentence.]

  [Add Hop 3+ as needed. Every hop: observability label + rationale, evidence coherence,
  falsification connection to a pre-existing F-NN or I-NN from FRAMER.]

Mechanism strength (preliminary): [ ] Strong  [ ] Moderate  [ ] Weak
Preliminary rationale: [1 sentence: ANALYST's pre-challenge assessment.]

ANALYST GATE:
[ ] At least two hops filled
[ ] Every hop: observability label + rationale, evidence coherence, falsification connection
[ ] Mechanism strength (preliminary) assigned with rationale
[ ] No confidence labels assigned (SKEPTIC's job)
[ ] No chain observability aggregate computed (SYNTHESIZER's job)
[ ] No adversarial content in this section

--- Do not advance to SKEPTIC until all gate items are checked. ---

---

## SKEPTIC

[Challenge every hop. Assign confidence labels to all F-NN and I-NN conditions. Deliver final
mechanism strength. SKEPTIC does not compute aggregates (SYNTHESIZER) or reassign testability
(FRAMER). SKEPTIC sees FRAMER's testability labels and carries them forward unchanged.]

Hop-by-hop challenge:

  Hop 1 challenge:
    What breaks X -> [intermediate A]? [Observable condition that disproves this hop]
    Observable test: [What to measure or detect]
    Alternative at this hop: [What else produces [intermediate A] without X?]
    Confidence: [ ] High  [ ] Medium  [ ] Low
    Confidence rationale: [1 sentence]

  Hop 2 challenge:
    What breaks [intermediate A] -> Y? [Observable condition]
    Observable test: [What to measure or detect]
    Alternative at this hop: [What else produces Y without [intermediate A]?]
    Confidence: [ ] High  [ ] Medium  [ ] Low
    Confidence rationale: [1 sentence]

  [Mirror all ANALYST hops.]

Confounders:
  Confounder 1: [Variable correlating with both X and Y. Name and describe.]

Inertia challenge:
  Adversarial view: [Could baseline effects or I-NN pathways explain observed Y?]
  Reference I-NN: [Which I-NN condition, if true, is most dangerous to the claim?]
  Revised inertia severity: [ ] Confirms FRAMER  [ ] Upgrades to ADVISORY  [ ] Upgrades to STOP

Final falsification table (FRAMER testability + SKEPTIC confidence):

| ID   | Condition text      | Testability (FRAMER)   | Confidence (SKEPTIC)        | Rationale |
|------|---------------------|------------------------|-----------------------------|-----------|
| F-01 | [text]              | [FRAMER Step 4 label]  | [ ] High  [ ] Med  [ ] Low  | [1 sentence] |
| F-02 | [text]              | [FRAMER Step 4 label]  | [ ] High  [ ] Med  [ ] Low  | [1 sentence] |
| I-01 | [text]              | [FRAMER Step 4 label]  | [ ] High  [ ] Med  [ ] Low  | [1 sentence] |
| I-02 | [text]              | [FRAMER Step 4 label]  | [ ] High  [ ] Med  [ ] Low  | [1 sentence] |
[Mirror all conditions. Testability column carries FRAMER labels unchanged.]

Mechanism strength (final): [ ] Strong  [ ] Moderate  [ ] Weak  [ ] NA (STOP)
Final rationale: [1 sentence. State whether changed from ANALYST preliminary and why.]

SKEPTIC GATE:
[ ] Every hop challenged with observable test and alternative
[ ] Confidence assigned to all F-NN and I-NN conditions
[ ] Final falsification table complete with FRAMER testability carried unchanged
[ ] Inertia challenge references at least one I-NN condition by ID
[ ] Final mechanism strength declared with rationale
[ ] At least one confounder named

--- Do not advance to SYNTHESIZER until all gate items are checked. ---

---

## SYNTHESIZER

[SYNTHESIZER is a diagnostic role, not an analysis role. It reads ANALYST's hop observability
labels, FRAMER's testability yield data, FRAMER's I-NN pool, and FRAMER's inertia observability
label. SYNTHESIZER computes four diagnostics and produces a single consolidated AMEND routing
table. SYNTHESIZER does not challenge mechanism, assign confidence, or propose scope.]

### Diagnostic 1: Chain Observability Aggregate

[Tally hop observability labels from ANALYST. Derive chain-level pattern.]

| Hop   | Mechanism step              | Observability (from ANALYST)    |
|-------|-----------------------------|---------------------------------|
| Hop 1 | X -> [intermediate A]       | [Observable / Partial / Opaque] |
| Hop 2 | [intermediate A] -> Y       | [Observable / Partial / Opaque] |
[Mirror all ANALYST hops.]

Observable hops: [Count]
Partial hops:    [Count]
Opaque hops:     [Count]
Total hops:      [Count]

Chain observability pattern: [ ] AllObservable  [ ] Mixed  [ ] PredominantlyOpaque
Pattern rationale: [1 sentence: what does this distribution mean for mechanism testability?]

### Diagnostic 2: Testability Refinement Yield

testability_refined_count (from FRAMER):  [Value]
testability_residual_unknown_count (from FRAMER): [Value]
Residual Unknown IDs: [From FRAMER, or "None"]
F-NN residual: [Count]  |  I-NN residual: [Count]
Pool asymmetry note: [One sentence: are I-NN conditions disproportionately Unknown-testability?
  Or: "No asymmetry detected."]
Yield quality: [ ] AllResolved  [ ] PartiallyResolved  [ ] Unresolved
Yield quality rationale: [1 sentence]

### Diagnostic 3: I-NN Pool Synthesis

I-NN condition count: [Total I-NN conditions from FRAMER]
I-NN conditions with Unknown testability after refinement: [List IDs, or "None"]
I-NN conditions with Low confidence from SKEPTIC: [List IDs, or "None"]
Pool coverage assessment: [ ] Comprehensive  [ ] Adequate  [ ] Minimal
  (Comprehensive = multiple distinct inertia pathways named with different mechanisms;
   Adequate = at least two conditions, plausibly covering main pathways;
   Minimal = conditions are restatements or cover only one pathway)
Pool coverage rationale: [1 sentence]
Most dangerous I-NN condition: [ID and one-sentence rationale: which, if true, most threatens claim?]

### Diagnostic 4: Inertia Pathway Observability

Inertia pathway observability (from FRAMER): [Observable / Partial / Opaque]
Inertia observability rationale: [Restate or elaborate FRAMER's rationale in 1 sentence]
Comparison to chain pattern: [One sentence: does inertia observability diverge from chain
  observability pattern? E.g., "Chain is AllObservable but inertia path is Opaque -- the
  mechanism is visible but the counterfactual is not."]

### Consolidated AMEND Routing Table

[All conditional AMEND decisions in one table. FRAMER (closing) includes only Required slots.]

| # | Diagnostic                   | Result                               | AMEND slot      | Routing               |
|---|------------------------------|--------------------------------------|-----------------|-----------------------|
| 1 | Chain observability pattern  | [AllObservable / Mixed / PredominantlyOpaque] | Observability | [Required if Mixed or PredominantlyOpaque / Not required] |
| 2 | Testability residual count   | [residual_unknown_count]             | Testability     | [Required if count > 0 / Not required] |
| 3 | Evidence quality             | [Strong / Moderate / Weak / None]    | Evidence        | [Required if None / Not required] |
| 4 | Inertia severity             | [SAFE / ADVISORY / STOP]             | Inertia         | [Required if ADVISORY or STOP / Not required] |
| 5 | I-NN pool coverage           | [Comprehensive / Adequate / Minimal] | Mechanism       | [Required if Minimal / Not required] |

SYNTHESIZER diagnostic note: [One sentence: what is the most critical gap across all four
  diagnostics? Which single finding, if unaddressed, most endangers the causal claim?]

SYNTHESIZER GATE:
[ ] Four diagnostics complete (chain aggregate, testability yield, I-NN pool, inertia observability)
[ ] AMEND routing table: all 5 rows filled with result and routing decision
[ ] Pool asymmetry note present (I-NN vs F-NN residual breakdown)
[ ] Inertia vs. chain observability comparison sentence present
[ ] At least one row marked Required (if none, flag as anomaly for FRAMER)

--- Do not advance to FRAMER (CLOSING) until all gate items are checked. ---

---

## FRAMER (CLOSING)

[Construct the scoped claim and AMEND block from SYNTHESIZER's routing table.
AMEND slots are generated mechanically from SYNTHESIZER rows marked Required.
Always include Narrow and Mechanism. Include all Required conditional slots.]

Scoped claim: ["X causes Y when [condition], for [population], assuming [precondition]."]
Scope condition: [Reference ANALYST mechanism and SKEPTIC adversarial findings.]
Out-of-scope: [At least one context where mechanism fails, from SKEPTIC challenge.]

Final inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP
Final inertia rationale: [1 sentence. Use SKEPTIC's revised verdict if upgraded.]

AMEND DIRECTIVE:
[Slots from SYNTHESIZER routing table rows marked Required. Always include Narrow + Mechanism.]

AMEND: discover-causal
  Narrow: [Scope tightening -- match scoped claim condition]
  Mechanism: [Hop notation: X -> [A] -> [B] -> Y. Use actual intermediate names.]
  Falsification: [Name the highest-confidence condition from SKEPTIC's final table. ID + testability + confidence.]
  [Evidence: Required if SYNTHESIZER row 3 = Required]
    "Mechanism is theoretical. Cite one context-specific observation before next decision gate."
  [Inertia: Required if SYNTHESIZER row 4 = Required]
    "Y occurs at [baseline rate] without X via [most dangerous I-NN pathway from SYNTHESIZER].
     Demonstrate incremental Y above this baseline."
  [Observability: Required if SYNTHESIZER row 1 = Required]
    "Chain observability: [pattern]. Hops [list Opaque/Partial hops by name] require proxy
     measurements or claim narrowing to the observable portion."
  [Testability: Required if SYNTHESIZER row 2 = Required]
    "Conditions [list IDs with pool label] have Unknown testability after evidence. Determine
     available instrumentation before treating these as actionable falsification targets."

---

Write artifact: simulations/discover/causal/{topic}-causal-{date}.md
Frontmatter: skill, topic, date, cause (X), outcome (Y),
             role_sequence (FRAMER-ANALYST-SKEPTIC-SYNTHESIZER-FRAMER), role_count (5),
             gate_checklists (5),
             inertia_verdict (SAFE/ADVISORY/STOP), baseline_rate,
             inertia_observability (Observable/Partial/Opaque),
             evidence_count, evidence_quality (Strong/Moderate/Weak/None),
             f_nn_count, i_nn_count, i_nn_pool_coverage (Comprehensive/Adequate/Minimal),
             hop_count,
             mechanism_strength_preliminary (Strong/Moderate/Weak),
             mechanism_strength_final (Strong/Moderate/Weak/NA), strength_changed (true/false),
             chain_observability_pattern (AllObservable/Mixed/PredominantlyOpaque),
             observability_amend_triggered (true/false),
             testability_refined_count, testability_residual_unknown_count,
             f_nn_residual_count, i_nn_residual_count, pool_asymmetry_detected (true/false),
             testability_amend_triggered (true/false),
             amend_routing_rows_required (count),
             confounder_named (true/false).
```

---

## V-02: Parallel Dual-Pool Table Architecture with AUDITOR

**Axis:** Output format — F-NN and I-NN pools are formatted as structurally identical tables
throughout the entire output. Both tables carry the same five columns: ID | Condition |
Testability | Confidence | Rationale. The inertia section uses a pool-level header block that
declares inertia severity, baseline rate, and inertia pathway observability before the I-NN
table rows appear. This makes A-14 visually unambiguous (any I-NN table with fewer than two
rows fails on inspection) and places A-15 as a labeled header field with immediate visibility.
The AUDITOR role closes with a routing table that references both pools by column.

**Hypothesis:** Prompts that mix table and prose formats for the two pools (as in R6 V-01–V-05,
where I-01 appeared in a different table structure than F-NN conditions) create asymmetric
treatment that may reduce I-NN pool quality. When I-NN and F-NN tables are formatted
identically, analysts recognize that inertia conditions are full peers of claim conditions --
same analytical investment, same label requirements. The inertia pool header block forces
A-15 (inertia observability) before I-NN rows are written, establishing the counterfactual
observability question as structurally prior to enumerating pathways.

```
You are running /discover-causal.
Your input is a feature hypothesis of the form "X causes Y."
Seven sections. Complete each fully before advancing.
Every classification judgment uses a discrete label from a fixed set with a rationale line.

Dual-pool architecture: all falsification conditions live in two structurally identical tables.
  F-NN pool (Section 1): claim-derived conditions.
  I-NN pool (Section 2): inertia-derived conditions.
Both tables carry columns: ID | Condition | Testability | Confidence | Rationale.
Testability = Unknown at genesis for all conditions. Confidence = Pending until Section 5.
Section 3 refines testability. Section 5 assigns confidence. No exceptions.

AUDITOR role: runs after Section 5 (adversarial). Produces AMEND routing table.

---

## SECTION 1: CLAIM AND F-NN POOL

Claim extraction:
  X (the cause): [Extract from input]
  Y (the claimed outcome): [Extract from input]
  Full claim: ["X causes Y" -- one sentence]

F-NN Pool:
[Claim-derived falsification conditions. At least two rows. Confidence column is Pending --
Section 5 (SKEPTIC) fills it. Testability = Unknown -- Section 3 (evidence) refines it.]

| ID   | Condition (claim false if observed)                     | Testability          | Confidence | Rationale |
|------|---------------------------------------------------------|----------------------|------------|-----------|
| F-01 | [What would show X does not cause Y?]                   | Unknown (see Sec 3)  | Pending    | [1 sentence: what failure mode does this expose?] |
| F-02 | [Second distinct condition.]                             | Unknown (see Sec 3)  | Pending    | [1 sentence] |
[Add F-NN as claim analysis generates more conditions.]

SECTION 1 GATE:
[ ] X and Y extracted separately
[ ] At least two F-NN rows with Unknown testability and Pending confidence
[ ] No mechanism or evidence content in this section

--- Do not advance to Section 2 until all items are checked. ---

---

## SECTION 2: I-NN POOL AND INERTIA HEADER

Inertia pool header:
[Establish baseline and inertia observability BEFORE writing I-NN rows. These fields are
prerequisites to I-NN pool generation: you cannot enumerate inertia pathways without first
asking whether you can observe them.]

Status-quo description: [One sentence: what happens today without X?]
Baseline rate: [Estimate or bound. Or: "Unknown."]
Inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP
Inertia severity rationale: [1 sentence]

Inertia pathway observability: [ ] Observable  [ ] Partial  [ ] Opaque
  (Observable = direct measurement of Y rate without X is available or achievable;
   Partial = proxy indicators exist but no direct measurement path;
   Opaque = no available path to observe whether status quo produces Y)
Inertia observability rationale: [1 sentence: what would enable direct measurement?]

[Inertia pathway observability answers a different question than mechanism hop observability.
Hop observability (Section 4) labels how detectable each forward causal step is.
Inertia pathway observability labels how detectable the status-quo-Y pathway is -- the
counterfactual. A mechanism chain may be AllObservable while the inertia path is Opaque.]

I-NN Pool:
[Inertia-derived falsification conditions. At least two rows. Same structure as F-NN table:
Confidence = Pending until Section 5. Testability = Unknown until Section 3.
Each I-NN condition names a specific mechanism by which Y occurs without X.]

| ID   | Condition (Y occurs without X via...)                   | Testability          | Confidence | Rationale |
|------|---------------------------------------------------------|----------------------|------------|-----------|
| I-01 | Y occurs at [baseline rate] without X via [mechanism 1] | Unknown (see Sec 3)  | Pending    | [1 sentence: what makes this pathway plausible?] |
| I-02 | Y occurs via [mechanism 2] without X                    | Unknown (see Sec 3)  | Pending    | [1 sentence] |
[Add I-NN as inertia analysis generates more pathways. Each must name a distinct mechanism.]

SECTION 2 GATE:
[ ] Inertia pool header complete: baseline rate, severity label with rationale
[ ] Inertia pathway observability label assigned with rationale (Observable/Partial/Opaque)
[ ] At least two I-NN rows with Unknown testability and Pending confidence
[ ] Each I-NN condition names a distinct inertia mechanism (not just restatements)

--- Do not advance to Section 3 until all items are checked. ---

---

## SECTION 3: EVIDENCE AND TESTABILITY REFINEMENT

[At least one context-specific observation, OR explicit "None found" with mandatory AMEND
evidence slot. After gathering evidence, run testability refinement across ALL F-NN and I-NN
conditions. Update testability column from Unknown to Easy/Hard/Unknown-confirmed.]

Evidence entry 1:
  Source type: [ ] Prior result  [ ] Analogous case  [ ] Domain observation  [ ] Counter-evidence
  Observation: [What was seen, where, when?]
  Bearing on X->Y: [1 sentence]

[Add entries as needed.]

Evidence quality: [ ] Strong  [ ] Moderate  [ ] Weak  [ ] None
Evidence quality rationale: [1 sentence]

Testability refinement pass:
[Update the testability column for every F-NN and I-NN condition. Write a refinement row
for each condition. Conditions that remain Unknown must be explicitly confirmed, not just left.]

| ID   | Testability after evidence       | Refinement rationale |
|------|----------------------------------|---------------------|
| F-01 | [ ] Easy  [ ] Hard  [ ] Unknown  | [1 sentence] |
| F-02 | [ ] Easy  [ ] Hard  [ ] Unknown  | [1 sentence] |
| I-01 | [ ] Easy  [ ] Hard  [ ] Unknown  | [1 sentence] |
| I-02 | [ ] Easy  [ ] Hard  [ ] Unknown  | [1 sentence] |
[Mirror all F-NN and I-NN conditions.]

Testability refinement yield:
  testability_refined_count: [Count moved from Unknown to Easy or Hard]
  testability_residual_unknown_count: [Count confirmed Unknown after evidence]
  Residual Unknown IDs: [List by ID, or "None"]
  F-NN residual count: [Count of F-NN conditions remaining Unknown]
  I-NN residual count: [Count of I-NN conditions remaining Unknown]

SECTION 3 GATE:
[ ] Evidence populated (or explicit "None found")
[ ] Evidence quality label with rationale
[ ] Testability refinement row for every F-NN and I-NN condition
[ ] testability_refined_count and testability_residual_unknown_count declared
[ ] F-NN and I-NN residual counts declared separately

--- Do not advance to Section 4 until all items are checked. ---

---

## SECTION 4: MECHANISM CHAIN

[Map the causal pathway from X to Y. Two hops minimum. Every hop carries observability label,
rationale, evidence coherence, and falsification connection to an F-NN or I-NN from Sections 1-2.
State mechanism only -- adversarial content belongs in Section 5.]

Hop 1: X [name] -> [intermediate A]: [How does X produce A?]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Observability rationale: [1 sentence]
  Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
  Falsification connection: [F-NN or I-NN ID. One sentence: if this hop fails, this condition holds.]

Hop 2: [intermediate A] -> Y: [How does A produce Y?]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Observability rationale: [1 sentence]
  Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
  Falsification connection: [F-NN or I-NN ID. One sentence.]

[Add Hop 3+ as needed. Every hop: observability + rationale, coherence, falsification connection.]

Mechanism strength (preliminary): [ ] Strong  [ ] Moderate  [ ] Weak
Preliminary rationale: [1 sentence: pre-challenge assessment based on hop labels and evidence.]

SECTION 4 GATE:
[ ] At least two hops filled
[ ] Every hop: observability label + rationale, evidence coherence, falsification connection
[ ] Mechanism strength (preliminary) with rationale
[ ] No confidence labels in this section (Section 5)
[ ] No chain observability aggregate (AUDITOR's job)

--- Do not advance to Section 5 until all items are checked. ---

---

## SECTION 5: ADVERSARIAL CHALLENGE

[Structurally separate from Section 4. Challenge every hop. Assign confidence labels to all
F-NN and I-NN conditions. Produce final mechanism strength. SKEPTIC mode.]

Hop-by-hop challenge:

  Hop 1 challenge:
    What breaks X -> [intermediate A]? [Observable condition]
    Observable test: [What to measure or detect]
    Alternative at this hop: [What else produces [intermediate A] without X?]

  Hop 2 challenge:
    What breaks [intermediate A] -> Y? [Observable condition]
    Observable test: [What to measure or detect]
    Alternative at this hop: [What else produces Y without [intermediate A]?]

  [Mirror all Section 4 hops.]

Confounders:
  Confounder 1: [Variable correlating with both X and Y. Name and describe.]

Inertia challenge:
  Adversarial view: [Which I-NN pathway is most plausible? Does analysis revise inertia verdict?]
  Most dangerous I-NN: [ID -- which condition, if true, most threatens the causal claim?]
  Revised inertia severity: [ ] Confirms  [ ] Upgrades to ADVISORY  [ ] Upgrades to STOP

Final combined table (testability from Section 3 + confidence from Section 5):

| ID   | Condition text      | Testability (Sec 3)  | Confidence (Sec 5)          | Rationale |
|------|---------------------|----------------------|-----------------------------|-----------|
| F-01 | [text]              | [Easy/Hard/Unknown]  | [ ] High  [ ] Med  [ ] Low  | [1 sentence] |
| F-02 | [text]              | [Easy/Hard/Unknown]  | [ ] High  [ ] Med  [ ] Low  | [1 sentence] |
| I-01 | [text]              | [Easy/Hard/Unknown]  | [ ] High  [ ] Med  [ ] Low  | [1 sentence] |
| I-02 | [text]              | [Easy/Hard/Unknown]  | [ ] High  [ ] Med  [ ] Low  | [1 sentence] |
[Mirror all conditions. Testability carries Section 3 values unchanged.]

Mechanism strength (final): [ ] Strong  [ ] Moderate  [ ] Weak  [ ] NA (STOP)
Final rationale: [1 sentence. Changed from preliminary or not -- state which and why.]

---

## AUDITOR

[Post-processing role. Runs after Section 5. Reads Section 3 yield data, Section 4 hop
observability labels, Section 2 I-NN pool and inertia observability, and Section 5 final table.
Produces consolidated AMEND routing table. Does not challenge mechanism or propose scope.]

### Diagnostic 1: Chain Observability Aggregate

| Hop   | Step                    | Observability (from Sec 4)      |
|-------|-------------------------|---------------------------------|
| Hop 1 | X -> [intermediate A]   | [Observable / Partial / Opaque] |
| Hop 2 | [intermediate A] -> Y   | [Observable / Partial / Opaque] |

Observable: [Count]  |  Partial: [Count]  |  Opaque: [Count]  |  Total: [Count]
Chain observability pattern: [ ] AllObservable  [ ] Mixed  [ ] PredominantlyOpaque
Pattern rationale: [1 sentence]

### Diagnostic 2: Testability Yield (from Section 3)

Refined count: [Value]  |  Residual Unknown count: [Value]
Residual Unknown IDs: [From Section 3, or "None"]
F-NN residual: [Count]  |  I-NN residual: [Count]
Pool asymmetry: [One sentence: are I-NN conditions disproportionately Unknown?]
Yield quality: [ ] AllResolved  [ ] PartiallyResolved  [ ] Unresolved

### Diagnostic 3: I-NN Pool Review (from Section 2)

I-NN condition count: [Total]
I-NN conditions with Unknown testability: [List IDs or "None"]
I-NN conditions with Low confidence: [List IDs or "None"]
Pool coverage: [ ] Comprehensive  [ ] Adequate  [ ] Minimal
Coverage rationale: [1 sentence]

### Diagnostic 4: Inertia Observability Review (from Section 2)

Inertia pathway observability: [Observable / Partial / Opaque -- from Section 2 header]
Divergence from chain pattern: [Does inertia observability differ from chain pattern? One sentence.]

### AMEND Routing Table

| # | Diagnostic                  | Result                               | AMEND slot    | Routing |
|---|-----------------------------|--------------------------------------|---------------|---------|
| 1 | Chain observability pattern | [AllObservable/Mixed/PredominantlyOpaque] | Observability | [Required if Mixed or PredominantlyOpaque / Not required] |
| 2 | Testability residual count  | [Count]                              | Testability   | [Required if > 0 / Not required] |
| 3 | Evidence quality            | [Strong/Moderate/Weak/None]          | Evidence      | [Required if None / Not required] |
| 4 | Inertia severity (final)    | [SAFE/ADVISORY/STOP]                 | Inertia       | [Required if ADVISORY or STOP / Not required] |

AUDITOR note: [One sentence: most critical gap.]

---

## SECTION 6: SCOPE AND AMEND

Scoped claim: ["X causes Y when [condition], for [population], assuming [precondition]."]
Out-of-scope: [At least one context where mechanism fails, from Section 5.]

Final inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP
[Use Section 5 revised verdict if different from Section 2.]

AMEND DIRECTIVE:
[All slots marked Required in AUDITOR's routing table. Always include Narrow + Mechanism.]

AMEND: discover-causal
  Narrow: [Scope tightening]
  Mechanism: [Hop notation: X -> [A] -> [B] -> Y]
  Falsification: [Highest-confidence condition from Section 5 table. ID + testability + confidence.]
  [Evidence: if AUDITOR row 3 = Required]
  [Inertia: if AUDITOR row 4 = Required -- reference most dangerous I-NN by ID]
  [Observability: if AUDITOR row 1 = Required]
  [Testability: if AUDITOR row 2 = Required -- list residual IDs with pool label]

---

Write artifact: simulations/discover/causal/{topic}-causal-{date}.md
Frontmatter: skill, topic, date, cause (X), outcome (Y),
             dual_pool_architecture (true), auditor_role (true), gate_checklists (4),
             inertia_verdict (SAFE/ADVISORY/STOP), baseline_rate,
             inertia_observability (Observable/Partial/Opaque),
             evidence_count, evidence_quality (Strong/Moderate/Weak/None),
             f_nn_count, i_nn_count, i_nn_pool_coverage (Comprehensive/Adequate/Minimal),
             hop_count,
             mechanism_strength_preliminary (Strong/Moderate/Weak),
             mechanism_strength_final (Strong/Moderate/Weak/NA), strength_changed (true/false),
             chain_observability_pattern (AllObservable/Mixed/PredominantlyOpaque),
             observability_amend_triggered (true/false),
             testability_refined_count, testability_residual_unknown_count,
             f_nn_residual_count, i_nn_residual_count, pool_asymmetry_detected (true/false),
             testability_amend_triggered (true/false),
             confounder_named (true/false),
             amend_routing_rows_required (count).
```

---

## V-03: Inertia-First Lifecycle with EVALUATOR

**Axis:** Lifecycle emphasis — inertia analysis runs FIRST, before claim extraction and before
the F-NN pool is generated. The inertia section produces the I-NN pool and inertia observability
label as foundational inputs that constrain how the causal claim is subsequently framed. The F-NN
pool is generated second, with I-NN conditions already in scope. Evidence and testability
refinement integrate both pools. An EVALUATOR role closes the analysis with a routing table.

**Hypothesis:** In all prior R6 variations, inertia was checked AFTER the mechanism was
established -- a late-stage sanity check. This ordering may bias the check: analysts who have
already constructed and defended a mechanism chain are less likely to conclude that inertia
produces Y at a meaningful rate. Inverting the lifecycle -- establish the counter-hypothesis
first, generate the I-NN pool before the F-NN pool exists -- removes this anchoring effect.
Analysts who see inertia conditions before drafting the mechanism may write more mechanistically
specific F-NN conditions that explicitly differentiate X-caused Y from inertia-produced Y.
The test: does inertia-first ordering change the character of F-NN conditions generated?

```
You are running /discover-causal.
Your input is a feature hypothesis of the form "X causes Y."
Seven steps plus EVALUATOR role. Complete each step fully before advancing.
Every classification judgment uses a discrete label from a fixed set with a rationale line.

Lifecycle order: inertia analysis first (Steps 1-2), then claim extraction and F-NN pool
(Steps 3-4), then evidence and refinement (Step 5), then mechanism (Step 6), then
adversarial (Step 7), then EVALUATOR (routing table), then scope and AMEND.

This ordering is intentional: establish the status-quo competitor before stating the
causal claim. I-NN conditions generated without knowledge of the claim mechanism may
be more diverse and mechanistically independent than conditions generated after.

---

## STEP 1: INERTIA BASELINE AND PATHWAY OBSERVABILITY

[Before stating the causal claim: assess the status quo. What does Y look like today?
How visible is the baseline? Label inertia pathway observability before any claim work.]

Status-quo description: [One sentence: what happens today without X?]
Baseline rate: [Estimate or bound: "Y occurs in approximately __% of cases without X."
  Or: "Unknown -- no measurement available."]

Inertia pathway observability: [ ] Observable  [ ] Partial  [ ] Opaque
  (Observable = direct measurement of Y-without-X rate is available or straightforward;
   Partial = proxy data accessible, no direct measurement path;
   Opaque = no data path exists to observe whether status quo produces Y independently)
Inertia observability rationale: [1 sentence: what data source or experiment would enable direct observation?]

Inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP
Inertia severity rationale: [1 sentence: does the baseline create a meaningful
  competing explanation for Y?]

STEP 1 GATE:
[ ] Baseline rate declared (estimate, bound, or explicit "Unknown")
[ ] Inertia pathway observability label assigned with rationale
[ ] Inertia severity label assigned with rationale
[ ] No claim extraction or F-NN content in this step

--- Do not advance to Step 2 until all items are checked. ---

---

## STEP 2: I-NN POOL (INERTIA FALSIFICATION CONDITIONS)

[Generate inertia falsification conditions BEFORE the claim is stated. Each I-NN condition
names a specific pathway by which Y could occur without X. At least two conditions.
Testability = Unknown at genesis. No confidence yet -- Step 7 (adversarial) assigns it.]

| ID   | Inertia falsification condition                          | Testability          | Rationale |
|------|----------------------------------------------------------|----------------------|-----------|
| I-01 | Y occurs without X via [specific mechanism 1]            | Unknown (see Step 5) | [1 sentence: what makes this pathway plausible from what we know today?] |
| I-02 | Y occurs without X via [specific mechanism 2]            | Unknown (see Step 5) | [1 sentence] |
[Add I-NN as the baseline analysis generates more inertia pathways. Aim for distinct mechanisms.]

I-NN pool summary:
  Condition count: [Total I-NN conditions]
  Dominant inertia pathway: [Which I-NN, if true, would most challenge a causal claim for X->Y?
    ID and one-sentence rationale.]

STEP 2 GATE:
[ ] At least two I-NN conditions with distinct mechanisms
[ ] All I-NN testability = Unknown
[ ] No F-NN or claim content in this step
[ ] Dominant inertia pathway identified by ID

--- Do not advance to Step 3 until all items are checked. ---

---

## STEP 3: CLAIM EXTRACTION

[Now state the causal claim. The I-NN pool (Steps 1-2) should inform how you frame X and Y.
Do not restate I-NN conditions as F-NN conditions -- they are already catalogued.]

X (the cause): [Extract from input]
Y (the claimed outcome): [Extract from input]
Full claim: ["X causes Y" -- one sentence]

Inertia-claim interface: [One sentence: does the dominant I-NN pathway (Step 2) directly
  compete with this claim, or does it produce a related but distinct version of Y?
  This distinction constrains how F-NN conditions will be written in Step 4.]

---

## STEP 4: F-NN POOL (CLAIM FALSIFICATION CONDITIONS)

[Claim-derived conditions. At least two. Testability = Unknown. No confidence yet.
F-NN conditions should be distinct from I-NN conditions -- they address mechanism failure,
not inertia. If a condition overlaps with an I-NN condition, note the overlap.]

| ID   | Falsification condition (claim false if observed)       | Testability          | Rationale |
|------|---------------------------------------------------------|----------------------|-----------|
| F-01 | [What would show X does not cause Y?]                   | Unknown (see Step 5) | [1 sentence: mechanism failure this exposes] |
| F-02 | [Second distinct condition.]                             | Unknown (see Step 5) | [1 sentence] |
[Add F-NN as claim analysis generates more conditions. Note any I-NN overlaps.]

F-NN/I-NN overlap note: [Are any F-NN conditions restatements of I-NN conditions? If so,
  which pairs overlap and how do they differ in framing? Or: "No overlaps detected."]

---

## STEP 5: EVIDENCE AND TESTABILITY REFINEMENT

[At least one context-specific observation, OR explicit "None found" with mandatory AMEND
evidence slot. Refine testability across both F-NN (Step 4) and I-NN (Step 2) conditions.]

Evidence entry 1:
  Source type: [ ] Prior result  [ ] Analogous case  [ ] Domain observation  [ ] Counter-evidence
  Observation: [What was seen, where, when?]
  Bearing on X->Y: [1 sentence]

[Add entries as needed.]

Evidence quality: [ ] Strong  [ ] Moderate  [ ] Weak  [ ] None
Evidence quality rationale: [1 sentence]

Testability refinement pass:
[Update testability for ALL F-NN and I-NN conditions. I-NN conditions were generated before
the claim -- does evidence gathered for the claim also refine inertia conditions?]

| ID   | Testability after evidence       | Refinement rationale |
|------|----------------------------------|---------------------|
| F-01 | [ ] Easy  [ ] Hard  [ ] Unknown  | [1 sentence] |
| F-02 | [ ] Easy  [ ] Hard  [ ] Unknown  | [1 sentence] |
| I-01 | [ ] Easy  [ ] Hard  [ ] Unknown  | [1 sentence] |
| I-02 | [ ] Easy  [ ] Hard  [ ] Unknown  | [1 sentence] |
[Mirror all conditions.]

Testability refinement yield:
  testability_refined_count: [Count moved from Unknown to Easy or Hard]
  testability_residual_unknown_count: [Count remaining Unknown]
  Residual Unknown IDs: [List by ID, or "None"]
  F-NN residual count: [Count]  |  I-NN residual count: [Count]
  Cross-pool note: [Did claim evidence refine any I-NN conditions? Or: "No cross-pool refinement."]

STEP 5 GATE:
[ ] Evidence populated (or explicit "None found")
[ ] Evidence quality label and rationale
[ ] Testability refinement row for every F-NN and I-NN condition
[ ] yield counts declared with pool breakdown
[ ] Cross-pool note present

--- Do not advance to Step 6 until all items are checked. ---

---

## STEP 6: MECHANISM CHAIN

[Map the causal pathway from X to Y. Two hops minimum. Every hop carries observability label,
rationale, evidence coherence, and falsification connection to an F-NN or I-NN.
State mechanism only. I-NN conditions established in Step 2 are available for cross-reference.]

Hop 1: X [name] -> [intermediate A]: [How does X produce A?]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Observability rationale: [1 sentence]
  Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
  Falsification connection: [F-NN or I-NN ID. One sentence.]

Hop 2: [intermediate A] -> Y: [How does A produce Y?]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Observability rationale: [1 sentence]
  Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
  Falsification connection: [F-NN or I-NN ID. One sentence.]

[Add Hop 3+ as needed.]

Mechanism strength (preliminary): [ ] Strong  [ ] Moderate  [ ] Weak
Preliminary rationale: [1 sentence]

STEP 6 GATE:
[ ] At least two hops with observability label + rationale, coherence, falsification connection
[ ] Mechanism strength (preliminary) with rationale
[ ] No adversarial content (Step 7)

--- Do not advance to Step 7 until all items are checked. ---

---

## STEP 7: ADVERSARIAL CHALLENGE

[Challenge every hop. Assign confidence to all F-NN and I-NN conditions. Final mechanism
strength. Structurally separate from Step 6. I-NN conditions are primary adversarial inputs.]

Hop-by-hop challenge:

  Hop 1 challenge:
    What breaks X -> [intermediate A]? [Observable condition]
    Observable test: [What to measure]
    Alternative at this hop: [What else produces [intermediate A] without X?]
    Confidence: [ ] High  [ ] Medium  [ ] Low
    Confidence rationale: [1 sentence]

  Hop 2 challenge:
    What breaks [intermediate A] -> Y? [Observable condition]
    Observable test: [What to measure]
    Alternative at this hop: [What else produces Y without [intermediate A]?]
    Confidence: [ ] High  [ ] Medium  [ ] Low
    Confidence rationale: [1 sentence]

  [Mirror all Step 6 hops.]

Confounders:
  Confounder 1: [Variable correlating with both X and Y. Name and describe.]

Inertia challenge:
  [Which I-NN condition is most threatening given the mechanism analysis?
   Has the mechanism work revealed new inertia pathways not in Step 2?]
  Dominant I-NN reference: [ID -- which I-NN, post-mechanism analysis, is most dangerous?]
  Revised inertia severity: [ ] Confirms Step 1  [ ] Upgrades to ADVISORY  [ ] Upgrades to STOP

Final falsification table:

| ID   | Condition                      | Testability (Step 5) | Confidence (Step 7)         | Rationale |
|------|--------------------------------|----------------------|-----------------------------|-----------|
| F-01 | [text]                         | [Easy/Hard/Unknown]  | [ ] High  [ ] Med  [ ] Low  | [1 sentence] |
| F-02 | [text]                         | [Easy/Hard/Unknown]  | [ ] High  [ ] Med  [ ] Low  | [1 sentence] |
| I-01 | [text]                         | [Easy/Hard/Unknown]  | [ ] High  [ ] Med  [ ] Low  | [1 sentence] |
| I-02 | [text]                         | [Easy/Hard/Unknown]  | [ ] High  [ ] Med  [ ] Low  | [1 sentence] |

Mechanism strength (final): [ ] Strong  [ ] Moderate  [ ] Weak  [ ] NA (STOP)
Final rationale: [1 sentence. Changed from preliminary? State which and why.]

---

## EVALUATOR

[Post-processing role. Runs after Step 7. Reads all prior outputs. Produces consolidated
AMEND routing table. Does not reopen analytical questions or propose scope.]

### Diagnostic 1: Chain Observability Aggregate

| Hop   | Step                      | Observability (from Step 6)     |
|-------|---------------------------|---------------------------------|
| Hop 1 | X -> [intermediate A]     | [Observable / Partial / Opaque] |
| Hop 2 | [intermediate A] -> Y     | [Observable / Partial / Opaque] |

Observable: [Count]  |  Partial: [Count]  |  Opaque: [Count]  |  Total: [Count]
Chain observability pattern: [ ] AllObservable  [ ] Mixed  [ ] PredominantlyOpaque
Pattern rationale: [1 sentence]

### Diagnostic 2: Testability Yield (from Step 5)

Refined: [Count]  |  Residual Unknown: [Count]  |  Residual IDs: [List or "None"]
F-NN residual: [Count]  |  I-NN residual: [Count]
Pool asymmetry: [1 sentence: are I-NN conditions disproportionately residual Unknown?]
Yield quality: [ ] AllResolved  [ ] PartiallyResolved  [ ] Unresolved

### Diagnostic 3: I-NN Pool (from Steps 1-2)

I-NN count: [Total]  |  Pool coverage: [ ] Comprehensive  [ ] Adequate  [ ] Minimal
Coverage rationale: [1 sentence]
Inertia-first dividend: [Did the inertia-first ordering produce I-NN conditions that are
  mechanistically distinct from the F-NN conditions? Or: "No clear dividend -- conditions overlap."]

### Diagnostic 4: Inertia Observability (from Step 1)

Inertia pathway observability: [Observable / Partial / Opaque -- from Step 1]
Divergence from chain: [How does inertia observability compare to chain pattern? 1 sentence.]

### AMEND Routing Table

| # | Diagnostic                    | Result                               | AMEND slot         | Routing |
|---|-------------------------------|--------------------------------------|--------------------|---------|
| 1 | Chain observability pattern   | [AllObservable/Mixed/PredominantlyOpaque] | Observability  | [Required if Mixed or PredominantlyOpaque / Not required] |
| 2 | Testability residual count    | [Count]                              | Testability        | [Required if > 0 / Not required] |
| 3 | Evidence quality              | [Strong/Moderate/Weak/None]          | Evidence           | [Required if None / Not required] |
| 4 | Inertia severity (final)      | [SAFE/ADVISORY/STOP]                 | Inertia            | [Required if ADVISORY or STOP / Not required] |
| 5 | Inertia pathway observability | [Observable/Partial/Opaque]          | Inertia-visibility | [Required if Opaque / Not required -- add to Inertia slot: "Inertia pathway is Opaque. Instrument baseline measurement before relying on inertia verdict."] |

EVALUATOR note: [Most critical gap in 1 sentence.]

---

## SCOPE AND AMEND

Scoped claim: ["X causes Y when [condition], for [population], assuming [precondition]."]
Out-of-scope: [At least one context where mechanism fails.]

Final inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP

AMEND DIRECTIVE:
[All Required slots from EVALUATOR routing table. Always include Narrow + Mechanism.]

AMEND: discover-causal
  Narrow: [Scope tightening]
  Mechanism: [Hop notation: X -> [A] -> [B] -> Y]
  Falsification: [Highest-confidence condition from Step 7 table. ID + testability + confidence.]
  [Evidence: if EVALUATOR row 3 = Required]
  [Inertia: if EVALUATOR row 4 = Required -- reference dominant I-NN by ID]
  [Observability: if EVALUATOR row 1 = Required]
  [Testability: if EVALUATOR row 2 = Required -- list residual IDs with pool label]
  [Inertia-visibility: if EVALUATOR row 5 = Required]

---

Write artifact: simulations/discover/causal/{topic}-causal-{date}.md
Frontmatter: skill, topic, date, cause (X), outcome (Y),
             lifecycle_order (inertia-first), evaluator_role (true), gate_checklists (4),
             inertia_verdict (SAFE/ADVISORY/STOP), baseline_rate,
             inertia_observability (Observable/Partial/Opaque),
             evidence_count, evidence_quality (Strong/Moderate/Weak/None),
             f_nn_count, i_nn_count, i_nn_pool_coverage (Comprehensive/Adequate/Minimal),
             hop_count,
             mechanism_strength_preliminary, mechanism_strength_final, strength_changed (true/false),
             chain_observability_pattern (AllObservable/Mixed/PredominantlyOpaque),
             observability_amend_triggered (true/false),
             testability_refined_count, testability_residual_unknown_count,
             f_nn_residual_count, i_nn_residual_count, pool_asymmetry_detected (true/false),
             cross_pool_refinement_detected (true/false),
             inertia_first_dividend (true/false),
             testability_amend_triggered (true/false),
             amend_routing_rows_required (count), confounder_named (true/false).
```

---

## V-04: Interrogative Phrasing Register with EXAMINER

**Axis:** Phrasing register — every section prompt is framed as a sequence of questions rather
than directives. The imperative voice ("Map the causal pathway") becomes interrogative ("What
is the causal pathway from X to Y?"). I-NN pool generation is driven by questions that force
explicit consideration of distinct inertia pathways. Inertia observability is elicited through
a direct question ("Can we detect whether Y occurs without X?") before a template appears.
An EXAMINER role closes the analysis with a routing table. Structure and criteria are identical
to V-01; phrasing is the single varying axis.

**Hypothesis:** Imperative prompts ("Generate at least two I-NN conditions") may produce
template-filling behavior: analysts write the minimum required rows without exploring the
inertia space. Interrogative prompts ("What pathways could produce Y without X -- and which
is most plausible from what you know today?") may produce more exploratory enumeration, because
questions invite open-ended reasoning before the constraint (minimum two) is imposed. The test:
does interrogative phrasing produce richer or more mechanistically specific I-NN pools than
V-01's imperative framing?

```
You are running /discover-causal.
Your input is a feature hypothesis of the form "X causes Y."
Seven phases. Answer each question set fully before advancing.
Every classification judgment uses a discrete label from a fixed set with a rationale line.

Two-pool design: F-NN conditions (claim-derived) and I-NN conditions (inertia-derived).
Both pools start testability = Unknown. Phase 4 refines both. Phase 6 assigns confidence.
EXAMINER role closes with AMEND routing table.

---

## PHASE 1: WHAT ARE WE CLAIMING?

  Q1.1: What is the proposed cause? (X): [One phrase extracted from input]
  Q1.2: What is the claimed outcome? (Y): [One phrase extracted from input]
  Q1.3: What is the full causal claim in one sentence? ["X causes Y."]

---

## PHASE 2: WHAT WOULD FALSIFY THE CLAIM?

[Enumerate conditions that, if observed, would show the claim is wrong.
  Q2.1: What would you expect to observe if X does NOT cause Y?
  Q2.2: What would show the mechanism is breaking down even when X is present?
  Q2.3: Are there additional conditions that would disprove X->Y in specific contexts?
Generate at least two conditions. Testability starts Unknown -- Phase 4 refines it.
Confidence is Pending until Phase 6. No confidence column yet.]

| ID   | Falsification condition (claim false if observed) | Testability          | Rationale |
|------|---------------------------------------------------|----------------------|-----------|
| F-01 | [Answer to Q2.1 or Q2.2]                          | Unknown (see Ph 4)   | [1 sentence: what failure mode does this expose?] |
| F-02 | [Answer to Q2.2 or Q2.3]                          | Unknown (see Ph 4)   | [1 sentence] |
[Continue until the claim's main failure modes are catalogued.]

---

## PHASE 3: DOES DOING NOTHING ALREADY PRODUCE Y?

[The most commonly skipped question in feature decisions.]

  Q3.1: What happens today without X? (Describe the status quo in one sentence.)
  Q3.2: At what rate does Y already occur without X?
    Answer: [Estimate, bound, or "Unknown."]
  Q3.3: Can we detect whether Y occurs without X?
    (Is the baseline observable? What data or instrumentation would reveal it?)
    Answer: [Observable / Partial / Opaque]
    Rationale: [1 sentence: what measurement path exists or is missing?]
  Q3.4: How severe is the inertia risk?
    Answer: [ ] SAFE  [ ] ADVISORY  [ ] STOP
    Rationale: [1 sentence]

Inertia pathway observability: [Observable / Partial / Opaque -- from Q3.3]
  [This label answers Q3.3 in structured form. It is independent of mechanism hop observability,
  which is computed in Phase 5. Inertia observability: can we see the counter-hypothesis?
  Hop observability: can we see the forward mechanism?]

  Q3.5: What specific pathways could produce Y without X?
    (Name at least two distinct mechanisms. Probe: are these independent pathways or variants
    of the same mechanism? Independent pathways strengthen the inertia case.)

I-NN Pool -- answers to Q3.5:
[At least two I-NN conditions. Testability = Unknown. No confidence yet.]

| ID   | How Y occurs without X (specific pathway)               | Testability          | Rationale |
|------|---------------------------------------------------------|----------------------|-----------|
| I-01 | [Answer to Q3.5 -- pathway 1. Name the mechanism.]      | Unknown (see Ph 4)   | [1 sentence: why is this pathway plausible?] |
| I-02 | [Answer to Q3.5 -- pathway 2. Different mechanism.]     | Unknown (see Ph 4)   | [1 sentence] |
[Continue for additional pathways from Q3.5.]

  Q3.6: Which I-NN condition, if true, would most threaten the claim?
    Answer: [ID and one-sentence rationale.]

PHASE 3 GATE:
[ ] Q3.1-Q3.4 answered with labeled responses (observability + severity)
[ ] Inertia pathway observability label declared (Observable/Partial/Opaque)
[ ] At least two I-NN conditions in table with testability Unknown
[ ] Q3.6 answered with dominant I-NN ID

--- Do not advance to Phase 4 until all items are checked. ---

---

## PHASE 4: WHAT DOES CONTEXT TELL US?

  Q4.1: What prior results, analogous cases, or domain knowledge bear on X->Y?
    (At least one observation required. If genuinely none exists, state "None found."
    Do not skip -- absence of evidence is itself a finding.)

Evidence entry 1:
  Source type: [ ] Prior result  [ ] Analogous case  [ ] Domain observation  [ ] Counter-evidence
  Observation: [Q4.1 answer]
  Bearing on X->Y: [1 sentence: supports, complicates, or challenges?]

[Add entries as needed.]

Evidence quality: [ ] Strong  [ ] Moderate  [ ] Weak  [ ] None
Evidence quality rationale: [1 sentence]

  Q4.2: For each falsification condition, can we now determine whether it is testable?
    (Conditions that remain Unknown after evidence are a finding, not a gap to paper over.)

Testability refinement pass:

| ID   | Testability after evidence       | Refinement rationale |
|------|----------------------------------|---------------------|
| F-01 | [ ] Easy  [ ] Hard  [ ] Unknown  | [1 sentence] |
| F-02 | [ ] Easy  [ ] Hard  [ ] Unknown  | [1 sentence] |
| I-01 | [ ] Easy  [ ] Hard  [ ] Unknown  | [1 sentence] |
| I-02 | [ ] Easy  [ ] Hard  [ ] Unknown  | [1 sentence] |
[Mirror all conditions.]

Testability refinement yield:
  testability_refined_count: [Count]
  testability_residual_unknown_count: [Count]
  Residual Unknown IDs: [List or "None"]
  F-NN residual: [Count]  |  I-NN residual: [Count]

  Q4.3: Are I-NN conditions disproportionately harder to test than F-NN conditions?
    (Pool asymmetry: is the inertia evidence harder to gather than mechanism evidence?)
    Answer: [Yes / No / Unclear -- 1 sentence rationale]

PHASE 4 GATE:
[ ] Evidence populated (or explicit "None found")
[ ] Evidence quality label and rationale
[ ] Testability refinement row for every F-NN and I-NN condition
[ ] yield counts declared with pool breakdown
[ ] Q4.3 answered

--- Do not advance to Phase 5 until all items are checked. ---

---

## PHASE 5: WHAT IS THE CAUSAL MECHANISM?

  Q5.1: What is the step-by-step causal pathway from X to Y?
    (Decompose into at least two hops. State only the mechanism -- challenge comes in Phase 6.)
  Q5.2: For each hop, can we directly observe the intermediate state?
  Q5.3: Is there evidence that supports, conflicts with, or is neutral to each hop?
  Q5.4: Which F-NN or I-NN condition would be confirmed if this hop fails?

Hop 1: X [name] -> [intermediate A]: [Q5.1 answer for hop 1]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque  (Q5.2)
  Observability rationale: [1 sentence]
  Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe  (Q5.3)
  Falsification connection: [F-NN or I-NN ID. One sentence.]  (Q5.4)

Hop 2: [intermediate A] -> Y: [Q5.1 answer for hop 2]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Observability rationale: [1 sentence]
  Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions
  Falsification connection: [F-NN or I-NN ID. One sentence.]

[Add Hop 3+ as needed.]

  Q5.5: How strong is the mechanism before challenge?
    Answer: Mechanism strength (preliminary): [ ] Strong  [ ] Moderate  [ ] Weak
    Rationale: [1 sentence]

PHASE 5 GATE:
[ ] At least two hops with observability + rationale, coherence, falsification connection
[ ] Mechanism strength (preliminary) with rationale
[ ] No adversarial content (Phase 6)

--- Do not advance to Phase 6 until all items are checked. ---

---

## PHASE 6: WHAT WOULD BREAK THIS?

[Structurally separate from Phase 5. Adversarial framing.]

  Q6.1: For each hop, what observable condition would show the hop is wrong?
  Q6.2: What else could produce each intermediate state without X?
  Q6.3: What confounders correlate with both X and Y?
  Q6.4: Has the adversarial analysis changed your view on inertia? Which I-NN is most dangerous?

Hop 1 challenge:
  What breaks X -> [intermediate A]? (Q6.1): [Observable condition]
  Observable test: [What to measure]
  Alternative (Q6.2): [What else produces [intermediate A] without X?]
  Confidence: [ ] High  [ ] Medium  [ ] Low
  Confidence rationale: [1 sentence]

Hop 2 challenge:
  What breaks [intermediate A] -> Y? (Q6.1): [Observable condition]
  Observable test: [What to measure]
  Alternative (Q6.2): [What else produces Y without [intermediate A]?]
  Confidence: [ ] High  [ ] Medium  [ ] Low
  Confidence rationale: [1 sentence]

[Mirror all Phase 5 hops.]

Confounders (Q6.3):
  Confounder 1: [Variable correlating with both X and Y. Name and describe.]

Inertia challenge (Q6.4):
  Adversarial I-NN: [Which I-NN is most dangerous post-mechanism analysis? ID + rationale.]
  Revised inertia: [ ] Confirms Phase 3  [ ] Upgrades to ADVISORY  [ ] Upgrades to STOP

Final falsification table:

| ID   | Condition                   | Testability (Ph 4)   | Confidence (Ph 6)           | Rationale |
|------|-----------------------------|----------------------|-----------------------------|-----------|
| F-01 | [text]                      | [Easy/Hard/Unknown]  | [ ] High  [ ] Med  [ ] Low  | [1 sentence] |
| F-02 | [text]                      | [Easy/Hard/Unknown]  | [ ] High  [ ] Med  [ ] Low  | [1 sentence] |
| I-01 | [text]                      | [Easy/Hard/Unknown]  | [ ] High  [ ] Med  [ ] Low  | [1 sentence] |
| I-02 | [text]                      | [Easy/Hard/Unknown]  | [ ] High  [ ] Med  [ ] Low  | [1 sentence] |

Mechanism strength (final): [ ] Strong  [ ] Moderate  [ ] Weak  [ ] NA (STOP)
Final rationale: [1 sentence. Changed from preliminary?]

---

## EXAMINER

[Post-processing role. Reads all phases. Produces AMEND routing table.
Questions are closed -- EXAMINER does not reopen analysis. Routing table only.]

  Q_E1: What is the chain observability pattern?

| Hop   | Step                    | Observability (from Phase 5)    |
|-------|-------------------------|---------------------------------|
| Hop 1 | X -> [intermediate A]   | [Observable / Partial / Opaque] |
| Hop 2 | [intermediate A] -> Y   | [Observable / Partial / Opaque] |

Observable: [Count]  |  Partial: [Count]  |  Opaque: [Count]  |  Total: [Count]
Chain observability pattern: [ ] AllObservable  [ ] Mixed  [ ] PredominantlyOpaque
Pattern rationale: [1 sentence]

  Q_E2: What is the testability residual status?

Residual Unknown count: [From Phase 4]  |  Residual IDs: [List or "None"]
Yield quality: [ ] AllResolved  [ ] PartiallyResolved  [ ] Unresolved
Pool asymmetry confirmed? [Yes/No from Phase 4 Q4.3]

  Q_E3: What is the I-NN pool coverage?

I-NN count: [Total]  |  Pool coverage: [ ] Comprehensive  [ ] Adequate  [ ] Minimal
Coverage rationale: [1 sentence]

  Q_E4: What is the inertia pathway observability?

Inertia pathway observability: [From Phase 3 Q3.3]
Divergence from chain: [Does inertia observability differ from chain pattern? 1 sentence.]

  Q_E5: Which AMEND slots are required?

| # | Diagnostic                    | Result                               | AMEND slot    | Routing |
|---|-------------------------------|--------------------------------------|---------------|---------|
| 1 | Chain observability pattern   | [AllObservable/Mixed/PredominantlyOpaque] | Observability | [Required if Mixed or PredominantlyOpaque / Not required] |
| 2 | Testability residual count    | [Count]                              | Testability   | [Required if > 0 / Not required] |
| 3 | Evidence quality              | [Strong/Moderate/Weak/None]          | Evidence      | [Required if None / Not required] |
| 4 | Inertia severity (final)      | [SAFE/ADVISORY/STOP]                 | Inertia       | [Required if ADVISORY or STOP / Not required] |

EXAMINER note: [Most critical finding -- 1 sentence.]

---

## PHASE 7: WHAT SHOULD WE AMEND?

Scoped claim: ["X causes Y when [condition], for [population], assuming [precondition]."]
Out-of-scope: [At least one context from Phase 6 where mechanism fails.]

Final inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP

AMEND DIRECTIVE:
[All Required slots from EXAMINER routing table. Always include Narrow + Mechanism.]

AMEND: discover-causal
  Narrow: [Scope tightening]
  Mechanism: [Hop notation: X -> [A] -> [B] -> Y]
  Falsification: [Highest-confidence condition from Phase 6 table. ID + testability + confidence.]
  [Evidence: if EXAMINER row 3 = Required]
  [Inertia: if EXAMINER row 4 = Required -- dominant I-NN from Phase 3 Q3.6 or Phase 6 Q6.4]
  [Observability: if EXAMINER row 1 = Required]
  [Testability: if EXAMINER row 2 = Required]

---

Write artifact: simulations/discover/causal/{topic}-causal-{date}.md
Frontmatter: skill, topic, date, cause (X), outcome (Y),
             phrasing_register (interrogative), examiner_role (true), gate_checklists (3),
             inertia_verdict (SAFE/ADVISORY/STOP), baseline_rate,
             inertia_observability (Observable/Partial/Opaque),
             evidence_count, evidence_quality (Strong/Moderate/Weak/None),
             f_nn_count, i_nn_count, i_nn_pool_coverage (Comprehensive/Adequate/Minimal),
             hop_count,
             mechanism_strength_preliminary, mechanism_strength_final, strength_changed (true/false),
             chain_observability_pattern (AllObservable/Mixed/PredominantlyOpaque),
             observability_amend_triggered (true/false),
             testability_refined_count, testability_residual_unknown_count,
             f_nn_residual_count, i_nn_residual_count, pool_asymmetry_detected (true/false),
             testability_amend_triggered (true/false),
             amend_routing_rows_required (count), confounder_named (true/false).
```

---

## V-05: Combination — Counter-Hypothesis Chain, AUDITOR, Triple-Gap Diagnostic

**Axes:** Inertia framing (counter-hypothesis mini-chain) + Role sequence (AUDITOR) +
Output format (section-letter structure). Combination variation.

The inertia check is framed as a counter-hypothesis: "What if there is an X-independent causal
chain that produces Y?" This counter-hypothesis is analyzed using the same hop-by-hop structure
as the main mechanism. Each counter-hypothesis hop gets an observability label. The aggregate
of counter-hypothesis hop labels IS the inertia pathway observability label (A-15). I-NN
conditions derive from the counter-hypothesis hop challenge (A-14): each hop that could fail
generates an I-NN condition. AUDITOR runs after SKEPTIC and produces the routing table (A-16).

New joint diagnostic: the triple gap. A condition is a triple gap if:
  - The mechanism hop that it references is Opaque (A-12)
  - AND the condition has Unknown testability after evidence (A-13)
  - AND the condition has an I-NN match (a parallel inertia condition with the same scope)
A triple gap represents maximum causal uncertainty at a point: we cannot observe the forward
mechanism, we cannot test the falsification condition, and the inertia path may produce Y
at the same point. Neither A-12, A-13, nor A-14 surfaces this co-occurrence individually.

**Hypothesis:** The counter-hypothesis mini-chain forces more mechanistically specific I-NN
conditions because each I-NN condition is tied to a hop in the inertia chain, not generated
abstractly from "what else might cause Y?" The structural cost is a longer prompt; the benefit
is I-NN conditions that are structurally parallel to F-NN conditions (both derived from chain
analysis) and that carry their own observability labels, enabling the triple-gap joint diagnostic.

```
You are running /discover-causal.
Your input is a feature hypothesis of the form "X causes Y."
Sections A through G, plus AUDITOR role. Complete each section fully before advancing.
Every classification judgment uses a discrete label from a fixed set with a rationale line.

Three-pool causal analysis:
  F-NN pool: claim-derived falsification conditions (Section A).
  I-NN pool: counter-hypothesis-derived falsification conditions (Section B).
  Mechanism hops: forward causal chain from X to Y (Section D).

Testability lifecycle: all conditions start Unknown in their source section.
Section C refines testability for F-NN and I-NN. Section E assigns confidence to all.

Inertia framing: the inertia pathway is analyzed as a counter-hypothesis mini-chain
in Section B. Each hop in the counter-hypothesis gets an observability label.
Inertia pathway observability = aggregate of counter-hypothesis hop labels.

AUDITOR role: runs after Section E. Produces AMEND routing table including triple-gap diagnostic.

---

## SECTION A: CLAIM AND F-NN POOL

A1. Claim:
  X (the cause): [Extract from input]
  Y (the claimed outcome): [Extract from input]
  Full claim: ["X causes Y" -- one sentence]

A2. F-NN Pool (claim-derived falsification conditions):
[At least two conditions. Testability = Unknown. No confidence yet.]

| ID   | Falsification condition (claim false if observed) | Testability          | Rationale |
|------|---------------------------------------------------|----------------------|-----------|
| F-01 | [What would show X does not cause Y?]             | Unknown (see Sec C)  | [1 sentence: mechanism failure exposed] |
| F-02 | [Second condition.]                               | Unknown (see Sec C)  | [1 sentence] |
[Add F-NN as needed.]

SECTION A GATE:
[ ] X and Y extracted separately
[ ] At least two F-NN conditions (Unknown testability, no confidence column)

--- Do not advance to Section B until checked. ---

---

## SECTION B: COUNTER-HYPOTHESIS CHAIN AND I-NN POOL

[The counter-hypothesis: "There exists an X-independent causal chain that produces Y."
Analyze this counter-hypothesis as a mini-chain with at least two hops, each hop annotated
with observability. The aggregate observability of the counter-hypothesis chain IS the
inertia pathway observability label (A-15). I-NN conditions derive from hop challenges (A-14).]

B1. Counter-hypothesis framing:
  Counter-hypothesis claim: ["Without X, Y still occurs via [mechanism]." -- one sentence]
  Baseline rate: [Estimate or bound. Or: "Unknown."]
  Inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP
  Inertia severity rationale: [1 sentence]

B2. Counter-hypothesis chain:
[At least two hops of the inertia pathway from status-quo conditions to Y.
Every hop carries: observability label, rationale, and inertia challenge question.]

  CH-Hop 1: [Status-quo condition] -> [intermediate state Z]: [How does the status quo produce Z?]
    Observability: [ ] Observable  [ ] Partial  [ ] Opaque
    Observability rationale: [1 sentence: can we directly detect this intermediate?]
    Inertia challenge: [What would show this counter-hypothesis hop fails?]

  CH-Hop 2: [intermediate state Z] -> Y: [How does Z produce Y?]
    Observability: [ ] Observable  [ ] Partial  [ ] Opaque
    Observability rationale: [1 sentence]
    Inertia challenge: [What would show this counter-hypothesis hop fails?]

  [Add CH-Hop 3+ if the inertia pathway decomposes into more steps.]

B3. Inertia pathway observability aggregate:
[Derived from counter-hypothesis hop labels. This is the inertia pathway observability (A-15).]

  CH-Observable hops: [Count]  |  CH-Partial hops: [Count]  |  CH-Opaque hops: [Count]
  Inertia pathway observability: [ ] Observable  [ ] Partial  [ ] Opaque
    (Observable = all or majority of counter-hypothesis hops are Observable;
     Partial = mixed counter-hypothesis hop labels;
     Opaque = majority of counter-hypothesis hops are Opaque)
  Inertia observability rationale: [1 sentence: what does this aggregate mean for our ability
    to detect whether Y occurs without X?]

B4. I-NN Pool (from counter-hypothesis hop challenges):
[Each I-NN condition derives from a CH-Hop challenge. At least two I-NN conditions.
Testability = Unknown at genesis. No confidence yet.]

| ID   | I-NN condition (from CH-Hop challenge)              | Source hop  | Testability          | Rationale |
|------|-----------------------------------------------------|-------------|----------------------|-----------|
| I-01 | [What would show CH-Hop 1 fails? Observable state.] | CH-Hop 1    | Unknown (see Sec C)  | [1 sentence] |
| I-02 | [What would show CH-Hop 2 fails? Observable state.] | CH-Hop 2    | Unknown (see Sec C)  | [1 sentence] |
[Add I-NN for additional CH-Hops.]

SECTION B GATE:
[ ] Counter-hypothesis claim stated
[ ] At least two CH-Hops with observability labels and rationale
[ ] Inertia pathway observability aggregate computed from CH-Hop labels
[ ] Inertia pathway observability label declared (Observable/Partial/Opaque)
[ ] At least two I-NN conditions derived from CH-Hop challenges
[ ] Inertia severity label with rationale

--- Do not advance to Section C until checked. ---

---

## SECTION C: EVIDENCE AND TESTABILITY REFINEMENT

[At least one context-specific observation, OR explicit "None found" with mandatory AMEND
evidence slot. Refine testability for all F-NN and I-NN conditions.]

Evidence entry 1:
  Source type: [ ] Prior result  [ ] Analogous case  [ ] Domain observation  [ ] Counter-evidence
  Observation: [What was seen, where, when?]
  Bearing on X->Y: [1 sentence]

[Add entries as needed.]

Evidence quality: [ ] Strong  [ ] Moderate  [ ] Weak  [ ] None
Evidence quality rationale: [1 sentence]

Testability refinement pass:

| ID   | Testability after evidence       | Refinement rationale |
|------|----------------------------------|---------------------|
| F-01 | [ ] Easy  [ ] Hard  [ ] Unknown  | [1 sentence] |
| F-02 | [ ] Easy  [ ] Hard  [ ] Unknown  | [1 sentence] |
| I-01 | [ ] Easy  [ ] Hard  [ ] Unknown  | [1 sentence] |
| I-02 | [ ] Easy  [ ] Hard  [ ] Unknown  | [1 sentence] |
[Mirror all F-NN and I-NN conditions.]

Testability refinement yield:
  testability_refined_count: [Count]
  testability_residual_unknown_count: [Count]
  Residual Unknown IDs: [List or "None"]
  F-NN residual: [Count]  |  I-NN residual: [Count]

SECTION C GATE:
[ ] Evidence populated (or explicit "None found")
[ ] Testability refinement row for every F-NN and I-NN condition
[ ] Yield counts declared with pool breakdown

--- Do not advance to Section D until checked. ---

---

## SECTION D: MECHANISM CHAIN

[Map the causal pathway from X to Y. Two hops minimum. Every hop carries: observability,
rationale, evidence coherence, falsification connection (F-NN or I-NN from Sections A-B).
Distinguish these mechanism hops from the counter-hypothesis hops in Section B.
State mechanism only -- adversarial content belongs in Section E.]

Hop 1: X [name] -> [intermediate A]: [How does X produce A?]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Observability rationale: [1 sentence]
  Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
  Falsification connection: [F-NN or I-NN ID. One sentence.]

Hop 2: [intermediate A] -> Y: [How does A produce Y?]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Observability rationale: [1 sentence]
  Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions
  Falsification connection: [F-NN or I-NN ID. One sentence.]

[Add Hop 3+ as needed.]

Mechanism strength (preliminary): [ ] Strong  [ ] Moderate  [ ] Weak
Preliminary rationale: [1 sentence]

SECTION D GATE:
[ ] At least two mechanism hops (distinct from Section B counter-hypothesis hops)
[ ] Every hop: observability + rationale, coherence, falsification connection
[ ] Mechanism strength (preliminary)
[ ] No adversarial content (Section E)

--- Do not advance to Section E until checked. ---

---

## SECTION E: ADVERSARIAL CHALLENGE

[Challenge every mechanism hop (Section D). Challenge the counter-hypothesis (Section B).
Assign confidence to all F-NN and I-NN conditions. Produce final mechanism strength.
Structurally separate from Section D.]

Mechanism hop-by-hop challenge:

  Hop 1 challenge:
    What breaks X -> [intermediate A]? [Observable condition]
    Observable test: [What to measure]
    Alternative: [What else produces [intermediate A] without X?]
    Confidence: [ ] High  [ ] Medium  [ ] Low
    Confidence rationale: [1 sentence]

  Hop 2 challenge:
    What breaks [intermediate A] -> Y? [Observable condition]
    Observable test: [What to measure]
    Alternative: [What else produces Y without [intermediate A]?]
    Confidence: [ ] High  [ ] Medium  [ ] Low
    Confidence rationale: [1 sentence]

  [Mirror all Section D hops.]

Confounders:
  Confounder 1: [Variable correlating with both X and Y. Name and describe.]

Counter-hypothesis challenge:
  [Review Section B's counter-hypothesis chain. Does mechanism analysis change the
  plausibility of the counter-hypothesis? Which I-NN condition is most dangerous?]
  Most dangerous I-NN: [ID + 1-sentence rationale]
  Revised inertia severity: [ ] Confirms Section B  [ ] Upgrades to ADVISORY  [ ] Upgrades to STOP

Final falsification table:

| ID   | Condition                      | Testability (Sec C)  | Confidence (Sec E)          | Rationale |
|------|--------------------------------|----------------------|-----------------------------|-----------|
| F-01 | [text]                         | [Easy/Hard/Unknown]  | [ ] High  [ ] Med  [ ] Low  | [1 sentence] |
| F-02 | [text]                         | [Easy/Hard/Unknown]  | [ ] High  [ ] Med  [ ] Low  | [1 sentence] |
| I-01 | [text]                         | [Easy/Hard/Unknown]  | [ ] High  [ ] Med  [ ] Low  | [1 sentence] |
| I-02 | [text]                         | [Easy/Hard/Unknown]  | [ ] High  [ ] Med  [ ] Low  | [1 sentence] |

Mechanism strength (final): [ ] Strong  [ ] Moderate  [ ] Weak  [ ] NA (STOP)
Final rationale: [1 sentence]

---

## AUDITOR

[Post-processing role. Runs after Section E. Reads all sections. Produces five diagnostics
and consolidated AMEND routing table. New: triple-gap joint diagnostic (Diagnostic 5).]

### Diagnostic 1: Mechanism Chain Observability Aggregate

| Hop   | Step                      | Observability (from Sec D)      |
|-------|---------------------------|---------------------------------|
| Hop 1 | X -> [intermediate A]     | [Observable / Partial / Opaque] |
| Hop 2 | [intermediate A] -> Y     | [Observable / Partial / Opaque] |

Observable: [Count]  |  Partial: [Count]  |  Opaque: [Count]  |  Total: [Count]
Chain observability pattern: [ ] AllObservable  [ ] Mixed  [ ] PredominantlyOpaque
Pattern rationale: [1 sentence]

### Diagnostic 2: Testability Yield (from Section C)

Refined: [Count]  |  Residual Unknown: [Count]  |  Residual IDs: [List or "None"]
F-NN residual: [Count]  |  I-NN residual: [Count]
Pool asymmetry: [1 sentence]
Yield quality: [ ] AllResolved  [ ] PartiallyResolved  [ ] Unresolved

### Diagnostic 3: I-NN Pool (from Section B)

I-NN count: [Total]  |  Pool coverage: [ ] Comprehensive  [ ] Adequate  [ ] Minimal
Coverage rationale: [1 sentence]
Counter-hypothesis dividend: [Did deriving I-NN from CH-Hops produce more mechanistically
  specific conditions than a table-seeded approach? Or: "Not determinable from this run."]

### Diagnostic 4: Inertia Pathway Observability (from Section B aggregate)

Inertia pathway observability: [From Section B B3 aggregate -- Observable/Partial/Opaque]
Comparison to mechanism chain: [One sentence: does inertia observability diverge from chain
  observability pattern? What does the divergence imply for the causal analysis?]

### Diagnostic 5: Triple-Gap Analysis (new joint diagnostic)

[A triple gap exists when all three conditions hold for a single falsification condition:
  1. The mechanism hop it cross-references (Section D) is Opaque
  2. Its testability is Unknown after Section C refinement
  3. An I-NN condition exists with the same or overlapping scope
A triple gap means: maximum causal uncertainty at a point.
We cannot observe the forward mechanism, cannot test the condition, and cannot rule out
that the inertia pathway produces Y at the same step.]

Triple-gap analysis:

| Condition ID | Hop observability | Testability (Sec C) | I-NN match? | Triple gap? |
|--------------|-------------------|---------------------|-------------|-------------|
| F-01         | [Sec D hop label] | [Easy/Hard/Unknown] | [I-NN ID or None] | [ ] Yes  [ ] No |
| F-02         | [Sec D hop label] | [Easy/Hard/Unknown] | [I-NN ID or None] | [ ] Yes  [ ] No |
| I-01         | [CH-Hop label]    | [Easy/Hard/Unknown] | [F-NN ID or None] | [ ] Yes  [ ] No |
| I-02         | [CH-Hop label]    | [Easy/Hard/Unknown] | [F-NN ID or None] | [ ] Yes  [ ] No |
[Mirror all conditions. I-NN conditions cross-reference F-NN matches, and vice versa.]

Triple-gap count: [How many conditions qualify?]
Triple-gap IDs: [List, or "None detected"]
Triple-gap severity: [ ] None  [ ] Advisory (1 gap)  [ ] Significant (2+ gaps)
Triple-gap implication: [One sentence: what does the triple-gap count mean for the
  reliability of this causal analysis? What is the recommended action?]

### AMEND Routing Table

| # | Diagnostic                    | Result                               | AMEND slot    | Routing |
|---|-------------------------------|--------------------------------------|---------------|---------|
| 1 | Chain observability pattern   | [AllObservable/Mixed/PredominantlyOpaque] | Observability | [Required if Mixed or PredominantlyOpaque / Not required] |
| 2 | Testability residual count    | [Count]                              | Testability   | [Required if > 0 / Not required] |
| 3 | Evidence quality              | [Strong/Moderate/Weak/None]          | Evidence      | [Required if None / Not required] |
| 4 | Inertia severity (final)      | [SAFE/ADVISORY/STOP]                 | Inertia       | [Required if ADVISORY or STOP / Not required] |
| 5 | Triple-gap count              | [Count]                              | Triple-gap    | [Required if count > 0 -- "Conditions [IDs] are triple gaps. These conditions carry maximum causal uncertainty and must be resolved before treating the causal claim as reliable."] |

AUDITOR note: [Most critical finding across all five diagnostics -- 1 sentence.]

---

## SECTION F: SCOPE AND AMEND

Scoped claim: ["X causes Y when [condition], for [population], assuming [precondition]."]
Out-of-scope: [At least one context where mechanism fails.]

Final inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP

AMEND DIRECTIVE:
[All Required slots from AUDITOR routing table. Always include Narrow + Mechanism.]

AMEND: discover-causal
  Narrow: [Scope tightening]
  Mechanism: [Hop notation: X -> [A] -> [B] -> Y]
  Falsification: [Highest-confidence condition from Section E table. ID + testability + confidence.
    If this condition is a triple gap, note it explicitly.]
  [Evidence: if AUDITOR row 3 = Required]
  [Inertia: if AUDITOR row 4 = Required -- reference most dangerous I-NN from Section E]
  [Observability: if AUDITOR row 1 = Required]
  [Testability: if AUDITOR row 2 = Required]
  [Triple-gap: if AUDITOR row 5 = Required]
    "Conditions [IDs] are triple gaps (Opaque hop + Unknown testability + I-NN match).
     These represent maximum causal uncertainty. Do not treat as supporting evidence for
     the claim until hop observability is improved, testability is determined, and the
     I-NN pathway is ruled out or bounded."

---

Write artifact: simulations/discover/causal/{topic}-causal-{date}.md
Frontmatter: skill, topic, date, cause (X), outcome (Y),
             combination_axes (counter-hypothesis-chain, auditor-role, section-letter),
             auditor_role (true), gate_checklists (4),
             inertia_verdict (SAFE/ADVISORY/STOP), baseline_rate,
             inertia_observability (Observable/Partial/Opaque),
             counter_hypothesis_hop_count,
             evidence_count, evidence_quality (Strong/Moderate/Weak/None),
             f_nn_count, i_nn_count, i_nn_pool_coverage (Comprehensive/Adequate/Minimal),
             i_nn_derivation (counter-hypothesis-chain),
             hop_count,
             mechanism_strength_preliminary, mechanism_strength_final, strength_changed (true/false),
             chain_observability_pattern (AllObservable/Mixed/PredominantlyOpaque),
             observability_amend_triggered (true/false),
             testability_refined_count, testability_residual_unknown_count,
             f_nn_residual_count, i_nn_residual_count, pool_asymmetry_detected (true/false),
             testability_amend_triggered (true/false),
             triple_gap_count, triple_gap_severity (None/Advisory/Significant),
             triple_gap_amend_triggered (true/false),
             amend_routing_rows_required (count), confounder_named (true/false).
```

---

### Round 7 Design Notes

**A-14 across five variations:**
All five generate a structured I-NN pool with at least two rows, same labeled columns as F-NN,
and testability starting Unknown. The derivation mechanism differs:
- V-01/V-02/V-04: table-seeded (FRAMER or section prompt lists inertia pathways)
- V-03: claim-context-free (generated before claim, possible independence dividend)
- V-05: chain-seeded (each I-NN derives from a CH-Hop challenge, strongest structural link)

**A-15 across five variations:**
All five produce a discrete Observable/Partial/Opaque label for the inertia pathway. The label
source differs:
- V-01/V-02/V-03/V-04: explicit dedicated field in the inertia/Step 3/Phase 3 section
- V-05: aggregate of counter-hypothesis hop labels (emergent from CH-Hop analysis)

**A-16 across five variations:**
All five have a named post-processing role with a structured routing table. Role names differ:
- V-01: SYNTHESIZER (5-row table, owns all four diagnostics)
- V-02: AUDITOR (4-row table, parallel-pool architecture)
- V-03: EVALUATOR (5-row table, adds inertia-observability as 5th row)
- V-04: EXAMINER (4-row table, interrogative framing)
- V-05: AUDITOR (5-row table, adds triple-gap diagnostic)

**V-01 vs R6-V-02 (AUDITOR) differentiation:**
R6-V-02 AUDITOR had 4 routing rows (chain-obs, testability, evidence, inertia). V-01 SYNTHESIZER
adds a 5th row (I-NN pool coverage -- Minimal triggers a Mechanism slot). The name change
from AUDITOR to SYNTHESIZER reflects the expanded ownership: SYNTHESIZER owns all four new
criteria (A-12, A-13, A-14, A-15) simultaneously, while R6-V-02 AUDITOR owned only A-12/A-13.

**New structural question seeded for R8:**
V-05 introduces I-NN derivation from counter-hypothesis hop challenges (chain-seeded). If
chain-seeded I-NN conditions are more mechanistically specific but harder to generate (longer
prompt, more analytical effort), the tradeoff is: do chain-seeded I-NN conditions produce
better AMEND guidance? R8 can test this by running V-01 (table-seeded) and V-05 (chain-seeded)
on the same hypothesis and comparing I-NN condition quality.
