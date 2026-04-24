## flow-integration — R12 Scoring (v12 rubric, 222 pt ceiling)

---

### Scoring Basis

**Point schedule:**
- C-01–C-04: 15 each (60 total, essential)
- C-05–C-07: 10 each (30 total, recommended)
- C-08–C-09: 5 each; C-10–C-14: 4 each; C-15: 3; C-16–C-17: 7 each
- C-18–C-34: 5 each (aspirational)

**Canonical-terms ceiling: 202 pts** — C-27/C-30/C-31/C-34 require non-standard substitution and are N/A (20 pts off-ceiling) for V-01, V-03, V-05.

**Non-canonical ceiling: 222 pts** — all criteria achievable when non-standard terms are in use.

---

## V-01 — C-33 Alternate ARE Subject Form (Q1 Probe)

Axis: "Flag column headers ARE the Obligation Term column values above" (drops definite article "the" and "in the Stage 1 inventory table" qualifier; ARE keyword and plural-subject collective form preserved).

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Call inventory | PASS | Inventory table schema present with Call ID, Target System, Call Type, Confidence |
| C-02 | Authentication documentation | PASS | N.1 AUTHENTICATION block per call with five labeled fields |
| C-03 | Request and response format | PASS | N.2 with Method, Endpoint, Request/Response key fields, Encoding — separate labeled positions |
| C-04 | Error propagation path | PASS | N.5 ERROR PROPAGATION with Error disposition, Propagation path, Swallowing risk |
| C-05 | Rate limit exposure | PASS | N.3 RATE LIMITS with Limit value, Burst risk, Throttle response |
| C-06 | Retry and idempotency | PASS | N.4 with Retry strategy, Idempotent, Mitigation if non-idempotent |
| C-07 | Gap inventory | PASS | Stage 3 GAP INVENTORY table with Call ID, Gap Type, Severity, Rationale, Remediation |
| C-08 | Severity ranking | PASS | Severity column (HIGH/MED/LOW) + Rationale column in Stage 3; MEDIUM/LOW not exempt |
| C-09 | Remediation sketch | PASS | Remediation column in Stage 3; instruction explicitly calls out HIGH findings |
| C-10 | Inventory-first gate | PASS | Stage 1 (inventory) precedes Stage 2 (per-call analysis) |
| C-11 | Single-concern phase isolation | PASS | Per-call sections carry "(this section: X only — Y, Z each have their own sections)" exclusions |
| C-12 | Gate-enforced per-call completion | PASS | INVENTORY GATE: "Stage 2 does not open until the table is complete" |
| C-13 | Per-call section-level concern exclusion | PASS | Each N.x section names one concern and excludes all others explicitly |
| C-14 | Five-concern completion checklist | PASS | CALL-[N] COMPLETION GATE with five rows; "Do not open CALL-[N+1] until all five rows are checked" |
| C-15 | Late-call inventory discipline | PASS | NEW-CALL RULE: "add a row with all four flag cells set before opening that call's analysis block" |
| C-16 | Expert persona declaration | PASS | EXPERT PERSONA DECLARATION before Stage 1; names domain + four discovery obligations |
| C-17 | In-block rate limit completeness | PASS | N.3 with three separate labeled fields; no registry-pointer shortcut |
| C-18 | Cross-stage structure secondary positioning | PASS | AGGREGATION RULE: populated-from + not-authoritative + not-required-for-assessment all explicit |
| C-19 | Expert persona four-obligation scope | PASS | All four categories present: forgotten-call, assumed-to-work, unknown-system, delegation-chain |
| C-20 | Unconditional cross-stage stage | PASS | Coda fires unconditionally; "If Stage 2 produced no cross-stage aggregation structures, write: 'No cross-stage structures produced'" |
| C-21 | Inventory flag alignment | PASS | [forgotten-call] [assumed-to-work] [unknown-system] [delegation-chain] as flag columns |
| C-22 | C-19/C-21 vocabulary unification | PASS | Flag column headers are exact tokens from obligation table rows — token identity confirmed by schema comparison |
| C-23 | Unnumbered coda | PASS | "no stage number — appended after Stage 3, the last numbered stage" |
| C-24 | Four-obligation table schema | PASS | Structured table, four rows, one per obligation category, before inventory gate |
| C-25 | Schema-aligned C-22 enforcement | PASS | Flag headers match obligation row terms; mismatch is visible by table comparison |
| C-26 | Schema-only C-25 enforcement | PASS | Schema instruction present; no VOCABULARY RULE block needed or used |
| C-27 | Dual-surface prohibition | N/A | Canonical terms — no substitution in play; no YOU MUST NOT block needed |
| C-28 | Explicit terminal-position formula | PASS | Header annotation + "It does not appear between any two numbered stages; it does not displace or renumber any existing element" |
| C-29 | ARE directive requirement | PASS | "Flag column headers ARE the Obligation Term column values above" — uppercase ARE in assertive declarative sentence |
| C-30 | Single-block comprehensive prohibition | N/A | Canonical terms — C-27 not triggered |
| C-31 | Explicit inline token enumeration | N/A | Canonical terms — C-30 not triggered |
| C-32 | Uppercase ARE assertive form | PASS | ARE is uppercase; sentence is assertive and declarative |
| C-33 | Multi-subject collective ARE form | PASS | "Flag column headers ARE..." — plural collective subject, single assertion covering all headers; "e.g." in C-33 definition confirms exact subject phrase is not required; any valid multi-subject plural ARE construction satisfies the structural requirement |
| C-34 | Complete inline enumeration | N/A | Canonical terms — C-31 not triggered |

**Score: 202 / 202** (canonical ceiling)
**Q1 resolution: PASS** — Alternate multi-subject ARE subject ("Flag column headers ARE...") satisfies C-33. Definite article and positional qualifier are incidental to the structural form, not definitional.

---

## V-02 — C-34 Extended Obligation Set, Substituted-Subset Enumeration (Q2 Probe)

Axis: Five-row obligation table (OBL-1/2/3 non-standard: trace-call/silent-pass/unverified-system; OBL-4 canonical kept: delegation-chain; OBL-5 new: cold-start). YOU MUST NOT block enumerates only the three substituted canonical tokens (forgotten-call, assumed-to-work, unknown-system).

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-09 | Essential + depth | PASS | All five stages structurally complete; same analysis as V-01 |
| C-10–C-15 | Format structural | PASS | Stage ordering, per-call sections, gate, completion checklist, late-call rule all present |
| C-16 | Expert persona declaration | PASS | EXPERT PERSONA DECLARATION before Stage 1; five obligations named (four canonical categories + cold-start extension) |
| C-17 | In-block rate limit completeness | PASS | N.3 with three fields per call block |
| C-18 | Cross-stage structure secondary positioning | PASS | AGGREGATION RULE present with all three demotion properties |
| C-19 | Expert persona four-obligation scope | PASS | All four canonical categories covered by non-standard terms (trace-call → forgotten, silent-pass → assumed, unverified-system → unknown, delegation-chain canonical) plus cold-start extension |
| C-20 | Unconditional cross-stage stage | PASS | Coda unconditional with no-structures default |
| C-21 | Inventory flag alignment | PASS | [trace-call] [silent-pass] [unverified-system] [delegation-chain] [cold-start] — five flags covering all five obligation rows |
| C-22 | Vocabulary unification | PASS | Flag headers exactly match five obligation row terms; token identity confirmed by schema |
| C-23 | Unnumbered coda | PASS | Coda appended after Stage 3 with no stage number |
| C-24 | Obligation table schema | PASS | Five-row structured table, one row per obligation category, before inventory gate; C-24 requires "one row per obligation category" — five categories, five rows satisfies the structural requirement |
| C-25 | Schema-aligned enforcement | PASS | Five flag column headers match five obligation table row terms |
| C-26 | Schema-only enforcement | PASS | ARE instruction present; no VOCABULARY RULE block |
| C-27 | Dual-surface prohibition | PASS | (1) Schema alignment (C-25) present; (2) YOU MUST NOT block names specific forbidden canonical tokens: "YOU MUST NOT use forgotten-call, assumed-to-work, or unknown-system as column headers or obligation names in this trace" — these are the three canonical tokens that were substituted and are now forbidden |
| C-28 | Terminal-position formula | PASS | Both surfaces: header annotation + prose sentence prohibiting mid-sequence placement |
| C-29 | ARE directive requirement | PASS | "The flag column headers in the Stage 1 inventory table ARE the Obligation Term column values above" — confirmed standard form |
| C-30 | Single-block comprehensive prohibition | PASS | Single YOU MUST NOT block; all substituted canonical tokens named together, not distributed across rows |
| C-31 | Explicit inline token enumeration | PASS | Block explicitly names forbidden-call, assumed-to-work, unknown-system by name inside the block; no table-reference shorthand |
| C-32 | Uppercase ARE assertive form | PASS | ARE uppercase, assertive declarative sentence |
| C-33 | Multi-subject collective ARE form | PASS | "The flag column headers in the Stage 1 inventory table ARE..." — confirmed form |
| C-34 | Complete inline enumeration (full coverage) | PASS | Substituted canonical tokens = forgotten-call (OBL-1), assumed-to-work (OBL-2), unknown-system (OBL-3) — exactly three; all three named in YOU MUST NOT block. delegation-chain (OBL-4) was not substituted — it is canonical and used, no prohibition needed. cold-start (OBL-5) has no canonical equivalent to prohibit — "each substituted canonical token" applies only to terms where a canonical token was replaced; per-substitution reading is the natural reading of C-31/C-34; prohibition surface is self-contained for all substituted terms |

**Score: 222 / 222** (full ceiling)
**Q2 resolution: PASS** — Substituted-subset enumeration satisfies C-34. "Each substituted canonical token" means every token where a canonical term was replaced by a non-standard substitute. Kept canonical terms (delegation-chain) and new terms with no canonical equivalent (cold-start) are outside C-34's scope.

---

## V-03 — Inertia Framing Prominence (Structural Neutrality Probe)

Axis: WHY THIS TRACE DISCIPLINE EXISTS prose block prepended before expert persona. No schema changes.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-32 | All prior criteria | PASS | Structurally identical to confirmed canonical baseline; WHY block contains no schema instructions, obligation terms, or format rules |
| C-33 | Multi-subject collective ARE form | PASS | "The flag column headers in the Stage 1 inventory table ARE the Obligation Term column values above" — confirmed form unchanged |
| C-34 | Complete inline enumeration | N/A | Canonical terms |
| C-27/C-30/C-31 | Dual-surface prohibition | N/A | Canonical terms |

No rubric criterion responds to contrast prose framing in either direction. The WHY block is purely explanatory — it names a displaced approach and explains the architectural rationale. All structural criteria test presence of schema elements, table rows, gate instructions, and vocabulary enforcement mechanisms, none of which are altered.

**Score: 202 / 202** (canonical ceiling)
**Inertia framing confirmed structurally neutral** — free variation axis.

---

## V-04 — Combined: C-33 Alternate ARE Subject + C-34 Extended Obligation Set (Q1+Q2 Joint Probe)

Axis: V-01's alternate ARE subject ("Flag column headers ARE...") + V-02's five-row mixed table with substituted-subset YOU MUST NOT enumeration.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-22 | Structural complete | PASS | Five-stage structure, five-row obligation table, flag alignment, vocabulary unification — same analysis as V-02 |
| C-23 | Unnumbered coda | PASS | Terminal-position pattern preserved |
| C-24 | Obligation table schema | PASS | Five-row table, one row per category |
| C-25 | Schema-aligned enforcement | PASS | Five flag headers match five obligation row terms |
| C-26 | Schema-only enforcement | PASS | No VOCABULARY RULE block; schema instruction alone |
| C-27 | Dual-surface prohibition | PASS | Schema alignment (C-25) + YOU MUST NOT block naming forbidden-call, assumed-to-work, unknown-system explicitly |
| C-28 | Terminal-position formula | PASS | Both surfaces present |
| C-29 | ARE directive requirement | PASS | "Flag column headers ARE the Obligation Term column values above" — ARE keyword present, assertive form |
| C-30 | Single-block prohibition | PASS | Single block, all substituted canonical tokens together |
| C-31 | Explicit inline enumeration | PASS | All three substituted canonical tokens named inside block |
| C-32 | Uppercase ARE | PASS | ARE uppercase |
| C-33 | Multi-subject collective ARE form | PASS | "Flag column headers ARE..." — plural collective subject, single assertion; same Q1 ruling as V-01: any valid multi-subject ARE construction satisfies C-33 |
| C-34 | Complete inline enumeration (full coverage) | PASS | Same Q2 ruling as V-02: substituted-subset is complete per-substitution; cold-start (no canonical equivalent) and delegation-chain (canonical kept) correctly excluded from YOU MUST NOT block |

**Score: 222 / 222** (full ceiling)
Both Q1 and Q2 resolve positively in joint test. No cascading failures. Combined-axis variation confirms both rulings are independent and composable.

---

## V-05 — Combined: Role Sequence + Phrasing Register (Confirming Clean Sweep)

Axis: Expert persona embedded inline within Stage 1 (after Stage 1 header, before inventory gate). Formal/technical declarative register throughout (noun-phrase section headers, declarative gate instructions).

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01–C-15 | Essential through late-call | PASS | Stage 1 still first; Stage 2 per-call analysis follows; five concern sections per call; gate explicit; late-call rule present ("a row with all four flag cells set is added before that call's analysis block is opened") |
| C-16 | Expert persona declaration | PASS | "Expert Persona and Discovery Obligations" subsection appears inside Stage 1 but BEFORE the Inventory Gate subsection; C-16 requires persona "before the inventory gate" — inline pre-gate positioning satisfies this; section-header presence vs. inline embedding is not a C-16 requirement |
| C-17 | In-block rate limit completeness | PASS | N.3 RATE LIMITS with three labeled fields |
| C-18 | Cross-stage structure secondary positioning | PASS | Aggregation Rule present in Stage 2 with all three demotion properties |
| C-19 | Expert persona four-obligation scope | PASS | Four obligation categories listed inline before inventory gate: forgotten-call, assumed-to-work, unknown-system, delegation-chain |
| C-20 | Unconditional cross-stage stage | PASS | Coda fires unconditionally with no-structures default |
| C-21 | Inventory flag alignment | PASS | [forgotten-call] [assumed-to-work] [unknown-system] [delegation-chain] as column headers |
| C-22 | Vocabulary unification | PASS | Flag headers match obligation row terms; token identity holds |
| C-23 | Unnumbered coda | PASS | Appended after Stage 3 with no stage number |
| C-24 | Four-obligation table schema | PASS | Obligation table appears inline within Stage 1 before the Inventory Gate subsection; "before the inventory gate" is satisfied by pre-gate positioning regardless of section boundary |
| C-25 | Schema-aligned enforcement | PASS | Flag headers match obligation table row terms |
| C-26 | Schema-only enforcement | PASS | No VOCABULARY RULE block |
| C-27–C-31 | Dual-surface prohibition | N/A | Canonical terms |
| C-28 | Terminal-position formula | PASS | Both surfaces present in coda header and prose |
| C-29 | ARE directive requirement | PASS | "The flag column headers in the Stage 1 inventory table ARE the Obligation Term column values above" — confirmed form |
| C-30 | Single-block prohibition | N/A | Canonical terms |
| C-31 | Explicit inline enumeration | N/A | Canonical terms |
| C-32 | Uppercase ARE | PASS | ARE uppercase, assertive |
| C-33 | Multi-subject collective ARE form | PASS | Confirmed standard form |
| C-34 | Complete inline enumeration | N/A | Canonical terms |

**Score: 202 / 202** (canonical ceiling)
**Inline persona positioning confirmed:** C-16/C-19/C-24 "before the inventory gate" requirement is about temporal/positional relationship to the gate, not about the persona occupying a standalone pre-Stage-1 section. Register variation is structurally neutral.

---

## Composite Score Table

| Variation | Score | Ceiling | Predicted | Delta | Q Resolved |
|-----------|-------|---------|-----------|-------|-----------|
| V-01 | 202/202 | 202 (canonical) | 202/202 | 0 | Q1: PASS — alternate multi-subject ARE satisfies C-33 |
| V-02 | 222/222 | 222 | 222/222 | 0 | Q2: PASS — substituted-subset enumeration satisfies C-34 |
| V-03 | 202/202 | 202 (canonical) | 202/202 | 0 | Structural neutrality confirmed |
| V-04 | 222/222 | 222 | 222/222 | 0 | Q1+Q2 both PASS; no cascade |
| V-05 | 202/202 | 202 (canonical) | 202/202 | 0 | Inline persona positioning confirmed |

All five variations at ceiling. All predictions confirmed.

---

## Ranking

| Rank | Variation | Score | Why |
|------|-----------|-------|-----|
| 1 (tied) | V-02 | 222/222 | Q2 probe — extended obligation set with per-substitution YOU MUST NOT; first to reach 222 |
| 1 (tied) | V-04 | 222/222 | Q1+Q2 joint probe — both open questions resolved together at ceiling |
| 3 (tied) | V-01 | 202/202 | Q1 probe — canonical ceiling; C-33 settled |
| 3 (tied) | V-03 | 202/202 | Inertia framing; canonical ceiling |
| 3 (tied) | V-05 | 202/202 | Inline persona; canonical ceiling |

---

## Excellence Signals

**Top-scoring patterns from V-02 and V-04 (222/222):**

1. **Per-substitution enumeration boundary** — C-34 applies to substituted canonical tokens only. The YOU MUST NOT block is self-contained when it names exactly the canonical tokens that were replaced. New terms with no canonical equivalent (cold-start) have nothing to prohibit — there is no canonical token being displaced. Kept canonical terms (delegation-chain) must not appear in the YOU MUST NOT block because they are the correct terms. The prohibition surface is defined by substitution, not by table row count.

2. **Reduced-phrase ARE subject satisfies C-33** — The multi-subject collective ARE form is a structural property (plural subject + uppercase ARE + single collective assertion), not a specific lexical phrase. Dropping the definite article ("Flag column headers ARE..." vs. "the flag column headers ARE...") preserves all structural properties. The "e.g." in C-33's definition confirms the example phrase is not exhaustively required.

3. **Extended obligation set composability** — A five-row obligation table satisfies C-24 ("structured table with exactly one row per obligation category") when five categories are present. The dual-surface prohibition architecture composes cleanly with extended sets: schema alignment (C-25) covers all five flag columns; the YOU MUST NOT block covers only the three substituted canonical tokens; the two surfaces are independent and do not require synchronization with new-category terms.

---

```json
{"top_score": 222, "all_essential_pass": true, "new_patterns": ["per-substitution enumeration boundary: C-34 applies only to substituted canonical tokens — new terms with no canonical equivalent and kept canonical terms are correctly excluded from YOU MUST NOT block; prohibition surface is self-contained when it covers exactly the replaced tokens", "reduced-phrase ARE satisfies C-33: any plural-subject collective ARE construction satisfies C-33 regardless of definite article or positional qualifier in the subject — structural form (plural subject + uppercase ARE + single collective assertion) is the criterion, not the lexical subject phrase"]}
```
