# flow-integration — Round 8 Scoring

## Results

| Rank | Variation | Score | C-24 | C-25 |
|------|-----------|-------|------|------|
| 1 (tied) | V-01 Role Sequence + Obligation Table | **177/177** | 4-row table | Schema + VOCABULARY RULE |
| 1 (tied) | V-02 Full-Table Schema-Only | **177/177** | 4-row table | Schema-only (no VOCABULARY RULE) |
| 1 (tied) | V-04 Phase Architecture + Terminal Coda | **177/177** | 4-row table in Phase 1 | Schema + VOCABULARY RULE |
| 1 (tied) | V-05 Non-Standard + Prohibition | **177/177** | Non-standard 4-row table | Non-standard schema + prohibition |
| 5 | **V-03 Mixed-Format Probe (Q2)** | **172/177** | PASS | **FAIL — no column header cells** |

---

## Open Question Verdicts

**Q1 — C-23 terminal-position constraint (V-04 definitive): CONFIRMED REAL.**
The explicit dual language — coda header `*(no phase number — appended after Phase 3, the last numbered phase)*` + prose "It does not appear between any two numbered phases; it does not displace or renumber any existing element" — achieves a clean PASS. The R7 V-04 failure (coda between Phase 2 and Phase 3) was structural, not stylistic. C-23 should be updated to make terminal-position mandatory.

**Q2 — C-25 column header requirement (V-03 definitive): COLUMN HEADERS REQUIRED.**
Inline flag tokens in pipe-delimited entries satisfy C-22 (VOCABULARY RULE covers token identity) but not C-25. The C-25 mechanism is header/row-term comparison, which requires actual Markdown table column header cells. No column headers = no schema comparison surface = C-25 FAIL.

---

## Excellence Signals (3 new patterns)

1. **Schema-only C-25** — VOCABULARY RULE is unnecessary when C-24 + C-25 table schemas share the same token. Structural mechanism subsumes declarative. V-02 confirms schema-only achieves 177/177.

2. **Dual-surface C-22/C-25 for non-standard terms** — Schema detects substitution at the table surface (column header mismatch); explicit canonical-substitution prohibition blocks it at the prose/annotation surface. YOU MUST NOT naming specific forbidden tokens is stronger than a generic instruction.

3. **Explicit terminal-position formula for C-23** — `*(no [frame-unit] number — appended after [last element], the last numbered [frame-unit])*` + "does not appear between any two numbered [frame-units]" is the definitive pattern for any outer frame style.

```json
{"top_score": 177, "all_essential_pass": true, "new_patterns": ["schema-only C-25 enforcement is sufficient — dropping VOCABULARY RULE and relying solely on obligation-table-row-term-to-inventory-column-header schema identity achieves full C-25 score; the structural mechanism subsumes the declarative one", "canonical substitution prohibition + schema alignment = dual-surface C-22/C-25 coverage for non-standard terms — schema detects substitution at table surface, prohibition blocks it at prose/annotation surface; explicit YOU MUST NOT naming specific canonical forbidden terms is required", "explicit terminal-position language in coda header + supporting prose sentence definitively satisfies C-23 in any outer frame — formula: no-number annotation + 'appended after [last element] — the last numbered element' + 'does not appear between any two numbered [elements]'"]}
```
y flag alignment | PASS | Inventory table column headers [forgotten-call] [assumed-to-work] [unknown-system] [delegation-chain] trace to obligation categories |
| C-22 C-19/C-21 vocabulary unification | PASS | VOCABULARY RULE block: "Column header `[forgotten-call]` = OBL-1 Obligation Term 'forgotten-call'" × four; token identity mechanically verifiable by table schema comparison; semantic correspondence alone does not satisfy |
| C-23 Unnumbered coda | PASS | `**CROSS-STAGE CODA** *(no stage number — appended after Stage 3)*` — terminal, unnumbered, after last numbered stage |
| **C-24 Four-obligation table schema** | **PASS** | 4-row obligation table with Obligation Term column; one row per category; appears before Stage 1 inventory gate; missing row would be structurally absent |
| **C-25 Schema-aligned C-22 enforcement** | **PASS** | Inventory table column headers ([forgotten-call], [assumed-to-work], [unknown-system], [delegation-chain]) are exact tokens from C-24 obligation table Obligation Term cells; VOCABULARY RULE reinforces but schema comparison is the structural mechanism |

**Score: 177 / 177**

---

## V-02 — Full-Table Format + C-24/C-25 Schema-Only Enforcement

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Call inventory | PASS | Markdown inventory table with Call ID, Target System, Call Type, Confidence, four flag columns |
| C-02 Auth documentation | PASS | AUTH TABLE per call block with Mechanism and Auth gap rows |
| C-03 Request/response format | PASS | REQUEST/RESPONSE FORMAT TABLE per call with Method, Request key fields, Response key fields, Encoding as separate labeled rows |
| C-04 Error propagation | PASS | ERROR PROPAGATION TABLE per call with Error disposition row |
| C-05 Rate limit exposure | PASS | RATE LIMIT TABLE per call with Limit value, Burst risk, Throttle response |
| C-06 Retry/idempotency | PASS | RETRY AND IDEMPOTENCY TABLE per call with Retry strategy, Idempotent, Mitigation |
| C-07 Gap inventory | PASS | SECTION 3 GAP INVENTORY as Markdown table with Gap ID, Call ID, Gap Type, Severity, Rationale, Remediation columns |
| C-08 Severity ranking | PASS | Severity column in gap table + Rationale column; "MEDIUM and LOW are not exempt" stated |
| C-09 Remediation sketch | PASS | Remediation column; "required for HIGH; specific to this call" stated |
| C-10 Inventory-first gate | PASS | Section 1 inventory precedes Section 2; "Populate this table completely before opening Section 2" |
| C-11 Single-concern phase isolation | PASS | Each call block table labeled with one concern + named exclusion of others |
| C-12 Gate-enforced per-call completion | PASS | CALL-[N] COMPLETION GATE table with five check rows |
| C-13 Per-call section-level concern exclusion | PASS | Each concern table header names the single concern and explicitly names the other four as having their own tables |
| C-14 Five-concern per-call completion checklist | PASS | Five-row completion gate: Auth / Format / Rate limits / Retry/idempotency / Error propagation |
| C-15 Late-call inventory discipline | PASS | New-call rule: "add a row with all flag cells set before opening that call's block" |
| C-16 Expert persona declaration | PASS | EXPERT PERSONA section before Section 1; domain + four discovery obligations in 4-row table |
| C-17 In-block rate limit completeness | PASS | RATE LIMIT TABLE has Limit value, Burst risk, Throttle response as separate labeled rows |
| C-18 Cross-stage structure secondary positioning | PASS | AGGREGATION RULE with three-property positioning table format; "Traces with no cross-stage structures pass this rule by default" |
| C-19 Four-obligation scope | PASS | 4-row obligation table: forgotten-call, assumed-to-work, unknown-system, delegation-chain |
| C-20 Unconditional cross-stage stage | PASS | `CROSS-STAGE AGGREGATION STRUCTURES *(no section number — appended after Section 3)*` unconditional; default-path table: "No cross-stage structures produced in this trace" |
| C-21 Inventory flag alignment | PASS | Inventory table column headers [forgotten-call] [assumed-to-work] [unknown-system] [delegation-chain] trace to obligation categories |
| C-22 C-19/C-21 vocabulary unification | PASS | Instruction: "The flag column headers in the Section 1 inventory table are the Obligation Term column values above — use those exact tokens as column headers. A column header that does not match its corresponding Obligation Term cell fails schema alignment and is detectable without reading prose." Token identity structurally enforced without VOCABULARY RULE block. |
| C-23 Unnumbered coda | PASS | `**CROSS-STAGE AGGREGATION STRUCTURES** *(no section number — appended after Section 3)*` — unnumbered, after last section |
| **C-24 Four-obligation table schema** | **PASS** | 4-row obligation table with Obligation Term column before Section 1; row count is the completeness check |
| **C-25 Schema-aligned C-22 enforcement** | **PASS** | Inventory table column headers ARE the obligation row terms by explicit schema instruction; no VOCABULARY RULE required — schema comparison alone is the enforcement mechanism; this is the cleanest C-25 implementation |

**Score: 177 / 177**

**Notable:** Schema-only C-25 — dropping the VOCABULARY RULE entirely and relying solely on table schema alignment achieves full C-25 score. The structural mechanism subsumes the declarative one. Demonstrates that C-25 does not require a VOCABULARY RULE block; schema identity is sufficient.

---

## V-03 — Mixed-Format Probe: Table Obligation Block + Pipe-Delimited Inventory (Q2)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Call inventory | PASS | Pipe-delimited inventory entries with Call ID, target system, call type, confidence, flag tokens |
| C-02 Auth documentation | PASS | AUTH section per call block |
| C-03 Request/response format | PASS | REQUEST/RESPONSE FORMAT section with separate labeled fields |
| C-04 Error propagation | PASS | ERROR PROPAGATION section with explicit disposition |
| C-05 Rate limit exposure | PASS | RATE LIMITS section per call |
| C-06 Retry/idempotency | PASS | RETRY AND IDEMPOTENCY section per call |
| C-07 Gap inventory | PASS | STAGE 3 GAP INVENTORY structured blocks |
| C-08 Severity ranking | PASS | Severity + rationale fields per gap block |
| C-09 Remediation sketch | PASS | Remediation field for HIGH findings |
| C-10 Inventory-first gate | PASS | "Inventory gate: do not open Stage 2 until the inventory is complete" |
| C-11 Single-concern phase isolation | PASS | Single-concern sections with named exclusions |
| C-12 Gate-enforced per-call completion | PASS | CALL-[N] COMPLETION GATE five-item checklist |
| C-13 Per-call section-level concern exclusion | PASS | Single-concern declaration in each section |
| C-14 Five-concern per-call completion checklist | PASS | Five-item checklist |
| C-15 Late-call inventory discipline | PASS | NEW-CALL RULE: add to inventory before opening block |
| C-16 Expert persona declaration | PASS | EXPERT PERSONA before Stage 1 with domain and four obligations |
| C-17 In-block rate limit completeness | PASS | RATE LIMITS section has limit value, burst risk, throttle response as separate labeled fields |
| C-18 Cross-stage structure secondary positioning | PASS | AGGREGATION RULE with all three positioning properties |
| C-19 Four-obligation scope | PASS | 4-row obligation table: all four categories |
| C-20 Unconditional cross-stage stage | PASS | Unconditional CROSS-STAGE CODA with no-structures default path |
| C-21 Inventory flag alignment | PASS | Flag tokens [forgotten-call] [assumed-to-work] [unknown-system] [delegation-chain] appear in pipe-delimited inventory entries, tracing to obligation categories |
| C-22 C-19/C-21 vocabulary unification | PASS | VOCABULARY RULE: "Flag `[forgotten-call]` = OBL-1 term 'forgotten-call'" × four; "the persona term and the flag token are the same string" — declarative token identity satisfied |
| C-23 Unnumbered coda | PASS | CROSS-STAGE CODA unnumbered, appended after Stage 3 |
| **C-24 Four-obligation table schema** | **PASS** | 4-row obligation table with Obligation Term column; all four rows present before Stage 1 |
| **C-25 Schema-aligned C-22 enforcement** | **FAIL** | Pipe-delimited inventory has no column header cells. C-25 requires: "The C-21 inventory's flag marker column headers are the same tokens as the corresponding row terms in the C-24 obligation table." A pipe-delimited entry format has positional fields and inline flag tokens — there are no column header cells to compare against obligation table row terms. VOCABULARY RULE satisfies C-22 (token identity is declared), but schema alignment cannot be verified by header/row-term comparison because no column headers exist. C-25 requires actual Markdown table column header cells. |

**Score: 172 / 177** (−5 on C-25)

**Q2 Verdict: C-25 REQUIRES column header cells.** Inline obligation-term tokens in a pipe-delimited inventory satisfy C-22 (with a VOCABULARY RULE) but not C-25. The defining mechanism of C-25 is table schema comparison — a reviewer comparing column header cells to obligation table row term cells — which is impossible without Markdown table column headers. Pipe-delimited format with inline flag tokens passes C-22 but fails C-25.

---

## V-04 — Phase Architecture + Corrected Terminal Coda (Q1 Definitive)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Call inventory | PASS | Phase 1 inventory table with Call ID, Target System, Call Type, Confidence, four flag columns |
| C-02 Auth documentation | PASS | AUTH section per call block in Phase 2 |
| C-03 Request/response format | PASS | REQUEST/RESPONSE FORMAT section with method, request key fields, response key fields, encoding |
| C-04 Error propagation | PASS | ERROR PROPAGATION section with explicit disposition |
| C-05 Rate limit exposure | PASS | RATE LIMITS section per call with limit value/burst risk/throttle response |
| C-06 Retry/idempotency | PASS | RETRY AND IDEMPOTENCY section per call |
| C-07 Gap inventory | PASS | PHASE 3 GAP INVENTORY structured blocks |
| C-08 Severity ranking | PASS | Severity + rationale fields per gap; "MEDIUM and LOW are not exempt" |
| C-09 Remediation sketch | PASS | Remediation field for HIGH findings |
| C-10 Inventory-first gate | PASS | Phase 1 closes with explicit gate: "Phase 2 opens only after this condition is met" |
| C-11 Single-concern phase isolation | PASS | Single-concern sections within call blocks, with named exclusions |
| C-12 Gate-enforced per-call completion | PASS | CALL-[N] COMPLETION GATE five-item checklist |
| C-13 Per-call section-level concern exclusion | PASS | Each section names its single concern and explicitly names the other four |
| C-14 Five-concern per-call completion checklist | PASS | Five-item gate: auth / format / rate limits / retry/idempotency / error propagation |
| C-15 Late-call inventory discipline | PASS | NEW-CALL RULE: "add a row with all flag cells set before opening its call block" |
| C-16 Expert persona declaration | PASS | Expert Persona Declaration in Phase 1 before inventory gate |
| C-17 In-block rate limit completeness | PASS | RATE LIMITS section per call with limit value, burst risk, throttle response as separate labeled fields |
| C-18 Cross-stage structure secondary positioning | PASS | AGGREGATION RULE: all three properties stated |
| C-19 Four-obligation scope | PASS | 4-row obligation table in Phase 1: all four categories |
| C-20 Unconditional cross-stage stage | PASS | CROSS-STAGE CODA unconditional; fires regardless of Phase 2 output; explicit no-structures default path |
| C-21 Inventory flag alignment | PASS | Inventory table column headers [forgotten-call] [assumed-to-work] [unknown-system] [delegation-chain] trace to Phase 1 obligation table |
| C-22 C-19/C-21 vocabulary unification | PASS | VOCABULARY RULE: "Column header `[forgotten-call]` = OBL-1 Obligation Term 'forgotten-call'" × four; "Token identity is mechanically verifiable by table schema comparison... Vocabulary identity is required; semantic correspondence alone does not satisfy this rule" |
| C-23 Unnumbered coda | PASS | `**CROSS-STAGE CODA** *(no phase number — appended after Phase 3, the last numbered phase)*` — terminal position explicit; "It does not appear between any two numbered phases; it does not displace or renumber any existing element" — the R7 V-04 failure (coda between Phase 2 and Phase 3) is definitively corrected |
| **C-24 Four-obligation table schema** | **PASS** | 4-row obligation table in Phase 1 with Obligation Term column; all four rows; appears before inventory gate |
| **C-25 Schema-aligned C-22 enforcement** | **PASS** | Inventory table column headers ([forgotten-call], [assumed-to-work], [unknown-system], [delegation-chain]) are exact tokens from Phase 1 obligation table Obligation Term cells; VOCABULARY RULE makes this verifiable by schema comparison |

**Score: 177 / 177**

**Q1 Verdict: C-23 terminal-position constraint is CONFIRMED REAL AND DEFINITIVE.** R7 V-04 failed C-23 because the coda appeared between Phase 2 and Phase 3. R8 V-04 with explicit terminal-position language — "appended after Phase 3 — the last numbered element of the outer frame" and "It does not appear between any two numbered phases" — achieves a clean C-23 PASS. The constraint must be formalized in C-23: the unnumbered coda must be the terminal element of the outer frame; a coda placed before any remaining numbered element does not satisfy the composition-primitive definition even when unnumbered.

---

## V-05 — Non-Standard Terms + C-24/C-25 + Canonical Substitution Prohibition

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Call inventory | PASS | Stage 1 inventory table with non-standard flag columns: [shadow-call] [taken-for-granted] [fog-system] [relay-chain] |
| C-02 Auth documentation | PASS | AUTH section per call block |
| C-03 Request/response format | PASS | REQUEST/RESPONSE FORMAT section with separate labeled fields |
| C-04 Error propagation | PASS | ERROR PROPAGATION section with explicit disposition |
| C-05 Rate limit exposure | PASS | RATE LIMITS section per call with limit value/burst risk/throttle response |
| C-06 Retry/idempotency | PASS | RETRY AND IDEMPOTENCY section with retry strategy/idempotent/mitigation |
| C-07 Gap inventory | PASS | STAGE 3 GAP INVENTORY structured blocks (with non-standard gap types: fog-system, relay-chain) |
| C-08 Severity ranking | PASS | Severity + rationale per gap; "MEDIUM and LOW are not exempt"; "YOU MUST NOT use generic advice" |
| C-09 Remediation sketch | PASS | Remediation field for HIGH findings; specific-to-call requirement stated |
| C-10 Inventory-first gate | PASS | "YOU MUST complete the inventory table before opening Stage 2"; "Stage 2 does not open until every row has all flag cells explicitly set" |
| C-11 Single-concern phase isolation | PASS | Single-concern sections with named exclusions |
| C-12 Gate-enforced per-call completion | PASS | CALL-[N] GATE with "YOU MUST check all five before CALL-[N+1]" |
| C-13 Per-call section-level concern exclusion | PASS | Single-concern declaration in each section |
| C-14 Five-concern per-call completion checklist | PASS | Five-item gate |
| C-15 Late-call inventory discipline | PASS | NEW-CALL RULE: "YOU MUST NOT open a call block for any call not already in the Stage 1 inventory table" + add with all flags set first |
| C-16 Expert persona declaration | PASS | EXPERT PERSONA before Stage 1 with domain and four discovery obligations in 4-row table |
| C-17 In-block rate limit completeness | PASS | RATE LIMITS section per call with limit value, burst risk, throttle response as separate labeled fields |
| C-18 Cross-stage structure secondary positioning | PASS | AGGREGATION RULE with all three positioning properties |
| C-19 Four-obligation scope | PASS | 4-row obligation table: shadow-call, taken-for-granted, fog-system, relay-chain — row count is structural completeness for non-standard vocabulary |
| C-20 Unconditional cross-stage stage | PASS | "YOU MUST include this coda unconditionally"; no-structures default path |
| C-21 Inventory flag alignment | PASS | Inventory table column headers [shadow-call] [taken-for-granted] [fog-system] [relay-chain] trace to non-standard obligation categories |
| C-22 C-19/C-21 vocabulary unification | PASS | VOCABULARY RULE: "Column header `[shadow-call]` = OBL-1 Obligation Term 'shadow-call'" × four; "YOU MUST NOT substitute a canonical term (e.g., `[forgotten-call]`, `[unknown-system]`) for any of the non-standard Obligation Terms above — canonical substitution breaks vocabulary identity within this trace, and a reviewer comparing the obligation table to the inventory table will see the mismatch as a structural discrepancy" |
| C-23 Unnumbered coda | PASS | CROSS-STAGE CODA unnumbered, "appended after Stage 3 — the last numbered stage" — terminal position |
| **C-24 Four-obligation table schema** | **PASS** | 4-row obligation table with non-standard Obligation Term cells (shadow-call, taken-for-granted, fog-system, relay-chain); all four rows present; appears before Stage 1 gate; structural completeness in non-standard vocabulary |
| **C-25 Schema-aligned C-22 enforcement** | **PASS** | Inventory table column headers [shadow-call] [taken-for-granted] [fog-system] [relay-chain] ARE the exact tokens from C-24 obligation table Obligation Term cells; canonical substitution prohibition makes any canonical-for-non-standard swap visible as a structural mismatch in the table schema AND explicitly prohibited declaratively — dual coverage |

**Score: 177 / 177**

**Notable:** V-05 achieves the highest-confidence C-22/C-25 enforcement for non-standard vocabulary: schema alignment (structural — column header/row-term mismatch is a table comparison) + canonical substitution prohibition (declarative — explicit YOU MUST NOT). This dual coverage closes both the table surface (C-25 structural detection) and the prose/annotation surface (model could still write canonical terms outside the table). The non-standard term ecosystem round-trips cleanly: obligation table → inventory column headers → per-call flag references in call block → gap type taxonomy — all in non-standard vocabulary.

---

## Ranking

| Rank | Variation | Score | C-24 | C-25 |
|------|-----------|-------|------|------|
| 1 (tied) | V-01 Role Sequence + Obligation Table | **177/177** | 4-row table before Stage 1 | Schema + VOCABULARY RULE |
| 1 (tied) | V-02 Full-Table Schema-Only | **177/177** | 4-row table before Section 1 | Schema-only (no VOCABULARY RULE) |
| 1 (tied) | V-04 Phase Architecture + Terminal Coda | **177/177** | 4-row table in Phase 1 | Schema + VOCABULARY RULE |
| 1 (tied) | V-05 Non-Standard + Prohibition | **177/177** | 4-row non-standard table | Non-standard schema + prohibition |
| 5 | V-03 Mixed-Format Probe (Q2) | **172/177** | PASS — 4-row obligation table | FAIL — no column headers in pipe-delimited inventory |

---

## Open Question Resolutions

**Q1 — C-23 terminal-position constraint (V-04 definitive):**
The terminal-position constraint IS real. The unnumbered coda satisfies C-23 only when it is appended after the last numbered element of the outer frame. A coda placed before any remaining numbered element fails C-23 even when unnumbered. The explicit language "appended after Phase 3 — the last numbered element of the outer frame" and "It does not appear between any two numbered phases" is the correct pattern. This constraint should be formalized: C-23 should explicitly state that the coda must be the terminal element of the outer frame.

**Q2 — C-25 column header requirement (V-03 definitive):**
C-25 requires actual Markdown table column header cells. Inline flag tokens in pipe-delimited inventory entries satisfy C-22 (via VOCABULARY RULE) but not C-25. The defining mechanism of C-25 is header/row-term comparison, which requires column header cells as the comparison surface. Pipe-delimited format has no column headers — the schema alignment is not mechanically verifiable by table comparison.

---

## Excellence Signals

**From V-02 (schema-only C-25):**
- **VOCABULARY RULE is unnecessary when C-24 + C-25 schema alignment is present.** When the obligation table and inventory table share the same token in the row term cell and the column header cell, the structural mechanism subsumes the declarative one. A mismatch is visible as a structural discrepancy without any prose rule. Dropping the VOCABULARY RULE block tests and confirms this: schema-only enforcement achieves full C-25 score.

**From V-05 (non-standard + dual coverage):**
- **Canonical substitution prohibition is the correct declarative complement to C-25 for non-standard terms.** C-25 detects substitution at the table schema surface (column header/row-term mismatch). The prohibition blocks substitution at the prose/annotation surface (model writing canonical terms outside the table). Together they constitute dual-surface coverage. The prohibition must explicitly name the canonical terms that are forbidden — "YOU MUST NOT substitute `[forgotten-call]`" is stronger than a generic "use non-standard terms" instruction.

**From V-04 (Q1 resolution):**
- **Explicit terminal-position language is required to definitively pass C-23 in non-Stage-sequence frames.** The formula: `*(no [element] number — appended after [last element], the last numbered [element])*` + prose sentence "It does not appear between any two numbered [elements]; it does not displace or renumber any existing element" — this dual statement (coda header + supporting sentence) makes the terminal constraint unambiguous for any outer frame style (phases, stages, sections).

---

```json
{"top_score": 177, "all_essential_pass": true, "new_patterns": ["schema-only C-25 enforcement is sufficient — dropping VOCABULARY RULE and relying solely on obligation-table-row-term-to-inventory-column-header schema identity achieves full C-25 score; the structural mechanism subsumes the declarative one", "canonical substitution prohibition + schema alignment = dual-surface C-22/C-25 coverage for non-standard terms — schema detects substitution at table surface, prohibition blocks it at prose/annotation surface; explicit YOU MUST NOT naming specific canonical forbidden terms is required", "explicit terminal-position language in coda header + supporting prose sentence definitively satisfies C-23 in any outer frame — formula: no-number annotation + 'appended after [last element] — the last numbered element' + 'does not appear between any two numbered [elements]'"]}
```
