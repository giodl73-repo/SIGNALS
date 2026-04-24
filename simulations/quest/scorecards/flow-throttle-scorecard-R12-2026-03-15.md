Now I have everything I need. Let me produce the full scorecard.

---

## flow-throttle — Round 12 Score Report

**Rubric:** v12 | **Criteria:** C-01 through C-34 | **Max composite:** 220
**Scoring bands:** Essential C-01–C-05 = 12 pts each (60 total) | Recommended C-06–C-08 = 10 pts each (30 total) | Aspirational C-09–C-34 = 5 pts each (130 total)

---

### Baseline carry confirmation

C-01 through C-32 are confirmed PASS for all variations. All variations inherit the R11 V-05 baseline, which was verified to pass every criterion through C-32 under v11. The only live evaluation axes in R12 are **C-33** and **C-34** (both 5-pt aspirational, introduced in v12).

---

### V-01 — Inertia framing: C-33 FAIL isolation (R11 V-04 baseline carry)

| ID | Band | Result | Evidence |
|----|------|--------|----------|
| C-01 | Essential | **PASS** | Binding-tier causal reason present at Phase 1B exit; names specific causal mechanism |
| C-02 | Essential | **PASS** | TABLE B has ≥2 rows with T-NN identifiers and named mechanism from permitted set |
| C-03 | Essential | **PASS** | TABLE A has ≥2 rows with Component, Scope, specific numeric Limit |
| C-04 | Essential | **PASS** | TABLE C has one row per TABLE A Tier-ID; no tier omitted |
| C-05 | Essential | **PASS** | TABLE D satisfies gap-reason or ≥2 named controls requirement |
| C-06–C-08 | Recommended | **PASS** (×3) | Carried from baseline; no change in this axis |
| C-09–C-32 | Aspirational | **PASS** (×24) | Carried from R11 V-05; all constraints, registers, gates, annotations, and escape routes intact |
| **C-33** | Aspirational | **FAIL** | Header reads "Inertia annotation for C-27 — why the register must be declared closed (C-29, C-30):" — names criteria but declares neither field count nor field names; auditor must enter annotation body and criterion-match to locate the three fields; count-scan is impossible at header level |
| **C-34** | Aspirational | **FAIL** | Gate-present path label: "*Gate-present audit method:*" with "confirm five named observables in sequence" inside prose — count (five) is embedded in description, not at the italic path-identifier line; Gate-absent: "*Gate-absent signature:*" with "Named observable for the absent condition" — no "1 observable" count label; both paths have open-enumeration form |

**Composite: 60 + 30 + (24 × 5) = 60 + 30 + 120 = 210 / 220**
All essential: PASS | Golden: YES (210 ≥ 80, all essential pass)

---

### V-02 — Inertia framing: C-33 PASS (field-count header added, C-34 open)

| ID | Band | Result | Evidence |
|----|------|--------|----------|
| C-01–C-05 | Essential | **PASS** (×5) | Inherited; no change |
| C-06–C-08 | Recommended | **PASS** (×3) | Inherited |
| C-09–C-32 | Aspirational | **PASS** (×24) | Inherited |
| **C-33** | Aspirational | **PASS** | Header reads "Inertia annotation for C-27 — why the register must be declared closed — 3 fields: Failure mode prevented \| Gap above C-25 \| Concrete example (C-29, C-30):" — count "3" declared; three field names pipe-delimited on the header line; auditor counts three names against "3" without reading annotation body; count-scan is fully operational at header level |
| **C-34** | Aspirational | **FAIL** | TYPE SCAN GATE audit paths unchanged from V-01: gate-present path identifier does not declare count; "confirm five named observables in sequence" remains embedded in prose; no "5 observables" label on path identifier line; gate-absent path has no "1 observable" label |

**Composite: 60 + 30 + (25 × 5) = 60 + 30 + 125 = 215 / 220**
All essential: PASS | Golden: YES

---

### V-03 — Lifecycle emphasis: C-34 PASS (per-path count at label level, C-33 open)

| ID | Band | Result | Evidence |
|----|------|--------|----------|
| C-01–C-05 | Essential | **PASS** (×5) | Inherited |
| C-06–C-08 | Recommended | **PASS** (×3) | Inherited |
| C-09–C-32 | Aspirational | **PASS** (×24) | Inherited |
| **C-33** | Aspirational | **FAIL** | Header carries V-01 form: "Inertia annotation for C-27 — why the register must be declared closed (C-29, C-30):" — no field count, no field name enumeration; auditor must read body and criterion-match; count-scan not possible |
| **C-34** | Aspirational | **PASS** | Gate-present path identifier reads "*Gate-present audit method — 5 observables:*" followed by "Confirm the following 5 observables in sequence:" — count (5) is at the path-label line; auditor verifies five numbered items against declared "5" without entering description prose. Gate-absent identifier reads "*Gate-absent signature — 1 observable:*" followed by "Confirm the following 1 observable:" — the absent path is now a closed set of declared size 1. Both paths apply the C-27 closed-register pattern to observable enumeration |

**Composite: 60 + 30 + (25 × 5) = 60 + 30 + 125 = 215 / 220**
All essential: PASS | Golden: YES

---

### V-04 — Combined axes: C-33 + C-34, single-role form

| ID | Band | Result | Evidence |
|----|------|--------|----------|
| C-01–C-05 | Essential | **PASS** (×5) | Inherited |
| C-06–C-08 | Recommended | **PASS** (×3) | Inherited |
| C-09–C-32 | Aspirational | **PASS** (×24) | Inherited |
| **C-33** | Aspirational | **PASS** | Header: "Inertia annotation for C-27 — why the register must be declared closed — 3 fields: Failure mode prevented \| Gap above C-25 \| Concrete example (C-29, C-30):" — identical to V-02; count and field names declared at header; count-scan operational |
| **C-34** | Aspirational | **PASS** | Gate path identifiers: "*Gate-present audit method — 5 observables:*" and "*Gate-absent signature — 1 observable:*" — identical to V-03; both paths have count labels at the path-label line; observable sets are closed and count-verifiable without entering prose |

**Composite: 60 + 30 + (26 × 5) = 60 + 30 + 130 = 220 / 220**
All essential: PASS | Golden: YES
V-02 + V-03 orthogonality confirmed: neither C-33 fix interferes with C-34 satisfaction and vice versa; combining them is strictly additive.

---

### V-05 — Role sequence + all axes: three-role pipeline with C-33 + C-34

| ID | Band | Result | Evidence |
|----|------|--------|----------|
| C-01–C-05 | Essential | **PASS** (×5) | Inherited |
| C-06–C-08 | Recommended | **PASS** (×3) | Inherited |
| C-09–C-32 | Aspirational | **PASS** (×24) | Inherited — V-05 inherits from R11 V-05 baseline; role pipeline carries through |
| **C-33** | Aspirational | **PASS** | Format Analyst (Role 1) produces the inertia annotation header with "3 fields: Failure mode prevented \| Gap above C-25 \| Concrete example (C-29, C-30):" as a FORMAT CONTRACT deliverable. "FORMAT CONTRACT COMPLETE" is stated before Role 2 activates, locking the field-count header; Role 2 (Domain Expert) and Role 3 cannot modify the contract. C-33 compliance is enforced by role architecture rather than by inline instruction proximity |
| **C-34** | Aspirational | **PASS** | Consequence Analyst (Role 3) entry is gated by the TYPE SCAN GATE result. The TYPE SCAN GATE section in Role 3's activation carries "*Gate-present audit method — 5 observables:*" and "*Gate-absent signature — 1 observable:*" at the path-identifier level — identical text to V-04 but now appearing as a role-boundary condition. The count declarations are the gate's structural form rather than an inline note; they appear at the architectural seam that determines Role 3 activation |

**Composite: 60 + 30 + (26 × 5) = 60 + 30 + 130 = 220 / 220**
All essential: PASS | Golden: YES
Delta over V-04: same text, same point total — structural enforcement mechanism is architectural (role-locked) vs. instructional (inline). V-05 is the hardened form of V-04; both achieve 220.

---

### Score Summary

| Variation | C-33 | C-34 | Essential | Composite | Golden |
|-----------|------|------|-----------|-----------|--------|
| V-01 | FAIL | FAIL | 5/5 PASS | 210 / 220 | YES |
| V-02 | PASS | FAIL | 5/5 PASS | 215 / 220 | YES |
| V-03 | FAIL | PASS | 5/5 PASS | 215 / 220 | YES |
| **V-04** | **PASS** | **PASS** | 5/5 PASS | **220 / 220** | YES |
| **V-05** | **PASS** | **PASS** | 5/5 PASS | **220 / 220** | YES |

**Rank:** V-04 = V-05 (220) > V-02 = V-03 (215) > V-01 (210)

---

### Excellence Signals (from V-04 / V-05)

**Signal 1 — Count-first annotation header (C-33 pattern)**
The form "N fields: name1 | name2 | nameN" at the annotation header converts field-set completeness verification from a criterion-matching body-read to a count-scan at the header line. The auditor sees "3", counts three pipe-delimited names, and is done. The body's content is irrelevant to the completeness check. This is the annotation analog of the closed-register pattern: the header declares the set size; the body carries the values; completeness is verifiable without reading the values.

**Signal 2 — Path-label observable count (C-34 pattern)**
Moving the count from description prose to the italic path-identifier line applies the closed-register closure pattern to observable sets. "*Gate-present audit method — 5 observables:*" declares the set size at the same level as the path name; an auditor counts items in the numbered list against the declared number without entering the prose. The absent-path form "*Gate-absent signature — 1 observable:*" closes a one-item set. Both directions are closed and count-scannable.

**Signal 3 — Orthogonality of C-33 and C-34 (confirmed by V-02/V-03 isolation)**
C-33 operates entirely in Section B (annotation header). C-34 operates entirely in the TYPE SCAN GATE audit test. The two transforms share no structural elements and do not interact: V-02 proves C-33 passes without C-34 and V-03 proves C-34 passes without C-33. Combining them in V-04 is strictly additive; no composite interaction risks.

**Signal 4 — Role-architecture enforcement of count declarations (V-05 over V-04)**
V-05 places C-33 compliance as a FORMAT CONTRACT deliverable (Format Analyst closes the contract with "FORMAT CONTRACT COMPLETE" before Role 2 activates) and C-34 compliance at the TYPE SCAN GATE role boundary (Consequence Analyst's gate entry condition carries the count labels). The count declarations are not inline instructions that an executor may skip — they are role handoff conditions. This is the hardened form: structural enforcement ensures the count declarations survive role transitions without reliance on instruction-following discipline.

---

```json
{"top_score": 220, "all_essential_pass": true, "new_patterns": ["Count-first annotation header: N fields: name1 | name2 | nameN at header line enables count-scan completeness verification without reading annotation body — annotation analog of closed-register pattern", "Path-label observable count: N observables: on italic path-identifier line closes observable enumeration — applies C-27 closed-register pattern to audit observable sets making completeness verifiable by count-scan without entering description prose", "Role-architecture count locking: placing C-33 field-count header as FORMAT CONTRACT deliverable and C-34 observable counts at TYPE SCAN GATE role boundary enforces count declarations architecturally rather than instructionally"]}
```
