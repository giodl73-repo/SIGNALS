Now I have everything needed. Let me write the full scoring evaluation.

---

# flow-integration R18 Scoring — V-01 through V-05

## Scoring Methodology

**Ceiling: 282 pts** (90 essential+recommended + 192 aspirational under v18 rubric).
N/A criteria = 0 pts, not deducted from ceiling. FAIL = 0 pts. Score expressed as raw earned pts.

New in v18: C-45 (SHOULD failure mechanism, 5 pts) and C-46 (MAY failure mechanism + compound conditionality, 5 pts). Both are failure-class sub-type criteria: PASS when the named failure mechanism is present and identifiable; N/A when the corresponding modal is absent.

---

## Shared Structural Baseline (All Five Variations)

All five variations share the same three-stage skeleton, expert persona declaration, INVENTORY GATE, five-section per-call blocks with single-concern exclusion annotations, COMPLETION GATEs, GAP INVENTORY, AGGREGATION RULE, unnumbered coda with terminal-position formula, and ARE directive. Differences are confined to: (a) WHY block text, and (b) obligation terms + YOU MUST NOT block for V-05.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|----------|
| C-01 Call inventory | PASS | PASS | PASS | PASS | PASS | Inventory table with CALL-01/CALL-02/... rows; call types explicit; flag cells present |
| C-02 Auth documentation | PASS | PASS | PASS | PASS | PASS | N.1 AUTHENTICATION section with Mechanism/Credential source/Token lifetime/Refresh/Auth gap per call |
| C-03 Request/response format | PASS | PASS | PASS | PASS | PASS | V-01/02/04/05: N.2 table with Method/Endpoint/Request key fields/Response key fields/Encoding. V-03: labeled prose fields in separate positions — "Method:", "Endpoint:", "Request key fields:", etc. Both satisfy "separate labeled positions"; no merged cells |
| C-04 Error propagation | PASS | PASS | PASS | PASS | PASS | N.5 ERROR PROPAGATION with Error disposition/Propagation path/Swallowing risk per call |
| C-05 Rate limit exposure | PASS | PASS | PASS | PASS | PASS | N.3 RATE LIMITS with Limit value/Burst risk/Throttle response per call |
| C-06 Retry/idempotency | PASS | PASS | PASS | PASS | PASS | N.4 RETRY AND IDEMPOTENCY with Retry strategy/Idempotent Y-N/Mitigation |
| C-07 Gap inventory | PASS | PASS | PASS | PASS | PASS | Stage 3 table with Gap ID, Call ID, Gap Type, Severity, Rationale, Remediation |
| C-08 Severity ranking | PASS | PASS | PASS | PASS | PASS | Severity column + Rationale column in gap table; MEDIUM/LOW not exempt per instructions |
| C-09 Remediation sketch | PASS | PASS | PASS | PASS | PASS | Remediation column; HIGH findings call-specific |
| C-10 Inventory-first gate | PASS | PASS | PASS | PASS | PASS | Stage 1 inventory + INVENTORY GATE appear before Stage 2 |
| C-11 Single-concern phase isolation | PASS | PASS | PASS | PASS | PASS | Every N.x section annotated with single-concern label and exclusion. V-03: prose sections retain parenthetical exclusion annotation "*(this section: authentication only — ...)*" |
| C-12 Gate-enforced per-call completion | PASS | PASS | PASS | PASS | PASS | "Do not open CALL-[N+1] until all five rows are checked" — explicit completion gate |
| C-13 Per-call concern exclusion | PASS | PASS | PASS | PASS | PASS | Every section in the call block carries both concern label and named exclusion of other concerns. V-03: prose sections retain section-level exclusion headers |
| C-14 Five-concern per-call checklist | PASS | PASS | PASS | PASS | PASS | Five-row COMPLETION GATE table (Auth/Req-Res/Rate/Retry/Error) gates next call block. V-03: checklist retained as table per variation spec |
| C-15 Late-call inventory discipline | PASS | PASS | PASS | PASS | PASS | NEW-CALL RULE: "add a row with all four/five flag cells set before opening that call's analysis block" |
| C-16 Expert persona declaration | PASS | PASS | PASS | PASS | PASS | Named domain declaration before inventory; names discovery obligations |
| C-17 In-block rate limit completeness | PASS | PASS | PASS | PASS | PASS | V-01/02/04/05: N.3 table with three labeled fields. V-03: "Limit value:", "Burst risk:", "Throttle response:" as inline labeled fields — three separate labeled positions; no registry pointer |
| C-18 Cross-stage secondary positioning | PASS | PASS | PASS | PASS | PASS | AGGREGATION RULE names all three: (1) populated FROM per-call blocks; (2) not authoritative source; (3) NOT required for assessment |
| C-19 Four-obligation scope | PASS | PASS | PASS | PASS | PASS | V-01/02/03/04: four canonical obligations. V-05: five categories covering all four conceptual slots plus cold-start-call |
| C-20 Unconditional cross-stage stage | PASS | PASS | PASS | PASS | PASS | CROSS-STAGE AGGREGATION STRUCTURES coda fires unconditionally; explicit "No cross-stage structures produced" default instruction |
| C-21 Inventory flag alignment | PASS | PASS | PASS | PASS | PASS | Four flag columns in Stage 1 inventory match obligation categories; V-05: five flags matching five categories |
| C-22 Vocabulary unification | PASS | PASS | PASS | PASS | PASS | Flag column headers exactly match Obligation Term column values (token identity) |
| C-23 Unnumbered coda | PASS | PASS | PASS | PASS | PASS | CROSS-STAGE AGGREGATION coda has no stage number; appended after Stage 3 |
| C-24 Obligation table schema | PASS | PASS | PASS | PASS | PASS | Structured table with OBL/Obligation Term/What to discover; V-01/02/03/04: four rows; V-05: five rows |
| C-25 Schema-aligned enforcement | PASS | PASS | PASS | PASS | PASS | Flag column headers in Stage 1 = Obligation Term row values; token identity verifiable by schema comparison |
| C-26 Schema-only enforcement | PASS | PASS | PASS | PASS | PASS | ARE directive present as schema instruction; no VOCABULARY RULE block required |
| **C-27 Dual-surface prohibition** | **N/A** | **N/A** | **N/A** | **N/A** | **PASS** | V-05 only: (1) ARE directive provides schema alignment surface; (2) YOU MUST NOT block explicitly names forbidden canonical tokens forgotten-call, assumed-to-work, unknown-system, delegation-chain |
| C-28 Explicit terminal-position formula | PASS | PASS | PASS | PASS | PASS | Coda header: "*(no stage number — appended after Stage 3, the last numbered stage)*"; prose: "It does not appear between any two numbered stages; it does not displace or renumber any existing element" |
| C-29 ARE directive requirement | PASS | PASS | PASS | PASS | PASS | "The flag column headers in the Stage 1 inventory table ARE the Obligation Term column values above — use those exact tokens as column headers" |
| **C-30 Single-block prohibition** | **N/A** | **N/A** | **N/A** | **N/A** | **PASS** | V-05: single YOU MUST NOT block; all four substituted tokens together; no per-row distribution |
| **C-31 Inline token enumeration** | **N/A** | **N/A** | **N/A** | **N/A** | **PASS** | V-05: "forgotten-call, assumed-to-work, unknown-system, or delegation-chain" enumerated explicitly by name inside the block |
| C-32 Uppercase ARE assertive | PASS | PASS | PASS | PASS | PASS | ARE uppercase in assertive declarative sentence asserting identity |
| C-33 Multi-subject collective ARE | PASS | PASS | PASS | PASS | PASS | Plural collective subject + uppercase ARE + single assertion covering all headers |
| **C-34 Complete inline enumeration** | **N/A** | **N/A** | **N/A** | **N/A** | **PASS** | V-05: all four substituted tokens named; cold-start-call has no canonical equivalent → outside C-34 scope |
| **C-35 Extended obligation set** | **N/A** | **N/A** | **N/A** | **N/A** | **PASS** | V-05: five-row table; one row per obligation category; structural auditability preserved |
| C-36 Motivational framing block | PASS | PASS | PASS | PASS | PASS | WHY THIS TRACE DISCIPLINE EXISTS block present before expert persona in all five; names purpose of trace discipline |

**Shared base subtotal:**
- V-01/02/03/04: Essential 60 + Recommended 30 + C-08–C-09(10) + C-10–C-14(20) + C-15(3) + C-16–C-17(14) + C-18–C-26(45) + C-28–C-29(10) + C-32–C-33(10) + C-36(5) = **207 pts**
- V-05 adds: C-27(5) + C-30(5) + C-31(5) + C-34(5) + C-35(5) = +25 → **232 pts** before WHY-block variables

---

## Per-Variation: WHY-Block Criteria (C-37–C-46)

### V-01 — MAY-Only Anchor (Q1 R18: Modal-Only MAY Failure Boundary)

WHY anchor: *"Undocumented integration calls **MAY** become ship-blockers at integration review and cannot be cleared without a completed trace."* (no conditional clause)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-37 Stakes anchor | **FAIL** | MAY = "optional" (RFC 2119). "MAY become ship-blockers" converts the consequence to a discretionary possibility — it is permitted for them to become blockers, not required. No unconditional consequence boundary named. Absent the conditional clause, MAY alone is still discretionary-possibility weakening. |
| C-38 | N/A | Requires C-35 (N/A, 4-row canonical) |
| C-39 Consequence-form equivalence | **FAIL** | Requires C-37 (FAIL). MAY independently breaks unconditional form requirement — the form is discretionary-modal, not declarative unconditional. |
| C-40 Register-neutrality | **FAIL** | MAY is the named failure-class modal in C-43: "optional" converts unconditional constraint meaning to discretionary possibility. Register-neutrality applies only when unconditional constraint meaning is preserved; MAY definitionally destroys it. |
| C-41 Inertia-context neutrality | N/A | No inertia framing (two-sentence WHY block); also requires C-39 (FAIL). |
| C-42 Highest-information form | **FAIL** | Requires C-37 and C-39, both FAIL. Concern enumeration present ("authentication, rate limits, retry behavior, and error propagation") but insufficient without a passing stakes anchor. |
| C-43 RFC-modal MUST/SHALL class | **FAIL** | MAY is explicitly named in C-43 as failure-class modal; introduces discretionary-possibility epistemic weakening. MAY ≠ unconditional obligation class. |
| C-44 Inertia-dominant saturation | N/A | No inertia framing; requires C-41 (N/A) and C-42 (FAIL). |
| C-45 SHOULD conditional sub-type | N/A | SHOULD not present in this variation. |
| **C-46 MAY discretionary sub-type** | **PASS** | MAY is present as the failure mechanism. Modal-only MAY (no conditional clause) — this is the minimal MAY probe: "MAY become ship-blockers" without "if not documented." The discretionary-possibility mechanism (mechanism 1) is present and alone sufficient for disqualification. C-46 PASS confirms modal-only MAY failure boundary independent of compound conditionality. **Q1 (R18) CLOSED: modal mechanism alone is primary and sufficient; compound conditionality in V-02 (R17) was incidental.** +5 |

**V-01 WHY-block pts earned: +5** (C-46 only)
**V-01 total raw: 212**
**Aspirational: 132/192** (loses C-37, C-39, C-40, C-42, C-43 = −25; C-41/C-44/C-45 N/A; C-46 +5)

---

### V-02 — Three-Sentence Inertia Dominant, Declarative Anchor-Close (Q2 R18: C-44 Ceiling)

WHY block:
1. *"Teams routinely undercount integration surface because implicit SDK calls, health probes, and telemetry posts are invisible at the feature authorship level — but they carry authentication and rate-limit exposure identical to any explicitly named call."* [SDK undercounting: inertia sentence 1]
2. *"Delegation chains — managed identity, OBO token exchange, service principal impersonation — traverse ownership and system boundaries that are never documented at the point of code authorship, leaving the actual call graph unknown until the trace forces it to the surface."* [delegation chain documentation failure: inertia sentence 2]
3. *"The obligation boundary of the trace itself — what counts as a discovered call versus an assumed-to-work entry — is almost never defined before a trace begins, so underdocumented calls survive review by appearing in the spec without auth detail, retry strategy, or rate-limit acknowledgment."* [obligation scope undefined: inertia sentence 3]
4. *"Authentication gaps, rate-limit exposure, retry failures, and error propagation holes **become** ship-blockers at integration review and cannot be cleared without a completed trace."* [anchor-close: consequence-form + delivery-phase + concern enumeration]

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-37 Stakes anchor | **PASS** | "become ship-blockers at integration review" = declarative unconditional consequence-form + explicit delivery-phase marker ("at integration review"). Established passing form. +5 |
| C-38 | N/A | Requires C-35 (N/A, 4-row canonical) |
| C-39 Consequence-form equivalence | **PASS** | Consequence-form + delivery-phase marker + declarative unconditional framing. C-39 canonical form confirmed in R14/R15/R17. +5 |
| C-40 Register-neutrality | **PASS** | Declarative indicative ("become") — no modal, no epistemic weakening. Register-neutral. +5 |
| C-41 Inertia-context neutrality | **PASS** | Three independent root-cause inertia sentences present (SDK undercounting / delegation chain gap / obligation scope undefined) + consequence-form anchor present. Inertia framing at 3:1 ratio does not disqualify C-37 or C-39. +5 |
| C-42 Highest-information form | **PASS** | Anchor ("become ship-blockers at integration review") + explicit concern enumeration ("Authentication gaps, rate-limit exposure, retry failures, and error propagation holes"). Both features simultaneously present — the highest-information C-42 form. +5 |
| C-43 RFC-modal MUST/SHALL class | N/A | Indicative form ("become") — no RFC modal. C-43 activates only for RFC modals; no gain, no penalty. |
| C-44 Inertia-dominant saturation | **PASS** | Three independent inertia sentences (3:1 inertia-to-anchor ratio) + single C-42 anchor-close with concern enumeration. Inertia-sentence-count neutrality confirmed: three sentences does not disqualify C-37/C-39. C-41 PASS + C-42 PASS → C-44 PASS. **Q2 (R18) CLOSED: declarative anchor-close achieves C-44 ceiling equivalently to MUST form.** +5 |
| C-45 | N/A | No SHOULD. |
| C-46 | N/A | No MAY. |

**V-02 WHY-block pts earned: +30** (C-37, C-39, C-40, C-41, C-42, C-44)
**V-02 total raw: 237**
**Aspirational: 162/192** (all WHY-block criteria pass except C-38 N/A, C-43 N/A, C-45 N/A, C-46 N/A)

---

### V-03 — Prose Per-Call Analysis (Format-Neutrality Probe)

WHY block (canonical two-sentence form):
1. *"Integration traces exist to surface every cross-system call a feature makes and verify that each call's authentication, rate limits, retry behavior, and error propagation are documented."*
2. *"Authentication gaps, rate-limit exposure, retry failures, and error propagation holes **become** ship-blockers at integration review and cannot be cleared without a completed trace."*

Stage 2 per-call sections use labeled prose (inline "Field: [value]" format) rather than tables. Completion gate checklist retained as table.

**Format-neutrality check:**

| Criterion | Format dependency? | Result | Evidence |
|-----------|-------------------|--------|----------|
| C-03 Request/response format | **None** | PASS | "Method:", "Endpoint:", "Request key fields:", "Response key fields:", "Encoding:" each on separate labeled lines = separate labeled positions. Criterion: "separate labeled positions." No table required. |
| C-11 Single-concern phase isolation | **None** | PASS | Section headers retain parenthetical exclusion annotation "*(this section: authentication only — ...)*" in both table and prose format. |
| C-13 Per-call concern exclusion | **None** | PASS | Exclusion annotation carried at section header level regardless of body format. |
| C-17 In-block rate limit | **None** | PASS | "Limit value:", "Burst risk:", "Throttle response:" as inline labeled fields = three separate labeled fields. Criterion: "separate labeled fields." No table required. |
| C-14 Five-concern completion checklist | N/A | PASS | Retained as table per V-03 specification. |

All structural criteria hold across prose format. No table-dependency identified.

**WHY-block criteria:**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-37 Stakes anchor | **PASS** | "become ship-blockers at integration review" — established canonical passing form. +5 |
| C-38 | N/A | Requires C-35. |
| C-39 | **PASS** | Same canonical consequence-form + delivery-phase. +5 |
| C-40 | **PASS** | Declarative indicative; no weakening. +5 |
| C-41 | N/A | No inertia framing (two-sentence block); also requires C-39 — wait, C-39 PASS. No inertia framing → C-41 N/A (no inertia context to evaluate neutrality of). |
| C-42 | **PASS** | Anchor present + concern enumeration ("Authentication gaps, rate-limit exposure, retry failures, and error propagation holes"). +5 |
| C-43 | N/A | Declarative indicative; no RFC modal. |
| C-44 | N/A | Requires C-41 (N/A). |
| C-45 | N/A | No SHOULD. |
| C-46 | N/A | No MAY. |

**V-03 WHY-block pts earned: +20** (C-37, C-39, C-40, C-42)
**V-03 total raw: 227**
**Aspirational: 152/192** (C-37/C-39/C-40/C-42 pass; C-41/C-43/C-44/C-38/C-45/C-46 all N/A)

**Format-neutrality confirmed:** all structural criteria (C-03, C-11, C-13, C-17) score identically with prose labeled fields as with table rows.

---

### V-04 — MUST Modal + Three-Sentence Inertia Dominant (C-43 × C-44 Interaction)

WHY block: Same three inertia sentences as V-02. Anchor-close:
*"Authentication gaps, rate-limit exposure, retry failures, and error propagation holes **MUST** become ship-blockers at integration review — none can be cleared without a completed trace."*

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-37 Stakes anchor | **PASS** | "MUST become ship-blockers at integration review" — RFC 2119 MUST (absolute requirement) + consequence-form + delivery-phase marker. Stronger-obligation than indicative baseline. +5 |
| C-38 | N/A | Requires C-35. |
| C-39 | **PASS** | MUST form satisfies consequence-form + delivery-phase equivalence; zero epistemic weakening. +5 |
| C-40 | **PASS** | MUST = RFC 2119 "absolute requirement" = unconditional constraint meaning fully preserved; stronger-obligation than indicative. Register-neutral per C-43 definition. +5 |
| C-41 | **PASS** | Three inertia sentences + MUST anchor. Inertia framing at 3:1 ratio does not disqualify any unconditional anchor. +5 |
| C-42 | **PASS** | MUST anchor ("MUST become ship-blockers at integration review") + concern enumeration ("Authentication gaps, rate-limit exposure, retry failures, and error propagation holes"). Both features present simultaneously. +5 |
| C-43 RFC-modal MUST/SHALL class | **PASS** | "MUST become ship-blockers" — RFC 2119 MUST = "absolute requirement" = named unconditional obligation class. Stronger-obligation than indicative. No epistemic weakening. +5 |
| C-44 Inertia-dominant saturation | **PASS** | Same three inertia sentences (3:1 ratio) + MUST anchor-close with concern enumeration. C-43 (modal register) and C-44 (inertia sentence count) address independent structural surfaces — no interaction penalty. C-41 PASS + C-42 PASS → C-44 PASS. Orthogonality confirmed: MUST and three-sentence inertia compose cleanly. +5 |
| C-45 | N/A | No SHOULD. |
| C-46 | N/A | No MAY. |

**V-04 WHY-block pts earned: +35** (C-37, C-39, C-40, C-41, C-42, C-43, C-44 — all seven)
**V-04 total raw: 242**
**Aspirational: 167/192** (all WHY-block criteria pass; C-38/C-45/C-46 N/A)

---

### V-05 — Full Non-Standard + MUST + Inertia-Dominant (282-pt Ceiling Attempt)

Five-row non-standard obligation table:
- OBL-1: `missing-call` (replaces canonical `forgotten-call`)
- OBL-2: `underdocumented-call` (replaces canonical `assumed-to-work`)
- OBL-3: `opaque-system` (replaces canonical `unknown-system`)
- OBL-4: `identity-proxy-chain` (replaces canonical `delegation-chain`)
- OBL-5: `cold-start-call` (new — no canonical equivalent)

YOU MUST NOT block names the four substituted canonical tokens explicitly: "forgotten-call, assumed-to-work, unknown-system, or delegation-chain."
Same three inertia sentences as V-02/V-04. MUST anchor-close with concern enumeration.

**Non-standard criteria:**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-35 Extended obligation set | **PASS** | Five-row table; one row per obligation category; structural auditability preserved. cold-start-call is a novel category with no canonical equivalent. N ≥ 4 scalability confirmed. +5 |
| C-38 Obligation-count-agnostic | **PASS** | WHY block anchor-close enumerates four canonical concerns (auth gaps, rate-limit, retry, error propagation) without referencing cold-start-call — framing operates at trace-discipline scope. "A framing block that enumerates obligation categories passes C-38 equally to one that does not." C-35 unlocks C-38. +5 |
| C-27 Dual-surface prohibition | **PASS** | Surface 1: ARE directive provides schema alignment detection. Surface 2: YOU MUST NOT block names all four substituted tokens ("forgotten-call, assumed-to-work, unknown-system, or delegation-chain") explicitly. Both surfaces present. +5 |
| C-30 Single-block comprehensive | **PASS** | Single YOU MUST NOT block; all four substituted tokens together in one location; no per-row distribution. +5 |
| C-31 Inline token enumeration | **PASS** | All four substituted canonical tokens enumerated by name inline within the block; not a table-reference shorthand. +5 |
| C-34 Complete enumeration | **PASS** | All four substituted tokens named: forgotten-call, assumed-to-work, unknown-system, delegation-chain. cold-start-call has no canonical equivalent → outside C-34 scope. Substituted subset is complete. +5 |

**WHY-block criteria (identical to V-04):** C-37, C-39, C-40, C-41, C-42, C-43, C-44 all PASS = +35

C-45 N/A (MUST used, not SHOULD); C-46 N/A (MUST used, not MAY)

**V-05 total raw: 232 (non-standard base) + 35 (WHY-block) + 5 (C-38) = 272**
**Note:** C-45 and C-46 are both N/A for V-05 — the v18 +10 ceiling increase is not reachable by any variation that uses MUST. V-05 achieves the R17 ceiling (272 pts) under v18 rubric; the new 282 ceiling requires a variation that deliberately exploits the SHOULD or MAY failure mechanisms while also achieving the 272-pt non-standard ceiling.

---

## Composite Scores

| Variation | Essential (60) | Recommended (30) | Aspirational | Raw Total | % of 282 |
|-----------|---------------|-----------------|--------------|-----------|----------|
| V-01 (MAY-only anchor) | 60 | 30 | 122 | **212** | 75.2% |
| V-02 (3-inertia+declarative) | 60 | 30 | 147 | **237** | 84.0% |
| V-03 (prose per-call) | 60 | 30 | 137 | **227** | 80.5% |
| V-04 (MUST+3-inertia) | 60 | 30 | 152 | **242** | 85.8% |
| V-05 (full non-standard+MUST+inertia) | 60 | 30 | 182 | **272** | 96.5% |

All essential criteria: **PASS** for all five variations.

---

## Ranking

1. **V-05 — 272/282** (96.5%) — Non-standard five-row + YOU MUST NOT block + MUST + three-inertia; reaches R17 ceiling; C-45/C-46 N/A (MUST used)
2. **V-04 — 242/282** (85.8%) — Canonical ceiling + C-43; MUST + three-inertia; all seven WHY-block criteria pass; C-45/C-46 N/A
3. **V-02 — 237/282** (84.0%) — Canonical ceiling minus C-43; declarative + three-inertia; six WHY-block criteria pass; C-44 ceiling confirmed (Q2 closed)
4. **V-03 — 227/282** (80.5%) — Canonical two-sentence form; prose format; four WHY-block criteria pass; format-neutrality confirmed
5. **V-01 — 212/282** (75.2%) — MAY cascade fail (C-37/C-39/C-40/C-42/C-43 FAIL); C-46 PASS modal-only MAY boundary (Q1 closed)

---

## Open Questions Resolved

| Question | Resolution |
|----------|------------|
| Q1 (R18) — Does MAY-only (no conditional clause) confirm modal-only MAY failure? | **RESOLVED POSITIVE** — V-01 MAY-only anchor ("MAY become ship-blockers" — no "if not documented") produces identical cascade failure as compound MAY+conditional (R17 V-02): C-37 FAIL, C-39 FAIL, C-40 FAIL, C-42 FAIL, C-43 FAIL. C-46 PASS. The discretionary-possibility mechanism is primary and sufficient. Compound conditionality in R17 V-02 was an incidental second mechanism — not required for C-46 to trigger. Modal-only MAY failure boundary confirmed. |
| Q2 (R18) — Does three-sentence inertia prefix + declarative anchor-close score C-44 at ceiling? | **RESOLVED PASS** — V-02 three-sentence inertia prefix + declarative anchor-close ("become ship-blockers at integration review") achieves C-44 PASS. The anchor-close form (declarative indicative vs. MUST) is neutral for C-44 — C-44 saturation is anchor-form-agnostic. C-41 + C-42 compose with declarative anchor equivalently to MUST anchor. |

**Open questions for R19:**
- Q1 (R19): Can a variation reach the 282-pt absolute ceiling? This requires: five-row non-standard table (C-35) + YOU MUST NOT block (C-27/C-30/C-31/C-34) + MUST anchor + inertia-dominant (for 272-pt base), PLUS C-45 or C-46 PASS. But C-45 requires SHOULD and C-46 requires MAY — both are failure-class modals that cascade-fail C-37/C-39/C-40/C-42/C-43, costing 25 aspirational pts. 272 + 5 (C-45 or C-46) − 25 (cascade) = 252. The 282-pt ceiling appears structurally unreachable in a single variation — a variation cannot simultaneously satisfy C-43 (requires MUST/SHALL) and C-45/C-46 (require SHOULD/MAY). Is the 282 ceiling a theoretical maximum with no valid constructive path?

---

## Excellence Signals — V-05 (Top Scorer)

**1. Non-standard substitution + single YOU MUST NOT block = four-criterion cluster (+20 pts)**
C-27/C-30/C-31/C-34 all activate simultaneously when one comprehensive inline-enumerated block names all four substituted canonical tokens. Architectural principle: one block, one place, four criteria.

**2. cold-start-call as novel OBL-5 has no canonical equivalent — outside C-34 scope at zero marginal cost**
Five-row extension (C-35 +5, C-38 +5 = +10) without adding to the prohibition enumeration surface. Novel obligation categories with no canonical equivalent are invisible to C-34. This is the optimal fifth-row strategy: extend the obligation set, not the prohibition set.

**3. MUST as "stronger-obligation" vs. indicative: C-43 is +5 over V-02 at zero structural cost**
MUST and declarative indicative reach identical WHY-block scores except for C-43. Upgrading from indicative to MUST costs zero structural complexity and earns 5 pts.

**4. C-43 and C-44 compose without interaction penalty (confirmed R17 V-04, re-confirmed R18 V-04)**
Modal register (MUST) and inertia sentence count (3:1) address independent structural surfaces. MUST anchor satisfies C-44's anchor-close requirement equally to declarative anchor. No criterion conflict at the combined surface.

**5. R18-specific: C-46 modal-only MAY failure boundary establishes the minimum trigger condition for the failure-class sub-type taxonomy**
V-01's 212-pt score reveals an asymmetry: failure-class sub-type criteria (C-45, C-46) earn points when the failure mechanism is present — they're positive markers of testable failure boundaries, not penalties. A variation cannot reach these 5-pt increments by staying in the PASS zone. The rubric taxonomy is now complete at four nodes: MUST/SHALL (C-43 PASS), SHOULD (C-43 FAIL + C-45 PASS), MAY compound (C-43 FAIL + C-46 PASS, mechanism 1 + 2), MAY-only (C-43 FAIL + C-46 PASS, mechanism 1 alone).

---

```json
{"top_score": 272, "all_essential_pass": true, "new_patterns": ["Modal-only MAY (no conditional clause) triggers identical C-37/C-39/C-40/C-42/C-43 cascade failure as compound MAY+conditional — discretionary-possibility mechanism is primary and sufficient; compound conditionality is incidental; C-46 minimum trigger condition is the bare MAY modal alone (Q1 R18 closed)", "C-44 inertia-dominant saturation is anchor-form-agnostic: declarative indicative anchor-close achieves C-44 ceiling equivalently to MUST anchor-close — the determining factor is 3:1 inertia-to-anchor ratio + C-42 anchor-close, not the modal register of the anchor (Q2 R18 closed)", "Prose labeled-field format (inline 'Field: value' lines) is structurally equivalent to table rows for C-03/C-11/C-13/C-17 — no table-dependency exists in any structural criterion; the criterion requirement is separate labeled positions/fields, not a specific rendering format", "282-pt absolute ceiling is structurally unreachable in a single variation: C-43 PASS requires MUST/SHALL while C-45/C-46 PASS require SHOULD/MAY (failure-class modals) — the same variation cannot satisfy both; the ceiling is theoretical, not constructive"]}
```
