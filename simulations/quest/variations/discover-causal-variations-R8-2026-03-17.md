1,857 lines. Here is the R8 design summary:

---

## Round 8 — 5 Variations

**Single-axis (three axes):**

| V | Axis | Key structural innovation |
|---|------|--------------------------|
| **V-01** | Lifecycle emphasis — hop-gap accumulation | Each mechanism hop includes an immediate `HOP-GAP CHECK` mini-record (gap candidate, gap type, note). The RESOLVER role aggregates from accumulated per-hop records; routing table rows carry a Traceable-source column citing specific hops that triggered each AMEND slot. |
| **V-02** | Output format — 5-column evidence table | All evidence lives in a structured table with a Mechanism-connection column forcing hop-level evidence citation at row-creation time. Routing table includes a hop-level evidence-coverage row (High/Partial/None) absent from R7 variations. |
| **V-03** | Inertia framing — H0 null hypothesis | Inertia is H0; the feature claim is H1. ANALYST labels each hop with H1/H0 distinguishability (Distinguishable/Indeterminate/Indistinguishable). ARBITER routing table row 3 is the H0-distinguishability diagnostic — a new row type not present in R7. |

**Combination (two axes each):**

| V | Axes combined | Key structural innovation |
|---|---------------|--------------------------|
| **V-04** | Role sequence + phrasing register | CHALLENGER role runs before ANALYST, generating 3–5 challenge questions the mechanism must survive. All instructions phrased as second-person questions. EXAMINER routing table row 4 is the CHALLENGER-survival diagnostic. Fails A-17. |
| **V-05** | Scope-inversion I-NN + AUDITOR + triple-gap | Each hop declares a validity-scope; I-NN conditions are derived by scope-inversion (one per hop, structurally paired). Triple-gap = F-NN connected to Opaque hop + Unknown testability; scope-paired I-NN existence is guaranteed by derivation. AUDITOR row 5 is the triple-gap diagnostic. Passes A-17. |

**New routing rows not in R7 (single-dimension):**
- V-01 RESOLVER: Traceable-source column
- V-02 AUDITOR row 3: Evidence-coverage (hop-level)
- V-03 ARBITER row 3: H0-distinguishability
- V-04 EXAMINER row 4: CHALLENGER-survival

**A-17 advancement:** V-05's scope-inversion derivation makes I-NN scope overlap structurally exact (no inference needed), producing a sharper triple-gap test than R7-V-05's chain-seeded approach.
p structurally exact for the triple-gap diagnostic (A-17). |

**R8 questions seeded:**
- Does hop-gap accumulation (V-01) produce more hop-traceable AMEND rationales than batch aggregation?
- Does the 5-column evidence table (V-02) shift analyst evidence-search from claim-level to hop-level?
- Does H0 framing (V-03) change inertia severity verdicts vs. prose-based inertia checks? Does it increase STOP verdicts?
- Does CHALLENGER-primed ordering (V-04) change mechanism chains -- do analysts write more conservative hops when adversarial questions are visible first?
- Does scope-inversion I-NN derivation (V-05) produce more structurally exact triple-gap matches than chain-seeded derivation (R7-V-05)?

---

## V-01: RESOLVER Role (Hop-Gap Accumulation)

**Axis:** Lifecycle emphasis -- each mechanism hop accumulates a per-hop gap record immediately
after it is written. The RESOLVER role aggregates these accumulated records rather than
recomputing observability and testability from scratch. Every hop carries: mechanism label,
observability, falsification connection, and a hop-gap mini-check. RESOLVER reads the
accumulated gap candidates, synthesizes four diagnostics, and produces a consolidated 5-row
AMEND routing table (A-16). No triple-gap row -- A-17 not targeted.

**Hypothesis:** In R7 variations, SYNTHESIZER/AUDITOR computed the chain observability aggregate
from hop labels collected in a separate role. When the mini gap-check is colocated with hop
construction, analysts immediately classify each hop as observable or not -- reducing the
cognitive distance between writing "Opaque" and understanding its routing consequence. The cost
is longer ANALYST output; the benefit is that RESOLVER's routing table is traceable: each
Required AMEND slot can cite the specific hop(s) that triggered it.

```
You are running /discover-causal.
Your input is a feature hypothesis of the form "X causes Y."
Five roles in sequence. Complete each role fully before advancing.
Every classification judgment uses a discrete label from a fixed set with a rationale line.

Role sequence:
  FRAMER (opening): claim, F-NN pool, I-NN pool, inertia baseline and observability,
    evidence with testability refinement.
  ANALYST: mechanism chain. Every hop includes a hop-gap mini-check immediately after
    the hop's observability label. ANALYST does not compute aggregates.
  SKEPTIC: adversarial challenge, confidence labels, final mechanism strength. Structurally
    separated from ANALYST. Does not compute aggregates.
  RESOLVER: reads accumulated hop-gap records from ANALYST plus FRAMER's yield data.
    Computes four diagnostics. Produces consolidated 5-row AMEND routing table.
  FRAMER (closing): scoped claim plus AMEND block built from RESOLVER routing table.

Two-pool falsification architecture:
  F-NN pool: claim-derived falsification conditions. Testability = Unknown at genesis.
  I-NN pool: inertia-derived falsification conditions. Same structure as F-NN.
Both pools undergo testability refinement in FRAMER Step 4.
Both pools receive confidence labels from SKEPTIC.
RESOLVER synthesizes both pools.

---

## FRAMER (OPENING)

[Establish the claim and both falsification pools. Complete all steps before advancing.]

### Step 1: Claim

X (the cause): [Extract from input]
Y (the claimed outcome): [Extract from input]
Full claim: ["X causes Y" -- one sentence, no mechanism embedded]

### Step 2: F-NN Pool

[Claim-derived falsification conditions. At least two. Testability = Unknown. No confidence.]

| ID   | Falsification condition (claim false if observed) | Testability | Rationale |
|------|---------------------------------------------------|-------------|-----------|
| F-01 | [What would show X does not cause Y?] | Unknown (see Step 4) | [1 sentence: what mechanism failure does this expose?] |
| F-02 | [A second distinct condition.] | Unknown (see Step 4) | [1 sentence] |
[Add F-NN as analysis generates more conditions.]

### Step 3: I-NN Pool and Inertia Analysis

[Generate at least two I-NN conditions naming distinct pathways by which Y could occur
without X. Establish inertia baseline and observability label BEFORE writing I-NN rows.]

Status-quo description: [One sentence: what happens today without X?]
Baseline rate: [Estimate or bound: "Y occurs in approximately __% of cases without X."
  Or: "Unknown -- [bounding reasoning]."]
Inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP
Inertia severity rationale: [1 sentence]

Inertia pathway observability: [ ] Observable  [ ] Partial  [ ] Opaque
  (Observable = direct measurement of Y rate without X is available;
   Partial = proxy data available, no direct measurement;
   Opaque = no path to observe whether status quo produces Y without X)
Inertia observability rationale: [1 sentence]

I-NN Pool:

| ID   | Inertia falsification condition | Testability | Rationale |
|------|---------------------------------|-------------|-----------|
| I-01 | Y occurs at [rate] without X via [mechanism 1] | Unknown (see Step 4) | [1 sentence: what makes this pathway plausible?] |
| I-02 | Y via [mechanism 2] without X | Unknown (see Step 4) | [1 sentence] |
[Add I-NN as inertia analysis generates more pathways.]

### Step 4: Evidence and Testability Refinement

[At least one context-specific observation, OR explicit "None found." Do not skip.]

Evidence entry 1:
  Source type: [ ] Prior result  [ ] Analogous case  [ ] Domain observation  [ ] Counter-evidence
  Observation: [What was seen, where, when?]
  Bearing on X->Y: [Supports / Complicates / Challenges -- 1 sentence]

[Add entries as needed.]

Evidence quality: [ ] Strong  [ ] Moderate  [ ] Weak  [ ] None
Evidence quality rationale: [1 sentence]

Testability refinement -- all F-NN and I-NN conditions:

| ID   | Testability after evidence | Refinement rationale |
|------|---------------------------|----------------------|
| F-01 | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence] |
| F-02 | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence] |
| I-01 | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence] |
| I-02 | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence] |
[Mirror all F-NN and I-NN conditions.]

Testability refinement yield:
  testability_refined_count: [Conditions moved from Unknown to Easy or Hard]
  testability_residual_unknown_count: [Conditions still Unknown after evidence]
  Residual Unknown IDs: [List, or "None"]
  F-NN residual: [Count]  |  I-NN residual: [Count]

FRAMER (OPENING) GATE:
[ ] X and Y extracted separately
[ ] At least two F-NN conditions (Unknown testability, no confidence)
[ ] At least two I-NN conditions (Unknown testability, no confidence)
[ ] Baseline rate declared (estimate, bound, or explicit "Unknown")
[ ] Inertia severity label with rationale
[ ] Inertia pathway observability label with rationale
[ ] Evidence populated (or explicit "None found")
[ ] Evidence quality label with rationale
[ ] Testability refinement complete for all F-NN and I-NN conditions
[ ] testability_refined_count and testability_residual_unknown_count declared with pool breakdown

--- Do not advance to ANALYST until all gate items are checked. ---

---

## ANALYST

[Map the causal chain from X to Y. Two hops minimum.
CRITICAL: after each hop's observability label, immediately write a hop-gap mini-check.
The hop-gap mini-check is a two-field record colocated with the hop that RESOLVER reads.
ANALYST does not compute chain-level aggregates -- RESOLVER does that from accumulated records.]

Hop 1: X [name] -> [intermediate A]: [How does X produce A?]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Observability rationale: [1 sentence: how directly can this intermediate be detected?]
  Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
  Falsification connection: [F-NN or I-NN ID. One sentence: if this hop fails, which condition holds?]
  HOP-GAP CHECK:
    Gap candidate: [ ] Yes (Opaque or Partial)  [ ] No (Observable)
    Gap type if Yes: [ ] Observability-gap  [ ] Evidence-gap  [ ] Both
    Note: [1 sentence: what would close this gap?]

Hop 2: [intermediate A] -> Y: [How does A produce Y?]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Observability rationale: [1 sentence]
  Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
  Falsification connection: [F-NN or I-NN ID. One sentence.]
  HOP-GAP CHECK:
    Gap candidate: [ ] Yes  [ ] No
    Gap type if Yes: [ ] Observability-gap  [ ] Evidence-gap  [ ] Both
    Note: [1 sentence]

[Add Hop 3+ as needed. Every hop must include the hop-gap mini-check immediately below it.]

Mechanism strength (preliminary): [ ] Strong  [ ] Moderate  [ ] Weak
Preliminary rationale: [1 sentence]

Gap candidate summary (ANALYST output for RESOLVER):
  Total gap candidates: [Count of hops marked Gap candidate = Yes]
  Opaque hops: [Count]  |  Partial hops: [Count]  |  Observable hops: [Count]

ANALYST GATE:
[ ] At least two hops filled with mechanism text
[ ] Every hop: observability + rationale, evidence coherence, falsification connection
[ ] Every hop: hop-gap mini-check filled immediately below the hop
[ ] Mechanism strength (preliminary) with rationale
[ ] Gap candidate summary complete
[ ] No confidence labels (SKEPTIC's job)
[ ] No chain-level aggregate computed (RESOLVER's job)

--- Do not advance to SKEPTIC until all gate items are checked. ---

---

## SKEPTIC

[Challenge every mechanism hop. Assign confidence to all F-NN and I-NN conditions.
Produce final mechanism strength. Structurally separate section -- no mechanism construction here.]

Hop-by-hop challenge:

  Hop 1 challenge:
    Breaks X -> [A] when: [Observable condition that disproves this hop]
    Observable test: [What to measure]
    Alternative at this hop: [What else produces [A] without X?]
    Confidence on Hop 1 mechanism: [ ] High  [ ] Medium  [ ] Low
    Confidence rationale: [1 sentence]

  Hop 2 challenge:
    Breaks [A] -> Y when: [Observable condition]
    Observable test: [What to measure]
    Alternative at this hop: [What else produces Y without [A]?]
    Confidence on Hop 2 mechanism: [ ] High  [ ] Medium  [ ] Low
    Confidence rationale: [1 sentence]

  [Mirror all ANALYST hops.]

Confounders:
  Confounder 1: [Variable correlating with both X and Y. Name and describe.]

Inertia challenge:
  Adversarial view: [Could baseline effects or I-NN pathways explain observed Y?]
  Most dangerous I-NN: [ID + 1-sentence rationale]
  Revised inertia severity: [ ] Confirms FRAMER  [ ] Upgrades to ADVISORY  [ ] Upgrades to STOP

Final falsification table (FRAMER testability + SKEPTIC confidence):

| ID   | Condition | Testability (FRAMER) | Confidence (SKEPTIC) | Rationale |
|------|-----------|----------------------|----------------------|-----------|
| F-01 | [text] | [FRAMER Step 4 label] | [ ] High  [ ] Med  [ ] Low | [1 sentence] |
| F-02 | [text] | [FRAMER Step 4 label] | [ ] High  [ ] Med  [ ] Low | [1 sentence] |
| I-01 | [text] | [FRAMER Step 4 label] | [ ] High  [ ] Med  [ ] Low | [1 sentence] |
| I-02 | [text] | [FRAMER Step 4 label] | [ ] High  [ ] Med  [ ] Low | [1 sentence] |
[Mirror all conditions. Testability column carries FRAMER labels unchanged.]

Mechanism strength (final): [ ] Strong  [ ] Moderate  [ ] Weak
Final rationale: [1 sentence. State whether changed from ANALYST preliminary and why.]

SKEPTIC GATE:
[ ] Every hop challenged with observable test and alternative
[ ] Confidence assigned to all F-NN and I-NN conditions
[ ] Final falsification table complete
[ ] Inertia challenge references a specific I-NN condition by ID
[ ] Final mechanism strength declared with rationale
[ ] At least one confounder named

--- Do not advance to RESOLVER until all gate items are checked. ---

---

## RESOLVER

[Post-processing role. Reads ANALYST's accumulated hop-gap records, FRAMER's testability yield,
and FRAMER's inertia observability. Aggregates four diagnostics from hop-level records.
Produces consolidated 5-row AMEND routing table. Does not challenge mechanism or assign confidence.]

### Diagnostic 1: Chain Observability Aggregate (from ANALYST hop-gap records)

[Read the gap candidate summary from ANALYST. Do not recount -- aggregate from ANALYST output.]

  Opaque hops (from ANALYST): [Count]
  Partial hops (from ANALYST): [Count]
  Observable hops (from ANALYST): [Count]
  Total hops: [Count]
  Chain observability pattern: [ ] AllObservable  [ ] Mixed  [ ] PredominantlyOpaque
  Pattern rationale: [1 sentence]
  Hops with gap candidate = Yes: [List hop numbers, or "None"]
  AMEND trigger: [Required if Mixed or PredominantlyOpaque / Not required]

### Diagnostic 2: Testability Residual Yield (from FRAMER)

  testability_residual_unknown_count (from FRAMER): [Value]
  Residual Unknown IDs: [From FRAMER, or "None"]
  F-NN residual: [Count]  |  I-NN residual: [Count]
  Pool asymmetry: [Are I-NN conditions disproportionately Unknown? 1 sentence]
  AMEND trigger: [Required if residual count > 0 / Not required]

### Diagnostic 3: I-NN Pool Synthesis (from FRAMER + SKEPTIC)

  I-NN condition count: [Total]
  I-NN conditions with Unknown testability: [List IDs, or "None"]
  I-NN conditions with Low confidence (SKEPTIC): [List IDs, or "None"]
  Pool coverage: [ ] Comprehensive  [ ] Adequate  [ ] Minimal
  Pool coverage rationale: [1 sentence]
  Most dangerous I-NN: [ID from SKEPTIC inertia challenge]
  AMEND trigger: [Required if Minimal / Not required]

### Diagnostic 4: Inertia Pathway Observability (from FRAMER)

  Inertia pathway observability (from FRAMER): [Observable / Partial / Opaque]
  Comparison to chain: [1 sentence: does inertia observability diverge from chain pattern?]
  AMEND trigger: [Required if Opaque and chain observability AMEND not already Required / Not required]

### Consolidated AMEND Routing Table

[5-row routing table. Each row cites the hop(s) or condition(s) that produced the finding.]

| # | Diagnostic | Result | Traceable source | AMEND slot | Routing |
|---|-----------|--------|------------------|------------|---------|
| 1 | Chain observability | [AllObservable/Mixed/PredominantlyOpaque] | Hop(s) [list gap candidates] | Observability | [Required / Not required] |
| 2 | Testability residual | [Count] | Conditions [IDs] | Testability | [Required if > 0 / Not required] |
| 3 | Evidence quality | [Strong/Moderate/Weak/None] | FRAMER Step 4 | Evidence | [Required if None / Not required] |
| 4 | Inertia severity (final) | [SAFE/ADVISORY/STOP] | SKEPTIC revision | Inertia | [Required if ADVISORY or STOP / Not required] |
| 5 | I-NN pool coverage | [Comprehensive/Adequate/Minimal] | FRAMER Step 3 | Mechanism | [Required if Minimal / Not required] |

RESOLVER note: [Most critical gap across all four diagnostics -- 1 sentence.]

RESOLVER GATE:
[ ] Four diagnostics complete
[ ] Every routing table row filled with result, traceable source, and routing decision
[ ] Pool asymmetry note present
[ ] Chain vs inertia observability comparison present
[ ] At least one row marked Required (if none, flag anomaly)

--- Do not advance to FRAMER (CLOSING) until all gate items are checked. ---

---

## FRAMER (CLOSING)

[Build scoped claim and AMEND block from RESOLVER routing table. AMEND slots derived
mechanically from RESOLVER rows marked Required. Always include Narrow and Mechanism.]

Scoped claim: ["X causes Y when [condition], for [population], assuming [precondition]."]
Out-of-scope: [At least one context where mechanism fails, from SKEPTIC challenge.]

Final inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP
Inertia rationale: [1 sentence. Use SKEPTIC's revised verdict if upgraded.]

AMEND DIRECTIVE:

AMEND: discover-causal
  Narrow: [Scope tightening -- match scoped claim condition]
  Mechanism: [Hop notation: X -> [A] -> [B] -> Y with actual intermediate names]
  Falsification: [Highest-confidence condition from SKEPTIC table. ID + testability + confidence.
    Cite the hop that triggered this condition (from ANALYST falsification connection).]
  [Evidence: if RESOLVER row 3 = Required]
    "Mechanism is theoretical. Cite one context-specific observation before next decision gate."
  [Inertia: if RESOLVER row 4 = Required]
    "Y occurs at [baseline rate] via [most dangerous I-NN from RESOLVER Diagnostic 3].
     Demonstrate incremental Y above this baseline."
  [Observability: if RESOLVER row 1 = Required]
    "Hops [list from RESOLVER traceable source] are [Opaque/Partial]. Require proxy measurements
     or claim narrowing to the observable portion before treating mechanism as confirmed."
  [Testability: if RESOLVER row 2 = Required]
    "Conditions [list IDs from RESOLVER Diagnostic 2] have Unknown testability. Determine
     instrumentation before treating these as actionable falsification targets."

---

Write artifact: simulations/discover/causal/{topic}-causal-{date}.md
Frontmatter: skill, topic, date, cause (X), outcome (Y),
             role_sequence (FRAMER-ANALYST-SKEPTIC-RESOLVER-FRAMER), role_count (5),
             gate_checklists (5),
             inertia_verdict (SAFE/ADVISORY/STOP), baseline_rate,
             inertia_observability (Observable/Partial/Opaque),
             evidence_count, evidence_quality (Strong/Moderate/Weak/None),
             f_nn_count, i_nn_count, i_nn_pool_coverage (Comprehensive/Adequate/Minimal),
             hop_count,
             mechanism_strength_preliminary, mechanism_strength_final, strength_changed (true/false),
             chain_observability_pattern (AllObservable/Mixed/PredominantlyOpaque),
             hop_gap_candidates (count of hops with gap_candidate=Yes),
             observability_amend_triggered (true/false),
             testability_refined_count, testability_residual_unknown_count,
             f_nn_residual_count, i_nn_residual_count, pool_asymmetry_detected (true/false),
             testability_amend_triggered (true/false),
             amend_routing_rows_required (count), confounder_named (true/false).
```

---

## V-02: Evidence Table with Mechanism-Connection Column

**Axis:** Output format -- the evidence section uses a strict 5-column table throughout.
Every evidence row carries a Mechanism-connection field citing which hop or claim the evidence
bears on. This creates bidirectional tracing: evidence -> mechanism hop. Evidence coverage is
assessed as a hop-level label (High/Partial/None) in addition to a global quality label.

**Hypothesis:** In R7 variations, evidence was gathered at claim level and annotated afterward
with mechanism bearing. When the evidence table forces a Mechanism-connection field at
row-creation time, analysts search for hop-specific evidence rather than claim-general evidence.
The coverage label surfaces evidence gaps at the hop level. A mechanism with AllObservable hops
but Partial evidence coverage is a qualitatively different risk than one with Mixed observability
and High evidence coverage -- this format makes that distinction visible before AMEND routing.

```
You are running /discover-causal.
Your input is a feature hypothesis of the form "X causes Y."
Six sections in sequence. Complete each fully before advancing.
Every classification judgment uses a discrete label from a fixed set with a rationale line.

Evidence architecture: all evidence lives in a 5-column table with a Mechanism-connection column.
  Evidence is gathered in Section 1 (before mechanism construction -- A-05 gate).
  Testability refinement runs in Section 1 after evidence is complete.
Dual-pool falsification: F-NN (Section 1) and I-NN (Section 2) tables, same 5-column structure.
AUDITOR role: runs after Section 5. Produces AMEND routing table with 5 rows.

---

## SECTION 1: CLAIM, EVIDENCE, AND F-NN POOL

[Complete in this order: claim extraction -> evidence table -> F-NN pool -> testability refinement.
Evidence precedes the F-NN pool because evidence shapes which falsification conditions to write.]

### 1.1 Claim Extraction

X (the cause): [Extract from input]
Y (the claimed outcome): [Extract from input]
Full claim: ["X causes Y" -- one sentence, no mechanism embedded]

### 1.2 Evidence Table

[Gather evidence FIRST. Use the 5-column format below. Every row requires a Mechanism-connection
field. At this stage, mechanism hops have not been named; use approximate labels like "X->Y link"
or the causal step you expect. Section 4 (ANALYST) will confirm these labels.
At least one evidence entry, OR an explicit "None found" row.]

| ID   | Source type | Observation | Bearing | Mechanism-connection |
|------|-------------|-------------|---------|----------------------|
| E-01 | [Prior result / Analogous case / Domain observation / Counter-evidence] | [What was seen, where, when?] | [Supports / Complicates / Challenges] | [Which hop or claim does this bear on? e.g., "X->A link", "A->Y link", "overall X->Y"] |
[Add rows as needed. Write "None found" as a single row with Bearing = N/A if no evidence.]

Evidence quality: [ ] Strong  [ ] Moderate  [ ] Weak  [ ] None
Evidence quality rationale: [1 sentence]

### 1.3 F-NN Pool

[Claim-derived falsification conditions. At least two. Testability = Unknown. Confidence = Pending.]

| ID   | Condition (claim false if observed) | Testability | Confidence | Rationale |
|------|-------------------------------------|-------------|------------|-----------|
| F-01 | [What would show X does not cause Y?] | Unknown (see 1.4) | Pending | [1 sentence] |
| F-02 | [Second distinct condition] | Unknown (see 1.4) | Pending | [1 sentence] |

### 1.4 Testability Refinement -- F-NN

| ID   | Testability after evidence | Refinement rationale |
|------|---------------------------|----------------------|
| F-01 | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence] |
| F-02 | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence] |

F-NN testability yield:
  f_nn_refined_count: [Moved from Unknown to Easy or Hard]
  f_nn_residual_unknown_count: [Still Unknown after evidence]

SECTION 1 GATE:
[ ] X and Y extracted
[ ] Evidence table complete (or explicit "None found" row)
[ ] Evidence quality label with rationale
[ ] At least two F-NN conditions (Unknown testability, Pending confidence)
[ ] F-NN testability refinement complete
[ ] No mechanism hop names in this section (ANALYST Section 4 owns mechanism)

--- Do not advance to Section 2 until all gate items are checked. ---

---

## SECTION 2: I-NN POOL AND INERTIA ANALYSIS

[Establish inertia baseline and observability label BEFORE writing I-NN rows.
I-NN pool uses the same 5-column format as F-NN pool.]

Status-quo description: [One sentence: what happens today without X?]
Baseline rate: [Estimate or bound, or "Unknown -- [reasoning]."]
Inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP
Inertia severity rationale: [1 sentence]

Inertia pathway observability: [ ] Observable  [ ] Partial  [ ] Opaque
  (Observable = direct measurement of Y rate without X is achievable;
   Partial = proxy indicators exist, no direct measurement;
   Opaque = no available path to observe whether status quo produces Y)
Inertia observability rationale: [1 sentence]

I-NN Pool:

| ID   | Inertia condition (Y without X via this pathway) | Testability | Confidence | Rationale |
|------|--------------------------------------------------|-------------|------------|-----------|
| I-01 | Y occurs at [rate] without X via [mechanism 1] | Unknown (see 2.1) | Pending | [1 sentence] |
| I-02 | Y via [mechanism 2] without X | Unknown (see 2.1) | Pending | [1 sentence] |
[Add I-NN as needed.]

### 2.1 Testability Refinement -- I-NN

| ID   | Testability after evidence | Refinement rationale |
|------|---------------------------|----------------------|
| I-01 | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence] |
| I-02 | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence] |

I-NN testability yield:
  i_nn_refined_count: [Moved from Unknown]
  i_nn_residual_unknown_count: [Still Unknown]

Combined testability yield (F-NN + I-NN):
  testability_refined_count: [Total moved from Unknown]
  testability_residual_unknown_count: [Total still Unknown]
  Residual Unknown IDs: [List by pool]

SECTION 2 GATE:
[ ] Baseline rate declared
[ ] Inertia severity with rationale
[ ] Inertia pathway observability with rationale (before I-NN rows)
[ ] At least two I-NN conditions (Unknown testability, Pending confidence)
[ ] I-NN testability refinement complete
[ ] Combined testability yield declared

--- Do not advance to Section 3 until gate is checked. ---
--- IF inertia severity is STOP: skip to Section 5 (SKEPTIC). ---

---

## SECTION 3: EVIDENCE COVERAGE PRE-CHECK

[Before mechanism hops are named, estimate hop-level evidence coverage from the
Mechanism-connection labels in the Section 1.2 evidence table.]

Distinct mechanism-connection labels in evidence table: [List labels from column 5]
Coverage estimate: [ ] High (evidence covers most expected hops)
                   [ ] Partial (some expected hops lack evidence)
                   [ ] None (no evidence, or evidence only at claim level)
Coverage rationale: [1 sentence: which expected hops appear uncovered?]
Coverage AMEND trigger: [Required if None or Partial -- flag for AUDITOR]

---

## SECTION 4: ANALYST -- MECHANISM CHAIN

[Map the causal chain. Two hops minimum. Every hop cross-references Section 1.2 evidence
by ID in the Evidence coherence field.]

Hop 1: X [name] -> [intermediate A]: [Mechanism text]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Observability rationale: [1 sentence]
  Evidence coherence: [E-NN IDs from Section 1.2 that bear on this hop. Or: "No evidence."]
  Coherence verdict: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
  Falsification connection: [F-NN or I-NN ID. 1 sentence: if this hop fails, which condition holds?]

Hop 2: [intermediate A] -> Y: [Mechanism text]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Observability rationale: [1 sentence]
  Evidence coherence: [E-NN IDs. Or: "No evidence."]
  Coherence verdict: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
  Falsification connection: [F-NN or I-NN ID. 1 sentence.]

[Add Hop 3+ as needed. Every hop: observability, evidence coherence with E-NN IDs,
falsification connection.]

Mechanism strength (preliminary): [ ] Strong  [ ] Moderate  [ ] Weak
Preliminary rationale: [1 sentence]

Evidence coverage update:
  Final coverage label: [ ] High  [ ] Partial  [ ] None
  Uncovered hops (if Partial or None): [List hop names]

SECTION 4 GATE:
[ ] At least two hops
[ ] Every hop: observability + rationale, evidence coherence with E-NN IDs, falsification connection
[ ] Mechanism strength (preliminary) with rationale
[ ] Evidence coverage label updated

--- Do not advance to Section 5 until gate is checked. ---

---

## SECTION 5: SKEPTIC -- ADVERSARIAL CHALLENGE

[Structurally separated from Section 4. Assign confidence to all F-NN and I-NN conditions.
Challenge every mechanism hop. Produce final mechanism strength.]

Hop-by-hop challenge:

  Hop 1 challenge:
    Breaks X -> [A] when: [Condition that disproves this hop]
    Alternative at this hop: [What else produces [A] without X?]
    Confidence: [ ] High  [ ] Med  [ ] Low
    Confidence rationale: [1 sentence]

  Hop 2 challenge:
    Breaks [A] -> Y when: [Condition]
    Alternative at this hop: [What else produces Y without [A]?]
    Confidence: [ ] High  [ ] Med  [ ] Low
    Confidence rationale: [1 sentence]

  [Mirror all Section 4 hops.]

Confounders: [At least one variable correlating with both X and Y.]

Inertia challenge:
  Most dangerous I-NN: [ID + 1 sentence]
  Revised inertia severity: [ ] Confirms Section 2  [ ] Upgrades to ADVISORY  [ ] STOP

Final falsification table:

| ID   | Condition | Testability | Confidence | Rationale |
|------|-----------|-------------|------------|-----------|
| F-01 | [text] | [Section 1.4] | [ ] High  [ ] Med  [ ] Low | [1 sentence] |
| F-02 | [text] | [Section 1.4] | [ ] High  [ ] Med  [ ] Low | [1 sentence] |
| I-01 | [text] | [Section 2.1] | [ ] High  [ ] Med  [ ] Low | [1 sentence] |
| I-02 | [text] | [Section 2.1] | [ ] High  [ ] Med  [ ] Low | [1 sentence] |
[Mirror all conditions. Testability carries Section 1.4/2.1 labels unchanged.]

Mechanism strength (final): [ ] Strong  [ ] Moderate  [ ] Weak
Final rationale: [1 sentence. Note if changed from preliminary.]

SECTION 5 GATE:
[ ] Every hop challenged
[ ] Confidence assigned to all F-NN and I-NN conditions
[ ] Final falsification table complete
[ ] Inertia challenge with specific I-NN ID
[ ] Final mechanism strength with rationale

--- Do not advance to AUDITOR until gate is checked. ---

---

## AUDITOR

[Post-processing role. Computes four diagnostics and AMEND routing table from all sections.]

### Diagnostic 1: Chain Observability

  Observable: [Count]  |  Partial: [Count]  |  Opaque: [Count]  |  Total: [Count]
  Chain observability pattern: [ ] AllObservable  [ ] Mixed  [ ] PredominantlyOpaque
  Opaque hop IDs (for AMEND traceability): [List, or "None"]
  AMEND trigger: [Required if Mixed or PredominantlyOpaque / Not required]

### Diagnostic 2: Testability Residual

  testability_residual_unknown_count (combined): [From Section 2 yield]
  Residual Unknown IDs: [F-NN list] + [I-NN list]
  Pool asymmetry: [1 sentence]
  AMEND trigger: [Required if count > 0 / Not required]

### Diagnostic 3: Evidence Coverage

  Final coverage label (from Section 4): [High / Partial / None]
  Uncovered hops: [List, or "None"]
  AMEND trigger: [Required if None or Partial / Not required]

### Diagnostic 4: Inertia Severity + Observability

  Inertia severity (Section 5 final): [SAFE / ADVISORY / STOP]
  Inertia pathway observability (Section 2): [Observable / Partial / Opaque]
  Chain vs inertia observability: [1 sentence]
  AMEND trigger: [Required if ADVISORY or STOP / Not required]

### AMEND Routing Table

| # | Diagnostic | Result | AMEND slot | Routing |
|---|-----------|--------|------------|---------|
| 1 | Chain observability | [pattern] | Observability | [Required / Not required] |
| 2 | Testability residual | [count] | Testability | [Required if > 0 / Not required] |
| 3 | Evidence coverage | [High/Partial/None] | Evidence | [Required if Partial or None / Not required] |
| 4 | Inertia severity | [SAFE/ADVISORY/STOP] | Inertia | [Required if ADVISORY or STOP / Not required] |
| 5 | I-NN pool coverage | [Comprehensive/Adequate/Minimal] | Mechanism | [Required if Minimal / Not required] |

AUDITOR note: [Most critical gap -- 1 sentence.]

---

## SECTION 6: FRAMER (CLOSING)

Scoped claim: ["X causes Y when [condition], for [population], assuming [precondition]."]
Out-of-scope: [Context where mechanism fails, from Section 5 challenge.]

Final inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP

AMEND DIRECTIVE:

AMEND: discover-causal
  Narrow: [Scope tightening]
  Mechanism: [X -> [A] -> [B] -> Y with actual intermediate names]
  Falsification: [Highest-confidence condition from Section 5 table. ID + testability + confidence.]
  [Evidence: if AUDITOR row 3 = Required]
    "Evidence coverage: [Partial/None]. Hops [list uncovered] lack evidence.
     Cite at least one context-specific observation per uncovered hop."
  [Inertia: if AUDITOR row 4 = Required]
    "Y occurs at [baseline] via [most dangerous I-NN]. Demonstrate incremental Y above baseline."
  [Observability: if AUDITOR row 1 = Required]
    "Hops [list Opaque] require proxy measurements or claim narrowing."
  [Testability: if AUDITOR row 2 = Required]
    "Conditions [list IDs] have Unknown testability. Determine instrumentation."

---

Write artifact: simulations/discover/causal/{topic}-causal-{date}.md
Frontmatter: skill, topic, date, cause (X), outcome (Y),
             format_axis (evidence-table-5col), evidence_table_rows (count),
             evidence_coverage_label (High/Partial/None), uncovered_hops (count),
             f_nn_count, i_nn_count, inertia_verdict, baseline_rate,
             inertia_observability, hop_count,
             chain_observability_pattern, observability_amend_triggered (true/false),
             testability_refined_count, testability_residual_unknown_count,
             f_nn_residual_count, i_nn_residual_count, pool_asymmetry_detected (true/false),
             testability_amend_triggered (true/false),
             mechanism_strength_preliminary, mechanism_strength_final, strength_changed (true/false),
             evidence_coverage_amend_triggered (true/false),
             amend_routing_rows_required (count), confounder_named (true/false).
```

---

## V-03: H0 Null-Hypothesis Inertia Framing

**Axis:** Inertia framing -- the status quo is formalized as the null hypothesis H0. The claim
is an alternative hypothesis H1. The inertia check becomes "Establish H0 before testing H1."
The I-NN pool is H0 pathways. The AMEND block includes an H0/H1 distinguishability verdict.
The post-processing role is named ARBITER. Its routing table includes an H0-distinguishability
row absent from all R7 variations.

**Hypothesis:** Prose-based inertia checks allow analysts to assign SAFE with minimal evidence
by framing inertia as unlikely. H0 framing inverts the burden: the null is assumed true until
the mechanism produces a distinguishable signal. Analysts who must explicitly reject H0 before
accepting H1 are more likely to produce ADVISORY/STOP verdicts and surface missing evidence.
The H0-distinguishability routing row adds a diagnostic unavailable in R7: it asks not whether
inertia is dangerous, but whether the mechanism is distinguishable from inertia at observable hops.

```
You are running /discover-causal.
Your input is a feature hypothesis of the form "X causes Y."
Five roles in sequence. Complete each role fully before advancing.
Every classification judgment uses a discrete label from a fixed set with a rationale line.

Causal framing:
  H0 (null hypothesis): Y occurs at baseline rate R0 without X. This is the inertia hypothesis.
  H1 (feature hypothesis): X increases Y above R0. This is the claim under test.
  The analysis asks: does the evidence support H1 over H0, and at which mechanism hops
  is H1 distinguishable from H0?

Role sequence:
  FRAMER-H0: establish the null first. Generate I-NN pool (H0 pathways) and baseline rate.
  FRAMER-H1: generate the claim, F-NN pool, evidence, testability refinement.
  ANALYST: mechanism chain for H1. Each hop answers: is H1 distinguishable from H0 here?
  SKEPTIC: adversarial challenge, confidence labels, final strength.
  ARBITER: H0/H1 distinguishability diagnostic + consolidated AMEND routing table.
  FRAMER (CLOSING): scoped claim, AMEND from ARBITER routing table.

---

## FRAMER-H0 (NULL ESTABLISHMENT)

[Establish H0 before examining H1. This forces analysts to specify the baseline before
committing to a mechanism -- the most common way inertia is underweighted.]

### H0.1: Null Hypothesis Statement

H0 label: ["Y occurs at baseline rate R0 without X, via natural or existing mechanisms."]
Status-quo description: [One sentence: what produces Y today without X?]
Baseline rate R0: [Estimate or bound: "Y occurs in approximately __% of cases without X."
  Or: "R0 = Unknown -- [bounding reasoning: what data would resolve this?]"]

H0 severity: [ ] SAFE (R0 near zero -- X would be primary Y-producer)
             [ ] ADVISORY (R0 meaningful -- X would be additive, not primary)
             [ ] STOP (R0 already high -- X adds marginal signal at best)
H0 severity rationale: [1 sentence]

### H0.2: Inertia Pathway Observability

Inertia pathway observability: [ ] Observable  [ ] Partial  [ ] Opaque
  (Can we directly measure R0? Observable = yes; Partial = proxy only; Opaque = no path)
Inertia observability rationale: [1 sentence: what instrumentation would resolve this?]

### H0.3: I-NN Pool (H0 pathways)

[Enumerate the specific mechanisms by which Y occurs at rate R0 without X.
Each I-NN condition is a named H0 pathway. At least two. Testability = Unknown at genesis.]

| ID   | H0 pathway (Y occurs without X via this mechanism) | Testability | Rationale |
|------|-----------------------------------------------------|-------------|-----------|
| I-01 | [Mechanism 1 producing Y without X] | Unknown (see H1.3) | [1 sentence] |
| I-02 | [Mechanism 2 producing Y without X] | Unknown (see H1.3) | [1 sentence] |
[Add I-NN conditions as H0 analysis generates more pathways.]

FRAMER-H0 GATE:
[ ] H0 statement written
[ ] Baseline rate R0 declared (estimate, bound, or explicit "Unknown")
[ ] H0 severity label with rationale
[ ] Inertia pathway observability label with rationale
[ ] At least two I-NN conditions (Unknown testability, no confidence yet)

--- Do not advance to FRAMER-H1 until gate is checked. ---

---

## FRAMER-H1 (CLAIM ESTABLISHMENT)

### H1.1: Claim Statement

X (the cause): [Extract from input]
Y (the claimed outcome): [Extract from input]
Full H1 claim: ["X causes Y above baseline R0" -- one sentence]

### H1.2: F-NN Pool (H1 falsification conditions)

[Conditions that would disprove H1. At least two. Testability = Unknown. Confidence = Pending.]

| ID   | Condition (H1 false if observed) | Testability | Confidence | Rationale |
|------|----------------------------------|-------------|------------|-----------|
| F-01 | [What would show X does not cause Y above R0?] | Unknown (see H1.3) | Pending | [1 sentence] |
| F-02 | [Second distinct condition] | Unknown (see H1.3) | Pending | [1 sentence] |

### H1.3: Evidence and Joint Testability Refinement

[Evidence bearing on X->Y. At least one entry, or explicit "None found."]

Evidence entry 1:
  Source type: [ ] Prior result  [ ] Analogous case  [ ] Domain observation  [ ] Counter-evidence
  Observation: [What was seen?]
  Bearing on H1 vs H0: [Favors H1 / Favors H0 / Neutral -- 1 sentence]

[Add entries as needed.]

Evidence quality: [ ] Strong  [ ] Moderate  [ ] Weak  [ ] None
Evidence quality rationale: [1 sentence]

Testability refinement -- all F-NN and I-NN conditions:

| ID   | Testability after evidence | Pool | Refinement rationale |
|------|---------------------------|------|----------------------|
| F-01 | [ ] Easy  [ ] Hard  [ ] Unknown | F-NN | [1 sentence] |
| F-02 | [ ] Easy  [ ] Hard  [ ] Unknown | F-NN | [1 sentence] |
| I-01 | [ ] Easy  [ ] Hard  [ ] Unknown | I-NN | [1 sentence] |
| I-02 | [ ] Easy  [ ] Hard  [ ] Unknown | I-NN | [1 sentence] |
[Mirror all conditions.]

Testability refinement yield:
  testability_refined_count: [Total moved from Unknown]
  testability_residual_unknown_count: [Total still Unknown]
  Residual Unknown IDs: [List by pool]

FRAMER-H1 GATE:
[ ] X and Y extracted
[ ] H1 claim states Y above R0
[ ] At least two F-NN conditions
[ ] Evidence populated (or explicit "None found")
[ ] Evidence quality label assigned
[ ] Testability refinement complete for all F-NN and I-NN
[ ] Yield counts declared

--- Do not advance to ANALYST until gate is checked. ---

---

## ANALYST

[Map the causal chain for H1. Two hops minimum. At each hop, explicitly answer:
is H1 distinguishable from H0 at this step? An Observable hop may still be indistinguishable
from H0 if both H1 and H0 predict the same intermediate state at that hop.]

Hop 1: X [name] -> [intermediate A]: [How does X produce A?]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Observability rationale: [1 sentence]
  H1 vs H0 distinguishability at this hop: [ ] Distinguishable  [ ] Indeterminate  [ ] Indistinguishable
  Distinguishability rationale: [1 sentence: would H0 pathways also produce [A]? How would we tell them apart?]
  Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
  Falsification connection: [F-NN or I-NN ID. 1 sentence.]

Hop 2: [intermediate A] -> Y: [How does A produce Y?]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Observability rationale: [1 sentence]
  H1 vs H0 distinguishability at this hop: [ ] Distinguishable  [ ] Indeterminate  [ ] Indistinguishable
  Distinguishability rationale: [1 sentence]
  Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
  Falsification connection: [F-NN or I-NN ID. 1 sentence.]

[Add Hop 3+ as needed. Every hop includes both observability and distinguishability labels.]

Mechanism strength (preliminary): [ ] Strong  [ ] Moderate  [ ] Weak
Preliminary rationale: [1 sentence]

Distinguishability summary: [ ] AllDistinguishable  [ ] Mixed  [ ] Indeterminate
  (AllDistinguishable = every hop distinguishable from H0;
   Mixed = some distinguishable, some not;
   Indeterminate = at least one hop is H1/H0 indistinguishable)

ANALYST GATE:
[ ] At least two hops
[ ] Every hop: observability + rationale, distinguishability + rationale, falsification connection
[ ] Mechanism strength (preliminary)
[ ] Distinguishability summary declared
[ ] No confidence labels (SKEPTIC)
[ ] No chain aggregates (ARBITER)

--- Do not advance to SKEPTIC until gate is checked. ---

---

## SKEPTIC

[Challenge every hop. Assign confidence. Produce final mechanism strength.
Structurally separate from ANALYST.]

Hop-by-hop challenge:

  Hop 1 challenge:
    Breaks X -> [A] when: [Observable condition]
    H0 alternative: [How does H0 produce [A] without X? Does this change the distinguishability verdict?]
    Confidence: [ ] High  [ ] Medium  [ ] Low
    Confidence rationale: [1 sentence]

  Hop 2 challenge:
    Breaks [A] -> Y when: [Observable condition]
    H0 alternative: [How does H0 produce Y without [A]?]
    Confidence: [ ] High  [ ] Medium  [ ] Low
    Confidence rationale: [1 sentence]

  [Mirror all hops.]

Confounders: [At least one variable correlating with both X and Y.]

H0 challenge:
  Risk: [Does mechanism analysis change H0 severity verdict? Why?]
  Most dangerous I-NN: [ID + 1 sentence]
  Revised H0 severity: [ ] Confirms FRAMER-H0  [ ] Upgrades to ADVISORY  [ ] Upgrades to STOP

Final falsification table:

| ID   | Condition | Pool | Testability | Confidence | Rationale |
|------|-----------|------|-------------|------------|-----------|
| F-01 | [text] | F-NN | [H1.3 label] | [ ] High  [ ] Med  [ ] Low | [1 sentence] |
| F-02 | [text] | F-NN | [H1.3 label] | [ ] High  [ ] Med  [ ] Low | [1 sentence] |
| I-01 | [text] | I-NN | [H1.3 label] | [ ] High  [ ] Med  [ ] Low | [1 sentence] |
| I-02 | [text] | I-NN | [H1.3 label] | [ ] High  [ ] Med  [ ] Low | [1 sentence] |

Mechanism strength (final): [ ] Strong  [ ] Moderate  [ ] Weak
Final rationale: [1 sentence. Note if changed from preliminary.]

SKEPTIC GATE:
[ ] Every hop challenged with H0 alternative
[ ] Confidence assigned to all F-NN and I-NN
[ ] Final falsification table complete
[ ] H0 severity revised or confirmed
[ ] Final mechanism strength

--- Do not advance to ARBITER until gate is checked. ---

---

## ARBITER

[Post-processing role. Computes five diagnostics including the H0-distinguishability diagnostic
absent from all R7 variations. Produces consolidated 5-row AMEND routing table.]

### Diagnostic 1: Chain Observability Aggregate

  Observable: [Count]  |  Partial: [Count]  |  Opaque: [Count]  |  Total: [Count]
  Chain observability pattern: [ ] AllObservable  [ ] Mixed  [ ] PredominantlyOpaque
  AMEND trigger: [Required if Mixed or PredominantlyOpaque / Not required]

### Diagnostic 2: Testability Residual Yield

  testability_residual_unknown_count: [From FRAMER-H1]
  Residual Unknown IDs: [F-NN list] + [I-NN list]
  Pool asymmetry: [1 sentence]
  AMEND trigger: [Required if count > 0 / Not required]

### Diagnostic 3: H0 Distinguishability

  Distinguishability summary (from ANALYST): [AllDistinguishable / Mixed / Indeterminate]
  Indeterminate or Indistinguishable hops: [List, or "None"]
  Interpretation: [1 sentence: an Indeterminate hop means we cannot tell whether Y at that
    step is X-caused or H0-caused.]
  AMEND trigger: [Required if Mixed or Indeterminate / Not required]

### Diagnostic 4: H0 Severity (final)

  H0 severity (SKEPTIC final): [SAFE / ADVISORY / STOP]
  Inertia pathway observability: [Observable / Partial / Opaque]
  Chain vs inertia observability: [1 sentence]
  AMEND trigger: [Required if ADVISORY or STOP / Not required]

### Diagnostic 5: I-NN Pool Coverage

  I-NN count: [Total]
  Pool coverage: [ ] Comprehensive  [ ] Adequate  [ ] Minimal
  Most dangerous I-NN: [ID from SKEPTIC]
  AMEND trigger: [Required if Minimal / Not required]

### Consolidated AMEND Routing Table

| # | Diagnostic | Result | AMEND slot | Routing |
|---|-----------|--------|------------|---------|
| 1 | Chain observability | [pattern] | Observability | [Required / Not required] |
| 2 | Testability residual | [count] | Testability | [Required if > 0 / Not required] |
| 3 | H0 distinguishability | [AllDistinguishable/Mixed/Indeterminate] | Distinguishability | [Required if Mixed or Indeterminate / Not required] |
| 4 | H0 severity | [SAFE/ADVISORY/STOP] | Inertia | [Required if ADVISORY or STOP / Not required] |
| 5 | I-NN pool coverage | [Comprehensive/Adequate/Minimal] | Mechanism | [Required if Minimal / Not required] |

ARBITER note: [Most critical H1 vs H0 finding -- 1 sentence.]

---

## FRAMER (CLOSING)

Scoped claim: ["X causes Y above R0 when [condition], for [population]."]
H0 status: [ ] Rejected (mechanism distinguishable from H0 at all key hops)
           [ ] Partially rejected (mechanism distinguishable at some hops)
           [ ] Not rejected (mechanism indistinguishable from H0 -- do not proceed)
Out-of-scope: [Context where H1 mechanism fails or H0 dominates.]

AMEND DIRECTIVE:

AMEND: discover-causal
  Narrow: [Scope tightening -- include H0 rejection condition]
  Mechanism: [X -> [A] -> [B] -> Y]
  Falsification: [Highest-confidence F-NN condition. ID + testability + confidence.]
  [Distinguishability: if ARBITER row 3 = Required]
    "Hops [list] are H1/H0 indeterminate. Cannot distinguish X-caused Y from baseline Y
     at these steps. Add measurement that isolates X's contribution above R0."
  [Inertia: if ARBITER row 4 = Required]
    "H0 severity: [ADVISORY/STOP]. Y occurs at R0 = [rate] via [most dangerous I-NN].
     Demonstrate X produces Y incrementally above R0."
  [Observability: if ARBITER row 1 = Required]
    "Hops [list Opaque] require proxy measurements."
  [Testability: if ARBITER row 2 = Required]
    "Conditions [list IDs] have Unknown testability after evidence."

---

Write artifact: simulations/discover/causal/{topic}-causal-{date}.md
Frontmatter: skill, topic, date, cause (X), outcome (Y),
             inertia_framing (null-hypothesis-H0), h0_severity (SAFE/ADVISORY/STOP),
             baseline_rate_R0, inertia_observability,
             distinguishability_summary (AllDistinguishable/Mixed/Indeterminate),
             indeterminate_hop_count, h0_rejected (true/false/partial),
             f_nn_count, i_nn_count, i_nn_pool_coverage,
             hop_count, chain_observability_pattern,
             mechanism_strength_preliminary, mechanism_strength_final, strength_changed (true/false),
             testability_refined_count, testability_residual_unknown_count,
             f_nn_residual_count, i_nn_residual_count, pool_asymmetry_detected (true/false),
             evidence_count, evidence_quality,
             arbiter_rows_required (count), confounder_named (true/false).
```

---

## V-04: CHALLENGER-Primed Role Sequence with Interrogative Phrasing

**Axes:** Role sequence (CHALLENGER primes adversarial questions before mechanism construction)
+ Phrasing register (second-person interrogative throughout -- all instructions are questions).

The CHALLENGER role runs before ANALYST. It reads the claim, falsification pools, and inertia
analysis, then generates explicit challenge questions for ANALYST to address while building the
mechanism chain. ANALYST constructs the mechanism with CHALLENGER's questions visible. SKEPTIC
refines CHALLENGER's challenges post-construction. The EXAMINER role produces a routing table
with a CHALLENGER-survival row absent from all R7 variations.

**Hypothesis:** In R7, SKEPTIC always ran after ANALYST, challenging a completed chain. This
may allow analysts to commit to a mechanism before seeing adversarial challenges, then defend
their construction. CHALLENGER-primed ordering shows challenges first: ANALYST builds knowing
what the chain must survive. The interrogative phrasing tests whether question-framing makes
challenge acceptance more natural.

```
You are running /discover-causal.
Your input is a feature hypothesis of the form "X causes Y."
Answer each section's questions fully before advancing.
Every classification judgment uses a discrete label from a fixed set with a rationale line.

Role sequence:
  FRAMER: What is the claim? What would falsify it? What does the baseline look like?
  EVIDENCE: What do we know? What can we test?
  CHALLENGER: What adversarial questions must the mechanism survive? (runs BEFORE mechanism)
  ANALYST: What is the mechanism chain? (constructed with CHALLENGER questions visible)
  SKEPTIC: Did the mechanism survive the CHALLENGER questions?
  EXAMINER: What does all of this mean for the AMEND directive?
  FRAMER (closing): What is the scoped claim and AMEND block?

Two-pool falsification: F-NN (claim-derived) and I-NN (inertia-derived).
Testability: Unknown at genesis, refined in EVIDENCE, confidence assigned in SKEPTIC.
EXAMINER produces consolidated AMEND routing table with 4 rows.

---

## FRAMER

What is the claim?
  X (the cause): [What is being built or changed?]
  Y (the claimed outcome): [What outcome is X claimed to produce?]
  Claim: ["X causes Y" -- one sentence]

What conditions would prove the claim wrong? (F-NN pool -- at least two)

| ID   | If you observed this, X does not cause Y | Testability | Confidence | Rationale |
|------|------------------------------------------|-------------|------------|-----------|
| F-01 | [What observation would falsify the mechanism?] | Unknown | Pending | [1 sentence] |
| F-02 | [A second, distinct falsifying observation] | Unknown | Pending | [1 sentence] |

What happens today without X?
  Without X: [One sentence describing status quo]
  Baseline rate: [How often does Y occur without X? Estimate, bound, or "Unknown -- [reasoning]"]
  Inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP
  Inertia severity rationale: [1 sentence]
  Can we directly observe whether Y occurs without X?
    Inertia pathway observability: [ ] Observable  [ ] Partial  [ ] Opaque
    Observability rationale: [1 sentence]

What alternative pathways produce Y without X? (I-NN pool -- at least two)

| ID   | Pathway by which Y occurs without X | Testability | Confidence | Rationale |
|------|-------------------------------------|-------------|------------|-----------|
| I-01 | Y occurs without X via [mechanism 1] | Unknown | Pending | [1 sentence] |
| I-02 | Y via [mechanism 2] without X | Unknown | Pending | [1 sentence] |

FRAMER GATE:
[ ] X and Y extracted separately
[ ] At least two F-NN conditions (Unknown testability, Pending confidence)
[ ] Baseline rate declared
[ ] Inertia severity and observability labeled
[ ] At least two I-NN conditions (Unknown testability, Pending confidence)

--- Do not advance to EVIDENCE until all questions above are fully answered. ---

---

## EVIDENCE

What context-specific evidence connects X to Y?
  [At least one entry, or write "No evidence found" -- do not leave blank]

  Entry 1:
    Where did you see this? [Prior result / Analogous case / Domain observation / Counter-evidence]
    What was observed? [Observation text]
    Does this support or complicate X->Y? [Supports / Complicates / Challenges -- 1 sentence]

  [Add entries as needed.]

  Evidence quality: [ ] Strong  [ ] Moderate  [ ] Weak  [ ] None
  Evidence quality rationale: [1 sentence]

Can these falsification conditions be tested with available resources?

| ID   | Can you run this test? | Rationale |
|------|------------------------|-----------|
| F-01 | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence] |
| F-02 | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence] |
| I-01 | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence] |
| I-02 | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence] |
[Mirror all F-NN and I-NN conditions.]

How much did evidence resolve testability?
  testability_refined_count: [Conditions moved from Unknown to Easy or Hard]
  testability_residual_unknown_count: [Still Unknown after evidence]
  Residual Unknown IDs: [List, or "None"]
  F-NN residual: [Count]  |  I-NN residual: [Count]

EVIDENCE GATE:
[ ] At least one evidence entry (or explicit "No evidence found")
[ ] Evidence quality labeled
[ ] Testability refinement complete for all F-NN and I-NN
[ ] Yield counts declared

--- Do not advance to CHALLENGER until all questions above are fully answered. ---

---

## CHALLENGER

[Before the mechanism chain is built, what adversarial questions must it survive?
CHALLENGER reads the claim, F-NN pool, I-NN pool, and inertia analysis. Produces 3-5 challenge
questions. ANALYST must address each one while constructing the chain.]

What would need to break for each step in the mechanism to fail?
  Challenge Q-1: [What observable condition would disprove the first causal step from X?]
  Challenge Q-2: [What observable condition would disprove the connection to Y?]
  [Add Q-3, Q-4 for expected additional hops.]

What is the strongest I-NN pathway that could produce Y without X?
  Challenge Q-I: [Which I-NN condition, if true, most directly negates the mechanism?]

How would we know X caused Y rather than the I-NN pathway?
  Challenge Q-D: [What measurement or observation would distinguish X-caused Y from I-NN-caused Y?]

CHALLENGER summary: [1 sentence: what is the single hardest question this mechanism must answer?]

[ANALYST will read all Challenge Q items above before constructing the chain.]

---

## ANALYST

[Build the mechanism chain with CHALLENGER's questions visible. Two hops minimum.
For each hop, address the relevant Challenge Q explicitly.]

Hop 1: X [name] -> [intermediate A]: [How does X produce A?]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Observability rationale: [1 sentence]
  Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
  Falsification connection: [F-NN or I-NN ID. 1 sentence.]
  Response to Challenge Q-1: [How does this hop survive CHALLENGER's first question?]

Hop 2: [intermediate A] -> Y: [How does A produce Y?]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Observability rationale: [1 sentence]
  Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
  Falsification connection: [F-NN or I-NN ID. 1 sentence.]
  Response to Challenge Q-2: [How does this hop survive Q-2?]

[Add Hop 3+ as needed. Each hop addresses its relevant Challenge Q.]

Inertia distinguishability:
  Response to Challenge Q-D: [How does the mechanism produce distinguishable Y above I-NN baseline?]

Mechanism strength (preliminary): [ ] Strong  [ ] Moderate  [ ] Weak
Preliminary rationale: [1 sentence]

ANALYST GATE:
[ ] At least two hops
[ ] Every hop: observability + rationale, evidence coherence, falsification connection
[ ] Every hop: response to its relevant CHALLENGER question
[ ] Inertia distinguishability addressed (Q-D)
[ ] Mechanism strength (preliminary)

--- Do not advance to SKEPTIC until gate is checked. ---

---

## SKEPTIC

[Did the mechanism survive? This section is structurally separate from ANALYST.
Review ANALYST's responses to CHALLENGER questions. For each hop: did the response survive?]

Did each Challenge Q survive?

  Challenge Q-1 verdict: [ ] Survived  [ ] Partially survived  [ ] Did not survive
  Q-1 rationale: [1 sentence]

  Challenge Q-2 verdict: [ ] Survived  [ ] Partially survived  [ ] Did not survive
  Q-2 rationale: [1 sentence]

  [Mirror all Challenge Qs.]

  Challenge Q-I verdict: [Which I-NN condition remains most dangerous after ANALYST response?]
  I-NN threat update: [ ] Reduced  [ ] Unchanged  [ ] Elevated
  Revised inertia severity: [ ] Confirms FRAMER  [ ] Upgrades to ADVISORY  [ ] Upgrades to STOP

Confounders: [At least one variable correlating with both X and Y.]

Confidence assignments (all F-NN and I-NN):

| ID   | Condition | Testability (EVIDENCE) | Confidence (SKEPTIC) | Rationale |
|------|-----------|------------------------|----------------------|-----------|
| F-01 | [text] | [EVIDENCE label] | [ ] High  [ ] Med  [ ] Low | [1 sentence] |
| F-02 | [text] | [EVIDENCE label] | [ ] High  [ ] Med  [ ] Low | [1 sentence] |
| I-01 | [text] | [EVIDENCE label] | [ ] High  [ ] Med  [ ] Low | [1 sentence] |
| I-02 | [text] | [EVIDENCE label] | [ ] High  [ ] Med  [ ] Low | [1 sentence] |

Mechanism strength (final): [ ] Strong  [ ] Moderate  [ ] Weak
Final rationale: [1 sentence. Note if changed from ANALYST preliminary.]

SKEPTIC GATE:
[ ] Every CHALLENGER question has a verdict
[ ] I-NN threat updated and severity revised
[ ] Confidence assigned to all F-NN and I-NN
[ ] Final mechanism strength with rationale

--- Do not advance to EXAMINER until gate is checked. ---

---

## EXAMINER

[What does all of this mean for AMEND? Post-processing role that aggregates diagnostics
and produces a consolidated 4-row AMEND routing table.]

What is the chain observability picture?
  Observable: [Count]  |  Partial: [Count]  |  Opaque: [Count]  |  Total: [Count]
  Chain pattern: [ ] AllObservable  [ ] Mixed  [ ] PredominantlyOpaque
  AMEND Observability: [Required if Mixed or PredominantlyOpaque / Not required]

What testability gaps remain?
  testability_residual_unknown_count: [From EVIDENCE]
  Residual Unknown IDs: [List, or "None"]
  Pool asymmetry: [1 sentence: are I-NN conditions disproportionately Unknown?]
  AMEND Testability: [Required if count > 0 / Not required]

What is the inertia verdict?
  Inertia severity (final): [SAFE / ADVISORY / STOP]
  Inertia pathway observability: [Observable / Partial / Opaque]
  Chain vs inertia observability: [1 sentence comparison]
  AMEND Inertia: [Required if ADVISORY or STOP / Not required]

What is the CHALLENGER challenge survival record?
  Challenges survived: [Count]  |  Partially survived: [Count]  |  Failed: [Count]
  Most critical failed or partial challenge: [Q-ID + 1 sentence, or "None failed"]
  AMEND Challenge: [Required if any challenge failed or partially survived / Not required]

AMEND Routing Table:

| # | Diagnostic | Result | AMEND slot | Routing |
|---|-----------|--------|------------|---------|
| 1 | Chain observability | [pattern] | Observability | [Required / Not required] |
| 2 | Testability residual | [count] | Testability | [Required if > 0 / Not required] |
| 3 | Inertia severity | [SAFE/ADVISORY/STOP] | Inertia | [Required if ADVISORY or STOP / Not required] |
| 4 | CHALLENGER survival | [All survived / Partial / Failed] | Challenge | [Required if Partial or Failed / Not required] |

EXAMINER note: [Most critical gap across all diagnostics -- 1 sentence.]

---

## FRAMER (CLOSING)

What is the scoped claim?
  Scoped claim: ["X causes Y when [condition], for [population]."]
  Out-of-scope: [Context from SKEPTIC where challenge failed or mechanism breaks down.]

AMEND DIRECTIVE:

AMEND: discover-causal
  Narrow: [Scope tightening]
  Mechanism: [X -> [A] -> [B] -> Y with actual intermediate names]
  Falsification: [Highest-confidence condition. ID + testability + confidence.]
  [Observability: if EXAMINER row 1 = Required]
    "Chain is [Mixed/PredominantlyOpaque]. Hops [list] need proxy measurements."
  [Testability: if EXAMINER row 2 = Required]
    "Conditions [list IDs] have Unknown testability after evidence."
  [Inertia: if EXAMINER row 3 = Required]
    "Y occurs at [baseline] via [most dangerous I-NN]. Demonstrate incremental Y."
  [Challenge: if EXAMINER row 4 = Required]
    "CHALLENGER questions [Q-IDs] were not fully survived. Address [specific failure]
     before treating the mechanism as established."

---

Write artifact: simulations/discover/causal/{topic}-causal-{date}.md
Frontmatter: skill, topic, date, cause (X), outcome (Y),
             combination_axes (challenger-primed, interrogative-phrasing),
             role_sequence (FRAMER-EVIDENCE-CHALLENGER-ANALYST-SKEPTIC-EXAMINER-FRAMER),
             challenger_questions_count, challenges_survived, challenges_failed,
             inertia_verdict, baseline_rate, inertia_observability,
             f_nn_count, i_nn_count, i_nn_pool_coverage,
             hop_count, chain_observability_pattern,
             mechanism_strength_preliminary, mechanism_strength_final, strength_changed (true/false),
             testability_refined_count, testability_residual_unknown_count,
             f_nn_residual_count, i_nn_residual_count, pool_asymmetry_detected (true/false),
             evidence_count, evidence_quality,
             examiner_rows_required (count), confounder_named (true/false).
```

---

## V-05: Scope-Inversion I-NN Derivation with AUDITOR and Triple-Gap Diagnostic

**Axes:** Output format (section-letter structure) + role sequence (AUDITOR post-processor) +
novel I-NN derivation (scope-inversion) + inertia framing (scope-edge analysis).
Combination variation targeting A-17.

**Scope-inversion derivation:** Each mechanism hop declares a validity-scope field: the
condition under which the hop holds. The scope-paired I-NN condition is generated by
scope-inversion: Y occurs via a non-X pathway when that scope condition is absent. This creates
structurally paired F-NN/I-NN conditions -- each I-NN targets the scope boundary of its hop.

**Triple-gap definition under scope-inversion:** A triple gap occurs when:
  1. The mechanism hop is Opaque (forward causal step unobservable)
  2. The falsification condition connected to that hop has Unknown testability after evidence
  3. A scope-paired I-NN condition exists for that hop (guaranteed by the derivation)
The scope-inversion makes I-NN-F-NN overlap structurally exact: the I-NN was derived from the
same scope boundary as the hop's falsification condition, so overlap requires no inference.
Triple-gap count = number of F-NN conditions connected to Opaque hops with Unknown testability.

**Hypothesis:** Chain-seeded I-NN derivation (R7-V-05) anchors I-NN to inertia chain hops.
Scope-inversion anchors I-NN to mechanism hop scope boundaries. Scope-inversion I-NN conditions
are maximally relevant to the forward mechanism: each inertia condition attacks exactly the scope
edge that makes the corresponding mechanism hop valid. Triple-gap detection is structural rather
than inferred, producing sharper co-occurrence identification than R7-V-05.

```
You are running /discover-causal.
Your input is a feature hypothesis of the form "X causes Y."
Six sections (A through F) plus AUDITOR. Complete each fully before advancing.
Every classification judgment uses a discrete label from a fixed set with a rationale line.

Three-pool analysis:
  F-NN pool: claim-derived falsification conditions (Section A).
  I-NN pool: scope-inversion-derived inertia conditions (Section C, one per mechanism hop).
  Mechanism hops: forward causal chain from X to Y (Section C).

Scope-inversion derivation (Section C):
  Each mechanism hop carries a validity-scope field: the condition under which the hop holds.
  The scope-paired I-NN condition is the inertia pathway active when that scope condition
  is absent -- the status quo exploits the scope edge.

Testability lifecycle:
  F-NN: Unknown at genesis (A), refined in B.
  I-NN: Unknown at genesis (C), refined in D.
  All conditions receive confidence labels in Section E.

AUDITOR: runs after Section E. Produces 5-row AMEND routing table with triple-gap row (A-17).

---

## SECTION A: CLAIM AND F-NN POOL

A1. Claim extraction:
  X (the cause): [Extract from input]
  Y (the claimed outcome): [Extract from input]
  Full claim: ["X causes Y" -- one sentence]

A2. F-NN pool (claim-derived falsification conditions):
[At least two. Testability = Unknown. Confidence = Pending until Section E.]

| ID   | Condition (claim false if observed) | Testability | Confidence | Rationale |
|------|-------------------------------------|-------------|------------|-----------|
| F-01 | [What would show X does not cause Y?] | Unknown (see B) | Pending | [1 sentence] |
| F-02 | [Second distinct condition] | Unknown (see B) | Pending | [1 sentence] |
[Add F-NN as needed.]

SECTION A GATE:
[ ] X and Y extracted separately
[ ] At least two F-NN rows (Unknown testability, Pending confidence)

--- Do not advance to Section B until checked. ---

---

## SECTION B: EVIDENCE AND F-NN TESTABILITY REFINEMENT

B1. Evidence:
[At least one context-specific observation, or explicit "None found."]

  Evidence entry 1:
    Source type: [ ] Prior result  [ ] Analogous case  [ ] Domain observation  [ ] Counter-evidence
    Observation: [What was seen, where, when?]
    Bearing on X->Y: [Supports / Complicates / Challenges -- 1 sentence]

  [Add entries as needed.]

  Evidence quality: [ ] Strong  [ ] Moderate  [ ] Weak  [ ] None
  Evidence quality rationale: [1 sentence]

B2. F-NN testability refinement:

| ID   | Testability after evidence | Refinement rationale |
|------|---------------------------|----------------------|
| F-01 | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence] |
| F-02 | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence] |
[Mirror all F-NN conditions.]

F-NN yield:
  f_nn_refined_count: [Moved from Unknown to Easy or Hard]
  f_nn_residual_unknown_count: [Still Unknown]
  F-NN residual IDs: [List, or "None"]

SECTION B GATE:
[ ] Evidence populated (or explicit "None found")
[ ] Evidence quality labeled
[ ] F-NN testability refinement complete with yield counts

--- Do not advance to Section C until checked. ---

---

## SECTION C: MECHANISM CHAIN WITH SCOPE-INVERSION I-NN DERIVATION

[Map the forward causal chain. Two hops minimum. For each hop:
  1. State the mechanism
  2. Label observability (Observable/Partial/Opaque) with rationale
  3. State the validity scope: the condition under which this hop holds
  4. Derive the scope-paired I-NN condition by inverting the validity scope
  5. Connect to a pre-existing F-NN condition from Section A

The scope-paired I-NN condition answers: "When the validity-scope condition is absent,
what inertia pathway could still produce Y via a different route?"
I-NN conditions carry testability = Unknown at genesis here in Section C.]

Mechanism chain:

  Hop 1: X [name] -> [intermediate A]: [How does X produce A?]
    Observability: [ ] Observable  [ ] Partial  [ ] Opaque
    Observability rationale: [1 sentence: how directly can this intermediate be detected?]
    Validity scope: ["This hop holds when [condition]. Without [condition], X does not produce A."]
    Scope-inversion I-NN:
      Inverted condition: ["When NOT [condition], an alternative pathway can produce A or Y."]
      I-NN condition:
        | I-01 | Y occurs without X via [inertia pathway exploiting absence of [condition]] | Unknown (see D) | Pending | [1 sentence: why does scope absence enable this pathway?] |
    Evidence coherence: [E-NN IDs from Section B. Or: "No evidence."]
    Coherence verdict: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
    Falsification connection: [F-NN ID. 1 sentence: if this hop fails, which F-NN condition holds?]

  Hop 2: [intermediate A] -> Y: [How does A produce Y?]
    Observability: [ ] Observable  [ ] Partial  [ ] Opaque
    Observability rationale: [1 sentence]
    Validity scope: ["This hop holds when [condition 2]."]
    Scope-inversion I-NN:
      Inverted condition: ["When NOT [condition 2], ..."]
      I-NN condition:
        | I-02 | Y occurs without X via [inertia pathway at scope edge of condition 2] | Unknown (see D) | Pending | [1 sentence] |
    Evidence coherence: [E-NN IDs. Or: "No evidence."]
    Coherence verdict: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
    Falsification connection: [F-NN ID. 1 sentence.]

  [Add Hop 3+ as needed. Each hop generates one scope-paired I-NN condition.]

Mechanism strength (preliminary): [ ] Strong  [ ] Moderate  [ ] Weak
Preliminary rationale: [1 sentence]

I-NN pool (consolidated from hop derivations):

| ID   | Scope-paired I-NN condition | Paired hop | Validity scope inverted | Testability | Confidence |
|------|-----------------------------|------------|------------------------|-------------|------------|
| I-01 | [text] | Hop 1 | [condition inverted] | Unknown (see D) | Pending |
| I-02 | [text] | Hop 2 | [condition inverted] | Unknown (see D) | Pending |
[One row per hop.]

SECTION C GATE:
[ ] At least two hops
[ ] Every hop: observability + rationale, validity scope, scope-inversion I-NN derivation
[ ] Every hop: evidence coherence with IDs, falsification connection to F-NN
[ ] Mechanism strength (preliminary)
[ ] I-NN consolidated table complete (one I-NN per hop)
[ ] No confidence labels in this section
[ ] No chain aggregates in this section (AUDITOR)

--- Do not advance to Section D until checked. ---

---

## SECTION D: INERTIA ANALYSIS AND I-NN TESTABILITY REFINEMENT

[Analyze the overall inertia picture. The inertia pathway observability is assessed
as an aggregate of per-I-NN scope-edge observability labels.]

D1. Inertia baseline:
  Status-quo description: [One sentence: what happens today without X?]
  Baseline rate: [Estimate or bound, or "Unknown -- [reasoning]."]
  Inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP
  Inertia severity rationale: [1 sentence]

D2. Inertia pathway observability (aggregate of I-NN scope-edge observability):

| ID   | Inertia pathway observability at this scope edge | Rationale |
|------|--------------------------------------------------|-----------|
| I-01 | [ ] Observable  [ ] Partial  [ ] Opaque | [1 sentence: can we detect whether this inertia pathway produces Y?] |
| I-02 | [ ] Observable  [ ] Partial  [ ] Opaque | [1 sentence] |
[Mirror all I-NN conditions.]

  I-NN Observable: [Count]  |  Partial: [Count]  |  Opaque: [Count]
  Inertia pathway observability (aggregate): [ ] Observable  [ ] Partial  [ ] Opaque
    (Observable = majority of I-NN scope edges are Observable;
     Partial = mixed;
     Opaque = majority are Opaque or no direct measurement path)
  Inertia observability rationale: [1 sentence]

D3. I-NN testability refinement (using Section B evidence):

| ID   | Testability after evidence | Refinement rationale |
|------|---------------------------|----------------------|
| I-01 | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence] |
| I-02 | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence] |

I-NN yield:
  i_nn_refined_count: [Moved from Unknown]
  i_nn_residual_unknown_count: [Still Unknown]
  I-NN residual IDs: [List, or "None"]

Combined yield (F-NN + I-NN):
  testability_refined_count: [Total]
  testability_residual_unknown_count: [Total]
  All residual Unknown IDs: [List by pool]

SECTION D GATE:
[ ] Baseline rate declared
[ ] Inertia severity labeled
[ ] Per-I-NN observability labels filled
[ ] Inertia pathway observability aggregate declared
[ ] I-NN testability refinement complete with yield
[ ] Combined yield declared

--- Do not advance to Section E until checked. ---

---

## SECTION E: ADVERSARIAL CHALLENGE

[Structurally separate from mechanism chain. Challenge every hop. Assign confidence to all
F-NN and I-NN. For each hop, include a scope-inversion plausibility check: does the scope-paired
I-NN condition remain plausible after mechanism analysis?]

Hop-by-hop challenge:

  Hop 1 challenge:
    Breaks X -> [A] when: [Observable condition]
    Observable test: [What to measure]
    Alternative at Hop 1: [What else produces [A] without X?]
    Scope-inversion plausibility: Does I-01 remain plausible after mechanism analysis?
      [ ] Plausible  [ ] Reduced  [ ] Implausible
      Rationale: [1 sentence]
    Confidence on Hop 1 mechanism: [ ] High  [ ] Medium  [ ] Low
    Confidence rationale: [1 sentence]

  Hop 2 challenge:
    Breaks [A] -> Y when: [Observable condition]
    Observable test: [What to measure]
    Alternative at Hop 2: [What else produces Y without [A]?]
    Scope-inversion plausibility: Does I-02 remain plausible?
      [ ] Plausible  [ ] Reduced  [ ] Implausible
      Rationale: [1 sentence]
    Confidence on Hop 2 mechanism: [ ] High  [ ] Medium  [ ] Low
    Confidence rationale: [1 sentence]

  [Mirror all Section C hops. Each challenge includes scope-inversion plausibility check.]

Confounders: [At least one variable correlating with both X and Y.]

Inertia challenge:
  Most dangerous I-NN: [ID + 1 sentence: which scope-paired inertia pathway is the greatest threat?]
  Revised inertia severity: [ ] Confirms Section D  [ ] Upgrades to ADVISORY  [ ] Upgrades to STOP

Final falsification table (all F-NN and I-NN with confidence):

| ID   | Condition | Pool | Paired hop | Testability | Confidence | Rationale |
|------|-----------|------|------------|-------------|------------|-----------|
| F-01 | [text] | F-NN | [Hop N via falsification connection] | [Sec B label] | [ ] High  [ ] Med  [ ] Low | [1 sentence] |
| F-02 | [text] | F-NN | [Hop N] | [Sec B label] | [ ] High  [ ] Med  [ ] Low | [1 sentence] |
| I-01 | [text] | I-NN | Hop 1 | [Sec D label] | [ ] High  [ ] Med  [ ] Low | [1 sentence] |
| I-02 | [text] | I-NN | Hop 2 | [Sec D label] | [ ] High  [ ] Med  [ ] Low | [1 sentence] |

Mechanism strength (final): [ ] Strong  [ ] Moderate  [ ] Weak
Final rationale: [1 sentence. Note if changed from Section C preliminary.]

SECTION E GATE:
[ ] Every hop challenged with observable test, alternative, and scope-inversion plausibility check
[ ] Confidence assigned to all F-NN and I-NN conditions
[ ] Final falsification table complete with Paired hop column
[ ] Final mechanism strength with rationale
[ ] At least one confounder named
[ ] Inertia challenge with specific I-NN ID

--- Do not advance to AUDITOR until checked. ---

---

## AUDITOR

[Post-processing role. Reads all sections. Computes five diagnostics including the triple-gap
joint diagnostic (A-17). Produces consolidated 5-row AMEND routing table.]

### Diagnostic 1: Mechanism Chain Observability Aggregate

| Hop   | Mechanism step | Observability (Section C) |
|-------|---------------|---------------------------|
| Hop 1 | X -> [A] | [Observable / Partial / Opaque] |
| Hop 2 | [A] -> Y | [Observable / Partial / Opaque] |
[Mirror all hops.]

  Observable: [Count]  |  Partial: [Count]  |  Opaque: [Count]  |  Total: [Count]
  Chain observability pattern: [ ] AllObservable  [ ] Mixed  [ ] PredominantlyOpaque
  Opaque hop IDs: [List, or "None"]
  AMEND trigger: [Required if Mixed or PredominantlyOpaque / Not required]

### Diagnostic 2: Testability Residual Yield

  testability_residual_unknown_count (combined): [From Section D]
  Residual Unknown IDs: [F-NN list] + [I-NN list]
  F-NN residual: [Count]  |  I-NN residual: [Count]
  Pool asymmetry: [1 sentence]
  AMEND trigger: [Required if count > 0 / Not required]

### Diagnostic 3: Evidence Quality

  Evidence quality (Section B): [Strong / Moderate / Weak / None]
  AMEND trigger: [Required if None / Not required]

### Diagnostic 4: Inertia Severity and Pathway Observability

  Inertia severity (Section E final): [SAFE / ADVISORY / STOP]
  Inertia pathway observability aggregate (Section D): [Observable / Partial / Opaque]
  Chain vs inertia observability: [1 sentence: does forward mechanism observability diverge
    from scope-edge inertia pathway observability?]
  AMEND trigger: [Required if ADVISORY or STOP / Not required]

### Diagnostic 5: Triple-Gap Analysis (A-17)

[A triple gap is a condition satisfying all three simultaneously:
  1. The F-NN condition is falsification-connected to an Opaque mechanism hop (Section C)
  2. The F-NN condition has Unknown testability after evidence (Section B)
  3. A scope-paired I-NN condition exists for that hop (guaranteed by scope-inversion in Section C)

Under scope-inversion, condition 3 is structural: every mechanism hop generated an I-NN
condition from its validity scope. The triple-gap test reduces to conditions 1 and 2 for
F-NN conditions connected to Opaque hops, because scope-pairing is inherent to the derivation.]

Triple-gap evaluation per F-NN condition:

| F-NN | Connected hop (from Sec C) | Hop observability | F-NN testability (Sec B) | Scope-paired I-NN | Triple-gap? |
|------|---------------------------|-------------------|--------------------------|-------------------|-------------|
| F-01 | [Hop N] | [from Sec C] | [from Sec B] | [I-NN ID paired to Hop N] | [ ] Yes  [ ] No |
| F-02 | [Hop N] | [from Sec C] | [from Sec B] | [I-NN ID] | [ ] Yes  [ ] No |
[A row is Yes when: Hop observability = Opaque AND Testability = Unknown AND scope-paired I-NN exists.]

Triple-gap count: [Count of F-NN rows marked Yes]
Triple-gap IDs: [F-NN IDs and their scope-paired I-NN IDs. Or: "None detected."]
Triple-gap severity: [ ] None  [ ] Advisory (1 gap)  [ ] Significant (2+ gaps)
Triple-gap implication: [1 sentence: at these conditions, the forward mechanism is unobservable,
  the falsification condition is untestable, and an inertia pathway operates at the same scope
  boundary. Maximum causal uncertainty. What is the recommended action?]
AMEND trigger: [Required if triple-gap count > 0 / Not required]

### Consolidated AMEND Routing Table (A-16 + A-17)

| # | Diagnostic | Result | AMEND slot | Routing |
|---|-----------|--------|------------|---------|
| 1 | Chain observability | [AllObservable/Mixed/PredominantlyOpaque] | Observability | [Required / Not required] |
| 2 | Testability residual | [Count] | Testability | [Required if > 0 / Not required] |
| 3 | Evidence quality | [Strong/Moderate/Weak/None] | Evidence | [Required if None / Not required] |
| 4 | Inertia severity | [SAFE/ADVISORY/STOP] | Inertia | [Required if ADVISORY or STOP / Not required] |
| 5 | Triple-gap count | [Count] | Triple-gap | [Required if count > 0 -- "Conditions [F-NN IDs] are triple gaps (Opaque hop + Unknown testability + scope-paired I-NN at [scope boundary]). Maximum causal uncertainty. Resolve before treating claim as reliable."] |

AUDITOR note: [Most critical finding across all five diagnostics -- 1 sentence.]

AUDITOR GATE:
[ ] Five diagnostics complete
[ ] Triple-gap evaluation table filled for all F-NN conditions
[ ] Triple-gap count and severity declared
[ ] AMEND routing table: all 5 rows filled
[ ] At least one row marked Required (if none, flag as anomaly)

--- Do not advance to Section F until AUDITOR gate is checked. ---

---

## SECTION F: FRAMER (CLOSING)

Scoped claim: ["X causes Y when [validity-scope conditions from Section C hops], for [population]."]
Scope note: The scoped claim explicitly acknowledges the scope boundaries that generated the I-NN pool.
Out-of-scope: [At least one context where the validity-scope condition is absent,
  meaning a scope-paired I-NN pathway could produce Y -- from Section E plausibility checks.]

Final inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP
Inertia pathway observability: [Observable / Partial / Opaque -- Section D aggregate]

AMEND DIRECTIVE:

AMEND: discover-causal
  Narrow: [Scope tightening -- cite validity-scope conditions from Section C hops]
  Mechanism: [X -> [A] -> [B] -> Y with intermediate names and validity scopes noted]
  Falsification: [Highest-confidence condition from Section E table. ID + testability + confidence.
    If this condition is a triple gap, note it explicitly.]
  [Observability: if AUDITOR row 1 = Required]
    "Chain observability: [pattern]. Hops [list Opaque/Partial] require proxy measurements
     or claim narrowing to the observable portion of the mechanism."
  [Testability: if AUDITOR row 2 = Required]
    "Conditions [list IDs with pool label] have Unknown testability after evidence.
     Determine instrumentation before treating these as actionable falsification targets."
  [Evidence: if AUDITOR row 3 = Required]
    "Mechanism is theoretical. Cite one context-specific observation before next decision gate."
  [Inertia: if AUDITOR row 4 = Required]
    "Y occurs at [baseline rate] via [most dangerous I-NN from Section E]. The I-NN pathway
     operates at the scope boundary of [Hop N validity scope]. Demonstrate incremental Y
     above this baseline within the declared scope condition."
  [Triple-gap: if AUDITOR row 5 = Required]
    "Conditions [F-NN IDs] are triple gaps (Opaque hop + Unknown testability + scope-paired I-NN
     at [scope boundary]). Do not treat these as supporting evidence for the claim until:
     (a) hop observability is improved or a proxy measurement is established,
     (b) testability is determined, and
     (c) the scope-paired I-NN pathway is ruled out or bounded within the declared scope."

---

Write artifact: simulations/discover/causal/{topic}-causal-{date}.md
Frontmatter: skill, topic, date, cause (X), outcome (Y),
             combination_axes (scope-inversion-i-nn, auditor-role, section-letter),
             i_nn_derivation (scope-inversion), auditor_role (true), gate_checklists (6),
             inertia_verdict (SAFE/ADVISORY/STOP), baseline_rate,
             inertia_observability (Observable/Partial/Opaque),
             inertia_observability_method (aggregate-of-i-nn-scope-edges),
             evidence_count, evidence_quality (Strong/Moderate/Weak/None),
             f_nn_count, i_nn_count, i_nn_pool_coverage (Comprehensive/Adequate/Minimal),
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

## Cross-Variation Analysis

**A-14 (I-NN pool) across five variations:**
All five produce a structured I-NN pool with per-row labels matching F-NN structure. Derivation differs:
- V-01 (RESOLVER): table-seeded in FRAMER Step 3 from inertia analysis
- V-02 (evidence-table): table-seeded in Section 2, same 5-column format as F-NN throughout
- V-03 (H0): table-seeded as H0 pathways in FRAMER-H0, framed as null pathways
- V-04 (CHALLENGER): table-seeded in FRAMER; CHALLENGER primes adversarial questions from pool
- V-05 (scope-inversion): hop-seeded via scope-inversion, one I-NN per mechanism hop

**A-15 (inertia pathway observability) across five variations:**
All five produce a discrete Observable/Partial/Opaque label. Source differs:
- V-01: explicit dedicated field in FRAMER Step 3
- V-02: pool-level header block in Section 2 (before I-NN rows)
- V-03: explicit field in FRAMER-H0 (H0 observability question)
- V-04: explicit field in FRAMER inertia analysis block
- V-05: aggregate of per-I-NN scope-edge observability labels (Section D)

**A-16 (post-processing routing table) across five variations:**
All five use a named post-processing role with a consolidated routing table. Names differ:
- V-01: RESOLVER (5-row, adds Traceable-source column)
- V-02: AUDITOR (5-row, adds evidence-coverage row)
- V-03: ARBITER (5-row, adds H0-distinguishability row)
- V-04: EXAMINER (4-row, adds CHALLENGER-survival row)
- V-05: AUDITOR (5-row, adds triple-gap row)

**A-17 (triple-gap) across five variations:**
- V-01 through V-04: routing tables carry only single-dimension rows. No triple-gap row. Fail A-17.
- V-05: AUDITOR row 5 is the triple-gap diagnostic. I-NN-F-NN pairing is structural (scope-inversion).
  Triple-gap count = F-NN conditions connected to Opaque hops with Unknown testability.
  Scope-paired I-NN existence is guaranteed, making overlap structurally exact rather than inferred.

**Novel routing rows not in any R7 variation:**
- V-03 ARBITER row 3: H0-distinguishability (AllDistinguishable/Mixed/Indeterminate)
  Tests whether the mechanism is distinguishable from the null at each hop.
- V-04 EXAMINER row 4: CHALLENGER-survival (All-survived/Partial/Failed)
  Tests whether adversarial questions from the priming role were survived by the mechanism.
- V-02 AUDITOR row 3: Evidence-coverage (High/Partial/None at hop level)
  Tests hop-level evidence coverage rather than claim-level evidence quality.
- V-01 RESOLVER: Traceable-source column in every routing row
  Makes each AMEND trigger traceable to specific hops or condition IDs.

**R8 seeded questions for R9:**
- Does hop-gap accumulation (V-01) produce more hop-traceable AMEND rationales? Compare
  V-01 RESOLVER routing table traceable-source citations vs V-02 AUDITOR row citations.
- Does the 5-column evidence table (V-02) shift evidence-search from claim-level to hop-level?
  Compare V-02 evidence-coverage label (hop-level) to V-01 evidence quality (claim-level).
- Does H0 framing (V-03) increase STOP verdicts vs prose-based inertia checks?
  Run same hypothesis through V-03 and V-01, compare h0_severity vs inertia_verdict.
- Does CHALLENGER-primed ordering (V-04) produce more conservative mechanism chains?
  Compare V-04 ANALYST hop observability distribution to V-01 ANALYST distribution.
- Does scope-inversion I-NN (V-05) produce more structurally exact triple-gap matches
  than chain-seeded derivation (R7-V-05)?
  Compare triple-gap IDs and scope/chain anchors across both on the same hypothesis.
