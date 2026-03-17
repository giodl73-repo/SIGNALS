Written. Here's the R5 design summary:

---

## Round 5 — 5 Variations

**R5 agenda**: v5 adds A-10 (hop observability) and A-11 (falsification testability distinct from confidence). All R4 variations remain golden under v5. R4-V-01 retroactively scores 100.0. R5 target: all 5 score 100.0 under v5 (11/11 aspirational).

| V | Axis | New mechanism |
|---|------|---------------|
| **V-01** | Output format — dual-column F-NN | Testability + confidence co-labeled at genesis in every condition table, including final table |
| **V-02** | Role sequence — dimension ownership | FRAMER owns testability, SKEPTIC owns confidence; gate explicitly prohibits cross-labeling |
| **V-03** | Inertia framing — two-pool dual-dimension | Both F-NN and I-NN pools carry testability + confidence; research question: do inertia conditions earn more Hard/Unknown testability? |
| **V-04** | Output format — observability summary table | Hop observability extracted into a standalone sub-table alongside the bidirectionality table; Opaque chains trigger mandatory AMEND slot |
| **V-05** | Lifecycle emphasis — testability refinement | All conditions start Unknown at genesis; evidence refines; residual Unknowns are findings, not skips |

**Key design decisions:**
- V-01 and V-03 are the clearest A-11 satisfiers (both columns side by side from genesis)
- V-02 is the strongest architectural enforcement (different role = different time = different rationale)
- V-04 extends the V-04 bidirectionality pattern to observability — a genuinely new coverage diagnostic
- V-05 is the most intellectually honest — Unknown is a legitimate state that evidence must resolve

**Key R6 questions seeded:**
- Does genesis assignment (V-01) produce more Easy ratings than refinement (V-05)?
- Does V-02 role ownership produce semantically distinct rationale text for testability vs. confidence?
- Do I-NN conditions (V-03) earn more Hard/Unknown testability than F-NN conditions?
- Does V-04's observability summary table reliably trigger AMEND for Opaque chains?
- What fraction of Unknown conditions in V-05 remain Unknown after evidence?
e detection of Opaque hops, which inline fields obscure |
| **V-05** | Lifecycle emphasis — testability refinement (Unknown at genesis → determinate via evidence) | Staging testability as Unknown then refining through evidence creates an observable before/after signal; residual Unknown labels are a finding about what this context cannot test |

**Key R6 questions seeded:**
- Does dual-column genesis (V-01) produce different testability distributions than refinement lifecycle (V-05)? Are there more Hard ratings when testability is assigned without evidence context?
- Does role ownership (V-02) reduce confidence/testability conflation in live runs? Do live artifacts show distinct rationale lines for each dimension?
- Do I-NN conditions (V-03) earn more Hard testability ratings than F-NN conditions — and does the two-pool design surface this asymmetry?
- Does the observability summary table (V-04) reveal Opaque hops that inline fields would leave implicit?
- Does testability refinement via evidence (V-05) produce an observable shift (conditions that move from Unknown to Easy/Hard) and does that shift correlate with evidence quality?

---

## V-01: Dual-Column F-NN (Testability + Confidence Co-Labeled at Genesis)

**Axis:** Output format — every falsification condition carries both `Testability` (Easy/Hard/Unknown) and `Confidence` (High/Medium/Low) as separate columns from the moment it is first generated. Both columns appear in the initial F-NN table (Section 1), in the I-01 inertia row (Section 3), and in the final prioritized table (Section 5). The two-column structure at genesis is the strongest signal for A-11 independence.

**Hypothesis:** Assigning both dimensions at generation time — before evidence and before mechanism — eliminates any ambiguity about whether testability derives from confidence or vice versa. Evidence may update either dimension but cannot be cited as the source of the distinction. This design produces the clearest artifact evidence for A-04 (all classification outputs use discrete labels) and A-11 simultaneously.

```
You are running /discover-causal.
Your input is a feature hypothesis of the form "X causes Y."
This skill is organized around falsification. Sections run in this order:
  1. Claim intake and initial falsification hypothesis (before mechanism work)
  2. Evidence (refines falsification conditions)
  3. Inertia check (status-quo as falsifier)
  4. Mechanism chain (maps hops to pre-existing falsification conditions)
  5. Adversarial extension (challenges mechanism, finalizes falsification table)
  6. Claim scope and AMEND

Every falsification condition carries two independent classification dimensions from the
moment it is generated:
  Testability (Easy/Hard/Unknown): can we run this test given available resources?
  Confidence (High/Medium/Low): how likely is this condition to actually falsify the mechanism?
Both columns appear in every table containing falsification conditions.

Every mechanism hop carries three per-hop fields: observability label (Observable/Partial/Opaque),
falsification cross-reference (A-08), and evidence coherence. Gate checklists close Sections 1-4.

---

## SECTION 1: CLAIM AND INITIAL FALSIFICATION HYPOTHESIS

Claim extraction:
  X (the cause): [Extract from input]
  Y (the claimed outcome): [Extract from input]
  Full claim: ["X causes Y" -- one sentence]

Initial falsification hypothesis:
[Before any evidence or mechanism work, list the conditions that, if observed, would prove
the claim false. Think from the claim alone. Assign IDs F-01, F-02, ...
Assign BOTH testability and confidence at generation time. Rationale covers the combined
judgment. These conditions will be cross-referenced by mechanism hops in Section 4.]

| ID | Initial falsification condition (claim false if observed) | Testability | Confidence | Rationale |
|----|-----------------------------------------------------------|-------------|------------|-----------|
| F-01 | [What would break X->Y?] | [ ] Easy  [ ] Hard  [ ] Unknown | [ ] High  [ ] Medium  [ ] Low | [1 sentence] |
| F-02 | [Add as many as the claim generates.] | [ ] Easy  [ ] Hard  [ ] Unknown | [ ] High  [ ] Medium  [ ] Low | [1 sentence] |

[These are preliminary -- testability and confidence may be revised in Sections 2-3. Record
any revision by noting the F-NN ID and which dimension changed and why.]

SECTION 1 GATE:
[ ] X and Y extracted separately
[ ] At least two initial falsification conditions listed with F-NN IDs
[ ] Both testability AND confidence columns filled for every row
[ ] Rationale provided for every row

--- Do not advance to Section 2 until all Section 1 gate items are checked. ---

---

## SECTION 2: EVIDENCE

[Establish what is known in this specific context. Generic citations fail. At least one
context-specific observation required, OR "None found" with mandatory AMEND evidence slot.
Evidence may revise testability (e.g., Unknown -> Easy) or confidence for any F-NN condition.
Document revisions explicitly by F-NN ID.]

Evidence entry 1:
  Source type: [ ] Prior result  [ ] Analogous case  [ ] Domain observation  [ ] Counter-evidence
  Observation: [What was seen, where, when?]
  Bearing on X->Y: [1 sentence: supports, complicates, or challenges the claim?]
  Revisions: [Any F-NN ID and which dimension changes (testability or confidence) and why.
    If none: "No revisions."]

[Add entries as needed.]

Evidence quality: [ ] Strong  [ ] Moderate  [ ] Weak  [ ] None
Evidence quality rationale: [1 sentence]

[If None: flag Evidence slot in AMEND as mandatory.]

SECTION 2 GATE:
[ ] At least one evidence entry populated (or explicit "None found" -- not skipped)
[ ] Evidence quality label assigned with rationale
[ ] Revisions field completed for every entry

--- Do not advance to Section 3 until all Section 2 gate items are checked. ---

---

## SECTION 3: INERTIA CHECK

[The null hypothesis -- doing nothing -- is itself a falsifier: if the status quo already
produces Y, the claim "X causes Y" is false or trivial.]

Status-quo description: [What happens today without X?]
Baseline rate: [Estimate or bound: "Y occurs approximately __% without X." Or: "Unknown."]

Inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP
  (SAFE = doing nothing does not produce Y;
   ADVISORY = partially produces Y for some users or conditions;
   STOP = status quo plausibly already produces Y at a meaningful rate)
Inertia rationale: [1 sentence]

Inertia as falsifier:
| ID | Inertia falsification condition | Testability | Confidence | Rationale |
|----|---------------------------------|-------------|------------|-----------|
| I-01 | Y occurs at [baseline rate] without X | [ ] Easy  [ ] Hard  [ ] Unknown | [ ] High  [ ] Medium  [ ] Low | [1 sentence] |

SECTION 3 GATE:
[ ] Status-quo description written
[ ] Baseline rate estimated or explicitly marked "Unknown"
[ ] Inertia severity label assigned with rationale
[ ] I-01 row filled with both testability AND confidence columns and rationale

--- Do not advance to Section 4 until all Section 3 gate items are checked. ---
--- IF STOP: skip Section 4; advance directly to Section 5. ---

---

## SECTION 4: MECHANISM CHAIN

[Map the causal pathway from X to Y. Two hops minimum. Cohere with Section 2 evidence.
Note evidence tensions explicitly. State mechanism only -- adversarial content belongs in
Section 5.

Every hop carries three required per-hop fields:
  Observability (Observable/Partial/Opaque): can we directly detect this intermediate state?
  Falsification connection: which F-NN or I-NN from Sections 1-3 does this hop explain?
    If no existing condition covers the hop, add a new F-NN to Section 1 first, then reference.
  Evidence coherence: does Section 2 evidence support, contradict, or is it neutral?]

Hop 1: X [name] -> [intermediate A]: [How does X produce A?]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Observability rationale: [1 sentence: how directly can this intermediate state be measured?]
  Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe briefly
  Falsification connection: [Which F-NN or I-NN from Sections 1-3 does this hop explain or
    refine? Write the condition ID and one sentence: if this hop fails, this condition holds.]

Hop 2: [intermediate A] -> Y [name]: [How does A produce Y?]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Observability rationale: [1 sentence]
  Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe briefly
  Falsification connection: [Which F-NN or I-NN does this hop explain or refine?
    Write the condition ID and one sentence.]

[Add Hop 3+ as needed. Every hop requires: observability label + rationale, evidence coherence,
and falsification connection to a pre-existing F-NN or I-NN.]

Mechanism strength (preliminary): [ ] Strong  [ ] Moderate  [ ] Weak
  (Before adversarial extension. Based on observability ratings and evidence coherence.)
Preliminary rationale: [1 sentence]

SECTION 4 GATE:
[ ] At least two hops filled
[ ] Every hop has observability label (Observable/Partial/Opaque) and rationale
[ ] Every hop has a falsification connection naming a pre-existing F-NN or I-NN
[ ] Mechanism strength (preliminary) assigned with rationale
[ ] No adversarial content written in this section

--- Do not advance to Section 5 until all Section 4 gate items are checked. ---

---

## SECTION 5: ADVERSARIAL EXTENSION

[Structurally separate from Section 4. Challenges the mechanism hop by hop, extends and
finalizes falsification conditions. Final table carries both testability and confidence
columns for every condition.]

Hop-by-hop challenge:

Hop 1:
  What breaks X -> [intermediate A]? [Observable condition that disproves this hop]
  Observable test: [What to measure or detect]
  Alternative: [What else produces [intermediate A] without X?]
  Confidence: [ ] High  [ ] Medium  [ ] Low
    (High = measurable next sprint; Medium = measurable with setup; Low = long-horizon only)
  Confidence rationale: [1 sentence]

Hop 2:
  What breaks [intermediate A] -> Y? [Observable condition]
  Observable test: [What to measure or detect]
  Alternative: [What else produces Y without [intermediate A]?]
  Confidence: [ ] High  [ ] Medium  [ ] Low
  Confidence rationale: [1 sentence]

[Mirror all Section 4 hops. Every hop requires confidence label and rationale.]

Confounders:
  Confounder 1: [Variable correlating with both X and Y, creating appearance of causation.
    Name and explain why it correlates with both.]

Inertia challenge:
  Adversarial inertia view: [Does analysis reveal Y could be largely explained by baseline
    effects rather than X->Y?]
  Revised inertia verdict: SAFE / ADVISORY / STOP / No change -- confirm

Final prioritized falsification table:
[Consolidate all conditions from Sections 1, 3, and 5. Sort High confidence -> Medium -> Low.
Both testability AND confidence columns required for every row. Carry forward testability
labels from generation; update only if evidence in Section 2 revised them.]

| ID | Falsification condition | Source | Testability | Confidence | Rationale |
|----|------------------------|--------|-------------|------------|-----------|
| F-01 | [Condition] | [ ] Initial  [ ] Inertia  [ ] Hop challenge  [ ] New | [ ] Easy  [ ] Hard  [ ] Unknown | [ ] High  [ ] Medium  [ ] Low | [1 sentence] |
[Add all conditions. Sort by confidence descending.]

Mechanism strength (final): [ ] Strong  [ ] Moderate  [ ] Weak  [ ] NA (STOP)
  (Update from preliminary if adversarial extension changed the rating.)
Final strength rationale: [1 sentence. State whether changed from preliminary and why.]

Inertia severity (confirmed): [ ] SAFE  [ ] ADVISORY  [ ] STOP

---

## SECTION 6: CLAIM SCOPE AND AMEND

Scoped claim: ["X causes Y when [condition], for [population], assuming [precondition]."]
Scope condition: [What must be true for the mechanism to hold against the top High-confidence
  falsification conditions from the final table?]
Out-of-scope: [At least one context from the final table where the mechanism fails]

AMEND DIRECTIVE:
[Address at least two of the four slots. Mandatory:
  - Evidence slot if Section 2 found no evidence
  - Inertia slot if confirmed inertia severity is STOP or ADVISORY]

AMEND: discover-causal
  Narrow: [Scope tightening -- reference scope condition above]
  Mechanism: [Hop notation: X -> [A] -> Y]
  Falsification: [Which HIGH confidence condition from the final table should be added to
    the hypothesis statement? Name it, its ID, and include both testability and confidence labels.]
  Evidence: [If none: "Mechanism is theoretical. Cite one context-specific observation."]
  [Inertia: (mandatory if STOP/ADVISORY) "Y already occurs at [baseline] without X.
   Reframe as incremental Y above baseline."]

---

Write artifact: simulations/discover/causal/{topic}-causal-{date}.md
Frontmatter: skill, topic, date, cause (X), outcome (Y),
             dual_column_falsification (true), gate_checklists (4),
             inertia_verdict (SAFE/ADVISORY/STOP), baseline_rate,
             evidence_count, evidence_quality (Strong/Moderate/Weak/None),
             hop_count, mechanism_strength_preliminary (Strong/Moderate/Weak/NA),
             mechanism_strength_final (Strong/Moderate/Weak/NA),
             strength_changed (true/false),
             mechanism_hop_falsification_links (true),
             hop_observability_labels (true),
             initial_falsification_count, final_falsification_count,
             falsification_testability_list (Easy/Hard/Unknown per condition sorted),
             falsification_confidence_list (High/Medium/Low per condition sorted),
             easy_testability_count, hard_testability_count, unknown_testability_count,
             high_confidence_count, medium_confidence_count, low_confidence_count,
             confounder_named (true/false).
```

---

## V-02: Role-Owned Dimensions (FRAMER=Testability, SKEPTIC=Confidence)

**Axis:** Role sequence — dimension ownership enforces A-11 separation structurally. FRAMER (opening) generates the falsification table with testability labels only — explicitly prohibited from assigning confidence. ANALYST maps mechanism with observability labels. SKEPTIC assigns confidence to every falsification condition during hop challenge and produces the final dual-dimension table. A gate item in FRAMER explicitly states: "Do not assign confidence — that is SKEPTIC's classification." Role separation makes temporal and dimensional independence architecturally guaranteed.

**Hypothesis:** When testability and confidence are owned by different roles at different times, no single-pass model run can conflate them. FRAMER assigns testability before seeing the mechanism; SKEPTIC assigns confidence after seeing the mechanism. This temporal separation should produce rationale lines that are genuinely distinct: testability rationale cites available instrumentation and access, while confidence rationale cites mechanism depth and adversarial exposure. Conflated rationales (same sentence for both) should be structurally impossible.

```
You are running /discover-causal.
Three roles execute in strict sequence. Each role owns distinct classification dimensions:
  FRAMER: Owns testability (Easy/Hard/Unknown). Does NOT assign confidence.
  ANALYST: Owns mechanism mapping with observability (Observable/Partial/Opaque).
            Does NOT assign testability or confidence to falsification conditions.
  SKEPTIC: Owns confidence (High/Medium/Low). Does NOT reassign testability.

Role sequence enforces A-11: testability and confidence are assigned by different roles at
different stages, making conflation architecturally impossible. A gate at each role boundary
enforces dimension ownership and prevents unauthorized cross-labeling.

Role definitions:
  FRAMER: Runs twice. Opening: claim intake, testability-labeled falsification table,
           evidence, inertia. Closing: scope + AMEND. Falsification table must exist with
           testability labels before ANALYST begins.
  ANALYST: Maps the causal mechanism using FRAMER evidence. Every hop carries observability
            label + rationale and a falsification cross-reference to a FRAMER F-NN condition.
            ANALYST does NOT label confidence -- that is SKEPTIC's job.
  SKEPTIC: Challenges mechanism hop by hop. Assigns confidence labels (High/Medium/Low) to
            every falsification condition. Produces the final dual-dimension table.
            SKEPTIC does NOT reassign testability -- that is FRAMER's classification.

Every classification judgment uses a discrete label from the fixed set shown, with rationale.

---

## FRAMER (OPENING): CLAIM INTAKE, TESTABILITY TABLE, EVIDENCE, INERTIA

[FRAMER's opening job: extract the claim, generate initial falsification conditions with
testability labels (NOT confidence -- that is SKEPTIC's job), then gather evidence and
establish the inertia baseline. FRAMER must complete this section before ANALYST begins.]

**Step 1: Claim extraction**
  X (the cause): [Extract from input]
  Y (the claimed outcome): [Extract from input]
  Full claim: ["X causes Y" -- one sentence]

**Step 2: Initial falsification hypothesis (testability-labeled)**
[From the claim alone -- before evidence or mechanism. What conditions, if observed, would
prove X->Y false? Assign IDs F-01, F-02, ...
TESTABILITY ONLY in this table. Do NOT assign confidence -- SKEPTIC assigns that after
seeing the mechanism. Testability rationale: cite instrumentation and access constraints.]

| ID | Initial falsification condition (claim false if observed) | Testability | Testability rationale |
|----|-----------------------------------------------------------|-------------|----------------------|
| F-01 | [What would break X->Y?] | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence: why this level?] |
| F-02 | [Add as many as the claim generates.] | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence] |

**Step 3: Prior evidence**
[At least one context-specific observation, OR "None found" with mandatory AMEND evidence
slot in FRAMER (CLOSING). Generic citations fail. Evidence may refine testability labels
(e.g., Unknown -> Easy if tooling confirmed). Document any revisions by F-NN ID.]

  Evidence entry 1:
    Source type: [ ] Prior result  [ ] Analogous case  [ ] Domain observation  [ ] Counter-evidence
    What was observed: [Specific: what happened, where, when?]
    Bearing on X->Y: [1 sentence: supports, complicates, or contradicts?]
    Testability revision: [Any F-NN ID with testability update, or "No revision."]

  [Add entries as needed.]

  Evidence quality: [ ] Strong  [ ] Moderate  [ ] Weak  [ ] None
  Evidence quality rationale: [1 sentence]

**Step 4: Status-quo baseline**
  What happens today without X? [One sentence]
  Baseline Y rate: [Estimate, bound, or "Unknown"]

  Inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP
    (SAFE = does not produce Y; ADVISORY = partially; STOP = already produces Y at meaningful rate)
  Inertia rationale: [1 sentence]

  Inertia as falsifier (testability only -- confidence added by SKEPTIC):
  | ID | Inertia falsification condition | Testability | Testability rationale |
  |----|---------------------------------|-------------|----------------------|
  | I-01 | Y occurs at [baseline rate] without X | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence] |

FRAMER (OPENING) GATE:
[ ] X and Y extracted separately
[ ] At least two initial falsification conditions with F-NN IDs and testability labels
[ ] Confidence column NOT present in this table (SKEPTIC owns confidence)
[ ] Evidence section populated (or explicit "None found" -- not skipped)
[ ] Evidence quality label assigned with rationale
[ ] Status-quo baseline and inertia severity written with rationale
[ ] I-01 row filled with testability label

--- IF STOP: ANALYST and SKEPTIC are skipped. Advance directly to FRAMER (CLOSING). ---
--- Do not advance to ANALYST until all FRAMER (OPENING) GATE items are checked. ---

---

## ANALYST: MECHANISM CHAIN

[ANALYST's job: map the causal pathway from X to Y using FRAMER's evidence. Every hop
carries observability label + rationale, evidence coherence, and falsification cross-reference
to a FRAMER F-NN or I-NN condition.
ANALYST does NOT assign confidence to falsification conditions -- that is SKEPTIC's job.
ANALYST states mechanism only -- adversarial challenges belong to SKEPTIC.]

Mechanism chain: [Two hops minimum.]

  Hop 1: X [name] -> [intermediate A]: [Describe the mechanism.]
    Observability: [ ] Observable  [ ] Partial  [ ] Opaque
    Observability rationale: [1 sentence: how directly can this intermediate be measured?]
    Evidence coherence: [ ] Supported by FRAMER evidence  [ ] Neutral  [ ] Tensions -- describe
    Falsification connection: [Which F-NN or I-NN from FRAMER's table does this hop explain?
      State the ID and one sentence: if this hop fails, this condition would be observed.]

  Hop 2: [intermediate A] -> Y [name]: [Describe the mechanism.]
    Observability: [ ] Observable  [ ] Partial  [ ] Opaque
    Observability rationale: [1 sentence]
    Evidence coherence: [ ] Supported by FRAMER evidence  [ ] Neutral  [ ] Tensions -- describe
    Falsification connection: [Which F-NN or I-NN does this hop explain? ID + one sentence.]

  [Add Hop 3+ as needed. Every hop: observability label + rationale, evidence coherence,
  falsification connection to a pre-existing FRAMER condition.]

Mechanism strength (preliminary): [ ] Strong  [ ] Moderate  [ ] Weak
  (ANALYST's assessment before SKEPTIC challenge. Based on observability ratings and
   evidence coherence. Explicitly preliminary -- SKEPTIC's confidence labeling may revise.)
Preliminary rationale: [1 sentence]

ANALYST GATE:
[ ] At least two hops filled
[ ] Every hop has observability label (Observable/Partial/Opaque) and rationale
[ ] Every hop has a falsification connection naming a pre-existing FRAMER F-NN or I-NN
[ ] Mechanism strength label (preliminary) assigned with rationale
[ ] No confidence labels assigned to falsification conditions in this section
[ ] No adversarial challenges written in this section

--- Do not advance to SKEPTIC until all ANALYST GATE items are checked. ---

---

## SKEPTIC: CHALLENGE AND CONFIDENCE LABELING

[SKEPTIC's job: challenge every mechanism hop, name what would break each step, name
alternatives and confounders, and assign confidence labels to all falsification conditions.
SKEPTIC is the sole classifier of confidence -- FRAMER owns testability, ANALYST owns
observability. SKEPTIC does NOT reassign testability labels.
SKEPTIC does NOT propose scope or AMEND -- that is FRAMER's job in closing.]

Hop-by-hop challenge:

  Hop 1 challenge:
    What breaks X -> [intermediate A]? [Observable condition that disproves this hop]
    Observable test: [Specific measurement or event]
    Alternative at this hop: [What else produces [intermediate A] without X?]
    Confidence: [ ] High  [ ] Medium  [ ] Low
      (High = testable next sprint; Medium = testable with setup; Low = long-horizon or proxy)
    Confidence rationale: [1 sentence: cite mechanism exposure and adversarial depth]

  Hop 2 challenge:
    What breaks [intermediate A] -> Y? [Observable condition]
    Observable test: [Specific measurement or event]
    Alternative at this hop: [What else produces Y without [intermediate A]?]
    Confidence: [ ] High  [ ] Medium  [ ] Low
    Confidence rationale: [1 sentence]

  [Mirror all ANALYST hops. Every hop requires confidence label and rationale.]

Inertia challenge:
  FRAMER's inertia verdict: [Repeat FRAMER's SAFE/ADVISORY/STOP]
  SKEPTIC review: Does the mechanism require X, or is Y attributable to baseline effects?
  SKEPTIC verdict: [ ] Confirms FRAMER  [ ] Upgrades to ADVISORY  [ ] Upgrades to STOP
  SKEPTIC rationale: [1 sentence]

Confounders:
  Confounder 1: [Variable correlating with both X and Y, mimicking causation. Name and describe.]

Final falsification table (FRAMER testability + SKEPTIC confidence):
[Consolidate all conditions. SKEPTIC adds confidence column. FRAMER's testability labels
carry forward read-only. Sort by confidence descending.]

| ID | Falsification condition | Source | Testability (FRAMER) | Confidence (SKEPTIC) | Rationale |
|----|------------------------|--------|----------------------|----------------------|-----------|
| F-01 | [Condition] | [ ] Initial  [ ] Inertia  [ ] Hop challenge  [ ] New | [FRAMER label] | [ ] High  [ ] Medium  [ ] Low | [1 sentence] |
[Add all conditions. Every row requires both columns populated.]

Mechanism strength (final): [ ] Strong  [ ] Moderate  [ ] Weak
  (SKEPTIC's assessment after challenge. State whether changed from ANALYST and why.)
Final strength rationale: [1 sentence. If changed: name the finding. If unchanged: confirm why.]

SKEPTIC GATE:
[ ] Every ANALYST hop has a challenge row with confidence label and rationale
[ ] At least one alternative cause named per hop
[ ] Inertia challenge verdict declared
[ ] At least one confounder named
[ ] Final falsification table populated with confidence labels for every row
[ ] Testability column carries FRAMER's labels unchanged (no SKEPTIC modifications)
[ ] Final mechanism strength label assigned with rationale

--- Do not advance to FRAMER (CLOSING) until all SKEPTIC GATE items are checked. ---

---

## FRAMER (CLOSING): SCOPE AND AMEND

[FRAMER returns using all prior outputs. FRAMER reads ANALYST's mechanism (with observability
labels and falsification cross-references) and SKEPTIC's final dual-dimension table. FRAMER
does not re-litigate findings.]

Scoped claim:
  Scope condition: [What must be true for X->Y to hold? Reference SKEPTIC's challenge findings.]
  Out-of-scope: [At least one condition from SKEPTIC where mechanism fails]
  Scoped claim text: ["X causes Y when [condition], for [population], assuming [precondition]."
    If STOP: "Claim is not supportable -- Y appears to occur at [baseline] without X."]

Final inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP
  (Confirm FRAMER's opening verdict, updated if SKEPTIC revised it.)
Final inertia rationale: [1 sentence]

AMEND DIRECTIVE:
[Address at least two of the four slots. Mandatory:
  - Evidence slot if FRAMER (opening) found no evidence
  - Inertia slot if final inertia severity is STOP or ADVISORY]

AMEND: discover-causal
  Narrow: [Scope tightening -- reference scoped claim above]
  Mechanism: [Hop notation: X -> [A] -> Y]
  Falsification: [Which HIGH confidence condition from SKEPTIC's final table should be added
    to the hypothesis? Name it, its ID, and include both FRAMER testability and SKEPTIC
    confidence labels.]
  Evidence: [If none: "No prior evidence found. Establish one context-specific observation
             before treating this claim as warranted."]
  [Inertia: (mandatory if STOP/ADVISORY) "Y occurs at [baseline] without X. Demonstrate
   incremental Y above baseline before mechanism analysis."]

---

Write artifact: simulations/discover/causal/{topic}-causal-{date}.md
Frontmatter: skill, topic, date, cause (X), outcome (Y),
             role_separation (testability=FRAMER/confidence=SKEPTIC/observability=ANALYST),
             evidence_count, evidence_quality (Strong/Moderate/Weak/None),
             inertia_verdict (SAFE/ADVISORY/STOP), baseline_rate,
             initial_falsification_count, final_falsification_count,
             hop_count, mechanism_strength_preliminary (Strong/Moderate/Weak),
             mechanism_strength_final (Strong/Moderate/Weak),
             strength_changed (true/false),
             mechanism_hop_falsification_links (true),
             hop_observability_labels (true),
             falsification_testability_list (Easy/Hard/Unknown per condition),
             falsification_confidence_list (High/Medium/Low per condition),
             confounder_named (true/false),
             gate_checklists (true), role_count (3).
```

---

## V-03: Two-Pool Dual-Dimension (A-11 Extended to I-NN)

**Axis:** Inertia framing — the inertia-first two-pool design (F-NN from claim, I-NN from inertia) extended to carry testability labels on both pools. Section 1 F-NN table: both testability and confidence. Section 2 I-NN table: both testability and confidence. Gate item confirms both pools have testability filled before mechanism begins. The research question: do inertia-derived conditions earn characteristically different testability ratings than claim-derived conditions?

**Hypothesis:** Inertia conditions are structurally different from claim-derived falsification conditions: I-NN conditions require observing the absence of an intervention (harder to isolate), often involve baseline measurement (may be Hard or Unknown depending on existing telemetry), and are frequently treated as theoretical rather than testable. Extending testability to I-NN systematically forces this question for each condition. If I-NN conditions earn more Hard or Unknown testability ratings than F-NN conditions, this is a finding about where mechanism testing bottlenecks arise.

```
You are running /discover-causal.
Your input is a feature hypothesis of the form "X causes Y."
Section order: initial falsification hypothesis first, then inertia check -- both before
evidence and mechanism. Both sections generate falsification conditions that mechanism hops
cross-reference. Gate checklists close Sections 1, 2, and 3. Every classification judgment
uses a discrete label with rationale.

Key design: two-pool falsification.
  F-NN pool: claim-derived conditions (Section 1)
  I-NN pool: inertia-derived conditions (Section 2)
Both pools carry testability (Easy/Hard/Unknown) and confidence (High/Medium/Low) columns.
Mechanism hops may cross-reference conditions from either pool.

---

## SECTION 1: CLAIM AND INITIAL FALSIFICATION HYPOTHESIS

[Extract the claim. Generate F-NN conditions from the claim alone before any inertia check
or evidence. Both testability and confidence columns required at generation time.]

Claim extraction:
  X (the cause): [Extract from input]
  Y (the claimed outcome): [Extract from input]
  Full claim: ["X causes Y" -- one sentence]

Initial falsification hypothesis (F-NN pool):
[What conditions, if observed, would prove X->Y false? From the claim alone.
Assign F-01, F-02, ... Both testability and confidence assigned at generation time.]

| ID | Initial falsification condition (claim false if observed) | Testability | Confidence | Rationale |
|----|-----------------------------------------------------------|-------------|------------|-----------|
| F-01 | [What would break X->Y?] | [ ] Easy  [ ] Hard  [ ] Unknown | [ ] High  [ ] Medium  [ ] Low | [1 sentence] |
| F-02 | [Add as many as the claim generates.] | [ ] Easy  [ ] Hard  [ ] Unknown | [ ] High  [ ] Medium  [ ] Low | [1 sentence] |

SECTION 1 GATE:
[ ] X and Y extracted separately
[ ] At least two F-NN conditions with IDs, testability, confidence, and rationale
[ ] No evidence or mechanism content written yet

--- Do not advance to Section 2 until all items are checked. ---

---

## SECTION 2: INERTIA CHECK

[First filter before evidence or mechanism: does doing nothing already produce Y? The
status quo is the strongest competitor. Confront the null hypothesis before forming a
causal theory. This section generates I-NN conditions that mechanism hops cross-reference
alongside the F-NN pool from Section 1.
Both testability and confidence columns required for I-NN conditions.]

Status-quo description: [One sentence: what is the current user experience without X?]
Does the status quo produce Y?  [ ] No  [ ] Partially  [ ] Yes or Unclear

Baseline rate: [Estimate or bound: "Y occurs approximately __% without X."
  Be as specific as possible. If unknown: "Unknown -- flag as evidence gap."]

Inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP
  (SAFE = baseline is negligible, status quo does not produce Y;
   ADVISORY = Y partially occurs without X -- some users or conditions already produce Y;
   STOP = Y occurs at a meaningful rate without X -- mechanism claim needs revision)
Inertia rationale: [1-2 sentences. If ADVISORY or STOP: name the population or condition
  where Y already occurs.]

Inertia falsification conditions (I-NN pool):
[Both testability and confidence required. Testability rationale: how would you test
whether inertia actually produces Y at this rate? Confidence: how likely is this condition
to be observable?]

| ID | Inertia falsification condition | Testability | Confidence | Rationale |
|----|---------------------------------|-------------|------------|-----------|
| I-01 | Y occurs at [baseline rate] without X | [ ] Easy  [ ] Hard  [ ] Unknown | [ ] High  [ ] Medium  [ ] Low | [1 sentence] |
[Add I-02, I-03 if the inertia check surfaces additional conditions.]

SECTION 2 GATE:
[ ] Status-quo description written
[ ] Baseline rate estimated or explicitly marked "Unknown"
[ ] Inertia severity label assigned with rationale
[ ] At least one I-NN condition with both testability AND confidence labels and rationale

--- Do not advance to Section 3 until all items are checked. ---
--- IF STOP: skip Sections 3 and 4; advance to Section 5. AMEND Inertia slot is mandatory. ---

---

## SECTION 3: EVIDENCE

[Before mapping the mechanism, establish what is known about X->Y in this context.
Generic citations fail. At least one context-specific observation required, OR "None found"
with mandatory AMEND evidence slot. Evidence may revise testability or confidence for any
F-NN or I-NN condition. Document revisions by condition ID.]

Evidence entry 1:
  Source type: [ ] Prior result  [ ] Analogous case  [ ] Domain observation  [ ] Counter-evidence
  What was observed: [Specific: what happened, where, when?]
  Bearing on X->Y: [1 sentence: supports, complicates, or contradicts?]
  Revisions: [Any F-NN or I-NN ID with dimension update (testability or confidence), or
    "No revisions."]

[Add entries as needed.]

Evidence quality: [ ] Strong  [ ] Moderate  [ ] Weak  [ ] None
Evidence quality rationale: [1 sentence]

Inertia adjustment: [Does this evidence change the inertia verdict from Section 2?
  Revised baseline if changed: [Updated rate or "No change -- confirmed."]]

SECTION 3 GATE:
[ ] At least one evidence entry (or explicit "None found" -- not skipped)
[ ] Evidence quality label assigned with rationale
[ ] Revisions field completed for every entry
[ ] Inertia adjustment addressed (update or confirm)

--- Do not advance to Section 4 until all items are checked. ---

---

## SECTION 4: MECHANISM CHAIN

[Map the causal pathway from X to Y. Two hops minimum. The mechanism must cohere with
both the inertia baseline (Section 2) and the evidence (Section 3).
If inertia is ADVISORY: scope the mechanism to explain Y *above the baseline*, not Y in general.

Every hop carries three required per-hop fields:
  Observability (Observable/Partial/Opaque): how directly can this intermediate be detected?
  Falsification connection: which F-NN or I-NN condition does this hop explain?
    Mechanism hops may cross-reference either pool (F-NN or I-NN).
  Evidence coherence: do Sections 2-3 support, contradict, or are neutral?
State mechanism only -- adversarial challenges belong in Section 5.]

Hop 1: X [name] -> [intermediate A]: [How does X produce A?]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Observability rationale: [1 sentence: how directly can this intermediate state be measured?]
  Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
  Falsification connection: [Which F-NN or I-NN from Sections 1-2 does this hop explain or
    refine? State the condition ID and one sentence: if this hop fails, this condition holds.]

Hop 2: [intermediate A] -> Y [name]: [How does A produce Y?]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Observability rationale: [1 sentence]
  Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
  Falsification connection: [Which F-NN or I-NN does this hop explain or refine? ID + 1 sentence.]

[Add Hop 3+ as needed. Every hop: observability label + rationale, evidence coherence,
falsification connection. Cross-referencing an I-NN condition is valid and encouraged.]

Mechanism strength (preliminary): [ ] Strong  [ ] Moderate  [ ] Weak
  (Accounts for inertia baseline and evidence coherence. Before adversarial challenge.)
Preliminary rationale: [1 sentence]

---

## SECTION 5: ADVERSARIAL CHALLENGE

[Structurally separate from Section 4. Challenge every hop. The challenge must also address
whether the mechanism explains incremental Y above the inertia baseline, not just Y in general.]

Hop-by-hop challenge:

Hop 1 challenge:
  What breaks X -> [intermediate A]? [Observable condition disproves this hop]
  Observable test: [What to measure]
  Alternative at this hop: [What else produces [intermediate A] without X?]
  Falsification confidence: [ ] High  [ ] Medium  [ ] Low
    (High = testable next sprint; Medium = testable with setup; Low = long-horizon or proxy)
  Confidence rationale: [1 sentence]

Hop 2 challenge:
  What breaks [intermediate A] -> Y? [Observable condition]
  Observable test: [What to measure]
  Alternative at this hop: [What else produces Y without [intermediate A]?]
  Falsification confidence: [ ] High  [ ] Medium  [ ] Low
  Confidence rationale: [1 sentence]

[Mirror all Section 4 hops.]

Baseline competitor challenge:
  [Does adversarial analysis reveal Y could be largely explained by baseline effects?]
  Adversarial baseline view: [1-2 sentences]
  Revised inertia verdict: SAFE / ADVISORY / STOP / No change -- confirm

Confounders:
  Confounder 1: [Variable correlating with both X and Y. Name and describe.]

Mechanism strength (final): [ ] Strong  [ ] Moderate  [ ] Weak  [ ] NA (STOP)
  (Update from preliminary if challenge degraded the rating.)
Final strength rationale: [1 sentence. State whether changed from preliminary and why.]

---

## SECTION 6: CLAIM SCOPE AND AMEND

Scoped claim: ["X causes Y when [condition], for [population], assuming [precondition]."]
  [If ADVISORY: "X causes Y *above the [baseline] baseline* when [condition], for [population]."]
Scope condition: [What must be true for the mechanism to hold?]
Out-of-scope: [At least one condition from Section 5 where mechanism fails]

Inertia severity (final): [ ] SAFE  [ ] ADVISORY  [ ] STOP
  (Confirm from Section 2, or update based on baseline competitor challenge above.)
Final inertia rationale: [1 sentence]

AMEND DIRECTIVE:
[Address at least two of the four slots. Mandatory:
  - Evidence slot if Section 3 found nothing
  - Inertia slot if final inertia severity is STOP or ADVISORY]

AMEND: discover-causal
  Narrow: [Scope tightening -- reference scope condition above]
  Mechanism: [Hop notation: X -> [A] -> Y]
  Falsification: [Which Section 5 challenge condition should be added to hypothesis?
    Include its confidence label and testability label.]
  Evidence: [If none: "Mechanism is theoretical. Cite one context-specific observation."]
  [Inertia: (mandatory if STOP/ADVISORY) "Y occurs at [baseline] without X.
   Reframe as incremental Y above baseline. Measure baseline before mechanism analysis."]

---

Write artifact: simulations/discover/causal/{topic}-causal-{date}.md
Frontmatter: skill, topic, date, cause (X), outcome (Y),
             two_pool_dual_dimension (true), inertia_first (false),
             gate_checklists (3),
             inertia_verdict (SAFE/ADVISORY/STOP), baseline_rate,
             evidence_count, evidence_quality (Strong/Moderate/Weak/None),
             initial_falsification_count (F-NN pool),
             inertia_falsification_count (I-NN pool),
             hop_count, mechanism_strength_preliminary (Strong/Moderate/Weak/NA),
             mechanism_strength_final (Strong/Moderate/Weak/NA),
             strength_changed (true/false),
             mechanism_hop_falsification_links (true),
             hop_observability_labels (true),
             fnn_testability_list (Easy/Hard/Unknown per F-NN sorted),
             inn_testability_list (Easy/Hard/Unknown per I-NN sorted),
             falsification_confidence_list (High/Medium/Low per condition sorted),
             confounder_named (true/false).
```

---

## V-04: Observability Summary Table (A-10 as Coverage Diagnostic)

**Axis:** Output format — A-10 is promoted from an inline per-hop annotation field to a first-class standalone sub-table in Section 5, positioned alongside the bidirectionality table. The Observability Summary table lists each hop with its observability label (Observable/Partial/Opaque), rationale, and a flag for whether it is a weak link in the causal chain. This externalizes observability the same way the bidirectionality table externalizes falsification coverage: aggregate patterns become visible that per-hop fields obscure. A-11 is satisfied by adding a testability column to the Section 1 F-NN table.

**Hypothesis:** When observability is in inline fields, each hop's label is consumed in isolation. When extracted into a summary table, the analyst sees the distribution: all Observable, all Opaque, or mixed. An all-Opaque hop chain is a signal that the mechanism is untestable by instrumentation alone — a finding that warrants AMEND. This aggregate view is impossible from inline annotation. The bidirectionality table already expresses this logic for falsification coverage; applying the same pattern to observability should produce equivalent diagnostic power.

```
You are running /discover-causal.
Your input is a feature hypothesis of the form "X causes Y."
This skill introduces an OBSERVABILITY SUMMARY TABLE in Section 5 alongside the
BIDIRECTIONALITY TABLE. Both tables are positioned between mechanism mapping and adversarial
challenge and share a single gate. Section order:
  1. Claim intake and initial falsification hypothesis (testability + confidence)
  2. Evidence
  3. Inertia check
  4. Mechanism chain (per-hop observability annotation + preliminary falsification connection)
  5. Coverage and observability tables (bidirectionality + observability summary; gated)
  6. Adversarial challenge
  7. Claim scope and AMEND

Every classification judgment uses a discrete label with rationale.

---

## SECTION 1: CLAIM AND INITIAL FALSIFICATION HYPOTHESIS

Claim extraction:
  X (the cause): [Extract from input]
  Y (the claimed outcome): [Extract from input]
  Full claim: ["X causes Y" -- one sentence]

Initial falsification hypothesis:
[From the claim alone: what conditions, if observed, would prove X->Y false?
Assign F-NN IDs. Both testability and confidence columns assigned at generation time.
These become rows in the bidirectionality table Direction A in Section 5.]

| ID | Initial falsification condition (claim false if observed) | Testability | Confidence | Rationale |
|----|-----------------------------------------------------------|-------------|------------|-----------|
| F-01 | [What would break X->Y?] | [ ] Easy  [ ] Hard  [ ] Unknown | [ ] High  [ ] Medium  [ ] Low | [1 sentence] |
| F-02 | [Add as many as the claim generates.] | [ ] Easy  [ ] Hard  [ ] Unknown | [ ] High  [ ] Medium  [ ] Low | [1 sentence] |

---

## SECTION 2: EVIDENCE

[At least one context-specific observation, OR "None found" with mandatory AMEND slot.
Evidence may revise testability or confidence for any F-NN condition.]

Evidence entry 1:
  Source type: [ ] Prior result  [ ] Analogous case  [ ] Domain observation  [ ] Counter-evidence
  Observation: [What was seen, where, when?]
  Bearing on X->Y: [1 sentence]
  Revisions: [Any F-NN ID with dimension update, or "No revisions."]

[Add entries as needed.]

Evidence quality: [ ] Strong  [ ] Moderate  [ ] Weak  [ ] None
Evidence quality rationale: [1 sentence]

---

## SECTION 3: INERTIA CHECK

Status-quo description: [What happens today without X?]
Baseline rate: [Estimate or bound. Or: "Unknown."]

Inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP
  (SAFE = does not produce Y; ADVISORY = partially; STOP = plausibly already produces Y)
Inertia rationale: [1 sentence]

Inertia as falsifier:
| ID | Inertia falsification condition | Testability | Confidence | Rationale |
|----|---------------------------------|-------------|------------|-----------|
| I-01 | Y occurs at [baseline rate] without X | [ ] Easy  [ ] Hard  [ ] Unknown | [ ] High  [ ] Medium  [ ] Low | [1 sentence] |

--- IF STOP: skip Sections 4 and 5; advance to Section 6. ---

---

## SECTION 4: MECHANISM CHAIN

[Map the causal pathway from X to Y. Two hops minimum. Cohere with Section 2 evidence.
Note evidence tensions explicitly. State mechanism only -- challenges belong in Section 6.

Every hop carries:
  Observability annotation (preliminary): the label that will be formalized in the
    Observability Summary table in Section 5.
  Falsification connection (preliminary): the condition ID that will be formalized in
    the Bidirectionality Table in Section 5.
  Evidence coherence.
The Section 5 tables finalize and cross-check both annotations.]

Hop 1: X [name] -> [intermediate A]: [How does X produce A?]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Observability rationale: [1 sentence: how directly can this intermediate be detected?]
  Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
  Falsification connection (preliminary): [Which F-NN or I-NN from Sections 1-3 does this
    hop most likely explain? Write the condition ID.]

Hop 2: [intermediate A] -> Y [name]: [How does A produce Y?]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Observability rationale: [1 sentence]
  Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
  Falsification connection (preliminary): [Which F-NN or I-NN does this hop explain? ID.]

[Add Hop 3+ as needed. Every hop: observability label + rationale, evidence coherence,
preliminary falsification connection.]

Mechanism strength (preliminary): [ ] Strong  [ ] Moderate  [ ] Weak
  (Before Section 5 tables and adversarial challenge.)
Preliminary rationale: [1 sentence]

---

## SECTION 5: COVERAGE AND OBSERVABILITY TABLES

[This section formalizes the two annotation types from Section 4 into dedicated diagnostic
tables. Complete both tables fully before advancing to Section 6. The tables serve as
coverage diagnostics: they reveal uncovered conditions, uncovered hops, and Opaque hop chains
that the inline annotations in Section 4 cannot surface in aggregate.]

### Bidirectionality Table

**Direction A: Falsification Condition -> Mechanism Hops**
[For each F-NN and I-NN condition, identify which mechanism hops explain it.
Update confidence labels if mechanism analysis changed the assessment.]

| Condition ID | Condition text (abbreviated) | Explained by | Testability | Confidence | Rationale | Gap? |
|--------------|------------------------------|-------------|-------------|------------|-----------|------|
| F-01 | [from Section 1] | Hop [N], Hop [N] | [from generation] | [ ] High  [ ] Medium  [ ] Low | [1 sentence] | [ ] Yes  [ ] No |
| I-01 | [from Section 3] | Hop [N] | [from generation] | [ ] High  [ ] Medium  [ ] Low | [1 sentence] | [ ] Yes  [ ] No |
[Add all F-NN and I-NN conditions. Mark Gap=Yes if no hop explains this condition.]

**Direction B: Mechanism Hop -> Falsification Conditions**
[For each hop, list the falsification conditions it explains. This finalizes Section 4 annotations.]

| Hop | Mechanism step (abbreviated) | Conditions explained | Coverage complete? |
|-----|------------------------------|---------------------|--------------------|
| Hop 1 | X -> [intermediate A] | F-NN, I-NN | [ ] Yes  [ ] No |
| Hop 2 | [intermediate A] -> Y | F-NN | [ ] Yes  [ ] No |
[Mirror all Section 4 hops. Mark Coverage complete=No if hop has no condition reference.]

**Bidirectionality gaps:**
  [List any Direction A gaps (conditions no hop explains) and Direction B gaps (hops with
  no condition). If none: "No gaps -- all conditions explained, all hops cross-referenced."]

### Observability Summary Table

[Extract observability labels from Section 4 into a standalone table. This enables aggregate
pattern detection: an all-Opaque chain means the mechanism is undetectable by instrumentation;
a mixed chain identifies which hops are measurement bottlenecks.]

| Hop | Mechanism step (abbreviated) | Observability | Rationale | Weak link? |
|-----|------------------------------|---------------|-----------|------------|
| Hop 1 | X -> [intermediate A] | [ ] Observable  [ ] Partial  [ ] Opaque | [from Section 4] | [ ] Yes  [ ] No |
| Hop 2 | [intermediate A] -> Y | [ ] Observable  [ ] Partial  [ ] Opaque | [from Section 4] | [ ] Yes  [ ] No |
[Mirror all Section 4 hops. Mark Weak link=Yes if Opaque and this hop is the bottleneck
for testing the mechanism.]

**Observability pattern:**
  [ ] All Observable -- mechanism is fully instrumented
  [ ] Mixed -- some hops require indirect detection
  [ ] Predominantly Opaque -- mechanism is largely unobservable; AMEND mechanism slot mandatory
Observability pattern rationale: [1 sentence]

SECTION 5 GATE:
[ ] Every F-NN and I-NN condition has a row in Direction A with testability and confidence
[ ] Every Section 4 hop has a row in Direction B
[ ] Gap field completed (or "No gaps")
[ ] Every Section 4 hop has a row in Observability Summary with label and weak-link flag
[ ] Observability pattern declared with rationale
[ ] No new mechanism hops added after Direction A was completed

--- Do not advance to Section 6 until all Section 5 gate items are checked. ---

---

## SECTION 6: ADVERSARIAL CHALLENGE

[Structurally separate from Sections 4 and 5. Challenge every hop. Use Section 5 tables
to prioritize: Direction A gaps and Opaque weak-link hops are priority targets.]

Hop-by-hop challenge:

Hop 1 challenge:
  What breaks X -> [intermediate A]? [Observable condition disproves this hop]
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
  Adversarial view: [Does analysis reveal Y could be explained by baseline effects?]
  Revised inertia verdict: SAFE / ADVISORY / STOP / No change -- confirm

Mechanism strength (final): [ ] Strong  [ ] Moderate  [ ] Weak  [ ] NA (STOP)
Final strength rationale: [1 sentence. State whether changed from preliminary and why.]

---

## SECTION 7: CLAIM SCOPE AND AMEND

Scoped claim: ["X causes Y when [condition], for [population], assuming [precondition]."]
Scope condition: [Reference bidirectionality gaps AND observability weak links AND adversarial findings.]
Out-of-scope: [At least one context from Section 6 where mechanism fails]

Inertia severity (final): [ ] SAFE  [ ] ADVISORY  [ ] STOP
Final inertia rationale: [1 sentence]

AMEND DIRECTIVE:
[Address at least two of the four slots. Mandatory:
  - Evidence slot if Section 2 found nothing
  - Inertia slot if final inertia severity is STOP or ADVISORY
  - Mechanism gap slot if Section 5 has uncovered conditions or predominantly Opaque hops]

AMEND: discover-causal
  Narrow: [Scope tightening]
  Mechanism: [Hop notation: X -> [A] -> Y]
  Falsification: [Which HIGH confidence condition from Section 6? Name, ID, testability label.]
  Evidence: [If none: "Mechanism is theoretical. Cite one context-specific observation."]
  [Inertia: (mandatory if STOP/ADVISORY) "Y occurs at [baseline] without X.
   Demonstrate incremental Y above baseline."]
  [Mechanism gap: (if Section 5 has uncovered conditions) "F-NN has no hop explanation.
   Add a mechanism hop covering this condition, or retire F-NN from the hypothesis."]
  [Observability: (if predominantly Opaque) "Mechanism hops [N] are unobservable. Identify
   proxy measurements or narrow claim to observable portion of mechanism."]

---

Write artifact: simulations/discover/causal/{topic}-causal-{date}.md
Frontmatter: skill, topic, date, cause (X), outcome (Y),
             observability_summary_table (true), bidirectionality_table (true),
             gate_checklists (1),
             inertia_verdict (SAFE/ADVISORY/STOP), baseline_rate,
             evidence_count, evidence_quality (Strong/Moderate/Weak/None),
             initial_falsification_count, inertia_falsification_count,
             hop_count, mechanism_strength_preliminary (Strong/Moderate/Weak/NA),
             mechanism_strength_final (Strong/Moderate/Weak/NA),
             strength_changed (true/false),
             bidirectionality_gaps (true/false),
             observability_pattern (AllObservable/Mixed/PredominantlyOpaque),
             hop_observability_labels (true),
             falsification_testability_list (Easy/Hard/Unknown per condition sorted),
             falsification_confidence_list (High/Medium/Low per condition sorted),
             confounder_named (true/false).
```

---

## V-05: Testability Refinement Lifecycle (Unknown at Genesis -> Determinate via Evidence)

**Axis:** Lifecycle emphasis — all falsification conditions start with testability = Unknown at generation time in Section A1. The evidence sub-section (Section A2) contains an explicit "Testability refinement" pass: for each condition, evidence may update testability from Unknown to Easy or Hard. A gate item at Section A requires at least one testability refinement OR explicit confirmation that all conditions remain Unknown (which is a finding, not a skip). The compact 4-section form (A/B/C/D) is preserved.

**Hypothesis:** Testability is often not knowable from the claim alone -- it requires knowing what instrumentation and data access is available, which emerges during evidence gathering. Starting all conditions at Unknown forces the evidence section to actually engage with the question "can we run this test?" for each condition, rather than allowing the analyst to assign Easy as a default. Residual Unknowns after evidence are a diagnostic: they identify conditions where neither prior evidence nor current tooling knowledge can answer the question. This is meaningfully different from Hard (we know it is hard) and should be surfaced explicitly.

```
You are running /discover-causal.
Your input is a feature hypothesis of the form "X causes Y."
Four sections. Complete each fully before advancing. Gate checklists close Sections A and B.
Every classification judgment uses a discrete label with rationale.

Testability lifecycle: every falsification condition starts as Unknown at generation.
The evidence sub-section (A2) refines testability where context allows. Conditions that
remain Unknown after evidence are a finding: record them explicitly. They are distinct from
Hard (testable but resource-constrained) and require action in AMEND.

---

## SECTION A: INTAKE -- FALSIFICATION, EVIDENCE, INERTIA

[Three sub-tasks in order. All must be complete before mechanism work begins.]

### A1: Claim and initial falsification
X (the cause): [Extract from input]
Y (the claimed outcome): [Extract from input]
Full claim: ["X causes Y" -- one sentence]

Initial falsification conditions:
[From the claim alone. Assign F-NN IDs. Confidence assigned at generation time.
Testability starts Unknown for all conditions -- refinement happens in A2.]

| ID | Falsification condition (claim false if observed) | Testability | Confidence | Rationale |
|----|---------------------------------------------------|-------------|------------|-----------|
| F-01 | [What would break X->Y?] | Unknown (see A2) | [ ] High  [ ] Medium  [ ] Low | [1 sentence] |
| F-02 | [Add as many as the claim generates.] | Unknown (see A2) | [ ] High  [ ] Medium  [ ] Low | [1 sentence] |

Inertia conditions are generated in A3 and also start Unknown.

### A2: Prior evidence and testability refinement
[At least one context-specific observation, OR "None found" with mandatory AMEND evidence slot.
After gathering evidence, explicitly revisit every F-NN condition and refine its testability
if the evidence enables it. Document each refinement or explicit confirmation that Unknown
persists. Evidence may also refine confidence labels.]

Evidence entry 1:
  Source type: [ ] Prior result  [ ] Analogous case  [ ] Domain observation  [ ] Counter-evidence
  Observation: [What was seen, where, when?]
  Bearing on X->Y: [1 sentence]

[Add entries as needed.]

Evidence quality: [ ] Strong  [ ] Moderate  [ ] Weak  [ ] None
Evidence quality rationale: [1 sentence]

Testability refinement pass:
[For each F-NN condition, decide: does the evidence above enable a testability determination?
Record the final testability label and the rationale.]

| ID | Final testability | Refinement rationale |
|----|-------------------|---------------------|
| F-01 | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence: what evidence enabled or blocked determination?] |
| F-02 | [ ] Easy  [ ] Hard  [ ] Unknown | [1 sentence] |
[Mirror all F-NN conditions from A1.]

Residual Unknown summary:
[List all conditions where testability remains Unknown after evidence. These require action
in AMEND section D. If none: "All conditions have determinate testability after evidence."]

### A3: Inertia check
Status-quo description: [One sentence: what happens today without X?]
Does the status quo produce Y?  [ ] No  [ ] Partially  [ ] Yes or Unclear
Baseline rate: [Estimate or bound. Or: "Unknown."]

Inertia severity: [ ] SAFE  [ ] ADVISORY  [ ] STOP
  (SAFE = does not produce Y; ADVISORY = partially; STOP = plausibly already produces Y)
Inertia rationale: [1 sentence]

| ID | Inertia falsification condition | Testability | Confidence | Rationale |
|----|---------------------------------|-------------|------------|-----------|
| I-01 | Y occurs at [baseline rate] without X | Unknown (see A2 testability refinement) | [ ] High  [ ] Medium  [ ] Low | [1 sentence] |

[Refine I-01 testability in the A2 testability refinement pass above. Add I-01 to the
refinement table before completing Section A gate.]

SECTION A GATE:
[ ] At least two F-NN conditions with IDs, initial testability (Unknown), confidence, and rationale
[ ] Evidence populated (or explicit "None found" -- not skipped)
[ ] Evidence quality label assigned with rationale
[ ] Testability refinement pass completed for every F-NN and I-NN condition
[ ] Residual Unknown summary written (or confirmed empty)
[ ] Inertia severity label assigned with rationale

--- Do not advance to Section B until all items are checked. ---
--- IF STOP: skip Section B; advance to Section C. ---

---

## SECTION B: MECHANISM CHAIN

[Map the causal pathway from X to Y. Two hops minimum. Cohere with Section A evidence.
Every hop carries observability label (Observable/Partial/Opaque) + rationale,
evidence coherence, and falsification connection to a pre-existing F-NN or I-NN from Section A.
State mechanism only -- adversarial content belongs in Section C.]

Hop 1: X [name] -> [intermediate A]: [How does X produce A?]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Observability rationale: [1 sentence: how directly can this intermediate be detected?]
  Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
  Falsification connection: [Which F-NN or I-NN from Section A does this hop explain?
    Write the condition ID and one sentence: if this hop fails, this condition is observed.]

Hop 2: [intermediate A] -> Y [name]: [How does A produce Y?]
  Observability: [ ] Observable  [ ] Partial  [ ] Opaque
  Observability rationale: [1 sentence]
  Evidence coherence: [ ] Supported  [ ] Neutral  [ ] Tensions -- describe
  Falsification connection: [Which F-NN or I-NN this hop explains. ID + 1 sentence.]

[Add Hop 3+ as needed. Every hop: observability label + rationale, evidence coherence,
falsification connection to a pre-existing condition from Section A.]

Mechanism strength (preliminary): [ ] Strong  [ ] Moderate  [ ] Weak
  (Before adversarial challenge. Based on observability ratings and evidence coherence.)
Preliminary rationale: [1 sentence]

SECTION B GATE:
[ ] At least two hops filled
[ ] Every hop has observability label (Observable/Partial/Opaque) and rationale
[ ] Every hop has a falsification connection naming a pre-existing F-NN or I-NN from Section A
[ ] Mechanism strength (preliminary) assigned with rationale
[ ] No adversarial content in this section

--- Do not advance to Section C until all items are checked. ---

---

## SECTION C: ADVERSARIAL CHALLENGE

[Structurally separate from Section B. Challenge every hop. Name what would break each
step, name alternatives, identify confounders. Reference testability labels from Section A
when assigning confidence: Easy conditions should be High confidence candidates; Hard or
Unknown conditions warrant explicit note if assigned High confidence.]

Hop 1 challenge:
  What breaks X -> [intermediate A]? [Observable condition disproves this hop]
  Observable test: [What to measure or detect]
  Alternative at this hop: [What else produces [intermediate A] without X?]
  Falsification confidence: [ ] High  [ ] Medium  [ ] Low
    (High = measurable next sprint; Medium = measurable with setup; Low = long-horizon only)
  Confidence rationale: [1 sentence. Note if testability is Unknown or Hard and confidence
    is High -- explain why confidence is warranted despite testability constraints.]

Hop 2 challenge:
  What breaks [intermediate A] -> Y? [Observable condition]
  Observable test: [What to measure or detect]
  Alternative at this hop: [What else produces Y without [intermediate A]?]
  Falsification confidence: [ ] High  [ ] Medium  [ ] Low
  Confidence rationale: [1 sentence]

[Mirror all Section B hops.]

Confounders:
  Confounder 1: [Variable correlating with both X and Y. Name and describe.]

Inertia challenge:
  [Does adversarial analysis change the inertia verdict from Section A3?]
  Adversarial view: [1-2 sentences]
  Revised verdict: SAFE / ADVISORY / STOP / No change -- confirm

Mechanism strength (final): [ ] Strong  [ ] Moderate  [ ] Weak  [ ] NA (STOP)
  (Update from preliminary if challenge degraded the rating.)
Final strength rationale: [1 sentence. State whether changed from preliminary and why.]

---

## SECTION D: SCOPE AND AMEND

Scoped claim: ["X causes Y when [condition], for [population], assuming [precondition]."]
Scope condition: [What must be true for the mechanism to hold?]
Out-of-scope: [At least one condition from Section C where mechanism fails]

Inertia severity (final): [ ] SAFE  [ ] ADVISORY  [ ] STOP
Final inertia rationale: [1 sentence]

AMEND DIRECTIVE:
[Address at least two of the four slots. Mandatory:
  - Evidence slot if Section A2 found nothing
  - Inertia slot if final inertia severity is STOP or ADVISORY
  - Testability slot if Section A2 residual Unknown summary has any entries]

AMEND: discover-causal
  Narrow: [Scope tightening]
  Mechanism: [Hop notation: X -> [A] -> Y]
  Falsification: [Which HIGH confidence condition from Section C? Name, ID, and testability
    label from Section A2 refinement. If testability is Unknown: note this is an open question.]
  Evidence: [If none: "Mechanism is theoretical. Cite one context-specific observation."]
  [Inertia: (mandatory if STOP/ADVISORY) "Y occurs at [baseline] without X.
   Demonstrate incremental Y above baseline."]
  [Testability: (mandatory if residual Unknowns in A2) "Conditions [F-NN IDs] have Unknown
   testability after evidence. Determine available instrumentation before treating these
   conditions as actionable."]

---

Write artifact: simulations/discover/causal/{topic}-causal-{date}.md
Frontmatter: skill, topic, date, cause (X), outcome (Y),
             testability_refinement_lifecycle (true), gate_checklists (2),
             inertia_verdict (SAFE/ADVISORY/STOP), baseline_rate,
             evidence_count, evidence_quality (Strong/Moderate/Weak/None),
             initial_falsification_count,
             hop_count, mechanism_strength_preliminary (Strong/Moderate/Weak/NA),
             mechanism_strength_final (Strong/Moderate/Weak/NA),
             strength_changed (true/false),
             mechanism_hop_falsification_links (true),
             hop_observability_labels (true),
             testability_refined_count (conditions that moved from Unknown to Easy/Hard),
             testability_residual_unknown_count (conditions remaining Unknown after evidence),
             falsification_testability_list (Easy/Hard/Unknown per condition after A2),
             falsification_confidence_list (High/Medium/Low per condition from C),
             confounder_named (true/false).
```

---

## Round 5 Design Notes

### v5 aspirational criterion coverage

| V | A-01 | A-02 | A-03 | A-04 | A-05 | A-06 | A-07 | A-08 | A-09 | A-10 | A-11 |
|---|------|------|------|------|------|------|------|------|------|------|------|
| V-01 | YES prelim+final S4/S5 | YES S3 baseline | YES S5 adversarial | YES all fields incl dual-col | YES S2 before S4 | YES prelim S4/final S5 | YES F-table S1 + I-01 + final S5 | YES S4 hop connection | YES 4 gates S1-S4 | YES S4 all hops | YES dual-col from genesis |
| V-02 | YES ANALYST prelim/SKEPTIC final | YES FRAMER baseline | YES SKEPTIC role | YES all fields | YES FRAMER before ANALYST | YES ANALYST prelim/SKEPTIC final | YES SKEPTIC final table per-row | YES ANALYST hop FRAMER F-ref | YES 3 role gates | YES ANALYST all hops | YES FRAMER table testability-only |
| V-03 | YES prelim+final | YES S2 I-NN baseline | YES S5 adversarial | YES all fields both pools | YES S3 before S4 | YES prelim S4/final S5 | YES F-table S1 + I-table S2 + S5 per-hop | YES S4 hop either pool | YES S1/S2/S3 gates | YES S4 all hops | YES both F-NN+I-NN pools |
| V-04 | YES prelim+final | YES S3 baseline | YES S6 adversarial | YES all fields | YES S2 before S4 | YES prelim S4/final S6 | YES F-table S1 + S5 Dir-A + S6 per-hop | YES S4 hop + S5 Dir-B | YES S5 gate | YES S4 hops + S5 Obs-Summary | YES S1 dual-col + S5 Dir-A |
| V-05 | YES prelim+final | YES A3 baseline | YES C adversarial | YES all fields | YES A before B | YES prelim B/final C | YES F-table A1 + A2 refined + C per-hop | YES B hop F-connection | YES A-gate + B-gate | YES B all hops | YES A2 refinement lifecycle |

### Predicted composite scores under v5 rubric

| V | Ess (est) | Rec (est) | Asp (est, v5/11) | Composite (est) | Golden (est) |
|---|-----------|-----------|-----------------|-----------------|--------------|
| V-01 | 5/5 | 3/3 | 11/11 | 100.0 | YES |
| V-02 | 5/5 | 3/3 | 11/11 | 100.0 | YES |
| V-03 | 5/5 | 3/3 | 11/11 | 100.0 | YES |
| V-04 | 5/5 | 3/3 | 11/11 | 100.0 | YES |
| V-05 | 5/5 | 3/3 | 11/11 | 100.0 | YES |

### Dimension ownership comparison across R5 variations

| V | Who assigns testability | When | Who assigns confidence | When |
|---|------------------------|------|----------------------|------|
| V-01 | Analyst (inline) | At generation (S1) | Analyst (inline) | At generation (S1) + refined S5 |
| V-02 | FRAMER role | At generation (opening) | SKEPTIC role | After mechanism (challenge) |
| V-03 | Analyst (inline) | At generation (S1+S2) | Analyst (inline) | At generation (S1+S2) + refined S5 |
| V-04 | Analyst (inline) | At generation (S1+S3) | Analyst (inline) | At generation + confirmed S5 |
| V-05 | Analyst (inline, staged) | Unknown at S-A1; refined at A2 | Analyst (inline) | At generation (A1) |

### Open research questions for R6

1. **Testability distribution at genesis vs. after refinement (V-01 vs V-05)**: V-01 assigns testability at generation without evidence context; V-05 defers to after evidence. Do the two approaches produce different distributions (more Easy in V-01 reflecting over-optimism; more Hard/Unknown in V-05 reflecting honest assessment after encountering evidence gaps)?

2. **Role ownership and rationale quality (V-02)**: Does assigning testability to FRAMER and confidence to SKEPTIC produce rationale text that is semantically distinct (testability rationale cites tooling/access; confidence rationale cites mechanism depth)? Can the test be automated by categorizing rationale words?

3. **I-NN testability asymmetry (V-03)**: Across live runs, do I-NN conditions earn more Hard or Unknown testability ratings than F-NN conditions? Hypothesis: inertia conditions are structurally harder to test because they require baseline measurement and counterfactual isolation.

4. **Observability summary pattern (V-04)**: Do live runs produce any all-Opaque or predominantly-Opaque observability patterns? If so, does the summary table reliably trigger the AMEND observability slot? Does this slot appear in V-01/V-02/V-03/V-05 (which have no summary table) at the same rate?

5. **Residual Unknown yield (V-05)**: What fraction of conditions start Unknown and remain Unknown after evidence? Is this fraction higher for I-NN conditions than F-NN conditions? Does residual Unknown count correlate with evidence quality (more residual Unknowns when evidence quality is None or Weak)?

```json
{"round": 5, "rubric_version": "v5", "target_score": 100.0, "all_essential_pass_predicted": true,
 "new_criteria": ["A-10: hop observability label (Observable/Partial/Opaque) + rationale per hop",
                  "A-11: testability rating (Easy/Hard/Unknown) per falsification condition, distinct from confidence"],
 "variation_axes": {
   "V-01": "dual-column F-NN: testability + confidence co-labeled at genesis",
   "V-02": "role-owned dimensions: FRAMER=testability, SKEPTIC=confidence",
   "V-03": "two-pool dual-dimension: A-11 extended to I-NN inertia pool",
   "V-04": "observability summary table: A-10 as standalone coverage diagnostic",
   "V-05": "testability refinement lifecycle: Unknown at genesis -> determinate via evidence"
 },
 "r6_questions": [
   "testability-distribution: does genesis assignment (V-01) vs refinement (V-05) produce different Easy/Hard/Unknown ratios?",
   "role-rationale-quality: does V-02 role ownership produce semantically distinct testability vs confidence rationales?",
   "inn-testability-asymmetry: do I-NN conditions earn more Hard/Unknown ratings than F-NN conditions in V-03?",
   "observability-pattern-detection: does V-04 summary table reliably trigger AMEND observability slot for Opaque chains?",
   "residual-unknown-yield: what fraction of Unknown conditions remain Unknown after evidence in V-05?"
 ]}
```
