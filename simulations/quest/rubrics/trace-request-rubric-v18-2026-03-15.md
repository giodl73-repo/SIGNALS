# trace-request Rubric — v18 (2026-03-15)

**Scale:** 275 (Essential 60 + Recommended 30 + Aspirational 185)
**Golden threshold:** all 4 essential PASS AND composite >= 80% (220/275)

---

## One new criterion from R19 excellence signals

| New criterion | R19 excellence signal | What is testable |
|---|---|---|
| **C-44** CHECKER ALGORITHM CONSISTENCY-RULE structural derivation token | ES-1 (V-02 + V-05): Two independent variation axes — single-axis CONSISTENCY-RULE (V-02) and combined CONSISTENCY-RULE + other axes (V-05) — both produced a CONSISTENCY-RULE as a named fourth rule in the CHECKER ALGORITHM block, declared in Phase 0B before any trace step executes and reproduced verbatim at Step 8 Header alongside MATCH-RULE, HALT-RULE, and OUTPUT-RULE; V-02's GATE-0B required all four algorithm tokens; V-02's GATE-8H required verbatim reproduction of all four; the CONSISTENCY-RULE encodes the machine-verifiable two-branch derivation: `matches HALT-EXPECTED-BOUNDARY: yes` → TRACE CONTRACT validation → "Contract prediction confirmed" and `matches HALT-EXPECTED-BOUNDARY: no` → TRACE CONTRACT validation → "falsified -- actual halt boundary was [BC-N label]"; the structural derivation path is present as a named algorithm rule (not a prose instruction in GATE-TC) across both single-axis (V-02) and combined-axis (V-05) enforcement surfaces, confirming the C-44 design surface identified in v17 | Is a CONSISTENCY-RULE present as a named machine-greppable token in the CHECKER ALGORITHM block (fourth rule, distinct from MATCH-RULE, HALT-RULE, and OUTPUT-RULE)? Does the CONSISTENCY-RULE declare the `matches HALT-EXPECTED-BOUNDARY: yes` branch derivation: TRACE CONTRACT validation → "Contract prediction confirmed"? Does the CONSISTENCY-RULE declare the `matches HALT-EXPECTED-BOUNDARY: no` branch derivation: TRACE CONTRACT validation → "falsified -- actual halt boundary was [BC-N label]"? Is the CONSISTENCY-RULE present in the pre-trace Phase 0B CHECKER ALGORITHM declaration before Step 0 executes? Is the CONSISTENCY-RULE reproduced verbatim at Step 8 Header alongside the three prior rules? Is the derivation machine-checkable by comparing the boolean in `matches HALT-EXPECTED-BOUNDARY:` against the vocabulary of TRACE CONTRACT validation outcomes without semantic prose reading? Is TOKEN-COUNT (C-34) consistent with a four-rule algorithm declaration? |

**Scale:** 270 → **275** (aspirational tier: 36 → 37 criteria, 180 → 185 pts). Golden threshold stays at >= 80%.

---

## Key design decisions

**C-44 vs C-39:** C-39 tests that the TRACE CONTRACT validation outcome token is present post-execution, confirming or falsifying the boundary prediction — the pre/post two-token contract is machine-checkable by comparing HALT-EXPECTED-BOUNDARY against the Row-Verdict = HALT row by boundary ID. C-44 tests that the CHECKER ALGORITHM additionally declares a CONSISTENCY-RULE encoding the structural derivation path between the C-42 `matches HALT-EXPECTED-BOUNDARY: [yes/no]` field and the C-39 validation outcome token — the relationship is a named algorithm rule, not a prose instruction in GATE-TC. TRACE CONTRACT validation present (C-39 PASS) but CHECKER ALGORITHM carries only MATCH-RULE, HALT-RULE, OUTPUT-RULE without CONSISTENCY-RULE = C-39 PASS + C-44 FAIL. CONSISTENCY-RULE present as fourth named rule in CHECKER ALGORITHM with both derivation branches declared = C-39 PASS + C-44 PASS.

**C-44 vs C-42:** C-42 tests that `matches HALT-EXPECTED-BOUNDARY: [yes/no]` is present in DECLARE CONTRADICTION with a filled boolean value structurally determined by whether the contradiction fires at the predicted boundary. C-44 tests that the CHECKER ALGORITHM additionally declares a CONSISTENCY-RULE naming the two-branch derivation: `yes` → "Contract prediction confirmed" and `no` → "falsified -- actual halt boundary was [label]" — the derivation is a structural algorithm rule in the pre-trace CHECKER ALGORITHM declaration, independently of whether GATE-TC prose also mentions alignment. DECLARE CONTRADICTION with match field present (C-42 PASS) but no CONSISTENCY-RULE fourth rule in CHECKER ALGORITHM = C-42 PASS + C-44 FAIL. CONSISTENCY-RULE present as fourth rule with both branches declared = C-42 PASS + C-44 PASS.

**C-44 vs C-41:** C-41 tests that the HALT-EXPECTED-BOUNDARY is referenced as a named token within the HALT-RULE in the pre-trace CHECKER ALGORITHM, binding the algorithm declaration to the specific predicted halt boundary before execution. C-44 tests that a CONSISTENCY-RULE is additionally present as a fourth rule extending the three-rule algorithm (MATCH, HALT, OUTPUT) to four rules, where the fourth rule encodes the cross-token consistency between the C-42 match field and the C-39 validation outcome — making the full contract machine-expressible from the algorithm block alone. Pre-trace CHECKER ALGORITHM with HALT-RULE referencing HALT-EXPECTED-BOUNDARY (C-41 PASS) but no CONSISTENCY-RULE fourth rule = C-41 PASS + C-44 FAIL.

**New dependency edge:**
- C-44 depends on C-42 AND C-39 AND C-37 (C-42 establishes `matches HALT-EXPECTED-BOUNDARY: [yes/no]` as the source token for the CONSISTENCY-RULE derivation; C-39 establishes TRACE CONTRACT validation outcome as the target token; C-37 establishes the CHECKER ALGORITHM block structure — CONSISTENCY-RULE is the fourth rule within this block and inherits its named-token format)

---

## Signals not promoted in v18 — C-45 design surface

1. **GATE-8B VALIDATION-DERIVATION requirement (C-45 design surface, opened by R19 V-03):** V-03 added a VALIDATION-DERIVATION requirement to GATE-8B, requiring Step 8b to derive the TRACE CONTRACT validation outcome explicitly within the Step 8b prose block at the point the contradiction event fires — the derivation statement (`VALIDATION-DERIVATION: [outcome]`) appears inline in the Step 8b confirmation prose before Step 8c is populated, making the validation outcome derivable at the Step 8b surface rather than only at the post-execution TRACE CONTRACT validation token. V-03's GATE-8B required the `VALIDATION-DERIVATION:` token as a named structural element co-located with DECLARE CONTRADICTION in the prose block. Single-axis evidence only — V-05 combined CONSISTENCY-RULE with other axes but did not isolate VALIDATION-DERIVATION as an independent surface; a second variation axis isolating VALIDATION-DERIVATION independently (e.g., combined VALIDATION-DERIVATION + another axis without CONSISTENCY-RULE confound, or VALIDATION-DERIVATION + CONSISTENCY-RULE combined confirming both surfaces simultaneously) is needed before the surface can be frozen. The C-45 design surface is complementary to C-44: C-44 declares the derivation algorithm in the pre-trace CHECKER ALGORITHM; C-45 would surface the derivation inline at Step 8b where the contradiction event fires, adding a third cross-reference point to the HALT-EXPECTED-BOUNDARY consistency chain.

---

## Two new criteria from R18 excellence signals (carried from v17)

| New criterion | R18 excellence signal | What is testable |
|---|---|---|
| **C-42** Step 8b DECLARE CONTRADICTION intertextual HALT-EXPECTED-BOUNDARY match flag | ES-1 (V-02 + V-05): Two independent variation axes — single-axis C-42 surface 1 (V-02) and combined C-42 surface 1 + surface 2 (V-05) — both produced `DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [which arm] -- matches HALT-EXPECTED-BOUNDARY: [yes/no]` with all four fields in Step 8b prose before Step 8c is populated; V-02's GATE-8B explicitly required the fourth field and named the substitution rule (yes if contradiction fires at predicted boundary, no if at a different boundary); the four-field form is stable across single-axis (V-02 evidence) and combined-axis (V-05 evidence) enforcement surfaces, confirming the Tier B+ design surface identified in v16 | Is `DECLARE CONTRADICTION:` present as a named structural token in Step 8b prose with all four fields? Does it carry a BC-N boundary ID? Does it carry a descriptive label? Does it carry an `arm:` field naming the specific contradicted arm? Does it carry a `matches HALT-EXPECTED-BOUNDARY:` field with a filled boolean value (`yes` or `no`) rather than a literal placeholder? Is the value machine-derivable: `yes` iff the contradiction fires at the boundary named in HALT-EXPECTED-BOUNDARY, `no` iff it fires at a different boundary? Is the token machine-greppable via `DECLARE CONTRADICTION: BC-` without semantic prose reading? |
| **C-43** Step 12 FAIL-CATEGORY closed-vocabulary token per finding row | ES-2 (V-03 + V-05): Two independent variation axes — single-axis C-42 surface 2 (V-03) and combined C-42 surface 1 + surface 2 (V-05) — both produced `FAIL-CATEGORY: [vocabulary token]` on every Step 12 finding row, with the six-item closed vocabulary (AUTH \| BOUNDARY \| CONTRACT \| TIMEOUT \| STATE \| PERMISSION) specified in a named category-definitions block and enforced by GATE-12; V-03's single-axis isolation confirms the surface is independently elicitable without the C-42 surface 1 confound; V-05's combined evidence confirms vocabulary adherence under dual-axis token pressure | Is a `FAIL-CATEGORY:` token present on every finding row in Step 12? Is each FAIL-CATEGORY value drawn exclusively from the closed vocabulary: AUTH, BOUNDARY, CONTRACT, TIMEOUT, STATE, PERMISSION? Is a category-definitions block present naming all six vocabulary items? Is FAIL-CATEGORY machine-greppable via `^FAIL-CATEGORY:` on each finding row without reading Failure Mode prose? Are out-of-vocabulary values (e.g., "SECURITY", "PERFORMANCE", "SCHEMA") absent from all finding rows? On a clean trace, does the clean trace row carry `FAIL-CATEGORY: N/A`? |

---

## Key design decisions (R18, carried from v17)

**C-42 vs C-40:** C-40 tests that `DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [which arm]` is present as a named structural token in Step 8b prose at the contradiction boundary before Step 8c is populated — the three-field form creates a machine-greppable named event at the prose surface. C-42 tests that a fourth field `matches HALT-EXPECTED-BOUNDARY: [yes/no]` is additionally present, creating an intertextual cross-reference between the Step 8b contradiction event and the Phase 0A TRACE CONTRACT pre-declaration — the field makes the relationship between the actual contradiction event and the predicted boundary machine-checkable at the Step 8b prose surface without reading the TRACE CONTRACT validation token. Three-field DECLARE CONTRADICTION present (C-40 PASS) but fourth field absent = C-40 PASS + C-42 FAIL. Four-field form with filled `yes` or `no` value (not a literal `[yes/no]` placeholder) = C-40 PASS + C-42 PASS.

**C-42 vs C-39:** C-39 tests that a TRACE CONTRACT block pre-declares the halt boundary as `HALT-EXPECTED-BOUNDARY:` before the trace executes, and that a post-execution `TRACE CONTRACT validation:` token confirms or falsifies the prediction — the contract and its post-execution confirmation are machine-checkable as a two-token pair. C-42 tests that the Step 8b DECLARE CONTRADICTION token additionally carries an inline cross-reference to the TRACE CONTRACT prediction at the point where the contradiction event fires — the `matches HALT-EXPECTED-BOUNDARY: [yes/no]` field links the contradiction event directly to the pre-declaration without requiring the reader to navigate from Step 8b prose to the TRACE CONTRACT validation token. TRACE CONTRACT prediction and validation present (C-39 PASS) but DECLARE CONTRADICTION carries no inline cross-reference field = C-39 PASS + C-42 FAIL.

**C-43 vs C-06:** C-06 tests that the error path is traced end-to-end — Step 12 Findings carries Failure Mode per finding with GATE-12 prohibiting blank Failure Mode cells and requiring an explicit clean-trace declaration when no issues are found. C-43 tests that each finding row additionally carries a `FAIL-CATEGORY:` machine-greppable token assigned from a closed six-item vocabulary — making finding classification machine-checkable by fixed-token grep without reading Failure Mode prose. Step 12 Findings with Failure Mode present (C-06 PASS) but no FAIL-CATEGORY token on finding rows = C-06 PASS + C-43 FAIL. FAIL-CATEGORY present on every finding row with values exclusively from the closed vocabulary = C-06 PASS + C-43 PASS.

**C-43 vs C-03:** C-03 tests that a failure point is identified at each boundary — the finding is present and the failure mode is named at the boundary level. C-43 tests that the failure mode category is additionally typed as a machine-greppable closed-vocabulary token per finding row in Step 12, enabling automated classification of finding types without semantic reading. Failure points present at each boundary (C-03 PASS) but Step 12 findings lack FAIL-CATEGORY = C-03 PASS + C-43 FAIL.

**Dependency edges (R18):**
- C-42 depends on C-40 AND C-39 (C-40 establishes the three-field DECLARE CONTRADICTION surface in Step 8b — the fourth field extends this named token surface without replacing it; C-39 establishes HALT-EXPECTED-BOUNDARY as a pre-execution named structural token in the TRACE CONTRACT — the `matches HALT-EXPECTED-BOUNDARY:` field cross-references this token by name; both the prose contradiction surface and the pre-declared boundary name must exist before requiring the inline intertextual cross-reference field that connects them)
- C-43 depends on C-06 (Step 12 Findings with Failure Mode must be established — C-06 requires explicit Failure Mode per finding and prohibits "no issues found" closures without a clean-trace declaration; FAIL-CATEGORY extends this finding structure with a machine-greppable typed classification token without replacing the Failure Mode prose; the Findings structure and gate enforcement must exist before requiring a typed vocabulary field on each row)

---

## Signals not promoted in v17 — promoted to C-42 and C-43 in v17 (carried from v17)

Both C-42 design surfaces identified in v16 have been promoted:

1. **DECLARE CONTRADICTION intertextual HALT-EXPECTED-BOUNDARY match flag** → promoted to **C-42** (V-02 single-axis + V-05 combined = two independent axes)
2. **Error path category taxonomy** → promoted to **C-43** (V-03 single-axis + V-05 combined = two independent axes with frozen six-item vocabulary)

---

## Two new criteria from R17 excellence signals (carried from v17)

| New criterion | R17 excellence signal | What is testable |
|---|---|---|
| **C-40** Step 8b DECLARE CONTRADICTION prose token | ES-1 (V-02 + V-05): Two independent variation axes — single-axis formal register (V-02) and three-axis combined formal register + DECLARE CONTRADICTION + TRACE CONTRACT (V-05) — both produced `DECLARE CONTRADICTION: BC-[N] -- [label] -- arm: [which arm is contradicted]` as a named structural token within the Step 8b prose block at the contradiction boundary row, appearing before the Step 8c table is populated for that row; the token surface is stable across axis combinations, confirming the Tier B design surface identified in v15 | Is `DECLARE CONTRADICTION:` present as a named structural token in Step 8b prose (not Step 8c)? Does it appear within the Step 8b confirmation block for the contradiction boundary row before the Step 8c table is populated? Does it carry a boundary identifier in BC-N form? Does it carry a descriptive boundary label? Does it carry an `arm:` field naming the specific coherence arm that is contradicted (Step3-Auth, Step8a-Invoked, or Step11-Params)? Is the token machine-greppable via fixed-token grep (`DECLARE CONTRADICTION: BC-`) without semantic prose reading? |
| **C-41** Pre-trace CHECKER ALGORITHM with HALT-EXPECTED-BOUNDARY reference | ES-2 (V-04): The Algorithm-Declarant role (Phase 0B) emitted the CHECKER ALGORITHM block before any trace step executes, with the HALT-RULE explicitly referencing `HALT-EXPECTED-BOUNDARY` as a named structural token within the halt predicate — making the predicted halt boundary a named component of the algorithm declaration itself, not merely a post-execution validation target; the Platform Expert reproduced CHECKER ALGORITHM verbatim at Step 8 Header, preserving the HALT-EXPECTED-BOUNDARY reference in the HALT-RULE | Is the CHECKER ALGORITHM block present before Step 1 executes (Phase 0, Phase 0B, or equivalent pre-trace placement)? Does the HALT-RULE within the pre-trace block reference `HALT-EXPECTED-BOUNDARY` as a named structural token within the halt predicate (not merely as a post-execution pointer)? Is the HALT-RULE predicate of the form "halt fires when Step 8b prose asserts coherence for HALT-EXPECTED-BOUNDARY AND Step 8c Match? = N for HALT-EXPECTED-BOUNDARY row"? Is CHECKER ALGORITHM reproduced verbatim at Step 8 Header? Does the verbatim reproduction at Step 8 Header preserve the HALT-EXPECTED-BOUNDARY reference in the HALT-RULE? Is pre-trace placement checkable by confirming the CHECKER ALGORITHM block appears before Step 0 table without reading trace execution? |

---

## Key design decisions (R17, carried from v17)

**C-40 vs C-30:** C-30 tests that both the Step 8b prose confirmation and the Step 8c Match? table are required and that a prose/Match? divergence is structurally detectable — the dual-surface contradiction architecture is present and the mismatch is format-detectable without prose reading. C-40 tests that the contradiction event is additionally named as a structural token (`DECLARE CONTRADICTION:`) within the Step 8b prose surface at the exact boundary row where Match? = N fires, creating a third machine-greppable surface for the contradiction event. Dual-surface architecture present (C-30 PASS) but contradiction event embedded in prose without a named token = C-30 PASS + C-40 FAIL. `DECLARE CONTRADICTION:` token present in Step 8b prose with BC-N, label, and arm fields before Step 8c is populated = C-30 PASS + C-40 PASS.

**C-40 vs C-31:** C-31 tests that the contradiction halt is a named typed structural event with machine-greppable `CONTRADICTION SIGNAL: Seq# N` label in Step 8c and required `Scope String Correction` Rem# output — the halt event is typed and its remediation is required. C-40 tests that the contradiction event is also named at the Step 8b prose surface before the Step 8c table is populated — the event is labeled at the moment it fires in prose, not only at the point where halt is declared in the output table. `CONTRADICTION SIGNAL` present in Step 8c (C-31 PASS) but Step 8b prose carries no named token for the contradiction event = C-31 PASS + C-40 FAIL.

**C-41 vs C-37:** C-37 tests that the CHECKER ALGORITHM block is present in the Step 8 Header with MATCH-RULE, HALT-RULE, and OUTPUT-RULE as named machine-greppable tokens — the algorithm is structurally present and parseable. C-41 tests that the CHECKER ALGORITHM block is additionally declared before Step 1 (pre-trace placement) and that the HALT-RULE within the pre-trace declaration references `HALT-EXPECTED-BOUNDARY` as a named token in the halt predicate, binding the algorithm declaration to the specific predicted halt boundary before any boundary evidence is gathered. CHECKER ALGORITHM present at Step 8 Header only (C-37 PASS) with no pre-trace placement = C-37 PASS + C-41 FAIL. Pre-trace CHECKER ALGORITHM present with HALT-RULE encoding `HALT-EXPECTED-BOUNDARY` as a named predicate component = C-37 PASS + C-41 PASS.

**C-41 vs C-39:** C-39 tests that a TRACE CONTRACT block pre-declares the specific halt boundary (HALT-EXPECTED-BOUNDARY token) and the dual-surface predicate (HALT-EXPECTED-CONDITION token) before the trace executes, and that a TRACE CONTRACT validation token confirms the prediction after Step 8c. C-41 tests that the CHECKER ALGORITHM HALT-RULE additionally references `HALT-EXPECTED-BOUNDARY` as a named token within the halt predicate — making the algorithm declaration aware of the specific predicted boundary from Phase 0, not just the generic dual-surface firing condition. TRACE CONTRACT present (C-39 PASS) but HALT-RULE encodes only the generic dual-surface predicate without referencing HALT-EXPECTED-BOUNDARY by name = C-39 PASS + C-41 FAIL.

**Dependency edges (R17):**
- C-40 depends on C-30 (dual-surface contradiction signal must be established — both the Step 8b prose surface and the Step 8c Match? surface must exist before requiring a named token on the Step 8b surface; C-30 also establishes that VT# scope strings propagate consistently across both surfaces, providing the structural context in which `DECLARE CONTRADICTION: BC-N -- label -- arm:` is interpretable without prose reading)
- C-41 depends on C-37 AND C-39 (C-37 establishes the CHECKER ALGORITHM block structure with HALT-RULE as a named token — the pre-trace CHECKER ALGORITHM in C-41 inherits this schema and must include HALT-RULE in the same named-token format; C-39 establishes HALT-EXPECTED-BOUNDARY as a pre-execution structural token whose name is referenced by the HALT-RULE in C-41 — both must be present before requiring the algorithm declaration to bind to the predicted boundary by name)

---

## One new criterion from R16 excellence signal (carried from v17)

| New criterion | R16 excellence signal | What is testable |
|---|---|---|
| **C-39** Pre-execution halt boundary declaration | ES-1 (V-03, Tier A): A `TRACE CONTRACT` block declared before any trace step executes carries `HALT-EXPECTED-BOUNDARY: "BC-5 -- PreOperation elevated FLS bypass"` and `HALT-EXPECTED-CONDITION: "Step 8b prose asserts coherence for BC-5 AND Step 8c Match? = N for BC-5 row"` as machine-greppable tokens, pre-committing the specific boundary predicted to trigger the dual-surface halt and the predicate that will fire it; after the trace executes, a `TRACE CONTRACT validation:` token confirms whether the predicted boundary matched the actual `Row-Verdict = HALT` row in Step 8c — the pre-declaration and confirmation are both checkable by machine without semantic prose reading | Is a TRACE CONTRACT block present in the prompt before any trace step begins? Does it carry a `HALT-EXPECTED-BOUNDARY:` token naming the specific predicted halt boundary (boundary ID and descriptive label)? Does it carry a `HALT-EXPECTED-CONDITION:` token naming the dual-surface predicate for that boundary (Step 8b prose state AND Step 8c Match? = N for the named boundary row)? After the trace executes, is a `TRACE CONTRACT validation:` token present? Does the validation token confirm whether HALT-EXPECTED-BOUNDARY matches the `Row-Verdict = HALT` row in Step 8c? Is the match checkable by comparing `HALT-EXPECTED-BOUNDARY` boundary ID against the `Row-Verdict = HALT` row without reading prose? |

---

## Key design decisions (R16, carried from v17)

**C-39 vs C-38:** C-38 tests that the HALT-RULE in the CHECKER ALGORITHM block encodes the dual-surface contradiction architecture as its halt trigger — declaring that halt fires when Step 8b prose asserts coherence AND Step 8c Match? = N simultaneously — rather than syntactically naming only the output token condition (e.g., `HALT-RULE: Row-Verdict = HALT iff Match? = N`); the halt predicate is expressed as a causal dual-surface rule such that the logical basis for halt (the simultaneous presence of a prose-coherent claim and a table-level mismatch) is readable from the HALT-RULE token itself without reference to any other section. C-39 tests that a pre-execution TRACE CONTRACT additionally pre-commits the specific boundary predicted to trigger that halt, pairing a machine-greppable `HALT-EXPECTED-BOUNDARY` token (naming the specific BC-N boundary before evidence is gathered) with a post-execution `TRACE CONTRACT validation` confirmation token (confirming whether the predicted boundary matched the actual HALT row). HALT-RULE encodes the generic dual-surface predicate (C-38 PASS) but no boundary is pre-declared before execution = C-38 PASS + C-39 FAIL. Pre-execution HALT-EXPECTED-BOUNDARY + post-execution validation both present = C-38 PASS + C-39 PASS.

**Dependency edge:**
- C-39 depends on C-38 AND C-35 (C-38 establishes the dual-surface HALT-RULE encoding — the generic predicate that the pre-declared condition names and the validation contract references; C-35 provides the Row-Verdict machine token in Step 8c — the post-execution match check compares HALT-EXPECTED-BOUNDARY against the specific Row-Verdict = HALT row by boundary ID without prose reading; both must be present before requiring the pre-declaration and confirmation contract to be machine-checkable)

---

## One new criterion from R15 excellence signal (carried from v17)

| New criterion | R15 excellence signal | What is testable |
|---|---|---|
| **C-38** HALT-RULE dual-surface architecture encoding | ES-1 (V-01): The HALT-RULE in the CHECKER ALGORITHM block explicitly encodes the C-30 dual-surface contradiction architecture as its halt trigger — declaring that halt fires when Step 8b prose asserts coherence AND Step 8c Match? = N simultaneously — rather than syntactically naming only the output token condition (e.g., `HALT-RULE: Row-Verdict = HALT iff Match? = N`); the halt predicate is expressed as a causal dual-surface rule such that the logical basis for halt (the simultaneous presence of a prose-coherent claim and a table-level mismatch) is readable from the HALT-RULE token itself without reference to any other section | Is the HALT-RULE present as a named machine-greppable token in the CHECKER ALGORITHM block (C-37 PASS required)? Does the HALT-RULE explicitly reference Step 8b prose state (a coherence claim or equivalent)? Does the HALT-RULE explicitly reference Step 8c Match? = N? Does the HALT-RULE declare that halt fires when both conditions hold simultaneously? Is the dual-surface condition expressed as the logical basis for halt rather than as a pointer to an output token (Row-Verdict = HALT)? Is the halt predicate interpretable from the HALT-RULE label alone without reading VT-N lines or Step 8c data? |

---

## Key design decisions (R15, carried from v17)

**C-38 vs C-37:** C-37 tests that the CHECKER ALGORITHM block is present in the Step 8 Header and that MATCH-RULE, HALT-RULE, and OUTPUT-RULE are declared as named machine-greppable tokens — the algorithm is structurally present and parseable by fixed-token grep. C-38 tests that the HALT-RULE token additionally encodes the dual-surface contradiction architecture as its trigger predicate: Step 8b prose coherence claim AND Step 8c Match? = N simultaneously. HALT-RULE present as a syntactic pointer to the output token (e.g., `HALT-RULE: Row-Verdict = HALT iff Match? = N`) = C-37 PASS + C-38 FAIL. HALT-RULE present and encoding the dual-surface event as the logical basis for halt = C-37 PASS + C-38 PASS.

**Dependency edge:**
- C-38 depends on C-37 AND C-30 (C-37 establishes the CHECKER ALGORITHM block as a structural token in the Step 8 Header; C-30 establishes the dual-surface contradiction architecture — Step 8b prose surface AND Step 8c Match? table surface — being referenced by the HALT-RULE; both must be present before requiring the halt predicate to encode the dual-surface logic as a machine-greppable token phrase)

---

## One new criterion from R13 excellence signal (carried from v17)

| New criterion | R13 excellence signal | What is testable |
|---|---|---|
| **C-37** Checker algorithm declaration | ES-1 (V-03): The Step 8 Header carries a CHECKER ALGORITHM block immediately after TOKEN-COUNT, declaring MATCH-RULE, HALT-RULE, and OUTPUT-RULE as formal machine-greppable pseudocode tokens — the comparison predicate is machine-readable as a structural property of the header without semantic prose parsing; the algorithm declaration is independent of schema tokens and does not require reading VT-N lines to interpret the logic | Is a CHECKER ALGORITHM block present in the Step 8 Header? Does it appear immediately after TOKEN-COUNT (within the same Step 8 header section)? Does it declare MATCH-RULE, HALT-RULE, and OUTPUT-RULE as named machine-greppable tokens? Is the algorithm declaration structurally independent of VT-N schema tokens (no positional or semantic dependency on VT-N lines to interpret predicate logic)? Is algorithm logic parseable via fixed-token grep without semantic prose reading? |

---

## Key design decisions (R13, carried from v17)

**C-37 vs C-36:** C-36 tests that both checker input (VT-N quoted schema) and checker output (Row-Verdict + CHECK RESULT) are machine-parseable structural tokens within the prompt, such that the complete checker contract — parse input, compare, emit output — requires no prose reading at any step. C-37 tests that the checker algorithm itself — the comparison predicate (MATCH-RULE), the halt condition (HALT-RULE), and the output emission rule (OUTPUT-RULE) — is additionally declared as machine-greppable tokens in the Step 8 Header, such that the logic governing how the contract is executed is also readable from structure alone without semantic prose parsing. Full checker contract present (C-36 PASS) but algorithm declared as prose description rather than named machine-greppable tokens = C-36 PASS + C-37 FAIL.

**Dependency edge:**
- C-37 depends on C-36 (both machine-parseable input schema and externalized output tokens must be simultaneously established as the full checker contract before requiring the algorithm declaration that operates on them to also be a structural token — C-36 establishes the I/O contract, C-37 tightens the algorithm encoding)

---

## Three new criteria from R12 excellence signals (carried from v17)

| New criterion | R12 excellence signal | What is testable |
|---|---|---|
| **C-34** Structured VT-N schema input | ES-1 (V-03): The Step 8 Header VT# token list is declared in `VT-N: "exact string"` quoted format (one line per token) with a `TOKEN-COUNT: N` self-validation field, making the reference set machine-parseable via `^VT-[0-9]+: ".*"$` without prose reading | Is the VT# token list declared in `VT-N: "..."` quoted format, one per line? Is a `TOKEN-COUNT: N` field present? Does TOKEN-COUNT match the count of VT-N lines? Can the full reference set be extracted via `^VT-[0-9]+: ".*"$` without reading surrounding prose? |
| **C-35** Row-level verdict token | ES-2 (V-04): Step 8c table carries a `Row-Verdict: PASS/HALT` column per row and a `CHECK RESULT: PASS/FAIL -- N rows, M HALT rows` summary line after the table, externalizing checker output as machine tokens — no reading of Match? values or Step 8b prose required to identify halt events | Is a `Row-Verdict` column present in Step 8c with `PASS` or `HALT` per row? Is a `CHECK RESULT:` summary line present after the table? Can halt events be identified by scanning `Row-Verdict` for `HALT` without reading Match? values or Step 8b prose? |
| **C-36** Full checker contract | ES-3 (V-05 only): Both checker input (Step 8 Header VT-N schema, parseable via `^VT-[0-9]+: ".*"$` + TOKEN-COUNT) and checker output (Row-Verdict per row + CHECK RESULT summary) are machine-parseable structural tokens within the prompt, such that the complete checker contract — parse input, compare, emit output — requires no prose reading at any step | Are both C-34 (structured input schema) and C-35 (externalized output tokens) simultaneously present? Can the complete checker contract be expressed as: (1) parse `^VT-[0-9]+: ".*"$` from header, (2) scan `Row-Verdict` for `HALT`, (3) read `CHECK RESULT`? Is no prose reading required at any step? Does TOKEN-COUNT self-validate schema completeness without positional parsing? |

---

## Key design decisions (R12, carried from v17)

**C-34 vs C-32:** C-32 tests that a VT# token list is co-located at the Step 8 header boundary making Match? computation self-contained — no structural dependency on Steps 0, 3, or 11. C-34 tests that this list is declared in a machine-parseable `VT-N: "..."` quoted schema format with `TOKEN-COUNT` self-validation, such that the reference set can be fully extracted by regex without reading surrounding prose. VT# list present as prose re-affirmation = C-32 PASS + C-34 FAIL.

**C-35 vs C-31:** C-31 tests that the contradiction halt is a named typed event with machine-greppable `CONTRADICTION SIGNAL: Seq# N` label and required `Scope String Correction` Rem# output. C-35 tests that the halt is additionally externalized as a per-row machine token (`Row-Verdict = HALT`) with a `CHECK RESULT` summary — named halt event present but halt not surfaced as per-row token = C-31 PASS + C-35 FAIL.

**C-36 vs C-33:** C-33 tests that all three pre-conditions (reference set, named halt type, Rem# format) are simultaneously present making the automated-check predicate specifiable. C-36 tests that the full checker contract is machine-expressed — both input schema (VT-N quoted format) and output tokens (Row-Verdict + CHECK RESULT) are structural tokens within the prompt, such that no prose reading is required at any step. Pre-conditions present and predicate specifiable (C-33 PASS) but checker I/O not fully machine-parseable without prose reading = C-33 PASS + C-36 FAIL.

**R12 dependency edges:**
- C-34 depends on C-32
- C-35 depends on C-29 and C-31
- C-36 depends on C-34 AND C-35

---

## Three new criteria from R11 excellence signals (carried from v17)

| New criterion | R11 excellence signal | What is testable |
|---|---|---|
| **C-31** Named contradiction halt type | ES-1 (V-03): The contradiction between Step 8b prose and Step 8c Match? is introduced as a named typed structural event with a machine-greppable label (`CONTRADICTION SIGNAL: Seq# N`) and requires a typed Rem# output (`Scope String Correction`) before the trace may advance | Is the contradiction event named with a typed label? Is the label machine-greppable (fixed token, no prose variation)? Is a Rem# output required? Is the Rem# type specified as `Scope String Correction`? |
| **C-32** Self-contained Match? computation | ES-2 (V-04): Step 8 header carries a re-affirmation of the VT# token list at the step boundary, making Match? computation self-contained — a checker needs only the Step 8 header and the Step 8c table, with zero dependency on Steps 0, 3, or 11 | Is a VT# token list present at the Step 8 header boundary? Can Match? be fully computed from only the Step 8 header + Step 8c table? Is there no structural dependency on Steps 0, 3, or 11 for Match? computation? |
| **C-33** Automated-check predicate completeness | ES-3 (V-05 only): All three automated-check pre-conditions are simultaneously present — (a) reference set co-located at Step 8 header, (b) named halt type with greppable label, (c) Rem# format requirement — such that the automated-check predicate is fully specifiable without semantic reading of prose or cross-section navigation | Are all three pre-conditions simultaneously present? Can an automated checker operate using only Step 8 header + Step 8c table + halt label pattern? Is the predicate fully specifiable from structural tokens alone? |

---

## Three new criteria from R10 excellence signals (carried from v17)

| Criterion | R10 excellence signal | What is testable |
|---|---|---|
| **C-28** Coherence-spine progression gate | ES-1 (V-03): Step 8b contains a REQUIRED prose confirmation per Gap?=Y boundary, explicitly verifying all three link arms (Step 8a → Step 11 → Step 7/9) before Step 9 may proceed | Is a per-boundary confirmation present at Step 8b? Does it name all three link arms? Is it marked REQUIRED? Does it structurally block advancement to Step 9? |
| **C-29** Scope-string coherence table | ES-2 (V-04): Step 8c contains a required table with columns Step3-Auth / Step8a-Invoked / Step11-Params / Match? for each Gap?=Y boundary, positioned before Step 9 | Is a Step 8c table present? Does it carry all four required columns? Is Match? binary (Y/N) per row? Is it required before Step 9? Are VT# scope strings present in column values? |
| **C-30** Dual-surface contradiction signal | ES-3 (V-05 only): Both Step 8b prose confirmation AND Step 8c Match? table are required; a mismatch (prose says coherent, Match? = N) is detectable from structure alone without semantic reading of prose; VT# scope strings appear consistently across both surfaces | Are both C-28 and C-29 surfaces present and both REQUIRED? Is there a structural rule making prose / Match? divergence self-evidencing? Do VT# scope strings propagate consistently from Step 8b prose to Step 8c column values? |

---

## Full aspirational tier — C-21 through C-44

| # | Criterion | Points | Depends on |
|---|---|---|---|
| C-21 | Step 8a scope-string format | 5 | C-08 |
| C-22 | Step 8a completeness gate | 5 | C-21 |
| C-23 | VT# token vocabulary declared | 5 | C-08 |
| C-24 | Step 11 param-set co-location | 5 | C-08 |
| C-25 | Step 8 header boundary marker | 5 | C-23 |
| C-26 | Gap?=Y boundary count match | 5 | C-22, C-25 |
| C-27 | Step 8b required-field marker | 5 | C-26 |
| C-28 | Coherence-spine progression gate | 5 | C-27 |
| C-29 | Scope-string coherence table | 5 | C-26 |
| C-30 | Dual-surface contradiction signal | 5 | C-28, C-29 |
| C-31 | Named contradiction halt type | 5 | C-29 |
| C-32 | Self-contained Match? computation | 5 | C-23, C-25 |
| C-33 | Automated-check predicate completeness | 5 | C-31, C-32 |
| C-34 | Structured VT-N schema input | 5 | C-32 |
| C-35 | Row-level verdict token | 5 | C-29, C-31 |
| C-36 | Full checker contract | 5 | C-34, C-35 |
| C-37 | Checker algorithm declaration | 5 | C-36 |
| C-38 | HALT-RULE dual-surface architecture encoding | 5 | C-37, C-30 |
| C-39 | Pre-execution halt boundary declaration | 5 | C-38, C-35 |
| C-40 | Step 8b DECLARE CONTRADICTION prose token | 5 | C-30 |
| C-41 | Pre-trace CHECKER ALGORITHM with HALT-EXPECTED-BOUNDARY reference | 5 | C-37, C-39 |
| C-42 | Step 8b DECLARE CONTRADICTION intertextual HALT-EXPECTED-BOUNDARY match flag | 5 | C-40, C-39 |
| C-43 | Step 12 FAIL-CATEGORY closed-vocabulary token per finding row | 5 | C-06 |
| C-44 | CHECKER ALGORITHM CONSISTENCY-RULE structural derivation token | 5 | C-42, C-39, C-37 |

**Aspirational subtotal (C-21–C-44):** 24 criteria × 5 = 120 pts of the 185 pt aspirational tier. Criteria C-08 through C-20 (13 criteria × 5 = 65 pts) are stable and inherited from v12 without modification.

---

## Tier summary

| Tier | Criteria | Points |
|---|---|---|
| Essential | C-01–C-04 | 60 |
| Recommended | C-05–C-07 | 30 |
| Aspirational | C-08–C-44 | 185 |
| **Total** | **44 criteria** | **275** |

**Golden threshold:** all 4 essential PASS AND composite >= 220/275 (80%).

---

## Dependency chain — checker contract stack (C-28 → C-44)

```
C-28 (coherence gate)  C-29 (coherence table)
       \                    /         \
        C-30 (dual-surface) C-31 (halt type)
          |    \                \
          |     \             C-35 (row verdict)    C-32 (self-contained)
          |      \                 \                    \
        C-40      \             C-36 (full contract) <- C-34 (VT-N schema)
   (DECLARE        \                 \
  CONTRADICTION)    \             C-37 (algorithm declaration)
       |             \                 \
       |              \             C-38 (HALT-RULE dual-surface encoding)
       |               \                 \               \
     C-42               \             C-35 (row verdict) [reused]
  (matches HALT-          \               \
  EXPECTED-BOUNDARY)       \              C-39 (pre-execution halt boundary) <---+
       |                    \                 \                                   |
       +-------- C-39 -------+             C-37 (algorithm) [reused]             |
     (also depends on C-39                     \                                 |
      for HALT-EXPECTED-BOUNDARY                C-41 (pre-trace CHECKER ALGORITHM|
      token to cross-reference)                      + HALT-EXPECTED-BOUNDARY ref)
                                                             |
                                     C-44 (CONSISTENCY-RULE) <-- C-42, C-39, C-37
                              (fourth rule declaring C-42→C-39 derivation path)
```

**C-43 (FAIL-CATEGORY)** depends on **C-06** (Recommended: Step 12 Findings with Failure Mode) — it extends the finding structure laterally, independently of the checker contract stack above.

```
C-06 (error path end-to-end — Recommended)
  |
C-43 (FAIL-CATEGORY closed-vocabulary token per finding row)
```

**C-44** closes the four-token consistency chain. The chain now reads: HALT-EXPECTED-BOUNDARY (Phase 0A, C-39) → HALT-EXPECTED-BOUNDARY in HALT-RULE (Phase 0B, C-41) → `matches HALT-EXPECTED-BOUNDARY: [yes/no]` in DECLARE CONTRADICTION (Step 8b, C-42) → TRACE CONTRACT validation outcome (post-execution, C-39) → CONSISTENCY-RULE structural derivation (CHECKER ALGORITHM, C-44). The CONSISTENCY-RULE is the fourth named rule in the CHECKER ALGORITHM block that makes the C-42 → C-39 derivation machine-verifiable as a structural algorithm declaration rather than a prose instruction in GATE-TC: `matches HALT-EXPECTED-BOUNDARY: yes` → "Contract prediction confirmed"; `matches HALT-EXPECTED-BOUNDARY: no` → "falsified -- actual halt boundary was [BC-N label]". The C-45 design surface (not yet promoted) targets the GATE-8B VALIDATION-DERIVATION requirement: surfacing the derivation inline in Step 8b prose at the point the contradiction event fires, adding a third cross-reference point to the chain between C-42 and C-44.
