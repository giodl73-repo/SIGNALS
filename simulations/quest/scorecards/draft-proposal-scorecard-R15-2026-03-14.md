## /quest:score — draft-proposal · Round 15 · Rubric v15

---

### Scoring Methodology

Formula (all essential + required pass): `composite = 90 + (aspirational_pass / 32 × 10)`

Denominator: `/32` (C-08..C-39). C-01..C-07 are mandatory C-tier, not counted.

All 5 variations are designed with essential (E-01..E-04) and required (R-01..R-03) passing — confirmed by structural review. Scoring focuses on the C-08..C-39 aspirational layer.

---

## V-01 — Architect-First | Designed fail: C-39

**Axis**: Role sequence (Architect → PM)

### Essential Criteria

| ID | Result | Evidence |
|----|--------|----------|
| E-01 | PASS | "ROLE SEQUENCE: Architect → PM" declared as typed header; applied in every subsequent phase header per spec |
| E-02 | PASS | 3+ options including do-nothing; all four anatomy fields (OPTION/PROBLEM/RISK/RATIONALE) in template |
| E-03 | PASS | Comparison matrix with OPTIONS as column headers; ≥4 dimensions; PM (Adoption friction, Business value) + Architect (Effort, Technical risk, Reversibility, Time-to-value) |
| E-04 | PASS | PM recommendation with rationale citing ≥2 matrix dimensions; qualifying conditions required in Phase 9 |

### Required Criteria

| ID | Result | Evidence |
|----|--------|----------|
| R-01 | PASS | Risk register `R-NN | RISK | P | I | P×I | MITIGATION`; ≥3 entries; P/I 1-5; P×I computed; project-specific anchors in Phase 3 |
| R-02 | PASS | Phase 7 prerequisites check before recommendation phase |
| R-03 | PASS | Phase 10 coverage verification; amendment table completion state set in Step 4 |

### Aspirational Criteria (C-08..C-39)

| ID | Result | Evidence |
|----|--------|----------|
| C-08 | PASS | Assumption register (A-NN entries) implied by PREREQUISITE GATE (C-20) requiring ≥2 A-NN entries |
| C-09 | PASS | Amend phase self-critique in template structure |
| C-10 | PASS | Scout artifact inventory step before option generation (Phase 1 scout reference) |
| C-11 | PASS | Per-category amend taxonomy (missing option, unweighted criterion, follow-up with OWNER) |
| C-12 | PASS | OWNER as typed format slot across all amend categories |
| C-13 | PASS | TEMPORAL ANCHOR and INACTION CONSEQUENCE as typed fields in Phase 1 |
| C-14 | PASS | OWNER + DEADLINE typed slots in amend entries |
| C-15 | PASS | Failure mode register (F-NN) with sign-off linkage in Phase 9 |
| C-16 | PASS | Phase 3 project-specific P/I anchors defined (P=1/3/5, I=1/3/5) before any scoring |
| C-17 | PASS | Assumption + risk registers precede recommendation (Phases 3/9b before Phase 9) |
| C-18 | PASS | Amendment table front-loaded at Phase 0; T-01..T-39 with STATUS=PENDING at init |
| C-19 | PASS | Canonical failure mode field labels (FAILURE MODE, TRIGGER CONDITION, MITIGATION) |
| C-20 | PASS | PREREQUISITE GATE block (Phase 7) confirming registers complete before recommendation |
| C-21 | PASS | Phase 5 gate audit verifies all phase headers carry [GATE: X-NN] citations |
| C-22 | PASS | Coverage table spec: `CRITERION | STATUS | CLOSED BY` — three-column format explicit |
| C-23 | PASS | Phase 9b back-fill replaces `[R-NN pending]` with R-NN IDs in all RISK fields |
| C-24 | PASS | "Populate trigger rules T-01..T-39" — 39-row table; "Trigger rules T-01..T-39 — exactly 39 rows" in amendment spec |
| C-25 | PASS | Phase 10 "Execute coverage verification as an explicitly numbered four-step list" with Step 1/2/3/4 |
| C-26 | PASS | Dedicated Phase 9b "RISK PROPAGATION [GATE: C-26]" as named phase |
| C-27 | PASS | Coverage table: "Populate one row per criterion: E-01..E-04, R-01..R-03, C-01..C-39. STATUS = PASS or FAIL." |
| C-28 | PASS | Qualifying conditions required in Phase 9 PM recommendation |
| C-29 | PASS | PHASE column in amendment spec; all key trigger rows carry explicit PHASE values |
| C-30 | PASS | Phase 10 Step 1: "Finding N: T-NN — [criterion ID and full name]" format; one finding per trigger |
| C-31 | PASS | Phase 2 RISK: "Declare [R-NN pending] to reserve the slot for Phase 9b back-fill" |
| C-32 | PASS | Phase 9b: "Domain 1 — Option RISK fields" and "Domain 2 — Comparison matrix risk column" both named |
| C-33 | PASS | Phase 2 RISK: "Do not compute P×I in Phase 2 RISK fields. Declare [R-NN pending]" — prohibition adjacent to placeholder |
| C-34 | PASS | "Domain 1 —" and "Domain 2 —" numeric-index prefixes on both domain headers |
| C-35 | PASS | Domain 1 per-site: `[OPTION-A label] RISK field: [R-NN pending] -> [R-03 (...), R-07 (...)]` — arrow notation |
| C-36 | PASS | Domain 1 transitions: `[R-03 (P:n × I:n = n), R-07 (P:n × I:n = n)]` — P×I compound scores in transition target |
| C-37 | PASS | Domain 2: `Risk row: [OPTION-A column: R-NN IDs] | [OPTION-B column: R-NN IDs] | [do-nothing column: R-NN IDs]` — per-column attribution explicit |
| C-38 | PASS | T-37 CONDITION in amendment spec carries Part 1: "row-level confirmation 'R-NN IDs applied to risk row' fires T-37" — inline failure exemplar present |
| C-39 | **FAIL** | T-37 CONDITION carries Part 1 only; stops after the failure exemplar with no correct-format prescription (Part 2 absent). Per rubric: "A T-37 CONDITION field carrying only Part 1 ... without a correct-format prescription passes C-38 but fails C-39." T-39 fires; Finding 1: T-39 |

**Fails: 1 (C-39). Aspirational passes: 31/32.**
**Composite: 90 + (31/32 × 10) = 99.69**
**All essential PASS. Golden threshold: MET.**

---

## V-02 — PM-First Compact | Designed fail: C-37; C-38 PASS, C-39 PASS

**Axis**: Output format (compact tables, PM-first)

### Essential + Required: all PASS (same structural completeness as V-01, PM-first role sequence)

### Aspirational Criteria — Delta from V-01

All C-08..C-39 PASS except the following changes:

| ID | Result | Evidence |
|----|--------|----------|
| C-22 | PASS | Explicitly stated: "Include CLOSED BY column even in compact format for traceability" |
| C-33 | PASS | Phase 2 RISK: "Do not compute P×I in Phase 2 RISK fields. Declare [R-NN pending] to reserve the slot." — prohibition present and adjacent |
| C-37 | **FAIL** | Phase 9b Domain 2: "Risk row: R-NN IDs applied to risk row. Confirm applicable register entries present." — row-level confirmation only; no per-column attribution. Exact firing construct per T-37: "R-NN IDs applied to risk row" |
| C-38 | PASS | T-37 CONDITION in amendment spec carries Part 1: "row-level confirmation 'R-NN IDs applied to risk row' fires T-37; per-column format required: [OPTION-A column: R-NN IDs] \| [OPTION-B: R-NN IDs]" — full two-part structure present |
| C-39 | PASS | T-37 CONDITION carries both Part 1 (failure exemplar) AND Part 2 (correct-format prescription: "per-column format required: [OPTION-A column: R-NN IDs] \| [OPTION-B: R-NN IDs]") — two-part structure complete |

T-37 fires (C-37 FAIL). T-38 and T-39 are silent (both parts present in CONDITION). Finding 1: T-37.

**Fails: 1 (C-37). Aspirational passes: 31/32.**
**Composite: 90 + (31/32 × 10) = 99.69**
**All essential PASS. Golden threshold: MET.**

---

## V-03 — Stale Table (38 rows) | Designed fails: C-24 + C-38 (independent) + C-39 (cascade)

**Axis**: Lifecycle emphasis (v14 amendment table carried forward)

### Essential + Required: all PASS

### Aspirational Criteria — Key evaluation

| ID | Result | Evidence |
|----|--------|----------|
| C-24 | **FAIL** | Amendment spec: "Build trigger rules from the current rubric criteria... Use the v14 criteria list for trigger construction: C-01 through C-38. Each criterion generates one trigger row (T-01..T-38). Total: 38 rows." — 38 ≠ 39 required by v15. T-24 fires at PRE-DOCUMENT. Finding 1: T-24 |
| C-36 | PASS | Domain 1: `[OPTION-A label] RISK field: [R-NN pending] -> [R-03 (P:n × I:n = n), R-07 (P:n × I:n = n)]` — P×I compound scores present |
| C-37 | PASS | Domain 2: `Risk row: [OPTION-A column: R-NN IDs] | [OPTION-B column: R-NN IDs] | [do-nothing column: R-NN IDs]` — per-column attribution present |
| C-38 | **FAIL** | T-37 CONDITION in stale amendment spec: "fires if Phase 9b Domain 2 does not carry per-option-column R-NN attribution" — abstract condition category, no inline failure exemplar quoting the exact construct. T-38 fires. Finding 2: T-38 |
| C-39 | **FAIL** | C-38 FAIL → C-39 FAIL (deterministic cascade). Abstract T-37 CONDITION contains neither Part 1 nor Part 2. T-39 is absent from the stale 38-row table (T-01..T-38 only), so T-39 cannot fire as a named trigger — but C-39 fails independently by rubric evaluation of the T-37 CONDITION cell |
| C-25 | PASS | Phase 10: "Execute as an explicitly numbered four-step list" with Step 1/2/3/4 |
| C-33 | PASS | Phase 2 RISK: "Do not compute P×I in Phase 2 RISK fields. Declare [R-NN pending]" — prohibition present |

All other C-08..C-23, C-25..C-36 criteria: PASS (lifecycle-gate-heavy design satisfies structural requirements; Phase 9b fully compliant with depth criteria).

**Fails: 3 (C-24, C-38, C-39). Aspirational passes: 29/32.**
**Composite: 90 + (29/32 × 10) = 99.06**
**All essential PASS. Golden threshold: MET.**

---

## V-04 — Conversational Register + PM-First | Designed fails: C-25 + C-33

**Axis**: Phrasing register (conversational) + role sequence combination

### Essential + Required: all PASS

### Aspirational Criteria — Key evaluation

| ID | Result | Evidence |
|----|--------|----------|
| C-25 | **FAIL** | Phase 10: "Walk through coverage verification as a narrative discussion." Prose walk-through — no numbered Step 1/2/3/4. The finding format "Finding N: T-NN" is present (C-30 PASS), but the numbered four-step structure is absent. T-25 fires. Finding 1: T-25 |
| C-30 | PASS | Phase 10 narrative: "produce a named finding inline in the narrative using the label format 'Finding N: T-NN': state the criterion ID and name... Each open trigger gets its own separately labeled finding entry. Do not bundle two open triggers into a single finding." Format requirement met |
| C-31 | PASS | Phase 2 RISK: "[R-NN pending] -- placeholder for risk register linkage" — forward-reference placeholder present |
| C-33 | **FAIL** | Phase 2 RISK template: `RISK: [R-NN pending] -- placeholder for risk register linkage; will be resolved in Phase 9b.` — placeholder present (C-31 PASS) but "Do not compute P×I" prohibition is absent from the adjacent template block. T-33 fires. Finding 2: T-33 |
| C-36 | PASS | Domain 1: `[OPTION-A label] RISK field: [R-NN pending] -> [R-03 (P:n × I:n = n), R-07 (P:n × I:n = n)]` — P×I compound scores in transition targets |
| C-37 | PASS | Domain 2: `Risk row: [OPTION-A column: R-NN IDs] | [OPTION-B column: R-NN IDs] | [do-nothing column: R-NN IDs]` — per-column attribution explicit |
| C-38 | PASS | T-38/T-39 CONDITION in amendment spec carries full two-part structure in conversational language — confirms C-38+C-39 satisfiable in non-formal register |
| C-39 | PASS | T-39 spec: "two-part form required: Part 1 quotes the failure construct AND Part 2 states 'per-column format required: [OPTION-A column: R-NN IDs] \| [OPTION-B: R-NN IDs]'" — correct-format prescription explicitly stated |
| C-24 | PASS | "Populate T-01..T-39 (39 trigger rules, one per v15 criterion)" — 39-row table |

All other C-08..C-32, C-34..C-35, C-37..C-39 criteria: PASS.

**Fails: 2 (C-25, C-33). Aspirational passes: 30/32.**
**Composite: 90 + (30/32 × 10) = 99.38**
**All essential PASS. Golden threshold: MET.**

---

## V-05 — Inertia-Forward + Quad Fail | Designed fails: C-36 + C-37 + C-38 + C-39

**Axis**: Inertia framing + depth/exemplar combination

### Essential + Required: all PASS

### Aspirational Criteria — Key evaluation

| ID | Result | Evidence |
|----|--------|----------|
| C-24 | PASS | "Populate T-01..T-39. Assign PHASE for each trigger." — 39-row table |
| C-25 | PASS | Phase 10: "Execute coverage verification as an explicitly numbered four-step list" with Step 1/2/3/4 |
| C-32 | PASS | "Domain 1 — Option RISK fields" and "Domain 2 — Comparison matrix risk column" both named |
| C-33 | PASS | Phase 2 RISK: "Do not compute P×I in Phase 2 RISK fields. Declare [R-NN pending] to reserve the slot." — prohibition adjacent to placeholder |
| C-34 | PASS | "Domain 1 —" and "Domain 2 —" numeric-index prefixes present |
| C-35 | PASS | Domain 1: `[OPTION-A label] RISK field: [R-NN pending] -> [R-NN IDs applicable to Option A]` — arrow notation present per site |
| C-36 | **FAIL** | Domain 1 transition targets: "R-NN IDs applicable to Option X" — R-NN IDs listed without P×I compound scores. Note in spec: "The risk register carries the full P×I scores; the register is the authoritative source for compound scoring." — authored clarification, not rubric substitute. C-36 requires P×I in the transition target itself. T-36 fires. Finding 1: T-36 |
| C-37 | **FAIL** | Domain 2: "Risk row: R-NN IDs applied by option. Applicable register entries referenced in risk row." — row-level only; no per-column attribution naming which R-NN IDs apply to which option column. T-37 fires. Finding 2: T-37 |
| C-38 | **FAIL** | T-37 CONDITION in amendment spec: "fires if Phase 9b Domain 2 enumeration does not carry per-option-column R-NN attribution" — abstract. No inline failure exemplar quoting the exact document construct. T-38 fires. Finding 3: T-38 |
| C-39 | **FAIL** | C-38 FAIL → C-39 FAIL (deterministic cascade). Abstract T-37 CONDITION contains neither Part 1 nor Part 2. T-39 fires. Finding 4: T-39 |

Four open triggers: T-36, T-37, T-38, T-39. Four findings.

**Fails: 4 (C-36, C-37, C-38, C-39). Aspirational passes: 28/32.**
**Composite: 90 + (28/32 × 10) = 98.75**
**All essential PASS. Golden threshold: MET.**

---

## Composite Scores — Ranked

| Rank | Variation | Fails | Passes | Composite |
|------|-----------|-------|--------|-----------|
| 1 (tie) | V-01 Architect-First | C-39 | 31/32 | **99.69** |
| 1 (tie) | V-02 PM-First Compact | C-37 | 31/32 | **99.69** |
| 3 | V-04 Conversational | C-25, C-33 | 30/32 | **99.38** |
| 4 | V-03 Stale Table | C-24, C-38, C-39 | 29/32 | **99.06** |
| 5 | V-05 Quad Fail | C-36, C-37, C-38, C-39 | 28/32 | **98.75** |

All predictions confirmed. Score separation is clean: each additional fail costs exactly 0.3125 points.

---

## Excellence Signals — Joint Top Scorers (V-01, V-02)

**Signal 1 — C-39 boundary case established by V-01.**
The one document state that passes C-38 and fails C-39: T-37 CONDITION carries the inline failure exemplar (Part 1 present, "row-level confirmation 'R-NN IDs applied to risk row' fires T-37") but stops there — no correct-format prescription for Part 2. T-39 fires as the sole open trigger. This is the precise C-39 criterion boundary, now demonstrated by a real variation rather than just asserted by the criterion definition.

**Signal 2 — C-38+C-39 double-pass achievable while T-37 fires (V-02).**
V-02 establishes the key invariant: a document with C-37 FAIL (Domain 2 row-level only) can still achieve C-38 PASS + C-39 PASS by making the T-37 CONDITION entry fully self-documenting. The amendment table entry is independent of Phase 9b compliance. The two-part structure passes regardless of whether T-37 fires or is silent.

**Signal 3 — Compact format is orthogonal to structural traceability.**
V-02 demonstrates that compact output (minimized prose, concise cell values) preserves C-22 (CLOSED BY column), C-33 (prohibition adjacent to placeholder), and C-25 (numbered finalization steps). Format density is not a risk axis for structural criteria — the CLOSED BY column note ("Include CLOSED BY column even in compact format for traceability") is the operative design decision.

**Signal 4 — C-38+C-39 both pass in conversational register (V-04).**
The two-part T-37 CONDITION structure is not syntax-dependent — natural language can satisfy both parts when the content carries the failure exemplar and the correct-format prescription. This eliminates "formal phrasing required" as a hypothetical exception for C-38/C-39.

---

```json
{"top_score": 99.69, "all_essential_pass": true, "new_patterns": ["C-39 independent fail confirmed by V-01: T-37 CONDITION with Part 1 only (failure exemplar, no correct-format prescription) passes C-38 and fails C-39 — boundary case demonstrated by a designed variation for the first time", "C-38+C-39 double-pass with T-37 firing confirmed by V-02: amendment table T-37 CONDITION can be fully self-documenting (both parts present) independent of Phase 9b Domain 2 compliance — the entry passes both criteria even when the trigger fires"]}
```
