Now I have all five variants completely read. Let me score each one.

---

## campaign-blueprint — Quest Scorecard R9

**Rubric version:** v9 | **Ceiling:** 178 | **Date:** 2026-03-17

---

### Pre-Scoring Analysis

All five R9 variants preserve the full V-01 (R8) structural core. The axis differences are:

| Variant | Change vs base |
|---------|---------------|
| V-01 | Conversational imperative register throughout |
| V-02 | TRACEABILITY AUDIT sub-field added to REFLECTION |
| V-03 | "Conviction type met" column added to CLOSE |
| V-04 | Both V-02 + V-03 additions |
| V-05 | Maximum prose compression to skeleton |

Critical question before scoring: does the V-01 register shift or the V-05 compression affect any load-bearing structural criteria?

**C-18 (Double-prohibition FINDINGS placement — explicit "not before" AND "not during"):**

| Variant | REFLECTION preamble | C-18 verdict |
|---------|---------------------|-------------|
| V-01 (R9) | "This phase opens only after the pitch file is on disk. Everything here looks backward at completed work." | NO CREDIT — "not during" absent |
| V-02 | "...not before pitch production begins, not during pitch production." | FULL |
| V-03 | "...not before pitch production begins, not during pitch production." | FULL |
| V-04 | "...not before pitch production begins, not during pitch production." | FULL |
| V-05 | "After pitch file exists on disk only." | NO CREDIT — "not during" absent |

**C-19 (Structural double-prohibition as named phase boundary):**
C-19 requires the *double* prohibition to be encoded as a phase boundary condition. Without the double prohibition, C-19 cannot be earned. V-01 (R9) and V-05 lose both C-18 and C-19.

**C-28 (Active fill directive):**
All five variants carry the active directive form in REQUIREMENTS:

| Variant | C-28 form |
|---------|-----------|
| V-01 (R9) | "...go to the SCOUT TRACEABILITY TABLE in CAMPAIGN SETUP above and fill in its Req-ID and Must-have entry before continuing." |
| V-02–V-04 | "As you write each Must-have, complete its Req-ID and Must-have entry in the SCOUT TRACEABILITY TABLE in CAMPAIGN SETUP above." |
| V-05 | "As you write each Must-have, complete its Req-ID and Must-have entry in the SCOUT TRACEABILITY TABLE in CAMPAIGN SETUP above." |

All five: C-28 FULL.

---

### V-01 — Register: Conversational Imperative

**Axis:** Phrasing register only — all structural invariants claimed to survive

| Band | Criterion | Verdict | Evidence |
|------|-----------|---------|---------|
| Essential | C-01 All three artifacts | PASS | SPEC / PROPOSAL / PITCH all instructed |
| Essential | C-02 Canonical paths | PASS | All three `simulations/draft/.../{date}.md` paths present |
| Essential | C-03 Topic identity consistency | PASS | `{topic}` placeholder consistent throughout |
| Essential | C-04 Execution order | PASS | SPEC→PROPOSAL→PITCH with GATE at each transition |
| Essential | C-05 Minimum structure | PASS | All five sections per artifact present |
| Recommended | C-06 Proposal respects spec | PASS | "Do not reopen anything the spec settled" |
| Recommended | C-07 Pitch crystallizes option | PASS | "crystallize it, do not revisit" |
| Recommended | C-08 Campaign framing | PASS | CAMPAIGN SETUP opens; CAMPAIGN CLOSE closes |
| Aspirational | C-09 Narrative arc | PASS | Factual→Optionality→Emotional sequence maintained |
| Aspirational | C-10 Scout signal pull visible | PASS | Per-artifact READ fields name scout namespaces |
| Aspirational | C-11 Hard GATE per transition | PASS | Both GATE instructions present verbatim |
| Aspirational | C-12 Proactive scout inventory | PASS | "Do this unconditionally — do not skip it" |
| Aspirational | C-13 Conviction audit | PASS | CONVICTION DELTA + NEAR-DUPLICATE CONTENT both present |
| Aspirational | C-14 Signal consumption log | PASS | "Scout signal consumed" column in CLOSE |
| Aspirational | C-15 Artifact contract | PASS | READ/WRITE/PRESERVE/CARRIES FORWARD at matrix and per-site |
| Aspirational | C-16 Post-execution FINDINGS | PASS | CAMPAIGN REFLECTION labeled with FINDINGS block |
| Aspirational | C-17 Dual-mechanism defense | PASS | Contract matrix + FINDINGS template both present |
| Aspirational | **C-18 Double-prohibition placement** | **FAIL** | "This phase opens only after the pitch file is on disk" — "not during" absent; only single prohibition present |
| Aspirational | **C-19 Structural double-prohibition** | **FAIL** | No double prohibition to encode as phase boundary; "only after" is single-prohibition gate |
| Aspirational | C-20 Contract proximity anchoring | PASS | Per-artifact inline reminders restate READ and PRESERVE |
| Aspirational | C-21 Conviction typing | PASS | CONVICTION TYPE label at each site; REFLECTION typed |
| Aspirational | C-22 Per-site conviction type restatement | PASS | READ + PRESERVE + CONVICTION TYPE at each artifact |
| Aspirational | C-23 Inertia-anchored conviction arc | PASS | Bracket notation `[INERTIA MODEL Cost → factual record]` at all per-site reminders |
| Aspirational | C-24 Scout-to-must-have traceability | PASS | "Pull scout-requirements if you found one" instruction present |
| Aspirational | C-25 Scout traceability table | PASS | Four-column table present |
| Aspirational | C-26 Named INERTIA MODEL entity | PASS | Three-field declaration with bulleted field-to-conviction-type mapping |
| Aspirational | C-27 Table in CAMPAIGN SETUP | PASS | Table pre-populated in SETUP; REQUIREMENTS back-references "SCOUT TRACEABILITY TABLE in CAMPAIGN SETUP above" |
| Aspirational | C-28 Active fill directive | PASS | "go to the SCOUT TRACEABILITY TABLE...and fill in its Req-ID and Must-have entry before continuing" |

**Deductions:** C-18 (−5) + C-19 (−5) = −10

**Score: 168 / 178**

**Finding:** The conversational register compression stripped the "not before pitch production begins, not during pitch production" double-prohibition to "only after the pitch file is on disk" — losing C-18 and C-19. Register change was NOT structurally neutral for these two criteria. The hypothesis fails.

---

### V-02 — REFLECTION: Traceability Audit Sub-field

**Axis:** TRACEABILITY AUDIT added to REFLECTION, closing the SETUP→REQUIREMENTS→REFLECTION loop

| Band | Criterion | Verdict | Evidence |
|------|-----------|---------|---------|
| Essential | C-01 to C-05 | PASS all | All three artifacts, canonical paths, identity, order, structure |
| Recommended | C-06 to C-08 | PASS all | Proposal constraint, pitch crystallization, campaign framing |
| Aspirational | C-09 to C-17 | PASS all | Narrative arc, scout pull, gates, inventory, audit, contract, FINDINGS, dual-mechanism |
| Aspirational | **C-18 Double-prohibition** | **PASS** | "...not before pitch production begins, not during pitch production" — both explicit |
| Aspirational | **C-19 Structural double-prohibition** | **PASS** | Encoded as phase boundary: "This phase begins only after the pitch file exists on disk — not before production begins, not during production" |
| Aspirational | C-20 to C-22 | PASS all | Proximity anchoring, conviction typing, per-site restatement |
| Aspirational | C-23 Bracket notation | PASS | `[INERTIA MODEL Cost → factual record]` at all sites |
| Aspirational | C-24 to C-25 | PASS | Scout citations instruction + four-column table |
| Aspirational | C-26 Named entity | PASS | Bulleted three-field mapping |
| Aspirational | C-27 Table in SETUP | PASS | Pre-populated in SETUP + REQUIREMENTS back-reference |
| Aspirational | C-28 Active directive | PASS | "complete its Req-ID and Must-have entry in the SCOUT TRACEABILITY TABLE" |

**Deductions:** None.

**Score: 178 / 178**

**New structural element (not scored under v9):**
TRACEABILITY AUDIT in REFLECTION: "Return to the SCOUT TRACEABILITY TABLE in CAMPAIGN SETUP. For each row: Name the REQUIREMENTS Must-have (by Req-ID). Confirm the Must-have appears in the written spec as a distinct bulleted item. If any row has no corresponding Must-have, name the gap. State which namespace could close it." — This closes the loop C-27 (pre-populate) → C-28 (active fill) → REFLECTION (per-row audit). **Candidate C-29.**

---

### V-03 — CLOSE: Conviction Quality Column

**Axis:** "Conviction type met" column added to CAMPAIGN CLOSE

| Band | Criterion | Verdict | Evidence |
|------|-----------|---------|---------|
| Essential | C-01 to C-05 | PASS all | All artifacts, paths, identity, order, structure |
| Recommended | C-06 to C-08 | PASS all | Proposal constraint, pitch crystallization, campaign framing |
| Aspirational | C-09 to C-17 | PASS all | Standard V-01 R8 base preserved |
| Aspirational | C-18 Double-prohibition | PASS | "not before pitch production begins, not during pitch production" |
| Aspirational | C-19 Structural | PASS | Phase boundary form preserved |
| Aspirational | C-20 to C-22 | PASS all | Proximity, conviction typing, per-site restatement |
| Aspirational | C-23 Bracket notation | PASS | `[INERTIA MODEL Cost → factual record]` |
| Aspirational | C-24 to C-25 | PASS | Scout citations + table |
| Aspirational | C-26 Named entity | PASS | Bulleted three-field mapping |
| Aspirational | C-27 Table in SETUP | PASS | Pre-populated + back-reference |
| Aspirational | C-28 Active directive | PASS | "complete its Req-ID and Must-have entry" active directive |

**Deductions:** None.

**Score: 178 / 178**

**New structural element (not scored under v9):**
CLOSE conviction quality column: instruction + `Y / partial / N` column assessing whether each artifact's dominant register matches its declared conviction type. Factual conviction met for spec? Optionality for proposal? Emotional for pitch? — Makes conviction type declarations into verifiable artifacts at campaign close. **Candidate C-30.**

---

### V-04 — Combination: Traceability Audit + Conviction Quality

**Axis:** V-02 TRACEABILITY AUDIT + V-03 conviction quality column combined

| Band | Criterion | Verdict | Evidence |
|------|-----------|---------|---------|
| Essential | C-01 to C-05 | PASS all | Full artifact set, canonical paths, consistency, order, structure |
| Recommended | C-06 to C-08 | PASS all | Constraint, crystallization, campaign framing |
| Aspirational | C-09 to C-17 | PASS all | Full base preserved |
| Aspirational | C-18 Double-prohibition | PASS | "not before production begins, not during production" |
| Aspirational | C-19 Structural | PASS | Phase boundary form |
| Aspirational | C-20 to C-22 | PASS all | Proximity, typing, restatement |
| Aspirational | C-23 Bracket notation | PASS | `[INERTIA MODEL Cost → factual record]` at all sites |
| Aspirational | C-24 to C-25 | PASS | Scout citations + table |
| Aspirational | C-26 Named entity | PASS | Bulleted three-field mapping |
| Aspirational | C-27 Table in SETUP | PASS | Pre-populated + REQUIREMENTS back-reference |
| Aspirational | C-28 Active directive | PASS | "complete its Req-ID and Must-have entry" |

**Deductions:** None.

**Score: 178 / 178**

**New structural elements (not scored under v9):**
Full traceability-conviction accountability loop: SETUP table pre-populate (C-27) → REQUIREMENTS active fill (C-28) → REFLECTION per-row audit (C-29 candidate) → CLOSE conviction quality gate (C-30 candidate). First variant to close all four lifecycle stages simultaneously. Highest-potential form for v10.

---

### V-05 — Minimum-Density Path to 178

**Axis:** Maximum prose compression, all four structural invariants (C-23, C-26, C-27, C-28) preserved by design

| Band | Criterion | Verdict | Evidence |
|------|-----------|---------|---------|
| Essential | C-01 to C-05 | PASS all | All artifacts, paths, identity, order, structure — compression didn't touch these |
| Recommended | C-06 to C-08 | PASS all | Constraint, crystallization, framing |
| Aspirational | C-09 to C-17 | PASS all | All standard criteria survive compression |
| Aspirational | **C-18 Double-prohibition** | **FAIL** | "After pitch file exists on disk only." — "not during" absent; single-prohibition gate only |
| Aspirational | **C-19 Structural double-prohibition** | **FAIL** | No double prohibition to encode as phase boundary |
| Aspirational | C-20 to C-22 | PASS all | Proximity anchoring, conviction typing, per-site restatement all survive |
| Aspirational | C-23 Bracket notation | PASS | `[INERTIA MODEL Cost → factual record]` — retained word-for-word per hypothesis |
| Aspirational | C-24 to C-25 | PASS | Scout citations + table |
| Aspirational | C-26 Named entity | PASS | Bulleted three-field mapping retained |
| Aspirational | C-27 Table in SETUP | PASS | Pre-populated + back-reference |
| Aspirational | C-28 Active directive | PASS | "complete its Req-ID and Must-have entry in the SCOUT TRACEABILITY TABLE in CAMPAIGN SETUP above" — retained verbatim |

**Deductions:** C-18 (−5) + C-19 (−5) = −10

**Score: 168 / 178**

**Finding:** V-05's hypothesis missed C-18 and C-19. The "skeleton floor" was identified as C-23/C-26/C-27/C-28, but the actual load-bearing content for C-18 is "...not before pitch production begins, not during pitch production" and for C-19 is the structural encoding of that double prohibition as a named boundary condition. These were stripped as "non-load-bearing prose." The true minimum-density path to 178 must retain the double-prohibition sentence verbatim.

---

### R9 Summary Table

| Variant | Essential | Recommended | Aspirational | Total | vs Ceiling |
|---------|-----------|-------------|-------------|-------|-----------|
| V-01 — Register: Conversational imperative | 60 | 30 | 78 (−C-18,C-19) | **168** | −10 |
| V-02 — REFLECTION: Traceability audit | 60 | 30 | 88 | **178** | ceiling |
| V-03 — CLOSE: Conviction quality column | 60 | 30 | 88 | **178** | ceiling |
| V-04 — Combination: Audit + quality | 60 | 30 | 88 | **178** | ceiling |
| V-05 — Minimum-density path | 60 | 30 | 78 (−C-18,C-19) | **168** | −10 |

**Ranking:** V-02 = V-03 = V-04 (178) > V-01 = V-05 (168)

**All essential pass:** YES

---

### Excellence Signals

**From V-02/V-03/V-04 (tied ceiling holders):**

1. **Preservation of C-18/C-19 double-prohibition language is not register-neutral.** The phrase "not before pitch production begins, not during pitch production" is load-bearing verbatim. Neither "only after" nor "after pitch file exists on disk only" is structurally equivalent. This sentence is the minimum required unit for C-18/C-19 and must survive any register shift or compression pass.

2. **REFLECTION TRACEABILITY AUDIT closes the C-27/C-28 loop.** The three-stage lifecycle — (1) table pre-populated in SETUP (C-27), (2) cells filled actively during REQUIREMENTS (C-28), (3) per-row Must-have coverage verified in REFLECTION (V-02 addition) — is structurally distinct from C-25 (table form), C-27 (placement), and C-28 (writing behavior). The audit detects gaps that the directive alone cannot: a Must-have could be written without corresponding to a table row even under C-28 enforcement. Candidate **C-29**.

3. **CLOSE conviction quality self-assessment makes declared conviction types verifiable.** The `Y / partial / N` column in CAMPAIGN CLOSE (V-03 addition) converts each artifact's conviction type declaration from a structural label into a completed assessment artifact. Factual conviction for the spec is not asserted by naming it — it is confirmed by the CLOSE review. Candidate **C-30**.

4. **V-04's full accountability loop is the R9 ceiling architecture.** SETUP pre-populate → REQUIREMENTS active fill → REFLECTION per-row audit → CLOSE conviction gate: all four lifecycle stages are structurally closed. This is the highest-potential v10 form.

**Diagnostic finding for v10:**

**D10 (C-18 is not register-neutral):** The double-prohibition sentence for CAMPAIGN REFLECTION ("not before pitch production begins, not during pitch production") must appear verbatim or with equivalent dual-clause form. "Only after" is a single-prohibition gate that satisfies neither C-18 nor C-19. Any prompt rewrite (register shift, compression, reformulation) must preserve both the "not before" and "not during" clauses explicitly.

---

```json
{"top_score": 178, "all_essential_pass": true, "new_patterns": ["REFLECTION TRACEABILITY AUDIT closes the C-27/C-28 loop — per-row Must-have coverage audit in REFLECTION is structurally distinct from table pre-population and active fill; candidate C-29", "CLOSE conviction quality self-assessment: Conviction type met column makes declared conviction types into verified artifacts at campaign close; candidate C-30", "C-18/C-19 double-prohibition language is load-bearing verbatim — the not-before/not-during dual clause survives neither register shift nor compression; candidate diagnostic rule D10"]}
```
