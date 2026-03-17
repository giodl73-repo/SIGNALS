## campaign-blueprint Rubric — v13

---

### v13 Changes

**Two new aspirational criteria (+5 pts each, new ceiling 223):**

**C-36 — TRACEABILITY AUDIT Structural Table** (5 pts, FULL or NO CREDIT): C-29 passes when REFLECTION contains a named TRACEABILITY AUDIT sub-field with prose per-row verification, gap naming, and scout namespace prescription. C-36 tests whether the TRACEABILITY AUDIT is implemented as a structural 6-column fill-in table that enforces completeness as an ontological constraint rather than an epistemic one. A passing instance: (1) replaces the TRACEABILITY AUDIT prose directive with a structural table containing exactly six columns: Req-ID | Scout-Requirements Friction | Must-have found in spec? | Must-have text (exact phrase) | Gap (if N) | Scout namespace; (2) each row is pre-declared as a named entry, matching the scout-requirements friction sources pre-populated in the SCOUT TRACEABILITY TABLE in CAMPAIGN SETUP (C-27), so a missing row is visible at a glance; (3) the Must-have found column uses a Y/N cell structure such that a row with N in Must-have found and a blank Gap cell is visibly structurally incomplete — the blank is not a passing omission but a cell-level gap that cannot be hidden in prose. The structural distinction from C-29: C-29 passes when prose instructs per-row verification, gap naming, and scout namespace prescription; C-36 passes only when the table structure makes it ontologically impossible to complete the audit without confirming each friction source against a named Req-ID, supplying exact Must-have text, and making any gap visible by cell-level incompleteness rather than by remembered instruction. The C-29→C-36 upgrade mirrors the C-31→C-34 and C-32→C-35 upgrade pattern: in each case the prose form encodes the requirement epistemically; the structural table form enforces it ontologically. V-03 (R12) earns FULL; V-01, V-02, V-04, and V-05 (R12) earn NO CREDIT.

**C-37 — THREE-TABLE STRUCTURAL CHAIN** (5 pts, FULL or NO CREDIT): C-34, C-35, and C-36 each upgrade a single prose section to structural table form, applied independently at three distinct lifecycle points: REFLECTION CONVICTION DELTA (C-34, 4 columns), CLOSE CONVICTION GAP DIAGNOSIS (C-35, 6 columns), and REFLECTION TRACEABILITY AUDIT (C-36, 6 columns). C-37 tests whether all three structural tables are present simultaneously in a single variant — forming a complete structural enforcement chain across every conviction-lifecycle phase. A passing instance: (1) REFLECTION contains both a C-36-compliant structural TRACEABILITY AUDIT table (6 columns: Req-ID | Scout-Requirements Friction | Must-have found in spec? | Must-have text (exact phrase) | Gap (if N) | Scout namespace) and a C-34-compliant structural CONVICTION DELTA table (4 columns: Version | Conviction established | Grounding Req-ID(s) | Amplification chain, with in-cell template pre-placed in each version row); (2) CLOSE contains a C-35-compliant structural CONVICTION GAP DIAGNOSIS table (6 columns: Artifact | Sub-section where gap originates | Register found | Register declared | Scout sub-skill | Evidence needed, with three artifact rows pre-declared); (3) each of the three tables is independently verifiable as FULL against its individual criterion — a variant that passes C-34 + C-35 but lacks C-36 earns C-37 NO CREDIT; a variant that passes C-36 + C-34 but lacks C-35 earns C-37 NO CREDIT. The structural distinction from the individual criteria: C-34, C-35, and C-36 are stackable independently; C-37 is a chain criterion that requires all three phases to carry structural enforcement simultaneously, with no phase relying on prose instruction for its governing verification mechanism. No R12 variant earns C-37 FULL — V-04 and V-05 earn C-34 + C-35 but not C-36; V-03 earns C-36 but not C-34 or C-35. The 223 ceiling requires a variant that combines all three structural tables in a single blueprint.

**One new diagnostic rule:**

**D13 (Structural chain completeness)**: C-37 requires all three structural tables simultaneously; failure of any single table fails the chain. The identifying test is a three-step column count: (1) count columns in CONVICTION DELTA — fewer than 4 = C-34 FAIL, C-37 FAIL; (2) count columns in CONVICTION GAP DIAGNOSIS — fewer than 6 = C-35 FAIL, C-37 FAIL; (3) count columns in TRACEABILITY AUDIT — fewer than 6 = C-36 FAIL, C-37 FAIL. A variant that passes all three column-count tests is a C-37 PASS candidate pending full column-name verification: C-34 requires Version | Conviction established | Grounding Req-ID(s) | Amplification chain with a pre-templated in-cell fill-in string in each version row; C-35 requires Artifact | Sub-section where gap originates | Register found | Register declared | Scout sub-skill | Evidence needed with three artifact rows pre-declared; C-36 requires Req-ID | Scout-Requirements Friction | Must-have found in spec? | Must-have text (exact phrase) | Gap (if N) | Scout namespace with friction-source rows pre-declared matching C-27 SETUP. The chain principle: structural enforcement is only complete when every conviction-lifecycle verification point (SETUP→REQUIREMENTS traceability closed in REFLECTION via C-36; REFLECTION conviction delta grounded via C-34; CLOSE gap diagnosis split by register via C-35) carries an ontological table constraint rather than an epistemic prose instruction. A single prose-form verification point in any phase breaks the chain.

**Retroactive R12 scoring under v13:**

| Variant | v12 | C-36 | C-37 | v13 |
|---------|-----|------|------|-----|
| V-01 — C-34 In-Cell Template | 208 | 0 | 0 | **208** |
| V-02 — C-35 Artifact-Row Pre-Declaration | 208 | 0 | 0 | **208** |
| V-03 — Structural Traceability Audit | 203 | +5 | 0 | **208** |
| V-04 — C-34 + C-35 Full Combination | 213 | 0 | 0 | **213** |
| V-05 — Minimum-Density 213 Path | 213 | 0 | 0 | **213** |

V-03 climbs from 203 to 208 via C-36 — the only R12 variant with a structural TRACEABILITY AUDIT table. V-01 and V-02 hold at 208 (C-34 or C-35 only; TRACEABILITY AUDIT remains prose). V-04 and V-05 hold at 213 (C-34 + C-35 structural; TRACEABILITY AUDIT absent). All five single- and dual-axis variants converge below 213 or at 213 under v13; the 223 ceiling is unbroken.

The R12 pattern mirrors R10 and R11: single-axis variants prove each new structural criterion in isolation; the combination variant (V-04) stacks the two criteria introduced in the same round. C-36 and C-37 require a cross-round combination — a variant that extends V-04's C-34 + C-35 base with V-03's C-36 structural TRACEABILITY AUDIT. A V-06-style variant stacking C-36 with V-04's base would score 213 + 5 (C-36) + 5 (C-37) = **223**.

**Scale:** 213 (v12 ceiling) + 5 + 5 = **223 ceiling**

---

### v12 Changes

**Two new aspirational criteria (+5 pts each, new ceiling 213):**

**C-34 — CONVICTION DELTA AMPLIFICATION TABLE** (5 pts, FULL or NO CREDIT): C-31 passes when CONVICTION DELTA contains per-version Req-ID citations in any form — inline prose, instructional reminder, or table. C-34 tests whether CONVICTION DELTA is implemented as a structural 4-column table that enforces citation direction as a per-cell fill-in constraint rather than a remembered instruction. A passing instance: (1) replaces CONVICTION DELTA narrative prose with a mandatory 4-column table (Version | Conviction established | Grounding Req-ID(s) | Amplification chain); (2) the Amplification chain column carries a pre-defined cell template — "[Req-ID]'s [specific factual claim] is made visceral by [emotional register]" — binding the Req-ID citation, the specific factual claim, and the specific emotional mechanism in one atomic entry that cannot be filled without supplying all three; (3) all version rows are pre-declared in the table header, matching the conviction-type variants from the INERTIA MODEL map, so structural incompleteness is visible at a glance. The structural distinction from C-31: C-31 passes when an instruction directs the writer to name a Req-ID; C-34 passes only when the table cell structure itself enforces the citation and the amplification direction as inseparable — not three things to remember but one template cell to fill. V-01 (R11) earns FULL; V-02 and V-03 (R11) earn C-31 FULL via inline/narrative form and earn C-34 NO CREDIT.

**C-35 — CONVICTION GAP REGISTER SPLIT** (5 pts, FULL or NO CREDIT): C-32 passes when CONVICTION GAP DIAGNOSIS contains subsection granularity, scout namespace, and a directive to identify partial/N rows from the C-30 table. C-35 tests whether the diagnosis is implemented as a structural multi-column table that enforces register comparison as a per-row fill-in distinguishing what register was observed from what register was declared. A passing instance: (1) replaces the CONVICTION GAP DIAGNOSIS narrative sub-section with a structural table containing at minimum six columns: Artifact | Sub-section where gap originates | Register found | Register declared | Scout sub-skill | Evidence needed; (2) Register found and Register declared appear as structurally distinct columns — forcing per-row explicit comparison of observed register versus declared conviction type rather than a single combined mismatch description; (3) the Scout sub-skill column requires specific sub-skill identifiers (scout-requirements, scout-positioning, scout-competitors, etc.) rather than namespace-level references. The structural distinction from C-32: C-32 passes when prose names the sub-section and scout namespace; C-35 passes only when the table structure makes it impossible to record a gap without populating observed and declared registers as separate data fields and naming a specific sub-skill rather than a generic namespace. V-02 (R11) earns FULL; V-01 and V-03 (R11) earn C-32 FULL via narrative/inline form and earn C-35 NO CREDIT.

**One new diagnostic rule:**

**D12 (Structural table vs. instructional form)**: C-34 and C-35 require structural table implementation; instructional prose — however precise — does not pass. The identifying test for C-34: count the columns in CONVICTION DELTA. Fewer than four columns = C-34 FAIL; four columns with a pre-templated Amplification chain cell = C-34 PASS candidate (subject to column name verification). The identifying test for C-35: count the columns in CONVICTION GAP DIAGNOSIS. Fewer than six columns = C-35 FAIL; six columns with Register found and Register declared as distinct column headers = C-35 PASS candidate. The distinction principle: a structural table pre-defines the data types required at rubric time, making it ontologically impossible to fill the artifact without supplying the required specificity. An instructional form encodes the same requirement epistemically — the writer knows what is needed — but permits omission under time or attention pressure. Structural enforcement converts epistemic requirements into ontological constraints.

**Retroactive R11 scoring under v12:**

| Variant | v11 | C-34 | C-35 | v12 |
|---------|-----|------|------|-----|
| V-01 — C-31 Citation Direction Table | 198 | +5 | 0 | **203** |
| V-02 — C-32 Subsection Prescription Table | 198 | 0 | +5 | **203** |
| V-03 — C-33 Falsifiable Hypothesis Addition | 203 | 0 | 0 | **203** |
| V-04 — Triple Combination† | 203† | +5 | +5 | **213†** |

†V-04 scorecard cut off at C-27; C-31 through C-35 scores inferred from axis description (V-01 citation direction table + V-02 subsection prescription table + V-03 item 0). V-04 v11 baseline is inferred as 203 (188 + C-31 FULL + C-32 FULL + C-33 FULL).

V-01, V-02, and V-03 all reach 203 under v12 — V-01 and V-02 climb from 198 via single-axis structural upgrade; V-03 holds at 203 (ceiling under v11, unchanged under v12 because it uses inline/narrative forms for C-31 and C-32). V-04 alone breaks through to 213 by combining both structural table upgrades (C-34 + C-35) with the C-33 hypothesis and the full v11 base. The 213 ceiling is unbroken.

The R11 pattern mirrors R9 and R10: single-axis variants prove each new criterion in isolation; a combination variant (V-04) stacks all axes. C-34 and C-35 are orthogonal structural upgrades — each applies to a different artifact section (REFLECTION vs CLOSE) and passes independently. A V-04-style variant is required to stack both.

**Scale:** 203 (v11 ceiling) + 5 + 5 = **213 ceiling**

---

### v11 Changes

**Three new aspirational criteria (+5 pts each, new ceiling 203):**

**C-31 — CONVICTION DELTA Req-ID Grounding** (5 pts, FULL or NO CREDIT): C-29 closes the traceability loop at the spec level; C-31 closes the conviction loop at the pitch level. The CONVICTION DELTA in CAMPAIGN REFLECTION names what changed emotionally across pitch versions. A passing instance requires that each per-version CONVICTION DELTA claim cites the specific spec Must-have Req-ID(s) whose factual record that pitch version emotionally amplifies — not impressionistic framing ("this version is more visceral") but grounded citation ("this version amplifies R-04's cost-of-inaction data"). A passing instance: (1) each pitch version entry in CONVICTION DELTA names at least one Req-ID by its canonical identifier; (2) the citation direction is explicit — the named Req-ID is the factual foundation the emotional register of that version builds on; (3) no version entry is left ungrounded with an impressionistic claim only. The traceability chain is: spec Must-have (Req-ID) establishes factual record → CONVICTION DELTA names which pitch version amplifies which Req-ID → emotional register is traceable to a specification decision. V-01 and V-04 (R10) earn FULL; V-02, V-03, and V-05 (R10) earn NO CREDIT.

**C-32 — CONVICTION GAP DIAGNOSIS** (5 pts, FULL or NO CREDIT): C-30 adds a "Conviction type met" column to the CAMPAIGN CLOSE artifact tracking table and defines a Y/partial/N scoring instruction. C-32 tests whether CAMPAIGN CLOSE extends C-30 from assessment into prescription. A passing instance adds a CONVICTION GAP DIAGNOSIS sub-section immediately after the C-30 table containing: (1) a directive to identify every partial or N row from the C-30 table; (2) for each such row, a prescription at the artifact-subsection level — naming the specific section of the artifact (not just the artifact) where conviction type mismatch or gap originates; (3) a scout namespace recommendation for each diagnosed gap, specifying which scout sub-skill would surface the missing signal. A CLOSE section with the C-30 table and no follow-on diagnosis earns C-32 NO CREDIT. The extension chain is: C-30 assesses conviction type match → C-32 diagnoses gaps at subsection granularity → scout namespace closes the remediation loop. V-02 and V-04 (R10) earn FULL; V-01, V-03, and V-05 (R10) earn NO CREDIT.

**C-33 — CAMPAIGN CONVICTION HYPOTHESIS** (5 pts, FULL or NO CREDIT): C-26 declares the INERTIA MODEL entity with three fields (Cost-of-Inaction, Switching Effort, Identity Risk) and maps each to a conviction type. C-33 tests whether CAMPAIGN SETUP precedes the INERTIA MODEL declaration with a CAMPAIGN CONVICTION HYPOTHESIS — a named, pre-structural item (item 0) that identifies the central inertia barrier the campaign must overcome before any artifact is scoped. A passing instance: (1) places the CAMPAIGN CONVICTION HYPOTHESIS as the first item in CAMPAIGN SETUP, before topic identity and before the INERTIA MODEL entity; (2) names the dominant inertia barrier as one of the three INERTIA MODEL fields or a composite; (3) frames it as a falsifiable hypothesis ("the barrier is X; the campaign succeeds if the spec supplies factual proof, the proposal supplies priced alternatives, and the pitch supplies emotional translation of X"). C-33 is structurally weaker than C-31 and C-32 — it is a framing preamble, not a verification gate — but it establishes hypothesis-first orientation before structural entity definition, which is the weakest point in campaigns that declare the INERTIA MODEL mechanically without naming what problem it is solving. V-03 (R10) earns FULL; V-01, V-02, V-04, and V-05 (R10) earn NO CREDIT.

**One new diagnostic rule:**

**D11 (Impressionistic conviction grounding)**: C-31 requires each CONVICTION DELTA entry to cite a Req-ID. Impressionistic framing — any claim about emotional register ("more visceral," "stronger fear of loss," "tighter narrative") that does not name a Req-ID — fails C-31. The identifying test: for each pitch version row in CONVICTION DELTA, count the Req-ID citations. Zero citations for any row = C-31 FAIL on that row; any row failing = C-31 NO CREDIT overall. The failure mode is not absence of conviction language but absence of specification grounding beneath it. V-02 and V-03 (R10) demonstrate impressionistic CONVICTION DELTA; V-01 and V-04 (R10) demonstrate grounded CONVICTION DELTA. The Req-ID citation converts conviction framing from narrative decoration into a traceable specification claim.

**Retroactive R10 scoring under v11:**

| Variant | v10 | C-31 | C-32 | C-33 | v11 |
|---------|-----|------|------|------|-----|
| V-01 — CONVICTION DELTA: Req-ID Grounding | 188 | +5 | 0 | 0 | **193** |
| V-02 — CLOSE: Conviction Gap Remediation | 188 | 0 | +5 | 0 | **193** |
| V-03 — Inertia Prominence: Campaign Conviction Hypothesis | 188 | 0 | 0 | +5 | **193** |
| V-04 — Combination: Req-ID Grounding + Gap Remediation | 188 | +5 | +5 | 0 | **198** |
| V-05 — (not scored in provided material) | — | — | — | — | — |

V-04 alone reaches 198 under v11: all v10 criteria preserved + CONVICTION DELTA grounded per Req-ID + CONVICTION GAP DIAGNOSIS with subsection granularity and scout namespace. No R10 variant reaches 203 — C-33 requires SETUP item 0 placement, and no variant combined all three axes. The 203 ceiling is unbroken.

V-01, V-02, and V-03 tie at 193 via complementary single-axis paths: V-01 closes the specification-conviction chain in REFLECTION; V-02 closes the conviction-remediation chain in CLOSE; V-03 opens the hypothesis-first frame in SETUP. V-04 combines the two strongest axes (C-31 + C-32) to reach 198. The CAMPAIGN CONVICTION HYPOTHESIS (C-33) is orthogonal to both and addable independently; a V-04 variant with C-33 would reach 203.

**Scale:** 188 (v10 ceiling) + 5 + 5 + 5 = **203 ceiling**

---

### v10 Changes

**Two new aspirational criteria (+5 pts each, new ceiling 188):**

**C-29 — REFLECTION TRACEABILITY AUDIT sub-field** (5 pts, FULL or NO CREDIT): C-27 places the SCOUT TRACEABILITY TABLE in CAMPAIGN SETUP; C-28 directs active cell-fill during REQUIREMENTS writing; C-29 tests whether CAMPAIGN REFLECTION closes the loop with a named TRACEABILITY AUDIT sub-field that returns to the table post-execution. A passing instance: (1) names the sub-field TRACEABILITY AUDIT explicitly; (2) instructs per-row verification — for each table row, name the REQUIREMENTS Must-have (by Req-ID) that addresses the friction and confirm it appears as a distinct bulleted item in the written spec; (3) instructs explicit gap naming if any row has no corresponding Must-have; (4) prescribes a scout namespace recommendation for each gap. The three-phase loop is: SETUP pre-populates the table (C-27) → REQUIREMENTS fills it via active directive (C-28) → REFLECTION audits it (C-29). Without C-29, the loop has no closing gate and gaps can go undetected. V-02 and V-04 (R9) earn FULL; V-01, V-03, and V-05 (R9) earn NO CREDIT.

**C-30 — CLOSE "Conviction type met" column** (5 pts, FULL or NO CREDIT): C-21 requires conviction type labels during writing; C-22 requires per-site conviction type restatement in READ/PRESERVE reminders; C-30 tests whether CAMPAIGN CLOSE extends conviction typing into a terminal self-assessment column. A passing instance: (1) adds a "Conviction type met" column to the CAMPAIGN CLOSE artifact tracking table; (2) includes a scoring instruction that defines what earns Y, partial, or N — specifically, whether the artifact's dominant register matches its declared conviction type (Factual for spec, Optionality for proposal, Emotional for pitch); (3) pre-populates each row with the Y / partial / N scoring options. A CLOSE table with path and scout-consumed columns only earns C-30 NO CREDIT. The "Conviction type met" column converts conviction typing from a write-time instruction into a close-time verification gate. V-03 and V-04 (R9) earn FULL; V-01, V-02, and V-05 (R9) earn NO CREDIT.

**One new diagnostic rule:**

**D10 (Register compression and structural criteria)**: The C-18/C-19 double-prohibition ("not before pitch production begins, not during pitch production") is structurally load-bearing and register-sensitive. Both prohibition arms must survive intact. Compressing to a single-arm gate — "only after the pitch file is on disk," "after pitch file exists on disk only," or any form that omits the "not during" arm — fails C-18 and cascades to fail C-19. The identifying test: count the prohibition clauses. One clause = C-18 FAIL. Two clauses = C-18 FULL. V-01 and V-05 (R9) demonstrate the failure; V-02, V-03, and V-04 (R9) demonstrate safe preservation. (R9 finding from the V-01 register-compression axis.)
