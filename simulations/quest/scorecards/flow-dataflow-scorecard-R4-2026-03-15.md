## flow-dataflow Round 4 Scorecard

**Rubric version**: v3 (C-01 through C-14)
**Variations scored**: V-01 through V-05

---

### Preliminary: Axis Coverage Baseline

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| Phrasing register | conversational | imperative | imperative | imperative | imperative |
| Structural tables (C-04 / schema) | none | STAGE TRACE TABLE | none | none | per-stage schema-diff |
| Structural tables (C-02 / boundary) | none | BOUNDARY TABLE | none | none | none (gates) |
| Structural tables (C-03 / loss points) | none | LOSS-POINT RECOVERY TABLE | none | none | none |
| Inline boundary gates | none | none | none | yes (B1->2 … B4->5) | yes (B1->2 … B4->5) |
| Incumbent baseline format | prose hint | prose section | 4-col named table | prose section | 4-col named table |
| Per-row citation requirement | none | no | yes (Manual Step value) | no (verbatim name) | yes (Manual Step value) |
| C-13 structural surfaces | 0 | 3 (all tables) | 0 | 1 (gate → C-02) | 2 (table → C-04, gate → C-02) |

---

### V-01 — Phrasing Register: Conversational / Descriptive

**Scenario**: Retail markdown pipeline (5 stages)

| Criterion | Tier | Pass / Partial / Fail | Evidence |
|-----------|------|-----------------------|----------|
| C-01 | E | PASS | Five stages with source ⇒ destination; "what comes in / what comes out" requested per stage |
| C-02 | E | PASS | "if there's genuinely no handling, say so" — explicit silence-fails equivalent for no-handling case |
| C-03 | E | PARTIAL | "try to name a concrete failure mode" per stage — advisory "try to" permits stage-level omissions that imperative phrasing would block |
| C-04 | E | PASS | "What changes: any fields added, renamed, retyped, or dropped... if nothing changed, note that explicitly" — explicit per stage |
| C-05 | R | PASS | "How long it takes: even a rough characterization helps" — asked per stage |
| C-06 | R | PASS | Dedicated Staleness Check section; two scenarios (normal + named failure); threshold anchored in domain context |
| C-07 | R | PASS | Entity vocabulary suggested upfront; domain entities named in prompt text (MarkdownDecision, PriceAdjustment, etc.) |
| C-08 | A | PARTIAL | "pair each one with a specific recovery idea. The more grounded the better" — advisory; no explicit specificity gate |
| C-09 | A | PASS | "Name an alternative... at least two trade-off dimensions... ground at least one in markdown-domain terms" |
| C-10 | A | PARTIAL | "Try to name your entity vocabulary upfront" — advisory; no protocol enforcement that inventory precedes stage trace |
| C-11 | A | PARTIAL | "Using boundary labels like B1->2, B2->3 makes it easier to reference them later" — advisory suggestion, not a labeling requirement |
| C-12 | A | PARTIAL | "if nothing changed, note that explicitly" — no required verification-claim format (`verified: no field added...`) |
| C-13 | A | FAIL | No tables, no inline gates; all requirements in advisory prose; omissions invisible without reading every sentence |
| C-14 | A | PARTIAL | "it's worth noting what a merchandising or finance associate would have done" — advisory framing; no named-step requirement |

**Score Calculation:**

```
essential_pass  = (1 + 1 + 0.5 + 1) / 4  →  3.5 / 4 * 60  =  52.5
recommended_pass = (1 + 1 + 1) / 3        →  3 / 3 * 30    =  30.0
aspirational_pass = (0.5+1+0.5+0.5+0.5+0+0.5) / 7  →  3.5/7 * 10  =  5.0
```

**V-01 composite: 87.5 — all_essential_pass: FALSE (C-03 PARTIAL)**

---

### V-02 — All-Section Structural Completeness Tables

**Scenario**: Employee expense reimbursement pipeline (6 stages)

| Criterion | Tier | Pass / Partial / Fail | Evidence |
|-----------|------|-----------------------|----------|
| C-01 | E | PASS | STAGE TRACE TABLE rows pre-populated with source ⇒ destination per stage; unbroken chain structurally enforced |
| C-02 | E | PASS | BOUNDARY TABLE column "Error Handling (mechanism or 'no handling — risk accepted')" — blank cell is visible gap |
| C-03 | E | PASS | STAGE TRACE TABLE "Loss Point" column; "errors may occur" or "data loss possible" explicitly disqualified |
| C-04 | E | PASS | STAGE TRACE TABLE: Input Schema, Transformations, Output Schema columns; "verified: no field added, removed, renamed, or retyped" exact text required |
| C-05 | R | PASS | Latency column in STAGE TRACE TABLE; Boundary Latency column in BOUNDARY TABLE |
| C-06 | R | PASS | STALE ANALYSIS section; additive accumulation shown; two scenarios (normal + named worst-case); FRESH/STALE verdicts |
| C-07 | R | PASS | DOMAIN CONTEXT entity vocabulary; "Entity at Risk" column explicitly disqualifies "data" or "records" |
| C-08 | A | PASS | LOSS-POINT RECOVERY TABLE "Recovery Mechanism (specific — generic advice fails)" column; INCUMBENT BASELINE section requires named-step citation |
| C-09 | A | PASS | TRADE-OFF ANALYSIS requires 2 dimensions; at least one compares automated elapsed time against manual cycle time from INCUMBENT BASELINE |
| C-10 | A | PASS | DOMAIN CONTEXT (entity inventory) declared before STAGE TRACE TABLE; section order enforced by structure |
| C-11 | A | PASS | BOUNDARY TABLE with labeled rows B1->2 through B5->6 forming complete inventory; LOSS-POINT RECOVERY TABLE references "Location (boundary label or stage name)" |
| C-12 | A | PASS | Transformations column rule: exact `verified: no field added, removed, renamed, or retyped` text required; BOUNDARY TABLE: "if N: 'verified unchanged'" |
| C-13 | A | PASS | Three independent tables each with "a row with any blank cell is a structural gap" — STAGE TRACE TABLE maps to C-04, BOUNDARY TABLE maps to C-02, LOSS-POINT RECOVERY TABLE maps to C-03 |
| C-14 | A | PASS | INCUMBENT BASELINE section requires 3+ named manual steps with actor + duration; LOSS-POINT RECOVERY TABLE "at least one entry must reference a named step from this section as the identified fallback process" |

**Score Calculation:**

```
essential_pass   = 4/4 * 60  =  60.0
recommended_pass = 3/3 * 30  =  30.0
aspirational_pass = 7/7 * 10 =  10.0
```

**V-02 composite: 100.0 — all_essential_pass: TRUE**

---

### V-03 — Inertia Framing: Structured Incumbent Baseline Table

**Scenario**: Product availability sync pipeline (5 stages)

| Criterion | Tier | Pass / Partial / Fail | Evidence |
|-----------|------|-----------------------|----------|
| C-01 | E | PASS | SECTION 3 traces 5 stages with source ⇒ destination; entity vocabulary from SECTION 2 anchors chain |
| C-02 | E | PASS | SECTION 4 requires error handling per boundary; "no handling — risk accepted" exact phrase or specific mechanism |
| C-03 | E | PASS | SECTION 3: "loss point: a concrete named failure mode — 'errors may occur' does not qualify" |
| C-04 | E | PASS | SECTION 3: input schema, transformations (specific field names), output schema; "`verified: no field added, removed, renamed, or retyped`" required if no change |
| C-05 | R | PASS | Latency asked per stage in SECTION 3; boundary latency in SECTION 4 |
| C-06 | R | PASS | SECTION 5: running accumulation, two scenarios, FRESH/STALE verdicts, threshold from SECTION 2 |
| C-07 | R | PASS | SECTION 2 declares entity vocabulary; all six entities named in scenario description |
| C-08 | A | PASS | SECTION 6: "specific recovery mechanism" required; "generic terms such as 'manual review' or 'human intervention'... do not qualify for C-14" |
| C-09 | A | PASS | SECTION 7: alternative pattern + 2 dimensions; one compares against INCUMBENT TOTAL |
| C-10 | A | PASS | SECTION 1 (incumbent baseline) + SECTION 2 (entity inventory) declared before SECTION 3 (stage trace); ordering enforced — "a Section 3 stage written before Section 1 is a protocol violation" |
| C-11 | A | PASS | SECTION 4 labels all four boundaries B1->2 through B4->5; complete inventory; each boundary annotation references label |
| C-12 | A | PASS | SECTION 3: "`verified: no field added, removed, renamed, or retyped`"; SECTION 4: "`verified unchanged`" |
| C-13 | A | **FAIL** | SECTION 1 INCUMBENT BASELINE TABLE is a 4-col structural table, but maps to incumbent documentation, **not** to a scorable requirement (C-02/C-03/C-04). SECTION 3 stage trace and SECTION 4 boundary checks are prose. No gates. Rubric requires: "table or gate must map directly to a scorable requirement (C-02, C-03, or C-04)" |
| C-14 | A | PASS | SECTION 6 requires citing fallback by **Manual Step** column value from SECTION 1 table; "generic terms such as 'manual review' or 'human intervention' without naming a specific table row do not qualify" — highest C-14 enforcement depth in the round |

**Score Calculation:**

```
essential_pass   = 4/4 * 60  =  60.0
recommended_pass = 3/3 * 30  =  30.0
aspirational_pass = 6/7 * 10 =   8.57
```

**V-03 composite: 98.6 — all_essential_pass: TRUE**

**C-13 miss analysis**: The structural richness of V-03's SECTION 1 INCUMBENT BASELINE TABLE is real, but it enforces an inventory requirement, not a pipeline data requirement. The rubric gate ("must map directly to C-02, C-03, or C-04") is the binding constraint. V-03 would need one more structural surface — a boundary table or stage-trace table — to reach 100.

---

### V-04 — Combined: Imperative Register + Inline Boundary Gates

**Scenario**: Trade promotion accrual pipeline (5 stages)

| Criterion | Tier | Pass / Partial / Fail | Evidence |
|-----------|------|-----------------------|----------|
| C-01 | E | PASS | 5 stages with source ⇒ destination; imperative "you must state all five items" drives per-stage input/output schema |
| C-02 | E | PASS | BOUNDARY GATE: "(a) Error handling: name the specific mechanism... or state exactly: `no handling — risk accepted [B1->2]`" — exact label required in annotation |
| C-03 | E | PASS | "name the failure as it would appear in an incident report" — imperative; "'errors may occur' fails" explicit disqualifier |
| C-04 | E | PASS | "if no change, you must state exactly: `verified: no field added, removed, renamed, or retyped`" — exact text required, imperative |
| C-05 | R | PASS | "Latency: a value, range, or characterization — silence fails" — imperative per stage |
| C-06 | R | PASS | STALE ANALYSIS: additive breakdown required; "showing each addend is required"; FRESH/STALE tokens; two scenarios mandatory |
| C-07 | R | PASS | DOMAIN CONTEXT declares entity vocabulary; 6 entities named in prompt text |
| C-08 | A | PASS | "Name the specific recovery mechanism... For at least one critical failure mode, name a specific step from INCUMBENT BASELINE as the identified fallback process; this step name must appear verbatim" |
| C-09 | A | PASS | TRADE-OFF ANALYSIS: 2 dimensions; one compares against INCUMBENT TOTAL |
| C-10 | A | PASS | Section order enforced: INCUMBENT BASELINE → DOMAIN CONTEXT → STAGE TRACE; "you may not skip a section" |
| C-11 | A | PASS | Gates B1->2, B2->3, B3->4, B4->5 form complete inventory; annotations use label in exact text (`no handling — risk accepted [B1->2]`); RECOVERY PRESCRIPTIONS references "every `no handling — risk accepted [B[N]->[N+1]]` gate annotation" |
| C-12 | A | PASS | "`verified: no field added, removed, renamed, or retyped`" exact text required in stage trace; "`verified unchanged at B1->2`" for gates |
| C-13 | A | PASS | Inline boundary gates: "STAGE N+1 does not open until BOUNDARY GATE BN->(N+1) is fully stated" + "a gate with any item missing is a protocol failure" — maps to C-02; missing gate block = structurally visible violation |
| C-14 | A | PASS | INCUMBENT BASELINE named steps with actor + duration; RECOVERY PRESCRIPTIONS: "this step name must appear verbatim as it does in that section" |

**Score Calculation:**

```
essential_pass   = 4/4 * 60  =  60.0
recommended_pass = 3/3 * 30  =  30.0
aspirational_pass = 7/7 * 10 =  10.0
```

**V-04 composite: 100.0 — all_essential_pass: TRUE**

---

### V-05 — Combined: Incumbent Baseline Table + Schema-Diff Tables + Inline Gates

**Scenario**: Payroll processing pipeline (5 stages)

| Criterion | Tier | Pass / Partial / Fail | Evidence |
|-----------|------|-----------------------|----------|
| C-01 | E | PASS | Steps 2–6 trace 5 stages with source ⇒ destination; entity vocabulary from STEP 1 anchors chain |
| C-02 | E | PASS | BOUNDARY GATE per stage: "(a) Error handling: name the mechanism — or state exactly: `no handling — risk accepted [B1->2]`" |
| C-03 | E | PASS | Per-stage: "Loss point: concrete named failure — 'errors may occur' fails" |
| C-04 | E | PASS | Per-stage schema-diff table with "Transformations cell rule: `verified: no field added, removed, renamed, or retyped`" — blank cell = structural gap |
| C-05 | R | PASS | Latency in schema-diff table and in STEP 7 running accumulation |
| C-06 | R | PASS | STEP 7: step-by-step running accumulation; FRESH/STALE tokens; two scenarios (normal + named failure) |
| C-07 | R | PASS | STEP 1 declares entity vocabulary; 6 entities named |
| C-08 | A | PASS | STEP 8: specific mechanism required; "cite the fallback by its Manual Step column value from the STEP 0 INCUMBENT BASELINE TABLE — generic terms... do not qualify" |
| C-09 | A | PASS | STEP 9: alternative + 2 dimensions; one compares against INCUMBENT TOTAL |
| C-10 | A | PASS | STEP 0 (incumbent baseline) + STEP 1 (entity inventory) before STEP 2 (first stage); ordering enforced |
| C-11 | A | PASS | Gates B1->2 through B4->5; label appears in exact annotation text; STEP 8 references by gate label |
| C-12 | A | PASS | Schema-diff table "Transformations cell rule"; gate "`verified unchanged at B1->2`" |
| C-13 | A | PASS | Two structural surfaces: per-stage schema-diff tables (blank cell = C-04 gap) + inline gates (missing gate = C-02 violation); both map to scorable requirements |
| C-14 | A | PASS | STEP 8: "cite the fallback by its Manual Step column value from the STEP 0 INCUMBENT BASELINE TABLE" — per-row structural citation, not prose naming |

**Score Calculation:**

```
essential_pass   = 4/4 * 60  =  60.0
recommended_pass = 3/3 * 30  =  30.0
aspirational_pass = 7/7 * 10 =  10.0
```

**V-05 composite: 100.0 — all_essential_pass: TRUE**

---

## Final Rankings

| Rank | Variation | Score | Essential | Notes |
|------|-----------|-------|-----------|-------|
| 1 (tied) | **V-02** | 100.0 | all pass | Three structural tables, full-spectrum C-13 coverage |
| 1 (tied) | **V-04** | 100.0 | all pass | Inline gates; imperative register closes all prose gaps |
| 1 (tied) | **V-05** | 100.0 | all pass | Schema-diff tables + gates; per-row C-14 citation |
| 4 | V-03 | 98.6 | all pass | Fails C-13: incumbent table doesn't map to C-02/03/04 |
| 5 | V-01 | 87.5 | **C-03 PARTIAL** | Advisory register; zero structural surfaces; C-13 FAIL |

---

## Excellence Signals

**H1 confirmed**: Advisory phrasing (V-01) produces 3 PARTIAL criterion scores vs zero for imperative variations. The phrasing contrast is sharpest on C-03 (loss points), C-10 (pre-trace inventory), and C-11 (boundary labeling) — all three suffer "try to" hedging that lets a model skip requirements without violating prompt instructions. C-13 was always going to fail V-01 (no structural surface), but advisory register degrades essential-tier C-03 too.

**H2 confirmed**: V-02's triple-table structure achieves C-13 PASS for all three scorable requirement types simultaneously. Current C-13 only requires one structural surface — V-02 over-satisfies. This creates no rubric differentiation vs V-04 (single surface), which is the signal: the criterion undervalues full-spectrum coverage.

**H3 confirmed**: V-03's 4-column INCUMBENT BASELINE TABLE with per-row citation requirement delivers the most enforceable C-14 of the round. But it fails C-13 because the table maps to incumbent documentation, not C-02/03/04. The structural investment was placed on the wrong surface for C-13 purposes — a clear design tension worth capturing.

**New pattern 1 — Full-spectrum structural coverage**: V-02 achieves C-13 for all three scorable requirement types (boundary table → C-02, loss-point table → C-03, schema-diff table → C-04). V-04 and V-05 achieve C-13 for one or two types. The rubric currently treats these identically. Full-spectrum is a quality amplifier: an omission in any requirement type is structurally visible without needing to check a sibling section. This is aspirational above C-13 — not about having a structural mechanism, but about having one per scorable requirement type.

**New pattern 2 — Column-value citation enforcement**: V-03 and V-05 upgrade C-14 from "name the pre-automation process" (V-04's prose verbatim requirement) to "cite the named row by its Manual Step column value." The column-value citation is machine-verifiable: the cell value appears verbatim or the prescription fails. V-04 requires verbatim step names too, but from unstructured prose — the column anchors the expected value before it is cited. This structural pre-declaration of citable values represents the next tier above current C-14.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["full-spectrum structural coverage — one structural mechanism per scorable requirement type (C-02, C-03, C-04) simultaneously, not just 'at least one'; V-02 is the only R4 variation achieving all three surfaces", "column-value citation enforcement — incumbent baseline presented as a named table whose Manual Step column values are the required citation targets in recovery prescriptions; V-03 and V-05 implement this; makes C-14 machine-verifiable without prose interpretation"]}
```
