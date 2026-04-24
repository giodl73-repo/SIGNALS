Now I have all the information needed. Let me score all five variations.

---

## Scoring: mock-ns Round 16 (Rubric v15, denominator 35)

### Scoring formula

```
Composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 35 * 10)
```

All five variations share identical essential and recommended structure — the only differentiation is at C-41, C-42, and C-43.

---

### Common baseline: C-01 through C-40

All variations pass C-01–C-40 (32 aspirational passes). Trace:

| Criterion | All V-01..V-05 | Evidence |
|-----------|---------------|----------|
| C-01 | PASS | MOCK ARTIFACT header block present, five fields |
| C-02 | PASS | Category table present; correct assignment logic |
| C-03 | PASS | A-3 generates skill-specific structure |
| C-04 | PASS | FLAG computed in S-3, referenced in A-1 header |
| C-05 | PASS | A-4 writes to `simulations/mock/{topic}-{namespace}-mock-{date}.md` |
| C-06 | PASS | Default skill table present; correct namespace→skill mapping |
| C-07 | PASS | A-2 emits category-appropriate fidelity warning as lead section |
| C-08 | PASS | A-5 emits next-step invocation as final artifact line |
| C-09 | PASS | Case 1 in S-3 covers Tier 2+ critical namespaces |
| C-10 | PASS | `> TOPICS.md: {result}` dedicated emit line in S-1 |
| C-11 | PASS | FLAG computed in S-3 before A-1 header assembly |
| C-12 | PASS | Exclusion constraint column carries topic-status exclusion note |
| C-13 | PASS | A-2 positions fidelity warning before mock body |
| C-14 | PASS | Prohibition at compute site ("FLAG MUST NOT…") + consumption site ("Copy FLAG from S-3 verbatim. Do not rederive it.") |
| C-15 | PASS | S-1 table has dedicated "Exclusion constraint" column |
| C-16 | PASS | "FLAG MUST NOT be recomputed anywhere in this run" |
| C-17 | PASS | "First rule" row is the first row in A-1 chain |
| C-18 | PASS | Path classes row: "not in any step, any conditional branch, any fallback path…" |
| C-19 | PASS | Anti-displacement row: "before any field is listed, before any category lookup, before any formatting instruction, or any other instruction in this step" |
| C-20 | PASS | "Failure conseq [A-1:FC]" row: category mismatch + undetectable corruption |
| C-21 | PASS | "Affirmative closure" + "No-exemption" rows in S-3 chain |
| C-22 | PASS | Anti-displacement includes "or any other instruction in this step" |
| C-23 | PASS | "Failure consequence" row in S-3: corrupted value indistinguishable from correct |
| C-24 | PASS | "All-governed" + "No-exemption" rows in A-1 chain |
| C-25 | PASS | "Guarantee-break" row: "This violation breaks the closure guarantee…" |
| C-26 | PASS | "Cross-site ref [S-3:CS]" row names A-1 Failure consequence row |
| C-27 | PASS | Each claim occupies a labeled table row — independently scannable |
| C-28 | PASS | "the Failure consequence row in step A-1" — location-specific navigation anchor |
| C-29 | PASS | A-1 "Failure conseq [A-1:FC]" carries "[Mutual target of S-3:CS — Cross-site reference row in S-3]" |
| C-30 | PASS | [S-3:CS] and [A-1:FC] bracket tokens at both sites |
| C-31 | PASS | P-0 is a dedicated pre-chain orientation block before all prohibition rows |
| C-32 | PASS | P-0 is a separate step before S-3 — precedes all FLAG computation cases |
| C-33 | PASS | Abbreviation key (`:CS`, `:FC`) + 5-column resolution table in P-0 |
| C-34 | PASS | "Lookup obligation: before processing any row containing a bracket token, look up the token in the table above" |
| C-35 | PASS | S-3 CONFIRMATION row: "(P-0 table, row 1)"; A-1: "(P-0 table, row 2)" |
| C-36 | PASS | Phase 1 Locate + Phase 2 Confirm two-phase protocol defined in P-0 |
| C-37 | PASS | "CONFIRMATION REQUIRED before writing this row" at both S-3 and A-1 |
| C-38 | PASS | "DO NOT WRITE THE ROW" hard-stop language at preamble Phase 2 and both use-site echoes |
| C-39 | PASS | All variants name the visual-recognition bypass and declare it non-compliant |
| C-40 | PASS | "Emit confirmation record" obligation present in Phase 2 definition in all variants |

---

### New criteria evaluation: C-41, C-42, C-43

#### C-41 — Pre-filled confirmation record template at both S-3 and A-1

| Variation | Evidence | Result |
|-----------|----------|--------|
| V-01 | Standalone table blocks present at S-3 ("Token: [S-3:CS], Step: S-3, Row type: Cross-site reference row, Match: ___") and A-1 ("Token: [A-1:FC], Step: A-1, Row type: Failure consequence row, Match: ___"). Both pre-populated with row-specific values, not generic placeholders. | **PASS** |
| V-02 | P-0 provides only a generic placeholder format (`{token-name}`, `{step-name}`, `{row-type-name}`). No pre-filled template at S-3 or A-1 use sites. | **FAIL** |
| V-03 | Step 2d in P-0 defines record format with generic placeholders only. S-3 and A-1 CONFIRMATION rows say "emit confirmation record (Step 2d)" but carry no pre-filled block. No use-site template present. | **FAIL** |
| V-04 | Standalone pre-filled blocks at S-3 and A-1 — same pattern as V-01. Token, Step, Row type populated; Match blank. Both use sites covered. | **PASS** |
| V-05 | Pre-filled table blocks at S-3 and A-1, with instruction "(fill Match field only)." Token, Step, Row type pre-populated at each site specifically. Both use sites covered. | **PASS** |

#### C-42 — Emit obligation woven into hard-stop gate condition at all three locations

The requirement: gate text must read "...and the record is emitted" (not merely listing emit as a Phase 2 sub-task).

| Variation | P-0 gate | S-3 gate | A-1 gate | Result |
|-----------|----------|----------|----------|--------|
| V-01 | "DO NOT WRITE THE ROW until **both phases pass**" — emit is mentioned in Phase 2 but absent from gate text | Same form | Same form | **FAIL** |
| V-02 | Same as V-01 — emit appears as "Emit confirmation record." in Phase 2, gate ends at "both phases pass" | Same | Same | **FAIL** |
| V-03 | "DO NOT WRITE THE ROW until Steps 2a through 2d are complete **and the record is emitted**" — emit woven in explicitly | "DO NOT WRITE THE ROW until Steps 2a-2d are complete **and the record is emitted**" | Same | **PASS** |
| V-04 | "DO NOT WRITE THE ROW until **both phases pass**" — emit listed in Phase 2, absent from gate | Same form | Same form | **FAIL** |
| V-05 | "DO NOT WRITE THE ROW until Steps 2a through 2d are complete **and the record is emitted**" | "DO NOT WRITE THE ROW until Steps 2a-2d are complete **and the record is emitted**" | Same | **PASS** |

#### C-43 — Dual-naming + protocol-failure severity framing

Requirements: (a) action-based description ("without reading the Step and Row type cells") AND protocol-based ("without performing Phase 2"), (b) "Locate-only is a protocol failure" categorical close.

| Variation | Action-based | Protocol-based | "Locate-only" close | Result |
|-----------|-------------|----------------|---------------------|--------|
| V-01 | ABSENT | PRESENT ("without performing Phase 2") | ABSENT — "has not satisfied this protocol" only | **FAIL** — single form, gap-framing close |
| V-02 | PRESENT ("without reading both cells" — action-based naming of cell-read omitted) | PRESENT ("without executing Phase 2") | PRESENT — "Locate-only is a protocol failure." as standalone sentence in dedicated PROTOCOL FAILURE MODES section | **PASS** |
| V-03 | ABSENT | PRESENT ("without performing Phase 2") | ABSENT — "has not satisfied this protocol" | **FAIL** |
| V-04 | PRESENT ("without reading the Step and Row type cells") | PRESENT ("without performing Phase 2") | PRESENT — "Locate-only is a protocol failure." | **PASS** |
| V-05 | PRESENT ("without reading the Step and Row type cells") | PRESENT ("without performing Phase 2") | PRESENT — "Locate-only is a protocol failure." in P-0 opening, plus per-row "Protocol reminder: processing this row without reading cells, or without performing Phase 2, is a protocol failure." at both use sites | **PASS** |

---

### Composite scores

| Variation | C-41 | C-42 | C-43 | Aspirational passes | Asp. score | Composite |
|-----------|------|------|------|---------------------|------------|-----------|
| V-01 | PASS | FAIL | FAIL | 33/35 | 9.43 | 99.43 |
| V-02 | FAIL | FAIL | PASS | 33/35 | 9.43 | 99.43 |
| V-03 | FAIL | PASS | FAIL | 33/35 | 9.43 | 99.43 |
| V-04 | PASS | FAIL | PASS | 34/35 | 9.71 | 99.71 |
| V-05 | PASS | PASS | PASS | 35/35 | 10.00 | **100.00** |

Essential: 5/5 × 60 = 60.00 (all variations)
Recommended: 3/3 × 30 = 30.00 (all variations)

**Ranking: V-05 > V-04 > V-01 = V-02 = V-03**

---

### Hypothesis validation

| Variation | Hypothesis | Confirmed? |
|-----------|-----------|------------|
| V-01 | Standalone table blocks make C-41 more audit-resistant than prose inline string | CONFIRMED — C-41 passes; each field is an independently verifiable row |
| V-02 | Labeled section form makes C-43 structurally prior and taxonomically distinct | CONFIRMED — C-43 passes; failure taxonomy is a named, pre-protocol structural unit |
| V-03 | Numbered Phase 2 list makes emit a mandatory lifecycle arrival, not a gate qualifier | CONFIRMED — C-42 passes at all three locations |
| V-04 | Role-sequence + inertia framing amplifies the value of the pre-filled template | PARTIAL — both C-43 and C-41 pass, but C-42 absent limits convergence |
| V-05 | Three mechanisms reinforce one another in combination | CONFIRMED — all 35 criteria pass; no single mechanism carries the full compliance burden |

---

### Excellence signals from V-05

**Signal 1 — Use-site per-row protocol-failure echo (v16 seed).**
V-05 uniquely adds a "Protocol reminder" line inside the CONFIRMATION REQUIRED cells at S-3 and A-1: *"processing this row without reading cells, or without performing Phase 2, is a protocol failure."* This brings the P-0 failure taxonomy to the exact moment of use. An executor who skimmed P-0 as a preamble cannot avoid this reminder when actually writing the bracket-token row. The C-43 opening paragraph (P-0) establishes the categorical failure frame once; the use-site echo re-activates it at zero recall cost at each row. This pattern cannot be tested by any single-axis variation — it requires C-43 (dual-naming close in P-0) to already be present as the source material the echo draws from.

**Signal 2 — Sequential emit lifecycle removes the "implied-by-phase" escape.**
V-03 demonstrates this in isolation, but V-05 shows its compounding effect with the full protocol. When emit is Step 2d in a numbered list, an executor processing Phase 2 must reach and complete Step 2d as a discrete action — they cannot treat "completing Phase 2" as implying record emission because the emit step is named independently with its own lifecycle identity. V-01, V-02, and V-04 all place emit as an appendage ("Emit confirmation record — see below") that can be mentally bundled into the phase-completion assertion. V-05's numbered form prevents this bundling.

**Signal 3 — Three-mechanism convergence produces layered enforcement.**
No single-axis variation tests whether C-41 + C-42 + C-43 produce emergent compliance properties when combined. V-05's compound structure means:
- C-43 (opening failure taxonomy) activates a rejection frame BEFORE the protocol is read
- C-42 (numbered Phase 2 lifecycle) enforces emit as a mandatory sequential arrival DURING protocol execution  
- C-41 (pre-filled use-site template) reduces compliance cost to a single judgment (Match field) AT the point of writing
- Use-site echo (v16 seed) re-activates the failure frame AT each row, independent of P-0 recall

Each layer catches a different failure mode. Together they eliminate the four primary bypass paths: skipping P-0, bundling emit into phase completion, constructing the record from memory rather than the template, and executing the row before the failure taxonomy is activated.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["use-site per-row protocol-failure echo brings dual-naming failure taxonomy to each bracket-token row at the moment of use, preventing treatment of P-0 as a skippable preamble without requiring additional executor recall", "numbered Phase 2 lifecycle makes emit a mandatory sequential waypoint rather than a gate qualifier, closing the implicit-completion escape where an executor conflates phase completion with record emission"]}
```
