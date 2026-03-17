Now I have everything needed to score all five variations. Let me produce the full scorecard.

---

## Round 17 Scorecard — corps-committee

### Rubric version: v17 | Denominator: 40 | Weight per criterion: 2.5 pts

---

### Per-Criterion Assessment

**Baseline inheritance:** All five variations are built on the R16 V-04 baseline. C-01 through C-45 (37 prior criteria) are evaluated identically across all variations. Key checks:

| Criterion | Basis | All Variations |
|-----------|-------|----------------|
| C-01 | Committee type labels declared | PASS |
| C-02 | Role voice compliance + STANCE token guard | PASS |
| C-04 | Action item owner enforcement | PASS |
| C-05 | Dissenting opinion per CONDITION/BLOCK | PASS |
| C-07 | Vague Tier 2 condition rejected | PASS |
| C-23 | Owner + Trigger when verdict not APPROVED | PASS |
| C-25 | TIER-N-SEQUENCE-COMMIT present | PASS |
| C-27 | Full token labels in INERTIA-FINDING | PASS |
| C-30/C-33/C-34 | AMEND routing + RECOMMIT MANIFEST | PASS |
| C-35 | Explicit closed-set manifest at PHASE-1-COMMIT | PASS — skeleton and fill rules both enforce |
| C-36 | 4-row CONFIRMATION; three-way vocabulary | PASS |
| C-37 | Dual-mechanism C-02 and C-04 enforcement | PASS — ROLE VOICE GUARD + TIER-N-SEQUENCE-COMMIT; OWNERSHIP TALLY |
| C-38 | FAILS [C-NN] positional syntax required | PASS — template states malformed examples |
| C-39 | REQUIRES: C-35 annotation before TOKEN TRACE fill rule | PASS — present in all variations |
| C-40 | Template carries self-referential entries for C-38/C-39 | PASS — CORRECT entries for C-38, C-39 present |
| C-41 | Forward annotation at PHASE-1-COMMIT referencing C-36 | PASS — "[This explicit closed set is the prerequisite for C-36 TOKEN TRACE CONFIRMATION row count = 4]" present in skeleton |
| C-42 | BEFORE YOU START: all imperative, no descriptive sentences | PASS — all BYS lines are conditional imperatives; parentheticals clarify scope, not explain purpose |
| C-43 | TOKEN TRACE fill rules echo C-41 annotation | PASS — C-41 ECHO block present with three-point traceability |
| C-44 | FAILS template carries CORRECT entries for C-42 and C-43 | PASS — both present in all variations |
| C-45 | CO-DEPENDENCY PREAMBLE declares C-43/C-41 three-leg row | PASS — full chain "C-39 at consumption → C-41 at source → C-43 in fill rules" present in all preambles |

**Prior 37 criteria: all PASS across all five variations.**

---

### R17 Discriminator Criteria (C-46, C-47, C-48)

#### V-01 — FAILS Template Recursive Currency Extension (C-46 only)

| Criterion | Evidence | Result |
|-----------|----------|--------|
| **C-46** | FAILS template carries CORRECT entries for C-44 and C-45 at lines 88–92. Text: "FAILS [C-44]: FAILS template omits CORRECT entry for C-42 or C-43..." and "FAILS [C-45]: CO-DEPENDENCY PREAMBLE omits C-43/C-41 three-leg row..." — exactly the recursive currency pattern. | **PASS** |
| **C-47** | BEFORE YOU START has no pre-flight halt for FAILS template currency. BYS block ends at "Do not begin the skeleton until every line above is read." — no check for template staleness at session-open. | **FAIL** |
| **C-48** | BEFORE YOU START has no pre-flight halt for CO-DEPENDENCY PREAMBLE completeness. No check for three-leg row presence at session-open. | **FAIL** |

**V-01 score: 38/40 = 95.0**

---

#### V-02 — BEFORE YOU START C-44 Pre-Flight Halt (C-47 only)

| Criterion | Evidence | Result |
|-----------|----------|--------|
| **C-46** | FAILS template identical to baseline: C-42/C-43 CORRECT entries present; C-44/C-45 CORRECT entries absent. Variation explicitly notes: "C-44/C-45 CORRECT entries absent. C-46 not satisfied." | **FAIL** |
| **C-47** | BYS carries: "If the FAILS SYNTAX TEMPLATE omits CORRECT examples for any aspirational criterion pair added after C-39 (i.e., C-42, C-43, or any later pair): template not current; C-44 miss. Halt. [C-47]" — imperative, tagged, fires before skeleton is printed. | **PASS** |
| **C-48** | BYS has no CO-DEPENDENCY PREAMBLE pre-flight. Variation explicitly notes: "C-48 is NOT satisfied." | **FAIL** |

**V-02 score: 38/40 = 95.0**

---

#### V-03 — BEFORE YOU START C-45 Pre-Flight Halt (C-48 only)

| Criterion | Evidence | Result |
|-----------|----------|--------|
| **C-46** | FAILS template identical to baseline — no C-44/C-45 CORRECT entries. Variation notes: "C-46 not satisfied." | **FAIL** |
| **C-47** | BYS has no FAILS template currency pre-flight. Variation explicitly notes: "C-47 is NOT satisfied." | **FAIL** |
| **C-48** | BYS carries: "If the CO-DEPENDENCY PREAMBLE omits the C-43/C-41 three-leg row: full traceability chain not declared as a unit; C-45 not satisfied. Halt. [C-48]" — imperative, tagged, fires before skeleton is printed. | **PASS** |

**V-03 score: 38/40 = 95.0**

---

#### V-04 — Combination: C-46 + C-47

| Criterion | Evidence | Result |
|-----------|----------|--------|
| **C-46** | FAILS template carries CORRECT entries for C-44 and C-45 (lines 835–839) — identical to V-01. Recursive currency satisfied. | **PASS** |
| **C-47** | BYS carries: "If the FAILS SYNTAX TEMPLATE omits CORRECT examples for any aspirational criterion pair added after C-39 (i.e., C-42, C-43, or any later pair): template not current; C-44 miss. Halt. [C-47]" — same text as V-02. Pre-flight fires at session-open. | **PASS** |
| **C-48** | BYS has no CO-DEPENDENCY PREAMBLE pre-flight. Variation explicitly notes: "C-48 is NOT satisfied." | **FAIL** |

**Note on C-47 text:** V-04's C-47 pre-flight still cites "C-44 miss" though the template now satisfies C-46. The pre-flight is functional — it would halt a stale template — but the citation is slightly behind the rubric evolution (C-46, not C-44, is now the governing criterion for currency of C-44/C-45 entries). C-47 is PASS (the mechanism fires), but this is a latent precision gap.

**V-04 score: 39/40 = 97.5**

---

#### V-05 — Full Integration: C-46 + C-47 + C-48

| Criterion | Evidence | Result |
|-----------|----------|--------|
| **C-46** | FAILS template carries CORRECT entries for C-44 and C-45 (lines 928–932) — and additionally carries self-referential entries for C-46, C-47, C-48 (lines 933–941). Recursive currency not only satisfied but extended to the C-46/C-47/C-48 triplet itself. | **PASS** |
| **C-47** | BYS carries: "If the FAILS SYNTAX TEMPLATE omits CORRECT examples for any aspirational criterion pair added after C-39 (i.e., C-42, C-43, C-44, C-45, or any later pair): template not current; C-46 miss. Halt. [C-47]" — updated from V-04's "C-44 miss" to "C-46 miss," naming C-44/C-45 in the pair list. Pre-flight citation stays current with rubric evolution. | **PASS** |
| **C-48** | BYS carries: "If the CO-DEPENDENCY PREAMBLE omits the C-43/C-41 three-leg row: full traceability chain not declared as a unit; C-45 not satisfied. Halt. [C-48]" — imperative, tagged, fires independently of C-47 check. | **PASS** |

**V-05 score: 40/40 = 100.0**

---

### Composite Scores + Ranking

| Rank | Variation | C-01–C-45 | C-46 | C-47 | C-48 | Score | Golden? |
|------|-----------|-----------|------|------|------|-------|---------|
| 1 | **V-05** Full integration | 37/37 | PASS | PASS | PASS | **100.0** | YES |
| 2 | **V-04** C-46 + C-47 | 37/37 | PASS | PASS | FAIL | **97.5** | YES |
| 3 | **V-01** C-46 only | 37/37 | PASS | FAIL | FAIL | **95.0** | — |
| 3 | **V-02** C-47 only | 37/37 | FAIL | PASS | FAIL | **95.0** | — |
| 3 | **V-03** C-48 only | 37/37 | FAIL | FAIL | PASS | **95.0** | — |

---

### Excellence Signals — V-05

**1. Version-aware pre-flight citations.** V-04's C-47 pre-flight cites "C-44 miss" after C-46 has been satisfied — accurate mechanically but stale conceptually. V-05 updates the citation to "C-46 miss" and expands the aspirational pair list to include C-44 and C-45. When a new criterion pair extends an existing one, the pre-flight text must evolve to reference the successor criterion, not the predecessor.

**2. Recursive forward maintenance applied to the C-46/C-47/C-48 triplet itself.** V-05 doesn't stop at adding entries for C-44/C-45 (what C-46 strictly requires). It adds CORRECT entries for C-46, C-47, and C-48 as well. The template is not just current for C-44/C-45 — it is current for every aspirational criterion that has been named, including the three introduced in this round. The FAILS template becomes self-describing one level further.

**3. Defense in depth: three independent detection layers.** Remove any one mechanism and a gap reopens: remove C-46 entries and a C-44/C-45 violation loses its canonical citation; remove C-47 and template staleness is invisible until the reviewer inspects the template directly; remove C-48 and a preamble gap is invisible until the reviewer reaches STEP 2. V-05 is the only variation where all three mechanisms fire independently. V-04 closes two gaps but leaves preamble staleness latent.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["version-aware pre-flight citations update criterion reference from predecessor to successor when a new criterion extends the prior one", "recursive forward maintenance of FAILS template applies to the governing criteria triplet itself, not only the criteria being governed"]}
```
