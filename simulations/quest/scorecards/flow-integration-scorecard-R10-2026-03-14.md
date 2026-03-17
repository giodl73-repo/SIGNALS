Now I have everything needed. Let me score all five variations.

---

# flow-integration — Round 10 Scorecard (v10 rubric, 202 pt ceiling)

## Scoring Notes

**Point allocation:**
- C-01–C-04: 15 each (60 essential)
- C-05–C-07: 10 each (30 recommended)
- C-08–C-09: 5 each; C-10–C-14: 4 each; C-15: 3; C-16–C-17: 7 each; C-18–C-30: 5 each (112 aspirational)

---

## V-01 — C-30 Table-Reference Shorthand (Q1 Probe)

Non-standard terms: footprint-call / implicit-pass / ghost-system / relay-chain. Uppercase ARE. Single YOU MUST NOT block referencing obligation table by role without enumerating canonical tokens.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Call inventory | PASS | ≥2-row template, call types explicit, confidence column present |
| C-02 Auth documentation | PASS | N.1 AUTHENTICATION section per call with 5 labeled fields |
| C-03 Request/response format | PASS | N.2 REQUEST AND RESPONSE FORMAT section, separate labeled, 5 fields |
| C-04 Error propagation | PASS | N.5 ERROR PROPAGATION section per call with 3 labeled fields |
| C-05 Rate limit exposure | PASS | N.3 RATE LIMITS with Limit value, Burst risk, Throttle response |
| C-06 Retry/idempotency | PASS | N.4 RETRY AND IDEMPOTENCY section, 3 fields including Mitigation |
| C-07 Gap inventory | PASS | Stage 3 table with Call ID, Gap Type, Severity, Rationale, Remediation columns |
| C-08 Severity ranking | PASS | Severity column + "MEDIUM and LOW findings not exempt" instruction |
| C-09 Remediation sketch | PASS | Remediation column + "HIGH findings require call-specific sketch" instruction |
| C-10 Inventory-first gate | PASS | "Populate this table before opening Stage 2" — inventory precedes all analysis |
| C-11 Single-concern phase isolation | PASS | Each N.x section labeled with one concern |
| C-12 Gate-enforced per-call completion | PASS | "Do not open CALL-[N+1] until CALL-[N] COMPLETION GATE is fully checked" |
| C-13 Per-call section-level concern exclusion | PASS | Each section carries exclusion parenthetical naming all other concerns |
| C-14 Five-concern checklist | PASS | Exactly 5-item completion gate per call block |
| C-15 Late-call inventory discipline | PASS | NEW-CALL RULE explicit instruction present |
| C-16 Expert persona declaration | PASS | Named domain + discovery obligations declared before inventory gate |
| C-17 In-block rate limit completeness | PASS | Three separate labeled fields in N.3 inside each call block |
| C-18 Cross-stage secondary positioning | PASS | Aggregation Rule names all three demotion properties explicitly |
| C-19 Four-obligation scope | PASS | Four-row table covers forgotten calls, assumed-to-work, unknown-system, delegation chain |
| C-20 Unconditional cross-stage stage | PASS | Coda fires unconditionally; explicit "no structures" default present |
| C-21 Inventory flag alignment | PASS | Inventory has 4 flag columns corresponding to 4 obligation categories |
| C-22 C-19/C-21 vocabulary unification | PASS | [footprint-call][implicit-pass][ghost-system][relay-chain] match obligation table row terms exactly |
| C-23 Unnumbered coda | PASS | Coda carries no number, appended after Stage 3, no displacement |
| C-24 Four-obligation table schema | PASS | Structured 4-row table, each row one obligation, before inventory gate |
| C-25 Schema-aligned C-22 enforcement | PASS | Inventory flag column headers = obligation table row terms by schema comparison |
| C-26 Schema-only C-25 enforcement | PASS | Explicit schema instruction with uppercase ARE; no VOCABULARY RULE block required |
| **C-27 Dual-surface prohibition** | **FAIL** | YOU MUST NOT block reads "canonical Obligation Term values listed in the obligation table above" — single block placement satisfied, but block delegates enumeration to the table rather than naming forgotten-call, assumed-to-work, unknown-system, delegation-chain inline; C-27 requires "names the specific canonical tokens that are forbidden"; indirect reference via table role does not meet the inline naming requirement — conservative ruling: FAIL |
| C-28 Explicit terminal-position formula | PASS | Header `*(no stage number — appended after Stage 3, the last numbered stage)*` + prose "It does not appear between any two numbered stages; it does not displace or renumber any existing element" |
| C-29 ARE directive requirement | PASS | Uppercase ARE present in assertive schema instruction — not the Q1 axis |
| **C-30 Single-block comprehensive prohibition** | **FAIL** | Requires C-27; C-27 FAIL → C-30 FAIL |

**V-01 score: 202 − 5 (C-27) − 5 (C-30) = 192/202**

**Q1 ruling (definitive):** Table-reference shorthand fails C-27/C-30. The prohibition block must enumerate the specific canonical tokens inline; delegating to the obligation table by role does not satisfy "names the specific canonical tokens."

---

## V-02 — C-29 Lowercase Non-Assertive ARE Form (Q2 Probe)

Canonical terms. Lowercase "are" in schema instruction. No non-standard substitution → C-27/C-30 N/A.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-07 | PASS | Same structure as V-01; all essential and recommended criteria present |
| C-08–C-17 | PASS | Same aspirational structure; all format and depth criteria met |
| C-18 | PASS | Aggregation Rule three-property demotion present |
| C-19 | PASS | Four-row obligation table with canonical terms |
| C-20 | PASS | Unconditional coda with no-structures default |
| C-21 | PASS | [forgotten-call][assumed-to-work][unknown-system][delegation-chain] flag columns |
| C-22 | PASS | Flag names match obligation row terms exactly (canonical-to-canonical) |
| C-23 | PASS | Unnumbered coda, no displacement |
| C-24 | PASS | Four-row structured obligation table |
| C-25 | PASS | Schema comparison verifies column header = row term identity |
| C-26 | PASS | Explicit schema instruction present; lowercase "are" still constitutes a schema instruction that aligns column headers to obligation terms; C-26 PASS pending C-29 determination |
| C-27 | PASS (N/A) | Canonical terms used — non-standard substitution did not occur; criterion trivially satisfied |
| C-28 | PASS | Full two-surface formula present in stage vocabulary |
| **C-29 ARE directive requirement** | **FAIL** | Schema instruction reads "The flag column headers in the Stage 1 inventory table **are** the Obligation Term column values above" — lowercase "are" in declarative construction, not uppercase ARE in assertive sentence; C-29 requires "explicit ARE directive of the form 'the flag column headers ARE the Obligation Term column values above'"; all confirmed PASS variations used uppercase ARE; lowercase non-assertive form does not satisfy the minimum — conservative ruling: FAIL |
| C-30 | PASS (N/A) | Requires C-27; C-27 trivially satisfied (no non-standard terms); C-30 trivially satisfied |

**V-02 score: 202 − 5 (C-29) = 197/202**

**Q2 ruling (definitive):** Lowercase "are" in a declarative sentence fails C-29. The explicit ARE directive requires the uppercase assertive form. The identity assertion ("headers ARE the values") is not equivalent to the declarative correspondence construction ("headers are the values") for purposes of C-29.

---

## V-03 — Inertia Framing Block (Structural Neutrality Probe)

Canonical terms. Uppercase ARE. Added DISCOVERY IMPERATIVE block between persona and inventory gate.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-07 | PASS | All essential and recommended present |
| C-08–C-17 | PASS | All aspirational format/depth criteria met |
| C-18 | PASS | Three-property aggregation demotion |
| C-19 | PASS | Four-row obligation table (forgotten-call, assumed-to-work, unknown-system, delegation-chain) |
| C-20 | PASS | Unconditional coda |
| C-21 | PASS | Four flag columns |
| C-22 | PASS | Vocabulary identity (canonical-to-canonical) |
| C-23 | PASS | Unnumbered coda |
| C-24 | PASS | Four-row table schema |
| C-25 | PASS | Schema comparison verification |
| C-26 | PASS | Uppercase ARE, no VOCABULARY RULE block |
| C-27 | PASS (N/A) | Canonical terms — no substitution |
| C-28 | PASS | Full two-surface formula in stage vocabulary |
| C-29 | PASS | Uppercase ARE assertive form |
| C-30 | PASS (N/A) | Canonical terms — trivially satisfied |

Note: DISCOVERY IMPERATIVE block explicitly maps four named failure modes (spec trust, assumed confidence, system opacity, delegation invisibility) to the four obligation categories. Structurally inert — adds no content conflicting with any criterion, does not alter gate sequencing or schema instructions.

**V-03 score: 202/202**

---

## V-04 — C-29 Lowercase + C-30 Table-Reference Shorthand (Q1+Q2 Joint Probe)

Non-standard terms: shadow-wire / assumed-clear / void-target / transfer-chain. Lowercase "are". Table-reference shorthand YOU MUST NOT block.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-07 | PASS | All essential and recommended present |
| C-08–C-17 | PASS | All aspirational format/depth criteria met |
| C-18 | PASS | Three-property aggregation demotion |
| C-19 | PASS | Four-row obligation table with non-standard terms |
| C-20 | PASS | Unconditional coda |
| C-21 | PASS | [shadow-wire][assumed-clear][void-target][transfer-chain] flag columns |
| C-22 | PASS | Non-standard terms in persona match flag column names exactly |
| C-23 | PASS | Unnumbered coda |
| C-24 | PASS | Four-row structured table |
| C-25 | PASS | Schema comparison: column headers = obligation table row terms |
| C-26 | PASS | Explicit schema instruction present (lowercase "are" is still a schema instruction; C-26 PASS; C-29 fails separately) |
| **C-27 Dual-surface prohibition** | **FAIL** | Same table-reference shorthand as V-01: "YOU MUST NOT use any of the canonical Obligation Term values listed in the obligation table above" — does not name forgotten-call, assumed-to-work, unknown-system, delegation-chain inline; Q1 ruling carries: inline enumeration required |
| C-28 | PASS | Full two-surface formula present |
| **C-29 ARE directive requirement** | **FAIL** | Lowercase "are" in declarative form; Q2 ruling carries: uppercase ARE required |
| **C-30 Single-block comprehensive prohibition** | **FAIL** | Requires C-27; C-27 FAIL → C-30 FAIL |

**V-04 score: 202 − 5 (C-27) − 5 (C-29) − 5 (C-30) = 187/202**

Joint probe confirms: Q1 and Q2 failures are independent — both fail simultaneously, scores accumulate additively.

---

## V-05 — Section Outer Frame (C-28 Section Formula Confirming)

Canonical terms. Uppercase ARE. Section 1/2/3 frame vocabulary. C-28 formula adapted to section vocabulary.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-07 | PASS | All essential and recommended present; Section frame carries same structural guarantees as Stage frame |
| C-08–C-17 | PASS | All aspirational format/depth criteria met |
| C-18 | PASS | Aggregation Rule names populated-from, not-authoritative, not-required in Section 2 block |
| C-19 | PASS | Four-row obligation table (forgotten-call, assumed-to-work, unknown-system, delegation-chain) |
| C-20 | PASS | Coda fires unconditionally; "No cross-section structures produced in this trace" default present |
| C-21 | PASS | Four flag columns |
| C-22 | PASS | Vocabulary identity (canonical-to-canonical) |
| C-23 | PASS | Unnumbered coda appended after Section 3, no number, no displacement |
| C-24 | PASS | Four-row structured obligation table |
| C-25 | PASS | Schema comparison: column headers = obligation table row terms |
| C-26 | PASS | "The flag column headers in the Section 1 inventory table ARE the Obligation Term column values above" — uppercase ARE, no VOCABULARY RULE block |
| C-27 | PASS (N/A) | Canonical terms — no substitution |
| C-28 | PASS | Header `*(no section number — appended after Section 3, the last numbered section)*` + prose "It does not appear between any two numbered sections; it does not displace or renumber any existing element" — full two-surface formula in section vocabulary |
| C-29 | PASS | Uppercase ARE in assertive schema instruction |
| C-30 | PASS (N/A) | Canonical terms — trivially satisfied |

**V-05 score: 202/202**

C-28 Section frame confirmed: the terminal-position formula is fully outer-frame-agnostic. Section vocabulary substitution produces identical structural guarantees. R9 V-04 contamination was exclusively from the open-question exposures (C-26/C-27/C-29), not from the Section frame itself.

---

## Composite Scores

| Variation | Score | Delta from 202 | Q1 (C-27/C-30) | Q2 (C-29) |
|-----------|-------|----------------|-----------------|-----------|
| V-01 | **192/202** | −10 | FAIL (table-ref shorthand) | PASS |
| V-02 | **197/202** | −5 | N/A (canonical) | FAIL (lowercase) |
| V-03 | **202/202** | 0 | N/A (canonical) | PASS |
| V-04 | **187/202** | −15 | FAIL + FAIL | FAIL (lowercase) |
| V-05 | **202/202** | 0 | N/A (canonical) | PASS |

**Ranking:** V-03 = V-05 (202) > V-02 (197) > V-01 (192) > V-04 (187)

---

## Open Question Verdicts from R10

**Q1 resolved — C-30 block composition (definitive).**
A single YOU MUST NOT block that references the obligation table by role ("canonical Obligation Term values listed in the obligation table above") without enumerating the specific canonical tokens inline does not satisfy C-27 or C-30. C-27's mechanism requires that the prohibited canonical tokens be named as specific tokens in the block. Delegation to the table by role creates a block that is single in placement but incomplete in surface — a reviewer must navigate to the obligation table to identify which tokens are forbidden, which recreates the per-row scanning problem that C-30 was designed to eliminate. V-01 and V-04 both fail. Conservative ruling confirmed. **C-30 codifies: inline enumeration of specific canonical tokens required; table-reference shorthand is insufficient.**

**Q2 resolved — C-29 ARE capitalisation and sentence form (definitive).**
Lowercase "are" in a declarative construction ("the flag column headers **are** the Obligation Term column values above") does not satisfy C-29. The ARE directive form is specifically an uppercase assertive construction that converts a correspondence description into an identity assertion; the lowercase declarative form describes the same relationship but does not achieve the structural identity constraint that ARE creates. V-02 and V-04 both fail. Conservative ruling confirmed. **C-29 codifies: uppercase ARE in an assertive sentence is the minimum form; lowercase declarative construction is insufficient.**

---

## Excellence Signals from Top-Scoring Variations (V-03, V-05)

**V-03 — Inertia framing block pattern:**
Adding a named DISCOVERY IMPERATIVE block between the persona declaration and the inventory gate — which names the specification as an incomplete artifact and maps four named failure modes (spec trust, assumed confidence, system opacity, delegation invisibility) to the four obligation categories — is structurally inert with respect to all rubric criteria while semantically strengthening the discovery mandate. The block does not alter gate sequencing, schema instructions, or any criterion surface. This is a zero-cost enrichment that anchors the persona's purpose relative to the primary discovery risk.

**V-05 — Section frame portability of C-28 formula:**
The explicit terminal-position formula (header annotation + prose sentence) is fully outer-frame-agnostic. Substituting "section" for "stage" throughout — including in the coda header, the coda prose, the inventory gate instruction, and the per-call analysis stage reference — produces a complete 202/202 trace without any Section-specific structural hazard. The R9 V-04 Section frame failures were caused entirely by the C-26/C-27/C-29 open-question axes, not by the Section vocabulary. C-28 formula portability is confirmed across stage and section frames.

---

## Open Questions Carried to R11

1. **C-29 minimum enumeration scope** — Q2 is settled for uppercase vs. lowercase. The new open question: does C-29 require the full canonical phrase "the flag column headers ARE the Obligation Term column values above — use those exact tokens as column headers" verbatim, or does any uppercase ARE in an assertive identity sentence satisfy the minimum (e.g., "The inventory flag headers ARE the obligation terms above")? The multi-clause form has been confirmed PASS; abbreviated assertive forms have not been tested.

2. **C-30 minimum enumeration form** — Q1 is settled for table-reference vs. explicit inline enumeration. The new open question: must the YOU MUST NOT block list the canonical tokens in exactly the form they appear as row terms in the obligation table (e.g., "forgotten-call, assumed-to-work, unknown-system, delegation-chain"), or does any explicit naming of the four tokens in the block satisfy the requirement (e.g., prose description that names each token)? R8 V-05 used exact row-term tokens inline and passed; this remains the only confirmed-PASS form.

---

```json
{"top_score": 202, "all_essential_pass": true, "new_patterns": ["inertia-framing-block: named DISCOVERY IMPERATIVE block maps four failure modes to four obligation categories, structurally inert relative to all criteria, placed between persona declaration and inventory gate", "section-frame-c28-portability: C-28 terminal-position formula is fully outer-frame-agnostic; section vocabulary substitution throughout produces 202/202; Section frame carries no structural hazard of its own"]}
```
