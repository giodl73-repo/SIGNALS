## flow-integration — R13 Score Report (v13 rubric, 232 pt ceiling)

---

### Evaluation Framework

**Trace artifact**: This round scores prompt-template variations (structural prescriptions), not executed traces. Criteria are evaluated against what the template instructs the model to produce.

**Key R13 questions under test:**
- **Q1**: Does C-36 require obligation-aware content, or does any purpose-naming prose satisfy it?
- **Q2**: When C-35 (5-row extended set) is in play, must the WHY block acknowledge extended categories?

**C-35 applicability note**: The pass condition for C-35 reads "N ≥ 4 obligation categories." A four-row canonical table satisfies C-35 because N=4 ≥ 4 — the criterion codifies the *scalability rule* (one-per-category), not a minimum of five rows. Confirmed by the canonical ceiling = 212 (which includes C-35) and the score predictions of 212/212 for V-01/V-03/V-05.

**C-27/C-30/C-31/C-34 applicability**: These 20 pts are N/A for canonical-term traces (no substitution = no prohibition surface needed). V-01, V-03, V-05 cap at 212.

---

## V-01 — C-36 Minimal Framing Content (Q1 Probe)

**Configuration**: 4-row canonical, one-sentence WHY block, imperative phrasing.
**WHY block**: "Integration traces exist to surface every cross-system call a feature makes and to verify that each call's authentication, rate limits, retry behavior, and error propagation are fully documented before the feature ships."

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Call inventory | PASS | Template with Call ID, Target System, Call Type, Confidence; unknown-system and assumed-to-work as flag columns |
| C-02 | Authentication documentation | PASS | [N.1] AUTHENTICATION section per call with Auth gap field |
| C-03 | Request and response format | PASS | [N.2] with Method, endpoint, request/response key fields as separate labeled rows |
| C-04 | Error propagation path | PASS | [N.5] ERROR PROPAGATION with Error disposition, Propagation path, Swallowing risk |
| C-05 | Rate limit exposure | PASS | [N.3] RATE LIMITS section with limit value, burst risk, throttle response per call |
| C-06 | Retry and idempotency analysis | PASS | [N.4] with retry strategy, idempotency flag, mitigation |
| C-07 | Gap inventory | PASS | STAGE 3 with Gap ID, Call ID, Gap Type, Severity, Rationale, Remediation columns |
| C-08 | Severity ranking | PASS | "Every finding must carry a severity label and a one-line rationale — MEDIUM and LOW findings are not exempt" |
| C-09 | Remediation sketch | PASS | "HIGH findings require a call-specific remediation sketch; generic advice does not satisfy" |
| C-10 | Inventory-first gate | PASS | STAGE 1 before STAGE 2; explicit INVENTORY GATE blocks Stage 2 |
| C-11 | Single-concern phase isolation | PASS | Each section labeled with exactly one concern |
| C-12 | Gate-enforced per-call completion | PASS | CALL-[N] COMPLETION GATE is explicit all-concerns condition |
| C-13 | Per-call section-level concern exclusion | PASS | "*(this section: authentication only — request/response format, rate limits, retry/idempotency, and error propagation each have their own sections below)*" |
| C-14 | Five-concern checklist | PASS | Checklist has all five concerns; explicitly gates next call block |
| C-15 | Late-call inventory discipline | PASS | NEW-CALL RULE present |
| C-16 | Expert persona declaration | PASS | Named expert persona before inventory gate with domain and four discovery obligations |
| C-17 | In-block rate limit completeness | PASS | Limit value, burst risk, throttle response as separate labeled fields per call |
| C-18 | Cross-stage structure secondary positioning | PASS | AGGREGATION RULE names all three: populated-FROM, not-authoritative, not-required-for-assessment |
| C-19 | Expert persona four-obligation scope | PASS | All four: forgotten-call, assumed-to-work, unknown-system, delegation-chain |
| C-20 | Unconditional cross-stage stage with default | PASS | Coda fires unconditionally; "No cross-stage structures produced in this trace" default present |
| C-21 | Inventory flag alignment | PASS | Four flag columns match four obligation categories; flag count = obligation count |
| C-22 | C-19/C-21 vocabulary unification | PASS | [forgotten-call], [assumed-to-work], [unknown-system], [delegation-chain] — exact token match |
| C-23 | Unnumbered coda as universal adapter | PASS | "*(no stage number — appended after Stage 3, the last numbered stage)*" |
| C-24 | Obligation table schema | PASS | Four-row table, one per obligation category, appears before inventory gate |
| C-25 | Schema-aligned C-22 enforcement | PASS | ARE instruction aligns flag column headers to Obligation Term row values |
| C-26 | Schema-only C-25 enforcement | PASS | No VOCABULARY RULE block; schema instruction alone enforces alignment |
| C-27 | Dual-surface prohibition | **N/A** (0) | Canonical terms — no substitution, no prohibition surface needed |
| C-28 | Explicit terminal-position formula | PASS | Header: "*(no stage number — appended after Stage 3, the last numbered stage)*" ✓; prose: "It does not appear between any two numbered stages; it does not displace or renumber any existing element." ✓ Both surfaces present |
| C-29 | Explicit ARE directive | PASS | "The flag column headers in the Stage 1 inventory table ARE the Obligation Term column values above — use those exact tokens as column headers" |
| C-30 | Single-block comprehensive prohibition | **N/A** (0) | Canonical terms |
| C-31 | Explicit inline token enumeration | **N/A** (0) | Canonical terms |
| C-32 | Uppercase ARE assertive form | PASS | "ARE" uppercase in assertive declarative sentence |
| C-33 | Multi-subject collective ARE form | PASS | "The flag column headers...ARE the Obligation Term column values above" — plural collective subject |
| C-34 | Complete inline enumeration (substituted-subset) | **N/A** (0) | Canonical terms — no substituted tokens |
| C-35 | C-24 extended obligation set scalability | PASS | N=4 ≥ 4; one-per-category rule satisfied; structural auditability preserved |
| C-36 | Motivational framing block | **PASS** | WHY block present before expert persona; names purpose ("surface every cross-system call… verify auth, rate limits, retry, error propagation are fully documented") and stakes ("before the feature ships"); Q1 resolution: presence + position + purpose statement is sufficient |

**C-36 Q1 adjudication**: The sentence names the trace discipline's purpose (surface all calls, verify documentation completeness) and stakes (pre-ship). "Before the feature ships" anchors the consequence. The criterion text emphasizes "its presence anchors the trace rationale above the persona boundary" — consistent with a minimal content standard. Any prose that names what the trace is for satisfies C-36. PASS.

**V-01 Score: 212 / 212**

---

## V-02 — C-35 + C-36 Count-Agnostic Framing (Q2 Probe)

**Configuration**: 5-row extended (trace-call/silent-pass/unverified-system/delegation-chain/cold-start), WHY block uses canonical four-obligation language only (no cold-start mention), YOU MUST NOT enumerates three substituted tokens.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01 | Call inventory | PASS | Five flag columns; unknown-system/assumed-to-work represented via unverified-system/silent-pass flags |
| C-02 | Authentication | PASS | [N.1] per call |
| C-03 | Request/response format | PASS | [N.2] with method + key fields |
| C-04 | Error propagation | PASS | [N.5] |
| C-05 | Rate limits | PASS | [N.3] |
| C-06 | Retry/idempotency | PASS | [N.4] |
| C-07 | Gap inventory | PASS | STAGE 3 with updated gap-type labels (unverified-system/delegation-chain/cold-start) |
| C-08 | Severity ranking | PASS | Same instruction as V-01 |
| C-09 | Remediation sketch | PASS | Same instruction |
| C-10 | Inventory-first gate | PASS | Same structure |
| C-11 | Single-concern isolation | PASS | Same structure |
| C-12 | Gate-enforced completion | PASS | COMPLETION GATE with five items |
| C-13 | Section-level concern exclusion | PASS | Per-section exclusion present |
| C-14 | Five-concern checklist | PASS | Five items, gates next call |
| C-15 | Late-call inventory discipline | PASS | NEW-CALL RULE with five flags |
| C-16 | Expert persona declaration | PASS | Persona before inventory, five obligations declared |
| C-17 | In-block rate limit completeness | PASS | Three labeled fields per call |
| C-18 | Cross-stage secondary positioning | PASS | AGGREGATION RULE with all three properties |
| C-19 | Expert persona four-obligation scope | PASS | Five categories declared — all four canonical plus cold-start (exceeds minimum) |
| C-20 | Unconditional cross-stage stage | PASS | Coda unconditional with default |
| C-21 | Inventory flag alignment | PASS | Five flags: [trace-call][silent-pass][unverified-system][delegation-chain][cold-start]; flag count = 5 = category count |
| C-22 | Vocabulary unification | PASS | Flag names match obligation terms exactly (non-standard-to-non-standard identity) |
| C-23 | Unnumbered coda | PASS | "(no stage number — appended after Stage 3, the last numbered stage)" |
| C-24 | Obligation table schema | PASS | Five-row table, one per category |
| C-25 | Schema-aligned C-22 enforcement | PASS | ARE instruction present |
| C-26 | Schema-only enforcement | PASS | No VOCABULARY RULE block |
| C-27 | Dual-surface prohibition | PASS | YOU MUST NOT block + schema alignment; both surfaces present |
| C-28 | Explicit terminal-position formula | PASS | Header formula ✓ + "It does not appear between any two numbered stages; it does not displace or renumber any existing element." ✓ |
| C-29 | Explicit ARE directive | PASS | Uppercase ARE assertive form |
| C-30 | Single-block comprehensive prohibition | PASS | One YOU MUST NOT block naming all three substituted tokens |
| C-31 | Explicit inline token enumeration | PASS | "YOU MUST NOT use forgotten-call, assumed-to-work, or unknown-system" — three tokens named inline |
| C-32 | Uppercase ARE assertive form | PASS | Uppercase ARE |
| C-33 | Multi-subject collective ARE | PASS | Plural collective form |
| C-34 | Complete inline enumeration (substituted-subset) | PASS | Three substituted tokens enumerated; delegation-chain (kept canonical) and cold-start (no canonical equivalent) correctly excluded from prohibition scope |
| C-35 | Extended obligation set scalability | PASS | Five-row table, N=5 ≥ 4, one-per-category rule preserved |
| C-36 | Motivational framing block | **PASS** | WHY block present before persona; names purpose and stakes using canonical four-obligation framing; Q2 resolution: count-agnostic framing satisfies C-36 regardless of obligation set size |

**C-36 Q2 adjudication**: The WHY block names the purpose and stakes of the integration trace discipline — it explains why undocumented calls cause production incidents and why the four obligation categories exist. That the framing uses canonical four-obligation language while five obligations are in the table is immaterial to C-36's pass condition: the block anchors trace rationale above the persona boundary. C-36's structural role is positional (above the persona) and content-minimal (purpose + stakes). It does not function as an obligation-set index. PASS.

**V-02 Score: 232 / 232**

---

## V-03 — Phrasing Register (Structural Neutrality Probe)

**Configuration**: 4-row canonical, declarative/descriptive phrasing throughout, obligation-aware WHY block.
**Key register changes**: "The inventory table is fully populated before Stage 2 analysis begins" (vs. "Populate this table before opening Stage 2"); "CALL-[N+1] opens only after the CALL-[N] COMPLETION GATE confirms all five concerns are documented"; section exclusions: "*(authentication only — the other four concerns each occupy a dedicated section in this call block)*"; coda: "This coda is present regardless of Stage 2 output."

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01–C-07 | Essential + Recommended | PASS all | Same template structure; concern columns, auth fields, format fields, error fields, gap table all present |
| C-08–C-09 | Severity / Remediation | PASS | Stage 3 instructions preserved verbatim (declarative register applied in stage body, not in the instruction sentences themselves — "Each finding carries a severity label") |
| C-10 | Inventory-first gate | PASS | "INVENTORY GATE: Stage 2 analysis begins only when every discovered call has a row..." — declarative gate is explicit and structural |
| C-11 | Single-concern isolation | PASS | Each section labeled with one concern |
| C-12 | Gate-enforced per-call completion | PASS | "CALL-[N+1] opens only after the CALL-[N] COMPLETION GATE confirms all five concerns are documented" — explicit completion condition; declarative ≠ voluntary |
| C-13 | Section-level concern exclusion | PASS | "*(authentication only — the other four concerns each occupy a dedicated section in this call block)*" — single-concern declaration + named exclusion present |
| C-14 | Five-concern checklist | PASS | Five-item checklist; "CALL-[N+1] opens only after all five rows are confirmed" |
| C-15 | Late-call inventory discipline | PASS | "Any call discovered during Stage 2 analysis that is not already in the inventory receives a row — with all four flag cells set — before its analysis block opens" |
| C-16 | Expert persona | PASS | Named persona before inventory gate |
| C-17 | In-block rate limit completeness | PASS | Three labeled fields |
| C-18 | Cross-stage secondary positioning | PASS | "populated FROM the per-call blocks — not the authoritative source... not required for trace assessment" — all three properties present in declarative form |
| C-19 | Four-obligation scope | PASS | Four categories in table |
| C-20 | Unconditional cross-stage | PASS | "This coda is present regardless of Stage 2 output. When Stage 2 produces no cross-stage aggregation structures, the entry reads: 'No cross-stage structures produced in this trace.'" — unconditional + explicit default ✓ |
| C-21 | Flag alignment | PASS | Four flags = four categories |
| C-22 | Vocabulary unification | PASS | Exact token match |
| C-23 | Unnumbered coda | PASS | Header formula present |
| C-24 | Obligation table | PASS | Four-row one-per-category |
| C-25 | Schema-aligned enforcement | PASS | ARE instruction present |
| C-26 | Schema-only | PASS | No VOCABULARY RULE block |
| C-27 | Dual-surface prohibition | **N/A** (0) | Canonical terms |
| C-28 | Terminal-position formula | PASS | Header: "*(no stage number — appended after Stage 3, the last numbered stage)*" ✓; prose: "It occupies no position between numbered stages; no existing element is displaced or renumbered." ✓ — rephrased but both surfaces intact |
| C-29 | Explicit ARE directive | PASS | Uppercase ARE assertive form unchanged |
| C-30–C-31 | Single-block / Inline enumeration | **N/A** (0, 0) | Canonical terms |
| C-32–C-33 | Uppercase ARE / Collective form | PASS | Unchanged ARE directive |
| C-34 | Complete enumeration | **N/A** (0) | Canonical terms |
| C-35 | Extended scalability | PASS | N=4 ≥ 4 |
| C-36 | Motivational framing block | PASS | Obligation-aware WHY block: "These forgotten calls, assumed-to-work entries, unknown-system placeholders, and delegation-chain exposures are the ones that cause production incidents. This trace discipline exists to discover them before the feature ships." Names all four categories + stakes explicitly |

**Structural neutrality confirmed**: Register change from imperative to declarative does not affect any pass/fail verdict. Gate instructions stated as declarations ("opens only after... confirms") are equally explicit — the gate fires on the same structural condition. Section exclusions phrased as descriptions carry the same single-concern declaration and named-exclusion content. Coda framing "is present regardless of" is equivalent to "fires unconditionally."

**V-03 Score: 212 / 212**

---

## V-04 — Combined: C-35 + C-36 Extended-Set-Aware Framing (Q1+Q2 Joint Probe)

**Configuration**: 5-row extended (same non-standard terms as V-02), WHY block explicitly names all five obligation categories including cold-start, imperative phrasing.

All structure identical to V-02 except WHY block content. Scoring differs only on C-36.

| ID | Criteria | Verdict | Delta from V-02 |
|----|----------|---------|----------------|
| C-01–C-34 | All criteria | PASS (same as V-02) | None — identical structure |
| C-35 | Extended scalability | PASS | Same five-row table |
| C-36 | Motivational framing block | **PASS** | WHY block names all five categories including cold-start as bullet points with stakes ("A trace that documents only the calls the specification named has not completed this discipline.") — satisfies C-36 under any Q1/Q2 resolution |

**V-04 Score: 232 / 232**

V-04 is the safe upper bound: regardless of how Q1/Q2 resolve, extended-set-aware framing satisfies C-36. Since V-02 also passes C-36 (count-agnostic framing sufficient), both V-02 and V-04 achieve 232/232.

---

## V-05 — Combined: Inertia Framing + Phrasing Register + Minimal C-36

**Configuration**: 4-row canonical, declarative phrasing (V-03 style), contrast/inertia WHY block.
**WHY block**: "The default approach to integration traces takes the spec's call list… A spec-walkthrough trace finds the calls someone already thought of. This trace finds the ones they did not."

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|---------|
| C-01–C-07 | Essential + Recommended | PASS all | Same template structure as V-03 |
| C-08–C-15 | Aspirational lower | PASS all | Same instructions as V-03 |
| C-16–C-17 | Persona + Rate limits | PASS | Identical persona and rate-limit structure |
| C-18–C-26 | Cross-stage + Obligation structure | PASS all | Same AGGREGATION RULE, ARE instruction, obligation table, flag columns |
| C-27 | Dual-surface prohibition | **N/A** (0) | Canonical terms |
| C-28 | Terminal-position formula | PASS | "*(no stage number — appended after Stage 3, the last numbered stage)*" ✓; "It occupies no position between numbered stages; no existing element is displaced or renumbered." ✓ |
| C-29 | Explicit ARE directive | PASS | Uppercase ARE assertive form unchanged |
| C-30–C-31 | Single-block / Inline enumeration | **N/A** (0, 0) | Canonical terms |
| C-32–C-33 | Uppercase ARE / Collective form | PASS | ARE form unchanged |
| C-34 | Complete enumeration | **N/A** (0) | Canonical terms |
| C-35 | Extended scalability | PASS | N=4 ≥ 4 |
| C-36 | Motivational framing block | **PASS** | WHY block present before persona; names stakes explicitly ("The calls that cause production incidents are not in that record") and purpose implicitly through contrast ("This trace finds the ones they did not"); four obligation categories illustrated by example (token refresh = forgotten-call, SDK probe = forgotten-call, unknown service = unknown-system, managed identity chain = delegation-chain); Q1 resolution applies: contrast framing that names stakes and purpose through displacement of the spec-walkthrough baseline satisfies C-36 |

**C-36 inertia-framing adjudication**: The WHY block names what the trace discipline exists to do — by contrast with what it displaces. Stakes ("production incidents") are named explicitly. Purpose ("find the calls they did not") is established through the contrast. The block is present before the expert persona and anchors the rationale. This is a different content strategy than direct enumeration but satisfies the "names the purpose and stakes" content standard. PASS.

**Three-axis composition confirmed**: Inertia framing + declarative register + contrast WHY framing compose independently. No criterion drops below its pass threshold when all three are applied together.

**V-05 Score: 212 / 212**

---

## Score Summary

| Variation | Ceiling | Score | Gap | Key result |
|-----------|---------|-------|-----|------------|
| V-04 | 232 | **232** | 0 | Perfect. Extended-set-aware framing — safe Q1+Q2 upper bound |
| V-02 | 232 | **232** | 0 | Perfect. Count-agnostic framing satisfies C-36 with five-row table |
| V-01 | 212 | **212** | 0 | Q1 resolved: minimal one-sentence WHY passes C-36 |
| V-03 | 212 | **212** | 0 | Register neutrality confirmed: declarative = imperative for all criteria |
| V-05 | 212 | **212** | 0 | Contrast/inertia framing passes C-36; all three combined axes neutral |

**Ranking**: V-02 = V-04 (232/232) > V-01 = V-03 = V-05 (212/212)

---

## Open Question Resolutions

### Q1 — C-36 Motivational Framing Content Specificity: RESOLVED

**Verdict**: C-36 is a structural criterion about block presence and position. Any prose block appearing before the expert persona that names the purpose of the trace discipline — regardless of content specificity — satisfies C-36. Obligation-category enumeration is not required.

**Evidence chain**: V-01's one sentence ("Integration traces exist to surface every cross-system call a feature makes and to verify that each call's authentication, rate limits, retry behavior, and error propagation are fully documented before the feature ships") passes C-36 at the same 212/212 ceiling as V-03's fully obligation-aware framing. V-05's contrast framing (which names stakes explicitly but purpose only by implication) also passes.

**Pass boundary established by V-01**: One sentence naming the trace goal (what the trace surfaces + what it verifies) + implied stakes (pre-ship) satisfies C-36. Content below this threshold (a block with no purpose content at all, just a header) would not satisfy.

### Q2 — C-35 + C-36 Extended-Set Framing Alignment: RESOLVED

**Verdict**: C-36 does not require the motivational framing block to acknowledge extended obligation categories beyond the canonical four. Obligation-count-agnostic framing satisfies C-36 regardless of obligation set size. The framing block is not an obligation-set index — it is a static rationale anchor.

**Evidence chain**: V-02's WHY block uses canonical four-obligation language ("forgotten calls, assumed-to-work entries, unknown-system placeholders, delegation chain risk") while the obligation table has five rows including cold-start. C-36 passes. V-04's WHY block names all five categories — same C-36 score. The difference between V-02 and V-04 is zero points; the extended-category acknowledgment is a stylistic choice, not a structural requirement.

---

## Excellence Signals (from V-02 and V-04, the top-scoring variations)

**Signal 1 — Extended obligation set preserves all schema discipline**: A five-row obligation table satisfies C-24, C-25, C-26, C-29, C-33, and C-35 with no schema degradation. The flag table in the inventory mirrors the five-row obligation table exactly. Adding a sixth obligation would follow the same pattern.

**Signal 2 — Substituted-subset YOU MUST NOT precision is exact, not conservative**: V-02/V-04 enumerate exactly three tokens in the YOU MUST NOT block — the three substituted canonical terms. delegation-chain is deliberately excluded (kept canonical, not a prohibition target). cold-start is excluded (new category, no canonical equivalent to prohibit). This precision satisfies C-34 by demonstrating complete coverage of the substituted subset, not over-coverage of the full table.

**Signal 3 — Motivational framing block is a robust free variation axis**: C-36 passes with: minimal one-sentence framing (V-01), count-agnostic four-obligation framing (V-02), direct obligation-aware framing (V-03), extended-set-aware framing (V-04), contrast/inertia framing (V-05). The framing block's structural contribution is position and presence, not content prescriptiveness.

**Signal 4 — Declarative gate phrasing is structurally equivalent to imperative**: "CALL-[N+1] opens only after… confirms all five concerns are documented" satisfies C-12 identically to "Do not open CALL-[N+1] until the CALL-[N] COMPLETION GATE is fully checked." The condition is explicit regardless of mood.

---

```json
{"top_score": 232, "all_essential_pass": true, "new_patterns": ["Minimal one-sentence WHY block satisfies C-36: presence, position, and minimal purpose statement are sufficient — obligation-category enumeration is not required (Q1 resolved)", "Count-agnostic motivational framing satisfies C-36 even when extended obligation set is in play: the WHY block need not acknowledge the extended categories to meet the presence-and-purpose standard (Q2 resolved)", "Contrast/inertia framing satisfies C-36: implicit purpose through displacement of the spec-walkthrough baseline meets the names-the-purpose-and-stakes content requirement"]}
```
