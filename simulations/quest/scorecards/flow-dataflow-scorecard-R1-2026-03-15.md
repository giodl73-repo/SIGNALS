# flow-dataflow Rubric Scoring — Round 1

> **Note**: Trace artifact marked `placeholder` — scoring each variation as a *prompt design evaluation*: does the variation's instructions structurally guarantee rubric-passing outputs? V-05 was not included in the prompt; evaluation covers V-01 through V-04. V-04 is truncated (Phase 2 instructions cut off after the staleness targets table).

---

## V-01 — Table-first format

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Data lineage chain | **PASS** | Per-entity stage table + named source/destination; Step 3 enforces unbroken chain |
| C-02 | Boundary error handling | **PASS** | "Error Handling" column required; `NO HANDLING — risk accepted` mandated explicitly |
| C-03 | Loss point identification | **PASS** | Loss point register Step 4: "at least one row per pipeline stage"; named failure required |
| C-04 | Schema state at each stage | **PASS** | "Schema In / Schema Out" columns; "pass-through" required if unchanged |
| C-05 | Latency characterization | **PASS** | Latency column; "Never leave blank" enforced |
| C-06 | Stale data windows | **PASS** | Step 5: normal-operation + failure-mode stale window both required |
| C-07 | Domain framing | **PASS** | Step 2 explicitly rejects "records"/"data"; pushes for entity names |
| C-08 | Recovery prescriptions | **PARTIAL** | Loss register has "Recovery Path" column, but no explicit tie from `NO HANDLING` flags to recovery prescriptions |
| C-09 | Pattern trade-off | **PASS** | Step 6: named alternative, 2 dimensions, 1 quantified in domain terms |

**Scores:**
- Essential: 4/4 → 60 pts
- Recommended: 3/3 → 30 pts
- Aspirational: C-08 partial (2.5) + C-09 (5) = 7.5 pts

**Composite: 97.5** | All essential: ✅

---

## V-02 — Domain expert leads

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Data lineage chain | **PASS** | Systems pass traces per entity through all stages source → destination |
| C-02 | Boundary error handling | **PASS** | "at every inter-stage handoff, name the mechanism or explicitly flag it as unhandled" |
| C-03 | Loss point identification | **PASS** | "A data loss point for each stage — not generic, named" |
| C-04 | Schema state at each stage | **PASS** | "schema at stage entry/exit" per entity per stage |
| C-05 | Latency characterization | **PARTIAL** | "latency of the stage" mentioned but no "never blank" enforcement or completion check |
| C-06 | Stale data windows | **PASS** | Normal-operation + failure-mode stale window; compared against domain-pass targets |
| C-07 | Domain framing | **PASS** | Domain pass anchors entity vocabulary before any tracing begins |
| C-08 | Recovery prescriptions | **PARTIAL** | Synthesis addresses unresolved gaps but only for gap-vs-target mismatches, not every loss scenario |
| C-09 | Pattern trade-off | **PASS** | Named alternative, 2 dimensions, 1 quantified against a domain target |

**Scores:**
- Essential: 4/4 → 60 pts
- Recommended: C-05 partial → (2.5+5+5)/30 × 30 = 25 pts
- Aspirational: C-08 partial (2.5) + C-09 (5) = 7.5 pts

**Composite: 92.5** | All essential: ✅

---

## V-03 — Lifecycle phase gates

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Data lineage chain | **PASS** | Phase 1 inventories source/destination; Phase 2 traces every entity × stage |
| C-02 | Boundary error handling | **PASS** | Phase 3: named mechanism or `NO HANDLING — risk accepted`; completion check enforces it |
| C-03 | Loss point identification | **PASS** | Phase 3: "at least one concrete data loss scenario" per stage; completion check: every stage checked |
| C-04 | Schema state at each stage | **PASS** | Phase 2: schema at entry, transformation, schema at exit; "pass-through" explicitly required |
| C-05 | Latency characterization | **PASS** | Phase 2: latency per row; completion check: "Every row has a latency annotation (not blank)" |
| C-06 | Stale data windows | **PASS** | Phase 3: normal-operation and failure-mode stale window; completion check enforces both |
| C-07 | Domain framing | **PASS** | Phase 1 completion check: "Every entity has a domain name (not just 'record' or 'data')" — hard gate |
| C-08 | Recovery prescriptions | **PASS** | Phase 4: "For every NO HANDLING flag AND every loss scenario from Phase 3: name the mechanism and where it applies" — exhaustively tied |
| C-09 | Pattern trade-off | **PASS** | Phase 4: named alternative, 2 dimensions, 1 quantified; completion check enforces it |

**Scores:**
- Essential: 4/4 → 60 pts
- Recommended: 3/3 → 30 pts
- Aspirational: C-08 (5) + C-09 (5) = 10 pts

**Composite: 100** | All essential: ✅

---

## V-04 — Combined: table-first + domain expert leads *(truncated)*

Phase 2 (systems trace + risk) is cut off after the staleness targets table. Scoring what is available:

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Data lineage chain | **PARTIAL** | Phase 1 entity register establishes scope; Phase 2 trace instructions absent |
| C-02 | Boundary error handling | **FAIL** | Phase 2 not shown; no error handling instructions visible |
| C-03 | Loss point identification | **FAIL** | Not shown |
| C-04 | Schema state at each stage | **FAIL** | Phase 2 absent |
| C-05 | Latency characterization | **PARTIAL** | Phase 1 has a latency targets table; Phase 2 trace enforcement absent |
| C-06 | Stale data windows | **PARTIAL** | Phase 1 staleness targets table present; Phase 2 trace enforcement absent |
| C-07 | Domain framing | **PASS** | Entity register explicitly rejects "record"/"data"; strongest domain anchoring of all variants |
| C-08 | Recovery prescriptions | **FAIL** | Not shown |
| C-09 | Pattern trade-off | **FAIL** | Not shown |

**Scores (provisional):**
- Essential: 1/4 → 15 pts
- Recommended: ~12.5 pts (partial on 2 of 3)
- Aspirational: 0 pts

**Composite: ~27.5 (incomplete — not rankable)** | All essential: ❌

---

## Rankings (complete variations only)

| Rank | Variation | Composite | All Essential |
|------|-----------|-----------|---------------|
| 1 | **V-03** — Phase gates | **100** | ✅ |
| 2 | **V-01** — Table-first | **97.5** | ✅ |
| 3 | **V-02** — Domain expert leads | **92.5** | ✅ |
| — | V-04 | ~27.5 (truncated) | ❌ |
| — | V-05 | not provided | — |

---

## Excellence Signals — V-03

**What made V-03 the top scorer:**

1. **Phase gates with binary completion checklists** — Each phase ends with checkboxes that must all be checked before the next phase begins. This converts "hoped-for" coverage into a hard gate. A blank latency cell or missing domain name can't slip through because the checklist fails first.

2. **Exhaustive recovery tying in Phase 4** — The instruction explicitly says "For every NO HANDLING flag AND every loss scenario from Phase 3." The word "every" + "AND" closes the gap that partial versions left open: V-01 only had a recovery column in the loss register; V-02 only addressed gap-vs-target mismatches. V-03 demands a prescription for each unhandled boundary *and* each loss point.

3. **Completion checks as a forcing function for C-08** — The Phase 4 completion check ("Every unhandled boundary has a recovery prescription / Every loss scenario has a recovery prescription") turns C-08 from aspirational to structural. The model must produce evidence before advancing, not backfill it.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["phase-gate completion checklist: binary go/no-go checks between phases prevent criterion skipping and turn aspirational coverage into a structural gate", "exhaustive recovery tying: explicitly scope recovery prescriptions to EVERY unhandled boundary AND every loss scenario, not just gap-vs-target mismatches"]}
```
