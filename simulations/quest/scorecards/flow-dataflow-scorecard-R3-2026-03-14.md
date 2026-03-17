# flow-dataflow Scorecard — Round 3

---

## V-01 — Role sequence (Domain expert seeds vocabulary before analyst traces)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Data lineage chain | **PASS** | Role 3 (Pipeline Analyst) explicitly traces source → stage(s) → destination with schema at each entry/exit |
| C-02 | Boundary error handling | **PASS** | BOUNDARY CHECK block requires `Error handling: <mechanism or "NONE">` — silence not structurally possible |
| C-03 | Data loss point identification | **PASS** | "Name at least one concrete data loss point. 'Errors may occur' does not qualify" — generic language rejected by instruction |
| C-04 | Schema state at each stage | **PASS** | "State schema at entry and exit. Mark any field rename, type change, or drop" — full diff required per stage |
| C-05 | Latency characterization | **PASS** | "Annotate latency: specific value, range, or characterization" — per stage in Role 3 block |
| C-06 | Stale data windows | **PASS** | STALE ANALYSIS derives rows from cumulative elapsed vs. pre-declared threshold — failure-mode vs. normal-mode both addressable |
| C-07 | Domain framing | **PASS** | Role 1 seeds exact entity vocabulary ("Purchase Order", "Settlement Batch") before any stage work; Role 2 carries same terms forward |
| C-08 | Recovery prescriptions | **PASS** | Role 4 provides specific prescriptions for every NONE and loss point; "Reference the incumbent failure mode from INCUMBENT BASELINE where applicable" closes C-02/C-03 loop |
| C-09 | Pattern trade-off analysis | **PASS** | Role 5 names one alternative, provides "at least two qualified or quantified trade-off dimensions," and references incumbent failure mode |
| C-10 | Pre-trace domain context gate | **PASS** | "Before any pipeline trace begins, establish the business context. Write a DOMAIN CONTEXT section" — named section required, locks entity + consumer + cadence; entity reappears in BOUNDARY CHECK (verbatim by instruction) |
| C-11 | Interleaved boundary gates | **PASS** | "After each consecutive stage pair, insert a BOUNDARY CHECK block" — inline placement enforced by structure of Role 3 instruction |
| C-12 | Domain entity exposure per boundary | **PASS** | BOUNDARY CHECK field: "Entity in transit: <domain entity name from DOMAIN CONTEXT>" with explicit exclusion "'Data' or 'records' is not an entity name" |
| C-13 | Pre-declared staleness contract | **PASS** | Role 1 requires: "State it as an explicit contract: 'Entity X must not be older than N minutes/hours at destination Y.' **This threshold is fixed. You may not revise it after Stage 1.**" — pre-commitment with explicit immutability |
| C-14 | Additive elapsed time calculation | **PASS** | BOUNDARY CHECK requires "Cumulative elapsed: <running total>" at each boundary; STALE ANALYSIS instructs "Derive every row by comparing the cumulative elapsed total from the final BOUNDARY CHECK against the declared threshold" |
| C-15 | Incumbent or manual-process baseline | **PASS** | Role 2 writes a named "INCUMBENT BASELINE section" using entity vocabulary from DOMAIN CONTEXT; Role 4 says "Reference the incumbent failure mode from INCUMBENT BASELINE where applicable"; Role 5 says "Reference at least one incumbent failure mode to ground the comparison" — full C-08/C-09 connection required by instruction |

```
Essential passed:     4 / 4   =>  (4 / 4) * 60 = 60
Recommended passed:   3 / 3   =>  (3 / 3) * 30 = 30
Aspirational passed:  8 / 8   =>  (8 / 8) * 10 = 10
                                  Composite      = 100

Golden: YES — all 4 essential pass AND composite 100 >= 80
```

---

## V-02 — Table-first boundary discipline

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Data lineage chain | **PASS** | Pass 2 STAGE blocks cover schema in → out per stage; entity flows through BOUNDARY CHECK tables |
| C-02 | Boundary error handling | **PASS** | BOUNDARY CHECK table has "Error handling: <mechanism or NONE>" column — structural, not optional |
| C-03 | Data loss point identification | **PASS** | STAGE block format requires "Loss point: <specific data loss risk — not generic>" |
| C-04 | Schema state at each stage | **PASS** | STAGE block has "Schema in / Schema out — mark renames, drops, type changes" fields |
| C-05 | Latency characterization | **PASS** | "Latency: <value or range>" required field in STAGE block |
| C-06 | Stale data windows | **PASS** | Pass 3 derives rows from "Declared SLA (Pass 1)" vs. "Cumulative elapsed (final boundary)" — Delta column forces comparison; "not independently asserted" enforced |
| C-07 | Domain framing | **PASS** | Context Table "Entity in transit: <exact business name>" propagates verbatim into every BOUNDARY CHECK "Entity in transit" field |
| C-08 | Recovery prescriptions | **PASS** | Recovery Prescriptions covers every NONE and loss point; incumbent failure mode analogues required explicitly |
| C-09 | Pattern trade-off analysis | **PASS** | Two-row comparison table with named alternative; "Reference at least one incumbent failure mode to anchor the comparison" |
| C-10 | Pre-trace domain context gate | **FAIL** | Content present (entity, consumer, cadence all locked in Pass 1 Context Table), but the output section is named "Pass 1 — Context Table" not "DOMAIN CONTEXT." Criterion requires "A DOMAIN CONTEXT section appears." Named section requirement not met. |
| C-11 | Interleaved boundary gates | **PASS** | "insert between every consecutive stage pair... A trailing BOUNDARY SUMMARY after all stages does not satisfy this requirement" — inline enforcement explicit |
| C-12 | Domain entity exposure per boundary | **PASS** | BOUNDARY CHECK table requires "Entity in transit: <entity name from Pass 1 Context Table>" |
| C-13 | Pre-declared staleness contract | **PASS** | "Staleness SLA" row in Context Table is pre-declared; "The Staleness SLA row is a pre-declared contract. It cannot change after this table is written"; Pass 3 derives from this row — post-hoc assertion excluded |
| C-14 | Additive elapsed time calculation | **PASS** | BOUNDARY CHECK table has "Cumulative elapsed so far: <running total from Stage 1 through this boundary>"; Pass 3 Stale Analysis Table compares against this cumulative total directly |
| C-15 | Incumbent or manual-process baseline | **FAIL** | Context Table has "Incumbent process" (one sentence) and "Incumbent failure mode" (one concrete failure) rows, and both are referenced in recovery and trade-off — but the criterion requires "a named baseline section." Table rows within a context header are not a named baseline section. Format requirement not met. |

```
Essential passed:     4 / 4   =>  (4 / 4) * 60 = 60
Recommended passed:   3 / 3   =>  (3 / 3) * 30 = 30
Aspirational passed:  6 / 8   =>  (6 / 8) * 10 = 7.5
                                  Composite      = 97.5

Golden: YES — all 4 essential pass AND composite 97.5 >= 80
```

---

## V-03 — Inertia framing (Incumbent baseline as structural anchor)

**Status: Incomplete — prompt body not provided.** Only the axis label and hypothesis are present; the prompt template was not generated this round.

Hypothesis inference: V-03 would foreground the incumbent process as the primary narrative frame, with the pipeline presented as a response to specific named failures. This design would strongly drive C-15, C-08, C-09, and C-03. Based on the hypothesis alone, it likely produces loss points grounded in known incumbent failures (a strength over template-fill approaches). Unknown: whether C-13 (pre-declared staleness contract) and C-14 (cumulative elapsed) are explicitly enforced — the inertia framing hypothesis does not address these directly. **Not scorable this round.**

---

## Rankings

| Rank | Variation | Composite | Golden |
|------|-----------|-----------|--------|
| 1 | V-01 — Role sequence | **100** | YES |
| 2 | V-02 — Table-first | **97.5** | YES |
| 3 | V-03 — Inertia framing | — | not scored |

---

## Excellence Signals — from V-01

**What made V-01 score 100 where V-02 reached 97.5:**

V-01 hit C-10 and C-15 because it produced *named sections* ("DOMAIN CONTEXT", "INCUMBENT BASELINE") rather than table rows. The naming is not cosmetic — rubric criteria C-10 and C-15 are graded against section presence. V-02's table-first approach optimized column-contract discipline at the cost of section identity.

Three patterns stood out that have not been captured in prior rubric criteria:

**1. Explicit cross-role reference obligation** — V-01 instructs each role to cite prior roles' outputs by name: Role 3 uses Role 1's vocabulary; Role 4 cites Role 2's failure modes ("This failure mode also occurred in the incumbent when X; the mitigation is Y"); Role 5 anchors trade-offs in Role 2's named failures. This creates a *dependency chain across roles* that closes vocabulary drift between sections without post-hoc patching. Neither C-07, C-12, nor C-15 individually captures this chaining behavior — they check outcomes, not the mechanism that produces them.

**2. Immutability declaration as a stronger form of pre-commitment** — C-13 requires pre-declaration of the staleness threshold. V-01 goes further: "This threshold is fixed. You may not revise it after Stage 1." The explicit prohibition on revision is not the same as asking for pre-declaration — it anticipates and forecloses the model behavior of adjusting the threshold post-trace to make the analysis appear consistent. This wording pattern is a distinct technique: *constraining future self*, not just requesting an earlier action.

**3. Cumulative elapsed as required boundary field (incremental rather than post-hoc)** — V-01 and V-02 both enforce cumulative elapsed in the BOUNDARY CHECK block. The effect: the running total is computed incrementally as a *side effect of writing each boundary*, making it impossible to skip or fabricate after the stages are written. A prompt that asks for a cumulative total in a post-stage SUMMARY section allows the model to add up selective latencies retroactively. The inline field pattern prevents this structurally.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["cross-role reference chain: instructing each role to cite prior roles outputs by name closes vocabulary drift without post-hoc patching", "immutability declaration stronger than pre-declaration alone: explicit prohibition on revising the threshold after Stage 1 forecloses model behavior of adjusting to fit the analysis", "incremental cumulative elapsed as required boundary field makes running total a side-effect of writing each boundary rather than a retroactive sum"]}
```
