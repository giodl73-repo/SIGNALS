## flow-throttle Round 17 — Scoring Report

**Rubric:** v17 (C-01–C-44) | **Max composite:** 270 | **Variations:** V-01 through V-05

---

### Scoring Basis

C-01 through C-41 carry over from the R16 baseline (all PASS per the state analysis in the variation document). Scoring focus is on the three new criteria: **C-42**, **C-43**, **C-44**. Each is worth 5 pts. All five essential criteria are architectural pass conditions already met.

---

## V-01 — Lifecycle emphasis (single-axis)

**Hypothesis:** Two-row milestone SIGNAL CHECKPOINT satisfies C-43 without Role 1.5; bypass-failure prohibition satisfies C-44.

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-01–C-41 | PASS | Identical to R16 baseline architecture |
| **C-42** | **PASS** | Field 5 names both signals at Milestone 1 / Milestone 2 and closes with "Gate compliance is verified by evidence in the checkpoint, not inferred from body quality." Both CHECKPOINT STATUS fields cited as required evidence |
| **C-43** | **PASS** | Two-row milestone table separates Signal 1 ("Confirms: Sections A, B, C structurally present") from Signal 2 ("count verification"). Signal distinction prose paragraph names non-overlap explicitly: "a Section C with 6 of 7 annotations satisfies Signal 1 while failing Signal 2. Conflating the two signals converts the count check into an unverified assertion." Two milestone rows are structurally distinct table entries |
| **C-44** | **PASS** | "Bypass-failure prohibition" is a named section. Bypass is labeled: "The 'looks complete' bypass failure mode: FORMAT CONTRACT COMPLETE has been stated and the analysis tables are scaffolded, so Role 2 appears ready to activate." Structural proof: "FORMAT CONTRACT COMPLETE is a section-presence signal only — it does not verify that the annotation inventory is complete to its declared count." Executor SHALL complete both milestones before Role 2 opens |

**Composite: 270/270**

---

## V-02 — Output format (single-axis)

**Hypothesis:** Signal distinction table with "Does NOT confirm" column satisfies C-43; bypass-attempt rejection table satisfies C-44.

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-01–C-41 | PASS | Identical to R16 baseline |
| **C-42** | **PASS** | Field 5 is a 4-row verification table. Row 4: "SIG-02 confirmed before Step 1A — cite Table 3 Verdict = PROCEED." Final clause: "Gate compliance is verified by evidence in the body, not inferred from output quality." Each row requires citation of body evidence |
| **C-43** | **PASS** | Table 1 (Signal distinction register): SIG-01 row reads "Confirms: Sections A, B, C are structurally present / Does NOT confirm: That Section C annotation count = declared count of 7"; SIG-02 row reads "Confirms: Section C count = 7." Non-conflation statement: "An executor SHALL NOT treat SIG-01 as evidence that SIG-02 is satisfied. 'Sections present' (SIG-01) and 'count verified' (SIG-02) are non-overlapping guarantees confirmed by distinct mechanisms." Column-readable distinction — strongest structural form for C-43 |
| **C-44** | **PASS** | Table 2 (Bypass-attempt rejection register): row has Bypass attempt = "Proceed to Role 2 after FORMAT CONTRACT COMPLETE without completing Table 3 count check"; Attempt type = "Looks complete — SIG-01 stated, tables scaffolded"; Structural reason = full proof that SIG-01 is section-presence only and a 6-of-7 Section C would pass SIG-01 while failing SIG-02. Bypass is a typed, named, scannable table row |

**Composite: 270/270**

---

## V-03 — Role sequence (single-axis)

**Hypothesis:** Role 1.5 (INVENTORY VERIFIER) as a separate role makes the two-signal chain architecturally visible; C-44 inertia-frame rejection opens Role 1.5.

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-01–C-41 | PASS | Identical to R16 baseline |
| **C-42** | **PASS** | Field 5: "The activation condition for Role 2 is INVENTORY VERIFIED — not FORMAT CONTRACT COMPLETE. The presence of FORMAT CONTRACT COMPLETE in Role 1 does not satisfy this field; only the Role 1.5 HANDOFF SIGNAL = INVENTORY VERIFIED record satisfies the Phase 1 activation requirement." Three FAIL modes enumerated: (a) field absent, (b) reads INVENTORY INCOMPLETE, (c) Step 1A opened without the handoff signal before it. Evidence from structural record, not body quality |
| **C-43** | **PASS** | "Signal distinction — why Role 1.5 exists as a separate role" paragraph: "FORMAT CONTRACT COMPLETE (Role 1 handoff) confirms that Sections A, B, and C are structurally present — it is a section-presence signal. INVENTORY VERIFIED (Role 1.5 handoff) confirms that Section C row count equals the declared count of 7 — it is a count-completeness signal. These are distinct guarantees produced by distinct roles." Architectural separation is the mechanism — the two-signal chain is visible in the role hierarchy |
| **C-44** | **PASS** | "Inertia-frame rejection — the 'looks complete' bypass failure mode": names the bypass ("FORMAT CONTRACT COMPLETE has been stated and the analysis tables are scaffolded, so Role 2 appears ready to activate. This framing is self-defeating."); delivers structural proof; includes C-26 parallel: "just as Step 1B cannot be deferred because Step 2G is structurally dependent on Load-shape verdicts that only Step 1B produces, Role 2 cannot bypass Role 1.5 because Role 2's annotation contract depends on a count-verified inventory that only Role 1.5 certifies" |

**Composite: 270/270**

---

## V-04 — Phrasing register + Lifecycle emphasis

**Hypothesis:** Maximum SHALL/SHALL NOT density at a named TWO-SIGNAL MANDATORY GATEWAY with numbered steps G-1 through G-4 satisfies all three new criteria.

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-01–C-41 | PASS | Identical to R16 baseline |
| **C-42** | **PASS** | Field 5 specifies four gateway steps G-1 through G-4 with SHALL-verify per step. Lead clause: "An executor SHALL NOT infer gateway compliance from body quality — explicit records from the gateway steps are required." Requires citing step-specific records: G-1 Signal 1 record, G-2 Actual count, G-3 Signal 2 record, G-4 GATEWAY STATUS field. PASS requires all four; FAIL cites the specific step where record is absent |
| **C-43** | **PASS** | "Signal non-conflation requirement" has two numbered normative obligations: "1. Signal 1 — FORMAT CONTRACT COMPLETE: ...section-presence confirmation. An executor SHALL NOT treat Signal 1 as evidence that Section C annotation count equals the declared count of 7. 2. Signal 2 — INVENTORY VERIFIED: ...count-completeness confirmation. An executor SHALL NOT activate Role 2 until Signal 2 is produced." Each signal is its own numbered SHALL-NOT-conflate obligation — conflation is a named normative violation category |
| **C-44** | **PASS** | "PROHIBITED — bypass via 'looks complete' framing" section with SHALL NOT at every decision branch: "An executor encountering FORMAT CONTRACT COMPLETE (Signal 1) SHALL NOT proceed directly to Role 2 on the basis that the prompt appears complete or that the analysis scaffolding is in place." Structural proof: "Signal 1 is a section-presence signal; it does NOT guarantee Signal 2. A Section C with 6 of 7 annotations stated FORMAT CONTRACT COMPLETE while Signal 2 would be withheld." SHA-NOT language converts bypass into named normative breach |

**Composite: 270/270**

---

## V-05 — Role sequence + Output format + Inertia framing (three-axis)

**Hypothesis:** Three combined axes produce the most reinforced C-42/C-43/C-44 coverage.

| Criterion | Verdict | Evidence note |
|-----------|---------|---------------|
| C-01–C-41 | PASS | Identical to R16 baseline, plus STEP 1A/1B GATE TABLEs as structured tables |
| **C-42** | **PASS** | Audit F-5 row: "Role 1.5 HANDOFF SIGNAL = INVENTORY VERIFIED (SIG-02) explicitly recorded before Step 1A; SIG-01 (FORMAT CONTRACT COMPLETE) and SIG-02 (INVENTORY VERIFIED) appear as structurally distinct entries — SIG-01 in Role 1, SIG-02 in Role 1.5; gate compliance verified by these records, not inferred from body quality." Both signals named with source roles — most explicit form of C-42 |
| **C-43** | **PASS** | Two structural forms simultaneously: (1) Role activation chain table at prompt header — SIG-01 and SIG-02 appear as separate cells in the Handoff signal column; the chain is scannable before any role begins. (2) Signal distinction table inside Role 1.5 with SIG-01/SIG-02 rows and "Does NOT confirm" column. Non-conflation statement: "An executor SHALL NOT treat the presence of SIG-01 as evidence that SIG-02 is satisfied." |
| **C-44** | **PASS** | Three reinforcing mechanisms: (1) Named failure mode "Looks complete / just start" with structural proof and C-26 parallel; (2) "Inertia-frame rejection field": "An executor SHALL fill this field before proceeding to the verification table: [ BYPASS ATTEMPT IDENTIFIED AND REJECTED / NO BYPASS ATTEMPT DETECTED ]" — field must be filled as structural prerequisite; (3) Field placement before the verification table forces bypass rejection processing before count verification can begin |

**Composite: 270/270**

---

## Ranking

All five variations achieve 270/270, closing all R16 gaps. Ranked by structural depth for C-43 + C-44:

| Rank | Variation | C-43 form | C-44 form |
|------|-----------|-----------|-----------|
| 1 | **V-05** | Chain table + distinction table (two simultaneous forms) | Named failure mode + structural proof + required fill field (structural prerequisite) |
| 2 | V-02 | "Does NOT confirm" column makes signal limitation column-readable | Bypass-attempt rejection register as typed, auditable table row |
| 3 | V-03 | Role 1.5 architectural separation — distinction visible in role hierarchy | C-26 parallel proof; bypass named before any verification content |
| 4 | V-04 | SHALL-NOT-conflate as numbered normative obligations | PROHIBITED bypass with SHALL NOT at every decision branch |
| 5 | V-01 | Two-row milestone table — per-signal row, Confirms column | Bypass-failure prohibition section with structural proof |

---

## Excellence Signals

Patterns from V-05 (top) and from the R17 variation set that are new relative to R16:

**1. Role activation chain table at prompt header (V-05)**
Placing all four roles in a named table with Activation signal and Handoff signal columns — before any role content — makes the full two-signal chain (FORMAT CONTRACT COMPLETE → INVENTORY VERIFIED) visible in a single structure. An executor can verify the chain requirement from the header table alone. A missing signal in the chain is a visible table gap, not a prose absence.

**2. Inertia-frame rejection field as structural prerequisite before verification table (V-05)**
Placing a fill field ("SHALL fill before proceeding to the verification table") between the inertia-frame rejection prose and the verification table converts bypass rejection from a reading obligation into a gating requirement. Parallel enforcement structure to the Step 1B gate: bypass the field, the verification table is entered with a visible unfilled precondition.

**3. Bypass-attempt rejection register as typed table (V-02)**
Encoding the "looks complete" bypass as a named row in a structured register (columns: Bypass attempt / Attempt type / Structural reason for rejection) makes the bypass an auditable, scannable record rather than an embedded prose argument. The typed Attempt type = "Looks complete" column makes the failure mode a category, not an example.

**4. SHALL-NOT-conflate as numbered normative obligations (V-04)**
Each signal in its own numbered normative step with SHALL NOT conflate language transforms non-conflation from a structural hint into a citable normative breach. Conflation is now a violation of a specific numbered obligation, not a design intent that must be inferred.

**5. Two-row milestone table with per-signal Confirms column (V-01)**
Representing each signal as a table row with "Confirms" as a column value makes section-presence vs. count-completeness machine-scannable at row granularity — a row-count scan confirms two signals exist; a column-scan reveals the distinct guarantee each provides.

---

## Summary Table

| Variation | C-42 | C-43 | C-44 | Composite | Golden threshold |
|-----------|------|------|------|-----------|-----------------|
| V-01 | PASS | PASS | PASS | 270/270 | MET |
| V-02 | PASS | PASS | PASS | 270/270 | MET |
| V-03 | PASS | PASS | PASS | 270/270 | MET |
| V-04 | PASS | PASS | PASS | 270/270 | MET |
| V-05 | PASS | PASS | PASS | 270/270 | MET |

All five variations meet golden threshold (all essential PASS + composite 270/270). R17 objective achieved: 0 of 5 variations remain below 270/270 (vs. 4 of 5 under R16 baseline).

```json
{"top_score": 270, "all_essential_pass": true, "new_patterns": ["Role activation chain table at prompt header makes both handoff signals scannable as table cells before any role begins — a missing signal is a visible table gap", "Inertia-frame rejection field placed before verification table as a structural prerequisite converts bypass rejection from reading obligation to gating requirement parallel to Step 1B gate", "Bypass-attempt rejection register as typed table with Attempt type and Structural reason columns makes the looks-complete bypass an auditable named row rather than embedded prose"]}
```
