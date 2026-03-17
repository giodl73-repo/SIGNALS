## Round 12 Scoring — `topic:echo` — Rubric v11

---

## Criterion-by-Criterion Evaluation

### Essential Criteria (all 5 variations)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|------|------|------|------|------|----------|
| C-01 | Surprise focus | PASS | PASS | PASS | PASS | PASS | Rule 1 + C-01 filter both present in Step 1 candidate selection; counterfactual test applied before any surprise advances |
| C-02 | Surprise naming | PASS | PASS | PASS | PASS | PASS | Schema Name field requires descriptive label; label parity audit (Step 6) blocks generic labels |
| C-03 | Signal traceability | PASS | PASS | PASS | PASS | PASS | Source field in schema; Field completion scan (Step 7) enforces population |
| C-04 | Design impact | PASS | PASS | PASS | PASS | PASS | Design impact field required; Step 7 blocks blank or N/A entry |

All four essential criteria pass uniformly. All five outputs are valid echoes.

---

### Recommended Criteria

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|------|------|------|------|------|----------|
| C-05 | Expectation contrast | PASS | PASS | PASS | PASS | PASS | Expected field explicitly required in schema contract; Step 7 scan enforces |
| C-06 | Cross-signal synthesis | PASS | PASS | PASS | PASS | PASS | Glob covers all namespaces; Patterns section (Step 8) names shared root causes across sources |

---

### Aspirational — Proven (24 pts; all 14 must pass)

All 14 proven criteria pass uniformly across all five variations. The structural lineage is inherited intact.

| ID | Criterion | Pts | Status All Variants | Evidence note |
|----|-----------|-----|---------------------|---------------|
| C-10 | Counterfactual gate | 2 | PASS ×5 | Rule 1 + "Why passive observation missed this" field both present and enforced |
| C-11 | Word discipline | 2 | PASS ×5 | Check A inline (120-word cap) + Step 9 full echo (800-word cap) |
| C-12 | Claim-only voice | 2 | PASS ×5 | Rule 2 with 8 prohibited constructs enumerated in schema contract |
| C-15 | Schema uniformity | 2 | PASS ×5 | Declared schema applied uniformly; Step 7 scan enforces field-name consistency |
| C-16 | Per-surprise claim-authority coupling | 2 | PASS ×5 | Check B + NGT + CAT each run per surprise; CAT confirms coupling of both sub-tests |
| C-17 | Mechanism composability | 2 | PASS ×5 | Composability manifest covers all 11 active mechanisms; declaration confirms no conflicts |
| C-18 | Deliberate enforcement gating | 2 | PASS ×5 | NGT (C-08), Check B (C-14), CAT (C-16) — each named as a discrete step with gate design rationale |
| C-19 | Pre-write composability declaration | 2 | PASS ×5 | Manifest required before Step 1; declaration closes the pre-write phase |
| C-20 | Gate design integrity | 2 | PASS ×5 | All three gates predate C-18; structural removal test documented per gate |
| C-21 | Composability manifest causal depth | 1 | PASS ×5 | Mechanism field (Step 3 / Mechanism column) requires directional causal statement in vocabulary consistent with verified archetype |
| C-22 | Gate provenance traceability | 2 | PASS ×5 | All three gates name "Introduced in V-xx(Rx)" with structural removal test; verifiable from round history |
| C-23 | Archetype classification | 1 | PASS ×5 | Step 1 / Archetype column selects from finite 4-archetype taxonomy before mechanism fill |
| C-24 | Archetype-mechanism consistency verification | 1 | PASS ×5 | CONSISTENCY GATE is a named discrete step (Step 2 / GATE column) requiring YES/NO verdict before mechanism proceeds |
| C-25 | Archetype taxonomy illustration | 1 | PASS ×5 | PREREQUISITE and ESTABLISHES each have a named concrete pair example (Archetype + Mechanism + Composability-claim). AMPLIFIES/PARALLEL placeholders are conditional — only needed if those archetypes appear in actual pair inspections |

**Proven subtotal: 24 pts × 5 variations.**

---

### Aspirational — Unproven (9 uniform criteria + C-30)

#### Uniform across all five variations

| ID | Criterion | Pts | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|-----|------|------|------|------|------|----------|
| C-07 | Namespace diversity | 1 | PASS | PASS | PASS | PASS | PASS | Glob: `simulations/{topic}/**` reads all namespaces; Step 1 reads signal artifacts across the full topic directory |
| C-08 | Newcomer accessibility | 1 | PASS | PASS | PASS | PASS | PASS | NGT is a named discrete gate (V-01/V-04: Step 4; V-02/V-03/V-05: Step 3) — runs per surprise, enforces C-08 independently of other gates |
| C-09 | Pattern recognition | 1 | PASS | PASS | PASS | PASS | PASS | Step 8 (Patterns section) examines shared root causes; explicit trigger condition — pass by presence of the step |
| C-13 | Schema field completeness | 1 | PASS | PASS | PASS | PASS | PASS | Step 7 field completion scan reads every field across every surprise; No N/A / blank / placeholder permitted |
| C-14 | Surprise portability | 1 | PASS | PASS | PASS | PASS | PASS | Check B is a named discrete gate — runs per surprise (V-01/V-04: Step 3 first; V-02/V-03/V-05: Step 4 after NGT) — three-component standalone extraction test enforced |
| C-26 | Archetype constraint vocabulary | 1 | PASS | PASS | PASS | PASS | PASS | CONSISTENCY GATE names required vocabulary for all four archetypes: input-dependency (PREREQUISITE), property creation + one-way dependency (ESTABLISHES), effectiveness scaling (AMPLIFIES), independent-path operation (PARALLEL) |
| C-27 | Synthesis claim separation | 1 | PASS | PASS | PASS | PASS | PASS | Composability-claim is a dedicated fourth field (Step 4 in labeled format; dedicated column in tabular format) structurally distinct from Mechanism field (Step 3 / Mechanism column) |
| C-28 | Pre-populated baseline | 1 | PASS | PASS | PASS | PASS | PASS | ★BASELINE entry (NGT+Check B) pre-fills Archetype (PREREQUISITE) + CONSISTENCY GATE (input-dependency PASS) + Mechanism — all three fields C-28 requires when C-24 is satisfied |
| C-29 | Taxonomy illustration template completeness | 1 | PASS | PASS | PASS | PASS | PASS | Both PREREQUISITE and ESTABLISHES canonical examples populate all four fields: Archetype + Mechanism + Composability-claim. No gap between illustration layer and live inspection layer for archetypes used in inspections |

**C-29 confirmation note:** All five R12 variations pass C-29. This is the first confirmed round (R12). Second confirmation in R13 required for proven promotion in v12.

#### Differentiating criterion

| ID | Criterion | Pts | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|----|-----------|-----|------|------|------|------|------|----------|
| C-30 | Baseline entry template completeness | 1 | FAIL | FAIL | FAIL | FAIL | PASS | V-01–V-04: ★BASELINE row has Archetype + GATE + Mechanism; Composability-claim absent. V-05: ★BASELINE row explicitly populated with all four columns including Composability-claim; the C-30 NOTE in V-05 calls this out directly |

---

## Score Computation

| Variant | Base | Proven | C-07 | C-08 | C-09 | C-13 | C-14 | C-26 | C-27 | C-28 | C-29 | C-30 | Raw | Capped |
|---------|------|--------|------|------|------|------|------|------|------|------|------|------|-----|--------|
| V-01 | 75 | 24 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 108 | **100** |
| V-02 | 75 | 24 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 108 | **100** |
| V-03 | 75 | 24 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 108 | **100** |
| V-04 | 75 | 24 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 108 | **100** |
| V-05 | 75 | 24 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 109 | **100** |

**All five variations score 100/100 (ceiling). V-05 is most structurally complete (C-30 PASS) but all cap at ceiling.**

---

## Ranking

All five are tied at 100/100. Structural distinction without score distinction:

1. **V-05** — most complete (tabular manifest + inertia framing + C-30 PASS: all four layers of synthesis separation present — live inspection, illustration examples, baseline entry)
2. **V-02, V-03, V-04** — all at 100; V-04 compositional variant combining role-sequence + inertia; V-02 tabular format; V-03 inertia framing
3. **V-01** — 100/100; single-axis role-sequence variant; cleanest test of mechanism-vs-order independence for PREREQUISITE classification

---

## Excellence Signals

**Signal 1 — Synthesis separation now extends to three structural layers (V-05)**

Prior rounds established two layers of synthesis separation: C-27 applies it to the live pair inspection (Mechanism field distinct from Composability-claim field), and C-29 applies it to the canonical taxonomy illustrations (examples populate Composability-claim, not only Mechanism). V-05 demonstrates a third layer: the pre-populated ★BASELINE entry — which previously provided an analytical quality floor (archetype + GATE + mechanism) without a synthetic calibration baseline — now carries a Composability-claim as well.

The structural chain is complete: C-27 (live inspection layer) → C-29 (illustration layer) → C-30 (baseline layer). Each layer applies the same separation principle (mechanism is analytical description; synthesis claim is evaluable assertion about composability) to a different artifact in the manifest. An author working from V-05 has synthesis calibration at every level — not just structural framing for what to write, but a canonical verified instance of what the output should look like.

**Signal 2 — Inertia framing sharpens the counterfactual anchor without mechanism interaction (V-03, V-04, V-05)**

The inertia preamble (V-03 axis, carried into V-04 and V-05) names the alternative artifact the echo is not: the findings summary. This converts the "Why passive observation missed this" field from an open-ended explanation ("name the gap") to a contrastive claim ("state why a findings summary would not report this item"). The counterfactual test gains a concrete reference artifact. This is a preamble property, not a process mechanism — it does not interact with the manifest structure, gate order, or pair inspections. V-04 confirms this: role-sequence change (V-01 axis) and inertia framing (V-03 axis) compose without degradation because they target non-overlapping phases of the process.

**Signal 3 — C-29 passes uniformly in first full-round confirmation**

R11 established C-29 as a single-variation demonstration (V-02 only). R12 confirms C-29 across all five variations — the first round in which all five templates independently populate Composability-claim in canonical taxonomy examples. The mechanism is stable: once PREREQUISITE and ESTABLISHES examples include the Composability-claim field (established in R11 V-02), the property is inherited uniformly by all subsequent variations. Second confirmation in R13 will enable proven promotion in v12.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Synthesis separation extends to three manifest layers: C-27 (live inspection), C-29 (illustration examples), C-30 (pre-populated baseline) — V-05 closes the final gap by populating Composability-claim in the BASELINE row, providing synthesis calibration at every level", "Inertia framing sharpens C-10 enforcement by naming the findings summary as the concrete alternative artifact, converting the passive-observation counterfactual from open-ended to contrastive without any manifest or gate interaction"]}
```
