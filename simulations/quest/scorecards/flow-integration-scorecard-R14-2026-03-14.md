# flow-integration — R14 Scoring (v14 rubric, 242 pt ceiling)

## Rubric Baseline

**Scoring architecture:**
- Essential C-01–C-04: 60 pts | Recommended C-05–C-07: 30 pts | Aspirational C-08–C-38: 152 pts
- Canonical-terms ceiling: 212 pts (C-27/C-30/C-31/C-34 require non-standard substitution; C-35/C-38 require extended obligation set)
- Full non-standard ceiling: 242 pts

**New criteria under test:**
- C-37 (5 pts): Temporal stakes anchor — explicit temporal OR delivery-phase anchor in WHY block converting framing from description to constraint
- C-38 (5 pts): Obligation-count-agnostic framing — canonical four-concern WHY satisfies C-36 regardless of extended obligation set

**R14 open questions:**
- Q1: Does consequence-form ("ship-blockers at integration review") satisfy C-37 as equivalently as temporal form ("before the feature ships")?
- Q2: Does temporal anchor alone — without concern enumeration — satisfy C-37?

---

## Common Base Assessment (applies to all five variations)

All variations share the same core structure. Criteria C-01 through C-26 and C-28–C-29, C-32–C-33 are assessed once and applied.

**Essential (60 pts — all PASS)**

| C | Pass condition satisfied | Evidence |
|---|--------------------------|----------|
| C-01 | Inventory-first; call types explicit; unknown/assumed-to-work entries expected | Inventory table with Call ID / Target System / Call Type / Confidence / flag columns present |
| C-02 | Every call has explicit auth entry | [N.1] AUTHENTICATION table per call block |
| C-03 | Method + key fields in separate labeled sections | [N.2] REQUEST AND RESPONSE FORMAT table |
| C-04 | Error disposition per call | [N.5] ERROR PROPAGATION table |

**Recommended (30 pts — all PASS)**

| C | Evidence |
|---|----------|
| C-05 | [N.3] RATE LIMITS section in every call block with limit value, burst risk, throttle response |
| C-06 | [N.4] RETRY AND IDEMPOTENCY table with retry strategy, idempotent Y/N, mitigation |
| C-07 | Stage 3 gap inventory with Call ID reference, Gap Type, Severity, Rationale, Remediation |

**Aspirational — shared criteria (C-08–C-26, C-28–C-29, C-32–C-33)**

| C | Pts | Verdict | Evidence |
|---|-----|---------|----------|
| C-08 | 5 | PASS | Gap table requires severity label + one-line rationale for every finding including MED/LOW |
| C-09 | 5 | PASS | HIGH findings require call-specific remediation sketch; generic advice named as insufficient |
| C-10 | 4 | PASS | INVENTORY GATE: Stage 2 does not open until table is complete |
| C-11 | 4 | PASS | Each of the five sections labeled with exactly one concern; sections isolated by label |
| C-12 | 4 | PASS | CALL-[N] COMPLETION GATE blocks CALL-[N+1] — explicit all-calls-covered condition |
| C-13 | 4 | PASS | Every concern section carries `*(this section: X only — other concerns each have their own sections)*` or equivalent exclusion annotation |
| C-14 | 4 | PASS | Five-item COMPLETION GATE per call block (auth / request-response / rate limits / retry / error propagation) |
| C-15 | 3 | PASS | NEW-CALL RULE: late-discovered calls get table row with all flag cells before analysis block opens |
| C-16 | 7 | PASS | Expert persona declaration names domain and all four obligation categories before inventory gate |
| C-17 | 7 | PASS | [N.3] RATE LIMITS block has limit value + burst risk + throttle response as separate labeled fields — in-block |
| C-18 | 5 | PASS | AGGREGATION RULE states populated-from + not-authoritative + not-required-for-assessment |
| C-19 | 5 | PASS | All four categories declared: forgotten-call / assumed-to-work / unknown-system / delegation-chain |
| C-20 | 5 | PASS | CROSS-STAGE coda fires unconditionally; explicit "no structures" default path present |
| C-21 | 5 | PASS | Four flag columns `[forgotten-call]` `[assumed-to-work]` `[unknown-system]` `[delegation-chain]` in inventory — flag count = category count |
| C-22 | 5 | PASS | Flag column headers are the same tokens as obligation terms in the persona declaration table |
| C-23 | 5 | PASS | CROSS-STAGE AGGREGATION STRUCTURES is unnumbered, appended after Stage 3 — no displacement |
| C-24 | 5 | PASS | Four-row obligation table — one row per category; structural auditability by row count |
| C-25 | 5 | PASS | Flag column headers ARE the Obligation Term values from the C-24 table — schema comparison verifiable |
| C-26 | 5 | PASS | Schema-only enforcement: ARE instruction present, no VOCABULARY RULE block |
| C-27 | — | *N/A canonical* | Canonical terms used in V-01–V-04; non-standard substitution not present |
| C-28 | 5 | PASS | Coda header: `*(no stage number — appended after Stage 3, the last numbered stage)*`; prose: "It does not appear between any two numbered stages; it does not displace or renumber any existing element" — both surfaces |
| C-29 | 5 | PASS | "The flag column headers in the Stage 1 inventory table ARE the Obligation Term column values above" — uppercase ARE in assertive declarative sentence |
| C-30 | — | *N/A canonical* | Depends on C-27 |
| C-31 | — | *N/A canonical* | Depends on C-27/C-30 |
| C-32 | 5 | PASS | Uppercase ARE keyword in assertive form — lowercase or non-assertive not present |
| C-33 | 5 | PASS | Multi-subject collective ARE: "The flag column headers…ARE the Obligation Term column values above" — plural collective subject |
| C-34 | — | *N/A canonical* | Depends on C-31 |
| C-35 | — | *N/A* (V-01–V-04) | Four-row canonical table; C-35 requires extended set N > 4 |
| C-36 | 5 | PASS | WHY THIS TRACE DISCIPLINE EXISTS block present before persona declaration; all variations name trace purpose |

**Canonical base subtotal (without C-37, without C-35/C-38, without C-27/C-30/C-31/C-34):**

| Section | Points |
|---------|--------|
| Essential | 60 |
| Recommended | 30 |
| Aspirational C-08–C-17 | 47 |
| Aspirational C-18–C-26, C-28–C-29, C-32–C-33, C-36 | 70 |
| **Base** | **207** |

---

## V-01 — C-37 Consequence-Form (Q1 Probe)

**WHY block:** "undocumented integration calls become ship-blockers at integration review and cannot be cleared without a completed trace."

**Form analysis:** Concern enumeration present (auth, rate limits, retry, error propagation). Temporal marker ("before the feature ships") absent. Consequence-form delivery-phase anchor present: "become ship-blockers **at integration review**."

**C-37 adjudication (Q1):**

C-37 pass condition: "explicit temporal **or** delivery-phase anchor naming the consequence boundary." The phrase "at integration review" is an explicit delivery-phase anchor — it names the phase at which undocumented calls BECOME ship-blockers. The framing converts from description ("what integration traces do") to constraint ("what happens when documentation is absent, and when"). The modal weakness of "can" is absent — "become ship-blockers" is declarative and unconditional.

**Q1 resolved: PERMISSIVE.** Consequence-form with explicit delivery-phase marker satisfies C-37 equivalently to temporal form.

| C | Pts | Verdict | Note |
|---|-----|---------|------|
| C-37 | 5 | **PASS** | "become ship-blockers at integration review" — explicit delivery-phase consequence boundary |
| C-38 | 0 | N/A | C-35 not in play (canonical four-row table) |

**V-01 score: 207 + 5 = 212 / 212 (canonical ceiling)**

---

## V-02 — C-37 Stakes-Alone (Q2 Probe)

**WHY block:** "Integration traces exist to surface every cross-system call a feature makes and to verify that all documentation gaps are resolved before the feature ships."

**Form analysis:** Temporal anchor present ("before the feature ships"). Concern enumeration absent — no mention of authentication, rate limits, retry behavior, or error propagation. Stakes-only framing.

**C-37 adjudication (Q2):**

C-37 pass condition: explicit temporal or delivery-phase anchor. The statement "documentation gaps are resolved **before the feature ships**" is an explicit temporal anchor naming the delivery-phase consequence boundary. Whether the framing also enumerates specific concerns (auth, rate limits, etc.) is not a C-37 requirement — C-37 codifies the stakes-anchor pattern, not the concern-enumeration pattern. V-01 (R13) established the pass boundary with both concern enumeration AND a temporal anchor; Q2 asks whether the temporal anchor alone achieves C-37. The conversion from description to constraint occurs by naming a delivery-phase boundary — the enumeration of concerns is C-36-grade content that supplements but is not required for the stakes anchor.

**Q2 resolved: PERMISSIVE.** Temporal anchor alone — without concern enumeration — satisfies C-37.

| C | Pts | Verdict | Note |
|---|-----|---------|------|
| C-37 | 5 | **PASS** | "before the feature ships" — temporal delivery-phase anchor present; concern enumeration not required |
| C-38 | 0 | N/A | C-35 not in play |

**V-02 score: 207 + 5 = 212 / 212 (canonical ceiling)**

---

## V-03 — Phrasing Register: Declarative (C-37 Register Neutrality Probe)

**WHY block:** "Each call's authentication, rate limits, retry behavior, and error propagation are documented before the feature ships — documentation gaps identified at that boundary are integration-review blockers, not post-ship discoveries."

**Form analysis:** Full C-37 form retained (temporal anchor + concern enumeration) in declarative register. Gate commands rephrased as declarative conditions ("CALL-[N+1] opens only after all five rows are confirmed"). Section exclusions reformulated ("the other four concerns each occupy a dedicated section").

**Declarative-register criteria check:**

| C | Assessment | Evidence |
|---|------------|----------|
| C-12 | PASS | "CALL-[N+1] opens only after all five rows are confirmed" — explicit completion condition; imperative mood not required |
| C-13 | PASS | "authentication only — the other four concerns each occupy a dedicated section in this call block" — single-concern declaration present; exclusion names the excluded class; all other concerns excluded |
| C-15 | PASS | "Any call discovered during Stage 2 analysis that is not already in this table receives a row — with all four flag cells set — before its analysis block opens" — explicitly required, declaratively stated |
| C-20 | PASS | "This coda is present regardless of Stage 2 output" — unconditional; explicit no-structures default present |

**C-37 adjudication:** Temporal anchor "before the feature ships" present in declarative form. C-37 names no register requirement. PASS.

| C | Pts | Verdict | Note |
|---|-----|---------|------|
| C-37 | 5 | **PASS** | Temporal anchor present in declarative form; register is a free variation axis |
| C-38 | 0 | N/A | C-35 not in play |

**V-03 score: 207 + 5 = 212 / 212 (canonical ceiling)**

---

## V-04 — Combined: Consequence-Form + Stakes-Alone (Lower Bound Probe)

**WHY block:** "Integration traces exist to surface the cross-system calls that can block a release — the ones not in the specification, the ones assumed to work, the ones with unknown owners, and the ones delegating credentials through chains the feature team has not mapped."

**Form analysis:** No temporal marker. No explicit delivery-phase anchor. No concern enumeration in documentation sense. Contains:
- Purpose statement: "surface the cross-system calls"
- Implied consequence: "**can** block a release" (modal — potential, not declarative)
- Obligation-category enumeration by description (not in documentation scope)

**C-37 adjudication:**

C-37 requires an "explicit temporal or delivery-phase anchor naming the consequence boundary." Analysis:

- "can block a release" — modal construction ("can"). Does not assert that undocumented calls WILL or DO become ship-blockers at a named phase. Compare to V-01: "become ship-blockers **at integration review**" (declarative + named phase). The modal form asserts possibility, not a consequence boundary.
- No delivery-phase named: "a release" is an event reference, not a delivery-phase anchor. It does not identify when in the feature lifecycle the consequence materializes.
- The framing describes categories of calls that are problematic — this is purpose-plus-scope framing, not stakes-anchor framing.

**Lower bound confirmed: FAIL.** Implicit consequence ("can block a release") without an explicit temporal marker or named delivery phase does not convert description to constraint. C-37 requires the explicit delivery-phase or temporal form — modal consequence language alone is insufficient.

| C | Pts | Verdict | Note |
|---|-----|---------|------|
| C-37 | 0 | **FAIL** | "can block a release" — modal/implied; no explicit temporal or delivery-phase consequence boundary |
| C-38 | 0 | N/A | C-35 not in play |

**V-04 score: 207 / 212 (−5 C-37)**

---

## V-05 — Combined: C-35 + C-37 Consequence-Form + C-38 (Full Ceiling Run)

**Configuration:**
- Five-row obligation table: expose-call / silent-entry / shadow-system / delegation-chain (canonical, kept) / burst-start (new, no canonical equivalent)
- YOU MUST NOT block: enumerates forgotten-call + assumed-to-work + unknown-system (three substituted canonical tokens)
- WHY block: consequence-form anchor + canonical four-concern framing, no burst-start mention

**WHY block:** "Integration traces exist to surface every cross-system call a feature makes and to verify that each call's authentication, rate limits, retry behavior, and error propagation are fully documented — calls without documentation become ship-blockers at integration review and cannot be cleared without a completed trace."

**Non-standard term assessment:**

| C | Pts | Verdict | Note |
|---|-----|---------|------|
| C-27 | 5 | **PASS** | Single YOU MUST NOT block present; enumerates forbidden canonical tokens explicitly |
| C-28 | 5 | PASS | Terminal-position formula in coda header + prose sentence both present |
| C-30 | 5 | **PASS** | YOU MUST NOT block is single, comprehensive — not distributed per-row |
| C-31 | 5 | **PASS** | Block enumerates "forgotten-call, assumed-to-work, or unknown-system" inline by name — self-contained prohibition surface |
| C-34 | 5 | **PASS** | All three substituted canonical tokens named (3/3); delegation-chain retained canonical (excluded from scope); burst-start new (excluded from scope) — substituted-subset scope complete |

**Extended obligation set assessment:**

| C | Pts | Verdict | Note |
|---|-----|---------|------|
| C-19 | 5 | PASS | All four canonical discovery categories present semantically: expose-call (forgotten-call), silent-entry (assumed-to-work), shadow-system (unknown-system), delegation-chain (kept) — plus burst-start |
| C-21 | 5 | PASS | Five flag columns match five obligation categories; flag count = category count = 5 |
| C-24 | 5 | PASS | Five-row table; one row per obligation category; structural auditability preserved |
| C-35 | 5 | **PASS** | N=5 extended obligation set; one-row-per-category rule satisfied at scale |

**C-37 adjudication (V-05):**

WHY block: "calls without documentation become ship-blockers **at integration review** and cannot be cleared without a completed trace."

Same consequence-form delivery-phase anchor as V-01 — "at integration review" is an explicit delivery-phase anchor. Q1 resolved permissive in V-01; the same form here achieves C-37. Concern enumeration (auth/rate-limits/retry/error-propagation) also present. → **PASS**

**C-38 adjudication:**

C-35 in play (five-row extended table with burst-start). WHY block uses canonical four-concern framing (authentication, rate limits, retry behavior, error propagation) — no burst-start mention. C-38 pass condition: framing block satisfies C-36 without enumerating extended obligation categories. The WHY block is evaluated at trace-discipline scope (purpose + stakes), not obligation-category enumeration scope. → **PASS**

| C | Pts | Verdict | Note |
|---|-----|---------|------|
| C-36 | 5 | PASS | WHY block names trace purpose; presence + position + purpose statement satisfied |
| C-37 | 5 | **PASS** | "become ship-blockers at integration review" — explicit delivery-phase anchor; Q1 permissive confirmed |
| C-38 | 5 | **PASS** | Canonical four-concern framing satisfies C-36 with five-row extended table; framing and obligation layers independent |

**Full V-05 score breakdown:**

| Section | Pts |
|---------|-----|
| Essential (C-01–C-04) | 60 |
| Recommended (C-05–C-07) | 30 |
| C-08–C-09 | 10 |
| C-10–C-14 | 20 |
| C-15 | 3 |
| C-16–C-17 | 14 |
| C-18–C-26, C-28–C-29, C-32–C-33 (shared) | 70 |
| C-27, C-30, C-31, C-34 (non-standard, all PASS) | 20 |
| C-35 | 5 |
| C-36, C-37, C-38 | 15 |
| **Total** | **247?** |

Wait — recalculating aspirational precisely:

C-08 (5) + C-09 (5) + C-10 (4) + C-11 (4) + C-12 (4) + C-13 (4) + C-14 (4) + C-15 (3) + C-16 (7) + C-17 (7) = 47  
C-18 through C-26: 9 × 5 = 45  
C-27 (5) + C-28 (5) + C-29 (5) + C-30 (5) + C-31 (5) + C-32 (5) + C-33 (5) + C-34 (5) + C-35 (5) + C-36 (5) + C-37 (5) + C-38 (5) = 60  

Aspirational total: 47 + 45 + 60 = 152 ✓  
Grand total: 60 + 30 + 152 = **242**

**V-05 score: 242 / 242 (full non-standard ceiling)**

---

## Score Summary

| Variation | Score | Ceiling | Delta | C-37 | C-38 | Q resolved |
|-----------|-------|---------|-------|------|------|------------|
| V-01 (consequence-form) | **212** | 212 | 0 | PASS | N/A | Q1: consequence-form PASS |
| V-02 (stakes-alone) | **212** | 212 | 0 | PASS | N/A | Q2: stakes-alone PASS |
| V-03 (declarative register) | **212** | 212 | 0 | PASS | N/A | register neutral confirmed |
| V-04 (lower bound) | **207** | 212 | −5 | FAIL | N/A | lower bound confirmed |
| V-05 (full ceiling) | **242** | 242 | 0 | PASS | PASS | Q1 permissive at scale |

**Rank: V-05 (242) > V-01 = V-02 = V-03 (212) > V-04 (207)**

---

## Q1 and Q2 Adjudications

**Q1 — C-37 temporal vs. consequence form: PERMISSIVE**

Consequence-form anchor with explicit delivery-phase marker ("become ship-blockers at integration review") satisfies C-37 equivalently to temporal form ("before the feature ships"). The pass condition requires "temporal OR delivery-phase anchor" — the phrase "at integration review" names the delivery-phase boundary. The declarative, unconditional form ("become") is essential; the modal lower-bound form ("can block a release") without a named phase fails.

**Q2 — C-37 stakes anchor alone vs. concern-enumerated: PERMISSIVE**

Temporal anchor alone ("all documentation gaps are resolved before the feature ships") satisfies C-37 without enumerating authentication, rate limits, retry behavior, or error propagation. Concern enumeration is C-36-grade content that enriches the framing but is not the stake anchor itself. C-37's conversion from description to constraint occurs at the temporal/delivery-phase boundary, not at the concern-enumeration level.

**C-37 lower bound established by V-04:**

The minimum failing form is: implied consequence ("can block a release") without explicit temporal or delivery-phase anchor. "A release" as a reference event does not name a delivery phase; "can" as a modal verb does not assert the consequence as a boundary condition. Both deficiencies together produce C-37 FAIL.

**C-37 minimum pass form:**

Any explicit statement of the form "documentation gap → consequence **at [named phase]** or **before [temporal marker]**" satisfies C-37. The named phase or temporal marker is the structurally required surface. Concern enumeration, specific concern naming, and temporal-vs-consequence form choice are free variation axes.

---

## Excellence Signals (V-05)

**1. Consequence-form delivery-phase anchor as C-37 pass form**
V-05 uses "become ship-blockers **at integration review**" without "before the feature ships." The delivery-phase anchor is the C-37 structural surface, not the temporal phrasing. This is a lighter-weight variation that achieves C-37 while varying the stakes articulation — the named phase ("integration review") is more precise than the generic temporal marker.

**2. Precision-scoped YOU MUST NOT enumeration**
The YOU MUST NOT block enumerates exactly the three substituted canonical tokens — forgotten-call, assumed-to-work, unknown-system — and correctly excludes delegation-chain (kept canonical) and burst-start (new category, no canonical equivalent). This is the minimum self-contained prohibition surface for C-31/C-34: enumerate every substituted canonical token, nothing more.

**3. Framing block and obligation table as independent structural layers**
The WHY block uses canonical four-concern framing with no burst-start mention despite a five-row obligation table that includes burst-start. C-38 PASS confirms: the framing block is evaluated at trace-discipline scope (what the discipline is for), the obligation table is evaluated at discovery-scope (what categories the model will apply). They do not need to align; canonical framing satisfies C-36/C-37 regardless of obligation set extension.

**4. Five-row extended set with mixed substitution pattern**
expose-call / silent-entry / shadow-system / delegation-chain / burst-start demonstrates three distinct table-entry patterns in one variation: standard canonical substitution (3 terms), canonical-kept (1 term), and new-without-canonical-equivalent (1 term). The YOU MUST NOT scoping correctly handles all three patterns from a single block.

---

## Open Questions for R15

**Q1 (partially resolved):** C-37 consequence-form with named delivery phase PASSES. Open sub-question: does consequence-form WITHOUT a named phase ("calls without documentation cannot ship" or "undocumented calls create release risk") satisfy C-37, or does the explicit phase name ("integration review") carry the structural weight?

**Q2 (resolved):** Temporal anchor alone satisfies C-37. Closed.

**New Q3:** V-03's declarative register used "the other four concerns each occupy a dedicated section" for C-13 section exclusion (class reference, not individually named concerns). Does C-13's "named exclusion of all other concerns" require individual concern names, or does a class reference ("the other four concerns") satisfy? V-03 scored C-13 PASS (class-reference form used); the individual-naming form has only appeared in prior canonical variations. This distinction could produce a new C-39 if individually-named exclusion is a strictly stronger form.

---

```json
{"top_score": 242, "all_essential_pass": true, "new_patterns": ["consequence-form delivery-phase anchor (become ship-blockers at integration review) satisfies C-37 equivalently to temporal form (before the feature ships) — Q1 resolved permissive", "temporal stakes anchor alone without concern enumeration satisfies C-37 — Q2 resolved permissive: concern enumeration is not a C-37 requirement", "implied-consequence-only form (can block a release) without explicit temporal or delivery-phase phase marker fails C-37 — lower bound: explicit phase or temporal anchor is the minimum pass surface"]}
```
