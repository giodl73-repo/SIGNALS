## topic-plan Round 4 Scorecard

### V-01: Formal Vocabulary Contract (C-17)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Read strategy.md | PASS | Step 1 reads strategy.md, fills Schema A with file path/date, requires direct quote |
| C-02 | Signal inventory | PASS | Schema C all 9 namespaces, Schema D namespace audit rows |
| C-03 | Delta detection | PASS | Schema D templated sentence with STRATEGY DATE, NEW/PRIOR split |
| C-04 | Typed change proposals | PASS | Schema E with ADD/REMOVE/REPRIORITIZE, silence not permitted |
| C-05 | Confirmation gate | PASS | Step 6 PENDING CONFIRMATION with YES/NO/REVISED stop |
| C-06 | Evidence citation | PASS | Evidence artifact column in Schema E |
| C-07 | Before/after diff | PASS | Schema F Before/After structure |
| C-08 | Inertia justification | PASS | "vs. NO CHANGE" column requires naming specific risk/gap |
| C-09 | Type-labeled null declarations | PASS | ADDITIONS/REMOVALS/REPRIORITIZATIONS labeled separately |
| C-10 | Conflict detection | FAIL | No conflict audit phase or schema |
| C-11 | Required-cell table schemas | PASS | All schemas pre-filled with `??` |
| C-12 | In-phase stop gates | PARTIAL | Step 1 and Step 3 have gates; Step 2/4 have scans but no "do not proceed" language |
| C-13 | Mandatory column enforcement | FAIL | No "mandatory" header label on any structural column |
| C-14 | Explicit placeholder tokens | PASS | Every cell initialized `??` per vocabulary contract |
| C-15 | Counted-total delta summary | PASS | Schema D templated sentence with integer slots |
| C-16 | Hedge-phrase disqualification | FAIL | "vs. NO CHANGE" specifies what to write but does not ban specific phrases by name |
| C-17 | Two-tier sentinel vocabulary | PASS | Standalone VOCABULARY CONTRACT block defines `??` (OPEN OBLIGATION) / `--` (CLOSED DECISION) with three named violations |
| C-18 | Pre-signal defense register | FAIL | No defense register of any kind |
| C-19 | Integer-enforcement gate language | FAIL | "integer count" is used but no banned-form list labeled "gate failure" |
| C-20 | Sequential phase-linked stop gates | FAIL | Uses Steps, not Phases; no consistent "Do not advance to Step N" language |

**Essential**: 5/5 → 60  
**Recommended**: 3/3 → 30  
**Aspirational**: C-09, C-11, C-14, C-15, C-17 = 5 PASS + C-12 PARTIAL = 5.5/12 → **4.6**

**V-01 Total: 95**

---

### V-02: Pre-Signal Defense Register as Phase 0 (C-18)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Read strategy.md | PASS | Phase 0 reads strategy.md, records file/date/dimensions, requires direct quote |
| C-02 | Signal inventory | PASS | Phase 1 all 9 namespace rows with integer counts |
| C-03 | Delta detection | PASS | Phase 2 delta summary sentence with STRATEGY DATE, NEW/PRIOR |
| C-04 | Typed change proposals | PASS | Phase 4 ADD/REMOVE/REPRIORITIZE with null declarations per type |
| C-05 | Confirmation gate | PASS | Phase 5 PENDING CONFIRMATION YES/NO/REVISED |
| C-06 | Evidence citation | PASS | "Evidence artifact: [NEW filename]" column in Phase 4 table |
| C-07 | Before/after diff | PASS | Before/after diff table in Phase 4 |
| C-08 | Inertia justification | PASS | "Defense defeated" column must cite Phase 0 row number — stronger than generic inertia |
| C-09 | Type-labeled null declarations | PASS | ADDITIONS/REMOVALS/REPRIORITIZATIONS each separately labeled with Phase 0 reference |
| C-10 | Conflict detection | FAIL | No conflict detection |
| C-11 | Required-cell table schemas | PASS | Structured tables in every phase |
| C-12 | In-phase stop gates | PASS | Every phase uses "Do not advance to Phase N" with explicit next-phase number |
| C-13 | Mandatory column enforcement | PARTIAL | "Defense defeated" has enforcement rules; no "mandatory" header label |
| C-14 | Explicit placeholder tokens | FAIL | Uses `[fill]` notation, no `??`/`--` sentinel vocabulary |
| C-15 | Counted-total delta summary | PASS | Templated sentence with integer counts "[N] and [M] must be integers" |
| C-16 | Hedge-phrase disqualification | PASS | Phase 4 explicitly names and bans: "New evidence found is not acceptable / Evidence is compelling is not acceptable" |
| C-17 | Two-tier sentinel vocabulary | FAIL | No vocabulary contract |
| C-18 | Pre-signal defense register | PASS | Phase 0 closes strategy.md before any artifact search; proposals must cite Phase 0 row number |
| C-19 | Integer-enforcement gate language | FAIL | "[N] and [M] must be integers" — quality instruction, not a named gate failure with banned form list |
| C-20 | Sequential phase-linked stop gates | PASS | Every phase gate: "Do not advance to Phase N without passing this gate" — complete chain Phase 0–6 |

**Essential**: 5/5 → 60  
**Recommended**: 3/3 → 30  
**Aspirational**: C-09, C-11, C-12, C-15, C-16, C-18, C-20 = 7 PASS + C-13 PARTIAL = 7.5/12 → **6.25**

**V-02 Total: 96**

---

### V-03: Sequential Phase-Linked Gates + Integer-Enforcement Gate Language (C-19 + C-20)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Read strategy.md | PASS | Phase 1 reads strategy.md, records file/date/dimensions, requires quote |
| C-02 | Signal inventory | PASS | Phase 2 all 9 namespace rows with integer counts |
| C-03 | Delta detection | PASS | Phase 3 DELTA SUMMARY BLOCK with STRATEGY DATE, NEW/PRIOR split |
| C-04 | Typed change proposals | PASS | Phase 5 ADD/REMOVE/REPRIORITIZE with null declarations per type |
| C-05 | Confirmation gate | PASS | Phase 6 PENDING CONFIRMATION YES/NO/REVISED |
| C-06 | Evidence citation | PASS | Evidence artifact column, only NEW filenames permitted |
| C-07 | Before/after diff | PASS | Before/after diff table in Phase 5 |
| C-08 | Inertia justification | PASS | "vs. NO CHANGE" column with specific consequence required |
| C-09 | Type-labeled null declarations | PASS | ADDITIONS/REMOVALS/REPRIORITIZATIONS separately labeled |
| C-10 | Conflict detection | FAIL | No conflict detection |
| C-11 | Required-cell table schemas | PASS | Tables throughout with `[fill]` notation |
| C-12 | In-phase stop gates | PASS | Every phase: "Do not advance to Phase N without passing this gate" — all 7 phases chained |
| C-13 | Mandatory column enforcement | PARTIAL | "vs. NO CHANGE" has banned phrases but no "mandatory" column header |
| C-14 | Explicit placeholder tokens | FAIL | Uses `[fill]` notation, no `??`/`--` vocabulary |
| C-15 | Counted-total delta summary | PASS | DELTA SUMMARY BLOCK with templated sentence at Phase 3 |
| C-16 | Hedge-phrase disqualification | PASS | Phase 5 explicitly lists and bans 6 phrases: "no change needed / compelling reason / clearly warranted / obviously beneficial / update is warranted / the strategy benefits from this" |
| C-17 | Two-tier sentinel vocabulary | FAIL | No vocabulary contract |
| C-18 | Pre-signal defense register | FAIL | No defense register |
| C-19 | Integer-enforcement gate language | PASS | INTEGER ENFORCEMENT RULE at Phase 3: "Writing 'a few', 'several', 'some', 'multiple', 'many'... is a gate failure" |
| C-20 | Sequential phase-linked stop gates | PASS | Every gate says "Do not advance to Phase N+1 without passing this gate" — no exceptions, Phase 1–7 |

**Essential**: 5/5 → 60  
**Recommended**: 3/3 → 30  
**Aspirational**: C-09, C-11, C-12, C-15, C-16, C-19, C-20 = 7 PASS + C-13 PARTIAL = 7.5/12 → **6.25**

**V-03 Total: 96**

---

### V-04: Vocabulary Contract + Defense Register (C-17 + C-18)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Read strategy.md | PASS | Phase 0 reads strategy.md, fills STRATEGY FILE/DATE, quotes sentence |
| C-02 | Signal inventory | PASS | Phase 1 all 9 namespace rows with `??` initialized cells |
| C-03 | Delta detection | PASS | Phase 2 DELTA SUMMARY with STRATEGY DATE, NEW/PRIOR split |
| C-04 | Typed change proposals | PASS | Phase 4 ADD/REMOVE/REPRIORITIZE; null declarations use `--` CLOSED DECISION per type |
| C-05 | Confirmation gate | PASS | Phase 5 PENDING CONFIRMATION YES/NO/REVISED |
| C-06 | Evidence citation | PASS | Evidence artifact column in Phase 4 table |
| C-07 | Before/after diff | PASS | Before/after diff table in Phase 4 |
| C-08 | Inertia justification | PASS | "Defense defeated" must cite Phase 0 row number — evidence-based inertia linkage |
| C-09 | Type-labeled null declarations | PASS | ADD/REMOVE/REPRIORITIZE null declarations each use `--` CLOSED DECISION with Phase 0 row reference |
| C-10 | Conflict detection | FAIL | No conflict detection |
| C-11 | Required-cell table schemas | PASS | All tables `??`-initialized per VOCABULARY CONTRACT |
| C-12 | In-phase stop gates | PASS | Every phase gate: "Do not advance to Phase N" — complete chain Phase 0–6 |
| C-13 | Mandatory column enforcement | PARTIAL | "Defense defeated" TOKEN LEFT OPEN enforcement present; no "mandatory" header label |
| C-14 | Explicit placeholder tokens | PASS | Every cell initialized `??`; VOCABULARY CONTRACT defines both `??` and `--` |
| C-15 | Counted-total delta summary | PASS | Phase 2 templated sentence; "[N] and [M] must be integers" |
| C-16 | Hedge-phrase disqualification | PARTIAL | Names 2 banned phrases in "Defense defeated": "New evidence found is not acceptable / Evidence is compelling is not acceptable" — partial ban list |
| C-17 | Two-tier sentinel vocabulary | PASS | VOCABULARY CONTRACT block defines `??` (OPEN OBLIGATION) and `--` (CLOSED DECISION) with TOKEN LEFT OPEN and PREMATURE CLOSURE named violations |
| C-18 | Pre-signal defense register | PASS | Phase 0 closes strategy.md before artifact search; defense register committed with `??` cells; proposals cite Phase 0 row # |
| C-19 | Integer-enforcement gate language | FAIL | "[N] and [M] must be integers" — no banned form list, no "gate failure" language |
| C-20 | Sequential phase-linked stop gates | PASS | Every gate: "Do not advance to Phase N without passing this gate" — consistent Phase 0–6 |

**Essential**: 5/5 → 60  
**Recommended**: 3/3 → 30  
**Aspirational**: C-09, C-11, C-12, C-14, C-15, C-17, C-18, C-20 = 8 PASS + C-13 PARTIAL + C-16 PARTIAL = 9/12 → **7.5**

**V-04 Total: 98**

---

### V-05: Full Combination (C-17 + C-18 + C-19 + C-20)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Read strategy.md | PASS | Phase 0 fills Schema A (file path, STRATEGY DATE, dimensions), requires direct quote |
| C-02 | Signal inventory | PASS | Schema C all artifacts; Schema D all 9 namespaces with integer counts |
| C-03 | Delta detection | PASS | Schema E DELTA SUMMARY BLOCK with STRATEGY DATE named, NEW/PRIOR split from Schema A |
| C-04 | Typed change proposals | PASS | Schema G ADD/REMOVE/REPRIORITIZE; null declarations with `--` CLOSED DECISION per type |
| C-05 | Confirmation gate | PASS | Phase 5 PENDING CONFIRMATION YES/NO/REVISED; final TOKEN LEFT OPEN scan before display |
| C-06 | Evidence citation | PASS | Schema G Evidence artifact column; only Schema E NEW list artifacts permitted |
| C-07 | Before/after diff | PASS | Schema H Before/After diff, one row per Schema G proposal |
| C-08 | Inertia justification | PASS | Schema G "Defense defeated" must cite Schema B row number and defense argument |
| C-09 | Type-labeled null declarations | PASS | ADD/REMOVE/REPRIORITIZE each have `--` CLOSED DECISION null declaration with Schema B row reference |
| C-10 | Conflict detection | PASS | Schema I conflict audit table; typed null form "CONFLICT AUDIT: `--` -- no contradictions detected" |
| C-11 | Required-cell table schemas | PASS | Schemas A–I all pre-committed with `??` initialization; no schema may be replaced by prose |
| C-12 | In-phase stop gates | PASS | Every phase: "Do not advance to Phase N without passing this gate" — Phase 0–6, no exceptions |
| C-13 | Mandatory column enforcement | PARTIAL | "Defense defeated" TOKEN LEFT OPEN enforcement + 7-item BANNED phrases list; no "mandatory" header label |
| C-14 | Explicit placeholder tokens | PASS | Every cell in Schemas A–I starts `??`; VOCABULARY CONTRACT defines both tokens with three named violations |
| C-15 | Counted-total delta summary | PASS | Schema E templated sentence; INTEGER ENFORCEMENT RULE at Phase 2 names exact counts |
| C-16 | Hedge-phrase disqualification | PASS | Phase 4 BANNED phrases list: "new evidence found / evidence is compelling / no change needed / clearly warranted / update is warranted / the strategy benefits from this / obviously beneficial" — 7 banned forms, each row containing them is removed |
| C-17 | Two-tier sentinel vocabulary | PASS | VOCABULARY CONTRACT before all phases: `??` (OPEN OBLIGATION) / `--` (CLOSED DECISION) with TOKEN LEFT OPEN, PREMATURE CLOSURE, CHAIN SKIP named violations |
| C-18 | Pre-signal defense register | PASS | Phase 0 with Schema B committed before Phase 1; "Do not open any signal artifact before Schema B is complete"; proposals cite Schema B row # |
| C-19 | Integer-enforcement gate language | PASS | INTEGER ENFORCEMENT RULE at Phase 2: "Writing 'a few', 'several', 'some', 'multiple', 'many', or any other non-integer value... is a gate failure. Non-integer counts are not a quality concern — they are a named, detectable failure condition." |
| C-20 | Sequential phase-linked stop gates | PASS | Every stop gate: "Do not advance to Phase N without passing this gate" — Phase 0–6 complete chain |

**Essential**: 5/5 → 60  
**Recommended**: 3/3 → 30  
**Aspirational**: C-09, C-10, C-11, C-12, C-14, C-15, C-16, C-17, C-18, C-19, C-20 = 11 PASS + C-13 PARTIAL = 11.5/12 → **9.6**

**V-05 Total: 100**

---

## Ranking

| Variation | Essential | Recommended | Aspirational | **Total** | Golden? |
|-----------|-----------|-------------|--------------|-----------|---------|
| V-05 | 5/5 | 3/3 | 11.5/12 | **100** | YES |
| V-04 | 5/5 | 3/3 | 9/12 | **98** | YES |
| V-02 | 5/5 | 3/3 | 7.5/12 | **96** | YES |
| V-03 | 5/5 | 3/3 | 7.5/12 | **96** | YES |
| V-01 | 5/5 | 3/3 | 5.5/12 | **95** | YES |

All five variations pass all essential criteria and all three recommended criteria. The spread is driven entirely by aspirational coverage.

---

## Excellence Signals (V-05)

**1. CHAIN SKIP as a third vocabulary contract violation**  
V-01 and V-04 define TOKEN LEFT OPEN and PREMATURE CLOSURE. V-05 adds CHAIN SKIP — "advancing to Phase N+1 without passing Phase N's stop gate." This elevates phase-sequence enforcement to contract level. A skipped gate is not just a missed instruction; it is a named breach of the vocabulary contract, making it catchable in the same scan that checks for `??` and `--` misuse.

**2. Alphabetic schema reference system (Schema A–I)**  
V-05 assigns permanent letter labels to all pre-committed schemas and cross-references them by name throughout phases: "fill Schema F... For WEAKENS rows from Schema F... Schema B row #." This creates an unambiguous information architecture that survives long-context drift. "Schema B row #" is always the defense register regardless of which phase is active; no restating of what was meant by "Phase 0 register" or "the earlier table."

**3. TOKEN LEFT OPEN scan at every phase gate**  
Rather than a single final scan at the confirmation gate, V-05 instructs a TOKEN LEFT OPEN check at each phase exit. Violations are caught locally before they propagate to later phases, eliminating the risk that a `??` present in Schema C becomes a silently broken reference in Schema F.

**4. Typed null form for conflict detection (Schema I)**  
Conflict detection (C-10) is given a dedicated pre-committed schema (Schema I) with a typed null form embedded: `CONFLICT AUDIT: \`--\` -- no contradictions detected between NEW artifacts on any strategy dimension.` The null form uses the VOCABULARY CONTRACT token (`--` = CLOSED DECISION) and names the scope of what was checked. Every prior variation that omitted conflict detection left a silent gap; V-05 makes the gap detectable at output-scan time.

---

## New Patterns Found

Two patterns present in V-05 not yet captured in C-01 through C-20:

1. **CHAIN SKIP as vocabulary-contract violation** — phase-sequence enforcement elevated to the same level as cell-level sentinel violations (TOKEN LEFT OPEN, PREMATURE CLOSURE), making phase skipping a named contract breach rather than a procedural omission.

2. **Alphabetic schema cross-reference system** — pre-committed output schemas assigned permanent letter labels (Schema A–I) cross-referenced by name throughout all phases, creating a persistent information architecture that prevents reference drift under long context.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["CHAIN SKIP as vocabulary-contract violation — phase-sequence enforcement elevated to contract level alongside TOKEN LEFT OPEN and PREMATURE CLOSURE, making gate-skipping a named detectable breach rather than a missed instruction", "Alphabetic schema cross-reference system — pre-committed schemas labeled Schema A through I and referenced by letter throughout all phases, creating persistent unambiguous information architecture that survives long-context drift"]}
```
