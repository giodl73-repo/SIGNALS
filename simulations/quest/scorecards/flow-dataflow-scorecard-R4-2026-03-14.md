## flow-dataflow — Round 4 Scoring

---

### V-01 — Artifact-labeled dependency chain

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Data lineage chain | **PASS** | ROLE 3 requires STAGE N blocks with Schema in/out at every stage; no destination without named origin |
| C-02 | Boundary error handling | **PASS** | BOUNDARY CHECK block requires `Error handling: [mechanism] OR [NONE — flag]`; silence prohibited |
| C-03 | Data loss point identification | **PASS** | Every STAGE block requires `Loss point: [specific condition — name the data item and failure mechanism]`; generic language explicitly barred |
| C-04 | Schema state at each stage | **PASS** | `Schema in:` and `Schema out:` required in every stage block; rename/drop/type change must be listed |
| C-05 | Latency characterization | **PASS** | `Latency:` field in every STAGE block + `Latency this boundary:` in every BOUNDARY CHECK |
| C-06 | Stale data windows | **PASS** | STALE ANALYSIS table with normal-op row + failure-mode row; threshold vs elapsed; both addressed separately |
| C-07 | Domain framing | **PASS** | ROLE 1 names entities; ROLE 2 carries without substitution; ROLE 3 opens "Tracing against ARTIFACT: DOMAIN CONTEXT entity vocabulary" |
| C-08 | Recovery prescriptions | **PASS** | ROLE 5 prescribes named pattern per NONE boundary; incumbent failure vocabulary explicitly closed |
| C-09 | Pattern trade-off | **PASS** | ROLE 5 requires named alternative + two-dimension comparison table; incumbent relevance column required |
| C-10 | Pre-trace domain context gate | **PASS** | ARTIFACT: DOMAIN CONTEXT produced by ROLE 2 before ROLE 3 begins; carries terms from ROLE 1 verbatim |
| C-11 | Interleaved boundary gates | **PASS** | "After each consecutive stage pair, before writing the next stage, insert this boundary block" — structural deferral prohibition |
| C-12 | Domain entity exposure per boundary | **PASS** | `Entity: [exact entity name from ARTIFACT: DOMAIN CONTEXT — "data" or "records" fails]` |
| C-13 | Pre-declared staleness contract | **PASS** | Staleness threshold declared in DOMAIN CONTEXT (ROLE 2) before stages; threshold derivation from F-02 required |
| C-14 | Additive elapsed time calculation | **PASS** | `Elapsed (cumulative):` required field in every BOUNDARY CHECK; STALE ANALYSIS table cites "Elapsed (cumulative) from final BOUNDARY CHECK in Role 3" |
| C-15 | Incumbent baseline | **PASS** | ARTIFACT: INCUMBENT BASELINE in ROLE 1; ROLE 5 trade-off table requires ARTIFACT: INCUMBENT BASELINE column; loop explicitly closed |
| C-16 | Cross-role reference chain | **PASS** | Every role opens with named citation: "Drawing from ARTIFACT: INCUMBENT BASELINE:", "Tracing against ARTIFACT: DOMAIN CONTEXT entity vocabulary:", "Evaluating against ARTIFACT: DOMAIN CONTEXT threshold and Elapsed (cumulative) from final BOUNDARY CHECK in Role 3:", "Closing gaps identified in Role 3 BOUNDARY CHECKs and Role 1 ARTIFACT: INCUMBENT BASELINE failure vocabulary:" |
| C-17 | Immutability declaration | **PASS** | IMMUTABLE THRESHOLD block contains "Prohibited revisions: no role after this point may adjust this value." — explicit prohibition, not merely early declaration |
| C-18 | Incremental boundary elapsed computation | **PASS** | "The `Elapsed (cumulative)` field is a required field in this block. It must be computed additively from the values already written above. Do not defer it to a post-stage summary. Do not write Stage N+1 until this block is complete." |

**Essential:** 4/4 → 60 | **Recommended:** 3/3 → 30 | **Aspirational:** 11/11 → 10

**Composite: 100** | **Golden: YES**

---

### V-02 — Numbered specification requirements

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Data lineage chain | **PASS** | Numbered requirements enforce stage trace with source → destination chain |
| C-02 | Boundary error handling | **PASS** | Boundary error handling covered by requirement (R-xx); NONE flag required |
| C-03 | Data loss point identification | **PASS** | Loss point field required per stage requirement |
| C-04 | Schema state at each stage | **PASS** | Schema in/out covered by stage requirements |
| C-05 | Latency characterization | **PASS** | Latency field required per stage requirement |
| C-06 | Stale data windows | **PASS** | Stale analysis required with normal-op and failure-mode rows |
| C-07 | Domain framing | **PASS** | R-01 requires named business entity; R-02 carries vocabulary without substitution |
| C-08 | Recovery prescriptions | **PASS** | Recovery requirement closes NONE boundaries |
| C-09 | Pattern trade-off | **PASS** | Alternative pattern section required |
| C-10 | Pre-trace domain context gate | **PASS** | DOMAIN CONTEXT section produced before stage blocks; terms re-used in subsequent content |
| C-11 | Interleaved boundary gates | **PASS** | Boundary check requirement instructs insertion between each consecutive stage pair |
| C-12 | Domain entity exposure per boundary | **PASS** | "data" / "records" barred per requirement |
| C-13 | Pre-declared staleness contract | **PASS** | R-03 declares threshold pre-stage; connects to R-01 F-02 |
| C-14 | Additive elapsed time calculation | **PASS** | R-08 field definition; cumulative total feeds stale analysis |
| C-15 | Incumbent baseline | **PASS** | R-01 INCUMBENT BASELINE referenced in trade-off comparison |
| C-16 | Cross-role reference chain | **PASS** | Citation syntax "Per R-02 DOMAIN CONTEXT" is a named reference; shown in partial prompt as "Per R-01 INCUMBENT BASELINE:" — verifiable by label |
| C-17 | Immutability declaration | **PASS** | Hypothesis explicitly states R-04 is a separate prohibition requirement from R-03 (declaration); design matches C-17 vs C-13 distinction |
| C-18 | Incremental boundary elapsed computation | **PASS** | R-08 defines elapsed field; R-09 deferral prohibition bars post-stage assembly |

**Essential:** 4/4 → 60 | **Recommended:** 3/3 → 30 | **Aspirational:** 11/11 → 10

**Composite: 99** | **Golden: YES**

> Minor reduction from 100: requirement-ID citations (R-xx) are slightly less explicit as "named artifact" targets than ARTIFACT: labels; the partial prompt confirms the pattern but full verification is unavailable.

---

### V-03 — Inertia framing: Incumbent as structural anchor

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Data lineage chain | **PASS** | Incumbent anchor implies stage-by-stage tracing |
| C-02 | Boundary error handling | **PASS** | BOUNDARY CHECK contains F-02 status field implying error annotation |
| C-03 | Data loss point identification | **PASS** | Loss points grounded in known failures (F-01) — specific by design |
| C-04 | Schema state at each stage | **PASS** | Stage trace requires schema context |
| C-05 | Latency characterization | **PASS** | F-02 status field implies latency tracking |
| C-06 | Stale data windows | **PASS** | F-02 freshness verdict drives stale analysis |
| C-07 | Domain framing | **PASS** | F-01/F-02 use specific entity names from incumbent |
| C-08 | Recovery prescriptions | **PASS** | Closing known failures from F-01/F-02 provides specific prescriptions |
| C-09 | Pattern trade-off | **PASS** | Incumbent comparison grounds trade-off |
| C-10 | Pre-trace domain context gate | **PASS** | Incumbent section precedes stages; entity vocabulary locked from F-01/F-02 |
| C-11 | Interleaved boundary gates | **PASS** | F-02 status field in every BOUNDARY CHECK implies interleaved placement |
| C-12 | Domain entity exposure per boundary | **PASS** | F-02 references specific entities from incumbent vocabulary |
| C-13 | Pre-declared staleness contract | **PASS** | F-02's time magnitude provides grounded threshold declared before stages |
| C-14 | Additive elapsed time calculation | **PARTIAL** | F-02 status verdict implies elapsed tracking but "cumulative elapsed total" as a named running sum is not explicitly required in the hypothesis; verdict field may be binary (FRESH/STALE) rather than additive |
| C-15 | Incumbent baseline | **PASS** | Incumbent is the structural anchor; referenced throughout |
| C-16 | Cross-role reference chain | **PASS** | F-01/F-02 labels create citation targets; every section "derives from or responds to F-01/F-02" satisfies named-citation requirement |
| C-17 | Immutability declaration | **FAIL** | Hypothesis focuses on inertia framing; no explicit prohibition statement on threshold revision is described. C-17 requires a structural prohibition — absent from design |
| C-18 | Incremental boundary elapsed computation | **PARTIAL** | F-02 status field may provide freshness verdict without explicitly naming a cumulative numeric field updated at each boundary |

**Essential:** 4/4 → 60 | **Recommended:** 3/3 → 30 | **Aspirational:** 9/11 → 8.18

**Composite: 98** | **Golden: YES**

---

### V-04 — Phase gates + Finance-first role sequence

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Data lineage chain | **PASS** | Finance-first role sequence traces pipeline stages |
| C-02 | Boundary error handling | **PASS** | Phase 2 gate checks boundary error fields |
| C-03 | Data loss point identification | **PASS** | Phase gate checklist requires loss point annotation |
| C-04 | Schema state at each stage | **PASS** | Phase gate checklist requires schema diff |
| C-05 | Latency characterization | **PASS** | Phase 2 gate checks elapsed fields implying latency annotations |
| C-06 | Stale data windows | **PASS** | Post-Phase 3 stale analysis required |
| C-07 | Domain framing | **PASS** | Finance domain entities in DOMAIN CONTEXT |
| C-08 | Recovery prescriptions | **PASS** | Recovery phase follows stale analysis |
| C-09 | Pattern trade-off | **PASS** | Final role covers pattern advice |
| C-10 | Pre-trace domain context gate | **PASS** | DOMAIN CONTEXT declared before Phase 2 stages |
| C-11 | Interleaved boundary gates | **PARTIAL** | "Phase 2 gate checking each boundary's elapsed field before Phase 3 begins" is ambiguous — if Phase 2 is the staging phase with inline BOUNDARY CHECKs, PASS; if Phase 2 is a post-Phase-1 gate collection, FAIL. Design description doesn't confirm inline placement |
| C-12 | Domain entity exposure per boundary | **PASS** | Finance domain vocabulary in each boundary check implied by Finance-first framing |
| C-13 | Pre-declared staleness contract | **PASS** | Threshold appears in DOMAIN CONTEXT before stages |
| C-14 | Additive elapsed time calculation | **PASS** | Phase 2 gate checks elapsed fields; cumulative total implied |
| C-15 | Incumbent baseline | **PASS** | Finance-first likely includes incumbent Finance process |
| C-16 | Cross-role reference chain | **PASS** | Role sequence creates citation chain; Finance-first structure implies each role builds on prior |
| C-17 | Immutability declaration | **PASS** | "C-17 appears in both DOMAIN CONTEXT and the gate, creating two enforcement surfaces" — explicit |
| C-18 | Incremental boundary elapsed computation | **PASS** | "Phase 2 gate checking each boundary's elapsed field" — elapsed field at each boundary enforced by gate |

**Essential:** 4/4 → 60 | **Recommended:** 3/3 → 30 | **Aspirational:** 10.5/11 → 9.55 (C-11 partial)

**Composite: 99.55 → 99** | **Golden: YES**

---

### V-05 — Table-primary (named-section fix) + Explicit C-16/C-17/C-18 fields

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Data lineage chain | **PASS** | Table-primary format covers source/stage/destination with full lineage |
| C-02 | Boundary error handling | **PASS** | Boundary table rows require error handling annotation |
| C-03 | Data loss point identification | **PASS** | Loss point row required in each stage table |
| C-04 | Schema state at each stage | **PASS** | Schema in/out rows required in stage tables |
| C-05 | Latency characterization | **PASS** | Latency row in every stage table |
| C-06 | Stale data windows | **PASS** | Stale analysis table with normal-op and failure-mode rows |
| C-07 | Domain framing | **PASS** | Named section headers carry domain vocabulary |
| C-08 | Recovery prescriptions | **PASS** | Recovery table prescribes named pattern per gap |
| C-09 | Pattern trade-off | **PASS** | Alternative pattern comparison table with incumbent reference |
| C-10 | Pre-trace domain context gate | **PASS** | Named section header `DOMAIN CONTEXT` wraps table — R3 V-02 fix applied |
| C-11 | Interleaved boundary gates | **PASS** | Required `Citing:` row in every boundary table; inline structure enforces interleaving |
| C-12 | Domain entity exposure per boundary | **PASS** | `Citing:` row names domain entity — "data"/"records" barred |
| C-13 | Pre-declared staleness contract | **PASS** | `LOCK` row in DOMAIN CONTEXT declares threshold before stages |
| C-14 | Additive elapsed time calculation | **PASS** | Named `Elapsed (cumulative)` row accumulates at each boundary table |
| C-15 | Incumbent baseline | **PASS** | Named section header `INCUMBENT BASELINE` wraps table — R3 fix; referenced in trade-off |
| C-16 | Cross-role reference chain | **PASS** | Required `Citing:` row in every boundary table is explicit named citation per C-16 |
| C-17 | Immutability declaration | **PASS** | Required `LOCK` row in DOMAIN CONTEXT provides explicit prohibition |
| C-18 | Incremental boundary elapsed computation | **PASS** | Named `Elapsed (cumulative)` row with explicit deferral prohibition — incremental at each boundary |

**Essential:** 4/4 → 60 | **Recommended:** 3/3 → 30 | **Aspirational:** 11/11 → 10

**Composite: 100** | **Golden: YES**

---

## Summary

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 | 4/4 | 3/3 | 11/11 | **100** | YES |
| V-05 | 4/4 | 3/3 | 11/11 | **100** | YES |
| V-04 | 4/4 | 3/3 | 10.5/11 | **99** | YES |
| V-02 | 4/4 | 3/3 | 11/11 | **99** | YES |
| V-03 | 4/4 | 3/3 | 9/11 | **98** | YES |

**Rank:** V-01 = V-05 > V-02 ≈ V-04 > V-03

All five variations achieve Golden (all essentials pass, composite ≥ 80). The saturation at the top indicates the rubric has been fully solved at the design level.

---

## Excellence Signals from Top Variations (V-01, V-05)

**1. Named artifact targets vs. citation references — structural asymmetry**
V-01 creates `ARTIFACT:` prefixed outputs (ARTIFACT: INCUMBENT BASELINE, ARTIFACT: DOMAIN CONTEXT) that serve as citation targets. Each subsequent role is required to open with an explicit named reference to a prior artifact. This makes C-16 verifiable by token match rather than prose judgment — a citation either names the artifact or it doesn't. V-05 achieves the same via `Citing:` row in every boundary table.

**2. Separation of declaration from prohibition as two distinct structural elements**
C-13 (pre-declaration) and C-17 (prohibition) address different model failure modes. V-01 expresses this as two distinct structural elements: the threshold line itself, then the IMMUTABLE THRESHOLD block with "Prohibited revisions: no role after this point may adjust this value." V-02 expresses it as R-03 (declaration requirement) + R-04 (prohibition requirement) — same separation, different encoding. V-03 fails here by treating early declaration as sufficient.

**3. Required inline field with deferral prohibition outperforms post-hoc requirement**
The distinction between C-14 and C-18 is where the cumulative total is computed. V-01's "Do not write Stage N+1 until this block is complete" converts C-18 into a structural gate — the output is incomplete if the field is absent. V-05's named `Elapsed (cumulative)` row achieves the same via table schema: an absent row makes the table structurally wrong, not merely incomplete.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["ARTIFACT: prefix creates machine-verifiable citation targets — C-16 satisfied by token match, not prose judgment", "Declaration requirement and prohibition requirement are structurally separate elements — C-13 and C-17 address different model failure modes and must not be collapsed", "Required named inline field with deferral prohibition converts cumulative elapsed to a structural gate — output is incomplete rather than merely non-compliant if field is absent"]}
```
