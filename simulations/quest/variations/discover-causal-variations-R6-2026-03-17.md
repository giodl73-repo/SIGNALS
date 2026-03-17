Here's the R6 design summary:

---

## Round 6 — 5 Variations

**R6 target:** all 5 score 100.0 under v6 (13/13 aspirational). Both A-12 and A-13 are now required in every variation.

| V | Axis | New mechanism |
|---|------|---------------|
| **V-01** | Output format — inline chain observability tally | Aggregate label computed as a running tally at the end of the mechanism section (no summary table); V-05-style testability refinement provides A-13 |
| **V-02** | Role sequence — AUDITOR role | Fourth role (AUDITOR) runs after SKEPTIC and owns both aggregate diagnostics; routes AMEND conditionally from a routing table |
| **V-03** | Inertia framing — I-NN in both aggregates | Inertia conditions start Unknown (A-13) and their observability contributes to the chain aggregate (A-12); pool asymmetry tracked |
| **V-04** | Output format — AMEND routing matrix | A-12 and A-13 are rows in a formal 4-row decision table; AMEND slots generated mechanically, not from prose conditions |
| **V-05** | Lifecycle — dual-diagnostic yield section | Section D between mechanism and adversarial computes A-12 and A-13 in parallel; joint gap analysis flags "double-blind gaps" (Opaque AND Unknown testability) |

**Key new design element: double-blind gaps (V-05)** — the first joint diagnostic across A-12 and A-13. A condition where the mechanism hop is Opaque *and* testability is Unknown is a gap neither criterion surfaces individually.

**A-12 implementations across V-01–V-05:**
- V-01: 4-count inline tally field after last hop
- V-02: AUDITOR's dedicated per-hop table + tally
- V-03: Combined tally including inertia observability label
- V-04: Inline tally feeding routing matrix row 1
- V-05: Section D standalone table feeding D3 joint analysis

**A-13 implementations:**
- V-01/V-04: Evidence section with refinement pass + yield fields
- V-02: FRAMER computes yield; AUDITOR summarizes it
- V-03: Both F-NN and I-NN pools; pool breakdown tracked separately
- V-05: Section B dedicated to refinement; D1 is a first-class before/after table

**R7 questions seeded:** Does inline tally (V-01) produce same routing accuracy as summary table? Does AUDITOR (V-02) synthesize richer diagnostic text? Does inertia observability (V-03) shift chain pattern toward Mixed? Does the routing matrix (V-04) over- or under-fire? Do double-blind gaps (V-05) appear in practice?
rose
- V-05 introduces the first joint diagnostic: a condition that is both Opaque (A-12) and Unknown testability (A-13) is a double-blind gap that neither criterion alone surfaces

**Key R7 questions seeded:**
- Does inline tally (V-01) produce the same AMEND routing accuracy as summary table (R5-V-04)? Does compact form obscure aggregate failures?
- Does AUDITOR (V-02) produce semantically richer diagnostic rationale than inline computation because it has access to both FRAMER and ANALYST outputs simultaneously?
- Do I-NN conditions (V-03) earn more Opaque observability labels than F-NN conditions? Does including I-NN in the aggregate change the chain pattern label?
- Does the routing matrix (V-04) surface more AMEND slots per run than prose-conditional AMEND? Does mechanical routing over- or under-fire?
- Do double-blind gaps (V-05 joint diagnostic) appear in practice? What fraction of conditions are both Opaque and Unknown testability?

---

## V-01: Inline Chain Observability Tally

**Axis:** Output format — the chain-level observability aggregate (A-12) is computed as an inline tally field at the end of the mechanism section, immediately after all hops are written. No dedicated summary table. The tally counts Observable/Partial/Opaque hops, derives the pattern label (AllObservable/Mixed/PredominantlyOpaque), and declares whether a mandatory AMEND Observability slot is triggered. Testability refinement lifecycle (Unknown at genesis, refined through evidence, residual Unknowns tracked) provides A-13, drawn from V-05.

**Hypothesis:** A dedicated summary table (R5-V-04) separates observability aggregation from mechanism work, creating a two-phase structure. An inline tally integrates aggregation directly into the mechanism section: the pattern emerges from the hop sequence as it is written, rather than in retrospect. The conditional AMEND trigger must still fire from the inline label — the test is whether the gate checklist enforces this without a summary table's visual separation. The inline form is more compact; the tradeoff is whether the aggregate is as visible to the analyst when embedded vs. extracted.

```
You are running /discover-causal.
Your input is a feature hypothesis of the form "X causes Y."
Six sections. Complete each fully before advancing.
Every classification judgment uses a discrete label from a fixed set with a rationale line.

Testability lifecycle: every falsification condition starts as Unknown at generation.
The evidence pass (Section 2) refines testability where context allows. Conditions that
remain Unknown after evidence are a finding tracked as structured output in Section 2.
Residual Unknowns route to a mandatory AMEND Testability slot.

Chain observability tally: after all mechanism hops are written (Section 4), compute
a hop-count tally and derive the chain observability pattern label inline. The pattern
label directly controls whether a mandatory AMEND Observability slot is required.

---

## SECTION 1: CLAIM AND INITIAL FALSIFICATION

Claim extraction:
  X (the cause): [Extract from input]
  Y (the claimed outcome): [Extract from input]
  Full claim: ["X causes Y" -- one sentence]

Initial falsification conditions:
[From the claim alone. Assign F-NN IDs. Confidence assigned at generation time.
Testability starts Unknown for all conditions -- refined in Section 2.]

| ID | Falsification condition (claim false if observed) | Testability | Confidence | Rationale |
|----|---------------------------------------------------|-------------|------------|-----------|
| F-01 | [What would break X->Y?] | Unknown (see Sec 2) | [ ] High  [ ] Medium  [ ] Low | [1 sentence] |
| F-02 | [Add as many as the claim generates.] | Unknown (see Sec 2) | [ ] High  [ ] Medium  [ ] Low | [1 sentence] |

SECTION 1 GATE:
[ ] X and Y extracted separately
[ ] At least two F-NN conditions with IDs, testability (Unknown), confidence, and rationale
[ ] No evidence or mechanism content written

--- Do not advance to Section 2 until all items are checked. ---

---

## SECTION 2: EVIDENCE AND TESTABILITY REFINEMENT

[At least one context-specific observation required, OR "None found" with mandatory AMEND
evidence slot. After gathering evidence, run the testability refinement pass: for each F-NN
condition, decide whether the evidence enables a testability determination. I-01 from Section 3
is added to this table after inertia is completed -- leave a row placeholder for it.]

Evidence entry 1:
  Source type: [ ] Prior result  [ ] Analogous case  [ ] Domain observation  [ ] Counter-evidence
  Observation: [What was seen, where, when?]
  Bearing on X->Y: [1 sentence: supports, complicates, or challenges the claim?]

[Add entries as needed.]

Evidence quality: [ ] Strong  [ ] Moderate  [ ] Weak  [ ] None
Evidence quality rationale: [1 sentence]

Testability refinement pass:
[For each F-NN condition and I-01 from Section 3, record the testability determination
after evidence. Explain what enabled or blocked the assessment.]

| ID | Final testability | Refinement rationale |
|----|-------------------|---------------------|
| F-01 | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence: what evidence enabled or blocked determination?] |
| F-02 | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence] |
| I-01 | [ ] Easy  [ ] Hard  [ ] Unknown | [Complete after Section 3. Add here before Section 2 Gate.] |
[Mirror all F-NN and I-NN conditions.]

Testability refinement yield:
  testability_refined_count: [Count of conditions that moved from Unknown to Easy or Hard]
  testability_residual_unknown_count: [Count of conditions still Unknown after evidence]
  Residual Unknown conditions: [List condition IDs, or "None"]
  [If residual_unknown_count > 0: AMEND Testability slot is mandatory in Section 6.]

Confidence revisions:
  [Any F-NN confidence label updates based on evidence. Note ID, old label, new label,
  and rationale. Or: "No confidence revisions."]

SECTION 2 GATE:
[ ] At least one evidence entry populated (or explicit "None found" -- not skipped)
[ ] Evidence quality label assigned with rationale
[ ] Testability refinement pass completed for all F-NN and I-NN conditions
[ ] testability_refined_count and testability_residual_unknown_count both declared
[ ] Residual Unknown conditions listed by ID (or confirmed empty)

--- Do not advance to Section 3 until all items are checked. ---
--- (Complete Section 3 first to get I-01, then return to fill I-01 row in the refinement table.) ---

---

## SECTION 3: INERTIA CHECK

Status-quo description: [What happens today without X?]
Baseline rate: [Estimate or bound: "Y occurs approximately __% without X." Or: "Unknown."]

Inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP
  (SAFE = doing nothing does not produce Y;
   ADVISORY = partially produces Y for some users or conditions;
   STOP = status quo plausibly already produces Y at a meaningful rate)
Inertia rationale: [1 sentence]

| ID | Inertia falsification condition | Testability | Confidence | Rationale |
|----|---------------------------------|-------------|------------|-----------|
| I-01 | Y occurs at [baseline rate] without X | Unknown (see Sec 2) | [ ] High  [ ] Medium  [ ] Low | [1 sentence] |
[Return to Section 2 to complete I-01 testability refinement before advancing to Section 4.]

--- IF STOP: skip Section 4; advance to Section 5. ---

---

## SECTION 4: MECHANISM CHAIN

[Map the causal pathway from X to Y. Two hops minimum. Cohere with Section 2 evidence.
Every hop carries:
  Observability (Observable/Partial/Opaque): can we directly detect this intermediate state?
  Observability rationale: 1 sentence.
  Evidence coherence: Supported / Neutral / Tensions.
  Falsification connection: which F-NN or I-NN from Sections 1-3 does this hop explain?
State mechanism only -- adversarial content belongs in Section 5.]

Hop 1: X [name] -> [intermediate A]: [How does X produce A?]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Observability rationale: [1 sentence: how directly can this intermediate be detected?]
  Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
  Falsification connection: [F-NN or I-NN ID from Sections 1-3. One sentence: if this hop
    fails, this condition holds.]

Hop 2: [intermediate A] -> Y [name]: [How does A produce Y?]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Observability rationale: [1 sentence]
  Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
  Falsification connection: [F-NN or I-NN ID. One sentence.]

[Add Hop 3+ as needed. Every hop: observability label + rationale, evidence coherence,
falsification connection to a pre-existing F-NN or I-NN from Sections 1-3.]

Mechanism strength (preliminary): [ ] Strong  [ ] Moderate  [ ] Weak
  (Before adversarial challenge. Based on observability ratings and evidence coherence.)
Preliminary rationale: [1 sentence]

Chain observability tally:
  Observable hops: [Count]
  Partial hops:    [Count]
  Opaque hops:     [Count]
  Total hops:      [Count]
  Chain observability pattern: [ ] AllObservable  [ ] Mixed  [ ] PredominantlyOpaque
    (AllObservable = all hops Observable;
     PredominantlyOpaque = majority of hops Opaque;
     Mixed = all other cases)
  Pattern rationale: [1 sentence: what does this distribution mean for mechanism testability?]
  [If Mixed or PredominantlyOpaque: AMEND Observability slot is mandatory in Section 6.]

SECTION 4 GATE:
[ ] At least two hops filled
[ ] Every hop has observability label (Observable/Partial/Opaque) and rationale
[ ] Every hop has a falsification connection naming a pre-existing F-NN or I-NN
[ ] Mechanism strength (preliminary) assigned with rationale
[ ] Chain observability tally completed with all four counts
[ ] Chain observability pattern label declared with rationale
[ ] AMEND Observability slot flagged as mandatory if pattern is Mixed or PredominantlyOpaque
[ ] No adversarial content in this section

--- Do not advance to Section 5 until all items are checked. ---

---

## SECTION 5: ADVERSARIAL CHALLENGE

[Structurally separate from Section 4. Challenge every hop. Use Section 4 pattern label
and Section 2 residual Unknowns as inputs: Opaque hops and Unknown-testability conditions
are priority challenge targets. Name what would break each step, name alternatives,
identify confounders.]

Hop 1 challenge:
  What breaks X -> [intermediate A]? [Observable condition disproves this hop]
  Observable test: [What to measure or detect]
  Alternative at this hop: [What else produces [intermediate A] without X?]
  Falsification confidence: [ ] High  [ ] Medium  [ ] Low
    (Reference Section 2 testability: note if testability is Unknown and confidence is High.)
  Confidence rationale: [1 sentence]

Hop 2 challenge:
  What breaks [intermediate A] -> Y? [Observable condition]
  Observable test: [What to measure or detect]
  Alternative at this hop: [What else produces Y without [intermediate A]?]
  Falsification confidence: [ ] High  [ ] Medium  [ ] Low
  Confidence rationale: [1 sentence]

[Mirror all Section 4 hops.]

Confounders:
  Confounder 1: [Variable correlating with both X and Y. Name and describe.]

Inertia challenge:
  Adversarial view: [Does analysis reveal Y could be explained by baseline effects?]
  Revised inertia verdict: [ ] SAFE  [ ] ADVISORY  [ ] STOP  [ ] No change -- confirm

Mechanism strength (final): [ ] Strong  [ ] Moderate  [ ] Weak  [ ] NA (STOP)
Final strength rationale: [1 sentence. State whether changed from preliminary and why.]

---

## SECTION 6: SCOPE AND AMEND

Scoped claim: ["X causes Y when [condition], for [population], assuming [precondition]."]
Scope condition: [Reference adversarial findings and Section 4 chain pattern.]
Out-of-scope: [At least one context from Section 5 where mechanism fails]

Final inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP
Final inertia rationale: [1 sentence]

AMEND DIRECTIVE:
[Address at least two of the four slots. Mandatory slots are triggered by diagnostic signals:
  - Evidence slot: mandatory if Section 2 evidence quality is None
  - Inertia slot: mandatory if final inertia severity is STOP or ADVISORY
  - Observability slot: mandatory if Section 4 chain pattern is Mixed or PredominantlyOpaque
  - Testability slot: mandatory if Section 2 testability_residual_unknown_count > 0]

AMEND: discover-causal
  Narrow: [Scope tightening]
  Mechanism: [Hop notation: X -> [A] -> Y]
  Falsification: [Which HIGH confidence condition from Section 5? Name, ID, testability label
    from Section 2 refinement.]
  Evidence: [If none: "Mechanism is theoretical. Cite one context-specific observation."]
  [Inertia: (mandatory if STOP/ADVISORY) "Y occurs at [baseline] without X.
   Demonstrate incremental Y above baseline."]
  [Observability: (mandatory if Mixed or PredominantlyOpaque) "Chain observability: [pattern].
   Hops [list Opaque/Partial hops] are [Opaque/Partial]. Identify proxy measurements or
   narrow claim to the observable portion of the mechanism."]
  [Testability: (mandatory if residual_unknown_count > 0) "Conditions [list IDs] have Unknown
   testability after evidence. Determine available instrumentation before treating these
   conditions as actionable."]

---

Write artifact: simulations/discover/causal/{topic}-causal-{date}.md
Frontmatter: skill, topic, date, cause (X), outcome (Y),
             inline_chain_tally (true), gate_checklists (3),
             inertia_verdict (SAFE/ADVISORY/STOP), baseline_rate,
             evidence_count, evidence_quality (Strong/Moderate/Weak/None),
             initial_falsification_count, inertia_falsification_count,
             hop_count, mechanism_strength_preliminary (Strong/Moderate/Weak/NA),
             mechanism_strength_final (Strong/Moderate/Weak/NA),
             strength_changed (true/false),
             mechanism_hop_falsification_links (true),
             hop_observability_labels (true),
             chain_observability_pattern (AllObservable/Mixed/PredominantlyOpaque),
             observability_amend_triggered (true/false),
             testability_refined_count,
             testability_residual_unknown_count,
             testability_amend_triggered (true/false),
             falsification_testability_list (Easy/Hard/Unknown per condition after Sec 2),
             falsification_confidence_list (High/Medium/Low per condition),
             confounder_named (true/false).
```

---

## V-02: AUDITOR Role (Post-Analysis Diagnostic Synthesis)

**Axis:** Role sequence — a fourth named role (AUDITOR) runs after SKEPTIC. AUDITOR's sole function is diagnostic synthesis: it reads ANALYST's hop observability labels and computes the chain observability aggregate (A-12), reads FRAMER's testability refinement yield data (A-13), and routes AMEND slots conditionally from both. AUDITOR does not challenge mechanism, does not assign confidence, and does not propose scope. Scope and AMEND are owned by FRAMER (closing). The architectural principle: diagnostic aggregation is a distinct cognitive act from analysis, challenge, and scoping — giving it a named role forces it to be explicit and sequenced.

**Hypothesis:** In variations where A-12 and A-13 are computed inline within existing sections (V-01, V-03), there is a risk that the aggregate computation is treated as a bookkeeping step rather than a diagnostic act. An AUDITOR role assigns a named agent to the synthesis task, creating a role boundary that makes diagnostic aggregation structurally visible. AUDITOR also has the advantage of seeing both ANALYST (hops) and FRAMER (conditions) output simultaneously — it is the first role that can compute cross-role aggregates without context switching.

```
You are running /discover-causal.
Your input is a feature hypothesis of the form "X causes Y."
Four roles in sequence. Complete each role fully before advancing.
Every classification judgment uses a discrete label from a fixed set with a rationale line.

Roles:
  FRAMER (opening): claim, falsification conditions, evidence and testability refinement,
    inertia check. Testability starts Unknown; refinement yields testability_refined_count
    and testability_residual_unknown_count.
  ANALYST: mechanism chain with observability annotation per hop.
  SKEPTIC: adversarial challenge, confidence labeling, final mechanism strength.
  FRAMER (closing): claim scope, AMEND construction using AUDITOR's routing.
  AUDITOR: diagnostic synthesis -- chain observability aggregate (from ANALYST) and
    testability refinement yield summary (from FRAMER). Routes AMEND slots conditionally.
    Runs between SKEPTIC and FRAMER (closing).

---

## FRAMER (OPENING)

[FRAMER's first task: establish the claim, generate falsification conditions, gather evidence
and refine testability, run the inertia check. All conditions start with testability = Unknown.
Evidence may refine testability from Unknown to Easy or Hard. Testability yield is tracked.
FRAMER does NOT assign confidence -- that is SKEPTIC's job.]

### Step 1: Claim extraction

X (the cause): [Extract from input]
Y (the claimed outcome): [Extract from input]
Full claim: ["X causes Y" -- one sentence]

### Step 2: Initial falsification conditions

[From the claim alone. Assign F-NN IDs. Testability = Unknown at generation.
Confidence column is NOT present in this table -- SKEPTIC assigns confidence.]

| ID | Falsification condition (claim false if observed) | Testability | Rationale |
|----|---------------------------------------------------|-------------|-----------|
| F-01 | [What would break X->Y?] | Unknown | [1 sentence: what mechanism failure does this condition expose?] |
| F-02 | [Add as many as the claim generates.] | Unknown | [1 sentence] |

### Step 3: Prior evidence

[At least one context-specific observation, OR "None found" with mandatory AMEND evidence slot.
Evidence may refine testability for any F-NN or I-NN condition.]

Evidence entry 1:
  Source type: [ ] Prior result  [ ] Analogous case  [ ] Domain observation  [ ] Counter-evidence
  Observation: [What was seen, where, when?]
  Bearing on X->Y: [1 sentence: supports, complicates, or challenges the claim?]

[Add entries as needed.]

Evidence quality: [ ] Strong  [ ] Moderate  [ ] Weak  [ ] None
Evidence quality rationale: [1 sentence]

### Step 4: Testability refinement

[After evidence, revisit every F-NN and I-NN condition. Record the determination after
evidence. I-01 row is added here after Step 5 inertia check is complete.]

| ID | Testability after evidence | Refinement rationale |
|----|---------------------------|---------------------|
| F-01 | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence: what evidence enabled or blocked the determination?] |
| F-02 | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence] |
| I-01 | [ ] Easy  [ ] Hard  [ ] Unknown | [Complete after Step 5. Add here before FRAMER gate.] |
[Mirror all F-NN and I-NN conditions.]

Testability refinement yield (FRAMER's diagnostic output -- AUDITOR will aggregate):
  testability_refined_count: [Count of conditions that moved from Unknown to Easy or Hard]
  testability_residual_unknown_count: [Count still Unknown after evidence]
  Residual Unknown IDs: [List, or "None"]

### Step 5: Inertia check

Status-quo description: [One sentence: what happens today without X?]
Baseline rate: [Estimate or bound. Or: "Unknown."]

Inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP
  (SAFE = does not produce Y; ADVISORY = partially; STOP = plausibly already produces Y)
Inertia rationale: [1 sentence]

| ID | Inertia falsification condition | Testability | Rationale |
|----|---------------------------------|-------------|-----------|
| I-01 | Y occurs at [baseline rate] without X | Unknown (see Step 4) | [1 sentence] |
[Return to Step 4 to complete I-01 testability refinement before gate.]

FRAMER (OPENING) GATE:
[ ] At least two F-NN conditions with IDs, testability (Unknown), and rationale
[ ] Confidence column NOT present in the F-NN table
[ ] Evidence populated (or explicit "None found" -- not skipped)
[ ] Evidence quality label assigned with rationale
[ ] Testability refinement pass completed for all F-NN and I-NN conditions
[ ] testability_refined_count and testability_residual_unknown_count declared
[ ] Inertia severity label assigned with rationale

--- Do not advance to ANALYST until all FRAMER (OPENING) GATE items are checked. ---
--- IF STOP: skip ANALYST; advance to SKEPTIC. ---

---

## ANALYST

[ANALYST's sole job: map the causal chain from X to Y. Every hop carries observability
annotation. Falsification connections reference FRAMER's F-NN and I-NN conditions.
ANALYST does NOT assign testability (FRAMER owns testability) or confidence (SKEPTIC owns
confidence). ANALYST does NOT compute the chain observability aggregate -- AUDITOR does that.
State the hop-level labels only; AUDITOR computes the chain-level pattern.]

Mechanism chain: [Two hops minimum.]

  Hop 1: X [name] -> [intermediate A]: [How does X produce A?]
    Observability: [ ] Observable  [ ] Partial  [ ] Opaque
    Observability rationale: [1 sentence: how directly can this intermediate be detected?]
    Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
    Falsification connection: [Which F-NN or I-NN from FRAMER's tables does this hop explain?
      State the ID. One sentence: if this hop fails, this condition holds.]

  Hop 2: [intermediate A] -> Y [name]: [How does A produce Y?]
    Observability: [ ] Observable  [ ] Partial  [ ] Opaque
    Observability rationale: [1 sentence]
    Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
    Falsification connection: [F-NN or I-NN ID. One sentence.]

  [Add Hop 3+ as needed. Every hop: observability label + rationale, evidence coherence,
  falsification connection to a pre-existing FRAMER condition.]

Mechanism strength (preliminary): [ ] Strong  [ ] Moderate  [ ] Weak
  (Before SKEPTIC challenge. ANALYST's view from observability ratings and evidence coherence.)
Preliminary rationale: [1 sentence]

ANALYST GATE:
[ ] At least two hops filled
[ ] Every hop has observability label (Observable/Partial/Opaque) and rationale
[ ] Every hop has a falsification connection naming a pre-existing FRAMER F-NN or I-NN
[ ] Mechanism strength (preliminary) assigned with rationale
[ ] No confidence labels assigned to conditions in this section
[ ] No chain observability aggregate computed in this section (AUDITOR's job)

--- Do not advance to SKEPTIC until all ANALYST GATE items are checked. ---

---

## SKEPTIC

[SKEPTIC challenges every hop, assigns confidence labels to all falsification conditions,
and delivers the final mechanism strength. SKEPTIC does NOT reassign testability (FRAMER)
or compute observability aggregate (AUDITOR). SKEPTIC is the final analytical voice before
AUDITOR aggregates and FRAMER closes.]

Hop-by-hop challenge:

  Hop 1 challenge:
    What breaks X -> [intermediate A]? [Observable condition disproves this hop]
    Observable test: [Specific measurement or event]
    Alternative at this hop: [What else produces [intermediate A] without X?]
    Confidence: [ ] High  [ ] Medium  [ ] Low
    Confidence rationale: [1 sentence]

  Hop 2 challenge:
    What breaks [intermediate A] -> Y? [Observable condition]
    Observable test: [Specific measurement or event]
    Alternative at this hop: [What else produces Y without [intermediate A]?]
    Confidence: [ ] High  [ ] Medium  [ ] Low
    Confidence rationale: [1 sentence]

  [Mirror all ANALYST hops.]

Confounders:
  Confounder 1: [Variable correlating with both X and Y. Name and describe.]

Inertia challenge:
  Adversarial view: [Does mechanism analysis change the inertia verdict?]
  Revised verdict: [ ] Confirms FRAMER  [ ] Upgrades to ADVISORY  [ ] Upgrades to STOP

Final falsification table (FRAMER testability + SKEPTIC confidence):

| ID | Falsification condition | Testability (FRAMER) | Confidence (SKEPTIC) | Rationale |
|----|------------------------|----------------------|----------------------|-----------|
| F-01 | [Condition text] | [FRAMER's final label] | [ ] High  [ ] Med  [ ] Low | [1 sentence] |
| I-01 | [Inertia condition] | [FRAMER's final label] | [ ] High  [ ] Med  [ ] Low | [1 sentence] |
[Mirror all conditions. Testability column carries FRAMER's labels unchanged.]

Mechanism strength (final): [ ] Strong  [ ] Moderate  [ ] Weak  [ ] NA (STOP)
Final strength rationale: [1 sentence. State whether changed from ANALYST preliminary.]

SKEPTIC GATE:
[ ] Every ANALYST hop has a challenge row with confidence label and rationale
[ ] At least one alternative named per hop
[ ] Inertia challenge verdict declared
[ ] At least one confounder named
[ ] Final falsification table complete with both testability (FRAMER) and confidence (SKEPTIC)
[ ] Testability column carries FRAMER labels unchanged
[ ] Final mechanism strength assigned with rationale

--- Do not advance to AUDITOR until all SKEPTIC GATE items are checked. ---

---

## AUDITOR

[AUDITOR is a diagnostic synthesis role, not an analysis role. AUDITOR reads ANALYST's
hop observability labels and FRAMER's testability refinement yield data. AUDITOR computes
the two aggregate diagnostics and declares which AMEND slots are mandatory. AUDITOR does
not challenge mechanism, does not propose scope, and does not reopen analytical questions.
AUDITOR produces a diagnostic summary that FRAMER (closing) uses to construct AMEND.]

### Diagnostic 1: Chain Observability Aggregate (from ANALYST)

[Enumerate each hop's observability label from ANALYST's section. Count labels.
Derive the chain-level pattern.]

| Hop | Mechanism step | Observability label |
|-----|---------------|---------------------|
| Hop 1 | X -> [intermediate A] | [Observable/Partial/Opaque from ANALYST] |
| Hop 2 | [intermediate A] -> Y | [Observable/Partial/Opaque from ANALYST] |
[Mirror all ANALYST hops.]

Chain observability tally:
  Observable: [Count]
  Partial:    [Count]
  Opaque:     [Count]
Chain observability pattern: [ ] AllObservable  [ ] Mixed  [ ] PredominantlyOpaque
Pattern rationale: [1 sentence: what does this distribution mean for mechanism testability?]
AMEND Observability slot: [ ] Required (Mixed or PredominantlyOpaque)  [ ] Not required

### Diagnostic 2: Testability Refinement Yield Summary (from FRAMER)

[Reproduce FRAMER's yield data. Assess whether the yield is sufficient.]

testability_refined_count (from FRAMER): [Value]
testability_residual_unknown_count (from FRAMER): [Value]
Residual Unknown IDs: [From FRAMER]
Yield quality: [ ] High (most conditions resolved)  [ ] Medium (some resolved)  [ ] Low (few resolved)
Yield quality rationale: [1 sentence: does the evidence quality explain the yield rate?]
AMEND Testability slot: [ ] Required (residual_unknown_count > 0)  [ ] Not required

### AMEND Routing Declaration

[AUDITOR declares mandatory slots. FRAMER (closing) uses this declaration verbatim.]

Mandatory AMEND slots:
| Signal | Diagnostic value | AMEND slot triggered? |
|--------|-----------------|----------------------|
| Chain observability pattern | [AllObservable/Mixed/PredominantlyOpaque] | [ ] Yes -- Observability  [ ] No |
| testability_residual_unknown_count | [Count] | [ ] Yes -- Testability  [ ] No |
| Evidence quality (from FRAMER) | [Strong/Moderate/Weak/None] | [ ] Yes -- Evidence (if None)  [ ] No |
| Inertia severity (from FRAMER/SKEPTIC) | [SAFE/ADVISORY/STOP] | [ ] Yes -- Inertia (if STOP/ADVISORY)  [ ] No |

Required slots summary: [List all required slots from the table above, or "Narrow and Mechanism only."]

AUDITOR NOTE:
[One sentence: what is the most important diagnostic finding? Which finding, if unaddressed,
most endangers the causal claim?]

---

## FRAMER (CLOSING)

Scoped claim: ["X causes Y when [condition], for [population], assuming [precondition]."]
Scope condition: [Reference SKEPTIC findings and AUDITOR diagnostic note.]
Out-of-scope: [At least one condition where mechanism fails]

Final inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP
Final inertia rationale: [1 sentence]

AMEND DIRECTIVE:
[Construct AMEND using AUDITOR's routing declaration. Address all required slots.]

AMEND: discover-causal
  Narrow: [Scope tightening]
  Mechanism: [Hop notation: X -> [A] -> Y]
  Falsification: [HIGH confidence condition from SKEPTIC's final table. Name, ID,
    testability from FRAMER, confidence from SKEPTIC.]
  Evidence: [If None: "Mechanism is theoretical. Cite one context-specific observation."]
  [Inertia: (mandatory if STOP/ADVISORY per AUDITOR routing) "Y occurs at [baseline] without X.
   Demonstrate incremental Y above baseline."]
  [Observability: (mandatory if AUDITOR flagged Mixed/PredominantlyOpaque) "Chain pattern: [label].
   Hops [list Opaque hops] are unobservable. Identify proxy measurements or narrow claim."]
  [Testability: (mandatory if AUDITOR flagged residual Unknowns) "Conditions [IDs] have Unknown
   testability after evidence. Determine instrumentation before treating as actionable."]

---

Write artifact: simulations/discover/causal/{topic}-causal-{date}.md
Frontmatter: skill, topic, date, cause (X), outcome (Y),
             auditor_role (true), role_count (4), gate_checklists (3),
             inertia_verdict (SAFE/ADVISORY/STOP), baseline_rate,
             evidence_count, evidence_quality (Strong/Moderate/Weak/None),
             initial_falsification_count, inertia_falsification_count,
             hop_count, mechanism_strength_preliminary (Strong/Moderate/Weak/NA),
             mechanism_strength_final (Strong/Moderate/Weak/NA),
             strength_changed (true/false),
             mechanism_hop_falsification_links (true),
             hop_observability_labels (true),
             chain_observability_pattern (AllObservable/Mixed/PredominantlyOpaque),
             observability_amend_triggered (true/false),
             testability_refined_count,
             testability_residual_unknown_count,
             testability_amend_triggered (true/false),
             auditor_yield_quality (High/Medium/Low),
             falsification_testability_list (Easy/Hard/Unknown per condition),
             falsification_confidence_list (High/Medium/Low per condition),
             confounder_named (true/false).
```

---

## V-03: Inertia-Inclusive Aggregates

**Axis:** Inertia framing — I-NN conditions fully participate in both aggregate diagnostics. For A-13: I-01 starts Unknown at genesis (like F-NN conditions), undergoes testability refinement during evidence, and its final state contributes to testability_refined_count and testability_residual_unknown_count. For A-12: the chain observability aggregate includes an explicit inertia observability check — how observable is the baseline mechanism that produces Y without X? This creates an "inertia hop" with an observability label that contributes to the chain pattern. Research question: do inertia conditions earn more Opaque observability labels than F-NN conditions, reflecting that the counterfactual "Y without X" is structurally harder to observe directly?

**Hypothesis:** In prior variations, inertia was a check (does the status quo produce Y?) but not a mechanism hop. Giving the inertia baseline an observability label forces the question: can we actually measure whether Y occurs without X? If the inertia baseline is Opaque — if we cannot directly observe the counterfactual — then even a SAFE inertia verdict is weak. Including inertia observability in the chain aggregate may shift the pattern toward Mixed or PredominantlyOpaque more often than mechanism hops alone, surfacing a class of observability failure that A-12 was not designed to catch.

```
You are running /discover-causal.
Your input is a feature hypothesis of the form "X causes Y."
Six sections. Complete each fully before advancing. Gate checklists close Sections 1, 2, and 4.
Every classification judgment uses a discrete label from a fixed set with a rationale line.

Two-pool falsification design:
  F-NN pool: claim-derived conditions (Section 1). Testability = Unknown at genesis.
  I-NN pool: inertia-derived conditions (Section 2). Testability = Unknown at genesis.
Both pools undergo testability refinement in Section 3 (evidence).
Both pools contribute to the chain observability aggregate in Section 4.

Testability lifecycle: all conditions (F-NN and I-NN) start Unknown. Section 3 refines.
Yield: testability_refined_count and testability_residual_unknown_count include both pools.

Chain observability aggregate: mechanism hops (Section 4) plus inertia observability
label (Section 2). Inertia observability answers: "Can we directly observe whether Y
occurs without X?" This label contributes to the chain-level pattern.

---

## SECTION 1: CLAIM AND INITIAL FALSIFICATION

Claim extraction:
  X (the cause): [Extract from input]
  Y (the claimed outcome): [Extract from input]
  Full claim: ["X causes Y" -- one sentence]

F-NN pool (claim-derived falsification conditions):
[From the claim alone. Assign F-01, F-02, ... Confidence assigned at generation.
Testability = Unknown. Both pools use the same column structure.]

| ID | Falsification condition (claim false if observed) | Testability | Confidence | Rationale |
|----|---------------------------------------------------|-------------|------------|-----------|
| F-01 | [What would break X->Y?] | Unknown (see Sec 3) | [ ] High  [ ] Medium  [ ] Low | [1 sentence] |
| F-02 | [Add as many as the claim generates.] | Unknown (see Sec 3) | [ ] High  [ ] Medium  [ ] Low | [1 sentence] |

SECTION 1 GATE:
[ ] X and Y extracted separately
[ ] At least two F-NN conditions with IDs, testability (Unknown), confidence, and rationale

--- Do not advance to Section 2 until Section 1 gate is checked. ---

---

## SECTION 2: INERTIA CHECK

[Inertia first, before evidence -- the null hypothesis (Y without X) is the primary
competitor to the causal claim. I-NN conditions start Unknown like F-NN conditions.
Inertia observability: how directly can we observe whether Y occurs without X?
This label contributes to the chain observability aggregate in Section 4.]

Status-quo description: [What happens today without X?]
Baseline rate: [Estimate or bound. Or: "Unknown."]

Inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP
  (SAFE = does not produce Y; ADVISORY = partially; STOP = plausibly already produces Y)
Inertia rationale: [1 sentence]

Inertia observability:
  How directly can we observe whether Y occurs at the baseline rate without X?
  Inertia observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Inertia observability rationale: [1 sentence: what data source or measurement would confirm
    or deny that Y occurs without X? Is it available?]
  [This label contributes to the chain observability aggregate in Section 4.]

I-NN pool (inertia-derived falsification conditions):

| ID | Inertia falsification condition | Testability | Confidence | Rationale |
|----|---------------------------------|-------------|------------|-----------|
| I-01 | Y occurs at [baseline rate] without X | Unknown (see Sec 3) | [ ] High  [ ] Medium  [ ] Low | [1 sentence] |
[Add I-NN conditions as needed. Each starts Unknown.]

--- IF STOP: skip Sections 3 and 4; advance to Section 5. ---

---

## SECTION 3: EVIDENCE AND TESTABILITY REFINEMENT

[At least one context-specific observation, OR "None found" with mandatory AMEND evidence slot.
Testability refinement covers both F-NN and I-NN conditions. Evidence may revise testability
from Unknown to Easy or Hard, or revise confidence labels. Yield tracks both pools.]

Evidence entry 1:
  Source type: [ ] Prior result  [ ] Analogous case  [ ] Domain observation  [ ] Counter-evidence
  Observation: [What was seen, where, when?]
  Bearing on X->Y: [1 sentence]
  Bearing on inertia: [1 sentence: does this evidence speak to the baseline rate?]

[Add entries as needed.]

Evidence quality: [ ] Strong  [ ] Moderate  [ ] Weak  [ ] None
Evidence quality rationale: [1 sentence]

Testability refinement pass (both F-NN and I-NN pools):
[For each condition, record final testability after evidence.]

| Pool | ID | Final testability | Refinement rationale |
|------|----|-------------------|---------------------|
| F-NN | F-01 | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence] |
| F-NN | F-02 | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence] |
| I-NN | I-01 | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence: is the counterfactual baseline testable?] |
[Mirror all F-NN and I-NN conditions.]

Testability refinement yield (both pools combined):
  testability_refined_count: [Conditions from either pool that moved Unknown -> Easy/Hard]
  testability_residual_unknown_count: [Conditions from either pool still Unknown after evidence]
  Residual Unknown IDs: [List by pool and ID, or "None"]
  Pool breakdown (informational):
    F-NN residual unknown: [Count]
    I-NN residual unknown: [Count]
    [If I-NN residual unknown > F-NN residual unknown: note this asymmetry as a finding.]
  [If residual_unknown_count > 0: AMEND Testability slot is mandatory in Section 6.]

SECTION 2 GATE (complete before Section 3 evidence; return here to complete refinement):
[ ] Inertia severity label assigned with rationale
[ ] Inertia observability label assigned (Observable/Partial/Opaque) with rationale
[ ] At least one I-NN condition with ID, testability (Unknown), confidence, and rationale

SECTION 3 GATE:
[ ] Evidence populated (or explicit "None found" -- not skipped)
[ ] Evidence quality label assigned with rationale
[ ] Testability refinement pass completed for all F-NN and I-NN conditions
[ ] testability_refined_count and testability_residual_unknown_count declared with pool breakdown
[ ] Residual Unknown conditions listed by pool and ID (or confirmed empty)

--- Do not advance to Section 4 until Section 3 gate is checked. ---

---

## SECTION 4: MECHANISM CHAIN

[Map the causal pathway from X to Y. Two hops minimum. After all hops, the chain
observability aggregate includes both mechanism hops AND the inertia observability
label from Section 2. This makes the aggregate sensitive to both mechanism opacity
and baseline observability.]

Hop 1: X [name] -> [intermediate A]: [How does X produce A?]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Observability rationale: [1 sentence]
  Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
  Falsification connection: [F-NN or I-NN ID from Sections 1-2. One sentence.]

Hop 2: [intermediate A] -> Y [name]: [How does A produce Y?]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Observability rationale: [1 sentence]
  Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
  Falsification connection: [F-NN or I-NN ID. One sentence.]

[Add Hop 3+ as needed. Mechanism hops only -- inertia observability computed separately.]

Mechanism strength (preliminary): [ ] Strong  [ ] Moderate  [ ] Weak
Preliminary rationale: [1 sentence]

Chain observability aggregate (mechanism hops + inertia):
  Mechanism hop observability:
  | Hop | Step | Observability |
  |-----|------|---------------|
  | Hop 1 | X -> [A] | [Observable/Partial/Opaque] |
  | Hop 2 | [A] -> Y | [Observable/Partial/Opaque] |
  [Mirror all hops.]

  Inertia observability (from Section 2): [Observable/Partial/Opaque]
  Inertia contribution note: [1 sentence: does inertia observability strengthen or weaken
    the chain pattern relative to mechanism hops alone?]

  Combined tally:
    Observable: [Count -- hops + inertia]
    Partial:    [Count]
    Opaque:     [Count]
  Chain observability pattern: [ ] AllObservable  [ ] Mixed  [ ] PredominantlyOpaque
  Pattern rationale: [1 sentence]
  [If Mixed or PredominantlyOpaque: AMEND Observability slot is mandatory in Section 6.]

SECTION 4 GATE:
[ ] At least two mechanism hops with observability label + rationale and falsification connection
[ ] Mechanism strength (preliminary) assigned with rationale
[ ] Inertia observability included in combined tally
[ ] Chain observability pattern declared with rationale
[ ] AMEND Observability slot flagged as mandatory if Mixed or PredominantlyOpaque
[ ] No adversarial content in this section

--- Do not advance to Section 5 until all items are checked. ---

---

## SECTION 5: ADVERSARIAL CHALLENGE

[Structurally separate from Section 4. Challenge every mechanism hop. Challenge the inertia
verdict with the additional question: even if Y does not occur at full rate without X, could
the baseline partially explain the observed Y? Name confounders.]

Hop 1 challenge:
  What breaks X -> [intermediate A]? [Observable condition]
  Observable test: [What to measure or detect]
  Alternative at this hop: [What else produces [intermediate A] without X?]
  Falsification confidence: [ ] High  [ ] Medium  [ ] Low
  Confidence rationale: [1 sentence. Note testability from Section 3 if relevant.]

Hop 2 challenge:
  What breaks [intermediate A] -> Y? [Observable condition]
  Observable test: [What to measure or detect]
  Alternative at this hop: [What else produces Y without [intermediate A]?]
  Falsification confidence: [ ] High  [ ] Medium  [ ] Low
  Confidence rationale: [1 sentence]

[Mirror all Section 4 mechanism hops.]

Confounders:
  Confounder 1: [Variable correlating with both X and Y. Name and describe.]

Inertia challenge:
  [Beyond the inertia severity rating: does the adversarial view suggest the baseline
  explanation is stronger than Section 2 indicated? Does inertia observability affect
  confidence in the SAFE/ADVISORY/STOP rating?]
  Adversarial inertia view: [1-2 sentences]
  Revised inertia verdict: [ ] Confirms  [ ] Upgrades to ADVISORY  [ ] Upgrades to STOP

Mechanism strength (final): [ ] Strong  [ ] Moderate  [ ] Weak  [ ] NA (STOP)
Final strength rationale: [1 sentence. State whether changed from preliminary.]

---

## SECTION 6: SCOPE AND AMEND

Scoped claim: ["X causes Y when [condition], for [population], assuming [precondition]."]
Out-of-scope: [At least one condition from Section 5 where mechanism fails]

Final inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP

AMEND DIRECTIVE:
[Mandatory slots triggered by diagnostic signals:]

AMEND: discover-causal
  Narrow: [Scope tightening]
  Mechanism: [Hop notation: X -> [A] -> Y]
  Falsification: [HIGH confidence condition from Section 5. Name, ID, testability from Section 3.]
  Evidence: [If None: "Mechanism is theoretical. Cite one context-specific observation."]
  [Inertia: (mandatory if STOP/ADVISORY) "Y occurs at [baseline] without X.
   Demonstrate incremental Y above baseline."]
  [Observability: (mandatory if Section 4 pattern is Mixed or PredominantlyOpaque)
   "Chain pattern: [label] including inertia observability. Opaque elements: [list].
   Identify proxy measurements or narrow claim to observable portion."]
  [Testability: (mandatory if Section 3 residual_unknown_count > 0)
   "Conditions [IDs by pool] have Unknown testability. Determine instrumentation.
   Note if I-NN conditions are disproportionately Unknown."]

---

Write artifact: simulations/discover/causal/{topic}-causal-{date}.md
Frontmatter: skill, topic, date, cause (X), outcome (Y),
             inertia_inclusive_aggregates (true), gate_checklists (4),
             inertia_verdict (SAFE/ADVISORY/STOP), baseline_rate,
             inertia_observability (Observable/Partial/Opaque),
             evidence_count, evidence_quality (Strong/Moderate/Weak/None),
             initial_falsification_count, inertia_falsification_count,
             hop_count, mechanism_strength_preliminary (Strong/Moderate/Weak/NA),
             mechanism_strength_final (Strong/Moderate/Weak/NA),
             strength_changed (true/false),
             mechanism_hop_falsification_links (true),
             hop_observability_labels (true),
             chain_observability_pattern (AllObservable/Mixed/PredominantlyOpaque),
             inertia_included_in_aggregate (true),
             observability_amend_triggered (true/false),
             testability_refined_count,
             testability_residual_unknown_count,
             fnn_residual_unknown_count,
             inn_residual_unknown_count,
             testability_amend_triggered (true/false),
             falsification_testability_list (Easy/Hard/Unknown per condition after Sec 3),
             falsification_confidence_list (High/Medium/Low per condition),
             confounder_named (true/false).
```

---

## V-04: AMEND Routing Matrix

**Axis:** Output format (combination with lifecycle) — the AMEND block is generated by evaluating a formal 4-row routing matrix. Each row maps a named diagnostic signal to a named AMEND slot with a binary trigger. The matrix is filled in explicitly after the adversarial section: each row is evaluated with the current diagnostic value and the trigger is marked. The list of triggered slots is then used to construct the AMEND block mechanically. A-12 fires via the chain observability pattern row; A-13 fires via the testability residual Unknowns row. The routing matrix replaces prose-conditional AMEND construction ("Mandatory: evidence slot if...") with a structured decision table.

**Hypothesis:** In all prior variations, AMEND slot construction is prose-conditional: the instruction lists which slots are mandatory and under what conditions, but the analyst must read the conditions and decide. This creates two failure modes: (1) the analyst misses a trigger because the condition is buried in prose, and (2) the analyst adds slots not triggered by actual findings (defensive over-AMENDing). A routing matrix makes slot generation observable and auditable: any run produces a visible matrix with trigger values, and the triggered slots are listed before the AMEND block is written. This diagnostic artifact is the R6 contribution to AMEND construction methodology.

```
You are running /discover-causal.
Your input is a feature hypothesis of the form "X causes Y."
Seven sections. Complete each fully before advancing.
Every classification judgment uses a discrete label from a fixed set with a rationale line.

Testability lifecycle: all conditions start Unknown. Section 3 refines.
testability_refined_count and testability_residual_unknown_count are computed in Section 3.
Residual Unknowns are a finding; they feed row 2 of the routing matrix in Section 7.

Chain observability pattern: computed inline in Section 4 (tally then label).
Chain pattern feeds row 1 of the routing matrix in Section 7.

AMEND routing matrix: Section 7 evaluates all 4 trigger conditions and generates the
required AMEND slots mechanically from the matrix result. AMEND block follows the matrix.

---

## SECTION 1: CLAIM AND INITIAL FALSIFICATION

Claim extraction:
  X (the cause): [Extract from input]
  Y (the claimed outcome): [Extract from input]
  Full claim: ["X causes Y" -- one sentence]

Initial falsification conditions:
[From claim alone. Confidence assigned at generation. Testability = Unknown for all.]

| ID | Falsification condition (claim false if observed) | Testability | Confidence | Rationale |
|----|---------------------------------------------------|-------------|------------|-----------|
| F-01 | [What would break X->Y?] | Unknown | [ ] High  [ ] Medium  [ ] Low | [1 sentence] |
| F-02 | [Add as many as the claim generates.] | Unknown | [ ] High  [ ] Medium  [ ] Low | [1 sentence] |

---

## SECTION 2: INERTIA CHECK

Status-quo description: [What happens today without X?]
Baseline rate: [Estimate or bound. Or: "Unknown."]

Inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP
  (SAFE = does not produce Y; ADVISORY = partially; STOP = plausibly already produces Y)
Inertia rationale: [1 sentence]

| ID | Inertia falsification condition | Testability | Confidence | Rationale |
|----|---------------------------------|-------------|------------|-----------|
| I-01 | Y occurs at [baseline rate] without X | Unknown | [ ] High  [ ] Medium  [ ] Low | [1 sentence] |

--- IF STOP: skip Sections 3 and 4; advance to Section 5. ---

---

## SECTION 3: EVIDENCE AND TESTABILITY REFINEMENT

[At least one context-specific observation, OR "None found."
Testability refinement pass covers all F-NN and I-NN conditions.]

Evidence entry 1:
  Source type: [ ] Prior result  [ ] Analogous case  [ ] Domain observation  [ ] Counter-evidence
  Observation: [What was seen, where, when?]
  Bearing on X->Y: [1 sentence]

[Add entries as needed.]

Evidence quality: [ ] Strong  [ ] Moderate  [ ] Weak  [ ] None
Evidence quality rationale: [1 sentence]
[If None: matrix row 4 will trigger AMEND Evidence slot.]

Testability refinement pass:

| ID | Final testability | Refinement rationale |
|----|-------------------|---------------------|
| F-01 | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence] |
| F-02 | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence] |
| I-01 | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence] |
[Mirror all conditions.]

Testability refinement yield:
  testability_refined_count: [Count moved Unknown -> Easy or Hard]
  testability_residual_unknown_count: [Count still Unknown]
  Residual Unknown IDs: [List, or "None"]
  [Carry testability_residual_unknown_count to Section 7 routing matrix row 2.]

SECTION 3 GATE:
[ ] Evidence populated (or explicit "None found" -- not skipped)
[ ] Evidence quality label assigned with rationale
[ ] Testability refinement pass completed for all conditions
[ ] testability_refined_count and testability_residual_unknown_count declared
[ ] Residual Unknown IDs listed (or confirmed empty)

--- Do not advance to Section 4 until all items are checked. ---

---

## SECTION 4: MECHANISM CHAIN

[Map the causal pathway. Two hops minimum. Every hop carries observability label + rationale
+ evidence coherence + falsification connection. After all hops, compute chain observability
tally and pattern label inline. Carry pattern label to Section 7 routing matrix row 1.]

Hop 1: X [name] -> [intermediate A]: [How does X produce A?]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Observability rationale: [1 sentence]
  Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
  Falsification connection: [F-NN or I-NN ID from Sections 1-2. One sentence.]

Hop 2: [intermediate A] -> Y [name]: [How does A produce Y?]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Observability rationale: [1 sentence]
  Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
  Falsification connection: [F-NN or I-NN ID. One sentence.]

[Add Hop 3+ as needed.]

Mechanism strength (preliminary): [ ] Strong  [ ] Moderate  [ ] Weak
Preliminary rationale: [1 sentence]

Chain observability tally:
  Observable: [Count]   Partial: [Count]   Opaque: [Count]   Total: [Count]
Chain observability pattern: [ ] AllObservable  [ ] Mixed  [ ] PredominantlyOpaque
Pattern rationale: [1 sentence]
[Carry chain observability pattern to Section 7 routing matrix row 1.]

SECTION 4 GATE:
[ ] At least two hops with observability label + rationale + falsification connection
[ ] Mechanism strength (preliminary) assigned with rationale
[ ] Chain observability tally completed with all counts
[ ] Chain observability pattern label declared with rationale

--- Do not advance to Section 5 until all items are checked. ---

---

## SECTION 5: ADVERSARIAL CHALLENGE

[Structurally separate from Section 4. Challenge every hop. Name alternatives. Confounders.]

Hop 1 challenge:
  What breaks X -> [intermediate A]? [Observable condition]
  Observable test: [What to measure or detect]
  Alternative at this hop: [What else produces [intermediate A] without X?]
  Falsification confidence: [ ] High  [ ] Medium  [ ] Low
  Confidence rationale: [1 sentence]

Hop 2 challenge:
  What breaks [intermediate A] -> Y? [Observable condition]
  Observable test: [What to measure or detect]
  Alternative at this hop: [What else produces Y without [intermediate A]?]
  Falsification confidence: [ ] High  [ ] Medium  [ ] Low
  Confidence rationale: [1 sentence]

[Mirror all Section 4 hops.]

Confounders:
  Confounder 1: [Variable correlating with both X and Y. Name and describe.]

Inertia challenge:
  Adversarial view: [Does mechanism analysis change the inertia verdict?]
  Revised verdict: [ ] Confirms  [ ] Upgrades to ADVISORY  [ ] Upgrades to STOP

Mechanism strength (final): [ ] Strong  [ ] Moderate  [ ] Weak  [ ] NA (STOP)
Final strength rationale: [1 sentence. State whether changed from preliminary.]

---

## SECTION 6: CLAIM SCOPE

Scoped claim: ["X causes Y when [condition], for [population], assuming [precondition]."]
Scope condition: [Reference adversarial findings and chain pattern from Section 4.]
Out-of-scope: [At least one condition from Section 5 where mechanism fails]

Final inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP
Final inertia rationale: [1 sentence]

---

## SECTION 7: AMEND ROUTING MATRIX AND DIRECTIVE

[Evaluate each routing row with the current diagnostic value. Mark trigger. Triggered
rows produce mandatory AMEND slots. Evaluate all four rows before writing AMEND.]

AMEND routing matrix:

| Row | Diagnostic signal | Current value | Trigger condition | Slot triggered? |
|-----|------------------|---------------|-------------------|-----------------|
| 1 | Chain observability pattern (Section 4) | [AllObservable/Mixed/PredominantlyOpaque] | Mixed or PredominantlyOpaque | [ ] Yes -- Observability  [ ] No |
| 2 | testability_residual_unknown_count (Section 3) | [Count] | Count > 0 | [ ] Yes -- Testability  [ ] No |
| 3 | Final inertia severity (Section 6) | [SAFE/ADVISORY/STOP] | STOP or ADVISORY | [ ] Yes -- Inertia  [ ] No |
| 4 | Evidence quality (Section 3) | [Strong/Moderate/Weak/None] | None | [ ] Yes -- Evidence  [ ] No |

Triggered slots: [List all Yes rows, e.g., "Observability, Testability" -- or "None (Narrow + Mechanism only)"]

AMEND DIRECTIVE:
[Address all triggered slots plus at minimum Narrow and Falsification.]

AMEND: discover-causal
  Narrow: [Scope tightening]
  Mechanism: [Hop notation: X -> [A] -> Y]
  Falsification: [HIGH confidence condition from Section 5. Name, ID, testability from Section 3.]
  Evidence: [Row 4 triggered: "Mechanism is theoretical. Cite one context-specific observation."]
  [Inertia: (row 3 triggered) "Y occurs at [baseline] without X.
   Demonstrate incremental Y above baseline."]
  [Observability: (row 1 triggered) "Chain pattern: [label]. Opaque hops: [list].
   Identify proxy measurements or narrow to observable mechanism portion."]
  [Testability: (row 2 triggered) "Conditions [IDs] have Unknown testability after evidence.
   Determine instrumentation before treating as actionable."]

[Include only the slots whose row triggered. Omit untriggered slots entirely.]

---

Write artifact: simulations/discover/causal/{topic}-causal-{date}.md
Frontmatter: skill, topic, date, cause (X), outcome (Y),
             amend_routing_matrix (true), gate_checklists (2),
             inertia_verdict (SAFE/ADVISORY/STOP), baseline_rate,
             evidence_count, evidence_quality (Strong/Moderate/Weak/None),
             initial_falsification_count, inertia_falsification_count,
             hop_count, mechanism_strength_preliminary (Strong/Moderate/Weak/NA),
             mechanism_strength_final (Strong/Moderate/Weak/NA),
             strength_changed (true/false),
             mechanism_hop_falsification_links (true),
             hop_observability_labels (true),
             chain_observability_pattern (AllObservable/Mixed/PredominantlyOpaque),
             amend_routing_matrix_row1_triggered (true/false),
             amend_routing_matrix_row2_triggered (true/false),
             amend_routing_matrix_row3_triggered (true/false),
             amend_routing_matrix_row4_triggered (true/false),
             amend_slots_triggered (list),
             testability_refined_count,
             testability_residual_unknown_count,
             falsification_testability_list (Easy/Hard/Unknown per condition),
             falsification_confidence_list (High/Medium/Low per condition),
             confounder_named (true/false).
```

---

## V-05: Dual-Diagnostic Yield Section

**Axis:** Lifecycle emphasis (combination with output format) — a dedicated "Section D: Diagnostic Yield" runs between mechanism (Section C) and adversarial challenge (Section E). Section D computes both A-12 and A-13 in parallel. The two diagnostics are treated as a pair: testability refinement yield (before/after table per condition) and chain observability aggregate (per-hop table + pattern label). After computing both, Section D produces a joint gap analysis: conditions that are both Opaque (their mechanism hop is unobservable) AND have Unknown testability are flagged as "double-blind gaps" — gaps that cannot be tested because we cannot see the hop AND do not know how to run the test. This joint finding type is new and not surfaced by either A-12 or A-13 individually.

**Hypothesis:** A-12 and A-13 were designed independently: A-12 concerns mechanism observability, A-13 concerns falsification testability. But they are not independent at the condition level: if a mechanism hop is Opaque AND the falsification condition it explains has Unknown testability, the analyst has no path to resolving whether that part of the mechanism works. The joint diagnostic surfaces this co-occurrence. The section ordering (Diagnostic Yield before Adversarial) is intentional: the adversarial section uses the diagnostic findings to prioritize its challenges, rather than challenging hops uniformly.

```
You are running /discover-causal.
Your input is a feature hypothesis of the form "X causes Y."
Five sections (A through E), one subsection (D between C and E). Section A precedes all
mechanism work. Complete each section fully before advancing.
Every classification judgment uses a discrete label from a fixed set with a rationale line.

Testability lifecycle: all conditions start Unknown at genesis (Section A). Section B
refines testability after evidence. testability_refined_count and testability_residual_unknown_count
are computed in Section B and carried to Section D yield.

Chain observability aggregate: hop observability labels from Section C are carried to
Section D yield and aggregated into the chain pattern label.

Diagnostic Yield (Section D): positioned between mechanism (Section C) and adversarial
challenge (Section E). Computes both diagnostics in parallel. Produces joint gap analysis.
Adversarial challenge (Section E) uses Section D findings to prioritize.

---

## SECTION A: INTAKE

[Three sub-tasks. All must complete before mechanism begins.]

### A1: Claim and initial falsification

X (the cause): [Extract from input]
Y (the claimed outcome): [Extract from input]
Full claim: ["X causes Y" -- one sentence]

Initial falsification conditions:
[Confidence assigned at generation. Testability = Unknown for all. Rationale covers
the mechanism failure exposed, not testability or confidence justification.]

| ID | Falsification condition (claim false if observed) | Testability | Confidence | Rationale |
|----|---------------------------------------------------|-------------|------------|-----------|
| F-01 | [What would break X->Y?] | Unknown | [ ] High  [ ] Medium  [ ] Low | [1 sentence] |
| F-02 | [Add as many as the claim generates.] | Unknown | [ ] High  [ ] Medium  [ ] Low | [1 sentence] |

### A2: Prior evidence

[At least one context-specific observation, OR "None found." Evidence may revise confidence.
Testability refinement is deferred to Section B (evidence refines testability, not genesis).]

Evidence entry 1:
  Source type: [ ] Prior result  [ ] Analogous case  [ ] Domain observation  [ ] Counter-evidence
  Observation: [What was seen, where, when?]
  Bearing on X->Y: [1 sentence]

[Add entries as needed.]

Evidence quality: [ ] Strong  [ ] Moderate  [ ] Weak  [ ] None
Evidence quality rationale: [1 sentence]

### A3: Inertia check

Status-quo description: [What happens today without X?]
Baseline rate: [Estimate or bound. Or: "Unknown."]

Inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP
Inertia rationale: [1 sentence]

| ID | Inertia falsification condition | Testability | Confidence | Rationale |
|----|---------------------------------|-------------|------------|-----------|
| I-01 | Y occurs at [baseline rate] without X | Unknown | [ ] High  [ ] Medium  [ ] Low | [1 sentence] |

SECTION A GATE:
[ ] At least two F-NN conditions with IDs, testability (Unknown), confidence, and rationale
[ ] Evidence populated (or explicit "None found" -- not skipped)
[ ] Evidence quality label assigned with rationale
[ ] Inertia severity label assigned with rationale

--- Do not advance to Section B until all items are checked. ---
--- IF STOP: skip Sections B and C; advance to Section D (complete testability yield only). ---

---

## SECTION B: TESTABILITY REFINEMENT

[Dedicated section for testability refinement. After Section A evidence, revisit every
F-NN and I-NN condition. Determine whether evidence enables a testability assessment.
This section exists independently of mechanism work -- testability is a property of
the falsification condition relative to available resources, not of the mechanism.]

Testability refinement pass:

| ID | Testability after evidence | Refinement rationale |
|----|---------------------------|---------------------|
| F-01 | [ ] Easy  [ ] Hard  [ ] Unknown | [What evidence enabled or blocked the determination?] |
| F-02 | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence] |
| I-01 | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence] |
[Mirror all F-NN and I-NN conditions from Section A.]

Testability refinement yield:
  testability_refined_count: [Conditions that moved Unknown -> Easy or Hard]
  testability_residual_unknown_count: [Conditions still Unknown after evidence]
  Residual Unknown IDs: [List, or "None"]
  [Carry both counts and IDs to Section D Diagnostic Yield.]

SECTION B GATE:
[ ] Testability refinement pass completed for all F-NN and I-NN conditions
[ ] testability_refined_count and testability_residual_unknown_count declared
[ ] Residual Unknown IDs listed (or confirmed empty)

--- Do not advance to Section C until all items are checked. ---

---

## SECTION C: MECHANISM CHAIN

[Map the causal pathway from X to Y. Two hops minimum. Every hop carries observability
label + rationale + evidence coherence + falsification connection. Do NOT compute the
chain observability aggregate here -- that is Section D's job. State hop-level labels only.
State mechanism only -- adversarial content belongs in Section E.]

Hop 1: X [name] -> [intermediate A]: [How does X produce A?]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Observability rationale: [1 sentence: how directly can this intermediate be detected?]
  Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
  Falsification connection: [F-NN or I-NN ID from Section A. One sentence: if this hop
    fails, this condition holds.]

Hop 2: [intermediate A] -> Y [name]: [How does A produce Y?]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Observability rationale: [1 sentence]
  Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
  Falsification connection: [F-NN or I-NN ID. One sentence.]

[Add Hop 3+ as needed. Every hop: observability label + rationale, evidence coherence,
falsification connection to a pre-existing condition from Section A.]

Mechanism strength (preliminary): [ ] Strong  [ ] Moderate  [ ] Weak
  (Before Section D diagnostic yield and Section E adversarial challenge.)
Preliminary rationale: [1 sentence. Based on observability ratings and evidence coherence.]

SECTION C GATE:
[ ] At least two hops filled
[ ] Every hop has observability label (Observable/Partial/Opaque) and rationale
[ ] Every hop has a falsification connection naming a pre-existing F-NN or I-NN
[ ] Mechanism strength (preliminary) assigned with rationale
[ ] Chain observability aggregate NOT computed in this section (Section D computes it)
[ ] No adversarial content in this section

--- Do not advance to Section D until all items are checked. ---

---

## SECTION D: DIAGNOSTIC YIELD

[Positioned between mechanism (Section C) and adversarial challenge (Section E).
Compute both diagnostics in parallel. Produce joint gap analysis. Section E uses
Section D findings to prioritize challenges -- priority targets are listed at the end.]

### D1: Testability Refinement Yield Summary

[Carry forward from Section B.]

| ID | Initial testability | Final testability (after Section B) | Status |
|----|--------------------|------------------------------------|--------|
| F-01 | Unknown | [Easy/Hard/Unknown] | [ ] Refined  [ ] Residual Unknown |
| F-02 | Unknown | [Easy/Hard/Unknown] | [ ] Refined  [ ] Residual Unknown |
| I-01 | Unknown | [Easy/Hard/Unknown] | [ ] Refined  [ ] Residual Unknown |
[Mirror all conditions. Status = Refined if Unknown -> Easy/Hard; Residual Unknown otherwise.]

testability_refined_count: [From Section B]
testability_residual_unknown_count: [From Section B]
Testability yield assessment: [ ] High  [ ] Medium  [ ] Low
  (High = most conditions refined; Medium = some; Low = few or none)
Yield assessment rationale: [1 sentence: does evidence quality explain the yield rate?]
AMEND Testability triggered: [ ] Yes (residual_unknown_count > 0)  [ ] No

### D2: Chain Observability Aggregate

[Carry forward hop observability labels from Section C. Compute tally and pattern label.]

| Hop | Mechanism step | Observability | Rationale | Falsification connection |
|-----|---------------|---------------|-----------|--------------------------|
| Hop 1 | X -> [intermediate A] | [Observable/Partial/Opaque] | [from Section C] | [F-NN or I-NN ID] |
| Hop 2 | [A] -> Y | [Observable/Partial/Opaque] | [from Section C] | [F-NN or I-NN ID] |
[Mirror all Section C hops.]

Chain observability tally:
  Observable: [Count]   Partial: [Count]   Opaque: [Count]   Total: [Count]
Chain observability pattern: [ ] AllObservable  [ ] Mixed  [ ] PredominantlyOpaque
Pattern rationale: [1 sentence]
AMEND Observability triggered: [ ] Yes (Mixed or PredominantlyOpaque)  [ ] No

### D3: Joint Gap Analysis

[For each condition that is a Residual Unknown testability, identify whether its mechanism
hop is also Opaque. If a condition is both Residual Unknown testability AND its hop is
Opaque, flag it as a double-blind gap: cannot observe the hop AND cannot test the condition.]

| Condition ID | Testability status | Mechanism hop | Hop observability | Joint gap? |
|--------------|-------------------|---------------|------------------|------------|
| F-01 | [Refined/Residual Unknown] | Hop [N] | [Observable/Partial/Opaque] | [ ] Yes (double-blind)  [ ] No |
| I-01 | [Refined/Residual Unknown] | Hop [N] | [Observable/Partial/Opaque] | [ ] Yes (double-blind)  [ ] No |
[Mirror all conditions. Joint gap = Yes if testability = Residual Unknown AND hop observability = Opaque.]

Double-blind gap count: [Count of Yes joint gaps]
Double-blind gap IDs: [List, or "None"]
Joint gap assessment: [1 sentence: what do double-blind gaps mean for the claim's testability?]
[If any double-blind gaps: note in AMEND that these are priority resolution items.]

### D4: Section E Priority Targets

[Based on D1-D3 findings, list which conditions and hops Section E adversarial challenge
should prioritize. Priority targets are those where the adversarial challenge is most likely
to surface a falsification path despite observability and testability constraints.]

Section E priority targets:
  Priority conditions (from D1 Residual Unknowns or D3 double-blind gaps): [List IDs]
  Priority hops (from D2 Opaque hops): [List hop numbers]
  Priority rationale: [1-2 sentences: why these?]

SECTION D GATE:
[ ] D1 yield table complete with Refined/Residual Unknown status for every condition
[ ] testability_refined_count and testability_residual_unknown_count confirmed
[ ] D2 observability table complete with all hops from Section C
[ ] Chain observability pattern label declared with rationale
[ ] D3 joint gap table complete for all conditions
[ ] Double-blind gap count declared
[ ] Section E priority targets listed
[ ] AMEND Testability trigger evaluated
[ ] AMEND Observability trigger evaluated

--- Do not advance to Section E until all items are checked. ---

---

## SECTION E: ADVERSARIAL CHALLENGE

[Structurally separate from Section C. Use Section D priority targets to direct challenge
effort: D3 double-blind gaps and D2 Opaque hops are priority targets. Challenge every hop
but give proportional depth to priority targets. Name alternatives. Confounders.]

Hop 1 challenge: [Priority: Yes/No per Section D]
  What breaks X -> [intermediate A]? [Observable condition]
  Observable test: [What to measure or detect -- note if Opaque per D2]
  Alternative at this hop: [What else produces [intermediate A] without X?]
  Falsification confidence: [ ] High  [ ] Medium  [ ] Low
  Confidence rationale: [1 sentence. If condition is Residual Unknown testability from D1:
    explain why confidence is warranted despite testability constraint, or assign Low.]

Hop 2 challenge: [Priority: Yes/No per Section D]
  What breaks [intermediate A] -> Y? [Observable condition]
  Observable test: [What to measure or detect]
  Alternative at this hop: [What else produces Y without [intermediate A]?]
  Falsification confidence: [ ] High  [ ] Medium  [ ] Low
  Confidence rationale: [1 sentence]

[Mirror all Section C hops. Note priority designation for each.]

Confounders:
  Confounder 1: [Variable correlating with both X and Y. Name and describe.]

Inertia challenge:
  Adversarial view: [Does mechanism analysis change the inertia verdict?]
  Revised verdict: [ ] Confirms  [ ] Upgrades to ADVISORY  [ ] Upgrades to STOP

Mechanism strength (final): [ ] Strong  [ ] Moderate  [ ] Weak  [ ] NA (STOP)
Final strength rationale: [1 sentence. State whether changed from preliminary and why.]

---

## SECTION F: SCOPE AND AMEND

Scoped claim: ["X causes Y when [condition], for [population], assuming [precondition]."]
Scope condition: [Reference Section E findings and Section D chain pattern.]
Out-of-scope: [At least one condition from Section E where mechanism fails]

Final inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP
Final inertia rationale: [1 sentence]

AMEND DIRECTIVE:
[Mandatory slots from Section D triggers. Address all triggered slots plus Narrow and Falsification.]

AMEND: discover-causal
  Narrow: [Scope tightening]
  Mechanism: [Hop notation: X -> [A] -> Y]
  Falsification: [HIGH confidence condition from Section E. Name, ID, testability from D1.]
  Evidence: [If None: "Mechanism is theoretical. Cite one context-specific observation."]
  [Inertia: (mandatory if STOP/ADVISORY) "Y occurs at [baseline] without X.
   Demonstrate incremental Y above baseline."]
  [Observability: (mandatory if D2 triggered) "Chain pattern: [label]. Opaque hops: [list].
   Identify proxy measurements or narrow to observable mechanism portion."]
  [Testability: (mandatory if D1 triggered) "Conditions [IDs] have Unknown testability.
   Determine instrumentation. Double-blind gaps [IDs if any]: these require both observability
   proxy AND testability resolution."]

---

Write artifact: simulations/discover/causal/{topic}-causal-{date}.md
Frontmatter: skill, topic, date, cause (X), outcome (Y),
             dual_diagnostic_yield_section (true), gate_checklists (4),
             inertia_verdict (SAFE/ADVISORY/STOP), baseline_rate,
             evidence_count, evidence_quality (Strong/Moderate/Weak/None),
             initial_falsification_count, inertia_falsification_count,
             hop_count, mechanism_strength_preliminary (Strong/Moderate/Weak/NA),
             mechanism_strength_final (Strong/Moderate/Weak/NA),
             strength_changed (true/false),
             mechanism_hop_falsification_links (true),
             hop_observability_labels (true),
             chain_observability_pattern (AllObservable/Mixed/PredominantlyOpaque),
             observability_amend_triggered (true/false),
             testability_refined_count,
             testability_residual_unknown_count,
             testability_amend_triggered (true/false),
             double_blind_gap_count,
             double_blind_gap_ids (list),
             testability_yield_assessment (High/Medium/Low),
             falsification_testability_list (Easy/Hard/Unknown per condition after Sec B),
             falsification_confidence_list (High/Medium/Low per condition),
             confounder_named (true/false).
```

---

## Round 6 Design Notes

### v6 aspirational criterion coverage

| V | A-01 | A-02 | A-03 | A-04 | A-05 | A-06 | A-07 | A-08 | A-09 | A-10 | A-11 | A-12 | A-13 |
|---|------|------|------|------|------|------|------|------|------|------|------|------|------|
| V-01 | YES S4 prelim/S5 final | YES S3 baseline | YES S5 adversarial | YES all fields | YES S2 before S4 | YES prelim S4/final S5 | YES S1 confidence per row | YES S4 hop connection | YES S1/S2/S4 gates (3) | YES S4 all hops | YES S1 Unknown + S2 refined | YES S4 inline tally + pattern + conditional gate item | YES S2 refined_count + residual_count + residual IDs |
| V-02 | YES ANALYST prelim/SKEPTIC final | YES FRAMER baseline | YES SKEPTIC role | YES all fields | YES FRAMER before ANALYST | YES ANALYST prelim/SKEPTIC final | YES SKEPTIC final table per row | YES ANALYST hop FRAMER connection | YES 3 role gates | YES ANALYST all hops | YES FRAMER testability-only column | YES AUDITOR D1 tally + pattern + routing row 1 | YES FRAMER refined_count + residual_count; AUDITOR D2 yield summary |
| V-03 | YES S4 prelim/S5 final | YES S2 baseline | YES S5 adversarial | YES all fields | YES S3 before S4 | YES prelim S4/final S5 | YES S1+S2 confidence per row | YES S4 hop either pool | YES S1/S2/S3/S4 gates (4) | YES S4 all hops + S2 inertia observability | YES S1+S2 Unknown + S3 refined both pools | YES S4 combined tally (hops + inertia) + pattern + gate item | YES S3 refined_count + residual_count pool breakdown |
| V-04 | YES S4 prelim/S5 final | YES S2 baseline | YES S5 adversarial | YES all fields | YES S3 before S4 | YES prelim S4/final S5 | YES S1 confidence per row | YES S4 hop connection | YES S3/S4 gates (2) | YES S4 all hops | YES S1 Unknown + S3 refined | YES S4 tally + pattern; S7 routing matrix row 1 | YES S3 refined_count + residual_count; S7 routing matrix row 2 |
| V-05 | YES Sec C prelim/Sec E final | YES A3 baseline | YES Sec E adversarial | YES all fields | YES Sec A+B before Sec C | YES prelim C/final E | YES A1 confidence per row | YES Sec C hop connection | YES A-gate/B-gate/C-gate/D-gate (4) | YES Sec C all hops | YES A1 Unknown + Sec B refined | YES D2 tally + pattern + AMEND Observability trigger; D3 joint gap surfaced | YES D1 yield table + refined_count + residual_count; D3 double-blind gap adds joint diagnostic |

### Predicted composite scores under v6 rubric

| V | Ess (est) | Rec (est) | Asp (est, v6/13) | Composite (est) | Golden (est) |
|---|-----------|-----------|-----------------|-----------------|--------------|
| V-01 | 5/5 | 3/3 | 13/13 | 100.0 | YES |
| V-02 | 5/5 | 3/3 | 13/13 | 100.0 | YES |
| V-03 | 5/5 | 3/3 | 13/13 | 100.0 | YES |
| V-04 | 5/5 | 3/3 | 13/13 | 100.0 | YES |
| V-05 | 5/5 | 3/3 | 13/13 | 100.0 | YES |

### A-12 implementation comparison

| V | A-12 implementation | Section | Form |
|---|--------------------|---------|----|
| V-01 | Inline tally + pattern label after all hops | Section 4 end | 4-count field + pattern label + gate item |
| V-02 | AUDITOR D1 table + tally + pattern | AUDITOR section | Standalone table per hop |
| V-03 | Combined tally including inertia observability | Section 4 end | 4-count field with inertia contribution noted |
| V-04 | Inline tally + routing matrix row 1 | Section 4 end + Section 7 | Tally inline; routing matrix is the gate |
| V-05 | D2 observability table + tally + pattern | Section D | Standalone table per hop; feeds D3 joint gap |

### A-13 implementation comparison

| V | A-13 implementation | Section | Unique |
|---|--------------------|---------|----|
| V-01 | Unknown at genesis; refined in S2; yield in S2 | Section 2 | Yield field in evidence section |
| V-02 | FRAMER yield in opening; AUDITOR D2 summary | FRAMER + AUDITOR | Yield computed by FRAMER, summarized by AUDITOR |
| V-03 | Both pools refined; pool breakdown in yield | Section 3 | Inn vs F-NN residual Unknown asymmetry tracked |
| V-04 | Unknown at genesis; refined in S3; routing matrix row 2 | Section 3 + Section 7 | Routing matrix makes yield trigger mechanical |
| V-05 | Dedicated Section B for refinement; D1 yield table | Section B + Section D | Yield as its own section; D1 is first-class table |

### New finding type: double-blind gap (V-05 only)

V-05 introduces the first joint diagnostic across A-12 and A-13: a condition that is both a Residual Unknown testability (A-13 residual) AND whose mechanism hop is Opaque (A-12 per-hop). This is a double-blind gap — the analyst cannot observe the mechanism step AND does not know how to run the test for the falsification condition. Neither A-12 nor A-13 individually requires identifying this co-occurrence.

Research question for R7: Do double-blind gaps appear in practice? Is the double-blind gap count predictable from chain observability pattern and testability yield rate?

### Open research questions for R7

1. **Inline tally vs. summary table (V-01 vs R5-V-04)**: Does the inline tally in V-01 produce the same AMEND routing accuracy as the standalone summary table in R5-V-04? Does the absence of a dedicated table reduce the visibility of chain-level patterns in live runs?

2. **AUDITOR role synthesis quality (V-02)**: Does AUDITOR's post-hoc aggregation produce diagnostic rationale that is richer than inline computation? Does AUDITOR's access to both FRAMER and ANALYST outputs simultaneously enable cross-role findings that single-role computation misses?

3. **Inertia observability in chain aggregate (V-03)**: Does including inertia observability in the chain aggregate change the pattern label (AllObservable → Mixed) in practice? Do I-NN conditions earn more Opaque observability labels than F-NN conditions?

4. **Routing matrix trigger accuracy (V-04)**: Does the explicit routing matrix surface more AMEND slots than prose-conditional AMEND? Does it produce spurious triggers (false positives from mechanical evaluation)?

5. **Double-blind gap prevalence (V-05)**: What fraction of runs produce at least one double-blind gap? Is the double-blind gap count correlated with evidence quality (fewer double-blind gaps when evidence is Strong)?

```json
{"round": 6, "rubric_version": "v6", "target_score": 100.0, "all_essential_pass_predicted": true,
 "new_criteria": ["A-12: aggregate chain observability label (AllObservable/Mixed/PredominantlyOpaque) with conditional AMEND routing",
                  "A-13: testability_refined_count + testability_residual_unknown_count tracked as structured findings; residual Unknowns route to mandatory AMEND Testability slot"],
 "variation_axes": {
   "V-01": "inline chain observability tally -- aggregate without dedicated summary table",
   "V-02": "AUDITOR role -- fourth role owns both aggregate diagnostics post-analysis",
   "V-03": "inertia-inclusive aggregates -- I-NN participates in both A-12 and A-13",
   "V-04": "AMEND routing matrix -- formal decision table generates AMEND slots mechanically",
   "V-05": "dual-diagnostic yield section -- parallel A-12+A-13 computation with joint gap analysis"
 },
 "new_finding_type": "double-blind gap (V-05): condition where hop is Opaque AND testability is Unknown -- neither A-12 nor A-13 surfaces this individually",
 "r7_questions": [
   "inline-vs-table: does V-01 inline tally produce same AMEND routing accuracy as R5-V-04 summary table?",
   "auditor-synthesis: does V-02 AUDITOR produce richer diagnostic rationale than inline computation?",
   "inertia-observability: does V-03 inertia in aggregate shift chain pattern toward Mixed/PredominantlyOpaque?",
   "matrix-accuracy: does V-04 routing matrix over- or under-fire relative to prose-conditional AMEND?",
   "double-blind-gap-prevalence: what fraction of V-05 runs produce at least one double-blind gap?"
 ]}
```
