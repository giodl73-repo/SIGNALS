# flow-integration R16 Scoring — v16 Rubric (262 pt ceiling)

## Scoring Method

- **V-01–V-04** (canonical four-row): C-27/C-30/C-31/C-34/C-35/C-38 excluded (N/A — no substitution or extension). Applicable ceiling: **232 pts**.
- **V-05** (non-standard five-row): All criteria apply. Applicable ceiling: **262 pts**.
- N/A criteria excluded from both numerator and denominator.

---

## V-01 — C-42 Reference Form: Formal Declarative + Concern Enumeration + Stakes Anchor

**WHY block**: *"Integration traces exist to surface every cross-system call a feature makes and verify that each call's authentication, rate limits, retry behavior, and error propagation are fully documented — undocumented integration calls become ship-blockers at integration review and cannot be cleared without a completed trace."*

| Criterion | Pts | Result | Evidence |
|-----------|-----|--------|----------|
| C-01 | 15 | PASS | Call inventory table with Call ID, Target, Type, Confidence, four flag columns |
| C-02 | 15 | PASS | [N.1] AUTHENTICATION section with five labeled fields per call |
| C-03 | 15 | PASS | [N.2] REQUEST AND RESPONSE FORMAT with Method, Endpoint, key fields |
| C-04 | 15 | PASS | [N.5] ERROR PROPAGATION with disposition + propagation path + swallow risk |
| C-05 | 10 | PASS | [N.3] RATE LIMITS per call (limit value, burst risk, throttle response) |
| C-06 | 10 | PASS | [N.4] RETRY AND IDEMPOTENCY per call with strategy + idempotency flag |
| C-07 | 10 | PASS | STAGE 3 gap inventory with Call ID refs, gap-type labels, severity column |
| C-08 | 5 | PASS | Severity label + one-line rationale required; MEDIUM/LOW not exempt |
| C-09 | 5 | PASS | HIGH findings require call-specific remediation sketch (Remediation column) |
| C-10 | 4 | PASS | INVENTORY GATE: "Stage 2 does not open until the table is complete" |
| C-11 | 4 | PASS | Each stage labeled one concern; five [N.x] sections each carry single-concern annotation |
| C-12 | 4 | PASS | CALL-[N] COMPLETION GATE: "Do not open CALL-[N+1] until all five rows are checked" |
| C-13 | 4 | PASS | Every [N.x] section carries "*(this section: X only — other concerns each have their own sections)*" |
| C-14 | 4 | PASS | Five-item checklist in every call block (Auth/Req/Rate/Retry/Error); gates next call |
| C-15 | 3 | PASS | NEW-CALL RULE: "add a row with all four flag cells set before opening that call's analysis block" |
| C-16 | 7 | PASS | Expert persona: domain + four discovery obligations before inventory gate |
| C-17 | 7 | PASS | [N.3] RATE LIMITS: limit value, burst risk, throttle response as separate labeled fields |
| C-18 | 5 | PASS | AGGREGATION RULE: three properties named — populated FROM, NOT authoritative, NOT required; default path present |
| C-19 | 5 | PASS | Four obligations: forgotten-call, assumed-to-work, unknown-system, delegation-chain — all four categories covered |
| C-20 | 5 | PASS | CROSS-STAGE coda fires unconditionally; explicit "no structures" default instruction present |
| C-21 | 5 | PASS | Inventory flag columns [forgotten-call] [assumed-to-work] [unknown-system] [delegation-chain] — one per obligation |
| C-22 | 5 | PASS | Flag headers are identical tokens to Obligation Term column values in obligation table |
| C-23 | 5 | PASS | Coda is unnumbered; header: "*(no stage number — appended after Stage 3, the last numbered stage)*" |
| C-24 | 5 | PASS | Obligation table: four rows, one per obligation category; structural auditability preserved |
| C-25 | 5 | PASS | ARE directive + flag headers match Obligation Term column values by token identity; mismatch detectable by table comparison |
| C-26 | 5 | PASS | No VOCABULARY RULE block; ARE instruction alone enforces schema alignment |
| **C-27** | 5 | **N/A** | Canonical terms used; no substitution |
| C-28 | 5 | PASS | Coda header: "*(no stage number — appended after Stage 3, the last numbered stage)*"; prose: "It does not appear between any two numbered stages; it does not displace or renumber any existing element" — both surfaces |
| C-29 | 5 | PASS | ARE directive present: "the flag column headers in the Stage 1 inventory table ARE the Obligation Term column values above" |
| **C-30** | 5 | **N/A** | Requires C-27; canonical terms |
| **C-31** | 5 | **N/A** | Requires C-30; canonical terms |
| C-32 | 5 | PASS | Uppercase ARE in assertive declarative sentence |
| C-33 | 5 | PASS | Plural collective subject: "The flag column headers in the Stage 1 inventory table ARE..." |
| **C-34** | 5 | **N/A** | Requires C-31; canonical terms |
| **C-35** | 5 | **N/A** | Four-row canonical table; five-row extension not present |
| C-36 | 5 | PASS | WHY THIS TRACE DISCIPLINE EXISTS block before persona declaration; names purpose |
| C-37 | 5 | PASS | Consequence-form delivery-phase anchor: "become ship-blockers at integration review" — declarative, unconditional |
| **C-38** | 5 | **N/A** | Requires C-35 |
| C-39 | 5 | PASS | Consequence-form + explicit delivery-phase marker ("at integration review") + declarative unconditional — both C-39 conditions met |
| C-40 | 5 | PASS | Formal declarative — confirmed baseline register; unconditional constraint meaning preserved |
| C-41 | 5 | PASS | No inertia framing; WHY block is prospective/definitional — default pass |
| C-42 | 5 | PASS | Both required elements present: consequence-form anchor ("become ship-blockers at integration review") + explicit concern enumeration (authentication, rate limits, retry behavior, error propagation) |

**V-01 Score: 232 / 232** (N/A excluded: C-27/C-30/C-31/C-34/C-35/C-38)

---

## V-02 — C-40 Probe: RFC-Modal MUST/SHALL Register

**WHY block**: *"Every cross-system call a feature makes MUST be discovered and documented before integration review — authentication, rate limits, retry behavior, and error propagation MUST each be addressed per call. Undocumented integration calls SHALL become ship-blockers at integration review and cannot be cleared without a completed trace."*

| Criterion | Pts | Result | Evidence |
|-----------|-----|--------|----------|
| C-01–C-07 | 90 | PASS (all) | Identical structural template to V-01 |
| C-08–C-15 | 38 | PASS (all) | Identical gate/gate/checklist/persona structure to V-01 |
| C-16–C-17 | 14 | PASS (all) | Persona and in-block rate limits identical |
| C-18–C-26 | 45 | PASS (all) | Obligation table, ARE directive, schema enforcement identical to V-01 |
| C-27/C-30/C-31/C-34 | — | **N/A** | Canonical terms |
| C-28–C-29 | 10 | PASS | Terminal-position formula and ARE directive present; ARE uppercase assertive |
| C-32–C-33 | 10 | PASS | Uppercase ARE, plural collective subject |
| C-35/C-38 | — | **N/A** | Four-row canonical |
| C-36 | 5 | PASS | WHY block present, before persona, names purpose |
| C-37 | 5 | PASS | "SHALL become ship-blockers at integration review" — RFC SHALL is unconditional obligation (RFC 2119: "absolute requirement"); delivery-phase marker present; no conditional modal weakening |
| C-39 | 5 | PASS | Consequence-form ("SHALL become ship-blockers") + delivery-phase marker ("at integration review") + unconditional — SHA is stronger-obligation than indicative, not weaker |
| **C-40** | **5** | **PASS** | **RFC-modal MUST/SHALL register passes register-neutrality test — MUST/SHALL are unconditional modals; they introduce zero epistemic weakening (no "may/might/could") and carry stronger obligation semantics than indicative; unconditional constraint meaning fully preserved** |
| C-41 | 5 | PASS | No inertia framing; prospective obligation framing — default pass |
| C-42 | 5 | PASS | "authentication, rate limits, retry behavior, and error propagation MUST each be addressed per call" (enumeration) + "SHALL become ship-blockers at integration review" (anchor) — both C-42 elements present |

**V-02 Score: 232 / 232** (N/A excluded: C-27/C-30/C-31/C-34/C-35/C-38)

**C-40 verdict: PASS.** RFC-modal MUST/SHALL register is register-neutral. No degradation.

---

## V-03 — C-41 Saturation Probe: Three-Sentence Inertia Dominant

**WHY block**: Three sentences of inertia framing followed by the consequence anchor:
1. *"Feature integration scopes routinely undercount cross-system calls: specs name the API calls a developer consciously wrote while the SDK adds implicit token refreshes, health probes, and pre-warm sequences that nobody documented."* [inertia]
2. *"Delegation chains go unrecorded because the design documents describe the happy path, not the managed identity exchange that actually executes at runtime."* [inertia]
3. *"Prior traces failed to catch these calls not because teams were careless but because the obligation scope — what counts as a discoverable call — was never explicitly defined."* [inertia]
4. *"This trace defines that scope: document each call's authentication, rate limits, retry behavior, and error propagation — undocumented integration calls become ship-blockers at integration review and cannot be cleared without a completed trace."* [scope + anchor + enumeration]

| Criterion | Pts | Result | Evidence |
|-----------|-----|--------|----------|
| C-01–C-35 (applicable) | — | PASS (all) | Identical structural template; obligation table, ARE directive, gates, persona all unchanged |
| C-36 | 5 | PASS | WHY block present before persona; purpose named |
| C-37 | 5 | PASS | "become ship-blockers at integration review" — declarative, unconditional, delivery-phase marker present; stakes anchor in sentence 4 |
| C-39 | 5 | PASS | Consequence-form + delivery-phase marker + declarative unconditional satisfied in sentence 4; inertia framing in sentences 1–3 does not modify the C-39 pass conditions |
| C-40 | 5 | PASS | Formal declarative register in the anchor sentence — baseline register; unconditional meaning preserved |
| **C-41** | **5** | **PASS** | **Maximal inertia saturation test: 3 of 4 sentences are obligation-scope discovery-failure framing. Consequence-form anchor is structurally present in sentence 4 ("become ship-blockers at integration review"). C-41 criterion: inertia framing is background narrative regardless of volume — it cannot displace a present anchor. No structural mechanism by which sentence-count majority converts narrative framing into a structural override. The anchor in sentence 4 remains the operative stakes boundary.** |
| C-42 | 5 | PASS | Sentence 4 contains both: concern enumeration ("authentication, rate limits, retry behavior, and error propagation") + consequence-form anchor ("become ship-blockers at integration review") |

**V-03 Score: 232 / 232** (N/A excluded: C-27/C-30/C-31/C-34/C-35/C-38)

**C-41 verdict: PASS under maximal saturation.** 3-sentence inertia-dominant framing does not displace a present anchor.

---

## V-04 — Combined C-40 + C-41: Imperative Register + Inertia Framing

**WHY block**: *"Don't ship a feature whose cross-system calls haven't been traced — integrations that look clean in the spec routinely hide SDK-internal calls, unmapped delegation chains, and underdocumented authentication flows that nobody caught until review blocked them. Run this trace before integration review: document each call's authentication, rate limits, retry behavior, and error propagation — make sure undocumented calls become ship-blockers at integration review so they cannot be cleared without a completed trace."*

| Criterion | Pts | Result | Evidence |
|-----------|-----|--------|----------|
| C-01–C-35 (applicable) | — | PASS (all) | Identical structural template |
| C-36 | 5 | PASS | WHY block present before persona; purpose named |
| C-37 | 5 | PASS | "make sure undocumented calls become ship-blockers at integration review" — delivery-phase marker present; consequence-form meaning preserved in imperative phrasing; "become ship-blockers" is declarative-unconditional in the embedded clause |
| C-39 | 5 | PASS | Consequence-form + delivery-phase marker ("at integration review") present; "make sure X become Y at Z" carries unconditional constraint semantics — no epistemic modal weakening present |
| **C-40** | **5** | **PASS** | **Imperative register probe: "make sure undocumented calls become ship-blockers at integration review" — conversational/imperative surface register. The unconditional constraint meaning is preserved: no conditional modal ("might," "can," "could") present. C-40 register-neutrality: register is a surface property; the structural C-39 conditions (consequence-form + delivery-phase marker + unconditional meaning) are satisfied regardless of surface register.** |
| **C-41** | **5** | **PASS** | **Inertia sentence: "integrations that look clean in the spec routinely hide SDK-internal calls, unmapped delegation chains, and underdocumented authentication flows that nobody caught until review blocked them" — one sentence of discovery-failure framing in imperative context. Consequence-form anchor is present in the second sentence. C-41 holds: inertia framing is background narrative regardless of register; register does not activate a C-41 threshold that prose framing alone cannot trigger. No interaction effect detected between C-40 register axis and C-41 framing-context axis.** |
| C-42 | 5 | PASS | "document each call's authentication, rate limits, retry behavior, and error propagation" (enumeration) + "make sure undocumented calls become ship-blockers at integration review" (anchor) — both C-42 elements present in imperative form |

**V-04 Score: 232 / 232** (N/A excluded: C-27/C-30/C-31/C-34/C-35/C-38)

**C-40 + C-41 interaction verdict: NO INTERACTION EFFECT.** The axes are structurally orthogonal — register is a surface property; framing context is a content property. Neither criterion reaches into the other's structural dimension.

---

## V-05 — Full 262-pt Ceiling: Five-Row Non-Standard + C-42 WHY Form

**WHY block**: Same as V-01 — formal declarative, consequence-form anchor + concern enumeration.

**Obligation table**: five non-standard terms — expose-call / silent-entry / shadow-system / delegation-chain (canonical, kept) / burst-start (new, no canonical equivalent).

**YOU MUST NOT block**: *"YOU MUST NOT use forgotten-call, assumed-to-work, or unknown-system as column headers or obligation names in this trace."*

| Criterion | Pts | Result | Evidence |
|-----------|-----|--------|----------|
| C-01–C-04 | 60 | PASS | Standard structural template; call inventory, auth, format, error propagation all present |
| C-05–C-07 | 30 | PASS | Rate limits, retry, gap inventory all present |
| C-08–C-09 | 10 | PASS | Severity ranking and remediation sketch required |
| C-10–C-15 | 23 | PASS | Inventory-first gate, phase isolation, completion gate, concern exclusion, 5-item checklist, NEW-CALL RULE |
| C-16–C-17 | 14 | PASS | Expert persona with five-obligation declaration; in-block rate limits |
| C-18–C-20 | 15 | PASS | AGGREGATION RULE (three properties), unconditional coda with no-structures default |
| C-21 | 5 | PASS | Inventory flag columns: [expose-call] [silent-entry] [shadow-system] [delegation-chain] [burst-start] — five flags for five obligations |
| C-22 | 5 | PASS | Flag headers are identical tokens to Obligation Term column values in five-row table |
| C-23 | 5 | PASS | Unnumbered coda appended after Stage 3 |
| C-24 | 5 | PASS | Five-row obligation table — one row per obligation; structural auditability preserved |
| C-25 | 5 | PASS | ARE directive + five flag headers match five Obligation Term values by token identity |
| C-26 | 5 | PASS | ARE instruction achieves schema enforcement without VOCABULARY RULE block; YOU MUST NOT block serves C-27 (substitution prohibition), not schema enforcement — C-26 layer unaffected |
| **C-27** | **5** | **PASS** | **Dual-surface coverage: (1) schema surface — ARE directive makes column-header/term mismatch detectable by table comparison; (2) YOU MUST NOT block names the three substituted canonical tokens (forgotten-call, assumed-to-work, unknown-system) explicitly by name** |
| C-28 | 5 | PASS | Terminal-position formula both surfaces present |
| C-29 | 5 | PASS | Explicit ARE directive with uppercase ARE |
| **C-30** | **5** | **PASS** | **"YOU MUST NOT use forgotten-call, assumed-to-work, or unknown-system as column headers or obligation names in this trace" — single block enumerating all three substituted canonical tokens; no per-term inline distribution** |
| **C-31** | **5** | **PASS** | **Inline enumeration: forgotten-call, assumed-to-work, unknown-system all named explicitly inside the YOU MUST NOT block; no table-reference delegation ("see table above")** |
| C-32 | 5 | PASS | Uppercase ARE in assertive declarative sentence |
| C-33 | 5 | PASS | Plural collective subject: "The flag column headers in the Stage 1 inventory table ARE..." |
| **C-34** | **5** | **PASS** | **Three canonical tokens substituted: forgotten-call → expose-call, assumed-to-work → silent-entry, unknown-system → shadow-system. delegation-chain is canonical (kept). burst-start is new (no canonical equivalent). YOU MUST NOT block names all three substituted tokens. Complete substituted-subset enumeration.** |
| **C-35** | **5** | **PASS** | **Five-row obligation table; N ≥ 4 structural rule satisfied; one row per obligation category; each category's presence/absence detectable as a present/absent row** |
| C-36 | 5 | PASS | WHY block present before persona |
| C-37 | 5 | PASS | Consequence-form anchor: "become ship-blockers at integration review" — declarative, unconditional |
| **C-38** | **5** | **PASS** | **Five-row extended obligation set in play (C-35); WHY block uses canonical four-concern framing (authentication, rate limits, retry behavior, error propagation); does not enumerate extended obligation categories; framing evaluated at trace-discipline scope, not obligation enumeration scope — C-38 PASS as designed** |
| C-39 | 5 | PASS | Consequence-form + delivery-phase marker + declarative unconditional |
| C-40 | 5 | PASS | Formal declarative — baseline register |
| C-41 | 5 | PASS | No inertia framing — default pass |
| C-42 | 5 | PASS | Consequence-form anchor + explicit concern enumeration — both C-42 elements present |

**V-05 Score: 262 / 262** — FIRST CONFIRMED 262-pt CEILING

---

## Composite Score Summary

| Variation | Axis | Score | % Ceiling |
|-----------|------|-------|-----------|
| V-05 | Five-row non-standard + C-42 WHY + YOU MUST NOT | **262 / 262** | 100% |
| V-01 | C-42 reference form — formal declarative | **232 / 232** | 100% |
| V-02 | C-40 probe — RFC-modal MUST/SHALL | **232 / 232** | 100% |
| V-03 | C-41 saturation — 3-sentence inertia dominant | **232 / 232** | 100% |
| V-04 | C-40 + C-41 combined — imperative + inertia | **232 / 232** | 100% |

**Ranking**: V-05 first (262 raw pts, full ceiling). V-01 through V-04 tied (232 raw pts each, all hitting canonical ceiling).

All five variations reach their respective maximum achievable scores. No failures or degradations detected across any criterion.

---

## Excellence Signals — V-05 (Top-Scoring Variation)

**Signal 1 — C-42 WHY form is structurally portable across all R16 axes.** V-05 uses the identical WHY block as V-01 (formal declarative, consequence-form + concern enumeration) without modification despite adding the most structurally complex obligation table. The WHY block operates at trace-discipline scope independently of obligation table content, count, or term style — C-38 and C-42 coexist without any schema coupling.

**Signal 2 — YOU MUST NOT block is the precise dual-surface complement to the ARE directive.** V-05 achieves C-25 via the ARE directive and C-27 via the YOU MUST NOT block. These serve distinct enforcement surfaces: ARE catches structural substitution at the table schema level; YOU MUST NOT blocks semantic substitution at the prose/annotation level. The block names only the three substituted canonical tokens — delegation-chain (kept) and burst-start (new, no canonical) are correctly excluded from the prohibition scope (C-34 satisfied by scoping precision).

**Signal 3 — burst-start as a novel gap type with no canonical equivalent.** The burst-start obligation (first-invocation cold-path behavior) extends C-35 without triggering C-34 (no canonical token to prohibit). The Stage 3 gap type column is updated to include `burst-start-undefined` as a valid gap type, maintaining structural consistency between the obligation table, flag columns, and gap taxonomy.

**Signal 4 — R16 confirms full structural orthogonality of the three WHY-block axes.** C-40 (register), C-41 (framing context), and C-42 (content richness) operate on independent structural dimensions. V-02 tests register in isolation, V-03 tests framing context in isolation, V-04 tests register + framing context combined — no interaction. V-05 layers C-42 content richness on top of all confirmed structural elements, and the WHY block satisfies C-37/C-39/C-40/C-41/C-42 simultaneously in every variation.

---

```json
{"top_score": 262, "all_essential_pass": true, "new_patterns": ["RFC-modal MUST/SHALL register is register-neutral under C-40 — unconditional obligation modals preserve or strengthen constraint semantics relative to declarative indicative; no epistemic weakening introduced", "Three-sentence inertia-dominant framing does not structurally displace a present consequence-form anchor — C-41 holds at maximal inertia saturation with no volume threshold", "C-40 register axis and C-41 framing-context axis are structurally orthogonal — combined imperative-register plus inertia-framing form exhibits zero negative interaction; neither criterion reaches the other's structural dimension"]}
```
